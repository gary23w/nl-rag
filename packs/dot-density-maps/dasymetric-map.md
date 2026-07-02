---
title: "Dasymetric map"
source: https://en.wikipedia.org/wiki/Dasymetric_map
domain: dot-density-maps
license: CC-BY-SA-4.0
tags: dot distribution, dasymetric map, point density, areal interpolation
fetched: 2026-07-02
---

# Dasymetric map

A **dasymetric map** (from Greek *δασύς dasýs* 'dense' and *μέτρο métro* 'measure') is a type of thematic map that uses areal symbols to visualize a geographic field by refining a choropleth map with ancillary information about the distribution of the variable. The name refers to the fact that the most common variable mapped using this technique has generally been population density. The dasymetric map is a hybrid product combining the strengths and weaknesses of choropleth and isarithmic maps.

Dasymetric maps are used instead of choropleth maps because they represent underlying data distributions more accurately. Choropleth maps and dasymetric maps differ in three main ways. First, dasymetric zones are generated using ancillary data while boundaries on choropleth maps use units used for more general purposes (such as U.S. county boundaries). Second, choropleth zones have varying levels of internal homogeneity while dasymetric maps are designed to be internally homogeneous. Last, choropleth mapping methods are standardized while dasymetric methods are under researched.

## History

The earliest maps using this kind of approach include an 1833 map of world population density by George Julius Poulett Scrope and an 1838 map of population density in Ireland by Henry Drury Harness, although the methods used to create these maps were never documented.

The term "dasymetric" was coined in 1911 by Benjamin Semyonov-Tian-Shansky, who first fully developed and documented the technique, defining them as maps "on which population density, irrespective of any administrative boundaries, is shown as it is distributed in reality, i.e. by natural spots of concentration and rarefaction." He proposed several methods for improving on choropleth maps, some of which can more properly termed isarithmic maps, but the dasymetric technique he most fully developed and applied is still used today, albeit using digital data and tools such as GIS.

Beyond Russia, the technique was popularized in the 1930s by J.K. Wright, who has sometimes been incorrectly credited with its invention. Waldo R. Tobler introduced one of the first computer algorithms for dasymetric mapping, which he called *pycnophylactic interpolation* (from Greek *πυκνός puknós* 'dense, compact' and *φυλάττω phylátto* 'to guard, preserve'); apparently unaware of the earlier work; he only cites literature on pure isarithmic mapping. Since then, most other methods have used computation algorithms or GIS software to construct a dasymetric map.

Like other forms of thematic mapping, the dasymetric method was created and historically used because of the need for accurate visualization methods of population data. Dasymetric maps are not widely used because of a lack of standardized dasymetric mapping techniques that are accessible to the public. This leads to methods which are highly subjective with inconsistent criteria. Although fields such as public health still rely on choropleth maps, dasymetric maps are becoming more prevalent in developing fields such as aerial interpolation and population estimation using remote sensing.

## Methods

The dasymetric technique starts with a chosen variable aggregated over predetermined geographical districts as in a choropleth map. Then ancillary information is incorporated to adjust the boundaries of these districts. The third step is to adjust the variable as needed by the new boundaries, either as an exact calculation or an interpolated estimate.

The most common type of ancillary data for this is land cover, reclassified into ordinal degrees of human inhabitation from uninhabited wilderness to urban development. Another option is cadastral data, including small-scale administrative areas (e.g., national parks, wilderness reserves) or large-scale parcels.

The simplest and most common technique is the *binary method*, using regions that are known to be uninhabited, such as water bodies and government-owned land, and cropping these regions out of the choropleth districts, so that they appear empty on the final map. If the variable being mapped is area-dependent (such as population density), the values need to be recalculated according to the areas of the refined districts.

Several techniques have been developed that attempt a more sophisticated interpolation, using the ancillary data to reallocate individuals (and thus aggregate totals) between areas believed to be more and less dense, similar to Tian-Shansky's original method. Originally, the amount to reallocate the population to different ancillary zones (e.g., how dense should "agricultural land" be?) was done in a common sense way, but modern automated methods use statistical analysis to estimate a "best fit" of the choropleth data to the ancillary zones.

The binary method can also be applied to dot density maps, in which the predefined districts (the same source data as a choropleth map) are filled with a number of dots proportional to the total amount of the variable. Because the dots are usually randomly placed, they can give an impression of internal homogeneity almost as strong as the constant color of the choropleth map. The dasymetric method is applied by incorporating an ancillary layer that represents the area known to have a value of 0 (in the case of population density, an uninhabited area), which is used as a mask to prevent the dots for each original district from being placed in the overlapping area, forcing them to be more concentrated in the unmasked space (where the individuals are likely more dense in reality). This results in a refined dot distribution that more closely represents the real-world density.

Tobler's pycnophylactic interpolation algorithm was based on an assumption that the geographic field being modeled by the original choropleth map has a high degree of spatial autocorrelation; that is, the real-world spatial transitions in population density should be gradual, rather than abruptly changing at district boundaries. Using the "statistical surface" conceptualization of fields that was common in cartography at the time, his algorithm uses differential equations to construct a smooth "surface" from the "stepped surface" of the choropleth, while insuring that total volume of the surface (i.e., the total population) remains constant. Because it does not directly incorporate ancillary information, some consider it to not technically be a form of dasymetric mapping, but a related "areal interpolation" technique. Algorithms have been developed that hybridize the dasymetric and pycnophylactic techniques.

## Comparison to choropleth and isarithmic maps

A dasymetric map has some properties of both choropleth maps and isarithmic maps. All three methods can represent some of the same field variables, such as population density. Like the choropleth map from which the dasymetric map was derived, the variable being mapped is an aggregate statistical summary over a district; there is still no information given on the degree of internal variation of the variable, thus retaining the danger of interpretation issues such as the ecological fallacy and the modifiable areal unit problem. Each adjusted district boundary, being at least somewhat aligned to the presumed locations of change in the variable, approximates an isoline. This should lead to a reduction in the internal variation of the variable in the adjusted districts, but they cannot be presumed to be homogeneous.

The dasymetric map differs from both of the alternatives in that it is a derivative product produced by interpolation. Thus, the values in each district are estimates, which are potentially more accurate but definitely less certain than the original data. Most choropleth data are direct summary statistics of the raw data on individuals, with only occasional estimation, making them largely reliable. Most isarithmic maps are interpolations, often from a set of sample point locations, making it a derivative product, but less so than the dasymetric map.
