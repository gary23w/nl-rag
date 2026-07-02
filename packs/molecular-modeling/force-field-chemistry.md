---
title: "Force field (chemistry)"
source: https://en.wikipedia.org/wiki/Force_field_(chemistry)
domain: molecular-modeling
license: CC-BY-SA-4.0
tags: molecular modeling, force field, molecular mechanics, potential energy surface
fetched: 2026-07-02
---

# Force field (chemistry)

In the context of chemistry, molecular physics, physical chemistry, and molecular modelling, a **force field** is a computational model that is used to describe the forces between atoms (or collections of atoms) within molecules or between molecules as well as in crystals. Force fields are a variety of interatomic potentials. More precisely, the force field refers to the functional form and parameter sets used to calculate the potential energy of a system on the atomistic level. Force fields are usually used in molecular dynamics or Monte Carlo simulations. The parameters for a chosen energy function may be derived from classical laboratory experiment data, calculations in quantum mechanics, or both. Force fields utilize the same concept as force fields in classical physics, with the main difference being that the force field parameters in chemistry describe the energy landscape on the atomistic level. From a force field, the acting forces on every particle are derived as a gradient of the potential energy with respect to the particle coordinates.

A large number of different force field types exist today (e.g. for organic molecules, ions, polymers, minerals, and metals). Depending on the material, different functional forms are usually chosen for the force fields since different types of atomistic interactions dominate the material behavior.

There are various criteria that can be used for categorizing force field parametrization strategies. An important differentiation is 'component-specific' and 'transferable'. For a component-specific parametrization, the considered force field is developed solely for describing a single given substance (e.g. water). For a transferable force field, all or some parameters are designed as building blocks and become transferable/ applicable for different substances (e.g. methyl groups in alkane transferable force fields). A different important differentiation addresses the physical structure of the models: A*ll-atom* force fields provide parameters for every type of atom in a system, including hydrogen, while *united-atom* interatomic potentials treat the hydrogen and carbon atoms in methyl groups and methylene bridges as one interaction center. *Coarse-grained* potentials, which are often used in long-time simulations of macromolecules such as proteins, nucleic acids, and multi-component complexes, sacrifice chemical details for higher computing efficiency.

## Force fields for molecular systems

The basic functional form of potential energy for modeling molecular systems includes intramolecular interaction terms for interactions of atoms that are linked by covalent bonds, and intermolecular (i.e. nonbonded also termed *noncovalent*) terms that describe the long-range electrostatic and van der Waals forces. The specific decomposition of the terms depends on the force field, but a general form for the total energy in an additive force field can be written as $E_{\text{total}}=E_{\text{bonded}}+E_{\text{nonbonded}}$ where the components of the covalent and noncovalent contributions are given by the following summations: $E_{\text{bonded}}=E_{\text{bond}}+E_{\text{angle}}+E_{\text{dihedral}}$ $E_{\text{nonbonded}}=E_{\text{electrostatic}}+E_{\text{van der Waals}}$

The bond and angle terms are usually modeled by quadratic energy functions that do not allow bond breaking. A more realistic description of a covalent bond at higher stretching is provided by the more expensive Morse potential. The functional form for dihedral energy is variable from one force field to another. Additionally, "improper torsional" terms may be added to enforce the planarity of aromatic rings and other conjugated systems, and "cross-terms" that describe the coupling of different internal variables, such as angles and bond lengths. Some force fields also include explicit terms for hydrogen bonds.

The nonbonded terms are computationally most intensive. A popular choice is to limit interactions to pairwise energies. The van der Waals term is usually computed with a Lennard-Jones potential or the Mie potential and the electrostatic term with Coulomb's law. However, both can be buffered or scaled by a constant factor to account for electronic polarizability. A large number of force fields based on this or similar energy expressions have been proposed in the past decades for modeling different types of materials such as molecular substances, metals, glasses etc. - see below for a comprehensive list of force fields.

### Bonded terms

#### Bond potential

As it is rare for bonds to deviate significantly from their equilibrium values, the most simplistic approaches utilize a Hooke's law formula: $E_{\text{bond}}={\frac {k_{ij}}{2}}(l_{ij}-l_{0,ij})^{2},$ where $k_{ij}$ is the force constant, $l_{ij}$ is the bond length, and $l_{0,ij}$ is the value for the bond length between atoms i and j when all other terms in the force field are set to 0. The term $l_{0,ij}$ is at times differently defined or taken at different thermodynamic conditions.

The bond stretching constant $k_{ij}$ can be determined from the experimental infrared spectrum, Raman spectrum, or high-level quantum-mechanical calculations. The constant $k_{ij}$ determines vibrational frequencies in molecular dynamics simulations. The stronger the bond is between atoms, the higher is the value of the force constant, and the higher the wavenumber (energy) in the IR/Raman spectrum.

Though the formula of Hooke's law provides a reasonable level of accuracy at bond lengths near the equilibrium distance, it is less accurate as one moves away. In order to model the Morse curve better, one could employ cubic and higher powers. However, for most practical applications these differences are negligible, and inaccuracies in predictions of bond lengths are on the order of the thousandth of an angstrom, which is also the limit of reliability for common force fields. A Morse potential can be employed instead to enable bond breaking and higher accuracy, even though it is less efficient to compute. For reactive force fields, bond breaking and bond orders are additionally considered.

#### Angle potential

Angular vibrations are usually described through a spring equation as well:

$E_{\text{angles}}=k_{i}^{\text{angle}}(\theta _{i}-\theta _{0})^{2}$

where $k_{i}^{\text{angle}}$ is the force constant, $\theta _{i}$ the angle between three atoms and $\theta _{0}$ the equilibrium angle.

#### Dihedral potential

A dihedral potential, also called torsion potential, is often described by the following function:

$E_{\text{dihedral}}=k_{i}^{\text{dihedral}}[1+\cos(n_{i}\phi _{i}+\delta _{i})]$

where $k_{i}^{\text{dihedral}}$ is the force constant, $\phi _{i}$ the dihedral angle, $\delta _{i}$ the phase and n defines the number of minima or maxima between 0 and $2\pi$ .

Dihedral terms admit a range of mathematical representations, as illustrated by the multiple dihedral functional forms provided in OpenMM’s standard forces.

### Non-bonded terms

#### Electrostatic interactions

Electrostatic interactions are represented by a Coulomb energy, which utilizes atomic charges $q_{i}$ to represent chemical bonding ranging from covalent to polar covalent and ionic bonding. The typical formula is the Coulomb law: $E_{\text{Coulomb}}={\frac {1}{4\pi \varepsilon _{0}}}{\frac {q_{i}q_{j}}{r_{ij}}},$ where $r_{ij}$ is the distance between two atoms i and j . The total Coulomb energy is a sum over all pairwise combinations of atoms and usually excludes 1, 2 bonded atoms, 1, 3 bonded atoms, as well as 1, 4 bonded atoms.

Atomic charges can make dominant contributions to the potential energy, especially for polar molecules and ionic compounds, and are critical to simulate the geometry, interaction energy, and the reactivity. The assignment of charges usually uses some heuristic approach, with different possible solutions.

Historically the electrostatic potential (ESP) has been used to determine partial charges with the Merz-Kollman method being one of the first. Other methods uses population based analysis schemes of wavefunctions like the Mulliken or Löwdin population analysis.

Another method to derive partial charges are charge equilibration methods like EEM, SQE or ACKS2. The idea is to assign geometry-dependent charges by letting electronegativity differences drive charge flow between atoms until a self-consistent minimum of the electrostatic energy is reached.

## Force fields for crystal systems

Atomistic interactions in crystal systems significantly deviate from those in molecular systems, e.g. of organic molecules. For crystal systems, particularly multi-body interactions, these interactions are important and cannot be neglected if a high accuracy of the force field is the aim. For crystal systems with covalent bonding, bond order potentials are usually used, e.g. Tersoff potentials. For metal systems, usually embedded atom potentials are used. Additionally, Drude model potentials have been developed, which describe a form of attachment of electrons to nuclei.

## Parameterization

In addition to the functional form of the potentials, a force fields consists of the parameters of these functions. Together, they specify the interactions on the atomistic level. The parametrization, i.e. determining of the parameter values, is crucial for the accuracy and reliability of the force field. Different parametrization procedures have been developed for the parametrization of different substances, e.g. metals, ions, and molecules. For different material types, usually different parametrization strategies are used. In general, two main types can be distinguished for the parametrization, either using data/ information from the atomistic level, e.g. from quantum mechanical calculations or spectroscopic data, or using data from macroscopic properties, e.g. the hardness or compressibility of a given material. Often a combination of these routes is used. Hence, one way or the other, the force field parameters are always determined in an empirical way. Nevertheless, the term 'empirical' is often used in the context of force field parameters when macroscopic material property data was used for the fitting. Experimental data (microscopic and macroscopic) included for the fit, for example, the enthalpy of vaporization, enthalpy of sublimation, dipole moments, and various spectroscopic properties such as vibrational frequencies. Often, for molecular systems, quantum mechanical calculations in the gas phase are used for parametrizing intramolecular interactions and parametrizing intermolecular dispersive interactions by using macroscopic properties such as liquid densities. The assignment of atomic charges often follows quantum mechanical protocols with some heuristics, which can lead to significant deviation in representing specific properties.

A large number of workflows and parametrization procedures have been employed in the past decades using different data and optimization strategies for determining the force field parameters. They differ significantly, which is also due to different focuses of different developments. The parameters for molecular simulations of biological macromolecules such as proteins, DNA, and RNA were often derived/transferred from observations for small organic molecules, which are more accessible for experimental studies and quantum calculations.

Atom types are defined for different elements as well as for the same elements in sufficiently different chemical environments. For example, oxygen atoms in water and an oxygen atoms in a carbonyl functional group are classified as different force field types. Typical molecular force field parameter sets include values for atomic mass, atomic charge, Lennard-Jones parameters for every atom type, as well as equilibrium values of bond lengths, bond angles, and dihedral angles. The bonded terms refer to pairs, triplets, and quadruplets of bonded atoms, and include values for the effective spring constant for each potential.

Heuristic force field parametrization procedures have been very successful for many years, but recently criticized since they are usually not fully automated and therefore subject to some subjectivity of the developers, which also brings problems regarding the reproducibility of the parametrization procedure.

Efforts to provide open source codes and methods include openMM and openMD. The use of semi-automation or full automation, without input from chemical knowledge, is likely to increase inconsistencies at the level of atomic charges, for the assignment of remaining parameters, and likely to dilute the interpretability and performance of parameters.

A open-source software to derive parameters for different potential function is the Alexandria Chemistry Toolkit (ACT) which was published in 2025. It can generate and optimize physics-based force fields from scratch by machine learning. Atom and bond parameters are considered genes of a genome, where force field accuracy is tied to the fitness of the genome. Using a genetic algorithm (GA) and a Markov chain Monte Carlo (MCMC) algorithm, it can perform chromosomal crossovers and induce point mutations for global and local improvements closely resembling actual evolutionary operators. Force field parameters are trained on quantum chemical energies, such as Symmetry-Adapted perturbation theory (SAPT) for non-covalent dimer interaction energies and Second-Order Møller-Plesset Perturbation Theory (MP2) scans for intramolecular energies.

## Force field databases

A large number of force fields has been published in the past decades - mostly in scientific publications. In recent years, some databases have attempted to collect, categorize and make force fields digitally available. Therein, different databases focus on different types of force fields. For example, the openKim database focuses on interatomic functions describing the individual interactions between specific elements. The TraPPE database focuses on transferable force fields of organic molecules (developed by the Siepmann group). The MolMod database focuses on molecular and ionic force fields (both component-specific and transferable).

## Transferability and mixing function types

Functional forms and parameter sets have been defined by the developers of interatomic potentials and feature variable degrees of self-consistency and transferability. When functional forms of the potential terms vary or are mixed, the parameters from one interatomic potential function can typically not be used together with another interatomic potential function. In some cases, modifications can be made with minor effort, for example, between 9-6 Lennard-Jones potentials to 12-6 Lennard-Jones potentials. Transfers from Buckingham potentials to harmonic potentials, or from Embedded Atom Models to harmonic potentials, on the contrary, would require many additional assumptions and may not be possible.

In many cases, force fields can be straight forwardly combined. Yet, often, additional specifications and assumptions are required.

## Limitations

All interatomic potentials are based on approximations and experimental data, therefore often termed *empirical*. The performance varies from higher accuracy than density functional theory (DFT) calculations, with access to million times larger systems and time scales, to random guesses depending on the force field. The use of accurate representations of chemical bonding, combined with reproducible experimental data and validation, can lead to lasting interatomic potentials of high quality with much fewer parameters and assumptions in comparison to DFT-level quantum methods.

Possible limitations include atomic charges, also called point charges. Most force fields rely on point charges to reproduce the electrostatic potential around molecules, which works less well for anisotropic charge distributions. The remedy is that point charges have a clear interpretation and virtual electrons can be added to capture essential features of the electronic structure, such as additional polarizability in metallic systems to describe the image potential, internal multipole moments in π-conjugated systems, and lone pairs in water. Electronic polarization of the environment may be better included by using *polarizable force fields* or using a macroscopic dielectric constant. However, application of one value of dielectric constant is a coarse approximation in the highly heterogeneous environments of proteins, biological membranes, minerals, or electrolytes.

All types of van der Waals forces are also strongly environment-dependent because these forces originate from interactions of induced and "instantaneous" dipoles (see Intermolecular force). The original Fritz London theory of these forces applies only in a vacuum. A more general theory of van der Waals forces in condensed media was developed by A. D. McLachlan in 1963 and included the original London's approach as a special case. The McLachlan theory predicts that van der Waals attractions in media are weaker than in vacuum and follow the *like dissolves like* rule, which means that different types of atoms interact more weakly than identical types of atoms. This is in contrast to *combinatorial rules* or Slater-Kirkwood equation applied for development of the classical force fields. The *combinatorial rules* state that the interaction energy of two dissimilar atoms (e.g., C...N) is an average of the interaction energies of corresponding identical atom pairs (i.e., C...C and N...N). According to McLachlan's theory, the interactions of particles in media can even be fully repulsive, as observed for liquid helium, however, the lack of vaporization and presence of a freezing point contradicts a theory of purely repulsive interactions. Measurements of attractive forces between different materials (Hamaker constant) have been explained by Jacob Israelachvili. For example, "*the interaction between hydrocarbons across water is about 10% of that across vacuum*". Such effects are represented in molecular dynamics through pairwise interactions that are spatially more dense in the condensed phase relative to the gas phase and reproduced once the parameters for all phases are validated to reproduce chemical bonding, density, and cohesive/surface energy.

Limitations have been strongly felt in protein structure refinement. The major underlying challenge is the huge conformation space of polymeric molecules, which grows beyond current computational feasibility when containing more than ~20 monomers. Participants in Critical Assessment of protein Structure Prediction (CASP) did not try to refine their models to avoid "*a central embarrassment of molecular mechanics, namely that energy minimization or molecular dynamics generally leads to a model that is less like the experimental structure*". Force fields have been applied successfully for protein structure refinement in different X-ray crystallography and NMR spectroscopy applications, especially using program XPLOR. However, the refinement is driven mainly by a set of experimental constraints and the interatomic potentials serve mainly to remove interatomic hindrances. The results of calculations were practically the same with rigid sphere potentials implemented in program DYANA (calculations from NMR data), or with programs for crystallographic refinement that use no energy functions at all. These shortcomings are related to interatomic potentials and to the inability to sample the conformation space of large molecules effectively. Thereby also the development of parameters to tackle such large-scale problems requires new approaches. A specific problem area is homology modeling of proteins. Meanwhile, alternative empirical scoring functions have been developed for ligand docking, protein folding, homology model refinement, computational protein design, and modeling of proteins in membranes.

It was also argued that some protein force fields operate with energies that are irrelevant to protein folding or ligand binding. The parameters of proteins force fields reproduce the enthalpy of sublimation, i.e., energy of evaporation of molecular crystals. However, protein folding and ligand binding are thermodynamically closer to crystallization, or liquid-solid transitions as these processes represent *freezing* of mobile molecules in condensed media. Thus, free energy changes during protein folding or ligand binding are expected to represent a combination of an energy similar to heat of fusion (energy absorbed during melting of molecular crystals), a conformational entropy contribution, and solvation free energy. The heat of fusion is significantly smaller than enthalpy of sublimation. Hence, the potentials describing protein folding or ligand binding need more consistent parameterization protocols, e.g., as described for IFF. Indeed, the energies of H-bonds in proteins are ~ −1.5 kcal/mol when estimated from protein engineering or alpha helix to coil transition data, but the same energies estimated from sublimation enthalpy of molecular crystals were −4 to −6 kcal/mol, which is related to re-forming existing hydrogen bonds and not forming hydrogen bonds from scratch. The depths of modified Lennard-Jones potentials derived from protein engineering data were also smaller than in typical potential parameters and followed the *like dissolves like* rule, as predicted by McLachlan theory.

## Force fields available in the literature

Different force fields are designed for different purposes:

### Classical

- AMBER (Assisted Model Building and Energy Refinement) – widely used for proteins and DNA.
- CFF (Consistent Force Field) – a family of force fields adapted to a broad variety of organic compounds, includes force fields for polymers, metals, etc. CFF was developed by Arieh Warshel, Lifson, and coworkers as a general method for unifying studies of energies, structures, and vibration of general molecules and molecular crystals. The CFF program, developed by Levitt and Warshel, is based on the Cartesian representation of all the atoms, and it served as the basis for many subsequent simulation programs.
- CHARMM (Chemistry at HARvard Molecular Mechanics) – originally developed at Harvard, widely used for both small molecules and macromolecules
- COSMOS-NMR – hybrid QM/MM force field adapted to various inorganic compounds, organic compounds, and biological macromolecules, including semi-empirical calculation of atomic charges NMR properties. COSMOS-NMR is optimized for NMR-based structure elucidation and implemented in COSMOS molecular modelling package.
- CVFF – also used broadly for small molecules and macromolecules.
- ECEPP – first force field for polypeptide molecules - developed by F.A. Momany, H.A. Scheraga and colleagues. ECEPP was developed specifically for the modeling of peptides and proteins. It uses fixed geometries of amino acid residues to simplify the potential energy surface. Thus, the energy minimization is conducted in the space of protein torsion angles. Both MM2 and ECEPP include potentials for H-bonds and torsion potentials for describing rotations around single bonds. ECEPP/3 was implemented (with some modifications) in Internal Coordinate Mechanics and FANTOM.
- GROMOS (GROningen MOlecular Simulation) – a force field that comes as part of the GROMOS software, a general-purpose molecular dynamics computer simulation package for the study of biomolecular systems. GROMOS force field A-version has been developed for application to aqueous or apolar solutions of proteins, nucleotides, and sugars. A B-version to simulate gas phase isolated molecules is also available.
- IFF (Interface Force Field) – covers metals, minerals, 2D materials, and polymers. It uses 12-6 LJ and 9-6 LJ interactions. IFF was developed as for compounds across the periodic table. It assigns consistent charges, utilizes standard conditions as a reference state, reproduces structures, energies, and energy derivatives, and quantifies limitations for all included compounds. The Interface force field (IFF) assumes one single energy expression for all compounds across the periodic (with 9-6 and 12-6 LJ options). The IFF is in most parts non-polarizable, but also comprises polarizable parts, e.g. for some metals (Au, W) and pi-conjugated molecules
- MMFF (Merck Molecular Force Field) – developed at Merck for a broad range of molecules.
- MM2 was developed by Norman Allinger mainly for conformational analysis of hydrocarbons and other small organic molecules. It is designed to reproduce the equilibrium covalent geometry of molecules as precisely as possible. It implements a large set of parameters that is continuously refined and updated for many different classes of organic compounds (MM3 and MM4).
- OPLS (Optimized Potential for Liquid Simulations) (variants include OPLS-AA, OPLS-UA, OPLS-2001, OPLS-2005, OPLS3e, OPLS4) – developed by William L. Jorgensen at the Yale University Department of Chemistry.
- QCFF/PI – A general force fields for conjugated molecules.
- UFF (Universal Force Field) – A general force field with parameters for the full periodic table up to and including the actinoids, developed at Colorado State University. The reliability is known to be poor due to lack of validation and interpretation of the parameters for nearly all claimed compounds, especially metals and inorganic compounds.

### Polarizable

Several force fields explicitly capture polarizability, where a particle's effective charge can be influenced by electrostatic interactions with its neighbors. Core-shell models are common, which consist of a positively charged core particle, representing the polarizable atom, and a negatively charged particle attached to the core atom through a spring-like harmonic oscillator potential. Recent examples include polarizable models with virtual electrons that reproduce image charges in metals and polarizable biomolecular force fields.

- AMBER – polarizable force field developed by Jim Caldwell and coworkers.
- AMOEBA (Atomic Multipole Optimized Energetics for Biomolecular Applications) – force field developed by Pengyu Ren (University of Texas at Austin) and Jay W. Ponder (Washington University). AMOEBA force field is gradually moving to more physics-rich AMOEBA+.
- CHARMM – polarizable force field developed by S. Patel (University of Delaware) and C. L. Brooks III (University of Michigan). Based on the classical Drude oscillator developed by Alexander MacKerell (University of Maryland, Baltimore) and Benoit Roux (University of Chicago).
- CFF/ind and ENZYMIX – The first polarizable force field which has subsequently been used in many applications to biological systems.
- COSMOS-NMR (Computer Simulation of Molecular Structure) – developed by Ulrich Sternberg and coworkers. Hybrid QM/MM force field enables explicit quantum-mechanical calculation of electrostatic properties using localized bond orbitals with fast BPT formalism. Atomic charge fluctuation is possible in each molecular dynamics step.
- DRF90 – developed by P. Th. van Duijnen and coworkers.
- NEMO (Non-Empirical Molecular Orbital) – procedure developed by Gunnar Karlström and coworkers at Lund University (Sweden)
- PIPF – The polarizable intermolecular potential for fluids is an induced point-dipole force field for organic liquids and biopolymers. The molecular polarization is based on Thole's interacting dipole (TID) model and was developed by Jiali Gao Gao Research Group | at the University of Minnesota.
- Polarizable Force Field (PFF) – developed by Richard A. Friesner and coworkers.
- SP-basis Chemical Potential Equalization (CPE) – approach developed by R. Chelli and P. Procacci.
- PHAST – polarizable potential developed by Chris Cioce and coworkers.
- ORIENT – procedure developed by Anthony J. Stone (Cambridge University) and coworkers.
- Gaussian Electrostatic Model (GEM) – a polarizable force field based on Density Fitting developed by Thomas A. Darden and G. Andrés Cisneros at NIEHS; and Jean-Philip Piquemal at Paris VI University.
- Atomistic Polarizable Potential for Liquids, Electrolytes, and Polymers(APPLE&P), developed by Oleg Borogin, Dmitry Bedrov and coworkers, which is distributed by Wasatch Molecular Incorporated.
- Polarizable procedure based on the Kim-Gordon approach developed by Jürg Hutter and coworkers (University of Zürich)
- GFN-FF (Geometry, Frequency, and Noncovalent Interaction Force-Field) – a completely automated partially polarizable generic force-field for the accurate description of structures and dynamics of large molecules across the periodic table developed by Stefan Grimme and Sebastian Spicher at the University of Bonn.
- WASABe v1.0 PFF (for Water, orgAnic Solvents, And Battery electrolytes) An isotropic atomic dipole polarizable force field for accurate description of battery electrolytes in terms of thermodynamic and dynamic properties for high lithium salt concentrations in sulfonate solvent by Oleg Starovoytov
- XED (eXtended Electron Distribution) - a polarizable force-field created as a modification of an atom-centered charge model, developed by Andy Vinter. Partially charged monopoles are placed surrounding atoms to simulate more geometrically accurate electrostatic potentials at a fraction of the expense of using quantum mechanical methods. Primarily used by software packages supplied by Cresset Biomolecular Discovery.

### Reactive

- EVB (Empirical valence bond) – reactive force field introduced by Warshel and coworkers for use in modeling chemical reactions in different environments. The EVB facilitates calculating activation free energies in condensed phases and in enzymes.
- ReaxFF – reactive force field (interatomic potential) developed by Adri van Duin, William Goddard and coworkers. It is slower than classical MD (50x), needs parameter sets with specific validation, and has no validation for surface and interfacial energies. Parameters are non-interpretable. It can be used atomistic-scale dynamical simulations of chemical reactions. Parallelized ReaxFF allows reactive simulations on >>1,000,000 atoms on large supercomputers.

### Coarse-grained

- DPD (Dissipative particle dynamics) – This is a method commonly applied in chemical engineering. It is typically used for studying the hydrodynamics of various simple and complex fluids which require consideration of time and length scales larger than those accessible to classical Molecular dynamics. The potential was originally proposed by Hoogerbrugge and Koelman with later modifications by Español and Warren The current state of the art was well documented in a CECAM workshop in 2008. Recently, work has been undertaken to capture some of the chemical subtitles relevant to solutions. This has led to work considering automated parameterisation of the DPD interaction potentials against experimental observables.
- MARTINI – a coarse-grained potential developed by Marrink and coworkers at the University of Groningen, initially developed for molecular dynamics simulations of lipids, later extended to various other molecules. The force field applies a mapping of four heavy atoms to one CG interaction site and is parameterized with the aim of reproducing thermodynamic properties.
- SAFT – A top-down coarse-grained model developed in the Molecular Systems Engineering group at Imperial College London fitted to liquid phase densities and vapor pressures of pure compounds by using the SAFT equation of state.
- SIRAH – a coarse-grained force field developed by Pantano and coworkers of the Biomolecular Simulations Group, Institut Pasteur of Montevideo, Uruguay; developed for molecular dynamics of water, DNA, and proteins. Free available for AMBER and GROMACS packages.
- VAMM (Virtual atom molecular mechanics) – a coarse-grained force field developed by Korkut and Hendrickson for molecular mechanics calculations such as large scale conformational transitions based on the virtual interactions of C-alpha atoms. It is a knowledge based force field and formulated to capture features dependent on secondary structure and on residue-specific contact information in proteins.

### Machine learning

- MACE (Multi Atomic Cluster Expansion) is a highly accurate machine learning force field architecture that combines the rigorous many-body expansion of the total potential energy with rotationally equivariant representations of the system.
- ANI (Artificial Narrow Intelligence) is a transferable neural network potential, built from atomic environment vectors, and able to provide DFT accuracy in terms of energies.
- FFLUX (originally QCTFF) A set of trained Kriging models which operate together to provide a molecular force field trained on Atoms in molecules or Quantum chemical topology energy terms including electrostatic, exchange and electron correlation.
- TensorMol, a mixed model, a neural network provides a short-range potential, whilst more traditional potentials add screened long-range terms.
- Δ-ML not a force field method but a model that adds learnt correctional energy terms to approximate and relatively computationally cheap quantum chemical methods in order to provide an accuracy level of a higher order, more computationally expensive quantum chemical model.
- SchNet a Neural network utilising continuous-filter convolutional layers, to predict chemical properties and potential energy surfaces.
- PhysNet is a Neural Network-based energy function to predict energies, forces and (fluctuating) partial charges.
- Neuroevolution potential (NEP, 2021) is a method to construct new potential functions using a neural network structure. Many pretrained models (parameter sets) are available. A variant couples it with interlayer VDW potentials.
- Denoising force field (DFF): method to use a diffusion model for coarse-grained protein dynamics. Sampling from the model is similar to sampling from the equilibrium distribution. The "score" used by the model can be extracted and used like an energy term.
- SO3LR, a pretrained force field for efficient molecular dynamics simulation of biomolecules on GPUs. Uses the SO3krates semilocal many-body potential (a transformer_along with universal pairwise force fields.

### Water

The set of parameters used to model water or aqueous solutions (basically a force field for water) is called a water model. Many water models have been proposed; some examples are TIP3P, TIP4P, SPC, flexible simple point charge water model (flexible SPC), ST2, and mW. Other solvents and methods of solvent representation are also applied within computational chemistry and physics; these are termed solvent models.

### Other

- LFMM (Ligand Field Molecular Mechanics) - functions for the coordination sphere around transition metals based on the angular overlap model (AOM). Implemented in the Molecular Operating Environment (MOE) as DommiMOE and in Tinker
- VALBOND - a function for angle bending that is based on valence bond theory and works for large angular distortions, hypervalent molecules, and transition metal complexes. It can be incorporated into other force fields such as CHARMM and UFF.
