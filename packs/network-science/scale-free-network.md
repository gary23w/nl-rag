---
title: "Scale-free network"
source: https://en.wikipedia.org/wiki/Scale-free_network
domain: network-science
license: CC-BY-SA-4.0
tags: network science, scale-free network, small-world network, community structure
fetched: 2026-07-02
---

# Scale-free network

A **scale-free network** is a network whose degree distribution follows a power law, at least asymptotically. That is, the fraction *P*(*k*) of nodes in the network having *k* connections to other nodes goes for large values of *k* as

$P(k)\ \sim \ k^{\boldsymbol {-\gamma }}$

where $\gamma$ is a parameter whose value is typically in the range ${\textstyle 2<\gamma <3}$ (wherein the second moment (scale parameter) of $k^{\boldsymbol {-\gamma }}$ is infinite but the first moment is finite), although occasionally it may lie outside these bounds. The name "scale-free" could be explained by the fact that some moments of the degree distribution are not defined, so that the network does not have a characteristic scale or "size".

Preferential attachment and the fitness model have been proposed as mechanisms to explain the power law degree distributions in real networks. Alternative models such as super-linear preferential attachment and second-neighbour preferential attachment may appear to generate transient scale-free networks, but the degree distribution deviates from a power law as networks become very large.

## History

In studies of citations between scientific papers, Derek de Solla Price showed in 1965 that the number of citations a paper receives had a heavy-tailed distribution following a Pareto distribution or power law. In a later paper in 1976, Price also proposed a mechanism to explain the occurrence of power laws in citation networks, which he called "cumulative advantage." However, both treated citations are scalar quantities, rather than a fundamental feature of a new class of networks.

The interest in scale-free networks started in 1999 with work by Albert-László Barabási and Réka Albert at the University of Notre Dame who mapped the topology of a portion of the World Wide Web, finding that some nodes, which they called "hubs", had many more connections than others and that the network as a whole had a power-law distribution of the number of links connecting to a node. In a subsequent paper Barabási and Albert showed that the power laws are not a unique property of the WWW, but the feature is present in a few real networks, prompting them to coin the term "scale-free network" to describe the class of networks that exhibit a power-law degree distribution.

Barabási and Réka Albert proposed a generative mechanism to explain the appearance of power-law distributions, which they called "preferential attachment". Analytic solutions for this mechanism were presented in 2000 by Dorogovtsev, Mendes and Samukhin and independently by Krapivsky, Redner, and Leyvraz, and later rigorously proved by mathematician Béla Bollobás.

## Overview

When the concept of "scale-free" was initially introduced in the context of networks, it primarily referred to a specific trait: a power-law distribution for a given variable k , expressed as $f(k)\propto k^{-\gamma }$ . This property maintains its form when subjected to a continuous scale transformation $k\to k+\epsilon k$ , evoking parallels with the renormalization group techniques in statistical field theory.

However, there's a key difference. In statistical field theory, the term "scale" often pertains to system size. In the realm of networks, "scale" k is a measure of connectivity, generally quantified by a node's degree—that is, the number of links attached to it. Networks featuring a higher number of high-degree nodes are deemed to have greater connectivity.

The power-law degree distribution enables us to make "scale-free" assertions about the prevalence of high-degree nodes. For instance, we can say that "nodes with triple the average connectivity occur half as frequently as nodes with average connectivity". The specific numerical value of what constitutes "average connectivity" becomes irrelevant, whether it's a hundred or a million.

## Characteristics

The most notable characteristic in a scale-free network is the relative commonness of vertices with a degree that greatly exceeds the average. The highest-degree nodes are often called "hubs", and are thought to serve specific purposes in their networks, although this depends greatly on the domain. In a random network the maximum degree, or the expected largest hub, scales as *kmax~ log N*, where *N* is the network size, a very slow dependence. In contrast, in scale-free networks the largest hub scales as *kmax~ ~N1/(γ−1)* indicating that the hubs increase polynomically with the size of the network.

A key feature of scale-free networks is their high degree heterogeneity, κ= *<k2>/<k>*, which governs multiple network-based processes, from network robustness to epidemic spreading and network synchronization. While for a random network κ= *<k> + 1,* i.e. the ration is independent of the network size *N*, for a scale-free network we have κ*~ N(3−γ)/(γ−1)*, increasing with the network size, indicating that for these networks the degree heterogeneity increases.

### Clustering

Another important characteristic of scale-free networks is the clustering coefficient distribution, which decreases as the node degree increases. This distribution also follows a power law. This implies that the low-degree nodes belong to very dense sub-graphs and those sub-graphs are connected to each other through hubs. Consider a social network in which nodes are people and links are acquaintance relationships between people. It is easy to see that people tend to form communities, i.e., small groups in which everyone knows everyone (one can think of such community as a complete graph). In addition, the members of a community also have a few acquaintance relationships to people outside that community. Some people, however, are connected to a large number of communities (e.g., celebrities, politicians). Those people may be considered the hubs responsible for the small-world phenomenon.

At present, the more specific characteristics of scale-free networks vary with the generative mechanism used to create them. For instance, networks generated by preferential attachment typically place the high-degree vertices in the middle of the network, connecting them together to form a core, with progressively lower-degree nodes making up the regions between the core and the periphery. The random removal of even a large fraction of vertices impacts the overall connectedness of the network very little, suggesting that such topologies could be useful for security, while targeted attacks destroys the connectedness very quickly. Other scale-free networks, which place the high-degree vertices at the periphery, do not exhibit these properties. Similarly, the clustering coefficient of scale-free networks can vary significantly depending on other topological details.

### Immunization

The question of how to immunize efficiently scale free networks which represent realistic networks such as the Internet and social networks has been studied extensively. One such strategy is to immunize the largest degree nodes, i.e., targeted (intentional) attacks since for this case p c is relatively high and less nodes are needed to be immunized. However, in many realistic cases the global structure is not available and the largest degree nodes are not known.

Properties of random graph may change or remain invariant under graph transformations. Mashaghi A. et al., for example, demonstrated that a transformation which converts random graphs to their edge-dual graphs (or line graphs) produces an ensemble of graphs with nearly the same degree distribution, but with degree correlations and a significantly higher clustering coefficient. Scale free graphs, as such, remain scale free under such transformations.

## Examples

Examples of networks found to be scale-free include:

- Some Social networks, including collaboration networks. Two examples that have been studied extensively are the collaboration of movie actors in films and the co-authorship by mathematicians of papers.
- Many kinds of computer networks, including the internet, the webgraph of the World Wide Web, and software module dependency graphs.
- Some financial networks such as interbank payment networks
- Protein–protein interaction networks.
- Semantic networks.
- Airline networks.

Scale free topology has been also found in high temperature superconductors. The qualities of a high-temperature superconductor — a compound in which electrons obey the laws of quantum physics, and flow in perfect synchrony, without friction — appear linked to the fractal arrangements of seemingly random oxygen atoms and lattice distortion.

## Generative models

Scale-free networks do not arise by chance alone. Erdős and Rényi (1960) studied a model of growth for graphs in which, at each step, two nodes are chosen uniformly at random and a link is inserted between them. The properties of these random graphs are different from the properties found in scale-free networks, and therefore a model for this growth process is needed.

The most widely known generative model for a subset of scale-free networks is Barabási and Albert's (1999) rich get richer generative model in which each new Web page creates links to existing Web pages with a probability distribution which is not uniform, but proportional to the current in-degree of Web pages. According to this process, a page with many in-links will attract more in-links than a regular page. This generates a power-law but the resulting graph differs from the actual Web graph in other properties such as the presence of small tightly connected communities. More general models and network characteristics have been proposed and studied. For example, Pachon et al. (2018) proposed a variant of the rich get richer generative model which takes into account two different attachment rules: a preferential attachment mechanism and a uniform choice only for the most recent nodes. For a review see the book by Dorogovtsev and Mendes. Some mechanisms such as super-linear preferential attachment and second neighbour attachment generate networks which are transiently scale-free, but deviate from a power law as networks grow large.

A somewhat different generative model for Web links has been suggested by Pennock et al. (2002). They examined communities with interests in a specific topic such as the home pages of universities, public companies, newspapers or scientists, and discarded the major hubs of the Web. In this case, the distribution of links was no longer a power law but resembled a normal distribution. Based on these observations, the authors proposed a generative model that mixes preferential attachment with a baseline probability of gaining a link.

Another generative model is the **copy** model studied by Kumar et al. (2000), in which new nodes choose an existent node at random and copy a fraction of the links of the existent node. This also generates a power law.

There are two major components that explain the emergence of the power-law distribution in the Barabási–Albert model: the growth and the preferential attachment. By "growth" is meant a growth process where, over an extended period of time, new nodes join an already existing system, a network (like the World Wide Web which has grown by billions of web pages over 10 years). Finally, by "preferential attachment" is meant that new nodes prefer to connect to nodes that already have a high number of links with others. Thus, there is a higher probability that more and more nodes will link themselves to that one which has already many links, leading this node to a hub *in-fine*. Depending on the network, the hubs might either be assortative or disassortative. Assortativity would be found in social networks in which well-connected/famous people would tend to know better each other. Disassortativity would be found in technological (Internet, World Wide Web) and biological (protein interaction, metabolism) networks.

However, the *growth* of the networks (adding new nodes) is not a necessary condition for creating a scale-free network (see Dangalchev). One possibility (Caldarelli et al. 2002) is to consider the structure as static and draw a link between vertices according to a particular property of the two vertices involved. Once specified the statistical distribution for these vertex properties (fitnesses), it turns out that in some circumstances also static networks develop scale-free properties.

## Generalized scale-free model

There has been a burst of activity in the modeling of scale-free complex networks. The recipe of Barabási and Albert has been followed by several variations and generalizations and the revamping of previous mathematical works.

In today's terms, if a complex network has a power-law distribution of any of its metrics, it's generally considered a scale-free network. Similarly, any model with this feature is called a scale-free model.

### Features

Many real networks are (approximately) scale-free and hence require scale-free models to describe them. In Price's scheme, there are two ingredients needed to build up a scale-free model:

1. Adding or removing nodes. Usually we concentrate on growing the network, i.e. adding nodes.

2. Preferential attachment: The probability $\Pi$ that new nodes will be connected to the "old" node.

Note that some models (see Dangalchev and Fitness model below) can work also statically, without changing the number of nodes. It should also be kept in mind that the fact that "preferential attachment" models give rise to scale-free networks does not prove that this is the mechanism underlying the evolution of real-world scale-free networks, as there might exist different mechanisms at work in real-world systems that nevertheless give rise to scaling.

### Examples

There have been several attempts to generate scale-free network properties. Here are some examples:

#### The Barabási–Albert model

The Barabási–Albert model, an undirected version of Price's model has a linear preferential attachment $\Pi (k_{i})={\frac {k_{i}}{\sum _{j}k_{j}}}$ and adds one new node at every time step.

(Note, another general feature of $\Pi (k)$ in real networks is that $\Pi (0)\neq 0$ , i.e. there is a nonzero probability that a new node attaches to an isolated node. Thus in general $\Pi (k)$ has the form $\Pi (k)=A+k^{\alpha }$ , where A is the initial attractiveness of the node.)

#### Two-level network model

Dangalchev (see ) builds a 2-L model by considering the importance of each of the neighbours of a target node in preferential attachment. The attractiveness of a node in the 2-L model depends not only on the number of nodes linked to it but also on the number of links in each of these nodes.

$\Pi (k_{i})={\frac {k_{i}+C\sum _{(i,j)}k_{j}}{\sum _{j}k_{j}+C\sum _{j}k_{j}^{2}}},$

where *C* is a coefficient between 0 and 1.

A variant of the 2-L model, the k2 model, where first and second neighbour nodes contribute equally to a target node's attractiveness, demonstrates the emergence of transient scale-free networks. In the k2 model, the degree distribution appears approximately scale-free as long as the network is relatively small, but significant deviations from the scale-free regime emerge as the network grows larger. This results in the relative attractiveness of nodes with different degrees changing over time, a feature also observed in real networks.

#### Non-linear preferential attachment

The Barabási–Albert model assumes that the probability $\Pi (k)$ that a node attaches to node i is proportional to the degree k of node i . This assumption involves two hypotheses: first, that $\Pi (k)$ depends on k , in contrast to random graphs in which $\Pi (k)=p$ , and second, that the functional form of $\Pi (k)$ is linear in k .

In non-linear preferential attachment, the form of $\Pi (k)$ is not linear, and recent studies have demonstrated that the degree distribution depends strongly on the shape of the function $\Pi (k)$

Krapivsky, Redner, and Leyvraz demonstrate that the scale-free nature of the network is destroyed for nonlinear preferential attachment. The only case in which the topology of the network is scale free is that in which the preferential attachment is asymptotically linear, i.e. $\Pi (k_{i})\sim a_{\infty }k_{i}$ as $k_{i}\to \infty$ . In this case the rate equation leads to

$P(k)\sim k^{-\gamma }{\text{ with }}\gamma =1+{\frac {\mu }{a_{\infty }}}.$

This way the exponent of the degree distribution can be tuned to any value between 2 and $\infty$ .

#### Hierarchical network model

Hierarchical network models are, by design, scale free and have high clustering of nodes.

The iterative construction leads to a hierarchical network. Starting from a fully connected cluster of five nodes, we create four identical replicas connecting the peripheral nodes of each cluster to the central node of the original cluster. From this, we get a network of 25 nodes (*N* = 25). Repeating the same process, we can create four more replicas of the original cluster – the four peripheral nodes of each one connect to the central node of the nodes created in the first step. This gives *N* = 125, and the process can continue indefinitely.

#### Fitness model

The idea is that the link between two vertices is assigned not randomly with a probability *p* equal for all the couple of vertices. Rather, for every vertex *j* there is an intrinsic *fitness* *x**j* and a link between vertex *i* and *j* is created with a probability $p(x_{i},x_{j})$ . In the case of World Trade Web it is possible to reconstruct all the properties by using as fitnesses of the country their GDP, and taking

$p(x_{i},x_{j})={\frac {\delta x_{i}x_{j}}{1+\delta x_{i}x_{j}}}.$

#### Hyperbolic geometric graphs

Assuming that a network has an underlying hyperbolic geometry, one can use the framework of spatial networks to generate scale-free degree distributions. This heterogeneous degree distribution then simply reflects the negative curvature and metric properties of the underlying hyperbolic geometry.

#### Edge dual transformation to generate scale free graphs with desired properties

Starting with scale free graphs with low degree correlation and clustering coefficient, one can generate new graphs with much higher degree correlations and clustering coefficients by applying edge-dual transformation.

#### Uniform-preferential-attachment model (UPA model)

UPA model is a variant of the preferential attachment model (proposed by Pachon et al.) which takes into account two different attachment rules: a preferential attachment mechanism (with probability 1−p) that stresses the rich get richer system, and a uniform choice (with probability p) for the most recent nodes. This modification is interesting to study the robustness of the scale-free behavior of the degree distribution. It is proved analytically that the asymptotically power-law degree distribution is preserved.

## Scale-free ideal networks

In the context of network theory a **scale-free ideal network** is a random network with a degree distribution following the scale-free ideal gas density distribution. These networks are able to reproduce city-size distributions and electoral results by unraveling the size distribution of social groups with information theory on complex networks when a competitive cluster growth process is applied to the network. In models of scale-free ideal networks it is possible to demonstrate that Dunbar's number is the cause of the phenomenon known as the 'six degrees of separation'.

## Novel characteristics

For a scale-free network with n nodes and power-law exponent $\gamma >3$ , the induced subgraph constructed by vertices with degrees larger than $\log {n}\times \log ^{*}{n}$ is a scale-free network with $\gamma '=2$ , almost surely.

## The scale-free metric

On a theoretical level, refinements to the abstract definition of scale-free have been proposed. For example, Li et al. (2005) offered a potentially more precise "scale-free metric". Briefly, let *G* be a graph with edge set *E*, and denote the degree of a vertex v (that is, the number of edges incident to v ) by $\deg(v)$ . Define

$s(G)=\sum _{(u,v)\in E}\deg(u)\cdot \deg(v).$

This is maximized when high-degree nodes are connected to other high-degree nodes. Now define

$S(G)={\frac {s(G)}{s_{\max }}},$

where *s*max is the maximum value of *s*(*H*) for *H* in the set of all graphs with degree distribution identical to that of *G*. This gives a metric between 0 and 1, where a graph *G* with small *S*(*G*) is "scale-rich", and a graph *G* with *S*(*G*) close to 1 is "scale-free". This definition captures the notion of self-similarity implied in the name "scale-free".

## Estimating the power law exponent

Estimating the power-law exponent $\gamma$ of a scale-free network is typically done by using the maximum likelihood estimation with the degrees of a few uniformly sampled nodes. However, since uniform sampling does not obtain enough samples from the important heavy-tail of the power law degree distribution, this method can yield a large bias and a variance. It has been recently proposed to sample random friends (i.e., random ends of random links) who are more likely come from the tail of the degree distribution as a result of the friendship paradox. Theoretically, maximum likelihood estimation with random friends lead to a smaller bias and a smaller variance compared to classical approach based on uniform sampling.

## Not all networks are scale-free

The widespread property of the scale-free property in social, biological and technological systems does not mean that *all* real networks are scale-free. Rather, several important networks do not share this property, like networks appearing in material science, describing the bonds between the atoms in crystalline or amorphous materials. In these networks each node has the same degree, determined by chemistry. Also, the neural network of the *C. elegans* worm and the power grid, consisting of generators and switches connected by transmission lines, have been shown to have exponential degree distributions. Further, in some real-world network's scale-free quality can be stronger or weaker. For example, social networks tend to be weakly scale-free, while some technological and biological networks can be strongly scale-free.
