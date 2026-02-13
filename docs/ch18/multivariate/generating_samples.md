# Generating Random Samples from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$

## Overview

In practice, we often need to generate random samples from a multivariate normal distribution with a specified mean and covariance. The standard approach uses the **Cholesky decomposition** of the covariance matrix to transform independent standard normals into correlated multivariate normals.

---

## Cholesky Decomposition

Any symmetric positive definite matrix $\boldsymbol{\Sigma}$ can be decomposed as:

$$
\boldsymbol{\Sigma} = LL^T
$$

where $L$ is a **lower triangular** matrix with positive diagonal entries. This is called the **Cholesky decomposition** (equivalently written $\boldsymbol{\Sigma} = U^T U$ where $U = L^T$ is upper triangular).

The Cholesky decomposition is:

- Unique for positive definite matrices
- Numerically stable and efficient: $O(d^3/3)$ operations
- The "square root" of a positive definite matrix

---

## Algorithm

**Step 1.** Compute the Cholesky decomposition $L = \text{chol}(\boldsymbol{\Sigma})$ so that $\boldsymbol{\Sigma} = LL^T$.

**Step 2.** Generate $\mathbf{z} = (z_1, \ldots, z_d)^T$ with $z_k \overset{\text{iid}}{\sim} N(0, 1)$.

**Step 3.** Set:

$$
\mathbf{x} = \boldsymbol{\mu} + L\mathbf{z}
$$

### Verification

**Mean:**

$$
E[\mathbf{x}] = E[\boldsymbol{\mu} + L\mathbf{z}] = \boldsymbol{\mu} + L \cdot E[\mathbf{z}] = \boldsymbol{\mu} + L\mathbf{0} = \boldsymbol{\mu}
$$

**Covariance:**

$$
E[(\mathbf{x} - \boldsymbol{\mu})(\mathbf{x} - \boldsymbol{\mu})^T] = E[(L\mathbf{z})(L\mathbf{z})^T] = L \cdot E[\mathbf{z}\mathbf{z}^T] \cdot L^T = LIL^T = LL^T = \boldsymbol{\Sigma}
$$

---

## Connection to the Constructive Definition

This is simply an application of the constructive definition $\mathbf{x} = A\mathbf{z} + \boldsymbol{\mu}$ with $A = L$. The Cholesky decomposition provides a specific, efficient choice of $A$ satisfying $AA^T = \boldsymbol{\Sigma}$.

!!! note "Other Decompositions"
    Any matrix $A$ satisfying $AA^T = \boldsymbol{\Sigma}$ works (e.g., from eigendecomposition $\boldsymbol{\Sigma} = Q\Lambda Q^T$, one can use $A = Q\Lambda^{1/2}$). The Cholesky decomposition is preferred for its numerical efficiency and stability.

---

## Python Implementation

### Basic Sampling

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Parameters
mu = np.array([1, 2])
Sigma = np.array([[3, 2],
                   [2, 5]])

# Method 1: Cholesky decomposition (manual)
L = np.linalg.cholesky(Sigma)
n = 1000
z = np.random.randn(2, n)
x = mu[:, np.newaxis] + L @ z

print("Cholesky factor L:")
print(L)
print(f"\nL @ L^T:\n{L @ L.T}")
print(f"Sigma:\n{Sigma}")

# Method 2: numpy built-in (uses Cholesky internally)
x2 = np.random.multivariate_normal(mu, Sigma, n).T

# Compare sample statistics
print(f"\n--- Method 1 (Cholesky) ---")
print(f"Sample mean: {x.mean(axis=1)}")
print(f"Sample cov:\n{np.cov(x)}")

print(f"\n--- Method 2 (numpy built-in) ---")
print(f"Sample mean: {x2.mean(axis=1)}")
print(f"Sample cov:\n{np.cov(x2)}")
```

### Visualization: Three Scenarios

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: Standard normal samples
n = 100
z = np.random.randn(2, n)
axes[0].plot(z[0], z[1], 'o', markersize=4)
axes[0].set_title('100 Standard Normal Samples')
axes[0].set_xlabel('$z_1$')
axes[0].set_ylabel('$z_2$')
axes[0].set_aspect('equal')
axes[0].grid(True, alpha=0.3)

# Plot 2: Samples from N(μ, Σ)
mu1 = np.array([1, 2])
Sigma1 = np.array([[3, 2], [2, 5]])
L1 = np.linalg.cholesky(Sigma1)
x1 = mu1[:, np.newaxis] + L1 @ np.random.randn(2, n)
axes[1].plot(x1[0], x1[1], 'o', markersize=4)
axes[1].set_title(r'100 Samples from $N(\mu, \Sigma)$')
axes[1].set_xlabel('$x_1$')
axes[1].set_ylabel('$x_2$')
axes[1].grid(True, alpha=0.3)

# Plot 3: Two clusters from different distributions
n1, n2 = 50, 40
mu_a = np.array([1, 2])
Sigma_a = np.array([[3, 2], [2, 5]])
L_a = np.linalg.cholesky(Sigma_a)
x_a = mu_a[:, np.newaxis] + L_a @ np.random.randn(2, n1)

mu_b = np.array([9, 7])
Sigma_b = np.array([[3, 1], [2, 3]])
# Ensure Sigma_b is symmetric for Cholesky
Sigma_b_sym = (Sigma_b + Sigma_b.T) / 2
L_b = np.linalg.cholesky(Sigma_b_sym)
x_b = mu_b[:, np.newaxis] + L_b @ np.random.randn(2, n2)

axes[2].plot(x_a[0], x_a[1], 'bo', markersize=4, label=r'$N(\mu_1, \Sigma_1)$')
axes[2].plot(x_b[0], x_b[1], 'ro', markersize=4, label=r'$N(\mu_2, \Sigma_2)$')
axes[2].set_title('Two Multivariate Normal Clusters')
axes[2].set_xlabel('$x_1$')
axes[2].set_ylabel('$x_2$')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### Higher Dimensions

```python
import numpy as np

np.random.seed(42)

# 5-dimensional multivariate normal
d = 5
mu = np.arange(1, d + 1, dtype=float)

# Create a valid covariance matrix via random factor
A_random = np.random.randn(d, d)
Sigma = A_random @ A_random.T + np.eye(d)  # ensure positive definite

# Generate samples
L = np.linalg.cholesky(Sigma)
n = 10_000
z = np.random.randn(d, n)
x = mu[:, np.newaxis] + L @ z

print(f"True mean: {mu}")
print(f"Sample mean: {x.mean(axis=1).round(2)}")
print(f"\nMax abs error in covariance: {np.max(np.abs(np.cov(x) - Sigma)):.4f}")
```

---

## Key Takeaways

- The Cholesky decomposition $\boldsymbol{\Sigma} = LL^T$ provides an efficient way to generate multivariate normal samples.
- The procedure transforms iid standard normals $\mathbf{z}$ into correlated normals $\mathbf{x} = \boldsymbol{\mu} + L\mathbf{z}$.
- This is numerically equivalent to `np.random.multivariate_normal()` but understanding the mechanism is essential for applications like the Kalman filter, Gaussian processes, and MCMC sampling.
- Any factorization $AA^T = \boldsymbol{\Sigma}$ works; Cholesky is preferred for efficiency.
