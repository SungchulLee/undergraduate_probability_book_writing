# Chi-Squared Distribution

The Chi-squared distribution is a special case of the Gamma distribution that arises from squaring standard normal random variables -- it plays a central role in statistical inference.

## Definition

The **Chi-squared distribution** with $d$ degrees of freedom is

$$
\chi^2_d \stackrel{d}{=} \Gamma\!\left(\frac{d}{2}, \frac{1}{2}\right)
$$

If $Z_1, Z_2, \ldots, Z_d$ are iid $N(0, 1)$, then

$$
Z_1^2 + Z_2^2 + \cdots + Z_d^2 \sim \chi^2_d
$$

**PDF:**

$$
f(x) = \frac{(1/2)(x/2)^{d/2 - 1} e^{-x/2}}{\Gamma(d/2)}, \quad x > 0
$$

**Moments:**

$$
E[\chi^2_d] = d, \qquad \text{Var}(\chi^2_d) = 2d
$$

**Additivity.** If $W_1 \sim \chi^2_{d_1}$ and $W_2 \sim \chi^2_{d_2}$ are independent, then $W_1 + W_2 \sim \chi^2_{d_1 + d_2}$.

## Explanation

### Deriving Chi-squared(1) from the Standard Normal

If $Z \sim N(0, 1)$, then $X = Z^2 \sim \chi^2_1 = \Gamma(1/2, 1/2)$.

**Proof via the CDF method.** For $x > 0$:

$$
P(X \leq x) = P(Z^2 \leq x) = P(-\sqrt{x} \leq Z \leq \sqrt{x}) = 2\Phi(\sqrt{x}) - 1
$$

Differentiating with respect to $x$:

$$
f_X(x) = 2\phi(\sqrt{x}) \cdot \frac{1}{2\sqrt{x}} = \frac{1}{\sqrt{2\pi}} x^{-1/2} e^{-x/2}
$$

Rewriting in Gamma form:

$$
f_X(x) = \frac{(1/2)(x/2)^{1/2 - 1} e^{-x/2}}{\Gamma(1/2)}
$$

since $\Gamma(1/2) = \sqrt{\pi}$. This is the PDF of $\Gamma(1/2, 1/2)$, confirming $Z^2 \sim \chi^2_1 = \Gamma(1/2, 1/2)$.

### Sum of Squared Normals via Gamma Additivity

Since each $Z_i^2 \sim \Gamma(1/2, 1/2)$ independently, the Gamma additivity property gives

$$
Z_1^2 + Z_2^2 + \cdots + Z_d^2 \sim \underbrace{\Gamma(1/2, 1/2) * \cdots * \Gamma(1/2, 1/2)}_{d \text{ terms}} = \Gamma\!\left(\frac{d}{2}, \frac{1}{2}\right) = \chi^2_d
$$

### Moments from the Gamma

Since $\chi^2_d = \Gamma(d/2, 1/2)$, the moments follow directly:

$$
E[\chi^2_d] = \frac{d/2}{1/2} = d
$$

$$
\text{Var}(\chi^2_d) = \frac{d/2}{(1/2)^2} = 2d
$$

The mean equals the degrees of freedom, and the variance is twice the degrees of freedom. As $d$ increases, the distribution becomes more concentrated relative to its mean: $\text{CV} = \sqrt{2/d}$.

### Additivity of Chi-Squared

Since Chi-squared distributions are Gamma distributions with the same rate $\lambda = 1/2$, the Gamma additivity property applies:

$$
\chi^2_{d_1} + \chi^2_{d_2} \sim \Gamma\!\left(\frac{d_1}{2} + \frac{d_2}{2}, \frac{1}{2}\right) = \chi^2_{d_1 + d_2}
$$

when the two Chi-squared random variables are independent.

### Shape of the PDF

The shape depends on the degrees of freedom:

- $d = 1$: unbounded at $x = 0$ (the $x^{-1/2}$ singularity from $\Gamma(1/2, 1/2)$), then sharply decreasing
- $d = 2$: $\chi^2_2 = \text{Exp}(1/2)$, a pure exponential decay
- $d \geq 3$: rises from zero, peaks at the mode $d - 2$, then decays
- Large $d$: approximately $N(d, 2d)$ by the Central Limit Theorem

### Summary of Special Cases

| Distribution | Gamma Parameters | Shape | Rate |
|:---:|:---:|:---:|:---:|
| $\text{Exp}(\lambda)$ | $\Gamma(1, \lambda)$ | $1$ | $\lambda$ |
| $\text{Erlang}(k, \lambda)$ | $\Gamma(k, \lambda)$ | $k$ (integer) | $\lambda$ |
| $\chi^2_1$ | $\Gamma(1/2, 1/2)$ | $1/2$ | $1/2$ |
| $\chi^2_d$ | $\Gamma(d/2, 1/2)$ | $d/2$ | $1/2$ |

## Examples

**Example 1.** If $Z_1, \ldots, Z_8$ are iid $N(0,1)$, find the distribution, mean, and variance of $W = Z_1^2 + \cdots + Z_8^2$.

$W \sim \chi^2_8 = \Gamma(4, 1/2)$. Then $E[W] = 8$ and $\text{Var}(W) = 16$.

**Example 2.** Show that $\chi^2_2 = \text{Exp}(1/2)$ and verify the Chi-squared distribution properties.

Setting $d = 2$: $\chi^2_2 = \Gamma(1, 1/2) = \text{Exp}(1/2)$, with PDF $f(x) = \frac{1}{2} e^{-x/2}$.

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 200_000

# --- Verify Z^2 ~ chi-squared(1) ---
Z = np.random.standard_normal(n_sim)
X = Z ** 2

print("=== Z^2 ~ chi-squared(1) ===")
print(f"E[Z^2]:   sim={np.mean(X):.4f}, theory=1.0000")
print(f"Var[Z^2]: sim={np.var(X):.4f}, theory=2.0000")

# --- Verify sum of squared normals ---
print("\n=== Sum of d squared N(0,1) ===")
for d in [1, 2, 5, 8, 20]:
    Z_mat = np.random.standard_normal((n_sim, d))
    W = np.sum(Z_mat**2, axis=1)
    print(f"d={d:2d}: E[W]={np.mean(W):.4f} (theory {d}), "
          f"Var[W]={np.var(W):.4f} (theory {2*d})")

# --- Verify chi-squared(2) = Exp(1/2) ---
chi2_samples = np.random.chisquare(2, n_sim)
exp_samples = np.random.exponential(2, n_sim)  # scale = 1/(1/2) = 2

print(f"\n=== chi-squared(2) vs Exp(1/2) ===")
print(f"chi2(2) mean: {np.mean(chi2_samples):.4f}, "
      f"Exp(1/2) mean: {np.mean(exp_samples):.4f}, theory: 2.0")

# --- Verify additivity ---
print(f"\n=== Additivity ===")
for d1, d2 in [(3, 5), (2, 8), (1, 1)]:
    W1 = np.random.chisquare(d1, n_sim)
    W2 = np.random.chisquare(d2, n_sim)
    S = W1 + W2
    print(f"chi2({d1}) + chi2({d2}): "
          f"mean={np.mean(S):.4f} (theory {d1+d2}), "
          f"var={np.var(S):.4f} (theory {2*(d1+d2)})")
```
