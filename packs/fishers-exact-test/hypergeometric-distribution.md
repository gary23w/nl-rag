---
title: "Hypergeometric distribution"
source: https://en.wikipedia.org/wiki/Hypergeometric_distribution
domain: fishers-exact-test
license: CC-BY-SA-4.0
tags: Fisher exact test, hypergeometric distribution, Barnard test, exact test
fetched: 2026-07-02
---

# Hypergeometric distribution

In probability theory and statistics, the **hypergeometric distribution** is a discrete probability distribution that describes the probability of k successes (random draws for which the object drawn has a specified feature) in n draws, *without* replacement, from a finite population of size N that contains exactly K objects with that feature, where in each draw is either a success or a failure. In contrast, the binomial distribution describes the probability of k successes in n draws *with* replacement.

## Definitions

### Probability mass function

The following conditions characterize the hypergeometric distribution:

- The result of each draw (the elements of the population being sampled) can be classified into one of two mutually exclusive categories (e.g. Pass/Fail or Employed/Unemployed).
- The probability of a success changes on each draw, as each draw decreases the population (*sampling without replacement* from a finite population).

A random variable X follows the hypergeometric distribution if its probability mass function (pmf) is given by

$p_{X}(k)=\Pr(X=k)={\frac {{\binom {K}{k}}{\binom {N-K}{n-k}}}{\binom {N}{n}}},$

where

- N is the population size,
- K is the number of success states in the population,
- n is the number of draws (i.e. quantity drawn in each trial),
- k is the number of observed successes,
- ${\textstyle \textstyle {a \choose b}}$ is a binomial coefficient.

The pmf is positive when $\max(0,n+K-N)\leq k\leq \min(K,n)$ .

A random variable distributed hypergeometrically with parameters N , K and n is written ${\textstyle X\sim \operatorname {Hypergeometric} (N,K,n)}$ and has probability mass function ${\textstyle p_{X}(k)}$ above.

### Combinatorial identities

As required, we have

$\sum _{0\leq k\leq {\textrm {min}}(n,K)}{{K \choose k}{N-K \choose n-k} \over {N \choose n}}=1,$

which essentially follows from Vandermonde's identity from combinatorics.

Also note that

${{K \choose k}{N-K \choose n-k} \over {N \choose n}}={{{n \choose k}{{N-n} \choose {K-k}}} \over {N \choose K}};$

This identity can be shown by expressing the binomial coefficients in terms of factorials and rearranging the latter. Additionally, it follows from the symmetry of the problem, described in two different but interchangeable ways.

For example, consider two rounds of drawing without replacement. In the first round, K out of N neutral marbles are drawn from an urn without replacement and coloured green. Then the colored marbles are put back. In the second round, n marbles are drawn without replacement and colored red. Then, the number of marbles with both colors on them (that is, the number of marbles that have been drawn twice) has the hypergeometric distribution. The symmetry in K and n stems from the fact that the two rounds are independent, and one could have started by drawing n balls and colouring them red first.

*Note that we are interested in the probability of k successes in n draws **without replacement**, since the probability of success on each trial is not the same, as the size of the remaining population changes as we remove each marble. Keep in mind not to confuse with the binomial distribution, which describes the probability of k successes in n draws **with replacement.***

## Properties

### Working example

The classical application of the hypergeometric distribution is **sampling without replacement**. Think of an urn with two colors of marbles, red and green. Define drawing a green marble as a success and drawing a red marble as a failure. Let *N* describe the number of **all marbles in the urn** (see contingency table below) and *K* describe the number of **green marbles**, then *N* − *K* corresponds to the number of **red marbles**. Now, standing next to the urn, you close your eyes and draw n marbles without replacement. Define *X* as a random variable whose outcome is *k*, the number of green marbles drawn in the experiment. This situation is illustrated by the following contingency table:

|   | drawn | not drawn | total |
|---|---|---|---|
| **green marbles** | *k* | *K* − *k* | *K* |
| **red marbles** | *n* − *k* | *N + k − n − K* | *N − K* |
| **total** | *n* | *N − n* | *N* |

Indeed, we are interested in calculating the probability of drawing k green marbles in n draws, given that there are K green marbles out of a total of N marbles. For this example, assume that there are **5** green and **45** red marbles in the urn. Standing next to the urn, you close your eyes and draw **10** marbles without replacement. What is the probability that exactly **4** of the **10** are green?

This problem is summarized by the following contingency table:

|   | drawn | not drawn | total |
|---|---|---|---|
| **green marbles** | *k* = **4** | *K* − *k* = **1** | *K* = **5** |
| **red marbles** | *n* − *k* = **6** | *N + k − n − K* = **39** | *N − K* = **45** |
| **total** | *n* = **10** | *N − n* = **40** | *N* = **50** |

To find the probability of **drawing k green marbles in exactly n draws out of N total draws**, we identify X as a hyper-geometric random variable to use the formula

$P(X=k)=f(k;N,K,n)={{{K \choose k}{{N-K} \choose {n-k}}} \over {N \choose n}}.$

To intuitively explain the given formula, consider the two symmetric problems represented by the identity

${{K \choose k}{N-K \choose n-k} \over {N \choose n}}={{{n \choose k}{{N-n} \choose {K-k}}} \over {N \choose K}}$

1. left-hand side - drawing a total of only n marbles out of the urn. We want to find the probability of the outcome of **drawing k green marbles out of K total green marbles, and drawing n-k red marbles out of N-K red marbles, in these n rounds.**
2. right hand side - alternatively, drawing all N marbles out of the urn. We want to find the probability of the outcome of drawing **k green marbles in n draws out of the total N draws, and K-k green marbles in the rest N-n draws.**

Back to the calculations, we use the formula above to calculate the probability of drawing exactly *k* green marbles

$P(X=4)=f(4;50,5,10)={{{5 \choose 4}{{45} \choose {6}}} \over {50 \choose 10}}={5\cdot 8145060 \over 10272278170}=0.003964583\dots .$

Intuitively we would expect it to be even more unlikely that all 5 green marbles will be among the 10 drawn.

$P(X=5)=f(5;50,5,10)={{{5 \choose 5}{{45} \choose {5}}} \over {50 \choose 10}}={1\cdot 1221759 \over 10272278170}=0.0001189375\dots ,$

As expected, the probability of drawing 5 green marbles is roughly 35 times less likely than that of drawing 4.

### Symmetries

Swapping the roles of green and red marbles:

$f(k;N,K,n)=f(n-k;N,N-K,n)$

Swapping the roles of drawn and not drawn marbles:

$f(k;N,K,n)=f(K-k;N,K,N-n)$

Swapping the roles of green and drawn marbles:

$f(k;N,K,n)=f(k;N,n,K)$

These symmetries generate the dihedral group $D_{4}$ .

### Order of draws

The probability of drawing any set of green and red marbles (the hypergeometric distribution) depends only on the numbers of green and red marbles, not on the order in which they appear; i.e., it is an exchangeable distribution. As a result, the probability of drawing a green marble in the $i^{\text{th}}$ draw is

$P(G_{i})={\frac {K}{N}}.$

This is an *ex ante* probability—that is, it is based on not knowing the results of the previous draws.

### Tail bounds

Let $X\sim \operatorname {Hypergeometric} (N,K,n)$ and $p=K/N$ . Then for $0<t<K/N$ we can derive the following bounds:

${\begin{aligned}\Pr[X\leq (p-t)n]&\leq e^{-n{\text{D}}(p-t\parallel p)}\leq e^{-2t^{2}n}\\\Pr[X\geq (p+t)n]&\leq e^{-n{\text{D}}(p+t\parallel p)}\leq e^{-2t^{2}n}\\\end{aligned}}\!$

where

$D(a\parallel b)=a\log {\frac {a}{b}}+(1-a)\log {\frac {1-a}{1-b}}$

is the Kullback–Leibler divergence and it is used that $D(a\parallel b)\geq 2(a-b)^{2}$ .

**Note**: In order to derive the previous bounds, one has to start by observing that $X={\frac {\sum _{i=1}^{n}Y_{i}}{n}}$ where $Y_{i}$ are *dependent* random variables with a specific distribution D . Because most of the theorems about bounds in sum of random variables are concerned with *independent* sequences of them, one has to first create a sequence $Z_{i}$ of *independent* random variables with the same distribution D and apply the theorems on $X'={\frac {\sum _{i=1}^{n}Z_{i}}{n}}$ . Then, it is proved from Hoeffding that the results and bounds obtained via this process hold for X as well.

If *n* is larger than *N*/2, it can be useful to apply symmetry to "invert" the bounds, which give you the following:

${\begin{aligned}\Pr[X\leq (p-t)n]&\leq e^{-(N-n){\text{D}}(p+{\tfrac {tn}{N-n}}||p)}\leq e^{-2t^{2}n{\tfrac {n}{N-n}}}\\\\\Pr[X\geq (p+t)n]&\leq e^{-(N-n){\text{D}}(p-{\tfrac {tn}{N-n}}||p)}\leq e^{-2t^{2}n{\tfrac {n}{N-n}}}\\\end{aligned}}\!$

## Statistical Inference

### Hypergeometric test

The **hypergeometric test** uses the hypergeometric distribution to measure the statistical significance of having drawn a sample consisting of a specific number of k successes (out of n total draws) from a population of size N containing K successes. In a test for over-representation of successes in the sample, the hypergeometric p-value is calculated as the probability of randomly drawing k or more successes from the population in n total draws. In a test for under-representation, the p-value is the probability of randomly drawing k or fewer successes.

The test based on the hypergeometric distribution (hypergeometric test) is identical to the corresponding one-tailed version of Fisher's exact test. Reciprocally, the p-value of a two-sided Fisher's exact test can be calculated as the sum of two appropriate hypergeometric tests (for more information see).

The test is often used to identify which sub-populations are over- or under-represented in a sample. This test has a wide range of applications. For example, a marketing group could use the test to understand their customer base by testing a set of known customers for over-representation of various demographic subgroups (e.g., women, people under 30).

Let $X\sim \operatorname {Hypergeometric} (N,K,n)$ and $p=K/N$ .

- If $n=1$ then X has a Bernoulli distribution with parameter p .
- Let Y have a binomial distribution with parameters n and p ; this models the number of successes in the analogous sampling problem *with* replacement. If N and K are large compared to n , and p is not close to 0 or 1, then X and Y have similar distributions, i.e., $P(X\leq k)\approx P(Y\leq k)$ .
- If n is large, N and K are large compared to n , and p is not close to 0 or 1, then

$P(X\leq k)\approx \Phi \left({\frac {k-np}{\sqrt {np(1-p)}}}\right)$

where $\Phi$ is the standard normal distribution function

- If the probabilities of drawing a green or red marble are not equal (e.g. because green marbles are bigger/easier to grasp than red marbles) then X has a noncentral hypergeometric distribution
- The beta-binomial distribution is a conjugate prior for the hypergeometric distribution.

The following table describes four distributions related to the number of successes in a sequence of draws:

|   | With replacements | No replacements |
|---|---|---|
| Given number of draws | binomial distribution | hypergeometric distribution |
| Given number of failures | negative binomial distribution | negative hypergeometric distribution |

### Multivariate hypergeometric distribution

The model of an urn with green and red marbles can be extended to the case where there are more than two colors of marbles. If there are *K**i* marbles of color *i* in the urn and you take *n* marbles at random without replacement, then the number of marbles of each color in the sample (*k*1, *k*2,..., *k**c*) has the multivariate hypergeometric distribution:

$\Pr(X_{1}=k_{1},\ldots ,X_{c}=k_{c})={\frac {\prod \limits _{i=1}^{c}{\binom {K_{i}}{k_{i}}}}{\binom {N}{n}}}$

This has the same relationship to the multinomial distribution that the hypergeometric distribution has to the binomial distribution—the multinomial distribution is the "with-replacement" distribution and the multivariate hypergeometric is the "without-replacement" distribution.

The properties of this distribution are given in the adjacent table, where *c* is the number of different colors and $N=\sum _{i=1}^{c}K_{i}$ is the total number of marbles in the urn.

#### Example

Suppose there are 5 black, 10 white, and 15 red marbles in an urn. If six marbles are chosen without replacement, the probability that exactly two of each color are chosen is

$P(2{\text{ black}},2{\text{ white}},2{\text{ red}})={{{5 \choose 2}{10 \choose 2}{15 \choose 2}} \over {30 \choose 6}}=0.079575596816976$

## Occurrence and applications

### Application to auditing elections

Election audits typically test a sample of machine-counted precincts to see if recounts by hand or machine match the original counts. Mismatches result in either a report or a larger recount. The sampling rates are usually defined by law, not statistical design, so for a legally defined sample size n, what is the probability of missing a problem which is present in K precincts, such as a hack or bug? This is the probability that *k* = 0 . Bugs are often obscure, and a hacker can minimize detection by affecting only a few precincts, which will still affect close elections, so a plausible scenario is for K to be on the order of 5% of N. Audits typically cover 1% to 10% of precincts (often 3%), so they have a high chance of missing a problem. For example, if a problem is present in 5 of 100 precincts, a 3% sample has 86% probability that *k* = 0 so the problem would not be noticed, and only 14% probability of the problem appearing in the sample (positive k ):

${\begin{aligned}\operatorname {\boldsymbol {\mathcal {P}}} \{\ X=0\ \}&={\frac {\ \left[\ {\binom {\text{Hack}}{0}}{\binom {N\ -\ {\text{Hack}}}{n\ -\ 0}}\ \right]\ }{\left[\ {\binom {N}{n}}\ \right]}}={\frac {\ \left[\ {\binom {N\ -\ {\text{Hack}}}{n}}\ \right]}{\ \left[\ {\binom {N}{n}}\ \right]\ }}={\frac {\ \left[\ {\frac {\ (N\ -\ {\text{Hack}})!\ }{n!(N\ -\ {\text{Hack}}-n)!}}\ \right]\ }{\left[\ {\frac {N!}{n!(N\ -\ n)!}}\ \right]}}={\frac {\ \left[\ {\frac {(N-{\text{Hack}})!}{(N\ -\ {\text{Hack}}\ -\ n)!}}\ \right]\ }{\left[\ {\frac {N!}{(N\ -\ n)!}}\ \right]}}\\[8pt]&={\frac {\ \left[\ {\binom {100-5}{3}}\ \right]\ }{\ \left[\ {\binom {100}{3}}\ \right]\ }}={\frac {\ \left[\ {\frac {(100-5)!}{(100-5-3)!}}\ \right]\ }{\left[\ {\frac {100!}{(100-3)!}}\ \right]}}={\frac {\ \left[\ {\frac {95!}{92!}}\ \right]\ }{\ \left[\ {\frac {100!}{97!}}\ \right]\ }}={\frac {\ 95\times 94\times 93\ }{100\times 99\times 98}}=86\%\end{aligned}}$

The sample would need 45 precincts in order to have probability under 5% that *k* = 0 in the sample, and thus have probability over 95% of finding the problem:

$\operatorname {\boldsymbol {\mathcal {P}}} \{\ X=0\ \}={\frac {\ \left[\ {\binom {100-5}{45}}\ \right]\ }{\left[\ {\binom {100}{45}}\ \right]}}={\frac {\ \left[\ {\frac {95!}{50!}}\ \right]\ }{\left[\ {\frac {100!}{55!}}\ \right]}}={\frac {\ 95\times 94\times \cdots \times 51\ }{\ 100\times 99\times \cdots \times 56\ }}={\frac {\ 55\times 54\times 53\times 52\times 51\ }{\ 100\times 99\times 98\times 97\times 96\ }}=4.6\%~.$

### Application to Texas hold'em poker

In hold'em poker players make the best hand they can combining the two cards in their hand with the 5 cards (community cards) eventually turned up on the table. The deck has 52 and there are 13 of each suit. For this example assume a player has 2 clubs in the hand and there are 3 cards showing on the table, 2 of which are also clubs. The player would like to know the probability of one of the next 2 cards to be shown being a club to complete the flush. (Note that the probability calculated in this example assumes no information is known about the cards in the other players' hands; however, experienced poker players may consider how the other players place their bets (check, call, raise, or fold) in considering the probability for each scenario. Strictly speaking, the approach to calculating success probabilities outlined here is accurate in a scenario where there is just one player at the table; in a multiplayer game this probability might be adjusted somewhat based on the betting play of the opponents.)

There are 4 clubs showing so there are 9 clubs still unseen. There are 5 cards showing (2 in the hand and 3 on the table) so there are $52-5=47$ still unseen.

The probability that exactly one of the next two cards turned is a club can be calculated using hypergeometric with $k=1,n=2,K=9$ and $N=47$ . (about 31.64%)

The probability that both of the next two cards turned are clubs can be calculated using hypergeometric with $k=2,n=2,K=9$ and $N=47$ . (about 3.33%)

The probability that neither of the next two cards turned are clubs can be calculated using hypergeometric with $k=0,n=2,K=9$ and $N=47$ . (about 65.03%)

### Application to Keno

The hypergeometric distribution is indispensable for calculating Keno odds. In Keno, 20 balls are randomly drawn from a collection of 80 numbered balls in a container, rather like American Bingo. Prior to each draw, a player selects a certain number of *spots* by marking a paper form supplied for this purpose. For example, a player might *play a 6-spot* by marking 6 numbers, each from a range of 1 through 80 inclusive. Then (after all players have taken their forms to a cashier and been given a duplicate of their marked form, and paid their wager) 20 balls are drawn. Some of the balls drawn may match some or all of the balls selected by the player. Generally speaking, the more *hits* (balls drawn that match player numbers selected) the greater the payoff.

For example, if a customer bets ("plays") $1 for a 6-spot (not an uncommon example) and hits 4 out of the 6, the casino would pay out $4. Payouts can vary from one casino to the next, but $4 is a typical value here. The probability of this event is:

$P(X=4)=f(4;80,6,20)={{{6 \choose 4}{{80-6} \choose {20-4}}} \over {80 \choose 20}}\approx 0.02853791$

Similarly, the chance for hitting 5 spots out of 6 selected is ${{{6 \choose 5}{{74} \choose {15}}} \over {80 \choose 20}}\approx 0.003095639$ while a typical payout might be $88. The payout for hitting all 6 would be around $1500 (probability ≈ 0.000128985 or 7752-to-1). The only other nonzero payout might be $1 for hitting 3 numbers (i.e., you get your bet back), which has a probability near 0.129819548.

Taking the sum of products of payouts times corresponding probabilities we get an expected return of 0.70986492 or roughly 71% for a 6-spot, for a house advantage of 29%. Other spots-played have a similar expected return. This very poor return (for the player) is usually explained by the large overhead (floor space, equipment, personnel) required for the game.
