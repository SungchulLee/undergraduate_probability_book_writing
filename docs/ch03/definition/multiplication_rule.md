# Multiplication Rule for Probabilities

## Chain Rule (Product Rule)

The **chain rule** (also called the **multiplication rule**) allows us to compute the probability of the intersection of events by successive conditioning.

### Two Events

$$
P(AB) = P(A)\,P(B \mid A)
$$

This follows directly from rearranging the definition of conditional probability.

### Three Events

$$
P(ABC) = P(A)\,P(B \mid A)\,P(C \mid AB)
$$

### Four Events

$$
P(ABCD) = P(A)\,P(B \mid A)\,P(C \mid AB)\,P(D \mid ABC)
$$

### General Form

For events $A_1, A_2, \ldots, A_n$:

$$
P(A_1 A_2 \cdots A_n) = P(A_1)\,P(A_2 \mid A_1)\,P(A_3 \mid A_1 A_2) \cdots P(A_n \mid A_1 A_2 \cdots A_{n-1})
$$

Each successive factor conditions on all preceding events.

## Example — Birthday Problem

Let $p(n)$ be the probability that there is at least one birthday match among $n$ people. Find the minimum $n$ such that $p(n) > 0.5$.

### Setup

Define:

$$
B_k = \{\text{the first } k \text{ people all have different birthdays}\}
$$

The complementary probability (no match) can be computed via the chain rule:

$$
1 - p(n) = P(B_1 B_2 B_3 \cdots B_n)
$$

$$
= P(B_1)\,P(B_2 \mid B_1)\,P(B_3 \mid B_1 B_2) \cdots P(B_n \mid B_1 B_2 \cdots B_{n-1})
$$

### Evaluating Each Factor

Given that the first $k-1$ people have distinct birthdays, the $k$-th person must avoid $k-1$ days out of 365:

$$
P(B_k \mid B_1 B_2 \cdots B_{k-1}) = \frac{365 - (k-1)}{365}
$$

Therefore:

$$
1 - p(n) = 1 \cdot \frac{364}{365} \cdot \frac{363}{365} \cdots \frac{365 - (n-1)}{365}
$$

### Approximate Computation

Using the approximation $1 - x \approx e^{-x}$ for small $x$:

$$
1 - p(n) \approx e^{-1/365} \cdot e^{-2/365} \cdots e^{-(n-1)/365} = e^{-n(n-1)/(2 \times 365)}
$$

Setting $e^{-n(n-1)/(2 \times 365)} = 0.5$ and solving:

$$
n(n-1) = 2 \times 365 \times \ln 2 \approx 506 \implies n \approx 23
$$

### Exact Computation

| $p(22)$ | $p(23)$ | $p(24)$ |
|---------|---------|---------|
| 0.4757 | 0.5073 | 0.5383 |

The minimum number of people for a greater than 50% chance of a birthday match is **$n = 23$**.

### Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

# q(n) = P(no birthday match among n people)
q = np.ones(365)
for n in range(1, 365):
    q[n] = q[n-1] * (1 - n / 365)

# p(n) = P(at least one birthday match among n people)
p = 1 - q

# Find the least n with p(n) >= 0.5
min_people = np.argmax(p >= 0.5) + 1  # +1 for 1-indexed

print(f"Minimum people for >50% match probability: {min_people}")
print(f"p(22) = {p[21]:.4f}, p(23) = {p[22]:.4f}, p(24) = {p[23]:.4f}")

# Plot
plt.figure(figsize=(8, 5))
plt.plot(range(1, 366), p, 'b-')
plt.axhline(y=0.5, color='b', linestyle='--', alpha=0.5)
plt.axvline(x=min_people, color='r', linestyle='--', alpha=0.5)
plt.xlabel('Number of People')
plt.ylabel('Probability of Match')
plt.title('Birthday Problem')
plt.grid(True, alpha=0.3)
plt.xlim([0, 366])
plt.ylim([-0.1, 1.1])
plt.tight_layout()
plt.savefig('birthday_problem.png', dpi=150, bbox_inches='tight')
plt.show()
```
