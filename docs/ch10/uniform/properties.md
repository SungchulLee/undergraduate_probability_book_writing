# Discrete Uniform Properties

Sums of discrete uniforms produce familiar distributions — two dice give the triangular distribution, and many dice converge to the normal.

## Definition

If $X_1, X_2 \stackrel{\text{iid}}{\sim} \text{DUnif}(1, \ldots, n)$, then $S = X_1 + X_2$ has the **triangular PMF** on $\{2, 3, \ldots, 2n\}$:

$$
P(S = s) = \frac{n - |s - (n+1)|}{n^2}
$$

The sum of $m$ independent $\text{DUnif}(1, \ldots, n)$ has mean $m(n+1)/2$ and variance $m(n^2-1)/12$.

## Explanation

### Sum of Two Dice

For $n = 6$: the sum $S = X_1 + X_2$ ranges from 2 to 12. The mode is $s = 7$ with $P(S = 7) = 6/36 = 1/6$. The PMF rises linearly from $s = 2$ to $s = 7$, then falls symmetrically.

### CLT for Dice Sums

By the CLT, the sum of $m$ dice is approximately $N(m(n+1)/2, m(n^2-1)/12)$ for large $m$. Even for $m = 12$ fair dice, the normal approximation is excellent.

### Special Cases

| Distribution | $n$ | $E[X]$ | $\text{Var}(X)$ |
|:-------------|:----|:-------|:----------------|
| Fair coin (0/1) | 2 | 0.5 | 0.25 |
| Fair die | 6 | 3.5 | 35/12 |
| DUnif(1,...,10) | 10 | 5.5 | 99/12 |
| DUnif(1,...,100) | 100 | 50.5 | 9999/12 |

## Examples

**Example.** Sum of two fair dice.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

X1 = np.random.randint(1, 7, n_sim)
X2 = np.random.randint(1, 7, n_sim)
S = X1 + X2

# PMF of sum
print("s   Simulated  Theory")
for s in range(2, 13):
    sim = np.mean(S == s)
    theory = (6 - abs(s - 7)) / 36
    print(f"{s:2d}  {sim:.4f}     {theory:.4f}")

print(f"\nE[S] = {S.mean():.3f}  (theory: 7.0)")
print(f"Var(S) = {S.var():.3f}  (theory: {35/6:.4f})")
```
