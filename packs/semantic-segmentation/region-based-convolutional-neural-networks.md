---
title: "Region Based Convolutional Neural Networks"
source: https://en.wikipedia.org/wiki/Region_Based_Convolutional_Neural_Networks
domain: semantic-segmentation
license: CC-BY-SA-4.0
tags: semantic segmentation, pixel labeling, scene parsing, dense prediction, image mask
fetched: 2026-07-02
---

# Region Based Convolutional Neural Networks

**Region-based Convolutional Neural Networks (R-CNN)** are a family of machine learning models for computer vision, and specifically object detection and localization. The original goal of R-CNN was to take an input image and produce a set of bounding boxes as output, where each bounding box contains an object and also the category (e.g. car or pedestrian) of the object. In general, R-CNN architectures perform selective search over feature maps outputted by a CNN.

R-CNN has been extended to perform other computer vision tasks, such as: tracking objects from a drone-mounted camera, locating text in an image, and enabling object detection in Google Lens.

Mask R-CNN is also one of seven tasks in the MLPerf Training Benchmark, which is a competition to speed up the training of neural networks.

## History

The following covers some of the versions of R-CNN that have been developed.

- November 2013: **R-CNN**.
- April 2015: **Fast R-CNN**.
- June 2015: **Faster R-CNN**.
- March 2017: **Mask R-CNN**.
- December 2017: **Cascade R-CNN** is trained with increasing Intersection over Union (IoU, also known as the Jaccard index) thresholds, making each stage more selective against nearby false positives.
- June 2019: **Mesh R-CNN** adds the ability to generate a 3D mesh from a 2D image.

## Architecture

For review articles see.

Given an image (or an image-like feature map), **selective search** (also called Hierarchical Grouping) first segments the image by the algorithm in (Felzenszwalb and Huttenlocher, 2004), then performs the following:

```
   Input: (colour) image 
   Output: Set of object location hypotheses L
    
   Segment image into initial regions R = {r1, ..., rn} using Felzenszwalb and Huttenlocher (2004)
   Initialise similarity set S = ∅
   foreach Neighbouring region pair (ri, rj) do
      Calculate similarity s(ri, rj)
      S = S ∪ s(ri, rj)
   while S ≠ ∅ do
      Get highest similarity s(ri, rj) = max(S)
      Merge corresponding regions rt = ri ∪ rj
      Remove similarities regarding ri: S = S \ s(ri, r∗)
      Remove similarities regarding rj: S = S \ s(r∗, rj)
      Calculate similarity set St between rt and its neighbours
      S = S ∪ St
      R = R ∪ rt
   Extract object location boxes L from all regions in R
```

### R-CNN

With R-CNN, prediction follows a two-step process. A preprocessing **selective search** step generates a large set of candidate objects (typically as many as 2000), known as regions of interest (ROI). These are forwarded to a CNN, which predicts an object class score and bounding box estimate, independently for each ROI.

Importantly, the ROIs are heavily filtered to remove excess candidates. This is achieved using two mechanisms. Filtering begins by removing ROIs assigned to the **background** category. This is a specialized category, which is scored by the CNN alongside other categories.

An unfortunate reality is that remaining ROIs typically suffer from heavy duplication. Namely, multiple ROIs that cover same objects in the image are all assigned non-background categories. This is resolved by a heuristic non-maximum suppression (**NMS**) step.

### Fast R-CNN

While the original R-CNN independently computed the neural network features on each of as many as two thousand regions of interest, Fast R-CNN runs the neural network once on the whole image.

At the end of the network is a **ROIPooling** module, which slices out each ROI from the network's output tensor, reshapes it, and classifies it. As in the original R-CNN, the Fast R-CNN uses selective search to generate its region proposals.

### Faster R-CNN

While Fast R-CNN used selective search to generate ROIs, Faster R-CNN integrates the ROI generation into the neural network itself.

### Mask R-CNN

While previous versions of R-CNN focused on object detections, Mask R-CNN adds instance segmentation. Mask R-CNN also replaced ROIPooling with a new method called ROIAlign, which can represent fractions of a pixel.
