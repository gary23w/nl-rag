---
title: "Chemical file format"
source: https://en.wikipedia.org/wiki/Chemical_file_format
domain: cheminformatics-rdkit
license: CC-BY-SA-4.0
tags: cheminformatics rdkit, molecular descriptor, smiles notation, chemical fingerprint
fetched: 2026-07-02
---

# Chemical file format

A **chemical file format** is a type of data file which is used specifically for depicting molecular data. One of the most widely used is the chemical table file format, which is similar to *Structure Data Format* (SDF) files. They are text files that represent multiple chemical structure records and associated data fields. The XYZ file format is a simple format that usually gives the number of atoms in the first line, a comment on the second, followed by a number of lines with atomic symbols (or atomic numbers) and cartesian coordinates. The Protein Data Bank Format is commonly used for proteins but is also used for other types of molecules. There are many other types which are detailed below. Various software systems are available to convert from one format to another.

## Distinguishing formats

Chemical information is usually provided as files or streams and many formats have been created, with varying degrees of documentation. The format is indicated in three ways:

- **file extension** (usually 3 letters). This is widely used, but fragile as common suffixes such as *`.mol`* and *`.dat`* are used by many systems, including non-chemical ones.
- **self-describing files** where the format information is included in the file. Examples are CIF and CML.
- **chemical MIME type** added by a chemically aware server. (see § The Chemical MIME Project)

## Chemical Markup Language

Chemical Markup Language (CML) is an open standard for representing molecular and other chemical data. The open source project includes XML Schema, source code for parsing and working with CML data, and an active community. The articles Tools for Working with Chemical Markup Language and XML for Chemistry and Biosciences discusses CML in more detail. CML data files are accepted by many tools, including JChemPaint, Jmol, XDrawChem and MarvinView.

## Connectivity-only formats

Simpler chemical format focus on describing the connectivity of atoms (and sometimes their stereochemistry). They include:

### InChI

InChI is an IUPAC-standard format for describing molecules. Multiple InChI strings can be joined into an "RInChI" to describe a chemical reaction, or into a "MInChI" to describe a mixture.

### SMILES

The simplified molecular input line entry system, or SMILES, is a line notation for molecules. SMILES strings include connectivity but do not include 2D or 3D coordinates.

Hydrogen atoms are not represented. Other atoms are represented by their element symbols `B`, `C`, `N`, `O`, `F`, `P`, `S`, `Cl`, `Br`, and `I`. The symbol `=` represents double bonds and `#` represents triple bonds. Branching is indicated by `( )`. Rings are indicated by pairs of digits.

Some examples are

| Name | Formula | SMILES string |
|---|---|---|
| Methane | CH4 | `C` |
| Ethanol | C2H6O | `CCO` |
| Benzene | C6H6 | `C1=CC=CC=C1` or `c1ccccc1` |
| Ethylene | C2H4 | `C=C` |

Multiple SMILES strings can be joined into a "reaction SMILES", which describes a chemical reaction.

### SYBYL Line Notation

SYBYL Line Notation (SLN) is a chemical line notation. Based on SMILES, it incorporates a complete syntax for specifying relative stereochemistry. SLN has a rich query syntax that allows for the specification of Markush structure queries. The syntax also supports the specification of combinatorial libraries of ChemDraw.

| Description | SLN string |
|---|---|
| Benzene | `C[1]H:CH:CH:CH:CH:CH:@1` |
| Alanine | `NH2C[s=n]H(CH3)C(=O)OH` |
| Query showing R sidechain | `R1[hac>1]C[1]:C:C:C:C:C:@1` |
| Query for amide/sulfamide | `NHC=M1{M1:O,S}` |

## Coordinate formats

Some chemical formats describe the coordinates of atoms. This is important for

- knowing the 3D structure of molecules and for simulating their behavior.
- maintaining the layout of 2D molecule drawings

### Chemical table formats

One of the most widely used industry standards are the chemical table file formats. They are text files that adhere to a strict format for representing multiple chemical structure records and associated data fields. The format was originally developed and published by Molecular Design Limited (MDL). This family includes the MOLfile, the SDfile (Structure Data Format, MOLfile with metadata), the RXNfile (multiple MOLfiles put together to describe a chemical reaction), and RDfile (RXNfile with metadata).

### Protein Data Bank Format

The Protein Data Bank Format is an obsolete format for protein structures developed in 1972. It is a fixed-width format and thus limited to a maximum number of atoms, residues, and chains; this resulted in splitting very large structures such as ribosomes into multiple files. For example, the E. coli 70S was represented as 4 PDB files in 2009: 3I1M Archived 2016-10-05 at the Wayback Machine, 3I1N Archived 2016-10-16 at the Wayback Machine, 3I1O, and 3I1P. In 2014, they were consolidated into a single file, 4V6C.

Some PDB files contained an optional section describing atom connectivity as well as position. Because these files were sometimes used to describe macromolecular assemblies or molecules represented in explicit solvent, they could grow very large and were often compressed. Some tools, such as Jmol and KiNG, could read PDB files in gzipped format. The wwPDB maintained the specifications of the PDB file format and its XML alternative, PDBML. There was a fairly major change in PDB format specification (to version 3.0) in August 2007, and a remediation of many file problems in the existing database. The typical file extension for a PDB file was *`.pdb`*, although some older files used *`.ent`* or *`.brk`*. Some molecular modeling tools wrote nonstandard PDB-style files that adapted the basic format to their own needs.

#### GROMACS format

The GROMACS file format family was created for use with the molecular simulation software package GROMACS. It closely resembles the PDB format but was designed for storing output from molecular dynamics simulations, so it allows for additional numerical precision and optionally retains information about particle velocity as well as position at a given point in the simulation trajectory. It does not allow for the storage of connectivity information, which in GROMACS is obtained from separate molecule and system topology files. The typical file extension for a GROMACS file is *`.gro`*.

#### CHARMM format

The CHARMM molecular dynamics package can read and write a number of standard chemical and biochemical file formats; however, the CARD (coordinate) and PSF (protein structure file) are largely unique to CHARMM. The CARD format is fixed-column-width, resembles the PDB format, and is used exclusively for storing atomic coordinates. The PSF file contains atomic connectivity information (which describes atomic bonds) and is required before beginning a simulation. The typical file extensions used are *`.crd`* and *`.psf`* respectively.

### mmCIF format

In 2014, the PDB format was officially replaced with mmCIF. mmCIF is a new text format for representing atomic coordinates and "biological assemblies", i.e. assemblies of molecules. It can express things that the PDB format cannot express, so some newer PDB structures may not have PDB files available (but a "bundle file" containing PDB files split from the main mmCIF file can be downloaded).

There is also a more verbose XML variant.

### GSD format

The General Simulation Data (GSD) file format created for efficient reading / writing of generic particle simulations, primarily - but not restricted to - those from HOOMD-blue. The package also contains a python module that reads and writes HOOMD schema gsd files with an easy-to-use syntax.[1]

### Ghemical file format

The Ghemical software can use OpenBabel to import and export a number of file formats. However, by default, it uses the GPR format. This file is composed of several parts, separated by a tag (`!Header`, `!Info`, `!Atoms`, `!Bonds`, `!Coord`, `!PartialCharges` and `!End`).

### XYZ

The XYZ file format is a simple format that usually gives the number of atoms in the first line, a comment on the second, followed by a number of lines with atomic symbols (or atomic numbers) and cartesian coordinates.

## Other common formats

PubChem offers data export for SDF, JSON, XML, and ASNT/B formats.

### Database references

These "formats" are references to entries in specific databases. Examples include:

- The **MDL number** contains a unique identification number for each reaction and variation. The format is RXXXnnnnnnnn. R indicates a reaction, XXX indicates which database contains the reaction record. The numeric portion, nnnnnnnn, is an 8-digit number.
- The **InChIKey** is derived from crytographic hashes of parts of an InChI. The same InChI always give the same key.
- PubChem, ChEBI, KEGG etc. each have numeric entry numbers.

### Container formats

These formats wrap other formats.

#### Mixfile

The Mixfile format is a JSON-based format for describing mixtures.

## The Chemical MIME Project

Just like extension names are used to distinguish file types in folders, MIME types are used to distinguish data-stream types on the Internet. "Chemical MIME" is a project for proposing MIME types to chemical streams.

> This project started in January 1994, and was first announced during the Chemistry workshop at the First WWW International Conference, held at CERN in May 1994. ... The first version of an Internet draft was published during May–October 1994, and the second revised version during April–September 1995. A paper presented to the CPEP (Committee on Printed and Electronic Publications) at the IUPAC meeting in August 1996 is available for discussion.

In 1998 the work was formally published in the JCIM.

| File extension | MIME Type | Proper Name | Description |
|---|---|---|---|
| `.alc` | chemical/x-alchemy | Alchemy Format |   |
| `.csf` | chemical/x-cache-csf | CAChe MolStruct CSF |   |
| `.cbin`, `.cascii`, `.ctab` | chemical/x-cactvs-binary | CACTVS format |   |
| `.cdx` | chemical/x-cdx | ChemDraw eXchange file |   |
| `.cer` | chemical/x-cerius | MSI Cerius II format |   |
| `.c3d` | chemical/x-chem3d | Chem3D Format |   |
| `.chm` | chemical/x-chemdraw | ChemDraw file |   |
| `.cif` | chemical/x-cif | Crystallographic Information File, Crystallographic Information Framework | Promulgated by the International Union of Crystallography |
| `.cmdf` | chemical/x-cmdf | CrystalMaker Data format |   |
| `.cml` | chemical/x-cml | Chemical Markup Language | XML based Chemical Markup Language. |
| `.cpa` | chemical/x-compass | Compass program of the Takahashi |   |
| `.bsd` | chemical/x-crossfire | Crossfire file |   |
| `.csm`, `.csml` | chemical/x-csml | Chemical Style Markup Language |   |
| `.ctx` | chemical/x-ctx | Gasteiger group CTX file format |   |
| `.cxf`, `.cef` | chemical/x-cxf | Chemical eXchange Format |   |
| `.emb`, `.embl` | chemical/x-embl-dl-nucleotide | EMBL Nucleotide Format |   |
| `.spc` | chemical/x-galactic-spc | SPC format for spectral and chromatographic data |   |
| `.inp`, `.gam`, `.gamin` | chemical/x-gamess-input | GAMESS Input format |   |
| `.fch`, `.fchk` | chemical/x-gaussian-checkpoint | Gaussian Checkpoint Format |   |
| `.cub` | chemical/x-gaussian-cube | Gaussian Cube (Wavefunction) Format |   |
| `.gau`, `.gjc`, `.gjf`, `.com` | chemical/x-gaussian-input | Gaussian Input Format |   |
| `.gcg` | chemical/x-gcg8-sequence | Protein Sequence Format |   |
| `.gen` | chemical/x-genbank | GenBank Format | Not a general-purpose chemical format, but one that focuses on biological macromolecule sequences |
|   | application/x-ghemical | Ghemical format |   |
| `.istr`, `.ist` | chemical/x-isostar | IsoStar Library of Intermolecular Interactions |   |
| `.jdx`, `.dx` | chemical/x-jcamp-dx | JCAMP Spectroscopic Data Exchange Format |   |
| `.kin` | chemical/x-kinemage | Kinetic (Protein Structure) Images; Kinemage |   |
| `.mcm` | chemical/x-macmolecule | MacMolecule File Format |   |
| `.mmd`, `.mmod` | chemical/x-macromodel-input | MacroModel Molecular Mechanics |   |
| `.mol` | chemical/x-mdl-molfile | MDL Molfile |   |
| `.smiles`, `.smi` | chemical/x-daylight-smiles | Simplified molecular input line entry specification | A line notation for molecules. |
| `.sdf` | chemical/x-mdl-sdfile | Structure-Data File |   |
| `.el` | chemical/x-sketchel | SketchEl Molecule |   |
| `.ds` | chemical/x-datasheet | SketchEl XML DataSheet |   |
| `.inchi` | chemical/x-inchi | IUPAC International Chemical Identifier (InChI) |   |
| `.jsd`, `.jsdraw` | chemical/x-jsdraw | JSDraw native file format |   |
| `.helm`, `.ihelm` | chemical/x-helm | Pistoia Alliance HELM string | A line notation for biological molecules |
| `.xhelm` | chemical/x-xhelm | Pistoia Alliance XHELM XML file | XML based HELM including monomer definitions |

### Support

For Linux/Unix, configuration files are available as a "*chemical-mime-data*" package in .deb, RPM and tar.gz formats to register chemical MIME types on a web server. Programs can then register as viewer, editor or processor for these formats so that full support for chemical MIME types is available.

## Converting between formats

OpenBabel and JOELib are freely available open source tools specifically designed for converting between file formats. Their chemical expert systems support a large atom type conversion tables.

obabel -i

input_format

input_file

-o

output_format

output_file

For example, to convert the file epinephrine.sdf in SDF to CML use the command

obabel -i sdf epinephrine.sdf -o cml epinephrine.cml

The resulting file is epinephrine.cml.

IOData is a free and open-source Python library for parsing, storing, and converting various file formats commonly used by quantum chemistry, molecular dynamics, and plane-wave density-functional-theory software programs. It also supports a flexible framework for generating input files for various software packages. For a complete list of supported formats, please go to https://iodata.readthedocs.io/en/latest/formats.html.

A number of tools intended for viewing and editing molecular structures are able to read in files in a number of formats and write them out in other formats. The tools JChemPaint (based on the Chemistry Development Kit), XDrawChem (based on OpenBabel), Chime, Jmol, Mol2mol and Discovery Studio fit into this category.

## Sources of chemical data

Here is a short list of sources of freely available molecular data. There are many more resources than listed here out there on the Internet. Links to these sources are given in the references below.

Small molecules:

1. The US National Institute of Health PubChem database is a huge source of chemical data. All entries have two-dimensional data, with a few having 3D conformer data available. Data includes SDF, SMILES, InChI, PubChem XML, and PubChem ASN1 formats.
2. eMolecules is a commercial database for molecular data. The data includes a two-dimensional structure diagram and a smiles string for each compound. eMolecules supports fast substructure searching based on parts of the molecular structure.
3. ChemExper is a commercial data base for molecular data. The search results include a two-dimensional structure diagram and a mole file for many compounds.
4. New York University Library of 3-D Molecular Structures.
5. The US Environmental Protection Agency's The Distributed Structure-Searchable Toxicity (DSSTox) Database Network is a project of EPA's Computational Toxicology Program. The database provides SDF molecular files with a focus on carcinogenic and otherwise toxic substances.

Macromolecules:

1. The worldwide Protein Data Bank (wwPDB) is an excellent source of protein and nucleic acid molecular coordinate data. The data is three-dimensional and provided in Protein Data Bank (PDB) format.
2. Databases for predicted protein and nucleic acid structures such as AlphaFold Protein Structure Database and Swiss-Model also provide PDB format download.
