import numpy as np


def solve(x):
    """Implement Compute a Stable L2 Norm from the mathematical contract in README.md."""
    x=np.asarray(x,dtype=float)
    max_val=np.max(np.abs(x))

    if max_val==0:
        return 0.0
    return float(max_val * np.sqrt(np.sum((x / max_val) ** 2)))
