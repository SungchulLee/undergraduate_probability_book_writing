# Inclusion-Exclusion Principle

## Overview

The **inclusion-exclusion principle** generalizes the addition rule to handle **overlapping** (non-disjoint) sets. When categories overlap, simply summing their sizes overcounts elements that belong to multiple categories. The inclusion-exclusion principle corrects for this overcounting systematically.

## Motivation — Minesweeper

Consider the game of **Minesweeper**, where determining the location of mines requires reasoning about overlapping regions. When cells labeled A, B, and C share neighboring mine zones, the total count of mines in their union requires careful subtraction of overlaps — a natural application of the inclusion-exclusion principle.

## Two Sets

For two sets $A$ and $B$:

**Upper bound (overcounting):**

$$|A \cup B| \leq |A| + |B|$$

**Exact formula:**

$$|A \cup B| = |A| + |B| - |A \cap B|$$

The term $|A \cap B|$ corrects for elements counted twice (once in $|A|$ and once in $|B|$).

## Three Sets

For three sets $A$, $B$, and $C$:

**First approximation (overcounting):**

$$|A \cup B \cup C| \leq |A| + |B| + |C|$$

**Second approximation (undercounting):**

$$|A \cup B \cup C| \geq |A| + |B| + |C| - |AB| - |BC| - |CA|$$

**Exact formula:**

$$|A \cup B \cup C| = |A| + |B| + |C| - |AB| - |BC| - |CA| + |ABC|$$

where $AB$ denotes $A \cap B$, etc.

## General Formula — Many Sets

For $n$ sets $A_1, A_2, \ldots, A_n$:

$$\left|\bigcup_{i=1}^{n} A_i\right| = \sum_{i=1}^{n} |A_i| - \sum_{1 \leq i < j \leq n} |A_i A_j| + \sum_{1 \leq i < j < k \leq n} |A_i A_j A_k| - \cdots + (-1)^{n+1} |A_1 A_2 \cdots A_n|$$

The pattern alternates between adding and subtracting: add single sets, subtract pairwise intersections, add triple intersections, and so on.

## Bonferroni Inequalities

The partial sums of the inclusion-exclusion formula alternate between upper and lower bounds:

$$\left|\bigcup_{i=1}^{n} A_i\right| \leq \sum_{i=1}^{n} |A_i|$$

$$\left|\bigcup_{i=1}^{n} A_i\right| \geq \sum_{i=1}^{n} |A_i| - \sum_{1 \leq i < j \leq n} |A_i A_j|$$

$$\left|\bigcup_{i=1}^{n} A_i\right| \leq \sum_{i=1}^{n} |A_i| - \sum_{1 \leq i < j \leq n} |A_i A_j| + \sum_{1 \leq i < j < k \leq n} |A_i A_j A_k|$$

These are known as the **Bonferroni inequalities** and are useful when computing the full inclusion-exclusion formula is impractical.

## Combining with Complement

The inclusion-exclusion principle combines naturally with complement counting. If $B = \Omega \setminus \bigcup_{i=1}^{n} A_i$, then:

$$|B| = |\Omega| - \left|\bigcup_{i=1}^{n} A_i\right|$$

This is exactly the approach used in the matching problem (derangements), covered in a later section.

## Python Implementation

```python
from itertools import combinations

def inclusion_exclusion(sets):
    """
    Compute |A1 ∪ A2 ∪ ... ∪ An| using the inclusion-exclusion principle.
    
    Parameters
    ----------
    sets : list of set
        The sets A1, A2, ..., An.
    
    Returns
    -------
    int
        Size of the union.
    """
    n = len(sets)
    total = 0
    for k in range(1, n + 1):
        sign = (-1) ** (k + 1)
        for combo in combinations(range(n), k):
            intersection = sets[combo[0]]
            for idx in combo[1:]:
                intersection = intersection & sets[idx]
            total += sign * len(intersection)
    return total

# Example: Two sets
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
print(f"|A ∪ B| = {inclusion_exclusion([A, B])}")
print(f"Verification: {len(A | B)}")
# Output: |A ∪ B| = 7, Verification: 7

# Example: Three sets
C = {5, 6, 7, 8}
print(f"|A ∪ B ∪ C| = {inclusion_exclusion([A, B, C])}")
print(f"Verification: {len(A | B | C)}")
# Output: |A ∪ B ∪ C| = 8, Verification: 8

# Step-by-step for three sets
print(f"\n|A| + |B| + |C| = {len(A) + len(B) + len(C)}")
print(f"|AB| + |BC| + |CA| = {len(A&B) + len(B&C) + len(C&A)}")
print(f"|ABC| = {len(A & B & C)}")
print(f"By IE: {len(A)+len(B)+len(C) - len(A&B)-len(B&C)-len(C&A) + len(A&B&C)}")
```

## Key Takeaway

The inclusion-exclusion principle is the primary tool for counting the size of a union of overlapping sets. It systematically corrects for overcounting by alternately subtracting and adding intersection terms. Combined with complement counting, it solves problems where direct counting is difficult — most notably the matching problem (derangements).
