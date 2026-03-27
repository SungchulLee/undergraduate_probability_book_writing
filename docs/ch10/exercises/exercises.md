# Chapter 10 Exercises

## Section 10.1: Bernoulli and Binomial

**Exercise 10.1.1** Let $X \sim \text{Bernoulli}(p)$. Show that $E[X^n] = p$ for every positive integer $n$.

**Exercise 10.1.2** A multiple-choice exam has 20 questions, each with 5 choices. A student guesses randomly on every question. Let $X$ be the number of correct answers.

(a) What is the distribution of $X$? State the parameters.

(b) Compute $E[X]$ and $\text{Var}(X)$.

(c) Find $P(X \ge 8)$ using the complement rule and the Binomial CDF.

**Exercise 10.1.3** Suppose $X \sim \text{Bin}(n, p)$ and $Y \sim \text{Bin}(m, p)$ are independent. Prove that $X + Y \sim \text{Bin}(n + m, p)$ using the Bernoulli decomposition.

**Exercise 10.1.4** Show that the mode of $\text{Bin}(n, p)$ satisfies $(n+1)p - 1 \le k^* \le (n+1)p$ by examining the ratio $P(X = k)/P(X = k - 1)$.

---

## Section 10.2: Geometric and Negative Binomial

**Exercise 10.2.1** A fair die is rolled repeatedly. Let $X$ be the number of rolls needed to see the first six.

(a) Compute $P(X = 4)$.

(b) Compute $P(X > 10)$.

(c) Given that the first 10 rolls were not sixes, find $P(X > 15 \mid X > 10)$ using the memoryless property.

**Exercise 10.2.2** Derive $E[X]$ for $X \sim \text{Geo}(p)$ by computing $\sum_{k=1}^{\infty} k q^{k-1} p$ directly. *(Hint: differentiate the geometric series.)*

**Exercise 10.2.3** Let $X$ be a positive-integer-valued random variable satisfying $P(X > s + t \mid X > s) = P(X > t)$ for all $s, t \ge 1$. Prove that $X$ must be Geometric by showing that $P(X > k) = q^k$ for some $q \in (0, 1)$.

**Exercise 10.2.4** A basketball player makes free throws with probability 0.75, independently. Let $X$ be the number of attempts needed to make 4 free throws.

(a) Name the distribution of $X$ and state its parameters.

(b) Compute $E[X]$ and $\text{SD}(X)$.

(c) Find $P(X = 6)$.

---

## Section 10.3: Coupon Collector

**Exercise 10.3.1** There are 5 different toys, one placed randomly in each cereal box. Compute the exact expected number of boxes needed to collect all 5 toys.

**Exercise 10.3.2** In the coupon collector problem with $n$ coupon types, show that $\text{Var}(T) < \frac{\pi^2}{6} n^2$ for all $n$.

---

## Section 10.4: Hypergeometric

**Exercise 10.4.1** A committee of 5 is chosen at random from a group of 8 men and 6 women.

(a) What is the distribution of the number of women on the committee?

(b) Compute the probability of having exactly 2 women.

(c) Compute the expected number of women using the indicator method.

**Exercise 10.4.2** A lot of $N = 50$ items contains $K = 5$ defectives. An inspector samples $n = 10$ items without replacement. Compute the probability that the sample contains at least one defective.

**Exercise 10.4.3** For $X \sim \text{HGeom}(N, K, n)$, verify that the indicator-variable derivation gives $\text{Cov}(X_i, X_j) = -\frac{K(N - K)}{N^2(N-1)}$ for $i \neq j$, and use this to derive the variance formula.

---

## Section 10.5: Discrete Uniform

**Exercise 10.5.1** Let $X \sim \text{DiscreteUniform}(1, n)$. Use the identity $\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$ to derive $\text{Var}(X) = \frac{n^2 - 1}{12}$.

**Exercise 10.5.2** Two fair dice are rolled independently. Let $S$ be the sum. Find $P(S = 7)$ and explain why 7 is the most likely sum.
