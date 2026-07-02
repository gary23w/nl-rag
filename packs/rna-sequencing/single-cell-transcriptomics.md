---
title: "Single-cell transcriptomics"
source: https://en.wikipedia.org/wiki/Single-cell_transcriptomics
domain: rna-sequencing
license: CC-BY-SA-4.0
tags: rna sequencing, single cell rna, transcript quantification, differential expression
fetched: 2026-07-02
---

# Single-cell transcriptomics

**Single-cell transcriptomics** refers to the quantification and analysis of the transcriptomes of individual cells. Single-cell transcriptomics makes it possible to unravel heterogeneous cell populations, reconstruct cellular developmental pathways, and model transcriptional dynamics.

## Background

The development of high-throughput RNA sequencing (RNA-seq) and microarrays has made gene expression analysis a routine. RNA analysis was previously limited to tracing individual transcripts by Northern blots or quantitative PCR. Higher throughput and speed allow researchers to frequently characterize the expression profiles of populations of thousands of cells. The data from bulk assays has led to identifying genes differentially expressed in distinct cell populations, and biomarker discovery.

These studies are limited as they provide measurements for whole tissues and, as a result, show an average expression profile for all the constituent cells. This has a couple of drawbacks. Firstly, different cell types within the same tissue can have distinct roles in multicellular organisms. They often form subpopulations with unique transcriptional profiles. Correlations in the gene expression of the subpopulations can often be missed due to the lack of subpopulation identification. Secondly, bulk assays fail to recognize whether a change in the expression profile is due to a change in regulation or composition — for example if one cell type arises to dominate the population. Lastly, when one's goal is to study cellular progression through differentiation, average expression profiles can only order cells by time rather than by developmental stage. Consequently, they cannot show trends in gene expression levels specific to certain stages.

Recent advances in biotechnology allow the measurement of gene expression in hundreds to thousands of individual cells simultaneously. While these breakthroughs in transcriptomics technologies have enabled the generation of single-cell transcriptomic data, they also presented new computational and analytical challenges. Bioinformaticians can use techniques from bulk RNA-seq for single-cell data. Still, many new computational approaches have had to be designed for this data type to facilitate a complete and detailed study of single-cell expression profiles.

## Experimental steps

There is so far no standardized technique to generate single-cell data: all methods must include cell isolation from the population, lysate formation, amplification through reverse transcription, and quantification of expression levels. Common techniques for measuring expression are quantitative PCR or RNA-seq.

### Isolating single cells

Several methods are available to isolate and amplify cells for single-cell analysis, differing primarily in throughput and potential for cell selection. Low-throughput techniques, such as micropipetting, cytoplasmic aspiration, and laser capture microdissection, typically isolate hundreds of cells but enable deliberate cell selection.

High-throughput methods allow for the rapid isolation of hundreds to tens of thousands of cells. Common high-throughput approaches include Fluorescence Activated Cell Sorting (FACS) and the use of microfluidic devices. Microfluidic platforms often isolate single cells either by mechanical separation into microwells (e.g., BD Rhapsody, Takara ICELL8, Vycap Puncher Platform, CellMicrosystems CellRaft) or by encapsulation within droplets (e.g., 10x Genomics Chromium, Illumina Bio-Rad ddSEQ, 1CellBio InDrop, Dolomite Bio Nadia). Furthermore, optimized protocols have been developed by integrating these isolation techniques directly with scRNA-seq workflows. For instance, combining FACS with scRNA-seq led to protocols like SORT-seq, and a list of studies utilizing SORT-seq can be found here. Similarly, the integration of microfluidic devices with scRNA-seq has been highly optimized in protocols such as those developed by 10x Genomics.

Single cell RNA-seq techniques that rely on split-pool barcoding can uniquely label cells without requiring the isolation of individual cells, including sci-RNA-seq, SPLiT-seq, and microSPLiT.

### Quantitative PCR (qPCR)

To measure the level of expression of each transcript qPCR can be applied. Gene specific primers are used to amplify the corresponding gene as with regular PCR and as a result data is usually only obtained for sample sizes of less than 100 genes. The inclusion of housekeeping genes, whose expression should be constant under the conditions, is used for normalization. The most commonly used house keeping genes include GAPDH and α-actin, although the reliability of normalization through this process is questionable as there is evidence that the level of expression can vary significantly. Fluorescent dyes are used as reporter molecules to detect the PCR product and monitor the progress of the amplification - the increase in fluorescence intensity is proportional to the amplicon concentration. A plot of fluorescence vs. cycle number is made and a threshold fluorescence level is used to find cycle number at which the plot reaches this value. The cycle number at this point is known as the threshold cycle (Ct) and is measured for each gene.

### Single-cell RNA-seq (scRNA-Seq)

The single-cell RNA-seq technique converts a population of RNAs to a library of cDNA fragments that can be sequenced. In droplet-based technologies such as 10x Genomics Chromium, single cells are isolated in droplets together with beads coated with barcoded oligonucleotides. Both cells and beads are supplied in limited amounts such that co-occupancy with multiple cells and beads is a very rare event. Cells are lysed within the droplets, and RNAs are reverse transcribed using the barcoded oligo-dT oligonucleotides as primers. After reverse transcription, the emulsion is broken, releasing the barcoded cDNA from all the droplets into a single solution. This pooled cDNA is then prepared for sequencing via the addition of sequencing adapters and PCR amplification.

These fragments are sequenced by high-throughput next generation sequencing techniques and the reads are mapped back to the reference genome, providing a count of the number of reads associated with each gene. Transcripts from a particular cell are identified by each cell's unique barcode.

Normalization of RNA-Seq data accounts for cell to cell variation in the efficiencies of the cDNA library formation and sequencing. One method relies on the use of extrinsic RNA spike-ins that are added in equal quantities to each cell lysate and used to normalize read count by the number of reads mapped to spike-in mRNA. Another control uses unique molecular identifiers (UMIs)-short DNA sequences (6–10nt) that are added to each cDNA before amplification and act as a bar code for each cDNA molecule. Normalization is achieved by using the count number of unique UMIs associated with each gene to account for differences in amplification efficiency.

A combination of both spike-ins, UMIs and other approaches have been combined to help identify artifacts during library preparation and for more accurate normalization.

#### Applications

scRNA-Seq is becoming widely used across biological disciplines including Development, Neurology, Oncology, Autoimmune disease, Infectious disease., brain disease, and environmental virology. Several scRNA-Seq protocols have been published: Tang et al., STRT, SMART-seq, CEL-seq, RAGE-seq, Quartz-seq and C1-CAGE. These protocols differ in terms of strategies for reverse transcription, cDNA synthesis and amplification, and the possibility to accommodate sequence-specific barcodes (i.e. UMIs) or the ability to process pooled samples. In 2017, two approaches were introduced to simultaneously measure single-cell mRNA and protein expression through oligonucleotide-labeled antibodies known as REAP-seq, and CITE-seq. A 2025 review in Science reported that applying single-cell transcriptomics to microbial communities reveals functional heterogeneity within gut communities, characteristic antibiotic responses, and the dynamics of mobile genetic elements. *Pountain, Andrew W.; Yanai, Itai (2025-09-04). "Dissecting microbial communities with single-cell transcriptome analysis". *Science*. **389** (6764) eadp6252. doi:10.1126/science.adp6252. PMC 12467864. PMID 40906858.*

scRNA-Seq has provided considerable insight into the development of embryos and organisms, including the worm *Caenorhabditis elegans*, and the regenerative planarian *Schmidtea mediterranea*. The first vertebrate animals to be mapped in this way were Zebrafish and *Xenopus laevis*. In each case multiple stages of the embryo were studied, allowing the entire process of development to be mapped on a cell-by-cell basis. Science recognized these advances as the 2018 Breakthrough of the Year.

### Considerations

A problem associated with single-cell data occurs in the form of zero inflated gene expression distributions, known as technical dropouts, that are common due to low mRNA concentrations of less-expressed genes that are not captured in the reverse transcription process. The percentage of mRNA molecules in the cell lysate that are detected is often only 10-20%.

When using RNA spike-ins for normalization the assumption is made that the amplification and sequencing efficiencies for the endogenous and spike-in RNA are the same. Evidence suggests that this is not the case given fundamental differences in size and features, such as the lack of a polyadenylated tail in spike-ins and therefore shorter length. Additionally, normalization using UMIs assumes the cDNA library is sequenced to saturation, which is not always the case.

In the amplification step, either PCR or in vitro transcription (IVT) is currently used to amplify cDNA. One of the advantages of PCR-based methods is the ability to generate full-length cDNA. However, different PCR efficiency on particular sequences (for instance, GC content and snapback structure) may also be exponentially amplified, producing libraries with uneven coverage. On the other hand, while libraries generated by IVT can avoid PCR-induced sequence bias, specific sequences may be transcribed inefficiently, thus causing sequence drop-out or generating incomplete sequences.

Challenges for scRNA-Seq include preserving the initial relative abundance of mRNA in a cell and identifying rare transcripts. The reverse transcription step is critical as the efficiency of the RT reaction determines how much of the cell's RNA population will be eventually analyzed by the sequencer. The processivity of reverse transcriptases and the priming strategies used may affect full-length cDNA production and the generation of libraries biased toward the 3' or 5' end of genes.

A further consideration when sequencing large, branched cell types, such as neurons, comes from the removal of distal processes containing local pools of RNA during the single-cell isolation process. In these cells, scRNA-seq datasets only capture transcript in the central cell body, omitting transcripts from RNA pools localized to cellular processes that can be involved in local translation or other RNA-mediated subcellular mechanisms. In the brain it has been estimated that over 40% of total RNA is not sequenced by scRNA-seq due to the prevalence of local transcriptomes in cellular processes such as axons, dendrites, myelin, and endfeet.

## Data analysis

Insights based on single-cell data analysis assume that the input is a matrix of normalized gene expression counts, generated by the approaches outlined above, and can provide opportunities that are not obtainable by bulk.

Three main insights provided:

1. Identification and characterization of cell types and their spatial organisation in time
2. Inference of gene regulatory networks and their strength across individual cells
3. Classification of the stochastic component of transcription

The techniques outlined have been designed to help visualise and explore patterns in the data in order to facilitate the revelation of these three features.

### Clustering

Clustering allows for the formation of subgroups in the cell population. Cells can be clustered by their transcriptomic profile in order to analyse the sub-population structure and identify rare cell types or cell subtypes. Alternatively, genes can be clustered by their expression states in order to identify covarying genes. A combination of both clustering approaches, known as biclustering, has been used to simultaneously cluster by genes and cells to find genes that behave similarly within cell clusters.

Clustering methods applied can be K-means clustering, forming disjoint groups or Hierarchical clustering, forming nested partitions.

#### Biclustering

Biclustering provides several advantages by improving the resolution of clustering. Genes that are only informative to a subset of cells and are hence only expressed there can be identified through biclustering. Moreover, similarly behaving genes that differentiate one cell cluster from another can be identified using this method.

### Dimensionality reduction

Dimensionality reduction algorithms such as Principal component analysis (PCA) and t-SNE can be used to simplify data for visualisation and pattern detection by transforming cells from a high to a lower dimensional space. The result of this method produces graphs with each cell as a point in a 2-D or 3-D space. Dimensionality reduction is frequently used before clustering as cells in high dimensions can wrongly appear to be close due to distance metrics behaving non-intuitively.

#### Principal component analysis

The most frequently used technique is PCA, which identifies the directions of largest variance principal components and transforms the data so that the first principal component has the largest possible variance, and successive principle components in turn each have the highest variance possible while remaining orthogonal to the preceding components. The contribution each gene makes to each component is used to infer which genes are contributing the most to variance in the population and are involved in differentiating different subpopulations.

### Differential expression

Detecting differences in gene expression level between two populations is used both single-cell and bulk transcriptomic data. Specialised methods have been designed for single-cell data that considers single cell features such as technical dropouts and shape of the distribution e.g. Bimodal vs. unimodal.

#### Gene ontology enrichment

Gene ontology terms describe gene functions and the relationships between those functions into three classes:

1. Molecular function
2. Cellular component
3. Biological process

Gene Ontology (GO) term enrichment is a technique used to identify which GO terms are over-represented or under-represented in a given set of genes. In single-cell analysis input list of genes of interest can be selected based on differentially expressed genes or groups of genes generated from biclustering. The number of genes annotated to a GO term in the input list is normalized against the number of genes annotated to a GO term in the background set of all genes in genome to determine statistical significance.

### Pseudotemporal ordering

Pseudo-temporal ordering (or trajectory inference) is a technique that aims to infer gene expression dynamics from snapshot single-cell data. The method tries to order the cells in such a way that similar cells are closely positioned to each other. This trajectory of cells can be linear, but can also bifurcate or follow more complex graph structures. The trajectory, therefore, enables the inference of gene expression dynamics and the ordering of cells by their progression through differentiation or response to external stimuli. The method relies on the assumptions that the cells follow the same path through the process of interest and that their transcriptional state correlates to their progression. The algorithm can be applied to both mixed populations and temporal samples.

More than 50 methods for pseudo-temporal ordering have been developed, and each has its own requirements for prior information (such as starting cells or time course data), detectable topologies, and methodology. An example algorithm is the Monocle algorithm that carries out dimensionality reduction of the data, builds a minimal spanning tree using the transformed data, orders cells in pseudo-time by following the longest connected path of the tree and consequently labels cells by type. Another example is the diffusion pseudotime (DPT) algorithm, which uses a diffusion map and diffusion process. Another class of methods such as MARGARET employ graph partitioning for capturing complex trajectory topologies such as disconnected and multifurcating trajectories.

### Network inference

Gene regulatory network inference is a technique that aims to construct a network, shown as a graph, in which the nodes represent the genes and edges indicate co-regulatory interactions. The method relies on the assumption that a strong statistical relationship between the expression of genes is an indication of a potential functional relationship. The most commonly used method to measure the strength of a statistical relationship is correlation. However, correlation fails to identify non-linear relationships and mutual information is used as an alternative. Gene clusters linked in a network signify genes that undergo coordinated changes in expression.

### Integration

The presence or strength of technical effects and the types of cells observed often differ in single-cell transcriptomics datasets generated using different experimental protocols and under different conditions. This difference results in strong batch effects that may bias the findings of statistical methods applied across batches, particularly in the presence of confounding. As a result of the aforementioned properties of single-cell transcriptomic data, batch correction methods developed for bulk sequencing data were observed to perform poorly. Consequently, researchers developed statistical methods to correct for batch effects that are robust to the properties of single-cell transcriptomic data to integrate data from different sources or experimental batches. Laleh Haghverdi performed foundational work in formulating the use of mutual nearest neighbors between each batch to define batch correction vectors. With these vectors, one can merge datasets that each include at least one shared cell type. An orthogonal approach involves the projection of each dataset onto a shared low-dimensional space using canonical correlation analysis. Mutual nearest neighbors and canonical correlation analysis have also been combined to define integration "anchors" comprising reference cells in one dataset, to which query cells in another dataset are normalized. Another class of methods (e.g., scDREAMER) uses deep generative models such as variational autoencoders for learning batch-invariant latent cellular representations which can be used for downstream tasks such as cell type clustering, denoising of single-cell gene expression vectors and trajectory inference.

**Cell-cell Communication**

Cell-cell communication tools leverage the expression of cognate ligand and receptor pairs in distinct cell pairs to predict putative interactions between cells. A pioneer tool is CellPhoneDB, which included a curate database of receptor complexes and ligand-receptor interactions. The method also implemented a statistical test by evaluating the expression of the ligand-receptor in the respective cell pair. One interesting advanced analysis is at scenarios when two conditions (disease vs. controls) are available. Here, one is interested in finding cell-cell interactions specific to disease or control conditions.

**Analysis of Disease Atlas**

With the lowering of single cell cost, it is possible to measure single cell data over large disease cohorts with up to 100 individual samples and million of cells. This brings several challenges such as individual variability and the multi-scale properties of the data, every single cell experiment represents a distribution of cells. MILO tackle individual variability by encoding single cell data as a k-nn graph followed by a differential abundance test. This allows to find cellular neighboorhoods associated to a particular disease condition. Optimal transport theory is another represents another framework to tackle multi-scale nature of single cell diseae atlas. By encoding single cell experiments of an patient as a distribution of cells, optimal transport based Wasserstein distance allows to measure a distance between two patient. This can be used for sample level clustering and trajectory analysis as explored by PILOT and QOT.

**Software frameworks**

An important pilar of single cell analysis are software packages providing functionally for quality check, normalization, clustering and down-stream analysis described above. They also provide data containers for the storage and representation of analysed single cell data. Seurat is the first and possibly most complete frameworks for single cell analysis. Scanpy is an alternative for python language. Additional software package offer specific data analysis taks. Notable examples is LIANA+ for cell-cell communication analysis, scVI as a package offering variational autoencoders for analysis of single cell data, and PILOT as a package for sample level analysis of disease atlas
