# 평균벡터와 공분산행렬로 정의하기

## 개요

**다변량정규분포**는 일변량정규분포와 이변량정규분포를 임의의 차원 $d$ 로 넓힌 것이다. 독립인 표준정규확률변수들의 일차변환으로 만들어 내는 방식으로 정의되며, 평균벡터 $\boldsymbol{\mu}$ 와 공분산행렬 $\boldsymbol{\Sigma}$ 만으로 완전히 결정된다.

---

## 밀도함수

$d$ 차원 확률벡터 $\mathbf{x} = (x_1, x_2, \ldots, x_d)^T$ 가 $\mathbf{x} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ 를 따를 때 밀도함수는 다음과 같다.

$$
f(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^d |\boldsymbol{\Sigma}|}} \exp\left(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})\right)
$$

여기에서

- $\boldsymbol{\mu} \in \mathbb{R}^d$ 는 **평균벡터**이다
- $\boldsymbol{\Sigma} \in \mathbb{R}^{d \times d}$ 는 **공분산행렬**이다(대칭이고 양정치이다)
- $|\boldsymbol{\Sigma}|$ 는 $\boldsymbol{\Sigma}$ 의 행렬식이다

---

## 일차변환으로 만드는 정의

다변량정규분포를 따르는 $\mathbf{x} \in \mathbb{R}^d$ 는 언제나 다음과 같이 쓸 수 있다.

$$
\mathbf{x} = A\mathbf{z} + \boldsymbol{\mu}
$$

여기에서

- $\mathbf{z} = (z_1, z_2, \ldots, z_n)^T$ 이고 $z_k \overset{\text{iid}}{\sim} N(0, 1)$ 이다
- $A \in \mathbb{R}^{d \times n}$ 는 상수행렬이다
- $\boldsymbol{\mu} \in \mathbb{R}^d$ 는 상수벡터이다

이 정의는 다변량정규분포를 가장 단순한 재료(독립인 표준정규확률변수)로부터 **만들어 내는** 방법을 알려 주기에 근본적이다.

---

## 평균과 공분산 구하기

$\mathbf{x} = A\mathbf{z} + \boldsymbol{\mu}$ 에서 출발한다.

**평균:**

$$
E[\mathbf{x}] = E[A\mathbf{z} + \boldsymbol{\mu}] = A \cdot E[\mathbf{z}] + \boldsymbol{\mu} = A \cdot \mathbf{0} + \boldsymbol{\mu} = \boldsymbol{\mu}
$$

**공분산행렬:**

$$
\boldsymbol{\Sigma} = E[(\mathbf{x} - \boldsymbol{\mu})(\mathbf{x} - \boldsymbol{\mu})^T] = E[(A\mathbf{z})(A\mathbf{z})^T] = A \cdot E[\mathbf{z}\mathbf{z}^T] \cdot A^T = A I A^T = AA^T
$$

곧 $\boldsymbol{\Sigma} = AA^T$ 이며, 이는 어떤 행렬 $A$ 에 대해서도 저절로 대칭이고 양반정치이다.

---

## 결합 적률생성함수

다변량정규분포의 적률생성함수는 일변량의 공식을 그대로 넓힌 꼴이다. $X \sim N(\mu, \sigma^2)$ 일 때 다음이 성립함을 떠올리자.

$$
\varphi(t) = E[e^{tX}] = e^{\mu t + \frac{1}{2}\sigma^2 t^2}
$$

$\mathbf{x} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ 에 대한 결합 적률생성함수는 다음과 같다.

$$
\varphi(\mathbf{t}) = E[e^{\mathbf{t}^T \mathbf{x}}] = e^{\mathbf{t}^T \boldsymbol{\mu} + \frac{1}{2}\mathbf{t}^T \boldsymbol{\Sigma} \mathbf{t}}
$$

### 유도

$\mathbf{x} = A\mathbf{z} + \boldsymbol{\mu}$ 이므로

$$
\mathbf{t}^T \mathbf{x} = \mathbf{t}^T(A\mathbf{z} + \boldsymbol{\mu}) = \sum_k a_k z_k + b
$$

이다. 여기에서 $a_k$ 는 $A^T\mathbf{t}$ 의 성분이고 $b = \mathbf{t}^T\boldsymbol{\mu}$ 이다. 이것은 독립인 표준정규확률변수들의 일차결합이므로

$$
\mathbf{t}^T \mathbf{x} \sim N(\mu_1, \sigma_1^2)
$$

이고, 여기에서

$$
\mu_1 = E[\mathbf{t}^T\mathbf{x}] = \mathbf{t}^T\boldsymbol{\mu}
$$

$$
\sigma_1^2 = \text{Var}(\mathbf{t}^T\mathbf{x}) = \mathbf{t}^T A E[\mathbf{z}\mathbf{z}^T] A^T \mathbf{t} = \mathbf{t}^T AA^T \mathbf{t} = \mathbf{t}^T \boldsymbol{\Sigma} \mathbf{t}
$$

이다. 따라서 다음을 얻는다.

$$
\varphi_{\mathbf{x}}(\mathbf{t}) = E[e^{\mathbf{t}^T\mathbf{x}}] = \varphi_{N(\mu_1, \sigma_1^2)}(1) = e^{\mu_1 + \frac{1}{2}\sigma_1^2} = e^{\mathbf{t}^T\boldsymbol{\mu} + \frac{1}{2}\mathbf{t}^T\boldsymbol{\Sigma}\mathbf{t}}
$$

---

## 주요 성질

결합 적률생성함수에서 중요한 결과들이 곧바로 따라 나온다.

**성질 1: $\boldsymbol{\mu}$ 와 $\boldsymbol{\Sigma}$ 가 분포를 완전히 결정한다.**

적률생성함수가 오직 $\boldsymbol{\mu}$ 와 $\boldsymbol{\Sigma}$ 로만 정해지고 적률생성함수는 분포를 하나로 결정하므로, 평균과 공분산이 같은 두 다변량정규확률벡터는 분포가 같다.

**성질 2: 일차결합은 정규분포를 따른다.**

어떤 일차결합 $\mathbf{a}^T\mathbf{x}$ 도 일변량정규분포를 따른다.

$$
\mathbf{a}^T\mathbf{x} \sim N(\mathbf{a}^T\boldsymbol{\mu},\; \mathbf{a}^T\boldsymbol{\Sigma}\mathbf{a})
$$

더 일반적으로, 어떤 일차변환 $B\mathbf{x} + \mathbf{c}$ 도 다변량정규분포를 따른다.

$$
B\mathbf{x} + \mathbf{c} \sim N(B\boldsymbol{\mu} + \mathbf{c},\; B\boldsymbol{\Sigma}B^T)
$$

---

## 파이썬 구현

```python
import numpy as np
from scipy.stats import multivariate_normal

# 3차원 다변량정규분포를 정한다
mu = np.array([1, 2, -1])
Sigma = np.array([
    [4,  2,  1],
    [2,  5, -1],
    [1, -1,  3]
])

# 양정치인지 확인한다
eigenvalues = np.linalg.eigvalsh(Sigma)
print(f"Eigenvalues of Σ: {eigenvalues}")
print(f"Positive definite: {all(eigenvalues > 0)}")

# 구성적 정의를 따라 표본을 만든다
np.random.seed(42)
n = 10_000
A = np.linalg.cholesky(Sigma)  # Σ = AA^T
z = np.random.randn(3, n)
x = A @ z + mu[:, np.newaxis]

print(f"\nSample mean: {x.mean(axis=1)}")
print(f"True mean:   {mu}")
print(f"\nSample covariance:\n{np.cov(x)}")
print(f"True covariance:\n{Sigma}")

# 결합 적률생성함수 확인: E[exp(t^T x)] 가 exp(t^T μ + 0.5 t^T Σ t) 와 같아야 한다
t = np.array([0.1, -0.2, 0.3])
empirical_mgf = np.exp((t @ x)).mean()
theoretical_mgf = np.exp(t @ mu + 0.5 * t @ Sigma @ t)
print(f"\nEmpirical MGF at t={t}: {empirical_mgf:.4f}")
print(f"Theoretical MGF:         {theoretical_mgf:.4f}")
```

---

## 핵심 정리

- 다변량정규분포는 $\mathbf{z}$ 의 성분이 i.i.d. 표준정규확률변수일 때 $\mathbf{x} = A\mathbf{z} + \boldsymbol{\mu}$ 로 만들어 내는 방식으로 정의된다.
- 공분산행렬은 $\boldsymbol{\Sigma} = AA^T$ 이며 저절로 대칭이고 양반정치이다.
- 결합 적률생성함수 $\varphi(\mathbf{t}) = e^{\mathbf{t}^T\boldsymbol{\mu} + \frac{1}{2}\mathbf{t}^T\boldsymbol{\Sigma}\mathbf{t}}$ 은 $\boldsymbol{\mu}$ 와 $\boldsymbol{\Sigma}$ 를 통해 분포를 하나로 결정한다.
- 다변량정규확률벡터의 일차결합이나 일차변환은 다시 다변량정규분포를 따른다.

## 연습문제

**연습문제 1.** $\boldsymbol{\mu} = (1, 2)^T$ 이고 $\boldsymbol{\Sigma} = \begin{pmatrix} 4 & 1 \\ 1 & 9 \end{pmatrix}$ 일 때 $\mathbf{X} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ 라고 하자. $Y = X_1 + X_2$ 의 분포를 구하여라.

??? success "연습문제 1 풀이"
    $\mathbf{a} = (1, 1)^T$ 라고 하면 $Y = \mathbf{a}^T \mathbf{X}$ 이다. 따라서 $Y \sim N(\mathbf{a}^T\boldsymbol{\mu}, \mathbf{a}^T\boldsymbol{\Sigma}\mathbf{a})$ 이다.

    $E[Y] = 1 + 2 = 3$ 이고 $\text{Var}(Y) = (1, 1)\begin{pmatrix} 4 & 1 \\ 1 & 9 \end{pmatrix}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = (5, 10)\begin{pmatrix} 1 \\ 1 \end{pmatrix} = 15$ 이다.

    $$Y \sim N(3, 15)$$

---

**연습문제 2.** $\boldsymbol{\Sigma}$ 가 대각행렬이면 $\mathbf{X}$ 의 성분들이 독립임을 보여라.

??? success "연습문제 2 풀이"
    $\boldsymbol{\Sigma} = \text{diag}(\sigma_1^2, \ldots, \sigma_d^2)$ 이면 $|\boldsymbol{\Sigma}| = \prod \sigma_i^2$ 이고 $\boldsymbol{\Sigma}^{-1} = \text{diag}(1/\sigma_1^2, \ldots, 1/\sigma_d^2)$ 이다.

    지수부는 $-\frac{1}{2}\sum_{i=1}^d \frac{(x_i - \mu_i)^2}{\sigma_i^2}$ 이 되고, 밀도함수는 다음과 같이 인수분해된다.

    $$
    f(\mathbf{x}) = \prod_{i=1}^d \frac{1}{\sqrt{2\pi}\sigma_i}\exp\!\left(-\frac{(x_i - \mu_i)^2}{2\sigma_i^2}\right)
    $$

    이것은 주변정규밀도함수들의 곱이므로 성분들은 독립이다. $\square$

---

**연습문제 3.** 3차원 다변량정규확률벡터 $\mathbf{X} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ 를 $\mathbf{Z} \sim N(\mathbf{0}, I_3)$ 을 써서 $\mathbf{X} = A\mathbf{Z} + \boldsymbol{\mu}$ 꼴로 나타내어라. $A$ 는 어떤 성질을 만족해야 하는가?

??? success "연습문제 3 풀이"
    $A$ 는 $AA^T = \boldsymbol{\Sigma}$ 를 만족해야 한다. 이것이 촐레스키 분해이며, 더 넓게는 $\boldsymbol{\Sigma}$ 의 제곱근 분해라면 무엇이든 된다. $\boldsymbol{\Sigma}$ 가 대칭이고 양정치이므로 이러한 $A$ 는 언제나 존재한다. 흔히 $A$ 로 아래삼각 촐레스키 인자를 잡는다.

---

**연습문제 4.** $\mathbf{X} \sim N(\mathbf{0}, I_d)$ 일 때 $\|\mathbf{X}\|^2 = X_1^2 + \cdots + X_d^2$ 의 분포는 무엇인가?

??? success "연습문제 4 풀이"
    각 $X_i \sim N(0,1)$ 이 서로 독립이므로 $X_i^2 \sim \chi^2_1$ 이다. 독립인 $\chi^2_1$ 확률변수 $d$ 개의 합은 $\chi^2_d$ 이다.

    $$
    \|\mathbf{X}\|^2 \sim \chi^2_d
    $$

---

**연습문제 5.** 각각의 주변분포가 정규분포인 두 확률변수의 결합분포가 이변량정규분포가 **아닐** 수 있는가? 예를 들거나 그럴 수 없는 까닭을 설명하여라.

??? success "연습문제 5 풀이"
    **그럴 수 있다.** $Z \sim N(0,1)$ 이라고 하고 $X = Z$, $Y = Z \cdot \text{sign}(U)$ 로 두자. 여기에서 $U \sim \text{Uniform}(0,1)$ 은 $Z$ 와 독립이다. 그러면 $Y$ 의 주변분포는 $N(0,1)$ 이다(대칭인 확률변수에 무작위 부호를 곱해도 분포가 바뀌지 않기 때문이다). 그러나 쌍 $(X, Y)$ 는 두 직선 $y = x$ 와 $y = -x$ 위의 값만 가지므로 받침이 $\mathbb{R}^2$ 전체여야 하는 이변량정규분포일 수 없다.
