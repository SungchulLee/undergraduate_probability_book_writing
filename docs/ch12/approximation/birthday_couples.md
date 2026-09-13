# 생일이 같은 짝 모의실험

이 모의실험은 현실적인 상황에서 푸아송 근사를 보여 준다. 어느 해에 이루어진 약 80,000건의 결혼 가운데 부부의 생일이 같은 쌍이 몇 쌍이나 되는지 어림하는 문제이다. 부부의 쌍이 아주 많고($n = 80{,}000$) 한 쌍의 생일이 같을 확률이 아주 작으므로($p = 1/365$), 푸아송 근사를 쓰기에 딱 맞는 본보기이다.

## 배경

$n$ 쌍의 부부가 있고, 각 부부의 두 사람 생일은 365일 가운데에서 서로 독립으로 고르게 정해진다고 하자. 어떤 한 쌍의 생일이 같을 확률은 다음과 같다.

$$
p = \frac{1}{365}
$$

$X_i = \mathbf{1}\{i \text{ 번째 부부의 생일이 같다}\}$ 라 하고 다음과 같이 정의하자.

$$
S_n = \sum_{i=1}^{n} X_i
$$

부부들이 서로 독립이고 각 $X_i \sim \text{Bernoulli}(1/365)$ 이므로 $S_n \sim B(n, p)$ 이다. $n = 80{,}000$ 이면 다음과 같다.

$$
\lambda = np = \frac{80{,}000}{365} \approx 219.18
$$

푸아송 극한정리는 $S_n \approx \text{Po}(\lambda)$ 를 준다. $\lambda \approx 219$ 가 작지는 않지만, $p = 1/365$ 가 매우 작고 $n$ 이 매우 크므로 근사는 여전히 정확하다. 르캉 경계는 다음과 같다.

$$
np^2 = 80{,}000 \cdot \left(\frac{1}{365}\right)^2 \approx 0.60
$$

이 값이 전변동거리가 작음을 보장해 준다.

## 코드

```python
"""생일이 같은 부부의 쌍의 수에 대한 푸아송 근사."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n_samples = 100_000
n = 80_000       # 부부의 쌍의 수
p = 1 / 365     # 한 쌍의 생일이 같을 확률
la = n * p       # 푸아송 모수

samples_binomial = np.random.binomial(n, p, n_samples)
samples_poisson = np.random.poisson(la, n_samples)

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 4))
bins = np.arange(150, 300)

ax0.hist(samples_binomial, bins=bins, density=True, color="steelblue", edgecolor="black")
ax0.set_title("Binomial sampling")
ax0.grid(True, alpha=0.3)

ax1.hist(samples_poisson, bins=bins, density=True, color="steelblue", edgecolor="black")
ax1.set_title("Poisson sampling")
ax1.grid(True, alpha=0.3)

plt.suptitle(f"Number of couples sharing a birthday (n={n:,}, λ={la:.1f})",
             fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("birthday_couples.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 실행 결과

이 스크립트는 두 개의 칸으로 이루어진 그림을 만드는데, 각 칸은 100,000개의 표본으로 그린 히스토그램이다.

1. **왼쪽 칸** -- $B(80{,}000,\; 1/365)$ 에서 뽑은 표본이다. 히스토그램은 $\lambda \approx 219$ 근처를 중심으로 거의 정규분포의 모양을 띤다($np$ 가 큰 이항분포에서 예상되는 바이다).

2. **오른쪽 칸** -- $\text{Po}(219.18)$ 에서 뽑은 표본이다. 히스토그램이 이항분포의 것과 눈으로는 구별되지 않는다.

두 히스토그램 모두 대략 $[180, 260]$ 범위에 걸쳐 있고 $219$ 근처에서 가장 높다. 표본통계량은 대체로 다음과 같다.

| 통계량 | $B(80000, 1/365)$ | $\text{Po}(219.18)$ |
|:---|:---:|:---:|
| 표본평균 | $\approx 219.2$ | $\approx 219.2$ |
| 표본표준편차 | $\approx 14.8$ | $\approx 14.8$ |

## 뜻풀이

이 모의실험은 이 문제에서 이항분포와 푸아송분포가 사실상 같은 결과를 낸다는 것을 확인해 준다. 눈여겨볼 점이 몇 가지 있다.

**$\lambda$ 가 큰데도 근사가 통하는 까닭.** 흔히 쓰는 어림 기준($\lambda \leq 20$)은 충분조건일 뿐 필요조건이 아니다. 중요한 것은 $p$ 가 작다는 사실이다. $p = 1/365 \approx 0.0027$ 이므로 르캉 경계 $np^2 \approx 0.60$ 이 1보다 한참 아래에 있고, 이것이 정확도를 보장한다.

**정규분포와의 관계.** $\lambda \approx 219$ 이면 $B(n, p)$ 와 $\text{Po}(\lambda)$ 모두 $N(\lambda, \lambda)$ 로 잘 근사된다. 이항분포의 분산은 $np(1-p) = \lambda(1 - 1/365) \approx 218.6$ 이고 푸아송분포의 분산은 $\lambda \approx 219.2$ 이다. 표준편차의 상대적인 차이는 $0.2\%$ 도 되지 않는다.

**실용적인 이점.** $n = 80{,}000$ 에 대한 이항확률을 계산하려면 큰 이항계수를 다루어야 해서 수치적으로 값비싸다. 푸아송분포의 확률질량함수 $e^{-\lambda}\lambda^k / k!$ 는 계산하기가 훨씬 간단하며, 점화식 $P(k) = P(k-1) \cdot \lambda / k$ 를 쓰면 더욱 그렇다.

## 연습문제

**연습문제 1.** $\lambda = 80{,}000/365$ 인 푸아송 근사를 써서 $P(S_n > 250)$, $P(S_n > 240)$, $P(200 \leq S_n \leq 240)$ 을 계산하여라. 정확한 이항분포로 답을 확인하여라.

??? success "연습문제 1 풀이"

    ```python
    from scipy.stats import binom, poisson

    n = 80_000
    p = 1 / 365
    la = n * p

    targets = [
        ("P(S > 250)", lambda d, *a: 1 - d.cdf(250, *a)),
        ("P(S > 240)", lambda d, *a: 1 - d.cdf(240, *a)),
        ("P(200 ≤ S ≤ 240)", lambda d, *a: d.cdf(240, *a) - d.cdf(199, *a)),
    ]

    print(f"{'Probability':>20} {'Binomial':>12} {'Poisson':>12} {'|Diff|':>12}")
    print("-" * 58)
    for label, func in targets:
        b = func(binom, n, p)
        po = func(poisson, la)
        print(f"{label:>20} {b:>12.6f} {po:>12.6f} {abs(b - po):>12.2e}")
    ```

    대체로 다음과 같은 결과가 나온다.

    | 확률 | 이항분포 | 푸아송분포 | 차이 |
    |:---|:---:|:---:|:---:|
    | $P(S > 250)$ | 0.0187 | 0.0188 | $\sim 10^{-4}$ |
    | $P(S > 240)$ | 0.0749 | 0.0752 | $\sim 10^{-4}$ |
    | $P(200 \leq S \leq 240)$ | 0.8468 | 0.8463 | $\sim 10^{-4}$ |

    푸아송 근사는 정확한 이항분포와 소수점 넷째 자리까지 일치한다.

**연습문제 2.** 어떤 도시에서 한 해에 $n = 200{,}000$ 건의 결혼이 이루어진다고 하자. $\lambda$ 를 계산하고 푸아송 근사를 써서 생일이 같은 부부가 적어도 600쌍일 확률을 어림하여라. 여기서도 푸아송 근사를 믿을 만한가? 르캉 경계를 확인하여라.

??? success "연습문제 2 풀이"

    $n = 200{,}000$ 이고 $p = 1/365$ 이면 다음과 같다.

    $$
    \lambda = \frac{200{,}000}{365} \approx 547.95
    $$

    르캉 경계는 다음과 같다.

    $$
    np^2 = 200{,}000 \cdot \left(\frac{1}{365}\right)^2 \approx 1.50
    $$

    ```python
    from scipy.stats import binom, poisson

    n = 200_000
    p = 1 / 365
    la = n * p

    b = 1 - binom.cdf(599, n, p)
    po = 1 - poisson.cdf(599, la)
    print(f"Binomial: P(S ≥ 600) = {b:.6f}")
    print(f"Poisson:  P(S ≥ 600) = {po:.6f}")
    print(f"Le Cam bound: np² = {n * p**2:.4f}")
    ```

    르캉 경계는 $1.50$ 으로 $1$ 보다 크지만 여전히 그리 크지 않다. 근사는 아직 꽤 좋지만($10^{-3}$ 정도의 차이) $n = 80{,}000$ 인 경우만큼 정밀하지는 않다. $\lambda$ 가 아주 클 때는 정규근사 $N(\lambda, \lambda)$ 를 쓰는 편이 나을 수 있다.

**연습문제 3.** 이 모의실험은 100,000개의 표본을 쓴다. 이항분포 표본과 푸아송분포 표본 각각에서 $P(S_n > 250)$ 을 어림하여라. 각 추정값에 대해 $95\%$ 신뢰구간을 계산하고 두 구간이 겹치는지 확인하여라.

??? success "연습문제 3 풀이"

    ```python
    import numpy as np

    np.random.seed(42)
    n, p = 80_000, 1 / 365
    la = n * p
    n_samples = 100_000

    bin_s = np.random.binomial(n, p, n_samples)
    po_s = np.random.poisson(la, n_samples)

    for label, samples in [("Binomial", bin_s), ("Poisson", po_s)]:
        phat = np.mean(samples > 250)
        se = np.sqrt(phat * (1 - phat) / n_samples)
        lo, hi = phat - 1.96 * se, phat + 1.96 * se
        print(f"{label:>10}: P(S > 250) ≈ {phat:.4f}, 95% CI: [{lo:.4f}, {hi:.4f}]")
    ```

    두 신뢰구간 모두 $0.019$ 근처를 중심으로 하며 크게 겹친다. 이 꼬리확률에 관한 한 두 분포가 통계적으로 구별되지 않는 결과를 냄을 확인해 준다.

**연습문제 4.** 저마다 확률이 $p = 1/365$ 인 독립인 사건 $A_1, \ldots, A_n$ 에 대하여 개수 $S_n = \sum_{i=1}^n \mathbf{1}_{A_i}$ 이 다음을 만족함을 증명하여라.

$$
d_{\text{TV}}\!\left(\mathcal{L}(S_n),\; \text{Po}(np)\right) \leq \frac{np}{365}
$$

여기서 $d_{\text{TV}}$ 는 전변동거리를 나타낸다.

??? success "연습문제 4 풀이"

    르캉 부등식에 따라, $P(X_i = 1) = p_i$ 인 독립인 베르누이확률변수 $X_i$ 에 대하여 $\mathcal{L}(S_n)$ 과 $\text{Po}(\lambda)$ 사이의 전변동거리는 다음을 만족한다.

    $$
    d_{\text{TV}}\!\left(\mathcal{L}(S_n),\; \text{Po}(\lambda)\right) \leq \sum_{i=1}^{n} p_i^2
    $$

    여기서 $\lambda = \sum_{i=1}^n p_i$ 이다. 지금 다루는 경우에는 모든 $i$ 에 대해 $p_i = p = 1/365$ 이므로 다음을 얻는다.

    $$
    \sum_{i=1}^{n} p_i^2 = n p^2 = np \cdot p = \frac{np}{365}
    $$

    $\square$

**연습문제 5.** 이항분포 표본과 푸아송분포 표본을 견주는 겹친 히스토그램(계단 그림) 하나만 그리도록 모의실험을 고쳐라. 여기에 세 번째 곡선으로 정수 점에서 값을 매긴 정규근사 $N(\lambda, \lambda)$ 를 덧붙여라. 눈으로 볼 때 이항분포에 더 가까운 근사는 푸아송분포인가 정규분포인가?

??? success "연습문제 5 풀이"

    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import norm

    np.random.seed(42)
    n, p = 80_000, 1 / 365
    la = n * p
    n_samples = 100_000

    bin_s = np.random.binomial(n, p, n_samples)
    po_s = np.random.poisson(la, n_samples)

    bins = np.arange(150, 300)
    plt.figure(figsize=(10, 5))
    plt.hist(bin_s, bins=bins, density=True, histtype="step",
             linewidth=2, color="b", label="Binomial")
    plt.hist(po_s, bins=bins, density=True, histtype="step",
             linewidth=2, color="r", alpha=0.7, label="Poisson")

    # 정규근사
    x = np.arange(150, 300)
    plt.plot(x, norm.pdf(x, la, np.sqrt(la)), 'g--', linewidth=2, label="Normal")

    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.title(f"Binomial vs Poisson vs Normal (n={n:,}, λ={la:.1f})")
    plt.tight_layout()
    plt.show()
    ```

    $\lambda \approx 219$ 이면 세 분포가 거의 같다. $\lambda$ 가 충분히 커서 중심극한정리에 따라 푸아송분포 자체도 정규분포로 잘 근사되므로, 푸아송 근사와 정규근사 모두 훌륭하다. 세 곡선은 거의 완벽하게 포개진다. 다만 정규분포는 연속인 밀도이고 이항분포와 푸아송분포는 이산이라는 점이 다르다.
