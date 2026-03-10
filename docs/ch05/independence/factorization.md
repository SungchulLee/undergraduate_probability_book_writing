# Verifying Independence via Factorization

Independence is verified by checking whether the joint distribution factors into the product of marginals for every pair of values — a single failure means dependence.

## Definition

$X$ and $Y$ are independent if and only if

$$
p_{X,Y}(x, y) = p_X(x) \cdot p_Y(y) \quad \text{for all } x, y
$$

If **any** pair $(x, y)$ violates this, $X$ and $Y$ are dependent.

## Explanation

### Constructing the Joint PMF Under Independence

When $X$ and $Y$ are independent, the joint PMF is completely determined by the two marginals — just multiply:

$$
p_{X,Y}(x_i, y_j) = p_X(x_i) \cdot p_Y(y_j)
$$

### Quick Dependence Test

If the joint PMF table has a zero at $(x_i, y_j)$ but both marginals $p_X(x_i) > 0$ and $p_Y(y_j) > 0$, then $X$ and $Y$ are dependent. Under independence, $p(x_i, y_j) = p_X(x_i) \cdot p_Y(y_j) > 0$, so an interior zero is impossible.

### Checking via Conditional Distributions

Equivalently, $X$ and $Y$ are independent iff the conditional distribution of $X$ given $Y = y$ does not depend on $y$:

$$
p_{X|Y}(x \mid y) = p_X(x) \quad \text{for all } x, y
$$

If the conditional changes with $y$, the variables are dependent.

## Examples

**Example 1 (Dependent).** Joint PMF:

| | $x=0$ | $x=1$ | $x=2$ | $p_Y(y)$ |
|:---|:---:|:---:|:---:|:---:|
| $y=3$ | $1/6$ | $1/6$ | $1/6$ | $3/6$ |
| $y=2$ | $1/6$ | $1/6$ | $0$ | $2/6$ |
| $y=1$ | $1/6$ | $0$ | $0$ | $1/6$ |
| $p_X(x)$ | $3/6$ | $2/6$ | $1/6$ | $1$ |

$p_X(1) \cdot p_Y(1) = (2/6)(1/6) = 2/36 \ne 0 = p_{X,Y}(1, 1)$. **Dependent.**

The conditional of $X$ given $Y$ also changes: $P(X=0 \mid Y=1) = 1$ but $P(X=0 \mid Y=3) = 1/3$.

**Example 2 (Independent).** If $p_X = (2/10, 3/10, 5/10)$ and $p_Y = (2/10, 3/10, 2/10, 3/10)$, the independent joint PMF has cell $(x_i, y_j) = p_X(x_i) \cdot p_Y(y_j)$. Every cell is positive and the factorization holds by construction.

```python
import numpy as np

# Example 1: Check dependence
joint = np.array([
    [1/6, 1/6, 1/6],  # y=3
    [1/6, 1/6, 0],    # y=2
    [1/6, 0,   0],    # y=1
])
px = joint.sum(axis=0)  # column sums
py = joint.sum(axis=1)  # row sums

independent = True
for i in range(3):
    for j in range(3):
        product = px[j] * py[i]
        if abs(joint[i, j] - product) > 1e-10:
            independent = False
            print(f"Violation at (x={j}, y={3-i}): "
                  f"joint={joint[i,j]:.4f}, product={product:.4f}")

print(f"Independent: {independent}")
```
