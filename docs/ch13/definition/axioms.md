# Definition and Axioms

The Poisson process is a counting process satisfying three axioms: it starts at zero, has independent increments, and counts events at a constant rate.

## Definition

A counting process $\{N(t) : t \ge 0\}$ is a **Poisson process with rate $\lambda > 0$** if:

1. $N(0) = 0$
2. $N(t)$ has **independent increments**: counts in disjoint intervals are independent
3. For any interval of length $h$: $N(t+h) - N(t) \sim \text{Pois}(\lambda h)$

Equivalently, the infinitesimal conditions:

$$
P(N(h) = 1) = \lambda h + o(h), \qquad P(N(h) \ge 2) = o(h)
$$

## Explanation

### What the Axioms Mean

- **Axiom 1:** No events at time 0
- **Axiom 2:** Knowing how many events occurred in $[0, 1]$ tells you nothing about $[2, 3]$
- **Axiom 3:** The count in any interval depends only on the interval's length, not its position (stationarity), and follows a Poisson distribution

### Interarrival Times

Let $T_i$ be the time between the $(i-1)$-th and $i$-th event. The axioms imply:

$$
T_1, T_2, T_3, \ldots \stackrel{\text{iid}}{\sim} \text{Exp}(\lambda)
$$

This is the memoryless property at work: the process "resets" after each event.

### Arrival Times

The $n$-th arrival time $S_n = T_1 + \cdots + T_n \sim \text{Gamma}(n, \lambda)$.

## Examples

**Example.** Customers arrive at rate $\lambda = 5$ per hour. In 2 hours, the count $N(2) \sim \text{Pois}(10)$.

```python
import numpy as np

np.random.seed(42)
n_sim = 100_000
lam = 5

# Simulate via interarrival times
counts = []
for _ in range(n_sim):
    t = 0
    count = 0
    while True:
        t += np.random.exponential(1/lam)
        if t > 2:
            break
        count += 1
    counts.append(count)

counts = np.array(counts)
print(f"E[N(2)] = {counts.mean():.3f}  (theory: 10)")
print(f"Var[N(2)] = {counts.var():.3f}  (theory: 10)")
```
