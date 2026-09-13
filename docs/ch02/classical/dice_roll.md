# 주사위 굴리기

이 모의실험은 공정한 주사위 $n$ 개의 눈의 합이 따르는 확률분포를 정확한 계산과 몬테카를로 추정 두 가지로 구하여 견주어 본다. 모든 결과가 같은 정도로 일어나는 고전적 확률이 모의실험과 어떻게 이어지는지를 보여 주고, 주사위 개수가 늘어남에 따라 표본공간이 얼마나 빠르게 커지는지를 드러낸다.

## 배경

공정한 정육면체 주사위 $n$ 개를 굴리면 표본공간에는 같은 정도로 일어나는 결과가 $|\Omega| = 6^n$ 개 있다. 합 $S = X_1 + X_2 + \cdots + X_n$ 은 $n$(모두 1)부터 $6n$(모두 6)까지의 값을 가진다. 고전적 확률모형에서 합이 특정한 값 $k$ 가 될 확률은 다음과 같다.

$$
P(S = k) = \frac{|\{(x_1, \ldots, x_n) \in \{1,\ldots,6\}^n : x_1 + \cdots + x_n = k\}|}{6^n}
$$

$n$ 이 작을 때는 $6^n$ 개의 결과를 모두 늘어놓아 정확한 확률을 구할 수 있다. $n$ 이 커지면 표본공간이 어마어마해지므로(예를 들어 $6^{10} \approx 6000$ 만), 몬테카를로 모의실험이 효율적인 대안이 된다.

!!! note "정확한 값과 모의실험 값"
    코드는 두 가지 방법을 나란히 쓴다.

    - **정확한 계산**: `itertools.product` 로 $6^n$ 개의 순서쌍을 모두 늘어놓고 목표 합이 되는 것을 센다.
    - **모의실험**: $N = 100{,}000$ 번 무작위로 굴려 상대도수로 확률을 어림한다.

    두 방법을 견주어 보면 큰수의 법칙이 눈에 들어온다. $N$ 이 커질수록 모의실험 확률은 정확한 값으로 다가간다.

## 코드

```python
"""주사위 눈의 합: 주사위 n개의 합에 대한 정확한 확률과 모의실험 확률을 구한다."""
import itertools
import numpy as np
import matplotlib.pyplot as plt


def exact_probability(n, k):
    """공정한 주사위 n개를 굴릴 때 P(합 = k)를 모두 늘어놓아 정확히 구한다."""
    total = 6 ** n
    count = sum(1 for combo in itertools.product(range(1, 7), repeat=n)
                if sum(combo) == k)
    return count / total


def simulated_probability(n, k, n_simulations=100000):
    """몬테카를로 모의실험으로 P(합 = k)를 어림한다."""
    rolls = np.random.randint(1, 7, size=(n_simulations, n))
    sums = rolls.sum(axis=1)
    return np.mean(sums == k)


def main():
    n_dice = 3  # 주사위의 개수
    possible_sums = np.arange(n_dice, 6 * n_dice + 1)

    exact_probs = [exact_probability(n_dice, k) for k in possible_sums]
    simulated_probs = [simulated_probability(n_dice, k) for k in possible_sums]

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # 왼쪽 그림: 정확한 확률과 모의실험 확률 견주기
    width = 0.35
    axes[0].bar(possible_sums - width / 2, exact_probs, width,
                label="Exact", color="steelblue", edgecolor="white")
    axes[0].bar(possible_sums + width / 2, simulated_probs, width,
                label="Simulated", color="coral", edgecolor="white", alpha=0.8)
    axes[0].set_xlabel("Sum")
    axes[0].set_ylabel("Probability")
    axes[0].set_title(f"P(Sum = k) for {n_dice} Dice")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3, axis="y")

    # 오른쪽 그림: 표본공간 크기의 증가
    dice_counts = np.arange(1, 7)
    space_sizes = [6 ** d for d in dice_counts]
    axes[1].bar(dice_counts, space_sizes, color="mediumpurple", edgecolor="white")
    axes[1].set_xlabel("Number of Dice")
    axes[1].set_ylabel("Sample Space Size")
    axes[1].set_title("Sample Space Growth ($6^n$)")
    axes[1].set_yscale("log")
    for i, s in enumerate(space_sizes):
        axes[1].text(dice_counts[i], s * 1.3, f"{s:,}", ha="center", fontsize=9)
    axes[1].grid(True, alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig("dice_roll_sum.png", dpi=150, bbox_inches="tight")
    plt.show()

    k_example = 10
    print(f"Example: P(sum={k_example} with {n_dice} dice)")
    print(f"  Exact:     {exact_probability(n_dice, k_example):.4f}")
    print(f"  Simulated: {simulated_probability(n_dice, k_example):.4f}")


if __name__ == "__main__":
    main()
```

## 실행 결과

이 스크립트를 돌리면 견주어 본 결과를 한 가지 찍어 준다.

```
Example: P(sum=10 with 3 dice)
  Exact:     0.1250
  Simulated: 0.1247
```

또한 두 칸짜리 그림을 그려 준다.

- **왼쪽 그림**: 주사위 3개를 굴릴 때 가능한 합 $k \in \{3, 4, \ldots, 18\}$ 마다 정확한 확률(파랑)과 모의실험 확률(산호색)을 나란히 놓은 막대그래프이다. 분포는 $k = 10.5$ 를 중심으로 대칭이고 종 모양이다. 모의실험 막대는 정확한 막대와 거의 겹친다.

- **오른쪽 그림**: 주사위가 $n = 1, 2, \ldots, 6$ 개일 때 표본공간의 크기 $6^n$ 을 로그 눈금 막대그래프로 보여 준다. 값은 6에서 46,656까지 커지며 막대마다 숫자가 붙어 있다. $n$ 이 클 때 모두 늘어놓는 방법이 왜 쓸모없어지는지를 잘 보여 준다.

## 뜻풀이

모의실험에서 눈여겨볼 것이 몇 가지 있다.

1. **정확한 확률과 모의실험 확률이 잘 맞는다.** 시행이 $N = 100{,}000$ 번이면 몬테카를로 어림값은 정확한 값과 소수점 아래 두 자리쯤까지 일치한다. 확률의 빈도주의적 해석, 곧 시행 횟수가 늘어남에 따라 상대도수가 참된 확률로 다가간다는 사실을 보여 준다.

2. **분포는 대칭이고 종 모양이다.** 주사위가 $n$ 개일 때 합의 분포는 평균 $\mu = 3.5n$ 을 중심으로 대칭이다. $n$ 이 커지면 중심극한정리에 따라 이 분포는 평균이 $3.5n$ 이고 분산이 $n \cdot 35/12$ 인 정규분포에 가까워진다.

3. **표본공간은 지수적으로 커진다.** 결과가 $6^n$ 개이므로 $n \leq 5$ 정도까지는 모두 늘어놓아 볼 만하지만 그 뒤로는 금세 계산이 버거워진다. 몬테카를로 모의실험은 훨씬 잘 견딘다. 드는 비용이 $|\Omega|$ 가 아니라 모의실험 횟수 $N$ 에만 달려 있기 때문이다.

!!! tip "언제 모의실험을 쓸 것인가"
    표본공간이 작고 정밀함이 중요할 때는 모두 늘어놓는 방법이 가장 좋다. $|\Omega|$ 가 클 때는 몬테카를로 모의실험이 현실적인 선택이며, 중심극한정리에 따라 정확도가 $O(1/\sqrt{N})$ 으로 좋아진다.

## 연습문제

**연습문제 1.** 모두 늘어놓는 방법으로 공정한 주사위 두 개를 굴릴 때의 $P(S = 7)$ 을 구하여라. 바라는 결과를 모두 적어 확인하여라.

??? success "연습문제 1 풀이"
    표본공간에는 결과가 $|\Omega| = 6^2 = 36$ 개 있다. $S = 7$ 이 되는 결과는 다음과 같다.

    $$
    \{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\}
    $$

    따라서 $|A| = 6$ 이고 다음을 얻는다.

    $$
    P(S = 7) = \frac{6}{36} = \frac{1}{6} \approx 0.1667
    $$

    `exact_probability(2, 7)` 을 돌려 보면 이 값이 확인된다.

**연습문제 2.** 주사위를 $n = 4$ 개 쓰도록 코드를 고쳐라. 가장 나올 법한 합은 무엇이고 그 정확한 확률은 얼마인가?

??? success "연습문제 2 풀이"
    `n_dice = 4` 로 바꾼다. 가능한 합은 4부터 24까지이다. 대칭성에 따라 분포는 $\mu = 4 \times 3.5 = 14$ 를 중심으로 대칭이므로 가장 나올 법한 합은 $k = 14$ 이다.

    `exact_probability(4, 14)` 를 구하면 다음과 같다.

    $$
    P(S = 14) = \frac{146}{6^4} = \frac{146}{1296} \approx 0.1127
    $$

    14를 $\{1, \ldots, 6\}$ 의 값 네 개의 순서 있는 합으로 적는 방법은 146가지이다.

**연습문제 3.** `exact_probability` 함수는 모든 결과를 늘어놓기 때문에 시간복잡도가 $O(6^n)$ 이다. 동적계획법을 써서 $O(n \cdot k)$ 시간에 도는 더 효율적인 알고리즘을 제안하여라.

??? success "연습문제 3 풀이"
    지금까지 굴린 주사위로 합이 $j$ 가 되는 방법의 수를 `dp[j]` 에 담는 DP 표를 쓴다.

    ```python
    def exact_probability_dp(n, k):
        dp = [0] * (6 * n + 1)
        dp[0] = 1
        for die in range(n):
            new_dp = [0] * (6 * n + 1)
            for j in range(len(dp)):
                if dp[j] > 0:
                    for face in range(1, 7):
                        if j + face <= 6 * n:
                            new_dp[j + face] += dp[j]
            dp = new_dp
        return dp[k] / (6 ** n)
    ```

    이 방법은 $O(6nk)$ 시간과 $O(k)$ 공간이면 되므로, $n$ 이 클 때 $O(6^n)$ 보다 엄청나게 빠르다.

**연습문제 4.** 공정한 주사위 $n$ 개의 합의 분포가 $3.5n$ 을 중심으로 대칭임을 증명하여라. 곧 모든 가능한 $k$ 에 대해 $P(S = k) = P(S = 7n - k)$ 임을 보여라.

??? success "연습문제 4 풀이"
    사상 $\varphi: (x_1, \ldots, x_n) \mapsto (7 - x_1, \ldots, 7 - x_n)$ 을 생각하자. 각 $x_i \in \{1, \ldots, 6\}$ 이므로 $7 - x_i \in \{1, \ldots, 6\}$ 이기도 하다. 따라서 $\varphi$ 는 $\{1,\ldots,6\}^n$ 위의 전단사이다. 게다가 다음이 성립한다.

    $$
    \sum_{i=1}^n (7 - x_i) = 7n - \sum_{i=1}^n x_i
    $$

    그러므로 $\varphi$ 는 합이 $k$ 인 결과를 합이 $7n - k$ 인 결과로 옮기고 그 반대도 마찬가지이다. $\varphi$ 가 전단사이므로 합이 $k$ 인 결과의 수와 합이 $7n - k$ 인 결과의 수가 같고, 따라서 $P(S = k) = P(S = 7n - k)$ 이다. $\square$

**연습문제 5.** 모의실험 횟수를 $N = 1{,}000{,}000$ 으로 늘린 뒤 최대 절대오차 $\max_k |P_{\text{exact}}(k) - P_{\text{sim}}(k)|$ 를 $N = 100{,}000$ 인 경우와 견주어 보아라. 오차가 몇 배쯤 줄어들 것으로 기대하며, 그 까닭은 무엇인가?

??? success "연습문제 5 풀이"
    중심극한정리에 따라 $N$ 번의 시행에 바탕을 둔 표본비율의 표준오차는 $\sqrt{p(1-p)/N}$ 이다. $N$ 을 10배로 늘리면 표준오차는 $\sqrt{10} \approx 3.16$ 배만큼 줄어든다.

    $N = 1{,}000{,}000$ 으로 돌리면 최대 절대오차는 보통 0.001 안팎이고, $N = 100{,}000$ 일 때는 0.003 안팎이다. 그 비가 대략 3이므로 $1/\sqrt{N}$ 수렴 속도와 잘 맞는다.

    이것이 몬테카를로 방법의 근본 성질이다. 정확도를 소수점 아래로 한 자리 더 얻으려면 표본이 대략 100배 더 있어야 한다.

**연습문제 6.** 포함배제 공식을 써서, 양의 정수 $k$ 를 $\{1, \ldots, 6\}$ 의 정수 $n$ 개의 순서 있는 합으로 적는 방법의 수를 정확히 구하여라.

??? success "연습문제 6 풀이"
    $y_i = x_i - 1$ 로 두면 $y_i \in \{0, 1, \ldots, 5\}$ 이고 $y_1 + \cdots + y_n = k - n$ 이다. $m = k - n$ 이라 하자. 구할 것은 $0 \leq y_i \leq 5$ 아래에서 $y_1 + \cdots + y_n = m$ 의 해의 개수이다.

    조건 $y_i \leq 5$ 에 포함배제를 쓰자. $A_i = \{y_i \geq 6\}$ 이라 두자. 제한이 없을 때의 개수는 막대와 별에 따라 $\binom{m + n - 1}{n - 1}$ 이다. 그러면 다음이 성립한다.

    $$
    |A_{i_1} \cap \cdots \cap A_{i_j}| = \binom{m - 6j + n - 1}{n - 1}
    $$

    ($z_{i_\ell} = y_{i_\ell} - 6$ 으로 바꾸어 놓으면 된다.) 포함배제에 따라 다음을 얻는다.

    $$
    \text{개수} = \sum_{j=0}^{\lfloor m/6 \rfloor} (-1)^j \binom{n}{j} \binom{m - 6j + n - 1}{n - 1}
    $$

    여기서 $m = k - n$ 이고 위 인수가 음수인 항은 0이다. 이것을 $6^n$ 으로 나누면 $P(S = k)$ 를 얻는다.

**연습문제 7.** 공정한 주사위를 되풀이해 굴리며 눈의 합을 계속 더해 나간다. 합이 1000 이상이 되는 순간 멈춘다. 마지막 굴림에서 가장 나올 법한 눈은 무엇인가?

??? success "연습문제 7 풀이"
    마지막 굴림 바로 앞의 상황을 생각해 보자.

    합이 999라면 어떤 눈(1~6)이 나와도 거기서 끝나므로 모든 눈이 마지막 굴림이 될 가능성이 똑같다.
    합이 998이라면 1이 나오면 합이 999가 되어 한 번 더 굴려야 한다. 반면 2, 3, 4, 5, 6 가운데 무엇이 나오든 거기서 곧바로 끝난다. 따라서 이 값들이 1보다 마지막 굴림이 될 가능성이 크다.
    합이 997이라면 3, 4, 5, 6만이 곧바로 끝내고 1이나 2는 한 번 더 굴려야 한다. 여기서도 큰 눈이 마지막 굴림이 될 가능성이 크다.
    이렇게 따져 나가면, 큰 눈일수록 1000까지 "남은 거리"가 더 여러 가지일 때 과정을 끝낼 수 있음을 알 수 있다. 그러므로 큰 수일수록 마지막 굴림이 될 가능성이 크다. 특히 6이 가장 나올 법하고 1이 가장 덜 나올 법하다.

    실제로 1000처럼 목표가 클 때 마지막 굴림이 $k$ 일 확률은 대략 $k$ 에 비례한다.

    $$
    \mathbb{P}(\text{마지막 굴림}=k)\approx\frac{k}{1+2+3+4+5+6}=\frac{k}{21}.
    $$

