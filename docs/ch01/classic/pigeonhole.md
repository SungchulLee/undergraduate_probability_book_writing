# Pigeonhole Principle


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Statement

!!! info "Pigeonhole Principle"
    If $n$ items are placed into $k$ containers and $n > k$, then **at least one container** holds more than one item.

**Formally:** If $f: A \to B$ is a function with $|A| > |B|$, then $f$ is not injective — there exist $a_1 \neq a_2$ in $A$ with $f(a_1) = f(a_2)$.

## Generalized Pigeonhole Principle

!!! info "Generalized Form"
    If $n$ items are placed into $k$ containers, then at least one container holds at least $\lceil n/k \rceil$ items.

**Proof.** If every container held at most $\lceil n/k \rceil - 1$ items, the total would be at most $k(\lceil n/k \rceil - 1) < k \cdot n/k = n$, a contradiction. $\square$

## Classic Applications

### Handshake Lemma

**Claim:** At any party with $n \geq 2$ people, at least two people have shaken the same number of hands.

**Proof.** Each person can shake between 0 and $n - 1$ hands, giving $n$ possible values. But 0 and $n - 1$ cannot both occur (if someone shook everyone's hand, no one shook zero hands). So there are at most $n - 1$ possible values for $n$ people. By the pigeonhole principle, at least two people share the same count. $\square$

### Subset Sum

**Claim:** Among any $n + 1$ integers from $\{1, 2, \ldots, 2n\}$, there exist two that are consecutive.

**Proof.** Partition $\{1, \ldots, 2n\}$ into $n$ pairs: $\{1,2\}, \{3,4\}, \ldots, \{2n-1, 2n\}$. By the pigeonhole principle, two of the $n+1$ chosen integers must lie in the same pair. $\square$

### Divisibility

**Claim:** Among any $n+1$ integers, there exist two whose difference is divisible by $n$.

**Proof.** There are $n$ possible remainders modulo $n$: $0, 1, \ldots, n-1$. With $n+1$ integers and $n$ containers (remainder classes), two must share the same remainder. Their difference is divisible by $n$. $\square$

### Monotone Subsequences (Erdős–Szekeres)

**Claim:** Every sequence of $n^2 + 1$ distinct real numbers contains a monotone subsequence of length $n + 1$.

**Proof sketch.** Assign to each element $a_i$ a pair $(d_i, e_i)$ where $d_i$ is the length of the longest increasing subsequence ending at $a_i$ and $e_i$ is the longest decreasing. If all $d_i \leq n$ and all $e_i \leq n$, there are at most $n^2$ distinct pairs for $n^2 + 1$ elements, contradicting pigeonhole. $\square$

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# --- Panel 1: Birthday-like pigeonhole ---
np.random.seed(42)
n_people_range = range(2, 50)
n_trials = 10000

prob_shared = []
for n in n_people_range:
    count = 0
    for _ in range(n_trials):
        # Assign n people to 12 birth months (pigeonhole with k=12)
        months = np.random.randint(0, 12, n)
        if len(np.unique(months)) < n:
            count += 1
    prob_shared.append(count / n_trials)

axes[0].plot(list(n_people_range), prob_shared, 'bo-', markersize=3)
axes[0].axhline(1.0, color='red', ls='--', alpha=0.5,
                label='Guaranteed at n=13')
axes[0].axvline(13, color='red', ls='--', alpha=0.5)
axes[0].set_title('P(shared birth month) vs n people (12 months)')
axes[0].set_xlabel('Number of people')
axes[0].set_ylabel('Probability')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# --- Panel 2: Max items per bin ---
n_items_list = [10, 20, 50, 100]
k_bins = 10
n_trials = 5000

for n_items in n_items_list:
    max_counts = []
    for _ in range(n_trials):
        bins = np.random.randint(0, k_bins, n_items)
        _, counts = np.unique(bins, return_counts=True)
        max_counts.append(counts.max())
    lower_bound = int(np.ceil(n_items / k_bins))
    axes[1].hist(max_counts, bins=range(0, max(max_counts)+2),
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
