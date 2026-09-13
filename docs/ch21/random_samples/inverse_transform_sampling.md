# 역변환 표집: 모의실험

**역변환 방법**(스미르노프 변환이라고도 한다)은 어떤 목표분포에서든 확률표본을 만들어 내는 가장 기본이 되는 기법 가운데 하나이다. 균등난수만 쓸 수 있는 상황에서 역누적분포함수를 이용해 원하는 분포를 따르는 표본을 만들어 낸다. 이 쪽에서는 직접 정의한 이산분포에 이 기법을 적용해 보고, NumPy에 내장된 `np.random.choice` 와 견주어 본다.

## 배경

값 $x_1 < x_2 < \cdots < x_k$ 를 확률 $p_1, p_2, \ldots, p_k$ 로 가지는 이산확률변수 $X$ 에서 표본을 뽑고 싶다고 하자. 누적분포함수는 다음과 같다.

$$
F(x) = P(X \leq x) = \sum_{j:\, x_j \leq x} p_j
$$

**역변환 방법**은 다음과 같이 진행한다.

1. $U \sim \text{Uniform}(0,1)$ 을 만든다.
2. $i = \min\{j : F(x_j) \geq U\}$ 일 때 $X = x_i$ 를 내놓는다.

달리 말하면 $x_i$ 까지의 누적확률이 균등난수 $U$ 를 넘어서는 가장 작은 첨자 $i$ 를 찾는 것이다. 이것이 통하는 까닭은 다음과 같다.

$$
P(X = x_i) = P\!\bigl(F(x_{i-1}) < U \leq F(x_i)\bigr) = F(x_i) - F(x_{i-1}) = p_i
$$

여기에서 약속에 따라 $F(x_0) = 0$ 으로 둔다. 핵심은 $U$ 가 각 "확률 층"에 꼭 알맞은 확률로 떨어진다는 것이다.

누적분포함수 $F$ 가 순증가하는 연속분포에서는 이 방법이 $X = F^{-1}(U)$ 로 간단해진다. $P(F^{-1}(U) \leq x) = P(U \leq F(x)) = F(x)$ 이기 때문이다.

아래 코드에서는 이 방법으로 $\{-3, -1, 1, 2, 5\}$ 위의 분포에서 표본을 뽑는데, 그 확률질량함수는 다음과 같다.

$$
P(X = -3) = 0.1, \quad P(X = -1) = 0.1, \quad P(X = 1) = 0.1, \quad P(X = 2) = 0.5, \quad P(X = 5) = 0.2
$$

## 코드

```python
"""이산확률변수를 위한 역변환 표집(스미르노프 변환)."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# 직접 정의한 이산분포
x_values = np.array([-3, -1, 1, 2, 5])
pmf = np.array([0.1, 0.1, 0.1, 0.5, 0.2])
n_sim = 10_000


def inverse_transform_sample(pmf, x_values):
    """역누적분포함수(스미르노프 변환)로 값 하나를 뽑는다."""
    cdf = np.cumsum(pmf)
    u = np.random.rand()
    idx = np.searchsorted(cdf, u)
    return x_values[idx]


# 방법 1: 역변환
samples_inv = np.array([inverse_transform_sample(pmf, x_values) for _ in range(n_sim)])

# 방법 2: np.random.choice (견주어 보기 위해)
samples_choice = np.random.choice(x_values, size=n_sim, p=pmf)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

bins = np.array([-4, -2, 0, 0.5, 1.5, 3.5, 6])

ax1.hist(samples_inv, bins=bins, density=True, alpha=0.7, color="steelblue",
         edgecolor="black")
ax1.set_title("Inverse Transform Sampling")
ax1.set_xticks(x_values)
ax1.grid(True, alpha=0.3)

ax2.hist(samples_choice, bins=bins, density=True, alpha=0.7, color="steelblue",
         edgecolor="black")
ax2.set_title("np.random.choice (reference)")
ax2.set_xticks(x_values)
ax2.grid(True, alpha=0.3)

plt.suptitle("Inverse Transform Sampling for Discrete RVs", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("inverse_transform_sampling.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 실행 결과

이 스크립트는 히스토그램 두 개를 나란히 놓아 견주어 보여 준다.

- **왼쪽 그림(역변환 표집):** 역누적분포함수 방법으로 만든 표본 10,000개의 히스토그램이다. 막대의 높이가 참확률질량함수 값과 잘 들어맞는다. $x = 2$ 의 막대가 가장 높고(참확률 0.5), 그다음이 $x = 5$ (0.2)이며, $x = -3$, $x = -1$, $x = 1$ 은 거의 같은 높이(각각 0.1)이다.

- **오른쪽 그림(np.random.choice):** NumPy에 내장된 `np.random.choice` 로 만든 표본 10,000개의 히스토그램으로, 견주어 볼 기준이 된다. 모양이 왼쪽 그림과 눈으로 구별되지 않는다.

두 히스토그램 모두 역변환 방법이 목표분포를 제대로 되살려 낸다는 것을 확인시켜 준다.

## 뜻풀이

이 모의실험은 몇 가지 중요한 점을 보여 준다.

1. **옳음.** 역변환 방법으로 만든 표본의 경험적 분포는 목표 확률질량함수와 들어맞는다. $n = 10{,}000$ 개의 표본이면 상대도수가 참확률에 매우 가깝다.

2. **두루 쓰임.** 이 방법은 어떤 이산분포에도 통한다. 필요한 것은 확률질량함수(또는 같은 말로 누적분포함수)와 균등난수를 만들어 낼 수단뿐이다.

3. **작동 방식.** 함수 `np.searchsorted(cdf, u)` 는 $F(x_{i-1}) < u \leq F(x_i)$ 가 되는 첨자 $i$ 를 빠르게 찾아 준다. 이것이 누적분포함수를 뒤집는 일을 계산으로 옮긴 것이다.

4. **내장 함수와 견주어 보기.** NumPy의 `np.random.choice` 도 속으로는 사실상 같은 생각을 쓰지만 C로 최적화되어 있어 큰 규모의 표집에서 더 빠르다. 여기의 역변환 구현은 알고리즘을 드러내 보이려는 교육적인 코드이다.

## 연습문제

**연습문제 1.**
$X$ 가 확률질량함수 $P(X = 0) = 0.3$, $P(X = 1) = 0.5$, $P(X = 2) = 0.2$ 를 갖는 이산확률변수라고 하자.

**(a)** 누적분포함수 $F(x)$ 를 적고, 역변환 방법에서 $X$ 의 각 값으로 옮겨지는 $u \in (0,1)$ 의 구간을 밝혀라.

**(b)** 역변환 방법으로 표본 $n = 50{,}000$ 개를 만들어 표본평균과 표본분산을 셈하여라. 이론값 $E[X]$, $\text{Var}(X)$ 와 견주어 보아라.

??? success "연습문제 1 풀이"
    **(a)** 누적분포함수는 $F(0) = 0.3$, $F(1) = 0.8$, $F(2) = 1.0$ 이다. 역변환은 다음과 같이 값을 매긴다.

    - $U \in [0, 0.3)$ 일 때 $X = 0$
    - $U \in [0.3, 0.8)$ 일 때 $X = 1$
    - $U \in [0.8, 1.0)$ 일 때 $X = 2$

    **(b)** 이론적으로 $E[X] = 0(0.3) + 1(0.5) + 2(0.2) = 0.9$ 이고 $E[X^2] = 0(0.3) + 1(0.5) + 4(0.2) = 1.3$ 이므로 $\text{Var}(X) = 1.3 - 0.81 = 0.49$ 이다.

    ```python
    import numpy as np

    np.random.seed(42)

    x_vals = np.array([0, 1, 2])
    pmf = np.array([0.3, 0.5, 0.2])
    cdf = np.cumsum(pmf)

    n = 50_000
    U = np.random.rand(n)
    samples = x_vals[np.searchsorted(cdf, U)]

    print(f"Sample mean: {np.mean(samples):.4f} (theory: 0.9)")
    print(f"Sample var:  {np.var(samples):.4f} (theory: 0.49)")
    ```

---

**연습문제 2.**
역변환 방법을 써서 **기하분포($p$)** 에서 표본을 뽑아라. 여기에서 $k = 1, 2, 3, \ldots$ 에 대하여 $P(X = k) = (1-p)^{k-1}p$ 이다.

**(a)** 역누적분포함수가 $F^{-1}(u) = \lceil \log(1-u) / \log(1-p) \rceil$ 임을 보여라.

**(b)** 이를 구현하여 $p = 0.3$ 으로 표본 $10{,}000$ 개를 만들어라. 표본평균이 $1/p$ 에 가까운지 확인하여라.

**(c)** ($k = 1, \ldots, 15$ 에 대하여) 경험적 확률질량함수를 이론적 확률질량함수와 견주어 보아라.

??? success "연습문제 2 풀이"
    **(a)** 기하분포($p$)의 누적분포함수는 $k = 1, 2, \ldots$ 에 대하여 $F(k) = 1 - (1-p)^k$ 이다. $F(k) \geq u$ 가 되는 가장 작은 $k$ 를 찾아야 하는데, $1 - (1-p)^k \geq u$ 에서 $(1-p)^k \leq 1-u$ 이므로 $k \geq \log(1-u)/\log(1-p)$ 이다. 따라서 $F^{-1}(u) = \lceil \log(1-u)/\log(1-p) \rceil$ 이다.

    **(b)–(c)**

    ```python
    import numpy as np

    np.random.seed(42)

    p = 0.3
    n = 10_000
    U = np.random.rand(n)
    samples = np.ceil(np.log(1 - U) / np.log(1 - p)).astype(int)

    print(f"Sample mean: {np.mean(samples):.4f} (theory: {1/p:.4f})")

    # k = 1..15 에 대한 경험적 확률질량함수와 이론적 확률질량함수
    for k in range(1, 16):
        emp = np.mean(samples == k)
        theory = (1 - p) ** (k - 1) * p
        print(f"P(X={k:2d}): empirical={emp:.4f}, theory={theory:.4f}")
    ```

---

**연습문제 3.**
**지수분포($\lambda$)** 의 누적분포함수는 $x \geq 0$ 에서 $F(x) = 1 - e^{-\lambda x}$ 이다.

**(a)** 역누적분포함수 $F^{-1}(u) = -\frac{1}{\lambda}\ln(1 - u)$ 를 유도하여라.

**(b)** $U \sim \text{Uniform}(0,1)$ 이면 $1 - U \sim \text{Uniform}(0,1)$ 이므로 $X = -\frac{1}{\lambda}\ln U$ 를 써도 똑같은 까닭을 설명하여라.

**(c)** 두 식을 모두 써서 $\lambda = 2$ 로 표본 $20{,}000$ 개를 만들어라. 표본평균과 표본분산이 각각 $1/\lambda$ 와 $1/\lambda^2$ 에 가까운지 확인하여라.

??? success "연습문제 3 풀이"
    **(a)** $u = 1 - e^{-\lambda x}$ 로 두고 풀면 $e^{-\lambda x} = 1 - u$ 이므로 $x = -\frac{1}{\lambda}\ln(1 - u)$ 이다. 따라서 $F^{-1}(u) = -\frac{1}{\lambda}\ln(1 - u)$ 이다.

    **(b)** $U \sim \text{Uniform}(0,1)$ 이면 $1 - U$ 도 $\text{Uniform}(0,1)$ 을 따른다. 식에서 $U$ 자리에 $1 - U$ 를 넣으면 $X = -\frac{1}{\lambda}\ln(U)$ 를 얻고, 이것도 같은 분포를 따른다.

    **(c)**

    ```python
    import numpy as np

    np.random.seed(42)

    lam = 2.0
    n = 20_000

    U = np.random.rand(n)
    samples1 = -np.log(1 - U) / lam
    samples2 = -np.log(U) / lam

    for label, s in [("Formula 1", samples1), ("Formula 2", samples2)]:
        print(f"{label}: mean={np.mean(s):.4f} (theory {1/lam:.4f}), "
              f"var={np.var(s):.4f} (theory {1/lam**2:.4f})")
    ```

---

**연습문제 4.**
**(a)** $F$ 가 연속이고 순증가하는 누적분포함수이며 $U \sim \text{Uniform}(0,1)$ 이면 $X = F^{-1}(U)$ 의 누적분포함수가 $F$ 임을 증명하여라.

**(b)** 그 역을 증명하여라. 곧 $X$ 의 누적분포함수 $F$ 가 연속이면 $F(X) \sim \text{Uniform}(0,1)$ 이다. 이것이 **확률적분변환**이다.

**(c)** $F$ 에 뜀이 있을 때(곧 $X$ 가 이산일 때) (b)가 성립하지 않는 까닭을 설명하여라. 이산인 경우에 $F(X)$ 는 어떤 분포를 따르는가?

??? success "연습문제 4 풀이"
    **(a)** 임의의 $x \in \mathbb{R}$ 에 대하여 다음이 성립한다.

    $$
    P(X \leq x) = P(F^{-1}(U) \leq x) = P(U \leq F(x)) = F(x)
    $$

    두 번째 등호에서는 $F$ 가 순증가한다는 사실($F^{-1}(u) \leq x \iff u \leq F(x)$)을, 세 번째 등호에서는 $U \sim \text{Uniform}(0,1)$ 을 썼다.

    **(b)** $Y = F(X)$ 라고 하자. $0 \leq y \leq 1$ 에 대하여 다음이 성립한다.

    $$
    P(Y \leq y) = P(F(X) \leq y) = P(X \leq F^{-1}(y)) = F(F^{-1}(y)) = y
    $$

    이는 $\text{Uniform}(0,1)$ 의 누적분포함수이다. 두 번째 등호에서는 $F$ 의 연속성과 순증가성을 썼다.

    **(c)** $F$ 에 뜀이 있으면 $F(X)$ 는 균등분포를 따르지 않는다. $X$ 가 확률 $p_i$ 로 값 $x_i$ 를 가지면 $F(X)$ 는 확률 $p_i$ 로 $F(x_i)$ 를 가진다. 그러므로 $F(X)$ 는 연속인 균등분포가 아니라 $\{F(x_1), F(x_2), \ldots\}$ 에 값을 가지는 이산확률변수이다. 그래도 역변환 방법은 그대로 통하는데, 일반화된 역함수 $F^{-1}(u) = \inf\{x : F(x) \geq u\}$ 가 균등난수를 목표분포로 제대로 옮겨 주기 때문이다.

---

**연습문제 5.**
**혼합분포**에서 표본을 뽑는 것을 생각해 보자. 확률 $\alpha$ 로 $\text{Exponential}(\lambda_1)$ 에서 뽑고, 확률 $1 - \alpha$ 로 $\text{Exponential}(\lambda_2)$ 에서 뽑는다.

**(a)** 이 혼합분포의 누적분포함수를 적고, 해석적으로 뒤집기가 쉽지 않은 까닭을 설명하여라.

**(b)** (혼합분포의 누적분포함수를 곧바로 뒤집지 않고) 역변환 방법을 쓰는 간단한 두 단계 알고리즘을 설명하여라.

**(c)** $\alpha = 0.4$, $\lambda_1 = 1$, $\lambda_2 = 5$ 로 이 알고리즘을 구현하여라. 표본 $10{,}000$ 개를 만들어 히스토그램을 참혼합밀도와 함께 그려라.

??? success "연습문제 5 풀이"
    **(a)** 누적분포함수는 $x \geq 0$ 에서 $F(x) = \alpha(1 - e^{-\lambda_1 x}) + (1 - \alpha)(1 - e^{-\lambda_2 x}) = 1 - \alpha e^{-\lambda_1 x} - (1 - \alpha)e^{-\lambda_2 x}$ 이다. 이를 뒤집으려면 $\alpha e^{-\lambda_1 x} + (1 - \alpha)e^{-\lambda_2 x} = 1 - u$ 를 풀어야 하는데, 일반적으로 닫힌 꼴의 해가 없다.

    **(b)** 두 단계 알고리즘은 다음과 같다.

    1. $U_1 \sim \text{Uniform}(0,1)$ 을 만든다. $U_1 < \alpha$ 이면 $\text{Exponential}(\lambda_1)$ 에서, 그렇지 않으면 $\text{Exponential}(\lambda_2)$ 에서 뽑는다.
    2. 고른 지수분포에 대하여 역변환을 쓴다. 곧 $U_2 \sim \text{Uniform}(0,1)$ 일 때 $X = -\ln(U_2)/\lambda$ 이다.

    **(c)**

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(42)

    alpha, lam1, lam2, n = 0.4, 1.0, 5.0, 10_000

    U1 = np.random.rand(n)
    U2 = np.random.rand(n)
    component = U1 < alpha
    samples = np.where(component, -np.log(U2) / lam1, -np.log(U2) / lam2)

    x = np.linspace(0, 5, 300)
    f_mix = alpha * lam1 * np.exp(-lam1 * x) + (1 - alpha) * lam2 * np.exp(-lam2 * x)

    plt.hist(samples, bins=80, density=True, alpha=0.7, label="Samples")
    plt.plot(x, f_mix, "r-", linewidth=2, label="True density")
    plt.legend()
    plt.title("Mixture of Exponentials via Inverse Transform")
    plt.show()
    ```
