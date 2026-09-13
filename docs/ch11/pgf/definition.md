# 확률생성함수의 정의와 성질

## 정의

음이 아닌 정수 값을 갖는 확률변수 $X$ 의 **확률생성함수(PGF)** 는 다음과 같이 정의된다.

$$G_X(s) = E[s^X] = \sum_{k=0}^{\infty} P(X = k)\,s^k$$

$|s^k P(X=k)| \leq P(X=k)$ 이고 $\sum P(X=k) = 1$ 이므로, 이 급수는 $|s| \leq 1$ 에서 절대수렴한다.

!!! note "확률생성함수는 왜 쓰는가"
    확률생성함수는 계수가 확률 $P(X = k)$ 인 멱급수이다. $X$ 의 분포 전체를 함수 하나에 담아 두며, 개수를 세는 것처럼 음이 아닌 정수 값을 갖는 확률변수에 특히 편리하다.

## 주요 성질

!!! info "확률생성함수의 성질"
    음이 아닌 정수 값을 갖는 확률변수 $X$ 에 대해 다음이 성립한다.

    1. $G_X(0) = P(X = 0)$
    2. $G_X(1) = 1$
    3. $G_X'(1) = E[X]$
    4. $G_X''(1) = E[X(X-1)]$ (2차 계승적률)
    5. $\text{Var}(X) = G_X''(1) + G_X'(1) - [G_X'(1)]^2$

**(3)의 증명.** 멱급수를 미분하면 다음과 같다.

$$G_X'(s) = \sum_{k=1}^{\infty} k\,P(X = k)\,s^{k-1}$$

$$G_X'(1) = \sum_{k=1}^{\infty} k\,P(X = k) = E[X]$$

**(4)의 증명.** 한 번 더 미분하면 다음과 같다.

$$G_X''(s) = \sum_{k=2}^{\infty} k(k-1)\,P(X = k)\,s^{k-2}$$

$$G_X''(1) = \sum_{k=2}^{\infty} k(k-1)\,P(X = k) = E[X(X-1)]$$

**분산 유도하기.** $E[X(X-1)] = E[X^2] - E[X]$ 이므로 다음을 얻는다.

$$E[X^2] = G_X''(1) + G_X'(1)$$

$$\text{Var}(X) = E[X^2] - (E[X])^2 = G_X''(1) + G_X'(1) - [G_X'(1)]^2$$

## 확률 되찾기

확률질량함수는 $s = 0$ 에서 확률생성함수를 미분하여 되찾을 수 있다.

$$P(X = k) = \frac{G_X^{(k)}(0)}{k!}$$

$G_X(s) = \sum P(X=k)\,s^k$ 가 $0$ 을 중심으로 한 테일러급수이기 때문이다.

## 적률생성함수와의 관계

확률생성함수와 적률생성함수는 $s = e^t$ 라는 치환으로 이어져 있다.

$$M_X(t) = E[e^{tX}] = E[(e^t)^X] = G_X(e^t)$$

같은 말로, $s > 0$ 에 대해 $G_X(s) = M_X(\ln s)$ 이다.

## 독립인 합에 대한 곱의 법칙

$X$ 와 $Y$ 가 음이 아닌 정수 값을 갖는 독립확률변수이면 다음이 성립한다.

$$G_{X+Y}(s) = G_X(s) \cdot G_Y(s)$$

증명은 적률생성함수의 경우와 똑같다. 독립성에 따라 $E[s^{X+Y}] = E[s^X s^Y] = E[s^X]\,E[s^Y]$ 이다.

## 파이썬으로 확인하기

```python
import numpy as np
from scipy.misc import derivative

def pgf_poisson(s, lam=3.0):
    """Po(lambda)의 확률생성함수: G(s) = exp(lambda(s - 1))"""
    return np.exp(lam * (s - 1))

lam = 3.0

# P(X = 0) = G(0)
print(f"Po({lam}):")
print(f"  P(X=0) = G(0) = {pgf_poisson(0, lam):.6f}  (exact: {np.exp(-lam):.6f})")
print(f"  G(1)   = {pgf_poisson(1, lam):.6f}  (exact: 1)")

# E[X] = G'(1)
EX = derivative(pgf_poisson, 1, n=1, dx=1e-6)
print(f"  E[X]   = G'(1) = {EX:.4f}  (exact: {lam})")

# E[X(X-1)] = G''(1)
EXX1 = derivative(pgf_poisson, 1, n=2, dx=1e-6)
VarX = EXX1 + EX - EX**2
print(f"  Var(X) = {VarX:.4f}  (exact: {lam})")
```

## 연습문제

**연습문제 1.**
$X \sim \text{Po}(\lambda)$ 의 확률생성함수가 $G_X(s) = e^{\lambda(s-1)}$ 이라 하자.

**(a)** $G_X(0) = P(X = 0)$ 과 $G_X(1) = 1$ 을 확인하여라.

**(b)** $G'(1)$ 과 $G''(1)$ 을 써서 $E[X]$ 와 $\text{Var}(X)$ 를 계산하여라.

**(c)** $G''(0)/2!$ 을 계산하여 확률생성함수에서 $P(X = 2)$ 를 되찾아라.

??? success "연습문제 1 풀이"

    **(a)** $G(0) = e^{-\lambda} = P(X=0)$ 이고 $G(1) = e^0 = 1$ 이다. 둘 다 맞다.

    **(b)** $G'(s) = \lambda e^{\lambda(s-1)}$ 이므로 $E[X] = G'(1) = \lambda$ 이다. $G''(s) = \lambda^2 e^{\lambda(s-1)}$ 이므로 $G''(1) = \lambda^2$ 이다.

    따라서 $\text{Var}(X) = \lambda^2 + \lambda - \lambda^2 = \lambda$ 이다.

    **(c)** $G''(0) = \lambda^2 e^{-\lambda}$ 이므로 $P(X=2) = \frac{\lambda^2 e^{-\lambda}}{2}$ 이고, 이는 $\frac{e^{-\lambda}\lambda^2}{2!}$ 과 일치한다.
