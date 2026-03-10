# Central Limit Theorem (Statement)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Setup

Let $X_1, X_2, \ldots$ be **iid** random variables with:

- Mean: $E[X_i] = \mu$
- Variance: $\text{Var}(X_i) = \sigma^2 < \infty$

Define the partial sum:

$$S_n = X_1 + X_2 + \cdots + X_n$$

Then $S_n$ has mean $n\mu$ and variance $n\sigma^2$.

## The Central Limit Theorem

!!! info "CLT"
    Let $X_1, X_2, \ldots$ be iid with mean $\mu$ and variance $\sigma^2$. Then:

    $$\frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0, 1) \quad \text{as } n \to \infty$$

    That is, for any $x$:

    $$P\left(\frac{S_n - n\mu}{\sigma\sqrt{n}} \leq x\right) \to \Phi(x) = \int_{-\infty}^{x} \frac{1}{\sqrt{2\pi}} e^{-s^2/2}\, ds$$

## What the CLT Says

| Random Variable | Mean | Variance | Distribution |
|----------------|------|----------|-------------|
| $X_i$ | $\mu$ | $\sigma^2$ | **Not** necessarily Normal |
| $S_n$ | $n\mu$ | $n\sigma^2$ | **Not** Normal, but **approximately normal** for large $n$ |
| $\frac{S_n - n\mu}{\sigma\sqrt{n}}$ | $0$ | $1$ | **Not** Normal, but **approximately** $N(0,1)$ for large $n$ |

## Contrast: Normal Case vs General Case

When the $X_i$ are themselves normal, the sum $S_n$ is **exactly** normal for all $n$ — no approximation is needed.

| | iid $N(\mu, \sigma^2)$ | iid with mean $\mu$, variance $\sigma^2$ (not Normal) |
|---|---|---|
| $S_n$ | $N(n\mu, n\sigma^2)$ exactly | $\approx N(n\mu, n\sigma^2)$ for large $n$ |
| $\frac{S_n - n\mu}{\sigma\sqrt{n}}$ | $N(0,1)$ exactly | $\approx N(0,1)$ for large $n$ |

## Practical Approximation

For large $n$, we use:

$$S_n \approx N(n\mu, \, n\sigma^2)$$

or equivalently:

$$\bar{X}_n = \frac{S_n}{n} \approx N\left(\mu, \, \frac{\sigma^2}{n}\right)$$

## Simulation Evidence

The CLT applies regardless of the original distribution of $X_i$. The following all produce approximately normal sums when $n$ is large:

- $X_i \sim \text{Bernoulli}(0.7)$: right-skewed discrete
- $X_i \sim \text{Exp}(2)$: right-skewed continuous
- $X_i \sim \text{Po}(2)$: right-skewed discrete
- $X_i \sim \text{Beta}(2, 5)$: skewed continuous on $[0,1]$
- $X_i \sim F(2, 5)$: heavily right-skewed
- $X_i \sim \text{Gamma}(2, 5)$: right-skewed continuous

Even with $n = 20$, the histograms of $S_{20}$ are strikingly bell-shaped for all these distributions.
