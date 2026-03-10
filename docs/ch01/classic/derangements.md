# Matching Problem and Derangements


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

The **matching problem** (also called the **hat-check problem** or **problème des rencontres**) asks: how many bijective functions on $\{1, 2, \ldots, n\}$ have **no fixed points**? Such a permutation is called a **derangement**.

## Setup

Let $f$ be a bijective function (permutation) on $\{1, 2, \ldots, n\}$.

A point $x$ is called a **fixed point** of $f$ if $f(x) = x$.

**Goal:** Count the number of permutations with **no** fixed points (derangements).

### Define the Sets

- $\Omega$ — the set of all bijective functions $f$ on $\{1, 2, \ldots, n\}$, so $|\Omega| = n!$
- $A_i$ — the set of bijective functions $f$ that fix $i$ (i.e., $f(i) = i$)
- $\bigcup_{i=1}^{n} A_i$ — the set of bijective functions that fix **some** $i$
- $B = \Omega \setminus \bigcup_{i=1}^{n} A_i$ — the set of bijective functions with **no** fixed points (derangements)

## Applying Inclusion-Exclusion

We need $|B| = |\Omega| - |\bigcup_{i=1}^{n} A_i|$, so we first compute $|\bigcup_{i=1}^{n} A_i|$.

### Computing Intersection Sizes

**Single sets:** $|A_i|$ counts permutations fixing $i$. The remaining $n - 1$ elements can be permuted freely:

$$|A_i| = (n-1)!$$

There are $\binom{n}{1}$ such sets, so $\sum |A_i| = \binom{n}{1}(n-1)!$.

**Pairwise intersections:** $|A_i \cap A_j|$ counts permutations fixing both $i$ and $j$:

$$|A_i \cap A_j| = (n-2)!$$

There are $\binom{n}{2}$ such pairs, so $\sum |A_i \cap A_j| = \binom{n}{2}(n-2)!$.

**General pattern:** $|A_{i_1} \cap A_{i_2} \cap \cdots \cap A_{i_k}|$ counts permutations fixing $k$ specified points:

$$|A_{i_1} \cap \cdots \cap A_{i_k}| = (n-k)!$$

There are $\binom{n}{k}$ such $k$-element subsets.

### Applying the Formula

By the inclusion-exclusion principle:

$$\left|\bigcup_{i=1}^{n} A_i\right| = \sum_{k=1}^{n} (-1)^{k+1} \binom{n}{k} (n-k)!$$

Expanding $\binom{n}{k}(n-k)! = \frac{n!}{k!}$:

$$\left|\bigcup_{i=1}^{n} A_i\right| = n! \left(\frac{1}{1!} - \frac{1}{2!} + \frac{1}{3!} - \cdots + (-1)^{n+1}\frac{1}{n!}\right)$$

### The Derangement Count

$$|B| = |\Omega| - \left|\bigcup_{i=1}^{n} A_i\right| = n! - n!\left(\frac{1}{1!} - \frac{1}{2!} + \cdots + (-1)^{n+1}\frac{1}{n!}\right)$$

$$\boxed{D_n = n!\left(1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \cdots + (-1)^n \frac{1}{n!}\right) = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}}$$

## Connection to e^(-1)

As $n \to \infty$, the sum $\sum_{k=0}^{n} \frac{(-1)^k}{k!}$ converges to $e^{-1}$. Therefore:

$$D_n \approx \frac{n!}{e}$$

More precisely, $D_n$ is the nearest integer to $n!/e$ for all $n \geq 1$.

The probability that a random permutation is a derangement is:

$$\frac{D_n}{n!} = \sum_{k=0}^{n} \frac{(-1)^k}{k!} \xrightarrow{n \to \infty} e^{-1} \approx 0.3679$$

## Python Implementation

```python
from math import factorial, e, comb

def derangement_count(n):
    """
    Count the number of derangements of {1, 2, ..., n}
    using the inclusion-exclusion formula.
    
    Parameters
    ----------
    n : int
        Size of the set.
    
    Returns
    -------
    int
        Number of derangements D_n.
    """
    return sum((-1)**k * factorial(n) // factorial(k) for k in range(n + 1))

def derangement_count_via_ie(n):
    """
    Count derangements step by step using inclusion-exclusion.
    Shows: |Omega| - |union of A_i|.
    """
    omega = factorial(n)
    # |union A_i| via inclusion-exclusion
    union_size = sum(
        (-1)**(k+1) * comb(n, k) * factorial(n - k) 
        for k in range(1, n + 1)
    )
    return omega - union_size

# Compute derangements for small n
print("n | D_n | n! | D_n/n! | 1/e")
print("-" * 45)
for n in range(1, 11):
    d_n = derangement_count(n)
    n_fact = factorial(n)
    ratio = d_n / n_fact
    print(f"{n:2d} | {d_n:7d} | {n_fact:7d} | {ratio:.6f} | {1/e:.6f}")

# Verify both methods agree
for n in range(1, 15):
    assert derangement_count(n) == derangement_count_via_ie(n)
print("\nBoth methods agree for n=1..14")

# Enumerate derangements for small n
from itertools import permutations

def enumerate_derangements(n):
    """Enumerate all derangements by brute force."""
    identity = list(range(1, n + 1))
    count = 0
    for perm in permutations(identity):
        if all(perm[i] != identity[i] for i in range(n)):
            count += 1
    return count

print("\nVerification by enumeration:")
for n in range(1, 9):
    d_formula = derangement_count(n)
    d_enum = enumerate_derangements(n)
    print(f"  n={n}: formula={d_formula}, enumeration={d_enum}, match={d_formula==d_enum}")
```

## Key Takeaway

The matching problem is the canonical application of inclusion-exclusion combined with complement counting. The derangement formula $D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$ emerges from systematically subtracting and adding permutations that fix specific subsets of points. The remarkable result $D_n/n! \to 1/e$ connects discrete combinatorics to the exponential function.
