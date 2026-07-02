---
title: "Peptide mass fingerprinting"
source: https://en.wikipedia.org/wiki/Peptide_mass_fingerprinting
domain: proteomics-bio
license: CC-BY-SA-4.0
tags: proteomics analysis, mass spectrometry proteomics, protein identification, two dimensional gel
fetched: 2026-07-02
---

# Peptide mass fingerprinting

**Peptide mass fingerprinting** (**PMF**), also known as **protein fingerprinting**, is an analytical technique for protein identification in which the unknown protein of interest is first cleaved into smaller peptides, whose absolute masses can be accurately measured with a mass spectrometer such as MALDI-TOF or ESI-TOF. The method was developed in 1993 by several groups independently. The peptide masses are compared to either a database containing known protein sequences or even the genome. This is achieved by using computer programs that translate the known genome of the organism into proteins, then theoretically cut the proteins into peptides, and calculate the absolute masses of the peptides from each protein. They then compare the masses of the peptides of the unknown protein to the theoretical peptide masses of each protein encoded in the genome. The results are statistically analyzed to find the best match.

The advantage of this method is that only the masses of the peptides have to be known. A disadvantage is that the protein sequence has to be present in the database of interest. Additionally most PMF algorithms assume that the peptides come from a single protein. The presence of a mixture can significantly complicate the analysis and potentially compromise the results. Typical for the PMF-based protein identification is the requirement for an isolated protein. Mixtures exceeding a number of 2–3 proteins typically require the additional use of MS/MS-based protein identification to achieve sufficient specificity of identification. Therefore, typical PMF samples are isolated proteins from two-dimensional gel electrophoresis (2D gels) or isolated SDS-PAGE bands. Additional analyses by MS/MS can either be direct, e.g., MALDI-TOF/TOF analysis or downstream nanoLC-ESI-MS/MS analysis of gel spot eluates.

## Origins

Due to the long, tedious process of analyzing proteins, peptide mass fingerprinting was developed. Edman degradation was used in protein analysis, and it required almost an hour to analyze one amino acid residue. SDS-PAGE was also used to separate proteins in very complex mixtures, which also employed methods of electroblotting and staining. Then, bands would be extracted from the gel and sequenced, automatically. A recurring problem in the process was that interfering proteins would also purify with the protein of interest. The sequences of these interfering proteins were compiled into what came to known as the Dayhoff database. Ultimately, having the sequences of these known protein contaminants in databases decreased instrument time and expenses involved in protein analysis.

## Sample preparation

Protein samples can be derived from SDS-PAGE or reversed phase HPLC, and are then subject to some chemical modifications. Disulfide bridges in proteins are reduced and cysteine amino acids are carbamidomethylated chemically or acrylamidated during the gel electrophoresis.

Then the proteins are cut into several fragments using proteolytic enzymes such as trypsin, chymotrypsin or Glu-C. A typical sample:protease ratio is 50:1. The proteolysis is typically carried out overnight and the resulting peptides are extracted with acetonitrile and dried under vacuum. The peptides are then dissolved in a small amount of distilled water or further concentrated and purified and are ready for mass spectrometric analysis.

## Mass spectrometric analysis

The digested protein can be analyzed with different types of mass spectrometers such as ESI-TOF or MALDI-TOF. MALDI-TOF is often the preferred instrument because it allows a high sample throughput and several proteins can be analyzed in a single experiment, if complemented by MS/MS analysis. LC/ESI-MS and CE/ESI-MS are also great techniques for peptide mass fingerprinting.

A small fraction of the peptide (usually 1 microliter or less) is pipetted onto a MALDI target and a chemical called a matrix is added to the peptide mix. Common matrices are sinapinic acid, Alpha-Cyano-4-hydroxycinnamic acid, and 2,3-Dihydroxybenzoic acid. The matrix molecules are required for the desorption of the peptide molecules. Matrix and peptide molecules co-crystallize on the MALDI target and are ready to be analyzed. There is one predominantly MALDI-MS sample preparation technique, namely dried droplet technique. The target is inserted into the vacuum chamber of the mass spectrometer and the desorption and ionisation of the polypeptide fragments is initiated by a pulsed laser beam which transfers high amounts of energy into the matrix molecules. The energy transfer is sufficient to promote the ionisation and transition of matrix molecules and peptides from the solid phase into the gas phase. The ions are accelerated in the electric field of the mass spectrometer and fly towards an ion detector where their arrival is detected as an electric signal. Their mass-to-charge ratio is proportional to their time of flight (TOF) in the drift tube and can be calculated accordingly.

Coupling ESI with capillary LC can separate peptides from protein digests, while obtaining their molecular masses at the same time. Capillary electrophoresis coupled with ESI-MS is another technique; however, it works best when analyzing small amounts of proteins.

## Computational analysis

The mass spectrometric analysis produces a list of molecular weights which is often called a peak list. The peptide masses are compared to protein databases such as Swissprot, which contain protein sequence information. Software performs *in silico* digests on proteins in the database with the same enzyme (e.g. trypsin) used in the chemical cleavage reaction. The mass of these peptides is then calculated and compared to the peak list of measured masses. The results are statistically analyzed and possible matches are returned in a results table.
