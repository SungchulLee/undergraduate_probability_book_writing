# One-Sided Chebyshev Inequality

Also called the Cantelli inequality, this bounds a single tail more tightly than the two-sided Chebyshev by optimizing a shift parameter.

## Definition

For $X$ with mean $\mu$ and variance $\sigma^2$, and $\varepsilon > 0$:

$$
P(X - \mu \ge \varepsilon) \le \frac{\sigma^2}{\sigma^2 + \varepsilon^2}
$$

The same bound holds for $P(X - \mu \le -\varepsilon)$.

## Explanation

### Proof

For any $b > 0$: $X - \mu \ge \varepsilon \implies (X - \mu + b)^2 \ge (\varepsilon + b)^2$. By Markov:

$$
P(X - \mu \ge \varepsilon) \le \frac{E[(X - \mu + b)^2]}{(\varepsilon + b)^2} = \frac{\sigma^2 + b^2}{(\varepsilon + b)^2}
$$

Minimizing over $b > 0$ gives $b^* = \sigma^2 / \varepsilon$, yielding $\sigma^2/(\sigma^2 + \varepsilon^2)$.

### Comparison with Chebyshev

Since $\frac{\sigma^2}{\sigma^2 + \varepsilon^2} < \frac{\sigma^2}{\varepsilon^2}$, the one-sided bound is always tighter than the two-sided Chebyshev (which bounds both tails combined).

## Examples

**Example.** $X \sim \operatorname{Bin}(1000, 0.01)$: bound $P(X \ge 20) = P(X - 10 \ge 10)$.

$$
\frac{9.9}{9.9 + 100} = 0.0901 \quad \text{(vs Chebyshev: } 0.0990\text{)}
$$

```python
from scipy import stats

n, p = 1000, 0.01
mu, var = n * p, n * p * (1 - p)

for threshold in [20, 100]:
    eps = threshold - mu
    exact = 1 - stats.binom.cdf(threshold - 1, n, p)
    cantelli = var / (var + eps**2)
    chebyshev = var / eps**2
    print(f"P(X ≥ {threshold}): exact={exact:.6f}, "
          f"Cantelli≤{cantelli:.4f}, Chebyshev≤{min(chebyshev, 1):.4f}")
```
