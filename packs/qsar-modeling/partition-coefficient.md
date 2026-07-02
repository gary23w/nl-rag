---
title: "Partition coefficient"
source: https://en.wikipedia.org/wiki/Partition_coefficient
domain: qsar-modeling
license: CC-BY-SA-4.0
tags: quantitative structure activity, molecular descriptor, regression, activity cliff
fetched: 2026-07-02
---

# Partition coefficient

In the physical sciences, a **partition coefficient** (***P***) or **distribution coefficient** (***D***) is the ratio of concentrations of a compound in a mixture of two immiscible solvents at equilibrium. This ratio is therefore a comparison of the solubilities of the solute in these two liquids. The partition coefficient generally refers to the concentration ratio of un-ionized species of compound, whereas the distribution coefficient refers to the concentration ratio of all species of the compound (ionized plus un-ionized).

In the chemical and pharmaceutical sciences, both phases usually are solvents. Most commonly, one of the solvents is water, while the second is hydrophobic, such as 1-octanol. Hence the partition coefficient measures how hydrophilic ("water-loving") or hydrophobic ("water-fearing") a chemical substance is. Partition coefficients are useful in estimating the distribution of drugs within the body. Hydrophobic drugs with high octanol-water partition coefficients are mainly distributed to hydrophobic areas such as lipid bilayers of cells. Conversely, hydrophilic drugs (low octanol/water partition coefficients) are found primarily in aqueous regions such as blood serum.

If one of the solvents is a gas and the other a liquid, a gas/liquid partition coefficient can be determined. For example, the blood/gas partition coefficient of a general anesthetic measures how easily the anesthetic passes from gas to blood. Partition coefficients can also be defined when one of the phases is solid, for instance, when one phase is a molten metal and the second is a solid metal, or when both phases are solids. The partitioning of a substance into a solid results in a solid solution.

Partition coefficients can be measured experimentally in various ways (by shake-flask, HPLC, etc.) or estimated by calculation based on a variety of methods (fragment-based, atom-based, etc.).

If a substance is present as several chemical species in the partition system due to association or dissociation, each species is assigned its own *K*ow value. A related value, D, does not distinguish between different species, only indicating the concentration ratio of the substance between the two phases.

## Nomenclature

Despite formal recommendation to the contrary, the term *partition coefficient* remains the predominantly used term in the scientific literature.

In contrast, the IUPAC recommends that the title term no longer be used, rather, that it be replaced with more specific terms. For example, *partition constant*, defined as

| (*K*D)A = ⁠[A]org/ [A]aq⁠, |   | 1 |
|---|---|---|

where *K*D is the process equilibrium constant, [A] represents the concentration of solute A being tested, and "org" and "aq" refer to the organic and aqueous phases respectively. The IUPAC further recommends "partition ratio" for cases where transfer activity coefficients can be determined, and "distribution ratio" for the ratio of total analytical concentrations of a solute between phases, regardless of chemical form.

## Partition coefficient and log *P*

The **partition coefficient**, abbreviated ***P***, is defined as a particular ratio of the concentrations of a solute between the two solvents (a biphase of liquid phases), specifically for un-ionized solutes, and the logarithm of the ratio is thus **log *P***. When one of the solvents is water and the other is a non-polar solvent, then the log *P* value is a measure of lipophilicity or hydrophobicity. The defined precedent is for the lipophilic and hydrophilic phase types to always be in the numerator and denominator respectively; for example, in a biphasic system of *n*-octanol (hereafter simply "octanol") and water:

$\log P_{\text{oct/wat}}=\log _{10}\left({\frac {{\big [}{\text{solute}}{\big ]}_{\text{octanol}}^{\text{un-ionized}}}{{\big [}{\text{solute}}{\big ]}_{\text{water}}^{\text{un-ionized}}}}\right).$

To a first approximation, the non-polar phase in such experiments is usually dominated by the un-ionized form of the solute, which is electrically neutral, though this may not be true for the aqueous phase. To measure the *partition coefficient of ionizable solutes*, the pH of the aqueous phase is adjusted such that the predominant form of the compound in solution is the un-ionized, or its measurement at another pH of interest requires consideration of all species, un-ionized and ionized (see following).

A corresponding **partition coefficient** for ionizable compounds, abbreviated **log *P* *I***, is derived for cases where there are dominant ionized forms of the molecule, such that one must consider partition of all forms, ionized and un-ionized, between the two phases (as well as the interaction of the two equilibria, partition and ionization). *M* is used to indicate the number of ionized forms; for the I-th form (*I* = 1, 2, ... , *M*) the logarithm of the corresponding partition coefficient, $\log P_{\text{oct/wat}}^{I}$ , is defined in the same manner as for the un-ionized form. For instance, for an octanol–water partition, it is

$\log \ P_{\text{oct/wat}}^{\mathrm {I} }=\log _{10}\left({\frac {{\big [}{\text{solute}}{\big ]}_{\text{octanol}}^{I}}{{\big [}{\text{solute}}{\big ]}_{\text{water}}^{I}}}\right).$

To distinguish between this and the standard, un-ionized, partition coefficient, the un-ionized is often assigned the symbol **log *P*0**, such that the indexed $\log P_{\text{oct/wat}}^{I}$ expression for ionized solutes becomes simply an extension of this, into the range of values *I* > 0.

## Distribution coefficient and log *D*

The **distribution coefficient**, **log *D***, is the ratio of the sum of the concentrations of all forms of the compound (ionized plus un-ionized) in each of the two phases, one essentially always aqueous; as such, it depends on the pH of the aqueous phase, and log *D* = log *P* for non-ionizable compounds at any pH. For measurements of distribution coefficients, the pH of the aqueous phase is buffered to a specific value such that the pH is not significantly perturbed by the introduction of the compound. The value of each **log *D*** is then determined as the logarithm of a ratio—of the sum of the experimentally measured concentrations of the solute's various forms in one solvent, to the sum of such concentrations of its forms in the other solvent; it can be expressed as

$\log D_{\text{oct/wat}}=\log _{10}\left({\frac {{\big [}{\text{solute}}{\big ]}_{\text{octanol}}^{\text{ionized}}+{\big [}{\text{solute}}{\big ]}_{\text{octanol}}^{\text{un-ionized}}}{{\big [}{\text{solute}}{\big ]}_{\text{water}}^{\text{ionized}}+{\big [}{\text{solute}}{\big ]}_{\text{water}}^{\text{un-ionized}}}}\right).$

In the above formula, the superscripts "ionized" each indicate the sum of concentrations of all ionized species in their respective phases. In addition, since log *D* is pH-dependent, the pH at which the log *D* was measured must be specified. In areas such as drug discovery—areas involving partition phenomena in biological systems such as the human body—the log *D* at the physiologic pH = 7.4 is of particular interest.

It is often convenient to express the log *D* in terms of *P*I, defined above (which includes *P*0 as state *I* = 0), thus covering both un-ionized and ionized species. For example, in octanol–water:

$\log D_{\text{oct/wat}}=\log _{10}\left(\sum _{I=0}^{M}f^{I}P_{\text{oct/wat}}^{I}\right),$

which sums the individual partition coefficients (not their logarithms), and where $f^{I}$ indicates the pH-dependent mole fraction of the I-th form (of the solute) in the aqueous phase, and other variables are defined as previously.

## Example partition coefficient data

The values for the octanol-water system in the following table are from the Dortmund Data Bank. They are sorted by the partition coefficient, smallest to largest (acetamide being hydrophilic, and 2,2',4,4',5-pentachlorobiphenyl lipophilic), and are presented with the temperature at which they were measured (which impacts the values).

| Component | log *P*OW | *T* (°C) |
|---|---|---|
| Acetamide | −1.16 | 25 |
| Methanol | −0.81 | 19 |
| Formic acid | −0.41 | 25 |
| Diethyl ether | 0.83 | 20 |
| p-Dichlorobenzene | 3.37 | 25 |
| Hexamethylbenzene | 4.61 | 25 |
| 2,2',4,4',5-Pentachlorobiphenyl | 6.41 | Ambient |

Values for other compounds may be found in a variety of available reviews and monographs. Critical discussions of the challenges of measurement of log *P* and related computation of its estimated values (see below) appear in several reviews.

## Applications

### Pharmacology

A drug's distribution coefficient strongly affects how easily the drug can reach its intended target in the body, how strong an effect it will have once it reaches its target, and how long it will remain in the body in an active form. Hence, the log *P* of a molecule is one criterion used in decision-making by medicinal chemists in pre-clinical drug discovery, for example, in the assessment of druglikeness of drug candidates. Likewise, it is used to calculate lipophilic efficiency in evaluating the quality of research compounds, where the efficiency for a compound is defined as its potency, via measured values of pIC50 or pEC50, minus its value of log *P*.

#### Pharmacokinetics

In the context of pharmacokinetics (how the body absorbs, metabolizes, and excretes a drug), the distribution coefficient has a strong influence on ADME properties of the drug. Hence the hydrophobicity of a compound (as measured by its distribution coefficient) is a major determinant of how drug-like it is. More specifically, for a drug to be orally absorbed, it normally must first pass through lipid bilayers in the intestinal epithelium (a process known as transcellular transport). For efficient transport, the drug must be hydrophobic enough to partition into the lipid bilayer, but not so hydrophobic, that once it is in the bilayer, it will not partition out again. Likewise, hydrophobicity plays a major role in determining where drugs are distributed within the body after absorption and, as a consequence, in how rapidly they are metabolized and excreted.

#### Pharmacodynamics

In the context of pharmacodynamics (how the drug affects the body), the hydrophobic effect is the major driving force for the binding of drugs to their receptor targets. On the other hand, hydrophobic drugs tend to be more toxic because they, in general, are retained longer, have a wider distribution within the body (e.g., intracellular), are somewhat less selective in their binding to proteins, and finally are often extensively metabolized. In some cases the metabolites may be chemically reactive. Hence it is advisable to make the drug as hydrophilic as possible while it still retains adequate binding affinity to the therapeutic protein target. For cases where a drug reaches its target locations through passive mechanisms (i.e., diffusion through membranes), the ideal distribution coefficient for the drug is typically intermediate in value (neither too lipophilic, nor too hydrophilic); in cases where molecules reach their targets otherwise, no such generalization applies.

### Environmental science

The hydrophobicity of a compound can give scientists an indication of how easily a compound might be taken up in groundwater to pollute waterways, and its toxicity to animals and aquatic life. Partition coefficient can also be used to predict the mobility of radionuclides in groundwater. In the field of hydrogeology, the octanol–water partition coefficient *K*ow is used to predict and model the migration of dissolved hydrophobic organic compounds in soil and groundwater.

### Agrochemical research

Hydrophobic insecticides and herbicides tend to be more active. Hydrophobic agrochemicals in general have longer half-lives and therefore display increased risk of adverse environmental impact.

### Metallurgy

In metallurgy, the partition coefficient is an important factor in determining how different impurities are distributed between molten and solidified metal. It is a critical parameter for purification using zone melting, and determines how effectively an impurity can be removed using directional solidification, described by the Scheil equation.

### Consumer product development

Many other industries take into account distribution coefficients, for example in the formulation of make-up, topical ointments, dyes, hair colors and many other consumer products.

## Measurement

A number of methods of measuring distribution coefficients have been developed, including the shake-flask, separating funnel method, reverse-phase HPLC, and pH-metric techniques.

### Separating-funnel method

In this method the solid particles present into the two immiscible liquids can be easily separated by suspending those solid particles directly into these immiscible or somewhat miscible liquids.

### Shake flask-type

The classical and most reliable method of log *P* determination is the *shake-flask method*, which consists of dissolving some of the solute in question in a volume of octanol and water, then measuring the concentration of the solute in each solvent. The most common method of measuring the distribution of the solute is by UV/VIS spectroscopy.

### HPLC-based

A faster method of log *P* determination makes use of high-performance liquid chromatography. The log *P* of a solute can be determined by correlating its retention time with similar compounds with known log *P* values.

An advantage of this method is that it is fast (5–20 minutes per sample). However, since the value of log *P* is determined by linear regression, several compounds with similar structures must have known log *P* values, and extrapolation from one chemical class to another—applying a regression equation derived from one chemical class to a second one—may not be reliable, since each chemical classes will have its characteristic regression parameters.

### pH-metric

The pH-metric set of techniques determine lipophilicity pH profiles directly from a single acid-base titration in a two-phase water–organic-solvent system. Hence, a single experiment can be used to measure the logarithms of the partition coefficient (log *P*) giving the distribution of molecules that are primarily neutral in charge, as well as the distribution coefficient (log *D*) of all forms of the molecule over a pH range, e.g., between 2 and 12. The method does, however, require the separate determination of the pKa value(s) of the substance.

### Electrochemical

Polarized liquid interfaces have been used to examine the thermodynamics and kinetics of the transfer of charged species from one phase to another. Two main methods exist. The first is ITIES, "interfaces between two immiscible electrolyte solutions". The second is droplet experiments. Here a reaction at a triple interface between a conductive solid, droplets of a redox active liquid phase and an electrolyte solution have been used to determine the energy required to transfer a charged species across the interface.

### Single-cell approach

There are attempts to provide partition coefficients for drugs at a single-cell level. This strategy requires methods for the determination of concentrations in individual cells, i.e., with Fluorescence correlation spectroscopy or quantitative Image analysis. Partition coefficient at a single-cell level provides information on cellular uptake mechanism.

## Prediction

There are many situations where prediction of partition coefficients prior to experimental measurement is useful. For example, tens of thousands of industrially manufactured chemicals are in common use, but only a small fraction have undergone rigorous toxicological evaluation. Hence there is a need to prioritize the remainder for testing. QSAR equations, which in turn are based on calculated partition coefficients, can be used to provide toxicity estimates. Calculated partition coefficients are also widely used in drug discovery to optimize screening libraries and to predict druglikeness of designed drug candidates before they are synthesized. As discussed in more detail below, estimates of partition coefficients can be made using a variety of methods, including fragment-based, atom-based, and knowledge-based that rely solely on knowledge of the structure of the chemical. Other prediction methods rely on other experimental measurements such as solubility. The methods also differ in accuracy and whether they can be applied to all molecules, or only ones similar to molecules already studied.

### Atom-based

Standard approaches of this type, using atomic contributions, have been named by those formulating them with a prefix letter: AlogP, XlogP, MlogP, etc. A conventional method for predicting log *P* through this type of method is to parameterize the distribution coefficient contributions of various atoms to the overall molecular partition coefficient, which produces a parametric model. This parametric model can be estimated using constrained least-squares estimation, using a training set of compounds with experimentally measured partition coefficients.

In order to get reasonable correlations, the most common elements contained in drugs (hydrogen, carbon, oxygen, sulfur, nitrogen, and halogens) are divided into several different atom types depending on the environment of the atom within the molecule. While this method is generally the least accurate, the advantage is that it is the most general, being able to provide at least a rough estimate for a wide variety of molecules.

### Fragment-based

The most common of these uses a group contribution method and is termed cLogP. It has been shown that the log *P* of a compound can be determined by the sum of its non-overlapping molecular fragments (defined as one or more atoms covalently bound to each other within the molecule). Fragmentary log *P* values have been determined in a statistical method analogous to the atomic methods (least-squares fitting to a training set). In addition, Hammett-type corrections are included to account of electronic and steric effects. This method in general gives better results than atomic-based methods, but cannot be used to predict partition coefficients for molecules containing unusual functional groups for which the method has not yet been parameterized (most likely because of the lack of experimental data for molecules containing such functional groups).

### Knowledge-based

A typical data-mining-based prediction uses support-vector machines, decision trees, or neural networks. This method is usually very successful for calculating log *P* values when used with compounds that have similar chemical structures and known log *P* values. Molecule mining approaches apply a similarity-matrix-based prediction or an automatic fragmentation scheme into molecular substructures. Furthermore, there exist also approaches using maximum common subgraph searches or molecule kernels.

### Log *D* from log *P* and p*K*a

For cases where the molecule is un-ionized:

$\log D\cong \log P.$

For other cases, estimation of log *D* at a given pH, from log *P* and the known mole fraction of the un-ionized form, $f^{0}$ , in the case where partition of ionized forms into non-polar phase can be neglected, can be formulated as

$\log D\cong \log P+\log \left(f^{0}\right).$

The following approximate expressions are valid only for monoprotic acids and bases:

${\begin{aligned}\log D_{\text{acids}}&\cong \log P+\log \left[{\frac {1}{1+10^{\mathrm {p} H-\mathrm {p} K_{a}}}}\right],\\\log D_{\text{bases}}&\cong \log P+\log \left[{\frac {1}{1+10^{\mathrm {p} K_{a}-\mathrm {pH} }}}\right].\end{aligned}}$

Further approximations for when the compound is largely ionized:

- for acids with $\mathrm {pH} -\mathrm {p} K_{a}>1$ , $\log D_{\text{acids}}\cong \log P+\mathrm {p} K_{a}-\mathrm {pH}$ ,
- for bases with $\mathrm {p} K_{a}-\mathrm {pH} >1$ , $\log D_{\text{bases}}\cong \log P-\mathrm {p} K_{a}+\mathrm {pH}$ .

For prediction of p*K*a, which in turn can be used to estimate log *D*, Hammett type equations have frequently been applied.

### Log *P* from log *S*

If the solubility, *S*, of an organic compound is known or predicted in both water and 1-octanol, then log *P* can be estimated as

$\log P=\log S_{\text{o}}-\log S_{\text{w}}.$

There are a variety of approaches to predict solubilities, and so log *S*.

## Octanol-water partition coefficient

The partition coefficient between *n*-Octanol and water is known as the ***n*-octanol-water partition coefficient**, or *K*ow. It is also frequently referred to by the symbol P, especially in the English literature. It is also known as ***n*-octanol-water partition ratio**.

*K*ow, being a type of partition coefficient, serves as a measure of the relationship between lipophilicity (fat solubility) and hydrophilicity (water solubility) of a substance. The value is greater than one if a substance is more soluble in fat-like solvents such as n-octanol, and less than one if it is more soluble in water.

### Example values

Values for log *K*ow typically range between -3 (very hydrophilic) and +10 (extremely lipophilic/hydrophobic).

The values listed here are sorted by the partition coefficient. Acetamide is hydrophilic, and 2,2′,4,4′,5-Pentachlorobiphenyl is lipophilic.

| Substance | log *K*OW | T | Reference |
|---|---|---|---|
| Acetamide | −1.155 | 25 °C |   |
| Methanol | −0.824 | 19 °C |   |
| Formic acid | −0.413 | 25 °C |   |
| Diethyl ether | 0.833 | 20 °C |   |
| *p*-Dichlorobenzene | 3.370 | 25 °C |   |
| Hexamethylbenzene | 4.610 | 25 °C |   |
| 2,2′,4,4′,5-Pentachlorobiphenyl | 6.410 | Ambient |   |
