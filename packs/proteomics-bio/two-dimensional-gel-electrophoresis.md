---
title: "Two-dimensional gel electrophoresis"
source: https://en.wikipedia.org/wiki/Two-dimensional_gel_electrophoresis
domain: proteomics-bio
license: CC-BY-SA-4.0
tags: proteomics analysis, mass spectrometry proteomics, protein identification, two dimensional gel
fetched: 2026-07-02
---

# Two-dimensional gel electrophoresis

**Two-dimensional gel electrophoresis**, abbreviated as **2-DE** or **2-D electrophoresis**, is a form of gel electrophoresis commonly used to analyze proteins. Mixtures of proteins are separated by two properties in two dimensions on 2D gels. 2-DE was independently introduced in 1969 by Macko and Stegemann (working with potato proteins) and Dale and Latner (working with serum).

## Basis for separation

2-D electrophoresis begins with electrophoresis in the first dimension and then separates the molecules perpendicularly from the first to create an electropherogram in the second dimension. In electrophoresis in the first dimension, molecules are separated linearly according to their isoelectric point. In the second dimension, the molecules are then separated at 90 degrees from the first electropherogram according to molecular mass. Since it is unlikely that two molecules will be similar in two distinct properties, molecules are more effectively separated in 2-D electrophoresis than in 1-D electrophoresis.

The two dimensions that proteins are separated into using this technique can be isoelectric point, protein complex mass in the native state, or protein mass.

- The separation by isoelectric point is called isoelectric focusing. Thereby, a pH gradient is applied to a gel and an electric potential is applied across the gel, making one end more positive than the other. At all pH values other than their isoelectric point, proteins will be charged. If they are positively charged, they will be pulled towards the more negative end of the gel and if they are negatively charged they will be pulled to the more positive end of the gel. The proteins applied in the first dimension will move along the gel and will accumulate at their isoelectric point; that is, the point at which the overall charge on the protein is 0 (a neutral charge).
- Separation by protein complex mass is done via native PAGE, in which proteins remain in their native state and are separated in the electric field following their mass and the mass of their complexes respectively. To obtain a separation by size and not by net charge, as in IEF, an additional charge is transferred to the proteins by the use of Coomassie brilliant blue or lithium dodecyl sulfate. Knowledge of protein complex is important for the analysis of the functioning of proteins in a cell, as proteins mostly act together in complexes to be fully functional. The analysis of this sub organelle organisation of the cell requires techniques conserving the native state of the protein complexes.
- Separate just by mass is commonly achieved using SDS-PAGE. SDS denatures the proteins, breaks apart most complexes, and approximately equalizes the mass-to-charge ratios. SDS must be done as the second, perpendicular dimension, as it breaks apart complexes (rendering native PAGE impossible) and equalizes mass-to-charge ratios (rendering IEF impossible).

## Detecting proteins

The result of this is a gel with proteins spread out on its surface. These proteins can then be detected by a variety of means, but the most commonly used stains are silver and Coomassie brilliant blue staining. In the former case, a silver colloid is applied to the gel. The silver binds to cysteine groups within the protein. The silver is darkened by exposure to ultra-violet light. The amount of silver can be related to the darkness, and therefore the amount of protein at a given location on the gel. This measurement can only give approximate amounts, but is adequate for most purposes. Silver staining is 100x more sensitive than Coomassie brilliant blue with a 40-fold range of linearity.

Molecules other than proteins can be separated by 2D electrophoresis. In supercoiling assays, coiled DNA is separated in the first dimension and denatured by a DNA intercalator (such as ethidium bromide or the less carcinogenic chloroquine) in the second. This is comparable to the combination of native PAGE/SDS-PAGE in protein separation.

## Common techniques

### IPG-DALT

A common technique is to use an Immobilized pH gradient (IPG) in the first dimension. This technique is referred to as **IPG-DALT**. The sample is first separated onto IPG gel (which is commercially available) then the gel is cut into slices for each sample which is then equilibrated in SDS-mercaptoethanol and applied to an SDS-PAGE gel for resolution in the second dimension. Typically IPG-DALT is not used for quantification of proteins due to the loss of low molecular weight components during the transfer to the SDS-PAGE gel.

### IEF SDS-PAGE

See Isoelectric focusing

## 2D gel analysis software

In quantitative proteomics, these tools primarily analyze bio-markers by quantifying individual proteins, and showing the separation between one or more protein "spots" on a scanned image of a 2-DE gel. Additionally, these tools match spots between gels of similar samples to show, for example, proteomic differences between early and advanced stages of an illness. While this technology is widely utilized, the intelligence has not been perfected. For example, some software may tend to agree on the quantification and analysis of well-defined well-separated protein spots, they deliver different results and analysis tendencies with less-defined less-separated spots. Comparative studies have previously been published to guide researchers on the "best" software for their analysis.

Challenges for automatic software-based analysis include incompletely separated (overlapping) spots (less-defined or separated), weak spots / noise (e.g., "ghost spots"), running differences between gels (e.g., protein migrates to different positions on different gels), unmatched/undetected spots, leading to missing values, mismatched spots, errors in quantification (several distinct spots may be erroneously detected as a single spot by the software and parts of a spot may be excluded from quantification), and differences in software algorithms and therefore analysis tendencies

Generated picking lists can be used for the automated in-gel digestion of protein spots, and subsequent identification of the proteins by mass spectrometry. Mass spectrometry analysis can identify precise mass measurements along with the sequencing of peptides that range from 1000–4000 atomic mass units.
