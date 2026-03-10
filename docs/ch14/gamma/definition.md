# Gamma Distribution Definition

The Gamma distribution generalizes the Exponential to model the total waiting time for multiple events in a Poisson process, with shape parameter $\alpha$ extending naturally to non-integer values.

## Definition

A continuous random variable $X$ has the **Gamma distribution** with shape parameter $\alpha > 0$ and rate parameter $\lambda > 0$, written $X \sim \Gamma(\alpha, \lambda)$, if its PDF is

$$
f(x) = \frac{\lambda(\lambda x)^{\alpha - 1} e^{-\lambda x}}{\Gamma(\alpha)}, \quad x > 0
$$

where $\Gamma(\alpha) = \int_0^\infty u^{\alpha-1} e^{-u} \, du$ is the Gamma function.

**Moments:**

$$
E[X] = \frac{\alpha}{\lambda}, \qquad \text{Var}(X) = \frac{\alpha}{\lambda^2}
$$

**MGF:**

$$
M_X(t) = \left(\frac{\lambda}{\lambda - t}\right)^\alpha, \quad t < \lambda
$$

**Additivity.** If $X \sim \Gamma(\alpha, \lambda)$ and $Y \sim \Gamma(\beta, \lambda)$ are independent (same rate), then

$$
X + Y \sim \Gamma(\alpha + \beta, \lambda)
$$

## Explanation

### Construction as a Sum of Exponentials

When $\alpha = n$ is a positive integer, the Gamma distribution arises as the sum of $n$ iid Exponentials:

$$
X_1 + X_2 + \cdots + X_n \sim \Gamma(n, \lambda) \quad \text{where } X_i \stackrel{\text{iid}}{\sim} \text{Exp}(\lambda)
$$

This builds up through convolutions:

| Sum | Distribution |
|:---:|:---:|
| $X_1$ | $\text{Exp}(\lambda) = \Gamma(1, \lambda)$ |
| $X_1 + X_2$ | $\Gamma(2, \lambda)$ |
| $X_1 + X_2 + X_3$ | $\Gamma(3, \lambda)$ |
| $X_1 + \cdots + X_n$ | $\Gamma(n, \lambda)$ |

For non-integer $\alpha$, the Gamma distribution is defined by the PDF above and no longer has a direct "sum of Exponentials" interpretation, but it retains the additivity property and all the same moment formulas.

### Verification: Exp is Gamma(1, lambda)

Setting $\alpha = 1$ in the Gamma PDF:

$$
\frac{\lambda(\lambda x)^{1-1} e^{-\lambda x}}{\Gamma(1)} = \lambda e^{-\lambda x}
$$

since $\Gamma(1) = 1$ and $(\lambda x)^0 = 1$. This is exactly the $\text{Exp}(\lambda)$ PDF.

### Proof of the Additivity Property

For independent $X \sim \Gamma(\alpha, \lambda)$ and $Y \sim \Gamma(\beta, \lambda)$, the convolution integral gives:

$$
f_{X+Y}(z) = \int_0^z f_X(s) \, f_Y(z - s) \, ds
$$

Substituting the Gamma PDFs and factoring out terms independent of $s$:

$$
f_{X+Y}(z) = \frac{\lambda(\lambda z)^{\alpha + \beta - 1} e^{-\lambda z}}{\Gamma(\alpha)\Gamma(\beta)} \int_0^1 t^{\alpha-1}(1-t)^{\beta-1} \, dt
$$

after the substitution $t = s/z$. The integral is the **Beta function** $B(\alpha, \beta) = \Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha + \beta)$, giving

$$
f_{X+Y}(z) = \frac{\lambda(\lambda z)^{(\alpha + \beta) - 1} e^{-\lambda z}}{\Gamma(\alpha + \beta)}
$$

which is the PDF of $\Gamma(\alpha + \beta, \lambda)$.

**Alternative proof via MGFs.** Since $M_X(t) = (\lambda/(\lambda-t))^\alpha$ and $M_Y(t) = (\lambda/(\lambda-t))^\beta$, independence gives

$$
M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = \left(\frac{\lambda}{\lambda - t}\right)^{\alpha + \beta}
$$

which is the MGF of $\Gamma(\alpha + \beta, \lambda)$. By uniqueness of MGFs, $X + Y \sim \Gamma(\alpha + \beta, \lambda)$.

### Shape of the PDF

The shape parameter $\alpha$ controls the PDF's qualitative behavior:

- $\alpha < 1$: PDF is unbounded at $x = 0$ (diverges as $x^{\alpha-1}$), then decreasing
- $\alpha = 1$: purely decreasing (Exponential)
- $\alpha > 1$: rises from zero, peaks at the mode $({\alpha - 1})/{\lambda}$, then decays
- Large $\alpha$: increasingly bell-shaped and symmetric (by the CLT)

### Related Distributions

| Distribution | Gamma Form | Description |
|:---:|:---:|:---|
| $\text{Exp}(\lambda)$ | $\Gamma(1, \lambda)$ | Time to 1st arrival |
| $\text{Erlang}(k, \lambda)$ | $\Gamma(k, \lambda)$ | Time to $k$-th arrival (integer $k$) |
| $\chi^2_1$ | $\Gamma(1/2, 1/2)$ | Square of a standard normal |
| $\chi^2_d$ | $\Gamma(d/2, 1/2)$ | Sum of $d$ squared standard normals |

## Examples

**Example 1.** Let $X \sim \Gamma(3, 2)$. Find $E[X]$, $\text{Var}(X)$, and $P(X \leq 2)$.

$E[X] = 3/2 = 1.5$, $\text{Var}(X) = 3/4 = 0.75$.

For the CDF, since $\alpha = 3$ is an integer, we can use the Poisson formula: $P(X \leq 2) = P(N \geq 3)$ where $N \sim \text{Po}(2 \times 2) = \text{Po}(4)$.

$$
P(X \leq 2) = 1 - \sum_{j=0}^{2} \frac{4^j}{j!} e^{-4} = 1 - e^{-4}(1 + 4 + 8) = 1 - 13e^{-4} \approx 0.7619
$$

**Example 2.** Verify the additivity property and the sum-of-Exponentials construction.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 200_000
lam = 2.0

# --- Verify Gamma(3,2) moments and CDF ---
alpha = 3
X = np.random.gamma(shape=alpha, scale=1/lam, size=n_sim)

cdf_theory = 1 - 13 * np.exp(-4)
cdf_sim = np.mean(X <= 2)
cdf_scipy = stats.gamma.cdf(2, a=alpha, scale=1/lam)

print("=== Gamma(3, 2) ===")
print(f"E[X]:    sim={np.mean(X):.4f}, theory={alpha/lam:.4f}")
print(f"Var(X):  sim={np.var(X):.4f}, theory={alpha/lam**2:.4f}")
print(f"P(X<=2): sim={cdf_sim:.4f}, formula={cdf_theory:.4f}, "
      f"scipy={cdf_scipy:.4f}")

# --- Additivity: Gamma(2,2) + Gamma(3,2) = Gamma(5,2) ---
X1 = np.random.gamma(shape=2, scale=1/lam, size=n_sim)
X2 = np.random.gamma(shape=3, scale=1/lam, size=n_sim)
S = X1 + X2

print(f"\n=== Additivity: Gamma(2,2) + Gamma(3,2) = Gamma(5,2) ===")
print(f"E[S]:   sim={np.mean(S):.4f}, theory={5/lam:.4f}")
print(f"Var(S): sim={np.var(S):.4f}, theory={5/lam**2:.4f}")

# --- Sum of n Exp(lam) = Gamma(n, lam) ---
print(f"\n=== Sum of n iid Exp({lam}) ===")
for n in [2, 3, 5, 10]:
    exp_sums = np.random.exponential(1/lam, size=(n_sim, n)).sum(axis=1)
    print(f"n={n:2d}: mean={np.mean(exp_sums):.4f} (theory {n/lam:.4f}), "
          f"var={np.var(exp_sums):.4f} (theory {n/lam**2:.4f})")
```
