---
title: "Best bin first"
source: https://en.wikipedia.org/wiki/Best_bin_first
domain: nearest-neighbor-search-nns
license: CC-BY-SA-4.0
tags: nearest neighbor search, best bin first, space partitioning, vantage point tree
fetched: 2026-07-02
---

# Best bin first

**Best bin first** is a search algorithm that is designed to efficiently find an approximate solution to the nearest neighbor search problem in very-high-dimensional spaces. The algorithm is based on a variant of the kd-tree search algorithm which makes indexing higher-dimensional spaces possible. Best bin first is an approximate algorithm which returns the nearest neighbor for a large fraction of queries and a very close neighbor otherwise.

## Differences from kd tree

- Bins are looked in increasing order of distance from the query point. The distance to a bin is defined as a minimal distance to any point of its boundary. This is implemented with priority queue.
- Search a fixed number of nearest candidates and stop.
- A speedup of two orders of magnitude is typical.
