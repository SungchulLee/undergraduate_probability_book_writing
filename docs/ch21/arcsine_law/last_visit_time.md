# 마지막 방문 시각

## 정리의 서술

원점에서 시작하여 $\mathbb{Z}$ 위의 단순확률보행 $S_0 = 0, S_1, S_2, \ldots, S_{2n}$ 을 시각 $2n$ 까지 돌린다. $L_{2n}$ 을 **원점으로의 마지막 방문 시각**, 곧 확률보행이 0으로 마지막으로 돌아오는 시각이라고 하자.

그러면 $0 \leq a < b \leq 1$ 에 대하여 다음이 성립한다.

$$
P\!\left(a \leq \frac{L_{2n}}{2n} \leq b\right) \to \int_a^b \frac{1}{\pi} \cdot \frac{1}{\sqrt{x(1-x)}} \, dx = \frac{2}{\pi}\left[\arcsin(\sqrt{b}) - \arcsin(\sqrt{a})\right]
$$

이는 $n \to \infty$ 일 때의 결과이다.

## 아크사인 분포

극한의 밀도

$$
f(x) = \frac{1}{\pi \sqrt{x(1-x)}}, \quad 0 < x < 1
$$

을 **아크사인 분포**라고 부른다. 그 누적분포함수는 다음과 같다.

$$
F(x) = \frac{2}{\pi} \arcsin(\sqrt{x})
$$

이 분포는 $U$ 자 모양이다. 곧 $x = 0$ 과 $x = 1$ 가까이에 확률질량이 가장 많이 놓인다. 이는 확률보행이 0을 마지막으로 방문하는 일이 아주 이른 때나 아주 늦은 때에 일어나기 쉽고 한가운데에서는 그렇지 않다는 뜻이다.

## 직관

아크사인 법칙은 직관에 어긋난다. 확률보행이 시간 내내 0을 "고르게" 오갈 것이라고 여기기 쉽지만 실제로는 그 반대이다. 확률보행은 0의 한쪽에 오래 머무는 경향이 있고, 0에 마지막으로 닿는 시각은 보통 보행의 처음이나 끝 가까이이다.

## 모의실험

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

% 모수
p = 0.5; n = 10000;       % 공정한 동전을 n 번 던진다
NumSimu = 1000;            % 이 실험을 NumSimu 번 한다
x = random('Binomial', 1*ones(NumSimu, n), p*ones(NumSimu, n));
x = 2*x - 1;              % +1/-1 걸음으로 바꾼다

Last_Visit_Time = zeros(NumSimu, 1);
for NumS = 1:NumSimu
    Sn = cumsum(x(NumS, :));
    Random_Walk = [0 Sn];
    Last_Visit_Time(NumS, 1) = find(Random_Walk == 0, 1, 'last') - 1;
end

hist(Last_Visit_Time)
```

**파이썬:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

p = 0.5
n = 10000
num_simu = 1000

# +1/-1 걸음을 만든다
x = 2 * np.random.binomial(1, p, size=(num_simu, n)) - 1

last_visit_time = np.zeros(num_simu)
for s in range(num_simu):
    walk = np.concatenate([[0], np.cumsum(x[s, :])])
    zeros = np.where(walk == 0)[0]
    last_visit_time[s] = zeros[-1]

plt.figure()
plt.hist(last_visit_time, bins=20, edgecolor='black')
plt.xlabel('Last Visit Time to Origin')
plt.ylabel('Frequency')
plt.title(f'Arcsine Law: Last visit time ({num_simu} simulations of {n} steps)')
plt.show()
```

## 관찰

히스토그램은 또렷한 $U$ 자 모양의 분포를 보여 준다. 0으로의 마지막 방문이 양 끝(시각 0과 시각 $n$) 가까이에 몰리고 한가운데에는 상대적으로 적다. 이는 아크사인 밀도와 완전히 들어맞는다.

이는 확률보행에 대한 세 가지 고전적인 아크사인 법칙 가운데 하나이며, 나머지 둘은 양수 쪽에서 보낸 시간의 비율(다음 절을 보아라)과 최댓값에 이르는 시각이다.

## 연습문제

**연습문제 1.** 아크사인 법칙의 극한에서 $P(L_{2n}/(2n) \leq 0.5)$ 를 셈하여라.

??? success "연습문제 1 풀이"
    $$
    P\!\left(\frac{L_{2n}}{2n} \leq 0.5\right) \to \frac{2}{\pi}\arcsin(\sqrt{0.5}) = \frac{2}{\pi} \cdot \frac{\pi}{4} = \frac{1}{2}
    $$

    대칭성에 따라 그 확률은 정확히 $1/2$ 이다.

---

**연습문제 2.** 원점으로의 마지막 방문이 보행의 처음 10% 안에서 일어날 확률, 곧 $P(L_{2n}/(2n) \leq 0.1)$ 을 구하여라.

??? success "연습문제 2 풀이"
    $$
    P\!\left(\frac{L_{2n}}{2n} \leq 0.1\right) \to \frac{2}{\pi}\arcsin(\sqrt{0.1}) = \frac{2}{\pi}\arcsin(0.3162) \approx \frac{2}{\pi} \times 0.3217 \approx 0.2048
    $$

    약 20.5%의 경우에 확률보행이 0으로 마지막으로 돌아오는 일이 처음 10% 안에서 일어난다.

---

**연습문제 3.** 아크사인 밀도는 $0 < x < 1$ 에서 $f(x) = \frac{1}{\pi\sqrt{x(1-x)}}$ 이다. $\int_0^1 f(x)\,dx$ 를 셈하여 이것이 올바른 확률밀도함수임을 확인하여라.

??? success "연습문제 3 풀이"
    $x = \sin^2\theta$, $dx = 2\sin\theta\cos\theta\,d\theta$ 로 바꾸어 놓으면 다음과 같다.

    $$
    \int_0^1 \frac{1}{\pi\sqrt{x(1-x)}}\,dx = \frac{1}{\pi}\int_0^{\pi/2}\frac{2\sin\theta\cos\theta}{\sin\theta\cos\theta}\,d\theta = \frac{1}{\pi}\int_0^{\pi/2}2\,d\theta = \frac{1}{\pi}\cdot\pi = 1
    $$

    $\square$

---

**연습문제 4.** 아크사인 분포가 종 모양이 아니라 U 자 모양(질량이 0과 1 가까이에 몰린 모양)인 까닭을 직관적으로 설명하여라.

??? success "연습문제 4 풀이"
    U 자 모양은 0으로의 마지막 방문이 보행의 아주 이른 때나 아주 늦은 때에 일어나기 쉽고 한가운데에서는 가장 일어나기 어렵다는 뜻이다. 이는 직관에 어긋나지만 확률보행의 근본적인 성질을 드러낸다. 곧 확률보행이 0에서 멀어지면 오랫동안 멀리 머무는 경향이 있다. 일찍 0으로 돌아왔다가 멀리 떠나 버리는 보행은 $L_{2n}/2n$ 이 0 가까이가 되고, 오랫동안 0 언저리에 머물다가 늦게 돌아오는 보행은 $L_{2n}/2n$ 이 1 가까이가 된다. 두 극단 모두 중간 값보다 더 일어나기 쉽다.

---

**연습문제 5.** 아크사인 분포는 잘 알려진 어떤 분포의 특별한 경우인가?

??? success "연습문제 5 풀이"
    아크사인 분포는 $\text{Beta}(1/2, 1/2)$ 이다. 그 확률밀도함수는 다음과 같다.

    $$
    f(x) = \frac{x^{-1/2}(1-x)^{-1/2}}{B(1/2, 1/2)} = \frac{1}{\pi\sqrt{x(1-x)}}
    $$

    $B(1/2, 1/2) = \frac{\Gamma(1/2)^2}{\Gamma(1)} = \pi$ 이기 때문이다.

