# 기대이익의 최대화(신문팔이 문제)

## 문제 설정

신문 장수는 수요 $D$ 를 보기 전에 신문을 몇 부 $q$ 를 주문할지 정해야 한다. 신문 한 부의 원가는 $c$ 이고 판매가는 $s > c$ 이다. 팔리지 않은 신문은 잔존가치 $v < c$ 를 갖는다.

- $D \geq q$ 이면 신문 $q$ 부를 모두 팔고 이익은 $q(s - c)$ 이다
- $D < q$ 이면 $D$ 부를 가격 $s$ 에 팔고 남은 $q - D$ 부를 가치 $v$ 로 처분한다

이익은 다음과 같다.

$$
\Pi(q) = s \min(D, q) + v \max(q - D, 0) - cq
$$

---

## 기대이익

$$
E[\Pi(q)] = s \, E[\min(D, q)] + v \, E[\max(q - D, 0)] - cq
$$

### 최적 주문량

최적의 $q^*$ 는 **임계비** 조건을 만족한다.

$$
P(D \leq q^*) = \frac{s - c}{s - v}
$$

$\frac{s-c}{s-v}$ 를 **임계비** 또는 **서비스 수준**이라 한다. 너무 많이 주문해서 드는 비용(초과 비용 $c - v$)과 너무 적게 주문해서 드는 비용(부족 비용 $s - c$)의 균형을 맞춘 값이다.

---

## 유도

기대이익은 다음과 같이 쓸 수 있다.

$$
E[\Pi(q)] = (s - c)E[D] - (s - c)E[\max(D - q, 0)] - (c - v)E[\max(q - D, 0)]
$$

$q$ 에 대하여 미분하고 0으로 놓으면 다음을 얻는다.

$$
\frac{d}{dq}E[\Pi(q)] = (s - c)P(D > q) - (c - v)P(D \leq q) = 0
$$

이를 풀면 $P(D \leq q^*) = \frac{s - c}{s - v}$ 이다.

---

## 예

수요가 $D \sim N(100, 20^2)$ 이고 판매가 $s = 10$, 원가 $c = 6$, 잔존가치 $v = 2$ 라 하자.

임계비: $\frac{s - c}{s - v} = \frac{10 - 6}{10 - 2} = 0.5$

정규분포는 대칭이므로 $P(D \leq q^*) = 0.5$ 에서 $q^* = 100$ 이다.

임계비가 $0.75$ 였다면 $q^* = \mu + \sigma \mathcal{N}^{-1}(0.75) = 100 + 20 \times 0.6745 \approx 113.5$ 이다.

---

## 파이썬 구현

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 모수
mu_d, sigma_d = 100, 20
s, c, v = 10, 6, 2

# 임계비와 최적 주문량
cr = (s - c) / (s - v)
q_star = stats.norm.ppf(cr, loc=mu_d, scale=sigma_d)
print(f"Critical ratio = {cr:.4f}")
print(f"Optimal order quantity q* = {q_star:.1f}")

# 몬테카를로로 구하는 기대이익
np.random.seed(42)
N = 100_000
D = np.random.normal(mu_d, sigma_d, N)

def mc_expected_profit(q, D, s, c, v):
    sales = np.minimum(D, q)
    salvage = np.maximum(q - D, 0)
    profit = s * sales + v * salvage - c * q
    return np.mean(profit)

q_range = np.arange(50, 151)
profits = [mc_expected_profit(q, D, s, c, v) for q in q_range]

plt.figure(figsize=(10, 6))
plt.plot(q_range, profits, 'b-', linewidth=2)
plt.axvline(x=q_star, color='r', linestyle='--', label=f'q* = {q_star:.1f}')
plt.xlabel('Order Quantity q')
plt.ylabel('Expected Profit E[Π(q)]')
plt.title('Newsboy Problem: Expected Profit vs Order Quantity')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('newsboy_profit.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.** 어떤 제빵사가 한 덩이에 원가 \$2 가 들고 \$5 에 파는 빵을 만든다. 팔리지 않은 빵은 기부한다(잔존가치 \$0). 하루 수요는 $D \sim \text{Poisson}(20)$ 이다. 임계비를 구하고 빵을 몇 덩이 구울지 최적값을 정하여라.

??? success "연습문제 1 풀이"
    $s = 5$, $c = 2$, $v = 0$ 이다. 임계비는 다음과 같다.

    $$
    \frac{s - c}{s - v} = \frac{3}{5} = 0.6
    $$

    $D \sim \text{Poisson}(20)$ 에 대하여 $P(D \leq q^*) \geq 0.6$ 이어야 한다. 푸아송 누적분포함수를 계산하면 $P(D \leq 20) \approx 0.559$ 이고 $P(D \leq 21) \approx 0.644$ 이다. 그러므로 $q^* = 21$ 이다.

---

**연습문제 2.** 이익폭 $(s - c)$ 이 초과 비용 $(c - v)$ 에 견주어 커질수록 임계비가 1에 가까워짐을 보여라. 이것은 신문 장수의 주문 전략에 대하여 무엇을 뜻하는가?

??? success "연습문제 2 풀이"
    임계비는 $\frac{s - c}{s - v} = 1 - \frac{c - v}{s - v}$ 이다. $c$ 와 $v$ 를 고정한 채 $s \to \infty$ 로 보내면 이 비는 1에 가까워진다. 곧 $P(D \leq q^*) \to 1$ 이므로 $q^* \to \infty$ 이다. 직관적으로 보면, 한 부를 팔아 얻는 이익이 팔리지 않은 신문에서 보는 손해보다 훨씬 클 때는 팔 기회를 놓치지 않도록 넉넉하게 주문해야 한다는 뜻이다.

---

**연습문제 3.** 수요가 $D \sim N(50, 10^2)$ 이다. 판매가는 \$8, 원가는 \$5, 잔존가치는 \$1 이다. $q^*$ 와 기대이익 $E[\Pi(q^*)]$ 를 구하여라.

??? success "연습문제 3 풀이"
    임계비는 $\frac{8-5}{8-1} = \frac{3}{7} \approx 0.4286$ 이다.

    $q^* = 50 + 10 \cdot \mathcal{N}^{-1}(0.4286) = 50 + 10 \times (-0.1800) \approx 48.2$ 이다.

    반올림하면 $q^* = 48$ 이다. 기대이익을 구하려면 정규손실함수를 써서 $E[\min(D, 48)]$ 과 $E[\max(48 - D, 0)]$ 을 계산해야 한다. 어림하면 다음과 같다.

    $$
    E[\Pi(48)] \approx 8 \cdot E[\min(D,48)] + 1 \cdot E[\max(48-D,0)] - 5 \cdot 48 \approx \$109
    $$

---

**연습문제 4.** 수요분포가 연속일 때, $c$ 와 $v$ 를 고정한 채 판매가 $s$ 가 커지면 최적 주문량 $q^*$ 가 커짐을 증명하여라.

??? success "연습문제 4 풀이"
    임계비는 $r = \frac{s-c}{s-v}$ 이다. $s$ 에 대하여 미분하면 다음과 같다.

    $$
    \frac{dr}{ds} = \frac{(s-v) - (s-c)}{(s-v)^2} = \frac{c-v}{(s-v)^2} > 0
    $$

    $c > v$ 이므로 임계비는 $s$ 에 대하여 증가한다. 누적분포함수 $F$ 가 순증가하는 연속 수요분포에서는 $q^* = F^{-1}(r)$ 이 $r$ 에 대하여 순증가한다. 그러므로 $q^*$ 는 $s$ 에 대하여 증가한다. $\square$

---

**연습문제 5.** 어떤 장수가 우산을 판다. 원가는 \$3, 판매가는 \$10 이고 잔존가치는 없다. 수요는 $\{0, 1, 2, \ldots, 10\}$ 위의 이산균등분포를 따른다. 최적 주문량을 구하여라.

??? success "연습문제 5 풀이"
    $s = 10$, $c = 3$, $v = 0$ 이다. 임계비는 $\frac{10-3}{10-0} = 0.7$ 이다.

    $D \sim \text{Uniform}\{0, 1, \ldots, 10\}$ 에 대하여 $P(D \leq k) = (k+1)/11$ 이다.

    $(q^*+1)/11 \geq 0.7$, 곧 $q^* \geq 6.7$ 이어야 한다. 그러므로 $q^* = 7$ 이고 이때 $P(D \leq 7) = 8/11 \approx 0.727$ 이다.
