# Negative Binomial Distribution
<<<<<<< Updated upstream

## Motivation

The Geometric distribution counts trials until the **first** success. What if we want the number of trials until the **r-th** success? For example, how many times must a salesperson make calls until closing 5 deals? This is the **Negative Binomial distribution**, which generalizes the Geometric in the same way that the Binomial generalizes the Bernoulli.

## Definition

A random variable $X$ has a **Negative Binomial distribution** with parameters $r \in \{1, 2, \ldots\}$ and $p \in (0, 1]$, written $X \sim \text{NB}(r, p)$, if its PMF is

$$
P(X = k) = \binom{k-1}{r-1} p^r (1-p)^{k-r}, \quad k = r, r+1, r+2, \ldots
$$

Here $k$ is the trial on which the $r$-th success occurs. The binomial coefficient $\binom{k-1}{r-1}$ counts the number of ways to place $r - 1$ successes among the first $k - 1$ trials (the $k$-th trial must be a success).

!!! info "Special Case"
    When $r = 1$, the Negative Binomial reduces to the Geometric: $\text{NB}(1, p) = \text{Geo}(p)$.

---

## Decomposition as a Sum of Geometrics

The $r$-th success can be reached by waiting for the 1st success, then the 2nd, and so on. Let $Y_i$ be the number of trials between the $(i-1)$-th and $i$-th success. By the memoryless property of Bernoulli trials, each $Y_i \sim \text{Geo}(p)$ independently, and

$$
X = Y_1 + Y_2 + \cdots + Y_r
$$

This decomposition is the most natural way to derive the mean and variance.

---

## Mean and Variance

Using $X = Y_1 + \cdots + Y_r$ with independent $Y_i \sim \text{Geo}(p)$:

**Mean:**

$$
E[X] = r \cdot E[Y_1] = \frac{r}{p}
$$

**Variance:**

$$
\text{Var}(X) = r \cdot \text{Var}(Y_1) = \frac{rq}{p^2}
$$

where $q = 1 - p$.

!!! info "Negative Binomial Moments"
    If $X \sim \text{NB}(r, p)$, then

    $$E[X] = \frac{r}{p}, \qquad \text{Var}(X) = \frac{rq}{p^2}$$

---

## Verification: PMF Sums to 1

Using the **negative binomial series** $(1 - q)^{-r} = \sum_{j=0}^{\infty} \binom{r+j-1}{j} q^j$, substituting $k = r + j$:

$$
\sum_{k=r}^{\infty} \binom{k-1}{r-1} p^r q^{k-r} = p^r \sum_{j=0}^{\infty} \binom{r+j-1}{j} q^j = p^r \cdot \frac{1}{(1-q)^r} = p^r \cdot \frac{1}{p^r} = 1
$$

This connection to the negative binomial series is the origin of the distribution's name.

---

## Examples

**Sales calls.** A salesperson closes each call independently with probability $p = 0.2$. The number of calls until 5 deals is $X \sim \text{NB}(5, 0.2)$ with $E[X] = 25$ and $\text{Var}(X) = 100$.

**Baseball hits.** A batter has a 0.300 batting average. The number of at-bats until 3 hits is $X \sim \text{NB}(3, 0.3)$ with $E[X] = 10$ and $\text{SD}(X) = \sqrt{3 \cdot 0.7 / 0.09} \approx 4.83$.

**Relation to Binomial.** The Binomial fixes the number of trials and counts successes. The Negative Binomial fixes the number of successes and counts trials. They are "complementary" views of the same Bernoulli process.
=======
>>>>>>> Stashed changes
