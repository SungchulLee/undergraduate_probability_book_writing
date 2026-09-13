# 정의, 존재성, 적률생성함수와의 관계

## 정의

확률변수 $X$ 의 **특성함수(CF)** 는 다음과 같이 정의된다.

$$\varphi_X(t) = E[e^{itX}]$$

여기서 $i = \sqrt{-1}$ 이고 $t \in \mathbb{R}$ 이다. 오일러 공식 $e^{itX} = \cos(tX) + i\sin(tX)$ 를 쓰면 다음과 같다.

$$\varphi_X(t) = E[\cos(tX)] + i\,E[\sin(tX)]$$

확률밀도함수 $f$ 를 갖는 연속확률변수 $X$ 에 대해서는 다음과 같다.

$$\varphi_X(t) = \int_{-\infty}^{\infty} e^{itx}\,f(x)\,dx$$

이것은 바로 밀도 $f$ 의 **푸리에 변환**이다.

## 존재성

!!! info "언제나 존재한다"
    특성함수 $\varphi_X(t) = E[e^{itX}]$ 는 **모든** 확률변수 $X$ 에 대해, 그리고 **모든** $t \in \mathbb{R}$ 에 대해 존재한다.

**증명.** $|e^{itX}| = |\cos(tX) + i\sin(tX)| = 1$ 이므로 다음이 성립한다.

$$|\varphi_X(t)| = |E[e^{itX}]| \leq E[|e^{itX}|] = E[1] = 1$$

유계인 확률변수의 기댓값은 언제나 존재한다. $\square$

이것이 적률생성함수와 견주었을 때의 결정적인 장점이다. 적률생성함수 $M_X(t) = E[e^{tX}]$ 에는 유계가 아닐 수 있는 $e^{tX}$ 가 들어 있어 기댓값이 발산할 수 있다. 특성함수는 $t$ 를 $it$ 로 바꾸어 지수적인 증가를 유계인 진동으로 바꾸어 놓는다.

## 적률생성함수와의 관계

적률생성함수 $M_X(t)$ 가 $0$ 의 근방에서 존재할 때, 특성함수는 형식적으로 $t \mapsto it$ 를 대입하여 얻는다.

$$\varphi_X(t) = M_X(it)$$

거꾸로 적률생성함수가 존재할 때는 $M_X(t) = \varphi_X(-it)$ 이다.

???+ example "정규분포"
    $X \sim N(\mu, \sigma^2)$ 의 적률생성함수는 $M_X(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2}$ 이다.

    $t \mapsto it$ 를 대입하면 다음과 같다.

    $$\varphi_X(t) = e^{\mu(it) + \frac{1}{2}\sigma^2(it)^2} = e^{i\mu t - \frac{1}{2}\sigma^2 t^2}$$

???+ example "지수분포"
    $X \sim \text{Exp}(\lambda)$ 의 적률생성함수는 $t < \lambda$ 에서 $M_X(t) = \frac{\lambda}{\lambda - t}$ 이다.

    $t \mapsto it$ 를 대입하면 다음과 같다.

    $$\varphi_X(t) = \frac{\lambda}{\lambda - it}$$

    적률생성함수는 $t < \lambda$ 에서만 존재하지만, 특성함수는 모든 $t \in \mathbb{R}$ 에서 정의된다.

## 적률생성함수가 존재하지 않을 때

적률생성함수를 갖지 않는 분포도 특성함수는 언제나 갖는다.

???+ example "코시분포"
    표준 코시분포의 확률밀도함수는 $f(x) = \frac{1}{\pi(1+x^2)}$ 이다. 이 분포는 적률생성함수를 갖지 않지만($t \neq 0$ 에서 $E[e^{tX}] = \infty$), 특성함수는 다음과 같다.

    $$\varphi_X(t) = e^{-|t|}$$

    이 특성함수는 잘 정의되고 매끄러우며 분포 전체를 담고 있다.

## 특성함수가 중요한 까닭

특성함수는 확률론에서 크게 세 가지 구실을 한다.

1. **보편성.** 모든 분포에 대해 존재하므로, 적률생성함수를 쓸 수 없을 때의 기본 도구가 된다.

2. **유일성.** 두 확률변수가 같은 분포를 갖는 것은 같은 특성함수를 가질 때 그리고 오직 그때만이다. 밀도는 역변환 공식으로 되찾을 수 있다(성질을 다룬 쪽을 보라).

3. **극한정리의 증명.** 레비 연속성 정리는 $X_n \xrightarrow{d} X$ 인 것이 모든 $t$ 에 대해 $\varphi_{X_n}(t) \to \varphi_X(t)$ 인 것과 같음을 말해 준다. 이것이 중심극한정리로 가는 가장 깔끔한 길이다.

## 변환 방법들의 비교

| 성질 | 적률생성함수 $M_X(t)$ | 확률생성함수 $G_X(s)$ | 특성함수 $\varphi_X(t)$ |
|:---|:---:|:---:|:---:|
| 정의 | $E[e^{tX}]$ | $E[s^X]$ | $E[e^{itX}]$ |
| 모든 확률변수에 대해 존재하는가? | 아니다 | $X \in \{0,1,2,\ldots\}$ 일 때만 | **그렇다** |
| 분포를 결정하는가? | 그렇다(존재할 때) | 그렇다(정의역 안에서) | **언제나 그렇다** |
| 실숫값인가? | 그렇다 | 그렇다 | **복소수** |
| 적률 뽑아내기 | $M^{(n)}(0)$ | 계승적률 | $\varphi^{(n)}(0)/i^n$ |
| 곱의 법칙(독립) | 그렇다 | 그렇다 | 그렇다 |

## 파이썬으로 확인하기

```python
import numpy as np
from scipy import stats

# t = 1에서 N(2, 9)의 특성함수를 확인한다
mu, sigma2 = 2, 9
t = 1.0

# 정확한 특성함수
cf_exact = np.exp(1j * mu * t - 0.5 * sigma2 * t**2)

# 몬테카를로 추정값
np.random.seed(42)
X = np.random.normal(mu, np.sqrt(sigma2), 200000)
cf_mc = np.mean(np.exp(1j * t * X))

print("CF of N(2, 9) at t=1:")
print(f"  Exact: {cf_exact:.6f}")
print(f"  MC:    {cf_mc:.6f}")

# 코시분포의 특성함수 exp(-|t|)를 확인한다
t_vals = [0.5, 1.0, 2.0]
X_cauchy = np.random.standard_cauchy(500000)
print("\nCauchy CF (no MGF exists):")
for t in t_vals:
    cf_exact = np.exp(-abs(t))
    cf_mc = np.mean(np.exp(1j * t * X_cauchy))
    print(f"  t={t}: exact={cf_exact:.4f}, MC real={cf_mc.real:.4f}")
```

## 연습문제

**연습문제 1.**
$X \sim \text{Exp}(1)$ 이라 하자.

**(a)** $\varphi_X(t) = E[e^{itX}]$ 를 적분으로 직접 계산하여라.

**(b)** 그 답이 $M_X(it) = \frac{1}{1 - it}$ 과 일치함을 확인하여라.

**(c)** $|\varphi_X(t)| \leq 1$ 과 $\varphi_X(0) = 1$ 을 확인하여라.

??? success "연습문제 1 풀이"

    **(a)** $\varphi_X(t) = \int_0^{\infty} e^{itx} e^{-x}\,dx = \int_0^{\infty} e^{-(1-it)x}\,dx = \frac{1}{1-it}$ 이다.

    $\text{Re}(1 - it) = 1 > 0$ 이므로 이 적분은 수렴한다.

    **(b)** $M_X(t) = \frac{1}{1-t}$ 이므로 $M_X(it) = \frac{1}{1-it}$ 이다. 확인되었다.

    **(c)** 모든 $t$ 에 대해 $|\varphi_X(t)| = \frac{1}{\sqrt{1+t^2}} \leq 1$ 이다. 또한 $\varphi_X(0) = 1$ 이다.
