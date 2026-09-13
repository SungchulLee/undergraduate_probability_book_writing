# 이항분포의 푸아송 근사: 모의실험

이 모의실험은 $B(n, p)$ 와 $\text{Po}(\lambda)$ 에서 각각 표본을 뽑아 히스토그램을 나란히 그려 두 분포를 견주어 본다. $n$ 이 크고 $p$ 가 작으며 $\lambda = np$ 가 알맞은 크기일 때 두 히스토그램은 사실상 구별되지 않으며, 이는 푸아송 극한정리를 경험적으로 확인해 준다.

## 배경

**푸아송 극한정리**는 $p_n = \lambda / n$ 인 $X_n \sim B(n, p_n)$ 에 대하여, 고정된 각 $k \geq 0$ 에서 다음이 성립함을 말해 준다.

$$
P(X_n = k) \to \frac{e^{-\lambda} \lambda^k}{k!} \quad n \to \infty \text{ 일 때}
$$

실제로는 $n$ 이 크고 $p$ 가 작으며 $\lambda = np$ 가 알맞은 크기이면(이를테면 $\lambda \leq 20$ 정도) 이 근사가 정확하다. 아래 모의실험은 $n = 1000$, $p = 0.01$ 을 써서 $\lambda = 10$ 이 되도록 하였다.

확률질량함수를 해석적으로 견주는 대신 **몬테카를로** 방법을 쓴다. 두 분포에서 표본을 많이 뽑아 경험적 히스토그램을 겹쳐 그린다. 근사가 좋다면 두 히스토그램은 거의 같아야 한다.

## 코드

```python
"""이항분포의 푸아송 근사: n이 크고 p가 작을 때 히스토그램을 견주어 본다."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

N = 1000       # 큰 n
P = 0.01       # 작은 p
LA = N * P     # lambda = np = 10
N_SAMPLES = 10_000

bin_samples = np.random.binomial(N, P, N_SAMPLES)
po_samples = np.random.poisson(LA, N_SAMPLES)

fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(14, 4))

bins = np.arange(int(3 * LA))

ax0.hist(bin_samples, bins=bins, density=True, color="steelblue", edgecolor="black")
ax0.set_title(f"Binomial({N}, {P})")

ax1.hist(po_samples, bins=bins, density=True, color="steelblue", edgecolor="black")
ax1.set_title(f"Poisson({LA:.0f})")

ax2.hist(bin_samples, bins=bins, density=True, label="Binomial", color="b",
         alpha=1, histtype="step", linewidth=2)
ax2.hist(po_samples, bins=bins, density=True, label="Poisson", color="r",
         alpha=0.5, histtype="step", linewidth=2)
ax2.set_title("Overlay Comparison")
ax2.legend()

for ax in (ax0, ax1, ax2):
    ax.grid(True, alpha=0.3)

plt.suptitle("Poisson Approximation of Binomial", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("poisson_approx_binomial.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 실행 결과

이 스크립트는 세 개의 칸으로 이루어진 그림을 만든다.

1. **왼쪽 칸** -- $B(1000, 0.01)$ 에서 뽑은 10,000개 표본의 히스토그램이다. 분포는 $\lambda = 10$ 근처를 중심으로 종 모양을 이루며 오른쪽으로 살짝 치우쳐 있다.

2. **가운데 칸** -- $\text{Po}(10)$ 에서 뽑은 10,000개 표본의 히스토그램이다. 모양이 이항분포의 히스토그램과 눈으로는 똑같다.

3. **오른쪽 칸** -- 두 히스토그램을 계단 윤곽선으로 겹쳐 그린 것이다. 이항분포(파랑)와 푸아송분포(빨강)의 윤곽이 받침 전체에 걸쳐 거의 완벽하게 포개진다.

표본통계량은 대체로 다음과 같다.

| 통계량 | $B(1000, 0.01)$ | $\text{Po}(10)$ |
|:---|:---:|:---:|
| 표본평균 | $\approx 10.0$ | $\approx 10.0$ |
| 표본표준편차 | $\approx 3.1$ | $\approx 3.2$ |

## 뜻풀이

겹쳐 그린 칸에서 두 윤곽이 거의 완벽하게 포개진다는 것은, 실용적인 뜻에서 $B(1000, 0.01)$ 과 $\text{Po}(10)$ 이 본질적으로 같은 분포임을 확인해 준다. 이는 이론에서도 예상되는 바이다. 르캉 경계는 다음을 준다.

$$
\sum_{k=0}^{\infty} |P(X = k) - P(Y = k)| \leq 2 \sum_{i=1}^{n} p_i^2 = 2np^2 = 2 \cdot 1000 \cdot (0.01)^2 = 0.2
$$

그러므로 전변동거리는 많아야 $0.2$ 이고, 실제 차이는 이보다 훨씬 작다. $n = 1000$, $p = 0.01$ 이면 비 $p = \lambda/n = 0.01$ 이 충분히 작아 푸아송 극한 증명에 나오는 고차 보정항이 무시할 만해진다.

이 모의실험은 푸아송 근사가 평균($\lambda = np = 10$ 으로 정확히 같다)과 분산($np(1-p) = 9.9 \approx \lambda = 10$)을 모두 지켜 준다는 것도 보여 준다.

## 연습문제

**연습문제 1.** $\lambda = 10$ 을 그대로 두고 $n = 100$, $p = 0.1$ 이 되도록 모의실험을 고쳐라. 각 분포에서 10,000개의 표본을 뽑아 겹쳐 그린 히스토그램을 견주어 보아라. $n = 1000$, $p = 0.01$ 일 때만큼 근사가 눈으로 보기에 좋은가?

??? success "연습문제 1 풀이"

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(42)
    n, p = 100, 0.1
    la = n * p
    N_SAMPLES = 10_000

    bin_samples = np.random.binomial(n, p, N_SAMPLES)
    po_samples = np.random.poisson(la, N_SAMPLES)

    plt.figure(figsize=(8, 4))
    bins = np.arange(int(3 * la))
    plt.hist(bin_samples, bins=bins, density=True, label="Binomial(100, 0.1)",
             color="b", alpha=1, histtype="step", linewidth=2)
    plt.hist(po_samples, bins=bins, density=True, label="Poisson(10)",
             color="r", alpha=0.5, histtype="step", linewidth=2)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.title("Overlay: B(100, 0.1) vs Po(10)")
    plt.tight_layout()
    plt.show()
    ```

    $n = 100$, $p = 0.1$ 이면 근사가 눈에 띄게 나빠진다. 이항분포의 분산은 $np(1-p) = 9$ 인데 $\text{Po}(10)$ 의 분산은 $10$ 이므로 푸아송분포의 히스토그램이 조금 더 넓게 퍼진다. 르캉 경계는 $np^2 = 100 \cdot 0.01 = 1.0$ 으로 $n = 1000$ 인 경우보다 열 배나 크다. 근사가 정확하려면 $p$ 가 작아야 함을 확인해 준다.

**연습문제 2.** $n = 1000$, $p = 0.01$ 에 대하여 $B(1000, 0.01)$ 과 $\text{Po}(10)$ 각각에서 $k = 0, 1, \ldots, 20$ 의 정확한 확률 $P(X = k)$ 를 계산하여라. 절대 차이 $|P_{\text{Bin}}(k) - P_{\text{Poi}}(k)|$ 가 최대가 되는 $k$ 의 값을 찾아라.

??? success "연습문제 2 풀이"

    ```python
    import numpy as np
    from scipy.stats import binom, poisson

    n, p = 1000, 0.01
    la = n * p

    print(f"{'k':>4} {'Binomial':>14} {'Poisson':>14} {'|Diff|':>14}")
    print("-" * 48)
    max_diff, max_k = 0, 0
    for k in range(21):
        b = binom.pmf(k, n, p)
        po = poisson.pmf(k, la)
        diff = abs(b - po)
        if diff > max_diff:
            max_diff, max_k = diff, k
        print(f"{k:>4} {b:>14.8f} {po:>14.8f} {diff:>14.2e}")

    print(f"\nMaximum difference: {max_diff:.4e} at k = {max_k}")
    ```

    최대 차이는 분포의 최빈값 가까이($k = 10$ 언저리)에서 나타나며 그 크기는 $10^{-4}$ 정도이다. 두 분포가 매우 잘 들어맞음을 확인해 준다.

**연습문제 3.** $n = 1000$, $p = 0.01$ 로 두되 `N_SAMPLES` 를 $10^5$ 으로, 다시 $10^6$ 으로 늘려 모의실험을 돌려라. 겹쳐 그린 그림의 품질은 어떻게 달라지는가? 표본 수를 늘리는 것이 눈으로 보는 비교에 왜 영향을 주는지 설명하여라.

??? success "연습문제 3 풀이"

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(42)
    n, p = 1000, 0.01
    la = n * p

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    for ax, ns in zip(axes, [10_000, 100_000, 1_000_000]):
        bins = np.arange(30)
        bin_s = np.random.binomial(n, p, ns)
        po_s = np.random.poisson(la, ns)
        ax.hist(bin_s, bins=bins, density=True, label="Binomial",
                color="b", alpha=1, histtype="step", linewidth=2)
        ax.hist(po_s, bins=bins, density=True, label="Poisson",
                color="r", alpha=0.5, histtype="step", linewidth=2)
        ax.set_title(f"N = {ns:,}")
        ax.legend()
        ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    ```

    표본이 많아질수록 큰수의 법칙에 따라 경험적 히스토그램은 저마다의 참된 확률질량함수로 수렴한다. 곧 눈으로 보는 비교가 실제 확률질량함수의 차이를 더 충실하게 비추게 된다. 표본이 $10^6$ 개이면 작은 확률질량함수의 차이까지 드러나지만, 참된 확률질량함수 자체가 가깝기 때문에 이항분포와 푸아송분포의 히스토그램은 여전히 거의 완벽하게 포개진다.

**연습문제 4.** 고정된 $\lambda > 0$ 과 $k \geq 0$ 에 대하여, $X_n \sim B(n, \lambda/n)$ 일 때 다음이 성립함을 증명하여라.

$$
P(X_n = k) - \frac{e^{-\lambda} \lambda^k}{k!} = O\!\left(\frac{1}{n}\right)
$$

??? success "연습문제 4 풀이"

    $p = \lambda/n$ 으로 두고 이항분포의 확률질량함수를 펼쳐 적자.

    $$
    P(X_n = k) = \frac{\lambda^k}{k!} \cdot \prod_{j=0}^{k-1}\left(1 - \frac{j}{n}\right) \cdot \left(1 - \frac{\lambda}{n}\right)^{n-k}
    $$

    내림 계승에서 온 인수는 테일러 전개로 다음과 같이 된다.

    $$
    \prod_{j=0}^{k-1}\left(1 - \frac{j}{n}\right) = 1 - \frac{1}{n}\sum_{j=0}^{k-1} j + O\!\left(\frac{1}{n^2}\right) = 1 - \frac{k(k-1)}{2n} + O\!\left(\frac{1}{n^2}\right)
    $$

    거듭제곱 인수는 $\ln(1 - \lambda/n) = -\lambda/n - \lambda^2/(2n^2) - \cdots$ 를 써서 다음과 같이 된다.

    $$
    \left(1 - \frac{\lambda}{n}\right)^{n-k} = e^{(n-k)\ln(1-\lambda/n)} = e^{-\lambda} \cdot e^{\lambda^2/(2n) + k\lambda/n + O(1/n^2)} = e^{-\lambda}\left(1 + \frac{\lambda^2 + 2k\lambda}{2n} + O\!\left(\frac{1}{n^2}\right)\right)
    $$

    이 둘을 합치면 다음을 얻는다.

    $$
    P(X_n = k) = \frac{e^{-\lambda}\lambda^k}{k!}\left(1 + \frac{\lambda^2 + 2k\lambda - k(k-1)}{2n} + O\!\left(\frac{1}{n^2}\right)\right)
    $$

    그러므로 차이는 다음과 같다.

    $$
    P(X_n = k) - \frac{e^{-\lambda}\lambda^k}{k!} = \frac{e^{-\lambda}\lambda^k}{k!} \cdot \frac{\lambda^2 + 2k\lambda - k(k-1)}{2n} + O\!\left(\frac{1}{n^2}\right) = O\!\left(\frac{1}{n}\right)
    $$

    $\square$

**연습문제 5.** 이 모의실험은 결과를 되풀이할 수 있도록 `np.random.seed(42)` 를 쓴다. 씨앗값을 없애고 스크립트를 다섯 번 돌려라. 그때마다 두 경험적 누적분포함수 사이의 콜모고로프–스미르노프 통계량 $D_n = \max_k |\hat{F}_{\text{Bin}}(k) - \hat{F}_{\text{Poi}}(k)|$ 을 계산하여라. 다섯 값을 적고 그 크기에 대해 설명하여라.

??? success "연습문제 5 풀이"

    ```python
    import numpy as np
    from scipy.stats import ks_2samp

    n, p = 1000, 0.01
    la = n * p
    N_SAMPLES = 10_000

    for trial in range(5):
        bin_s = np.random.binomial(n, p, N_SAMPLES)
        po_s = np.random.poisson(la, N_SAMPLES)
        stat, pval = ks_2samp(bin_s, po_s)
        print(f"Trial {trial+1}: D = {stat:.4f}, p-value = {pval:.4f}")
    ```

    대체로 다음과 같은 결과가 나온다.

    ```
    Trial 1: D = 0.0102, p-value = 0.6731
    Trial 2: D = 0.0089, p-value = 0.8012
    Trial 3: D = 0.0115, p-value = 0.5284
    Trial 4: D = 0.0078, p-value = 0.8923
    Trial 5: D = 0.0097, p-value = 0.7245
    ```

    콜모고로프–스미르노프 통계량이 모두 작고($D \approx 0.01$) $p$-값이 크므로, 두 표본을 통계적으로 구별할 수 없다. 이는 $B(1000, 0.01)$ 과 $\text{Po}(10)$ 이 사실상 같은 분포를 만들어 냄을 확인해 준다.
