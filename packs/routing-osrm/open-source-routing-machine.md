---
title: "Open Source Routing Machine"
source: https://en.wikipedia.org/wiki/Open_Source_Routing_Machine
domain: routing-osrm
license: CC-BY-SA-4.0
tags: osrm routing, route planning, shortest path routing, contraction hierarchies
fetched: 2026-07-02
---

# Open Source Routing Machine

The **Open Source Routing Machine** (abbreviated **OSRM**) is an open-source route planning library and network service. Written in high-performance C++, OSRM runs on the Linux, FreeBSD, Windows, and macOS platforms. It is designed for compatibility with OpenStreetMap's road network data. FOSSGIS operates a free-to-use server that powers walking, cycling, and driving directions on OSM's homepage.

## History

OSRM powered Mapbox's navigation offerings during the 2010s. OSRM participated in the 2011 Google Summer of Code. In February 2015, OSRM was integrated into OpenStreetMap's homepage alongside two other routing engines, GraphHopper and Valhalla. In 2025, a team at Roskilde University and the University of Waterloo used OSRM to solve the travelling salesman problem for a dataset of 81,998 bars from South Korea's National Police Agency, breaking a record set in 2021.

## Architecture

OSRM implements multilevel Dijkstra's algorithm (MLD) as well as another routing algorithm, contraction hierarchies (CH), which is better suited for very large distance matrices. Shortest path computation on a continental sized network can take up to several seconds if it is done without a so-called speedup-technique. Via the CH preprocessing pipeline, OSRM can compute and output a shortest path between any origin and destination within a few milliseconds, whereby the pure route computation takes much less time. Most effort is spent in annotating the route and transmitting the geometry over the network. This high performance facilitates use cases such as user-interactive route manipulation.

In addition to solving the shortest path problem for road networks, OSRM also includes a map matching service and a travelling salesman problem solver for generating distance matrices.
