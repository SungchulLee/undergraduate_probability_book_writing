# De Morgan's Laws

De Morgan's laws relate complements to unions and intersections. They are the key tool for converting "at least one" problems into "none" problems — one of the most common moves in probability.

## Definition

For any events $A_1, A_2, \ldots$:

$$
\left(\bigcup_{i} A_i\right)^c = \bigcap_{i} A_i^c \qquad \text{and} \qquad \left(\bigcap_{i} A_i\right)^c = \bigcup_{i} A_i^c
$$

In words:

- "None of the $A_i$ occurs" $=$ "every $A_i$ fails"
- "Not all $A_i$ occur" $=$ "at least one $A_i$ fails"

## Explanation

### Proof (Two-Event Case)

We show $(A \cup B)^c = A^c \cap B^c$.

$(\subseteq)$ If $\omega \in (A \cup B)^c$, then $\omega \notin A$ and $\omega \notin B$, so $\omega \in A^c \cap B^c$.

$(\supseteq)$ If $\omega \in A^c \cap B^c$, then $\omega \notin A$ and $\omega \notin B$, so $\omega \notin A \cup B$, hence $\omega \in (A \cup B)^c$. $\square$

### Application to Probability

De Morgan's laws give the fundamental complement-counting identity:

$$
P\left(\bigcup_{i=1}^{n} A_i\right) = 1 - P\left(\bigcap_{i=1}^{n} A_i^c\right)
$$

When the $A_i$ are independent, the right side factors:

$$
P\left(\bigcup_{i=1}^{n} A_i\right) = 1 - \prod_{i=1}^{n}(1 - P(A_i))
$$

## Examples

**Example 1 (At least one 6 in 4 rolls).** Let $A_i$ = "roll $i$ is a 6." By De Morgan and independence:

$$
P(\text{at least one 6}) = 1 - P(\text{no 6's}) = 1 - (5/6)^4 \approx 0.5177
$$

---

**Example 2 (Verification with sets).** $\Omega = \{1,\ldots,6\}$, $A = \{1,2,3\}$, $B = \{2,3,4\}$.

$(A \cup B)^c = \{5,6\} = A^c \cap B^c$. ✓

$(A \cap B)^c = \{1,4,5,6\} = A^c \cup B^c$. ✓

```python
import numpy as np

# Example 2: Set verification
omega = {1, 2, 3, 4, 5, 6}
A, B = {1, 2, 3}, {2, 3, 4}

assert omega - (A | B) == (omega - A) & (omega - B)
assert omega - (A & B) == (omega - A) | (omega - B)
print("De Morgan's laws verified.")

# Example 1: Simulation
np.random.seed(42)
rolls = np.random.randint(1, 7, size=(100_000, 4))
sim = np.mean(np.any(rolls == 6, axis=1))
exact = 1 - (5/6)**4
print(f"P(at least one 6 in 4 rolls): exact={exact:.4f}, sim={sim:.4f}")
```
