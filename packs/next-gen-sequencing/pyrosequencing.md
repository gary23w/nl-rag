---
title: "Pyrosequencing"
source: https://en.wikipedia.org/wiki/Pyrosequencing
domain: next-gen-sequencing
license: CC-BY-SA-4.0
tags: next generation sequencing, massively parallel sequencing, sequencing by synthesis, nanopore sequencing
fetched: 2026-07-02
---

# Pyrosequencing

**Pyrosequencing** is a non-electrophoretic DNA sequencing (determining the order of nucleotides in DNA) method based on the "sequencing by synthesis" principle, in which the sequencing is performed by detecting the nucleotide incorporated by a DNA polymerase. Pyrosequencing relies on light detection based on a chain reaction when pyrophosphate is released, hence, the name given it.

## Principles

The principle of pyrosequencing was first described in 1993 by P. Nyrén, B. Pettersson, and M. Uhlen. The technique combines solid phase sequencing, and use of streptavidin-coated magnetic beads, a recombinant DNA polymerase lacking 3´-to-5´exonuclease activity (proof-reading), and luminescence detection of inorganic pyrophosphate using the firefly luciferase enzyme.

Specifically, a solution of three enzymes—DNA polymerase, ATP sulfurylase, and firefly luciferase—and a deoxyribonucleoside triphosphate (dNTP) are added to single stranded DNA to be sequenced, and the incorporation of nucleotide is followed, measuring the light emitted as a consequence of inorganic pyrophosphate production. The intensity of the light determines if 0, 1, or more nucleotides have been incorporated, thus showing how many complementary nucleotides are present on the template strand. The nucleotide mixture is removed before a next nucleotide mixture is added, and the process is repeated for each of the four nucleotides, until the DNA sequence of the single stranded template is determined.

A second solution-based method for pyrosequencing was described in 1998 by Mostafa Ronaghi, [Mathias Uhlen], and Pål Nyren.In this alternative method, an additional enzyme, apyrase, is introduced to remove nucleotides that are not incorporated by the DNA polymerase. This enables the enzyme mixture— DNA polymerase, luciferase, and apyrase—to be added when sequencing is initiated, and kept in the reaction solution throughout the procedure (thus enabling easier automation). An automated instrument based on this principle was introduced to the market the following year by the company Pyrosequencing.

A third variant, a microfluidic pyrosequencing method, was described in 2005 by an industrial research team led by Jonathan Rothberg, at the company 454 Life Sciences. This alternative approach for pyrosequencing was based on the original principle of attaching the DNA to be sequenced to a solid support; Rothberg and co-workers demonstrated that sequencing could be performed in a highly parallel manner using a microfabrication and microarrays. This allowed high-throughput DNA sequencing, and an automated instrument was introduced to the market. This first next generation sequencing instrument initiated a new era in genomics research, and to rapidly falling prices for DNA sequencing, allowing affordable whole genome sequencing.

## Procedure

"Sequencing by synthesis" involves taking a single strand of the DNA to be sequenced and then synthesizing its complementary strand enzymatically. The pyrosequencing method is based on detecting the activity of DNA polymerase (a DNA synthesizing enzyme) with another chemoluminescent enzyme. Essentially, the method allows sequencing a single strand of DNA by synthesizing the complementary strand along it, one base pair at a time, and detecting which base was actually added at each step. The template DNA is immobile, and solutions of A, C, G, and T nucleotides are sequentially added and removed from the reaction. Light is produced only when the nucleotide solution complements the first unpaired base of the template. The sequence of solutions which produce chemiluminescent signals allows the determination of the sequence of the template.

For the solution-based version of pyrosequencing, the single-strand DNA (ssDNA) template is hybridized to a sequencing primer and incubated with the enzymes DNA polymerase, ATP sulfurylase, luciferase and apyrase, and with the substrates adenosine 5´ phosphosulfate (APS) and luciferin.

1. The addition of one of the four deoxynucleotide triphosphates initiates the second step; dNTPs)—dATPαS, which is not a substrate for a luciferase, is added instead of dATP to avoid noise. DNA polymerase incorporates the correct, complementary dNTPs onto the template. This incorporation releases pyrophosphate (PPi).

1. ATP sulfurylase converts PPi to ATP in the presence of adenosine 5´ phosphosulfate. This ATP acts as a substrate for the luciferase-mediated conversion of luciferin to oxyluciferin that generates visible light in amounts that are proportional to the amount. The light produced in the luciferase-catalyzed reaction is detected by a camera and analyzed in a program.

1. Unincorporated nucleotides and ATP are degraded by the apyrase, and the reaction can restart with another nucleotide.

The process can be represented by the following equations:

- PPi + APS → ATP + Sulfate (catalyzed by ATP-sulfurylase);
- ATP + luciferin + O2 → AMP + PPi + oxyluciferin + CO2 + hv (catalyzed by luciferase);

where PPi is pyrophosphate, APS is adenosine 5-phosphosulfate, ATP is adenosine triphosphate, O2 is dioxygen, AMP is adenosine monophosphate, CO2 is carbon dioxide, and hv is light.

## Limitations

Currently, a limitation of the method is that the lengths of individual reads of DNA sequence are in the neighborhood of 300-500 nucleotides, shorter than the 800-1000 obtainable with chain termination methods (e.g. Sanger sequencing). This can make the process of genome assembly more difficult, particularly for sequences containing a large amount of repetitive DNA. Also, lack of a proof-reading activity limits accuracy of this method.

## Commercialization

Pyrosequencing AB, a company based in Uppsala, Sweden, was founded with venture capital provided by HealthCap in order to commercialize machinery and reagents for sequencing short stretches of DNA using the pyrosequencing technique. Pyrosequencing AB was listed on the Stockholm Stock Exchange in 1999. When Pyrosequencing AB acquired Biotage LLC, a U.S.-based company, and other companies, in 2003, the company was renamed Biotage AB. The pyrosequencing and other biomedical units of Biotage AB were sold to Qiagen in 2008. The pyrosequencing technology was licensed to 454 Life Sciences. 454 developed an array-based pyrosequencing technology that emerged as a platform for large-scale DNA sequencing, including genome sequencing and metagenomics.

Roche acquired 454 Life Sciences, and announced the discontinuation of the 454 sequencing platform in 2013. The 454 sequencing platform was replaced, in part, by Illumina dye sequencing, and by Applied Biosystems sequencing products.
