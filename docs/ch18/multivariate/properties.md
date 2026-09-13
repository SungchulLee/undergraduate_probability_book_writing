# 성질과 일차변환

## 개요

다변량정규분포는 놀라운 닫힘 성질을 지닌다. 일차변환을 하여도, 주변분포를 구하여도, 조건을 걸어도 다시 다변량정규분포가 된다. 이 절에서는 결합 적률생성함수에서 따라 나오는 성질들, 그 가운데에서도 공분산이 $0$ 인 것과 독립인 것 사이의 관계를 중심으로 살펴본다.

---

## 성질 1: 적률생성함수에 따른 유일성

두 다변량정규확률벡터 $\mathbf{x}$ 와 $\mathbf{y}$ 의 평균 $\boldsymbol{\mu}$ 와 공분산행렬 $\boldsymbol{\Sigma}$ 가 같으면 결합 적률생성함수가 같다.

$$
\varphi_{\mathbf{x}}(\mathbf{t}) = e^{\mathbf{t}^T\boldsymbol{\mu} + \frac{1}{2}\mathbf{t}^T\boldsymbol{\Sigma}\mathbf{t}} = \varphi_{\mathbf{y}}(\mathbf{t})
$$

적률생성함수의 유일성 정리에 따라 $\mathbf{x}$ 와 $\mathbf{y}$ 는 같은 분포를 따른다.

---

## 성질 2: 비대각 성분이 0이면 독립이다

다변량정규확률벡터 $\mathbf{x} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ 의 공분산행렬이 대각행렬이면(비대각 성분이 모두 $0$ 이면) 모든 성분 $x_1, x_2, \ldots, x_d$ 가 **상호독립**이다.

### 적률생성함수의 인수분해를 이용한 증명

$\boldsymbol{\Sigma} = \text{diag}(\sigma_1^2, \sigma_2^2, \ldots, \sigma_d^2)$ 이면

$$
\mathbf{t}^T\boldsymbol{\Sigma}\mathbf{t} = \sum_{i=1}^d \sigma_i^2 t_i^2
$$

이므로 결합 적률생성함수가 다음과 같이 인수분해된다.

$$
\varphi_{\mathbf{x}}(\mathbf{t}) = e^{\sum_i \mu_i t_i + \frac{1}{2}\sum_i \sigma_i^2 t_i^2} = \prod_{i=1}^d \underbrace{e^{\mu_i t_i + \frac{1}{2}\sigma_i^2 t_i^2}}_{\varphi_{N(\mu_i, \sigma_i^2)}(t_i)}
$$

결합 적률생성함수가 주변 적률생성함수들의 곱과 같으므로 성분들은 독립이다.

---

## 성질 3: 쌍마다 공분산이 0이면 독립이다

더 일반적으로, 어떤 고정된 첨자 $i$ 에 대하여 $j \neq i$ 인 모든 $j$ 에서 $\Sigma_{ij} = 0$ 이면 $x_i$ 는 나머지 성분 $(x_j)_{j \neq i}$ 전체와 독립이다.

### 증명의 얼개

$\mathbf{x}$ 와 평균과 공분산이 같으면서 $y_i$ 가 $j \neq i$ 인 $y_j$ 와 독립인 벡터 $\mathbf{y}$ 를 만든다. $i$ 번째 행과 열에 걸린 비대각 성분이 모두 $0$ 이므로 $\mathbf{x}$ 와 $\mathbf{y}$ 의 결합 적률생성함수가 같다. 따라서 $\mathbf{x}$ 와 $\mathbf{y}$ 는 같은 분포를 따르고, 특히 $x_i$ 는 나머지와 독립이다.

!!! note "놓쳐서는 안 될 단서"
    이 성질은 결합분포가 다변량정규분포일 때에만 성립한다. 함께 정규분포를 따른다는 보장이 없는 일반적인 확률변수들에서는 쌍마다 공분산이 $0$ 이라고 해서 쌍마다 독립인 것은 **아니다**.

---

## 일차변환

### 아핀변환

$\mathbf{x} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ 이고 $B \in \mathbb{R}^{m \times d}$, $\mathbf{c} \in \mathbb{R}^m$ 에 대하여 $\mathbf{y} = B\mathbf{x} + \mathbf{c}$ 라고 하면 다음이 성립한다.

$$
\mathbf{y} \sim N(B\boldsymbol{\mu} + \mathbf{c},\; B\boldsymbol{\Sigma}B^T)
$$

### 특별한 경우

**스칼라 일차결합:** $a^T\mathbf{x} \sim N(\mathbf{a}^T\boldsymbol{\mu}, \mathbf{a}^T\boldsymbol{\Sigma}\mathbf{a})$

**성분들의 합:** $\sum_i x_i \sim N\!\left(\sum_i \mu_i,\; \sum_i\sum_j \Sigma_{ij}\right)$

**부분벡터(주변분포 구하기):** 성분 $x_{i_1}, \ldots, x_{i_m}$ 을 골라내는 것은 선택행렬 $B$ 를 곱하는 것과 같으며, 그 결과는 해당 부분평균과 부분공분산을 지닌 다변량정규분포이다.

---

## 파이썬: 성질 확인하기

```python
import numpy as np

np.random.seed(42)
n = 50_000

# 3차원 다변량정규분포
mu = np.array([1, 2, 3])
Sigma = np.array([
    [4, 0, 0],
    [0, 3, 0],
    [0, 0, 2]
])

# 표본을 만든다
L = np.linalg.cholesky(Sigma)
z = np.random.randn(3, n)
x = L @ z + mu[:, np.newaxis]

# 성질 2: Sigma 가 대각행렬이면 독립이다
# 확인: P(X1 > 1, X2 > 2) 가 P(X1 > 1) * P(X2 > 2) 와 같아야 한다
p_joint = np.mean((x[0] > 1) & (x[1] > 2))
p_x1 = np.mean(x[0] > 1)
p_x2 = np.mean(x[1] > 2)
print("=== Diagonal Σ: Independence Test ===")
print(f"P(X1>1, X2>2)     = {p_joint:.4f}")
print(f"P(X1>1) * P(X2>2) = {p_x1 * p_x2:.4f}")

# 일차변환
B = np.array([[1, 1, 0], [0, 1, -1]])
c = np.array([10, 20])
y = B @ x + c[:, np.newaxis]

print("\n=== Affine Transformation y = Bx + c ===")
print(f"Sample mean of y: {y.mean(axis=1)}")
print(f"Theoretical mean:  {B @ mu + c}")
print(f"\nSample cov of y:\n{np.cov(y)}")
print(f"Theoretical cov:\n{B @ Sigma @ B.T}")

# 대각행렬이 아닌 Sigma: 쌍마다의 독립이 무너짐을 확인한다
Sigma2 = np.array([
    [4, 2, 0],
    [2, 3, 0],
    [0, 0, 2]
])
L2 = np.linalg.cholesky(Sigma2)
x2 = L2 @ z + mu[:, np.newaxis]

print("\n=== Non-diagonal Σ (X3 independent of X1, X2) ===")
p_joint13 = np.mean((x2[0] > 1) & (x2[2] > 3))
p_x1_2 = np.mean(x2[0] > 1)
p_x3_2 = np.mean(x2[2] > 3)
print(f"P(X1>1, X3>3)     = {p_joint13:.4f}")
print(f"P(X1>1) * P(X3>3) = {p_x1_2 * p_x3_2:.4f}")

p_joint12 = np.mean((x2[0] > 1) & (x2[1] > 2))
p_x2_2 = np.mean(x2[1] > 2)
print(f"\nP(X1>1, X2>2)     = {p_joint12:.4f}")
print(f"P(X1>1) * P(X2>2) = {p_x1_2 * p_x2_2:.4f}  (not equal — dependent)")
```

---

## 핵심 정리

- 다변량정규분포에서는 $\boldsymbol{\mu}$ 와 $\boldsymbol{\Sigma}$ 가 적률생성함수를 통해 분포를 하나로 결정한다.
- 공분산행렬의 비대각 성분이 $0$ 이면 해당 성분들이 독립이다. 이는 다변량정규분포 집안만이 지닌 **특별한** 성질이다.
- 다변량정규분포는 아핀변환에 대하여 **닫혀 있다**. 곧 $B\mathbf{x} + \mathbf{c}$ 는 다시 다변량정규분포를 따른다.
- 주변분포를 구하는 일은 행렬로 성분을 골라내는 일차변환의 한 경우이다.

## 연습문제

**연습문제 1.**
$\boldsymbol{\mu} = (1, 2)^T$ 이고 $\boldsymbol{\Sigma} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$ 일 때 $\mathbf{x} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ 라고 하자.

**(a)** 결합 적률생성함수 $\varphi(\mathbf{t})$ 를 $\mathbf{t} = (1, 0)^T$ 와 $\mathbf{t} = (0, 1)^T$ 에서 구하여라.

**(b)** $X_1 + X_2$ 의 분포를 구하여라.

**(c)** $2X_1 - X_2$ 의 분포를 구하여라.

??? success "연습문제 1 풀이"
    **(a)**

    $\mathbf{t} = (1, 0)^T$ 에서: $\varphi = e^{1 + \frac{1}{2}(2)} = e^{2}$ (이것은 $X_1 \sim N(1, 2)$ 의 주변 적률생성함수이다).

    $\mathbf{t} = (0, 1)^T$ 에서: $\varphi = e^{2 + \frac{1}{2}(3)} = e^{3.5}$ ($X_2 \sim N(2, 3)$ 의 주변 적률생성함수이다).

    **(b)** $\mathbf{a} = (1, 1)^T$ 라고 하면 $X_1 + X_2 = \mathbf{a}^T\mathbf{x}$ 이다.

    평균: $1 + 2 = 3$. 분산: $\mathbf{a}^T\boldsymbol{\Sigma}\mathbf{a} = 2 + 2(1) + 3 = 7$.

    따라서 $X_1 + X_2 \sim N(3, 7)$ 이다.

    **(c)** $\mathbf{a} = (2, -1)^T$ 라고 하면 $2X_1 - X_2 = \mathbf{a}^T\mathbf{x}$ 이다.

    평균: $2(1) - 2 = 0$. 분산: $4(2) + (-1)^2(3) + 2(2)(-1)(1) = 8 + 3 - 4 = 7$.

    따라서 $2X_1 - X_2 \sim N(0, 7)$ 이다.
