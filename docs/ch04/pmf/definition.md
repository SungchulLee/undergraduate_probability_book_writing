# PMF Definition and Properties
<<<<<<< Updated upstream

## Motivation

For a discrete random variable $X$, the most natural way to describe its
distribution is to list every possible value together with its probability.
This list is called the **probability mass function (PMF)**. In the brick
analogy from Section 4.1, the PMF records the weight of each brick after it has
been placed on the real line.

## Definition

!!! info "Definition — Probability Mass Function"
    Let $X$ be a discrete random variable taking values in a countable set
    $\{x_1, x_2, x_3, \ldots\}$. The **probability mass function (PMF)** of $X$
    is the function

    $$
    p_X(x_i) = P(X = x_i)
    $$

    that assigns a probability to each possible value $x_i$.

The subscript $X$ in $p_X$ emphasizes which random variable the PMF belongs to.
When the random variable is clear from context, we sometimes write $p(x_i)$ or
$p_{x_i}$.
=======

## Definition

The **probability mass function (PMF)** of a discrete random variable $X$ assigns a probability to each possible value:

$$p_{x_i} = P(X = x_i) = \text{Weight of the brick attached to } x_i$$

## Properties

A valid PMF must satisfy:

1. **Non-negativity:** $p_{x_i} \ge 0$ for all $i$.
2. **Normalization:** $\displaystyle\sum_i p_{x_i} = 1$.
>>>>>>> Stashed changes

## Properties

<<<<<<< Updated upstream
A valid PMF must satisfy two conditions:

!!! info "PMF Properties"
    1. **Non-negativity:** $p_X(x_i) \ge 0$ for all $i$
    2. **Normalization:** $\displaystyle\sum_{i} p_X(x_i) = 1$
=======
## Computing Probabilities from the PMF
>>>>>>> Stashed changes

Any function on a countable set satisfying these two properties defines a valid
discrete distribution. Conversely, every discrete distribution gives rise to a
PMF satisfying both properties.

## Computing Probabilities from the PMF

For any set $A \subseteq \mathbb{R}$, the probability that $X$ falls in $A$ is
obtained by summing the PMF over all values in $A$:

$$P(X \in A) = \sum_{x_i \in A} p_{x_i}$$

<<<<<<< Updated upstream
This is the discrete counterpart of integration for continuous distributions.

## Visualization

The PMF is typically displayed as a **spike plot** (or bar chart), where a
vertical bar at each $x_i$ has height equal to $P(X = x_i)$. The heights must
sum to 1.

## Examples

**Example 1 (Fair Die).** Let $X$ be the result of rolling a fair six-sided die. The PMF is

$$
p_X(k) = P(X = k) = \frac{1}{6}, \quad k = 1, 2, 3, 4, 5, 6
$$

Verification: $\sum_{k=1}^{6} \frac{1}{6} = 1$.

**Example 2 (Loaded Coin).** Flip a coin with $P(\text{Heads}) = 0.7$. Let $X = 1$ if heads, $X = 0$ if tails. Then

$$
p_X(0) = 0.3, \qquad p_X(1) = 0.7
$$

This is a Bernoulli PMF with parameter $p = 0.7$. Note that $0.3 + 0.7 = 1$.

**Example 3 (Number of Heads).** Flip a fair coin twice and let $X$ count the
number of heads. The possible values are $\{0, 1, 2\}$ with

| $x$ | 0 | 1 | 2 |
|:---:|:---:|:---:|:---:|
| $p_X(x)$ | $1/4$ | $1/2$ | $1/4$ |

From this PMF we can compute $P(X \geq 1) = p_X(1) + p_X(2) = \frac{1}{2} + \frac{1}{4} = \frac{3}{4}$.

!!! tip "PMF vs PDF"
    The PMF applies only to **discrete** random variables. For continuous random variables, the analogous object is the probability density function (PDF), introduced in Section 4.4. A key difference: $p_X(x_i)$ is a genuine probability, while the PDF value $f_X(x)$ is a density that can exceed 1.
=======
## Visualization

The PMF is typically displayed as a bar chart or spike plot, where the height of each bar at $x_i$ equals $P(X = x_i)$.

## Example

**Fair die.** Let $X$ be the result of rolling a fair six-sided die. The PMF is:

$$p_k = P(X = k) = \frac{1}{6}, \quad k = 1, 2, 3, 4, 5, 6$$

**Verification:** $\sum_{k=1}^{6} \frac{1}{6} = 1$ ✓
>>>>>>> Stashed changes
