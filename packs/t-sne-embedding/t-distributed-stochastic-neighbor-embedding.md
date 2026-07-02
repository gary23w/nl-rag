---
title: "t-distributed stochastic neighbor embedding"
source: https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding
domain: t-sne-embedding
license: CC-BY-SA-4.0
tags: t sne embedding, stochastic neighbor embedding, high dimensional visualization, nonlinear projection
fetched: 2026-07-02
---

# t-distributed stochastic neighbor embedding

**t-distributed stochastic neighbor embedding** (**t-SNE**) is a statistical method for visualizing high-dimensional data by giving each datapoint a location in a two or three-dimensional map. It is based on Stochastic Neighbor Embedding originally developed by Geoffrey Hinton and Sam Roweis, where Laurens van der Maaten and Hinton proposed the *t*-distributed variant. It is a nonlinear dimensionality reduction technique for embedding high-dimensional data for visualization in a low-dimensional space of two or three dimensions. Specifically, it models each high-dimensional object by a two- or three-dimensional point in such a way that similar objects are modeled by nearby points and dissimilar objects are modeled by distant points with high probability.

The t-SNE algorithm comprises two main stages. First, t-SNE constructs a probability distribution over pairs of high-dimensional objects in such a way that similar objects are assigned a higher probability while dissimilar points are assigned a lower probability. Second, t-SNE defines a similar probability distribution over the points in the low-dimensional map, and it minimizes the Kullback–Leibler divergence (KL divergence) between the two distributions with respect to the locations of the points in the map. While the original algorithm uses the Euclidean distance between objects as the base of its similarity metric, this can be changed as appropriate. A Riemannian variant is UMAP.

t-SNE has been used for visualization in a wide range of applications, including genomics, computer security research, natural language processing, music analysis, cancer research, bioinformatics, geological domain interpretation, and biomedical signal processing.

For a data set with n elements, t-SNE runs in $O(n^{2})$ time and requires $O(n^{2})$ space.

## Details

Given a set of N high-dimensional objects $\mathbf {x} _{1},\dots ,\mathbf {x} _{N}$ , t-SNE first computes probabilities $p_{ij}$ that are proportional to the similarity of objects $\mathbf {x} _{i}$ and $\mathbf {x} _{j}$ , as follows.

For $i\neq j$ , define

$p_{j\mid i}={\frac {\exp(-\lVert \mathbf {x} _{i}-\mathbf {x} _{j}\rVert ^{2}/2\sigma _{i}^{2})}{\sum _{k\neq i}\exp(-\lVert \mathbf {x} _{i}-\mathbf {x} _{k}\rVert ^{2}/2\sigma _{i}^{2})}}$

and set $p_{i\mid i}=0$ . Note the above denominator ensures $\sum _{j}p_{j\mid i}=1$ for all i .

As van der Maaten and Hinton explained: "The similarity of datapoint $x_{j}$ to datapoint $x_{i}$ is the conditional probability, $p_{j|i}$ , that $x_{i}$ would pick $x_{j}$ as its neighbor if neighbors were picked in proportion to their probability density under a Gaussian centered at $x_{i}$ ."

Now define

$p_{ij}={\frac {p_{j\mid i}+p_{i\mid j}}{2N}}$

This is motivated because $p_{i}$ and $p_{j}$ from the N samples are estimated as 1/N, so the conditional probability can be written as $p_{i\mid j}=Np_{ij}$ and $p_{j\mid i}=Np_{ji}$ . Since $p_{ij}=p_{ji}$ , you can obtain previous formula.

Also note that $p_{ii}=0$ and $\sum _{i,j}p_{ij}=1$ .

The bandwidth of the Gaussian kernels $\sigma _{i}$ is set in such a way that the entropy of the conditional distribution equals a predefined entropy using the bisection method. As a result, the bandwidth is adapted to the density of the data: smaller values of $\sigma _{i}$ are used in denser parts of the data space. The entropy increases with the perplexity of this distribution $P_{i}$ ; this relation is seen as

$Perp(P_{i})=2^{H(P_{i})}$

where $H(P_{i})$ is the Shannon entropy $H(P_{i})=-\sum _{j}p_{j|i}\log _{2}p_{j|i}.$

The perplexity is a hand-chosen parameter of t-SNE, and as the authors state, "perplexity can be interpreted as a smooth measure of the effective number of neighbors. The performance of SNE is fairly robust to changes in the perplexity, and typical values are between 5 and 50.".

Since the Gaussian kernel uses the Euclidean distance $\lVert x_{i}-x_{j}\rVert$ , it is affected by the curse of dimensionality, and in high dimensional data when distances lose the ability to discriminate, the $p_{ij}$ become too similar (asymptotically, they would converge to a constant). It has been proposed to adjust the distances with a power transform, based on the intrinsic dimension of each point, to alleviate this.

t-SNE aims to learn a d -dimensional map $\mathbf {y} _{1},\dots ,\mathbf {y} _{N}$ (with $\mathbf {y} _{i}\in \mathbb {R} ^{d}$ and d typically chosen as 2 or 3) that reflects the similarities $p_{ij}$ as well as possible. To this end, it measures similarities $q_{ij}$ between two points in the map $\mathbf {y} _{i}$ and $\mathbf {y} _{j}$ , using a very similar approach. Specifically, for $i\neq j$ , define $q_{ij}$ as

$q_{ij}={\frac {(1+\lVert \mathbf {y} _{i}-\mathbf {y} _{j}\rVert ^{2})^{-1}}{\sum _{k}\sum _{l\neq k}(1+\lVert \mathbf {y} _{k}-\mathbf {y} _{l}\rVert ^{2})^{-1}}}$

and set $q_{ii}=0$ . Herein a heavy-tailed Student t-distribution (with one-degree of freedom, which is the same as a Cauchy distribution) is used to measure similarities between low-dimensional points in order to allow dissimilar objects to be modeled far apart in the map.

The locations of the points $\mathbf {y} _{i}$ in the map are determined by minimizing the (non-symmetric) Kullback–Leibler divergence of the distribution P from the distribution Q , that is:

$\mathrm {KL} \left(P\parallel Q\right)=\sum _{i\neq j}p_{ij}\log {\frac {p_{ij}}{q_{ij}}}$

The minimization of the Kullback–Leibler divergence with respect to the points $\mathbf {y} _{i}$ is performed using gradient descent. The result of this optimization is a map that reflects the similarities between the high-dimensional inputs.

## Output

While t-SNE plots often seem to display clusters, the visual clusters can be strongly influenced by the chosen parameterization (especially the perplexity) and so a good understanding of the parameters for t-SNE is needed. Such "clusters" can be shown to even appear in structured data with no clear clustering, and so may be false findings. Similarly, the size of clusters produced by t-SNE is not informative, and neither is the distance between clusters. Thus, interactive exploration may be needed to choose parameters and validate results. It has been shown that t-SNE can often recover well-separated clusters, and with special parameter choices, approximates a simple form of spectral clustering.

## Software

- A C++ implementation of Barnes-Hut is available on the github account of one of the original authors.
- The R package Rtsne implements t-SNE in R.
- ELKI contains tSNE, also with Barnes-Hut approximation
- scikit-learn, a popular machine learning library in Python implements t-SNE with both exact solutions and the Barnes-Hut approximation.
- Tensorboard, the visualization kit associated with TensorFlow, also implements t-SNE (online version)
- The Julia package TSne implements t-SNE
