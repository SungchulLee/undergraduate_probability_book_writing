# Convergence Modes (Preview)

Convergence in distribution is the weakest of three standard modes; stronger notions (in probability, almost sure) are needed for the law of large numbers.

## Definition

| Mode | Notation | Meaning |
|:---|:---:|:---|
| Almost sure | $X_n \xrightarrow{a.s.} X$ | Sample paths converge for almost every $\omega$ |
| In probability | $X_n \xrightarrow{p} X$ | $P(\lvert X_n - X \rvert > \varepsilon) \to 0$ for all $\varepsilon > 0$ |
| In distribution | $X_n \xrightarrow{d} X$ | CDFs converge pointwise at continuity points |

The implication hierarchy:

$$
X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{p} X \implies X_n \xrightarrow{d} X
$$

Reverse implications are **not** true in general.

## Explanation

### Special Case: Constant Limits

If $X_n \xrightarrow{d} c$ where $c$ is a **constant**, then $X_n \xrightarrow{p} c$ as well. Convergence in distribution to a constant is the same as convergence in probability.

### CLT vs LLN

- **CLT** (this chapter): $\frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0,1)$ — convergence in distribution
- **WLLN** (Chapter 20): $\bar{X}_n \xrightarrow{p} \mu$ — convergence in probability
- **SLLN** (Chapter 20): $\bar{X}_n \xrightarrow{a.s.} \mu$ — almost sure convergence

??? note "Full treatment"
    The detailed comparison, including proofs of the implication hierarchy and counterexamples showing the reverse implications fail, is presented in Chapter 20.

## Examples

**Example.** $\bar{X}_n \to \mu$ in probability (LLN) vs the CLT rescaling.

```python
import numpy as np

np.random.seed(42)
n_sim = 50_000
mu, sigma = 5.0, 2.0

for n in [10, 100, 1000, 10000]:
    X_bar = np.random.normal(mu, sigma, (n_sim, n)).mean(axis=1)
    p_dev = np.mean(np.abs(X_bar - mu) > 0.1)
    print(f"n={n:5d}: P(|X̄ - μ| > 0.1) = {p_dev:.4f}")
```
