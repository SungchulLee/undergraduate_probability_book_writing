# 베르누이분포와 이항분포의 적률생성함수

## Bernoulli(p)의 적률생성함수

$X \sim \text{Bernoulli}(p)$ 이면 다음과 같다.

$$M_X(t) = E[e^{tX}] = e^{t \cdot 1} \cdot p + e^{t \cdot 0} \cdot (1 - p) = 1 + p(e^t - 1)$$

$$\boxed{M_{\text{Bernoulli}(p)}(t) = 1 + p(e^t - 1)}$$

## Binomial(n, p)의 적률생성함수

$X \sim B(n, p)$ 이면 $X = \sum_{k=1}^n X_k$ 로 적을 수 있다. 여기서 $X_k \sim \text{Bernoulli}(p)$ 는 i.i.d. 이다. 독립성에 따라 다음을 얻는다.

$$M_X(t) = \prod_{k=1}^n M_{X_k}(t) = \prod_{k=1}^n \left[1 + p(e^t - 1)\right] = \left[1 + p(e^t - 1)\right]^n$$

$$\boxed{M_{B(n,p)}(t) = \left[1 + p(e^t - 1)\right]^n}$$

## 적률 유도하기

베르누이분포의 적률생성함수 $M(t) = 1 + p(e^t - 1)$ 에서 다음을 얻는다.

$$M'(t) = pe^t \implies E[X] = M'(0) = p$$

$$M''(t) = pe^t \implies E[X^2] = M''(0) = p$$

$$\text{Var}(X) = E[X^2] - (E[X])^2 = p - p^2 = p(1 - p)$$

이항분포의 적률생성함수 $M(t) = [1 + p(e^t - 1)]^n$ 에서는 다음과 같다.

$$M'(t) = n[1 + p(e^t - 1)]^{n-1} \cdot pe^t$$

$$E[X] = M'(0) = n \cdot 1 \cdot p = np$$

$M''(0)$ 을 계산하면 다음을 얻는다.

$$\text{Var}(X) = np(1 - p)$$

## 파이썬으로 확인하기

```python
import numpy as np

def mgf_binomial(t, n, p):
    return (1 + p * (np.exp(t) - 1))**n

# Binomial(20, 0.3): E[X] = 6, Var(X) = 4.2
n, p = 20, 0.3
dt = 1e-6

M0 = mgf_binomial(0, n, p)
M1 = (mgf_binomial(dt, n, p) - mgf_binomial(-dt, n, p)) / (2 * dt)
M2 = (mgf_binomial(dt, n, p) - 2*M0 + mgf_binomial(-dt, n, p)) / dt**2

print(f"B({n}, {p}):")
print(f"  E[X]   = {M1:.4f}  (exact: {n*p})")
print(f"  Var(X) = {M2 - M1**2:.4f}  (exact: {n*p*(1-p)})")
```

## 연습문제

**연습문제 1.** $\text{Bernoulli}(p)$ 의 적률생성함수를 써서 $E[X^3]$ 을 구하여라.

??? success "연습문제 1 풀이"
    $M(t) = 1 + p(e^t - 1)$ 이고 $M'''(t) = pe^t$ 이다. 그러므로 $E[X^3] = M'''(0) = p$ 이다.

    $X \in \{0, 1\}$ 이므로 $X^3 = X$ 라는 사실에서도 곧바로 따라 나온다.

---

**연습문제 2.** $M_{B(n,p)}(0) = 1$ 임을 확인하고, 어떤 적률생성함수에서도 왜 이것이 반드시 성립해야 하는지 설명하여라.

??? success "연습문제 2 풀이"
    $M_{B(n,p)}(0) = [1 + p(e^0 - 1)]^n = [1 + 0]^n = 1$ 이다.

    어떤 확률변수 $X$ 에 대해서도 $M_X(0) = E[e^{0 \cdot X}] = E[1] = 1$ 이다. $t = 0$ 에서의 적률생성함수는 상수 1의 기댓값이므로 반드시 이렇게 되어야 한다.

---

**연습문제 3.** 적률생성함수의 유일성을 써서, $X \sim B(n, p)$ 와 $Y \sim B(m, p)$ 가 독립이면 $X + Y \sim B(n + m, p)$ 임을 증명하여라.

??? success "연습문제 3 풀이"
    $M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = [1 + p(e^t - 1)]^n \cdot [1 + p(e^t - 1)]^m = [1 + p(e^t - 1)]^{n+m}$ 이다.

    이것은 $B(n+m, p)$ 의 적률생성함수이다. 유일성 정리에 따라 $X + Y \sim B(n+m, p)$ 이다. $\square$

---

**연습문제 4.** 적률생성함수를 써서 $X \sim B(n, p)$ 에 대한 $E[X(X-1)]$ 을 계산하여라.

??? success "연습문제 4 풀이"
    $E[X(X-1)] = E[X^2] - E[X]$ 이다. $M''(0) = E[X^2]$ 에서 출발하자.

    $M'(t) = np e^t [1 + p(e^t-1)]^{n-1}$ 이다.

    $t = 0$ 에서의 $M''(t)$ 는 곱의 미분법으로 구한다. $M''(0) = np[(n-1)p + 1] = n^2p^2 - np^2 + np$ 이다.

    $$
    E[X(X-1)] = n^2p^2 - np^2 + np - np = n(n-1)p^2
    $$

    이 값이 곧 **계승적률**이다. 즉 $E[X(X-1)] = n(n-1)p^2$ 이다.

---

**연습문제 5.** 베르누이분포의 적률생성함수는 $q = 1-p$ 로 두고 $M(t) = q + pe^t$ 로 적을 수도 있다. 이것이 $1 + p(e^t - 1)$ 과 같음을 보여라.

??? success "연습문제 5 풀이"
    $$
    q + pe^t = (1-p) + pe^t = 1 - p + pe^t = 1 + p(e^t - 1)
    $$

    $\square$
