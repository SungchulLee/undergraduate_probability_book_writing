# 주요 이산분포의 확률생성함수

## Bernoulli(p)

$X \sim \text{Bernoulli}(p)$ 이면 다음과 같다.

$$G_X(s) = E[s^X] = s^0(1-p) + s^1 \cdot p = 1 - p + ps$$

**적률:** $G'(s) = p$ 이므로 $E[X] = G'(1) = p$ 이다. $G''(s) = 0$ 이므로 $\text{Var}(X) = 0 + p - p^2 = p(1-p)$ 이다.

## Binomial(n, p)

$X \sim B(n, p)$ 이면 $X_i \stackrel{\text{iid}}{\sim} \text{Bernoulli}(p)$ 에 대해 $X = \sum_{i=1}^n X_i$ 이다. 곱의 법칙에 따라 다음을 얻는다.

$$G_X(s) = [G_{X_1}(s)]^n = (1 - p + ps)^n$$

**적률:** $G'(s) = np(1-p+ps)^{n-1}$ 이므로 $E[X] = np$ 이다.

$$G''(s) = n(n-1)p^2(1-p+ps)^{n-2} \implies G''(1) = n(n-1)p^2$$

$$\text{Var}(X) = n(n-1)p^2 + np - n^2p^2 = np(1-p)$$

## Geometric(p)

$X \sim \text{Geo}(p)$ 가 $k = 1, 2, \ldots$ 에 대해 $P(X = k) = (1-p)^{k-1}p$ 를 가지면 다음과 같다.

$$G_X(s) = \sum_{k=1}^{\infty} (1-p)^{k-1}p\,s^k = ps \sum_{j=0}^{\infty} [(1-p)s]^j = \frac{ps}{1 - (1-p)s}$$

여기서 $|s| < \frac{1}{1-p}$ 이다.

**적률:** $q = 1-p$ 라 하자. 그러면 $G'(s) = \frac{p}{(1 - qs)^2}$ 이므로 $E[X] = G'(1) = \frac{1}{p}$ 이다.

$$G''(s) = \frac{2pq}{(1-qs)^3} \implies G''(1) = \frac{2q}{p^2}$$

$$\text{Var}(X) = \frac{2q}{p^2} + \frac{1}{p} - \frac{1}{p^2} = \frac{q}{p^2}$$

## Negative Binomial(r, p)

$X \sim \text{NB}(r, p)$ 가 i.i.d. $\text{Geo}(p)$ 확률변수 $r$ 개의 합이면 다음과 같다.

$$G_X(s) = \left[\frac{ps}{1 - (1-p)s}\right]^r$$

**적률:** $E[X] = \frac{r}{p}$ 이고 $\text{Var}(X) = \frac{r(1-p)}{p^2}$ 이다.

## Poisson(λ)

$X \sim \text{Po}(\lambda)$ 이면 다음과 같다.

$$G_X(s) = \sum_{k=0}^{\infty} \frac{\lambda^k}{k!}e^{-\lambda}\,s^k = e^{-\lambda}\sum_{k=0}^{\infty}\frac{(\lambda s)^k}{k!} = e^{-\lambda} \cdot e^{\lambda s} = e^{\lambda(s-1)}$$

**적률:** $G'(s) = \lambda e^{\lambda(s-1)}$ 이므로 $E[X] = \lambda$ 이다.

$$G''(s) = \lambda^2 e^{\lambda(s-1)} \implies G''(1) = \lambda^2$$

$$\text{Var}(X) = \lambda^2 + \lambda - \lambda^2 = \lambda$$

## 요약 표

| 분포 | 확률생성함수 $G_X(s)$ | $E[X]$ | $\text{Var}(X)$ |
|:---|:---:|:---:|:---:|
| $\text{Bernoulli}(p)$ | $1 - p + ps$ | $p$ | $p(1-p)$ |
| $B(n, p)$ | $(1-p+ps)^n$ | $np$ | $np(1-p)$ |
| $\text{Geo}(p)$ | $\frac{ps}{1-(1-p)s}$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ |
| $\text{NB}(r, p)$ | $\left[\frac{ps}{1-(1-p)s}\right]^r$ | $\frac{r}{p}$ | $\frac{r(1-p)}{p^2}$ |
| $\text{Po}(\lambda)$ | $e^{\lambda(s-1)}$ | $\lambda$ | $\lambda$ |

## 파이썬으로 확인하기

```python
import numpy as np
from scipy.misc import derivative

pgfs = {
    "Bernoulli(0.4)": lambda s: 0.6 + 0.4 * s,
    "B(10, 0.4)":     lambda s: (0.6 + 0.4 * s)**10,
    "Geo(0.3)":       lambda s: 0.3 * s / (1 - 0.7 * s),
    "Po(5)":          lambda s: np.exp(5 * (s - 1)),
}

exact = {
    "Bernoulli(0.4)": (0.4, 0.24),
    "B(10, 0.4)":     (4.0, 2.4),
    "Geo(0.3)":       (10/3, 70/9),
    "Po(5)":          (5.0, 5.0),
}

for name, G in pgfs.items():
    EX = derivative(G, 1, n=1, dx=1e-6)
    EXX1 = derivative(G, 1, n=2, dx=1e-6)
    VarX = EXX1 + EX - EX**2
    mu, var = exact[name]
    print(f"{name}:  E[X]={EX:.4f} (exact {mu:.4f}),  Var={VarX:.4f} (exact {var:.4f})")
```

## 연습문제

**연습문제 1.**
$X \sim \text{Po}(3)$ 과 $Y \sim \text{Po}(7)$ 이 독립이라 하자.

**(a)** 확률생성함수의 곱의 법칙을 써서 $G_{X+Y}(s)$ 를 계산하여라.

**(b)** $X + Y$ 의 분포를 알아내어라.

**(c)** $E[X + Y]$ 와 $\text{Var}(X + Y)$ 가 그 답과 들어맞는지 확인하여라.

??? success "연습문제 1 풀이"

    **(a)** $G_{X+Y}(s) = e^{3(s-1)} \cdot e^{7(s-1)} = e^{10(s-1)}$ 이다.

    **(b)** 이것은 $\text{Po}(10)$ 의 확률생성함수이므로 $X + Y \sim \text{Po}(10)$ 이다.

    **(c)** $E[X+Y] = 3 + 7 = 10$ 이고 $\text{Var}(X+Y) = 3 + 7 = 10$ 이므로 둘 다 $\text{Po}(10)$ 과 들어맞는다.
