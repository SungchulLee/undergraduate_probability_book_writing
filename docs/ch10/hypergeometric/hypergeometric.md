# Hypergeometric Distribution

## Motivation

A deck has 52 cards, 4 of which are aces. You draw 5 cards **without replacement**. What is the probability of getting exactly 2 aces? Since cards are drawn without replacement, the draws are **dependent** -- each draw changes the composition of the remaining deck. The **Hypergeometric distribution** handles this setting.

## Setup

Consider a population of $N$ items, of which $K$ are "successes" and $N - K$ are "failures." We draw $n$ items **without replacement**. Let $X$ be the number of successes in the sample.

## Definition

!!! info "Hypergeometric PMF"
    $X \sim \text{HGeom}(N, K, n)$ has PMF

    $$P(X = k) = \frac{\dbinom{K}{k}\dbinom{N-K}{n-k}}{\dbinom{N}{n}}$$

    for $k = \max(0, n - N + K), \ldots, \min(n, K)$.

**Reading the formula.** The denominator $\binom{N}{n}$ counts all ways to choose $n$ items from $N$. The numerator counts favorable outcomes: choose $k$ of the $K$ successes and $n - k$ of the $N - K$ failures.

---

## Mean

The mean can be derived elegantly using indicator variables. Let $X_i = 1$ if the $i$-th drawn item is a success. Then $X = X_1 + \cdots + X_n$, and by symmetry each item in the sample is equally likely to be any of the $N$ items, so

$$
E[X_i] = \frac{K}{N}
$$

By linearity of expectation (which does **not** require independence):

$$
E[X] = n \cdot \frac{K}{N}
$$

This is the same as the Binomial mean $np$ with $p = K/N$. The mean is unaffected by whether we sample with or without replacement.

---

## Variance

The variance requires more care because the $X_i$ are **not** independent. Using the formula $\text{Var}(X) = \sum_i \text{Var}(X_i) + 2\sum_{i < j} \text{Cov}(X_i, X_j)$:

Each $X_i$ is Bernoulli with $p = K/N$, so $\text{Var}(X_i) = p(1-p)$.

For the covariance, $E[X_i X_j] = P(\text{items } i \text{ and } j \text{ both successes}) = \frac{K(K-1)}{N(N-1)}$, so

$$
\text{Cov}(X_i, X_j) = \frac{K(K-1)}{N(N-1)} - \frac{K^2}{N^2} = -\frac{K(N-K)}{N^2(N-1)}
$$

Combining $n$ variance terms and $\binom{n}{2}$ covariance terms:

$$
\text{Var}(X) = n \cdot \frac{K}{N} \cdot \frac{N-K}{N} \cdot \frac{N-n}{N-1}
$$

!!! info "Hypergeometric Variance"
    $$\text{Var}(X) = n \cdot \frac{K}{N} \cdot \frac{N-K}{N} \cdot \frac{N-n}{N-1}$$

    The factor $\dfrac{N-n}{N-1}$ is the **finite population correction**. It is always $\le 1$, so the Hypergeometric variance is always at most the corresponding Binomial variance $npq$.

---

## Support

The support of $X$ is not simply $\{0, 1, \ldots, n\}$. We need both:

- at least $k$ successes available: $k \le K$
- at least $n - k$ failures available: $n - k \le N - K$

So $k$ ranges from $\max(0, n - N + K)$ to $\min(n, K)$.

---

## Examples

**Card draw.** Draw $n = 5$ cards from a standard deck ($N = 52$) containing $K = 4$ aces. The number of aces $X \sim \text{HGeom}(52, 4, 5)$ has

$$
P(X = 2) = \frac{\binom{4}{2}\binom{48}{3}}{\binom{52}{5}} = \frac{6 \times 17296}{2598960} \approx 0.0399
$$

$$
E[X] = 5 \cdot \frac{4}{52} \approx 0.385, \qquad \text{Var}(X) \approx 0.341
$$

**Quality inspection.** A shipment of $N = 100$ items contains $K = 8$ defectives. An inspector draws $n = 10$ items without replacement. The expected number of defectives found is $E[X] = 10 \cdot 8/100 = 0.8$. The probability of finding no defectives is

$$
P(X = 0) = \frac{\binom{8}{0}\binom{92}{10}}{\binom{100}{10}} \approx 0.410
$$
