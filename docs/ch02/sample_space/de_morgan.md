# De Morgan's Laws

## Statement

**De Morgan's Laws** provide a fundamental connection between unions, intersections, and complements. They are essential tools for manipulating events in probability.

### For Two Events

$$

(A \cup B)^c = A^c \cap B^c

$$

$$

(A \cap B)^c = A^c \cup B^c

$$

In words:

- The complement of a union is the intersection of the complements: "neither $A$ nor $B$" means "not $A$ **and** not $B$."
- The complement of an intersection is the union of the complements: "not both $A$ and $B$" means "not $A$ **or** not $B$."

### For Finitely Many Events

$$

\left(\bigcup_{i=1}^{n} A_i\right)^c = \bigcap_{i=1}^{n} A_i^c

$$

$$

\left(\bigcap_{i=1}^{n} A_i\right)^c = \bigcup_{i=1}^{n} A_i^c

$$

### For Countably Many Events

$$

\left(\bigcup_{i=1}^{\infty} A_i\right)^c = \bigcap_{i=1}^{\infty} A_i^c

$$

$$

\left(\bigcap_{i=1}^{\infty} A_i\right)^c = \bigcup_{i=1}^{\infty} A_i^c

$$

## Proof (Two-Event Case)

We prove $(A \cup B)^c = A^c \cap B^c$ by showing each side is a subset of the other.

**$(\subseteq)$** Let $\omega \in (A \cup B)^c$. Then $\omega \notin A \cup B$, which means $\omega \notin A$ and $\omega \notin B$. Therefore $\omega \in A^c$ and $\omega \in B^c$, so $\omega \in A^c \cap B^c$.

**$(\supseteq)$** Let $\omega \in A^c \cap B^c$. Then $\omega \notin A$ and $\omega \notin B$, so $\omega \notin A \cup B$. Therefore $\omega \in (A \cup B)^c$.

The proof of $(A \cap B)^c = A^c \cup B^c$ is analogous.

## Why De Morgan's Laws Matter in Probability

De Morgan's Laws are frequently used to convert between "at least one" and "none" type problems:

$$

P\left(\bigcup_{i=1}^{n} A_i\right) = 1 - P\left(\bigcap_{i=1}^{n} A_i^c\right)

$$

This is especially powerful when the $A_i^c$ events are easier to work with — for instance, when the events are independent.

!!! example "Practical Application"
    **Problem:** What is the probability that at least one of $n$ independent events occurs?

    Let $A_i$ be the $i$-th event with $P(A_i) = p_i$. Then:

    $$

    P\left(\bigcup_{i=1}^{n} A_i\right) = 1 - P\left(\bigcap_{i=1}^{n} A_i^c\right) = 1 - \prod_{i=1}^{n}(1 - p_i)

    $$

    The last equality uses independence.

## Python Example

```python
# Verify De Morgan's Laws with sets
omega = {1, 2, 3, 4, 5, 6}
A = {1, 2, 3}
B = {2, 3, 4}

# De Morgan's First Law: (A ∪ B)^c = A^c ∩ B^c
lhs_1 = omega - (A | B)
rhs_1 = (omega - A) & (omega - B)
print(f"(A ∪ B)^c = {lhs_1}")
print(f"A^c ∩ B^c = {rhs_1}")
print(f"Equal: {lhs_1 == rhs_1}\n")

# De Morgan's Second Law: (A ∩ B)^c = A^c ∪ B^c
lhs_2 = omega - (A & B)
rhs_2 = (omega - A) | (omega - B)
print(f"(A ∩ B)^c = {lhs_2}")
print(f"A^c ∪ B^c = {rhs_2}")
print(f"Equal: {lhs_2 == rhs_2}")
```

**Output:**
```
(A ∪ B)^c = {5, 6}
A^c ∩ B^c = {5, 6}
Equal: True

(A ∩ B)^c = {1, 4, 5, 6}
A^c ∪ B^c = {1, 4, 5, 6}
Equal: True
```

```python
import numpy as np

# Probability application: "at least one" via complement
# Roll a die 4 times. P(at least one 6)?
n_rolls = 4
p_six = 1/6

# Direct: P(at least one 6) = 1 - P(no sixes)
# Using De Morgan: P(∪ Ai) = 1 - P(∩ Ai^c) = 1 - (5/6)^4
p_at_least_one = 1 - (1 - p_six)**n_rolls
print(f"P(at least one 6 in {n_rolls} rolls) = 1 - (5/6)^{n_rolls} = {p_at_least_one:.4f}")

# Simulation verification
np.random.seed(42)
n_sim = 100_000
rolls = np.random.randint(1, 7, size=(n_sim, n_rolls))
sim_prob = np.mean(np.any(rolls == 6, axis=1))
print(f"Simulated probability: {sim_prob:.4f}")
```

**Output:**
```
P(at least one 6 in 4 rolls) = 1 - (5/6)^4 = 0.5177
Simulated probability: 0.5169
```
