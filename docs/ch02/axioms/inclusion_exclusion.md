# Inclusion-Exclusion for Probabilities

The inclusion-exclusion principle extends from counting (Chapter 1) to probabilities, providing the exact probability of a union of overlapping events.

## Definition

For $n$ events $A_1, \ldots, A_n$:

$$
P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{k=1}^{n} (-1)^{k+1} \sum_{1 \le i_1 < \cdots < i_k \le n} P(A_{i_1} \cap \cdots \cap A_{i_k})
$$

The **Bonferroni inequalities** state that truncating at an odd number of terms gives an upper bound, and at an even number gives a lower bound.

## Explanation

### Two Events

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

Adding $P(A) + P(B)$ double-counts outcomes in $A \cap B$; subtracting $P(A \cap B)$ corrects this.

### Three Events

$$
P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(AB) - P(BC) - P(CA) + P(ABC)
$$

After subtracting pairwise intersections, outcomes in all three sets have been removed entirely; adding $P(ABC)$ restores them.

### Bonferroni Bounds

When computing all $2^n - 1$ intersection terms is impractical:

$$
P\left(\bigcup A_i\right) \le \sum P(A_i) \quad \text{(Boole's inequality — first upper bound)}
$$

$$
P\left(\bigcup A_i\right) \ge \sum P(A_i) - \sum_{i<j} P(A_i \cap A_j) \quad \text{(first lower bound)}
$$

Each additional level of terms flips the direction of the bound.

## Examples

**Example 1 (At least one ace in a 5-card hand).**

Let $A_i$ = "the $i$-th ace is in the hand." By symmetry, $P(A_i) = \binom{51}{4}/\binom{52}{5} = 5/52$.

The complement is simpler:

$$
P(\text{at least one ace}) = 1 - \frac{\binom{48}{5}}{\binom{52}{5}} \approx 0.3412
$$

---

**Example 2 (Die rolls).** Roll a fair die once. $A = \{2,4,6\}$ (even), $B = \{1,2,3\}$ (small), $C = \{3,4,5,6\}$ (at least 3).

$P(A \cup B \cup C) = 3/6 + 3/6 + 4/6 - 1/6 - 2/6 - 2/6 + 1/6 = 6/6 = 1$.

Every outcome belongs to at least one of $A, B, C$, so the union is $\Omega$.

```python
from math import comb
from itertools import combinations

# Example 1
p_no_ace = comb(48, 5) / comb(52, 5)
print(f"P(at least one ace) = {1 - p_no_ace:.6f}")

# Example 2
omega = set(range(1, 7))
P = lambda E: len(E) / len(omega)
A, B, C = {2, 4, 6}, {1, 2, 3}, {3, 4, 5, 6}

# Full inclusion-exclusion
S1 = P(A) + P(B) + P(C)
S2 = P(A & B) + P(B & C) + P(C & A)
S3 = P(A & B & C)
ie = S1 - S2 + S3
print(f"\nP(A∪B∪C) = {S1:.4f} - {S2:.4f} + {S3:.4f} = {ie:.4f}")
print(f"Direct: P(A∪B∪C) = {P(A | B | C):.4f}")

# Bonferroni bounds
print(f"\nBonferroni upper: {S1:.4f}")
print(f"Bonferroni lower: {S1 - S2:.4f}")
print(f"Exact:            {ie:.4f}")
```
