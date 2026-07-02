---
title: "Principal component analysis (part 1/2)"
source: https://en.wikipedia.org/wiki/Principal_component_analysis
domain: singular-value-decomposition-deep
license: CC-BY-SA-4.0
tags: singular value decomposition, moore-penrose inverse, low-rank approximation, polar decomposition
fetched: 2026-07-02
part: 1/2
---

# Principal component analysis

**Principal component analysis** (**PCA**) is a linear dimensionality reduction technique with applications in exploratory data analysis, visualization and data preprocessing.

The data are linearly transformed onto a new coordinate system such that the directions (principal components) capturing the largest variation in the data can be easily identified.

The **principal components** of a collection of points in a real coordinate space are a sequence of p unit vectors, where the i -th vector is the direction of a line that best fits the data while being orthogonal to the first $i-1$ vectors. Here, a best-fitting line is defined as one that minimizes the average squared perpendicular distance from the points to the line. These directions (i.e., principal components) constitute an orthonormal basis in which different individual dimensions of the data are linearly uncorrelated. Many studies use the first two principal components in order to plot the data in two dimensions and to visually identify clusters of closely related data points.

Principal component analysis has applications in many fields such as population genetics, microbiome studies, and atmospheric science.


## Overview

When performing PCA, the first principal component of a set of p variables is the derived variable formed as a linear combination of the original variables that explains the most variance. The second principal component explains the most variance in what is left once the effect of the first component is removed, and we may proceed through p iterations until all the variance is explained. PCA is most commonly used when many of the variables are highly correlated with each other and it is desirable to reduce their number to an independent set. The first principal component can equivalently be defined as a direction that maximizes the variance of the projected data. The i -th principal component can be taken as a direction orthogonal to the first $i-1$ principal components that maximizes the variance of the projected data.

For either objective, it can be shown that the principal components are eigenvectors of the data's covariance matrix. Thus, the principal components are often computed by eigendecomposition of the data covariance matrix or singular value decomposition of the data matrix. PCA is the simplest of the true eigenvector-based multivariate analyses and is closely related to factor analysis. Factor analysis typically incorporates more domain-specific assumptions about the underlying structure and solves eigenvectors of a slightly different matrix. PCA is also related to canonical correlation analysis (CCA). CCA defines coordinate systems that optimally describe the cross-covariance between two datasets while PCA defines a new orthogonal coordinate system that optimally describes variance in a single dataset. Robust and L1-norm-based variants of standard PCA have also been proposed.


## History

PCA was invented in 1901 by Karl Pearson, as an analogue of the principal axis theorem in mechanics; it was later independently developed and named by Harold Hotelling in the 1930s. Depending on the field of application, it is also named the discrete Karhunen–Loève transform (KLT) in signal processing, the Hotelling transform in multivariate quality control, proper orthogonal decomposition (POD) in mechanical engineering, singular value decomposition (SVD) of **X** (invented in the last quarter of the 19th century), eigenvalue decomposition (EVD) of **X**T**X** in linear algebra, factor analysis (for a discussion of the differences between PCA and factor analysis see Ch. 7 of Jolliffe's *Principal Component Analysis*), Eckart–Young theorem (Harman, 1960), or empirical orthogonal functions (EOF) in meteorological science (Lorenz, 1956), empirical eigenfunction decomposition (Sirovich, 1987), quasiharmonic modes (Brooks et al., 1988), spectral decomposition in noise and vibration, and empirical modal analysis in structural dynamics.


## Intuition

PCA can be thought of as fitting a *p*-dimensional ellipsoid to the data, where each axis of the ellipsoid represents a principal component. If some axis of the ellipsoid is small, then the variance along that axis is also small.

To find the axes of the ellipsoid, we must first center the values of each variable in the dataset on 0 by subtracting the mean of the variable's observed values from each of those values. These transformed values are used instead of the original observed values for each of the variables. Then, we compute the covariance matrix of the data and calculate the eigenvalues and corresponding eigenvectors of this covariance matrix. Then we must normalize each of the orthogonal eigenvectors to turn them into unit vectors. Once this is done, each of the mutually-orthogonal unit eigenvectors can be interpreted as an axis of the ellipsoid fitted to the data. This choice of basis will transform the covariance matrix into a diagonalized form, in which the diagonal elements represent the variance of each axis. The proportion of the variance that each eigenvector represents can be calculated by dividing the eigenvalue corresponding to that eigenvector by the sum of all eigenvalues.

Biplots and scree plots (degree of explained variance) are used to interpret findings of the PCA.


## Details

PCA is defined as an orthogonal linear transformation on a real inner product space that transforms the data to a new coordinate system such that the greatest variance by some scalar projection of the data comes to lie on the first coordinate (called the first principal component), the second greatest variance on the second coordinate, and so on.

Consider an $n\times p$ data matrix, **X**, with column-wise zero empirical mean (the sample mean of each column has been shifted to zero), where each of the *n* rows represents a different repetition of the experiment, and each of the *p* columns gives a particular kind of feature (say, the results from a particular sensor).

Mathematically, the transformation is defined by a set of size l (where l is usually selected to be strictly less than p to reduce dimensionality) of p -dimensional vectors of weights or coefficients $\mathbf {w} _{(k)}=(w_{1},\dots ,w_{p})_{(k)}$ that map each row vector $\mathbf {x} _{(i)}=(x_{1},\dots ,x_{p})_{(i)}$ of **X** to a new vector of principal component *scores* $\mathbf {t} _{(i)}=(t_{1},\dots ,t_{l})_{(i)}$ , given by

${t_{k}}_{(i)}=\mathbf {x} _{(i)}\cdot \mathbf {w} _{(k)}\qquad \mathrm {for} \qquad i=1,\dots ,n\qquad k=1,\dots ,l$

in such a way that the individual variables $t_{1},\dots ,t_{l}$ of **t** considered over the data set successively inherit the maximum possible variance from **X**, with each coefficient vector **w** constrained to be a unit vector.

The above may equivalently be written in matrix form as

$\mathbf {T} =\mathbf {X} \mathbf {W}$

where ${\mathbf {T} }_{ik}={t_{k}}_{(i)}$ , ${\mathbf {X} }_{ij}={x_{j}}_{(i)}$ , and ${\mathbf {W} }_{jk}={w_{j}}_{(k)}$ .

### First component

In order to maximize variance, the first weight vector **w**(1) thus has to satisfy

$\mathbf {w} _{(1)}=\arg \max _{\Vert \mathbf {w} \Vert =1}\,\left\{\sum _{i}(t_{1})_{(i)}^{2}\right\}=\arg \max _{\Vert \mathbf {w} \Vert =1}\,\left\{\sum _{i}\left(\mathbf {x} _{(i)}\cdot \mathbf {w} \right)^{2}\right\}$

Equivalently, writing this in matrix form gives

$\mathbf {w} _{(1)}=\arg \max _{\left\|\mathbf {w} \right\|=1}\left\{\left\|\mathbf {Xw} \right\|^{2}\right\}=\arg \max _{\left\|\mathbf {w} \right\|=1}\left\{\mathbf {w} ^{\mathsf {T}}\mathbf {X} ^{\mathsf {T}}\mathbf {Xw} \right\}$

Since **w**(1) has been defined to be a unit vector, it equivalently also satisfies

$\mathbf {w} _{(1)}=\arg \max \left\{{\frac {\mathbf {w} ^{\mathsf {T}}\mathbf {X} ^{\mathsf {T}}\mathbf {Xw} }{\mathbf {w} ^{\mathsf {T}}\mathbf {w} }}\right\}$

The quantity to be maximised can be recognised as a Rayleigh quotient. A standard result for a positive semidefinite matrix such as **X**T**X** is that the quotient's maximum possible value is the largest eigenvalue of the matrix, which occurs when ***w*** is the corresponding eigenvector.

With **w**(1) found, the first principal component of a data vector **x**(*i*) can then be given as a score *t*1(*i*) = **x**(*i*) ⋅ **w**(1) in the transformed co-ordinates, or as the corresponding vector in the original variables, {**x**(*i*) ⋅ **w**(1)} **w**(1).

### Further components

The *k*-th component can be found by subtracting the first *k* − 1 principal components from **X**:

$\mathbf {\hat {X}} _{k}=\mathbf {X} -\sum _{s=1}^{k-1}\mathbf {X} \mathbf {w} _{(s)}\mathbf {w} _{(s)}^{\mathsf {T}}$

and then finding the weight vector which extracts the maximum variance from this new data matrix

$\mathbf {w} _{(k)}=\mathop {\operatorname {arg\,max} } _{\left\|\mathbf {w} \right\|=1}\left\{\left\|\mathbf {\hat {X}} _{k}\mathbf {w} \right\|^{2}\right\}=\arg \max \left\{{\tfrac {\mathbf {w} ^{\mathsf {T}}\mathbf {\hat {X}} _{k}^{\mathsf {T}}\mathbf {\hat {X}} _{k}\mathbf {w} }{\mathbf {w} ^{T}\mathbf {w} }}\right\}$

It turns out that this gives the remaining eigenvectors of **X**T**X**, with the maximum values for the quantity in brackets given by their corresponding eigenvalues. Thus the weight vectors are eigenvectors of **X**T**X**.

The *k*-th principal component of a data vector **x**(*i*) can therefore be given as a score *t**k*(*i*) = **x**(*i*) ⋅ **w**(*k*) in the transformed coordinates, or as the corresponding vector in the space of the original variables, {**x**(*i*) ⋅ **w**(*k*)} **w**(*k*), where **w**(*k*) is the *k*th eigenvector of **X**T**X**.

The full principal components decomposition of **X** can therefore be given as

$\mathbf {T} =\mathbf {X} \mathbf {W}$

where **W** is a *p*-by-*p* matrix of weights whose columns are the eigenvectors of **X**T**X**. The transpose of **W** is sometimes called the whitening or sphering transformation. Columns of **W** multiplied by the square root of corresponding eigenvalues, that is, eigenvectors scaled up by the variances, are called *loadings* in PCA or in Factor analysis.

### Covariances

**X**T**X** itself can be recognized as proportional to the empirical sample covariance matrix of the dataset **X**.

The sample covariance *Q* between two of the different principal components over the dataset is given by:

${\begin{aligned}Q(\mathrm {PC} _{(j)},\mathrm {PC} _{(k)})&\propto (\mathbf {X} \mathbf {w} _{(j)})^{\mathsf {T}}(\mathbf {X} \mathbf {w} _{(k)})\\&=\mathbf {w} _{(j)}^{\mathsf {T}}\mathbf {X} ^{\mathsf {T}}\mathbf {X} \mathbf {w} _{(k)}\\&=\mathbf {w} _{(j)}^{\mathsf {T}}\lambda _{(k)}\mathbf {w} _{(k)}\\&=\lambda _{(k)}\mathbf {w} _{(j)}^{\mathsf {T}}\mathbf {w} _{(k)}\end{aligned}}$

where the eigenvalue property of **w**(*k*) has been used to move from line 2 to line 3. However eigenvectors **w**(*j*) and **w**(*k*) corresponding to eigenvalues of a symmetric matrix are orthogonal (if the eigenvalues are different), or can be orthogonalised (if the vectors happen to share an equal repeated value). The product in the final line is therefore zero; there is no sample covariance between different principal components over the dataset.

Another way to characterise the principal components transformation is therefore as the transformation to coordinates which diagonalise the empirical sample covariance matrix.

In matrix form, the empirical covariance matrix for the original variables can be written

$\mathbf {Q} \propto \mathbf {X} ^{\mathsf {T}}\mathbf {X} =\mathbf {W} \mathbf {\Lambda } \mathbf {W} ^{\mathsf {T}}$

The empirical covariance matrix between the principal components becomes

$\mathbf {W} ^{\mathsf {T}}\mathbf {Q} \mathbf {W} \propto \mathbf {W} ^{\mathsf {T}}\mathbf {W} \,\mathbf {\Lambda } \,\mathbf {W} ^{\mathsf {T}}\mathbf {W} =\mathbf {\Lambda }$

where **Λ** is the diagonal matrix of eigenvalues *λ*(*k*) of **X**T**X**. *λ*(*k*) is equal to the sum of the squares over the dataset associated with each component *k*, that is, *λ*(*k*) = Σ*i* *t**k*2(*i*) = Σ*i* (**x**(*i*) ⋅ **w**(*k*))2.

### Dimensionality reduction

The transformation **P** = **X** **W** maps a data vector **x**(*i*) from an original space of *x* variables to a new space of *p* variables which are uncorrelated over the dataset. To non-dimensionalize the centered data, let *Xc* represent the characteristic values of data vectors *Xi*, given by:

- $\|X\|_{\infty }$ (maximum norm),
- ${\frac {1}{n}}\|X\|_{1}$ (mean absolute value), or
- ${\frac {1}{\sqrt {n}}}\|X\|_{2}$ (normalized Euclidean norm),

for a dataset of size *n*. These norms are used to transform the original space of variables *x, y* to a new space of uncorrelated variables *p, q* (given *Yc* with same meaning), such that $p_{i}={\frac {X_{i}}{X_{c}}},\quad q_{i}={\frac {Y_{i}}{Y_{c}}}$ ; and the new variables are linearly related as: $q=\alpha p$ . To find the optimal linear relationship, we minimize the total squared reconstruction error: $E(\alpha )={\frac {1}{1-\alpha ^{2}}}\sum _{i=1}^{n}(\alpha p_{i}-q_{i})^{2}$ ; such that setting the derivative of the error function to zero $(E'(\alpha )=0)$ yields: $\alpha ={\frac {1}{2}}\left(-\lambda \pm {\sqrt {\lambda ^{2}+4}}\right)$ where $\lambda ={\frac {p\cdot p-q\cdot q}{p\cdot q}}$ .

Such dimensionality reduction can be a very useful step for visualising and processing high-dimensional datasets, while still retaining as much of the variance in the dataset as possible. For example, selecting *L* = 2 and keeping only the first two principal components finds the two-dimensional plane through the high-dimensional dataset in which the data are most spread out, so if the data contains clusters these too may be most spread out, and therefore most visible to be plotted out in a two-dimensional diagram; whereas if two directions through the data (or two of the original variables) are chosen at random, the clusters may be much less spread apart from each other, and may in fact be much more likely to substantially overlay each other, making them indistinguishable.

Similarly, in regression analysis, the larger the number of explanatory variables allowed, the greater is the chance of overfitting the model, producing conclusions that fail to generalise to other datasets. One approach, especially when there are strong correlations between different possible explanatory variables, is to reduce them to a few principal components and then run the regression against them, a method called principal component regression.

Dimensionality reduction may also be appropriate when the variables in a dataset are noisy. If each column of the dataset contains independent identically distributed Gaussian noise, then the columns of **T** will also contain similarly identically distributed Gaussian noise (such a distribution is invariant under the effects of the matrix **W**, which can be thought of as a high-dimensional rotation of the co-ordinate axes). However, with more of the total variance concentrated in the first few principal components compared to the same noise variance, the proportionate effect of the noise is less—the first few components achieve a higher signal-to-noise ratio. PCA thus can have the effect of concentrating much of the signal into the first few principal components, which can usefully be captured by dimensionality reduction; while the later principal components may be dominated by noise, and so disposed of without great loss. If the dataset is not too large, the significance of the principal components can be tested using parametric bootstrap, as an aid in determining how many principal components to retain.

### Singular value decomposition

The principal components transformation can also be associated with another matrix factorization, the singular value decomposition (SVD) of **X**,

$\mathbf {X} =\mathbf {U} \mathbf {\Sigma } \mathbf {W} ^{T}$

Here **Σ** is an *n*-by-*p* rectangular diagonal matrix of positive numbers *σ*(*k*), called the singular values of **X**; **U** is an *n*-by-*n* matrix, the columns of which are orthogonal unit vectors of length *n* called the left singular vectors of **X**; and **W** is a *p*-by-*p* matrix whose columns are orthogonal unit vectors of length *p* and called the right singular vectors of **X**.

In terms of this factorization, the matrix **X**T**X** can be written

${\begin{aligned}\mathbf {X} ^{T}\mathbf {X} &=\mathbf {W} \mathbf {\Sigma } ^{\mathsf {T}}\mathbf {U} ^{\mathsf {T}}\mathbf {U} \mathbf {\Sigma } \mathbf {W} ^{\mathsf {T}}\\&=\mathbf {W} \mathbf {\Sigma } ^{\mathsf {T}}\mathbf {\Sigma } \mathbf {W} ^{\mathsf {T}}\\&=\mathbf {W} \mathbf {\hat {\Sigma }} ^{2}\mathbf {W} ^{\mathsf {T}}\end{aligned}}$

where **$\mathbf {\hat {\Sigma }}$** is the square diagonal matrix with the singular values of **X**and the excess zeros chopped off that satisfies**$\mathbf {{\hat {\Sigma }}^{2}} =\mathbf {\Sigma } ^{\mathsf {T}}\mathbf {\Sigma }$**. Comparison with the eigenvector factorization of **X**T**X** establishes that the right singular vectors **W** of **X** are equivalent to the eigenvectors of **X**T**X**, while the singular values *σ*(*k*) of **$\mathbf {X}$** are equal to the square-root of the eigenvalues *λ*(*k*) of **X**T**X**.

Using the singular value decomposition the score matrix **T** can be written

${\begin{aligned}\mathbf {T} &=\mathbf {X} \mathbf {W} \\&=\mathbf {U} \mathbf {\Sigma } \mathbf {W} ^{\mathsf {T}}\mathbf {W} \\&=\mathbf {U} \mathbf {\Sigma } \end{aligned}}$

so each column of **T** is given by one of the left singular vectors of **X** multiplied by the corresponding singular value. This form is also the polar decomposition of **T**.

Efficient algorithms exist to calculate the SVD of **X** without having to form the matrix **X**T**X**, so computing the SVD is now the standard way to calculate a principal components analysis from a data matrix, unless only a handful of components are required.

As with the eigen-decomposition, a truncated *n* × *L* score matrix **T**L can be obtained by considering only the first L largest singular values and their singular vectors:

$\mathbf {T} _{L}=\mathbf {U} _{L}\mathbf {\Sigma } _{L}=\mathbf {X} \mathbf {W} _{L}$

The truncation of a matrix **M** or **T** using a truncated singular value decomposition in this way produces a truncated matrix that is the nearest possible matrix of rank *L* to the original matrix, in the sense of the difference between the two having the smallest possible Frobenius norm, a result known as the Eckart–Young theorem [1936].

> **Theorem (Optimal k‑dimensional fit).** Let P be an n×m data matrix whose columns have been mean‑centered and scaled, and let $P=U\,\Sigma \,V^{T}$ be its singular value decomposition. Then the best rank‑k approximation to P in the least‑squares (Frobenius‑norm) sense is $P_{k}=U_{k}\,\Sigma _{k}\,V_{k}^{T}$ , where Vk consists of the first k columns of V. Moreover, the relative residual variance is $R(k)={\frac {\sum _{j=k+1}^{m}\sigma _{j}^{2}}{\sum _{j=1}^{m}\sigma _{j}^{2}}}$ .


## Further considerations

The singular values (in **Σ**) are the square roots of the eigenvalues of the matrix **X**T**X**. Each eigenvalue is proportional to the portion of the "variance" (more correctly of the sum of the squared distances of the points from their multidimensional mean) that is associated with each eigenvector. The sum of all the eigenvalues is equal to the sum of the squared distances of the points from their multidimensional mean. PCA essentially rotates the set of points around their mean in order to align with the principal components. This moves as much of the variance as possible (using an orthogonal transformation) into the first few dimensions. The values in the remaining dimensions, therefore, tend to be small and may be dropped with minimal loss of information (see below). PCA is often used in this manner for dimensionality reduction. PCA has the distinction of being the optimal orthogonal transformation for keeping the subspace that has largest "variance" (as defined above). This advantage, however, comes at the price of greater computational requirements if compared, for example, and when applicable, to the discrete cosine transform, and in particular to the DCT-II which is simply known as the "DCT". Nonlinear dimensionality reduction techniques tend to be more computationally demanding than PCA.

PCA is sensitive to the scaling of the variables. Mathematically this sensitivity comes from the way a rescaling changes the sample‑covariance matrix that PCA diagonalises.

Let $\mathbf {X} _{\text{c}}$ be the *centered* data matrix (*n* rows, *p* columns) and define the covariance $\Sigma ={\frac {1}{n}}\,\mathbf {X} _{\text{c}}^{\mathsf {T}}\mathbf {X} _{\text{c}}.$ If the j ‑th variable is multiplied by a factor $\alpha _{j}$ we obtain $\mathbf {X} _{\text{c}}^{(\alpha )}=\mathbf {X} _{\text{c}}D,\qquad D=\operatorname {diag} (\alpha _{1},\ldots ,\alpha _{p}).$ Hence the new covariance is $\Sigma ^{(\alpha )}=D^{\mathsf {T}}\,\Sigma \,D.$

Because the eigenvalues and eigenvectors of $\Sigma ^{(\alpha )}$ are those of $\Sigma$ scaled by D , the principal axes rotate toward any column whose variance has been inflated, exactly as the 2‑D example below illustrates.

If we have just two variables and they have the same sample variance and are completely correlated, then the PCA will entail a rotation by 45° and the "weights" (they are the cosines of rotation) for the two variables with respect to the principal component will be equal. But if we multiply all values of the first variable by 100, then the first principal component will be almost the same as that variable, with a small contribution from the other variable, whereas the second component will be almost aligned with the second original variable. This means that whenever the different variables have different units (like temperature and mass), PCA is a somewhat arbitrary method of analysis. (Different results would be obtained if one used Fahrenheit rather than Celsius for example.) Pearson's original paper was entitled "On Lines and Planes of Closest Fit to Systems of Points in Space" – "in space" implies physical Euclidean space where such concerns do not arise. One way of making the PCA less arbitrary is to use variables scaled so as to have unit variance, by standardizing the data and hence use the autocorrelation matrix instead of the autocovariance matrix as a basis for PCA. However, this compresses (or expands) the fluctuations in all dimensions of the signal space to unit variance.

Classical PCA assumes the cloud of points has already been translated so its centroid is at the origin.

Write each observation as $\mathbf {q} _{i}={\boldsymbol {\mu }}+\mathbf {z} _{i},\qquad {\boldsymbol {\mu }}={\tfrac {1}{n}}\sum _{i=1}^{n}\mathbf {q} _{i}.$

Without subtracting ${\boldsymbol {\mu }}$ we are in effect diagonalising

$\Sigma _{\text{unc}}\;=\;n\,{\boldsymbol {\mu }}{\boldsymbol {\mu }}^{\mathsf {T}}\;+\;{\tfrac {1}{n}}\,\mathbf {Z} ^{\mathsf {T}}\mathbf {Z} ,$

where $\mathbf {Z}$ is the centered matrix. The rank‑one term $n\,{\boldsymbol {\mu }}{\boldsymbol {\mu }}^{\mathsf {T}}$ often dominates, forcing the leading eigenvector to point almost exactly toward the mean and obliterating any structure in the centred part $\mathbf {Z}$ . After mean subtraction that term vanishes and the principal axes align with the true directions of maximal variance.

Mean-centering is unnecessary if performing a principal components analysis on a correlation matrix, as the data are already centered after calculating correlations. Correlations are derived from the cross-product of two standard scores (Z-scores) or statistical moments (hence the name: *Pearson Product-Moment Correlation*). Also see the article by Kromrey & Foster-Johnson (1998) on *"Mean-centering in Moderated Regression: Much Ado About Nothing"*. Since covariances are correlations of normalized variables (Z- or standard-scores) a PCA based on the correlation matrix of **X** is equal to a PCA based on the covariance matrix of **Z**, the standardized version of **X**.

PCA is a popular primary technique in pattern recognition. It is not, however, optimized for class separability. However, it has been used to quantify the distance between two or more classes by calculating center of mass for each class in principal component space and reporting Euclidean distance between center of mass of two or more classes. The linear discriminant analysis is an alternative which is optimized for class separability.


## Table of symbols and abbreviations

| Symbol | Meaning | Dimensions | Indices |
|---|---|---|---|
| $\mathbf {X} =[X_{ij}]$ | data matrix, consisting of the set of all data vectors, one vector per row | $n\times p$ | $i=1\ldots n$ $j=1\ldots p$ |
| n | the number of row vectors in the data set | $1\times 1$ | *scalar* |
| p | the number of elements in each row vector (dimension) | $1\times 1$ | *scalar* |
| L | the number of dimensions in the dimensionally reduced subspace, $1\leq L\leq p$ | $1\times 1$ | *scalar* |
| $\mathbf {u} =[u_{j}]$ | vector of empirical means, one mean for each column *j* of the data matrix | $p\times 1$ | $j=1\ldots p$ |
| $\mathbf {s} =[s_{j}]$ | vector of empirical standard deviations, one standard deviation for each column *j* of the data matrix | $p\times 1$ | $j=1\ldots p$ |
| $\mathbf {h} =[h_{i}]$ | vector of all 1's | $1\times n$ | $i=1\ldots n$ |
| $\mathbf {B} =[B_{ij}]$ | deviations from the mean of each column *j* of the data matrix | $n\times p$ | $i=1\ldots n$ $j=1\ldots p$ |
| $\mathbf {Z} =[Z_{ij}]$ | z-scores, computed using the mean and standard deviation for each column *j* of the data matrix | $n\times p$ | $i=1\ldots n$ $j=1\ldots p$ |
| $\mathbf {C} =[C_{jj'}]$ | covariance matrix | $p\times p$ | $j=1\ldots p$ $j'=1\ldots p$ |
| $\mathbf {R} =[R_{jj'}]$ | correlation matrix | $p\times p$ | $j=1\ldots p$ $j'=1\ldots p$ |
| $\mathbf {V} =[V_{jj'}]$ | matrix consisting of the set of all eigenvectors of **C**, one eigenvector per column | $p\times p$ | $j=1\ldots p$ $j'=1\ldots p$ |
| $\mathbf {D} =[D_{jj'}]$ | diagonal matrix consisting of the set of all eigenvalues of **C** along its principal diagonal, and 0 for all other elements ( note $\mathbf {\Lambda }$ used above ) | $p\times p$ | $j=1\ldots p$ $j'=1\ldots p$ |
| $\mathbf {W} =[W_{jl}]$ | matrix of basis vectors, one vector per column, where each basis vector is one of the eigenvectors of **C**, and where the vectors in **W** are a sub-set of those in **V** | $p\times L$ | $j=1\ldots p$ $l=1\ldots L$ |
| $\mathbf {T} =[T_{il}]$ | matrix consisting of *n* row vectors, where each vector is the projection of the corresponding data vector from matrix **X** onto the basis vectors contained in the columns of matrix **W**. | $n\times L$ | $i=1\ldots n$ $l=1\ldots L$ |


## Properties and limitations

### Properties

Some properties of PCA include:

Property 1

:

For any integer

q

, 1 ≤

q

≤

p

, consider the orthogonal

linear transformation

$y=\mathbf {B'} x$

where

y

is a

q-element

vector and

$\mathbf {B'}$

is a (

q

×

p

) matrix, and let

$\mathbf {\Sigma } _{y}=\mathbf {B'} \mathbf {\Sigma } \mathbf {B}$

be the

variance

-

covariance

matrix for

y

. Then the trace of

$\mathbf {\Sigma } _{y}$

, denoted

$\operatorname {tr} (\mathbf {\Sigma } _{y})$

, is maximized by taking

$\mathbf {B} =\mathbf {A} _{q}$

, where

$\mathbf {A} _{q}$

consists of the first

q

columns of

$\mathbf {A}$

$(\mathbf {B'}$

is the transpose of

$\mathbf {B} )$

. (

$\mathbf {A}$

is not defined here)

Property 2

:

Consider again the

orthonormal transformation

$y=\mathbf {B'} x$

with

$x,\mathbf {B} ,\mathbf {A}$

and

$\mathbf {\Sigma } _{y}$

defined as before. Then

$\operatorname {tr} (\mathbf {\Sigma } _{y})$

is minimized by taking

$\mathbf {B} =\mathbf {A} _{q}^{*},$

where

$\mathbf {A} _{q}^{*}$

consists of the last

q

columns of

$\mathbf {A}$

.

The statistical implication of this property is that the last few PCs are not simply unstructured left-overs after removing the important PCs. Because these last PCs have variances as small as possible they are useful in their own right. They can help to detect unsuspected near-constant linear relationships between the elements of x, and they may also be useful in regression, in selecting a subset of variables from x, and in outlier detection.

Property 3

:

(Spectral decomposition of

Σ

)

$\mathbf {\Sigma } =\lambda _{1}\alpha _{1}\alpha _{1}'+\cdots +\lambda _{p}\alpha _{p}\alpha _{p}'$

Before we look at its usage, we first look at diagonal elements,

$\operatorname {Var} (x_{j})=\sum _{k=1}^{P}\lambda _{k}\alpha _{kj}^{2}$

Then, perhaps the main statistical implication of the result is that not only can we decompose the combined variances of all the elements of x into decreasing contributions due to each PC, but we can also decompose the whole covariance matrix into contributions $\lambda _{k}\alpha _{k}\alpha _{k}'$ from each PC. Although not strictly decreasing, the elements of $\lambda _{k}\alpha _{k}\alpha _{k}'$ will tend to become smaller as k increases, as $\lambda _{k}\alpha _{k}\alpha _{k}'$ is nonincreasing for increasing k , whereas the elements of $\alpha _{k}$ tend to stay about the same size because of the normalization constraints: $\alpha _{k}'\alpha _{k}=1,k=1,\dots ,p$ .

### Limitations

As noted above, the results of PCA depend on the scaling of the variables. This can be cured by scaling each feature by its standard deviation, so that one ends up with dimensionless features with unital variance.

The applicability of PCA as described above is limited by certain (tacit) assumptions made in its derivation. In particular, PCA can capture linear correlations between the features but fails when this assumption is violated (see Figure 6a in the reference). In some cases, coordinate transformations can restore the linearity assumption and PCA can then be applied (see kernel PCA).

Another limitation is the mean-removal process before constructing the covariance matrix for PCA. In fields such as astronomy, all the signals are non-negative, and the mean-removal process will force the mean of some astrophysical exposures to be zero, which consequently creates unphysical negative fluxes, and forward modeling has to be performed to recover the true magnitude of the signals. As an alternative method, non-negative matrix factorization focusing only on the non-negative elements in the matrices is well-suited for astrophysical observations. See more at the relation between PCA and non-negative matrix factorization.

PCA is at a disadvantage if the data has not been standardized before applying the algorithm to it. PCA transforms the original data into data that is relevant to the principal components of that data, which means that the new data variables cannot be interpreted in the same ways that the originals were. They are linear interpretations of the original variables. Also, if PCA is not performed properly, there is a high likelihood of information loss.

PCA relies on a linear model. If a dataset has a pattern hidden inside it that is nonlinear, then PCA can actually steer the analysis in the complete opposite direction of progress. Researchers at Kansas State University discovered that the sampling error in their experiments impacted the bias of PCA results. "If the number of subjects or blocks is smaller than 30, and/or the researcher is interested in PC's beyond the first, it may be better to first correct for the serial correlation, before PCA is conducted". The researchers at Kansas State also found that PCA could be "seriously biased if the autocorrelation structure of the data are not correctly handled".

### PCA and information theory

Dimensionality reduction results in a loss of information, in general. PCA-based dimensionality reduction tends to minimize that information loss, under certain signal and noise models.

Under the assumption that

$\mathbf {x} =\mathbf {s} +\mathbf {n} ,$

that is, that the data vector $\mathbf {x}$ is the sum of the desired information-bearing signal $\mathbf {s}$ and a noise signal $\mathbf {n}$ one can show that PCA can be optimal for dimensionality reduction, from an information-theoretic point-of-view.

In particular, Linsker showed that if $\mathbf {s}$ is Gaussian and $\mathbf {n}$ is Gaussian noise with a covariance matrix proportional to the identity matrix, the PCA maximizes the mutual information $I(\mathbf {y} ;\mathbf {s} )$ between the desired information $\mathbf {s}$ and the dimensionality-reduced output $\mathbf {y} =\mathbf {W} _{L}^{T}\mathbf {x}$ .

If the noise is still Gaussian and has a covariance matrix proportional to the identity matrix (that is, the components of the vector $\mathbf {n}$ are iid), but the information-bearing signal $\mathbf {s}$ is non-Gaussian (which is a common scenario), PCA at least minimizes an upper bound on the *information loss*, which is defined as

$I(\mathbf {x} ;\mathbf {s} )-I(\mathbf {y} ;\mathbf {s} ).$

The optimality of PCA is also preserved if the noise $\mathbf {n}$ is iid and at least more Gaussian (in terms of the Kullback–Leibler divergence) than the information-bearing signal $\mathbf {s}$ . In general, even if the above signal model holds, PCA loses its information-theoretic optimality as soon as the noise $\mathbf {n}$ becomes dependent.


## Computation using the covariance method

The following is a detailed description of PCA using the covariance method as opposed to the correlation method.

The goal is to transform a given data set **X** of dimension *p* to an alternative data set **Y** of smaller dimension *L*. Equivalently, we are seeking to find the matrix **Y**, where **Y** is the Karhunen–Loève transform (KLT) of matrix **X**:

$\mathbf {Y} =\mathbb {KLT} \{\mathbf {X} \}$

1. **Organize the data set** Suppose you have data comprising a set of observations of *p* variables, and you want to reduce the data so that each observation can be described with only *L* variables, *L* < *p*. Suppose further, that the data are arranged as a set of *n* data vectors $\mathbf {x} _{1}\ldots \mathbf {x} _{n}$ with each $\mathbf {x} _{i}$ representing a single grouped observation of the *p* variables.
  - Write $\mathbf {x} _{1}\ldots \mathbf {x} _{n}$ as row vectors, each with *p* elements.
  - Place the row vectors into a single matrix **X** of dimensions *n* × *p*.
2. **Calculate the empirical mean**
  - Find the empirical mean along each column *j* = 1, ..., *p*.
  - Place the calculated mean values into an empirical mean vector **u** of dimensions *p* × 1. $u_{j}={\frac {1}{n}}\sum _{i=1}^{n}X_{ij}$
3. **Calculate the deviations from the mean** Mean subtraction is an integral part of the solution towards finding a principal component basis that minimizes the mean square error of approximating the data. Hence we proceed by centering the data as follows: In some applications, each variable (column of **B**) may also be scaled to have a variance equal to 1 (see Z-score). This step affects the calculated principal components, but makes them independent of the units used to measure the different variables.
  - Subtract the empirical mean vector $\mathbf {u} ^{T}$ from each row of the data matrix **X**.
  - Store mean-subtracted data in the *n* × *p* matrix **B**. $\mathbf {B} =\mathbf {X} -\mathbf {h} \mathbf {u} ^{T}$ where **h** is an *n* × 1 column vector of all 1s: $h_{i}=1\,\qquad \qquad {\text{for }}i=1,\ldots ,n$
4. **Find the covariance matrix**
  - Find the *p* × *p* empirical covariance matrix **C** from matrix **B**: $\mathbf {C} ={1 \over {n-1}}\mathbf {B} ^{*}\mathbf {B}$ where * is the conjugate transpose operator. If **B** consists entirely of real numbers, which is the case in many applications, the "conjugate transpose" is the same as the regular transpose.
  - The reasoning behind using *n* − 1 instead of *n* to calculate the covariance is Bessel's correction.
5. **Find the eigenvectors and eigenvalues of the covariance matrix**
  - Compute the matrix **V** of eigenvectors which diagonalizes the covariance matrix **C**: $\mathbf {V} ^{-1}\mathbf {C} \mathbf {V} =\mathbf {D}$ where **D** is the diagonal matrix of eigenvalues of **C**. This step will typically involve the use of a computer-based algorithm for computing eigenvectors and eigenvalues. These algorithms are readily available as sub-components of most matrix algebra systems, such as SAS, R, MATLAB, Mathematica, SciPy, IDL (Interactive Data Language), or GNU Octave as well as OpenCV.
  - Matrix **D** will take the form of an *p* × *p* diagonal matrix, where $D_{k\ell }=\lambda _{k}\qquad {\text{for }}k=\ell$ is the *j*th eigenvalue of the covariance matrix **C**, and $D_{k\ell }=0\qquad {\text{for }}k\neq \ell .$
  - Matrix **V**, also of dimension *p* × *p*, contains *p* column vectors, each of length *p*, which represent the *p* eigenvectors of the covariance matrix **C**.
  - The eigenvalues and eigenvectors are ordered and paired. The *j*th eigenvalue corresponds to the *j*th eigenvector.
  - Matrix **V** denotes the matrix of *right* eigenvectors (as opposed to *left* eigenvectors). In general, the matrix of right eigenvectors need *not* be the (conjugate) transpose of the matrix of left eigenvectors.
6. **Rearrange the eigenvectors and eigenvalues**
  - Sort the columns of the eigenvector matrix **V** and eigenvalue matrix **D** in order of *decreasing* eigenvalue.
  - Make sure to maintain the correct pairings between the columns in each matrix.
7. **Compute the cumulative energy content for each eigenvector**
  - The eigenvalues represent the distribution of the source data's energy among each of the eigenvectors, where the eigenvectors form a basis for the data. The cumulative energy content *g* for the *j*th eigenvector is the sum of the energy content across all of the eigenvalues from 1 through *j* divided by the sum of energy content across all eigenvalues (shown in step 8): $g_{j}=\sum _{k=1}^{j}D_{kk}\qquad {\text{for }}j=1,\dots ,p$
8. **Select a subset of the eigenvectors as basis vectors**
  - Save the first *L* columns of **V** as the *p* × *L* matrix **W**: $W_{kl}=V_{k\ell }\qquad {\text{for }}k=1,\dots ,p\qquad \ell =1,\dots ,L$ where $1\leq L\leq p.$
  - Use the vector **g** as a guide in choosing an appropriate value for *L*. The goal is to choose a value of *L* as small as possible while achieving a reasonably high value of *g* on a percentage basis. For example, you may want to choose *L* so that the cumulative energy *g* is above a certain threshold, like 90 percent. In this case, choose the smallest value of *L* such that ${\frac {g_{L}}{g_{p}}}\geq 0.9$
9. **Project the data onto the new basis** That is, the first column of $\mathbf {T}$ is the projection of the data points onto the first principal component, the second column is the projection onto the second principal component, etc.
  - The projected data points are the rows of the matrix $\mathbf {T} =\mathbf {B} \cdot \mathbf {W}$


## Derivation using the covariance method

Let **X** be a *d*-dimensional random vector expressed as column vector. Without loss of generality, assume **X** has zero mean.

We want to find $(\ast )$ a *d* × *d* orthonormal transformation matrix **P** so that **PX** has a diagonal covariance matrix (that is, **PX** is a random vector with all its distinct components pairwise uncorrelated).

A quick computation assuming P were unitary yields:

${\begin{aligned}\operatorname {cov} (PX)&=\operatorname {E} [PX~(PX)^{*}]\\&=\operatorname {E} [PX~X^{*}P^{*}]\\&=P\operatorname {E} [XX^{*}]P^{*}\\&=P\operatorname {cov} (X)P^{-1}\\\end{aligned}}$

Hence $(\ast )$ holds if and only if $\operatorname {cov} (X)$ were diagonalisable by P .

This is very constructive, as cov(**X**) is guaranteed to be a non-negative definite matrix and thus is guaranteed to be diagonalisable by some unitary matrix.


## Covariance-free computation

In practical implementations, especially with high dimensional data (large p), the naive covariance method is rarely used because it is not efficient due to high computational and memory costs of explicitly determining the covariance matrix. The covariance-free approach avoids the *np*2 operations of explicitly calculating and storing the covariance matrix **XTX**, instead utilizing one of matrix-free methods, for example, based on the function evaluating the product **XT(X r)** at the cost of 2*np* operations.

### Iterative computation

One way to compute the first principal component efficiently is shown in the following pseudo-code, for a data matrix **X** with zero mean, without ever computing its covariance matrix.

```
r = a random vector of length p
r = r / norm(r)
do c times:
      s = 0 (a vector of length p)
      for each row x in X
            s = s + (x ⋅ r) x
      λ = rTs // λ is the eigenvalue
      error = |λ ⋅ r − s|
      r = s / norm(s)
      exit if error < tolerance
return λ, r
```

This power iteration algorithm simply calculates the vector **XT(X r)**, normalizes, and places the result back in **r**. The eigenvalue is approximated by **rT (XTX) r**, which is the Rayleigh quotient on the unit vector **r** for the covariance matrix **XTX**. If the largest singular value is well separated from the next largest one, the vector **r** gets close to the first principal component of **X** within the number of iterations c, which is small relative to p, at the total cost *2cnp*. The power iteration convergence can be accelerated without noticeably sacrificing the small cost per iteration using more advanced matrix-free methods, such as the Lanczos algorithm or the Locally Optimal Block Preconditioned Conjugate Gradient (LOBPCG) method.

Subsequent principal components can be computed one-by-one via deflation or simultaneously as a block. In the former approach, imprecisions in already computed approximate principal components additively affect the accuracy of the subsequently computed principal components, thus increasing the error with every new computation. The latter approach in the block power method replaces single-vectors **r** and **s** with block-vectors, matrices **R** and **S**. Every column of **R** approximates one of the leading principal components, while all columns are iterated simultaneously. The main calculation is evaluation of the product **XT(X R)**. Implemented, for example, in LOBPCG, efficient blocking eliminates the accumulation of the errors, allows using high-level BLAS matrix-matrix product functions, and typically leads to faster convergence, compared to the single-vector one-by-one technique.

### The NIPALS method

*Non-linear iterative partial least squares (NIPALS)* is a variant the classical power iteration with matrix deflation by subtraction implemented for computing the first few components in a principal component or partial least squares analysis. For very-high-dimensional datasets, such as those generated in the *omics sciences (for example, genomics, metabolomics) it is usually only necessary to compute the first few PCs. The non-linear iterative partial least squares (NIPALS) algorithm updates iterative approximations to the leading scores and loadings **t**1 and **r**1T by the power iteration multiplying on every iteration by **X** on the left and on the right, that is, calculation of the covariance matrix is avoided, just as in the matrix-free implementation of the power iterations to **XTX**, based on the function evaluating the product **XT(X r)** = **((X r)TX)T**.

The matrix deflation by subtraction is performed by subtracting the outer product, **t**1**r**1T from **X** leaving the deflated residual matrix used to calculate the subsequent leading PCs. For large data matrices, or matrices that have a high degree of column collinearity, NIPALS suffers from loss of orthogonality of PCs due to machine precision round-off errors accumulated in each iteration and matrix deflation by subtraction. A Gram–Schmidt re-orthogonalization algorithm is applied to both the scores and the loadings at each iteration step to eliminate this loss of orthogonality. NIPALS reliance on single-vector multiplications cannot take advantage of high-level BLAS and results in slow convergence for clustered leading singular values—both these deficiencies are resolved in more sophisticated matrix-free block solvers, such as the Locally Optimal Block Preconditioned Conjugate Gradient (LOBPCG) method.

### Online/sequential estimation

In an "online" or "streaming" situation with data arriving piece by piece rather than being stored in a single batch, it is useful to make an estimate of the PCA projection that can be updated sequentially. This can be done efficiently, but requires different algorithms.


## Qualitative variables

In exploratory data analysis, qualitative (categorical) variables not used to construct the model can be projected onto the principal component axes as supplementary elements. The use of supplementary qualitative variables was a defining feature of the French school of data analysis developed in the 1960s and 70s. Based upon the work of Ludovic Lebart, the method is available in the R environment through packages such as FactoMineR.
