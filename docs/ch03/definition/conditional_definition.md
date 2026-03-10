# Conditional Probability Definition

Conditional probability quantifies how the probability of an event changes when we learn that another event has occurred. It is one of the most important concepts in all of probability.

## Definition

The **conditional probability** of $B$ given $A$ (with $P(A) > 0$) is

$$
P(B \mid A) = \frac{P(A \cap B)}{P(A)}
$$

This measures the fraction of $A$ that also belongs to $B$. Conditioning on $A$ effectively restricts the sample space from $\Omega$ to $A$.

## Explanation

### Conditional Probability Is a Probability Measure

A crucial fact: $P(\cdot \mid B)$ satisfies all the Kolmogorov axioms. Every property of probability carries over — complement rule, inclusion-exclusion, monotonicity — simply by adding "$\mid B$" to every term. Specifically:

- $P(\Omega \mid B) = 1$, $\;P(\emptyset \mid B) = 0$
- $P(A^c \mid B) = 1 - P(A \mid B)$
- Finite/countable additivity holds for disjoint events
- $P(A_1 \cup A_2 \mid B) = P(A_1 \mid B) + P(A_2 \mid B) - P(A_1 \cap A_2 \mid B)$

This means you never need to re-derive results for conditional probabilities — every unconditional identity has a conditional counterpart.

## Examples

**Example (Double ace).** Draw 2 cards from a 52-card deck.

- $A$ = at least one ace, $A_1$ = spade ace is drawn, $B$ = both cards are aces.

**$P(B \mid A_1)$:** Given the spade ace is drawn, we need one of the 3 remaining aces from the 51 other cards:

$$
P(B \mid A_1) = \frac{3}{51} \approx 0.0588
$$

**$P(B \mid A)$:** Since $B \subset A$, we have $P(B \cap A) = P(B) = \binom{4}{2}/\binom{52}{2}$ and $P(A) = 1 - \binom{48}{2}/\binom{52}{2}$:

$$
P(B \mid A) = \frac{\binom{4}{2}/\binom{52}{2}}{1 - \binom{48}{2}/\binom{52}{2}} \approx 0.0303
$$

Knowing a *specific* ace was drawn ($A_1$) gives higher probability of two aces than knowing merely that *some* ace was drawn ($A$), because $A_1$ is a smaller, more informative event.

```python
from math import comb

# P(B | A1): specific ace drawn
P_B_given_A1 = 3 / 51
print(f"P(B | A1) = {P_B_given_A1:.4f}")

# P(B | A): at least one ace
P_B = comb(4, 2) / comb(52, 2)
P_A = 1 - comb(48, 2) / comb(52, 2)
P_B_given_A = P_B / P_A
print(f"P(B | A)  = {P_B_given_A:.4f}")
```
