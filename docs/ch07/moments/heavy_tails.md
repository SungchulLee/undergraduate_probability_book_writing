# Heavy Tails and the Moment Problem

Heavy-tailed distributions have excess kurtosis greater than zero. A deeper question — the moment problem — asks whether moments uniquely determine a distribution.

## Definition

A distribution is **heavy-tailed** (leptokurtic) if its excess kurtosis $\gamma_2 = \kappa_4 - 3 > 0$, meaning its tails contain more probability mass than the normal distribution.

The **moment problem** asks: does the sequence $\mu_k = E[X^k]$ for $k = 1, 2, 3, \ldots$ uniquely determine the distribution?

## Explanation

### Excess Kurtosis of Common Distributions

| Distribution | Excess Kurtosis $\gamma_2$ |
|:-------------|:--------------------------:|
| $\text{Uniform}(a,b)$ | $-6/5$ |
| $\text{Normal}$ | $0$ |
| $\text{Exponential}$ | $6$ |
| $\text{Laplace}$ | $3$ |
| $t(\nu)$, $\nu > 4$ | $6/(\nu-4)$ |

### Moment Determinacy

**Sufficient conditions for uniqueness:**

1. **Carleman's condition:** $\sum_{k=1}^{\infty}(E[|X|^{2k}])^{-1/(2k)} = \infty$
2. **MGF exists** in a neighborhood of 0 (implies Carleman's)

**Counterexample:** The log-normal distribution is moment-indeterminate. The family $f_a(x) = f_0(x)[1 + a\sin(2\pi\ln x)]$ for $a \in [-1,1]$ gives different distributions with identical moments.

## Examples

**Example.** The $t(5)$ distribution has excess kurtosis $6/(5-4) = 6$, identical to Exponential(1). But $t(5)$ is symmetric while Exponential is right-skewed — kurtosis alone does not characterize a distribution.

```python
from scipy import stats
import numpy as np

# Compare tail probabilities: Normal vs t(5)
for threshold in [2, 3, 4]:
    p_norm = 2 * stats.norm.sf(threshold)
    p_t5 = 2 * stats.t.sf(threshold, df=5)
    print(f"|X| > {threshold}: Normal={p_norm:.6f}, t(5)={p_t5:.6f}, "
          f"ratio={p_t5/p_norm:.2f}x")
```
