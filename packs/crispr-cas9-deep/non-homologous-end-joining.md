---
title: "Non-homologous end joining"
source: https://en.wikipedia.org/wiki/Non-homologous_end_joining
domain: crispr-cas9-deep
license: CC-BY-SA-4.0
tags: cas9 nuclease, guide rna, protospacer adjacent, double strand break
fetched: 2026-07-02
---

# Non-homologous end joining

**Non-homologous end joining** (**NHEJ**) is a pathway that repairs double-strand breaks in DNA. It is called "non-homologous" because the break ends are directly ligated without the need for a homologous template, in contrast to homology directed repair (HDR), which requires a homologous sequence to guide repair. NHEJ is active in both non-dividing and proliferating cells, while HDR is not readily accessible in non-dividing cells. The term "non-homologous end joining" was coined in 1996 by Moore and Haber.

NHEJ is typically guided by short homologous DNA sequences called microhomologies. These microhomologies are often present in single-stranded overhangs on the ends of double-strand breaks. When the overhangs are perfectly compatible, NHEJ usually repairs the break accurately. Imprecise repair leading to loss of nucleotides can also occur, but is much more common when the overhangs are not compatible. Inappropriate NHEJ can lead to translocations and telomere fusion, hallmarks of tumor cells.

NHEJ implementations are understood to have been existent throughout nearly all biological systems and it is the predominant double-strand break repair pathway in mammalian cells. In budding yeast (*Saccharomyces cerevisiae*), however, homologous recombination dominates when the organism is grown under common laboratory conditions.

When the NHEJ pathway is inactivated, double-strand breaks can be repaired by a more error-prone pathway called microhomology-mediated end joining (MMEJ). In this pathway, end resection reveals short microhomologies on either side of the break, which are then aligned to guide repair. This contrasts with classical NHEJ, which typically uses microhomologies already exposed in single-stranded overhangs on the DSB ends. Repair by MMEJ therefore leads to deletion of the DNA sequence between the microhomologies.

## In bacteria and archaea

Many species of bacteria, including *Escherichia coli*, lack an end joining pathway and thus rely completely on homologous recombination to repair double-strand breaks. NHEJ proteins have been identified in a number of bacteria, including *Bacillus subtilis*, *Mycobacterium tuberculosis*, and *Mycobacterium smegmatis*. Bacteria utilize a remarkably compact version of NHEJ in which all of the required activities are contained in only two proteins: a Ku homodimer and the multifunctional ligase/polymerase/nuclease LigD. In mycobacteria, NHEJ is much more error prone than in yeast, with bases often added to and deleted from the ends of double-strand breaks during repair. Many of the bacteria that possess NHEJ proteins spend a significant portion of their life cycle in a stationary haploid phase, in which a template for recombination is not available. NHEJ may have evolved to help these organisms survive DSBs induced during desiccation. It preferentially uses rNTPs (RNA nucleotides), possibly advantageous in dormant cells.

The archaeal NHEJ system in *Methanocella paludicola* have a homodimeric Ku, but the three functions of LigD are broken up into three single-domain proteins sharing an operon. All three genes retain substantial homology with their LigD counterparts and the polymerase retains the preference for rNTP. NHEJ has been lost and acquired multiple times in bacteria and archaea, with a significant amount of horizontal gene transfer shuffling the system around taxa.

Corndog and Omega, two related mycobacteriophages of *Mycobacterium smegmatis*, also encode Ku homologs and exploit the NHEJ pathway to recircularize their genomes during infection. Unlike homologous recombination, which has been studied extensively in bacteria, NHEJ was originally discovered in eukaryotes and was only identified in prokaryotes in the past decade.

## In eukaryotes

In contrast to bacteria, NHEJ in eukaryotes utilizes a number of proteins, which participate in the following steps:

### End binding and tethering

In yeast, the Mre11-Rad50-Xrs2 (MRX) complex is recruited to DSBs early and is thought to promote bridging of the DNA ends. The corresponding mammalian complex of Mre11-Rad50-Nbs1 (MRN) is also involved in NHEJ, but it may function at multiple steps in the pathway beyond simply holding the ends in proximity. DNA-PKcs is also thought to participate in end bridging during mammalian NHEJ.

Eukaryotic Ku is a heterodimer consisting of Ku70 and Ku80, and forms a complex with DNA-PKcs, which is present in mammals but absent in yeast. Ku is a basket-shaped molecule that slides onto the DNA end and translocates inward. Ku may function as a docking site for other NHEJ proteins, and is known to interact with the DNA ligase IV complex and XLF.

### End processing

End processing involves removal of damaged or mismatched nucleotides by nucleases and resynthesis by DNA polymerases. This step is not necessary if the ends are already compatible and have 3' hydroxyl and 5' phosphate termini.

Little is known about the function of nucleases in NHEJ. Artemis is required for opening the hairpins that are formed on DNA ends during V(D)J recombination, a specific type of NHEJ, and may also participate in end trimming during general NHEJ. Mre11 has nuclease activity, but it seems to be involved in homologous recombination, not NHEJ.

The X family DNA polymerases Pol λ and Pol μ (Pol4 in yeast) fill gaps during NHEJ. Yeast lacking Pol4 are unable to join 3' overhangs that require gap filling, but remain proficient for gap filling at 5' overhangs. This is because the primer terminus used to initiate DNA synthesis is less stable at 3' overhangs, necessitating a specialized NHEJ polymerase.

### Ligation

The DNA ligase IV complex, consisting of the catalytic subunit DNA ligase IV and its cofactor XRCC4 (Dnl4 and Lif1 in yeast), performs the ligation step of repair. XLF, also known as Cernunnos, is homologous to yeast Nej1 and is also required for NHEJ. While the precise role of XLF is unknown, it interacts with the XRCC4/DNA ligase IV complex and likely participates in the ligation step. Recent evidence suggests that XLF promotes re-adenylation of DNA ligase IV after ligation, recharging the ligase and allowing it to catalyze a second ligation.

### Other

In yeast, Sir2 was originally identified as an NHEJ protein, but is now known to be required for NHEJ only because it is required for the transcription of Nej1.

**NHEJ and heat-labile sites**

Induction of heat-labile sites (HLS) is a signature of ionizing radiation. The DNA clustered damage sites consist of different types of DNA lesions. Some of these lesions are not prompt DSBs but they convert to DSB after heating. HLS are not evolved to DSB under physiological temperature (37 C). Also, the interaction of HLS with other lesions and their role in living cells is yet elusive. The repair mechanisms of these sites are not fully revealed. The NHEJ is the dominant DNA repair pathway throughout the cell cycle. The DNA-PKcs protein is the critical element in the center of NHEJ. Using DNA-PKcs KO cell lines or inhibition of DNA-PKcs does not affect the repair capacity of HLS. Also blocking both HR and NHEJ repair pathways by dactolisib (NVP-BEZ235) inhibitor showed that repair of HLS is not dependent on HR and NHEJ. These results showed that the repair mechanism of HLS is independent of NHEJ and HR pathways

## Regulation

The choice between NHEJ and homologous recombination for repair of a double-strand break is regulated at the initial step in recombination, 5' end resection. In this step, the 5' strand of the break is degraded by nucleases to create long 3' single-stranded tails. DSBs that have not been resected can be rejoined by NHEJ, but resection of even a few nucleotides strongly inhibits NHEJ and effectively commits the break to repair by recombination. NHEJ is active throughout the cell cycle, but is most important during G1 when no homologous template for recombination is available. This regulation is accomplished by the cyclin-dependent kinase Cdk1 (Cdc28 in yeast), which is turned off in G1 and expressed in S and G2. Cdk1 phosphorylates the nuclease Sae2, allowing resection to initiate.

## V(D)J recombination

NHEJ plays a critical role in V(D)J recombination, the process by which B-cell and T-cell receptor diversity is generated in the vertebrate immune system. In V(D)J recombination, hairpin-capped double-strand breaks are created by the RAG1/RAG2 nuclease, which cleaves the DNA at recombination signal sequences. These hairpins are then opened by the Artemis nuclease and joined by NHEJ. A specialized DNA polymerase called terminal deoxynucleotidyl transferase (TdT), which is only expressed in lymph tissue, adds nontemplated nucleotides to the ends before the break is joined. This process couples "variable" (V), "diversity" (D), and "joining" (J) regions, which when assembled together create the variable region of a B-cell or T-cell receptor gene. Unlike typical cellular NHEJ, in which accurate repair is the most favorable outcome, error-prone repair in V(D)J recombination is beneficial in that it maximizes diversity in the coding sequence of these genes. Patients with mutations in NHEJ genes are unable to produce functional B cells and T cells and suffer from severe combined immunodeficiency (SCID).

## At telomeres

Telomeres are normally protected by a "cap" that prevents them from being recognized as double-strand breaks. Loss of capping proteins causes telomere shortening and inappropriate joining by NHEJ, producing dicentric chromosomes which are then pulled apart during mitosis. Paradoxically, some NHEJ proteins are involved in telomere capping. For example, Ku localizes to telomeres and its deletion leads to shortened telomeres. Ku is also required for subtelomeric silencing, the process by which genes located near telomeres are turned off.

## Consequences of dysfunction

Several human syndromes are associated with dysfunctional NHEJ. Hypomorphic mutations in LIG4 and XLF cause LIG4 syndrome and XLF-SCID, respectively. These syndromes share many features including cellular radiosensitivity, microcephaly and severe combined immunodeficiency (SCID) due to defective V(D)J recombination. Loss-of-function mutations in Artemis also cause SCID, but these patients do not show the neurological defects associated with LIG4 or XLF mutations. The difference in severity may be explained by the roles of the mutated proteins. Artemis is a nuclease and is thought to be required only for repair of DSBs with damaged ends, whereas DNA Ligase IV and XLF are required for all NHEJ events. Mutations in genes that participate in non-homologous end joining lead to ataxia-telangiectasia (ATM gene), Fanconi anemia (multiple genes), as well as hereditary breast and ovarian cancers (BRCA1 gene).

Many NHEJ genes have been knocked out in mice. Deletion of XRCC4 or LIG4 causes embryonic lethality in mice, indicating that NHEJ is essential for viability in mammals. In contrast, mice lacking Ku or DNA-PKcs are viable, probably because low levels of end joining can still occur in the absence of these components. All NHEJ mutant mice show a SCID phenotype, sensitivity to ionizing radiation, and neuronal apoptosis.

## Aging

A system was developed for measuring NHEJ efficiency in the mouse. NHEJ efficiency could be compared across tissues of the same mouse and in mice of different age. Efficiency was higher in the skin, lung and kidney fibroblasts, and lower in heart fibroblasts and brain astrocytes. Furthermore, NHEJ efficiency declined with age. The decline was 1.8 to 3.8-fold, depending on the tissue, in the 5-month-old compared to the 24-month-old mice. Reduced capability for NHEJ can lead to an increase in the number of unrepaired or faultily repaired DNA double-strand breaks that may then contribute to aging. An analysis of the level of NHEJ protein Ku80 in human, cow, and mouse indicated that Ku80 levels vary dramatically between species, and that these levels are strongly correlated with species longevity.

## List of proteins involved in NHEJ in human cells

- Ku70/80
- DNA-PKcs
- DNA Ligase IV
- XRCC4
- XLF
- Artemis
- DNA polymerase mu
- DNA polymerase lambda
- PNKP
- Aprataxin
- APLF
- BRCA1
- BRCA2
- CYREN
