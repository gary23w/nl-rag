---
title: "Virtual screening"
source: https://en.wikipedia.org/wiki/Virtual_screening
domain: virtual-screening
license: CC-BY-SA-4.0
tags: in silico screening, compound library, hit identification, chemical space
fetched: 2026-07-02
---

# Virtual screening

**Virtual screening** (**VS**) is a computational technique used in drug discovery to search libraries of small molecules in order to identify those structures which are most likely to bind to a drug target, typically a protein receptor or enzyme.

Virtual screening has been defined as "automatically evaluating very large libraries of compounds" using computer programs. As this definition suggests, VS has largely been a numbers game focusing on how the enormous chemical space of over 1060 conceivable compounds can be filtered to a manageable number that can be synthesized, purchased, and tested. Although searching the entire chemical universe may be a theoretically interesting problem, more practical VS scenarios focus on designing and optimizing targeted combinatorial libraries and enriching libraries of available compounds from in-house compound repositories or vendor offerings. As the accuracy of the method has increased, virtual screening has become an integral part of the drug discovery process. Virtual Screening can be used to select in house database compounds for screening, choose compounds that can be purchased externally, and to choose which compound should be synthesized next.

## Methods

There are two broad categories of screening techniques: ligand-based and structure-based.

### Ligand-based methods

Given a set of structurally diverse ligands that binds to a receptor, a model of the receptor can be built by exploiting the collective information contained in such set of ligands. Different computational techniques explore the structural, electronic, molecular shape, and physicochemical similarities of different ligands that could imply their mode of action against a specific molecular receptor or cell lines. A candidate ligand can then be compared to the pharmacophore model to determine whether it is compatible with it and therefore likely to bind. Different 2D chemical similarity analysis methods have been used to scan a databases to find active ligands. Another popular approach used in ligand-based virtual screening consist on searching molecules with shape similar to that of known actives, as such molecules will fit the target's binding site and hence will be likely to bind the target. There are a number of prospective applications of this class of techniques in the literature. Pharmacophoric extensions of these 3D methods are also freely-available as webservers. Also shape based virtual screening has gained significant popularity.

### Structure-based methods

Structure-based virtual screening approach includes different computational techniques that consider the structure of the receptor that is the molecular target of the investigated active ligands. Some of these techniques include molecular docking, structure-based pharmacophore modelling, and molecular dynamics simulations. Molecular docking is the most used structure-based technique, and it applies a scoring function to estimate the fitness of each ligand against the binding site of the macromolecular receptor, helping to choose the ligands with the most high affinity. Currently, there are some webservers oriented to prospective virtual screening.

### Hybrid methods

Hybrid methods that rely on structural and ligand similarity were also developed to overcome the limitations of traditional VLS approaches. This methodologies utilizes evolution‐based ligand‐binding information to predict small-molecule binders and can employ both global structural similarity and pocket similarity. A global structural similarity based approach employs both an experimental structure or a predicted protein model to find structural similarity with proteins in the PDB holo‐template library. Upon detecting significant structural similarity, 2D fingerprint based Tanimoto coefficient metric is applied to screen for small-molecules that are similar to ligands extracted from selected holo PDB templates. The predictions from this method have been experimentally assessed and shows good enrichment in identifying active small molecules.

The above specified method depends on global structural similarity and is not capable of *a priori* selecting a particular ligand‐binding site in the protein of interest. Further, since the methods rely on 2D similarity assessment for ligands, they are not capable of recognizing stereochemical similarity of small-molecules that are substantially different but demonstrate geometric shape similarity. To address these concerns, a new pocket centric approach, *PoLi,* capable of targeting specific binding pockets in holo‐protein templates, was developed and experimentally assessed.

## Computing infrastructure

The computation of pair-wise interactions between atoms, which is a prerequisite for the operation of many virtual screening programs, scales by $O(N^{2})$ , *N* is the number of atoms in the system. Due to the quadratic scaling, the computational costs increase quickly.

### Ligand-based approach

Ligand-based methods typically require a fraction of a second for a single structure comparison operation. Sometimes a single CPU is enough to perform a large screening within hours. However, several comparisons can be made in parallel in order to expedite the processing of a large database of compounds.

### Structure-based approach

The size of the task requires a parallel computing infrastructure, such as a cluster of Linux systems, running a batch queue processor to handle the work, such as Sun Grid Engine or Torque PBS.

A means of handling the input from large compound libraries is needed. This requires a form of compound database that can be queried by the parallel cluster, delivering compounds in parallel to the various compute nodes. Commercial database engines may be too ponderous, and a high speed indexing engine, such as Berkeley DB, may be a better choice. Furthermore, it may not be efficient to run one comparison per job, because the ramp up time of the cluster nodes could easily outstrip the amount of useful work. To work around this, it is necessary to process batches of compounds in each cluster job, aggregating the results into some kind of log file. A secondary process, to mine the log files and extract high scoring candidates, can then be run after the whole experiment has been run.

## Accuracy

The aim of virtual screening is to identify molecules of novel chemical structure that bind to the macromolecular target of interest. Thus, success of a virtual screen is defined in terms of finding interesting new scaffolds rather than the total number of hits. Interpretations of virtual screening accuracy should, therefore, be considered with caution. Low hit rates of interesting scaffolds are clearly preferable over high hit rates of already known scaffolds.

Most tests of virtual screening studies in the literature are retrospective. In these studies, the performance of a VS technique is measured by its ability to retrieve a small set of previously known molecules with affinity to the target of interest (active molecules or just actives) from a library containing a much higher proportion of assumed inactives or decoys. There are several distinct ways to select decoys by matching the properties of the corresponding active molecule and more recently decoys are also selected in a property-unmatched manner. The actual impact of decoy selection, either for training or testing purposes, has also been discussed.

By contrast, in prospective applications of virtual screening, the resulting hits are subjected to experimental confirmation (e.g., IC50 measurements). There is consensus that retrospective benchmarks are not good predictors of prospective performance and consequently only prospective studies constitute conclusive proof of the suitability of a technique for a particular target.

## Application to drug discovery

Virtual screening is a very useful application when it comes to identifying hit molecules as a beginning for medicinal chemistry. As the virtual screening approach begins to become a more vital and substantial technique within the medicinal chemistry industry the approach has had an expeditious increase.

## Ligand-based methods

Ligand-based methods are applied when the three-dimensional structure of the target receptor is unknown. Instead of modeling ligand–receptor interactions directly, these approaches rely on the structural and physicochemical properties of known active ligands to predict how new compounds may bind.

### Pharmacophore models

A **pharmacophore** is defined as the ensemble of steric and electronic features necessary to ensure optimal supramolecular interactions with a biological target and to trigger (or block) its biological response. These features typically include hydrogen-bond donors and acceptors, hydrophobic regions, aromatic rings, charged groups, and metal-binding functionalities.

Pharmacophore modeling is commonly applied in ligand-based drug design when the three-dimensional structure of the target protein is unknown or when multiple active ligands are available.

The general workflow involves several steps:

1. **Selection of active compounds:**A representative and structurally diverse set of biologically active ligands is selected. Structural diversity is important to ensure that the resulting model captures essential interaction features rather than compound-specific characteristics.
2. **Conformer generation:** Because ligands are flexible, multiple low-energy conformations (conformers) are generated for each molecule. This step aims to approximate the bioactive conformation, which is usually unknown in ligand-based approaches.
3. **Molecular alignment and superposition:** The generated conformers are superimposed to identify common spatial arrangements of key chemical features. By aligning shared pharmacophoric elements across active ligands, a pharmacophore hypothesis is constructed.

Unlike approaches that rely on a single reference structure, pharmacophore modeling integrates information from multiple active compounds. This generally improves robustness and predictive performance, particularly when dealing with chemically diverse ligands.

However, because multiple alignments and feature combinations are possible, pharmacophore modeling does not usually yield a single unique solution. Therefore, generated hypotheses must be validated using external test sets or experimental data.

### Shape-based virtual screening

Shape-based molecular similarity approaches have been established as important and popular virtual screening techniques. At present, the highly optimized screening platform ROCS (Rapid Overlay of Chemical Structures) is considered the de facto industry standard for shape-based, ligand-centric virtual screening. It uses a Gaussian function to define molecular volumes of small organic molecules. The selection of the query conformation is less important, rendering shape-based screening ideal for ligand-based modeling: As the availability of a bioactive conformation for the query is not the limiting factor for screening — it is more the selection of query compound(s) that is decisive for screening performance. Other shape-based molecular similarity methods such as Autodock-SS have also been developed.

### Field-based virtual screening

Field-based virtual screening methods extend shape-based similarity approaches by considering not only molecular shape but also the physicochemical interaction fields that govern ligand–receptor recognition.

Rather than focusing solely on structural overlap, these methods compare molecular interaction potentials, such as

- Electrostatic fields
- Hydrophobic fields
- Steric fields
- Hydrogen-bonding potentials

By evaluating these properties in three-dimensional space, field-based approaches aim to capture the underlying interaction patterns responsible for biological activity, while remaining largely independent of the specific chemical scaffold of the query molecule.

Compared to purely shape-based methods, field-based screening can provide a more nuanced description of molecular similarity, particularly when structurally distinct compounds share similar interaction profiles.

### Quantitative-structure activity relationship

Quantitative Structure–Activity Relationship (QSAR) models are predictive models that relate molecular descriptors to biological activity using a dataset of known active and inactive compounds. In contrast to qualitative structure–activity relationship (SAR) analysis, which identifies trends within structural classes, QSAR provides a quantitative mathematical relationship between molecular properties and measured biological responses.

#### Traditional QSAR methods

Traditional QSAR approaches typically rely on predefined molecular descriptors—such as physicochemical properties, topological indices, or electronic parameters—and apply statistical modeling techniques including:

- Ordinary least squares (OLS)
- Multiple linear regression (MLR)
- Partial least squares (PLS)

These methods assume a linear relationship between descriptors and biological activity. QSAR models are widely used to prioritize compounds in lead discovery and optimization.

#### Machine Learning in QSAR

Machine learning (ML) approaches can be viewed as an extension of QSAR methodology. Like classical QSAR models, ML-based methods use molecular descriptors or structural representations (such as molecular fingerprint, graphs) as input features. However, they employ more flexible algorithms capable of modeling nonlinear and complex relationships between molecular structure and biological activity.

In supervised learning, models are trained on datasets composed of known active and inactive compounds (or compounds with measured activity values). The trained model is then used to predict the activity or probability of activity for new compounds.

Common machine learning algorithms applied in virtual screening include:

- Decision trees
- Support vector machines (SVM)
- Random forests
- k-Nearest neighbors (k-NN)
- Artificial neural networks

These models typically output either:

- A predicted activity value (regression), or
- A probability that a compound is active (classification), which can then be used for ranking in virtual screening.

## Structure-based methods

Structure-based methods rely on the three-dimensional structure of the biological target, typically obtained from X-ray crystallography, NMR spectroscopy, or cryo-electron microscopy. Unlike ligand-based approaches, these methods explicitly model the interactions between a ligand and the binding site of a receptor.

### Pharmacophore models

In structure-based pharmacophore modeling, pharmacophoric features are derived directly from the three-dimensional structure of the target binding site, rather than from a set of known active ligands.

Key interaction features - such as hydrogen-bond donors and acceptors, hydrophobic regions, charged residues, and metal-binding sites - are identified based on the spatial arrangement of amino acid residues within the binding pocket. If a protein–ligand complex structure is available, pharmacophoric features can also be extracted from the observed ligand–receptor interactions.

The resulting pharmacophore model represents the essential interaction pattern required for binding and can be used to screen compound libraries.

### Molecular docking

Molecular docking aims to predict the binding mode (pose) and, in some cases, the binding affinity of a ligand within the active site of a target protein.

Docking involves two main components:

1. **Search algorithm** – explores possible orientations and conformations of the ligand within the binding pocket.
2. **Scoring function** – estimates the strength of the ligand–receptor interaction and ranks predicted poses accordingly.

The goal is to identify the most probable binding pose for a given ligand and to prioritize compounds based on their predicted binding affinity.

### Co-folding methods

Co-folding methods predict the structure of a protein–ligand complex by modeling the receptor and ligand simultaneously, allowing conformational adaptation during binding. Unlike classical docking, which typically treats the receptor as rigid or semi-flexible, co-folding approaches aim to capture induced-fit effects more explicitly.

Recent deep learning–based frameworks such as **Boltz-2** exemplify this strategy by predicting bound complex structures directly from sequence and ligand information. Although such approaches are computationally more demanding than traditional docking, they hold promise for refining binding poses, improving structural accuracy, and enhancing structure-based virtual screening workflows, particularly for flexible or challenging targets.
