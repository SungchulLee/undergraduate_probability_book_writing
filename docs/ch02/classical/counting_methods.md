# Counting Methods in Probability

## Overview

Under the equally likely model, $P(A) = |A|/|\Omega|$. Computing probabilities therefore reduces to **counting**. This section applies the counting techniques from Chapter 1 to probability problems.

## Strategy for Counting Problems

1. **Define the sample space** $\Omega$ and determine $|\Omega|$
2. **Define the event** $A$ of interest
3. **Count** $|A|$ using appropriate techniques (multiplication rule, permutations, combinations)
4. **Compute** $P(A) = |A|/|\Omega|$

!!! tip "Complement Counting"
    When $A$ is hard to count directly, use:

    $$P(A) = 1 - P(A^c)$$

    Often $|A^c|$ (the "bad" outcomes) is much easier to count than $|A|$.

## Newton–Pepys Problem (1693)

Samuel Pepys posed this question to Isaac Newton: which of the following has the greatest chance of success?

- **A:** Six fair dice are tossed and at least one "6" appears
- **B:** Twelve fair dice are tossed and at least two "6"s appear
- **C:** Eighteen fair dice are tossed and at least three "6"s appear

Pepys thought **C** was most likely. Newton showed that **A** has the highest probability.

### Computing P(A)

$$

|\Omega_A| = 6^6, \qquad |A^c| = 5^6

$$

$$

P(A) = 1 - P(A^c) = 1 - \left(\frac{5}{6}\right)^6 = 0.6651

$$

### Computing P(B)

$$

|\Omega_B| = 6^{12}

$$

The complement $B^c$ includes zero or one "6":

- No "6": $|B_0| = 5^{12}$
- Exactly one "6": $|B_1| = \binom{12}{1} \times 1 \times 5^{11}$

$$

P(B) = 1 - \frac{5^{12}}{6^{12}} - \frac{\binom{12}{1} \cdot 5^{11}}{6^{12}} = 0.6187

$$

### Computing P(C)

$$

|\Omega_C| = 6^{18}

$$

The complement $C^c$ includes zero, one, or two "6"s:

- No "6": $|C_0| = 5^{18}$
- Exactly one "6": $|C_1| = \binom{18}{1} \cdot 5^{17}$
- Exactly two "6"s: $|C_2| = \binom{18}{2} \cdot 5^{16}$

$$

P(C) = 1 - \frac{5^{18}}{6^{18}} - \frac{\binom{18}{1} \cdot 5^{17}}{6^{18}} - \frac{\binom{18}{2} \cdot 5^{16}}{6^{18}} = 0.5973

$$

### Conclusion

$$

P(A) = 0.6651 > P(B) = 0.6187 > P(C) = 0.5973

$$

!!! note "Intuition"
    This result may seem surprising because each scenario has the same expected number of 6's (namely 1, 2, and 3 respectively). The key insight is that the **variance** also increases with more dice, making it more likely to fall short of the target.

## Bertrand's Ballot Theorem (1887)

**Problem:** Candidate A receives $a$ votes and candidate B receives $b$ votes, with $a > b$. If votes are counted in random order, the probability that A is **strictly ahead** of B throughout the entire count is:

$$

P(\text{A strictly ahead throughout}) = \frac{a - b}{a + b}

$$

### Count Pattern as a Lattice Path

Represent the counting process as a path from $(0, 0)$ to $(b, a)$ on a grid:

- Each vote for A → move one unit **up** (U)
- Each vote for B → move one unit **right** (R)

For example, with votes AABABBABAAABAAA:

$$

AABABBABAAABAAA \iff UURURRURUUURUUU

$$

### Proof via the Reflection Principle

The total number of paths:

$$

|\Omega| = \binom{a+b}{b}

$$

**Paths starting with B** (first vote goes to B): these immediately fail the "strictly ahead" condition.

$$

|B_1| = \binom{a+b-1}{b-1}

$$

**Paths starting with A but touching the diagonal** at some point: by the **reflection principle**, these are in one-to-one correspondence with paths starting with B.

$$

|B_2| = |B_1| = \binom{a+b-1}{b-1}

$$

The number of "good" paths (A strictly ahead throughout):

$$

|A| = |\Omega| - |B_1| - |B_2|

$$

$$

P(A) = 1 - \frac{\binom{a+b-1}{b-1}}{\binom{a+b}{b}} - \frac{\binom{a+b-1}{b-1}}{\binom{a+b}{b}} = \frac{a-b}{a+b}

$$

## Python Example

```python
from math import comb
from scipy.stats import binom

# ========================================
# Newton-Pepys Problem
# ========================================
print("=== Newton-Pepys Problem ===\n")

# P(A): at least one 6 in 6 dice
P_A = 1 - (5/6)**6
print(f"P(A) = 1 - (5/6)^6 = {P_A:.4f}")

# P(B): at least two 6s in 12 dice
P_B = 1 - binom.cdf(1, 12, 1/6)
print(f"P(B) = 1 - P(X≤1) where X~Bin(12,1/6) = {P_B:.4f}")

# P(C): at least three 6s in 18 dice
P_C = 1 - binom.cdf(2, 18, 1/6)
print(f"P(C) = 1 - P(X≤2) where X~Bin(18,1/6) = {P_C:.4f}")

print(f"\nP(A) > P(B) > P(C): {P_A > P_B > P_C}")
print(f"Newton was right!")

# ========================================
# Bertrand's Ballot Theorem
# ========================================
print("\n=== Bertrand's Ballot Theorem ===\n")

def ballot_probability(a, b):
    """Exact probability A is strictly ahead throughout."""
    if a <= b:
        return 0.0
    return (a - b) / (a + b)

def ballot_simulation(a, b, n_sim=100_000):
    """Simulate the ballot counting process."""
    import numpy as np
    np.random.seed(42)

    count = 0
    votes = ['A'] * a + ['B'] * b
    for _ in range(n_sim):
        np.random.shuffle(votes)
        ahead = True
        a_count, b_count = 0, 0
        for v in votes:
            if v == 'A':
                a_count += 1
            else:
                b_count += 1
            if a_count <= b_count:
                ahead = False
                break
        if ahead:
            count += 1
    return count / n_sim

# Test cases
for a, b in [(10, 5), (7, 3), (15, 8)]:
    exact = ballot_probability(a, b)
    sim = ballot_simulation(a, b)
    print(f"a={a}, b={b}: P = (a-b)/(a+b) = {a-b}/{a+b} = {exact:.4f}, simulated = {sim:.4f}")
```

**Output:**
```
=== Newton-Pepys Problem ===

P(A) = 1 - (5/6)^6 = 0.6651
P(B) = 1 - P(X≤1) where X~Bin(12,1/6) = 0.6187
P(C) = 1 - P(X≤2) where X~Bin(18,1/6) = 0.5973

P(A) > P(B) > P(C): True
Newton was right!

=== Bertrand's Ballot Theorem ===

a=10, b=5: P = (a-b)/(a+b) = 5/15 = 0.3333, simulated = 0.3337
a=7, b=3: P = (a-b)/(a+b) = 4/10 = 0.4000, simulated = 0.4005
a=15, b=8: P = (a-b)/(a+b) = 7/23 = 0.3043, simulated = 0.3031
```
