---
title: "Docking (molecular)"
source: https://en.wikipedia.org/wiki/Docking_(molecular)
domain: molecular-docking
license: CC-BY-SA-4.0
tags: molecular docking, virtual screening, structure-based drug design, scoring function docking
fetched: 2026-07-02
---

# Docking (molecular)

| Docking glossary |
|---|
| Receptor**or**host**or**lock The "receiving" molecule, most commonly a protein or other biopolymer. Ligand**or**guest**or**key The complementary partner molecule which binds to the receptor. Ligands are most often small molecules but could also be another biopolymer. Docking Computational simulation of a candidate ligand binding to a receptor. Binding mode The orientation of the ligand relative to the receptor as well as the conformation of the ligand and receptor when bound to each other. Pose A candidate binding mode. Scoring The process of evaluating a particular pose by counting the number of favorable intermolecular interactions such as hydrogen bonds and hydrophobic contacts. Ranking The process of classifying which ligands are most likely to interact favorably to a particular receptor based on the predicted free-energy of binding. Docking assessment (DA) Procedure to quantify the predictive capability of a docking protocol. |
|   |

In the field of molecular modeling, **docking** is a method which predicts the preferred orientation of one molecule to a second when a ligand and a target are bound to each other to form a stable complex. Knowledge of the preferred orientation in turn may be used to predict the strength of association or binding affinity between two molecules using, for example, scoring functions.

The associations between biologically relevant molecules such as proteins, peptides, nucleic acids, carbohydrates, and lipids play a central role in signal transduction. Furthermore, the relative orientation of the two interacting partners may affect the type of signal produced (e.g., agonism vs antagonism). Therefore, docking is useful for predicting both the strength and type of signal produced.

Molecular docking is one of the most frequently used methods in structure-based drug design, due to its ability to predict the binding-conformation of small molecule ligands to the appropriate target binding site. Characterisation of the binding behaviour plays an important role in rational design of drugs as well as to elucidate fundamental biochemical processes. Hence, docking is useful to discover new ligand for a target by screening large virtual compound libraries and as a start for ligand optimization or investigation of mechanism of action.

## Definition of problem

One can think of molecular docking as a problem of *"lock-and-key"*, in which one wants to find the correct relative orientation of the *"key"* which will open up the *"lock"* (where on the surface of the lock is the key hole, which direction to turn the key after it is inserted, etc.). Here, the protein can be thought of as the "lock" and the ligand can be thought of as a "key". Molecular docking may be defined as an optimization problem, which would describe the "best-fit" orientation of a ligand that binds to a particular protein of interest. However, since both the ligand and the protein are flexible, a *"hand-in-glove"* analogy is more appropriate than *"lock-and-key"*. During the course of the docking process, the ligand and the protein adjust their conformation to achieve an overall "best-fit" and this kind of conformational adjustment resulting in the overall binding is referred to as **"induced-fit"**.

Molecular docking research focuses on computationally simulating the molecular recognition process. It aims to achieve an optimized conformation for both the protein and ligand and relative orientation between protein and ligand such that the free energy of the overall system is minimized.

## Docking approaches

Two approaches are particularly popular within the molecular docking community.

- One approach uses a matching technique that describes the protein and the ligand as complementary surfaces.
- The second approach simulates the actual docking process in which the ligand-protein pairwise interaction energies are calculated.

Both approaches have significant advantages as well as some limitations. These are outlined below.

### Shape complementarity

Geometric matching/shape complementarity methods describe the protein and ligand as a set of features that make them dockable. These features may include molecular surface/complementary surface descriptors. In this case, the receptor's molecular surface is described in terms of its solvent-accessible surface area and the ligand's molecular surface is described in terms of its matching surface description. The complementarity between the two surfaces amounts to the shape matching description that may help finding the complementary pose of docking the target and the ligand molecules. Another approach is to describe the hydrophobic features of the protein using turns in the main-chain atoms. Yet another approach is to use a Fourier shape descriptor technique. Whereas the shape complementarity based approaches are typically fast and robust, they cannot usually model the movements or dynamic changes in the ligand/protein conformations accurately, although recent developments allow these methods to investigate ligand flexibility. Shape complementarity methods can quickly scan through several thousand ligands in a matter of seconds and actually figure out whether they can bind at the protein's active site, and are usually scalable to even protein-protein interactions. They are also much more amenable to pharmacophore based approaches, since they use geometric descriptions of the ligands to find optimal binding.

### Simulation

Simulating the docking process is much more complicated. In this approach, the protein and the ligand are separated by some physical distance, and the ligand finds its position into the protein's active site after a certain number of "moves" in its conformational space. The moves incorporate rigid body transformations such as translations and rotations, as well as internal changes to the ligand's structure including torsion angle rotations. Each of these moves in the conformation space of the ligand induces a total energetic cost of the system. Hence, the system's total energy is calculated after every move.

The obvious advantage of docking simulation is that ligand flexibility is easily incorporated, whereas shape complementarity techniques must use ingenious methods to incorporate flexibility in ligands. Also, it more accurately models reality, whereas shape complementary techniques are more of an abstraction.

Clearly, simulation is computationally expensive, having to explore a large energy landscape. Grid-based techniques, optimization methods, and increased computer speed have made docking simulation more realistic.

## Mechanics of docking

To perform a docking screen, the first requirement is a structure of the protein of interest. Usually the structure has been determined using a biophysical technique such as

- X-ray crystallography,
- NMR spectroscopy or
- Cryo-electron microscopy (cryo-EM),

but can also derive from homology modeling construction or from AlphaFold predictions. This protein structure and a database of potential ligands serve as inputs to a docking program. The success of a docking program depends on two components: the search algorithm and the scoring function.

The search space in theory consists of all possible orientations and conformations of the protein paired with the ligand. However, in practice with current computational resources, it is impossible to exhaustively explore the search space — this would involve enumerating all possible distortions of each molecule (molecules are dynamic and exist in an ensemble of conformational states) and all possible rotational and translational orientations of the ligand relative to the protein at a given level of granularity. Most docking programs in use account for the whole conformational space of the ligand (flexible ligand), and several attempt to model a flexible protein receptor. Each "snapshot" of the pair is referred to as a **pose**.

A variety of conformational search strategies have been applied to the ligand and to the receptor. These include:

- systematic or stochastic torsional searches about rotatable bonds
- molecular dynamics simulations
- genetic algorithms to "evolve" new low energy conformations and where the score of each pose acts as the fitness function used to select individuals for the next iteration.

#### Ligand flexibility

Conformations of the ligand may be generated in the absence of the receptor and subsequently docked or conformations may be generated on-the-fly in the presence of the receptor binding cavity, or with full rotational flexibility of every dihedral angle using fragment based docking. Force field energy evaluation are most often used to select energetically reasonable conformations, but knowledge-based methods have also been used.

Peptides are both highly flexible and relatively large-sized molecules, which makes modeling their flexibility a challenging task. A number of methods were developed to allow for efficient modeling of flexibility of peptides during protein-peptide docking.

#### Receptor flexibility

Computational capacity has increased dramatically over the last decade making possible the use of more sophisticated and computationally intensive methods in computer-assisted drug design. However, dealing with receptor flexibility in docking methodologies is still a thorny issue. The main reason behind this difficulty is the large number of degrees of freedom that have to be considered in this kind of calculations. Neglecting it, however, in some of the cases may lead to poor docking results in terms of binding pose prediction.

Multiple static structures experimentally determined for the same protein in different conformations are often used to emulate receptor flexibility. Alternatively rotamer libraries of amino acid side chains that surround the binding cavity may be searched to generate alternate but energetically reasonable protein conformations.

### Scoring function

Docking programs generate a large number of potential ligand poses, of which some can be immediately rejected due to clashes with the protein. The remainder are evaluated using some scoring function, which takes a pose as input and returns a number indicating the likelihood that the pose represents a favorable binding interaction and ranks one ligand relative to another.

Most scoring functions are physics-based molecular mechanics force fields that estimate the energy of the pose within the binding site. The various contributions to binding can be written as an additive equation:

$\bigtriangleup G_{bind}=\bigtriangleup G_{solvent}+\bigtriangleup G_{conf}+\bigtriangleup G_{int}+\bigtriangleup G_{rot}+\bigtriangleup G_{t/t}+\bigtriangleup G_{vib}$

The components consist of solvent effects, conformational changes in the protein and ligand, free energy due to protein-ligand interactions, internal rotations, association energy of ligand and receptor to form a single complex and free energy due to changes in vibrational modes. A low (negative) energy indicates a stable system and thus a likely binding interaction.

Alternative approaches use modified scoring functions to include constraints based on known key protein-ligand interactions, or knowledge-based potentials derived from interactions observed in large databases of protein-ligand structures (e.g. the Protein Data Bank).

There are a large number of structures from X-ray crystallography for complexes between proteins and high affinity ligands, but comparatively fewer for low affinity ligands as the latter complexes tend to be less stable and therefore more difficult to crystallize. Scoring functions trained with this data can dock high affinity ligands correctly, but they will also give plausible docked conformations for ligands that do not bind. This gives a large number of false positive hits, i.e., ligands predicted to bind to the protein that actually don't when placed together in a test tube.

One way to reduce the number of false positives is to recalculate the energy of the top scoring poses using (potentially) more accurate but computationally more intensive techniques such as Generalized Born or Poisson-Boltzmann methods.

## Docking assessment

The interdependence between sampling and scoring function affects the docking capability in predicting plausible poses or binding affinities for novel compounds. Thus, an assessment of a docking protocol is generally required (when experimental data is available) to determine its predictive capability. Docking assessment can be performed using different strategies, such as:

- docking accuracy (DA) calculation;
- the correlation between a docking score and the experimental response or determination of the enrichment factor (EF);
- the distance between an ion-binding moiety and the ion in the active site;
- the presence of induce-fit models.

### Docking accuracy

Docking accuracy represents one measure of a docking program's ability to reproduce the experimentally observed binding pose of a ligand. Fitness is typically quantified by calculating the root-mean-square deviation (RMSD) of the non-hydrogen atoms between the docked pose and the experimental structure.

An RMSD value below 2.0 Å is commonly considered indicative of a successful docking model. However, because RMSD generally increases with the number of heavy atoms in the ligand, a more permissive cutoff may be appropriate for larger molecules.

Importantly, RMSD alone should not be used to evaluate docking quality. A comprehensive assessment should also consider the program's ability to reproduce key ligand–receptor interactions and the plausibility of the generated conformations. This is particularly relevant when using deep-learning–based molecular docking approaches.

### Enrichment factor

Docking screens can be evaluated based on their ability to enrich known active ligands from a large database of presumed non-binding "decoy" molecules. In this approach, the performance of a docking protocol is assessed by its capacity to rank a small number of known active compounds within the top fraction of screened molecules, despite the presence of a much larger number of decoys.

The enrichment factor (EF) quantifies this early recognition capability. It is defined as:

$EF_{x}={\frac {N_{\text{active x}}/N_{x}}{N_{\text{active total}}/N_{\text{total}}}}$

where:

- Nactive x is the number of active compounds found in the top x% of the ranked list,
- NX is the number of molecules in the top x% of the ranked list,
- Nactive total is the total number of active compounds in the dataset,
- Ntotal is the total number of molecules in the dataset.

Thus, EF compares the fraction of actives retrieved in the top-ranked subset to the fraction expected by random selection. An EF value greater than 1 indicates enrichment beyond random performance.

In particular, **EF1%** measures enrichment within the top 1% of the ranked database and is commonly used to evaluate early recognition performance in virtual screening, where identifying active compounds at the very top of the list is especially important.

In addition to EF, the area under the receiver operating characteristic (ROC) curve (AUC) is widely used to evaluate screening performance across the entire ranked list.

### Prospective

Resulting hits from docking screens are subjected to pharmacological validation (e.g. IC50, affinity or potency measurements). Only prospective studies constitute conclusive proof of the suitability of a technique for a particular target. In the case of G protein-coupled receptors (GPCRs), which are targets of more than 30% of marketed drugs, molecular docking led to the discovery of more than 500 GPCR ligands.

### Benchmarking

The potential of docking programs to reproduce binding modes as determined by X-ray crystallography can be assessed by a range of docking benchmark sets.

For small molecules, several benchmark data sets for docking and virtual screening exist e.g. *Astex Diverse Set* consisting of high quality protein−ligand X-ray crystal structures, the *Directory of Useful Decoys* (DUD) for evaluation of virtual screening performance, the *LEADS-FRAG* data set for fragments, and the *LIT-PCBA* data set for machine-learning and virtual screening.

In addition to dataset development, large-scale comparative assessments have been conducted. The Comparative Assessment of Scoring Functions (CASF) provides systematic benchmarking of docking and scoring functions using standardized protein–ligand complexes. CASF evaluates multiple aspects of performance, including docking power (pose prediction), scoring power (binding affinity prediction), ranking power, and screening power. Results from CASF studies have highlighted substantial variability among docking programs and scoring functions, emphasizing that no single method consistently outperforms others across all evaluation criteria.

An evaluation of docking programs for their potential to reproduce peptide binding modes can be assessed by *Lessons for Efficiency Assessment of Docking and Scoring* (LEADS-PEP).

## Applications

A binding interaction between a small molecule ligand and an enzyme protein may result in activation or inhibition of the enzyme. If the protein is a receptor, ligand binding may result in agonism or antagonism. Docking is most commonly used in the field of drug design — most drugs are small organic molecules, and docking may be applied to:

- hit identification – docking combined with a scoring function can be used to quickly screen large databases of potential drugs in silico to identify molecules that are likely to bind to protein target of interest (see virtual screening). Reverse pharmacology routinely uses docking for target identification.
- lead optimization – docking can be used to predict in where and in which relative orientation a ligand binds to a protein (also referred to as the binding mode or pose). This information may in turn be used to design more potent and selective analogs.
- bioremediation – protein ligand docking can also be used to predict pollutants that can be degraded by enzymes.
