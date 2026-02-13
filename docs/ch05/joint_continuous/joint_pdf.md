# Joint PDF

## Definition

For continuous random variables $(X, Y)$, the **joint probability density function (joint PDF)** is a function $f(x, y)$ such that:

$$P((X, Y) \in A) = \iint_A f(x, y) \, dx \, dy$$

Using the brick analogy:

$$f(x, y) \, dx \, dy = \text{Weight of the bricks in } [x, x+dx] \times [y, y+dy]$$

## Properties

A valid joint PDF satisfies:

1. **Non-negativity:** $f(x, y) \ge 0$ for all $(x, y)$.
2. **Normalization:** $\displaystyle\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \, dx \, dy = 1$.

## Computing Probabilities

For a rectangular region:

$$P(a \le X \le b, \, c \le Y \le d) = \int_a^b \int_c^d f(x, y) \, dy \, dx$$

For a general region $A$:

$$P((X, Y) \in A) = \iint_A f(x, y) \, dx \, dy$$

## Example: Uniform on the Unit Square

Let $(X, Y)$ be uniformly distributed on $[0,1]^2$:

$$f(x, y) = \begin{cases} 1 & 0 \le x \le 1, \, 0 \le y \le 1 \\ 0 & \text{otherwise} \end{cases}$$

Then $P(X \le 1/2, Y \le 1/2) = \int_0^{1/2} \int_0^{1/2} 1 \, dy \, dx = 1/4$.

## Extension to Higher Dimensions

For a random vector $\mathbf{X} = (X_1, \ldots, X_d)$ in $\mathbb{R}^d$:

$$f(\mathbf{x}) \, d\mathbf{x} = \text{Weight of the bricks in } \prod_{i=1}^d [x_i, x_i + dx_i]$$

$$P(\mathbf{X} \in A) = \int \cdots \int_A f(x_1, \ldots, x_d) \, dx_1 \cdots dx_d$$
