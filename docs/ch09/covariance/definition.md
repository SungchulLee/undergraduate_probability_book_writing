# Covariance Definition and Properties

Covariance measures the linear association between two random variables — positive when they move together, negative when they move oppositely.

## Definition

The **covariance** of $X$ and $Y$ is

$$
\text{Cov}(X, Y) = E\bigl[(X - E[X])(Y - E[Y])\bigr]
$$

**Shortcut formula:**

$$
\text{Cov}(X, Y) = E[XY] - E[X]\,E[Y]
$$

Note that $\text{Cov}(X, X) = \text{Var}(X)$.

## Explanation

### Sign Interpretation

- $\text{Cov}(X, Y) > 0$: when $X$ is above its mean, $Y$ tends to be above its mean
- $\text{Cov}(X, Y) < 0$: when $X$ is above its mean, $Y$ tends to be below its mean
- $\text{Cov}(X, Y) = 0$: no linear association (but nonlinear dependence is possible)

### Algebraic Properties

| Property | Formula |
|:---------|:--------|
| Symmetry | $\text{Cov}(X, Y) = \text{Cov}(Y, X)$ |
| Constant | $\text{Cov}(X, c) = 0$ |
| Scaling | $\text{Cov}(aX, bY) = ab\,\text{Cov}(X, Y)$ |
| Shift | $\text{Cov}(X + c, Y + d) = \text{Cov}(X, Y)$ |
| Sum | $\text{Cov}(X + Z, Y) = \text{Cov}(X, Y) + \text{Cov}(Z, Y)$ |
| Bilinearity | $\text{Cov}\bigl(\sum a_i X_i, \sum b_j Y_j\bigr) = \sum_i \sum_j a_i b_j \text{Cov}(X_i, Y_j)$ |

### Connection to Variance

The variance of a sum uses covariance as the correction term:

$$
\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X, Y)
$$

## Examples

**Example.** Roll two dice: $X$ = first die, $Y$ = sum of both dice. Then $Y = X + Z$ where $Z$ is the second die, independent of $X$.

$$
\text{Cov}(X, Y) = \text{Cov}(X, X + Z) = \text{Cov}(X, X) + \text{Cov}(X, Z) = \text{Var}(X) + 0 = \frac{35}{12}
$$

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

X = np.random.randint(1, 7, n_sim)
Z = np.random.randint(1, 7, n_sim)
Y = X + Z

cov_xy = np.mean((X - X.mean()) * (Y - Y.mean()))
print(f"Cov(X, Y) = {cov_xy:.4f}  (theory: {35/12:.4f})")
print(f"Var(X) = {X.var():.4f}  (theory: {35/12:.4f})")

# Shortcut formula
cov_shortcut = np.mean(X * Y) - X.mean() * Y.mean()
print(f"Shortcut:   {cov_shortcut:.4f}")
```
