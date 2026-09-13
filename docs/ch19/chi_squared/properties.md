# 성질, 평균, 분산

## 카이제곱분포의 적률생성함수

$\chi^2_d \sim \Gamma(d/2, 1/2)$ 이므로 적률생성함수를 직접 계산할 수 있다. $\lambda = 1/2 - t$ 로 치환하면 다음과 같다.

$$\varphi_{\chi^2_d}(t) = E[e^{tX}] = \int_0^{\infty} e^{tx} \frac{(1/2)^{d/2}}{\Gamma(d/2)} x^{d/2 - 1} e^{-x/2}\, dx$$

$$= \int_0^{\infty} \frac{(1/2)^{d/2}}{\Gamma(d/2)} x^{d/2 - 1} e^{-(1/2 - t)x}\, dx$$

$$= \left(\frac{1}{\sqrt{1 - 2t}}\right)^d \int_0^{\infty} \underbrace{\frac{\lambda (\lambda x)^{d/2 - 1} e^{-\lambda x}}{\Gamma(d/2)}}_{\Gamma(d/2, \lambda) \text{ 의 밀도함수}}\, dx = \left(\frac{1}{\sqrt{1 - 2t}}\right)^d$$

따라서 다음을 얻는다.

$$\varphi_{\chi^2_d}(t) = (1 - 2t)^{-d/2}, \quad t < \frac{1}{2}$$

## 평균과 분산

$\chi^2_d \sim \Gamma(d/2, 1/2)$ 이므로 평균과 분산은 감마분포에서 그대로 따라 나온다.

| 분포 | 평균 | 분산 |
|-------------|------|----------|
| $\text{Geo}(p)$ | $1/p$ | $q/p^2$ |
| $\frac{1}{n}\text{Geo}(p)$ | $1/(np)$ | $q/(np)^2$ |
| $\text{Exp}(\lambda) = \Gamma(1, \lambda)$ | $1/\lambda$ | $1/\lambda^2$ |
| $\Gamma(n, \lambda)$ | $n/\lambda$ | $n/\lambda^2$ |
| $\Gamma(\alpha, \lambda)$ | $\alpha/\lambda$ | $\alpha/\lambda^2$ |
| $\chi^2_1 = \Gamma(1/2, 1/2)$ | $\frac{1/2}{1/2} = 1$ | $\frac{1/2}{(1/2)^2} = 2$ |
| $\chi^2_d = \Gamma(d/2, 1/2)$ | $d$ | $2d$ |

### 직접 확인하기

**평균:** 각 $Z_i^2$ 에 대하여 $E[Z_i^2] = \text{Var}(Z_i) + (E[Z_i])^2 = 1 + 0 = 1$ 이다. 기댓값의 선형성에 따라

$$E[\chi^2_d] = \sum_{i=1}^d E[Z_i^2] = d$$

이다.

**분산:** 표준정규분포에서 $E[Z^4] = 3$ 이므로 각 $Z_i^2$ 에 대하여 $\text{Var}(Z_i^2) = E[Z_i^4] - (E[Z_i^2])^2 = 3 - 1 = 2$ 이다. 독립성에 따라

$$\text{Var}(\chi^2_d) = \sum_{i=1}^d \text{Var}(Z_i^2) = 2d$$

이다.

## 성질 요약

| 성질 | 값 |
|----------|-------|
| 밀도함수 | $x > 0$ 일 때 $\frac{(1/2)^{d/2}}{\Gamma(d/2)} x^{d/2-1} e^{-x/2}$ |
| 적률생성함수 | $t < 1/2$ 일 때 $(1 - 2t)^{-d/2}$ |
| 평균 | $d$ |
| 분산 | $2d$ |
| 최빈값 | $\max(d - 2, \, 0)$ |
| 왜도 | $\sqrt{8/d}$ |

!!! note "카이제곱분포의 모양"
    $d$ 가 작으면 분포가 오른쪽으로 크게 치우친다. $d$ 가 커질수록 왜도가 $1/\sqrt{d}$ 에 비례하여 줄어들고, $\chi^2_d$ 가 i.i.d. 확률변수 $d$ 개의 합이므로 중심극한정리에 따라 분포가 정규분포에 가까워진다.

## 연습문제

**연습문제 1.**
확률변수 $W$ 의 적률생성함수가 $\varphi_W(t) = (1 - 2t)^{-5}$ 이다. 이 분포가 무엇인지 밝혀라.

??? success "연습문제 1 풀이"
    $(1 - 2t)^{-5} = (1 - 2t)^{-d/2}$ 에서 $d = 10$ 이다. 따라서 $W \sim \chi^2_{10}$ 이다.
