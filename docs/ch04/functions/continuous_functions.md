# Functions of Continuous Random Variables

For continuous random variables, finding the distribution of $Y = g(X)$ requires the CDF method or, when $g$ is monotone, the change-of-variables formula.

## Definition

**CDF method** (always works): For $Y = g(X)$,

$$
F_Y(y) = P(g(X) \le y)
$$

Express the right side in terms of $F_X$, then differentiate to get $f_Y(y) = F_Y'(y)$.

**Change-of-variables formula** (monotone $g$): If $g$ is strictly monotone and differentiable with inverse $h = g^{-1}$, then

$$
f_Y(y) = f_X(h(y)) \cdot |h'(y)|
$$

## Explanation

### CDF Method Steps

1. Write $F_Y(y) = P(g(X) \le y)$
2. Solve the inequality $g(X) \le y$ for $X$ (e.g., $X \le g^{-1}(y)$ if $g$ is increasing)
3. Express using $F_X$
4. Differentiate: $f_Y(y) = F_Y'(y)$

### Why the Absolute Value

For a strictly increasing $g$: $P(g(X) \le y) = P(X \le g^{-1}(y))$, so $F_Y(y) = F_X(h(y))$ and $f_Y(y) = f_X(h(y)) \cdot h'(y)$ with $h' > 0$.

For a strictly decreasing $g$: $P(g(X) \le y) = P(X \ge g^{-1}(y)) = 1 - F_X(h(y))$, giving $f_Y(y) = -f_X(h(y)) \cdot h'(y)$ with $h' < 0$. The absolute value $|h'(y)|$ unifies both cases.

### Non-Monotone Functions

When $g$ is not monotone, partition the domain into intervals $A_1, \ldots, A_k$ where $g$ is monotone with local inverses $h_1, \ldots, h_k$:

$$
f_Y(y) = \sum_{i=1}^{k} f_X(h_i(y)) \cdot |h_i'(y)|
$$

### Key Results

| Transformation | Result |
|:---------------|:-------|
| $Y = aX + b$, $a \ne 0$ | $f_Y(y) = \frac{1}{|a|} f_X\!\left(\frac{y-b}{a}\right)$ |
| $X \sim N(\mu, \sigma^2)$, $Y = aX+b$ | $Y \sim N(a\mu+b, a^2\sigma^2)$ |
| $X \sim U(0,1)$, $Y = -\ln X$ | $Y \sim \text{Exp}(1)$ |
| $X \sim N(0,1)$, $Y = X^2$ | $Y \sim \chi^2(1)$ |

## Examples

**Example 1.** $X \sim \text{Uniform}(0,1)$, $Y = -\ln X$.

Since $g(x) = -\ln x$ is strictly decreasing on $(0,1)$ with inverse $h(y) = e^{-y}$ and $|h'(y)| = e^{-y}$:

$$
f_Y(y) = f_X(e^{-y}) \cdot e^{-y} = 1 \cdot e^{-y} = e^{-y}, \quad y > 0
$$

This is $\text{Exp}(1)$ — the basis of the inverse CDF method for simulation.

**Example 2.** $X \sim N(0,1)$, $Y = X^2$.

For $y > 0$: $F_Y(y) = P(X^2 \le y) = P(-\sqrt{y} \le X \le \sqrt{y}) = 2\Phi(\sqrt{y}) - 1$.

Differentiating:

$$
f_Y(y) = 2\varphi(\sqrt{y}) \cdot \frac{1}{2\sqrt{y}} = \frac{1}{\sqrt{2\pi y}}\,e^{-y/2}, \quad y > 0
$$

This is $\chi^2(1) = \text{Gamma}(1/2, 1/2)$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n = 200000

# Example 1: Y = -ln(X), X ~ U(0,1) -> Exp(1)
X1 = np.random.uniform(0, 1, n)
Y1 = -np.log(X1)
y_grid = np.linspace(0.01, 6, 300)
print("Y = -ln(X), X ~ U(0,1):")
print(f"  E[Y] = {Y1.mean():.4f} (theory: 1.0)")
print(f"  Var(Y) = {Y1.var():.4f} (theory: 1.0)")

# Example 2: Y = X^2, X ~ N(0,1) -> chi2(1)
X2 = np.random.normal(0, 1, n)
Y2 = X2**2
print(f"\nY = X^2, X ~ N(0,1):")
print(f"  E[Y] = {Y2.mean():.4f} (theory: 1.0)")
print(f"  Var(Y) = {Y2.var():.4f} (theory: 2.0)")

# Verify change of variables: linear Y = 3X + 2, X ~ N(0,1)
X3 = np.random.normal(0, 1, n)
Y3 = 3 * X3 + 2
print(f"\nY = 3X + 2, X ~ N(0,1):")
print(f"  E[Y] = {Y3.mean():.4f} (theory: 2.0)")
print(f"  Var(Y) = {Y3.var():.4f} (theory: 9.0)")
```
