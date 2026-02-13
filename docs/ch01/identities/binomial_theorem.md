# Binomial Theorem

## Overview

The **binomial theorem** provides the expansion of $(x + y)^n$ as a sum of terms involving binomial coefficients. It connects algebra to combinatorics: each coefficient counts the number of ways to choose terms in the expansion.

## Statement

$$\boxed{(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}}$$

where the **binomial coefficient** is:

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

## Combinatorial Interpretation

When expanding $(x + y)^n = (x + y)(x + y) \cdots (x + y)$, each term in the expansion is formed by choosing either $x$ or $y$ from each of the $n$ factors.

The term $x^k y^{n-k}$ arises whenever we choose $x$ from exactly $k$ of the $n$ factors (and $y$ from the remaining $n - k$ factors). The number of ways to make this choice is $\binom{n}{k}$.

## Special Cases

**Setting $x = y = 1$:**

$$2^n = \sum_{k=0}^{n} \binom{n}{k}$$

This says the total number of subsets of an $n$-element set is $2^n$.

**Setting $x = 1, y = -1$:**

$$0 = \sum_{k=0}^{n} (-1)^k \binom{n}{k}$$

This says the number of even-sized subsets equals the number of odd-sized subsets.

## Multinomial Generalization

The **multinomial expansion** generalizes the binomial theorem to $m$ terms:

$$(x_1 + x_2 + \cdots + x_m)^n = \sum_{k_1 + k_2 + \cdots + k_m = n} \binom{n}{k_1 \; k_2 \; \cdots \; k_m} x_1^{k_1} x_2^{k_2} \cdots x_m^{k_m}$$

where the **multinomial coefficient** is:

$$\binom{n}{k_1 \; k_2 \; \cdots \; k_m} = \frac{n!}{k_1! \, k_2! \cdots k_m!}$$

## Python Implementation

```python
from math import comb, factorial

def binomial_expansion(n):
    """
    Return the coefficients in the expansion of (x + y)^n.
    
    Parameters
    ----------
    n : int
        The exponent.
    
    Returns
    -------
    list of int
        Binomial coefficients [C(n,0), C(n,1), ..., C(n,n)].
    """
    return [comb(n, k) for k in range(n + 1)]

# Example: (x + y)^5
n = 5
coeffs = binomial_expansion(n)
print(f"(x + y)^{n} coefficients: {coeffs}")
# Output: [1, 5, 10, 10, 5, 1]

# Verify: sum of coefficients = 2^n
print(f"Sum of coefficients: {sum(coeffs)}")
print(f"2^{n} = {2**n}")

# Verify alternating sum = 0
alt_sum = sum((-1)**k * c for k, c in enumerate(coeffs))
print(f"Alternating sum: {alt_sum}")

# Multinomial expansion: (x + y + z)^3
n = 3
print(f"\n(x + y + z)^{n} expansion:")
for k1 in range(n + 1):
    for k2 in range(n - k1 + 1):
        k3 = n - k1 - k2
        coeff = factorial(n) // (factorial(k1) * factorial(k2) * factorial(k3))
        terms = []
        if k1 > 0:
            terms.append(f"x^{k1}" if k1 > 1 else "x")
        if k2 > 0:
            terms.append(f"y^{k2}" if k2 > 1 else "y")
        if k3 > 0:
            terms.append(f"z^{k3}" if k3 > 1 else "z")
        term_str = " * ".join(terms) if terms else "1"
        print(f"  {coeff} * {term_str}")
```

## Key Takeaway

The binomial theorem bridges algebra and combinatorics. The coefficient $\binom{n}{k}$ in the expansion of $(x+y)^n$ counts the number of ways to select $k$ factors contributing $x$ (and $n-k$ contributing $y$). The multinomial expansion generalizes this to any number of terms, with coefficients given by the multinomial coefficient.
