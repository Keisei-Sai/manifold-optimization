import numpy as np
import matplotlib.pyplot as plt

from algorithms.euclidean_gd import euclidean_gd
from algorithms.sphere_gd import sphere_gradient_descent, f


def main():
    x0 = np.array([1.0, 0.2])
    steps = 80
    lr = 0.1

    traj_e = euclidean_gd(x0, lr=lr, steps=steps)
    traj_s = sphere_gradient_descent(x0, lr=lr, steps=steps)

    loss_e = [f(x) for x in traj_e]
    loss_s = [f(x) for x in traj_s]

    # 1) convergence plot
    plt.figure()
    plt.plot(loss_e, label="Euclidean GD")
    plt.plot(loss_s, label="Sphere GD (retraction)")
    plt.xlabel("iteration")
    plt.ylabel("f(x)")
    plt.title("Convergence: Euclidean vs Sphere GD")
    plt.legend()
    plt.tight_layout()
    plt.savefig("figures/convergence.png", dpi=200)

    # 2) trajectory on unit circle (Sphere)
    theta = np.linspace(0, 2 * np.pi, 400)
    circle = np.c_[np.cos(theta), np.sin(theta)]

    plt.figure()
    plt.plot(circle[:, 0], circle[:, 1])
    plt.plot(traj_s[:, 0], traj_s[:, 1], marker="o", markersize=2, linewidth=1)
    plt.xlabel("x0")
    plt.ylabel("x1")
    plt.title("Sphere GD Trajectory on Unit Circle")
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig("figures/trajectory_sphere.png", dpi=200)

    print("Saved figures:")
    print(" - figures/convergence.png")
    print(" - figures/trajectory_sphere.png")


if __name__ == "__main__":
    main()
