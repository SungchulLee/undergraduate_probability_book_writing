# Convergence in Distribution

A sequence of random variables converges in distribution if the CDFs converge pointwise — the weakest and most commonly used mode of convergence in the CLT.

## Definition

$X_n \xrightarrow{d} X$ (**convergence in distribution**) if:

$$
\lim_{n \to \infty} F_{X_n}(x) = F_X(x)
$$

for every $x$ at which $F_X$ is continuous. Equivalently, $E[g(X_n)] \to E[g(X)]$ for all bounded continuous functions $g$.

## Explanation

### Intuition

Convergence in distribution says the histograms of $X_n$ look increasingly like the density of $X$. It makes no statement about the random variables being defined on the same probability space — only the **distributions** matter.

### MGF Characterization

A powerful tool for proving convergence in distribution:

If $M_{X_n}(t) \to M_X(t)$ for all $t$ in a neighborhood of $0$, and $M_X$ is the MGF of a random variable $X$, then $X_n \xrightarrow{d} X$.

This **continuity theorem** is the key technique in the MGF proof of the CLT.

### Key Examples

| Sequence | Limit | Mechanism |
|:---|:---|:---|
| Standardized $\operatorname{Bin}(n, p)$ | $N(0,1)$ | CLT for Bernoulli sums |
| Standardized $\operatorname{Pois}(n)$ | $N(0,1)$ | CLT for Poisson(1) sums |
| Uniform on $\{1/n, 2/n, \ldots, 1\}$ | $U(0,1)$ | Discrete grid refining |

## Examples

**Example.** Verify that standardized $\operatorname{Bin}(n, 0.3)$ converges to $N(0,1)$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
p = 0.3

for n in [10, 50, 200, 1000]:
    X = np.random.binomial(n, p, 100_000)
    Z = (X - n * p) / np.sqrt(n * p * (1 - p))
    ks_stat, pval = stats.kstest(Z, 'norm')
    print(f"n={n:5d}: KS stat={ks_stat:.4f}, p-value={pval:.4f}")
```
