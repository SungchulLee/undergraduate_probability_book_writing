# SLLN Intuition and Connections

The strong law guarantees that deviations from $\mu$ occur only finitely many times — a qualitatively different statement from the weak law, proved via Borel-Cantelli and subsequence arguments.

## Definition

$\bar{X}_n \xrightarrow{a.s.} \mu$ means: with probability 1, for every $\varepsilon > 0$, there exists $N$ (random) such that $\lvert \bar{X}_n - \mu \rvert < \varepsilon$ for all $n \ge N$.

## Explanation

### Borel-Cantelli Strategy

Let $A_n = \{\lvert \bar{X}_n - \mu \rvert > \varepsilon\}$. If $\sum_n P(A_n) < \infty$, then by the first Borel-Cantelli lemma, only finitely many $A_n$ occur a.s., giving $\bar{X}_n \to \mu$ a.s.

**Problem**: Chebyshev gives $P(A_n) \le \sigma^2/(n\varepsilon^2)$, and $\sum 1/n = \infty$ — not summable.

**Solution**: Work along the subsequence $n_k = k^2$, where $\sum 1/k^2 < \infty$. Then show $\bar{X}_n$ between $k^2$ and $(k+1)^2$ stays close to $\bar{X}_{k^2}$.

### Law of the Iterated Logarithm

The LIL gives the exact fluctuation envelope:

$$
\limsup_{n \to \infty} \frac{S_n - n\mu}{\sigma\sqrt{2n \ln \ln n}} = 1 \quad \text{a.s.}
$$

This sits between the CLT ($S_n$ fluctuates like $\sqrt{n}$) and the SLLN ($S_n/n \to \mu$).

### Borel's Theorem

For iid Bernoulli($p$): the relative frequency of success converges a.s. to $p$. This was the first SLLN (Borel, 1909) and formalizes the frequentist interpretation of probability.

## Examples

**Example.** Count violations of $\lvert \bar{X}_n - \mu \rvert > \varepsilon$ — they eventually stop (finitely many).

```python
import numpy as np

np.random.seed(42)
n = 100_000
eps = 0.01

X = np.random.normal(0, 1, n)
means = np.cumsum(X) / np.arange(1, n + 1)
violations = np.abs(means) > eps

last_violation = np.max(np.where(violations)[0]) + 1 if violations.any() else 0
total = violations.sum()
print(f"ε={eps}: {total} violations, last at n={last_violation}")
print(f"Final X̄ = {means[-1]:.6f}")
```
