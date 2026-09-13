# 로그정규분포의 로그는 정규분포이다: 모의실험

로그정규분포는 그 로그가 정규분포를 따른다는 성질로 정의된다. 이 모의실험은 그 사실을 눈으로 바로 보여 준다. 로그정규분포 표본에 자연로그를 씌우면 정규분포가 되돌아온다. $X \sim \text{Log-N}(\mu, \sigma^2)$ 일 때 $\ln X$ 의 히스토그램을 $N(\mu, \sigma^2)$ 에서 바로 뽑은 표본과 견주어, 둘이 같은 분포를 따름을 확인한다.

## 배경

$X \sim \text{Log-N}(\mu, \sigma^2)$ 이면 정의에 따라 다음이 성립한다.

$$
Y = \ln X \sim N(\mu, \sigma^2)
$$

이것은 더 흔히 쓰는 구성 $X = e^{Y}$ 의 **반대 방향**이다. 앞 방향(정규확률변수에 지수함수를 씌우기)이 치우쳐 있고 양수만 갖는 분포를 만들어 내는 데 견주어, 반대 방향(로그 씌우기)은 대칭인 종 모양 곡선을 되돌려 준다.

로그변환은 응용통계에서 아주 쓸모 있는 도구이다. 소득이나 주가, 생물학적 측정값처럼 자료가 양수이면서 오른쪽으로 치우쳐 있을 때, 로그를 씌우면 대체로 정규분포에 가까운 자료가 된다. 로그정규분포 모형은 이를 정확한 말로 다듬은 것이다. 곧 로그변환한 자료가 정확히 정규분포를 따르면 원래 자료는 로그정규분포를 따른다.

이 모의실험에서는 $\mu = 2$ 와 $\sigma = 2$ 를 쓴다. 이 모수를 갖는 로그정규분포는 크게 치우쳐 있지만, $\ln$ 을 씌우고 나면 중심이 $2$ 이고 표준편차가 $2$ 인 말끔한 $N(2, 4)$ 종 모양 곡선이 나온다.

## 코드

```python
"""로그정규분포 표본의 로그는 정규분포를 따른다."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

mu, sigma = 2, 2
s, scale = sigma, np.exp(mu)

data = np.log(stats.lognorm(s=s, scale=scale).rvs(10_000))
data_from_norm = stats.norm(loc=mu, scale=sigma).rvs(10_000)

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 4))

_, bins, _ = ax0.hist(data, bins=100, density=True, alpha=0.7, color="steelblue")
y = stats.norm(loc=mu, scale=sigma).pdf(bins)
ax0.plot(bins, y, "--r", lw=2)
ax0.set_title("log(Lognormal samples)")

ax1.hist(data_from_norm, bins=bins, density=True, alpha=0.7, color="steelblue")
ax1.plot(bins, y, "--r", lw=2)
ax1.set_title("Normal samples directly")

for ax in (ax0, ax1):
    ax.grid(True, alpha=0.3)

plt.suptitle(f"log(LogNormal) ~ Normal(μ={mu}, σ={sigma})", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("log_of_lognormal.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 실행 결과

이 코드는 두 개의 패널을 나란히 놓은 그림을 만든다.

- **왼쪽 패널("log(Lognormal samples)"):** 로그정규분포 표본 $X_i$ 10,000개에 대한 $\ln X_i$ 의 정규화된 히스토그램에 $N(2, 4)$ 밀도 곡선(빨간 점선)을 겹쳐 그린 것이다.
- **오른쪽 패널("Normal samples directly"):** $N(2, 4)$ 에서 바로 뽑은 표본 10,000개의 정규화된 히스토그램에 같은 밀도 곡선을 겹쳐 그린 것이다.

두 히스토그램 모두 $\mu = 2$ 를 중심으로 하는 특유의 종 모양을 보이며, 퍼짐의 정도는 $\sigma = 2$ 가 정한다. 범위는 대략 $-4$ 에서 $8$ 까지이다(거의 $\mu \pm 3\sigma$ 이다).

## 뜻풀이

두 패널이 눈으로 보아 똑같다는 사실이 다음 정의상의 동치를 확인해 준다.

$$
X \sim \text{Log-N}(\mu, \sigma^2) \quad \Longleftrightarrow \quad \ln X \sim N(\mu, \sigma^2)
$$

왼쪽 패널은 오른쪽으로 크게 치우친 로그정규분포 표본에서 시작하여 로그변환으로 대칭인 분포를 얻는다. 오른쪽 패널은 같은 대칭 분포를 바로 만들어 낸다. 두 히스토그램을 구별할 수 없다는 것은 로그변환이 지수변환으로 생긴 치우침을 고스란히 "되돌린다"는 뜻이다.

이 결과에는 실용적인 값어치가 있다. 자료 분석에서 원자료가 양수이고 오른쪽으로 치우쳐 보일 때, 로그변환을 하고 (히스토그램이나 Q-Q 그림으로) 정규성을 살펴보는 것은 흔한 진단 절차이다. $\ln X$ 가 대체로 정규분포를 따른다면 $X$ 는 대체로 로그정규분포를 따르고, 로그 눈금 위에서 정규분포에 바탕을 둔 추론 도구 일체(신뢰구간, 가설검정)를 쓸 수 있다.

## 연습문제

**연습문제 1.**
$X \sim \text{Log-N}(3, 9)$ 라 하자. $P(e^{0} < X < e^{6})$ 을 구하여라.

??? success "연습문제 1 풀이"
    $Y = \ln X \sim N(3, 9)$ 로 놓으면($\sigma = 3$) 다음이 성립한다.

    $$
    P(e^{0} < X < e^{6}) = P(0 < Y < 6) = P\!\left(\frac{0 - 3}{3} < Z < \frac{6 - 3}{3}\right) = P(-1 < Z < 1)
    $$

    표준정규분포표를 쓰면 다음을 얻는다.

    $$
    P(-1 < Z < 1) = \mathcal{N}(1) - \mathcal{N}(-1) = 0.8413 - 0.1587 = 0.6827
    $$

    이것은 정규분포의 낯익은 68% 규칙을 로그 눈금 위에서 쓴 것일 뿐이다.

**연습문제 2.**
모의실험을 고쳐 `data`(로그변환한 로그정규분포 표본)와 이론적인 $N(2, 4)$ 분위수를 견주는 Q-Q 그림을 넣어라. 코드를 쓰고 무엇이 나타날지 설명하여라.

??? success "연습문제 2 풀이"
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats

    np.random.seed(42)
    mu, sigma = 2, 2
    data = np.log(stats.lognorm(s=sigma, scale=np.exp(mu)).rvs(10_000))

    fig, ax = plt.subplots(figsize=(6, 6))
    stats.probplot(data, dist="norm", sparams=(mu, sigma), plot=ax)
    ax.set_title("Q-Q Plot: log(LogNormal) vs Normal(2, 4)")
    plt.tight_layout()
    plt.show()
    ```

    Q-Q 그림에서 점들이 대각선 기준선 $y = x$ 위에 거의 그대로 놓일 것이다. $X$ 가 로그정규분포를 따를 때 $\ln X$ 는 근사적으로가 아니라 정확히 정규분포를 따르기 때문이다. 꼬리에서 약간 벗어나는 것은 표집의 흔들림 탓이지만, 표본이 $n = 10{,}000$ 개나 되므로 꼬리에서도 선에 아주 가까울 것이다.

**연습문제 3.**
$X \sim \text{Log-N}(\mu, \sigma^2)$ 이면 $c \neq 0$ 인 어떤 상수에 대해서도 $X^{c} \sim \text{Log-N}(c\mu, c^2 \sigma^2)$ 임을 증명하여라.

??? success "연습문제 3 풀이"
    $Y = \ln X \sim N(\mu, \sigma^2)$ 이라 하자. 그러면 다음이 성립한다.

    $$
    \ln(X^{c}) = c \ln X = c Y
    $$

    $Y \sim N(\mu, \sigma^2)$ 이므로 일차변환 $cY$ 도 정규분포를 따른다.

    $$
    cY \sim N(c\mu, c^2 \sigma^2)
    $$

    따라서 $\ln(X^{c}) \sim N(c\mu, c^2 \sigma^2)$ 이고, 이는 $X^{c} \sim \text{Log-N}(c\mu, c^2 \sigma^2)$ 을 뜻한다. $\square$

    특별한 경우로 $c = -1$ 이면 $1/X \sim \text{Log-N}(-\mu, \sigma^2)$ 이고, $c = 1/2$ 이면 $\sqrt{X} \sim \text{Log-N}(\mu/2, \sigma^2/4)$ 이다.

**연습문제 4.**
양수 값 $n = 5{,}000$ 개로 이루어진 자료의 표본평균이 $\bar{x} = 54.6$ 이고 표본중앙값이 $\tilde{x} = 7.39$ 이다. 로그정규분포 모형 $\text{Log-N}(\mu, \sigma^2)$ 아래에서 중앙값으로 $\mu$ 를 어림하고, 이어 평균 공식으로 $\sigma^2$ 을 어림하여라.

??? success "연습문제 4 풀이"
    $\text{Log-N}(\mu, \sigma^2)$ 의 중앙값은 $e^{\mu}$ 이므로 다음을 얻는다.

    $$
    e^{\mu} = 7.39 \implies \mu = \ln 7.39 \approx 2.0
    $$

    $\text{Log-N}(\mu, \sigma^2)$ 의 평균은 $e^{\mu + \sigma^2/2}$ 이므로 다음을 얻는다.

    $$
    e^{\mu + \sigma^2/2} = 54.6 \implies \mu + \frac{\sigma^2}{2} = \ln 54.6 \approx 4.0
    $$

    $\mu \approx 2.0$ 을 대입하면 다음과 같다.

    $$
    \frac{\sigma^2}{2} = 4.0 - 2.0 = 2.0 \implies \sigma^2 = 4.0
    $$

    따라서 어림한 모수는 $\mu \approx 2$ 와 $\sigma^2 \approx 4$(곧 $\sigma \approx 2$)이다. 평균과 중앙값의 비가 크다는 것($54.6 / 7.39 \approx 7.4$)은 $\sigma$ 가 커서 오른쪽으로 심하게 치우쳐 있음을 보여 준다.

**연습문제 5.**
$X \sim \text{Log-N}(\mu, \sigma^2)$ 일 때 어떤 $t > 0$ 에 대해서도 적률생성함수 $E[e^{tX}]$ 가 존재하지 않음을 보여라.

??? success "연습문제 5 풀이"
    모든 $t > 0$ 에 대하여 $E[e^{tX}] = \infty$ 임을 보이면 된다. $Y \sim N(\mu, \sigma^2)$ 에 대하여 $X = e^{Y}$ 로 적으면 다음과 같다.

    $$
    E[e^{tX}] = E[e^{t e^{Y}}] = \int_{-\infty}^{\infty} e^{t e^{y}} \cdot \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(y - \mu)^2}{2\sigma^2}} \, dy
    $$

    어떤 $t > 0$ 에 대해서도 피적분함수는 인수 $e^{t e^{y}}$ 를 품고 있다. $y \to \infty$ 이면 $e^{y}$ 가 한없이 커지므로 $e^{t e^{y}}$ 는 지수를 뛰어넘는 속도로, 곧 $y$ 에 대한 어떤 다항식이나 지수함수보다도 빠르게 커진다. 그런데 정규분포의 밀도 $e^{-(y-\mu)^2/(2\sigma^2)}$ 는 가우스 꼴로만 줄어든다($y^2$ 에 대한 지수보다 느리다). $e^{te^{y}}$ 의 폭발적인 증가가 가우스 꼴의 감소를 압도하므로 적분은 발산한다.

    $$
    E[e^{tX}] = \infty \quad \text{모든 } t > 0 \text{ 에 대하여}
    $$

    따라서 로그정규분포의 적률생성함수는 어떤 양수 $t$ 에 대해서도 존재하지 않는다. 이는 모든 적률 $E[X^{n}] = e^{n\mu + n^2 \sigma^2/2}$ 이 유한한데도 그렇다. 로그정규분포는 **적률로 분포가 정해지지 않는** 대표적인 예이다. $\square$

**연습문제 6.**
$\text{Log-N}(0, 1)$ 에서 표본 $10{,}000$ 개를 만들어 각각에 $\ln$ 을 씌운 뒤, 그 결과에 정규성에 대한 샤피로–윌크 검정을 하는 모의실험을 돌려라. $p$-값을 해석하여라.

??? success "연습문제 6 풀이"
    ```python
    import numpy as np
    from scipy import stats

    np.random.seed(42)
    X = stats.lognorm(s=1, scale=np.exp(0)).rvs(10_000)
    Y = np.log(X)

    # 샤피로-윌크 검정 (표본 5000개까지만 쓸 수 있다)
    stat, p_value = stats.shapiro(Y[:5000])
    print(f"Shapiro-Wilk statistic: {stat:.6f}")
    print(f"p-value: {p_value:.4f}")
    ```

    샤피로–윌크 검정의 귀무가설 $H_0$ 는 "자료가 정규분포에서 나왔다"이다. $\ln X$ 가 정확히 $N(0, 1)$ 이므로 이 검정이 $H_0$ 를 **기각하지 않을** 것으로 기대된다. $p$-값은 클 것이고($0.05$ 같은 흔한 유의수준보다 훨씬 클 것이다), 정규성을 거스르는 증거가 없음을 뜻한다. 이는 이론적인 결과와도 들어맞는다. 로그정규확률변수에 로그를 씌운 것은 근사적으로가 아니라 정확히 정규분포를 따른다. `scipy.stats.shapiro` 는 표본을 최대 5,000개까지만 받으므로 부분 표본을 썼다는 점에 유의하자.
