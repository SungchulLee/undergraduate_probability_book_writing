# PGF Definition and Properties
<<<<<<< Updated upstream

## Definition

The **probability generating function (PGF)** of a non-negative integer-valued random variable $X$ is:

$$G_X(s) = E[s^X] = \sum_{k=0}^{\infty} P(X = k)\,s^k$$

The series converges absolutely for $|s| \leq 1$, since $|s^k P(X=k)| \leq P(X=k)$ and $\sum P(X=k) = 1$.

!!! note "Why PGFs?"
    The PGF is a power series whose coefficients are the probabilities $P(X = k)$. It encodes the entire distribution of $X$ in a single function, and is particularly convenient for non-negative integer-valued random variables (counts).

## Key Properties

!!! info "Properties of the PGF"
    For a non-negative integer-valued random variable $X$:

    1. $G_X(0) = P(X = 0)$
    2. $G_X(1) = 1$
    3. $G_X'(1) = E[X]$
    4. $G_X''(1) = E[X(X-1)]$ (the second factorial moment)
    5. $\text{Var}(X) = G_X''(1) + G_X'(1) - [G_X'(1)]^2$

**Proof of (3).** Differentiating the power series:

$$G_X'(s) = \sum_{k=1}^{\infty} k\,P(X = k)\,s^{k-1}$$

$$G_X'(1) = \sum_{k=1}^{\infty} k\,P(X = k) = E[X]$$

**Proof of (4).** Differentiating again:

$$G_X''(s) = \sum_{k=2}^{\infty} k(k-1)\,P(X = k)\,s^{k-2}$$

$$G_X''(1) = \sum_{k=2}^{\infty} k(k-1)\,P(X = k) = E[X(X-1)]$$

**Deriving the variance.** Since $E[X(X-1)] = E[X^2] - E[X]$:

$$E[X^2] = G_X''(1) + G_X'(1)$$

$$\text{Var}(X) = E[X^2] - (E[X])^2 = G_X''(1) + G_X'(1) - [G_X'(1)]^2$$

## Recovering Probabilities

The PMF can be recovered from the PGF by differentiation at $s = 0$:

$$P(X = k) = \frac{G_X^{(k)}(0)}{k!}$$

This follows because $G_X(s) = \sum P(X=k)\,s^k$ is a Taylor series centered at $0$.

## Relationship to the MGF

The PGF and MGF are related by the substitution $s = e^t$:

$$M_X(t) = E[e^{tX}] = E[(e^t)^X] = G_X(e^t)$$

Equivalently, $G_X(s) = M_X(\ln s)$ for $s > 0$.

## Product Rule for Independent Sums

If $X$ and $Y$ are independent non-negative integer-valued random variables:

$$G_{X+Y}(s) = G_X(s) \cdot G_Y(s)$$

The proof is identical to the MGF case: $E[s^{X+Y}] = E[s^X s^Y] = E[s^X]\,E[s^Y]$ by independence.

## Python Verification

```python
import numpy as np
from scipy.misc import derivative

def pgf_poisson(s, lam=3.0):
    """PGF of Po(lambda): G(s) = exp(lambda(s - 1))"""
    return np.exp(lam * (s - 1))

lam = 3.0

# P(X = 0) = G(0)
print(f"Po({lam}):")
print(f"  P(X=0) = G(0) = {pgf_poisson(0, lam):.6f}  (exact: {np.exp(-lam):.6f})")
print(f"  G(1)   = {pgf_poisson(1, lam):.6f}  (exact: 1)")

# E[X] = G'(1)
EX = derivative(pgf_poisson, 1, n=1, dx=1e-6)
print(f"  E[X]   = G'(1) = {EX:.4f}  (exact: {lam})")

# E[X(X-1)] = G''(1)
EXX1 = derivative(pgf_poisson, 1, n=2, dx=1e-6)
VarX = EXX1 + EX - EX**2
print(f"  Var(X) = {VarX:.4f}  (exact: {lam})")
```
=======
>>>>>>> Stashed changes
