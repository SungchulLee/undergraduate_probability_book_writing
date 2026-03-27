# Geometric Distribution

## Motivation

How many times must you roll a die before you see the first six? How many components must you test before finding the first defective one? The **Geometric distribution** models the number of independent Bernoulli trials needed to obtain the first success.

## Definition

A random variable $X$ has a **Geometric distribution** with parameter $p \in (0, 1]$, written $X \sim \text{Geo}(p)$, if its PMF is

$$
P(X = k) = (1-p)^{k-1} p, \quad k = 1, 2, 3, \ldots
$$

Here $k$ is the **trial number** of the first success: the first $k - 1$ trials are failures (each with probability $q = 1-p$) and the $k$-th trial is a success (probability $p$).

!!! warning "Convention"
    Some texts define the Geometric as the number of **failures before** the first success, supported on $\{0, 1, 2, \ldots\}$ with PMF $P(Y = k) = q^k p$. We use the "number of trials" convention throughout. The two are related by $Y = X - 1$.

---

## Verification: PMF Sums to 1

$$
\sum_{k=1}^{\infty} q^{k-1} p = p \sum_{j=0}^{\infty} q^{j} = p \cdot \frac{1}{1-q} = p \cdot \frac{1}{p} = 1
$$

This uses the geometric series formula $\sum_{j=0}^{\infty} r^j = \frac{1}{1-r}$ for $|r| < 1$.

---

## CDF and Tail Probability

The tail probability has a particularly clean form. The event $\{X > k\}$ means the first $k$ trials are all failures:

$$
P(X > k) = q^k, \quad k = 0, 1, 2, \ldots
$$

The CDF follows immediately:

$$
F(k) = P(X \le k) = 1 - q^k, \quad k = 1, 2, 3, \ldots
$$

---

## Mean

We derive $E[X]$ using the **tail-sum formula** for non-negative integer-valued random variables. Since $X \ge 1$:

$$
E[X] = \sum_{k=0}^{\infty} P(X > k) = \sum_{k=0}^{\infty} q^k = \frac{1}{1-q} = \frac{1}{p}
$$

!!! info "Mean of Geometric"
    If $X \sim \text{Geo}(p)$, then $E[X] = \dfrac{1}{p}$.

    On average, you need $1/p$ trials to see the first success. For a fair die ($p = 1/6$), you need 6 rolls on average.

---

## Variance

To find $\text{Var}(X)$, we compute $E[X^2]$ using $E[X(X-1)]$:

$$
E[X(X-1)] = \sum_{k=2}^{\infty} k(k-1) q^{k-1} p = pq \sum_{k=2}^{\infty} k(k-1) q^{k-2} = pq \cdot \frac{2}{(1-q)^3} = \frac{2q}{p^2}
$$

Then $E[X^2] = E[X(X-1)] + E[X] = \frac{2q}{p^2} + \frac{1}{p} = \frac{2q + p}{p^2} = \frac{1+q}{p^2}$, so

$$
\text{Var}(X) = E[X^2] - (E[X])^2 = \frac{1+q}{p^2} - \frac{1}{p^2} = \frac{q}{p^2}
$$

!!! info "Variance of Geometric"
    If $X \sim \text{Geo}(p)$, then $\text{Var}(X) = \dfrac{q}{p^2} = \dfrac{1-p}{p^2}$.

---

## Examples

**Rolling a die.** Let $X$ be the number of rolls until the first six appears, so $X \sim \text{Geo}(1/6)$.

- $E[X] = 6$ rolls on average.
- $\text{Var}(X) = \frac{5/6}{1/36} = 30$, so $\text{SD}(X) = \sqrt{30} \approx 5.48$.
- $P(X > 10) = (5/6)^{10} \approx 0.162$.

**Network packet.** A packet is transmitted with success probability $p = 0.9$. The number of attempts until the first successful transmission is $X \sim \text{Geo}(0.9)$ with $E[X] = 1/0.9 \approx 1.11$ and $P(X > 3) = (0.1)^3 = 0.001$.
