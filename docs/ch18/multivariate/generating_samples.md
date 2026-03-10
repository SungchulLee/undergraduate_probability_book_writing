# Generating Samples via Cholesky Decomposition

Generating random samples from a multivariate normal with a specified mean and covariance is a fundamental computational task. The standard approach factors the covariance matrix using the Cholesky decomposition and transforms independent standard normals.

## Definition

Any symmetric positive definite matrix $\boldsymbol{\Sigma}$ admits the **Cholesky decomposition**

$$
\boldsymbol{\Sigma} = LL^T
$$

where $L$ is a lower triangular matrix with positive diagonal entries. A sample from $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ is obtained by

$$
\mathbf{x} = \boldsymbol{\mu} + L\mathbf{z}, \qquad \mathbf{z} \sim N(\mathbf{0}, I)
$$

## Explanation

### Why it works

The mean is $E[\boldsymbol{\mu} + L\mathbf{z}] = \boldsymbol{\mu}$ and the covariance is

$$
E[(L\mathbf{z})(L\mathbf{z})^T] = L\,E[\mathbf{z}\mathbf{z}^T]\,L^T = LL^T = \boldsymbol{\Sigma}
$$

Since $L\mathbf{z} + \boldsymbol{\mu}$ is an affine transformation of a standard normal vector, the result is multivariate normal by the closure property.

### Connection to the constructive definition

This is the constructive definition $\mathbf{x} = A\mathbf{z} + \boldsymbol{\mu}$ with $A = L$. Any matrix satisfying $AA^T = \boldsymbol{\Sigma}$ works (e.g., from the eigendecomposition $A = Q\Lambda^{1/2}$), but Cholesky is preferred for its $O(d^3/3)$ cost and numerical stability.

### Algorithm

1. Compute $L = \text{chol}(\boldsymbol{\Sigma})$.
2. Draw $\mathbf{z} \sim N(\mathbf{0}, I_d)$.
3. Return $\mathbf{x} = \boldsymbol{\mu} + L\mathbf{z}$.

## Examples

Generate samples from a bivariate and a 5-dimensional normal, comparing sample statistics with the true parameters.

```python
import numpy as np

np.random.seed(42)

# 2D example
mu2 = np.array([1.0, 2.0])
Sigma2 = np.array([[3.0, 2.0],
                    [2.0, 5.0]])
L2 = np.linalg.cholesky(Sigma2)
n = 10_000
x2 = mu2[:, None] + L2 @ np.random.randn(2, n)

print("2D Cholesky sampling:")
print(f"  L @ L^T matches Sigma: {np.allclose(L2 @ L2.T, Sigma2)}")
print(f"  Sample mean: {x2.mean(axis=1).round(3)}")
print(f"  Sample cov:\n{np.cov(x2).round(3)}")

# 5D example
d = 5
mu5 = np.arange(1, d + 1, dtype=float)
A_rand = np.random.randn(d, d)
Sigma5 = A_rand @ A_rand.T + np.eye(d)

L5 = np.linalg.cholesky(Sigma5)
x5 = mu5[:, None] + L5 @ np.random.randn(d, n)

print(f"\n5D Cholesky sampling:")
print(f"  True mean:   {mu5}")
print(f"  Sample mean: {x5.mean(axis=1).round(2)}")
print(f"  Max cov error: {np.max(np.abs(np.cov(x5) - Sigma5)):.4f}")
```
