# 평균과 분산

## 평균

!!! info "Exp(λ) 의 평균"
    $X \sim \text{Exp}(\lambda)$ 이면 다음이 성립한다.

    $$E[X] = \frac{1}{\lambda}$$

### 유도

$u = x$, $dv = \lambda e^{-\lambda x} dx$ 로 놓고 부분적분을 하면 다음을 얻는다.

$$E[X] = \int_0^\infty x \lambda e^{-\lambda x} \, dx = \left[-x e^{-\lambda x}\right]_0^\infty + \int_0^\infty e^{-\lambda x} \, dx = 0 + \frac{1}{\lambda} = \frac{1}{\lambda}$$

### 뜻풀이

평균 $1/\lambda$ 은 비율이 $\lambda$ 인 푸아송 과정에서 사건 사이의 **평균 대기시간**이다. 사건이 시간당 $\lambda = 5$ 의 비율로 일어난다면 사건 사이의 평균 시간은 $1/5$ 시간, 곧 $12$ 분이다.

## 분산

!!! info "Exp(λ) 의 분산"
    $X \sim \text{Exp}(\lambda)$ 이면 다음이 성립한다.

    $$\text{Var}(X) = \frac{1}{\lambda^2}$$

### 유도

먼저 부분적분(또는 감마함수를 쓰는 방법)으로 $E[X^2]$ 을 구한다.

$$E[X^2] = \int_0^\infty x^2 \lambda e^{-\lambda x} \, dx$$

$u = \lambda x$ 로 치환하면 다음을 얻는다.

$$E[X^2] = \frac{1}{\lambda^2} \int_0^\infty u^2 e^{-u} \, du = \frac{\Gamma(3)}{\lambda^2} = \frac{2!}{\lambda^2} = \frac{2}{\lambda^2}$$

따라서 다음이 성립한다.

$$\text{Var}(X) = E[X^2] - (E[X])^2 = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}$$

### 표준편차

$$\text{SD}(X) = \frac{1}{\lambda} = E[X]$$

눈여겨볼 성질이 하나 있다. 지수분포에서는 **표준편차가 평균과 같다**. 따라서 변동계수는 비율모수가 무엇이든 늘 $1$ 이다.

## 고차 적률

감마함수를 쓰면 $X \sim \text{Exp}(\lambda)$ 의 $n$ 차 적률은 다음과 같다.

$$E[X^n] = \int_0^\infty x^n \lambda e^{-\lambda x} \, dx = \frac{\Gamma(n+1)}{\lambda^n} = \frac{n!}{\lambda^n}$$

## 요약 표

지수분포는 이산분포와 연속분포를 잇는 더 큰 얼개 안에 놓인다.

| 분포 | 평균 | 분산 |
|:---:|:---:|:---:|
| $\text{Geo}(p)$ | $\dfrac{1}{p}$ | $\dfrac{q}{p^2}$ |
| $\text{NegBin}(n, p)$ | $\dfrac{n}{p}$ | $\dfrac{nq}{p^2}$ |
| $\text{Exp}(\lambda)$ | $\dfrac{1}{\lambda}$ | $\dfrac{1}{\lambda^2}$ |
| $\Gamma(n, \lambda)$ | $\dfrac{n}{\lambda}$ | $\dfrac{n}{\lambda^2}$ |
| $\Gamma(\alpha, \lambda)$ | $\dfrac{\alpha}{\lambda}$ | $\dfrac{\alpha}{\lambda^2}$ |

기하분포와 음이항분포의 관계는 지수분포와 감마분포의 관계와 같다. 곧 i.i.d. 인 것을 $n$ 개 더한 것이다.

## 지수분포의 적률생성함수

$X \sim \text{Exp}(\lambda)$ 의 적률생성함수(MGF)는 다음과 같다.

$$M_X(t) = E[e^{tX}] = \int_0^\infty e^{tx} \lambda e^{-\lambda x} \, dx = \frac{\lambda}{\lambda - t}, \quad t < \lambda$$

이것으로 적률을 확인할 수 있다.

$$M_X'(0) = \frac{\lambda}{(\lambda - t)^2}\bigg|_{t=0} = \frac{1}{\lambda} = E[X]$$

$$M_X''(0) = \frac{2\lambda}{(\lambda - t)^3}\bigg|_{t=0} = \frac{2}{\lambda^2} = E[X^2]$$

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# 여러 비율에 대해 평균과 분산을 비교한다
rates = [0.5, 1.0, 2.0, 5.0]
n_sim = 50000

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for lam in rates:
    X = np.random.exponential(1/lam, n_sim)
    x = np.linspace(0, 6, 200)
    pdf = lam * np.exp(-lam * x)

    axes[0].plot(x, pdf, lw=2, label=f'λ={lam}, E[X]={1/lam:.2f}')
    axes[0].axvline(1/lam, linestyle='--', alpha=0.3)

axes[0].set_title('Exponential PDFs with Means Marked')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 평균 = 표준편차 성질 확인
lam_range = np.linspace(0.2, 5, 50)
means = 1 / lam_range
stds = 1 / lam_range

axes[1].plot(lam_range, means, 'b-', lw=2, label='E[X] = 1/λ')
axes[1].plot(lam_range, stds, 'r--', lw=2, label='SD(X) = 1/λ')
axes[1].set_title('Mean Equals Standard Deviation')
axes[1].set_xlabel('λ')
axes[1].set_ylabel('Value')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('exponential_mean_variance.png', dpi=150, bbox_inches='tight')
plt.show()

# 수치로 확인하기
for lam in rates:
    X = np.random.exponential(1/lam, n_sim)
    print(f"λ = {lam}: E[X] = {np.mean(X):.4f} (theory {1/lam:.4f}), "
          f"Var(X) = {np.var(X):.4f} (theory {1/lam**2:.4f})")
```


## 연습문제

**연습문제 1.**
균등확률변수 $U \sim U(0,1)$ 을 써서 확률변수 $X \sim \text{Exp}(0.5)$ 를 만들어라.

??? success "연습문제 1 풀이"
    $F(x) = 1 - e^{-0.5x}$ 이므로 $X = F^{-1}(U) = -2\log(1 - U) \sim \text{Exp}(0.5)$ 이다.

    $1 - U \sim U(0,1)$ 이므로 $X = -2\log(U) \sim \text{Exp}(0.5)$ 로 간단히 할 수 있다.

---

**연습문제 2.**
기계 A와 기계 B의 수명은 서로 독립이고, 각각 비율이 $\lambda_A = 0.1$ 과 $\lambda_B = 0.2$ (연 단위)인 지수분포를 따른다. 두 기계 가운데 처음으로 하나가 고장 날 때까지 걸리는 시간의 기댓값을 구하여라.

??? success "연습문제 2 풀이"
    $\min(T_A, T_B) \sim \text{Exp}(\lambda_A + \lambda_B) = \text{Exp}(0.3)$ 이다.

    $E[\min(T_A, T_B)] = \frac{1}{0.3} \approx 3.33$ 년이다.
