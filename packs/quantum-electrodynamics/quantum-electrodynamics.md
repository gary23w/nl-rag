---
title: "Quantum electrodynamics"
source: https://en.wikipedia.org/wiki/Quantum_electrodynamics
domain: quantum-electrodynamics
license: CC-BY-SA-4.0
tags: quantum electrodynamics, vacuum polarization, compton scattering, dirac equation
fetched: 2026-07-02
---

# Quantum electrodynamics

In particle physics, **quantum electrodynamics** (**QED**) is the relativistic quantum field theory of electrodynamics. In essence, it describes how light and matter interact and is the first theory where full agreement between quantum mechanics and special relativity is achieved. QED mathematically describes all phenomena involving electrically charged particles interacting by means of exchange of photons and represents the quantum counterpart of classical electromagnetism giving a complete account of matter and light interaction.

In technical terms, QED can be described as a perturbation theory of the electromagnetic quantum vacuum. Richard Feynman called it "the jewel of physics" for its extremely accurate predictions of quantities like the anomalous magnetic moment of the electron and the Lamb shift of the energy levels of hydrogen. It is the most precise and stringently tested theory in physics. However, the prediction of vacuum zero energy made by QED has 10^120 magnitude of difference compared to experimental observation value. This is called cosmological constant problem or vacuum catastrophe.

## History

The first formulation of a quantum theory describing radiation and matter interaction is attributed to Paul Dirac, who during the 1920s computed the coefficient of spontaneous emission of an atom. He is credited with coining the term "quantum electrodynamics".

Dirac described the quantization of the electromagnetic field as an ensemble of harmonic oscillators with the introduction of the concept of creation and annihilation operators of particles. In the following years, with contributions from Wolfgang Pauli, Eugene Wigner, Pascual Jordan, Werner Heisenberg and Enrico Fermi, physicists came to believe that, in principle, it was possible to perform any computation for any physical process involving photons and charged particles. However, further studies by Felix Bloch with Arnold Nordsieck, and Victor Weisskopf, in 1937 and 1939, revealed that such computations were reliable only at a first order of perturbation theory, a problem already pointed out by Robert Oppenheimer. At higher orders in the series infinities emerged, making such computations meaningless and casting doubt on the theory's internal consistency. This suggested that special relativity and quantum mechanics were fundamentally incompatible.

Difficulties increased through the end of the 1940s. Improvements in microwave technology made it possible to take more precise measurements of the shift of the levels of a hydrogen atom, later known as the Lamb shift and magnetic moment of the electron. These experiments exposed discrepancies that the theory was unable to explain.

A first indication of a possible solution was given by Hans Bethe in 1947. He made the first non-relativistic computation of the shift of the lines of the hydrogen atom as measured by Willis Lamb and Robert Retherford. Despite limitations of the computation, agreement was excellent. The idea was simply to attach infinities to corrections of mass and charge that were actually fixed to a finite value by experiments. In this way, the infinities get absorbed in those constants and yield a finite result with good experimental agreement. This procedure was named renormalization.

Based on Bethe's intuition and fundamental papers on the subject by Shin'ichirō Tomonaga, Julian Schwinger, Richard Feynman and Freeman Dyson, it was finally possible to produce fully covariant formulations that were finite at any order in a perturbation series of quantum electrodynamics. Tomonaga, Schwinger, and Feynman were jointly awarded the 1965 Nobel Prize in Physics for their work in this area. Their contributions, and Dyson's, were about covariant and gauge-invariant formulations of quantum electrodynamics that allow computations of observables at any order of perturbation theory. Feynman's mathematical technique, based on his diagrams, initially seemed unlike the field-theoretic, operator-based approach of Schwinger and Tomonaga, but Dyson later showed that the two approaches were equivalent. Renormalization, the need to attach a physical meaning at certain divergences appearing in the theory through integrals, became one of the fundamental aspects of quantum field theory and is seen as a criterion for a theory's general acceptability. Even though renormalization works well in practice, Feynman was never entirely comfortable with its mathematical validity, referring to renormalization as a "shell game" and "hocus pocus".

Neither Feynman nor Dirac were happy with that way to approach the observations made in theoretical physics, above all in quantum mechanics.

QED is the model and template for all subsequent quantum field theories. One such subsequent theory is quantum chromodynamics, which began in the early 1960s and attained its present form in the 1970s, developed by H. David Politzer, Sidney Coleman, David Gross and Frank Wilczek. Building on Schwinger's pioneering work, Gerald Guralnik, Dick Hagen, and Tom Kibble, Peter Higgs, Jeffrey Goldstone, and others, Sheldon Glashow, Steven Weinberg and Abdus Salam independently showed how the weak nuclear force and quantum electrodynamics could be merged into a single electroweak force.

## Feynman's view of quantum electrodynamics

### Introduction

Near the end of his life, Richard Feynman gave a series of lectures on QED intended for the lay public. These lectures were transcribed and published as Feynman (1985), *QED: The Strange Theory of Light and Matter*, a classic non-mathematical exposition of QED from the point of view articulated below.

The key components of Feynman's presentation of QED are three basic actions.

A

photon

goes from one place and time to another place and time.

An

electron

goes from one place and time to another place and time.

An electron emits or absorbs a photon at a certain place and time.

These actions are represented in the form of visual shorthand by the three basic elements of diagrams: a wavy line for the photon, a straight line for the electron and a junction of two straight lines and a wavy one for a vertex representing emission or absorption of a photon by an electron. These can all be seen in the adjacent diagram.

As well as the visual shorthand for the actions, Feynman introduces another kind of shorthand for the numerical quantities called probability amplitudes. The probability is the square of the absolute value of total probability amplitude, ${\text{probability}}=|f({\text{amplitude}})|^{2}$ . If a photon moves from one place and time A to another place and time B , the associated quantity is written in Feynman's shorthand as $P(A{\text{ to }}B)$ , and it depends on only the momentum and polarization of the photon. The similar quantity for an electron moving from C to D is written $E(C{\text{ to }}D)$ . It depends on the momentum and polarization of the electron, in addition to a constant Feynman calls *n*, sometimes called the "bare" mass of the electron: it is related to, but not the same as, the measured electron mass. Finally, the quantity that tells us about the probability amplitude for an electron to emit or absorb a photon Feynman calls *j*, and is sometimes called the "bare" charge of the electron: it is a constant, and is related to, but not the same as, the measured electron charge *e*.

QED is based on the assumption that complex interactions of many electrons and photons can be represented by fitting together a suitable collection of the above three building blocks and then using the probability amplitudes to calculate the probability of any such complex interaction. It turns out that the basic idea of QED can be communicated while assuming that the square of the total of the probability amplitudes mentioned above (*P*(*A* to *B*), *E*(*C* to *D*) and *j*) acts just like our everyday probability (a simplification made in Feynman's book). Later on, this will be corrected to include specifically quantum-style mathematics, following Feynman.

The basic rules of probability amplitudes that will be used are:

1. If an event can occur via a number of *indistinguishable* alternative processes (a.k.a. "virtual" processes), then its probability amplitude is the **sum** of the probability amplitudes of the alternatives.
2. If a virtual process involves a number of independent or concomitant sub-processes, then the probability amplitude of the total (compound) process is the **product** of the probability amplitudes of the sub-processes.

The indistinguishability criterion in (a) is very important: it means that there is *no observable feature present in the given system* that in any way "reveals" which alternative is taken. In such a case, one cannot observe which alternative actually takes place without changing the experimental setup in some way (e.g. by introducing a new apparatus into the system). Whenever one *is* able to observe which alternative takes place, one always finds that the *probability* of the event is the sum of the *probabilities* of the alternatives. Indeed, if this were not the case, the very term "alternatives" to describe these processes would be inappropriate. What (a) says is that once the *physical means* for observing which alternative occurred is *removed*, one cannot still say that the event is occurring through "exactly one of the alternatives" in the sense of adding probabilities; one must add the amplitudes instead.

Similarly, the independence criterion in (b) is very important: it only applies to processes which are not "entangled".

### Basic constructions

Suppose we start with one electron at a certain place and time (this place and time being given the arbitrary label *A*) and a photon at another place and time (given the label *B*). A typical question from a physical standpoint is: "What is the probability of finding an electron at *C* (another place and a later time) and a photon at *D* (yet another place and time)?". The simplest process to achieve this end is for the electron to move from *A* to *C* (an elementary action) and for the photon to move from *B* to *D* (another elementary action). From a knowledge of the probability amplitudes of each of these sub-processes – *E*(*A* to *C*) and *P*(*B* to *D*) – we would expect to calculate the probability amplitude of both happening together by multiplying them, using rule b) above. This gives a simple estimated overall probability amplitude, which is squared to give an estimated probability.

But there are other ways in which the result could come about. The electron might move to a place and time *E*, where it absorbs the photon; then move on before emitting another photon at *F*; then move on to *C*, where it is detected, while the new photon moves on to *D*. The probability of this complex process can again be calculated by knowing the probability amplitudes of each of the individual actions: three electron actions, two photon actions and two vertexes – one emission and one absorption. We would expect to find the total probability amplitude by multiplying the probability amplitudes of each of the actions, for any chosen positions of *E* and *F*. We then, using rule a) above, have to add up all these probability amplitudes for all the alternatives for *E* and *F*. (This is not elementary in practice and involves integration.) But there is another possibility, which is that the electron first moves to *G*, where it emits a photon, which goes on to *D*, while the electron moves on to *H*, where it absorbs the first photon, before moving on to *C*. Again, we can calculate the probability amplitude of these possibilities (for all points *G* and *H*). We then have a better estimation for the total probability amplitude by adding the probability amplitudes of these two possibilities to our original simple estimate. Incidentally, the name given to this process of a photon interacting with an electron in this way is Compton scattering.

An *infinite number* of other intermediate "virtual" processes exist in which photons are absorbed or emitted. For each of these processes, a Feynman diagram could be drawn describing it. This implies a complex computation for the resulting probability amplitudes, but provided it is the case that the more complicated the diagram, the less it contributes to the result, it is only a matter of time and effort to find as accurate an answer as one wants to the original question. This is the basic approach of QED. To calculate the probability of *any* interactive process between electrons and photons, it is a matter of first noting, with Feynman diagrams, all the possible ways in which the process can be constructed from the three basic elements. Each diagram involves some calculation involving definite rules to find the associated probability amplitude.

That basic scaffolding remains when one moves to a quantum description, but some conceptual changes are needed. One is that whereas we might expect in our everyday life that there would be some constraints on the points to which a particle can move, that is *not* true in full quantum electrodynamics. There is a nonzero probability amplitude of an electron at *A*, or a photon at *B*, moving as a basic action to *any other place and time in the universe*. That includes places that could only be reached at speeds greater than that of light and also *earlier times*. (An electron moving backwards in time can be viewed as a positron moving forward in time.)

### Probability amplitudes

Quantum mechanics introduces an important change in the way probabilities are computed. Probabilities are still represented by the usual real numbers we use for probabilities in our everyday world, but probabilities are computed as the square modulus of probability amplitudes, which are complex numbers.

Feynman avoids exposing the reader to the mathematics of complex numbers by using a simple but accurate representation of them as arrows on a piece of paper or screen. (These must not be confused with the arrows of Feynman diagrams, which are simplified representations in two dimensions of a relationship between points in three dimensions of space and one of time.) The amplitude arrows are fundamental to the description of the world given by quantum theory. They are related to our everyday ideas of probability by the simple rule that the probability of an event is the *square* of the length of the corresponding amplitude arrow. So, for a given process, if two probability amplitudes, **v** and **w**, are involved, the probability of the process will be given either by

$P=|\mathbf {v} +\mathbf {w} |^{2}$

or

$P=|\mathbf {v} \,\mathbf {w} |^{2}.$

The rules as regards adding or multiplying, however, are the same as above. But where you would expect to add or multiply probabilities, instead you add or multiply probability amplitudes that now are complex numbers.

Addition and multiplication are common operations in the theory of complex numbers and are given in the figures. The sum is found as follows. Let the start of the second arrow be at the end of the first. The sum is then a third arrow that goes directly from the beginning of the first to the end of the second. The product of two arrows is an arrow whose length is the product of the two lengths. The direction of the product is found by adding the angles that each of the two have been turned through relative to a reference direction: that gives the angle that the product is turned relative to the reference direction.

That change, from probabilities to probability amplitudes, complicates the mathematics without changing the basic approach. But that change is still not quite enough because it fails to take into account the fact that both photons and electrons can be polarized, which is to say that their orientations in space and time have to be taken into account. Therefore, *P*(*A* to *B*) consists of 16 complex numbers, or probability amplitude arrows. There are also some minor changes to do with the quantity *j*, which may have to be rotated by a multiple of 90° for some polarizations, which is only of interest for the detailed bookkeeping.

Associated with the fact that the electron can be polarized is another small necessary detail, which is connected with the fact that an electron is a fermion and obeys Fermi–Dirac statistics. The basic rule is that if we have the probability amplitude for a given complex process involving more than one electron, then when we include (as we always must) the complementary Feynman diagram in which we exchange two electron events, the resulting amplitude is the reverse – the negative – of the first. The simplest case would be two electrons starting at *A* and *B* ending at *C* and *D*. The amplitude would be calculated as the "difference", *E*(*A* to *D*) × *E*(*B* to *C*) − *E*(*A* to *C*) × *E*(*B* to *D*), where we would expect, from our everyday idea of probabilities, that it would be a sum.

### Propagators

Finally, one has to compute *P*(*A* to *B*) and *E*(*C* to *D*) corresponding to the probability amplitudes for the photon and the electron respectively. These are essentially the solutions of the Dirac equation, which describe the behavior of the electron's probability amplitude and the Maxwell's equations, which describes the behavior of the photon's probability amplitude. These are called Feynman propagators. The translation to a notation commonly used in the standard literature is as follows:

$P(A{\text{ to }}B)\to D_{F}(x_{B}-x_{A}),\quad E(C{\text{ to }}D)\to S_{F}(x_{D}-x_{C}),$

where a shorthand symbol such as $x_{A}$ stands for the four real numbers that give the time and position in three dimensions of the point labeled *A*.

### Mass renormalization

A problem arose historically which held up progress for twenty years: although we start with the assumption of three basic "simple" actions, the rules of the game say that if we want to calculate the probability amplitude for an electron to get from *A* to *B*, we must take into account *all* the possible ways: all possible Feynman diagrams with those endpoints. Thus there will be a way in which the electron travels to *C*, emits a photon there and then absorbs it again at *D* before moving on to *B*. Or it could do this kind of thing twice, or more. In short, we have a fractal-like situation in which if we look closely at a line, it breaks up into a collection of "simple" lines, each of which, if looked at closely, are in turn composed of "simple" lines, and so on *ad infinitum*. This is a challenging situation to handle. If adding that detail only altered things slightly, then it would not have been too bad, but disaster struck when it was found that the simple correction mentioned above led to *infinite* probability amplitudes. In time this problem was "fixed" by the technique of renormalization. However, Feynman himself remained unhappy about it, calling it a "dippy process", and Dirac also criticized this procedure, saying "in mathematics one does not get rid of infinities when it does not please you".

### Conclusions

Within the above framework physicists were then able to calculate to a high degree of accuracy some of the properties of electrons, such as the anomalous magnetic dipole moment. However, as Feynman points out, it fails to explain why particles such as the electron have the masses they do. "There is no theory that adequately explains these numbers. We use the numbers in all our theories, but we don't understand them – what they are, or where they come from. I believe that from a fundamental point of view, this is a very interesting and serious problem."

## Mathematical formulation

### QED action

Mathematically, QED is an abelian gauge theory with the symmetry group U(1), defined on Minkowski space (flat spacetime). The gauge field, which mediates the interaction between the charged spin-1/2 fields, is the electromagnetic field. The QED Lagrangian for a spin-1/2 field interacting with the electromagnetic field in natural units gives rise to the action

QED Action

$S_{\text{QED}}=\int d^{4}x\,\left[-{\frac {1}{4}}F^{\mu \nu }F_{\mu \nu }+{\bar {\psi }}\,(i\gamma ^{\mu }D_{\mu }-m)\,\psi \right]$

where

- $\gamma ^{\mu }$ are Dirac matrices.
- $\psi$ a Dirac spinor field of spin-1/2 particles (e.g. electron–positron field).
- ${\bar {\psi }}\equiv \psi ^{\dagger }\gamma ^{0}$ , called "psi-bar", is sometimes referred to as the Dirac adjoint.
- $D_{\mu }\equiv \partial _{\mu }+ieA_{\mu }+ieB_{\mu }$ is the gauge covariant derivative.
  - *e* is the coupling constant, equal to the electric charge of the Dirac spinor field.
  - $A_{\mu }$ is the covariant four-potential of the electromagnetic field generated by the electron itself. It is also known as a gauge field or a ${\text{U}}(1)$ connection.
  - $B_{\mu }$ is the external field imposed by external source.
- *m* is the mass of the electron or positron.
- $F_{\mu \nu }=\partial _{\mu }A_{\nu }-\partial _{\nu }A_{\mu }$ is the electromagnetic field tensor. This is also known as the curvature of the gauge field.

Expanding the covariant derivative reveals a second useful form of the Lagrangian (external field $B_{\mu }$ set to zero for simplicity)

${\mathcal {L}}=-{\frac {1}{4}}F_{\mu \nu }F^{\mu \nu }+{\bar {\psi }}(i\gamma ^{\mu }\partial _{\mu }-m)\psi -ej^{\mu }A_{\mu }$

where $j^{\mu }$ is the conserved ${\text{U}}(1)$ current arising from Noether's theorem. It is written

$j^{\mu }={\bar {\psi }}\gamma ^{\mu }\psi .$

### Equations of motion

Expanding the covariant derivative in the Lagrangian gives

${\mathcal {L}}=-{\frac {1}{4}}F_{\mu \nu }F^{\mu \nu }+i{\bar {\psi }}\gamma ^{\mu }\partial _{\mu }\psi -e{\bar {\psi }}\gamma ^{\mu }A_{\mu }\psi -m{\bar {\psi }}\psi$

$=-{\frac {1}{4}}F_{\mu \nu }F^{\mu \nu }+i{\bar {\psi }}\gamma ^{\mu }\partial _{\mu }\psi -m{\bar {\psi }}\psi -ej^{\mu }A_{\mu }.$

For simplicity, $B_{\mu }$ has been set to zero, with no loss of generality. Alternatively, we can absorb $B_{\mu }$ into a new gauge field $A'_{\mu }=A_{\mu }+B_{\mu }$ and relabel the new field as $A_{\mu }.$

From this Lagrangian, the equations of motion for the $\psi$ and $A_{\mu }$ fields can be obtained.

#### Equation of motion for ψ

These arise most straightforwardly by considering the Euler-Lagrange equation for ${\bar {\psi }}$ . Since the Lagrangian contains no $\partial _{\mu }{\bar {\psi }}$ terms, we immediately get

${\frac {\partial {\mathcal {L}}}{\partial (\partial _{\mu }{\bar {\psi }})}}=0$

so the equation of motion can be written $(i\gamma ^{\mu }\partial _{\mu }-m)\psi =e\gamma ^{\mu }A_{\mu }\psi .$

#### Equation of motion for Aμ

- Using the Euler–Lagrange equation for the $A_{\mu }$ field,

| $\partial _{\nu }\left({\frac {\partial {\mathcal {L}}}{\partial (\partial _{\nu }A_{\mu })}}\right)-{\frac {\partial {\mathcal {L}}}{\partial A_{\mu }}}=0,$ |   | 3 |
|---|---|---|

the derivatives this time are $\partial _{\nu }\left({\frac {\partial {\mathcal {L}}}{\partial (\partial _{\nu }A_{\mu })}}\right)=\partial _{\nu }\left(\partial ^{\mu }A^{\nu }-\partial ^{\nu }A^{\mu }\right),$ ${\frac {\partial {\mathcal {L}}}{\partial A_{\mu }}}=-e{\bar {\psi }}\gamma ^{\mu }\psi .$

Substituting back into (**3**) leads to

$\partial _{\mu }F^{\mu \nu }=e{\bar {\psi }}\gamma ^{\nu }\psi$

which can be written in terms of the ${\text{U}}(1)$ current $j^{\mu }$ as

$\partial _{\mu }F^{\mu \nu }=ej^{\nu }.$

Now, if we impose the Lorenz gauge condition $\partial _{\mu }A^{\mu }=0,$ the equations reduce to $\Box A^{\mu }=ej^{\mu },$ which is a wave equation for the four-potential, the QED version of the classical Maxwell equations in the Lorenz gauge. (The square represents the wave operator, $\Box =\partial _{\mu }\partial ^{\mu }$ .)

### Interaction picture

This theory can be straightforwardly quantized by treating bosonic and fermionic sectors as free. This permits us to build a set of asymptotic states that can be used to start computation of the probability amplitudes for different processes. In order to do so, we have to compute an evolution operator, which for a given initial state $|i\rangle$ will give a final state $\langle f|$ in such a way to have

$S_{fi}=\langle f|U|i\rangle .$

This technique is also known as the S-matrix, and $S_{fi}$ is therefore known as the S-matrix element. The evolution operator is obtained in the interaction picture, where time evolution is given by the interaction Hamiltonian, which is the integral over space of the second term in the Lagrangian density given above:

$V=e\int d^{3}x\,{\bar {\psi }}\gamma ^{\mu }\psi A_{\mu },$

Which can also be written in terms of an integral over the interaction Hamiltonian density ${\mathcal {H}}_{I}=e{\overline {\psi }}\gamma ^{\mu }\psi A_{\mu }$ . Thus, one has

$U=T\exp \left[-{\frac {i}{\hbar }}\int _{t_{0}}^{t}dt'\,V(t')\right],$

where *T* is the time-ordering operator. This evolution operator only has meaning as a series, and what we get here is a perturbation series with the fine-structure constant as the development parameter. This series expansion of the probability amplitude $S_{fi}$ is called the Dyson series, and is given by:

$S_{fi}=\langle f|U|i\rangle =\left\langle f\left|\sum _{n=0}^{\infty }{\frac {(-i)^{n}}{n!}}\int d^{4}x_{1}\cdots \int d^{4}x_{n}T{\bigg \{}{\mathcal {H}}(x_{1})\cdots {\mathcal {H}}(x_{n}){\bigg \}}\right|i\right\rangle$

As $S_{fi}$ typically contains delta functions that are not physically-measurable, it is convenient to define the **invariant amplitude** $M_{fi}$ with:

$S_{fi}=\langle f|i\rangle +(iM_{fi}\times {\text{Delta function terms}})$

### Feynman diagrams

Despite the conceptual clarity of the Feynman approach to QED, almost no early textbooks follow him in their presentation. When performing calculations, it is much easier to work with the Fourier transforms of the propagators. Experimental tests of quantum electrodynamics are typically scattering experiments. In scattering theory, particles' momenta rather than their positions are considered, and it is convenient to think of particles as being created or annihilated when they interact. Feynman diagrams then *look* the same, but the lines have different interpretations. The electron line represents an electron with a given energy and momentum, with a similar interpretation of the photon line. A vertex diagram represents the annihilation of one electron and the creation of another together with the absorption or creation of a photon, each having specified energies and momenta.

Using Wick's theorem on the terms of the Dyson series, all the terms of the S-matrix for quantum electrodynamics can be computed through the technique of Feynman diagrams. In this case, rules for drawing are the following

To these rules we must add a further one for closed loops that implies an integration on momenta ${\textstyle \int d^{4}p/(2\pi )^{4}}$ , since these internal ("virtual") particles are not constrained to any specific energy–momentum, even that usually required by special relativity (see Propagator for details). The signature of the metric $\eta _{\mu \nu }$ is ${\rm {diag}}(+---)$ .

From them, computations of probability amplitudes are straightforwardly given. An example is Compton scattering, with an electron and a photon undergoing elastic scattering. Feynman diagrams are in this case

and so we are able to get the corresponding amplitude at the first order of a perturbation series for the S-matrix:

$M_{fi}=(ie)^{2}{\overline {u}}({\vec {p}}',s')\epsilon \!\!\!/\,'({\vec {k}}',\lambda ')^{*}{\frac {p\!\!\!/+k\!\!\!/+m_{e}}{(p+k)^{2}-m_{e}^{2}}}\epsilon \!\!\!/({\vec {k}},\lambda )u({\vec {p}},s)+(ie)^{2}{\overline {u}}({\vec {p}}',s')\epsilon \!\!\!/({\vec {k}},\lambda ){\frac {p\!\!\!/-k\!\!\!/'+m_{e}}{(p-k')^{2}-m_{e}^{2}}}\epsilon \!\!\!/\,'({\vec {k}}',\lambda ')^{*}u({\vec {p}},s),$

from which we can compute the cross section for this scattering.

### Nonperturbative phenomena

The predictive success of quantum electrodynamics largely rests on the use of perturbation theory, expressed in Feynman diagrams. However, quantum electrodynamics also leads to predictions beyond perturbation theory. In the presence of very strong electric fields, it predicts that electrons and positrons will be spontaneously produced, so causing the decay of the field. This process, called the Schwinger effect, cannot be understood in terms of any finite number of Feynman diagrams and hence is described as nonperturbative. Mathematically, it can be derived by a semiclassical approximation to the path integral of quantum electrodynamics.

## Renormalizability

Higher-order terms can be straightforwardly computed for the evolution operator, but these terms display diagrams containing the following simpler ones

- (One-loop contribution to the vacuum polarization function '"`UNIQ--postMath-00000041-QINU`"') One-loop contribution to the vacuum polarization function $\Pi$
- (One-loop contribution to the electron self-energy function '"`UNIQ--postMath-00000042-QINU`"') One-loop contribution to the electron self-energy function $\Sigma$
- (One-loop contribution to the vertex function '"`UNIQ--postMath-00000043-QINU`"') One-loop contribution to the vertex function $\Gamma$

that, being closed loops, imply the presence of diverging integrals having no mathematical meaning. To overcome this difficulty, a technique called renormalization has been devised, producing finite results in very close agreement with experiments. A criterion for the theory being meaningful after renormalization is that the number of diverging diagrams is finite. In this case, the theory is said to be "renormalizable". The reason for this is that to get observables renormalized, one needs a finite number of constants to maintain the predictive value of the theory untouched. This is exactly the case of quantum electrodynamics displaying just three diverging diagrams. This procedure gives observables in very close agreement with experiment as seen e.g. for electron gyromagnetic ratio.

Renormalizability has become an essential criterion for a quantum field theory to be considered as a viable one. All the theories describing fundamental interactions, except gravitation, whose quantum counterpart is only conjectural and presently under very active research, are renormalizable theories.

## Nonconvergence of series

An argument by Freeman Dyson shows that the radius of convergence of the perturbation series in QED is zero. The basic argument goes as follows: if the coupling constant were negative, this would be equivalent to the Coulomb force constant being negative. This would "reverse" the electromagnetic interaction so that *like* charges would *attract* and *unlike* charges would *repel*. This would render the vacuum unstable against decay into a cluster of electrons on one side of the universe and a cluster of positrons on the other side of the universe. Because the theory is "sick" for any negative value of the coupling constant, the series does not converge but is at best an asymptotic series.

From a modern perspective, we say that QED is not well defined as a quantum field theory to arbitrarily high energy. The coupling constant runs to infinity at finite energy, signalling a Landau pole. The problem is essentially that QED appears to suffer from quantum triviality issues. This is one of the motivations for embedding QED within a Grand Unified Theory.

## Electrodynamics in curved spacetime

This theory can be extended, at least as a classical field theory, to curved spacetime. This arises similarly to the flat spacetime case, from coupling a free electromagnetic theory to a free fermion theory and including an interaction which promotes the partial derivative in the fermion theory to a gauge-covariant derivative.
