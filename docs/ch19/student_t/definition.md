# 정의와 유도

## 정의

$Z \sim N(0, 1)$ 과 $V \sim \chi^2_d$ 가 **독립**이면 다음이 성립한다.

$$T = \frac{Z}{\sqrt{V/d}} \sim t_d$$

여기에서 모수 $d$ 를 **자유도**라고 한다.

## 야코비안을 이용한 밀도함수 유도

### 문제 설정

$Z \sim N(0,1)$ 과 $V \sim \chi^2_d$ 가 독립일 때 $T = Z / \sqrt{V/d}$, $U = V$ 로 두자.

역변환은 $z = t\sqrt{u/d}$, $v = u$ 이다.

### 야코비안

$$\left|\frac{\partial(z, v)}{\partial(t, u)}\right| = \left|\frac{\partial(t, u)}{\partial(z, v)}\right|^{-1} = \left|\det \begin{pmatrix} 1/\sqrt{v/d} & * \\ 0 & 1 \end{pmatrix}\right|^{-1} = \sqrt{\frac{v}{d}} = \sqrt{\frac{u}{d}}$$

### 결합밀도함수

$Z$ 와 $V$ 가 독립이므로 $f_{Z,V}(z,v) = f_Z(z) \cdot f_V(v)$ 이고 다음을 얻는다.

$$f_{T,U}(t, u) = f_{Z,V}(z, v) \left|\frac{\partial(z,v)}{\partial(t,u)}\right|$$

$$= \frac{1}{\sqrt{2\pi}} e^{-z^2/2} \cdot \frac{(1/2)^{d/2}}{\Gamma(d/2)} v^{d/2-1} e^{-v/2} \cdot \sqrt{\frac{u}{d}}$$

여기에 $z = t\sqrt{u/d}$ 와 $v = u$ 를 넣으면 다음과 같다.

$$= \frac{(1/2)(1/2 \cdot u)^{d/2-1}}{\sqrt{2\pi}\,\Gamma(d/2)} \, e^{-\frac{1+t^2/d}{2}u} \cdot \sqrt{\frac{u}{d}}$$

### 조건부분포 알아보기

$\lambda = \frac{1 + t^2/d}{2}$ 로 두면 결합밀도함수가 다음과 같이 인수분해된다.

$$f_{T,U}(t, u) = \underbrace{\frac{1}{\sqrt{d}\, B(1/2, \, d/2)} \left(1 + \frac{t^2}{d}\right)^{-(d+1)/2}}_{f_T(t)} \cdot \underbrace{\frac{\lambda\, (\lambda u)^{(d+1)/2 - 1} e^{-\lambda u}}{\Gamma\!\left(\frac{d+1}{2}\right)}}_{f_{U|T=t}(u) \;=\; \Gamma\!\left(\frac{d+1}{2}, \, \lambda\right)}$$

### T 의 주변밀도함수

$u$ 에 대하여 적분하면(감마밀도함수의 적분이 $1$ 이므로) 다음을 얻는다.

$$\boxed{f_T(t) = \frac{1}{\sqrt{d}\, B\!\left(\frac{1}{2}, \frac{d}{2}\right)} \left(1 + \frac{t^2}{d}\right)^{-(d+1)/2}, \quad -\infty < t < \infty}$$

여기에서 $B(a, b) = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$ 는 베타함수이다.

## 파이썬으로 확인하기

```python
import numpy as np
from scipy import stats, special
import matplotlib.pyplot as plt

d = 5
x = np.linspace(-5, 5, 500)

# 이론적인 밀도함수
B = special.beta(0.5, d / 2)
pdf_formula = (1 + x**2 / d)**(-(d + 1) / 2) / (np.sqrt(d) * B)

# scipy 의 밀도함수
pdf_scipy = stats.t.pdf(x, d)

print(f"Max difference: {np.max(np.abs(pdf_formula - pdf_scipy)):.2e}")

# 모의실험으로 확인하기
np.random.seed(42)
z = np.random.standard_normal(100_000)
v = np.random.chisquare(d, 100_000)
t_samples = z / np.sqrt(v / d)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(t_samples, bins=100, density=True, alpha=0.5, label='Simulation')
ax.plot(x, pdf_scipy, 'r-', lw=2, label=f'$t_{{{d}}}$ PDF')
ax.set_xlabel('$t$')
ax.set_ylabel('Density')
ax.set_title(f"Student's $t$ Distribution ($d = {d}$)")
ax.legend()
plt.tight_layout()
plt.show()
```

## 연습문제

**연습문제 1.**
$Z \sim N(0,1)$ 과 $V \sim \chi^2_4$ 가 독립이라고 하자. $T = Z/\sqrt{V/4}$ 의 평균과 분산을 구하여라.

??? success "연습문제 1 풀이"
    $T \sim t_4$ 이다. $d = 4 > 1$ 이므로 평균은 $0$ 이고, 분산은 $4/(4-2) = 2$ 이다.
