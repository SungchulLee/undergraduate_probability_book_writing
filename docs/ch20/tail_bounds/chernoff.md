# Chernoff Bound

By exponentiating and applying Markov's inequality, Chernoff's bound leverages the full MGF to produce exponentially decaying tail bounds — far tighter than Chebyshev for large deviations.

## Definition

For any random variable $X$ and $a > 0$:

$$
P(X \ge a) \le \min_{t > 0} \frac{M_X(t)}{e^{ta}}
$$

where $M_X(t) = E[e^{tX}]$ is the moment generating function.

## Explanation

### Proof

For any $t > 0$: $X \ge a \iff e^{tX} \ge e^{ta}$. By Markov:

$$
P(X \ge a) = P(e^{tX} \ge e^{ta}) \le \frac{E[e^{tX}]}{e^{ta}} = \frac{M_X(t)}{e^{ta}}
$$

Optimizing over $t > 0$ gives the tightest bound.

### Why It Excels for Large Deviations

Chernoff uses the MGF, which encodes all moments. The optimization over $t$ adapts the bound to the specific threshold, typically giving exponential decay in the deviation size. For moderate deviations near the mean, it can be loose.

### Comparison Table for Bin(1000, 0.01)

| Bound | $P(X \ge 20)$ | $P(X \ge 100)$ |
|:---|:---|:---|
| Markov | $\le 0.50$ | $\le 0.10$ |
| Chebyshev | $\le 0.099$ | $\le 0.0012$ |
| Cantelli | $\le 0.090$ | $\le 0.0012$ |
| Chernoff | $\le 0.021$ | $\le 1.2 \times 10^{-61}$ |

## Examples

**Example.** Chernoff bound for $X \sim \operatorname{Pois}(100)$ at $P(X \ge 200)$.

Using $M_X(t) = e^{\lambda(e^t - 1)}$ with $t = \ln 2$:

$$
P(X \ge 200) \le \frac{e^{100(2-1)}}{2^{200}} = \frac{e^{100}}{2^{200}} \approx 1.67 \times 10^{-17}
$$

```python
import numpy as np
from scipy import stats

lam = 100
a = 200

# Chernoff with t = ln(a/lam)
t_opt = np.log(a / lam)
chernoff = np.exp(lam * (np.exp(t_opt) - 1) - t_opt * a)

exact = 1 - stats.poisson.cdf(a - 1, lam)
markov = lam / a
chebyshev = lam / (a - lam)**2

print(f"P(X ≥ {a}): exact={exact:.2e}")
print(f"Markov:    ≤ {markov:.4f}")
print(f"Chebyshev: ≤ {chebyshev:.4f}")
print(f"Chernoff:  ≤ {chernoff:.2e}")
```
