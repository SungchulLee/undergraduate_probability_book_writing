# 양수 구간의 개수

## 정리의 서술

원점에서 시작하여 $\mathbb{Z}$ 위의 단순확률보행 $S_0 = 0, S_1, S_2, \ldots, S_{2n}$ 을 시각 $2n$ 까지 돌린다. **구간**이란 선분 $(k-1, S_{k-1}) \to (k, S_k)$ 를 말한다. 구간의 한가운데가 $x$ 축 위에 있으면, 곧 다음이 성립하면 그 구간을 **양수 구간**이라고 한다.

$$
\frac{S_{k-1} + S_k}{2} > 0
$$

$N_{2n}$ 을 양수 구간의 개수라고 하자. 그러면 $0 \leq a < b \leq 1$ 에 대하여 다음이 성립한다.

$$
P\!\left(a \leq \frac{N_{2n}}{2n} \leq b\right) \to \int_a^b \frac{1}{\pi} \cdot \frac{1}{\sqrt{x(1-x)}} \, dx = \frac{2}{\pi}\left[\arcsin(\sqrt{b}) - \arcsin(\sqrt{a})\right]
$$

## 뜻풀이

확률보행이 양수 쪽에서 보내는 시간의 비율은 마지막 방문 시각과 똑같은 아크사인 분포를 따른다. 이는 다음을 뜻한다.

- 확률보행은 시간의 절반쯤을 0 위에서, 나머지 절반쯤을 0 아래에서 보내지 **않는다**.
- 오히려 거의 모든 시간을 한쪽에서만 보내기 쉽다.
- 양수 쪽에서 정확히 50%의 시간을 보내는 것이 사실은 *가장 일어나기 어려운* 결과이다.

## 모의실험

**MATLAB:**

```matlab
%% 양수 구간의 개수
clear all; close all; clc; rng('default')

% 모수
p = 0.5; n = 10000;       % 공정한 동전을 n 번 던진다
NumSimu = 1000;            % 이 실험을 NumSimu 번 한다
x = random('Binomial', 1*ones(NumSimu, n), p*ones(NumSimu, n));
x = 2*x - 1;

Number_of_Positive_Sticks = zeros(NumSimu, 1);
for NumS = 1:NumSimu
    Sn = cumsum(x(NumS, :));
    Random_Walk = [0 Sn];
    Center_of_Stick = (Random_Walk(1:end-1) + Random_Walk(2:end)) / 2;
    Positive_Side_Sticks = find(Center_of_Stick > 0);
    Number_of_Positive_Sticks(NumS, 1) = length(Positive_Side_Sticks);
end

hist(Number_of_Positive_Sticks)
```

**파이썬:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

p = 0.5
n = 10000
num_simu = 1000

x = 2 * np.random.binomial(1, p, size=(num_simu, n)) - 1

num_positive_sticks = np.zeros(num_simu)
for s in range(num_simu):
    walk = np.concatenate([[0], np.cumsum(x[s, :])])
    centers = (walk[:-1] + walk[1:]) / 2
    num_positive_sticks[s] = np.sum(centers > 0)

plt.figure()
plt.hist(num_positive_sticks, bins=20, edgecolor='black')
plt.xlabel('Number of Positive Sticks')
plt.ylabel('Frequency')
plt.title(f'Arcsine Law: Positive sticks ({num_simu} simulations of {n} steps)')
plt.show()
```

## 관찰

히스토그램은 이번에도 아크사인 분포 특유의 $U$ 자 모양을 보여 준다. 확률보행은 시간을 반반으로 가르기보다 거의 내내 양수 쪽에 있거나 거의 내내 음수 쪽에 있는 경향이 있다.

## 세 가지 아크사인 법칙

대칭 확률보행에 대한 고전적인 아크사인 법칙은 다음 세 양이 모두 같은 아크사인 분포를 따른다고 말한다.

1. **마지막 방문 시각** $L_{2n}/(2n)$ — 확률보행이 0으로 마지막으로 돌아오는 시각
2. **양수 쪽에서 보낸 시간의 비율** $N_{2n}/(2n)$ — 0 위에 있는 구간의 비율
3. **최댓값에 이르는 시각** — 확률보행이 최댓값에 다다르는 시각

폴 레비가 밝힌 이 결과들은 확률론에서 가장 아름답고 놀라운 것들에 속한다.

## 연습문제

**연습문제 1.** 100걸음짜리 확률보행에서 평균적으로 보행이 양수 쪽에서 보내는 시간의 비율은 대략 얼마인가?

??? success "연습문제 1 풀이"
    $N_{2n}/(2n)$ 이 아크사인 분포(Beta$(1/2, 1/2)$)로 수렴하므로 양수 구간 비율의 기댓값은 다음과 같다.

    $$
    E\!\left[\frac{N_{2n}}{2n}\right] \to E[\text{Beta}(1/2, 1/2)] = \frac{1/2}{1/2 + 1/2} = \frac{1}{2}
    $$

    평균적으로 확률보행은 시간의 절반을 양수 쪽에서, 절반을 음수 쪽에서 보낸다.

---

**연습문제 2.** 확률보행이 시간의 90%를 넘게 양수 쪽에서 보낼 확률은 얼마인가?

??? success "연습문제 2 풀이"
    $$
    P\!\left(\frac{N_{2n}}{2n} > 0.9\right) \to 1 - \frac{2}{\pi}\arcsin(\sqrt{0.9}) = 1 - \frac{2}{\pi}\arcsin(0.9487) \approx 1 - \frac{2}{\pi}(1.2490) \approx 1 - 0.795 = 0.205
    $$

    약 20.5%이다. 놀랄 만큼 높다.

---

**연습문제 3.** 아크사인 법칙에 따라 마지막 방문 시각과 양수 구간에 대하여 $P(N_{2n}/(2n) \leq x)$ 가 같음을 보여라. 이것이 왜 놀라운가?

??? success "연습문제 3 풀이"
    $L_{2n}/(2n)$ 과 $N_{2n}/(2n)$ 은 모두 같은 아크사인 분포 $\text{Beta}(1/2, 1/2)$ 로 수렴한다. 이는 놀라운 일인데, 마지막 방문 시각과 양수 쪽에서 보낸 시간의 비율은 확률보행의 아주 다른 면을 재기 때문이다. 앞의 것은 시각 하나이고, 뒤의 것은 모든 걸음에 걸친 합이다. 그런데도 둘이 같은 극한분포를 나누어 가지며, 이는 대칭 확률보행의 깊은 구조적 성질을 드러낸다.

---

**연습문제 4.** $P(\text{위로}) = p > 1/2$ 인 편향된 확률보행에서도 양수 쪽에서 보내는 시간의 비율이 아크사인 법칙을 따르리라고 보는가?

??? success "연습문제 4 풀이"
    **아니다.** 아크사인 법칙은 보행의 대칭성($p = 1/2$)에 기댄다. $p > 1/2$ 이면 보행이 위로 흐르므로 양수 쪽에서 보내는 시간의 비율은 1로 수렴한다(강법칙에 따라 $S_n/n \to p - (1-p) > 0$). 극한분포는 아크사인 분포가 아니라 1에 놓인 점질량으로 퇴화한다.

---

**연습문제 5.** (생각으로) 모의실험하여 확인하여라. 길이 1000인 대칭 확률보행 10,000개 가운데 구간의 80%를 넘게 양수로 가지는 보행의 비율은 얼마인가?

??? success "연습문제 5 풀이"
    아크사인 법칙의 근사를 쓰면 다음과 같다.

    $$
    P\!\left(\frac{N_{1000}}{1000} > 0.8\right) \approx 1 - \frac{2}{\pi}\arcsin(\sqrt{0.8}) = 1 - \frac{2}{\pi}\arcsin(0.8944) \approx 1 - \frac{2}{\pi}(1.1071) \approx 0.295
    $$

    10,000개 보행 가운데 약 29.5%, 곧 대략 2,950개가 양수 구간을 80% 넘게 가질 것이다.
