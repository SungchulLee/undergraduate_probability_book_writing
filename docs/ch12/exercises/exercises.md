# Chapter 12 Exercises

!!! warning "Exercise page"
    This page collects practice problems for Chapter 12 and does not follow the five-section structure used by concept pages.

Exercises on the Poisson distribution, the Poisson limit theorem, and the additivity property.

## Section 12.1 — Poisson Distribution

**Exercise 12.1.** Let $X \sim \text{Pois}(6)$. Compute $P(X = 0)$, $P(X = 6)$, $P(X \le 4)$, and $P(X > 8)$. Find the mode.

**Exercise 12.2.** Verify numerically that $E[X] = \text{Var}(X) = \lambda$ for $\lambda = 1, 5, 10, 20$ by simulation.

**Exercise 12.3.** Customer complaints arrive at rate 3 per day. What is the probability of 0 complaints? More than 5?

## Section 12.2 — Poisson Approximation

**Exercise 12.4.** A factory produces chips with defect probability $p = 0.002$ per chip, $n = 1000$. Using both exact binomial and Poisson approximation, compute $P(X = 0)$, $P(X \le 3)$, $P(X > 5)$. Find the Le Cam error bound.

**Exercise 12.5.** Among 80,000 married couples, estimate the probability that more than 250 share a birthday ($p = 1/365$). Compare binomial and Poisson answers.

**Exercise 12.6.** For $\lambda = 5$, compute $\max_k |P(\text{Bin}(n, 5/n) = k) - P(\text{Pois}(5) = k)|$ for $n = 10, 50, 100, 1000$. Verify the $O(1/n)$ convergence rate.

## Section 12.3 — Additivity

**Exercise 12.7.** Calls arrive from three sources: $\text{Pois}(8)$, $\text{Pois}(5)$, $\text{Pois}(2)$ per hour, independent. Find the distribution of total calls. Compute $P(\text{total} > 20)$.

**Exercise 12.8.** A car has 500 potential defects, each with $p = 0.001$. A factory ships 200 cars/day. Find the distribution and expected value of total defects per day.

## Section 12.4 — Diagnostics

**Exercise 12.9.** Observed daily counts: 3, 1, 4, 2, 7, 0, 3, 5, 1, 2, 8, 3, 2, 1, 4, 6, 0, 3, 2, 5, 1, 4, 3, 2, 1, 9, 3, 2, 4, 1. Compute the dispersion index. Is a Poisson model appropriate?
