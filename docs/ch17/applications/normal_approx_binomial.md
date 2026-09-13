# 이항분포의 정규근사

## 문제 설정

$X \sim B(n, p)$ 라 하자. i.i.d. 인 $X_i \sim \text{Bernoulli}(p)$ 에 대하여 $X = \sum_{i=1}^n X_i$ 이므로 중심극한정리에 따라 다음이 성립한다.

$$\frac{X - np}{\sqrt{np(1-p)}} \xrightarrow{d} N(0,1) \quad n \to \infty \text{ 일 때}$$

$n$ 이 크면 다음과 같다.

$$X \approx N(np, \, np(1-p))$$

## 언제 쓰는가

이항분포의 정규근사는 $np$ 와 $n(1-p)$ 가 둘 다 적어도 5~10은 될 때 쓸 만하다.

!!! tip "푸아송 근사와 견주어 보기"

    - **푸아송 근사**: $n$ 이 크고 $p$ 가 작으며 $np = \lambda$ 가 중간 정도 → $B(n,p) \approx \text{Po}(\lambda)$
    - **정규근사**: $n$ 이 크고 $p$ 가 지나치게 치우치지 않음 → $B(n,p) \approx N(np, np(1-p))$

## 예: 심리학 강의 수강 신청

어떤 심리학 강의에 수강 신청을 하는 학생 수가 평균이 $100$ 인 푸아송확률변수라고 하자. $120$ 명 이상이 신청하면 교수는 분반을 두 개 연다. 분반을 두 개 열게 될 확률은 얼마인가?

**정확한 값(푸아송):**

$$P(X \geq 120) = \sum_{k=120}^{\infty} \frac{100^k}{k!} e^{-100} = 0.0282$$

**연속성 보정을 한 정규근사:**

i.i.d. 인 $Y_i \sim \text{Po}(1)$ 에 대하여 $X \sim \text{Po}(100)$ 을 $X = \sum_{i=1}^{100} Y_i$ 로 적을 수 있으므로 $\mu = 100$, $\sigma^2 = 100$ 이다.

$$P(X \geq 120) = P(X \geq 119.5) = P\left(\frac{X - 100}{\sqrt{100}} \geq \frac{119.5 - 100}{\sqrt{100}}\right)$$

$$\approx 1 - \mathcal{N}(1.95) = 1 - 0.9744 = 0.0256$$

근사값 $0.0256$ 이 정확한 값 $0.0282$ 에 가깝다.

## 파이썬 구현

```python
import numpy as np
from scipy import stats

# 정확한 푸아송 값
lam = 100
exact = 1 - stats.poisson.cdf(119, lam)
print(f"Exact (Poisson): {exact:.4f}")

# 연속성 보정을 한 정규근사
z = (119.5 - 100) / np.sqrt(100)
approx = 1 - stats.norm.cdf(z)
print(f"Normal approx (with CC): {approx:.4f}")

# 연속성 보정을 하지 않은 정규근사
z_no_cc = (120 - 100) / np.sqrt(100)
approx_no_cc = 1 - stats.norm.cdf(z_no_cc)
print(f"Normal approx (without CC): {approx_no_cc:.4f}")
```

**실행 결과:**
```
Exact (Poisson): 0.0282
Normal approx (with CC): 0.0256
Normal approx (without CC): 0.0228
```

## 연습문제

**연습문제 1.**
어떤 보험 회사에 $10{,}000$ 명의 가입자가 있다. 각 가입자는 한 해 동안 서로 독립으로 확률 $0.05$ 로 보험금을 청구한다. 중심극한정리를 써서 이 회사가 $550$ 건보다 많은 청구를 받을 확률을 어림하여라.

---

**연습문제 2.**
$X \sim B(200, 0.4)$ 라 하자. (연속성 보정을 한) 정규근사를 써서 다음을 구하여라.

(a) $P(X \leq 75)$

(b) $P(X = 80)$

(c) $P(70 \leq X \leq 90)$

---

**연습문제 3.**
어떤 공장이 만드는 제품의 불량률이 $2\%$ 이다. 제품 $1{,}000$ 개를 한 묶음으로 할 때, 중심극한정리를 써서 불량품이 $15$ 개 이상 $30$ 개 이하일 확률을 어림하여라.
