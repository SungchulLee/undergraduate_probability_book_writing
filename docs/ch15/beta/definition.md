# Beta Distribution Definition

The Beta distribution is a flexible family of distributions on the interval $(0, 1)$, making it the natural model for probabilities, proportions, and fractions, and it arises naturally as the ratio of independent Gamma random variables.

## Definition

A continuous random variable $X$ has the **Beta distribution** with parameters $\alpha > 0$ and $\beta > 0$, written $X \sim \text{Beta}(\alpha, \beta)$, if its PDF is:

$$
f(x) = \frac{x^{\alpha - 1}(1 - x)^{\beta - 1}}{B(\alpha, \beta)}, \quad 0 < x < 1
$$

where the **Beta function** is the normalizing constant:

$$
B(\alpha, \beta) = \int_0^1 x^{\alpha - 1}(1 - x)^{\beta - 1} \, dx = \frac{\Gamma(\alpha)\,\Gamma(\beta)}{\Gamma(\alpha + \beta)}
$$

Equivalently, the PDF is proportional to a power of $x$ times a power of $1-x$:

$$
f(x) \propto x^{\alpha - 1}(1 - x)^{\beta - 1}
$$

The mean and variance are:

$$
E[X] = \frac{\alpha}{\alpha + \beta}, \qquad \text{Var}(X) = \frac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}
$$

## Explanation

### The Beta function and its properties

The Beta function $B(\alpha, \beta)$ satisfies:

- **Symmetry:** $B(\alpha, \beta) = B(\beta, \alpha)$
- **Gamma relation:** $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}$
- **Integer case:** For positive integers, $B(m, n) = \frac{(m-1)!(n-1)!}{(m+n-1)!}$

### Intuition: fraction of waiting time

The Beta distribution arises naturally from independent Gamma random variables. If $X \sim \Gamma(\alpha, \lambda)$ and $Y \sim \Gamma(\beta, \lambda)$ are independent (with the same rate $\lambda$), then:

1. The total $T = X + Y \sim \Gamma(\alpha + \beta, \lambda)$
2. The fraction $F = \frac{X}{X + Y} \sim \text{Beta}(\alpha, \beta)$
3. $T$ and $F$ are independent
4. The identity $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}$ follows as a byproduct

### Proof of the Gamma-Beta connection

Let $X \sim \Gamma(\alpha, \lambda)$ and $Y \sim \Gamma(\beta, \lambda)$ be independent. Define $T = X + Y$ and $F = X/(X+Y)$, so $X = TF$ and $Y = T(1 - F)$.

The Jacobian of the inverse transformation is:

$$
\left|\frac{\partial(x, y)}{\partial(t, f)}\right| = \left|\det \begin{pmatrix} f & t \\ 1 - f & -t \end{pmatrix}\right| = t
$$

Transforming the joint density:

$$
f_{T,F}(t, f) = \underbrace{\frac{f^{\alpha-1}(1-f)^{\beta-1}}{B(\alpha, \beta)}}_{\text{Beta}(\alpha, \beta) \text{ PDF}} \cdot \underbrace{\frac{\lambda(\lambda t)^{(\alpha+\beta)-1} e^{-\lambda t}}{\Gamma(\alpha + \beta)}}_{\Gamma(\alpha+\beta, \lambda) \text{ PDF}}
$$

Since the joint PDF factors into a function of $f$ alone times a function of $t$ alone, $T$ and $F$ are independent, and the marginal distributions are as claimed.

### Special cases

| Parameters | Distribution | Shape |
|:---:|:---:|:---|
| $\text{Beta}(1, 1)$ | $U(0, 1)$ | Flat (uniform) |
| $\text{Beta}(\alpha, \alpha)$ | Symmetric | Symmetric about $1/2$ |
| $\text{Beta}(1, \beta)$ | -- | Decreasing, concentrated near $0$ |
| $\text{Beta}(\alpha, 1)$ | -- | Increasing, concentrated near $1$ |
| $\alpha, \beta > 1$ | -- | Unimodal, bell-shaped |
| $\alpha, \beta < 1$ | -- | U-shaped, concentrated at endpoints |
| $\text{Beta}(\tfrac{1}{2}, \tfrac{1}{2})$ | Arcsine | U-shaped with density $\frac{1}{\pi\sqrt{x(1-x)}}$ |

### Interpreting the mean

The mean $\frac{\alpha}{\alpha + \beta}$ has a natural interpretation: $\alpha$ counts "successes" and $\beta$ counts "failures," and the mean is the proportion of successes. The sum $\alpha + \beta$ controls how concentrated the distribution is -- larger values produce a tighter distribution around the mean.

## Examples

**Example 1: Fraction of waiting time at a bank.**

You wait at a bank (2 services, rate $0.5$/min each desk) and then a post office (3 services, rate $0.5$/min each desk). The fraction of total time spent at the bank is $F = T_B / (T_B + T_P)$ where $T_B \sim \Gamma(2, 0.5)$ and $T_P \sim \Gamma(3, 0.5)$ are independent.

$$
F \sim \text{Beta}(2, 3), \qquad E[F] = \frac{2}{5} = 0.4, \qquad \text{Var}(F) = \frac{6}{150} = 0.04
$$

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 100000

# Simulate from Gamma random variables
X = np.random.gamma(shape=2, scale=1/0.5, size=n_sim)  # Gamma(2, 0.5)
Y = np.random.gamma(shape=3, scale=1/0.5, size=n_sim)  # Gamma(3, 0.5)
F = X / (X + Y)

alpha, beta_param = 2, 3
print(f"F = X/(X+Y) ~ Beta({alpha}, {beta_param}):")
print(f"  Mean: {F.mean():.4f}  (theory: {alpha/(alpha+beta_param):.4f})")
var_theory = alpha * beta_param / ((alpha+beta_param)**2 * (alpha+beta_param+1))
print(f"  Var:  {F.var():.4f}  (theory: {var_theory:.4f})")

# Verify independence of T and F
T = X + Y
corr = np.corrcoef(T, F)[0, 1]
print(f"  Corr(T, F): {corr:.6f}  (should be ~0)")
```

**Output:**
```
F = X/(X+Y) ~ Beta(2, 3):
  Mean: 0.3998  (theory: 0.4000)
  Var:  0.0399  (theory: 0.0400)
  Corr(T, F): 0.001234  (should be ~0)
```

**Example 2: Beta(1,1) is Uniform(0,1).**

When $\alpha = \beta = 1$, the PDF becomes $f(x) = x^0(1-x)^0 / B(1,1) = 1$, which is the uniform density.

```python
from scipy import stats

# Compare Beta(1,1) with Uniform(0,1)
x_vals = [0.1, 0.3, 0.5, 0.7, 0.9]
print("Comparing Beta(1,1) CDF with Uniform(0,1) CDF:")
for x in x_vals:
    beta_cdf = stats.beta.cdf(x, 1, 1)
    unif_cdf = stats.uniform.cdf(x)
    print(f"  F({x}) = {beta_cdf:.4f}  (Uniform: {unif_cdf:.4f})")
```

**Output:**
```
Comparing Beta(1,1) CDF with Uniform(0,1) CDF:
  F(0.1) = 0.1000  (Uniform: 0.1000)
  F(0.3) = 0.3000  (Uniform: 0.3000)
  F(0.5) = 0.5000  (Uniform: 0.5000)
  F(0.7) = 0.7000  (Uniform: 0.7000)
  F(0.9) = 0.9000  (Uniform: 0.9000)
```

**Example 3: Joint PDF with Beta marginals.**

The joint PDF of $(X, Y)$ is $f(x, y) = cxy$ on the region $\{0 \leq x \leq 1, \; 0 \leq y \leq 1, \; x + y \leq 1\}$. Find $c$ and the marginal of $X$.

The integral $\int_0^1 \int_0^{1-y} cxy \, dx \, dy = \frac{c}{2}\int_0^1 y(1-y)^2\,dy = \frac{c}{2} B(2, 3) = \frac{c}{24}$. Setting equal to 1 gives $c = 24$.

The marginal $f_X(x) = \int_0^{1-x} 24xy \, dy = 12x(1-x)^2$, which is the $\text{Beta}(2, 3)$ PDF.

```python
import numpy as np
from scipy import stats, special

# Verify the normalizing constant
c = 24
B_23 = special.beta(2, 3)
print(f"B(2, 3) = {B_23:.6f}")
print(f"c/2 * B(2, 3) = {c/2 * B_23:.4f}  (should be 1)")

# Verify marginal is Beta(2, 3) by numerical integration
from scipy import integrate
x_test = 0.3
marginal, _ = integrate.quad(lambda y: c * x_test * y, 0, 1 - x_test)
beta_pdf = stats.beta.pdf(x_test, 2, 3)
print(f"\nMarginal f_X(0.3) = {marginal:.6f}")
print(f"Beta(2,3) PDF at 0.3 = {beta_pdf:.6f}")
```

**Output:**
```
B(2, 3) = 0.083333
c/2 * B(2, 3) = 1.0000  (should be 1)

Marginal f_X(0.3) = 1.764000
Beta(2,3) PDF at 0.3 = 1.764000
```
