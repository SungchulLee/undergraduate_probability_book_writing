# 로그정규분포

## 정의

확률변수 $X$ 가 다음을 만족하면 모수가 $\mu$ 와 $\sigma^2$ 인 **로그정규분포**를 따른다고 한다.

$$Y \sim N(\mu, \sigma^2) \quad \Longleftrightarrow \quad X = e^Y \sim \text{Log-N}(\mu, \sigma^2)$$

같은 말로, $X$ 가 로그정규분포를 따르는 것은 $\log X$ 가 정규분포를 따를 때 그리고 오직 그때만이다.

## 확률밀도함수의 유도

### 누적분포함수 방법

$$P(X \leq x) = P(e^Y \leq x) = P(Y \leq \log x) = \int_{-\infty}^{\log x} \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(s - \mu)^2}{2\sigma^2}}\, ds$$

$x$ 에 대하여 미분하면 다음을 얻는다.

$$f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(\log x - \mu)^2}{2\sigma^2}} \cdot \frac{1}{x}, \quad x > 0$$

### 야코비 방법

$y = \log x$ 로 놓으면 $dy/dx = 1/x$ 이므로 다음을 얻는다.

$$f_X(x) = f_Y(y) \left|\frac{dy}{dx}\right| = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(\log x - \mu)^2}{2\sigma^2}} \cdot \frac{1}{x}, \quad x > 0$$

## 확률밀도함수, 평균, 분산

| 성질 | 공식 |
|----------|---------|
| 확률밀도함수 | $x > 0$ 에 대하여 $\frac{1}{x\sqrt{2\pi\sigma^2}} \exp\!\left(-\frac{(\log x - \mu)^2}{2\sigma^2}\right)$ |
| 평균 | $e^{\mu + \sigma^2/2}$ |
| 분산 | $(e^{\sigma^2} - 1) \cdot e^{2\mu + \sigma^2}$ |
| 중앙값 | $e^{\mu}$ |
| 최빈값 | $e^{\mu - \sigma^2}$ |

!!! note "모수의 뜻"
    모수 $\mu$ 와 $\sigma^2$ 은 $X$ 자체가 아니라 $X$ 의 **로그**의 평균과 분산이다. $X$ 의 평균은 $e^{\mu + \sigma^2/2}$ 이고 이는 언제나 중앙값 $e^{\mu}$ 보다 크다. 분포가 오른쪽으로 치우쳐 있음을 보여 주는 대목이다.

## 모양

로그정규분포의 모양은 다음과 같다.

- 받침(support)이 $(0, \infty)$ 이다
- 오른쪽으로 치우쳐 있다($\sigma^2$ 이 커질수록 더 치우친다)
- 오른쪽 꼬리가 정규분포보다 두껍다
- 주가, 소득 분포, 입자 크기를 나타내는 모형으로 흔히 쓰인다

## 파이썬 구현

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x = np.linspace(0.01, 10, 500)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# sigma 를 바꿔 가며
ax = axes[0]
mu = 0
for sigma in [0.25, 0.5, 1.0, 1.5]:
    ax.plot(x, stats.lognorm.pdf(x, s=sigma, scale=np.exp(mu)),
            label=f'$\\sigma = {sigma}$')
ax.set_title(f'Log-Normal PDF ($\\mu = {mu}$, varying $\\sigma$)')
ax.set_xlabel('$x$'); ax.set_ylabel('$f(x)$')
ax.set_ylim(0, 1.5); ax.legend()

# 평균, 중앙값, 최빈값 견주기
ax = axes[1]
mu, sigma = 0, 1
ax.plot(x, stats.lognorm.pdf(x, s=sigma, scale=np.exp(mu)), 'b-', lw=2)
mean_val = np.exp(mu + sigma**2 / 2)
median_val = np.exp(mu)
mode_val = np.exp(mu - sigma**2)
ax.axvline(mode_val, color='g', ls='--', label=f'Mode = {mode_val:.2f}')
ax.axvline(median_val, color='orange', ls='--', label=f'Median = {median_val:.2f}')
ax.axvline(mean_val, color='r', ls='--', label=f'Mean = {mean_val:.2f}')
ax.set_title('Log-N(0, 1): Mode < Median < Mean')
ax.set_xlabel('$x$'); ax.set_ylabel('$f(x)$')
ax.legend()

plt.tight_layout()
plt.show()
```

## 연습문제

**연습문제 1.**
주식 수익률을 $Y \sim N(0.05, 0.04)$ 에 대하여 $X = e^Y$ 로 나타내는 모형을 생각하자.

(a) $E[X]$ 와 $\text{Var}(X)$ 를 구하여라.

(b) $P(X > 1.2)$ 를 구하여라.

(c) $X$ 의 중앙값을 구하여라.

??? success "연습문제 1 풀이"
    (a) $E[X] = e^{0.05 + 0.02} = e^{0.07} \approx 1.0725$

    $\text{Var}(X) = (e^{0.04} - 1) \cdot e^{0.10 + 0.04} = (e^{0.04} - 1) \cdot e^{0.14} \approx 0.04082 \cdot 1.1503 \approx 0.04695$

    (b) $P(X > 1.2) = P(Y > \ln 1.2) = P\!\left(Z > \frac{0.1823 - 0.05}{0.2}\right) = 1 - \mathcal{N}(0.662) \approx 0.254$

    (c) $X$ 의 중앙값은 $e^{\mu} = e^{0.05} \approx 1.0513$ 이다.
