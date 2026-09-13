# 도착간격에서 얻는 지수분포

## 왜 필요한가: 첫 도착을 기다리기

비율이 $\lambda$ 인 **푸아송 과정**에서는 시간축을 따라 사건이 무작위로 일어난다. 잇달아 일어나는 두 사건 사이의 간격, 곧 **도착간격**은 **지수분포**를 따른다.

시각 $0$ 이후 첫 도착이 일어나는 시각을 $T_1$ 이라 하자. 그러면 다음이 성립한다.

$$P(T_1 > t) = P(\text{구간 } [0, t] \text{ 안에 도착이 없음}) = e^{-\lambda t}$$

$[0, t]$ 안의 도착 횟수가 $\text{Po}(\lambda t)$ 를 따르고 $P(N(t) = 0) = e^{-\lambda t}$ 이기 때문이다.

## 정의

!!! info "지수분포"
    연속확률변수 $X$ 의 확률밀도함수가 다음과 같으면, $X$ 는 비율모수가 $\lambda > 0$ 인 **지수분포**를 따른다고 하고 $X \sim \text{Exp}(\lambda)$ 로 적는다.

    $$f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$$

### 누적분포함수와 생존함수

**누적분포함수**는 다음과 같다.

$$F(x) = P(X \leq x) = 1 - e^{-\lambda x}, \quad x \geq 0$$

**생존함수**(꼬리확률)는 다음과 같다.

$$\bar{F}(x) = P(X > x) = e^{-\lambda x}, \quad x \geq 0$$

생존함수의 모양이 유난히 깔끔해서 지수분포는 다루기가 쉽다.

### 푸아송 과정과의 연결

비율이 $\lambda$ 인 푸아송 과정에서는 다음이 성립한다.

- 첫 도착까지 걸리는 시간 $T_1$ 은 $\text{Exp}(\lambda)$ 를 따른다
- 잇달아 일어나는 사건 사이의 도착간격 $T_1, T_2, T_3, \ldots$ 는 **독립이고 같은 분포를 따르는**(i.i.d.) $\text{Exp}(\lambda)$ 이다

이것이 사건의 개수를 세는 푸아송 과정과 대기시간을 재는 지수분포를 이어 주는 근본적인 고리이다.

### 기하분포와의 관계

지수분포는 기하분포의 **연속판**이다.

| 성질 | 기하분포 | 지수분포 |
|----------|-----------|-------------|
| 정의역 | 이산 ($1, 2, 3, \ldots$) | 연속 ($[0, \infty)$) |
| 무기억성 | 있다 | 있다 |
| 뜻 | 첫 성공까지의 시행 횟수 | 첫 사건까지의 시간 |
| 모수 | $p$ (성공확률) | $\lambda$ (비율) |
| 평균 | $1/p$ | $1/\lambda$ |
| 분산 | $q/p^2$ | $1/\lambda^2$ |

### 감마분포와의 관계

지수분포는 감마분포의 특별한 경우이다.

$$\text{Exp}(\lambda) \stackrel{d}{=} \Gamma(1, \lambda)$$

두 확률밀도함수를 견주어 보면 이것은 바로 나온다.

$$\lambda e^{-\lambda x} = \frac{\lambda(\lambda x)^{1-1} e^{-\lambda x}}{\Gamma(1)}, \quad x \geq 0$$

$\Gamma(1) = 1$ 이고 $(\lambda x)^0 = 1$ 이기 때문이다.

## 모의실험

균등확률변수 $U \sim U(0,1)$ 에서 $X \sim \text{Exp}(\lambda)$ 를 만들려면 **역누적분포함수 방법**을 쓴다.

$$X = F^{-1}(U) = -\frac{1}{\lambda} \log(1 - U)$$

$U \sim U(0,1)$ 이면 $1 - U \sim U(0,1)$ 이므로 이 식은 다음과 같이 간단해진다.

$$X = -\frac{1}{\lambda} \log(U) \sim \text{Exp}(\lambda)$$

??? example "예: Exp(0.5) 모의실험하기"
    $U \sim U(0,1)$ 이 주어졌을 때 $X \sim \text{Exp}(0.5)$ 를 만들어 보자.

    누적분포함수는 $x \geq 0$ 에 대하여 $F(x) = 1 - e^{-0.5x}$ 이다.

    $u = 1 - e^{-0.5x}$ 로 놓고 풀면 다음을 얻는다.

    $$x = -2\log(1 - u)$$

    따라서 $X = -2\log(1 - U) \sim \text{Exp}(0.5)$ 이다.

    간단히 한 꼴을 쓰면 $X = -2\log(U) \sim \text{Exp}(0.5)$ 이다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 모수
lam = 2.0  # 비율모수

# 확률밀도함수와 누적분포함수
x = np.linspace(0, 4, 200)
pdf = lam * np.exp(-lam * x)
cdf = 1 - np.exp(-lam * x)

# 역누적분포함수 방법을 이용한 모의실험
np.random.seed(42)
n_sim = 10000
U = np.random.uniform(0, 1, n_sim)
X_sim = -np.log(U) / lam

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 확률밀도함수
axes[0].plot(x, pdf, 'b-', lw=2)
axes[0].set_title(f'PDF of Exp({lam})')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].grid(True, alpha=0.3)

# 누적분포함수
axes[1].plot(x, cdf, 'r-', lw=2)
axes[1].set_title(f'CDF of Exp({lam})')
axes[1].set_xlabel('x')
axes[1].set_ylabel('F(x)')
axes[1].grid(True, alpha=0.3)

# 모의실험 히스토그램과 이론적 확률밀도함수
axes[2].hist(X_sim, bins=50, density=True, alpha=0.7, label='Simulated')
axes[2].plot(x, pdf, 'r-', lw=2, label='Theoretical PDF')
axes[2].set_title('Inverse CDF Simulation')
axes[2].set_xlabel('x')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('exponential_definition.png', dpi=150, bbox_inches='tight')
plt.show()

# 적률 확인
print(f"Theoretical mean: {1/lam:.4f}")
print(f"Simulated mean:   {np.mean(X_sim):.4f}")
print(f"Theoretical var:  {1/lam**2:.4f}")
print(f"Simulated var:    {np.var(X_sim):.4f}")
```

## 연습문제

**연습문제 1.**
$X \sim \text{Exp}(3)$ 이라 하자.

(a) $P(X > 2)$ 를 구하여라.

(b) $P(1 < X < 4)$ 를 구하여라.

(c) $X$ 의 중앙값을 구하여라.

??? success "연습문제 1 풀이"
    (a) $P(X > 2) = e^{-3 \cdot 2} = e^{-6} \approx 0.00248$

    (b) $P(1 < X < 4) = e^{-3} - e^{-12} \approx 0.0498$

    (c) $1 - e^{-3m} = 1/2$ 를 풀면 $m = \frac{\ln 2}{3} \approx 0.231$ 이다
