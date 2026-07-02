---
title: "Molecular descriptor"
source: https://en.wikipedia.org/wiki/Molecular_descriptor
domain: cheminformatics-rdkit
license: CC-BY-SA-4.0
tags: cheminformatics rdkit, molecular descriptor, smiles notation, chemical fingerprint
fetched: 2026-07-02
---

# Molecular descriptor

**Molecular descriptors** play a fundamental role in chemistry, pharmaceutical sciences, environmental protection policy, and health researches, as well as in quality control, being the way molecules, thought of as real bodies, are transformed into numbers, allowing some mathematical treatment of the chemical information contained in the molecule. This was defined by Todeschini and Consonni as:

"*The molecular descriptor is the final result of a logic and mathematical procedure which transforms chemical information encoded within a symbolic representation of a molecule into a useful number or the result of some standardized experiment.*"

By this definition, the molecular descriptors are divided into two main categories: **experimental measurements**, such as log P, molar refractivity, dipole moment, polarizability, and, in general, additive physico-chemical properties, and **theoretical molecular descriptors**, which are derived from a symbolic representation of the molecule and can be further classified according to the different types of molecular representation.

The main classes of theoretical molecular descriptors are: 1) **0D-descriptors** (i.e. constitutional descriptors, count descriptors), 2) **1D-descriptors** (i.e. list of structural fragments, fingerprints),3) **2D-descriptors** (i.e. graph invariants),4) **3D-descriptors** (such as, for example, 3D-MoRSE descriptors, WHIM descriptors, GETAWAY descriptors, quantum-chemical descriptors, size, steric, surface and volume descriptors),5) **4D-descriptors** (such as those derived from GRID or CoMFA methods, Volsurf). The outspread of artificial intelligence and machine learning to computational chemistry has also lead to various attempts to uncover new descriptors or to find the most predictive ones among some sort of candidates.

## Invariance properties of molecular descriptors

The invariance properties of molecular descriptors can be defined as the ability of the algorithm for their calculation to give a descriptor value that is independent of the particular characteristics of the molecular representation, such as atom numbering or labeling, spatial reference frame, molecular conformations, etc. Invariance to molecular numbering or labeling is assumed as a minimal basic requirement for any descriptor.

Two other important invariance properties, translational invariance and rotational invariance, are the invariance of a descriptor value to any translation or rotation of the molecules in the chosen reference frame. These last invariance properties are required for the 3D-descriptors.

## Degeneracy of molecular descriptors

This property refers to the ability of a descriptor to avoid equal values for different molecules. In this sense, descriptors can show no degeneracy at all, low, intermediate, or high degeneracy. For example, the number of molecule atoms and the molecular weights are high degeneracy descriptors, while, usually, 3D-descriptors show low or no degeneracy at all.

## Criteria for Molecular Descriptors

Molecular descriptors are numerical values that encapsulate chemical information about molecules, facilitating their mathematical analysis. Given the vast array of available descriptors, it's essential to establish foundational principles to ensure their reliability and utility. A robust molecular descriptor should:

1. Be invariant to atom labeling and numbering
2. Be invariant to the molecule roto-translation
3. Be defined by an unambiguous algorithm
4. Have a well-defined applicability on molecular structures

Beyond these foundational criteria, to be practically valuable, a molecular descriptor should also:

1. Should have structural interpretation
2. Should have a good correlation with at least one experimental property
3. Should not have trivial relation with other molecular descriptors
4. Should not be based on experimental properties 9. Should preferably be continuous
5. Should preferably show minimal degeneracy
6. Should preferably be simple
7. Should preferably be applicable to a broad class of molecules
8. Should preferably be able to discriminate among isomers
9. Should preferably have calculated values in a suitable numerical range for the set of molecules where it is applicable to

The initial set of principles ensures that a descriptor is well-defined and invariant to manipulations that don't alter the intrinsic molecular structure. Historically, many descriptors were designed for small organic molecules. However, contemporary challenges necessitate descriptors that can be applied to diverse compounds, including salts, ionic liquids, peptides, polymers, and nanostructures.

The subsequent set of guidelines emphasizes the descriptor's practical utility. An effective descriptor should be interpretable, correlate with experimental properties, and provide unique information not captured by other descriptors. Continuity and low degeneracy are crucial, as they ensure the descriptor can sensitively reflect minor structural variations. Ultimately, the information a descriptor provides is contingent upon the chosen molecular representation and its alignment with the specific property or activity being studied.

## Software for molecular descriptors calculation

Here there is a list of a selection of commercial and free descriptor calculation tools.

Name

0D descriptors

Fingerprints

3D descriptors

Python library

CLI

GUI

KNIME

Comments

License

Website

alvaDesc

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Available for

Windows

,

Linux

and

macOS

. Last update 2025.

Proprietary

,

commercial

https://www.alvascience.com/alvadesc/

Dragon

Yes

Yes

Yes

No

Yes

Yes

Yes

Discontinued.

Proprietary

,

commercial

https://chm.kode-solutions.net/products_dragon.php

Mordred

Yes

No

Yes

Yes

Yes

No

No

Based on

RDKit

. Official version discontinued (last update 2019), but has a community-maintained fork.

Free

open source

https://github.com/mordred-descriptor/mordred

,

https://github.com/JacksonBurns/mordred-community

PaDEL-descriptor

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Based on

CDK

. Discontinued (last update 2014).

Free

http://www.yapcwsoft.com/dd/padeldescriptor/

RDKit

Yes

Yes

Yes

Yes

No

No

Yes

Last update 2024

Free

open source

https://github.com/rdkit/rdkit

scikit-fingerprints

Yes

Yes

Yes

Yes

No

No

No

Last update 2025

Free

open source

https://github.com/scikit-fingerprints/scikit-fingerprints
