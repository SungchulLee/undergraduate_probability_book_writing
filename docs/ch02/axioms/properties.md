# Properties Derived from Axioms

## Overview

Starting from the three Kolmogorov axioms, we can derive a rich collection of properties. These properties are the everyday tools of probability computation.

## Property 4: Finite Additivity

For any **pairwise disjoint** events $A_1, A_2, \ldots, A_n$:

$$

P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i)

$$

This follows from Axiom 3 by setting $A_{n+1} = A_{n+2} = \cdots = \emptyset$.

## Property 5: Monotonicity

If $A \subseteq B$, then:

$$

P(A) \leq P(B)

$$

**Proof:** Write $B = A \cup (B \setminus A)$ where $A$ and $B \setminus A$ are disjoint. By finite additivity:

$$

P(B) = P(A) + P(B \setminus A) \geq P(A)

$$

since $P(B \setminus A) \geq 0$.

## Property 6: Complement Rule

$$

P(A) = 1 - P(A^c)

$$

**Proof:** Since $A$ and $A^c$ are disjoint and $A \cup A^c = \Omega$:

$$

1 = P(\Omega) = P(A \cup A^c) = P(A) + P(A^c)

$$

!!! tip "Practical Importance"
    The complement rule is one of the most frequently used tools in probability. It is often easier to compute $P(A^c)$ (the probability that $A$ does **not** happen) than $P(A)$ directly.

    The strategy: **$P(\text{at least one}) = 1 - P(\text{none})$**

## Additional Useful Properties

### Difference Rule

For any events $A$ and $B$:

$$

P(A \setminus B) = P(A) - P(A \cap B)

$$

**Proof:** $A = (A \setminus B) \cup (A \cap B)$ is a disjoint union, so $P(A) = P(A \setminus B) + P(A \cap B)$.

### Probability of a Union (General)

For any two events (not necessarily disjoint):

$$

P(A \cup B) = P(A) + P(B) - P(A \cap B)

$$

This is the simplest case of the inclusion-exclusion principle (covered in the next section).

### Subadditivity (Union Bound)

For any events $A_1, A_2, \ldots, A_n$ (not necessarily disjoint):

$$

P\left(\bigcup_{i=1}^{n} A_i\right) \leq \sum_{i=1}^{n} P(A_i)

$$

This is **Boole's inequality**, and it provides a useful upper bound.

## Summary Table

| # | Property | Statement |
|---|----------|-----------|
| 4 | Finite additivity | $P(\cup_{i=1}^n A_i) = \sum_{i=1}^n P(A_i)$ for disjoint $A_i$ |
| 5 | Monotonicity | $A \subseteq B \Rightarrow P(A) \leq P(B)$ |
| 6 | Complement rule | $P(A) = 1 - P(A^c)$ |

## Python Example

```python
import numpy as np

# Demonstrate properties with a fair die
omega = {1, 2, 3, 4, 5, 6}
P = lambda event: len(event) / len(omega)

A = {1, 2, 3}    # ≤ 3
B = {2, 3, 4, 5}  # between 2 and 5

# Property 5: Monotonicity
C = {2, 3}  # C ⊂ A
print(f"Monotonicity: P(C) = {P(C):.4f} ≤ P(A) = {P(A):.4f}: {P(C) <= P(A)}")

# Property 6: Complement rule
print(f"\nComplement rule:")
print(f"P(A) = {P(A):.4f}")
print(f"P(A^c) = {P(omega - A):.4f}")
print(f"P(A) + P(A^c) = {P(A) + P(omega - A):.4f}")

# Difference rule
print(f"\nDifference rule:")
print(f"P(A \\ B) = {P(A - B):.4f}")
print(f"P(A) - P(A ∩ B) = {P(A) - P(A & B):.4f}")

# Union formula
print(f"\nUnion formula:")
print(f"P(A ∪ B) = {P(A | B):.4f}")
print(f"P(A) + P(B) - P(A ∩ B) = {P(A) + P(B) - P(A & B):.4f}")

# Boole's inequality
print(f"\nBoole's inequality:")
print(f"P(A ∪ B) = {P(A | B):.4f} ≤ P(A) + P(B) = {P(A) + P(B):.4f}")
```

**Output:**
```
Monotonicity: P(C) = 0.3333 ≤ P(A) = 0.5000: True

Complement rule:
P(A) = 0.5000
P(A^c) = 0.5000
P(A) + P(A^c) = 1.0000

Difference rule:
P(A \ B) = 0.1667
P(A) - P(A ∩ B) = 0.1667

Union formula:
P(A ∪ B) = 0.8333
P(A) + P(B) - P(A ∩ B) = 0.8333

Boole's inequality:
P(A ∪ B) = 0.8333 ≤ P(A) + P(B) = 1.1667
```
