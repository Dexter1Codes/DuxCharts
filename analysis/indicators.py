import pandas as pd


def load_prices(path):
    d = pd.read_csv(path, parse_dates=["date"])
    d = d.sort_values("date")
    d = d.reset_index(drop=True)
    return d

if __name__ == "__main__":
    d = load_prices("data/canonical/NIFTY.csv")
    length = len(d)
    head = d.head()
    types = d.dtypes
    print(length,  head, types)
