---
title: "Evolvability"
source: https://en.wikipedia.org/wiki/Adaptive_potential
domain: axolotl
license: CC-BY-SA-4.0
tags: axolotl
fetched: 2026-07-04
---

# Evolvability

(Redirected from

Adaptive potential

)

**Evolvability** is defined as the capacity of a system for adaptive evolution. Evolvability is the ability of a population of organisms to not merely generate genetic diversity, but to generate *adaptive* genetic diversity, and thereby evolve through natural selection.

In order for a biological organism to evolve by natural selection, there must be a certain minimum probability that new, heritable variants are beneficial. Random mutations, unless they occur in DNA sequences with no function, are expected to be mostly detrimental. Beneficial mutations are always rare, but if they are too rare, then adaptation cannot occur. Early failed efforts to evolve computer programs by random mutation and selection showed that evolvability is not a given, but depends on the representation of the program as a data structure, because this determines how changes in the program map to changes in its behavior. Analogously, the evolvability of organisms depends on their genotype–phenotype map. This means that genomes are structured in ways that make beneficial changes more likely. This has been taken as evidence that evolution has created fitter populations of organisms that are better able to evolve.

## Alternative definitions

Andreas Wagner describes two definitions of evolvability. According to the first definition, a biological system is evolvable:

- if its properties show heritable genetic variation, and
- if natural selection can thus change these properties.

According to the second definition, a biological system is evolvable:

- if it can acquire novel functions through genetic change, functions that help the organism survive and reproduce.

For example, consider an enzyme with multiple alleles in the population. Each allele catalyzes the same reaction, but with a different level of activity. However, even after millions of years of evolution, exploring many sequences with similar function, no mutation might exist that gives this enzyme the ability to catalyze a different reaction. Thus, although the enzyme's activity is evolvable in the first sense, that does not mean that the enzyme's function is evolvable in the second sense. However, every system evolvable in the second sense must also be evolvable in the first.

Massimo Pigliucci recognizes three classes of definition, depending on timescale. The first corresponds to Wagner's first, and represents the very short timescales that are described by quantitative genetics. He divides Wagner's second definition into two categories, one representing the intermediate timescales that can be studied using population genetics, and one representing exceedingly rare long-term innovations of form.

Pigliucci's second definition of evolvability includes Altenberg's quantitative concept of evolvability, being not a single number, but the entire upper tail of the fitness distribution of the offspring produced by the population. This quantity was considered a "local" property of the instantaneous state of a population, and its integration over the population's evolutionary trajectory, and over many possible populations, would be necessary to give a more global measure of evolvability.

## Generating more variation

More heritable phenotypic variation means more evolvability. While mutation is the ultimate source of heritable variation, its permutations and combinations also make a big difference. Sexual reproduction generates more variation (and thereby evolvability) relative to asexual reproduction (see evolution of sexual reproduction). Evolvability is further increased by generating more variation when an organism is stressed, and thus likely to be less well adapted, but less variation when an organism is doing well. The amount of variation generated can be adjusted in many different ways, for example via the mutation rate, via the probability of sexual vs. asexual reproduction, via the probability of outcrossing vs. inbreeding, via dispersal, and via access to previously cryptic variants through the switching of an evolutionary capacitor. A large population size increases the influx of novel mutations in each generation.

## Robustness and evolvability

The relationship between robustness and evolvability depends on whether recombination can be ignored. Recombination can generally be ignored in asexual populations and for traits affected by single genes.

### Without recombination

Robustness in the face of mutation does not increase evolvability in the first sense. In organisms with a high level of robustness, mutations have smaller phenotypic effects than in organisms with a low level of robustness. Thus, robustness reduces the amount of heritable genetic variation on which selection can act. However, robustness may allow exploration of large regions of genotype space, increasing evolvability according to the second sense. Even without genetic diversity, some genotypes have higher evolvability than others, and selection for robustness can increase the "neighborhood richness" of phenotypes that can be accessed from the same starting genotype by mutation. For example, one reason many proteins are less robust to mutation is that they have marginal thermodynamic stability, and most mutations reduce this stability further. Proteins that are more thermostable can tolerate a wider range of mutations and are more evolvable. For polygenic traits, neighborhood richness contributes more to evolvability than does genetic diversity or "spread" across genotype space.

### With recombination

Temporary robustness, or canalisation, may lead to the accumulation of significant quantities of cryptic genetic variation. In a new environment or genetic background, this variation may be revealed and sometimes be adaptive.

### Factors affecting evolvability via robustness

Different genetic codes have the potential to change robustness and evolvability by changing the effect of single-base mutational changes.

## Exploration ahead of time

When mutational robustness exists, many mutants will persist in a cryptic state. Mutations tend to fall into two categories, having either a very bad effect or very little effect: few mutations fall somewhere in between. Sometimes, these mutations will not be completely invisible, but still have rare effects, with very low penetrance. When this happens, natural selection weeds out the very bad mutations, while leaving the others relatively unaffected. While evolution has no "foresight" to know which environment will be encountered in the future, some mutations cause major disruption to a basic biological process, and will never be adaptive in any environment. Screening these out in advance leads to preadapted stocks of cryptic genetic variation.

Another way that phenotypes can be explored, prior to strong genetic commitment, is through learning. An organism that learns gets to "sample" several different phenotypes during its early development, and later sticks to whatever worked best. Later in evolution, the optimal phenotype can be genetically assimilated so it becomes the default behavior rather than a rare behavior. This is known as the Baldwin effect, and it can increase evolvability.

Learning biases phenotypes in a beneficial direction. But an exploratory flattening of the fitness landscape can also increase evolvability even when it has no direction, for example when the flattening is a result of random errors in molecular and/or developmental processes. This increase in evolvability can happen when evolution is faced with crossing a "valley" in an adaptive landscape. This means that two mutations exist that are deleterious by themselves, but beneficial in combination. These combinations can evolve more easily when the landscape is first flattened, and the discovered phenotype is then fixed by genetic assimilation.

## Modularity

If every mutation affected every trait, then a mutation that was an improvement for one trait would be a disadvantage for other traits. This means that almost no mutations would be beneficial overall. But if pleiotropy is restricted to within functional modules, then mutations affect only one trait at a time, and adaptation is much less constrained. In a modular gene network, for example, a gene that induces a limited set of other genes that control a specific trait under selection may evolve more readily than one that also induces other gene pathways controlling traits not under selection. Individual genes also exhibit modularity. A mutation in one cis-regulatory element of a gene's promoter region may allow the expression of the gene to be altered only in specific tissues, developmental stages, or environmental conditions rather than changing gene activity in the entire organism simultaneously.

## Evolution of evolvability

While variation yielding high evolvability could be useful in the long term, in the short term most of that variation is likely to be a disadvantage. For example, naively it would seem that increasing the mutation rate via a mutator allele would increase evolvability. But as an extreme example, if the mutation rate is too high then all individuals will be dead or at least carry a heavy mutation load. Short-term selection for low variation most of the time is likely to be more powerful than long-term selection for evolvability, making it difficult for natural selection to cause the evolution of evolvability. Other forces of selection also affect the generation of variation; for example, mutation and recombination may in part be byproducts of mechanisms to cope with DNA damage.

When recombination is low, mutator alleles may still sometimes hitchhike on the success of adaptive mutations that they cause. In this case, selection can take place at the level of the lineage. This may explain why mutators are often seen during experimental evolution of microbes. Mutator alleles can also evolve more easily when they only increase mutation rates in nearby DNA sequences, not across the whole genome: this is known as a contingency locus.

The evolution of evolvability is less controversial if it occurs via the evolution of sexual reproduction, or via the tendency of variation-generating mechanisms to become more active when an organism is stressed. The yeast prion [PSI+] may also be an example of the evolution of evolvability through evolutionary capacitance. An evolutionary capacitor is a switch that turns genetic variation on and off. This is very much like bet-hedging the risk that a future environment will be similar or different. Theoretical models also predict the evolution of evolvability via modularity. When the costs of evolvability are sufficiently short-lived, more evolvable lineages may be the most successful in the long-term. However, the hypothesis that evolvability is an adaptation is often rejected in favor of alternative hypotheses, e.g. minimization of costs.

## Applications

The study of evolvability has practical applications. For protein engineering, high evolvability is desirable, while high evolvability in pathogens and agricultural pests is harmful to human interests. Protein evolvability is defined as the ability of the protein to acquire sequence diversity and conformational flexibility which can enable it to evolve toward a new function.

In protein engineering, both rational design and directed evolution approaches aim to create changes rapidly through mutations with large effects. Such mutations, however, commonly destroy enzyme function or at least reduce tolerance to further mutations. Identifying evolvable proteins and manipulating their evolvability is becoming increasingly necessary in order to achieve ever larger functional modification of enzymes. Proteins are also often studied as part of the basic science of evolvability, because the biophysical properties and chemical functions can be easily changed by a few mutations. More evolvable proteins can tolerate a broader range of amino acid changes and allow them to evolve toward new functions. The study of evolvability has fundamental importance for understanding very long term evolution of protein superfamilies.

Many human pathogens are capable of evolution. Viruses, bacteria, fungi and cancers evolve to be resistant to host immune defences, as well as pharmaceutical drugs. These same problems occur in agriculture with pesticide and herbicide resistance. It is possible that we are facing the end of the effective life of most of available antibiotics. Predicting the evolution and evolvability of our pathogens, and devising strategies to slow or circumvent the development of resistance, demands deeper knowledge of the complex forces driving evolution at the molecular level.

A better understanding of evolvability is proposed to be part of an Extended Evolutionary Synthesis.
