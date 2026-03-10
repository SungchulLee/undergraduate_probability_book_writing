# Kolmogorov Axioms

The Kolmogorov axioms provide the rigorous foundation for all of probability theory. Every probability result in this book ultimately traces back to these three axioms.

## Definition

A **probability space** is a triple $(\Omega, \mathcal{F}, P)$ where:

1. $\Omega$ is the **sample space** (set of all possible outcomes)
2. $\mathcal{F}$ is a **$\sigma$-algebra** on $\Omega$ (the collection of events, closed under complements and countable unions)
3. $P\colon \mathcal{F} \to [0,1]$ is a **probability measure** satisfying:

**Axiom 1 (Normalization):**

$$
P(\Omega) = 1
$$

**Axiom 2 (Non-negativity):**

$$
P(A) \geq 0 \quad \text{for every event } A \in \mathcal{F}
$$

**Axiom 3 (Countable additivity):** For any sequence of pairwise disjoint events $A_1, A_2, \ldots$:

$$
P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)
$$

!!! note "What the axioms do not include"
    The statement $P(\emptyset) = 0$ is **not** an axiom — it follows from Axiom 3 by taking $A_1 = \Omega, A_2 = A_3 = \cdots = \emptyset$. Similarly, $P(A) \le 1$ is derived from $P(A) + P(A^c) = 1$ and non-negativity.

## Explanation

### Why These Three Axioms?

- **Axiom 1** fixes the scale: certainty is 1.
- **Axiom 2** excludes negative probabilities.
- **Axiom 3** is the workhorse: it lets us compute probabilities of complex events by decomposing them into disjoint pieces. It also implies finite additivity (set $A_{n+1} = A_{n+2} = \cdots = \emptyset$).

The countable (rather than merely finite) additivity in Axiom 3 is essential for handling limits, which pervade probability theory (laws of large numbers, convergence of series, etc.).

### Constructing a Probability Measure

For a finite sample space $\Omega = \{\omega_1, \ldots, \omega_n\}$, assign weights $p_1, \ldots, p_n$ with $p_i \ge 0$ and $\sum p_i = 1$. Then $P(A) = \sum_{\omega_i \in A} p_i$ defines a valid probability measure. The $\sigma$-algebra is simply $\mathcal{F} = 2^\Omega$ (all subsets).

For uncountable spaces like $\mathbb{R}$, the $\sigma$-algebra must be restricted (to the Borel sets) — not all subsets can be assigned probabilities consistently.

## Examples

**Example 1 (Loaded die).** $\Omega = \{1,2,3,4,5,6\}$ with $P(6) = 1/2$ and $P(k) = 1/10$ for $k = 1,\ldots,5$.

Verify: $5 \times (1/10) + 1/2 = 1/2 + 1/2 = 1$. ✓

$P(\text{even}) = P(2) + P(4) + P(6) = 1/10 + 1/10 + 1/2 = 7/10$.

---

**Example 2 (Axiom verification).** Check all three axioms for the loaded die:

```python
import numpy as np

omega = [1, 2, 3, 4, 5, 6]
weights = [1/10, 1/10, 1/10, 1/10, 1/10, 1/2]

# Axiom 1
assert abs(sum(weights) - 1.0) < 1e-10, "Axiom 1 violated"
print(f"Axiom 1: P(Ω) = {sum(weights)}")

# Axiom 2
assert all(w >= 0 for w in weights), "Axiom 2 violated"
print(f"Axiom 2: all P(ω) ≥ 0: True")

# Axiom 3 (finite): P({1,2} ∪ {3,4}) = P({1,2}) + P({3,4})
P_12 = weights[0] + weights[1]
P_34 = weights[2] + weights[3]
P_union = sum(weights[i] for i in range(4))
assert abs(P_union - P_12 - P_34) < 1e-10
print(f"Axiom 3: P({{1,2}}) + P({{3,4}}) = {P_12 + P_34:.2f} = P({{1,2,3,4}}) = {P_union:.2f}")

# Derived: P(∅) = 0
print(f"\nDerived: P(∅) = 0 (follows from Axiom 3)")
print(f"P(even) = {weights[1] + weights[3] + weights[5]:.2f}")
```
