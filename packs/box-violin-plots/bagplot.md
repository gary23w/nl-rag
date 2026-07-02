---
title: "Bagplot"
source: https://en.wikipedia.org/wiki/Bagplot
domain: box-violin-plots
license: CC-BY-SA-4.0
tags: box plot, violin plot, bagplot, strip plot
fetched: 2026-07-02
---

# Bagplot

A **bagplot**, or **starburst plot**, is a method in robust statistics for visualizing two- or three-dimensional statistical data, analogous to the one-dimensional box plot. Introduced in 1999 by Rousseuw et al., the bagplot allows one to visualize the location, spread, skewness, and outliers of a data set.

## Construction

The bagplot consists of three nested polygons, called the "bag", the "fence", and the "loop".

- The inner polygon, called the *bag*, is constructed on the basis of Tukey depth, the smallest number of observations that can be contained by a half-plane that also contains a given point. It contains at most 50% of the data points.
- The outermost of the three polygons, called the *fence* is not drawn as part of the bagplot, but is used to construct it. It is formed by inflating the bag by a certain factor (usually 3). Observations outside the fence are flagged as outliers.
- The observations that are not marked as outliers are surrounded by a *loop*, the convex hull of the observations within the fence.

An asterisk symbol (*) near the center of the graph is used to mark the depth median, the point with the highest possible Tukey depth. The observations between the bag and fence are marked by line segments, on a line to the depth median, connecting them to the bag. The three-dimensional version consists of an inner and outer bag. The outer bag must be drawn in transparent colors so that the inner bag remains visible.

## Properties

The bagplot is invariant under affine transformations of the plane, and robust against outliers.
