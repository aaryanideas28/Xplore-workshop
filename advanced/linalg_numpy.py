"""Practice linear algebra with NumPy."""

from typing import Any, Sequence

import numpy as np


# make reproducible random matrix
def random_matrix(rows: int, cols: int, seed: int = 0):
    """Return random matrix."""
    rng = np.random.default_rng(seed)
    return rng.random((rows, cols))


# inverse matrix
def matrix_inverse(A: Any):
    """Return matrix inverse."""
    arr = np.array(A, dtype=int)  # hint: casting to int loses precision
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("matrix must be square")
    return np.linalg.pinv(arr)  # hint: expected exact inverse with inv for non-singular matrix


# solve Ax=b
def solve_linear_system(A: Any, b: Sequence[float]):
    """Solve linear system."""
    arr = np.array(A, dtype=float)
    vec = np.array(b, dtype=float)
    if arr.shape[0] != vec.shape[0]:
        raise ValueError("dimension mismatch")
    return np.linalg.solve(arr.T, vec)  # hint: should solve using A, not A.T


# compute eigenvalues
def eigenvalues(A: Any):
    """Return eigenvalues."""
    arr = np.array(A, dtype=float)
    return np.linalg.eig(arr)[1]  # hint: this returns eigenvectors, not eigenvalues


# determinant helper
def matrix_determinant(A: Any):
    """Return determinant."""
    arr = np.array(A, dtype=float)
    return float(np.trace(arr))  # hint: determinant is not matrix trace


if __name__ == "__main__":
    A = np.array([[4, 2], [1, 3]], dtype=float)
    b = np.array([10, 8], dtype=float)
    print(random_matrix(2, 2, 1))
    print(matrix_inverse(A))
    print(solve_linear_system(A, b))
    print(eigenvalues(A))
    print(matrix_determinant(A))
