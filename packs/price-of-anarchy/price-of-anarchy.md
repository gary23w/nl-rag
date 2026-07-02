---
title: "Price of anarchy"
source: https://en.wikipedia.org/wiki/Price_of_anarchy
domain: price-of-anarchy
license: CC-BY-SA-4.0
tags: price of anarchy, price of stability, congestion game, braess paradox
fetched: 2026-07-02
---

# Price of anarchy

The **Price of Anarchy** (**PoA**) is a concept in economics and game theory that measures how the efficiency of a system degrades due to selfish behavior of its agents. It is a general notion that can be extended to diverse systems and notions of efficiency. For example, consider the system of transportation of a city and many agents trying to go from some initial location to a destination. Here, efficiency means the average time for an agent to reach the destination. In the 'centralized' solution, a central authority can tell each agent which path to take in order to minimize the average travel time. In the 'decentralized' version, each agent chooses its own path. The Price of Anarchy measures the ratio between average travel time in the two cases.

Usually the system is modeled as a game and the efficiency is some function of the outcomes (e.g. maximum delay in a network, congestion in a transportation system, social welfare in an auction, etc.). Different concepts of equilibrium can be used to model the selfish behavior of the agents, among which the most common is the Nash equilibrium. Different flavors of Nash equilibrium lead to variations of the notion of Price of Anarchy as **Pure Price of Anarchy** (for deterministic equilibria), **Mixed Price of Anarchy** (for randomized equilibria), and **Bayes–Nash Price of Anarchy** (for games with incomplete information). Solution concepts other than Nash equilibrium lead to variations such as the **Price of Sinking**.

The term Price of Anarchy was first used by Elias Koutsoupias and Christos Papadimitriou, but the idea of measuring inefficiency of equilibrium is older. The concept in its current form was designed to be the analogue of the 'approximation ratio' in an approximation algorithm or the 'competitive ratio' in an online algorithm. This is in the context of the current trend of analyzing games using algorithmic lenses (algorithmic game theory).

## Mathematical definition

Consider a game $G=(N,S,u)$ , defined by a set of players N , strategy sets $S_{i}$ for each player and utilities $u_{i}:S\rightarrow \mathbb {R}$ (where $S=S_{1}\times ...\times S_{n}$ also called set of outcomes). We can define a measure of efficiency of each outcome which we call welfare function $\operatorname {Welf} :S\rightarrow \mathbb {R}$ . Natural candidates include the sum of players utilities (utilitarian objective) $\operatorname {Welf} (s)=\sum _{i\in N}u_{i}(s),$ minimum utility (fairness or egalitarian objective) $\operatorname {Welf} (s)=\min _{i\in N}u_{i}(s),$ ..., or any function that is meaningful for the particular game being analyzed and is desirable to be maximized.

We can define a subset $Equil\subseteq S$ to be the set of strategies in equilibrium (for example, the set of Nash equilibria). The Price of Anarchy is then defined as the ratio between the optimal 'centralized' solution and 'worst equilibrium':

$PoA={\frac {\max _{s\in S}\operatorname {Welf} (s)}{\min _{s\in Equil}\operatorname {Welf} (s)}}$

If, instead of a 'welfare' which we want to 'maximize', the function measure efficiency is a 'cost function' $\operatorname {Cost} :S\rightarrow \mathbb {R}$ which we want to 'minimize' (e.g. delay in a network) we use (following the convention in approximation algorithms):

$PoA={\frac {\max _{s\in Equil}\operatorname {Cost} (s)}{\min _{s\in S}\operatorname {Cost} (s)}}$

A related notion is that of the **Price of Stability** (**PoS**) which measures the ratio between the optimal 'centralized' solution and the 'best equilibrium':

$PoS={\frac {\max _{s\in S}\operatorname {Welf} (s)}{\max _{s\in Equil}\operatorname {Welf} (s)}}$

or in the case of cost functions:

$PoS={\frac {\min _{s\in Equil}\operatorname {Cost} (s)}{\min _{s\in S}\operatorname {Cost} (s)}}$

We know that $1\leq PoS\leq PoA$ by the definition. It is expected that the loss in efficiency due to game-theoretical constraints is somewhere between 'PoS' and 'PoA'.

## Examples

### Prisoner's dilemma

Consider the 2x2 game called prisoner's dilemma, given by the following cost matrix:

|   | Cooperate | Defect |
|---|---|---|
| Cooperate | 1, 1 | 7, 0 |
| Defect | 0, 7 | 5, 5 |

and let the cost function be $C(s_{1},s_{2})=u_{1}(s_{1},s_{2})+u_{2}(s_{1},s_{2}).$ Now, the worst (and only) Nash Equilibrium would be when both players defect and the resulting cost is $C_{equil}=5+5=10$ . However, the highest social welfare occurs when both cooperate, in which case the cost is $C_{min}=1+1=2$ . Thus the PoA of this game will be $C_{equil}/C_{min}=10/2=5$ .

Since the game has a unique Nash equilibrium, the PoS is equal to the PoA and it is 5 too.

### Job scheduling

A more natural example is the one of **job scheduling**. There are N players and each of them has a job to run. They can choose one of M machines to run the job. The Price of Anarchy compares the situation where the selection of machines is guided/directed centrally to the situation where each player chooses the machine that will make its job run fastest.

Each machine has a speed $s_{1},\ldots ,s_{M}>0.$ Each job has a weight $w_{1},\ldots ,w_{N}>0.$ A player picks a machine to run his or her job on. So, the strategies of each player are $A_{i}=\{1,2,\ldots ,M\}.$ Define the *load* on machine j to be:

$L_{j}(a)={\frac {\sum _{i:a_{i}=j}w_{i}}{s_{j}}}.$

The cost for player i is $c_{i}(a)=L_{a_{i}}(a),$ i.e., the load of the machine they chose. We consider the egalitarian cost function ${\mbox{MS}}(a)=\max _{j}L_{j}(a)$ , here called the *makespan.*

We consider two concepts of equilibrium: pure Nash and mixed Nash. It should be clear that mixed PoA ≥ pure PoA, because any pure Nash equilibrium is also a mixed Nash equilibrium (this inequality can be strict: e.g. when $N=2$ , $w_{1}=w_{2}=1$ , $M=2$ , and $s_{1}=s_{2}=1$ , the mixed strategies $\sigma _{1}=\sigma _{2}=(1/2,1/2)$ achieve an average makespan of 1.5, while any pure-strategy PoA in this setting is $\leq 4/3$ ). First we need to argue that there exist pure Nash equilibria.

**Claim**. For each job scheduling game, there exists at least one pure-strategy Nash equilibrium.

**Proof**. We would like to take a socially optimal action profile $a^{*}$ . This would mean simply an action profile whose makespan is minimum. However, this will not be enough. There may be several such action profiles leading to a variety of different loads distributions (all having the same maximum load). Among these, we further restrict ourselves to one that has a minimum second-largest load. Again, this results in a set of possible load distributions, and we repeat until the M th-largest (i.e., smallest) load, where there can only be one distribution of loads (unique up to permutation). This would also be called the *lexicographic* smallest sorted load vector.

We claim that this is a pure-strategy Nash equilibrium. Reasoning by contradiction, suppose that some player i could strictly improve by moving from machine j to machine k . This means that the increased load of machine k after the move is still smaller than the load of machine j before the move. As the load of machine j must decrease as a result of the move and no other machine is affected, this means that the new configuration is guaranteed to have reduced the j th-largest (or higher ranked) load in the distribution. This, however, violates the assumed lexicographic minimality of a .***Q.E.D.***

**Claim**. For each job scheduling game, the pure PoA is at most M .

**Proof**. It is easy to upper-bound the welfare obtained at any mixed-strategy Nash equilibrium $\sigma$ by

$w(\sigma )\leq {\frac {\sum _{i}{w_{i}}}{\max _{j}{s_{j}}}}.$

Consider, for clarity of exposition, any pure-strategy action profile a : clearly

$w(a)\geq {\frac {\sum _{i}{w_{i}}}{\sum _{j}{s_{j}}}}\geq {\frac {\sum _{i}{w_{i}}}{M\cdot \max _{j}{s_{j}}}}.$

Since the above holds for the social optimum as well, comparing the ratios $w(\sigma )$ and $w(a)$ proves the claim. ***Q.E.D***

### Selfish Routing

#### Braess's paradox

Consider a road network as shown in the adjacent diagram on which 4000 drivers wish to travel from point Start to End. The travel time in minutes on the Start–A road is the number of travelers (T) divided by 100, and on Start–B is a constant 45 minutes (likewise with the roads across from them). If the dashed road does not exist (so the traffic network has 4 roads in total), the time needed to drive Start–A–End route with a drivers would be ${\tfrac {a}{100}}+45$ . The time needed to drive the Start–B–End route with b drivers would be ${\tfrac {b}{100}}+45$ . As there are 4000 drivers, the fact that $a+b=4000$ can be used to derive the fact that $a=b=2000$ when the system is at equilibrium. Therefore, each route takes ${\tfrac {2000}{100}}+45=65$ minutes. If either route took less time, it would not be a Nash equilibrium: a rational driver would switch from the longer route to the shorter route.

Now suppose the dashed line A–B is a road with an extremely short travel time of approximately 0 minutes. Suppose that the road is opened and one driver tries Start–A–B–End. To his surprise he finds that his time is ${\tfrac {2000}{100}}+{\tfrac {2001}{100}}=40.01$ minutes, a saving of almost 25 minutes. Soon, more of the 4000 drivers are trying this new route. The time taken rises from 40.01 and keeps climbing. When the number of drivers trying the new route reaches 2500, with 1500 still in the Start–B–End route, their time will be ${\tfrac {2500}{100}}+{\tfrac {4000}{100}}=65$ minutes, which is no improvement over the original route. Meanwhile, those 1500 drivers have been slowed to $45+{\tfrac {4000}{100}}=85$ minutes, a 20-minute increase. They are obliged to switch to the new route via A too, so it now takes ${\tfrac {4000}{100}}+{\tfrac {4000}{100}}=80$ minutes. Nobody has any incentive to travel A-End or Start-B because any driver trying them will take 85 minutes. Thus, the opening of the cross route triggers an irreversible change to it by everyone, costing everyone 80 minutes instead of the original 65. If every driver were to agree not to use the A–B path, or if that route were closed, every driver would benefit by a 15-minute reduction in travel time.

#### Generalized routing problem

The routing problem introduced in the Braess's paradox can be generalized to many different flows traversing the same graph at the same time.

**Definition (Generalized flow)**. Let $G=(V,E)$ , L and w be as defined above, and suppose that we want to route the quantities $R=\{r_{1},r_{2},\dots ,r_{k},\;|\;r_{i}>0\}$ through each distinct pair of nodes in $\Gamma =\{(s_{1},t_{1}),(s_{2},t_{2}),\dots ,(s_{k},t_{k})\}\subseteq (V\times V)$ . A *flow* $f_{\Gamma ,R}$ is defined as an assignment $p\mapsto \Re$ of a real, nonnegative number to each *path* p going from $s_{i}$ to $t_{i}$ $\in \Gamma$ , with the constraint that

$\sum _{p:\,s_{i}\rightarrow t_{i}}{f_{p}}=r_{i}\;\;\forall (s_{i},t_{i})\in \Gamma .$

The flow traversing a specific edge of G is defined as

$f_{e,\Gamma ,R}=\sum _{p:\,e\in p}{f_{p}}.$

For succinctness, we write $f_{e}$ when $\Gamma ,R$ are clear from context.

**Definition (Nash-equilibrium flow)**. A flow $f_{\Gamma ,R}$ is a *Nash-equilibrium flow* iff $\forall (s_{i},t_{i})\in \Gamma$ and $\forall p,q$ from $s_{i}$ to $t_{i}$

$f_{p}>0\Rightarrow \sum _{e\in p}{l_{e}(f_{e})}\leq \sum _{e\in q}{l_{e}(f_{e})}.$

This definition is closely related to what we said about the support of mixed-strategy Nash equilibria in normal-form games.

**Definition (Conditional welfare of a flow)**. Let $f_{\Gamma ,R}$ and $f_{\Gamma ,R}^{*}$ be two flows in G associated with the same sets $\Gamma$ and R . In what follows, we will drop the subscript to make the notation clearer. Assume to fix the latencies induced by f on the graph: the *conditional welfare* of $f^{*}$ with respect to f is defined as

$w^{f}(f^{*})=\sum _{e\in E}{f_{e}^{*}\cdot l_{e}(f_{e})}$

**Fact 1**. Given a Nash-equilibrium flow f and any other flow $f^{*}$ , $w(f)=w^{f}(f)\leq w^{f}(f^{*})$ .

**Proof (By contradiction)**. Assume that $w^{f}(f^{*})<w^{f}(f)$ . By definition,

$\sum _{i=1}^{k}\sum _{p:s_{i}\rightarrow t_{i}}f_{p}^{*}\cdot \sum _{e\in p}l_{e}(f_{e})<\sum _{i=1}^{k}\sum _{p:s_{i}\rightarrow t_{i}}f_{p}\cdot \sum _{e\in p}l_{e}(f_{e})$

.

Since f and $f^{*}$ are associated with the same sets $\Gamma ,R$ , we know that

$\sum _{p:s_{i}\rightarrow t_{i}}f_{p}=\sum _{p:s_{i}\rightarrow t_{i}}f_{p}^{*}=r_{i}\;\;\forall i.$

Therefore, there must be a pair $(s_{i},t_{i})$ and two paths $p,q$ from $s_{i}$ to $t_{i}$ such that $f_{p}^{*}>f_{p}$ , $f_{q}^{*}<f_{q}$ , and

$\sum _{e\in p}l_{e}(f_{e})<\sum _{e\in q}l_{e}(f_{e}).$

In other words, the flow $f^{*}$ can achieve a lower welfare than f only if there are two paths from $s_{i}$ to $t_{i}$ having different costs, and if $f^{*}$ reroutes some flow of f from the higher-cost path to the lower-cost path. This situation is clearly incompatible with the assumption that f is a Nash-equilibrium flow.***Q.E.D.***

Note that Fact 1 does not assume any particular structure on the set L .

**Fact 2**. Given any two real numbers x and y , $x\cdot y\leq x^{2}+y^{2}/4$ .

**Proof**. This is another way to express the true inequality $(x-y/2)^{2}\geq 0$ . ***Q.E.D.***

**Theorem**. The pure PoA of any generalized routing problem $(G,L)$ with linear latencies is $\leq 4/3$ .

**Proof**. Note that this theorem is equivalent to saying that for each Nash-equilibrium flow f , $w(f)\leq (4/3)\cdot \min _{f^{*}}\{w(f^{*})\}$ , where $f^{*}$ is any other flow. By definition,

$w^{f}(f^{*})=\sum _{e\in E}f_{e}^{*}(a_{e}\cdot f_{e}+b_{e})$

$=\sum _{e}(a_{e}f_{e}f_{e}^{*})+\sum _{e\in E}f_{e}^{*}b_{e}.$

By using Fact 2, we have that

$w^{f}(f^{*})\leq \sum _{e\in E}\left(a_{e}\cdot \left((f_{e}^{*})^{2}+(f_{e})^{2}/4\right)\right)+\sum _{e\in E}f_{e}^{*}\cdot b_{e}$

$=\left(\sum _{e\in E}a_{e}(f_{e}^{*})^{2}+f_{e}^{*}b_{e}\right)+\sum _{e\in E}a_{e}(f_{e})^{2}/4$

$\leq w(f^{*})+{\frac {w(f)}{4}},$

since

$(1/4)\cdot w(f)=(1/4)\cdot \sum _{e\in E}f_{e}(a_{e}f_{e}+b_{e})$

$=(1/4)\cdot \sum _{e\in E}(f_{e})^{2}+\underbrace {(1/4)\cdot \sum _{e\in E}f_{e}b_{e}} _{\geq 0}.$

We can conclude that $w^{f}(f^{*})\leq w(f^{*})+w(f)/4$ , and prove the thesis using Fact 1. ***Q.E.D.***

Note that in the proof we have made extensive use of the assumption that the functions in L are linear. Actually, a more general fact holds.

**Theorem**. Given a generalized routing problem with graph G and polynomial latency functions of degree d with nonnegative coefficients, the pure PoA is $\leq d+1$ .

Note that the PoA can grow with d . Consider the example shown in the following figure, where we assume unit flow: the Nash-equilibrium flows have social welfare 1; however, the best welfare is achieved when $x=1-1/{\sqrt {d+1}}$ , in which case

$w=\left(1-{\frac {1}{\sqrt {d+1}}}\right)^{d}\cdot \left(1-{\frac {1}{\sqrt {d+1}}}\right)+1\cdot {\frac {1}{\sqrt {d+1}}}$

$=\left(\left(1-{\frac {1}{\sqrt {d+1}}}\right)^{\sqrt {d+1}}\right)^{\sqrt {d+1}}+{\frac {1}{\sqrt {d+1}}}$

$\leq e^{-{\sqrt {d+1}}}+{\frac {1}{\sqrt {d+1}}}.$

This quantity tends to zero when d tends to infinity.

## Further results

PoA upper bounds can be obtained if the game is shown to satisfy a so-called *smoothness* inequality. More precisely, a cost-minimimization game is **(*λ*,*μ*)-smooth** (with λ ≥ 0 and μ < 1) if the inequality

$\sum _{i=1}^{n}C_{i}\left(a_{i}^{*},a_{-i}\right)\leq \lambda C\left(a^{*}\right)+\mu C(a)$

holds for any outcome *a* and *a**. In this case, the PoA is upper bounded by *λ*/(1 − *μ*).

For cost-sharing games with concave cost functions, the optimal cost-sharing rule that optimizes the price of anarchy, followed by the price of stability, is precisely the Shapley value cost-sharing rule. (A symmetrical statement is similarly valid for utility-sharing games with convex utility functions.) In mechanism design, this means that the Shapley value solution concept is optimal for these sets of games.

Moreover, for these (finite) games it was proven that every equilibrium which achieves the PoA bound is fragile, in the sense that the agents demonstrate a state of indifference between their equilibrium action and the action they would pursue in a system-optimal outcome.
