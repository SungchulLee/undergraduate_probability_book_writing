# 순서통계량의 결합분포

## 모든 순서통계량의 결합 확률밀도함수

!!! info "모든 순서통계량의 결합밀도"
    $X_1, \ldots, X_n$ 이 확률밀도함수 $f$ 와 누적분포함수 $F$ 를 갖는 i.i.d. 확률변수라 하자. $(X_{(1)}, X_{(2)}, \ldots, X_{(n)})$ 의 결합 확률밀도함수는 다음과 같다.

    $$f_{X_{(1)}, \ldots, X_{(n)}}(x_1, \ldots, x_n) = n! \prod_{i=1}^n f(x_i), \quad x_1 < x_2 < \cdots < x_n$$

    그 밖에서는 0이다.

## 유도

독립성에 따라 **원래**의(순서를 매기지 않은) 표본 $(X_1, \ldots, X_n)$ 의 결합 확률밀도함수는 $\prod_{i=1}^n f(x_i)$ 이다.

$(x_1, \ldots, x_n)$ 을 늘어놓는 순열 가운데 정확히 $n!$ 개가 같은 순서열 $x_{(1)} < \cdots < x_{(n)}$ 을 만들어 낸다. 원래 표본의 각 순열이 순서를 매긴 표본의 같은 점으로 옮겨 가는 것이다. 따라서 순서를 매긴 표본의 밀도는 $n!$ 배 커지지만, 영역이 $x_1 < x_2 < \cdots < x_n$ 으로 제한된다. $\square$

**앞뒤가 맞는지 확인.** 영역 $x_1 < x_2 < \cdots < x_n$ 위에서 적분하면 다음과 같다.

$$\int \cdots \int_{x_1 < \cdots < x_n} n! \prod_{i=1}^n f(x_i)\, dx_1 \cdots dx_n = n! \cdot \frac{1}{n!} = 1$$

$1/n!$ 이라는 인수는 대칭성에 따라 영역 $\{x_1 < \cdots < x_n\}$ 이 전체 공간의 $1/n!$ 이라는 사실에서 나온다.

## 순서통계량 두 개의 결합 확률밀도함수

!!! info "$i < j$ 일 때 $(X_{(i)}, X_{(j)})$ 의 결합밀도"

    $$f_{X_{(i)}, X_{(j)}}(s, t) = \frac{n!}{(i-1)!(j-i-1)!(n-j)!} [F(s)]^{i-1} [F(t) - F(s)]^{j-i-1} [1-F(t)]^{n-j} f(s)\,f(t)$$

    단, $s < t$ 이다.

### 다항계수를 이용한 유도

$s < t$ 에 대하여 $X_{(i)} \approx s$ 이고 $X_{(j)} \approx t$ 이려면 $n$ 개의 관측값이 다섯 무리로 갈라져야 한다.

1. **$i - 1$ 개의 관측값**이 $s$ 아래에 있다: 확률 $[F(s)]^{i-1}$
2. **1개의 관측값**이 $s$ 에 있다: 확률 $f(s)\,ds$
3. **$j - i - 1$ 개의 관측값**이 $s$ 와 $t$ 사이에 있다: 확률 $[F(t) - F(s)]^{j-i-1}$
4. **1개의 관측값**이 $t$ 에 있다: 확률 $f(t)\,dt$
5. **$n - j$ 개의 관측값**이 $t$ 위에 있다: 확률 $[1 - F(t)]^{n-j}$

다항계수 $\frac{n!}{(i-1)!\cdot 1!\cdot (j-i-1)!\cdot 1!\cdot (n-j)!}$ 이 관측값을 이 무리들에 나누어 넣는 방법의 수를 센다.

## 특별한 경우: 최솟값과 최댓값의 결합 확률밀도함수

$i = 1$, $j = n$ 으로 놓으면 다음과 같다.

$$f_{X_{(1)}, X_{(n)}}(s, t) = n(n-1)[F(t) - F(s)]^{n-2} f(s)\,f(t), \quad s < t$$

??? example "예: 균등분포 표본의 범위"
    $F(x) = x$ 이고 $f(x) = 1$ 인 $X_i \overset{\text{iid}}{\sim} U(0, 1)$ 에 대하여 다음이 성립한다.

    $$f_{X_{(1)}, X_{(n)}}(s, t) = n(n-1)(t - s)^{n-2}, \quad 0 < s < t < 1$$

    범위 $R = X_{(n)} - X_{(1)}$ 의 확률밀도함수는 다음과 같다.

    $$f_R(r) = n(n-1)r^{n-2}(1-r), \quad 0 < r < 1$$

    이는 $t = s + r$ 로 치환한 뒤 결합밀도를 $s$ 에 대하여 적분하여 얻는다.

## 파이썬 구현

```python
import numpy as np
from scipy import stats

np.random.seed(42)
n, n_sim = 5, 100000

# 최솟값과 최댓값을 함께 모의실험한다
samples = np.sort(np.random.uniform(0, 1, (n_sim, n)), axis=1)
mins = samples[:, 0]
maxs = samples[:, -1]
ranges = maxs - mins

# 범위의 분포 확인
print(f"Range of {n} U(0,1) samples:")
print(f"  E[R] = {ranges.mean():.4f}  (theory {(n-1)/(n+1):.4f})")

# 특정한 점에서 결합밀도 확인
# U(0,1) 에 대하여 f(s,t) = n(n-1)(t-s)^(n-2)
s, t = 0.2, 0.8
joint_theory = n * (n-1) * (t - s)**(n-2)
print(f"\nJoint density f(0.2, 0.8) = {joint_theory:.4f}")

# 최솟값과 최댓값의 공분산
cov = np.cov(mins, maxs)[0, 1]
cov_theory = 1 / ((n+1)**2 * (n+2))
print(f"\nCov(X_(1), X_(n)) = {cov:.6f}  (theory {cov_theory:.6f})")
```

**실행 결과:**
```
Range of 5 U(0,1) samples:
  E[R] = 0.6662  (theory 0.6667)

Joint density f(0.2, 0.8) = 7.2000

Cov(X_(1), X_(n)) = 0.003937  (theory 0.003968)
```

## 연습문제

**연습문제 1.**
$U_1, \ldots, U_4 \overset{\text{iid}}{\sim} U(0, 1)$ 이라 하자. $(U_{(1)}, U_{(4)})$ 의 결합 확률밀도함수를 적고 $E[U_{(4)} - U_{(1)}]$ 를 구하여라.

??? success "연습문제 1 풀이"
    $i = 1$, $j = 4$, $n = 4$, $F(x) = x$, $f(x) = 1$ 을 넣으면 다음을 얻는다.

    $$f_{U_{(1)}, U_{(4)}}(s, t) = \frac{4!}{0!\cdot 2!\cdot 0!}(t - s)^2 = 12(t - s)^2, \quad 0 < s < t < 1$$

    $$E[U_{(4)} - U_{(1)}] = E[U_{(4)}] - E[U_{(1)}] = \frac{4}{5} - \frac{1}{5} = \frac{3}{5}$$

    다른 방법으로는 범위 $R = U_{(4)} - U_{(1)}$ 에 대하여 $E[R] = \frac{n-1}{n+1} = \frac{3}{5}$ 이다.
