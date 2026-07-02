---
title: "Hardy–Weinberg principle"
source: https://en.wikipedia.org/wiki/Hardy%E2%80%93Weinberg_principle
domain: population-genetics
license: CC-BY-SA-4.0
tags: population genetics, hardy-weinberg principle, coalescent theory, linkage disequilibrium
fetched: 2026-07-02
---

# Hardy–Weinberg principle

In population genetics, the **Hardy–Weinberg principle**, also known as the **Hardy–Weinberg equilibrium**, **model**, **theorem**, or **law**, states that allele and genotype frequencies in a population will remain constant from generation to generation in the absence of other evolutionary influences. These influences include *genetic drift*, *mate choice*, *assortative mating*, *natural selection*, *sexual selection*, *mutation*, *gene flow*, *meiotic drive*, *genetic hitchhiking*, *population bottleneck*, *founder effect,* *inbreeding and outbreeding depression*.

## Derivation

In the simplest case of a single locus with two alleles denoted *A* and *a* with frequencies *f*(A) = *p* and *f*(a) = *q*, respectively, the expected genotype frequencies under random mating are *f*(AA) = *p*2 for the AA homozygotes, *f*(aa) = *q*2 for the aa homozygotes, and *f*(Aa) = 2*pq* for the heterozygotes. In the absence of selection, mutation, genetic drift, or other forces, allele frequencies *p* and *q* are constant between generations, so equilibrium is reached.

The principle is named after G. H. Hardy and Wilhelm Weinberg, who first demonstrated it mathematically. Hardy's paper was focused on debunking the view that a dominant allele would automatically tend to increase in frequency (a view possibly based on a misinterpreted question at a lecture). Today, tests for Hardy–Weinberg genotype frequencies are used primarily to test for population stratification and other forms of non-random mating.

Consider a population of monoecious diploids, where each organism produces male and female gametes at equal frequency, and has two alleles at each gene locus. We assume that the population is so large that it can be treated as infinite. Organisms reproduce by random union of gametes (the "gene pool" population model). A locus in this population has two alleles, A and a, that occur with initial frequencies *f*0(A) = *p* and *f*0(a) = *q*, respectively. The allele frequencies at each generation are obtained by pooling together the alleles from each genotype of the same generation according to the expected contribution from the homozygote and heterozygote genotypes, which are 1 and 1/2, respectively:

| $f_{t}({\text{A}})=f_{t}({\text{AA}})+{\tfrac {1}{2}}f_{t}({\text{Aa}})$ |   | 1 |
|---|---|---|

| $f_{t}({\text{a}})=f_{t}({\text{aa}})+{\tfrac {1}{2}}f_{t}({\text{Aa}})$ |   | 2 |
|---|---|---|

The different ways to form genotypes for the next generation can be shown in a Punnett square, where the proportion of each genotype is equal to the product of the row and column allele frequencies from the current generation.

|   | Females |   |   |
|---|---|---|---|
| A (*p*) | a (*q*) |   |   |
| Males | A (*p*) | AA (*p*2) | Aa (*pq*) |
| a (*q*) | Aa (*qp*) | aa (*q*2) |   |

The sum of the entries is *p*2 + 2*pq* + *q*2 = 1, as the genotype frequencies must sum to one.

Note again that as *p* + *q* = 1, the binomial expansion of (*p* + *q*)2 = *p*2 + 2*pq* + *q*2 = 1 gives the same relationships.

Summing the elements of the Punnett square or the binomial expansion, we obtain the expected genotype proportions among the offspring after a single generation:

| $f_{1}({\text{AA}})=p^{2}=f_{0}({\text{A}})^{2}$ |   | 3 |
|---|---|---|

| $f_{1}({\text{Aa}})=pq+qp=2pq=2f_{0}({\text{A}})f_{0}({\text{a}})$ |   | 4 |
|---|---|---|

| $f_{1}({\text{aa}})=q^{2}=f_{0}({\text{a}})^{2}$ |   | 5 |
|---|---|---|

These frequencies define the Hardy–Weinberg equilibrium. It should be mentioned that the genotype frequencies after the first generation need not equal the genotype frequencies from the initial generation, e.g. *f*1(AA) ≠ *f*0(AA). However, the genotype frequencies for all *future* times will equal the Hardy–Weinberg frequencies, e.g. *ft*(AA) = *f*1(AA) for *t* > 1. This follows since the genotype frequencies of the next generation depend only on the allele frequencies of the current generation which, as calculated by equations (**1**) and (**2**), are preserved from the initial generation:

${\begin{aligned}f_{1}({\text{A}})&=f_{1}({\text{AA}})+{\tfrac {1}{2}}f_{1}({\text{Aa}})=p^{2}+pq=p(p+q)=p=f_{0}({\text{A}})\\f_{1}({\text{a}})&=f_{1}({\text{aa}})+{\tfrac {1}{2}}f_{1}({\text{Aa}})=q^{2}+pq=q(p+q)=q=f_{0}({\text{a}})\end{aligned}}$

For the more general case of dioecious diploids [organisms are either male or female] that reproduce by random mating of individuals, it is necessary to calculate the genotype frequencies from the nine possible matings between each parental genotype (*AA*, *Aa*, and *aa*) in either sex, weighted by the expected genotype contributions of each such mating. Equivalently, one considers the six unique diploid–diploid combinations:

$\left[({\text{AA}},{\text{AA}}),({\text{AA}},{\text{Aa}}),({\text{AA}},{\text{aa}}),({\text{Aa}},{\text{Aa}}),({\text{Aa}},{\text{aa}}),({\text{aa}},{\text{aa}})\right]$

and constructs a Punnett square for each, so as to calculate its contribution to the next generation's genotypes. These contributions are weighted according to the probability of each diploid–diploid combination, which follows a multinomial distribution with *k* = 3. For example, the probability of the mating combination (AA,aa) is 2 *f**t*(AA)*f**t*(aa) and it can only result in the Aa genotype: [0,1,0]. Overall, the resulting genotype frequencies are calculated as:

${\begin{aligned}&\left[f_{t+1}({\text{AA}}),f_{t+1}({\text{Aa}}),f_{t+1}({\text{aa}})\right]=\\&\qquad =f_{t}({\text{AA}})f_{t}({\text{AA}})\left[1,0,0\right]+2f_{t}({\text{AA}})f_{t}({\text{Aa}})\left[{\tfrac {1}{2}},{\tfrac {1}{2}},0\right]+2f_{t}({\text{AA}})f_{t}({\text{aa}})\left[0,1,0\right]\\&\qquad \qquad +f_{t}({\text{Aa}})f_{t}({\text{Aa}})\left[{\tfrac {1}{4}},{\tfrac {1}{2}},{\tfrac {1}{4}}\right]+2f_{t}({\text{Aa}})f_{t}({\text{aa}})\left[0,{\tfrac {1}{2}},{\tfrac {1}{2}}\right]+f_{t}({\text{aa}})f_{t}({\text{aa}})\left[0,0,1\right]\\&\qquad =\left[\left(f_{t}({\text{AA}})+{\tfrac {1}{2}}f_{t}({\text{Aa}})\right)^{2},2\left(f_{t}({\text{AA}})+{\tfrac {1}{2}}f_{t}({\text{Aa}})\right)\left(f_{t}({\text{aa}})+{\tfrac {1}{2}}f_{t}({\text{Aa}})\right),\left(f_{t}({\text{aa}})+{\tfrac {1}{2}}f_{t}({\text{Aa}})\right)^{2}\right]\\&\qquad =\left[f_{t}({\text{A}})^{2},2f_{t}({\text{A}})f_{t}({\text{a}}),f_{t}({\text{a}})^{2}\right]\end{aligned}}$

As before, one can show that the allele frequencies at time *t* + 1 equal those at time *t*, and so, are constant in time. Similarly, the genotype frequencies depend only on the allele frequencies, and so, after time *t* = 1 are also constant in time.

If in either monoecious or dioecious organisms, either the allele or genotype proportions are initially unequal in either sex, it can be shown that constant proportions are obtained after one generation of random mating. If dioecious organisms are heterogametic and the gene locus is located on the X chromosome, it can be shown that if the allele frequencies are initially unequal in the two sexes [*e.g*., XX females and XY males, as in humans], *f*′(a) in the heterogametic sex 'chases' *f*(a) in the homogametic sex of the previous generation, until an equilibrium is reached at the weighted average of the two initial frequencies.

## Deviations from Hardy–Weinberg equilibrium

The seven assumptions underlying Hardy–Weinberg equilibrium are as follows:

- organisms are diploid
- only sexual reproduction occurs
- generations are nonoverlapping
- mating is random
- population size is infinitely large
- allele frequencies are equal in the sexes
- there is no migration, gene flow, admixture, mutation or selection

Violations of the Hardy–Weinberg assumptions can cause deviations from expectation. How this affects the population depends on the assumptions that are violated.

- Random mating. The HWP states the population will have the given genotypic frequencies (called Hardy–Weinberg proportions) after a single generation of random mating within the population. When the random mating assumption is violated, the population will not have Hardy–Weinberg proportions. A common cause of non-random mating is inbreeding, which causes an increase in homozygosity for all genes.

If a population violates one of the following four assumptions, the population may continue to have Hardy–Weinberg proportions each generation, but the allele frequencies will change over time.

- Selection, in general, causes allele frequencies to change, often quite rapidly. While directional selection eventually leads to the loss of all alleles except the favored one (unless one allele is dominant, in which case recessive alleles can survive at low frequencies), some forms of selection, such as balancing selection, lead to equilibrium without loss of alleles.
- Mutation will have a very subtle effect on allele frequencies through the introduction of new allele into a population. Mutation rates are of the order 10−4 to 10−8, and the change in allele frequency will be, at most, the same order. Recurrent mutation will maintain alleles in the population, even if there is strong selection against them.
- Migration genetically links two or more populations together. In general, allele frequencies will become more homogeneous among the populations. Some models for migration inherently include nonrandom mating (Wahlund effect, for example). For those models, the Hardy–Weinberg proportions will normally not be valid.
- Small population size can cause a random change in allele frequencies. This is due to a sampling effect, and is called genetic drift. Sampling effects are most important when the allele is present in a small number of copies.

In real world genotype data, deviations from Hardy–Weinberg Equilibrium may be a sign of genotyping error.

## Sex linkage

Where the A gene is sex linked, the heterogametic sex (*e.g.*, mammalian males; avian females) have only one copy of the gene (and are termed hemizygous), while the homogametic sex (*e.g.*, human females) have two copies. The genotype frequencies at equilibrium are *p* and *q* for the heterogametic sex but *p*2, 2*pq* and *q*2 for the homogametic sex.

For example, in humans red–green colorblindness is an X-linked recessive trait. In western European males, the trait affects about 1 in 12, (*q* = 0.083) whereas it affects about 1 in 200 females (0.005, compared to *q*2 = 0.007), very close to Hardy–Weinberg proportions.

If a population is brought together with males and females with a different allele frequency in each subpopulation (males or females), the allele frequency of the male population in the next generation will follow that of the female population because each son receives its X chromosome from its mother. The population converges on equilibrium very quickly.

## Generalizations

The simple derivation above can be generalized for more than two alleles and polyploidy.

### Generalization for more than two alleles

Consider an extra allele frequency, *r*. The two-allele case is the binomial expansion of (*p* + *q*)2, and thus the three-allele case is the trinomial expansion of (*p* + *q* + *r*)2.

$(p+q+r)^{2}=p^{2}+q^{2}+r^{2}+2pq+2pr+2qr\,$

More generally, consider the alleles A1, ..., A*n* given by the allele frequencies *p*1 to *p**n*;

$(p_{1}+\cdots +p_{n})^{2}\,$

giving for all homozygotes:

$f(A_{i}A_{i})=p_{i}^{2}\,$

and for all heterozygotes:

$f(A_{i}A_{j})=2p_{i}p_{j}\,$

### Generalization for polyploidy

The Hardy–Weinberg principle may also be generalized to polyploid systems, that is, for organisms that have more than two copies of each chromosome. Consider again only two alleles. The diploid case is the binomial expansion of:

$(p+q)^{2}\,$

and therefore the polyploid case is the binomial expansion of:

$(p+q)^{c}\,$

where *c* is the ploidy, for example with tetraploid (*c* = 4):

| Genotype | Frequency |
|---|---|
| AAAA | $p^{4}$ |
| AAAa | $4p^{3}q$ |
| AAaa | $6p^{2}q^{2}$ |
| Aaaa | $4pq^{3}$ |
| aaaa | $q^{4}$ |

Whether the organism is a 'true' tetraploid or an amphidiploid will determine how long it will take for the population to reach Hardy–Weinberg equilibrium.

### Complete generalization

For n distinct alleles in c -ploids, the genotype frequencies in the Hardy–Weinberg equilibrium are given by individual terms in the multinomial expansion of $(p_{1}+\cdots +p_{n})^{c}$ :

$(p_{1}+\cdots +p_{n})^{c}=\sum _{k_{1},\ldots ,k_{n}\ \in \mathbb {N} :k_{1}+\cdots +k_{n}=c}{c \choose k_{1},\ldots ,k_{n}}p_{1}^{k_{1}}\cdots p_{n}^{k_{n}}$

## Significance tests for deviation

Testing deviation from the HWP is generally performed using Pearson's chi-squared test, using the observed genotype frequencies obtained from the data and the expected genotype frequencies obtained using the HWP. For systems where there are large numbers of alleles, this may result in data with many empty possible genotypes and low genotype counts, because there are often not enough individuals present in the sample to adequately represent all genotype classes. If this is the case, then the asymptotic assumption of the chi-squared distribution, will no longer hold, and it may be necessary to use a form of Fisher's exact test, which requires a computer to solve. More recently a number of MCMC methods of testing for deviations from HWP have been proposed (Guo & Thompson, 1992; Wigginton *et al.* 2005)

### Example chi-squared test for deviation

This data is from E. B. Ford (1971) on the scarlet tiger moth, for which the phenotypes of a sample of the population were recorded. Genotype–phenotype distinction is assumed to be negligibly small. The null hypothesis is that the population is in Hardy–Weinberg proportions, and the alternative hypothesis is that the population is not in Hardy–Weinberg proportions.

| Phenotype | White-spotted (AA) | Intermediate (Aa) | Little spotting (aa) | Total |
|---|---|---|---|---|
| Number | 1469 | 138 | 5 | 1612 |

From this, allele frequencies can be calculated:

${\begin{aligned}p&={2\times \mathrm {obs} ({\text{AA}})+\mathrm {obs} ({\text{Aa}}) \over 2\times (\mathrm {obs} ({\text{AA}})+\mathrm {obs} ({\text{Aa}})+\mathrm {obs} ({\text{aa}}))}\\\\&={2\times 1469+138 \over 2\times (1469+138+5)}\\\\&={3076 \over 3224}\\\\&=0.954\end{aligned}}$

and

${\begin{aligned}q&=1-p\\&=1-0.954\\&=0.046\end{aligned}}$

So the Hardy–Weinberg expectation is:

${\begin{aligned}\mathrm {Exp} ({\text{AA}})&=p^{2}n=0.954^{2}\times 1612=1467.4\\\mathrm {Exp} ({\text{Aa}})&=2pqn=2\times 0.954\times 0.046\times 1612=141.2\\\mathrm {Exp} ({\text{aa}})&=q^{2}n=0.046^{2}\times 1612=3.4\end{aligned}}$

Pearson's chi-squared test states:

${\begin{aligned}\chi ^{2}&=\sum {(O-E)^{2} \over E}\\&={(1469-1467.4)^{2} \over 1467.4}+{(138-141.2)^{2} \over 141.2}+{(5-3.4)^{2} \over 3.4}\\&=0.001+0.073+0.756\\&=0.83\end{aligned}}$

There is 1 degree of freedom (degrees of freedom for test for Hardy–Weinberg proportions are # genotypes − # alleles). The 5% significance level for 1 degree of freedom is 3.84, and since the χ2 value is less than this, the null hypothesis that the population is in Hardy–Weinberg frequencies is **not** rejected.

### Fisher's exact test (probability test)

Fisher's exact test can be applied to testing for Hardy–Weinberg proportions. Since the test is conditional on the allele frequencies, *p* and *q*, the problem can be viewed as testing for the proper number of heterozygotes. In this way, the hypothesis of Hardy–Weinberg proportions is rejected if the number of heterozygotes is too large or too small. The conditional probabilities for the heterozygote, given the allele frequencies are given in Emigh (1980) as

$\operatorname {prob} [n_{12}\mid n_{1}]={\frac {\binom {n}{n_{11},n_{12},n_{22}}}{\binom {2n}{n_{1},n_{2}}}}2^{n_{12}},$

where *n*11, *n*12, *n*22 are the observed numbers of the three genotypes, AA, Aa, and aa, respectively, and *n*1 is the number of A alleles, where $n_{1}=2n_{11}+n_{12}$ .

**An example** Using one of the examples from Emigh (1980), we can consider the case where *n* = 100, and *p* = 0.34. The possible observed heterozygotes and their exact significance level is given in Table 4.

| Number of heterozygotes | Significance level |
|---|---|
| 0 | 0.000 |
| 2 | 0.000 |
| 4 | 0.000 |
| 6 | 0.000 |
| 8 | 0.000 |
| 10 | 0.000 |
| 12 | 0.000 |
| 14 | 0.000 |
| 16 | 0.000 |
| 18 | 0.001 |
| 20 | 0.007 |
| 22 | 0.034 |
| 23 | 0.067 |
| 24 | 0.151 |
| 25 | 0.291 |
| 26 | 0.474 |
| 27 | 0.730 |
| 28 | 1.000 |

Using this table, one must look up the significance level of the test based on the observed number of heterozygotes. For example, if one observed 20 heterozygotes, the significance level for the test is 0.007. As is typical for Fisher's exact test for small samples, the gradation of significance levels is quite coarse.

However, a table like this has to be created for every experiment, since the tables are dependent on both *n* and *p*.

## Equivalence tests

The equivalence tests are developed in order to establish sufficiently good agreement of the observed genotype frequencies and Hardy Weinberg equilibrium. Let ${\mathcal {M}}$ denote the family of the genotype distributions under the assumption of Hardy Weinberg equilibrium. The distance between a genotype distribution p and Hardy Weinberg equilibrium is defined by $d(p,{\mathcal {M}})=\min _{q\in {\mathcal {M}}}d(p,q)$ , where d is some distance. The equivalence test problem is given by $H_{0}=\{d(p,{\mathcal {M}})\geq \varepsilon \}$ and $H_{1}=\{d(p,{\mathcal {M}})<\varepsilon \}$ , where $\varepsilon >0$ is a tolerance parameter. If the hypothesis $H_{0}$ can be rejected then the population is close to Hardy Weinberg equilibrium with a high probability. The equivalence tests for the biallelic case are developed among others in Wellek (2004). The equivalence tests for the case of multiple alleles are proposed in Ostrovski (2020).

## Inbreeding coefficient

The inbreeding coefficient, F (see also *F*-statistics), is one minus the observed frequency of heterozygotes over that expected from Hardy–Weinberg equilibrium.

$F={\frac {\operatorname {E} {(f({\text{Aa}}))}-\operatorname {O} (f({\text{Aa}}))}{\operatorname {E} (f({\text{Aa}}))}}=1-{\frac {\operatorname {O} (f({\text{Aa}}))}{\operatorname {E} (f({\text{Aa}}))}},$

where the expected value from Hardy–Weinberg equilibrium is given by

$\operatorname {E} (f({\text{Aa}}))=2pq$

For example, for Ford's data above:

$F=1-{138 \over 141.2}=0.023.$

For two alleles, the chi-squared goodness of fit test for Hardy–Weinberg proportions is equivalent to the test for inbreeding,  $F=0$ .

The inbreeding coefficient is unstable as the expected value approaches zero, and thus not useful for rare and very common alleles. For: $F{\big |}_{E=0,O=0}=-\infty$ ; $F{\big |}_{E=0,O>0}$ is undefined.

## History

Mendelian genetics were rediscovered in 1900. However, it remained somewhat controversial for several years as it was not then known how it could cause continuous characteristics. Udny Yule (1902) argued against Mendelism because he thought that dominant alleles would increase in the population. The American William E. Castle (1903) showed that without selection, the genotype frequencies would remain stable. Karl Pearson (1903) found one equilibrium position with values of *p* = *q* = 0.5. Reginald Punnett, unable to counter Yule's point, introduced the problem to G. H. Hardy, a British mathematician, with whom he played cricket. Hardy was a pure mathematician and held applied mathematics in some contempt; his view of biologists' use of mathematics comes across in his 1908 paper where he describes this as "very simple":

To the Editor of Science: I am reluctant to intrude in a discussion concerning matters of which I have no expert knowledge, and I should have expected the very simple point which I wish to make to have been familiar to biologists. However, some remarks of Mr. Udny Yule, to which Mr. R. C. Punnett has called my attention, suggest that it may still be worth making...

Suppose that Aa is a pair of Mendelian characters, A being dominant, and that in any given generation the number of pure dominants (AA), heterozygotes (Aa), and pure recessives (aa) are as

p

:2

q

:

r

.

Finally, suppose that the numbers are fairly large, so that mating may be regarded as random, that the sexes are evenly distributed among the three varieties, and that all are equally fertile. A little mathematics of the multiplication-table type is enough to show that in the next generation the numbers will be as

(

p

+

q

)

2

:2(

p

+

q

)(

q

+

r

):(

q

+

r

)

2

, or as

p

1

:2

q

1

:

r

1

,

say.

The interesting question is: in what circumstances will this distribution be the same as that in the generation before? It is easy to see that the condition for this is

q

2

=

pr

. And since

q

1

2

=

p

1

r

1

,

whatever the values of

p

,

q

,

and

r

may be, the distribution will in any case continue unchanged after the second generation.

The principle was thus known as *Hardy's law* in the English-speaking world until 1943, when Curt Stern pointed out that it had first been formulated independently in 1908 by the German physician Wilhelm Weinberg. William Castle in 1903 also derived the ratios for the special case of equal allele frequencies, and it is sometimes (but rarely) called the Hardy–Weinberg–Castle Law.

### Derivation of Hardy's equations

Hardy's statement begins with a recurrence relation for the frequencies *p*, 2*q*, and *r*. These recurrence relations follow from fundamental concepts in probability, specifically independence, and conditional probability. For example, consider the probability of an offspring from the generation $\textstyle t$ being homozygous dominant. Alleles are inherited independently from each parent. A dominant allele can be inherited from a homozygous dominant parent with probability 1, or from a heterozygous parent with probability 0.5. To represent this reasoning in an equation, let $\textstyle A_{t}$ represent inheritance of a dominant allele from a parent. Furthermore, let $\textstyle AA_{t-1}$ and $\textstyle Aa_{t-1}$ represent potential parental genotypes in the preceding generation.

${\begin{aligned}p_{t}&=P(A_{t},A_{t})=P(A_{t})^{2}\\&=\left(P(A_{t}\mid AA_{t-1})P(AA_{t-1})+P(A_{t}\mid Aa_{t-1})P(Aa_{t-1})\right)^{2}\\&=\left((1)p_{t-1}+(0.5)2q_{t-1}\right)^{2}\\&=\left(p_{t-1}+q_{t-1}\right)^{2}\end{aligned}}$

The same reasoning, applied to the other genotypes yields the two remaining recurrence relations. Equilibrium occurs when each proportion is constant between subsequent generations. More formally, a population is at equilibrium at generation $\textstyle t$ when

$\textstyle 0=p_{t}-p_{t-1}$

,

$\textstyle 0=q_{t}-q_{t-1}$

, and

$\textstyle 0=r_{t}-r_{t-1}$

By solving these equations necessary and sufficient conditions for equilibrium to occur can be determined. Again, consider the frequency of homozygous dominant animals. Equilibrium implies

${\begin{aligned}0&=p_{t}-p_{t-1}\\&=p_{t-1}^{2}+2p_{t-1}q_{t-1}+q_{t-1}^{2}-p_{t-1}\end{aligned}}$

First consider the case, where $\textstyle p_{t-1}=0$ , and note that it implies that $\textstyle q_{t-1}=0$ and $\textstyle r_{t-1}=1$ . Now consider the remaining case, where $\textstyle p_{t-1}\neq \textstyle 0$ :

${\begin{aligned}0&=p_{t-1}(p_{t-1}+2q_{t-1}+q_{t-1}^{2}/p_{t-1}-1)\\&=q_{t-1}^{2}/p_{t-1}-r_{t-1}\end{aligned}}$

where the final equality holds because the allele proportions must sum to one. In both cases, $\textstyle q_{t-1}^{2}=p_{t-1}r_{t-1}$ . It can be shown that the other two equilibrium conditions imply the same equation. Together, the solutions of the three equilibrium equations imply sufficiency of Hardy's condition for equilibrium. Since the condition always holds for the second generation, all succeeding generations have the same proportions.

### Numerical example

#### Estimation of genotype distribution

An example computation of the genotype distribution given by Hardy's original equations is instructive. The phenotype distribution from Table 3 above will be used to compute Hardy's initial genotype distribution. Note that the *p* and *q* values used by Hardy are not the same as those used above.

${\begin{aligned}{\text{sum}}&={\mathrm {obs} ({\text{AA}})+2\times \mathrm {obs} ({\text{Aa}})+\mathrm {obs} ({\text{aa}})}={1469+2\times 138+5}\\[5pt]&=1750\end{aligned}}$

${\begin{aligned}p&={1469 \over 1750}=0.83943\\[5pt]2q&={2\times 138 \over 1750}=0.15771\\[5pt]r&={5 \over 1750}=0.00286\end{aligned}}$

As checks on the distribution, compute

$p+2q+r=0.83943+0.15771+0.00286=1.00000\,$

and

$E_{0}=q^{2}-pr=0.00382.\,$

For the next generation, Hardy's equations give

${\begin{aligned}q&={0.15771 \over 2}=0.07886\\\\p_{1}&=(p+q)^{2}=0.84325\\[5pt]2q_{1}&=2(p+q)(q+r)=0.15007\\[5pt]r_{1}&=(q+r)^{2}=0.00668.\end{aligned}}$

Again as checks on the distribution, compute

$p_{1}+2q_{1}+r_{1}=0.84325+0.15007+0.00668=1.00000\,$

and

$E_{1}=q_{1}^{2}-p_{1}r_{1}=0.00000\,$

which are the expected values. The reader may demonstrate that subsequent use of the second-generation values for a third generation will yield identical results.

#### Estimation of carrier frequency

The Hardy–Weinberg principle can also be used to estimate the frequency of carriers of an autosomal recessive condition in a population based on the frequency of suffers.

Let us assume an estimated $\textstyle {\frac {1}{2500}}$ babies are born with cystic fibrosis, this is about the frequency of homozygous individuals observed in Northern European populations. We can use the Hardy–Weinberg equations to estimate the carrier frequency, the frequency of heterozygous individuals, $\textstyle 2pq$ .

${\begin{aligned}&q^{2}={\frac {1}{2500}}\\[5pt]&q={\frac {1}{50}}\\[5pt]&p=1-q\end{aligned}}$

As $\textstyle {\frac {1}{50}}$ is small we can take *p*, $\textstyle 1-{\frac {1}{50}}$ , to be 1.

${\begin{aligned}2pq=2\cdot {\frac {1}{50}}\\[5pt]2pq={\frac {1}{25}}\end{aligned}}$

We therefore estimate the carrier rate to be $\textstyle {\frac {1}{25}}$ , which is about the frequency observed in Northern European populations.

This can be simplified to the carrier frequency being about twice the square root of the birth frequency.

## Graphical representation

It is possible to represent the distribution of genotype frequencies for a bi-allelic locus within a population graphically using a de Finetti diagram. This uses a triangular plot (also known as trilinear, triaxial or ternary plot) to represent the distribution of the three genotype frequencies in relation to each other. It differs from many other such plots in that the direction of one of the axes has been reversed. The curved line in the diagram is the Hardy–Weinberg parabola and represents the state where alleles are in Hardy–Weinberg equilibrium. It is possible to represent the effects of natural selection and its effect on allele frequency on such graphs. The de Finetti diagram was developed and used extensively by A. W. F. Edwards in his book *Foundations of Mathematical Genetics*.
