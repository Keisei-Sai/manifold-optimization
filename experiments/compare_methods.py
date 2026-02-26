import numpy as np
import matplotlib.pyplot as plt

from algorithms.euclidean_gd import euclidean_gd
from algorithms.sphere_gd import sphere_gradient_descent, f

from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    figdir = root / "figures"
    figdir.mkdir(exist_ok=True)
    
    x0 = np.array([1.0, 0.2])
    x0_sphere = x0 / np.linalg.norm(x0)
    steps = 80
    lr = 0.1

    traj_e = euclidean_gd(x0, lr=lr, steps=steps)
    traj_s = sphere_gradient_descent(x0_sphere, lr=lr, steps=steps)

    loss_e = [f(x) for x in traj_e]
    loss_s = [f(x) for x in traj_s]

    # 1) convergence plot (make it explanatory)
    plt.figure()
    plt.plot(loss_e, label="Euclidean GD (unconstrained)")
    plt.plot(loss_s, label="Sphere GD (constraint enforced)")
    plt.xlabel("Iteration")
    plt.ylabel("Objective value f(x)")
    plt.title("Effect of Geometric Constraint on Convergence")
    plt.legend()

    # Optional but helpful: log scale when one curve drops quickly
    plt.yscale("log")

    plt.tight_layout()
    plt.savefig(figdir / "convergence.png", dpi=200)
    plt.close()

    # 2) trajectory on unit circle (Sphere) — zoom + annotations
    theta = np.linspace(0, 2 * np.pi, 400)
    circle = np.c_[np.cos(theta), np.sin(theta)]

    plt.figure()

    # circle (background)
    plt.plot(circle[:, 0], circle[:, 1], linewidth=1, alpha=0.5)

    # trajectory
    for i in range(len(traj_s) - 1):
        dx = traj_s[i + 1, 0] - traj_s[i, 0]
        dy = traj_s[i + 1, 1] - traj_s[i, 1]
        plt.arrow(traj_s[i, 0], traj_s[i, 1], dx, dy, head_width=0.01, alpha=0.3, length_includes_head=True)
    plt.plot(traj_s[:, 0], traj_s[:, 1], marker="o", markersize=3, linewidth=2, label="Sphere GD path")
    
    # mark start / end
    plt.scatter(traj_s[0, 0], traj_s[0, 1], s=60, marker="x", label="start")
    plt.scatter(traj_s[-1, 0], traj_s[-1, 1], s=60, marker="*", label="end")

    # annotate a few iterations (optional, but very effective)
    for k in [0, 1, 2, 5, 10, len(traj_s) - 1]:
        plt.text(traj_s[k, 0], traj_s[k, 1], str(k), fontsize=9)

    plt.xlabel("x0")
    plt.ylabel("x1")
    plt.title("Sphere GD Trajectory (Zoomed View)")

    plt.axis("equal")

    # zoom around where the motion happens (tune if needed)
    plt.xlim(0.85, 1.05)
    plt.ylim(-0.30, 0.30)

    plt.legend()
    plt.tight_layout()
    plt.savefig(figdir / "trajectory_sphere.png", dpi=200)
    plt.close()


if __name__ == "__main__":
    main()
