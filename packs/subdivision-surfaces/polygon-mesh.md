---
title: "Polygon mesh"
source: https://en.wikipedia.org/wiki/Polygon_mesh
domain: subdivision-surfaces
license: CC-BY-SA-4.0
tags: subdivision surface, catmull clark subdivision, loop subdivision surface, doo sabin subdivision
fetched: 2026-07-02
---

# Polygon mesh

In 3D computer graphics and solid modeling, a **polygon mesh** is a collection of **vertices**, **edges** and **faces** that define the shape of a polyhedral object's surface. It simplifies rendering, as in a wire-frame model. The faces usually consist of triangles (triangle mesh), quadrilaterals (quads), or other simple convex polygons (n-gons). A polygonal mesh may also be more generally composed of concave polygons, or even polygons with holes.

The study of polygon meshes is a large sub-field of computer graphics (specifically 3D computer graphics) and geometric modeling. Different representations of polygon meshes are used for different applications and goals. The variety of operations performed on meshes includes Boolean logic (Constructive solid geometry), smoothing, and simplification. Algorithms also exist for ray tracing, collision detection, and rigid-body dynamics with polygon meshes. If the mesh's edges are rendered instead of the faces, then the model becomes a wireframe model.

Several methods exist for mesh generation, including the marching cubes algorithm.

Volumetric meshes are distinct from polygon meshes in that they explicitly represent both the surface and interior region of a structure, while polygon meshes only explicitly represent the surface (the volume is implicit).

## Elements

(Elements of polygonal mesh modeling.)

Objects created with polygon meshes must store different types of elements. These include vertices, edges, faces, polygons and surfaces. In many applications, only vertices, edges and either faces or polygons are stored. A renderer may support only 3-sided faces, so polygons must be constructed of many of these, as shown above. However, many renderers either support quads and higher-sided polygons, or are able to convert polygons to triangles on the fly, making it unnecessary to store a mesh in a triangulated form.

### Vertices

A vertex in computer graphics terms is a data structure that describes the position of a point in 2, 3 or 4D space on a surface along with optional attributes - other values used to render the object correctly. Most attributes of a vertex represent vectors in the space to be rendered. These vectors are typically 2 (*x, y*) or 3 (*x, y, z*) dimensional and can include a fourth homogeneous coordinate (*w*).. In real-time rendering these properties are used by a vertex shader or vertex pipeline.

Attributes can include position, color, reflectance, specularity, texture mapping coordinates, normal vectors, and displacement mapping.

## Representations

Polygon meshes may be represented in a variety of ways, using different methods to store the vertex, edge and face data. These include:

- vertex-vertex
- face-vertex
- winged-edge
- half-edge
- quad-edge

Each representation has advantages and disadvantages, discussed in Smith (2006).

### Vertex-vertex meshes

Vertex-vertex meshes represent an object as a set of vertices connected to other vertices. This is the simplest representation, but not widely used since the face and edge information is implicit. Thus, it is necessary to traverse the data in order to generate a list of faces for rendering. In addition, operations on edges and faces are not easily accomplished.

However, VV meshes benefit from small storage space and efficient morphing of shape. The above figure shows a four-sided box as represented by a VV mesh. Each vertex indexes its neighboring vertices. The last two vertices, 8 and 9 at the top and bottom center of the "box-cylinder", have four connected vertices rather than five. A general system must be able to handle an arbitrary number of vertices connected to any given vertex.

For a complete description of VV meshes see Smith (2006).

### Face-vertex meshes

Face-vertex meshes represent an object as a set of faces and a set of vertices. This is the most widely used mesh representation, being the input typically accepted by modern graphics hardware.

Face-vertex meshes improve on VV mesh for modelling in that they allow explicit lookup of the vertices of a face, and the faces surrounding a vertex. The above figure shows the "box-cylinder" example as an FV mesh. Vertex v5 is highlighted to show the faces that surround it. Notice that, in this example, every face is required to have exactly 3 vertices. However, this does not mean every vertex has the same number of surrounding faces.

For rendering, the face list is usually transmitted to the GPU as a set of indices to vertices, and the vertices are sent as position/color/normal structures (in the figure, only position is given). This has the benefit that changes in shape, but not geometry, can be dynamically updated by simply resending the vertex data without updating the face connectivity.

Modelling requires easy traversal of all structures. With face-vertex meshes it is easy to find the vertices of a face. Also, the vertex list contains a list of faces connected to each vertex. Unlike VV meshes, both faces and vertices are explicit, so locating neighboring faces and vertices is constant time. However, the edges are implicit, so a search is still needed to find all the faces surrounding a given face. Other dynamic operations, such as splitting or merging a face, are also difficult with face-vertex meshes.

### Winged-edge meshes

Introduced by Baumgart in 1975, winged-edge meshes explicitly represent the vertices, faces, and edges of a mesh. This representation is widely used in modelling programs to provide the greatest flexibility in dynamically changing the mesh geometry, because split and merge operations can be done quickly. Their primary drawback is large storage requirements and increased complexity due to maintaining many indices. A good discussion of implementation issues of Winged-edge meshes may be found in the book *Graphics Gems II*.

Winged-edge meshes address the issue of traversing from edge to edge, and providing an ordered set of faces around an edge. For any given edge, the number of outgoing edges may be arbitrary. To simplify this, winged-edge meshes provide only four, the nearest clockwise and counter-clockwise edges at each end. The other edges may be traversed incrementally. The information for each edge therefore resembles a butterfly, hence "winged-edge" meshes. The above figure shows the "box-cylinder" as a winged-edge mesh. The total data for an edge consists of 2 vertices (endpoints), 2 faces (on each side), and 4 edges (winged-edge).

Rendering of winged-edge meshes for graphics hardware requires generating a face index list, which is usually done only when the geometry changes. Winged-edge meshes are ideally suited for dynamic geometry, such as subdivision surfaces and interactive modelling, since changes to the mesh can occur locally. Traversal across the mesh, as might be needed for collision detection, can be accomplished efficiently.

### Render dynamic meshes

Winged-edge meshes are not the only representation which allows for dynamic changes to geometry. A representation which combines winged-edge meshes and face-vertex meshes is the render dynamic mesh (RDM), which explicitly stores both, the vertices of a face and faces of a vertex (like FV meshes), and the faces and vertices of an edge (like winged-edge).

RDM's require less storage space than standard winged-edge meshes, and can be directly rendered by graphics hardware since the face list contains an index of vertices. In addition, traversal from vertex to face is explicit (constant time), as is from face to vertex. RDM's do not require the four outgoing edges since these can be found by traversing from edge to face, then face to neighboring edge. RDM's benefit from the features of winged-edge meshes by allowing for geometry to be dynamically updated.

See Tobler & Maierhofer (WSCG 2006) for more details.

### Efficiency

In the following table, *explicit* indicates that the operation can be performed in constant time, as the data is directly stored; *list compare* indicates that a list comparison between two lists must be performed to accomplish the operation; and *pair search* indicates a search must be done on two indices. The notation *avg(V,V)* means the average number of vertices connected to a given vertex; *avg(E,V)* means the average number of edges connected to a given vertex, and *avg(F,V)* is the average number of faces connected to a given vertex.

The notation "V → f1, f2, f3, ... → v1, v2, v3, ..." describes that a traversal across multiple elements is required to perform the operation. For example, to get "all vertices around a given vertex V" using the face-vertex mesh, it is necessary to first find the faces around the given vertex V using the vertex list. Then, from those faces, use the face list to find the vertices around them. Winged-edge meshes explicitly store nearly all information, and other operations always traverse to the edge first to get additional info. Vertex-vertex meshes are the only representation that explicitly stores the neighboring vertices of a given vertex.

As the mesh representations become more complex (from left to right in the summary), the amount of information explicitly stored increases. This gives more direct, constant time, access to traversal and topology of various elements but at the cost of increased overhead and space in maintaining indices properly.

As a general rule, face-vertex meshes are used whenever an object must be rendered on graphics hardware that does not change geometry (connectivity), but may deform or morph shape (vertex positions) such as real-time rendering of static or morphing objects. Winged-edge or render dynamic meshes are used when the geometry changes, such as in interactive modeling packages or for computing subdivision surfaces. Vertex-vertex meshes are ideal for efficient, complex changes in geometry or topology so long as hardware rendering is not of concern.

| Operation | Vertex-vertex | Face-vertex | Winged-edge | Render dynamic |   |
|---|---|---|---|---|---|
| V-V | All vertices around vertex | Explicit | V → f1, f2, f3, ... → v1, v2, v3, ... | V → e1, e2, e3, ... → v1, v2, v3, ... | V → e1, e2, e3, ... → v1, v2, v3, ... |
| E-F | All edges of a face | F(a,b,c) → {a,b}, {b,c}, {a,c} | F → {a,b}, {b,c}, {a,c} | Explicit | Explicit |
| V-F | All vertices of a face | F(a,b,c) → {a,b,c} | Explicit | F → e1, e2, e3 → a, b, c | Explicit |
| F-V | All faces around a vertex | Pair search | Explicit | V → e1, e2, e3 → f1, f2, f3, ... | Explicit |
| E-V | All edges around a vertex | V → {v,v1}, {v,v2}, {v,v3}, ... | V → f1, f2, f3, ... → v1, v2, v3, ... | Explicit | Explicit |
| F-E | Both faces of an edge | List compare | List compare | Explicit | Explicit |
| V-E | Both vertices of an edge | E(a,b) → {a,b} | E(a,b) → {a,b} | Explicit | Explicit |
| Flook | Find face with given vertices | (a,b,c) → F{a,b,c} | Set intersection of v1,v2,v3 | Set intersection of v1,v2,v3 | Set intersection of v1,v2,v3 |
| Storage size | V*avg(V,V) | 3F + V*avg(F,V) | 3F + 8E + V*avg(E,V) | 6F + 4E + V*avg(E,V) |   |
| Example with 10 vertices, 16 faces, 24 edges: |   |   |   |   |   |
| 10 * 5 = 50 | 3*16 + 10*5 = 98 | 3*16 + 8*24 + 10*5 = 290 | 6*16 + 4*24 + 10*5 = 242 |   |   |

## Other representations

Streaming meshes store faces in an ordered, yet independent, way so that the mesh can be transmitted in pieces. The order of faces may be spatial, spectral, or based on other properties of the mesh. Streaming meshes allow a very large mesh to be rendered even while it is still being loaded.

Progressive meshes transmit the vertex and face data with increasing levels of detail. Unlike *streaming meshes*, progressive meshes give the overall shape of the entire object, but at a low level of detail. Additional data, new edges and faces, progressively increase the detail of the mesh.

Normal meshes transmit progressive changes to a mesh as a set of normal displacements from a base mesh. With this technique, a series of textures represent the desired incremental modifications. Normal meshes are compact, since only a single scalar value is needed to express displacement. However, the technique requires a complex series of transformations to create the displacement textures.

## File formats

There exist many different file formats for storing polygon mesh data. Each format is most effective when used for the purpose intended by its creator. Popular formats include .fbx, .dae, .obj, and .stl. A table of some more of these formats is presented below:

| File suffix | Format name | Organization(s) | Program(s) | Description |
|---|---|---|---|---|
| .raw | Raw mesh | Unknown | Various | Open, ASCII-only format. Each line contains three vertices, separated by spaces, to form a triangle, like so: X1 Y1 Z1 X2 Y2 Z2 X3 Y3 Z3 |
| .blend | Blender File Format | Blender Foundation | Blender 3D | Open source, binary-only format |
| .fbx | Autodesk FBX Format | Autodesk | Various | Proprietary. Binary and ASCII specifications exist. |
| .3ds | 3ds Max File | Autodesk | 3ds Max | A common but outdated format with hard 16-bit limits on the number of vertices and faces. Neither standardised nor well documented, but used to be a "de facto standard" for data exchange. |
| .dae | Digital Asset Exchange (COLLADA) | Sony Computer Entertainment, Khronos Group | N/A | Stands for "**COLLA**borative **D**esign **A**ctivity". A universal format designed to prevent incompatibility. |
| .dgn | MicroStation File | Bentley Systems | MicroStation | There are two dgn file formats: pre-version 8 and version 8 (V8) |
| .3dm | Rhino File | Robert McNeel & Associates | Rhinoceros 3D |   |
| .dxf, .dwg | Drawing Exchange Format | Autodesk | AutoCAD |   |
| .obj | Wavefront OBJ | Wavefront Technologies | Various | ASCII format describing 3D geometry. All faces' vertices are ordered counter-clockwise, making facet normals implicit. Smooth normals are specified per vertex. |
| .ply | Polygon File Format | Stanford University | Various | Binary and ASCII |
| .pmd | Polygon Movie Maker data | Yu Higuchi | MikuMikuDance | Proprietary binary file format for storing humanoid model geometry with rigging, material, and physics information. |
| .stl | Stereolithography Format | 3D Systems | Many | Binary and ASCII format originally designed to aid in CNC. |
| .amf | Additive Manufacturing File Format | ASTM International | N/A | Like the STL format, but with added native color, material, and constellation support. |
| .wrl | Virtual Reality Modeling Language | Web3D Consortium | Web Browsers | ISO Standard 14772-1:1997 |
| .wrz | VRML Compressed | Web3D Consortium | Web Browsers |   |
| .x3d, .x3db, .x3dv | Extensible 3D | Web3D Consortium | Web Browsers | XML-based, open source, royalty-free, extensible, and interoperable; also supports color, texture, and scene information. ISO Standard 19775/19776/19777 |
| .x3dz, .x3dbz, .x3dvz | X3D Compressed Binary | Web3D Consortium | Web Browsers |   |
| .c4d | Cinema 4D File | Maxon | CINEMA 4D |   |
| .lwo | LightWave 3D object File | NewTek | LightWave 3D |   |
| .smb | SCOREC apf | RPI SCOREC | PUMI | Open source parallel adaptive unstructured 3D meshes for PDE based simulation workflows. |
| .msh | Gmsh Mesh | GMsh Developers | GMsh Project | Open source, providing an ASCII mesh description for linear and polynomially interpolated elements in one to three dimensions. |
| .mesh | OGRE XML | OGRE Development Team | OGRE, purebasic | Open Source. Binary (.mesh) and ASCII (.mesh.xml) format available. Includes data for vertex animation and Morph target animation (blendshape). Skeletal animation data in separate file (.skeleton). |
| .veg | Vega FEM tetrahedral mesh | Jernej Barbič | Vega FEM | Open Source. Stores a tetrahedral mesh and its material properties for FEM simulation. ASCII (.veg) and binary (.vegb) formats available. |
| .z3d | Z3d | Oleg Melashenko | Zanoza Modeler | - |
| .vtk | VTK mesh | VTK, Kitware | VTK, Paraview | Open, ASCII or binary format that contains many different data fields, including point data, cell data, and field data. |
| .l4d | LAI4D drawing | Laboratory of Artificial Intelligence for Design | LAI4D | ASCII data format that describes a hierarchical tree of entities. |
