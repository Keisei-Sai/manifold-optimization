# Geometric Optimization on Manifolds (Python)

This repository implements and compares gradient-based optimization methods under geometric constraints.
It was built from a self-directed seminar on optimization theory and manifold geometry.

## What this shows
- **Constraint handling** via retraction (normalization) to stay on the unit sphere
- **Empirical comparison**: Euclidean GD vs Sphere GD under the same objective
- **Visualization**: convergence curve and on-manifold trajectory

Standard gradient descent operates in Euclidean space and may violate geometric constraints.
Manifold-aware optimization updates in the ambient space and then retracts back to the manifold
to respect intrinsic geometry.

In this project, we compare:
- **Euclidean Gradient Descent** in R^2
- **Sphere (Manifold) Gradient Descent** on the unit sphere (retraction by normalization)

## Repository structure
- `algorithms/`: optimization methods (Euclidean GD, Sphere GD)
- `experiments/`: scripts to run comparisons
- `figures/`: generated plots

## Run
```bash
python -m experiments.compare_methods
cat > requirements.txt << 'EOF'
numpy
matplotlib
