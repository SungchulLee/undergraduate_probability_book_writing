# Gambler's Ruin Problem

The gambler's ruin is the foundational example of a random walk with absorbing barriers. It demonstrates that even a nearly fair game leads to near-certain ruin, making it one of the most important models in probability.

## Definition

A gambler starts with \$$i$ and bets \$$1$ per round: win \$$1$ with probability $p$, lose \$$1$ with probability $q = 1-p$. The game ends at ruin (\$$0$) or at the goal (\$$N$).

Let $Q(i) = P(\text{ruin} \mid \text{start with } i)$, with $Q(0) = 1$ and $Q(N) = 0$.

## Explanation

### Solution Summary

**Unfair game ($p \ne 1/2$):**

$$
Q(i) = \frac{(q/p)^N - (q/p)^i}{(q/p)^N - 1}
$$

**Fair game ($p = 1/2$):**

$$
Q(i) = \frac{N - i}{N}
$$

### Why "Gambler's Ruin"?

When $q > p$ (house edge), $(q/p)^N$ grows exponentially, driving $Q(i)$ toward 1 for all but the largest $i$. Even $p = 0.49$ with $i = 100$, $N = 200$ gives $Q(100) > 99.98\%$. The house edge compounds over the many rounds needed to double one's money.

In the fair game, ruin probability is still $1 - i/N$ — starting halfway gives 50% ruin.

## Examples

**Example ($p = 0.49$, $N = 200$):**

| Initial capital $i$ | $Q(i)$ |
|:---:|:---:|
| 200 | 0 |
| 190 | 0.33 |
| 150 | 0.98 |
| 100 | 0.9998 |
| 50 | $\approx 1$ |

```python
def ruin_prob(i, N, p):
    q = 1 - p
    if abs(p - 0.5) < 1e-10:
        return (N - i) / N
    r = q / p
    return (r**N - r**i) / (r**N - 1)

for i in [200, 190, 150, 100, 50, 0]:
    print(f"Q({i}) = {ruin_prob(i, 200, 0.49):.6f}")
```
