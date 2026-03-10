# Recovering Joint from Conditional and Marginal


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## The Chain Rule for Distributions

The **chain rule** (also called the **multiplication rule**) allows us to construct the joint distribution from a marginal and a conditional:

$$p(x, y) = p(x) \cdot p(y \mid x)$$

or equivalently:

$$p(x, y) = p(y) \cdot p(x \mid y)$$

In the continuous case:

$$f(x, y) = f_X(x) \cdot f_{Y|X}(y \mid x) = f_Y(y) \cdot f_{X|Y}(x \mid y)$$

## Why This Matters

In many real-world problems, the joint distribution is not directly available, but we can naturally specify a marginal and a conditional. The chain rule lets us reconstruct the joint.

## Example: Sampling Without Replacement

There are 3 red balls and 1 blue ball. We draw two balls without replacement.

Let $X_1 = 1$ if the first ball is blue (0 otherwise), and $X_2 = 1$ if the second ball is blue.

**Marginal of $X_1$:**

$$P(X_1 = 0) = \frac{3}{4}, \quad P(X_1 = 1) = \frac{1}{4}$$

**Conditional of $X_2$ given $X_1$:**

$$P(X_2 = 1 \mid X_1 = 0) = \frac{1}{3}, \quad P(X_2 = 0 \mid X_1 = 0) = \frac{2}{3}$$

$$P(X_2 = 1 \mid X_1 = 1) = 0, \quad P(X_2 = 0 \mid X_1 = 1) = 1$$

**Recovering the joint via chain rule:**

$$P(X_1 = 0, X_2 = 1) = P(X_1 = 0) \cdot P(X_2 = 1 \mid X_1 = 0) = \frac{3}{4} \times \frac{1}{3} = \frac{1}{4}$$

$$P(X_1 = 0, X_2 = 0) = \frac{3}{4} \times \frac{2}{3} = \frac{1}{2}$$

$$P(X_1 = 1, X_2 = 0) = \frac{1}{4} \times 1 = \frac{1}{4}$$

$$P(X_1 = 1, X_2 = 1) = \frac{1}{4} \times 0 = 0$$

## Extension to Multiple Variables

The chain rule extends to $n$ variables:

$$p(x_1, x_2, \ldots, x_n) = p(x_1) \cdot p(x_2 \mid x_1) \cdot p(x_3 \mid x_1, x_2) \cdots p(x_n \mid x_1, \ldots, x_{n-1})$$

This is the foundation of sequential modeling and Bayesian networks.

## Connection to Bayes' Theorem

Combining both forms of the chain rule:

$$p(x) \cdot p(y \mid x) = p(x, y) = p(y) \cdot p(x \mid y)$$

Rearranging gives **Bayes' theorem**:

$$p(x \mid y) = \frac{p(y \mid x) \cdot p(x)}{p(y)}$$
