---
title: "Repressilator"
source: https://en.wikipedia.org/wiki/Repressilator
domain: genetic-circuits
license: CC-BY-SA-4.0
tags: synthetic gene network, toggle switch, logic gate biology, oscillator
fetched: 2026-07-02
---

# Repressilator

The **repressilator** is a genetic regulatory network consisting of at least one feedback loop with at least three genes, each expressing a protein that represses the next gene in the loop. In biological research, repressilators have been used to build cellular models and understand cell function. There are both artificial and naturally occurring repressilators. Recently, the naturally occurring repressilator clock gene circuit in *Arabidopsis thaliana* (*A. thaliana*) and mammalian systems have been studied.

## Artificial Repressilators

Artificial repressilators were first engineered by Michael Elowitz and Stanislas Leibler in 2000, complementing other research projects studying simple systems of cell components and function. In order to understand and model the design and cellular mechanisms that confers a cell's function, Elowitz and Leibler created an artificial network consisting of a loop with three transcriptional repressors. This network was designed from scratch to exhibit a stable oscillation that acts like an electrical oscillator system with fixed time periods. The network was implemented in *Escherichia coli* (*E. coli)* via recombinant DNA transfer. It was then verified that the engineered colonies did indeed exhibit the desired oscillatory behavior.

The repressilator consists of three genes connected in a feedback loop, such that each gene represses the next gene in the loop and is repressed by the previous gene. In the synthetic insertion into *E. coli*, green fluorescent protein (GFP) was used as a reporter so that the behavior of the network could be observed using fluorescence microscopy.

The design of the repressilator was guided by biological and circuit principles with discrete and stochastic models of analysis. Six differential equations were used to model the kinetics of the repressilator system based on protein and mRNA concentrations, as well as appropriate parameter and Hill coefficient values. In the study, Elowitz and Leibler generated figures showing oscillations of repressor proteins, using integration and typical parameter values as well as a stochastic version of the repressilator model using similar parameters. These models were analyzed to determine the values of various rates that would yield a sustained oscillation. It was found that these oscillations were favored by promoters coupled to efficient ribosome binding sites, cooperative transcriptional repressors, and comparable protein and mRNA decay rates.

This analysis motivated two design features which were engineered into the genes. First, promoter regions were replaced with a more efficient hybrid promoter which combined the *E. coli* phage lambda PL (λ PL) promoter with *lac repressor* (*Lacl*) and *Tet repressor* (*TetR*) operator sequences. Second, to reduce the disparity between the lifetimes of the repressor proteins and the mRNAs, a carboxy terminal tag based on the ssrA-RNA sequence was added at the 3' end of each repressor gene. This tag is recognized by proteases which target the protein for degradation. The design was implemented using a low-copy plasmid encoding the repressilator and a higher-copy reporter, which were used to transform a culture of *E. coli*.

## Naturally Occurring Repressilators

### Plants

Circadian circuits in plants feature a transcriptional regulatory feedback loop called the repressilator. In the core oscillator loop (outlined in gray) in *A. thaliana*, light is first sensed by two cryptochromes and five phytochromes. Two transcription factors, Circadian Clock Associated 1 (CCA1) and Late Elongated Hypocotyl (LHY), repress genes associated with evening expression like *Timing of CAB expression 1* (*TOC1*) and activate genes associated with morning expression by binding to their promoters. *TOC1*, an evening gene, positively regulates *CCA1* and *LHY* via an unknown mechanism. Evening-phased transcription factor CCA1 Hiking Expedition (CHE) and histone demethylase jumonji C domain-containing 5 (JMJD5) directly repress *CCA1*. Other components have been found to be expressed throughout the day and either directly or indirectly inhibit or activate a consequent element in the circadian circuit, thereby creating a complex, robust and flexible network of feedback loops.

#### Morning-Phase Expression

The morning-phase expression loop refers to the genes and proteins that regulate rhythms during the day in *A. thaliana*. The two main genes are LHY and CCA1, which encode LHY and CCA1 transcription factors. These proteins form heterodimers that enter the nucleus and bind to the *TOC1* gene promoter, repressing the production of TOC1 protein. When TOC1 protein is expressed, it serves to regulate *LHY* and *CCA1* by inhibition of their transcription. This was later supported in 2012 by Dr. Alexandra Pokhilo, who used computational analyses to show that TOC1 served this role as an inhibitor of *LHY* and *CCA1* expression. The morning loop serves to inhibit hypocotyl elongation, in contrast with the evening-phase loop which promotes hypocotyl elongation. The morning phase loop has shown to be incapable of supporting circadian oscillation when evening-phase expression genes have been mutated, suggesting the interdependency of each component in this naturally occurring repressilator.

#### Evening-Phase Expression

*Early Flowering 3* (*ELF3*), *Early Flowering 4* (*ELF4*) and *Phytoclock1* (*LUX*) are the key elements in evening-phased clock gene expression in *A. thaliana.* They form the evening complex, in which *LUX* binds to the promoters of *Phytochrome Interacting Factor 4* (*PIF4*) and *Phytochrome Interacting Factor 5* (*PIF5*) and inhibits them. As a result, hypocotyl elongation is repressed in the early-evening. When the inhibition is alleviated late at night, the hypocotyl elongates. Photoperiod flowering is controlled by output gene *Gigantea* (*GI*). *GI* is activated at night and activates the expression of *Constans* (*CO*), which activates the expression of *Flowering Locus T* (*FT*). *FT* then causes flowering in long-days.

### Mammals

Mammals evolved an endogenous timing mechanism to coordinate both physiology and behavior to the 24 hour period. In 2016, researchers identified a sequence of three subsequent inhibitions within this mechanism that they identified as a repressilator, which is now believed to serve as a major core element of this circadian network. The necessity of this system was established through a series of gene knockouts amongst *cryptochrome* (*Cry*), *period* (*Per*), and *Rev-erb* *--* core mammalian clock genes whose knockouts lead to arrhythmicity. The model that these researchers generated includes *Bmal1* as a driver of E-box mediated transcription, *Per2* and *Cry1* as early and late E-box repressors, respectively, as well as the D-box regulator Dbp and the nuclear receptor Rev-erb-α. The sequential inhibitions by *Rev-erb*, *Per* and *Cry1* can generate sustained oscillations, and by clamping all other components except for this repressilator oscillations persisted with similar amplitudes and periods. All oscillating networks seem to involve any combination of these three core genes, as demonstrated in various schematics released by researchers.

## Recent Work

The repressilator model has been used to model and study other biological pathways and systems. Since, extensive work into the repressilator's modeling capacities has been performed. In 2003, the repressilator's representation and validation of biological models, being a model with many variables, was performed using the Simpathica system, which verified that the model does indeed oscillate with all of its complexities.

As stated in Elowitz and Leibler's original work, the ultimate goal for repressilator research is to build an artificial circadian clock that mirrors its natural, endogenous counterpart. This would involve developing an artificial clock with reduced noise and temperature compensation in order to better understand circadian rhythms that can be found in every domain of life. Disruption of circadian rhythms may lead to loss of rhythmicity in metabolic and transcriptional processes, and even quicken the onset of certain neurodegenerative diseases such as Alzheimer's disease. In 2017, oscillators that generated circadian rhythms and were not influenced much by temperature were created in a laboratory.

Pathologically, the repressilator model can be used to model cell growth and abnormalities that may arise, such as those present in cancer cells. In doing so, new treatments may be developed based on circadian activity of cancerous cells. Additionally, in 2016, a research team improved upon the previous design of the repressilator. Following noise (signal processing) analysis, the authors moved the GFP reporter construct onto the repressilator plasmid and removed the ssrA degradation tags from each repressor protein. This extended the period and improved the regularity of the oscillations of the repressilator.

## Significance

### Synthetic Biology

Artificial repressilators were discovered by implanting a synthetic inhibition loop into *E. coli*.  This represented the first implementation of synthetic oscillations into an organism. Further implications of this include the possibility of rescuing mutated components of oscillations synthetically in model organisms.

The artificial repressilator is a milestone of synthetic biology which shows that genetic regulatory networks can be designed and implemented to perform novel functions. However, it was found that the cells' oscillations drifted out of phase after a period of time and the artificial repressilator's activity was influenced by cell growth. The initial experiment therefore gave new appreciation to the circadian clock found in many organisms, as endogenous repressilators are significantly more robust than implanted artificial repressilators. New investigations at the RIKEN Quantitative Biology Center have found that chemical modifications to a single protein molecule could form a temperature independent, self-sustainable oscillator .

Artificial repressilators could potentially aid research and treatments in fields ranging from circadian biology to endocrinology. They are increasingly able to demonstrate the synchronization inherent to natural biological systems and the factors that affect them.

### Circadian Biology

A better understanding of the naturally occurring repressilator in model organisms with endogenous, circadian timings, like *A. thaliana,* has applications in agriculture, especially in regards to plant rearing and livestock management.
