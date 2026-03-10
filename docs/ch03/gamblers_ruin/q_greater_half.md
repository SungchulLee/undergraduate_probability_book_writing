# Unfair Game Solution (q > 1/2)

When the game is unfair ($q > p$), ruin is nearly certain. The ruin probability converges to 1 exponentially fast as the gambler's starting capital decreases.

## Definition

For $p \ne 1/2$ (distinct characteristic roots $1$ and $q/p$):

$$
Q(i) = \frac{(q/p)^N - (q/p)^i}{(q/p)^N - 1}
$$

## Explanation

### Derivation

General solution: $Q(i) = \alpha + \beta(q/p)^i$.

From $Q(0) = 1$: $\alpha + \beta = 1$.
From $Q(N) = 0$: $\alpha + \beta(q/p)^N = 0$.

Solving: $\alpha = (q/p)^N / ((q/p)^N - 1)$, $\beta = -1/((q/p)^N - 1)$.

### Exponential Convergence to Ruin

Since $q/p > 1$, for large $N$: $(q/p)^N \gg (q/p)^i$, so

$$
Q(i) \approx 1 - (q/p)^{-(N-i)} = 1 - e^{-(N-i)\ln(q/p)}
$$

The ruin probability approaches 1 exponentially fast as $i$ decreases from $N$.

## Examples

**Example ($p = 0.49$, $N = 200$):**

| $i$ | $Q(i)$ |
|:---:|:---:|
| 200 | 0 |
| 190 | 0.331 |
| 150 | 0.982 |
| 100 | 0.9998 |

Starting halfway to the goal, ruin is 99.98% certain — despite losing only a 2% edge per bet.

```python
def Q(i, N, p):
    r = (1 - p) / p
    return (r**N - r**i) / (r**N - 1)

N = 200
for i in [200, 190, 150, 100, 50]:
    print(f"Q({i}) = {Q(i, N, 0.49):.6f}")
```
