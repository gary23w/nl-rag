---
title: "Synthetic biological circuit"
source: https://en.wikipedia.org/wiki/Synthetic_biological_circuit
domain: genetic-circuits
license: CC-BY-SA-4.0
tags: synthetic gene network, toggle switch, logic gate biology, oscillator
fetched: 2026-07-02
---

# Synthetic biological circuit

**Synthetic biological circuits** are an application of synthetic biology where biological parts inside a cell are designed to perform logical functions mimicking those observed in electronic circuits. Typically, these circuits are categorized as either **genetic circuits**, **RNA circuits**, or **protein circuits**, depending on the types of biomolecule that interact to create the circuit's behavior. The applications of all three types of circuit range from simply inducing production to adding a measurable element, like green fluorescent protein, to an existing natural biological circuit, to implementing completely new systems of many parts.

The goal of synthetic biology is to generate an array of tunable and characterized parts, or modules, with which any desirable synthetic biological circuit can be easily designed and implemented. These circuits can serve as a method to modify cellular functions, create cellular responses to environmental conditions, or influence cellular development. By implementing rational, controllable logic elements in cellular systems, researchers can use living systems as engineered "biological machines" to perform a vast range of useful functions.

## History

The first natural gene circuit studied in detail was the lac operon. In studies of diauxic growth of *E. coli* on two-sugar media, Jacques Monod and Francois Jacob discovered that *E.coli* preferentially consumes the more easily processed glucose before switching to lactose metabolism. They discovered that the mechanism that controlled the metabolic "switching" function was a two-part control mechanism on the lac operon. When lactose is present in the cell the enzyme β-galactosidase is produced to convert lactose into glucose or galactose. When lactose is absent in the cell the lac repressor inhibits the production of the enzyme β-galactosidase to prevent any inefficient processes within the cell.

The lac operon is used in the biotechnology industry for production of recombinant proteins for therapeutic use. The gene or genes for producing an exogenous protein are placed on a plasmid under the control of the lac promoter. Initially the cells are grown in a medium that does not contain lactose or other sugars, so the new genes are not expressed. Once the cells reach a certain point in their growth, isopropyl β-D-1-thiogalactopyranoside (IPTG) is added. IPTG, a molecule similar to lactose, but with a sulfur bond that is not hydrolyzable so that E. coli does not digest it, is used to activate or "induce" the production of the new protein. Once the cells are induced, it is difficult to remove IPTG from the cells and therefore it is difficult to stop expression.

Two early examples of synthetic biological circuits were published in Nature in 2000. One, by Tim Gardner, Charles Cantor, and Jim Collins working at Boston University, demonstrated a "bistable" switch in *E. coli*. The switch is turned on by heating the culture of bacteria and turned off by addition of IPTG. They used green fluorescent protein as a reporter for their system. The second, by Michael Elowitz and Stanislas Leibler, showed that three repressor genes could be connected to form a negative feedback loop termed the Repressilator that produces self-sustaining oscillations of protein levels in *E. coli.*

Currently, synthetic circuits are a burgeoning area of research in systems biology with more publications detailing synthetic biological circuits published every year. There has been significant interest in encouraging education and outreach as well: the International Genetically Engineered Machines Competition manages the creation and standardization of BioBrick parts as a means to allow undergraduate and high school students to design their own synthetic biological circuits.

## Interest and goals

Both immediate and long term applications exist for the use of synthetic biological circuits, including different applications for metabolic engineering, and synthetic biology. Those demonstrated successfully include pharmaceutical production, and fuel production. However, methods involving direct genetic introduction are not inherently effective without invoking the basic principles of synthetic cellular circuits. For example, each of these successful systems employs a method to introduce all-or-none induction or expression. This is a biological circuit where a simple repressor or promoter is introduced to facilitate creation of the product, or inhibition of a competing pathway. However, with the limited understanding of cellular networks and natural circuitry, implementation of more robust schemes with more precise control and feedback is hindered. Therein lies the immediate interest in synthetic cellular circuits.

Development in understanding cellular circuitry can lead to exciting new modifications, such as cells which can respond to environmental stimuli. For example, cells could be developed that signal toxic surroundings and react by activating pathways used to degrade the perceived toxin. To develop such a cell, it is necessary to create a complex synthetic cellular circuit which can respond appropriately to a given stimulus.

Given synthetic cellular circuits represent a form of control for cellular activities, it can be reasoned that with complete understanding of cellular pathways, "plug and play" cells with well defined genetic circuitry can be engineered. It is widely believed that if a proper toolbox of parts is generated, synthetic cells can be developed implementing only the pathways necessary for cell survival and reproduction. From this cell, to be thought of as a minimal genome cell, one can add pieces from the toolbox to create a well defined pathway with appropriate synthetic circuitry for an effective feedback system. Because of the basic ground up construction method, and the proposed database of mapped circuitry pieces, techniques mirroring those used to model computer or electronic circuits can be used to redesign cells and model cells for easy troubleshooting and predictive behavior and yields.

## Example circuits

### Oscillators

1. Repressilator
2. Mammalian tunable synthetic oscillator
3. Bacterial tunable synthetic oscillator
4. Coupled bacterial oscillator
5. Globally coupled bacterial oscillator

Elowitz et al. and Fung et al. created oscillatory circuits that use multiple self-regulating mechanisms to create a time-dependent oscillation of gene product expression.

### Bistable switches

1. Toggle-switch

Gardner et al. used mutual repression between two control units to create an implementation of a toggle switch capable of controlling cells in a bistable manner: transient stimuli resulting in persistent responses.

Gene regulation is an essential part of developmental processes. During development, genes are turned on and off in different tissues, changes in regulatory mechanisms may result in genetic switching in a bistable system, the gene switches serve as regulatory molecule binding sites. These are proteins that activate transcription when they land on a gene switch and thereby express the gene that was expected to operate as a memory device, allowing cell fate decisions to be chosen and maintained.

Toggle switch which operates using two mutually inhibitory genes, each promoter is inhibited by the repressor that is transcribed by the opposing promoter. Toggle switch design: Inducer 1 inactivates repressor 1, which means repressor 2 is produced. Repressor 2, in turn, stops transcription of the repressor 1 gene and the reporter gene.

### Logical operators

### Analog tuners

Using negative feedback and identical promoters, linearizer gene circuits can impose uniform gene expression that depends linearly on extracellular chemical inducer concentration.

### Controllers of gene expression heterogeneity

Synthetic gene circuits can control gene expression heterogeneity can be controlled independently of the gene expression mean.

### Other engineered systems

Engineered systems are the result of implementation of combinations of different control mechanisms. A limited counting mechanism was implemented by a pulse-controlled gene cascade and application of logic elements enables genetic "programming" of cells as in the research of Tabor et al., which synthesized a photosensitive bacterial edge detection program.

## Circuit design

Recent developments in artificial gene synthesis and the corresponding increase in competition within the industry have led to a significant drop in price and wait time of gene synthesis and helped improve methods used in circuit design. At the moment, circuit design is improving at a slow pace because of insufficient organization of known multiple gene interactions and mathematical models. This issue is being addressed by applying computer-aided design (CAD) software to provide multimedia representations of circuits through images, text and programming language applied to biological circuits. Some of the more well known CAD programs include GenoCAD, Clotho framework and j5. GenoCAD uses grammars, which are either opensource or user generated "rules" which include the available genes and known gene interactions for cloning organisms. Clotho framework uses the Biobrick standard rules.
