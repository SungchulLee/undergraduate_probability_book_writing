# Events and Set Operations


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Events

An **event** is any subset $A$ of the sample space $\Omega$. An event collects all samples (outcomes) of interest.

$$
A \subseteq \Omega
$$

!!! example "Events for Rolling a Die"
    With $\Omega = \{1, 2, 3, 4, 5, 6\}$:

    - "Rolling an even number": $A = \{2, 4, 6\}$
    - "Rolling at most 3": $B = \{1, 2, 3\}$
    - "Rolling a 5": $C = \{5\}$ (a **simple** or **elementary** event)

## Special Events

| Event | Notation | Description |
|-------|----------|-------------|
| **Certain event** | $\Omega$ | The event that always occurs |
| **Impossible event** | $\emptyset$ | The event that never occurs |
| **Elementary event** | $\{\omega\}$ | An event containing a single outcome |

## Set Operations on Events

Since events are sets, we can combine them using standard set operations. Each set operation has a natural probabilistic interpretation.

### Union (OR)

The event "$A$ or $B$ (or both) occurs":

$$
A \cup B = \{\omega \in \Omega : \omega \in A \text{ or } \omega \in B\}
$$

### Intersection (AND)

The event "both $A$ and $B$ occur":

$$
A \cap B = \{\omega \in \Omega : \omega \in A \text{ and } \omega \in B\}
$$

We often write $A \cap B$ as $AB$ for brevity.

### Complement (NOT)

The event "$A$ does not occur":

$$
A^c = \{\omega \in \Omega : \omega \notin A\}
$$

### Difference

The event "$A$ occurs but $B$ does not":

$$
A \setminus B = A \cap B^c = \{\omega \in \Omega : \omega \in A \text{ and } \omega \notin B\}
$$

## Disjoint (Mutually Exclusive) Events

Events $A$ and $B$ are **disjoint** (or mutually exclusive) if they cannot both occur:

$$
A \cap B = \emptyset
$$

More generally, events $A_1, A_2, \ldots$ are **pairwise disjoint** if $A_i \cap A_j = \emptyset$ for all $i \neq j$.

## Partition of the Sample Space

Events $A_1, A_2, \ldots, A_n$ form a **partition** of $\Omega$ if:

1. They are pairwise disjoint: $A_i \cap A_j = \emptyset$ for all $i \neq j$
2. They cover the entire sample space: $A_1 \cup A_2 \cup \cdots \cup A_n = \Omega$

!!! note "Key Property"
    For any event $A$, the pair $\{A, A^c\}$ always forms a partition of $\Omega$.

## Key Set Identities

The following identities hold for events and are used frequently in probability:

**Commutativity:**

$$
A \cup B = B \cup A, \qquad A \cap B = B \cap A
$$

**Associativity:**

$$
(A \cup B) \cup C = A \cup (B \cup C), \qquad (A \cap B) \cap C = A \cap (B \cap C)
$$

**Distributivity:**

$$
A \cap (B \cup C) = (A \cap B) \cup (A \cap C)
$$

$$
A \cup (B \cap C) = (A \cup B) \cap (A \cup C)
$$

## Python Example

```python
# Define sample space and events for rolling a die
omega = {1, 2, 3, 4, 5, 6}
A = {2, 4, 6}        # even numbers
B = {1, 2, 3}        # at most 3
C = {4, 5, 6}        # at least 4

print(f"Ω = {omega}")
print(f"A (even) = {A}")
print(f"B (≤ 3) = {B}")
print(f"C (≥ 4) = {C}")

# Set operations
print(f"\nA ∪ B = {A | B}")
print(f"A ∩ B = {A & B}")
print(f"A^c = {omega - A}")
print(f"A \\ B = {A - B}")

# Check disjointness
print(f"\nB ∩ C = {B & C}  → Disjoint: {len(B & C) == 0}")
print(f"A ∩ B = {A & B}  → Disjoint: {len(A & B) == 0}")

# Check partition
print(f"\nB ∪ C = {B | C}  → Partition of Ω: {B | C == omega and len(B & C) == 0}")
```

**Output:**
```
Ω = {1, 2, 3, 4, 5, 6}
A (even) = {2, 4, 6}
B (≤ 3) = {1, 2, 3}
C (≥ 4) = {4, 5, 6}

A ∪ B = {1, 2, 3, 4, 6}
A ∩ B = {2}
A^c = {1, 3, 5}
A \ B = {4, 6}

B ∩ C = set()  → Disjoint: True
A ∩ B = {2}  → Disjoint: False

B ∪ C = {1, 2, 3, 4, 5, 6}  → Partition of Ω: True
```
