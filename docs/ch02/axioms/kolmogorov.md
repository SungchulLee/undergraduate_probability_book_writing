# Kolmogorov Axioms

## Definition

A **probability measure** $P$ is a real-valued function defined on events $A$:

$$
A \xrightarrow{P} P(A)
$$

More precisely, $P$ is a function from the collection of events to the real numbers that satisfies the following three axioms.

## The Three Axioms

### Axiom 1: Normalization

$$
P(\Omega) = 1, \qquad P(\emptyset) = 0
$$

The certain event has probability 1, and the impossible event has probability 0.

### Axiom 2: Non-negativity

$$
0 \leq P(A) \leq 1 \quad \text{for every event } A
$$

Every event has a probability between 0 and 1.

### Axiom 3: Countable Additivity ($\sigma$-additivity)

For any sequence of **pairwise disjoint** events $A_1, A_2, \ldots$:

$$
P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)
$$

If events cannot occur simultaneously, the probability of their union equals the sum of their individual probabilities.

!!! note "Historical Note"
    These axioms were formalized by Andrey Kolmogorov in his 1933 monograph *Grundbegriffe der Wahrscheinlichkeitsrechnung* (Foundations of the Theory of Probability). This axiomatic framework put probability theory on rigorous mathematical footing by grounding it in measure theory.

## The Probability Triple $(\Omega, \mathcal{F}, P)$

Formally, a probability model consists of three components:

1. **Sample space** $\Omega$: the set of all possible outcomes
2. **$\sigma$-algebra** $\mathcal{F}$: a collection of subsets of $\Omega$ (the "events") that is closed under complementation and countable unions
3. **Probability measure** $P$: a function $P: \mathcal{F} \to [0,1]$ satisfying the three axioms

For finite and countable sample spaces, we typically take $\mathcal{F} = 2^\Omega$ (all subsets). The $\sigma$-algebra becomes important for uncountable spaces like $\mathbb{R}$.

## Why These Axioms?

The axioms capture the minimal requirements for a coherent notion of probability:

- **Axiom 1** fixes the scale — certainty is 1, impossibility is 0.
- **Axiom 2** ensures probabilities are meaningful as "proportions of likelihood."
- **Axiom 3** is the most powerful axiom — it allows us to compute probabilities of complex events by decomposing them into simpler, non-overlapping pieces.

!!! tip "Finite Additivity as a Consequence"
    Axiom 3 immediately implies **finite additivity**: for pairwise disjoint events $A_1, \ldots, A_n$,

    $$
    P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} P(A_i)
    $$

    Simply set $A_{n+1} = A_{n+2} = \cdots = \emptyset$ in Axiom 3.

## Constructing a Probability Measure

For a finite sample space $\Omega = \{\omega_1, \omega_2, \ldots, \omega_n\}$, any assignment of weights $p_1, p_2, \ldots, p_n$ satisfying:

1. $p_i \geq 0$ for all $i$
2. $\sum_{i=1}^{n} p_i = 1$

defines a valid probability measure via $P(\{\omega_i\}) = p_i$.

## Python Example

```python
import numpy as np

# Define a probability measure on Ω = {1, 2, 3, 4, 5, 6}
# Example: loaded die with P(6) = 1/2, others equally likely
omega = [1, 2, 3, 4, 5, 6]
weights = [1/10, 1/10, 1/10, 1/10, 1/10, 1/2]

# Verify Axiom 1: P(Ω) = 1
print(f"Axiom 1: P(Ω) = {sum(weights):.4f}")

# Verify Axiom 2: 0 ≤ P(ω) ≤ 1
print(f"Axiom 2: All probabilities in [0,1]: {all(0 <= w <= 1 for w in weights)}")

# Verify Axiom 3 (finite case): disjoint events
# A = {1, 2}, B = {3, 4}  → disjoint
P_A = weights[0] + weights[1]
P_B = weights[2] + weights[3]
P_AuB = sum(weights[i] for i in [0, 1, 2, 3])
print(f"\nAxiom 3 check:")
print(f"P(A) = {P_A:.4f}, P(B) = {P_B:.4f}")
print(f"P(A) + P(B) = {P_A + P_B:.4f}")
print(f"P(A ∪ B) = {P_AuB:.4f}")
print(f"P(A ∪ B) = P(A) + P(B): {np.isclose(P_AuB, P_A + P_B)}")

# Simulate to verify
np.random.seed(42)
n_sim = 100_000
samples = np.random.choice(omega, size=n_sim, p=weights)
print(f"\nSimulated frequencies:")
for val in omega:
    freq = np.mean(samples == val)
    print(f"  P({val}) = {weights[val-1]:.2f}, simulated = {freq:.4f}")
```

**Output:**
```
Axiom 1: P(Ω) = 1.0000
Axiom 2: All probabilities in [0,1]: True

Axiom 3 check:
P(A) = 0.2000, P(B) = 0.2000
P(A) + P(B) = 0.4000
P(A ∪ B) = 0.4000
P(A ∪ B) = P(A) + P(B): True

Simulated frequencies:
  P(1) = 0.10, simulated = 0.1003
  P(2) = 0.10, simulated = 0.0988
  P(3) = 0.10, simulated = 0.1001
  P(4) = 0.10, simulated = 0.1007
  P(5) = 0.10, simulated = 0.1002
  P(6) = 0.50, simulated = 0.4999
```
