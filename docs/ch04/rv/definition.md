# Definition and Examples of Random Variables

<<<<<<< Updated upstream
## Why Random Variables?

In Chapters 2 and 3 we worked with events --- subsets of a sample space $\Omega$.
That framework is flexible, but many probability questions boil down to a single
number: "How many heads?", "What is the total?", "How long until failure?"
A **random variable** gives us a systematic way to attach a number to every
outcome, translating probability problems from abstract sets into questions
about numbers on the real line where we can use the full power of calculus and
algebra.

## Random Variable as a Function

!!! info "Definition — Random Variable"
    A **random variable** is a function

    $$
    X : \Omega \longrightarrow \mathbb{R}
    $$

    that assigns a real number $X(\omega)$ to every outcome $\omega \in \Omega$.

The notation $X(\omega)$ emphasizes that a random variable is a function of the
outcome, not a fixed number. Once the experiment is performed and the outcome
$\omega$ is determined, $X(\omega)$ becomes a definite real number.

## Distribution of a Random Variable

The **distribution** of $X$ describes how probability mass is spread across the
real line. A helpful mental picture is the "brick" analogy:

- Imagine a brick attached to each outcome $\omega \in \Omega$, with weight equal to $P(\{\omega\})$.
- The function $X$ moves each brick from $\omega$ to the point $X(\omega)$ on $\mathbb{R}$.
- After moving all bricks, the total weight on $\mathbb{R}$ is 1.
- The resulting weight distribution over $\mathbb{R}$ is the **distribution of $X$**.

Using this picture:

$$
P(X = a) = \text{total weight of the bricks that land at } a
$$

$$
P(X \in A) = \text{total weight of the bricks that land in } A
$$

where $A$ is any subset of $\mathbb{R}$.

## Examples

**Example 1 (Coin Flips).** Flip a fair coin three times. The sample space is

$$
\Omega = \{HHH,\; HHT,\; HTH,\; HTT,\; THH,\; THT,\; TTH,\; TTT\}
$$

Let $X$ = number of heads in the first two flips and $Y$ = total number of heads.
Then $X(HTH) = 1$ and $Y(HTH) = 2$. Both $X$ and $Y$ are random variables on the
same sample space, but they assign different numbers to the same outcome.

**Example 2 (Die Roll).** Roll a fair die once and let $X$ be the number shown.
Then $X$ takes values in $\{1, 2, 3, 4, 5, 6\} \subset \mathbb{R}$ with

$$
P(X = k) = \frac{1}{6}, \quad k = 1, 2, 3, 4, 5, 6
$$

From this we can compute, for instance,

$$
P(X \geq 5) = P(X = 5) + P(X = 6) = \frac{1}{6} + \frac{1}{6} = \frac{1}{3}
$$

**Example 3 (Lifetime of a Component).** Let $X$ denote the time (in hours)
until a light bulb fails. Here $X$ takes values in $[0, \infty)$ and is a
continuous random variable --- no single point carries positive probability.

!!! tip "Key Takeaway"
    A random variable converts an abstract probability experiment into a numerical quantity. Everything we do in Chapters 4 through 9 --- PMFs, CDFs, PDFs, expectation, variance --- builds on this idea.
=======
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
>>>>>>> Stashed changes
