# Relationship Between PDF and CDF


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## From PDF to CDF

Given the PDF $f(x)$, the CDF is obtained by integration:

$$F(x) = \int_{-\infty}^{x} f(s) \, ds$$

## From CDF to PDF

Given the CDF $F(x)$, the PDF is obtained by differentiation (wherever $F$ is differentiable):

$$f(x) = \frac{d}{dx} F(x) = F'(x)$$

## Unified View: Discrete and Continuous

| | Discrete | Continuous |
|---|---|---|
| Distribution function | PMF: $p_{x_i}$ | PDF: $f(x)$ |
| CDF formula | $F(x) = \displaystyle\sum_{x_i \le x} p_{x_i}$ | $F(x) = \displaystyle\int_{-\infty}^{x} f(s) \, ds$ |
| Recover distribution | $p_{x_i} = F(x_i) - F(x_i^-)$ | $f(x) = F'(x)$ |
| $P(X \in A)$ | $\displaystyle\sum_{x_i \in A} p_{x_i}$ | $\displaystyle\int_A f(x) \, dx$ |

## Example

Let $f(x) = 2x$ for $0 \le x \le 1$ and $f(x) = 0$ otherwise. Then:

$$F(x) = \int_0^x 2s \, ds = x^2, \quad 0 \le x \le 1$$

and $F(x) = 0$ for $x < 0$, $F(x) = 1$ for $x > 1$.

We can verify: $F'(x) = 2x = f(x)$ on $(0,1)$.
