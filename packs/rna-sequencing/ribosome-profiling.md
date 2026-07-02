---
title: "Ribosome profiling"
source: https://en.wikipedia.org/wiki/Ribosome_profiling
domain: rna-sequencing
license: CC-BY-SA-4.0
tags: rna sequencing, single cell rna, transcript quantification, differential expression
fetched: 2026-07-02
---

# Ribosome profiling

**Ribosome profiling**, or **Ribo-Seq** (also named **ribosome footprinting**), is an adaptation of a technique developed by Joan Steitz and Marilyn Kozak almost 50 years ago that Nicholas Ingolia and Jonathan Weissman adapted to work with next generation sequencing that uses specialized messenger RNA (mRNA) sequencing to determine which mRNAs are being actively translated. A related technique that can also be used to determine which mRNAs are being actively translated is the Translating Ribosome Affinity Purification (TRAP) methodology, which was developed by Nathaniel Heintz at Rockefeller University (in collaboration with Paul Greengard and Myriam Heiman). TRAP does not involve ribosome footprinting but provides cell type-specific information.

## Description

It produces a "global snapshot" of all the ribosomes actively translating in a cell at a particular moment, known as a translatome. Consequently, this enables researchers to identify the location of translation start sites, the complement of translated ORFs in a cell or tissue, the distribution of ribosomes on a messenger RNA, and the speed of translating ribosomes. Ribosome profiling targets only mRNA sequences protected by the ribosome during the process of decoding by translation unlike RNA-Seq, which sequences all of the mRNA of a given sequence present in a sample. This technique is also different from polysome profiling.

## History

Ribosome profiling is based on the discovery that the mRNA within a ribosome can be isolated through the use of nucleases that degrade unprotected mRNA regions. This technique analyzes the regions of mRNAs being converted to protein, as well as the levels of translation of each region to provide insight into global gene expression. Prior to its development, efforts to measure translation in vivo included microarray analysis on the RNA isolated from polysomes, as well as translational profiling through the affinity purification of epitope tagged ribosomes. These are useful and complementary methods, but neither allows the sensitivity and positional information provided by ribosome profiling.

## Uses

There are three main uses of ribosome profiling: identifying translated mRNA regions, observing how nascent peptides are folded, and measuring the amount of specific proteins that are synthesized.

### Identifying Translated mRNA Regions

By using specific drugs, ribosome profiling can identify initiating regions of mRNA, elongating regions, and areas of translation stalling. Initiating regions can be detected by adding harringtonine or lactidomycin to prevent any further initiation. This allows the starting codon of the mRNAs throughout the cell lysate to be analyzed, which has been used to determine non-AUG sequences that do initiate translation. The other elongating regions can be detected by adding antibiotics like cycloheximide that inhibit translocation, chloramphenicol that inhibits transfer of peptides within the ribosome, or non-drug means like thermal freezing. These elongation freezing methods allow for the kinetics of translation to be analyzed. Since multiple ribosomes can translate a single mRNA molecule to speed up the translation process, RiboSeq demonstrates the protein coding regions within the mRNA and how quickly this is done depending on the mRNA being sequenced. This also allows for ribosome profiling to show pause sites within the transcriptome at specific codons. These sites of slow or paused translation are demonstrated by an increase in ribosome density and these pauses can link specific proteins with their roles within the cell.

### Peptide Folding

Coupling ribosome profiling with ChIP can elucidate how and when newly synthesized proteins are folded. Using the footprints provided by Ribo-Seq, specific ribosomes associated with factors, like chaperones, can be purified. Pausing the ribosome at specific time points, allowing it to translate a polypeptide over time, and exposing the different points to a chaperone and precipitating out using ChIP purifies these samples and can show at which point in time the peptide is being folded.

### Measuring Protein Synthesis

Ribo-Seq can also be used to estimate translation efficiency, a proxy for protein synthesis. For this application, ribosome profiling and matched RNA sequencing data are generated. The initial data analyses can be achieved by dedicated computational frameworks (ex.). Translation efficiency can then be computed as the ribosome occupancy of each gene while controlling for its RNA expression. This approach can be coupled with directed disruption of proteins that bind to RNA and using ribosome profiling to measure the difference in translation. These disrupted mRNAs can be associated with proteins, whose binding sites have already been mapped on RNA, to indicate regulation.

## Procedure

Ribosome profiling typically follows these steps:

1. Lyse the cells or tissue and isolate the mRNA molecules bound to ribosomes.
2. Immobilize complexes. This is commonly performed with cycloheximide but other chemicals can be employed. It is also possible to forgo translation inhibitors with translation-incompetent lysis conditions.
3. Using ribonucleases, digest the RNA not protected by ribosomes.
4. Isolate the mRNA-ribosome complexes using sucrose gradient density centrifugation or specialized chromatography columns.
5. Phenol/chloroform purification of mixture to remove proteins.
6. Size-select for previously-protected mRNA fragments.
7. Ligate 3' adapter to fragments.
8. Reverse transcribe RNA to cDNA using reverse transcriptase.
9. Circularize the cDNA
10. Subtract known rRNA contaminants (optional).
11. Amplify in strand-specific manner.
12. Sequence reads.
13. Align sequence results to genomic sequence to determine translational profile.
14. Analyze resulting data using computational approaches specifically designed for ribosome profiling.

## Materials

- RNA-ribosome complexes
- Cycloheximide
- Nucleases
- Phenol/Chloroform
- Reverse transcriptase
- dNTPs
- Sequencing method-cDNA library.
