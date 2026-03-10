# Law of Iterated Expectations (Tower Property)

The overall average of $X$ equals the average of the conditional averages — compute group means first, then average over groups.

## Definition

For any random variables $X$ and $Y$:

$$
E[X] = E\bigl[E[X \mid Y]\bigr]
$$

The outer expectation averages over the randomness in $Y$. Explicitly:

**Discrete:**

$$
E[X] = \sum_y E[X \mid Y = y]\,P(Y = y)
$$

**Continuous:**

$$
E[X] = \int_{-\infty}^{\infty} E[X \mid Y = y]\,f_Y(y)\,dy
$$

## Explanation

### Proof (Discrete Case)

$$
\begin{aligned}
E\bigl[E[X \mid Y]\bigr] &= \sum_y E[X \mid Y = y]\,P(Y = y) \\
&= \sum_y \left(\sum_x x\,P(X = x \mid Y = y)\right) P(Y = y) \\
&= \sum_x x \sum_y P(X = x \mid Y = y)\,P(Y = y) \\
&= \sum_x x\,P(X = x) = E[X]
\end{aligned}
$$

The key step uses the law of total probability to collapse the inner sum.

### Intuition

The tower property is a weighted average of weighted averages. To find the mean height of all students in a university, compute the mean height in each department and then take a weighted average by department size. The result equals the overall mean.

### Properties of Conditional Expectation

These identities hold as equalities between random variables and are essential for applying the tower property:

| Property | Statement |
|:---------|:----------|
| Linearity | $E[aX + bZ \mid Y] = a\,E[X \mid Y] + b\,E[Z \mid Y]$ |
| Known values | $E[h(Y) \mid Y] = h(Y)$ |
| Factoring out | $E[h(Y) \cdot X \mid Y] = h(Y) \cdot E[X \mid Y]$ |
| Independence | $E[X \mid Y] = E[X]$ when $X \perp Y$ |
| Tower | $E\bigl[E[X \mid Y]\bigr] = E[X]$ |

### Strategy for Computing $E[X]$

1. Choose a conditioning variable $Y$ that simplifies the problem
2. Compute $E[X \mid Y = y]$ for each $y$
3. Average over $Y$: $E[X] = E\bigl[E[X \mid Y]\bigr]$

The tower property converts hard marginal calculations into easier conditional ones.

## Examples

**Example.** $X, Y$ iid $\text{Bin}(n, p)$. Find $E[X \mid X + Y = m]$.

By the tower property applied to $X + Y$: $E[X + Y \mid X + Y = m] = m$. By linearity and symmetry (since $X$ and $Y$ are iid), $E[X \mid X + Y = m] = E[Y \mid X + Y = m]$. Therefore:

$$
E[X \mid X + Y = m] = \frac{m}{2}
$$

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000
n, p = 10, 0.3

X = np.random.binomial(n, p, n_sim)
Y = np.random.binomial(n, p, n_sim)
S = X + Y

# Verify E[X | X+Y = m] = m/2
for m in [3, 5, 8, 10]:
    mask = (S == m)
    if mask.sum() > 100:
        print(f"E[X | X+Y={m}] = {X[mask].mean():.3f}  (theory: {m/2:.1f})")

# Verify tower property
print(f"\nE[X] = {X.mean():.4f}  (theory: {n*p})")
```
