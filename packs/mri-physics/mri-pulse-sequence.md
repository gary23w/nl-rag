---
title: "MRI pulse sequence"
source: https://en.wikipedia.org/wiki/MRI_pulse_sequence
domain: mri-physics
license: CC-BY-SA-4.0
tags: magnetic resonance imaging, mri physics, spin relaxation, pulse sequence
fetched: 2026-07-02
---

# MRI pulse sequence

An **MRI pulse sequence** in magnetic resonance imaging (MRI) is a particular setting of pulse sequences and pulsed field gradients, resulting in a particular image appearance.

A multiparametric MRI is a combination of two or more sequences, and/or including other specialized MRI configurations such as spectroscopy.

## Overview table

This table does not include uncommon and experimental sequences.

| Group | Sequence | Abbr. | Physics | Main clinical distinctions | Example |
|---|---|---|---|---|---|
| Spin echo | T1 weighted | **T1** | Measuring spin–lattice relaxation by using a short repetition time (TR) and echo time (TE). | Lower signal for more water content, as in edema, tumor, infarction, inflammation, infection, hyperacute or chronic hemorrhage. High signal for fat High signal for paramagnetic substances, such as MRI contrast agents Standard foundation and comparison for other sequences |   |
| T2 weighted | **T2** | Measuring spin–spin relaxation by using long TR and TE times | Higher signal for more water content Low signal for fat in standard Spine Echo (SE), though not with Fast Spin Echo/Turbo Spin Echo (FSE/TSE). FSE/TSE is the standard of care in modern medicine because it is faster. With FSE/TSE, fat has high signal due to disruption of hyperfine J-coupling between adjacent fat protons. Low signal for paramagnetic substances Standard foundation and comparison for other sequences |   |   |
| Proton density weighted | **PD** | Long TR (to reduce T1) and short TE (to minimize T2). | Joint disease and injury. High signal from meniscus tears. (pictured) |   |   |
| Gradient echo (GRE) | Steady-state free precession | **SSFP** | Maintenance of a steady, residual transverse magnetisation over successive cycles. | Creation of cardiac MRI videos (pictured). |   |
| Effective T2 or "T2-star" | **T2*** | Spoiled gradient recalled echo (GRE) with a long echo time and small flip angle | Low signal from hemosiderin deposits (pictured) and hemorrhages. |   |   |
| Susceptibility-weighted | **SWI** | Spoiled gradient recalled echo (GRE), fully flow compensated, long echo time, combines phase image with magnitude image | Detecting small amounts of hemorrhage (diffuse axonal injury pictured) or calcium. |   |   |
| Inversion recovery | Short tau inversion recovery | **STIR** | Fat suppression by setting an inversion time where the signal of fat is zero. | High signal in edema, such as in more severe stress fracture. Shin splints pictured: |   |
| Fluid-attenuated inversion recovery | **FLAIR** | Fluid suppression by setting an inversion time that nulls fluids | High signal in lacunar infarction, multiple sclerosis (MS) plaques, subarachnoid haemorrhage and meningitis (pictured). |   |   |
| Double inversion recovery | **DIR** | Simultaneous suppression of cerebrospinal fluid and white matter by two inversion times. | High signal of multiple sclerosis plaques (pictured). |   |   |
| Diffusion weighted (**DWI**) | Conventional | **DWI** | Measure of Brownian motion of water molecules. | High signal within minutes of cerebral infarction (pictured). |   |
| Apparent diffusion coefficient | **ADC** | Reduced T2 weighting by taking multiple conventional DWI images with different DWI weighting, and the change corresponds to diffusion. | Low signal minutes after cerebral infarction (pictured). |   |   |
| Diffusion tensor | **DTI** | Mainly tractography (pictured) by an overall greater Brownian motion of water molecules in the directions of nerve fibers. | Evaluating white matter deformation by tumors Reduced fractional anisotropy may indicate dementia. |   |   |
| Perfusion weighted (**PWI**) | Dynamic susceptibility contrast | **DSC** | Measures changes over time in susceptibility-induced signal loss due to gadolinium contrast injection. | Provides measurements of blood flow In cerebral infarction, the infarcted core and the penumbra have decreased perfusion and delayed contrast arrival (pictured). |   |
| Arterial spin labelling | **ASL** | Magnetic labeling of arterial blood below the imaging slab, which subsequently enters the region of interest. It does not need gadolinium contrast. |   |   |   |
| Dynamic contrast enhanced | **DCE** | Measures changes over time in the shortening of the spin–lattice relaxation (T1) induced by a gadolinium contrast bolus. | Faster Gd contrast uptake along with other features is suggestive of malignancy (pictured). |   |   |
| Functional MRI (**fMRI**) | Blood-oxygen-level dependent imaging | **BOLD** | Changes in oxygen saturation-dependent magnetism of hemoglobin reflects tissue activity. | Localizing brain activity from performing an assigned task (e.g. talking, moving fingers) before surgery, also used in research of cognition. |   |
| Magnetic resonance angiography (**MRA**) and venography | Time-of-flight | **TOF** | Blood entering the imaged area is not yet magnetically saturated, giving it a much higher signal when using short echo time and flow compensation. | Detection of aneurysm, stenosis, or dissection |   |
| Phase-contrast magnetic resonance imaging | **PC-MRA** | Two gradients with equal magnitude, but opposite direction, are used to encode a phase shift, which is proportional to the velocity of spins. | Detection of aneurysm, stenosis, or dissection (pictured). | (VIPR) |   |

## Spin echo

### T1 and T2

Each tissue returns to its equilibrium state after excitation by the independent relaxation processes of T1 (spin-lattice; that is, magnetization in the same direction as the static magnetic field) and T2 (spin-spin; transverse to the static magnetic field). To create a T1-weighted image, magnetization is allowed to recover before measuring the MR signal by changing the repetition time (TR). This image weighting is useful for assessing the cerebral cortex, identifying fatty tissue, characterizing focal liver lesions, and in general, obtaining morphological information, as well as for post-contrast imaging. To create a T2-weighted image, magnetization is allowed to decay before measuring the MR signal by changing the echo time (TE). This image weighting is useful for detecting edema and inflammation, revealing white matter lesions, and assessing zonal anatomy in the prostate and uterus.

The standard display of MRI images is to represent fluid characteristics in black and white images, where different tissues turn out as follows:

| Signal | T1-weighted | T2-weighted |
|---|---|---|
| **High** | Fat Subacute hemorrhage Melanin Protein-rich fluid Slowly flowing blood Paramagnetic substances, such as gadolinium, manganese, copper Cortical pseudolaminar necrosis | More water content, as in edema, tumor, infarction, inflammation and infection Extracellularly located methemoglobin in subacute hemorrhage |
| **Inter- mediate** | Grey matter darker than white matter | White matter darker than grey matter |
| **Low** | Bone Urine CSF Air More water content, as in edema, tumor, infarction, inflammation, infection, hyperacute or chronic hemorrhage Low proton density as in calcification | Bone Air Fat Low proton density, as in calcification and fibrosis Paramagnetic material, such as deoxyhemoglobin, intracellular methemoglobin, iron, ferritin, hemosiderin, melanin Protein-rich fluid |

### Proton density

Proton density (PD)- weighted images are created by having a long repetition time (TR) and a short echo time (TE). On images of the brain, this sequence has a more pronounced distinction between grey matter (bright) and white matter (darker grey), but with little contrast between brain and CSF. It is very useful for the detection of arthropathy and injury.

## Gradient echo

A *gradient echo sequence* does not use a 180 degrees RF pulse to make the spins of particles coherent. Instead, it uses magnetic gradients to manipulate the spins, allowing the spins to dephase and rephase when required. After an excitation pulse, the spins are dephased, no signal is produced because the spins are not coherent. When the spins are rephased, they become coherent, and thus signal (or "echo") is generated to form images. Unlike spin echo, gradient echo does not need to wait for transverse magnetisation to decay completely before initiating another sequence, thus it requires very short repetition times (TR), and therefore to acquire images in a short time. After echo is formed, some transverse magnetisations remains. Manipulating gradients during this time will produce images with different contrast. There are three main methods of manipulating contrast at this stage, namely steady-state free-precession (SSFP) that does not spoil the remaining transverse magnetisation, but attempts to recover them (thus producing T2-weighted images); the sequence with spoiler gradient that averages the transverse magnetisations (thus producing mixed T1 and T2-weighted images), and RF spoiler that vary the phases of RF pulse to eliminates the transverse magnetisation, thus producing pure T1-weighted images.

For comparison purposes, the repetition time of a gradient echo sequence is of the order of 3 milliseconds, versus about 30 ms of a spin echo sequence.

## Inversion recovery

**Inversion recovery** is an MRI sequence that provides high contrast between tissue and lesion. It can be used to provide high T1 weighted image, high T2 weighted image, and to suppress the signals from fat, blood, or cerebrospinal fluid (CSF).

## Diffusion weighted

Diffusion MRI measures the diffusion of water molecules in biological tissues. Clinically, diffusion MRI is useful for the diagnoses of conditions (e.g., stroke) or neurological disorders (e.g., multiple sclerosis), and helps better understand the connectivity of white matter axons in the central nervous system. In an isotropic medium (inside a glass of water for example), water molecules naturally move randomly according to turbulence and Brownian motion. In biological tissues however, where the Reynolds number is low enough for laminar flow, the diffusion may be anisotropic. For example, a molecule inside the axon of a neuron has a low probability of crossing the myelin membrane. Therefore, the molecule moves principally along the axis of the neural fiber. If it is known that molecules in a particular voxel diffuse principally in one direction, the assumption can be made that the majority of the fibers in this area are parallel to that direction.

The recent development of diffusion tensor imaging (DTI) enables diffusion to be measured in multiple directions, and the fractional anisotropy in each direction to be calculated for each voxel. This enables researchers to make brain maps of fiber directions to examine the connectivity of different regions in the brain (using tractography) or to examine areas of neural degeneration and demyelination in diseases like multiple sclerosis.

Another application of diffusion MRI is diffusion-weighted imaging (DWI). Following an ischemic stroke, DWI is highly sensitive to the changes occurring in the lesion. It is speculated that increases in restriction (barriers) to water diffusion, as a result of cytotoxic edema (cellular swelling), is responsible for the increase in signal on a DWI scan. The DWI enhancement appears within 5–10 minutes of the onset of stroke symptoms (as compared to computed tomography, which often does not detect changes of acute infarct for up to 4–6 hours) and remains for up to two weeks. Coupled with imaging of cerebral perfusion, researchers can highlight regions of "perfusion/diffusion mismatch" that may indicate regions capable of salvage by reperfusion therapy.

Like many other specialized applications, this technique is usually coupled with a fast image acquisition sequence, such as echo planar imaging sequence.

## Perfusion weighted

*Perfusion-weighted imaging* (PWI) is performed by 3 main techniques:

- Dynamic susceptibility contrast (DSC): Gadolinium contrast is injected, and rapid repeated imaging (generally gradient-echo echo-planar T2 weighted) quantifies susceptibility-induced signal loss.
- Dynamic contrast enhanced (DCE): Measuring shortening of the spin–lattice relaxation (T1) induced by a gadolinium contrast bolus.
- Arterial spin labelling (ASL): Magnetic labeling of arterial blood below the imaging slab, without the need of gadolinium contrast.

The acquired data is then postprocessed to obtain perfusion maps with different parameters, such as BV (blood volume), BF (blood flow), MTT (mean transit time) and TTP (time to peak).

In cerebral infarction, the penumbra has decreased perfusion. Another MRI sequence, diffusion-weighted MRI, estimates the amount of tissue that is already necrotic, and the combination of those sequences can therefore be used to estimate the amount of brain tissue that is salvageable by thrombolysis and/or thrombectomy.

## Functional MRI

Functional MRI (fMRI) measures signal changes in the brain that are due to changing neural activity. It is used to understand how different parts of the brain respond to external stimuli or passive activity in a resting state, and has applications in behavioral and cognitive research, and in planning neurosurgery of eloquent brain areas. Researchers use statistical methods to construct a 3-D parametric map of the brain indicating the regions of the cortex that demonstrate a significant change in activity in response to the task. Compared to anatomical T1W imaging, the brain is scanned at lower spatial resolution but at a higher temporal resolution (typically once every 2–3 seconds). Increases in neural activity cause changes in the MR signal via *T** 2 changes; this mechanism is referred to as the BOLD (blood-oxygen-level dependent) effect. Increased neural activity causes an increased demand for oxygen, and the vascular system actually overcompensates for this, increasing the amount of oxygenated hemoglobin relative to deoxygenated hemoglobin. Because deoxygenated hemoglobin attenuates the MR signal, the vascular response leads to a signal increase that is related to the neural activity. The precise nature of the relationship between neural activity and the BOLD signal is a subject of current research. The BOLD effect also allows for the generation of high resolution 3D maps of the venous vasculature within neural tissue.

While BOLD signal analysis is the most common method employed for neuroscience studies in human subjects, the flexible nature of MR imaging provides means to sensitize the signal to other aspects of the blood supply. Alternative techniques employ arterial spin labeling (ASL) or weighting the MRI signal by cerebral blood flow (CBF) and cerebral blood volume (CBV). The CBV method requires injection of a class of MRI contrast agents that are now in human clinical trials. Because this method has been shown to be far more sensitive than the BOLD technique in preclinical studies, it may potentially expand the role of fMRI in clinical applications. The CBF method provides more quantitative information than the BOLD signal, albeit at a significant loss of detection sensitivity.

## Magnetic resonance angiography

Magnetic resonance angiography (*MRA*) is a group of techniques based to image blood vessels. Magnetic resonance angiography is used to generate images of arteries (and less commonly veins) in order to evaluate them for stenosis (abnormal narrowing), occlusions, aneurysms (vessel wall dilatations, at risk of rupture) or other abnormalities. MRA is often used to evaluate the arteries of the neck and brain, the thoracic and abdominal aorta, the renal arteries, and the legs (the latter exam is often referred to as a "run-off").

### Phase contrast

Phase contrast MRI (PC-MRI) is used to measure flow velocities in the body. It is used mainly to measure blood flow in the heart and throughout the body. PC-MRI may be considered a method of magnetic resonance velocimetry. Since modern PC-MRI typically is time-resolved, it also may be referred to as 4-D imaging (three spatial dimensions plus time).

## Susceptibility weighted imaging

Susceptibility-weighted imaging (SWI) is a new type of contrast in MRI different from spin density, *T*1, or *T*2 imaging. This method exploits the susceptibility differences between tissues and uses a fully velocity-compensated, three-dimensional, RF-spoiled, high-resolution, 3D-gradient echo scan. This special data acquisition and image processing produces an enhanced contrast magnitude image very sensitive to venous blood, hemorrhage and iron storage. It is used to enhance the detection and diagnosis of tumors, vascular and neurovascular diseases (stroke and hemorrhage), multiple sclerosis, Alzheimer's, and also detects traumatic brain injuries that may not be diagnosed using other methods.

## Magnetization transfer

Magnetization transfer (MT) is a technique to enhance image contrast in certain applications of MRI.

Bound protons are associated with proteins and as they have a very short T2 decay they do not normally contribute to image contrast. However, because these protons have a broad resonance peak they can be excited by a radiofrequency pulse that has no effect on free protons. Their excitation increases image contrast by transfer of saturated spins from the bound pool into the free pool, thereby reducing the signal of free water. This homonuclear magnetization transfer provides an indirect measurement of macromolecular content in tissue. Implementation of homonuclear magnetization transfer involves choosing suitable frequency offsets and pulse shapes to saturate the bound spins sufficiently strongly, within the safety limits of specific absorption rate for MRI.

The most common use of this technique is for suppression of background signal in time of flight MR angiography. There are also applications in neuroimaging particularly in the characterization of white matter lesions in multiple sclerosis.

## Fat suppression

Fat suppression is useful for example to distinguish active inflammation in the intestines from fat deposition such as can be caused by long-standing (but possibly inactive) inflammatory bowel disease, but also obesity, chemotherapy and celiac disease. Without fat suppression techniques, fat and fluid will have similar signal intensities on fast spin-echo sequences.

Techniques to suppress fat on MRI mainly include:

- Identifying fat by the chemical shift of its atoms, causing different time-dependent phase shifts compared to water.
- Frequency-selective saturation of the spectral peak of fat by a "fat sat" pulse before imaging.
- Short tau inversion recovery (STIR), a T1-dependent method
- Spectral presaturation with inversion recovery (SPIR)

## Neuromelanin imaging

This method exploits the paramagnetic properties of neuromelanin and can be used to visualize the substantia nigra and the locus coeruleus. It is used to detect the atrophy of these nuclei in Parkinson's disease and other parkinsonisms, and also detects signal intensity changes in major depressive disorder and schizophrenia.

## Uncommon and experimental sequences

The following sequences are not commonly used clinically, and/or are at an experimental stage.

### T1 rho (T1ρ)

T1 rho (T1ρ) is an experimental MRI sequence that may be used in musculoskeletal imaging. It does not yet have widespread use.

Molecules have a kinetic energy that is a function of the temperature and is expressed as translational and rotational motions, and by collisions between molecules. The moving dipoles disturb the magnetic field but are often extremely rapid so that the average effect over a long time-scale may be zero. However, depending on the time-scale, the interactions between the dipoles do not always average away. At the slowest extreme the interaction time is effectively infinite and occurs where there are large, stationary field disturbances (e.g., a metallic implant). In this case the loss of coherence is described as a "static dephasing". T2* is a measure of the loss of coherence in an ensemble of spins that includes all interactions (including static dephasing). T2 is a measure of the loss of coherence that excludes static dephasing, using an RF pulse to reverse the slowest types of dipolar interaction. There is in fact a continuum of interaction time-scales in a given biological sample, and the properties of the refocusing RF pulse can be tuned to refocus more than just static dephasing. In general, the rate of decay of an ensemble of spins is a function of the interaction times and also the power of the RF pulse. This type of decay, occurring under the influence of RF, is known as T1ρ. It is similar to T2 decay but with some slower dipolar interactions refocused, as well as static interactions, hence T1ρ≥T2.

### Others

- *Saturation recovery sequences* are rarely used, but can measure spin-lattice relaxation time (T1) more quickly than an inversion recovery pulse sequence.
- *Double-oscillating-diffusion-encoding* (DODE) and *double diffusion encoding* (DDE) imaging are specific forms of MRI diffusion imaging, which can be used to measure diameters and lengths of axon pores.
