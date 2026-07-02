---
title: "Detailed balance"
source: https://en.wikipedia.org/wiki/Detailed_balance
domain: markov-chain-monte-carlo-deep
license: CC-BY-SA-4.0
tags: Markov chain Monte Carlo, detailed balance, ergodicity, burn-in
fetched: 2026-07-02
---

# Detailed balance

In thermodynamics, the principle of **detailed balance** says that every process of energy transfer in one direction must also allow energy transfer in the opposite direction, and in equilibrium, the flux in both directions must be equal. For example, the principle can be used in kinetic systems which are decomposed into elementary processes (collisions, or steps, or elementary reactions). It states that at equilibrium, each elementary process is in equilibrium with its reverse process.

## History

The principle of detailed balance was explicitly introduced for collisions by Ludwig Boltzmann. In 1872, he proved his H-theorem using this principle. The arguments in favor of this property are founded upon microscopic reversibility.

Five years before Boltzmann, James Clerk Maxwell used the principle of detailed balance for gas kinetics with the reference to the principle of sufficient reason. He compared the idea of detailed balance with other types of balancing (like cyclic balance) and found that "Now it is impossible to assign a reason" why detailed balance should be rejected (p. 64).

In 1901, Rudolf Wegscheider introduced the principle of detailed balance for chemical kinetics. In particular, he demonstrated that the irreversible cycles ${\ce {A1->A2->\cdots ->A_{\mathit {n}}->A1}}$ are impossible and found explicitly the relations between kinetic constants that follow from the principle of detailed balance. In 1931, Lars Onsager used these relations in his works, for which he was awarded the 1968 Nobel Prize in Chemistry.

The principle of detailed balance has been used in Markov chain Monte Carlo methods since their invention in 1953. In particular, in the Metropolis–Hastings algorithm and in its important particular case, Gibbs sampling, it is used as a simple and reliable condition to provide the desirable equilibrium state.

Now, the principle of detailed balance is a standard part of the university courses in statistical mechanics, physical chemistry, chemical and physical kinetics.

## Microscopic background

The microscopic "reversing of time" turns at the kinetic level into the "reversing of arrows": the elementary processes transform into their reverse processes. For example, the reaction

$\sum _{i}\alpha _{i}{\ce {A}}_{i}{\ce {->}}\sum _{j}\beta _{j}{\ce {B}}_{j}$

transforms into

$\sum _{j}\beta _{j}{\ce {B}}_{j}{\ce {->}}\sum _{i}\alpha _{i}{\ce {A}}_{i}$

and conversely. (Here, ${\ce {A}}_{i},{\ce {B}}_{j}$ are symbols of components or states, $\alpha _{i},\beta _{j}\geq 0$ are coefficients). The equilibrium ensemble should be invariant with respect to this transformation because of microreversibility and the uniqueness of thermodynamic equilibrium. This leads us immediately to the concept of detailed balance: each process is equilibrated by its reverse process.

This reasoning is based on three assumptions:

1. ${\ce {A}}_{i}$ does not change under time reversal;
2. Equilibrium is invariant under time reversal;
3. The macroscopic elementary processes are microscopically distinguishable. That is, they represent disjoint sets of microscopic events.

Any of these assumptions may be violated. For example, Boltzmann's collision can be represented as ${\ce {A_{\mathit {v}}+A_{\mathit {w}}->A_{\mathit {v'}}+A_{\mathit {w'}}}}$ , where ${\ce {A}}_{v}$ is a particle with velocity *v*. Under time reversal ${\ce {A}}_{v}$ transforms into ${\ce {A}}_{-v}$ . Therefore, the collision is transformed into the reverse collision by the *PT* transformation, where *P* is the space inversion and *T* is the time reversal. Detailed balance for Boltzmann's equation requires *PT*-invariance of collisions' dynamics, not just *T*-invariance. Indeed, after the time reversal the collision ${\ce {A_{\mathit {v}}+A_{\mathit {w}}->A_{\mathit {v'}}+A_{\mathit {w'}}}}$ , transforms into ${\ce {A_{\mathit {-v'}}+A_{\mathit {-w'}}->A_{\mathit {-v}}+A_{\mathit {-w}}}}$ . For the detailed balance we need transformation into ${\ce {A_{\mathit {v'}}+A_{\mathit {w'}}->A_{\mathit {v}}+A_{\mathit {w}}}}$ . For this purpose, we need to apply additionally the space reversal *P*. Therefore, for the detailed balance in Boltzmann's equation not *T*-invariance but *PT*-invariance is needed.

Equilibrium may be not *T*- or *PT*-invariant even if the laws of motion are invariant. This non-invariance may be caused by the spontaneous symmetry breaking. There exist *nonreciprocal media* (for example, some bi-isotropic materials) without *T* and *PT* invariance.

If different macroscopic processes are sampled from the same elementary microscopic events then macroscopic detailed balance may be violated even when microscopic detailed balance holds.

Now, after almost 150 years of development, the scope of validity and the violations of detailed balance in kinetics seem to be clear.

## Detailed balance

### Reversibility

A Markov process is called a *reversible Markov process* or *reversible Markov chain* if there exists a positive stationary distribution π that satisfies the **detailed balance equations** $\pi _{i}P_{ij}=\pi _{j}P_{ji}\,,$ where *P**ij* is the Markov transition probability from state *i* to state *j*, i.e. *P**ij* = *P*(*X**t* = *j* | *X**t* − 1 = *i*), and π*i* and π*j* are the equilibrium probabilities of being in states *i* and *j*, respectively. When Pr(*X**t*−1 = *i*) = π*i* for all *i*, this is equivalent to the joint probability matrix, Pr(*X**t*−1 = *i*, *X**t* = *j*) being symmetric in *i* and *j*; or symmetric in *t* − 1 and *t*.

The definition carries over straightforwardly to continuous variables, where π becomes a probability density, and *P*(*s*′, *s*) a transition kernel probability density from state *s*′ to state *s*: $\pi (s')P(s',s)=\pi (s)P(s,s')\,.$ The detailed balance condition is stronger than that required merely for a stationary distribution, because there are Markov processes with stationary distributions that do not have detailed balance.

Transition matrices that are symmetric (*P**ij* = *P**ji* or *P*(*s*′, *s*) = *P*(*s*, *s*′)) always have detailed balance. In these cases, a uniform distribution over the states is an equilibrium distribution.

### Kolmogorov's criterion

Reversibility is equivalent to Kolmogorov's criterion: the product of transition rates over any closed loop of states is the same in both directions.

For example, it implies that, for all *a*, *b* and *c*, $P(a,b)P(b,c)P(c,a)=P(a,c)P(c,b)P(b,a)\,.$ For example, if we have a Markov chain with three states such that only these transitions are possible: $A\to B,B\to C,C\to A,B\to A$ , then they violate Kolmogorov's criterion.

### Closest reversible Markov chain

For continuous systems with detailed balance, it may be possible to continuously transform the coordinates until the equilibrium distribution is uniform, with a transition kernel which then is symmetric. In the case of discrete states, it may be possible to achieve something similar by breaking the Markov states into appropriately-sized degenerate sub-states.

For a Markov transition matrix and a stationary distribution, the detailed balance equations may not be valid. However, it can be shown that a unique Markov transition matrix exists which is closest according to the stationary distribution and a given norm. The closest Matrix can be computed by solving a quadratic-convex optimization problem.

## Detailed balance and entropy increase

For many systems of physical and chemical kinetics, detailed balance provides *sufficient conditions* for the strict increase of entropy in isolated systems. For example, the famous Boltzmann H-theorem states that, according to the Boltzmann equation, the principle of detailed balance implies positivity of entropy production. The Boltzmann formula (1872) for entropy production in rarefied gas kinetics with detailed balance served as a prototype of many similar formulas for dissipation in mass action kinetics and generalized mass action kinetics with detailed balance.

Nevertheless, the principle of detailed balance is not necessary for entropy growth. For example, in the linear irreversible cycle ${\ce {A1 -> A2 -> A3 -> A1}}$ , entropy production is positive but the principle of detailed balance does not hold.

Thus, the principle of detailed balance is a sufficient but not necessary condition for entropy increase in Boltzmann kinetics. These relations between the principle of detailed balance and the second law of thermodynamics were clarified in 1887 when Hendrik Lorentz objected to the Boltzmann H-theorem for polyatomic gases. Lorentz stated that the principle of detailed balance is not applicable to collisions of polyatomic molecules.

Boltzmann immediately invented a new, more general condition sufficient for entropy growth. Boltzmann's condition holds for all Markov processes, irrespective of time-reversibility. Later, entropy increase was proved for all Markov processes by a direct method. These theorems may be considered as simplifications of the Boltzmann result. Later, this condition was referred to as the "cyclic balance" condition (because it holds for irreversible cycles) or the "semi-detailed balance" or the "complex balance". In 1981, Carlo Cercignani and Maria Lampis proved that the Lorentz arguments were wrong and the principle of detailed balance is valid for polyatomic molecules. Nevertheless, the extended semi-detailed balance conditions invented by Boltzmann in this discussion remain the remarkable generalization of the detailed balance.

## Wegscheider's conditions for the generalized mass action law

In chemical kinetics, the elementary reactions are represented by the stoichiometric equations $\sum _{i}\alpha _{ri}{\ce {A}}_{i}{\ce {->}}\sum _{j}\beta _{rj}{\ce {A}}_{j}\;\;(r=1,\ldots ,m)\,,$ where ${\ce {A}}_{i}$ are the components and $\alpha _{ri},\beta _{rj}\geq 0$ are the stoichiometric coefficients. Here, the reverse reactions with positive constants are included in the list separately. We need this separation of direct and reverse reactions to apply later the general formalism to the systems with some irreversible reactions. The system of stoichiometric equations of elementary reactions is the *reaction mechanism*.

The *stoichiometric matrix* is ${\boldsymbol {\Gamma }}=(\gamma _{ri})$ , $\gamma _{ri}=\beta _{ri}-\alpha _{ri}$ (gain minus loss). This matrix need not be square. The *stoichiometric vector* $\gamma _{r}$ is the *r*th row of ${\boldsymbol {\Gamma }}$ with coordinates $\gamma _{ri}=\beta _{ri}-\alpha _{ri}$ .

According to the *generalized mass action law*, the reaction rate for an elementary reaction is $w_{r}=k_{r}\prod _{i=1}^{n}a_{i}^{\alpha _{ri}}\,,$ where $a_{i}\geq 0$ is the activity (the "effective concentration") of $A_{i}$ .

The reaction mechanism includes reactions with the reaction rate constants $k_{r}>0$ . For each *r* the following notations are used: $k_{r}^{+}=k_{r}$ ; $w_{r}^{+}=w_{r}$ ; $k_{r}^{-}$ is the reaction rate constant for the reverse reaction if it is in the reaction mechanism and 0 if it is not; $w_{r}^{-}$ is the reaction rate for the reverse reaction if it is in the reaction mechanism and 0 if it is not. For a reversible reaction, $K_{r}=k_{r}^{+}/k_{r}^{-}$ is the equilibrium constant.

The principle of detailed balance for the generalized mass action law is: For given values $k_{r}$ there exists a positive equilibrium $a_{i}^{\rm {eq}}>0$ that satisfies detailed balance, that is, $w_{r}^{+}=w_{r}^{-}$ . This means that the system of *linear* detailed balance equations $\sum _{i}\gamma _{ri}x_{i}=\ln k_{r}^{+}-\ln k_{r}^{-}=\ln K_{r}$ is solvable ( $x_{i}=\ln a_{i}^{\rm {eq}}$ ). The following classical result gives the necessary and sufficient conditions for the existence of a positive equilibrium $a_{i}^{\rm {eq}}>0$ with detailed balance (see, for example, the textbook).

Two conditions are sufficient and necessary for solvability of the system of detailed balance equations:

1. If $k_{r}^{+}>0$ then $k_{r}^{-}>0$ and, conversely, if $k_{r}^{-}>0$ then $k_{r}^{+}>0$ (reversibility);
2. For any solution ${\boldsymbol {\lambda }}=(\lambda _{r})$ of the system ${\boldsymbol {\lambda \Gamma }}=0\;\;\left({\mbox{i.e.}}\;\;\sum _{r}\lambda _{r}\gamma _{ri}=0\;\;{\mbox{for all}}\;\;i\right)$

the Wegscheider's identity holds: $\prod _{r=1}^{m}(k_{r}^{+})^{\lambda _{r}}=\prod _{r=1}^{m}(k_{r}^{-})^{\lambda _{r}}\,.$

*Remark.* It is sufficient to use in the Wegscheider conditions a basis of solutions of the system ${\boldsymbol {\lambda \Gamma }}=0$ .

In particular, for any cycle in the monomolecular (linear) reactions the product of the reaction rate constants in the clockwise direction is equal to the product of the reaction rate constants in the counterclockwise direction. The same condition is valid for the reversible Markov processes (it is equivalent to the "no net flow" condition).

A simple nonlinear example gives us a linear cycle supplemented by one nonlinear step:

1. ${\ce {A1 <=> A2}}$
2. ${\ce {A2 <=> A3}}$
3. ${\ce {A3 <=> A1}}$
4. ${\ce {{A1}+A2 <=> 2A3}}$

There are two nontrivial independent Wegscheider's identities for this system: $k_{1}^{+}k_{2}^{+}k_{3}^{+}=k_{1}^{-}k_{2}^{-}k_{3}^{-}$ and $k_{3}^{+}k_{4}^{+}/k_{2}^{+}=k_{3}^{-}k_{4}^{-}/k_{2}^{-}$ They correspond to the following linear relations between the stoichiometric vectors: $\gamma _{1}+\gamma _{2}+\gamma _{3}=0$ and $\gamma _{3}+\gamma _{4}-\gamma _{2}=0.$

The computational aspect of the Wegscheider conditions was studied by D. Colquhoun with co-authors.

The Wegscheider conditions demonstrate that whereas the principle of detailed balance states a local property of equilibrium, it implies the relations between the kinetic constants that are valid for all states far from equilibrium. This is possible because a kinetic law is known and relations between the rates of the elementary processes at equilibrium can be transformed into relations between kinetic constants which are used globally. For the Wegscheider conditions this kinetic law is the law of mass action (or the generalized law of mass action).

## Dissipation in systems with detailed balance

To describe dynamics of the systems that obey the generalized mass action law, one has to represent the activities as functions of the concentrations *cj* and temperature. For this purpose, use the representation of the activity through the chemical potential: $a_{i}=\exp \left({\frac {\mu _{i}-\mu _{i}^{\ominus }}{RT}}\right)$ where *μi* is the chemical potential of the species under the conditions of interest, ⁠ $\mu _{i}^{\ominus }$ ⁠ is the chemical potential of that species in the chosen standard state, *R* is the gas constant and *T* is the thermodynamic temperature. The chemical potential can be represented as a function of *c* and *T*, where *c* is the vector of concentrations with components *cj*. For the ideal systems, $\mu _{i}=RT\ln c_{i}+\mu _{i}^{\ominus }$ and $a_{j}=c_{j}$ : the activity is the concentration and the generalized mass action law is the usual law of mass action.

Consider a system in isothermal (*T*=const) isochoric (the volume *V*=const) condition. For these conditions, the Helmholtz free energy ⁠ $F(T,V,N)$ ⁠ measures the "useful" work obtainable from a system. It is a functions of the temperature *T*, the volume *V* and the amounts of chemical components *Nj* (usually measured in moles), *N* is the vector with components *Nj*. For the ideal systems, $F=RT\sum _{i}N_{i}\left(\ln \left({\frac {N_{i}}{V}}\right)-1+{\frac {\mu _{i}^{\ominus }(T)}{RT}}\right).$

The chemical potential is a partial derivative: $\mu _{i}=\partial F(T,V,N)/\partial N_{i}$ .

The chemical kinetic equations are ${\frac {dN_{i}}{dt}}=V\sum _{r}\gamma _{ri}(w_{r}^{+}-w_{r}^{-}).$

If the principle of detailed balance is valid then for any value of *T* there exists a positive point of detailed balance *c*eq: $w_{r}^{+}(c^{\rm {eq}},T)=w_{r}^{-}(c^{\rm {eq}},T)=w_{r}^{\rm {eq}}$ Elementary algebra gives $w_{r}^{+}=w_{r}^{\rm {eq}}\exp \left(\sum _{i}{\frac {\alpha _{ri}(\mu _{i}-\mu _{i}^{\rm {eq}})}{RT}}\right);\;\;w_{r}^{-}=w_{r}^{\rm {eq}}\exp \left(\sum _{i}{\frac {\beta _{ri}(\mu _{i}-\mu _{i}^{\rm {eq}})}{RT}}\right);$ where $\mu _{i}^{\rm {eq}}=\mu _{i}(c^{\rm {eq}},T)$

For the dissipation we obtain from these formulas: ${\frac {dF}{dt}}=\sum _{i}{\frac {\partial F(T,V,N)}{\partial N_{i}}}{\frac {dN_{i}}{dt}}=\sum _{i}\mu _{i}{\frac {dN_{i}}{dt}}=-VRT\sum _{r}(\ln w_{r}^{+}-\ln w_{r}^{-})(w_{r}^{+}-w_{r}^{-})\leq 0$ The inequality holds because ln is a monotone function and, hence, the expressions $\ln w_{r}^{+}-\ln w_{r}^{-}$ and $w_{r}^{+}-w_{r}^{-}$ have always the same sign.

Similar inequalities are valid for other classical conditions for the closed systems and the corresponding characteristic functions: for isothermal isobaric conditions the Gibbs free energy decreases, for the isochoric systems with the constant internal energy (isolated systems) the entropy increases as well as for isobaric systems with the constant enthalpy.

## Onsager reciprocal relations and detailed balance

Let the principle of detailed balance be valid. Then, for small deviations from equilibrium, the kinetic response of the system can be approximated as linearly related to its deviation from chemical equilibrium, giving the reaction rates for the generalized mass action law as: $w_{r}^{+}=w_{r}^{\rm {eq}}\left(1+\sum _{i}{\frac {\alpha _{ri}(\mu _{i}-\mu _{i}^{\rm {eq}})}{RT}}\right);\;\;w_{r}^{-}=w_{r}^{\rm {eq}}\left(1+\sum _{i}{\frac {\beta _{ri}(\mu _{i}-\mu _{i}^{\rm {eq}})}{RT}}\right);$

Therefore, again in the linear response regime near equilibrium, the kinetic equations are ( $\gamma _{ri}=\beta _{ri}-\alpha _{ri}$ ): ${\frac {dN_{i}}{dt}}=-V\sum _{j}\left[\sum _{r}w_{r}^{\rm {eq}}\gamma _{ri}\gamma _{rj}\right]{\frac {\mu _{j}-\mu _{j}^{\rm {eq}}}{RT}}.$

This is exactly the Onsager form: following the original work of Onsager, we should introduce the thermodynamic forces $X_{j}$ and the matrix of coefficients $L_{ij}$ in the form $X_{j}={\frac {\mu _{j}-\mu _{j}^{\rm {eq}}}{T}};\;\;{\frac {dN_{i}}{dt}}=\sum _{j}L_{ij}X_{j}$

The coefficient matrix $L_{ij}$ is symmetric: $L_{ij}=-{\frac {V}{R}}\sum _{r}w_{r}^{\rm {eq}}\gamma _{ri}\gamma _{rj}$

These symmetry relations, $L_{ij}=L_{ji}$ , are exactly the Onsager reciprocal relations. The coefficient matrix L is non-positive. It is negative on the linear span of the stoichiometric vectors $\gamma _{r}$ .

So, the Onsager relations follow from the principle of detailed balance in the linear approximation near equilibrium.

## Local detailed balance

**Local detailed balance** is an extension of detailed balance for modeling open systems that are coupled to various mutually separate mechanical, chemical or thermal baths. It gives a physically motivated way and interpretation for constructing stochastic dynamical models for nonequilibrium processes. That question was already explicitly discussed by Bergmann and Lebowitz (1955) where they proposed it for a description of irreversible processes. It gets discussed in The point is to get sensible ways for effectively taking into account the presence of reservoirs, where the change in the reservoir is a function of the system trajectories. It naturally leads to stochastic energetics and the developments in stochastic thermodynamics. In that sense, the condition of local detailed balance stands crucially at the beginning of nonequilibrium statistical mechanics (directly) for stationary open systems, driven by the coupling with different spacetime-well-separated equilibrium baths.

Central to local detailed balance is the idea that each transition of the system state is accompanied by an exchange of energy or particles with a specific equilibrium reservoir, and that the corresponding updating follows the condition of detailed balance using the intensive variables of that reservoir. There need not be a (global) detailed balance as reservoirs can have different temperatures, chemical potentials, etc. In mathematical terms, the condition of local detailed balance assures that the logarithmic ratio of the probability of a trajectory to the probability of the time-reversed trajectory equals the entropy flux per *k*B to the system environment. It is important here that the environment consists of mutually separated thermodynamic equilibrium baths.

In particular, local detailed balance allows identification of currents and entropy flows, and is directly related to the so-called fluctuation theorems for entropy fluxes. As shown in a series of publications, local detailed balance implies detailed, integrated, local, steady-state or transient fluctuation theorems for the entropy flux satisfying a Gallavotti–Cohen-like symmetry. Discussions and derivations of local detailed balance are found in. Not all models that are commonly used in nonequilibrium statistical mechanics satisfy local detailed balance, which makes it less evident how to associate heat and entropy fluxes to the proposed dynamics.

## Semi-detailed balance

To formulate the principle of semi-detailed balance, it is convenient to count the direct and inverse elementary reactions separately. In this case, the kinetic equations have the form: ${\frac {dN_{i}}{dt}}=V\sum _{r}\gamma _{ri}w_{r}=V\sum _{r}(\beta _{ri}-\alpha _{ri})w_{r}$ Let us use the notations $\alpha _{r}=\alpha _{ri}$ , $\beta _{r}=\beta _{ri}$ for the input and the output vectors of the stoichiometric coefficients of the *r*th elementary reaction. Let Y be the set of all these vectors $\alpha _{r},\beta _{r}$ .

For each $\nu \in Y$ , let us define two sets of numbers: $R_{\nu }^{+}=\{r|\alpha _{r}=\nu \};\;\;\;R_{\nu }^{-}=\{r|\beta _{r}=\nu \}$

$r\in R_{\nu }^{+}$ if and only if $\nu$ is the vector of the input stoichiometric coefficients $\alpha _{r}$ for the *r*th elementary reaction; $r\in R_{\nu }^{-}$ if and only if $\nu$ is the vector of the output stoichiometric coefficients $\beta _{r}$ for the *r*th elementary reaction.

The principle of **semi-detailed balance** means that in equilibrium the semi-detailed balance condition holds: for every $\nu \in Y$ $\sum _{r\in R_{\nu }^{-}}w_{r}=\sum _{r\in R_{\nu }^{+}}w_{r}$

The semi-detailed balance condition is sufficient for the stationarity: it implies that ${\frac {dN}{dt}}=V\sum _{r}\gamma _{r}w_{r}=0.$

For the Markov kinetics the semi-detailed balance condition is just the elementary balance equation and holds for any steady state. For the nonlinear mass action law it is, in general, sufficient but not necessary condition for stationarity.

The semi-detailed balance condition is weaker than the detailed balance one: if the principle of detailed balance holds then the condition of semi-detailed balance also holds.

For systems that obey the generalized mass action law the semi-detailed balance condition is sufficient for the dissipation inequality $dF/dt\geq 0$ (for the Helmholtz free energy under isothermal isochoric conditions and for the dissipation inequalities under other classical conditions for the corresponding thermodynamic potentials).

Boltzmann introduced the semi-detailed balance condition for collisions in 1887 and proved that it guaranties the positivity of the entropy production. For chemical kinetics, this condition (as the *complex balance* condition) was introduced by Horn and Jackson in 1972.

The microscopic backgrounds for the semi-detailed balance were found in the Markov microkinetics of the intermediate compounds that are present in small amounts and whose concentrations are in quasiequilibrium with the main components. Under these microscopic assumptions, the semi-detailed balance condition is just the balance equation for the Markov microkinetics according to the **Michaelis–Menten–Stueckelberg theorem**.

## Dissipation in systems with semi-detailed balance

Let us represent the generalized mass action law in the equivalent form: the rate of the elementary process $\sum _{i}\alpha _{ri}{\ce {A}}_{i}{\ce {->}}\sum _{i}\beta _{ri}{\ce {A}}_{i}$ is $w_{r}=\varphi _{r}\exp \left(\sum _{i}{\frac {\alpha _{ri}\mu _{i}}{RT}}\right)$ where $\mu _{i}=\partial F(T,V,N)/\partial N_{i}$ is the chemical potential and $F(T,V,N)$ is the Helmholtz free energy. The exponential term is called the *Boltzmann factor* and the multiplier $\varphi _{r}\geq 0$ is the kinetic factor. Let us count the direct and reverse reaction in the kinetic equation separately: ${\frac {dN_{i}}{dt}}=V\sum _{r}\gamma _{ri}w_{r}$ An auxiliary function $\theta (\lambda )$ of one variable $\lambda \in [0,1]$ is convenient for the representation of dissipation for the mass action law $\theta (\lambda )=\sum _{r}\varphi _{r}\exp \left(\sum _{i}{\frac {(\lambda \alpha _{ri}+(1-\lambda )\beta _{ri})\mu _{i}}{RT}}\right)$ This function $\theta (\lambda )$ may be considered as the sum of the reaction rates for *deformed* input stoichiometric coefficients ${\tilde {\alpha }}_{\rho }(\lambda )=\lambda \alpha _{\rho }+(1-\lambda )\beta _{\rho }$ . For $\lambda =1$ it is just the sum of the reaction rates. The function $\theta (\lambda )$ is convex because $\theta ''(\lambda )\geq 0$ .

Direct calculation gives that according to the kinetic equations ${\frac {dF}{dt}}=-VRT\left.{\frac {d\theta (\lambda )}{d\lambda }}\right|_{\lambda =1}$ This is *the general dissipation formula for the generalized mass action law*.

Convexity of $\theta (\lambda )$ gives the sufficient and necessary conditions for the proper dissipation inequality: ${\frac {dF}{dt}}<0{\text{ if and only if }}\theta (\lambda )<\theta (1){\text{ for some }}\lambda <1;$ ${\frac {dF}{dt}}\leq 0{\text{ if and only if }}\theta (\lambda )\leq \theta (1){\text{ for some }}\lambda <1.$

The semi-detailed balance condition can be transformed into identity $\theta (0)\equiv \theta (1)$ . Therefore, for the systems with semi-detailed balance ${dF}/{dt}\leq 0$ .

## Cone theorem and local equivalence of detailed and complex balance

For any reaction mechanism and a given positive equilibrium a *cone of possible velocities* for the systems with detailed balance is defined for any non-equilibrium state *N* $\mathbf {Q} _{\rm {DB}}(N)={\rm {cone}}\{\gamma _{r}{\rm {sgn}}(w_{r}^{+}(N)-w_{r}^{-}(N))\ |\ r=1,\ldots ,m\},$ where cone stands for the conical hull and the piecewise-constant functions ${\rm {sgn}}(w_{r}^{+}(N)-w_{r}^{-}(N))$ do not depend on (positive) values of equilibrium reaction rates $w_{r}^{\rm {eq}}$ and are defined by thermodynamic quantities under assumption of detailed balance.

The **cone theorem** states that for the given reaction mechanism and given positive equilibrium, the velocity (*dN/dt*) at a state *N* for a system with complex balance belongs to the cone $\mathbf {Q} _{\rm {DB}}(N)$ . That is, there exists a system with detailed balance, the same reaction mechanism, the same positive equilibrium, that gives the same velocity at state *N*. According to cone theorem, for a given state *N*, the set of velocities of the semidetailed balance systems coincides with the set of velocities of the detailed balance systems if their reaction mechanisms and equilibria coincide. This means *local equivalence of detailed and complex balance.*

## Detailed balance for systems with irreversible reactions

Detailed balance states that in equilibrium each elementary process is equilibrated by its reverse process and requires reversibility of all elementary processes. For many real physico-chemical complex systems (e.g. homogeneous combustion, heterogeneous catalytic oxidation, most enzyme reactions etc.), detailed mechanisms include both reversible and irreversible reactions. If one represents irreversible reactions as limits of reversible steps, then it becomes obvious that not all reaction mechanisms with irreversible reactions can be obtained as limits of systems or reversible reactions with detailed balance. For example, the irreversible cycle ${\ce {A1 -> A2 -> A3 -> A1}}$ cannot be obtained as such a limit but the reaction mechanism ${\ce {A1 -> A2 -> A3 <- A1}}$ can.

**Gorban–Yablonsky theorem**. *A system of reactions with some irreversible reactions is a limit of systems with detailed balance when some constants tend to zero if and only if (i) the reversible part of this system satisfies the principle of detailed balance and (ii) the convex hull of the stoichiometric vectors of the irreversible reactions has empty intersection with the linear span of the stoichiometric vectors of the reversible reactions.* Physically, the last condition means that the irreversible reactions cannot be included in oriented cyclic pathways.
