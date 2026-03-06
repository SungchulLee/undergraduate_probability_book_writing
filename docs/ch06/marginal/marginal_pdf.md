# Marginal PDF from Joint PDF

## Definition

Given the joint PDF $f(x, y)$ of continuous random variables $(X, Y)$, the **marginal PDF** of $X$ is:

$$f_X(x) = \int_{-\infty}^{\infty} f(x, y) \, dy$$

Similarly, the marginal PDF of $Y$ is:

$$f_Y(y) = \int_{-\infty}^{\infty} f(x, y) \, dx$$

## Interpretation

Marginalization integrates out the unwanted variable. Geometrically, the marginal density $f_X(x)$ at a point $x$ is the total "mass" along the vertical line at $x$, obtained by integrating the joint density along that line.

## Example: Uniform on the Triangle

Let $(X, Y)$ be uniform on the triangle $\{(x,y) : 0 \le x \le 1, \, 0 \le y \le x\}$.

The area of this triangle is \$1/2$, so the joint PDF is:

$$f(x, y) = 2, \quad 0 \le y \le x \le 1$$

The marginal PDF of $X$ is:

$$f_X(x) = \int_0^x 2 \, dy = 2x, \quad 0 \le x \le 1$$

The marginal PDF of $Y$ is:

$$f_Y(y) = \int_y^1 2 \, dx = 2(1 - y), \quad 0 \le y \le 1$$

## Continuous Analogue of the Table

The discrete "sum rows / sum columns" procedure corresponds to integration in the continuous case:

| Operation | Discrete | Continuous |
|---|---|---|
| Marginal of $X$ | $p_X(x) = \sum_y p(x,y)$ | $f_X(x) = \int f(x,y) \, dy$ |
| Marginal of $Y$ | $p_Y(y) = \sum_x p(x,y)$ | $f_Y(y) = \int f(x,y) \, dx$ |

!!! tip "Key Point"
    When computing marginal PDFs, the limits of integration must respect the support of the joint PDF. These limits often depend on the variable being kept.
