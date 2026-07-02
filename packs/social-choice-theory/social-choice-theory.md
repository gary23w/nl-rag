---
title: "Social choice theory"
source: https://en.wikipedia.org/wiki/Social_choice_theory
domain: social-choice-theory
license: CC-BY-SA-4.0
tags: social choice theory, arrow impossibility theorem, voting rule, gibbard satterthwaite theorem
fetched: 2026-07-02
---

# Social choice theory

**Social choice theory** is a branch of welfare economics that seeks to extend the theory of rational choice to collective decision-making. Social choice studies the behavior of different mathematical procedures (social welfare functions) used to combine individual preferences into a coherent whole. It contrasts with political science in that it is a normative field that studies how a society can make good decisions, whereas political science is a descriptive field that observes how societies actually do make decisions. While social choice began as a branch of economics and decision theory, it has since received substantial contributions from mathematics, philosophy, political science, and game theory.

Real-world examples of social choice rules include constitutions and parliamentary procedures for voting on laws, as well as electoral systems; as such, the field is occasionally called **voting theory**. It is closely related to mechanism design, which uses game theory to model social choice with imperfect information and self-interested citizens.

Social choice differs from decision theory in that the latter is concerned with how *individuals*, rather than *societies*, can make rational decisions.

## History

The earliest work on social choice theory comes from the writings of the Marquis de Condorcet, who formulated several key results including his jury theorem and his example showing the impossibility of majority rule. His work was prefigured by Ramon Llull's 1299 manuscript *Ars Electionis* (*The Art of Elections*), which discussed many of the same concepts, but was lost in the Late Middle Ages and only rediscovered in the early 21st century.

Kenneth Arrow's book *Social Choice and Individual Values* is often recognized as inaugurating the modern era of social choice theory. Later work has also considered approaches to legal compensation, fair division, variable populations, partial strategy-proofing of social-choice mechanisms, natural resources, capabilities and functionings approaches, and measures of welfare.

## Key results

### Arrow's impossibility theorem

Arrow's impossibility theorem is a key result showing that social choice functions based only on ordinal comparisons, rather than cardinal utility, will behave incoherently (unless they are dictatorial). Such systems violate independence of irrelevant alternatives, meaning they suffer from spoiler effects—the system can behave erratically in response to changes in the quality or popularity of one of the options.

### Condorcet cycles

Condorcet's example demonstrates that democracy cannot be thought of as being the same as simple majority rule or majoritarianism; otherwise, it will be self-contradictory when three or more options are available. Majority rule can create cycles that violate the transitive property: Attempting to use majority rule as a social choice function creates situations where we have A better than B and B better than C, but C is also better than A.

This contrasts with May's theorem, which shows that simple majority is the optimal voting mechanism when there are only two outcomes, and only ordinal preferences are allowed.

### Harsanyi's theorem

Harsanyi's utilitarian theorem shows that if individuals have preferences that are well-behaved under uncertainty (i.e. coherent), the only coherent and Pareto efficient social choice function is the utilitarian rule. This lends some support to the viewpoint expressed of John Stuart Mill, who identified democracy with the ideal of maximizing the common good (or utility) of society as a whole, under an equal consideration of interests.

### Manipulation theorems

Gibbard's theorem provides limitations on the ability of any voting rule to elicit honest preferences from voters, showing that no voting rule is strategyproof (i.e. does not depend on other voters' preferences) for elections with 3 or more outcomes.

The Gibbard–Satterthwaite theorem proves a stronger result for ranked-choice voting systems, showing that no such voting rule can be sincere (i.e. free of reversed preferences).

### Median voter theorem

### Mechanism design

The field of mechanism design, a subset of social choice theory, deals with the identification of rules that preserve while incentivizing agents to honestly reveal their preferences. One particularly important result is the revelation principle, which is almost a reversal of Gibbard's theorem: for any given social choice function, there exists a mechanism that obtains the same results but incentivizes participants to be completely honest.

Because mechanism design places stronger assumptions on the behavior of participants, it is sometimes possible to design mechanisms for social choice that accomplish apparently-"impossible" tasks. For example, by allowing agents to compensate each other for losses with transfers, the Vickrey–Clarke–Groves (VCG) mechanism can achieve the "impossible" according to Gibbard's theorem: the mechanism ensures honest behavior from participants, while still achieving a Pareto efficient outcome. As a result, the VCG mechanism can be considered a "better" way to make decisions than voting (though only so long as monetary transfers are possible).

19 years after Arrow’s *Social Choice and Individual Values* was published, in 1970, Sen would publish *Collective Choice and Social Welfare*, which "expanded Arrow’s original social choice framework". In it, Sen outlines several “conditions” that would likely produce a balanced, satisfactory outcome for both the majority and individual members of society. Whereas Arrow had penned his theorem with the assumption of ordinality, Sen introduced the assumption of cardinality, or interpersonal comparison, into the social-choice theory model. The problem with ordinality is that it excludes "information about each individual’s strength of preference or about how to compare different individuals' preferences with one another". In contrast, Sen’s version of social-choice theory notes the importance of taking into consideration factors like equality of opportunity and “capability” as they relate to individual preferences. Sen replaced utilitarian welfare economics’ “individual utility” with the concept of “capability,” which can be defined as a person’s freedom of choice and economic mobility in a society. Furthermore, Sen emphasized that the preferences of the poor should “be the decisive criterion” in deciding an outcome.

### Others

If the domain of preferences is restricted to those that include a majority-strength Condorcet winner, then selecting that winner is the unique resolvable, neutral, anonymous, and non-manipulable voting rule.

## Interpersonal utility comparison

Social choice theory is the study of theoretical and practical methods to aggregate or combine individual preferences into a collective social welfare function. The field generally assumes that individuals have preferences, and it follows that they can be modeled using utility functions, by the VNM theorem. But much of the research in the field assumes that those utility functions are internal to humans, lack a meaningful unit of measure and *cannot* be compared across different individuals. Whether this type of *interpersonal utility comparison* is possible or not significantly alters the available mathematical structures for social welfare functions and social choice theory.

In one perspective, following Jeremy Bentham, utilitarians have argued that preferences and utility functions of individuals are interpersonally comparable and may therefore be added together to arrive at a measure of aggregate utility. Utilitarian ethics call for maximizing this aggregate.

In contrast many twentieth century economists, following Lionel Robbins, questioned whether such measures of utility could be measured, or even considered meaningful. Following arguments similar to those espoused by behaviorists in psychology, Robbins argued concepts of utility were unscientific and unfalsifiable. Consider for instance the law of diminishing marginal utility, according to which utility of an added quantity of a good decreases with the amount of the good that is already in possession of the individual. It has been used to defend transfers of wealth from the "rich" to the "poor" on the premise that the former do not derive as much utility as the latter from an extra unit of income. Robbins argued that this notion is beyond positive science; that is, one cannot measure changes in the utility of someone else, nor is it required by positive theory.

Apologists for the interpersonal comparison of utility have argued that Robbins claimed too much. John Harsanyi agreed that perfect comparisons of mental states are not practically possible, but people can still make *some* comparisons thanks to their similar backgrounds, cultural experiences, and psychologies. Amartya Sen argues that even if interpersonal comparisons of utility are imperfect, we can still say that (despite being positive for Nero) the Great Fire of Rome had a negative overall value. Harsanyi and Sen thus argue that at least *partial* comparability of utility is possible, and social choice theory should proceed under that assumption.

## Relationship to public choice theory

Despite the similar names, "public choice" and "social choice" are two distinct fields that are only weakly related. Public choice deals with the modeling of political systems as they actually exist in the real world, and is primarily limited to positive economics (predicting how politicians and other stakeholders will act). It is therefore often thought of as the application of microeconomic models to political science, in order to predict the behavior of political actors. By contrast, social choice has a much more normative bent, and deals with the abstract study of decision procedures and their properties.

The Journal of Economic Literature classification codes place Social Choice under Microeconomics at JEL D71 (with Clubs, Committees, and Associations) whereas Public Choice falls under JEL D72 (Economic Models of Political Processes: Rent-Seeking, Elections, Legislatures, and Voting Behavior).

## Empirical research

Since Arrow, social choice theory has been characterized by being predominantly mathematical and theoretical, but some research has aimed at estimating the frequency of various voting paradoxes, such as the Condorcet paradox. A summary of 37 individual studies, covering a total of 265 real-world elections, large and small, found 25 instances of a Condorcet paradox for a total likelihood of 9.4%. While examples of the paradox seem to occur often in small settings like parliaments, very few examples have been found in larger groups (electorates), although some have been identified. However, the frequency of such paradoxes depends heavily on the number of options and other factors.

## Rules

Let X be a set of possible 'states of the world' or 'alternatives'. Society wishes to choose a single state from X . For example, in a single-winner election, X may represent the set of candidates; in a resource allocation setting, X may represent all possible allocations.

Let I be a finite set, representing a collection of individuals. For each $i\in I$ , let $u_{i}:X\longrightarrow \mathbb {R}$ be a *utility function*, describing the amount of happiness an individual *i* derives from each possible state.

A *social choice rule* is a mechanism which uses the data $(u_{i})_{i\in I}$ to select some element(s) from X which are 'best' for society. The question of what 'best' means is a common question in social choice theory. The following rules are most common:

- *Utilitarian rule* – sometimes called the *max-sum rule* or *Benthamite welfare* – aims to maximize the sum of utilities.
- *Egalitarian rule* – sometimes called the *max-min rule* or *Rawlsian welfare* – aims to maximize the smallest utility.

A social choice function, sometimes called a voting system in the context of politics, is a rule that takes an individual's complete and transitive preferences over a set of outcomes and returns a single chosen outcome (or a set of tied outcomes). We can think of this subset as the winners of an election, and compare different social choice functions based on which axioms or mathematical properties they fulfill.

Arrow's impossibility theorem is what often comes to mind when one thinks about impossibility theorems in voting. There are several famous theorems concerning social choice functions. The Gibbard–Satterthwaite theorem implies that the only rule satisfying non-imposition (every alternative can be chosen) and strategyproofness when there are more than two candidates is the dictatorship mechanism. That is, a voter may be able to cast a ballot that misrepresents their preferences to obtain a result that is more favorable to them under their sincere preferences. May's theorem shows that when there are only two candidates and only rankings of options are available, the simple majority vote is the unique neutral, anonymous, and positively-responsive voting rule.
