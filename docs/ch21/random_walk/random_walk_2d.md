# 2차원 단순확률보행

## 정의

**2차원 단순확률보행**은 원점 $(0, 0)$ 에서 시작하여 매 걸음마다 이웃한 네 격자점, 곧 오른쪽, 왼쪽, 위, 아래 가운데 하나로 각각 확률 $\frac{1}{4}$ 로 옮겨 간다.

$k$ 번째 걸음에서 증분 $(X_k, Y_k)$ 는 $\{(1,0), (-1,0), (0,1), (0,-1)\}$ 에서 고르게 뽑히며, $m$ 걸음 뒤의 위치는 다음과 같다.

$$
(S_m^x, S_m^y) = \sum_{k=1}^{m} (X_k, Y_k)
$$

## 모의실험

매 걸음의 방향을 균등확률변수 하나로 정하는 것이 요령이다. $[0,1)$ 을 길이가 같은 네 구간으로 나눈다.

- $[0, 0.25)$: 오른쪽으로 $(+1, 0)$
- $[0.25, 0.5)$: 왼쪽으로 $(-1, 0)$
- $[0.5, 0.75)$: 위로 $(0, +1)$
- $[0.75, 1)$: 아래로 $(0, -1)$

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

m = 100;
coin = rand(m, 1);

increment = zeros(m, 2);
increment(coin < 0.25, 1) = 1;   increment(coin < 0.25, 2) = 0;
increment(0.25 <= coin & coin < 0.5, 1) = -1;  increment(0.25 <= coin & coin < 0.5, 2) = 0;
increment(0.5 <= coin & coin < 0.75, 1) = 0;   increment(0.5 <= coin & coin < 0.75, 2) = 1;
increment(0.75 < coin, 1) = 0;   increment(0.75 < coin, 2) = -1;

walk = cumsum(increment);
walk = [0 0; walk];
r = max(max(abs(walk))) + 1;

plot(0, 0, 'or'); grid on; hold on;
axis([-r r -r r])
for k = 1:m
    plot([walk(k,1) walk(k+1,1)], [walk(k,2) walk(k+1,2)], '-r')
    pause(0.1)
end
```

**파이썬:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

m = 100
directions = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
choices = np.random.randint(0, 4, size=m)
increments = directions[choices]

walk = np.vstack([[0, 0], np.cumsum(increments, axis=0)])

plt.figure(figsize=(6, 6))
plt.plot(walk[:, 0], walk[:, 1], '-r', linewidth=0.8)
plt.plot(0, 0, 'or', markersize=8)
plt.grid(True)
plt.axis('equal')
plt.title('2D Simple Random Walk (100 steps)')
plt.show()
```

## 성질

2차원 단순확률보행은 **재귀적**이다. 곧 확률 1로 원점으로 되돌아온다(폴리아의 정리, 1921). 그러나 되돌아오기까지 걸리는 걸음 수의 기댓값은 무한이다.

이는 3차원 단순확률보행과 대조된다. 3차원에서는 확률보행이 **비재귀적**이어서 원점으로 언젠가 되돌아올 확률이 대략 0.3405이다.

## 연습문제

**연습문제 1.**
처음 가진 돈이 $i$, 목표가 $N$, $P(\text{이김}) = p$ 인 도박꾼의 파산 문제에서 다음을 하여라.

**(a)** $p = 0.5$, $i = 5$, $N = 10$ 일 때 $10{,}000$ 판을 모의실험하여 기대 지속시간 $E[D]$ 를 어림하여라. 이론값 $E[D] = i(N - i) = 25$ 와 견주어 보아라.

**(b)** $p = 0.4$ 일 때 모의실험으로 $E[D]$ 를 어림하여라. 판이 이어진 길이의 히스토그램을 그려라.

**(c)** ($i = N/2$, $p = 0.5$ 로 고정할 때) $E[D]$ 는 $N$ 에 어떻게 기대는가? $N = 4, 6, \ldots, 50$ 에 대하여 $E[D]$ 를 $N$ 에 대한 함수로 그려라.

??? success "연습문제 1 풀이"
    ```python
    import numpy as np

    np.random.seed(42)

    def gamblers_ruin_duration(i, N, p, n_trials=10000):
        durations = []
        for _ in range(n_trials):
            fortune = i
            steps = 0
            while 0 < fortune < N:
                fortune += 1 if np.random.random() < p else -1
                steps += 1
            durations.append(steps)
        return np.array(durations)

    durations = gamblers_ruin_duration(5, 10, 0.5)
    print(f"E[D] approx {np.mean(durations):.1f} (theory = 25)")
    ```

---

**연습문제 2.**
**(a)** $P(X_i = 1) = P(X_i = -1) = 1/2$ 인 1차원 단순확률보행 $S_n = \sum_{i=1}^n X_i$ 를 $n = 10{,}000$ 걸음까지 모의실험하여라. 표본경로 5개를 그려라.

**(b)** 각 경로에 대하여 $S_n > 0$ 인 시간의 비율을 셈하여라. 이를 경로 $1{,}000$ 개에 대하여 되풀이하고 히스토그램을 그려라. 어떤 분포인가? (이는 아크사인 법칙과 이어져 있다.)

**(c)** $P(\text{어떤 } n > 100 \text{ 에 대하여 } S_n = 0 \mid S_{100} = 0)$ 을 어림하여라. (힌트: $S_{100} = 0$ 을 조건으로 두고 확률보행을 이어 가라.)

??? success "연습문제 2 풀이"
    걸음 $\pm 1$ 을 한꺼번에 뽑아 `cumsum` 으로 누적하면 경로 $1{,}000$ 개를 한 번에 만들 수 있다. (b)에서 재는 값은 $\#\{k \le n : S_k > 0\}/n$ 이고, (c)에서는 $S_{100} = 0$ 인 경로만 골라 낸 뒤 마르코프 성질에 따라 원점에서 새로 시작하는 확률보행을 이어 붙인다.

    ```python
    import numpy as np
    from math import comb

    np.random.seed(42)

    # (a) 1차원 단순확률보행 표본경로 5 개, n = 10,000 걸음
    n = 10000
    n_paths = 5
    steps = np.random.choice([-1, 1], size=(n_paths, n))
    paths = np.cumsum(steps, axis=1)
    print("Five sample paths, final positions S_10000:", paths[:, -1])

    # (b) 경로 1,000 개에 대하여 S_n > 0 인 시간의 비율
    n_sim = 1000
    steps = np.random.choice([-1, 1], size=(n_sim, n))
    walks = np.cumsum(steps, axis=1)
    frac_positive = np.mean(walks > 0, axis=1)
    print(f"\nFraction of time above 0 (1000 paths, n = {n}):")
    print(f"  mean   = {frac_positive.mean():.4f}   (arcsine mean = 0.5)")
    print(f"  median = {np.median(frac_positive):.4f}")
    print(f"  P(frac < 0.1) = {np.mean(frac_positive < 0.1):.4f}"
          f"   (arcsine: {2/np.pi*np.arcsin(np.sqrt(0.1)):.4f})")
    print(f"  P(frac > 0.9) = {np.mean(frac_positive > 0.9):.4f}"
          f"   (arcsine: {1 - 2/np.pi*np.arcsin(np.sqrt(0.9)):.4f})")
    print(f"  P(0.4 < frac < 0.6) = {np.mean((frac_positive > 0.4) & (frac_positive < 0.6)):.4f}"
          f"   (arcsine: {2/np.pi*(np.arcsin(np.sqrt(0.6)) - np.arcsin(np.sqrt(0.4))):.4f})")

    # (c) S_100 = 0 을 조건으로 두고 n > 100 에서 원점으로 되돌아올 확률
    n_trials = 100000
    horizon = 10000
    first100 = np.random.choice([-1, 1], size=(n_trials, 100))
    cond = np.cumsum(first100, axis=1)[:, -1] == 0     # S_100 = 0 인 경로만 남긴다
    n_cond = int(cond.sum())

    n_return = 0
    for i in range(0, n_cond, 2000):                   # 메모리를 아끼려고 나누어 처리한다
        block = min(2000, n_cond - i)
        cont = np.random.choice([-1, 1], size=(block, horizon))
        after = np.cumsum(cont, axis=1)                # S_100 = 0 에서 이어 간다
        n_return += int(np.any(after == 0, axis=1).sum())

    print(f"\nPaths with S_100 = 0: {n_cond} of {n_trials}"
          f"   (theory {comb(100, 50) / 2**100:.4f})")
    print(f"P(S_n = 0 for some 100 < n <= {100+horizon} | S_100 = 0) "
          f"= {n_return / n_cond:.4f}")
    print(f"Theoretical escape prob. within {horizon} steps "
          f"= {1/np.sqrt(np.pi*horizon/2):.4f}")

    # (a), (b) 그림: 표본경로와 아크사인 밀도
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    for k in range(n_paths):
        axes[0].plot(paths[k], linewidth=0.7)
    axes[0].axhline(0, color='k'); axes[0].set_xlabel('n'); axes[0].set_ylabel('$S_n$')
    axes[0].set_title('Five sample paths')
    xs = np.linspace(0.001, 0.999, 400)
    axes[1].hist(frac_positive, bins=40, density=True, edgecolor='black', alpha=0.7)
    axes[1].plot(xs, 1/(np.pi*np.sqrt(xs*(1-xs))), '-r', linewidth=2)
    axes[1].set_xlabel('fraction of time with $S_n > 0$')
    axes[1].set_title('Arcsine law')
    plt.tight_layout()
    plt.show()
    ```

    **실행 결과:**
    ```
    Five sample paths, final positions S_10000: [ -26  -14   74   30 -156]

    Fraction of time above 0 (1000 paths, n = 10000):
      mean   = 0.4922   (arcsine mean = 0.5)
      median = 0.4700
      P(frac < 0.1) = 0.1860   (arcsine: 0.2048)
      P(frac > 0.9) = 0.1930   (arcsine: 0.2048)
      P(0.4 < frac < 0.6) = 0.1400   (arcsine: 0.1282)

    Paths with S_100 = 0: 8077 of 100000   (theory 0.0796)
    P(S_n = 0 for some 100 < n <= 10100 | S_100 = 0) = 0.9927
    Theoretical escape prob. within 10000 steps = 0.0080
    ```

    **(a)** 표본경로 다섯 개의 마지막 위치는 $-156$ 에서 $74$ 까지 흩어져 있다. $S_n$ 의 크기가 대체로 $\sqrt{n} = 100$ 자리라는 것과 들어맞는다. 그림에서 다섯 경로는 축 언저리를 오가는 것이 아니라 저마다 한쪽으로 오래 머무는 모습을 보인다.

    **(b)** 히스토그램은 가운데가 아니라 **양 끝에 몰리는 U자 모양**이 된다. 이것이 아크사인 법칙이며, 극한밀도는 다음과 같다.

    $$
    g(x) = \frac{1}{\pi\sqrt{x(1-x)}}, \qquad 0 < x < 1
    $$

    직관과 어긋나는 대목이 바로 여기이다. 평균은 $0.5$ 이지만 $0.5$ 근처가 가장 드물다. 실제로 비율이 $0.4$ 와 $0.6$ 사이에 드는 경로는 $14\%$ 뿐인데, $0.1$ 아래이거나 $0.9$ 위인 경로는 합쳐서 $38\%$ 가 넘는다. 모의실험 값 $0.1860$, $0.1930$, $0.1400$ 은 아크사인 법칙이 주는 $0.2048$, $0.2048$, $0.1282$ 와 잘 맞는다. 공평한 동전으로 하는 놀이에서도 한쪽이 거의 내내 앞서는 일이 오히려 흔하며, 앞섬이 반반씩 나뉘는 일이 드물다는 뜻이다.

    **(c)** $S_{100} = 0$ 인 경로는 $100{,}000$ 개 가운데 $8{,}077$ 개로, 그 비율 $0.0808$ 은 이론값 $\binom{100}{50}/2^{100} = 0.0796$ 과 맞는다. 마르코프 성질에 따라 이들은 원점에서 새로 시작하는 확률보행과 같으므로, $10{,}000$ 걸음을 더 이어 붙여 원점을 다시 밟는지 보면 된다. 그 결과 $99.27\%$ 가 되돌아왔다.

    1차원 단순확률보행은 **재귀적**이므로 참값은 정확히 $1$ 이다. 모의실험 값이 $1$ 에 못 미치는 까닭은 걸음 수를 유한하게 끊었기 때문이다. $2m$ 걸음 안에 한 번도 원점으로 돌아오지 않을 확률은 다음과 같다.

    $$
    P(S_1 \neq 0, \ldots, S_{2m} \neq 0) = \binom{2m}{m} 4^{-m} \approx \frac{1}{\sqrt{\pi m}}
    $$

    $m = 5000$ 이면 이 값이 $0.0080$ 인데, 모의실험에서 되돌아오지 못한 비율 $1 - 0.9927 = 0.0073$ 이 이와 잘 맞는다. 되돌아오는 것은 확실하지만 그때까지 기다리는 시간의 기댓값은 무한이다. 그 사정이 $1/\sqrt{m}$ 이라는 느린 수렴에 그대로 드러난다. $\square$
