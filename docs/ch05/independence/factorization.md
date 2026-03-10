# Verifying Independence via Factorization


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## The Factorization Test

To verify whether $X$ and $Y$ are independent, check whether the joint PMF (or PDF) factors into the product of the marginals for **every** pair of values:

$$p(x, y) = p_X(x) \cdot p_Y(y) \quad \text{for all } x, y$$

If even **one** pair $(x, y)$ violates this equation, then $X$ and $Y$ are dependent.

## Example: Two Independent Random Variables

The marginal PMFs of $X$ and $Y$ are:

| $P(X = x_i)$ | $x=0$ | $x=1$ | $x=2$ |
|---|---|---|---|
| | $2/10$ | $3/10$ | $5/10$ |

| $P(Y = y_j)$ | $y=0$ | $y=1$ | $y=2$ | $y=3$ |
|---|---|---|---|---|
| | $2/10$ | $3/10$ | $2/10$ | $3/10$ |

If $X$ and $Y$ are independent, the joint PMF is determined by multiplying marginals:

| | $x=0$ | $x=1$ | $x=2$ |
|---|---|---|---|
| $y=3$ | $\frac{2}{10} \times \frac{3}{10} = \frac{6}{100}$ | $\frac{3}{10} \times \frac{3}{10} = \frac{9}{100}$ | $\frac{5}{10} \times \frac{3}{10} = \frac{15}{100}$ |
| $y=2$ | $\frac{2}{10} \times \frac{2}{10} = \frac{4}{100}$ | $\frac{3}{10} \times \frac{2}{10} = \frac{6}{100}$ | $\frac{5}{10} \times \frac{2}{10} = \frac{10}{100}$ |
| $y=1$ | $\frac{2}{10} \times \frac{3}{10} = \frac{6}{100}$ | $\frac{3}{10} \times \frac{3}{10} = \frac{9}{100}$ | $\frac{5}{10} \times \frac{3}{10} = \frac{15}{100}$ |
| $y=0$ | $\frac{2}{10} \times \frac{2}{10} = \frac{4}{100}$ | $\frac{3}{10} \times \frac{2}{10} = \frac{6}{100}$ | $\frac{5}{10} \times \frac{2}{10} = \frac{10}{100}$ |

When $X$ and $Y$ are independent, the joint PMF is **fully determined** by the two marginals.

## Example: Two Dependent Random Variables

The joint PMF of $X$ and $Y$ is:

| | $x=0$ | $x=1$ | $x=2$ |
|---|---|---|---|
| $y=3$ | $1/6$ | $1/6$ | $1/6$ |
| $y=2$ | $1/6$ | $1/6$ | $0$ |
| $y=1$ | $1/6$ | $0$ | $0$ |
| $y=0$ | $0$ | $0$ | $0$ |

**Method 1: Check conditional distributions.**

- Conditional PMF of $X$ given $Y = 1$: $P(X=0 \mid Y=1) = 1$
- Conditional PMF of $X$ given $Y = 2$: $P(X=0 \mid Y=2) = 1/2$, $P(X=1 \mid Y=2) = 1/2$
- Conditional PMF of $X$ given $Y = 3$: $P(X=0 \mid Y=3) = 1/3$, $P(X=1 \mid Y=3) = 1/3$, $P(X=2 \mid Y=3) = 1/3$

Since the conditional distribution of $X$ given $Y = y_j$ **depends on** $y_j$, the variables are **dependent**.

**Method 2: Check conditional distributions in the other direction.**

- Conditional PMF of $Y$ given $X = 0$: $P(Y=1 \mid X=0) = 1/3$, $P(Y=2 \mid X=0) = 1/3$, $P(Y=3 \mid X=0) = 1/3$
- Conditional PMF of $Y$ given $X = 1$: $P(Y=2 \mid X=1) = 1/2$, $P(Y=3 \mid X=1) = 1/2$
- Conditional PMF of $Y$ given $X = 2$: $P(Y=3 \mid X=2) = 1$

The conditional distribution of $Y$ given $X = x_i$ depends on $x_i$, confirming dependence.

## Quick Independence Check

A practical shortcut: if **any zero** appears in the interior of the joint PMF table (while the corresponding marginals are non-zero), then $X$ and $Y$ cannot be independent.
