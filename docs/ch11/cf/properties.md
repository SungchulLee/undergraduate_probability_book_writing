# 성질, 역변환, 레비 연속성 정리

## 특성함수는 왜 필요한가

적률생성함수 $M_X(t) = E[e^{tX}]$ 는 모든 분포에 대해 존재하지는 않는다(코시분포는 적률생성함수를 갖지 않고, 로그정규분포는 $t > 0$ 에서 $M_X(t) = \infty$ 이다). **특성함수**는 언제나 존재한다.

!!! info "존재성의 보장"
    **어떤** 확률변수 $X$ 에 대해서도(이산이든 연속이든 섞여 있든) $|e^{itX}| = 1$ 이므로 특성함수 $\varphi_X(t) = E[e^{itX}]$ 는 모든 $t \in \mathbb{R}$ 에서 존재한다.

## 기본 성질

!!! info "특성함수의 성질"
    특성함수 $\varphi_X(t)$ 를 갖는 임의의 확률변수 $X$ 에 대해 다음이 성립한다.

    1. $\varphi_X(0) = 1$
    2. 모든 $t$ 에 대해 $|\varphi_X(t)| \leq 1$
    3. $\varphi_X(-t) = \overline{\varphi_X(t)}$ (켤레복소수)
    4. $\varphi_X$ 는 $\mathbb{R}$ 위에서 **고르게 연속**이다
    5. $Y = aX + b$ 이면 $\varphi_Y(t) = e^{ibt}\,\varphi_X(at)$
    6. $X$ 와 $Y$ 가 독립이면 $\varphi_{X+Y}(t) = \varphi_X(t) \cdot \varphi_Y(t)$

성질 (6)은 $n$ 개의 독립확률변수로 넓혀진다. 곧 $\varphi_{\sum X_i}(t) = \prod \varphi_{X_i}(t)$ 이다.

## 특성함수에서 적률 구하기

$E[|X|^n] < \infty$ 이면 $\varphi_X$ 는 $t = 0$ 에서 $n$ 번 미분 가능하고 다음이 성립한다.

$$E[X^n] = \frac{\varphi_X^{(n)}(0)}{i^n}$$

특히 다음과 같다.

$$E[X] = \frac{\varphi_X'(0)}{i}, \qquad E[X^2] = \frac{\varphi_X''(0)}{i^2} = -\varphi_X''(0)$$

## 주요 분포의 특성함수

| 분포 | 특성함수 $\varphi_X(t)$ |
|:---|:---:|
| $\text{Bernoulli}(p)$ | $1 - p + pe^{it}$ |
| $\text{Binomial}(n, p)$ | $(1 - p + pe^{it})^n$ |
| $\text{Poisson}(\lambda)$ | $\exp\!\left(\lambda(e^{it} - 1)\right)$ |
| $\text{Geometric}(p)$ | $\frac{pe^{it}}{1 - (1-p)e^{it}}$ |
| $N(\mu, \sigma^2)$ | $\exp\!\left(i\mu t - \frac{\sigma^2 t^2}{2}\right)$ |
| $\text{Exp}(\lambda)$ | $\frac{\lambda}{\lambda - it}$ |
| $\text{Gamma}(\alpha, \lambda)$ | $\left(\frac{\lambda}{\lambda - it}\right)^\alpha$ |
| $\text{Cauchy}(0,1)$ | $e^{-|t|}$ |
| $\text{Uniform}(a,b)$ | $\frac{e^{itb} - e^{ita}}{it(b-a)}$ |

## 유일성 정리

!!! info "유일성(레비)"
    두 확률변수 $X$ 와 $Y$ 가 같은 분포를 갖는 것은 모든 $t \in \mathbb{R}$ 에 대해 $\varphi_X(t) = \varphi_Y(t)$ 일 때 그리고 오직 그때만이다.

이것은 적률생성함수의 유일성 정리에 짝이 되는 결과이지만, 특성함수는 언제나 존재하므로 **더 강하다**.

## 역변환 공식

특성함수는 분포를 유일하게 결정하며, 그 관계를 드러내어 적을 수도 있다.

!!! info "레비 역변환 공식"
    $X$ 의 특성함수가 $\varphi_X$ 이고 누적분포함수가 $F_X$ 이면, $F_X$ 의 연속인 점 $a < b$ 에서 다음이 성립한다.

    $$F_X(b) - F_X(a) = \lim_{T \to \infty} \frac{1}{2\pi} \int_{-T}^{T} \frac{e^{-ita} - e^{-itb}}{it}\,\varphi_X(t)\,dt$$

$\varphi_X \in L^1(\mathbb{R})$ 인, 곧 $\int_{-\infty}^{\infty} |\varphi_X(t)|\,dt < \infty$ 인 연속분포에서는 확률밀도함수를 곧바로 되찾을 수 있다.

$$f_X(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-itx}\,\varphi_X(t)\,dt$$

이것이 **역 푸리에 변환**이다. 특성함수는 밀도의 푸리에 변환이기 때문이다.

## 레비 연속성 정리

이 정리는 중심극한정리를 증명하는 열쇠가 되는 도구이다.

!!! info "레비 연속성 정리"
    $X_1, X_2, \ldots$ 를 특성함수가 $\varphi_{X_n}$ 인 확률변수라 하자.

    1. $X_n \xrightarrow{d} X$ 이면 모든 $t$ 에 대해 $\varphi_{X_n}(t) \to \varphi_X(t)$ 이다.
    2. 거꾸로 모든 $t$ 에 대해 $\varphi_{X_n}(t) \to \varphi(t)$ 이고 $\varphi$ 가 $t = 0$ 에서 연속이면, $\varphi$ 는 어떤 확률변수 $X$ 의 특성함수이고 $X_n \xrightarrow{d} X$ 이다.

**뜻.** 분포수렴을 증명하려면 특성함수가 각 점에서 수렴함을 보이는 것으로 충분하다. 이것은 누적분포함수를 직접 다루는 것보다 대수적으로 훨씬 간단할 때가 많다.

## 특성함수로 보는 중심극한정리 증명의 얼개

$X_1, X_2, \ldots$ 를 $E[X_i] = 0$, $\text{Var}(X_i) = 1$ 인 i.i.d. 라 하고 $Z_n = \frac{\sum_{i=1}^n X_i}{\sqrt{n}}$ 이라 하자.

$Z_n$ 의 특성함수는 다음과 같다.

$$\varphi_{Z_n}(t) = \left[\varphi_X\!\left(\frac{t}{\sqrt{n}}\right)\right]^n$$

$\varphi_X(s)$ 를 $s = 0$ 둘레에서 테일러 전개하면 다음과 같다.

$$\varphi_X(s) = 1 + is\,E[X] - \frac{s^2}{2}\,E[X^2] + o(s^2) = 1 - \frac{s^2}{2} + o(s^2)$$

$s = t/\sqrt{n}$ 으로 두면 다음을 얻는다.

$$\varphi_{Z_n}(t) = \left[1 - \frac{t^2}{2n} + o(1/n)\right]^n \to e^{-t^2/2}$$

$e^{-t^2/2}$ 이 $N(0,1)$ 의 특성함수이므로, 레비 연속성 정리에 따라 $Z_n \xrightarrow{d} N(0,1)$ 이다. $\square$

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

t = np.linspace(-5, 5, 500)

# --- 1번 그림: 특성함수의 실수부와 허수부 ---
# N(0,1): φ(t) = exp(-t²/2)
cf_normal = np.exp(-t**2 / 2)

# Exp(1): φ(t) = 1/(1-it)
cf_exp_real = 1 / (1 + t**2)
cf_exp_imag = t / (1 + t**2)

# 코시분포: φ(t) = exp(-|t|)
cf_cauchy = np.exp(-np.abs(t))

axes[0].plot(t, cf_normal, 'b-', lw=2, label='N(0,1): real (imag=0)')
axes[0].plot(t, cf_exp_real, 'r-', lw=2, label='Exp(1): real part')
axes[0].plot(t, cf_exp_imag, 'r--', lw=1.5, label='Exp(1): imag part')
axes[0].plot(t, cf_cauchy, 'g-', lw=2, label='Cauchy: real (imag=0)')
axes[0].set_title('Characteristic Functions')
axes[0].set_xlabel('t')
axes[0].legend(fontsize=8)
axes[0].grid(True, alpha=0.3)

# --- 2번 그림: 역변환으로 확률밀도함수 되찾기 ---
x = np.linspace(-4, 4, 300)

# N(0,1)에 대한 수치적 역변환
dt = 0.01
t_grid = np.arange(-50, 50, dt)
f_recovered = np.zeros_like(x)
for i, xi in enumerate(x):
    integrand = np.exp(-1j * t_grid * xi) * np.exp(-t_grid**2 / 2)
    f_recovered[i] = np.real(np.sum(integrand) * dt / (2 * np.pi))

axes[1].plot(x, stats.norm.pdf(x), 'b-', lw=2, label='True N(0,1) PDF')
axes[1].plot(x, f_recovered, 'r--', lw=2, label='Recovered via inversion')
axes[1].set_title('PDF Recovery via Inversion Formula')
axes[1].set_xlabel('x')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# --- 3번 그림: 특성함수로 보는 중심극한정리 ---
ns = [1, 2, 5, 20]
t_plot = np.linspace(-4, 4, 300)
colors = ['red', 'orange', 'green', 'blue']

# Exp(1)의 특성함수: 1/(1-it), 표준화한 평균: φ((t/sqrt(n)))^n
for n, color in zip(ns, colors):
    cf_sum = (1 / (1 - 1j * t_plot / np.sqrt(n)))**n
    axes[2].plot(t_plot, np.abs(cf_sum), color=color, lw=2,
                 label=f'n={n}')

cf_target = np.exp(-t_plot**2 / 2)
axes[2].plot(t_plot, cf_target, 'k--', lw=2, label='N(0,1) CF')
axes[2].set_title('CF of Standardized Sum → N(0,1) CF')
axes[2].set_xlabel('t')
axes[2].set_ylabel('|φ(t)|')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('characteristic_functions.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 연습문제

**연습문제 1.**
$X_1, \ldots, X_n$ 이 $E[X_i] = \mu$, $\text{Var}(X_i) = \sigma^2$ 인 i.i.d. 라 하자. $Z_n = \frac{\sum X_i - n\mu}{\sigma\sqrt{n}}$ 이라 정의한다.

**(a)** $\varphi_{Z_n}(t) = \left[\varphi_X\!\left(\frac{t}{\sigma\sqrt{n}}\right) \cdot e^{-i\mu t / (\sigma\sqrt{n})}\right]^n$ 임을 보여라.

**(b)** 테일러 전개 $\varphi_X(s) \approx 1 + i\mu s - \tfrac{1}{2}(\sigma^2 + \mu^2)s^2$ 를 써서 $n \to \infty$ 일 때 $\varphi_{Z_n}(t) \to e^{-t^2/2}$ 임을 보여라.

??? success "연습문제 1 풀이"

    **(a)** $Z_n = \frac{1}{\sigma\sqrt{n}}\sum(X_i - \mu)$ 이므로 $\varphi_{Z_n}(t) = \prod_{i=1}^n \varphi_{X_i - \mu}\!\left(\frac{t}{\sigma\sqrt{n}}\right) = \left[e^{-i\mu t/(\sigma\sqrt{n})}\varphi_X\!\left(\frac{t}{\sigma\sqrt{n}}\right)\right]^n$ 이다.

    **(b)** $s = t/(\sigma\sqrt{n})$ 이라 하자. 그러면 다음과 같다.

    $$e^{-i\mu s}\varphi_X(s) \approx e^{-i\mu s}\left(1 + i\mu s - \tfrac{1}{2}(\sigma^2+\mu^2)s^2\right) \approx 1 - \tfrac{1}{2}\sigma^2 s^2 = 1 - \frac{t^2}{2n}$$

    그러므로 $\varphi_{Z_n}(t) \approx \left(1 - \frac{t^2}{2n}\right)^n \to e^{-t^2/2}$ 이고, 이는 $N(0,1)$ 의 특성함수이다.
