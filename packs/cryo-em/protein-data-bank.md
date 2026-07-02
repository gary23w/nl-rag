---
title: "Protein Data Bank"
source: https://en.wikipedia.org/wiki/Protein_Data_Bank
domain: cryo-em
license: CC-BY-SA-4.0
tags: cryo-electron microscopy, single particle analysis, structural biology, vitreous ice
fetched: 2026-07-02
---

# Protein Data Bank

The **Protein Data Bank (PDB)** is a database for the three-dimensional structural data of large biological molecules such as proteins and nucleic acids, which is overseen by the Worldwide Protein Data Bank (wwPDB). This structural data is obtained and deposited by biologists and biochemists worldwide through the use of experimental methodologies such as X-ray crystallography, NMR spectroscopy, and, increasingly, cryogenic electron microscopy. All submitted data are reviewed by expert biocurators and, once approved, are made freely available on the Internet under the CC0 Public Domain Dedication. Global access to the data is provided by the websites of the wwPDB member organizations (PDBe, PDBj, RCSB PDB, BMRB and the EMDB).

The PDB is a key in areas of structural biology, such as structural genomics. Most major scientific journals and some funding agencies now require scientists to submit their structure data to the PDB. Many other databases use protein structures deposited in the PDB. For example, SCOP and CATH classify protein structures, while PDBsum provides a graphic overview of PDB entries using information from other sources, such as Gene Ontology.

## History

Two forces converged to initiate the PDB: a small but growing collection of sets of protein structure data determined by X-ray diffraction; and the newly available (1968) molecular graphics display, the *Brookhaven RAster Display* (BRAD), to visualize these protein structures in 3-D. In 1969, with the sponsorship of Walter Hamilton at the Brookhaven National Laboratory, Edgar Meyer (Texas A&M University) began to write software to store atomic coordinate files in a common format to make them available for geometric and graphical evaluation. By 1971, one of Meyer's programs, SEARCH, enabled researchers to remotely access information from the database to study protein structures offline. SEARCH was instrumental in enabling networking, thus marking the functional beginning of the PDB.

The Protein Data Bank was announced in October 1971 in Nature New Biology as a joint venture between Cambridge Crystallographic Data Centre, UK and Brookhaven National Laboratory, US.

Upon Hamilton's death in 1973, Tom Koetzle took over direction of the PDB for the subsequent 20 years. In January 1994, Joel Sussman of Israel's Weizmann Institute of Science was appointed head of the PDB. In October 1998, the PDB was transferred to the **Research Collaboratory for Structural Bioinformatics (RCSB)**; the transfer was completed in June 1999. The new director was Helen M. Berman of Rutgers University (one of the managing institutions of the RCSB, the other being the San Diego Supercomputer Center at UC San Diego). In 2003, with the formation of the wwPDB, the PDB became an international organization. The founding members are PDBe (Europe), RCSB (US), and PDBj (Japan). The Biological Magnetic Resonance Data Bank (BMRB) joined in 2006. The Electron Microscopy Data Bank (EMDB) joined in 2021. Each of the five members of wwPDB can act as deposition, data processing and distribution centers for PDB data. The data processing refers to the fact that wwPDB staff review and annotate each submitted entry. The data are then automatically checked for plausibility (the source code for this validation software has been made available to the public at no charge).

The PDB database is updated weekly (UTC+0 Wednesday), along with its holdings list. As of 21 May 2026, the PDB comprises the following:

| Molecular type | X-ray diffraction | Electron microscopy | NMR | Integrative | Multiple methods | Neutron | Total |
|---|---|---|---|---|---|---|---|
| Proteins only | 181,265 | 23,360 | 12,819 | 350 | 231 | 84 | 218,109 |
| Proteins with oligosaccharides | 10,500 | 3,754 | 34 | 8 | 11 | 1 | 14,308 |
| Protein/Nucleic Acid complexes | 9,212 | 6,856 | 287 | 26 | 8 | 0 | 16,389 |
| Nucleic Acids only | 3,161 | 27 | 1,580 | 3 | 15 | 3 | 4,789 |
| Other | 178 | 27 | 35 | 4 | 0 | 0 | 244 |
| Oligosaccharides only | 11 | 0 | 6 | 0 | 1 | 0 | 18 |
| *Total:* | 204,327 | 34,316 | 14,761 | 391 | 266 | 88 | 254,149 |

194,485 structures in the PDB have a

structure factor

file.

11,505 structures have an NMR restraint file.

6,038 structures in the PDB have a

chemical shifts

file.

33,747 structures in the PDB have a

3DEM

map file deposited in

EM Data Bank

Most structures are determined by X-ray diffraction, but about 7% of structures are determined by protein NMR. When using X-ray diffraction, approximations of the coordinates of the atoms of the protein are obtained, whereas using NMR, the distance between pairs of atoms of the protein is estimated. The final conformation of the protein is obtained from NMR by solving a distance geometry problem. After 2013, a growing number of proteins are determined by cryo-electron microscopy.

For PDB structures determined by X-ray diffraction that have a structure factor file, their electron density map may be viewed. The data of such structures may be viewed on the three PDB websites.

Historically, the number of structures in the PDB has grown at an approximately exponential rate, with 100 registered structures in 1982, 1,000 structures in 1993, 10,000 in 1999, 100,000 in 2014, and 200,000 in January 2023.

### PDB-IHM

PDB-Dev was a database also managed by wwPDB, for structural models arising from a "integrative" or "hybrid" approach, i.e. combining experiment and structure prediction. Included models use the same four-character accession code format. In 2024, PDB-Dev was renamed to PDB-IHM and unified into the PDB: its structures can now be accessed from regular wwPDB endpoints including websites. As of January 2026, PDB-IHM contains 382 entries.

## File format

The file format initially used by the PDB was called the PDB file format. The original format was restricted by the width of computer punch cards to 80 characters per line. Around 1996, the "macromolecular Crystallographic Information file" format, mmCIF, which is an extension of the CIF format was phased in. mmCIF became the standard format for the PDB archive in 2014. In 2019, the wwPDB announced that depositions for crystallographic methods would only be accepted in mmCIF format.

An XML version of PDB, called PDBML, was described in 2005. The structure files can be downloaded in any of these three formats, though an increasing number of structures do not fit the legacy PDB format. Individual files are easily downloaded into graphics packages from Internet URLs:

- For PDB format files, use, e.g., `http://www.pdb.org/pdb/files/4hhb.pdb.gz` or `http://pdbe.org/download/4hhb`
- For PDBML (XML) files, use, e.g., `http://www.pdb.org/pdb/files/4hhb.xml.gz` or `http://pdbe.org/pdbml/4hhb`

The "`4hhb`" is the PDB identifier. Each structure published in PDB receives a four-character alphanumeric identifier, its PDB ID. (This is not a unique identifier for biomolecules, because several structures for the same molecule—in different environments or conformations—may be contained in PDB with different PDB IDs.)

## Viewing the data

The structure files may be viewed using one of several free and open source computer programs, including Jmol, Pymol, VMD, Molstar and Rasmol. Other non-free, shareware programs include ICM-Browser, MDL Chime, UCSF Chimera, Swiss-PDB Viewer, StarBiochem (a Java-based interactive molecular viewer with integrated search of protein databank), Sirius, and VisProt3DS (a tool for Protein Visualization in 3D stereoscopic view in anaglyph and other modes), and Discovery Studio. The RCSB PDB website contains an extensive list of both free and commercial molecule visualization programs and web browser plugins.
