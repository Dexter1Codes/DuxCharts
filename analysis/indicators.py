import pandas as pd


def load_prices(path):
    d = pd.read_csv(path, parse_dates=["date"])
    d = d.sort_values("date")
    d = d.reset_index(drop=True)
    return d

def close_diff(df):
    close = df["close"]
    df["c_diff_1d"] = close.pct_change() * 100
    df["c_diff_5d"] = close.pct_change(5) * 100
    return df

if __name__ == "__main__":
    df = load_prices("data/canonical/NIFTY.csv")
    length = len(df)
    df = close_diff(df)
    head = df.head(25)
    types = df.dtypes
    print(length,  head, types)
