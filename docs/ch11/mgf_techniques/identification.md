# 적률생성함수로 분포 알아내기

## 전략

적률생성함수로 분포를 알아내는 방법은 세 걸음으로 이루어진다.

1. 관심 있는 확률변수(대개 합)의 적률생성함수를 **계산한다**.
2. 그 결과가 이미 아는 분포의 적률생성함수임을 **알아본다**.
3. 유일성 정리에 따라 두 분포가 같다고 **결론짓는다**.

이렇게 하면 훨씬 까다로울 수 있는 합성곱이나 누적분포함수를 직접 다루지 않아도 된다.

## 적률생성함수 참고표

| 분포 | 적률생성함수 $M_X(t)$ | 정의역 |
|:---|:---:|:---:|
| $\text{Bernoulli}(p)$ | $1 + p(e^t - 1)$ | 모든 $t$ |
| $B(n, p)$ | $[1 + p(e^t - 1)]^n$ | 모든 $t$ |
| $\text{Po}(\lambda)$ | $e^{\lambda(e^t - 1)}$ | 모든 $t$ |
| $\text{Geo}(p)$ | $\frac{pe^t}{1 - (1-p)e^t}$ | $t < -\ln(1-p)$ |
| $\text{NB}(r, p)$ | $\left[\frac{pe^t}{1-(1-p)e^t}\right]^r$ | $t < -\ln(1-p)$ |
| $\text{Exp}(\lambda)$ | $\frac{\lambda}{\lambda - t}$ | $t < \lambda$ |
| $\text{Gamma}(\alpha, \lambda)$ | $\left(\frac{\lambda}{\lambda - t}\right)^\alpha$ | $t < \lambda$ |
| $N(\mu, \sigma^2)$ | $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$ | 모든 $t$ |

## 예: 독립인 푸아송확률변수의 합

$X \sim \text{Po}(\lambda)$ 와 $Y \sim \text{Po}(\mu)$ 가 독립이라 하자.

**1단계.** 계산한다.

$$M_{X+Y}(t) = e^{\lambda(e^t - 1)} \cdot e^{\mu(e^t - 1)} = e^{(\lambda + \mu)(e^t - 1)}$$

**2단계.** 알아본다. 이것은 $\text{Po}(\lambda + \mu)$ 의 적률생성함수이다.

**3단계.** 결론짓는다. $X + Y \sim \text{Po}(\lambda + \mu)$ 이다.

## 예: 독립인 정규확률변수의 합

$X \sim N(\mu_1, \sigma_1^2)$ 와 $Y \sim N(\mu_2, \sigma_2^2)$ 가 독립이라 하자.

**1단계.** 계산한다.

$$M_{X+Y}(t) = e^{\mu_1 t + \frac{1}{2}\sigma_1^2 t^2} \cdot e^{\mu_2 t + \frac{1}{2}\sigma_2^2 t^2} = e^{(\mu_1+\mu_2)t + \frac{1}{2}(\sigma_1^2 + \sigma_2^2)t^2}$$

**2단계.** 알아본다. 이것은 $N(\mu_1 + \mu_2, \, \sigma_1^2 + \sigma_2^2)$ 의 적률생성함수이다.

**3단계.** 결론짓는다. $X + Y \sim N(\mu_1 + \mu_2, \, \sigma_1^2 + \sigma_2^2)$ 이다.

## 예: 비율 모수가 같은 독립인 감마확률변수의 합

$X \sim \text{Gamma}(\alpha_1, \lambda)$ 와 $Y \sim \text{Gamma}(\alpha_2, \lambda)$ 가 독립이라 하자.

**1단계.** 계산한다.

$$M_{X+Y}(t) = \left(\frac{\lambda}{\lambda - t}\right)^{\alpha_1} \cdot \left(\frac{\lambda}{\lambda - t}\right)^{\alpha_2} = \left(\frac{\lambda}{\lambda - t}\right)^{\alpha_1 + \alpha_2}$$

**2단계.** 알아본다. 이것은 $\text{Gamma}(\alpha_1 + \alpha_2, \lambda)$ 의 적률생성함수이다.

**3단계.** 결론짓는다. $X + Y \sim \text{Gamma}(\alpha_1 + \alpha_2, \lambda)$ 이다.

!!! warning "비율 모수가 같아야 한다"
    감마분포의 가법성 결과는 비율 $\lambda$ 가 같아야 성립한다. $\lambda_1 \neq \lambda_2$ 인 $X \sim \text{Gamma}(\alpha_1, \lambda_1)$ 와 $Y \sim \text{Gamma}(\alpha_2, \lambda_2)$ 라면, 그 합은 감마분포를 따르지 **않는다**.

## 예: p가 같은 독립인 이항확률변수의 합

$X \sim B(n_1, p)$ 와 $Y \sim B(n_2, p)$ 가 독립이라 하자.

$$M_{X+Y}(t) = [1 + p(e^t - 1)]^{n_1} \cdot [1 + p(e^t - 1)]^{n_2} = [1 + p(e^t - 1)]^{n_1 + n_2}$$

이것은 $B(n_1 + n_2, p)$ 의 적률생성함수이므로 $X + Y \sim B(n_1 + n_2, p)$ 이다.

## 닫힘 성질 요약

| 분포족 | 조건 | 결과 |
|:---|:---|:---|
| 푸아송 | 독립 | $\text{Po}(\lambda) + \text{Po}(\mu) = \text{Po}(\lambda + \mu)$ |
| 정규 | 독립 | $N(\mu_1, \sigma_1^2) + N(\mu_2, \sigma_2^2) = N(\mu_1+\mu_2, \sigma_1^2+\sigma_2^2)$ |
| 감마 | 독립, 같은 $\lambda$ | $\text{Gamma}(\alpha_1, \lambda) + \text{Gamma}(\alpha_2, \lambda) = \text{Gamma}(\alpha_1+\alpha_2, \lambda)$ |
| 이항 | 독립, 같은 $p$ | $B(n_1, p) + B(n_2, p) = B(n_1+n_2, p)$ |
| 음이항 | 독립, 같은 $p$ | $\text{NB}(r_1, p) + \text{NB}(r_2, p) = \text{NB}(r_1+r_2, p)$ |

## 연습문제

**연습문제 1.**
$X_1, \ldots, X_{20}$ 이 i.i.d. $\text{Bernoulli}(0.3)$ 이고 $S = \sum_{i=1}^{20} X_i$ 라 하자.

**(a)** 곱의 법칙을 써서 $M_S(t)$ 를 계산하여라.

**(b)** $S$ 의 분포를 알아내어라.

**(c)** 푸아송 근사의 적률생성함수를 써서 $P(S = 0)$ 을 근사하여라.

??? success "연습문제 1 풀이"

    **(a)** $M_S(t) = [1 + 0.3(e^t - 1)]^{20} = [0.7 + 0.3e^t]^{20}$ 이다.

    **(b)** 이것은 $B(20, 0.3)$ 의 적률생성함수이므로 $S \sim B(20, 0.3)$ 이다.

    **(c)** $\lambda = np = 6$ 이므로 $P(S = 0) \approx e^{-6} \approx 0.0025$ 이다. 정확한 값은 $0.7^{20} \approx 0.0008$ 이다.
