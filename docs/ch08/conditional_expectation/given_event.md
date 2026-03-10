# Conditional Expectation Given an Event


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

The **conditional expectation of $X$ given the event $Y = y$** is a number obtained by computing the expectation of $X$ using the conditional distribution of $X$ given $Y = y$.

### Discrete Case

$$
E(X \mid Y = y) = \sum_{x_i} x_i \, P(X = x_i \mid Y = y)
$$

This mirrors the unconditional expectation $E(X) = \sum_{x_i} x_i \, P(X = x_i)$, but with conditional probabilities replacing unconditional ones.

### Continuous Case

$$
E(X \mid Y = y) = \int_{-\infty}^{\infty} x \, f_{X|Y}(x \mid y) \, dx
$$

Again, this mirrors $E(X) = \int_{-\infty}^{\infty} x \, f_X(x) \, dx$, with the conditional density $f_{X|Y}(x \mid y)$ replacing the marginal density $f_X(x)$.

## Key Point

$E(X \mid Y = y)$ is a **number**, not a random variable. For each specific value $y$, we get a specific numerical answer. Different values of $y$ generally produce different numbers.

## Example: Joint PDF

Consider random variables $X$ and $Y$ with joint PDF:

$$
f(x, y) = \frac{e^{-x/y} \, e^{-y}}{y}, \quad 0 < x < \infty, \quad 0 < y < \infty
$$

To find $E(X \mid Y = y)$, first identify the conditional distribution. The conditional density of $X$ given $Y = y$ is:

$$
f_{X|Y}(x \mid y) \propto \frac{e^{-x/y} \, e^{-y}}{y} \propto \frac{1}{y} e^{-x/y}
$$

This is the density of an $\text{Exp}(\lambda)$ distribution with rate $\lambda = 1/y$. Therefore:

$$
E(X \mid Y = y) = \frac{1}{\lambda} = y
$$

$$
\text{Var}(X \mid Y = y) = \frac{1}{\lambda^2} = y^2
$$

## Conditional Expectation of Functions

By analogy with LOTUS, for any function $g$:

$$
E(g(X) \mid Y = y) = \sum_{x_i} g(x_i) \, P(X = x_i \mid Y = y) \quad \text{(discrete)}
$$

$$
E(g(X) \mid Y = y) = \int_{-\infty}^{\infty} g(x) \, f_{X|Y}(x \mid y) \, dx \quad \text{(continuous)}
$$
