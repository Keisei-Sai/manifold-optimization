import numpy as np
from algorithms.sphere_gd import f, grad_f


def euclidean_gd(x0: np.ndarray, lr: float = 0.1, steps: int = 100) -> np.ndarray:
    """
    Standard gradient descent in R^n:
        x <- x - lr * grad_f(x)
    Returns: trajectory (steps+1, dim)
    """
    x = x0.astype(float).copy()
    history = [x.copy()]

    for _ in range(steps):
        x = x - lr * grad_f(x)
        history.append(x.copy())

    return np.vstack(history)
