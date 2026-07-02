---
title: "Cellular deconvolution"
source: https://en.wikipedia.org/wiki/Cellular_deconvolution
domain: single-cell-sequencing
license: CC-BY-SA-4.0
tags: single cell rna, cell barcoding, droplet microfluidics, unique molecular identifier
fetched: 2026-07-02
---

# Cellular deconvolution

**Cellular deconvolution** (also referred to as **cell type composition** or **cell proportion estimation**) refers to computational techniques aiming at estimating the proportions of different cell types in samples collected from a tissue. For example, samples collected from the human brain are a mixture of various neuronal and glial cell types (e.g. microglia and astrocytes) in different proportions, where each cell type has a diverse gene expression profile. Since most high-throughput technologies use bulk samples and measure the aggregated levels of molecular information (e.g. expression levels of genes) for all cells in a sample, the measured values would be an aggregate of the values pertaining to the expression landscape of different cell types. Therefore, many downstream analyses such as differential gene expression might be confounded by the variations in cell type proportions when using the output of high-throughput technologies applied to bulk samples. The development of statistical methods to identify cell type proportions in large-scale bulk samples is an important step for better understanding of the relationship between cell type composition and diseases.

Cellular deconvolution algorithms have been applied to a variety of samples collected from saliva, buccal, cervical, PBMC, brain, kidney, and pancreatic cells, and many studies have shown that estimating and incorporating the proportions of cell types into various analyses improves the interpretability of high-throughput omics data and reduces the confounding effects of cellular heterogeneity, also known as tissue heterogeneity, in functional analysis of omics data.

## Mathematical Formulation

Most cellular deconvolution algorithms consider an input data in a form of a matrix $X_{m\times n}$ , which represents some molecular information (e.g. gene expression data or DNA methylation data) measured over a group of n samples and m marks (e.g. genes or CpG sites). The goal of the algorithm is to use these data and return an output matrix $W_{k\times n}$ , representing the proportions of k distinct cell types in each of the n samples. Some methods limit the sum of each column of W matrix less than or equal to one, so that the proportions of cell types sum up to the overall number of cells in the sample (less than one when there are some unknown cell types in the samples). Moreover, it is assumed that the values of W matrix are non-negative as they pertain to proportions of cell types.

## Current strategies

There are two broad categories of methods aiming at estimating the proportion of cell types in samples using some type of omics data (bulk gene expression or DNA methylation data). These approaches are labeled as reference-based (also called supervised) and reference-free (also called unsupervised) methods

### Reference-based methods

Reference-based methods require an a *priori* defined reference matrix consisting of the expected value (also called profile or signature) of gene expression (or DNA methylation) for a group of genes (or CpG sites) known to have a differential expression (or methylation)

across the cell types. A reference matrix can be represented by a matrix $H_{m\times k}$ , representing the expected value for m markers (genes or CpG sites) for each of k cell types known to be presented in the samples. These references can be derived by exploring external single-cell epigenomics or transcriptomics datasets generated for a group of samples similar (e.g. in terms of biological condition, sex and age) to the samples for which the deconvolution method will be applied. These methods use statistical approaches such as non-negative or constrained linear regression methods to dissect the contribution of each cell type to the aggregated bulk signals of genes or CpG sites. Constrained regression is the basis for many of reference-free cellular deconvolution methods existing in the literature, aiming at estimating the cell proportion values ( $W_{k\times n}$ ) that maximizes the similarity between $HW^{T}$ and X . The performance of reference-based methods depends critically on the quality of the reference profiles.

#### Construction of reference profiles

There are a variety of approaches for isolating different cell types to measure their gene expression or DNA methylation levels to be used as references in the deconvolution algorithms. Earlier methods used cell sorting methods such as FACS (fluorescence-activated cell sorting) based on the flow cytometry technique, which separates the populations of cells belonging to different cell types based on their cell sizes, morphologies (shape), and surface protein expressions. With the advance in single-cell technologies, newer approaches started to incorporate references for cell-types measured on a single-cell resolution obtained for a subset of subjects in the study or external subjects from a similar biological condition.

### Reference-free methods

Reference-free methods do not need the reference profiles of cell-type specific genes (or CpGs), although they might still require the identity (name) of cell-type-specific genes (or CpGs). These methods might be considered as a modification of reference-based methods where **both** H and W are unknown, and the goal is to jointly estimate both matrices so that the similarity between $HW^{T}$ and X is maximized. Many of the reference-free methods are based on mathematical framework of non-negative matrix factorization, which imposes a non-negativity constraint on the elements of H and W . Additional constraints such as the assumption of orthogonality between the columns of H might be incorporated to improve the interpretability of results and prevent overfitting.

|   | Title | Category | Input Data Type | Year |
|---|---|---|---|---|
| CIBERSORT | Robust enumeration of cell subsets from tissue expression profiles | Reference based | Gene expression | 2018 |
| CDSeq | A complete deconvolution method for dissecting tissue heterogeneity | Reference free | Gene expression | 2019 |
| FARDEEP | Fast and robust deconvolution of expression profiles | Reference based | Gene expression | 2019 |
| UNDO | Unsupervised deconvolution of tumor-stromal mixed expressions | Reference free | Gene expression | 2015 |
| dtangle | Accurate and robust cell type deconvolution | Reference based | Gene expression | 2019 |
| EPIC | Estimating the proportions of different cell types from bulk gene expression data | Reference based | Gene expression | 2017 |
| BSEQ-sc | Deconvolution of bulk sequencing experiments using single cell data | Reference based | Gene expression | 2016 |
| MuSiC | Cell-type Identification by estimating relative subsets of RNA transcripts | Reference based | Gene expression | 2019 |
| SCDC | Bulk gene expression deconvolution by multiple single-Cell RNA sequencing references | Reference based | Gene expression | 2020 |
| DWLS | Gene expression deconvolution using dampened weighted least squares | Reference based | Gene expression | 2019 |
| deconvSeq | Deconvolution of cell mixture distribution in sequencing data | Reference based | Gene expression | 2019 |
| Bisque | Decomposition of bulk expression with single-cell sequencing | Reference based | Gene expression | 2020 |
| TOAST | Tools for the analysis of heterogeneous tissues | Reference free | DNA methylation | 2019 |
| Houseman | Reference-free deconvolution of DNA methylation data and mediation by cell composition effects | Reference based | DNA methylation | 2016 |
| methylCC | Technology-independent estimation of cell type composition using differentially methylated regions | Reference based | DNA methylation | 2019 |
| BayesCCE | Bayesian framework for estimating cell-type composition from DNA methylation | Reference free | DNA methylation | 2018 |

## Advantages and limitations

### Advantages

#### In silico cell-type level resolution

The advance of single-cell technologies enables the profiling of each individual cell in a sample, which help elucidate the issue of cellular heterogeneity by measuring the proportions of different cells in samples. Even though the quality of single cell profiling technologies has been on the rise in recent years, these technologies are still costly, limiting their applications in large populations of samples. Single cell technologies such as single cell transcriptomic methods also tend to have higher error rates due to factors such as high dropout events. Cellular deconvolution methods provide a robust and cost-effective *in silico* alternatives for understanding the samples on a cell-type level resolution, by relying on single cell information of only a small subset of cells in the sample, the reference profiles generated by external sources, or even no reference profile at all.

#### (Re)analysis of old data

There are large amounts of old bulk data, such as microarray, from studies concerning various diseases and biological conditions. These datasets could be considered important resources in studying of rare disease, long follow-up studies or samples and tissues that are difficult to extract. In addition, this can also improve the statistical power by combining similar datasets. Since the biological samples for many of these studies are not available or accessible anymore, reprofiling the data using single cell technologies might not be within the realm of possibilities for many studies. Invention of more advanced cellular deconvolution methods gives the opportunity to researchers to come back to old omics studies, reanalyze their datasets, and scrutinize their findings.

### Limitations

#### Reliability of reference

Reference-based approaches rely on the availability of accurate references to estimate cell proportions. The discrepancy between the biology of the samples underlying the references and the samples for which the cell proportions are being estimated could introduce bias in estimated cell proportions. Studies have shown that using references obtained from samples with different phenotypes such as age, gender, and disease status than the population of interest reduces the performance of reference-based methods to levels lower than their reference-free counterparts.

#### Lack of reference for rare, unknown, or uncharacterized cell types

Reference-based approaches assume the existence of prior knowledge on the types of cells existing in a sample. Therefore, these methods may fail to perform accurately when the data includes rare or otherwise unknown cell types with no references incorporated in the algorithm. For example, cancer tumors consist of heterogeneous mixtures of various healthy cells of different types such as immune cells and cells related to affected tissues in addition to tumor cells. Although it might be possible to provide references for the immune cells, we do not usually have access to references or signatures for cancer cells due to the unique patterns of mutations and distributions of molecular information in each individual. These situations have been addressed in some studies under the label of deconvolution methods with partial reference availability.

## Applications

### Relationship between cell proportions and phenotypes

Studies have shown that the proportions of different cell types might show correlations with various phenotypes such as different diseases. For example, the proportions of Parathyroid oxyphil cells in the samples collected from the parathyroid gland for groups of patients show a significant correlation with the presence of clinical characteristics of chronic kidney disease (CKD). Another study applying the cellular deconvolution algorithms to gene expression data of Alzheimer's patients find that patients with lower proportions of neuronal cells in the samples collected from their cerebral cortex are more likely to show the clinical characteristics of dementia. Cellular deconvolution algorithms could enable researchers to investigate the interactions between cell proportions and various diseases or biological phenotypes.

### Dissecting the confounding effects of cell proportions in EWAS and TWAS studies

Epigenome-wide association study (EWAS) and transcriptome-wide association studies (TWAS) aim at finding the molecular markers such as genes or methylation CpG sites that show significant correlations between their expression or methylation levels and a biological phenotype of interest such as a disease. Since the proportions of cell types in samples vary and might show significant correlations with the disease or phenotype of interest, these correlations may confound the functional relationships between genes or CpG sites and the disease or phenotypes under study. For example, studies aimed at finding genes involved in Alzheimer's disease may end up selecting genes that are exclusively expressed in neurons and therefore have lower expression levels in Alzheimer's patients due to compositional changes of cell types during neurodegeneration. Such genes are not actionable targets for the treatment of Alzheimer's since they are not causally involved in the biological mechanism underlying Alzheimer's disease, but are only brought up by the confounding effects of cell types.
