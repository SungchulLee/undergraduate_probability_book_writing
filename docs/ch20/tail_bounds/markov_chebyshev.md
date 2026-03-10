# Markov and Chebyshev Inequalities

Upper bounds on tail probabilities using only moments — Markov uses the mean, Chebyshev uses the variance, and both are tools for proving the law of large numbers.

## Definition

**Markov's inequality.** For nonnegative $X$ and $a > 0$:

$$
P(X \ge a) \le \frac{E[X]}{a}
$$

**Chebyshev's inequality.** For any $X$ with mean $\mu$ and variance $\sigma^2$, and $\varepsilon > 0$:

$$
P(|X - \mu| \ge \varepsilon) \le \frac{\sigma^2}{\varepsilon^2}
$$

## Explanation

### Proof of Chebyshev from Markov

Apply Markov to $(X - \mu)^2$:

$$
P(|X - \mu| \ge \varepsilon) = P((X-\mu)^2 \ge \varepsilon^2) \le \frac{E[(X-\mu)^2]}{\varepsilon^2} = \frac{\sigma^2}{\varepsilon^2}
$$

### Strength Comparison

Markov uses only the first moment; Chebyshev uses the second. Chebyshev is always at least as tight for two-sided bounds, and often much tighter.

### Application to WLLN

For $\bar{X}_n$ with variance $\sigma^2/n$:

$$
P(|\bar{X}_n - \mu| \ge \varepsilon) \le \frac{\sigma^2}{n\varepsilon^2} \to 0
$$

This one-line proof establishes the Weak Law.

## Examples

**Example.** $X \sim \operatorname{Bin}(1000, 0.01)$: $\mu = 10$, $\sigma^2 = 9.9$.

```python
from scipy import stats

n, p = 1000, 0.01
mu, var = n * p, n * p * (1 - p)

for threshold in [20, 100]:
    exact = 1 - stats.binom.cdf(threshold - 1, n, p)
    markov = mu / threshold
    chebyshev = var / (threshold - mu)**2
    print(f"P(X ≥ {threshold}): exact={exact:.6f}, "
          f"Markov≤{markov:.4f}, Chebyshev≤{min(chebyshev, 1):.4f}")
```
