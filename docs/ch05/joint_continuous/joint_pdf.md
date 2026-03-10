# Joint PDF

The joint PDF describes how probability density is spread across $\mathbb{R}^2$ for a pair of continuous random variables — probability is obtained by integrating density over a region.

## Definition

For continuous random variables $(X, Y)$, the **joint PDF** is a function $f_{X,Y}(x, y) \ge 0$ satisfying

$$
P((X, Y) \in A) = \iint_A f_{X,Y}(x, y)\,dx\,dy
$$

A valid joint PDF satisfies:

1. **Non-negativity:** $f_{X,Y}(x, y) \ge 0$ for all $(x, y)$
2. **Normalization:** $\displaystyle\int_{-\infty}^{\infty}\!\int_{-\infty}^{\infty} f_{X,Y}(x, y)\,dx\,dy = 1$

## Explanation

### Probability as Volume

For a rectangular region:

$$
P(a \le X \le b,\; c \le Y \le d) = \int_a^b\!\int_c^d f_{X,Y}(x, y)\,dy\,dx
$$

This is the **volume** under the surface $z = f(x, y)$ above the rectangle $[a,b] \times [c,d]$. The total volume under the entire surface is 1.

### Density, Not Probability

Just as in one dimension, $f_{X,Y}(x, y)$ is a density and can exceed 1. The infinitesimal interpretation:

$$
P(x \le X \le x + dx,\; y \le Y \le y + dy) \approx f_{X,Y}(x, y)\,dx\,dy
$$

### Marginal PDFs

$$
f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y)\,dy, \qquad f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y)\,dx
$$

Integrate out the other variable to get the marginal density.

## Examples

**Example 1.** $(X, Y) \sim \text{Uniform}([0,1]^2)$: $f(x,y) = 1$ on the unit square.

$$
P(X \le 1/2,\; Y \le 1/2) = \int_0^{1/2}\!\int_0^{1/2} 1\,dy\,dx = 1/4
$$

**Example 2.** $f(x, y) = 6(1-y)$ for $0 \le x \le y \le 1$, zero otherwise.

Normalization check:

$$
\int_0^1\!\int_0^y 6(1-y)\,dx\,dy = \int_0^1 6y(1-y)\,dy = 6\left[\frac{1}{2} - \frac{1}{3}\right] = 1
$$

$$
P(X \le 1/4, Y \le 1/2) = \int_0^{1/2}\!\int_0^{\min(y, 1/4)} 6(1-y)\,dx\,dy
$$

```python
from scipy import integrate

# Example 2: f(x,y) = 6(1-y) for 0 <= x <= y <= 1
f = lambda y, x: 6 * (1 - y) if 0 <= x <= y <= 1 else 0

# Normalization
norm, _ = integrate.dblquad(lambda y, x: 6*(1-y), 0, 1, lambda x: x, 1)
print(f"Normalization: {norm:.6f}")

# P(X <= 1/4, Y <= 1/2)
prob, _ = integrate.dblquad(
    lambda y, x: 6*(1-y),
    0, 0.25,           # x from 0 to 1/4
    lambda x: x, 0.5   # y from x to 1/2
)
print(f"P(X <= 1/4, Y <= 1/2) = {prob:.6f}")

# Marginal of X: f_X(x) = integral from x to 1 of 6(1-y) dy
# = 6[(1-y) - (1-y)^2/2] evaluated = 3(1-x)^2
import numpy as np
x_vals = np.linspace(0, 1, 5)
for x in x_vals:
    fx = 3 * (1 - x)**2
    print(f"f_X({x:.2f}) = {fx:.4f}")
```
