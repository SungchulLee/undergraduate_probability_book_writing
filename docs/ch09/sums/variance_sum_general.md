# 합의 분산(일반 공식)

## 왜 필요한가

$E[X + Y] = E[X] + E[Y]$ 가 언제나 성립한다는 것은 이미 알고 있다. 분산도 같은 식으로 움직일까? 일반적으로는 **그렇지 않다**. 합의 분산은 각각의 분산뿐 아니라 변수들이 함께 어떻게 움직이는지에도 달려 있다.

---

## 확률변수가 둘일 때

!!! info "두 확률변수 합의 분산"
    임의의 확률변수 $X$ 와 $Y$ 에 대하여 다음이 성립한다.

    $$
    \text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X, Y)
    $$

**유도.** $\mu_X = E[X]$, $\mu_Y = E[Y]$ 라 두자.

$$
\text{Var}(X + Y) = E\bigl[(X + Y - \mu_X - \mu_Y)^2\bigr]
$$

$$
= E\bigl[((X - \mu_X) + (Y - \mu_Y))^2\bigr]
$$

$$
= E[(X - \mu_X)^2] + 2\,E[(X - \mu_X)(Y - \mu_Y)] + E[(Y - \mu_Y)^2]
$$

$$
= \text{Var}(X) + 2\,\text{Cov}(X, Y) + \text{Var}(Y)
$$

$\square$

**차**에 대해서는 $\text{Var}(X - Y) = \text{Var}(X) + \text{Var}(Y) - 2\,\text{Cov}(X, Y)$ 가 성립한다.

---

## 확률변수가 n개일 때의 일반 공식

!!! info "일반적인 합의 분산"
    확률변수 $X_1, X_2, \ldots, X_n$ 에 대하여 다음이 성립한다.

    $$
    \text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i) + 2\sum_{1 \leq i < j \leq n} \text{Cov}(X_i, X_j)
    $$

이중합을 쓰면 이와 같은 식을 다음처럼 적을 수도 있다.

$$
\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \sum_{j=1}^n \text{Cov}(X_i, X_j)
$$

여기서 대각항은 $\text{Cov}(X_i, X_i) = \text{Var}(X_i)$ 를 주고, 비대각항은 서로 다른 변수끼리의 공분산을 보탠다.

**유도.** 공분산의 겹선형성을 쓰면 다음과 같다.

$$
\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \text{Cov}\!\left(\sum_{i=1}^n X_i,\; \sum_{j=1}^n X_j\right) = \sum_{i=1}^n \sum_{j=1}^n \text{Cov}(X_i, X_j)
$$

대각항과 비대각항을 갈라 놓으면 다음을 얻는다.

$$
= \sum_{i=1}^n \text{Var}(X_i) + \sum_{\substack{i,j=1 \\ i \neq j}}^n \text{Cov}(X_i, X_j) = \sum_{i=1}^n \text{Var}(X_i) + 2\sum_{1 \leq i < j \leq n} \text{Cov}(X_i, X_j)
$$

$\square$

---

## 항의 개수 세기

변수가 $n$ 개일 때 이 공식에는 다음이 들어 있다.

- 분산 항 $n$ 개 (대각)
- 서로 다른 공분산 항 $\binom{n}{2} = \frac{n(n-1)}{2}$ 개 (각각 한 번씩 센다)

$n$ 이 커지면 공분산 항의 개수는 $O(n^2)$ 으로 늘어나 전체를 좌우할 수 있다. 실제 응용에서 변수 하나하나의 분산보다 변수들 사이의 상관이 더 중요해지는 까닭이 여기에 있다.

---

## 가중합

상수 $a_1, \ldots, a_n$ 에 대하여 다음이 성립한다.

$$
\text{Var}\!\left(\sum_{i=1}^n a_i X_i\right) = \sum_{i=1}^n a_i^2\,\text{Var}(X_i) + 2\sum_{1 \leq i < j \leq n} a_i a_j\,\text{Cov}(X_i, X_j)
$$

---

## 예제

??? example "공분산을 아는 합의 분산"
    $X_1, X_2, X_3$ 이 모든 $i$ 에 대하여 $\text{Var}(X_i) = 4$ 이고, $i \neq j$ 인 모든 짝에 대하여 $\text{Cov}(X_i, X_j) = 1$ 이라 하자. 그러면 다음과 같다.

    $$
    \text{Var}(X_1 + X_2 + X_3) = 3(4) + 2 \cdot 3(1) = 12 + 6 = 18
    $$

    분산을 단순히 더한 값 $3(4) = 12$ 와 견주어 보자. 양의 공분산 때문에 합의 분산이 50% 만큼 커졌다.

??? example "음의 공분산은 분산을 줄인다"
    분산은 그대로 두고 대신 $i \neq j$ 인 모든 짝에 대하여 $\text{Cov}(X_i, X_j) = -1$ 이라 하면 다음과 같다.

    $$
    \text{Var}(X_1 + X_2 + X_3) = 12 + 2(3)(-1) = 12 - 6 = 6
    $$

    음의 공분산은 서로 일부를 상쇄시켜 전체 변동을 줄인다. 이것이 포트폴리오 이론에서 말하는 **분산투자**의 원리이다.

---

## 파이썬으로 확인하기

```python
import numpy as np

np.random.seed(42)
N = 500_000

# Var=4, Cov=1 인 상관된 정규확률변수 3개
mu = [0, 0, 0]
Sigma = [[4, 1, 1],
         [1, 4, 1],
         [1, 1, 4]]
samples = np.random.multivariate_normal(mu, Sigma, N)
S = samples.sum(axis=1)

print(f"Var(X1+X2+X3) theory = 18")
print(f"Var(X1+X2+X3) MC = {np.var(S):.2f}")

# 공분산이 음인 경우
Sigma_neg = [[4, -1, -1],
             [-1, 4, -1],
             [-1, -1, 4]]
samples_neg = np.random.multivariate_normal(mu, Sigma_neg, N)
S_neg = samples_neg.sum(axis=1)

print(f"\nVar (neg cov) theory = 6")
print(f"Var (neg cov) MC = {np.var(S_neg):.2f}")
```

## 연습문제

**연습문제 1.** 확률변수 $X_1, X_2, X_3$ 이 모든 $i$ 에 대하여 $\text{Var}(X_i) = 2$ 이고 $\text{Cov}(X_1, X_2) = 0.5$, $\text{Cov}(X_1, X_3) = -0.3$, $\text{Cov}(X_2, X_3) = 0.8$ 이라 하자. $\text{Var}(X_1 + X_2 + X_3)$ 을 구하여라.

??? success "연습문제 1 풀이"
    $$
    \text{Var}\!\left(\sum_i X_i\right) = \sum_i \text{Var}(X_i) + 2 \sum_{i < j} \text{Cov}(X_i, X_j) = 3 \cdot 2 + 2(0.5 - 0.3 + 0.8) = 6 + 2 = 8
    $$

---

**연습문제 2.** 분산이 모두 $\sigma^2$ 로 같고 두 개씩의 상관계수가 모두 $\rho \geq 0$ 로 같은 확률변수 $n$ 개에 대하여 다음이 성립함을 보여라.

$$
\text{Var}\!\left(\frac{1}{n} \sum_{i=1}^{n} X_i\right) = \frac{\sigma^2}{n}\bigl(1 + (n - 1)\rho\bigr)
$$

$n \to \infty$ 일 때는 어떻게 되는가? 그 결과의 뜻을 풀이하여라.

??? success "연습문제 2 풀이"
    $i \neq j$ 일 때 두 변수의 공분산은 $\text{Cov}(X_i, X_j) = \rho \sigma^2$ 이다. 그러므로 다음과 같다.

    $$
    \text{Var}\!\left(\sum_{i=1}^n X_i\right) = n \sigma^2 + n(n - 1) \rho \sigma^2 = n \sigma^2 [1 + (n - 1)\rho]
    $$

    양변을 $n^2$ 으로 나누면 다음을 얻는다.

    $$
    \text{Var}(\bar{X}_n) = \frac{\sigma^2}{n}[1 + (n - 1)\rho]
    $$

    $\rho > 0$ 을 고정한 채 $n \to \infty$ 로 보내면 $\text{Var}(\bar{X}_n) \to \rho \sigma^2 > 0$ 이다. 즉 표본평균이 상수로 수렴하지 **않는다**. 공통의 종속성이 분산에 바닥을 만들어 놓기 때문이다. $\rho = 0$ 이거나 상관이 점점 사그라지면 익숙한 $\sigma^2/n \to 0$ 이 다시 나온다. 큰수의 법칙 같은 결과가 독립성이나 약한 종속성을 요구하는 까닭이 바로 이것이다.
