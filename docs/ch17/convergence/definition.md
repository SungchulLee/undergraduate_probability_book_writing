# Convergence in Distribution: Definition and Examples


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

A sequence of random variables $X_1, X_2, \ldots$ **converges in distribution** to a random variable $X$ if

$$\lim_{n \to \infty} F_{X_n}(x) = F_X(x)$$

for every $x$ at which $F_X$ is continuous. We write $X_n \xrightarrow{d} X$.

Equivalently, for all bounded continuous functions $g$,

$$\lim_{n \to \infty} E[g(X_n)] = E[g(X)]$$

## Intuition

Convergence in distribution is the **weakest** form of convergence. It says nothing about the random variables being defined on the same probability space — it only concerns the **CDFs**.

Think of it as: "the histograms of $X_n$ look more and more like the density of $X$."

## Key Examples

### Example 1: Binomial Approaching Normal

Let $X_n \sim B(n, p)$. Define the standardized version:

$$Z_n = \frac{X_n - np}{\sqrt{np(1-p)}}$$

Then $Z_n \xrightarrow{d} Z \sim N(0,1)$ as $n \to \infty$. This is precisely the **Central Limit Theorem** applied to sums of iid Bernoulli random variables.

### Example 2: Poisson Approaching Normal

Let $X_n \sim \text{Po}(n)$. Then:

$$\frac{X_n - n}{\sqrt{n}} \xrightarrow{d} N(0,1)$$

Since $X_n = \sum_{i=1}^n Y_i$ where $Y_i \sim \text{Po}(1)$ are iid, this follows directly from the CLT.

### Example 3: Discrete to Continuous

Let $X_n$ be uniform on $\left\{\frac{1}{n}, \frac{2}{n}, \ldots, \frac{n}{n}\right\}$. Then $X_n \xrightarrow{d} U(0,1)$.

## Convergence via MGFs

A powerful tool for proving convergence in distribution:

!!! info "Continuity Theorem for MGFs"
    If $M_{X_n}(t) \to M_X(t)$ for all $t$ in a neighborhood of $0$, and $M_X(t)$ is the MGF of $X$, then $X_n \xrightarrow{d} X$.

This is the key technique used in the **proof of the CLT**.
