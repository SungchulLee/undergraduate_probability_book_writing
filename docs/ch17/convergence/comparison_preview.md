# Convergence in Distribution vs Other Modes (Preview)

## Why Multiple Modes of Convergence?

When we say a sequence of random variables "converges," we need to specify what we mean. Unlike sequences of real numbers, random variables can converge in several distinct senses. These modes differ in strength and in what they tell us about the behavior of the sequence.

## Overview of Convergence Modes

There are three principal modes of convergence, listed from strongest to weakest:

| Mode | Notation | Formal Definition |
|------|----------|-------------------|
| Almost sure | $X_n \xrightarrow{a.s.} X$ | $P(\lim_{n\to\infty} X_n = X) = 1$ |
| In probability | $X_n \xrightarrow{p} X$ | $P(\|X_n - X\| > \varepsilon) \to 0$ for all $\varepsilon > 0$ |
| In distribution | $X_n \xrightarrow{d} X$ | $F_{X_n}(x) \to F_X(x)$ at every continuity point of $F_X$ |

**Almost sure convergence** says that for almost every outcome $\omega$, the entire sample path $X_n(\omega)$ converges to $X(\omega)$. **Convergence in probability** says that the probability of a large deviation shrinks to zero. **Convergence in distribution** says only that the CDFs converge pointwise.

## Implications

$$
X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{p} X \implies X_n \xrightarrow{d} X
$$

The reverse implications do **not** hold in general.

!!! warning "Special Case: Convergence to a Constant"
    If $X_n \xrightarrow{d} c$ where $c$ is a **constant**, then $X_n \xrightarrow{p} c$ as well. Convergence in distribution to a constant is equivalent to convergence in probability to that constant.

## Why This Matters for the CLT

The Central Limit Theorem is a statement about **convergence in distribution**:

$$
\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} N(0,1)
$$

This tells us that the **shape** of the distribution of the standardized sample mean approaches the bell curve. It says nothing about the behavior of individual sample paths. In particular, the standardized mean does not converge to any single value -- the standard normal is not a constant.

By contrast, the **Law of Large Numbers** (Chapter 20) gives the stronger statements:

- **Weak Law**: $\bar{X}_n \xrightarrow{p} \mu$ (convergence in probability)
- **Strong Law**: $\bar{X}_n \xrightarrow{a.s.} \mu$ (almost sure convergence)

These are stronger because $\mu$ is a constant, and the LLN tells us the sample mean itself settles down to $\mu$. The CLT tells us **how** the fluctuations around $\mu$ are distributed.

!!! note "Full Treatment in Chapter 20"
    Formal definitions, proofs of the implication hierarchy, counterexamples showing reverse implications fail, and the connection to the Law of Large Numbers are presented in **Chapter 20: Law of Large Numbers**, Section 20.2.
