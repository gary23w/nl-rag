---
title: "Silhouette (clustering)"
source: https://en.wikipedia.org/wiki/Silhouette_(clustering)
domain: cluster-analysis-stats
license: CC-BY-SA-4.0
tags: cluster analysis, k-means clustering, hierarchical clustering, silhouette score
fetched: 2026-07-02
---

# Silhouette (clustering)

**Silhouette** is a method of interpretation and validation of consistency within clusters of data. The technique provides a succinct graphical representation of how well each object has been classified. It was proposed by Belgian statistician Peter Rousseeuw in 1987.

The silhouette value is a measure of how similar an object is to its own cluster (cohesion) compared to other clusters (separation). The silhouette value ranges from −1 to +1, where a high value indicates that the object is well matched to its own cluster and poorly matched to neighboring clusters. If most objects have a high value, then the clustering configuration is appropriate. If many points have a low or negative value, then the clustering configuration may have too many or too few clusters. A clustering with an average silhouette width of over 0.7 is considered to be "strong", a value over 0.5 "reasonable", and over 0.25 "weak". However, with an increasing dimensionality of the data, it becomes difficult to achieve such high values because of the curse of dimensionality, as the distances become more similar. The silhouette score is specialized for measuring cluster quality when the clusters are convex-shaped, and may not perform well if the data clusters have irregular shapes or are of varying sizes. The silhouette value can be calculated with any distance metric, such as Euclidean distance or Manhattan distance.

## Definition

Assume the data have been clustered via any technique, such as k-medoids or k-means, into k clusters.

For data point $i\in C_{i}$ (data point i in the cluster $C_{i}$ ), calculate $a(i)$ , the average distance that i is from all other points in that cluster:

$a(i)={\frac {1}{|C_{i}|-1}}\sum _{j\in C_{i},i\neq j}d(i,j)$

where $|C_{i}|$ is the number of points belonging to cluster $C_{i}$ , and $d(i,j)$ is the distance between data points i and j in the cluster $C_{i}$ (we divide by $|C_{i}|-1$ because the distance $d(i,i)$ is not included in the sum). $a(i)$ can be interpreted as a measure of how well i is assigned to its cluster (the smaller the value, the better the assignment).

We then define the mean dissimilarity of point i to some cluster $C_{j}$ as the mean of the distance from i to all points in $C_{j}$ (where $C_{j}\neq C_{i}$ ).

For each data point $i\in C_{i}$ , we now define $b(i)$ as the average distance between i and the points in the closest cluster (hence: "min") that i does not belong to:

$b(i)=\min _{j\neq i}{\frac {1}{|C_{j}|}}\sum _{l\in C_{j}}d(i,l)$

The cluster with the smallest mean dissimilarity is said to be the "neighboring cluster" of i because it is the next best fit cluster for point i .

We now define a *silhouette* (value) of one data point i

$s(i)={\frac {b(i)-a(i)}{\max\{a(i),b(i)\}}}$

, if

$|C_{i}|>1$

and

$s(i)=0$

, if

$|C_{i}|=1$

,

which can also be written as

$s(i)={\begin{cases}1-{\frac {a(i)}{b(i)}},&{\mbox{ if }}a(i)<b(i)\\0,&{\mbox{if }}a(i)=b(i)\\{\frac {b(i)}{a(i)}}-1,&{\mbox{ if }}a(i)>b(i)\\\end{cases}}$

From the above definition, $s(i)$ is bounded to the interval $[-1,1]$ , i.e. $-1\leq s(i)\leq 1.$

Note that $a(i)$ is not clearly defined for clusters with size = 1, in which case we set $s(i)=0$ . This choice is arbitrary, but neutral in the sense that it is at the midpoint of the bounds, -1 and 1.

For $s(i)$ to be close to 1 we require $a(i)\ll b(i)$ . As $a(i)$ is a measure of how dissimilar i is to its own cluster, a small value means it is well matched. Furthermore, a large $b(i)$ implies that i is badly matched to its neighbouring cluster. Thus an $s(i)$ close to 1 means that the data is appropriately clustered. If $s(i)$ is close to -1, then by the same logic we see that i would be more appropriate if it was clustered in its neighbouring cluster. An $s(i)$ near zero means that the datum is on the border of two natural clusters.

The mean $s(i)$ over all points of a cluster is a measure of how tightly grouped all the points in the cluster are. Thus the mean $s(i)$ over all data of the entire dataset is a measure of how appropriately the data have been clustered. If there are too many or too few clusters, as may occur when a poor choice of k is used in the clustering algorithm (e.g., k-means), some of the clusters will typically display much narrower silhouettes than the rest. Thus silhouette plots and means may be used to determine the natural number of clusters within a dataset. One can also increase the likelihood of the silhouette being maximized at the correct number of clusters by re-scaling the data using feature weights that are cluster specific.

Kaufman et al. introduced the term *silhouette coefficient* for the maximum value of the mean $s(i)$ over all data of the entire dataset, i.e.,

$SC=\max _{k}{\tilde {s}}\left(k\right),$

where ${\tilde {s}}\left(k\right)$ represents the mean $s(i)$ over all data of the entire dataset for a specific number of clusters k . The silhouette coefficient describes the best possible clustering possible for a given number of clusters, as measured by the highest average *silhouette* score for all points in the dataset.

## Simplified and medoid silhouette

Computing the silhouette coefficient needs all ${\mathcal {O}}(N^{2})$ pairwise distances, making this evaluation much more costly than clustering with k-means. For a clustering with centers $\mu _{C_{I}}$ for each cluster $C_{I}$ , we can use the following simplified Silhouette for each point $i\in C_{I}$ instead, which can be computed using only ${\mathcal {O}}(Nk)$ distances:

$a'(i)=d(i,\mu _{C_{I}})$

and

$b'(i)=\min _{C_{J}\neq C_{I}}d(i,\mu _{C_{J}})$

,

which has the additional benefit that $a'(i)$ is always defined, then define accordingly the simplified silhouette and simplified silhouette coefficient

$s'(i)={\frac {b'(i)-a'(i)}{\max\{a'(i),b'(i)\}}}$

$SC'=\max _{k}{\frac {1}{N}}\sum _{i}s'\left(i\right)$

.

If the cluster centers are medoids (as in k-medoids clustering) instead of arithmetic means (as in k-means clustering), this is also called the medoid-based silhouette or medoid silhouette.

If every object is assigned to the nearest medoid (as in k-medoids clustering), we know that $a'(i)\leq b'(i)$ , and hence $s'(i)={\frac {b'(i)-a'(i)}{b'(i)}}=1-{\frac {a'(i)}{b'(i)}}$ .

## Silhouette clustering

Instead of using the average silhouette to evaluate a clustering obtained from, e.g., k-medoids or k-means, we can try to directly find a solution that maximizes the Silhouette. We do not have a closed form solution to maximize this, but it will usually be best to assign points to the nearest cluster as done by these methods. Van der Laan et al. proposed to adapt the standard algorithm for k-medoids, PAM, for this purpose and call this algorithm PAMSIL:

1. Choose initial medoids by using PAM
2. Compute the average silhouette of this initial solution
3. For each pair of a medoid m and a non-medoid x
  1. swap m and x
  2. compute the average silhouette of the resulting solution
  3. remember the best swap
  4. un-swap m and x for the next iteration
4. Perform the best swap and return to 3, otherwise stop if no improvement was found.

The loop in step 3 is executed for ${\mathcal {O}}(Nk)$ pairs, and involves computing the silhouette in ${\mathcal {O}}(N^{2})$ , hence this algorithm needs ${\mathcal {O}}(N^{3}ki)$ time, where i is the number of iterations.

Because this is a fairly expensive operation, the authors propose to also use the medoid-based silhouette, and call the resulting algorithm PAMMEDSIL. It needs ${\mathcal {O}}(N^{2}k^{2}i)$ time.

Batool et al. propose a similar algorithm under the name OSil, and propose a CLARA-like sampling strategy for larger data sets, that solves the problem only for a sub-sample.

By adopting recent improvements to the PAM algorithm, FastMSC reduces the runtime using the medoid silhouette to just ${\mathcal {O}}(N^{2}i)$ .

By starting with a maximum number of clusters kmax and iteratively removing the worst center (in terms of a change in silhouette) and re-optimizing, the best (highest medoid silhouette) clustering can be automatically determined. As data structures can be reused, this reduces the computation cost substantially over repeatedly running the algorithm for different numbers of clusters. This algorithm needs pairwise distances and is typically implemented with a pairwise distance matrix. The ${\mathcal {O}}(N^{2})$ memory requirement is the main limiting factor for applying this to very large data sets.

## Density-based Silhouette coefficient: the DBCV index

The traditional Silhouette score can be misleading when used to assess nested, concave-shaped clusters. In these contexts, a density-based version of the Silhouette score was proposed in 2014 by David Moulavi and colleagues in their work, and is called *DBCV index*.
