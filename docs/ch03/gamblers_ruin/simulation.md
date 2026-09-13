# 도박꾼의 파산 모의실험

## 표본경로 모의실험

도박꾼의 파산에서 표본경로 하나를 그려 보면 도박꾼의 밑천이 시간에 따라 확률보행을 하는 모습이 드러난다. 이 보행은 0(파산)이나 $N$ (목표)에 닿으면 끝난다.

### 파이썬 구현 — 경로 하나

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# 모수
p = 0.49          # 한 판을 이길 확률
IC = 100          # 처음 밑천
Goal = 200        # 목표
n = 10000         # 걸음 수의 최댓값

# 경로 만들기: 확률 p로 +1, 확률 q로 -1
steps = 2 * np.random.binomial(1, p, size=n) - 1
path = IC + np.cumsum(steps)
path = np.insert(path, 0, IC)

# 그림 그리기
plt.figure(figsize=(10, 5))
plt.plot(range(n + 1), path[:n + 1], linewidth=0.5)
plt.axhline(y=0, color='r', linewidth=1)
plt.axhline(y=Goal, color='r', linewidth=1)
plt.xlabel('Step')
plt.ylabel('Capital')
plt.title(f'Gambler\'s Ruin Sample Path (IC={IC}, Goal={Goal}, p={p})')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('gamblers_ruin_path.png', dpi=150, bbox_inches='tight')
plt.show()
```

## 몬테카를로로 파산 확률 어림하기

도박꾼의 파산 경로를 독립적으로 여러 개 모의실험한 뒤 파산으로 끝난 비율을 세면 $Q(i)$ 의 몬테카를로 어림값을 얻는다.

### 파이썬 구현 — 몬테카를로

```python
import numpy as np

np.random.seed(42)

# 모수
p = 0.49
IC = 100
Goal = 200
n = 10000           # 모의실험 하나당 최대 걸음 수
num_simu = 1000     # 모의실험 횟수

# 모든 경로를 한꺼번에 만든다
steps = 2 * np.random.binomial(1, p, size=(num_simu, n)) - 1
paths = IC + np.cumsum(steps, axis=1)
paths = np.hstack([IC * np.ones((num_simu, 1)), paths])

# 닿는 시각이 유한하도록 보초값을 덧붙인다
paths = np.hstack([paths, np.zeros((num_simu, 1)), Goal * np.ones((num_simu, 1))])

ruin_counter = 0
success_counter = 0
undecided_counter = 0

for i in range(num_simu):
    path = paths[i, :]
    # 0과 Goal에 처음 닿는 시각을 찾는다
    hits_zero = np.where(path <= 0)[0]
    hits_goal = np.where(path >= Goal)[0]
    
    T_0 = hits_zero[0] if len(hits_zero) > 0 else n + 10
    T_Goal = hits_goal[0] if len(hits_goal) > 0 else n + 10
    
    if T_0 <= n and T_0 < T_Goal:
        ruin_counter += 1
    elif T_Goal <= n and T_Goal < T_0:
        success_counter += 1
    else:
        undecided_counter += 1

print(f"Ruin:      {ruin_counter}")
print(f"Success:   {success_counter}")
print(f"Undecided: {undecided_counter}")

decided = ruin_counter + success_counter
if decided > 0:
    ruin_prob_est = ruin_counter / decided
    print(f"\nEstimated ruin probability: {ruin_prob_est:.4f}")
```

### 대표적인 결과

$p = 0.49$, $IC = 100$, $Goal = 200$ 으로 100번 모의실험하면 다음과 같다.

| 결과 | 횟수 |
|---------|-------|
| 파산 | 89 |
| 성공 | 4 |
| 미결 | 7 |

$$
\hat{Q}(100) = \frac{89}{89 + 4} = 0.957
$$

이론값과 잘 들어맞는다. $p$ 가 $0.5$ 에 가까운데도 파산 확률이 이토록 높다는 점이 이 문제를 "도박꾼의 파산"이라 부르는 까닭을 잘 보여 준다.

## 선형계로 수치해 구하기

처음 밑천이 $i = 0, 1, \ldots, N$ 인 모든 경우의 파산 확률은 점화식에서 나오는 삼중대각 선형계를 풀어 정확히 구할 수 있다([첫걸음 분석](first_step_analysis.md)을 보아라).

### 파이썬 구현 — 정확한 해

```python
import numpy as np
from scipy.sparse import spdiags
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for idx, p in enumerate([0.49, 0.50]):
    q = 1 - p
    Goal = 200

    # 삼중대각 계를 세운다: -q*Q(i-1) + Q(i) - p*Q(i+1) = 0
    n = Goal - 1
    d = np.ones(n)
    diagonals = np.array([-q * d, d, -p * d])
    offsets = [-1, 0, 1]
    A = spdiags(diagonals, offsets, n, n, format='csc')

    # 우변: 경계 조건 Q(0) = 1 에서 b(1) = q
    b = np.zeros(n)
    b[0] = q

    # 풀기
    Q_interior = spsolve(A, b)
    Q = np.concatenate([[1.0], Q_interior, [0.0]])

    # 그림 그리기
    axes[idx].plot(range(Goal + 1), Q)
    axes[idx].set_xlabel('Initial Capital')
    axes[idx].set_ylabel('Ruin Probability')
    axes[idx].set_title(f'p = {p}')
    axes[idx].grid(True, alpha=0.3)

plt.suptitle("Gambler's Ruin Probability")
plt.tight_layout()
plt.savefig('gamblers_ruin_exact.png', dpi=150, bbox_inches='tight')
plt.show()
```

왼쪽 그림($q > 1/2$)은 밑천이 줄어들 때 파산 확률이 지수적으로 빠르게 1에 다가가는 모습을 보여 준다. 오른쪽 그림($q = 1/2$)은 선형인 관계를 보여 준다.

## 연습문제

**연습문제 1.** 도박꾼의 파산 문제를 파이썬으로 모의실험하여라. $p = 0.49$, 처음 밑천 $i = 100$, 목표 $N = 200$ 으로 1,000번 돌린 뒤 어림한 파산 확률을 이론값과 견주어 보아라.

??? success "연습문제 1 풀이"
    ```python
    """도박꾼의 파산 모의실험: 파산 확률을 어림한다."""
    import random

    # === 한 번의 시행 ===
    def gamblers_ruin_trial(p: float, i: int, N: int) -> bool:
        """도박꾼이 파산하면(0에 이르면) True, N에 이르면 False를 돌려준다."""
        capital = i
        while 0 < capital < N:
            if random.random() < p:
                capital += 1
            else:
                capital -= 1
        return capital == 0

    # === 이론 공식 ===
    def theoretical_ruin(p: float, i: int, N: int) -> float:
        q = 1 - p
        if p == 0.5:
            return (N - i) / N
        r = q / p
        return (r**N - r**i) / (r**N - 1)

    # === 실험 돌리기 ===
    if __name__ == "__main__":
        p, i, N, trials = 0.49, 100, 200, 1_000
        ruins = sum(gamblers_ruin_trial(p, i, N) for _ in range(trials))
        print(f"Simulated ruin probability: {ruins / trials:.4f}")
        print(f"Theoretical ruin probability: {theoretical_ruin(p, i, N):.4f}")
    ```

    대개 모의실험 값은 $\approx 0.98$, 이론값은 $\approx 0.9820$ 이 나온다. 몬테카를로 오차 범위 안에서 두 값이 일치한다.
