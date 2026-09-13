# 표준정규확률변수의 제곱합으로서의 정의

## 되짚어 보기: 감마분포

카이제곱분포는 감마분포의 특별한 경우이다. $\Gamma(\alpha, \lambda)$ 의 주요 성질을 떠올려 보자.

1. $\text{Exp}(\lambda) \stackrel{d}{=} \Gamma(1, \lambda)$
2. $\text{Exp}(\lambda) * \text{Exp}(\lambda) \stackrel{d}{=} \Gamma(2, \lambda)$
3. $\underbrace{\text{Exp}(\lambda) * \cdots * \text{Exp}(\lambda)}_{n} \stackrel{d}{=} \Gamma(n, \lambda)$
4. $\Gamma(\alpha, \lambda) * \Gamma(\beta, \lambda) \stackrel{d}{=} \Gamma(\alpha + \beta, \lambda)$ (가법성)

여기에서 $*$ 는 합성곱, 곧 독립인 확률변수들의 합의 분포를 나타낸다.

## 정의

$Z_1, Z_2, \ldots, Z_d$ 가 **i.i.d.** $N(0, 1)$ 이면 다음이 성립한다.

$$\sum_{i=1}^d Z_i^2 \sim \chi^2_d$$

여기에서 모수 $d$ 를 **자유도**라고 한다.

## 감마분포와의 관계

### 1단계: χ²₁ = Z² ~ Γ(1/2, 1/2)

$x > 0$ 에 대하여

$$P(Z^2 \leq x) = P(-\sqrt{x} \leq Z \leq \sqrt{x}) = \int_{-\sqrt{x}}^{\sqrt{x}} \frac{1}{\sqrt{2\pi}} e^{-s^2/2}\, ds = 2\int_0^{\sqrt{x}} \frac{1}{\sqrt{2\pi}} e^{-s^2/2}\, ds$$

이고, 이를 $x$ 에 대하여 미분하면

$$f_{Z^2}(x) = 2 \cdot \frac{1}{\sqrt{2\pi}} e^{-x/2} \cdot \frac{1}{2} x^{-1/2} = \frac{\frac{1}{2} \left(\frac{1}{2} x\right)^{1/2 - 1} e^{-x/2}}{\Gamma(1/2)} = f_{\Gamma(1/2, \, 1/2)}(x)$$

를 얻는다. 따라서 다음이 성립한다.

$$\chi^2_1 \stackrel{d}{=} Z^2 \stackrel{d}{=} \Gamma\!\left(\frac{1}{2}, \frac{1}{2}\right)$$

### 2단계: χ²d ~ Γ(d/2, 1/2)

감마분포의 가법성에 따라 다음을 얻는다.

$$\chi^2_d \stackrel{d}{=} Z_1^2 + \cdots + Z_d^2 \stackrel{d}{=} \underbrace{\Gamma\!\left(\frac{1}{2}, \frac{1}{2}\right) * \cdots * \Gamma\!\left(\frac{1}{2}, \frac{1}{2}\right)}_{d} \stackrel{d}{=} \Gamma\!\left(\frac{d}{2}, \frac{1}{2}\right)$$

## 밀도함수

감마분포의 밀도함수에 $\alpha = d/2$, $\lambda = 1/2$ 를 넣으면 다음과 같다.

$$f_{\chi^2_d}(x) = \frac{(1/2)^{d/2}}{\Gamma(d/2)} x^{d/2 - 1} e^{-x/2}, \quad x > 0$$

## 파이썬으로 확인하기

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x = np.linspace(0.01, 30, 500)

fig, ax = plt.subplots(figsize=(8, 5))
for d in [1, 2, 3, 5, 10, 15]:
    ax.plot(x, stats.chi2.pdf(x, d), label=f'$d = {d}$')

ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.set_title('Chi-Squared PDF for Various Degrees of Freedom')
ax.legend()
ax.set_ylim(0, 0.5)
plt.tight_layout()
plt.show()
```

## 연습문제

**연습문제 1.**
$Z_1, Z_2, Z_3$ 가 i.i.d. $N(0,1)$ 이라고 하자. $E[Z_1^2 + Z_2^2 + Z_3^2]$ 과 $\text{Var}(Z_1^2 + Z_2^2 + Z_3^2)$ 을 구하여라.

??? success "연습문제 1 풀이"
    $Z_1^2 + Z_2^2 + Z_3^2 \sim \chi^2_3$ 이므로 기댓값은 $3$ 이고 분산은 $2(3) = 6$ 이다.

---

**연습문제 2.**
$X \sim N(0, \sigma^2)$ 이라고 하자. 분포함수를 이용하는 방법으로 $Y = X^2$ 의 밀도함수를 유도하여라.

??? success "연습문제 2 풀이"
    $y > 0$ 에 대하여

    $$P(Y \leq y) = P(X^2 \leq y) = P(-\sqrt{y} \leq X \leq \sqrt{y}) = \mathcal{N}\!\left(\frac{\sqrt{y}}{\sigma}\right) - \mathcal{N}\!\left(\frac{-\sqrt{y}}{\sigma}\right)$$

    이고, 이를 미분하면

    $$f_Y(y) = \frac{1}{\sigma\sqrt{2\pi}} e^{-y/(2\sigma^2)} \cdot \frac{1}{2\sqrt{y}} + \frac{1}{\sigma\sqrt{2\pi}} e^{-y/(2\sigma^2)} \cdot \frac{1}{2\sqrt{y}} = \frac{1}{\sigma\sqrt{2\pi y}} e^{-y/(2\sigma^2)}$$

    를 얻는다. $\sigma = 1$ 이면 $f_Y(y) = \frac{1}{\sqrt{2\pi y}} e^{-y/2}$ 이 되며, 이는 $\chi^2_1 = \Gamma(1/2, 1/2)$ 의 밀도함수이다.
