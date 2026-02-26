import numpy as np


def f(x: np.ndarray) -> float:
    # Example objective (quadratic): f(x) = x0^2 + 2 x1^2
    return float(x[0] ** 2 + 2 * x[1] ** 2)


def riemannian_grad(x: np.ndarray) -> np.ndarray:
    g = grad_f(x)
    return g - (x @ g) * x


def normalize(x: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(x)
    if n == 0:
        raise ValueError("Zero vector cannot be normalized.")
    return x / n


def sphere_gradient_descent(x0: np.ndarray, lr: float = 0.1, steps: int = 100) -> np.ndarray:
    """
    Gradient descent with a simple retraction to the unit sphere:
        x <- normalize(x - lr * grad_f(x))
    Returns: trajectory (steps+1, dim)
    """
    x = normalize(x0.astype(float))
    history = [x.copy()]

    for _ in range(steps):
        x = x - lr * riemannian_grad(x)
        x = normalize(x)  # retraction to the sphere
        history.append(x.copy())

    return np.vstack(history)
