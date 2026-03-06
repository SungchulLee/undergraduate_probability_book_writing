# Maximization of Expected Profit (Newsboy Problem)

## Problem Setup

A newsvendor must decide how many newspapers $q$ to order before observing demand $D$. Each newspaper costs $c$ and sells for $s > c$. Unsold newspapers have salvage value $v < c$.

- If $D \geq q$: sell all $q$ newspapers, profit $= q(s - c)$
- If $D < q$: sell $D$ at price $s$, salvage $q - D$ at value $v$

The profit is:

$$

\Pi(q) = s \min(D, q) + v \max(q - D, 0) - cq

$$

---

## Expected Profit

$$

E[\Pi(q)] = s \, E[\min(D, q)] + v \, E[\max(q - D, 0)] - cq

$$

### Optimal Order Quantity

The optimal $q^*$ satisfies the **critical ratio** condition:

$$

P(D \leq q^*) = \frac{s - c}{s - v}

$$

The ratio $\frac{s-c}{s-v}$ is called the **critical ratio** or **service level**. It balances the cost of ordering too much (overage cost $c - v$) against the cost of ordering too little (underage cost $s - c$).

---

## Derivation

The expected profit can be written as:

$$

E[\Pi(q)] = (s - c)E[D] - (s - c)E[\max(D - q, 0)] - (c - v)E[\max(q - D, 0)]

$$

Taking the derivative with respect to $q$ and setting it to zero:

$$

\frac{d}{dq}E[\Pi(q)] = (s - c)P(D > q) - (c - v)P(D \leq q) = 0

$$

Solving: $P(D \leq q^*) = \frac{s - c}{s - v}$.

---

## Example

Suppose demand $D \sim N(100, 20^2)$, selling price $s = 10$, cost $c = 6$, salvage $v = 2$.

Critical ratio: $\frac{s - c}{s - v} = \frac{10 - 6}{10 - 2} = 0.5$

Since $P(D \leq q^*) = 0.5$ for a symmetric normal, $q^* = 100$.

If the critical ratio were $0.75$: $q^* = \mu + \sigma \Phi^{-1}(0.75) = 100 + 20 \times 0.6745 \approx 113.5$.

---

## Python Implementation

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Parameters
mu_d, sigma_d = 100, 20
s, c, v = 10, 6, 2

# Critical ratio and optimal q
cr = (s - c) / (s - v)
q_star = stats.norm.ppf(cr, loc=mu_d, scale=sigma_d)
print(f"Critical ratio = {cr:.4f}")
print(f"Optimal order quantity q* = {q_star:.1f}")

# Monte Carlo expected profit
np.random.seed(42)
N = 100_000
D = np.random.normal(mu_d, sigma_d, N)

def mc_expected_profit(q, D, s, c, v):
    sales = np.minimum(D, q)
    salvage = np.maximum(q - D, 0)
    profit = s * sales + v * salvage - c * q
    return np.mean(profit)

q_range = np.arange(50, 151)
profits = [mc_expected_profit(q, D, s, c, v) for q in q_range]

plt.figure(figsize=(10, 6))
plt.plot(q_range, profits, 'b-', linewidth=2)
plt.axvline(x=q_star, color='r', linestyle='--', label=f'q* = {q_star:.1f}')
plt.xlabel('Order Quantity q')
plt.ylabel('Expected Profit E[Π(q)]')
plt.title('Newsboy Problem: Expected Profit vs Order Quantity')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('newsboy_profit.png', dpi=150, bbox_inches='tight')
plt.show()
```
