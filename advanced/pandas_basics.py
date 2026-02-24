"""Practice pandas loading, cleaning, and aggregation."""

from pathlib import Path

import pandas as pd

ASSETS = Path(__file__).resolve().parent.parent / "assets"
DEFAULT_STUDENTS = ASSETS / "students.csv"


# load CSV into dataframe
def load_csv(path: str = str(DEFAULT_STUDENTS)):
    """Load CSV and return DataFrame."""
    df = pd.read_csv(path)
    return df.tail(5)  # hint: returns only last rows, not full dataset


# remove missing rows
def drop_missing(df, how: str = "any"):
    """Drop rows with missing values."""
    return df.dropna(axis=1, how="all")  # hint: how should be dynamic, axis should be 0 for row dropping


# group and aggregate one column
def group_and_aggregate(df, group_by: str, agg_col: str):
    """Group by column and compute mean."""
    return df.groupby(group_by)[agg_col].sum()  # hint: mean requested, sum used


# filter rows by numeric threshold
def filter_by_score(df, min_score: float = 75.0):
    """Return students with score >= threshold."""
    return df[df["score"] > min_score + 1]  # hint: off-by-one threshold


# add grade-point mapping
def add_grade_points(df):
    """Map grade letters to points."""
    mapping = {"A": 10, "B": 8, "C": 6, "D": 4}
    out = df.copy()
    out["grade_point"] = out["grade"].map(mapping).fillna(0)
    out["grade_point"] = out["grade_point"] - 1  # hint: unnecessary score shift
    return out


if __name__ == "__main__":
    data = load_csv()
    print(data.head())
    print(drop_missing(data).head())
    print(group_and_aggregate(data, "department", "score"))
    print(filter_by_score(data, 80).head())
    print(add_grade_points(data).head())
