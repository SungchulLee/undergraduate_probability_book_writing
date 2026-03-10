# Computing P(A1 ∪ A2 ∪ ... ∪ An)

The probability of a union depends on the relationship between events: disjoint, independent, or general. The complement method is often the most efficient approach.

## Definition

**Disjoint events:** $P(\bigcup A_i) = \sum P(A_i)$

**General (inclusion-exclusion):**

$$
P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{k=1}^{n}(-1)^{k+1}\sum_{i_1 < \cdots < i_k} P(A_{i_1} \cap \cdots \cap A_{i_k})
$$

**Complement method (via De Morgan):**

$$
P\left(\bigcup_{i=1}^{n} A_i\right) = 1 - P\left(\bigcap_{i=1}^{n} A_i^c\right)
$$

For independent events: $= 1 - \prod_{i=1}^{n}(1 - P(A_i))$.

## Explanation

| Scenario | Best method |
|:---|:---|
| Disjoint | Direct sum |
| Independent | Complement: $1 - \prod(1-P(A_i))$ |
| Few events, overlaps known | Inclusion-exclusion |
| Many events, need bound | Union bound: $\le \sum P(A_i)$ |

The **Bonferroni inequalities** truncate inclusion-exclusion: odd-order truncation gives upper bounds, even-order gives lower bounds.

## Examples

**Example.** $P(A) = 0.3$, $P(B) = 0.4$, $P(A \cap B) = 0.1$.

$P(A \cup B) = 0.3 + 0.4 - 0.1 = 0.6$.

---

**Example (Independent).** 5 independent trials, each with $P(\text{success}) = 0.2$.

$P(\text{at least one success}) = 1 - 0.8^5 \approx 0.672$.

```python
# Independent trials
P_at_least_one = 1 - 0.8**5
print(f"P(at least one success in 5 trials) = {P_at_least_one:.4f}")
```
