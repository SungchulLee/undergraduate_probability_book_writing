# 전분산 법칙(이브의 법칙)

## 정리의 서술

임의의 확률변수 $X$ 와 $Y$ 에 대하여 다음이 성립한다.

$$
\text{Var}(X) = E\bigl[\text{Var}(X \mid Y)\bigr] + \text{Var}\bigl(E(X \mid Y)\bigr)
$$

이것을 **이브의 법칙**이라 한다(외우는 요령: **E**xpected **V**ariance + **V**ariance of **E**xpectation, 곧 EVVE).

## 뜻풀이

$X$ 의 전체 분산은 두 조각으로 쪼개진다.

**$E\bigl[\text{Var}(X \mid Y)\bigr]$** — **무리 안 분산의 평균**(*설명되지 않는 분산*이라고도 한다). $Y$ 로 조건을 준 뒤에도 남는 불확실성을 평균한 것이다. $Y$ 가 나눈 각 무리 안에서의 퍼짐을 무리 전체에 걸쳐 평균한 값이다.

**$\text{Var}\bigl(E(X \mid Y)\bigr)$** — **무리 사이 분산**(*설명되는 분산*이라고도 한다). 무리마다의 평균이 무리에 따라 얼마나 달라지는지를 잰다. $Y$ 를 알아서 "설명되는" $X$ 의 변동을 담는다.

## 따름

두 조각이 모두 음이 아니므로(분산은 언제나 $\geq 0$ 이고 음이 아닌 양의 기댓값도 $\geq 0$ 이다) 다음이 성립한다.

$$
\text{Var}(X) \geq E\bigl[\text{Var}(X \mid Y)\bigr] \qquad \text{그리고} \qquad \text{Var}(X) \geq \text{Var}\bigl(E(X \mid Y)\bigr)
$$

달리 말하면 **조건을 주면 평균적인 분산은 줄어들 뿐 늘지 않는다**. 곧 조건부분산의 평균은 많아야 조건 없는 분산이다.

## 증명

$\text{Var}(X) = E(X^2) - (EX)^2$ 에서 출발하여 두 항 모두에 탑 성질을 적용하자.

$$
E(X^2) = E\bigl[E(X^2 \mid Y)\bigr]
$$

조건부 간편식으로 $E(X^2 \mid Y) = \text{Var}(X \mid Y) + \bigl(E(X \mid Y)\bigr)^2$ 라 쓰면 다음을 얻는다.

$$
E(X^2) = E\bigl[\text{Var}(X \mid Y)\bigr] + E\bigl[(E(X \mid Y))^2\bigr]
$$

또한 탑 성질에 따라 $(EX)^2 = \bigl(E[E(X \mid Y)]\bigr)^2$ 이다. 그러므로 다음을 얻는다.

$$
\begin{aligned}
\text{Var}(X) &= E\bigl[\text{Var}(X \mid Y)\bigr] + E\bigl[(E(X \mid Y))^2\bigr] - \bigl(E[E(X \mid Y)]\bigr)^2 \\
&= E\bigl[\text{Var}(X \mid Y)\bigr] + \text{Var}\bigl(E(X \mid Y)\bigr)
\end{aligned}
$$

## 풀이 예제

### 백화점

$T = \sum_{i=1}^{N} X_i$ 이고 $E(T \mid N) = 8N$, $\text{Var}(T \mid N) = 16N$ 일 때 다음과 같다.

| 조각 | 계산 | 값 |
|:----------|:-----------|------:|
| $\text{Var}\bigl(E(T \mid N)\bigr)$ | $\text{Var}(8N) = 64 \cdot 100$ | 6400 |
| $E\bigl[\text{Var}(T \mid N)\bigr]$ | $E(16N) = 16 \cdot 50$ | 800 |
| $\text{Var}(T)$ | $6400 + 800$ | 7200 |

무리 사이 분산(6400)이 훨씬 크다. 하루 매출이 들쭉날쭉한 까닭은 손님 *개개인*의 씀씀이가 달라서가 아니라 손님 *수*가 달라지기 때문이다.

### 갇힌 광부

이브의 법칙을 되풀이해 적용하면 다음과 같다.

$$
\text{Var}(T) = 72.67 + \tfrac{2}{3}\,\text{Var}(T) \implies \text{Var}(T) = 218
$$

### HH 가 나올 때까지 기다리기

$$
\text{Var}(W_{HH}) = 9 + 2 + \tfrac{1}{2}\,\text{Var}(W_{HH}) \implies \text{Var}(W_{HH}) = 22
$$

## 파이썬으로 확인하기

```python
import numpy as np

np.random.seed(42)
n_sim = 500_000

# 지수분포 예로 이브의 법칙 확인
# X | Y=y ~ Exp(1/y), Y ~ Exp(1)
Y = np.random.exponential(1, n_sim)
X = np.array([np.random.exponential(y) for y in Y])

# E(X|Y) = Y,  Var(X|Y) = Y^2
E_X_given_Y = Y
Var_X_given_Y = Y**2

# 이브의 법칙의 두 조각
var_of_expectation = np.var(E_X_given_Y)
expected_variance = np.mean(Var_X_given_Y)
total_var = np.var(X)

print("=== Eve's Law Verification (Exponential Example) ===")
print(f"Var(X)                    = {total_var:.3f}")
print(f"Var(E(X|Y))               = {var_of_expectation:.3f}")
print(f"E(Var(X|Y))               = {expected_variance:.3f}")
print(f"Var(E(X|Y)) + E(Var(X|Y)) = {var_of_expectation + expected_variance:.3f}")
print(f"Match: {np.isclose(total_var, var_of_expectation + expected_variance, atol=0.1)}")
```

## 연습문제

**연습문제 1.** 전분산 법칙 $\text{Var}(X) = E[\text{Var}(X \mid Y)] + \text{Var}(E(X \mid Y))$ 에서 각 항이 무엇을 뜻하는지 직관적으로 설명하여라. 첫째 항이 0이 되는 조건은 무엇인가? 둘째 항이 0이 되는 조건은 무엇인가?

??? success "연습문제 1 풀이"

    - $E[\text{Var}(X \mid Y)]$ 는 **무리 안의 변동**이다. $Y$ 의 각 값에서 $X$ 의 분산을 평균한 값으로, $Y$ 로 *설명되지 않는* 잡음을 잰다.
    - $\text{Var}(E(X \mid Y))$ 는 **무리 사이의 변동**이다. $Y$ 가 달라질 때 $X$ 의 조건부평균이 얼마나 달라지는지를 재며, $Y$ 로 *설명되는* 신호를 잰다.

    첫째 항이 0일 필요충분조건은 $X$ 가 $Y$ 의 확정적인 함수인 것이다(잡음이 남지 않는다).

    둘째 항이 0일 필요충분조건은 $E(X \mid Y)$ 가 $Y$ 에 관계없이 상수인 것이다. 이를테면 $X$ 와 $Y$ 가 독립일 때, 더 넓게는 $Y$ 가 $E[X]$ 에 관한 정보를 전혀 주지 않을 때가 그렇다.

---

**연습문제 2.** 백화점 문제에 대하여 전분산 법칙을 확인하는 모의실험을 짜 보아라. 10만 일을 만들어 무리 안 분산과 무리 사이 분산을 구하고 이론값 $E[\text{Var}(T \mid N)] = 800$, $\text{Var}(E(T \mid N)) = 6400$ 과 견주어 보아라.

??? success "연습문제 2 풀이"
    ```python
    """백화점 예제에서 전분산 법칙을 확인한다."""
    import numpy as np

    # === 모의실험 ===
    def simulate(n_days: int = 100_000, seed: int = 42) -> dict:
        rng = np.random.default_rng(seed)
        # N ~ Poisson(10): 하루 손님 수
        N = rng.poisson(10, n_days)
        # T | N ~ Normal(40 * N, sqrt(80 * N)) (i.i.d. 씀씀이의 합)
        T = rng.normal(40 * N, np.sqrt(80 * np.maximum(N, 1)))

        # 전체 분산
        total_var = T.var()

        # 무리 안 분산: E[Var(T|N)] ≈ N 별 표본분산의 평균
        within = 0.0
        for k in np.unique(N):
            mask = N == k
            if mask.sum() > 1:
                within += mask.mean() * T[mask].var()

        # 무리 사이 분산: Var(E[T|N]) ≈ N 별 무리 평균의 분산
        means = np.array([T[N == k].mean() for k in np.unique(N) if (N == k).sum() > 0])
        weights = np.array([(N == k).mean() for k in np.unique(N) if (N == k).sum() > 0])
        grand_mean = (weights * means).sum()
        between = (weights * (means - grand_mean) ** 2).sum()

        return {"total": total_var, "within": within, "between": between}

    if __name__ == "__main__":
        stats = simulate()
        print(f"Var(T)        = {stats['total']:.1f}  (theory: 7200)")
        print(f"E[Var(T|N)]   = {stats['within']:.1f}  (theory: 800)")
        print(f"Var(E(T|N))   = {stats['between']:.1f}  (theory: 6400)")
        print(f"Sum           = {stats['within'] + stats['between']:.1f}")
    ```

    전형적인 출력은 전체 $\approx 7200$, 무리 안 $\approx 800$, 무리 사이 $\approx 6400$ 이다. 몬테카를로 오차 범위 안에서 전분산 법칙이 성립한다.
