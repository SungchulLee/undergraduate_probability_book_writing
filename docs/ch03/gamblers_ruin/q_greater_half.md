# Linear Recurrence Solution (q > 1/2)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Two Distinct Characteristic Roots

When $p \ne q$ (i.e., $p \ne 1/2$), the characteristic equation $p\lambda^2 - \lambda + q = 0$ has two distinct roots:

$$
\lambda_1 = 1, \qquad \lambda_2 = \frac{q}{p}
$$

The two corresponding linearly independent solutions are:

$$
Q_1(i) = 1, \qquad Q_2(i) = \left(\frac{q}{p}\right)^i
$$

## General Solution

The general solution is:

$$
Q(i) = \alpha + \beta \left(\frac{q}{p}\right)^i
$$

## Applying Boundary Conditions

**From $Q(0) = 1$:**

$$
\alpha + \beta = 1
$$

**From $Q(N) = 0$:**

$$
\alpha + \beta \left(\frac{q}{p}\right)^N = 0
$$

Solving this system:

$$
\alpha = \frac{(q/p)^N}{(q/p)^N - 1}, \qquad \beta = \frac{-1}{(q/p)^N - 1}
$$

## Solution

$$
\boxed{Q(i) = \frac{(q/p)^N - (q/p)^i}{(q/p)^N - 1}}
$$

## Why Gambler's Ruin?

Since $q/p > 1$, we have $(q/p)^N \gg 1$ for large $N$, so:

$$
Q(i) \approx \frac{(q/p)^N - (q/p)^i}{(q/p)^N} = 1 - \left(\frac{q}{p}\right)^{i - N} = 1 - \left(\frac{q}{p}\right)^{-(N - i)}
$$

$$
= 1 - e^{-(N-i)\ln(q/p)}
$$

Since $q/p > 1$, we have $\ln(q/p) > 0$, and as $i$ decreases from $N$ (i.e., the gambler loses money):

$$
e^{-(N-i)\ln(q/p)} \to 0 \quad \text{exponentially fast}
$$

$$
Q(i) \to 1 \quad \text{exponentially fast}
$$

Even a slight disadvantage ($p = 0.49$) leads to near-certain ruin. The exponential convergence means that losing even a small amount of capital dramatically increases the ruin probability.

## Numerical Example

With $p = 0.49$, $q = 0.51$, and $N = 200$:

| Initial Capital $i$ | $Q(i)$ |
|---------------------|---------|
| 200 | 0.0000 |
| 190 | 0.3309 |
| 150 | 0.9817 |
| 100 | 0.9998 |
| 50 | $\approx 1$ |

Even starting with \$100 out of a \$200 goal (halfway there), the ruin probability exceeds 99.98%.
