# Discrete vs Continuous Random Variables

## Discrete Random Variables

A random variable $X$ is **discrete** if it takes values in a countable set $\{x_1, x_2, x_3, \ldots\}$. Its distribution is fully described by the probability mass function (PMF):

$$
P(X = x_i) = p(x_i)
$$

Each value $x_i$ carries a positive "brick" of probability mass, and these masses sum to 1:

$$
\sum_{i} p(x_i) = 1
$$

!!! example "Examples of Discrete Random Variables"
    - Number of heads in $n$ coin flips (Binomial)
    - Number of flips until first head (Geometric)
    - Number of defective items in a sample (Hypergeometric)
    - Number of typos on a page (Poisson)

## Continuous Random Variables

A random variable $X$ is **continuous** if its CDF $F(x) = P(X \le x)$ is a continuous function. Equivalently, $P(X = a) = 0$ for every individual value $a$. The distribution is described by a probability density function (PDF) $f(x)$ satisfying

$$
P(X \in A) = \int_A f(x) \, dx
$$

for every measurable set $A \subseteq \mathbb{R}$. In particular, the CDF and PDF are related by

$$
F(x) = \int_{-\infty}^{x} f(t) \, dt, \qquad f(x) = F'(x) \text{ wherever } F \text{ is differentiable}
$$

For continuous random variables, probability is spread smoothly---no single point carries positive mass.

!!! example "Examples of Continuous Random Variables"
    - Uniform on $[0,1]$
    - Standard normal $N(0,1)$
    - Exponential waiting time $\text{Exp}(\lambda)$
    - Gamma distribution $\text{Gamma}(\alpha, \beta)$

## Key Distinction

| Property | Discrete | Continuous |
|----------|----------|------------|
| Values | Countable set | Uncountable (interval) |
| Point probability | $P(X = a) > 0$ possible | $P(X = a) = 0$ always |
| Described by | PMF $p(x_i)$ | PDF $f(x)$ |
| Summation vs integration | $\sum$ | $\int$ |
| CDF behavior | Step function | Continuous function |

!!! warning "Density Is Not Probability"
    For a continuous random variable, $f(x)$ is a **density**, not a probability. It is possible for $f(x) > 1$ at some points. Only the integral of $f$ over an interval gives a probability.
