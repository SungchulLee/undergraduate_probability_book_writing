# Exercises

## Conceptual Questions

**Exercise 8.1.** Explain the difference between $E(X \mid Y = y)$ (a number) and $E(X \mid Y)$ (a random variable). Give an example of each.

**Exercise 8.2.** True or false: if $X$ and $Y$ are independent, then $\text{Var}(X \mid Y) = \text{Var}(X)$. Justify your answer.

**Exercise 8.3.** In the law of total variance $\text{Var}(X) = E[\text{Var}(X \mid Y)] + \text{Var}(E(X \mid Y))$, give an intuitive explanation of what each term represents. Under what conditions is the first term zero? Under what conditions is the second term zero?

<<<<<<< Updated upstream
**Exercise 8.4.** Three fair coins are flipped. Let $X$ be the total number of heads and $Y$ be the indicator that the first flip is heads. Find the distribution of $E(X \mid Y)$ as a random variable and verify the tower property $E[E(X \mid Y)] = E(X)$.

## Computational Exercises

**Exercise 8.5.** Let $X$ and $Y$ have joint PDF $f(x, y) = 2$ for $0 < x < y < 1$. Find $E(X \mid Y = y)$ and $\text{Var}(X \mid Y = y)$.

**Exercise 8.6.** Let $N \sim \text{Poisson}(\lambda)$ and $X_i \sim \text{Bernoulli}(p)$ be iid, independent of $N$. Let $S = \sum_{i=1}^{N} X_i$. Find $E(S)$ and $\text{Var}(S)$ using the tower property and Eve's law.

**Exercise 8.7.** Let $X$ and $Y$ be iid $\text{Geometric}(p)$. Using the symmetry argument, find $E(X \mid X + Y = n)$.

**Exercise 8.8.** A bus arrives at a bus stop at a uniformly random time $Y$ between 0 and 30 minutes. Given that the bus arrives at time $Y = y$, passengers arrive according to a Poisson process with rate 2 per minute. Let $N$ be the number of passengers waiting when the bus arrives. Find $E(N)$ and $\text{Var}(N)$.

**Exercise 8.9.** Let $X$ and $Y$ have joint PDF $f(x,y) = e^{-y}$ for $0 < x < y < \infty$. Find $E(Y \mid X = x)$ and use it to compute $E(Y)$ via the tower property.

## Properties of Conditional Expectation

**Exercise 8.10.** Let $X$ and $Y$ be random variables with $E(X \mid Y) = 3Y + 2$.

(a) Find $E(X)$ if $E(Y) = 4$.

(b) Show that $E(XY) = 3\,E(Y^2) + 2\,E(Y)$ using the property $E(g(Y) \cdot X \mid Y) = g(Y) \cdot E(X \mid Y)$.

**Exercise 8.11.** Prove that if $X$ and $Y$ are independent, then $E(g(X) \mid Y) = E(g(X))$ for any function $g$.
=======
## Computational Exercises

**Exercise 8.4.** Let $X$ and $Y$ have joint PDF $f(x, y) = 2$ for $0 < x < y < 1$. Find $E(X \mid Y = y)$ and $\text{Var}(X \mid Y = y)$.

**Exercise 8.5.** Let $N \sim \text{Poisson}(\lambda)$ and $X_i \sim \text{Bernoulli}(p)$ be iid, independent of $N$. Let $S = \sum_{i=1}^{N} X_i$. Find $E(S)$ and $\text{Var}(S)$.

**Exercise 8.6.** Let $X$ and $Y$ be iid $\text{Geometric}(p)$. Using the symmetry argument, find $E(X \mid X + Y = n)$.

**Exercise 8.7.** A bus arrives at a bus stop at a uniformly random time $Y$ between 0 and 30 minutes. Given that the bus arrives at time $Y = y$, passengers arrive according to a Poisson process with rate 2 per minute. Let $N$ be the number of passengers waiting when the bus arrives. Find $E(N)$ and $\text{Var}(N)$.

## First-Step Analysis

**Exercise 8.8.** A gambler starts with \$1. On each round, he wins \$1 with probability $p = 0.4$ and loses \$1 with probability $q = 0.6$. He stops when he reaches \$0 (ruin) or \$5 (win). Using first-step analysis with conditional expectation, find the expected number of rounds played.

**Exercise 8.9.** Modify the trapped miner problem: the three doors now lead to safety after 2, 4, and 6 hours respectively, but only with probabilities 1, 0, 0 (i.e., the first door always leads to safety, the others always return the miner). The miner still chooses uniformly. Find $E(T)$ and $\text{Var}(T)$.

**Exercise 8.10.** Find the expected waiting time and variance for the pattern TH in repeated fair coin flips. Compare with HT and HH.

## Simulation Exercises

**Exercise 8.11.** Write a simulation to verify the law of total variance for the department store problem. Generate 100,000 days, compute the within-group and between-group variance components, and compare with the theoretical values.

**Exercise 8.12.** Simulate the waiting times for all four two-letter patterns (HH, HT, TH, TT) in fair coin flips. Create a table comparing the simulated means and variances with the theoretical values. Which pattern has the longest expected waiting time? Which has the largest variance?
>>>>>>> Stashed changes

## First-Step Analysis

**Exercise 8.12.** A gambler starts with \$1. On each round, he wins \$1 with probability $p = 0.4$ and loses \$1 with probability $q = 0.6$. He stops when he reaches \$0 (ruin) or \$5 (win). Using first-step analysis with conditional expectation, find the expected number of rounds played.

**Exercise 8.13.** A miner is trapped with 3 doors. Door 1 leads to safety after 2 hours. Door 2 returns the miner after 4 hours. Door 3 returns the miner after 6 hours. The miner picks each door with equal probability. Find $E(T)$ and $\text{Var}(T)$ using first-step analysis and Eve's law.

**Exercise 8.14.** Flip a fair coin repeatedly. Find the expected waiting time and variance for the patterns HT, HH, and TH. Explain why $E(W_{HT}) = E(W_{TH})$ while $E(W_{HH}) > E(W_{HT})$, even though all four two-letter patterns are equally likely to appear at any specific pair of consecutive flips.

## Simulation Exercises

**Exercise 8.15.** Write a simulation to verify the law of total variance for the department store problem. Generate 100,000 days, compute the within-group and between-group variance components, and compare with the theoretical values $E[\text{Var}(T \mid N)] = 800$ and $\text{Var}(E(T \mid N)) = 6400$.

**Exercise 8.16.** Simulate the waiting times for all four two-letter patterns (HH, HT, TH, TT) in fair coin flips. Create a table comparing the simulated means and variances with the theoretical values.
