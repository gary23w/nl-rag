---
title: "Fixation index"
source: https://en.wikipedia.org/wiki/Fixation_index
domain: population-genetics
license: CC-BY-SA-4.0
tags: population genetics, hardy-weinberg principle, coalescent theory, linkage disequilibrium
fetched: 2026-07-02
---

# Fixation index

The **fixation index** (**FST**) is a measure of population differentiation due to genetic structure. It is frequently estimated from genetic polymorphism data, such as single-nucleotide polymorphisms (SNP) or microsatellites. Developed as a special case of Wright's F-statistics, it is one of the most commonly used statistics in population genetics. Its values range from 0 to 1, with 0 being no differentiation and 1 being complete differentiation.

## Interpretation

This comparison of genetic variability within and between populations is frequently used in applied population genetics. The values range from 0 to 1. A zero value implies complete panmixia; that is, that the two populations are interbreeding freely. A value of one implies that all genetic variation is explained by the population structure, and that the two populations do not share any genetic diversity.

For idealized models such as Wright's finite island model, FST can be used to estimate migration rates. Under that model, the migration rate is

$M={\frac {m}{\mu }}\approx {\frac {1}{4}}\left({\frac {1}{F_{ST}}}-1\right)$

,

where m is the migration rate per generation, and $\mu$ is the mutation rate per generation.

The interpretation of FST can be difficult when the data analyzed are highly polymorphic. In this case, the probability of identity by descent is very low and FST can have an arbitrarily low upper bound, which might lead to misinterpretation of the data. Also, strictly speaking FST is not a distance in the mathematical sense, as it does not satisfy the triangle inequality.

## Definition

Two of the most commonly used definitions for FST at a given locus are based on 1) the variance of allele frequencies among populations, and on 2) the probability of identity by descent.

If ${\bar {p}}$ is the average frequency of an allele in the total population, $\sigma _{S}^{2}$ is the variance in the frequency of the allele among different subpopulations, weighted by the sizes of the subpopulations, and $\sigma _{T}^{2}$ is the variance of the allelic state in the total population, FST is defined as

$F_{ST}={\frac {\sigma _{S}^{2}}{\sigma _{T}^{2}}}={\frac {\sigma _{S}^{2}}{{\bar {p}}(1-{\bar {p}})}}$

Wright's definition illustrates that FST measures the amount of genetic variance that can be explained by population structure. This can also be thought of as the fraction of total diversity that is not a consequence of the average diversity within subpopulations, where diversity is measured by the probability that two randomly selected alleles are different, namely $2p(1-p)$ . If the allele frequency in the i th population is $p_{i}$ and the relative size of the i th population is $c_{i}$ , then

$F_{ST}={\frac {{\bar {p}}(1-{\bar {p}})-\sum c_{i}p_{i}(1-p_{i})}{{\bar {p}}(1-{\bar {p}})}}={\frac {{\bar {p}}(1-{\bar {p}})-{\overline {p(1-p)}}}{{\bar {p}}(1-{\bar {p}})}}$

Alternatively,

$F_{ST}={\frac {f_{0}-{\bar {f}}}{1-{\bar {f}}}}$

where $f_{0}$ is the probability of identity by descent of two individuals given that the two individuals are in the same subpopulation, and ${\bar {f}}$ is the probability that two individuals from the total population are identical by descent. Using this definition, FST can be interpreted as measuring how much closer two individuals from the same subpopulation are, compared to the total population. If the mutation rate is small, this interpretation can be made more explicit by linking the probability of identity by descent to coalescent times: Let T0 and T denote the average time to coalescence for individuals from the same subpopulation and the total population, respectively. Then,

$F_{ST}\approx 1-{\frac {T_{0}}{T}}$

This formulation has the advantage that the expected time to coalescence can easily be estimated from genetic data, which led to the development of various estimators for FST.

## Estimation

In practice, none of the quantities used for the definitions can be easily measured. As a consequence, various estimators have been proposed. A particularly simple estimator applicable to DNA sequence data is:

$F_{ST}={\frac {\pi _{\text{Between}}-\pi _{\text{Within}}}{\pi _{\text{Between}}}}$

where $\pi _{\text{Between}}$ and $\pi _{\text{Within}}$ represent the average number of pairwise differences between two individuals sampled from different sub-populations ( $\pi _{\text{Between}}$ ) or from the same sub-population ( $\pi _{\text{Within}}$ ). The average pairwise difference within a population can be calculated as the sum of the pairwise differences divided by the number of pairs. However, this estimator is biased when sample sizes are small or if they vary between populations. Therefore, more elaborate methods are used to compute FST in practice. Two of the most widely used procedures are the estimator by Weir & Cockerham (1984), or performing an Analysis of molecular variance. A list of implementations is available at the end of this article.

## FST in humans

FST values depend strongly on the choice of populations. Closely related ethnic groups, such as the Danes vs. the Dutch, or the Portuguese vs. the Spaniards show values significantly below 1%, indistinguishable from panmixia. Within Europe, the most divergent ethnic groups have been found to have values of the order of 7% (Sámi vs. Sardinians).

Larger values are found if highly divergent homogenous groups are compared: the highest such value found was at close to 46%, between Mbuti and Papuans.

## Genetic distances in human populations

### Autosomal genetic distances based on classical markers

In their study *The History and Geography of Human Genes (1994)*, Cavalli-Sforza, Menozzi and Piazza provide some of the most detailed and comprehensive estimates of genetic distances between human populations, within and across continents. Their initial database contains 76,676 gene frequencies (using 120 blood polymorphisms), corresponding to 6,633 samples in different locations. By culling and pooling such samples, they restrict their analysis to 491 populations.

They focus on *aboriginal populations* that were at their present location at the end of the 15th century when the great European migrations began. When studying genetic difference at the world level, the number is reduced to 42 representative populations, aggregating subpopulations characterized by a high level of genetic similarity. For these 42 populations, Cavalli-Sforza and coauthors report bilateral distances computed from 120 alleles. Among this set of 42 world populations, the greatest genetic distance observed is between Mbuti Pygmies and Papua New Guineans, where the Fst distance is 0.4573, while the smallest genetic distance (0.0021) is between the Danish and the English.

When considering more disaggregated data for 26 European populations, the smallest genetic distance (0.0009) is between the Dutch and the Danes, and the largest (0.0667) is between the Lapps and the Sardinians. The mean genetic distance among the 861 available pairings of the 42 selected populations was found to be 0.1338..

The following table shows Fst calculated by Cavalli-Sforza (1994) for some populations:

Bantu

Nio-Saharan

W. African

Mbuti

Japanese

Korean

Thai

Filipino

S. Chinese

Danish

English

Melanesian

New Guinean

Australian

Bantu

0.00

Nio-Saharan

0.01

0.00

W. African

0.02

0.02

0.00

Mbuti

0.07

0.08

0.08

0.00

Japanese

0.24

0.25

0.23

0.31

0.00

Korean

0.27

0.24

0.18

0.30

0.01

0.00

Thai

0.34

0.30

0.25

0.39

0.07

0.06

0.00

Filipino

0.29

0.30

0.23

0.38

0.10

0.12

0.06

0.00

S. Chinese

0.30

0.29

0.20

0.34

0.05

0.05

0.01

0.03

0.00

Danish

0.17

0.17

0.15

0.15

0.12

0.09

0.13

0.13

0.13

0.00

English

0.23

0.18

0.15

0.24

0.12

0.10

0.11

0.11

0.12

0.00

0.00

Melanesian

0.34

0.31

0.27

0.40

0.11

0.11

0.08

0.05

0.06

0.14

0.16

0.00

New Guinean

0.34

0.33

0.28

0.46

0.12

0.14

0.18

0.13

0.15

0.16

0.16

0.07

0.00

Australian

0.33

0.36

0.27

0.43

0.06

0.07

0.13

0.13

0.11

0.14

0.15

0.11

0.10

0.00

### Autosomal genetic distances based on SNPs

A 2012 study based on International HapMap Project data estimated FST between the three major "continental" populations of Europeans (combined from Utah residents of Northern and Western European ancestry from the CEPH collection and Italians from Tuscany), East Asians (combining Han Chinese from Beijing, Chinese from metropolitan Denver and Japanese from Tokyo, Japan) and Sub-Saharan Africans (combining Luhya of Webuye, Kenya, Maasai of Kinyawa, Kenya and Yoruba of Ibadan, Nigeria). It reported a value close to 12% between continental populations, and values close to panmixia (smaller than 1%) within continental populations.

|   | Europe (CEU) | Sub-Saharan Africa (Yoruba) | East-Asia (Japanese) |
|---|---|---|---|
| Sub-Saharan Africa (Yoruba) | 0.153 |   |   |
| East-Asia (Japanese) | 0.111 | 0.190 |   |
| East-Asia (Chinese) | 0.110 | 0.192 | 0.007 |

Intra-European/mediterranean autosomal genetic distances based on SNPs

Italians

Palestinians

Swedish

Finns

Spanish

Germans

Russians

French

Greeks

Palestinians

0.0064

Swedish

0.0064-0.0090

0.0191

Finns

0.0130-0.0230

0.0050-0.0110

Spanish

0.0010-0.0050

0.0101

0.0040-0055

0.0110-0.0170

Germans

0.0029-0.0080

0.0136

0.0007-0.0010

0.0060-0.0130

0.0015-0.0030

Russians

0.0088-0.0120

0.0202

0.0030-0.0036

0.0060-0.0120

0.0070-0.0079

0.0030-0.0037

French

0.0030-0.0050

0.0020

0.0080-0.0150

0.0010

0.0010

0.0050

Greeks

0.0000

0.0057

0.0084

0.0035

0.0039

0.0108

### Autosomal genetic distances based on whole exome sequencing (WES)

Pairwise Fst values among several populations based on whole exome sequencing (WES) in 2016:

## Programs for calculating FST

- Arlequin
- Fstat
- SMOGD
- diveRsity (R package)
- hierfstat (R package)
- FinePop (R package)
- Microsatellite Analyzer (MSA) Archived 2015-03-29 at the Wayback Machine
- VCFtools
- DnaSP
- Popoolation2

## Modules for calculating FST

- BioPerl
- BioPython
