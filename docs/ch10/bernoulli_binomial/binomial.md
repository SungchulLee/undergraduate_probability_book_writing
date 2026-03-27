# Binomial Distribution

## Motivation

Suppose we repeat a Bernoulli experiment $n$ independent times, each with success probability $p$. The total number of successes follows the **Binomial distribution** -- one of the most important discrete distributions in probability and statistics.

## Definition

A random variable $X$ has a **Binomial distribution** with parameters $n \in \{1, 2, \ldots\}$ and $p \in [0, 1]$, written $X \sim \text{Bin}(n, p)$, if its PMF is

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n
$$

Here $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ counts the number of ways to choose which $k$ of the $n$ trials are successes, $p^k$ is the probability of $k$ successes, and $(1-p)^{n-k}$ is the probability of $n - k$ failures.

!!! info "Binomial as a Sum of Bernoullis"
    If $X_1, X_2, \ldots, X_n$ are independent $\text{Bernoulli}(p)$ random variables, then

    $$S = X_1 + X_2 + \cdots + X_n \sim \text{Bin}(n, p)$$

    This is the defining construction. A Bernoulli is the special case $\text{Bin}(1, p)$.

---

## Verification: PMF Sums to 1

By the Binomial Theorem:

$$
\sum_{k=0}^{n} \binom{n}{k} p^k (1-p)^{n-k} = (p + (1-p))^n = 1^n = 1
$$

---

## Mean

Using the Bernoulli decomposition $X = X_1 + \cdots + X_n$ and linearity of expectation:

$$
E[X] = \sum_{i=1}^{n} E[X_i] = np
$$

This derivation avoids any binomial coefficient algebra -- linearity of expectation does not require independence.

---

## Variance

Since the $X_i$ are **independent**, the variance of the sum equals the sum of variances:

$$
\text{Var}(X) = \sum_{i=1}^{n} \text{Var}(X_i) = npq
$$

where $q = 1 - p$.

!!! tip "Why Independence Matters"
    Linearity of expectation holds without independence, so $E[X] = np$ always. But $\text{Var}(X) = npq$ uses the fact that the trials are independent. For dependent trials (e.g., sampling without replacement), the variance formula changes -- see the Hypergeometric distribution.

---

## Key Properties

**Mode.** The most probable value of $\text{Bin}(n, p)$ is $\lfloor (n+1)p \rfloor$ or $\lfloor (n+1)p \rfloor - 1$, depending on whether $(n+1)p$ is an integer.

**Symmetry.** If $X \sim \text{Bin}(n, p)$, then $n - X \sim \text{Bin}(n, 1-p)$. The number of failures is also Binomial.

**Additivity.** If $X \sim \text{Bin}(n, p)$ and $Y \sim \text{Bin}(m, p)$ are independent, then

$$
X + Y \sim \text{Bin}(n + m, p)
$$

This follows from the Bernoulli decomposition: concatenating two independent sequences of Bernoulli trials gives a longer sequence.

---

## Examples

**Coin flips.** Toss a fair coin 10 times. The number of heads $X \sim \text{Bin}(10, 0.5)$ has $E[X] = 5$ and $\text{Var}(X) = 2.5$. The probability of exactly 7 heads is

$$
P(X = 7) = \binom{10}{7} (0.5)^{10} = \frac{120}{1024} \approx 0.117
$$

**Quality control.** A batch of 50 items has a 4% defect rate. If items are tested independently, the number of defectives $X \sim \text{Bin}(50, 0.04)$ has $E[X] = 2$ and $\text{Var}(X) = 1.92$. The probability of zero defectives is

$$
P(X = 0) = (0.96)^{50} \approx 0.130
$$
