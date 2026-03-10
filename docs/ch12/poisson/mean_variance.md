# Mean and Variance of the Poisson

Both the mean and variance of a Poisson equal $\lambda$ — a defining fingerprint that distinguishes it from other discrete distributions.

## Definition

For $X \sim \text{Pois}(\lambda)$:

$$
E[X] = \lambda, \qquad E[X^2] = \lambda^2 + \lambda, \qquad \text{Var}(X) = \lambda
$$

The standard deviation is $\text{SD}(X) = \sqrt{\lambda}$.

## Explanation

### Direct Computation of the Mean

$$
E[X] = \sum_{k=1}^{\infty}k\,\frac{e^{-\lambda}\lambda^k}{k!} = e^{-\lambda}\lambda\sum_{j=0}^{\infty}\frac{\lambda^j}{j!} = \lambda
$$

using the substitution $j = k - 1$.

### Factorial Moment Trick

$$
E[X(X-1)] = \sum_{k=2}^{\infty}\frac{e^{-\lambda}\lambda^k}{(k-2)!} = \lambda^2
$$

Therefore $E[X^2] = E[X(X-1)] + E[X] = \lambda^2 + \lambda$ and $\text{Var}(X) = \lambda$.

### Dispersion Index

The **dispersion index** $D = \text{Var}(X)/E[X]$ is a diagnostic for Poisson fit:

| $D$ value | Interpretation | Alternative model |
|:----------|:---------------|:------------------|
| $D \approx 1$ | Equidispersion | Poisson appropriate |
| $D > 1$ | Overdispersion | Negative binomial |
| $D < 1$ | Underdispersion | Binomial |

## Examples

**Example.** Verify $E[X] = \text{Var}(X) = \lambda$ for several values of $\lambda$.

```python
import numpy as np

np.random.seed(42)
n_sim = 100_000

for la in [1, 5, 10, 20, 50]:
    X = np.random.poisson(la, n_sim)
    D = X.var(ddof=1) / X.mean()
    print(f"λ={la:2d}: mean={X.mean():.2f}, var={X.var(ddof=1):.2f}, D={D:.4f}")
```
