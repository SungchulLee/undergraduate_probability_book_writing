# Properties Derived from Axioms

The three Kolmogorov axioms imply a rich set of properties that form the everyday toolkit for probability computation.

## Definition

The following properties hold for any probability measure $P$ on $(\Omega, \mathcal{F}, P)$:

| Property | Statement |
|:---|:---|
| Complement | $P(A^c) = 1 - P(A)$ |
| Monotonicity | $A \subseteq B \implies P(A) \le P(B)$ |
| Difference | $P(A \setminus B) = P(A) - P(A \cap B)$ |
| Union (2 events) | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Subadditivity | $P(\bigcup_{i=1}^n A_i) \le \sum_{i=1}^n P(A_i)$ |

## Explanation

### Complement Rule

Since $A$ and $A^c$ partition $\Omega$, Axiom 3 gives $P(A) + P(A^c) = P(\Omega) = 1$.

This is one of the most frequently used tools: **$P(\text{at least one}) = 1 - P(\text{none})$**.

### Monotonicity

If $A \subseteq B$, write $B = A \cup (B \setminus A)$ as a disjoint union. Then $P(B) = P(A) + P(B \setminus A) \ge P(A)$.

### Difference Rule

$A = (A \setminus B) \cup (A \cap B)$ is disjoint, so $P(A) = P(A \setminus B) + P(A \cap B)$.

### Union of Two Events

$A \cup B = A \cup (B \setminus A)$ is disjoint, and $P(B \setminus A) = P(B) - P(A \cap B)$ by the difference rule. So $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

### Subadditivity (Boole's Inequality)

Follows by induction from the two-event union formula and the fact that $P(A \cap B) \ge 0$.

## Examples

**Example (Fair die).** $\Omega = \{1,2,3,4,5,6\}$, uniform. Let $A = \{1,2,3\}$ (at most 3), $B = \{2,4,6\}$ (even).

- $P(A^c) = 1 - 3/6 = 1/2$
- $A \cap B = \{2\}$, so $P(A \cup B) = 3/6 + 3/6 - 1/6 = 5/6$
- $P(A \setminus B) = P(A) - P(A \cap B) = 3/6 - 1/6 = 2/6$
- Boole: $P(A \cup B) = 5/6 \le P(A) + P(B) = 6/6$ ✓

```python
omega = set(range(1, 7))
P = lambda E: len(E) / len(omega)

A = {1, 2, 3}
B = {2, 4, 6}

# Complement
assert abs(P(omega - A) - (1 - P(A))) < 1e-10
print(f"P(A^c) = {P(omega - A):.4f} = 1 - P(A) = {1 - P(A):.4f}")

# Monotonicity
C = {2, 3}  # C ⊂ A
print(f"P(C={C}) = {P(C):.4f} ≤ P(A={A}) = {P(A):.4f}")

# Difference
print(f"P(A\\B) = {P(A - B):.4f} = P(A) - P(A∩B) = {P(A) - P(A & B):.4f}")

# Union
print(f"P(A∪B) = {P(A | B):.4f} = P(A)+P(B)-P(A∩B) = {P(A) + P(B) - P(A & B):.4f}")

# Boole
print(f"P(A∪B) = {P(A | B):.4f} ≤ P(A)+P(B) = {P(A) + P(B):.4f}")
```
