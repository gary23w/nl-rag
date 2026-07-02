---
title: "Quantum computing (part 2/2)"
source: https://en.wikipedia.org/wiki/Quantum_computing
domain: post-quantum-cryptography
license: CC-BY-SA-4.0
tags: post quantum cryptography, quantum resistant algorithm, shor algorithm threat, nist pqc standardization, quantum safe encryption
fetched: 2026-07-02
part: 2/2
---

## Engineering

As of 2023, classical computers outperform quantum computers for all real-world applications. While current quantum computers may speed up solutions to particular mathematical problems, they give no computational advantage for practical tasks. Scientists and engineers are exploring multiple technologies for quantum computing hardware and hope to develop scalable quantum architectures, but serious obstacles remain. In practice, improvements in qubit counts alone are not enough, because error rates, connectivity, and data movement also affect whether an end-to-end application can outperform classical methods.

### Challenges

There are a number of technical challenges in building a large-scale quantum computer. Physicist David DiVincenzo has listed these requirements for a practical quantum computer:

- Physically scalable to increase the number of qubits
- Qubits that can be initialized to arbitrary values
- Quantum gates that are faster than decoherence time
- Universal gate set
- Qubits that can be read easily.

The control of multi-qubit systems requires the generation and coordination of a large number of electrical signals with tight and deterministic timing resolution. This has led to the development of quantum controllers that enable interfacing with the qubits. Scaling these systems to support a growing number of qubits is an additional challenge.

The theoretical potential for large-scale quantum computers to eventually break widely used public-key encryption schemes has prompted significant motivated changes in global cybersecurity strategies. In response to this future challenge, organizations, including the National Institute of Standards and Technology (NIST), have initiated detailed standardization processes for post-quantum cryptography. These global efforts are designed to develop, evaluate, and deploy cryptographic algorithms that remain safe against both quantum and classical computer attacks, well before fully fault-tolerant quantum systems become available.

#### Coolant

Sourcing parts for quantum computers is also very difficult. Superconducting quantum computers, like those constructed by Google and IBM, need helium-3, a nuclear research byproduct, and special superconducting cables made only by the Japanese company Coax Co. On 27 January 2026, the US DARPA agency made a call for proposals for a quantum computing coolant below 1 kelvin, which does not use helium-3. In February 2026, the Chinese Academy of Sciences announced the testing of a rare-earth alloy, EuCo2Al9, which could fill a similar role.

#### Decoherence

One of the greatest challenges involved in constructing quantum computers is controlling or removing quantum decoherence. This usually means isolating the system from its environment, as interactions with the external world cause the system to decohere. However, other sources of decoherence also exist. Examples include the quantum gates, the lattice vibrations, and the background thermonuclear spin of the physical system used to implement the qubits. Decoherence is irreversible, as it is effectively non-unitary, and is usually something that should be highly controlled, if not avoided. Decoherence times for candidate systems in particular, the transverse relaxation time *T*2 (for NMR and MRI technology, also called the *dephasing time*), typically range between nanoseconds and seconds at low temperatures. Currently, some quantum computers require their qubits to be cooled to 20 millikelvin (usually using a dilution refrigerator) in order to prevent significant decoherence. A 2020 study argues that ionizing radiation such as cosmic rays can nevertheless cause certain systems to decohere within milliseconds.

As a result, time-consuming tasks may render some quantum algorithms inoperable, as attempting to maintain the state of qubits for a long enough duration will eventually corrupt the superpositions.

These issues are more difficult for optical approaches as the timescales are orders of magnitude shorter, and an often-cited approach to overcoming them is optical pulse shaping. Error rates are typically proportional to the ratio of operating time to decoherence time; hence, any operation must be completed much more quickly than the decoherence time.

As described by the threshold theorem, if the error rate is small enough, it is thought to be possible to use quantum error correction to suppress errors and decoherence. This allows the total calculation time to be longer than the decoherence time if the error correction scheme can correct errors faster than decoherence introduces them. An often-cited figure for the required error rate in each gate for fault-tolerant computation is 10−3, assuming the noise is depolarizing.

Meeting this scalability condition is possible for a wide range of systems. However, the use of error correction brings with it the cost of a greatly increased number of required qubits. The number required to factor integers using Shor's algorithm is still polynomial, and thought to be between L and *L*2, where L is the number of binary digits in the number to be factored; error correction algorithms would inflate this figure by an additional factor of L. For a 1000-bit number, this implies a need for about 104 bits without error correction. With error correction, the figure would rise to about 107 bits. Computation time is about *L*2 or about 107 steps and at 1 MHz, about 10 seconds. However, the encoding and error-correction overheads increase the size of a real fault-tolerant quantum computer by several orders of magnitude. Careful estimates show that at least 3 million physical qubits would factor 2,048-bit integer in 5 months on a fully error-corrected trapped-ion quantum computer. In terms of the number of physical qubits, to date, this remains the lowest estimate for practically useful integer factorization problem sizing 1,024-bit or larger.

One approach to overcoming errors combines low-density parity-check code with cat qubits that have intrinsic bit-flip error suppression. Implementing 100 logical qubits with 768 cat qubits could reduce the error rate to one part in 108 per cycle per bit.

Another approach to the stability-decoherence problem is to create a topological quantum computer with anyons, quasi-particles used as threads, and relying on braid theory to form stable logic gates. Non-Abelian anyons can, in effect, remember how they have been manipulated, making them potentially useful in quantum computing. As of 2025, Microsoft and other organizations are investing in quasi-particle research.

### Quantum supremacy

Physicist John Preskill coined the term *quantum supremacy* to describe the engineering feat of demonstrating that a programmable quantum device can solve a problem beyond the capabilities of state-of-the-art classical computers. The problem need not be useful, so some view the quantum supremacy test only as a potential future benchmark.

In October 2019, Google AI Quantum, with the help of NASA, became the first to claim to have achieved quantum supremacy by performing calculations on the Sycamore quantum computer more than 3,000,000 times faster than they could be done on Summit, generally considered the world's fastest computer. This claim has been subsequently challenged: IBM has stated that Summit can perform samples much faster than claimed, and researchers have since developed better algorithms for the sampling problem used to claim quantum supremacy, giving substantial reductions to the gap between Sycamore and classical supercomputers and even beating it.

In December 2020, a group at USTC implemented a type of boson sampling on 76 photons with a photonic quantum computer, Jiuzhang, to demonstrate quantum supremacy. The authors claim that a classical contemporary supercomputer would require a computational time of 600 million years to generate the number of samples their quantum processor can generate in 20 seconds.

Claims of quantum supremacy have generated hype around quantum computing, but they are based on contrived benchmark tasks that do not directly imply useful real-world applications. Accordingly, benchmark-level quantum advantage should not be interpreted as proof that quantum computers are already broadly useful across practical computing workloads.

In January 2024, a study published in *Physical Review Letters* provided direct verification of quantum supremacy experiments by computing exact amplitudes for experimentally generated bitstrings using a new-generation Sunway supercomputer, demonstrating a significant leap in simulation capability built on a multiple-amplitude tensor network contraction algorithm.

### Skepticism

Despite high hopes for quantum computing, significant progress in hardware, and optimism about future applications, a 2023 Nature spotlight article summarized current quantum computers as being "For now, [good for] absolutely nothing". The article elaborated that quantum computers are yet to be more useful or efficient than conventional computers in any case, though it also argued that, in the long term, such computers are likely to be useful. A 2023 Communications of the ACM article found that current quantum computing algorithms are "insufficient for practical quantum advantage without significant improvements across the software/hardware stack". It argues that the most promising candidates for achieving speedup with quantum computers are "small-data problems", for example, in chemistry and materials science. However, the article also concludes that a large range of the potential applications it considered, such as machine learning, "will not achieve quantum advantage with current quantum algorithms in the foreseeable future", and it identified I/O constraints that make speedup unlikely for "big data problems, unstructured linear systems, and database search based on Grover's algorithm".

This state of affairs can be traced to several current and long-term considerations.

- Conventional computer hardware and algorithms are not only optimized for practical tasks, but are still improving rapidly, particularly GPU accelerators.
- Current quantum computing hardware generates only a limited amount of entanglement before getting overwhelmed by noise.
- Quantum algorithms provide speedup over conventional algorithms only for some tasks, and matching these tasks with practical applications proved challenging. Some promising tasks and applications require resources far beyond those available today. In particular, processing large amounts of non-quantum data is a challenge for quantum computers.
- Some promising algorithms have been "dequantized", i.e., their non-quantum analogues with similar complexity have been found.
- If quantum error correction is used to scale quantum computers to practical applications, its overhead may undermine the speedup offered by many quantum algorithms.
- Complexity analysis of algorithms sometimes makes abstract assumptions that do not hold in applications. For example, input data may not already be available encoded in quantum states, and "oracle functions" used in Grover's algorithm often have internal structure that can be exploited for faster algorithms.

In particular, building computers with large numbers of qubits may be futile if those qubits are not connected well enough and cannot maintain a sufficiently high degree of entanglement for a long time. When trying to outperform conventional computers, quantum computing researchers often look for new tasks that can be solved on quantum computers, but this leaves the possibility that efficient non-quantum techniques will be developed in response, as seen for Quantum supremacy demonstrations. Therefore, it is desirable to prove lower bounds on the complexity of best possible non-quantum algorithms (which may be unknown) and show that some quantum algorithms asymptotically improve upon those bounds.

Bill Unruh doubted the practicality of quantum computers in a paper published in 1994. Paul Davies argued that a 400-qubit computer would even come into conflict with the cosmological information bound implied by the holographic principle. Skeptics like Gil Kalai doubt that quantum supremacy will ever be achieved. Physicist Mikhail Dyakonov has expressed skepticism of quantum computing as follows:

"So the number of continuous parameters describing the state of such a useful quantum computer at any given moment must be... about

10

300

... Could we ever learn to control the more than

10

300

continuously variable parameters defining the quantum state of such a system? My answer is simple.

No, never.

"

### Physical realizations

A practical quantum computer must use a physical system as a programmable quantum register. Researchers are exploring several technologies as candidates for reliable qubit implementations. Superconductors and trapped ions are some of the most developed proposals, but experimentalists are considering other hardware possibilities as well. For example, topological quantum computer approaches are being explored for more fault-tolerance computing systems.

The first quantum logic gates were implemented with trapped ions and prototype general-purpose machines with up to 20 qubits have been realized. However, the technology behind these devices combines complex vacuum equipment, lasers, and microwave and radio frequency equipment, making full-scale processors difficult to integrate with standard computing equipment. Moreover, the trapped ion system itself has engineering challenges to overcome.

The largest commercial systems are based on superconductor devices and have scaled to 2000 qubits. However, the error rates for larger machines have been on the order of 5%. Technologically, these devices are all cryogenic and scaling to large numbers of qubits requires wafer-scale integration, a serious engineering challenge by itself.

In addition to cryogenic platforms, room-temperature approaches to spin–photon interfaces have been experimentally demonstrated. In 2025, researchers at Stanford University realized a nanoscale device in which a thin layer of molybdenum diselenide is integrated on a nanostructured silicon substrate, enabling a spin–photon interface that operates at ambient conditions using structured "twisted" light to couple electronic and photonic degrees of freedom. Such room-temperature, chip-integrated spin–photon interfaces are being investigated as potential building blocks for heterogeneous quantum networks that combine different qubit modalities and reduce reliance on large cryogenic infrastructures.


## Theory

### Computability

Any computational problem solvable by a classical computer is also solvable by a quantum computer. Intuitively, this is because it is believed that all physical phenomena, including the operation of classical computers, can be described using quantum mechanics, which underlies the operation of quantum computers.

Conversely, any problem solvable by a quantum computer is also solvable by a classical computer. It is possible to simulate both quantum and classical computers manually with just some paper and a pen, if given enough time. More formally, any quantum computer can be simulated by a Turing machine. In other words, quantum computers provide no additional power over classical computers in terms of computability. This means that quantum computers cannot solve undecidable problems like the halting problem, and the existence of quantum computers does not disprove the Church–Turing thesis.

### Complexity

While quantum computers cannot solve any problems that classical computers cannot already solve, it is suspected that they can solve certain problems faster than classical computers. For instance, it is known that quantum computers can efficiently factor integers, while this is not believed to be the case for classical computers.

The class of problems that can be efficiently solved by a quantum computer with bounded error is called BQP, for "bounded error, quantum, polynomial time". More formally, BQP is the class of problems that can be solved by a polynomial-time quantum Turing machine with an error probability of at most 1/3. As a class of probabilistic problems, BQP is the quantum counterpart to BPP ("bounded error, probabilistic, polynomial time"), the class of problems that can be solved by polynomial-time probabilistic Turing machines with bounded error. It is known that ${\mathsf {BPP\subseteq BQP}}$ but there is no proof ${\mathsf {BQP\neq BPP}}$ , which intuitively would mean that quantum computers are more powerful than classical computers in terms of time complexity.

The exact relationship of BQP to P, NP, and PSPACE is not known. However, it is known that ${\mathsf {P\subseteq BQP\subseteq PSPACE}}$ ; that is, all problems that can be efficiently solved by a deterministic classical computer can also be efficiently solved by a quantum computer, and all problems that can be efficiently solved by a quantum computer can also be solved by a deterministic classical computer with polynomial space resources. It is further suspected that BQP is a strict superset of P, meaning that there exist problems that are efficiently solvable by quantum computers that are not efficiently solvable by deterministic classical computers. For instance, integer factorization and the discrete logarithm problem are known to be in BQP and are suspected to be outside of P. On the relationship of BQP to NP, little is known beyond the fact that some NP problems that are believed not to be in P are also in BQP (integer factorization and the discrete logarithm problem are both in NP, for example). It is suspected that ${\mathsf {NP\nsubseteq BQP}}$ ; that is, it is believed that there are efficiently checkable problems that are not efficiently solvable by a quantum computer. As a direct consequence of this belief, it is also suspected that BQP is disjoint from the class of NP-complete problems (if an NP-complete problem were in BQP, then it would follow from NP-hardness that all problems in NP are in BQP).


## List of quantum computers

- Hanyuan-1 — 100-qubit neutral atom quantum computer from the Chinese Academy of Sciences in China.
- IBM Quantum System One — IBM superconducting quantum-computing system introduced in 2019.
- IBM Quantum System Two — modular superconducting system using IBM Heron processors.
- Jiuzhang — photonic quantum-computing prototype for Gaussian boson sampling.
- QpiAI-Indus — 25-qubit superconducting quantum computer from QpiAI in India.

### Types of quantum computers

- Cat qubit quantum computer — proposed approach based on cat-state qubits.
- Kane quantum computer — proposed silicon-based nuclear spin quantum-computer architecture.
- Linear optical quantum computing — photonic model using photons and linear optical elements.
- Neutral atom quantum computer — approach using neutral atoms trapped and controlled with optical techniques.
- Nuclear magnetic resonance quantum computer — approach using nuclear magnetic resonance and molecular nuclear-spin states.
- Spin qubit quantum computer — semiconductor architecture using spin states as qubits.
- Superconducting quantum computing — approach using superconducting electronic circuits.
- Topological quantum computer — proposed approach using topological states such as anyons.
- Trapped-ion quantum computer — approach using trapped charged atoms as qubits.
