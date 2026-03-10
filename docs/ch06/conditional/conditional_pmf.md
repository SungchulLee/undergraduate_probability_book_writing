# Conditional PMF


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

The **conditional PMF** of $X$ given $Y = y$ is:

$$p(x \mid y) = P(X = x \mid Y = y) = \frac{p(x, y)}{p_Y(y)}$$

provided $P(Y = y) > 0$. Similarly:

$$p(y \mid x) = P(Y = y \mid X = x) = \frac{p(x, y)}{p_X(x)}$$

## Interpretation: Slice and Normalize

The conditional PMF is obtained by a two-step procedure:

1. **Slice:** Restrict attention to the row (or column) of the joint PMF table corresponding to the given value.
2. **Normalize:** Divide all entries in that slice by their sum so that the conditional probabilities add to 1.

This is equivalent to "removing all masses except those on the line $Y = y$, then rescaling so the remaining masses sum to 1."

## Worked Example

From the joint PMF:

| | $x=0$ | $x=1$ | $x=2$ |
|---|---|---|---|
| $y=3$ | $1/10$ | $1/10$ | $1/10$ |
| $y=2$ | $1/10$ | $0$ | $1/10$ |
| $y=1$ | $0$ | $2/10$ | $1/10$ |
| $y=0$ | $1/10$ | $0$ | $1/10$ |

### Conditional PMF of X given Y = 1

The $y=1$ row has entries: $0, \, 2/10, \, 1/10$. The row sum is $P(Y=1) = 3/10$.

$$P(X = 0 \mid Y = 1) = \frac{0}{3/10} = 0$$

$$P(X = 1 \mid Y = 1) = \frac{2/10}{3/10} = \frac{2}{3}$$

$$P(X = 2 \mid Y = 1) = \frac{1/10}{3/10} = \frac{1}{3}$$

**Verification:** $0 + 2/3 + 1/3 = 1$ ✓

### Conditional PMF of Y given X = 2

The $x=2$ column has entries: $1/10, \, 1/10, \, 1/10, \, 1/10$. The column sum is $P(X=2) = 4/10$.

$$P(Y = 0 \mid X = 2) = \frac{1/10}{4/10} = \frac{1}{4}$$

$$P(Y = 1 \mid X = 2) = \frac{1/10}{4/10} = \frac{1}{4}$$

$$P(Y = 2 \mid X = 2) = \frac{1/10}{4/10} = \frac{1}{4}$$

$$P(Y = 3 \mid X = 2) = \frac{1/10}{4/10} = \frac{1}{4}$$

Given $X = 2$, the variable $Y$ is uniformly distributed over $\{0, 1, 2, 3\}$.

## Connection to Independence

If $X$ and $Y$ are independent, then $p(x \mid y) = p_X(x)$ — the conditional PMF equals the marginal PMF, meaning knowing $Y$ provides no information about $X$.
