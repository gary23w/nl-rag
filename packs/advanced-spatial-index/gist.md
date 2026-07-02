---
title: "GiST"
source: https://en.wikipedia.org/wiki/GiST
domain: advanced-spatial-index
license: CC-BY-SA-4.0
tags: ub-tree, x-tree structure, bx-tree, space-filling curve, point access method
fetched: 2026-07-02
---

# GiST

In computing, **GiST** or Generalized Search Tree, is a data structure and API that can be used to build a variety of disk-based search trees. GiST is a generalization of the B+ tree, providing a concurrent and recoverable height-balanced search tree infrastructure without making any assumptions about the type of data being stored, or the queries being serviced. GiST can be used to easily implement a range of well-known indexes, including B+ trees, R-trees, hB-trees, RD-trees, and many others; it also allows for easy development of specialized indexes for new data types. It cannot be used directly to implement non-height-balanced trees such as quad trees or prefix trees (tries), though like prefix trees it does support compression, including lossy compression. GiST can be used for any data type that can be naturally ordered into a hierarchy of supersets. Not only is it extensible in terms of data type support and tree layout, it allows the extension writer to support any query predicates that they choose.

GiST is an example of software extensibility in the context of database systems: it allows the easy evolution of a database system to support new tree-based indexes. It achieves this by factoring out its core system infrastructure from a narrow API that is sufficient to capture the application-specific aspects of a wide variety of index designs. The GiST infrastructure code manages the layout of the index pages on disk, the algorithms for searching indexes and deleting from indexes, and complex transactional details such as page-level locking for high concurrency and write-ahead logging for crash recovery. This allows authors of new tree-based indexes to focus on implementing the novel features of the new index type — for example, the way in which subsets of the data should be described for search — without becoming experts in database system internals.

Although originally designed for answering Boolean selection queries, GiST can also support nearest-neighbor search, and various forms of statistical approximation over large data sets.

## Implementations

The most widely used GiST implementation is in the PostgreSQL relational database; it was also implemented in the Informix Universal Server, and as a standalone library, libgist.

### PostgreSQL

The PostgreSQL GiST implementation includes support for variable length keys, composite keys, concurrency control and recovery; these features are inherited by all GiST extensions. There are several contributed modules developed using GiST and distributed with PostgreSQL. For example:

- rtree_gist, btree_gist - GiST implementation of R-tree and B-tree
- intarray - index support for one-dimensional array of int4's
- tsearch2 - a searchable (full text) data type with indexed access
- ltree - data types, indexed access methods and queries for data organized as a tree-like structures
- hstore - a storage for (key,value) data
- cube - data type, representing multidimensional cubes

The PostgreSQL GiST implementation provides the indexing support for the PostGIS (geographic information system) and the BioPostgres bioinformatics system.
