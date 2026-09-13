# 베르누이에서 이항분포로: 모의실험

이 모의실험은 베르누이분포와 이항분포 사이의 근본적인 관계를 눈으로 보여 준다. 서로 독립인 $\text{Bernoulli}(p)$ 확률변수 $n$ 개를 만들어 더하면 그 분포가 $\text{Bin}(n, p)$ 의 확률질량함수와 일치함을 실험으로 확인한다. 모의실험으로 얻은 히스토그램과 이론적인 확률질량함수가 바싹 들어맞는 모습은 이항분포가 베르누이 시행을 되풀이하는 데에서 자연스럽게 생겨남을 보여 준다.

## 배경

**이항분포**는 서로 독립인 베르누이 시행의 합으로 나타난다. $X_1, X_2, \ldots, X_n$ 이 각각 $X_i \sim \text{Bernoulli}(p)$ 를 따르는 서로 독립인 확률변수이면, 성공 횟수의 총합

$$
S = X_1 + X_2 + \cdots + X_n
$$

은 $\text{Bin}(n, p)$ 분포를 따른다. $S$ 의 확률질량함수는 다음과 같다.

$$
P(S = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n
$$

이 항등식은 합성곱 공식을 써서 $n$ 에 대한 수학적 귀납법으로 증명할 수 있지만, 직관적으로도 알 수 있다. 성공이 $k$ 번, 실패가 $n - k$ 번 나오는 특정한 시행열 하나의 확률은 $p^k(1-p)^{n-k}$ 이고, 그런 시행열이 $\binom{n}{k}$ 개 있기 때문이다.

모의실험은 이를 곧바로 실험으로 확인해 준다. 베르누이 표본 $n$ 개를 여러 번 뽑아 묶음마다 더한 뒤, 그렇게 얻은 도수분포를 이론적인 확률질량함수와 견주어 본다. 모의실험 횟수가 늘어나면 **큰수의 법칙**에 따라 실험적인 도수가 참된 확률로 수렴한다.

## 코드

```python
"""베르누이 확률변수의 합이 이항분포를 따름을 보인다."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

n = 3
p = 0.7
n_sim = 10_000

samples_bernoulli = np.random.binomial(1, p, size=(n, n_sim))
samples_binomial = samples_bernoulli.sum(axis=0)

x = np.arange(n + 1)
pmf = stats.binom(n, p).pmf(x)

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x, pmf, alpha=0.4, label="Theoretical PMF", width=0.4)
ax.hist(
    samples_binomial,
    bins=np.arange(-0.5, n + 1.5),
    density=True,
    histtype="step",
    linewidth=2,
    color="red",
    label=f"Sum of {n} Bernoulli({p}) samples",
)
ax.set_title(f"Binomial B({n}, {p}): Theory vs Simulation", fontsize=14)
ax.set_xlabel("k")
ax.set_ylabel("Probability")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("from_bernoulli_to_binomial.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 실행 결과

이 스크립트는 이론적인 $\text{Bin}(3, 0.7)$ 확률질량함수(파란 막대)와, 서로 독립인 $\text{Bernoulli}(0.7)$ 확률변수 셋의 합을 10,000번 모의실험하여 얻은 정규화된 히스토그램(빨간 계단 외곽선)을 견주는 그림을 그려 낸다. 이론적인 확률은 다음과 같다.

| $k$ | $P(S = k)$ | 근삿값 |
|-----|-------------|-------------------|
| 0   | $(0.3)^3$   | 0.027             |
| 1   | $3(0.7)(0.3)^2$ | 0.189         |
| 2   | $3(0.7)^2(0.3)$ | 0.441         |
| 3   | $(0.7)^3$   | 0.343             |

모의실험으로 얻은 도수는 이 이론값들과 바싹 들어맞는다.

## 뜻풀이

그림은 이론적인 결과를 확인해 준다. **서로 독립인 베르누이 확률변수의 합은 이항분포를 따른다.** 눈여겨볼 점이 몇 가지 있다.

- 히스토그램(10,000번 되풀이하여 얻은 실험적 분포)은 이론적인 확률질량함수 막대와 거의 겹쳐, 항등식 $S = X_1 + X_2 + X_3 \sim \text{Bin}(3, 0.7)$ 을 확인해 준다.
- $p = 0.7 > 0.5$ 이므로 분포는 **왼쪽으로 치우쳐 있다**. 표준적인 약속에 따르면 이는 *꼬리*가 왼쪽(작은 $k$ 쪽)으로 뻗고 확률의 대부분은 큰 $k$ 쪽에 놓인다는 뜻이다. 최빈값은 $k = 2$ 로, 공식 $\lfloor (n+1)p \rfloor = \lfloor 2.8 \rfloor = 2$ 와 들어맞는다.
- 표본이 $n_{\text{sim}} = 10{,}000$ 개이므로 상대도수는 대략 $1/\sqrt{10{,}000} = 0.01$ 정도의 정확도를 가지며, 그래서 막대와 히스토그램의 차이가 작지만 눈에 띈다.
- `n_sim` 을 늘리면 그 틈이 더 좁아지는데, 이것이 큰수의 법칙이다. `n`(베르누이 시행의 횟수)을 늘리면 더 폭이 넓은 이항분포가 나오고, $n$ 이 어느 정도 커지면 그 모양이 종 모양에 가까워지기 시작한다. 이는 뒤에서 **중심극한정리**로 설명하게 될 현상이다.

## 연습문제

**연습문제 1.** 모의실험을 고쳐 $n = 10$, $p = 0.5$ 로 하여라. 그렇게 얻은 이항분포의 이론적인 평균과 분산을 구하고, 모의실험에서 나온 표본평균과 표본분산이 그 값에 가까운지 확인하여라.

??? note "풀이"

    $n = 10$, $p = 0.5$ 이면 분포는 $\text{Bin}(10, 0.5)$ 이다.

    - 이론적인 평균: $E[S] = np = 10 \times 0.5 = 5$.
    - 이론적인 분산: $\text{Var}(S) = npq = 10 \times 0.5 \times 0.5 = 2.5$.

    파이썬에서 `samples_binomial` 을 만든 뒤 다음과 같이 한다.

    ```python
    n, p = 10, 0.5
    samples_bernoulli = np.random.binomial(1, p, size=(n, 10_000))
    samples_binomial = samples_bernoulli.sum(axis=0)
    print(f"Sample mean: {samples_binomial.mean():.3f}")      # ≈ 5.0
    print(f"Sample variance: {samples_binomial.var(ddof=1):.3f}")  # ≈ 2.5
    ```

    10,000번 모의실험하면 표본평균은 5에, 표본분산은 2.5에 가깝게 나와 이론 공식 $E[S] = np$ 와 $\text{Var}(S) = npq$ 를 확인해 준다.

---

**연습문제 2.** $n = 3$, $p = 0.7$ 일 때 $P(S \ge 2)$ 를 확률질량함수 공식으로 구하고, 모의실험 표본 가운데 $S \ge 2$ 인 비율을 세어서도 구하여라.

??? note "풀이"

    확률질량함수에서 구하면 다음과 같다.

    $$
    P(S \ge 2) = P(S = 2) + P(S = 3) = \binom{3}{2}(0.7)^2(0.3) + \binom{3}{3}(0.7)^3
    $$

    $$
    = 3(0.49)(0.3) + (0.343) = 0.441 + 0.343 = 0.784
    $$

    모의실험에서는 다음과 같이 구한다.

    ```python
    empirical = np.mean(samples_binomial >= 2)
    print(f"Simulated P(S >= 2): {empirical:.4f}")  # ≈ 0.784
    ```

    모의실험으로 얻은 비율은 0.784에 가까워야 한다.

---

**연습문제 3.** $X_1, X_2, \ldots, X_n$ 이 서로 독립인 $\text{Bernoulli}(p)$ 확률변수이면 $S = \sum_{i=1}^n X_i$ 의 확률질량함수가 $P(S = k) = \binom{n}{k} p^k (1-p)^{n-k}$ 임을 $n$ 에 대한 수학적 귀납법으로 증명하여라.

??? note "풀이"

    **출발점** ($n = 1$): $S = X_1 \sim \text{Bernoulli}(p)$ 이므로 $P(S = 0) = 1 - p$, $P(S = 1) = p$ 이다. 이는 $k = 0, 1$ 에 대한 $\binom{1}{k} p^k (1-p)^{1-k}$ 와 일치한다.

    **귀납 단계**: $S_{n-1} = X_1 + \cdots + X_{n-1} \sim \text{Bin}(n-1, p)$ 라고 가정하자. $X_n$ 이 $S_{n-1}$ 과 독립이므로 합성곱 공식에 따라 다음을 얻는다.

    $$
    P(S_n = k) = P(S_{n-1} = k) \cdot P(X_n = 0) + P(S_{n-1} = k-1) \cdot P(X_n = 1)
    $$

    $$
    = \binom{n-1}{k} p^k (1-p)^{n-1-k} \cdot (1-p) + \binom{n-1}{k-1} p^{k-1} (1-p)^{n-k} \cdot p
    $$

    $$
    = p^k (1-p)^{n-k} \left[ \binom{n-1}{k} + \binom{n-1}{k-1} \right]
    $$

    파스칼 항등식에 따라 $\binom{n-1}{k} + \binom{n-1}{k-1} = \binom{n}{k}$ 이므로 다음이 성립한다.

    $$
    P(S_n = k) = \binom{n}{k} p^k (1-p)^{n-k}
    $$

    이로써 귀납법이 끝난다. $\square$

---

**연습문제 4.** 이 코드는 `np.random.binomial(1, p, ...)` 로 베르누이 표본을 만든다. `binomial(1, p)` 를 부르면 왜 베르누이 확률변수가 나오는지 설명하고, `np.random.uniform` 을 써서 베르누이 표본을 만드는 다른 방법을 서술하여라.

??? note "풀이"

    함수 `np.random.binomial(n, p)` 는 $\text{Bin}(n, p)$ 에서 표본을 뽑는다. $n = 1$ 이면 이는 바로 $\text{Bin}(1, p) = \text{Bernoulli}(p)$ 이며, 확률 $p$ 로 1을, 확률 $1-p$ 로 0을 돌려준다.

    균등난수를 쓰는 다른 방법은 **역변환**의 생각을 이용한다. $\text{Uniform}(0, 1)$ 확률변수 $U$ 는 $P(U \le p) = p$ 를 만족하므로 다음과 같이 할 수 있다.

    ```python
    U = np.random.uniform(size=(n, n_sim))
    samples_bernoulli = (U < p).astype(int)
    ```

    `U < p` 의 각 성분은 확률 $p$ 로 `True`, 확률 $1 - p$ 로 `False` 이다. 이를 `int` 로 바꾸면 각각 1과 0이 되어, 바로 $\text{Bernoulli}(p)$ 표본이 된다.

---

**연습문제 5.** 이 모의실험의 틀을 써서, 서로 독립인 $X \sim \text{Bin}(n_1, p)$ 와 $Y \sim \text{Bin}(n_2, p)$ 에 대하여 합 $X + Y \sim \text{Bin}(n_1 + n_2, p)$ 임을 실험으로 확인하여라.

??? note "풀이"

    $X + Y$ 의 실험적 분포를 이론적인 $\text{Bin}(n_1 + n_2, p)$ 확률질량함수와 견주어 확인할 수 있다.

    ```python
    n1, n2, p = 4, 6, 0.3
    n_sim = 10_000

    X = np.random.binomial(n1, p, size=n_sim)
    Y = np.random.binomial(n2, p, size=n_sim)
    Z = X + Y

    x = np.arange(n1 + n2 + 1)
    pmf = stats.binom(n1 + n2, p).pmf(x)

    fig, ax = plt.subplots()
    ax.bar(x, pmf, alpha=0.4, label=f"Bin({n1+n2}, {p}) PMF", width=0.4)
    ax.hist(Z, bins=np.arange(-0.5, n1+n2+1.5), density=True,
            histtype="step", linewidth=2, color="red", label="X + Y histogram")
    ax.legend()
    plt.show()
    ```

    $X + Y$ 의 히스토그램은 $\text{Bin}(10, 0.3)$ 의 확률질량함수와 바싹 들어맞는다. 이는 당연한 결과이다. $X$ 는 서로 독립인 베르누이 시행 $n_1$ 개의 합이고 $Y$ 는 $n_2$ 개의 합이므로(모두 같은 $p$ 를 갖고 서로 상호독립이다), $X + Y$ 는 서로 독립인 $\text{Bernoulli}(p)$ 시행 $n_1 + n_2$ 개의 합이고, 이는 정의에 따라 $\text{Bin}(n_1 + n_2, p)$ 이기 때문이다.

---

**연습문제 6.** 표본이 10,000개나 되는데도 모의실험의 히스토그램이 이론적인 확률질량함수와 정확히 일치하지 않는 까닭을 설명하여라. 그 차이의 크기는 `n_sim` 에 어떻게 달려 있는가? `n_sim` 이 무한대로 갈 때 그 차이가 사라짐을 보장하는 정리는 무엇인가?

??? note "풀이"

    히스토그램은 크기가 $n_{\text{sim}}$ 인 **유한한 표본**으로 만든 것이다. 각 막대의 높이는 표본비율 $\hat{p}_k = (S = k \text{ 인 횟수}) / n_{\text{sim}}$ 이고, 이는 확률변수이다. $k$ 를 하나 고정하면 그 횟수는 $p_k = P(S = k)$ 에 대하여 $\text{Bin}(n_{\text{sim}}, p_k)$ 를 따르므로 다음이 성립한다.

    $$
    \text{Var}(\hat{p}_k) = \frac{p_k(1 - p_k)}{n_{\text{sim}}}
    $$

    $\hat{p}_k$ 가 $p_k$ 에서 벗어나는 크기는 대략 다음 정도이다.

    $$
    \text{SD}(\hat{p}_k) = \sqrt{\frac{p_k(1-p_k)}{n_{\text{sim}}}} \approx \frac{1}{2\sqrt{n_{\text{sim}}}}
    $$

    $n_{\text{sim}} = 10{,}000$ 이면 이 값은 대략 $0.005$ 이며, 작지만 눈에 띄는 차이가 나는 까닭이 여기에 있다.

    **큰수의 법칙**은 $n_{\text{sim}} \to \infty$ 일 때 $\hat{p}_k \to p_k$ 가 거의 확실하게 성립함을 보장한다. 같은 말로, 임의의 $\epsilon > 0$ 에 대하여 $P(|\hat{p}_k - p_k| > \epsilon) \to 0$ 이다. `n_sim` 을 늘리면 히스토그램이 이론적인 확률질량함수로 수렴하는 까닭이 바로 이것이다.
