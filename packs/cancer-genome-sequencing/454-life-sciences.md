---
title: "454 Life Sciences"
source: https://en.wikipedia.org/wiki/454_Life_Sciences
domain: cancer-genome-sequencing
license: CC-BY-SA-4.0
tags: cancer genome sequencing
fetched: 2026-07-09
---

# 454 Life Sciences

**454 Life Sciences** was a biotechnology company based in Branford, Connecticut that specialized in high-throughput DNA sequencing. It was acquired by Roche in 2007 and shut down by Roche in 2013 when its technology became noncompetitive, although production continued until mid-2016.

## History

454 Life Sciences was founded by Jonathan Rothberg and was originally known as 454 Corporation, a subsidiary of CuraGen. For their method for low-cost gene sequencing, 454 Life Sciences was awarded the Wall Street Journal's Gold Medal for Innovation in the Biotech-Medical category in 2005. The name 454 was the code name by which the project was referred to at CuraGen, and the numbers have no known special meaning.

In November 2006, Rothberg, Michael Egholm, and colleagues at 454 published a cover article with Svante Pääbo in Nature describing the first million base pairs of the Neanderthal genome, and initiated the Neanderthal Genome Project to complete the sequence of the Neanderthal genome by 2009.

In late March 2007, Roche Diagnostics acquired 454 Life Sciences for US$154.9 million. It remained a separate business unit. In October 2013, Roche announced that it would shut down 454, and stop supporting the platform by mid-2016.

In May 2007, 454 published the results of Project "Jim": the sequencing of the genome of James Watson, co-discoverer of the structure of DNA.

## Technology

454 Sequencing used a large-scale parallel pyrosequencing system capable of sequencing roughly 400-600 megabases of DNA per 10-hour run on the Genome Sequencer FLX with GS FLX Titanium series reagents.

The system relied on fixing nebulized and adapter-ligated DNA fragments to small DNA-capture beads in a water-in-oil emulsion. The DNA fixed to these beads was then amplified by PCR. Each DNA-bound bead was placed into a ~29 μm well on a PicoTiterPlate, a fiber optic chip. A mix of enzymes such as DNA polymerase, ATP sulfurylase, and luciferase was also packed into the well. The PicoTiterPlate was then placed into the GS FLX System for sequencing.

454 released the GS20 sequencing machine in 2005, the first next-generation DNA sequencer on the market. In 2008, 454 Sequencing launched the GS FLX Titanium series reagents for use on the Genome Sequencer FLX instrument, with the ability to sequence 400-600 million base pairs per run with 400-500 base pair read lengths. In late 2009, 454 Life Sciences introduced the GS Junior System, a bench top version of the Genome Sequencer FLX System.

### DNA library preparation and emPCR

Genomic DNA was fractionated into smaller fragments (300-800 base pairs) and polished (made blunt at each end). Short adaptors were then ligated onto the ends of the fragments. These adaptors provided priming sequences for both amplification and sequencing of the sample-library fragments. One adaptor (Adaptor B) contained a 5'-biotin tag for immobilization of the DNA library onto streptavidin-coated beads. After nick repair, the non-biotinylated strand was released and used as a single-stranded template DNA (sstDNA) library. The sstDNA library was assessed for its quality, and the optimal amount (DNA copies per bead) needed for emPCR is determined by titration.

The sstDNA library was immobilized onto beads. The beads containing a library fragment carried a single sstDNA molecule. The bead-bound library was emulsified with the amplification reagents in a water-in-oil mixture. Each bead was captured within its own microreactor where PCR amplification occurs. This resulted in bead-immobilized, clonally amplified DNA fragments.

### Sequencing

Single-stranded template DNA library beads were added to the DNA Bead Incubation Mix (containing DNA polymerase) and were layered with *Enzyme Beads* (containing sulfurylase and luciferase) onto a PicoTiterPlate device. The device was centrifuged to deposit the beads into the wells. The layer of Enzyme Beads ensured that the DNA beads remained positioned in the wells during the sequencing reaction. The bead-deposition process was designed to maximize the number of wells that contain a single amplified library bead.

The loaded PicoTiterPlate device were placed into the Genome Sequencer FLX Instrument. The fluidics sub-system delivered sequencing reagents (containing buffers and nucleotides) across the wells of the plate. The four DNA nucleotides were added sequentially in a fixed order across the PicoTiterPlate device during a sequencing run. During the nucleotide flow, millions of copies of DNA bound to each of the beads were sequenced in parallel. When a nucleotide complementary to the template strand was added into a well, the polymerase extended the existing DNA strand by adding nucleotide(s). Addition of one (or more) nucleotide(s) generated a light signal that was recorded by the CCD camera in the instrument. This technique was based on sequencing-by-synthesis and called pyrosequencing. The signal strength was proportional to the number of nucleotides; for example, homopolymer stretches, incorporated in a single nucleotide flow, generated a greater signal than single nucleotides. However, the signal strength for homopolymer stretches was linear only up to eight consecutive nucleotides, after which the signal fell off rapidly. Data were stored in standard flowgram format (SFF) files for downstream analysis.
