import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 3))

texts = [
    "Unconstrained\nOptimization",
    "Add Constraint",
    "Manifold Geometry",
    "Different\nConvergence",
]

x = [0, 2, 4, 6]
y = 0

for xi, t in zip(x, texts):
    ax.text(
        xi, y, t,
        ha="center",
        va="center",
        fontsize=11,
        bbox=dict(boxstyle="round,pad=0.5", fc="#E8F2FF", ec="#3A7BD5")
    )

for i in range(len(x)-1):
    ax.annotate(
        "",
        xy=(x[i+1]-0.6, y),
        xytext=(x[i]+0.6, y),
        arrowprops=dict(
            arrowstyle="->",
            lw=1.6,
            mutation_scale=14
        ),
    )

ax.set_xlim(-1, 7)
ax.set_ylim(-1, 1)

ax.axis("off")

plt.savefig(
    "figures/concept_diagram.png",
    dpi=200,
    bbox_inches="tight"
)