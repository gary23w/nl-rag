---
title: "Leaf area index"
source: https://en.wikipedia.org/wiki/Leaf_area_index
domain: crop-monitoring-remote
license: CC-BY-SA-4.0
tags: crop monitoring, normalized difference vegetation index, multispectral imaging, leaf area index
fetched: 2026-07-02
---

# Leaf area index

**Leaf area index** (**LAI**) or **leaf area ratio** is a dimensionless quantity that characterizes plant canopies. It is defined as the ratio of *leaf area* (LA) and ground area, in SI units of square meters per square meter (m2/m2). In broadleaf canopies, the leaf area is defined as the one-sided green part of leaves. In conifers, three definitions for LA have been used for the needles: total surface area, half of the total needle surface area, and projected area.

The definition “half the total leaf area” pertains to biological processes, such as gas exchange, whereas the definition “projected leaf area” is rarely used, because the projection of a given area in one direction may differ in another direction when leaves are not flat, thick, or 3D-shaped. Moreover, “ground surface area” is specifically defined as “horizontal ground surface area” to clarify LAI on a sloping surface. The definition “half the total leaf area per unit horizontal ground surface area” is suitable for all kinds of leaves and flat or sloping surfaces.

LAI is commonly used as an indicator of the growth rate of a plant. LAI is a complex variable that relates not only to the size of the canopy, but also to its density, and the angle at which leaves are oriented in relation to one another and to light sources. In addition, LAI varies with seasonal changes in plant activity, and is typically highest in the spring when new leaves are being produced and lowest in late summer or early fall when leaves senesce (and may be shed). The study of LAI is called "phyllometry."

## Interpretation and application

LAI is a measure for the total area of leaves per unit ground area and directly related to the amount of light that can be intercepted by plants. It is an important variable used to predict photosynthetic primary production, evapotranspiration and as a reference tool for crop growth. As such, LAI plays an essential role in theoretical production ecology. An inverse exponential relation between LAI and light interception, which is linearly proportional to the primary production rate, has been established:

$P=P_{\max }\left(1-e^{-c\cdot LAI}\right)$

where *P*max designates the maximum primary production and c designates a crop-specific growth coefficient. This inverse exponential function is called the **primary production function**.

LAI ranges from 0 (bare ground) to over 10 (dense conifer forests).

## Determination

LAI can be determined directly by taking a statistically significant sample of foliage from a plant canopy, measuring the leaf area per sample plot and dividing it by the plot land surface area. Indirect methods measure canopy geometry or light extinction and relate it to LAI.

### Direct methods

Direct methods can be easily applied on deciduous species by collecting leaves during leaf fall in traps of certain area distributed below the canopy. The area of the collected leaves can be measured using a leaf area meter or an image scanner and image analysis software (ImageJ) and mobile applications (Leafscan, Petiole Pro, Easy Leaf Area). The measured leaf area can then be divided by the area of the traps to obtain LAI. Alternatively, leaf area can be measured on a sub-sample of the collected leaves and linked to the leaf dry mass (e.g. via Specific Leaf Area, SLA cm2/g). That way it is not necessary to measure the area of all leaves one by one, but weigh the collected leaves after drying (at 60–80 °C for 48 h). Leaf dry mass multiplied by the specific leaf area is converted into leaf area. Direct methods in evergreen species are necessarily destructive. However, they are widely used in crops and pastures by harvesting the vegetation and measuring leaf area within a certain ground surface area. It is very difficult (and also unethical) to apply such destructive techniques in natural ecosystems, particularly in forests of evergreen tree species. Foresters have developed techniques that determine leaf area in evergreen forests through allometric relationships. Due to the difficulties and the limitations of the direct methods for estimating LAI, they are mostly used as reference for indirect methods that are easier and faster to apply.

### Indirect methods

Indirect methods of estimating LAI *in situ* can be divided roughly into at least three categories:

1. indirect contact LAI measurements such as plumb lines and inclined point quadrats
2. indirect non-contact measurements
3. indirect estimation from remote sensing such as LiDAR and multispectral imaging,including indices such as the Normalized difference vegetation index (NDVI)

Due to the subjectivity and labor involved with the first method, indirect non-contact measurements are typically preferred. Non-contact LAI tools, such as hemispherical photography, Hemiview Plant Canopy Analyser from Delta-T Devices, the CI-110 Plant Canopy Analyzer from CID Bio-Science, LAI-2200 Plant Canopy Analyzer from LI-COR Biosciences and the LP-80 LAI ceptometer from Decagon Devices, measure LAI in a non-destructive way. Hemispherical photography methods estimate LAI and other canopy structure attributes from analyzing upward-looking fisheye photographs taken beneath the plant canopy. The LAI-2200 calculates LAI and other canopy structure attributes from solar radiation measurements made with a wide-angle optical sensor. Measurements made above and below the canopy are used to determine canopy light interception at five angles, from which LAI is computed using a model of radiative transfer in vegetative canopies based on Beer's law . The LP-80 calculates LAI by means of measuring the difference between light levels above the canopy and at ground level, and factoring in the leaf angle distribution, solar zenith angle, and plant extinction coefficient. Such indirect methods, where LAI is calculated based upon observations of other variables (canopy geometry, light interception, leaf length and width, etc.) are generally faster, amenable to automation, and thereby allow for a larger number of spatial samples to be obtained. For reasons of convenience when compared to the direct (destructive) methods, these tools are becoming more and more important.

### Disadvantages of methods

The disadvantage of the direct method is that it is destructive, time consuming and expensive, especially if the study area is very large.

The disadvantage of the indirect method is that in some cases it can underestimate the value of LAI in very dense canopies, as it does not account for leaves that lie on each other, and essentially act as one leaf according to the theoretical LAI models. Ignorance of non-randomness within canopies may cause underestimation of LAI up to 25%, introducing path length distribution in the indirect method can improve the measuring accuracy of LAI. Indirect estimation of LAI is also sensitive to the data analysis methods of choices.
