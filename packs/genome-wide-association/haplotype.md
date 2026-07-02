---
title: "Haplotype"
source: https://en.wikipedia.org/wiki/Haplotype
domain: genome-wide-association
license: CC-BY-SA-4.0
tags: genome wide association, gwas study, single nucleotide polymorphism, linkage disequilibrium
fetched: 2026-07-02
---

# Haplotype

A **haplotype** (haploid genotype) is a group of alleles in an organism that are inherited together from a single parent.

Many organisms contain genetic material (DNA) which is inherited from two parents. Normally these organisms have their DNA organized in two sets of pairwise similar chromosomes. The offspring gets one chromosome in each pair from each parent. A set of pairs of chromosomes is called diploid and a set of only one half of each pair is called haploid. The haploid genotype (haplotype) is a genotype that considers the singular chromosomes rather than the pairs of chromosomes. It can be all the chromosomes from one of the parents or a minor part of a chromosome, for example a sequence of 9000 base pairs or a small set of alleles.

Specific contiguous parts of the chromosome are likely to be inherited together and not be split by chromosomal crossover, a phenomenon called genetic linkage. As a result, identifying these statistical associations and a few alleles of a specific haplotype sequence can facilitate identifying *all other such* polymorphic sites that are nearby on the chromosome (imputation). Such information is critical for investigating the genetics of common diseases; which have been investigated in humans by the International HapMap Project.

Other parts of the genome are almost always haploid and do not undergo crossover: for example, human mitochondrial DNA is passed down through the maternal line, and the Y chromosome is passed down the paternal line. In these cases, the entire sequence can be grouped into a simple evolutionary tree, with each branch founded by a unique-event polymorphism mutation (often, but not always, a single-nucleotide polymorphism (SNP)). Each clade under a branch, containing haplotypes with a single shared ancestor, is called a haplogroup.

## Haplotype resolution

An organism's genotype may not define its haplotype uniquely. For example, consider a diploid organism and two bi-allelic loci (such as SNPs) on the same chromosome. Assume the first locus has alleles *A* or *T* and the second locus *G* or *C*. Both loci, then, have three possible genotypes: (*AA*, *AT*, and *TT*) and (*GG*, *GC*, and *CC*), respectively. For a given individual, there are nine possible configurations (haplotypes) at these two loci (shown in the Punnett square below). For individuals who are homozygous at one or both loci, the haplotypes are unambiguous - meaning that there is not any differentiation of haplotype T1T2 vs haplotype T2T1; where T1 and T2 are labeled to show that they are the same locus, but labeled as such to show it does not matter which order you consider them in, the end result is two T loci. For individuals heterozygous at both loci, the gametic phase is ambiguous - in these cases, an observer does not know which haplotype the individual has, e.g., TA vs AT.

| Locus 1Locus 2 | AA | AT | TT |
|---|---|---|---|
| GG | AG AG | AG TG | TG TG |
| GC | AG AC | AG TC or AC TG | TG TC |
| CC | AC AC | AC TC | TC TC |

The only unequivocal method of resolving phase ambiguity is by sequencing. However, it is possible to estimate the probability of a particular haplotype when phase is ambiguous using a sample of individuals.

Given the genotypes for a number of individuals, the haplotypes can be inferred by haplotype resolution or haplotype phasing techniques. These methods work by applying the observation that certain haplotypes are common in certain genomic regions. Therefore, given a set of possible haplotype resolutions, these methods choose those that use fewer different haplotypes overall. The specifics of these methods vary - some are based on combinatorial approaches (e.g., parsimony), whereas others use likelihood functions based on different models and assumptions such as the Hardy–Weinberg principle, the coalescent theory model, or perfect phylogeny. The parameters in these models are then estimated using algorithms such as the expectation-maximization algorithm (EM), Markov chain Monte Carlo (MCMC), or hidden Markov models (HMM).

Microfluidic whole genome haplotyping is a technique for the physical separation of individual chromosomes from a metaphase cell followed by direct resolution of the haplotype for each allele.

### Gametic phase

In genetics, a **gametic phase** represents the original allelic combinations that a diploid individual inherits from both parents. It is therefore a particular association of alleles at different loci on the same chromosome. Gametic phase is influenced by genetic linkage.

## Y-DNA haplotypes from genealogical DNA tests

Unlike other chromosomes, Y chromosomes generally do not come in pairs. Every human male (excepting those with XYY syndrome) has only one copy of that chromosome. This means that there is not any chance variation of which copy is inherited, and also (for most of the chromosome) not any shuffling between copies by recombination; so, unlike autosomal haplotypes, there is effectively not any randomisation of the Y-chromosome haplotype between generations. A human male should largely share the same Y chromosome as his father, give or take a few mutations; thus Y chromosomes tend to pass largely intact from father to son, with a small but accumulating number of mutations that can serve to differentiate male lineages. In particular, the Y-DNA represented as the numbered results of a Y-DNA genealogical DNA test should match, except for mutations.

### UEP results (SNP results)

Unique-event polymorphisms (UEPs) such as SNPs represent haplogroups. STRs represent haplotypes. The results that comprise the full Y-DNA haplotype from the Y chromosome DNA test can be divided into two parts: the results for UEPs, sometimes loosely called the SNP results as most UEPs are single-nucleotide polymorphisms, and the results for microsatellite short tandem repeat sequences (Y-STRs).

The UEP results represent the inheritance of events it is believed can be assumed to have happened only once in all human history. These can be used to identify the individual's Y-DNA haplogroup, his place in the "family tree" of the whole of humanity. Different Y-DNA haplogroups identify genetic populations that are often distinctly associated with particular geographic regions; their appearance in more recent populations located in different regions represents the migrations tens of thousands of years ago of the direct patrilineal ancestors of current individuals.

### Y-STR haplotypes

Genetic results also include the **Y-STR haplotype**, the set of results from the Y-STR markers tested.

Unlike the UEPs, the Y-STRs mutate much more easily, which allows them to be used to distinguish recent genealogy. But it also means that, rather than the population of descendants of a genetic event all sharing the *same* result, the Y-STR haplotypes are likely to have spread apart, to form a *cluster* of more or less similar results. Typically, this cluster will have a definite most probable center, the **modal haplotype** (presumably similar to the haplotype of the original founding event), and also a **haplotype diversity** — the degree to which it has become spread out. The further in the past the defining event occurred, and the more that subsequent population growth occurred early, the greater the haplotype diversity will be for a particular number of descendants. However, if the haplotype diversity is smaller for a particular number of descendants, this may indicate a more recent common ancestor, or a recent population expansion.

Unlike for UEPs, two individuals with a similar Y-STR haplotype may not necessarily share a similar ancestry. Y-STR events are not unique. Instead, the clusters of Y-STR haplotype results inherited from different events and different histories tend to overlap.

In most cases, it is a long time since the haplogroups' defining events, so typically the cluster of Y-STR haplotype results associated with descendants of that event has become rather broad. These results will tend to significantly overlap the (similarly broad) clusters of Y-STR haplotypes associated with other haplogroups. This makes it impossible for researchers to predict with absolute certainty to which Y-DNA haplogroup a Y-STR haplotype would point. If the UEPs are not tested, the Y-STRs may be used only to predict probabilities for haplogroup ancestry, but not certainties.

A similar scenario exists in trying to evaluate whether shared surnames indicate shared genetic ancestry. A cluster of similar Y-STR haplotypes may indicate a shared common ancestor, with an identifiable modal haplotype, but only if the cluster is sufficiently distinct from what may have happened by chance from different individuals who historically adopted the same name independently. Many names were adopted from common occupations, for instance, or were associated with habitation of particular sites. More extensive haplotype typing is needed to establish genetic genealogy. Commercial DNA-testing companies now offer their customers testing of more numerous sets of markers to improve definition of their genetic ancestry. The number of sets of markers tested has increased from 12 during the early years to 111 more recently.

Establishing plausible relatedness between different surnames data-mined from a database is significantly more difficult. The researcher must establish that the *very nearest* member of the population in question, chosen purposely from the population for that reason, would be unlikely to match by accident. This is more than establishing that a *randomly selected* member of the population is unlikely to have such a close match by accident. Because of the difficulty, establishing relatedness between different surnames as in such a scenario is likely to be impossible, except in special cases where there is specific information to drastically limit the size of the population of candidates under consideration.

## Diversity

Haplotype diversity is a measure of the uniqueness of a particular haplotype in a given population. The haplotype diversity (H) is computed as: $H={\frac {N}{N-1}}(1-\sum _{i}x_{i}^{2})$ where $x_{i}$ is the (relative) haplotype frequency of each haplotype in the sample and N is the sample size. Haplotype diversity is given for each sample.

## History

The term "haplotype" was first introduced by MHC biologist Ruggero Ceppellini during the Third International Histocompatibility Workshop to substitute "pheno-group".
