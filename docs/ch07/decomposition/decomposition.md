# 분해의 예(이항, 음이항, 주사위, 쿠폰 모으기)

## 생각의 뼈대

중요한 확률변수 가운데 많은 것이 더 단순한, 흔히 i.i.d. 인 확률변수들의 합으로 **분해**된다. 이렇게 분해해 두면 합에 대한 공식을 써서 평균과 분산을 손쉽게 구할 수 있다.

$$
S = \sum_{i=1}^n X_i \quad \Longrightarrow \quad E[S] = \sum_{i=1}^n E[X_i], \quad \text{Var}(S) = \sum_{i=1}^n \text{Var}(X_i) \text{ (독립인 경우)}
$$

---

## 예제 1: 베르누이로 보는 이항분포

앞면이 나올 확률이 $p$ 인 동전을 서로 독립으로 $n$ 번 던져 앞면의 수 $S$ 를 센다. $A_i$ 를 $i$ 번째 동전이 앞면으로 떨어지는 사건이라 하고 $\mathbf{1}_{A_i}$ 를 그 지시확률변수라 하자.

$$
\mathbf{1}_{A_i} \stackrel{iid}{\sim} \text{Bernoulli}(p) \quad \Longrightarrow \quad S = \sum_{i=1}^n \mathbf{1}_{A_i} \sim \text{Binomial}(n, p)
$$

$$
E[S] = \sum_{i=1}^n E[\mathbf{1}_{A_i}] = np
$$

$$
\text{Var}(S) = \sum_{i=1}^n \text{Var}(\mathbf{1}_{A_i}) = npq
$$

---

## 예제 2: 기하분포로 보는 음이항분포

앞면이 나올 확률이 $p$ 인 동전을 $r$ 번째 앞면이 나올 때까지 던진다. $X_i$ 를 $(i-1)$ 번째 앞면이 나온 뒤 $i$ 번째 앞면을 얻기까지 던진 횟수라 하자.

$$
X_i \stackrel{iid}{\sim} \text{Geo}(p) \quad \Longrightarrow \quad S = \sum_{i=1}^r X_i \sim \text{NB}(r, p)
$$

$$
E[S] = \sum_{i=1}^r E[X_i] = \frac{r}{p}
$$

$$
\text{Var}(S) = \sum_{i=1}^r \text{Var}(X_i) = \frac{rq}{p^2}
$$

---

## 예제 3: 주사위를 1000번 던지기

주사위를 1000번 던진다. 홀수 눈이 나오면 그 눈만큼 얻고 짝수 눈이 나오면 그 눈만큼 잃는다. 공정하게 만들려고 게임마다 $+0.5$ 의 덤을 얹는다.

$$
D_i = \begin{cases} +1 & \text{확률 } 1/6 \\ -2 & \text{확률 } 1/6 \\ +3 & \text{확률 } 1/6 \\ -4 & \text{확률 } 1/6 \\ +5 & \text{확률 } 1/6 \\ -6 & \text{확률 } 1/6 \end{cases}
$$

$X_i = D_i + 0.5$ 라 하자(i.i.d. 이다). 전체 손익은 $S = \sum_{i=1}^{1000} X_i$ 이다.

**$D_i$ 의 적률**:

$$
E[D_i] = \frac{1 - 2 + 3 - 4 + 5 - 6}{6} = -0.5
$$

$$
E[D_i^2] = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6} \approx 15.1667
$$

$$
\text{Var}(D_i) = 15.1667 - 0.25 = 14.9167
$$

**$X_i = D_i + 0.5$ 의 적률**: $E[X_i] = 0$, $\text{Var}(X_i) = 14.9167$.

**$S$ 의 적률**:

$$
E[S] = 1000 \times 0 = 0
$$

$$
\text{Var}(S) = 1000 \times 14.9167 = 14916.7, \quad \text{SD}(S) \approx 122.1
$$

---

## 예제 4: 쿠폰 모으기 문제

맥도날드 해피밀에 들어 있는 $n$ 가지 장난감을 모두 모으려 한다. 서로 다른 장난감을 $i-1$ 가지 모은 뒤 $i$ 번째 새 장난감을 얻기까지 사야 하는 해피밀의 수를 $\tau_i$ 라 하자. 그러면 다음이 성립한다.

$$
\tau_i \sim \text{Geo}\left(\frac{n - (i-1)}{n}\right), \quad \tau_i \text{ 는 서로 독립}
$$

$$
T_n = \sum_{i=1}^n \tau_i
$$

**평균**:

$$
E[T_n] = \sum_{i=1}^n E[\tau_i] = \sum_{i=1}^n \frac{n}{n - (i-1)} = n\left(1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}\right) = nH_n \sim n\log n
$$

**분산**:

$$
\text{Var}(T_n) = \sum_{k=1}^n \frac{1 - k/n}{(k/n)^2} = n^2 \sum_{k=1}^n \frac{1}{k^2} - n\sum_{k=1}^n \frac{1}{k} \approx \frac{\pi^2}{6}n^2 - n\log n
$$

그러므로 $\text{Var}(T_n) = O(n^2)$ 이다.

---

## 요약 표

| 분포 | 분해 | $E[S]$ | $\text{Var}(S)$ |
|:---:|:---:|:---:|:---:|
| $\text{Binomial}(n,p)$ | $\sum_{i=1}^n \text{Bernoulli}(p)$ | $np$ | $npq$ |
| $\text{NB}(r,p)$ | $\sum_{i=1}^r \text{Geo}(p)$ | $r/p$ | $rq/p^2$ |
| 쿠폰 모으기 | $\sum_{i=1}^n \text{Geo}((n-i+1)/n)$ | $nH_n$ | $\approx \frac{\pi^2}{6}n^2$ |

---

## 파이썬 구현

```python
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 주사위 게임 모의실험
# ============================================================
np.random.seed(42)
NumSimu = 10000
NumRolling = 1000

rolls = np.random.randint(1, 7, size=(NumRolling, NumSimu))
increment = np.where(rolls % 2 == 1, rolls, -rolls).astype(float) + 0.5
Sn = np.cumsum(increment, axis=0)
total_pnl = Sn[-1, :]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].hist(total_pnl, bins=50, edgecolor='black')
axes[0].set_xlabel('Total P&L')
axes[0].set_title('Histogram of Total P&L after 1000 Games')
axes[0].grid(True, alpha=0.3)

axes[1].plot(range(1, NumRolling + 1), Sn[:, 0])
axes[1].set_xlabel('Game number')
axes[1].set_ylabel('Cumulative P&L')
axes[1].set_title('Sample Path of Cumulative P&L')
axes[1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('dice_game_decomposition.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# 쿠폰 모으기 모의실험
# ============================================================
n_toys = 20
N_sim = 50000
T_samples = []
for _ in range(N_sim):
    collected = set()
    count = 0
    while len(collected) < n_toys:
        toy = np.random.randint(0, n_toys)
        collected.add(toy)
        count += 1
    T_samples.append(count)

T_samples = np.array(T_samples)
H_n = sum(1/k for k in range(1, n_toys + 1))
E_Tn = n_toys * H_n
Var_Tn = n_toys**2 * sum(1/k**2 for k in range(1, n_toys + 1)) - n_toys * H_n

print(f"Coupon Collector (n={n_toys}):")
print(f"  Theoretical E[T] = {E_Tn:.2f}, Simulated = {np.mean(T_samples):.2f}")
print(f"  Theoretical SD(T) = {np.sqrt(Var_Tn):.2f}, Simulated = {np.std(T_samples):.2f}")
```

## 연습문제

**연습문제 1.** 음이항분포 $\text{NB}(5, 0.4)$ 는 i.i.d. 인 기하확률변수 5개의 합으로 분해할 수 있다. 이 분해를 써서 평균과 분산을 구하여라.

??? success "연습문제 1 풀이"
    $\text{NB}(r, p) = \sum_{i=1}^{r} G_i$ 이고 각 $G_i \sim \text{Geometric}(p)$ 는 $E[G_i] = 1/p$, $\text{Var}(G_i) = (1 - p)/p^2$ 를 만족한다.

    $r = 5$, $p = 0.4$ 이므로 다음을 얻는다.

    $$
    E[\text{NB}] = \frac{5}{0.4} = 12.5
    $$

    $$
    \text{Var}(\text{NB}) = 5 \cdot \frac{0.6}{0.16} = 5 \cdot 3.75 = 18.75
    $$

---

**연습문제 2.** 수집용 카드가 50종류 있다. 전부 모으려면 몇 팩을 사야 할 것으로 기대되는가? 표준편차는 얼마인가?

??? success "연습문제 2 풀이"
    $n = 50$ 인 쿠폰 모으기 문제이다. 전체 팩 수 $T$ 를 서로 독립인 기하확률변수 50개의 합 $T = \sum_{k=1}^{50} G_k$ 로 분해하자. 여기서 $G_k \sim \text{Geometric}((50 - k + 1)/50)$ 은 이미 $k - 1$ 종류를 모은 뒤 새 종류를 볼 때까지 사야 하는 팩 수이다.

    $$
    E[T] = 50 \sum_{k=1}^{50} \frac{1}{k} = 50 H_{50} \approx 50 \cdot 4.4992 \approx 224.96
    $$

    $$
    \text{Var}(T) = 50^2 \sum_{k=1}^{50} \frac{1}{k^2} - 50 H_{50} \approx 2500 \cdot 1.6251 - 224.96 \approx 3837.8
    $$

    그러므로 $E[T] \approx 225$ 팩이고 $\text{SD}(T) = \sqrt{3837.8} \approx 61.95$ 팩이다.
