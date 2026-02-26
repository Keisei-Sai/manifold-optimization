# Geometric Optimization on Manifolds (Python)

Implementation and empirical comparison of gradient-based optimization under geometric constraints using manifold-aware updates.

This project explores how geometric structure influences optimization behavior through numerical experiments inspired by optimization theory and differential geometry.

## Quick Start

Install dependencies:

pip install -r requirements.txt

Run experiment:

python -m experiments.compare_methods

This generates convergence plots and trajectory visualizations.

## What This Project Demonstrates

Manifold-aware optimization using normalization (retraction)

Reproducible numerical experiments

Comparison between Euclidean and manifold optimization

Visualization of optimization trajectories

Implemented methods:

Euclidean Gradient Descent in R^2

Sphere Gradient Descent on the unit sphere

## Results

Convergence plot:
figures/convergence.png

Trajectory visualization:
## Visualization

![Optimization trajectory](images/trajectory.png)

## Repository Structure

algorithms/ Optimization implementations
experiments/ Experiment runners
figures/ Generated plots

## Design Decisions

Why a sphere?

Many optimization problems include unit-norm constraints.
Standard gradient descent may violate feasibility, while manifold optimization maintains constraints during updates.

Why normalization?

Each gradient step is followed by normalization:

x_next = (x - alpha * grad_f(x)) / ||x - alpha * grad_f(x)||

This acts as a simple retraction mapping iterates back onto the manifold.

## Mathematical Intuition

We consider:

minimize f(x)
subject to ||x|| = 1

A standard gradient descent step may leave the feasible set.
Normalization preserves feasibility while remaining computationally simple.

The goal is practical understanding of geometric optimization rather than formal proofs.

## Skills Demonstrated

Numerical optimization implementation

Translating mathematical theory into software

Experiment design and benchmarking

Scientific visualization in Python

Clean project organization

## Future Work

Riemannian gradient formulation

Additional manifolds (Stiefel / Grassmann)

Adaptive step sizes

Higher-dimensional experiments

## Requirements

numpy
matplotlib
