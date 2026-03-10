# Birthday Problem

The birthday problem asks how many people must be in a room before a shared birthday becomes likely. The answer — just 23 for a 50% chance — is famously counterintuitive and illustrates the power of complement counting.

## Definition

Given $n$ people with birthdays uniformly distributed over $d = 365$ days, the probability that at least two share a birthday is

$$
P(\text{match}) = 1 - \prod_{k=0}^{n-1}\left(1 - \frac{k}{d}\right)
$$

## Explanation

### Complement Counting

Counting "at least one match" directly is hard. The complement — "all $n$ birthdays are distinct" — is easy:

$$
P(\text{all different}) = \frac{365 \times 364 \times \cdots \times (365-n+1)}{365^n} = \prod_{k=0}^{n-1}\left(1 - \frac{k}{365}\right)
$$

### Why 23 Is Enough

The surprise comes from the quadratic growth of pairs: $n$ people produce $\binom{n}{2} = n(n-1)/2$ pairs, each a potential match. With 23 people, there are $\binom{23}{2} = 253$ pairs.

**Approximation.** Using $1 - x \approx e^{-x}$ for small $x$:

$$
P(\text{all different}) \approx e^{-n(n-1)/(2 \cdot 365)}
$$

Setting this to $1/2$: $n(n-1) \approx 730\ln 2 \approx 506$, giving $n \approx 23$.

### Generalization

With $d$ possible birthdays, the 50% threshold is $n \approx 1.2\sqrt{d}$.

!!! example "Application: Birthday Attack"
    A hash function with $d = 2^b$ outputs expects a collision after $\sim 2^{b/2}$ random inputs. A 128-bit hash provides only 64 bits of collision resistance.

## Examples

**Key values:**

| $n$ | $P(\text{match})$ | Pairs $\binom{n}{2}$ |
|:---:|:---:|:---:|
| 10 | 0.1169 | 45 |
| 20 | 0.4114 | 190 |
| **23** | **0.5073** | 253 |
| 30 | 0.7063 | 435 |
| 50 | 0.9704 | 1225 |
| 57 | 0.9901 | 1596 |

```python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def birthday_probability(n, days=365):
    """Exact probability of at least one shared birthday."""
    if n > days:
        return 1.0
    p = 1.0
    for k in range(n):
        p *= (days - k) / days
    return 1 - p

# Table
print(f"{'n':>4} | {'P(match)':>10} | {'pairs':>6}")
print("-" * 28)
for n in [10, 20, 23, 30, 50, 57, 70]:
    print(f"{n:4d} | {birthday_probability(n):10.4f} | {n*(n-1)//2:6d}")

# Monte Carlo verification
np.random.seed(42)
for n in [23, 50]:
    matches = sum(
        len(set(np.random.randint(0, 365, n))) < n
        for _ in range(100_000)
    )
    print(f"\nn={n}: exact={birthday_probability(n):.4f}, sim={matches/100_000:.4f}")

# Plot
ns = range(1, 81)
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(list(ns), [birthday_probability(n) for n in ns], 'b-', lw=2)
ax.axhline(0.5, color='r', ls='--', alpha=0.7, label='P = 0.5')
ax.axvline(23, color='g', ls='--', alpha=0.7, label='n = 23')
ax.set_xlabel('Number of people')
ax.set_ylabel('P(at least one shared birthday)')
ax.set_title('Birthday Problem')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('birthday_problem.png', dpi=150, bbox_inches='tight')
plt.close()
```
