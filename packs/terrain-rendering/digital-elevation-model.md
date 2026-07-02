---
title: "Digital elevation model"
source: https://en.wikipedia.org/wiki/Digital_elevation_model
domain: terrain-rendering
license: CC-BY-SA-4.0
tags: terrain rendering, heightmap terrain, geometry clipmap terrain, displacement terrain mesh
fetched: 2026-07-02
---

# Digital elevation model

A **digital elevation model** (**DEM**) or **digital surface model** (**DSM**) is a 3D computer graphics representation of elevation data to represent terrain or overlaying objects, commonly of a planet, moon, or asteroid. A "global DEM" refers to a discrete global grid. DEMs are used often in geographic information systems (GIS), and are the most common basis for digitally produced relief maps. A **digital terrain model** (**DTM**) represents specifically the ground surface while DEM and DSM may represent tree top canopy or building roofs.

While a DSM may be useful for landscape modeling, city modeling and visualization applications, a DTM is often required for flood or drainage modeling, land-use studies, geological applications, and other applications, and in planetary science.

## Terminology

There is no universal usage of the terms *digital elevation model* (DEM), *digital terrain model* (DTM) and *digital surface model* (DSM) in scientific literature. In most cases the term *digital surface model* represents the earth's surface and includes all objects on it. In contrast to a DSM, the *digital terrain model* (DTM) represents the bare ground surface without any objects like plants and buildings (see the figure on the right).

DEM is often used as a generic term for DSMs and DTMs, only representing height information without any further definition about the surface. Other definitions equalise the terms DEM and DTM, equalise the terms DEM and DSM, define the DEM as a subset of the DTM, which also represents other morphological elements, or define a DEM as a rectangular grid and a DTM as a three-dimensional model (TIN). Most of the data providers (USGS, ERSDAC, CGIAR, Spot Image) use the term DEM as a generic term for DSMs and DTMs. Some datasets such as SRTM or the ASTER GDEM are originally DSMs, although in forested areas, SRTM reaches into the tree canopy giving readings somewhere between a DSM and a DTM). DTMs are created from high resolution DSM datasets using complex algorithms to filter out buildings and other objects, a process known as "bare-earth extraction". In the following, the term DEM is used as a generic term for DSMs and DTMs.

## Types

A DEM can be represented as a raster (a grid of squares, also known as a heightmap when representing elevation) or as a vector-based triangular irregular network (TIN). The TIN DEM dataset is also referred to as a primary (measured) DEM, whereas the Raster DEM is referred to as a secondary (computed) DEM. The DEM could be acquired through techniques such as photogrammetry, lidar, IfSAR or InSAR, land surveying, etc. (Li et al. 2005).

DEMs are commonly built using data collected using remote sensing techniques, but they may also be built from land surveying.

### Rendering

The digital elevation model itself consists of a matrix of numbers, but the data from a DEM is often rendered in visual form to make it understandable to humans. This visualization may be in the form of a contoured topographic map, or could use shading and false color assignment (or "pseudo-color") to render elevations as colors (for example, using green for the lowest elevations, shading to red, with white for the highest elevation.).

Visualizations are sometimes also done as oblique views, reconstructing a synthetic visual image of the terrain as it would appear looking down at an angle. In these oblique visualizations, elevations are sometimes scaled using "vertical exaggeration" in order to make subtle elevation differences more noticeable. Some scientists, however, object to vertical exaggeration as misleading the viewer about the true landscape.

## Production

Mappers may prepare digital elevation models in a number of ways, but they frequently use remote sensing rather than direct survey data.

Older methods of generating DEMs often involve interpolating digital contour maps that may have been produced by direct survey of the land surface. This method is still used in mountain areas, where interferometry is not always satisfactory. Note that contour line data or any other sampled elevation datasets (by GPS or ground survey) are not DEMs, but may be considered digital terrain models. A DEM implies that elevation is available continuously at each location in the study area.

### Satellite mapping

One powerful technique for generating digital elevation models is interferometric synthetic aperture radar where two passes of a radar satellite (such as RADARSAT-1 or TerraSAR-X or Cosmo SkyMed), or a single pass if the satellite is equipped with two antennas (like the SRTM instrumentation), collect sufficient data to generate a digital elevation map tens of kilometers on a side with a resolution of around ten meters. Other kinds of stereoscopic pairs can be employed using the digital image correlation method, where two optical images are acquired with different angles taken from the same pass of an airplane or an Earth Observation Satellite (such as the HRS instrument of SPOT5 or the VNIR band of ASTER).

The SPOT 1 satellite (1986) provided the first usable elevation data for a sizeable portion of the planet's landmass, using two-pass stereoscopic correlation. Later, further data were provided by the European Remote-Sensing Satellite (ERS, 1991) using the same method, the Shuttle Radar Topography Mission (SRTM, 2000) using single-pass SAR and the Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER, 2000) instrumentation on the Terra satellite using double-pass stereo pairs.

The HRS instrument on SPOT 5 has acquired over 100 million square kilometers of stereo pairs.

### Planetary mapping

A tool of increasing value in planetary science has been use of orbital altimetry used to make digital elevation map of planets. A primary tool for this is laser altimetry but radar altimetry is also used. Planetary digital elevation maps made using laser altimetry include the Mars Orbiter Laser Altimeter (MOLA) mapping of Mars, the Lunar Orbital Laser Altimeter (LOLA) and Lunar Altimeter (LALT) mapping of the Moon, and the Mercury Laser Altimeter (MLA) mapping of Mercury. In planetary mapping, each planetary body has a unique reference surface. New Horizons' Long Range Reconnaissance Imager used stereo photogrammetry to produce partial surface elevation maps of Pluto and 486958 Arrokoth.

### Methods for obtaining elevation data used to create DEMs

- Lidar
- Radar
- Stereo photogrammetry from aerial surveys
  - Structure from motion / Multi-view stereo applied to aerial photography
- Block adjustment from optical satellite imagery
- Interferometry from radar data
- Real Time Kinematic GPS
- Topographic maps
- Theodolite or total station
- Doppler radar
- Focus variation
- Inertial surveys
- Surveying and mapping drones
- Range imaging

### Accuracy

The quality of a DEM is a measure of how accurate elevation is at each pixel (absolute accuracy) and how accurately is the morphology presented (relative accuracy). Quality assessment of DEM can be performed by comparison of DEMs from different sources. Several factors play an important role for quality of DEM-derived products:

- terrain roughness;
- sampling density (elevation data collection method);
- grid resolution or pixel size;
- interpolation algorithm;
- vertical resolution;
- terrain analysis algorithm;
- Reference 3D products include quality masks that give information on the coastline, lake, snow, clouds, correlation etc.

## Uses

Common uses of DEMs include:

- Extracting terrain parameters for geomorphology
- Modeling water flow for hydrology or mass movement (for example avalanches and landslides)
- Modeling soils wetness with Cartographic Depth to Water Indexes (DTW-index)
- Creation of relief maps
- Rendering of 3D visualizations.
- 3D flight planning and TERCOM
- Creation of physical models (including raised relief maps and 3D printed terrain models)
- Rectification of aerial photography or satellite imagery
- Reduction (terrain correction) of gravity measurements (gravimetry, physical geodesy)
- Terrain analysis in geomorphology and physical geography
- Geographic information systems (GIS)
- Engineering and infrastructure design
- Satellite navigation (for example GPS and GLONASS)
- Line-of-sight analysis
- Base mapping
- Flight simulation
- Train simulation
- Precision farming and forestry
- Surface analysis
- Intelligent transportation systems (ITS)
- Auto safety / advanced driver-assistance systems (ADAS)
- Archaeology
