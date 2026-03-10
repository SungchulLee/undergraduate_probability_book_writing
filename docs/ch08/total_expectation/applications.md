# Applications of the Tower Property

The tower property and Eve's law turn recursive and random-sum problems into clean algebraic equations.

## Definition

Two fundamental tools:

**Tower property:** $E[X] = E\bigl[E[X \mid Y]\bigr]$

**Random sum formula.** If $T = \sum_{i=1}^N X_i$ where the $X_i$ are iid (mean $\mu$, variance $\sigma^2$) and independent of $N$:

$$
E[T] = \mu\,E[N], \qquad \text{Var}(T) = \sigma^2\,E[N] + \mu^2\,\text{Var}(N)
$$

**First-step analysis.** Condition on the first random event to obtain a self-referencing equation for the unknown quantity.

## Explanation

### Random Sums

For $T = \sum_{i=1}^N X_i$, conditioning on $N$ fixes the number of terms:

$$
E[T \mid N] = N\mu, \qquad \text{Var}(T \mid N) = N\sigma^2
$$

Applying the tower property: $E[T] = E[N\mu] = \mu\,E[N]$.

Applying Eve's law: $\text{Var}(T) = E[N\sigma^2] + \text{Var}(N\mu) = \sigma^2 E[N] + \mu^2 \text{Var}(N)$.

### First-Step Analysis

Many problems have a recursive structure: after one step, you either finish or face the same problem again. Conditioning on the first step creates an equation where $E[T]$ appears on both sides, which can be solved algebraically.

**Template:**

1. Let $X$ be the first random choice
2. Write $E[T \mid X = x]$ for each outcome $x$
3. Apply tower: $E[T] = \sum_x E[T \mid X = x]\,P(X = x)$
4. Solve for $E[T]$

## Examples

**Example 1 (Department store).** $N$ customers (mean 50, variance 100) each spend $X_i$ (mean \$8, SD \$4), independent of $N$.

$$
E[T] = 8 \times 50 = 400
$$

$$
\text{Var}(T) = 16 \times 50 + 64 \times 100 = 800 + 6400 = 7200
$$

**Example 2 (Trapped miner).** Three doors chosen uniformly: door 1 leads to safety in 3 hours; doors 2, 3 return the miner after 5 and 7 hours.

$$
E[T] = \tfrac{1}{3}\bigl(3 + (5 + E[T]) + (7 + E[T])\bigr) = 5 + \tfrac{2}{3}E[T]
$$

Solving: $E[T] = 15$. By Eve's law with a similar recursion: $\text{Var}(T) = 218$.

**Example 3 (Waiting for HT).** $W_{HT}$ decomposes as $X + Y$ where $X, Y$ are independent $\text{Geo}(1/2)$:

$$
E[W_{HT}] = 2 + 2 = 4, \qquad \text{Var}(W_{HT}) = 2 + 2 = 4
$$

**Example 4 (Waiting for HH).** After the first H (taking $\text{Geo}(1/2)$ flips), the next flip is H (done) or T (restart):

$$
E[W_{HH}] = \tfrac{1}{2}(3) + \tfrac{1}{2}(3 + E[W_{HH}]) \implies E[W_{HH}] = 6
$$

$$
\text{Var}(W_{HH}) = 9 + 2 + \tfrac{1}{2}\text{Var}(W_{HH}) \implies \text{Var}(W_{HH}) = 22
$$

Note: $E[W_{HH}] = 6 > 4 = E[W_{HT}]$ — overlapping patterns take longer.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

def simulate_pattern(pattern, n_sim):
    """Simulate waiting time for a 2-flip pattern."""
    results = []
    for _ in range(n_sim):
        flips = []
        count = 0
        while True:
            flip = np.random.randint(0, 2)
            flips.append(flip)
            count += 1
            if len(flips) >= 2 and flips[-2] == pattern[0] and flips[-1] == pattern[1]:
                break
        results.append(count)
    return np.array(results)

W_HT = simulate_pattern([1, 0], n_sim)
W_HH = simulate_pattern([1, 1], n_sim)

print("=== HT ===")
print(f"E[W_HT] = {W_HT.mean():.3f}  (theory: 4)")
print(f"Var[W_HT] = {W_HT.var():.3f}  (theory: 4)")

print("\n=== HH ===")
print(f"E[W_HH] = {W_HH.mean():.3f}  (theory: 6)")
print(f"Var[W_HH] = {W_HH.var():.3f}  (theory: 22)")

# Trapped miner
miner_times = []
for _ in range(n_sim):
    t = 0
    while True:
        door = np.random.randint(1, 4)
        if door == 1:
            t += 3; break
        elif door == 2:
            t += 5
        else:
            t += 7
    miner_times.append(t)
miner_times = np.array(miner_times)

print("\n=== Trapped Miner ===")
print(f"E[T] = {miner_times.mean():.2f}  (theory: 15)")
print(f"Var[T] = {miner_times.var():.1f}  (theory: 218)")

# Department store
store_totals = []
for _ in range(n_sim):
    N = max(int(np.random.normal(50, 10)), 0)
    spending = np.random.normal(8, 4, N)
    store_totals.append(spending.sum())
store_totals = np.array(store_totals)

print("\n=== Department Store ===")
print(f"E[T] = {store_totals.mean():.1f}  (theory: 400)")
print(f"Var[T] = {store_totals.var():.0f}  (theory: 7200)")
```
