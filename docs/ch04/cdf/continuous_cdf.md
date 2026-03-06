# CDF for Continuous Random Variables

## Formula

For a continuous random variable $X$ with PDF $f(x)$, the CDF is:

$$F(x) = P(X \le x) = \int_{-\infty}^{x} f(s) \, ds$$

## Shape of Continuous CDFs

The CDF of a continuous random variable is a **continuous, non-decreasing function** (no jumps), which implies:

$$P(X = a) = F(a) - F(a^-) = 0$$

for every $a$. That is, no single point carries positive probability.

## Relationship to the PDF

By the Fundamental Theorem of Calculus, wherever $f$ is continuous:

$$f(x) = F'(x) = \frac{d}{dx} F(x)$$

The PDF is the derivative of the CDF.

## Computing Probabilities

$$P(a \le X \le b) = P(a < X < b) = F(b) - F(a) = \int_a^b f(x) \, dx$$

For continuous random variables, strict and non-strict inequalities give the same probability since $P(X = a) = 0$.

## Example: Uniform on [0, 1]

For $X \sim \text{Uniform}(0,1)$, $f(x) = 1$ on $[0,1]$, so:

$$F(x) = \begin{cases} 0 & x < 0 \\ x & 0 \le x \le 1 \\ 1 & x > 1 \end{cases}$$
