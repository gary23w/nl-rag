---
title: "Point Cloud Library"
source: https://en.wikipedia.org/wiki/Point_Cloud_Library
domain: point-cloud-processing
license: CC-BY-SA-4.0
tags: point cloud processing, point cloud registration, iterative closest point, lidar point cloud
fetched: 2026-07-02
---

# Point Cloud Library

The **Point Cloud Library** (**PCL**) is an open-source library of algorithms for point cloud processing tasks and 3D geometry processing, such as occur in three-dimensional computer vision. The library contains algorithms for filtering, feature estimation, surface reconstruction, 3D registration, model fitting, object recognition, and segmentation. Each module is implemented as a smaller library that can be compiled separately (for example, libpcl_filters, libpcl_features, libpcl_surface, ...). PCL has its own data format for storing point clouds - **PCD** (Point Cloud Data), but also allows datasets to be loaded and saved in many other formats. It is written in C++ and released under the BSD license.

These algorithms have been used, for example, for perception in robotics to filter outliers from noisy data, stitch 3D point clouds together, segment relevant parts of a scene, extract keypoints and compute descriptors to recognize objects in the world based on their geometric appearance, and create surfaces from point clouds and visualize them.

PCL requires several third-party libraries to function, which must be installed. Most mathematical operations are implemented using the Eigen library. The visualization module for 3D point clouds is based on VTK. Boost is used for shared pointers and the FLANN library for quick k-nearest neighbor search. Additional libraries such as Qhull, OpenNI, or Qt are optional and extend PCL with additional features.

PCL is cross-platform software that runs on the most commonly used operating systems: Linux, Windows, macOS and Android. The library is fully integrated with the Robot Operating System (ROS) and provides support for OpenMP and Intel Threading Building Blocks (TBB) libraries for multi-core parallelism.

The library is constantly updated and expanded, and its use in various industries is constantly growing. For example, PCL participated in the Google Summer of Code 2020 initiative with three projects. One was the extension of PCL for use with Python using Pybind11.

A large number of examples and tutorials are available on the PCL website, either as C++ source files or as tutorials with a detailed description and explanation of the individual steps.

## Applications

Point cloud library is widely used in many different fields, here are some examples:

- stitching 3D point clouds together
- recognize 3D objects on their geometric appearance
- filtering and smoothing out noisy data
- create surfaces from point clouds
- aligning a previously captured model of an object to some newly captured data
- cluster recognition and 6DoF pose estimation
- point cloud streaming to mobile devices with real-time visualization

## 3rd party libraries

PCL requires for its installation several third-party libraries, which are listed below. Some libraries are optional and extend PCL with additional features. The PCL library is built with the CMake build system (http://www.cmake.org/) at least in version 3.5.0.

Mandatory libraries:

- **Boost** (http://www.boost.org/) at least version 1.46.1. This set of C++ libraries is used for threading and mainly for shared pointers, so there is no need to re-copy data that is already in the system.
- **Eigen** (http://eigen.tuxfamily.org/) is required at least in version 3.0.0. It is an open-source template library for linear algebra (matrices, vectors). Most mathematical operations (SSE optimized) in PCL are implemented with Eigen.
- **FLANN** (http://www.cs.ubc.ca/research/flann/) in version 1.6.8 or higher. It is a library that performs a fast approximate nearest neighbor search in high dimensional spaces. In PCL, it is especially important in the kdtree module for fast k-nearest neighbor search operations.
- **VTK - Visualization ToolKit** (http://www.vtk.org/) at least version 5.6.1. Multi-platform software system for rendering 3D point cloud, modeling, image processing, volume rendering. Used in visualization module for point cloud rendering and visualization.

Optional libraries that enable some additional features:

- **QHULL** in version >= 2011.1 (http://www.qhull.org/) implements computation of the convex hull, Delaunay triangulation, Voronoi diagram, and so on. In PCL it is used for convex/concave hull decomposition on the surface.
- **OpenNI** in version >= 1.1.0.25 (http://www.openni.org/) provides a single unified interface to depth sensors. It is used to retrieve point clouds from devices.
- **Qt** version >= 4.6 (https://www.qt.io/) is a cross-platform C++ framework used for developing applications with a graphical user interface (GUI).
- **Googletest** in version >= 1.6.0 (http://code.google.com/p/googletest/) is a C++ testing framework. In PCL, it is used to build test units.

## PCD File Format

The **PCD** (**Point Cloud Data**) is a file format for storing 3D point cloud data. It was created because existing formats did not support some of the features provided by the PCL library. PCD is the primary data format in PCL, but the library also offers the ability to save and load data in other formats (such as PLY, IFS, VTK, STL, OBJ, X3D). However, these other formats do not have the flexibility and speed of PCD files. One of the PCD advantages is the ability to store and process organized point cloud datasets. Another is very fast saving and loading of points that are stored in binary form.

### Versions

The PCD version is specified with the numbers 0.x (e.g., 0.5, 0.6, etc.) in the header of each file. The official version in 2020 is PCD **0.7** (**PCD_V7**). The main difference compared to version 0.6 is that a new header - VIEWPOINT has been added. It specifies the information about the orientation of the sensor relative to the dataset.

### File structure

The PCD file is divided into two parts - **header** and **data**. The header has a precisely defined format and contains the necessary information about the point cloud data that are stored in it. The header must be encoded in ASCII, however, the data can be stored in ASCII or binary format. Thanks to the fact that the ASCII format is more human readable, it can be opened in standard software tools and easily edited.

In version 0.7 the *version* of the PCD file is at the beginning of the header, followed by the *name*, *size*, and *type* of each dimension of the stored data. It also shows a number of points (*height***width*) in the whole cloud and information about whether the point cloud dataset is organized or unorganized. The *data* type specifies in which format the point cloud data are stored (ASCII or binary). The header is followed by a set of points. Each point can be stored on a separate line (unorganized point-cloud) or they are stored in an image-like organized structure (organized point-cloud). More detailed information about header entries can be found in documentation. Below is an example of a PCD file. The order of header entries is important!

```
# .PCD v.7 - Point Cloud Data file format
VERSION .7
FIELDS x y z rgb
SIZE 4 4 4 4
TYPE F F F F
COUNT 1 1 1 1
WIDTH 213
HEIGHT 1
VIEWPOINT 0 0 0 1 0 0 0
POINTS 213
DATA ascii
0.93773 0.33763 0 4.2108e+06
0.90805 0.35641 0 4.2108e+06
0.81915 0.32 0 4.2108e+06
0.97192 0.278 0 4.2108e+06
...
...
```

## History

The development of the Point Cloud Library started in March 2010 at Willow Garage. The project initially resided on a sub domain of Willow Garage then moved to a new website www.pointclouds.org in March 2011. PCL's first official release (Version 1.0) was released two months later in May 2011.

## Modules

PCL is divided into several smaller code libraries that can be compiled separately. Some of the most important modules and their functions are described below.

### Filters

When scanning a 3D point cloud, errors and various deviations can occur, which causes noise in the data. This complicates the estimation of some local point cloud characteristics, such as surface normals. These inaccuracies can lead to significant errors in further processing and it is therefore advisable to remove them with a suitable filter. The **pcl_filters** library provides several useful filters for removing outliers and noise and also downsampling the data. Some of them use simple criteria to trim points, others use statistical analysis.

- **PassThrough** filter - is used to filter points in one selected dimension. This means that it can cut off points that are not within the range specified by the user.
- **VoxelGrid** filter - creates a grid of voxels in a point cloud. The points inside each voxel are then approximated by their centroid. This leads to downsampling (reduction of the number of points) in the point cloud data.
- **StatisticalOutlierRemoval** filter - It removes noise from a point cloud dataset using statistical analysis techniques applied to each point's neighborhood and trim all points whose mean distances are outside a defined interval.
- **RadiusOutlierRemoval** filter - removes those points that have less than the selected number of neighbors in the defined neighborhood.

### Features

The **pcl_features** library contains algorithms and data structures for 3D feature estimation. Mostly used local geometric features are the point normal and underlying surface's estimated curvature. The features describe geometrical patterns at a certain point based on selected k-neighborhood (data space selected around the point). The neighborhood can be selected by determining a fixed number of points in the closest area or defining a radius of a sphere around the point.

One of the easiest implemented methods for estimating the surface normal is an analysis of the eigenvectors and eigenvalues of a covariance matrix created from the neighborhood of the point. Point Feature Histograms (or faster FPFH) descriptors are an advanced feature representation and depend on normal estimations at each point. It generalizes the mean curvature around the point using a multidimensional histogram of values. Some of other descriptors in the library are Viewpoint Feature Histogram (VFH) descriptor, NARF descriptors, Moment of inertia and eccentricity based descriptors, Globally Aligned Spatial Distribution (GASD) descriptors, and more.

### Segmentation

The **pcl_segmentation** library contains algorithms for segmenting a point cloud into different clusters. Clustering is often used to divide the cloud into individual parts, that can be further processed. There are implemented several classes, that support various segmentation methods:

- **Plane model** segmentation - simple algorithm that finds all the points that support a plane model in the point cloud
- **Euclidean** clustering - creates clusters of points based on Euclidean distance
- **Conditional Euclidean** clustering - clustering points based on Euclidean distance and a user-defined condition
- **Region growing** segmentation - merge the points that are close enough in terms of the smoothness constraint
- **Color-based region growing** segmentation - same concept as the Region growing, but uses color instead of normals
- **Min-Cut** based binary segmentation - divides the cloud on foreground and background sets of points
- **Difference of Normals** Based Segmentation - scale based segmentation, finding points that belong within the scale parameters given
- **Supervoxel** clustering - generates volumetric over-segmentations of 3D point cloud data

### Visualization

The **pcl_visualization** library is used to quickly and easily visualize 3D point cloud data. The package makes use of the VTK library for 3D rendering of clouds and range images. The library offers:

- The **CloudViewer** class is for a simple point cloud visualization.
- **RangeImageVisualizer** can be used to visualize a range image as a 3D point cloud or as a picture where the colors correspond to range values.
- **PCLVisualizer** is a visualization class with several applications. It can display both simple point cloud and point cloud that contains colour data. Unlike CloudViewer, it can also draw interesting point cloud information such as normals, principal curvatures and geometries. It can display multiple point clouds side-by-side so they can be easily compared, or draw various primitive shapes (e.g., cylinders, spheres, lines, polygons, etc.) either from sets of points or from parametric equations.
- **PCLPlotter** class is used for easy plotting graphs, from polynomial functions to histograms. It can process different types of plot input (coordinates, functions) and does auto-coloring.
- **PCLHistogramVisualizer** is a histogram visualization module for 2D plots.

### Registration

Registration is the problem of aligning various point cloud datasets acquired from different views into a single point cloud model. The **pcl_registration** library implements number of point cloud registration algorithms for both organized and unorganized datasets. The task is to identify the corresponding points between the data sets and find a transformation that minimizes their distance.

The iterative closest point algorithm minimizes the distances between the points of two pointclouds. It can be used for determining if one PointCloud is just a rigid transformation of another. Normal Distributions Transform (NDT) is a registration algorithm that can be used to determine a rigid transformation between two point clouds that have over 100,000 points.

### Sample Consensus

The ***sample_consensus*** library holds SAmple Consensus (SAC) methods like RANSAC and models to detect specific objects in point clouds. Some of the models implemented in this library include plane models that are often used to detect interior surfaces such as walls and floors. Next models are the lines, 2D and 3D circles in a plane, sphere, cylinder, cone, a model for determining a line parallel with a given axis, a model for determining a plane perpendicular to a user-specified axis, plane parallel to a user-specified axis, etc. These can be used to detect objects with common geometric structures (e.g., fitting a cylinder model to a mug).

Robust sample consensus estimators that are available in the library:

- SAC_RANSAC - RANdom SAmple Consensus
- SAC_LMEDS - Least Median of Squares
- SAC_MSAC - M-Estimator SAmple Consensus
- SAC_RRANSAC - Randomized RANSAC
- SAC_RMSAC - Randomized MSAC
- SAC_MLESAC - Maximum LikeLihood Estimation SAmple Consensus
- SAC_PROSAC - PROgressive SAmple Consensus

### Surface

Several algorithms for surface reconstruction of 3D point clouds are implemented in the **pcl_surface** library. There are several ways to reconstruct the surface. One of the most commonly used is meshing, and the PCL library has two algorithms: very fast triangulation of original points and slower networking, which also smooths and fills holes. If the cloud is noisy, it is advisable to use surface smoothing using one of the implemented algorithms.

The Moving Least Squares (MLS) surface reconstruction method is a resampling algorithm that can reconstruct missing parts of a surface. Thanks to higher order polynomial interpolations between surrounding data points, MLS can correct and smooth out small errors caused by scanning.

Greedy Projection Triangulation implements an algorithm for fast surface triangulation on an unordered PointCloud with normals. The result is a triangle mesh that is created by projecting the local neighborhood of a point along the normal of the point. It works best if the surface is locally smooth and there are smooth transitions between areas with different point densities. Many parameters can be set that are taken into account when connecting points (how many neighbors are searched, the maximum distance for a point, minimum and maximum angle of a triangle).

The library also implements functions for creating a concave or convex hull polygon for a plane model, Grid projection surface reconstruction algorithm, marching cubes, ear clipping triangulation algorithm, Poisson surface reconstruction algorithm, etc.

### I/O

The **io_library** allows you to load and save point clouds to files, as well as capture clouds from various devices. It includes functions that allow you to concatenate the points of two different point clouds with the same type and number of fields. The library can also concatenate fields (e.g., dimensions) of two different point clouds with same number of points.

Starting with **PCL 1.0** the library offers a new generic grabber interface that provides easy access to different devices and file formats. The first devices supported for data collection were OpenNI compatible cameras (tested with *Primesense Reference Design*, *Microsoft Kinect* and *Asus Xtion Pro cameras*). As of **PCL 1.7**, point cloud data can be also obtained from the Velodyne High Definition LiDAR (HDL) system, which produces 360 degree point clouds. PCL supports both the original *HDL-64e* and *HDL-32e*. There is also a new driver for Dinast Cameras (tested with *IPA-1110*, *Cyclopes II* and *IPA-1002 ng T-Less NG*). **PCL 1.8** brings support for IDS-Imaging Ensenso cameras, DepthSense cameras (e.g. *Creative Senz3D*, *DepthSense DS325*), and davidSDK scanners.

### KdTree

The **pcl_kdtree** library provides the kd-tree data-structure for organizing a set of points in a space with k dimensions. Used to find the K nearest neighbors (using FLANN) of a specific point or location.

### Octree

The **pcl_octree** library implements the octree hierarchical tree data structure for point cloud data. The library provides nearest neighbor search algorithms, such as “Neighbors within Voxel Search”, “K Nearest Neighbor Search” and “Neighbors within Radius Search”. There are also several octree types that differ by their leaf node's properties. Each leaf node can hold a single point or a list of point indices, or it does not store any point information. The library can be also used for detection of spatial changes between multiple unorganized point clouds by recursive comparison of octet tree structures.

The **pcl_search** library implements methods for searching for nearest neighbors using different data structures, that can be found in other modules, such as KdTree, Octree, or specialized search for organized datasets.

### Range Image

The **range_image** library contains two classes for representing and working with range images whose pixel values represent a distance from the sensor. The range image can be converted to a point cloud if the sensor position is specified or the borders can be extracted from it.

### Keypoints

The **pcl_keypoints** library contains implementations of point cloud keypoint detection algorithms (AGAST corner point detector, Harris detector, BRISK detector, etc.).

### Common

The **pcl_common** library contains the core data structures for point cloud, types for point representation, surface normals, RGB color values, etc. There are also implemented useful methods for computing distances, mean values and covariance, geometric transformations, and more. The common library is mainly used by other PCL modules.
