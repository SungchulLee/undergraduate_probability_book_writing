# Conditional Distributions in the Multivariate Case

Conditioning a subset of a multivariate normal vector on the remaining components yields another multivariate normal with closed-form parameters. This result underpins Bayesian linear regression, the Kalman filter, and Gaussian process prediction.

## Definition

Partition $\mathbf{x} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ as $\mathbf{x} = (\mathbf{x}_1^T, \mathbf{x}_2^T)^T$ with conformable partitions of the mean and covariance. The conditional distribution is

$$
\mathbf{x}_1 \mid \mathbf{x}_2 \;\sim\; N\!\left(\boldsymbol{\mu}_{1|2},\; \boldsymbol{\Sigma}_{1|2}\right)
$$

where

$$
\boldsymbol{\mu}_{1|2} = \boldsymbol{\mu}_1 + \boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}(\mathbf{x}_2 - \boldsymbol{\mu}_2)
$$

$$
\boldsymbol{\Sigma}_{1|2} = \boldsymbol{\Sigma}_{11} - \boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}\boldsymbol{\Sigma}_{21}
$$

The matrix $\boldsymbol{\Sigma}_{1|2}$ is the Schur complement of $\boldsymbol{\Sigma}_{22}$ in $\boldsymbol{\Sigma}$.

## Explanation

### Precision matrix formulation

With $\boldsymbol{\Lambda} = \boldsymbol{\Sigma}^{-1}$ partitioned conformably, the conditional parameters simplify to

$$
\boldsymbol{\Sigma}_{1|2} = \boldsymbol{\Lambda}_{11}^{-1}
$$

$$
\boldsymbol{\mu}_{1|2} = \boldsymbol{\mu}_1 - \boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12}(\mathbf{x}_2 - \boldsymbol{\mu}_2)
$$

The precision matrix encodes conditional independence: $\Lambda_{ij} = 0$ means $x_i$ and $x_j$ are conditionally independent given all other variables.

### Derivation via completing the square

Expanding $(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Lambda} (\mathbf{x} - \boldsymbol{\mu})$ and treating $\mathbf{x}_2$ as fixed, complete the square in $\mathbf{x}_1$ to isolate the conditional quadratic form with center $\boldsymbol{\mu}_{1|2}$ and precision $\boldsymbol{\Lambda}_{11}$.

### Linear-Gaussian model

Given a prior $\mathbf{x} \sim N(\boldsymbol{\mu}_x, \boldsymbol{\Sigma}_x)$ and observation model $\mathbf{y} = A\mathbf{x} + \mathbf{b} + \boldsymbol{\varepsilon}$ with $\boldsymbol{\varepsilon} \sim N(\mathbf{0}, \boldsymbol{\Sigma}_\varepsilon)$ independent of $\mathbf{x}$, the posterior is

$$
\boldsymbol{\Sigma}_{x|y}^{-1} = \boldsymbol{\Sigma}_x^{-1} + A^T\boldsymbol{\Sigma}_\varepsilon^{-1} A
$$

$$
\boldsymbol{\mu}_{x|y} = \boldsymbol{\Sigma}_{x|y}\!\left(\boldsymbol{\Sigma}_x^{-1}\boldsymbol{\mu}_x + A^T\boldsymbol{\Sigma}_\varepsilon^{-1}(\mathbf{y} - \mathbf{b})\right)
$$

The posterior precision is the sum of prior precision and data precision -- the Bayesian update rule for Gaussian models.

## Examples

Compute the conditional distribution of $X_1$ given $X_2 = 3, X_3 = 4$ in a trivariate normal, using both covariance and precision formulations.

```python
import numpy as np

mu = np.array([1.0, 2.0, 3.0])
Sigma = np.array([[4.0, 2.0, 1.0],
                   [2.0, 5.0, 3.0],
                   [1.0, 3.0, 6.0]])

# Covariance form
S12 = Sigma[0:1, 1:]        # (1, 2)
S22 = Sigma[1:, 1:]         # (2, 2)
S22_inv = np.linalg.inv(S22)
x2_obs = np.array([3.0, 4.0])

mu_cond = mu[0] + S12 @ S22_inv @ (x2_obs - mu[1:])
Sigma_cond = Sigma[0, 0] - S12 @ S22_inv @ Sigma[1:, 0:1]
print(f"Covariance form:  mean={mu_cond.item():.4f}, var={Sigma_cond.item():.4f}")

# Precision form
Lambda = np.linalg.inv(Sigma)
Sigma_cond_prec = 1.0 / Lambda[0, 0]
mu_cond_prec = mu[0] - (Lambda[0, 1:] @ (x2_obs - mu[1:])) / Lambda[0, 0]
print(f"Precision form:   mean={mu_cond_prec:.4f}, var={Sigma_cond_prec:.4f}")

# Simulation check
np.random.seed(42)
n = 500_000
L = np.linalg.cholesky(Sigma)
samples = (mu[:, None] + L @ np.random.randn(3, n)).T
mask = (np.abs(samples[:, 1] - 3.0) < 0.1) & (np.abs(samples[:, 2] - 4.0) < 0.1)
x1_slice = samples[mask, 0]
print(f"\nSimulated mean:   {x1_slice.mean():.4f}")
print(f"Simulated var:    {x1_slice.var():.4f}")
```
