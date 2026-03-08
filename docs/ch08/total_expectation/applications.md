# Applications of the Tower Property

## Application 1: Expected Amount of Money Spent in a Store

**Problem.** The number of people entering a department store on a given day is a random variable $N$ with mean 50 and variance 100. The amount of money spent by each customer $X_i$ is iid with mean \$8 and standard deviation \$4. The amount spent by a customer is independent of the total number of customers. Find the expected total amount of money $T$ spent in the store on a given day.

**Setup.** The total spending is a **random sum**:

$$
T = \sum_{i=1}^{N} X_i
$$

**Step 1: Compute $E(T \mid N)$.**

Conditioning on $N$, the number of summands is fixed. By linearity of conditional expectation and by independence of $X_i$ from $N$:

$$
E(T \mid N) = E\!\left(\sum_{i=1}^{N} X_i \;\middle|\; N\right) = \sum_{i=1}^{N} E(X_i \mid N) = \sum_{i=1}^{N} E(X_i) = 8N
$$

Note that $E(T \mid N) = 8N$ is a random variable — a function of $N$.

**Step 2: Apply the tower property.**

$$
E(T) = E\bigl[E(T \mid N)\bigr] = E(8N) = 8 \, E(N) = 8 \times 50 = 400
$$

**Step 3: Compute $\text{Var}(T)$ using the law of total variance.**

First, $\text{Var}(T \mid N)$:

$$
\text{Var}(T \mid N) = \sum_{i=1}^{N} \text{Var}(X_i) = 16N
$$

Now apply Eve's law:

$$
\text{Var}\bigl(E(T \mid N)\bigr) = \text{Var}(8N) = 64 \, \text{Var}(N) = 64 \times 100 = 6400
$$

$$
E\bigl[\text{Var}(T \mid N)\bigr] = E(16N) = 16 \, E(N) = 16 \times 50 = 800
$$

$$
\text{Var}(T) = 6400 + 800 = 7200
$$

### General Random Sum Formula

For $T = \sum_{i=1}^{N} X_i$ where $X_i$ are iid with mean $\mu$ and variance $\sigma^2$, and $N$ is independent of the $X_i$'s:

$$
E(T) = \mu \, E(N)
$$

$$
\text{Var}(T) = \sigma^2 \, E(N) + \mu^2 \, \text{Var}(N)
$$

---

## Application 2: Trapped Miner

**Problem.** A miner is trapped in a mine with 3 doors. Door 1 leads to safety after 3 hours. Door 2 returns him to the mine after 5 hours. Door 3 returns him to the mine after 7 hours. The miner chooses each door with equal probability \$1/3$. Find $E(T)$, the expected time to reach safety.

**Setup.** Let $T$ be the total exit time and $X$ be the first door chosen. This is a **first-step analysis**: we condition on what happens at the first step.

$$
E(T \mid X = x) = \begin{cases}
3 & \text{if } x = 1 \quad \text{(reaches safety)} \\
5 + E(T) & \text{if } x = 2 \quad \text{(returns to same situation)} \\
7 + E(T) & \text{if } x = 3 \quad \text{(returns to same situation)}
\end{cases}
$$

The crucial insight for doors 2 and 3: after returning to the mine, the miner faces the exact same problem again (by the memoryless structure of the setup), so the remaining expected time is $E(T)$.

**Apply the tower property:**

$$
E(T) = E\bigl[E(T \mid X)\bigr] = 3 \cdot \tfrac{1}{3} + (5 + E(T)) \cdot \tfrac{1}{3} + (7 + E(T)) \cdot \tfrac{1}{3}
$$

$$
E(T) = \frac{3 + 5 + E(T) + 7 + E(T)}{3} = \frac{15 + 2\,E(T)}{3} = 5 + \tfrac{2}{3}\,E(T)
$$

$$
\tfrac{1}{3}\,E(T) = 5 \implies \boxed{E(T) = 15}
$$

### Variance of the Trapped Miner

**$\text{Var}\bigl(E(T \mid X)\bigr)$:** The conditional expectation takes values $3$, $5 + E(T) = 20$, and $7 + E(T) = 22$, each with probability \$1/3$:

$$
\text{Var}\bigl(E(T \mid X)\bigr) = \frac{3^2 + 20^2 + 22^2}{3} - 15^2 = \frac{9 + 400 + 484}{3} - 225 = 297.67 - 225 = 72.67
$$

**$E\bigl[\text{Var}(T \mid X)\bigr]$:** If the miner reaches safety (door 1), $\text{Var}(T \mid X = 1) = 0$ (deterministic). If returned to the mine, the remaining time has variance $\text{Var}(T)$:

$$
\text{Var}(T \mid X) = \begin{cases}
0 & \text{with probability } 1/3 \\
\text{Var}(T) & \text{with probability } 1/3 \\
\text{Var}(T) & \text{with probability } 1/3
\end{cases}
$$

$$
E\bigl[\text{Var}(T \mid X)\bigr] = 0 \cdot \tfrac{1}{3} + \text{Var}(T) \cdot \tfrac{1}{3} + \text{Var}(T) \cdot \tfrac{1}{3} = \tfrac{2}{3}\,\text{Var}(T)
$$

**Eve's law:**

$$
\text{Var}(T) = 72.67 + \tfrac{2}{3}\,\text{Var}(T)
$$

$$
\tfrac{1}{3}\,\text{Var}(T) = 72.67 \implies \boxed{\text{Var}(T) = 218}
$$

---

## Application 3: Waiting Time for HT

**Problem.** Flip a fair coin repeatedly until the pattern HT appears. Let $W_{HT}$ be the number of flips. Find $E(W_{HT})$ and $\text{Var}(W_{HT})$.

**Key observation:** The waiting time for HT decomposes as a sum of **independent** geometric random variables:

$$
W_{HT} = X + Y
$$

where $X$ is the number of flips to get the first H (including the H itself), and $Y$ is the number of additional flips after the first H to get a T. Both $X$ and $Y$ are $\text{Geo}(1/2)$.

The reason is: any sequence of T's before the first H is "wasted" (we need an H first), and once we have an H, any additional H's are also "wasted" (we need a T to complete the pattern). The T's before the first H don't interfere with the subsequent task of getting a T after an H.

**Expectation:**

$$
E(W_{HT}) = E(X) + E(Y) = \frac{1}{1/2} + \frac{1}{1/2} = 2 + 2 = 4
$$

**Variance** (using independence):

$$
\text{Var}(W_{HT}) = \text{Var}(X) + \text{Var}(Y) = \frac{1/2}{(1/2)^2} + \frac{1/2}{(1/2)^2} = 2 + 2 = 4
$$

---

## Application 4: Waiting Time for HH — Expectation

**Problem.** Flip a fair coin until the pattern HH appears. Let $W_{HH}$ be the number of flips. Find $E(W_{HH})$.

**Why HH is harder than HT.** Unlike HT, the pattern HH cannot be decomposed into independent pieces. After getting the first H, if the next flip is T, we must start completely over — the H we just got is useless for forming HH. This creates a recursive structure.

**Setup.** Let $X \sim \text{Geo}(1/2)$ be the number of flips to get the first H. After that first H (at the $X$-th flip), let $Y$ denote the result of the next coin flip.

$$
E(W_{HH} \mid Y = y) = \begin{cases}
E(X) + 1 = 3 & \text{if } y = 1 \text{ (H — pattern complete)} \\
E(X) + 1 + E(W_{HH}) = 3 + E(W_{HH}) & \text{if } y = 0 \text{ (T — restart)}
\end{cases}
$$

**Apply the tower property:**

$$
E(W_{HH}) = 3 \cdot \tfrac{1}{2} + (3 + E(W_{HH})) \cdot \tfrac{1}{2} = \frac{3 + 3 + E(W_{HH})}{2} = 3 + \tfrac{1}{2}\,E(W_{HH})
$$

$$
\tfrac{1}{2}\,E(W_{HH}) = 3 \implies \boxed{E(W_{HH}) = 6}
$$

Note that $E(W_{HH}) = 6 > 4 = E(W_{HT})$: waiting for HH takes longer on average than waiting for HT.

---

## Application 5: Waiting Time for HH — Variance

**$\text{Var}\bigl(E(W_{HH} \mid Y)\bigr)$:**

$$
E(W_{HH} \mid Y) = \begin{cases}
3 & \text{with probability } 1/2 \\
3 + E(W_{HH}) = 9 & \text{with probability } 1/2
\end{cases}
$$

$$
\text{Var}\bigl(E(W_{HH} \mid Y)\bigr) = \frac{3^2 + 9^2}{2} - 6^2 = \frac{9 + 81}{2} - 36 = 45 - 36 = 9
$$

**$E\bigl[\text{Var}(W_{HH} \mid Y)\bigr]$:**

If $Y = 1$ (success), then $W_{HH} = X + 1$ where $X \sim \text{Geo}(1/2)$, so $\text{Var}(W_{HH} \mid Y = 1) = \text{Var}(X) = 2$.

If $Y = 0$ (failure), then $W_{HH} = X + 1 + W'_{HH}$ where $X$ and $W'_{HH}$ are independent, so $\text{Var}(W_{HH} \mid Y = 0) = \text{Var}(X) + \text{Var}(W_{HH}) = 2 + \text{Var}(W_{HH})$.

$$
E\bigl[\text{Var}(W_{HH} \mid Y)\bigr] = 2 \cdot \tfrac{1}{2} + \bigl(2 + \text{Var}(W_{HH})\bigr) \cdot \tfrac{1}{2} = 2 + \tfrac{1}{2}\,\text{Var}(W_{HH})
$$

**Eve's law:**

$$
\text{Var}(W_{HH}) = 9 + 2 + \tfrac{1}{2}\,\text{Var}(W_{HH}) = 11 + \tfrac{1}{2}\,\text{Var}(W_{HH})
$$

$$
\tfrac{1}{2}\,\text{Var}(W_{HH}) = 11 \implies \boxed{\text{Var}(W_{HH}) = 22}
$$

---

## Python Simulation: All Waiting Time Problems

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
            flip = np.random.randint(0, 2)  # 0=T, 1=H
            flips.append(flip)
            count += 1
            if len(flips) >= 2 and flips[-2] == pattern[0] and flips[-1] == pattern[1]:
                break
        results.append(count)
    return np.array(results)

# Simulate HT and HH
W_HT = simulate_pattern([1, 0], n_sim)
W_HH = simulate_pattern([1, 1], n_sim)

print("=== Waiting Time for HT ===")
print(f"E(W_HT) = {W_HT.mean():.3f}  (theory: 4)")
print(f"Var(W_HT) = {W_HT.var():.3f}  (theory: 4)")

print("\n=== Waiting Time for HH ===")
print(f"E(W_HH) = {W_HH.mean():.3f}  (theory: 6)")
print(f"Var(W_HH) = {W_HH.var():.3f}  (theory: 22)")

# Simulate trapped miner
miner_times = []
for _ in range(n_sim):
    t = 0
    while True:
        door = np.random.randint(1, 4)
        if door == 1:
            t += 3
            break
        elif door == 2:
            t += 5
        else:
            t += 7
    miner_times.append(t)
miner_times = np.array(miner_times)

print("\n=== Trapped Miner ===")
print(f"E(T) = {miner_times.mean():.2f}  (theory: 15)")
print(f"Var(T) = {miner_times.var():.1f}  (theory: 218)")

# Simulate department store
store_totals = []
for _ in range(n_sim):
    N = int(np.random.normal(50, 10))  # mean 50, var 100
    N = max(N, 0)
    spending = np.random.normal(8, 4, N)  # mean 8, sd 4
    store_totals.append(spending.sum())
store_totals = np.array(store_totals)

print("\n=== Department Store ===")
print(f"E(T) = {store_totals.mean():.1f}  (theory: 400)")
print(f"Var(T) = {store_totals.var():.0f}  (theory: 7200)")
```
