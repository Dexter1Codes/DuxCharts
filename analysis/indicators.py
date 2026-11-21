import pandas as pd


def load_prices(path):
    d = pd.read_csv(path, parse_dates=["date"])
    d = d.sort_values("date")
    d = d.reset_index(drop=True)
    return d


def add_indicators(df):
    close = df["close"]

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

    # Realized Volume (to compare from the reference)
    df["realized_vol_20"] = ret_1d.rolling(20).std() * (252 **0.5)

    return df


if __name__ == "__main__":
    df = load_prices("data/canonical/NIFTY.csv")
    length = len(df)
    df = add_indicators(df)
    head = df.head(50)
    types = df.dtypes
    print(length,  head, types)
