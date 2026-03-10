# Conditional Probability Definition


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

The **conditional probability** of event $B$ given event $A$ is defined as

$$
P(B \mid A) = \frac{P(AB)}{P(A)}, \quad P(A) > 0
$$

This measures the probability that $B$ occurs, given that we know $A$ has occurred. Here $P(AB) = P(A \cap B)$ denotes the probability of both $A$ and $B$ occurring.

## Intuition

Conditioning on $A$ effectively **restricts the sample space** from $\Omega$ to $A$. Within this reduced sample space, the conditional probability asks: what fraction of $A$ also belongs to $B$?

If we think of probability as a measure of the "size" of events, then $P(B \mid A)$ is the ratio of the size of $AB$ to the size of $A$.

## Conditional Probability as a Probability Measure

A crucial fact is that $P(\cdot \mid B)$ is itself a valid probability measure. It satisfies all the axioms and properties that the usual probability measure $P(\cdot)$ satisfies. To convert any probability identity or inequality into its conditional version, you simply **add $\mid B$ before the closing parenthesis**.

Specifically, $P(\cdot \mid B)$ satisfies:

**(1) Normalization:**

$$
P(\Omega \mid B) = 1, \quad P(\emptyset \mid B) = 0
$$

**(2) Bounded:**

$$
0 \le P(A \mid B) \le 1 \quad \text{for any event } A
$$

**(3) Countable additivity:**

$$
P\!\left(\bigcup_{i=1}^{\infty} A_i \;\middle|\; B\right) = \sum_{i=1}^{\infty} P(A_i \mid B) \quad \text{for disjoint } A_i
$$

**(4) Finite additivity:**

$$
P\!\left(\bigcup_{i=1}^{n} A_i \;\middle|\; B\right) = \sum_{i=1}^{n} P(A_i \mid B) \quad \text{for disjoint } A_i
$$

**(5) Monotonicity:**

$$
P(A_1 \mid B) \le P(A_2 \mid B) \quad \text{for } A_1 \subset A_2
$$

**(6) Complement rule:**

$$
P(A^c \mid B) = 1 - P(A \mid B)
$$

**(7) Inclusion–exclusion (all forms):**

$$
P\!\left(\bigcup_{i=1}^{n} A_i \;\middle|\; B\right) \le \sum_{i=1}^{n} P(A_i \mid B)
$$

$$
P\!\left(\bigcup_{i=1}^{n} A_i \;\middle|\; B\right) \ge \sum_{i=1}^{n} P(A_i \mid B) - \sum_{1 \le i < j \le n} P(A_i A_j \mid B)
$$

$$
P\!\left(\bigcup_{i=1}^{n} A_i \;\middle|\; B\right) = \sum_{i=1}^{n} P(A_i \mid B) - \sum_{1 \le i < j \le n} P(A_i A_j \mid B) + \cdots + (-1)^{n+1} P(A_1 A_2 \cdots A_n \mid B)
$$

## Example — Double Ace

We choose two cards from an ordinary 52-card deck. Define:

| Event | Description |
|-------|-------------|
| $A$ | An ace is chosen (at least one ace among the two cards) |
| $A_1$ | The spade ace is chosen |
| $B$ | Both cards are aces |

**Calculate $P(B \mid A_1)$ and $P(B \mid A)$.**

### Computing P(B | A1)

Suppose the spade ace is chosen. Then there are 51 cards remaining, and to have both cards be aces we must choose the diamond, heart, or club ace. So

$$
P(B \mid A_1) = \frac{3}{51} = 0.0588
$$

### Computing P(B | A)

Since $B \subset A$ (both aces implies at least one ace), we have $P(AB) = P(B)$:

$$
P(B \mid A) = \frac{P(AB)}{P(A)} = \frac{P(B)}{P(A)} = \frac{P(B)}{1 - P(A^c)}
$$

The probability that no ace is chosen is $P(A^c) = \binom{48}{2}/\binom{52}{2}$, and $P(B) = \binom{4}{2}/\binom{52}{2}$, so

$$
P(B \mid A) = \frac{\binom{4}{2}/\binom{52}{2}}{1 - \binom{48}{2}/\binom{52}{2}} = 0.0303
$$

!!! note "Observation"
    Knowing a *specific* ace (the spade ace) was chosen gives a higher probability of both aces ($0.0588$) than merely knowing *some* ace was chosen ($0.0303$). This is because the event $A_1$ is more specific (and smaller) than $A$, concentrating the conditional probability on outcomes where a second ace is more likely.
