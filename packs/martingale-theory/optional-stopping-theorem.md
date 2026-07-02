---
title: "Optional stopping theorem"
source: https://en.wikipedia.org/wiki/Optional_stopping_theorem
domain: martingale-theory
license: CC-BY-SA-4.0
tags: martingale theory, stopping time, conditional expectation, optional stopping theorem
fetched: 2026-07-02
---

# Optional stopping theorem

In probability theory, the **optional stopping theorem** (or sometimes **Doob's optional sampling theorem**, for American probabilist Joseph Doob) says that, under certain conditions, the expected value of a martingale at a stopping time is equal to its initial expected value.

The concept can be understood through the following key principles:

- Since martingales can be used to model the wealth of a gambler participating in a fair game, the optional stopping theorem implies that, on average, nothing can be gained by stopping play based on the information obtainable so far (i.e., without looking into the future).
- Certain conditions are necessary for this result to hold true. In particular, the theorem applies to doubling strategies and illustrates mathematically why such strategies cannot guarantee a profit with finite resources.
- The optional stopping theorem is an important tool of mathematical finance in the context of the fundamental theorem of asset pricing, helping to evaluate the expected returns of various pricing models.

## Statement

A discrete-time version of the theorem is given below, with $\mathbb {N} _{0}$ denoting the set of natural numbers, including zero.

Let $X=(X_{t})_{t\in \mathbb {N} _{0}}$ be a discrete-time martingale and $\tau$ a stopping time with values in $\mathbb {N} _{0}\cup \{\infty \}$ , both with respect to a filtration $({\mathcal {F}}_{t})_{t\in \mathbb {N} _{0}}$ . Assume that one of the following three conditions holds:

(

a

) The stopping time

$\tau$

is

almost surely

bounded, i.e., there exists a

constant

$c\in \mathbb {N}$

such that

$\tau \leq c$

almost surely.

(

b

) The stopping time

$\tau$

has finite expectation and the conditional expectations of the

absolute value

of the martingale increments are almost surely bounded. More precisely,

$\mathbb {E} [\tau ]<\infty$

and there exists a constant

c

such that

$\mathbb {E} {\bigl [}|X_{t+1}-X_{t}|\,{\big \vert }\,{\mathcal {F}}_{t}{\bigr ]}\leq c$

almost surely on the event

$\{\tau >t\}$

for all

$t\in \mathbb {N} _{0}$

.

(

c

) There exists a constant

c

such that

$|X_{\min\{t,\tau \}}|\leq c$

almost surely for all

$t\in \mathbb {N} _{0}$

.

Then $X_{\tau }$ is an almost surely well-defined random variable and $\mathbb {E} [X_{\tau }]=\mathbb {E} [X_{0}]$ .

Similarly, if the stochastic process $X=(X_{t})_{t\in \mathbb {N} _{0}}$ is a submartingale or a supermartingale and one of the above conditions holds, then: $\mathbb {E} [X_{\tau }]\geq \mathbb {E} [X_{0}]$ for a submartingale, and $\mathbb {E} [X_{\tau }]\leq \mathbb {E} [X_{0}]$ for a supermartingale.

### Remark

Under condition (**c**) it is possible that $\tau =\infty$ happens with positive probability. On this event, $X_{\tau }$ is defined as the almost surely existing pointwise limit of $X=(X_{t})_{t\in \mathbb {N} _{0}}$ . See the proof below for details.

## Applications

The optional stopping theorem has widespread applications in probability, paradox resolution, and random walk theory:

- **Impossibility of perfect betting strategies:** The theorem can be used to prove the impossibility of successful betting strategies for a gambler with a finite lifetime (giving condition (**a**)) or a house limit on bets (condition (**b**)).
  - Suppose that the gambler can wager up to c dollars on a fair coin flip at times 1, 2, 3, etc., winning their wager if the coin comes up heads and losing it if the coin comes up tails.
  - Suppose further that the gambler can quit whenever they like, but cannot predict the outcome of gambles that have not happened yet.
  - The gambler's fortune over time is a martingale, and the time $\tau$ at which they decide to quit (or go broke and are forced to quit) is a stopping time. So the theorem says that $\mathbb {E} [X_{\tau }]=\mathbb {E} [X_{0}]$ . In other words, the gambler leaves with the same amount of money *on average* as when they started.
  - The same result holds if the gambler has a finite limit on their line of credit or how far in debt they may go, rather than a house limit on individual bets.
- **Expected stop position of a random walk:** Suppose a random walk starting at $a\geq 0$ goes up or down by one with equal probability on each step.
  - Suppose further that the walk stops if it reaches 0 or $m\geq a$ ; the time at which this first occurs is a stopping time.
  - If it is known that the expected time at which the walk ends is finite (e.g., from Markov chain theory), the optional stopping theorem predicts that the expected stop position is equal to the initial position a .
  - Solving $a=pm+(1-p)0$ for the probability p that the walk reaches m before 0 gives $p=a/m$ .
- **Expected time of a random walk:** Consider a random walk X that starts at 0 and stops if it reaches $-m$ or $+m$ , and use the $Y_{n}=X_{n}^{2}-n$ martingale from Martingale (probability theory) § Examples of martingales. If $\tau$ is the time at which X first reaches $\pm m$ , then $0=\mathbb {E} [Y_{0}]=\mathbb {E} [Y_{\tau }]=m^{2}-\mathbb {E} [\tau ]$ . This directly gives $\mathbb {E} [\tau ]=m^{2}$ .
- **Violations of the theorem (Counterexamples):** Care must be taken to ensure that one of the conditions of the theorem holds.
  - For example, suppose the last example had instead used a 'one-sided' stopping time, so that stopping only occurred at $+m$ , not at $-m$ .
  - The value of X at this stopping time would therefore be m , meaning the expectation value $\mathbb {E} [X_{\tau }]$ must also be m .
  - This seemingly violates the theorem which would give $\mathbb {E} [X_{\tau }]=X_{0}=0$ . The failure of the optional stopping theorem in this case shows that all three of the conditions fail for a one-sided stopping time with an unrestricted state space.

## Proof

Let $X^{\tau }$ denote the stopped process, which is also a martingale (or a submartingale or supermartingale, respectively). The framework of the proof relies on analyzing this process under the provided conditions:

- Under condition (**a**) or (**b**), the random variable $X^{\tau }$ is well defined.
- Under condition (**c**) the stopped process $X^{\tau }$ is bounded, hence by Doob's martingale convergence theorem it converges almost surely pointwise to a random variable which we call $X_{\tau }$ .

If condition (**c**) holds, then the stopped process $X^{\tau }$ is bounded by the constant random variable $M:=c$ . Otherwise, writing the stopped process as $X_{t}^{\tau }=X_{0}+\sum _{s=0}^{\tau -1\land t-1}(X_{s+1}-X_{s}),\quad t\in \mathbb {N} _{0}$ gives $X_{t}^{\tau }\leq M$ for all $t\in \mathbb {N} _{0}$ , where $M:=|X_{0}|+\sum _{s=0}^{\tau -1}|X_{s+1}-X_{s}|=|X_{0}|+\sum _{s=0}^{\infty }|X_{s+1}-X_{s}|\cdot \mathbf {1} _{\{\tau >s\}}.$

By the monotone convergence theorem, $\mathbb {E} [M]=\mathbb {E} [|X_{0}|]+\sum _{s=0}^{\infty }\mathbb {E} {\bigl [}|X_{s+1}-X_{s}|\cdot \mathbf {1} _{\{\tau >s\}}{\bigr ]}.$

If condition (**a**) holds, then this series only has a finite number of non-zero terms, hence M is integrable.

If condition (**b**) holds, then we continue by inserting a conditional expectation and using that the event $\{\tau >s\}$ is known at time s (note that $\tau$ is assumed to be a stopping time with respect to the filtration). This yields: ${\begin{aligned}\mathbb {E} [M]&=\mathbb {E} [|X_{0}|]+\sum _{s=0}^{\infty }\mathbb {E} {\bigl [}\underbrace {\mathbb {E} {\bigl [}|X_{s+1}-X_{s}|{\big |}{\mathcal {F}}_{s}{\bigr ]}\cdot \mathbf {1} _{\{\tau >s\}}} _{\leq \,c\,\mathbf {1} _{\{\tau >s\}}{\text{ a.s. by (b)}}}{\bigr ]}\\&\leq \mathbb {E} [|X_{0}|]+c\sum _{s=0}^{\infty }\mathbb {P} (\tau >s)\\&=\mathbb {E} [|X_{0}|]+c\,\mathbb {E} [\tau ]<\infty ,\\\end{aligned}}$ where a representation of the expected value of non-negative integer-valued random variables is used for the last equality.

Therefore, under any one of the three conditions in the theorem, the stopped process is dominated by an integrable random variable M . Since the stopped process $X^{\tau }$ converges almost surely to $X_{\tau }$ , the dominated convergence theorem implies: $\mathbb {E} [X_{\tau }]=\lim _{t\to \infty }\mathbb {E} [X_{t}^{\tau }].$

By the martingale property of the stopped process, $\mathbb {E} [X_{t}^{\tau }]=\mathbb {E} [X_{0}],\quad t\in \mathbb {N} _{0},$ hence $\mathbb {E} [X_{\tau }]=\mathbb {E} [X_{0}].$

Similarly, if X is a submartingale or supermartingale, respectively, change the equality in the last two formulas to the appropriate inequality.
