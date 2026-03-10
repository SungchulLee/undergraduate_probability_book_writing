# Definition of Independence for Random Variables


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Independence of Two Random Variables

Random variables $X$ and $Y$ are **independent** if for all $x$ and $y$:

$$p(x, y) = p(x) \cdot p(y)$$

Equivalently, the joint distribution factors into the product of the marginal distributions. This must hold for **every** pair of values, not just some.

## Independence of Multiple Random Variables

Random variables $X_1, X_2, \ldots, X_n$ are **(mutually) independent** if for all $x_1, x_2, \ldots, x_n$:

$$p(x_1, x_2, \ldots, x_n) = p(x_1) \cdot p(x_2) \cdots p(x_n)$$

## Pairwise Independence

$X_1, X_2, \ldots, X_n$ are **pairwise independent** if for every pair $X_i, X_j$ (with $i \ne j$):

$$X_i \text{ and } X_j \text{ are independent}$$

!!! warning "Important"
    Pairwise independence does **not** imply mutual independence in general. Mutual independence is a strictly stronger condition.

## Conditional Independence

$X_1, \ldots, X_n$ are **conditionally independent given $Y$** if for all $x_1, \ldots, x_n$ and $y$:

$$p(x_1, x_2, \ldots, x_n \mid y) = p(x_1 \mid y) \cdot p(x_2 \mid y) \cdots p(x_n \mid y)$$

!!! note
    Conditional independence given $Y$ does **not** imply (unconditional) independence, and vice versa.

## Checking Independence via Conditional Distributions

An equivalent way to check independence: $X$ and $Y$ are independent if and only if the conditional distribution of $X$ given $Y = y$ does not depend on $y$. That is:

$$p(x \mid y) = p(x) \quad \text{for all } x, y$$
