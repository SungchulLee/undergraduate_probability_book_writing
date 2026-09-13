# 이변량정규분포의 결합밀도함수

## 개요

**이변량정규분포**는 가장 단순한 다변량정규분포이다. 두 확률변수 $X$ 와 $Y$ 의 결합분포이며, 둘 사이의 의존 구조는 두 평균, 두 표준편차, 그리고 상관계수라는 다섯 개의 모수만으로 완전히 정해진다.

---

## 행렬로 쓴 밀도함수

$\mathbf{x} = (x, y)^T$ 가 이변량정규분포 $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ 를 따르면 결합밀도함수는 다음과 같다.

$$
f(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^2 |\boldsymbol{\Sigma}|}} \exp\left(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})\right)
$$

여기에서

- $\boldsymbol{\mu} = (\mu_X, \mu_Y)^T$ 는 **평균벡터**이다
- $\boldsymbol{\Sigma}$ 는 $2 \times 2$ **공분산행렬**이다
- $|\boldsymbol{\Sigma}|$ 는 $\boldsymbol{\Sigma}$ 의 **행렬식**이다

---

## 공분산행렬과 그 역행렬

이변량인 경우 공분산행렬은 다음과 같다.

$$
\boldsymbol{\Sigma} = \begin{pmatrix} \sigma_X^2 & \rho\sigma_X\sigma_Y \\ \rho\sigma_X\sigma_Y & \sigma_Y^2 \end{pmatrix}
$$

행렬식은 다음과 같고

$$
|\boldsymbol{\Sigma}| = \sigma_X^2 \sigma_Y^2 (1 - \rho^2)
$$

역행렬은 다음과 같다.

$$
\boldsymbol{\Sigma}^{-1} = \frac{1}{(1 - \rho^2)\sigma_X^2 \sigma_Y^2} \begin{pmatrix} \sigma_Y^2 & -\rho\sigma_X\sigma_Y \\ -\rho\sigma_X\sigma_Y & \sigma_X^2 \end{pmatrix}
$$

$|\boldsymbol{\Sigma}| > 0$ 이려면 $|\rho| < 1$ 이어야 함에 주의한다. $\rho = \pm 1$ 이면 분포는 평면 위의 한 직선으로 찌부러진다.

---

## 성분으로 풀어 쓴 꼴

표준화한 변수 $\tilde{x} = \frac{x - \mu_X}{\sigma_X}$ 와 $\tilde{y} = \frac{y - \mu_Y}{\sigma_Y}$ 를 들여오면 지수부의 이차형식은 다음과 같이 된다.

$$
(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) = \frac{\tilde{x}^2 + \tilde{y}^2 - 2\rho\tilde{x}\tilde{y}}{1 - \rho^2}
$$

따라서 밀도함수를 다음과 같이 풀어 쓸 수 있다.

$$
f(x, y) = \frac{1}{2\pi\sigma_X\sigma_Y\sqrt{1 - \rho^2}} \exp\left(-\frac{\tilde{x}^2 + \tilde{y}^2 - 2\rho\tilde{x}\tilde{y}}{2(1 - \rho^2)}\right)
$$

---

## 특별한 경우: 두 성분이 독립일 때 (ρ = 0)

$X$ 와 $Y$ 가 독립이면, 곧 $\rho = 0$ 이면 교차항이 사라지고 밀도함수가 다음과 같이 인수분해된다.

$$
f(x, y) = \frac{1}{2\pi\sigma_X\sigma_Y} \exp\left(-\frac{\tilde{x}^2 + \tilde{y}^2}{2}\right) = \underbrace{\frac{1}{\sqrt{2\pi}\sigma_X} e^{-\tilde{x}^2/2}}_{f_X(x)} \cdot \underbrace{\frac{1}{\sqrt{2\pi}\sigma_Y} e^{-\tilde{y}^2/2}}_{f_Y(y)}
$$

이 인수분해는 이변량정규분포에서는 $\rho = 0$ 이 곧 독립을 뜻한다는 사실을 확인해 준다.

---

## 특별한 경우: 표준이변량정규분포

$\mu_X = \mu_Y = 0$ 이고 $\sigma_X = \sigma_Y = 1$ 이면 다음과 같다.

$$
f(x, y) = \frac{1}{2\pi\sqrt{1 - \rho^2}} \exp\left(-\frac{x^2 + y^2 - 2\rho xy}{2(1 - \rho^2)}\right)
$$

---

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

def bivariate_normal_pdf(x, y, mu_x=0, mu_y=0, sigma_x=1, sigma_y=1, rho=0):
    """이변량정규분포의 밀도함수를 직접 계산한다."""
    x_tilde = (x - mu_x) / sigma_x
    y_tilde = (y - mu_y) / sigma_y
    z = (x_tilde**2 + y_tilde**2 - 2 * rho * x_tilde * y_tilde) / (1 - rho**2)
    return np.exp(-z / 2) / (2 * np.pi * sigma_x * sigma_y * np.sqrt(1 - rho**2))

# 이변량정규분포의 밀도함수를 그린다
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)

for ax, rho, title in zip(axes, [0, 0.7, -0.7],
                           ['ρ = 0', 'ρ = 0.7', 'ρ = −0.7']):
    Z = bivariate_normal_pdf(X, Y, rho=rho)
    ax.contourf(X, Y, Z, levels=20, cmap='Blues')
    ax.contour(X, Y, Z, levels=8, colors='navy', linewidths=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(title)
    ax.set_aspect('equal')

plt.suptitle('Standard Bivariate Normal PDF', y=1.02)
plt.tight_layout()
plt.show()
```

### 곡면 그림

```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = bivariate_normal_pdf(X, Y, rho=0.5)

ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')
ax.set_title('Bivariate Normal PDF (ρ = 0.5)')
plt.tight_layout()
plt.show()
```

---

## 핵심 정리

- 이변량정규분포는 $\mu_X, \mu_Y, \sigma_X, \sigma_Y, \rho$ 라는 다섯 개의 모수로 결정된다.
- 행렬로 쓴 꼴 $f(\mathbf{x}) \propto \exp\left(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})\right)$ 은 그대로 더 높은 차원으로 확장된다.
- $\rho = 0$ 이면 결합밀도함수가 주변밀도함수의 곱으로 쪼개지며, 이는 독립임을 확인해 준다.
- 분포가 찌부러지지 않으려면 공분산행렬이 양정치여야 한다($|\rho| < 1$).

## 연습문제

**연습문제 1.**
$(X, Y)^T \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ 이고 $\mu_X = 1$, $\mu_Y = -1$, $\sigma_X = 2$, $\sigma_Y = 3$, $\rho = 0.5$ 라고 하자.

**(a)** 공분산행렬 $\boldsymbol{\Sigma}$ 를 적고 그 행렬식과 역행렬을 구하여라.

**(b)** $f(1, -1)$ 을 구하여라(평균에서의 밀도).

**(c)** 조건부분포 $X \mid Y = 2$ 를 구하여라.

??? success "연습문제 1 풀이"
    **(a)**

    $$
    \boldsymbol{\Sigma} = \begin{pmatrix} 4 & 3 \\ 3 & 9 \end{pmatrix}, \quad |\boldsymbol{\Sigma}| = 36 - 9 = 27
    $$

    $$
    \boldsymbol{\Sigma}^{-1} = \frac{1}{27}\begin{pmatrix} 9 & -3 \\ -3 & 4 \end{pmatrix}
    $$

    **(b)** $\mathbf{x} = \boldsymbol{\mu}$ 에서는 지수부가 $0$ 이므로

    $$
    f(1, -1) = \frac{1}{2\pi\sqrt{27}} = \frac{1}{2\pi \cdot 3\sqrt{3}} \approx 0.0307
    $$

    **(c)**

    $$
    \mu_{X|Y} = 1 + 0.5 \cdot \frac{2}{3}(2 - (-1)) = 1 + 1 = 2
    $$

    $$
    \sigma_{X|Y}^2 = 4(1 - 0.25) = 3
    $$

    따라서 $X \mid Y = 2 \sim N(2, 3)$ 이다.
