# 무의식적 통계학자의 법칙(LOTUS)

## 왜 필요한가

$X$ 의 분포를 알고 있을 때 어떤 함수 $g$ 에 대하여 $E[g(X)]$ 를 구하고 싶다고 하자. 한 가지 방법은 먼저 $Y = g(X)$ 의 분포를 찾은 다음 $E[Y]$ 를 계산하는 것이다. 무의식적 통계학자의 법칙(LOTUS)은 지름길을 알려 준다. $g(X)$ 의 분포를 구하지 않고 $X$ 의 분포만으로 $E[g(X)]$ 를 곧바로 계산할 수 있다는 것이다.

---

## 정리의 서술

### 이산인 경우

$X$ 가 확률질량함수 $p(x)$ 를 갖는 이산확률변수이면 다음이 성립한다.

$$
E[g(X)] = \sum_{x} g(x) \, p(x)
$$

### 연속인 경우

$X$ 가 확률밀도함수 $f(x)$ 를 갖는 연속확률변수이면 다음이 성립한다.

$$
E[g(X)] = \int_{-\infty}^{\infty} g(x) \, f(x) \, dx
$$

---

## 왜 "무의식적 통계학자"인가

이 이름에는 익살이 담겨 있다. 이 공식은 마치 $g(x)$ 자체를 확률변수로 여겨 $g(X)$ 의 분포가 아닌 $X$ 의 분포로 기댓값을 "무심코" 계산하는 것처럼 보이기 때문이다. 이름은 그래도, 이것은 엄밀하게 증명되는 정리이다.

---

## 예제

### 예제 1: 공정한 주사위의 E[X²]

$X$ 를 공정한 주사위의 눈이라 하자. LOTUS에 따라 다음을 얻는다.

$$
E[X^2] = \sum_{k=1}^{6} k^2 \cdot \frac{1}{6} = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6} \approx 15.17
$$

참고: 일반적으로 $(E[X])^2 = 3.5^2 = 12.25 \neq E[X^2]$ 이다.

### 예제 2: 지수분포의 E[eX]

$X \sim \text{Exp}(\lambda)$ 이고 $x \geq 0$ 에서 $f(x) = \lambda e^{-\lambda x}$ 이면 다음을 얻는다.

$$
E[e^{tX}] = \int_0^{\infty} e^{tx} \cdot \lambda e^{-\lambda x} \, dx = \frac{\lambda}{\lambda - t}, \quad t < \lambda
$$

이것이 지수분포의 **적률생성함수(MGF)** 이다.

### 예제 3: 연속균등분포의 E[X²]

$X \sim \text{Uniform}(0, 1)$ 이면 다음을 얻는다.

$$
E[X^2] = \int_0^1 x^2 \cdot 1 \, dx = \frac{1}{3}
$$

---

## 결합분포에서의 LOTUS

LOTUS는 여러 확률변수의 함수로도 확장된다.

### 이산인 경우

$$
E[g(X, Y)] = \sum_x \sum_y g(x, y) \, p(x, y)
$$

### 연속인 경우

$$
E[g(X, Y)] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) \, f(x, y) \, dx \, dy
$$

---

## 응용: 분산 계산

분산을 다음 간편식으로 구할 때 LOTUS가 꼭 필요하다.

$$
\text{Var}(X) = E[X^2] - (E[X])^2
$$

여기서 $E[X^2]$ 는 $g(x) = x^2$ 로 놓고 LOTUS를 써서 계산한다.

---

## 파이썬 구현

```python
import numpy as np
from scipy import integrate

# LOTUS로 구하는 공정한 주사위의 E[X^2]
values = np.arange(1, 7)
probs = np.ones(6) / 6
E_X2 = np.sum(values**2 * probs)
E_X = np.sum(values * probs)
print(f"E[X^2] = {E_X2:.4f}")        # 15.1667
print(f"(E[X])^2 = {E_X**2:.4f}")    # 12.25

# 수치적분으로 구하는 Uniform(0,1)의 E[X^2]
result, _ = integrate.quad(lambda x: x**2 * 1, 0, 1)
print(f"E[X^2] for Uniform(0,1) = {result:.4f}")  # 0.3333

# Exp(lambda)의 E[e^(tX)] - 적률생성함수
lam = 2.0
t = 0.5
mgf_exact = lam / (lam - t)
mgf_numerical, _ = integrate.quad(lambda x: np.exp(t*x) * lam * np.exp(-lam*x), 0, np.inf)
print(f"MGF exact = {mgf_exact:.4f}")
print(f"MGF numerical = {mgf_numerical:.4f}")

# 몬테카를로로 확인
np.random.seed(42)
N = 1_000_000
samples = np.random.exponential(1/lam, N)
print(f"Monte Carlo E[e^(tX)] = {np.mean(np.exp(t * samples)):.4f}")
```

## 연습문제

**연습문제 1.** $X \sim \text{Uniform}(a, b)$ 일 때 LOTUS를 써서 $E[X^2] = \dfrac{a^2 + ab + b^2}{3}$ 임을 보여라.

??? success "연습문제 1 풀이"
    $X$ 는 $[a, b]$ 위에서 밀도 $f(x) = 1/(b - a)$ 를 갖는다. LOTUS에 따라 다음을 얻는다.

    $$
    E[X^2] = \int_a^b \frac{x^2}{b - a} \, dx = \frac{1}{b - a} \cdot \frac{b^3 - a^3}{3}
    $$

    $b^3 - a^3 = (b - a)(a^2 + ab + b^2)$ 로 인수분해하면 다음과 같다.

    $$
    E[X^2] = \frac{a^2 + ab + b^2}{3}
    $$

    $\square$

---

**연습문제 2.** $X \sim \text{Poisson}(\lambda)$ 라 하자. LOTUS를 써서 $E[X(X-1)]$ 을 구하고, 이로부터 $\text{Var}(X) = \lambda$ 임을 이끌어내어라.

??? success "연습문제 2 풀이"
    $g(x) = x(x-1)$ 로 놓고 LOTUS를 쓰면 다음을 얻는다.

    $$
    E[X(X-1)] = \sum_{k=0}^{\infty} k(k-1)\,\frac{e^{-\lambda}\lambda^k}{k!} = \lambda^2 \sum_{k=2}^{\infty} \frac{e^{-\lambda}\lambda^{k-2}}{(k-2)!} = \lambda^2
    $$

    그러면 $E[X^2] = E[X(X-1)] + E[X] = \lambda^2 + \lambda$ 이므로 다음과 같다.

    $$
    \text{Var}(X) = E[X^2] - (E[X])^2 = \lambda^2 + \lambda - \lambda^2 = \lambda
    $$

---

**연습문제 3.** $X \sim \text{Exp}(\lambda)$ 라 하자. LOTUS를 써서 모든 양의 정수 $n$ 에 대하여 $E[X^n] = \dfrac{n!}{\lambda^n}$ 임을 보여라.

??? success "연습문제 3 풀이"
    LOTUS에 따라 다음과 같다.

    $$
    E[X^n] = \int_0^{\infty} x^n \,\lambda e^{-\lambda x}\, dx
    $$

    $u = \lambda x$ 로 치환하면($dx = du/\lambda$) 다음을 얻는다.

    $$
    E[X^n] = \frac{1}{\lambda^n}\int_0^{\infty} u^n\, e^{-u}\, du = \frac{\Gamma(n+1)}{\lambda^n} = \frac{n!}{\lambda^n}
    $$

    $\square$

---

**연습문제 4.** $X$ 를 확률밀도함수가 $f$ 이고 평균이 $\mu = E[X]$ 인 연속확률변수라 하자. LOTUS를 써서 $\text{Var}(X) = E[X^2] - (E[X])^2$ 임을 증명하여라.

??? success "연습문제 4 풀이"
    정의에 따라 $\text{Var}(X) = E[(X - \mu)^2]$ 이다. $g(x) = (x - \mu)^2$ 로 놓고 LOTUS를 적용하면 다음과 같다.

    $$
    E[(X - \mu)^2] = \int_{-\infty}^{\infty} (x - \mu)^2\, f(x)\, dx = \int_{-\infty}^{\infty} (x^2 - 2\mu x + \mu^2)\, f(x)\, dx
    $$

    $$
    = E[X^2] - 2\mu\,E[X] + \mu^2 = E[X^2] - 2\mu^2 + \mu^2 = E[X^2] - \mu^2
    $$

    $\square$

---

**연습문제 5.** $X \sim \text{Uniform}(0, 1)$ 이라 하자. LOTUS를 써서 $E[\ln X]$ 를 구하여라.

??? success "연습문제 5 풀이"
    LOTUS에 따라 다음과 같다.

    $$
    E[\ln X] = \int_0^1 \ln x \cdot 1\, dx = \bigl[x\ln x - x\bigr]_0^1
    $$

    $x = 1$ 에서는 $1 \cdot 0 - 1 = -1$ 이다. $x = 0$ 에서는 로피탈의 정리에 따라 $\lim_{x \to 0^+}(x \ln x - x) = 0$ 이다. 그러므로 다음을 얻는다.

    $$
    E[\ln X] = -1
    $$
