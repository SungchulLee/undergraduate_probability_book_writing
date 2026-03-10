# Joint PMF

The joint PMF describes the simultaneous behavior of two or more discrete random variables — it is the multivariate generalization of the PMF.

## Definition

For discrete random variables $X$ and $Y$, the **joint PMF** is

$$
p_{X,Y}(x, y) = P(X = x, Y = y)
$$

A valid joint PMF satisfies:

1. **Non-negativity:** $p_{X,Y}(x, y) \ge 0$ for all $(x, y)$
2. **Normalization:** $\displaystyle\sum_x \sum_y p_{X,Y}(x, y) = 1$

For any set $A \subseteq \mathbb{R}^2$:

$$
P((X, Y) \in A) = \sum_{(x,y) \in A} p_{X,Y}(x, y)
$$

## Explanation

### Random Vectors

A **random vector** $(X, Y) : \Omega \to \mathbb{R}^2$ maps each outcome $\omega$ to the point $(X(\omega), Y(\omega))$. The joint distribution describes how probability mass is spread across $\mathbb{R}^2$.

In the brick analogy: each outcome $\omega$ carries a brick to the point $(X(\omega), Y(\omega))$ in the plane. The weight at each point $(x, y)$ is the joint PMF value $p_{X,Y}(x, y)$.

### Structural Zeros

Some joint PMF entries may be zero not by coincidence but by necessity. If $Y \ge X$ always holds (as when $X$ counts a subset of what $Y$ counts), then $p_{X,Y}(x, y) = 0$ for all $y < x$. Recognizing structural zeros helps catch errors in table construction.

### Joint PMF Determines Everything

The joint PMF contains all probabilistic information about $(X, Y)$. From it you can derive:

- Marginal PMFs (by summing rows or columns)
- Conditional PMFs (by normalizing a row or column)
- Independence (by checking if joint = product of marginals)

## Examples

**Example.** Flip a fair coin 3 times. Let $X$ = heads in first two flips, $Y$ = total heads.

| | $X=0$ | $X=1$ | $X=2$ |
|:---|:---:|:---:|:---:|
| $Y=3$ | 0 | 0 | $1/8$ |
| $Y=2$ | 0 | $2/8$ | $1/8$ |
| $Y=1$ | $1/8$ | $2/8$ | 0 |
| $Y=0$ | $1/8$ | 0 | 0 |

Structural zeros: $Y < X$ is impossible, and $Y > X + 1$ is impossible (only one remaining flip). So $Y \in \{X, X+1\}$.

$P(X = 1, Y = 2) = 2/8$ because two outcomes (HTH, THH) give $X=1, Y=2$.

```python
from itertools import product

outcomes = list(product('HT', repeat=3))
table = {}
for w in outcomes:
    x = w[:2].count('H')
    y = w.count('H')
    table[(x, y)] = table.get((x, y), 0) + 1/8

print("Joint PMF table:")
for y in range(3, -1, -1):
    row = [f"{table.get((x, y), 0):.3f}" for x in range(3)]
    print(f"  Y={y}: {row}")

print(f"Sum = {sum(table.values()):.4f}")
```
