# Chebyshev's Inequality

Chebyshev's inequality bounds the probability of deviating from the mean by $k$ standard deviations — it works for any distribution with finite variance.

## Definition

For any random variable $X$ with mean $\mu$ and variance $\sigma^2$:

$$
P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}
$$

Equivalently, for $a > 0$:

$$
P(|X - \mu| \ge a) \le \frac{\sigma^2}{a^2}
$$

## Explanation

### Proof

Apply Markov's inequality to the non-negative variable $(X - \mu)^2$:

$$
P(|X-\mu| \ge a) = P((X-\mu)^2 \ge a^2) \le \frac{E[(X-\mu)^2]}{a^2} = \frac{\sigma^2}{a^2}
$$

### Key Values

| $k$ | Upper bound | At least this much within $k\sigma$ |
|:---:|:-----------:|:------------------------------------:|
| 2 | 0.25 | 75% |
| 3 | 0.111 | 88.9% |
| 4 | 0.0625 | 93.75% |

### Application: Weak Law of Large Numbers

For iid $X_1, \ldots, X_n$ with mean $\mu$ and variance $\sigma^2$, the sample mean $\bar{X}_n$ has $\text{Var}(\bar{X}_n) = \sigma^2/n$. By Chebyshev:

$$
P(|\bar{X}_n - \mu| \ge \varepsilon) \le \frac{\sigma^2}{n\varepsilon^2} \to 0
$$

## Examples

**Example.** $X \sim N(0,1)$. Compare Chebyshev bounds to actual normal tail probabilities.

```python
import numpy as np

np.random.seed(42)
X = np.random.normal(0, 1, 1_000_000)

for k in [2, 3, 4, 5]:
    bound = 1 / k**2
    actual = np.mean(np.abs(X) >= k)
    print(f"k={k}: Chebyshev <= {bound:.4f}, actual = {actual:.6f}")
```
