# Log-Normal Distribution Properties


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Mean and Variance

!!! info "Moments of Log-Normal"
    If $X \sim \text{LogNormal}(\mu, \sigma^2)$, i.e., $\ln X \sim N(\mu, \sigma^2)$, then:

    $$E[X] = e^{\mu + \sigma^2/2}$$

    $$\text{Var}(X) = e^{2\mu + \sigma^2}\left(e^{\sigma^2} - 1\right)$$

**Derivation of the mean.** Since $X = e^Y$ where $Y \sim N(\mu, \sigma^2)$:

$$E[X] = E[e^Y] = M_Y(1)$$

where $M_Y(t) = e^{\mu t + \sigma^2 t^2/2}$ is the MGF of the Normal. Setting $t = 1$:

$$E[X] = e^{\mu + \sigma^2/2}$$

**Derivation of $E[X^2]$.** Similarly $E[X^2] = E[e^{2Y}] = M_Y(2) = e^{2\mu + 2\sigma^2}$, so:

$$\text{Var}(X) = e^{2\mu + 2\sigma^2} - e^{2\mu + \sigma^2} = e^{2\mu + \sigma^2}(e^{\sigma^2} - 1)$$

**General raw moments:**

$$E[X^k] = e^{k\mu + k^2\sigma^2/2}$$

## Median and Mode

!!! info "Median and Mode"

    $$\text{Median}(X) = e^{\mu}$$

    $$\text{Mode}(X) = e^{\mu - \sigma^2}$$

The median follows because $P(X \leq e^\mu) = P(Y \leq \mu) = 0.5$ where $Y = \ln X \sim N(\mu, \sigma^2)$.

The mode is obtained by differentiating the PDF and setting $f'(x) = 0$:

$$f(x) = \frac{1}{x\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(\ln x - \mu)^2}{2\sigma^2}\right)$$

The ordering $\text{Mode} < \text{Median} < \text{Mean}$ always holds (for $\sigma > 0$), reflecting the **right-skewness** of the log-normal distribution.

## Skewness and Kurtosis

$$\gamma_1 = (e^{\sigma^2} + 2)\sqrt{e^{\sigma^2} - 1}$$

$$\gamma_2 = e^{4\sigma^2} + 2e^{3\sigma^2} + 3e^{2\sigma^2} - 6$$

Both are always positive and depend only on $\sigma^2$, not on $\mu$. The log-normal is **always right-skewed** and **always leptokurtic** (heavy-tailed).

## Multiplicative Properties

The log-normal family is closed under **multiplication** (not addition).

!!! info "Products of Log-Normals"
    If $X_i \sim \text{LogNormal}(\mu_i, \sigma_i^2)$ are **independent**, then:

    $$\prod_{i=1}^{n} X_i \sim \text{LogNormal}\!\left(\sum_{i=1}^{n} \mu_i,\; \sum_{i=1}^{n} \sigma_i^2\right)$$

**Proof.** $\ln\!\left(\prod X_i\right) = \sum \ln X_i = \sum Y_i$ where $Y_i \sim N(\mu_i, \sigma_i^2)$ are independent. A sum of independent normals is normal. $\square$

Similarly, for a constant power $c$:

$$X^c \sim \text{LogNormal}(c\mu, c^2\sigma^2)$$

since $\ln(X^c) = c \ln X = cY \sim N(c\mu, c^2\sigma^2)$.

## Relationship to the Normal Distribution

| Property | Normal | Log-Normal |
|:---|:---:|:---:|
| Support | $(-\infty, \infty)$ | $(0, \infty)$ |
| Closed under | addition | multiplication |
| Skewness | 0 | always positive |
| Symmetry | symmetric | right-skewed |
| MGF exists? | yes | no (all moments exist, but MGF is infinite) |

!!! warning "No MGF"
    The log-normal distribution has **no moment generating function**. Specifically, $E[e^{tX}] = \infty$ for all $t > 0$. This is because the tails of the log-normal are "too heavy" for the exponential moment to converge. However, all raw moments $E[X^k]$ exist and are finite.

## CDF and Quantiles

The CDF of $X \sim \text{LogNormal}(\mu, \sigma^2)$ is:

$$F(x) = P(X \leq x) = P(Y \leq \ln x) = \Phi\!\left(\frac{\ln x - \mu}{\sigma}\right), \quad x > 0$$

The $p$-th quantile is:

$$Q(p) = \exp\!\left(\mu + \sigma\,\Phi^{-1}(p)\right)$$

This makes Value-at-Risk (VaR) calculations straightforward when asset returns are modeled as log-normal.

## Applications in Finance

The log-normal distribution is fundamental in quantitative finance:

**1. Geometric Brownian Motion.** If a stock price follows $dS = \mu S\,dt + \sigma S\,dW_t$, then:

$$S_T = S_0 \exp\!\left[\left(\mu - \frac{\sigma^2}{2}\right)T + \sigma W_T\right]$$

so $S_T \sim \text{LogNormal}$ with parameters $\ln S_0 + (\mu - \sigma^2/2)T$ and $\sigma^2 T$.

**2. Black-Scholes Model.** The Black-Scholes option pricing formula assumes log-normal stock prices.

**3. Portfolio Returns.** If single-period log-returns are $r_t \sim N(\mu, \sigma^2)$, then the cumulative gross return $\prod(1 + R_t) = e^{\sum r_t}$ is log-normal.

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# --- Panel 1: Shape analysis ---
x = np.linspace(0.001, 8, 500)
params = [(0, 0.25), (0, 0.5), (0, 1.0), (1, 0.5)]
colors = ['blue', 'red', 'green', 'purple']

for (mu, sigma), color in zip(params, colors):
    pdf = stats.lognorm.pdf(x, s=sigma, scale=np.exp(mu))
    axes[0].plot(x, pdf, color=color, lw=2,
                 label=f'μ={mu}, σ={sigma}')
    # Mark mean, median, mode
    mean = np.exp(mu + sigma**2 / 2)
    median = np.exp(mu)
    mode = np.exp(mu - sigma**2)
    axes[0].axvline(median, color=color, ls=':', alpha=0.4)

axes[0].set_title('Log-Normal PDF')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].set_ylim(0, 2.5)
axes[0].legend(fontsize=9)
axes[0].grid(True, alpha=0.3)

# --- Panel 2: Mean, Median, Mode relationship ---
sigma_range = np.linspace(0.1, 2, 100)
mu_val = 0

means = np.exp(mu_val + sigma_range**2 / 2)
medians = np.exp(mu_val) * np.ones_like(sigma_range)
modes = np.exp(mu_val - sigma_range**2)

axes[1].plot(sigma_range, means, 'r-', lw=2, label='Mean')
axes[1].plot(sigma_range, medians, 'b-', lw=2, label='Median')
axes[1].plot(sigma_range, modes, 'g-', lw=2, label='Mode')
axes[1].set_title('Mode < Median < Mean (μ=0)')
axes[1].set_xlabel('σ')
axes[1].set_ylabel('Value')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# --- Panel 3: Multiplicative closure ---
np.random.seed(42)
n_sim = 100000
mu1, sigma1 = 0.5, 0.3
mu2, sigma2 = 1.0, 0.4

X1 = np.random.lognormal(mu1, sigma1, n_sim)
X2 = np.random.lognormal(mu2, sigma2, n_sim)
product = X1 * X2

mu_prod = mu1 + mu2
sigma_prod = np.sqrt(sigma1**2 + sigma2**2)

x_plot = np.linspace(0.01, 30, 500)
axes[2].hist(product, bins=100, density=True, alpha=0.5,
             color='steelblue', label='X₁·X₂ simulated')
axes[2].plot(x_plot, stats.lognorm.pdf(x_plot, s=sigma_prod, scale=np.exp(mu_prod)),
             'r-', lw=2, label=f'LogN({mu_prod:.1f}, {sigma_prod:.2f}²)')
axes[2].set_title('Product of Independent Log-Normals')
axes[2].set_xlabel('x')
axes[2].set_xlim(0, 30)
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('lognormal_properties.png', dpi=150, bbox_inches='tight')
plt.show()
```
