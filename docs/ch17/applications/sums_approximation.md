# Approximating Sums

The CLT provides a general recipe for approximating tail probabilities of sums of iid random variables — standardize, then look up $\Phi$.

## Definition

For iid $X_1, \ldots, X_n$ with mean $\mu$ and variance $\sigma^2$:

$$
P(S_n \le a) \approx \Phi\!\left(\frac{a - n\mu}{\sigma\sqrt{n}}\right)
$$

where $S_n = \sum_{k=1}^n X_k$ and $\Phi$ is the standard normal CDF.

## Explanation

### Recipe

**Step 1.** Identify $\mu = E[X_i]$ and $\sigma^2 = \operatorname{Var}(X_i)$.

**Step 2.** Standardize: $z = \frac{a - n\mu}{\sigma\sqrt{n}}$.

**Step 3.** Compute $\Phi(z)$ (or $1 - \Phi(z)$ for upper tails).

For discrete $X_i$, apply continuity correction: shift $a$ by $\pm 0.5$.

### Random Walk Connection

For $Y_i = \pm 1$ equally likely ($\mu = 0$, $\sigma^2 = 1$):

| Quantity | Distribution |
|:---|:---|
| $\sum_{i=1}^n Y_i$ | $\approx N(0, n)$ |
| $\frac{1}{\sqrt{n}} \sum_{i=1}^n Y_i$ | $\approx N(0, 1)$ |
| $\frac{1}{\sqrt{n}} \sum_{i=1}^{\lfloor nt \rfloor} Y_i$ | $\approx N(0, t)$ |

The last line previews **Brownian motion**: the continuous-time limit of the scaled random walk, with $B(t) \sim N(0, t)$ and independent increments.

## Examples

**Example.** An instructor grades 25 exams; each takes mean 20 min, SD 4 min. Find $P(S_{25} \le 450)$.

$$
z = \frac{450 - 500}{4\sqrt{25}} = \frac{-50}{20} = -2.5
$$

So $P(S_{25} \le 450) \approx \Phi(-2.5) = 0.0062$.

```python
import numpy as np
from scipy import stats

mu, sigma, n = 20, 4, 25
a = 450

z = (a - n * mu) / (sigma * np.sqrt(n))
p = stats.norm.cdf(z)
print(f"z = {z:.2f}, P(S_25 ≤ 450) ≈ {p:.4f}")

# Simulation
np.random.seed(42)
sums = np.random.normal(mu, sigma, (100_000, n)).sum(axis=1)
print(f"Simulated: {np.mean(sums <= a):.4f}")
```
