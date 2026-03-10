# Pigeonhole Principle

The pigeonhole principle is the simplest existence argument in combinatorics: it guarantees that some container is "crowded" without specifying which one. Despite its simplicity, it yields surprisingly deep results.

## Definition

**Pigeonhole Principle.** If $n$ items are placed into $k$ containers and $n > k$, then at least one container holds more than one item.

Equivalently: if $f\colon A \to B$ with $|A| > |B|$, then $f$ is not injective.

**Generalized Pigeonhole Principle.** If $n$ items are placed into $k$ containers, then at least one container holds at least $\lceil n/k \rceil$ items.

*Proof.* If every container held at most $\lceil n/k \rceil - 1$ items, the total would be at most $k(\lceil n/k \rceil - 1) < n$, a contradiction. $\square$

## Explanation

The pigeonhole principle is purely existential — it tells you *that* a collision exists, not *where*. This makes it a powerful tool for impossibility proofs and non-constructive existence arguments. The typical proof strategy is:

1. **Identify the items** (pigeons) and **containers** (holes).
2. Show that there are **more items than containers**.
3. Conclude that some container must hold at least two items (or $\lceil n/k \rceil$ in the generalized version).

The creative part is always step 1: choosing the right items and containers. The examples below illustrate this.

## Examples

**Example 1 (Handshake lemma).** At any party with $n \ge 2$ people, at least two people have shaken the same number of hands.

*Proof.* Each person shakes between 0 and $n-1$ hands — that is $n$ possible values. But 0 and $n-1$ cannot both occur (if someone shook everyone's hand, no one shook zero hands). So there are at most $n-1$ possible values for $n$ people. By pigeonhole, two share the same count. $\square$

---

**Example 2 (Consecutive integers).** Among any $n+1$ integers from $\{1, 2, \ldots, 2n\}$, two are consecutive.

*Proof.* Partition $\{1, \ldots, 2n\}$ into $n$ pairs: $\{1,2\},\{3,4\},\ldots,\{2n-1,2n\}$. By pigeonhole, two of the $n+1$ chosen integers share a pair. $\square$

---

**Example 3 (Divisibility).** Among any $n+1$ integers, two have the same remainder mod $n$.

*Proof.* There are $n$ remainder classes $\{0, 1, \ldots, n-1\}$. By pigeonhole, two of the $n+1$ integers share a class, so their difference is divisible by $n$. $\square$

---

**Example 4 (Erdos-Szekeres).** Every sequence of $n^2 + 1$ distinct reals contains a monotone subsequence of length $n + 1$.

*Proof.* Assign to each element $a_i$ a pair $(d_i, e_i)$ where $d_i$ is the length of the longest increasing subsequence ending at $a_i$ and $e_i$ the longest decreasing. If both $d_i \le n$ and $e_i \le n$ for all $i$, there are at most $n^2$ distinct pairs — but we have $n^2 + 1$ elements, contradicting pigeonhole. $\square$

```python
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Panel 1: Probability of shared birth month
np.random.seed(42)
n_trials = 10_000
prob_shared = []
for n in range(2, 50):
    count = sum(
        1 for _ in range(n_trials)
        if len(np.unique(np.random.randint(0, 12, n))) < n
    )
    prob_shared.append(count / n_trials)

axes[0].plot(range(2, 50), prob_shared, 'bo-', markersize=3)
axes[0].axhline(1.0, color='red', ls='--', alpha=0.5, label='Guaranteed at n=13')
axes[0].axvline(13, color='red', ls='--', alpha=0.5)
axes[0].set_title('P(shared birth month) vs n people (12 months)')
axes[0].set_xlabel('Number of people')
axes[0].set_ylabel('Probability')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Panel 2: Max items per bin (generalized pigeonhole)
k_bins = 10
for n_items in [10, 20, 50, 100]:
    max_counts = [
        np.unique(np.random.randint(0, k_bins, n_items), return_counts=True)[1].max()
        for _ in range(5000)
    ]
    lower_bound = int(np.ceil(n_items / k_bins))
    axes[1].hist(max_counts, bins=range(0, max(max_counts) + 2),
                 density=True, alpha=0.4,
                 label=f'n={n_items}, ⌈n/k⌉={lower_bound}')

axes[1].set_title(f'Max items in any bin (k={k_bins} bins)')
axes[1].set_xlabel('Max count')
axes[1].set_ylabel('Frequency')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('pigeonhole.png', dpi=150, bbox_inches='tight')
plt.show()
```
