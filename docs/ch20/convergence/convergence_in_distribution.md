# Convergence in Distribution (Review from Ch 17)

## Definition

A sequence of random variables $X_1, X_2, \ldots$ **converges in distribution** to a random variable $X$ if

$$
\lim_{n \to \infty} F_{X_n}(x) = F_X(x)
$$

<<<<<<< Updated upstream
at every point $x$ where $F_X$ is continuous. We write $X_n \xrightarrow{d} X$.

## Why Review This Here?

Convergence in distribution was introduced in Chapter 17 as the language for the Central Limit Theorem. In this chapter, we place it alongside two stronger notions -- convergence in probability and almost sure convergence -- to understand where the CLT and the Law of Large Numbers fit in the hierarchy.

## Key Properties

Convergence in distribution is the **weakest** of the three modes. It concerns only the **CDFs** of the random variables, not the random variables themselves. Two sequences can converge in distribution to the same limit even if they are defined on entirely different probability spaces.

!!! info "Equivalent Characterization"
    $X_n \xrightarrow{d} X$ if and only if $E[g(X_n)] \to E[g(X)]$ for every bounded continuous function $g$.

## The CLT as an Example

The Central Limit Theorem (Chapter 17) is the most important example of convergence in distribution:
=======
at every point $x$ where $F_X$ is continuous. We write

$$
X_n \xrightarrow{d} X
$$

## Recap

Convergence in distribution is the weakest mode of convergence. It says that the **CDFs** of the sequence approach the CDF of the limit, but makes no statement about whether the random variables are "close" on the same probability space.

The Central Limit Theorem (Ch 17) is the most important example:
>>>>>>> Stashed changes

$$
\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} N(0,1)
$$

<<<<<<< Updated upstream
This tells us the **shape** of the distribution of the standardized sample mean approaches the standard normal bell curve. It does not tell us that the sample mean converges to any particular value -- the limit $N(0,1)$ is not a constant.

## Special Case: Convergence to a Constant

When the limit is a **constant** $c$ (i.e., $F_X$ is a step function jumping from 0 to 1 at $x = c$), convergence in distribution becomes equivalent to convergence in probability:

$$
X_n \xrightarrow{d} c \iff X_n \xrightarrow{p} c
$$

This special case is crucial because the Law of Large Numbers states $\bar{X}_n \to \mu$, where $\mu$ is a constant. Thus there is no gap between the WLLN (convergence in probability) and saying the CDF of $\bar{X}_n$ collapses to a point mass at $\mu$.

## Relationship to Other Modes

Both convergence in probability and almost sure convergence imply convergence in distribution:

$$
X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{p} X \implies X_n \xrightarrow{d} X
$$

The reverse implications fail in general (see the section on relationships between modes of convergence).
=======
This tells us the **shape** of the distribution of the standardized sample mean approaches a standard normal, but it does not say that the sample mean itself converges to any single value.

## Key Point

Convergence in distribution concerns only the **distribution functions**, not the random variables themselves. Two sequences can converge in distribution to the same limit even if they are defined on completely different probability spaces.
>>>>>>> Stashed changes
