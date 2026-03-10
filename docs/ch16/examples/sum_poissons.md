# Sum of Poissons

The Poisson family is closed under convolution: a sum of independent Poisson random variables is Poisson with the summed rate.

## Definition

If $X \sim \operatorname{Pois}(\lambda_1)$ and $Y \sim \operatorname{Pois}(\lambda_2)$ are independent, then:

$$
X + Y \sim \operatorname{Pois}(\lambda_1 + \lambda_2)
$$

More generally, independent $X_i \sim \operatorname{Pois}(\lambda_i)$ satisfy $\sum_{i=1}^n X_i \sim \operatorname{Pois}(\sum_{i=1}^n \lambda_i)$.

## Explanation

### Proof via Convolution

For non-negative integer $a$, summing over $b = 0, 1, \ldots, a$:

$$
p_{X+Y}(a) = \sum_{b=0}^{a} \frac{\lambda_1^b e^{-\lambda_1}}{b!} \cdot \frac{\lambda_2^{a-b} e^{-\lambda_2}}{(a-b)!} = \frac{e^{-(\lambda_1+\lambda_2)}}{a!} \sum_{b=0}^{a} \binom{a}{b} \lambda_1^b \lambda_2^{a-b}
$$

By the binomial theorem, $\sum_{b=0}^{a} \binom{a}{b} \lambda_1^b \lambda_2^{a-b} = (\lambda_1 + \lambda_2)^a$, giving:

$$
p_{X+Y}(a) = \frac{(\lambda_1 + \lambda_2)^a}{a!} e^{-(\lambda_1 + \lambda_2)}
$$

### Proof via MGFs

$$
M_{X+Y}(t) = e^{\lambda_1(e^t - 1)} \cdot e^{\lambda_2(e^t - 1)} = e^{(\lambda_1 + \lambda_2)(e^t - 1)}
$$

This is the MGF of $\operatorname{Pois}(\lambda_1 + \lambda_2)$.

### Poisson Process Interpretation

This result is the **merging property**: superimposing independent Poisson processes with rates $\lambda_1$ and $\lambda_2$ gives a Poisson process with rate $\lambda_1 + \lambda_2$.

## Examples

**Example.** Store A sees $\operatorname{Pois}(3)$ customers per hour, store B sees $\operatorname{Pois}(5)$. The total across both stores is $\operatorname{Pois}(8)$ per hour.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 100_000

lam1, lam2 = 3.0, 5.0
X = np.random.poisson(lam1, n_sim)
Y = np.random.poisson(lam2, n_sim)
S = X + Y

lam_sum = lam1 + lam2
print(f"Simulated: mean={S.mean():.4f} (theory {lam_sum})")
print(f"Simulated: var ={S.var():.4f} (theory {lam_sum})")

# Compare PMFs
k_vals = np.arange(0, 20)
pmf_theory = stats.poisson.pmf(k_vals, lam_sum)
pmf_sim = np.bincount(S, minlength=20)[:20] / n_sim

max_diff = np.max(np.abs(pmf_sim - pmf_theory))
print(f"Max |PMF difference|: {max_diff:.4f}")
```
