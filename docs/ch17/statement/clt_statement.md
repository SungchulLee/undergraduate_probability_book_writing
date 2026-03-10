# Central Limit Theorem

The standardized sum of iid random variables converges in distribution to the standard normal, regardless of the original distribution — the most important limit theorem in probability.

## Definition

Let $X_1, X_2, \ldots$ be iid with mean $\mu$ and finite variance $\sigma^2 > 0$. Then as $n \to \infty$:

$$
\frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0, 1)
$$

where $S_n = X_1 + \cdots + X_n$. Equivalently, for all $x \in \mathbb{R}$:

$$
P\!\left(\frac{S_n - n\mu}{\sigma\sqrt{n}} \le x\right) \to \Phi(x)
$$

## Explanation

### What the CLT Says

| Quantity | Mean | Variance | Distribution |
|:---|:---:|:---:|:---|
| $X_i$ | $\mu$ | $\sigma^2$ | Arbitrary |
| $S_n$ | $n\mu$ | $n\sigma^2$ | $\approx N(n\mu,\; n\sigma^2)$ for large $n$ |
| $\bar{X}_n = S_n/n$ | $\mu$ | $\sigma^2/n$ | $\approx N(\mu,\; \sigma^2/n)$ for large $n$ |

The CLT is an **approximation** statement: the exact distribution of $S_n$ is generally not normal, but the approximation improves with $n$.

### Normal Case vs General Case

| | iid $N(\mu, \sigma^2)$ | iid non-normal |
|:---|:---|:---|
| $S_n$ | Exactly $N(n\mu, n\sigma^2)$ | $\approx N(n\mu, n\sigma^2)$ for large $n$ |
| CLT needed? | No | Yes |

### Universality

The CLT applies regardless of the shape of the $X_i$ distribution: Bernoulli, exponential, Poisson, Beta, Gamma, or any distribution with finite variance. Even with $n = 20$--$30$, the normal approximation is typically excellent.

### Conditions

- **iid**: identically distributed and independent
- **Finite variance**: $\sigma^2 < \infty$ (fails for Cauchy)
- More general versions (Lindeberg, Lyapunov) relax the "identical" requirement

## Examples

**Example.** $X_i \sim \operatorname{Exp}(2)$, so $\mu = 0.5$, $\sigma^2 = 0.25$. For $n = 50$:

$$
S_{50} \approx N(25, 12.5)
$$

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 100_000

# Sum of 50 iid Exp(2) random variables
n = 50
lam = 2.0
mu, sig2 = 1/lam, 1/lam**2

S = np.random.exponential(1/lam, (n_sim, n)).sum(axis=1)
Z = (S - n * mu) / np.sqrt(n * sig2)

# KS test against N(0,1)
ks_stat, p_val = stats.kstest(Z, 'norm')
print(f"Standardized sum: mean={Z.mean():.4f}, var={Z.var():.4f}")
print(f"KS test vs N(0,1): stat={ks_stat:.4f}, p={p_val:.4f}")
```
