---
title: "Model-based clustering"
source: https://en.wikipedia.org/wiki/Model-based_clustering
domain: mixture-models-em
license: CC-BY-SA-4.0
tags: mixture model, expectation maximization, Gaussian mixture model, latent class model
fetched: 2026-07-02
---

# Model-based clustering

In statistics, cluster analysis is the algorithmic grouping of objects into homogeneous groups based on numerical measurements. **Model-based clustering** based on a statistical model for the data, usually a mixture model. This has several advantages, including a principled statistical basis for clustering, and ways to choose the number of clusters, to choose the best clustering model, to assess the uncertainty of the clustering, and to identify outliers that do not belong to any group.

## Model-based clustering

Suppose that for each of n observations we have data on d variables, denoted by $y_{i}=(y_{i,1},\ldots ,y_{i,d})$ for observation i . Then model-based clustering expresses the probability density function of $y_{i}$ as a finite mixture, or weighted average of G component probability density functions:

$p(y_{i})=\sum _{g=1}^{G}\tau _{g}f_{g}(y_{i}\mid \theta _{g}),$

where $f_{g}$ is a probability density function with parameter $\theta _{g}$ , $\tau _{g}$ is the corresponding mixture probability where $\sum _{g=1}^{G}\tau _{g}=1$ . Then in its simplest form, model-based clustering views each component of the mixture model as a cluster, estimates the model parameters, and assigns each observation to cluster corresponding to its most likely mixture component.

### Gaussian mixture model

The most common model for continuous data is that $f_{g}$ is a multivariate normal distribution with mean vector $\mu _{g}$ and covariance matrix $\Sigma _{g}$ , so that $\theta _{g}=(\mu _{g},\Sigma _{g})$ . This defines a Gaussian mixture model. The parameters of the model, $\tau _{g}$ and $\theta _{g}$ for $g=1,\ldots ,G$ , are typically estimated by maximum likelihood estimation using the expectation-maximization algorithm (EM); see also EM algorithm and GMM model.

Bayesian inference is also often used for inference about finite mixture models. The Bayesian approach also allows for the case where the number of components, G , is infinite, using a Dirichlet process prior, yielding a Dirichlet process mixture model for clustering.

### Choosing the number of clusters

An advantage of model-based clustering is that it provides statistically principled ways to choose the number of clusters. Each different choice of the number of groups G corresponds to a different mixture model. Then standard statistical model selection criteria such as the Bayesian information criterion (BIC) can be used to choose G . The integrated completed likelihood (ICL) is a different criterion designed to choose the number of clusters rather than the number of mixture components in the model; these will often be different if highly non-Gaussian clusters are present.

### Parsimonious Gaussian mixture model

For data with high dimension, d , using a full covariance matrix for each mixture component requires estimation of many parameters, which can result in a loss of precision, generalizabity and interpretability. Thus it is common to use more parsimonious component covariance matrices exploiting their geometric interpretation. Gaussian clusters are ellipsoidal, with their volume, shape and orientation determined by the covariance matrix. Consider the eigendecomposition of a matrix

$\Sigma _{g}=\lambda _{g}D_{g}A_{g}D_{g}^{T},$

where $D_{g}$ is the matrix of eigenvectors of $\Sigma _{g}$ , $A_{g}={\mbox{diag}}\{A_{1,g},\ldots ,A_{d,g}\}$ is a diagonal matrix whose elements are proportional to the eigenvalues of $\Sigma _{g}$ in descending order, and $\lambda _{g}$ is the associated constant of proportionality. Then $\lambda _{g}$ controls the volume of the ellipsoid, $A_{g}$ its shape, and $D_{g}$ its orientation.

Each of the volume, shape and orientation of the clusters can be constrained to be equal (E) or allowed to vary (V); the orientation can also be spherical, with identical eigenvalues (I). This yields 14 possible clustering models, shown in this table:

| Model | Description | # Parameters |
|---|---|---|
| EII | Spherical, equal volume | 1 |
| VII | Spherical, varying volume | 9 |
| EEI | Diagonal, equal volume & shape | 4 |
| VEI | Diagonal, equal shape | 12 |
| EVI | Diagonal, equal volume, varying shape | 28 |
| VVI | Diagonal, varying volume & shape | 36 |
| EEE | Equal | 10 |
| VEE | Equal shape & orientation | 18 |
| EVE | Equal volume & orientation | 34 |
| VVE | Equal orientation | 42 |
| EEV | Equal volume & shape | 58 |
| VEV | Equal shape | 66 |
| EVV | Equal volume | 82 |
| VVV | Varying | 90 |

It can be seen that many of these models are more parsimonious, with far fewer parameters than the unconstrained model that has 90 parameters when $G=4$ and $d=9$ .

Several of these models correspond to well-known heuristic clustering methods. For example, k-means clustering is equivalent to estimation of the EII clustering model using the classification EM algorithm. The Bayesian information criterion (BIC) can be used to choose the best clustering model as well as the number of clusters. It can also be used as the basis for a method to choose the variables in the clustering model, eliminating variables that are not useful for clustering.

Different Gaussian model-based clustering methods have been developed with an eye to handling high-dimensional data. These include the pgmm method, which is based on the mixture of factor analyzers model, and the HDclassif method, based on the idea of subspace clustering.

The mixture-of-experts framework extends model-based clustering to include covariates.

## Example

We illustrate the method with a dateset consisting of three measurements (glucose, insulin, sspg) on 145 subjects for the purpose of diagnosing diabetes and the type of diabetes present. The subjects were clinically classified into three groups: normal, chemical diabetes and overt diabetes, but we use this information only for evaluating clustering methods, not for classifying subjects.

The BIC plot shows the BIC values for each combination of the number of clusters, G , and the clustering model from the Table. Each curve corresponds to a different clustering model. The BIC favors 3 groups, which corresponds to the clinical assessment. It also favors the unconstrained covariance model, VVV. This fits the data well, because the normal patients have low values of both sspg and insulin, while the distributions of the chemical and overt diabetes groups are elongated, but in different directions. Thus the volumes, shapes and orientations of the three groups are clearly different, and so the unconstrained model is appropriate, as selected by the model-based clustering method.

The classification plot shows the classification of the subjects by model-based clustering. The classification was quite accurate, with a 12% error rate as defined by the clinical classification. Other well-known clustering methods performed worse with higher error rates, such as single-linkage clustering with 46%, average link clustering with 30%, complete-linkage clustering also with 30%, and k-means clustering with 28%.

## Outliers in clustering

An outlier in clustering is a data point that does not belong to any of the clusters. One way of modeling outliers in model-based clustering is to include an additional mixture component that is very dispersed, with for example a uniform distribution. Another approach is to replace the multivariate normal densities by t -distributions, with the idea that the long tails of the t -distribution would ensure robustness to outliers. However, this is not breakdown-robust. A third approach is the "tclust" or data trimming approach which excludes observations identified as outliers when estimating the model parameters.

## Non-Gaussian clusters and merging

Sometimes one or more clusters deviate strongly from the Gaussian assumption. If a Gaussian mixture is fitted to such data, a strongly non-Gaussian cluster will often be represented by several mixture components rather than a single one. In that case, cluster merging can be used to find a better clustering. A different approach is to use mixtures of complex component densities to represent non-Gaussian clusters.

## Non-continuous data

### Categorical data

Clustering multivariate categorical data is most often done using the latent class model. This assumes that the data arise from a finite mixture model, where within each cluster the variables are independent.

### Mixed data

These arise when variables are of different types, such as continuous, categorical or ordinal data. A latent class model for mixed data assumes local independence between the variable. The location model relaxes the local independence assumption. The clustMD approach assumes that the observed variables are manifestations of underlying continuous Gaussian latent variables.

### Count data

The simplest model-based clustering approach for multivariate count data is based on finite mixtures with locally independent Poisson distributions, similar to the latent class model. More realistic approaches allow for dependence and overdispersion in the counts. These include methods based on the multivariate Poisson distribution, the multivarate Poisson-log normal distribution, the integer-valued autoregressive (INAR) model and the Gaussian Cox model.

### Sequence data

These consist of sequences of categorical values from a finite set of possibilities, such as life course trajectories. Model-based clustering approaches include group-based trajectory and growth mixture models and a distance-based mixture model.

### Rank data

These arise when individuals rank objects in order of preference. The data are then ordered lists of objects, arising in voting, education, marketing and other areas. Model-based clustering methods for rank data include mixtures of Plackett-Luce models and mixtures of Benter models, and mixtures of Mallows models.

### Network data

These consist of the presence, absence or strength of connections between individuals or nodes, and are widespread in the social sciences and biology. The stochastic blockmodel carries out model-based clustering of the nodes in a network by assuming that there is a latent clustering and that connections are formed independently given the clustering. The latent position cluster model assumes that each node occupies a position in an unobserved latent space, that these positions arise from a mixture of Gaussian distributions, and that presence or absence of a connection is associated with distance in the latent space.

## Software

Much of the model-based clustering software is in the form of a publicly and freely available R package. Many of these are listed in the CRAN Task View on Cluster Analysis and Finite Mixture Models. The most used such package is mclust, which is used to cluster continuous data and has been downloaded over 8 million times.

The poLCA package clusters categorical data using the latent class model. The clustMD package clusters mixed data, including continuous, binary, ordinal and nominal variables.

The flexmix package does model-based clustering for a range of component distributions. The mixtools package can cluster different data types. Both flexmix and mixtools implement model-based clustering with covariates.

## History

Model-based clustering was first invented in 1950 by Paul Lazarsfeld for clustering multivariate discrete data, in the form of the latent class model.

In 1959, Lazarsfeld gave a lecture on latent structure analysis at the University of California-Berkeley, where John H. Wolfe was an M.A. student. This led Wolfe to think about how to do the same thing for continuous data, and in 1965 he did so, proposing the Gaussian mixture model for clustering. He also produced the first software for estimating it, called NORMIX. Day (1969), working independently, was the first to publish a journal article on the approach. However, Wolfe deserves credit as the inventor of model-based clustering for continuous data.

Murtagh and Raftery (1984) developed a model-based clustering method based on the eigenvalue decomposition of the component covariance matrices. McLachlan and Basford (1988) was the first book on the approach, advancing methodology and sparking interest. Banfield and Raftery (1993) coined the term "model-based clustering", introduced the family of parsimonious models, described an information criterion for choosing the number of clusters, proposed the uniform model for outliers, and introduced the mclust software. Celeux and Govaert (1995) showed how to perform maximum likelihood estimation for the models. Thus, by 1995 the core components of the methodology were in place, laying the groundwork for extensive development since then.
