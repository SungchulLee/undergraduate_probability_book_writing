# Coin Flip from Uniform Samples

Converting a uniform random variable into a Bernoulli trial is the simplest instance of the inverse CDF method — the building block for all discrete simulation.

## Definition

Given $U \sim U(0,1)$ and success probability $p$:

$$
B = \mathbf{1}(U > 1 - p) = \begin{cases} 1 & U > 1-p \\ 0 & U \le 1-p \end{cases}
$$

Then $B \sim \operatorname{Bernoulli}(p)$, since $P(B = 1) = P(U > 1-p) = p$.

## Explanation

### Why It Works

The CDF of $\operatorname{Bernoulli}(p)$ is $F(0) = 1-p$, $F(1) = 1$. Setting $B = \mathbf{1}(U > 1-p)$ is the generalized inverse CDF applied to $U$: whenever $U$ falls in $(1-p, 1]$, output 1; otherwise output 0.

### Extension to General Discrete

For any discrete distribution on $\{x_1, x_2, \ldots\}$ with probabilities $p_1, p_2, \ldots$, partition $[0,1)$ into intervals of lengths $p_i$ and assign $X = x_k$ when $U$ falls in the $k$-th interval.

## Examples

**Example.** Generate 10,000 Bernoulli(0.499) samples and verify.

```python
import numpy as np

np.random.seed(42)
n = 10_000
p = 0.499

U = np.random.rand(n)
B = (U > 1 - p).astype(int)

print(f"Sample mean: {B.mean():.4f} (theory: {p})")
print(f"First 20 U: {U[:5].round(3)}")
print(f"First 20 B: {B[:5]}")
```
