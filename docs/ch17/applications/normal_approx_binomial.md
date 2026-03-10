# Normal Approximation to the Binomial

Since $\operatorname{Bin}(n, p)$ is a sum of iid Bernoulli trials, the CLT provides a normal approximation that avoids computing large binomial coefficients.

## Definition

If $X \sim \operatorname{Bin}(n, p)$, then for large $n$:

$$
X \approx N(np, \; np(1-p))
$$

The approximation is reasonable when both $np \ge 5$ and $n(1-p) \ge 5$.

## Explanation

### Why It Works

Since $X = \sum_{i=1}^n X_i$ with $X_i \sim \operatorname{Bernoulli}(p)$ iid, the CLT gives:

$$
\frac{X - np}{\sqrt{np(1-p)}} \xrightarrow{d} N(0,1)
$$

### Continuity Correction

Since $X$ is integer-valued, apply continuity correction for better accuracy: e.g., $P(X \le k) \approx \Phi\!\left(\frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right)$.

### Comparison with Poisson Approximation

| Regime | Approximation |
|:---|:---|
| $n$ large, $p$ small, $np$ moderate | $\operatorname{Bin}(n,p) \approx \operatorname{Pois}(np)$ |
| $n$ large, $p$ not extreme | $\operatorname{Bin}(n,p) \approx N(np, np(1-p))$ |

## Examples

**Example.** $X \sim \operatorname{Bin}(200, 0.4)$. Find $P(X \le 75)$.

With continuity correction: $z = (75.5 - 80)/\sqrt{48} = -0.6495$, so $P(X \le 75) \approx \Phi(-0.6495) = 0.258$.

```python
from scipy import stats

n, p = 200, 0.4
mu = n * p
sigma = (n * p * (1 - p)) ** 0.5

# Exact
exact = stats.binom.cdf(75, n, p)

# Normal with continuity correction
z_cc = (75.5 - mu) / sigma
approx_cc = stats.norm.cdf(z_cc)

# Normal without CC
z = (75 - mu) / sigma
approx = stats.norm.cdf(z)

print(f"P(X ≤ 75): exact={exact:.4f}, with CC={approx_cc:.4f}, no CC={approx:.4f}")
```
