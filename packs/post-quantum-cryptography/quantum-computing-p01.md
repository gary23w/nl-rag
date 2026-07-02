---
title: "Quantum computing (part 1/2)"
source: https://en.wikipedia.org/wiki/Quantum_computing
domain: post-quantum-cryptography
license: CC-BY-SA-4.0
tags: post quantum cryptography, quantum resistant algorithm, shor algorithm threat, nist pqc standardization, quantum safe encryption
fetched: 2026-07-02
part: 1/2
---

# Quantum computing

A **quantum computer** is a real or theoretical computer that exploits quantum phenomena like superposition and entanglement in an essential way. It is widely believed that a quantum computer could perform *some* calculations exponentially faster than any classical computer. For example, a large-scale quantum computer could break some widely used encryption schemes and aid physicists in performing physical simulations. However, current hardware implementations of quantum computation are largely experimental and only suitable for specialized tasks.

The basic unit of information in quantum computing, the qubit (or "quantum bit"), serves the same function as the bit in ordinary or "classical" computing. However, unlike a classical bit, which can be in one of two states (a binary), a qubit can exist in a linear combination of two states known as a quantum superposition. The result of measuring a qubit is one of the two states given by a probabilistic rule. If a quantum computer manipulates the qubit in a particular way, wave interference effects amplify the probability of the desired measurement result. The design of quantum algorithms involves creating procedures that allow a quantum computer to perform this amplification.

Quantum computers are not yet practical for real-world applications. Physically engineering high-quality qubits has proven to be challenging. If a physical qubit is not sufficiently isolated from its environment, it suffers from quantum decoherence, introducing noise into calculations. National governments have invested heavily in experimental research aimed at developing scalable qubits with longer coherence times and lower error rates. Example implementations include superconductors (which isolate an electrical current by eliminating electrical resistance) and ion traps (which confine a single atomic particle using electromagnetic fields). Researchers have claimed, and are widely believed to be correct, that certain quantum devices can outperform classical computers on narrowly defined tasks, a milestone referred to as quantum advantage or quantum supremacy. These tasks are not necessarily useful for real-world applications. As a result, current demonstrations are best understood as scientific milestones rather than evidence of broad near-term deployment. In December 2024, Google's Willow chip achieved below-threshold error correction, a milestone 30 years in the making, while global government investment in quantum computing reached $10 billion by April 2025.


## History

For many years, the fields of quantum mechanics and computer science formed distinct academic communities. Modern quantum theory was developed in the 1920s to explain perplexing physical phenomena observed at atomic scales, and digital computers emerged in the following decades to replace human computers for tedious calculations. Both disciplines had practical applications during World War II; computers played a major role in wartime cryptography, and quantum physics was essential for nuclear physics used in the Manhattan Project.

As physicists applied quantum mechanical models to computational problems and swapped digital bits for qubits, the fields of quantum mechanics and computer science began to converge. In 1980, Paul Benioff introduced the quantum Turing machine, which uses quantum theory to describe a simplified computer. When digital computers became faster, physicists faced an exponential increase in overhead when simulating quantum dynamics, prompting Yuri Manin and Richard Feynman to independently suggest that hardware based on quantum phenomena might be more efficient for computer simulation. In a 1984 paper, Charles Bennett and Gilles Brassard applied quantum theory to cryptography protocols and demonstrated that quantum key distribution could enhance information security.

Quantum algorithms then emerged for solving oracle problems, such as Deutsch's algorithm in 1985, the Bernstein–Vazirani algorithm in 1993, and Simon's algorithm in 1994. These algorithms did not solve practical problems, but demonstrated mathematically that one could obtain more information by querying a black box with a quantum state in superposition, sometimes referred to as *quantum parallelism*.

Peter Shor built on these results with his 1994 algorithm for breaking the widely used RSA and Diffie–Hellman encryption protocols, which drew significant attention to the field of quantum computing. In 1996, Grover's algorithm established a quantum speedup for the widely applicable unstructured search problem. The same year, Seth Lloyd proved that quantum computers could simulate quantum systems without the exponential overhead present in classical simulations, validating Feynman's 1982 conjecture.

Over the years, experimentalists have constructed small-scale quantum computers using trapped ions and superconductors. In 1998, a two-qubit quantum computer demonstrated the feasibility of the technology, and subsequent experiments have increased the number of qubits and reduced error rates.

In 2019, Google AI and NASA announced that they had achieved quantum supremacy with a 54-qubit machine, performing a computation that classical supercomputers would take an estimated 10,000 years to complete—a claim subsequently disputed by IBM, which argued the calculation could be done in approximately 2.5 days on its Summit supercomputer with optimized algorithms, sparking a debate over the precise threshold for this milestone.

Recent milestones in quantum computing have increasingly focused on controlling decoherence through quantum error correction. In 2024, researchers demonstrated theoretical and practical approaches for high threshold, low-overhead fault-tolerant quantum memory. These developments represent a critical step toward scaling systems beyond the noisy intermediate-scale quantum (NISQ) era into reliable, fault-tolerant computing architectures, though large-scale physical implementation remains an ongoing engineering challenge.


## Quantum information processing

Computer engineers typically describe a modern computer's operation in terms of classical electrodynamics. In these "classical" computers, some components (such as semiconductors and random number generators) may rely on quantum behavior; however, because they are not isolated from their environment, any quantum information eventually quickly decoheres. While programmers may depend on probability theory when designing a randomized algorithm, quantum-mechanical notions such as superposition and wave interference are largely irrelevant in program analysis.

The "classical" in *classical computation* thus refers to the computational model, not to whether the microscopic physics of the hardware is ultimately quantum-mechanical. A conventional digital computer can be described by classical states and transition rules: memory stores bits, while logic elements transform one configuration of bits into another. This computational behavior is not tied to electronics, and can be abstracted through the idea of a Turing machine, a mechanical device that performs deterministic transformations on a finite state. In principle, the same classical transition rules can be implemented by some entirely classical mechanical device, possibly with a fixed slow-down in physical time. If a classical computation uses randomness, this can be modeled as access to random classical bits rather than as coherent quantum information. A quantum computer, by contrast, uses coherent quantum states, so that superposition, relative phase, and interference are part of the computation itself, and has no classical counterpart.

Quantum programs instead rely on precise control of coherent quantum systems. Physicists describe these systems mathematically using linear algebra. Complex numbers model probability amplitudes, vectors model quantum states, and matrices model the operations that can be performed on these states. Programming a quantum computer is then a matter of composing operations in such a way that the resulting program computes a useful result in theory and is implementable in practice.

Physicist Charlie Bennett noted that since classical computers are composed of quantum atoms, one might study them from the opposite direction:

> A classical computer is a quantum computer ... so we shouldn't be asking about "where do quantum speedups come from?" We should say, "Well, all computers are quantum. ... Where do classical slowdowns come from?"

### Quantum information

Just as the bit is the basic concept of classical information theory, the *qubit* is the fundamental unit of quantum information. The same term *qubit* is used to refer to an abstract mathematical model and to any physical system that is represented by that model. A classical bit, by definition, exists in either of two physical states, which can be denoted 0 and 1. A qubit is also described by a state, and two states, often written $|0\rangle$ and $|1\rangle$ , serve as the quantum counterparts of the classical states 0 and 1. However, the quantum states $|0\rangle$ and $|1\rangle$ belong to a vector space, meaning that they can be multiplied by constants and added together, and the result is again a valid quantum state. Such a combination is known as a *superposition* of $|0\rangle$ and $|1\rangle$ .

A two-dimensional vector mathematically represents a qubit state. Physicists typically use bra–ket notation for quantum mechanical linear algebra, writing $|\psi \rangle$ 'ket psi' for a vector labeled $\psi$ . Because a qubit is a two-state system, any qubit state takes the form $\alpha |0\rangle +\beta |1\rangle$ , where $|0\rangle$ and $|1\rangle$ are the standard *basis states*, and $\alpha$ and $\beta$ are the *probability amplitudes,* which are in general complex numbers. If either $\alpha$ or $\beta$ is zero, the qubit is effectively a classical bit; when both are nonzero, the qubit is in superposition. Such a quantum state vector behaves similarly to a (classical) probability vector, with one key difference: unlike probabilities, probability *amplitudes* are not necessarily positive numbers. Negative amplitudes allow for destructive wave interference.

When a qubit is measured in the standard basis, the result is a classical bit. The Born rule describes the norm-squared correspondence between amplitudes and probabilities—when measuring a qubit $\alpha |0\rangle +\beta |1\rangle$ , the state collapses to $|0\rangle$ with probability $|\alpha |^{2}$ , or to $|1\rangle$ with probability $|\beta |^{2}$ . Any valid qubit state has coefficients $\alpha$ and $\beta$ such that $|\alpha |^{2}+|\beta |^{2}=1$ . As an example, measuring the qubit $1/{\sqrt {2}}|0\rangle +1/{\sqrt {2}}|1\rangle$ would produce either $|0\rangle$ or $|1\rangle$ with equal probability.

Two particularly important superposition states are the plus state $|+\rangle =1/{\sqrt {2}}|0\rangle +1/{\sqrt {2}}|1\rangle$ and the minus state $|-\rangle =1/{\sqrt {2}}|0\rangle -1/{\sqrt {2}}|1\rangle$ . While both yield outcomes 0 and 1 with equal probability upon standard basis measurement, they behave differently under operations such as the Hadamard gate—which maps $|0\rangle \leftrightarrow |+\rangle$ and $|1\rangle \leftrightarrow |-\rangle$ —demonstrating that relative phase differences carry meaningful quantum information.

Each additional qubit doubles the dimension of the state space. As an example, the vector ⁠1/√2⁠|00⟩ + ⁠1/√2⁠|01⟩ represents a two-qubit state, a tensor product of the qubit |0⟩ with the qubit ⁠1/√2⁠|0⟩ + ⁠1/√2⁠|1⟩. This vector inhabits a four-dimensional vector space spanned by the basis vectors |00⟩, |01⟩, |10⟩, and |11⟩.

In general, the vector space for an n-qubit system is 2*n*-dimensional, and this makes it challenging for a classical computer to simulate a quantum one: representing a 100-qubit system requires storing 2100 classical values.

### Unitary operators

The state of this one-qubit quantum memory can be manipulated by applying quantum logic gates, analogous to how classical memory can be manipulated with classical logic gates. One important gate for both classical and quantum computation is the NOT gate, which can be represented by a matrix $X:={\begin{pmatrix}0&1\\1&0\end{pmatrix}}.$ Mathematically, the application of such a logic gate to a quantum state vector is modeled with matrix multiplication. Thus

$X|0\rangle =|1\rangle$

and

$X|1\rangle =|0\rangle$

.

The mathematics of single-qubit gates can be extended to operate on multi-qubit quantum memories in two important ways. One way is simply to select a qubit and apply that gate to the target qubit while leaving the remainder of the memory unaffected. Another way is to apply the gate to its target only if another part of the memory is in a desired state. These two choices can be illustrated using another example. The possible states of a two-qubit quantum memory are ${\displaystyle |00\rangle$ The controlled NOT (CNOT) gate can then be represented using the following matrix: $\operatorname {CNOT$ As a mathematical consequence of this definition, ${\textstyle \operatorname {CNOT} |00\rangle =|00\rangle }$ , ${\textstyle \operatorname {CNOT} |01\rangle =|01\rangle }$ , ${\textstyle \operatorname {CNOT} |10\rangle =|11\rangle }$ , and ${\textstyle \operatorname {CNOT} |11\rangle =|10\rangle }$ . In other words, the CNOT applies a NOT gate ( ${\textstyle X}$ from before) to the second qubit if and only if the first qubit is in the state ${\textstyle |1\rangle }$ . If the first qubit is ${\textstyle |0\rangle }$ , nothing is done to either qubit.

In summary, quantum computation can be described as a network of quantum logic gates and measurements. However, any measurement can be deferred to the end of quantum computation, though this deferment may come at a computational cost, so most quantum circuits depict a network consisting only of quantum logic gates and no measurements.

### Quantum parallelism

*Quantum parallelism* is the heuristic that quantum computers can be thought of as evaluating a function for multiple input values simultaneously. This can be achieved by preparing a quantum system in a superposition of input states and applying a unitary transformation that encodes the function to be evaluated. The resulting state encodes the function's output values for all input values in the superposition, enabling the simultaneous computation of multiple outputs. This property is key to the speedup of many quantum algorithms. However, "parallelism" in this sense is insufficient to speed up a computation, because the measurement at the end of the computation gives only one value. To be useful, a quantum algorithm must also incorporate some other conceptual ingredient.

### Quantum programming

There are multiple models of computation for quantum computing, distinguished by the basic elements in which the computation is decomposed.

#### Gate array

A quantum gate array decomposes computation into a sequence of few-qubit quantum gates. A quantum computation can be described as a network of quantum logic gates and measurements. However, any measurement can be deferred to the end of quantum computation, though this deferment may come at a computational cost, so most quantum circuits depict a network consisting only of quantum logic gates and no measurements.

Any quantum computation (which is, in the above formalism, any unitary matrix of size $2^{n}\times 2^{n}$ over n qubits) can be represented as a network of quantum logic gates from a fairly small family of gates. A choice of gate family that enables this construction is known as a universal gate set, since a computer that can run such circuits is a universal quantum computer. One common such set includes all single-qubit gates as well as the CNOT gate from above. This means any quantum computation can be performed by executing a sequence of single-qubit gates together with CNOT gates. Though this gate set is infinite, it can be replaced with a finite gate set by appealing to the Solovay-Kitaev theorem. Implementation of Boolean functions using the few-qubit quantum gates is presented here.

#### Measurement-based quantum computing

A measurement-based quantum computer decomposes computation into a sequence of Bell state measurements and single-qubit quantum gates applied to a highly entangled initial state (a cluster state), using a technique called quantum gate teleportation.

#### Adiabatic quantum computing

An adiabatic quantum computer, based on quantum annealing, decomposes computation into a slow continuous transformation of an initial Hamiltonian into a final Hamiltonian, whose ground states contain the solution.

#### Neuromorphic quantum computing

Neuromorphic quantum computing (abbreviated 'n.quantum computing') is an unconventional process of computing that uses neuromorphic computing to perform quantum operations. It was suggested that quantum algorithms, which are algorithms that run on a realistic model of quantum computation, can be computed equally efficiently with neuromorphic quantum computing. Both traditional quantum computing and neuromorphic quantum computing are physics-based unconventional computing approaches to computations and do not follow the von Neumann architecture. They both construct a system (a circuit) that represents the physical problem at hand and then leverage their respective physics properties of the system to seek the "minimum". Neuromorphic quantum computing and quantum computing share similar physical properties during computation.

#### Topological quantum computing

A topological quantum computer decomposes computation into the braiding of anyons in a 2D lattice.

#### Quantum Turing machine

A quantum Turing machine is the quantum analog of a Turing machine. All of these models of computation—quantum circuits, one-way quantum computation, adiabatic quantum computation, and topological quantum computation—have been shown to be equivalent to the quantum Turing machine; given a perfect implementation of one such quantum computer, it can simulate all the others with no more than polynomial overhead. This equivalence need not hold for practical quantum computers, since the overhead of simulation may be too large to be practical.

#### Noisy intermediate-scale quantum computing

The threshold theorem shows how increasing the number of qubits can mitigate errors, yet fully fault-tolerant quantum computing remains "a rather distant dream". According to some researchers, *noisy intermediate-scale quantum* (NISQ) machines may have specialized uses in the near future, but noise in quantum gates limits their reliability. Scientists at Harvard University successfully created "quantum circuits" that correct errors more efficiently than alternative methods, which may potentially remove a major obstacle to practical quantum computers. The Harvard research team was supported by MIT, QuEra Computing, Caltech, and Princeton University and funded by DARPA's Optimization with Noisy Intermediate-Scale Quantum devices (ONISQ) program.

#### Quantum cryptography and cybersecurity

Digital cryptography enables communications to remain private, preventing unauthorized parties from accessing them. Conventional encryption, the obscuring of a message with a key through an algorithm, relies on the algorithm being difficult to reverse. Encryption is also the basis for digital signatures and authentication mechanisms. Quantum computing may be sufficiently more powerful that difficult reversals are feasible, allowing messages relying on conventional encryption to be read.

Quantum cryptography replaces conventional algorithms with computations based on quantum computing. In principle, quantum encryption would be impossible to decode even with a quantum computer. This advantage comes at a significant cost in terms of elaborate infrastructure, while effectively preventing legitimate decoding of messages by governmental security officials.

Ongoing research in quantum and post-quantum cryptography has led to new algorithms for quantum key distribution, initial work on quantum random number generation and to some early technology demonstrations.


## Communication

Quantum cryptography enables new ways to transmit data securely; for example, quantum key distribution uses entangled quantum states to establish secure cryptographic keys. When a sender and receiver exchange quantum states, they can guarantee that an adversary does not intercept the message, as any unauthorized eavesdropper would disturb the delicate quantum system and introduce a detectable change. With appropriate cryptographic protocols, the sender and receiver can thus establish shared private information resistant to eavesdropping.

Modern fiber-optic cables can transmit quantum information over relatively short distances. Ongoing experimental research aims to develop more reliable hardware (such as quantum repeaters), hoping to scale this technology to long-distance quantum networks with end-to-end entanglement. Theoretically, this could enable novel technological applications, such as distributed quantum computing and enhanced quantum sensing.

### Quantum communication protocols

Quantum teleportation is a protocol by which Alice can transmit the quantum state of a qubit to Bob using one shared entangled pair (e-bit) and two classical bits of communication. The state of Alice's qubit is not physically transmitted—instead, it is reconstructed at Bob's end through classically communicated measurement outcomes and local unitary corrections. This demonstrates that quantum communication requires both entanglement and classical communication; neither alone is sufficient. Teleportation cannot be used to transmit information faster than light because the classical bits must travel through normal channels.

Superdense coding is the complementary protocol: using one shared e-bit and sending only one qubit, Alice can transmit two classical bits to Bob. This appears to violate Holevo's theorem—which states that a single qubit can carry at most one bit of classical information—but the shared entanglement circumvents this limit. Superdense coding thus demonstrates that entanglement can effectively double the classical information-carrying capacity of quantum communication.


## Algorithms

Progress in finding quantum algorithms typically focuses on the quantum circuit model, though exceptions like the quantum adiabatic algorithm exist. Quantum algorithms can be roughly categorized by the type of speedup achieved over corresponding classical algorithms.

Quantum algorithms that offer more than a polynomial speedup over the best-known classical algorithm include Shor's algorithm for factoring and the related quantum algorithms for computing discrete logarithms, solving Pell's equation, and, more generally, solving the hidden subgroup problem for abelian finite groups. These algorithms depend on the primitive of the quantum Fourier transform. No mathematical proof has been found that shows that an equally fast classical algorithm cannot be discovered, but evidence suggests that this is unlikely. Certain oracle problems like Simon's problem and the Bernstein–Vazirani problem do give provable speedups, though this is in the quantum query model, which is a restricted model where lower bounds are much easier to prove and don't necessarily translate to speedups for practical problems.

Other problems, including the simulation of quantum physical processes from chemistry and solid-state physics, the approximation of certain Jones polynomials, and the quantum algorithm for linear systems of equations, have quantum algorithms appearing to give super-polynomial speedups and are BQP-complete. Because these problems are BQP-complete, an equally fast classical algorithm for them would imply that "no quantum algorithm" provides a super-polynomial speedup, which is believed to be unlikely.

In addition to these problems, quantum algorithms are being explored for applications in cryptography, optimization, and machine learning, although most of these remain at the research stage and require significant advances in error correction and hardware scalability before practical implementation.

Some quantum algorithms, such as Grover's algorithm and amplitude amplification, give polynomial speedups over corresponding classical algorithms. Though these algorithms give comparably modest quadratic speedup, they are widely applicable and thus give speedups for a wide range of problems. These speed-ups are, however, over the theoretical worst-case of classical algorithms, and concrete real-world speed-ups over algorithms used in practice have not been demonstrated.

### Simulation of quantum systems

Since chemistry and nanotechnology rely on understanding quantum systems, and such systems are impossible to simulate in an efficient manner classically, quantum simulation may be an important application of quantum computing. Recent reviews identify quantum chemistry as one of the most promising application areas for quantum computing, particularly for problems in electronic structure, chemical dynamics, and spectroscopy, while noting that useful implementations remain limited by current hardware. Quantum simulation could also be used to simulate the behavior of atoms and particles at unusual conditions such as the reactions inside a collider. In June 2023, IBM computer scientists reported that a quantum computer produced better results for a physics problem than a conventional supercomputer.

About 2% of the annual global energy output is used for nitrogen fixation to produce ammonia for the Haber process in the agricultural fertiliser industry (even though naturally occurring organisms also produce ammonia). Quantum simulations might be used to understand this process and increase the energy efficiency of production. It is expected that an early use of quantum computing will be modeling that improves the efficiency of the Haber–Bosch process by the mid-2020s although some have predicted it will take longer.

### Post-quantum cryptography

A notable application of quantum computing is in attacking cryptographic systems that are currently in use. Integer factorization, which underpins the security of public key cryptographic systems, is believed to be computationally infeasible on a classical computer for large integers if they are the product of a few prime numbers (e.g., the product of two 300-digit primes). By contrast, a quantum computer could solve this problem exponentially faster using Shor's algorithm to factor the integer. This ability would allow a quantum computer to break many of the cryptographic systems in use today, in the sense that there would be a polynomial time (in the number of digits of the integer) algorithm for solving the problem. In particular, most of the popular public key ciphers are based on the difficulty of factoring integers or the discrete logarithm problem, both of which can be solved by Shor's algorithm. In particular, the RSA, Diffie–Hellman, and elliptic curve Diffie–Hellman algorithms could be broken. These are used to protect secure Web pages, encrypted email, and many other types of data. Breaking these would have significant ramifications for electronic privacy and security.

Identifying cryptographic systems that may be secure against quantum algorithms is an actively researched topic under the field of *post-quantum cryptography*. Some public-key algorithms are based on problems other than the integer factorization and discrete logarithm problems to which Shor's algorithm applies, such as the McEliece cryptosystem, which relies on a hard problem in coding theory. Lattice-based cryptosystems are also not known to be broken by quantum computers, and finding a polynomial time algorithm for solving the dihedral hidden subgroup problem, which would break many lattice-based cryptosystems, is a well-studied open problem. It has been shown that applying Grover's algorithm to break a symmetric (secret-key) algorithm by brute force requires time equal to roughly 2*n*/2 invocations of the underlying cryptographic algorithm, compared with roughly 2*n* in the classical case, meaning that symmetric key lengths are effectively halved: AES-256 would have comparable security against an attack using Grover's algorithm to that AES-128 has against classical brute-force search (see *Key size*).

The most well-known example of a problem that allows for a polynomial quantum speedup is *unstructured search*, which involves finding a marked item out of a list of n items in a database. This can be solved by Grover's algorithm using $O({\sqrt {n}})$ queries to the database, quadratically fewer than the $\Omega (n)$ queries required for classical algorithms. In this case, the advantage is not only provable but also optimal: it has been shown that Grover's algorithm gives the maximal possible probability of finding the desired element for any number of oracle lookups. Many examples of provable quantum speedups for query problems are based on Grover's algorithm, including Brassard, Høyer, and Tapp's algorithm for finding collisions in two-to-one functions, and Farhi, Goldstone, and Gutmann's algorithm for evaluating NAND trees.

Problems that can be efficiently addressed with Grover's algorithm have the following properties:

1. There is no searchable structure in the collection of possible answers,
2. The number of possible answers to check is the same as the number of inputs to the algorithm, and
3. There exists a Boolean function that evaluates each input and determines whether it is the correct answer.

For problems with all these properties, the running time of Grover's algorithm on a quantum computer scales as the square root of the number of inputs (or elements in the database), as opposed to the linear scaling of classical algorithms. A general class of problems to which Grover's algorithm can be applied is a Boolean satisfiability problem, where the *database* through which the algorithm iterates is that of all possible answers. An example and possible application of this is a password cracker that attempts to guess a password. Breaking symmetric ciphers with this algorithm is of interest to government agencies.

### Quantum annealing

Quantum annealing uses the adiabatic theorem to perform calculations. A system is placed in the ground state for a simple Hamiltonian, which slowly evolves to a more complicated Hamiltonian whose ground state represents the solution to the problem in question. The adiabatic theorem states that if the evolution is slow enough, the system will stay in its ground state at all times through the process. Quantum annealing can solve Ising models and the (computationally equivalent) QUBO problem, which in turn can be used to encode a wide range of combinatorial optimization problems. Adiabatic optimization may be helpful for solving computational biology problems.

### Machine learning

Since quantum computers can produce outputs that classical computers cannot produce efficiently, and since quantum computation is fundamentally linear algebraic, some express hope in developing quantum algorithms that can speed up machine learning tasks. However, review literature notes that many proposed quantum machine-learning advantages rely on assumptions about efficient data encoding or continued access to quantum hardware, and have not yet translated into broad practical end-to-end advantage on current devices. For example, the HHL Algorithm, named after its discoverers Harrow, Hassidim, and Lloyd, is believed to provide speedup over classical counterparts. Some research groups have recently explored the use of quantum annealing hardware for training Boltzmann machines and deep neural networks.

Deep generative chemistry models have been explored for potential applications in drug discovery. Early experimental work has explored the use of near-term quantum hardware in molecular generative modeling for drug discovery. In 2023, researchers at Gero reported a hybrid quantum–classical generative model based on a restricted Boltzmann machine, implemented on a commercially available quantum annealing device, to generate novel drug-like small molecules with physicochemical properties comparable to known medicinal compounds. However, the immense size and complexity of the structural space of all possible drug-like molecules pose significant obstacles, which could be overcome in the future by quantum computers. Quantum computers are naturally good for solving complex quantum many-body problems and thus may be instrumental in applications involving quantum chemistry. Therefore, one can expect that quantum-enhanced generative models including quantum GANs may eventually be developed into ultimate generative chemistry algorithms.

### AI-assisted algorithm discovery

Artificial intelligence has also been explored as a tool for discovering and optimizing algorithms relevant to quantum computing. AlphaEvolve, a Google DeepMind system based on large language models and evolutionary algorithms, has been described as a coding agent for scientific and algorithmic discovery. In quantum-computing research, AlphaEvolve-optimized quantum circuits have been used in work on quantum computation of molecular geometry through many-body nuclear spin echoes.
