# 임의의 점과 단위원

## [0,1]² 안의 임의의 점 100개

단위정사각형 안에서 고르게 임의의 점을 만드는 일은 간단하다. $x$ 좌표와 $y$ 좌표로 쓸 독립인 $U(0,1)$ 표본을 두 개 만들면 된다.

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

n = 100;
x = rand(2, n);

plot(x(1,:), x(2,:), 'o')
```

**파이썬:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

n = 100
x = np.random.rand(2, n)

plt.figure()
plt.plot(x[0, :], x[1, :], 'o')
plt.xlabel('x'); plt.ylabel('y')
plt.title('100 random points in $[0,1]^2$')
plt.show()
```

이렇게 얻은 산점도는 고르게 흩어진 점들의 특징적인 모습을 보여 준다. 대체로 고르게 퍼져 있지만 자연스럽게 뭉친 곳과 빈 곳이 함께 나타난다.

## 단위원 안에 든 점

한 걸음 더 나아가 보자. $[-1, 1]^2$ 위에서 고르게 임의의 점 100개를 만들고, 단위원 $x^2 + y^2 = 1$ 의 안에 있는지 밖에 있는지 가른다.

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

n = 100;
x = 2*rand(2, n) - 1;

plot(x(1,:), x(2,:), 'o'); grid on; hold on

r2 = x(1,:).^2 + x(2,:).^2;
i = find(r2 <= 1);
plot(x(1,i), x(2,i), 'or')

xp = -1:0.01:1;
yp = sqrt(1 - xp.^2);
plot(xp, yp, '-r', xp, -yp, '-r')
```

**파이썬:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

n = 100
x = 2 * np.random.rand(2, n) - 1

r2 = x[0, :]**2 + x[1, :]**2
inside = r2 <= 1
outside = ~inside

plt.figure(figsize=(6, 6))
plt.plot(x[0, outside], x[1, outside], 'ob', label='Outside')
plt.plot(x[0, inside], x[1, inside], 'or', label='Inside')

theta = np.linspace(0, 2*np.pi, 200)
plt.plot(np.cos(theta), np.sin(theta), '-r')

plt.axis('equal'); plt.grid(True)
plt.title('Points inside the unit circle')
plt.legend()
plt.show()
```

## 몬테카를로로 원주율 구하기와의 관계

원 안에 떨어지는 점의 비율은 넓이의 비에 가까워진다.

$$
\frac{\text{원의 넓이}}{\text{정사각형의 넓이}} = \frac{\pi \cdot 1^2}{(2)^2} = \frac{\pi}{4}
$$

따라서 점 $n$ 개 가운데 $k$ 개가 원 안에 떨어지면 다음 값이

$$
\hat{\pi} = \frac{4k}{n}
$$

$\pi$ 의 몬테카를로 어림값이 된다. 큰수의 법칙에 따라 $n \to \infty$ 일 때 $\hat{\pi} \to \pi$ 이다.

## 연습문제

**연습문제 1.**
**(a)** 모임의 크기가 $n = 2, 3, \ldots, 60$ 일 때 $P(\text{적어도 두 사람의 생일이 같다})$ 를 어림하는 모의실험을 짜라. 각 크기마다 $10{,}000$ 번씩 시행하여라. (생일 365가지가 모두 같은 정도로 일어난다고 하자.)

**(b)** 모의실험으로 얻은 확률을 정확한 공식과 함께 그려라. $n$ 이 얼마일 때 이 확률이 처음으로 0.5를 넘어서는가?

**(c)** "세 사람 생일 문제"에 맞게 모의실험을 고쳐라. 곧 $P(\text{적어도 세 사람의 생일이 같다})$ 를 구하여라. $n = 2, \ldots, 100$ 에 대하여 그려라.

??? success "연습문제 1 풀이"
    모임 크기마다 $10{,}000$ 번씩 시행해야 하므로 반복문 대신 벡터 연산을 쓴다. 한 번의 시행에서 뽑은 생일을 정렬해 두면, $m-1$ 칸 떨어진 두 자리의 값이 같다는 것과 같은 생일인 사람이 $m$ 명 이상 있다는 것이 같은 말이 된다. 이 한 가지 요령으로 (a)의 두 사람 문제와 (c)의 세 사람 문제를 함께 다룰 수 있다. 비교에 쓸 정확한 공식은 여집합 세기로 얻는다.

    $$
    P(n) = 1 - \prod_{k=0}^{n-1}\left(1 - \frac{k}{365}\right)
    $$

    ```python
    import numpy as np

    np.random.seed(42)

    n_trials = 10000
    sizes = np.arange(2, 61)

    # (a) 모임 크기마다 생일을 뽑아 같은 생일이 있는지 센다 (벡터화)
    def simulate_birthday(n, n_trials=10000, m=2):
        days = np.random.randint(0, 365, size=(n_trials, n))
        days.sort(axis=1)
        # 정렬한 뒤 m-1 칸 떨어진 값이 같으면 같은 생일이 m 명 이상 있다
        if n < m:
            return 0.0
        return np.mean(np.any(days[:, (m - 1):] == days[:, :n - (m - 1)], axis=1))

    sim = np.array([simulate_birthday(n, n_trials) for n in sizes])

    # 정확한 공식: P(n) = 1 - prod_{k=0}^{n-1} (1 - k/365)
    exact = 1 - np.array([np.prod(1 - np.arange(n) / 365) for n in sizes])

    # (b) 확률이 처음으로 0.5 를 넘는 모임 크기
    n_sim = sizes[np.argmax(sim > 0.5)]
    n_exact = sizes[np.argmax(exact > 0.5)]

    print("  n   simulated    exact")
    for n in [10, 20, 22, 23, 30, 40, 50, 60]:
        i = n - 2
        print(f"{n:3d}    {sim[i]:.4f}    {exact[i]:.4f}")
    print(f"\nFirst n with P > 0.5: simulation = {n_sim}, exact = {n_exact}")
    print(f"P(22) = {exact[20]:.4f},  P(23) = {exact[21]:.4f}")

    # (c) 세 사람 생일 문제
    sizes3 = np.arange(2, 101)
    sim3 = np.array([simulate_birthday(n, n_trials, m=3) for n in sizes3])
    n3 = sizes3[np.argmax(sim3 > 0.5)]
    print("\nTriple birthday problem:")
    for n in [30, 50, 70, 80, 88, 90, 100]:
        print(f"  n = {n:3d}: P(at least three share) = {sim3[n-2]:.4f}")
    print(f"First n with P > 0.5 (triple) = {n3}")

    # (b) 그림: 모의실험 값과 정확한 공식을 겹쳐 그린다
    import matplotlib.pyplot as plt
    plt.figure(figsize=(7, 5))
    plt.plot(sizes, sim, 'o', markersize=4, label='Simulation')
    plt.plot(sizes, exact, '-r', label='Exact formula')
    plt.axhline(0.5, color='gray', linestyle='--')
    plt.xlabel('Group size n'); plt.ylabel('P(at least two share a birthday)')
    plt.legend(); plt.grid(True)
    plt.show()
    ```

    **실행 결과:**
    ```
      n   simulated    exact
     10    0.1174    0.1169
     20    0.4050    0.4114
     22    0.4791    0.4757
     23    0.4974    0.5073
     30    0.7051    0.7063
     40    0.8887    0.8912
     50    0.9687    0.9704
     60    0.9950    0.9941

    First n with P > 0.5: simulation = 24, exact = 23
    P(22) = 0.4757,  P(23) = 0.5073

    Triple birthday problem:
      n =  30: P(at least three share) = 0.0299
      n =  50: P(at least three share) = 0.1281
      n =  70: P(at least three share) = 0.3065
      n =  80: P(at least three share) = 0.4172
      n =  88: P(at least three share) = 0.5091
      n =  90: P(at least three share) = 0.5320
      n = 100: P(at least three share) = 0.6501
    First n with P > 0.5 (triple) = 88
    ```

    모의실험으로 얻은 값과 정확한 공식은 어느 모임 크기에서나 0.01 안팎에서 맞아떨어진다. 그림에서 점(모의실험)은 빨간 곡선(정확한 공식) 위에 거의 그대로 얹힌다. 정확한 값으로 보면 $P(22) = 0.4757$, $P(23) = 0.5073$ 이므로 확률이 처음으로 $0.5$ 를 넘어서는 크기는 $n = 23$ 이다. 이것이 널리 알려진 "생일 문제"의 답이다. 다만 모의실험만 놓고 보면 $n = 23$ 에서 $0.4974$ 가 나와 경계를 아슬아슬하게 밑돌아 $n = 24$ 로 읽히는데, 이는 $10{,}000$ 번 시행의 표준오차가 $\sqrt{0.25/10000} = 0.005$ 정도이기 때문이다. 참값이 경계에 이렇게 가까울 때에는 모의실험만으로 경계를 가려내기 어렵다는 점을 함께 새겨 둘 만하다.

    세 사람 문제에서는 같은 정렬 요령에 $m = 3$ 만 넣으면 된다. 확률이 훨씬 천천히 자라서 $n = 88$ 에 이르러서야 $0.5$ 를 넘는다. 두 사람이 겹치는 짝은 $\binom{n}{2}$ 개이지만 세 사람이 겹치는 조는 $\binom{n}{3}$ 개이면서 각 조가 겹칠 확률은 $1/365^2$ 로 훨씬 작아지므로, 필요한 인원이 23명에서 88명으로 크게 늘어난다. $\square$

---

**연습문제 2.**
뷔퐁의 바늘 실험을 모의실험하여라. 길이가 $\ell$ 인 바늘을 간격이 $d \geq \ell$ 인 평행선 위에 떨어뜨린다. 선을 가로지를 확률은 $\frac{2\ell}{\pi d}$ 이다. 이를 써서 $\ell = d = 1$ 로 $100{,}000$ 번 떨어뜨려 $\pi$ 를 어림하여라.

??? success "연습문제 2 풀이"
    ```python
    import numpy as np

    np.random.seed(42)

    def buffon_needle(n_drops=100000, ell=1, d=1):
        theta = np.random.uniform(0, np.pi, n_drops)
        x = np.random.uniform(0, d / 2, n_drops)
        crosses = x <= (ell / 2) * np.sin(theta)
        p_cross = np.cumsum(crosses) / np.arange(1, n_drops + 1)
        pi_est = (2 * ell) / (d * p_cross)
        return pi_est

    pi_estimates = buffon_needle()
    print(f"pi estimate = {pi_estimates[-1]:.5f}")
    ```
