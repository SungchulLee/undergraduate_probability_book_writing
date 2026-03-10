# Chapter 6 Exercises

!!! warning "Exercise page"
    This page collects practice problems for Chapter 6 and does not follow the five-section structure used by concept pages.

Exercises on marginal distributions, conditional distributions, and the chain rule.

## Section 6.1 — Marginal Distributions

**Exercise 6.1.** The joint PMF of $X$ and $Y$ is given by:

| | $x=0$ | $x=1$ | $x=2$ |
|:---|:---:|:---:|:---:|
| $y=2$ | $0.1$ | $0.15$ | $0.05$ |
| $y=1$ | $0.2$ | $0.1$ | $0.15$ |
| $y=0$ | $0.05$ | $0.1$ | $0.1$ |

Find the marginal PMFs of $X$ and $Y$.

**Exercise 6.2.** Let $(X, Y)$ have joint PDF $f(x, y) = 6(1-y)$ for $0 \le x \le y \le 1$. Find the marginal PDFs of $X$ and $Y$.

## Section 6.2 — Conditional Distributions

**Exercise 6.3.** Using the joint PMF from Exercise 6.1, find:

(a) The conditional PMF of $Y$ given $X = 1$.

(b) The conditional PMF of $X$ given $Y = 2$.

(c) $P(Y \ge 1 \mid X = 0)$.

**Exercise 6.4.** A box has 5 red and 3 blue balls. Two balls are drawn without replacement. Let $X_1$ = number of red balls in the first draw, $X_2$ = number of red balls in the second draw. Find $P(X_1 = 1, X_2 = 1)$ using the chain rule.

## Section 6.3 — Relationships

**Exercise 6.5.** Suppose $P(X = x) = 1/3$ for $x \in \{0, 1, 2\}$ and the conditional distribution of $Y$ given $X = x$ is $\text{Bin}(x, 0.5)$. Reconstruct the joint PMF of $(X, Y)$.

**Exercise 6.6.** From the joint PMF of $(X, Y)$:

| | $x=1$ | $x=2$ | $x=3$ |
|:---|:---:|:---:|:---:|
| $y=1$ | $1/12$ | $1/6$ | $1/12$ |
| $y=2$ | $1/6$ | $1/6$ | $1/6$ |
| $y=3$ | $1/12$ | $0$ | $1/12$ |

(a) Find all marginal and conditional distributions.

(b) Determine whether $X$ and $Y$ are independent.

(c) Verify the chain rule $p(x, y) = p(x) \cdot p(y \mid x)$ for $(x, y) = (2, 1)$.

**Exercise 6.7.** Can two different joint distributions have the same pair of marginal distributions? Provide an example or prove impossibility.

**Exercise 6.8.** Let $(X, Y)$ have joint PDF $f(x, y) = e^{-y}$ for $0 \le x \le y < \infty$. Find the conditional PDF $f_{X|Y}(x \mid y)$ and identify the distribution.
