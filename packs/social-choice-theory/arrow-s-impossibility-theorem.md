---
title: "Arrow's impossibility theorem"
source: https://en.wikipedia.org/wiki/Arrow's_impossibility_theorem
domain: social-choice-theory
license: CC-BY-SA-4.0
tags: social choice theory, arrow impossibility theorem, voting rule, gibbard satterthwaite theorem
fetched: 2026-07-02
---

# Arrow's impossibility theorem

**Arrow's impossibility theorem** is a key result in social choice theory, proved by American economist Kenneth Arrow. It shows that no procedure for group decision-making under ordinal utilities can satisfy the requirements of rational choice theory. Specifically, no such rule can satisfy independence of irrelevant alternatives, the principle that a choice between two alternatives *A* and *B* should not depend on the quality of some third, unrelated option, *C*.

The result is often cited in discussions of voting rules, where it shows no ranked voting rule can eliminate the spoiler effect. This result was first shown by the Marquis de Condorcet, whose voting paradox showed the impossibility of logically-consistent majority rule; Arrow's theorem generalizes Condorcet's findings to include non-majoritarian rules like collective leadership or consensus decision-making.

While the impossibility theorem shows all ranked voting rules must have spoilers, the frequency of spoilers differs dramatically by rule. Plurality-rule methods like choose-one and ranked-choice (instant-runoff) voting are highly sensitive to spoilers, creating them even in some situations where they are not mathematically necessary (e.g. in center squeezes). In contrast, majority-rule (Condorcet) methods of ranked voting uniquely minimize the number of spoiled elections by restricting them to voting cycles, which are rare in ideologically-driven elections. Under some models of voter preferences (like the left-right spectrum assumed in the median voter theorem), spoilers disappear entirely for these methods.

Rated voting rules, where voters assign a separate grade to each candidate, are not affected by Arrow's theorem. Arrow initially asserted the information provided by these systems was meaningless and therefore could not be used to prevent paradoxes, leading him to overlook them. However, Arrow would later describe this as a mistake, admitting rules based on cardinal utilities (such as score and approval voting) are not subject to his theorem.

## Background

When Kenneth Arrow proved his theorem in 1950, it inaugurated the modern field of social choice theory, a branch of welfare economics studying mechanisms to aggregate preferences and beliefs across a society. Such a mechanism of study can be a market, voting system, constitution, or even a moral or ethical framework.

### Axioms of voting systems

#### Preferences

In the context of Arrow's theorem, citizens are assumed to have ordinal preferences, i.e. orderings of candidates. If *A* and *B* are different candidates or alternatives, then $A\succ B$ means *A* is preferred to *B*. Individual preferences (or ballots) are required to satisfy intuitive properties of orderings, e.g. they must be transitive—if $A\succeq B$ and $B\succeq C$ , then $A\succeq C$ . The social choice function is then a mathematical function that maps the individual orderings to a new ordering that represents the preferences of all of society.

#### Basic assumptions

Arrow's theorem assumes as background that any non-degenerate social choice rule will satisfy:

- ***Unrestricted domain*** – the social choice function is a total function over the domain of all possible orderings of outcomes, not just a partial function.
  - In other words, the system must always make *some* choice, and cannot simply "give up" when the voters have unusual opinions.
  - Without this assumption, majority rule satisfies Arrow's axioms by "giving up" whenever there is a Condorcet cycle.
- ***Non-dictatorship*** – the system does not depend on only one voter's ballot.
  - This weakens *anonymity* (one vote, one value) to allow rules that treat voters unequally.
  - It essentially defines *social* choices as those depending on more than one person's input.
- ***Non-imposition*** – the system does not ignore the voters entirely when choosing between some pairs of candidates.
  - In other words, it is possible for any candidate to defeat any other candidate, given some combination of votes.
  - This is often replaced with the stronger **Pareto efficiency** axiom: if every voter prefers *A* over *B*, then *A* should defeat *B*. However, the weaker non-imposition condition is sufficient.

Arrow's original statement of the theorem included non-negative responsiveness as a condition, i.e., that *increasing* the rank of an outcome should not make them *lose*—in other words, that a voting rule shouldn't penalize a candidate for being more popular. However, this assumption is not needed or used in his proof (except to derive the weaker condition of Pareto efficiency), and Arrow later corrected his statement of the theorem to remove the inclusion of this condition.

#### Independence

A commonly-considered axiom of rational choice is *independence of irrelevant alternatives* (IIA), which says that when deciding between *A* and *B*, one's opinion about a third option *C* should not affect their decision.

- ***Independence of irrelevant alternatives (IIA)*** – the social preference between candidate *A* and candidate *B* should only depend on the individual preferences between *A* and *B*.
  - In other words, the social preference should not change from $A\succ B$ to $B\succ A$ if voters change their preference about whether $A\succ C$ .
  - This is equivalent to the claim about independence of spoiler candidates when using the standard construction of a placement function.

IIA is sometimes illustrated with a short joke attributed, perhaps apocryphally, to philosopher Sidney Morgenbesser:

Morgenbesser, ordering dessert, is told by a waitress that he can choose between blueberry or apple pie. He orders apple. Soon the waitress comes back and explains cherry pie is also an option. Morgenbesser replies "In that case, I'll have blueberry."

Arrow's theorem shows that if a society wishes to make decisions while always avoiding such self-contradictions, it cannot use ranked information alone.

## Theorem

### Intuitive argument

Condorcet's example is already enough to see the impossibility of a fair ranked voting system, given stronger conditions for fairness than Arrow's theorem assumes. Suppose we have three candidates ( A , B , and C ) and three voters whose preferences are as follows:

| Voter | First preference | Second preference | Third preference |
|---|---|---|---|
| Voter 1 | A | B | C |
| Voter 2 | B | C | A |
| Voter 3 | C | A | B |

If C is chosen as the winner, it can be argued any fair voting system would say B should win instead, since two voters (1 and 2) prefer B to C and only one voter (3) prefers C to B . However, by the same argument A is preferred to B , and C is preferred to A , by a margin of two to one on each occasion. Thus, even though each individual voter has consistent preferences, the preferences of society are contradictory: A is preferred over B which is preferred over C which is preferred over A .

Because of this example, some authors credit Condorcet with having given an intuitive argument that presents the core of Arrow's theorem. However, Arrow's theorem is substantially more general; it applies to methods of making decisions other than one-person-one-vote elections, such as markets or weighted voting, based on ranked ballots.

### Formal statement

Let A be a set of *alternatives*. A voter's preferences over A are a complete and transitive binary relation on A (sometimes called a total preorder), that is, a subset R of $A\times A$ satisfying:

1. (Transitivity) If $(\mathbf {a} ,\mathbf {b} )$ is in R and $(\mathbf {b} ,\mathbf {c} )$ is in R , then $(\mathbf {a} ,\mathbf {c} )$ is in R ,
2. (Completeness) At least one of $(\mathbf {a} ,\mathbf {b} )$ or $(\mathbf {b} ,\mathbf {a} )$ must be in R .

The element $(\mathbf {a} ,\mathbf {b} )$ being in R is interpreted to mean that alternative $\mathbf {a}$ is preferred to or indifferent to alternative $\mathbf {b}$ . This situation is often denoted $\mathbf {a} \succsim \mathbf {b}$ or $\mathbf {a} R\mathbf {b}$ . The symmetric part of R yields the indifference relation I . This is written as $\mathbf {a} \sim \mathbf {b}$ or $\mathbf {a} I\mathbf {b}$ if and only if $(\mathbf {a} ,\mathbf {b} )$ and $(\mathbf {b} ,\mathbf {a} )$ are both in R . The asymmetric part of R yields the (strict) preference relation P . This is written as $\mathbf {a} \succ \mathbf {b}$ or $\mathbf {a} P\mathbf {b}$ if and only if $(\mathbf {a} ,\mathbf {b} )$ is in R and $(\mathbf {b} ,\mathbf {a} )$ is not in R . In the following, preference of one alternative over another denotes strict preference.

Denote the set of all preferences on A by $\Pi (A)$ . Equivalently, $\Pi (A)$ is the set of rankings of the alternatives in A from top to bottom, with ties allowed. Let N be a positive integer. An *ordinal (ranked)* *social welfare function* is a function

$\mathrm {F} :\Pi (A)^{N}\to \Pi (A)$

which aggregates voters' preferences into a single preference on A . An N -tuple $(R_{1},\ldots ,R_{N})\in \Pi (A)^{N}$ of voters' preferences is called a *preference profile*.

**Arrow's impossibility theorem**: If there are at least three alternatives, then there is no social welfare function satisfying all three of the conditions listed below:

**Pareto efficiency**

If alternative

$\mathbf {a}$

is preferred to

$\mathbf {b}$

for all orderings

$R_{1},\ldots ,R_{N}$

, then

$\mathbf {a}$

is preferred to

$\mathbf {b}$

by

$F(R_{1},R_{2},\ldots ,R_{N})$

.

**Non-dictatorship**

There is no individual

i

whose preferences always prevail. That is, there is no

$i\in \{1,\ldots ,N\}$

such that for all

$(R_{1},\ldots ,R_{N})\in \Pi (A)^{N}$

and all

$\mathbf {a}$

and

$\mathbf {b}$

, when

$\mathbf {a}$

is preferred to

$\mathbf {b}$

by

$R_{i}$

then

$\mathbf {a}$

is preferred to

$\mathbf {b}$

by

$F(R_{1},R_{2},\ldots ,R_{N})$

.

**Independence of irrelevant alternatives**

For two preference profiles

$(R_{1},\ldots ,R_{N})$

and

$(S_{1},\ldots ,S_{N})$

such that for all individuals

i

, alternatives

$\mathbf {a}$

and

$\mathbf {b}$

have the same order in

$R_{i}$

as in

$S_{i}$

, alternatives

$\mathbf {a}$

and

$\mathbf {b}$

have the same order in

$F(R_{1},\ldots ,R_{N})$

as in

$F(S_{1},\ldots ,S_{N})$

.

### Formal proof

| Proof by decisive coalition |
|---|
| Arrow's proof used the concept of *decisive coalitions*. Definition: A subset of voters is a **coalition**. A coalition is **decisive over an ordered pair $(x,y)$** if, when everyone in the coalition ranks $x\succ _{i}y$ , society overall will always rank $x\succ y$ . A coalition is **decisive** if and only if it is decisive over all ordered pairs. Our goal is to prove that the **decisive coalition** contains only one voter, who controls the outcome—in other words, a dictator. The following proof is a simplification taken from Amartya Sen and Ariel Rubinstein. The simplified proof uses an additional concept: A coalition is **weakly decisive** over $(x,y)$ if and only if when every voter i in the coalition ranks $x\succ _{i}y$ , *and* every voter j outside the coalition ranks $y\succ _{j}x$ , then $x\succ y$ . Thenceforth assume that the social choice system satisfies unrestricted domain, Pareto efficiency, and IIA. Also assume that there are at least 3 distinct outcomes. **Field expansion lemma**—if a coalition G is weakly decisive over $(x,y)$ for some $x\neq y$ , then it is decisive. **Proof** Let z be an outcome distinct from $x,y$ . Claim: G is decisive over $(x,z)$ . Let everyone in G vote x over z . By IIA, changing the votes on y does not matter for $x,z$ . So change the votes such that $x\succ _{i}y\succ _{i}z$ in G and $y\succ _{i}x$ and $y\succ _{i}z$ outside of G . By Pareto, $y\succ z$ . By coalition weak-decisiveness over $(x,y)$ , $x\succ y$ . Thus $x\succ z$ . $\square$ Similarly, G is decisive over $(z,y)$ . By iterating the above two claims (note that decisiveness implies weak-decisiveness), we find that G is decisive over all ordered pairs in $\{x,y,z\}$ . Then iterating that, we find that G is decisive over all ordered pairs in X . **Group contraction lemma**—If a coalition is decisive, and has size $\geq 2$ , then it has a proper subset that is also decisive. **Proof** Let G be a coalition with size $\geq 2$ . Partition the coalition into nonempty subsets $G_{1},G_{2}$ . Fix distinct $x,y,z$ . Design the following voting pattern (notice that it is the cyclic voting pattern which causes the Condorcet paradox): ${\begin{aligned}{\text{voters in }}G_{1}&:x\succ _{i}y\succ _{i}z\\{\text{voters in }}G_{2}&:z\succ _{i}x\succ _{i}y\\{\text{voters outside }}G&:y\succ _{i}z\succ _{i}x\end{aligned}}$ (Items other than $x,y,z$ are not relevant.) Since G is decisive, we have $x\succ y$ . So at least one is true: $x\succ z$ or $z\succ y$ . If $x\succ z$ , then $G_{1}$ is weakly decisive over $(x,z)$ . If $z\succ y$ , then $G_{2}$ is weakly decisive over $(z,y)$ . Now apply the field expansion lemma. By Pareto, the entire set of voters is decisive. Thus by the group contraction lemma, there is a size-one decisive coalition—a dictator. |

| Proof by showing there is only one pivotal voter |
|---|
| Proofs using the concept of the **pivotal voter** originated from Salvador Barberá in 1980. The proof given here is a simplified version based on two proofs published in *Economic Theory*. Setup Assume there are *n* voters. We assign all of these voters an arbitrary ID number, ranging from *1* through *n*, which we can use to keep track of each voter's identity as we consider what happens when they change their votes. Without loss of generality, we can say there are three candidates who we call **A**, **B**, and **C**. (Because of IIA, including more than 3 candidates does not affect the proof.) We will prove that any social choice rule respecting unanimity and independence of irrelevant alternatives (IIA) is a dictatorship. The proof is in three parts: We identify a *pivotal voter* for each individual contest (**A** vs. **B**, **B** vs. **C**, and **A** vs. **C**). Their ballot swings the societal outcome. We prove this voter is a *partial* dictator. In other words, they get to decide whether A or B is ranked higher in the outcome. We prove this voter is the same person, hence this voter is a dictator. Part one: There is a pivotal voter for A vs. B Consider the situation where everyone prefers **A** to **B**, and everyone also prefers **C** to **B**. By unanimity, society must also prefer both **A** and **C** to **B**. Call this situation *profile[0, x]*. On the other hand, if everyone preferred **B** to everything else, then society would have to prefer **B** to everything else by unanimity. Now arrange all the voters in some arbitrary but fixed order, and for each *i* let *profile i* be the same as *profile 0*, but move **B** to the top of the ballots for voters 1 through *i*. So *profile 1* has **B** at the top of the ballot for voter 1, but not for any of the others. *Profile 2* has **B** at the top for voters 1 and 2, but no others, and so on. Since **B** eventually moves to the top of the societal preference as the profile number increases, there must be some profile, number *k*, for which **B** *first* moves *above* **A** in the societal rank. We call the voter *k* whose ballot change causes this to happen the *pivotal voter for **B** over **A***. Note that the pivotal voter for **B** over **A** is not, a priori, the same as the pivotal voter for **A** over **B**. In part three of the proof we will show that these do turn out to be the same. Also note that by IIA the same argument applies if *profile 0* is any profile in which **A** is ranked above **B** by every voter, and the pivotal voter for **B** over **A** will still be voter *k*. We will use this observation below. Part two: The pivotal voter for B over A is a dictator for B over C In this part of the argument we refer to voter *k*, the pivotal voter for **B** over **A**, as the *pivotal voter* for simplicity. We will show that the pivotal voter dictates society's decision for **B** over **C**. That is, we show that no matter how the rest of society votes, if *pivotal voter* ranks **B** over **C**, then that is the societal outcome. Note again that the dictator for **B** over **C** is not a priori the same as that for **C** over **B**. In part three of the proof we will see that these turn out to be the same too. In the following, we call voters 1 through *k − 1*, *segment one*, and voters *k + 1* through *N*, *segment two*. To begin, suppose that the ballots are as follows: Every voter in segment one ranks **B** above **C** and **C** above **A**. Pivotal voter ranks **A** above **B** and **B** above **C**. Every voter in segment two ranks **A** above **B** and **B** above **C**. Then by the argument in part one (and the last observation in that part), the societal outcome must rank **A** above **B**. This is because, except for a repositioning of **C**, this profile is the same as *profile k − 1* from part one. Furthermore, by unanimity the societal outcome must rank **B** above **C**. Therefore, we know the outcome in this case completely. Now suppose that pivotal voter moves **B** above **A**, but keeps **C** in the same position and imagine that any number (even all!) of the other voters change their ballots to move **B** below **C**, without changing the position of **A**. Then aside from a repositioning of **C** this is the same as *profile k* from part one and hence the societal outcome ranks **B** above **A**. Furthermore, by IIA the societal outcome must rank **A** above **C**, as in the previous case. In particular, the societal outcome ranks **B** above **C**, even though Pivotal Voter may have been the *only* voter to rank **B** above **C**. By IIA, this conclusion holds independently of how **A** is positioned on the ballots, so pivotal voter is a dictator for **B** over **C**. Part three: There exists a dictator In this part of the argument we refer back to the original ordering of voters, and compare the positions of the different pivotal voters (identified by applying parts one and two to the other pairs of candidates). First, the pivotal voter for **B** over **C** must appear earlier (or at the same position) in the line than the dictator for **B** over **C**: As we consider the argument of part one applied to **B** and **C**, successively moving **B** to the top of voters' ballots, the pivot point where society ranks **B** above **C** must come at or before we reach the dictator for **B** over **C**. Likewise, reversing the roles of **B** and **C**, the pivotal voter for **C** over **B** must be at or later in line than the dictator for **B** over **C**. In short, if *k*X/Y denotes the position of the pivotal voter for **X** over **Y** (for any two candidates **X** and **Y**), then we have shown *k*B/C ≤ kB/A ≤ *k*C/B. Now repeating the entire argument above with **B** and **C** switched, we also have *k*C/B ≤ *k*B/C. Therefore, we have *k*B/C = kB/A = *k*C/B and the same argument for other pairs shows that all the pivotal voters (and hence all the dictators) occur at the same position in the list of voters. This voter is the dictator for the whole election. |

### Stronger versions

Arrow's impossibility theorem still holds if Pareto efficiency is weakened to the following condition:

**Non-imposition**

For any two alternatives

a

and

b

, there exists some preference profile

R

1

, …,

R

N

such that

a

is preferred to

b

by

F(

R

1

,

R

2

, …,

R

N

)

.

## Interpretation and practical solutions

Arrow's theorem establishes that no ranked voting rule can *always* satisfy independence of irrelevant alternatives, but it says nothing about the frequency of spoilers. This led Arrow to remark that "Most systems are not going to work badly all of the time. All I proved is that all can work badly at times."

Attempts at dealing with the effects of Arrow's theorem take one of two approaches: either accepting his rule and searching for the least spoiler-prone methods, or dropping one or more of his assumptions, such as by focusing on rated voting rules.

### Minimizing IIA failures: Majority-rule methods

The first set of methods studied by economists are the majority-rule, or *Condorcet*, methods. These rules limit spoilers to situations where majority rule is self-contradictory, called Condorcet cycles, and as a result uniquely minimize the possibility of a spoiler effect among ranked rules. (Indeed, many different social welfare functions can meet Arrow's conditions under such restrictions of the domain. It has been proven, however, that under any such restriction, if there exists any social welfare function that adheres to Arrow's criteria, then Condorcet method will adhere to Arrow's criteria.) Condorcet believed voting rules should satisfy both independence of irrelevant alternatives and the majority rule principle, i.e. if most voters rank *Alice* ahead of *Bob*, *Alice* should defeat *Bob* in the election.

Unfortunately, as Condorcet proved, this rule can be intransitive on some preference profiles. Thus, Condorcet proved a weaker form of Arrow's impossibility theorem long before Arrow, under the stronger assumption that a voting system in the two-candidate case will agree with a simple majority vote.

Unlike pluralitarian rules such as instant-runoff voting or plurality voting, Condorcet methods avoid the spoiler effect in non-cyclic elections, where candidates can be chosen by majority rule. Political scientists have found such cycles to be fairly rare, suggesting they may be of limited practical concern. Spatial voting models also suggest such paradoxes are likely to be infrequent or even non-existent.

#### Left-right spectrum

Soon after Arrow published his theorem, Duncan Black showed his own remarkable result, the median voter theorem. The theorem proves that if voters and candidates are arranged on a left-right spectrum, Arrow's conditions are all fully compatible, and all will be met by any rule satisfying Condorcet's majority-rule principle.

More formally, Black's theorem assumes preferences are *single-peaked*: a voter's happiness with a candidate goes up and then down as the candidate moves along some spectrum. For example, in a group of friends choosing a volume setting for music, each friend would likely have their own ideal volume; as the volume gets progressively too loud or too quiet, they would be increasingly dissatisfied. If the domain is restricted to profiles where every individual has a single-peaked preference with respect to the linear ordering, then social preferences are acyclic. In this situation, Condorcet methods satisfy a wide variety of highly-desirable properties, including being fully spoilerproof.

The rule does not fully generalize from the political spectrum to the political compass, a result related to the McKelvey-Schofield chaos theorem. However, a well-defined Condorcet winner does exist if the distribution of voters is rotationally symmetric or otherwise has a uniquely-defined median. In most realistic situations, where voters' opinions follow a roughly-normal distribution or can be accurately summarized by one or two dimensions, Condorcet cycles are rare (though not unheard of).

#### Generalized stability theorems

The Campbell-Kelly theorem shows that Condorcet methods are the most spoiler-resistant class of ranked voting systems: whenever it is possible for some ranked voting system to avoid a spoiler effect, a Condorcet method will do so. In other words, replacing a ranked method with its Condorcet variant (i.e. elect a Condorcet winner if they exist, and otherwise run the method) will sometimes prevent a spoiler effect, but can never create a new one.

In 1977, Ehud Kalai and Eitan Muller gave a full characterization of domain restrictions admitting a nondictatorial and strategyproof social welfare function. These correspond to preferences for which there is a Condorcet winner.

Holliday and Pacuit devised a voting system that provably minimizes the number of candidates who are capable of spoiling an election, albeit at the cost of occasionally failing vote positivity (though at a much lower rate than seen in instant-runoff voting).

As shown above, the proof of Arrow's theorem relies crucially on the assumption of ranked voting, and is not applicable to rated voting systems. These systems ask voters to rate candidates on a numerical scale (e.g. from 0–10), and then elect the candidate with the highest average (for score voting) or median (graduated majority judgment). This opens up the possibility of finding another social choice procedure that satisfies independence of irrelevant alternatives. Arrow's theorem can thus be considered a special case of Harsanyi's utilitarian theorem and other utility representation theorems like the VNM theorem, which show rational behavior requires consistent cardinal utilities.

While Arrow's theorem does not apply to graded systems, Gibbard's theorem still does: no voting game can be straightforward (i.e. have a single, clear, always-best strategy).

#### Meaningfulness of cardinal information

Arrow's framework assumed individual and social preferences are orderings or rankings, i.e. statements about which outcomes are better or worse than others. Taking inspiration from the behavioralist approach, some philosophers and economists rejected the idea of comparing internal human experiences of well-being. Such philosophers claimed it was impossible to compare the strength of preferences across people who disagreed; Sen gives as an example that it would be impossible to know whether the Great Fire of Rome was good or bad, because despite killing thousands of Romans, it had the positive effect of letting Nero expand his palace.

Arrow originally agreed with these position, rejecting the meaningfulness of cardinal utilities, thus interpreting his theorem as a kind of proof for nihilism or egoism. However, he later stated that cardinal methods can provide additional useful information, and that his theorem is not applicable to them. Similarly, Amartya Sen first claimed interpersonal comparability is necessary for IIA, but later came to argue in favor of cardinal methods for assessing social choice, arguing they would only require "rather limited levels of partial comparability" to hold in practice.

Other scholars have noted that interpersonal comparisons of utility are not unique to cardinal voting, but are instead a necessity of any non-dictatorial choice procedure, with cardinal voting rules making these comparisons explicit. David Pearce identified Arrow's original nihilist interpretation with a kind of circular reasoning, with Hildreth pointing out that "any procedure that extends the partial ordering of [Pareto efficiency] must involve interpersonal comparisons of utility." Similar observations have led to implicit utilitarian voting approaches, which attempt to make the assumptions of ranked procedures more explicit by modeling them as approximations of the utilitarian rule (or score voting).

In psychometrics, there is a general consensus that self-reported ratings (e.g. Likert scales) are meaningful and provide more information than pure rankings, as well as showing higher validity and reliability. Cardinal rating scales (e.g. Likert scales) provide more information than rankings alone. A review by Kaiser and Oswald found that ratings were more predictive of important decisions (such as international migration and divorce) than even standard socioeconomic predictors like income and demographics, writing that "this feelings-to-actions relationship takes a generic form, is consistently replicable, and is fairly close to linear in structure. Therefore, it seems that human beings can successfully operationalize an integer scale for feelings".

#### Nonstandard spoilers

Behavioral economists have shown individual irrationality involves violations of IIA (e.g. with decoy effects), suggesting human behavior can cause IIA failures even if the voting method itself does not. However, past research has typically found such effects to be fairly small, and such psychological spoilers can appear regardless of electoral system. Balinski and Laraki discuss techniques of ballot design derived from psychometrics that minimize these psychological effects, such as asking voters to give each candidate a verbal grade (e.g. "bad", "neutral", "good", "excellent") and issuing instructions to voters that refer to their ballots as judgments of individual candidates. Similar techniques are often discussed in the context of contingent valuation.

### Esoteric solutions

In addition to the above practical resolutions, there exist unusual (less-than-practical) situations where Arrow's requirement of IIA can be satisfied.

#### Supermajority rules

Supermajority rules can avoid Arrow's theorem at the cost of being poorly-decisive (i.e. frequently failing to return a result). In this case, a threshold that requires a $2/3$ majority for ordering 3 outcomes, $3/4$ for 4, etc. does not produce voting paradoxes.

In spatial (n-dimensional ideology) models of voting, this can be relaxed to require only $1-e^{-1}$ (roughly 64%) of the vote to prevent cycles, so long as the distribution of voters is well-behaved (quasiconcave). These results provide some justification for the common requirement of a two-thirds majority for constitutional amendments, which is sufficient to prevent cyclic preferences in most situations.

#### Infinite populations

Fishburn shows all of Arrow's conditions can be satisfied for uncountably infinite sets of voters given the axiom of choice; however, Kirman and Sondermann demonstrated this requires disenfranchising almost all members of a society (eligible voters form a set of measure 0), leading them to refer to such societies as "invisible dictatorships".

## Common misconceptions

Arrow's theorem is not related to strategic voting, which does not appear in his framework, though the theorem does have important implications for strategic voting (being used as a lemma to prove Gibbard's theorem). The Arrovian framework of social welfare assumes all voter preferences are known and the only issue is in aggregating them.

Monotonicity (called positive association by Arrow) is not a condition of Arrow's theorem. This misconception is caused by a mistake by Arrow himself, who included the axiom in his original statement of the theorem but did not use it. Dropping the assumption does not allow for constructing a social welfare function that meets his other conditions.

Contrary to a common misconception, Arrow's theorem deals with the limited class of ranked-choice voting systems, rather than voting systems as a whole.
