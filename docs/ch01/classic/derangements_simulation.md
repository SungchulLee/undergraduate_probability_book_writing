# 완전순열 모의실험

이 쪽에서는 무작위로 고른 순열이 완전순열일(고정점이 하나도 없을) 확률을 몬테카를로 모의실험으로 어림한다. 무작위 순열을 수만 개 만들어 고정점이 있는지 살펴보면, 이 확률이 $e^{-1} \approx 0.3679$ 로 다가감을 눈으로 확인할 수 있다. 완전순열 이론의 고전적인 결과가 그대로 나타나는 것이다. 또한 큰 무작위 순열의 고정점 개수가 대략 Poisson(1) 분포를 따른다는 것도 이 모의실험에서 드러난다.

## 배경

$\{1, 2, \ldots, n\}$ 의 **완전순열**이란 모든 $i$ 에 대하여 $\sigma(i) \neq i$ 를 만족하는 순열 $\sigma$ 를 말한다. 완전순열의 개수 $D_n$ 은 포함배제 공식을 만족한다.

$$
D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}
$$

따라서 $\{1, 2, \ldots, n\}$ 의 순열을 고르게 무작위로 하나 고를 때 그것이 완전순열일 확률은 다음과 같다.

$$
P(\text{완전순열}) = \frac{D_n}{n!} = \sum_{k=0}^{n} \frac{(-1)^k}{k!}
$$

$e^{-x}$ 의 매클로린 급수에 $x = 1$ 을 넣으면 $e^{-1} = \sum_{k=0}^{\infty} \frac{(-1)^k}{k!}$ 이므로 다음을 얻는다.

$$
P(\text{완전순열}) \xrightarrow{n \to \infty} e^{-1} \approx 0.3679
$$

!!! note "고정점의 푸아송 근사"
    확률론의 더 깊은 결과에 따르면, $n \to \infty$ 일 때 무작위 순열의 고정점 개수는 $\text{Poisson}(1)$ 확률변수로 분포수렴한다. 특히 고정점이 정확히 $k$ 개일 확률은 $e^{-1}/k!$ 로 다가간다. $k = 0$ 인 경우가 바로 완전순열의 확률 $e^{-1}$ 이다.

## 코드

```python
"""완전순열 모의실험: 무작위 순열에 고정점이 하나도 없을 확률을 어림한다."""
import numpy as np
import matplotlib.pyplot as plt


def main():
    n = 100                    # 순열의 크기
    n_simulations = 50000      # 몬테카를로 시행 횟수
    x = np.arange(n)

    # 완전순열(고정점이 없는 순열)의 누적 개수
    derangement_count = 0
    estimates = np.zeros(n_simulations)

    for i in range(n_simulations):
        y = np.random.permutation(n)
        if np.sum(x == y) == 0:
            derangement_count += 1
        estimates[i] = derangement_count / (i + 1)

    theoretical = np.exp(-1)

    # --- 모의실험 확률이 e^{-1} 로 다가가는 모습을 그린다 ---
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # 왼쪽 그림: 수렴
    axes[0].plot(estimates, linewidth=0.8, label="Simulated P(derangement)")
    axes[0].axhline(theoretical, color="red", linestyle="--", linewidth=1.5,
                    label=f"$e^{{-1}} \\approx {theoretical:.4f}$")
    axes[0].set_xlabel("Number of Simulations")
    axes[0].set_ylabel("Estimated Probability")
    axes[0].set_title("Convergence of Derangement Probability")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # 오른쪽 그림: 고정점 개수의 히스토그램
    fixed_point_counts = []
    for _ in range(n_simulations):
        y = np.random.permutation(n)
        fixed_point_counts.append(np.sum(x == y))

    axes[1].hist(fixed_point_counts, bins=np.arange(-0.5, max(fixed_point_counts) + 1.5),
                 density=True, color="steelblue", edgecolor="white", alpha=0.8,
                 label="Simulated")
    # Poisson(1) 확률질량함수를 겹쳐 그린다
    k_vals = np.arange(0, max(fixed_point_counts) + 1)
    poisson_pmf = np.exp(-1) * np.ones_like(k_vals, dtype=float)
    for k in k_vals:
        poisson_pmf[k] = np.exp(-1) / np.math.factorial(k)
    axes[1].plot(k_vals, poisson_pmf, "ro-", markersize=6, linewidth=1.5,
                 label="Poisson(1) PMF")
    axes[1].set_xlabel("Number of Fixed Points")
    axes[1].set_ylabel("Probability")
    axes[1].set_title("Distribution of Fixed Points (Approx Poisson)")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("derangements.png", dpi=150, bbox_inches="tight")
    plt.show()

    print(f"Simulated P(derangement) = {estimates[-1]:.4f}")
    print(f"Theoretical e^{{-1}}      = {theoretical:.4f}")


if __name__ == "__main__":
    main()
```

## 실행 결과

이 스크립트를 실행하면 글자 출력과 두 칸짜리 그림이 나온다.

**글자 출력** (실행할 때마다 값이 조금씩 달라진다):

```
Simulated P(derangement) = 0.3685
Theoretical e^{-1}      = 0.3679
```

**그림 설명:**

이 스크립트는 두 칸으로 이루어진 그림을 그린다.

- **왼쪽 그림 (수렴 그래프):** 완전순열 확률의 누적 추정값을 모의실험 횟수에 따라 그린다. 빨간 가로 점선은 이론값 $e^{-1} \approx 0.3679$ 를 나타낸다. 모의실험 곡선은 처음에는 크게 흔들리지만 시행 횟수가 늘어남에 따라 이론값 가까이에서 안정된다. 큰수의 법칙이 눈에 보이는 셈이다.

- **오른쪽 그림 (고정점 히스토그램):** 크기가 $n = 100$ 인 무작위 순열 50,000개에서 얻은 고정점 개수의 경험적 분포를 히스토그램으로 보여 준다. 그 위에 빨간 점을 선분으로 이어 $\text{Poisson}(1)$ 확률질량함수 $P(X = k) = e^{-1}/k!$ 를 겹쳐 그렸다. 히스토그램 막대와 푸아송 확률질량함수가 거의 맞아떨어지는 것을 보면 고정점에 대한 푸아송 근사가 잘 들어맞음을 알 수 있다.

!!! tip "재현성"
    실행할 때마다 똑같은 결과를 얻으려면 `main()` 의 맨 앞에 `np.random.seed(42)`(또는 아무 정수나)를 넣으면 된다.

## 뜻풀이

이 모의실험은 조합론과 확률론의 고전적인 결과 두 가지를 확인해 준다.

1. **완전순열의 확률은 $e^{-1}$ 로 다가간다.** 크기가 $n = 100$ 인 순열에서는 유한합 $\sum_{k=0}^{100} (-1)^k / k!$ 이 이미 기계 정밀도 수준에서 $e^{-1}$ 과 구별되지 않는다. 수렴 그래프를 보면 몬테카를로 추정값이 몇천 번의 시행 뒤에 이 값에 자리를 잡는다.

2. **고정점의 개수는 Poisson(1) 분포를 따른다.** 고정점 개수의 히스토그램은 $\text{Poisson}(1)$ 확률질량함수와 거의 완벽하게 맞아떨어진다. 이는 $n$ 이 클 때 지시확률변수 $\mathbf{1}[\sigma(i) = i]$ 들이 "거의 독립"이고 각각의 평균이 $1/n$ 이며 그 합의 평균이 $n \cdot (1/n) = 1$ 이기 때문이다. 푸아송 극한정리가 이를 엄밀하게 뒷받침한다.

!!! warning "표본이 작을 때의 주의점"
    $n$ 이 작으면(이를테면 $n \leq 5$) 푸아송 근사가 눈에 띄게 어긋난다. 부분합 $\sum_{k=0}^{n} (-1)^k/k!$ 이 아직 $e^{-1}$ 에 충분히 가까워지지 않아서 정확한 확률이 $e^{-1}/k!$ 에서 벗어나기 때문이다. 이 모의실험은 근사가 사실상 정확한 $n = 100$ 을 쓴다.

## 연습문제

**연습문제 1.**
$n = 100$ 대신 $n = 5$ 로 두고 모의실험을 돌려 보아라. 모의실험으로 얻은 완전순열 확률을 정확한 값 $D_5 / 5! = 44/120$ 과 견주어 보아라. 수렴 그래프는 $n = 100$ 일 때와 어떻게 다른가?

??? success "연습문제 1 풀이"
    코드에서 `n = 5` 로 두면 모의실험 확률이 대략 $44/120 \approx 0.3667$ 로 다가간다. 정확한 값은 다음과 같다.

    $$
    \frac{D_5}{5!} = \frac{44}{120} = \frac{11}{30} \approx 0.3667
    $$

    이는 $e^{-1} \approx 0.3679$ 보다 조금 작다. 부분합 $\sum_{k=0}^{5} (-1)^k/k! = 11/30$ 이 아직 완전히 수렴하지 않았기 때문이다. 수렴 그래프의 모양은 비슷하지만 가로 점근선이 $e^{-1}$ 이 아니라 $11/30$ 에 놓인다. 그 차이는 약 $0.0013$ 으로 작아서 눈으로는 가려내기 어렵다.

---

**연습문제 2.**
크기가 $n = 100$ 인 순열에서 $P(\text{고정점이 정확히 하나})$ 를 어림하도록 모의실험을 고쳐 보아라. 이론적으로 어떤 값이 나와야 하며, 모의실험 결과가 그와 맞는가?

??? success "연습문제 2 풀이"
    $P(\text{고정점이 정확히 하나})$ 를 어림하려면 완전순열인지 확인하는 부분을 다음과 같이 바꾼다.

    ```python
    if np.sum(x == y) == 1:
        derangement_count += 1
    ```

    이론적으로 고정점의 개수는 대략 $\text{Poisson}(1)$ 을 따르므로 다음을 얻는다.

    $$
    P(X = 1) = e^{-1} \cdot \frac{1^1}{1!} = e^{-1} \approx 0.3679
    $$

    모의실험 값도 대략 $0.3679$ 로 다가가야 한다. Poisson(1) 모형에서는 $P(\text{고정점이 0개}) = P(\text{고정점이 1개}) = e^{-1}$ 인데, 이는 눈에 띄는 우연이다.

---

**연습문제 3.**
포함배제 공식을 이용하여, $\{1, 2, \ldots, n\}$ 의 무작위 순열에 고정점이 하나도 없을 정확한 확률이 $\sum_{k=0}^{n} (-1)^k / k!$ 임을 보여라. 그리고 $n \to \infty$ 일 때 이 합이 $e^{-1}$ 로 수렴함을 증명하여라.

??? success "연습문제 3 풀이"
    $A_i$ 를 자리 $i$ 가 고정점이 되는 사건이라 하자. 포함배제에 따라 다음을 얻는다.

    $$
    P\!\left(\bigcup_{i=1}^n A_i\right) = \sum_{k=1}^{n} (-1)^{k+1} \binom{n}{k} \frac{(n-k)!}{n!}
    $$

    $\binom{n}{k} \cdot (n-k)!/n! = 1/k!$ 이므로 이는 다음과 같이 간단해진다.

    $$
    P\!\left(\bigcup_{i=1}^n A_i\right) = \sum_{k=1}^{n} \frac{(-1)^{k+1}}{k!}
    $$

    여집합 법칙에 따라 다음을 얻는다.

    $$
    P(\text{완전순열}) = 1 - \sum_{k=1}^{n} \frac{(-1)^{k+1}}{k!} = \sum_{k=0}^{n} \frac{(-1)^k}{k!}
    $$

    극한을 보기 위해 매클로린 급수 $e^x = \sum_{k=0}^{\infty} x^k / k!$ 가 모든 $x \in \mathbb{R}$ 에서 수렴함을 떠올리자. $x = -1$ 을 넣으면 다음을 얻는다.

    $$
    e^{-1} = \sum_{k=0}^{\infty} \frac{(-1)^k}{k!}
    $$

    부분합 $\sum_{k=0}^{n} (-1)^k / k!$ 이 이 급수로 수렴하므로 $n \to \infty$ 일 때 $P(\text{완전순열}) \to e^{-1}$ 이다. $\square$

---

**연습문제 4.**
이 모의실험은 고정점 히스토그램을 그리려고 순열 50,000개를 만든다. 모의실험으로 얻은 완전순열 확률 $\hat{p}$ 의 표준오차를 어림하고, 이를 이용하여 근사적인 95% 신뢰구간을 만들어라. 그 구간이 $e^{-1}$ 을 품는가?

??? success "연습문제 4 풀이"
    추정량 $\hat{p}$ 은 $N = 50{,}000$ 번의 시행에서 완전순열이 나온 표본비율이다. 각 시행은 성공확률이 $p = e^{-1}$ 인 베르누이 확률변수이다. 표준오차는 다음과 같다.

    $$
    \text{SE} = \sqrt{\frac{p(1-p)}{N}} = \sqrt{\frac{e^{-1}(1 - e^{-1})}{50000}}
    $$

    수치로 계산하면 다음과 같다.

    $$
    \text{SE} = \sqrt{\frac{0.3679 \times 0.6321}{50000}} \approx \sqrt{\frac{0.2325}{50000}} \approx 0.00216
    $$

    근사적인 95% 신뢰구간은 다음과 같다.

    $$
    \hat{p} \pm 1.96 \times \text{SE} \approx \hat{p} \pm 0.0042
    $$

    $\hat{p} \approx 0.3685$ 가 나온 보통의 실행이라면 구간은 대략 $(0.3643,\, 0.3727)$ 이다. $e^{-1} \approx 0.3679$ 가 이 구간 안에 있으므로 결과는 이론과 들어맞는다.

---

**연습문제 5.**
$\{1, 2, \ldots, n\}$ 의 고르게 무작위한 순열에서 고정점 개수의 기댓값이 모든 $n \geq 1$ 에 대하여 정확히 1임을 증명하여라.

??? success "연습문제 5 풀이"
    $i = 1, 2, \ldots, n$ 에 대하여 지시확률변수 $X_i = \mathbf{1}[\sigma(i) = i]$ 를 정의하자. 고정점의 총 개수는 $X = \sum_{i=1}^{n} X_i$ 이다. 기댓값의 선형성에 따라 다음을 얻는다.

    $$
    E[X] = \sum_{i=1}^{n} E[X_i] = \sum_{i=1}^{n} P(\sigma(i) = i)
    $$

    고르게 무작위한 순열에서는 각 $i$ 에 대하여 $P(\sigma(i) = i) = (n-1)!/n! = 1/n$ 이다. 따라서 다음을 얻는다.

    $$
    E[X] = \sum_{i=1}^{n} \frac{1}{n} = n \cdot \frac{1}{n} = 1
    $$

    이는 모든 $n \geq 1$ 에서 성립한다. $X_i$ 들이 독립일 필요는 없었다는 점에 주목하자. 기댓값의 선형성은 독립성을 요구하지 않는다. $\square$

---

**연습문제 6.**
그림의 왼쪽 칸(수렴 그래프)에서 모의실험 횟수가 적을 때는 출렁임이 크고 많을 때는 작아지는 까닭을 설명하여라. 이런 움직임의 바탕에 있는 수학적 원리가 무엇인지 밝히고, 출렁임의 크기가 시행 횟수 $N$ 에 따라 어떻게 줄어드는지 말하여라.

??? success "연습문제 6 풀이"
    바탕에 있는 원리는 **큰수의 법칙**이다. 누적 추정값 $\hat{p}_N = (N \text{ 번의 시행에서 나온 완전순열의 수}) / N$ 은 $p = e^{-1}$ 인 i.i.d. 베르누이$(p)$ 확률변수들의 표본평균이다.

    큰수의 강법칙에 따라 $N \to \infty$ 일 때 $\hat{p}_N \to p$ 가 거의 확실하게 성립한다.

    출렁임의 크기는 $\hat{p}_N$ 의 표준편차가 좌우한다.

    $$
    \text{SD}(\hat{p}_N) = \sqrt{\frac{p(1-p)}{N}} \propto \frac{1}{\sqrt{N}}
    $$

    $N$ 이 작으면 이 표준편차가 커서 그래프가 눈에 띄게 출렁인다. $N$ 이 커지면 표준편차가 $1/\sqrt{N}$ 처럼 줄어들어 곡선이 이론값 $e^{-1}$ 가까이에 자리를 잡는다. 예컨대 $N = 100$ 에서는 표준편차가 약 $0.048$ 이지만 $N = 50{,}000$ 에서는 약 $0.0022$ 로 떨어진다. 대략 22배가 줄어든 셈이며, 이는 $\sqrt{500}$ 이라는 비와 들어맞는다.
