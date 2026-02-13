# Chapter 7 Exercises

## Section 7.1: Expectation

**Exercise 7.1.1** Let $X$ be the number showing on a fair die. Compute $E[X]$, $E[X^2]$, and $E[2X + 3]$.

**Exercise 7.1.2** Let $X$ have PMF $P(X = -1) = 0.3$, $P(X = 0) = 0.4$, $P(X = 2) = 0.3$. Compute $E[X]$ and $E[X^2]$.

**Exercise 7.1.3** If $X \sim \text{Uniform}(a, b)$, use LOTUS to show $E[X^2] = \frac{a^2 + ab + b^2}{3}$.

**Exercise 7.1.4** Use the tail sum formula to compute the expectation of a geometric random variable with parameter $p$.

---

## Section 7.2: Indicator Random Variables

**Exercise 7.2.1** There are 100 people at a party. Each person independently has birthday uniform over 365 days. Use indicators to compute the expected number of pairs sharing a birthday.

**Exercise 7.2.2** Throw 200 balls into 100 bins uniformly at random. Use indicators to compute the expected number of empty bins and the variance.

**Exercise 7.2.3** 20 people enter an elevator at the ground floor. Each independently selects one of 10 floors. Find the expected number of floors at which the elevator stops and its variance.

---

## Section 7.3: Variance

**Exercise 7.3.1** If $X$ has mean 3 and $E[X^2] = 13$, compute $\text{Var}(X)$.

**Exercise 7.3.2** Compute the variance of the discrete random variable $X$ with $P(X = -2) = 1/4$, $P(X = 0) = 1/2$, $P(X = 3) = 1/4$.

**Exercise 7.3.3** Show that for any constant $c$, $E[(X - c)^2]$ is minimized when $c = E[X]$, and the minimum value is $\text{Var}(X)$.

---

## Section 7.4: Properties and Inequalities

**Exercise 7.4.1** If $X \geq 0$ with $E[X] = 5$, find an upper bound for $P(X \geq 20)$ using Markov's inequality.

**Exercise 7.4.2** If $E[X] = 10$ and $\text{Var}(X) = 4$, use Chebyshev's inequality to bound $P(|X - 10| \geq 6)$.

**Exercise 7.4.3** Use Jensen's inequality to show that $E[1/X] \geq 1/E[X]$ for $X > 0$.

---

## Section 7.5: Mean and Variance of Sums

**Exercise 7.5.1** Let $X_1, \ldots, X_{100}$ be iid with $E[X_i] = 2$ and $\text{Var}(X_i) = 9$. Compute $E[\sum X_i]$ and $\text{Var}(\sum X_i)$.

**Exercise 7.5.2** Let $S = 3X_1 - 2X_2 + X_3$ where $X_1, X_2, X_3$ are independent with means 1, 2, 3 and variances 4, 1, 9. Compute $E[S]$ and $\text{Var}(S)$.

**Exercise 7.5.3** A portfolio has weights $a = (0.5, 0.3, 0.2)$ and the asset covariance matrix is
$$\Sigma = \begin{pmatrix} 0.04 & 0.01 & 0.02 \\ 0.01 & 0.09 & 0.03 \\ 0.02 & 0.03 & 0.16 \end{pmatrix}$$
Compute the portfolio variance $\mathbf{a}^T \Sigma \mathbf{a}$.

---

## Section 7.6: Decomposition and Unbiased Estimation

**Exercise 7.6.1** The negative binomial $\text{NB}(5, 0.4)$ can be decomposed as a sum of 5 iid geometric random variables. Compute its mean and variance using this decomposition.

**Exercise 7.6.2** A class of 10 students takes a test. Scores $X_1, \ldots, X_{10}$ are iid with unknown mean $\mu$ and variance $\sigma^2$. Show that $\bar{X}$ is unbiased for $\mu$ and compute $\text{Var}(\bar{X})$.

**Exercise 7.6.3** There are 50 types of collectible cards. How many packs do you expect to buy to complete the collection? What is the standard deviation?

**Exercise 7.6.4** Show that dividing by $n$ instead of $n-1$ in the sample variance formula gives a biased estimator, and compute the bias.
