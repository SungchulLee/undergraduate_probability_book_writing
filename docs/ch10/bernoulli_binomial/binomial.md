# Binomial Distribution

The binomial distribution counts the number of successes in $n$ independent Bernoulli trials — the most fundamental discrete distribution in probability.

## Definition

$X \sim \text{Bin}(n, p)$ if $X = \sum_{i=1}^n X_i$ where $X_i \stackrel{\text{iid}}{\sim} \text{Bern}(p)$.

**PMF:**

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \qquad k = 0, 1, \ldots, n
$$

**Moments:**

$$
E[X] = np, \qquad \text{Var}(X) = np(1-p)
$$

**MGF:**

$$
M_X(t) = (q + pe^t)^n
$$

## Explanation

### Why the PMF Works

To get exactly $k$ successes: choose which $k$ trials succeed ($\binom{n}{k}$ ways), each with probability $p^k(1-p)^{n-k}$ by independence.

### Sum Property

If $X \sim \text{Bin}(n, p)$ and $Y \sim \text{Bin}(m, p)$ are independent, then $X + Y \sim \text{Bin}(n + m, p)$. This follows from the MGF or from combining independent Bernoulli trials.

### Mode

The most likely value is $\lfloor (n+1)p \rfloor$ or $\lfloor (n+1)p \rfloor - 1$. For large $n$, the mode is near $np$.

### Normal Approximation

For large $n$, by the CLT: $\text{Bin}(n, p) \approx N(np, np(1-p))$. Rule of thumb: the approximation is good when $np \ge 5$ and $n(1-p) \ge 5$.

## Examples

**Example.** 20 fair coin flips. $X \sim \text{Bin}(20, 0.5)$: $E[X] = 10$, $\text{SD}(X) = \sqrt{5} \approx 2.24$.

$$
P(X = 10) = \binom{20}{10}(0.5)^{20} \approx 0.176
$$

```python
import numpy as np
from scipy import stats
from math import comb

n, p = 20, 0.5
X = stats.binom(n, p)

print(f"E[X] = {X.mean():.1f}, SD(X) = {X.std():.4f}")
print(f"P(X=10) = {X.pmf(10):.4f}  (exact: {comb(20,10)*0.5**20:.4f})")
print(f"P(8 <= X <= 12) = {X.cdf(12) - X.cdf(7):.4f}")

# Simulation
np.random.seed(42)
samples = np.random.binomial(n, p, 200_000)
print(f"\nSimulated: E={samples.mean():.3f}, Var={samples.var():.3f}")
print(f"Theory:    E={n*p:.1f}, Var={n*p*(1-p):.1f}")
```
