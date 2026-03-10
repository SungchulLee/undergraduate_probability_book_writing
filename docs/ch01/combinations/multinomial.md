# Multinomial Coefficients

The multinomial coefficient generalizes the binomial coefficient to partitioning $n$ objects into more than two groups. It arises in both counting arrangements with repeated types and in the multinomial expansion.

## Definition

The **multinomial coefficient** is

$$
\binom{n}{k_1 \; k_2 \; \cdots \; k_m} = \frac{n!}{k_1!\, k_2! \cdots k_m!}
$$

where $k_1 + k_2 + \cdots + k_m = n$ and each $k_i \ge 0$. It counts the number of ways to partition $n$ distinct objects into $m$ labeled groups of sizes $k_1, \ldots, k_m$.

When $m = 2$, this reduces to the binomial coefficient: $\binom{n}{k_1\;k_2} = \binom{n}{k_1}$.

## Explanation

### Two Equivalent Interpretations

**Interpretation 1 (Partitioning).** Divide $n$ distinct objects into $m$ *labeled* groups of prescribed sizes. Choose $k_1$ for group 1, then $k_2$ from the remaining for group 2, etc.:

$$
\binom{n}{k_1}\binom{n-k_1}{k_2}\cdots\binom{k_m}{k_m} = \frac{n!}{k_1!\,k_2!\cdots k_m!}
$$

**Interpretation 2 (Permutations with repetition).** Count distinct arrangements of $n$ objects where $k_i$ are identical copies of type $i$. Divide the $n!$ total orderings by $k_i!$ for each type to remove internal rearrangements.

!!! warning "Labeled vs unlabeled groups"
    The multinomial coefficient assumes groups are **distinguishable** (labeled). If the groups are identical (e.g., dividing 12 people into three unlabeled teams of 4), divide by the number of ways to permute identical groups: $\frac{1}{3!}\binom{12}{4\;4\;4}$.

### Multinomial Expansion

$$
(x_1 + x_2 + \cdots + x_m)^n = \sum_{k_1+\cdots+k_m=n} \binom{n}{k_1\;\cdots\;k_m}\, x_1^{k_1}\cdots x_m^{k_m}
$$

Each term counts the ways to assign each of the $n$ factors to one of the $x_i$'s, choosing $x_i$ exactly $k_i$ times.

## Examples

**Example 1 (Anagram counting).** Distinct arrangements of the letters in MISSISSIPPI ($n=11$: M=1, I=4, S=4, P=2):

$$
\binom{11}{1\;4\;4\;2} = \frac{11!}{1!\,4!\,4!\,2!} = 34{,}650
$$

---

**Example 2 (Labeled teams).** Divide 12 players into teams A (4), B (4), C (4):

$$
\binom{12}{4\;4\;4} = \frac{12!}{4!\,4!\,4!} = 34{,}650
$$

If the teams are **unlabeled** (no distinction between A, B, C): $34{,}650 / 3! = 5{,}775$.

---

**Example 3 (Expansion).** List all terms of $(x+y+z)^3$:

```python
from math import factorial

def multinomial(n, groups):
    """Compute n! / (k1! * k2! * ... * km!)."""
    result = factorial(n)
    for k in groups:
        result //= factorial(k)
    return result

# Example 1: MISSISSIPPI
print(f"MISSISSIPPI arrangements: {multinomial(11, [1, 4, 4, 2])}")
# Output: MISSISSIPPI arrangements: 34650

# Example 2: Labeled vs unlabeled teams
labeled = multinomial(12, [4, 4, 4])
unlabeled = labeled // factorial(3)
print(f"Labeled teams: {labeled}, Unlabeled teams: {unlabeled}")
# Output: Labeled teams: 34650, Unlabeled teams: 5775

# Example 3: All terms of (x + y + z)^3
print("\n(x + y + z)^3 expansion:")
for k1 in range(4):
    for k2 in range(4 - k1):
        k3 = 3 - k1 - k2
        coeff = multinomial(3, [k1, k2, k3])
        print(f"  {coeff} * x^{k1} y^{k2} z^{k3}")
```
