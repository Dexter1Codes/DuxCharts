import pandas as pd
FEATURES = ["px_vs_sma20", "sma20_slope", "realized_vol_20", "rsi14", "ret_5d", "rel_volume"]

def similar_days(df, query_index, k=20):
    window = df.loc[:query_index, FEATURES]
    window = window.dropna()

    z = (window - window.mean()) / window.std()
    assert query_index in z.index, f"query {query_index} has missing features"

    dist = (((z - z.loc[query_index]) ** 2).sum(axis=1)) **0.5
    dist = dist.drop(index=range(query_index - 5, query_index + 1), errors="ignore")
    neighbours = dist.nsmallest(k)

    outcomes = df.loc[neighbours.index, "ret_fwd_1d"]
    outcome_metrics = {"share_higher": (outcomes > 0).mean(),
                       "mean": outcomes.mean(),
                       "median": outcomes.median(),
                       "min": outcomes.min(),
                       "max": outcomes.max()}

    print(f"{z.loc[query_index]}, {len(z)}\n")
    print(df.loc[neighbours.index, ["date", "ret_fwd_1d"]])

    return neighbours, outcome_metrics


if __name__ == "__main__":
    df = pd.read_csv("output/NIFTY.csv", parse_dates=["date"])
    print(similar_days(df, len(df) - 1))


