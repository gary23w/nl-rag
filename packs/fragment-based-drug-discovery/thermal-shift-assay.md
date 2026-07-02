---
title: "Thermal shift assay"
source: https://en.wikipedia.org/wiki/Thermal_shift_assay
domain: fragment-based-drug-discovery
license: CC-BY-SA-4.0
tags: fragment library, weak binder, surface plasmon resonance, growing
fetched: 2026-07-02
---

# Thermal shift assay

A **thermal shift assay** (**TSA**) measures the stability of a protein by the change in its thermal denaturation temperature. This is done under varying conditions, such as variations in drug concentration, buffer formulation (pH or ionic strength), redox potential, or sequence mutation. The most common method for measuring protein thermal shifts is differential scanning fluorimetry (DSF). DSF methodology includes techniques such as nanoDSF, which relies on the intrinsic fluorescence from native tryptophan or tyrosine residues, and Thermofluor, which utilizes extrinsic fluorogenic dyes.

The binding of low molecular weight ligands can increase the thermal stability of a protein, as described by Daniel Koshland (1958) and Kaj Ulrik Linderstrøm-Lang and Schellman (1959). Almost half of enzymes require a metal ion co-factor. Thermostable proteins are often more useful than their non-thermostable counterparts, e.g., DNA polymerase in the polymerase chain reaction, so protein engineering often includes adding mutations to increase thermal stability. Protein crystallization is more successful for proteins with a higher melting point and adding buffer components that stabilize proteins improve the likelihood of protein crystals forming. If examining pH then the possible effects of the buffer molecule on thermal stability should be taken into account along with the fact that pKa of each buffer molecule changes uniquely with temperature. Additionally, any time a charged species is examined the effects of the counterion should be accounted for.

Thermal stability of proteins has traditionally been investigated using biochemical assays, circular dichroism, or differential scanning calorimetry. Biochemical assays require a catalytic activity of the protein in question as well as a specific assay. Circular dichroism and differential scanning calorimetry both consume large amounts of protein and are low-throughput methods. The Thermofluor assay was the first high-throughput thermal shift assay and its utility and limitations has spurred the invention of a plethora of alternate methods. Each method has its strengths and weaknesses but they all struggle with intrinsically disordered proteins without any clearly defined tertiary structure as the essence of a thermal shift assay is measuring the temperature at which a protein goes from well-defined structure to disorder.

## Methods

### nanoDSF

nano-Differential scanning fluorimetry, or nanoDSF, is a biophysical characterization technique used for assessing the conformational stability of a biological sample, typically a protein. Samples are subjected to either temperature ramps or gradients of chemical denaturant, and the intrinsic fluorescence is measured and fit to determine the melting point (*T*m). Applications include formulation ranking, protein engineering (comparing mutants to wild type), and ligand binding (quantification of affinity constants). A prerequisite of the technique is that the protein must contain an intrinsically fluorescent residue, typically tryptophan or tyrosine residues. Benefits include tag-free analysis, avoidance of extrinsic fluorophores, low sample consumption, easy of use, amenity to automation, and high screening throughput. Drawbacks include a propensity for false positives and negatives, usually necessitating follow-up screening with a potentially lower-throughout orthogonal technique to confirm. Current commercial instruments employ either proprietary capillaries or generic high-throughput 384-well plates for sample analysis.

### Thermofluor

The technique was first described by Semisotnov et al. (1991) using 1,8-ANS and quartz cuvettes. 3 Dimensional Pharmaceuticals were the first to describe a high-throughput version using a plate reader and Wyeth Research published a variation of the method with SYPRO Orange instead of 1,8-ANS. SYPRO Orange has an excitation/emission wavelength profile compatible with qPCR machines which are almost ubiquitous in institutions that perform molecular biology research. The name differential scanning fluorimetry (DSF) was introduced later but Thermofluor is preferable as Thermofluor is no longer trademarked and differential scanning fluorimetry is easily confused with differential scanning calorimetry.

SYPRO Orange binds nonspecifically to hydrophobic surfaces, and water strongly quenches its fluorescence. When the protein unfolds, the exposed hydrophobic surfaces bind the dye, resulting in an increase in fluorescence by excluding water. Detergent micelles will also bind the dye and increase background noise dramatically. This effect is lessened by switching to the dye ANS; however, this reagent requires UV excitation. The stability curve and its midpoint value (melting temperature, *T*m also known as the temperature of hydrophobic exposure, *T*h) are obtained by gradually increasing the temperature to unfold the protein and measuring the fluorescence at each point. Curves are measured for protein only and protein + ligand, and Δ*T*m is calculated. The method may not work very well for protein-protein interactions if one of the interaction partners contains large hydrophobic patches as it is difficult to dissect prevention of aggregation, stabilization of a native folds, and steric hindrance of dye access to hydrophobic sites. In addition, partly aggregated protein can also limit the relative fluorescence increase upon heating; in extreme cases there will be no fluorescence increase at all because all protein is already in aggregates before heating. Knowing this effect can be very useful as a high relative fluorescence increase suggests a significant fraction of folded protein in the starting material.

This assay allows high-throughput screening of ligands to the target protein and it is widely used in the early stages of drug discovery in the pharmaceutical industry, structural genomics efforts, and high-throughput protein engineering.

#### A typical assay

1. Materials: A fluorometer equipped with temperature control or similar instrumentation (qPCR machines); suitable fluorescent dye; a suitable assay plate, such as a 96-well qPCR plate.
2. Compound solutions: Test ligands are prepared at a 50- to 100-fold concentrated solution, generally in the 10–100 mM range. For titration, a typical experimental protocol employs a set of 12 wells, comprising 11 different concentrations of a test compound with a single negative control well.
3. Protein solution: Typically, target protein is diluted from a concentrated stock to a working concentration of ~0.5–5 μM protein with dye into a suitable assay buffer. The exact concentrations of protein and dye are defined by experimental assay development studies.
4. Centrifugation and oil dispense: Brief centrifugation (~1000 × g, 1 min) of the assay plate to mix compounds into the protein solution, 1–2 μL of silicone oil to prevent the evaporation during heating is overlaid onto the solution (some systems use plastic seals instead), followed by an additional centrifugation step (~1000 × g, 1 min).
5. Instrumental set up: A typical temperature ramp rates range from 0.1 to 10 °C/min but generally in the range of 1 °C/min. The fluorescence in each well is measured at regular intervals, 0.2–1 °C/image, over a temperature range spanning the typical protein unfolding temperatures of 25–95 °C.

### CPM, thiol-specific dyes

Alexandrov et al. (2008) published a variation on the Thermofluor assay where SYPRO Orange was replaced by *N*-[4-(7-diethylamino-4-methyl-3-coumarinyl)phenyl]maleimide (CPM), a compound that only fluoresces after reacting with a nucleophile. CPM has a high preference for thiols over other typical biological nucleophiles and therefore will react with cysteine side chains before others. Cysteines are typically buried in the interior of a folded protein as they are hydrophobic. When a protein denatures cysteine thiols become available and a fluorescent signal can be read from reacted CPM. The excitation and emission wavelengths for reacted CPM are 387 nm/ 463 nm so a fluorescence plate reader or a qPCR machine with specialized filters is required. Alexandrov et al. used the technique successfully on the membrane proteins Apelin GPCR and FAAH as well as β-lactoglobin which fibrillates on heating rather than going to a molten globule.

### DSF-GTP

The DSF-GTP (GFP-Tagged Protein-of-Interest) technique was developed by a team led by Patrick Schaeffer at James Cook University and published in Moreau et al. 2012. The development of differential scanning fluorimetry and the high-throughput capability of Thermofluor have vastly facilitated the screening of crystallization conditions of proteins and large mutant libraries in structural genomics programs, as well as ligands in drug discovery and functional genomics programs. These techniques are limited by their requirement for both highly purified proteins and solvatochromic dyes, prompting the need for more robust high-throughput technologies that can be used with crude protein samples. This need was met with the development of a new high-throughput technology for the quantitative determination of protein stability and ligand binding by differential scanning fluorimetry of proteins tagged with green fluorescent protein (GFP). This technology is based on the principle that a change in the proximal environment of GFP, such as unfolding and aggregation of the protein of interest, is measurable through its effect on the fluorescence of the fluorophore. The technology is simple, fast and insensitive to variations in sample volumes, and the useful temperature and pH range is 30–80 °C and 5–11 respectively. The system does not require solvatochromic dyes, reducing the risk of interferences. The protein samples are simply mixed with the test conditions in a 96-well plate and subjected to a melt-curve protocol using a real-time thermal cycler. The data are obtained within 1–2 h and include unique quality control measures through the GFP signal. DSF-GTP has been applied for the characterization of proteins and the screening of small compounds.

### DCVJ, rigidity sensitive dyes

4-(dicyanovinyl)julolidine (DCVJ) is a molecular rotor probe with fluorescence that is strongly dependent on the rigidity of its environment. When protein denatures, DCVJ increases in fluorescence. It has been reported to work with 40 mg/ml of antibody.

### Intrinsic tryptophan fluorescence lifetime

The lifetime of tryptophan fluorescence differs between folded and unfolded protein. Quantification of UV-excited fluorescence lifetimes at various temperature intervals yields a measurement of *T*m. A prominent advantage of this technique is that no reporter dyes need be added as tryptophan is an intrinsic part of the protein. This can also be a disadvantage as not all proteins contain tryptophan. Intrinsic fluorescence lifetime works with membrane proteins and detergent micelles but a powerful UV fluorophore (e.g. auto-fluorescent small molecule) in the buffer could drown out the signal.

### Intrinsic tryptophan fluorescence wavelength

Utilization of the intrinsic fluorescence properties of tryptophan residues in many proteins forms the basis of nanoDSF. The emission wavelengths of tryptophan residues are dependent on the surrounding chemical environment, notably solvation (see solvatochromism) and therefore differ between folded and unfolded protein, just as with the fluorescence lifetime. Typically, interior tryptophan residues in a more hydrophobic environment exhibit a notable emission red shift from approximately 330 nm to 350 nm upon protein unfolding and exposure to water. Quantification of fluorescence wavelength shifts at various temperature intervals yields a measurement of *T*m. Currently there are at least three instruments on the market that can read this shift in wavelength in a high-throughput manner while heating the samples. The advantages and disadvantages are the same as for fluorescence lifetime except that there are more examples in the scientific literature of use. nanoDSF uses the intrinsic fluorescence of tryptophan residues present in many proteins to monitor protein folding and stability. Because tryptophan fluorescence depends on the local chemical environment, protein unfolding exposes buried residues to water and typically shifts the emission maximum from about 330 nm to 350 nm.

### Static light scattering

Static light scattering allows monitoring of the sizes of the species in solution. Since proteins typically aggregate upon denaturation (or form fibrils) the detected species size will go up.

This is label-free and independent of specific residues in the protein or buffer composition. The only requirement is that the protein actually aggregates/fibrillates after denaturation and that the protein of interest has been purified.

### FastPP

In fast parallel proteolysis the researcher adds a thermostable protease (thermolysin) and takes out samples in parallel upon heating in a thermal gradient cycler. Optionally, for instance for proteins expressed at low levels, a western blot is then run to determine at what temperature a protein becomes degraded. For pure or highly enriched proteins, direct SDS-PAGE detection is possible facilitating Commassie-fluorescence based direct quantification. FastPP exploits that proteins become increasingly susceptible to proteolysis when unfolded and that thermolysin cleaves at hydrophobic residues which are typically found in the core of proteins.

To reduce the workload, western blots could be replaced by SDS-PAGE gel polyhistidine-tag staining, provided that the protein has such a tag and is expressed in adequate amounts.

FastPP can be used on unpurified, complex mixtures of proteins and proteins fused with other proteins, such as GST or GFP, as long as the sequence that is the target of the western blot, e.g., His-tag, is directly linked to the protein of interest. However, commercially available thermolysin is dependent on calcium ions for activity and denatures itself just above 85 degrees Celsius. So calcium must be present and calcium chelators absent in the buffer - other compounds that interfere with the function (such as high concentrations of detergents) of the protease could also be problematic.

FASTpp has also been used to monitor binding-coupled folding of intrinsically disordered proteins (IDPs).

### CETSA

Cellular thermal shift assay (CETSA®) is a biophysical technique applicable on living cells as well as tissue biopsies. CETSA® is based on the discovery that protein melting curves can also be generated in intact cells and that drug binding leads to very significant thermal stabilization of proteins. Upon denaturation, proteins are aggregated and can thus be removed by centrifugation after lysis of the cells. The stable proteins are found in the supernatant can be detected; e.g., by western blot, alpha-LISA, or mass spectrometry. The CETSA®-technique is highly stringent, reproducible, and not prone to false positives. However, it is possible for a sample, or small molecule compound, to bind a protein in a given target's pathway. If that protein induces further stabilization of the original target protein through a cascade event, it could manifest as direct target engagement. An advantage of this method is that it is label-free and thus applicable for studies of drug binding in a wide range of cells and tissues. CETSA® can also be conducted on cell lysates versus intact cells, helping to determine sample penetration of the cell membrane.

### ThermoFAD

Thermofluor variant specific for flavin-binding proteins. Analogous to Thermofluor binding assays, a small volume of protein solution is heated up and the fluorescence increase is followed as function of temperature. In contrast to Thermofluor, no external fluorescent dye is needed because the flavin cofactor is already present in the flavin-binding protein and its fluorescence properties change upon unfolding.

### SEC-TS

Size exclusion chromatography can be used directly to access protein stability in the presence or absence of ligands. Samples of purified protein are heated in a water bath or thermocycler, cooled, centrifuged to remove aggregated proteins, and run on an analytical HPLC. As the melting temperature is reached and protein precipitates or aggregates, peak height decreases and void peak height increases. This can be used to identify ligands and inhibitors, and optimize purification conditions.

While of lower throughput than FSEC-TS, requiring large amounts of purified protein, SEC-TS avoids any influence of the fluorescent tag on apparent protein stability.

### FSEC-TS

In fluorescence-detection size exclusion chromatography the protein of interest is fluorescently tagged (e.g., with GFP) and run through a gel filtration column on an FPLC system equipped with a fluorescence detector. The resulting chromatogram allows the researcher to estimate the dispersity and expression level of the tagged protein in the current buffer. Since only fluorescence is measured, only the tagged protein is seen in the chromatogram. FSEC is typically used to compare membrane protein orthologs or screen detergents to solubilize specific membrane proteins in.

For fluorescence-detection size-exclusion chromatography-based thermostability assay (FSEC-TS) the samples are heated in the same manner as in FastPP and CETSA and following centrifugation to clear away precipitate the supernatant is treated in the same manner as FSEC. Larger aggregates are seen in the void volume while the peak height for the protein of interest decreases when the unfolding temperature is reached.

GFP has a *T*m of ~76 °C so the technique is limited to temperature below ~70 °C.

### Radioligand binding thermostability assay

GPCRs are pharmacologically important transmembrane proteins. Their X-ray crystal structures were revealed long after other transmembrane proteins of lesser interest. The difficulty in obtaining protein crystals of GPCRs was likely due to their high flexibility. Less flexible versions were obtained by truncating, mutating, and inserting T4 lysozyme in the recombinant sequence. One of the methods researchers used to guide these alterations was radioligand binding thermostability assay.

The assay is performed by incubating the protein with a radiolabelled ligand of the protein for 30 minutes at a given temperature, then quench on ice, run through a gel filtration mini column, and quantify the radiation levels of the protein that comes off the column. The radioligand concentration is high enough to saturate the protein. Denatured protein is unable to bind the radioligand and the protein and radioligand will be separated in the gel filtration mini column. When screening mutants selection will be for thermal stability in the specific conformation, i.e., if the radioligand is an agonist, selection will be for the agonist binding conformation and if it is an antagonist, then the screening is for stability in the antagonist binding conformation.

Radioassays have the advantage of working with minute amounts of protein. But it is work with radioactive substances and large amount of manual labour is involved. A high-affinity ligand has to be known for the protein of interest and the buffer must not interfere with the binding of the radioligand. Other thermal shift assays can also select for specific conformations if a ligand of the appropriate type is added to the experiment.

### Comparisons of the various approaches

Thermofluor

CPM

DCVJ

Tryptophan fluorescence lifetime

Tryptophan fluorescence wavelength

Static light scattering

FastPP

CETSA

SEC-TS

FSEC-TS

Radioligand binding thermostability assay

Purification

Pure protein

Pure protein

Pure protein at very high concentration

Pure protein

Pure protein

Pure protein

Complex mixture

Complex mixture

Pure protein

Complex mixture

Complex mixture

Detergents

Below

CMC

Yes

Yes

Yes

Yes

Yes

Yes (low conc.)

Yes

Yes

Yes

Yes

Buffer

Avoid very high conc. organic solvents

Avoid thiols, possibly other nucleophiles

-

-

-

-

Thermolysin requires calcium ions

-

-

-

Should maximize radioligand binding affinity

Throughput

Highest

Highest

Highest

Intermediate

Intermediate

Intermediate

Intermediate-low (if western required)

Lowest (intermediate with FRET)

Lowest

Lowest

Lowest

Sequence requirements

No

Cysteines, not on surface and not in disulphide bonds

No

Tryptophan

Tryptophan

No

Sequence must contain hydrophobic residues (required for cleavage)

For antibody

No

For fluorescent tag

No

Equipment requirements

qPCR machine

qPCR machine with UV excitation or fluorescence plate reader

qPCR machine

High-throughput differential intrinsic fluorescence lifetime reader

High-throughput differential intrinsic fluorescence wavelength reader

High-throughput differential static light scattering reader

Thermal cycler (or water bath) and western blot

Thermal cycler (or water bath) and western blot (or FRET reader)

Thermal cycler (or water bath) and HPLC

Thermal cycler (or water bath) and FPLC/HPLC with fluorescence reader

Thermal cycler (or water bath) and scintillation counter

Labels

Yes + DMSO

Yes + DMSO

Yes + DMSO

Label-free

Label-free

Label-free

Label-free

Label-free

Label-free

Yes

Radioligand

Possible interference from fluorophores in buffer

Yes

Yes

Yes

Yes

Yes

No

No

No

No

Yes

No

Fusion proteins

No

Possibly

No

Possibly

Possibly

No

Optional

No

No

Yes

Yes

Works with proteins that fibrillate when heated

No

Yes, at least with beta-lactoglobulin

Yes

Yes, probably

Yes, probably

Yes

Yes (if cleavage faster than fibrillisation at high TL conc.)

Yes

Yes

Yes

Yes

## Applications

### Label-free drug screening

Thermofluor has been extensively used in drug screening campaigns. Because Thermofluor detects high affinity binding sites for small molecules on proteins, it can find hits that bind to active site subsites, cofactor sites, or allosteric binding sites with equal efficacy. The method typically requires the use of screening compound concentrations at >10x the desired binding threshold. Setting 5 μM as a reasonable hit threshold consequently requires a test ligand concentration of 50 to 100 μM in the sample well. For most drug compound libraries, where many compounds are not soluble beyond ~100 μM, screening multiple compounds is consequently not feasible owing to solubility issues. Thermofluor screens do not require the development of custom screening reagents (e.g. cleavable substrate analogs), do not require any radioactive reagents, and are generally less sensitive to the effects of compounds that are chemically reactive with protein active site residues, and that consequently show up as undesirable hits in enzyme activity screens.

### Drug lead optimization

Thermofluor measurements of *T*m can be quantitatively related to drug *K*d values, although this requires the additional calorimetric measurements of the target proteins' enthalpy of unfolding, determined using DSC. The dynamic range of the Thermofluor assay is very large, so that the same assay can be used to find micromolar hits and to optimize sub-nanomolar leads, making the method particularly useful in the development of QSAR relationships for lead optimization.

### Studies of enzyme mechanism

Many proteins require the simultaneous or sequential binding of multiple substrates, cofactors, and/or allosteric effectors. Thermofluor studies of molecules that bind to active site subsites, cofactor sites, or allosteric binding sites can help elucidate specific features of enzyme mechanism that can be important in the design of effective drug screening campaigns and in characterizing novel inhibitory mechanisms.

### Protein stabilization for optimized isolation

Thermofluor pre-screens can be performed that sample a wide range of pH, ionic strength, and additives such as added metal ions and cofactors. The generation of a protein response surface is useful for establishing optimal assay conditions and can frequently lead to improved purification scheme as required to support HTS campaigns and biophysical studies.

### Characterization of engineered proteins

Many applications of protein engineering for drug discovery or biophysics applications involve modification of the protein amino acid sequence through truncation, domain fusions, site-specific modifications or random mutagenesis. Thermofluor provides a high throughput method for the evaluation of the effects of such sequence variations on protein stability as well as means for developing stabilizing conditions if required.

### Optimization of protein crystallization conditions

Although proteins are dynamic structures in solution, formation of protein crystals is expected to be favored when all molecules lie in their lowest energy conformation. Thermofluor evaluation of conditions that stabilize proteins is consequently a useful strategy for finding optimal crystallization conditions

### Screening for inhibitors of protein-protein interactions of modulators of protein conformational changes

Since Thermofluor is a label-free assay that detects small molecule binding to high affinity binding sites on a target protein, it is well suited to finding small molecule inhibitors of protein-protein interactions or allosteric modulation sites. Of course, whether or not a protein-protein interaction is ultimately "druggable" with a small molecule requires the presence of a suitable binding site on the target protein that provides enough local energetic interactions to allow specific drug binding.

### ThermoFluor of membrane proteins

Membrane proteins are often isolated in the presence of hydrophobic solubilizing agents that can partition hydrophobic-binding dyes like 1,8-ANS and SYPRO orange and generate a fluorescence background that obscures observation of a Thermofluor protein melting signal. Nevertheless, careful optimization of conditions (e.g., to avoid micelle formation of the solubilizing agent) can often produce satisfactory assay conditions

### Decrypting proteins of unknown biological function

The biochemical function of protein targets identified through gene knockout or proteomics approaches are often obscure if they have low amino acid sequence homology with proteins of known function. In many cases some useful information can be gained through the identification of binding cofactors or substrate analogs in classifying protein function, information useful in using Thermofluor can assist in "decrypting" the function of proteins whose biochemical function might otherwise be unknown.

### Parallel thermal shift assays

Recent developments have extended thermal shift approaches to the analysis of ligand interactions in complex mixtures, including intact cells. Initial observations of individual proteins using fast parallel proteolysis (FastPP) showed that stabilization by ligand binding could impart resistance to proteolytic digestion with thermolysin. Protection relative to reference was quantified through either protein staining on gels or western blotting with a labeling antibody directed to a tag fused to the target protein. CETSA, for cellular thermal shift assay, is a method that monitors the stabilization effect of drug binding through the prevention of irreversible protein precipitation, which is usually initiated when a protein becomes thermally denatured. In CETSA, aliquots of cell lysate are transiently heated to different temperatures, following which samples are centrifuged to separate soluble fractions from precipitated proteins. The presence of the target protein in each soluble fraction is determined by western blotting and used to construct a CETSA melting curve that can inform regarding in vivo targeting, drug distribution, and bioavailability. Both FastPP and CETSA generally require antibodies to facilitate target detection, and consequently are generally used in contexts where the target identity is known a priori. Newer developments seek to merge aspects of FastPP and CETSA approaches, by assessing the ligand-dependent dependent proteolytic protection of targets in cells using mass spectroscopy (MS) to detect shifts in proteolysis patterns associated with protein stabilization. Present implementations still require a priori knowledge of expected targets to facilitate data analysis, but improvements in MS data collection strategies, together with the use of improved computational tools and database structures can potentially allow the approach to be used for de novo target decryption on the total cell proteome scale. This would be a major advance for drug discovery since it would allow the identification of discrete molecular targets (as well as off-target interactions) for drugs identified through high-content cellular or phenotypic drug screens.
