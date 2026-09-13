# 확률적 개수의 합과 복합분포

## 문제 설정

$N$ 을 음이 아닌 정수 값을 갖는 확률변수라 하고, $X_1, X_2, \ldots$ 를 $N$ 과 독립이며 음이 아닌 정수 값을 갖는 i.i.d. 확률변수라 하자. **확률적 개수의 합**은 다음과 같다.

$$S = X_1 + X_2 + \cdots + X_N$$

여기서 $N = 0$ 일 때는 $S = 0$ 으로 약속한다. $S$ 의 분포를 **복합분포**라 한다.

## 합성 공식

!!! info "확률적 개수의 합의 확률생성함수"

    $$G_S(s) = G_N(G_X(s))$$

    확률적 개수의 합의 확률생성함수는 $N$ 의 확률생성함수에 $X$ 의 확률생성함수를 대입한 것이다.

**증명.** $N$ 으로 조건을 걸자.

$$G_S(s) = E[s^S] = \sum_{n=0}^{\infty} E[s^S \mid N = n]\,P(N = n)$$

$N = n$ 이 주어지면 $S = X_1 + \cdots + X_n$ 이므로, 독립성에 따라 다음을 얻는다.

$$E[s^S \mid N = n] = E[s^{X_1 + \cdots + X_n}] = [G_X(s)]^n$$

그러므로 다음이 성립한다.

$$G_S(s) = \sum_{n=0}^{\infty} [G_X(s)]^n P(N = n) = G_N(G_X(s)) \qquad \square$$

## 확률적 개수의 합의 적률

$G_S(s) = G_N(G_X(s))$ 를 미분하여 $s = 1$ 에서 값을 매기면 다음과 같다.

$$G_S'(s) = G_N'(G_X(s)) \cdot G_X'(s)$$

$$E[S] = G_S'(1) = G_N'(1) \cdot G_X'(1) = E[N] \cdot E[X]$$

분산은 전분산 법칙을 쓰거나 한 번 더 미분하여 얻는다.

$$\text{Var}(S) = E[N] \cdot \text{Var}(X) + \text{Var}(N) \cdot (E[X])^2$$

!!! tip "분산에 대한 발트 항등식"
    이 분산 공식은 두 가지 원천으로 쪼개진다.

    - $E[N] \cdot \text{Var}(X)$: 각 청구 금액 **안**에 있는 무작위성
    - $\text{Var}(N) \cdot (E[X])^2$: 청구 **건수**에 있는 무작위성

## 예: 복합 푸아송

$N \sim \text{Po}(\lambda)$ 이고 $X_i \stackrel{\text{iid}}{\sim} \text{Geo}(p)$ 로 확률생성함수가 $G_X(s) = \frac{ps}{1-(1-p)s}$ 라 하자.

$N$ 의 확률생성함수는 $G_N(s) = e^{\lambda(s-1)}$ 이다. 합성 공식에 따라 다음을 얻는다.

$$G_S(s) = \exp\!\left[\lambda\!\left(\frac{ps}{1-(1-p)s} - 1\right)\right] = \exp\!\left[\lambda \cdot \frac{ps - 1 + (1-p)s}{1-(1-p)s}\right]$$

$$= \exp\!\left[\lambda \cdot \frac{s - 1}{1-(1-p)s}\right]$$

**적률:**

$$E[S] = E[N] \cdot E[X] = \lambda \cdot \frac{1}{p} = \frac{\lambda}{p}$$

$$\text{Var}(S) = \lambda \cdot \frac{1-p}{p^2} + \lambda \cdot \frac{1}{p^2} = \frac{\lambda(2-p)}{p^2}$$

## 예: 복합 이항

$N \sim B(n, q)$ 이고 $X_i \stackrel{\text{iid}}{\sim} \text{Bernoulli}(p)$ 이며 모두 독립이라 하자. 그러면 다음과 같다.

$$G_S(s) = [1 - q + q(1 - p + ps)]^n = [1 - qp + qps]^n$$

이것은 $B(n, qp)$ 의 확률생성함수이므로 $S \sim B(n, qp)$ 이다. 베르누이 항을 더하는 복합 이항은 단순한 이항분포로 되돌아간다.

## 파이썬으로 확인하기

```python
import numpy as np

np.random.seed(42)
n_sim = 100000

# 복합 푸아송: N ~ Po(10), X_i ~ Geo(0.4)
lam, p = 10.0, 0.4

S = np.zeros(n_sim)
for i in range(n_sim):
    N = np.random.poisson(lam)
    if N > 0:
        X = np.random.geometric(p, size=N)
        S[i] = X.sum()

EX = 1 / p
VarX = (1 - p) / p**2

print("Compound Poisson: N ~ Po(10), X_i ~ Geo(0.4)")
print(f"  E[S]   = {S.mean():.4f}  (exact: {lam * EX:.4f})")
print(f"  Var(S) = {S.var():.4f}  (exact: {lam*VarX + lam*EX**2:.4f})")
```

## 연습문제

**연습문제 1.**
$N \sim \text{Po}(4)$ 이고 $X_i \stackrel{\text{iid}}{\sim} \text{Bernoulli}(0.5)$ 가 $N$ 과 독립이라 하자. $S = X_1 + \cdots + X_N$ 이라 하자.

**(a)** 합성 공식을 써서 $G_S(s)$ 를 구하여라.

**(b)** $S$ 의 분포를 알아내어라.

**(c)** $E[S]$ 와 $\text{Var}(S)$ 를 계산하여라.

??? success "연습문제 1 풀이"

    **(a)** $G_X(s) = 0.5 + 0.5s$ 이고 $G_N(s) = e^{4(s-1)}$ 이다.

    $G_S(s) = G_N(G_X(s)) = e^{4(0.5 + 0.5s - 1)} = e^{2(s-1)}$

    **(b)** 이것은 $\text{Po}(2)$ 의 확률생성함수이다. 그러므로 $S \sim \text{Po}(2)$ 이다.

    **(c)** $E[S] = E[N] \cdot E[X] = 4 \cdot 0.5 = 2$ 이고 $\text{Var}(S) = 4 \cdot 0.25 + 4 \cdot 0.25 = 2$ 이다. 둘 다 $\text{Po}(2)$ 와 들어맞는다.
