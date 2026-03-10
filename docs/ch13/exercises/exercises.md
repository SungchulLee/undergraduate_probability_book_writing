# Chapter 13 Exercises

!!! warning "Exercise page"
    This page collects practice problems for Chapter 13 and does not follow the five-section structure used by concept pages.

Exercises on the Poisson process: definition, properties, merging, splitting, and conditional distributions.

## Section 13.1 — Definition and Basics

**Exercise 13.1.** Customers arrive at a store as a Poisson process with rate 8 per hour. Find the probability of exactly 3 arrivals in a 15-minute window.

**Exercise 13.2.** Show that the interarrival times of a Poisson process are iid $\text{Exp}(\lambda)$.

**Exercise 13.3.** If events arrive at rate $\lambda = 4$/min, find the probability that the time until the 5th event exceeds 2 minutes.

## Section 13.2 — Properties

**Exercise 13.4.** Calls arrive at rate 10/hour. Find the expected number and variance of calls in a 3-hour shift.

**Exercise 13.5.** Prove that the Poisson process has independent increments using the memoryless property of exponential interarrivals.

**Exercise 13.6.** Why does a renewal process with $\text{Gamma}(2, \lambda)$ interarrivals *not* have independent increments?

## Section 13.3 — Merging and Splitting

**Exercise 13.7.** Two independent Poisson processes have rates 3 and 5 per hour. What is the distribution of the total count in 2 hours?

**Exercise 13.8.** Emails arrive at rate 20/hour. Each is spam with probability 0.4, independently. Find the distribution of spam emails per hour and verify by simulation.

**Exercise 13.9.** Accidents occur on a highway as a Poisson process with rate 2/day. Each accident is fatal with probability 0.05. Find $P(\text{no fatal accidents in a week})$.

## Section 13.4 — Conditional Distributions

**Exercise 13.10.** Given that 10 events occurred in $[0, 5]$, find the expected arrival time of the first event and the last event.

**Exercise 13.11.** Given $N(1) = 3$, find the probability that all three events occurred in $[0, 0.5]$.

**Exercise 13.12.** Write a simulation to verify the uniform-arrivals property: condition on $N(10) = 8$ and compare the histogram of arrival positions with $\text{Uniform}(0, 10)$.
