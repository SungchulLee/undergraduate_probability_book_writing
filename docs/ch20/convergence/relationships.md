# Relationships Between Convergence Modes

Almost sure convergence implies convergence in probability, which implies convergence in distribution — a strict hierarchy with no reverse implications in general.

## Definition

The implication chain:

$$
X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{p} X \implies X_n \xrightarrow{d} X
$$

**Special case**: $X_n \xrightarrow{d} c \iff X_n \xrightarrow{p} c$ when the limit is a constant.

## Explanation

### Summary Table

| Mode | Notation | What converges |
|:---|:---:|:---|
| Almost sure | $X_n \xrightarrow{a.s.} X$ | Sample paths (with prob. 1) |
| In probability | $X_n \xrightarrow{p} X$ | Tail probabilities to 0 |
| In distribution | $X_n \xrightarrow{d} X$ | CDFs pointwise |

### Why Reverse Fails

The **typewriter sequence** gives convergence in probability but not a.s.: indicators of intervals cycling through $[0,1]$ with shrinking width satisfy $X_n \xrightarrow{p} 0$, but $X_n(\omega) = 1$ infinitely often for every $\omega$.

### Constant Limit Exception

When $X_n \xrightarrow{d} c$ (a constant), the CDF of the limit is a step function, and convergence of CDFs forces $P(\lvert X_n - c \rvert > \varepsilon) \to 0$.

## Examples

**Example.** The LLN gives $\bar{X}_n \xrightarrow{p} \mu$ (constant limit), so convergence in distribution also holds.

```python
import numpy as np

np.random.seed(42)
n_sim = 50_000

# Demonstrate all three modes for sample mean
for n in [50, 500, 5000]:
    means = np.random.exponential(1.0, (n_sim, n)).mean(axis=1)
    p_dev = np.mean(np.abs(means - 1.0) > 0.05)
    print(f"n={n:5d}: P(|X̄-1|>0.05) = {p_dev:.4f}")
```
