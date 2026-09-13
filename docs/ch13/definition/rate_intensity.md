# 비율 모수와 강도

## 비율 모수

푸아송 과정의 정의에 나오는 상수 $\lambda > 0$ 을 **비율 모수**(또는 **강도**)라 한다. 이 값이 사건이 얼마나 자주 일어나는지를 결정한다.

!!! info "비율의 뜻"
    비율이 $\lambda$ 인 푸아송 과정에 대하여 다음이 성립한다.

    - $\lambda$ 는 **단위시간당 기대되는 사건의 개수**이다
    - 길이가 $t$ 인 구간에서 기대되는 사건의 개수는 $\lambda t$ 이다
    - 아주 작은 구간 $(t, t+h]$ 에서 사건이 일어날 확률은 대략 $\lambda h$ 이다

---

## 평균과 분산

$N(t) \sim \text{Po}(\lambda t)$ 이므로 평균과 분산은 푸아송분포의 성질에서 곧바로 따라 나온다.

$$
E[N(t)] = \lambda t
$$

$$
\text{Var}(N(t)) = \lambda t
$$

기대되는 개수는 시간에 비례해 늘어나고 분산도 그러하다. 곧 **표준편차**는 $\sqrt{\lambda t}$ 로 늘어나므로, 상대적인 흔들림 $\text{SD}(N(t))/E[N(t)] = 1/\sqrt{\lambda t}$ 는 관찰하는 시간이 길수록 줄어든다.

---

## 자료에서 비율 되찾기

관찰한 자료가 주어지면 비율을 다음과 같이 어림할 수 있다.

$$
\hat{\lambda} = \frac{\text{전체 사건 개수}}{\text{전체 관찰 시간}} = \frac{N(t)}{t}
$$

큰수의 법칙에 따라 이 추정량은 관찰 시간이 길어질수록 참된 $\lambda$ 로 수렴한다.

---

## 단위와 차원 살피기

비율 $\lambda$ 의 단위는 언제나 **단위시간당 사건 수**이다. 시간의 단위를 정해 두고 한결같이 써야 한다.

| 상황 | 비율 $\lambda$ | 단위 |
|:---|:---|:---|
| 콜센터에 걸려 오는 전화 | 12 | 시간당 통화 수 |
| 방사성 붕괴 | 0.693 | 초당 붕괴 수 |
| 가게에 들어오는 손님 | 2.5 | 분당 손님 수 |
| 어떤 지역의 지진 | 0.3 | 해당 지진 수 |
| 인쇄된 쪽의 오탈자 | 1.2 | 쪽당 오류 수 |

??? example "단위 바꾸기"
    어떤 콜센터에 시간당 $\lambda = 12$ 통의 비율로 전화가 걸려 온다. 이를 다른 단위로 나타내면 다음과 같다.

    - 분당: $\lambda = 12/60 = 0.2$ 통
    - 8시간 근무당: 근무 한 번에 기대되는 전화는 $\lambda \cdot 8 = 96$ 통

    15분 동안의 전화 건수는 $N(0.25) \sim \text{Po}(12 \times 0.25) = \text{Po}(3)$ 이다.

---

## 강도함수(비동차인 경우)

표준적인 푸아송 과정은 비율 $\lambda$ 가 일정하며, 이는 어느 순간에나 사건이 같은 정도로 일어날 수 있다는 뜻이다. 그런데 실제로는 비율이 시간에 따라 달라지는 현상도 많다.

**비동차 푸아송 과정**은 상수 $\lambda$ 를 시간에 따라 달라지는 **강도함수** $\lambda(t)$ 로 바꾼 것이다. 이때 $(s, s+t]$ 안의 사건 개수는 다음을 따른다.

$$
N(s, s+t) \sim \text{Po}\!\left(\int_s^{s+t} \lambda(u)\, du\right)
$$

증분은 여전히 독립이지만 더는 정상이 아니다. 분포가 구간이 언제 시작하는지에 기대기 때문이다. 이 장에서는 동차인 경우($\lambda$ 가 상수)를 다룬다. 비동차로 넓힌 경우는 빠짐없이 짚기 위해 언급해 두며, 더 깊은 과목에서 다루어진다.

---

## 정리하며

비율 모수 $\lambda$ 는 푸아송 과정 전체를 다스리는 하나뿐인 모수이다. 이 값이 기대되는 사건 개수($\lambda t$), 분산($\lambda t$), 사건 사이의 평균 기다림 시간(14장에서 볼 $1/\lambda$), 그리고 어떤 구간에서든 사건이 일어날 확률을 모두 결정한다. $\lambda$ 와 시간 변수의 단위가 서로 들어맞는지 언제나 살펴보아야 한다.

## 연습문제

**연습문제 1.**
**(a)** 조건부 균등 방법을 써서 $[0, 10]$ 위에 $\lambda = 5$ 인 푸아송 과정을 만들어 내는 파이썬 모의실험을 작성하여라. 먼저 $N \sim \text{Po}(50)$ 을 뽑고, 그다음 i.i.d. $\text{Uniform}(0, 10)$ 값을 $N$ 개 만들어 정렬하면 된다.

**(b)** 지수분포를 따르는 도착간격을 써서 같은 일을 되풀이하여라. 두 방법의 표본 경로를 그려 견주어 보아라.

**(c)** 10,000번 되풀이하여 $[0, 2]$ 안의 개수가 평균 $\approx 10$, 분산 $\approx 10$ 임을 경험적으로 확인하여라.

??? success "연습문제 1 풀이"

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    np.random.seed(42)
    lam = 5
    T = 10

    # (a) 조건부 균등 방법
    N = np.random.poisson(lam * T)
    arrivals_uniform = np.sort(np.random.uniform(0, T, N))

    # (b) 지수분포 도착간격 방법
    interarrivals = np.random.exponential(1 / lam, size=200)
    arrivals_exp = np.cumsum(interarrivals)
    arrivals_exp = arrivals_exp[arrivals_exp < T]

    fig, axes = plt.subplots(2, 1, figsize=(12, 4))
    axes[0].step(arrivals_uniform,
                 np.arange(1, len(arrivals_uniform) + 1),
                 where='post', label='Uniform method')
    axes[0].set_ylabel('N(t)')
    axes[0].legend()

    axes[1].step(arrivals_exp,
                 np.arange(1, len(arrivals_exp) + 1),
                 where='post', color='orange',
                 label='Exponential method')
    axes[1].set_xlabel('t')
    axes[1].set_ylabel('N(t)')
    axes[1].legend()
    plt.tight_layout()
    plt.show()

    # (c) 평균과 분산 확인하기
    n_rep = 10_000
    counts = np.random.poisson(lam * 2, n_rep)
    print(f"Mean of N(0,2): {counts.mean():.3f} (theory: 10)")
    print(f"Var of N(0,2):  {counts.var(ddof=1):.3f} (theory: 10)")
    ```
