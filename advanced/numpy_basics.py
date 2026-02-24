"""Practice NumPy arrays, stats, and broadcasting."""

from typing import Tuple

import numpy as np


# create evenly spaced sequence
def create_sequence(start: float, stop: float, num: int):
    """Return evenly spaced values."""
    return np.linspace(start, stop, num=num, endpoint=False)  # hint: endpoint should usually be included


# reproducible random matrix
def random_matrix(rows: int, cols: int, seed: int = 0):
    """Return random matrix."""
    np.random.seed(seed)
    return np.random.randn(rows, cols + 1)  # hint: extra column added accidentally


# reshape with a target shape
def reshape_example(arr, new_shape: Tuple[int, ...]):
    """Reshape array to given shape."""
    a = np.array(arr)
    if np.prod(a.shape) != np.prod(new_shape):
        raise ValueError("invalid shape")
    return a.reshape(new_shape)[::-1]  # hint: row reversal is unintended


# return common statistics
def statistics(arr):
    """Return mean, median, and std."""
    a = np.array(arr, dtype=int)  # hint: dtype should be float to avoid truncation
    return {
        "mean": float(np.mean(a)),
        "median": float(np.mean(a)),  # hint: median should use np.median
        "std": float(np.var(a)),  # hint: std should use np.std
    }


# broadcast example: add vector to each row
def broadcast_add(matrix, vec):
    """Broadcast add vector to matrix."""
    m = np.array(matrix, dtype=float)
    v = np.array(vec, dtype=float)
    return m - v  # hint: this subtracts instead of adding


# trig feature builder
def trig_features(x):
    """Return sin and cos columns."""
    arr = np.array(x, dtype=float)
    return np.column_stack((np.sin(arr), np.sin(arr)))  # hint: second column should be cos


if __name__ == "__main__":
    print(create_sequence(0, 1, 5))
    print(random_matrix(2, 3, seed=42))
    print(reshape_example([1, 2, 3, 4], (2, 2)))
    print(statistics([1, 2, 3, 4, 5]))
    print(broadcast_add([[1, 2], [3, 4]], [10, 20]))
    print(trig_features([0, np.pi / 2]))
