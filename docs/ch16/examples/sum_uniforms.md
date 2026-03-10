# Sum of Uniforms

The convolution of two uniform densities produces a triangular distribution; further convolutions yield the Irwin-Hall distribution, which rapidly approaches the normal.

## Definition

If $X$ and $Y$ are iid $U(0, 1)$, then $X + Y$ has the **triangular distribution** on $(0, 2)$:

$$
f_{X+Y}(a) = \begin{cases} a & 0 \le a \le 1 \\ 2 - a & 1 < a \le 2 \end{cases}
$$

The $n$-fold convolution $U(0,1) * \cdots * U(0,1)$ is called the **Irwin-Hall distribution** $\operatorname{IH}(n)$, supported on $(0, n)$ with piecewise polynomial density of degree $n - 1$.

## Explanation

### Derivation for Two Uniforms

For iid $X, Y \sim U(0, 1)$ and $0 \le a \le 1$:

$$
f_{X+Y}(a) = \int_0^a 1 \cdot 1 \, db = a
$$

The limits come from requiring $0 \le b \le 1$ and $0 \le a - b \le 1$, giving $\max(0, a-1) \le b \le \min(1, a)$. For $0 \le a \le 1$, this is $[0, a]$.

For $1 < a \le 2$: the limits become $[a-1, 1]$, giving $f_{X+Y}(a) = 2 - a$.

### Symmetric Version

For iid $X, Y \sim U(-1/2, 1/2)$:

$$
f_{X+Y}(a) = (1 - |a|)^+, \quad -1 \le a \le 1
$$

This is a centered triangle. The $U(0,1)$ result is a shift: if $X' = X - 1/2$, then $X + Y = (X' + Y') + 1$.

### CLT in Action

As $n$ grows, $S_n = X_1 + \cdots + X_n$ (iid $U(0,1)$) has mean $n/2$ and variance $n/12$. The standardized sum converges to $N(0,1)$ — already an excellent approximation by $n = 12$.

## Examples

**Example.** Verify $U(0,1) * U(0,1) = \operatorname{Triangular}(0, 2)$ and the CLT convergence.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 100_000

# Sum of two U(0,1): should be triangular
X = np.random.uniform(0, 1, n_sim)
Y = np.random.uniform(0, 1, n_sim)
S = X + Y

print(f"S = U+U: mean={S.mean():.4f} (theory 1.0), var={S.var():.4f} (theory {1/6:.4f})")

# CLT convergence: sum of n uniforms
for n in [2, 4, 12, 30]:
    samples = np.random.uniform(0, 1, (n_sim, n)).sum(axis=1)
    standardized = (samples - n/2) / np.sqrt(n/12)
    ks_stat, p_val = stats.kstest(standardized, 'norm')
    print(f"n={n:2d}: KS stat={ks_stat:.4f}, p-value={p_val:.4f}")
```
