---
title: "FASTA format"
source: https://en.wikipedia.org/wiki/FASTA_format
domain: bioinformatics
license: CC-BY-SA-4.0
tags: bioinformatics, sequence analysis, phylogenetic tree, protein structure prediction
fetched: 2026-07-02
---

# FASTA format

In bioinformatics and biochemistry, the **FASTA format** is a text-based format for representing either nucleotide sequences or amino acid (protein) sequences, in which nucleotides or amino acids are represented using single-letter codes.

The format allows for sequence names and comments to precede the sequences. It originated from the FASTA software package and has since become a near-universal standard in bioinformatics.

The simplicity of FASTA format makes it easy to manipulate and parse sequences using text-processing tools and scripting languages.

## Overview

A sequence begins with a greater-than character (">") followed by a description of the sequence (all in a single line). The lines immediately following the description line are the sequence representation, with one letter per amino acid or nucleic acid, and are typically no more than 80 characters in length.

For example:

```mw
>MCHU - Calmodulin - Human, rabbit, bovine, rat, and chicken
MADQLTEEQIAEFKEAFSLFDKDGDGTITTKELGTVMRSLGQNPTEAELQDMINEVDADGNGTID
FPEFLTMMARKMKDTDSEEEIREAFRVFDKDGNGYISAAELRHVMTNLGEKLTDEEVDEMIREA
DIDGDGQVNYEEFVQMMTAK*
```

### Original format

The original FASTA/Pearson format is described in the documentation for the FASTA suite of programs. It can be downloaded with any free distribution of FASTA (see fasta20.doc, fastaVN.doc, or fastaVN.me—where VN is the Version Number).

In the original format, a sequence was represented as a series of lines, each of which was no longer than 120 characters and usually did not exceed 80 characters. This probably was to allow for the preallocation of fixed line sizes in software: at the time most users relied on Digital Equipment Corporation (DEC) VT220 (or compatible) terminals which could display 80 or 132 characters per line. Most people preferred the bigger font in 80-character modes and so it became the recommended fashion to use 80 characters or less (often 70) in FASTA lines. Also, the width of a standard printed page is 70 to 80 characters (depending on the font). Hence, 80 characters became the norm.

The first line in a FASTA file started either with a ">" (greater-than) symbol or, less frequently, a ";" (semicolon) was taken as a comment. Subsequent lines starting with a semicolon would be ignored by software. Since the only comment used was the first, it quickly became used to hold a summary description of the sequence, often starting with a unique library accession number, and with time it has become commonplace to always use ">" for the first line and to not use ";" comments (which would otherwise be ignored).

Following the initial line (used for a unique description of the sequence) was the actual sequence itself in the standard one-letter character string. Anything other than a valid character would be ignored (including spaces, tabulators, asterisks, etc...). It was also common to end the sequence with an "*" (asterisk) character (in analogy with use in PIR formatted sequences) and, for the same reason, to leave a blank line between the description and the sequence. Below are a few sample sequences:

```mw
;LCBO - Prolactin precursor - Bovine
; a sample sequence in FASTA format
MDSKGSSQKGSRLLLLLVVSNLLLCQGVVSTPVCPNGPGNCQVSLRDLFDRAVMVSHYIHDLSS
EMFNEFDKRYAQGKGFITMALNSCHTSSLPTPEDKEQAQQTHHEVLMSLILGLLRSWNDPLYHL
VTEVRGMKGAPDAILSRAIEIEEENKRLLEGMEMIFGQVIPGAKETEPYPVWSGLPSLQTKDED
ARYSAFYNLLHCLRRDSSKIDTYLKLLNCRIIYNNNC*

>MCHU - Calmodulin - Human, rabbit, bovine, rat, and chicken
MADQLTEEQIAEFKEAFSLFDKDGDGTITTKELGTVMRSLGQNPTEAELQDMINEVDADGNGTID
FPEFLTMMARKMKDTDSEEEIREAFRVFDKDGNGYISAAELRHVMTNLGEKLTDEEVDEMIREA
DIDGDGQVNYEEFVQMMTAK*

>gi|5524211|gb|AAD44166.1| cytochrome b [Elephas maximus maximus]
LCLYTHIGRNIYYGSYLYSETWNTGIMLLLITMATAFMGYVLPWGQMSFWGATVITNLFSAIPYIGTNLV
EWIWGGFSVDKATLNRFFAFHFILPFTMVALAGVHLTFLHETGSNNPLGLTSDSDKIPFHPYYTIKDFLG
LLILILLLLLLALLSPDMLGDPDNHMPADPLNTPLHIKPEWYFLFAYAILRSVPNKLGGVLALFLSIVIL
GLMPFLHTSKHRSMMLRPLSQALFWTLTMDLLTLTWIGSQPVEYPYTIIGQMASILYFSIILAFLPIAGX
IENY
```

A multiple-sequence FASTA format, or multi-FASTA format, would be obtained by concatenating several single-sequence FASTA files in one file. This does not imply a contradiction with the format as only the first line in a FASTA file may start with a ";" or ">", forcing all subsequent sequences to start with a ">" in order to be taken as separate sequences (and further forcing the exclusive reservation of ">" for the sequence definition line). Thus, the examples above would be a multi-FASTA file if taken together.

Modern bioinformatics programs that rely on the FASTA format expect the sequence headers to be preceded by ">". The sequence is generally represented as "interleaved", or on multiple lines as in the above example, but may also be "sequential", or on a single line. Running different bioinformatics programs may require conversions between "sequential" and "interleaved" FASTA formats.

## Description line

The description line (defline) or header/identifier line, which begins with ">", gives a name and/or a unique identifier for the sequence, and may also contain additional information. In a deprecated practice, the header line sometimes contained more than one header, separated by a ^A (Control-A) character. In the original Pearson FASTA format, one or more comments, distinguished by a semi-colon at the beginning of the line, may occur after the header. Some databases and bioinformatics applications do not recognize these comments and follow the NCBI FASTA specification. An example of a multiple sequence FASTA file follows:

```mw
>SEQUENCE_1
MTEITAAMVKELRESTGAGMMDCKNALSETNGDFDKAVQLLREKGLGKAAKKADRLAAEG
LVSVKVSDDFTIAAMRPSYLSYEDLDMTFVENEYKALVAELEKENEERRRLKDPNKPEHK
IPQFASRKQLSDAILKEAEEKIKEELKAQGKPEKIWDNIIPGKMNSFIADNSQLDSKLTL
MGQFYVMDDKKTVEQVIAEKEKEFGGKIKIVEFICFEVGEGLEKKTEDFAAEVAAQL
>SEQUENCE_2
SATVSEINSETDFVAKNDQFIALTKDTTAHIQSNSLQSVEELHSSTINGVKFEEYLKSQI
ATIGENLVVRRFATLKAGANGVVNGYIHTNGRVGVVIAAACDSAEVASKSRDLLRQICMH
```

### NCBI identifiers

The NCBI defined a standard for the unique identifier used for the sequence (SeqID) in the header line. This allows a sequence that was obtained from a database to be labelled with a reference to its database record. The database identifier format is understood by the NCBI tools like `makeblastdb` and `table2asn`. The following list describes the NCBI FASTA defined format for sequence identifiers.

| Type | Format(s) | Example(s) |
|---|---|---|
| local (i.e. no database reference) | `lcl\|*integer*` `lcl\|*string*` | `lcl\|123` `lcl\|hmm271` |
| GenInfo backbone seqid | `bbs\|*integer*` | `bbs\|123` |
| GenInfo backbone moltype | `bbm\|*integer*` | `bbm\|123` |
| GenInfo import ID | `gim\|*integer*` | `gim\|123` |
| GenBank | `gb\|*accession*\|*locus*` | `gb\|M73307\|AGMA13GT` |
| EMBL | `emb\|*accession*\|*locus*` | `emb\|CAM43271.1\|` |
| PIR | `pir\|*accession*\|*name*` | `pir\|\|G36364` |
| SWISS-PROT | `sp\|*accession*\|*name*` | `sp\|P01013\|OVAX_CHICK` |
| patent | `pat\|*country*\|*patent*\|*sequence-number*` | `pat\|US\|RE33188\|1` |
| pre-grant patent | `pgp\|*country*\|*application-number*\|*sequence-number*` | `pgp\|EP\|0238993\|7` |
| RefSeq | `ref\|*accession*\|*name*` | `ref\|NM_010450.1\|` |
| general database reference (a reference to a database that's not in this list) | `gnl\|*database*\|*integer*` `gnl\|*database*\|*string*` | `gnl\|taxon\|9606` `gnl\|PID\|e1632` |
| GenInfo integrated database | `gi\|*integer*` | `gi\|21434723` |
| DDBJ | `dbj\|*accession*\|*locus*` | `dbj\|BAC85684.1\|` |
| PRF | `prf\|*accession*\|*name*` | `prf\|\|0806162C` |
| PDB | `pdb\|*entry*\|*chain*` | `pdb\|1I4L\|D` |
| third-party GenBank | `tpg\|*accession*\|*name*` | `tpg\|BK003456\|` |
| third-party EMBL | `tpe\|*accession*\|*name*` | `tpe\|BN000123\|` |
| third-party DDBJ | `tpd\|*accession*\|*name*` | `tpd\|FAA00017\|` |
| TrEMBL | `tr\|*accession*\|*name*` | `tr\|Q90RT2\|Q90RT2_9HIV1` |

The vertical bars ("|") in the above list are not separators in the sense of the Backus–Naur form but are part of the format. Multiple identifiers can be concatenated, also separated by vertical bars.

## Sequence representation

Following the header line, the actual sequence is represented. Sequences may be protein sequences or nucleic acid sequences, and they can contain gaps or alignment characters (see sequence alignment). Sequences are expected to be represented in the standard IUB/IUPAC amino acid and nucleic acid codes, with these exceptions: lower-case letters are accepted and are mapped into upper-case; a single hyphen or dash can be used to represent a gap character; and in amino acid sequences, U and * are acceptable letters (see below). Numerical digits are not allowed but are used in some databases to indicate the position in the sequence. The nucleic acid codes supported are:

| Nucleic Acid Code | Meaning | Mnemonic |
|---|---|---|
| A | A | **A**denine |
| C | C | **C**ytosine |
| G | G | **G**uanine |
| T | T | **T**hymine |
| U | U | **U**racil |
| (i) | i | **i**nosine (non-standard) |
| R | A or G (I) | pu**R**ine |
| Y | C, T or U | p**Y**rimidines |
| K | G, T or U | bases which are **K**etones |
| M | A or C | bases with a**M**ino groups |
| S | C or G | **S**trong interaction |
| W | A, T or U | **W**eak interaction |
| B | not A (i.e. C, G, T or U) | **B** comes after A |
| D | not C (i.e. A, G, T or U) | **D** comes after C |
| H | not G (i.e., A, C, T or U) | **H** comes after G |
| V | neither T nor U (i.e. A, C or G) | **V** comes after U |
| N | A C G T U | **N**ucleic acid |
| - | gap of indeterminate length |   |

The amino acid codes supported (22 amino acids and 3 special codes) are:

| Amino Acid Code | Meaning |
|---|---|
| A | Alanine |
| B | Aspartic acid (D) or Asparagine (N) |
| C | Cysteine |
| D | Aspartic acid |
| E | Glutamic acid |
| F | Phenylalanine |
| G | Glycine |
| H | Histidine |
| I | Isoleucine |
| J | Leucine (L) or Isoleucine (I) |
| K | Lysine |
| L | Leucine |
| M | Methionine/Start codon |
| N | Asparagine |
| O | Pyrrolysine (rare) |
| P | Proline |
| Q | Glutamine |
| R | Arginine |
| S | Serine |
| T | Threonine |
| U | Selenocysteine (rare) |
| V | Valine |
| W | Tryptophan |
| Y | Tyrosine |
| Z | Glutamic acid (E) or Glutamine (Q) |
| X | any |
| * | translation stop |
| - | gap of indeterminate length |

## FASTA file

### Filename extension

There is no standard filename extension for a text file containing FASTA formatted sequences. The table below shows each extension and its respective meaning.

| Extension | Meaning | Notes |
|---|---|---|
| fasta, fas, fa | generic FASTA | Any generic FASTA file |
| fna | FASTA nucleic acid | Used generically to specify nucleic acids |
| ffn | FASTA nucleotide of gene regions | Contains coding regions for a genome |
| faa | FASTA amino acid | Contains amino acid sequences |
| mpfa | FASTA amino acids | Contains multiple protein sequences |
| frn | FASTA non-coding RNA | Contains non-coding RNA regions for a genome, e.g. tRNA, rRNA |

## Extensions

FASTQ format is a form of FASTA format extended to indicate information related to sequencing. It is created by the Sanger Centre in Cambridge.

A2M/A3M are a family of FASTA-derived formats used for sequence alignments. In A2M/A3M sequences, lowercase characters are taken to mean insertions, which are then indicated in the other sequences as the dot (".") character. The dots can be discarded for compactness without loss of information. As with typical FASTA files used in alignments, the gap ("-") is taken to mean exactly one position. A3M is similar to A2M, with the added rule that gaps aligned to insertions can too be discarded.

## Working with FASTA files

A plethora of user-friendly scripts are available from the community to perform FASTA file manipulations. Online toolboxes, such as FaBox or the FASTX-Toolkit within Galaxy servers, are also available. These can be used to segregate sequence headers/identifiers, rename them, shorten them, or extract sequences of interest from large FASTA files based on a list of wanted identifiers (among other available functions). A tree-based approach to sorting multi-FASTA files (TREE2FASTA) also exists based on the coloring and/or annotation of sequences of interest in the FigTree viewer. Additionally, the Bioconductor *Biostrings* package can be used to read and manipulate FASTA files in R.

Several online format converters exist to rapidly reformat multi-FASTA files to different formats (e.g. NEXUS, PHYLIP) for use with different phylogenetic programs, such as the converter available on phylogeny.fr.
