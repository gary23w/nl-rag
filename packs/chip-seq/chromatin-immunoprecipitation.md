---
title: "Chromatin immunoprecipitation"
source: https://en.wikipedia.org/wiki/Chromatin_immunoprecipitation
domain: chip-seq
license: CC-BY-SA-4.0
tags: chromatin immunoprecipitation, transcription factor binding, peak calling, histone mark
fetched: 2026-07-02
---

# Chromatin immunoprecipitation

**Chromatin immunoprecipitation** (**ChIP**) is a type of immunoprecipitation experimental technique used to investigate the interaction between proteins and DNA in the cell. It aims to determine whether specific proteins are associated with specific genomic regions, such as transcription factors on promoters or other DNA binding sites, and possibly define cistromes. ChIP also aims to determine the specific location in the genome that various histone modifications are associated with, indicating the target of the histone modifiers. ChIP is crucial for the advancements in the field of epigenomics and learning more about epigenetic phenomena.

Briefly, the conventional method is as follows:

1. DNA and associated proteins on chromatin in living cells or tissues are crosslinked (this step is omitted in Native ChIP).
2. The DNA-protein complexes (chromatin-protein) are then sheared into ~500 bp DNA fragments by sonication or nuclease digestion.
3. Cross-linked DNA fragments associated with the protein(s) of interest are selectively immunoprecipitated from the cell debris using an appropriate protein-specific antibody.
4. The associated DNA fragments are purified and their sequence is determined. Enrichment of specific DNA sequences represents regions on the genome that the protein of interest is associated with *in vivo*.

## Typical ChIP

There are mainly two types of ChIP, primarily differing in the starting chromatin preparation. The first uses reversibly cross-linked chromatin sheared by sonication called cross-linked ChIP (XChIP). Native ChIP (NChIP) uses native chromatin sheared by micrococcal nuclease digestion.

### Cross-linked ChIP (XChIP)

Cross-linked ChIP is mainly suited for mapping the DNA target of transcription factors or other chromatin-associated proteins, and uses reversibly cross-linked chromatin as starting material. The agent for reversible cross-linking could be formaldehyde or UV light. Then the cross-linked chromatin is usually sheared by sonication, providing fragments of 300–1000 base pairs (bp) in length. Mild formaldehyde crosslinking followed by nuclease digestion has been used to shear the chromatin. Chromatin fragments of 400–500 bp have proven to be suitable for ChIP assays as they cover two to three nucleosomes.

Cell debris in the sheared lysate is then cleared by sedimentation and protein–DNA complexes are selectively immunoprecipitated using specific antibodies to the protein(s) of interest. The antibodies are commonly coupled to agarose, sepharose, or magnetic beads. Alternatively, chromatin-antibody complexes can be selectively retained and eluted by inert polymer discs. The immunoprecipitated complexes (i.e., the bead–antibody–protein–target DNA sequence complex) are then collected and washed to remove non-specifically bound chromatin, the protein–DNA cross-link is reversed and proteins are removed by digestion with proteinase K. An epitope-tagged version of the protein of interest, or *in vivo* biotinylation can be used instead of antibodies to the native protein of interest.

The DNA associated with the complex is then purified and identified by polymerase chain reaction (PCR), microarrays (ChIP-on-chip), molecular cloning and sequencing, or direct high-throughput sequencing (ChIP-Seq).

### Native ChIP (NChIP)

Native ChIP is mainly suited for mapping the DNA target of histone modifiers. Generally, native chromatin is used as starting chromatin. As histones wrap around DNA to form nucleosomes, they are naturally linked. Then the chromatin is sheared by micrococcal nuclease digestion, which cuts DNA at the length of the linker, leaving nucleosomes intact and providing DNA fragments of one nucleosome (200 bp) to five nucleosomes (1000 bp) in length. Thereafter, methods similar to XChIP are used for clearing the cell debris, immunoprecipitating the protein of interest, removing protein from the immunoprecipitated complex, and purifying and analyzing the complex-associated DNA.

### Comparison of XChIP and NChIP

The major advantage of NChIP is antibody specificity. Most antibodies to modified histones are raised against unfixed, synthetic peptide antigens. The epitopes they need to recognize in the XChIP may be disrupted or destroyed by formaldehyde cross-linking, particularly as the cross-links are likely to involve lysine e-amino groups in the N-terminals, disrupting the epitopes. This is likely to explain the consistently low efficiency of XChIP protocols compared to NChIP.

But XChIP and NChIP have different aims and advantages relative to each other. XChIP is for mapping target sites of transcription factors and other chromatin-associated proteins; NChIP is for mapping target sites of histone modifiers (see Table 1).

### Comparison of ChIP-seq and ChIP-chip

Chromatin Immunoprecipitation sequencing, also known as ChIP-seq, is an experimental technique used to identify transcription factor binding events throughout an entire genome. Knowing how the proteins in the human body interact with DNA to regulate gene expression is a key component of our knowledge of human diseases and biological processes. ChIP-seq is the primary technique to complete this task, as it has proven to be extremely effective in resolving how proteins and transcription factors influence phenotypical mechanisms. Overall ChIP-seq has risen to be a very efficient method for determining these factors, but there is a rivaling method known as ChIP-on-chip.

ChIP-on-chip, also known as ChIP-chip, is an experimental technique used to isolate and identify genomic sites occupied by specific DNA-binding proteins in living cells. ChIP-on-chip is a relatively newer technique, as it was introduced in 2001 by Peggy Farnham and Michael Zhang. ChIP-on-chip gets its name by combining the methods of Chromatin Immunoprecipitation and DNA microarray, thus creating ChIP-on-chip.

The two methods seek similar results, as they both strive to find protein binding sites that can help identify elements in the human genome. Those elements in the human genome are important for the advancement of knowledge in human diseases and biological processes. The difference between ChIP-seq and ChIP-chip is established by the specific site of the protein binding identification. The main difference comes from the efficacy of the two techniques, ChIP-seq produces results with higher sensitivity and spatial resolution because of the wide range of genomic coverage. Even though ChIP-seq has proven to be more efficient than ChIP-chip, ChIP-seq is not always the first choice for scientists. The cost and accessibility of ChIP-seq is a major disadvantage, which has led to the more predominant use of ChIP-chip in laboratories across the world.

**Table 1 Advantages and disadvantages of NChIP and XChIP**

|   | **XChIP** | **NChIP** |
|---|---|---|
| **Advantages** | Suitable for transcriptional factors, or any other weakly binding chromatin associated proteins. Applicable to any organisms where native protein is hard to prepare | Testable antibody specificity Better antibody specificity as target protein naturally intact Better chromatin and protein revery efficiency due to better antibody specificity |
| **Disadvantages** | Inefficient chromatin recovery due to antibody target protein epitope disruption May cause false positive result due to fixation of transient proteins to chromatin Wide range of chromatin shearing size due to random cut by sonication. | Usually not suitable for non-histone proteins Nucleosomes may rearrange during digestion |

## History and New ChIP methods

In 1984 John T. Lis and David Gilmour, at the time a graduate student in the Lis lab, used UV irradiation, a zero-length protein-nucleic acid crosslinking agent, to covalently cross-link proteins bound to DNA in living bacterial cells. Following lysis of cross-linked cells and immunoprecipitation of bacterial RNA polymerase, DNA associated with enriched RNA polymerase was hybridized to probes corresponding to different regions of known genes to determine the in vivo distribution and density of RNA polymerase at these genes. A year later they used the same methodology to study the distribution of eukaryotic RNA polymerase II on fruit fly heat shock genes. These reports are considered the pioneering studies in the field of chromatin immunoprecipitation. XChIP was further modified and developed by Alexander Varshavsky and co-workers, who examined the distribution of histone H4 on heat shock genes using formaldehyde cross-linking. This technique was extensively developed and refined thereafter. NChIP approach was first described by Hebbes *et al*., 1988, and has also been developed and refined quickly. The typical ChIP assay usually takes 4–5 days and requires 106~ 107 cells at least. Now new techniques on ChIP could be achieved as few as 100~1000 cells and completed within one day.

- **Bead-free ChIP**: This novel method ChIP uses discs of inert, porous polymer functionalized with either Protein A or G in spin columns or microplates. The chromatin-antibody complex is selectively retained by the disc and eluted to obtain enriched DNA for downstream applications such as qPCR and sequencing. The porous environment is specifically designed to maximize capture efficiency and reduce non-specific binding. Due to less manual handling and optimized protocols, ChIP can be performed in 5 hours.
- **Carrier ChIP** (CChIP): This approach could use as few as 100 cells by adding *Drosophila* cells as carrier chromatin to reduce loss and facilitate precipitation of the target chromatin. However, it demands highly specific primers for detection of the target cell chromatin from the foreign carrier chromatin background, and it takes two to three days.
- **Fast ChIP** (qChIP): The fast ChIP assay reduced the time by shortening two steps in a typical ChIP assay: *(i)* an ultrasonic bath accelerates the rate of antibody binding to target proteins—and thereby reduces immunoprecipitation time *(ii)* a resin-based (Chelex-100) DNA isolation procedure reduces the time of cross-link reversal and DNA isolation. However, the fast protocol is suitable only for large cell samples (in the range of 106~107). Up to 24 sheared chromatin samples can be processed to yield PCR-ready DNA in 5 hours, allowing multiple chromatin factors be probed simultaneously and/or looking at genomic events over several time points.

- **Quick and quantitative ChIP** (Q2ChIP): The assay uses 100,000 cells as starting material and is suitable for up to 1,000 histone ChIPs or 100 transcription factor ChIPs. Thus many chromatin samples can be prepared in parallel and stored, and Q2ChIP can be undertaken in a day.
- **MicroChIP** (μChIP): chromatin is usually prepared from 1,000 cells and up to 8 ChIPs can be done in parallel without carriers. The assay can also start with 100 cells, but only suit for one ChIP. It can also use small (1 mm3) tissue biopsies and microChIP can be done within one day.
- **Matrix ChIP**: This is a microplate-based ChIP assay with increased throughput and a simplified procedure. All steps are done in microplate wells without sample transfers, enabling potential for automation. It enables 96 ChIP assays for histone and various DNA-bound proteins in a single day.
- **Pathology-ChIP** (PAT-ChIP): This technique allows ChIP from pathology formalin-fixed and paraffin-embedded tissues and thus the use of pathology archives (even those that are several years old) for epigenetic analyses and the identification of candidate epigenetic biomarkers or targets.

ChIP has also been applied for genome-wide analysis by combining with microarray technology (ChIP-on-chip) or second-generation DNA-sequencing technology (Chip-Sequencing). ChIP can also combine with paired-end tags sequencing in Chromatin Interaction Analysis using Paired End Tag sequencing (ChIA-PET), a technique developed for large-scale, de novo analysis of higher-order chromatin structures.

## Limitations

- Large Scale assays using ChIP is challenging using intact model organisms. This is because antibodies have to be generated for each TF, or, alternatively, transgenic model organisms expressing epitope-tagged TFs need to be produced.
- Researchers studying differential gene expression patterns in small organisms also face problems as genes expressed at low levels, in a small number of cells, in narrow time window.
- ChIP experiments cannot discriminate between different TF isoforms (Protein isoform).
