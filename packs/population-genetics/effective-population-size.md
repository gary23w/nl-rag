---
title: "Effective population size"
source: https://en.wikipedia.org/wiki/Effective_population_size
domain: population-genetics
license: CC-BY-SA-4.0
tags: population genetics, hardy-weinberg principle, coalescent theory, linkage disequilibrium
fetched: 2026-07-02
---

# Effective population size

The **effective population size** (*N**e*) is the size of an idealised population that would experience the same rate of genetic drift as the real population. Idealised populations are those where each locus evolves independently, following the assumptions of the neutral theory of molecular evolution. The effective population size is normally smaller than the census population size *N*. This can be due to chance events prevent some individuals from breeding, to occasional population bottlenecks, to background selection, and to genetic hitchhiking.

The same real population could have a different effective population size for different properties of interest, such as genetic drift (or more precisely, the speed of coalescence) over one generation vs. over many generations. Within a species, areas of the genome that have more genes and/or less genetic recombination tend to have lower effective population sizes, because of the effects of selection at linked sites. In a population with selection at many loci and abundant linkage disequilibrium, the coalescent effective population size may not reflect the census population size at all, or may reflect its logarithm.

The concept of effective population size was introduced in the field of population genetics in 1931 by the American geneticist Sewall Wright. Some versions of the effective population size are used in wildlife conservation.

## Empirical measurements

In a rare experiment that directly measured genetic drift one generation at a time, in *Drosophila* populations of census size 16, the effective population size was 11.5. This measurement was achieved through studying changes in the frequency of a neutral allele from one generation to another in over 100 replicate populations.

More commonly, effective population size is estimated indirectly by comparing data on current within-species genetic diversity to theoretical expectations. According to the neutral theory of molecular evolution, an idealised diploid population will have a pairwise nucleotide diversity equal to 4 $\mu$ *N**e*, where $\mu$ is the mutation rate. The effective population size can therefore be estimated empirically by dividing the nucleotide diversity by 4 $\mu$ . This captures the cumulative effects of genetic drift, genetic hitchhiking, and background selection over longer timescales. More advanced methods, permitting a changing effective population size over time, have also been developed.

The effective size measured to reflect these longer timescales may have little relationship to the number of individuals physically present in a population. Measured effective population sizes vary between genes in the same population, being low in genome areas of low recombination and high in genome areas of high recombination. Sojourn times are proportional to N in neutral theory, but for alleles under selection, sojourn times are proportional to log(N). Genetic hitchhiking can cause neutral mutations to have sojourn times proportional to log(N): this may explain the relationship between measured effective population size and the local recombination rate.

If the recombination map of recombination frequencies along chromosomes is known, *N**e* can be inferred from *r*P2 = 1 / (1+4*N**e* *r*), where *r*P is the Pearson correlation coefficient between loci. This expression can be interpreted as the probability that two lineages coalesce before one allele on either lineage recombines onto some third lineage.

The population size might not be constant over time, and thus neither might the effective population size (defined as coalescence speed). With a constant population size, we expect larger pairwise Hamming distance between sequences to be rarer. Under population expansion, an intermediate Hamming distance is instead most common; this is seen for humans. A skyline plot more directly describes coalescence speed over time. The pairwise sequential Markovian coalescent and multiple sequential Markovian coalescent take the average of skyline plots over many loci. An alternative approach infers effective population size over time, together with migration among populations, using the allele frequency spectrum, describing how often alleles are rare versus common. Yet another approach exploits runs of homozygosity to incorporate information from recombination events.

A survey of publications on 102 mostly wildlife animal and plant species yielded 192 *N**e*/*N* ratios. Seven different estimation methods were used in the surveyed studies. Accordingly, the ratios ranged widely from 10*-6* for Pacific oysters to 0.994 for humans, with an average of 0.34 across the examined species. Based on these data they subsequently estimated more comprehensive ratios, accounting for fluctuations in population size, variance in family size and unequal sex-ratio. These ratios average to only 0.10-0.11.

A genealogical analysis of Inuit hunter-gatherers determined the effective-to-census population size ratio for haploid (mitochondrial DNA, Y chromosomal DNA), and diploid (autosomal DNA) loci separately: the ratio of the effective to the census population size was estimated as 0.6–0.7 for autosomal and X-chromosomal DNA, 0.7–0.9 for mitochondrial DNA and 0.5 for Y-chromosomal DNA.

## Selection effective size

In an idealised Wright-Fisher model, the fate of an allele, beginning at an intermediate frequency, is largely determined by selection if the selection coefficient s ≫ 1/N, and largely determined by neutral genetic drift if s ≪ 1/N. In real populations, the cutoff value of s may depend instead on local recombination rates. This limit to selection in a real population may be captured in a toy Wright-Fisher simulation through the appropriate choice of Ne.

The ability of a species to differentiate between nearly neutral alleles can be measured by how codon bias differs from neutral expectations. The Ka/Ks ratio is also sometimes used as a proxy.

The drift-barrier hypothesis claims that populations with different selection effective population sizes are predicted to evolve profoundly different genome architectures.

## History of theory

Ronald Fisher and Sewall Wright originally defined effective population size as "the number of breeding individuals in an idealised population that would show the same amount of dispersion of allele frequencies under random genetic drift or the same amount of inbreeding as the population under consideration". This implied two potentially different effective population sizes, based either on the one-generation increase in variance across replicate populations **(variance effective population size)**, or on the one-generation change in the inbreeding coefficient **(inbreeding effective population size)**. These two are closely linked, and derived from F-statistics, but they are not identical.

Today, the effective population size is usually estimated empirically with respect to the amount of within-species genetic diversity divided by the mutation rate, yielding a **coalescent effective population size** that reflects the cumulative effects of genetic drift, background selection, and genetic hitchhiking over longer time periods. Another important effective population size is the **selection effective population size** 1/scritical, where scritical is the critical value of the selection coefficient at which selection becomes more important than genetic drift.

### Variance effective size

In the Wright-Fisher idealized population model, the conditional variance of the allele frequency $p'$ , given the allele frequency p in the previous generation, is

$\operatorname {var} (p'\mid p)={p(1-p) \over 2N}.$

Let ${\widehat {\operatorname {var} }}(p'\mid p)$ denote the same, typically larger, variance in the actual population under consideration. The variance effective population size $N_{e}^{(v)}$ is defined as the size of an idealized population with the same variance. This is found by substituting ${\widehat {\operatorname {var} }}(p'\mid p)$ for $\operatorname {var} (p'\mid p)$ and solving for N which gives

$N_{e}^{(v)}={p(1-p) \over 2{\widehat {\operatorname {var} }}(p)}.$

In the following examples, one or more of the assumptions of a strictly idealised population are relaxed, while other assumptions are retained. The variance effective population size of the more relaxed population model is then calculated with respect to the strict model.

#### Variations in population size

Population size varies over time. Suppose there are *t* non-overlapping generations, then effective population size is given by the harmonic mean of the population sizes:

${1 \over N_{e}}={1 \over t}\sum _{i=1}^{t}{1 \over N_{i}}$

For example, say the population size was *N* = 10, 100, 50, 80, 20, 500 for six generations (*t* = 6). Then the effective population size is the harmonic mean of these, giving:

| ${1 \over N_{e}}$ | $={{\begin{matrix}{\frac {1}{10}}\end{matrix}}+{\begin{matrix}{\frac {1}{100}}\end{matrix}}+{\begin{matrix}{\frac {1}{50}}\end{matrix}}+{\begin{matrix}{\frac {1}{80}}\end{matrix}}+{\begin{matrix}{\frac {1}{20}}\end{matrix}}+{\begin{matrix}{\frac {1}{500}}\end{matrix}} \over 6}$ |
|---|---|
|   | $={0.1945 \over 6}$ |
|   | $=0.032416667$ |
| $N_{e}$ | $=30.8$ |

Note this is less than the arithmetic mean of the population size, which in this example is 126.7. The harmonic mean tends to be dominated by the smallest bottleneck that the population goes through.

#### Dioeciousness

If a population is dioecious, i.e. there is no self-fertilisation then

$N_{e}=N+{\begin{matrix}{\frac {1}{2}}\end{matrix}}$

or more generally,

$N_{e}=N+{\begin{matrix}{\frac {D}{2}}\end{matrix}}$

where *D* represents dioeciousness and may take the value 0 (for not dioecious) or 1 for dioecious.

When *N* is large, *N**e* approximately equals *N*, so this is usually trivial and often ignored:

$N_{e}=N+{\begin{matrix}{\frac {1}{2}}\approx N\end{matrix}}$

#### Variance in reproductive success

If population size is to remain constant, each individual must contribute on average two gametes to the next generation. An idealized population assumes that this follows a Poisson distribution so that the variance of the number of gametes contributed, *k* is equal to the mean number contributed, i.e. 2:

$\operatorname {var} (k)={\bar {k}}=2.$

However, in natural populations the variance is often larger than this. The vast majority of individuals may have no offspring, and the next generation stems only from a small number of individuals, so

$\operatorname {var} (k)>2.$

The effective population size is then smaller, and given by:

$N_{e}^{(v)}={4N-2D \over 2+\operatorname {var} (k)}$

Note that if the variance of *k* is less than 2, *N**e* is greater than *N*. In the extreme case of a population experiencing no variation in family size, in a laboratory population in which the number of offspring is artificially controlled, *V**k* = 0 and *N**e* = 2*N*.

#### Non-Fisherian sex-ratios

When the sex ratio of a population varies from the Fisherian 1:1 ratio, effective population size is given by:

$N_{e}^{(v)}=N_{e}^{(F)}={4N_{m}N_{f} \over N_{m}+N_{f}}$

Where *N**m* is the number of males and *N**f* the number of females. For example, with 80 males and 20 females (an absolute population size of 100):

| $N_{e}$ | $={4\times 80\times 20 \over 80+20}$ |
|---|---|
|   | $={6400 \over 100}$ |
|   | $=64$ |

Again, this results in *N**e* being less than *N*.

### Inbreeding effective size

Alternatively, the effective population size may be defined by noting how the average inbreeding coefficient changes from one generation to the next, and then defining *N**e* as the size of the idealized population that has the same change in average inbreeding coefficient as the population under consideration. The presentation follows Kempthorne (1957).

For the idealized population, the inbreeding coefficients follow the recurrence equation

$F_{t}={\frac {1}{N}}\left({\frac {1+F_{t-2}}{2}}\right)+\left(1-{\frac {1}{N}}\right)F_{t-1}.$

Using Panmictic Index (1 − *F*) instead of inbreeding coefficient, we get the approximate recurrence equation

$1-F_{t}=P_{t}=P_{0}\left(1-{\frac {1}{2N}}\right)^{t}.$

The difference per generation is

${\frac {P_{t+1}}{P_{t}}}=1-{\frac {1}{2N}}.$

The inbreeding effective size can be found by solving

${\frac {P_{t+1}}{P_{t}}}=1-{\frac {1}{2N_{e}^{(F)}}}.$

This is

$N_{e}^{(F)}={\frac {1}{2\left(1-{\frac {P_{t+1}}{P_{t}}}\right)}}$

.

#### Theory of overlapping generations and age-structured populations

When organisms live longer than one breeding season, effective population sizes have to take into account the life tables for the species.

##### Haploid

Assume a haploid population with discrete age structure. An example might be an organism that can survive several discrete breeding seasons. Further, define the following age structure characteristics:

$v_{i}=$

Fisher's reproductive value

for age

i

,

$\ell _{i}=$

The chance an individual will survive to age

i

, and

$N_{0}=$

The number of newborn individuals per breeding season.

The generation time is calculated as

$T=\sum _{i=0}^{\infty }\ell _{i}v_{i}=$

average age of a reproducing individual

Then, the inbreeding effective population size is

$N_{e}^{(F)}={\frac {N_{0}T}{1+\sum _{i}\ell _{i+1}^{2}v_{i+1}^{2}({\frac {1}{\ell _{i+1}}}-{\frac {1}{\ell _{i}}})}}.$

##### Diploid

Similarly, the inbreeding effective number can be calculated for a diploid population with discrete age structure. This was first given by Johnson, but the notation more closely resembles Emigh and Pollak.

Assume the same basic parameters for the life table as given for the haploid case, but distinguishing between male and female, such as *N*0*ƒ* and *N*0*m* for the number of newborn females and males, respectively (notice lower case *ƒ* for females, compared to upper case *F* for inbreeding).

The inbreeding effective number is

${\begin{aligned}{\frac {1}{N_{e}^{(F)}}}={\frac {1}{4T}}\left\{{\frac {1}{N_{0}^{f}}}+{\frac {1}{N_{0}^{m}}}+\sum _{i}\left(\ell _{i+1}^{f}\right)^{2}\left(v_{i+1}^{f}\right)^{2}\left({\frac {1}{\ell _{i+1}^{f}}}-{\frac {1}{\ell _{i}^{f}}}\right)\right.\,\,\,\,\,\,\,\,&\\\left.{}+\sum _{i}\left(\ell _{i+1}^{m}\right)^{2}\left(v_{i+1}^{m}\right)^{2}\left({\frac {1}{\ell _{i+1}^{m}}}-{\frac {1}{\ell _{i}^{m}}}\right)\right\}.&\end{aligned}}$
