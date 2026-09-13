# 적률생성함수의 정의와 성질

## 정의

확률변수 $X$ 의 **적률생성함수(MGF)** 는 다음과 같이 정의된다.

$$M_X(t) = E[e^{tX}]$$

단, 이 기댓값이 $t = 0$ 의 어떤 근방에서 존재해야 한다.

이산인 경우와 연속인 경우로 나누어 적으면 다음과 같다.

$$M_X(t) = \begin{cases} \displaystyle\sum_x e^{tx} \, p(x) & X \text{ 가 이산일 때} \\[10pt] \displaystyle\int_{-\infty}^{\infty} e^{tx} f(x)\,dx & X \text{ 가 연속일 때} \end{cases}$$

## 왜 "적률을 만들어 내는" 함수인가

적률생성함수는 $t = 0$ 에서 미분하는 것만으로 $X$ 의 모든 적률을 만들어 낸다.

$$M_X^{(n)}(0) = E[X^n]$$

**유도:**

$$M_X(t) = E[e^{tX}] \implies M_X'(t) = E[Xe^{tX}] \implies M_X'(0) = E[X]$$

$$M_X''(t) = E[X^2 e^{tX}] \implies M_X''(0) = E[X^2]$$

$$\vdots$$

$$M_X^{(n)}(t) = E[X^n e^{tX}] \implies M_X^{(n)}(0) = E[X^n]$$

특히 다음이 성립한다.

- $E[X] = M_X'(0)$
- $\text{Var}(X) = M_X''(0) - [M_X'(0)]^2$

## 적률생성함수가 쓸모 있는 까닭

!!! info "두 가지 핵심 성질"

    1. **유일성:** $0$ 의 어떤 근방에 있는 모든 $t$ 에 대해 $M_X(t) = M_Y(t)$ 이면, $X$ 와 $Y$ 는 **같은 분포**를 갖는다.

    2. **수렴성:** $0$ 의 어떤 근방에 있는 모든 $t$ 에 대해 $M_{X_n}(t) \to M_Y(t)$ 이면, $X_n \xrightarrow{d} Y$ 이다(분포수렴).

성질 (1) 덕분에 적률생성함수를 맞추어 보는 것만으로 분포를 **알아낼** 수 있다. 성질 (2)는 **중심극한정리의 증명**에서 열쇠가 되는 도구이다.

## 파이썬 구현

```python
import numpy as np
from scipy.misc import derivative

# X ~ Exp(1)에 대해 MGF의 성질을 수치적으로 확인한다
# t < 1일 때 M_X(t) = 1/(1-t)
def mgf_exp(t, lam=1):
    """Exp(lambda)의 적률생성함수: lambda/(lambda - t)"""
    return lam / (lam - t)

# 1차 적률: E[X] = M'(0)
EX = derivative(mgf_exp, 0, n=1, dx=1e-6)
print(f"E[X] = M'(0) = {EX:.6f}  (exact: 1.0)")

# 2차 적률: E[X^2] = M''(0)
EX2 = derivative(mgf_exp, 0, n=2, dx=1e-6)
print(f"E[X²] = M''(0) = {EX2:.4f}  (exact: 2.0)")

# 분산
VarX = EX2 - EX**2
print(f"Var(X) = {VarX:.4f}  (exact: 1.0)")
```

**실행 결과:**
```
E[X] = M'(0) = 1.000000  (exact: 1.0)
E[X²] = M''(0) = 2.0000  (exact: 2.0)
Var(X) = 1.0000  (exact: 1.0)
```

## 연습문제

**연습문제 1.**
$X$ 의 확률질량함수가 $P(X = -1) = \tfrac{1}{4}$, $P(X = 0) = \tfrac{1}{2}$, $P(X = 1) = \tfrac{1}{4}$ 라고 하자.

**(a)** $M_X(t)$ 를 구하여라.

**(b)** 적률생성함수를 써서 $E[X]$ 와 $\text{Var}(X)$ 를 구하여라.

??? success "연습문제 1 풀이"

    **(a)**

    $$M_X(t) = \tfrac{1}{4}e^{-t} + \tfrac{1}{2} + \tfrac{1}{4}e^{t} = \tfrac{1}{2} + \tfrac{1}{2}\cosh(t)$$

    **(b)** $M_X'(t) = \tfrac{1}{4}(-e^{-t} + e^{t}) = \tfrac{1}{2}\sinh(t)$ 이므로 $E[X] = M_X'(0) = 0$ 이다.

    $M_X''(t) = \tfrac{1}{2}\cosh(t)$ 이므로 $E[X^2] = M_X''(0) = \tfrac{1}{2}$ 이다.

    따라서 $\text{Var}(X) = \tfrac{1}{2} - 0 = \tfrac{1}{2}$ 이다.
