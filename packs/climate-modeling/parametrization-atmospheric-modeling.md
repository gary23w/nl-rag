---
title: "Parametrization (atmospheric modeling)"
source: https://en.wikipedia.org/wiki/Parametrization_(atmospheric_modeling)
domain: climate-modeling
license: CC-BY-SA-4.0
tags: climate model, general circulation model, radiative transfer, model intercomparison
fetched: 2026-07-02
---

# Parametrization (atmospheric modeling)

**Parametrization** (or **parameterization**) in an atmospheric model (either weather model or climate model) is a method of replacing processes that are too small-scale or complex to be physically represented in the model by a simplified process. This can be contrasted with other processes—e.g., large-scale flow of the atmosphere—that are explicitly resolved within the models. Associated with these parametrizations are various *parameters* used in the simplified processes. Examples include the descent rate of raindrops, convective clouds, simplifications of the atmospheric radiative transfer on the basis of atmospheric radiative transfer codes, and cloud microphysics. Radiative parametrizations are important to both atmospheric and oceanic modeling alike. Atmospheric emissions from different sources within individual grid boxes also need to be parametrized to determine their impact on air quality.

## Clouds

Weather and climate model gridboxes have sides of between 5 kilometres (3.1 mi) and 300 kilometres (190 mi). A typical cumulus cloud has a scale of less than 1 kilometre (0.62 mi), and would require a grid even finer than this to be represented physically by the equations of fluid motion. Therefore, the processes that such clouds represent are *parametrized*, by processes of various sophistication. In the earliest models, if a column of air in a model gridbox was unstable (i.e., the bottom warmer than the top) then it would be overturned, and the air in that vertical column mixed. More sophisticated schemes add enhancements, recognizing that only some portions of the box might convect and that entrainment and other processes occur. Weather models that have gridboxes with sides between 5 kilometres (3.1 mi) and 25 kilometres (16 mi) can explicitly represent convective clouds, although they still need to parametrize cloud microphysics.

The formation of large-scale (stratus-type) clouds is more physically based: they form when the relative humidity reaches some prescribed value. Still, sub grid scale processes need to be taken into account. Rather than assuming that clouds form at 100% relative humidity, the cloud fraction can be related to a critical relative humidity of 70% for stratus-type clouds, and at or above 80% for cumuliform clouds, reflecting the sub grid scale variation that would occur in the real world. Portions of the precipitation parametrization include the condensation rate, energy exchanges dealing with the change of state from water vapor into liquid drops, and the microphysical component which controls the rate of change from water vapor to water droplets.

## Radiation and atmosphere-surface interaction

The amount of solar radiation reaching ground level in rugged terrain, or due to variable cloudiness, is parametrized as this process occurs on the molecular scale. This method of parametrization is also done for the surface flux of energy between the ocean and the atmosphere in order to determine realistic sea surface temperatures and type of sea ice found near the ocean's surface. Also, the grid size of the models is large when compared to the actual size and roughness of clouds and topography. Sun angle as well as the impact of multiple cloud layers is taken into account. Soil type, vegetation type, and soil moisture all determine how much radiation goes into warming and how much moisture is drawn up into the adjacent atmosphere. Thus, they are important to parametrize.

## Air quality

Air quality forecasting attempts to predict when the concentrations of pollutants will attain levels that are hazardous to public health. The concentration of pollutants in the atmosphere is determined by transport, diffusion, chemical transformation, and ground deposition. Alongside pollutant source and terrain information, these models require data about the state of the fluid flow in the atmosphere to determine its transport and diffusion. Within air quality models, parametrizations take into account atmospheric emissions from multiple relatively tiny sources (e.g. roads, fields, factories) within specific grid boxes.

## Eddies

The ocean (and, although more variably, the atmosphere) is stratified through density. At rest, surfaces of constant density (known as isopycnals in the ocean) will be parallel to surfaces of constant pressure (isobars). However, various processes such as geostrophy and upwelling can result in isopycnals becoming tilted relative to isobars. These tilted density surfaces represent a source of potential energy and, if the slope becomes steep enough, a fluid instability known as baroclinic instability can be triggered. Eddies are generated through baroclinic instability, which act to flatten density surfaces through the slantwise exchange of fluid.

The resulting eddies are formed at a characteristic scale called the Rossby deformation radius. This scale depends on the strength of stratification and the coriolis parameter (which in turn depends on the latitude). As a result, baroclinic eddies form on scales of around 1° (~100 km) at the tropics, but less than 1/12° (~10 km) at the poles and in some shelf seas. Most climate models, such as those run as part of CMIP experiments, are run at a resolution of 1-1/4° in the ocean, and can therefore not resolve baroclinic eddies across large parts of the ocean, particularly at the poles. However, high-latitude baroclinic eddies are important for many ocean processes such as the Atlantic Meridional Overturning Circulation (AMOC), which affects global climate. As a result, the effects of eddies are parametrized in climate models, such as through the widely-used Gent-McWilliams (GM) parametrization which represents the isopycnal-flattening effects of eddies as advection (often misinterpreted as diffusion of surfaces). This parametrization is not perfect - for instance, it may overpredict the sensitivity of the Antarctic Circumpolar Current and AMOC to the strength of winds over the Southern Ocean. As a result, alternative parametrizations are being developed to improve the representation of eddies in ocean models.

## Problems with increased resolution

As model resolution increases, errors associated with moist convective processes are increased as assumptions which are statistically valid for larger grid boxes become questionable once the grid boxes shrink in scale towards the size of the convection itself. At resolutions greater than T639, which has a grid box dimension of about 30 kilometres (19 mi), the Arakawa-Schubert convective scheme produces minimal convective precipitation, making most precipitation unrealistically stratiform in nature.

## Calibration

When a physical process is parametrized, two choices have to be made: what is the structural form (for instance, two variables can be related linearly) and what is the exact value of the parameters (for instance, the constant of proportionality). The process of determining the exact values of the parameters in a parametrization is called calibration, or sometimes less precise, tuning. Calibration is a difficult process, and different strategies are used to do it. One popular method is to run a model, or a submodel, and compare it to a small set of selected metrics, such as temperature. The parameters that lead to the model run which resembles reality best are chosen.
