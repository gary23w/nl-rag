---
title: "Ising model (part 1/2)"
source: https://en.wikipedia.org/wiki/Ising_model
domain: computational-physics
license: CC-BY-SA-4.0
tags: computational physics, verlet integration, n-body simulation, ising model
fetched: 2026-07-02
part: 1/2
---

# Ising model

The **Ising model** (or **Lenz–Ising model**), named after the physicists Ernst Ising and Wilhelm Lenz, is a mathematical model of ferromagnetism in statistical mechanics. The model consists of discrete variables that represent magnetic dipole moments of atomic "spins" that can be in one of two states (+1 or −1). The spins are arranged in a graph, usually a lattice (where the local structure repeats periodically in all directions), allowing each spin to interact with its neighbors. Neighboring spins that agree have a lower energy than those that disagree; the system tends to the lowest energy but heat disturbs this tendency, thus creating the possibility of different structural phases. The two-dimensional square-lattice Ising model is one of the simplest statistical models to show a phase transition. Though it is a highly simplified model of a magnetic material, the Ising model can still provide qualitative and sometimes quantitative results applicable to real physical systems, and in general, it can be seen as a specialization of Stanley's *n*-vector model for *n* = 1.

The Ising model was invented by the physicist Wilhelm Lenz (1920), who gave it as a problem to his student Ernst Ising. The one-dimensional Ising model was solved by Ising (1925) alone in his 1924 thesis; it has no phase transition. The two-dimensional square-lattice Ising model is much harder and was only given an analytic description much later, by Lars Onsager (1944). It is usually solved by a transfer-matrix method, although there exists a very simple approach relating the model to a non-interacting fermionic quantum field theory.

In dimensions greater than four, the phase transition of the Ising model is described by mean-field theory. The Ising model for greater dimensions was also explored with respect to various tree topologies in the late 1970s, culminating in an exact solution of the zero-field, time-independent Barth (1981) model for closed Cayley trees of arbitrary branching ratio, and thereby, arbitrarily large dimensionality within tree branches. The solution to this model exhibited a new, unusual phase transition behavior, along with non-vanishing long-range and nearest-neighbor spin-spin correlations, deemed relevant to large neural networks as one of its possible applications.

The Ising problem without an external field can be equivalently formulated as a graph maximum cut (Max-Cut) problem that can be solved via combinatorial optimization.


## Definition

Consider a set $\Lambda$ of lattice sites, each with a set of adjacent sites (e.g. a graph) forming a d -dimensional lattice. For each lattice site $k\in \Lambda$ there is a discrete variable $\sigma _{k}$ such that $\sigma _{k}\in \{-1,+1\}$ , representing the site's spin. A *spin configuration*, ${\sigma }=\{\sigma _{k}\}_{k\in \Lambda }$ is an assignment of spin value to each lattice site.

For any two adjacent sites $i,j\in \Lambda$ there is an *interaction* $J_{ij}$ . Also a site $j\in \Lambda$ has an *external magnetic field* $h_{j}$ interacting with it. The *energy* of a configuration ${\sigma }$ is given by the Hamiltonian function

$H(\sigma )=-\sum _{\langle ij\rangle }J_{ij}\sigma _{i}\sigma _{j}-\mu \sum _{j}h_{j}\sigma _{j},$

where the first sum is over pairs of adjacent spins (every pair is counted once). The notation $\langle ij\rangle$ indicates that sites i and j are nearest neighbors. The magnetic moment is given by $\mu$ . Note that the sign in the second term of the Hamiltonian above should actually be positive because the electron's magnetic moment is antiparallel to its spin, but the negative term is used conventionally. The Ising Hamiltonian is an example of a pseudo-Boolean function; tools from the analysis of Boolean functions can be applied to describe and study it.

The *configuration probability* is given by the Boltzmann distribution with inverse temperature $\beta \geq 0$ :

$P_{\beta }(\sigma )={\frac {e^{-\beta H(\sigma )}}{Z_{\beta }}},$

where $\beta =1/(k_{\text{B}}T)$ , and the normalization constant

$Z_{\beta }=\sum _{\sigma }e^{-\beta H(\sigma )}$

is the partition function. For a function f of the spins ("observable"), one denotes by

$\langle f\rangle _{\beta }=\sum _{\sigma }f(\sigma )P_{\beta }(\sigma )$

the expectation (mean) value of f .

The configuration probabilities $P_{\beta }(\sigma )$ represent the probability that (in equilibrium) the system is in a state with configuration $\sigma$ .

### Discussion

The minus sign on each term of the Hamiltonian function $H(\sigma )$ is conventional. Using this sign convention, Ising models can be classified according to the sign of the interaction: if, for a pair *i*, *j*

- $J_{ij}>0$ , the interaction is called ferromagnetic,
- $J_{ij}<0$ , the interaction is called antiferromagnetic,
- $J_{ij}=0$ , the spins are *noninteracting*.

The system is called ferromagnetic or antiferromagnetic if all interactions are ferromagnetic or all are antiferromagnetic. The original Ising models were ferromagnetic, and it is still often assumed that "Ising model" means a ferromagnetic Ising model.

In a ferromagnetic Ising model, spins desire to be aligned: the configurations in which adjacent spins are of the same sign have higher probability. In an antiferromagnetic model, adjacent spins tend to have opposite signs.

The sign convention of *H*(σ) also explains how a spin site *j* interacts with the external field. Namely, the spin site wants to line up with the external field. If:

- $h_{j}>0$ , the spin site *j* desires to line up in the positive direction,
- $h_{j}<0$ , the spin site *j* desires to line up in the negative direction,
- $h_{j}=0$ , there is no external influence on the spin site.

### Simplifications

Ising models are often examined without an external field interacting with the lattice, that is, *h* = 0 for all *j* in the lattice Λ. Using this simplification, the Hamiltonian becomes

$H(\sigma )=-\sum _{\langle i~j\rangle }J_{ij}\sigma _{i}\sigma _{j}.$

When the external field is zero everywhere, *h* = 0, the Ising model is symmetric under switching the value of the spin in all the lattice sites; a nonzero field breaks this symmetry.

Another common simplification is to assume that all of the nearest neighbors ⟨*ij*⟩ have the same interaction strength. Then we can set *Jij* = *J* for all pairs *i*, *j* in Λ. In this case the Hamiltonian is further simplified to

$H(\sigma )=-J\sum _{\langle i~j\rangle }\sigma _{i}\sigma _{j}.$

### Connection to graph maximum cut

A subset S of the vertex set V(G) of a weighted undirected graph G determines a cut of the graph G into S and its complementary subset G\S. The size of the cut is the sum of the weights of the edges between S and G\S. A maximum cut size is at least the size of any other cut, varying S.

For the Ising model without an external field on a graph G, the Hamiltonian becomes the following sum over the graph edges E(G)

$H(\sigma )=-\sum _{ij\in E(G)}J_{ij}\sigma _{i}\sigma _{j}$

.

Here each vertex i of the graph is a spin site that takes a spin value $\sigma _{i}=\pm 1$ . A given spin configuration $\sigma$ partitions the set of vertices $V(G)$ into two $\sigma$ -depended subsets, those with spin up $V^{+}$ and those with spin down $V^{-}$ . We denote by $\delta (V^{+})$ the $\sigma$ -depended set of edges that connects the two complementary vertex subsets $V^{+}$ and $V^{-}$ . The *size* $\left|\delta (V^{+})\right|$ of the cut $\delta (V^{+})$ to bipartite the weighted undirected graph G can be defined as

$\left|\delta (V^{+})\right|={\frac {1}{2}}\sum _{ij\in \delta (V^{+})}W_{ij},$

where $W_{ij}$ denotes a weight of the edge $ij$ and the scaling 1/2 is introduced to compensate for double counting the same weights $W_{ij}=W_{ji}$ .

The identities

${\begin{aligned}H(\sigma )&=-\sum _{ij\in E(V^{+})}J_{ij}-\sum _{ij\in E(V^{-})}J_{ij}+\sum _{ij\in \delta (V^{+})}J_{ij}\\&=-\sum _{ij\in E(G)}J_{ij}+2\sum _{ij\in \delta (V^{+})}J_{ij},\end{aligned}}$

where the total sum in the first term does not depend on $\sigma$ , imply that minimizing $H(\sigma )$ in $\sigma$ is equivalent to minimizing $\sum _{ij\in \delta (V^{+})}J_{ij}$ . Defining the edge weight $W_{ij}=-J_{ij}$ thus turns the Ising problem without an external field into a graph Max-Cut problem maximizing the cut size $\left|\delta (V^{+})\right|$ , which is related to the Ising Hamiltonian as follows,

$H(\sigma )=\sum _{ij\in E(G)}W_{ij}-4\left|\delta (V^{+})\right|.$

### Questions

A significant number of statistical questions to ask about this model are in the limit of large numbers of spins:

- In a typical configuration, are most of the spins +1 or −1, or are they split equally?
- If a spin at any given position *i* is 1, what is the probability that the spin at position *j* is also 1?
- If *β* is changed, is there a phase transition?
- On a lattice Λ, what is the fractal dimension of the shape of a large cluster of +1 spins?


## Basic properties and history

The most studied case of the Ising model is the translation-invariant ferromagnetic zero-field model on a *d*-dimensional lattice, namely, Λ = **Z***d*, *J**ij* = 1, *h* = 0.

### No phase transition in one dimension

In his 1924 PhD thesis, Ising solved the model for the *d* = 1 case, which can be thought of as a linear horizontal lattice where each site only interacts with its left and right neighbor. In one dimension, the solution admits no phase transition. Namely, for any positive β, the correlations ⟨σ*i*σ*j*⟩ decay exponentially in |*i* − *j*|: $\langle \sigma _{i}\sigma _{j}\rangle _{\beta }\leq C\exp \left(-c(\beta )|i-j|\right),$

and the system is disordered. On the basis of this result, he incorrectly concluded that this model does not exhibit phase behaviour in any dimension.

### Phase transition and exact solution in two dimensions

The Ising model undergoes a phase transition between an ordered and a disordered phase in 2 dimensions or more. Namely, the system is disordered for small β, whereas for large β the system exhibits ferromagnetic order:

$\langle \sigma _{i}\sigma _{j}\rangle _{\beta }\geq c(\beta )>0.$

This was first proven by Rudolf Peierls in 1936, using what is now called a **Peierls argument**.

The Ising model on a two-dimensional square lattice with no magnetic field was analytically solved by Lars Onsager (1944). Onsager obtained the correlation functions and free energy of the Ising model and announced the formula for the spontaneous magnetization for the 2-dimensional model in 1949 but did not give a derivation. Yang (1952) gave the first published proof of this formula, using a limit formula for Fredholm determinants, proved in 1951 by Szegő in direct response to Onsager's work.

### Correlation inequalities

A number of correlation inequalities have been derived rigorously for the Ising spin correlations (for general lattice structures), which have enabled mathematicians to study the Ising model both on and off criticality.

#### Griffiths inequality

Given any subset of spins $\sigma _{A}$ and $\sigma _{B}$ on the lattice, the following inequality holds,

$\langle \sigma _{A}\sigma _{B}\rangle \geq \langle \sigma _{A}\rangle \langle \sigma _{B}\rangle ,$

where $\langle \sigma _{A}\rangle =\langle \prod _{j\in A}\sigma _{j}\rangle$ .

With $B=\emptyset$ , the special case $\langle \sigma _{A}\rangle \geq 0$ results.

This means that spins are positively correlated on the Ising ferromagnet. An immediate application of this is that the magnetization of any set of spins $\langle \sigma _{A}\rangle$ is increasing with respect to any set of coupling constants $J_{B}$ .

#### Simon-Lieb inequality

The Simon-Lieb inequality states that for any set S disconnecting x from y (e.g. the boundary of a box with x being inside the box and y being outside),

$\langle \sigma _{x}\sigma _{y}\rangle \leq \sum _{z\in S}\langle \sigma _{x}\sigma _{z}\rangle \langle \sigma _{z}\sigma _{y}\rangle .$

This inequality can be used to establish the sharpness of phase transition for the Ising model.

#### FKG inequality

This inequality is proven first for a type of positively-correlated percolation model, of which includes a representation of the Ising model. It is used to determine the critical temperatures of planar Potts model using percolation arguments (which includes the Ising model as a special case).


## Historical significance

While the laws of chemical bonding made it clear to nineteenth century chemists that atoms were real, among physicists the debate continued well into the early twentieth century. Atomists, notably James Clerk Maxwell and Ludwig Boltzmann, applied Hamilton's formulation of Newton's laws to large systems, and found that the statistical behavior of the atoms correctly describes room temperature gases. But classical statistical mechanics did not account for all of the properties of liquids and solids, nor of gases at low temperature.

Once modern quantum mechanics was formulated, atomism was no longer in conflict with experiment, but this did not lead to a universal acceptance of statistical mechanics, which went beyond atomism. Josiah Willard Gibbs had given a complete formalism to reproduce the laws of thermodynamics from the laws of mechanics. But many faulty arguments survived from the 19th century, when statistical mechanics was considered dubious. The lapses in intuition mostly stemmed from the fact that the limit of an infinite statistical system has many zero-one laws which are absent in finite systems: an infinitesimal change in a parameter can lead to big differences in the overall, aggregate behavior.

### No phase transitions in finite volume

In the early part of the twentieth century, some believed that the partition function could never describe a phase transition, based on the following argument:

1. The partition function is a sum of *e*−β*E* over all configurations.
2. The exponential function is everywhere analytic as a function of β.
3. The sum of analytic functions is an analytic function.

This argument works for a finite sum of exponentials, and correctly establishes that there are no singularities in the free energy of a system of a finite size. For systems which are in the thermodynamic limit (that is, for infinite systems) the infinite sum can lead to singularities. The convergence to the thermodynamic limit is fast, so that the phase behavior is apparent already on a relatively small lattice, even though the singularities are smoothed out by the system's finite size.

This was first established by Rudolf Peierls in the Ising model.

### Peierls droplets

Shortly after Lenz and Ising constructed the Ising model, Peierls was able to explicitly show that a phase transition occurs in two dimensions.

To do this, he compared the high-temperature and low-temperature limits. At infinite temperature (β = 0) all configurations have equal probability. Each spin is completely independent of any other, and if typical configurations at infinite temperature are plotted so that plus/minus are represented by black and white, they look like television snow. For high, but not infinite temperature, there are small correlations between neighboring positions, the snow tends to clump a little bit, but the screen stays randomly looking, and there is no net excess of black or white.

A quantitative measure of the excess is the **magnetization**, which is the average value of the spin:

$M={\frac {1}{N}}\sum _{i=1}^{N}\sigma _{i}.$

A bogus argument analogous to the argument in the last section now establishes that the *average* magnetization in the Ising model is always zero.

1. Every configuration of spins has equal energy to the configuration with all spins flipped.
2. So for every configuration with magnetization *M* there is a configuration with magnetization −*M* with equal probability.
3. The system should therefore spend equal amounts of time in the configuration with magnetization *M* as with magnetization −*M*.
4. So the average magnetization (over all time) is zero.

As before, this only proves that the average magnetization is zero at any finite volume. For an infinite system, fluctuations might not be able to push the system from a mostly plus state to a mostly minus with a nonzero probability.

For very high temperatures, the magnetization is zero, as it is at infinite temperature. To see this, note that if spin A has only a small correlation ε with spin B, and B is only weakly correlated with C, but C is otherwise independent of A, the amount of correlation of A and C goes like ε2. For two spins separated by distance *L*, the amount of correlation goes as ε*L*, but if there is more than one path by which the correlations can travel, this amount is enhanced by the number of paths.

The number of paths of length *L* on a square lattice in *d* dimensions is $N(L)=(2d)^{L},$ since there are 2*d* choices for where to go at each step.

A bound on the total correlation is given by the contribution to the correlation by summing over all paths linking two points, which is bounded above by the sum over all paths of length *L* divided by $\sum _{L}(2d)^{L}\varepsilon ^{L},$ which goes to zero when ε is small.

At low temperatures (β ≫ 1) the configurations are near the lowest-energy configuration, the one where all the spins are plus or all the spins are minus. Peierls asked whether it is statistically possible at low temperature, starting with all the spins minus, to fluctuate to a state where most of the spins are plus. For this to happen, droplets of plus spin must be able to congeal to make the plus state.

The energy of a droplet of plus spins in a minus background is proportional to the perimeter of the droplet L, where plus spins and minus spins neighbor each other. For a droplet with perimeter *L*, the area is somewhere between (*L* − 2)/2 (the straight line) and (*L*/4)2 (the square box). The probability cost for introducing a droplet has the factor *e*−β*L*, but this contributes to the partition function multiplied by the total number of droplets with perimeter *L*, which is less than the total number of paths of length *L*: $N(L)<4^{2L}.$ So that the total spin contribution from droplets, even overcounting by allowing each site to have a separate droplet, is bounded above by $\sum _{L}L^{2}4^{2L}e^{-4\beta L},$

which goes to zero at large β. For β sufficiently large, this exponentially suppresses long loops, so that they cannot occur, and the magnetization never fluctuates too far from −1.

So Peierls established that the magnetization in the Ising model eventually defines superselection sectors, separated domains not linked by finite fluctuations.

### Kramers–Wannier duality

Kramers and Wannier were able to show that the high-temperature expansion and the low-temperature expansion of the model are equal up to an overall rescaling of the free energy. This allowed the phase-transition point in the two-dimensional model to be determined exactly (under the assumption that there is a unique critical point).

### Yang–Lee zeros

After Onsager's solution, Yang and Lee investigated the way in which the partition function becomes singular as the temperature approaches the critical temperature.


## Applications

### Magnetism

The original motivation for the model was the phenomenon of ferromagnetism. Iron is magnetic; once it is magnetized it stays magnetized for a long time compared to any atomic time.

In the 19th century, it was thought that magnetic fields are due to currents in matter, and Ampère postulated that permanent magnets are caused by permanent atomic currents. The motion of classical charged particles could not explain permanent currents though, as shown by Larmor. In order to have ferromagnetism, the atoms must have permanent magnetic moments which are not due to the motion of classical charges.

Once the electron's spin was discovered, it was clear that the magnetism should be due to a large number of electron spins all oriented in the same direction. It was natural to ask how the electrons' spins all know which direction to point in, because the electrons on one side of a magnet don't directly interact with the electrons on the other side. They can only influence their neighbors. The Ising model was designed to investigate whether a large fraction of the electron spins could be oriented in the same direction using only local forces.

### Lattice gas

The Ising model can be reinterpreted as a statistical model for the motion of atoms. Since the kinetic energy depends only on momentum and not on position, while the statistics of the positions only depends on the potential energy, the thermodynamics of the gas only depends on the potential energy for each configuration of atoms.

A coarse model is to make space-time a lattice and imagine that each position either contains an atom or it doesn't. The space of configuration is that of independent bits *Bi*, where each bit is either 0 or 1 depending on whether the position is occupied or not. An attractive interaction reduces the energy of two nearby atoms. If the attraction is only between nearest neighbors, the energy is reduced by −4*JB**i**B**j* for each occupied neighboring pair.

The density of the atoms can be controlled by adding a chemical potential, which is a multiplicative probability cost for adding one more atom. A multiplicative factor in probability can be reinterpreted as an additive term in the logarithm – the energy. The extra energy of a configuration with *N* atoms is changed by *μN*. The probability cost of one more atom is a factor of exp(−*βμ*).

So the energy of the lattice gas is: $E=-{\frac {1}{2}}\sum _{\langle i,j\rangle }4JB_{i}B_{j}+\sum _{i}\mu B_{i}.$

Rewriting the bits in terms of spins, $B_{i}=(S_{i}+1)/2.$ $E=-{\frac {1}{2}}\sum _{\langle i,j\rangle }JS_{i}S_{j}-{\frac {1}{2}}\sum _{i}(4J-\mu )S_{i}.$

For lattices where every site has an equal number of neighbors, this is the Ising model with a magnetic field *h* = (*zJ* − *μ*)/2, where *z* is the number of neighbors.

In biological systems, modified versions of the lattice gas model have been used to understand a range of binding behaviors. These include the binding of ligands to receptors in the cell surface, the binding of chemotaxis proteins to the flagellar motor, and the condensation of DNA.

### Neuroscience

The activity of neurons in the brain can be modelled statistically. Each neuron at any time is either active + or inactive −. The active neurons are those that send an action potential down the axon in any given time window, and the inactive ones are those that do not.

Following the general approach of Jaynes, a later interpretation of Schneidman, Berry, Segev and Bialek, is that the Ising model is useful for any model of neural function, because a statistical model for neural activity should be chosen using the principle of maximum entropy. Given a collection of neurons, a statistical model which can reproduce the average firing rate for each neuron introduces a Lagrange multiplier for each neuron: $E=-\sum _{i}h_{i}S_{i}$ But the activity of each neuron in this model is statistically independent. To allow for pair correlations, when one neuron tends to fire (or not to fire) along with another, introduce pair-wise lagrange multipliers: $E=-{\tfrac {1}{2}}\sum _{ij}J_{ij}S_{i}S_{j}-\sum _{i}h_{i}S_{i}$ where $J_{ij}$ are not restricted to neighbors. Note that this generalization of Ising model is sometimes called the quadratic exponential binary distribution in statistics. This energy function only introduces probability biases for a spin having a value and for a pair of spins having the same value. Higher order correlations are unconstrained by the multipliers. An activity pattern sampled from this distribution requires the largest number of bits to store in a computer, in the most efficient coding scheme imaginable, as compared with any other distribution with the same average activity and pairwise correlations. This means that Ising models are relevant to any system which is described by bits which are as random as possible, with constraints on the pairwise correlations and the average number of 1s, which frequently occurs in both the physical and social sciences.

### Spin glasses

With the Ising model the so-called spin glasses can also be described, by the usual Hamiltonian ${\textstyle H=-{\frac {1}{2}}\,\sum J_{i,k}\,S_{i}\,S_{k},}$ where the *S*-variables describe the Ising spins, while the *Ji,k* are taken from a random distribution. For spin glasses a typical distribution chooses antiferromagnetic bonds with probability *p* and ferromagnetic bonds with probability 1 − *p* (also known as the random-bond Ising model). These bonds stay fixed or "quenched" even in the presence of thermal fluctuations. When *p* = 0 we have the original Ising model. This system deserves interest in its own; particularly one has "non-ergodic" properties leading to strange relaxation behaviour. Much attention has been also attracted by the related bond and site dilute Ising model, especially in two dimensions, leading to intriguing critical behavior.

### Artificial neural network

The Ising model was instrumental in the development of the Hopfield network. The original Ising model is a model for equilibrium. Roy J. Glauber in 1963 studied the Ising model evolving in time, as a process towards thermal equilibrium (Glauber dynamics), adding in the component of time. (Kaoru Nakano, 1971) and (Shun'ichi Amari, 1972), proposed to modify the weights of an Ising model by Hebbian learning rule as a model of associative memory. The same idea was published by (William A. Little, 1974), who was cited by Hopfield in his 1982 paper.

The Sherrington–Kirkpatrick model of spin glass, published in 1975, is the Hopfield network with random initialization. Sherrington and Kirkpatrick found that it is highly likely for the energy function of the SK model to have many local minima. In the 1982 paper, Hopfield applied this recently developed theory to study the Hopfield network with binary activation functions. In a 1984 paper he extended this to continuous activation functions. It became a standard model for the study of neural networks through statistical mechanics.

### Sea ice

The melt pond can be modelled by the Ising model; sea ice topography data bears rather heavily on the results. The state variable is binary for a simple 2D approximation, being either water or ice.

### Cayley tree topologies and large neural networks

In order to investigate an Ising model with potential relevance for large (e.g. with $10^{4}$ or $10^{5}$ interactions per node) neural nets, at the suggestion of Krizan in 1979, Barth (1981) obtained the exact analytical expression for the free energy of the Ising model on the closed Cayley tree (with an arbitrarily large branching ratio) for a zero-external magnetic field (in the thermodynamic limit) by applying the methodologies of Glasser (1970) and Jellito (1979)

$-\beta f=\ln 2+{\frac {2\gamma }{(\gamma +1)}}\ln(\cosh J)+{\frac {\gamma (\gamma -1)}{(\gamma +1)}}\sum _{i=2}^{z}{\frac {1}{\gamma ^{i}}}\ln J_{i}(\tau )$

where $\gamma$ is an arbitrary branching ratio (greater than or equal to 2), $t\equiv \tanh J$ , $\tau \equiv t^{2}$ , $J\equiv \beta \epsilon$ (with $\epsilon$ representing the nearest-neighbor interaction energy) and there are k (→ ∞ in the thermodynamic limit) generations in each of the tree branches (forming the closed tree architecture as shown in the given closed Cayley tree diagram.) The sum in the last term can be shown to converge uniformly and rapidly (i.e. for z → ∞, it remains finite) yielding a continuous and monotonous function, establishing that, for $\gamma$ greater than or equal to 2, the free energy is a continuous function of temperature T. Further analysis of the free energy indicates that it exhibits an unusual discontinuous first derivative at the critical temperature (Krizan, Barth & Glasser (1983), Glasser & Goldberg (1983).)

The spin-spin correlation between sites (in general, m and n) on the tree was found to have a transition point when considered at the vertices (e.g. A and Ā, its reflection), their respective neighboring sites (such as B and its reflection), and between sites adjacent to the top and bottom extreme vertices of the two trees (e.g. A and B), as may be determined from $\langle s_{m}s_{n}\rangle ={Z_{N}}^{-1}(0,T)[\cosh J]^{N_{b}}2^{N}\sum _{l=1}^{z}g_{mn}(l)t^{l}$ where $N_{b}$ is equal to the number of bonds, $g_{mn}(l)t^{l}$ is the number of graphs counted for odd vertices with even intermediate sites (see cited methodologies and references for detailed calculations), $2^{N}$ is the multiplicity resulting from two-valued spin possibilities and the partition function ${Z_{N}}$ is derived from $\sum _{\{s\}}e^{-\beta H}$ . (Note: $s_{i}$ is consistent with the referenced literature in this section and is equivalent to $S_{i}$ or $\sigma _{i}$ utilized above and in earlier sections; it is valued at $\pm 1$ .) The critical temperature $T_{C}$ is given by $T_{C}={\frac {2\epsilon }{k_{\text{B}}[\ln({\sqrt {\gamma }}+1)-\ln({\sqrt {\gamma }}-1)]}}.$

The critical temperature for this model is only determined by the branching ratio $\gamma$ and the site-to-site interaction energy $\epsilon$ , a fact which may have direct implications associated with neural structure vs. its function (in that it relates the energies of interaction and branching ratio to its transitional behavior.) For example, a relationship between the transition behavior of activities of neural networks between sleeping and wakeful states (which may correlate with a spin-spin type of phase transition) in terms of changes in neural interconnectivity ( $\gamma$ ) and/or neighbor-to-neighbor interactions ( $\epsilon$ ), over time, is just one possible avenue suggested for further experimental investigation into such a phenomenon. In any case, for this Ising model it was established, that "the stability of the long-range correlation increases with increasing $\gamma$ or increasing $\epsilon$ ."

For this topology, the spin-spin correlation was found to be zero between the extreme vertices and the central sites at which the two trees (or branches) are joined (i.e. between A and individually C, D, or E.) This behavior is explained to be due to the fact that, as k increases, the number of links increases exponentially (between the extreme vertices) and so even though the contribution to spin correlations decrease exponentially, the correlation between sites such as the extreme vertex (A) in one tree and the extreme vertex in the joined tree (Ā) remains finite (above the critical temperature.) In addition, A and B also exhibit a non-vanishing correlation (as do their reflections) thus lending itself to, for B level sites (with A level), being considered "clusters" which tend to exhibit synchronization of firing.

Based upon a review of other classical network models as a comparison, the Ising model on a closed Cayley tree was determined to be the first classical statistical mechanical model to demonstrate both local and long-range sites with non-vanishing spin-spin correlations, while at the same time exhibiting intermediate sites with zero correlation, which indeed was a relevant matter for large neural networks at the time of its consideration. The model's behavior is also of relevance for any other divergent-convergent tree physical (or biological) system exhibiting a closed Cayley tree topology with an Ising-type of interaction. This topology should not be ignored since its behavior for Ising models has been solved exactly, and presumably nature will have found a way of taking advantage of such simple symmetries at many levels of its designs.

Barth (1981) early on noted the possibility of interrelationships between (1) the classical large neural network model (with similar coupled divergent-convergent topologies) with (2) an underlying statistical quantum mechanical model (independent of topology and with persistence in fundamental quantum states):

> The most significant result obtained from the closed Cayley tree model involves the occurrence of long-range correlation in the absence of intermediate-range correlation. This result has not been demonstrated by other classical models. The failure of the classical view of impulse transmission to account for this phenomenon has been cited by numerous investigators (Ricciiardi and Umezawa, 1967, Hokkyo 1972, Stuart, Takahashi and Umezawa 1978, 1979) as significant enough to warrant radically new assumptions on a very fundamental level and have suggested the existence of quantum cooperative modes within the brain…In addition, it is interesting to note that the (modeling) of…Goldstone particles or bosons (as per Umezawa, et al)…within the brain, demonstrates the long-range correlation of quantum numbers preserved in the ground state…In the closed Cayley tree model ground states of pairs of sites, as well as the state variable of individual sites, (can) exhibit long-range correlation.

It was a natural and common belief among early neurophysicists (e.g. Umezawa, Krizan, Barth, etc.) that classical neural models (including those with statistical mechanical aspects) will one day have to be integrated with quantum physics (with quantum statistical aspects), similar perhaps to how the domain of chemistry has historically integrated itself into quantum physics via quantum chemistry.

Several additional statistical mechanical problems of interest remain to be solved for the closed Cayley tree, including the time-dependent case and the external field situation, as well as theoretical efforts aimed at understanding interrelationships with underlying quantum constituents and their physics.


## Numerical simulation

The Ising model can often be difficult to evaluate numerically if there are many states in the system. Consider an Ising model with

L

= |Λ|: the total number of sites on the lattice,

σ

j

∈ {−1, +1}: an individual spin site on the lattice,

j

= 1, ...,

L

,

S

∈ {−1, +1}

L

: state of the system.

Since every spin site has ±1 spin, there are *2**L* different states that are possible. This motivates the reason for the Ising model to be simulated using Monte Carlo methods.

The Hamiltonian that is commonly used to represent the energy of the model when using Monte Carlo methods is:

$H(\sigma )=-J\sum _{\langle i~j\rangle }\sigma _{i}\sigma _{j}-h\sum _{j}\sigma _{j}.$

Furthermore, the Hamiltonian is further simplified by assuming zero external field *h*, since many questions that are posed to be solved using the model can be answered in absence of an external field. This leads us to the following energy equation for state σ:

$H(\sigma )=-J\sum _{\langle i~j\rangle }\sigma _{i}\sigma _{j}.$

Given this Hamiltonian, quantities of interest such as the specific heat or the magnetization of the magnet at a given temperature can be calculated.

### Metropolis algorithm

The Metropolis–Hastings algorithm is the most commonly used Monte Carlo algorithm to calculate Ising model estimations. The algorithm first chooses *selection probabilities* *g*(μ, ν), which represent the probability that state ν is selected by the algorithm out of all states, given that one is in state μ. It then uses acceptance probabilities *A*(μ, ν) so that detailed balance is satisfied. If the new state ν is accepted, then we move to that state and repeat with selecting a new state and deciding to accept it. If ν is not accepted then we stay in μ. This process is repeated until some stopping criterion is met, which for the Ising model is often when the lattice becomes ferromagnetic, meaning all of the sites point in the same direction.

When implementing the algorithm, one must ensure that *g*(μ, ν) is selected such that ergodicity is met. In thermal equilibrium a system's energy only fluctuates within a small range. This is the motivation behind the concept of **single-spin-flip dynamics**, which states that in each transition, we will only change one of the spin sites on the lattice. Furthermore, by using single- spin-flip dynamics, one can get from any state to any other state by flipping each site that differs between the two states one at a time. The maximum amount of change between the energy of the present state, *H*μ and any possible new state's energy *H*ν (using single-spin-flip dynamics) is 2*J* between the spin we choose to "flip" to move to the new state and that spin's neighbor. Thus, in a 1D Ising model, where each site has two neighbors (left and right), the maximum difference in energy would be 4*J*. Let *c* represent the *lattice coordination number*; the number of nearest neighbors that any lattice site has. We assume that all sites have the same number of neighbors due to periodic boundary conditions. It is important to note that the Metropolis–Hastings algorithm does not perform well around the critical point due to critical slowing down. Other techniques such as multigrid methods, Niedermayer's algorithm, Swendsen–Wang algorithm, or the Wolff algorithm are required in order to resolve the model near the critical point; a requirement for determining the critical exponents of the system.

Specifically for the Ising model and using single-spin-flip dynamics, one can establish the following. Since there are *L* total sites on the lattice, using single-spin-flip as the only way we transition to another state, we can see that there are a total of *L* new states ν from our present state μ. The algorithm assumes that the selection probabilities are equal to the *L* states: *g*(μ, ν) = 1/*L*. Detailed balance tells us that the following equation must hold:

${\frac {P(\mu ,\nu )}{P(\nu ,\mu )}}={\frac {g(\mu ,\nu )A(\mu ,\nu )}{g(\nu ,\mu )A(\nu ,\mu )}}={\frac {A(\mu ,\nu )}{A(\nu ,\mu )}}={\frac {P_{\beta }(\nu )}{P_{\beta }(\mu )}}={\frac {{\frac {1}{Z}}e^{-\beta (H_{\nu })}}{{\frac {1}{Z}}e^{-\beta (H_{\mu })}}}=e^{-\beta (H_{\nu }-H_{\mu })}.$

Thus, we want to select the acceptance probability for our algorithm to satisfy

${\frac {A(\mu ,\nu )}{A(\nu ,\mu )}}=e^{-\beta (H_{\nu }-H_{\mu })}.$

If *H*ν > *H*μ, then *A*(ν, μ) > *A*(μ, ν). Metropolis sets the larger of *A*(μ, ν) or *A*(ν, μ) to be 1. By this reasoning the acceptance algorithm is:

$A(\mu ,\nu )={\begin{cases}e^{-\beta (H_{\nu }-H_{\mu })},&{\text{if }}H_{\nu }-H_{\mu }>0,\\1&{\text{otherwise}}.\end{cases}}$

The basic form of the algorithm is as follows:

1. Pick a spin site using selection probability *g*(μ, ν) and calculate the contribution to the energy involving this spin.
2. Flip the value of the spin and calculate the new contribution.
3. If the new energy is less, keep the flipped value.
4. If the new energy is more, only keep with probability $e^{-\beta (H_{\nu }-H_{\mu })}.$
5. Repeat.

The change in energy *H*ν − *H*μ only depends on the value of the spin and its nearest graph neighbors. So if the graph is not too connected, the algorithm is fast. This process will eventually produce a pick from the distribution.

### As a Markov chain

It is possible to view the Ising model as a Markov chain, as the immediate probability *P*β(ν) of transitioning to a future state ν only depends on the present state μ. The Metropolis algorithm is actually a version of a Markov chain Monte Carlo simulation, and since we use single-spin-flip dynamics in the Metropolis algorithm, every state can be viewed as having links to exactly *L* other states, where each transition corresponds to flipping a single spin site to the opposite value. Furthermore, since the energy equation *H*σ change only depends on the nearest-neighbor interaction strength *J*, the Ising model and its variants such the Sznajd model can be seen as a form of a voter model for opinion dynamics.
