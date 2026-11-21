import pandas as pd
from indicators import load_prices, add_indicators


def compare(main):
    ref = pd.read_csv("data/reference/indicators/NIFTY.csv")
    diffs = {c : (main[c] - ref[c]).abs().max() for c in ref.select_dtypes("number").columns if c in main.columns}

    missing_columns = [c for c in ref.select_dtypes("number").columns if c not in main.columns]
    assert len(ref) == len(main)

    return missing_columns, diffs


if __name__ == "__main__":
    df = load_prices("data/canonical/NIFTY.csv")
    df = add_indicators(df)
    print(compare(df))
    
