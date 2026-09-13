# 응용

## 응용 1: 상점에서 쓴 돈의 기댓값

**문제.** 어느 날 백화점에 들어오는 사람의 수는 평균이 50, 분산이 100인 확률변수 $N$ 이다. 손님 한 사람이 쓰는 돈 $X_i$ 는 평균 \$8, 표준편차 \$4 인 i.i.d. 확률변수이다. 손님이 쓰는 돈은 전체 손님 수와 독립이다. 그날 백화점에서 쓰인 돈의 총액 $T$ 의 기댓값을 구하여라.

**문제 설정.** 총지출은 **무작위한 개수의 합**이다.

$$
T = \sum_{i=1}^{N} X_i
$$

**1단계: $E(T \mid N)$ 을 구한다.**

$N$ 으로 조건을 주면 더하는 항의 개수가 고정된다. 조건부기댓값의 선형성과 $X_i$ 가 $N$ 과 독립이라는 사실에 따라 다음을 얻는다.

$$
E(T \mid N) = E\!\left(\sum_{i=1}^{N} X_i \;\middle|\; N\right) = \sum_{i=1}^{N} E(X_i \mid N) = \sum_{i=1}^{N} E(X_i) = 8N
$$

$E(T \mid N) = 8N$ 은 $N$ 의 함수인 확률변수임에 주목하자.

**2단계: 탑 성질을 적용한다.**

$$
E(T) = E\bigl[E(T \mid N)\bigr] = E(8N) = 8 \, E(N) = 8 \times 50 = 400
$$

**3단계: 전분산 법칙으로 $\text{Var}(T)$ 를 구한다.**

먼저 $\text{Var}(T \mid N)$ 은 다음과 같다.

$$
\text{Var}(T \mid N) = \sum_{i=1}^{N} \text{Var}(X_i) = 16N
$$

이제 이브의 법칙을 적용한다.

$$
\text{Var}\bigl(E(T \mid N)\bigr) = \text{Var}(8N) = 64 \, \text{Var}(N) = 64 \times 100 = 6400
$$

$$
E\bigl[\text{Var}(T \mid N)\bigr] = E(16N) = 16 \, E(N) = 16 \times 50 = 800
$$

$$
\text{Var}(T) = 6400 + 800 = 7200
$$

### 무작위 개수의 합에 대한 일반 공식

$X_i$ 가 평균 $\mu$, 분산 $\sigma^2$ 인 i.i.d. 확률변수이고 $N$ 이 $X_i$ 들과 독립일 때 $T = \sum_{i=1}^{N} X_i$ 에 대하여 다음이 성립한다.

$$
E(T) = \mu \, E(N)
$$

$$
\text{Var}(T) = \sigma^2 \, E(N) + \mu^2 \, \text{Var}(N)
$$

---

## 응용 2: 갇힌 광부

**문제.** 어떤 광부가 문이 3개 있는 광산에 갇혔다. 1번 문으로 가면 3시간 뒤에 밖으로 나온다. 2번 문으로 가면 5시간 뒤에 광산으로 되돌아온다. 3번 문으로 가면 7시간 뒤에 광산으로 되돌아온다. 광부는 각 문을 같은 확률 $1/3$ 로 고른다. 밖으로 나오기까지 걸리는 시간의 기댓값 $E(T)$ 를 구하여라.

**문제 설정.** $T$ 를 탈출까지 걸리는 전체 시간, $X$ 를 처음 고른 문이라 하자. 이것은 **첫걸음 분석**이다. 곧 첫걸음에서 무슨 일이 일어나는지로 조건을 준다.

$$
E(T \mid X = x) = \begin{cases}
3 & x = 1 \text{ 일 때} \quad \text{(밖으로 나온다)} \\
5 + E(T) & x = 2 \text{ 일 때} \quad \text{(같은 상황으로 되돌아온다)} \\
7 + E(T) & x = 3 \text{ 일 때} \quad \text{(같은 상황으로 되돌아온다)}
\end{cases}
$$

2번과 3번 문에서 핵심이 되는 통찰은 이렇다. 광산으로 되돌아오고 나면 (설정이 무기억적이므로) 광부는 똑같은 문제를 처음부터 다시 마주하게 되고, 따라서 남은 시간의 기댓값은 다시 $E(T)$ 이다.

**탑 성질을 적용하면:**

$$
E(T) = E\bigl[E(T \mid X)\bigr] = 3 \cdot \tfrac{1}{3} + (5 + E(T)) \cdot \tfrac{1}{3} + (7 + E(T)) \cdot \tfrac{1}{3}
$$

$$
E(T) = \frac{3 + 5 + E(T) + 7 + E(T)}{3} = \frac{15 + 2\,E(T)}{3} = 5 + \tfrac{2}{3}\,E(T)
$$

$$
\tfrac{1}{3}\,E(T) = 5 \implies \boxed{E(T) = 15}
$$

### 갇힌 광부 문제의 분산

**$\text{Var}\bigl(E(T \mid X)\bigr)$:** 조건부기댓값은 $3$, $5 + E(T) = 20$, $7 + E(T) = 22$ 의 값을 각각 확률 $1/3$ 로 갖는다.

$$
\text{Var}\bigl(E(T \mid X)\bigr) = \frac{3^2 + 20^2 + 22^2}{3} - 15^2 = \frac{9 + 400 + 484}{3} - 225 = 297.67 - 225 = 72.67
$$

**$E\bigl[\text{Var}(T \mid X)\bigr]$:** 광부가 밖으로 나오면(1번 문) $\text{Var}(T \mid X = 1) = 0$ 이다(확정된 값이다). 광산으로 되돌아오면 남은 시간의 분산은 $\text{Var}(T)$ 이다.

$$
\text{Var}(T \mid X) = \begin{cases}
0 & \text{확률 } 1/3 \\
\text{Var}(T) & \text{확률 } 1/3 \\
\text{Var}(T) & \text{확률 } 1/3
\end{cases}
$$

$$
E\bigl[\text{Var}(T \mid X)\bigr] = 0 \cdot \tfrac{1}{3} + \text{Var}(T) \cdot \tfrac{1}{3} + \text{Var}(T) \cdot \tfrac{1}{3} = \tfrac{2}{3}\,\text{Var}(T)
$$

**이브의 법칙:**

$$
\text{Var}(T) = 72.67 + \tfrac{2}{3}\,\text{Var}(T)
$$

$$
\tfrac{1}{3}\,\text{Var}(T) = 72.67 \implies \boxed{\text{Var}(T) = 218}
$$

---

## 응용 3: HT 를 기다리는 시간

**문제.** 공정한 동전을 HT 라는 무늬가 나올 때까지 되풀이해 던진다. 던진 횟수를 $W_{HT}$ 라 할 때 $E(W_{HT})$ 와 $\text{Var}(W_{HT})$ 를 구하여라.

**핵심 관찰:** HT 를 기다리는 시간은 **서로 독립인** 기하확률변수들의 합으로 쪼개진다.

$$
W_{HT} = X + Y
$$

여기서 $X$ 는 첫 H 가 나올 때까지 던진 횟수(그 H 자체를 포함한다)이고, $Y$ 는 첫 H 뒤에 T 가 나올 때까지 더 던진 횟수이다. $X$ 와 $Y$ 는 모두 $\text{Geo}(1/2)$ 를 따른다.

그 까닭은 이렇다. 첫 H 앞에 나온 T 들은 모두 "버려진다"(먼저 H 가 있어야 한다). 그리고 H 를 얻은 뒤 더 나오는 H 들도 "버려진다"(무늬를 끝내려면 T 가 필요하다). 첫 H 앞의 T 들은 H 다음에 T 를 얻는 뒤이은 과제에 아무런 영향을 주지 않는다.

**기댓값:**

$$
E(W_{HT}) = E(X) + E(Y) = \frac{1}{1/2} + \frac{1}{1/2} = 2 + 2 = 4
$$

**분산** (독립성을 이용):

$$
\text{Var}(W_{HT}) = \text{Var}(X) + \text{Var}(Y) = \frac{1/2}{(1/2)^2} + \frac{1/2}{(1/2)^2} = 2 + 2 = 4
$$

??? note "첫걸음 분석으로 푸는 다른 풀이"
    가장 최근에 나온 면으로 상태를 정하자. $E_0$ 를 아무것도 없는 상태에서 HT 가 나올 때까지 던지는 횟수의 기댓값, $E_H$ 를 마지막 던지기가 H 였을 때 더 던지는 횟수의 기댓값이라 하자.

    **아무것도 없는 상태에서:** 첫 던지기가 H 이면(상태 H 로 옮겨 간다) 또는 T 이면(T 하나만으로는 HT 로 나아가지 못하므로 처음 그대로이다) 다음이 성립한다.

    $$
    E_0 = 1 + \tfrac{1}{2}\,E_H + \tfrac{1}{2}\,E_0 \implies E_0 = 2 + E_H
    $$

    **상태 H 에서:** 다음 던지기가 T 이면 끝나고(HT 가 완성된다), H 이면 그 새 H 가 다시 HT 의 시작이 될 수 있으므로 상태 H 에 머문다. 따라서 다음이 성립한다.

    $$
    E_H = 1 + \tfrac{1}{2} \cdot 0 + \tfrac{1}{2}\,E_H \implies E_H = 2
    $$

    대입하면 $E_0 = 2 + 2 = 4$ 이다.

    HH 와 견주어 보자. 상태 H 에서 T 가 나오면 HT 는 곧바로 완성되지만(다시 시작하지 않는다) HH 에서는 T 가 나오면 완전히 처음부터 다시 시작해야 한다. 이것이 $E(W_{HT}) = 4 < 6 = E(W_{HH})$ 인 까닭이다.

---

## 응용 4: HH 를 기다리는 시간 — 기댓값

**문제.** 공정한 동전을 HH 라는 무늬가 나올 때까지 던진다. 던진 횟수를 $W_{HH}$ 라 할 때 $E(W_{HH})$ 를 구하여라.

**왜 HH 가 HT 보다 어려운가.** HT 와 달리 HH 라는 무늬는 서로 독립인 조각으로 쪼갤 수 없다. 첫 H 를 얻은 뒤 다음이 T 이면 완전히 처음부터 다시 시작해야 한다. 방금 얻은 H 가 HH 를 이루는 데 아무 쓸모가 없기 때문이다. 여기에서 되풀이되는 구조가 생긴다.

**문제 설정.** $X \sim \text{Geo}(1/2)$ 를 첫 H 가 나올 때까지 던진 횟수라 하자. 그 첫 H 가 나온 뒤($X$ 번째 던지기) 다음 던지기의 결과를 $Y$ 라 하자.

$$
E(W_{HH} \mid Y = y) = \begin{cases}
E(X) + 1 = 3 & y = 1 \text{ 일 때 (H — 무늬가 완성된다)} \\
E(X) + 1 + E(W_{HH}) = 3 + E(W_{HH}) & y = 0 \text{ 일 때 (T — 다시 시작한다)}
\end{cases}
$$

**탑 성질을 적용하면:**

$$
E(W_{HH}) = 3 \cdot \tfrac{1}{2} + (3 + E(W_{HH})) \cdot \tfrac{1}{2} = \frac{3 + 3 + E(W_{HH})}{2} = 3 + \tfrac{1}{2}\,E(W_{HH})
$$

$$
\tfrac{1}{2}\,E(W_{HH}) = 3 \implies \boxed{E(W_{HH}) = 6}
$$

$E(W_{HH}) = 6 > 4 = E(W_{HT})$ 임에 주목하자. 평균적으로 HH 를 기다리는 편이 HT 를 기다리는 것보다 오래 걸린다.

??? note "첫걸음 분석으로 푸는 다른 풀이"
    가장 최근에 나온 면으로 상태를 정하자. $E_0$ 를 아무것도 없는 상태에서 HH 가 나올 때까지 던지는 횟수의 기댓값, $E_H$ 를 마지막 던지기가 H 였을 때 더 던지는 횟수의 기댓값이라 하자.

    **아무것도 없는 상태에서:** 첫 던지기가 H 이면 상태 H 로 옮겨 가고 T 이면 처음 그대로이므로 다음이 성립한다.

    $$
    E_0 = 1 + \tfrac{1}{2}\,E_H + \tfrac{1}{2}\,E_0 \implies E_0 = 2 + E_H
    $$

    **상태 H 에서:** 다음 던지기가 H 이면 끝나고 T 이면 처음부터 다시 시작하므로 다음이 성립한다.

    $$
    E_H = 1 + \tfrac{1}{2} \cdot 0 + \tfrac{1}{2}\,E_0 = 1 + \tfrac{1}{2}\,E_0
    $$

    대입하면 $E_0 = 2 + 1 + \frac{1}{2}E_0 = 3 + \frac{1}{2}E_0$ 이므로 $E_0 = 6$ 이다.

---

## 응용 5: HH 를 기다리는 시간 — 분산

**$\text{Var}\bigl(E(W_{HH} \mid Y)\bigr)$:**

$$
E(W_{HH} \mid Y) = \begin{cases}
3 & \text{확률 } 1/2 \\
3 + E(W_{HH}) = 9 & \text{확률 } 1/2
\end{cases}
$$

$$
\text{Var}\bigl(E(W_{HH} \mid Y)\bigr) = \frac{3^2 + 9^2}{2} - 6^2 = \frac{9 + 81}{2} - 36 = 45 - 36 = 9
$$

**$E\bigl[\text{Var}(W_{HH} \mid Y)\bigr]$:**

$Y = 1$ 이면(성공) $X \sim \text{Geo}(1/2)$ 에 대하여 $W_{HH} = X + 1$ 이므로 $\text{Var}(W_{HH} \mid Y = 1) = \text{Var}(X) = 2$ 이다.

$Y = 0$ 이면(실패) $X$ 와 $W'_{HH}$ 가 독립일 때 $W_{HH} = X + 1 + W'_{HH}$ 이므로 $\text{Var}(W_{HH} \mid Y = 0) = \text{Var}(X) + \text{Var}(W_{HH}) = 2 + \text{Var}(W_{HH})$ 이다.

$$
E\bigl[\text{Var}(W_{HH} \mid Y)\bigr] = 2 \cdot \tfrac{1}{2} + \bigl(2 + \text{Var}(W_{HH})\bigr) \cdot \tfrac{1}{2} = 2 + \tfrac{1}{2}\,\text{Var}(W_{HH})
$$

**이브의 법칙:**

$$
\text{Var}(W_{HH}) = 9 + 2 + \tfrac{1}{2}\,\text{Var}(W_{HH}) = 11 + \tfrac{1}{2}\,\text{Var}(W_{HH})
$$

$$
\tfrac{1}{2}\,\text{Var}(W_{HH}) = 11 \implies \boxed{\text{Var}(W_{HH}) = 22}
$$

---

## 파이썬 모의실험: 기다리는 시간 문제 모음

```python
import numpy as np

np.random.seed(42)
n_sim = 200_000

def simulate_pattern(pattern, n_sim):
    """두 번 던져 이루어지는 무늬를 기다리는 시간을 모의실험한다."""
    results = []
    for _ in range(n_sim):
        flips = []
        count = 0
        while True:
            flip = np.random.randint(0, 2)  # 0=T, 1=H
            flips.append(flip)
            count += 1
            if len(flips) >= 2 and flips[-2] == pattern[0] and flips[-1] == pattern[1]:
                break
        results.append(count)
    return np.array(results)

# HT 와 HH 모의실험
W_HT = simulate_pattern([1, 0], n_sim)
W_HH = simulate_pattern([1, 1], n_sim)

print("=== Waiting Time for HT ===")
print(f"E(W_HT) = {W_HT.mean():.3f}  (theory: 4)")
print(f"Var(W_HT) = {W_HT.var():.3f}  (theory: 4)")

print("\n=== Waiting Time for HH ===")
print(f"E(W_HH) = {W_HH.mean():.3f}  (theory: 6)")
print(f"Var(W_HH) = {W_HH.var():.3f}  (theory: 22)")

# 갇힌 광부 모의실험
miner_times = []
for _ in range(n_sim):
    t = 0
    while True:
        door = np.random.randint(1, 4)
        if door == 1:
            t += 3
            break
        elif door == 2:
            t += 5
        else:
            t += 7
    miner_times.append(t)
miner_times = np.array(miner_times)

print("\n=== Trapped Miner ===")
print(f"E(T) = {miner_times.mean():.2f}  (theory: 15)")
print(f"Var(T) = {miner_times.var():.1f}  (theory: 218)")

# 백화점 모의실험
store_totals = []
for _ in range(n_sim):
    N = int(np.random.normal(50, 10))  # 평균 50, 분산 100
    N = max(N, 0)
    spending = np.random.normal(8, 4, N)  # 평균 8, 표준편차 4
    store_totals.append(spending.sum())
store_totals = np.array(store_totals)

print("\n=== Department Store ===")
print(f"E(T) = {store_totals.mean():.1f}  (theory: 400)")
print(f"Var(T) = {store_totals.var():.0f}  (theory: 7200)")
```

## 연습문제

**연습문제 1.** $N \sim \text{Poisson}(\lambda)$ 이고 $X_i \sim \text{Bernoulli}(p)$ 는 i.i.d. 이며 $N$ 과 독립이라 하자. $S = \sum_{i=1}^{N} X_i$ 라 할 때 탑 성질과 이브의 법칙을 써서 $E(S)$ 와 $\text{Var}(S)$ 를 구하여라.

??? success "연습문제 1 풀이"
    **평균.** 탑 성질에 따라 다음을 얻는다.

    $$
    E[S] = E[E(S \mid N)] = E[N p] = p \lambda
    $$

    **분산.** 이브의 법칙에 따라 다음을 얻는다.

    $$
    \text{Var}(S) = E[\text{Var}(S \mid N)] + \text{Var}(E(S \mid N)) = E[N p(1 - p)] + \text{Var}(N p)
    $$

    $$
    = p(1 - p) \lambda + p^2 \lambda = \lambda p [(1 - p) + p] = \lambda p
    $$

    (실제로 푸아송 솎아내기 정리에 따라 $S \sim \text{Poisson}(\lambda p)$ 이다.)

---

**연습문제 2.** 버스가 0분과 30분 사이의 균등하게 무작위한 시각 $Y$ 에 정류장에 도착한다. 버스가 시각 $Y = y$ 에 도착한다는 조건이 주어지면 승객은 분당 비율 2인 푸아송 과정에 따라 도착한다. 버스가 왔을 때 기다리고 있는 승객의 수를 $N$ 이라 할 때 $E(N)$ 과 $\text{Var}(N)$ 을 구하여라.

??? success "연습문제 2 풀이"
    $Y = y$ 가 주어지면 $N \mid Y = y \sim \text{Poisson}(2y)$ 이므로 $E(N \mid Y) = 2Y$ 이고 $\text{Var}(N \mid Y) = 2Y$ 이다.

    $Y \sim \text{Uniform}(0, 30)$ 은 $E[Y] = 15$ 와 $\text{Var}(Y) = 900/12 = 75$ 를 만족한다.

    **평균.** $E[N] = E[2Y] = 30$ 이다.

    **분산.** 이브의 법칙에 따라 다음을 얻는다.

    $$
    \text{Var}(N) = E[2Y] + \text{Var}(2Y) = 30 + 4 \cdot 75 = 30 + 300 = 330
    $$

---

**연습문제 3.** 어떤 도박꾼이 \$1 을 가지고 시작한다. 매 판마다 확률 $p = 0.4$ 로 \$1 을 따고 확률 $q = 0.6$ 으로 \$1 을 잃는다. 가진 돈이 \$0 이 되거나(파산) \$5 가 되면(승리) 멈춘다. 조건부기댓값을 이용한 첫걸음 분석으로 치르게 되는 판 수의 기댓값을 구하여라.

??? success "연습문제 3 풀이"
    $i = 0, 1, \ldots, 5$ 에 대하여 $\tau_i = E[\text{판 수} \mid i \text{ 에서 시작}]$ 이라 하고 $\tau_0 = \tau_5 = 0$ 이라 하자. 첫걸음 분석에 따라 다음이 성립한다.

    $$
    \tau_i = 1 + p \tau_{i+1} + q \tau_{i-1}, \quad i = 1, 2, 3, 4
    $$

    $p = 0.4$, $q = 0.6$ 이면 이것은 일차연립방정식이다. 수치로 풀면 다음과 같다.

    | $i$ | 1 | 2 | 3 | 4 |
    |---|---|---|---|---|
    | $\tau_i$ | $3.879$ | $6.197$ | $6.697$ | $4.379$ |

    (한 가지 방법: $\tau_1 = 1 + 0.4 \tau_2$, $\tau_2 = 1 + 0.4 \tau_3 + 0.6 \tau_1$ 등 네 개의 방정식을 푼다.)

    \$1 에서 시작하면 치르는 판 수의 기댓값은 $\tau_1 \approx 3.88$ 이다.

---

**연습문제 4.** 어떤 광부가 문이 3개 있는 곳에 갇혔다. 1번 문으로 가면 2시간 뒤에 밖으로 나온다. 2번 문으로 가면 4시간 뒤에 되돌아온다. 3번 문으로 가면 6시간 뒤에 되돌아온다. 광부는 각 문을 같은 확률로 고른다. 첫걸음 분석과 이브의 법칙을 써서 $E(T)$ 와 $\text{Var}(T)$ 를 구하여라.

??? success "연습문제 4 풀이"
    $T$ 를 탈출까지 걸리는 전체 시간이라 하자. 처음 고른 문 $D \in \{1, 2, 3\}$ 으로 조건을 주며 각 확률은 $1/3$ 이다.

    **평균.** $\mu = E[T]$ 라 하자. 첫걸음 분석에 따라 다음이 성립한다.

    $$
    \mu = \tfrac{1}{3}(2) + \tfrac{1}{3}(4 + \mu) + \tfrac{1}{3}(6 + \mu)
    $$

    (문을 고르는 일이 서로 독립이므로 되돌아온 뒤에는 새로운 시행이 시작된다.) 풀면 $\mu = 2/3 + 10/3 + 2 \mu/3$ 이므로 $\mu/3 = 4$ 이고 $\mu = 12$ 이다.

    **분산.** $\sigma^2 = \text{Var}(T)$ 라 하자. $D$ 로 조건을 주면 $T \mid D = 1$ 은 상수이고(분산 0), $T' \overset{d}{=} T$ 에 대하여 $T \mid D = 2$ 는 $4 + T'$ 과 같으므로 $\text{Var}(T \mid D = 2) = \sigma^2$ 이다. 마찬가지로 $\text{Var}(T \mid D = 3) = \sigma^2$ 이다.

    조건부평균은 $E(T \mid D = 1) = 2$, $E(T \mid D = 2) = 4 + 12 = 16$, $E(T \mid D = 3) = 6 + 12 = 18$ 이다. 각각에 $1/3$ 의 가중치를 주어 그 분산을 구하면 다음과 같다.

    $$
    \text{Var}(E(T \mid D)) = E[E(T \mid D)^2] - \mu^2 = \tfrac{1}{3}(4 + 256 + 324) - 144 = \tfrac{584}{3} - 144 = \frac{152}{3}
    $$

    무리 안 분산은 $E[\text{Var}(T \mid D)] = \tfrac{1}{3}(0 + \sigma^2 + \sigma^2) = \tfrac{2 \sigma^2}{3}$ 이다.

    이브의 법칙에 따라 다음을 얻는다.

    $$
    \sigma^2 = \tfrac{2 \sigma^2}{3} + \tfrac{152}{3} \implies \tfrac{\sigma^2}{3} = \tfrac{152}{3} \implies \sigma^2 = 152
    $$

    그러므로 $E[T] = 12$ 시간, $\text{Var}(T) = 152$ 시간$^2$, $\text{SD}(T) \approx 12.33$ 시간이다.

---

**연습문제 5.** 공정한 동전을 되풀이해 던진다. 무늬 HT, HH, TH 각각에 대하여 기다리는 시간의 기댓값과 분산을 구하여라. 이어지는 두 번의 던지기만 놓고 보면 두 글자짜리 무늬 네 가지가 모두 같은 정도로 나타나는데도 왜 $E(W_{HT}) = E(W_{TH})$ 이면서 $E(W_{HH}) > E(W_{HT})$ 인지 설명하여라.

??? success "연습문제 5 풀이"
    공정한 동전에 대하여 (부분적으로 맞은 상태를 상태로 삼는 마르코프 연쇄로) 첫걸음 분석을 하면 다음을 얻는다.

    - $E[W_{HT}] = E[W_{TH}] = 4$ (분산은 $= 4$).
    - $E[W_{HH}] = E[W_{TT}] = 6$ (분산은 $= 22$).

    **HT 와 TH 의 평균이 4인 까닭.** "틀린" 글자가 나와도 부분적인 진전이 남는다. 이를테면 HT 를 기다릴 때 T 가 나오면 다음 H 에서 "H" 라는 조건이 갖추어진다. 더 정확히는, 일단 H 가 나오면 다음 T 까지 평균 2번만 더 던지면 HT 가 완성된다.

    **HH 의 평균이 더 큰 까닭.** H 뒤에 T 가 나오면 연속이 끊겨 HH 를 바랄 수 있기 전에 다시 H 를 기다려야 한다. 실패가 진전을 "지워 버리는" 것이다. 반면 HT 에서는 실패(HH)가 나도 "방금 H 를 보았다"는 상태에 그대로 남아 뒤로 물러서지 않는다. 무늬가 스스로 겹치는 구조가 기다리는 시간을 좌우한다.

---

**연습문제 6.** 공정한 동전 던지기에서 두 글자짜리 무늬 네 가지(HH, HT, TH, TT)를 기다리는 시간을 모두 모의실험하여라. 모의실험으로 얻은 평균과 분산을 이론값과 견주는 표를 만들어라.

??? success "연습문제 6 풀이"
    ```python
    """공정한 동전 던지기에서 두 글자짜리 무늬를 기다리는 시간을 모의실험한다."""
    import random

    # === 한 번의 시행: 정해진 무늬를 기다린다 ===
    def wait_for(pattern: str) -> int:
        prev = ""
        count = 0
        while True:
            flip = random.choice("HT")
            count += 1
            window = (prev + flip)[-2:]
            if window == pattern:
                return count
            prev = flip

    # === 실험 실행 ===
    if __name__ == "__main__":
        n_trials = 100_000
        patterns = ["HH", "HT", "TH", "TT"]
        print(f"{'pattern':>8} {'mean (sim)':>12} {'var (sim)':>12} {'mean (th)':>10} {'var (th)':>10}")
        theory = {"HH": (6, 22), "HT": (4, 4), "TH": (4, 4), "TT": (6, 22)}
        for p in patterns:
            samples = [wait_for(p) for _ in range(n_trials)]
            m = sum(samples) / n_trials
            v = sum((s - m) ** 2 for s in samples) / n_trials
            tm, tv = theory[p]
            print(f"{p:>8} {m:>12.3f} {v:>12.3f} {tm:>10} {tv:>10}")
    ```

    전형적인 출력은 HH 와 TT 의 표본평균이 $\approx 6$, 분산이 $\approx 22$ 이고, HT 와 TH 의 표본평균이 $\approx 4$, 분산이 $\approx 4$ 로 이론과 들어맞는다.
