# Geometric Distribution

The geometric distribution counts the number of trials until the first success — the discrete analogue of the exponential distribution.

## Definition

$X \sim \text{Geo}(p)$ if $X$ is the number of trials until the first success in independent Bernoulli($p$) trials.

**PMF:**

$$
P(X = k) = (1-p)^{k-1}p, \qquad k = 1, 2, 3, \ldots
$$

**CDF:**

$$
P(X \le k) = 1 - (1-p)^k
$$

**Moments:**

$$
E[X] = \frac{1}{p}, \qquad \text{Var}(X) = \frac{1-p}{p^2}
$$

**MGF:**

$$
M_X(t) = \frac{pe^t}{1 - (1-p)e^t}, \qquad t < -\ln(1-p)
$$

## Explanation

### Tail Probability

The survival function has a clean form: $P(X > k) = (1-p)^k$. This says: surviving $k$ trials means failing all $k$, each with probability $1 - p$.

### Deriving the Mean

**Via tail sum:** $E[X] = \sum_{k=0}^{\infty} P(X > k) = \sum_{k=0}^{\infty}(1-p)^k = 1/p$.

**Via first-step analysis:** $E[X] = p \cdot 1 + (1-p)(1 + E[X])$, solving gives $E[X] = 1/p$.

### Convention Warning

Some textbooks define the geometric as the number of *failures* before the first success, giving $P(Y = k) = (1-p)^k p$ for $k = 0, 1, 2, \ldots$ and $E[Y] = (1-p)/p$. We use the "number of trials" convention throughout.

## Examples

**Example.** Roll a fair die until a 6 appears. $X \sim \text{Geo}(1/6)$: $E[X] = 6$, $\text{SD}(X) = \sqrt{30} \approx 5.48$.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000
p = 1/6

samples = np.random.geometric(p, n_sim)
print(f"E[X] = {samples.mean():.3f}  (theory: {1/p:.1f})")
print(f"Var(X) = {samples.var():.2f}  (theory: {(1-p)/p**2:.2f})")
print(f"P(X > 6) = {np.mean(samples > 6):.4f}  (theory: {(1-p)**6:.4f})")
```
