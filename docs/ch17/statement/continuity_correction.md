# Continuity Correction

When approximating a discrete distribution with the continuous normal, shifting boundaries by $\pm 0.5$ accounts for the gap between integer values and continuous density.

## Definition

For a discrete random variable $X$ taking integer values, the **continuity correction** adjusts the normal approximation as follows:

| Discrete probability | Continuity-corrected form |
|:---|:---|
| $P(X \le k)$ | $P(Y \le k + 0.5)$ |
| $P(X \ge k)$ | $P(Y \ge k - 0.5)$ |
| $P(X < k)$ | $P(Y \le k - 0.5)$ |
| $P(X > k)$ | $P(Y \ge k + 0.5)$ |
| $P(X = k)$ | $P(k - 0.5 \le Y \le k + 0.5)$ |

where $Y \sim N(\mu, \sigma^2)$ is the normal approximation to $X$.

## Explanation

### Why It Helps

Each integer $k$ "occupies" the interval $[k - 0.5, k + 0.5]$ in the continuous approximation. Without the correction, $P(X \le k)$ maps to $P(Y \le k)$, which misses half the probability mass at $k$ itself.

### When to Use

- **Use** when approximating discrete distributions (Binomial, Poisson, etc.) with the normal
- **Skip** when the original variable is already continuous

### Diminishing Importance

For large $n$, the correction $\pm 0.5$ is small relative to the standard deviation $\sigma\sqrt{n}$, so its effect diminishes. It matters most for moderate $n$.

## Examples

**Example.** $X \sim \operatorname{Pois}(100)$. Find $P(X \ge 120)$.

- Without correction: $z = (120 - 100)/10 = 2.0$, giving $1 - \Phi(2.0) = 0.0228$
- With correction: $z = (119.5 - 100)/10 = 1.95$, giving $1 - \Phi(1.95) = 0.0256$
- Exact: $P(X \ge 120) = 0.0282$

The corrected answer ($0.0256$) is closer to the exact value.

```python
from scipy import stats

lam = 100

exact = 1 - stats.poisson.cdf(119, lam)
no_cc = 1 - stats.norm.cdf((120 - lam) / lam**0.5)
with_cc = 1 - stats.norm.cdf((119.5 - lam) / lam**0.5)

print(f"Exact:      {exact:.4f}")
print(f"No CC:      {no_cc:.4f}")
print(f"With CC:    {with_cc:.4f}")
```
