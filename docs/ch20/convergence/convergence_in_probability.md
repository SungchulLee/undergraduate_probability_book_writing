# Convergence in Probability

A sequence of random variables converges in probability to a limit if the chance of large deviations vanishes — the mode of convergence used in the Weak Law of Large Numbers.

## Definition

$X_n \xrightarrow{p} X$ if for every $\varepsilon > 0$:

$$
\lim_{n \to \infty} P(|X_n - X| > \varepsilon) = 0
$$

## Explanation

### Intuition

For any tolerance $\varepsilon$, the probability that $X_n$ deviates from $X$ by more than $\varepsilon$ goes to zero. Large deviations become increasingly unlikely, though they are not completely ruled out for any finite $n$.

### Key Properties

| Property | Statement |
|:---|:---|
| Implies convergence in distribution | $X_n \xrightarrow{p} X \implies X_n \xrightarrow{d} X$ |
| Constant limit equivalence | $X_n \xrightarrow{d} c \iff X_n \xrightarrow{p} c$ |
| Preserved under continuous maps | $X_n \xrightarrow{p} X \implies g(X_n) \xrightarrow{p} g(X)$ for continuous $g$ |

### WLLN Connection

The sample mean $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ of iid random variables with finite variance satisfies $\bar{X}_n \xrightarrow{p} \mu$ — this is the Weak Law.

## Examples

**Example.** Verify convergence in probability for the sample mean of $\operatorname{Exp}(1)$ variables.

```python
import numpy as np

np.random.seed(42)
n_sim = 50_000
mu = 1.0

for n in [10, 100, 1000, 10000]:
    means = np.random.exponential(1.0, (n_sim, n)).mean(axis=1)
    for eps in [0.1, 0.01]:
        p = np.mean(np.abs(means - mu) > eps)
        print(f"n={n:5d}, ε={eps}: P(|X̄-μ|>ε) = {p:.4f}")
```
