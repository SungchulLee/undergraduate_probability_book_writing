# Variance-Covariance Matrix

The covariance matrix packages all pairwise covariances into a single matrix, enabling compact formulas for portfolio variance and multivariate analysis.

## Definition

For a random vector $\mathbf{X} = (X_1, \ldots, X_n)^T$, the **covariance matrix** is

$$
\boldsymbol{\Sigma} = \text{Cov}(\mathbf{X}) = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T]
$$

where $\boldsymbol{\mu} = E[\mathbf{X}]$. The $(i,j)$ entry is $\Sigma_{ij} = \text{Cov}(X_i, X_j)$.

The variance of a linear combination $S = \mathbf{a}^T\mathbf{X}$ is

$$
\text{Var}(S) = \mathbf{a}^T\boldsymbol{\Sigma}\,\mathbf{a}
$$

## Explanation

### Structure

$$
\boldsymbol{\Sigma} = \begin{pmatrix} \text{Var}(X_1) & \text{Cov}(X_1, X_2) & \cdots & \text{Cov}(X_1, X_n) \\ \text{Cov}(X_2, X_1) & \text{Var}(X_2) & \cdots & \text{Cov}(X_2, X_n) \\ \vdots & \vdots & \ddots & \vdots \\ \text{Cov}(X_n, X_1) & \text{Cov}(X_n, X_2) & \cdots & \text{Var}(X_n) \end{pmatrix}
$$

- **Symmetric:** $\Sigma_{ij} = \Sigma_{ji}$
- **Positive semi-definite:** $\mathbf{a}^T\boldsymbol{\Sigma}\,\mathbf{a} \ge 0$ for all $\mathbf{a}$ (since variance $\ge 0$)
- **Diagonal entries:** variances; **off-diagonal entries:** covariances

### Correlation Matrix

The correlation matrix $\mathbf{R}$ is the covariance matrix of the standardized variables:

$$
R_{ij} = \frac{\Sigma_{ij}}{\sqrt{\Sigma_{ii}\,\Sigma_{jj}}} = \rho(X_i, X_j)
$$

Equivalently, $\mathbf{R} = \mathbf{D}^{-1}\boldsymbol{\Sigma}\,\mathbf{D}^{-1}$ where $\mathbf{D} = \text{diag}(\text{SD}(X_1), \ldots, \text{SD}(X_n))$.

### Linear Transformations

If $\mathbf{Y} = \mathbf{A}\mathbf{X} + \mathbf{b}$, then $\text{Cov}(\mathbf{Y}) = \mathbf{A}\boldsymbol{\Sigma}\,\mathbf{A}^T$.

## Examples

**Example (Portfolio variance).** Three assets with weights $\mathbf{a} = (0.5, 0.3, 0.2)^T$, SDs $(0.20, 0.30, 0.40)$, and correlations $\rho_{12} = 0.3$, $\rho_{13} = 0.1$, $\rho_{23} = 0.5$.

```python
import numpy as np

a = np.array([0.5, 0.3, 0.2])
sd = np.array([0.20, 0.30, 0.40])
R = np.array([[1.0, 0.3, 0.1],
              [0.3, 1.0, 0.5],
              [0.1, 0.5, 1.0]])

Sigma = np.outer(sd, sd) * R
port_var = a @ Sigma @ a
port_sd = np.sqrt(port_var)

print("Covariance matrix:")
print(Sigma)
print(f"\nPortfolio variance = {port_var:.6f}")
print(f"Portfolio SD = {port_sd:.4f}")

# Compare: if assets were independent
port_var_indep = np.sum((a * sd)**2)
print(f"If independent: SD = {np.sqrt(port_var_indep):.4f}")

# Simulate to verify
np.random.seed(42)
returns = np.random.multivariate_normal([0, 0, 0], Sigma, 200_000)
port_returns = returns @ a
print(f"\nSimulated portfolio SD = {port_returns.std():.4f}")
```
