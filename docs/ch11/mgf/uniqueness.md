# Uniqueness Theorem

If two random variables share the same MGF in a neighborhood of zero, they have the same distribution — enabling distribution identification purely from the MGF.

## Definition

**Uniqueness theorem.** If $M_X(t) = M_Y(t)$ for all $t \in (-h, h)$ with $h > 0$, then $X \stackrel{d}{=} Y$.

**Convergence theorem.** If $M_{X_n}(t) \to M_Y(t)$ for all $t$ in a neighborhood of 0, then $X_n \xrightarrow{d} Y$.

## Explanation

### Why Uniqueness Holds

The MGF is a Laplace transform of the distribution. Since the Laplace transform is injective when it converges in a neighborhood of the origin, no two different distributions can share the same MGF.

### Strategy: Identify via MGF

1. Compute $M_X(t)$ from the definition or by algebraic manipulation
2. Recognize the result as the MGF of a known distribution
3. Conclude $X$ has that distribution by uniqueness

This is especially powerful for sums: compute $M_{X+Y}(t) = M_X(t)\,M_Y(t)$ and recognize the product.

### Convergence and the CLT

The convergence version is the key tool for proving the CLT: show the MGF of the standardized sum converges to $e^{t^2/2}$ (the MGF of $N(0,1)$).

## Examples

**Example.** $X \sim \text{Bin}(n, p)$, $Y \sim \text{Bin}(m, p)$ independent.

$$
M_{X+Y}(t) = (q + pe^t)^{n+m}
$$

By uniqueness, $X + Y \sim \text{Bin}(n + m, p)$.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

X = np.random.binomial(10, 0.3, n_sim)
Y = np.random.binomial(15, 0.3, n_sim)
S = X + Y
Z = np.random.binomial(25, 0.3, n_sim)

print(f"X+Y: mean={S.mean():.3f}, var={S.var():.3f}")
print(f"Bin(25,0.3): mean={Z.mean():.3f}, var={Z.var():.3f}")
print(f"Theory: mean={25*0.3}, var={25*0.3*0.7}")
```
