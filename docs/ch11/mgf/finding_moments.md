# Finding Moments from the MGF

## Derivative Method

The $n$-th derivative of the MGF evaluated at $t = 0$ gives the $n$-th moment:

$$M_X^{(n)}(0) = E[X^n]$$

The first few derivatives yield the most commonly needed quantities:

- **First moment:** $E[X] = M_X'(0)$
- **Second moment:** $E[X^2] = M_X''(0)$
- **Variance:** $\text{Var}(X) = M_X''(0) - [M_X'(0)]^2$

## Taylor Expansion Approach

Since $e^{tX} = \sum_{n=0}^{\infty} \frac{(tX)^n}{n!}$, taking expectations term by term gives:

$$M_X(t) = E[e^{tX}] = \sum_{n=0}^{\infty} \frac{E[X^n]}{n!}\,t^n$$

This is a power series whose coefficients encode every moment of $X$. To extract the $n$-th moment, read off the coefficient of $t^n$ and multiply by $n!$:

$$E[X^n] = n! \cdot [\text{coefficient of } t^n \text{ in } M_X(t)]$$

!!! tip "When to Use Each Method"
    - **Derivative method:** best when the MGF has a simple closed form that is easy to differentiate (e.g., exponential, Poisson).
    - **Taylor expansion:** best when the MGF is already expressed as a power series or is easy to expand (e.g., $e^{\lambda(e^t - 1)}$).

## Worked Example

???+ example "Extracting moments from $M_X(t) = e^{3t + 2t^2}$"
    **Derivative method.** Write $M_X(t) = e^{3t + 2t^2}$ and let $g(t) = 3t + 2t^2$.

    $$M_X'(t) = g'(t)\,M_X(t) = (3 + 4t)\,e^{3t + 2t^2}$$

    $$E[X] = M_X'(0) = 3 \cdot 1 = 3$$

    For the second derivative, use the product rule:

    $$M_X''(t) = g''(t)\,M_X(t) + [g'(t)]^2\,M_X(t) = [4 + (3+4t)^2]\,e^{3t + 2t^2}$$

    $$E[X^2] = M_X''(0) = 4 + 9 = 13$$

    $$\text{Var}(X) = 13 - 3^2 = 4$$

    **Taylor expansion method.** Expand $e^{3t + 2t^2} = e^{3t} \cdot e^{2t^2}$:

    $$e^{3t} = 1 + 3t + \frac{9t^2}{2} + \cdots, \qquad e^{2t^2} = 1 + 2t^2 + \cdots$$

    $$M_X(t) = 1 + 3t + \left(\frac{9}{2} + 2\right)t^2 + \cdots = 1 + 3t + \frac{13}{2}\,t^2 + \cdots$$

    Reading off coefficients: $E[X] = 1! \cdot 3 = 3$ and $E[X^2] = 2! \cdot \frac{13}{2} = 13$.

## Recognizing the Normal MGF

The MGF $M_X(t) = e^{3t + 2t^2}$ matches the normal form $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$ with $\mu = 3$ and $\sigma^2 = 4$. So $X \sim N(3, 4)$, which is consistent with $E[X] = 3$ and $\text{Var}(X) = 4$.

## Python Verification

```python
import numpy as np
from scipy.misc import derivative

def mgf(t):
    """M_X(t) = exp(3t + 2t^2)"""
    return np.exp(3 * t + 2 * t**2)

# Extract moments via numerical differentiation
EX = derivative(mgf, 0, n=1, dx=1e-6)
EX2 = derivative(mgf, 0, n=2, dx=1e-6)
VarX = EX2 - EX**2

print("M_X(t) = exp(3t + 2t^2)")
print(f"  E[X]   = {EX:.4f}   (exact: 3)")
print(f"  E[X^2] = {EX2:.4f}  (exact: 13)")
print(f"  Var(X) = {VarX:.4f}   (exact: 4)")
```
