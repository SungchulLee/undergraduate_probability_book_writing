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
