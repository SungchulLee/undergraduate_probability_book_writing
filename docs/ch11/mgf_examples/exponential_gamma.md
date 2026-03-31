# MGF of Exponential and Gamma
<<<<<<< Updated upstream

## MGF of Exponential$(\lambda)$

If $X \sim \text{Exp}(\lambda)$ with PDF $f(x) = \lambda e^{-\lambda x}$ for $x \geq 0$, then:

$$M_X(t) = E[e^{tX}] = \int_0^{\infty} e^{tx} \lambda e^{-\lambda x}\,dx = \lambda \int_0^{\infty} e^{-(\lambda - t)x}\,dx$$

The integral converges when $\lambda - t > 0$, i.e., $t < \lambda$:

$$M_X(t) = \lambda \cdot \frac{1}{\lambda - t} = \frac{\lambda}{\lambda - t}$$

$$\boxed{M_{\text{Exp}(\lambda)}(t) = \frac{\lambda}{\lambda - t}, \quad t < \lambda}$$

### Deriving Moments

Write $M_X(t) = \lambda(\lambda - t)^{-1}$:

$$M_X'(t) = \lambda(\lambda - t)^{-2}$$

$$E[X] = M_X'(0) = \frac{\lambda}{\lambda^2} = \frac{1}{\lambda}$$

$$M_X''(t) = 2\lambda(\lambda - t)^{-3}$$

$$E[X^2] = M_X''(0) = \frac{2\lambda}{\lambda^3} = \frac{2}{\lambda^2}$$

$$\text{Var}(X) = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}$$

## MGF of Gamma$(\alpha, \lambda)$

If $X \sim \text{Gamma}(\alpha, \lambda)$ with PDF $f(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\lambda x}$ for $x > 0$, then:

$$M_X(t) = \int_0^{\infty} e^{tx} \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\lambda x}\,dx = \frac{\lambda^\alpha}{\Gamma(\alpha)} \int_0^{\infty} x^{\alpha - 1} e^{-(\lambda - t)x}\,dx$$

For $t < \lambda$, substitute $u = (\lambda - t)x$:

$$= \frac{\lambda^\alpha}{\Gamma(\alpha)} \cdot \frac{\Gamma(\alpha)}{(\lambda - t)^\alpha} = \left(\frac{\lambda}{\lambda - t}\right)^\alpha$$

$$\boxed{M_{\text{Gamma}(\alpha, \lambda)}(t) = \left(\frac{\lambda}{\lambda - t}\right)^\alpha, \quad t < \lambda}$$

!!! note "Exponential as a Special Case"
    Setting $\alpha = 1$ recovers $M_{\text{Exp}(\lambda)}(t) = \frac{\lambda}{\lambda - t}$, confirming that $\text{Exp}(\lambda) = \text{Gamma}(1, \lambda)$.

### Deriving Moments

$$M_X'(t) = \alpha \lambda^\alpha (\lambda - t)^{-\alpha - 1}$$

$$E[X] = M_X'(0) = \frac{\alpha}{\lambda}$$

$$M_X''(t) = \alpha(\alpha + 1)\lambda^\alpha (\lambda - t)^{-\alpha - 2}$$

$$E[X^2] = M_X''(0) = \frac{\alpha(\alpha + 1)}{\lambda^2}$$

$$\text{Var}(X) = \frac{\alpha(\alpha + 1)}{\lambda^2} - \frac{\alpha^2}{\lambda^2} = \frac{\alpha}{\lambda^2}$$

## Python Verification

```python
import numpy as np
from scipy.misc import derivative

def mgf_exp(t, lam=2.0):
    return lam / (lam - t)

def mgf_gamma(t, alpha=3.0, lam=2.0):
    return (lam / (lam - t))**alpha

# Exp(2): E[X] = 0.5, Var(X) = 0.25
EX = derivative(mgf_exp, 0, n=1, dx=1e-6)
EX2 = derivative(mgf_exp, 0, n=2, dx=1e-6)
print("Exp(2):")
print(f"  E[X]   = {EX:.4f}  (exact: 0.5)")
print(f"  Var(X) = {EX2 - EX**2:.4f}  (exact: 0.25)")

# Gamma(3, 2): E[X] = 1.5, Var(X) = 0.75
EX = derivative(mgf_gamma, 0, n=1, dx=1e-6)
EX2 = derivative(mgf_gamma, 0, n=2, dx=1e-6)
print("\nGamma(3, 2):")
print(f"  E[X]   = {EX:.4f}  (exact: 1.5)")
print(f"  Var(X) = {EX2 - EX**2:.4f}  (exact: 0.75)")
```
=======
>>>>>>> Stashed changes
