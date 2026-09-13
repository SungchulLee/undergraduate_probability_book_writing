# 다변량에서의 조건부분포

## 개요

다변량정규확률벡터의 일부 성분에 대하여 나머지 성분을 주고 조건을 걸면 그 조건부분포는 다시 다변량정규분포이다. 그 공식은 **나누어 쓴 공분산행렬**로 표현되며, 같은 것을 **정밀도행렬**(공분산행렬의 역행렬)로도 나타낼 수 있다. 이 절에서는 두 방식으로 조건부평균과 조건부분산을 유도하고, 나아가 중요한 **선형가우스모형**까지 다룬다.

---

## 블록으로 나눈 다변량정규분포

벡터 $\mathbf{x}$ 와 그 모수를 다음과 같이 나눈다.

$$
\mathbf{x} = \begin{pmatrix} \mathbf{x}_1 \\ \mathbf{x}_2 \end{pmatrix} \sim N\!\left(\begin{pmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{pmatrix},\; \begin{pmatrix} \boldsymbol{\Sigma}_{11} & \boldsymbol{\Sigma}_{12} \\ \boldsymbol{\Sigma}_{21} & \boldsymbol{\Sigma}_{22} \end{pmatrix}\right)
$$

여기에서 $\mathbf{x}_1 \in \mathbb{R}^{d_1}$, $\mathbf{x}_2 \in \mathbb{R}^{d_2}$ 이고 $d_1 + d_2 = d$ 이다.

---

## 주변분포

$\mathbf{x}_1$ 의 주변분포는 다음과 같이 간단하다.

$$
\mathbf{x}_1 \sim N(\boldsymbol{\mu}_1, \boldsymbol{\Sigma}_{11})
$$

---

## 조건부분포

$\mathbf{x}_2$ 가 주어졌을 때 $\mathbf{x}_1$ 의 조건부분포는 다음과 같다.

$$
\mathbf{x}_1 \mid \mathbf{x}_2 \;\sim\; N\!\left(\boldsymbol{\mu}_{1|2},\; \boldsymbol{\Sigma}_{1|2}\right)
$$

여기에서

$$
\boldsymbol{\mu}_{1|2} = \boldsymbol{\mu}_1 + \boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}(\mathbf{x}_2 - \boldsymbol{\mu}_2)
$$

$$
\boldsymbol{\Sigma}_{1|2} = \boldsymbol{\Sigma}_{11} - \boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}\boldsymbol{\Sigma}_{21}
$$

이다. 행렬 $\boldsymbol{\Sigma}_{1|2}$ 는 $\boldsymbol{\Sigma}$ 안에서 $\boldsymbol{\Sigma}_{22}$ 의 **슈어 여인자**이다.

---

## 정밀도행렬로 나타내기

**정밀도행렬**(정보행렬) $\boldsymbol{\Lambda} = \boldsymbol{\Sigma}^{-1}$ 을 다음과 같이 나누어 쓴다.

$$
\boldsymbol{\Lambda} = \begin{pmatrix} \boldsymbol{\Lambda}_{11} & \boldsymbol{\Lambda}_{12} \\ \boldsymbol{\Lambda}_{21} & \boldsymbol{\Lambda}_{22} \end{pmatrix}
$$

조건부분포의 모수를 $\boldsymbol{\Lambda}$ 로 바로 나타낼 수 있다.

$$
\boldsymbol{\Sigma}_{1|2} = \boldsymbol{\Lambda}_{11}^{-1}
$$

$$
\boldsymbol{\mu}_{1|2} = \boldsymbol{\mu}_1 - \boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12}(\mathbf{x}_2 - \boldsymbol{\mu}_2)
$$

!!! info "정밀도행렬을 왜 쓰는가"
    정밀도행렬에는 **조건부독립** 구조가 그대로 새겨져 있다. $\Lambda_{ij} = 0$ 이면 나머지 변수를 모두 주었을 때 $x_i$ 와 $x_j$ 가 조건부독립이다. 그래서 정밀도행렬은 그래프모형(가우스 마르코프 확률장)에서 중심 구실을 한다.

---

## 유도: Σ 와 Λ 의 성질

항등식 $\boldsymbol{\Sigma}\boldsymbol{\Lambda} = I$ 에서 출발한다.

$$
\begin{pmatrix} \boldsymbol{\Sigma}_{11} & \boldsymbol{\Sigma}_{12} \\ \boldsymbol{\Sigma}_{21} & \boldsymbol{\Sigma}_{22} \end{pmatrix} \begin{pmatrix} \boldsymbol{\Lambda}_{11} & \boldsymbol{\Lambda}_{12} \\ \boldsymbol{\Lambda}_{21} & \boldsymbol{\Lambda}_{22} \end{pmatrix} = \begin{pmatrix} I_{11} & 0_{12} \\ 0_{21} & I_{22} \end{pmatrix}
$$

$(1,2)$ 블록에서 $\boldsymbol{\Sigma}_{11}\boldsymbol{\Lambda}_{12} + \boldsymbol{\Sigma}_{12}\boldsymbol{\Lambda}_{22} = \mathbf{0}$ 을 얻는다.

$(1,1)$ 블록에서 $\boldsymbol{\Sigma}_{11}\boldsymbol{\Lambda}_{11} + \boldsymbol{\Sigma}_{12}\boldsymbol{\Lambda}_{21} = I$ 를 얻는다.

$(2,1)$ 블록에서 $\boldsymbol{\Sigma}_{21}\boldsymbol{\Lambda}_{11} + \boldsymbol{\Sigma}_{22}\boldsymbol{\Lambda}_{21} = \mathbf{0}$ 이므로 $\boldsymbol{\Lambda}_{21} = -\boldsymbol{\Sigma}_{22}^{-1}\boldsymbol{\Sigma}_{21}\boldsymbol{\Lambda}_{11}$ 이다.

이를 $(1,1)$ 식에 넣으면 다음을 얻는다.

$$
\boldsymbol{\Lambda}_{11}^{-1} = \boldsymbol{\Sigma}_{11} - \boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}\boldsymbol{\Sigma}_{21}
$$

마찬가지로 $(1,2)$ 블록에서 다음을 얻는다.

$$
\boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12} = -\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}
$$

이 두 항등식이 공분산으로 쓴 표현과 정밀도로 쓴 표현을 이어 준다.

---

## 유도: 완전제곱 만들기

$\mathbf{y}_i = \mathbf{x}_i - \boldsymbol{\mu}_i$ 라고 두고 지수부의 이차형식에서 출발한다.

$$
(\mathbf{x} - \boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu}) = \mathbf{y}_1^T\boldsymbol{\Lambda}_{11}\mathbf{y}_1 + \mathbf{y}_1^T\boldsymbol{\Lambda}_{12}\mathbf{y}_2 + \mathbf{y}_2^T\boldsymbol{\Lambda}_{21}\mathbf{y}_1 + \mathbf{y}_2^T\boldsymbol{\Lambda}_{22}\mathbf{y}_2
$$

$\mathbf{y}_2$ 를 고정된 값으로 보고 $\mathbf{y}_1$ 에 대하여 완전제곱을 만들면

$$
= (\mathbf{y}_1 - \boldsymbol{\alpha})^T\boldsymbol{\Lambda}_{11}(\mathbf{y}_1 - \boldsymbol{\alpha}) + \mathbf{y}_2 \text{ 만 들어 있는 항}
$$

이 된다. 여기에서 $\boldsymbol{\alpha} = -\boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12}\mathbf{y}_2$ 이다. 원래 좌표로 되돌리면

$$
\mathbf{x}_1 - \boldsymbol{\mu}_{1|2} = \mathbf{y}_1 - \boldsymbol{\alpha} = \mathbf{x}_1 - \left(\boldsymbol{\mu}_1 - \boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12}(\mathbf{x}_2 - \boldsymbol{\mu}_2)\right)
$$

가 된다. 이로써 $\boldsymbol{\mu}_{1|2} = \boldsymbol{\mu}_1 - \boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12}(\mathbf{x}_2 - \boldsymbol{\mu}_2)$ 와 $\boldsymbol{\Sigma}_{1|2} = \boldsymbol{\Lambda}_{11}^{-1}$ 이 확인된다.

---

## 선형가우스모형

$\mathbf{x}$ 와 $\mathbf{y}$ 가 가우스 잡음이 섞인 일차 모형으로 이어져 있을 때 특히 중요한 응용이 나타난다.

$$
\mathbf{x} \sim N(\boldsymbol{\mu}_x, \boldsymbol{\Sigma}_x), \qquad \mathbf{y} = A\mathbf{x} + \mathbf{b} + \boldsymbol{\varepsilon}, \quad \boldsymbol{\varepsilon} \sim N(\mathbf{0}, \boldsymbol{\Sigma}_\varepsilon)
$$

여기에서 $\boldsymbol{\varepsilon}$ 은 $\mathbf{x}$ 와 독립이다. 그러면 결합분포는 다음과 같다.

$$
\begin{pmatrix} \mathbf{x} \\ \mathbf{y} \end{pmatrix} \sim N\!\left(\begin{pmatrix} \boldsymbol{\mu}_x \\ A\boldsymbol{\mu}_x + \mathbf{b} \end{pmatrix},\; \begin{pmatrix} \boldsymbol{\Sigma}_x & \boldsymbol{\Sigma}_x A^T \\ A\boldsymbol{\Sigma}_x & A\boldsymbol{\Sigma}_x A^T + \boldsymbol{\Sigma}_\varepsilon \end{pmatrix}\right)
$$

### y 의 주변분포

$$
\mathbf{y} \sim N(A\boldsymbol{\mu}_x + \mathbf{b},\; A\boldsymbol{\Sigma}_x A^T + \boldsymbol{\Sigma}_\varepsilon)
$$

### 사후분포: y 가 주어졌을 때의 x

조건부분포 공식을 그대로 적용하면 다음을 얻는다.

$$
\boldsymbol{\mu}_{x|y} = \boldsymbol{\mu}_x + \boldsymbol{\Sigma}_x A^T (A\boldsymbol{\Sigma}_x A^T + \boldsymbol{\Sigma}_\varepsilon)^{-1}(\mathbf{y} - A\boldsymbol{\mu}_x - \mathbf{b})
$$

$$
\boldsymbol{\Sigma}_{x|y} = \boldsymbol{\Sigma}_x - \boldsymbol{\Sigma}_x A^T (A\boldsymbol{\Sigma}_x A^T + \boldsymbol{\Sigma}_\varepsilon)^{-1} A\boldsymbol{\Sigma}_x
$$

### 정밀도 꼴 (우드베리 항등식 이용)

우드베리 항등식 $(A + UCV)^{-1} = A^{-1} - A^{-1}U(C^{-1} + VA^{-1}U)^{-1}VA^{-1}$ 을 쓰면 다음을 얻는다.

$$
\boldsymbol{\Sigma}_{x|y}^{-1} = \boldsymbol{\Sigma}_x^{-1} + A^T\boldsymbol{\Sigma}_\varepsilon^{-1} A
$$

$$
\boldsymbol{\mu}_{x|y} = \boldsymbol{\Sigma}_{x|y}\left(\boldsymbol{\Sigma}_x^{-1}\boldsymbol{\mu}_x + A^T\boldsymbol{\Sigma}_\varepsilon^{-1}(\mathbf{y} - \mathbf{b})\right)
$$

!!! note "베이즈 추론과의 연결"
    정밀도 꼴로 보면 사후 정밀도는 사전 정밀도에 자료의 정밀도를 더한 것이다. 사후평균은 사전평균과 자료를 정밀도로 가중하여 섞은 것이다. 이것이 가우스모형에서의 **베이즈 갱신 규칙**이며 칼만 필터의 바탕이 된다.

### 정밀도행렬의 유도

$\log p(\mathbf{x}, \mathbf{y}) = \log p(\mathbf{x}) + \log p(\mathbf{y} \mid \mathbf{x})$ 에서 출발하면

$$
\log p(\mathbf{x}, \mathbf{y}) \propto -\frac{1}{2}\tilde{\mathbf{x}}^T\boldsymbol{\Sigma}_x^{-1}\tilde{\mathbf{x}} - \frac{1}{2}(\tilde{\mathbf{y}} - A\tilde{\mathbf{x}})^T\boldsymbol{\Sigma}_\varepsilon^{-1}(\tilde{\mathbf{y}} - A\tilde{\mathbf{x}})
$$

이다. 여기에서 $\tilde{\mathbf{x}} = \mathbf{x} - \boldsymbol{\mu}_x$ 이고 $\tilde{\mathbf{y}} = \mathbf{y} - A\boldsymbol{\mu}_x - \mathbf{b}$ 이다. 이를 펼치면 다음과 같다.

$$
= -\frac{1}{2}\begin{pmatrix} \tilde{\mathbf{x}} \\ \tilde{\mathbf{y}} \end{pmatrix}^T \underbrace{\begin{pmatrix} \boldsymbol{\Sigma}_x^{-1} + A^T\boldsymbol{\Sigma}_\varepsilon^{-1}A & -A^T\boldsymbol{\Sigma}_\varepsilon^{-1} \\ -\boldsymbol{\Sigma}_\varepsilon^{-1}A & \boldsymbol{\Sigma}_\varepsilon^{-1} \end{pmatrix}}_{\boldsymbol{\Lambda}} \begin{pmatrix} \tilde{\mathbf{x}} \\ \tilde{\mathbf{y}} \end{pmatrix}
$$

블록을 읽어 내면

$$
\boldsymbol{\Lambda}_{11} = \boldsymbol{\Sigma}_x^{-1} + A^T\boldsymbol{\Sigma}_\varepsilon^{-1}A, \qquad \boldsymbol{\Lambda}_{12} = -A^T\boldsymbol{\Sigma}_\varepsilon^{-1}
$$

이므로 다음을 얻는다.

$$
\boldsymbol{\Sigma}_{x|y} = \boldsymbol{\Lambda}_{11}^{-1} = (\boldsymbol{\Sigma}_x^{-1} + A^T\boldsymbol{\Sigma}_\varepsilon^{-1}A)^{-1}
$$

$$
\boldsymbol{\mu}_{x|y} = \boldsymbol{\mu}_x - \boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12}\tilde{\mathbf{y}} = \boldsymbol{\Sigma}_{x|y}(\boldsymbol{\Sigma}_x^{-1}\boldsymbol{\mu}_x + A^T\boldsymbol{\Sigma}_\varepsilon^{-1}(\mathbf{y} - \mathbf{b}))
$$

---

## 파이썬 구현

```python
import numpy as np

def conditional_normal(mu, Sigma, idx1, idx2, x2_observed):
    """
    x[idx2] = x2_observed 가 주어졌을 때 x[idx1] 의 조건부분포를 구한다.

    매개변수
    ----------
    mu : 평균벡터
    Sigma : 공분산행렬
    idx1 : 조건부분포를 구할 변수의 첨자(출력)
    idx2 : 관측된 변수의 첨자
    x2_observed : 관측값

    반환값
    -------
    mu_cond, Sigma_cond : 조건부평균과 조건부공분산
    """
    mu1 = mu[idx1]
    mu2 = mu[idx2]
    S11 = Sigma[np.ix_(idx1, idx1)]
    S12 = Sigma[np.ix_(idx1, idx2)]
    S21 = Sigma[np.ix_(idx2, idx1)]
    S22 = Sigma[np.ix_(idx2, idx2)]

    S22_inv = np.linalg.inv(S22)
    mu_cond = mu1 + S12 @ S22_inv @ (x2_observed - mu2)
    Sigma_cond = S11 - S12 @ S22_inv @ S21
    return mu_cond, Sigma_cond


# 예: 3차원 다변량정규분포
mu = np.array([1.0, 2.0, 3.0])
Sigma = np.array([
    [4.0, 2.0, 1.0],
    [2.0, 5.0, 3.0],
    [1.0, 3.0, 6.0]
])

# x2=3, x3=4 로 조건을 건다
x2_obs = np.array([3.0, 4.0])
mu_cond, Sigma_cond = conditional_normal(mu, Sigma, [0], [1, 2], x2_obs)
print(f"X1 | X2=3, X3=4 ~ N({mu_cond[0]:.4f}, {Sigma_cond[0,0]:.4f})")

# 정밀도행렬로 확인한다
Lambda = np.linalg.inv(Sigma)
print(f"\nPrecision matrix Λ:\n{Lambda}")
print(f"\nΛ11⁻¹ = {1/Lambda[0,0]:.4f}")
print(f"Σ_{'{1|2}'} = {Sigma_cond[0,0]:.4f}")


# 선형가우스모형 예제
print("\n=== Linear-Gaussian Model ===")
mu_x = np.array([0.0, 0.0])
Sigma_x = np.array([[1.0, 0.5], [0.5, 2.0]])
A = np.array([[1.0, 1.0]])
b = np.array([0.0])
Sigma_eps = np.array([[0.1]])

# 결합분포
mu_joint = np.concatenate([mu_x, A @ mu_x + b])
Sigma_joint = np.block([
    [Sigma_x, Sigma_x @ A.T],
    [A @ Sigma_x, A @ Sigma_x @ A.T + Sigma_eps]
])
print(f"Joint mean: {mu_joint}")
print(f"Joint covariance:\n{Sigma_joint}")

# 사후분포 x|y
y_obs = np.array([2.0])
mu_post, Sigma_post = conditional_normal(
    mu_joint, Sigma_joint, [0, 1], [2], y_obs
)
print(f"\nPosterior mean: {mu_post}")
print(f"Posterior covariance:\n{Sigma_post}")

# 정밀도 꼴로 확인한다
Sigma_x_inv = np.linalg.inv(Sigma_x)
Sigma_eps_inv = np.linalg.inv(Sigma_eps)
Sigma_post_inv = Sigma_x_inv + A.T @ Sigma_eps_inv @ A
Sigma_post_prec = np.linalg.inv(Sigma_post_inv)
mu_post_prec = Sigma_post_prec @ (Sigma_x_inv @ mu_x + A.T @ Sigma_eps_inv @ (y_obs - b))
print(f"\nPosterior mean (precision form): {mu_post_prec}")
print(f"Posterior cov (precision form):\n{Sigma_post_prec}")
```

---

## 핵심 정리

- 다변량정규확률벡터의 부분벡터에 대한 조건부분포는 다시 다변량정규분포이며, 평균과 공분산이 닫힌 꼴로 주어진다.
- **공분산 꼴**은 $\boldsymbol{\Sigma}_{12}\boldsymbol{\Sigma}_{22}^{-1}$ 을, **정밀도 꼴**은 $\boldsymbol{\Lambda}_{11}^{-1}\boldsymbol{\Lambda}_{12}$ 를 쓴다. 둘은 서로 같은 것이다.
- 조건부공분산 $\boldsymbol{\Sigma}_{1|2} = \boldsymbol{\Lambda}_{11}^{-1}$ 은 관측값에 따라 달라지지 않는다. 관측값에 따라 옮겨 가는 것은 조건부평균뿐이다.
- 선형가우스모형은 베이즈 갱신, 곧 사후 정밀도 = 사전 정밀도 + 자료의 정밀도로 이어진다. 이것이 칼만 필터의 바탕이다.

## 연습문제

**연습문제 1.**
$\mathbf{x} = (X_1, X_2, X_3)^T \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ 이고

$$
\boldsymbol{\mu} = \begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix}, \qquad \boldsymbol{\Sigma} = \begin{pmatrix} 4 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 3 \end{pmatrix}
$$

라고 하자.

**(a)** $(X_1, X_2)^T$ 의 주변분포를 구하여라.

**(b)** $X_1 \mid X_2 = 3, X_3 = 1$ 의 조건부분포를 구하여라.

**(c)** 정밀도행렬을 살펴서 $X_2$ 가 주어졌을 때 $X_1$ 과 $X_3$ 가 조건부독립인지 확인하여라.

??? success "연습문제 1 풀이"
    **(a)** $(X_1, X_2)^T \sim N\!\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 4 & 1 \\ 1 & 2 \end{pmatrix}\right)$

    **(b)** $\mathbf{x}_1 = X_1$, $\mathbf{x}_2 = (X_2, X_3)^T$ 로 두면

    $\boldsymbol{\Sigma}_{12} = (1, 0)$, $\boldsymbol{\Sigma}_{22} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$, $\boldsymbol{\Sigma}_{22}^{-1} = \frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}$

    $\mu_{1|2} = 0 + (1, 0)\frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} 2 \\ -1 \end{pmatrix} = \frac{1}{5}(3, -1)\begin{pmatrix} 2 \\ -1 \end{pmatrix} = \frac{7}{5} = 1.4$

    $\Sigma_{1|2} = 4 - (1, 0)\frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = 4 - \frac{3}{5} = \frac{17}{5} = 3.4$

    따라서 $X_1 \mid X_2 = 3, X_3 = 1 \sim N(1.4, 3.4)$ 이다.

    **(c)** $\boldsymbol{\Lambda} = \boldsymbol{\Sigma}^{-1}$ 을 계산해 보자. $\Sigma_{13} = 0$ 이지만 일반적으로 $\Lambda_{13} \neq 0$ 일 것으로 기대된다. 실제로 수치로 확인해 보면 $\Lambda_{13} \approx 0.029 \neq 0$ 이므로 $X_2$ 가 주어졌을 때 $X_1$ 과 $X_3$ 는 일반적으로 조건부독립이 **아니다**. ($\boldsymbol{\Sigma}$ 의 $0$ 은 조건부무상관이 아니라 주변적인 무상관을 뜻한다.)
