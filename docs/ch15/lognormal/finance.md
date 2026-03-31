# Log-Normal Distribution in Finance

## Stock Price Modeling

Under the **geometric Brownian motion** (GBM) model, a stock price $S_t$ satisfies:

$$dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$$

where $\mu$ is the drift rate, $\sigma$ is the volatility, and $W_t$ is a standard Brownian motion. The solution is:

$$S_T = S_0 \exp\!\left[\left(\mu - \frac{\sigma^2}{2}\right)T + \sigma W_T\right]$$

Since $W_T \sim N(0, T)$, we have $\ln S_T \sim N\!\left(\ln S_0 + (\mu - \frac{\sigma^2}{2})T,\; \sigma^2 T\right)$, so $S_T$ is **log-normally distributed**.

!!! info "GBM Distribution"
    $$S_T \sim \text{LogNormal}\!\left(\ln S_0 + \left(\mu - \frac{\sigma^2}{2}\right)T,\;\; \sigma^2 T\right)$$

    $$E[S_T] = S_0 e^{\mu T}, \qquad \text{Var}(S_T) = S_0^2 e^{2\mu T}\left(e^{\sigma^2 T} - 1\right)$$

## Log Returns vs Simple Returns

Let $R_t = \frac{S_t - S_{t-1}}{S_{t-1}}$ be the simple return and $r_t = \ln\frac{S_t}{S_{t-1}} = \ln(1 + R_t)$ be the log return.

Under GBM with daily increments:

$$r_t \sim N\!\left(\left(\mu - \frac{\sigma^2}{2}\right)\Delta t,\;\; \sigma^2 \Delta t\right)$$

**Multi-period compounding.** Over $n$ periods:

$$\frac{S_n}{S_0} = \prod_{t=1}^{n}(1 + R_t) = \exp\!\left(\sum_{t=1}^{n} r_t\right)$$

Since log returns are iid normal, $\sum r_t$ is normal, and $S_n / S_0$ is log-normal.

## Value at Risk (VaR)

Under the log-normal model, the $\alpha$-level VaR for a long position is the loss exceeded with probability $\alpha$:

$$\text{VaR}_\alpha = S_0 - S_0 \exp\!\left(\left(\mu - \frac{\sigma^2}{2}\right)T + \sigma\sqrt{T}\,\Phi^{-1}(\alpha)\right)$$

For small $T$ and $\mu \approx 0$, this simplifies to:

$$\text{VaR}_\alpha \approx -S_0\,\sigma\sqrt{T}\,\Phi^{-1}(\alpha)$$

## Conditional Value at Risk (CVaR)

The **CVaR** (Expected Shortfall) at level $\alpha$ is:

$$\text{CVaR}_\alpha = E\left[-R \mid R \leq -\text{VaR}_\alpha / S_0\right]$$

Under the log-normal model:

$$\text{CVaR}_\alpha = S_0\left(1 - \frac{e^{\mu T}}{\alpha}\,\Phi\!\left(\Phi^{-1}(\alpha) - \sigma\sqrt{T}\right)\right)$$

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

np.random.seed(42)

# --- Parameters ---
S0, mu, sigma, T = 100, 0.08, 0.25, 1.0
n_paths, n_steps = 50, 252

# --- Panel 1: GBM sample paths ---
dt = T / n_steps
t = np.linspace(0, T, n_steps + 1)

for _ in range(n_paths):
    dW = np.random.normal(0, np.sqrt(dt), n_steps)
    log_returns = (mu - 0.5 * sigma**2) * dt + sigma * dW
    S = S0 * np.exp(np.cumsum(np.concatenate([[0], log_returns])))
    axes[0, 0].plot(t, S, alpha=0.3, lw=0.8)

E_ST = S0 * np.exp(mu * t)
axes[0, 0].plot(t, E_ST, 'r-', lw=2, label=f'E[S(t)] = {S0}·exp({mu}t)')
axes[0, 0].set_title('GBM Sample Paths')
axes[0, 0].set_xlabel('Time (years)')
axes[0, 0].set_ylabel('Stock Price')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# --- Panel 2: Terminal distribution ---
n_sim = 100000
WT = np.random.normal(0, np.sqrt(T), n_sim)
ST = S0 * np.exp((mu - 0.5 * sigma**2) * T + sigma * WT)

x_plot = np.linspace(40, 250, 500)
mu_ln = np.log(S0) + (mu - 0.5 * sigma**2) * T
sigma_ln = sigma * np.sqrt(T)

axes[0, 1].hist(ST, bins=100, density=True, alpha=0.5, color='steelblue')
axes[0, 1].plot(x_plot, stats.lognorm.pdf(x_plot, s=sigma_ln, scale=np.exp(mu_ln)),
                'r-', lw=2, label='LogNormal PDF')

mean_ST = S0 * np.exp(mu * T)
median_ST = np.exp(mu_ln)
axes[0, 1].axvline(mean_ST, color='red', ls='--', label=f'Mean={mean_ST:.1f}')
axes[0, 1].axvline(median_ST, color='blue', ls='--', label=f'Median={median_ST:.1f}')
axes[0, 1].set_title(f'Terminal Distribution S({T})')
axes[0, 1].set_xlabel('Stock Price')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# --- Panel 3: VaR and CVaR visualization ---
alpha_level = 0.05
log_returns_annual = (mu - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * np.random.normal(0, 1, n_sim)
simple_returns = np.exp(log_returns_annual) - 1

var_empirical = -np.percentile(simple_returns, alpha_level * 100)
cvar_empirical = -np.mean(simple_returns[simple_returns <= -var_empirical])

axes[1, 0].hist(simple_returns, bins=100, density=True, alpha=0.5, color='steelblue')
axes[1, 0].axvline(-var_empirical, color='red', ls='--', lw=2,
                    label=f'VaR(5%) = {var_empirical:.2%}')
axes[1, 0].axvline(-cvar_empirical, color='darkred', ls='--', lw=2,
                    label=f'CVaR(5%) = {cvar_empirical:.2%}')
axes[1, 0].fill_betweenx([0, 5], -1, -var_empirical, alpha=0.2, color='red')
axes[1, 0].set_xlim(-0.8, 1.5)
axes[1, 0].set_title('VaR and CVaR under Log-Normal')
axes[1, 0].set_xlabel('Annual Return')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# --- Panel 4: Log returns are Normal ---
daily_log_returns = np.diff(np.log(
    S0 * np.exp(np.cumsum(np.concatenate([[0],
        np.random.normal((mu - 0.5*sigma**2)/252, sigma/np.sqrt(252), 10000)])))))

axes[1, 1].hist(daily_log_returns, bins=80, density=True, alpha=0.5,
                color='steelblue', label='Daily log returns')
x_norm = np.linspace(-0.06, 0.06, 200)
axes[1, 1].plot(x_norm, stats.norm.pdf(x_norm,
                loc=(mu - 0.5*sigma**2)/252, scale=sigma/np.sqrt(252)),
                'r-', lw=2, label='Normal fit')
axes[1, 1].set_title('Daily Log Returns ~ Normal')
axes[1, 1].set_xlabel('Log Return')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('lognormal_finance.png', dpi=150, bbox_inches='tight')
plt.show()
```
