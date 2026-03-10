# Buffon's Needle

A needle of length 1 dropped on parallel lines spaced 1 apart crosses a line with probability $2/\pi$ — connecting geometric probability to the LLN for estimating $\pi$.

## Definition

Drop a unit needle on unit-spaced parallel lines. The crossing probability is:

$$
P(\text{cross}) = \frac{1}{\pi}\int_0^{\pi} \sin\theta \, d\theta = \frac{2}{\pi}
$$

where $\theta \sim U(0, \pi)$ is the needle angle. By the SLLN:

$$
\pi \approx \frac{2n}{\sum_{i=1}^n R_i}
$$

where $R_i = \mathbf{1}(\text{needle } i \text{ crosses a line})$.

## Explanation

### Setup

The needle position is determined by:

- $Y \sim U(0, 1)$: height of the lower end
- $\Theta \sim U(0, \pi)$: angle from horizontal

The needle crosses the line at $y = 1$ iff $Y + \sin\Theta \ge 1$.

### Computing the Probability

$$
P(\text{cross}) = \int_0^{\pi} P(Y \ge 1 - \sin\theta) \frac{d\theta}{\pi} = \frac{1}{\pi}\int_0^{\pi} \sin\theta \, d\theta = \frac{2}{\pi}
$$

### LLN Application

$R_i$ are iid $\operatorname{Bernoulli}(2/\pi)$, so $\bar{R}_n \xrightarrow{a.s.} 2/\pi$, giving $\hat{\pi}_n = 2/\bar{R}_n \xrightarrow{a.s.} \pi$.

## Examples

**Example.** Simulate Buffon's needle to estimate $\pi$.

```python
import numpy as np

np.random.seed(42)
n = 100_000

Y = np.random.uniform(0, 1, n)
theta = np.random.uniform(0, np.pi, n)
crosses = (Y + np.sin(theta)) >= 1

pi_hat = 2 * n / crosses.sum()
print(f"Crosses: {crosses.sum()} / {n} = {crosses.mean():.4f} (theory: {2/np.pi:.4f})")
print(f"π estimate: {pi_hat:.6f} (true: {np.pi:.6f})")
```
