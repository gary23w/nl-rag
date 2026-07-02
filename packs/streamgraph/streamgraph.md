---
title: "Streamgraph"
source: https://en.wikipedia.org/wiki/Streamgraph
domain: streamgraph
license: CC-BY-SA-4.0
tags: streamgraph, stacked area, theme river, flowing bands
fetched: 2026-07-02
---

# Streamgraph

A **streamgraph**, or **stream graph**, is a type of stacked area graph which is displaced around a central axis, resulting in a flowing, organic shape. Unlike a traditional stacked area graph in which the layers are stacked on top of an axis, in a streamgraph the layers are positioned to minimize their "wiggle". More formally, the layers are displaced to minimize the sum of the squared slopes of each layer, weighted by the area of the layer. Streamgraphs display data with only positive values, and are not able to represent both negative and positive values.

Streamgraphs and their use were popularized by Amanda Cox in a February 2008 *New York Times* article on movie box office revenues. Cox got the idea from then-undergraduate Lee Byron, who had used a similar method for visualizing his music listening history.

A related graph, sometimes conflated with streamgraphs, is the ThemeRiver, in which the "silhouette" of the graph is symmetrically arranged around the central axis.

Streamgraphs were found to be more readable than basic stacked area graphs or ThemeRivers for value comparison tasks.

Streamgraphs are officially supported by Matplotlib and D3.js.

Marco Di Bartolomeo and Yifan Hu (2016) propose several improvements to streamgraphs, such as using 1-norm minimization instead of 2-norm minimization.
