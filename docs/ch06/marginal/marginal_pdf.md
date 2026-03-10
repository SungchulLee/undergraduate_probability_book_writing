# Marginal PDF

The marginal PDF of a continuous random variable is obtained by integrating the joint PDF over all values of the other variable.

## Definition

Given the joint PDF $f_{X,Y}(x, y)$, the **marginal PDFs** are

$$
f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y)\,dy, \qquad f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y)\,dx
$$

## Explanation

### Geometric Interpretation

The marginal density $f_X(x)$ at a point $x$ is the total density along the vertical line at $x$ — the integral of the joint density surface along that line. This "projects" the two-dimensional density onto the $x$-axis.

### Integration Limits

!!! warning "Limits depend on the support"
    When the support of $(X, Y)$ is not a rectangle, the integration limits for $y$ depend on $x$ (and vice versa). Getting these limits correct is the main difficulty in marginal PDF computations.

## Examples

**Example.** $(X, Y)$ uniform on the triangle $\{0 \le y \le x \le 1\}$.

Area $= 1/2$, so $f(x, y) = 2$ on the triangle.

Marginal of $X$: for $0 \le x \le 1$,

$$
f_X(x) = \int_0^x 2\,dy = 2x
$$

Marginal of $Y$: for $0 \le y \le 1$,

$$
f_Y(y) = \int_y^1 2\,dx = 2(1 - y)
$$

Verification: $\int_0^1 2x\,dx = 1$ and $\int_0^1 2(1-y)\,dy = 1$.

```python
from scipy import integrate

# f(x, y) = 2 on triangle 0 <= y <= x <= 1
# Marginal of X: f_X(x) = 2x
# Marginal of Y: f_Y(y) = 2(1-y)

# Verify normalization
norm_x, _ = integrate.quad(lambda x: 2*x, 0, 1)
norm_y, _ = integrate.quad(lambda y: 2*(1-y), 0, 1)
print(f"int f_X(x) dx = {norm_x:.4f}")
print(f"int f_Y(y) dy = {norm_y:.4f}")

# Verify joint normalization
norm_joint, _ = integrate.dblquad(
    lambda y, x: 2, 0, 1, lambda x: 0, lambda x: x
)
print(f"int int f(x,y) dy dx = {norm_joint:.4f}")
```
