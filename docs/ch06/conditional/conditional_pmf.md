# Conditional PMF

The conditional PMF describes the distribution of one discrete random variable given the observed value of another — it is obtained by slicing and normalizing the joint PMF.

## Definition

The **conditional PMF** of $X$ given $Y = y$ is

$$
p_{X|Y}(x \mid y) = \frac{p_{X,Y}(x, y)}{p_Y(y)}, \qquad p_Y(y) > 0
$$

Similarly, $p_{Y|X}(y \mid x) = p_{X,Y}(x, y) / p_X(x)$.

## Explanation

### Slice and Normalize

1. **Slice:** Extract the row (or column) of the joint PMF table corresponding to the given value
2. **Normalize:** Divide each entry by the row (or column) sum so the result sums to 1

### Verification

$$
\sum_x p_{X|Y}(x \mid y) = \sum_x \frac{p_{X,Y}(x, y)}{p_Y(y)} = \frac{p_Y(y)}{p_Y(y)} = 1
$$

### Connection to Independence

If $X \perp Y$, then $p_{X|Y}(x \mid y) = p_X(x)$ — the conditional equals the marginal. Knowing $Y$ tells you nothing about $X$.

## Examples

**Example.** From the joint PMF:

| | $x=0$ | $x=1$ | $x=2$ |
|:---|:---:|:---:|:---:|
| $y=3$ | $1/10$ | $1/10$ | $1/10$ |
| $y=2$ | $1/10$ | $0$ | $1/10$ |
| $y=1$ | $0$ | $2/10$ | $1/10$ |
| $y=0$ | $1/10$ | $0$ | $1/10$ |

**Conditional of $X$ given $Y = 1$:** Row $y=1$ is $(0, 2/10, 1/10)$, row sum $= 3/10$.

$$
P(X=0 \mid Y=1) = 0, \quad P(X=1 \mid Y=1) = \frac{2}{3}, \quad P(X=2 \mid Y=1) = \frac{1}{3}
$$

**Conditional of $Y$ given $X = 2$:** Column $x=2$ is $(1/10, 1/10, 1/10, 1/10)$, sum $= 4/10$.

$$
P(Y=k \mid X=2) = \frac{1}{4} \text{ for } k = 0, 1, 2, 3
$$

Given $X = 2$, the variable $Y$ is uniform on $\{0, 1, 2, 3\}$.

```python
import numpy as np

joint = np.array([
    [1/10, 1/10, 1/10],  # y=3
    [1/10, 0,    1/10],  # y=2
    [0,    2/10, 1/10],  # y=1
    [1/10, 0,    1/10],  # y=0
])

# Conditional of X given Y=1 (row index 2)
row = joint[2, :]
cond = row / row.sum()
print("P(X | Y=1):", [f"{p:.4f}" for p in cond])

# Conditional of Y given X=2 (column index 2)
col = joint[:, 2]
cond_y = col / col.sum()
print("P(Y | X=2):", [f"{p:.4f}" for p in cond_y])
```
