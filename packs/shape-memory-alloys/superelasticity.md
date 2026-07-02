---
title: "Pseudoelasticity"
source: https://en.wikipedia.org/wiki/Superelasticity
domain: shape-memory-alloys
license: CC-BY-SA-4.0
tags: shape-memory alloy, nitinol material, superelasticity effect, martensite phase
fetched: 2026-07-02
---

# Pseudoelasticity

(Redirected from

Superelasticity

)

In materials science, **pseudoelasticity**, sometimes called **superelasticity**, is an elastic (reversible) response to an applied stress, caused by a phase transformation between the austenitic and martensitic phases of a crystal. It is exhibited in shape-memory alloys.

## Overview

Pseudoelasticity is from the reversible motion of domain boundaries during the phase transformation, rather than just bond stretching or the introduction of defects in the crystal lattice (thus it is not true superelasticity but rather pseudoelasticity). Even if the domain boundaries do become pinned, they may be reversed through heating. Thus, a pseudoelastic material may return to its previous shape (hence, *shape memory*) after the removal of even relatively high applied strains. One special case of pseudoelasticity is called the Bain Correspondence. This involves the austenite/martensite phase transformation between a face-centered crystal lattice (FCC) and a body-centered tetragonal crystal structure (BCT).

This behavior differs fundamentally from ordinary elasticity and plasticity:

- Ordinary elasticity**:** In a normal metal or material under elastic load, deformation is *reversible* but typically limited to small strains (e.g. <0.2% for many metals). Elastic deformation arises from slight changes in interatomic spacing or bond stretching, and no permanent defects are introduced.
- Plasticity: If stress exceeds the yield strength, plastic deformation occurs via mechanisms like dislocation slip or twinning, causing permanent lattice defects. Plastic strain is *irreversible* – the material will not return to its exact original shape when the load is removed.
- Superelasticity: A superelastic material can reversibly accommodate far larger strains (several percent) than ordinary elasticity allows. Instead of yielding plastically, the material undergoes a *phase transformation* under stress. For example, NiTi (Nitinol) can deform up to ~8–10% strain and fully recover upon unloading. This is an *elastic-like* behavior but achieved by phase change rather than just bond stretching – hence the term “pseudoelastic.”

Superelastic alloys belong to the larger family of shape-memory alloys. When mechanically loaded, a superelastic alloy deforms reversibly to very high strains (up to 10%) by the creation of a stress-induced phase. When the load is removed, the new phase becomes unstable and the material regains its original shape. Unlike shape-memory alloys, no change in temperature is needed for the alloy to recover its initial shape.

Superelastic devices take advantage of their large, reversible deformation and include antennas, eyeglass frames, and biomedical stents.

## Pseudoelasticity of nickel titanium (Nitinol)

Superelasticity is most famously exhibited by shape-memory alloys (SMAs) such as nickel-titanium (NiTi), also known as Nitinol.

The key points of the mechanism for Nitinol are:

- **Austenite to Martensite Transformation**: At temperatures above $A_{f}$ , NiTi is fully in the austenite phase at rest. When a sufficient mechanical stress is applied, the alloy begins to transform into martensite at constant temperature (hence *isothermal* transformation). This stress-induced martensite formation is often called SIM (stress-induced martensite).
- **Reversible Transformation:** The martensitic phase can accommodate deformation by twinning (reorienting its lattice in a shear-like manner without major slip). As a result, the material can deform significantly (several percent strain) as austenite transforms to martensite. Crucially, this martensitic transformation is *thermoelastic* and reversible. When the applied stress is removed, the martensite becomes unstable (since the material is still above $A_{f}$ ) and it **reverts back to austenite**, thereby recovering the strain. The material essentially “un-transforms” back to the original phase and shape.
- **No Temperature Change Needed for Recovery:** Unlike the classic shape memory effect (SME), which requires heating to recover shape, **superelasticity needs no temperature change**. The reverse transformation (martensite to austenite) happens upon unloading alone.
- **Temperature Window :** For a given SMA composition, superelasticity is observed in a finite temperature range. The lower end is just above $A_{f}$ (so the alloy starts in austenite). The upper end is often denoted $M_{d}$ (the temperature above which martensite cannot be stress-induced). For NiTi, $M_{d}$ is typically about ~40 °C above **$A_{f}$ .** Within this window, applied stress can induce martensite; above $M_{d}$ , the austenite is so stable that only plastic yielding (slip) occurs under load.

## Stress–strain behavior and characteristics

The stress–strain curve of a superelastic alloy (like NiTi) has a distinctive shape, reflecting the sequence of phase transformations during loading and unloading

### Loading

During loading, three regimes are observed

1. **Elastic Austenite:** At small strains , the material responds with ordinary elastic behavior as austenite. Stress rises approximately linearly with strain ( $\sigma =E\epsilon$ ) up to the point where the martensitic transformation begins. The end of this stage is around the Martensite-Start strain $\epsilon _{Mf}$ (corresponding to a stress $\sigma _{Ms}$ ). For NiTi, this might be on the order of ~0.5–1% strain and a few hundred MPa of stress.
2. **Stress Plateau – Martensitic Transformation:** Once the stress is high enough to trigger martensite nucleation, the stress remains roughly constant over a considerable strain interval. In this plateau region, additional strain is being accommodated not by increasing stress (much), but by the progressive conversion of austenite to martensite (phase transformation). The plateau stress level is often around 400–600 MPa in NiTi (depending on alloy/process), and the plateau strain range can span 5–8% strain
3. **Elastic Martensite & Hardening:** Once the transformation to martensite is almost complete (at Martensite-Finish strain $\epsilon _{Mf}$ ), further strain requires deforming the martensite itself or aligning the last remaining variants. The stress begins to rise steeply again with strain. Martensite’s elastic modulus may differ from austenite’s (often somewhat lower), but the curve climbs until ultimate stress/strain or until the loading is stopped. If the material is loaded to a high strain (beyond the transformation strain), some plastic deformation of martensite can also occur, which would manifest as deviation from full strain recovery later

Mathematically, an **idealized piecewise model** for the superelastic loading curve can be written as:

$\sigma (\epsilon )={\begin{cases}E\epsilon &{\text{if }}\epsilon <\epsilon _{Ms}\\\sigma _{Ms}+\alpha (\epsilon -\epsilon _{Ms})&{\text{if }}\epsilon _{Ms}<\epsilon <\epsilon _{Mf}\\\sigma _{Ms}+E(\epsilon -\epsilon _{Mf}+\epsilon _{Ms})&{\text{if }}\epsilon _{Mf}<\epsilon \end{cases}}$ where $\sigma$ is the stress, $\epsilon$ is the strain, E is the Young's modulus, $\epsilon _{Ms}$ and $\epsilon _{Mf}$ are the start and finish strains for the martensitic transformation, $\sigma _{Ms}$ is the stress at the start of the martensitic transformation, and $\alpha$ is a material parameter.

In an ideal case, $\alpha \approx 0$ so the stress plateau is flat (perfectly constant stress during phase change). For simplicity, the above model assumes the transformation finish stress $\sigma _{Mf}=\sigma _{Ms}$ (flat plateau).

### Unloading

On unloading, the reverse sequence occurs, but importantly at a lower stress level. As soon as the load is released from the fully martensitic state, the material unloads elastically in martensite briefly, then enters a reverse transformation plateau (martensite reverts to austenite) at a stress $\sigma _{As}$ which is below $\sigma _{Ms}$ . Finally, once all martensite has turned back to austenite (at $\sigma _{Af}$ ), the last part of unloading is just elastic recovery of austenite. Thus, the unloading curve is shifted down relative to loading. The result is a hysteresis loop in the stress–strain diagram. The area inside this loop represents the energy dissipated per cycle (as heat) due to internal friction and phase transformation entropy change.

## Size effects

Recently, there have been interests of discovering materials exhibiting superelasticity in nanoscale for MEMS (Microelectromechanical systems) application. The ability to control the martensitic phase transformation has already been reported. But the behavior of superelasticity has been observed to have size effects in nanoscale.

Qualitatively speaking, superelasticity is the reversible deformation by phase transformation. Therefore, it competes with the irreversible plastic deformation by dislocation motion. At nanoscale, the dislocation density and possible Frank–Read source sites are greatly reduced, so the yield stress is increased with reduced size. Therefore, for materials exhibiting superelasticity behavior in nanoscale, it has been found that they can operate in long-term cycling with little detrimental evolution. On the other hand, the critical stress for martensitic phase transformation to occur is also increased because of the reduced possible sites for nucleation to begin. Nucleation usually begins near dislocation or at surface defects. But for nanoscale materials, the dislocation density is greatly reduced, and the surface is usually atomically smooth. Therefore, the phase transformation of nanoscale materials exhibiting superelasticity is usually found to be homogeneous, resulting in much higher critical stress. Specifically, for Zirconia, where it has three phases, the competition between phase transformation and plastic deformation has been found to be orientation dependent, indicating the orientation dependence of activation energy of dislocation and nucleation. Therefore, for nanoscale materials suitable for superelasticity, one should research on the optimized crystal orientation and surface roughness for most enhanced superelasticity effect.

## Applications

### Biomedical stents and medical devices

One of the most celebrated uses of superelastic NiTi is in self-expanding stents for cardiovascular surgery. A NiTi stent can be crimped and inserted into a blood vessel, once released at body temperature, it springs back to a larger diameter to prop the vessel open. The superelastic effect allows the stent to apply a consistent outward force over a range of deformations and to resist kinking.

### Eyeglass frames and consumer products

Eyewear frames made of NiTi (or Cu-based SMAs) can be bent dramatically (e.g. twisted or sat on) and will recover their original shape. This durability has made flexible “memory metal” glasses a popular consumer product. Similarly, some high-end sports equipment and cell phone antennas have used superelastic alloys to withstand deformation.

### Aerospace and morphing structures

The aerospace industry exploits superelasticity for lightweight, adaptive components. Superelastic actuators and damping links can be used in deployable structures or morphing wings. For instance, a superelastic SMA rod or tendon can act as a passive actuator that accommodates deformation when a certain load is reached (protecting structures by “giving” and then springing back). Landing gear and aircraft engine components have been explored that utilize NiTi inserts to absorb impact or vibration and then self-center. The high energy absorption per unit volume and the ability to sustain cyclic deformation make superelastic alloys appealing for these purposes.

In satellite applications, temperature-controlled SMA elements (combining superelasticity and shape-memory effect) are used for deployable antennas and solar panels, thanks to their reliability and compactness.
