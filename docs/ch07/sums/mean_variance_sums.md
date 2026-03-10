# Mean and Variance of Sums

The mean of a sum always equals the sum of the means. The variance of a sum equals the sum of variances only when the variables are uncorrelated.

## Definition

For random variables $X_1, \ldots, X_n$:

$$
E\!\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n E[X_i] \qquad \text{(always)}
$$

$$
\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i) + 2\sum_{i < j}\text{Cov}(X_i, X_j)
$$

If $X_1, \ldots, X_n$ are **independent**: $\text{Var}(\sum X_i) = \sum \text{Var}(X_i)$.

If **iid**: $E[\sum X_i] = nE[X_1]$, $\text{Var}(\sum X_i) = n\,\text{Var}(X_1)$.

## Explanation

### Weighted Sums

For $S = \sum a_i X_i$:

$$
E[S] = \sum a_i E[X_i], \qquad \text{Var}(S) = \sum a_i^2\,\text{Var}(X_i) + 2\sum_{i<j}a_i a_j\,\text{Cov}(X_i, X_j)
$$

### Matrix Form

With $S = \mathbf{a}^T\mathbf{X}$ and covariance matrix $\boldsymbol{\Sigma}$:

$$
\text{Var}(S) = \mathbf{a}^T\boldsymbol{\Sigma}\,\mathbf{a}
$$

## Examples

**Example 1 (Binomial).** $S = \sum_{i=1}^n \mathbf{1}_{A_i}$, iid $\text{Bern}(p)$: $E[S] = np$, $\text{Var}(S) = np(1-p)$.

**Example 2 (Negative Binomial).** $S = \sum_{i=1}^r X_i$, iid $\text{Geo}(p)$: $E[S] = r/p$, $\text{Var}(S) = r(1-p)/p^2$.

**Example 3 (Portfolio).** Three assets with weights $\mathbf{a} = (0.4, 0.35, 0.25)$, SDs $(0.20, 0.15, 0.25)$, and correlations. Portfolio variance $= \mathbf{a}^T\boldsymbol{\Sigma}\,\mathbf{a}$.

```python
import numpy as np

# Portfolio variance example
a = np.array([0.4, 0.35, 0.25])
sigma = np.array([0.20, 0.15, 0.25])
rho = np.array([[1, 0.3, 0.1], [0.3, 1, 0.5], [0.1, 0.5, 1]])
Sigma = np.outer(sigma, sigma) * rho

port_var = a @ Sigma @ a
print(f"Portfolio SD = {np.sqrt(port_var):.4f}")

# Compare: if independent (rho = I)
port_var_indep = np.sum((a * sigma)**2)
print(f"If independent: SD = {np.sqrt(port_var_indep):.4f}")
```
