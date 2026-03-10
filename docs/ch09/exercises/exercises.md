# Chapter 9 Exercises

!!! warning "Exercise page"
    This page collects practice problems for Chapter 9 and does not follow the five-section structure used by concept pages.

Exercises on covariance, correlation, the Cauchy-Schwarz inequality, and variance of sums.

## Section 9.1 — Covariance

**Exercise 9.1.** Compute $\text{Cov}(X, Y)$ where $X$ and $Y$ have joint PMF: $P(0,0) = 0.1$, $P(0,1) = 0.2$, $P(1,0) = 0.3$, $P(1,1) = 0.4$.

**Exercise 9.2.** Let $X \sim \text{Uniform}(0,1)$ and $Y = X^2$. Compute $\text{Cov}(X, Y)$ and $\text{Corr}(X, Y)$.

**Exercise 9.3.** Prove the bilinearity property: $\text{Cov}(X + Y, Z) = \text{Cov}(X, Z) + \text{Cov}(Y, Z)$.

**Exercise 9.4.** Show that $\text{Cov}(X, Y) = 0$ does not imply independence by constructing an example with discrete $X$ and $Y$.

## Section 9.2 — Correlation and Cauchy-Schwarz

**Exercise 9.5.** If $Y = 3 - 2X$, find $\text{Corr}(X, Y)$ without computing any expectations.

**Exercise 9.6.** Prove the Cauchy-Schwarz inequality using the non-negative quadratic approach.

**Exercise 9.7.** Let $X$ and $Y$ be iid with $E[X] = 0$ and $\text{Var}(X) = 1$. Find $\text{Corr}(X + Y, X - Y)$.

## Section 9.3 — Variance of Sums

**Exercise 9.8.** Let $X_1, X_2, X_3$ be independent with $\text{Var}(X_i) = i^2$. Compute $\text{Var}(2X_1 - X_2 + 3X_3)$.

**Exercise 9.9.** Draw 10 cards from a 52-card deck without replacement. Find the variance of the number of hearts using the general formula with indicators.

**Exercise 9.10.** A portfolio has equal weights $a_i = 1/n$ for $n$ assets with common variance $\sigma^2$ and common pairwise correlation $\rho$. Show that the portfolio variance is $\sigma^2(\rho + (1-\rho)/n)$ and find its limit as $n \to \infty$.

**Exercise 9.11.** Let $S = X_1 + X_2 + \cdots + X_{100}$ where the $X_i$ are iid with mean 5 and variance 2. Compute $E[S]$, $\text{Var}(S)$, and $\text{SD}(S)$.
