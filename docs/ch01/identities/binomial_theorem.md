# Binomial Theorem

The binomial theorem expands $(x+y)^n$ as a weighted sum of monomials, with binomial coefficients as weights. It is the bridge between algebra and combinatorics.

## Definition

For any non-negative integer $n$:

$$
(x + y)^n = \sum_{k=0}^{n} \binom{n}{k}\, x^k\, y^{n-k}
$$

## Explanation

### Combinatorial Proof

Expand $(x+y)^n = (x+y)(x+y)\cdots(x+y)$ by choosing $x$ or $y$ from each of the $n$ factors. The monomial $x^k y^{n-k}$ appears once for each way to choose $x$ from exactly $k$ factors, and there are $\binom{n}{k}$ such choices.

### Key Special Cases

**$x = y = 1$:** The total number of subsets of an $n$-element set:

$$
2^n = \sum_{k=0}^{n} \binom{n}{k}
$$

**$x = 1,\; y = -1$:** Even-sized and odd-sized subsets are equally numerous:

$$
0 = \sum_{k=0}^{n} (-1)^k \binom{n}{k}
$$

**$x = 1,\; y = 1$ weighted by $k$:** Differentiating $(1+y)^n$ with respect to $y$ and setting $y=1$:

$$
n \cdot 2^{n-1} = \sum_{k=0}^{n} k\binom{n}{k}
$$

### Multinomial Generalization

For $m$ terms:

$$
(x_1 + \cdots + x_m)^n = \sum_{k_1+\cdots+k_m=n} \frac{n!}{k_1!\cdots k_m!}\, x_1^{k_1}\cdots x_m^{k_m}
$$

## Examples

**Example 1.** Expand $(x+y)^4$:

$$
(x+y)^4 = x^4 + 4x^3y + 6x^2y^2 + 4xy^3 + y^4
$$

Coefficients: $1, 4, 6, 4, 1$ (row 4 of Pascal's triangle).

---

**Example 2.** Compute $\sum_{k=0}^{6}\binom{6}{k}3^k$ without listing all terms.

By the binomial theorem with $x=3, y=1$: $(3+1)^6 = 4^6 = 4096$.

```python
from math import comb

# Example 1: Coefficients of (x+y)^4
coeffs = [comb(4, k) for k in range(5)]
print(f"(x+y)^4 coefficients: {coeffs}")
# Output: (x+y)^4 coefficients: [1, 4, 6, 4, 1]

# Verify special cases for n=10
n = 10
assert sum(comb(n, k) for k in range(n + 1)) == 2**n
assert sum((-1)**k * comb(n, k) for k in range(n + 1)) == 0
assert sum(k * comb(n, k) for k in range(n + 1)) == n * 2**(n - 1)
print(f"All special-case identities verified for n={n}.")

# Example 2
print(f"Sum C(6,k)*3^k = {sum(comb(6,k)*3**k for k in range(7))}")
print(f"4^6 = {4**6}")
```
