---
title: "Protospacer adjacent motif"
source: https://en.wikipedia.org/wiki/Protospacer_adjacent_motif
domain: crispr-cas9-deep
license: CC-BY-SA-4.0
tags: cas9 nuclease, guide rna, protospacer adjacent, double strand break
fetched: 2026-07-02
---

# Protospacer adjacent motif

A **protospacer adjacent motif** (**PAM**) is a 2–6-base pair DNA sequence immediately following the DNA sequence targeted by the Cas9 nuclease in the CRISPR bacterial adaptive immune system. The PAM is a component of the invading virus or plasmid, but is not found in the bacterial host genome and hence is not a component of the bacterial CRISPR locus. Cas9 will not successfully bind to or cleave the target DNA sequence if it is not followed by the PAM sequence. PAM is an essential targeting component which distinguishes bacterial self from non-self DNA, thereby preventing the CRISPR locus from being targeted and destroyed by the CRISPR-associated nuclease.

## Spacers/protospacers

In a bacterial genome, CRISPR loci contain "spacers" (viral DNA inserted into a CRISPR locus) that in type II adaptive immune systems were created from invading viral or plasmid DNA (called "protospacers"). Upon subsequent invasion, a CRISPR-associated nuclease such as Cas9 attaches to a tracrRNA–crRNA complex, which guides Cas9 to the invading protospacer sequence. But Cas9 will not cleave the protospacer sequence unless there is an adjacent PAM sequence. The spacer in the bacterial CRISPR loci will not contain a PAM sequence, and thus will not be cut by the nuclease, but the protospacer in the invading virus or plasmid will contain the PAM sequence, and thus will be cleaved by the Cas9 nuclease. In genome editing applications, a single-stranded RNA known as a single guide RNA (sgRNA) is synthesized to perform the function of the tracrRNA–crRNA complex in recognizing gene sequences having a PAM sequence at the 3'-end, thereby "guiding" the nuclease to a specific sequence which the nuclease is capable of cutting.

## PAM sequences

The canonical Cas9 PAM is the sequence 5'-NGG-3', where "N" is any nucleobase followed by two guanine ("G") nucleobases. sgRNAs can transport Cas9 to any locus in the genome for gene editing, but no editing can occur at any site other than one at which Cas9 recognizes PAM. The canonical PAM is associated with the Cas9 nuclease of *Streptococcus pyogenes* (designated SpCas9), whereas different PAMs are associated with the Cas9 proteins of the bacteria *Neisseria meningitidis*, *Treponema denticola*, and *Streptococcus thermophilus*. 5'-NGA-3' can be a highly efficient non-canonical PAM for human cells, but efficiency varies with genome location. Attempts have been made to engineer Cas9s to recognize different PAMs in order to improve the ability of CRISPR-Cas9 to edit genes at any desired genome location.

The Cas9 of *Francisella novicida* recognizes the canonical PAM sequence 5'-NGG-3', but has been engineered to recognize 5'-YG-3' (where "Y" is a pyrimidine), thus adding to the range of possible Cas9 targets. The Cpf1 nuclease of *Francisella novicida* recognizes the PAM 5'-TTTN-3' or 5'-YTN-3'.

Aside from CRISPR-Cas9 and CRISPR-Cpf1, there are doubtless many yet undiscovered nucleases and PAMs.

CRISPR/Cas13a (formerly C2c2) from the bacterium *Leptotrichia shahii* is an RNA-guided CRISPR system that targets sequences in RNA rather than DNA. PAM is not relevant for an RNA-targeting CRISPR, although a guanine flanking the target negatively affects efficacy, and has been designated a "protospacer flanking site" (PFS).

## GUIDE-Seq

A technology called GUIDE-Seq has been devised to assay off-target cleavages produced by such gene editing. The PAM requirement can be exploited to specifically target single-nucleotide heterozygous mutations while exerting no aberrant effects on wild-type alleles.
