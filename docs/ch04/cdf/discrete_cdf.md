# CDF for Discrete Random Variables


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Formula

For a discrete random variable $X$ with PMF $p_{x_i} = P(X = x_i)$, the CDF is:

$$F(x) = P(X \le x) = \sum_{x_i \le x} p_{x_i}$$

This is a **step function** that jumps at each value $x_i$ by the amount $p_{x_i}$.

## Shape of Discrete CDFs

The CDF of a discrete random variable is a **right-continuous step function**:

- It is flat between consecutive values of $X$.
- It jumps upward at each value $x_i$ by exactly $P(X = x_i)$.
- It starts at 0 (for $x < \min\{x_i\}$) and approaches 1 as $x \to \infty$.

## Examples

### Bernoulli CDF

For $X \sim \text{B}(p)$:

$$F(x) = \begin{cases} 0 & x < 0 \\ 1-p & 0 \le x < 1 \\ 1 & x \ge 1 \end{cases}$$

### Binomial CDF

For $X \sim \text{B}(n, p)$:

$$F(k) = \sum_{i=0}^{k} \binom{n}{i} p^i (1-p)^{n-i}, \quad k = 0, 1, \ldots, n$$

### Geometric CDF

For $X \sim \text{Geo}(p)$:

$$F(k) = 1 - (1-p)^k, \quad k = 1, 2, 3, \ldots$$

## Recovering the PMF from the CDF

Given the CDF, recover the PMF via:

$$P(X = x_i) = F(x_i) - F(x_i^-)$$

where $F(x_i^-)$ is the left-hand limit at $x_i$.
