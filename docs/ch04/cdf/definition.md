# Cumulative Distribution Function

The CDF is the universal description of a random variable's distribution — it works for discrete, continuous, and mixed random variables alike.

## Definition

The **cumulative distribution function (CDF)** of a random variable $X$ is

$$
F_X(x) = P(X \le x), \quad x \in \mathbb{R}
$$

Every CDF satisfies three properties:

1. **Non-decreasing:** $a < b \implies F(a) \le F(b)$
2. **Right-continuous:** $\lim_{x \to a^+} F(x) = F(a)$
3. **Boundary limits:** $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to +\infty} F(x) = 1$

Conversely, any function satisfying these three properties is the CDF of some random variable.

## Explanation

### Computing Probabilities from the CDF

$$
P(a < X \le b) = F(b) - F(a)
$$

$$
P(X > a) = 1 - F(a)
$$

$$
P(X = a) = F(a) - F(a^-) = \text{jump size at } a
$$

where $F(a^-) = \lim_{x \to a^-} F(x)$ is the left-hand limit.

### Why Right-Continuous?

The CDF is defined with $\le$ (not $<$), so $F(a)$ includes the point $a$ itself. For discrete variables, this means the CDF jumps *at* the point and the new value is $F(a)$, making it right-continuous. The left-hand limit $F(a^-)$ captures the cumulative probability just before $a$.

### Discrete vs Continuous CDF

| Property | Discrete CDF | Continuous CDF |
|:---------|:-------------|:---------------|
| Shape | Step function | Smooth curve |
| Jumps | At each value $x_i$ | None |
| $P(X = a)$ | Jump size at $a$ | Always 0 |
| Recover distribution | PMF from jumps | PDF from derivative |

## Examples

**Example.** A discrete random variable has the following CDF with jumps at $x = 1, 3, 5$:

$$
F(x) = \begin{cases}
0 & x < 1 \\
0.2 & 1 \le x < 3 \\
0.7 & 3 \le x < 5 \\
1.0 & x \ge 5
\end{cases}
$$

Reading probabilities:

- $P(X = 1) = 0.2 - 0 = 0.2$
- $P(X = 3) = 0.7 - 0.2 = 0.5$
- $P(X = 5) = 1.0 - 0.7 = 0.3$
- $P(2 < X \le 5) = F(5) - F(2) = 1.0 - 0.2 = 0.8$
- $P(X > 3) = 1 - F(3) = 1 - 0.7 = 0.3$

```python
import numpy as np

# Discrete CDF with jumps at 1, 3, 5
def F(x):
    if x < 1: return 0.0
    elif x < 3: return 0.2
    elif x < 5: return 0.7
    else: return 1.0

# Verify probability computations
print(f"P(X = 1) = {F(1) - F(0.999):.1f}")
print(f"P(X = 3) = {F(3) - F(2.999):.1f}")
print(f"P(X = 5) = {F(5) - F(4.999):.1f}")
print(f"P(2 < X <= 5) = {F(5) - F(2):.1f}")
print(f"P(X > 3) = {1 - F(3):.1f}")
print(f"Sum of PMF = {0.2 + 0.5 + 0.3:.1f}")
```
