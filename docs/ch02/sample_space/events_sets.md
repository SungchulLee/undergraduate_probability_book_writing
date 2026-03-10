# Events and Set Operations

Events are subsets of the sample space. Combining events with set operations — union, intersection, complement — translates everyday questions ("A or B happens", "neither occurs") into precise mathematics.

## Definition

An **event** is any subset $A \subseteq \Omega$. The fundamental set operations on events are:

| Operation | Notation | Meaning |
|:---|:---|:---|
| Union | $A \cup B$ | $A$ or $B$ (or both) occurs |
| Intersection | $A \cap B$ | Both $A$ and $B$ occur |
| Complement | $A^c$ | $A$ does not occur |
| Difference | $A \setminus B = A \cap B^c$ | $A$ occurs but $B$ does not |

Special events: $\Omega$ (certain), $\emptyset$ (impossible), $\{\omega\}$ (elementary).

Events $A, B$ are **disjoint** (mutually exclusive) if $A \cap B = \emptyset$.

Events $A_1, \ldots, A_n$ form a **partition** of $\Omega$ if they are pairwise disjoint and $\bigcup A_i = \Omega$.

## Explanation

### Set Identities for Events

**Commutativity:** $A \cup B = B \cup A$, $\;A \cap B = B \cap A$

**Associativity:** $(A \cup B) \cup C = A \cup (B \cup C)$

**Distributivity:** $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$

**Key fact:** For any event $A$, the pair $\{A, A^c\}$ is always a partition of $\Omega$.

## Examples

**Example (Die).** $\Omega = \{1,2,3,4,5,6\}$. Let $A = \{2,4,6\}$ (even), $B = \{1,2,3\}$ (small), $C = \{4,5,6\}$ (large).

- $A \cup B = \{1,2,3,4,6\}$
- $A \cap B = \{2\}$
- $A^c = \{1,3,5\}$
- $B$ and $C$ are disjoint and form a partition of $\Omega$

```python
omega = {1, 2, 3, 4, 5, 6}
A, B, C = {2, 4, 6}, {1, 2, 3}, {4, 5, 6}

print(f"A ∪ B = {A | B}")
print(f"A ∩ B = {A & B}")
print(f"A^c   = {omega - A}")
print(f"A \\ B = {A - B}")
print(f"B, C disjoint: {B & C == set()}")
print(f"B ∪ C = Ω: {B | C == omega}")
```
