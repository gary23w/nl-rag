---
title: "Braess's paradox"
source: https://en.wikipedia.org/wiki/Braess's_paradox
domain: algorithmic-game-theory
license: CC-BY-SA-4.0
tags: algorithmic game theory, computational equilibrium, combinatorial auction, selfish routing
fetched: 2026-07-02
---

# Braess's paradox

**Braess's paradox** is the observation that adding one or more roads to a road network can slow down overall traffic flow through it. The paradox was first discovered by Arthur Pigou in 1920, and later named after the German mathematician Dietrich Braess in 1968.

The paradox may have analogies in electrical power grids and biological systems. It has been suggested that, in theory, the improvement of a malfunctioning network could be accomplished by removing certain parts of it. The paradox has been used to explain instances of improved traffic flow when existing major roads are closed.

## Discovery and definition

Dietrich Braess, a mathematician at Ruhr University, Germany, noticed the flow in a road network could be impeded by adding a new road, when he was working on traffic modelling. His idea was that if each driver is making the optimal self-interested decision as to which route is quickest, a shortcut could be chosen too often for drivers to have the shortest travel times possible. More formally, the idea behind Braess's discovery is that the Nash equilibrium may not equate with the best overall flow through a network.

The paradox is stated as follows:

> For each point of a road network, let there be given the number of cars starting from it and the destination of the cars. Under these conditions, one wishes to estimate the distribution of traffic flow. Whether one street is preferable to another depends not only on the quality of the road, but also on the density of the flow. If every driver takes the path that looks most favourable to them, the resultant running times need not be minimal. Furthermore, it is indicated by an example that an extension of the road network may cause a redistribution of the traffic that results in longer individual running times.

Adding extra capacity to a network when the moving entities selfishly choose their route can in some cases reduce overall performance. That is because the Nash equilibrium of such a system is not necessarily optimal. The network change induces a new game structure which leads to a (multiplayer) prisoner's dilemma. In a Nash equilibrium, drivers have no incentive to change their routes. While the system is not in a Nash equilibrium, individual drivers are able to improve their respective travel times by changing the routes they take. In the case of Braess's paradox, drivers will continue to switch until they reach Nash equilibrium despite the reduction in overall performance.

If the latency functions are linear, adding an edge can never make total travel time at equilibrium worse by a factor of more than 4/3.

## Examples

Braess's paradox has a counterpart in case of a reduction of the road network, which may cause a reduction of individual commuting time.

In Seoul, South Korea, traffic around the city sped up when the Cheonggye Expressway was removed as part of the Cheonggyecheon restoration project. In Stuttgart, Germany, after investments into the road network in 1969, the traffic situation did not improve until a section of newly built road was closed for traffic again. In 1990 the temporary closing of 42nd Street in Manhattan, New York City, for Earth Day reduced the amount of congestion in the area. In 2008 Youn, Gastner and Jeong demonstrated specific routes in Boston, New York City and London where that might actually occur and pointed out roads that could be closed to reduce predicted travel times. In 2009, New York experimented with closures of Broadway at Times Square and Herald Square, which resulted in improved traffic flow and permanent pedestrian plazas.

In 2012, Paul Lecroart, of the institute of planning and development of the Île-de-France, wrote that "Despite initial fears, the removal of main roads does not cause deterioration of traffic conditions beyond the starting adjustments. The traffic transfer are limited and below expectations". He also notes that some private vehicle trips (and related economic activity) are not transferred to public transport and simply disappear ("evaporate").

The same phenomenon was also observed when road closing was not part of an urban project but the consequence of an accident. In 2012 in Rouen, a bridge was destroyed by fire. Over the next two years, other bridges were used more, but the total number of cars crossing bridges was reduced.

## Mathematical approach

### Example

Consider a road network on which 4000 drivers wish to travel from a Start point to an End point. They have two roads available to choose from, one that goes via point A and one that goes via point B.

The travel time in minutes from the Start to point A is the number of travellers (T) divided by 100, and the time to point B is a constant 45 minutes. These times are then reversed for the routes to the End point: from point A to the End point takes 45 minutes, and from B to the End point takes ${\tfrac {T}{100}}$ .

If these are the only routes available, the time needed to drive Start–A–End route with a drivers would be ${\tfrac {a}{100}}+45$ . The time needed to drive the Start–B–End route with b drivers would be ${\tfrac {b}{100}}+45$ . As there are 4000 drivers, the fact that $a+b=4000$ can be used to derive the fact that $a=b=2000$ when the system is at equilibrium. Therefore, each route takes ${\tfrac {2000}{100}}+45=65$ minutes. If either route took less time, it would not be a Nash equilibrium: a rational driver would switch from the longer route to the shorter route.

Now suppose a new road was built connecting points A and B, with an extremely short travel time of approximately 0 minutes. Suppose that the road is opened and one driver tries Start–A–B–End. To his surprise he finds that his time is ${\tfrac {2000}{100}}+{\tfrac {2001}{100}}=40.01$ minutes, a saving of almost 25 minutes. Soon, more of the 4000 drivers are trying this new route. The time taken rises from 40.01 and keeps climbing. When the number of drivers trying the new route reaches 2500, with 1500 still in the Start–B–End route, their time will be ${\tfrac {2500}{100}}+{\tfrac {4000}{100}}=65$ minutes, which is no improvement over the original route. Meanwhile, those 1500 drivers have been slowed to $45+{\tfrac {4000}{100}}=85$ minutes, a 20-minute increase. They are obliged to switch to the new route via A too, so it now takes ${\tfrac {4000}{100}}+{\tfrac {4000}{100}}=80$ minutes. Nobody has any incentive to travel A-End or Start-B because any driver trying them will take 85 minutes. Thus, the opening of the cross route triggers an irreversible change to it by everyone, costing everyone 80 minutes instead of the original 65. If every driver were to agree not to use the A–B path, or if that route were closed, every driver would benefit by a 15-minute reduction in travel time.

### Existence of an equilibrium

If one assumes the travel time for each person driving on an edge to be equal, an equilibrium will always exist.

Let $L_{e}(x)$ be the formula for the travel time of each person traveling along edge e when x people take that edge. Suppose there is a traffic graph with $x_{e}$ people driving along edge e . Let the energy of e , $E(e)$ , be

$\sum _{i=1}^{x_{e}}L_{e}(i)=L_{e}(1)+L_{e}(2)+\cdots +L_{e}(x_{e})$

(If $x_{e}=0$ let $E(e)=0$ ). Let the total energy of the traffic graph be the sum of the energies of every edge in the graph.

Take a choice of routes that minimizes the total energy. Such a choice must exist because there are finitely many choices of routes. That will be an equilibrium.

Assume, for contradiction, this is not the case. Then, there is at least one driver who can switch the route and improve the travel time. Suppose the original route is $e_{0},e_{1},\ldots ,e_{n}$ while the new route is $e'_{0},e'_{1},\ldots ,e'_{m}$ . Let E be total energy of the traffic graph, and consider what happens when the route $e_{0},e_{1},...e_{n}$ is removed. The energy of each edge $e_{i}$ will be reduced by $L_{e_{i}}(x_{e_{i}})$ and so the E will be reduced by ${\textstyle \sum _{i=0}^{n}L_{e_{i}}(x_{e_{i}})}$ . That is simply the total travel time needed to take the original route. If the new route is then added, $e'_{0},e'_{1},\ldots ,e'_{m}$ , the total energy E will be increased by the total travel time needed to take the new route. Because the new route is shorter than the original route, E must decrease relative to the original configuration, contradicting the assumption that the original set of routes minimized the total energy.

Therefore, the choice of routes minimizing total energy is an equilibrium.

### Finding an equilibrium

The above proof outlines a procedure known as best response dynamics, which finds an equilibrium for a linear traffic graph and terminates in a finite number of steps. The algorithm is termed "best response" because at each step of the algorithm, if the graph is not at equilibrium then some driver has a best response to the strategies of all other drivers and switches to that response.

Pseudocode for Best Response Dynamics:

```
Let P be some traffic pattern.
while P is not at equilibrium:
    compute the potential energy e of P
    for each driver d in P:
        for each alternate path p available to d:
            compute the potential energy n of the pattern when d takes path p
            if n < e:
                modify P so that d takes path p
continue the topmost while
```

At each step, if some particular driver could do better by taking an alternate path (a "best response"), doing so strictly decreases the energy of the graph. If no driver has a best response, the graph is at equilibrium. Since the energy of the graph strictly decreases with each step, the best response dynamics algorithm must eventually halt.

### How far from optimal is traffic at equilibrium?

If the travel time functions are linear, that is $L_{e}(x)=a_{e}x+b_{e}$ for some $a_{e},b_{e}\geq 0$ , then at worst, traffic in the energy-minimizing equilibrium is twice as bad as socially optimal.

Proof: Let Z be some traffic configuration, with associated energy $E(Z)$ and total travel time $T(Z)$ . For each edge, the energy is the sum of an arithmetic progression, and using the formula for the sum of an arithmetic progression, one can show that $E(Z)\leq T(Z)\leq 2E(Z)$ . If $Z_{o}$ is the socially-optimal traffic flow and $Z_{e}$ is the energy-minimizing traffic flow, the inequality implies that $T(Z_{e})\leq 2E(Z_{e})\leq 2E(Z_{o})\leq 2T(Z_{o})$ .

Thus, the total travel time for the energy-minimizing equilibrium is at most twice as bad as for the optimal flow.

### Effect of network topology

Mlichtaich proved that Braess's paradox occurs in a two-terminal network if and only if it is not a series-parallel graph.

### Prevalence

In 1983, Steinberg and Zangwill provided, under reasonable assumptions, the necessary and sufficient conditions for Braess's paradox to occur in a general transportation network when a new route is added. (Note that their result applies to the addition of *any* new route, not just to the case of adding a single link.) As a corollary, they obtain that Braess's paradox is about as likely to occur as not occur when a random new route is added.

## Possible non-traffic analogies

### Electricity

In 2012, scientists at the Max Planck Institute for Dynamics and Self-Organization demonstrated, through computational modelling, the potential for the phenomenon to occur in power transmission networks where power generation is decentralized.

In 2012, an international team of researchers from Institut Néel (CNRS, France), INP (France), IEMN (CNRS, France) and UCL (Belgium) published in *Physical Review Letters* a paper showing that Braess's paradox may occur in mesoscopic electron systems. In particular, they showed that adding a path for electrons in a nanoscopic network paradoxically reduced its conductance. That was shown both by simulations as well as experiments at low temperature using scanning gate microscopy.

### Springs

A model with springs and ropes can show that a hung weight can rise in height despite a taut rope in the hanging system being cut, and follows from the same mathematical structure as the original Braess's paradox.

For two identical springs joined in series by a short rope, their total spring constant is half of each individual spring, resulting in a long stretch when a certain weight is hung. This remains the case as we add two longer ropes in slack to connect the lower end of the upper spring to the hung weight (lower end of the lower spring), and the upper end of the lower spring to the hanging point (upper end of the upper spring). However, when the short rope is cut, the longer ropes become taut, and the two springs become parallel (in the mechanical sense) to each other. The total spring constant is twice that of each individual spring, and when the length of the long ropes is not too long, the hung weight will actually be higher compared to before the short rope was cut.

The fact that the hung weight rises despite cutting a taut rope (the short rope) in the hanging system is counter-intuitive, but it does follow from Hooke's law and the way springs work in series and in parallel.

### Biology

Adilson E. Motter and collaborators demonstrated that Braess's paradox outcomes may often occur in biological and ecological systems. Motter suggests removing part of a perturbed network could rescue it. For resource management of endangered species food webs, in which extinction of many species might follow sequentially, selective removal of a doomed species from the network could in principle bring about the positive outcome of preventing a series of further extinctions.

### Team sports strategy

It has been suggested that in basketball, a team can be seen as a network of possibilities for a route to scoring a basket, with a different efficiency for each pathway, and a star player could reduce the overall efficiency of the team, analogous to a shortcut that is overused increasing the overall times for a journey through a road network. A proposed solution for maximum efficiency in scoring is for a star player to shoot about the same number of shots as teammates. However, this approach is not supported by hard statistical evidence, as noted in the original paper.

### Blockchain networks

Braess's paradox has been shown to appear in blockchain payment channel networks, also known as layer-2 networks. Payment channel networks implement a solution to the scalability problem of blockchain networks, allowing transactions of high rates without recording them on the blockchain. In such a network, users can establish a channel by locking funds on each side of the channel. Transactions are executed either through a channel connecting directly the payer and payee or through a path of channels with intermediate users that ask for some fees.

While intuitively, opening new channels allows higher routing flexibility, adding a new channel might cause higher fees, and similarly closing existing channels might decrease fees. The paper presented a theoretical analysis with conditions for the paradox, methods for mitigating the paradox as well as an empirical analysis, showing the appearance in practice of the paradox and its effects on Bitcoin's Lightning network.
