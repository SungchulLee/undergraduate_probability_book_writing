# 확률질량함수 표집 모의실험

이 모의실험은 확률질량함수를 알고 있는 이산확률변수에서 무작위 표본을 뽑아,
경험적 상대도수를 이론적 확률과 견주어 본다. 또한 표본평균이 쌓여 가는 모습을
따라가며 그것이 참값인 기댓값 $E[X]$ 로 다가가는 것을 보여 준다.
큰수의 법칙이 실제로 작동하는 장면이다.

## 배경

가능한 값이 $\{x_1, x_2, \ldots, x_k\}$ 이고 확률질량함수가

$$
p_X(x_i) = P(X = x_i), \quad i = 1, 2, \ldots, k,
$$

인 이산확률변수 $X$ 가 주어졌다고 하자. 이 분포를 따르는 독립인 뽑기를 되풀이하면
$X$ 에서 **표집**할 수 있다. $n$ 번 뽑아 $X_1, X_2, \ldots, X_n$ 을 얻었을 때,
결과 $x_i$ 의 **경험적 확률**(상대도수)은 다음과 같다.

$$
\hat{p}_n(x_i) = \frac{1}{n} \sum_{j=1}^{n} \mathbf{1}(X_j = x_i).
$$

큰수의 법칙에 따라 $n \to \infty$ 일 때 확률 1로 $\hat{p}_n(x_i) \to p_X(x_i)$ 이다.
마찬가지로 **표본평균**

$$
\bar{X}_n = \frac{1}{n} \sum_{j=1}^{n} X_j
$$

은 **기댓값**

$$
E[X] = \sum_{i} x_i \, p_X(x_i).
$$

으로 거의 확실하게 수렴한다.

!!! info "표집이 왜 중요한가"
    현실에서는 확률질량함수를 모르는 경우가 많다. 표집을 하면 자료에서 확률과
    기댓값을 **추정**할 수 있다. 경험적 도수가 참된 확률질량함수와 어떻게 이어져
    있는지를 이해하는 것이 이산분포에 대한 통계적 추론의 출발점이다.

## 코드

```python
"""PMF Sampling: 이산확률변수에서 표본을 뽑아 그 확률질량함수와 견주어 본다."""
import numpy as np
import matplotlib.pyplot as plt


def main():
    # 이산확률변수 X를 정의한다
    outcomes = np.array([-3, -1, 1, 2, 5])
    pmf = np.array([0.10, 0.10, 0.10, 0.50, 0.20])

    # 표본을 생성한다
    n_samples = 10000
    samples = np.random.choice(outcomes, p=pmf, size=n_samples)

    # 경험적 도수를 계산한다
    empirical_probs = np.array([np.mean(samples == x) for x in outcomes])

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # 왼쪽 그림: 표본의 히스토그램과 이론적 확률질량함수
    width = 0.35
    axes[0].bar(outcomes - width / 2, empirical_probs, width,
                label="Empirical", color="steelblue", edgecolor="white")
    axes[0].bar(outcomes + width / 2, pmf, width,
                label="Theoretical PMF", color="coral", edgecolor="white")
    axes[0].set_xlabel("Outcome")
    axes[0].set_ylabel("Probability")
    axes[0].set_title(f"Empirical vs Theoretical PMF (n = {n_samples})")
    axes[0].set_xticks(outcomes)
    axes[0].legend()
    axes[0].grid(True, alpha=0.3, axis="y")

    # 오른쪽 그림: 경험적 평균이 E[X]로 수렴하는 모습
    expected_value = np.sum(outcomes * pmf)
    cumulative_means = np.cumsum(samples) / np.arange(1, n_samples + 1)
    axes[1].plot(cumulative_means, linewidth=0.8, color="steelblue",
                 label="Running sample mean")
    axes[1].axhline(expected_value, color="red", linestyle="--", linewidth=1.5,
                    label=f"E[X] = {expected_value:.2f}")
    axes[1].set_xlabel("Number of Samples")
    axes[1].set_ylabel("Sample Mean")
    axes[1].set_title("Convergence of Sample Mean to E[X]")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("pmf_sampling.png", dpi=150, bbox_inches="tight")
    plt.show()

    print(f"Theoretical E[X] = {expected_value:.4f}")
    print(f"Sample mean       = {np.mean(samples):.4f}")


if __name__ == "__main__":
    main()
```

## 실행 결과

이 스크립트를 돌리면 이론적 평균과 경험적 평균을 견주어 보여 준다.

```
Theoretical E[X] = 1.5000
Sample mean       = 1.4932
```

표본평균의 정확한 값은 실행할 때마다 달라진다. 실행할 때마다 새로운 무작위 표본을
뽑기 때문이다. $n = 10{,}000$ 개를 뽑으면 표본평균은 보통 참값에서
$\pm 0.05$ 안쪽에 들어온다.

이 스크립트는 두 칸짜리 그림도 그려 낸다.

- **왼쪽 그림(경험적 확률질량함수와 이론적 확률질량함수).** 다섯 가지 결과
  $\{-3, -1, 1, 2, 5\}$ 각각에 대해 경험적 상대도수(파랑)와 이론적 확률질량함수 값
  (산호색)을 나란히 세운 막대그래프이다. $n = 10{,}000$ 이면 두 막대가 거의
  구별되지 않는다.

- **오른쪽 그림(표본평균의 수렴).** 표본평균 $\bar{X}_n$ 을 $n$ 의 함수로 그린
  꺾은선이다. $n$ 이 작을 때는 크게 출렁이다가 차츰 $E[X] = 1.50$ 에 그은 수평
  점선 쪽으로 가라앉는다. 큰수의 법칙을 눈으로 곧바로 확인할 수 있다.

## 뜻풀이

이 모의실험은 확률론의 근본 결과 두 가지를 보여 준다.

1. **확률의 빈도주의적 해석.** 표본의 크기가 커지면 각 결과의 상대도수가 참된
   확률로 수렴한다. 왼쪽 그림은 $n = 10{,}000$ 일 때 모든 $i$ 에 대해
   $\hat{p}_n(x_i) \approx p_X(x_i)$ 임을 확인해 준다.

2. **큰수의 법칙.** 표본평균 $\bar{X}_n$ 은 모평균 $E[X]$ 로 수렴한다. 오른쪽
   그림이 이 수렴을 눈에 보이게 해 준다. 초반의 출렁임이 잦아들면서 쌓여 가는
   평균이 $1.50$ 언저리에서 안정된다.

!!! tip "표본 크기의 영향"
    `n_samples` 를 100, 1000, 100000으로 바꾸어 보아라. 표본이 적을수록 경험적
    막대가 이론적 확률질량함수에서 눈에 띄게 벗어나고, 쌓여 가는 평균의 곡선도
    더 심하게 출렁인다. 표본이 많아지면 둘이 더 바싹 맞아떨어진다. 이는
    **수렴의 속도**가 대체로 $1/\sqrt{n}$ 만큼임을 보여 준다.

이 분포의 기댓값은 곧바로 계산할 수 있다.

$$
E[X] = (-3)(0.10) + (-1)(0.10) + (1)(0.10) + (2)(0.50) + (5)(0.20) = 1.50
$$

분산은 다음과 같다.

$$
\operatorname{Var}(X) = E[X^2] - (E[X])^2
$$

여기서

$$
E[X^2] = (-3)^2(0.10) + (-1)^2(0.10) + (1)^2(0.10) + (2)^2(0.50) + (5)^2(0.20) = 8.10
$$

이므로 $\operatorname{Var}(X) = 8.10 - 1.50^2 = 5.85$ 이다. 따라서 표본평균의
표준편차는 $\sigma_{\bar{X}} = \sqrt{5.85 / 10000} \approx 0.024$ 이다. 표본평균이
늘 $1.50$ 에 가깝게 나오는 까닭이 여기에 있다.

## 연습문제

**연습문제 1.** 이산확률변수 $Y$ 가 $\{1, 2, 3, 4\}$ 의 값을 가지며 $k = 1, 2, 3, 4$ 에
대해 확률질량함수가 $P(Y = k) = k/10$ 이라 하자. $E[Y]$ 와
$\operatorname{Var}(Y)$ 를 구하여라.

??? success "연습문제 1 풀이"
    먼저 기댓값을 구한다.

    $$
    E[Y] = 1 \cdot \frac{1}{10} + 2 \cdot \frac{2}{10} + 3 \cdot \frac{3}{10} + 4 \cdot \frac{4}{10} = \frac{1 + 4 + 9 + 16}{10} = \frac{30}{10} = 3
    $$

    다음으로 $E[Y^2]$ 을 구한다.

    $$
    E[Y^2] = 1 \cdot \frac{1}{10} + 4 \cdot \frac{2}{10} + 9 \cdot \frac{3}{10} + 16 \cdot \frac{4}{10} = \frac{1 + 8 + 27 + 64}{10} = \frac{100}{10} = 10
    $$

    따라서 다음을 얻는다.

    $$
    \operatorname{Var}(Y) = E[Y^2] - (E[Y])^2 = 10 - 9 = 1
    $$

---

**연습문제 2.** 모의실험 코드를 고쳐 $n = 500$ 개의 표본을 쓰도록 하여라. 다섯 번
돌려 표본평균 다섯 개를 적어라. 그런 다음 $n = 50{,}000$ 으로 같은 일을 되풀이하여라.
두 경우에 표본평균이 흩어진 정도를 견주고, 표준오차 공식으로 그 차이를 설명하여라.

??? success "연습문제 2 풀이"
    스크립트에 나오는 분포에서 $\operatorname{Var}(X) = 5.85$ 이다. 표본평균의
    표준오차는 다음과 같다.

    $$
    \text{SE} = \frac{\sigma}{\sqrt{n}} = \frac{\sqrt{5.85}}{\sqrt{n}}
    $$

    $n = 500$ 이면 $\text{SE} = \sqrt{5.85/500} \approx 0.108$ 이므로, 다섯 개의
    표본평균은 대체로 $1.50$ 에서 $\pm 0.22$ 정도(표준오차의 약 두 배) 안에
    흩어진다.

    $n = 50{,}000$ 이면 $\text{SE} = \sqrt{5.85/50000} \approx 0.011$ 이므로,
    다섯 개의 표본평균이 $1.50$ 에서 $\pm 0.02$ 정도 안에 촘촘히 모인다.

    흩어진 정도가 $\sqrt{50000/500} = 10$ 배만큼 줄어드는데, 이는 표준오차가
    $1/\sqrt{n}$ 으로 줄어드는 것과 들어맞는다.

---

**연습문제 3.** $X$ 가 모의실험에 나온 확률질량함수를 따른다고 하자. 곧
$P(X = -3) = 0.10$, $P(X = -1) = 0.10$, $P(X = 1) = 0.10$,
$P(X = 2) = 0.50$, $P(X = 5) = 0.20$ 이다. $P(X > 0)$ 과
$P(|X| \leq 2)$ 를 구하여라.

??? success "연습문제 3 풀이"
    양수인 값은 $1, 2, 5$ 이다.

    $$
    P(X > 0) = P(X = 1) + P(X = 2) + P(X = 5) = 0.10 + 0.50 + 0.20 = 0.80
    $$

    $|X| \leq 2$ 를 만족하는 값은 $-1, 1, 2$ 이다.

    $$
    P(|X| \leq 2) = P(X = -1) + P(X = 1) + P(X = 2) = 0.10 + 0.10 + 0.50 = 0.70
    $$

---

**연습문제 4.** $X_1, X_2, \ldots, X_n$ 이 평균 $\mu$ 와 분산 $\sigma^2$ 이 유한한
분포에서 독립으로 뽑은 값이라면, $E[\bar{X}_n] = \mu$ 이고
$\operatorname{Var}(\bar{X}_n) = \sigma^2 / n$ 임을 증명하여라.

??? success "연습문제 4 풀이"
    기댓값의 선형성에 따라 다음을 얻는다.

    $$
    E[\bar{X}_n] = E\!\left[\frac{1}{n}\sum_{j=1}^{n} X_j\right] = \frac{1}{n}\sum_{j=1}^{n} E[X_j] = \frac{1}{n} \cdot n\mu = \mu
    $$

    분산의 경우, $X_j$ 들이 독립이므로 다음을 얻는다.

    $$
    \operatorname{Var}(\bar{X}_n) = \operatorname{Var}\!\left(\frac{1}{n}\sum_{j=1}^{n} X_j\right) = \frac{1}{n^2}\sum_{j=1}^{n} \operatorname{Var}(X_j) = \frac{1}{n^2} \cdot n\sigma^2 = \frac{\sigma^2}{n}
    $$

    이는 $\bar{X}_n$ 이 $\mu$ 의 **불편추정량**이고 그 분산이 $1/n$ 의 속도로
    줄어든다는 뜻이다. $\square$

---

**연습문제 5.** $\{0, 1, 2\}$ 의 값을 갖는 이산확률변수 $Z$ 의 확률질량함수를
모른다고 하자. $n = 1000$ 개의 표본을 뽑았더니 결과 $0$ 이 정확히 $320$ 번,
$1$ 이 정확히 $510$ 번, $2$ 가 정확히 $170$ 번 나왔다. 확률질량함수를 추정하고
$P(Z = 1)$ 에 대한 근사적인 95% 신뢰구간을 구하여라.

??? success "연습문제 5 풀이"
    경험적 확률질량함수는 다음과 같다.

    $$
    \hat{p}(0) = \frac{320}{1000} = 0.320, \quad \hat{p}(1) = \frac{510}{1000} = 0.510, \quad \hat{p}(2) = \frac{170}{1000} = 0.170
    $$

    $P(Z = 1)$ 의 점추정값은 $\hat{p} = 0.510$ 이다. 각 표본은 (결과가 1인가
    아닌가를 묻는) 베르누이 시행이고, 그 분산의 추정값은
    $\hat{p}(1 - \hat{p}) = 0.510 \times 0.490 = 0.2499$ 이다. 표준오차는
    다음과 같다.

    $$
    \text{SE} = \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}} = \sqrt{\frac{0.2499}{1000}} \approx 0.0158
    $$

    따라서 근사적인 95% 신뢰구간은 다음과 같다.

    $$
    \hat{p} \pm 1.96 \cdot \text{SE} = 0.510 \pm 0.031 = (0.479,\; 0.541)
    $$

---

**연습문제 6.** 이론적 확률이 무리수일 때, 표집으로 얻은 경험적 상대도수가
(우연이 아니고서는) 결코 이론적 확률질량함수와 정확히 같아질 수 없는 까닭을
설명하여라. 이것이 큰수의 법칙과 어긋나는가?

??? success "연습문제 6 풀이"
    $n$ 개의 표본을 뽑았을 때 어떤 결과의 경험적 상대도수는 $0 \leq k \leq n$ 인
    정수 $k$ 에 대해 $k/n$ 꼴의 유리수이다. 참된 확률 $p_X(x_i)$ 가 (이를테면
    $1/\sqrt{2}$ 처럼) 무리수라면, $n$ 이 무엇이든 어떤 비 $k/n$ 도 그것과 꼭
    같아질 수 없다.

    그러나 이것은 큰수의 법칙과 **어긋나지 않는다**. 큰수의 법칙은 $n \to \infty$
    일 때 $\hat{p}_n(x_i) \to p_X(x_i)$ 라고 말할 뿐이다. 곧 임의의
    $\varepsilon > 0$ 에 대해 언젠가부터
    $|\hat{p}_n(x_i) - p_X(x_i)| < \varepsilon$ 이 된다는 뜻이다. 수렴이란 얼마든지
    가까워진다는 것이지 정확히 같아진다는 것이 아니다. 유리수는 실수 안에서
    조밀하므로, 유리수 근사 $k/n$ 은 어떤 무리수에도 원하는 만큼 가까이 갈 수 있다.
