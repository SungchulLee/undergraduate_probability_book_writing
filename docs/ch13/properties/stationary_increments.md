# Stationary Increments

## Definition

The **stationary increments** property means that the distribution of the number of events in any interval depends only on the length of the interval, not on when it starts.

!!! info "Stationary Increments"
    A counting process $\{N(t)\}$ has **stationary increments** if, for every $s \geq 0$ and $t > 0$:

    $$
    N(s, s+t) \stackrel{d}{=} N(0, t)
    $$

    That is, $N(s, s+t)$ and $N(0, t)$ have the same distribution.

For the Poisson process, both $N(s, s+t)$ and $N(0, t)$ follow $\text{Po}(\lambda t)$, confirming stationarity.

---

## Intuition: Time-Shift Invariance

Stationarity means the process "looks the same" regardless of when you start observing it. Imagine watching events arrive on a timeline:

- The probability of seeing exactly 3 events in a 1-hour window is the same whether you watch from 2pm to 3pm or from 8pm to 9pm
- The expected number of events per hour is always $\lambda$, regardless of the hour

In everyday language: **the process has no memory of when you started watching**.

---

## Formal Consequence

Combined with independent increments, stationarity gives the full joint distribution of the process. For any partition $0 = t_0 < t_1 < \cdots < t_n$:

$$
P\bigl(N(t_0, t_1) = k_1, \ldots, N(t_{n-1}, t_n) = k_n\bigr) = \prod_{i=1}^{n} \frac{e^{-\lambda(t_i - t_{i-1})} [\lambda(t_i - t_{i-1})]^{k_i}}{k_i!}
$$

Each factor depends only on the interval length $t_i - t_{i-1}$, not on the absolute times.

---

## When Stationarity Fails

Many real-world counting processes are **not** stationary. Recognizing this is important for choosing the right model.

| Scenario | Why stationarity fails |
|:---|:---|
| Customer arrivals at a restaurant | Lunch and dinner rushes create time-varying rates |
| Website traffic | Peaks during business hours, low at night |
| Emergency room visits | Higher rates on weekends and holidays |
| Earthquake aftershocks | Rate decays after the main shock (Omori's law) |

In these situations, the **non-homogeneous Poisson process** with a time-varying rate $\lambda(t)$ is more appropriate. The count in $(s, s+t]$ is then $\text{Po}\!\left(\int_s^{s+t} \lambda(u)\,du\right)$, which generally depends on $s$.

---

## Stationarity Does Not Imply Independent Increments

!!! warning "The Two Properties Are Distinct"
    A process can have stationary increments without having independent increments, and vice versa.

    - A **renewal process** with non-exponential interarrival times has stationary increments (asymptotically) but generally does not have independent increments
    - A process where each interval's count is drawn from a Poisson distribution but the draws are correlated would have stationary increments without independence

    The Poisson process is special precisely because it satisfies **both** properties simultaneously.

??? example "Testing Stationarity"
    A hospital records patient arrivals and counts events in each hour of the day over many weeks. If the average count per hour is roughly constant (say $\lambda \approx 4.2$ regardless of the hour), stationarity is plausible. If the count is systematically higher during certain hours, stationarity fails and a non-homogeneous model is needed.

---

## Summary

Stationarity is the property that makes the Poisson process "clock-invariant": shifting the observation window in time does not change the statistical behavior. Together with independent increments and the initialization $N(0) = 0$, it completely determines the Poisson process. When stationarity is violated, we move to the non-homogeneous Poisson process, which retains independent increments but allows a time-varying rate.
