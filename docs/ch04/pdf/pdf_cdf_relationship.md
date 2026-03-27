# Relationship Between PDF and CDF

## Motivation

The CDF and PDF are two descriptions of the same continuous distribution.
The CDF accumulates probability from $-\infty$ up to $x$, while the PDF
describes the rate at which probability is accumulating at each point. The
Fundamental Theorem of Calculus connects the two: integration turns a PDF into
a CDF, and differentiation turns a CDF back into a PDF.

## From PDF to CDF

!!! info "Integration: PDF to CDF"
    Given the PDF $f_X(x)$, the CDF is obtained by integration:

    $$
    F_X(x) = \int_{-\infty}^{x} f_X(s) \, ds
    $$

Geometrically, $F_X(x)$ equals the area under the PDF curve to the left of $x$.
As $x$ increases, this area grows from 0 to 1.

## From CDF to PDF

!!! info "Differentiation: CDF to PDF"
    Given the CDF $F_X(x)$, the PDF is recovered by differentiation (wherever
    $F_X$ is differentiable):

    $$
    f_X(x) = \frac{d}{dx} F_X(x) = F_X'(x)
    $$

Where the CDF is steep, probability is densely packed (high PDF). Where the CDF
is nearly flat, probability is sparse (low PDF).

## Unified View: Discrete and Continuous

The table below summarizes the parallel structure between the discrete and
continuous cases.

| | Discrete | Continuous |
|---|---|---|
| Distribution function | PMF: $p_X(x_i)$ | PDF: $f_X(x)$ |
| CDF formula | $F(x) = \displaystyle\sum_{x_i \le x} p_X(x_i)$ | $F(x) = \displaystyle\int_{-\infty}^{x} f_X(s) \, ds$ |
| Recover distribution | $p_X(x_i) = F(x_i) - F(x_i^-)$ | $f_X(x) = F'(x)$ |
| $P(X \in A)$ | $\displaystyle\sum_{x_i \in A} p_X(x_i)$ | $\displaystyle\int_A f_X(x) \, dx$ |
| Operation | Summation $\sum$ | Integration $\int$ |

In both cases, the CDF is the "running total" of probability mass, and the
distribution function (PMF or PDF) captures the local rate at which mass is
added.

## Example 1: Triangular Density

Let $f_X(x) = 2x$ for $0 \le x \le 1$ and $f_X(x) = 0$ otherwise. Then

$$
F_X(x) = \int_0^x 2s \, ds = x^2, \quad 0 \le x \le 1
$$

with $F_X(x) = 0$ for $x < 0$ and $F_X(x) = 1$ for $x > 1$.

Verification: $F_X'(x) = 2x = f_X(x)$ on $(0, 1)$.

## Example 2: Exponential Distribution

Let $f_X(x) = \lambda e^{-\lambda x}$ for $x \ge 0$ (with $\lambda > 0$) and
$f_X(x) = 0$ for $x < 0$. Then

$$
F_X(x) = \int_0^x \lambda e^{-\lambda s} \, ds = 1 - e^{-\lambda x}, \quad x \ge 0
$$

Verification: $F_X'(x) = \lambda e^{-\lambda x} = f_X(x)$ for $x > 0$.

Using the CDF, we can quickly compute tail probabilities:

$$
P(X > t) = 1 - F_X(t) = e^{-\lambda t}
$$

!!! tip "Which Direction to Use?"
    **PDF to CDF** (integration) is the natural direction when you are given a
    density and need cumulative probabilities. **CDF to PDF** (differentiation)
    is useful when the CDF has a simple closed form and you want the density for
    visualization or further computation.
