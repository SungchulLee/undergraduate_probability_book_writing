# Lattice Path Counting


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Problem Setup

A **lattice path** is a path on the integer grid $\mathbb{Z}^2$ that moves only **right (R)** or **up (U)** at each step. We count the number of such paths from $(0, 0)$ to $(m, n)$.

## Basic Counting

!!! info "Lattice Path Count"
    The number of lattice paths from $(0, 0)$ to $(m, n)$ using exactly $m$ right steps and $n$ up steps is:

    $$\binom{m + n}{m} = \binom{m + n}{n}$$

**Proof.** Each path consists of $m + n$ total steps, of which $m$ must be R and $n$ must be U. The path is completely determined by choosing which $m$ of the $m + n$ positions are R steps. $\square$

**Example.** Paths from $(0,0)$ to $(3,2)$: total steps $= 5$, choose $3$ right steps: $\binom{5}{3} = 10$.

## Connection to the Binomial Coefficients

Each lattice path corresponds to a binary string of length $m + n$ with exactly $m$ ones (R steps) and $n$ zeros (U steps). This establishes a bijection between:

- Lattice paths from $(0,0)$ to $(m,n)$
- Binary strings of length $m+n$ with $m$ ones
- $m$-element subsets of $\{1, 2, \ldots, m+n\}$

## Paths Through a Given Point

The number of lattice paths from $(0,0)$ to $(m,n)$ that pass through intermediate point $(a,b)$ (where $0 \leq a \leq m$ and $0 \leq b \leq n$) is:

$$\binom{a+b}{a} \cdot \binom{(m-a)+(n-b)}{m-a}$$

This follows from the **multiplication rule**: count paths from $(0,0)$ to $(a,b)$ and from $(a,b)$ to $(m,n)$ independently.

## Paths Avoiding a Region: The Reflection Principle

!!! info "Reflection Principle (André)"
    The number of lattice paths from $(0,0)$ to $(m,n)$ that **touch or cross** the line $y = x + c$ (where $c > 0$) equals the total number of lattice paths from the reflected starting point $(-c, c)$ to $(m, n)$, which is $\binom{m+n}{m+c}$ (valid when $n \geq c$).

The reflection principle is a powerful technique used in:

- The **ballot problem**: Candidate A gets $a$ votes, B gets $b$ votes ($a > b$). The probability A is **strictly ahead** throughout the count is $\frac{a - b}{a + b}$.
- Deriving the distribution of the **maximum** of a random walk
- Proving the **arcsine laws** for random walks

## The Ballot Problem

**Problem:** In an election, candidate A receives $a$ votes and B receives $b$ votes, with $a > b$. Assuming all orderings equally likely, what is the probability that A is **strictly ahead of B throughout the entire count**?

!!! info "Ballot Problem Solution"

    $$P(\text{A strictly ahead throughout}) = \frac{a - b}{a + b}$$

**Proof via the Cycle Lemma.** Consider the vote sequence $v_1, v_2, \ldots, v_{a+b}$ where each $v_i = +1$ (vote for A) or $v_i = -1$ (vote for B), with $a$ values of $+1$ and $b$ values of $-1$. Let $S_k = v_1 + \cdots + v_k$ be the running tally, so $S_{a+b} = a - b > 0$. A is strictly ahead throughout if and only if $S_k > 0$ for all $k = 1, \ldots, a+b$.

By the **Cycle Lemma**, for any sequence of integers summing to a positive value $s$, exactly $s$ of the $a+b$ cyclic shifts have all positive partial sums. Since $s = a - b$, and all $\binom{a+b}{a}$ orderings are equally likely, the probability is:

$$P = \frac{a - b}{a + b}$$

## Catalan Numbers

The number of lattice paths from $(0,0)$ to $(n,n)$ that **never go above** the diagonal $y = x$ is the $n$-th **Catalan number**:

!!! info "Catalan Number"

    $$C_n = \frac{1}{n+1}\binom{2n}{n}$$

The first few values are: $C_0 = 1, C_1 = 1, C_2 = 2, C_3 = 5, C_4 = 14, C_5 = 42$.

**Derivation.** Total paths from $(0,0)$ to $(n,n)$: $\binom{2n}{n}$. Bad paths (those that cross the diagonal) are, by reflection about $y = x + 1$, in bijection with paths from $(−1, 1)$ to $(n, n)$, of which there are $\binom{2n}{n+1}$. So:

$$C_n = \binom{2n}{n} - \binom{2n}{n+1} = \frac{1}{n+1}\binom{2n}{n}$$

Catalan numbers count many combinatorial objects: valid parenthesizations, binary trees with $n$ nodes, triangulations of a polygon, non-crossing partitions, and more.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from math import comb, factorial

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# --- Panel 1: All lattice paths from (0,0) to (3,2) ---
from itertools import combinations

m, n = 3, 2
total_steps = m + n
paths = list(combinations(range(total_steps), m))  # positions of R steps

for path_r in paths:
    x, y = [0], [0]
    for step in range(total_steps):
        if step in path_r:
            x.append(x[-1] + 1)
            y.append(y[-1])
        else:
            x.append(x[-1])
            y.append(y[-1] + 1)
    axes[0].plot(x, y, alpha=0.5, lw=1.5)

axes[0].set_title(f'All {comb(total_steps, m)} lattice paths (0,0)→({m},{n})')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].set_xticks(range(m + 1))
axes[0].set_yticks(range(n + 1))
axes[0].grid(True, alpha=0.3)
axes[0].set_aspect('equal')

# --- Panel 2: Ballot problem simulation ---
np.random.seed(42)
a_votes, b_votes = 7, 3
n_sim = 100000
ahead_count = 0

for _ in range(n_sim):
    ballot = np.random.permutation([1]*a_votes + [-1]*b_votes)
    cumsum = np.cumsum(ballot)
    if np.all(cumsum > 0):
        ahead_count += 1

p_sim = ahead_count / n_sim
p_theory = (a_votes - b_votes) / (a_votes + b_votes)

axes[1].bar(['Simulated', 'Theory'], [p_sim, p_theory],
            color=['steelblue', 'coral'], alpha=0.7)
axes[1].set_title(f'Ballot Problem: a={a_votes}, b={b_votes}')
axes[1].set_ylabel('P(A strictly ahead)')
for i, v in enumerate([p_sim, p_theory]):
    axes[1].text(i, v + 0.01, f'{v:.4f}', ha='center', fontsize=11)
axes[1].grid(True, alpha=0.3)

# --- Panel 3: Catalan numbers ---
ns = np.arange(0, 15)
catalans = [comb(2*nn, nn) // (nn + 1) for nn in ns]

axes[2].bar(ns, catalans, color='steelblue', alpha=0.7)
axes[2].set_title('Catalan Numbers $C_n$')
axes[2].set_xlabel('n')
axes[2].set_ylabel('$C_n$')
axes[2].set_yscale('log')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('lattice_paths.png', dpi=150, bbox_inches='tight')
plt.show()
```
