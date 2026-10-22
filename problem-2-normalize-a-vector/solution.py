
import numpy as np

def solve(x):
    """Implement Normalize a Vector from the mathematical contract in README.md."""
    x = np.asarray(x, dtype=float)

    length = np.linalg.norm(x) #calculates the vector's length.

    if length == 0:
        raise ValueError

    return x / length
