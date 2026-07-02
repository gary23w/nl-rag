---
title: "CASP"
source: https://en.wikipedia.org/wiki/CASP
domain: alphafold-prediction
license: CC-BY-SA-4.0
tags: protein structure prediction, deep learning fold, contact map, homology
fetched: 2026-07-02
---

# CASP

**Critical Assessment of Structure Prediction** (**CASP**), sometimes called **Critical Assessment of Protein Structure Prediction**, is a community-wide, worldwide experiment for protein structure prediction taking place every two years since 1994. CASP provides research groups with an opportunity to objectively test their structure prediction methods and delivers an independent assessment of the state of the art in protein structure modeling to the research community and software users. Even though the primary goal of CASP is to help advance the methods of identifying protein three-dimensional structure from its amino acid sequence many view the experiment more as a "world championship" in this field of science. More than 100 research groups from all over the world participate in CASP on a regular basis and it is not uncommon for entire groups to suspend their other research for months while they focus on getting their servers ready for the experiment and on performing the detailed predictions.

## Selection of target proteins

In order to ensure that no predictor can have prior information about a protein's structure that would put them at an advantage, it is important that the experiment be conducted in a double-blind fashion: Neither predictors nor the organizers and assessors know the structures of the target proteins at the time when predictions are made. Targets for structure prediction are either structures soon-to-be solved by X-ray crystallography or NMR spectroscopy, or structures that have just been solved (mainly by one of the structural genomics centers) and are kept on hold by the Protein Data Bank. If the given sequence is found to be related by common descent to a protein sequence of known structure (called a template), comparative protein modeling may be used to predict the tertiary structure. Templates can be found using sequence alignment methods (e.g. BLAST or HHsearch) or protein threading methods, which are better in finding distantly related templates. Otherwise, *de novo* protein structure prediction must be applied (e.g. Rosetta), which is much less reliable but can sometimes yield models with the correct fold (usually, for proteins less than 100-150 amino acids). Truly new folds are becoming quite rare among the targets, making that category smaller than desirable.

## Evaluation

The primary method of evaluation is a comparison of the predicted model α-carbon positions with those in the target structure. The comparison is shown visually by cumulative plots of distances between pairs of equivalents α-carbon in the alignment of the model and the structure, such as shown in the figure (a perfect model would stay at zero all the way across), and is assigned a numerical score GDT-TS (Global Distance Test—Total Score) describing percentage of well-modeled residues in the model with respect to the target. Free modeling (template-free, or *de novo*) is also evaluated visually by the assessors, since the numerical scores do not work as well for finding loose resemblances in the most difficult cases. High-accuracy template-based predictions were evaluated in CASP7 by whether they worked for molecular-replacement phasing of the target crystal structure with successes followed up later, and by full-model (not just α-carbon) model quality and full-model match to the target in CASP8.

Evaluation of the results is carried out in the following prediction categories:

- tertiary structure prediction (all CASPs)
- secondary structure prediction (dropped after CASP5)
- prediction of structure complexes (CASP2 only; a separate experiment—CAPRI—carries on this subject)
- residue-residue contact prediction (starting CASP4)
- disordered regions prediction (starting CASP5)
- domain boundary prediction (CASP6–CASP8)
- function prediction (starting CASP6)
- model quality assessment (starting CASP7)
- model refinement (starting CASP7)
- high-accuracy template-based prediction (starting CASP7)

Tertiary structure prediction category was further subdivided into:

- homology modeling
- fold recognition (also called protein threading; note that this naming is incorrect as threading is a method)
- *de novo* structure prediction, now referred to as 'New Fold' as many methods apply evaluation, or scoring, functions that are biased by knowledge of native protein structures, such as an artificial neural network.

Starting with CASP7, categories have been redefined to reflect developments in methods. The 'Template based modeling' category includes all former comparative modeling, homologous fold based models and some analogous fold based models. The 'template free modeling (FM)' category includes models of proteins with previously unseen folds and hard analogous fold based models. Due to limited numbers of template free targets (they are quite rare), in 2011 so called CASP ROLL was introduced. This continuous (rolling) CASP experiment aims at more rigorous evaluation of template free prediction methods through assessment of a larger number of targets outside of the regular CASP prediction season. Unlike LiveBench and EVA, this experiment is in the blind-prediction spirit of CASP, i.e. all the predictions are made on yet unknown structures.

The CASP results are published in special supplement issues of the scientific journal *Proteins*, all of which are accessible through the CASP website. A lead article in each of these supplements describes specifics of the experiment while a closing article evaluates progress in the field.

## AlphaFold

In December 2018, CASP13 made headlines when it was won by AlphaFold, an artificial intelligence program created by DeepMind. In November 2020, an improved version 2 of AlphaFold won CASP14. According to one of CASP co-founders John Moult, AlphaFold scored around 90 on a 100-point scale of prediction accuracy for moderately difficult protein targets. AlphaFold was made open source in 2021, and in CASP15 in 2022, while DeepMind did not enter, virtually all of the high-ranking teams used AlphaFold or modifications of AlphaFold.

## NIH funding cancellation

Until 2025, funding for the competition was provided by a grant from the National Institutes of Health. However, the NIH did not renew funding for the program in 2025, due to budget cuts made by the Trump administration. The competition was on the verge of closing down before Google DeepMind stepped in to provide interim funding.
