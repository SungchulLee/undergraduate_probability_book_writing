# MGF Definition and Properties

The moment generating function encodes all moments of a distribution into a single function, enabling algebraic techniques for identifying distributions and proving limit theorems.

## Definition

The **moment generating function (MGF)** of $X$ is

$$
M_X(t) = E[e^{tX}]
$$

provided the expectation exists in a neighborhood of $t = 0$.

$$
M_X(t) = \begin{cases} \displaystyle\sum_x e^{tx}\,p(x) & \text{(discrete)} \\[10pt] \displaystyle\int_{-\infty}^{\infty} e^{tx}\,f(x)\,dx & \text{(continuous)} \end{cases}
$$

The $n$-th moment is recovered by: $E[X^n] = M_X^{(n)}(0)$.

## Explanation

### Why It Generates Moments

Expanding $e^{tX} = \sum_{n=0}^{\infty}(tX)^n/n!$ and taking expectations:

$$
M_X(t) = \sum_{n=0}^{\infty}\frac{E[X^n]}{n!}\,t^n
$$

Differentiating $n$ times and setting $t = 0$ picks out $E[X^n]$. In particular:

- $M_X'(0) = E[X]$
- $\text{Var}(X) = M_X''(0) - (M_X'(0))^2$

### Key Properties

| Property | Formula |
|:---------|:--------|
| Constant | $M_c(t) = e^{ct}$ |
| Scaling | $M_{aX+b}(t) = e^{bt}\,M_X(at)$ |
| Independence | $M_{X+Y}(t) = M_X(t)\,M_Y(t)$ |
| Uniqueness | $M_X = M_Y$ near 0 $\Rightarrow$ $X \stackrel{d}{=} Y$ |

### When the MGF Does Not Exist

Not every distribution has an MGF. The Cauchy and log-normal have $E[e^{tX}] = \infty$ for all $t \ne 0$. The characteristic function $\varphi_X(t) = E[e^{itX}]$ always exists as an alternative.

## Examples

**Example.** $X \sim \text{Exp}(1)$: $M_X(t) = 1/(1-t)$ for $t < 1$.

```python
import numpy as np
from scipy.misc import derivative

def mgf_exp(t, lam=1):
    return lam / (lam - t)

EX = derivative(mgf_exp, 0, n=1, dx=1e-6)
EX2 = derivative(mgf_exp, 0, n=2, dx=1e-6)
print(f"E[X] = M'(0) = {EX:.6f}  (exact: 1)")
print(f"E[X^2] = M''(0) = {EX2:.4f}  (exact: 2)")
print(f"Var(X) = {EX2 - EX**2:.4f}  (exact: 1)")
```
