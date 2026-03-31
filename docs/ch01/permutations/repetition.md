# Permutations with Repetition

## Overview

When some objects are **identical** (repeated), the number of distinct arrangements is less than $n!$ because swapping identical objects does not produce a new arrangement. The **many-to-one** principle provides an elegant way to derive the correct count.

## The Many-to-One Principle

The many-to-one principle is a powerful counting technique based on establishing a mapping between two sets:

**One-to-one:** If $f: A \to B$ is a bijection, then $|B| = |A|$.

**Many-to-one:** If $f: A \to B$ is a $k$-to-1 surjection (every element of $B$ has exactly $k$ preimages), then:

$$|A| : |B| = k : 1 \quad \Rightarrow \quad |B| = \frac{|A|}{k}$$

**One-to-many:** If every element of $A$ maps to $k$ elements of $B$, then $|A| = k|B|$.

## Example — Words Made from BOB

**Step 1: Attach indices.** Treat the two B's as distinct: $B_1 O B_2$.

The number of arrangements of $B_1 O B_2$ (all distinct) is $3! = 6$.

**Step 2: Remove indices.** List all arrangements and observe what happens:

| With indices | Without indices |
|:---:|:---:|
| $B_1 B_2 O$ | $BBO$ |
| $B_1 O B_2$ | $BOB$ |
| $B_2 B_1 O$ | $BBO$ |
| $B_2 O B_1$ | $BOB$ |
| $O B_1 B_2$ | $OBB$ |
| $O B_2 B_1$ | $OBB$ |

**Step 3: Apply many-to-one.** Each distinct word (without indices) corresponds to exactly $2! = 2$ indexed arrangements (since the two B's can be swapped). This is a **2-to-1** mapping.

$$\text{Number of words from BOB} = \frac{3!}{2!} = \frac{6}{2} = 3$$

The three distinct words are: $BBO$, $BOB$, $OBB$.

## Example — Words Made from BBOOO

**Step 1: Attach indices.** Treat letters as distinct: $B_1 B_2 O_1 O_2 O_3$.

Number of arrangements: $5! = 120$.

**Step 2: Remove indices.** For each distinct word, the two B's can be permuted among themselves in $2!$ ways, and the three O's can be permuted among themselves in $3!$ ways.

For example, the word $BBOOO$ corresponds to $2! \times 3! = 12$ indexed arrangements:

$B_1 B_2 O_1 O_2 O_3$, $B_1 B_2 O_1 O_3 O_2$, $B_1 B_2 O_2 O_1 O_3$, $B_1 B_2 O_2 O_3 O_1$, $B_1 B_2 O_3 O_1 O_2$, $B_1 B_2 O_3 O_2 O_1$, $B_2 B_1 O_1 O_2 O_3$, $B_2 B_1 O_1 O_3 O_2$, $B_2 B_1 O_2 O_1 O_3$, $B_2 B_1 O_2 O_3 O_1$, $B_2 B_1 O_3 O_1 O_2$, $B_2 B_1 O_3 O_2 O_1$

**Step 3: Apply many-to-one.** This is a $(2! \cdot 3!)$-to-1 mapping.

$$\text{Number of words from BBOOO} = \frac{5!}{2! \cdot 3!} = \frac{120}{2 \cdot 6} = 10$$

## General Formula — Multinomial Coefficient

Given $n$ objects where there are $n_1$ identical objects of type 1, $n_2$ of type 2, ..., $n_m$ of type $m$ (with $n_1 + n_2 + \cdots + n_m = n$), the number of distinct arrangements is the **multinomial coefficient**:

$$\binom{n}{n_1 \; n_2 \; \cdots \; n_m} = \frac{n!}{n_1! \cdot n_2! \cdots n_m!}$$

This follows from the many-to-one principle: start with $n!$ arrangements of all-distinct objects, then divide by the product of factorials to account for indistinguishable swaps within each group.

## Python Implementation

```python
from math import factorial
from itertools import permutations

def permutations_with_repetition(word):
    """
    Count distinct permutations of a word with repeated letters.
    Uses the multinomial coefficient: n! / (n1! * n2! * ... * nm!)
    
    Parameters
    ----------
    word : str
        The word whose letters are to be permuted.
    
    Returns
    -------
    int
        Number of distinct arrangements.
    """
    n = len(word)
    from collections import Counter
    counts = Counter(word)
    denominator = 1
    for c in counts.values():
        denominator *= factorial(c)
    return factorial(n) // denominator

# Example: BOB
word = "BOB"
result = permutations_with_repetition(word)
print(f"Distinct permutations of '{word}': {result}")
# Output: Distinct permutations of 'BOB': 3

# Verification by enumeration
distinct = set(permutations(word))
print(f"Verification: {len(distinct)}")
print(f"Words: {sorted([''.join(p) for p in distinct])}")
# Output: Words: ['BBO', 'BOB', 'OBB']

# Example: BBOOO
word = "BBOOO"
result = permutations_with_repetition(word)
print(f"\nDistinct permutations of '{word}': {result}")
# Output: Distinct permutations of 'BBOOO': 10

distinct = set(permutations(word))
print(f"Verification: {len(distinct)}")
print(f"Words: {sorted([''.join(p) for p in distinct])}")
```

## Key Takeaway

The many-to-one principle converts a difficult counting problem into an easy one: first count as if all objects were distinct ($n!$), then divide by the number of "equivalent" arrangements caused by identical objects. This is the foundation of the multinomial coefficient.
