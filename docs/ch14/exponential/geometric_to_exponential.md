# 기하분포에서 지수분포로의 수렴

기하분포는 지수분포의 이산판이다. 둘 다 저마다의 상황에서 "대기시간"을 나타내는 모형이다. 시간을 점점 더 잘게 쪼개면, 알맞게 눈금을 맞춘 기하확률변수는 지수확률변수로 분포수렴한다. 이 극한정리는 지수분포가 이산적인 베르누이 시행의 연속시간 극한으로 나타난다는 직관을 정확한 말로 다듬어 준다.

## 배경

### 이산적인 대기시간으로서의 기하분포

성공확률이 $p$ 인 베르누이 시행을 독립적으로 되풀이한다고 하자. 첫 성공이 나올 때까지의 시행 횟수(그 성공 시행을 포함한다)를 $G \sim \text{Geom}(p)$ 라 하면 다음이 성립한다.

$$P(G = k) = (1 - p)^{k-1} p, \quad k = 1, 2, 3, \ldots$$

평균과 분산은 $E[G] = 1/p$ 와 $\text{Var}(G) = (1 - p)/p^2$ 이다.

### 시간을 잘게 쪼개기

비율모수 $\lambda > 0$ 을 고정하고, 단위 시간을 길이가 $1/n$ 인 $n$ 개의 작은 구간으로 나누자. 각 작은 구간에서 사건이 일어날 확률은 $p = \lambda / n$ 이다. 첫 사건이 일어날 때까지의 작은 구간의 개수를 $G_n \sim \text{Geom}(\lambda/n)$ 이라 하면, **눈금을 다시 맞춘 대기시간**은 다음과 같다.

$$X_n = \frac{G_n}{n}$$

이것은 첫 사건까지 걸리는 실제 시간(연속적인 단위로 잰 시간)이다.

### 수렴 결과

!!! info "정리: 기하분포에서 지수분포로의 극한"
    $\lambda > 0$ 을 고정하자. $G_n \sim \text{Geom}(\lambda / n)$ 이면 다음이 성립한다.

    $$\frac{G_n}{n} \xrightarrow{d} \text{Exp}(\lambda) \quad \text{as } n \to \infty$$

    곧 눈금을 다시 맞춘 기하확률변수는 지수확률변수로 분포수렴한다.

### 누적분포함수를 이용한 증명

$t \geq 0$ 에서 $X_n = G_n / n$ 의 생존함수는 다음과 같다.

$$P(X_n > t) = P\!\left(G_n > nt\right) = \left(1 - \frac{\lambda}{n}\right)^{\lfloor nt \rfloor}$$

$n \to \infty$ 일 때 다음이 성립한다.

$$\left(1 - \frac{\lambda}{n}\right)^{\lfloor nt \rfloor} \to e^{-\lambda t}$$

$(1 - \lambda/n)^n \to e^{-\lambda}$ 이고 $\lfloor nt \rfloor / n \to t$ 이기 때문이다. 이것은 바로 $\text{Exp}(\lambda)$ 의 생존함수이므로 $X_n \xrightarrow{d} \text{Exp}(\lambda)$ 이다. $\square$

### 적률생성함수를 이용한 증명

$G_n$ 의 적률생성함수는 다음과 같다.

$$M_{G_n}(s) = \frac{p \, e^s}{1 - (1 - p) e^s}, \quad s < -\ln(1-p)$$

여기서 $p = \lambda/n$ 이다. $X_n = G_n / n$ 의 적률생성함수는 $M_{X_n}(s) = M_{G_n}(s/n)$ 이다. 이를 대입하고 $n \to \infty$ 로 보내면 다음을 얻는다.

$$M_{X_n}(s) = \frac{(\lambda/n) \, e^{s/n}}{1 - (1 - \lambda/n) e^{s/n}} \to \frac{\lambda}{\lambda - s}, \quad s < \lambda$$

이것은 $\text{Exp}(\lambda)$ 의 적률생성함수이므로 분포수렴이 확인된다. $\square$

## 코드

```python
"""p = λ/n 일 때 Geometric(p)/n 이 n → ∞ 에서 Exponential(λ) 로 수렴함을 보인다."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

LA = 20
BT = 1 / LA
N = 1000
P = LA / N
N_SIM = 10_000

x_geo = stats.geom(P).rvs(N_SIM) / N
x_exp = stats.expon(scale=BT).rvs(N_SIM)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))

# --- 히스토그램 겹쳐 그리기 ---
ax1.hist(x_geo, bins=100, density=True, alpha=0.3, color="blue", label="Geometric/n")
ax1.hist(x_exp, bins=100, density=True, color="red", histtype="step",
         linewidth=2, label="Exponential")
ax1.set_title("Geometric/n  vs  Exponential")
ax1.legend()
ax1.grid(True, alpha=0.3)

# --- Geometric/n 위에 이론적 확률밀도함수 겹쳐 그리기 ---
_, bins, _ = ax2.hist(x_geo, bins=100, density=True, alpha=0.3, label="Geometric/n")
ax2.plot(bins, stats.expon(scale=BT).pdf(bins), "--r", lw=2, label="Exp PDF")
ax2.set_title(f"Geometric(p={P})/n  →  Exp(λ={LA})")
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.suptitle("Geometric-to-Exponential Convergence", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("geometric_to_exponential.png", dpi=150, bbox_inches="tight")
plt.show()
```

## 실행 결과

이 코드는 두 개의 패널을 나란히 놓은 그림을 만든다.

- **왼쪽 패널**: $G_n / n$ 의 정규화된 히스토그램($\lambda = 20$, $n = 1000$ 이므로 $p = 0.02$)과 진짜 $\text{Exp}(20)$ 표본의 계단 히스토그램을 겹쳐 그린 것이다. 두 분포는 눈으로는 구별되지 않는다.
- **오른쪽 패널**: 같은 $G_n / n$ 히스토그램 위에 이론적인 $\text{Exp}(20)$ 확률밀도함수 곡선 $f(x) = 20 \, e^{-20x}$ 를 겹쳐 그린 것이다. 매끄러운 빨간 곡선이 히스토그램의 윗부분을 거의 그대로 따라간다.

작은 구간을 $n = 1000$ 개로 나눈 것만으로도 기하분포에서 얻은 대기시간은 이미 지수분포에 아주 높은 정확도로 수렴해 있다.

## 뜻풀이

이 모의실험은 기하분포에서 지수분포로 가는 극한에 대해 몇 가지 핵심을 보여 준다.

1. **수렴 속도**: $n = 1000$(따라서 $p = 0.02$)만 되어도 눈금을 다시 맞춘 기하분포는 지수분포와 거의 같다. 근사 $(1 - \lambda/n)^n \approx e^{-\lambda}$ 이 그다지 크지 않은 $n$ 에서도 이미 정확하기 때문에 수렴이 빠르다.

2. **이산과 연속을 잇는 다리**: 기하분포는 이산적인 시행을 센다. 이를 $n$ 으로 나누면 그 개수가 연속적인 시간의 측정값으로 바뀐다. $n \to \infty$ 이면 크기가 $1/n$ 인 이산적인 걸음이 한없이 작아지면서 연속분포가 나온다.

3. **푸아송 과정과의 연결**: 이 극한이 푸아송 과정의 바탕이다. 시간을 너비가 $1/n$ 인 $n$ 개의 칸으로 나누고 각 칸에서 사건이 일어날 확률을 $\lambda/n$ 이라 한 뒤 $n \to \infty$ 로 보내면 연속시간에서의 도착이 된다. 첫 도착까지의 시간은 $\text{Exp}(\lambda)$ 이며, 이는 우리의 극한정리가 말하는 그대로이다.

4. **실제 모형화**: 사건이 이산적인 시간 단계마다 일어나는 상황(예를 들어 네트워크의 시간 칸마다 도착하는 패킷)에서는, 시간 단계가 작고 각 단계의 확률이 $\lambda \cdot \Delta t$ 에 비례할 때 지수분포 근사를 쓰는 것이 정당하다.

## 연습문제

**연습문제 1.**
$p = \lambda / n$ 인 $G \sim \text{Geom}(p)$ 를 생각하자. $E[G/n]$ 과 $\text{Var}(G/n)$ 을 계산하고, $n \to \infty$ 일 때 이들이 $\text{Exp}(\lambda)$ 의 평균과 분산으로 수렴함을 확인하여라.

??? success "연습문제 1 풀이"
    $E[G] = 1/p = n/\lambda$ 이고 $\text{Var}(G) = (1-p)/p^2$ 이므로 다음을 얻는다.

    $$E\!\left[\frac{G}{n}\right] = \frac{1}{np} = \frac{1}{n \cdot \lambda/n} = \frac{1}{\lambda}$$

    $$\text{Var}\!\left(\frac{G}{n}\right) = \frac{1}{n^2} \cdot \frac{1-p}{p^2} = \frac{1 - \lambda/n}{(n \cdot \lambda/n)^2} = \frac{1 - \lambda/n}{\lambda^2}$$

    $n \to \infty$ 이면 다음이 성립한다.

    $$E\!\left[\frac{G}{n}\right] = \frac{1}{\lambda}, \qquad \text{Var}\!\left(\frac{G}{n}\right) \to \frac{1}{\lambda^2}$$

    이는 $X \sim \text{Exp}(\lambda)$ 의 $E[X] = 1/\lambda$ 와 $\text{Var}(X) = 1/\lambda^2$ 에 들어맞는다.

**연습문제 2.**
모의실험 코드를 고쳐 $n = 10, 50, 200, 1000$ 을 쓰고, 눈금을 다시 맞춘 네 기하분포 히스토그램을 같은 축 위에 $\text{Exp}(\lambda)$ 확률밀도함수와 겹쳐 그려라. $n$ 이 커질수록 근사가 어떻게 좋아지는지 설명하여라.

??? success "연습문제 2 풀이"
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats

    np.random.seed(42)
    lam = 20
    n_sim = 10_000
    n_values = [10, 50, 200, 1000]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    for ax, n in zip(axes.flat, n_values):
        p = lam / n
        x_geo = stats.geom(p).rvs(n_sim) / n
        ax.hist(x_geo, bins=80, density=True, alpha=0.4, label=f"Geom/n, n={n}")
        t = np.linspace(0, 0.4, 200)
        ax.plot(t, stats.expon(scale=1/lam).pdf(t), "r-", lw=2, label="Exp PDF")
        ax.set_title(f"n = {n}, p = {p:.4f}")
        ax.legend()
        ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    ```

    $n = 10$ 일 때는 히스토그램이 눈에 띄게 들쭉날쭉하고 이산적이며 계단의 크기가 $0.1$ 이다. $n = 50$ 이면 모양은 분명히 지수분포꼴이지만 이산화의 흔적이 조금 남아 있다. $n = 200$ 과 $n = 1000$ 에서는 히스토그램이 매끄러운 지수분포 확률밀도함수와 사실상 구별되지 않아, 수렴이 빠름을 확인할 수 있다.

**연습문제 3.**
$X_n = G_n / n$ 의 누적분포함수가 모든 $t > 0$ 에서 $\text{Exp}(\lambda)$ 의 누적분포함수로 점별수렴함을 증명하여라. 곧 다음을 보여라.

$$P\!\left(\frac{G_n}{n} \leq t\right) \to 1 - e^{-\lambda t}$$

??? success "연습문제 3 풀이"
    $G_n \sim \text{Geom}(\lambda/n)$ 이므로 다음이 성립한다.

    $$P(G_n \leq k) = 1 - (1 - \lambda/n)^{k}$$

    사건 $G_n / n \leq t$ 는 $G_n \leq nt$ 와 같으므로 다음을 얻는다.

    $$P\!\left(\frac{G_n}{n} \leq t\right) = P(G_n \leq \lfloor nt \rfloor) = 1 - \left(1 - \frac{\lambda}{n}\right)^{\lfloor nt \rfloor}$$

    $0 \leq \{nt\} < 1$ 인 $\{nt\}$ 를 써서 $\lfloor nt \rfloor = nt - \{nt\}$ 로 적으면 다음과 같다.

    $$\left(1 - \frac{\lambda}{n}\right)^{\lfloor nt \rfloor} = \left[\left(1 - \frac{\lambda}{n}\right)^{n}\right]^{t - \{nt\}/n}$$

    $n \to \infty$ 일 때 $(1 - \lambda/n)^n \to e^{-\lambda}$ 이고 $\{nt\}/n \to 0$ 이므로 다음이 성립한다.

    $$\left(1 - \frac{\lambda}{n}\right)^{\lfloor nt \rfloor} \to e^{-\lambda t}$$

    따라서 모든 $t > 0$ 에 대하여 $P(G_n / n \leq t) \to 1 - e^{-\lambda t} = F_{\text{Exp}(\lambda)}(t)$ 이다. $\square$

**연습문제 4.**
기하분포는 무기억성 $P(G > m + k \mid G > m) = P(G > k)$ 를 갖는다. 이 성질이 극한에서도 이어짐을 보여라. 곧 이산판에서 $m = \lfloor ns \rfloor$, $k = \lfloor nt \rfloor$ 로 놓으면 지수분포의 무기억성 $P(X > s + t \mid X > s) = P(X > t)$ 가 따라 나옴을 보여라.

??? success "연습문제 4 풀이"
    $G_n \sim \text{Geom}(\lambda/n)$ 에 대한 이산판 무기억성은 다음과 같다.

    $$P(G_n > m + k \mid G_n > m) = P(G_n > k) = \left(1 - \frac{\lambda}{n}\right)^k$$

    $m = \lfloor ns \rfloor$, $k = \lfloor nt \rfloor$ 로 놓자. 그러면 $G_n > m + k$ 는 $G_n / n > (m+k)/n$ 을 뜻하고, $n \to \infty$ 일 때 다음이 성립한다.

    $$\frac{m + k}{n} = \frac{\lfloor ns \rfloor + \lfloor nt \rfloor}{n} \to s + t$$

    $$\frac{m}{n} = \frac{\lfloor ns \rfloor}{n} \to s, \qquad \frac{k}{n} = \frac{\lfloor nt \rfloor}{n} \to t$$

    따라서 이산판 무기억성은 다음이 된다.

    $$P\!\left(\frac{G_n}{n} > s + t \;\middle|\; \frac{G_n}{n} > s\right) \to P(X > t) = e^{-\lambda t}$$

    극한에서 이것은 바로 연속판 무기억성 $P(X > s + t \mid X > s) = P(X > t)$ 이다. 이렇게 지수분포의 무기억성은 극한을 거쳐 기하분포의 무기억성에서 물려받은 것이다. $\square$

**연습문제 5.**
$\lambda = 20$ 으로 두고 $n = 10, 50, 100, 500, 1000, 5000$ 에 대하여 콜모고로프–스미르노프 통계량 $D_n = \sup_t |F_{X_n}(t) - F_{\text{Exp}}(t)|$ 를 수치적으로 계산하여라. $D_n$ 을 $n$ 에 대해 로그–로그 눈금으로 그리고 수렴 속도를 어림하여라.

??? success "연습문제 5 풀이"
    ```python
    import numpy as np
    from scipy import stats

    lam = 20
    n_values = [10, 50, 100, 500, 1000, 5000]

    for n in n_values:
        p = lam / n
        x_geo = stats.geom(p).rvs(50_000) / n
        ks_stat, _ = stats.kstest(x_geo, "expon", args=(0, 1/lam))
        print(f"n = {n:5d}: D_n = {ks_stat:.6f}")
    ```

    KS 통계량은 $G_n/n$ 의 경험적 누적분포함수와 진짜 $\text{Exp}(\lambda)$ 누적분포함수 사이의 최대 차이를 잰다. 로그–로그 그림에서 $D_n$ 은 대략 $O(1/n)$ 으로 줄어드는데, 이는 누적분포함수의 가장 큰 오차가 이산화 간격 $1/n$ 에서 온다는 사실을 반영한다. 이론적으로도 큰 $n$ 에서 점별 최대 오차는 $\lambda / (2n)$ 으로 눌리며, 이 $O(1/n)$ 속도와 들어맞는다.

**연습문제 6.**
음이항분포에서 감마분포로의 수렴이 기하분포에서 지수분포로의 수렴을 일반화한 것임을 설명하여라. 구체적으로 $Y_n \sim \text{NegBin}(r, \lambda/n)$($r$ 번째 성공까지의 시행 횟수)일 때 $n \to \infty$ 에서 $Y_n / n$ 의 극한을 서술하고 그 까닭을 밝혀라.

??? success "연습문제 6 풀이"
    음이항확률변수 $Y_n \sim \text{NegBin}(r, \lambda/n)$ 은 $r$ 번째 성공까지의 시행 횟수를 센다. 이것은 독립인 기하확률변수 $r$ 개의 합으로 적을 수 있다.

    $$Y_n = G_n^{(1)} + G_n^{(2)} + \cdots + G_n^{(r)}$$

    여기서 각 $G_n^{(i)} \sim \text{Geom}(\lambda/n)$ 이다. 따라서 다음이 성립한다.

    $$\frac{Y_n}{n} = \frac{G_n^{(1)}}{n} + \frac{G_n^{(2)}}{n} + \cdots + \frac{G_n^{(r)}}{n}$$

    각 $G_n^{(i)}/n$ 이 서로 독립으로 $\text{Exp}(\lambda)$ 에 분포수렴하므로, 연속사상정리(또는 같은 말로 합에 대한 적률생성함수의 수렴)에 따라 다음을 얻는다.

    $$\frac{Y_n}{n} \xrightarrow{d} X_1 + X_2 + \cdots + X_r \sim \text{Gamma}(r, \lambda)$$

    여기서 $X_1, \ldots, X_r$ 은 i.i.d. $\text{Exp}(\lambda)$ 이다. 이것이 **음이항분포에서 감마분포로의 극한**이고, 기하분포에서 지수분포로 가는 경우는 $r = 1$ 인 특별한 경우이다.
