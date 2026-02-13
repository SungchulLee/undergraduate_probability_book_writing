# Pascal's Rule and Vandermonde's Identity

## Overview

Combinatorial identities often arise from counting the same quantity in two different ways. This section presents **Pascal's rule** and **Vandermonde's identity**, two fundamental identities involving binomial coefficients.

## Pascal's Rule

### Statement

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

### Combinatorial Proof

Consider forming a committee of $k$ people from $n$ people. Fix one person, say person $X$:

- **$X$ is on the committee:** Choose the remaining $k - 1$ members from the other $n - 1$ people: $\binom{n-1}{k-1}$
- **$X$ is not on the committee:** Choose all $k$ members from the other $n - 1$ people: $\binom{n-1}{k}$

These two cases are disjoint and exhaustive, so by the addition rule:

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

Pascal's rule generates **Pascal's triangle**, where each entry is the sum of the two entries above it.

## Vandermonde's Identity

### Statement

$$\binom{m + n}{k} = \sum_{\ell = \max(0, k-n)}^{\min(m, k)} \binom{m}{\ell} \binom{n}{k - \ell}$$

When the bounds are clear (i.e., $\binom{m}{\ell} = 0$ for $\ell > m$ and $\binom{n}{k-\ell} = 0$ for $k - \ell > n$), this simplifies to:

$$\binom{m + n}{k} = \sum_{\ell=0}^{k} \binom{m}{\ell} \binom{n}{k - \ell}$$

### Combinatorial Proof — Committee from Men and Women

Consider choosing a committee of $k$ people from a group of $m$ men and $n$ women.

**Method 1 (direct):** Choose $k$ people from all $m + n$: $\binom{m+n}{k}$

**Method 2 (by gender composition):** Choose $\ell$ men and $k - \ell$ women:

- Choose $\ell$ men from $m$: $\binom{m}{\ell}$
- Choose $k - \ell$ women from $n$: $\binom{n}{k-\ell}$
- Sum over all valid values of $\ell$: $\sum_\ell \binom{m}{\ell}\binom{n}{k-\ell}$

Since both methods count the same thing:

$$\binom{m+n}{k} = \sum_{\ell} \binom{m}{\ell} \binom{n}{k-\ell}$$

## Python Implementation

```python
from math import comb

def verify_pascal(n, k):
    """Verify Pascal's rule: C(n,k) = C(n-1,k-1) + C(n-1,k)."""
    lhs = comb(n, k)
    rhs = comb(n - 1, k - 1) + comb(n - 1, k)
    return lhs, rhs, lhs == rhs

def verify_vandermonde(m, n, k):
    """Verify Vandermonde's identity: C(m+n, k) = sum_l C(m,l)*C(n,k-l)."""
    lhs = comb(m + n, k)
    rhs = sum(comb(m, l) * comb(n, k - l) for l in range(k + 1))
    return lhs, rhs, lhs == rhs

# Verify Pascal's rule
for n in range(2, 8):
    for k in range(1, n):
        lhs, rhs, ok = verify_pascal(n, k)
        assert ok, f"Failed for n={n}, k={k}"
print("Pascal's rule verified for n=2..7, all valid k")

# Verify Vandermonde's identity
m, n, k = 5, 7, 4
lhs, rhs, ok = verify_vandermonde(m, n, k)
print(f"\nVandermonde: C({m}+{n}, {k}) = {lhs}")
print(f"Sum of C({m},l)*C({n},{k}-l) = {rhs}")
print(f"Match: {ok}")

# Show the breakdown
print(f"\nBreakdown (m={m} men, n={n} women, committee of {k}):")
for l in range(k + 1):
    c_m = comb(m, l)
    c_n = comb(n, k - l)
    if c_m > 0 and c_n > 0:
        print(f"  {l} men, {k-l} women: C({m},{l})*C({n},{k-l}) = {c_m}*{c_n} = {c_m*c_n}")

# Generate Pascal's triangle
print("\nPascal's Triangle (rows 0-7):")
for row in range(8):
    values = [comb(row, k) for k in range(row + 1)]
    print(f"  Row {row}: {values}")
```

## Key Takeaway

Pascal's rule and Vandermonde's identity are both proved elegantly by the "two ways of counting" technique. Pascal's rule partitions by the status of one fixed element; Vandermonde's identity partitions by the composition across two disjoint groups. Both identities are fundamental building blocks in combinatorics and probability.
