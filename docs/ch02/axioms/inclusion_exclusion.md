# Inclusion-Exclusion for Probabilities

## Two Events

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

!!! note "Why Subtract?"
    When we add $P(A) + P(B)$, outcomes in $A \cap B$ are counted twice. Subtracting $P(A \cap B)$ corrects for this double-counting.

**Upper bound (Boole's inequality):**

$$
P(A \cup B) \leq P(A) + P(B)
$$

## Three Events

**Exact formula:**

$$
P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(AB) - P(BC) - P(CA) + P(ABC)
$$

where we use the shorthand $P(AB) = P(A \cap B)$, etc.

**Bonferroni inequalities for three events:**

$$
P(A \cup B \cup C) \leq P(A) + P(B) + P(C)
$$

$$
P(A \cup B \cup C) \geq P(A) + P(B) + P(C) - P(AB) - P(BC) - P(CA)
$$

## General Case: n Events

### Inclusion-Exclusion Principle

$$
P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i) - \sum_{1 \leq i < j \leq n} P(A_i A_j) + \sum_{1 \leq i < j < k \leq n} P(A_i A_j A_k) - \cdots + (-1)^{n+1} P(A_1 A_2 \cdots A_n)
$$

Written compactly:

$$
P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{k=1}^{n} (-1)^{k+1} \sum_{1 \leq i_1 < \cdots < i_k \leq n} P(A_{i_1} \cap \cdots \cap A_{i_k})
$$

### Bonferroni Inequalities

The partial sums of the inclusion-exclusion formula alternate between upper and lower bounds:

$$
P\left(\bigcup_{i=1}^{n} A_i\right) \leq \sum_{i=1}^{n} P(A_i)
$$

$$
P\left(\bigcup_{i=1}^{n} A_i\right) \geq \sum_{i=1}^{n} P(A_i) - \sum_{1 \leq i < j \leq n} P(A_i A_j)
$$

$$
P\left(\bigcup_{i=1}^{n} A_i\right) \leq \sum_{i=1}^{n} P(A_i) - \sum_{1 \leq i < j \leq n} P(A_i A_j) + \sum_{1 \leq i < j < k \leq n} P(A_i A_j A_k)
$$

The pattern continues: truncating at an **odd** number of terms gives an **upper bound**, and truncating at an **even** number of terms gives a **lower bound**.

### Naming Convention

| Name | Formula |
|------|---------|
| **Boole's inequality** | First upper bound: $P(\cup A_i) \leq \sum P(A_i)$ |
| **Bonferroni inequalities** | All the alternating bounds |
| **Inclusion-exclusion principle** | The exact equality (final line) |

## Example: Cards

!!! example "At Least One Ace in a 5-Card Hand"
    Let $A_i$ = event that the $i$-th ace is in the hand, for $i = 1, 2, 3, 4$.

    By inclusion-exclusion:

    $$
    P(A_1 \cup A_2 \cup A_3 \cup A_4) = \binom{4}{1}\frac{\binom{51}{4}}{\binom{52}{5}} - \binom{4}{2}\frac{\binom{50}{3}}{\binom{52}{5}} + \binom{4}{3}\frac{\binom{49}{2}}{\binom{52}{5}} - \binom{4}{4}\frac{\binom{48}{1}}{\binom{52}{5}}
    $$

    Or more simply, using the complement:

    $$
    P(\text{at least one ace}) = 1 - P(\text{no aces}) = 1 - \frac{\binom{48}{5}}{\binom{52}{5}}
    $$

## Python Example

```python
from math import comb
from itertools import combinations

def inclusion_exclusion(sets, omega_size):
    """
    Compute P(A1 ∪ A2 ∪ ... ∪ An) using inclusion-exclusion.
    """
    n = len(sets)
    total = 0
    for k in range(1, n + 1):
        sign = (-1)**(k + 1)
        for combo in combinations(range(n), k):
            intersection = sets[combo[0]]
            for idx in combo[1:]:
                intersection = intersection & sets[idx]
            total += sign * len(intersection) / omega_size
    return total

# Example: rolling a fair die
omega = set(range(1, 7))
A = {2, 4, 6}     # even
B = {1, 2, 3}     # at most 3
C = {3, 4, 5, 6}  # at least 3

# Two events
ie_2 = inclusion_exclusion([A, B], len(omega))
direct_2 = len(A | B) / len(omega)
print(f"Two events: P(A ∪ B)")
print(f"  Inclusion-exclusion: {ie_2:.4f}")
print(f"  Direct: {direct_2:.4f}")

# Three events
ie_3 = inclusion_exclusion([A, B, C], len(omega))
direct_3 = len(A | B | C) / len(omega)
print(f"\nThree events: P(A ∪ B ∪ C)")
print(f"  Inclusion-exclusion: {ie_3:.4f}")
print(f"  Direct: {direct_3:.4f}")

# Bonferroni bounds for three events
S1 = sum(len(s)/len(omega) for s in [A, B, C])
S2 = sum(len(A_i & A_j)/len(omega)
         for A_i, A_j in combinations([A, B, C], 2))

print(f"\nBonferroni bounds:")
print(f"  Upper (S1):       {S1:.4f}")
print(f"  Lower (S1 - S2):  {S1 - S2:.4f}")
print(f"  Exact:            {ie_3:.4f}")

# At least one ace in a 5-card hand
print(f"\n--- At Least One Ace in 5-Card Hand ---")
p_no_ace = comb(48, 5) / comb(52, 5)
p_at_least_one = 1 - p_no_ace
print(f"P(at least one ace) = 1 - C(48,5)/C(52,5) = {p_at_least_one:.6f}")
```

**Output:**
```
Two events: P(A ∪ B)
  Inclusion-exclusion: 0.8333
  Direct: 0.8333

Three events: P(A ∪ B ∪ C)
  Inclusion-exclusion: 1.0000
  Direct: 1.0000

Bonferroni bounds:
  Upper (S1):       2.1667
  Lower (S1 - S2):  0.8333
  Exact:            1.0000

--- At Least One Ace in 5-Card Hand ---
P(at least one ace) = 1 - C(48,5)/C(52,5) = 0.341392
```
