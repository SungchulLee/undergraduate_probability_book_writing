# 푸아송 근사를 언제 쓰는가

## 세 가지 조건

이항분포에 대한 푸아송 근사는 다음과 같을 때 알맞다.

| 조건 | 뜻 |
|:---|:---|
| $n$ 이 **크다** | 시행 횟수가 많다(대체로 $n \geq 20$) |
| $p$ 가 **작다** | 시행마다 성공할 확률이 낮다(대체로 $p \leq 0.05$) |
| $\lambda = np$ 가 **알맞다** | 기대되는 개수가 너무 작지도 너무 크지도 않다 |

한마디로 하면 **시행이 많고, 저마다 성공확률이 작으며, 기대되는 성공 횟수가 알맞은 크기**일 때이다.

---

## 어림잡는 기준

널리 쓰이는 지침은 다음과 같다.

!!! tip "어림잡는 기준"
    다음과 같을 때 푸아송 근사 $B(n, p) \approx \text{Po}(\lambda)$ 를 쓴다.

    - $n \geq 20$ 이고 $p \leq 0.05$ 이거나, 더 조심스럽게는
    - $n \geq 100$ 이고 $np \leq 10$

    $\lambda = np$ 를 고정한 채 $n$ 이 커지고 $p$ 가 작아질수록 근사는 좋아진다.

---

## 오차 경계

$A_1, A_2, \ldots, A_n$ 이 확률 $p_i = P(A_i)$ 가 서로 다를 수도 있는 독립인 사건이고 $X = \sum_{i=1}^{n} \mathbf{1}_{A_i}$ 인 일반적인 경우에, **르캉 경계**는 다음을 준다.

$$
\left| P(X \in A) - P(Y \in A) \right| \leq \sum_{i=1}^{n} p_i^2 \leq \left(\max_{1 \leq i \leq n} p_i\right) \cdot \lambda
$$

여기서 $Y \sim \text{Po}(\lambda)$ 이고 $\lambda = \sum_{i=1}^{n} p_i$ 이다.

모든 $p_i = p$ 일 때는 이것이 다음과 같이 간단해진다.

$$
\text{오차} \leq np^2 = p\lambda
$$

그러므로 오차는 $p \cdot \lambda$ 로 조절된다. $p$ 가 작고 $\lambda$ 가 알맞은 크기라면 좋은 근사가 보장된다.

---

## 그냥 이항분포를 쓰면 안 되는가

$n$ 이 그리 크지 않다면 이항확률을 직접 계산해도 된다. 그렇지만 다음과 같은 상황에서는 푸아송 근사가 쓸모 있다.

1. **계산이 간단하다**: $\frac{e^{-\lambda}\lambda^k}{k!}$ 를 쓰면 $n$ 이 클 때 큰 계승이 들어가는 $\binom{n}{k}$ 를 계산하지 않아도 된다.

2. **$n$ 을 모른다**: 여러 응용에서(예를 들어 일정 기간에 일어나는 드문 사건을 모형으로 삼을 때) $n$ 이 뚜렷하게 정해지지 않는다. 이럴 때 비율 $\lambda$ 를 갖는 푸아송 모형이 자연스러운 출발점이 된다.

3. **확률이 시행마다 다르다**: $p_i$ 가 시행마다 다르면 그 합은 정확히 이항분포가 아니지만, 푸아송분포로는 여전히 잘 근사된다.

4. **이론이 아름답다**: 푸아송분포는 더 좋은 수학적 성질을 갖는다(독립인 푸아송확률변수의 가법성, 푸아송 과정과의 이어짐 등).

---

## 흔히 쓰이는 곳

정해진 범위 안에서 일어나는 "드문 사건"의 개수를 셀 때면 언제나 푸아송분포가 자연스러운 모형이 된다.

- **보험**: 한 달에 접수되는 청구 건수
- **금융**: 대출 포트폴리오에서 일어나는 부도 건수
- **통신**: 콜센터에 1분 동안 걸려 오는 전화 건수
- **생물학**: DNA 가닥에 생긴 돌연변이의 개수
- **제조**: 제품 한 단위에 있는 결함의 개수
- **교통**: 한 교차로에서 한 해 동안 일어나는 사고 건수
- **역학**: 한 지역에서 발생한 질병 사례의 수

---

## 진단: 근사가 나빠지는 때는 언제인가

다음과 같을 때 근사가 무너진다.

- $p$ 가 작지 않을 때(예: $p = 0.3$): 이항분포의 치우친 정도가 푸아송분포와 눈에 띄게 달라진다
- $n$ 이 작을 때: 극한이 힘을 쓸 만큼 시행이 많지 않다
- $\lambda = np$ 가 아주 클 때: 중심극한정리에 따라 이항분포와 푸아송분포 모두 정규분포로 잘 근사되므로 푸아송분포를 쓸 이유가 별로 없다

```python
import numpy as np
from scipy.stats import binom, poisson

def approximation_quality(n, p):
    """B(n,p)에 대한 푸아송 근사의 품질을 살펴본다."""
    la = n * p
    k_max = min(n, int(la + 5 * np.sqrt(la)) + 1)
    k = np.arange(0, k_max + 1)

    binom_pmf = binom.pmf(k, n, p)
    poisson_pmf = poisson.pmf(k, la)

    max_diff = np.max(np.abs(binom_pmf - poisson_pmf))
    total_variation = 0.5 * np.sum(np.abs(binom_pmf - poisson_pmf))

    print(f"B({n}, {p}) vs Po({la})")
    print(f"  Max PMF difference:   {max_diff:.6e}")
    print(f"  Total variation dist: {total_variation:.6e}")
    print(f"  Le Cam bound (p·λ):   {p * la:.6e}")
    print()

# 근사가 좋은 경우
approximation_quality(1000, 0.01)   # n이 크고 p가 작다
approximation_quality(2000, 0.005)  # n이 매우 크고 p가 매우 작다

# 근사가 그저 그런 경우
approximation_quality(100, 0.05)    # n도 p도 어중간하다
approximation_quality(50, 0.1)      # n은 어중간하고 p가 그리 작지 않다

# 근사가 나쁜 경우
approximation_quality(20, 0.3)      # p가 너무 크다
approximation_quality(10, 0.5)      # p가 지나치게 크다
```


## 연습문제

**연습문제 1.**
지난해 뉴욕에서 약 80,000쌍이 결혼하였다.

**(a)** 푸아송 근사를 써서 생일이 같은 부부가 250쌍보다 많을 확률을 어림하여라.

**(b)** 이항분포로 정확한 확률을 계산하여 견주어 보아라.

**(c)** 이 문제에서 $\lambda$ 는 얼마인가? $S_n$ 을 생일이 같은 부부의 쌍의 수라 할 때 $E[S_n]$ 과 $\text{SD}(S_n)$ 을 계산하여라.

??? success "연습문제 1 풀이"

    **(a)** $n = 80{,}000$, $p = 1/365$, $\lambda = np = 80000/365 \approx 219.18$ 이다.

    ```python
    from scipy.stats import poisson, binom

    n = 80_000
    p = 1 / 365
    la = n * p

    poisson_prob = 1 - poisson.cdf(250, la)
    print(f"P(X > 250) ≈ {poisson_prob:.4f}  (Poisson)")
    ```

    $P(X > 250) \approx 0.0188$ 이다.

    **(b)**

    ```python
    binom_prob = 1 - binom.cdf(250, n, p)
    print(f"P(S > 250) = {binom_prob:.4f}  (Binomial exact)")
    ```

    $P(S_n > 250) = 0.0187$ 이다. 푸아송 근사가 아주 훌륭하다.

    **(c)** $\lambda = 80000/365 \approx 219.18$ 이다. 따라서 $E[S_n] = \lambda \approx 219.18$ 이고 $\text{SD}(S_n) \approx \sqrt{219.18} \approx 14.81$ 이다.

---

**연습문제 2.**
어떤 자동차 회사는 출고 전에 차량을 검사한다. 차량 한 대마다 일어날 수 있는 결함 $n = 500$ 가지를 살피는데, 각 결함은 서로 독립으로 확률 $p = 0.001$ 로 일어난다.

**(a)** 차량 한 대에서 기대되는 결함의 개수는 얼마인가?

**(b)** 결함이 하나도 없을 확률은 얼마인가?

**(c)** 한 대에서 결함이 3개보다 많이 나올 확률은 얼마인가?

**(d)** 이 공장은 하루에 200대를 출고한다. 가법성을 써서 하루에 발견되는 전체 결함 개수의 기댓값과 그 분포를 구하여라.

??? success "연습문제 2 풀이"

    **(a)** $\lambda = np = 500 \times 0.001 = 0.5$ 이다.

    **(b)** $P(X = 0) = e^{-0.5} \approx 0.6065$ 이다.

    **(c)**

    ```python
    from scipy.stats import poisson
    la = 0.5
    print(f"P(X > 3) = {1 - poisson.cdf(3, la):.6f}")
    ```

    $P(X > 3) \approx 0.0018$ 이다.

    **(d)** 차량 한 대의 결함 개수는 $\sim \text{Po}(0.5)$ 이다. 독립인 차량 200대에 대해서는 전체 결함 개수가 $\sim \text{Po}(200 \times 0.5) = \text{Po}(100)$ 이다. 따라서 하루에 기대되는 전체 결함은 100개이다.
