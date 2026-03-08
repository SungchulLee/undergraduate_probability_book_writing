# Relationship to the Chi-Squared Distribution

## Chi-Squared as a Special Case of Gamma

!!! info "Chi-Squared–Gamma Connection"
    The **Chi-squared distribution** with $d$ degrees of freedom is a special case of the Gamma distribution:

    $$\chi^2_d \stackrel{d}{=} \Gamma\!\left(\frac{d}{2}, \frac{1}{2}\right)$$

    In particular:

    $$\chi^2_1 \stackrel{d}{=} \Gamma\!\left(\frac{1}{2}, \frac{1}{2}\right)$$

## Derivation: Z^2 ~ Chi-squared(1)

If $Z \sim N(0, 1)$, then $X = Z^2 \sim \chi^2_1 = \Gamma(1/2, 1/2)$.

Using the CDF method: for $x > 0$,

$$P(X \leq x) = P(Z^2 \leq x) = P(-\sqrt{x} \leq Z \leq \sqrt{x}) = 2\Phi(\sqrt{x}) - 1$$

Differentiating:

$$f_X(x) = 2\phi(\sqrt{x}) \cdot \frac{1}{2\sqrt{x}} = \frac{1}{\sqrt{2\pi}} x^{-1/2} e^{-x/2}$$

This can be rewritten as:

$$f_X(x) = \frac{(x/2)^{1/2 - 1} e^{-x/2}}{2 \, \Gamma(1/2)} \cdot \frac{1}{1} = \frac{\frac{1}{2}\left(\frac{1}{2}x\right)^{1/2-1} e^{-x/2}}{\Gamma(1/2)}$$

which is the PDF of $\Gamma(1/2, 1/2)$, confirming $\chi^2_1 = \Gamma(1/2, 1/2)$.

## Sum of Squared Normals

If $Z_1, Z_2, \ldots, Z_d$ are iid $N(0,1)$, then by the additivity of the Gamma distribution:

$$Z_1^2 + Z_2^2 + \cdots + Z_d^2 \sim \Gamma\!\left(\frac{1}{2}, \frac{1}{2}\right) * \cdots * \Gamma\!\left(\frac{1}{2}, \frac{1}{2}\right) = \Gamma\!\left(\frac{d}{2}, \frac{1}{2}\right) = \chi^2_d$$

## Moments from the Gamma

Since $\chi^2_d = \Gamma(d/2, 1/2)$, the moments follow directly from the Gamma formulas:

$$E[\chi^2_d] = \frac{d/2}{1/2} = d$$

$$\text{Var}(\chi^2_d) = \frac{d/2}{(1/2)^2} = 2d$$

## Additivity of Chi-Squared

Since the Chi-squared is a Gamma with rate $\lambda = 1/2$, the Gamma additivity property gives:

$$\chi^2_{d_1} + \chi^2_{d_2} \sim \chi^2_{d_1 + d_2}$$

when the two Chi-squared random variables are independent.

## Summary of Special Cases

| Distribution | Gamma Parameters | Shape $\alpha$ | Rate $\lambda$ |
|:---:|:---:|:---:|:---:|
| $\text{Exp}(\lambda)$ | $\Gamma(1, \lambda)$ | $1$ | $\lambda$ |
| Erlang$(k, \lambda)$ | $\Gamma(k, \lambda)$ | $k$ (integer) | $\lambda$ |
| $\chi^2_1$ | $\Gamma(1/2, 1/2)$ | $1/2$ | $1/2$ |
| $\chi^2_d$ | $\Gamma(d/2, 1/2)$ | $d/2$ | $1/2$ |

## Inverse Gamma Distribution

The **Inverse Gamma distribution** $\text{IG}(\alpha, \lambda)$ is the distribution of $1/X$ when $X \sim \Gamma(\alpha, \lambda)$. It arises as a conjugate prior in Bayesian statistics for variance parameters.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Verify chi-squared = Gamma(d/2, 1/2)
x = np.linspace(0, 20, 300)
for d in [1, 2, 5, 10]:
    chi2_pdf = stats.chi2.pdf(x, df=d)
    gamma_pdf = stats.gamma.pdf(x, a=d/2, scale=2)  # scale = 1/rate = 2
    axes[0].plot(x, chi2_pdf, '-', lw=2, label=f'χ²({d})')
    axes[0].plot(x, gamma_pdf, '--', lw=1, alpha=0.7)

axes[0].set_title('χ² PDFs (solid) vs Γ(d/2, 1/2) (dashed)')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)
axes[0].set_ylim(0, 0.5)

# Demonstrate Z^2 ~ χ²_1
Z = np.random.standard_normal(n_sim)
X = Z ** 2

axes[1].hist(X, bins=100, density=True, alpha=0.5, range=(0, 8),
             color='blue', label='Z² (simulated)')
x_theory = np.linspace(0.01, 8, 300)
pdf_theory = stats.chi2.pdf(x_theory, df=1)
axes[1].plot(x_theory, pdf_theory, 'r-', lw=2, label='χ²(1) PDF')
axes[1].set_title('Z² ~ χ²(1) = Γ(1/2, 1/2)')
axes[1].set_xlabel('x')
axes[1].set_ylim(0, 2)
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('chi_squared_gamma.png', dpi=150, bbox_inches='tight')
plt.show()

# Verify additivity
print("=== Chi-Squared Additivity ===")
for d1, d2 in [(3, 5), (2, 8), (1, 1)]:
    X1 = np.random.chisquare(d1, n_sim)
    X2 = np.random.chisquare(d2, n_sim)
    S = X1 + X2
    print(f"χ²({d1}) + χ²({d2}): mean={np.mean(S):.3f} "
          f"(theory {d1+d2}), var={np.var(S):.3f} (theory {2*(d1+d2)})")
```
