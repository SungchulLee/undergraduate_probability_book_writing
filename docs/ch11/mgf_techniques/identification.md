# Identifying Distributions via MGFs

Compute the MGF, match it to a known form, and invoke uniqueness — the standard technique for proving distributional results without direct PMF/PDF computation.

## Definition

**Strategy.** To show $X$ has distribution $\mathcal{D}$:

1. Compute $M_X(t)$
2. Show $M_X(t)$ equals the MGF of $\mathcal{D}$
3. Conclude $X \sim \mathcal{D}$ by the uniqueness theorem

## Explanation

### MGF Reference Table

| Distribution | MGF $M_X(t)$ | Domain |
|:-------------|:-------------|:-------|
| $\text{Bern}(p)$ | $q + pe^t$ | all $t$ |
| $\text{Bin}(n, p)$ | $(q + pe^t)^n$ | all $t$ |
| $\text{Pois}(\lambda)$ | $e^{\lambda(e^t-1)}$ | all $t$ |
| $\text{Geo}(p)$ | $pe^t/(1-qe^t)$ | $t < -\ln q$ |
| $\text{NB}(r, p)$ | $(pe^t/(1-qe^t))^r$ | $t < -\ln q$ |
| $N(\mu, \sigma^2)$ | $e^{\mu t + \sigma^2 t^2/2}$ | all $t$ |
| $\text{Exp}(\lambda)$ | $\lambda/(\lambda - t)$ | $t < \lambda$ |
| $\text{Gamma}(\alpha, \lambda)$ | $(\lambda/(\lambda-t))^\alpha$ | $t < \lambda$ |

### Common Applications

- **Sum of independent RVs:** Multiply MGFs and identify the product
- **Poisson limit theorem:** Show binomial MGF converges to Poisson MGF
- **CLT:** Show standardized-sum MGF converges to $e^{t^2/2}$
- **Chi-squared:** Sum of squared standard normals has $\text{Gamma}(n/2, 1/2)$ MGF

## Examples

**Example.** Let $X \sim \text{Pois}(\lambda_1)$ and $Y \sim \text{Pois}(\lambda_2)$ be independent. Then:

$$
M_{X+Y}(t) = e^{\lambda_1(e^t-1)}\,e^{\lambda_2(e^t-1)} = e^{(\lambda_1+\lambda_2)(e^t-1)}
$$

This is the MGF of $\text{Pois}(\lambda_1 + \lambda_2)$, so $X + Y \sim \text{Pois}(\lambda_1 + \lambda_2)$.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

X = np.random.poisson(3, n_sim)
Y = np.random.poisson(7, n_sim)
S = X + Y

print(f"Pois(3) + Pois(7): mean={S.mean():.3f}, var={S.var():.3f}")
print(f"Theory Pois(10):   mean=10, var=10")
```
