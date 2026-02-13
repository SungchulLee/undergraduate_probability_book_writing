# Chi-Squared Distribution: Properties, Mean, and Variance

## MGF of the Chi-Squared Distribution

Since $\chi^2_d \sim \Gamma(d/2, 1/2)$, we can compute the MGF directly. With the substitution $\lambda = 1/2 - t$:

$$\varphi_{\chi^2_d}(t) = E[e^{tX}] = \int_0^{\infty} e^{tx} \frac{(1/2)^{d/2}}{\Gamma(d/2)} x^{d/2 - 1} e^{-x/2}\, dx$$

$$= \int_0^{\infty} \frac{(1/2)^{d/2}}{\Gamma(d/2)} x^{d/2 - 1} e^{-(1/2 - t)x}\, dx$$

$$= \left(\frac{1}{\sqrt{1 - 2t}}\right)^d \int_0^{\infty} \underbrace{\frac{\lambda (\lambda x)^{d/2 - 1} e^{-\lambda x}}{\Gamma(d/2)}}_{\text{PDF of } \Gamma(d/2, \lambda)}\, dx = \left(\frac{1}{\sqrt{1 - 2t}}\right)^d$$

Therefore:

$$\varphi_{\chi^2_d}(t) = (1 - 2t)^{-d/2}, \quad t < \frac{1}{2}$$

## Mean and Variance

Since $\chi^2_d \sim \Gamma(d/2, 1/2)$, the mean and variance follow from the Gamma distribution:

| Distribution | Mean | Variance |
|-------------|------|----------|
| $\text{Geo}(p)$ | $1/p$ | $q/p^2$ |
| $\frac{1}{n}\text{Geo}(p)$ | $1/(np)$ | $q/(np)^2$ |
| $\text{Exp}(\lambda) = \Gamma(1, \lambda)$ | $1/\lambda$ | $1/\lambda^2$ |
| $\Gamma(n, \lambda)$ | $n/\lambda$ | $n/\lambda^2$ |
| $\Gamma(\alpha, \lambda)$ | $\alpha/\lambda$ | $\alpha/\lambda^2$ |
| $\chi^2_1 = \Gamma(1/2, 1/2)$ | $\frac{1/2}{1/2} = 1$ | $\frac{1/2}{(1/2)^2} = 2$ |
| $\chi^2_d = \Gamma(d/2, 1/2)$ | $d$ | $2d$ |

### Direct Verification

**Mean:** Each $Z_i^2$ has $E[Z_i^2] = \text{Var}(Z_i) + (E[Z_i])^2 = 1 + 0 = 1$. By linearity:

$$E[\chi^2_d] = \sum_{i=1}^d E[Z_i^2] = d$$

**Variance:** Each $Z_i^2$ has $\text{Var}(Z_i^2) = E[Z_i^4] - (E[Z_i^2])^2 = 3 - 1 = 2$ (since $E[Z^4] = 3$ for standard normal). By independence:

$$\text{Var}(\chi^2_d) = \sum_{i=1}^d \text{Var}(Z_i^2) = 2d$$

## Summary of Properties

| Property | Value |
|----------|-------|
| PDF | $\frac{(1/2)^{d/2}}{\Gamma(d/2)} x^{d/2-1} e^{-x/2}$ for $x > 0$ |
| MGF | $(1 - 2t)^{-d/2}$ for $t < 1/2$ |
| Mean | $d$ |
| Variance | $2d$ |
| Mode | $\max(d - 2, \, 0)$ |
| Skewness | $\sqrt{8/d}$ |

!!! note "Shape of the Chi-Squared Distribution"
    For small $d$, the distribution is heavily right-skewed. As $d$ increases, the skewness decreases (proportional to $1/\sqrt{d}$) and the distribution approaches a normal distribution by the CLT, since $\chi^2_d$ is a sum of $d$ iid random variables.
