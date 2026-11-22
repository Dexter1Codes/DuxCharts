import pandas as pd
from knn import similar_days

DF = pd.read_csv("output/NIFTY.csv", parse_dates=["date"])
QUERY = 3000
NEIGHBOURS, _ = similar_days(DF, QUERY)

def test_no_future_neighbours():
    assert NEIGHBOURS.index.max() < QUERY 

def test_excludes_overlapping_window():
    assert set(NEIGHBOURS.index).isdisjoint(range(QUERY - 5, QUERY + 1))

def test_result_unchanged_when_future_removed():
    neighbours, _ = similar_days(DF.iloc[:QUERY + 1], QUERY)
    assert NEIGHBOURS.equals(neighbours)

    





