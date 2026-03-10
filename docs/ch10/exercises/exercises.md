# Chapter 10 Exercises

!!! warning "Exercise page"
    This page collects practice problems for Chapter 10 and does not follow the five-section structure used by concept pages.

Exercises on the Bernoulli, binomial, geometric, negative binomial, hypergeometric, and discrete uniform distributions.

## Section 10.1 — Bernoulli and Binomial

**Exercise 10.1.** If $X \sim \text{Bin}(20, 0.3)$, compute $P(X = 6)$, $E[X]$, and $\text{Var}(X)$.

**Exercise 10.2.** Show that $\text{Bin}(n, p) + \text{Bin}(m, p) \sim \text{Bin}(n+m, p)$ when the two are independent, using MGFs.

**Exercise 10.3.** A manufacturer's defect rate is 2%. In a batch of 100 items, find the probability of 0, 1, 2, or 3 defects. Compare the binomial answer with the Poisson approximation.

## Section 10.2 — Geometric and Negative Binomial

**Exercise 10.4.** A basketball player makes free throws with probability 0.8. Find the expected number of attempts until the third miss.

**Exercise 10.5.** Prove the memoryless property of the geometric distribution.

**Exercise 10.6.** There are 200 types of collectible cards. How many packs must you buy to expect a complete collection? What is the standard deviation?

## Section 10.3 — Hypergeometric

**Exercise 10.7.** A committee of 5 is chosen from 12 men and 8 women. Find the probability that the committee has exactly 3 women. Compute the mean and variance.

**Exercise 10.8.** Show that $\text{HGeom}(N, K, n) \to \text{Bin}(n, p)$ as $N \to \infty$ with $K/N \to p$, by showing the PMF converges.

## Section 10.4 — Discrete Uniform

**Exercise 10.9.** Derive $\text{Var}(X)$ for $X \sim \text{DUnif}(1, \ldots, n)$ using $\sum_{k=1}^n k^2 = n(n+1)(2n+1)/6$.

**Exercise 10.10.** Two fair dice are rolled. Let $S$ be their sum and $D = |X_1 - X_2|$ their absolute difference. Find $E[D]$ and determine whether $S$ and $D$ are independent.

**Exercise 10.11.** Simulate 10,000 coupon collector trials with $n = 30$. Plot the histogram and compare with the theoretical mean and standard deviation.
