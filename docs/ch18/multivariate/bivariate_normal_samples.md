# 이변량정규분포의 표본: 산점도

확률표본의 산점도는 이론적인 밀도함수를 경험적으로 뒷받침해 준다.
이변량정규분포에서 표본을 많이 뽑아 점으로 찍어 보면 타원 모양으로 모이는 모습, 두 변수가 함께 움직이는 방향, 각 축 방향의 퍼짐을 자료에서 바로 볼 수 있다.
이 절에서는 양의 상관이 강한 이변량정규분포에서 표본 500개를 뽑아 산점도로 그리는 코드를 소개한다.

## 배경

$(X, Y)^T \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ 이고

$$
\boldsymbol{\mu} = \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \qquad \boldsymbol{\Sigma} = \begin{pmatrix} \sigma_1^2 & \rho\,\sigma_1\sigma_2 \\ \rho\,\sigma_1\sigma_2 & \sigma_2^2 \end{pmatrix}
$$

이라고 하자.

표본을 만드는 표준적인 방법은 **촐레스키 분해**이다. $\boldsymbol{\Sigma} = \mathbf{L}\mathbf{L}^T$ 로 분해하여 $\mathbf{L}$ 을 아래삼각행렬로 잡고, $\mathbf{z} \sim N(\mathbf{0}, \mathbf{I})$ 에 대하여 $\mathbf{x} = \boldsymbol{\mu} + \mathbf{L}\mathbf{z}$ 로 두는 것이다. 실제로는 `scipy.stats.multivariate_normal` 이 이 일을 속으로 해 준다.

$\rho > 0$ 이면 점들이 기울기가 양수인 타원을 따라 모이고, $\rho < 0$ 이면 타원이 반대쪽으로 기운다. 표준이변량정규분포($\sigma_1 = \sigma_2 = 1$)에서 $p$ 분위수에 해당하는 **집중타원**의 반축은 $\sqrt{\lambda_i \chi^2_2(p)}$ 에 비례하며, 여기에서 $\lambda_1 = 1 + \rho$ 와 $\lambda_2 = 1 - \rho$ 는 $\boldsymbol{\Sigma}$ 의 고윳값이다.

아래 코드는 $\mu_1 = \mu_2 = 0$, $\sigma_1 = \sigma_2 = 1$, $\rho = 0.8$ 로 두고 $n = 500$ 개의 표본을 뽑는다.

## 코드

```python
"""이변량정규분포에서 뽑은 표본의 산점도."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

mu1, mu2 = 0, 0
sigma1, sigma2 = 1, 1
rho = 0.8

cov = [[sigma1**2, rho * sigma1 * sigma2],
       [rho * sigma1 * sigma2, sigma2**2]]
samples = stats.multivariate_normal([mu1, mu2], cov).rvs(500)

fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(samples[:, 0], samples[:, 1], alpha=0.5, s=15)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title(f"Bivariate Normal Samples (ρ = {rho})")
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("bivariate_normal_samples.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 실행 결과

이 코드는 $\rho = 0.8$ 인 이변량정규분포에서 뽑은 500개의 점을 찍은 산점도 하나를 만들어 낸다. 점들은 원점을 중심으로 오른쪽 위로 기울어진, 뚜렷하게 길쭉한 구름을 이룬다. 대부분의 점이 각 방향으로 대략 표준편차 $\pm 2$ 안에 들어 있으며, 구름의 장축은 두 변수가 함께 커지는 방향으로 놓인다. 두 축의 비율을 같게 맞추고 옅은 격자선을 넣었기에 타원 모양이 한눈에 들어온다.

## 뜻풀이

이 산점도는 이변량정규분포의 중요한 성질 몇 가지를 드러내 준다.

1. **타원 모양.** 표본이 이루는 구름이 타원 꼴을 그린다. 이변량정규분포 밀도함수의 등고선이 타원이라는 사실이 그대로 나타난 것이다. $\rho = 0.8$ 이므로 타원이 눈에 띄게 길쭉하다.

2. **함께 움직이는 방향.** 타원의 장축이 왼쪽 아래에서 오른쪽 위로 향한다. 양의 상관, 곧 $X$ 가 클 때 $Y$ 도 큰 경향을 확인해 준다.

3. **주변분포의 정규성.** 점들을 어느 한 축에 내리쏘면 대략 $N(0, 1)$ 을 따르는 표본이 된다. 이변량정규분포의 주변분포가 정규분포라는 이론과 들어맞는다.

4. **밀도의 쏠림.** 점들은 원점(평균) 가까이에서 가장 빽빽하고 가장자리로 갈수록 성기어진다. 종 모양 밀도 곡면을 그대로 비추는 모습이다.

5. **표본의 흔들림.** $\rho = 0.8$ 이 강한 상관이기는 하지만 개별 점들은 회귀직선 $Y = \rho X = 0.8X$ 에서 꽤 많이 벗어날 수 있다. 조건부분산이 $1 - \rho^2 = 0.36$ 이므로 조건부표준편차는 $0.6$ 이다.

## 연습문제

**연습문제 1.** 표본상관계수는 $r = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2 \sum_{i=1}^n (y_i - \bar{y})^2}}$ 이다. 위 코드에 500개의 표본에서 $r$ 을 계산하여 출력하는 줄을 덧붙여라. $r$ 은 참값 $\rho = 0.8$ 에 얼마나 가까운가?

??? success "풀이"
    표본을 뽑는 줄 뒤에 다음을 덧붙인다.

    ```python
    r = np.corrcoef(samples[:, 0], samples[:, 1])[0, 1]
    print(f"Sample correlation: {r:.4f}")
    ```

    씨앗값 `42` 와 $n = 500$ 에서는 출력이 대략 $r \approx 0.80$ 이다. 표본상관계수의 점근이론에 따르면 $n$ 이 클 때 $r$ 은 대략 $N\!\left(\rho, \frac{(1-\rho^2)^2}{n}\right)$ 을 따르므로 표준오차가 약 $\frac{1-0.64}{\sqrt{500}} \approx 0.016$ 이다. 따라서 $r$ 은 보통 $[0.77, 0.83]$ 안에 들어온다.

**연습문제 2.** 코드를 고쳐 $\rho \in \{-0.9, 0, 0.5, 0.9\}$ 에 대한 산점도를 $2 \times 2$ 격자로 그려라. 네 값에 걸쳐 점 구름의 모양이 어떻게 달라지는지 말하여라.

??? success "풀이"
    ```python
    rhos = [-0.9, 0, 0.5, 0.9]
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    for ax, rho in zip(axes.flat, rhos):
        cov = [[1, rho], [rho, 1]]
        samp = stats.multivariate_normal([0, 0], cov).rvs(500)
        ax.scatter(samp[:, 0], samp[:, 1], alpha=0.5, s=15)
        ax.set_title(f"ρ = {rho}")
        ax.set_aspect("equal")
        ax.set_xlim(-4, 4)
        ax.set_ylim(-4, 4)
        ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    ```

    - $\rho = -0.9$: 왼쪽 위에서 오른쪽 아래로 기울어진(기울기가 음수인) 좁은 타원.
    - $\rho = 0$: 특정한 방향 없이 거의 원에 가까운 구름.
    - $\rho = 0.5$: 오른쪽 위로 기울어진 적당히 길쭉한 타원.
    - $\rho = 0.9$: 오른쪽 위로 기울어진 아주 좁고 가는 타원으로 거의 직선에 가깝다.

**연습문제 3.** 상관계수가 $\rho$ 인 표준이변량정규분포에서 공분산행렬의 고윳값이 $\lambda_1 = 1 + \rho$ 와 $\lambda_2 = 1 - \rho$ 임을 증명하여라. 이를 써서 $|\rho| \to 1$ 일 때 산점도가 왜 더 길쭉해지는지 설명하여라.

??? success "풀이"
    공분산행렬은 다음과 같다.

    $$
    \boldsymbol{\Sigma} = \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}
    $$

    특성방정식은

    $$
    \det(\boldsymbol{\Sigma} - \lambda \mathbf{I}) = (1-\lambda)^2 - \rho^2 = 0
    $$

    이므로 $1 - \lambda = \pm \rho$ 이고, 따라서 $\lambda_1 = 1 + \rho$, $\lambda_2 = 1 - \rho$ 이다.

    집중타원의 두 반축의 비는 $\sqrt{\lambda_1 / \lambda_2} = \sqrt{(1+\rho)/(1-\rho)}$ 이다. $|\rho| \to 1$ 이면 한 고윳값은 $2$ 로, 다른 하나는 $0$ 으로 가므로 이 비가 발산한다. 곧 타원이 선분으로 퇴화해 가며, 산점도는 구름이라기보다 좁은 띠처럼 보이게 된다. $\square$

**연습문제 4.** $(X, Y)$ 가 $\rho = 0.8$ 인 표준이변량정규분포를 따른다고 하자. $P(X > 0, Y > 0)$ 을 구하여라.

??? success "풀이"
    평균이 원점인 표준이변량정규분포에서 **사분면 확률** $P(X > 0, Y > 0)$ 은 다음과 같이 주어진다.

    $$
    P(X > 0, Y > 0) = \frac{1}{4} + \frac{\arcsin(\rho)}{2\pi}
    $$

    이것은 고전적인 결과이다. $\rho = 0.8$ 이면

    $$
    P(X > 0, Y > 0) = \frac{1}{4} + \frac{\arcsin(0.8)}{2\pi} = 0.25 + \frac{0.9273}{6.2832} \approx 0.25 + 0.1476 = 0.3976
    $$

    이다. 표본의 약 40%가 제1사분면에 들어간다는 뜻이며, 산점도에서 보이는 모습(양의 상관이 점들을 제1, 제3사분면 쪽으로 밀어 놓는다)과 들어맞는다.

**연습문제 5.** $(X, Y)$ 가 상관계수 $\rho$ 인 표준이변량정규분포를 따를 때 $U = X + Y$, $V = X - Y$ 로 두자. $(U, V)$ 의 결합분포를 구하고, $U$ 와 $V$ 가 독립이 되는 $\rho$ 의 값을 구하여라.

??? success "풀이"
    $(X, Y)^T \sim N(\mathbf{0}, \boldsymbol{\Sigma})$ 이므로 어떤 일차변환을 하여도 다시 이변량정규분포가 된다.

    $$
    \begin{pmatrix} U \\ V \end{pmatrix} = \mathbf{A} \begin{pmatrix} X \\ Y \end{pmatrix}, \qquad \mathbf{A} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
    $$

    로 두면 새 공분산행렬은 다음과 같다.

    $$
    \boldsymbol{\Sigma}_{UV} = \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^T = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
    $$

    계산하면

    $$
    \mathbf{A}\boldsymbol{\Sigma} = \begin{pmatrix} 1+\rho & 1+\rho \\ 1-\rho & \rho-1 \end{pmatrix}
    $$

    $$
    \boldsymbol{\Sigma}_{UV} = \begin{pmatrix} 2(1+\rho) & 0 \\ 0 & 2(1-\rho) \end{pmatrix}
    $$

    이므로 $(U, V)^T \sim N\!\left(\mathbf{0}, \begin{pmatrix} 2(1+\rho) & 0 \\ 0 & 2(1-\rho) \end{pmatrix}\right)$ 이다.

    비대각 성분이 $\rho$ 의 값과 상관없이 $0$ 이므로 $U$ 와 $V$ 는 **언제나 독립**이다. $\operatorname{Cov}(U, V) = \operatorname{Var}(X) - \operatorname{Var}(Y) = 1 - 1 = 0$ 이고, 함께 정규분포를 따르는 확률변수에서는 공분산이 $0$ 이면 독립이기 때문이다. $\square$
