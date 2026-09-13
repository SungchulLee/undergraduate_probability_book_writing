# 정규분포에서 로그정규분포로: 모의실험

로그정규분포는 정규확률변수에 지수함수를 씌운 것으로 자연스럽게 나타난다. 이 모의실험에서는 두 가지 표집 방법을 견주어 그 동치성을 보인다. 하나는 `scipy.stats.lognorm` 으로 로그정규분포에서 바로 뽑는 것이고, 다른 하나는 정규분포에서 뽑은 표본에 지수함수를 씌우는 것이다. 두 방법 모두 같은 모양의 분포를 내놓으며, 이는 $X \sim \text{Log-N}(\mu, \sigma^2)$ 인 것이 $Y \sim N(\mu, \sigma^2)$ 에 대하여 $X = e^Y$ 인 것과 같음을 확인해 준다.

## 배경

확률변수 $X$ 의 자연로그가 정규분포를 따르면 $X$ 는 모수가 $\mu$ 와 $\sigma^2$ 인 **로그정규분포**를 따른다.

$$
\ln X \sim N(\mu, \sigma^2)
$$

같은 말로, $Y \sim N(\mu, \sigma^2)$ 이면 $X = e^{Y}$ 가 로그정규분포 $\text{Log-N}(\mu, \sigma^2)$ 을 따른다. $X$ 의 확률밀도함수는 다음과 같다.

$$
f_X(x) = \frac{1}{x \sigma \sqrt{2\pi}} \exp\!\left(-\frac{(\ln x - \mu)^2}{2\sigma^2}\right), \quad x > 0
$$

SciPy에서는 **shape** 모수 $s = \sigma$ 와 **scale** 모수 $\text{scale} = e^{\mu}$ 를 쓴다. 곧 `stats.lognorm(s=sigma, scale=np.exp(mu))` 가 $\text{Log-N}(\mu, \sigma^2)$ 을 나타낸다. 이 모의실험에서는 $\mu = 2$ 와 $\sigma = 2$ 를 써서 오른쪽으로 크게 치우친 분포를 만들어, 동치성이 눈에 잘 띄도록 했다.

## 코드

```python
"""Lognormal from Normal: 로그정규분포에서 바로 뽑기와 exp(정규) 를 견준다."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

mu, sigma = 2, 2
s, scale = sigma, np.exp(mu)

data_lognorm = stats.lognorm(s=s, scale=scale).rvs(10_000)
data_from_norm = np.exp(stats.norm(loc=mu, scale=sigma).rvs(10_000))

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 4))
bins = np.linspace(0, 20, 100)

_, bins_out, _ = ax0.hist(data_lognorm, bins=bins, density=True, alpha=0.7,
                          color="steelblue")
y = stats.lognorm(s=s, scale=scale).pdf(bins_out)
ax0.plot(bins_out, y, "--r", lw=2)
ax0.set_title("Lognormal sampling")

ax1.hist(data_from_norm, bins=bins, density=True, alpha=0.7, color="steelblue")
ax1.plot(bins_out, y, "--r", lw=2)
ax1.set_title("exp(Normal) sampling")

for ax in (ax0, ax1):
    ax.grid(True, alpha=0.3)

plt.suptitle(f"LogNormal(μ={mu}, σ={sigma})", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("lognormal_from_normal.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 실행 결과

이 코드는 두 개의 패널을 나란히 놓은 그림을 만든다.

- **왼쪽 패널("Lognormal sampling"):** `stats.lognorm(s=2, scale=np.exp(2))` 에서 바로 뽑은 표본 10,000개의 정규화된 히스토그램에 정확한 로그정규분포 확률밀도함수(빨간 점선)를 겹쳐 그린 것이다.
- **오른쪽 패널("exp(Normal) sampling"):** 각 $Y_i \sim N(2, 4)$ 에 대하여 $e^{Y_i}$ 로 계산한 값 10,000개의 정규화된 히스토그램에 같은 로그정규분포 확률밀도함수를 겹쳐 그린 것이다.

두 히스토그램 모두 오른쪽으로 크게 치우쳐 있고 최빈값이 0 가까이에 있으며 꼬리가 $x = 20$ 너머까지 길게 뻗어 있고, 이론적인 밀도 곡선과 잘 맞는다.

## 뜻풀이

두 패널은 눈으로는 구별되지 않으며, 이는 로그정규분포를 정의하는 성질을 확인해 준다.

$$
X \sim \text{Log-N}(\mu, \sigma^2) \quad \Longleftrightarrow \quad X = e^{Y}, \; Y \sim N(\mu, \sigma^2)
$$

SciPy의 `lognorm` 분포도 속으로는 바로 이 방식으로 표본을 만든다. 표준정규분포에서 뽑은 뒤 위치와 크기를 맞추어 지수변환을 하는 것이다. 이 모의실험은 그 속사정을 겉으로 드러내 준다. 실제로 이 관계를 알아 두면 쓸모가 많다. 예를 들어 $P(X > c)$ 를 구하는 것처럼 이론적인 계산을 할 때 정규분포 쪽으로 옮겨 $P(X > c) = P(Y > \ln c)$($Y$ 는 정규확률변수)로 바꾸면 간단해지기 때문이다.

## 연습문제

**연습문제 1.**
$Y \sim N(3, 1)$ 이고 $X = e^{Y}$ 라 하자. $E[X]$ 와 $\text{Var}(X)$ 를 구하여라.

??? success "연습문제 1 풀이"
    $Y \sim N(\mu, \sigma^2)$ 에 대하여 $X = e^{Y}$ 일 때 적률은 $E[X] = e^{\mu + \sigma^2/2}$ 와 $\text{Var}(X) = (e^{\sigma^2} - 1) \cdot e^{2\mu + \sigma^2}$ 이다.

    $\mu = 3$, $\sigma^2 = 1$ 을 넣으면 다음을 얻는다.

    $$
    E[X] = e^{3 + 1/2} = e^{3.5} \approx 33.115
    $$

    $$
    \text{Var}(X) = (e^{1} - 1) \cdot e^{2(3) + 1} = (e - 1) \cdot e^{7} \approx 1.7183 \times 1096.63 \approx 1884.8
    $$

**연습문제 2.**
모의실험 코드를 고쳐 $\mu = 0$ 과 $\sigma = 0.5$ 를 쓰도록 하여라. $\mu = 2$, $\sigma = 2$ 인 경우와 견주어 히스토그램의 모양이 어떻게 달라지는지 설명하고 그 까닭을 밝혀라.

??? success "연습문제 2 풀이"
    $\mu = 0$, $\sigma = 0.5$ 이면 로그정규분포는 훨씬 덜 치우치고 평균 둘레에 더 모인다. 최빈값은 $e^{\mu - \sigma^2} = e^{-0.25} \approx 0.78$, 중앙값은 $e^{\mu} = 1$, 평균은 $e^{\mu + \sigma^2/2} = e^{0.125} \approx 1.13$ 이다. 이 세 값이 서로 가까워서 분포가 거의 대칭으로 보인다.

    이와 달리 $\mu = 2$, $\sigma = 2$ 이면 최빈값은 $e^{2 - 4} = e^{-2} \approx 0.14$, 중앙값은 $e^{2} \approx 7.39$, 평균은 $e^{2 + 2} = e^{4} \approx 54.6$ 이다. 최빈값과 평균의 큰 차이가 극심한 오른쪽 치우침을 낳는다. 곧 모수 $\sigma$ 가 치우침의 정도를 정하며, $\sigma$ 가 작을수록 로그정규분포는 대칭에 가까워진다.

**연습문제 3.**
$X_1 \sim \text{Log-N}(\mu_1, \sigma_1^2)$ 과 $X_2 \sim \text{Log-N}(\mu_2, \sigma_2^2)$ 이 독립이면 $X_1 X_2 \sim \text{Log-N}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$ 임을 대수적으로 보여라.

??? success "연습문제 3 풀이"
    $Y_1 \sim N(\mu_1, \sigma_1^2)$ 과 $Y_2 \sim N(\mu_2, \sigma_2^2)$ 이 독립일 때 $X_1 = e^{Y_1}$, $X_2 = e^{Y_2}$ 로 적자. 그러면 다음이 성립한다.

    $$
    X_1 X_2 = e^{Y_1} \cdot e^{Y_2} = e^{Y_1 + Y_2}
    $$

    $Y_1$ 과 $Y_2$ 가 독립인 정규확률변수이므로 그 합도 정규분포를 따른다.

    $$
    Y_1 + Y_2 \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)
    $$

    따라서 $X_1 X_2 = e^{Y_1 + Y_2} \sim \text{Log-N}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$ 이다. $\square$

**연습문제 4.**
$Y \sim N(\mu, \sigma^2)$ 일 때의 관계 $P(X > c) = P(Y > \ln c)$ 를 써서 $X \sim \text{Log-N}(2, 4)$ 일 때 $P(X > 10)$ 을 구하여라. 답은 표준정규분포의 누적분포함수 $\mathcal{N}$ 으로 나타내어라.

??? success "연습문제 4 풀이"
    $\mu = 2$ 이고 $\sigma^2 = 4$ 이므로 $\sigma = 2$ 이다. 그러면 다음이 성립한다.

    $$
    P(X > 10) = P(Y > \ln 10) = P\!\left(Z > \frac{\ln 10 - 2}{2}\right)
    $$

    여기서 $Z \sim N(0,1)$ 이다. 인수를 계산하면 다음과 같다.

    $$
    \frac{\ln 10 - 2}{2} = \frac{2.3026 - 2}{2} = \frac{0.3026}{2} = 0.1513
    $$

    따라서 다음을 얻는다.

    $$
    P(X > 10) = 1 - \mathcal{N}(0.1513) \approx 1 - 0.5601 = 0.4399
    $$

    확률의 약 44%가 $x = 10$ 위쪽에 놓여 있으며, 이는 $\sigma$ 가 큰 로그정규분포의 두꺼운 오른쪽 꼬리를 보여 준다.

**연습문제 5.**
$X \sim \text{Log-N}(\mu, \sigma^2)$ 의 중앙값이 $\sigma^2$ 과 상관없이 $e^{\mu}$ 임을 증명하여라.

??? success "연습문제 5 풀이"
    중앙값을 $m$ 이라 하자. 정의에 따라 $P(X \leq m) = 1/2$ 이다. $Y \sim N(\mu, \sigma^2)$ 에 대하여 $X = e^{Y}$ 로 적으면 다음이 성립한다.

    $$
    P(X \leq m) = P(e^{Y} \leq m) = P(Y \leq \ln m)
    $$

    이것을 $1/2$ 로 놓으면 다음과 같다.

    $$
    P(Y \leq \ln m) = \frac{1}{2}
    $$

    $Y \sim N(\mu, \sigma^2)$ 이고 정규분포는 평균에 대하여 대칭이므로 $Y$ 의 중앙값은 $\mu$ 이다. 따라서 $P(Y \leq \mu) = 1/2$ 이고 $\ln m = \mu$ 이므로 다음을 얻는다.

    $$
    m = e^{\mu}
    $$

    이는 $\sigma^2 > 0$ 인 어떤 값에 대해서도 성립한다. $\square$

**연습문제 6.**
$\text{Log-N}(1, 0.25)$ 에서 표본 $n = 50{,}000$ 개를 만들어 평균, 분산, 중앙값을 어림하는 파이썬 코드를 작성하여라. 정확한 값과 견주고 그 정확도를 논하여라.

??? success "연습문제 6 풀이"
    ```python
    import numpy as np
    from scipy import stats

    mu, sigma = 1, 0.5
    n = 50_000
    samples = stats.lognorm(s=sigma, scale=np.exp(mu)).rvs(n)

    print(f"Sample mean:     {np.mean(samples):.4f}")
    print(f"Exact  mean:     {np.exp(mu + sigma**2 / 2):.4f}")
    print(f"Sample variance: {np.var(samples, ddof=1):.4f}")
    print(f"Exact  variance: {(np.exp(sigma**2) - 1) * np.exp(2*mu + sigma**2):.4f}")
    print(f"Sample median:   {np.median(samples):.4f}")
    print(f"Exact  median:   {np.exp(mu):.4f}")
    ```

    $\mu = 1$, $\sigma = 0.5$ 일 때 값은 다음과 같다.

    - 정확한 평균: $e^{1.125} \approx 3.0802$
    - 정확한 분산: $(e^{0.25} - 1) \cdot e^{2.25} \approx 0.2840 \times 9.4877 \approx 2.6945$
    - 정확한 중앙값: $e^{1} \approx 2.7183$

    표본이 $n = 50{,}000$ 개이면 표본에서 얻은 값들이 정확한 값과 소수 둘째 자리쯤까지 맞아떨어질 것이다. 중앙값이 가장 빨리 수렴하는데, 오른쪽 꼬리의 극단값에 휘둘리지 않기 때문이다. 반면 표본평균과 특히 표본분산은 분포가 치우쳐 있어서 더 느리게 수렴한다.
