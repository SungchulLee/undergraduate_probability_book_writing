# Matching Problem and Derangements

The matching problem (also called the hat-check problem or *problème des rencontres*) asks how many permutations of $\{1, 2, \ldots, n\}$ have no fixed points. It is the canonical application of inclusion-exclusion combined with complement counting.

## Definition

A **derangement** of $\{1, 2, \ldots, n\}$ is a permutation $\sigma$ such that $\sigma(i) \neq i$ for every $i$. The number of derangements is denoted $D_n$ and equals

$$
D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}
$$

Equivalently, $D_n$ is the nearest integer to $n!/e$ for all $n \geq 1$.

## Explanation

### Derivation via Inclusion-Exclusion

Define the following sets over the space $\Omega$ of all $n!$ permutations:

- $A_i$ = permutations that fix element $i$ (i.e., $\sigma(i) = i$)
- $\bigcup_{i=1}^n A_i$ = permutations with **at least one** fixed point
- $B = \Omega \setminus \bigcup_{i=1}^n A_i$ = derangements (no fixed points)

We need $|B| = n! - |\bigcup A_i|$, so we compute $|\bigcup A_i|$ by inclusion-exclusion.

**Intersection sizes.** A permutation that fixes a specified set of $k$ elements can permute the remaining $n - k$ elements freely, so

$$
|A_{i_1} \cap \cdots \cap A_{i_k}| = (n - k)!
$$

There are $\binom{n}{k}$ ways to choose which $k$ elements are fixed. Thus

$$
\left|\bigcup_{i=1}^{n} A_i\right| = \sum_{k=1}^{n} (-1)^{k+1} \binom{n}{k}(n-k)!
$$

**Simplification.** Since $\binom{n}{k}(n-k)! = \frac{n!}{k!}$, we have

$$
\left|\bigcup_{i=1}^{n} A_i\right| = n!\left(\frac{1}{1!} - \frac{1}{2!} + \frac{1}{3!} - \cdots + (-1)^{n+1}\frac{1}{n!}\right)
$$

**Result.** Subtracting from $n!$:

$$
D_n = n! - n!\left(\frac{1}{1!} - \frac{1}{2!} + \cdots + (-1)^{n+1}\frac{1}{n!}\right) = n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}
$$

### Asymptotic Probability

The probability that a uniformly random permutation is a derangement is

$$
\frac{D_n}{n!} = \sum_{k=0}^{n} \frac{(-1)^k}{k!} \xrightarrow{n \to \infty} e^{-1} \approx 0.3679
$$

The convergence is extremely fast — already at $n = 5$, the ratio agrees with $1/e$ to four decimal places. This means that for any reasonably large $n$, roughly 36.8% of all permutations are derangements.

## Examples

**Example 1 (Small cases).** Enumerate derangements for small $n$:

| $n$ | All permutations | Derangements | $D_n$ | $D_n / n!$ |
|:---:|:---|:---|:---:|:---:|
| 1 | $(1)$ | none | 0 | 0 |
| 2 | $(1,2),\;(2,1)$ | $(2,1)$ | 1 | 0.5 |
| 3 | 6 permutations | $(2,3,1),\;(3,1,2)$ | 2 | 0.333 |
| 4 | 24 permutations | 9 derangements | 9 | 0.375 |

For $n=4$: $D_4 = 4!\left(1 - 1 + \tfrac{1}{2} - \tfrac{1}{6} + \tfrac{1}{24}\right) = 24 \cdot \tfrac{9}{24} = 9$.

---

**Example 2 (Hat-check problem).** Ten guests check their hats. The hats are returned at random (uniformly). What is the probability that nobody gets their own hat?

$$
P(\text{no match}) = \frac{D_{10}}{10!} = \sum_{k=0}^{10} \frac{(-1)^k}{k!} \approx 0.3679
$$

So there is about a 36.8% chance that no guest receives their own hat — almost independent of the number of guests.

```python
from math import factorial, e
from itertools import permutations

def derangement_count(n):
    """Count derangements D_n via inclusion-exclusion."""
    return sum((-1)**k * factorial(n) // factorial(k) for k in range(n + 1))

# Table of D_n and D_n/n!
print("  n |     D_n |      n! |   D_n/n! |      1/e")
print("-" * 50)
for n in range(1, 11):
    d_n = derangement_count(n)
    n_fact = factorial(n)
    print(f" {n:2d} | {d_n:7d} | {n_fact:7d} | {d_n/n_fact:.6f} | {1/e:.6f}")

# Verify against brute-force enumeration for small n
for n in range(1, 9):
    identity = list(range(1, n + 1))
    brute = sum(
        1 for p in permutations(identity)
        if all(p[i] != identity[i] for i in range(n))
    )
    formula = derangement_count(n)
    assert brute == formula, f"Mismatch at n={n}"
print("\nFormula matches brute force for n=1..8")
```
