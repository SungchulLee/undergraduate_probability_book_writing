# Joint PMF Tables and Marginals

A joint PMF table organizes the probabilities of $(X, Y)$ into a grid, with marginal distributions appearing as row and column sums.

## Definition

A **joint PMF table** has:

- Columns indexed by values of $X$
- Rows indexed by values of $Y$
- Cell $(x_i, y_j)$ contains $p_{X,Y}(x_i, y_j) = P(X = x_i, Y = y_j)$

The **marginal PMFs** are obtained by summing:

$$
p_X(x) = \sum_y p_{X,Y}(x, y), \qquad p_Y(y) = \sum_x p_{X,Y}(x, y)
$$

## Explanation

### Reading the Table

- Any probability about $(X, Y)$ is computed by summing the relevant cells
- Row sums give the marginal PMF of $Y$
- Column sums give the marginal PMF of $X$
- The grand total (sum of all cells) must equal 1

### Chain Rule Construction

When the joint PMF is not given directly, build it using the chain rule:

$$
p_{X,Y}(x, y) = p_X(x) \cdot p_{Y|X}(y \mid x)
$$

This is especially useful for sequential experiments (drawing without replacement, multistage sampling).

### Visualization

- **3D bar chart:** height at $(x, y)$ equals the joint probability
- **Heat map:** color intensity represents probability
- **Bubble plot:** bubble area is proportional to probability

## Examples

**Example 1.** Joint PMF table with marginals.

| | $x=0$ | $x=1$ | $x=2$ | $p_Y(y)$ |
|:---|:---:|:---:|:---:|:---:|
| $y=3$ | $1/10$ | $1/10$ | $1/10$ | $3/10$ |
| $y=2$ | $1/10$ | $0$ | $1/10$ | $2/10$ |
| $y=1$ | $0$ | $2/10$ | $1/10$ | $3/10$ |
| $y=0$ | $1/10$ | $0$ | $1/10$ | $2/10$ |
| $p_X(x)$ | $3/10$ | $3/10$ | $4/10$ | $1$ |

$P(X \ge 1, Y \le 1) = p(1,1) + p(1,0) + p(2,1) + p(2,0) = 2/10 + 0 + 1/10 + 1/10 = 4/10$.

**Example 2.** Urn with 3 red and 1 blue ball, draw 2 without replacement. Let $X_i = 1$ if draw $i$ is blue.

Using the chain rule:

$$
P(X_1 = 0, X_2 = 1) = P(X_1 = 0) \cdot P(X_2 = 1 \mid X_1 = 0) = \frac{3}{4} \cdot \frac{1}{3} = \frac{1}{4}
$$

| | $X_1=0$ | $X_1=1$ | $p_{X_2}$ |
|:---|:---:|:---:|:---:|
| $X_2=0$ | $1/2$ | $1/4$ | $3/4$ |
| $X_2=1$ | $1/4$ | $0$ | $1/4$ |
| $p_{X_1}$ | $3/4$ | $1/4$ | $1$ |

Note: $P(X_1=1, X_2=1) = 0$ because there is only one blue ball.

```python
# Build the urn example via chain rule
# 3 red, 1 blue, draw 2 without replacement
table = {}
for x1 in [0, 1]:
    for x2 in [0, 1]:
        if x1 == 0:
            p_x1 = 3/4
            p_x2_given = (2/3 if x2 == 0 else 1/3)
        else:
            p_x1 = 1/4
            p_x2_given = (1.0 if x2 == 0 else 0.0)
        table[(x1, x2)] = p_x1 * p_x2_given

for (x1, x2), p in sorted(table.items()):
    print(f"P(X1={x1}, X2={x2}) = {p:.4f}")
print(f"Total = {sum(table.values()):.4f}")
```
