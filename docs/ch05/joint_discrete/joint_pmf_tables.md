# Joint PMF Tables and Visualization

## Joint PMF Table Format

A joint PMF for discrete random variables $(X, Y)$ is conveniently displayed as a table where:

- Columns correspond to values of $X$.
- Rows correspond to values of $Y$.
- Each cell contains $P(X = x_i, Y = y_j)$.
- All entries are non-negative and sum to 1.

## Worked Example

The joint PMF of $X$ and $Y$ is given by:

| | $x=0$ | $x=1$ | $x=2$ |
|---|---|---|---|
| $y=3$ | $1/10$ | $1/10$ | $1/10$ |
| $y=2$ | $1/10$ | $0$ | $1/10$ |
| $y=1$ | $0$ | $2/10$ | $1/10$ |
| $y=0$ | $1/10$ | $0$ | $1/10$ |

**Verification:** All 10 entries sum to $10/10 = 1$. ✓

## Adding Marginals to the Table

By summing rows and columns, we can augment the table with **marginal distributions** (covered in detail in Chapter 6):

| | $x=0$ | $x=1$ | $x=2$ | $P(Y=y_j)$ |
|---|---|---|---|---|
| $y=3$ | $1/10$ | $1/10$ | $1/10$ | $3/10$ |
| $y=2$ | $1/10$ | $0$ | $1/10$ | $2/10$ |
| $y=1$ | $0$ | $2/10$ | $1/10$ | $3/10$ |
| $y=0$ | $1/10$ | $0$ | $1/10$ | $2/10$ |
| $P(X=x_i)$ | $3/10$ | $3/10$ | $4/10$ | $1$ |

The row sums give the marginal PMF of $Y$, and the column sums give the marginal PMF of $X$.

## Visualization

Joint PMFs can be visualized as:

- **3D bar charts:** Height of bar at $(x_i, y_j)$ equals $p(x_i, y_j)$.
- **Heat maps:** Color intensity at $(x_i, y_j)$ represents $p(x_i, y_j)$.
- **Bubble plots:** Bubble size at $(x_i, y_j)$ is proportional to probability.

## Example: 3 Red Balls and 1 Blue Ball

There are 3 red balls and 1 blue ball in a bin. We draw two balls without replacement. Let:

$$X_i = \begin{cases} 1 & \text{if } i\text{-th ball is blue} \\ 0 & \text{otherwise} \end{cases}$$

Using the chain rule for joint probabilities:

$$P(X_1 = 0, X_2 = 1) = P(X_1 = 0) \cdot P(X_2 = 1 \mid X_1 = 0) = \frac{3}{4} \times \frac{1}{3} = \frac{1}{4}$$

This illustrates that the joint PMF can be computed from marginal and conditional probabilities using the **chain rule**: $p(x, y) = p(x) \cdot p(y|x)$.
