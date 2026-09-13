# 적률생성함수로 적률 구하기

## 미분하는 방법

적률생성함수를 $n$ 번 미분하여 $t = 0$ 에서 값을 매기면 $n$ 차 적률이 나온다.

$$M_X^{(n)}(0) = E[X^n]$$

낮은 차수의 도함수 몇 개만으로도 가장 자주 쓰는 양들을 얻을 수 있다.

- **1차 적률:** $E[X] = M_X'(0)$
- **2차 적률:** $E[X^2] = M_X''(0)$
- **분산:** $\text{Var}(X) = M_X''(0) - [M_X'(0)]^2$

## 테일러 전개로 보는 방법

$e^{tX} = \sum_{n=0}^{\infty} \frac{(tX)^n}{n!}$ 이므로 항별로 기댓값을 취하면 다음을 얻는다.

$$M_X(t) = E[e^{tX}] = \sum_{n=0}^{\infty} \frac{E[X^n]}{n!}\,t^n$$

이것은 계수 안에 $X$ 의 모든 적률이 담겨 있는 멱급수이다. $n$ 차 적률을 뽑아내려면 $t^n$ 의 계수를 읽어 $n!$ 을 곱하면 된다.

$$E[X^n] = n! \cdot [M_X(t) \text{ 에서 } t^n \text{ 의 계수}]$$

!!! tip "어느 방법을 언제 쓸 것인가"

    - **미분하는 방법:** 적률생성함수가 미분하기 쉬운 간단한 닫힌 꼴일 때 가장 좋다(지수분포, 푸아송분포 등).
    - **테일러 전개:** 적률생성함수가 이미 멱급수 꼴이거나 전개하기 쉬울 때 가장 좋다($e^{\lambda(e^t - 1)}$ 등).

## 풀이 예제

???+ example "$M_X(t) = e^{3t + 2t^2}$ 에서 적률 뽑아내기"
    **미분하는 방법.** $M_X(t) = e^{3t + 2t^2}$ 로 두고 $g(t) = 3t + 2t^2$ 이라 하자.

    $$M_X'(t) = g'(t)\,M_X(t) = (3 + 4t)\,e^{3t + 2t^2}$$

    $$E[X] = M_X'(0) = 3 \cdot 1 = 3$$

    2차 도함수는 곱의 미분법을 쓴다.

    $$M_X''(t) = g''(t)\,M_X(t) + [g'(t)]^2\,M_X(t) = [4 + (3+4t)^2]\,e^{3t + 2t^2}$$

    $$E[X^2] = M_X''(0) = 4 + 9 = 13$$

    $$\text{Var}(X) = 13 - 3^2 = 4$$

    **테일러 전개로 보는 방법.** $e^{3t + 2t^2} = e^{3t} \cdot e^{2t^2}$ 으로 쪼개어 전개한다.

    $$e^{3t} = 1 + 3t + \frac{9t^2}{2} + \cdots, \qquad e^{2t^2} = 1 + 2t^2 + \cdots$$

    $$M_X(t) = 1 + 3t + \left(\frac{9}{2} + 2\right)t^2 + \cdots = 1 + 3t + \frac{13}{2}\,t^2 + \cdots$$

    계수를 읽으면 $E[X] = 1! \cdot 3 = 3$ 이고 $E[X^2] = 2! \cdot \frac{13}{2} = 13$ 이다.

## 정규분포의 적률생성함수 알아보기

적률생성함수 $M_X(t) = e^{3t + 2t^2}$ 은 정규분포의 꼴 $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$ 에 $\mu = 3$, $\sigma^2 = 4$ 를 넣은 것과 같다. 그러므로 $X \sim N(3, 4)$ 이고, 이는 앞에서 얻은 $E[X] = 3$, $\text{Var}(X) = 4$ 와 들어맞는다.

## 파이썬으로 확인하기

```python
import numpy as np
from scipy.misc import derivative

def mgf(t):
    """M_X(t) = exp(3t + 2t^2)"""
    return np.exp(3 * t + 2 * t**2)

# 수치미분으로 적률을 뽑아낸다
EX = derivative(mgf, 0, n=1, dx=1e-6)
EX2 = derivative(mgf, 0, n=2, dx=1e-6)
VarX = EX2 - EX**2

print("M_X(t) = exp(3t + 2t^2)")
print(f"  E[X]   = {EX:.4f}   (exact: 3)")
print(f"  E[X^2] = {EX2:.4f}  (exact: 13)")
print(f"  Var(X) = {VarX:.4f}   (exact: 4)")
```

## 연습문제

**연습문제 1.**
$t < \tfrac{1}{2}$ 에 대해 $M_X(t) = \frac{1}{1 - 2t}$ 라고 하자.

**(a)** $M_X(t)$ 를 멱급수로 전개하여 일반적인 $n$ 에 대한 $E[X^n]$ 을 알아내어라.

**(b)** $X$ 는 어떤 이름 있는 분포를 따르는가?

??? success "연습문제 1 풀이"

    **(a)** $\frac{1}{1-2t} = \sum_{n=0}^{\infty}(2t)^n = \sum_{n=0}^{\infty} 2^n t^n$ 이다. $M_X(t) = \sum \frac{E[X^n]}{n!}t^n$ 이므로 $E[X^n] = 2^n \cdot n!$ 을 얻는다.

    **(b)** 이것은 $\text{Exp}(\tfrac{1}{2})$ 의 적률생성함수이다. 곧 $\lambda = \tfrac{1}{2}$ 일 때 $\frac{\lambda}{\lambda - t} = \frac{1/2}{1/2 - t} = \frac{1}{1-2t}$ 이다.

---

**연습문제 2.**
$t < \tfrac{1}{2}$ 에 대해 $M_X(t) = \frac{1}{1 - 2t}$ 라고 하자.

**(a)** $M_X(t)$ 를 멱급수로 전개하여 일반적인 $n$ 에 대한 $E[X^n]$ 을 알아내어라.

**(b)** $X$ 는 어떤 이름 있는 분포를 따르는가?

??? success "연습문제 2 풀이"

    **(a)** $\frac{1}{1-2t} = \sum_{n=0}^{\infty}(2t)^n = \sum_{n=0}^{\infty} 2^n t^n$ 이다. $M_X(t) = \sum \frac{E[X^n]}{n!}t^n$ 이므로 $E[X^n] = 2^n \cdot n!$ 을 얻는다.

    **(b)** 이것은 $\text{Exp}(\tfrac{1}{2})$ 의 적률생성함수이다. 곧 $\lambda = \tfrac{1}{2}$ 일 때 $\frac{\lambda}{\lambda - t} = \frac{1/2}{1/2 - t} = \frac{1}{1-2t}$ 이다.
