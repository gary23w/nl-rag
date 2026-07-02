---
title: "Wave function collapse"
source: https://en.wikipedia.org/wiki/Wave_function_collapse
domain: wave-function-collapse
license: CC-BY-SA-4.0
tags: wave function collapse, model synthesis, constraint-based generation, tile constraint solver
fetched: 2026-07-02
---

# Wave function collapse

In various interpretations of quantum mechanics, **wave function collapse**, also called **reduction of the state vector**, occurs when a wave function—initially in a superposition of several eigenstates—reduces to a single eigenstate due to interaction with the external world. This interaction is called an *observation* and is the essence of a measurement in quantum mechanics, which connects the wave function with classical observables such as position and momentum. Collapse is one of the two processes by which quantum systems evolve in time; the other is the continuous evolution governed by the Schrödinger equation.

In the Copenhagen interpretation, wave function collapse connects quantum to classical models, with a special role for the observer. By contrast, objective-collapse proposes an origin in physical processes. In the many-worlds interpretation, collapse does not exist; all wave function outcomes occur while quantum decoherence accounts for the appearance of collapse.

Historically, Werner Heisenberg was the first to use the idea of wave function reduction to explain quantum measurement.

## Mathematical description

In quantum mechanics each measurable physical quantity of a quantum system is called an observable which, for example, could be the position r and the momentum p but also energy E , z components of spin ( $s_{z}$ ), and so on. The observable acts as a linear function on the states of the system; its eigenvectors correspond to the quantum state (i.e. eigenstate) and the eigenvalues to the possible values of the observable. The collection of eigenstates/eigenvalue pairs represent all possible values of the observable. Writing $\phi _{i}$ for an eigenstate and $c_{i}$ for the corresponding observed value, any arbitrary state of the quantum system can be expressed as a vector using bra–ket notation: $|\psi \rangle =\sum _{i}c_{i}|\phi _{i}\rangle .$ The kets $\{|\phi _{i}\rangle \}$ specify the different available quantum "alternatives", i.e., particular quantum states.

The wave function is a specific representation of a quantum state. Wave functions can therefore always be expressed as eigenstates of an observable though the converse is not necessarily true.

### Collapse

To account for the experimental result that repeated measurements of a quantum system give the same results, the theory postulates a "collapse" or "reduction of the state vector" upon observation, abruptly converting an arbitrary state into a single component eigenstate of the observable:

$|\psi \rangle =\sum _{i}c_{i}|\phi _{i}\rangle \mapsto |\psi '\rangle =|\phi _{i}\rangle .$

where the arrow represents a measurement of the observable corresponding to the $\phi$ basis. For any single event, only one eigenvalue is measured, chosen randomly from among the possible values.

### Meaning of the expansion coefficients

The complex coefficients $\{c_{i}\}$ in the expansion of a quantum state in terms of eigenstates $\{|\phi _{i}\rangle \}$ , $|\psi \rangle =\sum _{i}c_{i}|\phi _{i}\rangle .$ can be written as an (complex) overlap of the corresponding eigenstate and the quantum state: $c_{i}=\langle \phi _{i}|\psi \rangle .$ They are called the probability amplitudes. The square modulus $|c_{i}|^{2}$ is the probability that a measurement of the observable yields the eigenstate $|\phi _{i}\rangle$ . The sum of the probability over all possible outcomes must be one:

$\langle \psi |\psi \rangle =\sum _{i}|c_{i}|^{2}=1.$

As examples, individual counts in a double slit experiment with electrons appear at random locations on the detector; after many counts are summed the distribution shows a wave interference pattern. In a Stern-Gerlach experiment with silver atoms, each particle appears in one of two areas unpredictably, but the final conclusion has equal numbers of events in each area.

This statistical aspect of quantum measurements differs fundamentally from classical mechanics. In quantum mechanics the only information we have about a system is its wave function and measurements of its wave function can only give statistical information.

## Terminology

The two terms "reduction of the state vector" (or "state reduction" for short) and "wave function collapse" are used to describe the same concept. A quantum state is a mathematical description of a quantum system; a quantum state vector uses Hilbert space vectors for the description. Reduction of the state vector replaces the full state vector with a single eigenstate of the observable.

The term "wave function" is typically used for a different mathematical representation of the quantum state, one that uses spatial coordinates also called the "position representation". When the wave function representation is used, the "reduction" is called "wave function collapse".

## The measurement problem

The Schrödinger equation describes quantum systems but does not describe their measurement. Solutions to the equation include all possible observable values for measurements, but measurements only result in one definite outcome. This difference is called the measurement problem of quantum mechanics. To predict measurement outcomes from quantum solutions, the orthodox interpretation of quantum theory postulates wave function collapse and uses the Born rule to compute the probable outcomes. Despite the widespread quantitative success of these postulates scientists remain dissatisfied and have sought more detailed physical models. Rather than suspending the Schrödinger equation during the process of measurement, the measurement apparatus should be included and governed by the laws of quantum mechanics.

## Physical approaches to collapse

Quantum theory offers no dynamical description of the "collapse" of the wave function. Viewed as a statistical theory, no description is expected. As Fuchs and Peres put it, "collapse is something that happens in our description of the system, not to the system itself".

Various interpretations of quantum mechanics attempt to provide a physical model for collapse. Three treatments of collapse can be found among the common interpretations. The first group includes hidden-variable theories like de Broglie–Bohm theory; here random outcomes only result from unknown values of hidden variables. Results from tests of Bell's theorem shows that these variables would need to be non-local. The second group models measurement as quantum entanglement between the quantum state and the measurement apparatus. This results in a simulation of classical statistics called quantum decoherence. This group includes the many-worlds interpretation and consistent histories models. The third group postulates additional, but as yet undetected, physical basis for the randomness; this group includes for example the objective-collapse interpretations. While models in all groups have contributed to better understanding of quantum theory, no alternative explanation for individual events has emerged as more useful than collapse followed by statistical prediction with the Born rule.

The significance ascribed to the wave function varies from interpretation to interpretation and even within an interpretation (such as the Copenhagen interpretation). If the wave function merely encodes an observer's knowledge of the universe, then the wave function collapse corresponds to the receipt of new information. This is somewhat analogous to the situation in classical physics, except that the classical "wave function" does not necessarily obey a wave equation. If the wave function is physically real, in some sense and to some extent, then the collapse of the wave function is also seen as a real process, to the same extent.

### Quantum decoherence

Quantum decoherence explains why a system interacting with an environment transitions from being a pure state, exhibiting superpositions, to a mixed state, an incoherent combination of classical alternatives. This transition is fundamentally reversible, as the combined state of system and environment is still pure, but for all practical purposes irreversible in the same sense as in the second law of thermodynamics: the environment is a very large and complex quantum system, and it is not feasible to reverse their interaction. Decoherence is thus very important for explaining the classical limit of quantum mechanics, but cannot explain wave function collapse, as all classical alternatives are still present in the mixed state, and wave function collapse selects only one of them.

The form of decoherence known as environment-induced superselection proposes that when a quantum system interacts with the environment, the superpositions *apparently* reduce to mixtures of classical alternatives. The combined wave function of the system and environment continue to obey the Schrödinger equation throughout this *apparent* collapse. More importantly, this is not enough to explain *actual* wave function collapse, as decoherence does not reduce it to a single eigenstate.

## History

The concept of wavefunction collapse was introduced by Werner Heisenberg in his 1927 paper on the uncertainty principle, "Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik", and incorporated into the mathematical formulation of quantum mechanics by John von Neumann, in his 1932 treatise *Mathematische Grundlagen der Quantenmechanik*. Heisenberg did not try to specify exactly what the collapse of the wavefunction meant. However, he emphasized that it should not be understood as a physical process. Niels Bohr never mentions wave function collapse in his published work, but he repeatedly cautioned that we must give up a "pictorial representation". Despite the differences between Bohr and Heisenberg, their views are often grouped together as the "Copenhagen interpretation", of which wave function collapse is regarded as a key feature.

John von Neumann's influential 1932 work *Mathematical Foundations of Quantum Mechanics* took a more formal approach, developing an "ideal" measurement scheme that postulated that there were two processes of wave function change:

1. The probabilistic, non-unitary, non-local, discontinuous change brought about by observation and measurement (state reduction or collapse).
2. The deterministic, unitary, continuous time evolution of an isolated system that obeys the Schrödinger equation.

In 1957 Hugh Everett III proposed a model of quantum mechanics that dropped von Neumann's first postulate. Everett observed that the measurement apparatus was also a quantum system and its quantum interaction with the system under observation should determine the results. He proposed that the discontinuous change is instead a splitting of a wave function representing the universe. While Everett's approach rekindled interest in foundational quantum mechanics, it left core issues unresolved. Two key issues relate to origin of the observed classical results: what causes quantum systems to appear classical and to resolve with the observed probabilities of the Born rule.

Beginning in 1970 H. Dieter Zeh sought a detailed quantum decoherence model for the discontinuous change without postulating collapse. Further work by Wojciech H. Zurek in 1980 lead eventually to a large number of papers on many aspects of the concept. Decoherence assumes that every quantum system interacts quantum mechanically with its environment and such interaction is not separable from the system, a concept called an "open system". Decoherence has been shown to work very quickly and within a minimal environment, but as yet it has not succeeded in a providing a detailed model replacing the collapse postulate of orthodox quantum mechanics.

By explicitly dealing with the interaction of object and measuring instrument, von Neumann described a quantum mechanical measurement scheme consistent with wave function collapse. However, he did not prove the *necessity* of such a collapse. Von Neumann's projection postulate was conceived based on experimental evidence available during the 1930s, in particular Compton scattering. Later work refined the notion of measurements into the more easily discussed *first kind*, that will give the same value when immediately repeated, and the *second kind* that give different values when repeated.
