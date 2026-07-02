---
title: "Octree"
source: https://en.wikipedia.org/wiki/Octree
domain: sparse-voxel-octree
license: CC-BY-SA-4.0
tags: sparse voxel octree, svo raytracing, voxel octree traversal, hierarchical voxel structure
fetched: 2026-07-02
---

# Octree

An **octree** is a tree data structure in which each internal node has exactly eight children. Octrees are most often used to partition a three-dimensional space by recursively subdividing it into eight octants. Octrees are the three-dimensional analog of quadtrees. The word is derived from *oct* (Greek root meaning "eight") + *tree*. Octrees are often used in 3D graphics and 3D game engines.

## For spatial representation

Each node in an octree subdivides the space it represents into eight octants. In a point region (PR) octree (analogous to a point quadtree), the node stores an explicit three-dimensional point, which is the "center" of the subdivision for that node; the point defines one of the corners for each of the eight children. In a matrix-based (MX) octree (analogous to a region quadtree), the subdivision point is implicitly the center of the space the node represents. The root node of a PR octree can represent infinite space; the root node of an MX octree must represent a finite bounded space so that the implicit centers are well-defined. Note that octrees are not the same as *k*-d trees: *k*-d trees split along a dimension and octrees split around a point. Also *k*-d trees are always binary, which is not the case for octrees. By using a depth-first search the nodes are to be traversed and only required surfaces are to be viewed.

## History

A spatial subdivision much like an octree was used in 1934, in the Whitney covering lemma in mathematics. The use of octrees for 3D computer graphics was pioneered by Donald Meagher at Rensselaer Polytechnic Institute, described in a 1980 report "Octree Encoding: A New Technique for the Representation, Manipulation and Display of Arbitrary 3-D Objects by Computer", for which he holds a 1995 patent (with a 1984 priority date) "High-speed image generation of complex solid objects using octree encoding"

## Common uses

- Level of detail rendering in 3D computer graphics
- Spatial indexing
- Nearest neighbor search
- Efficient collision detection in three dimensions
- View frustum culling
- Fast multipole method
- Unstructured grid
- Finite element analysis
- Sparse voxel octree
- State estimation
- Set estimation

## Application to color quantization

The octree color quantization algorithm, invented by Gervautz and Purgathofer in 1988, encodes image color data as an octree up to nine levels deep. Octrees are used because $2^{3}=8$ and there are three color components in the RGB system. The node index to branch out from at the top level is determined by a formula that uses the most significant bits of the red, green, and blue color components, e.g. 4r + 2g + b. The next lower level uses the next bit significance, and so on. Less significant bits are sometimes ignored to reduce the tree size.

The algorithm is highly memory efficient because the tree's size can be limited. The bottom level of the octree consists of leaf nodes that accrue color data not represented in the tree; these nodes initially contain single bits. If much more than the desired number of palette colors are entered into the octree, its size can be continually reduced by seeking out a bottom-level node and averaging its bit data up into a leaf node, pruning part of the tree. Once sampling is complete, exploring all routes in the tree down to the leaf nodes, taking note of the bits along the way, will yield approximately the required number of colors.

## Implementation for point decomposition

The example recursive algorithm outline below (MATLAB syntax) decomposes an array of 3-dimensional points into octree style bins. The implementation begins with a single bin surrounding all given points, which then recursively subdivides into its 8 octree regions. Recursion is stopped when a given exit condition is met. Examples of such exit conditions (shown in code below) are:

- When a bin contains fewer than a given number of points
- When a bin reaches a minimum size or volume based on the length of its edges
- When recursion has reached a maximum number of subdivisions

```mw
function [binDepths, binParents, binCorners, pointBins] = OcTree(points)

binDepths = [0]     % Initialize an array of bin depths with this single base-level bin
binParents = [0]    % This base level bin is not a child of other bins
binCorners = [min(points) max(points)] % It surrounds all points in XYZ space
pointBins(:) = 1    % Initially, all points are assigned to this first bin
divide(1)           % Begin dividing this first bin

function divide(binNo)

% If this bin meets any exit conditions, do not divide it any further.
binPointCount = nnz(pointBins == binNo)
binEdgeLengths = binCorners(binNo, 1:3) - binCorners(binNo, 4:6)
binDepth = binDepths(binNo)
exitConditionsMet = binPointCount<value || min(binEdgeLengths) < value || binDepth > value
if exitConditionsMet
    return; % Exit recursive function
end

% Otherwise, split this bin into 8 new sub-bins with a new division point
newDiv = (binCorners(binNo, 1:3) + binCorners(binNo, 4:6)) / 2
for i = 1:8
    newBinNo = length(binDepths) + 1
    binDepths(newBinNo) = binDepths(binNo) + 1
    binParents(newBinNo) = binNo
    binCorners(newBinNo) = [one of the 8 pairs of the newDiv with minCorner or maxCorner]
    oldBinMask = pointBins == binNo
    % Calculate which points in pointBins == binNo now belong in newBinNo
    pointBins(newBinMask) = newBinNo
    % Recursively divide this newly created bin
    divide(newBinNo)
end
```

## Example color quantization

Taking the full list of colors of a 24-bit RGB image as point input to the Octree point decomposition implementation outlined above, the following example show the results of octree color quantization. The first image is the original (532818 distinct colors), while the second is the quantized image (184 distinct colors) using octree decomposition, with each pixel assigned the color at the center of the octree bin in which it falls. Alternatively, final colors could be chosen at the centroid of all colors in each octree bin, however this added computation has very little effect on the visual result.

```mw
% Read the original RGB image
Img = imread('IMG_9980.CR2');
% Extract pixels as RGB point triplets
pts = reshape(Img, [], 3);
% Create OcTree decomposition object using a target bin capacity
OT = OcTree(pts, 'BinCapacity', ceil((size(pts, 1) / 256) * 7));
% Find which bins are "leaf nodes" on the octree object
leafs = find(~ismember(1:OT.BinCount, OT.BinParents) & ...
    ismember(1:OT.BinCount, OT.PointBins));
% Find the central RGB location of each leaf bin
binCents = mean(reshape(OT.BinBoundaries(leafs,:), [], 3, 2), 3);
 
% Make a new "indexed" image with a color map
ImgIdx = zeros(size(Img, 1), size(Img, 2));
for i = 1:length(leafs)
    pxNos = find(OT.PointBins==leafs(i));
    ImgIdx(pxNos) = i;
end
ImgMap = binCents / 255; % Convert 8-bit color to MATLAB rgb values
 
% Display the original 532818-color image and resulting 184-color image 
figure
subplot(1, 2, 1), imshow(Img)
title(sprintf('Original %d color image', size(unique(pts,'rows'), 1)))
subplot(1, 2, 2), imshow(ImgIdx, ImgMap)
title(sprintf('Octree-quantized %d color image', size(ImgMap, 1)))
```
