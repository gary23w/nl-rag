---
title: "National Center for Biotechnology Information"
source: https://en.wikipedia.org/wiki/National_Center_for_Biotechnology_Information
domain: balneolales
license: CC-BY-SA-4.0
tags: balneolales
fetched: 2026-07-09
---

# National Center for Biotechnology Information

Coordinates

:

38°59′45″N

77°05′56″W

﻿ / ﻿

38.9959°N 77.0989°W

﻿ /

38.9959; -77.0989

The **National Center for Biotechnology Information** (**NCBI**) is part of the National Library of Medicine (NLM), a branch of the National Institutes of Health (NIH). It is approved and funded by the government of the United States. The NCBI is located in Bethesda, Maryland, and was founded in 1988 through legislation sponsored by US Congressman Claude Pepper.

The NCBI houses a series of databases relevant to biotechnology and biomedicine and is an important resource for bioinformatics tools and services. Major databases include GenBank for DNA sequences and PubMed, a bibliographic database for biomedical literature. Other databases include the NCBI Epigenomics database. All these databases are available online through the Entrez search engine. NCBI was directed by David Lipman, one of the original authors of the BLAST sequence alignment program and a widely respected figure in bioinformatics.

## History

### Proposal and establishment

The US National Library of Medicine performed a planning excursion from 1985 through 1986 to develop long-term plans for the agency which highlighted inconsistencies in the naming schemes utilized by and lack of connections between existing biotechnology knowledge databases created by different organizations researching genetics. These inconsistencies created roadblocks for researchers utilizing multiple databases in tandem in their studies, as related information in different databases was difficult to integrate and made using information from one database as evidence to explain information in another database difficult. This led the NLM to propose the creation of the NCBI to lead the standardization between biotechnology databases to promote easier retrieval of information by users and allow interlinking of databases for study. The proposal for NCBI also sought for it to act as a storage repository and distribution center for biotechnology information, as well as a developer of information analysis tools. Congressman Claude Pepper, an advocate for medical research, introduced multiple bills to Congress between 1986 and 1988 proposing the creation of the NCBI before the proposal was approved on November 4, 1988, establishing the NCBI within the NLM.

### Further developments

In 1990, a team at NCBI including mathematician Stephen Altschul developed the BLAST tool for comparing biological sequences, building upon the preexisting FASTA program. The NCBI also assumed responsibility for the preexisting GenBank database of DNA and amino acid sequences, initially allowing internet access through email in 1992. In 1994, the NCBI established a website to allow easier online access to their services, namely the BLAST tool, the GenBank database, and the Entrez retrieval system for searching biomedical databases. The NCBI would later go on in 2000 to host access to the human genome, mapped by the Human Genome Project, as well as PubMed Central, a free online archive of biomedical literature from scientific journals. The US Congress would later mandate in 2008 that papers resulting from research provided by NIH funding featured in scientific journals be made available publicly on PubMed within 12 months of publication, further broadening the articles hosted.

## Key NCBI resources

The NCBI website provides a wide range of databases and tools for Biomedical and genomic research.

### Literature resources

- PubMed: A database for searching for citations and abstracts of various biomedical research literature.
- Bookshelf: A collection of books on life science and healthcare.
- PubMed Central(PMC): A free full-text archive for biomedical and life sciences journal literature that can be used for research, publishing, and text mining.

### Analysis tools

- BLAST: A tool used to find similarities between biological sequences.

### Molecular and genomic databases

- Nucleotide Database: A database of nucleotide sequences.
- Protein Database: A database of protein sequences.
- Genome Database: A database that gives you access to over 3.45 million genomes as of 2026.
- Gene Database: A database that has information about genes across species.
- dbSNP: A database that contains human single-nucleotide variations, microsatellites, small-scale insertions, and deletions.
- PubChem: A database of freely accessible chemical information.
- Sequence Read Archive: The SRA stores sequencing data from the next generation of sequencing platforms, including Roche 454 GS System, Illumina Genome Analyzer, Life Technologies AB SOLiD System, Helicos Biosciences Heliscope, Complete Genomics, and Pacific Biosciences SMRT.
- ClinVar: A database that aggregates information about genomic variations and their relationship to human health.

A complete list of available resources can be found on the All-Resources page.

## NCBI Bookshelf

The NCBI Bookshelf stands as a freely accessible digital repository which provides researchers and educators and the public with access to biomedical books and documents. The repository is maintained by the National Center for Biotechnology Information which supports wide dissemination of scientific knowledge.

The Bookshelf contains multiple publication types including textbooks and clinical manuals and guidelines and monographs. These resources are contributed by government agencies and academic institutions and scientific publishers which ensures reliability and relevance to the biomedical field.

Access to the NCBI Bookshelf is provided through the NCBI web interface which allows users to search and navigate filters across integrated biomedical databases. The interface incorporates search functionalities which support keyword queries and filtering for efficient information retrieval.

The integration of the Bookshelf with other NCBI resources stands as a key strength which enables navigation between scientific literature and biological data. Entries may be linked to related records in PubMed and Gene databases which enhances accessibility and research productivity.

Publishers may submit materials to the Bookshelf through a structured process which requires scientific accuracy and peer review and relevance to biomedical topics. Accepted materials undergo standardized formatting and metadata indexing which facilitates efficient searching and cross-referencing.

The NCBI Bookshelf plays an important role in supporting education and clinical practice and research because it provides free access to high-quality scientific literature. This availability encourages evidence-based decision making and contributes to knowledge dissemination and research advancement within the global biomedical community.

BLAST (Basic Local Alignment Search Tool) is an algorithm and suite of programs used to perform sequence similarity searches between a query sequence and sequences in a selected database, such as GenBank. It is commonly used to compare nucleotide and protein sequences by identifying regions of local similarity.

BLAST operates by using heuristic methods, taking shortcuts in order to reach an answer faster. BLAST has to read in a user-inputted query sequence then the sequence from the selected database and search parameters. It then analyzes the query sequence for low complexity and repeats within this sequence in order to produce a set of characters that’ll be used to compare the query sequence to sequences within the database. First, the database searches for short matching sequences using the character set, which are then extended, not allowing gaps to find initial alignments. If these gap free alignments reach a certain score threshold, they are used to begin a gapped extension that estimates the alignment's score and length without yet calculating insertions or deletions, which are more computationally expensive. In order to avoid a computationally expensive process, only gapped alignments that meet a specified score are kept, with lower scored alignments being discarded. Finally, BLAST performs traceback, meaning the retained alignments are fully extended again, this time including insertions and deletions as well as more sensitive parameters to produce the final, detailed alignments.

Input sequences are typically provided in FASTA or GenBank format, and results can be returned in multiple formats including HTML, XML, and plain text. The default output from the webpage presents results in table format, along with graphs of matched sequences in a separate tab, statistical significance values, and detailed alignments between the query and subject sequences.

### BLAST programs

There are multiple BLAST programs available through the NCBI BLAST homepage, which differ in the types of sequences they analyze. The Image below displays one such program, blastp, displaying the interface's general layout.

These Programs include:

- **blastn**: Compares nucleotide sequences against nucleotide sequences in a selected database, often used for identifying more distant relationships.
- **blastp**: Compares protein sequences against protein sequences in a selected database; its algorithm forms the basis for other BLAST programs such as blastx and tblastn.
- **blastx**: Compares translated nucleotide sequences against protein sequences in a selected database.
- **tblastn**: Compares protein sequences against translated nucleotide sequences in a selected database.

## Entrez

The Entrez Global Query Cross-Database Search System is used at NCBI for all the major databases such as Nucleotide and Protein Sequences, Protein Structures, PubMed, Taxonomy, Complete Genomes, OMIM, and several others. Entrez is both an indexing and retrieval system having data from various sources for biomedical research. NCBI distributed the first version of Entrez in 1991, composed of nucleotide sequences from PDB and GenBank, protein sequences from SWISS-PROT, translated GenBank, PIR, PRF, PDB, and associated abstracts and citations from PubMed. Entrez is specially designed to integrate the data from several different sources, databases, and formats into a uniform information model and retrieval system which can efficiently retrieve that relevant references, sequences, and structures.

## Databases

NCBI hosts many different databases associated with Biotechnology Information, Ranging from chemical compounds to gene and protein sequences.

### GenBank

GenBank is the NIH genetic sequence database, an annotated collection of all publicly available DNA sequences. Database resources have been maintained by NCBI since 1992 when the organization had responsibility for making available the GenBank DNA sequence database. GenBank coordinates with individual laboratories and other sequence databases, such as those of the European Molecular Biology Laboratory (EMBL) and the DNA Data Bank of Japan (DDBJ). Since 1992, NCBI has grown to provide other databases in addition to GenBank.

### Gene

The database Gene is a collection of characterization and organized information about genes. It serves as a major node in the nexus of the genomic map, expression, sequence, protein function, structure, and homology data. A unique GeneID is assigned to each gene record that can be followed through revision cycles. Gene records for known or predicted genes are established here and are demarcated by map positions or nucleotide sequences. Gene has several advantages over its predecessor, LocusLink, including, better integration with other databases in NCBI, broader taxonomic scope, and enhanced options for query and retrieval provided by the Entrez system.

### Protein

The database Protein is a collection of text record for individual protein sequences, derived from many different resources such as NCBI Reference Sequence (RefSeq) project, GenBank, PDB, and UniProtKB/SWISS-Prot. Protein records are present in different formats including FASTA and XML and are linked to other NCBI resources. Protein provides the relevant data to the users such as genes, DNA/RNA sequences, biological pathways, expression and variation data, and literature. It also provides the predetermined sets of similar and identical proteins for each sequence as computed by the BLAST. The Structure database of NCBI contains 3D coordinate sets for experimentally determined structures in PDB that are imported by NCBI. The Conserved Domain database (CDD) of protein contains sequence profiles that characterize highly conserved domains within protein sequences. It also has records from external resources like SMART and Pfam. There is another database of proteins known as Protein Clusters database, which contains sets of proteins sequences that are clustered according to the maximum alignments between the individual sequences as calculated by BLAST.

### PubChem

The PubChem database of NCBI is a public resource for molecules and their activities against biological assays. PubChem is searchable and accessible by Entrez information retrieval system. Furthermore, PubChem consists of three primary databases:

- Substance stores descriptions of chemical samples from various sources.
- Compound is a database storing validated chemical depictions. Such structures are pre-clustered and are referenced through similarity groups.
- BioAssay is a PubChem database storing bioactivity of chemical substances.

The data stored in both the BioAssay and the Compound databases describes data from PubChem's Substance database.

### Other databases

Some of the other databases provided by NCBI include the Online Mendelian Inheritance in Man, the Molecular Modeling Database (3D protein structures), dbSNP (a database of single-nucleotide polymorphisms), the Reference Sequence Collection, a map of the human genome, and a taxonomy browser, and coordinates with the National Cancer Institute to provide the Cancer Genome Anatomy Project. The NCBI assigns a unique identifier (taxonomy ID number) to each species of organism. The NCBI has software tools that are available through web browsers or by File Transfer Protocol (FTP).
