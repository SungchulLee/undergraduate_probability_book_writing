# PMF Definition and Properties


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

The **probability mass function (PMF)** of a discrete random variable $X$ assigns a probability to each possible value:

$$p_{x_i} = P(X = x_i) = \text{Weight of the brick attached to } x_i$$

## Properties

A valid PMF must satisfy:

1. **Non-negativity:** $p_{x_i} \ge 0$ for all $i$.
2. **Normalization:** $\displaystyle\sum_i p_{x_i} = 1$.

Any function satisfying these two properties defines a valid discrete distribution.

## Computing Probabilities from the PMF

For any set $A \subseteq \mathbb{R}$:

$$P(X \in A) = \sum_{x_i \in A} p_{x_i}$$

## Visualization

The PMF is typically displayed as a bar chart or spike plot, where the height of each bar at $x_i$ equals $P(X = x_i)$.

## Example

**Fair die.** Let $X$ be the result of rolling a fair six-sided die. The PMF is:

$$p_k = P(X = k) = \frac{1}{6}, \quad k = 1, 2, 3, 4, 5, 6$$

**Verification:** $\sum_{k=1}^{6} \frac{1}{6} = 1$ ✓
