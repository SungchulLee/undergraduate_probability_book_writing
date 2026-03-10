# MGF of Bernoulli and Binomial


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## MGF of Bernoulli(p)

If $X \sim \text{Bernoulli}(p)$, then:

$$M_X(t) = E[e^{tX}] = e^{t \cdot 1} \cdot p + e^{t \cdot 0} \cdot (1 - p) = 1 + p(e^t - 1)$$

$$\boxed{M_{\text{Bernoulli}(p)}(t) = 1 + p(e^t - 1)}$$

## MGF of Binomial(n, p)

If $X \sim B(n, p)$, then $X = \sum_{k=1}^n X_k$ where $X_k \sim \text{Bernoulli}(p)$ are iid. By independence:

$$M_X(t) = \prod_{k=1}^n M_{X_k}(t) = \prod_{k=1}^n \left[1 + p(e^t - 1)\right] = \left[1 + p(e^t - 1)\right]^n$$

$$\boxed{M_{B(n,p)}(t) = \left[1 + p(e^t - 1)\right]^n}$$

## Deriving Moments

From the Bernoulli MGF $M(t) = 1 + p(e^t - 1)$:

$$M'(t) = pe^t \implies E[X] = M'(0) = p$$

$$M''(t) = pe^t \implies E[X^2] = M''(0) = p$$

$$\text{Var}(X) = E[X^2] - (E[X])^2 = p - p^2 = p(1 - p)$$

From the Binomial MGF $M(t) = [1 + p(e^t - 1)]^n$:

$$M'(t) = n[1 + p(e^t - 1)]^{n-1} \cdot pe^t$$

$$E[X] = M'(0) = n \cdot 1 \cdot p = np$$

After computing $M''(0)$:

$$\text{Var}(X) = np(1 - p)$$

## Python Verification

```python
import numpy as np

def mgf_binomial(t, n, p):
    return (1 + p * (np.exp(t) - 1))**n

# Binomial(20, 0.3): E[X] = 6, Var(X) = 4.2
n, p = 20, 0.3
dt = 1e-6

M0 = mgf_binomial(0, n, p)
M1 = (mgf_binomial(dt, n, p) - mgf_binomial(-dt, n, p)) / (2 * dt)
M2 = (mgf_binomial(dt, n, p) - 2*M0 + mgf_binomial(-dt, n, p)) / dt**2

print(f"B({n}, {p}):")
print(f"  E[X]   = {M1:.4f}  (exact: {n*p})")
print(f"  Var(X) = {M2 - M1**2:.4f}  (exact: {n*p*(1-p)})")
```
