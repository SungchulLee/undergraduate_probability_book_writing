# Additivity of Independent Poisson Random Variables

The sum of independent Poissons is Poisson — a closure property that makes the Poisson family especially convenient for modeling.

## Definition

If $X_1, \ldots, X_n$ are independent with $X_i \sim \text{Pois}(\lambda_i)$, then

$$
\sum_{i=1}^n X_i \sim \text{Pois}\!\left(\sum_{i=1}^n \lambda_i\right)
$$

## Explanation

### Proof via MGF

$$
M_{\sum X_i}(t) = \prod_{i=1}^n e^{\lambda_i(e^t-1)} = e^{(\sum \lambda_i)(e^t-1)}
$$

This is the MGF of $\text{Pois}(\sum \lambda_i)$; by uniqueness, the sum is Poisson.

### Proof via Convolution

For $X \sim \text{Pois}(\lambda_1)$, $Y \sim \text{Pois}(\lambda_2)$ independent:

$$
P(X+Y = k) = \sum_{j=0}^k \frac{e^{-\lambda_1}\lambda_1^j}{j!}\cdot\frac{e^{-\lambda_2}\lambda_2^{k-j}}{(k-j)!} = \frac{e^{-(\lambda_1+\lambda_2)}}{k!}(\lambda_1+\lambda_2)^k
$$

using the binomial theorem on $\sum_j \binom{k}{j}\lambda_1^j\lambda_2^{k-j}$.

### Independence Is Required

If $X$ and $Y$ are dependent Poissons, $X + Y$ is generally **not** Poisson ($\text{Var}(X+Y) \ne E[X+Y]$ when $\text{Cov}(X,Y) \ne 0$).

### Connection to Poisson Process

Merging independent Poisson processes with rates $\lambda_1, \lambda_2$ yields a Poisson process with rate $\lambda_1 + \lambda_2$. Additivity is the count-level version of this merging property.

## Examples

**Example.** Calls from three independent sources: $\text{Pois}(8)$, $\text{Pois}(5)$, $\text{Pois}(2)$. Total $\sim \text{Pois}(15)$.

```python
import numpy as np
from scipy.stats import poisson

np.random.seed(42)
n_sim = 100_000

X1 = np.random.poisson(8, n_sim)
X2 = np.random.poisson(5, n_sim)
X3 = np.random.poisson(2, n_sim)
S = X1 + X2 + X3

print(f"Mean = {S.mean():.3f} (theory: 15)")
print(f"Var = {S.var():.3f} (theory: 15)")
print(f"P(S > 20) = {np.mean(S > 20):.4f} "
      f"(theory: {1 - poisson.cdf(20, 15):.4f})")
```
