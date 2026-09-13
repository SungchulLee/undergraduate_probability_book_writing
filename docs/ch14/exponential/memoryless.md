# 무기억성

## 무기억성이란

지수분포에는 눈에 띄는 성질이 하나 있다. 바로 **미래가 과거와 무관하다**는 것이다. 시간 $s$ 만큼 기다렸는데도 아직 사건이 일어나지 않았다면, 남은 대기시간의 분포는 방금 기다리기 시작했을 때와 똑같다.

!!! info "무기억성"
    $X \sim \text{Exp}(\lambda)$ 이면 모든 $s, t \geq 0$ 에 대하여 다음이 성립한다.

    $$P(X > s + t \mid X > s) = P(X > t)$$

    같은 말로, 시각 $s$ 까지 사건이 일어나지 않았다는 조건 아래에서 첫 사건까지 남은 시간은 여전히 $\text{Exp}(\lambda)$ 분포를 따른다.

### 증명

$$P(X > s + t \mid X > s) = \frac{P(X > s + t)}{P(X > s)} = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = e^{-\lambda t} = P(X > t)$$

핵심은 지수함수의 곱셈 성질 $e^{-\lambda(s+t)} = e^{-\lambda s} \cdot e^{-\lambda t}$ 이다.

## 유일성

지수분포는 무기억성을 갖는 **유일한 연속분포**이다. 마찬가지로 기하분포는 이 성질을 갖는 유일한 이산분포이다.

!!! note "특성화 정리"
    $X$ 가 양의 값을 갖는 연속확률변수이고 모든 $s, t \geq 0$ 에 대하여 $P(X > s + t \mid X > s) = P(X > t)$ 를 만족하면, 어떤 $\lambda > 0$ 에 대하여 $X \sim \text{Exp}(\lambda)$ 이다.

### 증명의 얼개

무기억성은 생존함수가 다음을 만족한다는 뜻이다.

$$\bar{F}(s + t) = \bar{F}(s) \cdot \bar{F}(t)$$

$\bar{F}(0) = 1$ 이고 $\bar{F}(t) \to 0$ 인 이 함수방정식(코시의 지수방정식)의 연속인 해는 $\lambda > 0$ 에 대한 $\bar{F}(t) = e^{-\lambda t}$ 뿐이다.

## 뜻풀이와 따라 나오는 결과

### "새로 시작하는" 성질

푸아송 과정이 진행되는 어느 시점에서든, 다음 사건까지 걸리는 시간은 마지막 사건이 언제 일어났는지와 상관없이 $\text{Exp}(\lambda)$ 분포를 따른다. 푸아송 과정을 두고 "기억이 없다"거나 "뒤끝이 없다"고 말하는 까닭이 여기에 있다.

### 독립인 지수확률변수의 최솟값

$X_1 \sim \text{Exp}(\lambda_1)$ 과 $X_2 \sim \text{Exp}(\lambda_2)$ 가 독립이면 다음이 성립한다.

$$\min(X_1, X_2) \sim \text{Exp}(\lambda_1 + \lambda_2)$$

왜냐하면 다음이 성립하기 때문이다.

$$P(\min(X_1, X_2) > t) = P(X_1 > t) P(X_2 > t) = e^{-\lambda_1 t} e^{-\lambda_2 t} = e^{-(\lambda_1 + \lambda_2)t}$$

### 위험률

지수분포의 **위험률**(고장률)은 일정하다.

$$h(t) = \frac{f(t)}{\bar{F}(t)} = \frac{\lambda e^{-\lambda t}}{e^{-\lambda t}} = \lambda$$

위험률이 일정하다는 것은 무기억성과 같은 말이다. 곧 지수분포는 시스템이 얼마나 오래 돌아갔든 상관없이 바로 다음 순간에 고장 날 확률이 늘 같은 상황을 나타내는 모형이다.

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
lam = 1.0
n_sim = 100000

# Exp(lambda) 표본 생성
X = np.random.exponential(1/lam, n_sim)

# 무기억성 보이기
s = 2.0  # X > s 를 조건으로 준다
X_conditional = X[X > s] - s  # X > s 일 때 남은 시간
X_unconditional = X  # 조건을 주지 않은 분포

# 비교 그림
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 히스토그램 비교
t_vals = np.linspace(0, 6, 200)
axes[0].hist(X_unconditional, bins=80, density=True, alpha=0.5,
             range=(0, 6), label='Unconditional X', color='blue')
axes[0].hist(X_conditional, bins=80, density=True, alpha=0.5,
             range=(0, 6), label=f'X - {s} | X > {s}', color='red')
axes[0].plot(t_vals, lam * np.exp(-lam * t_vals), 'k-', lw=2,
             label='Exp(1) PDF')
axes[0].set_title('Memoryless Property Demonstration')
axes[0].set_xlabel('t')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 생존함수 비교
t_grid = np.linspace(0, 5, 100)
surv_uncond = np.array([np.mean(X > t) for t in t_grid])
surv_cond = np.array([np.mean(X_conditional > t) for t in t_grid])
surv_theory = np.exp(-lam * t_grid)

axes[1].plot(t_grid, surv_uncond, 'b-', lw=2, alpha=0.7,
             label='P(X > t)')
axes[1].plot(t_grid, surv_cond, 'r--', lw=2, alpha=0.7,
             label=f'P(X > {s}+t | X > {s})')
axes[1].plot(t_grid, surv_theory, 'k:', lw=2,
             label='e^{-λt} (theory)')
axes[1].set_title('Survival Function Comparison')
axes[1].set_xlabel('t')
axes[1].set_ylabel('Probability')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('memoryless_property.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.**
어떤 전구의 수명이 평균 1000시간인 지수분포를 따른다고 하자. 이 전구가 이미 500시간 동안 켜져 있었다면, 앞으로 남은 수명의 기댓값은 얼마인가?

??? success "연습문제 1 풀이"
    무기억성에 따라 남은 수명은 여전히 평균이 1000시간인 $\text{Exp}(1/1000)$ 을 따른다. 이미 지나간 500시간은 남은 시간에 대해 아무런 정보도 주지 않는다.
