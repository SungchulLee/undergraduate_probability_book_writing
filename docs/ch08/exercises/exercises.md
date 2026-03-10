# Chapter 8 Exercises

!!! warning "Exercise page"
    This page collects practice problems for Chapter 8 and does not follow the five-section structure used by concept pages.

Exercises on conditional expectation, the tower property, Eve's law, and first-step analysis.

## Section 8.1 — Conditional Expectation

**Exercise 8.1.** Explain the difference between $E[X \mid Y = y]$ (a number) and $E[X \mid Y]$ (a random variable). Give an example of each.

**Exercise 8.2.** True or false: if $X$ and $Y$ are independent, then $\text{Var}(X \mid Y) = \text{Var}(X)$. Justify your answer.

**Exercise 8.3.** Let $X$ and $Y$ have joint PDF $f(x, y) = 2$ for $0 < x < y < 1$. Find $E[X \mid Y = y]$ and $\text{Var}(X \mid Y = y)$.

## Section 8.2 — Tower Property

**Exercise 8.4.** Let $X$ and $Y$ be iid $\text{Geo}(p)$. Using the symmetry argument, find $E[X \mid X + Y = n]$.

**Exercise 8.5.** Let $N \sim \text{Poisson}(\lambda)$ and $X_i \sim \text{Bern}(p)$ be iid, independent of $N$. Let $S = \sum_{i=1}^N X_i$. Find $E[S]$ and $\text{Var}(S)$.

**Exercise 8.6.** A bus arrives at a uniformly random time $Y \in [0, 30]$ minutes. Given $Y = y$, the number of waiting passengers is $\text{Poisson}(2y)$. Find $E[N]$ and $\text{Var}(N)$.

## Section 8.3 — Eve's Law

**Exercise 8.7.** In Eve's law $\text{Var}(X) = E[\text{Var}(X \mid Y)] + \text{Var}(E[X \mid Y])$, give an intuitive explanation of each term. When is the first term zero? When is the second term zero?

**Exercise 8.8.** A gambler starts with \$1. Each round: win \$1 with probability $p = 0.4$, lose \$1 with probability $q = 0.6$. He stops at \$0 or \$5. Use first-step analysis to find the expected number of rounds.

**Exercise 8.9.** Modify the trapped miner: doors lead to safety after 2, 4, 6 hours, but only door 1 succeeds (doors 2, 3 always return). The miner chooses uniformly. Find $E[T]$ and $\text{Var}(T)$.

**Exercise 8.10.** Find the expected waiting time and variance for the pattern TH in fair coin flips. Compare with HT and HH.

## Section 8.4 — Simulation

**Exercise 8.11.** Write a simulation to verify Eve's law for the department store problem. Generate 100,000 days and compare the within-group and between-group variance components with theory.

**Exercise 8.12.** Simulate waiting times for all four two-letter patterns (HH, HT, TH, TT). Create a table comparing simulated and theoretical means and variances.

**Exercise 8.13.** Extend the trapped miner simulation to compute the full distribution of exit times. Plot a histogram and overlay the theoretical mean and standard deviation.
