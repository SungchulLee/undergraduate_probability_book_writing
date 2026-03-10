# Linearity of Expectation for Sums

The mean of a sum always equals the sum of the means — no independence required.

## Definition

For any random variables $X_1, \ldots, X_n$ and constants $a_1, \ldots, a_n$:

$$
E\!\left[\sum_{i=1}^n a_i X_i\right] = \sum_{i=1}^n a_i\,E[X_i]
$$

This holds regardless of the dependence structure among the $X_i$.

## Explanation

### Why No Independence Is Needed

Linearity of expectation follows directly from the linearity of summation and integration. The proof uses only $E[X + Y] = E[X] + E[Y]$ and $E[cX] = c\,E[X]$, neither of which requires independence.

### Common Applications

- **Binomial mean:** $X = \sum_{i=1}^n \mathbf{1}_{A_i}$ with $\text{Bern}(p)$ indicators: $E[X] = np$
- **Hypergeometric mean:** Same indicator decomposition works even though indicators are dependent
- **Coupon collector:** $E[T] = n \sum_{k=1}^n 1/k = nH_n$, using dependent geometric waiting times

### Contrast with Variance

Variance is **not** linear in general:

$$
\text{Var}\!\left(\sum a_i X_i\right) = \sum a_i^2\,\text{Var}(X_i) + 2\sum_{i < j} a_i a_j\,\text{Cov}(X_i, X_j)
$$

The cross-terms vanish only when all pairs are uncorrelated.

## Examples

**Example.** Draw 5 cards from a standard deck without replacement. $X$ = number of aces. Write $X = \sum_{i=1}^5 \mathbf{1}_{i\text{-th card is ace}}$. The indicators are dependent (drawing without replacement), but:

$$
E[X] = 5 \cdot P(\text{card is ace}) = 5 \cdot \frac{4}{52} = \frac{5}{13}
$$

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

# Draw 5 cards without replacement; count aces
deck = list(range(52))  # 0-3 are aces
results = []
for _ in range(n_sim):
    hand = np.random.choice(deck, 5, replace=False)
    results.append(np.sum(hand < 4))

print(f"E[aces in 5 cards] = {np.mean(results):.4f}  (theory: {5*4/52:.4f})")
print(f"Linearity works despite dependence!")
```
