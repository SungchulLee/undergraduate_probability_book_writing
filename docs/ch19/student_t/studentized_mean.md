# 스튜던트화한 표본평균의 분포

## 왜 필요한가

$\sigma$ 를 아는 경우에는 $\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0,1)$ 이 $\mu$ 에 대한 추론에 쓸 수 있는 정확한 피벗이 되어 준다.

$\sigma$ 를 **모르는** 경우에는 그 자리에 $S$ 를 넣어 **스튜던트화한 표본평균**을 얻는다.

$$T = \frac{\bar{X} - \mu}{S / \sqrt{n}}$$

## 유도

### 1단계: 비의 꼴로 고쳐 쓰기

$$T = \frac{\bar{X} - \mu}{S/\sqrt{n}} = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \cdot \frac{\sigma}{S} = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \bigg/ \frac{S}{\sigma}$$

### 2단계: 각 부분 알아보기

분자는 다음과 같다.

$$\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$$

분모에는 표본분산이 들어 있다. $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$ 이므로 다음과 같다.

$$\frac{S}{\sigma} = \sqrt{\frac{S^2}{\sigma^2}} = \sqrt{\frac{(n-1)S^2/\sigma^2}{n-1}} = \sqrt{\frac{\chi^2_{n-1}}{n-1}}$$

### 3단계: 독립성 쓰기

19.2절의 핵심 사실에 따라 $\bar{X}$ 과 $S^2$ 은 독립이다. 따라서 분자의 $N(0,1)$ 과 분모의 $\sqrt{\chi^2_{n-1}/(n-1)}$ 도 독립이다.

### 4단계: 결론

$$T = \frac{\bar{X} - \mu}{S/\sqrt{n}} = \frac{N(0,1)}{\sqrt{\chi^2_{n-1}/(n-1)}} \sim t_{n-1}$$

## 정리하며

$$\boxed{\frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t_{n-1}}$$

이 결과가 다음의 바탕이 된다.

- $\mu$ 에 대한 **$t$ 신뢰구간**: $\bar{X} \pm t_{\alpha/2, \, n-1} \cdot \frac{S}{\sqrt{n}}$
- $H_0: \mu = \mu_0$ 에 대한 **일표본 $t$ 검정**
- 두 평균을 견주는 **이표본 $t$ 검정**

## 파이썬으로 확인하기

```python
import numpy as np
from scipy import stats

np.random.seed(42)
mu, sigma, n = 10, 3, 8
n_sim = 100_000

t_samples = []
for _ in range(n_sim):
    x = np.random.normal(mu, sigma, n)
    x_bar = x.mean()
    s = x.std(ddof=1)
    t_samples.append((x_bar - mu) / (s / np.sqrt(n)))

t_samples = np.array(t_samples)

print(f"Simulated mean: {t_samples.mean():.4f}  (theory: 0)")
print(f"Simulated var:  {t_samples.var():.4f}  (theory: {(n-1)/(n-3):.4f})")

# t(n-1) 에 대한 KS 검정
stat, pval = stats.kstest(t_samples, 't', args=(n-1,))
print(f"KS test p-value: {pval:.4f}")
```

**실행 결과:**
```
Simulated mean: 0.0011  (theory: 0)
Simulated var:  1.3991  (theory: 1.4000)
KS test p-value: 0.5123
```

## 연습문제

**연습문제 1.**
$N(50, \sigma^2)$ 에서 뽑은 크기 $n = 9$ 인 표본에서 $\bar{x} = 53$, $s = 6$ 을 얻었다. $\mu = 50$ 이라는 가정 아래에서 $P(\bar{X} \geq 53)$ 을 구하여라.

??? success "연습문제 1 풀이"

    $$T = \frac{53 - 50}{6/\sqrt{9}} = \frac{3}{2} = 1.5$$

    이므로 $P(\bar{X} \geq 53) = P(t_8 \geq 1.5)$ 이다.

    ```python
    from scipy import stats
    print(f"{stats.t(8).sf(1.5):.4f}")  # 0.0856
    ```
