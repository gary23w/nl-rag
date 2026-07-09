---
title: "AMR (R package)"
source: https://en.wikipedia.org/wiki/AMR_(R_package)
domain: antimicrobial-resistance
license: CC-BY-SA-4.0
tags: antimicrobial resistance
fetched: 2026-07-09
---

# AMR (R package)

**AMR** is a free and open-source package for the R programming language, designed to simplify the analysis of antimicrobial resistance (AMR) data.

It has aimed to provide a standard for clean and reproducible AMR data analysis, enabling surveillance and treatment evaluation in both clinical and research settings. Since its first public release on CRAN in early 2018, the package has been downloaded from over 175 countries, as measured by CRAN download logs. It has been adopted in clinical, veterinary, and environmental microbiology settings worldwide.

Studies employing the package have included national paediatric bloodstream infection surveillance, population-wide AMR burden analysis, companion animal MRSA surveillance across veterinary practices, environmental resistance gene screening in fresh produce, and a perspective on clinical AMR surveillance tools.

## Initial development

The package was initially developed at the University of Groningen and the University Medical Center Groningen (UMCG), in the Netherlands.

The work was published as a peer-reviewed paper in the *Journal of Statistical Software* and formed the basis of two PhD theses at the University of Groningen. According to CRAN, the package has no external dependencies and is compatible with R versions from R-3.0 (April 2013) onwards.

## Background

Antimicrobial resistance is recognised by the World Health Organization as one of the leading public health threats globally. Laboratories routinely test microorganisms for resistance against antimicrobial agents, and the resulting data must be reported and analysed at various levels, from local hospitals to international surveillance networks. Despite the existence of international standards for testing and reporting, there was, prior to the AMR package, a lack of standardised open-source tools to process and analyse these data in a reproducible manner. Data from laboratory information systems often require substantial cleaning and validation before analysis, and meaningful interpretation depends on up-to-date reference data, such as microbial taxonomy and clinical breakpoint guidelines.

The AMR package was developed to bridge this gap, providing an integrated toolbox that incorporates relevant international guidelines and reference data directly into the analysis workflow.

## Functionality

The package offers tools for several core tasks in AMR data analysis.

It includes a built-in taxonomic database of microbial species, drawing on sources such as the List of Prokaryotic names with Standing in Nomenclature (LPSN), the Global Biodiversity Information Facility (GBIF), and MycoBank, allowing users to look up and standardise microorganism names and properties.

A comprehensive data set of antimicrobial and antiviral agents is included, linked to international coding systems such as the ATC classification, EARS-Net, PubChem, LOINC, and SNOMED CT.

Clinical breakpoint guidelines from the Clinical and Laboratory Standards Institute (CLSI) and the European Committee on Antimicrobial Susceptibility Testing (EUCAST) are integrated, covering multiple years of published guidelines and including veterinary breakpoints and epidemiological cut-off values. These enable the interpretation of raw laboratory measurements, such as minimum inhibitory concentration values and disk diffusion diameters, into standardised susceptibility categories.

Additional functions support the determination of first isolates per patient, the generation of antibiograms (including WISCA), the identification of multi-drug resistant organisms, and the calculation and visualisation of resistance proportions. The package can import data in any format, including exports from the WHO's WHONET software.

All reference data sets are freely available for download in multiple formats, including Microsoft Excel, Apache Parquet, SPSS, Stata, and plain text, making them accessible to users outside the R ecosystem as well.

## Custom data types

AMR introduces several new data types (called S3 classes) to R, including `mo` (microorganism codes), `ab` (antimicrobial drug codes), `sir` (susceptibility interpretation results), `mic` (minimum inhibitory concentrations), and `disk` (disk diffusion diameters). These classes support validation, intelligent coercion, and integration with common R workflows.

## Python wrapper

A Python wrapper is also available, which runs the AMR R package natively in Python. The Python package follows the same version numbering and is built automatically alongside the R package.

## Licensing

The AMR package is licensed under the GNU General Public License v2.0 (GPL-2).
