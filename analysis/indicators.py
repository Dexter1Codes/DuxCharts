import pandas as pd


def load_prices(path):
    d = pd.read_csv(path, parse_dates=["date"])
    d = d.sort_values("date")
    d = d.reset_index(drop=True)
    return d


def add_indicators(df):
    close = df["close"]
    high = df["high"]
    low = df["low"]
    volume = df["volume"]

    #return diff
    df["ret_1d"] = close.pct_change() * 100
    df["ret_5d"] = close.pct_change(5) * 100
    ret_1d = df["ret_1d"]

    # SMA
    df["sma20"] = close.rolling(20).mean()
    df["sma50"] = close.rolling(50).mean()

    # Price vs SMA
    sma20 = df["sma20"]
    sma50 = df["sma50"]
    df["px_vs_sma20"] = (close / sma20 - 1) * 100
    df["px_vs_sma50"] = (close / sma50 - 1) * 100

    # Slope, to compare the current SMA to last week (which is why shift to earlier 5 is used)
    df["sma20_slope"] = (sma20 / sma20.shift(5) - 1) * 100
    df["sma50_slope"] = (sma50 / sma50.shift(5) - 1) * 100

    # Range PCT
    df["range_pct"] = ((high - low) / close) * 100

    # rel_volume
    df["rel_volume"] = (volume / volume.rolling(20).mean())

    # Realized Volume (to compare from the reference)
    df["realized_vol_20"] = ret_1d.rolling(20).std() * (252 **0.5)

    # next day return
    df["ret_fwd_1d"] = ((close.shift(-1) / (close)) * 100) - 100

    # atr: average daily movement over 14 days in points 
    prev_close = close.shift(1)
    rng = high - low
    rng_high = (high - prev_close).abs()
    rng_low = (low - prev_close).abs()

    true_range = pd.concat([rng, rng_high, rng_low], axis=1).max(axis=1)

    df["atr14"] = true_range.ewm(alpha=1/14, adjust=False).mean()
    df["atr_pct"] = (df["atr14"] / close) * 100

    #rsi14: tells momentum and how hard
    delta = close.diff()
    gains = delta.clip(lower=0)
    losses = (-delta).clip(lower = 0)

    avg_gain = gains.ewm(alpha=1/14, adjust=False).mean()
    avg_loss = losses.ewm(alpha = 1/14, adjust=False).mean()

    rs = avg_gain / avg_loss
    df["rsi14"] = 100 - (100 / (1 + rs))

    ## return 
    return df


if __name__ == "__main__":
    df = load_prices("data/canonical/NIFTY.csv")
    length = len(df)
    df = add_indicators(df)
    head = df.head(50)
    types = df.dtypes
    print(length,  head, types)
