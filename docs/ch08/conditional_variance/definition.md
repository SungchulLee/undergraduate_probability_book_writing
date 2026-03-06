# Conditional Variance Definition

## Var(X | Y = y) as a Number

The **conditional variance of $X$ given $Y = y$** measures the spread of $X$ around its conditional mean $E(X \mid Y = y)$, computed using the conditional distribution of $X$ given $Y = y$.

$$

\text{Var}(X \mid Y = y) = E\bigl[(X - E(X \mid Y = y))^2 \mid Y = y\bigr]

$$

As with unconditional variance, there is a **shortcut formula**:

$$

\text{Var}(X \mid Y = y) = E(X^2 \mid Y = y) - \bigl(E(X \mid Y = y)\bigr)^2

$$

This follows by expanding the square in the definition and using linearity of conditional expectation.

## Var(X | Y) as a Random Variable

Just as $E(X \mid Y)$ is a random variable obtained by letting $y$ vary, $\text{Var}(X \mid Y)$ is also a random variable:

$$

\omega \;\longrightarrow\; y = Y(\omega) \;\longrightarrow\; P(X = x \mid Y = y) \;\longrightarrow\; \text{Var}(X \mid Y = y)

$$

Formally:

$$

\text{Var}(X \mid Y)(\omega) = \text{Var}(X \mid Y = Y(\omega))

$$

## Example: Joint PDF

For the joint PDF $f(x, y) = \frac{e^{-x/y} e^{-y}}{y}$, we found $X \mid Y = y \sim \text{Exp}(1/y)$. The variance of an exponential with rate $\lambda = 1/y$ is $1/\lambda^2 = y^2$, so:

$$

\text{Var}(X \mid Y = y) = y^2 \implies \text{Var}(X \mid Y) = Y^2

$$

## Interpretation

$\text{Var}(X \mid Y = y)$ measures the **residual uncertainty** in $X$ after learning that $Y = y$. If knowing $Y$ determines $X$ exactly, then $\text{Var}(X \mid Y) = 0$. If knowing $Y$ provides no information about $X$ (independence), then $\text{Var}(X \mid Y) = \text{Var}(X)$.
