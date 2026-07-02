---
title: "Epipolar geometry"
source: https://en.wikipedia.org/wiki/Epipolar_geometry
domain: photogrammetry-3d
license: CC-BY-SA-4.0
tags: photogrammetry 3d, structure from motion, bundle adjustment reconstruction, epipolar geometry photogrammetry
fetched: 2026-07-02
---

# Epipolar geometry

**Epipolar geometry** is the geometry of stereo vision. When two cameras view a 3D scene from two distinct positions, there are a number of geometric relations between the 3D points and their projections onto the 2D images that lead to constraints between the image points. These relations are derived based on the assumption that the cameras can be approximated by the pinhole camera model.

## Definitions

The figure below depicts two pinhole cameras looking at point **X**. In real cameras, the image plane is actually behind the focal center, and produces an image that is symmetric about the focal center of the lens. Here, however, the problem is simplified by placing a *virtual image plane* in front of the focal center i.e. optical center of each camera lens to produce an image not transformed by the symmetry. **O**L and **O**R represent the centers of symmetry of the two cameras lenses. **X** represents the point of interest in both cameras. Points **x**L and **x**R are the projections of point **X** onto the image planes.

Each camera captures a 2D image of the 3D world. This conversion from 3D to 2D is referred to as a perspective projection and is described by the pinhole camera model. It is common to model this projection operation by rays that emanate from the camera, passing through its focal center. Each emanating ray corresponds to a single point in the image.

### Epipole or epipolar point

Since the optical centers of the cameras lenses are distinct, each center projects onto a distinct point into the other camera's image plane. These two image points, denoted by **e**L and **e**R, are called *epipoles* or *epipolar points*. Both epipoles **e**L and **e**R in their respective image planes and both optical centers **O**L and **O**R lie on a single 3D line.

### Epipolar line

The line **O**L–**X** is seen by the left camera as a point because it is directly in line with that camera's lens optical center. However, the right camera sees this line as a line in its image plane. That line (**e**R–**x**R) in the right camera is called an *epipolar line*. Symmetrically, the line **O**R–**X** is seen by the right camera as a point and is seen as epipolar line **e**L–**x**Lby the left camera.

An epipolar line is a function of the position of point **X** in the 3D space, i.e. as **X** varies, a set of epipolar lines is generated in both images. Since the 3D line **O**L–**X** passes through the optical center of the lens **O**L, the corresponding epipolar line in the right image must pass through the epipole **e**R (and correspondingly for epipolar lines in the left image). All epipolar lines in one image contain the epipolar point of that image. In fact, any line which contains the epipolar point is an epipolar line since it can be derived from some 3D point **X**.

### Epipolar plane

As an alternative visualization, consider the points **X**, **O**L & **O**R that form a plane called the *epipolar plane*. The epipolar plane intersects each camera's image plane where it forms lines—the epipolar lines. The epipolar plane and all epipolar lines intersect the epipoles regardless of where **X** is located.

## Epipolar constraint and triangulation

If the relative position of the two cameras is known, this leads to two important observations:

- Assume the projection point **x**L is known, and the epipolar line **e**R–**x**R is known and the point **X** projects into the right image, on a point **x**R which must lie on this particular epipolar line. This means that for each point observed in one image the same point must be observed in the other image on a known epipolar line. This provides an *epipolar constraint*: the projection of X on the right camera plane **x**R must be contained in the **e**R–**x**R epipolar line. All points X e.g. **X**1, **X**2, **X**3 on the **O**L–**X**L line will verify that constraint. It means that it is possible to test if two points correspond to the same 3D point. Epipolar constraints can also be described by the fundamental matrix, or in the case of normalized image coordinates, the essential matrix between the two cameras.
- If the points **x**L and **x**R are known, their projection lines are also known. If the two image points correspond to the same 3D point **X** the projection lines must intersect precisely at **X**. This means that **X** can be calculated from the coordinates of the two image points, a process called *triangulation*.

## Simplified cases

The epipolar geometry is simplified if the two camera image planes coincide. In this case, the epipolar lines also coincide (**e**L–**X**L = **e**R–**X**R). Furthermore, the epipolar lines are parallel to the line **O**L–**O**R between the centers of projection, and can in practice be aligned with the horizontal axes of the two images. This means that for each point in one image, its corresponding point in the other image can be found by looking only along a horizontal line. If the cameras cannot be positioned in this way, the image coordinates from the cameras may be transformed to emulate having a common image plane. This process is called image rectification.

## Epipolar geometry of pushbroom sensor

In contrast to the conventional frame camera which uses a two-dimensional CCD, pushbroom camera adopts an array of one-dimensional CCDs to produce long continuous image strip which is called "image carpet". If the one-dimensional sensor is moved over the focal plane of a static scene with fixed in place optics it is equivalent to a two-dimensional sensor other than that each part of the image is captured at a different time. Epipolar geometry of this sensor is quite different from that of pinhole projection cameras. First, the epipolar line of pushbroom sensor is not straight, but hyperbola-like curve. Second, epipolar 'curve' pair does not exist. However, in some special conditions, the epipolar geometry of the satellite images could be considered as a linear model.
