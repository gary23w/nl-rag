---
title: "Vickrey–Clarke–Groves mechanism"
source: https://en.wikipedia.org/wiki/Vickrey%E2%80%93Clarke%E2%80%93Groves_mechanism
domain: mechanism-design
license: CC-BY-SA-4.0
tags: mechanism design, incentive compatibility, vickrey clarke groves, revelation principle
fetched: 2026-07-02
---

# Vickrey–Clarke–Groves mechanism

In mechanism design, the **Vickrey–Clarke–Groves** (**VCG**) **mechanism** is a generic truthful mechanism for achieving a socially optimal solution whenever monetary transfers are available. It generalizes the Vickrey–Clarke–Groves auction into a general-purpose mechanism for social choice, which can be used to select any outcome from a set of possible outcomes. However, the VCG mechanism also has several problems which keep it from fully solving the public goods problem, including its vulnerability to collusion and the issue of participants failing to pay their bids.

## Notation

There is a set X of possible outcomes.

There are n agents, each of which has a set of outcome valuations. The valuation of agent i is represented as a function:

$v_{i}:X\to \mathbb {R} _{+}$

which expresses the value it has for each alternative, in monetary terms.

It is assumed that the agents have quasilinear utility functions; this means that, if the outcome is x and in addition the agent receives a payment $p_{i}$ (positive or negative), then the total utility of agent i is:

$u_{i}:=v_{i}(x)+p_{i}$

Our goal is to select an outcome that maximizes the sum of values, i.e.:

$x^{opt}(v)=\arg \max _{x\in X}\sum _{i=1}^{n}v_{i}(x)$

In other words, our social-choice function is utilitarian.

## Solution family

The VCG family is a family of mechanisms that implements the utilitarian welfare function. A typical mechanism in the VCG family works in the following way:

1. It asks the agents to report their value function. I.e, each agent i should report $v_{i}(x)$ for each option x .

2. Based on the agents' report-vector v , it calculates $x^{*}=x^{opt}(v)$ as above.

3. It pays, to each agent i , a sum of money equal to the total values of the *other* agents:

$p_{i}:=\sum _{j\neq i}v_{j}(x^{*})$

4. It pays, to each agent i , an additional sum, based on an arbitrary function of the values of the other agents:

$p_{i}+h_{i}(v_{-i})$

where $v_{-i}=(v_{1},\dots ,v_{i-1},v_{i+1},\dots ,v_{n})$ , that is, $h_{i}$ is a function that depends only on the valuations of the other agents.

## Truthfulness

Every mechanism in the VCG family is a truthful mechanism, that is, a mechanism where bidding the true valuation is a dominant strategy.

The trick is in step 3. The agent is paid the total value of the other agents; hence, together with its own value, the total welfare of the agent is exactly equal to the total welfare of society. Hence, the incentives of the agent are aligned with those of the society and the agent is incentivized to be truthful in order to help the mechanism achieve its goal.

The function $h_{i}$ , in step 4, does not affect the agent's incentives, since it depends only on the declarations of the other agents.

## The Clarke pivot rule

The function $h_{i}$ is a parameter of the mechanism. Every selection of $h_{i}$ yields a different mechanism in the VCG family.

We could take, for example:

$h_{i}(v_{-i})=0$

,

but then we would have to actually pay the players to participate in the auction. We would rather prefer that players give money to the mechanism.

An alternative function is:

$h_{i}(v_{-i})=-\max _{x\in X}\sum _{j\neq i}v_{j}(x)$

It is called the *Clarke pivot rule*. With the Clarke pivot rule, the total amount paid by the player is:

(social welfare of others if

i

were absent) - (social welfare of others when

i

is present).

This is exactly the externality of player i .

When the valuations of all agents are weakly-positive, the Clarke pivot rule has two important properties:

- Individual rationality: for every player *i*, $v_{i}(x)+p_{i}\geq 0$ . It means that all the players are getting positive utility by participating in the auction. No one is forced to bid.
- No positive transfers: for every player *i*, $p_{i}\leq 0$ . The mechanism does not need to pay anything to the bidders.

This makes the VCG mechanism a win-win game: the players receive the outcomes they desire, and pay an amount which is less than their gain. So the players remain with a net positive gain, and the mechanism gains a net positive payment.

## Weighted VCG mechanism

Instead of maximizing the sum of values, we may want to maximize a weighted sum:

$x^{opt}(v)=\arg \max _{x\in X}\sum _{i=1}^{n}w_{i}v_{i}(x)$

where $w_{i}$ is a weight assigned to agent i .

The VCG mechanism from above can easily be generalized by changing the price function in step 3 to:

$p_{i}:={1 \over w_{i}}\sum _{j\neq i}w_{j}v_{j}(x^{*})$

## Cost minimization

The VCG mechanism can be adapted to situations in which the goal is to minimize the sum of costs (instead of maximizing the sum of gains). Costs can be represented as negative values, so that minimization of cost is equivalent to maximization of values.

The payments in step 3 are negative: each agent has to pay the total cost incurred by all other agents. If agents are free to choose whether to participate or not, then we must make sure that their net payment is non-negative (this requirement is called individual rationality). The Clarke pivot rule can be used for this purpose: in step 4, each agent i is paid the total cost that would have been incurred by other agents, if the agent i would not participate. The net payment to agent i is its marginal contribution to reducing the total cost.

## Applications

### Auctions

The Vickrey–Clarke–Groves auction is a specific application of the VCG mechanism to the problem of selling goods. Here, X is the set of all possible allocations of items to the agents. Each agent assigns a personal monetary value to each bundle of items, and the goal is to maximize the sum of values for all agents.

A well-known special case is the Vickrey auction, or the sealed second-bid auction. Here, there is only a single item, and the set X contains $n+1$ possible outcomes: either sell the item to one of the n agents, or not to sell it at all. In step 3, the winner agent is paid 0 (since the total value of the others is 0) and the losers receive a payment equal to the declared value of the winner. In step 4, the winner pays the second-highest bid (the total value of the others had he not participated) and the losers pay the declared value of the winner (the total value of the others had they not participated). All in all, the winner pays the second-highest bid and the losers pay 0.

A VCG mechanism can also be used in a double auction. It is the most general form of incentive-compatible double-auction since it can handle a combinatorial auction with arbitrary value functions on bundles. Unfortunately, it is not budget-balanced: the total value paid by the buyers is smaller than the total value received by the sellers. Hence, in order to make it work, the auctioneer has to subsidize the trade.

### Public project

The government wants to decide whether to undertake a certain project. The cost of the project is *C*. Each citizen derives a different value from the project. The project should be undertaken if the sum of values of all citizens is more than the cost. Here, the VCG mechanism with the Clarke pivot rule means that a citizen pays a non-zero tax for that project if and only if they are pivotal, i.e., without their declaration the total value is less than *C* and with their declaration the total value is more than *C*. This taxing scheme is incentive-compatible, but again it is not budget-balanced – the total amount of tax collected is usually less than *C*.

### Quickest paths

The **quickest path** problem is a cost-minimization problem. The goal is to send a message between two points in a communication network, which is modeled as a graph. Each computer in the network is modeled as an edge in the graph. Different computers have different transmission speeds, so every edge in the network has a numeric cost equal to the number of milliseconds it takes to transmit the message. Our goal is to send the message as quickly as possible, so we want to find the path with the smallest total cost.

If we know the transmission-time of each computer (-the cost of each edge), then we can use a standard algorithm for solving the shortest path problem. If we do not know the transmission times, then we have to ask each computer to tell us its transmission-time. But, the computers have their own selfish interests so they might not tell us the truth. For example, a computer might tell us that its transmission time is very large, so that we will not bother it with our messages.

The VCG mechanism can be used to solve this problem. Here, X is the set of all possible paths; the goal is to select a path $x\in X$ with minimal total cost.

The value of an agent, $v_{i}(x)$ , is minus the time it spent on the message: it is negative if $i\in x$ and it is zero if $i\notin x$ . The payment in step 3 is negative: each agent should pay to us the total time that the other agents spent on the message (note that the value is measured in units of time. We assume that it is possible to pay computers in units of time, or that it there is a standard way to translate time to money). This means that, together with its own spent time, each agent actually loses the total time it took the message to arrive its destination, so the agent is incentivized to help the mechanism achieve the shortest transmission time.

The Clarke pivot rule can be used to make the mechanism individually-rational: after paying us the cost, each agent receives from us a positive payment, which is equal to the time it would have taken the message to arrive at its destination if the agent would not have been present. Obviously, this time is weakly larger than the time required when the agent is present, so the net gain of every agent is weakly positive. Intuitively, each agent is paid according to its marginal contribution to the transmission.

Other graph problems can be solved in a similar way, e.g. minimum spanning tree or maximum matching. A similar solution applies to the more general case where each agent holds some subset of the edges.

For another example, where the VCG mechanism provides a sub-optimal approximation, see truthful job scheduling.

## Uniqueness

A VCG mechanism implements a utilitarian social-choice function - a function that maximizes a weighted sum of values (also called an **affine maximizer**). Roberts' theorem proves that, if:

- The agents' valuation functions are unrestricted (each agent can have as value function any function from X to $\mathbb {R}$ ), and -
- There are at least three different possible outcomes ( $|X|\geq 3$ and at least three different outcomes from X can happen),

then *only* weighted utilitarian functions can be implemented. So with unrestricted valuations, the social-choice functions implemented by VCG mechanisms are the *only* functions that can be implemented truthfully.

Moreover, the price-functions of the VCG mechanisms are also unique in the following sense. If:

- The domains of the agents' valuations are connected sets (particularly, agents can have real-valued preferences and not only integral preferences);
- There is a truthful mechanism that implements a certain $Outcome$ function with certain payment functions $p_{1},\dots ,p_{n}$ ;
- There is another truthful mechanism that implements the same $Outcome$ function with different payment functions $p'_{1},\dots ,p'_{n}$ ;

Then, there exist functions $h_{1},\dots ,h_{n}$ such that, for all i :

$p'_{i}(v_{i},v_{-i})=p_{i}(v_{i},v_{-i})+h_{i}(v_{-i})$

I.e, the price functions of the two mechanisms differ only by a function that does not depend on the agent's valuation $v_{i}$ (only on the valuations of the other agents).

This means that VCG mechanisms are the only truthful mechanisms that maximize the utilitarian social-welfare.

## Computational issues

A VCG mechanism has to calculate the optimal outcome, based on the agents' reports (step 2 above). In some cases, this calculation is computationally difficult. For example, in combinatorial auctions, calculating the optimal assignment is NP-hard.

Sometimes there are approximation algorithms to the optimization problem, but, using such an approximation might make the mechanism non-truthful.
