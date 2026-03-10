# Chapter 17 Exercises

!!! warning "Exercise page"
    This page collects practice problems for Chapter 17 and does not follow the five-section structure used by concept pages.

Exercises on the Central Limit Theorem: statement, standardization, continuity correction, normal approximation, and confidence intervals.

## Section 17.1 — CLT Statement and Standardization

**Exercise 17.1.** State the CLT precisely. What conditions on $X_1, X_2, \ldots$ are required?

**Exercise 17.2.** Explain why the CLT does not apply to iid Cauchy random variables.

**Exercise 17.3.** If $X_i$ are iid $N(\mu, \sigma^2)$, is the CLT needed to conclude $\frac{S_n - n\mu}{\sigma\sqrt{n}} \sim N(0,1)$? Explain.

**Exercise 17.4.** Let $X_1, \ldots, X_{100}$ be iid with $E[X_i] = 5$ and $\operatorname{Var}(X_i) = 9$. Approximate: (a) $P(S_{100} \le 520)$, (b) $P(480 \le S_{100} \le 520)$, (c) $P(S_{100} \ge 530)$.

## Section 17.2 — Continuity Correction

**Exercise 17.5.** What is the purpose of the continuity correction? When is it used?

**Exercise 17.6.** Let $X \sim \operatorname{Bin}(200, 0.4)$. Use the normal approximation with continuity correction to find: (a) $P(X \le 75)$, (b) $P(X = 80)$, (c) $P(70 \le X \le 90)$.

## Section 17.3 — Applications

**Exercise 17.7.** A fair die is rolled 360 times. Let $S$ be the sum. Approximate $P(S \ge 1300)$ and $P(1200 \le S \le 1300)$. (Use $\mu = 3.5$, $\sigma^2 = 35/12$.)

**Exercise 17.8.** An insurance company has 10,000 policyholders, each filing a claim with probability 0.05 independently. Approximate $P(\text{more than 550 claims})$.

**Exercise 17.9.** Customers arrive at rate 20/hour (Poisson). Approximate the probability that more than 220 arrive in a 10-hour day.

**Exercise 17.10.** A factory has a 2% defect rate. In 1,000 items, approximate $P(15 \le X \le 30)$ where $X$ is the number of defectives.

## Section 17.4 — Confidence Intervals

**Exercise 17.11.** Measurements are iid with unknown mean $\mu$ and $\sigma = 10$. How many measurements are needed for $\bar{X}$ to be within $\pm 2$ of $\mu$ with (a) 90%, (b) 95%, (c) 99% confidence?

**Exercise 17.12.** A poll estimates proportion $p$ (using worst-case $p = 0.5$). How many respondents are needed for margin $\pm 0.03$ at 95% confidence?

## Section 17.5 — Proof and Theory

**Exercise 17.13.** Fill in the details of the CLT proof via MGFs: justify the Taylor expansion and the limit $(1 + t^2/(2n))^n \to e^{t^2/2}$.

**Exercise 17.14.** Let $X_i = \pm 1$ equally likely. Define $W_n(t) = \frac{1}{\sqrt{n}}\sum_{i=1}^{\lfloor nt \rfloor} X_i$. Find the approximate distribution of $W_n(t)$ and of $W_n(t) - W_n(s)$ for $0 \le s < t \le 1$.
