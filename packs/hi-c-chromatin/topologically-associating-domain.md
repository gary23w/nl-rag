---
title: "Topologically associating domain"
source: https://en.wikipedia.org/wiki/Topologically_associating_domain
domain: hi-c-chromatin
license: CC-BY-SA-4.0
tags: chromosome conformation, topologically associating domain, genome folding, contact matrix
fetched: 2026-07-02
---

# Topologically associating domain

A **topologically associating domain** (TAD) is a self-interacting genomic region, meaning that DNA sequences within a TAD physically interact with each other more frequently than with sequences outside the TAD. The average size of a topologically associating domain (TAD) is 1000 kb in humans, 880 kb in mouse cells, and 140 kb in fruit flies. Boundaries at both side of these domains are conserved between different mammalian cell types and even across species and are highly enriched with CCCTC-binding factor (CTCF) and cohesin. In addition, some types of genes (such as transfer RNA genes and housekeeping genes) appear near TAD boundaries more often than would be expected by chance.

The functions of TADs are not fully understood and are still a matter of debate. Most of the studies indicate TADs regulate gene expression by limiting the enhancer-promoter interaction to each TAD; however, a recent study uncouples TAD organization and gene expression. Disruption of TAD boundaries are found to be associated with wide range of diseases such as cancer, variety of limb malformations such as synpolydactyly, Cooks syndrome, and F-syndrome, and number of brain disorders like Hypoplastic corpus callosum and Adult-onset demyelinating leukodystrophy. Furthermore, studies have revealed that interactions between promoters and enhancers spanning single or multiple TADs, are fundamental to the exact dynamics of gene expression. The genomic elements underlying these interactions are named distal tethering elements (DTEs) and it has been shown that these elements are important for precise gene activation of Hox genes in early embryogenesis of *D. melanogaster*.

The mechanisms underlying TAD formation are also complex and not yet fully elucidated, though a number of protein complexes and DNA elements are associated with TAD boundaries. However, the handcuff model and the loop extrusion model describe the TAD formation by the aid of CTCF and cohesin proteins. Furthermore, it has been proposed that the stiffness of TAD boundaries itself could cause the domain insulation and TAD formation. A typical TAD boundary contains a cluster of CTCF sites which may act synergistically to create a region with distinct properties of the nucleosome fiber that separates two neighboring TADs.

## Discovery and diversity

TADs are defined as regions whose DNA sequences preferentially contact each other. They were discovered in 2012 using chromosome conformation capture techniques including Hi-C. They have been shown to be present in multiple species, including fruit flies (Drosophila), mouse, plants, fungi and human genomes. In bacteria, they are referred to as Chromosomal Interacting Domains (CIDs).

## Analytical tools and databases

TAD locations are defined by applying an algorithm to Hi-C data. For example, TADs are often called according to the so-called "directionality index". The directionality index is calculated for individual 40kb bins, by collecting the reads that fall in the bin, and observing whether their paired reads map upstream or downstream of the bin (read pairs are required to span no more than 2Mb). A positive value indicates that more read pairs lie downstream than upstream, and a negative value indicates the reverse. Mathematically, the directionality index is a signed chi-square statistic.

The development of specialized genome browsers and visualization tools such as Juicebox, HiGlass/HiPiler, The 3D Genome Browser, 3DIV, 3D-GNOME, and TADKB have enabled us to visualize the TAD organization of regions of interest in different cell types.

## Mechanisms of formation

A number of proteins are known to be associated with TAD formation including the protein CTCF (usually several CTCF binding sites are present at a TAD boundary) and the protein complex cohesin. It is also unknown what components are required at TAD boundaries; however, in mammalian cells, it has been shown that these boundary regions have comparatively high levels of CTCF binding. In addition, some types of genes (such as transfer RNA genes and housekeeping genes) appear near TAD boundaries more often than would be expected by chance.

Computer simulations have shown that chromatin loop extrusion driven by cohesin motors can generate TADs. In the loop extrusion model, cohesin binds chromatin, pulls it in, and extrudes chromatin to progressively grow a loop. Chromatin on both sides of the cohesin complex is extruded until cohesin encounters a chromatin-bound CTCF protein, typically located at the boundary of a TAD. In this way, TAD boundaries can be brought together as the anchors of a chromatin loop. Indeed, in vitro, cohesin has been observed to processively extrude DNA loops in an ATP-dependent manner and stall at CTCF. However, some in vitro data indicates that the observed loops may be artifacts. Importantly, since cohesins can dynamically unbind from chromatin, this model suggests that TADs (and associated chromatin loops) are dynamic, transient structures, in agreement with in vivo observations.

Other mechanisms for TAD formation have been suggested. For example, some simulations suggest that transcription-generated supercoiling can relocalize cohesin to TAD boundaries or that passively diffusing cohesin "slip links" can generate TADs.

## Properties

### Conservation

TADs have been reported to be relatively constant between different cell types (in stem cells and blood cells, for example), and even between species in specific cases. Comparative TAD analysis between *Drosophila melanogaster* and *Drosophila subobscura*, with a divergence time of approximately 49 million years, has revealed a conservation in range of 30-40%.

### Relationship with promoter-enhancer contacts

The majority of observed interactions between promoters and enhancers do not cross TAD boundaries. Removing a TAD boundary (for example, using CRISPR to delete the relevant region of the genome) can allow new promoter-enhancer contacts to form. This can affect gene expression nearby - such misregulation has been shown to cause limb malformations (e.g. polydactyly) in humans and mice.

Computer simulations have shown that transcription-induced supercoiling of chromatin fibres can explain how TADs are formed and how they can assure very efficient interactions between enhancers and their cognate promoters located in the same TAD.

### Relationship with other structural features of the genome

Replication timing domains have been shown to be associated with TADs as their boundary is co localized with the boundaries of TADs that are located at either sides of compartments. Insulated neighborhoods, DNA loops formed by CTCF/cohesin-bound regions, are proposed to functionally underlie TADs.

Genome rearrangement breakpoint have shown to be enriched at the TAD boundaries in *D. melanogaster*.

## Role in disease

Disruption of TAD boundaries can affect the expression of nearby genes, and this can cause disease.

For example, genomic structural variants that disrupt TAD boundaries have been reported to cause developmental disorders such as human limb malformations. Additionally, several studies have provided evidence that the disruption or rearrangement of TAD boundaries can provide growth advantages to certain cancers, such as T-cell acute lymphoblastic leukemia (T-ALL), gliomas, and lung cancer.

## Lamina-associated domains

Lamina-associated domains (LADs) are parts of the chromatin that heavily interact with the lamina, a network-like structure at the inner membrane of the nucleus. LADs consist mostly of transcriptionally silent chromatin, being enriched with trimethylated Lys27 on histone H3, (i.e. H3K27me3); which is a common posttranslational histone modification of heterochromatin. LADs have CTCF-binding sites at their periphery.
