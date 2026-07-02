---
title: "Substitution matrix"
source: https://en.wikipedia.org/wiki/Substitution_matrix
domain: sequence-alignment
license: CC-BY-SA-4.0
tags: sequence alignment, multiple sequence alignment, substitution matrix, gap penalty
fetched: 2026-07-02
---

# Substitution matrix

In bioinformatics and evolutionary biology, a **substitution matrix** describes the frequency at which a character in a nucleotide sequence or a protein sequence changes to other character states over evolutionary time. The information is often in the form of log odds of finding two specific character states aligned and depends on the assumed number of evolutionary changes or sequence dissimilarity between compared sequences. It is an application of a stochastic matrix. Substitution matrices are usually seen in the context of amino acid or DNA sequence alignments, where they are used to calculate similarity scores between the aligned sequences.

## Background

In the process of evolution, from one generation to the next the amino acid sequences of an organism's proteins are gradually altered through the action of DNA mutations. For example, the sequence

```
ALEIRYLRD
```

could mutate into the sequence

```
ALEINYLRD
```

in one step, and possibly

```
AQEINYQRD
```

over a longer period of evolutionary time. Each amino acid is more or less likely to mutate into various other amino acids. For instance, a hydrophilic residue such as arginine is more likely to be replaced by another hydrophilic residue such as glutamine, than it is to be mutated into a hydrophobic residue such as leucine. (Here, a residue refers to an amino acid stripped of a hydrogen and/or a hydroxyl group and inserted in the polymeric chain of a protein.) This is primarily due to redundancy in the genetic code, which translates similar codons into similar amino acids. Furthermore, mutating an amino acid to a residue with significantly different properties could affect the folding and/or activity of the protein. This type of disruptive substitution is likely to be removed from populations by the action of purifying selection because the substitution has a higher likelihood of rendering a protein nonfunctional.

If we have two amino acid sequences in front of us, we should be able to say something about how likely they are to be derived from a common ancestor, or homologous. If we can line up the two sequences using a sequence alignment algorithm such that the mutations required to transform a hypothetical ancestor sequence into both of the current sequences would be evolutionarily plausible, then we'd like to assign a high score to the comparison of the sequences.

To this end, we will construct a 20x20 matrix where the $(i,j)$ th entry is equal to the probability of the i th amino acid being transformed into the j th amino acid in a certain amount of evolutionary time. There are many different ways to construct such a matrix, called a **substitution matrix**. Here are the most commonly used ones:

## Identity matrix

The simplest possible substitution matrix would be one in which each amino acid is considered maximally similar to itself, but not able to transform into any other amino acid. This matrix would look like

${\begin{bmatrix}1&0&\cdots &0&0\\0&1&&0&0\\\vdots &&\ddots &&\vdots \\0&0&&1&0\\0&0&\cdots &0&1\end{bmatrix}}$

This identity matrix will succeed in the alignment of very similar amino acid sequences but will be miserable at aligning two distantly related sequences. We need to figure out all the probabilities in a more rigorous fashion. It turns out that an empirical examination of previously aligned sequences works best.

## Log-odds matrices

We express the probabilities of transformation in what are called log-odds scores. The scores matrix S is defined as

$S_{i,j}=\log {\frac {p_{i}\cdot M_{i,j}}{p_{i}\cdot p_{j}}}=\log {\frac {M_{i,j}}{p_{j}}}=\log {\frac {\text{observed frequency}}{\text{expected frequency}}},$

where $M_{i,j}$ is the probability that amino acid i transforms into amino acid j , and $p_{i}$ , $p_{j}$ are the frequencies of amino acids *i* and *j*. The base of the logarithm is not important, and the same substitution matrix is often expressed in different bases.

## Example amino-acid matrices

### PAM

One of the first amino acid substitution matrices, the PAM *(Point Accepted Mutation)* matrix was developed by Margaret Dayhoff in the 1970s. This matrix is calculated by observing the differences in closely related proteins. Because the use of very closely related homologs, the observed mutations are not expected to significantly change the common functions of the proteins. Thus the observed substitutions (by point mutations) are considered to be accepted by natural selection.

One PAM unit is defined as 1% of the amino acid positions that have been changed. To create a PAM1 substitution matrix, a group of very closely related sequences with mutation frequencies corresponding to one PAM unit is chosen. Based on collected mutational data from this group of sequences, a substitution matrix can be derived. This PAM1 matrix estimates what rate of substitution would be expected if 1% of the amino acids had changed.

The PAM1 matrix is used as the basis for calculating other matrices by assuming that repeated mutations would follow the same pattern as those in the PAM1 matrix, and multiple substitutions can occur at the same site. With this assumption, the PAM2 matrix can estimated by squaring the probabilities. Using this logic, Dayhoff derived matrices as high as PAM250. Usually the PAM 30 and the PAM70 are used.

### BLOSUM

Dayhoff's methodology of comparing closely related species turned out not to work very well for aligning evolutionarily divergent sequences. Sequence changes over long evolutionary time scales are not well approximated by compounding small changes that occur over short time scales. The BLOSUM *(BLOck SUbstitution Matrix)* series of matrices rectifies this problem. Henikoff & Henikoff constructed these matrices using multiple alignments of evolutionarily divergent proteins. The probabilities used in the matrix calculation are computed by looking at "blocks" of conserved sequences found in multiple protein alignments. These conserved sequences are assumed to be of functional importance within related proteins and will therefore have lower substitution rates than less conserved regions. To reduce bias from closely related sequences on substitution rates, segments in a block with a sequence identity above a certain threshold were clustered, reducing the weight of each such cluster (Henikoff and Henikoff). For the BLOSUM62 matrix, this threshold was set at 62%. Pairs frequencies were then counted between clusters, hence pairs were only counted between segments less than 62% identical. One would use a higher numbered BLOSUM matrix for aligning two closely related sequences and a lower number for more divergent sequences.

It turns out that the BLOSUM62 matrix does an excellent job detecting similarities in distant sequences, and this is the matrix used by default in most recent alignment applications such as BLAST.

It also turns out the BLOSUM computer code written by Henikoff and Henikoff does not exactly match the description in their paper. Surprisingly, this commonly used "wrong" version has better search performance.

### Differences between PAM and BLOSUM

1. PAM matrices are based on an explicit evolutionary model (i.e. replacements are counted on the branches of a phylogenetic tree: maximum parismony), whereas the BLOSUM matrices are based on an implicit model of evolution.
2. The PAM matrices are based on mutations observed throughout a global alignment, this includes both highly conserved and highly mutable regions. The BLOSUM matrices are based only on highly conserved regions in series of alignments forbidden to contain gaps.
3. The method used to count the replacements is different: unlike the PAM matrix, the BLOSUM procedure uses groups of sequences within which not all mutations are counted the same.
4. Higher numbers in the PAM matrix naming scheme denote larger evolutionary distance, while larger numbers in the BLOSUM matrix naming scheme denote higher sequence similarity and therefore smaller evolutionary distance. Example: PAM150 is used for more distant sequences than PAM100; BLOSUM62 is used for closer sequences than BLOSUM50.

### Newer matrices

A number of newer substitution matrices have been proposed to deal with inadequacies in earlier designs.

- JTT (1992). Published in the same year as BLOSOM, it also performs clustering and uses an implicit model. This may help reduce the systematic error from maximum parismony (MP), but also wastes sequence information.
- VTML (2001), a PAM-like matrix based on the alignments in the SYSTERS database, iteratively improved using a maximum likelihood estimator starting from the 1970s Dayhoff PAM model.
- WAG (Wheelan And Goldman, 2001) uses a maximum likelihood estimating procedure instead of any form of MP over a "BRKALN" dataset. The substitution scores are calculated based on the likelihood of a change considering multiple tree topologies derived using neighbor-joining. The scores correspond to a substitution model which includes also amino-acid stationary frequencies and a scaling factor in the similarity scoring. There are two versions of the matrix: WAG matrix based on the assumption of the same amino-acid stationary frequencies across all the compared protein and WAG* matrix with different frequencies for each of included protein families.
- PMB (Probability Matrix from Blocks, 2003), a set of "true" substitution frequencies estimated from the observed frequencies of BLOSUM, taking into account the possibility of a later substitution masking a previous one. It thus creates a evolutionary model where the distances have theoretical meaning (BLOSUM does not have this feature, unlike PAM, WAG, and most other later matrices, and hence is *not* recommended for phylogeny by IQ-TREE).
- LG (2008), which uses a larger dataset (Pfam-based) than WAG. An extension of the WAG algorithm is used, with a new PhyML (WAG+Γ4) model taking into account of sites with different evolutionary rates.
- Qmaker and nQmaker (2021, 2022), programs with the ability to estimate time-reversible and nonreversible matrices from very large datasets quickly. Each provide a general matrix and 5 specialized matrices, for a total of 12 precalculated substitution matrices.
- Matrices using a selection of proteins based on structural relatedness, as proposed by Benner et al. (1994), Fan (2004), and Steven et al. (2004).
- Matrices using structural alignments of proteins instead of simple sequence alignment (6 separate publications).
- Matrices using known physiochemical parameters of amino acid residues (5 separate publications).

For a list of more models (including irreversible i.e. asymmetric and/or specialized ones), see the documentation for recent bioinformatic software including IQ-Tree, PhyML, and RAxML.

#### Specialized substitution matrices and their extensions

The real substitution rates in a protein depends not only on the identity of the amino acid, but also on the specific structural or sequence context it is in. Many specialized matrices have been developed for these contexts, such as in transmembrane alpha helices, for combinations of secondary structure states and solvent accessibility states, or for local sequence-structure contexts. These context-specific substitution matrices lead to generally improved alignment quality at some cost of speed but are not yet widely used.

Since the 2000s, an increasing amount of matrices are defined for subsets of proteins not optimally aligned by traditional "general-purpose" matrices. These include:

- PfSSM (2008), CBM and CCF (2008) for *Plasmodium* proteins, which have a different amino acid evolutionary bias due to the low GC content of the genome.
- Matrices for transmembrane proteins. JTT transmembrane (1994) is the first of the class. Later work include:
  - For alpha-helical transmembrane proteins, PHAT (2000) and SLIM (2001).
  - For beta-barrel transmembrane proteins, bbTM (2008).
- Matrices for a specific protein family, including GPCRtm (2015) for the transmembrane (mostly helical) regions of GPCRs.
- Matrices for proteins with a specific role, including Hubsm (2017) for "hub proteins" in protein‐protein interaction networks.
- Matrices for intrinsically disordered proteins, including DUNMat (2002), MidicMat (2009), Disorder (2010), and EDSSMat (2019).

Recently, sequence context-specific amino acid similarities have been derived that do not need substitution matrices but that rely on a library of sequence contexts instead. Using this idea, a context-specific extension of the popular BLAST program has been demonstrated to achieve a twofold sensitivity improvement for remotely related sequences over BLAST at similar speeds (CS-BLAST).

## Nucleotide matrices

With nucleotides only having four possible values (in most bioinformatic sequences), the emphasis lies not in setting fixed values in the matrix, but in designing parameterized models that fit the observed evolution of the input sequence as it's being aligned. See Models of DNA evolution.

## Terminology

Although "transition matrix" is often used interchangeably with "substitution matrix" in fields other than bioinformatics, the former term is problematic in bioinformatics. With regards to nucleotide substitutions, "transition" is also used to indicate those substitutions that are between the two-ring purines (A → G and G → A) or are between the one-ring pyrimidines (C → T and T → C). Because these substitutions do not require a change in the number of rings, they occur more frequently than the other substitutions. "Transversion" is the term used to indicate the slower-rate substitutions that change a purine to a pyrimidine or vice versa (A ↔ C, A ↔ T, G ↔ C, and G ↔ T).
