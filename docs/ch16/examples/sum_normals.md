# 독립인 정규확률변수의 합(합성곱으로)

## 결과

!!! info "정규분포의 합성곱"
    $X \sim N(\mu_1, \sigma_1^2)$ 과 $Y \sim N(\mu_2, \sigma_2^2)$ 가 독립이면 다음이 성립한다.

    $$X + Y \sim N(\mu_1 + \mu_2, \; \sigma_1^2 + \sigma_2^2)$$

    곧 정규분포족은 **합성곱에 대하여 닫혀 있다**. 독립인 정규확률변수의 합은 다시 정규분포를 따른다.

## 적률생성함수를 쓴 증명

적률생성함수를 쓰는 방법이 가장 깔끔하다.

$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = e^{\mu_1 t + \sigma_1^2 t^2/2} \cdot e^{\mu_2 t + \sigma_2^2 t^2/2} = e^{(\mu_1+\mu_2)t + (\sigma_1^2+\sigma_2^2)t^2/2}$$

이것은 $N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$ 의 적률생성함수이다. 적률생성함수의 유일성에 따라 결론이 따라 나온다.

## 합성곱 적분을 쓴 증명

$X \sim N(0, 1)$ 과 $Y \sim N(0, 1)$ 이 독립인 경우(표준적인 경우)를 보자.

$$f_{X+Y}(a) = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-b^2/2} \cdot \frac{1}{\sqrt{2\pi}} e^{-(a-b)^2/2} \, db$$

지수에서 완전제곱을 만든 뒤 가우스적분을 계산하면 다음을 얻는다.

$$f_{X+Y}(a) = \frac{1}{\sqrt{4\pi}} e^{-a^2/4}$$

이것은 $N(0, 2)$ 의 확률밀도함수이므로 $N(0,1) + N(0,1) = N(0, 2)$ 임이 확인된다.

## 일반적인 합

$X_1, X_2, \ldots, X_n$ 이 독립이고 $X_i \sim N(\mu_i, \sigma_i^2)$ 이면 다음이 성립한다.

$$\sum_{i=1}^n X_i \sim N\!\left(\sum_{i=1}^n \mu_i, \; \sum_{i=1}^n \sigma_i^2\right)$$

특히 $X_i$ 가 i.i.d. $N(\mu, \sigma^2)$ 이면 다음을 얻는다.

$$\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i \sim N\!\left(\mu, \; \frac{\sigma^2}{n}\right)$$

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
n_sim = 100000

mu1, sig1 = 2, 1.5
mu2, sig2 = -1, 2.0

X = np.random.normal(mu1, sig1, n_sim)
Y = np.random.normal(mu2, sig2, n_sim)
S = X + Y

mu_sum = mu1 + mu2
sig_sum = np.sqrt(sig1**2 + sig2**2)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(S, bins=80, density=True, alpha=0.5, color='steelblue',
        label='Simulated X+Y')
x = np.linspace(mu_sum - 4*sig_sum, mu_sum + 4*sig_sum, 200)
ax.plot(x, stats.norm.pdf(x, mu_sum, sig_sum), 'r-', lw=2,
        label=f'N({mu_sum}, {sig_sum**2:.2f}) PDF')
ax.set_title(f'N({mu1},{sig1**2}) + N({mu2},{sig2**2}) = N({mu_sum},{sig_sum**2:.2f})')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sum_normals.png', dpi=150, bbox_inches='tight')
plt.show()

print(f"Simulated: mean={np.mean(S):.4f}, var={np.var(S):.4f}")
print(f"Theory:    mean={mu_sum:.4f}, var={sig_sum**2:.4f}")
```

## 연습문제

**연습문제 1.**
확률변수 $W$ 의 적률생성함수가 $t < 1/2$ 에서 $M_W(t) = (1 - 2t)^{-5}$ 라고 하자. $W$ 의 분포가 무엇인지 알아내어라. 또 $V_1 \sim \chi^2_3$ 과 $V_2 \sim \chi^2_7$ 이 독립이고 $W = V_1 + V_2$ 라 할 때, $V_1 + V_2$ 의 적률생성함수가 $M_W(t)$ 와 일치함을 확인하고 그 분포가 무엇인지 밝혀라.

---

**연습문제 2.**
$X_1, \ldots, X_4$ 가 독립이고 $X_i \sim N(i, i^2)$ 이라고 하자. $S = X_1 + X_2 + X_3 + X_4$ 의 정확한 분포를 구하여라.

---

**연습문제 3.**
$X \sim N(3, 4)$ 와 $Y \sim N(-1, 9)$ 가 독립이라고 하자. $P(X + Y > 5)$ 를 구하여라.

*힌트: 먼저 $X + Y$ 의 분포를 알아낸 다음 표준화한다.*
