---
title: "Parallel coordinates"
source: https://en.wikipedia.org/wiki/Parallel_coordinates
domain: parallel-coordinates
license: CC-BY-SA-4.0
tags: parallel coordinates, andrews plot, high dimensional, multivariate plot
fetched: 2026-07-02
---

# Parallel coordinates

**Parallel Coordinates** plots are a common method of visualizing high-dimensional datasets to analyze multivariate data having multiple variables, or attributes.

To plot, or visualize, a set of points in *n*-dimensional space, *n* parallel lines are drawn over the background representing coordinate axes, typically oriented vertically with equal spacing. Points in *n*-dimensional space are represented as individual polylines with *n* vertices placed on the parallel axes corresponding to each coordinate entry of the *n*-dimensional point, vertices are connected with *n-1* polyline segments.

This data visualization is similar to time series visualization, except that Parallel Coordinates are applied to data which do not correspond with chronological time. Therefore, different axes arrangements can be of interest, including reflecting axes horizontally, otherwise inverting the attribute range.

## History

The concept of Parallel Coordinates is often said to originate in 1885 by a French mathematician Philbert Maurice d'Ocagne. d'Ocagne sought a way to provide graphical calculation of mathematical functions using alignment diagrams called nomograms which used parallel axes with different scales. For example, a three-variable equation could be solved using three parallel axes, marking known values on their scales, then drawing a line between them, with an unknown read from the scale at the point where the line intersects that scale.

The use of Parallel Coordinates as a visualization technique to show data is also often said to have originated earlier with Henry Gannett in work preceding the Statistical Atlas of the United States for the 1890 Census, for example his "General Summary, Showing the Rank of States, by Ratios, 1880", that shows the rank of 10 measures (population, occupations, wealth, manufacturing, agriculture, and so forth) on parallel axes connected by lines for each state.

However, both d'Ocagne and Gannet were far preceded in this by André-Michel Guerry, Plate IV, "Influence de l'Age", where he showed rankings of crimes against persons by age along parallel axes, connecting the same crime across age groups.

Parallel Coordinates were popularised again 87 years later by Alfred Inselberg in 1985 and systematically developed as a coordinate system starting from 1977. Some important applications are in collision avoidance algorithms for air traffic control (1987—3 USA patents), data mining (USA patent), computer vision (USA patent), Optimization, process control, more recently in intrusion detection and elsewhere.

## Higher dimensions

On the plane with an XY Cartesian coordinate system, adding more dimensions in parallel coordinates (often abbreviated ||-coords, PCP, or PC) involves adding more axes. The value of parallel coordinates is that certain geometrical properties in high dimensions transform into easily seen 2D patterns. For example, a set of points on a line in *n*-space transforms to a set of polylines in parallel coordinates all intersecting at *n* − 1 points. For *n* = 2 this yields a point-line duality pointing out why the mathematical foundations of parallel coordinates are developed in the projective rather than Euclidean space. A pair of lines intersects at a unique point which has two coordinates and, therefore, can correspond to a unique line which is also specified by two parameters (or two points). In contrast, more than two points are required to specify a curve and also a pair of curves may not have a unique intersection. Hence by using curves in parallel coordinates instead of lines, the point line duality is lost together with all the other properties of projective geometry, and the known nice higher-dimensional patterns corresponding to (hyper)planes, curves, several smooth (hyper)surfaces, proximities, convexity and recently non-orientability. The goal is to map n-dimensional relations into 2D patterns. Hence, parallel coordinates is not a point-to-point mapping but rather a *n*D subset to 2D subset mapping, there is no loss of information. Note: even a point in nD is not mapped into a point in 2D, but to a polygonal line—a subset of 2D.

## Statistical considerations

When used for statistical data visualisation there are three important considerations: the order, the rotation, and the scaling of the axes.

The order of the axes is critical for finding features, and in typical data analysis many reorderings will need to be tried. Some authors have come up with ordering heuristics which may create illuminating orderings.

The rotation of the axes is a translation in the parallel coordinates and if the lines intersected outside the parallel axes it can be translated between them by rotations. The simplest example of this is rotating the axis by 180 degrees.

Scaling is necessary because the plot is based on interpolation (linear combination) of consecutive pairs of variables. Therefore, the variables must be in common scale, and there are many scaling methods to be considered as part of data preparation process that can reveal more informative views.

A smooth parallel coordinate plot is achieved with splines. In the smooth plot, every observation is mapped into a parametric line (or curve), which is smooth, continuous on the axes, and orthogonal to each parallel axis. This design emphasizes the quantization level for each data attribute.

## Reading

Inselberg (Inselberg 1997) made a full review of how to visually read out parallel coordinates relational patterns. When most lines between two parallel axes are somewhat parallel to each other, it suggests a positive relationship between these two dimensions. When lines cross in a kind of superposition of X-shapes, it's a negative relationship. When lines cross randomly or are parallel, it shows there is no particular relationship.

## Limitations

In parallel coordinates, each axis can have at most two neighboring axes (one on the left, and one on the right). For a *n*-dimensional data set, at most *n*-1 relationships can be shown at a time without altering the approach. In time series visualization, there exists a natural predecessor and successor; therefore in this special case, there exists a preferred arrangement. However, when the axes do not have a unique order, finding a good axis arrangement requires the use of experimentation and feature engineering. To explore more relationships, axes may be reordered or restructured.

One approach arranges axes in 3-dimensional space (still in parallel, forming a Lattice graph), an axis can have more than two neighbors in a circle around the central attribute, and the arrangement problem can be improve by using a minimum spanning tree. A prototype of this visualization is available as extension to the data mining software ELKI. However, the visualization is harder to interpret and interact with than a linear order.

## Software

While there are a large number of papers about parallel coordinates, there are only a few notable software publicly available to convert databases into parallel coordinates graphics. Notable software are ELKI, GGobi, Mondrian, and ROOT. Libraries include Protovis.js, D3.js provides basic examples. D3.Parcoords.js (a D3-based library) specifically dedicated to parallel coordinates graphic creation has also been published. The Python data structure and analysis library Pandas implements parallel coordinates plotting, using the plotting library matplotlib.

## Other visualizations for multivariate data

- Radar chart – A visualization with coordinate axes arranged radially.
- Andrews plot – A Fourier transform of the Parallel Coordinates graph.
- Sankey diagram - A visualization that emphasizes flow/movement/change from one state to another.
