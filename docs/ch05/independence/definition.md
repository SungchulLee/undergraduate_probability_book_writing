# Definition of Independence for Random Variables

## From Events to Random Variables

In Chapter 3, two events $A$ and $B$ are independent when $P(A \cap B) = P(A) \, P(B)$. Independence for random variables extends this idea: knowing the value of one variable provides no information about the other. The formal definition requires the factorization condition to hold for **every** pair of values simultaneously.

## Independence of Two Discrete Random Variables

!!! info "Definition"
    Discrete random variables $X$ and $Y$ are **independent** if for all $x$ and $y$:

    $$p_{X,Y}(x, y) = p_X(x) \cdot p_Y(y)$$

    That is, the joint PMF factors into the product of the marginal PMFs at every point.

If even a single pair $(x, y)$ violates this equation, then $X$ and $Y$ are **dependent**.

**Example.** Roll two fair dice independently. Let $X$ be the result of the first die and $Y$ the result of the second. Then $p_X(x) = 1/6$ for $x \in \{1,\ldots,6\}$ and $p_Y(y) = 1/6$ for $y \in \{1,\ldots,6\}$. Every entry of the joint PMF equals

$$p_{X,Y}(x,y) = \frac{1}{36} = \frac{1}{6} \cdot \frac{1}{6} = p_X(x) \cdot p_Y(y)$$

so $X$ and $Y$ are independent.

## Independence of Two Continuous Random Variables

!!! info "Definition"
    Continuous random variables $X$ and $Y$ are **independent** if for all $x$ and $y$:

    $$f_{X,Y}(x, y) = f_X(x) \cdot f_Y(y)$$

    That is, the joint PDF factors into the product of the marginal PDFs everywhere.

## General Definition via CDFs

The most general definition covers both discrete, continuous, and mixed cases.

!!! info "Definition"
    Random variables $X$ and $Y$ are **independent** if for all $x$ and $y$:

    $$F_{X,Y}(x, y) = F_X(x) \cdot F_Y(y)$$

    Equivalently, $P(X \le x, \, Y \le y) = P(X \le x) \, P(Y \le y)$ for all $x, y \in \mathbb{R}$.

## Independence of Multiple Random Variables

Random variables $X_1, X_2, \ldots, X_n$ are **(mutually) independent** if the joint distribution factors into the product of all marginals. In the discrete case, this means for all $x_1, x_2, \ldots, x_n$:

$$p_{X_1, \ldots, X_n}(x_1, \ldots, x_n) = p_{X_1}(x_1) \cdot p_{X_2}(x_2) \cdots p_{X_n}(x_n)$$

Mutual independence is a strong requirement: it demands that **every** sub-collection of the variables is also independent, not just each pair.

## Pairwise vs Mutual Independence

$X_1, X_2, \ldots, X_n$ are **pairwise independent** if every pair $X_i, X_j$ (with $i \ne j$) is independent.

!!! warning "Pairwise does not imply mutual"
    Pairwise independence is strictly weaker than mutual independence.

**Counterexample.** Let $X_1$ and $X_2$ be independent fair coin flips taking values $0$ or $1$, and define $X_3 = X_1 \oplus X_2$ (addition mod 2). Then:

- Each $X_i$ is $\text{Bernoulli}(1/2)$.
- Any pair $(X_i, X_j)$ is independent: for instance, $P(X_1 = a, X_3 = b) = 1/4$ for all $a, b \in \{0,1\}$.
- But the three variables are **not** mutually independent because $X_3$ is completely determined by $X_1$ and $X_2$.

## Checking Independence via Conditional Distributions

An equivalent characterization: $X$ and $Y$ are independent if and only if the conditional distribution of $X$ given $Y = y$ does not depend on $y$. In the discrete case:

$$p_{X \mid Y}(x \mid y) = p_X(x) \quad \text{for all } x, y$$

Intuitively, learning the value of $Y$ tells us nothing new about $X$.

## Conditional Independence

$X_1, \ldots, X_n$ are **conditionally independent given** $Y$ if, for all $x_1, \ldots, x_n$ and $y$:

$$p_{X_1, \ldots, X_n \mid Y}(x_1, \ldots, x_n \mid y) = p_{X_1 \mid Y}(x_1 \mid y) \cdot p_{X_2 \mid Y}(x_2 \mid y) \cdots p_{X_n \mid Y}(x_n \mid y)$$

!!! note "Independence and conditional independence are separate properties"
    Conditional independence given $Y$ does **not** imply unconditional independence, and unconditional independence does **not** imply conditional independence given $Y$. The two concepts must be checked separately.
