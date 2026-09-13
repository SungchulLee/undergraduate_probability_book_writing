# 푸아송 과정 모의실험

모의실험은 푸아송 과정의 이론적인 성질을 손에 잡히게 확인하는 방법이다. 이 쪽에서는 서로를 채워 주는 두 가지 모의실험 방법을 구현한다. 하나는 시간을 잘게 나누어 베르누이 동전을 던지는 방법이고, 다른 하나는 지수분포를 따르는 도착간격을 쓰는 방법이다. 두 방법이 만들어 내는 사건의 무늬를 견주어 본다.

## 배경

비율이 $\lambda$ 인 푸아송 과정은 근본적으로 다른 두 가지 방법으로 만들 수 있으며, 각 방법은 이 과정의 핵심적인 특징 하나씩을 비추어 준다.

**방법 1 — 베르누이 근사.** 관찰 구간 $[0, T]$ 를 길이가 $\Delta = T/n$ 인 아주 작은 구간 $n$ 개로 나눈다. 각 작은 구간에서 사건은 확률 $p = \lambda / n$ 로 서로 독립하게 일어난다. 각 작은 구간이 하나의 베르누이 시행이고, 전체 개수는 이항분포 $B(nT, \lambda/n)$ 을 따른다. $n \to \infty$ 일 때 푸아송 극한정리에 따라 이것은 푸아송 과정으로 수렴한다.

**방법 2 — 지수분포 도착간격.** 잇따른 사건 사이의 도착간격 $T_1, T_2, T_3, \ldots$ 은 독립이고 같은 지수분포를 따르는 확률변수이다.

$$
T_i \sim \text{Exp}(\lambda), \quad f_{T_i}(t) = \lambda e^{-\lambda t}, \quad t \geq 0
$$

$n$ 번째 도착시각은 $S_n = T_1 + T_2 + \cdots + T_n$ 이다. 사건을 시각 $S_1, S_2, \ldots$ 에 놓고, $S_n$ 이 관찰 구간을 넘어설 때까지 이어 간다.

두 방법 모두 같은 푸아송 과정의 실현을 만들어 낸다. 베르누이 방법은 쪼갠 개수 $n$ 이 커질수록 좋아지는 근사이고, 지수분포 방법은 푸아송 과정의 표본 경로를 정확히 만들어 낸다.

## 코드

```python
"""푸아송 과정을 두 가지로 모의실험한다: 베르누이 동전 던지기와 지수분포 도착간격."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

LA = 1       # 비율(lambda)
BT = 1 / LA  # 평균 도착간격
N = 1000     # 시간을 잘게 나누는 촘촘함
P = LA / N   # 아주 작은 구간마다의 성공확률
T = 8        # 관찰 구간 [0, T]


def ppp_coin(ax):
    """아주 작은 구간마다 치우친 동전을 던져 푸아송 과정을 근사한다."""
    x = np.random.binomial(1, P, size=int(N * T))
    arrivals = [i / N for i, v in enumerate(x) if v]
    ax.plot(arrivals, np.zeros(len(arrivals)), "o", color="red", label="PPP via coin")


def ppp_expon(ax):
    """지수분포 도착간격을 써서 푸아송 과정을 정확히 만든다."""
    interarrivals = np.random.exponential(scale=BT, size=int(LA * T * 10))
    arrivals = interarrivals.cumsum()
    arrivals = arrivals[arrivals < T]
    ax.plot(arrivals, np.ones(len(arrivals)), "o", color="blue", label="PPP via exponential")


def main():
    fig, ax = plt.subplots(figsize=(14, 2))
    ppp_coin(ax)
    ppp_expon(ax)
    ax.legend(loc="center right")
    ax.set_title(f"Poisson Process (λ = {LA}, T = {T})", fontsize=13)
    ax.set_xlabel("Time")
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    plt.tight_layout()
    plt.savefig("poisson_process_simulation.png", dpi=150, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
```

## 실행 결과

이 스크립트는 구간 $[0, 8]$ 위의 같은 시간축에 점을 두 줄로 찍은 그림 하나를 만든다.

- **빨간 점**(아래쪽 줄, $y = 0$): 단위시간당 작은 구간 $n = 1000$ 개를 쓰는 베르누이 동전 던지기 방법으로 만든 도착시각이다.
- **파란 점**(위쪽 줄, $y = 1$): 지수분포 도착간격을 뽑아 만든 도착시각이다.

비율이 $\lambda = 1$ 이고 관찰 구간이 $T = 8$ 이므로 두 방법 모두 평균 8개쯤의 사건을 만들어 낸다. 점들은 시간축을 따라 들쭉날쭉 흩어져 있으며, 푸아송 과정 특유의 뭉침과 빈틈을 보여 준다.

## 뜻풀이

두 모의실험 방법은 푸아송 과정의 서로 다른 면을 비추어 준다.

**분포가 일치한다.** 두 줄 모두 사건의 개수가 거의 같다. 평균 $\lambda T = 8$ 쯤이며, 이는 $n$ 이 클 때 베르누이 근사가 정확한 푸아송 과정으로 수렴함을 확인해 준다. 길이가 $t$ 인 어떤 부분구간에서든 사건 개수는 두 방법 모두 대략 $\text{Po}(\lambda t)$ 를 따른다.

**도착 무늬의 무작위성.** 점들은 고르게 떨어져 있지 않다. 어떤 곳에서는 사건이 바싹 뭉쳐 있고 또 어떤 구간은 텅 비어 있다. 이것이 푸아송 과정의 표지이다. 지수분포의 무기억성 때문에, 방금 사건이 일어났다는 사실은 다음 사건이 언제 일어날지에 대해 아무것도 알려 주지 않는다.

**베르누이로 잘게 나누기.** 동전 던지기 방법은 단위시간당 아주 작은 구간 $n = 1000$ 개를 쓰므로 사건 사이의 가장 작은 간격이 $1/n = 0.001$ 이다. $n$ 이 커질수록 이 해상도가 좋아져 베르누이 방법은 정확한 지수분포 방법과 구별되지 않게 된다. $n$ 이 그리 크지 않으면, 연속인 시간에서라면 "동시"라 할 만큼 가까우면서도 서로 다른 작은 구간에 두 사건이 놓이는 일이 이따금 생긴다.

**지수분포 방법.** 도착간격을 쓰는 방법은 정확하다. 지수분포가 정해 주는 바로 그 시각에 사건을 놓으므로 잘게 나누기에서 오는 군더더기가 없다. 그래서 실제로 푸아송 과정을 모의실험할 때는 이 방법을 즐겨 쓴다.

## 연습문제

**연습문제 1.** 지수분포 도착간격 방법을 써서 $[0, 10]$ 위에 비율이 $\lambda = 3$ 인 푸아송 과정을 모의실험하여라. 사건의 개수와 표본평균 도착간격을 적어라. 이론적인 값은 얼마인가?

??? success "연습문제 1 풀이"
    ```python
    import numpy as np

    np.random.seed(0)
    lam = 3
    T = 10
    interarrivals = np.random.exponential(1 / lam, size=300)
    arrivals = np.cumsum(interarrivals)
    arrivals = arrivals[arrivals < T]
    n_events = len(arrivals)
    mean_interarrival = np.mean(np.diff(np.concatenate([[0], arrivals])))
    print(f"Number of events: {n_events}")
    print(f"Sample mean interarrival time: {mean_interarrival:.4f}")
    ```

    기대되는 사건의 개수는 $E[N(T)] = \lambda T = 30$ 이고 이론적인 평균 도착간격은 $1/\lambda = 1/3 \approx 0.3333$ 이다. 모의실험은 이 값들에 가까운 결과를 낼 것이다.

---

**연습문제 2.** 베르누이 동전 던지기 방법에서 아주 작은 구간마다의 성공확률은 $p = \lambda / n$ 이다. 잘게 나눈 정도 $n$ 이 무엇이든 $[0, T]$ 안에서 기대되는 사건의 개수가 $\lambda T$ 임을 보여라.

??? success "연습문제 2 풀이"
    $[0, T]$ 안의 아주 작은 구간은 $nT$ 개이다. 각각은 성공확률이 $p = \lambda / n$ 인 독립인 베르누이 시행이다. 전체 개수는 $X \sim B(nT, \lambda/n)$ 이므로 다음과 같다.

    $$
    E[X] = nT \cdot \frac{\lambda}{n} = \lambda T
    $$

    이는 모든 $n$ 에서 성립하므로, 잘게 나눈 정도와 상관없이 베르누이 근사가 편향되지 않음을 확인해 준다. $\square$

---

**연습문제 3.** 지수분포 방법을 써서 각 단위구간 $[0,1), [1,2), \ldots, [7,8)$ 안의 사건 개수를 세도록 모의실험을 고쳐라. 모의실험을 10,000번 되풀이하여 표본분포를 푸아송분포의 확률질량함수와 견줌으로써, 각 개수가 $\text{Po}(\lambda)$ 를 따름을 경험적으로 확인하여라.

??? success "연습문제 3 풀이"
    ```python
    import numpy as np
    from scipy.stats import poisson

    np.random.seed(42)
    lam = 1
    T = 8
    num_sims = 10_000
    counts = np.zeros((num_sims, T), dtype=int)

    for sim in range(num_sims):
        interarrivals = np.random.exponential(1 / lam, size=100)
        arrivals = np.cumsum(interarrivals)
        arrivals = arrivals[arrivals < T]
        for a in arrivals:
            idx = int(a)
            if idx < T:
                counts[sim, idx] += 1

    # 첫 번째 구간을 푸아송분포의 확률질량함수와 견준다
    for k in range(6):
        obs_freq = np.mean(counts[:, 0] == k)
        theory = poisson.pmf(k, lam)
        print(f"P(N=={k}): observed={obs_freq:.4f}, theory={theory:.4f}")
    ```

    관찰된 빈도는 각 $k$ 에서 $P(N(1) = k) = e^{-1}/k!$ 에 가깝게 맞아떨어질 것이며, 단위구간 안의 사건 개수가 $\text{Po}(1)$ 을 따름을 확인해 준다.

---

**연습문제 4.** $[0, T]$ 위에서 베르누이 동전 던지기로 센 개수의 분산이 $n \to \infty$ 일 때 $\lambda T$ 로 수렴함을 증명하여라.

??? success "연습문제 4 풀이"
    개수 $X \sim B(nT, \lambda/n)$ 의 분산은 다음과 같다.

    $$
    \text{Var}(X) = nT \cdot \frac{\lambda}{n} \cdot \left(1 - \frac{\lambda}{n}\right) = \lambda T \left(1 - \frac{\lambda}{n}\right)
    $$

    $n \to \infty$ 일 때 다음을 얻는다.

    $$
    \text{Var}(X) \to \lambda T \cdot 1 = \lambda T
    $$

    이는 $\text{Var}(\text{Po}(\lambda T)) = \lambda T$ 와 같으며, 베르누이 근사가 분포뿐 아니라 분산에서도 수렴함을 확인해 준다. $\square$

---

**연습문제 5.** 지수분포 도착간격 방법은 정확한 푸아송 과정을 만들어 내는 반면 베르누이 동전 던지기 방법은 유한한 $n$ 에서 근사에 그치는 까닭을 설명하여라. 어떤 조건에서 이 근사가 정확해지는가?

??? success "연습문제 5 풀이"
    지수분포 방법이 정확한 것은 다음의 동치 정리 때문이다. 어떤 세기 과정이 비율 $\lambda$ 인 푸아송 과정인 것은 도착간격 $T_1, T_2, \ldots$ 이 i.i.d. $\text{Exp}(\lambda)$ 일 때 그리고 오직 그때만이다. `np.random.exponential` 은 정확한 지수분포에서 뽑으므로, 여기에서 얻어지는 도착시각들은 참된 푸아송 과정을 이룬다.

    베르누이 방법은 시간을 길이 $1/n$ 인 구간들로 잘게 나눈다. 각 구간 안에는 사건이 많아야 하나 있을 수 있으므로 두 사건이 $1/n$ 보다 가까이 놓일 수 없다. 유한한 $n$ 에서는 이것이 푸아송 과정의 연속적인 성격을 깨뜨린다. 게다가 각 구간 안의 개수는 푸아송분포가 아니라 베르누이분포를 따르고, 전체 개수도 푸아송분포가 아니라 이항분포 $B(nT, \lambda/n)$ 이다.

    푸아송 극한정리에 따라 $n \to \infty$ 일 때 $B(nT, \lambda/n) \to \text{Po}(\lambda T)$ 이다. 이 근사는 시간을 잘게 나눈 폭이 사라지고 베르누이 시행이 한없이 작아지는 $n \to \infty$ 인 극한에서만 정확해진다.

---

**연습문제 6.** 지수분포 방법으로 $[0, T]$ 위에 비율이 $\lambda$ 인 푸아송 과정을 모의실험한다고 하자. $S_n$ 을 $n$ 번째 도착시각이라 하자. $E[S_n] = n/\lambda$ 와 $\text{Var}(S_n) = n/\lambda^2$ 임을 보여라.

??? success "연습문제 6 풀이"
    $n$ 번째 도착시각은 $S_n = T_1 + T_2 + \cdots + T_n$ 이고, 여기서 $T_i \sim \text{Exp}(\lambda)$ 는 독립이다. 각 도착간격은 $E[T_i] = 1/\lambda$ 와 $\text{Var}(T_i) = 1/\lambda^2$ 을 갖는다.

    기댓값의 선형성에 따라 다음을 얻는다.

    $$
    E[S_n] = \sum_{i=1}^{n} E[T_i] = \frac{n}{\lambda}
    $$

    독립성에 따라 다음을 얻는다.

    $$
    \text{Var}(S_n) = \sum_{i=1}^{n} \text{Var}(T_i) = \frac{n}{\lambda^2}
    $$

    예를 들어 $\lambda = 1$ 이면 다섯 번째 도착은 시각 $E[S_5] = 5$ 에 기대되고 표준편차는 $\sqrt{5} \approx 2.24$ 이다. 다섯 번째 사건이 언제 일어나는지에 꽤 큰 흔들림이 있음을 보여 준다. $\square$
