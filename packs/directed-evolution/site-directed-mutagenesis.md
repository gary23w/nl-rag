---
title: "Site-directed mutagenesis"
source: https://en.wikipedia.org/wiki/Site-directed_mutagenesis
domain: directed-evolution
license: CC-BY-SA-4.0
tags: laboratory evolution, mutagenesis library, selection pressure, screening variant
fetched: 2026-07-02
---

# Site-directed mutagenesis

**Site-directed mutagenesis** is a molecular biology method that is used to make specific and intentional mutations to a particular DNA sequence, such as a gene, or to its gene products. Also called **site-specific mutagenesis** or **oligonucleotide-directed mutagenesis**, it is widely used for investigating the structure and biological activity of DNA, RNA, and protein molecules, and for protein engineering. The term encompasses numerous techniques that work by a wide variety of distinct mechanisms, all with the same goal of creating one or more precise, targeted nucleotide mutations (either insertions, deletions, or substitutions) within a specific nucleic acid sequence.

Site-directed mutagenesis remains one of the most important laboratory methods for creating DNA libraries by introducing mutations into DNA sequences, but with decreasing costs of *de novo* oligonucleotide synthesis, artificial gene synthesis has become an increasingly common alternative to mutating existing DNA sequences. New techniques for achieving site-directed mutagenesis continue to be developed. For example, the development of CRISPR/Cas9 technologies, based on a prokaryotic viral defense system, has allowed for precisely targeted editing of the genome *in vivo*, which is sometimes considered a type of site-directed mutagenesis.

## History

Early attempts at mutagenesis using radiation or chemical mutagens were not site-specific, instead generating random mutations in unpredictable locations. Nucleic acid analogues and other chemicals were later used to generate localized point mutations; examples of such chemicals include aminopurine, nitrosoguanidine, and bisulfite. Site-directed mutagenesis was first achieved in 1974 in the laboratory of Charles Weissmann using the nucleotide analogue N4-hydroxycytidine, which induces transition mutations of GC to AT. These methods of mutagenesis, however, are limited by the kinds of mutation they can achieve, and they are more likely to result in non-specific, off-target mutations than later site-directed mutagenesis methods.

In 1971, Clyde Hutchison and Marshall Edgell showed that it is possible to produce mutants with small fragments of phage ΦX174 and restriction nucleases. Hutchison later produced with his collaborator Michael Smith a more flexible approach to site-directed mutagenesis by using oligonucleotides in a primer extension method with DNA polymerase. For his part in the development of this process, Smith later shared the Nobel Prize in Chemistry in October 1993 with Kary B. Mullis, who invented the polymerase chain reaction.

## Basic mechanism

The basic procedure of site-directed mutagenesis requires the synthesis of a short DNA oligonucleotide primer. This synthetic primer contains the desired mutation and is complementary to the DNA sequence around the mutation site so that it can hybridize with the DNA template. The mutation may constitute one or more base substitutions (a point mutation), deletions, or insertions. The single-stranded primer is then used as the starting point for the synthesis of a new DNA molecule by DNA polymerase, which copies the rest of the gene from the complementary template. The newly synthesized molecule thus contains the mutated site, and is then introduced into a host cell in a plasmid vector and cloned. Finally, DNA sequencing of the plasmid DNA purified from colonies grown from the transformed cells is used to check that they contain the desired mutation.

## Approaches

The original method using single-primer extension was inefficient due to a low yield of mutants. This resulting mixture contains both the original unmutated template as well as the mutant strand, producing a mixed population of mutant and non-mutant progenies. Furthermore, the template used is methylated while the mutant strand is unmethylated, and the mutants may be counter-selected due to the presence of a mismatch repair system that favors the methylated template DNA, resulting in fewer mutants. Many approaches have since been developed to improve the efficiency of mutagenesis.

A large number of techniques are now available to achieve site-directed mutagenesis, although most of them have rarely been used in laboratories since the early 2000s, as newer techniques have allowed for faster and easier ways of introducing site-specific mutations into genes.

### Kunkel's method

In 1985, Thomas Kunkel introduced a technique that reduces the need to select for the mutants. The DNA fragment to be mutated is inserted into a phagemid such as M13mp18/19 and is then transformed into an *E. coli* strain deficient in two enzymes, dUTPase (*dut*) and uracil deglycosidase (*udg*). Both enzymes are part of a DNA repair pathway that protects the bacterial chromosome from mutations by the spontaneous deamination of dCTP to dUTP. The dUTPase deficiency prevents the breakdown of dUTP, resulting in a high level of dUTP in the cell. The uracil deglycosidase deficiency prevents the removal of uracil from newly synthesized DNA. As the double-mutant *E. coli* replicates the phage DNA, its enzymatic machinery may, therefore, misincorporate dUTP instead of dTTP, resulting in single-stranded DNA that contains some uracils (ssUDNA). The ssUDNA is extracted from the bacteriophage that is released into the medium, and then used as a template for mutagenesis. An oligonucleotide containing the desired mutation is used for primer extension. The heteroduplex DNA that forms consists of one parental non-mutated strand containing dUTP and a mutated strand containing dTTP. The DNA is then transformed into an *E. coli* strain carrying the wild-type *dut* and *udg* genes. Here, the uracil-containing parental DNA strand is degraded, so that nearly all of the resulting DNA consists of the mutated strand.

### Cassette mutagenesis

Unlike other methods, cassette mutagenesis need not involve primer extension using DNA polymerase. In this method, a fragment of DNA is synthesized and then inserted into a plasmid. It involves cleavage by a restriction enzyme at restriction sites in the plasmid and the subsequent ligation into the plasmid of a pair of complementary oligonucleotides containing the mutation in the gene of interest. Usually, the restriction enzymes that cut at the plasmid and the oligonucleotide are the same, permitting sticky ends of the plasmid and insert to ligate to one another. This method can generate mutants at close to 100% efficiency, but is limited by the availability of suitable restriction sites flanking the site that is to be mutated.

### PCR site-directed mutagenesis

The limitation of restriction sites in cassette mutagenesis may be overcome by using the polymerase chain reaction with oligonucleotide "primers", such that a larger fragment is generated, covering two convenient restriction sites. The exponential amplification in PCR produces a fragment containing the desired mutation in sufficient quantities to be separated from the original, unmutated plasmid by gel electrophoresis, which may then be inserted into the original context using standard recombinant molecular biology techniques. There are many variations of the same technique. The simplest method places the mutation site toward one of the ends of the fragment whereby one of two oligonucleotides used for generating the fragment contains the mutation. This involves a single step of PCR, but still has the inherent problem of requiring a suitable restriction site near the mutation site unless a very long primer is used. Other variations, therefore, employ three or four oligonucleotides, two of which may be non-mutagenic oligonucleotides that cover two convenient restriction sites and generate a fragment that can be digested and ligated into a plasmid, whereas the mutagenic oligonucleotide may be complementary to a location within that fragment well away from any convenient restriction site. These methods require multiple steps of PCR so that the final fragment to be ligated can contain the desired mutation. The design process for generating a fragment with the desired mutation and relevant restriction sites can be cumbersome. Software tools like SDM-Assist can simplify the process.

### Whole plasmid mutagenesis

For plasmid manipulations, other site-directed mutagenesis techniques have been supplanted largely by techniques that are highly efficient but relatively simple, easy to use, and commercially available as a kit. An example of these techniques is the "Quikchange" method, wherein a pair of complementary mutagenic primers are used to amplify the entire plasmid in a thermocycling reaction using a high-fidelity non-strand-displacing DNA polymerase such as *Pfu* polymerase. The reaction generates a nicked, circular DNA molecule. The template DNA must be eliminated by enzymatic digestion with a restriction enzyme such as *Dpn*I, which is specific for methylated DNA. All DNA replicated in the cells of most *Escherichia coli* strains is methylated; the template plasmid that is biosynthesized in *E. coli* will, therefore, be digested, while the mutated plasmid, which is generated *in vitro* and is therefore unmethylated, will be left undigested. Note that, in these double-stranded plasmid mutagenesis methods, while the thermocycling reaction may be used, the DNA is not exponentially amplified if the two primers are designed such that they bind symmetrically to the same region around the mutagenesis site, as described in the original protocol. In this case the amplification is linear, and it is therefore inaccurate to describe the procedure as PCR, since there is no chain reaction. However, if the primers are designed to bind in an offset manner such that the mutagenesis site is close to the 5' ends of both primers, the 3' regions of the primers can bind also to the amplified products and thus exponential product formation is observed. The name "Quikchange" originates from the registered trademark "QuikChange mutagenesis" of Stratagene, now Agilent Technologies, for site-directed mutagenesis kits. The method was developed by scientists working at Stratagene.

Note that *Pfu* polymerase can become strand-displacing at higher extension temperatures (≥70 °C) which can result in the failure of the experiment, therefore the extension reaction should be performed at the recommended temperature of 68 °C. In some applications, this method has been observed to lead to insertion of multiple copies of primers. A variation of this method, called SPRINP, prevents these artifacts and has been used in different types of site-directed mutagenesis.

Other techniques such as scanning mutagenesis of oligo-directed targets (SMOOT) can semi-randomly combine mutagenic oligonucleotides in plasmid mutagenesis. This technique can create plasmid mutagenesis libraries ranging from single mutations to comprehensive codon mutagenesis across an entire gene.

### *In vivo* site-directed mutagenesis methods

- *Delitto perfetto*
- Transplacement "pop-in pop-out"
- Direct gene deletion and site-specific mutagenesis with PCR and one recyclable marker
- Direct gene deletion and site-specific mutagenesis with PCR and one recyclable marker using long homologous regions
- *In vivo* site-directed mutagenesis with synthetic oligonucleotides

### CRISPR

Since 2013, the development of CRISPR/Cas9 genome editing technologies has allowed for the efficient introduction of various mutations into genomic DNA in a wide variety of organisms. The method does not require a transposon insertion site, leaves no marker, and its efficiency and simplicity has made it the preferred method for genome editing.

## Applications

Site-directed mutagenesis is used to generate mutations that may produce a rationally designed protein that has improved or special properties (i.e. protein engineering).

**Investigative tools** – specific mutations in DNA allow the function and properties of a DNA sequence or a protein to be investigated in a rational approach. Furthermore, single amino-acid changes by site-directed mutagenesis in proteins can help understand the importance of post-translational modifications. For instance changing a particular serine (phosphoacceptor) to an alanine (phospho-non-acceptor) in a substrate protein blocks the attachment of a phosphate group, thereby allows the phosphorylation to be investigated. This approach has been used to uncover the phosphorylation of the protein CBP by the kinase HIPK2 Another comprehensive approach is site saturation mutagenesis where one codon or a set of codons may be substituted with all possible amino acids at the specific positions.

**Commercial applications** – Proteins may be engineered to produce mutant forms that are tailored for a specific application. For example, commonly used laundry detergents may contain subtilisin, whose wild-type form has a methionine that can be oxidized by bleach, significantly reducing the activity the protein in the process. This methionine may be replaced by alanine or other residues, making it resistant to oxidation thereby keeping the protein active in the presence of bleach.

## Gene synthesis

As the cost of DNA oligonucleotide synthesis falls, artificial synthesis of a complete gene *de novo* is now a viable method for introducing mutations into genes. This method allows for extensive mutagenesis over multiple sites, including the complete redesign of the codon usage of the gene to optimise it for expression in a particular organism.
