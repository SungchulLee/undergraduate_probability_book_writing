# 이변량정규분포의 밀도함수: 3차원 그림

이변량정규분포를 살펴보는 가장 밝은 길 가운데 하나가 3차원 곡면 그림이다.
결합밀도함수를 $(x, y)$ 평면 위의 곡면으로 그려 보면, 상관계수 $\rho$ 가 모양과 기울기와 확률의 쏠림을 어떻게 좌우하는지 눈으로 바로 확인할 수 있다.
이 절에서는 서로 다른 세 개의 $\rho$ 값에 대한 3차원 그림을 나란히 그려 주는 파이썬 코드를 소개한다.

## 배경

평균벡터가 $\boldsymbol{\mu} = (\mu_1, \mu_2)^T$ 이고 공분산행렬이

$$
\boldsymbol{\Sigma} = \begin{pmatrix} \sigma_1^2 & \rho\,\sigma_1\sigma_2 \\ \rho\,\sigma_1\sigma_2 & \sigma_2^2 \end{pmatrix}
$$

인 **이변량정규분포**의 결합확률밀도함수는 다음과 같다.

$$
f(x, y) = \frac{1}{2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}} \exp\!\left(-\frac{1}{2(1-\rho^2)}\left[\frac{(x-\mu_1)^2}{\sigma_1^2} - 2\rho\frac{(x-\mu_1)(y-\mu_2)}{\sigma_1\sigma_2} + \frac{(y-\mu_2)^2}{\sigma_2^2}\right]\right)
$$

여기에서 $-1 < \rho < 1$ 은 $X$ 와 $Y$ 사이의 **상관계수**이다.

지수부는 $(x, y)$ 에 대한 이차형식이다. 등위집합 $f(x,y) = c$ 는 타원이며, 그 축은 $\boldsymbol{\Sigma}^{-1}$ 의 고유벡터로 정해진다. $\rho = 0$ 이면 타원의 축이 좌표축과 나란하다. $\rho \neq 0$ 이면 타원이 기울어지는데, $\rho$ 가 양수이면 직선 $y = x$ 쪽으로, 음수이면 $y = -x$ 쪽으로 기운다.

아래 코드는 $\mu_1 = \mu_2 = 0$, $\sigma_1 = 1$, $\sigma_2 = 0.5$ 로 두고 $\rho \in \{0, -0.8, 0.8\}$ 에 대한 곡면을 그린다.

## 코드

```python
"""상관계수를 달리하며 이변량정규분포 밀도함수를 3차원 곡면으로 그린다."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

n = 40
mu1, mu2 = 0, 0
sigma1, sigma2 = 1, 0.5
rhos = (0.0, -0.8, 0.8)

x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
pos = np.stack([X, Y], axis=-1)

fig, axes = plt.subplots(1, 3, figsize=(16, 5), subplot_kw={"projection": "3d"})
for ax, rho in zip(axes, rhos):
    cov = [[sigma1**2, rho * sigma1 * sigma2],
           [rho * sigma1 * sigma2, sigma2**2]]
    Z = stats.multivariate_normal([mu1, mu2], cov).pdf(pos)
    ax.plot_surface(X, Y, Z, cmap="viridis", linewidth=0, antialiased=True)
    ax.set_title(f"ρ = {rho}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.view_init(30, -60)

plt.suptitle("Bivariate Normal PDF", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("bivariate_normal_pdf.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 실행 결과

이 코드는 세 개의 3차원 곡면 그림이 나란히 놓인 그림 하나를 만들어 낸다.

- **왼쪽 ($\rho = 0$):** 곡면은 $x$ 축 방향으로 길게 늘어난($\sigma_1 = 1 > \sigma_2 = 0.5$ 이므로) 대칭인 종 모양이며, 그 축이 좌표축과 나란하다.
- **가운데 ($\rho = -0.8$):** 종 모양이 기울어져 $(x, y)$ 평면에서 장축이 왼쪽 위에서 오른쪽 아래로 향한다. 강한 음의 상관을 그대로 보여 준다.
- **오른쪽 ($\rho = 0.8$):** 종 모양이 반대쪽으로 기울어져 장축이 왼쪽 아래에서 오른쪽 위로 향한다. 강한 양의 상관을 보여 준다.

세 곡면 모두 `viridis` 색지도로 칠했으며, 밝은 색일수록 밀도가 높은 곳이다.

## 뜻풀이

이 세 그림은 이변량정규분포의 중요한 특징 몇 가지를 한눈에 드러내 준다.

1. **상관계수가 기울기를 정한다.** $\rho$ 가 $0$ 에서 $\pm 1$ 쪽으로 옮겨 갈수록 종 모양 곡면이 회전한다. $\rho$ 가 양수이면 마루가 $x$ 와 $y$ 가 함께 커지는 방향으로 놓이고, 음수이면 하나가 커질 때 다른 하나가 작아지는 방향으로 놓인다.

2. **상관계수가 쏠림을 정한다.** $|\rho|$ 가 $1$ 에 가까우면 곡면이 좁고 길쭉한 마루가 되어 확률이 한 직선 가까이에 몰린다. $\rho = 0$ 일 때는 주어진 주변분산 아래에서 곡면이 가장 넓게 퍼진다.

3. **주변분산이 다르면 비대칭이 생긴다.** $\sigma_1 = 1$ 이고 $\sigma_2 = 0.5$ 이므로 $\rho = 0$ 일 때조차 곡면이 $y$ 방향보다 $x$ 방향으로 더 넓다. 이 비대칭은 세 그림 모두에서 그대로 남는다.

4. **꼭짓점의 높이가 달라진다.** 밀도함수의 최댓값은 $f(\mu_1, \mu_2) = \frac{1}{2\pi\sigma_1\sigma_2\sqrt{1 - \rho^2}}$ 이다. $|\rho|$ 가 커질수록 $\sqrt{1 - \rho^2}$ 이 작아지므로, $|\rho| = 0.8$ 일 때가 $\rho = 0$ 일 때보다 꼭짓점이 더 높다.

## 연습문제

**연습문제 1.** $\mu_1 = \mu_2 = 0$, $\sigma_1 = 1$, $\sigma_2 = 0.5$ 일 때, 세 상관계수 $\rho \in \{0, -0.8, 0.8\}$ 각각에 대하여 꼭짓점의 밀도 $f(0,0)$ 을 구하여라.

??? success "풀이"
    꼭짓점은 평균에 있다.

    $$
    f(0, 0) = \frac{1}{2\pi \sigma_1 \sigma_2 \sqrt{1 - \rho^2}} = \frac{1}{2\pi (1)(0.5)\sqrt{1 - \rho^2}} = \frac{1}{\pi\sqrt{1 - \rho^2}}
    $$

    - $\rho = 0$: $f(0,0) = \frac{1}{\pi} \approx 0.3183$.
    - $\rho = \pm 0.8$: $\sqrt{1 - 0.64} = \sqrt{0.36} = 0.6$ 이므로 $f(0,0) = \frac{1}{0.6\pi} \approx 0.5305$.

    상관이 클수록 확률이 마루 가까이로 몰리므로 꼭짓점이 높아진다.

**연습문제 2.** $\rho = 0$ 이고 $\sigma_1 = \sigma_2 = \sigma$ 이면 등위곡선 $f(x, y) = c$ 가 $(\mu_1, \mu_2)$ 를 중심으로 하는 원임을 보여라.

??? success "풀이"
    $\rho = 0$ 이고 $\sigma_1 = \sigma_2 = \sigma$ 이면 밀도함수가 다음과 같이 간단해진다.

    $$
    f(x, y) = \frac{1}{2\pi\sigma^2}\exp\!\left(-\frac{(x - \mu_1)^2 + (y - \mu_2)^2}{2\sigma^2}\right)
    $$

    $f(x, y) = c$ 로 두고 로그를 취하면 다음을 얻는다.

    $$
    -\frac{(x - \mu_1)^2 + (y - \mu_2)^2}{2\sigma^2} = \ln(2\pi\sigma^2 c)
    $$

    곧 $r^2 = -2\sigma^2 \ln(2\pi\sigma^2 c)$ 라고 할 때 $(x - \mu_1)^2 + (y - \mu_2)^2 = r^2$ 이 되며, 이는 $(\mu_1, \mu_2)$ 를 중심으로 하는 원의 방정식이다. $\square$

**연습문제 3.** 코드에서 $\rho = 0.8$ 일 때 쓰인 공분산행렬 $\boldsymbol{\Sigma}$ 의 고윳값을 구하여라. 이 고윳값들은 밀도 곡면의 모양에 대하여 무엇을 말해 주는가?

??? success "풀이"
    공분산행렬은 다음과 같다.

    $$
    \boldsymbol{\Sigma} = \begin{pmatrix} 1 & 0.4 \\ 0.4 & 0.25 \end{pmatrix}
    $$

    특성방정식은 다음과 같다.

    $$
    \lambda^2 - \mathrm{tr}(\boldsymbol{\Sigma})\,\lambda + \det(\boldsymbol{\Sigma}) = 0
    $$

    $\mathrm{tr}(\boldsymbol{\Sigma}) = 1.25$ 이고 $\det(\boldsymbol{\Sigma}) = 0.25 - 0.16 = 0.09$ 이므로

    $$
    \lambda = \frac{1.25 \pm \sqrt{1.5625 - 0.36}}{2} = \frac{1.25 \pm \sqrt{1.2025}}{2} = \frac{1.25 \pm 1.0966}{2}
    $$

    따라서 $\lambda_1 \approx 1.1733$, $\lambda_2 \approx 0.0767$ 이다. 비 $\lambda_1 / \lambda_2 \approx 15.3$ 이 크다는 것은 밀도 곡면이 $\lambda_1$ 에 딸린 고유벡터 방향으로 매우 길쭉한 마루 모양임을 뜻한다.

**연습문제 4.** 코드를 고쳐 $\rho = 0.99$ 인 네 번째 그림을 덧붙여라. 코드를 돌리기 전에 그 곡면이 $\rho = 0.8$ 인 그림과 어떻게 달라질지 말로 예측하여라. 그런 다음 고친 코드를 돌려 확인하여라.

??? success "풀이"
    **예측:** $\rho \to 1$ 이면 $\sqrt{1 - \rho^2} \to 0$ 이므로 꼭짓점의 밀도 $f(0,0) = 1/(\pi\sqrt{1-\rho^2})$ 이 한없이 커진다. 곡면은 직선 $y = (\sigma_2/\sigma_1)(x - \mu_1) + \mu_2$, 여기에서는 $y = 0.5x$ 가까이에 몰린 매우 좁고 높은 마루가 된다. $\rho = 0.8$ 인 그림과 견주면 거의 찌부러진 모습으로 보일 것이다.

    **고친 코드:**

    ```python
    rhos = (0.0, -0.8, 0.8, 0.99)
    fig, axes = plt.subplots(1, 4, figsize=(20, 5), subplot_kw={"projection": "3d"})
    ```

    돌려 보면 예측대로 네 번째 그림에 $y = 0.5x$ 를 따라 아주 높고 가는 마루가 나타난다.

**연습문제 5.** 표준이변량정규분포($\mu_1 = \mu_2 = 0$, $\sigma_1 = \sigma_2 = 1$)에서 $X = x$ 가 주어졌을 때 $Y$ 의 조건부분포가 $N(\rho x, 1 - \rho^2)$ 임을 증명하여라.

??? success "풀이"
    결합밀도함수

    $$
    f(x, y) = \frac{1}{2\pi\sqrt{1-\rho^2}} \exp\!\left(-\frac{x^2 - 2\rho xy + y^2}{2(1-\rho^2)}\right)
    $$

    과 주변밀도함수 $f_X(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ 에서 출발하면 조건부밀도함수는 다음과 같다.

    $$
    f_{Y|X}(y \mid x) = \frac{f(x, y)}{f_X(x)}
    $$

    이 비의 지수부는 다음과 같이 된다.

    $$
    -\frac{x^2 - 2\rho xy + y^2}{2(1-\rho^2)} + \frac{x^2}{2}
    $$

    분모를 $2(1 - \rho^2)$ 로 통일하여 정리하면

    $$
    = \frac{-(x^2 - 2\rho xy + y^2) + x^2(1 - \rho^2)}{2(1-\rho^2)} = \frac{-\rho^2 x^2 + 2\rho xy - y^2}{2(1-\rho^2)} = -\frac{(y - \rho x)^2}{2(1-\rho^2)}
    $$

    를 얻는다. 정규화 상수는 $\frac{1}{\sqrt{2\pi(1-\rho^2)}}$ 이 되므로

    $$
    f_{Y|X}(y \mid x) = \frac{1}{\sqrt{2\pi(1-\rho^2)}} \exp\!\left(-\frac{(y - \rho x)^2}{2(1-\rho^2)}\right)
    $$

    이고, 이는 $N(\rho x, 1 - \rho^2)$ 의 밀도함수이다. $\square$

**연습문제 6.** $\rho = 1$ 인 이변량정규분포의 밀도함수를 제대로 만들 수 없는 까닭을 설명하여라. $\rho \to 1$ 일 때 밀도 곡면에는 기하적으로 무슨 일이 일어나는가?

??? success "풀이"
    $\rho = 1$ 이면 공분산행렬이

    $$
    \boldsymbol{\Sigma} = \begin{pmatrix} \sigma_1^2 & \sigma_1\sigma_2 \\ \sigma_1\sigma_2 & \sigma_2^2 \end{pmatrix}
    $$

    이 되고, 그 행렬식은 $\sigma_1^2\sigma_2^2 - \sigma_1^2\sigma_2^2 = 0$ 이다. $\boldsymbol{\Sigma}$ 가 특이행렬이어서 역행렬이 없으므로 이변량정규분포의 밀도함수 공식이 정의되지 않는다(정규화 상수에 들어 있는 $1/\sqrt{|\boldsymbol{\Sigma}|}$ 가 발산한다).

    기하적으로는 밀도 곡면이 직선 $Y - \mu_2 = \frac{\sigma_2}{\sigma_1}(X - \mu_1)$ 위의 1차원 마루로 찌부러진다. $\rho \to 1$ 이면 곡면이 점점 높고 가늘어지면서 확률이 모두 이 직선 위로 몰린다. 극한에서는 분포가 **퇴화**한다. 곧 $Y$ 가 $X$ 의 결정론적 일차함수가 되며, 이 "분포"는 2차원 르베그 측도에 대한 밀도함수로는 나타낼 수 없고 그 직선 위의 디랙 델타 측도로만 나타낼 수 있다. $\square$
