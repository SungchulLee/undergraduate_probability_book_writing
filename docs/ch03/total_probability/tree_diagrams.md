# Tree Diagrams

Tree diagrams are the visual tool for organizing sequential probability calculations. Each branch carries a conditional probability, and path probabilities multiply — directly implementing the chain rule.

## Definition

A **tree diagram** for a multi-stage experiment has:

- **Root:** Initial state
- **Branches:** Each labeled with a conditional probability $P(B_j \mid \text{parent})$
- **Leaves:** Complete outcomes, with $P(\text{path}) = \prod(\text{branch probabilities along path})$
- **Total probability:** $P(B_j) = \sum(\text{all paths reaching } B_j)$

## Explanation

For a two-stage experiment with first outcome $A_i$ and second outcome $B_j$:

- Level 1 branches carry $P(A_i)$
- Level 2 branches carry $P(B_j \mid A_i)$
- Path probability: $P(A_i \cap B_j) = P(A_i)\,P(B_j \mid A_i)$

Summing paths to a given outcome implements the law of total probability. Working backwards from a leaf via Bayes' theorem reverses the conditional direction.

## Examples

**Example 1 (Without replacement).** Bag: 2 green, 1 purple. Draw two without replacement.

| Path | Probability |
|:---|:---|
| Green, Green | $(2/3)(1/2) = 1/3$ |
| Green, Purple | $(2/3)(1/2) = 1/3$ |
| Purple, Green | $(1/3)(1) = 1/3$ |

$P(\text{2nd green}) = 1/3 + 1/3 = 2/3$ (same as unconditional — a nice symmetry).

---

**Example 2 (Medical test).** Prevalence $P(D) = 0.0001$, sensitivity 95%, false positive 1%.

- Path $D \to +$: $(0.0001)(0.95) = 0.000095$
- Path $H \to +$: $(0.9999)(0.01) = 0.009999$
- $P(D \mid +) = 0.000095 / (0.000095 + 0.009999) \approx 0.0094$

```python
# Example 1: Drawing without replacement
# P(2nd green) via total probability
P_2nd_green = (2/3)*(1/2) + (1/3)*(1)
print(f"P(2nd green) = {P_2nd_green:.4f}")

# Example 2: Medical test
P_D_pos = 0.0001 * 0.95
P_H_pos = 0.9999 * 0.01
print(f"P(D | +) = {P_D_pos / (P_D_pos + P_H_pos):.4f}")
```
