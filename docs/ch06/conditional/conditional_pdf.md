# Conditional PDF


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

The **conditional PDF** of $X$ given $Y = y$ is:

$$f_{X|Y}(x \mid y) = \frac{f(x, y)}{f_Y(y)}$$

provided $f_Y(y) > 0$. Similarly:

$$f_{Y|X}(y \mid x) = \frac{f(x, y)}{f_X(x)}$$

## Interpretation

The conditional PDF is the continuous analogue of "slice and normalize":

- **Slice:** Fix $Y = y$ and look at the joint density along that horizontal line, giving the function $f(x, y)$ as a function of $x$ alone.
- **Normalize:** Divide by $f_Y(y)$ to ensure the result integrates to 1 over $x$.

## Verification

The conditional PDF must be a valid PDF:

$$\int_{-\infty}^{\infty} f_{X|Y}(x \mid y) \, dx = \int_{-\infty}^{\infty} \frac{f(x, y)}{f_Y(y)} \, dx = \frac{1}{f_Y(y)} \int_{-\infty}^{\infty} f(x, y) \, dx = \frac{f_Y(y)}{f_Y(y)} = 1$$

## Example: Uniform on the Triangle

For $(X, Y)$ uniform on $\{0 \le y \le x \le 1\}$ with $f(x, y) = 2$:

The marginal of $X$ is $f_X(x) = 2x$ for $0 \le x \le 1$.

The conditional PDF of $Y$ given $X = x$ is:

$$f_{Y|X}(y \mid x) = \frac{f(x, y)}{f_X(x)} = \frac{2}{2x} = \frac{1}{x}, \quad 0 \le y \le x$$

This is a Uniform$(0, x)$ distribution: given $X = x$, the variable $Y$ is uniformly distributed on $[0, x]$.

## Conditional Expectation (Preview)

Using the conditional PDF, the conditional expectation of $Y$ given $X = x$ is:

$$E[Y \mid X = x] = \int_{-\infty}^{\infty} y \, f_{Y|X}(y \mid x) \, dy$$

This is explored in depth in Chapter 8.
