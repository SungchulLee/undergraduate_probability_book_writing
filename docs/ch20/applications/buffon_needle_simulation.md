# 뷔퐁의 바늘 모의실험

이 모의실험은 뷔퐁의 바늘 실험으로 $\pi$ 를 어림한다. 한 단위 간격으로 그은 평행선 위에 길이 1인 바늘을 되풀이해 떨어뜨리고 선을 가로지른 비율을 따라가면, 큰수의 법칙이 그 어림값이 $\pi$ 의 참값으로 수렴함을 보장한다.

## 배경

뷔퐁의 바늘 문제에서는 평행한 가로줄을 한 단위 간격으로 긋고 길이 1인 바늘을 무작위로 떨어뜨린다. 바늘의 위치는 두 확률변수로 정해진다.

- $Y \sim \text{Uniform}(0, 1)$: 바늘 아래쪽 끝의 높이.
- $\Theta \sim \text{Uniform}(0, \pi)$: 바늘이 가로 방향과 이루는 각.

바늘 위쪽 끝의 높이는 $Y + \sin\Theta$ 이다. 바늘이 (높이 1에 있는) 선을 가로지를 필요충분조건은 $Y + \sin\Theta \geq 1$ 이다. 가로지를 확률은 다음과 같다.

$$
p = P(Y + \sin\Theta \geq 1) = \frac{1}{\pi}\int_0^{\pi} \sin\theta\, d\theta = \frac{2}{\pi}
$$

$i$ 번째 떨어뜨림에서 가로지름을 나타내는 지시확률변수를 다음과 같이 정의하자.

$$
R_i = \mathbf{1}(Y_i + \sin\Theta_i \geq 1)
$$

$R_i$ 들은 i.i.d. 베르누이$(2/\pi)$ 확률변수이다. 큰수의 강법칙에 따라 다음이 성립한다.

$$
\frac{1}{n}\sum_{i=1}^n R_i \xrightarrow{a.s.} \frac{2}{\pi}
$$

이를 고쳐 쓰면 추정량을 얻는다.

$$
\hat{\pi}_n = \frac{2n}{\sum_{i=1}^n R_i} \xrightarrow{a.s.} \pi
$$

이 수렴은 $x = 2/\pi$ 에서 연속인 $g(x) = 2/x$ 에 연속사상정리를 적용해 얻는다.

## 코드

```python
"""뷔퐁의 바늘: 평행선 위에 바늘을 떨어뜨려 π 를 어림한다."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n = 10_000
x = np.random.uniform(0, 1, (n, 2))  # 0열 = 중심 높이, 1열 = 각/π
h = x[:, 0] + np.sin(np.pi * x[:, 1])  # 위쪽 끝의 높이
crosses = (h >= 1).astype(int)

N_cum = crosses.cumsum()
idx = np.arange(1, n + 1)
pi_est = 2 * idx / np.maximum(N_cum, 1)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(pi_est[10:], linewidth=1.5, label="Estimate of π")
ax.axhline(np.pi, color="r", linestyle="--", lw=2, label=f"π ≈ {np.pi:.5f}")
ax.set_title("Buffon's Needle: Estimating π", fontsize=14)
ax.set_xlabel("Number of needles")
ax.set_ylabel("Estimated π")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("buffon_needle.png", dpi=150, bbox_inches="tight")
plt.show()

print(f"Final estimate of π (n = {n:,}): {pi_est[-1]:.5f}")
```

## 실행 결과

이 스크립트는 수렴 그림 하나와 출력된 어림값 하나를 내놓는다.

**수렴 그림:** 그때까지의 어림값 $\hat{\pi}_n = 2n / \sum_{i=1}^n R_i$ 을 $n$ 이 10에서 10,000까지 갈 때 그린 것이다. 빨간 점선 가로줄은 $\pi \approx 3.14159$ 를 나타낸다. $n$ 이 작을 때에는(특히 가로지름이 몇 번 일어나지 않았을 때) 크게 출렁이다가, $n$ 이 커지면서 $\pi$ 쪽으로 차츰 수렴한다.

**출력된 값:** `Final estimate of π (n = 10,000): 3.12964` (정확한 값은 씨앗값에 따라 달라진다).

## 뜻풀이

1. **큰수의 법칙에 따른 수렴.** 이 그림은 큰수의 강법칙을 그대로 눈으로 보여 준다. 가로지른 비율 $\bar{R}_n = \frac{1}{n}\sum R_i$ 이 $2/\pi$ 로 수렴하므로 역수를 쓴 추정량 $\hat{\pi}_n = 2/\bar{R}_n$ 이 $\pi$ 로 수렴한다. $n$ 이 커지면서 출렁임이 잦아드는데, 이는 분산이 $1/n$ 의 속도로 줄어드는 것과 들어맞는다.

2. **몬테카를로와 견주어 보기.** 뷔퐁의 바늘과 사분원 몬테카를로 방법은 둘 다 큰수의 법칙으로 $\pi$ 를 어림하지만 기하학적 설정이 다르다. 뷔퐁 방법의 분산은 다음과 같다.

    $$
    \operatorname{Var}(\bar{R}_n) = \frac{p(1-p)}{n} = \frac{(2/\pi)(1 - 2/\pi)}{n} \approx \frac{0.2313}{n}
    $$

    그런데 추정량 $\hat{\pi}_n = 2/\bar{R}_n$ 은 $\bar{R}_n$ 의 비선형 변환이므로 (델타 방법으로 구한) 그 분산은 대략 다음과 같다.

    $$
    \operatorname{Var}(\hat{\pi}_n) \approx \left(\frac{d}{dp}\frac{2}{p}\right)^2 \operatorname{Var}(\bar{R}_n) = \frac{4}{p^4}\cdot\frac{p(1-p)}{n} = \frac{4(1-p)}{p^3 n} \approx \frac{5.63}{n}
    $$

    이는 사분원을 직접 쓰는 추정량의 분산($\approx 2.70/n$)의 약 두 배이므로 뷔퐁의 바늘이 조금 덜 효율적이다.

3. **처음의 불안정함.** $n$ 이 아주 작을 때에는 가로지름이 몇 번 없거나 아예 없어서 어림값이 들쭉날쭉할 수 있다. 코드에서는 `np.maximum(N_cum, 1)` 로 0으로 나누는 일을 막지만, 처음 몇십 번의 떨어뜨림에서 나온 어림값은 믿을 것이 못 된다.

4. **역사적 뜻.** 뷔퐁의 바늘(1777)은 기하와 확률을 이은 가장 이른 예 가운데 하나이다. 큰수의 법칙이 엄밀하게 서술되기도 전에 나왔으며, 오늘날의 몬테카를로 방법의 앞선 모습이다.

## 연습문제

**연습문제 1.** 바늘 $n = 100{,}000$ 개로 모의실험을 돌려 보아라. $\pi$ 의 마지막 어림값을 보고하고 $n = 10{,}000$ 일 때와 견주어 수렴 그림이 어떻게 달라지는지 설명하여라.

??? success "연습문제 1 풀이"
    `n = 100_000` 으로 바꾼다. 보통 한 번 돌리면 $\hat{\pi} \approx 3.1420$ 이 나온다. 수렴 그림에서는 $n$ 이 클 때 출렁임이 눈에 띄게 작아지면서 어림값이 $\pi$ 에 더 가까이 자리 잡는다. 추정량의 표준편차는 $n = 10{,}000$ 일 때보다 $\sqrt{10} \approx 3.16$ 배 줄어들므로 어림값이 약 3배 더 정밀해진다. $\square$

---

**연습문제 2.** 이중적분

$$
p = \int_0^{\pi}\int_0^1 \mathbf{1}(y + \sin\theta \geq 1)\, dy\, \frac{d\theta}{\pi}
$$

을 셈하여 가로지를 확률 $p = 2/\pi$ 를 유도하여라.

??? success "연습문제 2 풀이"
    $\theta \in (0, \pi)$ 를 고정하면 $y$ 에 대한 안쪽 적분은 다음과 같다.

    $$
    \int_0^1 \mathbf{1}(y + \sin\theta \geq 1)\, dy = \int_0^1 \mathbf{1}(y \geq 1 - \sin\theta)\, dy
    $$

    $\theta \in (0, \pi)$ 이면 $\sin\theta \in (0, 1]$ 이므로 $1 - \sin\theta \in [0, 1)$ 이다. 이 적분은 다음과 같다.

    $$
    \int_{\max(0,\, 1-\sin\theta)}^1 dy = 1 - (1 - \sin\theta) = \sin\theta
    $$

    ($\sin\theta \geq 1$ 일 때, 곧 $\theta = \pi/2$ 일 때에는 아래끝이 0이고 적분값이 1이지만 $\sin(\pi/2) = 1$ 이므로 이 식이 그대로 성립한다.)

    이제 $\theta$ 에 대하여 적분한다.

    $$
    p = \frac{1}{\pi}\int_0^{\pi}\sin\theta\, d\theta = \frac{1}{\pi}\left[-\cos\theta\right]_0^{\pi} = \frac{1}{\pi}(1 - (-1)) = \frac{2}{\pi}
    $$

    $\square$

---

**연습문제 3.** 간격이 $d$ 인 줄 위에 길이 $\ell$ 인 바늘을 떨어뜨릴 때($\ell \leq d$) 가로지를 확률이 $2\ell/(\pi d)$ 임을 보여라. 이 일반적인 경우를 모의실험하려면 코드를 어떻게 고쳐야 하는가?

??? success "연습문제 3 풀이"
    간격이 $d$ 이고 바늘 길이가 $\ell \leq d$ 일 때, 아래쪽 끝의 높이를 $Y \sim \text{Uniform}(0, d)$, 각을 $\Theta \sim \text{Uniform}(0, \pi)$ 라고 하자. 바늘이 선을 가로지를 조건은 $Y + \ell\sin\Theta \geq d$ 이다. 같은 셈을 따라가면 다음을 얻는다.

    $$
    p = \frac{1}{\pi d}\int_0^{\pi}\ell\sin\theta\, d\theta = \frac{\ell}{\pi d}\left[-\cos\theta\right]_0^{\pi} = \frac{2\ell}{\pi d}
    $$

    코드는 해당 줄들을 다음과 같이 바꾸면 된다.

    ```python
    ell = 0.5   # 바늘의 길이
    d = 1.0     # 줄 사이의 간격
    x = np.random.uniform(0, 1, (n, 2))
    h = d * x[:, 0] + ell * np.sin(np.pi * x[:, 1])
    crosses = (h >= d).astype(int)
    pi_est = 2 * ell * idx / (d * np.maximum(N_cum, 1))
    ```

    추정량은 $\hat{\pi}_n = 2\ell n / (d \sum R_i)$ 이 된다. $\square$

---

**연습문제 4.** $\bar{R}_n = \frac{1}{n}\sum_{i=1}^n R_i$ 일 때 델타 방법을 써서 $\hat{\pi}_n = 2/\bar{R}_n$ 의 근사 분산을 유도하여라.

??? success "연습문제 4 풀이"
    $g(x) = 2/x$ 라고 하면 $\hat{\pi}_n = g(\bar{R}_n)$ 이다. $g'(x) = -2/x^2$ 이다. 델타 방법에 따라 $n$ 이 크면 다음이 성립한다.

    $$
    \operatorname{Var}(g(\bar{R}_n)) \approx [g'(p)]^2 \operatorname{Var}(\bar{R}_n)
    $$

    $p = 2/\pi$ 이고 $\operatorname{Var}(\bar{R}_n) = p(1-p)/n$ 이므로 다음과 같다.

    $$
    [g'(p)]^2 = \left(\frac{-2}{p^2}\right)^2 = \frac{4}{p^4}
    $$

    $$
    \operatorname{Var}(\hat{\pi}_n) \approx \frac{4}{p^4}\cdot\frac{p(1-p)}{n} = \frac{4(1-p)}{p^3 n}
    $$

    $p = 2/\pi$ 를 넣으면 다음을 얻는다.

    $$
    \operatorname{Var}(\hat{\pi}_n) \approx \frac{4(1-2/\pi)}{(2/\pi)^3 n} = \frac{4 \cdot 0.3634}{(0.6366)^3 n} = \frac{1.4536}{0.2579 n} \approx \frac{5.636}{n}
    $$

    $n = 10{,}000$ 이면 $\text{SD}(\hat{\pi}_n) \approx \sqrt{5.636/10000} \approx 0.0237$ 이다. $\square$

---

**연습문제 5.** 코드에서 `np.maximum(N_cum, 1)` 이 하는 일을 설명하여라. 이것이 없다면 어떤 일이 벌어지는가?

??? success "연습문제 5 풀이"
    추정량 $\hat{\pi}_n = 2n / \sum_{i=1}^n R_i$ 은 그때까지 가로지른 횟수로 나누는 일을 담고 있다. 처음 몇 번의 떨어뜨림에서는 아직 가로지름이 한 번도 일어나지 않았을 수 있다($\sum R_i = 0$). `np.maximum(N_cum, 1)` 이 없으면 0으로 나누게 되어 `inf` 나 `nan` 이 나온다.

    `N_cum` 을 `np.maximum(N_cum, 1)` 로 바꾸면 분모가 적어도 1이 되도록 보장한다. 그래서 처음 몇 번에 대해서도 (정확하지는 않지만) 유한한 어림값을 준다. 가로지름이 한 번이라도 일어나면 `np.maximum(N_cum, 1) = N_cum` 이 되어 이 장치는 아무 영향을 주지 않는다.

    $n$ 번 떨어뜨린 뒤에도 가로지름이 한 번도 없을 확률은 $(1 - 2/\pi)^n$ 으로 지수적으로 줄어든다. 열 번만 떨어뜨려도 그 확률이 대략 $(0.3634)^{10} \approx 4 \times 10^{-5}$ 이므로, 이 문제는 맨 처음 몇 개의 바늘에서만 뜻이 있다. $\square$

---

**연습문제 6.** $\pi$ 를 어림할 때 뷔퐁의 바늘과 사분원 몬테카를로 방법의 효율을 견주어 보아라. 같은 정확도를 얻는 데 표본이 더 적게 드는 쪽은 어느 것이며 그 까닭은 무엇인가?

??? success "연습문제 6 풀이"
    사분원 몬테카를로 추정량 $\hat{\pi}_n^{\text{MC}} = \frac{4}{n}\sum I_i$ 의 분산은 다음과 같다.

    $$
    \operatorname{Var}(\hat{\pi}_n^{\text{MC}}) = \frac{\pi(4-\pi)}{n} \approx \frac{2.698}{n}
    $$

    뷔퐁의 바늘 추정량 $\hat{\pi}_n^{\text{B}} = 2/\bar{R}_n$ 의 (델타 방법으로 구한) 근사 분산은 다음과 같다.

    $$
    \operatorname{Var}(\hat{\pi}_n^{\text{B}}) \approx \frac{5.636}{n}
    $$

    그 비는 $5.636 / 2.698 \approx 2.09$ 이므로 뷔퐁 추정량의 분산이 약 두 배이다. 같은 정밀도를 얻으려면 뷔퐁의 바늘은 대략 두 배 더 많이 떨어뜨려야 한다.

    그 까닭은 뷔퐁 추정량이 표본비율의 비선형 변환 $g(x) = 2/x$ 를 거치면서 분산을 키우기 때문이다. 사분원 추정량은 표본비율의 선형함수($4\bar{I}_n$)이므로 베르누이 분산을 키움 없이 그대로 이어받는다. $\square$
