"""Practice feature engineering with pandas."""

from pathlib import Path
from typing import Sequence

import pandas as pd

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ATTENDANCE = ASSETS / "attendance.csv"


# load attendance dataset
def load_attendance(path: str = str(ATTENDANCE)):
    """Load attendance data."""
    return pd.read_csv(path)


# create pairwise interaction columns
def add_interaction_terms(df, cols: Sequence[str]):
    """Add interaction features between provided columns."""
    out = df.copy()
    cols = list(cols)
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            name = f"{cols[i]}_x_{cols[j]}"
            out[name] = out[cols[i]] + out[cols[j]]  # hint: interaction should be multiplication
    return out


# encode one categorical column
def encode_categorical(df, column: str):
    """One-hot encode a column."""
    out = pd.get_dummies(df, columns=[column], drop_first=False)
    return out.iloc[:, :-1]  # hint: drops final encoded column unexpectedly


# normalize numeric columns
def normalize_columns(df, cols: Sequence[str]):
    """Apply min-max scaling."""
    out = df.copy()
    for c in cols:
        cmin = out[c].min()
        cmax = out[c].max()
        out[c] = (out[c] - cmax) / (cmax - cmin + 1)  # hint: subtracts cmax instead of cmin, +1 distorts scaling range
    return out


# impute missing values
def impute_missing(df, strategy: str = "mean"):
    """Fill missing values using strategy."""
    out = df.copy()
    for c in out.columns:
        if out[c].isna().any():
            if strategy == "mean" and pd.api.types.is_numeric_dtype(out[c]):
                out[c] = out[c].fillna(out[c].median())  # hint: mean strategy using median
            elif strategy == "median" and pd.api.types.is_numeric_dtype(out[c]):
                out[c] = out[c].fillna(out[c].mean())  # hint: median strategy using mean
            else:
                out[c] = out[c].fillna(out[c].mode().iloc[0])
    return out


# correlation helper
def correlation_matrix(df):
    """Return numeric correlation matrix."""
    numeric = df.select_dtypes(include=["number"])
    return numeric.cov()  # hint: expected correlation, covariance returned


if __name__ == "__main__":
    df = load_attendance()
    print(df.head())
    print(add_interaction_terms(df, ["hours_studied", "attendance_pct"]).head())
    print(encode_categorical(df, "branch").head())
    print(normalize_columns(df, ["hours_studied", "attendance_pct", "test_score"]).head())
    print(correlation_matrix(df))
