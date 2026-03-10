# Recovering the Joint Distribution

The chain rule reconstructs the joint distribution from a marginal and a conditional — this is the standard approach for sequential experiments and Bayesian models.

## Definition

The **chain rule** (multiplication rule for distributions):

$$
p_{X,Y}(x, y) = p_X(x) \cdot p_{Y|X}(y \mid x) = p_Y(y) \cdot p_{X|Y}(x \mid y)
$$

For $n$ variables:

$$
p(x_1, \ldots, x_n) = p(x_1)\,p(x_2 \mid x_1)\,p(x_3 \mid x_1, x_2)\cdots p(x_n \mid x_1, \ldots, x_{n-1})
$$

## Explanation

### When to Use This

Use the chain rule when the problem naturally specifies:

- A **marginal** (distribution of the first draw, prior distribution)
- A **conditional** (distribution of the second draw given the first, likelihood)

This arises in sampling without replacement, multistage experiments, and Bayesian inference.

### Connection to Bayes' Theorem

From $p_X(x) \cdot p_{Y|X}(y \mid x) = p_Y(y) \cdot p_{X|Y}(x \mid y)$:

$$
p_{X|Y}(x \mid y) = \frac{p_{Y|X}(y \mid x)\,p_X(x)}{p_Y(y)}
$$

This is Bayes' theorem — a direct consequence of the two chain rule decompositions.

## Examples

**Example.** Urn with 3 red and 1 blue ball, draw 2 without replacement. $X_i = \mathbf{1}(\text{draw } i \text{ is blue})$.

Marginal of $X_1$: $P(X_1 = 1) = 1/4$, $P(X_1 = 0) = 3/4$.

Conditional of $X_2$ given $X_1$:

| | $P(X_2 = 0 \mid X_1)$ | $P(X_2 = 1 \mid X_1)$ |
|:---|:---:|:---:|
| $X_1 = 0$ | $2/3$ | $1/3$ |
| $X_1 = 1$ | $1$ | $0$ |

Joint via chain rule:

| | $X_1 = 0$ | $X_1 = 1$ |
|:---|:---:|:---:|
| $X_2 = 0$ | $(3/4)(2/3) = 1/2$ | $(1/4)(1) = 1/4$ |
| $X_2 = 1$ | $(3/4)(1/3) = 1/4$ | $(1/4)(0) = 0$ |

Sum $= 1/2 + 1/4 + 1/4 + 0 = 1$.

```python
# Recover joint from marginal + conditional
# 3 red, 1 blue, draw 2 without replacement
joint = {}
for x1 in [0, 1]:
    px1 = 1/4 if x1 == 1 else 3/4
    for x2 in [0, 1]:
        if x1 == 0:
            px2_given = 1/3 if x2 == 1 else 2/3
        else:
            px2_given = 0 if x2 == 1 else 1
        joint[(x1, x2)] = px1 * px2_given

for key in sorted(joint):
    print(f"P(X1={key[0]}, X2={key[1]}) = {joint[key]:.4f}")
print(f"Sum = {sum(joint.values()):.4f}")
```
