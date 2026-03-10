# Variance of a Sum (Independent Case)

When variables are independent (or just uncorrelated), all cross-terms vanish and variance becomes additive.

## Definition

If $X_1, \ldots, X_n$ are **uncorrelated** (which holds if they are independent):

$$
\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i)
$$

For a weighted sum with independent variables:

$$
\text{Var}\!\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2\,\text{Var}(X_i)
$$

If **iid** with common variance $\sigma^2$: $\text{Var}(\sum X_i) = n\sigma^2$.

## Explanation

### Why Independence Suffices

Independent variables have zero covariance, so the $2\sum_{i<j}\text{Cov}(X_i, X_j)$ term in the general formula vanishes. The same holds under the weaker condition of uncorrelatedness.

### Standard Decompositions

| Distribution | Sum of | $\text{Var}(S)$ |
|:-------------|:-------|:----------------|
| $\text{Bin}(n, p)$ | $n$ iid $\text{Bern}(p)$ | $np(1-p)$ |
| $\text{NB}(r, p)$ | $r$ iid $\text{Geo}(p)$ | $r(1-p)/p^2$ |
| $\text{Poisson}(\lambda_1 + \lambda_2)$ | Indep. $\text{Pois}(\lambda_1) + \text{Pois}(\lambda_2)$ | $\lambda_1 + \lambda_2$ |

### Variance of Sample Mean

For iid $X_1, \ldots, X_n$ with variance $\sigma^2$:

$$
\text{Var}(\bar{X}) = \text{Var}\!\left(\frac{1}{n}\sum X_i\right) = \frac{1}{n^2}\cdot n\sigma^2 = \frac{\sigma^2}{n}
$$

This is the basis for the $\sigma/\sqrt{n}$ standard error.

## Examples

**Example.** $S = 3X_1 - 2X_2 + X_3$ where $X_1, X_2, X_3$ are independent with variances 4, 1, 9.

$$
\text{Var}(S) = 9(4) + 4(1) + 1(9) = 36 + 4 + 9 = 49
$$

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

# S = 3X1 - 2X2 + X3, independent
X1 = np.random.normal(0, 2, n_sim)    # Var = 4
X2 = np.random.normal(0, 1, n_sim)    # Var = 1
X3 = np.random.normal(0, 3, n_sim)    # Var = 9
S = 3*X1 - 2*X2 + X3

print(f"Var(S) = {S.var():.2f}  (theory: 49)")

# Sample mean variance
n = 25
sigma2 = 4.0
means = [np.random.normal(0, 2, n).mean() for _ in range(n_sim)]
print(f"\nVar(X_bar), n=25 = {np.var(means):.4f}  (theory: {sigma2/n:.4f})")
```
