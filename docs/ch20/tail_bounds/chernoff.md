# Chernoff's Bound

## Statement

For any random variable $X$ and $\varepsilon > 0$,

$$

P(X \geq \varepsilon) \leq \min_{t > 0} \frac{\mathbb{E}e^{tX}}{e^{t\varepsilon}}

$$

## Proof

For any $t > 0$:

$$

X \geq \varepsilon \iff tX \geq t\varepsilon \iff e^{tX} \geq e^{t\varepsilon}

$$

Since $e^{tX}$ is nonneg, apply Markov's inequality:

$$

P(X \geq \varepsilon) = P(e^{tX} \geq e^{t\varepsilon}) \leq \frac{\mathbb{E}e^{tX}}{e^{t\varepsilon}}

$$

Since this holds for all $t > 0$, we take the minimum.

## Why Chernoff is Often the Tightest

Chernoff's bound uses the **moment generating function** $M_X(t) = \mathbb{E}e^{tX}$, which encodes information about all moments. By optimizing over $t$, the bound adapts to the full shape of the distribution, often giving exponentially decaying bounds.

## Example: Binomial X ~ B(1000, 0.01)

The MGF of a single $X_i \sim B(1, p)$ is $\mathbb{E}e^{tX_i} = 1 + p(e^t - 1)$. For $X = \sum_{i=1}^n X_i$:

$$

\mathbb{E}e^{tX} = \left(1 + p(e^t - 1)\right)^n \leq e^{np(e^t - 1)}

$$

using the inequality $1 + x \leq e^x$.

With $n = 1000$, $p = 0.01$, so $np = 10$. Choosing $t$ such that $e^t = 2$ (i.e., $t = \log 2$):

$$

P(X \geq 20) \leq \frac{e^{10(2-1)}}{e^{20\log 2}} = \frac{e^{10}}{2^{20}} = 0.0210

$$

This is much tighter than Markov ($0.5$), Chebyshev ($0.099$), or one-sided Chebyshev ($0.0901$).

For $P(X \geq 100)$:

$$

P(X \geq 100) \leq \frac{e^{10(2-1)}}{e^{100\log 2}} = \frac{e^{10}}{2^{100}} = 1.2204 \times 10^{-61}

$$

## Example: Poisson X ~ Poi(100)

The MGF is $\mathbb{E}e^{tX} = e^{\lambda(e^t - 1)}$ with $\lambda = 100$. Choosing $e^t = 2$:

$$

P(X \geq 200) \leq \frac{e^{100(2-1)}}{e^{200\log 2}} = \frac{e^{100}}{2^{200}} = 1.6728 \times 10^{-17}

$$

## Comparison Table: B(1000, 0.01)

| Bound | $P(X \geq 20)$ | $P(X \geq 100)$ |
|-------|-----------------|------------------|
| Markov | $0.5$ | $0.1$ |
| Chebyshev | $0.0990$ | $0.0012$ |
| One-sided Chebyshev | $0.0901$ | $0.0012$ |
| Chernoff | $0.0210$ | $1.22 \times 10^{-61}$ |
| CLT approximation | $7.41 \times 10^{-4}$ | $\approx 0$ |

## Comparison Table: Poi(100)

| Bound | $P(X \geq 200)$ | $P(X \geq 110)$ |
|-------|------------------|------------------|
| Markov | $0.5$ | $0.9091$ |
| Chebyshev | $0.0100$ | $1$ |
| One-sided Chebyshev | $0.0099$ | $0.5$ |
| Chernoff | $1.67 \times 10^{-17}$ | $0.6162$ |
| CLT approximation | $7.62 \times 10^{-24}$ | $0.1587$ |

!!! note
    Chernoff's bound excels for **large deviations** (far from the mean) due to its exponential decay, but can be loose for moderate deviations close to the mean.
