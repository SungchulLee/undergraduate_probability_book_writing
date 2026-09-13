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
