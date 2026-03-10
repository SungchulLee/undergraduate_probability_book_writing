# Conditional Independence

Conditional independence captures the idea that once a common cause is known, the remaining variables carry no information about each other. It is the foundation of Bayesian networks, Markov chains, and naive Bayes classifiers.

## Definition

Events $A$ and $C$ are **conditionally independent given $B$** if

$$
P(A \cap C \mid B) = P(A \mid B)\,P(C \mid B)
$$

Equivalently: $P(A \mid B, C) = P(A \mid B)$ — once $B$ is known, learning $C$ gives no additional information about $A$.

## Explanation

### Neither Direction of Implication Holds

Independence and conditional independence are **different properties**. Neither implies the other.

**Independent but not conditionally independent.** Toss a fair coin twice. $A$ = "first H", $C$ = "second H", $B$ = "exactly one H." Given $B$, knowing $A$ means $C$ did not happen — they become dependent.

**Conditionally independent but not independent.** Choose a bag at random (Bag 1: 2R, 1B; Bag 2: 1R, 2B). Draw twice with replacement. Given which bag, draws are conditionally independent. But marginally, the first draw being red makes Bag 1 more likely, making the second draw more likely red — so the draws are dependent.

### Applications

Conditional independence structures probability models:

- **Bayesian networks:** Each node is conditionally independent of non-descendants given its parents
- **Naive Bayes:** Features are conditionally independent given the class label
- **Markov chains:** $X_{n+1} \perp\!\!\!\perp (X_1, \ldots, X_{n-1}) \mid X_n$

### Joint, Marginal, and Conditional

For partitions $\{A_i\}$ and $\{B_j\}$, three types of probability are related:

$$
P(A_i B_j) = P(A_i)\,P(B_j \mid A_i) \qquad P(A_i) = \sum_j P(A_i B_j) \qquad P(B_j \mid A_i) = \frac{P(A_i B_j)}{P(A_i)}
$$

Given any two of {joint, marginal, conditional}, the third is determined.

## Examples

**Example (Bag drawing).** Two bags: Bag 1 has $P(\text{red}) = 2/3$, Bag 2 has $P(\text{red}) = 1/3$. Each bag chosen with probability $1/2$. Draw twice with replacement.

Given Bag 1: $P(R_1 \cap R_2 \mid \text{Bag 1}) = (2/3)^2 = 4/9 = P(R_1 \mid \text{Bag 1})\,P(R_2 \mid \text{Bag 1})$. ✓ (Conditionally independent.)

Marginally: $P(R_1) = P(R_2) = 1/2$, but $P(R_1 \cap R_2) = (1/2)(4/9) + (1/2)(1/9) = 5/18 \ne 1/4$. ✗ (Not independent.)

```python
# Bag example
P_R1_R2 = 0.5 * (2/3)**2 + 0.5 * (1/3)**2  # joint
P_R1 = 0.5 * 2/3 + 0.5 * 1/3               # marginal
print(f"P(R1∩R2) = {P_R1_R2:.4f}")
print(f"P(R1)*P(R2) = {P_R1**2:.4f}")
print(f"Independent? {abs(P_R1_R2 - P_R1**2) < 1e-10}")
```
