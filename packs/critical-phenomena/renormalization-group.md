---
title: "Renormalization group"
source: https://en.wikipedia.org/wiki/Renormalization_group
domain: critical-phenomena
license: CC-BY-SA-4.0
tags: critical phenomena, critical exponent, renormalization group, ising model
fetched: 2026-07-02
---

# Renormalization group

In theoretical physics, the **renormalization group** (**RG**) is a mathematical tool that allows systematic investigation into the changes in a physical system as it is viewed at different scales. The scales of the system typically describe the interactions of the objects; they may be variable ("running") couplings which measure the strength of various forces, mass parameters, or the size of the system. The renormalization group is related to scale invariance and conformal invariance, symmetries in which a system exhibits self-similarity; in some cases, the parameters of the model can be assigned to special values, known as a "fixed point", where the field theory is conformally invariant and any running couplings cease to change.

In particle physics, this treatment reflects the changes in the underlying physical laws (codified in a quantum field theory that is renormalizable) as the energy or mass scale at which physical processes occur varies. For example, in quantum electrodynamics (QED), an electron appears to be composed of electron and positron pairs and photons at very short distances. Taken together, this set of particles has a slightly different electric charge than the dressed electron seen at large distances, and this change in the value of the charge is determined by the renormalization group equation.

## History

The renormalization group was initially developed for particle physics applications but has since been applied to solid-state physics, fluid mechanics, physical cosmology, and nanotechnology. An early article by Ernst Stueckelberg and André Petermann in 1953 anticipates the idea in quantum field theory: they noted that renormalization exhibits a group of transformations which transfers quantities from the bare terms to the counter terms, and introduced a function *h*(*e*) in quantum electrodynamics (QED), which is now known as the beta function.

### Beginnings

Murray Gell-Mann and Francis E. Low restricted the idea to scale transformations in QED in 1954 and focused on asymptotic forms of the photon propagator at high energies. They determined the variation of the electromagnetic coupling in QED by considering the scaling structure, and discovered that the coupling parameter *g*(*μ*) at the energy scale *μ* is effectively given by the group equation $g(\mu )=G^{-1}\left(\left({\frac {\mu }{M}}\right)^{d}G(g(M))\right)$ for an arbitrary Wegner's scaling function *G* and a constant *d*, in terms of the coupling *g(M)* at a reference scale *M*.

Gell-Mann and Low realized that the effective scale can be arbitrarily taken as *μ*, and can vary to define the theory at any other scale: $g(\kappa )=G^{-1}\left(\left({\frac {\kappa }{\mu }}\right)^{d}G(g(\mu ))\right)=G^{-1}\left(\left({\frac {\kappa }{M}}\right)^{d}G(g(M))\right)$ The core of the RG is this group property: as the scale *μ* varies, the theory presents self-similarly, and any scale can be accessed from any other scale by this group action. More formally, this transformation is described mathematically by Schröder's equation.

On the basis of this finite group equation and its scaling property, Gell-Mann and Low focused on infinitesimal transformations, and invented a computational method based on the function *ψ*(*g*) = *G* *d*/(∂*G*/∂*g*) which they introduced. Like the earlier function *h*(*e*), their function determines the change of the coupling *g*(*μ*) with respect to change in energy scale *μ* through a differential equation, the renormalization group equation $\displaystyle {\frac {\partial g}{\partial \ln \mu }}=\psi (g)=\beta (g)$ or the beta function. Since it is a function of *g*, integration in *g* of a perturbative estimate of it permits specification of the variation of the function with energy - effectively the function *G* in this approximation. The renormalization group prediction was confirmed 40 years later at the Large Electron–Positron Collider experiments: the fine structure "constant" of QED was measured to be about 1⁄127 at energies close to 200 GeV, as opposed to the standard low-energy physics value of 1⁄137.

### Deeper understanding

The renormalization group emerges from the renormalization of the quantum field variables, which has to address the problem of infinite terms in a quantum field theory. The process for doing this systematically for QED was created by Richard Feynman, Julian Schwinger and Shin'ichirō Tomonaga, who received the 1965 Nobel prize for these contributions. They devised the theory of mass and charge renormalization, in which the infinity in the momentum scale is cut off by an ultra-large regulator, Λ.

The dependence of physical quantities on the scale Λ is hidden, effectively swapped for the longer-distance scales at which the physical quantities are measured; as a result, all observable quantities are finite even for an infinite Λ. Gell-Mann and Low thus realized in these results that, while a tiny change in*g* is provided by the above RG equation given ψ(*g*), the self-similarity is expressed by the fact that ψ(*g*) depends explicitly only upon the parameters of the theory, and not upon the scale *μ*. Consequently, the above renormalization group equation may be solved for (*G* and thus) *g*(*μ*).

A deeper understanding of the physical meaning and generalization of the renormalization process, which goes beyond the dilation group of conventional renormalizable theories, considers methods where widely different scales appear simultaneously. It came from condensed matter physics: Leo P. Kadanoff's paper in 1966 proposed the "block-spin" renormalization group. The "blocking idea" is a way to define the components of the theory at large distances as aggregates of components at shorter distances.

This approach covered the conceptual point and was given full computational substance in the work of Kenneth Wilson. Wilson demonstrated a constructive iterative renormalization solution of a long-standing problem, the Kondo problem, in 1975, as well as the preceding seminal developments of his new method in the theory of second-order phase transitions and critical phenomena in 1971. He was awarded the Nobel prize for these contributions in 1982.

### Reformulation

The RG in particle physics was reformulated in more practical terms by Callan and Symanzik in 1970. The above beta function, which describes the "running of the coupling" parameter with scale, was found to represent the quantum-mechanical breaking of scale symmetry in a field theory. Applications of the RG to particle physics sharply increased in number in the 1970s with the establishment of the Standard Model.

In 1973, it was discovered that a theory of interacting quarks had a negative beta function. This means that an initial high-energy value of the coupling will eventuate a special value of μ at which the coupling diverges. This special value is the scale of the strong interactions, μ = ΛQCD (~200 mega-electronvolts). Conversely, the coupling becomes weak at very high energies (asymptotic freedom), and the quarks become observable as point-like particles, in deep inelastic scattering, as anticipated by Feynman–Bjorken scaling. QCD was thereby established as the quantum field theory controlling the strong interactions of particles.

Momentum space RG also became a highly developed tool in solid state physics, but was hindered by the extensive use of perturbation theory, which prevented the theory from succeeding in strongly correlated systems.

## Elementary theory

A generic theory is described by a certain function Z of the state variables $\{s_{i}\}$ and a certain set of coupling constants $\{J_{k}\}$ . This function may be a partition function, an action, a Hamiltonian, so long as it contains the whole description of the physics of the system.

For a certain transformation of the state variables $\{s_{i}\}\to \{{\tilde {s}}_{i}\}$ , the number of ${\tilde {s}}_{i}$ is less than the number of $s_{i}$ . If the Z function can be rewritten only in terms of the ${\tilde {s}}_{i}$ by a certain change in the parameters, $\{J_{k}\}\to \{{\tilde {J}}_{k}\}$ , then the theory is said to be renormalizable. The change in the parameters is implemented by a certain beta function: $\{{\tilde {J}}_{k}\}=\beta (\{J_{k}\})$ , which is said to induce a renormalization group flow (or RG flow) on the J -space. The values of J under the flow are called running couplings.

Most fundamental theories of physics with the exception of gravity are exactly renormalizable. Similarly, most theories in condensed matter physics are approximately renormalizable.

### Conformal symmetry and fixed points

Conformal symmetry is associated with the vanishing of the beta function. This can occur naturally if a coupling constant is attracted, by running, toward a fixed point at which *β*(*g*) = 0. In QCD, the fixed point occurs at short distances where *g* → 0 and is called a (trivial) ultraviolet fixed point. For heavy quarks, such as the top quark, the coupling to the Higgs boson runs toward a fixed non-zero (non-trivial) infrared fixed point The top quark Yukawa coupling lies slightly below the infrared fixed point of the Standard Model suggesting the possibility of additional new physics, such as sequential heavy Higgs bosons.

In string theory, conformal invariance of the string world-sheet is a fundamental symmetry: *β* = 0 is a requirement. Here, *β* is a function of the geometry of the space-time in which the string moves. This determines the space-time dimensionality of the string theory and enforces Einstein's equations of general relativity on the geometry. The RG is of fundamental importance to string theory and theories of grand unification.

If the fixed points of the system correspond to a free field theory, the theory is said to exhibit quantum triviality and possesses a Landau pole. For a φ4 interaction, Michael Aizenman proved that this theory is indeed trivial, for space-time dimension D ≥ 5. For D = 4, the triviality has yet to be proven rigorously, but lattice computations have provided strong evidence for this. This fact is important as quantum triviality can be used to bound or even predict parameters such as the Higgs boson mass in asymptotic safety scenarios. Numerous fixed points appear in the study of lattice Higgs theories, but the nature of the quantum field theories associated with these remains an open question. Since the RG transformations in such systems are lossy (i.e. the number of variables decreases), there need not be an inverse for a given RG transformation.

### Relevant and irrelevant operators

For a certain observable A of a physical system undergoing an RG transformation, the magnitude of the observable as the scale of the system goes from small to large determines the importance of the observable for the scaling law:

| ***If its magnitude*** ... | ***then the observable is*** ... |
|---|---|
| always increases | **relevant** |
| always decreases | **irrelevant** |
| other | **marginal** |

A relevant observable is needed to describe the macroscopic behavior of the system; irrelevant observables are not needed. Marginal observables may or may not need to be taken into account. Most observables are irrelevant, i.e., the macroscopic physics is dominated by only a few observables in most systems. As an example, in microscopic physics, to describe a system consisting of a mole of carbon-12 atoms we need of the order of 1023 (the Avogadro number) variables, while to describe it as a macroscopic system (12 grams of carbon-12) we only need a few.

### Critical exponents and universality

Before Wilson's RG approach, it was unclear why the critical exponents describing transitions in very disparate phenomena. In general, thermodynamic features of a system near a phase transition depend only on a small number of variables, such as the dimensionality and symmetry, but are insensitive to details of the underlying microscopic properties of the system. This property is known as universality.

Universality can be explained using the renormalization group, by demonstrating that the differences in phenomena among the individual fine-scale components are determined by irrelevant observables, while the relevant observables are shared in common. Therefore, many macroscopic phenomena may be grouped into a small set of universality classes, specified by the shared sets of relevant observables.

## Simple model: block spins

One of the simpler forms of RG is the block spin RG, devised by Leo P. Kadanoff in 1966. For a 2D set of atoms in a perfect square array (Figure 1), atoms interact among themselves only with their nearest neighbors at some temperature T and a certain coupling J. The physics of the system is then described by a certain function of these parameters, such as the Hamiltonian *H*(*T*, *J*).

The solid is then divided into blocks of 2×2 blocks*,* described in terms of block variables that represent the average behavior within each block. The physics of block variables is approximately described by a formula of the same kind, but with different values for T and J: *H*(*T′*, *J′*). The original problem may be computationally intractable due to the large number of atomic variables involved; in the renormalized problem, there are one fourth as many. Another iteration of the same kind leads to *H*(*T"*, *J"*), and only one sixteenth of the atoms. This process increases the observation scale with each RG step.

Iterating until there is only one large block is roughly equivalent to finding the long range behavior of the RG transformation which took (*T*,*J*) → (*T′*,*J′*) and (*T′*, *J′*) → (*T"*, *J"*). Often, when iterated many times, this RG transformation leads to a certain number of fixed points.

For the test case of an Ising model lattice of spins interacting magnetically, some positive coupling J denotes the trend of neighbor spins to be aligned. The behavior of the system is determined by competition between the J term (which tends to "order" the system by aligning spins) and the disordering effect of temperature, which the alignment of spins to vary randomly.

For models of this type, there are three fixed points:

1. *T* = 0 and *J* → ∞. At the largest scale, temperature becomes unimportant, i.e., the disordering factor vanishes and the system appears to be ordered. This is a ferromagnetic phase, where the lack of disorder leads to every spin pointing in the same direction.
2. *T* → ∞ and *J* → 0. Temperature dominates, and the system is disordered at large scales.
3. A nontrivial point between them, *T* = *T**c* and *J* = *J**c*. At this point, changing the scale does not change the physics, because the system will look the same at any choice of scales. This corresponds to the critical point of the Curie phase transition, where the two effects above are perfectly balanced.

Given a certain material with given values of T and J, the large-scale behavior of the system is then determined by these fixed points.

## Exact renormalization group equations

An exact renormalization group equation (ERGE) is one that takes irrelevant couplings into account. As there are infinitely many choices of field rescalings, there are also infinitely many different interpolating ERGEs, but the most common approaches are presented below.

### Wilson ERGE

The Wilson ERGE is the simplest conceptually, but is difficult to implement. The method begins with a Fourier transform into momentum space after Wick rotating into Euclidean space. By setting a hard momentum cutoff, *p*2 ≤ Λ2, the only degrees of freedom are those with momenta less than Λ. The partition function is $Z=\int _{p^{2}\leq \Lambda ^{2}}{\mathcal {D}}\varphi \exp \left[-S_{\Lambda }[\varphi ]\right].$ For any positive Λ′ less than Λ, the functional *S*Λ′ is defined as $\exp \left(-S_{\Lambda '}[\varphi ]\right)\ {\stackrel {\mathrm {def} }{=}}\ \int _{\Lambda '\leq p\leq \Lambda }{\mathcal {D}}\varphi \exp \left[-S_{\Lambda }[\varphi ]\right].$ If *S*Λ depends only on ϕ and not derivatives thereof, this may be rewritten as $\exp \left(-S_{\Lambda '}[\varphi ]\right)\ {\stackrel {\mathrm {def} }{=}}\ \prod _{\Lambda '\leq p\leq \Lambda }\int d\varphi (p)\exp \left[-S_{\Lambda }[\varphi (p)]\right],$ Since only functions *φ* well-defined between Λ' and Λ are integrated over, the left hand side may still depend on *ϕ* outside that range. So $Z=\int _{p^{2}\leq {\Lambda '}^{2}}{\mathcal {D}}\varphi \exp \left[-S_{\Lambda '}[\varphi ]\right].$ In fact, this transformation is transitive. If you compute *S*Λ′ from *S*Λ and then compute *SΛ′′* from *S*Λ′, this gives you the same Wilsonian action as computing *S*Λ″ directly from *S*Λ.

### Polchinski ERGE

The Polchinski ERGE involves a smooth UV regulator cutoff,an improvement over the Wilson ERGE. This suppresses contributions from momenta greater than Λ heavily. The smoothness of the cutoff, however, generates a functional differential equation in the cutoff scale Λ. As in Wilson's approach, there is a different action functional for each Λ. Each of these actions are supposed to describe exactly the same model - which means that their partition functionals have to match exactly.

As an example (in condensed deWitt notation), for a real scalar field, $Z_{\Lambda }[J]=\int {\mathcal {D}}\varphi \exp \left(-S_{\Lambda }[\varphi ]+J\cdot \varphi \right)=\int {\mathcal {D}}\varphi \exp \left(-{\tfrac {1}{2}}\varphi \cdot R_{\Lambda }\cdot \varphi -S_{\operatorname {int} \Lambda }[\varphi ]+J\cdot \varphi \right)$ and *Z*Λ is independent of Λ. The action is split into a quadratic kinetic part and an interacting part *S*int Λ. This split is not clean generically; the "interacting" part can also contain quadratic kinetic terms and if there is any wave function renormalization, it must. This can be reduced by introducing field rescalings. RΛ is a function of the momentum p and the second term in the exponent is ${\frac {1}{2}}\int {\frac {d^{d}p}{(2\pi )^{d}}}{\tilde {\varphi }}^{*}(p)R_{\Lambda }(p){\tilde {\varphi }}(p)$ when expanded.

When $p\ll \Lambda$ , *R*Λ(*p*)/*p*2 is essentially 1. When $p\gg \Lambda$ , *R*Λ(*p*)/*p*2 approaches infinity. *R*Λ(*p*)/*p*2 is always greater than or equal to 1 and is smooth. This leaves the fluctuations with momenta less than the cutoff Λ unaffected but heavily suppresses contributions from those with momenta greater than the cutoff. The condition that the partition functional be independent of the cutoff (i.e. that the derivative with respect to the cutoff is zero) can be satisfied by, for example, ${\frac {d}{d\Lambda }}S_{\operatorname {int} \Lambda }={\frac {1}{2}}{\frac {\delta S_{\operatorname {int} \Lambda }}{\delta \varphi }}\cdot \left({\frac {d}{d\Lambda }}R_{\Lambda }^{-1}\right)\cdot {\frac {\delta S_{\operatorname {int} \Lambda }}{\delta \varphi }}-{\frac {1}{2}}\operatorname {Tr} \left[{\frac {\delta ^{2}S_{\operatorname {int} \Lambda }}{\delta \varphi \,\delta \varphi }}\cdot {\frac {d}{d\Lambda }}R_{\Lambda }^{-1}\right].$ Jacques Distler claimed without proof that this ERGE is not correct nonperturbatively.

### Effective average action ERGE

The effective average action ERGE involves a smooth IR regulator cutoff, which accounts for all fluctuations up to an IR scale k. The effective average action (EAA) will be accurate for fluctuations with momenta larger than k. As k is lowered, the effective average action approaches the effective action which includes all quantum and classical fluctuations. In contrast, for large k the effective average action is close to the "bare action". So, the effective average action interpolates between the "bare action" and the effective action.

For a real scalar field, one adds an IR cutoff ${\frac {1}{2}}\int {\frac {d^{d}p}{(2\pi )^{d}}}{\tilde {\varphi }}^{*}(p)R_{k}(p){\tilde {\varphi }}(p)$ to the action S, where *R**k* is a function of both k and p such that for $p\gg k$ , Rk(p) is very tiny and approaches 0 and for $p\ll k$ , $R_{k}(p)\gtrsim k^{2}$ . *R**k* is both smooth and nonnegative. Its large value for small momenta leads to a suppression of their contribution to the partition function which is effectively the same thing as neglecting large-scale fluctuations.

Defiine the regulator as ${\frac {1}{2}}\varphi \cdot R_{k}\cdot \varphi$ So, $\exp \left(W_{k}[J]\right)=Z_{k}[J]=\int {\mathcal {D}}\varphi \exp \left(-S[\varphi ]-{\frac {1}{2}}\varphi \cdot R_{k}\cdot \varphi +J\cdot \varphi \right)$ where J is the source field. The Legendre transform of *W**k* ordinarily gives the effective action. However, the initial action is in fact *S*[*φ*] + 1/2 *φ⋅R**k*⋅*φ* and so the second term must be subtracted to get the effective average action. In other words, $\varphi [J;k]={\frac {\delta W_{k}}{\delta J}}[J]$ can be inverted to give *J**k*[*φ*] . Finally, define the effective average action Γ*k* as $\Gamma _{k}[\varphi ]\ {\stackrel {\mathrm {def} }{=}}\ \left(-W\left[J_{k}[\varphi ]\right]+J_{k}[\varphi ]\cdot \varphi \right)-{\tfrac {1}{2}}\varphi \cdot R_{k}\cdot \varphi .$ Note the effective action Γk is related to Polchinski's effective action Sint via a Legendre transform relation. Taking a derivative with respect to the cutoff completes the process, producing an expression known as the Wetterich equation.

## Renormalization group improvement of the effective potential

The renormalization group can also be used to compute effective potentials at orders higher than 1-loop, such as when computing corrections to the Coleman–Weinberg mechanism. To do so, write the renormalization group equation in terms of the effective potential. In the case of the $\varphi ^{4}$ model: $\left(\mu {\frac {\partial }{\partial \mu }}+\beta _{\lambda }{\frac {\partial }{\partial \lambda }}+\varphi \gamma _{\varphi }{\frac {\partial }{\partial \varphi }}\right)V_{\text{eff}}=0.$ In order to determine the effective potential, it is useful to write $V_{\text{eff}}$ as $V_{\text{eff}}={\frac {1}{4}}\varphi ^{4}S_{\text{eff}}{\big (}\lambda ,L(\varphi ){\big )},$ where $S_{\text{eff}}$ is a power series in $L(\varphi )=\log {\frac {\varphi ^{2}}{\mu ^{2}}}$ : $S_{\text{eff}}=A+BL+CL^{2}+DL^{3}+\cdots .$ Using the above ansatz, it is possible to solve the renormalization group equation perturbatively and find the effective potential up to desired order.
