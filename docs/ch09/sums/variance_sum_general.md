# Variance of a Sum (General Formula)

The variance of a sum includes cross-terms from every pair of variables — covariances that vanish only under uncorrelatedness.

## Definition

For any random variables $X_1, \ldots, X_n$:

$$
\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i) + 2\sum_{i < j}\text{Cov}(X_i, X_j)
$$

For a weighted sum $S = \sum a_i X_i$:

$$
\text{Var}(S) = \sum_{i=1}^n a_i^2\,\text{Var}(X_i) + 2\sum_{i < j}a_i a_j\,\text{Cov}(X_i, X_j)
$$

## Explanation

### Derivation

$$
\text{Var}\!\left(\sum X_i\right) = E\!\left[\left(\sum (X_i - \mu_i)\right)^2\right] = \sum_i \sum_j E[(X_i - \mu_i)(X_j - \mu_j)]
$$

The diagonal terms ($i = j$) give variances; the off-diagonal terms ($i \ne j$) give covariances. By symmetry, each pair appears twice.

### Counting the Terms

With $n$ variables there are $n$ variance terms and $\binom{n}{2}$ covariance terms. The total number of cross-terms grows as $O(n^2)$, so even small pairwise covariances can dominate the sum when $n$ is large.

### Special Cases

| Condition | Formula |
|:----------|:--------|
| General | $\sum \text{Var}(X_i) + 2\sum_{i<j}\text{Cov}(X_i, X_j)$ |
| Uncorrelated | $\sum \text{Var}(X_i)$ |
| Equal pairwise $\text{Cov} = c$ | $\sum \text{Var}(X_i) + n(n-1)c$ |
| iid | $n\,\text{Var}(X_1)$ |

### Application: Hypergeometric Variance

Drawing $n$ cards without replacement from $N$ cards containing $K$ aces: the indicator $\mathbf{1}_i$ are identically distributed but negatively correlated. The general formula gives:

$$
\text{Var}(X) = n \cdot \frac{K}{N}\cdot\frac{N-K}{N} + n(n-1)\cdot\left(-\frac{K(N-K)}{N^2(N-1)}\right) = n\frac{K}{N}\frac{N-K}{N}\frac{N-n}{N-1}
$$

The factor $(N-n)/(N-1)$ is the **finite population correction**.

## Examples

**Example.** $X_1, X_2, X_3$ with $\text{Var}(X_i) = 4$ and $\text{Cov}(X_i, X_j) = 1$ for $i \ne j$.

$$
\text{Var}(X_1 + X_2 + X_3) = 3(4) + 2 \cdot 3 \cdot 1 = 12 + 6 = 18
$$

Compare with independent case: $3(4) = 12$. Positive correlation inflates the variance.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

# Three correlated normals: Var=4, Cov=1
mu = [0, 0, 0]
Sigma = [[4, 1, 1], [1, 4, 1], [1, 1, 4]]
samples = np.random.multivariate_normal(mu, Sigma, n_sim)
S = samples.sum(axis=1)

print(f"Var(X1+X2+X3) = {S.var():.2f}  (theory: 18)")

# Hypergeometric: 5 cards from 52, count aces
deck = list(range(52))
counts = []
for _ in range(n_sim):
    hand = np.random.choice(deck, 5, replace=False)
    counts.append(np.sum(hand < 4))
counts = np.array(counts)

N, K, n = 52, 4, 5
var_theory = n * K/N * (N-K)/N * (N-n)/(N-1)
print(f"\nHypergeometric Var = {counts.var():.4f}  (theory: {var_theory:.4f})")
```
