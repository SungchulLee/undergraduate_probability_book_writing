# Sample Spaces and Outcomes

## Overview

The foundation of probability theory begins with the concept of an **experiment** — any procedure that produces observable outcomes. Before we can assign probabilities, we must carefully describe what outcomes are possible.

## Sample

A **sample** (or **outcome**) is a possible result of an experiment. We denote an individual outcome by $\omega$.

!!! example "Examples of Samples"
    - Flipping a coin: $\omega = H$ or $\omega = T$
    - Rolling a die: $\omega \in \{1, 2, 3, 4, 5, 6\}$
    - Measuring a stock return: $\omega \in \mathbb{R}$

## Sample Space

The **sample space** $\Omega$ is the set of all possible outcomes of an experiment.

$$

\Omega = \{\text{all possible outcomes } \omega\}

$$

!!! example "Examples of Sample Spaces"
    - **Coin flip:** $\Omega = \{H, T\}$
    - **Rolling a die:** $\Omega = \{1, 2, 3, 4, 5, 6\}$
    - **Flipping a fair coin three times:**

    $$

    \Omega = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}

    $$

    Here $|\Omega| = 8$.

    - **Measuring a stock price:** $\Omega = [0, \infty)$

## Finite vs. Infinite Sample Spaces

Sample spaces can be classified by their size:

- **Finite:** $\Omega$ contains finitely many outcomes (e.g., rolling a die)
- **Countably infinite:** $\Omega$ can be put in one-to-one correspondence with the natural numbers (e.g., counting the number of trades until a profit)
- **Uncountable:** $\Omega$ has the cardinality of the continuum (e.g., measuring a continuous quantity like a stock return)

The mathematical treatment of probability differs depending on whether $\Omega$ is discrete (finite or countably infinite) or continuous (uncountable).

## Probability Measure

For each outcome $\omega$ in $\Omega$, we attach a "weight" — think of it as a brick placed on that outcome. Each brick may have a different weight, but the total weight of all bricks is 1. This weight distribution over the sample space $\Omega$ is a **probability measure**.

$$

P(\omega) = \text{Weight of the brick attached to } \omega

$$

For any event $A \subseteq \Omega$:

$$

P(A) = \sum_{\omega \in A} P(\omega) = \text{Total weight of the bricks attached to } A

$$

!!! note "The Brick Analogy"
    The brick analogy provides powerful intuition:

    - Every outcome gets exactly one brick
    - Bricks can have different weights (but all non-negative)
    - The total weight of all bricks equals 1
    - The probability of an event is the total weight of bricks in that event

## Python Example

```python
import numpy as np

# Sample space for flipping a fair coin three times
omega = ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']

# Equally likely probability measure
prob = {outcome: 1/len(omega) for outcome in omega}

print("Sample space:", omega)
print(f"|Ω| = {len(omega)}")
print(f"\nProbability of each outcome: {1/len(omega):.4f}")

# Event A: at least two heads
A = [w for w in omega if w.count('H') >= 2]
P_A = sum(prob[w] for w in A)
print(f"\nEvent A (at least 2 heads): {A}")
print(f"P(A) = {len(A)}/{len(omega)} = {P_A:.4f}")
```

**Output:**
```
Sample space: ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']
|Ω| = 8
Probability of each outcome: 0.1250

Event A (at least 2 heads): ['HHH', 'HHT', 'HTH', 'THH']
P(A) = 4/8 = 0.5000
```
