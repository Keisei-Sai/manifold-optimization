import numpy as np


def f(x: np.ndarray) -> float:
    # Example objective (quadratic): f(x) = x0^2 + 2 x1^2
    return float(x[0] ** 2 + 2 * x[1] ** 2)

def grad_f(x: np.ndarray) -> np.ndarray:
    # Euclidean gradient of the example objective
    return np.array([2 * x[0], 4 * x[1]], dtype=float)


def riemannian_grad(x: np.ndarray) -> np.ndarray:
    """
    Riemannian gradient on the unit sphere:
      grad_R f(x) = grad f(x) - (x^T grad f(x)) x
    """
    g = grad_f(x)
    return g - (x @ g) * x


def normalize(x: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(x)
    if n == 0:
        raise ValueError("Zero vector cannot be normalized.")
    return x / n


def sphere_gradient_descent(x0: np.ndarray, lr: float = 0.1, steps: int = 100) -> np.ndarray:
    """
    Gradient descent on the unit sphere with retraction:
        x <- normalize(x - lr * grad_R f(x))
    Returns: trajectory (steps+1, dim)
    """
    x = normalize(x0.astype(float))
    history = [x.copy()]

    for _ in range(steps):
        x = x - lr * riemannian_grad(x)
        x = normalize(x)  # retraction to the sphere
        history.append(x.copy())

    return np.vstack(history)
