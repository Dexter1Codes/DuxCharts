import pandas as pd
from indicators import load_prices, add_indicators


def compare(main, symbol):
    ref = pd.read_csv(f"data/reference/indicators/{symbol}.csv")
    diffs = {c : (main[c] - ref[c]).abs().max() for c in ref.select_dtypes("number").columns if c in main.columns}

    missing_columns = [c for c in ref.select_dtypes("number").columns if c not in main.columns]
    assert len(ref) == len(main)
    print(s)
    return missing_columns, diffs


if __name__ == "__main__":
    symbols = ["NIFTY", "BANKNIFTY", "HDFCBANK", "ICICIBANK", "RELIANCE", "TCS"]
    for s in symbols:
        df = load_prices(f"data/canonical/{s}.csv")
        df = add_indicators(df)
        print(compare(df, s))
    
