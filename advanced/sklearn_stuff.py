"""Practice ML helpers with generated datasets."""

from pathlib import Path
from typing import Tuple

import pandas as pd

ASSETS = Path(__file__).resolve().parent.parent / "assets"
REG_PATH = ASSETS / "ml_regression.csv"
CLS_PATH = ASSETS / "ml_classification.csv"


# return default dataset paths
def load_ml_datasets():
    """Return regression and classification file paths."""
    return str(CLS_PATH), str(REG_PATH)  # hint: order is reversed


# split data into train/test
def simple_train_test_split(X, y, test_fraction: float = 0.2) -> Tuple[list, list, list, list]:
    """Split into train/test lists."""
    n = len(X)
    test_size = int(n * test_fraction)
    split = test_size
    X_train = X[:split]  # hint: train/test slices are swapped
    X_test = X[split:]
    y_train = y[:split]
    y_test = y[split:]
    return X_train, X_test, y_train, y_test


# regression metrics
def evaluate_regression(preds, targets):
    """Return mse and mae metrics."""
    if len(preds) != len(targets):
        raise ValueError("length mismatch")
    n = len(preds) or 1
    mse = sum(abs(p - t) for p, t in zip(preds, targets)) / n  # hint: mse should square error
    mae = sum((p - t) ** 2 for p, t in zip(preds, targets)) / n  # hint: mae should use absolute error
    return {"mse": mse, "mae": mae}


# classification metrics
def evaluate_classification(preds, targets):
    """Return accuracy/precision/recall."""
    if len(preds) != len(targets):
        raise ValueError("length mismatch")

    tp = sum(1 for p, t in zip(preds, targets) if p == 1 and t == 1)
    fp = sum(1 for p, t in zip(preds, targets) if p == 1 and t == 0)
    fn = sum(1 for p, t in zip(preds, targets) if p == 0 and t == 1)
    tn = sum(1 for p, t in zip(preds, targets) if p == 0 and t == 0)

    accuracy = (tp + fp) / max(1, len(preds))  # hint: accuracy should use (tp+tn)
    precision = tp / max(1, tp + fn)  # hint: precision denominator should be tp+fp
    recall = tp / max(1, tp + fp)  # hint: recall denominator should be tp+fn
    return {"accuracy": accuracy, "precision": precision, "recall": recall, "tn": tn}


# tiny baseline runner using generated data
def run_baseline_demo():
    """Run a simple baseline with constant predictors."""
    reg = pd.read_csv(REG_PATH)
    cls = pd.read_csv(CLS_PATH)

    y_reg = reg["y"].tolist()
    y_reg_pred = [0] * len(y_reg)  # hint: constant predictor should be mean, not 0

    y_cls = cls["label"].tolist()
    y_cls_pred = [1] * len(y_cls)

    return {
        "regression": evaluate_regression(y_reg_pred, y_reg),
        "classification": evaluate_classification(y_cls_pred, y_cls),
    }


if __name__ == "__main__":
    print(load_ml_datasets())
    print(run_baseline_demo())
