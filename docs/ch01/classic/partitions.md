# Partition Problems

## Distributing Objects into Boxes

Many counting problems reduce to distributing $n$ objects into $k$ boxes under various constraints. The answer depends on whether the objects and boxes are **distinguishable** or **indistinguishable**.

## Summary of Cases

!!! info "Distribution Counting"
    | Objects | Boxes | Constraint | Formula |
    |:---:|:---:|:---:|:---:|
    | Distinguishable | Distinguishable | None | $k^n$ |
    | Distinguishable | Distinguishable | At most 1 per box ($n \leq k$) | $k!/(k-n)!$ |
    | Distinguishable | Distinguishable | Exactly 1 per box ($n = k$) | $k!$ |
    | Indistinguishable | Distinguishable | None | $\binom{n+k-1}{k-1}$ |
    | Indistinguishable | Distinguishable | At least 1 per box | $\binom{n-1}{k-1}$ |
    | Distinguishable | Indistinguishable | None | $\sum_{j=1}^{k} S(n,j)$ |
    | Indistinguishable | Indistinguishable | None | $p_k(n)$ |

Here $S(n, k)$ denotes the **Stirling number of the second kind** and $p_k(n)$ denotes the number of **partitions of $n$ into at most $k$ parts**.

## Case 1: Distinguishable Objects, Distinguishable Boxes (No Constraint)

Each of $n$ objects independently goes into one of $k$ boxes. By the multiplication rule: $k^n$.

**Example.** Assign 3 students to 4 groups: $4^3 = 64$ ways.

## Case 2: Indistinguishable Objects, Distinguishable Boxes — Stars and Bars

This is the classic **stars and bars** problem (covered in Section 1.3).

!!! info "Stars and Bars"
    The number of ways to distribute $n$ identical objects into $k$ distinct boxes is:

    $$\binom{n + k - 1}{k - 1}$$

    With the constraint "each box gets at least 1":

    $$\binom{n - 1}{k - 1}$$

**Example.** Distribute 10 identical cookies to 4 children: $\binom{13}{3} = 286$ ways.

**With at least 1 each:** First give 1 to each child (using 4), then distribute remaining 6 freely: $\binom{9}{3} = 84$.

## Case 3: Distinguishable Objects, Indistinguishable Boxes — Stirling Numbers

When boxes are indistinguishable, the number of ways to partition $n$ distinct objects into exactly $k$ non-empty groups is the **Stirling number of the second kind** $S(n, k)$.

!!! info "Stirling Number of the Second Kind"
    $S(n, k)$ counts the number of ways to partition a set of $n$ elements into exactly $k$ non-empty subsets.

    $$S(n, k) = \frac{1}{k!} \sum_{j=0}^{k} (-1)^{k-j} \binom{k}{j} j^n$$

    **Recurrence:** $S(n, k) = k \cdot S(n-1, k) + S(n-1, k-1)$

    **Boundary conditions:** $S(n, 1) = S(n, n) = 1$, and $S(n, 0) = 0$ for $n \geq 1$.

**Example.** Partition $\{a, b, c\}$ into 2 non-empty groups:

$\{a\}\{b,c\}$, $\{b\}\{a,c\}$, $\{c\}\{a,b\}$ — so $S(3, 2) = 3$.

## Case 4: Indistinguishable Objects, Indistinguishable Boxes — Integer Partitions

The number of ways to write $n$ as a sum of at most $k$ positive integers, where the order of summands does not matter, is the **partition function** $p_k(n)$.

**Example.** Partitions of 5 into at most 3 parts: $5$, $4+1$, $3+2$, $3+1+1$, $2+2+1$ — so $p_3(5) = 5$.

## The Bell Numbers

The **Bell number** $B_n$ counts the total number of partitions of an $n$-element set into any number of non-empty subsets:

$$B_n = \sum_{k=0}^{n} S(n, k)$$

The first few: $B_0 = 1, B_1 = 1, B_2 = 2, B_3 = 5, B_4 = 15, B_5 = 52$.

## The Twelvefold Way

The table above is part of what combinatorialists call the **twelvefold way** — a systematic classification of distribution problems by whether objects/boxes are distinguishable and whether each box can hold any number, at most one, or at least one.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from math import comb, factorial
from functools import lru_cache

# Stirling numbers
@lru_cache(maxsize=None)
def stirling2(n, k):
    if k == 0:
        return 1 if n == 0 else 0
    if k == 1 or k == n:
        return 1
    if k > n:
        return 0
    return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)

# Bell numbers
def bell(n):
    return sum(stirling2(n, k) for k in range(n + 1))

# Integer partitions
@lru_cache(maxsize=None)
def partitions(n, max_part=None):
    if max_part is None:
        max_part = n
    if n == 0:
        return 1
    if n < 0 or max_part == 0:
        return 0
    return partitions(n - max_part, max_part) + partitions(n, max_part - 1)

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# --- Panel 1: Stirling triangle ---
N = 8
triangle = np.zeros((N + 1, N + 1))
for n in range(N + 1):
    for k in range(N + 1):
        triangle[n, k] = stirling2(n, k)

im = axes[0].imshow(triangle[1:, 1:], cmap='YlOrRd', aspect='auto')
for i in range(N):
    for j in range(N):
        val = int(triangle[i + 1, j + 1])
        if val > 0:
            axes[0].text(j, i, str(val), ha='center', va='center', fontsize=7)
axes[0].set_title('Stirling Numbers S(n,k)')
axes[0].set_xlabel('k')
axes[0].set_ylabel('n')
axes[0].set_xticks(range(N))
axes[0].set_xticklabels(range(1, N + 1))
axes[0].set_yticks(range(N))
axes[0].set_yticklabels(range(1, N + 1))

# --- Panel 2: Bell numbers ---
ns = range(0, 13)
bells = [bell(n) for n in ns]
axes[1].bar(list(ns), bells, color='steelblue', alpha=0.7)
axes[1].set_title('Bell Numbers $B_n$')
axes[1].set_xlabel('n')
axes[1].set_ylabel('$B_n$')
axes[1].set_yscale('log')
axes[1].grid(True, alpha=0.3)

# --- Panel 3: Comparison of distribution formulas ---
n_objects = 6
ks = range(1, 7)

dist_dist = [k**n_objects for k in ks]           # dist obj, dist box
stars_bars = [comb(n_objects + k - 1, k - 1) for k in ks]  # indist obj, dist box
stirling_vals = [sum(stirling2(n_objects, j) for j in range(1, k+1)) for k in ks]
part_vals = [partitions(n_objects, k) for k in ks]

axes[2].plot(list(ks), dist_dist, 'ro-', label='Dist-Dist: $k^n$', lw=2)
axes[2].plot(list(ks), stars_bars, 'bs-', label='Indist-Dist: Stars&Bars', lw=2)
axes[2].plot(list(ks), stirling_vals, 'g^-', label='Dist-Indist: Stirling', lw=2)
axes[2].plot(list(ks), part_vals, 'mD-', label='Indist-Indist: Partitions', lw=2)
axes[2].set_title(f'Distribution Problems (n={n_objects} objects)')
axes[2].set_xlabel('k (number of boxes)')
axes[2].set_ylabel('Count')
axes[2].set_yscale('log')
axes[2].legend(fontsize=8)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('partitions.png', dpi=150, bbox_inches='tight')
plt.show()
```
