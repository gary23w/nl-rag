---
title: "Bundle adjustment"
source: https://en.wikipedia.org/wiki/Bundle_adjustment
domain: photogrammetry-3d
license: CC-BY-SA-4.0
tags: photogrammetry 3d, structure from motion, bundle adjustment reconstruction, epipolar geometry photogrammetry
fetched: 2026-07-02
---

# Bundle adjustment

In photogrammetry and computer stereo vision, **bundle adjustment** is simultaneous refining of the 3D coordinates describing the scene geometry, the parameters of the relative motion, and the optical characteristics of the camera(s) employed to acquire the images, given a set of images depicting a number of 3D points from different viewpoints. Its name refers to the *geometrical bundles* of light rays originating from each 3D feature and converging on each camera's optical center, which are adjusted optimally according to an optimality criterion involving the corresponding image projections of all points.

## Uses

Bundle adjustment is almost always used as the last step of feature-based 3D reconstruction algorithms. It amounts to an optimization problem on the 3D structure and viewing parameters (i.e., camera pose and possibly intrinsic calibration and radial distortion), to obtain a reconstruction which is optimal under certain assumptions regarding the noise pertaining to the observed image features: If the image error is zero-mean Gaussian, then bundle adjustment is the Maximum Likelihood Estimator. Bundle adjustment was originally conceived in the field of photogrammetry during the 1950s and has increasingly been used by computer vision researchers during recent years.

## General approach

Bundle adjustment boils down to minimizing the reprojection error between the image locations of observed and predicted image points, which is expressed as the sum of squares of a large number of nonlinear, real-valued functions. Thus, the minimization is achieved using nonlinear least-squares algorithms. Of these, Levenberg–Marquardt has proven to be one of the most successful due to its ease of implementation and its use of an effective damping strategy that lends it the ability to converge quickly from a wide range of initial guesses. By iteratively linearizing the function to be minimized in the neighborhood of the current estimate, the Levenberg–Marquardt algorithm involves the solution of linear systems termed the normal equations. When solving the minimization problems arising in the framework of bundle adjustment, the normal equations have a sparse block structure owing to the lack of interaction among parameters for different 3D points and cameras. This can be exploited to gain tremendous computational benefits by employing a sparse variant of the Levenberg–Marquardt algorithm which explicitly takes advantage of the normal equations zeros pattern, avoiding storing and operating on zero-elements.

## Mathematical definition

Bundle adjustment amounts to jointly refining a set of initial camera and structure parameter estimates for finding the set of parameters that most accurately predict the locations of the observed points in the set of available images. More formally, assume that n 3D points are seen in m views and let $\mathbf {x} _{ij}$ be the projection of the i th point on image j . Let $\displaystyle v_{ij}$ denote the binary variables that equal 1 if point i is visible in image j and 0 otherwise. Assume also that each camera j is parameterized by a vector $\mathbf {a} _{j}$ and each 3D point i by a vector $\mathbf {b} _{i}$ . Bundle adjustment minimizes the total reprojection error with respect to all 3D point and camera parameters, specifically

$\min _{\mathbf {a} _{j},\,\mathbf {b} _{i}}\displaystyle \sum _{i=1}^{n}\;\displaystyle \sum _{j=1}^{m}\;v_{ij}\,d(\mathbf {Q} (\mathbf {a} _{j},\,\mathbf {b} _{i}),\;\mathbf {x} _{ij})^{2},$

where $\mathbf {Q} (\mathbf {a} _{j},\,\mathbf {b} _{i})$ is the predicted projection of point i on image j and $d(\mathbf {x} ,\,\mathbf {y} )$ denotes the Euclidean distance between the image points represented by vectors $\mathbf {x}$ and $\mathbf {y}$ . Because the minimum is computed over many points and many images, bundle adjustment is by definition tolerant to missing image projections, and if the distance metric is chosen reasonably (e.g., Euclidean distance), bundle adjustment will also minimize a physically meaningful criterion.
