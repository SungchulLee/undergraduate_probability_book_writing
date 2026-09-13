# 신뢰구간 미리보기

## 중심극한정리에서 신뢰구간으로

중심극한정리는 다음을 말해 준다.

$$\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \approx N(0, 1)$$

이는 다음을 뜻한다.

$$P\left(-z_{\alpha/2} \leq \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \leq z_{\alpha/2}\right) \approx 1 - \alpha$$

$\mu$ 에 대하여 정리하면 다음과 같다.

$$P\left(\bar{X}_n - z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \leq \mu \leq \bar{X}_n + z_{\alpha/2} \frac{\sigma}{\sqrt{n}}\right) \approx 1 - \alpha$$

이것이 $\mu$ 에 대한 **$(1-\alpha)$ 신뢰구간**이다.

$$\bar{X}_n \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$

**95% 신뢰구간**이면 $\alpha = 0.05$ 이므로 $z_{\alpha/2} = z_{0.025} = 1.96$ 이고 다음과 같다.

$$\bar{X}_n \pm 1.96 \frac{\sigma}{\sqrt{n}}$$

## 예: 천체까지의 거리 재기

어떤 천문학자가 별까지의 거리를 잰다. 측정값은 i.i.d. 이고 참평균이 $d$ (실제 거리), 분산이 $\sigma^2 = 4$ 광년$^2$ 이다. 표본평균이 95% 신뢰수준으로 $d$ 에서 $\pm 0.5$ 광년 안에 들어오게 하려면 몇 번이나 재야 하는가?

중심극한정리에 따라 다음이 성립한다.

$$\bar{X}_n \approx N\left(d, \frac{4}{n}\right)$$

다음을 만족해야 한다.

$$|\bar{X}_n - d| \leq 1.96 \sqrt{\frac{4}{n}} \leq 0.5 \quad \text{95\% 신뢰수준으로}$$

풀면 다음을 얻는다.

$$1.96 \cdot \frac{2}{\sqrt{n}} \leq 0.5 \implies \sqrt{n} \geq \frac{1.96 \times 2}{0.5} = 7.84 \implies n \geq 61.47$$

곧 **적어도 62번** 재야 한다.

## 표본크기에 대한 일반 공식

신뢰수준 $1 - \alpha$ 에서 오차한계 $\varepsilon$ 을 얻으려면 다음이어야 한다.

$$n \geq \left(\frac{z_{\alpha/2} \cdot \sigma}{\varepsilon}\right)^2$$

| 신뢰수준 | $z_{\alpha/2}$ |
|-----------------|----------------|
| 90% | 1.645 |
| 95% | 1.960 |
| 99% | 2.576 |

## 파이썬 구현

```python
import numpy as np
from scipy import stats

# 천문학자 예제
sigma = 2       # 표준편차
epsilon = 0.5   # 바라는 오차한계
alpha = 0.05    # 유의수준

z = stats.norm.ppf(1 - alpha / 2)
n_min = (z * sigma / epsilon) ** 2
print(f"z_{alpha/2:.3f} = {z:.4f}")
print(f"Minimum n = ({z:.2f} × {sigma} / {epsilon})² = {n_min:.4f}")
print(f"Need at least {int(np.ceil(n_min))} measurements")
```

**실행 결과:**
```
z_0.025 = 1.9600
Minimum n = (1.96 × 2 / 0.5)² = 61.4656
Need at least 62 measurements
```

!!! note "미리보기"
    이것은 신뢰구간을 **미리 맛보는** 것이다. $\sigma$ 를 모르고 자료에서 추정해야 하면 정규분포 대신 **스튜던트 t분포**(19장)를 쓰며, 그러면 $n$ 이 작을 때 구간이 더 넓어진다.

## 연습문제

**연습문제 1.**
어떤 연구자가 재는 양의 측정값이 i.i.d. 이고 평균 $\mu$ 는 모르지만 표준편차가 $\sigma = 10$ 임은 알고 있다. 표본평균이 $\mu$ 에서 $\pm 2$ 안에 들어오게 하려면 다음 각 신뢰수준에서 몇 번이나 재야 하는가?

(a) 90% 신뢰수준

(b) 95% 신뢰수준

(c) 99% 신뢰수준

---

**연습문제 2.**
어떤 여론조사 기관이 특정 후보를 지지하는 유권자의 비율 $p$ 를 추정하려 한다. 응답 하나하나를 베르누이($p$) 분포로 본다. (분산이 가장 큰 최악의 경우인) $p \approx 0.5$ 를 써서, 표본비율이 95% 신뢰수준으로 $p$ 에서 $\pm 0.03$ 안에 들어오려면 몇 명이나 조사해야 하는가?
