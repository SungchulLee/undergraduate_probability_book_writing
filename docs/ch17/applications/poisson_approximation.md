# 푸아송 확률의 근사

## 푸아송분포에 중심극한정리를 쓸 수 있는 까닭

$X \sim \text{Po}(\lambda)$ 이면 $X$ 를 i.i.d. 푸아송확률변수의 합으로 쪼갤 수 있다.

$$X = \sum_{i=1}^{\lambda} Y_i, \qquad Y_i \sim \text{Po}(1) \text{ iid}$$

($\lambda$ 가 양의 정수일 때이다.) $E[Y_i] = 1$ 이고 $\text{Var}(Y_i) = 1$ 이므로 중심극한정리에 따라 다음이 성립한다.

$$\frac{X - \lambda}{\sqrt{\lambda}} \xrightarrow{d} N(0,1) \quad \lambda \to \infty \text{ 일 때}$$

$\lambda$ 가 크면 다음과 같다.

$$X \approx N(\lambda, \lambda)$$

## 근사의 사슬

$n$ 이 크고 $p$ 가 작은 i.i.d. 베르누이 시행의 합에 대하여 다음이 성립한다.

$$B(n, p) \approx \text{Po}(np) \approx N(np, np)$$

- 첫 번째 근사(푸아송)는 $p$ 가 작을수록 좋다.
- 두 번째 근사(정규)는 $\lambda = np$ 가 클수록 좋다.

## 예

$X \sim \text{Po}(100)$ 이라 하고 $P(X \geq 120)$ 을 구해 보자.

**연속성 보정을 한 중심극한정리를 쓰면:**

$$P(X \geq 120) = P(X \geq 119.5) = P\left(Z \geq \frac{119.5 - 100}{\sqrt{100}}\right) = P(Z \geq 1.95)$$

$$= 1 - \mathcal{N}(1.95) = 0.0256$$

## 파이썬 구현

```python
import numpy as np
from scipy import stats

lambdas = [10, 25, 50, 100, 200]

for lam in lambdas:
    # 정확한 값: P(X >= lam + 2*sqrt(lam))
    threshold = int(lam + 2 * np.sqrt(lam))
    exact = 1 - stats.poisson.cdf(threshold - 1, lam)

    # 연속성 보정을 한 정규근사
    z = (threshold - 0.5 - lam) / np.sqrt(lam)
    approx = 1 - stats.norm.cdf(z)

    print(f"λ={lam:>3d}, threshold={threshold:>3d}: "
          f"Exact={exact:.4f}, Normal≈{approx:.4f}")
```

**실행 결과:**
```
λ= 10, threshold= 16: Exact=0.0487, Normal≈0.0418
λ= 25, threshold= 35: Exact=0.0297, Normal≈0.0287
λ= 50, threshold= 64: Exact=0.0302, Normal≈0.0294
λ=100, threshold=120: Exact=0.0282, Normal≈0.0256
λ=200, threshold=228: Exact=0.0281, Normal≈0.0274
```

$\lambda$ 가 커질수록 정규근사가 좋아진다.

## 연습문제

**연습문제 1.**
어떤 가게에 한 시간 동안 오는 손님의 수가 평균 $20$ 인 푸아송분포를 따른다. 중심극한정리를 써서 영업시간이 $10$ 시간인 하루에 손님이 $220$ 명보다 많이 올 확률을 어림하여라.

??? success "연습문제 1 풀이"
    **1단계: 하루 전체의 분포.** $i$ 번째 시간에 오는 손님 수를 $Y_i$ 라 하면 $Y_i \sim \text{Po}(20)$ 이고 서로 독립이다. 독립인 푸아송확률변수의 합은 다시 푸아송분포를 따르며 모수가 더해진다.

    $$
    X = \sum_{i=1}^{10} Y_i \sim \text{Po}(10 \times 20) = \text{Po}(200)
    $$

    적률생성함수로 확인해 보면 $M_{Y_i}(t) = e^{20(e^t - 1)}$ 이므로 다음과 같다.

    $$
    M_X(t) = \left(e^{20(e^t-1)}\right)^{10} = e^{200(e^t - 1)}
    $$

    이것이 $\text{Po}(200)$ 의 적률생성함수이다.

    **2단계: 평균과 표준편차.** 푸아송분포는 평균과 분산이 같다.

    $$
    \mu = \lambda = 200, \qquad \sigma = \sqrt{\lambda} = \sqrt{200} \approx 14.1421
    $$

    $\lambda = 200$ 이 충분히 크므로 정규근사 $X \approx N(200, 200)$ 을 쓸 수 있다.

    **3단계: 연속성 보정.** $X$ 가 정수값을 가지므로 $\{X > 220\}$ 은 $\{X \ge 221\}$ 과 같은 사건이고, 경계는 $220$ 과 $221$ 의 한가운데인 $220.5$ 이다.

    $$
    P(X > 220) = P(X \ge 221) \approx P(X \ge 220.5)
    $$

    **4단계: 표준화하고 값을 읽는다.**

    $$
    z = \frac{220.5 - 200}{14.1421} \approx 1.4496
    $$

    $$
    P(X > 220) \approx 1 - \mathcal{N}(1.4496) = 1 - 0.9264 = 0.0736
    $$

    **5단계: 정확한 값과 견주기.** 푸아송분포로 곧바로 계산하면 다음과 같다.

    $$
    P(X > 220) = 1 - \sum_{k=0}^{220} e^{-200}\frac{200^k}{k!} = 0.0753
    $$

    | 방법 | 값 |
    |---|---|
    | 정규근사(연속성 보정) | $0.0736$ |
    | 정규근사(보정 없음, $z = 1.4142$) | $0.0787$ |
    | 정확한 푸아송분포 값 | $0.0753$ |

    보정을 한 값 $0.0736$ 과 하지 않은 값 $0.0787$ 이 정확한 값 $0.0753$ 을 양쪽에서 감싸고 있다. 두 값 모두 오차가 $0.005$ 안쪽이며, 이 정도면 "한가한 날인지 붐비는 날인지" 를 가늠하는 데 넉넉하다.

    보정을 한 쪽이 조금 작게 나오는 것은 푸아송분포의 오른쪽 꼬리가 정규분포보다 두껍기 때문이다. 왜도가 $1/\sqrt{\lambda} = 1/\sqrt{200} \approx 0.0707 > 0$ 으로 양수이므로, 정규분포는 오른쪽 꼬리확률을 조금씩 과소평가한다. 본문의 표에서 $\lambda$ 가 커질수록 정확한 값과 근사값의 차이가 줄어드는 것도 같은 이유이며, 이 왜도가 $\lambda \to \infty$ 에서 $0$ 으로 가기 때문이다.

    **뜻풀이.** 하루 평균 $200$ 명이 오는 가게에서 $220$ 명을 넘는 날은 대략 $13$ 일에 하루꼴이다. $220$ 은 평균보다 표준편차의 약 $1.45$ 배 위에 있는 값이다. $\square$
