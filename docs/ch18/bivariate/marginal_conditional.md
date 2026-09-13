# 주변분포와 조건부분포

## 개요

이변량정규분포가 지닌 가장 강력한 성질 가운데 하나는 **주변분포**와 **조건부분포**가 모두 다시 정규분포라는 점이다. 게다가 조건부분포는 아름다운 기하적 뜻을 지닌 간단한 닫힌 꼴로 주어진다. $Y = y$ 로 조건을 걸면 종 모양 곡면을 한 번 "잘라 내는" 셈이 되며, 그렇게 얻은 단면이 다시 정규분포이고 그 평균은 $y$ 에 대하여 일차로 옮겨 간다.

---

## 주변분포

$(X, Y)^T \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ 이고

$$
\boldsymbol{\mu} = \begin{pmatrix} \mu_X \\ \mu_Y \end{pmatrix}, \qquad
\boldsymbol{\Sigma} = \begin{pmatrix} \sigma_X^2 & \rho\sigma_X\sigma_Y \\ \rho\sigma_X\sigma_Y & \sigma_Y^2 \end{pmatrix}
$$

이면 주변분포는 다음과 같다.

$$
X \sim N(\mu_X, \sigma_X^2), \qquad Y \sim N(\mu_Y, \sigma_Y^2)
$$

주변분포는 공분산행렬의 대각선을 그대로 "읽어 오면" 된다. 상관계수 $\rho$ 는 주변분포에 나타나지 않는다. 두 변수가 함께 움직이는 방식에만 관여하기 때문이다.

!!! warning "역은 성립하지 않는다"
    각각의 주변분포가 정규분포라고 해서 결합분포가 이변량정규분포인 것은 **아니다**. $X$ 와 $Y = SX$ 가 각각은 정규분포를 따르지만 함께는 정규분포를 따르지 않는 [반례](uncorrelated_independent.md)를 보라.

---

## 조건부분포: Y = y 가 주어졌을 때의 X

$Y = y$ 가 주어졌을 때 $X$ 의 조건부분포는 다음과 같다.

$$
X \mid Y = y \;\sim\; N\!\left(\mu_{X|Y},\; \sigma_{X|Y}^2\right)
$$

여기에서

$$
\mu_{X|Y} = \mu_X + \rho\frac{\sigma_X}{\sigma_Y}(y - \mu_Y)
$$

$$
\sigma_{X|Y}^2 = \sigma_X^2(1 - \rho^2)
$$

이다.

### 뜻풀이

- **조건부평균** $\mu_{X|Y}$: 이것은 **회귀함수** $E[X \mid Y = y]$ 이며 $y$ 에 대한 일차함수이다. 기울기 $\rho \cdot \sigma_X / \sigma_Y$ 는 $y$ 가 한 단위 바뀔 때 조건부평균이 얼마나 옮겨 가는지를 말해 준다.
- **조건부분산** $\sigma_{X|Y}^2$: 이것은 **상수**이며 $y$ 에 따라 달라지지 않는다. 인자 $(1 - \rho^2)$ 는 $Y$ 를 알게 됨으로써 $X$ 에 대한 불확실성이 얼마나 줄어드는지를 보여 준다. $|\rho| = 1$ 이면 조건부분산이 $0$ 이 되어 완전히 예측할 수 있다.

대칭성에 따라 $X = x$ 가 주어졌을 때 $Y$ 의 조건부분포는 다음과 같다.

$$
Y \mid X = x \;\sim\; N\!\left(\mu_Y + \rho\frac{\sigma_Y}{\sigma_X}(x - \mu_X),\; \sigma_Y^2(1 - \rho^2)\right)
$$

---

## 완전제곱 만들기를 이용한 유도

표준화한 좌표 $\tilde{x} = (x - \mu_X)/\sigma_X$ 와 $\tilde{y} = (y - \mu_Y)/\sigma_Y$ 로 쓴 결합밀도함수에서 출발한다.

$$
f(x, y) \propto \exp\left(-\frac{\tilde{x}^2 + \tilde{y}^2 - 2\rho\tilde{x}\tilde{y}}{2(1 - \rho^2)}\right)
$$

$f(x \mid y)$ 를 구하려면 $\tilde{y}$ 를 고정된 값으로 보고 $\tilde{x}$ 에 대한 항을 모은다.

$$
\tilde{x}^2 - 2\rho\tilde{y}\tilde{x} = (\tilde{x} - \rho\tilde{y})^2 - \rho^2\tilde{y}^2
$$

$\rho^2\tilde{y}^2$ 항은 $y$ 에만 의존하므로 정규화 상수 안으로 흡수되고, 다음을 얻는다.

$$
f(x \mid y) \propto \exp\left(-\frac{(\tilde{x} - \rho\tilde{y})^2}{2(1 - \rho^2)}\right)
$$

원래 척도로 되돌리면

$$
x - \mu_X - \rho\frac{\sigma_X}{\sigma_Y}(y - \mu_Y) \sim N\!\left(0,\; \sigma_X^2(1 - \rho^2)\right)
$$

가 되어 위의 조건부분포 공식을 얻는다.

---

## 선형회귀와의 관계

조건부기댓값 $E[X \mid Y = y] = \mu_X + \rho(\sigma_X/\sigma_Y)(y - \mu_Y)$ 는 $Y$ 가 주어졌을 때 $X$ 의 **최량선형예측량**과 정확히 같다. 이변량정규분포에서는 이 일차 예측량이 선형인 것들 가운데 가장 좋은 데 그치지 않고 **모든 예측량 가운데 가장 좋은 것**이다.

회귀계수는 다음과 같다.

$$
\beta = \rho \cdot \frac{\sigma_X}{\sigma_Y} = \frac{\text{Cov}(X, Y)}{\text{Var}(Y)}
$$

이것은 최소제곱법(OLS)의 기울기 계수와 그대로 이어진다.

---

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal, norm

# 모수
mu_x, mu_y = 1, 2
sigma_x, sigma_y = 2, 1.5
rho = 0.7

# 이변량정규분포에서 표본을 뽑는다
mu = [mu_x, mu_y]
Sigma = [[sigma_x**2, rho * sigma_x * sigma_y],
         [rho * sigma_x * sigma_y, sigma_y**2]]

np.random.seed(42)
samples = np.random.multivariate_normal(mu, Sigma, 2000)

# Y = y_given 일 때의 조건부분포 모수
y_given = 3.0
mu_cond = mu_x + rho * (sigma_x / sigma_y) * (y_given - mu_y)
sigma_cond = sigma_x * np.sqrt(1 - rho**2)

print(f"Conditional distribution X | Y={y_given}:")
print(f"  Mean: {mu_cond:.4f}")
print(f"  Std:  {sigma_cond:.4f}")

# 그림 그리기
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 왼쪽: 결합분포와 조건부 단면
ax = axes[0]
ax.scatter(samples[:, 0], samples[:, 1], s=2, alpha=0.3, label='Samples')
ax.axhline(y=y_given, color='red', linestyle='--', label=f'Y = {y_given}')
x_line = np.linspace(mu_x - 3*sigma_x, mu_x + 3*sigma_x, 100)
regression_line = mu_x + rho * (sigma_x / sigma_y) * (x_line - mu_x)  # E[Y|X=x]
# 회귀직선으로는 E[X|Y=y] 를 그린다
y_range = np.linspace(mu_y - 3*sigma_y, mu_y + 3*sigma_y, 100)
e_x_given_y = mu_x + rho * (sigma_x / sigma_y) * (y_range - mu_y)
ax.plot(e_x_given_y, y_range, 'g-', linewidth=2, label='E[X|Y=y]')
ax.plot(mu_cond, y_given, 'ro', markersize=8, zorder=5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Joint Distribution with Conditional Slice')
ax.legend(fontsize=8)

# 오른쪽: 조건부밀도함수
ax = axes[1]
x_vals = np.linspace(mu_cond - 4*sigma_cond, mu_cond + 4*sigma_cond, 200)
cond_pdf = norm.pdf(x_vals, mu_cond, sigma_cond)
ax.plot(x_vals, cond_pdf, 'b-', linewidth=2)
ax.fill_between(x_vals, cond_pdf, alpha=0.2)
ax.axvline(mu_cond, color='red', linestyle='--', label=f'E[X|Y={y_given}] = {mu_cond:.2f}')
ax.set_xlabel('X')
ax.set_ylabel('Density')
ax.set_title(f'Conditional Distribution X | Y = {y_given}')
ax.legend()

plt.tight_layout()
plt.show()
```

---

## 핵심 정리

- 이변량정규분포의 주변분포는 정규분포이며, 그 모수는 $\boldsymbol{\mu}$ 와 $\boldsymbol{\Sigma}$ 의 대각선에서 바로 읽어 온다.
- 조건부분포 $X \mid Y = y$ 는 정규분포이고, 평균은 $y$ 에 대하여 일차로 옮겨 가지만 분산은 $y$ 와 무관한 상수이다.
- 조건부평균은 회귀함수이고, 조건부분산은 조건을 걸고 난 뒤에 남은 불확실성의 크기이다.
- 인자 $(1 - \rho^2)$ 는 조건을 거는 변수가 "설명해 주지 못하고" 남긴 분산의 몫을 재어 준다.

## 연습문제

**연습문제 1.**
$X \sim N(0, 4)$ 이고 $Y = 2X + 1 + \varepsilon$ 이라고 하자. 여기에서 $\varepsilon \sim N(0, 1)$ 은 $X$ 와 독립이다.

**(a)** $(X, Y)^T$ 의 결합분포를 구하여라.

**(b)** $Y$ 의 주변분포를 구하여라.

**(c)** 사후분포 $X \mid Y = 5$ 를 구하여라.

**(d)** 사후 정밀도와 사후평균을 정밀도 꼴로 나타내어라.

??? success "연습문제 1 풀이"
    **(a)** $A = 2$, $b = 1$, $\Sigma_x = 4$, $\Sigma_\varepsilon = 1$ 이므로

    $(X, Y)^T \sim N\!\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 4 & 8 \\ 8 & 17 \end{pmatrix}\right)$

    **(b)** $Y \sim N(1, 4 \cdot 4 + 1) = N(1, 17)$.

    **(c)** $\mu_{X|Y} = 0 + \frac{8}{17}(5 - 1) = \frac{32}{17} \approx 1.882$

    $\Sigma_{X|Y} = 4 - \frac{64}{17} = \frac{4}{17} \approx 0.235$

    따라서 $X \mid Y = 5 \sim N(32/17,\; 4/17)$ 이다.

    **(d)** 사후 정밀도: $\Sigma_{X|Y}^{-1} = \frac{1}{4} + \frac{4}{1} = \frac{17}{4}$

    사후평균: $\Sigma_{X|Y}(\Sigma_x^{-1}\mu_x + A^T\Sigma_\varepsilon^{-1}(y - b)) = \frac{4}{17}(0 + 2 \cdot 4) = \frac{32}{17}$ $\checkmark$
