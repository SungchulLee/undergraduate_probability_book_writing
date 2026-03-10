# Conditional PDF

The conditional PDF is the continuous analogue of the conditional PMF — slice the joint density at the given value and normalize.

## Definition

The **conditional PDF** of $X$ given $Y = y$ is

$$
f_{X|Y}(x \mid y) = \frac{f_{X,Y}(x, y)}{f_Y(y)}, \qquad f_Y(y) > 0
$$

Similarly, $f_{Y|X}(y \mid x) = f_{X,Y}(x, y) / f_X(x)$.

## Explanation

### Slice and Normalize (Continuous)

1. **Slice:** Fix $Y = y$ and view $f_{X,Y}(x, y)$ as a function of $x$ alone
2. **Normalize:** Divide by $f_Y(y)$ so the result integrates to 1 over $x$

### Verification

$$
\int_{-\infty}^{\infty} f_{X|Y}(x \mid y)\,dx = \frac{1}{f_Y(y)}\int_{-\infty}^{\infty} f_{X,Y}(x, y)\,dx = \frac{f_Y(y)}{f_Y(y)} = 1
$$

### Conditional Expectation (Preview)

$$
E[X \mid Y = y] = \int_{-\infty}^{\infty} x\,f_{X|Y}(x \mid y)\,dx
$$

This is treated in depth in Chapter 8.

## Examples

**Example.** $(X, Y)$ uniform on the triangle $\{0 \le y \le x \le 1\}$ with $f(x,y) = 2$.

Marginal: $f_X(x) = 2x$ for $0 \le x \le 1$.

Conditional of $Y$ given $X = x$:

$$
f_{Y|X}(y \mid x) = \frac{f(x, y)}{f_X(x)} = \frac{2}{2x} = \frac{1}{x}, \quad 0 \le y \le x
$$

This is $\text{Uniform}(0, x)$. Given $X = x$, the variable $Y$ is uniformly spread over $[0, x]$.

Conditional expectation: $E[Y \mid X = x] = x/2$.

Marginal: $f_Y(y) = 2(1-y)$ for $0 \le y \le 1$.

Conditional of $X$ given $Y = y$:

$$
f_{X|Y}(x \mid y) = \frac{2}{2(1-y)} = \frac{1}{1-y}, \quad y \le x \le 1
$$

This is $\text{Uniform}(y, 1)$.

```python
from scipy import integrate

# f(x,y) = 2 on triangle, f_X(x) = 2x
# f_{Y|X}(y | x) = 1/x on [0, x]

# Verify conditional integrates to 1 for x = 0.6
x = 0.6
cond_norm, _ = integrate.quad(lambda y: 1/x, 0, x)
print(f"Conditional PDF normalization for x={x}: {cond_norm:.4f}")

# Conditional expectation E[Y | X = x] = x/2
E_Y_given_x, _ = integrate.quad(lambda y: y * (1/x), 0, x)
print(f"E[Y | X={x}] = {E_Y_given_x:.4f} (theory: {x/2:.4f})")
```
