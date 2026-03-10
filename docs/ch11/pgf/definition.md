# PGF Definition and Properties

The probability generating function is tailored to non-negative integer-valued random variables, encoding the PMF as coefficients of a power series.

## Definition

For a non-negative integer-valued random variable $X$, the **probability generating function (PGF)** is

$$
G_X(s) = E[s^X] = \sum_{k=0}^{\infty}P(X = k)\,s^k
$$

for $|s| \le 1$. The PGF always converges on $[-1, 1]$.

**Recovering the PMF:** $P(X = k) = G_X^{(k)}(0)/k!$.

**Moments:**

$$
E[X] = G_X'(1), \qquad E[X(X-1)] = G_X''(1)
$$

$$
\text{Var}(X) = G_X''(1) + G_X'(1) - (G_X'(1))^2
$$

## Explanation

### Relationship to MGF

$G_X(s) = E[s^X] = E[e^{X\ln s}] = M_X(\ln s)$. Conversely, $M_X(t) = G_X(e^t)$.

### Key Properties

| Property | Formula |
|:---------|:--------|
| Normalization | $G_X(1) = 1$ |
| PMF recovery | $P(X = k) = G_X^{(k)}(0)/k!$ |
| Independence | $G_{X+Y}(s) = G_X(s)\,G_Y(s)$ |
| Uniqueness | $G_X = G_Y \Leftrightarrow X \stackrel{d}{=} Y$ |

### Factorial Moments

The $n$-th factorial moment $E[X(X-1)\cdots(X-n+1)] = G_X^{(n)}(1)$. These are often easier to compute than raw moments.

## Examples

**Example.** $X \sim \text{Bern}(p)$: $G_X(s) = q + ps$.

$G_X'(s) = p$, so $E[X] = G_X'(1) = p$. $G_X''(s) = 0$, so $\text{Var}(X) = 0 + p - p^2 = pq$.

```python
import numpy as np

# PGF of Poisson: G(s) = exp(lambda(s-1))
lam = 3.0
G = lambda s: np.exp(lam * (s - 1))

# Recover PMF: P(X=k) = G^(k)(0)/k!
from scipy.misc import derivative
from math import factorial

print("k  PGF method  Direct")
for k in range(8):
    pgf_val = derivative(G, 0, n=k, dx=1e-4) / factorial(k)
    direct = np.exp(-lam) * lam**k / factorial(k)
    print(f"{k}  {pgf_val:.6f}    {direct:.6f}")
```
