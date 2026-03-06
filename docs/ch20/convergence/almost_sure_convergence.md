# Almost Sure Convergence

## Definition

A sequence of random variables $X_1, X_2, \ldots$ **converges almost surely** (a.s.) to a random variable $X$ if

$$

P\left(\lim_{n \to \infty} X_n = X\right) = 1

$$

We write

$$

X_n \xrightarrow{a.s.} X

$$

This is also called **convergence with probability 1**.

## Interpretation

Almost sure convergence means that the set of outcomes $\omega$ for which $X_n(\omega) \to X(\omega)$ has probability 1. For **almost every** realization of the random sequence, the values eventually settle down to the limit.

!!! note "Weak vs Strong"
    - **Convergence in probability** (weak): For any fixed $\varepsilon$, the probability of a deviation $> \varepsilon$ goes to 0.
    - **Almost sure convergence** (strong): With probability 1, the entire sample path converges.

## Comparison with Convergence in Probability

Almost sure convergence is **stronger** than convergence in probability:

$$

X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{p} X

$$

The converse is not true in general.

## Visual Intuition

Consider flipping a fair coin many times and tracking the running sample mean:

- **Strong law** (a.s. convergence): A single sequence of flips. As the number of flips grows, the running average converges to 0.5. The plot of one sample path approaches the true mean.
- **Weak law** (convergence in probability): Repeat the experiment many times (each time flipping $n$ coins and recording the average). As $n$ grows, the histogram of sample means concentrates around 0.5.

The left panel (single trajectory converging) illustrates the **strong** law, while the right panel (histogram concentrating) illustrates the **weak** law.
