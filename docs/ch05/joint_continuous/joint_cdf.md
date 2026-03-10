# Joint CDF

The joint CDF is the universal characterization of a joint distribution — it works for discrete, continuous, and mixed random vectors.

## Definition

The **joint CDF** of random variables $(X, Y)$ is

$$
F_{X,Y}(x, y) = P(X \le x, Y \le y)
$$

Properties:

1. **Non-decreasing** in each argument
2. **Boundary limits:** $F(-\infty, y) = F(x, -\infty) = 0$, $F(\infty, \infty) = 1$
3. **Right-continuous** in each argument

**Continuous case:**

$$
F_{X,Y}(x, y) = \int_{-\infty}^{x}\!\int_{-\infty}^{y} f_{X,Y}(s, t)\,dt\,ds
$$

**Discrete case:**

$$
F_{X,Y}(x, y) = \sum_{x_i \le x}\sum_{y_j \le y} p_{X,Y}(x_i, y_j)
$$

## Explanation

### Recovering the Joint PDF

For continuous $(X, Y)$:

$$
f_{X,Y}(x, y) = \frac{\partial^2}{\partial x\,\partial y}F_{X,Y}(x, y)
$$

### Rectangle Probability Formula

$$
P(a < X \le b,\; c < Y \le d) = F(b,d) - F(a,d) - F(b,c) + F(a,c)
$$

This is inclusion-exclusion for the rectangle $(a,b] \times (c,d]$. The pattern generalizes to higher dimensions via the inclusion-exclusion principle on hyperrectangles.

### Marginal CDFs

$$
F_X(x) = F_{X,Y}(x, \infty) = \lim_{y \to \infty} F_{X,Y}(x, y)
$$

$$
F_Y(y) = F_{X,Y}(\infty, y) = \lim_{x \to \infty} F_{X,Y}(x, y)
$$

## Examples

**Example.** $(X, Y) \sim \text{Uniform}([0,1]^2)$ with $f(x,y) = 1$ on the unit square.

$$
F(x, y) = \begin{cases}
xy & 0 \le x \le 1,\; 0 \le y \le 1 \\
x & 0 \le x \le 1,\; y > 1 \\
y & x > 1,\; 0 \le y \le 1 \\
1 & x > 1,\; y > 1 \\
0 & x < 0 \text{ or } y < 0
\end{cases}
$$

Rectangle probability: $P(1/4 < X \le 3/4,\; 1/4 < Y \le 3/4)$

$$
= F(3/4, 3/4) - F(1/4, 3/4) - F(3/4, 1/4) + F(1/4, 1/4)
$$

$$
= \frac{9}{16} - \frac{3}{16} - \frac{3}{16} + \frac{1}{16} = \frac{4}{16} = \frac{1}{4}
$$

```python
# Uniform on [0,1]^2: verify rectangle formula
def F(x, y):
    x = max(0, min(1, x))
    y = max(0, min(1, y))
    return x * y

# P(1/4 < X <= 3/4, 1/4 < Y <= 3/4)
a, b, c, d = 1/4, 3/4, 1/4, 3/4
prob = F(b, d) - F(a, d) - F(b, c) + F(a, c)
print(f"P(1/4 < X <= 3/4, 1/4 < Y <= 3/4) = {prob:.4f}")
print(f"Direct: (3/4 - 1/4) * (3/4 - 1/4) = {(b-a) * (d-c):.4f}")

# Marginals
print(f"\nF_X(0.5) = F(0.5, inf) = {F(0.5, 1):.4f}")
print(f"F_Y(0.7) = F(inf, 0.7) = {F(1, 0.7):.4f}")
```
