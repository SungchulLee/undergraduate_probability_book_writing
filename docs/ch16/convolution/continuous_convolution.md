# Continuous Convolution

The PDF of a sum of independent continuous random variables is obtained by convolving their densities — integrating over all ways the parts can add up.

## Definition

If $X$ and $Y$ are **independent** continuous random variables, the **convolution** of their PDFs gives the PDF of $X + Y$:

$$
f_{X+Y}(a) = (f_X * f_Y)(a) = \int_{-\infty}^{\infty} f_X(b) \cdot f_Y(a - b) \, db
$$

The integrand is nonzero only where both $f_X(b) > 0$ and $f_Y(a-b) > 0$.

## Explanation

### Derivation

Conditioning on $X = b$:

$$
f_{X+Y}(a) = \int_{-\infty}^{\infty} f_Y(a - b) \cdot f_X(b) \, db
$$

This sums the density of $Y = a - b$ weighted by the density of $X = b$ over all possible values of $b$.

### Finding Integration Limits

The main challenge is determining where the integrand is nonzero.

**Strategy:**

1. Write the supports: $b \in [x_{\min}, x_{\max}]$ and $a - b \in [y_{\min}, y_{\max}]$
2. Solve for $b$: combine $x_{\min} \le b \le x_{\max}$ with $a - y_{\max} \le b \le a - y_{\min}$
3. Take the intersection to get effective limits

The limits often depend on $a$, creating a piecewise formula.

### Properties

| Property | Statement |
|:---|:---|
| Commutativity | $f_X * f_Y = f_Y * f_X$ |
| Associativity | $(f_X * f_Y) * f_Z = f_X * (f_Y * f_Z)$ |
| MGF domain | $f_X * f_Y \leftrightarrow M_X(t) \cdot M_Y(t)$ |
| Variance | $\operatorname{Var}(X+Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$ (independence) |

Convolution in the density domain is multiplication in the MGF domain — analogous to the convolution theorem in signal processing.

## Examples

**Example.** $X, Y$ iid $\operatorname{Exp}(1)$. For $a \ge 0$:

$$
f_{X+Y}(a) = \int_0^a e^{-b} \cdot e^{-(a-b)} \, db = e^{-a} \int_0^a db = a \, e^{-a}
$$

This is the $\operatorname{Gamma}(2, 1)$ PDF.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 100_000

X = np.random.exponential(1.0, n_sim)
Y = np.random.exponential(1.0, n_sim)
S = X + Y

# Compare simulation with Gamma(2,1) theory
a_vals = np.linspace(0, 8, 200)
pdf_theory = stats.gamma.pdf(a_vals, a=2, scale=1.0)

# Numerical convolution on a grid
dx = 0.01
grid = np.arange(0, 10, dx)
f_exp = np.exp(-grid)
f_conv = np.convolve(f_exp, f_exp) * dx

print(f"Simulated: mean={S.mean():.4f}, var={S.var():.4f}")
print(f"Theory:    mean=2.0000, var=2.0000")
print(f"Numerical convolution peak at a=1: {f_conv[100]:.4f}  (theory: {1*np.exp(-1):.4f})")
```
