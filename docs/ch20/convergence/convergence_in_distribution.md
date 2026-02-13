# Convergence in Distribution (Review from Ch 17)

## Definition

A sequence of random variables $X_1, X_2, \ldots$ **converges in distribution** to a random variable $X$ if

$$
\lim_{n \to \infty} F_{X_n}(x) = F_X(x)
$$

at every point $x$ where $F_X$ is continuous. We write

$$
X_n \xrightarrow{d} X
$$

## Recap

Convergence in distribution is the weakest mode of convergence. It says that the **CDFs** of the sequence approach the CDF of the limit, but makes no statement about whether the random variables are "close" on the same probability space.

The Central Limit Theorem (Ch 17) is the most important example:

$$
\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} N(0,1)
$$

This tells us the **shape** of the distribution of the standardized sample mean approaches a standard normal, but it does not say that the sample mean itself converges to any single value.

## Key Point

Convergence in distribution concerns only the **distribution functions**, not the random variables themselves. Two sequences can converge in distribution to the same limit even if they are defined on completely different probability spaces.
