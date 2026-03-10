# Normal Approximation to the Poisson

For large $\lambda$, the Poisson distribution is well approximated by a normal with matching mean and variance — both equal to $\lambda$.

## Definition

If $X \sim \operatorname{Pois}(\lambda)$, then for large $\lambda$:

$$
X \approx N(\lambda, \lambda)
$$

Equivalently, $\frac{X - \lambda}{\sqrt{\lambda}} \approx N(0, 1)$.

## Explanation

### Why the CLT Applies

Decompose $X = \sum_{i=1}^{\lambda} Y_i$ where $Y_i \sim \operatorname{Pois}(1)$ are iid (when $\lambda$ is a positive integer). Since $E[Y_i] = \operatorname{Var}(Y_i) = 1$, the CLT gives:

$$
\frac{X - \lambda}{\sqrt{\lambda}} \xrightarrow{d} N(0,1) \quad \text{as } \lambda \to \infty
$$

### Approximation Chain

For $n$ large and $p$ small:

$$
\operatorname{Bin}(n, p) \approx \operatorname{Pois}(np) \approx N(np, np)
$$

The Poisson approximation is best when $p$ is small; the normal approximation is best when $\lambda = np$ is large.

### Continuity Correction

Since Poisson is discrete, use $P(X \ge k) \approx 1 - \Phi\!\left(\frac{k - 0.5 - \lambda}{\sqrt{\lambda}}\right)$.

## Examples

**Example.** Compare normal approximation accuracy across increasing $\lambda$.

```python
import numpy as np
from scipy import stats

for lam in [10, 25, 50, 100, 200]:
    k = int(lam + 2 * np.sqrt(lam))  # threshold at mu + 2*sigma
    exact = 1 - stats.poisson.cdf(k - 1, lam)
    z = (k - 0.5 - lam) / np.sqrt(lam)
    approx = 1 - stats.norm.cdf(z)
    print(f"λ={lam:>3d}, k={k:>3d}: exact={exact:.4f}, normal≈{approx:.4f}")
```
