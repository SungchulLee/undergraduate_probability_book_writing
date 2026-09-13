# 기댓값의 선형성

## 정리의 서술

임의의 확률변수 $X_1, X_2, \ldots, X_n$ (서로 독립일 필요가 없다)과 상수 $a_1, a_2, \ldots, a_n, b$ 에 대하여 다음이 성립한다.

$$
E\left[\sum_{i=1}^n a_i X_i + b\right] = \sum_{i=1}^n a_i E[X_i] + b
$$

가장 간단한 꼴로, 확률변수가 둘일 때는 다음과 같다.

$$
E[aX + bY + c] = aE[X] + bE[Y] + c
$$

!!! note "핵심 통찰"
    기댓값의 선형성은 **확률변수들이 독립인지 종속인지와 상관없이** 성립한다. 바로 이 점 덕분에 대단히 강력한 도구가 된다.

---

## 증명의 얼개 (이산인 경우)

두 확률변수 $X$ 와 $Y$ 에 대하여 다음과 같이 계산한다.

$$
E[X + Y] = \sum_x \sum_y (x + y) \, p(x, y) = \sum_x \sum_y x \, p(x, y) + \sum_x \sum_y y \, p(x, y)
$$

첫째 합은 $\sum_x x \, p_X(x) = E[X]$ 와 같고, 둘째 합은 $\sum_y y \, p_Y(y) = E[Y]$ 와 같다.

---

## 응용

### 예제 1: 주사위 눈의 합의 기댓값

공정한 주사위를 $n$ 개 던진다. $X_i$ 를 $i$ 번째 주사위의 눈이라 하고 $S = X_1 + X_2 + \cdots + X_n$ 이라 하자.

$$
E[S] = \sum_{i=1}^n E[X_i] = n \cdot 3.5
$$

$n = 2$ 이면 $E[S] = 7$ 이다.

### 예제 2: 선형성으로 구하는 이항분포의 평균

$S \sim \text{Binomial}(n, p)$ 일 때 $S = \sum_{i=1}^n X_i$ 로 적자. 여기서 $X_i \sim \text{Bernoulli}(p)$ 는 서로 독립이다. 그러면 다음을 얻는다.

$$
E[S] = \sum_{i=1}^n E[X_i] = np
$$

$E[S] = \sum_{k=0}^n k \binom{n}{k} p^k (1-p)^{n-k}$ 를 곧바로 계산하는 것보다 훨씬 간단하다.

### 예제 3: 음이항분포의 평균

$S \sim \text{NB}(r, p)$ 일 때 $S = \sum_{i=1}^r X_i$ 로 적자. 여기서 $X_i \sim \text{Geo}(p)$ 는 서로 독립이다. 그러면 다음을 얻는다.

$$
E[S] = \sum_{i=1}^r E[X_i] = \frac{r}{p}
$$

### 예제 4: 쿠폰 모으기의 평균

$n$ 가지 쿠폰을 모두 모으는 데 걸리는 시간을 $T_n = \sum_{i=1}^n \tau_i$ 라 하자. 여기서 $\tau_i \sim \text{Geo}\left(\frac{n-(i-1)}{n}\right)$ 이다. 그러면 다음을 얻는다.

$$
E[T_n] = \sum_{i=1}^n E[\tau_i] = \sum_{i=1}^n \frac{n}{n-(i-1)} = n\sum_{k=1}^n \frac{1}{k} = nH_n \sim n \log n
$$

여기서 $H_n = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}$ 은 $n$ 번째 조화수이다.

---

## 종속인 확률변수에서의 선형성

### 예: 생일이 같은 짝

어떤 반에 $n$ 명이 있고 각자 365일 가운데 하루를 균등하게 무작위로 생일로 고른다. $S_n$ 을 생일이 같은 짝의 개수라 하자.

$i$ 번 사람과 $j$ 번 사람의 생일이 같음을 나타내는 지시확률변수를 $\mathbf{1}_{A_{ij}}$ 라 하면 다음과 같다.

$$
S_n = \sum_{1 \leq i < j \leq n} \mathbf{1}_{A_{ij}}
$$

이 지시확률변수들은 **독립이 아니다**($i$ 의 생일이 $j$, $k$ 와 각각 같다면 $j$ 와 $k$ 의 생일도 같을 가능성이 커진다). 그러나 선형성에 따라 다음을 얻는다.

$$
E[S_n] = \sum_{1 \leq i < j \leq n} E[\mathbf{1}_{A_{ij}}] = \binom{n}{2} \cdot \frac{1}{365}
$$

---

## 파이썬 구현

```python
import numpy as np
from math import comb

# 선형성으로 구하는 이항분포의 평균
n, p = 20, 0.3
E_binomial = n * p
print(f"E[Binomial({n},{p})] = {E_binomial}")  # 6.0

# 선형성으로 구하는 음이항분포의 평균
r, p = 5, 0.4
E_negbin = r / p
print(f"E[NB({r},{p})] = {E_negbin}")  # 12.5

# 쿠폰 모으기의 평균
n = 50
harmonic_n = sum(1/k for k in range(1, n+1))
E_coupon = n * harmonic_n
print(f"E[coupon collector, n={n}] = {E_coupon:.2f}")
print(f"n*ln(n) approximation = {n * np.log(n):.2f}")

# 생일이 같은 짝의 개수의 평균
n_people = 30
E_birthday_pairs = comb(n_people, 2) / 365
print(f"E[birthday pairs, {n_people} people] = {E_birthday_pairs:.4f}")

# 몬테카를로: 종속인 확률변수에서도 선형성이 성립함을 확인
np.random.seed(42)
N_sim = 100_000
count = 0
for _ in range(N_sim):
    birthdays = np.random.randint(0, 365, n_people)
    pairs = 0
    for i in range(n_people):
        for j in range(i+1, n_people):
            if birthdays[i] == birthdays[j]:
                pairs += 1
    count += pairs
mc_estimate = count / N_sim
print(f"Monte Carlo E[birthday pairs] = {mc_estimate:.4f}")
print(f"Exact E[birthday pairs] = {E_birthday_pairs:.4f}")
```

## 연습문제

**연습문제 1.** $E[X] = 3$, $E[Y] = -2$ 인 확률변수 $X$ 와 $Y$ 에 대하여 $E[4X - 3Y + 7]$ 을 구하여라.

??? success "연습문제 1 풀이"
    선형성에 따라 다음을 얻는다.

    $$
    E[4X - 3Y + 7] = 4E[X] - 3E[Y] + 7 = 4(3) - 3(-2) + 7 = 12 + 6 + 7 = 25
    $$

---

**연습문제 2.** $X \sim \text{Hypergeometric}(N, K, n)$ 일 때(빨간 공 $K$ 개가 섞인 $N$ 개의 공에서 비복원으로 $n$ 개를 뽑는다) 선형성을 써서 $E[X]$ 를 구하여라.

??? success "연습문제 2 풀이"
    $A_i$ 를 "$i$ 번째로 뽑은 공이 빨간 공이다"라는 사건이라 하고 $X = \sum_{i=1}^n \mathbf{1}_{A_i}$ 로 적자. 대칭성에 따라 모든 $i$ 에 대하여 $P(A_i) = K/N$ 이다. 선형성에 따라 다음을 얻는다.

    $$
    E[X] = \sum_{i=1}^n P(A_i) = n \cdot \frac{K}{N}
    $$

    참고: 비복원추출이므로 지시확률변수들은 독립이 **아니지만** 선형성은 그대로 쓸 수 있다.

---

**연습문제 3.** 50명이 자기 외투를 50개의 고리에 무작위로 건다. $X$ 를 자기 외투를 되찾는 사람의 수라 할 때 $E[X]$ 를 구하여라.

??? success "연습문제 3 풀이"
    $\mathbf{1}_{A_i}$ 를 $i$ 번 사람이 자기 외투를 되찾음을 나타내는 지시확률변수라 하자. 그러면 $P(A_i) = 1/50$ 이고 $X = \sum_{i=1}^{50} \mathbf{1}_{A_i}$ 이다.

    $$
    E[X] = \sum_{i=1}^{50} \frac{1}{50} = 1
    $$

    놀랍게도 고정점의 개수의 기댓값은 $n$ 과 관계없이 언제나 1이다.

---

**연습문제 4.** 공정한 주사위 10개를 던지고 눈의 합을 $S$ 라 하자. $E[X_i] = 3.5$ 와 $E[X_i^2] = 91/6$ 만을 쓰고 선형성을 이용하여 $E[S]$ 와 $E[S^2 - S]$ 를 구하여라.

??? success "연습문제 4 풀이"
    $E[S] = 10 \times 3.5 = 35$ 이다.

    $E[S^2 - S] = E[S^2] - E[S]$ 이므로 $E[S^2]$ 가 필요하다.

    $$
    E[S^2] = E\!\left[\left(\sum_{i=1}^{10} X_i\right)^2\right] = \sum_i E[X_i^2] + 2\sum_{i < j} E[X_i]E[X_j]
    $$

    (교차항에는 독립성을 썼다.) 따라서 $E[S^2] = 10 \cdot \frac{91}{6} + 2\binom{10}{2}(3.5)^2 = \frac{910}{6} + 90 \times 12.25 = 151.667 + 1102.5 = 1254.167$ 이다.

    $$
    E[S^2 - S] = 1254.167 - 35 = 1219.167
    $$

---

**연습문제 5.** 어떤 반에 30명이 있고 생일은 서로 독립이며 365일 위에 균등하게 퍼져 있다. 학생이 둘 이상 몰린 날의 수의 기댓값을 선형성을 써서 구하여라.

??? success "연습문제 5 풀이"
    $D_j$ 를 $j$ 번째 날에 학생이 2명 이상 있다는 사건이라 하고 그 지시확률변수를 $\mathbf{1}_{D_j}$ 라 하자. 생일이 겹치는 날의 총수는 $X = \sum_{j=1}^{365} \mathbf{1}_{D_j}$ 이다.

    $P(D_j) = 1 - P(j \text{ 번째 날의 학생이 0명 또는 1명}) = 1 - \left(\frac{364}{365}\right)^{30} - 30 \cdot \frac{1}{365}\left(\frac{364}{365}\right)^{29}$ 이다.

    수치로 계산하면 $P(D_j) \approx 1 - 0.9209 - 0.0760 = 0.0031$ 이다.

    $$
    E[X] = 365 \times 0.0031 \approx 1.13
    $$
