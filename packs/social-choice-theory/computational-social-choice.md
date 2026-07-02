---
title: "Computational social choice"
source: https://en.wikipedia.org/wiki/Computational_social_choice
domain: social-choice-theory
license: CC-BY-SA-4.0
tags: social choice theory, arrow impossibility theorem, voting rule, gibbard satterthwaite theorem
fetched: 2026-07-02
---

# Computational social choice

**Computational social choice** (**COMSOC**) is a field at the intersection of social choice theory, theoretical computer science, and the analysis of multi-agent systems. It consists of the analysis of problems arising from the aggregation of preferences of a group of agents from a computational perspective. In particular, computational social choice is concerned with the efficient computation of outcomes of voting rules, with the computational complexity of various forms of manipulation, and issues arising from the problem of representing and eliciting preferences in combinatorial settings.

## Winner determination

The usefulness of a particular voting system can be severely limited if it takes a very long time to calculate the winner of an election. Therefore, it is important to design fast algorithms that can evaluate a voting rule when given ballots as input. As is common in computational complexity theory, an algorithm is thought to be efficient if it takes polynomial time. Many popular voting rules can be evaluated in polynomial time in a straightforward way (i.e., counting), such as the Borda count, approval voting, or the plurality rule. For rules such as the Schulze method or ranked pairs, more sophisticated algorithms can be used to show polynomial runtime. Certain voting systems, however, are computationally difficult to evaluate. In particular, winner determination for the Kemeny-Young method, Dodgson's method, and Young's method are all NP-hard problems. This has led to the development of approximation algorithms and fixed-parameter tractable algorithms to improve the theoretical calculation of such problems.

## Preference Representation

An important differentiation between voting rules is the format of ballots used by the voters to represent their preference. The two most common formats are approval ballots and ordinal ranks.

In approval ballots, each voter approves some candidates she likes. There is no further differentiation or hierarchy within the approved candidates. The same holds for the non-approved candidates. Thus, such ballots are also called dichotomous. Approval ballots are used for instance in satisfaction approval voting and proportional approval voting.

In contrast, ordinal ranks require the voter to rank all candidates from best to worst. This type of ballot is used for example in Borda's rule or in Bucklin voting.

There are many other types of ballot formats described in literature, such as truncated ranks, trichotomous ballots, or cardinal utility ballots.

Some research in computational social choice is focused on how representative ballot formats are, and on developing expressive, yet compact ballot formats. This is especially important in combinatorial settings, such as multiwinner voting.

## Other topics

### Tournament solutions

A tournament solution is a rule that assigns to every tournament a set of winners. Since a preference profile induces a tournament through its majority relation, every tournament solution can also be seen as a voting rule which only uses information about the outcomes of pairwise majority contests. Many tournament solutions have been proposed, and computational social choice theorists have studied the complexity of the associated winner determination problems.

### Preference restrictions

Restricted preference domains, such as single-peaked or single-crossing preferences, are an important area of study in social choice theory, since preferences from these domains avoid the Condorcet paradox and thus can circumvent impossibility results like Arrow's theorem and the Gibbard-Satterthwaite theorem. From a computational perspective, such domain restrictions are useful to speed up winner determination problems, both computationally hard single-winner and multi-winner rules can be computed in polynomial time when preferences are structured appropriately. On the other hand, manipulation problem also tend to be easy on these domains, so complexity shields against manipulation are less effective. Another computational problem associated with preference restrictions is that of recognizing when a given preference profile belongs to some restricted domain. This task is polynomial time solvable in many cases, including for single-peaked and single-crossing preferences, but can be hard for more general classes.

### Multiwinner elections

While most traditional voting rules focus on selecting a single winner, many situations require selecting multiple winners. This is the case when a fixed-size parliament or a committee is to be elected, though multiwinner voting rules can also be used to select a set of recommendations or facilities or a shared bundle of items. Work in computational social choice has focused on defining such voting rules, understanding their properties, and studying the complexity of the associated winner determination problems. See multiwinner voting.
