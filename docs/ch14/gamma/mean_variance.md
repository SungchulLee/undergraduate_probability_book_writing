# Mean and Variance of the Gamma Distribution

The moments of the Gamma distribution follow a clean pattern: the shape parameter $\alpha$ scales both the mean and the variance, while the rate $\lambda$ sets the time scale.

## Definition

If $X \sim \Gamma(\alpha, \lambda)$, then

$$
E[X] = \frac{\alpha}{\lambda}, \qquad \text{Var}(X) = \frac{\alpha}{\lambda^2}
$$

The $k$-th moment is

$$
E[X^k] = \frac{\Gamma(\alpha + k)}{\lambda^k \, \Gamma(\alpha)}
$$

## Explanation

### Deriving the Mean

$$
E[X] = \int_0^\infty x \cdot \frac{\lambda(\lambda x)^{\alpha - 1} e^{-\lambda x}}{\Gamma(\alpha)} \, dx
$$

The key technique is to **recognize a Gamma PDF inside the integral**. Multiply and divide to create the PDF of $\Gamma(\alpha + 1, \lambda)$:

$$
E[X] = \frac{\Gamma(\alpha + 1)}{\lambda \, \Gamma(\alpha)} \int_0^\infty \underbrace{\frac{\lambda(\lambda x)^{(\alpha+1)-1} e^{-\lambda x}}{\Gamma(\alpha + 1)}}_{\text{PDF of } \Gamma(\alpha+1, \lambda)} \, dx = \frac{\alpha \, \Gamma(\alpha)}{\lambda \, \Gamma(\alpha)} = \frac{\alpha}{\lambda}
$$

The integral equals 1 because it integrates a valid PDF, and we used $\Gamma(\alpha + 1) = \alpha \, \Gamma(\alpha)$.

### Deriving the Second Moment

Similarly, create the PDF of $\Gamma(\alpha + 2, \lambda)$:

$$
E[X^2] = \frac{\Gamma(\alpha + 2)}{\lambda^2 \, \Gamma(\alpha)} \int_0^\infty \underbrace{\frac{\lambda(\lambda x)^{(\alpha+2)-1} e^{-\lambda x}}{\Gamma(\alpha + 2)}}_{\text{PDF of } \Gamma(\alpha+2, \lambda)} \, dx = \frac{(\alpha + 1)\alpha \, \Gamma(\alpha)}{\lambda^2 \, \Gamma(\alpha)} = \frac{\alpha(\alpha + 1)}{\lambda^2}
$$

using $\Gamma(\alpha + 2) = (\alpha + 1)\alpha \, \Gamma(\alpha)$.

### Deriving the Variance

$$
\text{Var}(X) = E[X^2] - (E[X])^2 = \frac{\alpha(\alpha + 1)}{\lambda^2} - \frac{\alpha^2}{\lambda^2} = \frac{\alpha}{\lambda^2}
$$

### The General Moment Technique

The derivations above illustrate a powerful technique: to compute $E[X^k]$ for a Gamma random variable, **reshape the integrand to be a Gamma PDF with shifted parameters**, then use the fact that a PDF integrates to 1.

In general, for $X \sim \Gamma(\alpha, \lambda)$:

$$
E[X^k] = \frac{\Gamma(\alpha + k)}{\lambda^k \, \Gamma(\alpha)}
$$

For integer $k$, this simplifies using the recursion $\Gamma(\alpha + k) = (\alpha + k - 1)(\alpha + k - 2) \cdots \alpha \cdot \Gamma(\alpha)$:

$$
E[X^k] = \frac{\alpha(\alpha+1)\cdots(\alpha+k-1)}{\lambda^k}
$$

### Discrete-Continuous Analogy

| Distribution | Mean | Variance |
|:---:|:---:|:---:|
| $\text{Geo}(p)$ | $\dfrac{1}{p}$ | $\dfrac{q}{p^2}$ |
| $\text{NegBin}(n, p)$ | $\dfrac{n}{p}$ | $\dfrac{nq}{p^2}$ |
| $\text{Exp}(\lambda)$ | $\dfrac{1}{\lambda}$ | $\dfrac{1}{\lambda^2}$ |
| $\Gamma(\alpha, \lambda)$ | $\dfrac{\alpha}{\lambda}$ | $\dfrac{\alpha}{\lambda^2}$ |

The pattern is clear: the shape parameter $\alpha$ scales both the mean and the variance linearly, while the rate parameter $\lambda$ appears in the denominator (once for the mean, squared for the variance). The continuous Gamma formulas arise from the discrete Negative Binomial formulas by taking $q \to 1$ (since $q = 1 - p$ and $p \to 0$ in the continuous limit).

### Coefficient of Variation

$$
\text{CV}(X) = \frac{\text{SD}(X)}{E[X]} = \frac{\sqrt{\alpha}/\lambda}{\alpha/\lambda} = \frac{1}{\sqrt{\alpha}}
$$

As $\alpha$ increases, the distribution becomes relatively more concentrated around its mean. When $\alpha = 1$ (Exponential), $\text{CV} = 1$. When $\alpha = 100$, $\text{CV} = 0.1$ -- the distribution is tightly peaked.

## Examples

**Example 1.** Let $X \sim \Gamma(5, 2)$. Find $E[X]$, $\text{Var}(X)$, $E[X^2]$, and $E[X^3]$.

- $E[X] = 5/2 = 2.5$
- $\text{Var}(X) = 5/4 = 1.25$
- $E[X^2] = \text{Var}(X) + (E[X])^2 = 1.25 + 6.25 = 7.5$
- $E[X^3] = \frac{5 \cdot 6 \cdot 7}{2^3} = \frac{210}{8} = 26.25$

**Example 2.** Verify the mean, variance, and higher moments for several parameter combinations.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 200_000

# --- Mean and variance verification ---
print("=== Mean and Variance ===")
print(f"{'alpha':>6} {'lam':>5} | {'E[X] thy':>9} {'E[X] sim':>9} | "
      f"{'Var thy':>9} {'Var sim':>9}")
print("-" * 60)

params = [(1, 1), (2, 1), (3, 2), (5, 2), (0.5, 0.5), (10, 3)]
for alpha, lam in params:
    X = np.random.gamma(shape=alpha, scale=1/lam, size=n_sim)
    print(f"{alpha:6.1f} {lam:5.1f} | {alpha/lam:9.4f} {np.mean(X):9.4f} | "
          f"{alpha/lam**2:9.4f} {np.var(X):9.4f}")

# --- Higher moments for Gamma(5, 2) ---
alpha, lam = 5, 2
X = np.random.gamma(shape=alpha, scale=1/lam, size=n_sim)

print(f"\n=== Higher Moments of Gamma({alpha}, {lam}) ===")
for k in range(1, 5):
    # E[X^k] = alpha*(alpha+1)*...*(alpha+k-1) / lambda^k
    theory = 1.0
    for j in range(k):
        theory *= (alpha + j)
    theory /= lam**k
    simulated = np.mean(X**k)
    print(f"E[X^{k}]: theory={theory:.4f}, sim={simulated:.4f}")

# --- Coefficient of variation ---
print(f"\n=== Coefficient of Variation ===")
for alpha in [1, 4, 25, 100]:
    X = np.random.gamma(shape=alpha, scale=1.0, size=n_sim)
    cv_thy = 1 / np.sqrt(alpha)
    cv_sim = np.std(X) / np.mean(X)
    print(f"alpha={alpha:3d}: CV theory={cv_thy:.4f}, CV sim={cv_sim:.4f}")
```
