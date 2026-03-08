# Birthday Problem

## The Problem

In a room of $n$ people, what is the probability that at least two people share the same birthday?

**Assumptions:**

- 365 equally likely birthdays (ignore leap years)
- Birthdays are independent across people

## Solution via the Complement

It is much easier to compute the probability of the complement — that **all $n$ birthdays are distinct**.

### Sample Space

Each of the $n$ people can have any of 365 birthdays:

$$
|\Omega| = 365^n
$$

### Counting A^c (All Different Birthdays)

- Person 1: 365 choices
- Person 2: 364 choices (must differ from person 1)
- Person 3: 363 choices
- $\vdots$
- Person $n$: $365 - (n-1)$ choices

$$
|A^c| = 365 \times 364 \times 363 \times \cdots \times (365 - n + 1) = \frac{365!}{(365-n)!}
$$

### Probability of a Match

$$
P(\text{at least one match}) = 1 - P(\text{all different}) = 1 - \frac{365 \times 364 \times \cdots \times (365 - n + 1)}{365^n}
$$

$$
= 1 - \prod_{k=0}^{n-1}\left(1 - \frac{k}{365}\right)
$$

## Key Results

| $n$ | $P(\text{at least one match})$ |
|-----|-------------------------------|
| 10 | 0.1169 |
| 20 | 0.4114 |
| **23** | **0.5073** |
| 30 | 0.7063 |
| 50 | 0.9704 |
| 57 | 0.9901 |
| 70 | 0.9992 |

!!! note "The Surprise"
    With only **23 people**, there is already a greater than 50% chance of a shared birthday. With 57 people, the probability exceeds 99%. This is often called the **birthday paradox** because the threshold is surprisingly low.

## Why Is the Threshold So Low?

The key insight is that we are not asking whether a **specific** person shares a birthday with someone else. We are asking whether **any pair** among all $n$ people shares a birthday. The number of pairs grows quadratically:

$$
\binom{n}{2} = \frac{n(n-1)}{2}
$$

With 23 people, there are $\binom{23}{2} = 253$ pairs — each a potential match.

## Approximation via exp(-x) approx 1 - x

For small $x$, $1 - x \approx e^{-x}$. Therefore:

$$
P(\text{all different}) = \prod_{k=0}^{n-1}\left(1 - \frac{k}{365}\right) \approx \prod_{k=0}^{n-1} e^{-k/365} = e^{-n(n-1)/(2 \cdot 365)}
$$

Setting $P(\text{match}) = 0.5$:

$$
e^{-n(n-1)/730} = 0.5 \implies n(n-1) \approx 730 \ln 2 \approx 506 \implies n \approx 23
$$

## Python Example

```python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def birthday_probability(n, days=365):
    """Exact probability of at least one shared birthday among n people."""
    if n > days:
        return 1.0
    p_all_different = 1.0
    for k in range(n):
        p_all_different *= (days - k) / days
    return 1 - p_all_different

# Compute probabilities
ns = range(1, 81)
probs = [birthday_probability(n) for n in ns]

# Find threshold for P > 0.5
threshold = next(n for n in ns if birthday_probability(n) > 0.5)
print(f"Smallest n with P > 0.5: n = {threshold}")
print(f"P({threshold}) = {birthday_probability(threshold):.4f}")

# Print table
print(f"\n{'n':>4} | {'P(match)':>10} | {'# pairs':>8}")
print("-" * 30)
for n in [10, 20, 23, 30, 40, 50, 57, 70]:
    p = birthday_probability(n)
    pairs = n * (n - 1) // 2
    print(f"{n:4d} | {p:10.4f} | {pairs:8d}")

# Monte Carlo simulation
def birthday_simulation(n, n_sim=100_000):
    """Simulate the birthday problem."""
    np.random.seed(42)
    matches = 0
    for _ in range(n_sim):
        birthdays = np.random.randint(0, 365, size=n)
        if len(set(birthdays)) < n:
            matches += 1
    return matches / n_sim

print(f"\nSimulation verification (100,000 trials):")
for n in [23, 50, 70]:
    exact = birthday_probability(n)
    sim = birthday_simulation(n)
    print(f"  n={n}: exact={exact:.4f}, simulated={sim:.4f}")

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(ns, probs, 'b-', linewidth=2)
ax.axhline(y=0.5, color='r', linestyle='--', alpha=0.7, label='P = 0.5')
ax.axvline(x=23, color='g', linestyle='--', alpha=0.7, label='n = 23')
ax.set_xlabel('Number of people (n)', fontsize=12)
ax.set_ylabel('P(at least one shared birthday)', fontsize=12)
ax.set_title('Birthday Problem', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_xlim(1, 80)
ax.set_ylim(0, 1.05)
plt.tight_layout()
plt.savefig('/home/claude/ch02/classical/birthday_problem.png', dpi=150)
plt.close()
print("\nPlot saved.")
```

**Output:**
```
Smallest n with P > 0.5: n = 23
P(23) = 0.5073

   n |   P(match) |  # pairs
------------------------------
  10 |     0.1169 |       45
  20 |     0.4114 |      190
  23 |     0.5073 |      253
  30 |     0.7063 |      435
  40 |     0.8912 |      780
  50 |     0.9704 |     1225
  57 |     0.9901 |     1596
  70 |     0.9992 |     2415

Simulation verification (100,000 trials):
  n=23: exact=0.5073, simulated=0.5063
  n=50: exact=0.9704, simulated=0.9700
  n=70: exact=0.9992, simulated=0.9992
```

## Generalization

The birthday problem generalizes naturally. With $d$ possible birthdays (instead of 365), the probability of a match among $n$ people is:

$$
P(\text{match}) \approx 1 - e^{-n(n-1)/(2d)}
$$

The 50% threshold occurs at approximately $n \approx 1.2\sqrt{d}$.

!!! example "Application in Cryptography"
    The birthday problem underlies the **birthday attack** in cryptography. For a hash function with $d = 2^b$ possible outputs ($b$-bit hash), a collision is expected after roughly $2^{b/2}$ random inputs. This is why a 128-bit hash provides only 64 bits of collision resistance.
