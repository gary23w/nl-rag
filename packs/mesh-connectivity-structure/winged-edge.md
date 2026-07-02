---
title: "Winged edge"
source: https://en.wikipedia.org/wiki/Winged_edge
domain: mesh-connectivity-structure
license: CC-BY-SA-4.0
tags: half-edge mesh, winged edge, quad-edge, doubly connected edge list
fetched: 2026-07-02
---

# Winged edge

In computer graphics, the **winged edge** data structure is a way to represent polygon meshes in computer memory. It is a type of boundary representation and describes both the geometry and topology of a model. Three types of records are used: vertex records, edge records, and face records. Given a reference to an edge record, one can answer several types of adjacency queries (queries about neighboring edges, vertices and faces) in constant time. This kind of adjacency information is useful for algorithms such as subdivision surface.

## Features

The **winged edge** data structure explicitly describes the geometry and topology of faces, edges, and vertices when three or more surfaces come together and meet at a common edge. The ordering is such that the surfaces are ordered counter-clockwise with respect to the innate orientation of the intersection edge. Moreover the representation allows numerically unstable situations like that depicted below.

The winged edge data structure allows for quick traversal between faces, edges, and vertices due to the explicitly linked structure of the network. It serves adjacency queries in constant time with little storage overhead. This rich form of specifying an unstructured grid is in contrast to simpler specifications of polygon meshes such as a node and element list, or the implied connectivity of a regular grid. An alternative to the winged edge data structure is the Half-edge data structure.

## Structure and pseudocode

The face and vertex records are relatively simple, while the edge record is more complex.

- For each vertex, its record stores only the vertex's position (e.g. coordinates) and a reference to one incident edge. The other edges can be found by following further references in the edge.
- Similarly each face record only stores a reference to one of the edges surrounding the face. There is no need to store the direction of the edge relative to the face (CCW or CW) as the face can be trivially compared to the edge's own left and right faces to obtain this information.
- Finally, the structure of the edge record is as follows. An edge is assumed to be directed. The edge record contains two references to the vertices that make up the endpoints of the edge, two references to the faces on either side of the edge, and four references to the previous and next edges surrounding the left and right face.

In short, the edge record has references to all its adjacent records, both when traversing around an adjacent vertex or around an adjacent face.

```
class Edge
{
    Vertex *vert_origin, *vert_destination;
    Face *face_left, *face_right;
    Edge *edge_left_cw,
         *edge_left_ccw,
         *edge_right_cw,
         *edge_right_ccw;
}

class Vertex
{
    float x, y, z;
    Edge *edge;
}

class Face
{
    Edge *edge;
}
```
