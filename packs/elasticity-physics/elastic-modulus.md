---
title: "Elastic modulus"
source: https://en.wikipedia.org/wiki/Elastic_modulus
domain: elasticity-physics
license: CC-BY-SA-4.0
tags: elasticity theory, hooke's law, young's modulus, shear modulus
fetched: 2026-07-02
---

# Elastic modulus

An **elastic modulus** is a quantity that describes an object's or substance's resistance to being deformed elastically (i.e., non-permanently) when a stress is applied to it.

## Definition

The elastic modulus of an object is defined as the slope of its stress–strain curve in the elastic deformation region; a stiffer material will have a higher elastic modulus. An elastic modulus has the form:

$\delta \ {\stackrel {\text{def}}{=}}\ {\frac {\text{stress}}{\text{strain}}}$

where *stress* is the force causing the deformation divided by the area to which the force is applied and *strain* is the ratio of the change in some parameter caused by the deformation to the original value of the parameter.

Since strain is a dimensionless quantity, the units of $\delta$ will be the same as the units of stress.

## Elastic constants and moduli

Elastic constants are specific parameters that quantify the stiffness of a material in response to applied stresses and are fundamental in defining the elastic properties of materials. These constants form the elements of the stiffness matrix in tensor notation, which relates stress to strain through linear equations in anisotropic materials. Commonly denoted as *Cijkl*, where *i*,*j*,*k*, and *l* are the coordinate directions, these constants are essential for understanding how materials deform under various loads.

## Types of elastic modulus

Specifying how stress and strain are to be measured, including directions, allows for many types of elastic moduli to be defined. The four primary ones are:

1. *Young's modulus* (*E*) describes tensile and compressive elasticity, or the tendency of an object to deform along an axis when opposing forces are applied along that axis; it is defined as the ratio of tensile stress to tensile strain. It is often referred to simply as the *elastic modulus*.
2. The *shear modulus* or *modulus of rigidity* (*G* or $\mu \,$ Lamé second parameter) describes an object's tendency to shear (the deformation of shape at constant volume) when acted upon by opposing forces; it is defined as shear stress over shear strain. The shear modulus is part of the derivation of viscosity.
3. The *bulk modulus* (*K*) describes volumetric elasticity, or the tendency of an object to deform in all directions when uniformly loaded in all directions; it is defined as volumetric stress over volumetric strain, and is the inverse of compressibility. The bulk modulus is an extension of Young's modulus to three dimensions.
4. *Flexural modulus* (*E*flex) describes the object's tendency to flex when acted upon by a moment.

Two other elastic moduli are Lamé's first parameter, *λ,* and P-wave modulus, *M*, as used in table of modulus comparisons given below references. Homogeneous and isotropic (similar in all directions) materials (solids) have their (linear) elastic properties fully described by two elastic moduli, and one may choose any pair. Given a pair of elastic moduli, all other elastic moduli can be calculated according to formulas in the table below at the end of page.

Fluids at rest are special in that they cannot support shear stress, meaning that the shear modulus is always zero. This also implies that Young's modulus for this group is always zero. When moving relative to a solid surface a fluid will experience shear stresses adjacent to the surface, giving rise to the phenomenon of viscosity.

In some texts, the modulus of elasticity is referred to as the *elastic constant*, while the inverse quantity is referred to as *elastic modulus*.

## Density functional theory calculation

Density functional theory (DFT) provides reliable methods for determining several forms of elastic moduli that characterise distinct features of a material's reaction to mechanical stresses. Utilize DFT software such as VASP, Quantum ESPRESSO, or ABINIT. Overall, conduct tests to ensure that results are independent of computational parameters such as the density of the k-point mesh, the plane-wave cutoff energy, and the size of the simulation cell.

1. Young's modulus (*E*) - apply small, incremental changes in the lattice parameter along a specific axis and compute the corresponding stress response using DFT. Young's modulus is then calculated as *E*=*σ*/*ϵ*, where *σ* is the stress and *ϵ* is the strain.
  1. Initial structure: Start with a relaxed structure of the material. All atoms should be in a state of minimum energy (i.e., minimum energy state with zero forces on atoms) before any deformations are applied.
  2. Incremental uniaxial strain: Apply small, incremental strains to the crystal lattice along a particular axis. This strain is usually uniaxial, meaning it stretches or compresses the lattice in one direction while keeping other dimensions constant or periodic.
  3. Calculate stresses: For each strained configuration, run a DFT calculation to compute the resulting stress tensor. This involves solving the Kohn-Sham equations to find the ground state electron density and energy under the strained conditions
  4. Stress-strain curve: Plot the calculated stress versus the applied strain to create a stress-strain curve. The slope of the initial, linear portion of this curve gives Young's modulus. Mathematically, Young's modulus *E* is calculated using the formula *E*=*σ*/*ϵ*, where *σ* is the stress and *ϵ* is the strain.
2. Shear modulus (*G*)
  1. Initial structure: Start with a relaxed structure of the material. All atoms should be in a state of minimum energy with no residual forces. (i.e., minimum energy state with zero forces on atoms) before any deformations are applied.
  2. Shear strain application: Apply small increments of shear strain to the material. Shear strains are typically off-diagonal components in the strain tensor, affecting the shape but not the volume of the crystal cell.
  3. Stress calculation: For each configuration with applied shear strain, perform a DFT calculation to determine the resulting stress tensor.
  4. Shear stress vs. shear strain curve: Plot the calculated shear stress against the applied shear strain for each increment. The slope of the stress-strain curve in its linear region provides the shear modulus, *G*=*τ*/*γ*, where *τ* is the shear stress and *γ* is the applied shear strain.
3. Bulk modulus (*K*)
  1. Initial structure: Start with a relaxed structure of the material. It's crucial that the material is fully optimized, ensuring that any changes in volume are purely due to applied pressure.
  2. Volume changes: Incrementally change the volume of the crystal cell, either compressing or expanding it. This is typically done by uniformly scaling the lattice parameters.
  3. Calculate pressure: For each altered volume, perform a DFT calculation to determine the pressure required to maintain that volume. DFT allows for the calculation of stress tensors which provide a direct measure of the internal pressure.
  4. Pressure-volume curve: Plot the applied pressure against the resulting volume change. The bulk modulus can be calculated from the slope of this curve in the linear elastic region. The bulk modulus is defined as *K*=−*VdV*/*dP*, where *V* is the original volume, *dP* is the change in pressure, and *dV* is the change in volume.
