# Almost Sure Convergence

With probability one, the entire sample path of $X_n$ converges to the limit — the strongest standard mode of convergence, used in the Strong Law.

## Definition

$X_n \xrightarrow{a.s.} X$ if:

$$
P\!\left(\lim_{n \to \infty} X_n = X\right) = 1
$$

This is also called **convergence with probability 1**.

## Explanation

### Comparison with Convergence in Probability

| | Convergence in probability | Almost sure convergence |
|:---|:---|:---|
| Statement | $P(\lvert X_n - X \rvert > \varepsilon) \to 0$ for each $\varepsilon$ | $P(X_n \to X) = 1$ |
| Allows | Infinitely many deviations (if rare enough) | Only finitely many deviations |
| Strength | Weaker | Stronger |

Almost sure convergence implies convergence in probability, but not conversely.

### Visual Intuition

- **SLLN (a.s.)**: A single sequence of coin flips — the running average converges to 0.5 and eventually stays close
- **WLLN (in prob.)**: Repeat the experiment many times — the histogram of sample means concentrates around 0.5

### SLLN Connection

For iid $X_i$ with $E[\lvert X_i \rvert] < \infty$: $\bar{X}_n \xrightarrow{a.s.} \mu$.

## Examples

**Example.** Multiple sample paths of $\bar{X}_n$ for $\operatorname{Exp}(1)$ — all converge to $\mu = 1$.

```python
import numpy as np

np.random.seed(42)
n = 10_000

for path in range(5):
    samples = np.random.exponential(1.0, n)
    running_mean = np.cumsum(samples) / np.arange(1, n + 1)
    final_dev = abs(running_mean[-1] - 1.0)
    print(f"Path {path+1}: X̄_{n} = {running_mean[-1]:.6f}, |X̄-μ| = {final_dev:.6f}")
```
