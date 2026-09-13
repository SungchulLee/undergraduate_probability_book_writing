# 기하분포와 음이항분포의 적률생성함수

## Geometric(p)의 적률생성함수

$X \sim \text{Geo}(p)$ 가 첫 성공까지의 시행 횟수를 센다고 하자. 곧 $k = 1, 2, 3, \ldots$ 에 대해 $P(X = k) = (1-p)^{k-1}p$ 이다.

$$M_X(t) = E[e^{tX}] = \sum_{k=1}^{\infty} e^{tk}(1-p)^{k-1}p = pe^t \sum_{k=0}^{\infty} [(1-p)e^t]^k$$

등비급수는 $(1-p)e^t < 1$ 일 때, 곧 $t < -\ln(1-p)$ 일 때 수렴한다.

$$M_X(t) = \frac{pe^t}{1 - (1-p)e^t}$$

$$\boxed{M_{\text{Geo}(p)}(t) = \frac{pe^t}{1 - (1-p)e^t}, \quad t < -\ln(1-p)}$$

### 적률 유도하기

$q = 1 - p$ 라 하자. $M(t) = pe^t(1 - qe^t)^{-1}$ 로 적고 몫의 미분법으로 미분하면 다음과 같다.

$$M'(t) = \frac{pe^t(1 - qe^t) + pe^t \cdot qe^t}{(1 - qe^t)^2} = \frac{pe^t}{(1 - qe^t)^2}$$

$$E[X] = M'(0) = \frac{p}{(1 - q)^2} = \frac{p}{p^2} = \frac{1}{p}$$

2차 도함수는 다음과 같다.

$$M''(t) = \frac{pe^t(1 - qe^t)^2 + 2pe^t \cdot qe^t(1 - qe^t)}{(1 - qe^t)^4} = \frac{pe^t(1 + qe^t)}{(1 - qe^t)^3}$$

$$E[X^2] = M''(0) = \frac{p(1 + q)}{p^3} = \frac{1 + q}{p^2} = \frac{2 - p}{p^2}$$

$$\text{Var}(X) = \frac{2 - p}{p^2} - \frac{1}{p^2} = \frac{1 - p}{p^2} = \frac{q}{p^2}$$

## Negative Binomial(r, p)의 적률생성함수

음이항분포 $X \sim \text{NB}(r, p)$ 는 $r$ 번째 성공까지의 시행 횟수를 센다. 이는 독립인 기하확률변수 $r$ 개의 합으로 적을 수 있다.

$$X = X_1 + X_2 + \cdots + X_r, \quad X_i \stackrel{\text{iid}}{\sim} \text{Geo}(p)$$

독립성에 따라 합의 적률생성함수는 각 적률생성함수의 곱이다.

$$M_X(t) = \prod_{i=1}^r M_{X_i}(t) = \left[\frac{pe^t}{1 - (1-p)e^t}\right]^r$$

$$\boxed{M_{\text{NB}(r,p)}(t) = \left[\frac{pe^t}{1 - (1-p)e^t}\right]^r, \quad t < -\ln(1-p)}$$

### 기하분포를 거쳐 적률 유도하기

$X_i$ 가 i.i.d. $\text{Geo}(p)$ 인 $X = \sum_{i=1}^r X_i$ 이므로 다음을 얻는다.

$$E[X] = r \cdot E[X_1] = \frac{r}{p}$$

$$\text{Var}(X) = r \cdot \text{Var}(X_1) = \frac{r(1-p)}{p^2}$$

## 파이썬으로 확인하기

```python
import numpy as np
from scipy.misc import derivative

def mgf_geo(t, p=0.3):
    q = 1 - p
    return p * np.exp(t) / (1 - q * np.exp(t))

def mgf_nb(t, r=5, p=0.3):
    return mgf_geo(t, p)**r

# Geo(0.3): E[X] = 10/3, Var(X) = 70/9
p = 0.3
EX = derivative(mgf_geo, 0, n=1, dx=1e-6)
EX2 = derivative(mgf_geo, 0, n=2, dx=1e-6)
print(f"Geo({p}):")
print(f"  E[X]   = {EX:.4f}  (exact: {1/p:.4f})")
print(f"  Var(X) = {EX2 - EX**2:.4f}  (exact: {(1-p)/p**2:.4f})")

# NB(5, 0.3): E[X] = 50/3, Var(X) = 350/9
r = 5
EX = derivative(mgf_nb, 0, n=1, dx=1e-6)
EX2 = derivative(mgf_nb, 0, n=2, dx=1e-6)
print(f"\nNB({r}, {p}):")
print(f"  E[X]   = {EX:.4f}  (exact: {r/p:.4f})")
print(f"  Var(X) = {EX2 - EX**2:.4f}  (exact: {r*(1-p)/p**2:.4f})")
```

## 연습문제

**연습문제 1.** $\text{Geo}(0.5)$ 의 적률생성함수가 수렴하는 정의역을 구하고 $M(0.5)$ 의 값을 계산하여라.

??? success "연습문제 1 풀이"
    정의역은 $t < -\ln(1 - 0.5) = -\ln(0.5) = \ln 2 \approx 0.693$ 이다.

    $$
    M(0.5) = \frac{0.5 \cdot e^{0.5}}{1 - 0.5 \cdot e^{0.5}} = \frac{0.5 \times 1.6487}{1 - 0.8244} = \frac{0.8244}{0.1756} \approx 4.694
    $$

---

**연습문제 2.** 적률생성함수를 써서 독립인 두 $\text{Geo}(p)$ 확률변수의 합이 $\text{NB}(2, p)$ 임을 보여라.

??? success "연습문제 2 풀이"
    $X_1, X_2$ 가 i.i.d. $\text{Geo}(p)$ 라 하자. 그러면 다음과 같다.

    $$
    M_{X_1 + X_2}(t) = M_{X_1}(t) \cdot M_{X_2}(t) = \left[\frac{pe^t}{1-(1-p)e^t}\right]^2 = M_{\text{NB}(2,p)}(t)
    $$

    적률생성함수의 유일성에 따라 $X_1 + X_2 \sim \text{NB}(2, p)$ 이다. $\square$

---

**연습문제 3.** 적률생성함수를 직접 미분하여 $t = 0$ 에서 값을 매김으로써 $\text{Geo}(p)$ 에 대해 $E[X] = 1/p$ 임을 확인하여라.

??? success "연습문제 3 풀이"
    $q = 1-p$ 로 두면 $M(t) = pe^t(1 - qe^t)^{-1}$ 이다. 몫의 미분법과 곱의 미분법을 쓰면 다음을 얻는다.

    $$
    M'(t) = \frac{pe^t}{(1-qe^t)^2}
    $$

    $t = 0$ 에서 $M'(0) = \frac{p}{(1-q)^2} = \frac{p}{p^2} = \frac{1}{p}$ 이다. $\checkmark$

---

**연습문제 4.** $X \sim \text{NB}(3, 0.4)$ 라 하자. $E[X]$ 와 $\text{Var}(X)$ 를 구하여라.

??? success "연습문제 4 풀이"
    $$
    E[X] = \frac{r}{p} = \frac{3}{0.4} = 7.5
    $$

    $$
    \text{Var}(X) = \frac{r(1-p)}{p^2} = \frac{3 \times 0.6}{0.16} = \frac{1.8}{0.16} = 11.25
    $$

---

**연습문제 5.** 등비급수가 언제 발산하는지 살펴서 $t \geq -\ln(1-p)$ 일 때 $\text{NB}(r, p)$ 의 적률생성함수가 존재하지 않음을 보여라.

??? success "연습문제 5 풀이"
    적률생성함수는 $M(t) = \left[\frac{pe^t}{1-(1-p)e^t}\right]^r$ 이다. 분모 $1 - (1-p)e^t$ 는 $(1-p)e^t = 1$ 일 때, 곧 $e^t = 1/(1-p)$ 일 때, 다시 말해 $t = -\ln(1-p)$ 일 때 $0$ 이 된다.

    $t \geq -\ln(1-p)$ 이면 $(1-p)e^t \geq 1$ 이므로 등비급수 $\sum_{k=0}^{\infty}[(1-p)e^t]^k$ 가 발산한다. 따라서 적률생성함수는 무한대가 되거나 정의되지 않으며, $t < -\ln(1-p)$ 에서만 존재한다. $\square$
