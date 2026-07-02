---
title: "Threading (protein sequence)"
source: https://en.wikipedia.org/wiki/Threading_(protein_sequence)
domain: alphafold-prediction
license: CC-BY-SA-4.0
tags: protein structure prediction, deep learning fold, contact map, homology
fetched: 2026-07-02
---

# Threading (protein sequence)

In molecular biology, **protein threading**, also known as **fold recognition**, is a method of protein modeling which is used to model those proteins which have the same fold as proteins of known structures, but do not have homologous proteins with known structure. It differs from the homology modeling method of structure prediction as it (protein threading) is used for proteins which do not have their homologous protein structures deposited in the Protein Data Bank (PDB), whereas homology modeling is used for those proteins which do. Threading works by using statistical knowledge of the relationship between the structures deposited in the PDB and the sequence of the protein which one wishes to model.

The prediction is made by "threading" (i.e. placing, aligning) each amino acid in the target sequence to a position in the template structure, and evaluating how well the target fits the template. After the best-fit template is selected, the structural model of the sequence is built based on the alignment with the chosen template. Protein threading is based on two basic observations: that the number of different folds in nature is fairly small (approximately 1300); and that 90% of the new structures submitted to the PDB in the past three years have similar structural folds to ones already in the PDB.

## Classification of protein structure

The Structural Classification of Proteins database (SCOP) provides a detailed and comprehensive description of the structural and evolutionary relationships of known structure. Proteins are classified to reflect both structural and evolutionary relatedness. Many levels exist in the hierarchy, but the principal levels are family, superfamily, and fold:

- Family (clear evolutionary relationship): Proteins clustered together into families are clearly evolutionarily related. Generally, this means that pairwise residue identities between the proteins are 30% and greater. However, in some cases similar functions and structures provide definitive evidence of common descent in the absence of high sequence identity; for example, many globins form a family though some members have sequence identities of only 15%.
- Superfamily (probable common evolutionary origin): Proteins that have low sequence identities, but whose structural and functional features suggest that a common evolutionary origin is probable, are placed together in superfamilies. For example, actin, the ATPase domain of the heat shock protein, and hexokinase together form a superfamily.
- Fold (major structural similarity): Proteins are defined as having a common fold if they have the same major secondary structures in the same arrangement and with the same topological connections. Different proteins with the same fold often have peripheral elements of secondary structure and turn regions that differ in size and conformation. In some cases, these differing peripheral regions may comprise half the structure. Proteins placed together in the same fold category may not have a common evolutionary origin: the structural similarities could arise just from the physics and chemistry of proteins favoring certain packing arrangements and chain topologies.

### Method

A general paradigm of protein threading consists of the following four steps:

1. The construction of a structure template database: Select protein structures from the protein structure databases as structural templates. This generally involves selecting protein structures from databases such as Protein Data Bank (PDB), Families of Structurally Similar Proteins database (FSSP), Structural Classification of Proteins database (SCOP), or CATH database, after removing protein structures with high sequence similarities.
2. The design of the scoring function: Design a good scoring function to measure the fitness between target sequences and templates based on the knowledge of the known relationships between the structures and the sequences. A good scoring function should contain mutation potential, environment fitness potential, pairwise potential, secondary structure compatibilities, and gap penalties. The quality of the energy function is closely related to the prediction accuracy, especially the alignment accuracy.
3. Threading alignment: Align the target sequence with each of the structure templates by optimizing the designed scoring function. This step is one of the major tasks of all threading-based structure prediction programs that take into account the pairwise contact potential; otherwise, a dynamic programming algorithm can fulfill it.
4. Threading prediction: Select the threading alignment that is statistically most probable as the threading prediction. Then construct a structure model for the target by placing the backbone atoms of the target sequence at their aligned backbone positions of the selected structural template.

### Comparison with homology modeling

Homology modeling and protein threading are both template-based methods and there is no rigorous boundary between them in terms of prediction techniques. But the protein structures of their targets are different. Homology modeling is for those targets which have homologous proteins with known structure (usually/maybe of same family), while protein threading is for those targets with only fold-level homology found. In other words, homology modeling is for "easier" targets and protein threading is for "harder" targets.

Homology modeling treats the template in an alignment as a sequence, and only sequence homology is used for prediction. Protein threading treats the template in an alignment as a structure, and both sequence and structure information extracted from the alignment are used for prediction. When there is no significant homology found, protein threading can make a prediction based on the structure information. That also explains why protein threading may be more effective than homology modeling in many cases.

In practice, when the sequence identity in a sequence sequence alignment is low (i.e. <25%), homology modeling may not produce a significant prediction. In this case, if there is distant homology found for the target, protein threading can generate a good prediction.

### More about threading

Fold recognition methods can be broadly divided into two types: those that derive a 1-D profile for each structure in the fold library and align the target sequence to these profiles; and those that consider the full 3-D structure of the protein template. A simple example of a profile representation would be to take each amino acid in the structure and simply label it according to whether it is buried in the core of the protein or exposed on the surface. More elaborate profiles might take into account the local secondary structure (e.g. whether the amino acid is part of an alpha helix) or even evolutionary information (how conserved the amino acid is). In the 3-D representation, the structure is modeled as a set of inter-atomic distances, i.e. the distances are calculated between some or all of the atom pairs in the structure. This is a much richer and far more flexible description of the structure, but is much harder to use in calculating an alignment. The profile-based fold recognition approach was first described by Bowie, Lüthy and David Eisenberg in 1991. The term *threading* was first coined by David Jones, William R. Taylor and Janet Thornton in 1992, and originally referred specifically to the use of a full 3-D structure atomic representation of the protein template in fold recognition. Today, the terms threading and fold recognition are frequently (though somewhat incorrectly) used interchangeably.

Fold recognition methods are widely used and effective because it is believed that there are a strictly limited number of different protein folds in nature, mostly as a result of evolution but also due to constraints imposed by the basic physics and chemistry of polypeptide chains. There is, therefore, a good chance (currently 70-80%) that a protein which has a similar fold to the target protein has already been studied by X-ray crystallography or nuclear magnetic resonance (NMR) spectroscopy and can be found in the PDB. Currently there are nearly 1300 different protein folds known, but new folds are still being discovered every year due in significant part to the ongoing structural genomics projects.

Many different algorithms have been proposed for finding the correct threading of a sequence onto a structure, though many make use of dynamic programming in some form. For full 3-D threading, the problem of identifying the best alignment is very difficult (it is an NP-hard problem for some models of threading). Researchers have made use of many combinatorial optimization methods such as conditional random fields, simulated annealing, branch and bound, and linear programming, searching to arrive at heuristic solutions. It is interesting to compare threading methods to methods which attempt to align two protein structures (protein structural alignment), and indeed many of the same algorithms have been applied to both problems.

## Protein threading software

- HHpred is a popular threading server which runs HHsearch, a widely used software for remote homology detection based on pairwise comparison of hidden Markov models.
- RAPTOR is an integer programming based protein threading software. It has been replaced by a new protein threading program RaptorX, which employs probabilistic graphical models and statistical inference to both single template and multi-template based protein threading. RaptorX significantly outperforms RAPTOR and is especially good at aligning proteins with sparse sequence profile. The RaptorX server is free to public.
- Phyre is a popular threading server combining HHsearch with *ab initio* and multiple-template modelling.
- MUSTER is a standard threading algorithm based on dynamic programming and sequence profile-profile alignment. It also combines multiple structural resources to assist the sequence profile alignment.
- SPARKS X is a probabilistic-based sequence-to-structure matching between predicted one-dimensional structural properties of query and corresponding native properties of templates.
- BioShell is a threading algorithm using optimized profile-to-profile dynamic programming algorithm combined with predicted secondary structure.
