# 정규분포의 적률생성함수

## N(μ, σ²)의 적률생성함수

$$M_{N(\mu, \sigma^2)}(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2}$$

### 유도

$$M_X(t) = \int_{-\infty}^{\infty} e^{tx} \cdot \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \, dx$$

지수 부분에서 완전제곱을 만든다. 피적분함수의 지수는 다음과 같다.

$$tx - \frac{(x - \mu)^2}{2\sigma^2} = -\frac{1}{2\sigma^2}\left[(x - \mu)^2 - 2\sigma^2 tx\right]$$

$$= -\frac{1}{2\sigma^2}\left[x^2 - 2(\mu + \sigma^2 t)x + \mu^2\right]$$

$$= -\frac{(x - (\mu + \sigma^2 t))^2}{2\sigma^2} + \mu t + \frac{1}{2}\sigma^2 t^2$$

그러므로 다음을 얻는다.

$$M_X(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2} \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - (\mu + \sigma^2 t))^2}{2\sigma^2}} \, dx = e^{\mu t + \frac{1}{2}\sigma^2 t^2}$$

여기서 적분은 $N(\mu + \sigma^2 t, \sigma^2)$ 확률밀도함수의 전체 질량이므로 $1$ 이기 때문이다.

### 표준정규분포인 경우

$Z \sim N(0, 1)$ 에 대해서는 다음과 같다.

$$M_Z(t) = e^{t^2/2}$$

## 적률생성함수로 보는 정규분포의 성질

### 성질 1: 일차변환

$X \sim N(\mu, \sigma^2)$ 이면 $aX + b \sim N(a\mu + b, \, a^2\sigma^2)$ 이다.

**적률생성함수를 쓴 증명:**

$$M_{aX+b}(t) = E[e^{t(aX+b)}] = e^{bt} E[e^{(at)X}] = e^{bt} M_X(at)$$

$$= e^{bt} \cdot e^{\mu(at) + \frac{1}{2}\sigma^2(at)^2} = e^{(a\mu + b)t + \frac{1}{2}a^2\sigma^2 t^2} = M_{N(a\mu+b, \, a^2\sigma^2)}(t)$$

### 성질 2: 독립인 정규확률변수의 합

$X \sim N(\mu_1, \sigma_1^2)$ 와 $Y \sim N(\mu_2, \sigma_2^2)$ 가 **독립**이면 다음이 성립한다.

$$X + Y \sim N(\mu_1 + \mu_2, \, \sigma_1^2 + \sigma_2^2)$$

**적률생성함수를 쓴 증명:**

$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = e^{\mu_1 t + \frac{1}{2}\sigma_1^2 t^2} \cdot e^{\mu_2 t + \frac{1}{2}\sigma_2^2 t^2}$$

$$= e^{(\mu_1 + \mu_2)t + \frac{1}{2}(\sigma_1^2 + \sigma_2^2)t^2} = M_{N(\mu_1 + \mu_2, \, \sigma_1^2 + \sigma_2^2)}(t)$$

## 파이썬 구현

```python
import numpy as np
from scipy import stats

# 확인: X ~ N(3, 4), Y ~ N(-1, 9)가 독립일 때
# X + Y는 N(2, 13)이어야 한다
np.random.seed(42)
n = 100000
X = np.random.normal(3, 2, n)     # N(3, 4)
Y = np.random.normal(-1, 3, n)    # N(-1, 9)
Z = X + Y

print("X + Y: simulated vs theoretical N(2, 13)")
print(f"  Mean: {Z.mean():.4f} vs 2.0000")
print(f"  Var:  {Z.var():.4f} vs 13.0000")

# 확인: 2X + 1은 N(7, 16)이어야 한다
W = 2 * X + 1
print(f"\n2X + 1: simulated vs theoretical N(7, 16)")
print(f"  Mean: {W.mean():.4f} vs 7.0000")
print(f"  Var:  {W.var():.4f} vs 16.0000")
```

## 연습문제

**연습문제 1.** 적률생성함수를 써서 $Z \sim N(0,1)$ 에 대한 $E[Z^4]$ 를 구하여라.

??? success "연습문제 1 풀이"
    $M_Z(t) = e^{t^2/2}$ 이다. $M^{(4)}(0)$ 이 필요하다.

    $M'(t) = te^{t^2/2}$, $M''(t) = (1 + t^2)e^{t^2/2}$, $M'''(t) = (3t + t^3)e^{t^2/2}$, $M^{(4)}(t) = (3 + 6t^2 + t^4)e^{t^2/2}$ 이다.

    $$
    E[Z^4] = M^{(4)}(0) = 3
    $$

---

**연습문제 2.** $X \sim N(5, 9)$ 라 하자. 적률생성함수를 써서 $E[e^{2X}]$ 를 구하여라.

??? success "연습문제 2 풀이"
    $E[e^{2X}] = M_X(2) = e^{5 \cdot 2 + \frac{1}{2} \cdot 9 \cdot 4} = e^{10 + 18} = e^{28}$ 이다.

---

**연습문제 3.** $X_1, \ldots, X_n$ 이 독립이고 $X_i \sim N(\mu_i, \sigma_i^2)$ 이면 $\sum_{i=1}^n X_i \sim N\!\left(\sum \mu_i, \sum \sigma_i^2\right)$ 임을 증명하여라.

??? success "연습문제 3 풀이"
    $$
    M_{\sum X_i}(t) = \prod_{i=1}^n M_{X_i}(t) = \prod_{i=1}^n e^{\mu_i t + \frac{1}{2}\sigma_i^2 t^2} = e^{(\sum \mu_i)t + \frac{1}{2}(\sum \sigma_i^2)t^2}
    $$

    이것은 $N(\sum \mu_i, \sum \sigma_i^2)$ 의 적률생성함수이다. 유일성에 따라 $\sum X_i \sim N(\sum \mu_i, \sum \sigma_i^2)$ 이다. $\square$

---

**연습문제 4.** $X \sim N(\mu, \sigma^2)$ 이라 하자. 적률생성함수를 써서 $Z = (X - \mu)/\sigma \sim N(0, 1)$ 임을 보여라.

??? success "연습문제 4 풀이"
    $M_Z(t) = E[e^{t(X-\mu)/\sigma}] = e^{-\mu t/\sigma} M_X(t/\sigma)$ 이다.

    $$
    = e^{-\mu t/\sigma} \cdot e^{\mu(t/\sigma) + \frac{1}{2}\sigma^2(t/\sigma)^2} = e^{t^2/2} = M_{N(0,1)}(t)
    $$

    유일성에 따라 $Z \sim N(0,1)$ 이다. $\square$

---

**연습문제 5.** 정규분포의 적률생성함수는 모든 $t \in \mathbb{R}$ 에서 존재한다. 적률생성함수의 수렴반지름이 유한한 분포들과 견주어 이것이 왜 뜻깊은지 설명하여라.

??? success "연습문제 5 풀이"
    적률생성함수가 모든 $t$ 에서 존재하는 분포는 (적률생성함수의 유일성 정리에 따라) 그 적률만으로 유일하게 결정됨이 보장된다. 게다가 모든 적률이 존재하며 적률생성함수를 미분하여 계산할 수 있다. 기하분포나 지수분포처럼 적률생성함수가 제한된 구간에서만 수렴하는 분포에서는 모든 $t$ 값에 대해 적률생성함수 기법을 적용할 수 없다. 정규분포가 어디서나 수렴한다는 것은 그 적률의 수열이 카를레만 조건을 만족한다는 뜻이기도 하며, 이는 적률만으로 분포가 결정됨을 보장한다.
