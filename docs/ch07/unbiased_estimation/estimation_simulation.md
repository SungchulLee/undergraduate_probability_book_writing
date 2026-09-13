# 추정 모의실험: 편향추정량과 불편추정량

이 페이지에서는 모분산의 편향추정량과 불편추정량을 견주어 보는 파이썬 모의실험을 다룬다. 이미 알고 있는 정규분포에서 표본을 뽑아 보면, $n$ 으로 나눌 때 $\sigma^2$ 를 늘 낮추어 잡는 모습과 $n - 1$ 로 나눌 때 그 편향이 바로잡히는 모습을 눈으로 볼 수 있다. 또한 표본 크기가 커질 때 두 추정량이 어떻게 수렴해 가는지도 함께 보인다.

## 배경

평균이 $\mu$, 분산이 $\sigma^2$ 인 분포에서 뽑은 i.i.d. 표본 $X_1, X_2, \ldots, X_n$ 이 주어졌을 때 **표본평균**

$$
\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i
$$

은 $\mu$ 의 불편추정량이다. 곧 $E[\bar{X}] = \mu$ 이다.

분산에 대해서는 자연스러운 추정량이 둘 나온다. **편향 표본분산**은 $n$ 으로 나눈다.

$$
\tilde{S}^2 = \frac{1}{n} \sum_{i=1}^n (X_i - \bar{X})^2
$$

그 기댓값은 다음과 같다.

$$
E[\tilde{S}^2] = \frac{n-1}{n} \sigma^2 < \sigma^2
$$

곧 참인 분산을 늘 낮추어 잡는다. **불편 표본분산**(베셀 보정)은 $n - 1$ 로 나눈다.

$$
S^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2
$$

이것은 $E[S^2] = \sigma^2$ 를 만족한다. 여기서 $n - 1$ 이라는 값은 **자유도**를 나타낸다. $\mu$ 를 $\bar{X}$ 로 추정하느라 자유도 하나를 썼기 때문이다.

## 코드

```python
"""추정 모의실험: 평균과 분산의 불편추정을 보인다."""
import numpy as np
import matplotlib.pyplot as plt


def main():
    np.random.seed(42)

    true_mu = 2.0
    true_sigma = 2.0
    n_samples = 1000

    # 정규분포 표본 생성
    x = np.random.normal(true_mu, true_sigma, size=n_samples)

    # 불편추정량
    mu_hat = np.mean(x)
    sigma2_hat_unbiased = np.sum((x - mu_hat) ** 2) / (n_samples - 1)
    sigma2_hat_biased = np.sum((x - mu_hat) ** 2) / n_samples

    # 겹쳐 그릴 확률밀도함수
    xp = np.linspace(mu_hat - 4 * np.sqrt(sigma2_hat_unbiased),
                     mu_hat + 4 * np.sqrt(sigma2_hat_unbiased), 200)
    pdf_estimated = (np.exp(-(xp - mu_hat) ** 2 / (2 * sigma2_hat_unbiased))
                     / np.sqrt(2 * np.pi * sigma2_hat_unbiased))
    pdf_true = (np.exp(-(xp - true_mu) ** 2 / (2 * true_sigma ** 2))
                / np.sqrt(2 * np.pi * true_sigma ** 2))

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # 왼쪽 패널: 히스토그램에 추정된 확률밀도함수와 참인 확률밀도함수를 겹쳐 그린다
    axes[0].hist(x, bins=30, density=True, color="steelblue",
                 edgecolor="white", alpha=0.7, label="Samples")
    axes[0].plot(xp, pdf_estimated, "--r", linewidth=2,
                 label=f"Estimated: N({mu_hat:.2f}, {sigma2_hat_unbiased:.2f})")
    axes[0].plot(xp, pdf_true, "-k", linewidth=1.5, alpha=0.5,
                 label=f"True: N({true_mu}, {true_sigma ** 2})")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("Density")
    axes[0].set_title("Sample Histogram with Estimated Normal PDF")
    axes[0].legend(fontsize=9)
    axes[0].grid(True, alpha=0.3)

    # 오른쪽 패널: 표본분산 추정량들의 수렴 모습
    n_range = np.arange(2, n_samples + 1)
    biased_variances = np.array([np.sum((x[:n] - np.mean(x[:n])) ** 2) / n
                                 for n in n_range])
    unbiased_variances = np.array([np.sum((x[:n] - np.mean(x[:n])) ** 2) / (n - 1)
                                   for n in n_range])

    axes[1].plot(n_range, biased_variances, linewidth=0.8, alpha=0.7,
                 label="Biased ($\\div n$)")
    axes[1].plot(n_range, unbiased_variances, linewidth=0.8, alpha=0.7,
                 label="Unbiased ($\\div (n-1)$)")
    axes[1].axhline(true_sigma ** 2, color="red", linestyle="--", linewidth=1.5,
                    label=f"True $\\sigma^2$ = {true_sigma ** 2}")
    axes[1].set_xlabel("Sample Size n")
    axes[1].set_ylabel("Estimated Variance")
    axes[1].set_title("Biased vs Unbiased Variance Estimators")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("estimation_simulation.png", dpi=150, bbox_inches="tight")
    plt.show()

    print(f"True parameters:     mu = {true_mu}, sigma^2 = {true_sigma ** 2}")
    print(f"Estimated (unbiased): mu_hat = {mu_hat:.4f}, sigma^2_hat = {sigma2_hat_unbiased:.4f}")
    print(f"Estimated (biased):   sigma^2_hat = {sigma2_hat_biased:.4f}")


if __name__ == "__main__":
    main()
```

## 실행 결과

이 스크립트를 돌리면 나란히 놓인 두 개의 그림과 글로 된 요약이 나온다.

**왼쪽 패널**: 1,000개의 표본으로 그린 히스토그램 위에 ($\hat{\mu}$ 와 $S^2$ 를 쓴) 추정된 정규 확률밀도함수와 참인 정규 확률밀도함수를 겹쳐 그렸다. 두 곡선이 거의 포개지므로 표본에서 얻은 추정값이 참값에 가깝다는 것을 확인할 수 있다.

**오른쪽 패널**: 표본 크기 $n$ 을 $n = 2$ 에서 $n = 1000$ 까지 늘려 가며 편향추정값과 불편추정값을 차례로 그린 것이다. 두 추정량 모두 $n$ 이 작을 때는 요동이 심하지만 $n$ 이 커질수록 참값 $\sigma^2 = 4$ 로 다가간다. 편향추정량은 줄곧 불편추정량보다 조금씩 아래에 놓인다.

**콘솔 출력** (전형적인 예):

```
True parameters:     mu = 2.0, sigma^2 = 4.0
Estimated (unbiased): mu_hat = 1.9754, sigma^2_hat = 3.8276
Estimated (biased):   sigma^2_hat = 3.8238
```

## 뜻풀이

이 모의실험은 편향추정과 불편추정에 관하여 몇 가지 중요한 점을 보여 준다.

1. **표본평균은 잘 작동한다.** 표본이 $n = 1000$ 개일 때 $\hat{\mu} \approx 1.98$ 로 참값 $\mu = 2.0$ 에 가깝다. 표준오차 $\sigma / \sqrt{n} = 2 / \sqrt{1000} \approx 0.063$ 이 이 정도의 정확도를 예고한다.

2. **$n$ 이 크면 편향추정량과 불편추정량은 거의 같다.** $n$ 으로 나누는 것과 $n - 1$ 로 나누는 것의 차이는 $S^2 / n$ 인데 $n$ 이 커질수록 줄어든다. $n = 1000$ 이면 그 차이는 무시할 만하다.

3. **$n$ 이 작을 때는 차이가 문제가 된다.** 수렴 그림을 보면 $n$ 이 작을 때(이를테면 $n < 50$) 두 곡선이 눈에 띄게 갈라진다. 그 구간에서는 편향추정량이 $\sigma^2$ 를 뚜렷이 낮추어 잡는다.

4. **두 추정량 모두 일치추정량이다.** $\tilde{S}^2$ 가 편향되어 있기는 해도 $n \to \infty$ 일 때 두 추정량 모두 $\sigma^2$ 로 수렴한다. 불편성은 유한 표본의 성질이고 일치성은 점근적인 성질이다.

## 연습문제

**연습문제 1.** `true_sigma = 5.0`, `n_samples = 50` 으로 모의실험을 돌려 보아라. $\hat{\mu}$ 와 편향 분산추정값, 불편 분산추정값을 보고하여라. 어느 추정량이 $\sigma^2 = 25$ 에서 더 멀리 떨어져 있는가?

??? success "연습문제 1 풀이"
    ```python
    import numpy as np
    np.random.seed(42)
    x = np.random.normal(2.0, 5.0, size=50)
    mu_hat = np.mean(x)
    s2_unbiased = np.sum((x - mu_hat)**2) / 49
    s2_biased = np.sum((x - mu_hat)**2) / 50
    print(f"mu_hat = {mu_hat:.4f}")
    print(f"Unbiased S^2 = {s2_unbiased:.4f}")
    print(f"Biased S^2   = {s2_biased:.4f}")
    ```

    전형적인 출력은 $\hat{\mu} \approx 1.74$, $S^2 \approx 23.92$ (불편), $\tilde{S}^2 \approx 23.44$ (편향)이다. 편향추정량이 참값 $\sigma^2 = 25$ 에서 더 멀리 떨어져 있고, 보정 계수가 $(n-1)/n = 49/50 = 0.98$ 이어서 편향추정값을 2%만큼 줄이므로 $n = 1000$ 일 때보다 차이가 더 두드러진다.

---

**연습문제 2.** 자료집합 하나가 아니라 $N(0, 4)$ 에서 크기 $n = 10$ 인 자료집합을 $M = 10{,}000$ 개 만들어 보아라. 모든 자료집합에 걸쳐 편향 분산추정값과 불편 분산추정값의 평균을 구하여 $E[S^2] \approx \sigma^2 = 4$ 와 $E[\tilde{S}^2] \approx \frac{n-1}{n} \sigma^2 = 3.6$ 을 확인하여라.

??? success "연습문제 2 풀이"
    ```python
    import numpy as np
    np.random.seed(42)
    M, n, sigma2 = 10_000, 10, 4.0
    biased_list, unbiased_list = [], []
    for _ in range(M):
        x = np.random.normal(0, np.sqrt(sigma2), size=n)
        biased_list.append(np.var(x, ddof=0))
        unbiased_list.append(np.var(x, ddof=1))
    print(f"E[S^2 (unbiased)] = {np.mean(unbiased_list):.4f}  (expect 4.0)")
    print(f"E[S^2 (biased)]   = {np.mean(biased_list):.4f}  (expect 3.6)")
    ```

    전형적인 출력은 불편추정값의 평균이 약 4.00, 편향추정값의 평균이 약 3.60 으로, 다음 이론값과 들어맞는다.

    $$
    E[S^2] = \sigma^2 = 4, \qquad E[\tilde{S}^2] = \frac{n-1}{n}\sigma^2 = \frac{9}{10} \cdot 4 = 3.6
    $$

---

**연습문제 3.** $n \to \infty$ 일 때 $\tilde{S}^2$ 의 편향이 사라짐을, 곧 $\tilde{S}^2$ 가 **점근적으로 불편**임을 증명하여라.

??? success "연습문제 3 풀이"
    $\tilde{S}^2$ 의 편향은 다음과 같다.

    $$
    \text{편향}(\tilde{S}^2) = E[\tilde{S}^2] - \sigma^2 = \frac{n-1}{n}\sigma^2 - \sigma^2 = -\frac{\sigma^2}{n}
    $$

    $n \to \infty$ 이면 다음과 같다.

    $$
    \left|\text{편향}(\tilde{S}^2)\right| = \frac{\sigma^2}{n} \to 0
    $$

    그러므로 $\tilde{S}^2$ 는 점근적으로 불편이다. 나아가 $\text{Var}(\tilde{S}^2) \to 0$ 임도 보일 수 있으므로 $\tilde{S}^2$ 는 $\sigma^2$ 의 일치추정량이다. $\square$

---

**연습문제 4.** 정규분포 대신 $\text{Exponential}(\lambda = 1)$ 에서 표본을 뽑도록 모의실험을 고쳐 보아라. $\bar{X}$ 와 $S^2$ 의 불편성이 여전히 성립하는가? 그 까닭을 설명하여라.

??? success "연습문제 4 풀이"
    ```python
    import numpy as np
    np.random.seed(42)
    M, n, lam = 10_000, 20, 1.0
    mu_true = 1 / lam        # = 1.0
    sigma2_true = 1 / lam**2  # = 1.0
    means, s2_vals = [], []
    for _ in range(M):
        x = np.random.exponential(1 / lam, size=n)
        means.append(np.mean(x))
        s2_vals.append(np.var(x, ddof=1))
    print(f"E[X_bar] = {np.mean(means):.4f}  (expect {mu_true})")
    print(f"E[S^2]   = {np.mean(s2_vals):.4f}  (expect {sigma2_true})")
    ```

    전형적인 출력은 $E[\bar{X}] \approx 1.00$, $E[S^2] \approx 1.00$ 이다. $\bar{X}$ 와 $S^2$ 의 불편성은 정규성에 기대지 **않는다**. 증명에 쓰인 것은 기댓값의 선형성, i.i.d. 가정, 그리고 분산의 정의뿐이며 어느 것도 정규분포를 필요로 하지 않는다. 표본평균은 평균이 유한한 어떤 분포에서도 불편이고, $S^2$ 는 분산이 유한한 어떤 분포에서도 불편이다.

---

**연습문제 5.** 평균이 $\mu$, 분산이 $\sigma^2$ 인 i.i.d. 확률변수 $X_1, \ldots, X_n$ 에 대하여 $T = \frac{1}{n+1} \sum_{i=1}^n (X_i - \bar{X})^2$ 이라 하자. $E[T]$ 를 구하고 $T$ 를 $\sigma^2$ 의 추정량으로 볼 때의 편향을 구하여라.

??? success "연습문제 5 풀이"
    다음을 이미 알고 있다.

    $$
    E\!\left[\sum_{i=1}^n (X_i - \bar{X})^2\right] = (n-1)\sigma^2
    $$

    그러므로 다음을 얻는다.

    $$
    E[T] = \frac{1}{n+1} \cdot (n-1)\sigma^2 = \frac{n-1}{n+1}\sigma^2
    $$

    편향은 다음과 같다.

    $$
    \text{편향}(T) = E[T] - \sigma^2 = \frac{n-1}{n+1}\sigma^2 - \sigma^2 = -\frac{2\sigma^2}{n+1}
    $$

    그러므로 $T$ 는 편향이 $-\sigma^2 / n$ 인 $\tilde{S}^2$ 보다도 $\sigma^2$ 를 더 심하게 낮추어 잡는다. 실제로 모든 $n \geq 1$ 에 대하여 $|{-2/(n+1)}| > |{-1/n}|$ 이다.

---

**연습문제 6.** 편향이 있는데도 편향추정량 $\tilde{S}^2$ 의 평균제곱오차가 불편추정량 $S^2$ 의 평균제곱오차보다 작을 수 있음을 보여라. 어떤 조건에서 그러한가?

??? success "연습문제 6 풀이"
    평균제곱오차는 다음과 같이 쪼갤 수 있다.

    $$
    \text{MSE}(\hat{\theta}) = \text{Var}(\hat{\theta}) + [\text{편향}(\hat{\theta})]^2
    $$

    i.i.d. 정규표본에서는 $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$ 이므로 $\text{Var}(S^2) = \frac{2\sigma^4}{n-1}$ 이다.

    $\tilde{S}^2 = \frac{n-1}{n} S^2$ 이므로 다음을 얻는다.

    $$
    \text{Var}(\tilde{S}^2) = \left(\frac{n-1}{n}\right)^2 \text{Var}(S^2) = \frac{(n-1)^2}{n^2} \cdot \frac{2\sigma^4}{n-1} = \frac{2(n-1)\sigma^4}{n^2}
    $$

    그리고 $\text{편향}(\tilde{S}^2) = -\sigma^2/n$ 이다. 그러므로 다음과 같다.

    $$
    \text{MSE}(\tilde{S}^2) = \frac{2(n-1)\sigma^4}{n^2} + \frac{\sigma^4}{n^2} = \frac{(2n-1)\sigma^4}{n^2}
    $$

    불편추정량에서는 $\text{편향}(S^2) = 0$ 이므로 다음과 같다.

    $$
    \text{MSE}(S^2) = \text{Var}(S^2) = \frac{2\sigma^4}{n-1}
    $$

    둘을 견주면 다음을 얻는다.

    $$
    \text{MSE}(\tilde{S}^2) < \text{MSE}(S^2) \iff \frac{2n-1}{n^2} < \frac{2}{n-1} \iff (2n-1)(n-1) < 2n^2
    $$

    전개하면 $2n^2 - 3n + 1 < 2n^2$ 이고 이는 $-3n + 1 < 0$, 곧 $n > 1/3$ 으로 간단해진다. 이는 모든 $n \geq 1$ 에서 성립한다.

    그러므로 (정규성 아래에서) 표본 크기가 $n \geq 2$ 인 모든 경우에 편향추정량 $\tilde{S}^2$ 의 평균제곱오차가 불편추정량 $S^2$ 의 것보다 엄밀히 작다. 이는 불편성이 평균제곱오차의 뜻에서 최적을 보장하지 않음을 보여 준다. 편향을 조금 감수하는 대신 분산을 충분히 크게 줄일 수 있다면 그편이 이로울 수 있다. $\square$
