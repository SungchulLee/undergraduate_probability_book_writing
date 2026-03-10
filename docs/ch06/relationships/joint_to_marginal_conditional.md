# Joint, Marginal, and Conditional Relationships

The joint, marginal, and conditional distributions form a triangle: given any two, you can recover the third.

## Definition

**Marginalization** (joint $\to$ marginal):

$$
p_X(x) = \sum_y p_{X,Y}(x, y), \qquad f_X(x) = \int f_{X,Y}(x, y)\,dy
$$

**Conditioning** (joint $\to$ conditional):

$$
p_{Y|X}(y \mid x) = \frac{p_{X,Y}(x, y)}{p_X(x)}, \qquad f_{Y|X}(y \mid x) = \frac{f_{X,Y}(x, y)}{f_X(x)}
$$

**Chain rule** (marginal + conditional $\to$ joint):

$$
p_{X,Y}(x, y) = p_X(x) \cdot p_{Y|X}(y \mid x)
$$

## Explanation

### The Triangle

| Known | Want | Formula |
|:------|:-----|:--------|
| Joint $p(x,y)$ | Marginal $p_X(x)$ | $\sum_y p(x,y)$ |
| Joint $p(x,y)$ | Conditional $p(y \mid x)$ | $p(x,y) / p_X(x)$ |
| Marginal $p_X(x)$ + Conditional $p(y \mid x)$ | Joint $p(x,y)$ | $p_X(x) \cdot p(y \mid x)$ |

### Why the Chain Rule Matters

In many problems, the joint distribution is not given directly, but a marginal and conditional are natural. Drawing without replacement, multistage experiments, and Bayesian models all specify distributions sequentially — the chain rule assembles the joint from these pieces.

### Connection to Bayes' Theorem

Both decompositions of the joint must agree:

$$
p_X(x) \cdot p_{Y|X}(y \mid x) = p_{X,Y}(x, y) = p_Y(y) \cdot p_{X|Y}(x \mid y)
$$

Rearranging: $p_{X|Y}(x \mid y) = p_{Y|X}(y \mid x) \cdot p_X(x) / p_Y(y)$ — Bayes' theorem.

## Examples

**Example.** Verify the chain rule with the joint PMF:

| | $x=0$ | $x=1$ | $x=2$ |
|:---|:---:|:---:|:---:|
| $y=1$ | $0$ | $2/10$ | $1/10$ |

Marginals: $p_X(1) = 3/10$. Conditional: $p_{Y|X}(1 \mid 1) = (2/10)/(3/10) = 2/3$.

Chain rule: $p_X(1) \cdot p_{Y|X}(1 \mid 1) = (3/10)(2/3) = 2/10 = p_{X,Y}(1, 1)$.

```python
# Verify chain rule: p(x,y) = p(x) * p(y|x)
joint_11 = 2/10
px_1 = 3/10
py_given_x1_1 = joint_11 / px_1

reconstructed = px_1 * py_given_x1_1
print(f"p(1,1) = {joint_11:.4f}")
print(f"p_X(1) * p(Y=1|X=1) = {px_1:.2f} * {py_given_x1_1:.4f} = {reconstructed:.4f}")
print(f"Match: {abs(joint_11 - reconstructed) < 1e-10}")
```
