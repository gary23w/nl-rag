---
title: "Photogrammetry"
source: https://en.wikipedia.org/wiki/Photogrammetry
domain: photogrammetry-3d
license: CC-BY-SA-4.0
tags: photogrammetry 3d, structure from motion, bundle adjustment reconstruction, epipolar geometry photogrammetry
fetched: 2026-07-02
---

# Photogrammetry

**Photogrammetry** is the science and technology of obtaining reliable information about physical objects and the environment through the process of recording, measuring and interpreting photographic images and patterns of electromagnetic radiant imagery and other phenomena.

While the invention of the method is attributed to Aimé Laussedat, the term "photogrammetry" was coined by the German architect Albrecht Meydenbauer, which appeared in his 1867 article "Die Photometrographie."

There are many variants of photogrammetry. One example is the extraction of three-dimensional measurements from two-dimensional data (i.e. images); for example, the distance between two points that lie on a plane parallel to the photographic image plane can be determined by measuring their distance on the image, if the scale of the image is known. Another is the extraction of accurate color ranges and values representing such quantities as albedo, specular reflection, metallicity, or ambient occlusion from photographs of materials for the purposes of physically based rendering.

Close-range photogrammetry refers to the collection of photography from a lesser distance than traditional aerial (or orbital) photogrammetry. Photogrammetric analysis may be applied to one photograph, or may use high-speed photography and remote sensing to detect, measure and record complex 2D and 3D motion fields by feeding measurements and imagery analysis into computational models in an attempt to successively estimate, with increasing accuracy, the actual, 3D relative motions.

From its beginning with the stereoplotters used to plot contour lines on topographic maps, it now has a very wide range of uses such as sonar, radar, and lidar.

## Methods

Photogrammetry uses methods from many disciplines, including optics and projective geometry. Digital image capturing and photogrammetric processing includes several well defined stages, which allow the generation of 2D or 3D digital models of the object as an end product. The data model on the right shows what type of information can go into and come out of photogrammetric methods.

The *3D coordinates* define the locations of object points in the 3D space. The *image coordinates* define the locations of the object points' images on the film or an electronic imaging device. The *exterior orientation* of a camera defines its location in space and its view direction. The *inner orientation* defines the geometric parameters of the imaging process. This is primarily the focal length of the lens, but can also include the description of lens distortions. Further *additional observations* play an important role: With *scale bars*, basically a known distance of two points in space, or known *fix points*, the connection to the basic measuring units is created.

Each of the four main variables can be an *input* or an *output* of a photogrammetric method.

Algorithms for photogrammetry typically attempt to minimize the sum of the squares of errors over the coordinates and relative displacements of the reference points. This minimization is known as bundle adjustment and is often performed using the Levenberg–Marquardt algorithm.

### Stereophotogrammetry

A special case, called **stereophotogrammetry**, involves estimating the three-dimensional coordinates of points on an object employing measurements made in two or more photographic images taken from different positions (see stereoscopy). Common points are identified on each image. A line of sight (or ray) can be constructed from the camera location to the point on the object. It is the intersection of these rays (triangulation) that determines the three-dimensional location of the point. More sophisticated algorithms can exploit other information about the scene that is known *a priori*, for example symmetries, in some cases allowing reconstructions of 3D coordinates from only one camera position. Stereophotogrammetry is emerging as a robust non-contacting measurement technique to determine dynamic characteristics and mode shapes of non-rotating and rotating structures. The collection of images for the purpose of creating photogrammetric models can be called more properly, polyoscopy, after Pierre Seguin

## Integration

Photogrammetric data can be complemented with range data from other techniques. Photogrammetry is more accurate in the x and y direction while range data are generally more accurate in the z direction . This range data can be supplied by techniques like LiDAR, laser scanners (using time of flight, triangulation or interferometry), white-light digitizers and any other technique that scans an area and returns x, y, z coordinates for multiple discrete points (commonly called "point clouds"). Photos can clearly define the edges of buildings when the point cloud footprint can not. It is beneficial to incorporate the advantages of both systems and integrate them to create a better product.

A 3D visualization can be created by georeferencing the aerial photos and LiDAR data in the same reference frame, orthorectifying the aerial photos, and then draping the orthorectified images on top of the LiDAR grid. It is also possible to create digital terrain models and thus 3D visualisations using pairs (or multiples) of aerial photographs or satellite (e.g. SPOT satellite imagery). Techniques such as adaptive least squares stereo matching are then used to produce a dense array of correspondences which are transformed through a camera model to produce a dense array of x, y, z data which can be used to produce digital terrain model and orthoimage products. Systems which use these techniques, e.g. the ITG system, were developed in the 1980s and 1990s but have since been supplanted by LiDAR and radar-based approaches, although these techniques may still be useful in deriving elevation models from old aerial photographs or satellite images.

## Applications

Photogrammetry is used in fields such as topographic mapping, architecture, filmmaking, engineering, manufacturing, quality control, police investigation, cultural heritage, and geology. Archaeologists use it to quickly produce plans of large or complex sites, and meteorologists use it to determine the wind speed of tornadoes when objective weather data cannot be obtained.

It is also used to combine live action with computer-generated imagery in movies post-production; *The Matrix* is a good example of the use of photogrammetry in film (details are given in the DVD extras). Photogrammetry was used extensively to create photorealistic environmental assets for video games including *The Vanishing of Ethan Carter* as well as EA DICE's *Star Wars Battlefront*. The main character of the game *Hellblade: Senua's Sacrifice* was derived from photogrammetric motion-capture models taken of actress Melina Juergens.

Photogrammetry is also commonly employed in collision engineering, especially with automobiles. When litigation for a collision occurs and engineers need to determine the exact deformation present in the vehicle, it is common for several years to have passed and the only evidence that remains is crash scene photographs taken by the police. Photogrammetry is used to determine how much the car in question was deformed, which relates to the amount of energy required to produce that deformation. The energy can then be used to determine important information about the crash (such as the velocity at time of impact).

This technology is also used for the inspection of submerged objects and infrastructure, thanks to its ability to produce precise, georeferenced 3D models. **Subsea photogrammetry** applications are numerous in the marine energy sector, including integrity monitoring of offshore wind turbine foundations, assessment of anchor chain wear, inspection of cable protection and burial systems, and overall evaluation of offshore structures.It also plays an increasing role in maritime and river civil engineering, particularly for inspecting port quays, dikes, dams, and other hydraulic structures. By providing reliable and reproducible metric data, underwater photogrammetry improves the monitoring of structural changes, optimizes maintenance operations, and reduces the costs associated with interventions in underwater environments.

### Mapping

Photomapping is the process of making a map with "cartographic enhancements" that have been drawn from a photomosaic that is "a composite photographic image of the ground," or more precisely, as a controlled photomosaic where "individual photographs are rectified for tilt and brought to a common scale (at least at certain control points)."

Rectification of imagery is generally achieved by "fitting the projected images of each photograph to a set of four control points whose positions have been derived from an existing map or from ground measurements. When these rectified, scaled photographs are positioned on a grid of control points, a good correspondence can be achieved between them through skillful trimming and fitting and the use of the areas around the principal point where the relief displacements (which cannot be removed) are at a minimum."

"It is quite reasonable to conclude that some form of photomap will become the standard general map of the future." They go on to suggest that, "photomapping would appear to be the only way to take reasonable advantage" of future data sources like high altitude aircraft and satellite imagery.

### Archaeology

Demonstrating the link between orthophotomapping and archaeology, historic airphotos photos were used to aid in developing a reconstruction of the Ventura mission that guided excavations of the structure's walls.

Photogrammetry has been as used in digital art restoration, particularly for the virtual reconstruction of historical sculptures and monuments destroyed during iconoclastic movements.

Overhead photography has been widely applied for mapping surface remains and excavation exposures at archaeological sites. Suggested platforms for capturing these photographs has included: War Balloons from World War I; rubber meteorological balloons; kites; wooden platforms, metal frameworks, constructed over an excavation exposure; ladders both alone and held together with poles or planks; three legged ladders; single and multi-section poles; bipods; tripods; tetrapods, and aerial bucket trucks ("cherry pickers").

Handheld, near-nadir, overhead digital photographs have been used with geographic information systems (GIS) to record excavation exposures.

Photogrammetry is increasingly being used in maritime archaeology because of the relative ease of mapping sites compared to traditional methods, allowing the creation of 3D maps which can be rendered in virtual reality.

A recent study applied high-resolution photogrammetry in combination with 3D scanning and quantitative morphometric analysis to compare Graeco-Roman funerary masks, enabling the re-identification of fragments and the attribution of archaeological provenience within museum collections.

### 3D modeling

A somewhat similar application is the scanning of objects to automatically make 3D models of them. Since photogrammetry relies on images, there are physical limitations when those images are of an object that has dark, shiny or clear surfaces. In those cases, the produced model often still contains gaps, so additional cleanup with software like MeshLab, netfabb or MeshMixer is often still necessary. Alternatively, spray painting such objects with matte finish can remove any transparent or shiny qualities.

Google Earth uses photogrammetry to create 3D imagery.

There is also a project called Rekrei that uses photogrammetry to make 3D models of lost/stolen/broken artifacts that are then posted online.

On Mount Stanley, an exhibition team sent out by Project Pressure created the first ever 3D model of the glacier using drone photography and GNSS technology showing a surface area decline of 29.5% between 2020 and 2024.

### Rock mechanics

High-resolution 3D point clouds derived from UAV or ground-based photogrammetry can be used to automatically or semi-automatically extract rock mass properties such as discontinuity orientations, persistence, and spacing.

## Software

There exist many software packages for photogrammetry; see comparison of photogrammetry software.
