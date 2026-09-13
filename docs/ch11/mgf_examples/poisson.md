# 푸아송분포의 적률생성함수

## Po(λ)의 적률생성함수

$X \sim \text{Po}(\lambda)$ 이면 다음과 같다.

$$M_X(t) = E[e^{tX}] = \sum_{k=0}^{\infty} e^{tk} \frac{\lambda^k}{k!} e^{-\lambda}$$

$$= e^{-\lambda} \sum_{k=0}^{\infty} \frac{(\lambda e^t)^k}{k!} = e^{-\lambda} \cdot e^{\lambda e^t} = e^{\lambda(e^t - 1)}$$

$$\boxed{M_{\text{Po}(\lambda)}(t) = e^{\lambda(e^t - 1)}}$$

## 적률 유도하기

$$M'(t) = \lambda e^t \cdot e^{\lambda(e^t - 1)}$$

$$E[X] = M'(0) = \lambda \cdot 1 = \lambda$$

$$M''(t) = (\lambda e^t)^2 e^{\lambda(e^t - 1)} + \lambda e^t \cdot e^{\lambda(e^t - 1)}$$

$$E[X^2] = M''(0) = \lambda^2 + \lambda$$

$$\text{Var}(X) = \lambda^2 + \lambda - \lambda^2 = \lambda$$

이로써 푸아송분포에서 $E[X] = \text{Var}(X) = \lambda$ 임이 확인된다.

## 푸아송 근사와의 관계

적률생성함수는 푸아송 극한정리를 깔끔하게 증명해 준다. $np = \lambda$ 인 $X \sim B(n, p)$ 에 대하여 다음이 성립한다.

$$M_{B(n,p)}(t) = \left[1 + p(e^t - 1)\right]^n = \left[1 + \frac{\lambda}{n}(e^t - 1)\right]^n$$

$n \to \infty$ 일 때 다음과 같다.

$$\left[1 + \frac{\lambda(e^t - 1)}{n}\right]^n \to e^{\lambda(e^t - 1)} = M_{\text{Po}(\lambda)}(t)$$

적률생성함수가 수렴하므로, $n \to \infty$, $p \to 0$, $np = \lambda$ 일 때 $B(n, p) \xrightarrow{d} \text{Po}(\lambda)$ 이다.

## 파이썬으로 확인하기

```python
import numpy as np

def mgf_poisson(t, lam):
    return np.exp(lam * (np.exp(t) - 1))

lam = 5.0
dt = 1e-6

M0 = mgf_poisson(0, lam)
M1 = (mgf_poisson(dt, lam) - mgf_poisson(-dt, lam)) / (2 * dt)
M2 = (mgf_poisson(dt, lam) - 2*M0 + mgf_poisson(-dt, lam)) / dt**2

print(f"Po({lam}):")
print(f"  E[X]   = {M1:.4f}  (exact: {lam})")
print(f"  Var(X) = {M2 - M1**2:.4f}  (exact: {lam})")
```

## 연습문제

**연습문제 1.** 적률생성함수를 써서 독립인 푸아송확률변수의 합이 다시 푸아송분포를 따름을 증명하여라. 곧 $X \sim \text{Po}(\lambda)$ 와 $Y \sim \text{Po}(\mu)$ 가 독립이면 $X + Y \sim \text{Po}(\lambda + \mu)$ 이다.

??? success "연습문제 1 풀이"
    $$
    M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = e^{\lambda(e^t-1)} \cdot e^{\mu(e^t-1)} = e^{(\lambda+\mu)(e^t-1)}
    $$

    이것은 $\text{Po}(\lambda + \mu)$ 의 적률생성함수이다. 유일성에 따라 $X + Y \sim \text{Po}(\lambda + \mu)$ 이다. $\square$

---

**연습문제 2.** 적률생성함수를 써서 $X \sim \text{Po}(\lambda)$ 에 대한 $E[X^3]$ 을 계산하여라.

??? success "연습문제 2 풀이"
    $M(t) = e^{\lambda(e^t-1)}$ 이다. $M'(t) = \lambda e^t M(t)$ 이고 $M''(t) = (\lambda e^t + \lambda^2 e^{2t})M(t)$ 이다. $t = 0$ 에서의 $M'''(t)$ 는 다음과 같다.

    $M'''(0) = \lambda + 3\lambda^2 + \lambda^3$

    $$
    E[X^3] = \lambda^3 + 3\lambda^2 + \lambda
    $$

---

**연습문제 3.** 푸아송 적률생성함수의 극한 결과를 써서 $X \sim B(100, 0.02)$ 일 때 $P(X = 3)$ 을 근사하여라.

??? success "연습문제 3 풀이"
    $\lambda = np = 100 \times 0.02 = 2$ 이다. 푸아송 근사에 따라 다음을 얻는다.

    $$
    P(X = 3) \approx e^{-2}\frac{2^3}{3!} = e^{-2} \cdot \frac{8}{6} = \frac{4}{3}e^{-2} \approx 0.1804
    $$

    정확한 이항분포 값은 $\binom{100}{3}(0.02)^3(0.98)^{97} \approx 0.1823$ 이다. 근사가 매우 가깝다.

---

**연습문제 4.** 푸아송분포의 적률생성함수는 모든 $t \in \mathbb{R}$ 에서 존재한다. 모든 $t$ 에 대해 $M(t) < \infty$ 임을 보여 이를 확인하여라.

??? success "연습문제 4 풀이"
    $M(t) = e^{\lambda(e^t - 1)}$ 이다. 유한한 $t$ 에 대해 $e^t$ 는 유한한 수이므로 $\lambda(e^t - 1)$ 도 유한하고, 따라서 $e^{\lambda(e^t-1)}$ 은 유한한 양수이다. 그러므로 모든 $t \in \mathbb{R}$ 에 대해 $M(t) < \infty$ 이다. $\square$

---

**연습문제 5.** $X \sim \text{Po}(3)$ 이라 하자. 적률생성함수를 써서 $E[2^X]$ 를 계산하여라.

??? success "연습문제 5 풀이"
    $E[2^X] = E[e^{X \ln 2}] = M_X(\ln 2) = e^{3(e^{\ln 2} - 1)} = e^{3(2 - 1)} = e^3 \approx 20.086$ 이다.
