# Expectation via Indicators

Expressing a counting variable as a sum of indicators and applying linearity of expectation is one of the most powerful techniques in probability.

## Definition

If $X = \sum_{i=1}^m \mathbf{1}_{A_i}$, then by linearity:

$$
E[X] = \sum_{i=1}^m P(A_i)
$$

This works **regardless of dependence** among the indicators.

For variance:

$$
\text{Var}(X) = \sum_i \text{Var}(\mathbf{1}_{A_i}) + 2\sum_{i < j}\text{Cov}(\mathbf{1}_{A_i}, \mathbf{1}_{A_j})
$$

## Explanation

### When Is the Sum Binomial?

$X = \sum \mathbf{1}_{A_i}$ is $\text{Bin}(m, p)$ only if all indicators have the same $p$ and are mutually independent. If either condition fails, $X$ is not Binomial — but the indicator method still gives $E[X]$ and $\text{Var}(X)$.

### Strategy

1. Identify what $X$ counts
2. Write $X = \sum \mathbf{1}_{A_i}$ where $A_i$ = "$i$-th item is counted"
3. Compute $P(A_i)$ (often the same for all $i$ by symmetry)
4. Sum: $E[X] = \sum P(A_i)$

## Examples

**Example 1 (Binomial).** $S = \sum_{i=1}^n \mathbf{1}_{A_i}$ where $\mathbf{1}_{A_i} \stackrel{\text{iid}}{\sim} \text{Bern}(p)$. Then $E[S] = np$, $\text{Var}(S) = np(1-p)$.

**Example 2 (Birthday pairs).** $S_n = \sum_{i<j} \mathbf{1}_{A_{ij}}$ where $P(A_{ij}) = 1/365$. Not binomial (dependent indicators), but $E[S_n] = \binom{n}{2}/365$.

**Example 3 (Empty bins).** $n$ balls into $M$ bins. $S = \sum_{i=1}^M \mathbf{1}_{A_i}$ where $P(A_i) = ((M-1)/M)^n$. Then $E[S] = M((M-1)/M)^n$.

```python
from math import comb

# Birthday pairs
n = 30
E_pairs = comb(n, 2) / 365
print(f"E[birthday pairs, n={n}] = {E_pairs:.4f}")

# Empty bins: 100 balls, 365 bins
n_balls, M = 100, 365
p = ((M-1)/M)**n_balls
E_empty = M * p
print(f"E[empty bins] = {E_empty:.1f}")

# Elevator stops = non-empty bins
E_stops = M * (1 - p)
print(f"E[elevator stops] = {E_stops:.1f}")
```
