# MGF of Normal

The normal MGF has a clean exponential-quadratic form that makes proving closure under linear transformations and sums immediate.

## Definition

If $X \sim N(\mu, \sigma^2)$:

$$
M_X(t) = \exp\!\left(\mu t + \tfrac{1}{2}\sigma^2 t^2\right)
$$

For $Z \sim N(0,1)$: $M_Z(t) = e^{t^2/2}$. The MGF exists for all $t \in \mathbb{R}$.

## Explanation

### Derivation (Completing the Square)

$$
M_X(t) = \int_{-\infty}^{\infty} e^{tx}\,\frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-(x-\mu)^2/(2\sigma^2)}\,dx
$$

The exponent $tx - (x-\mu)^2/(2\sigma^2)$ completes to $-(x - (\mu + \sigma^2 t))^2/(2\sigma^2) + \mu t + \sigma^2 t^2/2$. The remaining integral is the total mass of a $N(\mu + \sigma^2 t, \sigma^2)$ density, which equals 1.

### Closure Properties (via MGF)

**Linear transformation:** $aX + b \sim N(a\mu + b, a^2\sigma^2)$.

$$
M_{aX+b}(t) = e^{bt}M_X(at) = e^{bt}\,e^{\mu(at) + \sigma^2(at)^2/2} = e^{(a\mu+b)t + a^2\sigma^2 t^2/2}
$$

**Sum of independent normals:** $X + Y \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$.

$$
M_{X+Y}(t) = M_X(t)\,M_Y(t) = e^{(\mu_1+\mu_2)t + (\sigma_1^2+\sigma_2^2)t^2/2}
$$

### Moments

$M_Z'(0) = 0 = E[Z]$, $M_Z''(0) = 1 = E[Z^2] = \text{Var}(Z)$.

## Examples

**Example.** $X \sim N(3, 4)$, $Y \sim N(-1, 9)$ independent. Then $X + Y \sim N(2, 13)$.

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

X = np.random.normal(3, 2, n_sim)
Y = np.random.normal(-1, 3, n_sim)
S = X + Y

print(f"X+Y: mean={S.mean():.4f} (theory: 2), var={S.var():.3f} (theory: 13)")

W = 2*X + 1
print(f"2X+1: mean={W.mean():.4f} (theory: 7), var={W.var():.3f} (theory: 16)")
```
