---
title: "Ab initio quantum chemistry methods"
source: https://en.wikipedia.org/wiki/Ab_initio_quantum_chemistry_methods
domain: buckingham-potential
license: CC-BY-SA-4.0
tags: buckingham potential
fetched: 2026-07-04
---

# *Ab initio* quantum chemistry methods

***Ab initio* quantum chemistry methods** are a class of computational chemistry techniques based on quantum chemistry that aim to solve the electronic Schrödinger equation. *Ab initio* means "from first principles" or "from the beginning", meaning using only physical constants and the positions and number of electrons in the system as input. This *ab initio* approach contrasts with other computational methods that rely on empirical parameters or approximations. By solving this fundamental equation, *ab initio* methods seek to accurately predict various chemical properties, including electron densities, energies, and molecular structures.

The ability to run these calculations has enabled theoretical chemists to solve a range of problems and their importance is highlighted by the awarding of the 1998 Nobel prize to John Pople and Walter Kohn. The term *ab initio* was first used in quantum chemistry by Robert Parr and coworkers, including David Craig in a semiempirical study on the excited states of benzene. The background is described by Parr.

## Accuracy and scaling

*Ab initio* electronic structure methods aim to calculate the many-electron function which is the solution of the non-relativistic electronic Schrödinger equation (in the Born–Oppenheimer approximation). The many-electron function is generally a linear combination of many simpler electron functions with the dominant function being the Hartree-Fock function. Each of these simple functions are then approximated using only one-electron functions. The one-electron functions are then expanded as a linear combination of a finite set of basis functions. This approach has the advantage that it can be made to converge to the exact solution, when the basis set tends toward the limit of a complete set and where all possible configurations are included (called "Full CI"). However this convergence to the limit is computationally very demanding and most calculations are far from the limit. Nevertheless important conclusions have been made from these more limited classifications.

One needs to consider the computational cost of *ab initio* methods when determining whether they are appropriate for the problem at hand. When compared to much less accurate approaches, such as molecular mechanics, *ab initio* methods often take larger amounts of computer time, memory, and disk space, though, with modern advances in computer science and technology such considerations are becoming less of an issue. The Hartree-Fock (HF) method scales nominally as *N*4 (*N* being a relative measure of the system size, not the number of basis functions) – e.g., if one doubles the number of electrons and the number of basis functions (double the system size), the calculation will take 16 (24) times as long per iteration. However, in practice it can scale closer to *N*3 as the program can identify zero and extremely small integrals and neglect them. Correlated calculations scale less favorably, though their accuracy is usually greater, which is the trade off one needs to consider. One popular method is Møller–Plesset perturbation theory (MP). To second order (MP2), MP scales as *N*4. To third order (MP3) MP scales as *N*6. To fourth order (MP4) MP scales as *N*7. Another method, coupled cluster with singles and doubles (CCSD), scales as *N*6 and extensions, CCSD(T) and CR-CC(2,3), scale as *N*6 with one noniterative step which scales as *N*7. Hybrid Density functional theory (DFT) methods using functionals which include Hartree–Fock exchange scale in a similar manner to Hartree–Fock but with a larger proportionality term and are thus more expensive than an equivalent Hartree–Fock calculation. Local DFT methods that do not include Hartree–Fock exchange can scale better than Hartree–Fock.

### Linear scaling approaches

The problem of computational expense can be alleviated through simplification schemes. In the *density fitting* scheme, the four-index integrals used to describe the interaction between electron pairs are reduced to simpler two- or three-index integrals, by treating the charge densities they contain in a simplified way. This reduces the scaling with respect to basis set size. Methods employing this scheme are denoted by the prefix "df-", for example the density fitting MP2 is df-MP2 (many authors use lower-case to prevent confusion with DFT). In the *local approximation*, the molecular orbitals are first localized by a unitary rotation in the orbital space (which leaves the reference wave function invariant, i.e., not an approximation) and subsequently interactions of distant pairs of localized orbitals are neglected in the correlation calculation. This sharply reduces the scaling with molecular size, a major problem in the treatment of biologically-sized molecules. Methods employing this scheme are denoted by the prefix "L", e.g. LMP2. Both schemes can be employed together, as in the df-LMP2 and df-LCCSD(T0) methods. In fact, df-LMP2 calculations are faster than df-Hartree–Fock calculations and thus are feasible in nearly all situations in which also DFT is.

## Classes of methods

The most popular classes of *ab initio* electronic structure methods:

### Hartree–Fock methods

- Hartree–Fock – Approximation method in quantum physicsPages displaying short descriptions of redirect targets (HF)
- Restricted open-shell Hartree–Fock (ROHF)
- Unrestricted Hartree–Fock – Method for calculating open-shell systems (UHF)

### Post-Hartree–Fock methods

- Møller–Plesset perturbation theory – Method in ab initio Quantum Chemistry (MP*n*)
- Configuration interaction – Concept in computational chemistry (CI)
- Coupled cluster – Method for approximating many-body systems (CC)
- Quadratic configuration interaction (QCI)
- Quantum chemistry composite methods – Combining multiple simulation methods
- Sign learning kink-based (SiLK) quantum Monte Carlo

### Multi-reference methods

- Multi-configurational self-consistent field – Method in quantum chemistry (MCSCF including CASSCF and RASSCF)
- Multi-reference configuration interaction (MRCI)
- n-electron valence state perturbation theory (NEVPT)
- Complete active space perturbation theory (CASPT*n*)
- State universal multi-reference coupled-cluster theory (SUMR-CC)

## Methods in detail

### Hartree–Fock and post-Hartree–Fock methods

The simplest type of *ab initio* electronic structure calculation is the Hartree–Fock (HF) scheme, in which the instantaneous Coulombic electron-electron repulsion is not specifically taken into account. Only its average effect (mean field) is included in the calculation. This is a variational procedure; therefore, the obtained approximate energies, expressed in terms of the system's wave function, are always equal to or greater than the exact energy, and tend to a limiting value called the Hartree–Fock limit as the size of the basis is increased. Many types of calculations begin with a Hartree–Fock calculation and subsequently correct for electron-electron repulsion, referred to also as electronic correlation. Møller–Plesset perturbation theory (MP*n*) and coupled cluster theory (CC) are examples of these post-Hartree–Fock methods. In some cases, particularly for bond breaking processes, the Hartree–Fock method is inadequate and this single-determinant reference function is not a good basis for post-Hartree–Fock methods. It is then necessary to start with a wave function that includes more than one determinant such as multi-configurational self-consistent field (MCSCF) and methods have been developed that use these multi-determinant references for improvements. However, if one uses coupled cluster methods such as CCSDT, CCSDt, CR-CC(2,3), or CC(t;3) then single-bond breaking using the single determinant HF reference is feasible. For an accurate description of double bond breaking, methods such as CCSDTQ, CCSDTq, CCSDtq, CR-CC(2,4), or CC(tq;3,4) also make use of the single determinant HF reference, and do not require one to use multi-reference methods.

**Example**

Is the bonding situation in

disilyne

Si

2

H

2

the same as in

acetylene

(C

2

H

2

)?

A series of *ab initio* studies of Si2H2 is an example of how *ab initio* computational chemistry can predict new structures that are subsequently confirmed by experiment. They go back over 20 years, and most of the main conclusions were reached by 1995. The methods used were mostly post-Hartree–Fock, particularly configuration interaction (CI) and coupled cluster (CC). Initially the question was whether disilyne, Si2H2 had the same structure as ethyne (acetylene), C2H2. In early studies, by Binkley and Lischka and Kohler, it became clear that linear Si2H2 was a transition structure between two equivalent trans-bent structures and that the ground state was predicted to be a four-membered ring bent in a 'butterfly' structure with hydrogen atoms bridged between the two silicon atoms. Interest then moved to look at whether structures equivalent to vinylidene (Si=SiH2) existed. This structure is predicted to be a local minimum, i.e. an isomer of Si2H2, lying higher in energy than the ground state but below the energy of the trans-bent isomer. Then a new isomer with an unusual structure was predicted by Brenda Colegrove in Henry F. Schaefer III's group. It requires post-Hartree–Fock methods to obtain a local minimum for this structure. It does not exist on the Hartree–Fock energy hypersurface. The new isomer is a planar structure with one bridging hydrogen atom and one terminal hydrogen atom, cis to the bridging atom. Its energy is above the ground state but below that of the other isomers. Similar results were later obtained for Ge2H2. Al2H2 and Ga2H2 have exactly the same isomers, in spite of having two electrons less than the Group 14 molecules. The only difference is that the four-membered ring ground state is planar and not bent. The cis-mono-bridged and vinylidene-like isomers are present. Experimental work on these molecules is not easy, but matrix isolation spectroscopy of the products of the reaction of hydrogen atoms and silicon and aluminium surfaces has found the ground state ring structures and the cis-mono-bridged structures for Si2H2 and Al2H2. Theoretical predictions of the vibrational frequencies were crucial in understanding the experimental observations of the spectra of a mixture of compounds. This may appear to be an obscure area of chemistry, but the differences between carbon and silicon chemistry is always a lively question, as are the differences between group 13 and group 14 (mainly the B and C differences). The silicon and germanium compounds were the subject of a Journal of Chemical Education article.

### Valence bond methods

Valence bond (VB) methods are generally *ab initio* although some semi-empirical versions have been proposed. Current VB approaches are:

- Generalized valence bond – Quantum chemistry method extending valence bond theory (GVB)
- Modern valence bond theory (MVBT)

### Quantum Monte Carlo methods

A method that avoids making the variational overestimation of HF in the first place is Quantum Monte Carlo (QMC), in its variational, diffusion, and Green's function forms. These methods work with an explicitly correlated wave function and evaluate integrals numerically using a Monte Carlo integration. Such calculations can be very time-consuming. The accuracy of QMC depends strongly on the initial guess of many-body wave-functions and the form of the many-body wave-function. One simple choice is Slater-Jastrow wave-function in which the local correlations are treated with the Jastrow factor.

Sign Learning Kink-based (SiLK) Quantum Monte Carlo (website): The Sign Learning Kink (SiLK) based Quantum Monte Carlo (QMC) method is based on Feynman's path integral formulation of quantum mechanics, and can reduce the minus sign problem when calculating energies in atomic and molecular systems.
