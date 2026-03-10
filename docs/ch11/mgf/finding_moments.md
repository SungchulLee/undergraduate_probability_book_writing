# Finding Moments from the MGF

Differentiating the MGF at zero extracts moments one by one — often easier than computing $E[X^n]$ directly from the definition.

## Definition

If $M_X(t)$ exists in a neighborhood of $t = 0$:

$$
E[X^n] = M_X^{(n)}(0)
$$

The **variance shortcut:**

$$
\text{Var}(X) = M_X''(0) - \bigl(M_X'(0)\bigr)^2
$$

## Explanation

### Practical Technique

1. Write down $M_X(t)$
2. Differentiate: $M_X'(0) = E[X]$, $M_X''(0) = E[X^2]$
3. Compute $\text{Var}(X) = E[X^2] - (E[X])^2$

### Cumulant Generating Function

The **cumulant generating function** $K_X(t) = \ln M_X(t)$ simplifies variance calculations:

$$
K_X'(0) = E[X], \qquad K_X''(0) = \text{Var}(X)
$$

For the Poisson: $K_X(t) = \lambda(e^t - 1)$, so $K_X'(0) = \lambda$ and $K_X''(0) = \lambda$.

### Taylor Expansion Method

Sometimes it is easier to expand $M_X(t)$ as a power series and read off $E[X^n]/n!$ as the coefficient of $t^n$.

## Examples

**Example.** $X \sim \text{Bin}(n, p)$: $M_X(t) = (q + pe^t)^n$.

$$
M_X'(t) = n(q + pe^t)^{n-1}\,pe^t \implies E[X] = np
$$

$$
E[X^2] = M_X''(0) = n(n-1)p^2 + np \implies \text{Var}(X) = npq
$$

```python
import numpy as np

def mgf_binom(t, n, p):
    return ((1 - p) + p * np.exp(t))**n

n, p = 20, 0.3
dt = 1e-6
M0 = mgf_binom(0, n, p)
M1 = (mgf_binom(dt, n, p) - mgf_binom(-dt, n, p)) / (2 * dt)
M2 = (mgf_binom(dt, n, p) - 2*M0 + mgf_binom(-dt, n, p)) / dt**2

print(f"E[X] = {M1:.4f}  (exact: {n*p})")
print(f"Var(X) = {M2 - M1**2:.4f}  (exact: {n*p*(1-p):.1f})")
```
