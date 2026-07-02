---
title: "Ocean general circulation model"
source: https://en.wikipedia.org/wiki/Ocean_general_circulation_model
domain: ocean-modeling
license: CC-BY-SA-4.0
tags: ocean general circulation model, physical oceanography, thermohaline circulation, ekman transport
fetched: 2026-07-02
---

# Ocean general circulation model

**Ocean general circulation models** (OGCMs) are a particular kind of general circulation model to describe physical and thermodynamical processes in oceans. The oceanic general circulation is defined as the horizontal space scale and time scale larger than mesoscale (of order 100 km and 6 months). They depict oceans using a three-dimensional grid that include active thermodynamics and hence are most directly applicable to climate studies. They are the most advanced tools currently available for simulating the response of the global ocean system to increasing greenhouse gas concentrations. A hierarchy of OGCMs have been developed that include varying degrees of spatial coverage, resolution, geographical realism, process detail, etc.

## History

The first generation of OGCMs assumed “rigid lid” to eliminate high-speed external gravity waves. According to CFL criteria without those fast waves, we can use a bigger time step, which is not so computationally expensive. But it also filtered those ocean tides and other waves having the speed of tsunamis. Within this assumption, Kirk Bryan and co-worker Micheal Cox developed a 2D model, a 3D box model, and then a model of full circulation in GFDL, with variable density as well, for the world ocean with its complex coastline and bottom topography. The first application with specified global geometry was done in the early 1970s. Cox designed a 2° latitude-longitude grid with up to 12 vertical levels at each point.

With more and more research on ocean model, mesoscale phenomenon, e.g. most ocean currents have cross-stream dimensions equal to Rossby radius of deformation, started to get more awareness. However, in order to analyze those eddies and currents in numerical models, we need grid spacing to be approximately 20 km in middle latitudes. Thanks to those faster computers and further filtering the equations in advance to remove internal gravity waves, those major currents and low-frequency eddies then can be resolved, one example is the three-layer quasi-geostrophic models designed by Holland. Meanwhile, there are some model retaining internal gravity wave, for example one adiabatic layered model by O'Brien and his students, which did retain internal gravity waves so that equatorial and coastal problems involving these waves could be treated, led to an initial understanding of El Niño in terms of those waves.

In the late 1980s, simulations could finally be undertaken using the GFDL formulation with eddies marginally resolved over extensive domains and with observed winds and some atmospheric influence on density. Furthermore, these simulations with high enough resolution such as the Southern Ocean south of latitude 25°, the North Atlantic, and the World Ocean without the Arctic provided first side-by-side comparison with data. Early in the 1990s, for those large-scale and eddies resolvable models, the computer requirement for the 2D ancillary problem associated with the rigid lid approximation was becoming excessive. Furthermore, in order to predict tidal effects or compare height data from satellites, methods were developed to predict the height and pressure of the ocean surface directly. For example, one method is to treat the free surface and the vertically averaged velocity using many small steps in time for each single step of the full 3D model. Another method developed at Los Alamos National Laboratory solves the same 2D equations using an implicit method for the free surface. Both methods are quite efficient.

## Importance

OGCMs have many important applications: dynamical coupling with the atmosphere, sea ice, and land run-off that in reality jointly determine the oceanic boundary fluxes; transpire of biogeochemical materials; interpretation of the paleoclimate record;climate prediction for both natural variability and anthropogenic chafes; data assimilation and fisheries and other biospheric management. OGCMs play a critical role in Earth system model. They maintain the thermal balance as they transport energy from tropical to the polar latitudes. To analyze the feedback between ocean and atmosphere we need ocean model, which can initiate and amplify climate change on many different time scales, for instance, the interannual variability of El Niño and the potential modification of the major patterns for oceanic heat transport as a result of increasing greenhouse gases. Oceans are a kind of undersampled nature fluid system, so by using OGCMs we can fill in those data blank and improve understanding of basic processes and their interconnectedness, as well as to help interpret sparse observations. Even though, simpler models can be used to estimate climate response, only OGCM can be used conjunction with atmospheric general circulation model to estimate global climate change.

## Grid types

There are different types grid types that can be used by OGCMs. There is often a separation between vertical and horizontal grids.

### Horizontal grid types

Most models use one of the following horizontal grid types.

- Finite Differences
- Finite Element
- Spectral Grid

#### Finite differences grid

Finite differences grids are the most common grid types for OGCMs. For the grids, the Arakawa Grids are often used. On the A grid all quantities are calculated on a single point. This was only used in some of the earliest OGCMs. However, it was quickly realized that the solutions were extremely poor. The B grid has the velocity components on the edges of the Temperature grid boxes. While the C grid separates these velocity components in an u and v component. Both are still used presently in different models.

It is also possible to have a so-called Nested Grid Model. A nested grid model is an adaptation of the finite differences grid in which some parts have a higher density of grid points.

#### Finite element grid

Sometimes models use a finite element grid. Here, the variables are solved on a triangular grid. The big advantage of finite element grids is that it allows flexible resolution throughout the domain of the model. This is especially useful when studying a flow in a near a coastal environment as the coast can be more easily mapped.

#### Spectral grid

The spectral grids are the least used grids for OGCMs, while being widely used in atmospheric general circulation models. They are harder to use for ocean modelling because of the more complicated boundary conditions in the ocean compared to atmospheric models where they are extensively used.

### Vertical grid types

The vertical grids used for ocean general circulation models are often different from their atmospheric counterparts. Atmospheric models often use pressure as a vertical coordinate because of its isentropic nature.

- z-coordinates
- sigma coordinates
- isopycnal coordinates

#### Z coordinate systems

The z coordinate system in which height is taken as a coordinate is the simplest type of system to implement. The layers are often of varying depth with the layers near the top of the ocean being thinner than the deeper layers. This is because the features nearer to the surface happen on smaller scales. Z-coordinate systems have difficulties representing the bottom boundary layer and downslope flow due to odd diabatic mixing.

#### Sigma coordinates

In a sigma coordinate system the bottom topography determines the thickness of the vertical layer at each horizontal grid point. Similarly to the Z coordinate system the layers are often more closely spaced near the surface and/or the bottom than they are in the interior. Sigma coordinates allow the boundary layer to be better represented but have difficulties with pressure gradient errors when sharp bottom topography features are not smoothed out.

#### Isopycnal models

Isopycnal models model the potential density at a given pressure level as the vertical coordinate. The layers thus vary in thickness throughout the domain. This type of model is particularly useful when studying tracer transport. This is because tracers often move along lines of constant density. Isopycnal models have a subtle difference with layered models. The main difference is whether the model allows the vanishing of the isopycnals. For layered models the isopycnals are not allowed to vanish which has computational speed benefits.

## Subgridscale parameterization

Molecular friction rarely upsets the dominant balances (geostrophic and hydrostatic) in the ocean. With kinematic viscosities of v=10−6m 2 s−1 the Ekman number is several orders of magnitude smaller than unity; therefore, molecular frictional forces are certainly negligible for large-scale oceanic motions. A similar argument holds for the tracer equations, where the molecular thermodiffusivity and salt diffusivity lead to Reynolds number of negligible magnitude, which means the molecular diffusive time scales are much longer than advective time scale. So we can thus safely conclude that the direct effects of molecular processes are insignificant for large-scale. Yet the molecular friction is essential somewhere. The point is that large-scale motions in the ocean interacted with other scales by the nonlinearities in primitive equation. We can show that by Reynolds approach, which will leads to the closure problem. That means new variables arise at each level in the Reynolds averaging procedure. This leads to the need of parameterization scheme to account for those sub grid scale effects.

Here is a schematic “family tree” of subgridscale (SGS) mixing schemes. Although there is a considerable degree of overlap and interrelatedness among the huge variety of schemes in use today, several branch points maybe defined. Most importantly, the approaches for lateral and vertical subgridscale closure vary considerably. Filters and higher-order operators are used to remove small-scale noise that is numerically necessary. Those special dynamical parameterizations (topographic stress, eddy thickness diffusion and convection) are becoming available for certain processes. In the vertical, the surface mixed layer (sml) has historically received special attention because of its important role in air-sea exchange. Now there are so many schemes can be chose from: Price-Weller-Pinkel, Pacanowksi and Philander, bulk, Mellor-Yamada and k-profile parameterization (KPP) schemes.

Adaptive (non-constant) mixing length schemes are widely used for parameterization of both lateral and vertical mixing. In the horizontal, parameterizations dependent on the rates of stress and strain (Smagroinsky), grid spacing and Reynolds number (Re) have been advocated. In the vertical, vertical mixing as a function stability frequency (N^2) and/or Richardson number are historically prevalent. The rotated mixing tensors scheme is the one considering the angle of the principle direction of mixing, as for in the main thermocline, mixing along isopycnals dominates diapycnal mixing. Therefore, the principle direction of mixing is neither strictly vertical nor purely horizontal, but a spatially variable mixture of the two.

## Spin-up of OGCMs

OGCMs require a long spin-up time to be able to realistically represent the studied basins. Spin-up time is the time a model needs to reach a certain equilibrium. This equilibrium is often defined as a statistical parameter at which the change over time of a range of variables gets below a set threshold for a certain number of simulation timesteps. For OGCMs of a global scale it is often a challenge to reach this state. It can take thousands of model years to reach an equilibrium state for a model. The speed at which this equilibrium is reached is determined by slow processes below the thermocline.

### Decreasing the spin-up time

There have been many attempts to decrease the spin-up time of OGCMs. To accelerate the convergence of a model, several methods have been proposed. Better initial conditions significantly decrease the time a model needs to spin-up. However, this is not always possible, especially for the deep ocean.

Another approach is the distorted physics approach. This works on the basis that the ocean has processes on relatively short time scales above the thermocline. While processes below the thermocline are often diffusive and very slow. The acceleration of these processes is achieved by decreasing the local heat capacity, while not changing the transport and the mixing of heat. This makes the speed of reaching equilibrium for these models much quicker and nearly as efficient as atmospheric models with similar resolution. This method is very successful as there is (almost) no change to the final solution of the model.

It is also possible to reduce the spin-up time by exponential extrapolation. In this method, the temperature and salinity fields are repeatedly extrapolated with the assumption that they exponentially decay towards their equilibrium value. This method can in some cases reduce the spin-up time by a factor of two or three.

A third proposed method is the jacobian–free Newton–Krylov method. This method uses the matrix-vector products obtained from an explicit OGCM's jacobian. The method can be applied to many existing explicit OGCMs and can significantly speed up the spin-up time.

## Comparison with Atmospheric General Circulation Model

OGCMs and AGCMs have much in common, such as, the equations of motion and the numerical techniques. However, OGCMs have some unique features. For example, the atmosphere is forced thermally throughout its volume, the ocean is forced both thermally and mechanically primarily at its surface, in addition, the geometry of ocean basins is very complex. The boundary conditions are totally different. For ocean models, we need to consider those narrow but important boundary layers on nearly all bounding surfaces as well as within the oceanic interior. These boundary conditions on ocean flows are difficult to define and to parameterize, which results in a high computationally demand.

Ocean modeling is also strongly constrained by the existence in much of the world's oceans of mesoscale eddies with time and space scales, respectively, of weeks to months and tens to hundreds of kilometers. Dynamically, these nearly geostrophic turbulent eddies are the oceanographic counterparts of the atmospheric synoptic scale. Nevertheless, there are important differences. First, ocean eddies are not perturbations on an energetic mean flow. They may play an important role in the poleward transport of heat. Second, they are relatively small in horizontal extent so that ocean climate models, which must have the same overall exterior dimensions as AGCMs, may require as much as 20 times the resolution as AGCM if the eddies are to be explicitly resolved.

There also are more constraints on the OGCM's due to lacking data for the ocean. The bottom topography is especially lacking. Large swaths of the ocean are not mapped in high detail. This is in stark contrast to the land topography which can be mapped in detail by satellite altimeters. This creates even bigger uncertainties in the boundary conditions. Secondly, the atmosphere only has a changing geometry for the lower levels for most of its extent. While the ocean has sharp boundaries, with large swaths of land as complex boundary conditions.

## OGCMs in paleoceanography

The relation between paleoclimate and the effect on the ocean circulation has been widely studied. The first attempts at doing this often used the present-day forcings extrapolated to the past climate from proxies. The closure of the different passages in the ocean can then be simulated by simply blocking them with a thin line in the bathymetry. For instance closing the present-day Drake Passage.

These days, more complicated paleo bathymetries are used along with better proxies. To test the quality of the models, the Paleoclimate Modelling Intercomparison Project has been established.

## Classification

We can classify ocean models according to different standards. For example, according to vertical ordinates we have geo-potential, isopycnal and topography-following models. According to horizontal discretizations we have unstaggered or staggered grids. According to methods of approximation we have finite difference and finite element models. There are three basic types of OGCMs:

1. Idealized geometry models: Models with idealized basin geometry have been used extensively in ocean modeling and have played a major role in the development of new modeling methodologies. They use a simplified geometry, offering a basin itself, while the distribution of winds and buoyancy force are generally chosen as simple functions of latitude.
2. Basin-scale models: To compare OGCM results with observations we need realistic basin information instead of idealized data. However, if we only pay attention to local observation data, we don't need to run whole global simulation, and by doing that we can save a lot of computational resources.
3. Global models: This kind of model is the most computationally costly one. More experiments are needed as a preliminary step in constructing coupled Earth system models.
