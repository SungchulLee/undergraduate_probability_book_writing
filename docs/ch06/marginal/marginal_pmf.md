# Marginal PMF from Joint PMF

## Definition

Given the joint PMF $p(x, y) = P(X = x, Y = y)$, the **marginal PMF** of $X$ is obtained by summing over all values of $Y$:

$$p_X(x) = P(X = x) = \sum_y p(x, y)$$

Similarly, the marginal PMF of $Y$ is:

$$p_Y(y) = P(Y = y) = \sum_x p(x, y)$$

## Interpretation

Marginalization "collapses" the joint distribution onto one variable by integrating out (summing over) the other. In the joint PMF table, the marginal of $X$ is obtained by computing **column sums**, and the marginal of $Y$ by computing **row sums**.

## Worked Example

The joint PMF of $X$ and $Y$ is:

| | $x=0$ | $x=1$ | $x=2$ |
|---|---|---|---|
| $y=3$ | $1/10$ | $1/10$ | $1/10$ |
| $y=2$ | $1/10$ | $0$ | $1/10$ |
| $y=1$ | $0$ | $2/10$ | $1/10$ |
| $y=0$ | $1/10$ | $0$ | $1/10$ |

**Marginal PMF of $X$ (column sums):**

$$P(X = 0) = \frac{1}{10} + \frac{1}{10} + 0 + \frac{1}{10} = \frac{3}{10}$$

$$P(X = 1) = \frac{1}{10} + 0 + \frac{2}{10} + 0 = \frac{3}{10}$$

$$P(X = 2) = \frac{1}{10} + \frac{1}{10} + \frac{1}{10} + \frac{1}{10} = \frac{4}{10}$$

**Marginal PMF of $Y$ (row sums):**

$$P(Y = 0) = \frac{1}{10} + 0 + \frac{1}{10} = \frac{2}{10}$$

$$P(Y = 1) = 0 + \frac{2}{10} + \frac{1}{10} = \frac{3}{10}$$

$$P(Y = 2) = \frac{1}{10} + 0 + \frac{1}{10} = \frac{2}{10}$$

$$P(Y = 3) = \frac{1}{10} + \frac{1}{10} + \frac{1}{10} = \frac{3}{10}$$

## Augmented Joint PMF Table

| | $x=0$ | $x=1$ | $x=2$ | $P(Y=y_j)$ |
|---|---|---|---|---|
| $y=3$ | $1/10$ | $1/10$ | $1/10$ | $3/10$ |
| $y=2$ | $1/10$ | $0$ | $1/10$ | $2/10$ |
| $y=1$ | $0$ | $2/10$ | $1/10$ | $3/10$ |
| $y=0$ | $1/10$ | $0$ | $1/10$ | $2/10$ |
| $P(X=x_i)$ | $3/10$ | $3/10$ | $4/10$ | $1$ |

The bottom row contains the marginal of $X$, and the right column contains the marginal of $Y$. These are sometimes called the "margins" of the table, which is where the name "marginal distribution" comes from.

## Coin Flip Example

For $X$ = number of heads in first two flips and $Y$ = total heads in three fair coin flips:

**From joint to marginal of $X$:** Summing over $Y$ values in each column of the joint PMF table, we obtain $P(X = 0) = 2/8 = 1/4$, $P(X = 1) = 4/8 = 1/2$, $P(X = 2) = 2/8 = 1/4$, which is the $\text{B}(2, 1/2)$ distribution as expected.
