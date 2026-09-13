# 금융에서의 로그정규분포

## 주가 모형

**기하 브라운 운동**(GBM) 모형에서 주가 $S_t$ 는 다음을 만족한다.

$$dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$$

여기서 $\mu$ 는 표류율, $\sigma$ 는 변동성, $W_t$ 는 표준 브라운 운동이다. 그 해는 다음과 같다.

$$S_T = S_0 \exp\!\left[\left(\mu - \frac{\sigma^2}{2}\right)T + \sigma W_T\right]$$

$W_T \sim N(0, T)$ 이므로 $\ln S_T \sim N\!\left(\ln S_0 + (\mu - \frac{\sigma^2}{2})T,\; \sigma^2 T\right)$ 이고, 따라서 $S_T$ 는 **로그정규분포**를 따른다.

!!! info "기하 브라운 운동의 분포"

    $$S_T \sim \text{LogNormal}\!\left(\ln S_0 + \left(\mu - \frac{\sigma^2}{2}\right)T,\;\; \sigma^2 T\right)$$

    $$E[S_T] = S_0 e^{\mu T}, \qquad \text{Var}(S_T) = S_0^2 e^{2\mu T}\left(e^{\sigma^2 T} - 1\right)$$

## 로그수익률과 단순수익률

단순수익률을 $R_t = \frac{S_t - S_{t-1}}{S_{t-1}}$, 로그수익률을 $r_t = \ln\frac{S_t}{S_{t-1}} = \ln(1 + R_t)$ 라 하자.

기하 브라운 운동에서 하루 단위 증분을 보면 다음이 성립한다.

$$r_t \sim N\!\left(\left(\mu - \frac{\sigma^2}{2}\right)\Delta t,\;\; \sigma^2 \Delta t\right)$$

**여러 기간의 복리.** $n$ 기간에 걸쳐 다음이 성립한다.

$$\frac{S_n}{S_0} = \prod_{t=1}^{n}(1 + R_t) = \exp\!\left(\sum_{t=1}^{n} r_t\right)$$

로그수익률이 i.i.d. 정규분포를 따르므로 $\sum r_t$ 는 정규분포를 따르고 $S_n / S_0$ 는 로그정규분포를 따른다.

## 위험가치(VaR)

로그정규분포 모형에서 매수 포지션에 대한 수준 $\alpha$ 의 위험가치는 확률 $\alpha$ 로 넘어서는 손실이다.

$$\text{VaR}_\alpha = S_0 - S_0 \exp\!\left(\left(\mu - \frac{\sigma^2}{2}\right)T + \sigma\sqrt{T}\,\mathcal{N}^{-1}(\alpha)\right)$$

$T$ 가 작고 $\mu \approx 0$ 이면 이 식은 다음과 같이 간단해진다.

$$\text{VaR}_\alpha \approx -S_0\,\sigma\sqrt{T}\,\mathcal{N}^{-1}(\alpha)$$

## 조건부 위험가치(CVaR)

수준 $\alpha$ 의 **조건부 위험가치**(기대손실)는 다음과 같다.

$$\text{CVaR}_\alpha = E\left[-R \mid R \leq -\text{VaR}_\alpha / S_0\right]$$

로그정규분포 모형에서는 다음과 같다.

$$\text{CVaR}_\alpha = S_0\left(1 - \frac{e^{\mu T}}{\alpha}\,\mathcal{N}\!\left(\mathcal{N}^{-1}(\alpha) - \sigma\sqrt{T}\right)\right)$$

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

np.random.seed(42)

# --- 모수 ---
S0, mu, sigma, T = 100, 0.08, 0.25, 1.0
n_paths, n_steps = 50, 252

# --- 패널 1: 기하 브라운 운동의 표본 경로 ---
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

# --- 패널 2: 만기 시점의 분포 ---
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

# --- 패널 3: VaR 과 CVaR 그림 ---
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

# --- 패널 4: 로그수익률은 정규분포를 따른다 ---
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

## 연습문제

**연습문제 1.** 어떤 주식이 지금 \$100 에 거래되고 있고 연간 표류율은 $\mu = 0.10$, 변동성은 $\sigma = 0.20$ 이다. 기하 브라운 운동 아래에서 $E[S_1]$ 과 $S_1$ 의 중앙값을 구하여라.

??? success "연습문제 1 풀이"
    $E[S_1] = 100 \cdot e^{0.10} \approx \$110.52$ 이다.

    중앙값: $\exp(\ln 100 + (0.10 - 0.02) \cdot 1) = 100 \cdot e^{0.08} \approx \$108.33$ 이다.

---

**연습문제 2.** 연습문제 1과 같은 모형에서 $P(S_1 > 120)$ 을 구하여라.

??? success "연습문제 2 풀이"
    $\ln S_1 \sim N(\ln 100 + 0.08, 0.04)$ 이다. 곧 $\ln S_1 \sim N(4.6852 + 0.08, 0.04) = N(4.6652, 0.04)$ 이다.

    $$
    P(S_1 > 120) = P\!\left(\frac{\ln S_1 - 4.6652}{0.2} > \frac{\ln 120 - 4.6652}{0.2}\right) = P\!\left(Z > \frac{4.7875 - 4.6652}{0.2}\right) = P(Z > 0.611)
    $$

    $$
    \approx 1 - \mathcal{N}(0.611) \approx 1 - 0.7294 = 0.2706
    $$

---

**연습문제 3.** 어떤 자산 묶음의 하루 로그수익률이 $r_t \sim N(0.0003, 0.0004)$ 이다. 거래일 기준 한 해(252일) 동안의 누적 총수익률 $S_{252}/S_0$ 의 분포는 무엇인가?

??? success "연습문제 3 풀이"
    $\ln(S_{252}/S_0) = \sum_{t=1}^{252} r_t \sim N(252 \times 0.0003, 252 \times 0.0004) = N(0.0756, 0.1008)$ 이다.

    따라서 $S_{252}/S_0 \sim \text{LogNormal}(0.0756, 0.1008)$ 이다.

    $E[S_{252}/S_0] = e^{0.0756 + 0.0504} = e^{0.1260} \approx 1.134$ 이므로 기대수익률은 약 13.4% 이다.

---

**연습문제 4.** 연간 표류율이 $\mu = 0.05$, 변동성이 $\sigma = 0.30$ 인 \$1,000,000 짜리 자산 묶음에 대하여 1년 기간의 5% 위험가치를 구하여라.

??? success "연습문제 4 풀이"
    $\mathcal{N}^{-1}(0.05) \approx -1.645$ 이다.

    $$
    \text{VaR}_{0.05} = S_0 - S_0 \exp\!\left((0.05 - 0.045) \cdot 1 + 0.30 \cdot (-1.645)\right)
    $$

    $$
    = 1{,}000{,}000\left(1 - e^{0.005 - 0.4935}\right) = 1{,}000{,}000(1 - e^{-0.4885}) \approx 1{,}000{,}000 \times 0.3867 = \$386{,}700
    $$

---

**연습문제 5.** 금융 모형에서 단순수익률보다 하루 로그수익률을 더 즐겨 쓰는 까닭을 로그정규분포의 틀과 이어서 설명하여라.

??? success "연습문제 5 풀이"
    로그수익률 $r_t = \ln(S_t/S_{t-1})$ 을 더 즐겨 쓰는 까닭은 다음과 같다.

    1. **더할 수 있다:** 여러 기간의 로그수익률은 합이 된다. 곧 $\ln(S_T/S_0) = \sum r_t$ 이다. i.i.d. 정규확률변수의 합은 정규분포를 따르므로 다루기가 쉬워진다.
    2. **정규성:** 기간이 충분히 짧으면 중심극한정리가 로그수익률을 정규분포로 보는 것을 정당화해 준다.
    3. **음수 문제가 없다:** 단순수익률 $R_t$ 는 아래로 $-1$ 에 막혀 있지만(100%보다 더 잃을 수는 없다), 정규분포를 따르는 단순수익률은 얼마든지 음수가 될 수 있다. 로그수익률은 이 문제를 비껴간다. $S_t = S_0 e^{r_t} > 0$ 이 언제나 성립하기 때문이다.
    4. **곱셈에 대해 닫혀 있다:** 로그정규분포를 따르는 가격의 곱은 다시 로그정규분포를 따르므로 모형이 같은 분포 집안 안에 머문다.
