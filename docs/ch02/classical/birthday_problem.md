# 생일 문제

## 문제

생일 문제는 확률이 직관을 얼마나 배신할 수 있는지 보여 주는 고전적인 예이다. 물음은 얄미울 만큼 단순하지만 답은 대부분의 사람을 놀라게 한다. 그리 크지 않은 무리에서도 쌍을 지어 견주는 경우가 얼마나 많은지를 사람들이 낮추어 보기 때문이다.

$n$ 명이 있는 방에서 적어도 두 사람의 생일이 같을 확률은 얼마인가?

**가정:**

- 생일은 365가지이고 모두 같은 정도로 일어난다(윤년은 무시한다)
- 사람들의 생일은 서로 독립이다

## 여사건을 쓴 풀이

여사건, 곧 **$n$ 명의 생일이 모두 다를** 확률을 구하는 편이 훨씬 쉽다.

### 표본공간

$n$ 명은 저마다 365가지 생일 가운데 아무것이나 가질 수 있다.

$$
|\Omega| = 365^n
$$

### 여사건 Ac 세기 (생일이 모두 다른 경우)

- 1번 사람: 365가지
- 2번 사람: 364가지 (1번 사람과 달라야 한다)
- 3번 사람: 363가지
- $\vdots$
- $n$ 번 사람: $365 - (n-1)$ 가지

$$
|A^c| = 365 \times 364 \times 363 \times \cdots \times (365 - n + 1) = \frac{365!}{(365-n)!}
$$

### 생일이 겹칠 확률

$$
P(\text{적어도 한 쌍이 겹침}) = 1 - P(\text{모두 다름}) = 1 - \frac{365 \times 364 \times \cdots \times (365 - n + 1)}{365^n}
$$

$$
= 1 - \prod_{k=0}^{n-1}\left(1 - \frac{k}{365}\right)
$$

!!! note "되풀이해서 구하기"
    생일이 모두 다를 확률은 한 단계씩 쌓아 올려 구할 수 있다. $B_k$ 를 앞의 $k$ 명의 생일이 모두 다를 확률이라 하자. 그러면 $B_1 = 1$ 이고 다음이 성립한다.

    $$
    B_k = B_{k-1} \cdot \left(1 - \frac{k-1}{365}\right)
    $$

    이 점화식을 쓰면 큰 계승을 계산하지 않아도 되고 수치적으로도 안정적이다.

## 주요 결과

| $n$ | $P(\text{적어도 한 쌍이 겹침})$ |
|-----|-------------------------------|
| 10 | 0.1169 |
| 20 | 0.4114 |
| **23** | **0.5073** |
| 30 | 0.7063 |
| 50 | 0.9704 |
| 57 | 0.9901 |
| 70 | 0.9992 |

!!! note "놀라운 점"
    **23명**만 있어도 생일이 겹칠 확률이 이미 50%를 넘는다. 57명이면 그 확률이 99%를 넘는다. 이 경계가 놀라울 만큼 낮기 때문에 흔히 **생일 역설**이라 부른다.

## 왜 경계가 이토록 낮은가

핵심은 **특정한** 한 사람이 다른 누군가와 생일이 같은지를 묻는 것이 아니라는 데 있다. $n$ 명 가운데 **어느 한 쌍**이라도 생일이 같은지를 묻는 것이다. 쌍의 개수는 2차식으로 늘어난다.

$$
\binom{n}{2} = \frac{n(n-1)}{2}
$$

23명이면 쌍이 $\binom{23}{2} = 253$ 개 있고, 저마다 겹칠 기회가 된다.

## 근사

$x$ 가 작을 때 $1 - x \approx e^{-x}$ 이다. 그러므로 다음을 얻는다.

$$
P(\text{모두 다름}) = \prod_{k=0}^{n-1}\left(1 - \frac{k}{365}\right) \approx \prod_{k=0}^{n-1} e^{-k/365} = e^{-n(n-1)/(2 \cdot 365)}
$$

$P(\text{겹침}) = 0.5$ 로 두면 다음과 같다.

$$
e^{-n(n-1)/730} = 0.5 \implies n(n-1) \approx 730 \ln 2 \approx 506 \implies n \approx 23
$$

!!! tip "곱 공식과의 관계"
    곱에 들어 있는 인수 $1 - k/365$ 는 하나하나 보면 1에 가깝지만, 이들을 죽 곱하면 값이 빠르게 줄어든다. 근사식 $1 - x \approx e^{-x}$ 는 이 곱을 다음과 같이 바꾸어 준다.

    $$
    P(\text{모두 다름}) \approx e^{-n(n-1)/730}
    $$

    이렇게 하면 지수가 2차식으로 커진다는 점이 뚜렷이 드러난다.

## 일반화

생일 문제는 자연스럽게 일반화된다. 생일이 365가지가 아니라 $d$ 가지라면 $n$ 명 가운데 생일이 겹칠 확률은 다음과 같다.

$$
P(\text{겹침}) \approx 1 - e^{-n(n-1)/(2d)}
$$

50% 경계는 대략 $n \approx 1.2\sqrt{d}$ 에서 나타난다.

!!! example "암호학에서의 응용"
    생일 문제는 암호학의 **생일 공격**의 바탕이 된다. 출력이 $d = 2^b$ 가지인 해시 함수($b$ 비트 해시)에서는 무작위 입력을 대략 $2^{b/2}$ 개쯤 넣으면 충돌이 일어날 것으로 기대된다. 128비트 해시가 충돌 저항성은 64비트밖에 주지 못하는 까닭이 여기에 있다.

## 파이썬 예제

```python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def birthday_probability(n, days=365):
    """n명 가운데 적어도 두 사람의 생일이 같을 정확한 확률."""
    if n > days:
        return 1.0
    p_all_different = 1.0
    for k in range(n):
        p_all_different *= (days - k) / days
    return 1 - p_all_different

# 확률 구하기
ns = range(1, 81)
probs = [birthday_probability(n) for n in ns]

# P > 0.5 가 되는 경계 찾기
threshold = next(n for n in ns if birthday_probability(n) > 0.5)
print(f"Smallest n with P > 0.5: n = {threshold}")
print(f"P({threshold}) = {birthday_probability(threshold):.4f}")

# 표 찍기
print(f"\n{'n':>4} | {'P(match)':>10} | {'# pairs':>8}")
print("-" * 30)
for n in [10, 20, 23, 30, 40, 50, 57, 70]:
    p = birthday_probability(n)
    pairs = n * (n - 1) // 2
    print(f"{n:4d} | {p:10.4f} | {pairs:8d}")

# 몬테카를로 모의실험
def birthday_simulation(n, n_sim=100_000):
    """생일 문제를 모의실험한다."""
    np.random.seed(42)
    matches = 0
    for _ in range(n_sim):
        birthdays = np.random.randint(0, 365, size=n)
        if len(set(birthdays)) < n:
            matches += 1
    return matches / n_sim

print(f"\nSimulation verification (100,000 trials):")
for n in [23, 50, 70]:
    exact = birthday_probability(n)
    sim = birthday_simulation(n)
    print(f"  n={n}: exact={exact:.4f}, simulated={sim:.4f}")

# 그림 그리기
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(ns, probs, 'b-', linewidth=2)
ax.axhline(y=0.5, color='r', linestyle='--', alpha=0.7, label='P = 0.5')
ax.axvline(x=23, color='g', linestyle='--', alpha=0.7, label='n = 23')
ax.set_xlabel('Number of people (n)', fontsize=12)
ax.set_ylabel('P(at least one shared birthday)', fontsize=12)
ax.set_title('Birthday Problem', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_xlim(1, 80)
ax.set_ylim(0, 1.05)
plt.tight_layout()
plt.savefig('/home/claude/ch02/classical/birthday_problem.png', dpi=150)
plt.close()
print("\nPlot saved.")
```

**실행 결과:**
```
Smallest n with P > 0.5: n = 23
P(23) = 0.5073

   n |   P(match) |  # pairs
------------------------------
  10 |     0.1169 |       45
  20 |     0.4114 |      190
  23 |     0.5073 |      253
  30 |     0.7063 |      435
  40 |     0.8912 |      780
  50 |     0.9704 |     1225
  57 |     0.9901 |     1596
  70 |     0.9992 |     2415

Simulation verification (100,000 trials):
  n=23: exact=0.5073, simulated=0.5063
  n=50: exact=0.9704, simulated=0.9700
  n=70: exact=0.9992, simulated=0.9992
```

무리의 크기에 따른 겹침 확률은 S자 모양의 곡선을 그린다. $n$ 이 작을 때는(쌍이 적어) 천천히 오르다가 가운데 구간에서 빠르게 치솟고, $n$ 이 크면 1에 가까이 붙어 버린다. 이런 모양은 "모두 다를" 확률이 점점 작아지는 인수들의 곱으로 줄어드는, 여사건에 바탕을 둔 확률에서 흔히 나타난다.

## 연습문제

**연습문제 1.**

**(a)** 학생이 30명인 학급에서 적어도 두 학생의 생일이 같을 확률은 얼마인가? (365일이 모두 같은 정도로 일어난다고 하자.)

**(b)** 그 확률이 0.99를 넘으려면 학급이 얼마나 커야 하는가?

**(c)** 생일이 100가지뿐이라고 하자. 생일이 겹칠 확률이 50%가 되려면 몇 명이 필요한가?

??? success "연습문제 1 풀이"
    **(a)** 정확한 공식을 쓰면 다음과 같다.

    $$
    P(\text{겹침}) = 1 - \frac{365!}{(365-30)! \cdot 365^{30}} \approx 0.7063
    $$

    **(b)** $1 - \prod_{k=0}^{n-1}(1 - k/365) > 0.99$ 를 수치적으로 푼다. 경계는 $n = 57$ 이다($n = 57$ 에서 $P \approx 0.9901$, $n = 56$ 에서 $P \approx 0.9883$).

    **(c)** $d = 100$ 에 근사식 $n \approx 1.2\sqrt{d}$ 를 쓰면 $n \approx 12$ 이다. 정확히 확인해 보면 $n = 12$ 에서 $P \approx 0.500$ 이므로 어림 규칙이 잘 맞는다.

---

**연습문제 2.** 위의 `birthday_probability` 함수를 써서 $P(\text{겹침}) \geq 0.99$ 가 되는 가장 작은 $n$ 을 찾아라.

??? success "연습문제 2 풀이"
    경계를 넘을 때까지 $n$ 을 하나씩 늘려 본다.

    ```python
    threshold = next(n for n in range(1, 366) if birthday_probability(n) >= 0.99)
    ```

    답은 $n = 57$ 이다. 이 크기에서 다음이 성립한다.

    $$
    P(\text{겹침}) = 1 - \prod_{k=0}^{56}\left(1 - \frac{k}{365}\right) \approx 0.9901
    $$

---

**연습문제 3.** `birthday_probability` 함수를 365가지가 아니라 같은 정도로 일어나는 $d$ 가지 생일에 대해 돌아가도록 일반화하여라. $d = 100$ 으로 돌려서 $P(\text{겹침}) \geq 0.5$ 가 되는 가장 작은 $n$ 을 찾아라.

??? success "연습문제 3 풀이"
    이 함수는 이미 `days` 인수를 받는다.

    ```python
    threshold = next(n for n in range(1, 101) if birthday_probability(n, days=100) >= 0.5)
    ```

    $d = 100$ 일 때 경계는 $n = 12$ 이다. 근사식 $n \approx 1.2\sqrt{d} = 1.2\sqrt{100} = 12$ 와 잘 맞는다.

---

**연습문제 4.** $\{0, 1, \ldots, 364\}$ 에서 균등하게 생일 23개를 무작위로 뽑아 둘이 겹치는지를 확인하는 몬테카를로 모의실험을 작성하여라. $N = 100{,}000$ 번 돌린 뒤 모의실험 확률을 정확한 값 $0.5073$ 과 견주어 보아라.

??? success "연습문제 4 풀이"
    ```python
    import numpy as np

    n_people = 23
    n_sim = 100_000
    matches = 0
    for _ in range(n_sim):
        birthdays = np.random.randint(0, 365, size=n_people)
        if len(set(birthdays)) < n_people:
            matches += 1
    simulated = matches / n_sim
    print(f"Simulated: {simulated:.4f}, Exact: 0.5073")
    ```

    한 번 돌리면 대개 `Simulated: 0.5065, Exact: 0.5073` 같은 결과가 나온다. 모의실험 값이 정확한 값과 가까우므로 해석적인 결과가 확인된다.

---

**연습문제 5.** $B_1 = 1$ 인 점화식 $B_k = B_{k-1} \cdot (1 - (k-1)/365)$ 가 닫힌 꼴 $B_n = 365! / (365^n \cdot (365-n)!)$ 과 같음을 증명하여라.

??? success "연습문제 5 풀이"
    귀납법을 쓴다. 첫 단계 $B_1 = 1 = 365!/(365^1 \cdot 364!)$ 은 성립한다. $B_{k-1} = 365!/(365^{k-1}(365-k+1)!)$ 이라 가정하자. 그러면 다음을 얻는다.

    $$
    B_k = B_{k-1} \cdot \frac{365 - (k-1)}{365} = \frac{365!}{365^{k-1}(365-k+1)!} \cdot \frac{365-k+1}{365}
    $$

    $$
    = \frac{365! \cdot (365-k+1)}{365^k \cdot (365-k+1)!} = \frac{365!}{365^k \cdot (365-k)!}
    $$

    이것이 바로 $B_k$ 의 닫힌 꼴이다. $\square$

---

**연습문제 6.** $n > 365$ 일 때 $P(\text{겹침}) = 1$ 인 까닭을 설명하여라. 어떤 조합론의 원리가 이를 보장하며, 곱 공식은 그것을 어떻게 담아내는가?

??? success "연습문제 6 풀이"
    **비둘기집 원리** 때문이다. $n > 365$ 명이 저마다 365가지 생일 가운데 하나를 받는다면 적어도 두 사람의 생일이 같을 수밖에 없으므로 $P(\text{겹침}) = 1$ 이다.

    곱 공식에서는 $k = 365$ 에 해당하는 인수가 $1 - 365/365 = 0$ 이므로 곱 전체가 $P(\text{모두 다름}) = 0$ 이 되고, 따라서 $P(\text{겹침}) = 1 - 0 = 1$ 이 된다. 그 뒤의 인수도 모두 0(또는 물리적으로 뜻이 없는 음수)이므로 $n > 365$ 에서도 공식이 그대로 옳음을 알 수 있다.
