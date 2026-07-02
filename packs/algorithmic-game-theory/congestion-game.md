---
title: "Congestion game"
source: https://en.wikipedia.org/wiki/Congestion_game
domain: algorithmic-game-theory
license: CC-BY-SA-4.0
tags: algorithmic game theory, computational equilibrium, combinatorial auction, selfish routing
fetched: 2026-07-02
---

# Congestion game

**Congestion games** (CG) are a class of games in game theory. They represent situations which commonly occur in roads, communication networks, oligopoly markets and natural habitats. There is a set of resources (e.g. roads or communication links); there are several players who need resources (e.g. drivers or network users); each player chooses a subset of these resources (e.g. a path in the network); the delay in each resource is determined by the number of players choosing a subset that contains this resource. The cost of each player is the sum of delays among all resources he chooses. Naturally, each player wants to minimize his own delay; however, each player's choices impose a negative externality on the other players, which may lead to inefficient outcomes.

The research of congestion games was initiated by the American economist Robert W. Rosenthal in 1973. He proved that every congestion game has a Nash equilibrium in pure strategies (aka *pure Nash equilibrium*, PNE). During the proof, he in fact proved that every congestion game is an exact potential game. Later, Monderer and Shapley proved a converse result: any game with an exact potential function is equivalent to some congestion game. Later research focused on questions such as:

- Does the existence of equilibrium, as well as the existence of a potential function, extend to more general models of congestion games?
- What is the quantitative inefficiency of congestion games?
- What is the computational complexity of finding an equilibrium?

## Example

Consider a traffic net where two players originate at point O and need to get to point T. Suppose that node O is connected to node T via two paths: *O*-*A*-*T* and *O*-*B*-*T*, where A is a little closer than B (i.e. A is more likely to be chosen by each player), as in the picture at the right.

The roads from both connection points to T get easily congested, meaning the more players pass through a point, the greater the delay of each player becomes, so having both players go through the same connection point causes extra delay. Formally, the delay in each of *A**T* and *B**T* when x players go there is $x^{2}$ .

A good outcome in this game will be for the two players to "coordinate" and pass through different connection points. Can such an outcome be achieved?

The following matrix expresses the costs of the players in terms of delays depending on their choices:

| p2p1 | OAT | OBT |
|---|---|---|
| OAT | (5,5) | (2,3) |
| OBT | (3,2) | (6,6) |

The pure Nash equilibria in this game are (OAT,OBT) and (OBT,OAT): any unilateral change by one of the players increases the cost of this player (note that the values in the table are costs, so players prefer them to be smaller). In this example, the Nash equilibrium is *efficient* - the players choose different lanes and the sum of costs is minimal.

In contrast, suppose the delay in each of AT and BT when x players go there is $0.8x$ . Then the cost matrix is:

| p2p1 | OAT | OBT |
|---|---|---|
| OAT | (2.6,2.6) | (1.8,2.8) |
| OBT | (2.8,1.8) | (3.6,3.6) |

Now, the only pure Nash equilibrium is ⁠ $(OAT,OAT)$ ⁠: any player switching to OBT increases his cost from 2.6 to 2.8. An equilibrium still exists, but it is not efficient: the sum of costs is 5.2, while the sum of cost in ⁠ $(OAT,OBT)$ ⁠ and ⁠ $(OBT,OAT)$ ⁠ is 4.6.

## Basic result

### Notation

The basic definition of a CG has the following components.

- A base set E of congestible elements (also called *resources* or *factors*). In the above example, E is the set of roads (OA, AT, OB and BT).
- A set of n players. In the above example $n=2$ .
- A finite set of strategies $S_{i}$ for each player, where each strategy $P\in S_{i}$ is a subset of E.
  - In the above example, both players have the same set of strategies: $S_{1}=S_{2}=\{\{OA,AT\},\{OB,BT\}\}$ . CGs in which all players have the same set of strategies are called **symmetric CGs**. In general, different players may have different sets, for example, if each player has a different source and/or a different target. Such CGs are called **asymmetric** **CGs**.
  - In general, a strategy can be any subset of E. CGs in which a strategy can only be a path in a given graph (as in the above example) are called **network CGs**. CGs in which a strategy can only be a single resource are called **singleton CGs**.
- For each element $e\in E$ and a vector of strategies $(P_{1},P_{2},\ldots ,P_{n})$ , the *load* is defined as $x_{e}=\#\{i:e\in P_{i}\}$ .
- For each element $e\in E$ there is a **delay function** $d_{e}:\mathbb {N} \longrightarrow \mathbb {R}$ (also called **latency function** or **cost function**). Given a vector of strategies, the delay on e is $d_{e}(x_{e})$ . Each $d_{e}$ is assumed to be positive and monotone increasing.
- Given a strategy $P_{i}$ , player i experiences delay $\textstyle \sum _{e\in P_{i}}d_{e}(x_{e})$ ; each player wants to minimize his delay.
- A *Nash equilibrium* is a vector of strategies $(P_{1},P_{2},\ldots ,P_{n})$ such that, for each player i, replacing $P_{i}$ with a different strategy $Q_{i}$ would not decrease the delay experienced by i.

### Existence of Nash equilibria

Every CG has a Nash equilibrium in pure strategies. This can be shown by constructing a *potential function* that assigns a value to each outcome. Moreover, this construction will also show that iterated best response finds a Nash equilibrium. Define $\textstyle \Phi =\sum _{e\in E}\sum _{k=1}^{x_{e}}d_{e}(k)$ . Note that this function is *not* the social welfare $\textstyle \sum _{e\in E}x_{e}d_{e}(x_{e})$ , but rather a discrete integral of sorts. The critical property of a potential function for a congestion game is that if one player switches strategy, the change in his delay is equal to the change in the potential function.

Consider the case when player i switches from $P_{i}$ to $Q_{i}$ . Elements that are in both of the strategies remain unaffected, elements that the player leaves (i.e. $e\in P_{i}-Q_{i}$ ) decrease the potential by $d_{e}(x_{e})$ , and the elements the player joins (i.e. $e\in Q_{i}-P_{i}$ ) increase the potential by $d_{e}(x_{e}+1)$ . This change in potential is precisely the change in delay for player i, so $\Phi$ is in fact a potential function.

Now observe that any minimum of $\Phi$ is a pure Nash equilibrium. Fixing all but one player, any improvement in strategy by that player corresponds to decreasing $\Phi$ , which cannot happen at a minimum. Now since there are a finite number of configurations and each $d_{e}$ is monotone, there exists an equilibrium.

The existence of a potential function has an additional implication, called the **finite improvement property (FIP)**. If we start with any strategy-vector, pick a player arbitrarily, and let him change his strategy to a better strategy for him, and repeat, then the sequence of improvements must be finite (that is, the sequence will not cycle). This is because each such improvement strictly increases the potential.

### Extensions

Below we present various extensions and variations on the basic CG model.

## Nonatomic congestion games

A **nonatomic** **CG** is the limit of a standard CG with *n* players, as $n\rightarrow \infty$ . As in any nonatomic game, there is a continuum of players, the players are considered "infinitesimally small", and each individual player has a negligible effect on the congestion. Nonatomic CGs were studied by Milchtaich, Friedman, Blonsky, and Roughgarden and Tardos.

- We keep E a *finite* set of congestible elements.
- Instead of recognizing n players, as in the discrete case, we have n *types* of players, where each type i is associated with a number $r_{i}$ , representing the *rate* of traffic for that type.
- Each agent in type *i* picks a strategy from the strategy set $S_{i}$ .
- As before, the delay functions $d_{e}$ are monotone and positive, but we now add the assumption that they are continuous as well.
- We allow players in a type to distribute fractionally over their strategy set. That is, for every strategy $P\in S_{i}$ , let $f_{P}$ denote the fraction of players in type i using strategy P. By definition, $\textstyle \sum _{P\in S_{i}}f_{P}=r_{i}$ .
- For each element $e\in E$ , the *load* is defined as the sum of fractions of players using *e*, that is, $x_{e}=\sum _{P\ni e}f_{P}$ .

### Existence of equilibria in nonatomic CGs

Strategies are now collections of strategy profiles $f_{P}$ . For a strategy set $S_{i}$ of size n, the collection of all valid profiles is a compact subset of $[0,r_{i}]^{n}$ . We now define the potential function as $\textstyle \Phi =\sum _{e\in E}\int _{0}^{x_{e}}d_{e}(z)\,dz$ , replacing the discrete integral with the standard one.

As a function of the strategy, $\Phi$ is continuous: $d_{e}$ is continuous by assumption, and $x_{e}$ is a continuous function of the strategy. Then by the extreme value theorem, $\Phi$ attains its global minimum.

The final step is to show that a minimum of $\Phi$ is indeed a Nash equilibrium. Assume for contradiction that there exists a collection of $f_{P}$ that minimize $\Phi$ but are not a Nash equilibrium. Then for some type i, there exists some improvement $Q\in S_{i}$ over the current choice P. That is, $\textstyle \sum _{e\in Q}d_{e}(x_{e})<\sum _{e\in P}d_{e}(x_{e})$ . The idea now is to take a small amount $\delta <f_{P}$ of players using strategy P and move them to strategy Q. Now for any $x_{e}\in Q$ , we have increased its load by $\delta$ , so its term in $\Phi$ is now $\textstyle \int _{0}^{x_{e}+\delta }d_{e}(z)dz$ . Differentiating the integral, this change is approximately $\delta \cdot d_{e}(x_{e})$ , with error $\delta ^{2}$ . The equivalent analysis of the change holds when we look at edges in P.

Therefore, the change in potential is approximately $\textstyle \delta (\sum _{e\in Q}d_{e}(x_{e})-\sum _{e\in P}d_{e}(x_{e}))$ , which is less than zero. This is a contradiction, as then $\Phi$ was not minimized. Therefore, a minimum of $\Phi$ must be a Nash equilibrium.

## Splittable congestion games

In a **splittable CG** (also called **atomic splittable CG**), as in an atomic CG, there are finitely many players, each of whom has a certain load to transfer. As in a nonatomic CG, each player can split his load into fractional loads going through different paths, like a transportation company choosing a set of paths for mass transportation. In contrast to a nonatomic CG, each player has a non-negligible effect on the congestion.

Splittable CGs were first analyzed by Ariel Orda, Raphael Rom and Nachum Shimkin in 1993, in the context of communication networks. They show that, for a simple network with two nodes and multiple parallel links, the Nash equilibrium is unique under reasonable convexity conditions, and has some interesting monotonicity properties. For general network topologies, more complex conditions are required to guarantee the uniqueness of Nash equilibrium.

In parallel, Haurie and Marcotte studied splittable CGs in the context of transportation networks. They defined a Nash-Cournot equilibrium and provided conditions for its existence and uniqueness. They showed that, under reasonable conditions, the asymptotic behavior of this NE yield a total flow vector corresponding to a Wardrop equilibrium.

The price of anarchy in splittable CGs was studied by Gairing, Monien and Tiemann, Cominetti, Correa and Stier-Moses, Harks, and finally Roughgarden and Schoppmann.

Huang studies the effect of collusion on the social cost in splittable CGs. He shows that if the network satifies some natural structural condition, and all delay functions are affine, then collusion decreases the social cost in equilibrium. But if either of these conditions is not satisfied, collusion might decrease the social cost.

Richman and Shimkin characterize the networks that guarantee that every splittable CG has a unique PNE. Harks and Timmermans also study equilibrium uniqueness in atomic splittable polymatroid CGs.

### Computation

Marcotte presented four numeric algorithms for computing NE on congested transportation networks, and analyzed their convergence properties. Meunier and Pradeau presented a numeric algorithm, similar to the Lemke-Howson algorithm, for nonatomic network CGs with affine player-specific delay functions. Both these numeric algorithms were not shown to run in polynomial time.

Cominetti, Correa and Stier-Moses studied splittable CGs with affine player-independent delay functions: $d_{e,i}(x)=a_{e}\cdot x_{e}+b_{e}$ , where *xe* is the load on edge *e*, and *ae*,*be* are player-independent constants. They showed a convex potential function whose global minima are PNE. This means that epsilon-approximate PNEs can be computed in polytime by convex programming.

Huang also considered affine player-independent delay functions. He devised a combinatorial algorithm computing an exact PNE for splittable CGs on symmetric graphs that satisfy a natural structural condition he calls "well-designed" (for example, series–parallel graphs).

Bhaskar and Lolakapuri considered splittable network CGs with convex player-independent delay functions. They presented two algorithms for computing approximate PNE: the first is exponential in the number of players, and while the second is exponential in the number of edges. They also show that in general networks, it is NP-hard to decide if there exists a PNE where every player has cost at most some given constant *C*.

Klimm and Warode studied atomic splittable network CGs with affine player-specific delay functions $d_{e,i}(x)=a_{e,i}\cdot x_{e}+b_{e,i}$ , where *xe* is the load on edge *e*, and *aei*, *bei* are player-specific constants. They proved that computing a PNE is PPAD-complete.

Harks and Timmermans study splittable atomic CGs with singleton strategy sets - each player should split his load among the edges (not among the paths). This corresponds to a network of *m* parallel edges between the source and the target. They allow player-specific delay functions. The total cost suffered by each player *i* is $\sum _{e}x_{i,e}\cdot d_{e,i}(x)$ . They present an algorithm for computing a PNE in time $O((nm)^{3}+n^{2}m^{14}\log(D/k_{0}))$ , where *n* is the number of players, *m* the number of edges, *D* is the maximum player-specific demand, and *k*0 the smallest packet size.

They also note that computing a PNE in atomic splittable CGs with singleton strategies and affine delay funcions can be presented as a Linear complementarity problem.

## Weighted congestion games

In a **weighted** **CG**, different players may have different effects on the congestion. For example, in a road network, a truck adds congestion much more than a motorcycle. Whereas an unweighted CG is an anonymous game, a weighted CG is not anonymous, as the payoff of a player depends not only on the number of players who take each action, but also on their weight.

In general, the weight of a player may depend on the resource (**resource-specific weights**): for every player *i* and resource *e*, there is weight $w_{i,e}$ , and the load on the resource *e* is $x_{e}=\sum _{i:e\in P_{i}}w_{i,e}$ . An important special case is when the weight depends only on the player (**resource-independent weights**), that is, each player i has a weight $w_{i}$ , and $x_{e}=\sum _{i:e\in P_{i}}w_{i}$ .

### Weighted singleton CGs with resource-independent weights

Milchtaich considered the special case of weighted CGs in which each strategy is a single resource ("singleton CG"), the weights are *resource-independent*, and all players have the same strategy set. The following is proved:

- If all players have the same delay functions, then the game has the finite-improvement property (and thus has a PNE).
- If there are only two strategies (and arbitrarily many players with possibly different delay functions), then the game has the finite-improvement property (and thus has a PNE).
- If there are only two players (with possibly different delay functions), then the game has the finite-best-response property (and thus has a PNE).
- If there are three or more strategies and three or more players with different delay functions, a PNE might not exist.

### Weighted network CGs

Milchtaich considered the special case of weighted CGs in which each strategy is a path in a given undirected graph ("network CG"). He proved that every finite game can be represented as a weighted network congestion game, with nondecreasing (but not necessarily negative) cost-functions. This implies that not every such game has a PNE. Concrete examples of weighted CGs without PNE are given by Libman and Orda, as well as Goemans Mirrokni and Vetta. This raises the question of what conditions guarantee the existence of PNE.

In particular, we say that a certain graph *G guarantees* a certain property if every weighted network CG in which the underlying network is *G* has that property. Milchtaich characterized networks that guarantee the existence of PNE, as well as the finite-improvement property, with the additional condition that a player with a lower weight has weakly more allowed strategies (formally, $w_{i}<w_{j}$ implies $|S_{i}|\geq |S_{j}|$ ). He proved that:

- A graph *G* guarantees the finite-improvement property iff *G* is homeomorphic to either a *parallel network* (a graph made of one or more single-edge networks connected in parallel), or to a parallel network connected in series with one or two single-edge networks.
- A graph *G* guarantees the existence of a PNE iff *G* is homeomorphic to a connection in series of one or more networks from a set of six "allowed networks"; an equivalent condition is that no network from a set of six "forbidden network" is embedded in *G*.

In the special case in which every player is allowed to use any strategy ("public edges"), there are more networks that guarantee the existence of PNE; a complete characterization of such networks is posed as an open problem.

Milchtaich analyzes the effect of network topology on the *efficiency* of PNE:

- A graph *G* guarantees that every PNE is Pareto-efficient, iff three simple "forbidden networks" are not embedded in *G*.
- A graph *G* guarantees that Braess's paradox does not occur, iff it is a series-parallel graph.

Milchtaich analyzes the effect of network topology on the *uniqueness* of the PNE costs:

- A graph *G* guarantees that the PNE costs are unique iff *G* is a connection in series of one or more networks of several simple kinds.
- A graph *G* does *not* guarantee that PNE costs are unique iff *G* contains an embedded network of a particular simple type.

Holzman and Law-Yone also characterize the networks that guarantee that every atomic CG has a strong PNE, a unique PNE, or a Pareto-efficient PNE.

Richman and Shimkin characterize the networks that guarantee that every *splittable* CG has a unique PNE.

### General weighted CGs

We say that a class *C* of functions *guarantees* a certain property if every weighted CG in which all delay functions are elements of *C* has that property.

- Fotakis, Kontogiannis and Spirakis prove that the class of linear functions guarantees the existence of an exact potential, and hence the existence of PNE.
- Panagopoulou and Spirakis prove that the class of exponential functions guarantees the existence of a weighted potential, and hence the existence of PNE.
- Harks, Klimm and Mohring prove that a class of functions guarantees the existence of an exact potential, if and only if it contains only affine functions. This characterization remain valid when restricted to two-player games, three-resource games, singleton games, games with symmetric strategies, or games with integral weights. Moreover, a class of functions guarantees the existence of a weighted potential, if and only if either (1) it contains only affine functions, or (2) it contains only exponential functions of the form $a_{e}\cdot \exp {(\phi \cdot x_{e})}+b_{e}$ , where $\phi$ is the same for all resources. This characterization remain valid when restricted to four-player games, four-resource games, singleton games, games with symmetric strategies, or games with integral weights. For two-player games, a class of functions guarantees the existence of a weighted potential, if and only if all functions in it are of the form $a_{e}\cdot f(x_{e})+b_{e}$ , where f is a monotone function (the same for all resources).
- Harks and Klimm prove a similar result for the existence of PNE: they prove that a class of functions guarantees the existence of PNE if and only if either (1) it contains only affine functions, or (2) it contains only exponential functions of the form $a_{e}\cdot \exp {(\phi \cdot x_{e})}+b_{e}$ , where $\phi$ is the same for all resources. This characterization remain valid when restricted to three-player games. For two-player games, a class of functions guarantees the existence of PNE if and only if all functions in it are of the form $a_{e}\cdot f(x_{e})+b_{e}$ , where f is a monotone function (the same for all resources).

Gairing, Monien and Tiemann study weighted network CGs with player-specific delays. They consider both splittable and unsplittable flows. When the delay functions are linear (without a constant term, that is *be*=0), they introduce two new potential functions and derive results on computation of PNE.

### Other results

There are many other papers about weighted congestion games.

## Player-specific cost functions

The basic CG model can be extended by allowing the delay function of each resource to depend on the player. So for each resource *e* and player *i*, there is a delay function $d_{i,e}$ . Given a strategy $P_{i}$ , player i experiences delay $\textstyle \sum _{e\in P_{i}}d_{i,e}(x_{e})$ .

### Player-specific costs in singleton CGs (crowding games)

Milchtaich introduced and studied **CGs with player-specific costs** in the following special case:

- Each player chooses a single resource (such games are called **singleton CG**s);
- All players have the same set of strategies.

This special case of CG is also called a **crowding game**. It represents a setting in which several people simultaneously choose a place to go to (e.g. a room, a settlement, a restaurant), and their payoff is determined both by the place and by the number of other players choosing the same place.

In a crowding game, given a strategy $P_{i}=\{e\}$ , player i experiences delay $d_{i,e}(x_{e})$ . If the player switches to a different strategy f, his delay would be $d_{i,f}(x_{f}+1)$ ; hence, a strategy vector is a PNE iff for every player i, $d_{i,e}(x_{e})\leq d_{i,f}(x_{f}+1)$ for all *e*,*f*.

In general, CGs with player-specific delays might *not* admit a potential function. For example, suppose there are three resources x,y,z and two players A and B with the following delay functions:

- $d_{A,x}(1)<d_{A,y}(0)<d_{A,y}(2)<d_{A,z}(0)<d_{A,z}(2)<d_{A,x}(2)$
- $d_{B,y}(1)<d_{B,x}(0)<d_{B,x}(2)<d_{B,z}(0)<d_{B,z}(2)<d_{B,y}(2)$

The following is a cyclic improvement path: $(z,y)\to (y,y)\to (y,z)\to (x,z)\to (x,x)\to (z,x)\to (z,y)$ . This shows that the finite-improvement property does not hold, so the game cannot have a potential function (not even a generalized-ordinal-potential function). However:

- With only two resources, the finite improvement property holds. Hence, a PNE exists.
- With only two players, every finite best-response property holds. Hence, a PNE exists.

When there are three or more players, even best-response paths might be cyclic. However, every CG still has a PNE. The proof is constructive and shows an algorithm that finds a Nash equilibrium in at most ${n+1 \choose 2}$ steps. Moreover, every CG is weakly acyclic: for any initial strategy-vector, at least one best-response path starting at this vector has a length of at most $r{n+1 \choose 2}$ , which terminates at an equilibrium.

Every crowding game is *sequentially solvable*. This means that, for every ordering of the players, the sequential game in which each player in turn picks a strategy has a subgame-perfect equilibrium in which the players' actions are a PNE in the original simultaneous game. Every crowding game has at least one strong PNE; every strong PNE of a crowding game can be attained as a subgame-perfect equilibrium of a sequential version of the game.

In general, a crowding game might have many different PNE. For example, suppose there are *n* players and *n* resources, and the negative effect of congestion on the payoff is much higher than the positive value of the resources. Then there are n! different PNEs: every one-to-one matching of players to resources is a PNE, as no player would move to a resource occupied by another player. However, if a crowding game is replicated *m* times, then the set of PNEs converges to a single point as *m* goes to infinity. Moreover, in a "large" (nonatomic) crowding game, there is generically a unique PNE. This PNE has an interesting graph-theoretic property. Let *G* be a bipartite graph with players on one side and resources on the other side, where each player is adjacent to all the resources that his copies choose in the unique PNE. Then G contains no cycles.

### Separable cost functions

A special case of the player-specific delay functions is that the delay functions can be separated into a player-specific factor and a general factor. There are two sub-cases:

- **Multiplicatively-separable** **cost functions**: $d_{i,e}(x_{e})=a_{i,e}\cdot d(x_{e})$ , where $a_{i,e}$ is a constant that represents the base cost of resource *e* to player *i*, and *d* is a general delay function (the same for all resources).
- **Additively-separable** **cost functions**: $d_{i,e}(x_{e})=a_{i,e}+d(x_{e})$ , where $a_{i,e}$ is a constant that represents the fixed cost of resource *e* to player *i,* and *d* is a general delay function (the same for all resources).

When only pure-strategies are considered, these two notions are equivalent, since the logarithm of a product is a sum. Moreover, when players may have resource-specific weights, the setting with resource-specific delay functions can be reduced to the setting with a universal delay function. Games with separable cost functions occur in load-balancing, M/M/1 queueing, and habitat selection. The following is known about weighted singleton CGs with separable costs:

- If the base costs $a_{i,e}$ are player-independent ( $a_{i,e}=a_{e}$ for every player *i*), then the CG has the FIP, hence it has a PNE. The same holds if the base costs are resource-independent ( $a_{i,e}=a_{i}$ for every resource *e*). The proof is based on a vector-valued potential function. For each state of the game, the potential is a vector of size *n* containing the costs of all players, sorted from large to small. Whenever a player deviates to a resource with a smaller cost for him, the vector of costs becomes smaller in the leximin order.
- If the weights are player-independent (equivalently: the CG is unweighted and the delay-functions are resource-specific), then it has the FIP, hence it has a PNE. If the cost-functions are additively-separable, then the game even has an exact potential function. The result holds even if the cost functions are not monotonically-increasing with the load. If the cost-functions are not additively-separable, then FIP may not hold, and there may be no potential function, but a PNE still exists.
- If the weights are resource-independent, then a PNE exists in the following cases:
  - When there are at most *three* players, a PNE exists, though the best-response improvement property might not hold. In contrast, there is a CG with separable costs and resource-independent weights with *eight* players in which no PNE exists.
  - When cost functions are additively-separable with linear variable-cost functions, the CG has a weighted potential, hence it has the FIP, hence it has a PNE.
  - When cost functions are additively-separable with logarithmic variable-cost function, and there are at most three players, the CG has the best-response improvement property, hence it has a PNE. However, it might not have the finite-improvement property. For more than three players, the existence of PNE is open.

Every weighted *singleton* CG with separable player-specific preferences is isomorphic to a weighted *network* CG with player-independent preference.

### Network CGs with player-specific costs

Milchtaich considered the special case of CGs with player-specific costs, in which each strategy is a path in a given graph ("network CG"). He proved that every finite game can be represented as an (unweighted) network congestion game with player-specific costs, with nondecreasing (but not necessarily negative) cost-functions. A complete characterization of networks that guarantee the existence of PNE in such CGs is posed as an open problem.

## Computing a pure Nash equilibrium

### Computing an equilibrium in unweighted CGs

The proof of existence of PNE is constructive: it shows a finite algorithm (an improvement path) that always finds a PNE. This raises the question of how many steps are required to find this PNE? Fabrikant, Papadimitriou and Talwar proved:

- If all strategies are paths in a network ("network CG"), and all players have the same set of strategies ("symmetric CG"), then a PNE can be computed in polynomial time by maximizing the potential, through reduction to min-cost flow. The algorithm can be adapted to nonatomic CGs: under certain smoothness assumptions, a Nash equilibrium in such a game can be approximated in strongly-polynomial time.
- If the strategies can be general subsets, or the players may have different sets of strategies ("asymmetric CG"), then computing a PNE is PLS-complete. This implies that there are examples with exponentially-long improvement paths. It also implies that finding a Nash equilibrium reachable from a specified state is PSPACE-complete.
- For every problem in the complexity class PLS (essentially, every local search problem), there exists an ordinal potential game with polynomially many players, such that the set of pure Nash equilibria equals the set of local optima.

Even-Dar, Kesselman and Mansour analyze the number of steps required for convergence to equilibrium in a load-balancing setting.

Caragiannis, Fanelli, Gravin and Skopalik present an algorithm that computes a constant-factor approximation PNE. In particular:

- With linear delay functions, the approximation ratio is 2+ε, and the runtime is polynomial in the number of players, the number of resources, and 1/ε.
- When delay functions are degree-*d* polynomials, the approximation ratio is *d*O(*d*)*.*

Their algorithm identifies a short sequence of best-response moves, that leads to an approximate equilibrium. They also show that, for more general CGs, attaining any polynomial approximation of PNE is PLS-complete.

### Computing an equilibrium in weighted network CGs

Fotakis, Kontogiannis and Spirakis present an algorithm that, in any weighted network CG with linear delay functions, finds a PNE in pseudo-polynomial time (polynomial in the number of players *n* and the sum of players' weights *W*). Their algorithm is a greedy best-response algorithm: players enter the game in descending order of their weight, and choose a best-response to existing players' strategies.

Panagopoulou and Spirakis show empirical evidence that the algorithm of Fotakis, Kontogiannis and Spirakis in fact runs in time polynomial in *n* and log *W*. They also propose an initial strategy-vector that dramatically speeds this algorithm.

In general, a weighted network CG may not have a PNE. Milchtaich proves that deciding whether a given weighted network CG has a PNE is NP-hard even in the following cases:

- There are two players; all players are allowed to use all paths; all cost-functions are nonnegative.
- There are two players; the CG is unweighted; the costs are player-specific and nonnegative.

The proof is by reduction from the directed edge-disjoint paths problem.

Caragiannis, Fanelli, Gravin and Skopalik present an algorithm that computes a constant-factor approximation PNE in weighted CGs. In particular:

- With linear delay functions, the approximation ratio is ${\frac {3+{\sqrt {5}}}{2}}+O(\epsilon )$ , and the runtime is polynomial in the number of players, the number of resources, and 1/ε.
- When delay functions are degree-*d* polynomials, the approximation ratio is $d^{2d+o(d)}$ *.*

To prove their results, they show that, although weighted CGs may not have a potential function, every weighted CG can be *approximated* by a certain potential game. This lets them show that every weighted CG has a (*d*!)-approximate PNE. Their algorithm identifies a short sequence of best-response moves, that leads to such an approximate PNE.

## Summary of congestion game classifications

In summary, CGs can be classified according to various parameters:

- Number and splittability of players: **atomic** **CG**, **splittable CG** or **nonatomic CG**;
- Weight of players: **unweighted** **CG** or **weighted** **CG** (with **resource-independent weights** or **resource-specific weights**);
- Cost functions for different players using the same resource: **identical** or **player-specific** (with **separable** or **nonseparable** cost-functions).
- Possible strategies: one resource (**singleton** **CG**) or path in a network (**network CG**) or any subset (**general CG)**.
- Strategy sets of different players: different (**asymmetric CG**) or identical (**symmetric CG**).
