---
title: "Hierarchical clustering"
source: https://en.wikipedia.org/wiki/Hierarchical_clustering
domain: dendrogram-viz
license: CC-BY-SA-4.0
tags: dendrogram, hierarchical clustering, neighbor joining, tree diagram
fetched: 2026-07-02
---

# Hierarchical clustering

In data mining and statistics, **hierarchical clustering** (also called **hierarchical cluster analysis** or **HCA**) is a method of cluster analysis that seeks to build a hierarchy of clusters. Strategies for hierarchical clustering generally fall into two categories:

- **Agglomerative**: Agglomerative clustering, often referred to as a "bottom-up" approach, begins with each data point as an individual cluster. At each step, the algorithm merges the two most similar clusters based on a chosen distance metric (e.g., Euclidean distance) and linkage criterion (e.g., single-linkage, complete-linkage). This process continues until all data points are combined into a single cluster or a stopping criterion is met. Agglomerative methods are more commonly used due to their simplicity and computational efficiency for small to medium-sized datasets.
- **Divisive**: Divisive clustering, known as a "top-down" approach, starts with all data points in a single cluster and recursively splits the cluster into smaller ones. At each step, the algorithm selects a cluster and divides it into two or more subsets, often using a criterion such as maximizing the distance between resulting clusters. Divisive methods are less common but can be useful when the goal is to identify large, distinct clusters first.

In general, the merges and splits are determined in a greedy manner. The results of hierarchical clustering are usually presented in a dendrogram.

Hierarchical clustering has the distinct advantage that any valid measure of distance can be used. In fact, the observations themselves are not required: all that is used is a matrix of distances. On the other hand, except for the special case of single-linkage distance, none of the algorithms (except exhaustive search in ${\mathcal {O}}(2^{n})$ ) can be guaranteed to find the optimum solution.

## Complexity

The standard algorithm for **hierarchical agglomerative clustering** (HAC) has a time complexity of ${\mathcal {O}}(n^{3})$ and requires $\Omega (n^{2})$ memory, which makes it too slow for even medium data sets. However, for some special cases, optimal efficient agglomerative methods (of complexity ${\mathcal {O}}(n^{2})$ ) are known: **SLINK** for single-linkage and CLINK for complete-linkage clustering. With a heap, the runtime of the general case can be reduced to ${\mathcal {O}}(n^{2}\log n)$ instead of ${\mathcal {O}}(n^{3})$ , at the cost of additional the memory requirements. In many cases, the memory overheads of this approach are too large to make it practically usable. Methods exist which use quadtrees that demonstrate ${\mathcal {O}}(n^{2})$ total running time with ${\mathcal {O}}(n)$ space.

Divisive clustering with an exhaustive search is ${\mathcal {O}}(2^{n})$ , but it is common to use faster heuristics to choose splits, such as *k*-means.

## Distance metrics

While the linkage criterion determines how dissimilarity between sets of observations is computed, the underlying distance metric determines how dissimilarity between individual observations is measured. Because hierarchical clustering permits any valid measure of distance, the choice of metric is guided by the nature of the data and can have a significant effect on the resulting clustering.

**Euclidean distance** is the most widely used metric for continuous numerical data. It corresponds to the straight-line distance between two points in Euclidean space and is the default choice in most statistical software:

$d(\mathbf {x} ,\mathbf {y} )={\sqrt {\sum _{i=1}^{n}(x_{i}-y_{i})^{2}}}$

**Manhattan distance** (also called city-block or *L*1 distance) sums the absolute differences across features:

$d(\mathbf {x} ,\mathbf {y} )=\sum _{i=1}^{n}|x_{i}-y_{i}|$

It is often preferred when features are measured on different scales or when the data contain outliers, as it is less sensitive to large deviations than Euclidean distance.

**Cosine distance** measures angular dissimilarity between two non-zero vectors:

$d(\mathbf {x} ,\mathbf {y} )=1-{\frac {\mathbf {x} \cdot \mathbf {y} }{\lVert \mathbf {x} \rVert \,\lVert \mathbf {y} \rVert }}$

Because it disregards vector magnitude, it is frequently used in text mining and document clustering, where documents are represented as high-dimensional term-frequency vectors.

**Mahalanobis distance** accounts for correlations between features by incorporating the inverse of the data's covariance matrix *S*:

$d(\mathbf {x} ,\mathbf {y} )={\sqrt {(\mathbf {x} -\mathbf {y} )^{\top }S^{-1}(\mathbf {x} -\mathbf {y} )}}$

Unlike Euclidean distance, it is scale-invariant and is useful when features are correlated or measured in different units.

**Hamming distance** is used for categorical or binary data and counts the number of positions at which two observations differ. It is commonly applied to genetic sequences and binary feature vectors.

The choice of metric interacts with the choice of linkage criterion. For example, Ward's method and centroid-based linkages are defined in terms of squared Euclidean distances, whereas single-linkage and complete-linkage clustering can be used with any valid metric.

## Cluster linkage

In order to decide which clusters should be combined (for agglomerative), or where a cluster should be split (for divisive), a measure of dissimilarity between sets of observations is required. In most methods of hierarchical clustering, this is achieved by use of an appropriate distance *d*, such as the Euclidean distance, between *single* observations of the data set, and a linkage criterion, which specifies the dissimilarity of *sets* as a function of the pairwise distances of observations in the sets. The choice of metric as well as linkage can have a major impact on the result of the clustering, where the lower level metric determines which objects are most similar, whereas the linkage criterion influences the shape of the clusters. For example, complete-linkage tends to produce more spherical clusters than single-linkage.

The linkage criterion determines the distance between sets of observations as a function of the pairwise distances between observations.

Some commonly used linkage criteria between two sets of observations *A* and *B* and a distance *d* are:

| Names | Formula |
|---|---|
| Maximum or complete-linkage clustering | $\max _{a\in A,\,b\in B}d(a,b)$ |
| Minimum or single-linkage clustering | $\min _{a\in A,\,b\in B}d(a,b)$ |
| Unweighted average linkage clustering (or UPGMA) | ${\frac {1}{\|A\|\cdot \|B\|}}\sum _{a\in A}\sum _{b\in B}d(a,b).$ |
| Weighted average linkage clustering (or WPGMA) | $d(i\cup j,k)={\frac {d(i,k)+d(j,k)}{2}}.$ |
| Centroid linkage clustering, or UPGMC | $\lVert \mu _{A}-\mu _{B}\rVert ^{2}$ where $\mu _{A}$ and $\mu _{B}$ are the centroids of *A* resp. *B*. |
| Median linkage clustering, or WPGMC | $d(i\cup j,k)=d(m_{i\cup j},m_{k})$ where $m_{i\cup j}={\tfrac {1}{2}}\left(m_{i}+m_{j}\right)$ |
| Versatile linkage clustering | ${\sqrt[{p}]{{\frac {1}{\|A\|\cdot \|B\|}}\sum _{a\in A}\sum _{b\in B}d(a,b)^{p}}},p\neq 0$ |
| Ward linkage, Minimum Increase of Sum of Squares (MISSQ) | ${\frac {\|A\|\cdot \|B\|}{\|A\cup B\|}}\lVert \mu _{A}-\mu _{B}\rVert ^{2}=\sum _{x\in A\cup B}\lVert x-\mu _{A\cup B}\rVert ^{2}-\sum _{x\in A}\lVert x-\mu _{A}\rVert ^{2}-\sum _{x\in B}\lVert x-\mu _{B}\rVert ^{2}$ |
| Minimum Error Sum of Squares (MNSSQ) | $\sum _{x\in A\cup B}\lVert x-\mu _{A\cup B}\rVert ^{2}$ |
| Minimum Increase in Variance (MIVAR) | ${\frac {1}{\|A\cup B\|}}\sum _{x\in A\cup B}\lVert x-\mu _{A\cup B}\rVert ^{2}-{\frac {1}{\|A\|}}\sum _{x\in A}\lVert x-\mu _{A}\rVert ^{2}-{\frac {1}{\|B\|}}\sum _{x\in B}\lVert x-\mu _{B}\rVert ^{2}$ $={\text{Var}}(A\cup B)-{\text{Var}}(A)-{\text{Var}}(B)$ |
| Minimum Variance (MNVAR) | ${\frac {1}{\|A\cup B\|}}\sum _{x\in A\cup B}\lVert x-\mu _{A\cup B}\rVert ^{2}={\text{Var}}(A\cup B)$ |
| Hausdorff linkage | $\max _{x\in A\cup B}\min _{y\in A\cup B}d(x,y)$ |
| Minimum Sum Medoid linkage | $\min _{m\in A\cup B}\sum _{y\in A\cup B}d(m,y)$ such that m is the medoid of the resulting cluster |
| Minimum Sum Increase Medoid linkage | $\min _{m\in A\cup B}\sum _{y\in A\cup B}d(m,y)-\min _{m\in A}\sum _{y\in A}d(m,y)-\min _{m\in B}\sum _{y\in B}d(m,y)$ |
| Medoid linkage | $d(m_{A},m_{B})$ where $m_{A}$ , $m_{B}$ are the medoids of the previous clusters |
| Minimum energy clustering | ${\frac {2}{nm}}\sum _{i,j=1}^{n,m}\\|a_{i}-b_{j}\\|_{2}-{\frac {1}{n^{2}}}\sum _{i,j=1}^{n}\\|a_{i}-a_{j}\\|_{2}-{\frac {1}{m^{2}}}\sum _{i,j=1}^{m}\\|b_{i}-b_{j}\\|_{2}$ |

Some of these can only be recomputed recursively (WPGMA, WPGMC), for many a recursive computation with Lance-Williams-equations is more efficient, while for other (Hausdorff, Medoid) the distances have to be computed with the slower full formula. Other linkage criteria include:

- The probability that candidate clusters spawn from the same distribution function (V-linkage).
- The product of in-degree and out-degree on a k-nearest-neighbour graph (graph degree linkage).
- The increment of some cluster descriptor (i.e., a quantity defined for measuring the quality of a cluster) after merging two clusters.

### Comparison of linkage methods

The choice of linkage criterion significantly affects the shape and quality of the resulting clusters. Each method has distinct strengths and weaknesses depending on the structure of the data.

**Single linkage** (also called the nearest-neighbor method) defines the distance between two clusters as the minimum distance between any pair of points, one from each cluster. This method can detect and handle clusters of arbitrary shape, including elongated and non-globular structures. However, it is highly sensitive to noise and outliers, because a single pair of close points is sufficient to merge two clusters.

**Complete linkage** defines the distance between two clusters as the maximum distance between any pair of points across the two clusters. It is less susceptible to noise and outliers than single linkage. However, complete linkage is biased toward producing globular clusters of similar size and may incorrectly break apart large or irregularly shaped clusters.

**Average linkage** (specifically UPGMA, the unweighted pair group method with arithmetic mean) defines the distance between two clusters as the average of all pairwise distances between points in the two clusters. It represents a compromise between the extremes of single and complete linkage. Average linkage is more robust to noise than single linkage but, like complete linkage, it tends to be biased toward detecting globular clusters.

| Linkage method | Distance definition | Cluster shape detected | Noise sensitivity | Key limitation |
|---|---|---|---|---|
| Single linkage | Minimum pairwise distance | Arbitrary (non-globular) | High | Sensitive to noise and outliers |
| Complete linkage | Maximum pairwise distance | Globular | Low | Tends to break large clusters |
| Average linkage (UPGMA) | Mean of all pairwise distances | Globular | Moderate | Biased toward equal-sized clusters |

#### Computational complexity

The naive implementation of agglomerative hierarchical clustering has a time complexity of O(*n*³) and a space complexity of O(*n*²), where *n* is the number of data points, because at each of the *n* − 1 merge steps the algorithm must search and update an *n* × *n* proximity matrix. For single linkage, optimized algorithms based on minimum spanning trees reduce the time complexity to O(*n*² log *n*). For other linkage criteria, the use of priority queues and nearest-neighbor chains can also achieve O(*n*² log *n*) time in practice.

## Hausdorff linkage

Hausdorff linkage is a hierarchical clustering criterion based on the Hausdorff distance, a metric defined between sets of points in a given metric space. Unlike standard linkage methods that rely on pairwise distances between individual observations, Hausdorff linkage evaluates distances between entire clusters, thereby incorporating information about their geometric structure.

Formally, let $(S,\delta )$ be a metric space, and let A and B be nonempty compact subsets of S . The distance from a point a to a set B is defined as:

${\tilde {d}}(a,B)=\inf _{b\in B}\delta (a,b)$

Extending this to sets, the directed distance from A to B is:

${\tilde {d}}(A,B)=\sup _{a\in A}\inf _{b\in B}\delta (a,b)$

Since this quantity is not symmetric, the Hausdorff distance between two sets is defined as:

$d_{H}(A,B)=\max\{{\tilde {d}}(A,B),{\tilde {d}}(B,A)\}$

This definition captures the largest distance from a point in one set to the closest point in the other set. Equivalently, it can be interpreted as the smallest radius r such that every point of A lies within distance r of some point in B , and every point of B lies within distance r of some point in A . In this sense, the Hausdorff distance measures the maximum mismatch between two sets.

In hierarchical clustering, Hausdorff linkage uses $d_{H}(A,B)$ as the dissimilarity measure between clusters. Initially, each data point forms its own cluster, and the Hausdorff distance between singleton sets reduces to the original metric. At each step, the two clusters with the smallest Hausdorff distance are merged, and distances are recomputed using the same set-based definition. This iterative process continues until all points belong to a single cluster, producing a hierarchical structure (dendrogram).

Compared to other linkage criteria such as single, complete, or average linkage, Hausdorff linkage operates on a set-to-set basis rather than relying solely on pairwise point distances. As a result, it captures the global geometry of clusters and can better preserve structural features of the data. It has been shown to provide behavior intermediate between single and complete linkage, avoiding the chaining effect of the former while reducing the tendency of the latter to overestimate distances between clusters.

However, these advantages come with increased computational cost. Computing the Hausdorff distance between two clusters typically requires evaluating distances between all pairs of points across the sets, often via a max–min procedure over a distance matrix. This makes Hausdorff linkage more computationally expensive than simpler linkage criteria, particularly for large datasets.

Overall, Hausdorff linkage provides a mathematically well-founded clustering approach that is effective for distinguishing complex structures in data.

## Agglomerative clustering example

For example, suppose this data is to be clustered, and the Euclidean distance is the distance metric.

The hierarchical clustering dendrogram would be:

Cutting the tree at a given height will give a partitioning clustering at a selected precision. In this example, cutting after the second row (from the top) of the dendrogram will yield clusters {a} {b c} {d e} {f}. Cutting after the third row will yield clusters {a} {b c} {d e f}, which is a coarser clustering, with a smaller number but larger clusters.

### Animated example

The clustering process can also be illustrated step-by-step to show how the dendrogram is constructed from the underlying data.

In this visualization, each point begins as its own cluster. At each step, the two clusters with the smallest distance between them are merged. On the left, dashed lines indicate which clusters are combined, and a running list of cluster groupings shows how clusters evolve over time. On the right, the dendrogram is constructed simultaneously, with each merge represented by a new branch.

The height of each merge in the dendrogram corresponds to the distance or dissimilarity between the clusters being combined. Merges that occur at lower heights represent clusters that are more similar, while merges at higher heights indicate greater dissimilarity. Color-coding is used to associate each merge step in the data visualization with its corresponding branch in the dendrogram.

### Interpreting dendrogram height

A key aspect of interpreting a dendrogram is understanding the meaning of branch height. The height at which two clusters are joined represents the distance or dissimilarity between those clusters, where lower merges indicate greater similarity and higher merges indicate greater dissimilarity. Early merges at lower heights reflect the closest relationships between observations, while later merges combine increasingly different groups.

When the dendrogram is scaled using actual or normalized distances, the vertical spacing between merges provides insight into the relative differences between clusters. Large vertical gaps between successive merges often indicate meaningful separations in the data.and can help guide the selection of cluster boundaries, although dendrograms alone should not be used to definitively determine the number of clusters. Because dendrograms summarize underlying distance relationships, some information may be lost in the visualization, and interpretations are generally most reliable for clusters that merge at lower heights.

## Selecting the number of clusters

In hierarchical clustering, the number of clusters is not determined automatically and must be chosen by analyzing the dendrogram. A common approach is to “cut” the dendrogram at a selected height, which partitions the data into clusters based on where the cut intersects the tree structure. The choice of cut level has a significant impact on the resulting clustering.

One widely used heuristic is to identify large vertical gaps in the dendrogram, which correspond to substantial increases in the distance between successive merges. Cutting the dendrogram at a height just before such a gap can produce clusters that reflect natural groupings in the data. This is based on the observation that merges occurring at much larger distances often combine dissimilar clusters.

In practice, the selection of the number of clusters may also depend on domain knowledge or application-specific requirements. Quantitative measures such as the silhouette coefficient can be used to evaluate the quality of different clusterings. Because hierarchical clustering is sensitive to the choice of distance metric and linkage criterion, the optimal number of clusters may vary depending on these factors.

This method builds the hierarchy from the individual elements by progressively merging clusters. In our example, we have six elements {a} {b} {c} {d} {e} and {f}. The first step is to determine which elements to merge in a cluster. Usually, we want to take the two closest elements, according to the chosen distance.

Optionally, one can also construct a distance matrix at this stage, where the number in the *i*-th row *j*-th column is the distance between the *i*-th and *j*-th elements. Then, as clustering progresses, rows and columns are merged as the clusters are merged and the distances updated. This is a common way to implement this type of clustering, and has the benefit of caching distances between clusters. A simple agglomerative clustering algorithm is described in the single-linkage clustering page; it can easily be adapted to different types of linkage (see below).

Suppose we have merged the two closest elements *b* and *c*, we now have the following clusters {*a*}, {*b*, *c*}, {*d*}, {*e*} and {*f*}, and want to merge them further. To do that, we need to take the distance between {a} and {b c}, and therefore define the distance between two clusters. Usually the distance between two clusters ${\mathcal {A}}$ and ${\mathcal {B}}$ is one of the following:

- The maximum distance between elements of each cluster (also called complete-linkage clustering):

$\max\{\,d(x,y):x\in {\mathcal {A}},\,y\in {\mathcal {B}}\,\}.$

- The minimum distance between elements of each cluster (also called single-linkage clustering):

$\min\{\,d(x,y):x\in {\mathcal {A}},\,y\in {\mathcal {B}}\,\}.$

- The mean distance between elements of each cluster (also called average linkage clustering, used e.g. in UPGMA):

${1 \over {|{\mathcal {A}}|\cdot |{\mathcal {B}}|}}\sum _{x\in {\mathcal {A}}}\sum _{y\in {\mathcal {B}}}d(x,y).$

- The sum of all intra-cluster variance.
- The increase in variance for the cluster being merged (Ward's method)
- The probability that candidate clusters spawn from the same distribution function (V-linkage).

In case of tied minimum distances, a pair is randomly chosen, thus being able to generate several structurally different dendrograms. Alternatively, all tied pairs may be joined at the same time, generating a unique dendrogram.

One can always decide to stop clustering when there is a sufficiently small number of clusters (number criterion). Some linkages may also guarantee that agglomeration occurs at a greater distance between clusters than the previous agglomeration, and then one can stop clustering when the clusters are too far apart to be merged (distance criterion). However, this is not the case of, e.g., the centroid linkage where the so-called reversals (inversions, departures from ultrametricity) may occur.

## Divisive clustering

The basic principle of divisive clustering was published as the DIANA (DIvisive ANAlysis clustering) algorithm. Initially, all data is in the same cluster, and the largest cluster is split until every object is separate. Because there exist $O(2^{n})$ ways of splitting each cluster, heuristics are needed. DIANA chooses the object with the maximum average dissimilarity and then moves all objects to this cluster that are more similar to the new cluster than to the remainder.

Informally, DIANA is not so much a process of "dividing" as it is of "hollowing out": each iteration, an existing cluster (e.g. the initial cluster of the entire dataset) is chosen to form a new cluster inside of it. Objects progressively move to this nested cluster, and hollow out the existing cluster. Eventually, all that's left inside a cluster is nested clusters that grew there, without it owning any loose objects by itself.

Formally, DIANA operates in the following steps:

1. Let $C_{0}=\{1\dots n\}$ be the set of all n object indices and ${\mathcal {C}}=\{C_{0}\}$ the set of all formed clusters so far.
2. Iterate the following until $|{\mathcal {C}}|=n$ :
  1. Find the current cluster with 2 or more objects that has the largest diameter: $C_{*}=\arg \max _{C\in {\mathcal {C}}}\max _{i_{1},i_{2}\in C}\delta (i_{1},i_{2})$
  2. Find the object in this cluster with the most dissimilarity to the rest of the cluster: $i^{*}=\arg \max _{i\in C_{*}}{\frac {1}{|C_{*}|-1}}\sum _{j\in C_{*}\setminus \{i\}}\delta (i,j)$
  3. Pop $i^{*}$ from its old cluster $C_{*}$ and put it into a new *splinter group* $C_{\textrm {new}}=\{i^{*}\}$ .
  4. As long as $C_{*}$ isn't empty, keep migrating objects from $C_{*}$ to add them to $C_{\textrm {new}}$ . To choose which objects to migrate, don't just consider dissimilarity to $C_{*}$ , but also adjust for dissimilarity to the splinter group: let $i^{*}=\arg \max _{i\in C}D(i)$ where we define $D(i)={\frac {1}{|C_{*}|-1}}\sum _{j\in C_{*}\setminus \{i\}}\delta (i,j)-{\frac {1}{|C_{\textrm {new}}|}}\sum _{j\in C_{\textrm {new}}}\delta (i,j)$ , then either stop iterating when $D(i^{*})<0$ , or migrate $i^{*}$ .
  5. Add $C_{\textrm {new}}$ to ${\mathcal {C}}$ .

Intuitively, $D(i)$ above measures how strongly an object wants to leave its current cluster, but it is attenuated when the object wouldn't fit in the splinter group either. Such objects will likely start their own splinter group eventually.

The dendrogram of DIANA can be constructed by letting the splinter group $C_{\textrm {new}}$ be a child of the hollowed-out cluster $C_{*}$ each time. This constructs a tree with $C_{0}$ as its root and n unique single-object clusters as its leaves.

## Software

### Open source implementations

- ALGLIB implements several hierarchical clustering algorithms (single-link, complete-link, Ward) in C++ and C# with O(n²) memory and O(n³) run time.
- ELKI includes multiple hierarchical clustering algorithms, various linkage strategies and also includes the efficient SLINK, CLINK and Anderberg algorithms, flexible cluster extraction from dendrograms and various other cluster analysis algorithms.
- Julia has an implementation inside the Clustering.jl package.
- Octave, the GNU analog to MATLAB implements hierarchical clustering in function "linkage".
- Orange, a data mining software suite, includes hierarchical clustering with interactive dendrogram visualisation.
- R has built-in functions and packages that provide functions for hierarchical clustering.
- SciPy implements hierarchical clustering in Python, including the efficient SLINK algorithm.
- scikit-learn also implements hierarchical clustering in Python.
- Weka includes hierarchical cluster analysis.

### Commercial implementations

- MATLAB includes hierarchical cluster analysis.
- SAS includes hierarchical cluster analysis in PROC CLUSTER.
- Mathematica includes a Hierarchical Clustering Package.
- NCSS includes hierarchical cluster analysis.
- SPSS includes hierarchical cluster analysis.
- Qlucore Omics Explorer includes hierarchical cluster analysis.
- Stata includes hierarchical cluster analysis.
- CrimeStat includes a nearest neighbor hierarchical cluster algorithm with a graphical output for a Geographic Information System.

## Scalable implementation with HAL-x

Standard hierarchical agglomerative clustering is difficult to apply to very large datasets because typical implementations require substantial memory for pairwise structures and can scale poorly as n grows (see § Complexity above). In computational biology, single-cell technologies such as mass cytometry routinely produce tens of millions of high-dimensional observations, which motivates specialized workflows that preserve biological resolution without requiring that every expensive step be run on the full matrix at once.

### Overview

**HAL-x** is a hierarchical density clustering algorithm introduced for large, high-dimensional point clouds. Rather than agglomerating solely from a fixed linkage criterion on a precomputed distance matrix, HAL-x builds an initial set of high-density “pure” clusters in a low-dimensional embedding of a downsampled subset of the data, then merges clusters using **supervised linkage**: it trains supervised classifiers on the original (unreduced) feature space to measure how reliably two proposed clusters can be separated, and uses those separation scores to decide merge order. The method outputs a hierarchy that can be read as a tree of merges together with a predictive model that can assign labels to held-out or newly collected cells without re-running the entire clustering pipeline on every point during exploratory iterations.

In outline, the published implementation proceeds by (i) normalizing and downsampling for dimensionality reduction (commonly t-SNE or UMAP), (ii) estimating density in the embedded space to obtain initial clusters, (iii) constructing a sparse *k*-nearest neighbor graph between clusters with edge weights derived from classifier-based separability on unreduced coordinates, and (iv) agglomeratively merging the weakest edges while retaining cross-validated accuracy information so users can obtain multiple resolutions from one fitted model.

The figure summarizes the HAL-x workflow: dimensionality reduction for density estimation, density-based seed clusters, a supervised linkage graph between clusters, and successive merges to a chosen generalization threshold.

### Tradeoffs compared with traditional hierarchical clustering

Compared with textbook agglomerative hierarchical clustering on a full $n\times n$ dissimilarity structure, HAL-x trades exact, purely geometric linkage updates for a pipeline that depends on embedding choices, density-thresholding heuristics, and the capacity of classifiers such as random forests or support vector machines to estimate separability in high dimensions. This design targets scalability: expensive steps are deliberately restricted to manageable downscaled subsamples, while label prediction can be applied broadly to the full dataset once the hierarchy and classifiers are established. Because of this, HAL-x is extremely useful when hierarchical clustering requires minimal RAM. A practical limitation, common to embedding-first pipelines, is that low-dimensional representations can distort global geometry and reduce accuracy. The HAL-x paper discusses when auxiliary preprocessing such as PCA may help for correlated features.

### Applications in cellular biology

HAL-x was motivated by workflows in which biologists need many related clusterings at different granularities (for example to preserve rare leukocyte subsets while still summarizing abundant lineages) without repeatedly training separate models from scratch on millions of cells. The authors report analyses on large cytometry-style datasets where rapid, tunable clusterings are used to support downstream interpretation of cellular phenotypes across conditions.
