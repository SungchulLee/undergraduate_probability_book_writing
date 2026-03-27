# Distribution of g(X)

## Motivation

Once we know the distribution of a random variable $X$, we often need the
distribution of a transformed variable $Y = g(X)$ for some function
$g : \mathbb{R} \to \mathbb{R}$. For example, if $X$ is a temperature in
Celsius, then $Y = 1.8X + 32$ is the same temperature in Fahrenheit. If $X$ is
a stock return, then $Y = X^2$ measures squared deviation. The question is
always the same: given the distribution of $X$ and the function $g$, what is
the distribution of $Y$?

## Functions of a Random Variable

If $X$ is a random variable and $g : \mathbb{R} \to \mathbb{R}$ is a function,
then $Y = g(X)$ is also a random variable. For every outcome $\omega$,

$$
Y(\omega) = g(X(\omega))
$$

The distribution of $Y$ is completely determined by the distribution of $X$ and
the function $g$. No additional information about the sample space is needed.

## Discrete Case

When $X$ is discrete, the idea is simple: group all values of $X$ that map to
the same value of $Y$ and sum their probabilities.

!!! info "PMF of g(X) --- Discrete Case"
    If $X$ is discrete with PMF $p_X(x)$ and $Y = g(X)$, then

    $$
    P(Y = y) = \sum_{x :\, g(x) = y} P(X = x)
    $$

    That is, collect all values of $X$ that map to $y$ under $g$ and add their
    probabilities.

## Example: Generating a Symmetric Random Variable from Bernoulli

Let $X \sim \text{B}(p)$ (Bernoulli) and define $Y = 2X - 1$. Then

$$
Y = \begin{cases} 1 & \text{with probability } p \\ -1 & \text{with probability } 1 - p \end{cases}
$$

When $p = 1/2$, this produces a symmetric $\pm 1$ random variable. If we flip a
fair coin $n$ times independently, recording each flip as $X_i \in \{0, 1\}$,
and set $Y_i = 2X_i - 1$, then

$$
Y_i \stackrel{\text{iid}}{\sim} \begin{cases} +1 & \text{prob } 0.5 \\ -1 & \text{prob } 0.5 \end{cases}
$$

This transformation is fundamental in random walk models and financial
applications.

## Example: Squaring a Die Roll

Roll a fair die and let $X$ be the outcome. Define $Y = (X - 3.5)^2$, the
squared deviation from the mean. Since $X$ takes values $1, 2, \ldots, 6$ each
with probability $1/6$:

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $y = (x - 3.5)^2$ | 6.25 | 2.25 | 0.25 | 0.25 | 2.25 | 6.25 |

Grouping by $y$ values:

| $y$ | 0.25 | 2.25 | 6.25 |
|:---:|:---:|:---:|:---:|
| $P(Y = y)$ | $2/6$ | $2/6$ | $2/6$ |

The function $g$ is not one-to-one, so six values of $X$ collapse into three
values of $Y$.

## Continuous Case (Preview)

For continuous random variables, finding the distribution of $g(X)$ requires
the **CDF method** or the **change-of-variables formula**, which involves the
Jacobian of the transformation. These techniques are introduced in the following
pages for simple cases and developed fully in Chapter 15.

!!! tip "General Strategy"
    Regardless of whether $X$ is discrete or continuous, the starting point is
    always the same: express $\{Y \le y\}$ or $\{Y = y\}$ in terms of $X$ and
    use the known distribution of $X$ to compute the probability.
