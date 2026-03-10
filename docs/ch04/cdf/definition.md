# CDF Definition and Properties


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

The **cumulative distribution function (CDF)** of a random variable $X$ is:

$$F(x) = P(X \le x)$$

Using the brick analogy:

$$F(x) = \text{Weight of the bricks cumulatively stacked from } -\infty \text{ up to } x$$

## Properties of the CDF

Every CDF satisfies:

1. **Non-decreasing:** If $a < b$, then $F(a) \le F(b)$.
2. **Right-continuous:** $\displaystyle\lim_{x \to a^+} F(x) = F(a)$ for all $a$.
3. **Limits at infinity:**
    - $\displaystyle\lim_{x \to -\infty} F(x) = 0$
    - $\displaystyle\lim_{x \to +\infty} F(x) = 1$

## Computing Probabilities from the CDF

$$P(a < X \le b) = F(b) - F(a)$$

$$P(X > a) = 1 - F(a)$$

$$P(X = a) = F(a) - F(a^-) = \text{size of jump at } a$$

where $F(a^-) = \lim_{x \to a^-} F(x)$ is the left-hand limit.

## Example: Reading a CDF

Consider a discrete CDF with jumps at $x = 5, 7, 10, 20, 25, 30$.

From the graph:

$$P(X = 5) = F(5) - F(5^-) = 0.2 - 0 = 0.2$$

$$P(X < 20) = F(20^-) = 0.6 \implies P(X \ge 20) = 1 - P(X < 20) = 0.4$$

!!! tip "Key Insight"
    For discrete random variables, $P(X = a)$ equals the **jump size** of the CDF at $a$. If there is no jump at $a$, then $P(X = a) = 0$.
