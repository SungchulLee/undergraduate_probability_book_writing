# Multinomial Coefficients

## Overview

The **multinomial coefficient** generalizes the binomial coefficient to partitioning $n$ objects into more than two groups. It counts the number of ways to divide $n$ distinct objects into groups of specified sizes, or equivalently, the number of distinct arrangements of objects with repeated types.

## Definition

The multinomial coefficient is:

$$\binom{n}{k_1 \; k_2 \; \cdots \; k_m} = \frac{n!}{k_1! \, k_2! \cdots k_m!}$$

where $k_1 + k_2 + \cdots + k_m = n$.

## Connection to Permutations with Repetition

As derived in the permutations with repetition section, the number of distinct arrangements of $n$ objects where there are $k_i$ identical objects of type $i$ is exactly the multinomial coefficient:

$$\frac{n!}{k_1! \, k_2! \cdots k_m!}$$

For example, the number of distinct words from BBOOO:

$$\binom{5}{2 \; 3} = \frac{5!}{2! \cdot 3!} = 10$$

## Multinomial Expansion

The multinomial coefficient appears as the coefficient in the **multinomial expansion**:

$$(x_1 + x_2 + \cdots + x_m)^n = \sum_{k_1 + k_2 + \cdots + k_m = n} \binom{n}{k_1 \; k_2 \; \cdots \; k_m} x_1^{k_1} x_2^{k_2} \cdots x_m^{k_m}$$

where the sum ranges over all non-negative integer solutions to $k_1 + k_2 + \cdots + k_m = n$.

Each term $\binom{n}{k_1 \cdots k_m} x_1^{k_1} \cdots x_m^{k_m}$ counts the number of ways to assign each of the $n$ factors $(x_1 + \cdots + x_m)$ to one of the $x_i$'s, such that $x_i$ is chosen $k_i$ times.

## Special Case: Binomial Coefficient

When $m = 2$, the multinomial coefficient reduces to the binomial coefficient:

$$\binom{n}{k_1 \; k_2} = \frac{n!}{k_1! \, k_2!} = \binom{n}{k_1}$$

since $k_2 = n - k_1$.

## Python Implementation

```python
from math import factorial

def multinomial(n, groups):
    """
    Compute the multinomial coefficient n! / (k1! * k2! * ... * km!).
    
    Parameters
    ----------
    n : int
        Total number of objects.
    groups : list of int
        Sizes of each group (must sum to n).
    
    Returns
    -------
    int
        The multinomial coefficient.
    """
    assert sum(groups) == n, "Group sizes must sum to n"
    result = factorial(n)
    for k in groups:
        result //= factorial(k)
    return result

# Example: Words from BBOOO
print(f"Multinomial(5; 2, 3) = {multinomial(5, [2, 3])}")
# Output: 10

# Example: Divide 12 people into groups of 4, 4, 4
print(f"Multinomial(12; 4, 4, 4) = {multinomial(12, [4, 4, 4])}")
# Output: 34650

# Verify multinomial expansion: (x + y + z)^3
# All terms with their coefficients
n = 3
m = 3
print(f"\nMultinomial expansion of (x1 + x2 + x3)^{n}:")
for k1 in range(n + 1):
    for k2 in range(n - k1 + 1):
        k3 = n - k1 - k2
        coeff = multinomial(n, [k1, k2, k3])
        if coeff > 0:
            print(f"  ({k1},{k2},{k3}): coefficient = {coeff}")
```

## Key Takeaway

The multinomial coefficient $\frac{n!}{k_1! \cdots k_m!}$ unifies two perspectives: it counts distinct arrangements of objects with repeated types, and it gives the coefficients in the multinomial expansion. The binomial coefficient is the special case $m = 2$.
