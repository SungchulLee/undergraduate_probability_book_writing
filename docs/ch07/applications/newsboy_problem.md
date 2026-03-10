# Newsboy Problem

The newsvendor problem finds the order quantity that maximizes expected profit under demand uncertainty — a cornerstone of inventory theory.

## Definition

A newsvendor orders $q$ units at cost $c$ per unit, sells at price $s > c$, and salvages unsold units at value $v < c$. Demand $D$ is random. The profit is

$$
\Pi(q) = s\min(D, q) + v\max(q-D, 0) - cq
$$

The optimal order quantity $q^*$ satisfies the **critical ratio** condition:

$$
P(D \le q^*) = \frac{s - c}{s - v}
$$

## Explanation

### Derivation

The expected profit derivative is

$$
\frac{d}{dq}E[\Pi(q)] = (s-c)P(D > q) - (c-v)P(D \le q)
$$

Setting to zero: $(s-c)(1 - F(q)) = (c-v)F(q)$, giving $F(q^*) = (s-c)/(s-v)$.

### Intuition

The critical ratio balances **underage cost** $(s-c)$ against **overage cost** $(c-v)$. If the profit margin is high relative to the loss on unsold items, order more aggressively.

## Examples

**Example.** $D \sim N(100, 20^2)$, $s = 10$, $c = 6$, $v = 2$.

Critical ratio: $(10-6)/(10-2) = 0.5$. Since $\Phi^{-1}(0.5) = 0$: $q^* = 100$.

If $s = 12$: critical ratio $= 6/10 = 0.6$, so $q^* = 100 + 20\Phi^{-1}(0.6) \approx 105.1$.

```python
from scipy import stats

mu, sigma = 100, 20
s, c, v = 10, 6, 2

cr = (s - c) / (s - v)
q_star = stats.norm.ppf(cr, mu, sigma)
print(f"Critical ratio = {cr:.2f}, q* = {q_star:.1f}")

# Higher selling price
s2 = 12
cr2 = (s2 - c) / (s2 - v)
q_star2 = stats.norm.ppf(cr2, mu, sigma)
print(f"s=12: CR = {cr2:.2f}, q* = {q_star2:.1f}")
```
