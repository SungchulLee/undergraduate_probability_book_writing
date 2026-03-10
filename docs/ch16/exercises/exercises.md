# Chapter 16 Exercises

!!! warning "Exercise page"
    This page collects practice problems for Chapter 16 and does not follow the five-section structure used by concept pages.

Exercises on convolution: discrete and continuous convolution formulas, sums of standard distributions, and the Irwin-Hall distribution.

## Section 16.1 — Discrete Convolution

**Exercise 16.1.** Compute the PMF of $X + Y$ where $X \sim \operatorname{Bin}(3, 1/2)$ and $Y \sim \operatorname{Bin}(2, 1/2)$ are independent, using the convolution formula. Verify that the result is $\operatorname{Bin}(5, 1/2)$.

**Exercise 16.2.** Let $X$ and $Y$ be independent with $P(X = k) = 1/3$ for $k \in \{0, 1, 2\}$ and $P(Y = 0) = P(Y = 1) = 1/2$. Find the PMF of $X + Y$.

**Exercise 16.3.** Use `np.convolve` to compute the PMF of the sum of three fair dice. What is the most likely sum?

## Section 16.2 — Continuous Convolution

**Exercise 16.4.** Compute the convolution $f_{X+Y}$ where $X \sim U(0, 1)$ and $Y \sim U(0, 2)$ are independent. Carefully determine the integration limits for each piece.

**Exercise 16.5.** If $X \sim \operatorname{Exp}(1)$ and $Y \sim \operatorname{Exp}(2)$ are independent, compute $f_{X+Y}(a)$ for $a > 0$ and verify it is a hypoexponential density.

**Exercise 16.6.** Prove commutativity of continuous convolution: $f_X * f_Y = f_Y * f_X$.

## Section 16.3 — Sums of Standard Distributions

**Exercise 16.7.** Show that $\operatorname{Pois}(\lambda_1) * \operatorname{Pois}(\lambda_2) = \operatorname{Pois}(\lambda_1 + \lambda_2)$ using MGFs.

**Exercise 16.8.** If $X_1, \ldots, X_{10}$ are iid $\operatorname{Exp}(3)$, find $P(S_{10} > 5)$ where $S_{10} = \sum X_i$.

**Exercise 16.9.** Let $X_1, \ldots, X_n$ be iid $N(\mu, \sigma^2)$. Show that $\bar{X} \sim N(\mu, \sigma^2/n)$ using the MGF of a sum.

**Exercise 16.10.** Write a simulation comparing the Irwin-Hall PDF for $n = 3, 6, 12$ with the corresponding normal approximation.
