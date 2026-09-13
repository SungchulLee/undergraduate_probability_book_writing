# 촐레스키 분해로 확률표본 만들기

## 개요

실제로는 평균과 공분산을 정해 놓고 그에 맞는 다변량정규분포에서 확률표본을 뽑아야 할 때가 많다. 표준적인 방법은 공분산행렬의 **촐레스키 분해**를 써서 독립인 표준정규확률변수들을 서로 상관이 있는 다변량정규확률벡터로 바꾸는 것이다.

---

## 촐레스키 분해

대칭이고 양정치인 행렬 $\boldsymbol{\Sigma}$ 는 언제나 다음과 같이 분해된다.

$$
\boldsymbol{\Sigma} = LL^T
$$

여기에서 $L$ 은 대각성분이 모두 양수인 **아래삼각행렬**이다. 이를 **촐레스키 분해**라고 한다($U = L^T$ 를 위삼각행렬이라 하고 $\boldsymbol{\Sigma} = U^T U$ 로 써도 같은 말이다).

촐레스키 분해는 다음과 같은 성질을 지닌다.

- 양정치행렬에 대하여 유일하다
- 수치적으로 안정하고 빠르다: 연산량이 $O(d^3/3)$ 이다
- 양정치행렬의 "제곱근"에 해당한다

---

## 알고리즘

**1단계.** 촐레스키 분해 $L = \text{chol}(\boldsymbol{\Sigma})$ 를 구하여 $\boldsymbol{\Sigma} = LL^T$ 가 되게 한다.

**2단계.** $z_k \overset{\text{iid}}{\sim} N(0, 1)$ 인 $\mathbf{z} = (z_1, \ldots, z_d)^T$ 를 만든다.

**3단계.** 다음과 같이 둔다.

$$
\mathbf{x} = \boldsymbol{\mu} + L\mathbf{z}
$$

### 확인

**평균:**

$$
E[\mathbf{x}] = E[\boldsymbol{\mu} + L\mathbf{z}] = \boldsymbol{\mu} + L \cdot E[\mathbf{z}] = \boldsymbol{\mu} + L\mathbf{0} = \boldsymbol{\mu}
$$

**공분산:**

$$
E[(\mathbf{x} - \boldsymbol{\mu})(\mathbf{x} - \boldsymbol{\mu})^T] = E[(L\mathbf{z})(L\mathbf{z})^T] = L \cdot E[\mathbf{z}\mathbf{z}^T] \cdot L^T = LIL^T = LL^T = \boldsymbol{\Sigma}
$$

---

## 구성적 정의와의 관계

이는 구성적 정의 $\mathbf{x} = A\mathbf{z} + \boldsymbol{\mu}$ 에서 $A = L$ 로 잡은 것일 뿐이다. 촐레스키 분해는 $AA^T = \boldsymbol{\Sigma}$ 를 만족하는 $A$ 를 구체적이고 효율적으로 고르는 한 방법이다.

!!! note "다른 분해들"
    $AA^T = \boldsymbol{\Sigma}$ 를 만족하는 행렬 $A$ 라면 무엇이든 쓸 수 있다(이를테면 고윳값분해 $\boldsymbol{\Sigma} = Q\Lambda Q^T$ 에서 $A = Q\Lambda^{1/2}$ 로 잡아도 된다). 그럼에도 촐레스키 분해를 즐겨 쓰는 까닭은 계산이 빠르고 수치적으로 안정하기 때문이다.

---

## 파이썬 구현

### 기본 표집

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# 모수
mu = np.array([1, 2])
Sigma = np.array([[3, 2],
                   [2, 5]])

# 방법 1: 촐레스키 분해를 직접 쓰기
L = np.linalg.cholesky(Sigma)
n = 1000
z = np.random.randn(2, n)
x = mu[:, np.newaxis] + L @ z

print("Cholesky factor L:")
print(L)
print(f"\nL @ L^T:\n{L @ L.T}")
print(f"Sigma:\n{Sigma}")

# 방법 2: numpy 내장 함수 쓰기(속으로는 촐레스키 분해를 쓴다)
x2 = np.random.multivariate_normal(mu, Sigma, n).T

# 표본통계량 견주기
print(f"\n--- Method 1 (Cholesky) ---")
print(f"Sample mean: {x.mean(axis=1)}")
print(f"Sample cov:\n{np.cov(x)}")

print(f"\n--- Method 2 (numpy built-in) ---")
print(f"Sample mean: {x2.mean(axis=1)}")
print(f"Sample cov:\n{np.cov(x2)}")
```

### 그림으로 보기: 세 가지 경우

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 그림 1: 표준정규분포에서 뽑은 표본
n = 100
z = np.random.randn(2, n)
axes[0].plot(z[0], z[1], 'o', markersize=4)
axes[0].set_title('100 Standard Normal Samples')
axes[0].set_xlabel('$z_1$')
axes[0].set_ylabel('$z_2$')
axes[0].set_aspect('equal')
axes[0].grid(True, alpha=0.3)

# 그림 2: N(μ, Σ) 에서 뽑은 표본
mu1 = np.array([1, 2])
Sigma1 = np.array([[3, 2], [2, 5]])
L1 = np.linalg.cholesky(Sigma1)
x1 = mu1[:, np.newaxis] + L1 @ np.random.randn(2, n)
axes[1].plot(x1[0], x1[1], 'o', markersize=4)
axes[1].set_title(r'100 Samples from $N(\mu, \Sigma)$')
axes[1].set_xlabel('$x_1$')
axes[1].set_ylabel('$x_2$')
axes[1].grid(True, alpha=0.3)

# 그림 3: 서로 다른 두 분포에서 나온 두 무리
n1, n2 = 50, 40
mu_a = np.array([1, 2])
Sigma_a = np.array([[3, 2], [2, 5]])
L_a = np.linalg.cholesky(Sigma_a)
x_a = mu_a[:, np.newaxis] + L_a @ np.random.randn(2, n1)

mu_b = np.array([9, 7])
Sigma_b = np.array([[3, 1], [2, 3]])
# 촐레스키 분해를 쓰려면 Sigma_b 가 대칭이어야 한다
Sigma_b_sym = (Sigma_b + Sigma_b.T) / 2
L_b = np.linalg.cholesky(Sigma_b_sym)
x_b = mu_b[:, np.newaxis] + L_b @ np.random.randn(2, n2)

axes[2].plot(x_a[0], x_a[1], 'bo', markersize=4, label=r'$N(\mu_1, \Sigma_1)$')
axes[2].plot(x_b[0], x_b[1], 'ro', markersize=4, label=r'$N(\mu_2, \Sigma_2)$')
axes[2].set_title('Two Multivariate Normal Clusters')
axes[2].set_xlabel('$x_1$')
axes[2].set_ylabel('$x_2$')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### 더 높은 차원

```python
import numpy as np

np.random.seed(42)

# 5차원 다변량정규분포
d = 5
mu = np.arange(1, d + 1, dtype=float)

# 무작위 인자로 제대로 된 공분산행렬을 만든다
A_random = np.random.randn(d, d)
Sigma = A_random @ A_random.T + np.eye(d)  # 양정치가 되도록 한다

# 표본을 만든다
L = np.linalg.cholesky(Sigma)
n = 10_000
z = np.random.randn(d, n)
x = mu[:, np.newaxis] + L @ z

print(f"True mean: {mu}")
print(f"Sample mean: {x.mean(axis=1).round(2)}")
print(f"\nMax abs error in covariance: {np.max(np.abs(np.cov(x) - Sigma)):.4f}")
```

---

## 핵심 정리

- 촐레스키 분해 $\boldsymbol{\Sigma} = LL^T$ 를 쓰면 다변량정규분포의 확률표본을 효율적으로 만들 수 있다.
- 이 방법은 i.i.d. 표준정규확률변수 $\mathbf{z}$ 를 서로 상관이 있는 정규확률벡터 $\mathbf{x} = \boldsymbol{\mu} + L\mathbf{z}$ 로 바꾸는 것이다.
- 결과만 보면 `np.random.multivariate_normal()` 과 같지만, 그 속내를 알아 두는 것은 칼만 필터, 가우스 과정, MCMC 표집 같은 응용에서 꼭 필요하다.
- $AA^T = \boldsymbol{\Sigma}$ 인 분해라면 무엇이든 쓸 수 있으나 효율 때문에 촐레스키 분해를 즐겨 쓴다.

## 연습문제

**연습문제 1.**
$\boldsymbol{\Sigma} = \begin{pmatrix} 4 & 2 \\ 2 & 3 \end{pmatrix}$ 이라고 하자.

**(a)** $\boldsymbol{\Sigma} = LL^T$ 가 되는 촐레스키 인자 $L$ 을 구하여라.

**(b)** $LL^T = \boldsymbol{\Sigma}$ 임을 확인하여라.

**(c)** 표준정규분포에서 뽑은 값이 $\mathbf{z} = (1.5, -0.5)^T$ 일 때, $\boldsymbol{\mu} = (1, 2)^T$ 인 $N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ 에서 이에 대응하는 표본 $\mathbf{x}$ 를 구하여라.

??? success "연습문제 1 풀이"
    **(a)** $L = \begin{pmatrix} 2 & 0 \\ 1 & \sqrt{2} \end{pmatrix}$

    ($L_{11} = \sqrt{4} = 2$, $L_{21} = 2/2 = 1$, $L_{22} = \sqrt{3 - 1} = \sqrt{2}$ 에서 얻는다.)

    **(b)** $LL^T = \begin{pmatrix} 2 & 0 \\ 1 & \sqrt{2} \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 0 & \sqrt{2} \end{pmatrix} = \begin{pmatrix} 4 & 2 \\ 2 & 3 \end{pmatrix} = \boldsymbol{\Sigma}$ $\checkmark$

    **(c)** $\mathbf{x} = \boldsymbol{\mu} + L\mathbf{z} = \begin{pmatrix} 1 \\ 2 \end{pmatrix} + \begin{pmatrix} 2 & 0 \\ 1 & \sqrt{2} \end{pmatrix}\begin{pmatrix} 1.5 \\ -0.5 \end{pmatrix} = \begin{pmatrix} 1 + 3 \\ 2 + 1.5 - 0.5\sqrt{2} \end{pmatrix} = \begin{pmatrix} 4 \\ 2.793 \end{pmatrix}$

---

**연습문제 2.**
**(a)** $\boldsymbol{\mu} = (3, -1)^T$, $\sigma_X = 2$, $\sigma_Y = 1$, $\rho = -0.6$ 인 이변량정규분포에서 표본 5000개를 뽑는 파이썬 코드를 작성하여라. 표본평균, 표본공분산, 표본상관계수를 확인하여라.

**(b)** 같은 표본에서 $|Y - 0| < 0.1$ 인 것만 골라 $X$ 의 경험적 조건부분포를 구하고, 이론적인 $X \mid Y = 0$ 과 견주어 보아라.

??? success "연습문제 2 풀이"
    ```python
    import numpy as np

    np.random.seed(42)
    n = 5000
    mu = np.array([3, -1])
    sigma_x, sigma_y, rho = 2, 1, -0.6
    Sigma = np.array([[sigma_x**2, rho*sigma_x*sigma_y],
                       [rho*sigma_x*sigma_y, sigma_y**2]])

    L = np.linalg.cholesky(Sigma)
    z = np.random.randn(2, n)
    x = mu[:, np.newaxis] + L @ z

    print(f"Sample mean: {x.mean(axis=1)}")
    print(f"Sample cov:\n{np.cov(x)}")
    print(f"Sample corr: {np.corrcoef(x)[0,1]:.4f}")

    # (b)
    mask = np.abs(x[1] - 0) < 0.1
    x_given_y0 = x[0, mask]

    mu_cond = 3 + rho * (sigma_x / sigma_y) * (0 - (-1))
    sigma_cond = sigma_x * np.sqrt(1 - rho**2)

    print(f"\nEmpirical E[X|Y~0]: {x_given_y0.mean():.4f}")
    print(f"Theoretical E[X|Y=0]: {mu_cond:.4f}")
    print(f"Empirical Std[X|Y~0]: {x_given_y0.std():.4f}")
    print(f"Theoretical Std[X|Y=0]: {sigma_cond:.4f}")
    ```
