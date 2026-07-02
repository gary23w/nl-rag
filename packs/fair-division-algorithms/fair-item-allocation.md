---
title: "Fair item allocation"
source: https://en.wikipedia.org/wiki/Fair_item_allocation
domain: fair-division-algorithms
license: CC-BY-SA-4.0
tags: fair division, envy free allocation, cake cutting, proportional share
fetched: 2026-07-02
---

# Fair item allocation

**Fair item allocation** is a kind of the fair division problem in which the items to divide are *discrete* rather than continuous. The items have to be divided among several partners who potentially value them differently, and each item has to be given as a whole to a single person. This situation arises in various real-life scenarios:

- Several heirs want to divide the inherited property, which contains e.g. a house, a car, a piano and several paintings.
- Several lecturers want to divide the courses given in their faculty. Each lecturer can teach one or more whole courses.
- Gift-exchange party games featuring white elephant-type items.

The indivisibility of the items implies that a fair division may not be possible. As an extreme example, if there is only a single item (e.g. a house), it must be given to a single partner, but this is not fair to the other partners. This is in contrast to the fair cake-cutting problem, where the dividend is divisible and a fair division always exists. In some cases, the indivisibility problem can be mitigated by introducing *monetary payments* or *time-based rotation*, or by discarding some of the items. But such solutions are not always available.

An item assignment problem has several ingredients:

1. The partners have to express their *preferences* for the different item-bundles.
2. The group should decide on a *fairness criterion*.
3. Based on the preferences and the fairness criterion, a *fair assignment algorithm* should be executed to calculate a fair division.

## Preferences

### Combinatorial preferences

A naive way to determine the preferences is asking each partner to supply a numeric value for each possible bundle. For example, if the items to divide are a car and a bicycle, a partner may value the car as 800, the bicycle as 200, and the bundle {car, bicycle} as 900 (see Utility functions on indivisible goods for more examples). There are two problems with this approach:

1. It may be difficult for a person to calculate exact numeric values to the bundles.
2. The number of possible bundles can be huge: if there are m items then there are $2^{m}$ possible bundles. For example, if there are 16 items then each partner will have to present their preferences using 65536 numbers.

The first problem motivates the use of ordinal utility rather than cardinal utility. In the ordinal model, each partner should only express a ranking over the $2^{m}$ different bundles, i.e., say which bundle is the best, which is the second-best, and so on. This may be easier than calculating exact numbers, but it is still difficult if the number of items is large.

The second problem is often handled by working with individual items rather than bundles:

- In the cardinal approach, each partner should report a numeric valuation for each item;
- In the ordinal approach, each partner should report a ranking over the items, i.e., say which item is the best, which is the second-best, etc.

Under suitable assumptions, it is possible to *lift* the preferences on items to preferences on bundles. Then, the agents report their valuations/rankings on individual items, and the algorithm calculates for them their valuations/rankings on bundles.

### Additive preferences

To make the item-assignment problem simpler, it is common to assume that all items are independent goods (so they are not substitute goods nor complementary goods). Then:

- In the cardinal approach, each agent has an additive utility function (also called: *modular* utility function). Once the agent reports a value for each individual item, it is easy to calculate the value of each bundle by summing up the values of its items.
- In the ordinal approach, additivity allows us to infer some rankings between bundles. For example, if a person prefers w to x to y to z, then he necessarily prefers {w,x} to {w,y} or to {x,y}, and {w,y} to {x}. This inference is only partial, e.g., we cannot know whether the agent prefers {w} to {x,y} or even {w,z} to {x,y}.

The additivity implies that each partner can always choose a "preferable item" from the set of items on the table, and this choice is independent of the other items that the partner may have. This property is used by some fair assignment algorithms that will be described next.

### Compact preference representation languages

*Compact preference representation languages* have been developed as a compromise between the full expressiveness of combinatorial preferences to the simplicity of additive preferences. They provide a succinct representation to some natural classes of utility functions that are more general than additive utilities (but not as general as combinatorial utilities). Some examples are:

- *2-additive preferences*: each partner reports a value for each bundle of size at most 2. The value of a bundle is calculated by summing the values for the individual items in the bundle and adding the values of pairs in the bundle. Typically, when there are substitute items, the values of pairs will be negative, and when there are complementary items, the values of pairs will be positive. This idea can be generalized to *k-additive preferences* for every positive integer *k*.
- *Graphical models*: for each partner, there is a graph that represents the dependencies between different items. In the cardinal approach, a common tool is the *GAI net* (Generalized Additive Independence). In the ordinal approach, a common tool is the *CP net* (Conditional Preferences) and its extensions: *TCP net*, *UCP net*, *CP theory*, *CI net* (Conditional Importance) and *SCI net* (a simplification of CI net).
- *Logic based languages*: each partner describes some bundles using a first order logic formula, and may assign a value for each formula. For example, a partner may say: "For (x or (y and z)), my value is 5". This means that the agent has a value of 5 for any of the bundles: x, xy, xz, yz, xyz.
- *Bidding languages*: many languages for representing combinatorial preferences have been studied in the context of combinatorial auctions. Some of these languages can be adapted to the item assignment setting.

## Fairness criteria

### Individual guarantee criteria

An *individual guarantee criterion* is a criterion that should hold for each individual partner, as long as the partner truthfully reports his preferences. Five such criteria are presented below. They are ordered from the weakest to the strongest (assuming the valuations are additive):

The maximin-share (also called: max-min-fair-share guarantee) of an agent is the most preferred bundle he could guarantee himself as divider in divide and choose against adversarial opponents. An allocation is called *MMS-fair* if every agent receives a bundle that he weakly prefers over his MMS.

The proportional-fair-share of an agent is 1/*n* of his utility from the entire set of items. An allocation is called *proportional* if every agent receives a bundle worth at least his proportional-fair-share.

The min-max-fair-share of an agent is the minimal utility that she can hope to get from an allocation if all the other agents have the same preferences as her, when she always receives the best share. It is also the minimal utility that an agent can get for sure in the allocation game “Someone cuts, I choose first”. An allocation is *mFS-fair* if all agents receive a bundle that they weakly prefer over their mFS. mFS-fairness can be described as the result of the following negotiation process. A certain allocation is suggested. Each agent can object to it by demanding that a different allocation be made by another agent, letting him choose first. Hence, an agent would object to an allocation only if in *all* partitions, there is a bundle that he strongly prefers over his current bundle. An allocation is mFS-fair iff no agent objects to it, i.e., for every agent there exists a partition in which all bundles are weakly worse than his current share.

For every agent with subadditive utility, the mFS is worth *at least* $1/n$ . Hence, every mFS-fair allocation is proportional. For every agent with superadditive utility, the MMSis worth *at most* $1/n$ . Hence, every proportional allocation is MMS-fair. Both inclusions are strict, even when every agent has additive utility. This is illustrated in the following example:

There are three agents and three items:

- Alice values the items as 2,2,2. For her, MMS=PFS=mFS=2.
- Bob values the items as 3,2,1. For him, MMS=1, PFS=2 and mFS=3.
- Carl values the items as 3,2,1. For him, MMS=1, PFS=2 and mFS=3.

The possible allocations are as follows:

- Every allocation which gives an item to each agent is MMS-fair.
- Every allocation which gives the first and second items to Bob and Carl and the third item to Alice is proportional.
- No allocation is mFS-fair.

The above implications do not hold when the agents' valuations are not sub/superadditive.

#### Envy-freeness (EF)

Every agent weakly prefers his own bundle to any other bundle. Every envy-free allocation of all items is mFS-fair; this follows directly from the ordinal definitions and does not depend on additivity. If the valuations are additive, then an EF allocation is also proportional and MMS-fair. Otherwise, an EF allocation may be not proportional and even not MMS.

Weaker versions of EF include:

- **Envy-freeness-except-1 (EF1)**: for each two agents A and B, if we remove from the bundle of B the item most valuable for A, then A does not envy B (in other words, the "envy level" of A in B is at most the value of a single item). Under monotonicity, an EF1 allocation always exists.
- **Envy-freeness-except-cheapest (EFx)**: For each two agents A and B, if we remove from the bundle of B the item *least* valuable for A, then A does not envy B. EFx is strictly stronger than EF1. It is not known whether EFx allocations always exist.

#### Competitive equilibrium from Equal Incomes (CEEI)

This criterion is based on the following argument: the allocation process should be considered as a search for an equilibrium between the supply (the set of objects, each one having a public price) and the demand (the agents’ desires, each agent having the same budget for buying the objects). A competitive equilibrium is reached when the supply matches the demand. The fairness argument is straightforward: prices and budgets are the same for everyone. CEEI implies EF regardless of additivity. When the agents' preferences are additive and strict (each bundle has a different value), CEEI implies Pareto efficiency.

### Global optimization criteria

A *global optimization criterion* evaluates a division based on a given social welfare function:

- The *egalitarian* social welfare is minimum utility of a single agent. An item assignment is called *egalitarian-optimal* if it attains the maximum possible egalitarian welfare, i.e., it maximizes the utility of the poorest agent. Since there can be several different allocations maximizing the smallest utility, egalitarian optimality is often refined to *leximin-optimality*: from the subset of allocations maximizing the smallest utility, it selects those allocations that maximize the second-smallest utility, then the third-smallest utility, and so on.
- The *Nash* social welfare is the product of the utilities of the agents. An assignment called *Nash-optimal* or *Maximum-Nash-Welfare* if it maximizes the product of utilities. Nash-optimal allocations have some nice fairness properties.

An advantage of global optimization criteria over individual criteria is that welfare-maximizing allocations are Pareto efficient.

## Allocation algorithms

Various algorithms for fair item allocation are surveyed in pages on specific fairness criteria:

- Maximin-share item allocation;
- Proportional item allocation;
- Minimax-share item allocation: The problem of calculating the mFS of an agent is coNP-complete. The problem of deciding whether an mFS allocation exists is in $NP^{NP}$ , but its exact computational complexity is still unknown.
- Envy-free item allocation;
- Efficient approximately fair item allocation;
- Egalitarian item allocation;
- Nash-optimal allocation: and prove hardness of calculating utilitarian-optimal and Nash-optimal allocations. present an approximation procedure for Nash-optimal allocations.
- Picking sequence: a simple protocol where the agents take turns in selecting items, based on some pre-specified sequence of turns. The goal is to design the picking-sequence in a way that maximizes the expected value of a social welfare function (e.g. egalitarian or utilitarian) under some probabilistic assumptions on the agents' valuations.
- Competitive equilibrium: various algorithms for finding a CE allocation are described in the article on Fisher market.

## Between divisible and indivisible

Traditional papers on fair allocation either assume that all items are divisible, or that all items are indivisible. Some recent papers study settings in which the distinction between divisible and indivisible is more fuzzy.

### Bounding the amount of sharing

Several works assume that all objects can be divided if needed (e.g. by shared ownership or time-sharing), but sharing is costly or undesirable. Therefore, it is desired to find a fair allocation with the smallest possible number of shared objects, or of sharings. There are tight upper bounds on the number of shared objects / sharings required for various kinds of fair allocations among *n* agents:

- For proportional, envy-free, equitable and egalitarian allocation, *n*−1 sharings/shared objects are always sufficient, and may be necessary;
- For Consensus splitting into *k* parts, *n*(*n*−1) sharings/shared objects are always sufficient, and may be necessary.

This raises the question of whether it is possible to attain fair allocations with fewer sharings than the worst-case upper bound:

- Sandomirskiy and Segal-Halevi study sharing minimization in allocations that are both fair and Fractionally Pareto efficient (fPO). They prove that, if the agents' valuations are non-degenerate, the number of fPO allocations is polynomial in the number of objects (for a fixed number of agents). Therefore, it is possible to enumerate all of them in polynomial time, and find an allocation that is fair and fPO with the smallest number of sharings. In contrast, of the valuations are degenerate, the problem becomes NP-hard. They present empirical evidence that, in realistic cases, there often exists an allocation with substantially fewer sharings than the worst-case bound.
- Misra and Sethia complement their result by proving that, when *n* is not fixed, even for non-degenerate valuations, it is NP-hard to decide whether there exists an fPO envy-free allocation with 0 sharings. They also demonstrate an alternate approach to enumerating distinct consumption graph for allocations with a small number of sharings.
- Goldberg, Hollender, Igarashi, Manurangsi and Suksompong study sharing minimization in consensus splitting. They prove that, for agents with additive utilities, there is a polynomial-time algorithm for computing a consensus halving with at most *n* sharings, and for computing a consensus *k*-division with at most (*k*−1)*n* cuts. But sharing minimization is NP-hard: for any fixed *n*, it is NP-hard to distinguish between an instance that requires *n* sharings and an instance that requires 0 sharings. Probabilistically, *n* sharings are almost surely necessary for consensus halving when agents' utilities are drawn from probabilistic distributions. For agents with non-additive monotone utilities, consensus halving is PPAD-hard, but there are polynomial-time algorithms for a fixed number of agents.
- Bismuth, Makarov, Shapira and Segal-Halevi study fair allocation with identical valuations, which is equivalent to Identical-machines scheduling, and also the more general setting of Uniform-machines scheduling. They study the run-time complexity of deciding the existence of a fair allocation with s sharings or shared objects, where *s* is smaller than the worst-case upper bound of *n*−1. They prove that, for sharings, the problem is NP-hard for any *s* ≤ *n*−2; but for shared objects and *n* ≥ 3, the problem is polynomial for *s* = *n*−2 and NP-hard for any *s* ≤ *n*−3. When *n* is not fixed, the problem is strongly NP-hard.
- Bismuth, Bliznets and Segal-Halevi also study the run-time complexity of deciding the existence of a fair allocation with *s* sharings or shared objects, where the valuations are not identical but have other structural properties (binary valuations, equal-sum generalized-binary valuations, or non-degenerate).

### Mixture of divisible and indivisible goods

- Bei, Li, Liu, Liu and Lu study a mixture of indivisible and divisible *goods* (objects with positive utilities). They define an approximation to envy-freeness called *EFM* (envy-freeness for mixed items), which generalizes both envy-freeness for divisible items and EF1 for indivisible items. They prove that an EFM allocation always exists for any number of agents with additive valuations. They present efficient algorithms to compute EFM allocations for two agents with general additive valuations, and for *n* agents with piecewise linear valuations over the divisible goods. They also present an efficient algorithm that finds an *epsilon*-approximate EFM allocation.
- Bei, Liu, Lu and Wang study the same setting, focusing on maximin-share fairness. They propose an algorithm that computes an alpha-approximate MMS allocation for any number of agents, where alpha is a constant between 1/2 and 1, which is monotonically increasing with the value of the divisible goods relative to the MMS values.
- Bhaskar, Sricharan and Vaish study a mixture of indivisible *chores* (objects with negative utilities) and a divisible cake (with positive utility). They present an algorithm for finding an EFM allocation in two special cases: when each agent has the same preference ranking over the set of chores, and when the number of items is at most the number of agents plus 1.
- Li, Liu, Lu and Tao study truthful mechanisms for EFM. They show that, in general, no truthful EFM algorithm exists, even if there is only one indivisible good and one divisible good and only two agents. But, when agents have binary valuations on indivisible goods and identical valuations on a single divisible good, an EFM and truthful mechanism exists. When agents have binary valuations over both divisible and indivisible goods, an EFM and truthful mechanism exists when there are only two agents, or when there is a single divisible good.
- Nishimura and Sumita study the properties of the maximum Nash welfare allocation (MNW) for mixed goods. They prove that, when all agents' valuations are binary and linear for each good, an MNW allocation satisfies a property stronger than EFM, which they call "envy-freeness up to any good for mixed goods". Their results hold not only for max Nash welfare, but also for a general fairness notion based on minimizing a symmetric strictly convex function. For general additive valuations, they prove that an MNW allocation satisfies an EF approximation that is weaker than EFM.
- Kawase, Nishimura and Sumita study *optimal* allocation of mixed goods, where the utility vector should minimize a symmetric strictly-convex function (this is a generalization off Egalitarian item allocation and max Nash welfare). They assume that all agents have binary valuations. It is known that, if only divisible goods or only indivisible goods exist, the problem is polytime solvable. They show that, with mixed goods, the problem is NP-hard even when all indivisible goods are identical. In contrast, if all divisible goods are identical, a polytime algorithm exists.
- Bei, Liu and Lu study a more general setting, in which the same object can be divisible for some agents and indivisible for others. They show that the best possible approximation for MMS is 2/3, even for two agents; and present algorithms attaining this bound for 2 or 3 agents. For any number of agents, they present a 1/2-MMS approximation. They also show that EFM is incompatible with non-wastefulness.
- Li, Li, Liu and Wu study a setting in which each agent may have a different "indivisibility ratio" (= proportion of items that are indivisible). Each agent is guaranteed an allocation that is EF/PROP up to a fraction of an item, where the fraction depends on the agent's indivisibility ratio. The results are tight up to a constant for EF and asymptotically tight for PROP.
- Li, Liu, Lu, Tao and Tao study the price of fairness in both indivisible and mixed item allocation. They provide bounds for the price of EF1, EFx, EFM and EFxM. They provide tight bounds for two agents and asymptotically tight bounds for *n* agents, for both scaled and unscaled utilities.

Liu, Lu, Suzuki and Walsh survey some recent results on mixed items, and identify several open questions:

1. Is EFM compatible with Pareto-efficiency?
2. Are there efficient algorithms for maximizing Utilitarian social welfare among EFM allocations?
3. Are there bounded or even finite algorithms for computing EFM allocations in the Robertson–Webb query model?
4. Does there always exist an EFM allocation when there are indivisible chores and a cake?
5. More generally: does there always exist an EFM allocation when both divisible items and indivisible items may be positive for some agents and negative for others?
6. Is there a truthful EFM algorithm for agents with binary additive valuations?

## Variants and extensions

### Different entitlements

In this variant, different agents are entitled to different fractions of the resource. A common use-case is dividing cabinet ministries among parties in the coalition. It is common to assume that each party should receive ministries according to the number of seats it has in the parliament. The various fairness notions have to be adapted accordingly. Several classes of fairness notions were considered:

- Notions based on weighted competitive equilibrium;
- Notions based on weighted envy-freeness;
- Notions based on weighted fair share;

### Allocation to groups

In this variant, bundles are given not to individual agents but to groups of agents. Common use-cases are: dividing inheritance among families, or dividing facilities among departments in a university. All agents in the same group consume the same bundle, though they may value it differently. The classic item allocation setting corresponds to the special case in which all groups are singletons.

With groups, it may be impossible to guarantee *unanimous fairness* (fairness in the eyes of all agents in each group), so it is often relaxed to *democratic fairness* (fairness in the eyes of e.g. at least half the agents in each group).

### Allocation of public goods

In this variant, each item provides utility not only to a single agent but to all agents. Different agents may attribute different utilities to the same item. The group has to choose a subset of items satisfying some constraints, for example:

- At most *k* items can be selected. This variant is closely related to multiwinner voting, except that in multiwinner voting the number of elected candidates is usually much smaller than the number of voters, while in public goods allocation the number of chosen goods is usually much larger than the number of agents. An example is a public library that has to decide which books to purchase, respecting the preferences of the readers; the number of books is usually much larger than the number of readers.
- The total cost of all items must not exceed a fixed budget. This variant is often known as participatory budgeting.
- The number of items should be as small as possible, subject to that all agents must agree that the chosen set is better than the non-chosen set. This variant is known as the agreeable subset problem.
- There may be general matroid constraints, matching constraints or knapsack constraints on the chosen set.

Allocation of private goods can be seen as a special case of allocating public goods: given a private-goods problem with *n* agents and *m* items, where agent *i* values item *j* at *vij*, construct a public-goods problem with *n* · *m* items, where agent *i* values each item *i,j* at *vij,* and the other items at 0. Item *i,j* essentially represents the decision to give item *j* to agent *i*. This idea can be formalized to show a general reduction from private-goods allocation to public-goods allocation that retains the maximum Nash welfare allocation, as well as a similar reduction that retains the leximin optimal allocation.

Common solution concepts for public goods allocation are core stability (which implies both Pareto-efficiency and proportionality), maximum Nash welfare, leximin optimality and proportionality up to one item.

### Public decision making

In this variant, several agents have to accept decisions on several issues. A common use-case is a family that has to decide what activity to do each day (here each issue is a day). Each agent assigns different utilities to the various options in each issue. The classic item allocation setting corresponds to the special case in which each issue corresponds to an item, each decision option corresponds to giving that item to a particular agent, and the agents' utilities are zero for all options in which the item is given to someone else. In this case, proportionality means that the utility of each agent is at least 1/*n* of his "dictatorship utility", i.e., the utility he could get by picking the best option in each issue. Proportionality might be unattainable, but PROP1 is attainable by Round-robin item allocation.

### Repeated allocation

Often, the same items are allocated repeatedly. For example, recurring house chores. If the number of repetitions is a multiple of the number of agents, then it is possible to find in polynomial time a sequence of allocations that is envy-free and complete, and to find in exponential time a sequence that is proportional and Pareto-optimal. But, an envy-free and Pareto-optimal sequence may not exist. With two agents, if the number of repetitions is even, it is always possible to find a sequence that is envy-free and Pareto-optimal.

### Stochastic allocations of indivisible goods

*Stochastic allocations of indivisible goods* is a type of fair item allocation in which a solution describes a probability distribution over the set of deterministic allocations.

Assume that m items should be distributed between n agents. Formally, in the deterministic setting, a solution describes a feasible allocation of the items to the agents — a partition of the set of items into n subsets (one for each agent). The set of all deterministic allocations can be described as follows:

${\mathcal {A}}=\{(A^{1},\dots ,A^{n})\mid \forall i\in [n]\colon A^{i}\subseteq [m],\quad \forall i\neq j\in [n]\colon A^{i}\cap A^{j}=\emptyset ,\quad \cup _{i=1}^{n}A^{i}=[m]\}$

In the stochastic setting, a solution is a probability distribution over the set ${\mathcal {A}}$ . That is, the set of all stochastic allocations (i.e., all feasible solutions to the problem) can be described as follows:

${\mathcal {D}}=\{d\mid p_{d}\colon {\mathcal {A}}\to [0,1],\sum _{A\in {\mathcal {A}}}p_{d}(A)=1\}$

There are two functions related to each agent, a utility function associated with a deterministic allocation $u_{i}\colon {\mathcal {A}}\to \mathbb {R} _{+}$ ; and an expected utility function associated with a stochastic allocation $E_{i}\colon {\mathcal {D}}\to \mathbb {R} _{+}$ which defined according to $u_{i}$ as follows:

$E_{i}(d)=\sum _{A\in {\mathcal {A}}}p_{d}(A)\cdot u_{i}(A)$

#### Fairness criteria

The same criteria that are suggested for deterministic setting can also be considered in the stochastic setting:

- **Utilitarian rule**: this rule says that society should choose the solution that maximize the sum of utilities. That is, to choose a *stochastic* allocation $d^{*}\in {\mathcal {D}}$ that maximizes the *utilitarian welfare*: $d^{*}={\underset {d\in {\mathcal {D}}}{\operatorname {argmax} }}\sum _{i=1}^{n}\sum _{A\in {\mathcal {A}}}\left(p_{d}(A)\cdot u_{i}(A)\right)$ Kawase and Sumita show that maximization of the utilitarian welfare in the stochastic setting can always be achieved with a deterministic allocation. The reason is that the utilitarian value of the *deterministic* allocation $A^{*}={\underset {A\in {\mathcal {A}}\colon p_{d^{*}}(A)>0}{\operatorname {argmax} }}\sum _{i=1}^{n}u_{i}(A)$ is at least the utilitarian value of $d^{*}$ : $\sum _{i=1}^{n}\sum _{A\in {\mathcal {A}}}\left(p_{d^{*}}(A)\cdot u_{i}(A)\right)=\sum _{A\in {\mathcal {A}}}p_{d^{*}}(A)\sum _{i=1}^{n}u_{i}(A)\leq \max _{A\in {\mathcal {A}}\colon p_{d^{*}}(A)>0}\sum _{i=1}^{n}u_{i}(A)$
- **Egalitarian rule:** this rule says that society should choose the solution that maximize the utility of the poorest. That is, to choose a *stochastic* allocation $d^{*}\in {\mathcal {D}}$ that maximizes the *egalitarian welfare*: $d^{*}={\underset {d\in {\mathcal {D}}}{\operatorname {argmax} }}\min _{i=1,\ldots ,n}\sum _{A\in {\mathcal {A}}}\left(p_{d}(A)\cdot u_{i}(A)\right)$ In contrast to the utilitarian rule, here, the stochastic setting allows society to achieve higher value — as an example, consider the case where are two identical agents and only one item that worth 100. It is easy to see that in the deterministic setting the egalitarian value is 0, while in the stochastic setting it is 50.
  - **Hardness:** Kawase and Sumita prove that finding a stochastic allocation that maximizes the egalitarian welfare is NP-hard even when agents' utilities are all *budget-additive;* and also, that it is NP-hard to approximate the egalitarian welfare to a factor better than $1-{\tfrac {1}{e}}$ even when all agents have the same submodular utility function.
  - **Algorithm:** Kawase and Sumita present an algorithm that, given an algorithm for finding a deterministic allocation that approximates the utilitarian welfare to a factor α, finds a stochastic allocation that approximates the egalitarian welfare to the same factor α.
