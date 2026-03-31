# PDF Definition and Properties
<<<<<<< Updated upstream

## Motivation

For a discrete random variable, the PMF tells us the probability of each value
directly: $P(X = x_i) = p_X(x_i)$. For a continuous random variable, however,
$P(X = a) = 0$ for every individual point $a$. Instead of asking "what is the
probability of this exact value?", we ask "how densely is probability packed
near this point?" The answer is the **probability density function (PDF)**.

## Definition

!!! info "Definition — Probability Density Function"
    A continuous random variable $X$ has **probability density function (PDF)**
    $f_X(x)$ if, for every subset $A \subseteq \mathbb{R}$,

    $$
    P(X \in A) = \int_A f_X(x) \, dx
    $$

The PDF describes the **density** of probability at each point, not the
probability itself. Thinking in terms of the brick analogy, the bricks are now
ground into a continuous layer of sand, and $f_X(x)$ measures how thickly the
sand is spread at position $x$.

## Properties

A valid PDF must satisfy two conditions:

!!! info "PDF Properties"
    1. **Non-negativity:** $f_X(x) \ge 0$ for all $x$
    2. **Normalization:** $\displaystyle\int_{-\infty}^{\infty} f_X(x) \, dx = 1$

These are the continuous analogues of the PMF properties (non-negativity and
summation to 1).

!!! warning "A PDF Value Is Not a Probability"
    The value $f_X(x)$ can exceed 1. For example, if
    $X \sim \text{Uniform}(0, 1/2)$, then $f_X(x) = 2$ for $x \in [0, 1/2]$.
    Only the **integral** of $f_X$ over an interval gives a probability, and
    that integral is always at most 1.

## Probability from the PDF

For an interval $[a, b]$:

$$
P(a \le X \le b) = \int_a^b f_X(x) \, dx
$$
=======

## Definition

The **probability density function (PDF)** of a continuous random variable $X$ is a function $f(x)$ such that:

$$P(X \in A) = \int_A f(x) \, dx$$

Using the brick analogy:

$$f(x) \, dx = \text{Weight of the bricks in } [x, x + dx]$$

The PDF represents the **density** of probability at each point, not the probability itself.

## Properties
>>>>>>> Stashed changes

Geometrically, this is the **area under the PDF curve** between $a$ and $b$.

<<<<<<< Updated upstream
## Infinitesimal Interpretation

For a small increment $\epsilon > 0$:

$$
P(x \le X \le x + \epsilon) \approx f_X(x) \cdot \epsilon
$$

The PDF gives the probability per unit length near the point $x$. This
approximation becomes exact in the limit as $\epsilon \to 0$.

## Examples

**Example 1 (Uniform).** Let $X \sim \text{Uniform}(0, 1)$, so
$f_X(x) = 1$ for $0 \le x \le 1$ and $f_X(x) = 0$ otherwise. Then

$$
P(0.3 \le X \le 0.7) = \int_{0.3}^{0.7} 1 \, dx = 0.4
$$

**Example 2 (Triangular density).** Let $f_X(x) = 2x$ for $0 \le x \le 1$ and $f_X(x) = 0$ otherwise.

- Verification: $\int_0^1 2x \, dx = x^2 \big|_0^1 = 1$.
- Probability computation:

$$
P\!\left(X \le \frac{1}{2}\right) = \int_0^{1/2} 2x \, dx = x^2 \Big|_0^{1/2} = \frac{1}{4}
$$

Most of the probability is concentrated near $x = 1$ because the density is
increasing.

**Example 3 (Density exceeding 1).** Let $f_X(x) = 3$ for
$0 \le x \le 1/3$ and $f_X(x) = 0$ otherwise. Here $f_X(x) = 3 > 1$ on the
support, yet $\int_0^{1/3} 3 \, dx = 1$, confirming this is a valid PDF.
=======
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
>>>>>>> Stashed changes
