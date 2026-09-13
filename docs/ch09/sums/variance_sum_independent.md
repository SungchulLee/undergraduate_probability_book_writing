# 합의 분산(독립인 경우)

## 간단해지는 까닭

확률변수들이 독립이면 공분산 항이 모두 사라지고, 일반 공식은 깔끔한 덧셈 규칙으로 줄어든다.

!!! info "독립인 확률변수 합의 분산"
    $X_1, X_2, \ldots, X_n$ 이 **독립**이면 다음이 성립한다.

    $$
    \text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i)
    $$

**증명.** 독립이면 $i \neq j$ 에 대하여 $\text{Cov}(X_i, X_j) = 0$ 이다. 이를 일반 공식에 넣으면 다음과 같다.

$$
\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i) + 2\sum_{i < j} \underbrace{\text{Cov}(X_i, X_j)}_{= 0} = \sum_{i=1}^n \text{Var}(X_i)
$$

$\square$

독립인 확률변수들의 가중합에 대해서는 $\text{Var}\!\left(\sum a_i X_i\right) = \sum a_i^2 \,\text{Var}(X_i)$ 가 성립한다.

---

## 대표적인 분포에 적용하기

### 이항분포의 분산

$S \sim \text{Binomial}(n, p)$ 일 때 $S = \sum_{i=1}^n X_i$ 로 적자. 여기서 $X_i \sim \text{Bernoulli}(p)$ 는 서로 독립이다. 그러면 다음을 얻는다.

$$
\text{Var}(S) = \sum_{i=1}^n \text{Var}(X_i) = n \cdot p(1-p) = npq
$$

### 음이항분포의 분산

$S \sim \text{NB}(r, p)$ 일 때 $S = \sum_{i=1}^r X_i$ 로 적자. 여기서 $X_i \sim \text{Geo}(p)$ 는 서로 독립이다. 그러면 다음을 얻는다.

$$
\text{Var}(S) = r \cdot \frac{1-p}{p^2} = \frac{r(1-p)}{p^2}
$$

### 푸아송분포의 분산

$X_i \sim \text{Poisson}(\lambda_i)$ 가 서로 독립이면 $\sum X_i \sim \text{Poisson}(\sum \lambda_i)$ 이고 다음이 성립한다.

$$
\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \lambda_i
$$

---

## 표본평균의 분산

$X_1, \ldots, X_n$ 을 분산이 $\sigma^2$ 인 i.i.d. 확률변수라 하자. 표본평균 $\bar{X}_n = \frac{1}{n}\sum X_i$ 의 분산은 다음과 같다.

$$
\text{Var}(\bar{X}_n) = \text{Var}\!\left(\frac{1}{n}\sum_{i=1}^n X_i\right) = \frac{1}{n^2}\sum_{i=1}^n \text{Var}(X_i) = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}
$$

!!! tip "제곱근 법칙"
    표본평균의 표준편차는 $\sigma/\sqrt{n}$ 이다. 표준오차를 절반으로 줄이려면 관측값이 **네 배** 있어야 한다. 이것이 통계적 추정과 큰수의 법칙을 떠받치는 기본 척도 법칙이다.

---

## 요약 표

| 분포 | 분해 | 분산 |
|:---|:---|:---:|
| $\text{Binomial}(n,p)$ | i.i.d. $\text{Bernoulli}(p)$ $n$ 개 | $npq$ |
| $\text{NB}(r,p)$ | i.i.d. $\text{Geo}(p)$ $r$ 개 | $r(1-p)/p^2$ |
| $\text{Poisson}(\lambda_1 + \cdots + \lambda_n)$ | 독립인 푸아송 $n$ 개 | $\sum \lambda_i$ |
| $\bar{X}_n$ (i.i.d., 분산 $\sigma^2$) | i.i.d. $n$ 개의 평균 | $\sigma^2/n$ |

---

## 예제

??? example "독립인 주사위들의 합"
    공정한 주사위 $n = 10$ 개를 던진다. 각 $X_i$ 를 한 주사위의 눈이라 하고 $S = \sum_{i=1}^{10} X_i$ 라 하자.

    주사위 하나의 분산은 $\text{Var}(X_i) = 35/12$ 이다. 독립성에 따라 다음을 얻는다.

    $$
    \text{Var}(S) = 10 \cdot \frac{35}{12} = \frac{350}{12} \approx 29.17
    $$

    $$
    \text{SD}(S) = \sqrt{29.17} \approx 5.40
    $$

    $E[S] = 35$ 와 합쳐 보면 주사위 10개의 눈의 합은 대략 $35 \pm 5.4$ 임을 알 수 있다.

---

## 파이썬으로 확인하기

```python
import numpy as np

np.random.seed(42)
N = 500_000

# i.i.d. 베르누이로 구하는 이항분포의 분산
n, p = 20, 0.3
X = np.random.binomial(1, p, (N, n))
S = X.sum(axis=1)
print(f"Binomial({n},{p}): Var theory = {n*p*(1-p):.2f}, MC = {np.var(S):.2f}")

# 표본평균의 분산
sigma_sq = 4.0
n_obs = 50
samples = np.random.normal(0, np.sqrt(sigma_sq), (N, n_obs))
X_bar = samples.mean(axis=1)
print(f"\nVar(X_bar) theory = {sigma_sq/n_obs:.4f}, MC = {np.var(X_bar):.4f}")

# 주사위 10개의 합
dice = np.random.randint(1, 7, (N, 10))
S_dice = dice.sum(axis=1)
print(f"\nVar(10 dice) theory = {10*35/12:.2f}, MC = {np.var(S_dice):.2f}")
```

## 연습문제

**연습문제 1.** $X_1, \ldots, X_{50}$ 이 i.i.d.이고 $E[X_i] = 10$, $\text{Var}(X_i) = 16$ 이라 하자. $E[\bar{X}_{50}]$, $\text{Var}(\bar{X}_{50})$, $\text{SD}(\bar{X}_{50})$ 을 구하여라.

??? success "연습문제 1 풀이"
    $$
    E[\bar{X}_{50}] = 10
    $$

    $$
    \text{Var}(\bar{X}_{50}) = \frac{16}{50} = 0.32
    $$

    $$
    \text{SD}(\bar{X}_{50}) = \sqrt{0.32} \approx 0.566
    $$
