# Chapter 21 Exercises

!!! warning "Exercise page"
    This page collects practice problems for Chapter 21 and does not follow the five-section structure used by concept pages.

Exercises on simulation techniques: random sampling, Monte Carlo estimation, random walks, and the arcsine laws.

## Section 21.1 — Generating Random Samples

**Exercise 21.1.** Use the inverse CDF method to generate samples from $F(x) = 1 - e^{-x^2}$ for $x \ge 0$. Verify by comparing the sample mean with the numerical integral $\int_0^\infty x \cdot 2x e^{-x^2} dx$.

**Exercise 21.2.** Implement rejection sampling to generate from $f(x) = \frac{3}{2}(1 - x^2)$ on $[-1, 1]$ using a uniform proposal. What is the acceptance rate?

## Section 21.2 — Monte Carlo Applications

**Exercise 21.3.** Estimate $e$ using the fact that $E[N] = e$ where $N = \min\{n : U_1 + \cdots + U_n > 1\}$ and $U_i \sim U(0,1)$. Report the estimate and standard error from 10,000 trials.

**Exercise 21.4.** Use Monte Carlo to estimate $\int_0^1 e^{-x^2} dx$ with 10,000 samples and provide a 95% confidence interval.

**Exercise 21.5.** Simulate the birthday problem for group sizes $n = 2, \ldots, 60$. At what $n$ does $P(\text{shared birthday})$ first exceed 0.5?

## Section 21.3 — Random Walks

**Exercise 21.6.** Simulate a 1D random walk for $n = 10{,}000$ steps. Plot 5 sample paths. For each, compute the fraction of time $S_n > 0$.

**Exercise 21.7.** Simulate a 2D random walk for 10,000 steps. Count how many times it returns to the origin.

**Exercise 21.8.** In the gambler's ruin with $i = 5$, $N = 10$, $p = 0.5$: estimate the expected game duration from 10,000 simulations. Compare with the theoretical value $i(N-i) = 25$.

## Section 21.4 — Arcsine Laws

**Exercise 21.9.** Simulate 1000 symmetric random walks of length 10,000. For each, record (a) the last visit time to zero, (b) the fraction of time positive, (c) the time of the maximum. Plot histograms and verify all three follow the arcsine distribution.

**Exercise 21.10.** Explain intuitively why spending exactly 50% of time positive is the least likely outcome for a symmetric random walk.

## Section 21.5 — Longest Run

**Exercise 21.11.** For $n = 100, 1000, 10000, 100000$ coin flips, estimate the mean longest run via simulation. Plot against $\log_2 n$.

**Exercise 21.12.** Modify the longest run simulation for a biased coin with $p = 0.7$. How does the expected longest run of heads change compared to the fair coin case?
