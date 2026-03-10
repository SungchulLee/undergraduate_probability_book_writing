# From Joint to Marginal and Conditional


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## The Three Fundamental Relationships

Given the joint distribution $p(x, y)$, we can derive both the marginal and conditional distributions. Conversely, given a marginal and a conditional, we can recover the joint.

### Chain Rule (Joint from Marginal and Conditional)

$$p(x, y) = p(x) \cdot p(y \mid x) = p(y) \cdot p(x \mid y)$$

### Marginalization (Marginal from Joint)

$$p(x) = \sum_y p(x, y) \qquad \text{(discrete)}$$

$$f_X(x) = \int f(x, y) \, dy \qquad \text{(continuous)}$$

### Conditioning (Conditional from Joint)

$$p(y \mid x) = \frac{p(x, y)}{p(x)} \qquad p(x \mid y) = \frac{p(x, y)}{p(y)}$$

## How to Get Any Two from the Third

Given **any two** of the three — joint, marginal, conditional — you can recover the third:

| Known | Want | Formula |
|---|---|---|
| Joint $p(x,y)$ | Marginal $p(x)$ | $\sum_y p(x,y)$ |
| Joint $p(x,y)$ | Conditional $p(y \mid x)$ | $p(x,y) / p(x)$ |
| Marginal $p(x)$ + Conditional $p(y \mid x)$ | Joint $p(x,y)$ | $p(x) \cdot p(y \mid x)$ |

## Complete Worked Example

Starting from the joint PMF:

| | $x=0$ | $x=1$ | $x=2$ |
|---|---|---|---|
| $y=3$ | $1/10$ | $1/10$ | $1/10$ |
| $y=2$ | $1/10$ | $0$ | $1/10$ |
| $y=1$ | $0$ | $2/10$ | $1/10$ |
| $y=0$ | $1/10$ | $0$ | $1/10$ |

**Step 1 — Marginals (by summation):**

$P(X=0) = 3/10$, $P(X=1) = 3/10$, $P(X=2) = 4/10$

$P(Y=0) = 2/10$, $P(Y=1) = 3/10$, $P(Y=2) = 2/10$, $P(Y=3) = 3/10$

**Step 2 — Conditional of $X$ given $Y=1$ (slice and normalize):**

$P(X=0 \mid Y=1) = 0$, $P(X=1 \mid Y=1) = 2/3$, $P(X=2 \mid Y=1) = 1/3$

**Step 3 — Conditional of $Y$ given $X=2$ (slice and normalize):**

$P(Y=y \mid X=2) = 1/4$ for $y = 0, 1, 2, 3$ (uniform)

**Step 4 — Verify the chain rule:**

$p(1, 1) = P(X=1) \cdot P(Y=1 \mid X=1) = \frac{3}{10} \cdot \frac{2/10}{3/10} = \frac{3}{10} \cdot \frac{2}{3} = \frac{2}{10}$ ✓
