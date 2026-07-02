---
title: "Guide RNA"
source: https://en.wikipedia.org/wiki/Guide_RNA
domain: crispr-cas9-deep
license: CC-BY-SA-4.0
tags: cas9 nuclease, guide rna, protospacer adjacent, double strand break
fetched: 2026-07-02
---

# Guide RNA

**Guide RNA** (gRNA) or single guide RNA (sgRNA) is a short sequence of RNA that guides a CRISPR-associated protein to its nucleic acid sequence target by Watson-Crick base pairing. In bacteria and archaea, gRNAs are a part of the CRISPR-Cas system that serves as an adaptive immune defense that protects the organism from viruses. Here the short gRNAs serve as detectors of foreign DNA and direct the Cas-enzymes that degrades the foreign nucleic acid.

## History

The RNA editing guide RNA was discovered in 1990 by B. Blum, N. Bakalara, and L. Simpson through Northern Blot Hybridization in the mitochondrial maxicircle DNA of the eukaryotic parasite Leishmania tarentolae. Subsequent research throughout the mid-2000s and the following years explored the structure and function of gRNA and the CRISPR-Cas system. A significant breakthrough occurred in 2012 when it was discovered that gRNA could guide the Cas9 endonuclease to introduce target-specific cuts in double-stranded DNA. This discovery led to the 2020 Nobel Prize in Chemistry awarded to Jennifer Doudna and Emmanuelle Charpentier for their contributions to the development of CRISPR-Cas9 gene-editing technology.

## Guide RNA in Protists

Trypanosomatid protists and other kinetoplastids have a post-transcriptional RNA modification process known as "RNA editing" that performs a uridine insertion/deletion inside mitochondria. This mitochondrial DNA is circular and is divided into maxicircles and minicircles. A mitochondrion contains about 50 maxicircles which have both coding and non coding regions and consists of approximately 20 kilo bases (kb). The coding region is highly conserved (16-17kb) and the non-coding region varies depending on the species. Minicircles are small (around 1 kb) but more numerous than maxicircles, a mitochondrion contains several thousands minicircles. Maxicircles can encode "cryptogenes" and some gRNAs; minicircles can encode the majority of gRNAs. Some gRNA genes show identical insertion and deletion sites even if they have different sequences, whereas other gRNA sequences are not complementary to pre-edited mRNA. Maxicircles and minicircles molecules are catenated into a giant network of DNA inside the mitochondrion.

The majority of maxicircle transcripts cannot be translated into proteins due to frameshifts in their sequences. These frameshifts are corrected post-transcriptionally through the insertion and deletion of uridine residues at precise sites, which then create an open reading frame. This open reading frame is subsequently translated into a protein that is homologous to mitochondrial proteins found in other cells. The process of uridine insertion and deletion is mediated by short guide RNAs (gRNAs), which encode the editing information through complementary sequences, and allow for base pairing between guanine and uracil (GU) as well as between guanine and cytosine (GC), facilitating the editing process.

### The function of the gRNA-mRNA Complex

Guide RNAs are mainly transcribed from the intergenic region of DNA maxicircle and have sequences complementary to mRNA. The 3' end of gRNAs contains an oligo 'U' tail (5-24 nucleotides in length) which is in a nonencoded region but interacts and forms a stable complex with A and G rich regions of pre-edited mRNA and gRNA, that are thermodynamically stabilized by a 5' and 3' anchors. This initial hybrid helps in the recognition of specific mRNA site to be edited.

RNA editing typically progresses from the 3' to the 5' end on the mRNA. The initial editing process begins when a gRNA forms an RNA duplex with a complementary mRNA sequence located just downstream of the editing site. This pairing recruits a number of ribonucleoprotein complexes that direct the cleavage of the first mismatched base adjacent to the gRNA-mRNA anchor. Following this, Uridylyltransferase inserts a 'U' at the 3' end, and RNA ligase then joins the two severed ends. The process repeats at the next upstream editing site in a similar manner. A single gRNA usually encodes the information for several editing sites (an editing "block"), the editing of which produces a complete gRNA/mRNA duplex. This process of sequential editing is known as the enzyme cascade model.

In the case of "pan-edited" mRNAs, the duplex unwinds and another gRNA forms a duplex with the edited mRNA sequence, initiating another round of editing. These overlapping gRNAs form an editing "domain". Some genes contain multiple editing domains. The extent of editing for any particular gene varies among trypanosomatid species. The variation consists of the loss of editing at the 3' side, probably due to the loss of minicircle sequence classes that encode specific gRNAs. A retroposition model has been proposed to explain the partial, and in some cases, complete loss of editing through evolution. Although the loss of editing is typically lethal, such losses have been observed in old laboratory strains. The maintenance of editing over the long evolutionary history of these ancient protists suggests the presence of a selective advantage, the exact nature of which is still uncertain.

It is not clear why trypanosomatids utilize such an elaborate mechanism to produce mRNAs. It might have originated in the early mitochondria of the ancestor of the kintoplastid protist lineage, since it is present in the bodonids which are ancestral to the trypanosomatids, and may not be present in the euglenoids, which branched from the same common ancestor as the kinetoplastids.

### Guide RNA sequences

In the protozoan *Leishmania tarentolae*, 12 of the 18 mitochondrial genes are edited using this process. One such gene is Cyb. The mRNA is actually edited twice in succession. For the first edit, the relevant sequence on the mRNA is as follows:

```
mRNA 5' AAAGAAAAGGCUUUAACUUCAGGUUGU 3'
```

The 3' end is used to anchor the gRNA (gCyb-I gRNA in this case) by basepairing (some G/U pairs are used). The 5' end does not exactly match and one of three specific endonucleases cleaves the mRNA at the mismatch site.

```
gRNA 3' AAUAAUAAAUUUUUAAAUAUAAUAGAAAAUUGAAGUUCAGUA 5'
mRNA 5'   A  A   AGAAA   A G  G C UUUAACUUCAGGUUGU 3'
```

The mRNA is now "repaired" by adding U's at each editing site in succession, giving the following sequence:

```
gRNA 3' AAUAAUAAAUUUUUAAAUAUAAUAGAAAAUUGAAGUUCAGUA 5'
mRNA 5' UUAUUAUUUAGAAAUUUAUGUUGUCUUUUAACUUCAGGUUGU 3'
```

This particular gene has two overlapping gRNA editing sites. The 5' end of this section is the 3' anchor for another gRNA (gCyb-II gRNA).

## Guide RNA in Prokaryotes

### CRISPR In Prokaryotes

Prokaryotes as bacteria and archaea, use CRISPR (clustered regularly interspaced short palindromic repeats) and its associated Cas enzymes, as their adaptive immune system. When prokaryotes are infected by phages, and manage to fend off the attack, specific Cas enzymes cut the phage DNA (or RNA) and integrate the fragments into the CRISPR sequence interspaces. These stored segments are then recognized during future virus attacks, allowing Cas enzymes to use RNA copies of these segments, along with their associated CRISPR sequences, as gRNA to identify and neutralize the foreign sequences.

### Structure

Guide RNA targets the complementary sequences by simple Watson-Crick base pairing. In the type II CRISPR/cas system, the sgRNA directs the Cas-enzyme to target specific regions in the genome for targeted DNA cleavage. The sgRNA is an artificially engineered combination of two RNA molecules: CRISPR RNA (crRNA) and trans-activating crRNA (tracrRNA). The crRNA component is responsible for binding to the target-specific DNA region, while the tracrRNA component is responsible for the activation of the Cas9 endonuclease activity. These two components are linked by a short tetraloop structure, resulting in the formation of the sgRNA. The tracrRNA consist of base pairs that form a stem-loop structure, enabling its attachment to the endonuclease enzyme. The transcription of the CRISPR locus generates crRNA, which contains spacer regions flanked by repeat sequences, typically 18-20 base pairs (bp) in length. This crRNA guides the Cas9 endonuclease to the complementary target region on the DNA, where it cleaves the DNA, forming what is known as the effector complex. Modifications in the crRNA sequence within the sgRNA can alter the binding location, allowing for precise targeting of different DNA regions, effectively making it a programmable system for genome editing.

## Applications

### Designing gRNAs

The targeting specificity of CRISPR-Cas9 is determined by the 20-nucleotide (nt) sequence at the 5' end of the gRNA. The desired target sequence must precede the Protospacer Adjacent Motif (PAM), which is a short DNA sequence usually 2-6 base pairs in length that follows the DNA region targeted for cleavage by the CRISPR system, such as CRISPR-Cas9. The PAM is required for a Cas nuclease to cut and is usually located 3-4 nucleotides downstream from the cut site. Once the gRNA base pairs with the target, Cas9 induces a double-strand break about 3 nucleotides upstream of the PAM.

The optimal GC content of the guide sequence should be over 50%. A higher GC content enhances the stability of the RNA-DNA duplex and reduces off-target hybridization. The length of guide sequences is typically 20 bp, but they can also range from 17 to 24 bp. A longer sequence minimizes off-target effects. Guide sequences shorter than 17 bp are at risk of targeting multiple loci.

### CRISPR Cas9

CRISPR (Clustered regularly interspaced short palindromic repeats)/Cas9 is a technique used for gene editing and gene therapy. Cas is an endonuclease enzyme that cuts DNA at a specific location directed by a guide RNA. This is a target-specific technique that can introduce gene knockouts or knock-ins depending on the double strand repair pathway. Evidence shows that both in vitro and in vivo, tracrRNA is required for Cas9 to bind to the target DNA sequence. The CRISPR-Cas9 system consists of three main stages. The first stage involves the extension of bases in the CRISPR locus region by addition of foreign DNA spacers in the genome sequence. Proteins like cas1 and cas2, assist in finding new spacers. The next stage involves transcription of CRISPR: pre-crRNA (precursor CRISPR RNA) are expressed by the transcription of CRISPR repeat-spacer array. Upon further modification, the pre-crRNA is converted to single spacer flanked regions forming short crRNA. RNA maturation process is similar in type I and III but different in type II. The third stage involves binding of cas9 protein and directing it to cleave the DNA segment. The Cas9 protein binds to a combined form of crRNA and tracrRNA forming an effector complex. This serves as guide RNA for the cas9 protein directing its endonuclease activity.

### RNA mutagenesis

One important method of gene regulation is RNA mutagenesis, which can be introduced through RNA editing with the assistance of gRNA. Guide RNA replaces adenosine with inosine at specific target sites, modifying the genetic code. Adenosine deaminase acts on RNA, bringing post transcriptional modification by altering codons and different protein functions. Guide RNAs are small nucleolar RNAs that, along with riboproteins, perform intracellular RNA alterations such as ribomethylation in rRNA and the introduction of pseudouridine in preribosomal RNA. Guide RNAs bind to the antisense RNA sequence and regulate RNA modification. It has been observed that small interfering RNA (siRNA) and micro RNA (miRNA) are generally used as target RNA sequences, and modifications are comparatively easy to introduce due to their small size.
