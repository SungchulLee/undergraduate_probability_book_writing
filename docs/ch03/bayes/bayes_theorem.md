# Bayes' Theorem

Bayes' theorem "reverses" a conditional probability: it computes $P(B \mid A)$ from $P(A \mid B)$. It is the foundation of Bayesian inference and one of the most consequential results in probability.

## Definition

$$
P(B \mid A) = \frac{P(A \mid B)\,P(B)}{P(A)}
$$

Combined with the law of total probability over a partition $\{B_1, \ldots, B_n\}$:

$$
P(B_j \mid A) = \frac{P(A \mid B_j)\,P(B_j)}{\sum_{k=1}^{n} P(A \mid B_k)\,P(B_k)}
$$

## Explanation

### Derivation

From the chain rule: $P(AB) = P(A)P(B \mid A) = P(B)P(A \mid B)$. Solving for $P(B \mid A)$ gives Bayes' theorem.

### Prior-Posterior Interpretation

| Term | Expression | Meaning |
|:---|:---|:---|
| **Prior** | $P(B_j)$ | Belief about $B_j$ before data |
| **Likelihood** | $P(A \mid B_j)$ | Probability of data under hypothesis $B_j$ |
| **Evidence** | $P(A)$ | Total probability of observed data |
| **Posterior** | $P(B_j \mid A)$ | Updated belief after observing data |

$$
\text{Posterior} = \frac{\text{Likelihood} \times \text{Prior}}{\text{Evidence}}
$$

### Odds Form

For two hypotheses $B_1, B_2$, the normalizing constant cancels:

$$
\frac{P(B_1 \mid A)}{P(B_2 \mid A)} = \frac{P(B_1)}{P(B_2)} \cdot \frac{P(A \mid B_1)}{P(A \mid B_2)}
$$

$$
\text{Posterior odds} = \text{Prior odds} \times \text{Bayes factor}
$$

## Examples

**Example (Medical test).** Disease prevalence $P(D) = 0.0001$, sensitivity $P(+ \mid D) = 0.95$, false positive rate $P(+ \mid H) = 0.01$.

$$
P(D \mid +) = \frac{(0.0001)(0.95)}{(0.0001)(0.95) + (0.9999)(0.01)} = \frac{0.000095}{0.010094} \approx 0.0094
$$

Despite 95% test accuracy, a positive result gives only a 0.94% chance of disease, because the low prevalence means false positives vastly outnumber true positives.

```python
# Medical testing example
P_D = 0.0001
P_pos_D = 0.95
P_pos_H = 0.01
P_H = 1 - P_D

P_D_pos = (P_D * P_pos_D) / (P_D * P_pos_D + P_H * P_pos_H)
print(f"P(Disease | Positive) = {P_D_pos:.4f}")

# Per million breakdown
pop = 1_000_000
tp = pop * P_D * P_pos_D
fp = pop * P_H * P_pos_H
print(f"True positives:  {tp:.0f}")
print(f"False positives: {fp:.0f}")
print(f"P(D|+) = {tp/(tp+fp):.4f}")
```
