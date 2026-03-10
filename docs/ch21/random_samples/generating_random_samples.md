# How to Generate Random Samples


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

Simulation is a powerful tool in probability and statistics. By generating random samples from known distributions, we can explore probabilistic phenomena, verify theoretical results, and solve problems that may be analytically intractable.

Most programming environments provide built-in functions for generating random numbers. In MATLAB, the core random number generators are:

| Function | Description |
|----------|-------------|
| `rand` | Uniform on $[0, 1]$ — generates $U(0,1)$ samples |
| `randn` | Standard normal — generates $N(0,1)$ samples |
| `randi` | Uniform on $\{1, 2, \ldots, N\}$ |
| `randperm` | Random permutation of $\{1, 2, \ldots, N\}$ |

## The `random` Function

For more general distributions, MATLAB provides the `random` function:

```matlab
x = random('Dist', Pa1*ones(n,m), Pa2*ones(n,m))
```

This generates an $n \times m$ matrix of samples from the specified distribution with parameters `Pa1` and `Pa2`. Use `help random` for detailed distribution names and corresponding parameters.

## Controlling the Random Number Generator

For reproducibility, it is important to control the state of the random number generator (RNG):

| Command | Description |
|---------|-------------|
| `rng('default')` | Reset RNG to its default initial state |
| `rng(n)` | Reset RNG with seed `n` |

Setting the seed ensures that the same sequence of "random" numbers is generated each time, which is essential for debugging and reproducible experiments.

## Python Equivalents

In Python (NumPy), the equivalent functions are:

```python
import numpy as np

# Set seed for reproducibility
np.random.seed(0)
# or using the newer Generator API:
rng = np.random.default_rng(seed=0)

# Uniform on [0, 1]
U = np.random.rand(n, m)        # or rng.random((n, m))

# Standard normal N(0, 1)
Z = np.random.randn(n, m)       # or rng.standard_normal((n, m))

# Uniform on {1, 2, ..., N}
X = np.random.randint(1, N+1, size=(n, m))  # or rng.integers(1, N+1, size=(n, m))

# Random permutation of {0, 1, ..., N-1}
perm = np.random.permutation(N)  # or rng.permutation(N)
```

For general distributions, NumPy provides functions such as `np.random.binomial`, `np.random.poisson`, `np.random.exponential`, and many more.
