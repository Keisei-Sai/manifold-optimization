# Geometric Optimization on Manifolds (Python)
> A small experimental project exploring how geometry changes optimization behavior.

Implementation and empirical comparison of gradient-based optimization under geometric constraints using manifold-aware updates.

## Project Goal

This project compares optimization behavior with and without geometric constraints.
By comparing unconstrained gradient descent with sphere-constrained optimization, the implementation visualizes how geometry affects convergence dynamics.
Many real-world optimization problems include constraints, and understanding their geometric effects is essential for designing reliable algorithms.

## Key Result

### Effect of geometric constraints on convergence

![Convergence](figures/convergence.png)

Even with the same optimization principle, enforcing geometric constraints fundamentally changes convergence behavior.

### Optimization trajectory on the unit sphere

![Trajectory](figures/trajectory_sphere.png)

The optimization path remains on the constraint manifold through retraction-based updates.

## Overview

This project investigates how geometric constraints influence optimization behavior by comparing optimization methods in both Euclidean space and manifold settings.

Starting from classical optimization examples (Rosenbrock function), the project extends intuition toward optimization on constrained spaces such as the unit sphere.

## Why This Matters

Optimization under constraints appears in many applications such as machine learning, signal processing, and scientific computing.
This project provides an intuitive numerical perspective on how geometry influences algorithmic behavior.

## Visualization

![Optimization trajectory](images/trajectory_rosenbrock.png)

## What This Project Demonstrates

- Manifold-aware optimization using normalization (retraction)

- Reproducible numerical experiments

- Comparison between Euclidean and manifold optimization

- Visualization of optimization trajectories

### Implemented Methods

- Euclidean Gradient Descent in R^2

- Sphere Gradient Descent on the unit sphere

## Quick Start

Install dependencies:

- pip install -r requirements.txt
Run experiment:
- python -m experiments.compare_methods

This generates convergence plots and trajectory visualizations.

## Design Decisions

Why a sphere?

Many optimization problems include unit-norm constraints.
Standard gradient descent may violate feasibility, while manifold optimization maintains constraints during updates.

Why normalization?

Each gradient step is followed by normalization:

x_next = (x - alpha * grad_f(x)) / ||x - alpha * grad_f(x)||

This acts as a simple retraction mapping iterates back onto the manifold.

## Mathematical Intuition

We consider the constrained optimization problem:

minimize f(x)  
subject to ||x|| = 1

A standard gradient descent step may leave the feasible set.
Normalization preserves feasibility while remaining computationally simple.

This section explains the geometric motivation behind the implementation.

## Results

The following figures compare convergence behavior and optimization trajectories under geometric constraints.

### Convergence plot:
![Convergence](figures/convergence.png)

### Trajectory visualization:
![Trajectory](figures/trajectory_sphere.png)


## Repository Structure

- algorithms/ Optimization implementations
- experiments/ Experiment runners
- figures/ Generated plots
- images/ Visualization assets

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

- numpy
- matplotlib

Author: Keisei Sai  
GitHub: https://github.com/Keisei-Sai
