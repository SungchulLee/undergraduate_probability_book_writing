# Marginal PMF

The marginal PMF extracts the distribution of a single variable from a joint distribution by summing over all values of the other variable.

## Definition

Given the joint PMF $p_{X,Y}(x, y)$, the **marginal PMFs** are

$$
p_X(x) = \sum_y p_{X,Y}(x, y), \qquad p_Y(y) = \sum_x p_{X,Y}(x, y)
$$

In a joint PMF table: column sums give $p_X$, row sums give $p_Y$.

## Explanation

### Why "Marginal"

The name comes from writing marginal totals in the margins of a joint PMF table. The right margin contains row sums ($p_Y$) and the bottom margin contains column sums ($p_X$).

### Information Loss

Marginalization discards information about the relationship between $X$ and $Y$. Different joint PMFs can produce the same marginals — the marginals alone cannot reconstruct the joint (unless independence is known).

### Discrete vs Continuous

| Operation | Discrete | Continuous |
|:----------|:---------|:-----------|
| Marginal of $X$ | $p_X(x) = \sum_y p(x,y)$ | $f_X(x) = \int f(x,y)\,dy$ |
| Marginal of $Y$ | $p_Y(y) = \sum_x p(x,y)$ | $f_Y(y) = \int f(x,y)\,dx$ |

## Examples

**Example.** Joint PMF table with marginals:

| | $x=0$ | $x=1$ | $x=2$ | $p_Y(y)$ |
|:---|:---:|:---:|:---:|:---:|
| $y=3$ | $1/10$ | $1/10$ | $1/10$ | $3/10$ |
| $y=2$ | $1/10$ | $0$ | $1/10$ | $2/10$ |
| $y=1$ | $0$ | $2/10$ | $1/10$ | $3/10$ |
| $y=0$ | $1/10$ | $0$ | $1/10$ | $2/10$ |
| $p_X(x)$ | $3/10$ | $3/10$ | $4/10$ | $1$ |

$P(X = 0) = 1/10 + 1/10 + 0 + 1/10 = 3/10$ (column sum).

$P(Y = 1) = 0 + 2/10 + 1/10 = 3/10$ (row sum).

```python
import numpy as np

joint = np.array([
    [1/10, 1/10, 1/10],  # y=3
    [1/10, 0,    1/10],  # y=2
    [0,    2/10, 1/10],  # y=1
    [1/10, 0,    1/10],  # y=0
])

px = joint.sum(axis=0)  # column sums
py = joint.sum(axis=1)  # row sums

print("Marginal of X:", [f"{p:.1f}" for p in px])
print("Marginal of Y:", [f"{p:.1f}" for p in py])
print(f"Total: {joint.sum():.1f}")
```
