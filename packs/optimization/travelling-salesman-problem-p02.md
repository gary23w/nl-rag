---
title: "Travelling salesman problem (part 2/2)"
source: https://en.wikipedia.org/wiki/Travelling_salesman_problem
domain: optimization
license: CC-BY-SA-4.0
tags: mathematical optimization, linear programming, convex optimization, simplex, lagrange multiplier
fetched: 2026-07-02
part: 2/2
---

## Computational complexity

The problem has been shown to be NP-hard (more precisely, it is complete for the complexity class FPNP; see function problem), and the decision problem version ("given the costs and a number *x*, decide whether there is a round-trip route cheaper than *x*") is NP-complete. The bottleneck travelling salesman problem is also NP-hard. The problem remains NP-hard even for the case when the cities are in the plane with Euclidean distances, as well as in a number of other restrictive cases. Removing the condition of visiting each city "only once" does not remove the NP-hardness, since in the planar case there is an optimal tour that visits each city only once (otherwise, by the triangle inequality, a shortcut that skips a repeated visit would not increase the tour length).

### Complexity of approximation

In the general case, finding a shortest travelling salesman tour is NPO-complete. If the distance measure is a metric (and thus symmetric), the problem becomes APX-complete, and the algorithm of Christofides and Serdyukov approximates it within 1.5.

If the distances are restricted to 1 and 2 (but still are a metric), then the approximation ratio becomes 8/7. In the asymmetric case with triangle inequality, in 2018, a constant factor approximation was developed by Svensson, Tarnawski, and Végh. An algorithm by Vera Traub and Jens Vygen achieves a performance ratio of 22 + ε {\displaystyle 22+\varepsilon } ({\displaystyle 22+\varepsilon }). This factor was further improved to 17 + ε {\displaystyle 17+\varepsilon } ({\displaystyle 17+\varepsilon }). The best known inapproximability bound is 75/74.

The corresponding maximization problem of finding the *longest* travelling salesman tour is approximable within 63/38. If the distance function is symmetric, then the longest tour can be approximated within 4/3 by a deterministic algorithm and within ( 33 + ε ) / 25 {\displaystyle (33+\varepsilon )/25} ({\displaystyle (33+\varepsilon )/25}) by a randomized algorithm.


## Human and animal performance

The TSP, in particular the Euclidean variant of the problem, has attracted the attention of researchers in cognitive psychology. It has been observed that humans are able to produce near-optimal solutions quickly, in a close-to-linear fashion, with performance that ranges from 1% less efficient, for graphs with 10–20 nodes, to 11% less efficient for graphs with 120 nodes. The apparent ease with which humans accurately generate near-optimal solutions to the problem has led researchers to hypothesize that humans use one or more heuristics, with the two most popular theories arguably being the convex-hull hypothesis and the crossing-avoidance heuristic. However, additional evidence suggests that human performance is quite varied, and individual differences as well as graph geometry appear to affect performance in the task. Nevertheless, results suggest that computer performance on the TSP may be improved by understanding and emulating the methods used by humans for these problems, and have also led to new insights into the mechanisms of human thought. The first issue of the *Journal of Problem Solving* was devoted to the topic of human performance on TSP, and a 2011 review listed dozens of papers on the subject.

A 2011 study in animal cognition titled "Let the Pigeon Drive the Bus," named after the children's book *Don't Let the Pigeon Drive the Bus!*, examined spatial cognition in pigeons by studying their flight patterns between multiple feeders in a laboratory in relation to the travelling salesman problem. In the first experiment, pigeons were placed in the corner of a lab room and allowed to fly to nearby feeders containing peas. The researchers found that pigeons largely used proximity to determine which feeder they would select next. In the second experiment, the feeders were arranged in such a way that flying to the nearest feeder at every opportunity would be largely inefficient if the pigeons needed to visit every feeder. The results of the second experiment indicate that pigeons, while still favoring proximity-based solutions, "can plan several steps ahead along the route when the differences in travel costs between efficient and less efficient routes based on proximity become larger." These results are consistent with other experiments done with non-primates, which have proven that some non-primates were able to plan complex travel routes. This suggests non-primates may possess a relatively sophisticated spatial cognitive ability.


## Natural computation

Humans are not the only species to show excellent efficiency. For example, when presented with a spatial configuration of food sources, the amoeboid *Physarum polycephalum* adapts its morphology to create an efficient path between the food sources, which can also be viewed as an approximate solution to TSP. Similarly, honey bees and bumblebees have been shown to be very adept at maximising efficiency to a very high degree of accuracy when collecting nectar and pollen by using collective intelligence.


## Benchmarks

For benchmarking of TSP algorithms, TSPLIB is a library of sample instances of the TSP and related problems. Many of them are lists of actual cities and layouts of actual printed circuits.


## Popular culture

- *Travelling Salesman*, by director Timothy Lanzone, is the story of four mathematicians hired by the U.S. government to solve the most elusive problem in computer-science history: P vs. NP.
- Solutions to the problem are used by mathematician Robert A. Bosch in a subgenre called TSP art.
