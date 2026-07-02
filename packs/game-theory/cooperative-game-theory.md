---
title: "Cooperative game theory"
source: https://en.wikipedia.org/wiki/Cooperative_game_theory
domain: game-theory
license: CC-BY-SA-4.0
tags: game theory, nash equilibrium, zero-sum game, cooperative game
fetched: 2026-07-02
---

# Cooperative game theory

In game theory, a **cooperative** or **coalitional game** is a game with groups of players who form binding "coalitions" with external enforcement of cooperative behavior (e.g. through contract law). This is different from non-cooperative games in which there is either no possibility to forge alliances or all agreements need to be self-enforcing (e.g. through credible threats).

Cooperative games are analysed by focusing on coalitions that can be formed, and the joint actions that groups can take and the resulting collective payoffs.

## Mathematical definition

A cooperative game is given by specifying a value for every coalition. Formally, the coalitional game consists of a finite set of players N , called the *grand coalition*, and a *characteristic function* $v:2^{N}\to \mathbb {R}$ from the set of all possible coalitions of players to a set of payments that satisfies $v(\emptyset )=0$ . The function describes how much collective payoff a set of players can gain by forming a coalition.

## Key attributes

Cooperative game theory is a branch of game theory that deals with the study of games where players can form coalitions, cooperate with one another, and make binding agreements. The theory offers mathematical methods for analysing scenarios in which two or more players are required to make choices that will affect other players wellbeing.

- **Common interests:** In cooperative games, players share a common interest in achieving a specific goal or outcome. The players must identify and agree on a common interest to establish the foundation and reasoning for cooperation. Once the players have a clear understanding of their shared interest, they can work together to achieve it.
- **Necessary information exchange:** Cooperation requires communication and information exchange among the players. Players must share information about their preferences, resources, and constraints to identify opportunities for mutual gain. By sharing information, players can better understand each other's goals and work towards achieving them together.
- **Voluntariness, equality, and mutual benefit:** In cooperative games, players voluntarily come together to form coalitions and make agreements. The players must be equal partners in the coalition, and any agreements must be mutually beneficial. Cooperation is only sustainable if all parties feel they are receiving a fair share of the benefits.
- **Compulsory contract:** In cooperative games, agreements between players are binding and mandatory. Once the players have agreed to a particular course of action, they have an obligation to follow through. The players must trust each other to keep their commitments, and there must be mechanisms in place to enforce the agreements. By making agreements binding and mandatory, players can ensure that they will achieve their shared goal.

## Subgames

Let $S\subsetneq N$ be a non-empty coalition of players. The *subgame* $v_{S}:2^{S}\to \mathbb {R}$ on S is naturally defined as

$v_{S}(T)=v(T),\forall ~T\subseteq S.$

In other words, we simply restrict our attention to coalitions contained in S . Subgames are useful because they allow us to apply solution concepts defined for the grand coalition on smaller coalitions.

## Mathematical properties

### Superadditivity

Characteristic functions are often assumed to be superadditive (Owen 1995, p. 213). This means that the value of a union of disjoint coalitions is no less than the sum of the coalitions' separate values:

$v(S\cup T)\geq v(S)+v(T)$ whenever $S,T\subseteq N$ satisfy $S\cap T=\emptyset$ .

### Monotonicity

Larger coalitions gain more:

$S\subseteq T\Rightarrow v(S)\leq v(T)$ .

This follows from superadditivity. i.e. if payoffs are normalized so singleton coalitions have zero value.

### Properties for simple games

A coalitional game v is considered **simple** if payoffs are either 1 or 0, i.e. coalitions are either "winning" or "losing".

Equivalently, a **simple game** can be defined as a collection W of coalitions, where the members of W are called **winning** coalitions, and the others **losing** coalitions. It is sometimes assumed that a simple game is nonempty or that it does not contain an empty set. However, in other areas of mathematics, simple games are also called hypergraphs or Boolean functions (logic functions).

- A simple game W is **monotonic** if any coalition containing a winning coalition is also winning, that is, if $S\in W$ and $S\subseteq T$ imply $T\in W$ .
- A simple game W is **proper** if the complement (opposition) of any winning coalition is losing, that is, if $S\in W$ implies $N\setminus S\notin W$ .
- A simple game W is **strong** if the complement of any losing coalition is winning, that is, if $S\notin W$ implies $N\setminus S\in W$ .
  - If a simple game W is proper and strong, then a coalition is winning if and only if its complement is losing, that is, $S\in W$ iff $N\setminus S\notin W$ . (If v is a coalitional simple game that is proper and strong, $v(S)=1-v(N\setminus S)$ for any S.)
- A **veto player** (vetoer) in a simple game is a player that belongs to all winning coalitions. Supposing there is a veto player, any coalition not containing a veto player is losing. A simple game W is **weak** (*collegial*) if it has a veto player, that is, if the intersection $\bigcap W:=\bigcap _{S\in W}S$ of all winning coalitions is nonempty.
  - A **dictator** in a simple game is a veto player such that any coalition containing this player is winning. The dictator does not belong to any losing coalition. (Dictator games in experimental economics are unrelated to this.)
- A **carrier** of a simple game W is a set $T\subseteq N$ such that for any coalition S, we have $S\in W$ iff $S\cap T\in W$ . When a simple game has a carrier, any player not belonging to it is ignored. A simple game is sometimes called *finite* if it has a finite carrier (even if N is infinite).
- The **Nakamura number** of a simple game is the minimal number of *winning coalitions* with empty intersection. According to Nakamura's theorem, the number measures the degree of rationality; it is an indicator of the extent to which an aggregation rule can yield well-defined choices.

A few relations among the above axioms have widely been recognized, such as the following (e.g., Peleg, 2002, Section 2.1):

- If a simple game is weak, it is proper.
- A simple game is dictatorial if and only if it is strong and weak.

More generally, a complete investigation of the relation among the four conventional axioms (monotonicity, properness, strongness, and non-weakness), finiteness, and algorithmic computability has been made (Kumabe and Mihara, 2011), whose results are summarized in the Table "Existence of Simple Games" below.

| Type | Finite Non-comp | Finite Computable | Infinite Non-comp | Infinite Computable |
|---|---|---|---|---|
| 1111 | No | Yes | Yes | Yes |
| 1110 | No | Yes | No | No |
| 1101 | No | Yes | Yes | Yes |
| 1100 | No | Yes | Yes | Yes |
| 1011 | No | Yes | Yes | Yes |
| 1010 | No | No | No | No |
| 1001 | No | Yes | Yes | Yes |
| 1000 | No | No | No | No |
| 0111 | No | Yes | Yes | Yes |
| 0110 | No | No | No | No |
| 0101 | No | Yes | Yes | Yes |
| 0100 | No | Yes | Yes | Yes |
| 0011 | No | Yes | Yes | Yes |
| 0010 | No | No | No | No |
| 0001 | No | Yes | Yes | Yes |
| 0000 | No | No | No | No |

The restrictions that various axioms for simple games impose on their Nakamura number were also studied extensively. In particular, a computable simple game without a veto player has a Nakamura number greater than 3 only if it is a *proper* and *non-strong* game.

## Relation with non-cooperative theory

Let *G* be a strategic (non-cooperative) game. Then, assuming that coalitions have the ability to enforce coordinated behaviour, there are several cooperative games associated with *G*. These games are often referred to as *representations of G*. The two standard representations are:

- The α-effective game associates with each coalition the sum of gains its members can 'guarantee' by joining forces. By 'guaranteeing', it is meant that the value is the max-min, e.g. the maximal value of the minimum taken over the opposition's strategies.
- The β-effective game associates with each coalition the sum of gains its members can 'strategically guarantee' by joining forces. By 'strategically guaranteeing', it is meant that the value is the min-max, e.g. the minimal value of the maximum taken over the opposition's strategies.

## Solution concepts

The main assumption in cooperative game theory is that the grand coalition N will form. The challenge is then to allocate the payoff $v(N)$ among the players in some way. (This assumption is not restrictive, because even if players split off and form smaller coalitions, we can apply solution concepts to the subgames defined by whatever coalitions actually form.) A *solution concept* is a vector $x\in \mathbb {R} ^{N}$ (or a set of vectors) that represents the allocation to each player. Researchers have proposed different solution concepts based on different notions of fairness. Some properties to look for in a solution concept include:

- Efficiency: The payoff vector exactly splits the total value: $\sum _{i\in N}x_{i}=v(N)$ .
- Individual rationality: No player receives less than what he could get on his own: $x_{i}\geq v(\{i\}),\forall ~i\in N$ .
- Existence: The solution concept exists for any game v .
- Uniqueness: The solution concept is unique for any game v .
- Marginality: The payoff of a player depends only on the marginal contribution of this player, i.e., if these marginal contributions are the same in two different games, then the payoff is the same: $v(S\cup \{i\})=w(S\cup \{i\}),\forall ~S\subseteq N\setminus \{i\}$ implies that $x_{i}$ is the same in v and in w .
- Monotonicity: The payoff of a player increases if the marginal contribution of this player increase: $v(S\cup \{i\})\leq w(S\cup \{i\}),\forall ~S\subseteq N\setminus \{i\}$ implies that $x_{i}$ is weakly greater in w than in v .
- Computational ease: The solution concept can be calculated efficiently (i.e. in polynomial time with respect to the number of players $|N|$ .)
- Symmetry: The solution concept x allocates equal payments $x_{i}=x_{j}$ to symmetric players i , j . Two players i , j are *symmetric* if $v(S\cup \{i\})=v(S\cup \{j\}),\forall ~S\subseteq N\setminus \{i,j\}$ ; that is, we can exchange one player for the other in any coalition that contains only one of the players and not change the payoff.
- Additivity: The allocation to a player in a sum of two games is the sum of the allocations to the player in each individual game. Mathematically, if v and $\omega$ are games, the game $(v+\omega )$ simply assigns to any coalition the sum of the payoffs the coalition would get in the two individual games. An additive solution concept assigns to every player in $(v+\omega )$ the sum of what he would receive in v and $\omega$ .
- Zero Allocation to Null Players: The allocation to a null player is zero. A *null player* i satisfies $v(S\cup \{i\})=v(S),\forall ~S\subseteq N\setminus \{i\}$ . In economic terms, a null player's marginal value to any coalition that does not contain him is zero.

An efficient payoff vector is called a *pre-imputation*, and an individually rational pre-imputation is called an imputation. Most solution concepts are imputations.

### The stable set

The stable set of a game (also known as the *von Neumann-Morgenstern solution* (von Neumann & Morgenstern 1944)) was the first solution proposed for games with more than 2 players. Let v be a game and let x , y be two imputations of v . Then x *dominates* y if some coalition $S\neq \emptyset$ satisfies $x_{i}>y_{i},\forall ~i\in S$ and $\sum _{i\in S}x_{i}\leq v(S)$ . In other words, players in S prefer the payoffs from x to those from y , and they can threaten to leave the grand coalition if y is used because the payoff they obtain on their own is at least as large as the allocation they receive under x .

A *stable set* is a set of imputations that satisfies two properties:

- Internal stability: No payoff vector in the stable set is dominated by another vector in the set.
- External stability: All payoff vectors outside the set are dominated by at least one vector in the set.

Von Neumann and Morgenstern saw the stable set as the collection of acceptable behaviours in a society: None is clearly preferred to any other, but for each unacceptable behaviour there is a preferred alternative. The definition is very general allowing the concept to be used in a wide variety of game formats.

#### Properties

- A stable set may or may not exist (Lucas 1969), and if it exists it is typically not unique (Lucas 1992). Stable sets are usually difficult to find. This and other difficulties have led to the development of many other solution concepts.
- A positive fraction of cooperative games have unique stable sets consisting of the core (Owen 1995, p. 240).
- A positive fraction of cooperative games have stable sets which discriminate $n-2$ players. In such sets at least $n-3$ of the discriminated players are excluded (Owen 1995, p. 240).

### The core

Let v be a game. The *core* of v is the set of payoff vectors

$C(v)=\left\{x\in \mathbb {R} ^{N}:\sum _{i\in N}x_{i}=v(N);\quad \sum _{i\in S}x_{i}\geq v(S),\forall ~S\subseteq N\right\}.$

In words, the core is the set of imputations under which no coalition has a value greater than the sum of its members' payoffs. Therefore, no coalition has incentive to leave the grand coalition and receive a larger payoff.

#### Properties

- The core of a game may be empty (see the Bondareva–Shapley theorem). Games with non-empty cores are called *balanced*.
- If it is non-empty, the core does not necessarily contain a unique vector.
- The core is contained in any stable set, and if the core is stable it is the unique stable set; see (Driessen 1988) for a proof.

### The core of a simple game with respect to preferences

For simple games, there is another notion of the core, when each player is assumed to have preferences on a set X of alternatives. A *profile* is a list $p=(\succ _{i}^{p})_{i\in N}$ of individual preferences $\succ _{i}^{p}$ on X . Here $x\succ _{i}^{p}y$ means that individual i prefers alternative x to y at profile p . Given a simple game v and a profile p , a *dominance* relation $\succ _{v}^{p}$ is defined on X by $x\succ _{v}^{p}y$ if and only if there is a winning coalition S (i.e., $v(S)=1$ ) satisfying $x\succ _{i}^{p}y$ for all $i\in S$ . The *core* $C(v,p)$ of the simple game v with respect to the profile p of preferences is the set of alternatives undominated by $\succ _{v}^{p}$ (the set of maximal elements of X with respect to $\succ _{v}^{p}$ ):

$x\in C(v,p)$

if and only if there is no

$y\in X$

such that

$y\succ _{v}^{p}x$

.

The *Nakamura number* of a simple game is the minimal number of winning coalitions with empty intersection. *Nakamura's theorem* states that the core $C(v,p)$ is nonempty for all profiles p of *acyclic* (alternatively, *transitive*) preferences if and only if X is finite *and* the cardinal number (the number of elements) of X is less than the Nakamura number of v . A variant by Kumabe and Mihara states that the core $C(v,p)$ is nonempty for all profiles p of preferences that have a *maximal element* if and only if the cardinal number of X is less than the Nakamura number of v . (See Nakamura number for details.)

### The strong epsilon-core

Because the core may be empty, a generalization was introduced in (Shapley & Shubik 1966). The *strong $\varepsilon$ -core* for some number $\varepsilon \in \mathbb {R}$ is the set of payoff vectors

$C_{\varepsilon }(v)=\left\{x\in \mathbb {R} ^{N}:\sum _{i\in N}x_{i}=v(N);\quad \sum _{i\in S}x_{i}\geq v(S)-\varepsilon ,\forall ~S\subseteq N\right\}.$

In economic terms, the strong $\varepsilon$ -core is the set of pre-imputations where no coalition can improve its payoff by leaving the grand coalition, if it must pay a penalty of $\varepsilon$ for leaving. $\varepsilon$ may be negative, in which case it represents a bonus for leaving the grand coalition. Clearly, regardless of whether the core is empty, the strong $\varepsilon$ -core will be non-empty for a large enough value of $\varepsilon$ and empty for a small enough (possibly negative) value of $\varepsilon$ . Following this line of reasoning, the *least-core*, introduced in (Maschler, Peleg & Shapley 1979), is the intersection of all non-empty strong $\varepsilon$ -cores. It can also be viewed as the strong $\varepsilon$ -core for the smallest value of $\varepsilon$ that makes the set non-empty (Bilbao 2000).

### The Shapley value

The *Shapley value* is the unique payoff vector that is efficient, symmetric, and satisfies monotonicity. It was introduced by Lloyd Shapley (Shapley 1953) who showed that it is the unique payoff vector that is efficient, symmetric, additive, and assigns zero payoffs to dummy players. The Shapley value of a superadditive game is individually rational, but this is not true in general. (Driessen 1988)

### The kernel

Let $v:2^{N}\to \mathbb {R}$ be a game, and let $x\in \mathbb {R} ^{N}$ be an efficient payoff vector. The *maximum surplus* of player *i* over player *j* with respect to *x* is

$s_{ij}^{v}(x)=\max \left\{v(S)-\sum _{k\in S}x_{k}:S\subseteq N\setminus \{j\},i\in S\right\},$

the maximal amount player *i* can gain without the cooperation of player *j* by withdrawing from the grand coalition *N* under payoff vector *x*, assuming that the other players in *i'*s withdrawing coalition are satisfied with their payoffs under *x*. The maximum surplus is a way to measure one player's bargaining power over another. The *kernel* of v is the set of imputations *x* that satisfy

- $(s_{ij}^{v}(x)-s_{ji}^{v}(x))\times (x_{j}-v(j))\leq 0$ , and
- $(s_{ji}^{v}(x)-s_{ij}^{v}(x))\times (x_{i}-v(i))\leq 0$

for every pair of players *i* and *j*. Intuitively, player *i* has more bargaining power than player *j* with respect to imputation *x* if $s_{ij}^{v}(x)>s_{ji}^{v}(x)$ , but player *j* is immune to player *i'*s threats if $x_{j}=v(j)$ , because he can obtain this payoff on his own. The kernel contains all imputations where no player has this bargaining power over another. This solution concept was first introduced in (Davis & Maschler 1965).

### Harsanyi dividend

The *Harsanyi dividend* (named after John Harsanyi, who used it to generalize the Shapley value in 1963) identifies the surplus that is created by a coalition of players in a cooperative game. To specify this surplus, the worth of this coalition is corrected by subtracting the surplus that was already created by subcoalitions. To this end, the dividend $d_{v}(S)$ of coalition S in game v is recursively determined by

${\begin{aligned}d_{v}(\{i\})&=v(\{i\})\\d_{v}(\{i,j\})&=v(\{i,j\})-d_{v}(\{i\})-d_{v}(\{j\})\\d_{v}(\{i,j,k\})&=v(\{i,j,k\})-d_{v}(\{i,j\})-d_{v}(\{i,k\})-d_{v}(\{j,k\})-d_{v}(\{i\})-d_{v}(\{j\})-d_{v}(\{k\})\\&\vdots \\d_{v}(S)&=v(S)-\sum _{T\subsetneq S}d_{v}(T)\end{aligned}}$

An explicit formula for the dividend is given by ${\textstyle d_{v}(S)=\sum _{T\subseteq S}(-1)^{|S\setminus T|}v(T)}$ . The function $d_{v}:2^{N}\to \mathbb {R}$ is also known as the Möbius inverse of $v:2^{N}\to \mathbb {R}$ . Indeed, we can recover v from $d_{v}$ by help of the formula ${\textstyle v(S)=d_{v}(S)+\sum _{T\subsetneq S}d_{v}(T)}$ .

Harsanyi dividends are useful for analyzing both games and solution concepts, e.g. the Shapley value is obtained by distributing the dividend of each coalition among its members, i.e., the Shapley value $\phi _{i}(v)$ of player i in game v is given by summing up a player's share of the dividends of all coalitions that she belongs to, ${\textstyle \phi _{i}(v)=\sum _{S\subset N:i\in S}{d_{v}(S)}/{|S|}}$ .

### The nucleolus

Let $v:2^{N}\to \mathbb {R}$ be a game, and let $x\in \mathbb {R} ^{N}$ be a payoff vector. The *excess* of x for a coalition $S\subseteq N$ is the quantity $v(S)-\sum _{i\in S}x_{i}$ ; that is, the gain that players in coalition S can obtain if they withdraw from the grand coalition N under payoff x and instead take the payoff $v(S)$ . The *nucleolus* of v is the imputation for which the vector of excesses of all coalitions (a vector in $\mathbb {R} ^{2^{N}}$ ) is smallest in the leximin order. The nucleolus was introduced in (Schmeidler 1969).

(Maschler, Peleg & Shapley 1979) gave a more intuitive description: Starting with the least-core, record the coalitions for which the right-hand side of the inequality in the definition of $C_{\varepsilon }(v)$ cannot be further reduced without making the set empty. Continue decreasing the right-hand side for the remaining coalitions, until it cannot be reduced without making the set empty. Record the new set of coalitions for which the inequalities hold at equality; continue decreasing the right-hand side of remaining coalitions and repeat this process as many times as necessary until all coalitions have been recorded. The resulting payoff vector is the nucleolus.

#### Properties

- Although the definition does not explicitly state it, the nucleolus is always unique. (See Section II.7 of (Driessen 1988) for a proof.)
- If the core is non-empty, the nucleolus is in the core.
- The nucleolus is always in the kernel, and since the kernel is contained in the bargaining set, it is always in the bargaining set (see (Driessen 1988) for details.)

## Convex cooperative games

Introduced by Shapley in (Shapley 1971), convex cooperative games capture the intuitive property some games have of "snowballing". Specifically, a game is *convex* if its characteristic function v is supermodular:

$v(S\cup T)+v(S\cap T)\geq v(S)+v(T),\forall ~S,T\subseteq N.$

It can be shown (see, e.g., Section V.1 of (Driessen 1988)) that the supermodularity of v is equivalent to

$v(S\cup \{i\})-v(S)\leq v(T\cup \{i\})-v(T),\forall ~S\subseteq T\subseteq N\setminus \{i\},\forall ~i\in N;$

that is, "the incentives for joining a coalition increase as the coalition grows" (Shapley 1971), leading to the aforementioned snowball effect. For cost games, the inequalities are reversed, so that we say the cost game is *convex* if the characteristic function is submodular.

### Properties

Convex cooperative games have many nice properties:

- Supermodularity trivially implies superadditivity.
- Convex games are *totally balanced*: The core of a convex game is non-empty, and since any subgame of a convex game is convex, the core of any subgame is also non-empty.
- A convex game has a unique stable set that coincides with its core.
- The Shapley value of a convex game is the center of gravity of its core.
- An extreme point (vertex) of the core can be found in polynomial time using the greedy algorithm: Let $\pi :N\to N$ be a permutation of the players, and let $S_{i}=\{j\in N:\pi (j)\leq i\}$ be the set of players ordered 1 through i in $\pi$ , for any $i=0,\ldots ,n$ , with $S_{0}=\emptyset$ . Then the payoff $x\in \mathbb {R} ^{N}$ defined by $x_{i}=v(S_{\pi (i)})-v(S_{\pi (i)-1}),\forall ~i\in N$ is a vertex of the core of v . Any vertex of the core can be constructed in this way by choosing an appropriate permutation $\pi$ .

### Similarities and differences with combinatorial optimization

Submodular and supermodular set functions are also studied in combinatorial optimization. Many of the results in (Shapley 1971) have analogues in (Edmonds 1970), where submodular functions were first presented as generalizations of matroids. In this context, the core of a convex cost game is called the *base polyhedron*, because its elements generalize base properties of matroids.

However, the optimization community generally considers submodular functions to be the discrete analogues of convex functions (Lovász 1983), because the minimization of both types of functions is computationally tractable. Unfortunately, this conflicts directly with Shapley's original definition of supermodular functions as "convex".

## The relationship between cooperative game theory and firm

Corporate strategic decisions can develop and create value through cooperative game theory. This means that cooperative game theory can become the strategic theory of the firm, and different CGT solutions can simulate different institutions.
