---
title: "Langmuir adsorption model"
source: https://en.wikipedia.org/wiki/Langmuir_adsorption_model
domain: surface-chemistry
license: CC-BY-SA-4.0
tags: surface chemistry, surface tension, adsorption isotherm, contact angle
fetched: 2026-07-02
---

# Langmuir adsorption model

The **Langmuir adsorption model** explains adsorption by assuming an adsorbate behaves as an ideal gas at isothermal conditions. According to the model, adsorption and desorption are reversible processes. This model even explains the effect of pressure; *i.e.*, at these conditions the adsorbate's partial pressure $p_{A}$ is related to its volume V adsorbed onto a solid adsorbent. The adsorbent, as indicated in the figure, is assumed to be an ideal solid surface composed of a series of distinct sites capable of binding the adsorbate. The adsorbate binding is treated as a chemical reaction between the adsorbate gaseous molecule $A_{\text{g}}$ and an empty sorption site S. This reaction yields an adsorbed species $A_{\text{ad}}$ with an associated equilibrium constant $K_{\text{eq}}$ :

${\ce {A_{g}{}+ S <=> A_{ad}}}$

.

From these basic hypotheses the mathematical formulation of the Langmuir adsorption isotherm can be derived in various independent and complementary ways: by the kinetics, the thermodynamics, and the statistical mechanics approaches respectively (see below for the different demonstrations).

The Langmuir adsorption equation is

$\theta _{A}={\frac {V}{V_{\text{m}}}}={\frac {K_{\text{eq}}^{A}\,p_{A}}{1+K_{\text{eq}}^{A}\,p_{A}}},$

where $\theta _{A}$ is the fractional occupancy of the adsorption sites, i.e., the ratio of the volume V of gas adsorbed onto the solid to the volume $V_{\text{m}}$ of a gas molecules monolayer covering the whole surface of the solid and completely occupied by the adsorbate. A continuous monolayer of adsorbate molecules covering a homogeneous flat solid surface is the conceptual basis for this adsorption model.

## Background and experiments

In 1916, Irving Langmuir presented his model for the adsorption of species onto simple surfaces. Langmuir was awarded the Nobel Prize in 1932 for his work concerning surface chemistry. He hypothesized that a given surface has a certain number of equivalent sites to which a species can "stick", either by physisorption or chemisorption. His theory began when he postulated that gaseous molecules do not rebound elastically from a surface, but are held by it in a similar way to groups of molecules in solid bodies.

Langmuir published two papers that confirmed the assumption that adsorbed films do not exceed one molecule in thickness. The first experiment involved observing electron emission from heated filaments in gases. The second, a more direct evidence, examined and measured the films of liquid onto an adsorbent surface layer. He also noted that generally the attractive strength between the surface and the first layer of adsorbed substance is much greater than the strength between the first and second layer. However, there are instances where the subsequent layers may condense given the right combination of temperature and pressure.

## Basic assumptions of the model

Inherent within this model, the following assumptions are valid specifically for the simplest case: the adsorption of a single adsorbate onto a series of equivalent sites onto the surface of the solid.

1. The surface containing the adsorbing sites is a perfectly flat plane with no corrugations (assume the surface is homogeneous). However, chemically heterogeneous surfaces can be considered to be homogeneous if the adsorbate is bound to only one type of functional groups on the surface.
2. The adsorbing gas adsorbs into an immobile state.
3. All sites are energetically equivalent, and the energy of adsorption is equal for all sites.
4. Each site can hold at most one molecule (mono-layer coverage only).
5. No (or ideal) interactions between adsorbate molecules on adjacent sites. When the interactions are ideal, the energy of side-to-side interactions is equal for all sites regardless of the surface occupancy.

## Derivations of the Langmuir adsorption isotherm

The mathematical expression of the Langmuir adsorption isotherm involving only one sorbing species can be demonstrated in different ways: the kinetics approach, the thermodynamics approach, and the statistical mechanics approach respectively. In case of two competing adsorbed species, the competitive adsorption model is required, while when a sorbed species dissociates into two distinct entities, the dissociative adsorption model need to be used.

### Kinetic derivation

This section provides a kinetic derivation for a single-adsorbate case. The kinetic derivation applies to gas-phase adsorption. The multiple-adsorbate case is covered in the competitive adsorption sub-section. The model assumes adsorption and desorption as being elementary processes, where the rate of adsorption *r*ad and the rate of desorption *r*d are given by

$r_{\text{ad}}=k_{\text{ad}}p_{A}[S],$

$r_{\text{d}}=k_{d}[A_{\text{ad}}],$

where *pA* is the partial pressure of *A* over the surface, [*S*] is the concentration of free sites in number/m2, [*A*ad] is the surface concentration of *A* in molecules/m2 (concentration of occupied sites), and *k*ad and *k*d are constants of forward adsorption reaction and backward desorption reaction in the above reactions.

At equilibrium, the rate of adsorption equals the rate of desorption. Setting *r*ad = *r*d and rearranging, we obtain

${\frac {[A_{\text{ad}}]}{p_{A}[S]}}={\frac {k_{\text{ad}}}{k_{\text{d}}}}=K_{\text{eq}}^{A}.$

The concentration of sites is given by dividing the total number of sites (*S*0) covering the whole surface by the area of the adsorbent (*a*):

$[S_{0}]=S_{0}/a.$

We can then calculate the concentration of all sites by summing the concentration of free sites [*S*] and occupied sites:

$[S_{0}]=[S]+[A_{\text{ad}}].$

Combining this with the equilibrium equation, we get

$[S_{0}]={\frac {[A_{\text{ad}}]}{K_{\text{eq}}^{A}p_{A}}}+[A_{\text{ad}}]={\frac {1+K_{\text{eq}}^{A}p_{A}}{K_{\text{eq}}^{A}p_{A}}}[A_{\text{ad}}].$

We define now the fraction of the surface sites covered with *A* as

$\theta _{A}={\frac {[A_{\text{ad}}]}{[S_{0}]}}.$

This, applied to the previous equation that combined site balance and equilibrium, yields the Langmuir adsorption isotherm:

$\theta _{A}={\frac {K_{\text{eq}}^{A}p_{A}}{1+K_{\text{eq}}^{A}p_{A}}}.$

### Thermodynamic derivation

In condensed phases (solutions), adsorption to a solid surface is a competitive process between the solvent (*A*) and the solute (*B*) to occupy the binding site. The thermodynamic equilibrium is described as

Solvent (bound) + Solute (free) ↔ Solvent (free) + Solute (bound).

If we designate the solvent by the subscript "1" and the solute by "2", and the bound state by the superscript "s" (surface/bound) and the free state by the "b" (bulk solution / free), then the equilibrium constant can be written as a ratio between the activities of products over reactants:

$K={\frac {a_{1}^{\text{b}}\times a_{2}^{\text{s}}}{a_{2}^{\text{b}}\times a_{1}^{\text{s}}}}.$

For dilute solutions the activity of the solvent in bulk solution $a_{1}^{\text{b}}\simeq 1,$ and the activity coefficients ( $\gamma$ ) are also assumed to ideal on the surface. Thus, $a_{2}^{\text{s}}=X_{2}^{\text{s}}=\theta ,$ $a_{1}^{\text{s}}=X_{1}^{\text{s}},$ , and $X_{1}^{\text{s}}+X_{2}^{\text{s}}=1,$ where $X_{i}$ are mole fractions. Re-writing the equilibrium constant and solving for $\theta$ yields

$\theta ={\frac {Ka_{2}^{\text{b}}}{1+Ka_{2}^{\text{b}}}}.$

Note that the concentration of the solute adsorbate can be used instead of the activity coefficient. However, the equilibrium constant will no longer be dimensionless and will have units of reciprocal concentration instead. The difference between the kinetic and thermodynamic derivations of the Langmuir model is that the thermodynamic uses activities as a starting point while the kinetic derivation uses rates of reaction. The thermodynamic derivation allows for the activity coefficients of adsorbates in their bound and free states to be included. The thermodynamic derivation is usually referred to as the "Langmuir-like equation".

### Statistical mechanical derivation

This derivation based on statistical mechanics was originally provided by Volmer and Mahnert in 1925. The partition function of the finite number of adsorbents adsorbed on a surface, in a canonical ensemble, is given by

$Z(N_{A})=\left[\zeta _{L}^{N_{A}}{\frac {N_{S}!}{(N_{S}-N_{A})!}}\right]{\frac {1}{N_{A}!}},$

where $\zeta _{L}$ is the partition function of a single adsorbed molecule, $N_{S}$ is the number of adsorption sites (both occupied and unoccupied), and $N_{A}$ is the number of adsorbed molecules which should be less than or equal to $N_{S}$ . The terms in the bracket give the total partition function of the $N_{A}$ adsorbed molecules by taking a product of the individual partition functions (refer to Partition function of subsystems). The $1/N_{A}!$ factor accounts for the overcounting arising due to the indistinguishable nature of the adsorbates. The grand canonical partition function is given by

${\mathcal {Z}}(\mu _{A})=\sum _{N_{A}=0}^{N_{S}}\exp \left({\frac {N_{A}\mu _{A}}{k_{\text{B}}T}}\right){\frac {\zeta _{L}^{N_{A}}}{N_{A}!}}\,{\frac {N_{S}!}{(N_{S}-N_{A})!}}.$

$\mu _{A}$ is the chemical potential of an adsorbed molecule. As it has the form of binomial series, the summation is reduced to

${\mathcal {Z}}(\mu _{A})=(1+x)^{N_{S}},$

where $x=\zeta _{L}\exp \left({\frac {\mu _{A}}{k_{\rm {B}}T}}\right).$

The grand canonical potential is

$\Omega =-k_{\rm {B}}T\ln({\mathcal {Z}})=-k_{\rm {B}}TN_{S}\ln(1+x),$

based on which the average number of occupied sites is calculated

$\langle N_{A}\rangle =-\left({\frac {\partial \Omega }{\partial \mu _{A}}}\right)_{T,{\text{area}}},$

which gives the coverage

$\theta _{A}={\frac {\langle N_{A}\rangle }{N_{S}}}={\frac {x}{1+x}}.$

Now, invoking the condition that the system is in equilibrium, that is, the chemical potential of the adsorbed molecules is equal to that of the molecules in gas phase, we have

$\mu _{A}=\mu _{\text{g}},$

The chemical potential of an ideal gas is

$\mu _{\text{g}}=\left({\frac {\partial A_{\text{g}}}{\partial N}}\right)_{T,V}$

where $A_{g}=-k_{\rm {B}}T\ln Z_{g}$ is the Helmholtz free energy of an ideal gas with its partition function

$Z_{g}={\frac {q^{N}}{N!}}.$

q is the partition function of a single particle in the volume of V (only consider the translational freedom here).

$q=V\left({\frac {2\pi mk_{\rm {B}}T}{h^{2}}}\right)^{3/2}.$

We thus have $\mu _{g}=-k_{\rm {B}}T\ln(q/N)$ , where we use Stirling's approximation.

Plugging $\mu _{g}$ to the expression of x , we have

${\frac {\theta _{A}}{1-\theta _{A}}}=x=\zeta _{L}{\frac {N}{q}}$

which gives the coverage

$\theta _{A}={\frac {\zeta _{L}/(q/N)}{1+\zeta _{L}/(q/N)}}$

By defining

$P_{0}={\frac {k_{\text{B}}T}{\zeta _{L}}}\left({\frac {2\pi mk_{\text{B}}T}{h^{2}}}\right)^{3/2}$

and using the identity $PV=Nk_{\rm {B}}T$ , finally, we have

$\theta _{A}={\frac {P}{P+P_{0}}}.$

It is plotted in the figure alongside demonstrating that the surface coverage increases quite rapidly with the partial pressure of the adsorbants, but levels off after *P* reaches *P*0.

### Competitive adsorption

The previous derivations assumed that there is only one species, *A*, adsorbing onto the surface. This section considers the case when there are two distinct adsorbates present in the system. Consider two species *A* and *B* that compete for the same adsorption sites. The following hypotheses are made here:

1. All the sites are equivalent.
2. Each site can hold at most one molecule of *A,* or one molecule of *B*, but *not both simultaneously*.
3. There are no interactions between adsorbate molecules on adjacent sites.

As derived using kinetic considerations, the equilibrium constants for both *A* and *B* are given by

${\frac {[A_{\text{ad}}]}{p_{A}\,[S]}}=K_{\text{eq}}^{A}$

and

${\frac {[B_{\text{ad}}]}{p_{B}\,[S]}}=K_{\text{eq}}^{B}.$

The site balance states that the concentration of total sites [*S*0] is equal to the sum of free sites, sites occupied by *A* and sites occupied by *B*:

$[S_{0}]=[S]+[A_{\text{ad}}]+[B_{\text{ad}}].$

Inserting the equilibrium equations and rearranging in the same way we did for the single-species adsorption, we get similar expressions for both θ*A* and θ*B*:

$\theta _{A}={\frac {K_{\text{eq}}^{A}\,p_{A}}{1+K_{\text{eq}}^{A}\,p_{A}+K_{\text{eq}}^{B}\,p_{B}}},$

$\theta _{B}={\frac {K_{\text{eq}}^{B}\,p_{B}}{1+K_{\text{eq}}^{A}\,p_{A}+K_{\text{eq}}^{B}\,p_{B}}}.$

### Dissociative adsorption

The other case of special importance is when a molecule *D*2 dissociates into two atoms upon adsorption. Here, the following assumptions would be held to be valid:

1. *D*2 completely dissociates to two molecules of *D* upon adsorption.
2. The *D* atoms adsorb onto distinct sites on the surface of the solid and then move around and equilibrate.
3. All sites are equivalent.
4. Each site can hold at most one atom of *D*.
5. There are no interactions between adsorbate molecules on adjacent sites.

Using similar kinetic considerations, we get

${\frac {[D_{\text{ad}}]}{p_{D_{2}}^{1/2}[S]}}=K_{\text{eq}}^{D}.$

The 1/2 exponent on *p**D*2 arises because one gas phase molecule produces two adsorbed species. Applying the site balance as done above,

$\theta _{D}={\frac {(K_{\text{eq}}^{D}\,p_{D_{2}})^{1/2}}{1+(K_{\text{eq}}^{D}\,p_{D_{2}})^{1/2}}}.$

## Entropic considerations

The formation of Langmuir monolayers by adsorption onto a surface dramatically reduces the entropy of the molecular system.

To find the entropy decrease, we find the entropy of the molecule when in the adsorbed condition.

$S=S_{\text{configurational}}+S_{\text{vibrational}},$

$S_{\text{conf}}=k_{\rm {B}}\ln \Omega _{\text{conf}},$

$\Omega _{\text{conf}}={\frac {N_{S}!}{N!(N_{S}-N)!}}.$

Using Stirling's approximation, we have

$\ln N!\approx N\ln N-N,$

$S_{\text{conf}}/k_{\rm {B}}\approx -\theta _{A}\ln(\theta _{A})-(1-\theta _{A})\ln(1-\theta _{A}).$

On the other hand, the entropy of a molecule of an ideal gas is

${\frac {S_{\text{gas}}}{Nk_{\text{B}}}}=\ln \left({\frac {k_{\text{B}}T}{P\lambda ^{3}}}\right)+5/2,$

where $\lambda$ is the thermal de Broglie wavelength of the gas molecule.

## Limitations of the model

The Langmuir adsorption model deviates significantly in many cases, primarily because it fails to account for the surface roughness of the adsorbent. Rough inhomogeneous surfaces have multiple site types available for adsorption, with some parameters varying from site to site, such as the heat of adsorption. Moreover, specific surface area is a scale-dependent quantity, and no single true value exists for this parameter. Thus, the use of alternative probe molecules can often result in different obtained numerical values for surface area, rendering comparison problematic.

The model also ignores adsorbate–adsorbate interactions. Experimentally, there is clear evidence for adsorbate–adsorbate interactions in heat of adsorption data. There are two kinds of adsorbate–adsorbate interactions: direct interaction and indirect interaction. Direct interactions are between adjacent adsorbed molecules, which could make adsorbing near another adsorbate molecule more or less favorable and greatly affects high-coverage behavior. In indirect interactions, the adsorbate changes the surface around the adsorbed site, which in turn affects the adsorption of other adsorbate molecules nearby.

## Modifications

The modifications try to account for the points mentioned in above section like surface roughness, inhomogeneity, and adsorbate–adsorbate interactions.

### Two-mechanism Langmuir-like equation (TMLLE)

Also known as the two-site Langmuir equation. This equation describes the adsorption of one adsorbate to two or more distinct types of adsorption sites. Each binding site can be described with its own Langmuir expression, as long as the adsorption at each binding site type is independent from the rest.

$q_{\text{total}}={\frac {q_{1}^{\text{max}}K_{1}a_{2}^{\text{b}}}{1+K_{1}a_{2}^{\text{b}}}}+{\frac {q_{2}^{\text{max}}K_{2}a_{2}^{\text{b}}}{1+K_{2}a_{2}^{\text{b}}}}+\dots ,$

where

$q_{\text{total}}$

– total amount adsorbed at a given adsorbate concentration,

$q_{1}^{\text{max}}$

– maximum capacity of site type 1,

$q_{2}^{\text{max}}$

– maximum capacity of site type 2,

$K_{1}$

– equilibrium (affinity) constant of site type 1,

$K_{2}$

– equilibrium (affinity) constant of site type 2,

$a_{2}^{\text{b}}$

– adsorbate activity in solution at equilibrium

This equation works well for adsorption of some drug molecules to activated carbon in which some adsorbate molecules interact with hydrogen bonding while others interact with a different part of the surface by hydrophobic interactions (hydrophobic effect). The equation was modified to account for the hydrophobic effect (also known as entropy-driven adsorption):

$q_{\text{total}}={\frac {q_{1}^{\text{max}}K_{1}a_{2}^{\text{b}}}{1+K_{1}a_{2}^{\text{b}}}}+q_{\text{HB}}.$

The hydrophobic effect is independent of concentration, since $K_{2}a_{2}^{\text{b}}\gg 1.$ Therefore, the capacity of the adsorbent for hydrophobic interactions $q_{\text{HB}}$ can obtained from fitting to experimental data. The entropy-driven adsorption originates from the restriction of translational motion of bulk water molecules by the adsorbate, which is alleviated upon adsorption.

### Freundlich adsorption isotherm

The Freundlich isotherm is the most important multi-site adsorption isotherm for rough surfaces.

$\theta _{A}=\alpha _{F}p^{C_{\text{F}}},$

where *α*F and *C*F are fitting parameters. This equation implies that if one makes a log–log plot of adsorption data, the data will fit a straight line. The Freundlich isotherm has two parameters, while Langmuir's equations has only one: as a result, it often fits the data on rough surfaces better than the Langmuir isotherm. However, the Freundlich equation is not unique; consequently, a good fit of the data points does not offer sufficient proof that the surface is heterogeneous. The heterogeneity of the surface can be confirmed with calorimetry. Homogeneous surfaces (or heterogeneous surfaces that exhibit homogeneous adsorption (single-site)) have a constant $\Delta H$ of adsorption as a function of the occupied-sites fraction. On the other hand, heterogeneous adsorbents (multi-site) have a variable $\Delta H$ of adsorption depending on the sites occupation. When the adsorbate pressure (or concentration) is low, the fractional occupation is small and as a result, only low-energy sites are occupied, since these are the most stable. As the pressure increases, the higher-energy sites become occupied, resulting in a smaller $\Delta H$ of adsorption, given that adsorption is an exothermic process.

A related equation is the *Toth equation*. Rearranging the Langmuir equation, one can obtain

$\theta _{A}={\frac {p_{A}}{{\frac {1}{K_{\text{eq}}^{A}}}+p_{A}}}.$

J. Toth modified this equation by adding two parameters *α**T*0 and *C**T*0 to formulate the **Toth equation**:

$\theta ^{C_{T_{0}}}={\frac {\alpha _{T_{0}}p_{A}^{C_{T_{0}}}}{{\frac {1}{K_{\text{eq}}^{A}}}+p_{A}^{C_{T_{0}}}}}.$

### Temkin adsorption isotherm

This isotherm takes into account indirect adsorbate–adsorbate interactions on adsorption isotherms. Temkin noted experimentally that heats of adsorption would more often decrease than increase with increasing coverage.

The heat of adsorption Δ*H*ad is defined as

${\frac {[A_{\text{ad}}]}{p_{A}[S]}}=K_{\text{eq}}^{A}\propto \mathrm {e} ^{-\Delta G_{\text{ad}}/RT}=\mathrm {e} ^{\Delta S_{\text{ad}}/R}\,\mathrm {e} ^{-\Delta H_{\text{ad}}/RT}.$

He derived a model assuming that as the surface is loaded up with adsorbate, the heat of adsorption of all the molecules in the layer would decrease linearly with coverage due to adsorbate–adsorbate interactions:

$\Delta H_{\text{ad}}=\Delta H_{\text{ad}}^{0}(1-\alpha _{T}\theta ),$

where *αT* is a fitting parameter. Assuming the Langmuir adsorption isotherm still applied to the adsorbed layer, $K_{\text{eq}}^{A}$ is expected to vary with coverage as follows:

$K_{\text{eq}}^{A}=K_{\text{eq}}^{A,0}\mathrm {e} ^{\Delta H_{\text{ad}}^{0}(1-\alpha _{T}\theta )/RT}.$

Langmuir's isotherm can be rearranged to

$K_{\text{eq}}^{A}p_{A}={\frac {\theta }{1-\theta }}.$

Substituting the expression of the equilibrium constant and taking the natural logarithm:

$\ln {\big (}K_{\text{eq}}^{A,0}p_{A}{\big )}={\frac {-\Delta H_{\text{ad}}^{0}\alpha _{T}\theta }{RT}}+\ln {\frac {\theta }{1-\theta }}.$

### BET equation

Brunauer, Emmett and Teller (BET) derived the first isotherm for multilayer adsorption. It assumes a random distribution of sites that are empty or that are covered with by one monolayer, two layers and so on, as illustrated alongside. The main equation of this model is

${\frac {[A]}{S_{0}}}={\frac {c_{B}x_{B}}{(1-x_{B})[1+(c_{B}-1)x_{B}]}},$

where

$x_{B}=p_{A}K_{m},\quad c_{B}={\frac {K_{1}}{K_{m}}},$

and [*A*] is the total concentration of molecules on the surface, given by

$[A]=\sum _{i=1}^{\infty }i[A]_{i}=\sum _{i=1}^{\infty }iK_{1}K_{m}^{i-1}p_{A}^{i}[A]_{0},$

where

$K_{i}={\frac {[A]_{i}}{p_{A}[A]_{i-1}}},$

in which [*A*]0 is the number of bare sites, and [*A*]i is the number of surface sites covered by *i* molecules.

## Adsorption of a binary liquid on a solid

This section describes the surface coverage when the adsorbate is in liquid phase and is a binary mixture.

For ideal both phases[*clarification needed*] – no lateral interactions, homogeneous surface – the composition of a surface phase for a binary liquid system in contact with solid surface is given by a classic Everett isotherm equation (being a simple analogue of Langmuir equation), where the components are interchangeable (i.e. "1" may be exchanged to "2") without change of equation form:

$x_{1}^{s}={\frac {Kx_{1}^{l}}{1+(K-1)x_{1}^{l}}},$

where the normal definition of multi-component system is valid as follows:

$\sum _{i=1}^{k}x_{i}^{s}=1,\quad \sum _{i=1}^{k}x_{i}^{l}=1.$

By simple rearrangement, we get

$x_{1}^{s}={\frac {K[x_{1}^{l}/(1-x_{1}^{l})]}{1+K[x_{1}^{l}/(1-x_{1}^{l})]}}.$

This equation describes competition of components "1" and "2".
