# Decomposition of a Random Variable

## Concept

Many important random variables can be **decomposed** as sums of simpler, often iid, random variables. This decomposition allows us to compute means and variances easily using the formulas for sums.

$$

S = \sum_{i=1}^n X_i \quad \Longrightarrow \quad E[S] = \sum_{i=1}^n E[X_i], \quad \text{Var}(S) = \sum_{i=1}^n \text{Var}(X_i) \text{ (if independent)}

$$

---

## Example 1: Binomial via Bernoulli

Flip a $p$-coin $n$ times independently and count the number $S$ of heads. Let $A_i$ be the event that the $i$-th coin lands heads and $\mathbf{1}_{A_i}$ its indicator.

$$

\mathbf{1}_{A_i} \stackrel{iid}{\sim} \text{Bernoulli}(p) \quad \Longrightarrow \quad S = \sum_{i=1}^n \mathbf{1}_{A_i} \sim \text{Binomial}(n, p)

$$

$$

E[S] = \sum_{i=1}^n E[\mathbf{1}_{A_i}] = np

$$

$$

\text{Var}(S) = \sum_{i=1}^n \text{Var}(\mathbf{1}_{A_i}) = npq

$$

---

## Example 2: Negative Binomial via Geometric

Flip a $p$-coin until the $r$-th head. Let $X_i$ be the number of flips to get the $i$-th head after the $(i-1)$-th head.

$$

X_i \stackrel{iid}{\sim} \text{Geo}(p) \quad \Longrightarrow \quad S = \sum_{i=1}^r X_i \sim \text{NB}(r, p)

$$

$$

E[S] = \sum_{i=1}^r E[X_i] = \frac{r}{p}

$$

$$

\text{Var}(S) = \sum_{i=1}^r \text{Var}(X_i) = \frac{rq}{p^2}

$$

---

## Example 3: Roll the Dice 1000 Times

Roll a die 1000 times. Gain the face value for odd outcomes and lose the face value for even outcomes. Add a $+0.5$ bonus per game for fairness.

$$

D_i = \begin{cases} +1 & \text{w.p. } 1/6 \\ -2 & \text{w.p. } 1/6 \\ +3 & \text{w.p. } 1/6 \\ -4 & \text{w.p. } 1/6 \\ +5 & \text{w.p. } 1/6 \\ -6 & \text{w.p. } 1/6 \end{cases}

$$

Let $X_i = D_i + 0.5$ (iid). The total P\&L is $S = \sum_{i=1}^{1000} X_i$.

**Moments of $D_i$**:

$$

E[D_i] = \frac{1 - 2 + 3 - 4 + 5 - 6}{6} = -0.5

$$

$$

E[D_i^2] = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6} \approx 15.1667

$$

$$

\text{Var}(D_i) = 15.1667 - 0.25 = 14.9167

$$

**Moments of $X_i = D_i + 0.5$**: $E[X_i] = 0$, $\text{Var}(X_i) = 14.9167$.

**Moments of $S$**:

$$

E[S] = 1000 \times 0 = 0

$$

$$

\text{Var}(S) = 1000 \times 14.9167 = 14916.7, \quad \text{SD}(S) \approx 122.1

$$

---

## Example 4: Coupon Collector Problem

To collect all $n$ types of toys from McDonald's Happy Meals, let $\tau_i$ be the number of meals needed to find the $i$-th new toy after having collected $i-1$ distinct toys. Then:

$$

\tau_i \sim \text{Geo}\left(\frac{n - (i-1)}{n}\right), \quad \tau_i \text{ independent}

$$

$$

T_n = \sum_{i=1}^n \tau_i

$$

**Mean**:

$$

E[T_n] = \sum_{i=1}^n E[\tau_i] = \sum_{i=1}^n \frac{n}{n - (i-1)} = n\left(1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}\right) = nH_n \sim n\log n

$$

**Variance**:

$$

\text{Var}(T_n) = \sum_{k=1}^n \frac{1 - k/n}{(k/n)^2} = n^2 \sum_{k=1}^n \frac{1}{k^2} - n\sum_{k=1}^n \frac{1}{k} \approx \frac{\pi^2}{6}n^2 - n\log n

$$

So $\text{Var}(T_n) = O(n^2)$.

---

## Summary Table

| Distribution | Decomposition | $E[S]$ | $\text{Var}(S)$ |
|:---:|:---:|:---:|:---:|
| $\text{Binomial}(n,p)$ | $\sum_{i=1}^n \text{Bernoulli}(p)$ | $np$ | $npq$ |
| $\text{NB}(r,p)$ | $\sum_{i=1}^r \text{Geo}(p)$ | $r/p$ | $rq/p^2$ |
| Coupon collector | $\sum_{i=1}^n \text{Geo}((n-i+1)/n)$ | $nH_n$ | $\approx \frac{\pi^2}{6}n^2$ |

---

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Dice game simulation
# ============================================================
np.random.seed(42)
NumSimu = 10000
NumRolling = 1000

rolls = np.random.randint(1, 7, size=(NumRolling, NumSimu))
increment = np.where(rolls % 2 == 1, rolls, -rolls).astype(float) + 0.5
Sn = np.cumsum(increment, axis=0)
total_pnl = Sn[-1, :]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].hist(total_pnl, bins=50, edgecolor='black')
axes[0].set_xlabel('Total P&L')
axes[0].set_title('Histogram of Total P&L after 1000 Games')
axes[0].grid(True, alpha=0.3)

axes[1].plot(range(1, NumRolling + 1), Sn[:, 0])
axes[1].set_xlabel('Game number')
axes[1].set_ylabel('Cumulative P&L')
axes[1].set_title('Sample Path of Cumulative P&L')
axes[1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('dice_game_decomposition.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# Coupon collector simulation
# ============================================================
n_toys = 20
N_sim = 50000
T_samples = []
for _ in range(N_sim):
    collected = set()
    count = 0
    while len(collected) < n_toys:
        toy = np.random.randint(0, n_toys)
        collected.add(toy)
        count += 1
    T_samples.append(count)

T_samples = np.array(T_samples)
H_n = sum(1/k for k in range(1, n_toys + 1))
E_Tn = n_toys * H_n
Var_Tn = n_toys**2 * sum(1/k**2 for k in range(1, n_toys + 1)) - n_toys * H_n

print(f"Coupon Collector (n={n_toys}):")
print(f"  Theoretical E[T] = {E_Tn:.2f}, Simulated = {np.mean(T_samples):.2f}")
print(f"  Theoretical SD(T) = {np.sqrt(Var_Tn):.2f}, Simulated = {np.std(T_samples):.2f}")
```
