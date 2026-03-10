# Independence of Random Variables

Two random variables are independent if knowing the value of one provides no information about the other — their joint distribution factors into the product of the marginals.

## Definition

Random variables $X$ and $Y$ are **independent** if for all $x, y$:

$$
p_{X,Y}(x, y) = p_X(x) \cdot p_Y(y) \qquad \text{(discrete)}
$$

$$
f_{X,Y}(x, y) = f_X(x) \cdot f_Y(y) \qquad \text{(continuous)}
$$

$X_1, \ldots, X_n$ are **mutually independent** if for all $x_1, \ldots, x_n$:

$$
p(x_1, \ldots, x_n) = p_{X_1}(x_1) \cdots p_{X_n}(x_n)
$$

## Explanation

### Equivalent Characterizations

$X$ and $Y$ are independent if and only if any of the following hold:

1. Joint = product of marginals (definition above)
2. $p_{X|Y}(x \mid y) = p_X(x)$ for all $x, y$ (conditional equals marginal)
3. $F_{X,Y}(x, y) = F_X(x) \cdot F_Y(y)$ for all $x, y$ (joint CDF factors)
4. $E[g(X)h(Y)] = E[g(X)]\,E[h(Y)]$ for all bounded $g, h$

### Pairwise vs Mutual Independence

**Pairwise independence:** every pair $X_i, X_j$ is independent. **Mutual independence:** the full joint factors into a product of all marginals.

!!! warning "Pairwise does not imply mutual"
    Mutual independence requires the joint to factor for *all* subsets, not just pairs. Pairwise independence is strictly weaker.

### Conditional Independence

$X$ and $Y$ are **conditionally independent given $Z$** if $p(x, y \mid z) = p(x \mid z) \cdot p(y \mid z)$ for all $x, y, z$.

Neither conditional independence nor unconditional independence implies the other.

## Examples

**Example.** Roll two fair dice independently. Let $X$ = first die, $Y$ = second die, $S = X + Y$.

$X$ and $Y$ are independent: $P(X = i, Y = j) = 1/36 = (1/6)(1/6)$ for all $i, j$.

$X$ and $S$ are **not** independent: $P(X = 6, S = 2) = 0$ but $P(X = 6) \cdot P(S = 2) = (1/6)(1/36) > 0$.

```python
# Verify X and Y independent, X and S dependent
from itertools import product

outcomes = [(i, j) for i in range(1,7) for j in range(1,7)]

# Check X, Y independence
for i in range(1, 7):
    for j in range(1, 7):
        joint = sum(1 for x, y in outcomes if x == i and y == j) / 36
        marginal = (1/6) * (1/6)
        assert abs(joint - marginal) < 1e-10

print("X, Y: independent (all 36 cells match product of marginals)")

# Check X, S dependence: find a counterexample
x_val, s_val = 6, 2
joint = sum(1 for x, y in outcomes if x == x_val and x + y == s_val) / 36
px = 1/6
ps = sum(1 for x, y in outcomes if x + y == s_val) / 36
print(f"\nP(X=6, S=2) = {joint:.4f}")
print(f"P(X=6) * P(S=2) = {px * ps:.6f}")
print("X, S: dependent")
```
