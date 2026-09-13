# 기댓값의 꼬리합 공식

## 정리의 서술

### 음이 아닌 정숫값을 갖는 확률변수

$X$ 가 음이 아닌 정숫값을 갖는 확률변수이면 다음이 성립한다.

$$
E[X] = \sum_{k=1}^{\infty} P(X \geq k) = \sum_{k=0}^{\infty} P(X > k)
$$

### 음이 아닌 연속확률변수

$X$ 가 음이 아닌 연속확률변수이면 다음이 성립한다.

$$
E[X] = \int_0^{\infty} P(X > t) \, dt = \int_0^{\infty} [1 - F_X(t)] \, dt
$$

---

## 증명 (이산인 경우)

$$
\sum_{k=1}^{\infty} P(X \geq k) = \sum_{k=1}^{\infty} \sum_{j=k}^{\infty} P(X = j) = \sum_{j=1}^{\infty} \sum_{k=1}^{j} P(X = j) = \sum_{j=1}^{\infty} j \cdot P(X = j) = E[X]
$$

핵심은 합의 순서를 바꾸는 데 있다. 각 항 $P(X = j)$ 가 정확히 $j$ 번 나타나기 때문이다.

---

## 증명 (연속인 경우)

$$
\int_0^{\infty} P(X > t) \, dt = \int_0^{\infty} \int_t^{\infty} f(x) \, dx \, dt = \int_0^{\infty} \int_0^{x} dt \, f(x) \, dx = \int_0^{\infty} x \, f(x) \, dx = E[X]
$$

---

## 예제

### 예제 1: 기하분포

$X \sim \text{Geo}(p)$ 이면(첫 성공까지의 시행 횟수) 다음이 성립한다.

$$
P(X \geq k) = (1-p)^{k-1}
$$

꼬리합 공식에 따라 다음을 얻는다.

$$
E[X] = \sum_{k=1}^{\infty} (1-p)^{k-1} = \frac{1}{1-(1-p)} = \frac{1}{p}
$$

### 예제 2: 지수분포

$X \sim \text{Exp}(\lambda)$ 이면 $P(X > t) = e^{-\lambda t}$ 이다. 꼬리합 공식에 따라 다음을 얻는다.

$$
E[X] = \int_0^{\infty} e^{-\lambda t} \, dt = \frac{1}{\lambda}
$$

---

## 일반적인 꼬리합 공식

임의의 확률변수 $X$ 에 대하여(음이 아닐 필요가 없다) 다음이 성립한다.

$$
E[X] = \int_0^{\infty} P(X > t) \, dt - \int_0^{\infty} P(X < -t) \, dt
$$

이것은 $X$ 를 양의 부분과 음의 부분으로 쪼갠 것이다. 곧 $X^+ = \max(X, 0)$, $X^- = \max(-X, 0)$ 으로 두면 $X = X^+ - X^-$ 이다.

---

## 파이썬 구현

```python
import numpy as np

# Geometric(p)의 꼬리합
p = 0.3
# 정확한 값
E_geo_exact = 1 / p
# 꼬리합으로 계산 (유한 항까지 자름)
E_geo_tail = sum((1 - p)**(k - 1) for k in range(1, 1000))
print(f"E[Geo({p})] exact = {E_geo_exact:.4f}")
print(f"E[Geo({p})] tail sum = {E_geo_tail:.4f}")

# Exponential(lambda)의 꼬리합
lam = 2.0
from scipy import integrate
E_exp_exact = 1 / lam
E_exp_tail, _ = integrate.quad(lambda t: np.exp(-lam * t), 0, np.inf)
print(f"E[Exp({lam})] exact = {E_exp_exact:.4f}")
print(f"E[Exp({lam})] tail sum = {E_exp_tail:.4f}")

# 몬테카를로로 확인
np.random.seed(42)
N = 1_000_000
geo_samples = np.random.geometric(p, N)
exp_samples = np.random.exponential(1/lam, N)
print(f"MC E[Geo({p})] = {np.mean(geo_samples):.4f}")
print(f"MC E[Exp({lam})] = {np.mean(exp_samples):.4f}")
```

## 연습문제

**연습문제 1.** 꼬리합 공식을 써서 모수가 $p$ 인 기하분포를 따르는 확률변수의 기댓값을 구하여라.

??? success "연습문제 1 풀이"
    받침이 $\{1, 2, 3, \ldots\}$ 인 $X \sim \text{Geometric}(p)$ 에 대하여 $k \geq 1$ 일 때 $P(X \geq k) = (1 - p)^{k - 1}$ 이다. 꼬리합 공식에 따라 다음을 얻는다.

    $$
    E[X] = \sum_{k=1}^{\infty} P(X \geq k) = \sum_{k=1}^{\infty} (1 - p)^{k - 1} = \frac{1}{1 - (1 - p)} = \frac{1}{p}
    $$

---

**연습문제 2.** $X$ 의 확률질량함수가 $k = 1, 2, 3, \ldots$ 에 대하여 $P(X = k) = 1/2^k$ 이라 하자. 꼬리합 공식을 써서 $E[X]$ 를 구하여라.

??? success "연습문제 2 풀이"
    먼저 $P(X \geq k) = \sum_{j=k}^{\infty} 1/2^j = (1/2^k)/(1 - 1/2) = 1/2^{k-1}$ 이다. 꼬리합 공식에 따라 다음을 얻는다.

    $$
    E[X] = \sum_{k=1}^{\infty} P(X \geq k) = \sum_{k=1}^{\infty} \frac{1}{2^{k-1}} = \frac{1}{1 - 1/2} = 2
    $$

---

**연습문제 3.** 파레토분포의 확률밀도함수는 $\alpha > 1$ 일 때 $x \geq 1$ 에서 $f(x) = \alpha / x^{\alpha+1}$ 이다. 연속형 꼬리합 공식을 써서 $E[X]$ 를 구하여라.

??? success "연습문제 3 풀이"
    생존함수는 $t \geq 1$ 에서 $P(X > t) = t^{-\alpha}$ 이고 $0 \leq t < 1$ 에서 $P(X > t) = 1$ 이다. 꼬리합 공식에 따라 다음을 얻는다.

    $$
    E[X] = \int_0^{\infty} P(X > t)\, dt = \int_0^1 1\, dt + \int_1^{\infty} t^{-\alpha}\, dt = 1 + \frac{t^{-\alpha+1}}{-\alpha+1}\bigg|_1^{\infty} = 1 + \frac{1}{\alpha - 1} = \frac{\alpha}{\alpha - 1}
    $$

    이 적분이 수렴하는 것은 바로 $\alpha > 1$ 이기 때문이다.

---

**연습문제 4.** 연속형 꼬리합 공식을 증명하여라. 곧 $X \geq 0$ 이 확률밀도함수 $f$ 와 누적분포함수 $F$ 를 가질 때 $E[X] = \int_0^{\infty} [1 - F(t)]\, dt$ 임을 보여라.

??? success "연습문제 4 풀이"
    우변에서 시작하자.

    $$
    \int_0^{\infty} [1 - F(t)]\, dt = \int_0^{\infty} P(X > t)\, dt = \int_0^{\infty}\!\int_t^{\infty} f(x)\, dx\, dt
    $$

    피적분함수 $f(x)$ 가 음이 아니므로 푸비니 정리에 따라 적분의 순서를 바꿀 수 있다. 적분 영역은 $\{(t, x) : 0 \leq t \leq x\}$ 이므로 다음을 얻는다.

    $$
    \int_0^{\infty}\!\int_0^{x} dt\, f(x)\, dx = \int_0^{\infty} x\, f(x)\, dx = E[X]
    $$

    $\square$

---

**연습문제 5.** 누적분포함수가 $F$ 인 음이 아닌 확률변수 $X$ 에 대하여 다음이 성립함을 보여라.

$$
E[X^2] = 2\int_0^{\infty} t\,[1 - F(t)]\, dt
$$

??? success "연습문제 5 풀이"
    $Y = X^2$ 에 연속형 꼬리합 공식을 적용하면 다음과 같다.

    $$
    E[X^2] = E[Y] = \int_0^{\infty} P(Y > s)\, ds = \int_0^{\infty} P(X > \sqrt{s})\, ds
    $$

    $s = t^2$, $ds = 2t\, dt$ 로 치환하면 다음을 얻는다.

    $$
    = \int_0^{\infty} P(X > t)\cdot 2t\, dt = 2\int_0^{\infty} t\,[1 - F(t)]\, dt
    $$

    $\square$
