# Memoryless Property

The geometric distribution is the only discrete distribution with no memory — past failures provide no information about future waiting time.

## Definition

$X$ is **memoryless** if for all $s, t \ge 0$:

$$
P(X > s + t \mid X > s) = P(X > t)
$$

The geometric distribution is the **unique** discrete distribution satisfying this property.

## Explanation

### Proof for Geometric

Using $P(X > k) = (1-p)^k$:

$$
P(X > s + t \mid X > s) = \frac{P(X > s + t)}{P(X > s)} = \frac{(1-p)^{s+t}}{(1-p)^s} = (1-p)^t = P(X > t)
$$

### Intuition

If you have been flipping a coin for $s$ rounds without heads, the probability of waiting at least $t$ more rounds is the same as if you were starting fresh. The coin does not remember its past.

### Uniqueness

If $P(X > s + t) = P(X > s)\,P(X > t)$ for all non-negative integers $s, t$, then $P(X > k) = (P(X > 1))^k$, which is the geometric survival function with $q = P(X > 1)$.

### Continuous Analogue

The exponential distribution is the unique continuous memoryless distribution: $P(X > s + t \mid X > s) = P(X > t)$ for all $s, t \ge 0$.

## Examples

**Example.** A light bulb has geometric lifetime with $p = 0.01$ (fails each day with probability 1%). Given it has survived 100 days, the probability of surviving another 50 days is $(0.99)^{50} \approx 0.605$ — the same as a brand-new bulb surviving 50 days.

```python
import numpy as np

np.random.seed(42)
n_sim = 500_000
p = 0.01

X = np.random.geometric(p, n_sim)

# P(X > 150 | X > 100) should equal P(X > 50)
p_conditional = np.mean(X[X > 100] > 150)
p_fresh = np.mean(X > 50)
theory = (1 - p)**50

print(f"P(X > 150 | X > 100) = {p_conditional:.4f}")
print(f"P(X > 50)            = {p_fresh:.4f}")
print(f"Theory: (0.99)^50    = {theory:.4f}")
```
