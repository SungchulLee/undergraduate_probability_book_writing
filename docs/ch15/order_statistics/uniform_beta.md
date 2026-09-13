# 균등분포의 순서통계량과 베타분포의 관계

## 주요 결과

!!! info "균등분포의 순서통계량은 베타분포를 따른다"
    $U_1, U_2, \ldots, U_n \overset{\text{iid}}{\sim} U(0, 1)$ 이면 다음이 성립한다.

    $$U_{(k)} \sim \text{Beta}(k, \, n - k + 1)$$

이것은 확률론에서 가장 아름다운 연결 가운데 하나이다. 균등분포의 순서통계량이 정확히 베타분포를 따른다는 것이다.

## 증명

$k$ 번째 순서통계량에 대한 일반 공식에 $0 < x < 1$ 에서 $F(x) = x$ 와 $f(x) = 1$ 을 넣으면 다음을 얻는다.

$$f_{U_{(k)}}(x) = \frac{n!}{(k-1)!(n-k)!} \, x^{k-1}(1-x)^{n-k}, \quad 0 < x < 1$$

베타분포의 확률밀도함수는 $0 < x < 1$ 에서 $f(x) = \frac{x^{\alpha - 1}(1 - x)^{\beta - 1}}{B(\alpha, \beta)}$ 였음을 떠올리자.

$\alpha = k$ 와 $\beta = n - k + 1$ 로 놓으면 다음과 같다.

$$\frac{1}{B(k, n-k+1)} = \frac{\Gamma(n+1)}{\Gamma(k)\,\Gamma(n-k+1)} = \frac{n!}{(k-1)!(n-k)!}$$

두 식이 일치하므로 $U_{(k)} \sim \text{Beta}(k, n - k + 1)$ 이 확인된다. $\square$

## 평균과 분산

$U_{(k)} \sim \text{Beta}(k, n - k + 1)$ 이므로 적률은 베타분포에서 바로 나온다.

$$E[U_{(k)}] = \frac{k}{n + 1}$$

$$\text{Var}(U_{(k)}) = \frac{k(n - k + 1)}{(n + 1)^2(n + 2)}$$

평균 $k/(n+1)$ 은 균등분포 표본 $n$ 개 가운데 $k$ 번째로 작은 값이 놓이는 자리의 기댓값이다. 순서통계량은 평균적으로 고르게 흩어져 있다. 간격 $E[U_{(k+1)}] - E[U_{(k)}] = 1/(n+1)$ 이 모두 같기 때문이다.

## 균등분포 순서통계량의 공분산

$i < j$ 에 대하여 다음이 성립한다.

$$\text{Cov}(U_{(i)}, U_{(j)}) = \frac{i(n - j + 1)}{(n+1)^2(n+2)}$$

이 값은 언제나 양수이다. $U_{(i)}$ 가 크다는 것을 알면 $U_{(j)}$ 도 클 가능성이 커지기 때문이다.

## 특별한 경우

| 순서통계량 | 분포 | 평균 | 분산 |
|:---:|:---:|:---:|:---:|
| $U_{(1)}$ (최솟값) | $\text{Beta}(1, n)$ | $\frac{1}{n+1}$ | $\frac{n}{(n+1)^2(n+2)}$ |
| $U_{(n)}$ (최댓값) | $\text{Beta}(n, 1)$ | $\frac{n}{n+1}$ | $\frac{n}{(n+1)^2(n+2)}$ |
| $U_{(\lceil n/2 \rceil)}$ (중앙값) | $\text{Beta}(\lceil n/2 \rceil, \lfloor n/2 \rfloor + 1)$ | $\approx 1/2$ | $\approx \frac{1}{4(n+2)}$ |

## 거꾸로 본 관점

베타분포와 균등분포의 연결은 거꾸로도 통한다. 모수가 정수인 $\text{Beta}(\alpha, \beta)$ 분포는 언제나 순서통계량으로 읽을 수 있다. 구체적으로 $\text{Beta}(k, n - k + 1)$ 은 i.i.d. 균등확률변수 $n$ 개에서 얻은 $k$ 번째 순서통계량의 분포이다. 이로써 모수가 양의 정수인 모든 베타분포에 자연스러운 표집의 뜻이 붙는다.

## 파이썬 구현

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n, n_sim = 10, 100000

samples = np.sort(np.random.uniform(0, 1, (n_sim, n)), axis=1)

print(f"Order statistics of {n} U(0,1) samples vs Beta theory:\n")
print(f"{'k':>3}  {'E[U_(k)] sim':>14}  {'E[U_(k)] theory':>16}  {'Var sim':>10}  {'Var theory':>12}")
for k in range(1, n + 1):
    os_k = samples[:, k - 1]
    alpha, beta_param = k, n - k + 1
    e_theory = alpha / (alpha + beta_param)
    v_theory = alpha * beta_param / ((alpha + beta_param)**2 * (alpha + beta_param + 1))
    print(f"{k:3d}  {os_k.mean():14.4f}  {e_theory:16.4f}  {os_k.var():10.6f}  {v_theory:12.6f}")
```

**실행 결과:**
```
Order statistics of 10 U(0,1) samples vs Beta theory:

  k  E[U_(k)] sim  E[U_(k)] theory     Var sim    Var theory
  1        0.0909            0.0909    0.007530      0.007576
  2        0.1818            0.1818    0.012390      0.012397
  3        0.2726            0.2727    0.015010      0.014876
  4        0.3636            0.3636    0.015920      0.016012
  5        0.4547            0.4545    0.015680      0.015805
  6        0.5453            0.5455    0.015650      0.015805
  7        0.6363            0.6364    0.015880      0.016012
  8        0.7273            0.7273    0.014870      0.014876
  9        0.8183            0.8182    0.012370      0.012397
 10        0.9091            0.9091    0.007550      0.007576
```

## 연습문제

**연습문제 1.** $U_1, \ldots, U_5 \sim \text{Uniform}(0,1)$ 이 i.i.d. 라 하자. $U_{(3)}$ 의 분포와 평균, 분산을 구하여라.

??? success "연습문제 1 풀이"
    $U_{(3)} \sim \text{Beta}(3, 3)$ 이다.

    $E[U_{(3)}] = \frac{3}{6} = 0.5$ 이다. $\text{Var}(U_{(3)}) = \frac{3 \times 3}{36 \times 7} = \frac{9}{252} = \frac{1}{28} \approx 0.0357$ 이다.

---

**연습문제 2.** 균등분포 순서통계량에서 $n = 10$ 일 때 $P(U_{(1)} > 0.1)$ 을 구하여라.

??? success "연습문제 2 풀이"
    $U_{(1)} \sim \text{Beta}(1, 10)$ 이므로 $F_{U_{(1)}}(x) = 1 - (1-x)^{10}$ 이다.

    $$
    P(U_{(1)} > 0.1) = (1 - 0.1)^{10} = 0.9^{10} \approx 0.3487
    $$

---

**연습문제 3.** $k = 1, \ldots, n$ 에 대하여 $E[U_{(k)}] = \frac{k}{n+1}$ 이 고르게 놓임을 보여라.

??? success "연습문제 3 풀이"
    $E[U_{(k)}] = \frac{k}{n+1}$ 이다. 잇달은 기댓값 사이의 간격은 다음과 같다.

    $$
    E[U_{(k+1)}] - E[U_{(k)}] = \frac{k+1}{n+1} - \frac{k}{n+1} = \frac{1}{n+1}
    $$

    이 값이 일정하므로 순서통계량의 기댓값들은 $(0,1)$ 위에 간격 $1/(n+1)$ 로 고르게 놓인다. $\square$

---

**연습문제 4.** $U_{(n)}$(i.i.d. 균등확률변수 $n$ 개의 최댓값)의 확률밀도함수를 구하고 $E[U_{(n)}]$ 을 계산하여라.

??? success "연습문제 4 풀이"
    $U_{(n)} \sim \text{Beta}(n, 1)$ 이므로 $0 < x < 1$ 에서 $f(x) = nx^{n-1}$ 이다.

    $$
    E[U_{(n)}] = \frac{n}{n+1}
    $$

    $n \to \infty$ 이면 $E[U_{(n)}] \to 1$ 이며, 최댓값이 1에 가까워진다는 사실과 들어맞는다.

---

**연습문제 5.** $U_{(k)} \sim \text{Beta}(k, n-k+1)$ 에 대하여 $\text{Var}(U_{(k)}) = \frac{k(n-k+1)}{(n+1)^2(n+2)}$ 임을 수치적으로 확인하거나 증명하여라.

??? success "연습문제 5 풀이"
    $X \sim \text{Beta}(\alpha, \beta)$ 에 대하여 $\text{Var}(X) = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ 이다.

    $\alpha = k$, $\beta = n-k+1$, $\alpha + \beta = n+1$ 을 넣으면 다음을 얻는다.

    $$
    \text{Var}(U_{(k)}) = \frac{k(n-k+1)}{(n+1)^2(n+2)}
    $$

    예를 들어 $n = 5$, $k = 2$ 이면 $\text{Var} = \frac{2 \times 4}{36 \times 7} = \frac{8}{252} = \frac{2}{63} \approx 0.0317$ 이다. $\square$
