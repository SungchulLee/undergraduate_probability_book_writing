# 고전적 확률

## 같은 정도로 일어나는 확률측도

공정한 동전 던지기, 공정한 주사위 굴리기, 잘 섞은 카드 한 벌에서 뽑기처럼 많은 실험에는 자연스러운 대칭성이 있어 모든 결과가 같은 정도로 일어난다. 이런 상황에서 확률 계산은 세기 문제로 바뀐다. 바라는 결과의 수를 세어 전체 결과의 수로 나누면 되기 때문이다.

유한한 표본공간의 모든 결과가 **같은 정도로 일어난다면** 확률측도는 아주 단순한 꼴이 된다.

$$
P(\omega) = \frac{1}{|\Omega|}
$$

임의의 사건 $A \subseteq \Omega$ 에 대해서는 다음과 같다.

$$
P(A) = \frac{|A|}{|\Omega|}
$$

이것이 **고전적** 확률모형, 곧 **같은 정도로 일어나는** 확률모형이다. 확률을 구하는 일이 세는 일로 바뀐다. 바라는 결과의 수 $|A|$ 를 세어 전체 결과의 수 $|\Omega|$ 로 나누면 된다.

!!! note "언제 쓸 수 있는가"
    같은 정도로 일어나는 모형은 다음 조건에서 쓸 수 있다.

    - 표본공간이 유한하다
    - 무게를 똑같이 주어도 된다는 것을 뒷받침하는 대칭성이 있다(예: 공정한 동전, 공정한 주사위, 잘 섞은 카드 한 벌)

    결과마다 일어날 법한 정도가 다를 때는(예: 치우친 주사위, 치우친 동전) 이 모형을 쓸 수 **없다**.

## 예제: 공정한 동전을 세 번 던지기

표본공간에는 같은 정도로 일어나는 결과가 $|\Omega| = 2^3 = 8$ 개 있다.

$$
\Omega = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}
$$

결과마다 확률은 다음과 같다.

$$
P(\omega) = \frac{1}{8}
$$

!!! example "사건의 확률 구하기"

    - $P(\text{모두 앞면}) = P(\{HHH\}) = \frac{1}{8}$
    - $P(\text{앞면이 정확히 2번}) = P(\{HHT, HTH, THH\}) = \frac{3}{8}$
    - $P(\text{앞면이 적어도 1번}) = 1 - P(\{TTT\}) = 1 - \frac{1}{8} = \frac{7}{8}$

## 예제: 풀하우스가 나올 확률

포커에서 **풀하우스**란 같은 끗수의 카드 3장과 다른 끗수의 카드 2장으로 이루어진 패를 말한다.

**표본공간:** 표준 52장 카드 한 벌에서 5장을 고르는 방법의 수는 다음과 같다.

$$
|\Omega| = \binom{52}{5}
$$

**바라는 결과 세기:**

| 단계 | 가짓수 |
|------|-------|
| 세 장이 될 끗수를 고른다 | 13가지 |
| 그 끗수에서 4개의 무늬 가운데 3개를 고른다 | $\binom{4}{3}$ 가지 |
| 두 장이 될 끗수를 고른다 | 남은 12가지 |
| 그 끗수에서 4개의 무늬 가운데 2개를 고른다 | $\binom{4}{2}$ 가지 |

그러므로 다음을 얻는다.

$$
|A| = 13 \cdot \binom{4}{3} \cdot 12 \cdot \binom{4}{2}
$$

풀하우스가 나올 확률은 다음과 같다.

$$
P(\text{풀하우스}) = \frac{|A|}{|\Omega|} = \frac{13 \cdot \binom{4}{3} \cdot 12 \cdot \binom{4}{2}}{\binom{52}{5}}
$$

## 파이썬 예제

```python
from math import comb

# 동전 던지기 예제
omega_coins = ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']

# 사건 세기
exactly_2H = [w for w in omega_coins if w.count('H') == 2]
at_least_1H = [w for w in omega_coins if w.count('H') >= 1]

print("=== Fair Coin (3 flips) ===")
print(f"P(all heads) = 1/{len(omega_coins)} = {1/len(omega_coins):.4f}")
print(f"P(exactly 2 heads) = {len(exactly_2H)}/{len(omega_coins)} = {len(exactly_2H)/len(omega_coins):.4f}")
print(f"P(at least 1 head) = {len(at_least_1H)}/{len(omega_coins)} = {len(at_least_1H)/len(omega_coins):.4f}")

# 풀하우스 확률
print("\n=== Full House ===")
omega_size = comb(52, 5)
full_house = 13 * comb(4, 3) * 12 * comb(4, 2)

print(f"|Ω| = C(52,5) = {omega_size}")
print(f"|A| = 13 × C(4,3) × 12 × C(4,2) = 13 × {comb(4,3)} × 12 × {comb(4,2)} = {full_house}")
print(f"P(full house) = {full_house}/{omega_size} = {full_house/omega_size:.6f}")
print(f"P(full house) ≈ 1 in {omega_size/full_house:.0f}")
```

**실행 결과:**
```
=== Fair Coin (3 flips) ===
P(all heads) = 1/8 = 0.1250
P(exactly 2 heads) = 3/8 = 0.3750
P(at least 1 head) = 7/8 = 0.8750

=== Full House ===
|Ω| = C(52,5) = 2598960
|A| = 13 × C(4,3) × 12 × C(4,2) = 13 × 4 × 12 × 6 = 3744
P(full house) = 3744/2598960 = 0.001441
P(full house) ≈ 1 in 694
```

## 연습문제

**연습문제 1.** 공정한 주사위 두 개를 굴린다. 두 눈의 합이 7일 확률은 얼마인가?

??? success "연습문제 1 풀이"
    같은 정도로 일어나는 결과가 $|\Omega| = 36$ 개 있다. 합이 7이 되는 쌍은 $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$ 이므로 $|A| = 6$ 이다.

    $$
    P(\text{합} = 7) = \frac{6}{36} = \frac{1}{6}
    $$

---

**연습문제 2.** 표준 52장 카드 한 벌을 섞은 뒤 카드 2장을 뽑는다. 둘 다 에이스일 확률은 얼마인가?

??? success "연습문제 2 풀이"
    $$
    P(\text{둘 다 에이스}) = \frac{\binom{4}{2}}{\binom{52}{2}} = \frac{6}{1326} = \frac{1}{221} \approx 0.00452
    $$

---

**연습문제 3.** 남자 8명과 여자 6명 가운데 5명으로 이루어진 위원회를 무작위로 뽑는다. 위원회가 남자 3명과 여자 2명으로 이루어질 확률은 얼마인가?

??? success "연습문제 3 풀이"
    $$
    P = \frac{\binom{8}{3}\binom{6}{2}}{\binom{14}{5}} = \frac{56 \times 15}{2002} = \frac{840}{2002} = \frac{60}{143} \approx 0.4196
    $$

---

**연습문제 4.** 서로 다른 책 4권을 책꽂이에 무작위로 꽂는다. 이 책들이 가나다순으로 놓일 확률은 얼마인가?

??? success "연습문제 4 풀이"
    $|\Omega| = 4! = 24$ 이다. 가나다순인 배열은 정확히 하나뿐이다.

    $$
    P(\text{가나다순}) = \frac{1}{24} \approx 0.0417
    $$

    더 일반적으로, 서로 다른 책이 $n$ 권이면 확률은 $1/n!$ 이다.

---

**연습문제 5.** 주머니에 빨간 구슬 5개와 파란 구슬 7개가 들어 있다. 구슬 3개를 비복원으로 무작위로 뽑는다. 세 개가 모두 같은 색일 확률을 구하여라.

??? success "연습문제 5 풀이"
    $$
    P(\text{모두 빨강}) = \frac{\binom{5}{3}}{\binom{12}{3}} = \frac{10}{220}
    $$

    $$
    P(\text{모두 파랑}) = \frac{\binom{7}{3}}{\binom{12}{3}} = \frac{35}{220}
    $$

    $$
    P(\text{모두 같은 색}) = \frac{10 + 35}{220} = \frac{45}{220} = \frac{9}{44} \approx 0.2045
    $$
