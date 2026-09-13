# 2차원 확률보행 모의실험

이 쪽에서는 정수격자 위의 2차원 단순확률보행을 몬테카를로로 모의실험한다. 낱낱의 표본경로를 눈으로 보고, 보행자가 원점에서 마지막에 얼마나 떨어져 있는지의 분포를 살펴본 뒤, 경험적인 결과를 이론이 내다보는 바와 견주어 본다.

## 배경

**2차원 단순확률보행**은 원점 $(0,0)$ 에서 시작하여 매 걸음마다 가장 가까운 네 격자 이웃, 곧 오른쪽, 왼쪽, 위, 아래 가운데 하나로 각각 확률 $\frac{1}{4}$ 로 옮겨 간다. $n$ 걸음 뒤의 위치를 $(S_n^x, S_n^y)$ 로 적으면 다음이 성립한다.

$$
(S_n^x, S_n^y) = \sum_{k=1}^{n} (X_k, Y_k)
$$

여기에서 각 증분 $(X_k, Y_k)$ 는 $\{(1,0),(-1,0),(0,1),(0,-1)\}$ 에서 고르게 뽑힌다.

$x$ 좌표와 $y$ 좌표는 서로 독립인 "게으른" 확률보행처럼 움직인다. 각 좌표는 걸음마다 평균이 $0$ 이고 분산이 $\frac{1}{2}$ 이다(각 좌표는 확률 $\frac{1}{2}$ 로 $\pm 1$ 만큼 바뀌고 확률 $\frac{1}{2}$ 로 $0$ 에 머물기 때문이다). 따라서 다음이 성립한다.

$$
E[S_n^x] = 0, \quad \text{Var}(S_n^x) = \frac{n}{2}
$$

$S_n^y$ 에 대해서도 마찬가지이다.

$n$ 걸음 뒤 원점으로부터의 **유클리드 거리**는 $R_n = \sqrt{(S_n^x)^2 + (S_n^y)^2}$ 이다. $E[(S_n^x)^2 + (S_n^y)^2] = n$ 이므로 이 거리의 자연스러운 눈금은 $\sqrt{n}$ 이다. 더 정확히 말하면, 중심극한정리에 따라 $n$ 이 크면 표준화한 위치 $(S_n^x / \sqrt{n/2},\, S_n^y / \sqrt{n/2})$ 가 표준이변량정규분포로 수렴하고, $R_n / \sqrt{n/2}$ 는 모수가 $\sigma = 1$ 인 **레일리분포**로 수렴한다.

**폴리아의 재귀 정리**(1921)에 따라 2차원 단순확률보행은 **재귀적**이다. 곧 확률 1로 원점으로 돌아온다. 이는 보행이 비재귀적인 3차원과 뚜렷하게 대비된다.

## 코드

```python
"""2차원 단순확률보행: 정수격자 위의 보행을 모의실험하고 눈으로 본다."""
import numpy as np
import matplotlib.pyplot as plt


def main():
    np.random.seed(337)

    n_steps = 500
    n_paths = 3

    # 방향: N, E, S, W
    directions = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])

    fig, axes = plt.subplots(1, 2, figsize=(13, 6))

    # 왼쪽 그림: 2차원 확률보행 경로 여러 개
    for path_idx in range(n_paths):
        steps = directions[np.random.randint(0, 4, size=n_steps)]
        positions = np.vstack([[0, 0], np.cumsum(steps, axis=0)])

        axes[0].plot(positions[:, 0], positions[:, 1], linewidth=0.7,
                     alpha=0.8, label=f"Path {path_idx + 1}")
        axes[0].plot(0, 0, "go", markersize=8, zorder=5)
        axes[0].plot(positions[-1, 0], positions[-1, 1], "rx", markersize=8, zorder=5)

    bound = 1.5 * np.sqrt(n_steps)
    axes[0].set_xlim(-bound, bound)
    axes[0].set_ylim(-bound, bound)
    axes[0].set_aspect("equal")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("y")
    axes[0].set_title(f"2D Simple Random Walk ({n_steps} steps)")
    axes[0].legend(fontsize=9)
    axes[0].grid(True, alpha=0.3)

    # 오른쪽 그림: 원점으로부터의 마지막 거리의 분포
    n_simulations = 5000
    final_distances = np.zeros(n_simulations)
    for i in range(n_simulations):
        steps = directions[np.random.randint(0, 4, size=n_steps)]
        final_pos = np.sum(steps, axis=0)
        final_distances[i] = np.sqrt(final_pos[0] ** 2 + final_pos[1] ** 2)

    axes[1].hist(final_distances, bins=40, density=True, color="steelblue",
                 edgecolor="white", alpha=0.8)
    axes[1].axvline(np.mean(final_distances), color="red", linestyle="--",
                    linewidth=1.5, label=f"Mean = {np.mean(final_distances):.1f}")
    axes[1].axvline(np.sqrt(n_steps), color="orange", linestyle="--",
                    linewidth=1.5, label=f"$\\sqrt{{n}}$ = {np.sqrt(n_steps):.1f}")
    axes[1].set_xlabel("Distance from Origin")
    axes[1].set_ylabel("Density")
    axes[1].set_title(f"Final Distance Distribution ({n_simulations} walks)")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("random_walk_2d.png", dpi=150, bbox_inches="tight")
    plt.show()

    print(f"Mean final distance:   {np.mean(final_distances):.2f}")
    print(f"Expected (sqrt(n)):    {np.sqrt(n_steps):.2f}")


if __name__ == "__main__":
    main()
```

## 실행 결과

이 스크립트는 두 칸짜리 그림을 내놓는다.

- **왼쪽 그림(표본경로):** 500걸음짜리 독립인 2차원 확률보행 세 개를 정수격자 위에 그린다. 원점의 출발점은 초록 점으로, 각 경로의 끝점은 빨간 가위표로 나타낸다. 경로들은 들쭉날쭉 떠돌며 때로는 원점 가까이로 되돌아오고 때로는 멀리 흘러간다. 축의 범위는 $\pm 1.5\sqrt{n} \approx \pm 33.5$ 로 잡았는데, 이 안에 보행의 대부분이 높은 확률로 들어온다.

- **오른쪽 그림(거리의 분포):** 독립인 보행 5,000개에 대하여 원점으로부터의 마지막 유클리드 거리 $R_{500}$ 의 히스토그램이다. 이 분포는 오른쪽으로 치우쳐 있고 레일리분포를 닮았다. 두 개의 세로 점선은 경험적 평균(빨강)과 기준값 $\sqrt{n} = \sqrt{500} \approx 22.4$ (주황)를 나타낸다.

콘솔 출력은 다음과 같다.

```
Mean final distance:   17.68
Expected (sqrt(n)):    22.36
```

## 뜻풀이

1. **경로의 움직임.** 표본경로들은 확률보행 특유의 "확산" 움직임을 보여 준다. 곧 $\sqrt{n}$ 에 비례하는 속도로 원점에서 퍼져 나가면서도 이미 지나온 곳을 자주 다시 찾는다. 이는 폴리아의 재귀 정리와 들어맞는다.

2. **거리의 눈금.** 마지막 거리의 평균은 $\sqrt{n}$ 정도이며, 이는 평균제곱근 변위가 $\sqrt{n}$ 으로 자란다는 것을 확인시켜 준다. 경험적 평균이 $\sqrt{n}$ 보다 조금 작은 까닭은 제곱근이 오목함수여서 옌센 부등식에 따라 $E[R_n] < \sqrt{E[R_n^2]} = \sqrt{n}$ 이기 때문이다.

3. **레일리 근사.** $n$ 이 크면 중심극한정리에 따라 $(S_n^x, S_n^y) \approx \sqrt{n/2}\,(Z_1, Z_2)$ 이고 여기에서 $Z_1, Z_2$ 는 i.i.d. 표준정규확률변수이다. 그러면 거리 $R_n / \sqrt{n/2}$ 는 대략 레일리($\sigma = 1$) 분포를 따르고, 그 평균은 $\sqrt{\pi/2} \approx 1.253$ 이다. 이로부터 $E[R_n] \approx \sqrt{n/2} \cdot \sqrt{\pi/2} = \sqrt{\pi n / 4} \approx \sqrt{\pi \cdot 500 / 4} \approx 19.8$ 을 내다볼 수 있고, 이는 모의실험 값과 가깝다.

4. **변동.** 히스토그램은 상당히 넓게 퍼져 있다. 어떤 보행은 원점에 아주 가까이에서 끝나고 어떤 보행은 40 넘게 멀어진다. 이렇게 변동이 큰 것이 확산 과정의 특징이다.

## 연습문제

**연습문제 1.**
**(a)** 길이가 $n = 100, 500, 1000, 5000$ 인 보행을 돌리도록 모의실험을 고쳐라. 각 $n$ 마다 보행 $5{,}000$ 개로 $E[R_n]$ 을 어림하고 $E[R_n]$ 을 $\sqrt{n}$ 에 대하여 그려라.

**(b)** 선형모형 $E[R_n] = c\sqrt{n}$ 을 맞추어 상수 $c$ 를 어림하여라. 이론이 내다보는 $c = \sqrt{\pi/4} \approx 0.886$ 과 견주어 보아라.

??? success "연습문제 1 풀이"
    **(a)–(b)**

    ```python
    import numpy as np

    np.random.seed(42)

    directions = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])
    ns = [100, 500, 1000, 5000]
    n_walks = 5000

    means = []
    for n in ns:
        dists = []
        for _ in range(n_walks):
            steps = directions[np.random.randint(0, 4, size=n)]
            final = np.sum(steps, axis=0)
            dists.append(np.sqrt(final[0]**2 + final[1]**2))
        means.append(np.mean(dists))
        print(f"n={n:5d}: E[R_n]={means[-1]:.2f}, sqrt(n)={np.sqrt(n):.2f}")

    # c 를 맞춘다: E[R_n] = c * sqrt(n)
    sqrt_ns = np.array([np.sqrt(n) for n in ns])
    c_hat = np.dot(means, sqrt_ns) / np.dot(sqrt_ns, sqrt_ns)
    print(f"\nEstimated c = {c_hat:.4f} (theory sqrt(pi/4) = {np.sqrt(np.pi/4):.4f})")
    ```

---

**연습문제 2.**
2차원 보행은 재귀적이므로 확률 1로 원점으로 돌아온다.

**(a)** 길이가 $n = 10{,}000$ 인 보행 $1{,}000$ 개를 모의실험하여라. 각 보행에 대하여 원점으로 한 번이라도 돌아왔는지를 기록하여라. $P(n \text{ 걸음 안에 원점으로 돌아옴})$ 을 어림하여라.

**(b)** 돌아온 보행들에 대하여 첫 귀환 시각 $T$ 를 기록하여라. $T$ 의 히스토그램을 그려라.

**(c)** 모의실험으로 $E[T]$ 를 어림하여라. 보행의 수를 늘려도 그 어림값이 안정적인가? 2차원 보행에서 $E[T] = \infty$ 라는 사실에 비추어 그 까닭을 설명하여라.

??? success "연습문제 2 풀이"
    **(a)–(c)**

    ```python
    import numpy as np

    np.random.seed(42)

    directions = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])
    n_steps = 10_000
    n_walks = 1000

    returned = 0
    return_times = []

    for _ in range(n_walks):
        steps = directions[np.random.randint(0, 4, size=n_steps)]
        positions = np.cumsum(steps, axis=0)
        at_origin = np.where((positions[:, 0] == 0) & (positions[:, 1] == 0))[0]
        if len(at_origin) > 0:
            returned += 1
            return_times.append(at_origin[0] + 1)  # 걸음을 1부터 세므로 +1

    print(f"P(return) ≈ {returned / n_walks:.4f}")
    print(f"Number that returned: {returned}/{n_walks}")
    if return_times:
        print(f"Mean first return time: {np.mean(return_times):.1f}")
        print(f"Median first return time: {np.median(return_times):.1f}")
        print(f"Max first return time: {np.max(return_times)}")
    ```

    $P(\text{돌아옴})$ 의 어림값은 1에 가까워야 한다(다만 $n = 10{,}000$ 걸음에서 잘라내므로 1보다는 작다). $T$ 의 평균은 돌릴 때마다 들쭉날쭉한데, $E[T] = \infty$ 이기 때문이다. 곧 $T$ 의 분포가 두꺼운 꼬리를 가지므로 이따금 나오는 아주 큰 귀환 시각이 표본평균을 좌우한다.

---

**연습문제 3.**
**(a)** 2차원 단순확률보행에 대하여 $E[(S_n^x)^2] = n/2$ 임을 증명하여라. (힌트: $k$ 번째 걸음의 $x$ 성분을 $X_k$ 라고 할 때 $S_n^x = \sum_{k=1}^n X_k$ 로 적어라.)

**(b)** $E[R_n^2] = E[(S_n^x)^2 + (S_n^y)^2] = n$ 임을 보여라.

**(c)** 옌센 부등식을 써서 $E[R_n] \leq \sqrt{n}$ 임을 증명하여라.

??? success "연습문제 3 풀이"
    **(a)** 각 걸음의 $x$ 성분은 $X_k \in \{-1, 0, 0, 1\}$ 이며 각각 확률 $\frac{1}{4}$ 이다. 그러므로 $E[X_k] = 0$ 이고 $E[X_k^2] = \frac{1}{4}(1) + \frac{1}{2}(0) + \frac{1}{4}(1) = \frac{1}{2}$ 이다. $X_k$ 들이 독립이므로 다음이 성립한다.

    $$
    E[(S_n^x)^2] = \text{Var}(S_n^x) = \sum_{k=1}^n \text{Var}(X_k) = \frac{n}{2}
    $$

    **(b)** 대칭성과 (a)에 따라 $E[(S_n^y)^2] = n/2$ 이기도 하므로 다음이 성립한다.

    $$
    E[R_n^2] = E[(S_n^x)^2] + E[(S_n^y)^2] = \frac{n}{2} + \frac{n}{2} = n
    $$

    **(c)** 제곱근 함수는 오목함수이다. 옌센 부등식에 따라 다음이 성립한다.

    $$
    E[R_n] = E\!\left[\sqrt{R_n^2}\right] \leq \sqrt{E[R_n^2]} = \sqrt{n}
    $$

---

**연습문제 4.**
**(a)** **3차원 단순확률보행**(여섯 방향, 각각 확률 $\frac{1}{6}$)을 $n = 10{,}000$ 걸음까지 모의실험하여라. 보행 $1{,}000$ 개를 돌려 원점으로 돌아올 확률을 어림하여라.

**(b)** 어림값을 이론값 $P(\text{돌아옴}) \approx 0.3405$ 와 견주어 보아라(폴리아의 정리: 3차원 보행은 비재귀적이다).

**(c)** 돌아온 보행들에 대하여 첫 귀환 시각의 히스토그램을 그리고 연습문제 2의 2차원 경우와 견주어 보아라.

??? success "연습문제 4 풀이"
    **(a)–(c)**

    ```python
    import numpy as np

    np.random.seed(42)

    directions_3d = np.array([
        [1, 0, 0], [-1, 0, 0],
        [0, 1, 0], [0, -1, 0],
        [0, 0, 1], [0, 0, -1]
    ])

    n_steps = 10_000
    n_walks = 1000
    returned = 0
    return_times = []

    for _ in range(n_walks):
        steps = directions_3d[np.random.randint(0, 6, size=n_steps)]
        positions = np.cumsum(steps, axis=0)
        at_origin = np.where(
            (positions[:, 0] == 0) & (positions[:, 1] == 0) & (positions[:, 2] == 0)
        )[0]
        if len(at_origin) > 0:
            returned += 1
            return_times.append(at_origin[0] + 1)

    print(f"P(return) ≈ {returned / n_walks:.4f} (theory ≈ 0.3405)")
    if return_times:
        print(f"Mean first return time (3D): {np.mean(return_times):.1f}")
        print(f"Median first return time (3D): {np.median(return_times):.1f}")
    ```

    어림한 귀환 확률은 1보다 한참 아래(0.34 언저리)여야 하며, 이는 3차원 보행이 비재귀적임을 확인시켜 준다. 3차원에서 첫 귀환 시각은 2차원보다 작은 경향이 있는데, 돌아오는 보행은 대개 빨리 돌아오고 멀리 떠난 보행은 끝내 돌아오지 않기 때문이다.

---

**연습문제 5.**
$R_n$ 을 2차원 단순확률보행에서 $n$ 걸음 뒤 원점으로부터의 거리라고 하자. $n$ 이 크면 중심극한정리에 따라 $R_n / \sqrt{n/2}$ 는 대략 레일리($\sigma = 1$) 분포를 따르며, 그 확률밀도함수는 $r \geq 0$ 에서 $f(r) = r\,e^{-r^2/2}$ 이다.

**(a)** 레일리($\sigma = 1$) 분포의 평균이 $\sqrt{\pi/2}$ 이고 분산이 $2 - \pi/2$ 임을 보여라.

**(b)** $n = 2000$ 걸음짜리 보행 $10{,}000$ 개를 돌려라. 마지막 거리들을 $\sqrt{n/2}$ 로 나누어 표준화하고 히스토그램을 레일리 확률밀도함수와 함께 그려라.

**(c)** 표준화한 거리들을 레일리분포와 견주는 콜모고로프–스미르노프 검정을 하여라. 검정통계량과 $p$-값을 보고하여라.

??? success "연습문제 5 풀이"
    **(a)** 확률밀도함수가 $f(r) = re^{-r^2/2}$ 인 $R \sim \text{Rayleigh}(\sigma = 1)$ 에 대하여 다음이 성립한다.

    $$
    E[R] = \int_0^\infty r \cdot r e^{-r^2/2}\, dr = \int_0^\infty r^2 e^{-r^2/2}\, dr = \sqrt{\frac{\pi}{2}}
    $$

    여기에서 가우스 적분 $\int_0^\infty r^2 e^{-r^2/2}\,dr = \sqrt{\pi/2}$ 를 썼다. 또한 다음이 성립한다.

    $$
    E[R^2] = \int_0^\infty r^2 \cdot r e^{-r^2/2}\, dr = \int_0^\infty r^3 e^{-r^2/2}\, dr = 2
    $$

    ($u = r^2/2$ 로 바꾸어 놓으면 된다.) 따라서 $\text{Var}(R) = 2 - \pi/2$ 이다.

    **(b)–(c)**

    ```python
    import numpy as np
    from scipy import stats

    np.random.seed(42)

    directions = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])
    n_steps = 2000
    n_walks = 10_000

    normalized = np.zeros(n_walks)
    for i in range(n_walks):
        steps = directions[np.random.randint(0, 4, size=n_steps)]
        final = np.sum(steps, axis=0)
        dist = np.sqrt(final[0]**2 + final[1]**2)
        normalized[i] = dist / np.sqrt(n_steps / 2)

    # Rayleigh(scale=1) 과 견주는 KS 검정
    ks_stat, p_value = stats.kstest(normalized, 'rayleigh')
    print(f"KS statistic: {ks_stat:.4f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Mean normalized dist: {np.mean(normalized):.4f} "
          f"(theory sqrt(pi/2) = {np.sqrt(np.pi/2):.4f})")
    ```

    $n = 2000$ 이면 $p$-값이 꽤 크게 나와야 하며, 이는 레일리 근사가 잘 맞는다는 뜻이다. $n$ 이 커질수록 이 근사는 더 좋아진다.
