# Discrete vs Continuous Random Variables


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Discrete Random Variables

A random variable $X$ is **discrete** if it takes values in a countable set $\{x_1, x_2, x_3, \ldots\}$. Its distribution is fully described by the probability mass function (PMF):

$$p_{x_i} = P(X = x_i)$$

Each value $x_i$ carries a positive "brick" of probability mass, and these masses sum to 1:

$$\sum_i p_{x_i} = 1$$

**Examples of discrete random variables:**

- Number of heads in $n$ coin flips (Binomial)
- Number of flips until first head (Geometric)
- Number of defective items in a sample (Hypergeometric)

## Continuous Random Variables

A random variable $X$ is **continuous** if its CDF $F(x) = P(X \le x)$ is a continuous function. Equivalently, $P(X = a) = 0$ for every individual value $a$. The distribution is described by a probability density function (PDF) $f(x)$ such that:

$$P(X \in A) = \int_A f(x) \, dx$$

For continuous random variables, probability is spread smoothly — no single point carries positive mass.

**Examples of continuous random variables:**

- Uniform on $[0,1]$
- Standard Normal
- Exponential waiting time

## Key Distinction

| Property | Discrete | Continuous |
|----------|----------|------------|
| Values | Countable set | Uncountable (interval) |
| Point probability | $P(X = a) > 0$ possible | $P(X = a) = 0$ always |
| Described by | PMF $p_{x_i}$ | PDF $f(x)$ |
| Summation vs Integration | $\sum$ | $\int$ |
| CDF behavior | Step function | Continuous function |
