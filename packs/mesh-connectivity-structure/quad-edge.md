---
title: "Quad-edge"
source: https://en.wikipedia.org/wiki/Quad-edge
domain: mesh-connectivity-structure
license: CC-BY-SA-4.0
tags: half-edge mesh, winged edge, quad-edge, doubly connected edge list
fetched: 2026-07-02
---

# Quad-edge

A **quad-edge** data structure is a computer representation of the topology of a two-dimensional or three-dimensional map, that is, a graph drawn on a (closed) surface. It was first described by Jorge Stolfi and Leonidas J. Guibas. It is a variant of the earlier winged edge data structure.

## Overview

The fundamental idea behind the quad-edge structure is the recognition that a single edge, in a closed polygonal mesh topology, sits between exactly two faces and exactly two vertices.

The quad-edge data structure represents an edge, along with the edges it is connected to around the adjacent vertices and faces to encode the topology of the graph. An example implementation of the quad-edge data-type is as follows

```mw
typedef struct {
  quadedge_ref e[4];
} quadedge;

typedef struct {
  quadedge *next;
  unsigned int rot;
} quadedge_ref;
```

Each quad-edge contains four references to adjacent quad-edges. Each of the four references points to the next edge counter-clockwise around either a vertex or a face. Each of these references represent either the origin vertex of the edge, the right face, the destination vertex, or the left face. Each quad-edge reference points to a quad-edge and the rotation (from 0 to 3) of the 'arm' it points at.

Due to this representation, the quad-edge:

- represents a graph, its dual, and its mirror image.
- the dual of the graph can be obtained simply by reversing the convention on what is a vertex and what is a face; and
- can represent the most general form of a map, admitting vertices and faces of degree 1 and 2.

## Details

The quad-edge structure gets its name from the general mechanism by which they are stored. A single Edge structure conceptually stores references to up to two faces, two vertices, and 4 edges. The four edges stored are the edges starting with the two vertices that are attached to the two stored faces.

## Uses

Much like winged edge, quad-edge structures are used in programs to store the topology of a 2D or 3D polygonal mesh. The mesh itself does not need to be closed in order to form a valid quad-edge structure.

Using a quad-edge structure, iterating through the topology is quite easy. Often, the interface to quad-edge topologies is through directed edges. This allows the two vertices to have explicit names (start and end), and this gives faces explicit names as well (left and right, relative to a person standing on start and looking in the direction of end). The four edges are also given names, based on the vertices and faces: start-left, start-right, end-left, and end-right. A directed edge can be reversed to generate the edge in the opposite direction.

Iterating around a particular face only requires having a single directed edge to which that face is on the left (by convention) and then walking through all of the start-left edges until the original edge is reached.
