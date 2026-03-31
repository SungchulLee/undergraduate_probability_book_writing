# Why Chi-Squared, $t$, and $F$ Arise Naturally

## The Central Question

When working with a normal population $N(\mu, \sigma^2)$, inference requires knowing the **sampling distributions** of $\bar{X}$ and $S^2$. Three distributions emerge naturally from this setup.

## From Samples to Sampling Distributions

For $X_1, \ldots, X_n$ iid from $N(\mu, \sigma^2)$:

**When $\sigma$ is known**, the standardized sample mean is:

$$\frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)$$

This is straightforward — a linear combination of normals is normal.

**When $\sigma$ is unknown**, we must replace $\sigma$ with $S$:

$$\frac{\bar{X} - \mu}{S / \sqrt{n}} \sim \; ?$$

This is **not** normal, because $S$ is random and depends on the same data. To determine its distribution, we need to understand $S^2$, which leads to the chi-squared distribution.

## The Three Distributions and Their Roles

### Chi-Squared: Distribution of $S^2$

$$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$$

The chi-squared distribution captures the variability in the sample variance. It arises because the sum of squared deviations from the mean is a sum of squared normal quantities (with a rank reduction from estimating $\mu$ by $\bar{X}$).

### Student's $t$: When $\sigma$ Is Unknown

$$\frac{\bar{X} - \mu}{S/\sqrt{n}} = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \Big/ \sqrt{\frac{(n-1)S^2/\sigma^2}{n-1}} = \frac{N(0,1)}{\sqrt{\chi^2_{n-1}/(n-1)}} \sim t_{n-1}$$

The $t$ distribution arises as the ratio of a standard normal to the square root of an independent chi-squared divided by its degrees of freedom.

### $F$: Comparing Two Variances

$$\frac{S_1^2 / \sigma_1^2}{S_2^2 / \sigma_2^2} = \frac{\chi^2_{n_1 - 1} / (n_1 - 1)}{\chi^2_{n_2 - 1} / (n_2 - 1)} \sim F_{n_1 - 1, \, n_2 - 1}$$

The $F$ distribution arises when comparing variability from two independent normal samples.

## The Logical Chain

$$\boxed{N(\mu, \sigma^2)} \;\xrightarrow{\text{square}}\; \boxed{\chi^2} \;\xrightarrow{N/\sqrt{\chi^2/d}}\; \boxed{t} \;\xrightarrow{\chi^2/\chi^2}\; \boxed{F}$$

Each distribution builds on the previous one, all originating from the normal distribution.

## Prerequisite: How to Find PDFs

The derivations in this chapter rely on two techniques for finding the PDF of a transformed random variable.

### Method 1: CDF Method

Compute the CDF of $Y = g(X)$, then differentiate:

$$P(Y \leq y) = P(X \leq g^{-1}(y)) \quad \Rightarrow \quad f_Y(y) = \frac{d}{dy} F_Y(y)$$

### Method 2: Jacobian Method

For a one-to-one transformation $Y = g(X)$ with inverse $x = g^{-1}(y)$:

$$f_Y(y) = f_X(x) \left|\frac{dx}{dy}\right|$$

For multivariate transformations $(X_1, \ldots, X_n) \to (Y_1, \ldots, Y_n)$:

$$f_{Y_1, \ldots, Y_n}(y_1, \ldots, y_n) = f_{X_1, \ldots, X_n}(x_1, \ldots, x_n) \left|\frac{\partial(x_1, \ldots, x_n)}{\partial(y_1, \ldots, y_n)}\right|$$

where the Jacobian determinant satisfies:

$$\left|\frac{\partial(x_1, \ldots, x_n)}{\partial(y_1, \ldots, y_n)}\right| = \frac{1}{\left|\frac{\partial(y_1, \ldots, y_n)}{\partial(x_1, \ldots, x_n)}\right|}$$

### Example: PDF of $Y = X^3$ Where $X \sim U(0,1)$

**CDF method.** For $0 < y < 1$:

$$P(Y \leq y) = P(X^3 \leq y) = P(X \leq y^{1/3}) = y^{1/3}$$

$$\Rightarrow \quad f_Y(y) = \frac{1}{3} y^{-2/3} \quad \text{for } 0 < y < 1$$

**Jacobian method.** With $y = x^3$:

$$\frac{dy}{dx} = 3x^2 = 3y^{2/3} \quad \Rightarrow \quad \left|\frac{dx}{dy}\right| = \frac{1}{3} y^{-2/3}$$

$$f_Y(y) = f_X(x) \left|\frac{dx}{dy}\right| = 1 \cdot \frac{1}{3} y^{-2/3} = \frac{1}{3} y^{-2/3} \quad \text{for } 0 < y < 1$$
