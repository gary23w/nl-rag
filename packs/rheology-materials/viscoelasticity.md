---
title: "Viscoelasticity"
source: https://en.wikipedia.org/wiki/Viscoelasticity
domain: rheology-materials
license: CC-BY-SA-4.0
tags: viscoelasticity, shear stress, flow behavior, storage modulus
fetched: 2026-07-02
---

# Viscoelasticity

**Viscoelasticity** is a material property that combines both viscous and elastic characteristics. Many materials have such viscoelastic properties, especially materials that consist of large molecules. Polymers are viscoelastic because their macromolecules can have temporary entanglements with neighbouring molecules, causing elastic properties. After some time these entanglements disappear and the macromolecules flow into other positions where new entanglements occur (viscous properties).

A viscoelastic material shows elastic properties on short time scales and viscous properties on long time scales. These materials exhibit behavior that depends on the time and rate of applied forces, allowing them to both store and dissipate energy.

Viscoelasticity has been studied since the 19th century by researchers such as James Clerk Maxwell, Ludwig Boltzmann, and Lord Kelvin.

Several models are available for the mathematical description of the viscoelastic properties of a substance:

- Constitutive models of linear viscoelasticity assume a linear relationship between stress and strain. These models are valid for relatively small deformations only.
- Constitutive models of non-linear viscoelasticity are based on a more realistic non-linear relationship between stress and strain. These models are valid for relatively large deformations.

The viscoelastic properties of polymers are highly temperature dependent. From low to high temperature the material can be in the glass phase, rubber phase or the melt phase. These phases have a very strong effect on the mechanical and viscous properties of the polymers.

Typical viscoelastic properties are:

- A time dependant stress in the polymer under constant deformation (strain).
- A time dependant strain in the polymer under constant stress.
- A time and temperature dependant stiffness of the polymer.
- Viscous energy loss during deformation of the polymer in the glass or rubber phase (hysteresis).
- A strain rate dependant viscosity of the molten polymer.
- An ongoing deformation of a polymer in the glass phase at constant load (creep).

The viscoelasticity properties are measured with various techniques, such as tensile testing, dynamic mechanical analysis, shear rheometry and extensional rheometry.

## Background

In the nineteenth century, physicists such as James Clerk Maxwell, Ludwig Boltzmann, and Lord Kelvin researched and experimented with creep and recovery of glasses, metals, and rubbers. Viscoelasticity was further examined in the late twentieth century when synthetic polymers were engineered and used in a variety of applications.

Viscoelasticity calculations depend heavily on the viscosity variable, *η*. The inverse of *η* is also known as fluidity, *φ*. The value of either can be derived as a function of temperature or as a given value (i.e. for a dashpot).

Depending on the change of strain rate versus stress inside a material, the viscosity can be categorized as having a linear, non-linear, or plastic response:

- When a material exhibits a linear response it is categorized as a Newtonian material. In this case the stress is linearly proportional to the strain rate.
- If the material exhibits a non-linear response to the strain rate, it is categorized as non-Newtonian fluid.
- There is also an interesting case where the viscosity decreases as the shear/strain rate remains constant. A material which exhibits this type of behavior is known as thixotropic.
- In addition, when the stress is independent of this strain rate, the material exhibits plastic deformation. Many viscoelastic materials exhibit rubber like behavior explained by the thermodynamic theory of polymer elasticity.

Some examples of viscoelastic materials are amorphous polymers, semicrystalline polymers, biopolymers, metals at very high temperatures, and bitumen materials. Cracking occurs when the strain is applied quickly and outside of the elastic limit. Ligaments and tendons in the human body are viscoelastic, so the extent of the potential damage to them depends on both the rate of the change of their length and the force applied.

A viscoelastic material has the following properties:

- hysteresis is seen in the stress–strain curve
- stress relaxation occurs: step constant strain causes decreasing stress
- creep occurs: step constant stress causes increasing strain
- its stiffness depends on the strain rate ${\dot {\varepsilon }}$ or the stress rate ${\dot {\sigma }}$

## Elastic versus viscoelastic behavior

Unlike purely elastic substances, a viscoelastic substance has an elastic component and a viscous component. The viscosity of a viscoelastic substance gives the substance a strain rate dependence on time. Purely elastic materials do not dissipate energy (heat) when a load is applied, then removed. However, a viscoelastic substance dissipates energy when a load is applied, then removed. Hysteresis is observed in the stress–strain curve, with the area of the loop being equal to the energy lost during the loading cycle. Since viscosity is the resistance to thermally activated plastic deformation, a viscous material loses energy through a loading cycle. Plastic deformation results in lost energy, which is uncharacteristic of a purely elastic material's reaction to a loading cycle.

Specifically, viscoelasticity is a molecular rearrangement. When a stress is applied to a viscoelastic material such as a polymer, parts of the long polymer chain change positions. This movement or rearrangement is called creep. Polymers remain a solid material even when these parts of their chains are rearranging to accommodate the stress, and as this occurs, it creates a back stress in the material. When the back stress is the same magnitude as the applied stress, the material no longer creeps. When the original stress is taken away, the accumulated back stresses causes the polymer to return to its original form. The material creeps, which gives the prefix visco-, and the material fully recovers, which gives the suffix -elasticity.

## Linear viscoelasticity and nonlinear viscoelasticity

**Linear viscoelasticity** is behavior in which the function is separable in both creep response and load. All linear viscoelastic models can be represented by a Volterra equation connecting stress and strain: $\varepsilon (t)={\frac {\sigma (t)}{E_{\text{inst,creep}}}}+\int _{0}^{t}K(t-t'){\dot {\sigma }}(t')dt'$ or $\sigma (t)=E_{\text{inst,relax}}\varepsilon (t)+\int _{0}^{t}F(t-t'){\dot {\varepsilon }}(t')dt'$ where

- t is time
- $\sigma (t)$ is stress
- $\varepsilon (t)$ is strain
- $E_{\text{inst,creep}}$ and $E_{\text{inst,relax}}$ are instantaneous elastic moduli for creep and relaxation
- *K*(*t*) is the creep function
- *F*(*t*) is the relaxation function

Linear viscoelasticity is usually applicable only for small deformations.

In **nonlinear viscoelasticity**, the function is not separable. It usually happens when the deformations are large or if the material changes its properties under deformations. Nonlinear viscoelasticity also elucidates observed phenomena such as normal stresses, shear thinning, and extensional thickening in viscoelastic fluids.

An **anelastic** material is a special case of a viscoelastic material: an anelastic material fully recovers to its original state on the removal of load.

When distinguishing between elastic, viscous, and forms of viscoelastic behavior, it is helpful to reference the time scale of the measurement relative to the relaxation times of the material being observed, known as the Deborah number (De) where: $De=\lambda /t$ where

- $\lambda$ is the relaxation time of the material
- t is time

## Dynamic modulus

Viscoelasticity is studied using dynamic mechanical analysis, applying a small oscillatory stress and measuring the resulting strain.

- Purely elastic materials have stress and strain in phase, so that the response of one caused by the other is immediate.
- In purely viscous materials, strain lags stress by a 90-degree phase.
- Viscoelastic materials exhibit behavior somewhere in the middle of these two types of material, exhibiting some lag in strain.

A complex dynamic modulus G can be used to represent the relations between the oscillating stress and strain: $G=G'+iG''$ where $i^{2}=-1$ ; $G'$ is the *storage modulus* and $G''$ is the *loss modulus*: $G'={\frac {\sigma _{0}}{\varepsilon _{0}}}\cos \delta$ $G''={\frac {\sigma _{0}}{\varepsilon _{0}}}\sin \delta$ where $\sigma _{0}$ and $\varepsilon _{0}$ are the amplitudes of stress and strain respectively, and $\delta$ is the phase shift between them.

## Constitutive models of linear viscoelasticity

Viscoelastic materials, such as amorphous polymers, semicrystalline polymers, biopolymers and even the living tissue and cells, can be modeled in order to determine their stress and strain or force and displacement interactions as well as their temporal dependencies. These models, which include the Maxwell model, the Kelvin–Voigt model, the standard linear solid model, and the Burgers model, are used to predict a material's response under different loading conditions.

Viscoelastic behavior has elastic and viscous components modeled as linear combinations of springs and dashpots, respectively. Each model differs in the arrangement of these elements, and all of these viscoelastic models can be equivalently modeled as electrical circuits.

In an equivalent electrical circuit, stress is represented by current, and strain rate by voltage. The elastic modulus of a spring is analogous to the inverse of a circuit's *inductance* (it stores energy) and the viscosity of a dashpot to a circuit's *resistance* (it dissipates energy).

The elastic components, as previously mentioned, can be modeled as springs of elastic constant E, given the formula: $\sigma =E\varepsilon$ where σ is the stress, E is the elastic modulus of the material, and ε is the strain that occurs under the given stress, similar to Hooke's law.

The viscous components can be modeled as dashpots such that the stress–strain rate relationship can be given as, $\sigma =\eta {\frac {d\varepsilon }{dt}}$ where σ is the stress, η is the viscosity of the material, and dε/dt is the time derivative of strain.

The relationship between stress and strain can be simplified for specific stress or strain rates. For high stress or strain rates/short time periods, the time derivative components of the stress–strain relationship dominate. In these conditions it can be approximated as a rigid rod capable of sustaining high loads without deforming. Hence, the dashpot can be considered to be a "short-circuit".

Conversely, for low stress states/longer time periods, the time derivative components are negligible and the dashpot can be effectively removed from the system – an "open" circuit. As a result, only the spring connected in parallel to the dashpot contributes to the total strain in the system.

### Maxwell model

The Maxwell model can be represented by a purely viscous damper and a purely elastic spring connected in series, as shown in the diagram. The model can be represented by the following equation: $\sigma +{\frac {\eta }{E}}{\dot {\sigma }}=\eta {\dot {\varepsilon }}$

Under this model, if the material is put under a constant strain, the stresses gradually relax. When a material is put under a constant stress, the strain has two components. First, an elastic component occurs instantaneously, corresponding to the spring, and relaxes immediately upon release of the stress. The second is a viscous component that grows with time as long as the stress is applied. The Maxwell model predicts that stress decays exponentially with time, which is accurate for most polymers. One limitation of this model is that it does not predict creep accurately. The Maxwell model for creep or constant-stress conditions postulates that strain increases linearly with time. However, polymers for the most part show the strain rate to be decreasing with time.

This model can be applied to soft solids: thermoplastic polymers in the vicinity of their melting temperature, fresh concrete (neglecting its aging), and numerous metals at a temperature close to their melting point.

The equation introduced here, however, lacks a consistent derivation from more microscopic model and is not observer independent. The Upper-convected Maxwell model is its sound formulation in terms of the Cauchy stress tensor and constitutes the simplest tensorial constitutive model for viscoelasticity (see e.g. or ).

### Kelvin–Voigt model

The Kelvin–Voigt model, also known as the Voigt model, consists of a Newtonian damper and Hookean elastic spring connected in parallel, as shown in the picture. It is used to explain the creep behaviour of polymers.

The constitutive relation is expressed as a linear first-order differential equation: $\sigma =E\varepsilon +\eta {\dot {\varepsilon }}$

This model represents a solid undergoing reversible, viscoelastic strain. Upon application of a constant stress, the material deforms at a decreasing rate, asymptotically approaching the steady-state strain. When the stress is released, the material gradually relaxes to its undeformed state. At constant stress (creep), the model is quite realistic as it predicts strain to tend to σ/E as time continues to infinity. Similar to the Maxwell model, the Kelvin–Voigt model also has limitations. The model is extremely good with modelling creep in materials, but with regards to relaxation the model is much less accurate.

This model can be applied to organic polymers, rubber, and wood when the load is not too high.

### Standard linear solid model

The standard linear solid model, also referred as the Kelvin or Zener model, consists of two springs and a dashpot. This model is referred as Kelvin model by some authors, as Lord Kelvin (William Thomson) observed that the rate of dissipation of energy increases less rapidly than the square of the frequency as predicted by a simple Voigt Model. Finally, he concluded that simple Voigt Model does not corresponds to reality . However, the standard linear solid model formally proposed by John Henry Poynting and Joseph John Thomson in 1902 . It is the simplest model that describes both the creep and stress relaxation behaviors of a viscoelastic material properly. For this model, the governing constitutive relations are:

| Maxwell representation | Voigt representation |
|---|---|
|   |   |
| $\sigma +{\frac {\eta }{E_{2}}}{\dot {\sigma }}=E_{1}\varepsilon +{\frac {\eta (E_{1}+E_{2})}{E_{2}}}{\dot {\varepsilon }}$ | $\sigma +{\frac {\eta }{E_{1}+E_{2}}}{\dot {\sigma }}={\frac {E_{1}E_{2}}{E_{1}+E_{2}}}\varepsilon +{\frac {E_{1}\eta }{E_{1}+E_{2}}}{\dot {\varepsilon }}$ |

Under a constant stress, the modeled material instantaneously deforms to some strain, which is the instantaneous elastic portion of the strain. After that it continues to deform and asymptotically approach a steady-state strain, which is the retarded elastic portion of the strain. Although the standard linear solid model is more accurate than the Maxwell and Kelvin–Voigt models in predicting material responses, mathematically it returns inaccurate results for strain under specific loading conditions.

### Jeffreys model

The Jeffreys model like the Zener model is a three element model. It consist of two dashpots and a spring.

It was proposed in 1929 by Harold Jeffreys to study Earth's mantle.

### Burgers model

The Burgers model consists of either two Maxwell components in parallel or a Kelvin–Voigt component, a spring and a dashpot in series. For this model, the governing constitutive relations are:

| Maxwell representation | Kelvin representation |
|---|---|
|   |   |
| $\sigma +\left({\frac {\eta _{1}}{E_{1}}}+{\frac {\eta _{2}}{E_{2}}}\right){\dot {\sigma }}+{\frac {\eta _{1}\eta _{2}}{E_{1}E_{2}}}{\ddot {\sigma }}=\left(\eta _{1}+\eta _{2}\right){\dot {\varepsilon }}+{\frac {\eta _{1}\eta _{2}\left(E_{1}+E_{2}\right)}{E_{1}E_{2}}}{\ddot {\varepsilon }}$ | $\sigma +\left({\frac {\eta _{1}}{E_{1}}}+{\frac {\eta _{2}}{E_{1}}}+{\frac {\eta _{2}}{E_{2}}}\right){\dot {\sigma }}+{\frac {\eta _{1}\eta _{2}}{E_{1}E_{2}}}{\ddot {\sigma }}=\eta _{2}{\dot {\varepsilon }}+{\frac {\eta _{1}\eta _{2}}{E_{1}}}{\ddot {\varepsilon }}$ |

This model incorporates viscous flow into the standard linear solid model, giving a linearly increasing asymptote for strain under fixed loading conditions.

### Generalized Maxwell model

The generalized Maxwell model, also known as the Wiechert model, is the most general form of the linear model for viscoelasticity. It takes into account that the relaxation does not occur at a single time, but at a distribution of times. Due to molecular segments of different lengths with shorter ones contributing less than longer ones, there is a varying time distribution. The Wiechert model shows this by having as many spring–dashpot Maxwell elements as necessary to accurately represent the distribution. The figure on the right shows the generalised Wiechert model. Applications: metals and alloys at temperatures lower than one quarter of their absolute melting temperature (expressed in K) and characterizing elastic efficiency.

## Constitutive models for nonlinear viscoelasticity

Non-linear viscoelastic constitutive equations are needed to quantitatively account for phenomena in fluids like differences in normal stresses, shear thinning, and extensional thickening. Necessarily, the history experienced by the material is needed to account for time-dependent behavior, and is typically included in models as a history kernel **K**.

### Second-order fluid

The second-order fluid is typically considered the simplest nonlinear viscoelastic model, and typically occurs in a narrow region of materials behavior occurring at high strain amplitudes and Deborah number between Newtonian fluids and other more complicated nonlinear viscoelastic fluids. The second-order fluid constitutive equation is given by:

$\mathbf {T} =-p\mathbf {I} +2\eta _{0}\mathbf {D} -\psi _{1}\mathbf {D} ^{\triangledown }+4\psi _{2}\mathbf {D} \cdot \mathbf {D}$

where:

- $\mathbf {I}$ is the identity tensor
- $\mathbf {D}$ is the deformation tensor
- $\eta _{0},\psi _{1},\psi _{2}$ denote viscosity, and first and second normal stress coefficients, respectively
- $\mathbf {D} ^{\triangledown }$ denotes the upper-convected derivative of the deformation tensor where $\mathbf {D} ^{\triangledown }\equiv {\dot {\mathbf {D} }}-(\nabla \mathbf {v} )^{\mathbf {T} }\cdot \mathbf {D} -\mathbf {D} \cdot \nabla \mathbf {v}$ and ${\dot {\mathbf {D} }}\equiv {\frac {\partial }{\partial t}}\mathbf {D} +\mathbf {v} \cdot \nabla \mathbf {D}$ is the material time derivative of the deformation tensor.

### Upper-convected Maxwell model

The upper-convected Maxwell model incorporates nonlinear time behavior into the viscoelastic Maxwell model, given by:

$\mathbf {\tau } +\lambda \mathbf {\tau } ^{\triangledown }=2\eta _{0}\mathbf {D}$ where $\mathbf {\tau }$ denotes the stress tensor.

### Oldroyd-B model

The Oldroyd-B model is an extension of the Upper Convected Maxwell model and is interpreted as a solvent filled with elastic bead and spring dumbbells. The model is named after its creator James G. Oldroyd.

The model can be written as: $\mathbf {T} +\lambda _{1}{\stackrel {\nabla }{\mathbf {T} }}=2\eta _{0}(\mathbf {D} +\lambda _{2}{\stackrel {\nabla }{\mathbf {D} }})$ where:

- $\mathbf {T}$ is the stress tensor;
- $\lambda _{1}$ is the relaxation time;
- $\lambda _{2}$ is the retardation time = ${\frac {\eta _{s}}{\eta _{0}}}\lambda _{1}$ ;
- ${\stackrel {\nabla }{\mathbf {T} }}$ is the upper convected time derivative of stress tensor: ${\stackrel {\nabla }{\mathbf {T} }}={\frac {\partial }{\partial t}}\mathbf {T} +\mathbf {v} \cdot \nabla \mathbf {T} -((\nabla \mathbf {v} )^{T}\cdot \mathbf {T} +\mathbf {T} \cdot (\nabla \mathbf {v} ));$
- $\mathbf {v}$ is the fluid velocity;
- $\eta _{0}$ is the total viscosity composed of solvent and polymer components, $\eta _{0}=\eta _{s}+\eta _{p}$ ;
- $\mathbf {D}$ is the deformation rate tensor or rate of strain tensor, $\mathbf {D} ={\frac {1}{2}}\left[{\boldsymbol {\nabla }}\mathbf {v} +({\boldsymbol {\nabla }}\mathbf {v} )^{T}\right]$ .

Whilst the model gives good approximations of viscoelastic fluids in shear flow, it has an unphysical singularity in extensional flow, where the dumbbells are infinitely stretched. This is, however, specific to idealised flow; in the case of a cross-slot geometry the extensional flow is not ideal, so the stress, although singular, remains integrable, although the stress is infinite in a correspondingly infinitely small region.

If the solvent viscosity is zero, the Oldroyd-B becomes the Upper Convected Maxwell model.

### Wagner model

Wagner model is might be considered as a simplified practical form of the Bernstein–Kearsley–Zapas model. The model was developed by German rheologist Manfred Wagner.

For the isothermal conditions the model can be written as: $\mathbf {\sigma } (t)=-p\mathbf {I} +\int _{-\infty }^{t}M(t-t')h(I_{1},I_{2})\mathbf {B} (t')\,dt'$

where:

- $\mathbf {\sigma } (t)$ is the Cauchy stress tensor as function of time *t*,
- *p* is the pressure
- $\mathbf {I}$ is the unity tensor
- *M* is the memory function showing, usually expressed as a sum of exponential terms for each mode of relaxation: $M(x)=\sum _{k=1}^{m}{\frac {g_{i}}{\theta _{i}}}\exp \left({\frac {-x}{\theta _{i}}}\right),$ where for each mode of the relaxation, $g_{i}$ is the relaxation modulus and $\theta _{i}$ is the relaxation time;
- $h(I_{1},I_{2})$ is the *strain damping* function that depends upon the first and second invariants of Finger tensor $\mathbf {B}$ .

The *strain damping function* is usually written as: $h(I_{1},I_{2})=m^{*}\exp(-n_{1}{\sqrt {I_{1}-3}})+(1-m^{*})\exp(-n_{2}{\sqrt {I_{2}-3}})$ If the value of the strain hardening function is equal to one, then the deformation is small; if it approaches zero, then the deformations are large.

### Prony series

In a one-dimensional relaxation test, the material is subjected to a sudden strain that is kept constant over the duration of the test, and the stress is measured over time. The initial stress is due to the elastic response of the material. Then, the stress relaxes over time due to the viscous effects in the material. Typically, either a tensile, compressive, bulk compression, or shear strain is applied. The resulting stress vs. time data can be fitted with a number of equations, called models. Only the notation changes depending on the type of strain applied: tensile-compressive relaxation is denoted E , shear is denoted G , bulk is denoted K . The Prony series for the shear relaxation is

$G(t)=G_{\infty }+\sum _{i=1}^{N}G_{i}\exp(-t/\tau _{i})$

where $G_{\infty }$ is the long term modulus once the material is totally relaxed, $\tau _{i}$ are the relaxation times (not to be confused with $\tau _{i}$ in the diagram); the higher their values, the longer it takes for the stress to relax. The data is fitted with the equation by using a minimization algorithm that adjust the parameters ( $G_{\infty },G_{i},\tau _{i}$ ) to minimize the error between the predicted and data values.

An alternative form is obtained noting that the elastic modulus is related to the long term modulus by

$G(t=0)=G_{0}=G_{\infty }+\sum _{i=1}^{N}G_{i}$

Therefore,

$G(t)=G_{0}-\sum _{i=1}^{N}G_{i}\left[1-e^{-t/\tau _{i}}\right]$

This form is convenient when the elastic shear modulus $G_{0}$ is obtained from data independent from the relaxation data, and/or for computer implementation, when it is desired to specify the elastic properties separately from the viscous properties, as in Simulia (2010).

A creep experiment is usually easier to perform than a relaxation one, so most data is available as (creep) compliance vs. time. Unfortunately, there is no known closed form for the (creep) compliance in terms of the coefficient of the Prony series. So, if one has creep data, it is not easy to get the coefficients of the (relaxation) Prony series, which are needed for example in. An expedient way to obtain these coefficients is the following. First, fit the creep data with a model that has closed form solutions in both compliance and relaxation; for example the Maxwell-Kelvin model (eq. 7.18-7.19) in Barbero (2007) or the Standard Solid Model (eq. 7.20-7.21) in Barbero (2007) (section 7.1.3). Once the parameters of the creep model are known, produce relaxation pseudo-data with the conjugate relaxation model for the same times of the original data. Finally, fit the pseudo data with the Prony series.

## Effect of temperature

The secondary bonds of a polymer constantly break and reform due to thermal motion. Application of a stress favors some conformations over others, so the molecules of the polymer gradually "flows" into the favored conformations over time. Because thermal motion is one factor contributing to the deformation of polymers, viscoelastic properties change with increasing or decreasing temperature. In most cases, the creep modulus, defined as the ratio of applied stress to the time-dependent strain, decreases with increasing temperature. Generally speaking, an increase in temperature correlates to a logarithmic decrease in the time required to impart equal strain under a constant stress. In other words, it takes less work to stretch a viscoelastic material an equal distance at a higher temperature than it does at a lower temperature.

More detailed effect of temperature on the viscoelastic behavior of polymer can be plotted as shown.

There are mainly five regions (some denoted four, which combines IV and V together) included in the typical polymers.

- Region I: Glassy state of the polymer is presented in this region. The temperature in this region for a given polymer is too low to endow molecular motion. Hence the motion of the molecules is frozen in this area. The mechanical property is hard and brittle in this region.
- Region II: Polymer passes glass transition temperature in this region. Beyond Tg, the thermal energy provided by the environment is enough to unfreeze the motion of molecules. The molecules are allowed to have local motion in this region hence leading to a sharp drop in stiffness compared to Region I.
- Region III: Rubbery plateau region. Materials lie in this region would exist long-range elasticity driven by entropy. For instance, a rubber band is disordered in the initial state of this region. When rubber band is stretched, the structure is aligned to be more ordered. Therefore, when releasing the rubber band, it spontaneously seeks a higher-entropy state and hence goes back to its initial state. This is entropy-driven elasticity shape recovery.
- Region IV: The behavior in the rubbery flow region is highly time-dependent. Polymers in this region would need to use a time-temperature superposition to get more detailed information to cautiously decide how to use the materials. For instance, if the material is used to cope with short interaction time purpose, it could present as 'hard' material. While using for long interaction time purposes, it would act as 'soft' material.
- Region V: Viscous polymer flows easily in this region. Another significant drop in stiffness.

Extreme cold temperatures can cause viscoelastic materials to change to the glass phase and become brittle. For example, exposure of pressure sensitive adhesives to extreme cold (dry ice, freeze spray, etc.) causes them to lose their tack, resulting in debonding.

## Viscoelastic creep

When subjected to a step constant stress, viscoelastic materials experience a time-dependent increase in strain. This phenomenon is known as viscoelastic creep.

At time $t_{0}$ , a viscoelastic material is loaded with a constant stress that is maintained for a sufficiently long time period. The material responds to the stress with a strain that increases until the material ultimately fails, if it is a viscoelastic liquid. If, on the other hand, it is a viscoelastic solid, it may or may not fail depending on the applied stress versus the material's ultimate resistance. When the stress is maintained for a shorter time period, the material undergoes an initial strain until a time $t_{1}$ , after which the strain immediately decreases (discontinuity) then gradually decreases at times $t>t_{1}$ to a residual strain.

Viscoelastic creep data can be presented by plotting the creep modulus (constant applied stress divided by total strain at a particular time) as a function of time. Below its critical stress, the viscoelastic creep modulus is independent of stress applied. A family of curves describing strain versus time response to various applied stress may be represented by a single viscoelastic creep modulus versus time curve if the applied stresses are below the material's critical stress value.

Viscoelastic creep is important when considering long-term structural design. Given loading and temperature conditions, designers can choose materials that best suit component lifetimes.

## Measurement

### Shear rheometry

Shear rheometers are based on the idea of putting the material to be measured between two plates, one or both of which move in a shear direction to induce stresses and strains in the material. The testing can be done at constant strain rate, stress, or in an oscillatory fashion (a form of dynamic mechanical analysis). Shear rheometers are typically limited by edge effects where the material may leak out from between the two plates and slipping at the material/plate interface.

### Extensional rheometry

Extensional rheometers, also known as extensiometers, measure viscoelastic properties by pulling a viscoelastic fluid, typically uniaxially. Because this typically makes use of capillary forces and confines the fluid to a narrow geometry, the technique is often limited to fluids with relatively low viscosity like dilute polymer solutions or some molten polymers. Extensional rheometers are also limited by edge effects at the ends of the extensiometer and pressure differences between inside and outside the capillary.

Despite the apparent limitations mentioned above, extensional rheometry can also be performed on high viscosity fluids. Although this requires the use of different instruments, these techniques and apparatuses allow for the study of the extensional viscoelastic properties of materials such as polymer melts. Three of the most common extensional rheometry instruments developed within the last 50 years are the Meissner-type rheometer, the filament stretching rheometer (FiSER), and the Sentmanat Extensional Rheometer (SER).

The Meissner-type rheometer, developed by Meissner and Hostettler in 1996, uses two sets of counter-rotating rollers to strain a sample uniaxially. This method uses a constant sample length throughout the experiment, and supports the sample in between the rollers via an air cushion to eliminate sample sagging effects. It does suffer from a few issues – for one, the fluid may slip at the belts which leads to lower strain rates than one would expect. Additionally, this equipment is challenging to operate and costly to purchase and maintain.

The FiSER rheometer simply contains fluid in between two plates. During an experiment, the top plate is held steady and a force is applied to the bottom plate, moving it away from the top one. The strain rate is measured by the rate of change of the sample radius at its middle. It is calculated using the following equation: ${\dot {\epsilon }}=-{\frac {2}{R}}{dR \over dt}$ where R is the mid-radius value and ${\dot {\epsilon }}$ is the strain rate. The viscosity of the sample is then calculated using the following equation: $\eta ={\frac {F}{\pi R^{2}{\dot {\epsilon }}}}$ where $\eta$ is the sample viscosity, and F is the force applied to the sample to pull it apart.

Much like the Meissner-type rheometer, the SER rheometer uses a set of two rollers to strain a sample at a given rate. It then calculates the sample viscosity using the well known equation: $\sigma =\eta {\dot {\epsilon }}$ where $\sigma$ is the stress, $\eta$ is the viscosity and ${\dot {\epsilon }}$ is the strain rate. The stress in this case is determined via torque transducers present in the instrument. The small size of this instrument makes it easy to use and eliminates sample sagging between the rollers. A schematic detailing the operation of the SER extensional rheometer can be found on the right.

### Other methods

Though there are many instruments that test the mechanical and viscoelastic response of materials, broadband viscoelastic spectroscopy (BVS) and resonant ultrasound spectroscopy (RUS) are more commonly used to test viscoelastic behavior because they can be used above and below ambient temperatures and are more specific to testing viscoelasticity. These two instruments employ a damping mechanism at various frequencies and time ranges with no appeal to time–temperature superposition. Using BVS and RUS to study the mechanical properties of materials is important to understanding how a material exhibiting viscoelasticity performs.
