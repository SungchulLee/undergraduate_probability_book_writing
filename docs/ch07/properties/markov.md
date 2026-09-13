# 마르코프 부등식

## 정리의 서술

$X$ 가 음이 아닌 확률변수이고 $a > 0$ 이면 다음이 성립한다.

$$
P(X \geq a) \leq \frac{E[X]}{a}
$$

---

## 증명

$$
E[X] = \int_0^{\infty} x f(x) \, dx \geq \int_a^{\infty} x f(x) \, dx \geq a \int_a^{\infty} f(x) \, dx = a \, P(X \geq a)
$$

---

## 예

$X$ 의 평균이 10이면 $P(X \geq 50) \leq 10/50 = 0.2$ 이다.

이 경계는 헐거울 때가 많지만, 분포의 생김새에 관한 정보 없이 평균만 알면 쓸 수 있다.

---

## 파이썬 구현

```python
import numpy as np

np.random.seed(42)
N = 1_000_000

# Exponential(1): 평균 = 1
X = np.random.exponential(1, N)
a = 3
markov_bound = 1 / a
actual_prob = np.mean(X >= a)
print(f"P(X >= {a}): Markov bound = {markov_bound:.4f}, actual = {actual_prob:.4f}")
```

## 연습문제

**연습문제 1.** $X \geq 0$ 이고 $E[X] = 5$ 일 때 마르코프 부등식을 써서 $P(X \geq 20)$ 의 상계를 구하여라.

??? success "연습문제 1 풀이"
    $$
    P(X \geq 20) \leq \frac{E[X]}{20} = \frac{5}{20} = 0.25
    $$

    그러므로 $P(X \geq 20) \leq 1/4$ 이다. 분포에 관한 다른 정보가 없을 때 얻을 수 있는 가장 촘촘한 결론이다.
