# Definition and Examples of Random Variables


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Random Variable as a Function

A **random variable** is a function that maps outcomes from a sample space to the real numbers:

$$X : \Omega \longrightarrow \mathbb{R}$$

Each outcome $\omega \in \Omega$ is assigned a real number $X(\omega)$.

## Distribution of a Random Variable

The **distribution** of $X$ describes how probability mass is spread across the real line. Using the "brick" analogy:

- Imagine a brick attached to each outcome $\omega \in \Omega$, with weight equal to $P(\{\omega\})$.
- The function $X$ moves each brick from $\omega$ to the point $X(\omega)$ on the real line $\mathbb{R}$.
- After moving all bricks, the total weight on $\mathbb{R}$ is 1.
- This weight distribution over $\mathbb{R}$ is the **distribution of $X$**.

Formally:

$$P(X = a) = \text{Weight of the bricks at } a$$

$$P(X \in A) = \text{Weight of the bricks in } A$$

## Examples

**Example: Coin Flips.** Consider flipping a fair coin three times. Let $X$ denote the number of heads in the first two flips, and let $Y$ denote the total number of heads in all three flips. The sample space is $\Omega = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}$, and for instance $X(HTH) = 1$ and $Y(HTH) = 2$.

**Example: Die Roll.** Roll a fair die once and let $X$ be the number shown. Then $X : \Omega \to \{1, 2, 3, 4, 5, 6\}$ with $P(X = k) = 1/6$ for each $k$.

**Example: Lifetime of a Component.** Let $X$ denote the time until a light bulb fails. Here $X$ takes values in $[0, \infty)$ and is a continuous random variable.

## Why Random Variables Matter

Random variables allow us to translate probability problems from abstract sample spaces into questions about numbers on the real line, making it possible to use the full power of calculus and algebra.
