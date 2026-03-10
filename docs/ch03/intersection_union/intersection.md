# Computing P(A1 ∩ A2 ∩ ... ∩ An)

Computing the probability of an intersection depends on whether the events are independent or dependent, with the chain rule as the universal tool.

## Definition

**Independent events:**

$$
P(A_1 \cap \cdots \cap A_n) = \prod_{i=1}^{n} P(A_i)
$$

**General (chain rule):**

$$
P(A_1 \cap \cdots \cap A_n) = P(A_1)\,P(A_2 \mid A_1)\,P(A_3 \mid A_1 A_2) \cdots P(A_n \mid A_1 \cdots A_{n-1})
$$

## Explanation

The chain rule is always valid. For independent events, each conditional factor reduces to $P(A_k)$, recovering the product rule. The chain rule is most useful for sequential problems (drawing without replacement, multi-stage experiments) where each conditional probability is easy to compute given the history.

| Scenario | Method |
|:---|:---|
| Independent | Product: $\prod P(A_i)$ |
| Dependent | Chain rule |
| Joint table available | Direct lookup |

## Examples

**Example (Cards without replacement).** Draw 3 cards. $P(\text{all hearts})$:

$$
P = \frac{13}{52} \cdot \frac{12}{51} \cdot \frac{11}{50} = \frac{1716}{132600} \approx 0.0129
$$

```python
P = (13/52) * (12/51) * (11/50)
print(f"P(all hearts) = {P:.4f}")
```
