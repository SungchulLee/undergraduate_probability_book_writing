# Pascal's Rule and Vandermonde's Identity

These two fundamental identities for binomial coefficients both arise from counting the same quantity in two different ways — a technique that pervades combinatorics.

## Definition

**Pascal's Rule.** For $1 \le k \le n-1$:

$$
\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
$$

**Vandermonde's Identity.** For non-negative integers $m, n, k$:

$$
\binom{m+n}{k} = \sum_{\ell=0}^{k} \binom{m}{\ell}\binom{n}{k-\ell}
$$

## Explanation

### Pascal's Rule — Condition on One Element

Fix one person $X$ among $n$. Every $k$-person committee either includes $X$ or not:

- **$X$ included:** choose the remaining $k-1$ from $n-1$ people: $\binom{n-1}{k-1}$
- **$X$ excluded:** choose all $k$ from $n-1$ people: $\binom{n-1}{k}$

These cases are disjoint and exhaustive, so $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$.

Pascal's rule generates **Pascal's triangle**: each entry is the sum of the two entries directly above it. Row $n$ gives the coefficients of $(x+y)^n$.

### Vandermonde's Identity — Partition by Group Composition

Choose a committee of $k$ from $m$ men and $n$ women.

**Direct count:** $\binom{m+n}{k}$.

**By gender breakdown:** Choose $\ell$ men and $k-\ell$ women, then sum over $\ell$:

$$
\sum_{\ell=0}^{k} \binom{m}{\ell}\binom{n}{k-\ell}
$$

Both expressions count the same committees, establishing the identity.

**Special case ($m = n = k$):**

$$
\binom{2n}{n} = \sum_{\ell=0}^{n}\binom{n}{\ell}^2
$$

The sum of squares of the entries in row $n$ of Pascal's triangle equals the central binomial coefficient.

## Examples

**Example 1 (Pascal).** $\binom{7}{3} = \binom{6}{2} + \binom{6}{3} = 15 + 20 = 35$. ✓

---

**Example 2 (Vandermonde).** Verify $\binom{10}{5} = \sum_{\ell=0}^{4}\binom{4}{\ell}\binom{6}{5-\ell}$:

$$
1\cdot 6 + 4\cdot 15 + 6\cdot 20 + 4\cdot 15 + 1\cdot 6 = 6 + 60 + 120 + 60 + 6 = 252 = \binom{10}{5}
$$

---

**Example 3 (Committee selection).** From 5 men and 7 women, form a committee of 4. The breakdown by gender:

| Men $\ell$ | Women $4-\ell$ | Ways |
|:---:|:---:|:---:|
| 0 | 4 | $\binom{5}{0}\binom{7}{4} = 35$ |
| 1 | 3 | $\binom{5}{1}\binom{7}{3} = 175$ |
| 2 | 2 | $\binom{5}{2}\binom{7}{2} = 210$ |
| 3 | 1 | $\binom{5}{3}\binom{7}{1} = 70$ |
| 4 | 0 | $\binom{5}{4}\binom{7}{0} = 5$ |

Total: $495 = \binom{12}{4}$. ✓

```python
from math import comb

# Pascal's rule verification
for n in range(2, 10):
    for k in range(1, n):
        assert comb(n, k) == comb(n - 1, k - 1) + comb(n - 1, k)
print("Pascal's rule verified for n=2..9")

# Vandermonde verification (Example 2)
lhs = comb(10, 5)
rhs = sum(comb(4, l) * comb(6, 5 - l) for l in range(5))
print(f"C(10,5) = {lhs}, sum = {rhs}, match: {lhs == rhs}")

# Example 3 breakdown
m, n, k = 5, 7, 4
total = 0
for l in range(k + 1):
    ways = comb(m, l) * comb(n, k - l)
    if ways > 0:
        total += ways
        print(f"  {l} men, {k-l} women: {comb(m,l)}*{comb(n,k-l)} = {ways}")
print(f"Total: {total} = C({m+n},{k}) = {comb(m+n, k)}")
```
