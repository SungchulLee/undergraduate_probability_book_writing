# PDF-CDF Relationship

Integration converts the PDF to the CDF; differentiation converts the CDF back to the PDF. This duality is the Fundamental Theorem of Calculus applied to probability.

## Definition

**From PDF to CDF** (integration):

$$
F_X(x) = \int_{-\infty}^{x} f_X(t)\,dt
$$

**From CDF to PDF** (differentiation, wherever $F_X$ is differentiable):

$$
f_X(x) = \frac{d}{dx} F_X(x) = F_X'(x)
$$

## Explanation

### Unified View

| | Discrete | Continuous |
|:--|:---------|:-----------|
| Distribution | PMF: $p_X(x_i)$ | PDF: $f_X(x)$ |
| CDF formula | $F(x) = \sum_{x_i \le x} p_X(x_i)$ | $F(x) = \int_{-\infty}^{x} f_X(t)\,dt$ |
| Recover distribution | $p_X(x_i) = F(x_i) - F(x_i^-)$ | $f_X(x) = F'(x)$ |
| $P(X \in A)$ | $\sum_{x_i \in A} p_X(x_i)$ | $\int_A f_X(x)\,dx$ |

The pattern: summation and differences for discrete; integration and differentiation for continuous.

### Geometric Interpretation

- **CDF from PDF:** $F(x)$ is the area under $f$ from $-\infty$ to $x$. As $x$ increases, more area accumulates.
- **PDF from CDF:** $f(x)$ is the slope of $F$ at $x$. Where $F$ is steep, the density is high; where $F$ is flat, the density is zero.

### Checking Consistency

Given a candidate PDF-CDF pair, verify:

1. $F(-\infty) = 0$ and $F(+\infty) = 1$
2. $F$ is non-decreasing and continuous
3. $F'(x) = f(x)$ wherever $f$ is continuous

## Examples

**Example 1.** Let $f(x) = 2x$ for $0 \le x \le 1$.

$$
F(x) = \int_0^x 2t\,dt = t^2\big|_0^x = x^2, \quad 0 \le x \le 1
$$

Full CDF: $F(x) = 0$ for $x < 0$, $F(x) = x^2$ for $0 \le x \le 1$, $F(x) = 1$ for $x > 1$.

Check: $F'(x) = 2x = f(x)$ on $(0,1)$. $F(0) = 0$, $F(1) = 1$.

**Example 2.** Given CDF $F(x) = 1 - e^{-3x}$ for $x \ge 0$, find the PDF.

$$
f(x) = F'(x) = 3e^{-3x}, \quad x \ge 0
$$

This is $\text{Exp}(3)$. Verify: $\int_0^{\infty} 3e^{-3x}\,dx = 1$.

```python
import numpy as np
from scipy import integrate

# Example 1: f(x) = 2x, F(x) = x^2
f = lambda x: 2 * x
F = lambda x: x**2

# Verify F via numerical integration
for x_val in [0.25, 0.5, 0.75, 1.0]:
    F_num, _ = integrate.quad(f, 0, x_val)
    print(f"x={x_val}: F(x) = {F(x_val):.4f}, integral = {F_num:.4f}")

# Example 2: F(x) = 1 - e^(-3x), f(x) = 3e^(-3x)
lam = 3
F2 = lambda x: 1 - np.exp(-lam * x)
f2 = lambda x: lam * np.exp(-lam * x)

# Verify normalization
norm, _ = integrate.quad(f2, 0, np.inf)
print(f"\nExp(3) PDF normalization: {norm:.6f}")

# Verify F'(x) = f(x) numerically at x = 1
h = 1e-8
deriv = (F2(1 + h) - F2(1)) / h
print(f"F'(1) = {deriv:.4f}, f(1) = {f2(1):.4f}")
```
