# 체비쇼프 부등식

## 정리의 서술

평균이 $\mu$ 이고 분산이 $\sigma^2$ 인 임의의 확률변수 $X$ 와 임의의 $k > 0$ 에 대하여 다음이 성립한다.

$$
P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}
$$

같은 말로, 임의의 $a > 0$ 에 대하여 다음이 성립한다.

$$
P(|X - \mu| \geq a) \leq \frac{\sigma^2}{a^2}
$$

---

## 증명

음이 아닌 확률변수 $(X - \mu)^2$ 에 마르코프 부등식을 적용하자.

$$
P(|X - \mu| \geq a) = P((X - \mu)^2 \geq a^2) \leq \frac{E[(X-\mu)^2]}{a^2} = \frac{\sigma^2}{a^2}
$$

$a = k\sigma$ 로 두면 $P(|X - \mu| \geq k\sigma) \leq 1/k^2$ 를 얻는다.

---

## 주요 값

| $k$ | $P(\lvert X - \mu\rvert \geq k\sigma) \leq$ | $k\sigma$ 안에 들어 있는 확률(최소) |
|:---:|:---:|:---:|
| 1 | 1 | 0% (뜻이 없음) |
| 2 | 0.25 | 75% |
| 3 | 0.111 | 88.9% |
| 4 | 0.0625 | 93.75% |
| 5 | 0.04 | 96% |

---

## 응용: 큰수의 약법칙

$X_1, \ldots, X_n$ 을 평균이 $\mu$, 분산이 $\sigma^2$ 인 i.i.d. 확률변수라 하자. 표본평균 $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ 는 $E[\bar{X}_n] = \mu$ 와 $\text{Var}(\bar{X}_n) = \sigma^2/n$ 을 만족한다. 체비쇼프 부등식에 따라 다음을 얻는다.

$$
P(|\bar{X}_n - \mu| \geq \epsilon) \leq \frac{\sigma^2}{n\epsilon^2} \to 0 \text{ as } n \to \infty
$$

---

## 파이썬 구현

```python
import numpy as np

np.random.seed(42)
N = 1_000_000

# Normal(0,1): 체비쇼프 경계와 실제값 비교
X = np.random.normal(0, 1, N)

for k in [1, 2, 3, 4, 5]:
    chebyshev = 1 / k**2
    actual = np.mean(np.abs(X) >= k)
    print(f"k={k}: Chebyshev <= {chebyshev:.4f}, actual = {actual:.4f}")
```

## 연습문제

**연습문제 1.** $E[X] = 10$ 이고 $\text{Var}(X) = 4$ 일 때 체비쇼프 부등식을 써서 $P(|X - 10| \geq 6)$ 의 상계를 구하여라.

??? success "연습문제 1 풀이"
    $$
    P(|X - 10| \geq 6) \leq \frac{\text{Var}(X)}{6^2} = \frac{4}{36} = \frac{1}{9} \approx 0.111
    $$

    그러므로 $P(|X - 10| \geq 6) \leq 1/9$ 이다. 같은 말로, $k = 6/\sigma = 3$ 으로 두면 체비쇼프 부등식은 "3-시그마" 경계 $1/k^2 = 1/9$ 를 준다.
