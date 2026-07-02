---
title: "Small RNA sequencing"
source: https://en.wikipedia.org/wiki/Small_RNA_sequencing
domain: rna-sequencing
license: CC-BY-SA-4.0
tags: rna sequencing, single cell rna, transcript quantification, differential expression
fetched: 2026-07-02
---

# Small RNA sequencing

**Small RNA sequencing** (Small RNA-Seq) is a type of RNA sequencing based on the use of NGS technologies that allows to isolate and get information about noncoding RNA molecules in order to evaluate and discover new forms of small RNA and to predict their possible functions. By using this technique, it is possible to discriminate small RNAs from the larger RNA family to better understand their functions in the cell and in gene expression. Small RNA-Seq can analyze thousands of small RNA molecules with a high throughput and specificity. The greatest advantage of using RNA-seq is represented by the possibility of generating libraries of RNA fragments starting from the whole RNA content of a cell.

## Introduction

Small RNAs are noncoding RNA molecules between 20 and 200 nucleotide in length. The item "small RNA" is a rather arbitrary term, which is vaguely defined based on its length comparing with regular RNA such as messenger RNA (mRNA). Previously bacterial short regulatory RNAs have been referred to as small RNAs, but they are not related to eukaryotic small RNAs.

Small RNAs include several different classes of noncoding RNAs, depending on their sizes and functions: snRNA, snoRNA, scRNA, piRNA, miRNA, YRNA, tsRNA, rsRNA, and siRNA. Their functions go from RNAi (specific for endogenously expressed miRNA and exogenously derived siRNA), RNA processing and modification, epigenetic modifications, protein stability and transport.

## Small RNA sequencing

### Purification

This step is very critical and important for any molecular-based technique since it ensures that the small RNA fragments found in the samples to be analyzed are characterized by a good level of purity and quality. There are different purification methods that can be used, based on the purposes of the experiment:

- acid guanidinium thiocyanate-phenol-chloroform extraction: it is based on the use of a guanidinium-thiocyanate solution combined with acid phenol that disrupts cell membranes bringing in solution the nucleic acids and inactivating cellular ribonucleases (chaotropic agent). After this step an aliquot of chloroform is added in order to separate the aqueous phase (containing the RNA molecules) from the organic phase (cellular debris and other contaminants).
- spin column chromatography: universally used method to purify nucleic acids that exploits a spin column containing a special resin that, after a first step of cell lysis, allows the binding of the RNA molecules, eluting unbound particles (several proteins and rRNA). The protocol includes two separate chromatographic runs: the first one is required to isolate the whole RNA content from the sample, while the second one is specific for the isolation of small RNA by adding a small RNA enriched matrix to the column and by using a specific buffer to finally elute them. This method can separate small RNA molecules without the need of adding phenol.

Once small RNAs have been isolated, it is important to quantify them and to evaluate the quality of the purification. There are two different methods to do this:

- analysis of the absorbances and gel electrophoresis: this practical approach exploits the use of a spectrophotometer to evaluate the absorbance of RNA molecules at 260 nm (1 OD = 40 μg/μL) in order to estimate their concentration and to discover possible contaminations (i.g. proteins or carbohydrates); this can be coupled with an electrophoretic run performed in denaturating conditions (8 M urea) to analyze the quality of the purification extracts (low quality extracts will be degraded and displayed as smears in the gel).
- Agilent bioanalyzer: fully automated technique that is based on the use of a special apparatus composed by a chip that allows to perform capillary electrophoresis (CE) using small aliquots of the starting samples and obtaining an electropherogram that is useful to estimate the quality of the extracts thanks to a score (ranging from 1 to 10) attributed by the system.

### Library preparation and amplification

Many of the NGS sequencing protocols rely on the production of a genomic library that contains thousands of fragments of the target nucleic acids that will then be sequenced by proper technologies. According to the sequencing methods to be used, libraries can be created differently (in the case of the Ion Torrent technology RNA fragments are directly attached to a magnetic bead through an adapter, while for Illumina sequencing, the RNA fragments are firstly ligated to the adapters and then attached to the surface of a plate): generally, universal adapters A and B (containing well known sequences comprehensive of Unique Molecular Identifiers that are used to quantify small RNAs in a sample and sample indexing that allows to discriminate between different RNA molecules deriving from different samples) are ligated to the 5' and 3' ends of the RNA fragments thanks to the activity of the T4 RNA ligase 2 truncated. After the adapters are ligated to both ends of the small RNAs, retrotranscription occurs producing complementary DNA molecules (cDNAs) which will be, eventually, amplified by different amplification techniques depending on the sequencing protocol that is being followed (Ion Torrent exploits the emulsion PCR, while Illumina requires a bridge PCR) in order to obtain up to billions of amplicons to be sequenced. Besides the regular PCR mix, masking oligonucleotides targeting 5.8s rRNA are added to increase sensitivity to small RNA targets and to improve the amplification results. Caution has to be used, as RNA samples are prone to degradation, and further improvement of this technique should be oriented towards the elimination of adapter dimers. Some specific RNA modifications (such as 5′ hydroxyl (5′-OH), 3′-phosphate (3′-P) and 2′,3′-cyclic phosphate (2′3′-cP)) can block the adapter ligation process, while some other RNA modifications ( such as m1A, m3C, m1G and m22G) can interfere with reverse transcription process. Small RNA bearing one or more of these modifications are often inefficiently and incompletely converted into cDNAs, leading to challenges with their detection and quantitation by deep sequencing, which can be overcome by enzyme (such as PNK and AlkB) pre-treatment.

### Sequencing

Depending on the purpose of the analysis, RNA-seq can be performed using different approaches:

- Ion Torrent sequencing: NGS technology based on the use of a semiconductor chip where the sample is loaded integrated with an ion-sensitive field-effect transistor able to sensitively detect reductions of the pH value due to the release of one or more protons after the incorporation of one or more dNTPs during sequencing by synthesis: the signal is, then, transmitted to a machine composed of an electronic reading board to interface with the chip, a microprocessor for signal processing and a fluidics system to control the flow of reagents over the chip.
- Illumina sequencing: it offers a good method for small RNA sequencing and it is the most widely used approach. After the library preparation and amplification steps, the sequencing (based on the use of reversible dye-terminators) can be performed by using different systems, such as Miseq System, Miseq Series, NextSeq Series and many others, according to the applications

### Data analysis and storage

The final step regards analysis of data and storage: after obtaining the sequencing reads, UMI and index sequences are automatically removed from the reads and their quality is analyzed by PHRED (software able to evaluate the quality of the sequencing process); reads can then be mapped or aligned to a reference genome in order to extract information about their similarity: reads having the same length, sequence and UMI are considered as equal and are removed from the hit list. Indeed, the number of different UMIs for a given small RNA sequence reflects its copy number. The small RNAs are finally quantified by assigning molecules to transcript annotations from different databases (Mirbase, GtRNAdb and Gencode).

### Applications

Small RNA sequencing can be useful for:

- studying the expression profile of miRNA and other small RNAs
- increasing the understanding of how cells are regulated or misregulated under pathological conditions
- small RNA clustering
- novel small RNA discovery
- small RNA prediction
- differential expression of all small RNAs in any sample
