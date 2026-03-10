# Lattice Path Counting

Lattice paths connect combinatorics to geometry: counting paths on an integer grid reduces to choosing subsets, and restrictions on paths lead to deep results including the ballot problem and Catalan numbers.

## Definition

A **lattice path** from $(0,0)$ to $(m,n)$ is a sequence of $m + n$ steps on $\mathbb{Z}^2$, each either right (R) or up (U). The number of such paths is

$$
\binom{m+n}{m} = \binom{m+n}{n}
$$

since each path is determined by choosing which $m$ of the $m+n$ positions are R steps.

## Explanation

### Bijections

Each lattice path from $(0,0)$ to $(m,n)$ corresponds to:

- A binary string of length $m+n$ with exactly $m$ ones (R) and $n$ zeros (U)
- An $m$-element subset of $\{1, 2, \ldots, m+n\}$

These bijections let us translate between path-counting and subset-counting problems freely.

### Paths Through a Given Point

The number of lattice paths from $(0,0)$ to $(m,n)$ that pass through $(a,b)$ (with $0 \le a \le m$, $0 \le b \le n$) is

$$
\binom{a+b}{a} \cdot \binom{(m-a)+(n-b)}{m-a}
$$

by the multiplication rule: independently count paths from $(0,0)$ to $(a,b)$ and from $(a,b)$ to $(m,n)$.

### The Reflection Principle

To count paths that *avoid* a boundary, we use André's reflection principle. The idea: establish a bijection between "bad" paths (those that touch a forbidden line) and unrestricted paths from a reflected starting point.

**Setup.** Consider lattice paths from $(0,0)$ to $(m,n)$. A path is "bad" if it touches or crosses the line $y = x + c$ (where $c \ge 1$). At the first point where a bad path touches $y = x + c$, reflect the initial segment of the path about that line. This maps the starting point $(0,0)$ to its reflection $(-c, c)$, and the mapping is a bijection between bad paths and all paths from $(-c, c)$ to $(m,n)$.

A path from $(-c, c)$ to $(m,n)$ uses $m + c$ right steps and $n - c$ up steps, so the number of bad paths is $\binom{m+n}{m+c}$ (provided $n \ge c$).

### The Ballot Problem

**Problem.** Candidate A receives $a$ votes and B receives $b$ votes ($a > b$). If all orderings are equally likely, the probability that A is strictly ahead throughout the entire count is

$$
P(\text{A strictly ahead throughout}) = \frac{a - b}{a + b}
$$

**Proof.** Represent the vote sequence as a lattice path from $(0,0)$ to $(b, a)$, where a vote for A is an up step and a vote for B is a right step. A is strictly ahead throughout iff the path stays strictly above the diagonal $y = x$, i.e., never touches $y = x$. By the reflection principle (reflecting about $y = x$), the number of bad paths (touching $y = x$) equals the number of unrestricted paths from $(1, -1)$ to $(b, a)$, which is $\binom{a+b}{b-1}$.

Good paths: $\binom{a+b}{b} - \binom{a+b}{b-1}$. The probability is

$$
\frac{\binom{a+b}{b} - \binom{a+b}{b-1}}{\binom{a+b}{b}} = 1 - \frac{b}{a+1} \cdot \frac{(a+1)}{a+b} \cdot \ldots
$$

A slicker calculation uses the identity $\binom{a+b}{b} - \binom{a+b}{b-1} = \frac{a-b+1}{a+1}\binom{a+b}{b}$.

Actually, the cleanest approach: among the $a+b$ cyclic shifts of any vote sequence with sum $a - b > 0$, exactly $a - b$ shifts have all partial sums positive (Cycle Lemma). Since all $\binom{a+b}{a}$ orderings are equally likely, and each sequence contributes $(a-b)$ good cyclic shifts out of $(a+b)$ total, the fraction of good orderings is $(a-b)/(a+b)$.

### Catalan Numbers

The number of lattice paths from $(0,0)$ to $(n,n)$ that never go above the diagonal $y = x$ is the $n$-th Catalan number:

$$
C_n = \frac{1}{n+1}\binom{2n}{n}
$$

**Derivation.** Total paths: $\binom{2n}{n}$. Bad paths cross $y = x$, which means they touch $y = x + 1$. By reflection about $y = x + 1$, bad paths biject with paths from $(-1, 1)$ to $(n, n)$, which use $n + 1$ right steps and $n - 1$ up steps: $\binom{2n}{n+1}$.

$$
C_n = \binom{2n}{n} - \binom{2n}{n+1} = \frac{1}{n+1}\binom{2n}{n}
$$

The first values are $C_0 = 1,\; C_1 = 1,\; C_2 = 2,\; C_3 = 5,\; C_4 = 14,\; C_5 = 42$.

## Examples

**Example (All paths from $(0,0)$ to $(3,2)$).** There are $\binom{5}{3} = 10$ lattice paths. Listing them as binary strings (R=1, U=0):

$$
\text{RRRUU},\; \text{RRUРУ},\; \text{RRUUR},\; \text{RURRU},\; \text{RURUR},\; \text{RUУРР},\; \text{URRRU},\; \text{URRUR},\; \text{URURR},\; \text{UURRR}
$$

The figure below plots all 10 paths, simulates the ballot problem, and displays Catalan numbers.

```python
import numpy as np
import matplotlib.pyplot as plt
from math import comb
from itertools import combinations

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Panel 1: All lattice paths (0,0) -> (3,2)
m, n = 3, 2
total_steps = m + n
paths = list(combinations(range(total_steps), m))

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

# Panel 2: Ballot problem simulation
np.random.seed(42)
a_votes, b_votes = 7, 3
n_sim = 100_000
ahead_count = 0

for _ in range(n_sim):
    ballot = np.random.permutation([1] * a_votes + [-1] * b_votes)
    if np.all(np.cumsum(ballot) > 0):
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

# Panel 3: Catalan numbers
ns = np.arange(0, 15)
catalans = [comb(2 * nn, nn) // (nn + 1) for nn in ns]

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
