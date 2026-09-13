# 지수분포와 감마분포의 적률생성함수

## Exponential(λ)의 적률생성함수

$X \sim \text{Exp}(\lambda)$ 가 $x \geq 0$ 에서 확률밀도함수 $f(x) = \lambda e^{-\lambda x}$ 를 가지면 다음과 같다.

$$M_X(t) = E[e^{tX}] = \int_0^{\infty} e^{tx} \lambda e^{-\lambda x}\,dx = \lambda \int_0^{\infty} e^{-(\lambda - t)x}\,dx$$

이 적분은 $\lambda - t > 0$ 일 때, 곧 $t < \lambda$ 일 때 수렴한다.

$$M_X(t) = \lambda \cdot \frac{1}{\lambda - t} = \frac{\lambda}{\lambda - t}$$

$$\boxed{M_{\text{Exp}(\lambda)}(t) = \frac{\lambda}{\lambda - t}, \quad t < \lambda}$$

### 적률 유도하기

$M_X(t) = \lambda(\lambda - t)^{-1}$ 로 적으면 다음과 같다.

$$M_X'(t) = \lambda(\lambda - t)^{-2}$$

$$E[X] = M_X'(0) = \frac{\lambda}{\lambda^2} = \frac{1}{\lambda}$$

$$M_X''(t) = 2\lambda(\lambda - t)^{-3}$$

$$E[X^2] = M_X''(0) = \frac{2\lambda}{\lambda^3} = \frac{2}{\lambda^2}$$

$$\text{Var}(X) = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}$$

## Gamma(α, λ)의 적률생성함수

$X \sim \text{Gamma}(\alpha, \lambda)$ 가 $x > 0$ 에서 확률밀도함수 $f(x) = \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\lambda x}$ 를 가지면 다음과 같다.

$$M_X(t) = \int_0^{\infty} e^{tx} \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\lambda x}\,dx = \frac{\lambda^\alpha}{\Gamma(\alpha)} \int_0^{\infty} x^{\alpha - 1} e^{-(\lambda - t)x}\,dx$$

$t < \lambda$ 일 때 $u = (\lambda - t)x$ 로 치환하면 다음을 얻는다.

$$= \frac{\lambda^\alpha}{\Gamma(\alpha)} \cdot \frac{\Gamma(\alpha)}{(\lambda - t)^\alpha} = \left(\frac{\lambda}{\lambda - t}\right)^\alpha$$

$$\boxed{M_{\text{Gamma}(\alpha, \lambda)}(t) = \left(\frac{\lambda}{\lambda - t}\right)^\alpha, \quad t < \lambda}$$

!!! note "특별한 경우로서의 지수분포"
    $\alpha = 1$ 로 두면 $M_{\text{Exp}(\lambda)}(t) = \frac{\lambda}{\lambda - t}$ 가 되살아난다. 이는 $\text{Exp}(\lambda) = \text{Gamma}(1, \lambda)$ 임을 확인해 준다.

### 적률 유도하기

$$M_X'(t) = \alpha \lambda^\alpha (\lambda - t)^{-\alpha - 1}$$

$$E[X] = M_X'(0) = \frac{\alpha}{\lambda}$$

$$M_X''(t) = \alpha(\alpha + 1)\lambda^\alpha (\lambda - t)^{-\alpha - 2}$$

$$E[X^2] = M_X''(0) = \frac{\alpha(\alpha + 1)}{\lambda^2}$$

$$\text{Var}(X) = \frac{\alpha(\alpha + 1)}{\lambda^2} - \frac{\alpha^2}{\lambda^2} = \frac{\alpha}{\lambda^2}$$

## 파이썬으로 확인하기

```python
import numpy as np
from scipy.misc import derivative

def mgf_exp(t, lam=2.0):
    return lam / (lam - t)

def mgf_gamma(t, alpha=3.0, lam=2.0):
    return (lam / (lam - t))**alpha

# Exp(2): E[X] = 0.5, Var(X) = 0.25
EX = derivative(mgf_exp, 0, n=1, dx=1e-6)
EX2 = derivative(mgf_exp, 0, n=2, dx=1e-6)
print("Exp(2):")
print(f"  E[X]   = {EX:.4f}  (exact: 0.5)")
print(f"  Var(X) = {EX2 - EX**2:.4f}  (exact: 0.25)")

# Gamma(3, 2): E[X] = 1.5, Var(X) = 0.75
EX = derivative(mgf_gamma, 0, n=1, dx=1e-6)
EX2 = derivative(mgf_gamma, 0, n=2, dx=1e-6)
print("\nGamma(3, 2):")
print(f"  E[X]   = {EX:.4f}  (exact: 1.5)")
print(f"  Var(X) = {EX2 - EX**2:.4f}  (exact: 0.75)")
```

## 연습문제

**연습문제 1.**
$X \sim \text{Exp}(3)$ 이라 하자.

**(a)** $M_X(t)$ 와 그 정의역을 적어라.

**(b)** $E[X]$, $E[X^2]$, $E[X^3]$ 을 계산하여라.

**(c)** 일반적인 $n$ 에 대해 $E[X^n] = \frac{n!}{\lambda^n}$ 임을 확인하여라.

??? success "연습문제 1 풀이"

    **(a)** $t < 3$ 에 대해 $M_X(t) = \frac{3}{3 - t}$ 이다.

    **(b)** $M_X^{(n)}(t) = \frac{n! \cdot 3}{(3-t)^{n+1}}$ 이므로 $M_X^{(n)}(0) = \frac{n!}{3^n}$ 이다.

    따라서 $E[X] = \tfrac{1}{3}$, $E[X^2] = \tfrac{2}{9}$, $E[X^3] = \tfrac{6}{27} = \tfrac{2}{9}$ 이다.

    **(c)** $M_X(t) = \frac{\lambda}{\lambda - t} = \sum_{n=0}^{\infty}\frac{t^n}{\lambda^n}$ 이므로 $\frac{E[X^n]}{n!} = \frac{1}{\lambda^n}$ 이고, 따라서 $E[X^n] = \frac{n!}{\lambda^n}$ 이다.

---

**연습문제 2.**
$X_1, \ldots, X_{20}$ 이 i.i.d. $\text{Bernoulli}(0.3)$ 이고 $S = \sum_{i=1}^{20} X_i$ 라 하자.

**(a)** 곱의 법칙을 써서 $M_S(t)$ 를 계산하여라.

**(b)** $S$ 의 분포를 알아내어라.

**(c)** 푸아송 근사의 적률생성함수를 써서 $P(S = 0)$ 을 근사하여라.

??? success "연습문제 2 풀이"

    **(a)** $M_S(t) = [1 + 0.3(e^t - 1)]^{20} = [0.7 + 0.3e^t]^{20}$ 이다.

    **(b)** 이것은 $B(20, 0.3)$ 의 적률생성함수이므로 $S \sim B(20, 0.3)$ 이다.

    **(c)** $\lambda = np = 6$ 이므로 $P(S = 0) \approx e^{-6} \approx 0.0025$ 이다. 정확한 값은 $0.7^{20} \approx 0.0008$ 이다.
