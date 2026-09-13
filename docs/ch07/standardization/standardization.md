# 표준화와 역표준화

## 표준화

$X$ 의 평균이 $\mu$ 이고 표준편차가 $\sigma$ 일 때, $X$ 를 **표준화**한 것은 다음과 같다.

$$Z = \frac{X - \mu}{\sigma}$$

이 변환을 거치면 다음이 성립한다.

- $E[Z] = 0$
- $\text{SD}(Z) = 1$

$X$ 가 **정규분포**를 따르면 $Z \sim N(0, 1)$ 이다.

### 왜 표준화하는가

표준화는 어떤 확률변수든 공통의 눈금 위로 옮겨 놓아 서로 다른 분포끼리 견줄 수 있게 해 준다. 특히 정규분포에서는 모든 $N(\mu, \sigma^2)$ 문제를 표준정규분포 $N(0,1)$ 표를 찾아보는 일로 바꾸어 준다.

## 역표준화

$Z$ 의 평균이 $0$ 이고 표준편차가 $1$ 이면 다음 확률변수는

$$X = \mu + \sigma Z$$

평균이 $\mu$ 이고 표준편차가 $\sigma$ 이다.

$Z \sim N(0, 1)$ 이면 $X \sim N(\mu, \sigma^2)$ 이다.

## 정리하며

| 방향 | 공식 | 결과 |
|-----------|---------|--------|
| 표준화 | $Z = \frac{X - \mu}{\sigma}$ | 평균 $0$, 표준편차 $1$ |
| 역표준화 | $X = \mu + \sigma Z$ | 평균 $\mu$, 표준편차 $\sigma$ |

## 분위수와의 관계

$N(\mu, \sigma^2)$ 의 $\alpha$-분위수 $q_\alpha$ 는 $N(0,1)$ 의 $\alpha$-분위수 $z_\alpha$ 로 다음과 같이 나타낼 수 있다.

$$q_\alpha = \mu + \sigma \cdot z_\alpha$$

이는 분위수에 역표준화를 적용한 것에 지나지 않는다.

## 파이썬 구현

```python
import numpy as np
from scipy import stats

# 표준화의 예
mu, sigma = 70, 10
x = 85

z = (x - mu) / sigma
print(f"X = {x} with μ={mu}, σ={sigma}")
print(f"Standardized: Z = {z}")
print(f"P(X ≤ {x}) = P(Z ≤ {z}) = {stats.norm.cdf(z):.4f}")

# 역표준화: P(X ≤ x) = 0.95 가 되는 x 찾기
z_95 = stats.norm.ppf(0.95)
x_95 = mu + sigma * z_95
print(f"\n95th percentile of N({mu},{sigma}²):")
print(f"z_0.95 = {z_95:.4f}")
print(f"q_0.95 = {mu} + {sigma} × {z_95:.4f} = {x_95:.4f}")
```

**실행 결과:**
```
X = 85 with μ=70, σ=10
Standardized: Z = 1.5
P(X ≤ 85) = P(Z ≤ 1.5) = 0.9332

95th percentile of N(70,100):
z_0.95 = 1.6449
q_0.95 = 70 + 10 × 1.6449 = 86.4485
```

## 연습문제

**연습문제 1.** 시험 점수가 $N(72, 8^2)$ 을 따른다. 어떤 학생이 88점을 받았다. 이 학생의 $z$-점수와 백분위를 구하여라.

??? success "연습문제 1 풀이"
    $$
    z = \frac{88 - 72}{8} = 2.0
    $$

    $P(Z \leq 2.0) = \mathcal{N}(2.0) \approx 0.9772$ 이다. 이 학생은 **97.7 백분위**에 있다.

---

**연습문제 2.** 성인 남성의 키가 $N(175, 7^2)$ cm 를 따른다. 10 백분위에 해당하는 키는 얼마인가?

??? success "연습문제 2 풀이"
    $z_{0.10} = \mathcal{N}^{-1}(0.10) \approx -1.2816$ 이다.

    $$
    q_{0.10} = 175 + 7 \times (-1.2816) = 175 - 8.97 = 166.03 \text{ cm}
    $$

---

**연습문제 3.** $X$ 의 평균이 $\mu$, 표준편차가 $\sigma$ 일 때 $Z = (X - \mu)/\sigma$ 가 $E[Z] = 0$ 과 $\text{Var}(Z) = 1$ 을 만족함을 증명하여라.

??? success "연습문제 3 풀이"
    $$
    E[Z] = E\!\left[\frac{X - \mu}{\sigma}\right] = \frac{E[X] - \mu}{\sigma} = \frac{\mu - \mu}{\sigma} = 0
    $$

    $$
    \text{Var}(Z) = \text{Var}\!\left(\frac{X - \mu}{\sigma}\right) = \frac{1}{\sigma^2}\text{Var}(X - \mu) = \frac{\sigma^2}{\sigma^2} = 1
    $$

    $\square$

---

**연습문제 4.** $Z \sim N(0, 1)$ 일 때 $P(-c \leq Z \leq c) = 0.90$ 이 되는 $c$ 를 구하여라.

??? success "연습문제 4 풀이"
    $P(-c \leq Z \leq c) = 2\mathcal{N}(c) - 1 = 0.90$ 에서 $\mathcal{N}(c) = 0.95$ 를 얻는다.

    $$
    c = \mathcal{N}^{-1}(0.95) \approx 1.6449
    $$

---

**연습문제 5.** SAT 수학 점수는 $N(500, 100^2)$ 을, ACT 수학 점수는 $N(21, 5^2)$ 을 따른다. 어떤 학생이 SAT에서 650점, ACT에서 28점을 받았다. 이 학생은 어느 시험에서 상대적으로 더 잘한 것인가?

??? success "연습문제 5 풀이"
    SAT의 $z$-점수는 $z_{\text{SAT}} = (650 - 500)/100 = 1.5$ 이다.

    ACT의 $z$-점수는 $z_{\text{ACT}} = (28 - 21)/5 = 1.4$ 이다.

    $1.5 > 1.4$ 이므로 이 학생은 **SAT** 에서 상대적으로 더 잘했다(백분위가 93.3% 대 91.9% 로 더 높다).
