# 고전적인 예(짝맞추기, 생일, 빈 상자, 엘리베이터)

## 예제 1: 짝맞추기 문제 (완전순열)

외투 보관소 직원이 $n$ 명에게 모자 $n$ 개를 무작위로 돌려준다. $X$ 를 자기 모자를 받는 사람의 수라 하자.

$$
X = \sum_{i=1}^n \mathbf{1}_{A_i}
$$

여기서 $A_i$ 는 $i$ 번 사람이 자기 모자를 받는 사건이다.

**평균**: 대칭성에 따라 모든 $i$ 에 대하여 $P(A_i) = \frac{1}{n}$ 이므로 다음을 얻는다.

$$
E[X] = \sum_{i=1}^n \frac{1}{n} = 1
$$

놀랍게도 짝이 맞는 개수의 기댓값은 $n$ 과 관계없이 정확히 1이다.

**분산**: $i \neq j$ 에 대하여 $P(A_i \cap A_j)$ 가 필요하다.

$$
P(A_i \cap A_j) = \frac{(n-2)!}{n!} = \frac{1}{n(n-1)}
$$

$$
\text{Cov}(\mathbf{1}_{A_i}, \mathbf{1}_{A_j}) = \frac{1}{n(n-1)} - \frac{1}{n^2} = \frac{1}{n^2(n-1)}
$$

$$
\text{Var}(X) = n \cdot \frac{1}{n}\left(1 - \frac{1}{n}\right) + 2\binom{n}{2} \cdot \frac{1}{n^2(n-1)} = \frac{n-1}{n} + \frac{1}{n} = 1
$$

그러므로 모든 $n$ 에 대하여 $\text{Var}(X) = 1$ 이고 $\text{SD}(X) = 1$ 이다.

---

## 예제 2: 생일이 같은 짝의 개수

어떤 반에 $n$ 명이 있고 각자 365일 가운데 하루를 서로 독립으로 균등하게 생일로 고른다. $S_n$ 을 생일이 같은 짝의 개수라 하자.

$$
S_n = \sum_{1 \leq i < j \leq n} \mathbf{1}_{A_{ij}}
$$

여기서 $A_{ij}$ 는 $i$ 번 사람과 $j$ 번 사람의 생일이 같은 사건이다.

!!! warning "이항분포가 아니다"
    각각 $p = 1/365$ 인 베르누이 지시확률변수가 $m = \binom{n}{2}$ 개 있지만, 이 지시확률변수들이 서로 독립이 아니므로 $S_n$ 은 $\text{Binomial}(m, p)$ 가 **아니다**.

**평균**:

$$
E[S_n] = \binom{n}{2} \cdot \frac{1}{365}
$$

**분산**: 이 지시확률변수들은 쌍별로 독립이다($i,j$ 의 생일이 같은지 알아도 그와 겹치는 사람이 없는 짝 $k,l$ 의 확률은 달라지지 않는다). 더 정확히 말하면, 겹치는 사람이 없는 두 짝 $(i,j)$ 와 $(k,l)$ 에 대하여 다음이 성립한다.

$$
P(A_{ij} \cap A_{kl}) = P(A_{ij})P(A_{kl}) = \frac{1}{365^2}
$$

따라서 공분산 항이 모두 사라지고 다음을 얻는다.

$$
\text{Var}(S_n) = \binom{n}{2} \cdot \frac{1}{365} \cdot \frac{364}{365}
$$

---

## 예제 3: 빈 상자의 개수

공 $n$ 개와 상자 $M = 365$ 개가 있다. 각 공은 서로 독립으로 균등하게 상자를 하나 고른다. $S_n$ 을 빈 상자의 개수라 하자.

$$
S_n = \sum_{i=1}^{M} \mathbf{1}_{A_i}
$$

여기서 $A_i$ 는 {$i$ 번 상자가 비어 있다} 는 사건이다. 그러면 $P(A_i) = \left(\frac{M-1}{M}\right)^n$ 이다.

**평균**:

$$
E[S_n] = M \left(\frac{M-1}{M}\right)^n
$$

**분산**: 여기서는 지시확률변수들이 독립이 **아니고** 공분산이 0이 아니다.

$$
P(A_i \cap A_j) = \left(\frac{M-2}{M}\right)^n
$$

$$
\text{Cov}(\mathbf{1}_{A_i}, \mathbf{1}_{A_j}) = \left(\frac{M-2}{M}\right)^n - \left(\frac{M-1}{M}\right)^{2n}
$$

$$
\text{Var}(S_n) = M \cdot p(1-p) + 2\binom{M}{2}\left[\left(\frac{M-2}{M}\right)^n - p^2\right]
$$

여기서 $p = \left(\frac{M-1}{M}\right)^n$ 이다.

---

## 예제 4: 멈추는 횟수 (엘리베이터 문제)

지하층 엘리베이터에 $n$ 명이 타고 있다. 각자 서로 독립으로 $M = 365$ 개의 층 가운데 하나를 균등하게 고른다. $X_n$ 을 엘리베이터가 멈추는 총횟수라 하자.

멈추는 횟수는 비어 있지 않은 상자의 개수와 같다.

$$
X_n = M - S_n
$$

여기서 $S_n$ 은 빈 상자의 개수, 곧 아무도 고르지 않은 층의 개수이다.

**평균**:

$$
E[X_n] = M - E[S_n] = M - M\left(\frac{M-1}{M}\right)^n = M\left[1 - \left(\frac{M-1}{M}\right)^n\right]
$$

**분산**:

$$
\text{Var}(X_n) = \text{Var}(M - S_n) = \text{Var}(S_n)
$$

---

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from math import comb

# ============================================================
# 생일이 같은 짝: n 에 따른 평균과 표준편차
# ============================================================
n_people = np.arange(1, 367)
mu_pairs = np.array([comb(n, 2) for n in n_people]) / 365
sd_pairs = np.sqrt(mu_pairs * 364 / 365)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].plot(n_people, mu_pairs)
axes[0].set_xlabel('Number of people in class')
axes[0].set_title('Mean of number of common birthday pairs')
axes[0].grid(True)

axes[1].plot(n_people, sd_pairs)
axes[1].set_xlabel('Number of people in class')
axes[1].set_title('Standard deviation of number of common birthday pairs')
axes[1].grid(True)
plt.tight_layout()
plt.savefig('birthday_pairs.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# 빈 상자: n 에 따른 평균과 표준편차
# ============================================================
M = 365
n_balls = np.arange(1, 2001)
p1 = ((M - 1) / M) ** n_balls
p2 = ((M - 2) / M) ** n_balls
mu_empty = M * p1
var_empty = M * p1 * (1 - p1) + 2 * comb(M, 2) * (p2 - p1**2)
sd_empty = np.sqrt(np.maximum(var_empty, 0))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].plot(n_balls, mu_empty)
axes[0].set_xlabel('Number of balls thrown')
axes[0].set_title('Mean of number of empty bins')
axes[0].grid(True)

axes[1].plot(n_balls, sd_empty)
axes[1].set_xlabel('Number of balls thrown')
axes[1].set_title('Standard deviation of number of empty bins')
axes[1].grid(True)
plt.tight_layout()
plt.savefig('empty_bins.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# 멈추는 횟수: n 에 따른 평균과 표준편차
# ============================================================
mu_stops = M - mu_empty
sd_stops = sd_empty  # Var(M - S) = Var(S)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].plot(n_balls, mu_stops)
axes[0].set_xlabel('Number of people in elevator')
axes[0].set_title('Mean of number of overall stops')
axes[0].grid(True)

axes[1].plot(n_balls, sd_stops)
axes[1].set_xlabel('Number of people in elevator')
axes[1].set_title('Standard deviation of number of overall stops')
axes[1].grid(True)
plt.tight_layout()
plt.savefig('elevator_stops.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.** 어떤 모임에 100명이 있다. 각자의 생일은 서로 독립이며 365일 위에 균등하게 퍼져 있다. 지시확률변수를 써서 생일이 같은 짝의 개수의 기댓값을 구하여라.

??? success "연습문제 1 풀이"
    순서를 따지지 않는 $\binom{100}{2} = 4950$ 개의 짝 $(i, j)$ 각각에 대하여, $i$ 번 사람과 $j$ 번 사람의 생일이 같으면 $I_{ij} = 1$ 이라 하자. 그러면 $E[I_{ij}] = 1/365$ 이다($i$ 번 사람의 생일을 정하고 나면 $j$ 번 사람의 생일이 그와 같을 확률이 $1/365$ 이기 때문이다). $N = \sum_{i < j} I_{ij}$ 라 하자.

    선형성에 따라 다음을 얻는다.

    $$
    E[N] = \binom{100}{2} \cdot \frac{1}{365} = \frac{4950}{365} \approx 13.56
    $$

---

**연습문제 2.** 공 200개를 100개의 상자에 균등하게 무작위로 던져 넣는다. 지시확률변수를 써서 빈 상자 개수의 기댓값과 분산을 구하여라.

??? success "연습문제 2 풀이"
    $k$ 번 상자가 비어 있으면 $I_k = 1$ 이라 하자. $P(I_k = 1) = (99/100)^{200}$ 이므로 다음을 얻는다.

    $$
    E[\text{빈 상자의 수}] = 100 \cdot (99/100)^{200} \approx 100 \cdot 0.1340 \approx 13.40
    $$

    분산을 구하려면 $\text{Var}(\sum I_k) = \sum \text{Var}(I_k) + \sum_{k \neq l} \text{Cov}(I_k, I_l)$ 가 필요하다.

    - $p = (99/100)^{200}$ 일 때 $\text{Var}(I_k) = p(1 - p)$ 이다.
    - $P(I_k = 1, I_l = 1) = (98/100)^{200}$ 이므로 $\text{Cov}(I_k, I_l) = (98/100)^{200} - p^2$ 이다.

    $p = (99/100)^{200} \approx 0.1340$, $q = (98/100)^{200} \approx 0.01758$ 이라 하면 다음을 얻는다.

    $$
    \text{Var}(E) = 100 p(1 - p) + 100 \cdot 99 (q - p^2) \approx 100(0.1160) + 9900(0.01758 - 0.01795) \approx 11.60 - 3.68 \approx 7.92
    $$

    그러므로 빈 상자의 개수는 평균이 $\approx 13.4$, 분산이 $\approx 7.9$ 이다.

---

**연습문제 3.** 20명이 1층에서 엘리베이터를 탄다. 각자 서로 독립으로 10개의 층 가운데 하나를 고른다. 엘리베이터가 멈추는 층수의 기댓값과 분산을 구하여라.

??? success "연습문제 3 풀이"
    $k = 1, \ldots, 10$ 에 대하여 적어도 한 사람이 $k$ 층을 골랐으면 $I_k = 1$ 이라 하자. $P(I_k = 0) = (9/10)^{20}$ 이므로 $P(I_k = 1) = 1 - (9/10)^{20} \approx 0.8784$ 이다.

    $S = \sum_{k=1}^{10} I_k$ 라 하면 $E[S] = 10(1 - (9/10)^{20}) \approx 8.784$ 이다.

    분산은 다음과 같이 구한다.

    $$
    \text{Var}(I_k) = p(1 - p), \quad p = 1 - (9/10)^{20}
    $$

    $k \neq l$ 에 대하여 $P(I_k = 0 \text{ 그리고 } I_l = 0) = (8/10)^{20}$ 이고 다음을 얻는다.

    $$
    P(I_k = 1, I_l = 1) = 1 - 2(9/10)^{20} + (8/10)^{20} \approx 1 - 0.2432 + 0.01153 \approx 0.7684
    $$

    $$
    \text{Cov}(I_k, I_l) = 0.7684 - p^2 \approx 0.7684 - 0.7716 \approx -0.0032
    $$

    모두 더하면 $\text{Var}(S) = 10 p(1 - p) + 10 \cdot 9 \cdot \text{Cov}(I_k, I_l) \approx 10(0.1068) - 90(0.0032) \approx 1.068 - 0.288 \approx 0.78$ 이다.

    그러므로 멈추는 횟수는 평균이 $\approx 8.78$, 분산이 $\approx 0.78$ 이다.
