# Gambler's Fallacy

The mistaken belief that random outcomes must "balance out" confuses the LLN's dilution mechanism with a nonexistent compensating force.

## Definition

The **gambler's fallacy** is the erroneous belief that if a random event has occurred more frequently than expected, it becomes less likely in the future — as if the process has memory.

## Explanation

### What the LLN Actually Says

The LLN says $\bar{X}_n \to \mu$ through **dilution**: past deviations become negligible relative to the growing number of observations. It does **not** say future outcomes compensate for past ones.

After 10 heads in a row: $\bar{X}_{10} = 1.0$. The LLN predicts convergence to 0.5 because:

$$
\bar{X}_n = \frac{10 + \text{(future heads in next } n-10 \text{ flips)}}{n} \to 0.5
$$

The fixed excess of 10 is diluted by $n$, not corrected by biased future flips.

### The Key Distinction

| | Gambler's fallacy | LLN |
|:---|:---|:---|
| Mechanism | Future compensates for past | New data dilutes past |
| Independence | Violated | Maintained |
| Next flip after 10H | "Tails is due" | Still 50-50 |

## Examples

**Example.** After a streak, the coin is still fair.

```python
import numpy as np

np.random.seed(42)
n_sim = 100_000

# After 10 heads, what fraction of next 1000 flips are heads?
next_1000 = np.random.binomial(1000, 0.5, n_sim)
print(f"Mean heads in next 1000 (after 10H streak): {next_1000.mean():.2f}")
print(f"This is 50%, confirming independence")
```
