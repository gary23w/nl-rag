---
title: "Isothermal titration calorimetry"
source: https://en.wikipedia.org/wiki/Isothermal_titration_calorimetry
domain: fragment-based-drug-discovery
license: CC-BY-SA-4.0
tags: fragment library, weak binder, surface plasmon resonance, growing
fetched: 2026-07-02
---

# Isothermal titration calorimetry

In chemical thermodynamics, **isothermal titration calorimetry** (**ITC**) is a physical technique used to determine the thermodynamic parameters of interactions in solution. ITC is the only technique capable of comprehensively characterizing thermodynamic and kinetic profiles of a molecular interaction by simultaneously determining binding constants ( $K_{a}$ ), reaction stoichiometry ( n ), enthalpy ( $\Delta H$ ), Gibbs free energy ( $\Delta G$ ) and entropy ( $\Delta S$ ) within a single experiment. It consists of two cells which are enclosed in an adiabatic jacket.

The compounds to be studied are placed in the sample cell, while the other cell, the reference cell, is used as a control and contains the buffer in which the sample is dissolved. The technique quantifies the heat released or absorbed during the binding process by incrementally adding one reactant (via a syringe) to another (in the sample cell) while maintaining constant temperature and pressure. Heat-sensing devices within the ITC detect temperature variations between two cells, transmitting this information to heaters that adjust accordingly to restore thermal equilibrium between the cells. This energy is converted into binding enthalpy using the information about concentrations of the reactants and the cell volume. Compared to other calorimeters, ITC does not require any correctors since there is no heat exchange between the system and the environment. ITC is also highly sensitive with a fast response time and benefits from modest sample requirements. While differential scanning calorimetry (DSC) can also provide direct information about the thermodynamic of binding interactions, ITC offers the added capability of quantifying the thermodynamics of metal ion binding to proteins.

## History of ITC

The history of ITC can be traced back to the 1930s when isothermal calorimetry was used to study chemical reactions. In 1965 Christensen and Izatt introduced titration calorimetry as a method for simultaneously determining the equilibrium constant and enthalpy. The ITC technique was then developed by H. D. Johnston in 1968 as a part of his Ph.D. dissertation at Brigham Young University, and was considered niche until introduced commercially by MicroCal Inc. in 1988. In 1978, Beaudette and Langerman conducted one of the earliest calorimetric binding studies using a small volume isoperibol titration calorimeter and a decade later, in 1989, Wiseman, Williston, Brandts, and Lin demonstrated its application in biological systems, marking the beginning of titration calorimetry as a valuable tool for studying biological equilibria. Originally, ITC was most often used to study the binding of small molecules (such as medicinal compounds) to larger macromolecules (proteins, DNA etc.) in a label-free environment. Its application has now broadened, aided by modern improvements, making it possible to measure the heat effects as small as 0.1 μcal (0.4 μJ) and determine the binding constants (K) as high as 108–109 M−1.

## Thermodynamic measurements

ITC is a quantitative technique that can determine the binding affinity ( $K_{a}$ ), reaction enthalpy ( $\Delta H$ ), and binding stoichiometry ( n ) of the interaction between two or more molecules in solution. This is achieved by measuring the enthalpies of a series of binding reactions caused by injections of a solution of one molecule to a reaction cell containing a solution of another molecule. The enthalpy values are plotted over the molar ratios resulting from the injections. From the plot, the molar reaction enthalpy $\Delta H$ , the affinity constant ( $K_{a}$ ) and the stochiometry are determined by curve fitting. The reaction's Gibbs free energy change ( $\Delta G$ ) and entropy change ( $\Delta S$ ) can be determined using the relationship:

$\Delta G=-RT\ln {K_{a}}=\Delta H-T\Delta S$

(where R is the gas constant and T is the absolute temperature).

For accurate measurements of binding affinity, the curve of the thermogram must be sigmoidal. A steep sigmoidal curve signals a strong binding whereas a less steep sigmoidal curve points to a weaker binding. The profile of the curve is determined by the c-value, which is calculated using the equation:

$c=nK_{a}M$

where n is the stoichiometry of the binding, $K_{a}$ is the association constant and M is the concentration of the molecule in the cell. The c-value must fall between 1 and 1000, ideally between 10 and 100. In terms of binding affinity, it would be approximately from $1.0\times 10^{3}$ ~ $10^{7}$ within the limit range. If it does not fall within the above range, the thermodynamic values obtained from the experiment are less robust to interpretation.

## Instrumental measurements

An isothermal titration calorimeter is composed of two identical cells made of a highly efficient thermally conducting and chemically inert material such as Hastelloy alloy or gold, surrounded by an adiabatic jacket. In this setup, one of the cells, the sample cell, holds the solution of one reactant, and the other cell, the reference cell, is filled with either a buffer or water.

The second reactant, which has a higher concentration than the first, is placed in a syringe and gradually injected into the sample cell in small aliquots throughout the titration process. This process is semi-automated and the sensitive thermopile/thermocouple circuits are used to detect temperature differences between the reference cell (filled with buffer or water) and the sample cell containing the macromolecule. Prior to addition of ligand, a constant power (<1 mW) is applied to the reference cell. This directs a feedback circuit, activating a heater located on the sample cell. During the experiment, ligand is titrated into the sample cell in precisely known aliquots, causing heat to be either taken up or evolved (depending on the nature of the reaction). Measurements consist of the time-dependent input of power required to maintain equal temperatures between the sample and reference cells.

In an exothermic reaction, the temperature in the sample cell increases upon addition of ligand. This causes the feedback power to the sample cell to be decreased (remember: a reference power is applied to the reference cell) in order to maintain an equal temperature between the two cells. In an endothermic reaction, the opposite occurs; the feedback circuit increases the power in order to maintain a constant temperature (isothermal operation).

Observations are plotted as the power needed to maintain the reference and the sample cell at an identical temperature against time. As a result, the experimental raw data consists of a series of spikes of heat flow (power), with every spike corresponding to one ligand injection. These heat flow spikes/pulses are integrated with respect to time, giving the total heat exchanged per injection. By integrating each peak from the baseline, the total heat associated with each injection is obtained, including both reaction-specific and non-reaction-related contributions. The pattern of these heat effects as a function of the molar ratio [ligand]/[macromolecule] can then be analyzed to give the thermodynamic parameters of the interaction under study.

## Experimental Procedures

In order to accurately and precisely measure the thermodynamic parameters using ITC, certain procedures must be followed, involving instrument set up, parameter configuration, sample loading, buffer selection, and instrument cleaning. To obtain an optimum result, each injection should be given enough time for a reaction equilibrium to reach. Degassing samples is often necessary in order to obtain good measurements as the presence of gas bubbles within the sample cell will lead to abnormal data plots in the recorded results. The entire experiment takes place under computer control.

Direct titration is performed most commonly with ITC to obtain the thermodynamic data, by binding two components of the reaction directly to each other. However, many of the chemical reactions and binding interactions may have higher binding affinity above what is desirable with the c-window. To troubleshoot the limitation of c-window and conditions for certain binding interactions, various different methods of titration can be performed. In some cases, simply doing a reverse titration of changing the samples between the injection syringe and sample cell can solve the issue, depending on the binding mechanism. However, the process of introducing a ligand to a macromolecule is distinct from the process of adding a macromolecule to a ligand. While the binding equilibrium remains unchanged in both direct and reverse titrations, the route to equilibrium and the accessible binding states varies, particularly when one molecule possesses multiple binding sites for the other. Most of the high or low affinity bindings require chelation or competitive titration. This method is done by loading pre-bound complex solution in the sample cell and chelating one of the components out with a reagent of higher observed binding affinity within the desirable c-window.

In order to ensure optimum instrument stability, the ITC instrument should be powered on at least one day before use. Samples should ideally be pre-equilibrated to approximately 2 °C below the target experimental temperature to reduce stabilization time after loading, although starting at the exact experimental temperature is also an option. For instrument cleaning, sample cell should be rinsed with the experimental buffer and dried under vacuum, and any remaining rinsed solution should be discarded manually with a syringe. Then, the sample cell is filled with the experimental solution and the reference cell with either high-purity water or the same buffer. To prevent air contamination, gas-tight Hamilton syringes are used, ensuring the needle is positioned near the bottom of the sample cell before dispensing the liquid slowly. Experimental parameters such as the number of injections, initial injection volume, subsequent injection volumes, temperature, reference power, stirring speed, spacing, initial delay, and filter period should be adjusted according to the specific study.

If the experiment is to be repeated, the syringe should be emptied, with the solution either discarded or saved for further analysis. Before refilling with the same solution, the syringe needle should be externally rinsed and dried with lint-free paper, without the need for an internal wash. However, when switching to a different reagent or concentration, the syringe must be thoroughly washed, flushed with ethanol or methanol, and carefully dried under vacuum-using a ThermoVac for VP-ITC or the integrated vacuum systems in other models. The sample cell should be emptied using the loading syringe and rinsed multiple times with water.

## Analysis and interpretation

### *Post-hoc* analysis and proton inventory

It is necessary to conduct a post-hoc analysis to determine the buffer or solvent-independent enthalpy from the experimental thermodynamics. The collected experimental data reflects not only the binding thermodynamics of the interaction of interest, but any contributing competing equilibria associated to it. A post-hoc analysis can be performed to determine the buffer or solvent-independent enthalpy from the experimental thermodynamics, by simply going through the process of Hess' law. Below example shows a simple interaction between a metal ion (M) and a ligand (L). B represents the buffer used for this interaction and ${\ce {H+}}$ represents protons.

> ${\ce {M - B <=> M + B}}$ ${\ce {-\Delta H_{MB}}}$
> 
> ${\ce {L - H <=> L + H+}}$ $-(n_{H+})\Delta H_{LH}$
> 
> ${\ce {H+ + B <=> H - B}}$ $(n_{H+})\Delta H_{BH}$
> 
> ${\ce {M + L <=> M - L}}$ $\Delta H_{ML}$

Therefore,

> $\Delta H_{ITC}=-\Delta H_{MB}-(n_{H+})\Delta H_{LH}+(n_{H+})\Delta H_{BH}+\Delta H_{ML}$

which can be further processed to calculate the enthalpy of metal-ligand interaction. Although this example is between a metal and a ligand, it is applicable to any ITC experiment, regarding binding interactions.

As a part of the analysis, a number of protons are required to calculate the solvent-independent thermodynamics. This can be easily done by plotting a graph such as shown below.

The linear equation of this plot is the rearranged version of the equation above from the post-hoc analysis in a form of y = mx + b:

> $\Delta H_{ITC}=(n_{H+})\Delta H_{BH}+[-\Delta H_{MB}-(n_{H+})\Delta H_{LH}+\Delta H_{ML}]$

### Equilibrium constant

Equilibrium constant of the reaction is also not independent from the other competing equilibria. Competition would include buffer interactions and other pH-dependent reactions depending on the experimental conditions. The competition from species other than the species of interest is included in the competition factor, Q in the following equation:

> $Q=\Sigma (\beta _{n}[\mathrm {X} ]_{n})$

where, X represents species such a buffer or protons, $\beta$ represents their equilibrium constant, when,

> $K_{ML}=K_{ITC}Q$

## Applications

For the past 30 years, isothermal titration calorimetry has been used in a wide array of fields, ranging from metal binding studies to drug discovery, and nanomaterials research. In the old days, this technique was used to determine fundamental thermodynamic values for basic small molecular interactions. In recent years, ITC has been used in more industrially applicable areas, such as drug discovery and testing synthetic materials. Although it is still heavily used in fundamental chemistry, the trend has shifted over to the biological side, where label-free and buffer independent values are relatively harder to achieve.

### Enzyme kinetics

Using the thermodynamic data from ITC, it is possible to deduce enzyme kinetics including proton or electron transfer, allostery and cooperativity, and enzyme inhibition. Modern ITC instruments can measure heat rates as small as 0.1 μcal/sec, allowing for the precise determination of reaction rates in the range of 10−12 mol/sec and ITC can determine values for Km and kcat, in the ranges of 10−2–103 μM and 0.05–500 sec−1, respectively. ITC collects data over time that is useful for any kinetic experiments, but especially with the proteins due to constant aliquots of injections. In terms of calculation, equilibrium constant and the slopes of binding can be directly utilized to determine the allostery and charge transfer, by comparing experimental data of different conditions (pH, use of mutated peptide chain and binding sites, etc.). Kinetic data obtained from ITC have been found to closely align with results from other purely kinetic methods, such as surface plasmon resonance.

### Membrane and self-assembling peptide studies

Membrane proteins and self-assembly properties of certain proteins can be studied under this technique, due to being a label-free calorimeter. Membrane proteins are known to have difficulties with selection of proper solubilization and purification protocols. As ITC is a non-destructive calorimetric tool, it can be used as a detector to locate the fraction of protein with desired binding sites, by binding a known binding ligand to the protein. This feature also applies in studies of self-assembling proteins, especially in use of measuring thermodynamics of their structural transformation.

### Drug development

ITC can provide insights into drug development by charactering the affinity, selectivity, ligand-induced conformational changes, and drug partitioning into membranes. Binding affinity carries a huge importance in medicinal chemistry, as drugs need to bind to the protein effectively within a desired range. An exothermic binding process with a favorable enthalpy is considered a desirable characteristic for specific protein binders, as it indicates strong potential for optimization and high selectivity. However, determining enthalpy changes and optimization of thermodynamic parameters are hugely difficult when designing drugs. ITC troubleshoots this issue easily by deducing the binding affinity, enthalpic/entropic contributions and its binding stoichiometry.

### Chiral chemistry

Applying the ideas above, chirality of organometallic compounds can be deduced as well with this technique. Each chiral compound has its own unique properties and binding mechanisms that are comparable to each other, which leads to differences in thermodynamic properties. By binding chiral solutions in a binding site can deduce the type of chirality and depending on the purpose, which chiral compound is more suitable for binding.

### Metal binding interactions

Binding metal ions to protein and other components of biological material is one of the most popular uses of ITC, since ovotransferrin to ferric iron binding study published by Lin et al. from MicroCal Inc. This is due to some of the metal ions utilized in biological systems having d10 electron configuration which cannot be studied with other common techniques such as UV-vis spectrophotometry or electron paramagnetic resonance. It is also closely related to biochemical and medicinal studies due to the large abundance of metal binding enzymes in biological systems.

The technique has been well utilized in studying carbon nanotubes to determine thermodynamic binding interactions with biological molecules and graphene composite interactions. Another notable use of ITC with carbon nanotubes is optimization of preparation of carbon nanotubes from graphene composite and polyvinyl alcohol (PVA). PVA assembly process can be measured thermodynamically as mixing of the two ingredients is an exothermic reaction, and its binding trend can be easily observed by ITC.

### Nanoparticle-Protein Interactions

ITC is increasingly utilized to study protein-nanoparticle interactions by providing key insights into binding affinity (in the form of association constant), interaction mechanisms (quantified through binding enthalpy, binding entropy, and Gibbs free energy), and binding stoichiometry. These thermodynamic parameters from ITC can help assess structural modifications in proteins upon adsorption onto nanoparticle surfaces.

## Limitations

One of the main limitations of ITC is that it is prone to allowing only moderate binding conformations to be detected, making it less effective for detecting very weak or extremely tight binding events. Hence, it may struggle to provide accurate thermodynamic parameters for slow kinetic processes with long time constants, as these interactions may be masked by baseline noise and variability. On the other hand, high-affinity interactions can be challenging to measure if they take several minutes or longer to fully develop, or if the measured signal depends on the reaction enthalpy. When the binding enthalpy is close to zero, ITC may fail to generate meaningful interaction data, instead producing a series of small, uniform peaks that result in flat and uninformative thermograms.

ITC is also susceptible to interference from unrelated heat signals, making it difficult to isolate and interpret the heat changes associated with the interaction of interest. Other limitations include solubility constraints, challenges in accurately determining protein concentration and the need to prepare the ligand in the same solution conditions as the protein for reliable measurements.
