# k번째 순서통계량의 밀도함수

## 주요 결과

!!! info "k번째 순서통계량의 밀도함수"
    $X_1, \ldots, X_n$ 이 누적분포함수 $F$ 와 확률밀도함수 $f$ 를 갖는 i.i.d. 확률변수라 하자. $X_{(k)}$ 의 확률밀도함수는 다음과 같다.

    $$f_{X_{(k)}}(x) = \frac{n!}{(k-1)!\,(n-k)!} \, [F(x)]^{k-1} \, [1 - F(x)]^{n-k} \, f(x)$$

## 다항계수를 이용한 유도

$X_{(k)}$ 가 작은 구간 $(x, x + dx)$ 안에 놓이려면 $n$ 개의 관측값이 세 무리로 갈라져야 한다.

1. **$k - 1$ 개의 관측값**이 $x$ 아래에 떨어진다. 각각의 확률은 $F(x)$ 이다
2. **1개의 관측값**이 $(x, x + dx)$ 안에 떨어진다. 확률은 $f(x)\,dx$ 이다
3. **$n - k$ 개의 관측값**이 $x + dx$ 위에 떨어진다. 각각의 확률은 $1 - F(x)$ 이다

$n$ 개의 관측값을 이 세 무리에 나누어 넣는 방법의 수는 다항계수 $\frac{n!}{(k-1)!\cdot 1!\cdot (n-k)!}$ 이다. 따라서 다음이 성립한다.

$$P(x < X_{(k)} < x + dx) = \frac{n!}{(k-1)!\cdot 1!\cdot (n-k)!} \, [F(x)]^{k-1} \, f(x)\,dx \, [1 - F(x)]^{n-k}$$

$dx$ 로 나누면 확률밀도함수를 얻는다. $\square$

## 특별한 경우 확인하기

$k = 1$ 로 놓으면 다음과 같다.

$$f_{X_{(1)}}(x) = n[1 - F(x)]^{n-1} f(x)$$

$k = n$ 으로 놓으면 다음과 같다.

$$f_{X_{(n)}}(x) = n[F(x)]^{n-1} f(x)$$

둘 다 앞 절에서 유도한 최솟값·최댓값 공식과 일치한다.

## 풀이 예제: 균등확률변수 다섯 개의 중앙값

??? example "예: U(0, 1) 표본의 중앙값"
    $n = 5$ 이고 $X_i \overset{\text{iid}}{\sim} U(0, 1)$ 이라 하자. 중앙값은 $X_{(3)}$ 이다.

    $(0, 1)$ 위에서 $F(x) = x$ 이고 $f(x) = 1$ 이므로 다음을 얻는다.

    $$f_{X_{(3)}}(x) = \frac{5!}{2!\cdot 2!} \, x^2(1-x)^2 = 30\, x^2(1-x)^2, \quad 0 < x < 1$$

    이것은 $1/2$ 에 대하여 대칭인 $\text{Beta}(3, 3)$ 의 밀도함수이다.

    $$E[X_{(3)}] = \frac{3}{6} = \frac{1}{2}, \qquad \text{Var}(X_{(3)}) = \frac{3 \cdot 3}{36 \cdot 7} = \frac{1}{28}$$

## k번째 순서통계량의 누적분포함수

누적분포함수는 불완전 베타함수로 나타낼 수 있다. $X_{(k)} \leq x$ 이려면 $n$ 개 가운데 적어도 $k$ 개가 $x$ 아래에 떨어져야 하므로 다음이 성립한다.

$$F_{X_{(k)}}(x) = \sum_{j=k}^{n} \binom{n}{j} [F(x)]^j [1 - F(x)]^{n-j}$$

이것은 $\text{Binomial}(n, F(x))$ 분포의 꼬리확률이며, 정규화된 불완전 베타함수 $I_{F(x)}(k, n - k + 1)$ 과 같다.

## 파이썬 구현

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n, k, n_sim = 5, 3, 100000

# U(0,1) 표본 5개의 중앙값을 모의실험한다
samples = np.sort(np.random.uniform(0, 1, (n_sim, n)), axis=1)
median_samples = samples[:, k - 1]

x = np.linspace(0.01, 0.99, 200)
pdf_theory = stats.beta.pdf(x, k, n - k + 1)

print(f"Median X_(3) of 5 U(0,1) samples:")
print(f"  E[X_(3)] = {median_samples.mean():.4f}  (theory 0.5000)")
print(f"  Var[X_(3)] = {median_samples.var():.4f}  (theory {1/28:.4f})")

# k=2, n=6 에 대해 일반 공식을 확인한다
n2, k2 = 6, 2
samples2 = np.sort(np.random.uniform(0, 1, (n_sim, n2)), axis=1)
os2 = samples2[:, k2 - 1]
print(f"\nX_(2) of 6 U(0,1) samples:")
print(f"  E[X_(2)] = {os2.mean():.4f}  (theory {k2/(n2+1):.4f})")
```

**실행 결과:**
```
Median X_(3) of 5 U(0,1) samples:
  E[X_(3)] = 0.5006  (theory 0.5000)
  Var[X_(3)] = 0.0355  (theory 0.0357)

X_(2) of 6 U(0,1) samples:
  E[X_(2)] = 0.2856  (theory 0.2857)
```

## 연습문제

**연습문제 1.**
i.i.d. $U(0, 1)$ 표본 $n = 7$ 개에 대하여 중앙값 $X_{(4)}$ 의 확률밀도함수를 적고, 베타함수를 써서 그 적분이 1임을 확인하여라.

??? success "연습문제 1 풀이"

    $$f_{X_{(4)}}(x) = \frac{7!}{3!\cdot 3!} x^3(1-x)^3 = 140\, x^3(1-x)^3, \quad 0 < x < 1$$

    이것은 $\text{Beta}(4, 4)$ 이므로 다음이 성립한다.

    $$\int_0^1 140\, x^3(1-x)^3\, dx = 140 \cdot B(4, 4) = 140 \cdot \frac{3!\cdot 3!}{7!} = 140 \cdot \frac{36}{5040} = 140 \cdot \frac{1}{140} = 1 \checkmark$$
