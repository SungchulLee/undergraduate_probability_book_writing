# Tree Diagrams

## Overview

A **tree diagram** is a visual tool for organizing and computing probabilities involving sequential events. Each branch represents a possible outcome at a stage, and the probability of a complete path is the product of the probabilities along its branches (by the chain rule).

## Structure of a Tree Diagram

A tree diagram has the following components:

- **Root node:** The starting point representing the initial state.
- **Branches:** Each branch from a node represents one possible outcome at that stage, labeled with its (conditional) probability.
- **Leaf nodes:** The endpoints representing complete outcomes.
- **Path probability:** The probability of reaching a leaf is the product of all branch probabilities along the path from root to leaf.

## Connection to the Chain Rule

For a two-stage experiment with first outcome $A_i$ and second outcome $B_j$:

$$
P(A_i \cap B_j) = P(A_i) \cdot P(B_j \mid A_i)
$$

The first-level branches carry $P(A_i)$, and the second-level branches carry $P(B_j \mid A_i)$.

## Connection to Total Probability

The total probability of an event $B_j$ is obtained by **summing over all paths** that lead to $B_j$:

$$
P(B_j) = \sum_{i} P(A_i)\,P(B_j \mid A_i)
$$

This is precisely the law of total probability, visualized as collecting all leaf nodes corresponding to $B_j$.

## Example — Dependent Events (Drawing Without Replacement)

A bag contains 2 green marbles and 1 purple marble. Draw two marbles without replacement.

**Tree structure:**

- **First draw:** $P(\text{Green}) = 2/3$, $\;P(\text{Purple}) = 1/3$
- **Second draw (given first was Green):** $P(\text{Green}) = 1/2$, $\;P(\text{Purple}) = 1/2$
- **Second draw (given first was Purple):** $P(\text{Green}) = 2/2 = 1$, $\;P(\text{Purple}) = 0$

**Path probabilities:**

| Path | Probability |
|------|-------------|
| Green, Green | $(2/3)(1/2) = 1/3$ |
| Green, Purple | $(2/3)(1/2) = 1/3$ |
| Purple, Green | $(1/3)(1) = 1/3$ |

The probability of getting a green marble on the second draw **depends** on the first draw — this is a dependent experiment.

## Example — Independent Events (Drawing With Replacement)

Same bag (2 green, 1 purple), but now replace the first marble before drawing the second.

**Tree structure:**

- **First draw:** $P(\text{Green}) = 2/3$, $\;P(\text{Purple}) = 1/3$
- **Second draw (regardless of first):** $P(\text{Green}) = 2/3$, $\;P(\text{Purple}) = 1/3$

**Path probabilities:**

| Path | Probability |
|------|-------------|
| Green, Green | $(2/3)(2/3) = 4/9$ |
| Green, Purple | $(2/3)(1/3) = 2/9$ |
| Purple, Green | $(1/3)(2/3) = 2/9$ |
| Purple, Purple | $(1/3)(1/3) = 1/9$ |

The probability of getting a green marble on the second draw does **not** depend on the first draw — the draws are independent.

## Example — False Positive (Medical Testing)

A blood test is 95% effective in detecting a certain disease when present. The test yields a false positive for 1% of healthy persons. If 0.01% of the population has the disease, what is $P(D \mid d)$?

### Events

| Event | Description |
|-------|-------------|
| $H$ | Person is healthy |
| $D$ | Person has the disease |
| $h$ | Test reports healthy |
| $d$ | Test reports disease (positive) |

### Given Information

| Probability | Value | Meaning |
|-------------|-------|---------|
| $P(d \mid D)$ | $0.95$ | Test sensitivity (true positive rate) |
| $P(h \mid D)$ | $0.05$ | False negative rate |
| $P(d \mid H)$ | $0.01$ | False positive rate |
| $P(h \mid H)$ | $0.99$ | True negative rate |
| $P(D)$ | $0.0001$ | Disease prevalence |
| $P(H)$ | $0.9999$ | Proportion healthy |

### Tree Diagram Computation

**Level 1 (Health status):** Branch into $D$ and $H$ with probabilities $0.0001$ and $0.9999$.

**Level 2 (Test result):** From each health status, branch into $d$ and $h$.

**Paths leading to positive test result $d$:**

$$
P(D \cap d) = P(D)\,P(d \mid D) = (0.0001)(0.95) = 0.000095
$$

$$
P(H \cap d) = P(H)\,P(d \mid H) = (0.9999)(0.01) = 0.009999
$$

### Applying Bayes' Rule with Total Probability

$$
P(D \mid d) = \frac{P(D)\,P(d \mid D)}{P(D)\,P(d \mid D) + P(H)\,P(d \mid H)} = \frac{(0.0001)(0.95)}{(0.0001)(0.95) + (0.9999)(0.01)} = 0.0094
$$

!!! warning "Surprising Result"
    Even with a 95% accurate test, a positive result only means a **0.94% chance** of actually having the disease. The overwhelming number of healthy people (99.99% of the population) generates far more false positives than the tiny number of sick people generates true positives. This is why rare-disease screening often requires confirmatory testing.
