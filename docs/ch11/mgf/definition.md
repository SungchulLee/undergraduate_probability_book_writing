# MGF Definition and Properties


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

The **moment generating function (MGF)** of a random variable $X$ is:

$$M_X(t) = E[e^{tX}]$$

provided the expectation exists in a neighborhood of $t = 0$.

For discrete and continuous cases:

$$M_X(t) = \begin{cases} \displaystyle\sum_x e^{tx} \, p(x) & \text{if } X \text{ is discrete} \\[10pt] \displaystyle\int_{-\infty}^{\infty} e^{tx} f(x)\,dx & \text{if } X \text{ is continuous} \end{cases}$$

## Why "Moment Generating"?

The MGF generates all moments of $X$ via differentiation at $t = 0$:

$$M_X^{(n)}(0) = E[X^n]$$

**Derivation:**

$$M_X(t) = E[e^{tX}] \implies M_X'(t) = E[Xe^{tX}] \implies M_X'(0) = E[X]$$

$$M_X''(t) = E[X^2 e^{tX}] \implies M_X''(0) = E[X^2]$$

$$\vdots$$

$$M_X^{(n)}(t) = E[X^n e^{tX}] \implies M_X^{(n)}(0) = E[X^n]$$

In particular:

- $E[X] = M_X'(0)$
- $\text{Var}(X) = M_X''(0) - [M_X'(0)]^2$

## Why MGFs Are Useful

!!! info "Two Key Properties"
    1. **Uniqueness:** If $M_X(t) = M_Y(t)$ for all $t$ in a neighborhood of $0$, then $X$ and $Y$ have the **same distribution**.

    2. **Convergence:** If $M_{X_n}(t) \to M_Y(t)$ for all $t$ in a neighborhood of $0$, then $X_n \xrightarrow{d} Y$ (convergence in distribution).

Property (1) allows us to **identify** distributions by matching MGFs. Property (2) is the key tool in the **proof of the CLT**.

## Python Implementation

```python
import numpy as np
from scipy.misc import derivative

# Numerically verify MGF properties for X ~ Exp(1)
# M_X(t) = 1/(1-t) for t < 1
def mgf_exp(t, lam=1):
    """MGF of Exp(lambda): lambda/(lambda - t)"""
    return lam / (lam - t)

# First moment: E[X] = M'(0)
EX = derivative(mgf_exp, 0, n=1, dx=1e-6)
print(f"E[X] = M'(0) = {EX:.6f}  (exact: 1.0)")

# Second moment: E[X^2] = M''(0)
EX2 = derivative(mgf_exp, 0, n=2, dx=1e-6)
print(f"E[X²] = M''(0) = {EX2:.4f}  (exact: 2.0)")

# Variance
VarX = EX2 - EX**2
print(f"Var(X) = {VarX:.4f}  (exact: 1.0)")
```

**Output:**
```
E[X] = M'(0) = 1.000000  (exact: 1.0)
E[X²] = M''(0) = 2.0000  (exact: 2.0)
Var(X) = 1.0000  (exact: 1.0)
```
