# 등고선과 기하적 해석

## 개요

이변량정규분포의 등고선 그림을 보면 **평균벡터**가 중심을 정하고 **공분산행렬**이 분포의 모양과 기울기와 퍼짐을 정한다는 것을 알 수 있다. 등고선을 이해하면 상관과 의존 관계를 기하적으로 바라보는 눈이 생긴다.

---

## 밀도가 일정한 등고선

이변량정규분포 밀도함수의 등고선은 밀도가 일정한 곡선이다. 어떤 상수 $c > 0$ 에 대하여 $f(x, y) = c$ 로 두는 것은 다음과 같다.

$$
(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) = k
$$

여기에서 $k > 0$ 은 상수이다. 이것은 $\boldsymbol{\mu}$ 를 중심으로 하는 **타원**의 방정식이다.

---

## 모수의 기하적 구실

### 평균벡터 μ

평균벡터 $\boldsymbol{\mu} = (\mu_X, \mu_Y)^T$ 는 타원 등고선의 **중심**을 정한다. $\boldsymbol{\mu}$ 를 바꾸면 모양은 그대로인 채 분포 전체가 평행이동한다.

### 분산 σX² 과 σY²

주변분산은 각 축 방향의 **퍼짐**을 정한다. $\sigma_X^2$ 이 클수록 타원이 가로로 늘어나고, $\sigma_Y^2$ 이 클수록 세로로 늘어난다.

### 상관계수 ρ

상관계수 $\rho$ 는 타원의 **기울기**와 **찌그러진 정도**를 정한다.

| $\rho$ | 모양 | 기울기 |
|:---:|:---|:---|
| $\rho = 0$ | 축이 좌표축과 나란함 | 기울지 않음 |
| $\rho > 0$ | $y = x$ 방향으로 기욺 | 양의 기울기 |
| $\rho < 0$ | $y = -x$ 방향으로 기욺 | 음의 기울기 |
| $\rho \to \pm 1$ | 타원이 직선으로 찌부러짐 | 완전한 일차 관계 |

---

## 고윳값으로 본 해석

등고선 타원의 축은 $\boldsymbol{\Sigma}$ 의 **고유벡터** 방향과 일치하고, 그 길이는 **고윳값**의 제곱근에 비례한다. 특히 표준이변량정규분포($\sigma_X = \sigma_Y = 1$)의 경우

$$
\boldsymbol{\Sigma} = \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}
$$

이고, 고윳값은 $\lambda_1 = 1 + \rho$ 와 $\lambda_2 = 1 - \rho$ 이며 고유벡터는 각각 $45°$ 와 $135°$ 방향이다. $|\rho| \to 1$ 이면 한 고윳값이 $0$ 으로 가면서 타원이 퇴화한다.

---

## 파이썬: 등고선 모음

다음 코드는 평균과 공분산행렬이 이변량정규분포에 어떤 영향을 주는지 보여 주는 등고선 그림들을 격자로 그린다. 상관계수 7가지와 평균벡터 4가지를 짜임새 있게 훑어보는 것이다.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

fig, axes = plt.subplots(7, 4, figsize=(14, 20))

means = [
    [0, 0],
    [1, 0],
    [2, 0],
    [2, 2],
]

rhos = [-0.9, -0.6, -0.3, 0.0, 0.3, 0.6, 0.9]

x = np.linspace(-5, 5, 200)
y = np.linspace(-4, 4, 200)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

for i, rho in enumerate(rhos):
    for j, mu in enumerate(means):
        Sigma = [[1, rho], [rho, 1]]
        rv = multivariate_normal(mean=mu, cov=Sigma)
        Z = rv.pdf(pos)

        ax = axes[i, j]
        ax.contour(X, Y, Z, levels=6)
        ax.set_xlim(-5, 5)
        ax.set_ylim(-4, 4)
        ax.set_aspect('equal')

        if i == 0:
            ax.set_title(f'μ = {mu}', fontsize=9)
        if j == 0:
            ax.set_ylabel(f'ρ = {rho}', fontsize=9)

        ax.tick_params(labelsize=6)

plt.suptitle('Bivariate Normal Contours: Varying Mean and Correlation',
             fontsize=14, y=1.01)
plt.tight_layout()
plt.show()
```

---

## 마할라노비스 거리

이차형식 $(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})$ 은 $\mathbf{x}$ 에서 $\boldsymbol{\mu}$ 까지의 **마할라노비스 거리**의 제곱이다. 같은 등고선 타원 위의 점들은 평균으로부터 마할라노비스 거리가 같다.

이변량인 경우 이 거리의 제곱은 $\chi^2(2)$ 분포를 따른다.

$$
(\mathbf{X} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{X} - \boldsymbol{\mu}) \sim \chi^2(2)
$$

따라서 마할라노비스 거리가 $\sqrt{k}$ 인 타원 안에 들어 있는 확률은 $P(\chi^2(2) \leq k) = 1 - e^{-k/2}$ 이다.

---

## 핵심 정리

- 이변량정규분포의 등고선은 $\boldsymbol{\mu}$ 를 중심으로 하는 **타원**이다.
- $\boldsymbol{\mu}$ 는 위치를, $\sigma_X, \sigma_Y$ 는 퍼짐을, $\rho$ 는 기울기와 찌그러진 정도를 정한다.
- 타원의 축은 $\boldsymbol{\Sigma}$ 의 고유벡터 방향과 나란하고 길이는 고윳값의 제곱근에 비례한다.
- 마할라노비스 거리는 척도에 영향받지 않는, 중심으로부터의 거리 재는 잣대를 준다.

## 연습문제

**연습문제 1.**
$\mu_X = \mu_Y = 0$, $\sigma_X = \sigma_Y = 1$ 이고 상관계수가 $\rho$ 인 표준이변량정규분포에 대하여 다음에 답하여라.

**(a)** 등고선 타원의 반축이 $(1, 1)^T / \sqrt{2}$ 와 $(1, -1)^T / \sqrt{2}$ 방향임을 보여라.

**(b)** $\boldsymbol{\Sigma}$ 의 고윳값을 $\rho$ 로 나타내어라.

**(c)** 등고선이 원이 되는 $\rho$ 의 값을 구하여라.

??? success "연습문제 1 풀이"
    **(a)** 공분산행렬은 $\boldsymbol{\Sigma} = \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}$ 이다. 고유벡터는 $(1, 1)^T/\sqrt{2}$ 와 $(1, -1)^T/\sqrt{2}$ 이다(직접 계산하여 확인할 수 있다).

    **(b)** $\lambda_1 = 1 + \rho$, $\lambda_2 = 1 - \rho$.

    **(c)** 등고선이 원이 되는 것은 $\lambda_1 = \lambda_2$ 일 때, 곧 $\rho = 0$ 일 때이다.
