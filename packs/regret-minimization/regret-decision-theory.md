---
title: "Regret (decision theory)"
source: https://en.wikipedia.org/wiki/Regret_(decision_theory)
domain: regret-minimization
license: CC-BY-SA-4.0
tags: regret minimization, multi armed bandit, no regret dynamics, thompson sampling
fetched: 2026-07-02
---

# Regret (decision theory)

In decision theory, **regret aversion** (or **anticipated regret**) describes how the human emotional response of regret can influence decision-making under uncertainty. When individuals make choices without complete information, they often experience regret if they later discover that a different choice would have produced a better outcome. This regret can be quantified as the difference in value between the actual decision made and what would have been the optimal decision in hindsight.

Unlike traditional models that consider regret as merely a post-decision emotional response, the theory of regret aversion proposes that decision-makers actively anticipate potential future regret and incorporate this anticipation into their current decision-making process. This anticipation can lead individuals to make choices specifically designed to minimize the possibility of experiencing regret later, even if those choices are not optimal from a purely probabilistic expected-value perspective.

Regret is a powerful negative emotion with significant social and reputational implications, playing a central role in how humans learn from experience and in the psychology of risk aversion. The conscious anticipation of regret creates a feedback loop that elevates regret from being simply an emotional reaction—often modeled as mere human behavior—into a key factor in rational choice behavior that can be formally modeled in decision theory.

This anticipatory mechanism helps explain various observed decision patterns that deviate from standard expected utility theory, including status quo bias, inaction inertia, and the tendency to avoid decisions that might lead to easily imagined counterfactual scenarios where a better outcome would have occurred.

## Description

Regret theory is a model in theoretical economics simultaneously developed in 1982 by Graham Loomes and Robert Sugden, David E. Bell, and Peter C. Fishburn. Regret theory models choice under uncertainty taking into account the effect of anticipated regret. Subsequently, several other authors improved upon it.

It incorporates a regret term in the utility function which depends negatively on the realized outcome and positively on the best alternative outcome given the uncertainty resolution. This regret term is usually an increasing, continuous and non-negative function subtracted to the traditional utility index. These types of preferences always violate transitivity in the traditional sense, although most satisfy a weaker version.

For independent lotteries and when regret is evaluated over the difference between utilities and then averaged over all combinations of outcomes, the regret can still be transitive but for only specific form of regret functional. It is shown that only hyperbolic sine function will maintain this property. This form of regret inherits most of desired features, such as holding right preferences in face of first order stochastic dominance, risk averseness for logarithmic utilities and the ability to explain Allais paradox.

Regret aversion is not only a theoretical economics model, but a cognitive bias occurring as a decision has been made to abstain from regretting an alternative decision. To better preface, regret aversion can be seen through fear by either commission or omission; the prospect of committing to a failure or omitting an opportunity that we seek to avoid. Regret, feeling sadness or disappointment over something that has happened, can be rationalized for a certain decision, but can guide preferences and can lead people astray. This contributes to the spread of disinformation because things are not seen as one's personal responsibility.

## Evidence

Several experiments over both incentivized and hypothetical choices attest to the magnitude of this effect.

Experiments in first price auctions show that by manipulating the feedback the participants expect to receive, significant differences in the average bids are observed. In particular, "Loser's regret" can be induced by revealing the winning bid to all participants in the auction, and thus revealing to the losers whether they would have been able to make a profit and how much could it have been (a participant that has a valuation of $50, bids $30 and finds out the winning bid was $35 will also learn that he or she could have earned as much as $15 by bidding anything over $35.) This in turn allows for the possibility of regret and if bidders correctly anticipate this, they would tend to bid higher than in the case where no feedback on the winning bid is provided in order to decrease the possibility of regret.

In decisions over lotteries, experiments also provide supporting evidence of anticipated regret. As in the case of first price auctions, differences in feedback over the resolution of the uncertainty can cause the possibility of regret and if this is anticipated, it may induce different preferences. For example, when faced with a choice between $40 with certainty and a coin toss that pays $100 if the outcome is guessed correctly and $0 otherwise, not only does the certain payment alternative minimizes the risk but also the possibility of regret, since typically the coin will not be tossed (and thus the uncertainty not resolved) while if the coin toss is chosen, the outcome that pays $0 will induce regret. If the coin is tossed regardless of the chosen alternative, then the alternative payoff will always be known and then there is no choice that will eliminate the possibility of regret.

### Anticipated regret versus experienced regret

Anticipated regret tends to be overestimated for both choices and actions over which people perceive themselves to be responsible. People are particularly likely to overestimate the regret they will feel when missing a desired outcome by a narrow margin. In one study, commuters predicted they would experience greater regret if they missed a train by 1 minute more than missing a train by 5 minutes, for example, but commuters who actually missed their train by 1 or 5 minutes experienced (equal and) lower amounts of regret. Commuters appeared to overestimate the regret they would feel when missing the train by a narrow margin, because they tended to underestimate the extent to which they would attribute missing the train to external causes (e.g., missing their wallet or spending less time in the shower).

## Applications

Besides the traditional setting of choices over lotteries, regret aversion has been proposed as an explanation for the typically observed overbidding in first price auctions, and the disposition effect, among others.

## Minimax regret

The minimax regret approach is to minimize the worst-case regret, originally presented by Leonard Savage in 1951. The aim of this is to perform as closely as possible to the optimal course. Since the minimax criterion applied here is to the regret (difference or ratio of the payoffs) rather than to the payoff itself, it is not as pessimistic as the ordinary minimax approach. Similar approaches have been used in a variety of areas such as:

- Hypothesis testing
- Prediction
- Economics

One benefit of minimax (as opposed to expected regret) is that it is independent of the probabilities of the various outcomes: thus if regret can be accurately computed, one can reliably use minimax regret. However, probabilities of outcomes are hard to estimate.

This differs from the standard minimax approach in that it uses *differences* or *ratios* between outcomes, and thus requires interval or ratio measurements, as well as ordinal measurements (ranking), as in standard minimax.

### Example

Suppose an investor has to choose between investing in stocks, bonds or the money market, and the total return depends on what happens to interest rates. The following table shows some possible returns:

| Return | Interest rates rise | Static rates | Interest rates fall | *Worst return* |
|---|---|---|---|---|
| Stocks | −4 | 4 | 12 | *−4* |
| Bonds | −2 | 3 | 8 | *−2* |
| Money market | 3 | 2 | 1 | *1* |
| *Best return* | *3* | *4* | *12* |   |

The crude maximin choice based on returns would be to invest in the money market, ensuring a return of at least 1. However, if interest rates fell then the regret associated with this choice would be large. This would be 11, which is the difference between the 12 which could have been received if the outcome had been known in advance and the 1 received. A mixed portfolio of about 11.1% in stocks and 88.9% in the money market would have ensured a return of at least 2.22; but, if interest rates fell, there would be a regret of about 9.78.

The regret table for this example, constructed by subtracting actual returns from best returns, is as follows:

| Regret | Interest rates rise | Static rates | Interest rates fall | *Worst regret* |
|---|---|---|---|---|
| Stocks | 7 | 0 | 0 | *7* |
| Bonds | 5 | 1 | 4 | *5* |
| Money market | 0 | 2 | 11 | *11* |

Therefore, using a minimax choice based on regret, the best course would be to invest in bonds, ensuring a regret of no worse than 5. A mixed investment portfolio would do even better: 61.1% invested in stocks, and 38.9% in the money market would produce a regret no worse than about 4.28.

## Example: Linear estimation setting

What follows is an illustration of how the concept of regret can be used to design a linear estimator. In this example, the problem is to construct a linear estimator of a finite-dimensional parameter vector x from its noisy linear measurement with known noise covariance structure. The loss of reconstruction of x is measured using the mean-squared error (MSE). The unknown parameter vector is known to lie in an ellipsoid E centered at zero. The regret is defined to be the difference between the MSE of the linear estimator that doesn't know the parameter x , and the MSE of the linear estimator that knows x . Also, since the estimator is restricted to be linear, the zero MSE cannot be achieved in the latter case. In this case, the solution of a convex optimization problem gives the optimal, minimax regret-minimizing linear estimator, which can be seen by the following argument.

According to the assumptions, the observed vector y and the unknown deterministic parameter vector x are tied by the linear model

$y=Hx+w$

where H is a known $n\times m$ matrix with full column rank m , and w is a zero mean random vector with a known covariance matrix $C_{w}$ .

Let

${\hat {x}}=Gy$

be a linear estimate of x from y , where G is some $m\times n$ matrix. The MSE of this estimator is given by

$MSE=E\left(||{\hat {x}}-x||^{2}\right)=Tr(GC_{w}G^{*})+x^{*}(I-GH)^{*}(I-GH)x.$

Since the MSE depends explicitly on x it cannot be minimized directly. Instead, the concept of regret can be used in order to define a linear estimator with good MSE performance. To define the regret here, consider a linear estimator that knows the value of the parameter x , i.e., the matrix G can explicitly depend on x :

${\hat {x}}^{o}=G(x)y.$

The MSE of ${\hat {x}}^{o}$ is

$MSE^{o}=E\left(||{\hat {x}}^{o}-x||^{2}\right)=Tr(G(x)C_{w}G(x)^{*})+x^{*}(I-G(x)H)^{*}(I-G(x)H)x.$

To find the optimal $G(x)$ , $MSE^{o}$ is differentiated with respect to G and the derivative is equated to 0 getting

$G(x)=xx^{*}H^{*}(C_{w}+Hxx^{*}H^{*})^{-1}.$

Then, using the Matrix Inversion Lemma

$G(x)={\frac {1}{1+x^{*}H^{*}C_{w}^{-1}Hx}}xx^{*}H^{*}C_{w}^{-1}.$

Substituting this $G(x)$ back into $MSE^{o}$ , one gets

$MSE^{o}={\frac {x^{*}x}{1+x^{*}H^{*}C_{w}^{-1}Hx}}.$

This is the smallest MSE achievable with a linear estimate that knows x . In practice this MSE cannot be achieved, but it serves as a bound on the optimal MSE. The regret of using the linear estimator specified by G is equal to

$R(x,G)=MSE-MSE^{o}=Tr(GC_{w}G^{*})+x^{*}(I-GH)^{*}(I-GH)x-{\frac {x^{*}x}{1+x^{*}H^{*}C_{w}^{-1}Hx}}.$

The minimax regret approach here is to minimize the worst-case regret, i.e., $\sup _{x\in E}R(x,G).$ This will allow a performance as close as possible to the best achievable performance in the worst case of the parameter x . Although this problem appears difficult, it is an instance of convex optimization and in particular a numerical solution can be efficiently calculated. Similar ideas can be used when x is random with uncertainty in the covariance matrix.

## Regret in principal-agent problems

Camara, Hartline and Johnsen study principal-agent problems. These are incomplete-information games between two players called *Principal* and *Agent*, whose payoffs depend on a state of nature known only by the Agent. The Principal commits to a policy, then the agent responds, and then the state of nature is revealed. They assume that the principal and agent interact repeatedly, and may learn over time from the state history, using reinforcement learning. They assume that the agent is driven by regret-aversion. In particular, the agent minimizes his *counterfactual internal regret*. Based on this assumption, they develop mechanisms that minimize the principal's regret.

Collina, Roth and Shao improve their mechanism both in running-time and in the bounds for regret (as a function of the number of distinct states of nature).
