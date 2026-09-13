# 불편추정량(표본평균과 표본분산)

## 정의

### 모수

**모수** $\theta$ 는 분포가 지닌 수치적 특성이다(이를테면 평균 $\mu$, 분산 $\sigma^2$).

### 통계량

**통계량**이란 관측된 표본의 함수 $f(X_1, X_2, \ldots, X_n)$ 을 말한다.

### 추정량

$\theta$ 의 **추정량**이란 모수 $\theta$ 를 어림하는 데 쓰는 통계량 $f(X_1, X_2, \ldots, X_n)$ 이다.

### 불편추정량

$\theta$ 의 추정량 $f(X_1, X_2, \ldots, X_n)$ 이 다음을 만족하면 **불편**이라 한다.

$$
E[f(X_1, X_2, \ldots, X_n)] = \theta
$$

곧 평균적으로 보면 추정량이 옳은 값을 준다는 뜻이다.

---

## 평균의 불편추정량

$X_1, X_2, \ldots, X_n$ 을 평균 $\mu$ 와 분산 $\sigma^2$ 를 모르는 어떤 분포에서 뽑은 i.i.d. 표본이라 하자.

**표본평균**은 다음과 같다.

$$
\bar{X} = \frac{\sum_{i=1}^n X_i}{n}
$$

**불편성**: 기댓값의 선형성에 따라 다음을 얻는다.

$$
E[\bar{X}] = \frac{\sum_{i=1}^n E[X_i]}{n} = \frac{n\mu}{n} = \mu \quad \checkmark
$$

**표본평균의 분산**:

$$
\text{Var}(\bar{X}) = \frac{1}{n^2} \text{Var}\left(\sum_{i=1}^n X_i\right) = \frac{1}{n^2} \sum_{i=1}^n \text{Var}(X_i) = \frac{\sigma^2}{n}
$$

!!! note "표준오차"
    $\text{SE}(\bar{X}) = \text{SD}(\bar{X}) = \frac{\sigma}{\sqrt{n}}$ 를 평균의 **표준오차**라 한다. $n$ 이 커질수록 작아지므로, 자료가 많을수록 더 촘촘한 추정을 얻는다는 뜻이다.

---

## 분산의 불편추정량

**표본분산**은 다음과 같다.

$$
S^2 = \frac{\sum_{i=1}^n (X_i - \bar{X})^2}{n - 1}
$$

**불편성**: $E[S^2] = \sigma^2$ 임을 보여야 한다.

### 증명

**1단계**: $(X_i - \bar{X})^2$ 를 전개한다.

$$
(X_i - \bar{X})^2 = \left[(X_i - \mu) - (\bar{X} - \mu)\right]^2 = (X_i - \mu)^2 + (\bar{X} - \mu)^2 - 2(X_i - \mu)(\bar{X} - \mu)
$$

**2단계**: 기댓값을 취한다.

$$
E[(X_i - \bar{X})^2] = \sigma^2 + \frac{\sigma^2}{n} - 2E[(X_i - \mu)(\bar{X} - \mu)]
$$

**3단계**: $E[(X_i - \mu)(\bar{X} - \mu)]$ 를 계산한다.

$$
E[(X_i - \mu)(\bar{X} - \mu)] = E\left[(X_i - \mu) \cdot \frac{\sum_{j=1}^n (X_j - \mu)}{n}\right]
$$

$$
= E\left[(X_i - \mu) \cdot \frac{\sum_{j \neq i}(X_j - \mu)}{n} + \frac{(X_i - \mu)}{n}\right]
$$

$j \neq i$ 일 때 $X_i$ 와 $X_j$ 가 독립이므로 $E[(X_i - \mu)(X_j - \mu)] = 0$ 이다. 그러므로 다음을 얻는다.

$$
E[(X_i - \mu)(\bar{X} - \mu)] = \frac{1}{n}E[(X_i - \mu)^2] = \frac{\sigma^2}{n}
$$

**4단계**: 모아서 정리한다.

$$
E[(X_i - \bar{X})^2] = \sigma^2 + \frac{\sigma^2}{n} - \frac{2\sigma^2}{n} = \sigma^2 \cdot \frac{n-1}{n}
$$

**5단계**: 모두 더하고 나눈다.

$$
E[S^2] = \frac{\sum_{i=1}^n E[(X_i - \bar{X})^2]}{n-1} = \frac{n \cdot \frac{n-1}{n}\sigma^2}{n-1} = \sigma^2 \quad \checkmark
$$

---

## 왜 n-1 로 나누는가

$n$ 으로 나누었다면 다음을 얻었을 것이다.

$$
E\left[\frac{\sum(X_i - \bar{X})^2}{n}\right] = \frac{n-1}{n}\sigma^2 < \sigma^2
$$

이것은 $\sigma^2$ 를 늘 낮추어 잡는 **편향된** 추정량이다. $n-1$ 로 나누면 이 편향이 바로잡힌다.

보정하는 값 $n-1$ 은 **자유도**를 나타낸다. $\mu$ 를 $\bar{X}$ 로 추정하느라 자유도를 하나 잃었기 때문이다.

---

## 정리하며

| 대상 | 추정량 | 불편인가? | 추정량의 분산 |
|:---:|:---:|:---:|:---:|
| $\mu$ | $\bar{X} = \frac{1}{n}\sum X_i$ | 그렇다 | $\sigma^2/n$ |
| $\sigma^2$ | $S^2 = \frac{1}{n-1}\sum(X_i - \bar{X})^2$ | 그렇다 | — |
| $\sigma^2$ | $\frac{1}{n}\sum(X_i - \bar{X})^2$ | 아니다 (낮게 편향) | — |

---

## 파이썬 구현

```python
import numpy as np

np.random.seed(42)

# 참인 모수
mu_true = 5.0
sigma_true = 2.0

# 불편성을 확인하려고 자료집합을 여러 번 만든다
N_datasets = 100_000
n = 10  # 자료집합마다의 표본 크기

sample_means = []
sample_vars_unbiased = []
sample_vars_biased = []

for _ in range(N_datasets):
    X = np.random.normal(mu_true, sigma_true, n)
    sample_means.append(np.mean(X))
    sample_vars_unbiased.append(np.var(X, ddof=1))  # n-1 로 나눈다
    sample_vars_biased.append(np.var(X, ddof=0))    # n 으로 나눈다

sample_means = np.array(sample_means)
sample_vars_unbiased = np.array(sample_vars_unbiased)
sample_vars_biased = np.array(sample_vars_biased)

print(f"True μ = {mu_true}")
print(f"E[X̄] = {np.mean(sample_means):.4f}  (should be {mu_true})")
print(f"Var(X̄) = {np.var(sample_means):.4f}  (should be {sigma_true**2/n:.4f})")
print()
print(f"True σ² = {sigma_true**2}")
print(f"E[S² (n-1)] = {np.mean(sample_vars_unbiased):.4f}  (unbiased)")
print(f"E[S² (n)]   = {np.mean(sample_vars_biased):.4f}  (biased, should be {(n-1)/n * sigma_true**2:.4f})")
```

## 연습문제

**연습문제 1.** 10명으로 이루어진 반에서 시험을 본다. 점수 $X_1, \ldots, X_{10}$ 은 평균 $\mu$ 와 분산 $\sigma^2$ 를 모르는 분포에서 뽑은 i.i.d. 표본이다. $\bar{X}$ 가 $\mu$ 의 불편추정량임을 보이고 $\text{Var}(\bar{X})$ 를 구하여라.

??? success "연습문제 1 풀이"
    선형성에 따라 다음을 얻는다.

    $$
    E[\bar{X}] = E\!\left[\frac{1}{10} \sum_{i=1}^{10} X_i\right] = \frac{1}{10} \sum_{i=1}^{10} E[X_i] = \frac{10 \mu}{10} = \mu
    $$

    그러므로 $\bar{X}$ 는 불편이다. 독립성에 따라 다음을 얻는다.

    $$
    \text{Var}(\bar{X}) = \frac{1}{100} \sum_{i=1}^{10} \text{Var}(X_i) = \frac{10 \sigma^2}{100} = \frac{\sigma^2}{10}
    $$

---

**연습문제 2.** 표본분산 공식에서 $n - 1$ 대신 $n$ 으로 나누면 편향된 추정량이 됨을 보이고 그 편향을 구하여라.

??? success "연습문제 2 풀이"
    $\tilde{S}^2 = \dfrac{1}{n} \sum_{i=1}^{n} (X_i - \bar{X})^2$ 라 하자. 평균 $\mu$, 분산 $\sigma^2$ 인 i.i.d. $X_i$ 에 대하여 항등식 $\sum (X_i - \bar{X})^2 = \sum (X_i - \mu)^2 - n(\bar{X} - \mu)^2$ 을 쓰면 다음을 얻는다.

    $$
    E\!\left[\sum_{i=1}^{n} (X_i - \bar{X})^2\right] = n \sigma^2 - n \cdot \frac{\sigma^2}{n} = (n - 1) \sigma^2
    $$

    그러므로 다음과 같다.

    $$
    E[\tilde{S}^2] = \frac{(n - 1) \sigma^2}{n} = \sigma^2 - \frac{\sigma^2}{n}
    $$

    편향은 다음과 같다.

    $$
    E[\tilde{S}^2] - \sigma^2 = -\frac{\sigma^2}{n}
    $$

    곧 늘 낮추어 잡는다. 분모를 $n - 1$ 로 하면 이 편향이 정확히 바로잡혀 흔히 쓰는 불편 표본분산 $S^2$ 를 얻는다.
