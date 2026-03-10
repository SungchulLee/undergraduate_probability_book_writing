# Chapter 7 Exercises

!!! warning "Exercise page"
    This page collects practice problems for Chapter 7 and does not follow the five-section structure used by concept pages.

Exercises on expectation, variance, indicators, inequalities, and sums of random variables.

## Section 7.1 — Expectation

**Exercise 7.1.** Let $X$ be the number showing on a fair die. Compute $E[X]$, $E[X^2]$, and $E[2X + 3]$.

**Exercise 7.2.** Let $X$ have PMF $P(X = -1) = 0.3$, $P(X = 0) = 0.4$, $P(X = 2) = 0.3$. Compute $E[X]$ and $E[X^2]$.

**Exercise 7.3.** If $X \sim \text{Uniform}(a, b)$, use LOTUS to show $E[X^2] = (a^2 + ab + b^2)/3$.

**Exercise 7.4.** Use the tail sum formula to derive $E[X] = 1/p$ for $X \sim \text{Geo}(p)$.

## Section 7.2 — Indicators

**Exercise 7.5.** 100 people at a party each have a birthday uniform over 365 days. Use indicators to compute the expected number of pairs sharing a birthday.

**Exercise 7.6.** Throw 200 balls into 100 bins uniformly at random. Use indicators to compute the expected number of empty bins and its variance.

**Exercise 7.7.** 20 people enter an elevator at the ground floor. Each independently selects one of 10 floors. Find the expected number of stops and its variance.

## Section 7.3 — Variance

**Exercise 7.8.** If $E[X] = 3$ and $E[X^2] = 13$, compute $\text{Var}(X)$.

**Exercise 7.9.** Compute the variance of $X$ with $P(X = -2) = 1/4$, $P(X = 0) = 1/2$, $P(X = 3) = 1/4$.

**Exercise 7.10.** Show that $E[(X-c)^2]$ is minimized when $c = E[X]$ and the minimum value is $\text{Var}(X)$.

## Section 7.4 — Inequalities

**Exercise 7.11.** If $X \ge 0$ with $E[X] = 5$, find an upper bound for $P(X \ge 20)$ using Markov's inequality.

**Exercise 7.12.** If $E[X] = 10$ and $\text{Var}(X) = 4$, use Chebyshev's inequality to bound $P(|X - 10| \ge 6)$.

**Exercise 7.13.** Use Jensen's inequality to show that $E[1/X] \ge 1/E[X]$ for $X > 0$.

## Section 7.5 — Sums and Decomposition

**Exercise 7.14.** Let $X_1, \ldots, X_{100}$ be iid with $E[X_i] = 2$ and $\text{Var}(X_i) = 9$. Compute $E[\sum X_i]$ and $\text{Var}(\sum X_i)$.

**Exercise 7.15.** Let $S = 3X_1 - 2X_2 + X_3$ where $X_1, X_2, X_3$ are independent with means 1, 2, 3 and variances 4, 1, 9. Compute $E[S]$ and $\text{Var}(S)$.

**Exercise 7.16.** A portfolio has weights $\mathbf{a} = (0.5, 0.3, 0.2)$ and covariance matrix

$$
\boldsymbol{\Sigma} = \begin{pmatrix} 0.04 & 0.01 & 0.02 \\ 0.01 & 0.09 & 0.03 \\ 0.02 & 0.03 & 0.16 \end{pmatrix}
$$

Compute the portfolio variance $\mathbf{a}^T\boldsymbol{\Sigma}\,\mathbf{a}$.

**Exercise 7.17.** There are 50 types of collectible cards. How many packs do you expect to buy to complete the collection? What is the standard deviation?

**Exercise 7.18.** Show that dividing by $n$ instead of $n-1$ in the sample variance formula gives a biased estimator, and compute the bias.
