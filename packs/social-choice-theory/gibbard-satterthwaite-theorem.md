---
title: "Gibbard–Satterthwaite theorem"
source: https://en.wikipedia.org/wiki/Gibbard%E2%80%93Satterthwaite_theorem
domain: social-choice-theory
license: CC-BY-SA-4.0
tags: social choice theory, arrow impossibility theorem, voting rule, gibbard satterthwaite theorem
fetched: 2026-07-02
---

# Gibbard–Satterthwaite theorem

The **Gibbard–Satterthwaite theorem** is a theorem in social choice theory. It was first conjectured by the philosopher Michael Dummett and the mathematician Robin Farquharson in 1961 and then proved independently by the philosopher Allan Gibbard in 1973 and economist Mark Satterthwaite in 1975. It deals with deterministic ordinal electoral systems, and shows that for every voting rule of this form, at least one of the following things must hold:

1. The rule is dictatorial, i.e. there exists a distinguished voter who can choose the winner; or
2. The rule limits the possible outcomes to two alternatives only; or
3. The rule is manipulable, i.e. not strategyproof, i.e., there is no single always-best strategy (one that does not depend on other voters' preferences or behavior).
4. The rule does not yield a single winner

Gibbard's proof of the theorem is more general and covers processes of collective decision that may not be ordinal, such as cardinal voting. Gibbard's 1978 theorem and Hylland's theorem are even more general and extend these results to non-deterministic processes, where the outcome may depend partly on chance; the Duggan–Schwartz theorem extends these results to multiwinner electoral systems.

The theorem has two interpretations. The old interpretation views it as a proof that "democracy is impossible", stating that if we require a voting rule to yield a single winner, there are distributions of voter preferences where the rule is dictatorial or "allows manipulation".

The modern interpretation views it as a proof that **there is no point to look for an agreement using a voting rule when there is no agreement.** In this interpretation the theorem is an argument to use "**none of above**" as a choice in every vote (as the Debian General Resolution Procedure does), and to accept that a vote can yield no result, signaling that more deliberation is needed about the topic.

## Informal description

Consider three voters named Alice, Bob and Carol, who wish to select a winner among four candidates named a , b , c and d . Assume that they use the Borda count: each voter communicates their preference order over the candidates. For each ballot, 3 points are assigned to the top candidate, 2 points to the second candidate, 1 point to the third one and 0 points to the last one. Once all ballots have been counted, the candidate with the most points is declared the winner.

Assume that their preferences are as follows.

| Voter | Choice 1 | Choice 2 | Choice 3 | Choice 4 |
|---|---|---|---|---|
| Alice | a | b | c | d |
| Bob | c | b | d | a |
| Carol | c | b | d | a |

If the voters cast sincere ballots, then the scores are: $(a:3,b:6,c:7,d:2)$ . Hence, candidate c will be elected, with 7 points.

But Alice can vote strategically and change the result. Assume that she modifies her ballot, in order to produce the following situation.

| Voter | Choice 1 | Choice 2 | Choice 3 | Choice 4 |
|---|---|---|---|---|
| Alice | b | a | d | c |
| Bob | c | b | d | a |
| Carol | c | b | d | a |

Alice has strategically upgraded candidate b and downgraded candidate c . Now, the scores are: $(a:2,b:7,c:6,d:3)$ . Hence, b is elected. Alice is satisfied by her ballot modification, because she prefers the outcome b to c , which is the outcome she would obtain if she voted sincerely.

We say that the Borda count is *manipulable*: there exists situations where a sincere ballot does not defend a voter's preferences best.

The Gibbard–Satterthwaite theorem states that every ranked-choice voting is manipulable, except possibly in two cases: if there is a distinguished voter who has a dictatorial power, or if the rule limits the possible outcomes to two options only.

## Formal statement

Let ${\mathcal {A}}$ be the set of *alternatives* (which is assumed finite), also called *candidates*, even if they are not necessarily persons: they can also be several possible decisions about a given issue. We denote by ${\mathcal {N}}=\{1,\ldots ,n\}$ the set of *voters*. Let ${\mathcal {P}}$ be the set of strict weak orders over ${\mathcal {A}}$ : an element of this set can represent the preferences of a voter, where a voter may be indifferent regarding the ordering of some alternatives. A *voting rule* is a function $f:{\mathcal {P}}^{n}\to {\mathcal {A}}$ . Its input is a profile of preferences $(P_{1},\ldots ,P_{n})\in {\mathcal {P}}^{n}$ and it yields the identity of the winning candidate.

We say that f is *manipulable* if and only if there exists a profile $(P_{1},\ldots ,P_{n})\in {\mathcal {P}}^{n}$ where some voter i , by replacing her ballot $P_{i}$ with another ballot $P_{i}'$ , can get an outcome that she prefers (in the sense of $P_{i}$ ).

We denote by $f({\mathcal {P}}^{n})$ the image of f , i.e. the set of *possible outcomes* for the election. For example, we say that f has at least three possible outcomes if and only if the cardinality of $f({\mathcal {P}}^{n})$ is 3 or more.

We say that f is *dictatorial* if and only if there exists a voter i who is a *dictator*, in the sense that the winning alternative is always her most-liked one among the possible outcomes *regardless of the preferences of other voters*. If the dictator has several equally most-liked alternatives among the possible outcomes, then the winning alternative is simply one of them.

**Gibbard–Satterthwaite theorem**—If an ordinal voting rule has at least 3 possible outcomes and is non-dictatorial, then it is manipulable.

## Corollary for strict preferences

We now consider the case where by assumption, a voter cannot be indifferent between two candidates. We denote by ${\mathcal {L}}$ the set of strict total orders over ${\mathcal {A}}$ and we define a *strict voting rule* as a function $f:{\mathcal {L}}^{n}\to {\mathcal {A}}$ . The definitions of *possible outcomes*, *manipulable*, *dictatorial* have natural adaptations to this framework.

For a strict voting rule, the converse of the Gibbard–Satterthwaite theorem is true. Indeed, a strict voting rule is dictatorial if and only if it always selects the most-liked candidate of the dictator among the possible outcomes; in particular, it does not depend on the other voters' ballots. As a consequence, it is not manipulable: the dictator is perfectly defended by her sincere ballot, and the other voters have no impact on the outcome, hence they have no incentive to deviate from sincere voting. Thus, we obtain the following equivalence.

**Theorem**—If a strict voting rule has at least 3 possible outcomes, it is non-manipulable if and only if it is dictatorial.

In the theorem, as well as in the corollary, it is not needed to assume that any alternative can be elected. It is only assumed that at least three of them can win, i.e. are *possible outcomes* of the voting rule. It is possible that some other alternatives can be elected in no circumstances: the theorem and the corollary still apply. However, the corollary is sometimes presented under a less general form: instead of assuming that the rule has at least three possible outcomes, it is sometimes assumed that ${\mathcal {A}}$ contains at least three elements and that the voting rule is *onto*, i.e. every alternative is a possible outcome. The assumption of being onto is sometimes even replaced with the assumption that the rule is *unanimous*, in the sense that if all voters prefer the same candidate, then she must be elected.

## Proofs

### Proof using Arrow's impossibility theorem

The original proofs by Gibbard and Satterthwaite used the Arrow's impossibility theorem for social ranking functions. We give a sketch of proof in the simplified case where some voting rule f is assumed to be Pareto-efficient.

It is possible to build a social ranking function $\operatorname {Rank}$ , as follows: in order to decide whether $a\prec b$ , the $\operatorname {Rank}$ function creates new preferences in which a and b are moved to the top of all voters' preferences. Then, $\operatorname {Rank}$ examines whether f chooses a or b .

It is possible to prove that, if f is non-manipulable and non-dictatorial, $\operatorname {Rank}$ satisfies independence of irrelevant alternatives. Arrow's impossibility theorem says that, when there are three or more alternatives, such a $\operatorname {Rank}$ function must be a dictatorship. Hence, such a voting rule f must also be a dictatorship.

Later authors have developed other variants of the proof.

### Proof using Menus

Barbera and Peleg presented a different proof, using the notion of *menus* (also called: *option sets*). For simplicity, we present the proof for *n*=2 voters, and for preferences without ties (The extension to any number of voters can be done by straightforward induction; the extension to preferences with ties is straightforward as long as the domain contains all profiles without ties).

Definitions:

- Given a preference-ordering *P* and a set of candidates B, define **Best(P,B)** as the best candidate in *B*, given preference ordering *P*.
- Given a preference-ordering *P*1 for agent 1, define **Menu2(*P*1)** as the *option set of 2* - the set of all candidates that could potentially be elected when agent 1 votes *P*1 (ranging over all possible votes of agent 2).

The following lemmas are proved for a strategyproof rule *f*:

1. ***f*(P1,P2) = Best(P2, Menu2(*P*1)),** as otherwise agent 2 could manipulate. Similarly, ***f*(P1,P2) = Best(*P*1, Menu1(*P*2))**, as otherwise agent 1 could manipulate.
2. For any preference reported by agent 1, the best candidate by that preference is on the menu for agent 2. Formally, **Best(*P*1,Range(*f*)) in Menu2(*P*1)**. *Proof*: Let OPT1 := Best(*P*1,Range(*f*)). Since OPT1 is in range *f*, it equals R(P1*,P2*) for some profile (P1*,P2*). Hence, it is in Menu1(P2*). By Lemma 1, *f*(P1,P2*) = Best(*P*1, Menu1(*P2**)) = OPT1 = Best(*P*2*, Menu2(*P1*)). In particular, OPT1 is in Menu2(*P1*).
3. Unanimity holds: **If Best(*P*1,Range(*f*)) = Best(*P2*,Range(*f*)) = *x,* then f(*P*1,*P2*)=x.** *Proof*: follows from Lemmas 2 and 1.
4. The menu depends only on the best element; formally, **if Best(*P*1,Range(*f*)) = Best(*P1****,Range(*f*)) = x, then Menu2(*P*1)=Menu2(*P*1***)**. *Proof*: By Lemma 2, x is in both Menu2(P1) and Menu2(P1*). If the menus are not equal, then (wlog) some candidate z is in Menu2(P1) and not in Menu2(P1*). Let P2* be a preference that ranks z first, x second, and then all other candidates. Then, by Lemma 1, f(P1,P2*) = z and f(P1*,P2*) = x. But this means that x is in Menu1(P2), so by Lemma 1 again, *f*(P1,P2*) = Best(P1, Menu1(P2*))=*x* --- a contradiction [agent 1 could manipulate from P1 to P1*].
  - Hence, we can write from now on Menu2(x), meaning, Menu2(P1) for all P1 with best element x; by Lemma 2, **x in Menu2(x) for all x.**
5. For every x and z in Range(f), and for every Px with best candidate x and Pz with best candidate z, **Px prefers Best(Pz,Menu2(x)) to z**. *Proof*: Take x,z,Px,Pz as in the lemma statement, and let y=Best(Pz,Menu2(x)). Assume by contradiction that Px prefers z to y. By Lemma 1, f(Px,Pz)=Best(Pz, Menu2(x)) = y. By Lemma 3, f(Pz,Pz)=Best(Pz,Range(f)) = z. But this means that z is in Menu1(Pz), so y cannot be Best(Px, Menu1(Pz)). But by Lemma 1, *f*(Px,Pz) = Best(Px, Menu1(Pz)) --- a contradiction [agent 1 can profitably manipulate from Px to Pz].
6. For every x in Range(f), Menu2(x) is either a singleton or the entire Range(f). *Proof*: By contradiction, let x be some candidate that violates that statement. So Menu2(x) contains x (by Lemma 2), and some other element y (as it is not a singleton), but not some third element z (as it is not the entire range). Then there is a preference Px with best candidate x, that prefers z to y; and a preference Pz with best candidate z, that ranks y second. Then Best(Pz, Menu2(x)) = y but Px prefers z to y, contradicting Lemma 5.
7. Menu2(x) is either a singleton for all x, or the entire Range(*f*) for all x. *Proof*: By contradiction, let x be some candidate for which Menu2(x) is a singleton (and must be equal to {x}), and y some other candidate for which Menu2(y) = Range(*f*). Let Py be a preference with best element y, that prefers x to some third candidate z (here we assume that Range(f) contains at least three candidates). Since Menu2(Py) = Range(*f*), there is some P2 for which f(Py,P2)=z. But then agent 1 could manipulate from Py to some preference Px with best element x, as this would force the outcome to be x.

Based on Lemma 7, there are two options:

- If Menu2(P1) is a singleton for all P1, then by Lemma 2 this singleton must be Best(*P*1,Range(*f*)). Then *f*(P1,P2) = Best(*P*1,Range(*f*)), so 1 is a dictator.
- If Menu2(P1) = Range(*f*) for all P1, then by Lemma 1 *f*(P1,P2) = Best(P2, Range(*f*)), so 2 is a dictator.

## Variants

### Non-ordinal ballots

Gibbard's theorem deals with processes of collective choice that may not be ordinal, i.e. where a voter's action may not consist in communicating a preference order over the candidates.

### Non-deterministic voting rules

Gibbard's 1978 theorem and Hylland's theorem extend these results to non-deterministic mechanisms, i.e. where the outcome may not only depend on the ballots but may also involve a part of chance.

### Multi-winner voting rules

The Duggan–Schwartz theorem extend this result in another direction, by dealing with deterministic voting rules that choose multiple winners.

## Restricted preference domains

The GS theorem crucially relies on the fact that *all* preference rankings over the sets of candidates are possible. The theorem might not hold under *domain restrictions*, that is, when the agents are allowed to express preferences from a restricted set. There are various works studying possibility and impossibility results for restricted preference domains.

### Single-peaked preferences

When the agents are restricted to have single-peaked preferences, the GS theorem does not hold, as the median voting rule is strategyproof and non-dictatorial.

### Continuous preferences

Barbera and Peleg consider voting on continuous domains, such as budget-proposal aggregation, when the set of candidates is some metric space *M*, and the agents' preferences are restricted to continuous utility functions over *M*. They extend their Proof by Menus (above) to this restricted domain.

As a preliminary result, they prove that it is sufficient to consider preferences with a *single* best candidate. They prove that, if a voting rule *f* is dictatorial when restricted to preferences with a single best candidate, then it remains dictatorial without that restriction. They also prove that this restriction does not change the range of *f*. They also prove that Range(*f*) is a closed set, and that for every utility continuous function u1, Menu2(u1) is a closed set.

**Lemmas 1--3** from above do not make any domain assumptions, so they still hold.

**Lemma 4** (menu depends only on best element; **if Best(*u*1,Range(*f*)) = Best(*u1**,Range(*f*)) = x, then Menu2(*u*1)=Menu2(*u*1***)**) requires a different proof, as the preference P2* assumed in that proof is not necessarily continuous. *Proof*: By Lemma 2, x is in both Menu2(u1) and Menu2(u1*). If the menus are not equal, then (wlog) some candidate z is in Menu2(u1) and not in Menu2(u1*). Let *r* be a positive real number such that Ball(z,2r) --- the ball of radius *2r* around z --- does not intersect Menu2(u1*).

Let u2z be the following continuous utility function: u2z(y) = ${\frac {d(y,M\setminus Ball(z,r))}{d(y,z)+d(y,M\setminus Ball(z,r))}}$ , where *M* is the set of all candidates, and *d* is its metric. This function looks like a dome with a peak at z; it has u2z(t)=0 for all *t* in Menu2(u1*), and z = Best(u2z).

Similarly, let u2x be the following continuous utility function: u2x(y) = ${\frac {d(y,M\setminus Ball(x,r))}{2[d(y,x)+d(y,M\setminus Ball(x,r))]}}$ ; it is a dome with a peak at x. Note that Ball(z,r) and Ball(x,r) do not intersect.

Finally, let u2* := u2z+u2x; it has a high dome with a peak at z, and a distinct lower dome with a peak at x.

We have f(u1,u2*) = Best(u2*,Menu2(u1)) = z, as z is in Menu2(u1). Simultaneously, f(u1*,u2*) = Best(u2*,Menu2(u1*)) = x, as the entire dome with peak at z is not in Menu2(u1*). Hence, when 2 reports u2*, agent 1 can gain by manipulating from u1 to u1*.

Hence, we can still write the menu as a function of the best element: Menu2(*x*) = Menu2(u1) for all u1 with best element x.

**Lemma 5** does not make any domain assumptions, so it still holds given Lemma 4.

**Lemma 6** (For every x in Range(f), Menu2(x) is either a singleton or the entire Range(f)) requires a similar proof. *Proof*: By contradiction, let x be some candidate that violates that statement. So Menu2(x) contains x (by Lemma 2), and some other element y (as it is not a singleton), but not some third element z (as it is not the entire range). Then there is a continuous function ux with global maximum x and ux(z) > ux(y), and a continuous function uz with global maximum z, whose maximum on Menu2(x) is y. Then Best(uz, Menu2(x)) = y. Then ux(z) > ux(Best(uz, Menu2(x))), contradicting Lemma 5.

The rest of the proof is similar to the finite case: Lemma 6 implies Lemma 7, which implies that either agent 1 or agent 2 is a dictator.

The same proof holds for any utility domain that satisfies the following:

- If some candidate x is in both Menu2(u1) and Menu2(u1*), and some other candidate z is in Menu2(u1) and not in Menu2(u1*), then the domain contains a utility function u2 with Best(u2, Menu2(u1)) = z and Best(u2, Menu2(u1*)) = x.
- For every three candidates x y and z, such that Menu2(x) contains y but does not contain z, there is a function u1 with global maximum at x and with u1(z) > u1(y), and a function u2 with a global maximum at z and whose maximum on Menu2(x) is y.
- For every candidate y with Menu2(y) = Range(*f*), there is a utility function with maximum element y, that prefers x to some third candidate z.

## History

The strategic aspect of voting is already noticed in 1876 by Charles Dodgson, also known as Lewis Carroll, a pioneer in social choice theory. His quote (about a particular voting system) was made famous by Duncan Black:

> This principle of voting makes an election more of a game of skill than a real test of the wishes of the electors.

During the 1950s, Robin Farquharson published influential articles on voting theory. In an article with Michael Dummett, he conjectures that deterministic voting rules with at least three outcomes are never straightforward tactical voting. This conjecture was later proven independently by Allan Gibbard and Mark Satterthwaite. In a 1973 article, Gibbard exploits Arrow's impossibility theorem from 1951 to prove the result we now know as Gibbard's theorem. Independently, Satterthwaite proved the same result in his PhD dissertation in 1973, then published it in a 1975 article. This proof is also based on Arrow's impossibility theorem, but does not involve the more general version given by Gibbard's theorem.

## Importance

The Gibbard–Satterthwaite theorem is generally presented as a result about voting systems, but it can also be seen as an important result of mechanism design, which deals with a broader class of decision rules. Noam Nisan describes this relation:

> The GS theorem seems to quash any hope of designing incentive-compatible social-choice functions. The whole field of Mechanism Design attempts escaping from this impossibility result using various modifications in the model.

The main idea of these "escape routes" is that they allow for a broader class of mechanisms than ranked voting, similarly to the escape routes from Arrow's impossibility theorem.
