---
title: "Renormalization"
source: https://en.wikipedia.org/wiki/Renormalization
domain: quantum-field-theory
license: CC-BY-SA-4.0
tags: quantum field theory, gauge theory, feynman diagram, path integral formulation
fetched: 2026-07-02
---

# Renormalization

**Renormalization** is a collection of techniques in quantum field theory, statistical field theory, and the theory of self-similar geometric structures, that is used to treat infinities arising in calculated quantities by altering values of these quantities to compensate for effects of their **self-interactions**. Even if no infinities arose in loop diagrams in quantum field theory, it can be shown that it is necessary to renormalize the mass and fields appearing in the original Lagrangian. This is the dominant method used in theoretical physics to treat these divergent quantities due its broad applicability, though more limited but rigorous approaches like causal perturbation theory are also used.

For example, an electron theory may begin by postulating an electron with an initial mass and charge. In quantum field theory a cloud of virtual particles, such as photons, positrons, and others surrounds and interacts with the initial electron. Accounting for the interactions of the surrounding particles (e.g. collisions at different energies) shows that the electron-system behaves as if it had a different mass and charge than initially postulated. Renormalization, in this example, mathematically replaces the initially postulated mass and charge of an electron (the bare particle) with the experimentally observed mass and charge (the dressed particle). Mathematics and experiments prove that positrons and more massive particles such as protons exhibit precisely the same observed charge as the electron – even in the presence of much stronger interactions and more intense clouds of virtual particles. Renormalization procedures are based on the requirement that certain physical quantities (such as the mass and charge of an electron) equal observed (experimental) values.

Renormalization specifies relationships between parameters in the theory when parameters describing large distance scales differ from parameters describing small distance scales. Physically, the pileup of contributions from an infinite number of scales involved in a problem may then result in further infinite quantities. When describing spacetime as a continuum, certain statistical and quantum mechanical constructions are not well-defined. To define them unambiguously, a continuum limit must carefully remove "construction scaffolding" of lattices at various scales.

Renormalization was first developed in quantum electrodynamics (QED) to make sense of infinite integrals in perturbation theory. Initially viewed as a suspect provisional procedure even by some of its originators, renormalization eventually was embraced as an important and self-consistent actual mechanism of scale physics in several fields of physics and mathematics. Despite his later skepticism, it was Paul Dirac who pioneered renormalization.

Today, on the basis of the breakthrough renormalization group insights of Nikolay Bogolyubov and Kenneth Wilson, the focus of studies of renormalization is on variation of physical quantities across contiguous scales; distant scales are instead related to each other through "effective" descriptions. All scales are linked in a broadly systematic way, and the actual physics pertinent to each is extracted with suitable computational techniques appropriate for each. Wilson clarified which variables of a system are crucial and which are redundant.

Renormalization is performed by setting a "renormalization scheme", equations which determine how the physical parameters are rescaled within the theory. Different approaches such as on-shell or minimal subtraction are required depending on the type of interaction being considered. Renormalization is distinct from regularization, another technique to control infinities by assuming the existence of new unknown physics at new scales, though the two can be used in tandem.

## Self-interactions in classical physics

The problem of infinities first arose in the classical electrodynamics of point particles in the 19th and early 20th century. The mass of a charged particle should include the mass–energy in its electrostatic field (electromagnetic mass). Assume that the particle is a charged spherical shell of radius *r*e. The mass–energy in the field is $m_{\text{em}}c^{2}=\int {\frac {1}{2}}\varepsilon _{0}E^{2}\,dV=\int _{r_{\text{e}}}^{\infty }{\frac {1}{2}}\varepsilon _{0}\left({\frac {q}{4\pi \varepsilon _{0}r^{2}}}\right)^{2}4\pi r^{2}\,dr={\frac {q^{2}}{8\pi \varepsilon _{0}r_{\text{e}}}},$ which becomes infinite as *r*e → 0. This implies that the point particle would have infinite inertia and thus cannot be accelerated. Incidentally, the value of *r*e that makes $m_{\text{em}}$ equal to the electron mass is called the classical electron radius, which (setting $q=e$ and ignoring factor of ${1}/{2}$ ) turns out to be $r_{\text{e}}={\frac {e^{2}}{4\pi \varepsilon _{0}m_{\text{e}}c^{2}}}=\alpha {\frac {\hbar }{m_{\text{e}}c}}\approx 2.8\times 10^{-15}~{\text{m}},$ where $\alpha \approx 1/137$ is the fine-structure constant, and $\hbar /(m_{\text{e}}c)$ is the reduced Compton wavelength of the electron.

The total effective mass of a spherical charged particle includes the actual bare mass of the spherical shell (in addition to the mass mentioned above associated with its electric field). If the shell's bare mass is allowed to be negative, it might be possible to take a consistent point limit. This was called renormalization, and Lorentz and Abraham attempted to develop a classical theory of the electron this way. This early work was the inspiration for later attempts at regularization and renormalization in quantum field theory.

When calculating the electromagnetic interactions of charged particles, the back-reaction of a particle's own field on itself (analogous to the back-EMF of circuit analysis.) is necessary to explain the friction on charged particles when they emit radiation. If the electron is assumed to be a point, the value of the back-reaction diverges, for the same reason that the mass diverges, because the field is inverse-square.

The Abraham–Lorentz theory includes a retrocausal "pre-acceleration", allowing solution where an electron would start moving *before* the force is applied. These problems remain in the relativistic version of the Abraham-Lorentz equation. This is a sign that the point limit is inconsistent, and/or that a quantum mechanical treatment is required.

The trouble was worse in classical field theory than in quantum field theory, because in quantum field theory a charged particle experiences Zitterbewegung due to interference with virtual particle–antiparticle pairs, thus effectively smearing out the charge over a region comparable to the Compton wavelength. In quantum electrodynamics at small coupling, the electromagnetic mass only diverges as the logarithm of the radius of the particle.

## Divergences in quantum electrodynamics

Divergences within quantum field theories are common, but were first encountered in the development of quantum electrodynamics in the 1930s by Max Born, Werner Heisenberg, Pascual Jordan, and Paul Dirac They discovered that, upon adding in perturbative corrections, many integrals within the theory were divergent.

One way of describing the perturbation theory corrections' divergences was discovered in 1947–49 by Hans Kramers, Hans Bethe, Julian Schwinger, Richard Feynman, and Shin'ichiro Tomonaga, and systematized by Freeman Dyson in 1949. The divergences appear in radiative corrections involving Feynman diagrams with closed loops of virtual particles in them.

While virtual particles obey conservation of energy and momentum, they can have any energy and momentum, even off-shell ones that are not allowed by the relativistic energy–momentum relation for the observed mass of that particle. When there is a loop, the momentum of the particles involved in the loop is not uniquely determined by the energies and momenta of incoming and outgoing particles. A variation in the energy of one particle in the loop can be balanced by an equal and opposite change in the energy of another particle in the loop, without affecting the incoming and outgoing particles. Thus many variations are possible. Finding the amplitude for the loop process requires integration over all possible combinations of energy and momentum that could travel around the loop. These integrals are often divergent.

### Ultraviolet divergences

These divergences have two types; the first is "ultraviolet" (UV), which comes from

- the region in the integral where all particles in the loop have large energies and momenta,
- very short wavelengths and high-frequencies fluctuations of the fields, in the path integral for the field,
- very short proper time between particle emission and absorption, if the loop is thought of as a sum over particle paths.

Shown in the pictures at the right margin, there are exactly three one-loop divergent loop diagrams in quantum electrodynamics:

1. A photon creates a virtual electron–positron pair, which then annihilates. This is a vacuum polarization diagram, which provides corrections to the field normalization.
2. An electron quickly emits and reabsorbs a virtual photon, called a self-energy. This diagram adjusts the mass of the electron.
3. An electron emits a photon, emits a second photon, and reabsorbs the first. This process is shown in the section below in figure 2 as a "penguin diagram", and it is called a *vertex renormalization*. This provides corrections to the electron charge.

### Infrared divergences

The second class of divergence called an infrared divergence. Every process involving charged particles emits infinitely many coherent photons of infinite wavelength, and the amplitude for emitting any finite number of photons is zero. For example, at the one-loop order, the vertex function has both ultraviolet and infrared divergences. In contrast to the ultraviolet divergence, the infrared divergence does not require the renormalization of a parameter in the theory involved. The infrared divergence of the vertex diagram is removed by including a diagram similar to the vertex diagram with the following important difference: the photon connecting the two legs of the electron is cut and replaced by two on-shell (i.e. real) photons whose wavelengths tend to infinity; this diagram is equivalent to the bremsstrahlung process. This additional diagram must be included because there is no physical way to distinguish a zero-energy photon flowing through a loop as in the vertex diagram and zero-energy photons emitted through bremsstrahlung. From a mathematical point of view, the IR divergences can be regularized by assuming fractional differentiation with respect to a parameter, for example: $\left(p^{2}-a^{2}\right)^{\frac {1}{2}}$ is well defined at *p* = *a* but is UV divergent; if we take the 3⁄2-th fractional derivative with respect to −*a*2, we obtain the IR divergence ${\frac {1}{p^{2}-a^{2}}},$ so IR divergences can be converted into UV divergences.

### Example calculation

The diagram in Figure 2 shows one of the several one-loop contributions to electron–electron scattering in QED. The electron on the left side of the diagram, represented by the solid line, starts out with 4-momentum *pμ* and ends up with 4-momentum *rμ*. It emits a virtual photon carrying *rμ* − *pμ* to transfer energy and momentum to the other electron (the black curved line). But in this diagram, before that happens, it emits another virtual photon carrying 4-momentum *qμ*, which is reabsorbed after emitting the first virtual photon. Energy and momentum conservation do not determine the 4-momentum *qμ* uniquely, so all possibilities contribute equally and we must integrate.

This diagram's amplitude ends up with, among other things, a factor from the loop of $-ie^{3}\int {\frac {d^{4}q}{(2\pi )^{4}}}\gamma ^{\mu }{\frac {i(\gamma ^{\alpha }(r-q)_{\alpha }+m)}{(r-q)^{2}-m^{2}+i\epsilon }}\gamma ^{\rho }{\frac {i(\gamma ^{\beta }(p-q)_{\beta }+m)}{(p-q)^{2}-m^{2}+i\epsilon }}\gamma ^{\nu }{\frac {-ig_{\mu \nu }}{q^{2}+i\epsilon }}.$ The various *γμ* factors in this expression are gamma matrices as in the covariant formulation of the Dirac equation; they have to do with the spin of the electron. Here e is the electric coupling constant, and i is the imaginary unit. Key here is the dependence on *qμ* of the three fractional factors in the integrand, which are from the propagators of the two electron lines and the photon line in the loop.

Expanding the integrand out, there is a term with two powers of *qμ* in the numerator that dominates at large values of *qμ*: $e^{3}\gamma ^{\mu }\gamma ^{\alpha }\gamma ^{\rho }\gamma ^{\beta }\gamma _{\mu }\int {\frac {d^{4}q}{(2\pi )^{4}}}{\frac {q_{\alpha }q_{\beta }}{(r-q)^{2}(p-q)^{2}q^{2}}}.$ This integral is divergent, unless the energy and momentum are cut off at some finite value.

## Renormalized and bare quantities

The solution to the problem of divergences was to account for the fact that initial values of quantities like the electron's electric charge and mass did not actually correspond to the physical constants measured in the laboratory. As written, the theory was using bare particles that did not take into account the contribution of virtual-particle loop effects to the physical constants themselves. In general, these effects would be just as divergent as the amplitudes under consideration in the first place, so finite measured quantities would imply divergent bare quantities.

To connect these bare values to the experimental results, the formulae would have to be rewritten in terms of measurable, renormalized quantities. The charge of the electron, for example, could be defined in terms of a quantity measured at a specific kinematic renormalization point or subtraction point (which will have a characteristic energy, called the renormalization energy scale). The remaining terms left over, involving the remaining portions of the bare quantities, could then be reinterpreted as counterterms involved in a new set of diagrams exactly canceling out the earlier set of divergent diagrams.

### Renormalization in QED

For example, in the Lagrangian of QED ${\mathcal {L}}={\bar {\psi }}_{B}\left[i\gamma _{\mu }\left(\partial ^{\mu }+ie_{B}A_{B}^{\mu }\right)-m_{B}\right]\psi _{B}-{\frac {1}{4}}F_{B\mu \nu }F_{B}^{\mu \nu }$ the fields and coupling constant are really bare quantities, hence the subscript B above. Conventionally the bare quantities are written so that the corresponding Lagrangian terms are multiples of the renormalized ones: $\left({\bar {\psi }}m\psi \right)_{B}=Z_{0}{\bar {\psi }}m\psi$ $\left({\bar {\psi }}\left(\partial ^{\mu }+ieA^{\mu }\right)\psi \right)_{B}=Z_{1}{\bar {\psi }}\left(\partial ^{\mu }+ieA^{\mu }\right)\psi$ $\left(F_{\mu \nu }F^{\mu \nu }\right)_{B}=Z_{2}\,F_{\mu \nu }F^{\mu \nu }.$ Note that gauge invariance, via a Ward–Takahashi identity, is used in the second line such that the two terms of the covariant derivative can be renormalized together.

The electron–photon interaction pictured in Figure 1 can then be written ${\mathcal {L}}_{I}=-e{\bar {\psi }}\gamma _{\mu }A^{\mu }\psi -(Z_{1}-1)e{\bar {\psi }}\gamma _{\mu }A^{\mu }\psi$ The electron charge e can then be defined in terms of some specific experiment: set the renormalization scale equal to the energy characteristic of this experiment, and the first term gives the interaction observed in the laboratory (up to small, finite corrections from loop diagrams). The rest is the counterterm. If the theory is renormalizable as in QED, the divergent parts of loop diagrams can all be decomposed into pieces with three or fewer legs, with an algebraic form that can be canceled out by the second term (or by the similar counterterms that come from *Z*0 and *Z*3).

The diagram with the *Z*1 counterterm's interaction vertex placed as in Figure 3 cancels out the divergence from the loop in Figure 2.

Historically, the splitting of the "bare terms" into the original terms and counterterms came before the renormalization group insight due to Kenneth Wilson. According to such renormalization group insights, this splitting is unphysical, as all scales of the problem enter in continuous systematic ways.

### Running couplings

To minimize the contribution of loop diagrams to a given calculation (and therefore make it easier to extract results), one chooses a renormalization point close to the energies and momenta exchanged in the interaction. However, the renormalization point is not itself a physical quantity: the physical predictions of the theory, calculated to all orders, should in principle be *independent* of the choice of renormalization point, as long as it is within the domain of application of the theory. Changes in renormalization scale will simply affect how much of a result comes from Feynman diagrams without loops, and how much comes from the remaining finite parts of loop diagrams. One can exploit this fact to calculate the effective variation of physical constants with changes in scale. This variation is encoded by beta-functions, and the general theory of this kind of scale-dependence is known as the renormalization group.

Colloquially, particle physicists often speak of certain physical "constants" as varying with the energy of interaction, though in fact, it is the renormalization scale that is the independent quantity. This *running* does, however, provide a convenient means of describing changes in the behavior of a field theory under changes in the energies involved in an interaction. For example, since the coupling in quantum chromodynamics becomes small at large energy scales, the theory behaves more like a free theory as the energy exchanged in an interaction becomes large – a phenomenon known as asymptotic freedom. Choosing an increasing energy scale and using the renormalization group makes this clear from simple Feynman diagrams; were this not done, the prediction would be the same, but would arise from complicated high-order cancellations.

For example, $I=\int _{0}^{a}{\frac {1}{z}}\,dz-\int _{0}^{b}{\frac {1}{z}}\,dz=\ln a-\ln b-\ln 0+\ln 0$ is ill-defined.

To eliminate the divergence, simply change lower limit of integral into εa and εb: $I=\ln a-\ln b-\ln {\varepsilon _{a}}+\ln {\varepsilon _{b}}=\ln {\tfrac {a}{b}}-\ln {\tfrac {\varepsilon _{a}}{\varepsilon _{b}}}$ Making sure ⁠*εb*/*εa*⁠ → 1, then *I* = ln ⁠*a*/*b*⁠.

## Renormalization and regularization

Since the quantity ∞ − ∞ is ill-defined, the cancelling of divergences can be made mathematically rigorous using the theory of limits, in a process known as regularization. Integrals can be made to converge at high momenta and energy by introducing an additional modification to their form known as a regulator. A regulator has a characteristic energy scale known as the cutoff; taking this cutoff to infinity (or, equivalently, the corresponding length/time scale to zero) recovers the original integrals. Divergent terms in the integrals then become finite but cutoff-dependent, which can be canceled out with cutoff-dependent counterterms. The cutoff is taken to infinity and finite physical results are recovered; if physics on measurable scales is independent of what happens at the very short distance and time scales, then it should be possible to get cutoff-independent results.

Many different types of regulator are used in quantum field theory. One of the most popular is dimensional regularization, in which integrals are extended into a space with a fictitious fractional number of dimensions. Another is Pauli–Villars regularization, which adds fictitious particles with very large masses to the theory, such that loop integrands involving the massive particles cancel out the existing loops at large momenta. Yet another regularization scheme is the lattice regularization, which places four-dimensional spacetime on a lattice with a fixed grid size; this size constrains the momentum that a particle can possess when propagating on the lattice. After treating several lattices with different grid size, the physical result is extrapolated to grid size zero i.e. the continuum limit, producing the physics of the natural universe.

## Attitudes and interpretation

The early formulators of QED and other quantum field theories were, as a rule, dissatisfied with this state of affairs. It seemed illegitimate to do something tantamount to subtracting infinities from infinities to get finite answers. Dyson argued that these infinities are of a basic nature and cannot be eliminated by any formal mathematical procedures, such as the renormalization method.

Dirac's criticism was the most persistent. As late as 1975, he was saying:

> Most physicists are very satisfied with the situation. They say: 'Quantum electrodynamics is a good theory and we do not have to worry about it any more.' I must say that I am very dissatisfied with the situation because this so-called 'good theory' does involve neglecting infinities which appear in its equations, ignoring them in an arbitrary way. This is just not sensible mathematics. Sensible mathematics involves disregarding a quantity when it is small – not neglecting it just because it is infinitely great and you do not want it!

Another important critic was Feynman. Despite his crucial role in the development of quantum electrodynamics, he wrote the following in 1985:

> The shell game that we play to find *n* and *j* is technically called 'renormalization'. But no matter how clever the word, it is still what I would call a dippy process! Having to resort to such hocus-pocus has prevented us from proving that the theory of quantum electrodynamics is mathematically self-consistent. It's surprising that the theory still hasn't been proved self-consistent one way or the other by now; I suspect that renormalization is not mathematically legitimate.

Feynman was concerned that all field theories known in the 1960s had the property that the interactions become infinitely strong at short enough distance scales. These Landau poles made it plausible that quantum field theories were all inconsistent. In 1974, David Gross, Hugh David Politzer and Frank Wilczek showed that another quantum field theory, quantum chromodynamics, does not have a Landau pole. Feynman, along with most others, accepted that quantum chromodynamics was a fully consistent theory.

The general unease was almost universal in texts up to the 1970s and 1980s. Beginning in the 1970s, however, inspired by work on the renormalization group and effective field theory, and despite the fact that Dirac and various others never withdrew their criticisms, attitudes began to change. Kenneth G. Wilson and others demonstrated that the renormalization group is useful in statistical field theory applied to condensed matter physics, where it provides important insights into the behavior of phase transitions. In condensed matter physics, a physical short-distance regulator exists: matter ceases to be continuous on the scale of atoms. Short-distance divergences in condensed matter physics do not present a philosophical problem since the field theory is only an effective, smoothed-out representation of the behavior of matter; there are no infinities since the cutoff is always finite, and the bare quantities are cutoff-dependent.

If quantum field theory holds past the Planck length, then there may be no problem with short-distance divergences in particle physics either, and all field theories could simply be effective field theories.

However, Abdus Salam remarked in 1972:

> Field-theoretic infinities – first encountered in Lorentz's computation of electron self-mass – have persisted in classical electrodynamics for seventy and in quantum electrodynamics for some thirty-five years. These long years of frustration have left in the subject a curious affection for the infinities and a passionate belief that they are an inevitable part of nature; so much so that even the suggestion of a hope that they may, after all, be circumvented — and finite values for the renormalization constants computed – is considered irrational.

In quantum field theory, the value of a physical constant depends on the scale that one chooses as the renormalization point. The coupling constants in the Standard Model of particle physics vary in different ways with increasing energy scale: the coupling of quantum chromodynamics and the weak isospin coupling of the electroweak force tend to decrease, and the weak hypercharge coupling of the electroweak force tends to increase. At energy scale of 1015 GeV (far beyond the reach of current particle accelerators), they all become approximately the same size, a major motivation for speculations about grand unified theory.

If a renormalized theory can only be interpreted as an effective field theory, then the problem remains of discovering a more accurate theory that does not have these renormalization problems. As Lewis Ryder has put it, "In the Quantum Theory, these [classical] divergences do not disappear; on the contrary, they appear to get worse. And despite the comparative success of renormalisation theory, the feeling remains that there ought to be a more satisfactory way of doing things."

## Renormalizability

Not all theories lend themselves to renormalization in the manner described above, with a finite supply of counterterms and all quantities becoming cutoff-independent at the end of the calculation. If the Lagrangian contains combinations of field operators of high enough dimension in energy units, an infinite number of counterterms is required to cancel all divergences. At first glance, the theory would seem to gain an infinite number of free parameters and therefore lose all predictive power. Such theories are called "nonrenormalizable".

The Standard Model of particle physics contains only renormalizable operators, but the interactions of general relativity become nonrenormalizable if one attempts to construct a field theory of quantum gravity in the most straightforward manner (treating the metric in the Einstein–Hilbert Lagrangian as a perturbation about the Minkowski metric), suggesting that perturbation theory is not satisfactory in application to quantum gravity.

However, in an effective field theory, "renormalizability" is a misnomer. In nonrenormalizable effective field theory, terms in the Lagrangian do multiply to infinity, but have coefficients suppressed by ever-increasing inverse powers of the energy cutoff. If the cutoff is a physical quantity—that is, if the theory is only an effective description of physics up to some maximum energy or minimum distance scale—then these additional terms could represent real physical interactions. Assuming that the dimensionless constants in the theory do not get too large, one can group calculations by inverse powers of the cutoff, and extract approximate predictions to finite order in the cutoff that still have a finite number of free parameters. This can be used to renormalize these "nonrenormalizable" interactions.

Nonrenormalizable interactions in effective field theories rapidly become weaker as the energy scale becomes much smaller than the cutoff. The classic example is the Fermi theory of the weak nuclear force, a nonrenormalizable effective theory whose cutoff is comparable to the mass of the W particle. This fact may also provide a possible explanation for why almost all of the particle interactions we see are describable by renormalizable theories: others that may exist at the GUT or Planck scale simply become too weak to be observable. There is one exception: gravity, the exceedingly weak interaction of which is magnified by the presence of the enormous masses of stars and planets.

## In statistical physics

### History

A deeper understanding of the physical meaning and generalization of the renormalization process, which goes beyond the dilatation group of conventional renormalizable theories, came from condensed matter physics. Leo P. Kadanoff's proposed the "block-spin" renormalization group, which defines the components of the theory at large distances as aggregates of components at shorter distances.

This approach covered the conceptual point and was given full computational substance by Kenneth Wilson. Wilson developed his new method by applying it to the theory of second-order phase transitions and critical phenomena in 1971, and demonstrated a constructive iterative renormalization solution of the long-standing problem Kondo problem in 1974 He was awarded the Nobel Prize in Physics for these contributions in 1982.

### Principles

In more technical terms, consider a theory described by a certain function Z of the state variables $\{s_{i}\}$ and coupling constants $\{J_{k}\}$ . Z may be a partition function, an action, a Hamiltonian, etc - it must contain the whole description of the physics of the system.

Consider a blocking transformation of the state variables $\{s_{i}\}\to \{{\tilde {s}}_{i}\}$ , where the number of ${\tilde {s}}_{i}$ must be lower than the number of $s_{i}$ . If Z can be written as a function of only the ${\tilde {s}}_{i}$ via a similar transformation of the couplings, $\{J_{k}\}\to \{{\tilde {J}}_{k}\}$ , then the theory is said to be renormalizable.The possible macroscopic states of the system, at a large scale, are given by this set of fixed points within the renormalization group flow of the beta functions associated with the couplings.
