# Classic Indicator Examples

Three classic applications of indicator decomposition: the matching problem, birthday pairs, and empty bins.

## Definition

In each example, a counting variable $X$ is decomposed as $X = \sum \mathbf{1}_{A_i}$, and $E[X]$ and $\text{Var}(X)$ are computed via linearity and the covariance formula.

## Explanation

### Matching Problem (Derangements)

A hat-check person returns $n$ hats at random. $X = \sum_{i=1}^n \mathbf{1}_{A_i}$ counts correct matches.

$P(A_i) = 1/n$, so $E[X] = 1$ for all $n$.

$P(A_i \cap A_j) = 1/(n(n-1))$ for $i \ne j$, giving $\text{Cov}(\mathbf{1}_{A_i}, \mathbf{1}_{A_j}) = 1/(n^2(n-1))$.

$$
\text{Var}(X) = n \cdot \frac{1}{n}\cdot\frac{n-1}{n} + 2\binom{n}{2}\cdot\frac{1}{n^2(n-1)} = \frac{n-1}{n} + \frac{1}{n} = 1
$$

Remarkably: $E[X] = 1$ and $\text{Var}(X) = 1$ for all $n$.

### Birthday Pairs

$S = \sum_{i<j}\mathbf{1}_{A_{ij}}$ with $P(A_{ij}) = 1/365$. Disjoint pairs are independent, so:

$$
E[S] = \binom{n}{2}/365, \qquad \text{Var}(S) = \binom{n}{2}\cdot\frac{1}{365}\cdot\frac{364}{365}
$$

### Empty Bins

$n$ balls, $M$ bins. $S = \sum_{i=1}^M \mathbf{1}_{A_i}$ with $p = ((M-1)/M)^n$.

Indicators are dependent: $P(A_i \cap A_j) = ((M-2)/M)^n \ne p^2$.

$$
\text{Var}(S) = Mp(1-p) + 2\tbinom{M}{2}\!\left[((M-2)/M)^n - p^2\right]
$$

The elevator problem: stops $= M - S$, so $E[\text{stops}] = M(1 - p)$, $\text{Var}(\text{stops}) = \text{Var}(S)$.

## Examples

**Example.** Matching problem with $n = 10$.

$E[X] = 1$, $\text{SD}(X) = 1$. By Chebyshev: $P(X \ge 4) \le P(|X-1| \ge 3) \le 1/9$.

```python
import numpy as np
from math import comb, factorial

# Matching problem: simulate
np.random.seed(42)
n = 10
N_sim = 100_000
matches = []
for _ in range(N_sim):
    perm = np.random.permutation(n)
    matches.append(sum(perm[i] == i for i in range(n)))

matches = np.array(matches)
print(f"Matching (n={n}): E={matches.mean():.4f} (theory: 1)")
print(f"  Var={matches.var():.4f} (theory: 1)")

# Empty bins: 100 balls, 365 bins
n_balls, M = 100, 365
p = ((M-1)/M)**n_balls
p2 = ((M-2)/M)**n_balls
E_empty = M * p
Var_empty = M*p*(1-p) + 2*comb(M,2)*(p2 - p**2)
print(f"\nEmpty bins: E={E_empty:.1f}, SD={np.sqrt(Var_empty):.1f}")
```
