# Hypergeometric Distribution

The hypergeometric distribution counts successes in draws without replacement — the finite-population analogue of the binomial.

## Definition

Draw $n$ items without replacement from a population of $N$ containing $K$ successes. The number of successes $X \sim \text{HGeom}(N, K, n)$ has

**PMF:**

$$
P(X = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}, \qquad \max(0, n-N+K) \le k \le \min(n, K)
$$

**Moments:**

$$
E[X] = n\frac{K}{N}, \qquad \text{Var}(X) = n\frac{K}{N}\frac{N-K}{N}\frac{N-n}{N-1}
$$

## Explanation

### PMF Intuition

The PMF counts favorable arrangements over total arrangements. To get $k$ successes: choose $k$ of $K$ success items ($\binom{K}{k}$) and $n-k$ of $N-K$ failure items ($\binom{N-K}{n-k}$), out of $\binom{N}{n}$ total ways to draw $n$ items.

### Variance and Finite Population Correction

The variance has the same $npq$ form as the binomial (with $p = K/N$), multiplied by the **finite population correction** $(N-n)/(N-1)$. This factor is less than 1 when $n > 1$, reflecting reduced variability from sampling without replacement.

- When $n = 1$: correction = 1, same as binomial
- When $n = N$: correction = 0, no randomness (you draw the entire population)

### Support Constraints

The support $\max(0, n - N + K) \le k \le \min(n, K)$ reflects physical constraints: you can't draw more successes than exist ($k \le K$), more than you draw ($k \le n$), and you must draw enough successes if failures are insufficient ($k \ge n - N + K$).

## Examples

**Example.** Draw 5 cards from a standard deck. $X$ = number of aces. $X \sim \text{HGeom}(52, 4, 5)$.

$$
E[X] = 5 \cdot \frac{4}{52} = \frac{5}{13} \approx 0.385
$$

$$
P(X = 2) = \frac{\binom{4}{2}\binom{48}{3}}{\binom{52}{5}} = \frac{6 \cdot 17296}{2598960} \approx 0.0399
$$

```python
import numpy as np
from scipy import stats
from math import comb

N, K, n = 52, 4, 5
X = stats.hypergeom(N, K, n)

print(f"E[X] = {X.mean():.4f}  (theory: {n*K/N:.4f})")
print(f"Var(X) = {X.var():.6f}")

fpc = (N - n) / (N - 1)
var_theory = n * K/N * (N-K)/N * fpc
print(f"Var (formula) = {var_theory:.6f}")

# PMF check
for k in range(5):
    pmf_exact = comb(K, k) * comb(N-K, n-k) / comb(N, n)
    print(f"P(X={k}) = {pmf_exact:.6f}  (scipy: {X.pmf(k):.6f})")
```
