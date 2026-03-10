# Multiplication Rule for Probabilities

The multiplication rule (chain rule) computes the probability of an intersection by successive conditioning. It is the direct rearrangement of the conditional probability definition.

## Definition

For events $A_1, A_2, \ldots, A_n$:

$$
P(A_1 A_2 \cdots A_n) = P(A_1)\,P(A_2 \mid A_1)\,P(A_3 \mid A_1 A_2) \cdots P(A_n \mid A_1 \cdots A_{n-1})
$$

Each factor conditions on all preceding events.

**Special case (two events):** $P(AB) = P(A)\,P(B \mid A)$.

## Explanation

The chain rule is the probability analogue of the counting multiplication rule. Where the counting version multiplies choices at each stage, the chain rule multiplies conditional probabilities at each stage.

It is especially useful when the problem is naturally sequential: drawing cards without replacement, counting votes in order, or building a sequence one element at a time.

## Examples

**Example (Birthday problem via chain rule).** Let $B_k$ = "the first $k$ people all have distinct birthdays." Then

$$
P(\text{no match among } n) = P(B_1)\,P(B_2 \mid B_1)\cdots P(B_n \mid B_1\cdots B_{n-1})
$$

$$
= 1 \cdot \frac{364}{365} \cdot \frac{363}{365} \cdots \frac{365-(n-1)}{365}
$$

For $n = 23$: $P(\text{match}) = 1 - P(\text{no match}) \approx 0.5073$.

```python
import numpy as np

# Birthday problem via chain rule
def birthday_no_match(n):
    p = 1.0
    for k in range(1, n):
        p *= (365 - k) / 365
    return p

for n in [22, 23, 24]:
    print(f"P(match among {n}) = {1 - birthday_no_match(n):.4f}")
# Output: 0.4757, 0.5073, 0.5383
```
