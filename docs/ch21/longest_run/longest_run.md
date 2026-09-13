# 동전 던지기에서의 최장 연속

## 문제

공정한 동전을 $n$ 번 던질 때 **최장 연속**, 곧 앞면(또는 뒷면)이 잇달아 나오는 가장 긴 토막의 길이는 어떤 확률분포를 따르는가?

이는 확률에서 고전적인 문제로, 해석적으로 풀기는 어렵지만 모의실험으로 살펴보기는 쉽다.

## 이론적 배경

공정한 동전을 $n$ 번 던질 때 최장 연속의 기대 길이는 대략 다음과 같다.

$$
E[\text{최장 연속}] \approx \log_2 n
$$

더 정확히 말하면 최장 연속 $R_n$ 은 다음을 만족한다.

$$
\frac{R_n}{\log_2 n} \to 1 \quad n \to \infty \text{ 일 때 확률의 뜻으로}
$$

$n = 10{,}000$ 이면 $\log_2(10{,}000) \approx 13.3$ 을 기대하는데, 이는 모의실험 히스토그램이 13–15 언저리에 몰리는 것과 들어맞는다.

## 모의실험

공정한 동전을 $n = 10{,}000$ 번 던지고 최장 연속을 기록한다. 이 실험을 1000번 되풀이해 히스토그램을 만든다.

**MATLAB:**

```matlab
clear all; close all; clc; rng('default')

p = 0.5; n = 10000;       % 공정한 동전을 n 번 던진다
NumSimu = 1000;            % 이 실험을 NumSimu 번 한다
x = random('Binomial', 1*ones(NumSimu, n), p*ones(NumSimu, n));

Run = zeros(NumSimu, 1);
for NumS = 1:NumSimu
    Current_Run = 1;
    Overall_Run = 1;
    for i = 2:n
        if x(NumS, i) == x(NumS, i-1)
            Current_Run = Current_Run + 1;
            Overall_Run = max(Current_Run, Overall_Run);
        else
            Current_Run = 1;
        end
    end
    Run(NumS, 1) = Overall_Run;
end

hist(Run)
```

**파이썬:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

p = 0.5
n = 10000
num_simu = 1000

x = np.random.binomial(1, p, size=(num_simu, n))

runs = np.zeros(num_simu)
for s in range(num_simu):
    current_run = 1
    overall_run = 1
    for i in range(1, n):
        if x[s, i] == x[s, i-1]:
            current_run += 1
            overall_run = max(current_run, overall_run)
        else:
            current_run = 1
    runs[s] = overall_run

plt.figure()
plt.hist(runs, bins=range(int(runs.min()), int(runs.max()) + 2),
         edgecolor='black', align='left')
plt.xlabel('Longest Run Length')
plt.ylabel('Frequency')
plt.title(f'Histogram of longest run in {n} coin flips ({num_simu} simulations)')
plt.show()

print(f"Mean longest run: {runs.mean():.2f}")
print(f"Theoretical approximation (log2 n): {np.log2(n):.2f}")
```

## 관찰

1000번의 모의실험에서 얻은 히스토그램을 보면, 공정한 동전 10,000번 던지기에서 최장 연속은 보통 10과 22 사이에 놓이고 분포는 13–16 언저리에 몰려 있다. 이는 $\log_2 n$ 어림과 놀랄 만큼 잘 들어맞는다.

이 결과는 실제로 뜻하는 바가 있다. 사람들은 무작위 수열에서 연속이 얼마나 길게 나타날 수 있는지를 낮추어 보는 경향이 있고, 그래서 참으로 무작위인 수열이 사람들의 기대보다 덜 무작위해 "보이는" 일이 잦다.

## 연습문제

**연습문제 1.** 공정한 동전 1000번 던지기에서 앞면의 기대 최장 연속을 어림하여라.

??? success "연습문제 1 풀이"
    $$
    E[\text{최장 연속}] \approx \log_2 1000 = \frac{\ln 1000}{\ln 2} \approx \frac{6.908}{0.693} \approx 9.97
    $$

    따라서 앞면이 잇달아 약 **10**번 나오는 것이 보통이다.

---

**연습문제 2.** 어떤 선생님이 학생들에게 동전 던지기 200번의 "무작위" 수열을 적어 보라고 했다. 어떤 학생의 최장 연속이 겨우 3이라면 이는 의심스러운가?

??? success "연습문제 2 풀이"
    200번 던지기에서 기대 최장 연속은 $\log_2 200 \approx 7.6$ 이다. 최장 연속이 겨우 3이라면 기대보다 훨씬 작다. 길이 200의 참으로 무작위인 수열에는 거의 언제나 길이 6 이상의 연속이 들어 있다. 최장 연속이 3이라는 것은 그 수열이 지어낸 것임을 강하게 시사한다(사람들은 너무 자주 바꾸는 경향이 있어 자연스러운 연속 길이를 낮추어 본다).

---

**연습문제 3.** $P(H) = p$ 인 편향된 동전에서 앞면의 기대 최장 연속은 대략 $\frac{-\log n}{\log(1/p)}$ 이다. $n = 1000$, $p = 0.3$ 일 때 이 값을 셈하여라.

??? success "연습문제 3 풀이"
    $$
    E[R_n] \approx \frac{\log 1000}{\log(1/0.3)} = \frac{\ln 1000}{\ln(10/3)} = \frac{6.908}{1.204} \approx 5.74
    $$

    편향된 동전($p = 0.3$)에서는 앞면의 최장 연속이 공정한 동전(약 10)보다 짧아 약 6이다.

---

**연습문제 4.** $P(H) = p$ 인 동전을 $n$ 번 던질 때 앞면의 최장 연속 $R_n$ 에 대하여 합집합 경계를 써서 $P(R_n \geq k) \leq n \cdot p^k$ 임을 증명하여라.

??? success "연습문제 4 풀이"
    $i$ 번째 자리에서 시작하는 길이 $k$ 의 연속이 나올 확률은 $p^k$ 이다. 시작할 수 있는 자리는 많아야 $n - k + 1 \leq n$ 개이다. 합집합 경계에 따라 다음이 성립한다.

    $$
    P(R_n \geq k) \leq n \cdot p^k
    $$

    이 값을 작은 상수 $\alpha$ 와 같다고 두고 풀면 $k \approx \frac{\log(n/\alpha)}{\log(1/p)}$ 를 얻는데, 이는 $p = 1/2$ 일 때의 $\log_2 n$ 눈금과 들어맞는다. $\square$

---

**연습문제 5.** $R_n / \log_2 n \to 1$ 이 확률의 뜻으로 성립하는 까닭, 곧 최장 연속이 선형이 아니라 로그꼴로 자라는 까닭을 직관적으로 설명하여라.

??? success "연습문제 5 풀이"
    길이 $k$ 의 연속이 나오려면 앞면이 $k$ 번 잇달아야 하고 그 확률은 $(1/2)^k$ 이다. 그런 연속이 시작될 기회는 대략 $n$ 번 있다. 길이 $k$ 의 연속이 나타나는 횟수의 기댓값은 대략 $n \cdot 2^{-k}$ 이다. 이 값은 $k = \log_2 n$ 일 때 1이 된다. $k \gg \log_2 n$ 이면 기대 횟수가 하찮아지므로($\to 0$) 그렇게 긴 연속은 거의 나오지 않는다. $k \ll \log_2 n$ 이면 기대 횟수가 크므로 그 길이의 연속은 틀림없이 있다. "거의 확실히 있다"와 "거의 확실히 없다"를 가르는 문턱이 $k \approx \log_2 n$ 이다.
