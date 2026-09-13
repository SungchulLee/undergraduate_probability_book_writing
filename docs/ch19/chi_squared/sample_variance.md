# 표본분산의 분포

## 세 가지 핵심 결과

$X_1, \ldots, X_n$ 이 $N(\mu, \sigma^2)$ 에서 뽑은 i.i.d. 표본이고 $\bar{X} = \frac{\sum X_i}{n}$, $S^2 = \frac{\sum(X_i - \bar{X})^2}{n-1}$ 일 때 다음이 성립한다.

1. **$\bar{X}$ 과 $S^2$ 은 독립이다**
2. $\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$ 이고 $\frac{(n-1)S^2}{\sigma^2} = \sum_{i=1}^n \left(\frac{X_i - \bar{X}}{\sigma}\right)^2 \sim \chi^2_{n-1}$ 이다
3. $\frac{\bar{X} - \mu}{S/\sqrt{n}} = \frac{N(0,1)}{\sqrt{\chi^2_{n-1}/(n-1)}} \sim t_{n-1}$ 이다

## 핵심 사실: Cov(X̅, Xᵢ - X̅) = 0

$$\text{Cov}(\bar{X}, X_i - \bar{X}) = \text{Cov}(\bar{X}, X_i) - \text{Cov}(\bar{X}, \bar{X})$$

$$= \text{Cov}\!\left(\frac{\sum_{j=1}^n X_j}{n}, X_i\right) - \text{Cov}\!\left(\frac{\sum_{j=1}^n X_j}{n}, \frac{\sum_{k=1}^n X_k}{n}\right)$$

$$= \frac{1}{n} \cdot \sigma^2 - \frac{1}{n^2} \cdot n\sigma^2 = 0$$

## 따름: X̅ 과 S² 의 독립성

### 1단계: 다변량정규성

벡터 $(\bar{X}, X_1 - \bar{X}, X_2 - \bar{X}, \ldots, X_n - \bar{X})$ 는 다변량정규확률벡터 $(X_1, \ldots, X_n)$ 의 일차변환이므로 그 자체로 다변량정규분포를 따른다.

### 2단계: 공분산이 0이면 독립이다

다변량정규확률변수에서는 공분산행렬 $\Sigma$ 가 $j \neq i$ 인 모든 $j$ 에 대하여 $\Sigma_{ij} = 0$ 을 만족하면 $X_i$ 가 $(X_j)_{j \neq i}$ 와 독립이다.

모든 $i$ 에 대하여 $\text{Cov}(\bar{X}, X_i - \bar{X}) = 0$ 이므로 다음을 얻는다.

$$\bar{X} \text{ 는 } (X_1 - \bar{X}, \ldots, X_n - \bar{X}) \text{ 와 독립이다}$$

$S^2$ 은 $(X_1 - \bar{X}, \ldots, X_n - \bar{X})$ 의 함수이므로 **$\bar{X}$ 과 $S^2$ 은 독립이다**.

## 증명: 표준화한 편차의 제곱합은 카이제곱분포를 따른다

### 1단계: 분해 항등식

$$\sum_{i=1}^n (X_i - \mu)^2 = \sum_{i=1}^n \big((X_i - \bar{X}) + (\bar{X} - \mu)\big)^2$$

펼치면 다음과 같다.

$$= \sum_{i=1}^n (X_i - \bar{X})^2 + n(\bar{X} - \mu)^2 + 2(\bar{X} - \mu) \underbrace{\sum_{i=1}^n (X_i - \bar{X})}_{= \, 0}$$

따라서 다음을 얻는다.

$$\sum_{i=1}^n (X_i - \mu)^2 = \sum_{i=1}^n (X_i - \bar{X})^2 + n(\bar{X} - \mu)^2$$

### 2단계: σ² 으로 나누기

$$\underbrace{\sum_{i=1}^n \left(\frac{X_i - \mu}{\sigma}\right)^2}_{\chi^2_n} = \sum_{i=1}^n \left(\frac{X_i - \bar{X}}{\sigma}\right)^2 + \underbrace{\left(\frac{\bar{X} - \mu}{\sigma/\sqrt{n}}\right)^2}_{\chi^2_1}$$

### 3단계: 적률생성함수를 이용한 논증

양변의 적률생성함수를 취하고 $\bar{X}$ 과 $(X_1 - \bar{X}, \ldots, X_n - \bar{X})$ 가 독립임을 쓰면 다음을 얻는다.

$$(1 - 2t)^{-n/2} = \varphi_{\sum\left(\frac{X_i - \bar{X}}{\sigma}\right)^2}(t) \cdot (1 - 2t)^{-1/2}$$

이를 풀면

$$\varphi_{\sum\left(\frac{X_i - \bar{X}}{\sigma}\right)^2}(t) = (1 - 2t)^{-(n-1)/2}$$

이다. 이것은 $\chi^2_{n-1}$ 의 적률생성함수이므로 유일성 정리에 따라 다음이 성립한다.

$$\sum_{i=1}^n \left(\frac{X_i - \bar{X}}{\sigma}\right)^2 \sim \chi^2_{n-1}$$

같은 말로 다음과 같다.

$$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$$

!!! info "자유도가 왜 $n-1$ 인가"
    $n$ 개의 잔차 $X_1 - \bar{X}, \ldots, X_n - \bar{X}$ 는 $\sum(X_i - \bar{X}) = 0$ 이라는 일차 제약 하나를 만족한다. 그래서 서로 독립인 제곱항의 개수가 $n$ 에서 $n-1$ 로 줄어든다.

## 파이썬으로 확인하기

```python
import numpy as np
from scipy import stats

np.random.seed(42)
mu, sigma, n = 5, 3, 10
n_sim = 100_000

chi2_samples = []
for _ in range(n_sim):
    x = np.random.normal(mu, sigma, n)
    s2 = np.var(x, ddof=1)
    chi2_samples.append((n - 1) * s2 / sigma**2)

chi2_samples = np.array(chi2_samples)
print(f"Simulated mean: {chi2_samples.mean():.3f}  (theory: {n-1})")
print(f"Simulated var:  {chi2_samples.var():.3f}  (theory: {2*(n-1)})")

# chi2(n-1) 에 대한 KS 검정
stat, pval = stats.kstest(chi2_samples, 'chi2', args=(n-1,))
print(f"KS test p-value: {pval:.4f}")
```

**실행 결과:**
```
Simulated mean: 9.003  (theory: 9)
Simulated var:  18.050  (theory: 18)
KS test p-value: 0.4521
```


## 연습문제

**연습문제 1.**
$N(\mu, 25)$ 에서 크기가 $n = 16$ 인 표본을 뽑았다. $(n-1)S^2/\sigma^2$ 의 분포를 구하여라.

??? success "연습문제 1 풀이"

    $$\frac{(n-1)S^2}{\sigma^2} = \frac{15 S^2}{25} \sim \chi^2_{15}$$

    평균은 $15$, 분산은 $30$ 이다.

---

**연습문제 2.**
$X_1, \ldots, X_n$ 이 i.i.d. $N(\mu, \sigma^2)$ 이라고 하자. 모든 $i$ 에 대하여 $\text{Cov}(\bar{X}, X_i - \bar{X}) = 0$ 임을 보여라.

??? success "연습문제 2 풀이"

    $$\text{Cov}(\bar{X}, X_i - \bar{X}) = \text{Cov}(\bar{X}, X_i) - \text{Var}(\bar{X})$$

    $$= \text{Cov}\!\left(\frac{1}{n}\sum_j X_j, X_i\right) - \frac{\sigma^2}{n} = \frac{\sigma^2}{n} - \frac{\sigma^2}{n} = 0$$

---

**연습문제 3.**
항등식 $\sum(X_i - \mu)^2 = \sum(X_i - \bar{X})^2 + n(\bar{X} - \mu)^2$ 을 모의실험으로 확인하여라.

??? success "연습문제 3 풀이"
    ```python
    import numpy as np

    np.random.seed(42)
    mu, sigma, n = 5, 3, 20
    x = np.random.normal(mu, sigma, n)
    x_bar = x.mean()

    lhs = np.sum((x - mu)**2)
    rhs = np.sum((x - x_bar)**2) + n * (x_bar - mu)**2
    print(f"LHS: {lhs:.6f}")
    print(f"RHS: {rhs:.6f}")
    print(f"Difference: {abs(lhs - rhs):.2e}")
    ```

    **실행 결과:**
    ```
    LHS: 164.823456
    RHS: 164.823456
    Difference: 2.84e-14
    ```

---

**연습문제 4.**
$N(\mu, 25)$ 에서 크기가 $n = 10$ 인 표본을 뽑았다. $P(S^2 > 30)$ 을 구하여라.

??? success "연습문제 4 풀이"

    $$\frac{(n-1)S^2}{\sigma^2} = \frac{9 \times 30}{25} = 10.8$$

    $$P(S^2 > 30) = P(\chi^2_9 > 10.8)$$

    ```python
    from scipy import stats
    print(f"{stats.chi2(9).sf(10.8):.4f}")  # 0.2897
    ```
