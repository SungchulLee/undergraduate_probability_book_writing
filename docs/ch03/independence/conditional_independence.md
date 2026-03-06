# Conditional Independence

## Definition

Events $A_1, A_2, \ldots, A_n$ are **conditionally independent given $B$** if for every subcollection $A_{i_1}, A_{i_2}, \ldots, A_{i_m}$ (with $2 \le m \le n$):

$$

P(A_{i_1} A_{i_2} \cdots A_{i_m} \mid B) = P(A_{i_1} \mid B)\,P(A_{i_2} \mid B) \cdots P(A_{i_m} \mid B)

$$

In other words, once we condition on $B$, the events behave as if they are independent within the reduced probability space defined by $B$.

## For Two Events

$A$ and $C$ are conditionally independent given $B$ if:

$$

P(AC \mid B) = P(A \mid B)\,P(C \mid B)

$$

Equivalently (when $P(C \cap B) > 0$):

$$

P(A \mid B, C) = P(A \mid B)

$$

Once $B$ is known, additional knowledge of $C$ provides no further information about $A$.

## Independence does not imply Conditional Independence

A crucial point: **independence and conditional independence are different properties**. Neither implies the other.

### Independent but Not Conditionally Independent

**Example:** Toss a fair coin twice. Let $A$ = "first toss is heads," $C$ = "second toss is heads," and $B$ = "exactly one head." Then $A$ and $C$ are independent, but given $B$ (exactly one head), knowing $A$ occurred means $C$ did not — so $A$ and $C$ are not conditionally independent given $B$.

### Conditionally Independent but Not Independent

**Example:** Suppose a bag is chosen at random: Bag 1 has 2 red and 1 blue ball; Bag 2 has 1 red and 2 blue balls. Two draws are made with replacement from the chosen bag. Let $A_1$ = "first draw is red" and $A_2$ = "second draw is red." Given which bag was chosen ($B$), the draws are conditionally independent. However, $A_1$ and $A_2$ are not (marginally) independent, because observing $A_1$ = red makes it more likely Bag 1 was chosen, which in turn makes $A_2$ = red more likely.

## Conditional Independence in Practice

Conditional independence is a foundational concept in:

- **Bayesian networks:** Nodes are conditionally independent of their non-descendants given their parents.
- **Naive Bayes classifier:** Features are assumed conditionally independent given the class label.
- **Markov chains:** The future state is conditionally independent of the past given the present state.
- **Hidden Markov models:** Observations are conditionally independent given the hidden states.

## Joint, Marginal, and Conditional Probabilities

When the sample space $\Omega$ is decomposed two different ways:

$$

\Omega = \bigcup_{i=1}^{m} A_i \quad \text{(disjointly)} \qquad \text{and} \qquad \Omega = \bigcup_{j=1}^{n} B_j \quad \text{(disjointly)}

$$

we can organize probabilities into a table:

### Three Types of Probabilities

| Type | Notation | Description |
|------|----------|-------------|
| **Joint** | $P(A_i B_j)$ | Probability of both $A_i$ and $B_j$ |
| **Marginal** | $P(A_i)$, $P(B_j)$ | Row/column sums of the joint table |
| **Conditional** | $P(B_j \mid A_i)$ | Probability of $B_j$ given $A_i$ |

### Relationships (How to Obtain One from the Other Two)

Given any two of {joint, marginal, conditional}, you can recover the third:

**Chain rule (joint from marginal + conditional):**

$$

P(A_i B_j) = P(A_i)\,P(B_j \mid A_i)

$$

**Marginalization (marginal from joint):**

$$

P(A_i) = \sum_{j} P(A_i B_j)

$$

**Conditioning (conditional from joint + marginal):**

$$

P(B_j \mid A_i) = \frac{P(A_i B_j)}{P(A_i)}

$$
