# CDF for Continuous Random Variables

## Motivation

In Section 4.3, we defined the CDF $F(x) = P(X \le x)$ for any random variable
and saw that a discrete CDF is a step function with jumps at each possible
value. For a continuous random variable the situation is different: probability
is spread smoothly across an interval, so the CDF has **no jumps** and is
obtained by integrating the PDF.

## CDF via Integration

!!! info "Continuous CDF"
    If $X$ is a continuous random variable with PDF $f(x)$, then its CDF is

    $$
    F(x) = P(X \le x) = \int_{-\infty}^{x} f(s) \, ds
    $$

The dummy variable $s$ is used inside the integral to avoid confusion with the
upper limit $x$.

## Shape of Continuous CDFs

Because $F$ is defined as an integral of a non-negative function, every
continuous CDF is a **continuous, non-decreasing** curve --- unlike the staircase
pattern of a discrete CDF. In particular, there are no jumps, which means

$$
P(X = a) = F(a) - \lim_{x \to a^-} F(x) = 0
$$

for every real number $a$. No single point carries positive probability.

## Recovering the PDF

By the Fundamental Theorem of Calculus, wherever $f$ is continuous we can
recover the PDF from the CDF by differentiation:

$$
f(x) = F'(x) = \frac{d}{dx} F(x)
$$

This is the continuous analogue of recovering the PMF from a discrete CDF via
jump sizes.

## Computing Probabilities

For continuous random variables, strict and non-strict inequalities give the
same result because $P(X = a) = 0$:

$$
P(a \le X \le b) = P(a < X < b) = F(b) - F(a) = \int_a^b f(x) \, dx
$$

!!! tip "Strict vs Non-Strict Inequalities"
    For discrete random variables, $P(X \le b)$ and $P(X < b)$ can differ.
    For continuous random variables, they are always equal.

## Example: Uniform on the Unit Interval

Let $X \sim \text{Uniform}(0, 1)$, so $f(x) = 1$ for $0 \le x \le 1$ and
$f(x) = 0$ otherwise. Integrating:

$$
F(x) = \begin{cases} 0 & x < 0 \\ x & 0 \le x \le 1 \\ 1 & x > 1 \end{cases}
$$

For instance, $P(0.2 \le X \le 0.7) = F(0.7) - F(0.2) = 0.7 - 0.2 = 0.5$.

## Example: Quadratic PDF

Let $f(x) = 3x^2$ for $0 \le x \le 1$ and $f(x) = 0$ otherwise. Then

$$
F(x) = \int_0^x 3s^2 \, ds = x^3, \quad 0 \le x \le 1
$$

with $F(x) = 0$ for $x < 0$ and $F(x) = 1$ for $x > 1$. Verification:
$F'(x) = 3x^2 = f(x)$ on $(0, 1)$.

We can compute $P(X > 0.5) = 1 - F(0.5) = 1 - 0.125 = 0.875$.
