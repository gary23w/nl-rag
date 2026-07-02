---
title: "Drug design"
source: https://en.wikipedia.org/wiki/Drug_design
domain: structure-based-drug-design
license: CC-BY-SA-4.0
tags: rational drug design, target binding, receptor pocket, affinity
fetched: 2026-07-02
---

# Drug design

| (Drug discovery cycle schematic) |
|---|

**Drug design**, often referred to as **rational drug design** or simply rational design, is the inventive process of finding new medications based on the knowledge of a biological target. The drug is most commonly an organic small molecule that activates or inhibits the function of a biomolecule such as a protein, which in turn results in a therapeutic benefit to the patient. In the most basic sense, drug design involves the design of molecules that are complementary in shape and charge to the biomolecular target with which they interact and therefore will bind to it. Drug design frequently but not necessarily relies on computer modeling techniques. This type of modeling is sometimes referred to as **computer-aided drug design**. Finally, drug design that relies on the knowledge of the three-dimensional structure of the biomolecular target is known as **structure-based drug design**. In addition to small molecules, biopharmaceuticals including peptides and especially therapeutic antibodies are an increasingly important class of drugs and computational methods for improving the affinity, selectivity, and stability of these protein-based therapeutics have also been developed.

## Definition

The phrase "drug design" is similar to ligand design (i.e., design of a molecule that will bind tightly to its target). Although design techniques for prediction of binding affinity are reasonably successful, there are many other properties, such as bioavailability, metabolic half-life, and side effects, that first must be optimized before a ligand can become a safe and effective drug. These other characteristics are often difficult to predict with rational design techniques.

Due to high attrition rates, especially during clinical phases of drug development, more attention is being focused early in the drug design process on selecting candidate drugs whose physicochemical properties are predicted to result in fewer complications during development and hence more likely to lead to an approved, marketed drug. Furthermore, in vitro experiments complemented with computation methods are increasingly used in early drug discovery to select compounds with more favorable ADME (absorption, distribution, metabolism, and excretion) and toxicological profiles.

## Drug targets

A biomolecular target (most commonly a protein or a nucleic acid) is a key molecule involved in a particular metabolic or signaling pathway that is associated with a specific disease condition or pathology or to the infectivity or survival of a microbial pathogen. Potential drug targets are not necessarily disease causing but must by definition be disease modifying. In some cases, small molecules will be designed to enhance or inhibit the target function in the specific disease modifying pathway. Small molecules (for example receptor agonists, antagonists, inverse agonists, or modulators; enzyme activators or inhibitors; or ion channel openers or blockers) will be designed that are complementary to the binding site of target. Small molecules (drugs) can be designed so as not to affect any other important "off-target" molecules (often referred to as antitargets) since drug interactions with off-target molecules may lead to undesirable side effects. Due to similarities in binding sites, closely related targets identified through sequence homology have the highest chance of cross reactivity and hence highest side effect potential.

Most commonly, drugs are organic small molecules produced through chemical synthesis, but biopolymer-based drugs (also known as biopharmaceuticals) produced through biological processes are becoming increasingly more common. In addition, mRNA-based gene silencing technologies may have therapeutic applications. For example, nanomedicines based on mRNA can streamline and expedite the drug development process, enabling transient and localized expression of immunostimulatory molecules. In vitro transcribed (IVT) mRNA allows for delivery to various accessible cell types via the blood or alternative pathways. The use of IVT mRNA serves to convey specific genetic information into a person's cells, with the primary objective of preventing or altering a particular disease.

### Drug discovery

#### Phenotypic drug discovery

Phenotypic drug discovery is a traditional drug discovery method, also known as forward pharmacology or classical pharmacology. It uses the process of phenotypic screening on collections of synthetic small molecules, natural products, or extracts within chemical libraries to pinpoint substances exhibiting beneficial therapeutic effects. This method is to first discover the in vivo or in vitro functional activity of drugs (such as extract drugs or natural products), and then perform target identification. Phenotypic discovery uses a practical and target-independent approach to generate initial leads, aiming to discover pharmacologically active compounds and therapeutics that operate through novel drug mechanisms. This method allows the exploration of disease phenotypes to find potential treatments for conditions with unknown, complex, or multifactorial origins, where the understanding of molecular targets is insufficient for effective intervention.

#### Rational drug discovery

Rational drug design (also called reverse pharmacology) begins with a hypothesis that modulation of a specific biological target may have therapeutic value. In order for a biomolecule to be selected as a drug target, two essential pieces of information are required. The first is evidence that modulation of the target will be disease modifying. This knowledge may come from, for example, disease linkage studies that show an association between mutations in the biological target and certain disease states. The second is that the target is capable of binding to a small molecule and that its activity can be modulated by the small molecule.

Once a suitable target has been identified, the target is normally cloned and produced and purified. The purified protein is then used to establish a screening assay. In addition, the three-dimensional structure of the target may be determined.

The search for small molecules that bind to the target is begun by screening libraries of potential drug compounds. This may be done by using the screening assay (a "wet screen"). In addition, if the structure of the target is available, a virtual screen may be performed of candidate drugs. Ideally, the candidate drug compounds should be "drug-like", that is they should possess properties that are predicted to lead to oral bioavailability, adequate chemical and metabolic stability, and minimal toxic effects. Several methods are available to estimate druglikeness such as Lipinski's Rule of Five and a range of scoring methods such as lipophilic efficiency. Several methods for predicting drug metabolism have also been proposed in the scientific literature.

Due to the large number of drug properties that must be simultaneously optimized during the design process, multi-objective optimization techniques are sometimes employed. Finally because of the limitations in the current methods for prediction of activity, drug design is still very much reliant on serendipity and bounded rationality.

## Computer-aided drug design

The most fundamental goal in drug design is to predict whether a given molecule will bind to a target and if so how strongly. Molecular mechanics or molecular dynamics is most often used to estimate the strength of the intermolecular interaction between the small molecule and its biological target. These methods are also used to predict the conformation of the small molecule and to model conformational changes in the target that may occur when the small molecule binds to it. Semi-empirical, ab initio quantum chemistry methods, or density functional theory are often used to provide optimized parameters for the molecular mechanics calculations and also provide an estimate of the electronic properties (electrostatic potential, polarizability, etc.) of the drug candidate that will influence binding affinity.

Molecular mechanics methods may also be used to provide semi-quantitative prediction of the binding affinity. Also, knowledge-based scoring function may be used to provide binding affinity estimates. These methods use linear regression, machine learning, neural nets or other statistical techniques to derive predictive binding affinity equations by fitting experimental affinities to computationally derived interaction energies between the small molecule and the target.

Ideally, the computational method will be able to predict affinity before a compound is synthesized and hence in theory only one compound needs to be synthesized, saving enormous time and cost. The reality is that present computational methods are imperfect and provide, at best, only qualitatively accurate estimates of affinity. In practice, it requires several iterations of design, synthesis, and testing before an optimal drug is discovered. Computational methods have accelerated discovery by reducing the number of iterations required and have often provided novel structures.

Computer-aided drug design may be used at any of the following stages of drug discovery:

1. hit identification using virtual screening (structure- or ligand-based design)
2. hit-to-lead optimization of affinity and selectivity (structure-based design, QSAR, etc.)
3. lead optimization of other pharmaceutical properties while maintaining affinity

In order to overcome the insufficient prediction of binding affinity calculated by recent scoring functions, the protein-ligand interaction and compound 3D structure information are used for analysis. For structure-based drug design, several post-screening analyses focusing on protein-ligand interaction have been developed for improving enrichment and effectively mining potential candidates:

- Consensus scoring
  - Selecting candidates by voting of multiple scoring functions
  - May lose the relationship between protein-ligand structural information and scoring criterion
- Cluster analysis
  - Represent and cluster candidates according to protein-ligand 3D information
  - Needs meaningful representation of protein-ligand interactions.

## Types

There are two major types of drug design. The first is referred to as ligand-based drug design and the second, structure-based drug design.

### Ligand-based

Ligand-based drug design (or *indirect drug design*) relies on knowledge of other molecules that bind to the biological target of interest. These other molecules may be used to derive a pharmacophore model that defines the minimum necessary structural characteristics a molecule must possess in order to bind to the target. A model of the biological target may be built based on the knowledge of what binds to it, and this model in turn may be used to design new molecular entities that interact with the target. Alternatively, a quantitative structure-activity relationship (QSAR), in which a correlation between calculated properties of molecules and their experimentally determined biological activity, may be derived. These QSAR relationships in turn may be used to predict the activity of new analogs.

### Structure-based

Structure-based drug design (or *direct drug design*) relies on knowledge of the three dimensional structure of the biological target obtained through methods such as x-ray crystallography or NMR spectroscopy. If an experimental structure of a target is not available, it may be possible to create a homology model of the target based on the experimental structure of a related protein. Using the structure of the biological target, candidate drugs that are predicted to bind with high affinity and selectivity to the target may be designed using interactive graphics and the intuition of a medicinal chemist. Alternatively, various automated computational procedures may be used to suggest new drug candidates.

Current methods for structure-based drug design can be divided roughly into three main categories. The first method is identification of new ligands for a given receptor by searching large databases of 3D structures of small molecules to find those fitting the binding pocket of the receptor using fast approximate docking programs. This method is known as virtual screening.

A second category is de novo design of new ligands. In this method, ligand molecules are built up within the constraints of the binding pocket by assembling small pieces in a stepwise manner. These pieces can be either individual atoms or molecular fragments. The key advantage of such a method is that novel structures, not contained in any database, can be suggested. A third method is the optimization of known ligands by evaluating proposed analogs within the binding cavity.

#### Binding site identification

Binding site identification is the first step in structure based design. If the structure of the target or a sufficiently similar homolog is determined in the presence of a bound ligand, then the ligand should be observable in the structure in which case location of the binding site is trivial. However, there may be unoccupied allosteric binding sites that may be of interest. Furthermore, it may be that only apoprotein (protein without ligand) structures are available and the reliable identification of unoccupied sites that have the potential to bind ligands with high affinity is non-trivial. In brief, binding site identification usually relies on identification of concave surfaces on the protein that can accommodate drug sized molecules that also possess appropriate "hot spots" (hydrophobic surfaces, hydrogen bonding sites, etc.) that drive ligand binding.

#### Scoring functions

Structure-based drug design attempts to use the structure of proteins as a basis for designing new ligands by applying the principles of molecular recognition. Selective high affinity binding to the target is generally desirable since it leads to more efficacious drugs with fewer side effects. Thus, one of the most important principles for designing or obtaining potential new ligands is to predict the binding affinity of a certain ligand to its target (and known antitargets) and use the predicted affinity as a criterion for selection.

One early general-purposed empirical scoring function to describe the binding energy of ligands to receptors was developed by Böhm. This empirical scoring function took the form:

$\Delta G_{\text{bind}}=\Delta G_{\text{0}}+\Delta G_{\text{hb}}\Sigma _{h-bonds}+\Delta G_{\text{ionic}}\Sigma _{ionic-int}+\Delta G_{\text{lipophilic}}\left\vert A\right\vert +\Delta G_{\text{rot}}{\mathit {NROT}}$

where:

- ΔG0 – empirically derived offset that in part corresponds to the overall loss of translational and rotational entropy of the ligand upon binding.
- ΔGhb – contribution from hydrogen bonding
- ΔGionic – contribution from ionic interactions
- ΔGlip – contribution from lipophilic interactions where |Alipo| is surface area of lipophilic contact between the ligand and receptor
- ΔGrot – entropy penalty due to freezing a rotatable in the ligand bond upon binding

A more general thermodynamic "master" equation is as follows:

${\begin{array}{lll}\Delta G_{\text{bind}}=-RT\ln K_{\text{d}}\\[1.3ex]K_{\text{d}}={\dfrac {[{\text{Ligand}}][{\text{Receptor}}]}{[{\text{Complex}}]}}\\[1.3ex]\Delta G_{\text{bind}}=\Delta G_{\text{desolvation}}+\Delta G_{\text{motion}}+\Delta G_{\text{configuration}}+\Delta G_{\text{interaction}}\end{array}}$

where:

- desolvation – enthalpic penalty for removing the ligand from solvent
- motion – entropic penalty for reducing the degrees of freedom when a ligand binds to its receptor
- configuration – conformational strain energy required to put the ligand in its "active" conformation
- interaction – enthalpic gain for "resolvating" the ligand with its receptor

The basic idea is that the overall binding free energy can be decomposed into independent components that are known to be important for the binding process. Each component reflects a certain kind of free energy alteration during the binding process between a ligand and its target receptor. The Master Equation is the linear combination of these components. According to Gibbs free energy equation, the relation between dissociation equilibrium constant, Kd, and the components of free energy was built.

Various computational methods are used to estimate each of the components of the master equation. For example, the change in polar surface area upon ligand binding can be used to estimate the desolvation energy. The number of rotatable bonds frozen upon ligand binding is proportional to the motion term. The configurational or strain energy can be estimated using molecular mechanics calculations. Finally the interaction energy can be estimated using methods such as the change in non polar surface, statistically derived potentials of mean force, the number of hydrogen bonds formed, etc. In practice, the components of the master equation are fit to experimental data using multiple linear regression. This can be done with a diverse training set including many types of ligands and receptors to produce a less accurate but more general "global" model or a more restricted set of ligands and receptors to produce a more accurate but less general "local" model.

## Examples

A particular example of rational drug design involves the use of three-dimensional information about biomolecules obtained from such techniques as X-ray crystallography and NMR spectroscopy. Computer-aided drug design in particular becomes much more tractable when there is a high-resolution structure of a target protein bound to a potent ligand. This approach to drug discovery is sometimes referred to as structure-based drug design. The first unequivocal example of the application of structure-based drug design leading to an approved drug is the carbonic anhydrase inhibitor dorzolamide, which was approved in 1995.

Another case study in rational drug design is imatinib, a tyrosine kinase inhibitor designed specifically for the *bcr-abl* fusion protein that is characteristic for Philadelphia chromosome-positive leukemias (chronic myelogenous leukemia and occasionally acute lymphocytic leukemia). Imatinib is substantially different from previous drugs for cancer, as most agents of chemotherapy simply target rapidly dividing cells, not differentiating between cancer cells and other tissues.

Additional examples include:

- Many of the atypical antipsychotics
- Cimetidine, the prototypical H2-receptor antagonist from which the later members of the class were developed
- Selective COX-2 inhibitor NSAIDs
- Enfuvirtide, a peptide HIV entry inhibitor
- Nonbenzodiazepines like zolpidem and zopiclone
- Raltegravir, an HIV integrase inhibitor
- SSRIs (selective serotonin reuptake inhibitors), a class of antidepressants
- Zanamivir, an antiviral drug

## Drug screening

Types of drug screening include phenotypic screening, high-throughput screening, and virtual screening. Phenotypic screening is characterized by the process of screening drugs using cellular or animal disease models to identify compounds that alter the phenotype and produce beneficial disease-related effects. Emerging technologies in high-throughput screening substantially enhance processing speed and decrease the required detection volume. Virtual screening is completed by computer, enabling a large number of molecules can be screened with a short cycle and low cost. Virtual screening uses a range of computational methods that empower chemists to reduce extensive virtual libraries into more manageable sizes.

## Case studies

- 5-HT3 antagonists
- Acetylcholine receptor agonists
- Angiotensin receptor antagonists
- Bcr-Abl tyrosine-kinase inhibitors
- Cannabinoid receptor antagonists
- CCR5 receptor antagonists
- Cyclooxygenase 2 inhibitors
- Dipeptidyl peptidase-4 inhibitors
- HIV protease inhibitors
- NK1 receptor antagonists
- Non-nucleoside reverse transcriptase inhibitors
- Nucleoside and nucleotide reverse transcriptase inhibitors
- PDE5 inhibitors
- Proton pump inhibitors
- Renin inhibitors
- Triptans
- TRPV1 antagonists
- c-Met inhibitors

## Criticism

It has been argued that the highly rigid and focused nature of rational drug design suppresses serendipity in drug discovery.
