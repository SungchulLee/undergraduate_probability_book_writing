# k번째 도착까지의 대기시간

## k번째 도착시각

비율이 $\lambda$ 인 푸아송 과정에서 $k$ 번째 도착이 일어나는 시각을 $S_k$ 라 하자. 도착간격 $T_1, T_2, \ldots, T_k$ 가 i.i.d. $\text{Exp}(\lambda)$ 이므로 다음이 성립한다.

$$S_k = T_1 + T_2 + \cdots + T_k \sim \Gamma(k, \lambda) = \text{Erlang}(k, \lambda)$$

### Sₖ 의 평균과 분산

$$E[S_k] = \frac{k}{\lambda}, \qquad \text{Var}(S_k) = \frac{k}{\lambda^2}$$

$k$ 번째 도착까지 걸리는 시간의 기댓값은 도착간격의 기댓값에 $k$ 를 곱한 것일 뿐이다. 이는 직관에 잘 들어맞는다.

## 푸아송분포와의 연결

사건 $\{S_k \leq t\}$($k$ 번째 도착이 시각 $t$ 까지 일어남)는 $\{N(t) \geq k\}$(시각 $t$ 까지 도착이 적어도 $k$ 번 일어남)와 같고, 여기서 $N(t) \sim \text{Po}(\lambda t)$ 이다. 따라서 다음이 성립한다.

$$P(S_k \leq t) = P(N(t) \geq k) = 1 - \sum_{j=0}^{k-1} \frac{(\lambda t)^j}{j!} e^{-\lambda t}$$

이것은 얼랑분포의 닫힌 꼴 누적분포함수를 주는 동시에 깊은 쌍대성을 드러낸다. 곧 **감마/얼랑분포의 누적분포함수**가 **푸아송분포의 꼬리확률**과 같다는 것이다.

## 검사의 역설

!!! warning "도착간격의 역설"
    $t = -\infty$ 에서 $t = \infty$ 까지 이어지는, 비율이 $\lambda$ 인 푸아송 과정을 생각하자. **시각 하나를 고정해서** 고르자(예를 들어 오늘 날짜). 그 고정된 시점을 **품고 있는** 도착간격의 길이를 $\tau$ 라 하자.

    **뜻밖의 결과:**

    - 낱낱의 도착간격 $T_i$ 는 평균이 $1/\lambda$ 인 $\text{Exp}(\lambda)$ 이다
    - 그런데 $\tau \sim \Gamma(2, \lambda)$ 이고 평균은 $2/\lambda$ 이다

    내가 떨어진 구간은 평균적으로 보통의 도착간격보다 **두 배나 길다!**

### 왜 이런 일이 일어나는가

이것은 **검사의 역설**(**길이편향 표집** 또는 **버스 기다리기의 역설**이라고도 한다)의 한 보기이다. 아무 때나 골라 도착하면 다음과 같은 일이 일어난다.

- 짧은 도착간격보다 **긴** 도착간격 안에 떨어질 가능성이 크다
- 어떤 구간 안에 떨어질 확률은 그 구간의 길이에 비례한다
- 그래서 관찰된 구간의 길이가 위쪽으로 치우친다

### 엄밀한 설명

고정된 시점은 $\tau$ 를 두 조각으로 가른다.

- **뒤쪽 재귀시간** $B$: 고정된 시점 직전의 도착으로부터 지난 시간
- **앞쪽 재귀시간** $F$: 고정된 시점에서 다음 도착까지의 시간

푸아송 과정의 무기억성에 따라 다음이 성립한다.

- $F \sim \text{Exp}(\lambda)$ (무기억성: 다음 사건까지의 시간은 언제나 $\text{Exp}(\lambda)$)
- $B \sim \text{Exp}(\lambda)$ (푸아송 과정의 시간 되짚기 성질에 따라)
- $B$ 와 $F$ 는 독립이다

따라서 다음을 얻는다.

$$\tau = B + F \sim \text{Exp}(\lambda) * \text{Exp}(\lambda) = \Gamma(2, \lambda)$$

$$E[\tau] = \frac{2}{\lambda}, \qquad \text{Var}(\tau) = \frac{2}{\lambda^2}$$

### 검사의 역설을 보여 주는 일상의 예

- **버스 기다리기**: 버스가 푸아송 과정에 따라 오고 내가 아무 때나 도착한다면, 내 기다림의 기댓값은 $1/\lambda$, 곧 평균 도착간격을 통째로 기다리는 것이지 그 절반이 아니다
- **학급 크기**: 학생을 무작위로 골라 학급 인원을 물으면 그 평균은 전체 평균 학급 인원보다 크다(큰 학급에 학생이 더 많이 들어 있기 때문이다)
- **가족 크기**: 아이를 무작위로 골라 가족 수를 물으면 그 답은 위쪽으로 치우친다

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
lam = 1.0
n_sim = 100000

# 푸아송 과정을 모의실험하여 고정된 시점을 품는 구간을 찾는다
def simulate_inspection_paradox(lam, fixed_point, n_arrivals=1000):
    """고정된 시점을 품고 있는 도착간격을 모의실험한다."""
    # 도착간격을 많이 만들어 낸다
    interarrivals = np.random.exponential(1/lam, n_arrivals)
    arrival_times = np.cumsum(interarrivals)

    # 고정된 시점을 품는 구간을 찾는다
    idx = np.searchsorted(arrival_times, fixed_point)
    if idx == 0:
        return interarrivals[0]  # 고정된 시점이 첫 도착보다 앞선 경우
    return interarrivals[idx]  # 고정된 시점을 품는 구간의 길이

# 모의실험 실행
fixed_point = 50.0  # 아무렇게나 고른 고정 시각
tau_samples = np.array([
    simulate_inspection_paradox(lam, fixed_point, 200)
    for _ in range(n_sim)
])

# 보통의 도착간격
regular_interarrivals = np.random.exponential(1/lam, n_sim)

# 비교 그림
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

x = np.linspace(0, 8, 200)

# 히스토그램
axes[0].hist(regular_interarrivals, bins=80, density=True, alpha=0.5,
             range=(0, 8), label=f'Regular T_i ~ Exp({lam})', color='blue')
axes[0].hist(tau_samples, bins=80, density=True, alpha=0.5,
             range=(0, 8), label=f'τ (containing fixed point)', color='red')
axes[0].plot(x, stats.expon.pdf(x, scale=1/lam), 'b-', lw=2,
             label='Exp(1) PDF')
axes[0].plot(x, stats.gamma.pdf(x, a=2, scale=1/lam), 'r-', lw=2,
             label='Γ(2,1) PDF')
axes[0].set_title('Inspection Paradox')
axes[0].set_xlabel('Interarrival time')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 검사의 역설을 푸아송 과정 위에 그려 본다
np.random.seed(7)
interarrivals = np.random.exponential(1/lam, 20)
arrivals = np.cumsum(interarrivals)
arrivals = arrivals[arrivals < 8]

fixed_t = 5.0
axes[1].plot(arrivals, np.zeros(len(arrivals)), 'or', markersize=8)
axes[1].axvline(fixed_t, color='black', lw=2, label=f'Fixed point t={fixed_t}')

# 품고 있는 구간 찾기
idx = np.searchsorted(arrivals, fixed_t)
if idx > 0 and idx < len(arrivals):
    left = arrivals[idx-1]
    right = arrivals[idx]
    axes[1].axvline(left, color='red', lw=2, alpha=0.7)
    axes[1].axvline(right, color='red', lw=2, alpha=0.7)
    axes[1].annotate('', xy=(right, -0.3), xytext=(left, -0.3),
                     arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    axes[1].text((left+right)/2, -0.4, f'τ = {right-left:.2f}',
                 ha='center', color='red', fontsize=12)

for a in arrivals:
    axes[1].plot([a, a], [-0.1, 0.1], 'r-', lw=1)

axes[1].set_xlim(0, 8)
axes[1].set_ylim(-0.6, 0.6)
axes[1].set_title('Interarrival Interval Containing Fixed Point')
axes[1].set_xlabel('Time')
axes[1].legend(loc='upper right')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('kth_arrival_paradox.png', dpi=150, bbox_inches='tight')
plt.show()

# 통계값 출력
print("=== Inspection Paradox Statistics ===")
print(f"Regular interarrival: E[T] = {np.mean(regular_interarrivals):.4f} "
      f"(theory {1/lam:.4f})")
print(f"Containing interval:  E[τ] = {np.mean(tau_samples):.4f} "
      f"(theory {2/lam:.4f})")
print(f"Ratio E[τ]/E[T] = {np.mean(tau_samples)/np.mean(regular_interarrivals):.4f} "
      f"(theory 2.0)")
```

## 연습문제

**연습문제 1.**
창구가 하나인 은행에 손님이 시간당 $\lambda = 6$ 의 비율로 푸아송 과정에 따라 온다. 내가 세 번째로 줄을 서 있다. 내가 볼일을 다 마칠 때까지의 전체 대기시간의 분포와 평균, 표준편차를 구하여라.

??? success "연습문제 1 풀이"
    처리가 세 번 끝나기를 기다려야 한다. 처리 시간이 i.i.d. $\text{Exp}(6)$(시간 단위)이라면 전체 기다림은 $S_3 = T_1 + T_2 + T_3 \sim \Gamma(3, 6)$ 이다.

    $E[S_3] = 3/6 = 0.5$ 시간 = 30분

    $\text{SD}(S_3) = \sqrt{3/36} = \sqrt{3}/6 \approx 0.289$ 시간 $\approx 17.3$ 분

---

**연습문제 2.**
버스가 어떤 정류장에 시간당 $\lambda = 4$ 의 비율로 푸아송 과정에 따라 온다. 나는 아무 때나 정류장에 도착한다.

(a) 내가 떨어지는 도착간격의 길이의 기댓값은 얼마인가?

(b) 다음 버스가 올 때까지의 시간의 기댓값은 얼마인가?

(c) (b)의 답이 $1/(2\lambda)$ 가 아니라 $1/\lambda$ 인 까닭을 설명하여라.

??? success "연습문제 2 풀이"
    (a) 검사의 역설에 따라 $\tau \sim \Gamma(2, 4)$ 이므로 $E[\tau] = 2/4 = 0.5$ 시간 = 30분이다. 이는 평균 도착간격 15분의 두 배이다.

    (b) 무기억성에 따라 앞쪽 재귀시간은 $\text{Exp}(4)$ 이므로 기다림의 기댓값은 $1/4$ 시간 = 15분이다.

    (c) "평균적으로 구간의 한가운데에 도착하니 절반만 기다린다"는 순진한 논리는 구간 안에서 균등하게 도착한다고 가정한 것이다. 그러나 나는 긴 구간에 떨어질 가능성이 더 크고, 이 효과가 "한가운데" 효과를 정확히 상쇄한다. 무기억성을 쓰면 답이 곧바로 나온다. 마지막 버스가 언제 왔든 다음 버스까지의 시간은 언제나 $\text{Exp}(\lambda)$ 이다.
