# Conditional Expectation Given a Random Variable


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## From Numbers to Random Variables

While $E(X \mid Y = y)$ is a number for each fixed $y$, we can define $E(X \mid Y)$ as a **random variable** by letting $y$ vary over all possible values of $Y$.

The key idea is that as the outcome $\omega$ determines $Y(\omega) = y$, which in turn determines $P(X = x \mid Y = y)$, which in turn determines $E(X \mid Y = y)$:

$$
\omega \;\longrightarrow\; y = Y(\omega) \;\longrightarrow\; P(X = x \mid Y = y) \;\longrightarrow\; E(X \mid Y = y)
$$

Formally:

$$
E(X \mid Y)(\omega) = E(X \mid Y = Y(\omega))
$$

## E(X | Y) as a Function of Y

$E(X \mid Y)$ is a function of the random variable $Y$. If we define $g(y) = E(X \mid Y = y)$, then:

$$
E(X \mid Y) = g(Y)
$$

Since $g(Y)$ is a function of a random variable, $E(X \mid Y)$ is itself a random variable. It inherits its randomness entirely from $Y$.

## Discrete Representation

When $Y$ takes values $y_1, y_2, \ldots, y_n$, the random variable $E(X \mid Y)$ can be written explicitly:

$$
E(X \mid Y) = \begin{cases}
E(X \mid Y = y_1) & \text{if } Y = y_1, \text{ with probability } P(Y = y_1) \\
E(X \mid Y = y_2) & \text{if } Y = y_2, \text{ with probability } P(Y = y_2) \\
\vdots & \vdots \\
E(X \mid Y = y_n) & \text{if } Y = y_n, \text{ with probability } P(Y = y_n)
\end{cases}
$$

## Example: Joint PDF (Continued)

From the joint PDF example where $f(x, y) = \frac{e^{-x/y} e^{-y}}{y}$, we found $E(X \mid Y = y) = y$. Therefore:

$$
E(X \mid Y) = Y
$$

$$
\text{Var}(X \mid Y) = Y^2
$$

Here $E(X \mid Y) = Y$ is a random variable — it takes whatever value $Y$ happens to take.
