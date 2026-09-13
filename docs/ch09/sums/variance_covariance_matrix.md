# 분산–공분산 행렬

## 왜 필요한가

확률벡터 $\mathbf{X} = (X_1, X_2, \ldots, X_n)^T$ 를 다룰 때에는 모든 분산과 두 변수씩의 공분산을 한꺼번에 담아 둘 간결한 방법이 필요하다. **분산–공분산 행렬**(줄여서 **공분산행렬**)은 이 정보를 하나의 행렬로 정리해 주며, 그 덕분에 선형결합의 분산을 깔끔한 공식으로 쓸 수 있다.

---

## 정의

!!! info "공분산행렬"
    평균벡터가 $\boldsymbol{\mu} = E[\mathbf{X}]$ 인 확률벡터 $\mathbf{X} = (X_1, \ldots, X_n)^T$ 에 대하여 **공분산행렬**은 다음과 같은 $n \times n$ 행렬이다.

    $$
    \boldsymbol{\Sigma} = \text{Cov}(\mathbf{X}) = E\bigl[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T\bigr]
    $$

    그 성분은 $\Sigma_{ij} = \text{Cov}(X_i, X_j)$ 이다.

풀어 쓰면 다음과 같다.

$$
\boldsymbol{\Sigma} = \begin{pmatrix} \text{Var}(X_1) & \text{Cov}(X_1, X_2) & \cdots & \text{Cov}(X_1, X_n) \\ \text{Cov}(X_2, X_1) & \text{Var}(X_2) & \cdots & \text{Cov}(X_2, X_n) \\ \vdots & \vdots & \ddots & \vdots \\ \text{Cov}(X_n, X_1) & \text{Cov}(X_n, X_2) & \cdots & \text{Var}(X_n) \end{pmatrix}
$$

대각 성분은 분산이고 비대각 성분은 공분산이다.

---

## 성질

1. **대칭이다**: $\text{Cov}(X_i, X_j) = \text{Cov}(X_j, X_i)$ 이므로 $\boldsymbol{\Sigma} = \boldsymbol{\Sigma}^T$ 이다.

2. **양의 준정부호이다**: 임의의 벡터 $\mathbf{a} \in \mathbb{R}^n$ 에 대하여 다음이 성립한다.

$$
\mathbf{a}^T \boldsymbol{\Sigma}\, \mathbf{a} = \text{Var}\!\left(\sum_{i=1}^n a_i X_i\right) \geq 0
$$

분산은 언제나 음이 아니기 때문이다.

3. **대각 성분은 음이 아니다**: $\Sigma_{ii} = \text{Var}(X_i) \geq 0$ 이다.

4. **성분이 독립인 경우**: $X_1, \ldots, X_n$ 이 서로 독립이면 $\boldsymbol{\Sigma}$ 는 대각행렬이 된다.

---

## 선형결합의 분산 (행렬 꼴)

일반 공식 $\text{Var}(\sum a_i X_i) = \sum_i \sum_j a_i a_j \text{Cov}(X_i, X_j)$ 는 다음과 같이 간결하게 쓸 수 있다.

$$
\text{Var}(\mathbf{a}^T \mathbf{X}) = \mathbf{a}^T \boldsymbol{\Sigma}\, \mathbf{a}
$$

이는 가중치 $\mathbf{a}$ 에 대한 **이차형식**이다.

---

## 변수가 둘일 때의 예

??? example "두 변수의 공분산행렬"
    $X$ 와 $Y$ 가 $\text{Var}(X) = 4$, $\text{Var}(Y) = 9$, $\text{Cov}(X, Y) = -3$ 을 만족한다고 하자. 그러면 다음과 같다.

    $$
    \boldsymbol{\Sigma} = \begin{pmatrix} 4 & -3 \\ -3 & 9 \end{pmatrix}
    $$

    $\mathbf{a} = (2, 1)^T$ 에 대하여 다음을 얻는다.

    $$
    \text{Var}(2X + Y) = \begin{pmatrix} 2 & 1 \end{pmatrix} \begin{pmatrix} 4 & -3 \\ -3 & 9 \end{pmatrix} \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \end{pmatrix} \begin{pmatrix} 5 \\ 3 \end{pmatrix} = 13
    $$

    확인해 보자. $4(4) + 1(9) + 2(2)(1)(-3) = 16 + 9 - 12 = 13$ 으로 서로 들어맞는다.

---

## 상관행렬

**상관행렬** $\mathbf{R}$ 는 $\boldsymbol{\Sigma}$ 를 표준화한 것이다.

$$
R_{ij} = \frac{\Sigma_{ij}}{\sqrt{\Sigma_{ii}\,\Sigma_{jj}}} = \rho(X_i, X_j)
$$

행렬 기호로 $\mathbf{D} = \text{diag}(\sigma_1, \ldots, \sigma_n)$ 이라 두면 다음과 같다.

$$
\mathbf{R} = \mathbf{D}^{-1} \boldsymbol{\Sigma}\, \mathbf{D}^{-1}
$$

상관행렬은 대각에 1이 놓이고 비대각에 상관계수가 놓인다.

---

## 선형변환

행렬 $\mathbf{A}$ 와 벡터 $\mathbf{b}$ 에 대하여 $\mathbf{Y} = \mathbf{A}\mathbf{X} + \mathbf{b}$ 라 하면 다음이 성립한다.

$$
\text{Cov}(\mathbf{Y}) = \mathbf{A}\,\boldsymbol{\Sigma}\,\mathbf{A}^T
$$

이는 스칼라에서의 규칙 $\text{Var}(aX + b) = a^2\text{Var}(X)$ 를 일반화한 것이다.

---

## 파이썬 예제

```python
import numpy as np

# 공분산행렬을 정의한다
Sigma = np.array([[4, -3],
                  [-3, 9]])

# 양의 준정부호인지 확인한다
eigenvalues = np.linalg.eigvalsh(Sigma)
print(f"Eigenvalues: {eigenvalues}")  # 둘 다 음이 아니다
print(f"Positive semi-definite: {all(eigenvalues >= 0)}")

# 2X + Y 의 분산
a = np.array([2, 1])
var_linear = a @ Sigma @ a
print(f"Var(2X + Y) = {var_linear}")  # 13

# 상관행렬
D_inv = np.diag(1 / np.sqrt(np.diag(Sigma)))
R = D_inv @ Sigma @ D_inv
print(f"Correlation matrix:\n{R}")
```

## 연습문제

**연습문제 1.** 어떤 포트폴리오의 가중치가 $\mathbf{a} = (0.4, 0.4, 0.2)^T$ 이고 자산들의 공분산행렬이 다음과 같다고 하자.

$$
\boldsymbol{\Sigma} = \begin{pmatrix} 0.04 & 0.02 & -0.01 \\ 0.02 & 0.09 & 0.03 \\ -0.01 & 0.03 & 0.16 \end{pmatrix}
$$

포트폴리오의 분산 $\mathbf{a}^T \boldsymbol{\Sigma} \, \mathbf{a}$ 를 구하고 $\boldsymbol{\Sigma}$ 가 양의 준정부호임을 확인하여라.

??? success "연습문제 1 풀이"
    먼저 $\boldsymbol{\Sigma} \mathbf{a}$ 를 구한다.

    $$
    \boldsymbol{\Sigma} \mathbf{a} = \begin{pmatrix} 0.04(0.4) + 0.02(0.4) - 0.01(0.2) \\ 0.02(0.4) + 0.09(0.4) + 0.03(0.2) \\ -0.01(0.4) + 0.03(0.4) + 0.16(0.2) \end{pmatrix} = \begin{pmatrix} 0.022 \\ 0.050 \\ 0.040 \end{pmatrix}
    $$

    그러면 다음을 얻는다.

    $$
    \mathbf{a}^T \boldsymbol{\Sigma} \mathbf{a} = 0.4(0.022) + 0.4(0.050) + 0.2(0.040) = 0.0088 + 0.020 + 0.008 = 0.0368
    $$

    **양의 준정부호인지 확인하기.** 대칭행렬이 양의 준정부호일 필요충분조건은 모든 고윳값이 음이 아닌 것이다(같은 말로, 모든 선행 주소행렬식이 음이 아닌 것이다). $\boldsymbol{\Sigma}$ 의 주소행렬식은 다음과 같다.

    - $1 \times 1$: $0.04 > 0$
    - $2 \times 2$: $0.04 \cdot 0.09 - 0.02^2 = 0.0036 - 0.0004 = 0.0032 > 0$
    - $3 \times 3$: $\det \boldsymbol{\Sigma} = 0.04(0.09 \cdot 0.16 - 0.03^2) - 0.02(0.02 \cdot 0.16 - 0.03 \cdot (-0.01)) + (-0.01)(0.02 \cdot 0.03 - 0.09 \cdot (-0.01))$

    $= 0.04(0.0144 - 0.0009) - 0.02(0.0032 + 0.0003) - 0.01(0.0006 + 0.0009)$

    $= 0.04 \cdot 0.0135 - 0.02 \cdot 0.0035 - 0.01 \cdot 0.0015$

    $= 0.00054 - 0.00007 - 0.000015 = 0.000455 > 0$.

    모든 주소행렬식이 양수이므로 $\boldsymbol{\Sigma}$ 는 양의 정부호이고, 따라서 양의 준정부호이기도 하다.
