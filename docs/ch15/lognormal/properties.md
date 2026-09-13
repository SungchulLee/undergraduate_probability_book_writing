# 성질과 적률

## 평균과 분산

!!! info "로그정규분포의 적률"
    $X \sim \text{LogNormal}(\mu, \sigma^2)$, 곧 $\ln X \sim N(\mu, \sigma^2)$ 이면 다음이 성립한다.

    $$E[X] = e^{\mu + \sigma^2/2}$$

    $$\text{Var}(X) = e^{2\mu + \sigma^2}\left(e^{\sigma^2} - 1\right)$$

**평균의 유도.** $Y \sim N(\mu, \sigma^2)$ 에 대하여 $X = e^Y$ 이므로 다음이 성립한다.

$$E[X] = E[e^Y] = M_Y(1)$$

여기서 $M_Y(t) = e^{\mu t + \sigma^2 t^2/2}$ 는 정규분포의 적률생성함수이다. $t = 1$ 로 놓으면 다음을 얻는다.

$$E[X] = e^{\mu + \sigma^2/2}$$

**$E[X^2]$ 의 유도.** 마찬가지로 $E[X^2] = E[e^{2Y}] = M_Y(2) = e^{2\mu + 2\sigma^2}$ 이므로 다음을 얻는다.

$$\text{Var}(X) = e^{2\mu + 2\sigma^2} - e^{2\mu + \sigma^2} = e^{2\mu + \sigma^2}(e^{\sigma^2} - 1)$$

**일반적인 원점 적률:**

$$E[X^k] = e^{k\mu + k^2\sigma^2/2}$$

## 중앙값과 최빈값

!!! info "중앙값과 최빈값"

    $$\text{Median}(X) = e^{\mu}$$

    $$\text{Mode}(X) = e^{\mu - \sigma^2}$$

중앙값은 $Y = \ln X \sim N(\mu, \sigma^2)$ 에 대하여 $P(X \leq e^\mu) = P(Y \leq \mu) = 0.5$ 이기 때문에 나온다.

최빈값은 확률밀도함수를 미분하여 $f'(x) = 0$ 으로 놓아 얻는다.

$$f(x) = \frac{1}{x\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(\ln x - \mu)^2}{2\sigma^2}\right)$$

$\sigma > 0$ 이면 언제나 $\text{Mode} < \text{Median} < \text{Mean}$ 의 순서가 성립하며, 이는 로그정규분포가 **오른쪽으로 치우쳐 있음**을 보여 준다.

## 왜도와 첨도

$$\gamma_1 = (e^{\sigma^2} + 2)\sqrt{e^{\sigma^2} - 1}$$

$$\gamma_2 = e^{4\sigma^2} + 2e^{3\sigma^2} + 3e^{2\sigma^2} - 6$$

둘 다 언제나 양수이고 $\mu$ 가 아니라 $\sigma^2$ 에만 달려 있다. 로그정규분포는 **언제나 오른쪽으로 치우쳐 있고** **언제나 뾰족하다**(꼬리가 두껍다).

## 곱셈에 대한 성질

로그정규분포 집안은 덧셈이 아니라 **곱셈**에 대해 닫혀 있다.

!!! info "로그정규확률변수의 곱"
    $X_i \sim \text{LogNormal}(\mu_i, \sigma_i^2)$ 가 **독립**이면 다음이 성립한다.

    $$\prod_{i=1}^{n} X_i \sim \text{LogNormal}\!\left(\sum_{i=1}^{n} \mu_i,\; \sum_{i=1}^{n} \sigma_i^2\right)$$

**증명.** $\ln\!\left(\prod X_i\right) = \sum \ln X_i = \sum Y_i$ 이고 여기서 $Y_i \sim N(\mu_i, \sigma_i^2)$ 는 독립이다. 독립인 정규확률변수의 합은 정규분포를 따른다. $\square$

마찬가지로 상수 거듭제곱 $c$ 에 대하여 다음이 성립한다.

$$X^c \sim \text{LogNormal}(c\mu, c^2\sigma^2)$$

$\ln(X^c) = c \ln X = cY \sim N(c\mu, c^2\sigma^2)$ 이기 때문이다.

## 정규분포와의 관계

| 성질 | 정규분포 | 로그정규분포 |
|:---|:---:|:---:|
| 받침(support) | $(-\infty, \infty)$ | $(0, \infty)$ |
| 닫혀 있는 연산 | 덧셈 | 곱셈 |
| 왜도 | 0 | 언제나 양수 |
| 대칭성 | 대칭 | 오른쪽으로 치우침 |
| 적률생성함수가 있는가? | 있다 | 없다(모든 적률은 있지만 적률생성함수는 무한대) |

!!! warning "적률생성함수가 없다"
    로그정규분포에는 **적률생성함수가 없다**. 구체적으로 모든 $t > 0$ 에 대하여 $E[e^{tX}] = \infty$ 이다. 로그정규분포의 꼬리가 "너무 두꺼워서" 지수 적률이 수렴하지 않기 때문이다. 그러나 모든 원점 적률 $E[X^k]$ 은 있고 유한하다.

## 누적분포함수와 분위수

$X \sim \text{LogNormal}(\mu, \sigma^2)$ 의 누적분포함수는 다음과 같다.

$$F(x) = P(X \leq x) = P(Y \leq \ln x) = \mathcal{N}\!\left(\frac{\ln x - \mu}{\sigma}\right), \quad x > 0$$

$p$ 번째 분위수는 다음과 같다.

$$Q(p) = \exp\!\left(\mu + \sigma\,\mathcal{N}^{-1}(p)\right)$$

덕분에 자산 수익률을 로그정규분포로 나타낼 때 위험가치(VaR) 계산이 간단해진다.

## 금융에서의 응용

로그정규분포는 계량 금융의 바탕이 되는 분포이다.

**1. 기하 브라운 운동.** 주가가 $dS = \mu S\,dt + \sigma S\,dW_t$ 를 따르면 다음이 성립한다.

$$S_T = S_0 \exp\!\left[\left(\mu - \frac{\sigma^2}{2}\right)T + \sigma W_T\right]$$

따라서 $S_T$ 는 모수가 $\ln S_0 + (\mu - \sigma^2/2)T$ 와 $\sigma^2 T$ 인 로그정규분포를 따른다.

**2. 블랙–숄즈 모형.** 블랙–숄즈 옵션 가격 공식은 주가가 로그정규분포를 따른다고 가정한다.

**3. 자산 묶음의 수익률.** 한 기간의 로그수익률이 $r_t \sim N(\mu, \sigma^2)$ 이면 누적 총수익률 $\prod(1 + R_t) = e^{\sum r_t}$ 는 로그정규분포를 따른다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# --- 패널 1: 모양 분석 ---
x = np.linspace(0.001, 8, 500)
params = [(0, 0.25), (0, 0.5), (0, 1.0), (1, 0.5)]
colors = ['blue', 'red', 'green', 'purple']

for (mu, sigma), color in zip(params, colors):
    pdf = stats.lognorm.pdf(x, s=sigma, scale=np.exp(mu))
    axes[0].plot(x, pdf, color=color, lw=2,
                 label=f'μ={mu}, σ={sigma}')
    # 평균, 중앙값, 최빈값 표시
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

# --- 패널 2: 평균, 중앙값, 최빈값의 관계 ---
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

# --- 패널 3: 곱셈에 대해 닫혀 있음 ---
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

## 연습문제

**연습문제 1.** $X \sim \text{LogNormal}(2, 0.25)$ 라 하자. $E[X]$, $\text{Var}(X)$, 그리고 중앙값을 구하여라.

??? success "연습문제 1 풀이"
    $E[X] = e^{2 + 0.125} = e^{2.125} \approx 8.372$ 이다.

    $\text{Var}(X) = e^{4 + 0.25}(e^{0.25} - 1) = e^{4.25}(1.284 - 1) = 70.105 \times 0.284 \approx 19.91$ 이다.

    중앙값 $= e^{2} \approx 7.389$ 이다.

---

**연습문제 2.** $X \sim \text{LogNormal}(1, 0.04)$ 와 $Y \sim \text{LogNormal}(2, 0.09)$ 가 독립일 때 $XY$ 의 분포를 구하여라.

??? success "연습문제 2 풀이"
    곱셈에 대한 성질에 따라 다음이 성립한다.

    $$
    XY \sim \text{LogNormal}(1 + 2, 0.04 + 0.09) = \text{LogNormal}(3, 0.13)
    $$

---

**연습문제 3.** $\sigma > 0$ 인 어떤 로그정규분포에 대해서도 최빈값 $<$ 중앙값 $<$ 평균임을 증명하여라.

??? success "연습문제 3 풀이"
    최빈값 $= e^{\mu - \sigma^2}$, 중앙값 $= e^{\mu}$, 평균 $= e^{\mu + \sigma^2/2}$ 이다.

    $\sigma^2 > 0$ 이므로 $\mu - \sigma^2 < \mu < \mu + \sigma^2/2$ 이고, 지수함수가 순증가하므로 $e^{\mu - \sigma^2} < e^{\mu} < e^{\mu + \sigma^2/2}$ 이다. $\square$

---

**연습문제 4.** $X \sim \text{LogNormal}(0, 1)$ 의 95번째 백분위수를 구하여라.

??? success "연습문제 4 풀이"
    $$
    Q(0.95) = \exp(\mu + \sigma \cdot \mathcal{N}^{-1}(0.95)) = \exp(0 + 1 \times 1.6449) = e^{1.6449} \approx 5.18
    $$

---

**연습문제 5.** $X \sim \text{LogNormal}(\mu, \sigma^2)$ 일 때 모든 $t > 0$ 에 대하여 $E[e^{tX}] = \infty$ 임을 보여라.

??? success "연습문제 5 풀이"
    $Y \sim N(\mu, \sigma^2)$ 에 대하여 $X = e^Y$ 이다. 그러면 $E[e^{tX}] = E[e^{te^Y}]$ 이다.

    $t > 0$ 이고 $y$ 가 클 때 $te^y$ 는 $y^2/(2\sigma^2)$ 보다 훨씬 빠르게 커진다. 곧 다음과 같다.

    $$
    E[e^{tX}] = \int_{-\infty}^{\infty} e^{te^y} \frac{e^{-(y-\mu)^2/(2\sigma^2)}}{\sigma\sqrt{2\pi}}\,dy
    $$

    $y$ 가 클 때 피적분함수는 $\exp(te^y - y^2/(2\sigma^2))$ 처럼 커진다. $y \to \infty$ 일 때 $e^y \gg y^2$ 이므로 지수가 $+\infty$ 로 발산하고, 따라서 적분값이 무한대가 된다. $\square$

---

**연습문제 6.** $Y \sim N(0, 1)$ 이고 $X = e^Y$ 라 하자. $E[X]$ 를 구하여라.

??? success "연습문제 6 풀이"
    $\ln X = Y \sim N(0, 1)$ 이므로 $X \sim \text{LogNormal}(0, 1)$ 이다. $\mu = 0$, $\sigma^2 = 1$ 을 평균 공식에 넣으면 다음을 얻는다.

    $$
    E[X] = e^{\mu + \sigma^2/2} = e^{0 + 1/2} = e^{1/2} = \sqrt{e} \approx 1.6487
    $$
