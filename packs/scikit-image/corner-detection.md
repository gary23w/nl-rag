---
title: "Corner detection"
source: https://en.wikipedia.org/wiki/Corner_detection
domain: scikit-image
license: BSD-3-Clause
tags: scikit-image library, image segmentation, edge detection, mathematical morphology
fetched: 2026-07-02
---

# Corner detection

**Corner detection** is an approach used within computer vision systems to extract certain kinds of features and infer the contents of an image. Corner detection is frequently used in motion detection, image registration, video tracking, image mosaicing, panorama stitching, 3D reconstruction and object recognition. Corner detection overlaps with the topic of **interest point detection**.

## Formalization

A corner can be defined as the intersection of two edges. A corner can also be defined as a point for which there are two dominant and different edge directions in a local neighbourhood of the point.

An interest point is a point in an image which has a well-defined position and can be robustly detected. This means that an interest point can be a corner but it can also be, for example, an isolated point of local intensity maximum or minimum, line endings, or a point on a curve where the curvature is locally maximal.

In practice, most so-called corner detection methods detect interest points in general, and in fact, the term "corner" and "interest point" are used more or less interchangeably through the literature. As a consequence, if only corners are to be detected it is necessary to do a local analysis of detected interest points to determine which of these are real corners. Examples of edge detection that can be used with post-processing to detect corners are the Kirsch operator and the Frei-Chen masking set.

"Corner", "interest point" and "feature" are used interchangeably in literature, confusing the issue. Specifically, there are several blob detectors that can be referred to as "interest point operators", but which are sometimes erroneously referred to as "corner detectors". Moreover, there exists a notion of ridge detection to capture the presence of elongated objects.

Corner detectors are not usually very robust and often require large redundancies introduced to prevent the effect of individual errors from dominating the recognition task.

One determination of the quality of a corner detector is its ability to detect the same corner in multiple similar images, under conditions of different lighting, translation, rotation and other transforms.

A simple approach to corner detection in images is using correlation, but this gets very computationally expensive and suboptimal. An alternative approach used frequently is based on a method proposed by Harris and Stephens (below), which in turn is an improvement of a method by Moravec.

## Moravec corner detection algorithm

This is one of the earliest corner detection algorithms and defines a *corner* to be a point with low self-similarity. The algorithm tests each pixel in the image to see whether a corner is present by considering how similar a patch centered on the pixel is to nearby, largely overlapping patches. The similarity is measured by taking the sum of squared differences (SSD) between the corresponding pixels of two patches. A lower number indicates more similarity.

If the pixel is in a region of uniform intensity, then the nearby patches will look similar. If the pixel is on an edge, then nearby patches in a direction perpendicular to the edge will look quite different, but nearby patches in a direction parallel to the edge will result in only a small change. If the pixel is on a feature with variation in all directions, then none of the nearby patches will look similar.

The corner strength is defined as the smallest SSD between the patch and its neighbours (horizontal, vertical and on the two diagonals). The reason is that if this number is high, then the variation along all shifts is either equal to it or larger than it, so capturing that all nearby patches look different.

If the corner strength number is computed for all locations, that it is locally maximal for one location indicates that a feature of interest is present in it.

As pointed out by Moravec, one of the main problems with this operator is that it is not isotropic: if an edge is present that is not in the direction of the neighbours (horizontal, vertical, or diagonal), then the smallest SSD will be large and the edge will be incorrectly chosen as an interest point.

## The Harris & Stephens / Shi–Tomasi corner detection algorithms

Harris and Stephens improved upon Moravec's corner detector by considering the differential of the corner score with respect to direction directly, instead of using shifted patches. (This corner score is often referred to as autocorrelation, since the term is used in the paper in which this detector is described. However, the mathematics in the paper clearly indicate that the sum of squared differences is used.)

Without loss of generality, we will assume a grayscale 2-dimensional image is used. Let this image be given by I . Consider taking an image patch over the area $(u,v)$ and shifting it by $(x,y)$ . The weighted *sum of squared differences* (SSD) between these two patches, denoted S , is given by $S(x,y)=\sum _{u}\sum _{v}w(u,v)[I(u+x,v+y)-I(u,v)]^{2}.$ $I(u+x,v+y)$ can be approximated by a Taylor expansion. Let $I_{x}$ and $I_{y}$ be the partial derivatives of I , such that $I(u+x,v+y)\approx I(u,v)+I_{x}(u,v)x+I_{y}(u,v)y.$

This produces the approximation $S(x,y)\approx \sum _{u}\sum _{v}w(u,v)[I_{x}(u,v)x+I_{y}(u,v)y]^{2},$ which can be written in matrix form: $S(x,y)\approx {\begin{bmatrix}x&y\end{bmatrix}}A{\begin{bmatrix}x\\y\end{bmatrix}},$ where *A* is the structure tensor, $A=\sum _{u}\sum _{v}w(u,v){\begin{bmatrix}I_{x}(u,v)^{2}&I_{x}(u,v)I_{y}(u,v)\\I_{x}(u,v)I_{y}(u,v)&I_{y}(u,v)^{2}\end{bmatrix}}={\begin{bmatrix}\langle I_{x}^{2}\rangle &\langle I_{x}I_{y}\rangle \\\langle I_{x}I_{y}\rangle &\langle I_{y}^{2}\rangle \end{bmatrix}}.$

In words, we find the covariance of the partial derivative of the image intensity I with respect to the x and y axes.

Angle brackets denote averaging (i.e. summation over $(u,v)$ ), and $w(u,v)$ denotes the type of window that slides over the image. If a box filter is used, the response will be anisotropic, but if a Gaussian is used, then the response will be isotropic.

A corner (or in general an interest point) is characterized by a large variation of S in all directions of the vector ${\begin{bmatrix}x&y\end{bmatrix}}$ . By analyzing the eigenvalues of A , this characterization can be expressed in the following way: A should have two "large" eigenvalues for an interest point. Based on the magnitudes of the eigenvalues, the following inferences can be made based on this argument:

1. If $\lambda _{1}\approx 0$ and $\lambda _{2}\approx 0,$ then this pixel $(x,y)$ has no features of interest.
2. If $\lambda _{1}\approx 0$ and $\lambda _{2}$ has some large positive value, then an edge is found.
3. If $\lambda _{1}$ and $\lambda _{2}$ have large positive values, then a corner is found.

Harris and Stephens note that exact computation of the eigenvalues is computationally expensive, since it requires the computation of a square root, and instead suggest the function $M_{c}=\lambda _{1}\lambda _{2}-\kappa (\lambda _{1}+\lambda _{2})^{2}=\det(A)-\kappa \operatorname {tr} ^{2}(A),$ where $\kappa$ is a tunable sensitivity parameter.

Therefore, the algorithm does not have to actually compute the eigenvalue decomposition of the matrix $A,$ and instead it is sufficient to evaluate the determinant and trace of A to find corners, or rather interest points in general.

The Shi–Tomasi corner detector directly computes $\min(\lambda _{1},\lambda _{2})$ because under certain assumptions, the corners are more stable for tracking. Note that this method is also sometimes referred to as the Kanade–Tomasi corner detector.

The value of $\kappa$ has to be determined empirically, and in the literature values in the range 0.04–0.15 have been reported as feasible.

One can avoid setting the parameter $\kappa$ by using Noble's corner measure $M_{c}'$ which amounts to the harmonic mean of the eigenvalues: $M_{c}'=2{\frac {\det(A)}{\operatorname {tr} (A)+\epsilon }},$ where $\epsilon$ is a small positive constant.

If A can be interpreted as the precision matrix for the corner position, the covariance matrix for the corner position is $A^{-1}$ , i.e. ${\frac {1}{\langle I_{x}^{2}\rangle \langle I_{y}^{2}\rangle -\langle I_{x}I_{y}\rangle ^{2}}}{\begin{bmatrix}\langle I_{y}^{2}\rangle &-\langle I_{x}I_{y}\rangle \\-\langle I_{x}I_{y}\rangle &\langle I_{x}^{2}\rangle \end{bmatrix}}.$

The sum of the eigenvalues of $A^{-1}$ , which in that case can be interpreted as a generalized variance (or a "total uncertainty") of the corner position, is related to Noble's corner measure $M_{c}'$ as $\lambda _{1}(A^{-1})+\lambda _{2}(A^{-1})={\frac {\operatorname {tr} (A)}{\det(A)}}\approx {\frac {2}{M_{c}'}}.$

## The Förstner corner detector

In some cases, one may wish to compute the location of a corner with subpixel accuracy. To achieve an approximate solution, the Förstner algorithm solves for the point closest to all the tangent lines of the corner in a given window and is a least-square solution. The algorithm relies on the fact that for an ideal corner, tangent lines cross at a single point.

The equation of a tangent line $T_{\mathbf {x} '}(\mathbf {x} )$ at pixel $\mathbf {x} '$ is given by:

$T_{\mathbf {x'} }(\mathbf {x} )=\nabla I(\mathbf {x'} )^{\top }(\mathbf {x} -\mathbf {x'} )=0$

where $\nabla I(\mathbf {x'} )={\begin{bmatrix}I_{\mathbf {x} }&I_{\mathbf {y} }\end{bmatrix}}^{\top }$ is the gradient vector of the image I at $\mathbf {x'}$ .

The point $\mathbf {x} _{0}$ closest to all the tangent lines in the window N is:

$\mathbf {x} _{0}={\underset {\mathbf {x} \in \mathbb {R} ^{2\times 1}}{\operatorname {argmin} }}\int _{\mathbf {x'} \in N}T_{\mathbf {x'} }(\mathbf {x} )^{2}d\mathbf {x'}$

The distance from $\mathbf {x} _{0}$ to the tangent lines $T_{\mathbf {x'} }$ is weighted by the gradient magnitude, thus giving more importance to tangents passing through pixels with strong gradients.

Solving for $\mathbf {x} _{0}$ :

${\begin{aligned}\mathbf {x} _{0}&={\underset {\mathbf {x} \in \mathbb {R} ^{2\times 1}}{\operatorname {argmin} }}\int _{\mathbf {x'} \in N}\left(\nabla I\left(\mathbf {x'} \right)^{\top }\left(\mathbf {x} -\mathbf {x'} \right)\right)^{2}d\mathbf {x'} \\&={\underset {\mathbf {x} \in \mathbb {R} ^{2\times 1}}{\operatorname {argmin} }}\int _{\mathbf {x'} \in N}(\mathbf {x} -\mathbf {x'} )^{\top }\nabla I(\mathbf {x'} )\nabla I(\mathbf {x'} )^{\top }(\mathbf {x} -\mathbf {x'} )d\mathbf {x'} \\&={\underset {\mathbf {x} \in \mathbb {R} ^{2\times 1}}{\operatorname {argmin} }}\left(\mathbf {x} ^{\top }A\mathbf {x} -2\mathbf {x} ^{\top }\mathbf {b} +c\right)\end{aligned}}$

$A\in \mathbb {R} ^{2\times 2},{\textbf {b}}\in \mathbb {R} ^{2\times 1},c\in \mathbb {R}$ are defined as:

${\begin{aligned}A&=\int \nabla I(\mathbf {x'} )\nabla I(\mathbf {x'} )^{\top }d\mathbf {x'} \\\mathbf {b} &=\int \nabla I(\mathbf {x'} )\nabla I(\mathbf {x'} )^{\top }\mathbf {x'} d\mathbf {x'} \\c&=\int \mathbf {x'} ^{\top }\nabla I(\mathbf {x'} )\nabla I(\mathbf {x'} )^{\top }\mathbf {x'} d\mathbf {x'} \\\end{aligned}}$

Minimizing this equation can be done by differentiating with respect to x and setting it equal to 0:

$2A\mathbf {x} -2\mathbf {b} =0\Rightarrow A\mathbf {x} =\mathbf {b}$

Note that $A\in \mathbb {R} ^{2\times 2}$ is the structure tensor. For the equation to have a solution, A must be invertible, which implies that A must be full rank (rank 2). Thus, the solution

$x_{0}=A^{-1}\mathbf {b}$

only exists where an actual corner exists in the window N .

A methodology for performing *automatic scale selection* for this corner localization method has been presented by Lindeberg by minimizing the normalized residual

${\tilde {d}}_{\min }={\frac {c-b^{T}A^{-1}b}{\operatorname {trace} A}}$

over scales. Thereby, the method has the ability to automatically adapt the scale levels for computing the image gradients to the noise level in the image data, by choosing coarser scale levels for noisy image data and finer scale levels for near ideal corner-like structures.

Notes:

- c can be viewed as a residual in the least-square solution computation: if $c=0$ , then there was no error.
- this algorithm can be modified to compute centers of circular features by changing tangent lines to normal lines.

## The multi-scale Harris operator

The computation of the second moment matrix (sometimes also referred to as the structure tensor) A in the Harris operator, requires the computation of image derivatives $I_{x},I_{y}$ in the image domain as well as the summation of non-linear combinations of these derivatives over local neighbourhoods. Since the computation of derivatives usually involves a stage of scale-space smoothing, an operational definition of the Harris operator requires two scale parameters: (i) a *local scale* for smoothing prior to the computation of image derivatives, and (ii) an *integration scale* for accumulating the non-linear operations on derivative operators into an integrated image descriptor.

With I denoting the original image intensity, let L denote the scale space representation of I obtained by convolution with a Gaussian kernel

$g(x,y,t)={\frac {1}{2{\pi }t}}e^{-\left(x^{2}+y^{2}\right)/2t}$

with local scale parameter t :

$L(x,y,t)\ =g(x,y,t)*I(x,y)$

and let $L_{x}=\partial _{x}L$ and $L_{y}=\partial _{y}L$ denote the partial derivatives of L . Moreover, introduce a Gaussian window function $g(x,y,s)$ with integration scale parameter s . Then, the *multi-scale second-moment matrix* can be defined as

$\mu (x,y;t,s)=\int _{\xi =-\infty }^{\infty }\int _{\eta =-\infty }^{\infty }{\begin{bmatrix}L_{x}^{2}(x-\xi ,y-\eta ;t)&L_{x}(x-\xi ,y-\eta ;t)\,L_{y}(x-\xi ,y-\eta ;t)\\L_{x}(x-\xi ,y-\eta ;t)\,L_{y}(x-\xi ,y-\eta ;t)&L_{y}^{2}(x-\xi ,y-\eta ;t)\end{bmatrix}}g(\xi ,\eta ;s)\,d\xi \,d\eta .$

Then, we can compute eigenvalues of $\mu$ in a similar way as the eigenvalues of A and define the *multi-scale Harris corner measure* as

$M_{c}(x,y;t,s)=\det(\mu (x,y;t,s))-\kappa \,\operatorname {trace} ^{2}(\mu (x,y;t,s)).$

Concerning the choice of the local scale parameter t and the integration scale parameter s , these scale parameters are usually coupled by a relative integration scale parameter $\gamma$ such that $s=\gamma ^{2}t$ , where $\gamma$ is usually chosen in the interval $[1,2]$ . Thus, we can compute the multi-scale Harris corner measure $M_{c}(x,y;t,\gamma ^{2}t)$ at any scale t in scale-space to obtain a multi-scale corner detector, which responds to corner structures of varying sizes in the image domain.

In practice, this multi-scale corner detector is often complemented by a *scale selection step*, where the scale-normalized Laplacian operator

$\nabla _{\mathrm {norm} }^{2}L(x,y;t)\ =t\nabla ^{2}L(x,y,t)=t(L_{xx}(x,y,t)+L_{yy}(x,y,t))$

is computed at every scale in scale-space and *scale adapted corner points with automatic scale selection* (the "Harris-Laplace operator") are computed from the points that are simultaneously:

- spatial maxima of the multi-scale corner measure $M_{c}(x,y;t,\gamma ^{2}t)$ $({\hat {x}},{\hat {y}};t)=\operatorname {argmaxlocal} _{(x,y)}M_{c}\left(x,y;t,\gamma ^{2}t\right)$
- local maxima or minima over scales of the scale-normalized Laplacian operator $\nabla _{\mathrm {norm} }^{2}(x,y,t)$ : ${\hat {t}}=\operatorname {argmaxminlocal} _{t}\nabla _{\mathrm {norm} }^{2}L({\hat {x}},{\hat {y}};t)$

## The level curve curvature approach

An earlier approach to corner detection is to detect points where the curvature of level curves and the gradient magnitude are *simultaneously* high. A differential way to detect such points is by computing *the rescaled level curve curvature* (the product of the level curve curvature and the gradient magnitude raised to the power of three)

${\tilde {\kappa }}(x,y;t)=L_{x}^{2}L_{yy}+L_{y}^{2}L_{xx}-2L_{x}L_{y}L_{xy}$

and to detect positive maxima and negative minima of this differential expression at some scale t in the scale space representation L of the original image. A main problem when computing the rescaled level curve curvature entity at a single scale however, is that it may be sensitive to noise and to the choice of the scale level. A better method is to compute the *$\gamma$ -normalized rescaled level curve curvature*

${\tilde {\kappa }}_{\mathrm {norm} }(x,y;t)=t^{2\gamma }(L_{x}^{2}L_{yy}+L_{y}^{2}L_{xx}-2L_{x}L_{y}L_{xy})$

with $\gamma =7/8$ and to detect *signed scale-space extrema* of this expression, that are points and scales that are positive maxima and negative minima with respect to both space and scale

$({\hat {x}},{\hat {y}};{\hat {t}})=\operatorname {argminmaxlocal} _{(x,y;t)}{\tilde {\kappa }}_{\mathrm {norm} }(x,y;t)$

in combination with a complementary localization step to handle the increase in localization error at coarser scales. In this way, larger scale values will be associated with rounded corners of large spatial extent while smaller scale values will be associated with sharp corners with small spatial extent. This approach is the first corner detector with automatic scale selection (prior to the "Harris-Laplace operator" above) and has been used for tracking corners under large scale variations in the image domain and for matching corner responses to edges to compute structural image features for geon-based object recognition.

## Laplacian of Gaussian, differences of Gaussians and determinant of the Hessian scale-space interest points

LoG is an acronym standing for *Laplacian of Gaussian*, DoG is an acronym standing for *difference of Gaussians* (DoG is an approximation of LoG), and DoH is an acronym standing for *determinant of the Hessian*. These scale-invariant interest points are all extracted by detecting scale-space extrema of scale-normalized differential expressions, i.e., points in scale-space where the corresponding scale-normalized differential expressions assume local extrema with respect to both space and scale

$({\hat {x}},{\hat {y}};{\hat {t}})=\operatorname {argminmaxlocal} _{(x,y;t)}(D_{\mathrm {norm} }L)(x,y;t)$

where $D_{norm}L$ denotes the appropriate scale-normalized differential entity (defined below).

These detectors are more completely described in blob detection. The scale-normalized Laplacian of the Gaussian and difference-of-Gaussian features (Lindeberg 1994, 1998; Lowe 2004)

${\begin{aligned}\nabla _{\mathrm {norm} }^{2}L(x,y;t)&=t\,(L_{xx}+L_{yy})\\&\approx {\frac {t\left(L(x,y;t+\Delta t)-L(x,y;t)\right)}{\Delta t}}\end{aligned}}$

do not necessarily make highly selective features, since these operators may also lead to responses near edges. To improve the corner detection ability of the differences of Gaussians detector, the feature detector used in the SIFT system therefore uses an additional post-processing stage, where the eigenvalues of the Hessian of the image at the detection scale are examined in a similar way as in the Harris operator. If the ratio of the eigenvalues is too high, then the local image is regarded as too edge-like, so the feature is rejected. Also Lindeberg's Laplacian of the Gaussian feature detector can be defined to comprise complementary thresholding on a complementary differential invariant to suppress responses near edges.

The scale-normalized determinant of the Hessian operator (Lindeberg 1994, 1998)

$\det H_{\mathrm {norm} }L=t^{2}(L_{xx}L_{yy}-L_{xy}^{2})$

is on the other hand highly selective to well localized image features and does only respond when there are significant grey-level variations in two image directions and is in this and other respects a better interest point detector than the Laplacian of the Gaussian. The determinant of the Hessian is an affine covariant differential expression and has better scale selection properties under affine image transformations than the Laplacian operator (Lindeberg 2013, 2015). Experimentally this implies that determinant of the Hessian interest points have better repeatability properties under local image deformation than Laplacian interest points, which in turns leads to better performance of image-based matching in terms higher efficiency scores and lower 1−precision scores.

The scale selection properties, affine transformation properties and experimental properties of these and other scale-space interest point detectors are analyzed in detail in (Lindeberg 2013, 2015).

## Scale-space interest points based on the Lindeberg Hessian feature strength measures

Inspired by the structurally similar properties of the Hessian matrix $Hf$ of a function f and the second-moment matrix (structure tensor) $\mu$ , as can e.g. be manifested in terms of their similar transformation properties under affine image deformations

$(Hf')=A^{-T}\,(Hf)\,A^{-1}$

,

$\mu '=A^{-T}\,\mu \,A^{-1}$

,

Lindeberg (2013, 2015) proposed to define four feature strength measures from the Hessian matrix in related ways as the Harris and Shi-and-Tomasi operators are defined from the structure tensor (second-moment matrix). Specifically, he defined the following unsigned and signed Hessian feature strength measures:

- the unsigned Hessian feature strength measure I: $D_{1,\mathrm {norm} }L={\begin{cases}t^{2}\,(\det HL-k\,\operatorname {trace} ^{2}HL)&{\mbox{if}}\,\det HL-k\,\operatorname {trace} ^{2}HL>0\\0&{\mbox{otherwise}}\end{cases}}$
- the signed Hessian feature strength measure I: ${\tilde {D}}_{1,\mathrm {norm} }L={\begin{cases}t^{2}\,(\det HL-k\,\operatorname {trace} ^{2}HL)&{\mbox{if}}\,\det HL-k\,\operatorname {trace} ^{2}HL>0\\t^{2}\,(\det HL+k\,\operatorname {trace} ^{2}HL)&{\mbox{if}}\,\det HL+k\,\operatorname {trace} ^{2}HL<0\\0&{\mbox{otherwise}}\end{cases}}$
- the unsigned Hessian feature strength measure II: $D_{2,\mathrm {norm} }L=t\,\min(|\lambda _{1}(HL)|,|\lambda _{2}(HL)|)$
- the signed Hessian feature strength measure II: ${\tilde {D}}_{2,\mathrm {norm} }L={\begin{cases}t\,\lambda _{1}(HL)&{\mbox{if}}\,|\lambda _{1}(HL)|<|\lambda _{2}(HL)|\\t\,\lambda _{2}(HL)&{\mbox{if}}\,|\lambda _{2}(HL)|<|\lambda _{1}(HL)|\\t\,(\lambda _{1}(HL)+\lambda _{2}(HL))/2&{\mbox{otherwise}}\end{cases}}$

where $\operatorname {trace} HL=L_{xx}+L_{yy}$ and $\det HL=L_{xx}L_{yy}-L_{xy}^{2}$ denote the trace and the determinant of the Hessian matrix $HL$ of the scale-space representation L at any scale t , whereas

$\lambda _{1}(HL)=L_{pp}={\frac {1}{2}}\left(L_{xx}+L_{yy}-{\sqrt {(L_{xx}-L_{yy})^{2}+4L_{xy}^{2}}}\right)$

$\lambda _{2}(HL)=L_{qq}={\frac {1}{2}}\left(L_{xx}+L_{yy}+{\sqrt {(L_{xx}-L_{yy})^{2}+4L_{xy}^{2}}}\right)$

denote the eigenvalues of the Hessian matrix.

The unsigned Hessian feature strength measure $D_{1,\mathrm {norm} }L$ responds to local extrema by positive values and is not sensitive to saddle points, whereas the signed Hessian feature strength measure ${\tilde {D}}_{1,\mathrm {norm} }L$ does additionally respond to saddle points by negative values. The unsigned Hessian feature strength measure $D_{2,\mathrm {norm} }L$ is insensitive to the local polarity of the signal, whereas the signed Hessian feature strength measure ${\tilde {D}}_{2,\mathrm {norm} }L$ responds to the local polarity of the signal by the sign of its output.

In Lindeberg (2015) these four differential entities were combined with local scale selection based on either scale-space extrema detection

$({\hat {x}},{\hat {y}};{\hat {t}})=\operatorname {argminmaxlocal} _{(x,y;t)}(D_{\mathrm {norm} }L)(x,y;t)$

or scale linking. Furthermore, the signed and unsigned Hessian feature strength measures $D_{2,\mathrm {norm} }L$ and ${\tilde {D}}_{2,\mathrm {norm} }L$ were combined with complementary thresholding on $D_{1,\mathrm {norm} }L>0$ .

By experiments on image matching under scaling transformations on a poster dataset with 12 posters with multi-view matching over scaling transformations up to a scaling factor of 6 and viewing direction variations up to a slant angle of 45 degrees with local image descriptors defined from reformulations of the pure image descriptors in the SIFT and SURF operators to image measurements in terms of Gaussian derivative operators (Gauss-SIFT and Gauss-SURF) instead of original SIFT as defined from an image pyramid or original SURF as defined from Haar wavelets, it was shown that scale-space interest point detection based on the unsigned Hessian feature strength measure $D_{1,\mathrm {norm} }L$ allowed for the best performance and better performance than scale-space interest points obtained from the determinant of the Hessian $\det H_{\mathrm {norm} }L=t^{2}\left(L_{xx}L_{yy}-L_{xy}^{2}\right)$ . Both the unsigned Hessian feature strength measure $D_{1,\mathrm {norm} }L$ , the signed Hessian feature strength measure ${\tilde {D}}_{1,norm}L$ and the determinant of the Hessian $\det H_{norm}L$ allowed for better performance than the Laplacian of the Gaussian $\nabla _{\mathrm {norm} }^{2}L=t\,(L_{xx}+L_{yy})$ . When combined with scale linking and complementary thresholding on $D_{1,\mathrm {norm} }L>0$ , the signed Hessian feature strength measure ${\tilde {D}}_{2,\mathrm {norm} }L$ did additionally allow for better performance than the Laplacian of the Gaussian $\nabla _{\mathrm {norm} }^{2}L$ .

Furthermore, it was shown that all these differential scale-space interest point detectors defined from the Hessian matrix allow for the detection of a larger number of interest points and better matching performance compared to the Harris and Shi-and-Tomasi operators defined from the structure tensor (second-moment matrix).

A theoretical analysis of the scale selection properties of these four Hessian feature strength measures and other differential entities for detecting scale-space interest points, including the Laplacian of the Gaussian and the determinant of the Hessian, is given in Lindeberg (2013) and an analysis of their affine transformation properties as well as experimental properties in Lindeberg (2015).

## Affine-adapted interest point operators

The interest points obtained from the multi-scale Harris operator with automatic scale selection are invariant to translations, rotations and uniform rescalings in the spatial domain. The images that constitute the input to a computer vision system are, however, also subject to perspective distortions. To obtain an interest point operator that is more robust to perspective transformations, a natural approach is to devise a feature detector that is *invariant to affine transformations*. In practice, affine invariant interest points can be obtained by applying affine shape adaptation where the shape of the smoothing kernel is iteratively warped to match the local image structure around the interest point or equivalently a local image patch is iteratively warped while the shape of the smoothing kernel remains rotationally symmetric (Lindeberg 1993, 2008; Lindeberg and Garding 1997; Mikolajzcyk and Schmid 2004). Hence, besides the commonly used multi-scale Harris operator, affine shape adaptation can be applied to other corner detectors as listed in this article as well as to differential blob detectors such as the Laplacian/difference of Gaussian operator, the determinant of the Hessian and the Hessian–Laplace operator.

## The Wang and Brady corner detection algorithm

The Wang and Brady detector considers the image to be a surface, and looks for places where there is large curvature along an image edge. In other words, the algorithm looks for places where the edge changes direction rapidly. The corner score, C , is given by:

$C=\left({\frac {\delta ^{2}I}{\delta \mathbf {t} ^{2}}}\right)^{2}-c|\nabla I|^{2},$

where ${\bf {t}}$ is the unit vector perpendicular to the gradient, and c determines how edge-phobic the detector is. The authors also note that smoothing (Gaussian is suggested) is required to reduce noise.

Smoothing also causes displacement of corners, so the authors derive an expression for the displacement of a 90 degree corner, and apply this as a correction factor to the detected corners.

## The SUSAN corner detector

SUSAN is an acronym standing for *smallest univalue segment assimilating nucleus*. This method is the subject of a 1994 UK patent which is no longer in force.

For feature detection, SUSAN places a circular mask over the pixel to be tested (the nucleus). The region of the mask is M , and a pixel in this mask is represented by ${\vec {m}}\in M$ . The nucleus is at ${\vec {m}}_{0}$ . Every pixel is compared to the nucleus using the comparison function:

$c({\vec {m}})=e^{-\left({\frac {I({\vec {m}})-I({\vec {m}}_{0})}{t}}\right)^{6}}$

where t is the brightness difference threshold, I is the brightness of the pixel and the power of the exponent has been determined empirically. This function has the appearance of a smoothed top-hat or rectangular function. The area of the SUSAN is given by:

$n(M)=\sum _{{\vec {m}}\in M}c({\vec {m}})$

If c is the rectangular function, then n is the number of pixels in the mask which are within t of the nucleus. The response of the SUSAN operator is given by:

$R(M)={\begin{cases}g-n(M)&{\mbox{if}}\ n(M)<g\\0&{\mbox{otherwise,}}\end{cases}}$

where g is named the 'geometric threshold'. In other words, the SUSAN operator only has a positive score if the area is small enough. The smallest SUSAN locally can be found using non-maximal suppression, and this is the complete SUSAN operator.

The value t determines how similar points have to be to the nucleus before they are considered to be part of the univalue segment. The value of g determines the minimum size of the univalue segment. If g is large enough, then this becomes an edge detector.

For corner detection, two further steps are used. Firstly, the centroid of the SUSAN is found. A proper corner will have the centroid far from the nucleus. The second step insists that all points on the line from the nucleus through the centroid out to the edge of the mask are in the SUSAN.

## The Trajkovic and Hedley corner detector

In a manner similar to SUSAN, this detector directly tests whether a patch under a pixel is self-similar by examining nearby pixels. ${\vec {c}}$ is the pixel to be considered, and ${\vec {p}}\in P$ is point on a circle P centered around ${\vec {c}}$ . The point ${\vec {p}}'$ is the point opposite to ${\vec {p}}$ along the diameter.

The response function is defined as:

$r({\vec {c}})=\min _{{\vec {p}}\in P}\left(\left(I({\vec {p}})-I({\vec {c}})\right)^{2}+\left(I({\vec {p}}')-I({\vec {c}})\right)^{2}\right)$

This will be large when there is no direction in which the centre pixel is similar to two nearby pixels along a diameter. P is a discretised circle (a Bresenham circle), so interpolation is used for intermediate diameters to give a more isotropic response. Since any computation gives an upper bound on the $\min$ , the horizontal and vertical directions are checked first to see if it is worth proceeding with the complete computation of c .

## AST-based feature detectors

AST is an acronym standing for *accelerated segment test*. This test is a relaxed version of the SUSAN corner criterion. Instead of evaluating the circular disc, only the pixels in a Bresenham circle of radius r around the candidate point are considered. If n contiguous pixels are all brighter than the nucleus by at least t or all darker than the nucleus by t , then the pixel under the nucleus is considered to be a feature. This test is reported to produce very stable features. The choice of the order in which the pixels are tested is a so-called Twenty Questions problem. Building short decision trees for this problem results in the most computationally efficient feature detectors available.

The first corner detection algorithm based on the AST is FAST (features from accelerated segment test). Although r can in principle take any value, FAST uses only a value of 3 (corresponding to a circle of 16 pixels circumference), and tests show that the best results are achieved with n being 9. This value of n is the lowest one at which edges are not detected. The order in which pixels are tested is determined by the ID3 algorithm from a training set of images. Confusingly, the name of the detector is somewhat similar to the name of the paper describing Trajkovic and Hedley's detector.

## Automatic synthesis of detectors

Trujillo and Olague introduced a method by which genetic programming is used to automatically synthesize image operators that can detect interest points. The terminal and function sets contain primitive operations that are common in many previously proposed man-made designs. Fitness measures the stability of each operator through the repeatability rate, and promotes a uniform dispersion of detected points across the image plane. The performance of the evolved operators has been confirmed experimentally using training and testing sequences of progressively transformed images. Hence, the proposed GP algorithm is considered to be human-competitive for the problem of interest point detection.

## Spatio-temporal interest point detectors

The Harris operator has been extended to space-time by Laptev and Lindeberg. Let $\mu$ denote the spatio-temporal second-moment matrix defined by

$A=\sum _{u}\sum _{v}\sum _{w}h(u,v,w){\begin{bmatrix}L_{x}(u,v,w)^{2}&L_{x}(u,v,w)L_{y}(u,v,w)&L_{x}(u,v,w)L_{t}(u,v,w)\\L_{x}(u,v,w)L_{y}(u,v,w)&L_{y}(u,v,w)^{2}&L_{y}(u,v,w)L_{t}(u,v,w)\\L_{x}(u,v,w)L_{t}(u,v,w)&L_{y}(u,v,w)L_{t}(u,v,w)&L_{t}(u,v,w)^{2}\\\end{bmatrix}}={\begin{bmatrix}\langle L_{x}^{2}\rangle &\langle L_{x}L_{y}\rangle &\langle L_{x}L_{t}\rangle \\\langle L_{x}L_{y}\rangle &\langle L_{y}^{2}\rangle &\langle L_{y}L_{t}\rangle \\\langle L_{x}L_{t}\rangle &\langle L_{y}L_{t}\rangle &\langle L_{t}^{2}\rangle \\\end{bmatrix}}$

Then, for a suitable choice of $k<1/27$ , spatio-temporal interest points are detected from spatio-temporal extrema of the following spatio-temporal Harris measure:

$H=\det(\mu )-\kappa \,\operatorname {trace} ^{2}(\mu ).$

The determinant of the Hessian operator has been extended to joint space-time by Willems et al and Lindeberg, leading to the following scale-normalized differential expression:

$\det(H_{(x,y,t),\mathrm {norm} }L)=\,s^{2\gamma _{s}}\tau ^{\gamma _{\tau }}\left(L_{xx}L_{yy}L_{tt}+2L_{xy}L_{xt}L_{yt}-L_{xx}L_{yt}^{2}-L_{yy}L_{xt}^{2}-L_{tt}L_{xy}^{2}\right).$

In the work by Willems et al, a simpler expression corresponding to $\gamma _{s}=1$ and $\gamma _{\tau }=1$ was used. In Lindeberg, it was shown that $\gamma _{s}=5/4$ and $\gamma _{\tau }=5/4$ implies better scale selection properties in the sense that the selected scale levels obtained from a spatio-temporal Gaussian blob with spatial extent $s=s_{0}$ and temporal extent $\tau =\tau _{0}$ will perfectly match the spatial extent and the temporal duration of the blob, with scale selection performed by detecting spatio-temporal scale-space extrema of the differential expression.

The Laplacian operator has been extended to spatio-temporal video data by Lindeberg, leading to the following two spatio-temporal operators, which also constitute models of receptive fields of non-lagged vs. lagged neurons in the LGN:

$\partial _{t,\mathrm {norm} }(\nabla _{(x,y),\mathrm {norm} }^{2}L)=s^{\gamma _{s}}\tau ^{\gamma _{\tau }/2}(L_{xxt}+L_{yyt}),$

$\partial _{tt,\mathrm {norm} }(\nabla _{(x,y),\mathrm {norm} }^{2}L)=s^{\gamma _{s}}\tau ^{\gamma _{\tau }}(L_{xxtt}+L_{yytt}).$

For the first operator, scale selection properties call for using $\gamma _{s}=1$ and $\gamma _{\tau }=1/2$ , if we want this operator to assume its maximum value over spatio-temporal scales at a spatio-temporal scale level reflecting the spatial extent and the temporal duration of an onset Gaussian blob. For the second operator, scale selection properties call for using $\gamma _{s}=1$ and $\gamma _{\tau }=3/4$ , if we want this operator to assume its maximum value over spatio-temporal scales at a spatio-temporal scale level reflecting the spatial extent and the temporal duration of a blinking Gaussian blob.

Colour extensions of spatio-temporal interest point detectors have been investigated by Everts et al.
