---
title: "Schelling's model of segregation"
source: https://en.wikipedia.org/wiki/Schelling%27s_model_of_segregation
domain: agent-based-modeling
license: CC-BY-SA-4.0
tags: agent-based model, complex adaptive system, swarm intelligence, segregation model
fetched: 2026-07-02
---

# Schelling's model of segregation

**Schelling's model of segregation** is an agent-based model developed by economist Thomas Schelling. Schelling's model does not include outside factors that place pressure on agents to segregate, such as Jim Crow laws in the United States, but Schelling's work does demonstrate that having people with "mild" in-group preference towards their own group could still lead to a highly segregated society via de facto segregation.

## Model

The original model is set in an $N\times N$ grid. Agents are split into two groups and occupy the spaces of the grid and only one agent can occupy a space at a time. Agents desire a fraction $B_{\textrm {a}}$ of their neighborhood (in this case, defined to be the eight adjacent agents around them) to be from the same group. Increasing $B_{\textrm {a}}$ corresponds to increasing the agent's intolerance of outsiders.

Each round consists of agents checking their neighborhood to see if the fraction of neighbors B that matches their group—ignoring empty spaces—is greater than or equal to $B_{\textrm {a}}$ . If $B<B_{\textrm {a}}$ , then the agent will choose to relocate to a vacant spot where $B\geq B_{\textrm {a}}$ . This continues until every agent is satisfied. Every agent is not guaranteed to be satisfied, and in these cases, it is of interest to study the patterns (if any) of the agent dynamics.

While studying population dynamics of two groups of equal size, Schelling found a threshold $B_{\textrm {seg}}$ such that $B_{\textrm {a}}<B_{\textrm {seg}}$ leads to a random population configuration and $B_{\textrm {a}}\geq B_{\textrm {seg}}$ leads to a segregated configuration. The value of $B_{\textrm {seg}}$ was approximately ${\frac {1}{3}}$ . This points to how individuals with even a small amount of in-group preference can form segregated societies. There are different parameterizations and variants of the model and a 'unified' approach is presented in allowing the simulations to explore the thresholds for different segregation events to occur.

## Physical model analogies

There have been observations that the fundamental dynamics of the agents resemble the mechanics used in the Ising model of ferromagnetism. This primarily relies on the similar nature in which each occupied grid location calculates an aggregate measure based upon the similarities of the adjacent grid cells. If each agent produces a satisfaction based upon their homophilic satisfaction threshold as ${\textstyle [0,1]}$ then the summation of those values can provide an indication for the segregation of the state that is analogous to the clustering of the aligned spins in a magnetic material. If each cell is a member of a group ${\textstyle m_{n}\in {m_{1},m_{2},m_{empty}}}$ , then the local homogeneity can be found via

${\textstyle l(m_{n})=\sum _{i=-1}^{1}\sum _{j=-1}^{1}\left(\delta _{m_{(ni,nj)},m_{(ni+i,nj+j)}}:i,j\neq 0\right)}$ where the 1-d position of n can be translated into i,j coordinates of ni,nj. Then the state of whether the agent $m_{n}$ moves to a randomly empty grid cell position or 'remains' is defined by:

$r\left(m_{n}\right)={\begin{cases}\left(l\left(m_{n}\right)\geq B_{a}\right),&{\text{if}}:m_{n}\notin {m_{empty}}\\0,&{\text{if}}:m_{n}\in {m_{empty}}\end{cases}}$

Each agent produces a binary value, so that for each grid configuration of agents of both groups, a vector can be produced of the remain due to satisfaction or not. The overall satisfaction from the remain states of all the agents can be computed; ${\textstyle R=\sum _{n=1}^{N}r(m_{n})}$ .

R then provides a measure for the amount of homogeneity (segregation) on the grid and can be used with the maximum possible value (total sum of agents) as a 'density' of segregation over the simulation of movements as is performed in. Following the approach of R can be interpreted as a macrostate whose density $\Omega$ can be estimated by sampling via the Monte Carlo method the grid space from the random initialisations of the grid to produce a calculation of the entropy; ${\textstyle S=k_{B}{\text{ln}}\Omega (R).}$ This allows a trace of the entropy to be computed over the iterations of the simulation as is done with other physical systems.

## Broader model considerations

The canonical Schelling model does not consider variables which may affect the agent's ability to relocate positions in the grid. The work of Hatna and Benenson investigates a model extension where the utility available to agents to move governs this action. It can explain some of the patterns seen where groups do not segregate due to the financial barrier homogeneous zones produce as a result of high demand. The consideration of the financial aspect is also investigated in two other papers, in 2012 and 2009. The work of Mantzaris further develops this concept of the importance of the monetary factor in the decision making, and uses it to extend the model with a dual dynamic where agents radiate their income store whenever a movement is made. This also provides a means to produce a more complete model where the trace of the entropy is non-decreasing and adds support that social systems obey the Second law of thermodynamics.

Schelling's model has also been studied from a game-theoretic perspective: In *Schelling games*, agents strategically strive to maximize their utilities by relocating to a position with the highest fraction of neighboring agents from the same group.
