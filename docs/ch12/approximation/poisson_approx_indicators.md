# 지시확률변수의 합으로 보는 푸아송 근사: 모의실험

이 모의실험은 푸아송 근사가 (성공확률이 모두 같은) 이항분포에만 쓰이는 것이 아니라, 성공확률이 **서로 다른** 독립인 베르누이 지시확률변수의 합에도 쓰인다는 것을 보여 준다. 일반화된 푸아송 극한정리와 르캉 부등식을 곧바로 눈으로 보여 주는 실험이다.

## 배경

$X_1, X_2, \ldots, X_n$ 을 독립인 베르누이확률변수라 하자. 여기서 $X_i \sim \text{Bernoulli}(p_i)$ 이고 $p_i$ 가 반드시 같을 필요는 없다. 다음과 같이 정의한다.

$$
S_n = \sum_{i=1}^{n} X_i
$$

$p_i$ 가 서로 다르므로 $S_n$ 은 일반적으로 이항분포가 **아니다**. 그러나 모든 $p_i$ 가 작다면 $S_n$ 의 분포는 다음의 $\lambda$ 에 대한 $\text{Po}(\lambda)$ 로 잘 근사된다.

$$
\lambda = \sum_{i=1}^{n} p_i
$$

르캉 부등식은 다음과 같은 오차 경계를 준다.

$$
d_{\text{TV}}\!\left(\mathcal{L}(S_n),\; \text{Po}(\lambda)\right) \leq \sum_{i=1}^{n} p_i^2
$$

모든 $p_i$ 가 작으면(이를테면 $p_i < 0.01$) 이 경계는 대략 $\max_i p_i \cdot \lambda$ 가 되며, $\lambda$ 자체가 어느 정도 크더라도 이 값은 작다.

이 모의실험에서는 $[0, 0.01]$ 에서 고르게 뽑은 성공확률 $p_i$ 를 갖는 독립인 지시확률변수 $n = 1000$ 개를 다룬다. 전체의 기댓값은 $\lambda = \sum p_i \approx 5$ 이고, 르캉 경계는 $\sum p_i^2 \approx \max_i p_i \cdot \lambda / 3 \ll 1$ 이다.

## 코드

```python
"""서로 같지 않은 베르누이 지시확률변수 합에 대한 푸아송 근사."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

N_SAMPLES = 10_000
n = 1000

# 지시확률변수마다 (작고 무작위인) 서로 다른 성공확률을 갖는다
P_vec = np.random.uniform(0.0, 1.0, (n, 1)) / 100
uniform_samples = np.random.uniform(0.0, 1.0, (n, N_SAMPLES))
X_i = (uniform_samples < P_vec).astype(int)
S_n = X_i.sum(axis=0)

LA = P_vec.sum()
po_samples = np.random.poisson(lam=LA, size=N_SAMPLES)

fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(14, 4))
bins = np.arange(int(3 * LA))

ax0.hist(S_n, bins=bins, density=True, color="steelblue", edgecolor="black")
ax0.set_title("Sum of non-identical indicators")

ax1.hist(po_samples, bins=bins, density=True, color="steelblue", edgecolor="black")
ax1.set_title(f"Poisson(λ ≈ {LA:.1f})")

ax2.hist(S_n, bins=bins, density=True, label="Indicators sum", color="b",
         alpha=1, histtype="step", linewidth=2)
ax2.hist(po_samples, bins=bins, density=True, label="Poisson", color="r",
         alpha=0.5, histtype="step", linewidth=2)
ax2.set_title("Overlay Comparison")
ax2.legend()

for ax in (ax0, ax1, ax2):
    ax.grid(True, alpha=0.3)

plt.suptitle("Poisson Approximation of Non-Identical Bernoulli Sum",
             fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("poisson_approx_indicators.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 실행 결과

이 스크립트는 세 개의 칸으로 이루어진 그림을 만든다.

1. **왼쪽 칸** -- 모의실험 10,000번에서 얻은 $S_n = \sum_{i=1}^{1000} X_i$ 의 히스토그램이다. 각 $X_i$ 는 서로 다른 작은 확률 $p_i \in [0, 0.01]$ 을 갖는다. 분포는 $\lambda \approx 5$ 근처를 중심으로 오른쪽으로 치우쳐 있다.

2. **가운데 칸** -- $\lambda = \sum p_i$ 인 $\text{Po}(\lambda)$ 에서 뽑은 10,000개 표본의 히스토그램이다. 모양이 왼쪽 칸과 아주 비슷하다.

3. **오른쪽 칸** -- 두 히스토그램을 겹쳐 그린 것이다. 지시확률변수의 합(파랑)과 푸아송분포(빨강)의 윤곽이 잘 포개져 근사가 좋음을 확인해 준다.

표본통계량은 대체로 다음과 같다(정확한 값은 무작위로 뽑힌 $p_i$ 에 따라 달라진다).

| 통계량 | 지시확률변수의 합 | $\text{Po}(\lambda)$ |
|:---|:---:|:---:|
| 표본평균 | $\approx 5.0$ | $\approx 5.0$ |
| 표본표준편차 | $\approx 2.2$ | $\approx 2.2$ |

## 뜻풀이

이 모의실험은 중요한 일반화를 보여 준다. 푸아송 근사에는 성공확률이 모두 같아야 한다는 조건이 필요하지 않다. 결정적인 조건은 $n$ 이 크고 $\lambda = \sum p_i$ 가 어느 정도 크더라도 낱낱의 $p_i$ 가 저마다 작다는 것이다.

**왜 통하는가.** $p_i$ 를 $\text{Uniform}(0, 0.01)$ 에서 뽑았으므로 $\max_i p_i < 0.01$ 이다. 르캉 경계는 다음을 준다.

$$
d_{\text{TV}} \leq \sum_{i=1}^{n} p_i^2
$$

$p_i \sim \text{Uniform}(0, 0.01)$ 이므로 $E[p_i^2] = (0.01)^2/3 \approx 3.3 \times 10^{-5}$ 이고, 따라서 다음과 같다.

$$
\sum_{i=1}^{1000} p_i^2 \approx 1000 \times 3.3 \times 10^{-5} = 0.033
$$

전변동거리가 이만큼 작다는 사실이 겹쳐 그린 그림에서 두 분포가 잘 들어맞는 까닭을 말해 준다.

**이항분포인 경우와의 견줌.** 모든 $p_i$ 가 $\bar{p} = \lambda / n$ 으로 같다면 $S_n$ 은 정확히 $B(n, \bar{p})$ 가 된다. 여기서는 $p_i$ 가 제각각이어서 $S_n$ 이 이항분포가 아니지만, 푸아송 근사는 여전히 성립한다. 이것이 바로 르캉 부등식의 힘이다. 확률이 같든 다르든 독립인 드문 사건들의 모임이면 어디에나 쓸 수 있다.

**분산의 견줌.** $S_n$ 의 정확한 분산은 $\sum_{i=1}^n p_i(1 - p_i) \approx \sum p_i = \lambda$ 이며(각 $p_i \ll 1$ 이므로), 이는 $\text{Var}(\text{Po}(\lambda)) = \lambda$ 와 들어맞는다.

## 연습문제

**연습문제 1.** 성공확률을 $\text{Uniform}(0, 0.01)$ 대신 $\text{Uniform}(0, 0.1)$ 에서 뽑도록 모의실험을 고쳐라. $n = 1000$ 은 그대로 둔다. 르캉 경계 $\sum p_i^2$ 을 계산하고 겹쳐 그린 히스토그램을 견주어 보아라. 푸아송 근사가 여전히 좋은가?

??? success "연습문제 1 풀이"

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(42)
    N_SAMPLES = 10_000
    n = 1000

    P_vec = np.random.uniform(0.0, 0.1, (n, 1))
    uniform_samples = np.random.uniform(0.0, 1.0, (n, N_SAMPLES))
    X_i = (uniform_samples < P_vec).astype(int)
    S_n = X_i.sum(axis=0)

    LA = P_vec.sum()
    le_cam = (P_vec**2).sum()
    po_samples = np.random.poisson(lam=LA, size=N_SAMPLES)

    print(f"λ = {LA:.2f}")
    print(f"Le Cam bound = {le_cam:.4f}")

    bins = np.arange(int(3 * LA))
    plt.figure(figsize=(8, 4))
    plt.hist(S_n, bins=bins, density=True, histtype="step",
             linewidth=2, color="b", label="Indicators sum")
    plt.hist(po_samples, bins=bins, density=True, histtype="step",
             linewidth=2, color="r", alpha=0.5, label="Poisson")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.title(f"Non-identical indicators, p_i ~ U(0,0.1), λ≈{LA:.1f}")
    plt.tight_layout()
    plt.show()
    ```

    $p_i \sim \text{Uniform}(0, 0.1)$ 이면 $\lambda \approx 50$ 이고 $\sum p_i^2 \approx 1000 \cdot (0.1)^2/3 \approx 3.3$ 이다. 르캉 경계가 훨씬 커지고, 겹쳐 그린 그림에서도 눈에 띄는 어긋남이 보인다. 낱낱의 확률이 더는 충분히 작지 않기 때문에 푸아송 근사가 무너진다.

**연습문제 2.** 처음 설정($n = 1000$, $p_i \sim \text{Uniform}(0, 0.01)$)에 대하여 생성된 $p_i$ 값들로부터 정확한 르캉 경계 $\sum_{i=1}^n p_i^2$ 을 계산하고, 모의실험에서 어림한 전변동거리와 견주어 보아라.

??? success "연습문제 2 풀이"

    ```python
    import numpy as np

    np.random.seed(42)
    N_SAMPLES = 100_000
    n = 1000

    P_vec = np.random.uniform(0.0, 1.0, (n, 1)) / 100
    uniform_samples = np.random.uniform(0.0, 1.0, (n, N_SAMPLES))
    X_i = (uniform_samples < P_vec).astype(int)
    S_n = X_i.sum(axis=0)

    LA = P_vec.sum()
    le_cam = (P_vec**2).sum()

    # 경험적 분포에서 전변동거리를 어림한다
    k_max = int(3 * LA) + 1
    hist_S, _ = np.histogram(S_n, bins=np.arange(k_max + 1), density=True)

    from scipy.stats import poisson
    poisson_pmf = poisson.pmf(np.arange(k_max), LA)

    tv_est = 0.5 * np.sum(np.abs(hist_S - poisson_pmf))

    print(f"λ = {LA:.4f}")
    print(f"Le Cam bound (Σ p_i²) = {le_cam:.6f}")
    print(f"Estimated TV distance = {tv_est:.6f}")
    print(f"Ratio (TV / bound) = {tv_est / le_cam:.4f}")
    ```

    어림한 전변동거리는 대체로 르캉 경계보다 훨씬 작다(비가 $0.1$--$0.3$ 언저리이다). 르캉 부등식은 상계일 뿐 빈틈없는 어림값은 아님을 확인해 준다.

**연습문제 3.** $P(X_i = 1) = p_i$ 인 독립인 베르누이확률변수 $X_i$ 에 대하여 $S_n = \sum X_i$ 의 분산이 다음을 만족함을 증명하여라.

$$
\text{Var}(S_n) = \sum_{i=1}^{n} p_i(1-p_i) = \lambda - \sum_{i=1}^{n} p_i^2
$$

여기서 $\lambda = \sum p_i$ 이다. 이 결과는 푸아송분포의 분산 $\lambda$ 가 언제 좋은 근사가 되는지에 대해 무엇을 말해 주는가?

??? success "연습문제 3 풀이"

    독립성에 따라 $\text{Var}(S_n) = \sum_{i=1}^n \text{Var}(X_i) = \sum_{i=1}^n p_i(1 - p_i)$ 이다.

    이를 펼치면 다음과 같다.

    $$
    \sum_{i=1}^n p_i(1 - p_i) = \sum_{i=1}^n p_i - \sum_{i=1}^n p_i^2 = \lambda - \sum_{i=1}^n p_i^2
    $$

    푸아송 근사는 분산으로 $\lambda$ 를 쓴다. 분산에서 생기는 근사 오차는 정확히 $\sum p_i^2$ 이며, 이는 르캉 경계에 나오는 것과 같은 양이다. 그러므로 다음과 같다.

    - $\sum p_i^2$ 이 작으면(모든 $p_i$ 가 작으면) 참된 분산 $\lambda - \sum p_i^2 \approx \lambda$ 이므로 푸아송분포의 분산이 정확하다.
    - $\sum p_i^2$ 이 작지 않으면 푸아송분포가 분산을 지나치게 크게 잡게 되어 근사가 나빠진다.

    이로써 르캉 경계에 손에 잡히는 뜻이 생긴다. 르캉 경계는 분포의 근사 오차와 분산의 어긋남을 함께 재고 있다. $\square$

**연습문제 4.** $p_i$ 를 균등분포에서 뽑는 대신 $i = 1, 2, \ldots, n$ 에 대해 $p_i = c/i$ 로 두어라. 여기서 $c > 0$ 은 상수이다. $\lambda = \sum_{i=1}^{1000} c/i \approx 5$ 가 되도록 $c$ 를 고르고, 모의실험을 돌려 $\text{Po}(5)$ 와 견주어 보아라.

??? success "연습문제 4 풀이"

    조화합은 $H_{1000} = \sum_{i=1}^{1000} 1/i \approx 7.485$ 이다. $\lambda = cH_{1000} = 5$ 로 두면 $c = 5/H_{1000} \approx 0.668$ 이다.

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(42)
    N_SAMPLES = 10_000
    n = 1000

    H_n = sum(1/i for i in range(1, n+1))
    c = 5.0 / H_n
    P_vec = np.array([c / i for i in range(1, n+1)]).reshape(-1, 1)

    uniform_samples = np.random.uniform(0.0, 1.0, (n, N_SAMPLES))
    X_i = (uniform_samples < P_vec).astype(int)
    S_n = X_i.sum(axis=0)

    LA = P_vec.sum()
    le_cam = (P_vec**2).sum()
    po_samples = np.random.poisson(lam=LA, size=N_SAMPLES)

    print(f"c = {c:.4f}, λ = {LA:.4f}, Le Cam = {le_cam:.6f}")
    print(f"max p_i = {P_vec.max():.4f}")

    bins = np.arange(15)
    plt.figure(figsize=(8, 4))
    plt.hist(S_n, bins=bins, density=True, histtype="step",
             linewidth=2, color="b", label="Indicators sum")
    plt.hist(po_samples, bins=bins, density=True, histtype="step",
             linewidth=2, color="r", alpha=0.5, label="Poisson(5)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.title(f"Harmonic probabilities: p_i = {c:.3f}/i")
    plt.tight_layout()
    plt.show()
    ```

    가장 큰 확률은 $p_1 = c \approx 0.668$ 로 결코 작지 않다. 르캉 경계는 $\sum p_i^2 = c^2 \sum 1/i^2 \approx (0.668)^2 \cdot \pi^2/6 \approx 0.734$ 로 어중간한 크기이다. 앞쪽 몇 개의 지시확률변수가 무시할 수 없는 성공확률을 갖기 때문에, 겹쳐 그린 그림에서 특히 꼬리 쪽에 눈에 보이는 어긋남이 나타난다.

**연습문제 5.** 처음 모의실험($p_i \sim \text{Uniform}(0, 0.01)$, $n = 1000$)을 돌리되 $n$ 을 $\{100, 500, 1000, 5000, 10000\}$ 으로 바꾸어 가며 돌려라. 이때 $p_i$ 는 언제나 $\text{Uniform}(0, 0.01)$ 에서 뽑는다. 각 $n$ 에 대해 $\lambda = \sum p_i$ 와 르캉 경계 $\sum p_i^2$ 을 계산하여라. 르캉 경계를 $n$ 의 함수로 그려라. 어떤 흐름이 보이는가?

??? success "연습문제 5 풀이"

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(42)
    n_values = [100, 500, 1000, 5000, 10000]
    lambdas = []
    le_cams = []

    for n in n_values:
        P_vec = np.random.uniform(0.0, 0.01, n)
        la = P_vec.sum()
        lc = (P_vec**2).sum()
        lambdas.append(la)
        le_cams.append(lc)
        print(f"n = {n:>6}: λ = {la:.3f}, Le Cam = {lc:.6f}")

    plt.figure(figsize=(8, 5))
    plt.plot(n_values, le_cams, 'o-', linewidth=2, markersize=8)
    plt.xlabel('n')
    plt.ylabel('Le Cam bound (Σ p_i²)')
    plt.title('Le Cam bound vs number of indicators')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    ```

    $E[p_i^2] = (0.01)^2/3 \approx 3.3 \times 10^{-5}$ 이므로 르캉 경계는 $\sum p_i^2 \approx n \cdot 3.3 \times 10^{-5}$ 으로 $n$ 에 비례해 커진다. $n$ 이 커지면 $\lambda$ 도 함께 커지지만($\lambda \approx n \cdot 0.005$) 르캉 경계도 같은 속도로 커지므로, 상대적인 정확도 $\sum p_i^2 / \lambda \approx 0.01/3 \approx 0.0033$ 은 그대로 유지된다. $\max_i p_i$ 가 작게 남아 있는 한, $n$ 이 커져도 푸아송 근사는 한결같이 좋다.
