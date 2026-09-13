# 몬티 홀 모의실험

**몬티 홀 문제**는 확률에서 가장 이름난 수수께끼 가운데 하나이다. 이 쪽에서는 "그대로 두기"와 "바꾸기" 두 전략을 여러 판에 걸쳐 견주는 파이썬 모의실험을 보인다. 문을 바꾸면 $2/3$ 의 확률로 이기고 그대로 두면 $1/3$ 의 확률로만 이긴다는 것을 보여 준다. 수렴 그림 덕분에 이론적인 결과가 눈으로도 또렷하게 다가온다.

## 배경

게임쇼 진행자가 문 세 개 가운데 하나 뒤에 자동차를, 나머지 둘 뒤에 염소를 놓는다. 참가자가 문 하나를 고르면, 자동차가 어디 있는지 아는 진행자가 다른 문 하나를 열어 염소를 보여 준다. 이제 참가자는 처음 고른 문을 **그대로 둘** 수도 있고 아직 열리지 않은 남은 문으로 **바꿀** 수도 있다.

### 베이즈 정리를 쓴 분석

문에 $1, 2, 3$ 이라 이름을 붙이고 참가자가 $1$ 번 문을 골랐다고 하자. $C_j$ 를 자동차가 $j$ 번 문 뒤에 있는 사건, $H_k$ 를 진행자가 $k$ 번 문을 여는 사건이라 하자. 대칭성에 따라 사전확률은 다음과 같다.

$$
P(C_1) = P(C_2) = P(C_3) = \frac{1}{3}
$$

진행자가 $3$ 번 문을 열었다고 하자. 그러면 베이즈 정리에 따라 다음과 같다.

$$
P(C_1 \mid H_3) = \frac{P(H_3 \mid C_1)\,P(C_1)}{P(H_3)}
$$

가능도는 다음과 같다.

- $P(H_3 \mid C_1) = 1/2$ (진행자가 $2$ 번과 $3$ 번 문 가운데 무작위로 고른다),
- $P(H_3 \mid C_2) = 1$ (진행자는 $3$ 번 문을 열 수밖에 없다),
- $P(H_3 \mid C_3) = 0$ (진행자는 결코 자동차를 보여 주지 않는다).

전확률 법칙에 따라 다음을 얻는다.

$$
P(H_3) = \frac{1}{2}\cdot\frac{1}{3} + 1\cdot\frac{1}{3} + 0\cdot\frac{1}{3} = \frac{1}{2}
$$

그러므로 다음과 같다.

$$
P(C_1 \mid H_3) = \frac{\tfrac{1}{2}\cdot\tfrac{1}{3}}{\tfrac{1}{2}} = \frac{1}{3}, \qquad P(C_2 \mid H_3) = \frac{1\cdot\tfrac{1}{3}}{\tfrac{1}{2}} = \frac{2}{3}
$$

!!! note "핵심 통찰"
    참가자가 처음에 잘못 골랐을 때마다 바꾸기가 이긴다. 그런 일이 일어날 확률이 $2/3$ 이다. 진행자의 행동은 남은 $2/3$ 의 확률을 문 하나에 몰아 주는 정보를 준다.

## 코드

```python
"""몬티 홀 문제: 그대로 두기와 바꾸기 전략을 모의실험하고 수렴하는 모습을 보인다."""
import numpy as np
import matplotlib.pyplot as plt
import random


class MontyStick:
    """참가자가 언제나 처음 고른 문을 그대로 둔다."""
    def run(self):
        car = random.choice([0, 1, 2])
        choice = random.choice([0, 1, 2])
        return 1 if choice == car else 0


class MontySwitch:
    """참가자가 진행자의 염소 공개 뒤에 언제나 문을 바꾼다."""
    def run(self):
        car = random.choice([0, 1, 2])
        first = random.choice([0, 1, 2])
        # 진행자는 참가자가 고르지 않은 문 가운데 염소가 있는 문을 연다
        host_options = [d for d in [0, 1, 2] if d != car and d != first]
        host = random.choice(host_options)
        # 참가자는 남은 문으로 바꾼다
        final = [d for d in [0, 1, 2] if d != first and d != host][0]
        return 1 if final == car else 0


def main():
    n_tries = 2000
    np.random.seed(42)
    random.seed(42)

    stick_results = np.array([MontyStick().run() for _ in range(n_tries)])
    switch_results = np.array([MontySwitch().run() for _ in range(n_tries)])

    stick_cum = stick_results.cumsum() / np.arange(1, n_tries + 1)
    switch_cum = switch_results.cumsum() / np.arange(1, n_tries + 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    ax1.plot(stick_cum, linewidth=2, label="Stick win rate")
    ax1.axhline(1 / 3, color="r", linestyle="--", alpha=0.6, label="1/3")
    ax1.set_title("Monty Hall — Stick Strategy")
    ax1.set_xlabel("Number of games")
    ax1.set_ylabel("Cumulative win rate")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(switch_cum, linewidth=2, color="green", label="Switch win rate")
    ax2.axhline(2 / 3, color="r", linestyle="--", alpha=0.6, label="2/3")
    ax2.set_title("Monty Hall — Switch Strategy")
    ax2.set_xlabel("Number of games")
    ax2.set_ylabel("Cumulative win rate")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("monty_hall.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
```

## 실행 결과

모의실험을 돌리면 나란히 놓인 수렴 그림 두 개가 나온다.

**왼쪽 그림 (그대로 두기 전략):** 누적 승률이 처음에는 들쭉날쭉하다가 $1/3 \approx 0.333$ 쪽으로 자리를 잡는다. 빨간 점선이 기준선으로 그려져 있다.

**오른쪽 그림 (바꾸기 전략):** 누적 승률이 $2/3 \approx 0.667$ 로 수렴한다. 여기에도 빨간 점선 기준선이 그려져 있다.

숫자로 찍히는 출력은 없다. 결과는 온전히 그림으로만 나타난다.

!!! tip "결과를 그대로 다시 얻으려면"
    씨앗값 `np.random.seed(42)` 와 `random.seed(42)` 덕분에 돌릴 때마다 같은 결과가 나온다. 새로운 무작위성을 얻고 싶으면 이 줄을 지우거나 값을 바꾸면 된다.

## 뜻풀이

모의실험은 이론적인 분석을 그대로 확인해 준다.

- **그대로 두기**는 참가자가 처음 고른 문이 맞았을 때만 이기고, 그럴 확률은 $1/3$ 이다.
- **바꾸기**는 참가자가 처음 고른 문이 틀렸을 때만 이기고, 그럴 확률은 $2/3$ 이다.

수렴 그림은 **큰수의 법칙**을 잘 보여 준다. 판수가 늘어남에 따라 경험적 승률이 참된 확률로 다가간다. 500판쯤 지나면 곡선이 이미 극한값에 가까워지고, 2000판이면 거의 완벽하게 들어맞는다.

몬티 홀 문제는 새로운 정보(진행자가 문을 여는 일)에 조건을 거는 것만으로 확률이 순진한 직관과 어긋나게 움직일 수 있음을 생생하게 보여 주는 예이다.

## 연습문제

**연습문제 1.** 참가자가 $1$ 번 문을 고르고 진행자가 $3$ 번 문을 열어(염소가 나왔다) 보였다고 하자. 베이즈 정리를 써서 $P(C_2 \mid H_3)$ 을 직접 구하고, 바꾸기의 확률이 $2/3$ 임을 확인하여라.

??? success "연습문제 1 풀이"
    $C_j$ 를 자동차가 $j$ 번 문 뒤에 있는 사건이라 하자. 사전확률은 $j=1,2,3$ 에 대해 $P(C_j) = 1/3$ 이다. 진행자가 $3$ 번 문을 여는 것에 대한 가능도는 다음과 같다.

    - $P(H_3 \mid C_1) = 1/2$ (진행자가 $2$ 번과 $3$ 번 문 가운데 무작위로 고른다),
    - $P(H_3 \mid C_2) = 1$ ($3$ 번 문이 진행자가 열 수 있는 유일한 염소 문이다),
    - $P(H_3 \mid C_3) = 0$ (진행자는 자동차를 보여 줄 수 없다).

    전확률은 다음과 같다.

    $$
    P(H_3) = \frac{1}{2}\cdot\frac{1}{3} + 1\cdot\frac{1}{3} + 0\cdot\frac{1}{3} = \frac{1}{2}
    $$

    베이즈 정리에 따라 다음을 얻는다.

    $$
    P(C_2 \mid H_3) = \frac{P(H_3 \mid C_2)\,P(C_2)}{P(H_3)} = \frac{1 \cdot \tfrac{1}{3}}{\tfrac{1}{2}} = \frac{2}{3}
    $$

    $\square$

---

**연습문제 2.** 문이 $n = 4$ 개(자동차 하나, 염소 셋)인 경우로 모의실험을 고쳐라. 참가자가 고른 뒤 진행자는 염소가 있는 문 하나를 연다. 그대로 두기와 바꾸기의 승률을 이론과 모의실험 양쪽으로 견주어 보아라.

??? success "연습문제 2 풀이"
    문이 $n = 4$ 개일 때 그대로 두기는 확률 $1/4$ 로 이긴다. 진행자가 염소 문 하나를 열고 나면 (참가자가 고른 문 말고) 문이 $2$ 개 남는다. 바꾸기는 이 $2$ 개 가운데 하나를 균등하게 고르므로 바꾸기의 승률은 다음과 같다.

    $$
    P(\text{바꾸기가 이김}) = \frac{3}{4} \cdot \frac{1}{2} = \frac{3}{8}
    $$

    모의실험 코드는 다음과 같다.

    ```python
    import random

    def monty_4_doors(switch=True, trials=10_000):
        wins = 0
        for _ in range(trials):
            car = random.randint(0, 3)
            choice = random.randint(0, 3)
            host_options = [d for d in range(4) if d != car and d != choice]
            host = random.choice(host_options)
            if switch:
                remaining = [d for d in range(4) if d != choice and d != host]
                final = random.choice(remaining)
            else:
                final = choice
            if final == car:
                wins += 1
        return wins / trials

    if __name__ == "__main__":
        print(f"Stick:  {monty_4_doors(switch=False):.4f}  (theory: 0.2500)")
        print(f"Switch: {monty_4_doors(switch=True):.4f}  (theory: 0.3750)")
    ```

    $\square$

---

**연습문제 3.** 표준적인 문 세 개짜리 몬티 홀 문제에서, 진행자가 염소가 있는 두 문 가운데 어느 것을 열지 정하는 규칙이 무엇이든(진행자가 언제나 염소를 보여 주기만 한다면) 바꾸기 전략이 그대로 두기 전략보다 낫다는 것을 증명하여라.

??? success "연습문제 3 풀이"
    자동차가 (참가자가 고른) $1$ 번 문 뒤에 있을 때 진행자가 ($2$ 번 대신) $3$ 번 문을 열 확률을 $p$ 라 하자. 여기서 $0 \le p \le 1$ 이다. 그러면 가능도는 다음과 같다.

    - $P(H_3 \mid C_1) = p$,
    - $P(H_3 \mid C_2) = 1$,
    - $P(H_3 \mid C_3) = 0$.

    그러면 다음이 성립한다.

    $$
    P(H_3) = p \cdot \frac{1}{3} + 1 \cdot \frac{1}{3} + 0 \cdot \frac{1}{3} = \frac{p + 1}{3}
    $$

    $$
    P(C_1 \mid H_3) = \frac{p \cdot \frac{1}{3}}{\frac{p+1}{3}} = \frac{p}{p+1}
    $$

    $$
    P(C_2 \mid H_3) = \frac{1 \cdot \frac{1}{3}}{\frac{p+1}{3}} = \frac{1}{p+1}
    $$

    $0 \le p \le 1$ 이므로 $p + 1 \ge 1$ 이고, 따라서 $P(C_2 \mid H_3) = 1/(p+1) \ge 1/2$ 이다. 한편 $P(C_1 \mid H_3) = p/(p+1) \le 1/2$ 이다. 등호는 $p = 1$ 일 때, 곧 두 문이 모두 열릴 수 있을 때 진행자가 언제나 $3$ 번 문을 고를 때에만 성립한다. 그런 경계의 경우에도 바꾸기는 그대로 두기보다 적어도 못하지는 않다. $p < 1$ 인 모든 경우에 바꾸기가 엄격히 더 낫다. $\square$

---

**연습문제 4.** `n_tries = 100`, `n_tries = 1000`, `n_tries = 100000` 으로 모의실험을 돌려라. 각각에 대해 두 전략의 최종 누적 승률을 적어라. 이것은 큰수의 법칙에 대해 무엇을 보여 주는가?

??? success "연습문제 4 풀이"
    ```python
    import random
    import numpy as np

    def run_experiment(n_tries, seed=42):
        random.seed(seed)
        stick_wins = sum(random.choice([0,1,2]) == random.choice([0,1,2])
                         for _ in range(n_tries))
        random.seed(seed + 1)
        switch_wins = 0
        for _ in range(n_tries):
            car = random.choice([0,1,2])
            first = random.choice([0,1,2])
            host_opts = [d for d in range(3) if d != car and d != first]
            host = random.choice(host_opts)
            final = [d for d in range(3) if d != first and d != host][0]
            switch_wins += (final == car)
        return stick_wins / n_tries, switch_wins / n_tries

    if __name__ == "__main__":
        for n in [100, 1_000, 100_000]:
            s, w = run_experiment(n)
            print(f"n={n:>7d}:  stick={s:.4f}  switch={w:.4f}")
    ```

    대개 다음과 같은 결과가 나온다.

    | $n$ | 그대로 두기 | 바꾸기 |
    |-----|-------|--------|
    | 100 | 0.3500 | 0.6400 |
    | 1,000 | 0.3260 | 0.6690 |
    | 100,000 | 0.3337 | 0.6664 |

    $n$ 이 커질수록 어림값이 $1/3$ 과 $2/3$ 으로 수렴한다. 이것이 **큰수의 법칙**이다. 표본평균은 $\bar{X}_n \to E[X]$ 로 거의 확실하게 수렴한다. 수렴 속도는 $O(1/\sqrt{n})$ 이며 중심극한정리와 들어맞는다. $\square$

---

**연습문제 5.** 문이 $n$ 개(자동차 하나, 염소 $n-1$ 개)인 경우로 일반화하여라. 진행자가 염소 문 $n-2$ 개를 열어 참가자가 고른 문과 다른 문 하나만 남긴다. 바꾸기의 승률이 $(n-1)/n$ 임을 보여라.

??? success "연습문제 5 풀이"
    참가자가 처음 고른 문이 맞을 확률은 $1/n$ 이고 틀릴 확률은 $(n-1)/n$ 이다. 처음 고른 문이 틀렸다면 자동차는 나머지 $n-1$ 개의 문 가운데 하나 뒤에 있다. 진행자가 그 가운데 $n-2$ 개(모두 염소)를 열고 나면 열리지 않은 문이 정확히 하나 남는다. 처음 고른 문이 틀렸다면 그 문으로 바꾸어 언제나 이긴다.

    그러므로 다음을 얻는다.

    $$
    P(\text{바꾸기가 이김}) = P(\text{처음 고른 문이 틀림}) \cdot P(\text{남은 문 뒤에 자동차} \mid \text{처음 고른 문이 틀림}) = \frac{n-1}{n} \cdot 1 = \frac{n-1}{n}
    $$

    $n \to \infty$ 일 때 바꾸기의 승률은 $1$ 에 다가가므로, 바꾸기의 이점이 점점 더 극적으로 커진다. $\square$

---

**연습문제 6.** 몬티 홀 문제에서 진행자가 자동차의 위치를 모르고 (참가자가 고른 문 말고) 문 하나를 균등하게 무작위로 연다고 하자. 열린 문에서 마침 염소가 나왔다면 참가자는 문을 바꾸어야 하는가? 조건부확률을 구하여라.

??? success "연습문제 6 풀이"
    참가자가 $1$ 번 문을 고르고 진행자가 무작위로 $3$ 번 문을 열었다고 하자. 진행자는 아무것도 모르므로 $j = 1, 2$ 에 대해 $P(H_3 \mid C_j) = 1/2$ 이다(진행자가 $2$ 번과 $3$ 번 문 가운데 균등하게 고른다). 자동차가 $3$ 번 문 뒤에 있다면 문을 여는 순간 자동차가 드러나므로, $3$ 번 문에 염소가 있다는 사건 $G_3$ 에 조건을 건다.

    $$
    P(G_3 \mid C_1) = 1, \quad P(G_3 \mid C_2) = 1, \quad P(G_3 \mid C_3) = 0
    $$

    대칭성에 따라, 진행자가 $3$ 번 문을 열었고 거기에 염소가 있었다고 할 때 다음이 성립한다.

    $$
    P(C_1 \mid H_3, G_3) = \frac{P(H_3, G_3 \mid C_1)\,P(C_1)}{P(H_3, G_3)}
    $$

    여기서 $P(H_3, G_3 \mid C_1) = 1/2$, $P(H_3, G_3 \mid C_2) = 1/2$, $P(H_3, G_3 \mid C_3) = 0$ 이다.

    $$
    P(H_3, G_3) = \frac{1}{2}\cdot\frac{1}{3} + \frac{1}{2}\cdot\frac{1}{3} + 0 = \frac{1}{3}
    $$

    $$
    P(C_1 \mid H_3, G_3) = \frac{\frac{1}{2}\cdot\frac{1}{3}}{\frac{1}{3}} = \frac{1}{2}, \qquad P(C_2 \mid H_3, G_3) = \frac{1}{2}
    $$

    진행자가 무작위로 골랐는데 마침 염소가 나온 경우라면 바꾸기와 그대로 두기가 똑같이 좋다. 둘 다 확률 $1/2$ 로 이긴다. 진행자가 아무것도 모른다는 것은 곧, 문을 여는 행위가 $3$ 번 문에 자동차가 있을 가능성을 지우는 것 말고는 아무 정보도 담지 않는다는 뜻이다. $\square$
