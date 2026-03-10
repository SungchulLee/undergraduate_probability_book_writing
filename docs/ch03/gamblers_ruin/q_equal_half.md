# Fair Game Solution (q = 1/2)

When the game is fair ($p = q = 1/2$), the characteristic equation has a double root, yielding a linear ruin probability.

## Definition

For $p = q = 1/2$:

$$
Q(i) = \frac{N - i}{N}
$$

## Explanation

### Double Root

The characteristic equation $\frac{1}{2}\lambda^2 - \lambda + \frac{1}{2} = 0$ simplifies to $(\lambda-1)^2 = 0$, giving a double root $\lambda = 1$.

The two linearly independent solutions are $Q_1(i) = 1$ and $Q_2(i) = i$ (verify: $\frac{1}{2}(i+1) + \frac{1}{2}(i-1) = i$ ✓).

General solution: $Q(i) = \alpha + \beta i$.

Boundary conditions: $Q(0) = 1 \Rightarrow \alpha = 1$; $Q(N) = 0 \Rightarrow \beta = -1/N$.

### Interpretation

| $i$ | $Q(i)$ |
|:---:|:---:|
| $0$ | $1$ |
| $N/4$ | $3/4$ |
| $N/2$ | $1/2$ |
| $3N/4$ | $1/4$ |
| $N$ | $0$ |

Ruin probability decreases linearly with initial capital. Starting halfway gives exactly 50% ruin.

## Examples

**Example.** Fair game, goal $N = 100$. Starting with \$40: $Q(40) = 60/100 = 0.6$.

| Fair ($p=0.5$) vs Unfair ($p=0.49$) | $Q(i)$ |
|:---|:---:|
| Fair, $i=100$, $N=200$ | $0.50$ |
| Unfair, $i=100$, $N=200$ | $0.9998$ |

The 2% edge transforms a coin-flip outcome into near-certain ruin.

```python
# Compare fair vs unfair
def Q(i, N, p):
    q = 1 - p
    if abs(p - 0.5) < 1e-10:
        return (N - i) / N
    r = q / p
    return (r**N - r**i) / (r**N - 1)

N = 200
for i in [50, 100, 150]:
    print(f"i={i}: fair={Q(i,N,0.5):.4f}, unfair={Q(i,N,0.49):.6f}")
```
