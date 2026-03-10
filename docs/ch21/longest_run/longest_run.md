# Longest Run

In $n$ fair coin flips, the longest consecutive run of heads (or tails) grows as $\log_2 n$ — surprisingly long streaks are the norm, not the exception.

## Definition

For $n$ iid Bernoulli(0.5) trials, let $R_n$ be the length of the longest run of identical outcomes. Then:

$$
\frac{R_n}{\log_2 n} \xrightarrow{p} 1 \quad \text{as } n \to \infty
$$

The expected longest run is approximately $\log_2 n$.

## Explanation

### Intuition

There are about $n/k$ non-overlapping blocks of length $k$. A block is all-heads with probability $2^{-k}$, so the expected number of all-heads blocks is $n \cdot 2^{-k}/k \approx n \cdot 2^{-k}$. Setting this to 1 gives $k \approx \log_2 n$.

### Practical Implication

People underestimate natural streak lengths. In 10,000 flips, runs of 13-16 are typical ($\log_2 10000 \approx 13.3$). Truly random sequences contain longer streaks than people intuitively expect.

### Exact Distribution

The exact distribution of $R_n$ involves inclusion-exclusion over runs, making it analytically complex. Simulation is the practical approach.

## Examples

**Example.** Simulate longest runs in 10,000 flips, repeated 1,000 times.

```python
import numpy as np

np.random.seed(42)
n = 10_000
n_sim = 1_000

runs = np.zeros(n_sim)
for s in range(n_sim):
    flips = np.random.randint(0, 2, n)
    max_run = current = 1
    for i in range(1, n):
        if flips[i] == flips[i-1]:
            current += 1
            max_run = max(max_run, current)
        else:
            current = 1
    runs[s] = max_run

print(f"Mean longest run: {runs.mean():.2f} (theory ≈ log₂({n}) = {np.log2(n):.2f})")
print(f"Range: [{runs.min():.0f}, {runs.max():.0f}]")
print(f"Std dev: {runs.std():.2f}")
```
