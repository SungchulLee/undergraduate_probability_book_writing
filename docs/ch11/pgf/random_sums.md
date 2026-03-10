# Random Sums and Compound Distributions

The PGF of a random sum $S = \sum_{i=1}^N X_i$ is a composition $G_N(G_X(s))$ — a key tool for insurance and queuing models.

## Definition

Let $N$ be a non-negative integer RV and $X_1, X_2, \ldots$ be iid non-negative integer RVs independent of $N$. The **compound** (random) sum is

$$
S = \sum_{i=1}^N X_i
$$

Its PGF is the **composition**:

$$
G_S(s) = G_N(G_X(s))
$$

## Explanation

### Proof

Conditioning on $N$:

$$
G_S(s) = E[s^S] = E\bigl[E[s^{X_1+\cdots+X_N} \mid N]\bigr] = E\bigl[(G_X(s))^N\bigr] = G_N(G_X(s))
$$

### Moments of the Random Sum

$$
E[S] = E[N]\,E[X]
$$

$$
\text{Var}(S) = E[N]\,\text{Var}(X) + (E[X])^2\,\text{Var}(N)
$$

These follow from the tower property and Eve's law (or by differentiating the compound PGF).

### Compound Poisson

If $N \sim \text{Pois}(\lambda)$ and $X_i$ are iid:

$$
G_S(s) = e^{\lambda(G_X(s) - 1)}
$$

This is the **compound Poisson** distribution, fundamental in insurance mathematics for modeling aggregate claims.

## Examples

**Example.** $N \sim \text{Pois}(10)$ claims per day, each claim $X_i \sim \text{Geo}(0.5)$. Total payout $S = \sum_{i=1}^N X_i$.

$$
E[S] = 10 \cdot 2 = 20, \qquad \text{Var}(S) = 10 \cdot 2 + 4 \cdot 10 = 60
$$

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

lam = 10
p = 0.5

results = []
for _ in range(n_sim):
    N = np.random.poisson(lam)
    if N > 0:
        claims = np.random.geometric(p, N)
        results.append(claims.sum())
    else:
        results.append(0)

S = np.array(results)
EX = 1/p
VarX = (1-p)/p**2

print(f"E[S] = {S.mean():.2f}  (theory: {lam * EX:.1f})")
print(f"Var(S) = {S.var():.1f}  (theory: {lam*VarX + EX**2*lam:.1f})")
```
