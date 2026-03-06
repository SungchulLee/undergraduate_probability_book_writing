# MGF of Poisson

## MGF of Po(lambda)

If $X \sim \text{Po}(\lambda)$, then:

$$M_X(t) = E[e^{tX}] = \sum_{k=0}^{\infty} e^{tk} \frac{\lambda^k}{k!} e^{-\lambda}$$

$$= e^{-\lambda} \sum_{k=0}^{\infty} \frac{(\lambda e^t)^k}{k!} = e^{-\lambda} \cdot e^{\lambda e^t} = e^{\lambda(e^t - 1)}$$

$$\boxed{M_{\text{Po}(\lambda)}(t) = e^{\lambda(e^t - 1)}}$$

## Deriving Moments

$$M'(t) = \lambda e^t \cdot e^{\lambda(e^t - 1)}$$

$$E[X] = M'(0) = \lambda \cdot 1 = \lambda$$

$$M''(t) = (\lambda e^t)^2 e^{\lambda(e^t - 1)} + \lambda e^t \cdot e^{\lambda(e^t - 1)}$$

$$E[X^2] = M''(0) = \lambda^2 + \lambda$$

$$\text{Var}(X) = \lambda^2 + \lambda - \lambda^2 = \lambda$$

This confirms $E[X] = \text{Var}(X) = \lambda$ for the Poisson distribution.

## Connection to Poisson Approximation

The MGF provides an elegant proof of the Poisson limit theorem. For $X \sim B(n, p)$ with $np = \lambda$:

$$M_{B(n,p)}(t) = \left[1 + p(e^t - 1)\right]^n = \left[1 + \frac{\lambda}{n}(e^t - 1)\right]^n$$

As $n \to \infty$:

$$\left[1 + \frac{\lambda(e^t - 1)}{n}\right]^n \to e^{\lambda(e^t - 1)} = M_{\text{Po}(\lambda)}(t)$$

Since the MGFs converge, $B(n, p) \xrightarrow{d} \text{Po}(\lambda)$ when $n \to \infty$, $p \to 0$, $np = \lambda$.

## Python Verification

```python
import numpy as np

def mgf_poisson(t, lam):
    return np.exp(lam * (np.exp(t) - 1))

lam = 5.0
dt = 1e-6

M0 = mgf_poisson(0, lam)
M1 = (mgf_poisson(dt, lam) - mgf_poisson(-dt, lam)) / (2 * dt)
M2 = (mgf_poisson(dt, lam) - 2*M0 + mgf_poisson(-dt, lam)) / dt**2

print(f"Po({lam}):")
print(f"  E[X]   = {M1:.4f}  (exact: {lam})")
print(f"  Var(X) = {M2 - M1**2:.4f}  (exact: {lam})")
```
