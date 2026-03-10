# PDF Definition and Properties


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

The **probability density function (PDF)** of a continuous random variable $X$ is a function $f(x)$ such that:

$$P(X \in A) = \int_A f(x) \, dx$$

Using the brick analogy:

$$f(x) \, dx = \text{Weight of the bricks in } [x, x + dx]$$

The PDF represents the **density** of probability at each point, not the probability itself.

## Properties

A valid PDF must satisfy:

1. **Non-negativity:** $f(x) \ge 0$ for all $x$.
2. **Normalization:** $\displaystyle\int_{-\infty}^{\infty} f(x) \, dx = 1$.

!!! warning "Important"
    $f(x)$ is **not** a probability. It is a density, and $f(x)$ can exceed 1. For example, $X \sim \text{Uniform}(0, 1/2)$ has $f(x) = 2$ on $[0, 1/2]$.

## Probability from the PDF

For an interval $[a, b]$:

$$P(a \le X \le b) = \int_a^b f(x) \, dx$$

This is the area under the PDF curve between $a$ and $b$.

## Infinitesimal Interpretation

For small $\epsilon > 0$:

$$P(x \le X \le x + \epsilon) \approx f(x) \cdot \epsilon$$

The PDF gives the probability per unit length near $x$.
