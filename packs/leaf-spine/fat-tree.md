---
title: "Fat tree"
source: https://en.wikipedia.org/wiki/Fat_tree
domain: leaf-spine
license: CC-BY-SA-4.0
tags: leaf spine architecture, data center topology, two-tier fabric, network scaling
fetched: 2026-07-02
---

# Fat tree

The **fat tree network** is a universal network for provably efficient communication. It was invented by Charles E. Leiserson of the MIT in 1985. k-ary n-trees, the type of fat-trees commonly used in most high-performance networks, were initially formalized in 1997.

In a tree data structure, every branch has the same thickness (bandwidth), regardless of their place in the hierarchy—they are all "skinny" (*skinny* in this context means low-bandwidth). In a fat tree, branches nearer the top of the hierarchy are "fatter" (thicker) than branches further down the hierarchy. In a telecommunications network, the branches are data links; the varied thickness (bandwidth) of the data links allows for more efficient and technology-specific use.

Mesh and hypercube topologies have communication requirements that follow a rigid algorithm, and cannot be tailored to specific packaging technologies.

## Applications in supercomputers

Supercomputers that use a fat tree network include the two fastest as of late 2018, Summit and Sierra, as well as Tianhe-2, the Meiko Scientific CS-2, Yellowstone, the Earth Simulator, the Cray X2, the Connection Machine CM-5, and various Altix supercomputers.

Mercury Computer Systems applied a variant of the fat tree topology—the hypertree network—to their multicomputers. In this architecture, 2 to 360 compute nodes are arranged in a circuit-switched fat tree network. Each node has local memory that can be mapped by any other node. Each node in this heterogeneous system could be an Intel i860, a PowerPC, or a group of three SHARC digital signal processors.

The fat tree network was particularly well suited to fast Fourier transform computations, which customers used for such signal processing tasks as radar, sonar, and medical imaging.

In August 2008, a team of computer scientists at UCSD published a scalable design for network architecture that uses a topology inspired by the fat tree topology to realize networks that scale better than those of previous hierarchical networks. The architecture uses commodity switches that are cheaper and more power-efficient than high-end modular data center switches.

This topology is actually a special instance of a Clos network, rather than a fat-tree as described above. That is because the edges near the root are emulated by many links to separate parents instead of a single high-capacity link to a single parent. However, many authors continue to use the term in this way.
