---
title: "Loop extrusion"
source: https://en.wikipedia.org/wiki/Loop_extrusion
domain: hi-c-chromatin
license: CC-BY-SA-4.0
tags: chromosome conformation, topologically associating domain, genome folding, contact matrix
fetched: 2026-07-02
---

# Loop extrusion

**Loop extrusion** is a major mechanism of nuclear organization. It is a dynamic process in which structural maintenance of chromosomes (SMC) protein complexes progressively grow loops of DNA or chromatin. In this process, SMC complexes, such as condensin or cohesin, bind to DNA/chromatin, use ATP-driven motor activity to reel in DNA, and as a result, extrude the collected DNA as a loop.

## Background

The organization of DNA presents a remarkable biological challenge: human DNA can reach 2 meters and is packed into the nucleus with the diameter of 5-20 μm. At the same time, the critical cell processes involve complex processes on highly compacted DNA, such as transcription, replication, recombination, DNA repair, and cell division.

Loop extrusion is a key mechanism that organizes DNA into loops, enabling its efficient compaction and functional organization. For instance, *in vitro* experiments show that cohesin can compact DNA by 80%, while condensin achieves a remarkable 10,000-fold compaction of mitotic chromosomes, as evidenced by microscopy, Hi-C, and polymer simulations.

Another challenge lies in establishing long-range genomic communication, which can span hundreds of thousands of base pairs. Physical encounters between genomic elements are intrinsically random and promiscuous without mechanisms to facilitate them. Loop extrusion has been proposed to provide an effective solution to regulate contacts by bringing target elements into proximity while limiting contact with unwanted loci.

## Key components

The key components of the loop extrusion process are

- DNA molecule that serves as the substrate for the movement of extruder
- Extruders, usually SMC complexes, that moves along DNA in ATP-dependent manner
- Accessory factors
  - Loaders of the extruder, a factor that facilitates loading of extruder on DNA (NIPBL/MAU2 are thought to play the key role in loading extruder on DNA)
  - Unloaders of the extruder, the molecule that facilitates detachment of extruder from DNA (for example, WAPL)
  - Road-blocks located on DNA that present a hindrance to extruder movement and lead to stalling of the extrusion machinery.

### SMC proteins

Loop extrusion is performed by the SMC family of protein-complexes which includes cohesin, condensin, and SMC5/6 each playing specialized roles depending on the organism, cell cycle phase, and biological context. Cohesin mediates chromatin loop formation and stabilization, particularly during interphase in vertebrates, where it facilitates transcriptional regulation by promoting distal enhancer-promoter interactions. During mitosis and meiosis, cohesin dissociates from chromosome arms ceding its loop extrusion role to condensin. Loop extrusion by condensin mediates large-scale chromosome compaction, creating the compact, rod-like chromosome structures required for accurate segregation. Unlike cohesin and condensin, SMC5/6 is a loop extruding factor which primarily functions in maintaining genome integrity during DNA damage repair and resolving replication stress.

Despite their distinct roles, SMC complexes share a highly conserved ring-like structure. Two SMC proteins (usually, SMC1 and SMC3) are connected via a hinge region and linked at their heads by a kleisin subunit, forming a closed ring. These two SMC proteins have ATPase domains at their heads, which bind together and hydrolyze ATP. Cycles of ATP binding and hydrolysis mediate conformational changes in the ring structure, driving DNA translocation and stepwise loop extrusion. ATP is essential for both initiating loop extrusion (e.g., loading SMC complexes onto DNA) and propagating it (growing loops by translocating along DNA). The tension within the DNA significantly influences extrusion efficiency. At low tension, SMC complexes can make larger loop-capture steps, while higher tension can lead to stalling or reversal of loop extrusion.

### Modifications and factors for loading/unloading

The dynamic nature of loop extrusion is tightly controlled by accessory factors and post-translational modifications, especially in the case of cohesin. In vertebrates, NIPBL (and orthologs like Mau2 in yeast or SCC2 and SCC4) is crucial for loading SMC complexes onto DNA, initiating and maintaining active extrusion. PDS5 is thought to pause the extrusion process. The SMC can then either restart extruding or be unloaded by the additional binding of WAPL, which ensure proper recycling and turnover. Post-translational modifications also play a key role. Acetylation of cohesin by enzymes such as ESCO1 and ESCO2 stabilizes chromatin loops, particularly at CTCF-bound sites. Similarly, SUMOylation, mediated by the NSE2 subunit of the SMC5/6 complex, enhances the recruitment of SMC5/6 to sites of DNA damage, supporting its role in genomic stability.

### Roadblocks of loop extrusion

Loop extruders can encounter various obstacles while extruding. For example, many of which were shown to directly interact with cohesin and hypothesized to stop its movement on DNA. However, *in vivo* experiments demonstrate that cohesin can frequently bypass obstacles larger than its ring size.

1. **Other cohesin and condensin molecules:** Extruding cohesins and condensins has been found to be obstacle to other extruders that they encounter on the way. As such, they present a fundamental road-block that can be randomly encountered on the DNA.
2. **CTCF:** The C-terminal DNA-binding domain of CTCF has been shown to directly interact with SA2 and SCC1 subunits of cohesin to stop extrusion and retain it on DNA with recent evidence suggesting a tension-dependence to the interaction. CTCF stalls cohesin in a highly directional manner where cohesin can bypass CTCF in one orientation but stalls when encountering it in the opposite orientation. This directionality allows for the creation of isolated domains on the genome called Topologically Associating Domains (TADs) which have been proposed to have a large role in gene-regulation.
3. **RNA polymerase/transcription**: Transcribing polymerases can serve as barriers to cohesin that may not only stall extruders but also act as a motor pushing cohesin in the direction of polymerase movement. The size of a polymerase with an RNA transcript is usually larger than the size of the cohesin ring, and the stall force of cohesin is much smaller than that of polymerase, allowing for effective barrier function by polymerase. Furthermore, it has been found that RNA can directly interact with cohesin subunits.
4. **DNA replication:** Replication forks and replisomes have been shown to restrict loop extrusion activity. Additionally, the MCM helicase, which is associated with origins of replication, has been found to counteract the extrusion of cohesin on DNA.
5. **R-loops**: Some evidence suggests that R-loops can also act as barriers to loop extrusion, and R-loops have been shown to interact with cohesin subunits. However, other evidence suggests that R-loops may instead act as cohesin loaders.

## Molecular mechanism

The molecular mechanisms of DNA-loop extrusion by SMC proteins have not yet been fully understood, but recent structural studies have made significant progress in developing several working models, like the scrunching model, the Brownian-ratchet model, the DNA-segment capture model/DNA-pumping model, the hold-and-feed model and the swing-and-clamp model.

## Evidence for loop extrusion

### Evidence for loop extruding molecules and their properties

#### Direct visualization *in vitro*

The first direct evidence of loop extrusion came from in vitro imaging studies on fluorescently labeled DNA with condensin or cohesin. Extrusion was found to be ATP-dependent and happened at ~1-3kb/s. The stall force was measured to be around 0.1-1pN which is small compared to other molecular motors.

#### *In vivo* evidence

Loop extrusion by the SMC complex cohesin was suggested on the basis of chromatin contact maps from Hi-C experiments. These maps displayed genomic domains of self-contact of a few hundred kb in size, referred to as topologically associating domains (TADs). These domains are generally bordered by binding sites for the CTCF protein, which are oriented in a convergent manner such that CTCF proteins "point" toward each other. This observation suggested that this aspect of chromatin organization must be executed by a 1-dimensional, linear scanning mechanism, rather than a 3-dimensional mechanism involving random encounters, which would exhibit CTCF orientations (convergent, divergent, and two parallel orientations) in equal probabilities. Subsequent quantitative simulation models proposing loop extrusion by cohesin were able to reproduce patterns of chromatin contacts observed in Hi-C.

More recent evidence comes from imaging of chromatin dynamics in the presence and absence of cohesin. Experiments with fluorescently tagged genomic loci analyzed by mathematical inference techniques indicate that these loci into come into spatial proximity more frequently in the presence of cohesin. Associated simulation modeling again indicates that chromatin loop extrusion can explain these observations.

### Evidence for the biological role of loop extrusion

Most work on the biological role of loop extrusion relies on inhibiting loop extruders and observing the consequences. Depletion of cohesin leads to the disappearance of TADs and some loss in transcription genome-wide. In more specific settings, inhibition of cohesin has been found to inhibit neuronal maturation and differentiation and function of dendritic cells. Depletion of either condensin I or condensin II at the entry into mitosis leads to abnormal chromosome formation and improper segregation of sister chromatids.

## Biological function

Loop extrusion has been found across the tree of life with suggested roles in immune response, DNA repair, enhancer-promoter interactions, and mitosis.

- **Mitosis in eukaryotes:** In mitosis, loop extrusion by condensin is critical for the segregation of sister chromatids and for providing structural rigidity after separation. Condensin I has been found to modulate the size and arrangement of nested inner loops and condensin II organizing the backbone from which loops emanate.
- **Cell division in bacteria:** In bacteria, SMC proteins have been found to maintain the juxtaposition of the chromosome arms by loading at the centromere and extruding until the terminus.
- **Enhancer–promoter communication:** During interphase, cohesin-mediated loop extrusion has been proposed to facilitate communication between distal enhancers and promoters that regulate gene transcription. As cohesin extrudes loops of chromatin, it can transiently bring regulatory elements separated by tens to hundreds of kilobases into proximity, enabling enhancer-bound transcription factors to interact with promoter-associated transcriptional machinery. CTCF binding sites can modulate this process by blocking or stabilizing extrusion, thereby constraining which enhancers can contact which promoters. Through this mechanism CTCF and cohesin have been shown to enable complex developmental and regulatory programs:
  - **V(D)J recombination:** Loop extrusion by cohesin has been found to play a key role in V(D)J recombination to generate diversity in antibodies and T-cell receptors as depletion of cohesin inhibits V(D)J recombination. There are CTCF motifs throughout the recombination region, and inversions of their orientation or mutation of the motifs lead to changes in recombination probabilities consistent with those predicted by loop extrusion.
  - **Protocadherin promoter choice:** Protocadherins are mammalian proteins involved in cell adhesion of the neurons encoded in DNA in multiple similar genes located in the protocadherin locus. Neurons usually express only a subset of the protocadherins, enabling variability in the interactions between neurons. The choice of protocadherins rely on cohesin, which bridges alternative promoters of protocadherin with the enhancer in a CTCF-dependent manner. This process involves intricate regulation by CTCF and WAPL.
- **Topologically associating domains (TADs):** During interphase, chromosomes are locally compacted at the sub-megabase scale into so-called TADs. Generally, they are bordered by motifs for CTCF and completely disappear if either cohesin or CTCF is degraded. CTCF sites at TAD boundaries act as barriers to loop extrusion, preventing cohesin from extruding loops across domain borders. As a result, enhancers and promoters located in different TADs are less likely to be brought together by cohesin-mediated looping, making TADs function as regulatory neighborhoods that constrain enhancer–promoter communication within the same domain.

## Theoretical models of loop extrusion

In mathematical models of loop extrusion, the two legs of a loop-extruding factor (LEF) are represented as points on a one-dimensional line, evolving according to different extrusion policies:

- **LEF Translocation:** These dictate how LEFs move along the chromatin. These include symmetric extrusion—where both legs move in opposite directions—and one-sided extrusion—where one leg remains stalled while the other moves. Cohesin is often modeled with symmetric extrusion, while condensin is thought to follow a one-sided extrusion mechanism.
- **Stochastic Binding and Unbinding**: LEFs bind to chromatin at a random time and position along the chain, and unbind after a characteristic time.
- **LEF-LEF interactions**: When LEFs encounter one another, different interaction policies can be implemented. LEFs may halt upon collision, or bypass each other, as observed in some contexts.
- **Extrusion Barriers**: Bound proteins such as CTCF or RNA polymerase II can act as obstacles, stalling or halting LEF motion.

Since the exact modalities of LEF dynamics remain uncertain, these models provide a flexible framework to explore different hypothetical behaviors of LEFs.

In these models, the statistics of LEFs are characterized by two key physical parameters:

- **Processivity** ( ${\textstyle \lambda =2v\tau }$ ): Average size of a loop extruded by an unobstructed LEF before dissociating. This characteristic loop size depends on the extrusion speed v and the residence time $\tau$ of the LEF on the chromatin.
- **Separation** ( $d=L/N$ )**:** Average distance between LEFs on the chromatin fiber. It is determined by the total number of LEFs N and the length of the chromatin L . A shorter separation results in denser packing of loops, while larger separation leaves gaps between loops.

The interplay of these two parameters, encapsulated by the dimensionless parameter $\lambda /d$ , defines two states of chromatin organization:

- **Sparse State** ( $\lambda /d\ll 1$ ): LEFs operate independently, forming isolated loops with large gaps between them. This state results in minimal compaction of the chromatin fiber.
- **Dense State** ( $\lambda /d\gg 1$ ): LEFs are abundant enough to form a continuous, gapless array of loops. This leads to significant chromatin compaction, as seen during mitosis.
