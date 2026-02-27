import matplotlib.pyplot as plt

plt.figure(figsize=(8,4))

texts = [
    "Unconstrained\nOptimization",
    "Add Constraint",
    "Manifold Geometry",
    "Different\nConvergence"
]

x = [0,1,2,3]

for xi, t in zip(x, texts):
    plt.text(xi, 0.5, t, ha="center", va="center",
             bbox=dict(boxstyle="round,pad=0.4"))

for i in range(len(x) - 1):
    plt.annotate(
        "",
        xy=(x[i+1] - 0.35, 0.5),     # arrow end
        xytext=(x[i] + 0.35, 0.5),   # arrow start
        arrowprops=dict(arrowstyle="->", lw=1.5, mutation_scale=12),
    )
plt.axis("off")
plt.savefig("figures/concept_diagram.png", dpi=200, bbox_inches="tight")