---
title: "Genome Taxonomy Database"
source: https://en.wikipedia.org/wiki/Genome_Taxonomy_Database
domain: balneolales
license: CC-BY-SA-4.0
tags: balneolales
fetched: 2026-07-09
---

# Genome Taxonomy Database

The **Genome Taxonomy Database** (GTDB) is an online database that maintains information on a proposed nomenclature of prokaryotes, following a phylogenomic approach based on a set of conserved single-copy proteins. In addition to resolving paraphyletic groups, this method also reassigns taxonomic ranks algorithmically, updating names in both cases. Information for archaea was added in 2020, along with a species classification based on average nucleotide identity. Each update incorporates new genomes as well as automated and manual curation of the taxonomy.

An open-source tool called GTDB-Tk is available to classify draft genomes into the GTDB hierarchy. The GTDB system, via GTDB-Tk, has been used to catalogue not-yet-named bacteria in the human gut microbiome and other metagenomic sources.

The GTDB is incorporated into the *Bergey's Manual of Systematics of Archaea and Bacteria* in 2019 as its phylogenomic resource.

## Methodology

The genomes used to construct the phylogeny are obtained from NCBI (RefSeq and Genbank), and GTDB releases are indexed to RefSeq releases, starting with release 76. Importantly and increasingly, this dataset includes draft genomes of uncultured microorganisms obtained from metagenomes and single cells, ensuring improved genomic representation of the microbial world. All genomes are independently quality controlled using CheckM before inclusion in GTDB.

Genomes first undergo gene calling to extract genes. The taxonomy is based on trees inferred with FastTree from an aligned concatenated set of 120 single copy marker proteins for Bacteria under a WAG model, and with IQ-TREE from a concatenated set of 53 (since RS207; 122 before) marker proteins for Archaea under the PMSF model. Additional marker sets are also used to cross-validate tree topologies including concatenated ribosomal proteins and ribosomal RNA genes. The *relative evolutionary divergence* (RED) metric, which determines the taxonomic ranks used, is derived from the two main trees by the PhyloRank program.

Species are delimited using average nucleotide identity and alignment fraction, both calculated by *skani*. For species existing in a previous release, GTDB compares the quality and position of two genomes and may decide to switch to a new *species representative* genome.

Taxonomy comes from the following sources:

- A previous release, if available for the neighborhood of genomic similarity.
- National Center for Biotechnology Information (NCBI) taxonomy was initially used to decorate the genome tree via tax2tree.
- The 16S rRNA-based Greengenes taxonomy is used to supplement the taxonomy particularly in regions of the tree with no cultured representatives.
- List of Prokaryotic names with Standing in Nomenclature (LPSN) is used as the primary taxonomic authority for establishing naming priorities.

GTDB personnel curates the taxonomy from the aforementioned sources by checking them against the results of PhyloRank and the tree.

- The tree node corresponding to a taxon name may have a RED inappropriate for its rank. The name may either be moved onto another node or (by changing the Latin suffix) into a different rank.
  - Splitting may happen on the level of species or genera if the divergence turns out too high. Doing so creates new taxa.
- The taxon may turn out to be polyphyletic. The curator first restricts the taxon to the clade containing its type material. A new taxon is created for each of the other clades.

For the each new taxon, the curators try to find a proposed name in literature for it. If there is no name proposed, the taxon is given a placeholder name by adding a suffix to the original name, e.g. *Lactobacillus gasseri*_A. After "Z" comes "AA".

Each release contains:

- Taxonomy tables containing the assignment of all included genome assemblies to the phylum-to-species taxonomy. (One per domain.)
- Files containing the metadata given to each genome assembly, including original taxonomy from NCBI, original strain identifier, GTDB taxonomy, quality estimates, and presence of important genes (tRNA and rRNA). (One per domain.)
- Species tree Newick files containing the species-representative genomes (1 per species), built as described in the previous section. (One per domain.)
- For species-representative genomes:
  - alignments of marker genes identified from these genomes
  - file containing one 16S rRNA sequence from each species
  - tarballs containing amino acid and nucleotide versions of all predicted genes in these genomes
  - tarball containing the full contents of all these genomes
- For all genomes that pass quality check:
  - alignments of marker genes identified from these genomes
  - file containing all 16S rRNA sequences identified from these genomes
- Auxiliary files; see the full FILE_DESCRIPTIONS.txt。

The web interface displays a tree based on the taxonomy (not the entire Newick file), down to the genome assembly level. Each genome assembly has a page detailing its metadata and a history of how it's classified in each GTDB release. There is a search functionality.

## Effects on the accepted taxonomy

GTDB "has now become an important resource for prokaryotic taxonomy". Both its species tree and elements of its methodology are used by taxonomists to improve the current, accepted taxonomy under the *Prokaryotic Code*. For example, a taxonomist may make references to the GTDB tree on top of their own phylogenetic tree to further support a taxonomic proposal.

There has been even more ambitious proposals to import large parts of the database into the accepted taxonomy. A 2022 article in the IJSEM, written by third-party authors, proposes to assign names based on meaningless Latin syllable to over 65 thousand GTDB taxa, though none of these names have made their way into the LPSN. A 2023 article by the GTDB team proposes to import 223 higher-order taxa into the *Prokaryotic Code* system and 49 under the *SeqCode* system. Many of the names published under the *Prokaryotic Code* have already been validated. (The *SeqCode* requires registration of the names for valid publication, which has also been done.)

### Cyanobacteria

Unlike other bacteria, cyanobacteria are governed by a separate nomenclature code, the *Botanical Code* (ICNafp), and has a rich collection of taxa described morphologically, before the advent of molecular methods. Considerable work has been done at the higher taxonomical ranks (orders and families) to harmonize them with the results of molecular phylogeny, but problematic taxa remain at the lower levels. One representative example is the genus *Synechococcus* (and the broader Synechococcales), where distantly-related taxa remain lumped together. A 2020 article proposed using GTDB's methods to split this taxon into five orders, but it did not make an effect on the accepted taxonomy as the names were not validly published.

The *Botanical Code* treats names validly published under the *Prokaryotic Code* as valid, but the converse was not true until 2022, when the *Prokaryotic Code* reciprocated. Using some cyanobacterial genera names published under the *Botanical Code*, the aforementioned 2023 GTDB article proposed 10 cyanobacterial higher taxa to be accepted under the *Prokrayotic Code*.

The cyanobacterial community revised its higher-level taxa in 2023 independently of the GTDB, making use of a combination of phylogenomic and 16S trees. Major differences compared to GTDB include:

- GTDB takes into account genera and species never validly published and builds higher-order taxa such as "Leptococcales" from them. The corresponding clade does not have a name in the 2023 taxonomy.
- Many cyanobacterial taxa are justified by morphological differences that do not necessarily correspond to a large evolutional divergence. GTDB exhibits lumping of such taxa due to RED normalization. For example, "Cyanobacteriales" corresponds to many orders in the 2023 taxonomy: Desertifilales, Geitlerinematales, Oscillatoriales, Spirulinales, Coleofasciculales, Chroococales, Gomontiellales, Chroococcidiopsidales, Nostocales.

More broadly, the nomenclatural situation of cyanobacteria remains disordered enough to cause several confusing assignments in GTDB requiring manual adjustment. For example:

- Some cyanobacterial taxa are known to be nested in another and still provisionally kept for having "unique and distinct" features. GTDB does not respect this distinction, leading to reassignments. Results can be confusing when the genera to be merged have species that share the same specific epithets. An example is described at *Aphanizomenon flos-aquae* § Taxonomy and diversity.
- Some genera do not have a genome for its type species, nor a species closely allied to the type. This can cause a surprisingly different concept of a genus compared to the accepted taxonomy as GTDB only uses the genome, never other sources such as 16S rDNA. For example, the GTDB concept of "*Limnothrix*" is defined around a *Limnothrix rosea*, which is known to more properly belong in *Picosynechococcus*.

(Both of the above may happen for any group of prokaryotes, but cyanobacteria are particularly affected due to a higher scarcity of genomes and a historical delay in adopting molecular-based methods.)
