# Frequentist Interpretation of Probability

The SLLN provides the mathematical foundation for defining probability as long-run relative frequency — repeating an experiment makes the observed frequency converge to the true probability.

## Definition

For iid indicator variables $\mathbf{1}_{A_i}$ of event $A$:

$$
\frac{1}{n}\sum_{i=1}^n \mathbf{1}_{A_i} \xrightarrow{a.s.} P(A)
$$

This is the SLLN applied to $X_i = \mathbf{1}(A_i)$ with $\mu = P(A)$.

## Explanation

### Interpretation

Saying "the probability of heads is 0.5" means: if you flip the coin many times, the fraction of heads converges to 0.5 with probability 1. The LLN converts this from an empirical observation into a theorem.

### Limitation

The frequentist view requires **repeatable** experiments. For one-time events ("probability of rain tomorrow"), the framework is less natural — motivating the Bayesian interpretation.

## Examples

**Example.** Relative frequency of heads converges to 0.5.

```python
import numpy as np

np.random.seed(42)
n = 50_000
flips = np.random.binomial(1, 0.5, n)
freq = np.cumsum(flips) / np.arange(1, n + 1)

for k in [100, 1000, 10000, 50000]:
    print(f"n={k:>5d}: relative frequency = {freq[k-1]:.6f}")
```
