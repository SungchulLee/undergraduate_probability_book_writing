# 독립확률변수 합의 적률생성함수

## 곱의 법칙

!!! info "독립확률변수 합의 적률생성함수"
    $X$ 와 $Y$ 가 **독립**이고 각각의 적률생성함수가 존재하면 다음이 성립한다.

    $$M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$$

**증명.**

$$M_{X+Y}(t) = E[e^{t(X+Y)}] = E[e^{tX} e^{tY}]$$

$X$ 와 $Y$ 가 독립이므로 $e^{tX}$ 와 $e^{tY}$ 도 독립이고, 따라서 기댓값이 곱으로 쪼개진다.

$$= E[e^{tX}] \cdot E[e^{tY}] = M_X(t) \cdot M_Y(t) \qquad \square$$

!!! warning "독립성은 없어서는 안 된다"
    독립이 아니면 곱의 법칙은 성립하지 않는다. $X$ 와 $Y$ 가 종속이면 일반적으로 $E[e^{tX}e^{tY}] \neq E[e^{tX}]\,E[e^{tY}]$ 이다.

## n개의 독립확률변수로 넓히기

$X_1, X_2, \ldots, X_n$ 이 독립이면 귀납법에 따라 다음이 성립한다.

$$M_{X_1 + X_2 + \cdots + X_n}(t) = \prod_{i=1}^n M_{X_i}(t)$$

특히 $X_i$ 가 i.i.d. 이고 공통 적률생성함수가 $M_X(t)$ 이면 다음과 같다.

$$M_{S_n}(t) = [M_X(t)]^n \quad \text{여기서 } S_n = X_1 + \cdots + X_n$$

## 예: 독립인 지수확률변수의 합

$X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} \text{Exp}(\lambda)$ 라 하자. 각각의 적률생성함수는 $M_{X_i}(t) = \frac{\lambda}{\lambda - t}$ 이다.

$$M_{S_n}(t) = \left(\frac{\lambda}{\lambda - t}\right)^n$$

이것은 $\text{Gamma}(n, \lambda)$ 의 적률생성함수이다. 유일성 정리에 따라 다음을 얻는다.

$$X_1 + X_2 + \cdots + X_n \sim \text{Gamma}(n, \lambda)$$

이로써 i.i.d. 지수확률변수 $n$ 개의 합이 감마분포를 따른다는 것을 적률생성함수로 증명한 셈이다.

## 예: 독립인 푸아송확률변수의 합

$X \sim \text{Po}(\lambda)$ 와 $Y \sim \text{Po}(\mu)$ 가 독립이라 하자. 각각의 적률생성함수는 $e^{\lambda(e^t - 1)}$ 과 $e^{\mu(e^t - 1)}$ 이다.

$$M_{X+Y}(t) = e^{\lambda(e^t - 1)} \cdot e^{\mu(e^t - 1)} = e^{(\lambda + \mu)(e^t - 1)}$$

이것은 $\text{Po}(\lambda + \mu)$ 의 적률생성함수이다. 유일성에 따라 다음을 얻는다.

$$X + Y \sim \text{Po}(\lambda + \mu)$$

## 일차변환

$Y = aX + b$ 에 대해서는 다음이 성립한다.

$$M_Y(t) = E[e^{t(aX+b)}] = e^{bt}\,M_X(at)$$

이것을 곱의 법칙과 함께 쓸 수 있다. 예를 들어 $X_1, \ldots, X_n$ 이 공통 적률생성함수 $M_X(t)$ 를 갖는 i.i.d. 이고 $\bar{X} = \frac{1}{n}\sum X_i$ 라 하면 다음과 같다.

$$M_{\bar{X}}(t) = \left[M_X\!\left(\frac{t}{n}\right)\right]^n$$

## 파이썬으로 확인하기

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n_sim = 100000

# i.i.d. Exp(2) 5개의 합은 Gamma(5, scale=0.5)여야 한다
lam = 2.0
n = 5
samples = np.sum(np.random.exponential(1/lam, (n_sim, n)), axis=1)

print(f"Sum of {n} iid Exp({lam}):")
print(f"  Mean:  {samples.mean():.4f}  (exact: {n/lam})")
print(f"  Var:   {samples.var():.4f}  (exact: {n/lam**2})")

# 독립인 Po(3) + Po(5)의 합은 Po(8)이어야 한다
X = np.random.poisson(3, n_sim)
Y = np.random.poisson(5, n_sim)
S = X + Y

print(f"\nPo(3) + Po(5):")
print(f"  Mean:  {S.mean():.4f}  (exact: 8)")
print(f"  Var:   {S.var():.4f}  (exact: 8)")
```

## 연습문제

**연습문제 1.**
$X \sim \text{Gamma}(2, 3)$ 과 $Y \sim \text{Gamma}(5, 3)$ 이 독립이라 하자.

**(a)** $M_{X+Y}(t)$ 를 구하여라.

**(b)** $X + Y$ 의 분포를 알아내어라.

**(c)** 대신 $Y \sim \text{Gamma}(5, 4)$ 라면 무엇이 어긋나는가?

??? success "연습문제 1 풀이"

    **(a)** $M_{X+Y}(t) = \left(\frac{3}{3-t}\right)^2 \cdot \left(\frac{3}{3-t}\right)^5 = \left(\frac{3}{3-t}\right)^7$ 이다.

    **(b)** 유일성에 따라 $X + Y \sim \text{Gamma}(7, 3)$ 이다.

    **(c)** $M_{X+Y}(t) = \left(\frac{3}{3-t}\right)^2\left(\frac{4}{4-t}\right)^5$ 이 되는데, 이는 어떤 표준 감마분포의 적률생성함수와도 맞지 않는다. 비율 모수가 다른 감마확률변수의 합은 감마분포가 아니다.
