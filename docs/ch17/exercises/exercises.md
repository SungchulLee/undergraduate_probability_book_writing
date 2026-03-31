# Exercises: Central Limit Theorem

## Conceptual Questions

**Exercise 17.1.** State the Central Limit Theorem precisely. What are the required conditions on the random variables $X_1, X_2, \ldots$?

**Exercise 17.2.** Explain why the CLT does not apply to iid Cauchy random variables. What condition of the CLT fails?

**Exercise 17.3.** If $X_1, X_2, \ldots$ are iid $N(\mu, \sigma^2)$, is the CLT needed to conclude that $\frac{S_n - n\mu}{\sigma\sqrt{n}} \sim N(0,1)$? Explain.

**Exercise 17.4.** What is the purpose of the continuity correction? When should it be used, and when is it unnecessary?

## Computation Problems

**Exercise 17.5.** Let $X_1, \ldots, X_{100}$ be iid with $E[X_i] = 5$ and $\text{Var}(X_i) = 9$. Use the CLT to approximate:

(a) $P(S_{100} \leq 520)$

(b) $P(480 \leq S_{100} \leq 520)$

(c) $P(S_{100} \geq 530)$

**Exercise 17.6.** The number of customers arriving at a store each hour is Poisson with mean $20$. Use the CLT to approximate the probability that more than $220$ customers arrive in a $10$-hour day.

**Exercise 17.7.** A fair die is rolled $360$ times. Let $S$ be the sum of all rolls. Use the CLT to approximate:

(a) $P(S \geq 1300)$

(b) $P(1200 \leq S \leq 1300)$

*Hint: For a single die roll, $\mu = 3.5$ and $\sigma^2 = 35/12$.*

**Exercise 17.8.** An insurance company has $10{,}000$ policyholders. Each policyholder files a claim in a given year with probability $0.05$, independently. Use the CLT to approximate the probability that the company receives more than $550$ claims.

## Normal Approximation Problems

**Exercise 17.9.** Let $X \sim B(200, 0.4)$. Use the normal approximation (with continuity correction) to find:

(a) $P(X \leq 75)$

(b) $P(X = 80)$

(c) $P(70 \leq X \leq 90)$

**Exercise 17.10.** A factory produces items with a defect rate of $2\%$. In a batch of $1{,}000$ items, use the CLT to approximate the probability that between $15$ and $30$ items are defective (inclusive).

## Confidence Interval Problems

**Exercise 17.11.** A researcher measures a quantity whose measurements are iid with unknown mean $\mu$ and known standard deviation $\sigma = 10$. How many measurements are needed for the sample mean to be within $\pm 2$ of $\mu$ with:

(a) 90% confidence

(b) 95% confidence

(c) 99% confidence

**Exercise 17.12.** A polling organization wants to estimate the proportion $p$ of voters supporting a candidate. They model each response as Bernoulli($p$). Using $p \approx 0.5$ (worst case for variance), how many voters must be surveyed so the sample proportion is within $\pm 0.03$ of $p$ with 95% confidence?

## Proof and Theory

**Exercise 17.13.** Fill in the details of the CLT proof via MGFs. In particular, rigorously justify the Taylor expansion step $M_{Y_1}(t) \approx 1 + t^2/2$ and the limit $\left(1 + \frac{t^2}{2n}\right)^n \to e^{t^2/2}$.

**Exercise 17.14.** Let $X_i$ be the $i$-th flip of a fair coin, recorded as $+1$ (heads) or $-1$ (tails). Define $W_n = \frac{1}{\sqrt{n}} \sum_{i=1}^{\lfloor nt \rfloor} X_i$ for $t \in [0,1]$.

(a) Find $E[W_n]$ and $\text{Var}(W_n)$.

(b) Use the CLT to find the approximate distribution of $W_n$.

(c) For $0 \leq s < t \leq 1$, find the approximate distribution of $W_n(t) - W_n(s)$ where $W_n(t) = \frac{1}{\sqrt{n}}\sum_{i=1}^{\lfloor nt \rfloor} X_i$.
