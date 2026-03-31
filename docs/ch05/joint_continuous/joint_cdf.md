# Joint CDF

## Definition

The **joint cumulative distribution function (joint CDF)** of a random vector $\mathbf{X} = (X_1, \ldots, X_d)$ is:

$$F(\mathbf{x}) = P(\mathbf{X} \le \mathbf{x}) = P(X_1 \le x_1, X_2 \le x_2, \ldots, X_d \le x_d)$$

Using the brick analogy:

$$F(\mathbf{x}) = \text{Weight of the bricks cumulatively stacked from } -\boldsymbol{\infty} \text{ up to } \mathbf{x}$$

## Joint CDF for Two Variables

For the bivariate case $(X, Y)$:

$$F(x, y) = P(X \le x, Y \le y)$$

### Discrete Case

$$F(x, y) = \sum_{x_i \le x} \sum_{y_j \le y} p(x_i, y_j)$$

### Continuous Case

$$F(x, y) = \int_{-\infty}^{x} \int_{-\infty}^{y} f(s, t) \, dt \, ds$$

## Properties

1. **Monotonicity:** $F$ is non-decreasing in each argument.
2. **Limits:**
    - $F(-\infty, y) = F(x, -\infty) = 0$
    - $F(\infty, \infty) = 1$
3. **Right-continuity:** $F$ is right-continuous in each argument.

## Recovering the Joint PDF

For continuous random variables:

$$f(x, y) = \frac{\partial^2}{\partial x \, \partial y} F(x, y)$$

## Computing Probabilities from the Joint CDF

$$P(a < X \le b, \, c < Y \le d) = F(b, d) - F(a, d) - F(b, c) + F(a, c)$$

This is the two-dimensional inclusion-exclusion formula applied to the rectangle $(a, b] \times (c, d]$.
