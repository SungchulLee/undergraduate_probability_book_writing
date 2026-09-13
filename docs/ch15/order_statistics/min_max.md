# 최솟값과 최댓값의 분포

## 최댓값의 누적분포함수

$X_1, \ldots, X_n$ 이 누적분포함수 $F$ 와 확률밀도함수 $f$ 를 갖는 i.i.d. 확률변수라 하자. 최댓값 $X_{(n)}$ 은 다음을 만족한다.

$$F_{X_{(n)}}(x) = P(X_{(n)} \leq x) = P(X_1 \leq x, \ldots, X_n \leq x) = [F(x)]^n$$

핵심은 독립성을 쓴 대목이다. 최댓값이 $x$ 이하인 것은 **모든** 관측값이 $x$ 이하일 때 그리고 오직 그때만이다.

!!! info "최댓값의 분포"

    $$F_{X_{(n)}}(x) = [F(x)]^n, \qquad f_{X_{(n)}}(x) = n[F(x)]^{n-1} f(x)$$

확률밀도함수는 누적분포함수를 연쇄법칙으로 미분하여 얻는다.

## 최솟값의 누적분포함수

최솟값 $X_{(1)}$ 에 대해서는 **생존함수**를 쓰는 편이 더 쉽다.

$$P(X_{(1)} > x) = P(X_1 > x, \ldots, X_n > x) = [1 - F(x)]^n$$

최솟값이 $x$ 보다 큰 것은 **모든** 관측값이 $x$ 보다 클 때 그리고 오직 그때만이다.

!!! info "최솟값의 분포"

    $$F_{X_{(1)}}(x) = 1 - [1 - F(x)]^n, \qquad f_{X_{(1)}}(x) = n[1 - F(x)]^{n-1} f(x)$$

## 예: Uniform(0, 1)

??? example "균등분포 표본의 최솟값과 최댓값"
    $X_1, \ldots, X_n \overset{\text{iid}}{\sim} U(0, 1)$ 이라 하자. 그러면 $0 < x < 1$ 에서 $F(x) = x$ 이고 $f(x) = 1$ 이다.

    **최댓값:**

    $$f_{X_{(n)}}(x) = nx^{n-1}, \quad 0 < x < 1$$

    이것은 $\text{Beta}(n, 1)$ 분포이다.

    $$E[X_{(n)}] = \frac{n}{n+1}, \qquad \text{Var}(X_{(n)}) = \frac{n}{(n+1)^2(n+2)}$$

    **최솟값:**

    $$f_{X_{(1)}}(x) = n(1-x)^{n-1}, \quad 0 < x < 1$$

    이것은 $\text{Beta}(1, n)$ 분포이다.

    $$E[X_{(1)}] = \frac{1}{n+1}, \qquad \text{Var}(X_{(1)}) = \frac{n}{(n+1)^2(n+2)}$$

    대칭성에 눈길을 주자. $E[X_{(1)}] + E[X_{(n)}] = 1$ 이다.

## 예: 지수분포

??? example "지수분포 표본의 최솟값"
    $X_1, \ldots, X_n \overset{\text{iid}}{\sim} \text{Exp}(\lambda)$ 라 하자. 그러면 $F(x) = 1 - e^{-\lambda x}$ 이다.

    $$P(X_{(1)} > x) = [e^{-\lambda x}]^n = e^{-n\lambda x}$$

    따라서 $X_{(1)} \sim \text{Exp}(n\lambda)$ 이다.

    비율이 $\lambda$ 인 i.i.d. 지수확률변수 $n$ 개의 최솟값은 비율이 $n\lambda$ 인 지수분포를 따른다. 최솟값의 기댓값은 $1/(n\lambda)$ 로, 하나하나의 평균의 $1/n$ 이다.

## 범위의 분포

**범위** $R = X_{(n)} - X_{(1)}$ 은 표본이 퍼진 정도를 잰다.

$U(0,1)$ 표본에 대하여 범위의 확률밀도함수는 다음과 같다.

$$f_R(r) = n(n-1)r^{n-2}(1-r), \quad 0 < r < 1$$

그리고 $E[R] = \frac{n-1}{n+1}$ 이다.

## 파이썬 구현

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n, n_sim = 10, 100000

# U(0,1) 표본의 최솟값과 최댓값을 모의실험한다
samples = np.random.uniform(0, 1, (n_sim, n))
mins = samples.min(axis=1)
maxs = samples.max(axis=1)

x = np.linspace(0.001, 0.999, 200)

print(f"Max of {n} U(0,1):")
print(f"  E[X_(n)] = {maxs.mean():.4f}  (theory {n/(n+1):.4f})")
print(f"Min of {n} U(0,1):")
print(f"  E[X_(1)] = {mins.mean():.4f}  (theory {1/(n+1):.4f})")
print(f"Range:")
print(f"  E[R] = {(maxs - mins).mean():.4f}  (theory {(n-1)/(n+1):.4f})")

# 지수분포의 최솟값
lam = 2
exp_samples = np.random.exponential(1/lam, (n_sim, n))
exp_mins = exp_samples.min(axis=1)
print(f"\nMin of {n} Exp({lam}):")
print(f"  E[X_(1)] = {exp_mins.mean():.4f}  (theory {1/(n*lam):.4f})")
```

**실행 결과:**
```
Max of 10 U(0,1):
  E[X_(n)] = 0.9090  (theory 0.9091)
Min of 10 U(0,1):
  E[X_(1)] = 0.0909  (theory 0.0909)
Range:
  E[R] = 0.8181  (theory 0.8182)

Min of 10 Exp(2):
  E[X_(1)] = 0.0501  (theory 0.0500)
```

## 연습문제

**연습문제 1.**
$X_1, \ldots, X_5 \overset{\text{iid}}{\sim} \text{Exp}(2)$ 라 하자.

(a) $X_{(1)} = \min(X_1, \ldots, X_5)$ 의 분포를 구하여라.

(b) $P(X_{(1)} > 0.5)$ 를 구하여라.

??? success "연습문제 1 풀이"
    (a) $X_{(1)} \sim \text{Exp}(5 \cdot 2) = \text{Exp}(10)$

    (b) $P(X_{(1)} > 0.5) = e^{-10 \cdot 0.5} = e^{-5} \approx 0.0067$
