---
title: "Condorcet paradox"
source: https://en.wikipedia.org/wiki/Condorcet_paradox
domain: social-choice-theory
license: CC-BY-SA-4.0
tags: social choice theory, arrow impossibility theorem, voting rule, gibbard satterthwaite theorem
fetched: 2026-07-02
---

# Condorcet paradox

In social choice theory, **Condorcet's voting paradox** (also called **Condorcet's paradox** or the **Condorcet paradox**) is a fundamental discovery by the Marquis de Condorcet that majority rule is inherently self-contradictory. The result implies that it is logically impossible for any voting system to guarantee that a winner will have support from a majority of voters; for example, there can be rock-paper-scissors scenarios where a majority of voters will prefer A to B, B to C, and also C to A, even if every voter's individual preferences are rational and avoid self-contradiction. Examples of Condorcet's paradox are called **Condorcet cycles** or **cyclic ties**.

In such a cycle, every possible choice is rejected by the electorate in favor of another alternative, who is preferred by more than half of all voters. Thus, any attempt to ground social decision-making in majoritarianism must accept such self-contradictions (commonly called spoiler effects). Systems that attempt to do so, while minimizing the rate of such self-contradictions, are called Condorcet methods.

Condorcet's paradox is a special case of Arrow's paradox, which shows that *any* kind of social decision-making process is either self-contradictory, a dictatorship, or incorporates information about the strength of different voters' preferences (e.g. cardinal utility or rated voting).

## History

Condorcet's paradox was first discovered by Catalan philosopher and theologian Ramon Llull in the 13th century, during his investigations into church governance, but his work was lost until the 21st century. The mathematician and political philosopher Marquis de Condorcet rediscovered the paradox in the late 18th century.

Condorcet's discovery means he arguably identified the key result of Arrow's impossibility theorem, albeit under stronger conditions than required by Arrow: Condorcet cycles create situations where any ranked voting system that respects majorities must have a spoiler effect.

## Example

Suppose we have three candidates, A, B, and C, and that there are three voters with preferences as follows:

| Voter | First preference | Second preference | Third preference |
|---|---|---|---|
| Voter 1 | A | B | C |
| Voter 2 | B | C | A |
| Voter 3 | C | A | B |

If C is chosen as the winner, it can be argued that B should win instead, since two voters (1 and 2) prefer B to C and only one voter (3) prefers C to B. However, by the same argument A is preferred to B, and C is preferred to A, by a margin of two to one on each occasion. Thus the society's preferences show cycling: A is preferred over B which is preferred over C which is preferred over A.

As a result, any attempt to appeal to the principle of majority rule will lead to logical self-contradiction. Regardless of which alternative we select, we can find another alternative that would be preferred by most voters.

### Practical scenario

The voters in Cactus County prefer the incumbent county executive **Alex** of the Farmers' Party over rival **Beatrice** of the Solar Panel Party by about a 2-to-1 margin. This year a third candidate, **Charlie**, is running as an independent. Charlie is a wealthy and outspoken businessman, of whom the voters hold polarized views.

The voters divide into three groups:

- Group 1 revere Charlie for saving the high school football team. They rank Charlie first, and then Alex above Beatrice as usual (**CAB**).
- Group 2 despise Charlie for his sharp business practices. They rank Charlie *last*, and then Alex above Beatrice as usual (**ABC**).
- Group 3 are Beatrice's core supporters. They want the Farmers' Party out of office in favor of the Solar Panel Party, and regard Charlie's candidacy as a sideshow. They rank Beatrice first and Alex last as usual, and Charlie second by default (**BCA**).

Therefore a majority of voters prefer Alex to Beatrice (A > B), as they always have. A majority of voters are either Beatrice-lovers or Charlie-haters, so prefer Beatrice to Charlie (B > C). And a majority of voters are either Charlie-lovers or Alex-haters, so prefer Charlie to Alex (C > A). Combining the three preferences gives us A > B > C > A, a Condorcet cycle.

## Likelihood

It is possible to estimate the probability of the paradox by extrapolating from real election data, or using mathematical models of voter behavior, though the results depend strongly on which model is used.

### Impartial culture model

We can calculate the probability of seeing the paradox for the special case where voter preferences are uniformly distributed among the candidates. (This is the "impartial culture" model, which is known to be a "worst-case scenario"—most models show substantially lower probabilities of Condorcet cycles.)

For n voters providing a preference list of three candidates A, B, C, we write $X_{n}$ (resp. $Y_{n}$ , $Z_{n}$ ) the random variable equal to the number of voters who placed A in front of B (respectively B in front of C, C in front of A). The sought probability is $p_{n}=2P(X_{n}>n/2,Y_{n}>n/2,Z_{n}>n/2)$ (we double because there is also the symmetric case A> C> B> A). We show that, for odd n , $p_{n}=3q_{n}-1/2$ where $q_{n}=P(X_{n}>n/2,Y_{n}>n/2)$ which makes one need to know only the joint distribution of $X_{n}$ and $Y_{n}$ .

If we put $p_{n,i,j}=P(X_{n}=i,Y_{n}=j)$ , we show the relation which makes it possible to compute this distribution by recurrence:

$p_{n+1,i,j}={1 \over 6}p_{n,i,j}+{1 \over 3}p_{n,i-1,j}+{1 \over 3}p_{n,i,j-1}+{1 \over 6}p_{n,i-1,j-1}.$

The following results are then obtained:

| n | 3 | 101 | 201 | 301 | 401 | 501 | 601 |
|---|---|---|---|---|---|---|---|
| $p_{n}$ | 5.556% | 8.690% | 8.732% | 8.746% | 8.753% | 8.757% | 8.760% |

The sequence seems to be tending towards a finite limit.

Using the central limit theorem, we show that $q_{n}$ tends to $q={\frac {1}{4}}P\left(|T|>{\frac {\sqrt {2}}{4}}\right),$ where T is a variable following a Cauchy distribution, which gives

$q={\dfrac {1}{2\pi }}\int _{{\sqrt {2}}/4}^{+\infty }{\frac {dt}{1+t^{2}}}={\dfrac {\arctan 2{\sqrt {2}}}{2\pi }}={\dfrac {\arccos {\frac {1}{3}}}{2\pi }}$ (constant quoted in the OEIS).

The asymptotic probability of encountering the Condorcet paradox is therefore ${{3\arccos {1 \over 3}} \over {2\pi }}-{1 \over 2}={\arcsin {{\sqrt {6}} \over 9} \over \pi }$ which gives the value 8.77%.

Some results for the case of more than three candidates have been calculated and simulated. The simulated likelihood for an impartial culture model with 25 voters increases with the number of candidates:

| 3 | 4 | 5 | 7 | 10 |
|---|---|---|---|---|
| 8.4% | 16.6% | 24.2% | 35.7% | 47.5% |

The likelihood of a Condorcet cycle for related models approach these values for three-candidate elections with large electorates:

- Impartial anonymous culture (IAC): 6.25%
- Uniform culture (UC): 6.25%
- Maximal culture condition (MC): 9.17%

All of these models are unrealistic, but can be investigated to establish an upper bound on the likelihood of a cycle.

### Group coherence models

When modeled with more realistic voter preferences, Condorcet paradoxes in elections with a small number of candidates and a large number of voters become very rare.

### Spatial model

A study of three-candidate elections analyzed 12 different models of voter behavior, and found the spatial model of voting to be the most accurate to real-world ranked-ballot election data. Analyzing this spatial model, they found the likelihood of a cycle to decrease to zero as the number of voters increases, with likelihoods of 5% for 100 voters, 0.5% for 1000 voters, and 0.06% for 10,000 voters.

Another spatial model found likelihoods of 2% or less in all simulations of 201 voters and 5 candidates, whether two or four-dimensional, with or without correlation between dimensions, and with two different dispersions of candidates.

### Empirical studies

Many attempts have been made at finding empirical examples of the paradox. Empirical identification of a Condorcet paradox presupposes extensive data on the decision-makers' preferences over all alternatives—something that is only very rarely available.

While examples of the paradox seem to occur occasionally in small settings (e.g., parliaments) very few examples have been found in larger groups (e.g. electorates), although some have been identified.

A summary of 37 individual studies, covering a total of 265 real-world elections, large and small, found 25 instances of a Condorcet paradox, for a total likelihood of 9.4% (and this may be a high estimate, since cases of the paradox are more likely to be reported on than cases without).

An analysis of 883 three-candidate elections extracted from 84 real-world ranked-ballot elections of the Electoral Reform Society found a Condorcet cycle likelihood of 0.7%. These derived elections had between 350 and 1,957 voters. A similar analysis of data from the 1970–2004 American National Election Studies thermometer scale surveys found a Condorcet cycle likelihood of 0.4%. These derived elections had between 759 and 2,521 "voters".

Andrew Myers, who operates the Condorcet Internet Voting Service, analyzed 10,354 nonpolitical CIVS elections and found cycles in 17% of elections with at least 10 votes, with the figure dropping to 2.1% for elections with at least 100 votes, and 1.2% for ≥300 votes.

### Real world instances

A database of 189 ranked United States elections from 2004 to 2022 contained only one Condorcet cycle: the 2021 Minneapolis City Council election in Ward 2, with a narrow circular tie between candidates of the Green Party (Cam Gordon), the Minnesota Democratic–Farmer–Labor Party (Yusra Arab), and an independent democratic socialist (Robin Wonsley). Voters' preferences were non-transitive: Arab was preferred over Gordon, Gordon over Wonsley, and Wonsley over Arab, creating a cyclical pattern with no clear winner. Additionally, the election exhibited a downward monotonicity paradox, as well as a paradox akin to Simpson’s paradox.

A second instance of a Condorcet cycle was found in the 2022 District 4 School Director election in Oakland, California. Manigo was preferred to Hutchinson, Hutchinson to Resnick, and Resnick to Manigo. Like in Minneapolis, the margins were quite narrow: for instance, 11370 voters preferred Manigo to Hutchinson while 11322 preferred Hutchinson to Manigo.

Another instance of a Condorcet cycle was with the seat of Prahran in the 2014 Victorian state election, with a narrow circular tie between the Greens, Liberal, and Labor candidates. The Greens candidate, who was initially third on primary votes, defeated the Liberal candidate by less than 300 votes. However, if the contest had been between Labor and Liberal, the Liberal candidate would have won by 25 votes. While a Greens vs Labor count was not conducted, Liberal preferences tend to flow more towards Labor than Greens in other cases (including in the seat of Richmond in the same election), meaning that Labor would have very likely been preferred to the Greens. This means there was a circular pattern, with the Greens preferred over Liberal, who were preferred over Labor, who were preferred over the Greens.

## Implications

When a Condorcet method is used to determine an election, the voting paradox of cyclical societal preferences implies that the election has no Condorcet winner: no candidate who can win a one-on-one election against each other candidate. There will still be a smallest group of candidates, known as the Smith set, such that each candidate in the group can win a one-on-one election against each of the candidates outside the group. The several variants of the Condorcet method differ on how they resolve such ambiguities when they arise to determine a winner. The Condorcet methods which always elect someone from the Smith set when there is no Condorcet winner are known as Smith-efficient. Note that using only rankings, there is no fair and deterministic resolution to the trivial example given earlier because each candidate is in an exactly symmetrical situation.

Situations having the voting paradox can cause voting mechanisms to violate the axiom of independence of irrelevant alternatives—the choice of winner by a voting mechanism could be influenced by whether or not a losing candidate is available to be voted for.

### Two-stage voting processes

One important implication of the possible existence of the voting paradox in a practical situation is that in a paired voting process like those of standard parliamentary procedure, the eventual winner will depend on the way the majority votes are ordered. For example, say a popular bill is set to pass, before some other group offers an amendment; this amendment passes by majority vote. This may result in a majority of a legislature rejecting the bill as a whole, thus creating a paradox (where a popular amendment to a popular bill has made it unpopular). This logical inconsistency is the origin of the poison pill amendment, which deliberately engineers a false Condorcet cycle to kill a bill. Likewise, the order of votes in a legislature can be manipulated by the person arranging them to ensure their preferred outcome wins.

Despite frequent objections by social choice theorists about the logically incoherent results of such procedures, and the existence of better alternatives for choosing between multiple versions of a bill, the procedure of pairwise majority-rule is widely-used and is codified into the by-laws or parliamentary procedures of almost every kind of deliberative assembly.

### Spoiler effects

Condorcet paradoxes imply that majoritarian methods fail independence of irrelevant alternatives. Label the three candidates in a race *Rock*, *Paper*, and *Scissors*. In one-on-one races, Rock loses to Paper, Paper loses to Scissors, and Scissors loses to Rock.

Without loss of generality, say that Rock wins the election with a certain method. Then, Scissors is a spoiler candidate for Paper; if Scissors were to drop out, Paper would win the only one-on-one race (Paper defeats Rock). The same reasoning applies regardless of the winner.

This example also shows why Condorcet elections are rarely (if ever) spoiled; spoilers can *only* happen when there is no Condorcet winner. Condorcet cycles are rare in large elections, and the median voter theorem shows that cycles are impossible whenever candidates are arrayed on a left-right spectrum.
