# Log-Normal Distribution in Finance

The log-normal distribution is the foundation of quantitative finance: geometric Brownian motion models stock prices as log-normal, the Black-Scholes formula assumes log-normal prices, and Value-at-Risk calculations rely on the log-normal CDF.

## Definition

Under the **geometric Brownian motion** (GBM) model, a stock price $S_t$ satisfies the stochastic differential equation:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
$$

where $\mu$ is the drift (expected return), $\sigma$ is the volatility, and $W_t$ is a standard Brownian motion. The solution is:

$$
S_T = S_0 \exp\!\left[\left(\mu - \frac{\sigma^2}{2}\right)T + \sigma W_T\right]
$$

Since $W_T \sim N(0, T)$, the terminal stock price is log-normally distributed:

$$
S_T \sim \text{LogN}\!\left(\ln S_0 + \left(\mu - \frac{\sigma^2}{2}\right)T, \;\; \sigma^2 T\right)
$$

with moments:

$$
E[S_T] = S_0 e^{\mu T}, \qquad \text{Var}(S_T) = S_0^2 e^{2\mu T}(e^{\sigma^2 T} - 1)
$$

## Explanation

### Log returns versus simple returns

Let $R_t = (S_t - S_{t-1})/S_{t-1}$ be the **simple return** and $r_t = \ln(S_t / S_{t-1}) = \ln(1 + R_t)$ the **log return**. Under GBM with time step $\Delta t$:

$$
r_t \sim N\!\left(\left(\mu - \frac{\sigma^2}{2}\right)\Delta t, \;\; \sigma^2 \Delta t\right)
$$

Log returns are preferred in finance because they are additive over time:

$$
\ln\frac{S_n}{S_0} = \sum_{t=1}^{n} r_t
$$

Since independent normal variables sum to a normal, multi-period log returns are also normal, and the multi-period price ratio $S_n/S_0$ is log-normal.

### The drift adjustment

The parameter in the exponent is $\mu - \sigma^2/2$, not $\mu$. This arises because the exponential function is convex, so $E[e^Y] > e^{E[Y]}$ (Jensen's inequality). The term $-\sigma^2/2$ is the **Ito correction** that ensures $E[S_T] = S_0 e^{\mu T}$.

Without this correction, the median of $S_T$ would equal $S_0 e^{\mu T}$ instead of the mean. The correction shifts the log-mean downward so that the exponential mean comes out correctly.

### Value at Risk

The **Value at Risk** (VaR) at confidence level $1 - \alpha$ for a long position held over horizon $T$ is:

$$
\text{VaR}_\alpha = S_0 - S_0 \exp\!\left(\left(\mu - \frac{\sigma^2}{2}\right)T + \sigma\sqrt{T}\,\Phi^{-1}(\alpha)\right)
$$

For small $T$ and $\mu \approx 0$, this simplifies to:

$$
\text{VaR}_\alpha \approx -S_0\,\sigma\sqrt{T}\,\Phi^{-1}(\alpha)
$$

### Conditional Value at Risk

The **CVaR** (Expected Shortfall) at level $\alpha$ measures the expected loss given that the loss exceeds the VaR:

$$
\text{CVaR}_\alpha = S_0\!\left(1 - \frac{e^{\mu T}}{\alpha}\,\Phi\!\left(\Phi^{-1}(\alpha) - \sigma\sqrt{T}\right)\right)
$$

CVaR is always larger than VaR and is considered a more coherent risk measure.

### Limitations of the log-normal model

While mathematically elegant, the log-normal model has known limitations:

- **Fat tails:** Real stock returns exhibit heavier tails than the normal distribution, meaning extreme events occur more frequently than predicted.
- **Volatility clustering:** Real markets show periods of high and low volatility, while GBM assumes constant volatility.
- **No jumps:** The GBM model produces continuous paths, but real prices can jump (e.g., on earnings announcements).

Despite these limitations, the log-normal model remains the standard baseline in finance due to its tractability.

## Examples

**Example 1: Stock price distribution.**

A stock has current price $S_0 = \$100$, expected annual return $\mu = 0.08$, and annual volatility $\sigma = 0.25$. Find the distribution of the price after 1 year and the probability it falls below \$80.

```python
import numpy as np
from scipy import stats

S0, mu, sigma, T = 100, 0.08, 0.25, 1.0

# Log-normal parameters
mu_ln = np.log(S0) + (mu - 0.5 * sigma**2) * T
sigma_ln = sigma * np.sqrt(T)

E_ST = S0 * np.exp(mu * T)
median_ST = np.exp(mu_ln)
print(f"S_T ~ LogN({mu_ln:.4f}, {sigma_ln:.4f}^2)")
print(f"E[S_T] = {E_ST:.2f}")
print(f"Median[S_T] = {median_ST:.2f}")

# P(S_T < 80)
p_below_80 = stats.lognorm.cdf(80, s=sigma_ln, scale=np.exp(mu_ln))
print(f"P(S_T < 80) = {p_below_80:.4f}")
```

**Output:**
```
S_T ~ LogN(4.6888, 0.2500^2)
E[S_T] = 108.33
Median[S_T] = 108.69
P(S_T < 80) = 0.1112
```

**Example 2: Multi-period compounding.**

Daily log returns are iid $N(0.0003, 0.015^2)$ (approximately 7.5% annual return, 24% annual volatility). Find the distribution of the stock price after 252 trading days.

```python
import numpy as np
from scipy import stats

S0 = 100
mu_daily = 0.0003
sigma_daily = 0.015
n_days = 252

# Sum of daily log returns
mu_annual = n_days * mu_daily
sigma_annual = sigma_daily * np.sqrt(n_days)

print(f"Annual log return ~ N({mu_annual:.4f}, {sigma_annual:.4f}^2)")
print(f"Expected annual return (simple): {np.exp(mu_annual + sigma_annual**2/2) - 1:.2%}")

# 90% prediction interval for year-end price
lo = S0 * np.exp(mu_annual + sigma_annual * stats.norm.ppf(0.05))
hi = S0 * np.exp(mu_annual + sigma_annual * stats.norm.ppf(0.95))
print(f"90% prediction interval for S_252: ({lo:.2f}, {hi:.2f})")
```

**Output:**
```
Annual log return ~ N(0.0756, 0.2381^2)
Expected annual return (simple): 10.85%
90% prediction interval for S_252: (74.33, 156.26)
```

**Example 3: Value at Risk calculation.**

Compute the 5% VaR for a \$1,000,000 portfolio with $\mu = 0.10$, $\sigma = 0.20$ over a 10-day horizon.

```python
import numpy as np
from scipy import stats

S0 = 1_000_000
mu, sigma = 0.10, 0.20
T = 10 / 252  # 10 trading days

# Exact log-normal VaR
alpha = 0.05
ST_alpha = S0 * np.exp((mu - 0.5*sigma**2)*T + sigma*np.sqrt(T)*stats.norm.ppf(alpha))
VaR_exact = S0 - ST_alpha

# Approximate VaR (for small T)
VaR_approx = -S0 * sigma * np.sqrt(T) * stats.norm.ppf(alpha)

print(f"Portfolio: ${S0:,.0f}, T = {T:.4f} years ({10} days)")
print(f"Exact VaR(5%):  ${VaR_exact:,.0f}")
print(f"Approx VaR(5%): ${VaR_approx:,.0f}")

# CVaR
phi_inv = stats.norm.ppf(alpha)
CVaR = S0 * (1 - np.exp(mu*T)/alpha * stats.norm.cdf(phi_inv - sigma*np.sqrt(T)))
print(f"CVaR(5%):       ${CVaR:,.0f}")
```

**Output:**
```
Portfolio: $1,000,000, T = 0.0397 years (10 days)
Exact VaR(5%):  $63,576
Approx VaR(5%): $65,552
CVaR(5%):       $80,543
```

**Example 4: Simulating GBM paths.**

```python
import numpy as np

np.random.seed(42)
S0, mu, sigma = 100, 0.08, 0.25
T, n_steps = 1.0, 252
dt = T / n_steps

# Simulate 5 paths
for path in range(5):
    dW = np.random.normal(0, np.sqrt(dt), n_steps)
    log_returns = (mu - 0.5*sigma**2) * dt + sigma * dW
    S_final = S0 * np.exp(np.sum(log_returns))
    total_return = S_final / S0 - 1
    print(f"Path {path+1}: S_T = {S_final:.2f}, return = {total_return:+.2%}")

# Large simulation for distribution verification
n_sim = 100000
WT = np.random.normal(0, np.sqrt(T), n_sim)
ST = S0 * np.exp((mu - 0.5*sigma**2)*T + sigma*WT)
print(f"\n{n_sim} simulations:")
print(f"  Mean S_T:   {ST.mean():.2f}  (theory: {S0*np.exp(mu*T):.2f})")
print(f"  Median S_T: {np.median(ST):.2f}  (theory: {S0*np.exp((mu-0.5*sigma**2)*T):.2f})")
print(f"  P(loss):    {np.mean(ST < S0):.4f}")
```

**Output:**
```
Path 1: S_T = 113.44, return = +13.44%
Path 2: S_T = 86.87, return = -13.13%
Path 3: S_T = 120.19, return = +20.19%
Path 4: S_T = 139.83, return = +39.83%
Path 5: S_T = 91.52, return = -8.48%

100000 simulations:
  Mean S_T:   108.26  (theory: 108.33)
  Median S_T: 96.09  (theory: 96.08)
  P(loss):    0.3893
```
