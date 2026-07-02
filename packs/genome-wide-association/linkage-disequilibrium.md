---
title: "Linkage disequilibrium"
source: https://en.wikipedia.org/wiki/Linkage_disequilibrium
domain: genome-wide-association
license: CC-BY-SA-4.0
tags: genome wide association, gwas study, single nucleotide polymorphism, linkage disequilibrium
fetched: 2026-07-02
---

# Linkage disequilibrium

**Linkage disequilibrium**, often abbreviated to LD, is a term in population genetics referring to the association of genes, usually linked genes, in a population. It has become an important tool in medical genetics and other fields.

In defining LD, it is important first to distinguish two different concepts: linkage disequilibrium and linkage (genetic linkage). Linkage disequilibrium refers to the association of genes *in a population.* Linkage, on the other hand, tells us whether genes are on the same chromosome *in an individual*. There is no necessary relationship between the two. Genes that are closely linked may or may not be associated in populations. Looking at parents and offspring, if genes at closely linked loci are present together in the parent, then they will usually be found together in the offspring. But looking at individuals in a population with no known common ancestry, it is much more difficult to see any relationships.

To give a concrete, although imaginary, example in terms of frequencies of characters, consider a case where the "gene for red hair" is closely linked to the "gene for blue eyes". What does that tell us about the expected population frequency of individuals with red hair and blue eyes? Are all redheads expected to have blue eyes, just because the genes controlling these characters are closely linked?

## Formal definition

Consider an allele *A* at the *A* locus with frequency *pA* in a particular population. At a linked *B* locus, the frequency of the allele *B* is *pB*. The question is, what is the expected frequency *pAB* of the allele pair, or *haplotype*, *AB*? (See note below about genetic nomenclature.)

If the *A* and *B* alleles are independent in a population, then, by definition, *pAB* is simply the product *p*A*pB*. The difference between these two is given by *D*, the coefficient of linkage disequilbrium:

*D* = *pAB* - *pApB*

Departure of *D* from zero indicates LD.

## Note on genetic nomenclature

The descriptors "allele *A* at the *A* locus" and "allele *B* at the *B* locus" seem unnecessarily complicated. Why not just the "*A* gene" and the "*B* gene"? The problem is that the term "gene" has been used since the foundation of genetics without a clear understanding of what a gene actually is. So, despite its widespread popular usage, its use is now avoided in genetics journals (see for a discussion about the changing definition of the gene). This is unfortunate for discussions of population frequencies where the nature of the gene is not important.

Use of the term "allele" rather than "gene" sidesteps this problem, but in a way that is not entirely satisfactory. Allele was originally defined and still understood as meaning "alternative", and allele *A* and allele *B* are not alleles (of each other). The easiest way of talking about these linked "things" would be to use the term "gene".

## Historical

The expectation, dating back to 1918, is that LD is NOT to be expected, even for loci that are closely linked. Robbins showed that recombination is expected to decrease the value of *D* in each generation by a factor (1 - *c*), where *c* is the frequency of recombination.

If *D* between alleles at two loci at generation 0 is given the designation *D*0, then in the following generation :

*D*1 = *D*0 (1 - *c*)

and in generation *t* :

*Dt* = *D*0 (1 - *c*)*t*

If there is some recombination, *c* will be greater than zero, *Dt* approaches zero as *t* becomes large.

For the example given previously, no association is expected between hair colour and eye colour. The frequency of individuals who are both red-headed and blue-eyed is expected to become simply the product of the frequency of red-headed individuals multiplied by the frequency of blue-eyed individuals, despite the fact that the two characters are controlled by closely linked loci.

Selection provides one possible way in which LD might be expected, in spite of the above argument. If particular gene combinations are favoured, selection can cause LD to arise in the population, maintaining the frequency of the favoured gene combinations. Such "equilibrium models" require reasonably high levels of selection, specifically "selective interaction", which is only possible for a minority of gene pairs.

The term LD remains as a legacy from this period. It was introduced for cases where there is known recombination but where the population has not come to equilibrium for the gene pair in question. But the most prominent uses of LD now involve very closely linked DNA bases (see below). Independence cannot be expected in such cases. The 'disequilibrium' description seems inappropriate, with its implication that this situation is temporary and/or unexpected.

## The molecular era

The molecular era for population genetics can be said to date from 1966 following the studies of Lewontin and Hubby in Drosophila and Harris in humans. Using protein electrophoresis, these authors showed that around one third of loci must be 'polymorphic', having some genetic differences between individuals in the population. Given the large number of loci in the genome and the limited amount of recombination, it followed that there must be many very closely linked polymorphic loci.

Subsequent DNA sequencing, e.g. the International HapMap Project has shown that protein studies considerably underestimate the amount of polymorphism. There will usually be thousands of genetic differences, titled Single Nucleotide Polymorphism or SNPs, within short regions of the genome. Cases of zero or very low recombination must be common.

A second important finding pertaining to LD was the realisation that LD can arise simply because of population structure. Studies such as those of Robbins referred to above essentially assume an infinite population size. Small population size, in particular, can lead to LD quite independently of any selection. It became clear that LD, rather than being rare and of secondary importance, must be widespread.

This has had enormous importance in diverse fields of human genetics and animal breeding. It means that any gene of importance is likely to be surrounded by DNA SNPs in high LD with the gene of interest. The position of the gene may be unknown, but the position of all DNA SNPs is known exactly. This has allowed the mapping of causal genes in human genetics, using Genome-wide association studies (GWAS). It has allowed DNA 'breeding values' to be used as predictors, leading to advances in animal and plant breeding.

## LD as a covariance or correlation of frequencies

Haplotype frequencies can be set out in the form of a table with **x** and **y** columns. Allele *A* is given the value '1' and allele *a* the value '0' in the **x** column. Similarly for *B* in the **y** column. Gamete frequencies are of the form *gi*, summing to 1.

| Haplotype | x value | y value | frequency (*f*) |
|---|---|---|---|
| *AB* | 1 | 1 | *g*1 |
| *Ab* | 1 | 0 | *g*2 |
| *aB* | 0 | 1 | *g*3 |
| *ab* | 0 | 0 | *g*4 |

Then summing over the four classes:

Σ*fxy* = 1.*g*1 + 0.*g*2 + 0.*g*3 + 0.*g*4 = *g*1

Σ*fx* = *g*1 + *g*2 = *pA*

Σ*fy* = *g*1 + *g*3 = *pB*

The covariance between *x* and *y* values is

Σ*fxy* - Σ*fx* Σ*fy* = *g*1 - *pA pB*

which is equivalent to the LD coefficient, *D*, as defined above.

It is usually convenient to calculate the correlation rather than the covariance, normalising by the variances:

V(x) = Σ*fx2* - (Σ*fx)2* = *pA* - *pA2* = *pA* ( 1 - *pA* )

V(y) = Σ*fy2* - (Σ*fy)2* = *pB* - *pB2* = *pB* ( 1 - *pB* )

Substituting gives the correlation, which can be given the designation *rAB*, as:

$r_{AB}={\frac {D}{\sqrt {p_{A}(1-p_{A})p_{B}(1-p_{B})}}}$

or

$r_{AB}^{2}={\frac {D^{2}}{p_{A}(1-p_{A})p_{B}(1-p_{B})}}$

This LD measure was introduced by Sewall Wright and its use popularised by Hill and Robertson.

## LD for diploid frequencies

The above LD theory is based on haploid frequencies. In practice, direct observation of such frequencies is rarely possible, since in most species of interest only diploid genotypes can be observed. Assumptions need to be made to infer haploid frequencies.

A different approach to estimating LD from diploid frequencies is to calculate the covariance and correlation of frequencies, just as for haploid frequencies. Gao et al show that the diploid covariance is the same as "Burrows' composite LD measure". The table below shows *x* and *y* values for diploid genotypes. It also shows the expected frequencies on the assumption of random mating.

| Genotype | x value | y value | frequency *(f*) |
|---|---|---|---|
| *AABB* | 1 | 1 | *g*12 |
| *AABb* | 1 | 1/2 | 2*g*1*g*2 |
| *AAbb* | 1 | 0 | *g*22 |
| *AaBB* | 1/2 | 1 | 2*g*1*g*3 |
| *AaBb* | 1/2 | 1/2 | 2*g*1*g*4+2*g*2*g*3 |
| *Aabb* | 1/2 | 0 | 2*g*2*g*4 |
| *aaBB* | 0 | 1 | *g*32 |
| *aaBb* | 0 | 1/2 | 2*g*3*g*4 |
| *aabb* | 0 | 0 | *g*42 |

Covariance and correlation calculations for these frequencies are as follows:

Σ*fxy* = *g*12 + *g*1*g*2 + *g*1*g*3 + *g*1*g*4/2 + *g*2*g*3/2

Noting the alternative definition of *D* = *g*1*g*4 - *g*2*g*3, this simplifies to

Σ*fxy* = *g*1 - D/2.

Σ*fx* = *g*12 + 2*g*1*g*2 + *g*22 + *g*1*g*3 + *g*1*g*4 + *g*2*g*3 + *g*3*g*4

which simplifies, as in the haploid calculation, to

Σ*fx* = *g*1 + *g*2 = *pA*

Similary, Σ*fy* = *g*1 + *g*3 = *pB*

The covariance between *x* and *y* values is

Σ*fxy* - Σ*fx* Σ*fy* = *g*1 - *D*/2 - *pA pB*

which is simply *D*/2.

V(*x*) = Σ*fx2* - (Σ*fx)2* which can be shown to be *pA* ( 1 - *pA* )/2

V(*y*) = Σ*fy2* - (Σ*fy)2* = *pB* ( 1 - *pB* )/2

Normalising by the variances, the factor 2 cancels out. The diploid correlation which can be designated as *RAB*, has expectation:

$E(R_{AB})={\frac {D}{\sqrt {p_{A}(1-p_{A})p_{B}(1-p_{B})}}}$

Surprisingly, this is identical to the haploid LD correlation *rAB*. The result is, as mentioned above, an expectation based on the assumption of random mating. But this assumption can be relaxed.

If the deviation from random mating is expressed in terms of the inbreeding coefficient *F*, the expected frequency of *AABB* homozygotes is equal to (1-*F*)*g*12 + *Fg*1, the expected frequency of non-homozygotes such as *AABb* is equal to (1-*F*)*g*1*g*2 etc.  Using these frequencies, the covariance and variance statistics simplify to:

Cov(*x*,*y*) = (1+*F*)*D*/2

V(*x*) = (1+*F*)*pA*(1-*pA*)/2  [equivalent to (*pA*(1-*pA*) + *DA)/2*, where *DA* is the *A* locus disequilibrium]

V(y) = (1+*F*)*pB*(1-*pB*)/2

Terms in (1+*F*) cancel, so that the diploid correlation still estimates the haploid correlation:

E(*RAB*) = *rAB*

## More calculations involving D

For two biallelic loci, where *a* and *b* are the other alleles at these two loci, the restrictions are so strong that only one value of *D* is sufficient to represent all linkage disequilibrium relationships between these alleles. In this case, $D_{AB}=-D_{Ab}=-D_{aB}=D_{ab}$ . Their relationships can be characterized as follows.

$D=P_{AB}-P_{A}P_{B}$

$-D=P_{Ab}-P_{A}P_{b}$

$-D=P_{aB}-P_{a}P_{B}$

$D=P_{ab}-P_{a}P_{b}$

The sign of *D* in this case is chosen arbitrarily. The magnitude of *D* is more important than the sign of *D* because the magnitude of *D* is representative of the degree of linkage disequilibrium. However, positive *D* value means that the gamete is more frequent than expected while negative means that the combination of these two alleles are less frequent than expected.

Linkage disequilibrium in asexual populations can be defined in a similar way in terms of population allele frequencies. Furthermore, it is also possible to define linkage disequilibrium among three or more alleles, however these higher-order associations are not commonly used in practice.

## Normalization

The linkage disequilibrium D reflects both changes in the intensity of the linkage correlation and changes in gene frequency. This poses an issue when comparing linkage disequilibrium between alleles with differing frequencies. Normalization of linkage disequilibrium allows these alleles to be compared more easily.

### D' Method

Lewontin suggested calculating the normalized linkage disequilibrium (also referred to as relative linkage disequilibrium) $D'$ by dividing D by the theoretical maximum difference between the observed and expected allele frequencies as follows:

$D'={\frac {D}{D_{\max }}}$

where

$D_{\max }={\begin{cases}\min\{p_{A}p_{B},\,(1-p_{A})(1-p_{B})\}&{\text{when }}D<0\\\min\{p_{A}(1-p_{B}),\,p_{B}(1-p_{A})\}&{\text{when }}D>0\end{cases}}$

The value of $D'$ will be within the range $-1\leq D'\leq 1$ . When $D'=0$ , the loci are independent. When $-1\leq D'<0$ , the alleles are found less often than expected. When $0<D'\leq 1$ , the alleles are found more often than expected.

Note that $|D'|$ may be used in place of $D'$ when measuring how close two alleles are to linkage equilibrium.

### r2 Method

An alternative to $D'$ is the correlation coefficient between pairs of loci, usually expressed as its square, $r^{2}$ ,

$r^{2}={\frac {D^{2}}{p_{A}(1-p_{A})p_{B}(1-p_{B})}}$

The value of $r^{2}$ will be within the range $0\leq r^{2}\leq 1$ . When $r^{2}=0$ , there is no correlation between the pair. When $r^{2}=1$ , the correlation is either perfect positive or perfect negative according to the sign of r .

### d Method

Another alternative normalizes D by the product of two of the four allele frequencies when the two frequencies represent alleles from the same locus. This allows comparison of asymmetry between a pair of loci. This is often used in case-control studies where **B** is the locus containing a disease allele.

$d={\frac {D}{p_{B}(1-p_{B})}}$

### ρ Method

Similar to the d method, this alternative normalizes D by the product of two of the four allele frequencies when the two frequencies represent alleles from different loci.

$\rho ={\frac {D}{(1-p_{A})p_{B}}}$

### Limits for the ranges of linkage disequilibrium measures

The measures $r^{2}$ and $D'$ have limits to their ranges and do not range over all values of zero to one for all pairs of loci. The maximum of $r^{2}$ depends on the allele frequencies at the two loci being compared and can only range fully from zero to one where either the allele frequencies at both loci are equal, $P_{A}=P_{B}$ where $D>0$ , or when the allele frequencies have the relationship $P_{A}=1-P_{B}$ when $D<0$ . While $D'$ can always take a maximum value of 1, its minimum value for two loci is equal to $|r|$ for those loci.

## Example: Two-loci and two-alleles

Consider the haplotypes for two loci A and B with two alleles each—a two-loci, two-allele model. Then the following table defines the frequencies of each combination:

| Haplotype | Frequency |
|---|---|
| $A_{1}B_{1}$ | $x_{11}$ |
| $A_{1}B_{2}$ | $x_{12}$ |
| $A_{2}B_{1}$ | $x_{21}$ |
| $A_{2}B_{2}$ | $x_{22}$ |

Note that these are relative frequencies. One can use the above frequencies to determine the frequency of each of the alleles:

| Allele | Frequency |
|---|---|
| $A_{1}$ | $p_{1}=x_{11}+x_{12}$ |
| $A_{2}$ | $p_{2}=x_{21}+x_{22}$ |
| $B_{1}$ | $q_{1}=x_{11}+x_{21}$ |
| $B_{2}$ | $q_{2}=x_{12}+x_{22}$ |

If the two loci and the alleles are independent from each other, then we would expect the frequency of each haplotype to be equal to the product of the frequencies of its corresponding alleles (e.g. $x_{11}=p_{1}q_{1}$ ).

The deviation of the observed frequency of a haplotype from the expected is a quantity called the linkage disequilibrium and is commonly denoted by a capital *D*:

$D=x_{11}-p_{1}q_{1}$

Thus, if the loci were inherited independently, then $x_{11}=p_{1}q_{1}$ , so $D=0$ , and there is linkage equilibrium. However, if the observed frequency of haplotype $A_{1}B_{1}$ were higher than what would be expected based on the individual frequencies of $A_{1}$ and $B_{1}$ then $x_{11}>p_{1}q_{1}$ , so $D>0$ , and there is positive linkage disequilibrium. Conversely, if the observed frequency were lower, then $x_{11}<p_{1}q_{1}$ , $D<0$ , and there is negative linkage disequilibrium.

The following table illustrates the relationship between the haplotype frequencies and allele frequencies and D.

|   | $A_{1}$ | $A_{2}$ | Total |
|---|---|---|---|
| $B_{1}$ | $x_{11}=p_{1}q_{1}+D$ | $x_{21}=p_{2}q_{1}-D$ | $q_{1}$ |
| $B_{2}$ | $x_{12}=p_{1}q_{2}-D$ | $x_{22}=p_{2}q_{2}+D$ | $q_{2}$ |
| Total | $p_{1}$ | $p_{2}$ | 1 |

Additionally, we can normalize our data based on what we are trying to accomplish. For example, if we aim to create an association map in a case-control study, then we may use the d method due to its asymmetry. If we are trying to find the probability that a given haplotype will descend in a population without being recombined by other haplotypes, then it may be better to use the ρ method. But for most scenarios, $r^{2}$ tends to be the most popular method due to the usefulness of the correlation coefficient in statistics. A couple examples of where $r^{2}$ may be very useful would include measuring the recombination rate in an evolving population, or detecting disease associations.

## Role of recombination

In the absence of evolutionary forces other than random mating, Mendelian segregation, random chromosomal assortment, and chromosomal crossover (i.e. in the absence of natural selection, inbreeding, and genetic drift), the linkage disequilibrium measure D converges to zero along the time axis at a rate depending on the magnitude of the recombination rate c between the two loci.

Using the notation above, $D=x_{11}-p_{1}q_{1}$ , we can demonstrate this convergence to zero as follows. In the next generation, $x_{11}'$ , the frequency of the haplotype $A_{1}B_{1}$ , becomes

$x_{11}'=(1-c)\,x_{11}+c\,p_{1}q_{1}$

This follows because a fraction $(1-c)$ of the haplotypes in the offspring have not recombined, and are thus copies of a random haplotype in their parents. A fraction $x_{11}$ of those are $A_{1}B_{1}$ . A fraction c have recombined these two loci. If the parents result from random mating, the probability of the copy at locus A having allele $A_{1}$ is $p_{1}$ and the probability of the copy at locus B having allele $B_{1}$ is $q_{1}$ , and as these copies are initially in the two different gametes that formed the diploid genotype, these are independent events so that the probabilities can be multiplied.

This formula can be rewritten as

$x_{11}'-p_{1}q_{1}=(1-c)\,(x_{11}-p_{1}q_{1})$

so that

$D_{1}=(1-c)\;D_{0}$

where D at the n -th generation is designated as $D_{n}$ . Thus we have

$D_{n}=(1-c)^{n}\;D_{0}.$

If $n\to \infty$ , then $(1-c)^{n}\to 0$ so that $D_{n}$ converges to zero.

If at some time we observe linkage disequilibrium, it will disappear in the future due to recombination. However, the smaller the distance between the two loci, the smaller will be the rate of convergence of D to zero.

## Visualization

Once linkage disequilibrium has been calculated for a dataset, a visualization method is often chosen to display the linkage disequilibrium to make it more easily understandable.

The most common method is to use a heatmap, where colors are used to indicate the loci with positive linkage disequilibrium, and linkage equilibrium. This example displays the full heatmap, but because the heatmap is symmetrical across the diagonal (that is, the linkage disequilibrium between loci A and B is the same as between B and A), a triangular heatmap that shows the pairs only once is also commonly employed. This method has the advantage of being easy to interpret, but it also cannot display information about other variables that may be of interest.

More robust visualization options are also available, like the textile plot. In a textile plot, combinations of alleles at a certain loci can be linked with combinations of alleles at a different loci. Each genotype (combination of alleles) is represented by a circle which has an area proportional to the frequency of that genotype, with a column for each loci. Lines are drawn from each circle to the circles in the other column(s), and the thickness of the connecting line is proportional to the frequency that the two genotypes occur together. Linkage disequilibrium is seen through the number of line crossings in the diagram, where a greater number of line crossings indicates a low linkage disequilibrium and fewer crossings indicate a high linkage disequilibrium. The advantage of this method is that it shows the individual genotype frequencies and includes a visual difference between absolute (where the alleles at the two loci always appear together) and complete (where alleles at the two loci show a strong connection but with the possibility of recombination) linkage disequilibrium by the shape of the graph.

Another visualization option is forests of hierarchical latent class models (FHLCM). All loci are plotted along the top layer of the graph, and below this top layer, boxes representing latent variables are added with links to the top level. Lines connect the loci at the top level to the latent variables below, and the lower the level of the box that the loci are connected to, the greater the linkage disequilibrium and the smaller the distance between the loci. While this method does not have the same advantages of the textile plot, it does allow for the visualization of loci that are far apart without requiring the sequence to be rearranged, as is the case with the textile plot.

This is not an exhaustive list of visualization methods, and multiple methods may be used to display a data set in order to give a better picture of the data based on the information that the researcher aims to highlight.

## Resources

A comparison of different measures of LD is provided by Devlin & Risch

The International HapMap Project enables the study of LD in human populations online. The Ensembl project integrates HapMap data with other genetic information from dbSNP.

## Analysis software

- PLINK – whole genome association analysis toolset, which can calculate LD among other things
- LDHat Archived 2016-05-13 at the Wayback Machine
- Haploview
- LdCompare— open-source software for calculating LD.
- SNP and Variation Suite – commercial software with interactive LD plot.
- GOLD Archived 2014-09-21 at the Wayback Machine – Graphical Overview of Linkage Disequilibrium
- TASSEL – software to evaluate linkage disequilibrium, traits associations, and evolutionary patterns
- rAggr – finds proxy markers (SNPs and indels) that are in linkage disequilibrium with a set of queried markers, using the 1000 Genomes Project and HapMap genotype databases.
- SNeP – Fast computation of LD and Ne for large genotype datasets in PLINK format.
- LDlink – A suite of web-based applications to easily and efficiently explore linkage disequilibrium in population subgroups. All population genotype data originates from Phase 3 of the 1000 Genomes Project and variant RS numbers are indexed based on dbSNP build 151.
- Bcftools – utilities for variant calling and manipulating VCFs and BCFs.

## Simulation software

- Haploid — a C library for population genetic simulation (GPL)
