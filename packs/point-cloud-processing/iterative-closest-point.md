---
title: "Iterative closest point"
source: https://en.wikipedia.org/wiki/Iterative_closest_point
domain: point-cloud-processing
license: CC-BY-SA-4.0
tags: point cloud processing, point cloud registration, iterative closest point, lidar point cloud
fetched: 2026-07-02
---

# Iterative closest point

**Iterative closest point** (**ICP**) is a point cloud registration algorithm employed to minimize the difference between two clouds of points. ICP is often used to reconstruct 2D or 3D surfaces from different scans, to localize robots and achieve optimal path planning (especially when wheel odometry is unreliable due to slippery terrain), to co-register bone models, etc.

## Overview

The Iterative Closest Point algorithm keeps one point cloud, the reference or target, fixed, while transforming the other, the source, to best match the reference. The transformation (combination of translation and rotation) is iteratively estimated in order to minimize an error metric, typically the sum of squared differences between the coordinates of the matched pairs. ICP is one of the widely used algorithms in aligning three dimensional models given an initial guess of the rigid transformation required. The ICP algorithm was first introduced by Chen and Medioni, and Besl and McKay.

Inputs: reference and source point clouds, initial estimation of the transformation to align the source to the reference (optional), criteria for stopping the iterations.

Output: refined transformation.

Essentially, the algorithm steps are:

1. For each point (from the whole set of vertices usually referred to as dense or a selection of pairs of vertices from each model) in the source point cloud, match the closest point in the reference point cloud (or a selected set).
2. Estimate the combination of rotation and translation using a root mean square point-to-point distance metric minimization technique which will best align each source point to its match found in the previous step. This step may also involve weighting points and rejecting outliers prior to alignment.
3. Transform the source points using the obtained transformation.
4. Iterate (re-associate the points, and so on).

Zhang proposes a modified *k*-d tree algorithm for efficient closest point computation. In this work a statistical method based on the distance distribution is used to deal with outliers, occlusion, appearance, and disappearance, which enables subset-subset matching.

There exist many ICP variants, from which point-to-point and point-to-plane are the most popular. The latter usually performs better in structured environments.

### Non-rigid ICP

While traditional ICP assumes rigid transformations, non-rigid ICP methods extend the algorithm to handle deformable objects and non-rigid registration scenarios. These methods incorporate additional constraints and regularization terms to model local deformations while maintaining surface coherence.

## Implementations

- MeshLab an open source mesh processing tool that includes a GNU General Public License implementation of the ICP algorithm.
- CloudCompare an open source point and model processing tool that includes an implementation of the ICP algorithm. Released under the GNU General Public License.
- PCL (Point Cloud Library) is an open-source framework for n-dimensional point clouds and 3D geometry processing. It includes several variants of the ICP algorithm.
- Open source C++ implementations of the ICP algorithm are available in VTK, ITK and Open3D libraries.
- libpointmatcher is an implementation of point-to-point and point-to-plane ICP released under a BSD license.
- simpleICP is an implementation of a rather simple version of the ICP algorithm in various languages.
- 3D-nonrigid-ICP is an open-source implementation of a non-rigid ICP method.
