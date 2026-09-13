# 도박꾼의 파산 모의실험 코드

이 쪽에서는 도박꾼의 파산 문제를 객체지향 방식으로 몬테카를로 모의실험한다. `GamblerRuin` 클래스가 확률보행 경로를 만들고 그 결과를 파산·성공·미결로 갈라 준다. 경로 하나를 그려 확률보행의 움직임을 보이고, 큰 규모의 모의실험으로 파산 확률을 어림한다.

## 배경

도박꾼이 처음 밑천 $i$ 로 시작해 단위 금액을 되풀이해서 건다. 판마다 확률 $p$ 로 이기고 확률 $q = 1 - p$ 로 진다. 도박꾼의 밑천은 다음과 같은 확률보행을 따른다.

$$
S_n = i + X_1 + X_2 + \cdots + X_n
$$

여기서 각 $X_k$ 는 독립이고 확률 $p$ 로 $+1$, 확률 $q$ 로 $-1$ 이다. 이 보행은 $0$ (파산)이나 $N$ (목표)에 처음 닿는 순간 **흡수된다**.

### 도달시각

**도달시각**을 $T = \min\{n \ge 0 : S_n = 0 \text{ 또는 } S_n = N\}$ 으로 정의하자. $p \ne 1/2$ 일 때 도달시각의 기댓값은 다음과 같다.

$$
E[T \mid S_0 = i] = \frac{1}{q - p}\left(i - N\,\frac{1 - (q/p)^i}{1 - (q/p)^N}\right)
$$

$p = 1/2$ 일 때 도달시각의 기댓값은 $E[T] = i(N - i)$ 이다.

!!! warning "모의실험 길이가 유한하다는 점"
    이 모의실험은 걸음 수를 정해 놓고 쓴다(`num_steps`). 그 안에 어느 벽에도 닿지 못하면 그 경로는 "미결"로 분류한다. 파산 확률을 정확히 어림하려면 미결 경로의 비율이 무시할 만큼 작아지도록 `num_steps` 가 충분히 커야 한다.

### 벡터화한 모의실험

코드는 `np.random.binomial` 로 무작위 걸음을 한꺼번에 만든 뒤, $B \sim \text{Bernoulli}(p)$ 에 대해 $2B - 1$ 변환으로 베르누이 결과를 $\pm 1$ 로 바꾼다. 그런 다음 누적합으로 경로 행렬 전체를 효율적으로 얻는다.

## 코드

```python
"""도박꾼의 파산: 치우친 확률보행을 몬테카를로로 모의실험한다."""
import numpy as np
import matplotlib.pyplot as plt


class GamblerRuin:
    def __init__(self, p=0.49, initial=10, goal=20):
        self.p = p
        self.q = 1 - p
        self.initial = initial
        self.goal = goal

    def simulate(self, num_paths=1, num_steps=200, seed=None):
        if seed is not None:
            np.random.seed(seed)
        steps = 2 * np.random.binomial(1, self.p, (num_paths, num_steps)) - 1
        path = self.initial + np.concatenate(
            [np.zeros((num_paths, 1)), steps.cumsum(axis=1)], axis=1
        )
        results = np.zeros(num_paths)
        for i in range(num_paths):
            for pos in path[i]:
                if pos >= self.goal:
                    results[i] = 1
                    break
                if pos <= 0:
                    results[i] = -1
                    break
        return path, results


def main():
    p = 0.49
    gambler = GamblerRuin(p=p, initial=10, goal=20)

    # --- 경로 하나 그려 보기 ---
    path, result = gambler.simulate(num_paths=1, num_steps=400, seed=0)
    fig, ax = plt.subplots(figsize=(12, 3))
    ax.plot(path[0], "-b")
    ax.axhline(0, color="r", linestyle="--", alpha=0.5)
    ax.axhline(20, color="r", linestyle="--", alpha=0.5)
    ax.set_title(f"Gambler's Ruin (p={p})")
    ax.set_xlabel("Step")
    ax.set_ylabel("Capital")
    plt.tight_layout()
    plt.savefig("gamblers_ruin_simulation.png", dpi=150, bbox_inches="tight")
    plt.show()

    # --- 경로 여럿: 파산 확률 어림하기 ---
    _, results = gambler.simulate(num_paths=10_000, num_steps=2000, seed=42)
    num_ruin = np.sum(results == -1)
    num_win = np.sum(results == 1)
    print(f"Ruin probability (simulation): {num_ruin / (num_ruin + num_win):.4f}")


if __name__ == "__main__":
    main()
```

## 실행 결과

이 코드는 그림 하나와 한 줄짜리 글자 출력을 내놓는다.

**경로 하나 그림:** $i = 10$ 에서 출발해 $0$ 과 $N = 20$ 에 벽(빨간 점선)이 있는 도박꾼의 밑천을 시간에 따라 그린 것이다. 경로는 오르내리면서도 아래쪽으로 조금씩 흘러가고($p = 0.49 < 0.5$ 이기 때문이다) 결국 두 벽 가운데 하나에 닿는다.

**몬테카를로 어림값(경로 10,000개):**

```
Ruin probability (simulation): 0.6726
```

!!! tip "이론값과 견주어 보기"
    $p = 0.49$, $i = 10$, $N = 20$ 일 때의 이론적인 파산 확률은 다음과 같다.

    $$
    Q(10) = \frac{(q/p)^{20} - (q/p)^{10}}{(q/p)^{20} - 1} = \frac{(51/49)^{20} - (51/49)^{10}}{(51/49)^{20} - 1} \approx 0.6700
    $$

    모의실험 어림값이 이 값과 잘 들어맞는다.

## 뜻풀이

모의실험 결과에서 눈여겨볼 것이 몇 가지 있다.

1. **아래쪽으로 흐른다.** $p = 0.49$ 이면 한 걸음의 기댓값이 $E[X_k] = 2p - 1 = -0.02$ 이므로 보행은 한 걸음마다 $0.02$ 씩 아래로 흘러간다. 여러 걸음에 걸쳐 이 흐름이 쌓이면서 도박꾼을 파산 쪽으로 밀어붙인다.

2. **경로마다 들쭉날쭉하다.** 아래로 흐르는데도 개별 경로는 크게 오르내릴 수 있다. 경로 하나 그림을 보면 목표에 거의 다가갔다가 결국 파산 쪽으로 끌려가는 모습이 나타난다. 도박꾼이 흔히 "다 이긴 것 같다"고 느끼는 까닭이 여기에 있다.

3. **결과의 분류.** 코드는 결과를 세 갈래로 나눈다.
    - `results[i] = -1`: 파산(밑천이 $0$ 에 닿음),
    - `results[i] = 1`: 성공(밑천이 $N$ 에 닿음),
    - `results[i] = 0`: 미결(`num_steps` 안에 어느 벽에도 닿지 못함).

    `num_steps = 2000` 이고 $N = 20$ 이면 거의 모든 경로가 결판난다. $N$ 이 더 크면 걸음 수를 더 늘려야 할 수도 있다.

4. **규모를 키우기 좋다.** 벡터화한 방식은 모든 걸음을 행렬 연산 한 번으로 만들어 내므로 `num_paths` 가 커도 효율적이다. 경로 안의 위치를 하나씩 훑는 안쪽 반복문이 병목이다. 실제로 쓸 때는 도달시각을 찾는 부분도 벡터화할 수 있다.

## 연습문제

**연습문제 1.** $p = 0.50$, $i = 10$, $N = 20$ 으로 모의실험을 돌려라. 이론적으로 기대되는 파산 확률은 얼마인가? 경로 10,000개로 확인하여라.

??? success "연습문제 1 풀이"
    $p = 1/2$ 일 때 이론적인 파산 확률은 다음과 같다.

    $$
    Q(i) = 1 - \frac{i}{N} = 1 - \frac{10}{20} = 0.50
    $$

    ```python
    import numpy as np

    gambler = GamblerRuin(p=0.50, initial=10, goal=20)
    _, results = gambler.simulate(num_paths=10_000, num_steps=5000, seed=42)
    num_ruin = np.sum(results == -1)
    num_win = np.sum(results == 1)
    print(f"Ruin probability: {num_ruin / (num_ruin + num_win):.4f}")
    ```

    대개 $0.50$ 언저리가 나와 이론과 들어맞는다. 공정한 게임에서는 `num_steps` 를 더 늘려야 할 수도 있다. 흡수시각의 기댓값 $E[T] = i(N-i) = 100$ 은 유한하지만 분산이 크기 때문이다. $\square$

---

**연습문제 2.** `simulate` 메서드를 고쳐 **흡수시각**(보행이 벽에 처음 닿는 걸음 번호)을 기록하도록 하여라. $p = 0.49$, $i = 10$, $N = 20$ 으로 경로 10,000개의 흡수시각 히스토그램을 그려라.

??? success "연습문제 2 풀이"
    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    class GamblerRuinTimed(GamblerRuin):
        def simulate_with_times(self, num_paths=1, num_steps=2000, seed=None):
            path, results = self.simulate(num_paths, num_steps, seed)
            times = np.full(num_paths, np.nan)
            for i in range(num_paths):
                for t, pos in enumerate(path[i]):
                    if pos <= 0 or pos >= self.goal:
                        times[i] = t
                        break
            return path, results, times

    if __name__ == "__main__":
        g = GamblerRuinTimed(p=0.49, initial=10, goal=20)
        _, results, times = g.simulate_with_times(num_paths=10_000, num_steps=2000, seed=42)
        valid = ~np.isnan(times)
        plt.figure(figsize=(8, 5))
        plt.hist(times[valid], bins=50, edgecolor="black", alpha=0.7)
        plt.xlabel("Absorption Time")
        plt.ylabel("Frequency")
        plt.title("Distribution of Absorption Times")
        plt.tight_layout()
        plt.show()
        print(f"Mean absorption time: {np.nanmean(times):.1f}")
        print(f"Median absorption time: {np.nanmedian(times):.1f}")
    ```

    히스토그램은 오른쪽으로 심하게 치우쳐 있다. 대부분의 경로는 빨리 흡수되지만 어떤 경로는 수백 걸음이 걸린다. 오른쪽 꼬리가 길어서 평균이 중앙값보다 크다. $\square$

---

**연습문제 3.** $p = 0.49$, $i = 10$, $N = 20$ 에 대해 닫힌 꼴 공식으로 이론적인 파산 확률을 구하고 모의실험 어림값과 견주어라. 어림값이 $95\%$ 신뢰수준에서 참값의 $\pm 0.01$ 안에 들어오려면 경로가 몇 개나 필요한가?

??? success "연습문제 3 풀이"
    이론적인 파산 확률은 다음과 같다.

    $$
    Q(10) = \frac{r^{20} - r^{10}}{r^{20} - 1}, \qquad r = \frac{q}{p} = \frac{0.51}{0.49} \approx 1.04082
    $$

    계산하면 $r^{10} \approx 1.4920$, $r^{20} \approx 2.2260$ 이다.

    $$
    Q(10) = \frac{2.2260 - 1.4920}{2.2260 - 1} = \frac{0.7340}{1.2260} \approx 0.599
    $$

    너비가 $\pm 0.01$ 인 $95\%$ 신뢰구간을 얻으려면 다음이 필요하다.

    $$
    1.96\,\sqrt{\frac{Q(1-Q)}{n}} \le 0.01
    $$

    $Q \approx 0.6$ 이면 $Q(1-Q) \approx 0.24$ 이다.

    $$
    n \ge \left(\frac{1.96}{0.01}\right)^2 \cdot 0.24 \approx 9{,}220
    $$

    그러므로 대략 $n \ge 9{,}300$ 개면 충분하다. 경로 $n = 10{,}000$ 개짜리 모의실험이면 정밀도가 넉넉하다. $\square$

---

**연습문제 4.** $p = 0.49$, $i = 10$, $N = 20$ 에 대해 표본경로 20개를 한 그림에 함께 그려라. 파산으로 끝난 경로는 빨강으로, 목표에 이른 경로는 초록으로 칠하여라.

??? success "연습문제 4 풀이"
    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    gambler = GamblerRuin(p=0.49, initial=10, goal=20)
    paths, results = gambler.simulate(num_paths=20, num_steps=500, seed=42)

    fig, ax = plt.subplots(figsize=(12, 5))
    for i in range(20):
        # 흡수시각 찾기
        t_end = len(paths[i])
        for t, pos in enumerate(paths[i]):
            if pos <= 0 or pos >= 20:
                t_end = t + 1
                break
        color = "red" if results[i] == -1 else ("green" if results[i] == 1 else "gray")
        ax.plot(paths[i, :t_end], color=color, alpha=0.5, linewidth=0.8)

    ax.axhline(0, color="black", linestyle="--", alpha=0.3)
    ax.axhline(20, color="black", linestyle="--", alpha=0.3)
    ax.set_xlabel("Step")
    ax.set_ylabel("Capital")
    ax.set_title("20 Sample Paths (red = ruin, green = goal)")
    plt.tight_layout()
    plt.show()
    ```

    그림에는 $i = 10$ 에서 퍼져 나가는 부챗살 모양의 경로들이 나타난다. 파산으로 끝난 경로(빨강)는 아래로 흘러가는 경향이 있고, 목표에 이른 더 적은 수의 경로(초록)는 흐름을 거슬러 위로 치고 올라가는 모습을 보인다. $\square$

---

**연습문제 5.** 코드가 걸음을 만들 때 `2 * np.random.binomial(1, self.p, ...) - 1` 을 쓰는 까닭을 설명하여라. 각 걸음은 어떤 분포를 따르는가? $E[X_k] = 2p - 1$ 과 $\text{Var}(X_k) = 4p(1-p)$ 임을 확인하여라.

??? success "연습문제 5 풀이"
    $B \sim \text{Bernoulli}(p)$ 라 하자. 그러면 확률 $p$ 로 $B = 1$ 이고 확률 $q = 1-p$ 로 $B = 0$ 이다. 변환 $X = 2B - 1$ 은 다음과 같이 옮긴다.

    - $B = 1 \mapsto X = +1$ (이김, 확률 $p$),
    - $B = 0 \mapsto X = -1$ (짐, 확률 $q$).

    그러므로 $X$ 는 바라던 확률로 $\pm 1$ 의 값을 가진다. 이를 **라데마허 꼴** 확률변수(모수 $p$ 를 가지도록 옮긴 것)라고 부른다.

    **평균:**

    $$
    E[X] = E[2B - 1] = 2E[B] - 1 = 2p - 1
    $$

    **분산:**

    $$
    \text{Var}(X) = \text{Var}(2B - 1) = 4\,\text{Var}(B) = 4p(1-p)
    $$

    $p = 0.49$ 이면 $E[X] = -0.02$ 이고 $\text{Var}(X) = 4(0.49)(0.51) = 0.9996 \approx 1$ 이다. $\square$

---

**연습문제 6.** `simulate` 메서드의 안쪽 반복문은 벽에 닿았는지 알아보려고 위치를 하나씩 차례로 살핀다. `np.argmax` 나 `np.where` 를 쓰는 벡터화한 대안을 제안하고 구현하여라. 경로 100,000개에 대해 걸리는 시간을 견주어 보아라.

??? success "연습문제 6 풀이"
    ```python
    import numpy as np
    import time

    def simulate_vectorized(p, initial, goal, num_paths, num_steps, seed=42):
        np.random.seed(seed)
        steps = 2 * np.random.binomial(1, p, (num_paths, num_steps)) - 1
        path = initial + np.concatenate(
            [np.zeros((num_paths, 1)), steps.cumsum(axis=1)], axis=1
        )
        # 닿은 곳 찾기: path <= 0 또는 path >= goal 인 자리가 True
        hit_ruin = (path <= 0)
        hit_goal = (path >= goal)
        hit_any = hit_ruin | hit_goal

        # 경로마다 처음 닿은 시각 (argmax가 첫 True를 찾아 준다)
        has_hit = hit_any.any(axis=1)
        first_hit = np.argmax(hit_any, axis=1)

        results = np.zeros(num_paths)
        for i in range(num_paths):
            if has_hit[i]:
                t = first_hit[i]
                if path[i, t] <= 0:
                    results[i] = -1
                else:
                    results[i] = 1
        return results

    if __name__ == "__main__":
        n = 100_000
        t0 = time.time()
        r = simulate_vectorized(0.49, 10, 20, n, 2000)
        t1 = time.time()
        ruin = np.sum(r == -1)
        win = np.sum(r == 1)
        print(f"Ruin prob: {ruin / (ruin + win):.4f}")
        print(f"Time: {t1 - t0:.2f}s")
    ```

    벡터화한 판은 불 배열에 `np.argmax` 를 써서(첫 `True` 의 자리를 돌려준다) 위치를 하나씩 훑는 파이썬 안쪽 반복문을 없앤다. 경로를 도는 바깥 반복문은 남아 있지만 경로마다 $O(1)$ 만큼만 일한다. 경로 100,000개에서는 대개 원래의 이중 반복문 판보다 5~10배 빠르다. 고급 색인을 쓰면 바깥 반복문까지 없앤 완전 벡터화도 가능하다. $\square$
