---
title: "Principal component analysis (part 2/2)"
source: https://en.wikipedia.org/wiki/Principal_component_analysis
domain: singular-value-decomposition-deep
license: CC-BY-SA-4.0
tags: singular value decomposition, moore-penrose inverse, low-rank approximation, polar decomposition
fetched: 2026-07-02
part: 2/2
---

## Applications

### Intelligence

The earliest application of factor analysis was in locating and measuring components of human intelligence. It was believed that intelligence had various uncorrelated components such as spatial intelligence, verbal intelligence, induction, deduction etc and that scores on these could be adduced by factor analysis from results on various tests, to give a single index known as the Intelligence Quotient (IQ). The pioneering statistical psychologist Spearman actually developed factor analysis in 1904 for his two-factor theory of intelligence, adding a formal technique to the science of psychometrics. In 1924 Thurstone looked for 56 factors of intelligence, developing the notion of Mental Age. Standard IQ tests today are based on this early work.

### Residential differentiation

In 1949, Shevky and Williams introduced the theory of **factorial ecology**, which dominated studies of residential differentiation from the 1950s to the 1970s. Neighbourhoods in a city were recognizable or could be distinguished from one another by various characteristics which could be reduced to three by factor analysis. These were known as 'social rank' (an index of occupational status), 'familism' or family size, and 'ethnicity'; Cluster analysis could then be applied to divide the city into clusters or precincts according to values of the three key factor variables. An extensive literature developed around factorial ecology in urban geography, but the approach went out of fashion after 1980 as being methodologically primitive and having little place in postmodern geographical paradigms.

One of the problems with factor analysis has always been finding convincing names for the various artificial factors. In 2000, Flood revived the factorial ecology approach to show that principal components analysis actually gave meaningful answers directly, without resorting to factor rotation. The principal components were actually dual variables or shadow prices of 'forces' pushing people together or apart in cities. The first component was 'accessibility', the classic trade-off between demand for travel and demand for space, around which classical urban economics is based. The next two components were 'disadvantage', which keeps people of similar status in separate neighbourhoods (mediated by planning), and ethnicity, where people of similar ethnic backgrounds try to co-locate.

About the same time, the Australian Bureau of Statistics defined distinct indexes of advantage and disadvantage taking the first principal component of sets of key variables that were thought to be important. These SEIFA indexes are regularly published for various jurisdictions, and are used frequently in spatial analysis.

### Development indexes

PCA can be used as a formal method for the development of indexes. As an alternative confirmatory composite analysis has been proposed to develop and assess indexes.

The City Development Index was developed by PCA from about 200 indicators of city outcomes in a 1996 survey of 254 global cities. The first principal component was subject to iterative regression, adding the original variables singly until about 90% of its variation was accounted for. The index ultimately used about 15 indicators but was a good predictor of many more variables. Its comparative value agreed very well with a subjective assessment of the condition of each city. The coefficients on items of infrastructure were roughly proportional to the average costs of providing the underlying services, suggesting the Index was actually a measure of effective physical and social investment in the city.

The country-level Human Development Index (HDI) from UNDP, which has been published since 1990 and is very extensively used in development studies, has very similar coefficients on similar indicators, strongly suggesting it was originally constructed using PCA.

### Population genetics

In 1978 Cavalli-Sforza and others pioneered the use of principal components analysis (PCA) to summarise data on variation in human gene frequencies across regions. The components showed distinctive patterns, including gradients and sinusoidal waves. They interpreted these patterns as resulting from specific ancient migration events.

Since then, PCA has been ubiquitous in population genetics, with thousands of papers using PCA as a display mechanism. Genetics varies largely according to proximity, so the first two principal components actually show spatial distribution and may be used to map the relative geographical location of different population groups, thereby showing individuals who have wandered from their original locations.

PCA in genetics has been technically controversial, in that the technique has been performed on discrete non-normal variables and often on binary allele markers. The lack of any measures of standard error in PCA are also an impediment to more consistent usage. In August 2022, the molecular biologist Eran Elhaik published a theoretical paper in Scientific Reports analyzing 12 PCA applications. He concluded that it was easy to manipulate the method, which, in his view, generated results that were 'erroneous, contradictory, and absurd.' Specifically, he argued, the results achieved in population genetics were characterized by cherry-picking and circular reasoning.

### Market research and indexes of attitude

Market research has been an extensive user of PCA. It is used to develop customer satisfaction or customer loyalty scores for products, and with clustering, to develop market segments that may be targeted with advertising campaigns, in much the same way as factorial ecology will locate geographical areas with similar characteristics.

PCA rapidly transforms large amounts of data into smaller, easier-to-digest variables that can be more rapidly and readily analyzed. In any consumer questionnaire, there are series of questions designed to elicit consumer attitudes, and principal components seek out latent variables underlying these attitudes. For example, the Oxford Internet Survey in 2013 asked 2000 people about their attitudes and beliefs, and from these analysts extracted four principal component dimensions, which they identified as 'escape', 'social networking', 'efficiency', and 'problem creating'.

Another example from Joe Flood in 2008 extracted an attitudinal index toward housing from 28 attitude questions in a national survey of 2697 households in Australia. The first principal component represented a general attitude toward property and home ownership. The index, or the attitude questions it embodied, could be fed into a General Linear Model of tenure choice. The strongest determinant of private renting by far was the attitude index, rather than income, marital status or household type.

### Quantitative finance

In quantitative finance, PCA is used in financial risk management, and has been applied to other problems such as portfolio optimization.

PCA is commonly used in problems involving fixed income securities and portfolios, and interest rate derivatives. Valuations here depend on the entire yield curve, comprising numerous highly correlated instruments, and PCA is used to define a set of components or factors that explain rate movements, thereby facilitating the modelling. One common risk management application is to calculating value at risk, VaR, applying PCA to the Monte Carlo simulation. Here, for each simulation-sample, the components are stressed, and rates, and in turn option values, are then reconstructed; with VaR calculated, finally, over the entire run. PCA is also used in hedging exposure to interest rate risk, given partial durations and other sensitivities. Under both, the first three, typically, principal components of the system are of interest (representing "shift", "twist", and "curvature"). These principal components are derived from an eigen-decomposition of the covariance matrix of yield at predefined maturities; and where the variance of each component is its eigenvalue (and as the components are orthogonal, no correlation need be incorporated in subsequent modelling).

For equity, an optimal portfolio is one where the expected return is maximized for a given level of risk, or alternatively, where risk is minimized for a given return; see Markowitz model for discussion. Thus, one approach is to reduce portfolio risk, where allocation strategies are applied to the "principal portfolios" instead of the underlying stocks. A second approach is to enhance portfolio return, using the principal components to select companies' stocks with upside potential. PCA has also been used to understand relationships between international equity markets, and within markets between groups of companies in industries or sectors.

PCA may also be applied to stress testing, essentially an analysis of a bank's ability to endure a hypothetical adverse economic scenario. Its utility is in "distilling the information contained in [several] macroeconomic variables into a more manageable data set, which can then [be used] for analysis." Here, the resulting factors are linked to e.g. interest rates – based on the largest elements of the factor's eigenvector – and it is then observed how a "shock" to each of the factors affects the implied assets of each of the banks.

### Neuroscience

A variant of principal components analysis is used in neuroscience to identify the specific properties of a stimulus that increases a neuron's probability of generating an action potential. This technique is known as spike-triggered covariance analysis. In a typical application an experimenter presents a white noise process as a stimulus (usually either as a sensory input to a test subject, or as a current injected directly into the neuron) and records a train of action potentials, or spikes, produced by the neuron as a result. Presumably, certain features of the stimulus make the neuron more likely to spike. In order to extract these features, the experimenter calculates the covariance matrix of the *spike-triggered ensemble*, the set of all stimuli (defined and discretized over a finite time window, typically on the order of 100 ms) that immediately preceded a spike. The eigenvectors of the difference between the spike-triggered covariance matrix and the covariance matrix of the *prior stimulus ensemble* (the set of all stimuli, defined over the same length time window) then indicate the directions in the space of stimuli along which the variance of the spike-triggered ensemble differed the most from that of the prior stimulus ensemble. Specifically, the eigenvectors with the largest positive eigenvalues correspond to the directions along which the variance of the spike-triggered ensemble showed the largest positive change compared to the variance of the prior. Since these were the directions in which varying the stimulus led to a spike, they are often good approximations of the sought after relevant stimulus features.

In neuroscience, PCA is also used to discern the identity of a neuron from the shape of its action potential. Spike sorting is an important procedure because extracellular recording techniques often pick up signals from more than one neuron. In spike sorting, one first uses PCA to reduce the dimensionality of the space of action potential waveforms, and then performs clustering analysis to associate specific action potentials with individual neurons.

PCA as a dimension reduction technique is particularly suited to detect coordinated activities of large neuronal ensembles. It has been used in determining collective variables, that is, order parameters, during phase transitions in the brain.


## Relation with other methods

### Correspondence analysis

Correspondence analysis (CA) was developed by Jean-Paul Benzécri and is conceptually similar to PCA, but scales the data (which should be non-negative) so that rows and columns are treated equivalently. It is traditionally applied to contingency tables. CA decomposes the chi-squared statistic associated to this table into orthogonal factors. Because CA is a descriptive technique, it can be applied to tables for which the chi-squared statistic is appropriate or not. Several variants of CA are available including detrended correspondence analysis and canonical correspondence analysis. One special extension is multiple correspondence analysis, which may be seen as the counterpart of principal component analysis for categorical data.

### Factor analysis

Principal component analysis creates variables that are linear combinations of the original variables. The new variables have the property that the variables are all orthogonal. The PCA transformation can be helpful as a pre-processing step before clustering. PCA is a variance-focused approach seeking to reproduce the total variable variance, in which components reflect both common and unique variance of the variable. PCA is generally preferred for purposes of data reduction (that is, translating variable space into optimal factor space) but not when the goal is to detect the latent construct or factors.

Factor analysis is similar to principal component analysis, in that factor analysis also involves linear combinations of variables. Different from PCA, factor analysis is a correlation-focused approach seeking to reproduce the inter-correlations among variables, in which the factors "represent the common variance of variables, excluding unique variance". In terms of the correlation matrix, this corresponds with focusing on explaining the off-diagonal terms (that is, shared co-variance), while PCA focuses on explaining the terms that sit on the diagonal. However, as a side result, when trying to reproduce the on-diagonal terms, PCA also tends to fit relatively well the off-diagonal correlations. Results given by PCA and factor analysis are very similar in most situations, but this is not always the case, and there are some problems where the results are significantly different. Factor analysis is generally used when the research purpose is detecting data structure (that is, latent constructs or factors) or causal modeling. If the factor model is incorrectly formulated or the assumptions are not met, then factor analysis will give erroneous results.

### *K*-means clustering

It has been asserted that the relaxed solution of *k*-means clustering, specified by the cluster indicators, is given by the principal components, and the PCA subspace spanned by the principal directions is identical to the cluster centroid subspace. However, that PCA is a useful relaxation of *k*-means clustering was not a new result, and it is straightforward to uncover counterexamples to the statement that the cluster centroid subspace is spanned by the principal directions.

### Non-negative matrix factorization

Non-negative matrix factorization (NMF) is a dimension reduction method where only non-negative elements in the matrices are used, which is therefore a promising method in astronomy, in the sense that astrophysical signals are non-negative. The PCA components are orthogonal to each other, while the NMF components are all non-negative and therefore constructs a non-orthogonal basis.

In PCA, the contribution of each component is ranked based on the magnitude of its corresponding eigenvalue, which is equivalent to the fractional residual variance (FRV) in analyzing empirical data. For NMF, its components are ranked based only on the empirical FRV curves. The residual fractional eigenvalue plots, that is, $1-\sum _{i=1}^{k}\lambda _{i}{\Big /}\sum _{j=1}^{n}\lambda _{j}$ as a function of component number k given a total of n components, for PCA have a flat plateau, where no data are captured to remove the quasi-static noise, then the curves drop quickly as an indication of over-fitting (random noise). The FRV curves for NMF is decreasing continuously when the NMF components are constructed sequentially, indicating the continuous capturing of quasi-static noise; then converge to higher levels than PCA, indicating the less over-fitting property of NMF.

### Iconography of correlations

It is often difficult to interpret the principal components when the data include many variables of various origins, or when some variables are qualitative. This leads the PCA user to a delicate elimination of several variables. If observations or variables have an excessive impact on the direction of the axes, they should be removed and then projected as supplementary elements. In addition, it is necessary to avoid interpreting the proximities between the points close to the center of the factorial plane.

The iconography of correlations, on the contrary, which is not a projection on a system of axes, does not have these drawbacks. We can therefore keep all the variables.

The principle of the diagram is to underline the "remarkable" correlations of the correlation matrix, by a solid line (positive correlation) or dotted line (negative correlation).

A strong correlation is not "remarkable" if it is not direct, but caused by the effect of a third variable. Conversely, weak correlations can be "remarkable". For example, if a variable Y depends on several independent variables, the correlations of Y with each of them are weak and yet "remarkable".


## Generalizations

### Sparse PCA

A particular disadvantage of PCA is that the principal components are usually linear combinations of all input variables. Sparse PCA overcomes this disadvantage by finding linear combinations that contain just a few input variables. It extends the classic method of principal component analysis (PCA) for the reduction of dimensionality of data by adding sparsity constraint on the input variables. Several approaches have been proposed, including

- a regression framework,
- a convex relaxation/semidefinite programming framework,
- a generalized power method framework
- an alternating maximization framework
- forward-backward greedy search and exact methods using branch-and-bound techniques,
- Bayesian formulation framework.

The methodological and theoretical developments of Sparse PCA as well as its applications in scientific studies were recently reviewed in a survey paper.

### Nonlinear PCA

Most of the modern methods for nonlinear dimensionality reduction find their theoretical and algorithmic roots in PCA or K-means. Pearson's original idea was to take a straight line (or plane) which will be "the best fit" to a set of data points. Trevor Hastie expanded on this concept by proposing **Principal curves** as the natural extension for the geometric interpretation of PCA, which explicitly constructs a manifold for data approximation followed by projecting the points onto it. See also the elastic map algorithm and principal geodesic analysis. Another popular generalization is kernel PCA, which corresponds to PCA performed in a reproducing kernel Hilbert space associated with a positive definite kernel.

In multilinear subspace learning, PCA is generalized to multilinear PCA (MPCA) that extracts features directly from tensor representations. MPCA is solved by performing PCA in each mode of the tensor iteratively. MPCA has been applied to face recognition, gait recognition, etc. MPCA is further extended to uncorrelated MPCA, non-negative MPCA and robust MPCA.

*N*-way principal component analysis may be performed with models such as Tucker decomposition, PARAFAC, multiple factor analysis, co-inertia analysis, STATIS, and DISTATIS.

### Robust PCA

While PCA finds the mathematically optimal method (as in minimizing the squared error), it is still sensitive to outliers in the data that produce large errors, something that the method tries to avoid in the first place. It is therefore common practice to remove outliers before computing PCA. However, in some contexts, outliers can be difficult to identify. For example, in data mining algorithms like correlation clustering, the assignment of points to clusters and outliers is not known beforehand. A recently proposed generalization of PCA based on a weighted PCA increases robustness by assigning different weights to data objects based on their estimated relevancy.

Outlier-resistant variants of PCA have also been proposed, based on L1-norm formulations (L1-PCA).

Robust principal component analysis (RPCA) via decomposition in low-rank and sparse matrices is a modification of PCA that works well with respect to grossly corrupted observations.


## Similar techniques

### Independent component analysis

Independent component analysis (ICA) is directed to similar problems as principal component analysis, but finds additively separable components rather than successive approximations.

### Network component analysis

Given a matrix E , it tries to decompose it into two matrices such that $E=AP$ . A key difference from techniques such as PCA and ICA is that some of the entries of A are constrained to be 0. Here P is termed the regulatory layer. While in general such a decomposition can have multiple solutions, they prove that if the following conditions are satisfied :

1. A has full column rank
2. Each column of A must have at least $L-1$ zeroes where L is the number of columns of A (or alternatively the number of rows of P ). The justification for this criterion is that if a node is removed from the regulatory layer along with all the output nodes connected to it, the result must still be characterized by a connectivity matrix with full column rank.
3. P must have full row rank.

then the decomposition is unique up to multiplication by a scalar.

### Discriminant analysis of principal components

Discriminant analysis of principal components (DAPC) is a multivariate method used to identify and describe clusters of genetically related individuals. Genetic variation is partitioned into two components: variation between groups and within groups, and it maximizes the former. Linear discriminants are linear combinations of alleles which best separate the clusters. Alleles that most contribute to this discrimination are therefore those that are the most markedly different across groups. The contributions of alleles to the groupings identified by DAPC can allow identifying regions of the genome driving the genetic divergence among groups In DAPC, data are first transformed using a principal components analysis (PCA) and subsequently clusters are identified using discriminant analysis (DA).

A DAPC can be realized on R using the package Adegenet. (more info: adegenet on the web)

### Directional component analysis

Directional component analysis (DCA) is a method used in the atmospheric sciences for analysing multivariate datasets. Like PCA, it allows for dimension reduction, improved visualization and improved interpretability of large data-sets. Also like PCA, it is based on a covariance matrix derived from the input dataset. The difference between PCA and DCA is that DCA additionally requires the input of a vector direction, referred to as the impact. Whereas PCA maximises explained variance, DCA maximises probability density given impact. The motivation for DCA is to find components of a multivariate dataset that are both likely (measured using probability density) and important (measured using the impact). DCA has been used to find the most likely and most serious heat-wave patterns in weather prediction ensembles , and the most likely and most impactful changes in rainfall due to climate change .


## Software/source code

- ALGLIB – a C++ and C# library that implements PCA and truncated PCA
- Analytica – The built-in EigenDecomp function computes principal components.
- ELKI – includes PCA for projection, including robust variants of PCA, as well as PCA-based clustering algorithms.
- Gretl – principal component analysis can be performed either via the `pca` command or via the `princomp()` function.
- Julia – Supports PCA with the `pca` function in the MultivariateStats package.
- KNIME – A java based nodal arranging software for Analysis, in this the nodes called PCA, PCA compute, PCA Apply, PCA inverse make it easily.
- Maple (software) – The PCA command is used to perform a principal component analysis on a set of data.
- Mathematica – Implements principal component analysis with the PrincipalComponents command using both covariance and correlation methods.
- MathPHP – PHP mathematics library with support for PCA.
- MATLAB – The SVD function is part of the basic system. In the Statistics Toolbox, the functions `princomp` and `pca` (R2012b) give the principal components, while the function `pcares` gives the residuals and reconstructed matrix for a low-rank PCA approximation.
- Matplotlib – a Python library that has a PCA package in the .mlab module.
- mlpack – Provides an implementation of principal component analysis in C++.
- mrmath – A high performance math library for Delphi and FreePascal can perform PCA; including robust variants.
- NAG Library – Principal components analysis is implemented via the `g03aa` routine (available in both the Fortran versions of the Library).
- NMath – Proprietary numerical library containing PCA for the .NET Framework.
- GNU Octave – Free software computational environment mostly compatible with MATLAB, the function `princomp` gives the principal component.
- OpenCV
- Oracle Database 12c – Implemented via `DBMS_DATA_MINING.SVDS_SCORING_MODE` by specifying setting value `SVDS_SCORING_PCA`.
- Orange (software) – Integrates PCA in its visual programming environment. PCA displays a scree plot (degree of explained variance) where user can interactively select the number of principal components.
- Origin – Contains PCA in its Pro version.
- Qlucore – Commercial software for analyzing multivariate data with instant response using PCA.
- R – Free statistical package, the functions `princomp` and `prcomp` can be used for principal component analysis; `prcomp` uses singular value decomposition which generally gives better numerical accuracy. Some packages that implement PCA in R, include, but are not limited to: `ade4`, `vegan`, `ExPosition`, `dimRed`, and `FactoMineR`.
- SAS – Proprietary software; for example, see.
- scikit-learn – Python library for machine learning which contains PCA, Probabilistic PCA, Kernel PCA, Sparse PCA and other techniques in the decomposition module.
- Scilab – Free and open-source, cross-platform numerical computational package, the function `princomp` computes principal component analysis, the function `pca` computes principal component analysis with standardized variables.
- SPSS – Proprietary software most commonly used by social scientists for PCA, factor analysis and associated cluster analysis.
- Weka – Java library for machine learning which contains modules for computing principal components.
