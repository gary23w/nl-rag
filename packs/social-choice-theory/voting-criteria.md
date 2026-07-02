---
title: "Voting criteria"
source: https://en.wikipedia.org/wiki/Voting_criteria
domain: social-choice-theory
license: CC-BY-SA-4.0
tags: social choice theory, arrow impossibility theorem, voting rule, gibbard satterthwaite theorem
fetched: 2026-07-02
---

# Voting criteria

There are a number of different criteria which can be used for voting systems in an election, including the following

## Condorcet criterion and similar criteria

### Condorcet criterion

A Condorcet winner (French: [kɔ̃dɔʁsɛ], English: /kɒndɔːrˈseɪ/) is a candidate who would receive more support than their opponent in a one-on-one race against any one of their opponents. Voting systems where a Condorcet winner will always win the election are said to satisfy the Condorcet winner criterion. The Condorcet winner criterion extends the principle of majority rule to elections with multiple candidates.

Named after Nicolas de Condorcet, it is also called a majority winner, a majority-preferred candidate, a beats-all winner, or tournament winner (by analogy with round-robin tournaments). A Condorcet winner may not necessarily always exist in a given electorate: for example, it is possible to have a rock paper scissors-style cycle, when multiple candidates defeat each other (rock < paper < scissors < rock). This is called Condorcet's voting paradox, and is analogous to the counterintuitive intransitive dice phenomenon known in probability. However, the Smith set, a generalization of the Condorcet criteria that is the smallest set of candidates that are pairwise unbeaten by every candidate outside of it, will always exist.

If voters are arranged on a single 1-dimensional axis, such as a left-right political spectrum, and always prefer candidates who are more similar to themselves, a majority-rule winner always exists and is the candidate whose ideology is most representative of the electorate; this result is known as the median voter theorem. However, political electorates are inherently multidimensional in real-life, and the use of a one- or even two-dimensional model of such electorates would be inaccurate. For multi-dimensional spaces there might be no Condorcet winner according to the McKelvey–Schofield chaos theorem.

Previous research has found cycles to be somewhat rare in real elections, with estimates of their prevalence ranging from 1% to 10% of races.

Systems that guarantee the election of a Condorcet winners (when one exists) include Ranked pairs, Schulze's method, and the Tideman alternative method. Methods that do *not* guarantee that the Cordorcet winner will be elected, even when one does exist, include instant-runoff voting (often called ranked-choice in the United States), first-past-the-post voting, and the two-round system. Most rated systems (like score voting and the highest median rules) are not Condorcet methods, as they try to account for the strengths of different voters' preferences rather than always following the majority.

### Condorcet loser criterion

In single-winner voting system theory, the Condorcet loser criterion (CLC) is a measure for differentiating voting systems. It implies the majority loser criterion but does not imply the Condorcet winner criterion.

A voting system complying with the Condorcet loser criterion will never allow a *Condorcet loser* to win. A Condorcet loser is a candidate who can be defeated in a head-to-head competition against each other candidate. (Not all elections will have a Condorcet loser since it is possible for three or more candidates to be mutually defeatable in different head-to-head competitions.)

### Smith criterion

The Smith set, sometimes called the top-cycle generalizes the idea of a Condorcet winner to cases where no such winner exists. It does so by allowing cycles of candidates to be treated jointly, as if they were a single Condorcet winner. Voting systems that always elect a candidate from the Smith set pass the Smith criterion. The Smith set and Smith criterion are both named for mathematician John H. Smith.

The Smith set provides one standard of optimal choice for an election outcome. An alternative, stricter criterion is given by the Landau set.

## Consistency criterion

A voting system satisfies join-consistency (also called the reinforcement criterion) if combining two sets of votes, both electing *A* over *B*, always results in a combined electorate that ranks *A* over *B*. It is a stronger form of the participation criterion. Systems that fail the consistency criterion (such as instant-runoff voting or Condorcet methods) are susceptible to the multiple-district paradox, a pathological behavior where a candidate can win an election without carrying even a single precinct. Conversely, it can be seen as allowing for a particularly egregious kind of gerrymander: it is possible to draw boundaries in such a way that a candidate who wins the overall election fails to carry even a single electoral district.

Rules susceptible to the multiple-districts paradox include all Condorcet methods and instant-runoff (or ranked-choice) voting. Rules that are not susceptible to it include all positional voting rules (such as first-preference plurality and the Borda count) as well as score voting and approval voting.

## Homogeneity criterion

Homogeneity is a common property for voting systems. The property is satisfied if, in any election, the result depends only on the proportion of ballots of each possible type. That is, if every ballot is replicated the same number of times, then the result should not change.

## Independence criteria

### Independence of irrelevant alternatives

Independence of irrelevant alternatives (IIA) is an axiom of decision theory which codifies the intuition that a choice between A and B (which are both related) should not depend on the quality of a third, unrelated outcome ${\textstyle C}$ . There are several different variations of this axiom, which are generally equivalent under mild conditions. As a result of its importance, the axiom has been independently rediscovered in various forms across a wide variety of fields, including economics, cognitive science, social choice, fair division, rational choice, artificial intelligence, probability, and game theory. It is closely tied to many of the most important theorems in these fields, including Arrow's impossibility theorem, the Balinski–Young theorem, and the money pump arguments.

In behavioral economics, failures of IIA (caused by irrationality) are called menu effects or menu dependence.

### Independence of clones criterion

In social choice theory, the independence of (irrelevant) clones criterion says that adding a *clone*, i.e. a new candidate very similar to an already-existing candidate, should not spoil the results. It can be considered a weak form of the independence of irrelevant alternatives (IIA) criterion that nevertheless is failed by a number of voting rules. A method that passes the criterion is said to be clone independent.

A group of candidates are called clones if they are always ranked together, placed side-by-side, by every voter; no voter ranks any of the non-clone candidates between or equal to the clones. In other words, the process of *cloning* a candidate involves taking an existing candidate *C*, then replacing them with several candidates *C1*, *C2..*. who are slotted into the original ballots in the spot where *C* previously was, with the clones being arranged in any order. If a set of clones contains at least two candidates, the criterion requires that deleting one of the clones must not increase or decrease the winning chance of any candidate not in the set of clones.

Ranked pairs, the Schulze method, and systems that unconditionally satisfy independence of irrelevant alternatives are clone independent. Instant-runoff voting passes as long as tied ranks are disallowed. If they are allowed, its clone independence depends on specific details of how the criterion is defined and how tied ranks are handled.

Rated methods like range voting or majority judgment that are spoilerproof under certain conditions are also clone independent under those conditions.

The Borda count, minimax, Kemeny–Young, Copeland's method, plurality, and the two-round system all fail the independence of clones criterion. Voting methods that limit the number of allowed ranks also fail the criterion, because the addition of clones can leave voters with insufficient space to express their preferences about other candidates. For similar reasons, ballot formats that impose such a limit may cause an otherwise clone-independent method to fail.

This criterion is very weak, as adding a substantially similar (but not quite identical) candidate to a race can still substantially affect the results and cause vote splitting. For example, the center squeeze pathology that affects instant-runoff voting means that several similar (but not identical) candidates competing in the same race will tend to hurt each other's chances of winning.

### Independence of Smith-dominated alternatives

Independence of Smith-dominated alternatives (ISDA, also known as Smith-IIA) is a voting system criterion which says that the winner of an election should not be affected by candidates who are not in the Smith set.

Another way of defining ISDA is to say that adding a new candidate should not change the winner of an election, *unless* that new candidate would beat the original winner, either directly or indirectly.

## Later-no criteria

### Later-no-harm criterion

| Name | Comply? |
|---|---|
| Plurality | Yes |
| Two-round system | Yes |
| Partisan primary | Yes |
| Instant-runoff voting | Yes |
| Minimax Opposition | Yes |
| DSC | Yes |
| Anti-plurality | No |
| Approval | N/A |
| Borda | No |
| Dodgson | No |
| Copeland | No |
| Kemeny | No |
| Ranked Pairs | No |
| Schulze | No |
| Score | No |
| Majority judgment | No |

Later-no-harm is a property of voting systems first described by Douglas Woodall. In later-no-harm systems, increasing the rating or rank of a candidate ranked below the winner of an election cannot cause a higher-ranked candidate to lose. It is a common property in the plurality-rule family of voting systems.

For example, say a group of voters ranks Alice 2nd and Bob 6th, and Alice wins the election. In the next election, Bob focuses on expanding his appeal with this group of voters, but does not manage to defeat Alice—Bob's rating increases from 6th-place to 3rd. Later-no-harm says that this increased support from Alice's voters should not allow Bob to win.

Later-no-harm may be confused as implying center squeeze, since later-no-harm is a defining characteristic of first-preference plurality (FPP) and instant-runoff voting (IRV), and descending solid coalitions (DSC), systems that have similar mechanics that are based on first preference counting. These systems pass later-no-harm compliance by making sure the results either do not depend on lower preferences at all (plurality) or only depend on them if all higher preferences have been eliminated (IRV and DSC), and thus exhibit a center squeeze effect. However, this does not mean that methods that pass later-no-harm must be vulnerable to center squeezes. The properties are distinct, as Minimax opposition also passes later-no-harm.

Later-no-harm is also often confused with immunity to a kind of strategic voting called strategic truncation or bullet voting. Satisfying later-no-harm does not provide immunity to such strategies. Systems like instant runoff that pass later-no-harm but fail monotonicity still incentivize truncation or bullet voting in some situations.

### Later-no-help criterion

The later-no-help criterion (or LNHe, not to be confused with LNH) is a voting system criterion formulated by Douglas Woodall. The criterion is satisfied if, in any election, a voter giving an additional ranking or positive rating to a less-preferred candidate can not cause a more-preferred candidate to win. Voting systems that fail the later-no-help criterion are vulnerable to the tactical voting strategy called mischief voting, which can deny victory to a sincere Condorcet winner.

## Majority winner and loser

### Majority winner criterion

The majority criterion is a voting system criterion applicable to voting rules over ordinal preferences required that if only one candidate is ranked first by over 50% of voters, that candidate must win.

Some methods that comply with this criterion include any Condorcet method, instant-runoff voting, Bucklin voting, plurality voting, and approval voting.

The mutual majority criterion is a generalized form of the criterion meant to account for when the majority prefers multiple candidates above all others; voting methods which pass majority but fail mutual majority can encourage all but one of the majority's preferred candidates to drop out in order to ensure one of the majority-preferred candidates wins, creating a spoiler effect.

### Majority loser criterion

The majority loser criterion is a criterion to evaluate single-winner voting systems. The criterion states that if a majority of voters give a candidate no support, i.e. do not list that candidate on their ballot, that candidate must lose (unless no candidate is accepted by a majority of voters).

Either of the Condorcet loser criterion or the mutual majority criterion implies the majority loser criterion. However, the Condorcet criterion does not imply the majority loser criterion, since the minimax method satisfies the Condorcet but not the majority loser criterion. Also, the majority criterion is logically independent from the majority loser criterion, since the plurality rule satisfies the majority but not the majority loser criterion, and the anti-plurality rule satisfies the majority loser but not the majority criterion. There is no positional scoring rule which satisfies both the majority and the majority loser criterion, but several non-positional rules, including many Condorcet rules, do satisfy both. Some voting systems, like instant-runoff voting, fail the criterion if extended to handle incomplete ballots.

## Monotonicity criterion

Non-negative responsiveness or monotonicity is a property of a social choice rule, which says that increasing a candidate's rank on some ballots should not cause them to lose (or vice versa, that decreasing a candidate's rank should not cause them to win). This means rankings can be interpreted as ordering candidates from best to worst, with higher ranks corresponding to more support. Voting systems that violate non-negative responsiveness can be said to exhibit negative response, perversity, or an additional support paradox.

Perversity is often described by social choice theorists as an exceptionally severe kind of electoral pathology, as such rules can have "backwards" responses to voters' opinions, where popularity causes defeat while unpopularity leads to a win. Such rules treat the well-being of some voters as "less than worthless". These issues have led to constitutional prohibitions on such systems as violating the right to equal and direct suffrage. Negative response is often cited as an example of a perverse incentive, as rules with negative response can incentivize politicians to take extreme or unpopular positions in an attempt to shed excess votes.

Most ranked methods (including Borda and all common round-robin rules) satisfy non-negative responsiveness, as do all common rated voting methods (including approval, highest medians, and score).

Negative responsiveness occurs in instant-runoff voting (IRV), the single transferable vote, and the two-round system. Some quota-based apportionment methods also violate the rule, as can the randomized Condorcet method in cases of cyclic ties.

The participation criterion is closely related, but different. While non-negative responsiveness deals with a voter changing their opinion (or vote), participation deals with situations where a voter choosing to cast a ballot at all has a backwards effect on the election.

## Proportionality for solid coalitions

Proportionality for solid coalitions (PSC) is a criterion of proportionality for ranked voting systems. It is an adaptation of the quota rule to voting systems in which there are no official party lists, and voters can directly support candidates. The criterion was first proposed by the British philosopher and logician Michael Dummett.

PSC is a relatively minimal definition of proportionality. To be guaranteed representation, a coalition of voters must rank all candidates within the same party first before candidates of other parties. And PSC does not guarantee proportional representation if voters rank candidates of different parties together (as they will no longer form a solid coalition).

## Participation criterion

The participation criterion is a voting system criterion that says candidates should never lose an election as a result of receiving too many votes in support. More formally, it says that adding more voters who prefer *Alice* to *Bob* should not cause *Alice* to lose the election to *Bob*.

Voting systems that fail the participation criterion exhibit the no-show paradox, where a voter is effectively disenfranchised by the electoral system because turning out to vote could make the result worse for them; such voters are sometimes referred to as having negative vote weights, particularly in the context of German constitutional law, where courts have ruled such a possibility violates the principle of one man, one vote.

Positional methods and score voting satisfy the participation criterion. All deterministic voting rules that satisfy pairwise majority-rule can fail in situations involving four-way cyclic ties, though such scenarios are empirically rare, and the randomized Condorcet rule is not affected by the pathology. The majority judgment rule fails as well. Instant-runoff voting and the two-round system both fail the participation criterion with high frequency in competitive elections, typically as a result of a center squeeze.

The no-show paradox is similar to, but not the same as, the perverse response paradox. Perverse response happens when an *existing* voter can make a candidate win by *de*creasing their rating of that candidate (or vice-versa). For example, under instant-runoff voting, moving a candidate from first-place to last-place on a ballot can cause them to win.

## Plurality criterion

**Woodall****'s** **plurality criterion** is a voting criterion for ranked voting. It is stated as follows:

If the number of ballots ranking A as the first preference is greater than the number of ballots on which another candidate B is given any preference [other than last], then A's probability of winning must be no less than B's.

Woodall has called the plurality criterion "a rather weak property that surely must hold in any real election" opining that "every reasonable electoral system seems to satisfy it."

Among Condorcet methods which permit truncation, whether the plurality criterion is satisfied depends often on the measure of defeat strength. When *winning votes* is used as the measure of defeat strength, plurality is satisfied. Plurality is failed when *margins* is used. Minimax using *pairwise opposition* also fails plurality.

When truncation is permitted under Borda count, the plurality criterion is satisfied when no points are scored to truncated candidates, and ranked candidates receive no fewer votes than if the truncated candidates had been ranked. If truncated candidates are instead scored the average number of points that would have been awarded to those candidates had they been strictly ranked, or if Nauru's modified Borda count is used, the plurality criterion is failed.

## Resolvability criteria

A voting system is called decisive, resolvable, or resolute if it ensures a low probability of tied elections. There are two different criterion that formalize this.

- In Nicolaus Tideman's version of the criterion, adding one extra vote (with no tied ranks) should make the winner unique.
- Douglas R. Woodall's version requires that the probability of a tied vote under an impartial culture model gives a tie approaches zero as the number of voters increases toward infinity.

A non-resolvable social choice function is often only considered to be a *partial* electoral method, sometimes called a voting correspondence or set-valued voting rule. Such methods frequently require tiebreakers that can substantially affect the result. However, non-resolute methods can be used as a first stage to eliminate candidates before ties are broken with some other method. Methods that have been used this way include the Copeland set, the Smith set, and the Landau set.

## Reversal symmetry

The reversal symmetry criterion is a voting system criterion which says that if every voter's opinions on each of the candidates is perfectly reversed (i.e. they rank candidates in order from worst to best), the outcome of the election should be reversed as well, i.e. the first- and last-place finishers should switch places. In other words, the results of the election should not depend arbitrarily on whether voters rank candidates from best to worst (and then select the best candidate), or whether we ask them to rank candidates from worst to best (and then select the least-bad candidate).

Another, equivalent way to motivate the criterion is to say that a voting system should never elect the worst candidate, according to the method itself (as doing so suggests the method is, in some sense, self-contradictory). The worst candidate can be identified by reversing all ballots (to rank candidates from worst-to-best) and then running the algorithm to find a single worst candidate.

Situations where the same candidate is elected when all ballots are reversed are sometimes called best-is-worst paradoxes, and can occur in instant-runoff voting and minimax. Methods that satisfy reversal symmetry include the Borda count, ranked pairs, Kemeny–Young, and Schulze. Most rated voting systems, including approval and score voting, satisfy the criterion as well.

## Unrestricted domain

In social choice theory, unrestricted domain, or universality, is a property of social welfare functions in which all preferences of all voters (but no other considerations) are allowed. Intuitively, unrestricted domain is a common requirement for social choice functions, and is a condition for Arrow's impossibility theorem.

With unrestricted domain, the social welfare function accounts for all preferences among all voters to yield a unique and complete ranking of societal choices. Thus, the voting mechanism must account for all individual preferences, it must do so in a manner that results in a complete ranking of preferences for society, and it must deterministically provide the same ranking each time voters' preferences are presented the same way.
