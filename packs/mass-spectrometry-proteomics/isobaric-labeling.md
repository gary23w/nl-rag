---
title: "Isobaric labeling"
source: https://en.wikipedia.org/wiki/Isobaric_labeling
domain: mass-spectrometry-proteomics
license: CC-BY-SA-4.0
tags: shotgun proteomics, peptide fragmentation, tandem ms, electrospray
fetched: 2026-07-02
---

# Isobaric labeling

**Isobaric labeling** is a mass spectrometry strategy used in quantitative proteomics. Peptides or proteins are labeled with chemical groups that have nominally identical mass (isobaric), but vary in terms of distribution of heavy isotopes in their structure. These tags, commonly referred to as tandem mass tags, are designed so that the mass tag is cleaved at a specific linker region upon high-energy collision-induced dissociation (HCD) during tandem mass spectrometry yielding reporter ions of different masses.

The most common isobaric tags are amine-reactive tags. However, tags that react with cysteine residues and carbonyl groups have also been described. These amine-reactive groups go through N-hydroxysuccinimide (NHS) reactions, which are based around three types of functional groups. Isobaric labeling methods include tandem mass tags (TMT), isobaric tags for relative and absolute quantification (iTRAQ), mass differential tags for absolute and relative quantification, and dimethyl labeling. TMTs and iTRAQ methods are most common and developed of these methods. Tandem mass tags have a mass reporter region, a cleavable linker region, a mass normalization region, and a protein reactive group and have the same total mass.

## Workflow

A typical bottom-up proteomics workflow is described by (Yates, 2014). Protein samples are enzymatically digested by a protease to produce peptides. Each digested experimental sample is derivative from a set with a different isotopic variant of the tag. The samples are mixed in typically equal ratios and analyzed simultaneously in one MS run. Since the tags are isobaric and have identical chemical properties, the isotopic variants of the tags appear as a single composite peak at the same m/z value in an MS1 scan with identical liquid chromatography (LC) retention times. During the MS2 analysis and upon fragmentation, each isotopic variant of the tag produces sequence-specific product ions. These product ions are used to determine the peptide sequence and the reporter tags whose abundances reflect the relative ratio of the peptide in the combined samples. The use of MS/MS is required to detect the tags, therefore, unlabeled peptides are not quantified.

## Advantages

Explained previously by (Lee, Choe, Aggarwal, 2017). A key benefit of isobaric labeling over other quantification techniques (e.g. label-free) is the multiplex capabilities and thus increased throughput potential. The ability to combine and analyze several samples simultaneously in one LC-MS run eliminates the need to analyze multiple data sets and eliminates run-to-run variation. Multiplexing reduces sample processing variability, improves specificity by quantifying the peptides from each condition simultaneously, and reduces turnaround time for multiple samples. Without multiplexing, information can be missed from run to run, affecting identification and quantification, as peptides selected for fragmentation on one LC-MS/MS run may not be present or of suitable quantity in subsequent sample runs. The current available isobaric chemical tags facilitate the simultaneous analysis of 2 to 11 experimental samples.

## Applications

Isobaric labeling has been successfully used for many biological applications including protein identification and quantification, protein expression profiling of normal vs abnormal states, quantitative analysis of proteins for which no antibodies are available and identification and quantification of post-translationally modified proteins.

## Availability

There are two types of isobaric tags commercially available: tandem mass tags (TMT) and isobaric tags for relative and absolute quantitation (iTRAQ). Amine-reactive TMT are available in duplex, 6-plex 10-plex, and now 11-plex sets. Amine-reactive iTRAQ are available in 4-plex and 8-plex forms.
