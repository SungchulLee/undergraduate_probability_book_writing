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

## 예: 동전 100번 던지기

공정한 동전을 $100$ 번 던진다. 앞면이 $60$ 번 이상 나올 확률은 얼마인가? 앞면의 횟수를 $X$ 라 하면 $X \sim B(100, 0.5)$ 이다.

**정확한 값(이항분포):**

$$P(X \geq 60) = \sum_{k=60}^{100} \binom{100}{k} \left(\tfrac{1}{2}\right)^{100} = 0.0284$$

**연속성 보정을 한 정규근사:**

$np = 50 \geq 10$ 이고 $n(1-p) = 50 \geq 10$ 이므로 정규근사를 쓸 수 있다. $\mu = np = 50$, $\sigma = \sqrt{np(1-p)} = 5$ 이다.

$$P(X \geq 60) = P(X \geq 59.5) = P\left(\frac{X - 50}{5} \geq \frac{59.5 - 50}{5}\right)$$

$$\approx 1 - \mathcal{N}(1.90) = 1 - 0.9713 = 0.0287$$

근사값 $0.0287$ 이 정확한 값 $0.0284$ 에 매우 가깝다. 연속성 보정을 하지 않으면 $1 - \mathcal{N}(2.00) = 0.0228$ 이 되어 훨씬 어긋난다. 이산확률변수를 연속분포로 어림할 때 보정이 왜 필요한지 잘 보여 주는 대목이다.

## 파이썬 구현

```python
import numpy as np
from scipy import stats

# 정확한 이항분포 값
n, p = 100, 0.5
exact = 1 - stats.binom.cdf(59, n, p)
print(f"Exact (Binomial): {exact:.4f}")

mu = n * p
sigma = np.sqrt(n * p * (1 - p))

# 연속성 보정을 한 정규근사
z = (59.5 - mu) / sigma
approx = 1 - stats.norm.cdf(z)
print(f"Normal approx (with CC): {approx:.4f}")

# 연속성 보정을 하지 않은 정규근사
z_no_cc = (60 - mu) / sigma
approx_no_cc = 1 - stats.norm.cdf(z_no_cc)
print(f"Normal approx (without CC): {approx_no_cc:.4f}")
```

**실행 결과:**
```
Exact (Binomial): 0.0284
Normal approx (with CC): 0.0287
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
