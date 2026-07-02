---
title: "Metabolic flux analysis"
source: https://en.wikipedia.org/wiki/Metabolic_flux_analysis
domain: metabolic-engineering
license: CC-BY-SA-4.0
tags: metabolic pathway engineering, flux balance, chassis strain, titer
fetched: 2026-07-02
---

# Metabolic flux analysis

**Metabolic flux analysis (MFA)** is an experimental fluxomics technique used to examine production and consumption rates of metabolites in a biological system. At an intracellular level, it allows for the quantification of metabolic fluxes, thereby elucidating the central metabolism of the cell. Various methods of MFA, including isotopically stationary metabolic flux analysis, isotopically non-stationary metabolic flux analysis, and thermodynamics-based metabolic flux analysis, can be coupled with stoichiometric models of metabolism and mass spectrometry methods with isotopic mass resolution to elucidate the transfer of moieties containing isotopic tracers from one metabolite into another and derive information about the metabolic network. Metabolic flux analysis (MFA) has many applications such as determining the limits on the ability of a biological system to produce a biochemical such as ethanol, predicting the response to gene knockout, and guiding the identification of bottleneck enzymes in metabolic networks for metabolic engineering efforts.

Metabolic flux analysis may use 13C-labeled isotope tracers for isotopic labeling experiments. Nuclear magnetic resonance (NMR) techniques and mass spectrometry may then be used to measure metabolite labeling patterns to provide information for determination of pathway fluxes. Because MFA typically requires rigorous flux calculation of complex metabolic networks, publicly available software tools have been developed to automate MFA and reduce its computational burden.

## Experimental method

Although using a stoichiometric balance and constraints of the metabolites comprising the metabolic network can elucidate fluxes, this approach has limitations including difficulty in stimulating fluxes through parallel, cyclic, and reversible pathways. Moreover, there is limited insight on how metabolites interconvert in a metabolic network without the use of isotope tracers. Thus, the use of isotopes has become the dominant technique for MFA.

### Isotope labeling experiments

Isotope labeling experiments are optimal for gathering experimental data necessary for MFA. Because fluxes determine the isotopic labeling patterns of intracellular metabolites, measuring these patterns allows for inference of fluxes. The first step in the workflow of isotope labeling experiments is cell culture on labeled substrates. A substrate such as glucose is labeled by isotope(s), most often 13C, and is introduced into the culture medium. The medium also typically contains vitamins and essential amino acids to facilitate cells' growth. The labeled substrate is then metabolized by the cells, leading to the incorporation of the 13C tracer in other intracellular metabolites. After the cells reach steady-state physiology (i.e., constant metabolite concentrations in culture), cells are then lysed to extract metabolites. For mammalian cells, extraction involves quenching of cells using methanol to stop their cellular metabolism and subsequent extraction of metabolites using methanol and water extraction. Concentrations of metabolites and labeled isotope in metabolites of the extracts are measured by instruments like liquid chromatography-mass spectrometry or NMR, which also provide information on the position and number of labeled atoms on the metabolites. These data are necessary for gaining insight into the dynamics of intracellular metabolism and metabolite turnover rates to infer metabolic flux.

## Methodologies

### Isotopically stationary

A predominant method for metabolic flux analysis is isotopically stationary MFA. This technique for flux quantitation is applicable under metabolic and isotopic steady-state, two conditions that assume that metabolite concentrations and isotopomer distributions are not changing over time, respectively. Knowledge of the stoichiometric matrix (S) comprising the consumption and production of metabolites within biochemical reactions is needed to balance fluxes (v) around the assumed metabolic network model. Assuming metabolic steady-state, metabolic fluxes can thus be quantitated by solving the inverse of the following simple linear algebra equation:

$S\times v=0$

To reduce the possible solution space for flux distributions, isotopically stationary MFA requires additional stoichiometric constraints such as growth rates, substrate secretion and uptake, and product accumulation rates as well as upper and lower bounds for fluxes. Although isotopically stationary MFA allows precise deduction of metabolic fluxes through mathematical modeling, the analysis is limited to batch cultures during the exponential phase. Moreover, after addition of a labeled substrate, the time-point for when metabolic and isotopic steady-state may be accurately assumed can be difficult to determine.

### Isotopically non-stationary

When isotope labeling is transient and has not yet equilibrated, isotopically non-stationary MFA (INST-MFA) is advantageous in deducing fluxes, particularly for systems with slow labeling dynamics. Similar to isotopically stationary MFA, this method requires mass and isotopomer balances to characterize the stoichiometry and atom transitions of the metabolic network. Unlike traditional MFA methods, however, INST-MFA requires applying ordinary differential equations to examine how isotopic labeling patterns of metabolites change over time; such examination can be accomplished by measuring changing isotopic labeling patterns over different time points to input into INST-MFA. INST-MFA is thus a powerful method for elucidating fluxes of systems with pathway bottlenecks and revealing metabolic phenotypes of autotrophic organisms. Although INST-MFA's computationally intensive demands previously hindered its widespread use, newly developed software tools have streamlined INST-MFA to decrease computational time and demand.

### Thermodynamics-based

Thermodynamics-Based Metabolic Flux Analysis (TMFA) is a specialized type of metabolic flux analysis which utilizes linear thermodynamic constraints in addition to mass balance constraints to generate thermodynamically feasible fluxes and metabolite activity profiles. TMFA takes into consideration only pathways and fluxes that are feasible by using the Gibbs free energy change of the reactions and activities of the metabolites that are part of the model. By calculating Gibbs free energies of metabolic reactions and consequently their thermodynamic favorability, TMFA facilitates identification of limiting pathway bottleneck reactions that may be ideal candidates for pathway regulation.

## Software

Simulation algorithms are needed to model the biological system and calculate the fluxes of all pathways in a complex network. Several computational software exist to meet the need for efficient and precise tools for flux quantitation. Generally, the steps for applying modeling software towards MFA include metabolic reconstruction to compile all desired enzymatic reactions and metabolites, provide experimental information such as the labeling pattern of the substrate, define constraints such as growth equations, and minimizing the error between the experimental and simulated results to obtain final fluxes. Examples of MFA software include 13CFLUX2 and OpenFLUX, which evaluate 13C labeling experiments for flux calculation under metabolic and isotopically stationary conditions. The increasing interest in developing computation tools for INST-MFA calculation has also led to the development of software applications such as INCA, which was the first software capable of performing INST-MFA and simulating transient isotope labeling experiments.

## Applications

### Biofuel production

Metabolic flux analysis has been used to guide scale-up efforts for fermentation of biofuels. By directly measuring enzymatic reaction rates, MFA can capture the dynamics of cells' behavior and metabolic phenotypes in bioreactors during large-scale fermentations. For example, MFA models were used to optimize the conversion of xylose into ethanol in xylose-fermenting yeast by using calculated flux distributions to determine maximal theoretical capacities of the selected yeast towards ethanol production.

### Metabolic engineering

Identification of bottleneck enzymes determines rate-limiting reactions that limit the productivity of a biosynthetic pathway. Moreover, MFA can help predict unexpected phenotypes of genetically engineered strains by constructing a fundamental understanding of how fluxes are wired in engineered cells. For example, by calculating the Gibbs free energies of reactions in *Escherichia coli* metabolism, TMFA facilitated identification of a thermodynamic bottleneck reaction in a genome-scale model of *Escherichia coli.*
