# Functions of Discrete Random Variables

For discrete random variables, finding the distribution of $g(X)$ reduces to grouping values of $X$ that map to the same output and summing their probabilities.

## Definition

If $X$ is discrete with PMF $p_X(x)$ and $Y = g(X)$, then $Y$ is discrete with PMF

$$
p_Y(y) = \sum_{x:\, g(x) = y} p_X(x)
$$

The support of $Y$ is $\{g(x) : x \in \text{support of } X\}$.

## Explanation

### Algorithm

1. List all values $x$ in the support of $X$ and their probabilities
2. Compute $g(x)$ for each
3. Group by the resulting $y$ values
4. Sum probabilities within each group

### Many-to-One Functions

When $g$ is not injective, distinct $x$ values can produce the same $y$. This concentrates probability: the PMF of $Y$ can have fewer support points but larger individual probabilities than $X$.

### Common Transformations

| Function $g$ | Effect |
|:-------------|:-------|
| $g(x) = x^2$ | Folds negative and positive values together |
| $g(x) = \|x\|$ | Same as $x^2$ for sign, preserves magnitude |
| $g(x) = \mathbf{1}(x > c)$ | Reduces to Bernoulli |
| $g(x) = \max(x, 0)$ | Truncates negatives to 0 (point mass) |

## Examples

**Example 1.** $X \sim \text{Bin}(10, 0.3)$ and $Y = \mathbf{1}(X \ge 5)$.

All 11 values of $X$ collapse into two values of $Y$:

$$
P(Y = 1) = P(X \ge 5) = \sum_{k=5}^{10}\binom{10}{k}(0.3)^k(0.7)^{10-k} \approx 0.1503
$$

$$
P(Y = 0) = 1 - P(Y = 1) \approx 0.8497
$$

**Example 2.** $X \sim \text{Uniform}\{-3, -2, -1, 0, 1, 2, 3\}$ and $Y = \max(X, 0)$.

| $y$ | 0 | 1 | 2 | 3 |
|:---:|:---:|:---:|:---:|:---:|
| $p_Y(y)$ | $4/7$ | $1/7$ | $1/7$ | $1/7$ |

The four values $\{-3, -2, -1, 0\}$ all map to $y = 0$, creating a large point mass.

```python
from math import comb

# Example 1: Indicator of Binomial
n, p = 10, 0.3
p_ge_5 = sum(comb(n, k) * p**k * (1-p)**(n-k) for k in range(5, 11))
print(f"P(Y=1) = P(X >= 5) = {p_ge_5:.4f}")
print(f"P(Y=0) = P(X <  5) = {1 - p_ge_5:.4f}")

# Example 2: max(X, 0)
x_vals = list(range(-3, 4))
px = 1 / len(x_vals)
from collections import Counter
py = Counter()
for x in x_vals:
    py[max(x, 0)] += px

print("\nY = max(X, 0):")
for y in sorted(py):
    print(f"  P(Y = {y}) = {py[y]:.4f}")
```
