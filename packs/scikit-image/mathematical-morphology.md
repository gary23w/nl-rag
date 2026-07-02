---
title: "Mathematical morphology"
source: https://en.wikipedia.org/wiki/Mathematical_morphology
domain: scikit-image
license: BSD-3-Clause
tags: scikit-image library, image segmentation, edge detection, mathematical morphology
fetched: 2026-07-02
---

# Mathematical morphology

**Mathematical morphology** (**MM**) is a theory and technique for analyzing and processing geometrical structures. It's based on set theory, lattice theory, topology, and random functions. MM is most commonly applied to digital images, but it can be employed as well on graphs, surface meshes, solids, and many other spatial structures.

Topological and geometrical continuous-space concepts such as size, shape, convexity, connectivity, and geodesic distance, were introduced by MM on both continuous and discrete spaces. MM is also the foundation of morphological image processing, which consists of a set of operators that transform images according to the above characterizations.

The basic morphological operators are erosion, dilation, opening and closing.

MM was originally developed for binary images, and was later extended to grayscale functions and images. The subsequent generalization to complete lattices is widely accepted today as MM's theoretical foundation.

## History

Mathematical Morphology was developed in 1964 by the collaborative work of Georges Matheron and Jean Serra, at the *École des Mines de Paris*, France. Matheron supervised the PhD thesis of Serra, devoted to the quantification of mineral characteristics from thin cross sections, and this work resulted in a novel practical approach, as well as theoretical advancements in integral geometry and topology.

In 1968, the *Centre de Morphologie Mathématique* was founded by the École des Mines de Paris in Fontainebleau, France, led by Matheron and Serra.

During the rest of the 1960s and most of the 1970s, MM dealt essentially with binary images, treated as sets, and generated a large number of binary operators and techniques: Hit-or-miss transform, dilation, erosion, opening, closing, granulometry, thinning, skeletonization, ultimate erosion, conditional bisector, and others. A random approach was also developed, based on novel image models. Most of the work in that period was developed in Fontainebleau.

From the mid-1970s to mid-1980s, MM was generalized to grayscale functions and images as well. Besides extending the main concepts (such as dilation, erosion, etc.) to functions, this generalization yielded new operators, such as morphological gradients, top-hat transform and the Watershed (MM's main segmentation approach).

In the 1980s and 1990s, MM gained a wider recognition, as research centers in several countries began to adopt and investigate the method. MM started to be applied to a large number of imaging problems and applications, especially in the field of non-linear filtering of noisy images.

In 1986, Serra further generalized MM, this time to a theoretical framework based on complete lattices. This generalization brought flexibility to the theory, enabling its application to a much larger number of structures, including color images, video, graphs, meshes, etc. At the same time, Matheron and Serra also formulated a theory for morphological filtering, based on the new lattice framework.

The 1990s and 2000s also saw further theoretical advancements, including the concepts of *connections* and *levelings*.

In 1993, the first International Symposium on Mathematical Morphology (ISMM) took place in Barcelona, Spain. Since then, ISMMs are organized every 2–3 years: Fontainebleau, France (1994); Atlanta, USA (1996); Amsterdam, Netherlands (1998); Palo Alto, CA, USA (2000); Sydney, Australia (2002); Paris, France (2005); Rio de Janeiro, Brazil (2007); Groningen, Netherlands (2009); Intra (Verbania), Italy (2011); Uppsala, Sweden (2013); Reykjavík, Iceland (2015); Fontainebleau, France (2017); and Saarbrücken, Germany (2019).
