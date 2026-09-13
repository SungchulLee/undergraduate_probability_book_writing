# 확률변수 합의 평균과 분산

## 합의 평균

### 일반적인 경우

**임의의** 확률변수 $X_1, X_2, \ldots, X_n$ 에 대하여(서로 독립일 필요가 없다) 다음이 성립한다.

$$
E\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n E[X_i]
$$

이는 **기댓값의 선형성**에서 곧바로 따라 나온다.

### i.i.d. 인 경우

$X_1, \ldots, X_n$ 이 i.i.d.(독립이고 같은 분포를 따른다)이면 다음이 성립한다.

$$
E\left[\sum_{i=1}^n X_i\right] = n \, E[X_1]
$$

---

## 합의 분산

### 일반적인 경우

$$
\text{Var}\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i) + \sum_{i \neq j} \text{Cov}(X_i, X_j)
= \sum_{i=1}^n \text{Var}(X_i) + 2\sum_{1 \leq i < j \leq n} \text{Cov}(X_i, X_j)
$$

### 독립인 경우

$X_1, \ldots, X_n$ 이 **독립**이면 다음이 성립한다.

$$
\text{Var}\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i)
$$

### i.i.d. 인 경우

$X_1, \ldots, X_n$ 이 **i.i.d.** 이면 다음이 성립한다.

$$
\text{Var}\left(\sum_{i=1}^n X_i\right) = n \, \text{Var}(X_1)
$$

---

## 가중합

### 일반적인 경우

상수 $a_1, a_2, \ldots, a_n$ 에 대하여 다음이 성립한다.

$$
E\left[\sum_{i=1}^n a_i X_i\right] = \sum_{i=1}^n a_i E[X_i]
$$

$$
\text{Var}\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2 \, \text{Var}(X_i) + 2\sum_{1 \leq i < j \leq n} a_i a_j \, \text{Cov}(X_i, X_j)
$$

### 독립인 경우

$$
\text{Var}\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2 \, \text{Var}(X_i)
$$

### i.i.d. 인 경우

$$
E\left[\sum_{i=1}^n a_i X_i\right] = \left(\sum_{i=1}^n a_i\right) E[X_1]
$$

$$
\text{Var}\left(\sum_{i=1}^n a_i X_i\right) = \left(\sum_{i=1}^n a_i^2\right) \text{Var}(X_1)
$$

---

## 행렬로 나타내기

$\mathbf{a} = (a_1, \ldots, a_n)^T$ 와 $\mathbf{X} = (X_1, \ldots, X_n)^T$ 에 대하여 $S = \sum_{i=1}^n a_i X_i = \mathbf{a}^T \mathbf{X}$ 라 하자.

다음과 같이 두자.

- $\mu_i = E[X_i]$: $X_i$ 의 평균
- $\sigma_i^2 = \text{Var}(X_i)$: $X_i$ 의 분산
- $\sigma_{ij} = \text{Cov}(X_i, X_j)$: $X_i$ 와 $X_j$ 의 공분산
- $\rho_{ij}$: $X_i$ 와 $X_j$ 의 상관계수

**평균**:

$$
E[S] = \sum_{i=1}^n a_i \mu_i = \mathbf{a}^T \boldsymbol{\mu}
$$

**분산**:

$$
\text{Var}(S) = \sum_{i=1}^n a_i^2 \sigma_i^2 + 2\sum_{1 \leq i < j \leq n} a_i a_j \sigma_{ij}
= \sum_{i=1}^n a_i^2 \sigma_i^2 + 2\sum_{1 \leq i < j \leq n} a_i a_j \rho_{ij} \sigma_i \sigma_j
$$

행렬로 쓰면 다음과 같다.

$$
\text{Var}(S) = \mathbf{a}^T \boldsymbol{\Sigma} \, \mathbf{a}
$$

여기서 **공분산행렬**은 다음과 같다.

$$
\boldsymbol{\Sigma} = \begin{pmatrix}
\sigma_1^2 & \sigma_{12} & \cdots & \sigma_{1n} \\
\sigma_{21} & \sigma_2^2 & \cdots & \sigma_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{n1} & \sigma_{n2} & \cdots & \sigma_n^2
\end{pmatrix}
$$

---

## 분해의 예

### 예제 1: 베르누이로 보는 이항분포

앞면이 나올 확률이 $p$ 인 동전을 서로 독립으로 $n$ 번 던진다. $\mathbf{1}_{A_i} \stackrel{iid}{\sim} \text{Bernoulli}(p)$ 라 하자.

$$
S = \sum_{i=1}^n \mathbf{1}_{A_i} \sim \text{Binomial}(n, p)
$$

$$
E[S] = \sum_{i=1}^n E[\mathbf{1}_{A_i}] = np
$$

$$
\text{Var}(S) = \sum_{i=1}^n \text{Var}(\mathbf{1}_{A_i}) = npq
$$

### 예제 2: 기하분포로 보는 음이항분포

앞면이 나올 확률이 $p$ 인 동전을 $r$ 번째 앞면이 나올 때까지 던진다. $X_i \stackrel{iid}{\sim} \text{Geo}(p)$ 를 $(i-1)$ 번째 앞면 다음부터 $i$ 번째 앞면이 나올 때까지 던진 횟수라 하자.

$$
S = \sum_{i=1}^r X_i \sim \text{NB}(r, p)
$$

$$
E[S] = \sum_{i=1}^r E[X_i] = \frac{r}{p}
$$

$$
\text{Var}(S) = \sum_{i=1}^r \text{Var}(X_i) = \frac{rq}{p^2}
$$

### 예제 3: 주사위를 1000번 던지기

주사위를 1000번 던진다. 홀수 눈이 나오면 그 눈만큼 얻고, 짝수 눈이 나오면 그 눈만큼 잃는다. 게임마다 $+0.5$ 의 덤을 얹으면 다음과 같다.

$$
D_i = \begin{cases} +1 & \text{확률 } 1/6 \\ -2 & \text{확률 } 1/6 \\ +3 & \text{확률 } 1/6 \\ -4 & \text{확률 } 1/6 \\ +5 & \text{확률 } 1/6 \\ -6 & \text{확률 } 1/6 \end{cases}
\qquad X_i = D_i + 0.5
$$

$D_i$ 의 적률을 구하면 다음과 같다.

$$
E[D_i] = \frac{1 - 2 + 3 - 4 + 5 - 6}{6} = \frac{-3}{6} = -0.5
$$

$$
E[D_i^2] = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6} \approx 15.1667
$$

$$
\text{Var}(D_i) = E[D_i^2] - (E[D_i])^2 = 15.1667 - 0.25 = 14.9167
$$

$X_i = D_i + 0.5$ 이므로 $E[X_i] = 0$ 이고 $\text{Var}(X_i) = 14.9167$ 이다.

전체 손익 $S = \sum_{i=1}^{1000} X_i$ 에 대해서는 다음과 같다.

$$
E[S] = 1000 \times 0 = 0
$$

$$
\text{Var}(S) = 1000 \times 14.9167 = 14916.7, \quad \text{SD}(S) \approx 122.1
$$

### 예제 4: 쿠폰 모으기 문제

$n$ 가지 장난감을 모두 모으는 데 걸리는 시간을 보자. $\tau_i \sim \text{Geo}\left(\frac{n-(i-1)}{n}\right)$ 가 서로 독립이라 하고 $T_n = \sum_{i=1}^n \tau_i$ 라 하면 다음을 얻는다.

$$
E[T_n] = \sum_{i=1}^n \frac{n}{n - (i-1)} = n\left(1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}\right) = nH_n \sim n\log n
$$

$$
\text{Var}(T_n) = \sum_{k=1}^n \frac{1 - k/n}{(k/n)^2} = n^2 \sum_{k=1}^n \frac{1}{k^2} - n\sum_{k=1}^n \frac{1}{k} \approx \frac{\pi^2}{6} n^2 - n\log n
$$

---

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 예: 주사위를 1000번 던지기
# ============================================================
np.random.seed(42)
NumSimu = 10000
NumRolling = 1000

# 주사위 던지기 생성
rolls = np.random.randint(1, 7, size=(NumRolling, NumSimu))

# 손익으로 바꾸기: 홀수 눈 -> +값, 짝수 눈 -> -값
increment = np.where(rolls % 2 == 1, rolls, -rolls).astype(float)
increment += 0.5  # 덤

# 누적 손익
Sn = np.cumsum(increment, axis=0)

# 이론값
E_D = (-3) / 6
Var_D = 91/6 - 0.25
print(f"E[D_i] = {E_D:.4f}")
print(f"Var(D_i) = {Var_D:.4f}")
print(f"E[X_i] = {E_D + 0.5:.4f}")
print(f"Var(X_i) = {Var_D:.4f}")
print(f"E[S] = {1000 * (E_D + 0.5):.4f}")
print(f"Var(S) = {1000 * Var_D:.4f}")
print(f"SD(S) = {np.sqrt(1000 * Var_D):.4f}")

# 모의실험으로 확인
total_pnl = Sn[-1, :]
print(f"\nSimulated E[S] = {np.mean(total_pnl):.4f}")
print(f"Simulated SD(S) = {np.std(total_pnl):.4f}")

# 그림
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].hist(total_pnl, bins=50, edgecolor='black')
axes[0].set_xlabel('Total P&L')
axes[0].set_title('Histogram of Total P&L after 1000 Games')
axes[0].grid(True, alpha=0.3)

axes[1].plot(range(1, NumRolling + 1), Sn[:, 0])
axes[1].set_xlabel('Game number')
axes[1].set_ylabel('Cumulative P&L')
axes[1].set_title('Sample Path of Cumulative P&L')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('dice_1000_pnl.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# 쿠폰 모으기
# ============================================================
n_toys = 50
harmonic = sum(1/k for k in range(1, n_toys + 1))
E_Tn = n_toys * harmonic
Var_Tn = n_toys**2 * sum(1/k**2 for k in range(1, n_toys + 1)) - n_toys * harmonic
print(f"\nCoupon Collector (n={n_toys}):")
print(f"E[T_n] = {E_Tn:.2f}")
print(f"SD(T_n) = {np.sqrt(Var_Tn):.2f}")

# ============================================================
# 행렬 표현의 예
# ============================================================
# 자산 3개로 이루어진 포트폴리오의 분산
a = np.array([0.4, 0.35, 0.25])  # 비중
sigma = np.array([0.20, 0.15, 0.25])  # 각 자산의 표준편차
rho = np.array([[1.0, 0.3, 0.1],
                [0.3, 1.0, 0.5],
                [0.1, 0.5, 1.0]])  # 상관행렬

# 공분산행렬 만들기
Sigma = np.outer(sigma, sigma) * rho
portfolio_var = a @ Sigma @ a
print(f"\nPortfolio Example:")
print(f"Weights: {a}")
print(f"Asset SDs: {sigma}")
print(f"Portfolio Var = a'Σa = {portfolio_var:.6f}")
print(f"Portfolio SD = {np.sqrt(portfolio_var):.4f}")
```

## 연습문제

**연습문제 1.** $X_1, \ldots, X_{100}$ 을 $E[X_i] = 2$, $\text{Var}(X_i) = 9$ 인 i.i.d. 확률변수라 하자. $E[\sum X_i]$ 와 $\text{Var}(\sum X_i)$ 를 구하여라.

??? success "연습문제 1 풀이"
    선형성에 따라 다음을 얻는다.

    $$
    E\!\left[\sum_{i=1}^{100} X_i\right] = 100 \cdot 2 = 200
    $$

    독립성에 따라 다음을 얻는다.

    $$
    \text{Var}\!\left(\sum_{i=1}^{100} X_i\right) = 100 \cdot 9 = 900
    $$

---

**연습문제 2.** $X_1, X_2, X_3$ 가 서로 독립이고 평균이 각각 $1, 2, 3$, 분산이 각각 $4, 1, 9$ 일 때 $S = 3 X_1 - 2 X_2 + X_3$ 의 $E[S]$ 와 $\text{Var}(S)$ 를 구하여라.

??? success "연습문제 2 풀이"
    $$
    E[S] = 3(1) - 2(2) + 1(3) = 3 - 4 + 3 = 2
    $$

    $$
    \text{Var}(S) = 3^2 \cdot 4 + (-2)^2 \cdot 1 + 1^2 \cdot 9 = 36 + 4 + 9 = 49
    $$

    (독립성에 따라 교차항은 사라진다. $a < 0$ 일 때도 $\text{Var}(aX) = a^2 \text{Var}(X)$ 임에 주의하자.)

---

**연습문제 3.** 어떤 포트폴리오의 비중이 $a = (0.5, 0.3, 0.2)$ 이고 자산의 공분산행렬이 다음과 같다.

$$
\Sigma = \begin{pmatrix} 0.04 & 0.01 & 0.02 \\ 0.01 & 0.09 & 0.03 \\ 0.02 & 0.03 & 0.16 \end{pmatrix}
$$

포트폴리오의 분산 $\mathbf{a}^T \Sigma \mathbf{a}$ 를 구하여라.

??? success "연습문제 3 풀이"
    먼저 $\Sigma \mathbf{a}$ 를 구하자.

    $$
    \Sigma \mathbf{a} = \begin{pmatrix} 0.04 \cdot 0.5 + 0.01 \cdot 0.3 + 0.02 \cdot 0.2 \\ 0.01 \cdot 0.5 + 0.09 \cdot 0.3 + 0.03 \cdot 0.2 \\ 0.02 \cdot 0.5 + 0.03 \cdot 0.3 + 0.16 \cdot 0.2 \end{pmatrix} = \begin{pmatrix} 0.027 \\ 0.038 \\ 0.051 \end{pmatrix}
    $$

    그러면 다음을 얻는다.

    $$
    \mathbf{a}^T \Sigma \mathbf{a} = 0.5(0.027) + 0.3(0.038) + 0.2(0.051) = 0.0135 + 0.0114 + 0.0102 = 0.0351
    $$

    포트폴리오의 표준편차는 $\approx \sqrt{0.0351} \approx 0.1873$ 이다.

---

**연습문제 4.** 공정한 정육면체 주사위 두 개를 던질 때 나온 눈의 합의 기댓값은 얼마인가?

??? success "연습문제 4 풀이"
    $X_1$ 과 $X_2$ 를 두 주사위의 눈이라 하자. 각 주사위의 기댓값은 다음과 같다.

    $$
    E[X_1] = E[X_2] = \frac{1 + 2 + 3 + 4 + 5 + 6}{6} = 3.5
    $$

    기댓값의 선형성에 따라 다음을 얻는다.

    $$
    E[X_1 + X_2] = E[X_1] + E[X_2] = 3.5 + 3.5 = 7
    $$
