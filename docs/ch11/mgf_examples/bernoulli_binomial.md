# MGF of Bernoulli and Binomial

The binomial MGF factors as a product of Bernoulli MGFs — a direct consequence of the iid indicator representation.

## Definition

**Bernoulli:** $M_X(t) = q + pe^t$ where $q = 1 - p$.

**Binomial:** $M_X(t) = (q + pe^t)^n$.

Both exist for all $t \in \mathbb{R}$.

## Explanation

### Derivation

For $\text{Bern}(p)$: $M_X(t) = e^0 q + e^t p = q + pe^t$.

For $\text{Bin}(n, p) = \sum_{i=1}^n \text{Bern}(p)$: by independence, $M_X(t) = (q + pe^t)^n$.

### Moments

From the Bernoulli MGF: $M'(0) = p$, $M''(0) = p$, so $\text{Var}(X) = p - p^2 = pq$.

For the binomial: $E[X] = np$, $\text{Var}(X) = npq$.

### Sum Property

$(q + pe^t)^n \cdot (q + pe^t)^m = (q + pe^t)^{n+m}$, proving $\text{Bin}(n,p) + \text{Bin}(m,p) \sim \text{Bin}(n+m,p)$.

## Examples

**Example.** $X \sim \text{Bin}(20, 0.3)$: $E[X] = 6$, $\text{Var}(X) = 4.2$.

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
print(f"Var(X) = {M2 - M1**2:.4f}  (exact: {n*p*(1-p)})")
```
