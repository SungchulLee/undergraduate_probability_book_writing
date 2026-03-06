# Convergence in Probability

## Definition

A sequence of random variables $X_1, X_2, \ldots$ **converges in probability** to a random variable $X$ if for every $\varepsilon > 0$,

$$

\lim_{n \to \infty} P(|X_n - X| > \varepsilon) = 0

$$

We write

$$

X_n \xrightarrow{p} X

$$

## Interpretation

Convergence in probability means that for any tolerance $\varepsilon > 0$, the probability that $X_n$ deviates from $X$ by more than $\varepsilon$ vanishes as $n \to \infty$. In other words, large deviations become increasingly unlikely, though they are not completely ruled out for any finite $n$.

## Example: Sample Mean

Let $X_1, X_2, \ldots$ be iid with mean $\mu$ and variance $\sigma^2 < \infty$. The sample mean $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ satisfies

$$

\bar{X}_n \xrightarrow{p} \mu

$$

This is precisely the statement of the **Weak Law of Large Numbers**.

## Relationship to Convergence in Distribution

Convergence in probability implies convergence in distribution:

$$

X_n \xrightarrow{p} X \implies X_n \xrightarrow{d} X

$$

The converse is generally false, except when the limit is a **constant** $c$:

$$

X_n \xrightarrow{d} c \iff X_n \xrightarrow{p} c

$$
