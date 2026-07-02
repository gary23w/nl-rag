---
title: "Radon transform"
source: https://en.wikipedia.org/wiki/Filtered_back_projection
domain: radon-transform
license: CC-BY-SA-4.0
tags: radon transform, filtered back projection, tomographic reconstruction, projection-slice theorem
fetched: 2026-07-02
---

# Radon transform

(Redirected from

Filtered back projection

)

In mathematics, the **Radon transform** is the integral transform which takes a function *f* defined on the plane to a function *Rf* defined on the (two-dimensional) space of lines in the plane, whose value at a particular line is equal to the line integral of the function over that line. The transform was introduced in 1917 by Johann Radon, who also provided a formula for the inverse transform. Radon further included formulas for the transform in three dimensions, in which the integral is taken over planes (integrating over lines is known as the X-ray transform). It was later generalized to higher-dimensional Euclidean spaces and more broadly in the context of integral geometry. The complex analogue of the Radon transform is known as the Penrose transform. The Radon transform is widely applicable to tomography, the creation of an image from the projection data associated with cross-sectional scans of an object.

## Explanation

If a function f represents an unknown density, then the Radon transform represents the projection data obtained as the output of a tomographic scan. The inverse of the Radon transform can be used to reconstruct the original density from the projection data, and thus it forms the mathematical underpinning for tomographic reconstruction, also known as iterative reconstruction.

The Radon transform data is often called a **sinogram** because the Radon transform of an off-center point source is a sinusoid. Consequently, the Radon transform of a number of small objects appears graphically as a number of blurred sine waves with different amplitudes and phases.

The Radon transform is useful in computed axial tomography (CAT scan), barcode scanners, electron microscopy of macromolecular assemblies like viruses and protein complexes, reflection seismology and in the solution of hyperbolic partial differential equations.

## Definition

Let $f(\mathbf {x} )=f(x,y)$ be a function that satisfies the three regularity conditions:

1. $f(\mathbf {x} )$ is continuous;
2. the double integral $\displaystyle \iint {\frac {\vert f(\mathbf {x} )\vert }{\sqrt {x^{2}+y^{2}}}}\,dx\,dy$ , extending over the whole plane, converges;
3. for any arbitrary point $(x,y)$ on the plane, $\lim _{r\to \infty }\int _{0}^{2\pi }f(x+r\cos \varphi ,y+r\sin \varphi )\,d\varphi =0.$

The Radon transform, $Rf$ , is a function defined on the space of straight lines $L\subset \mathbb {R} ^{2}$ by the line integral along each such line as: $Rf(L)=\int _{L}f(\mathbf {x} )\vert d\mathbf {x} \vert .$ Concretely, the parametrization of any straight line L with respect to arc length z can always be written: $(x(z),y(z))={\Big (}(z\,\sin \alpha +s\,\cos \alpha ),(-z\,\cos \alpha +s\,\sin \alpha ){\Big )}$ where s is the distance of L from the origin and $\alpha$ is the angle the normal vector to L makes with the x -axis. It follows that the quantities $(\alpha ,s)$ can be considered as coordinates on the space of all lines in $\mathbb {R} ^{2}$ , and the Radon transform can be expressed in these coordinates by: ${\begin{aligned}Rf(\alpha ,s)&=\int _{-\infty }^{\infty }f(x(z),y(z))\,dz\\&=\int _{-\infty }^{\infty }f{\big (}(z\,\sin \alpha +s\,\cos \alpha ),(-z\,\cos \alpha +s\,\sin \alpha ){\big )}\,dz.\end{aligned}}$ More generally, in n -dimensional Euclidean space $\mathbb {R} ^{n}$ , the Radon transform of a function f satisfying the regularity conditions is a function $Rf$ on the space $\Sigma _{n}$ of all hyperplanes in $\mathbb {R} ^{n}$ . It is defined by:

Shepp Logan phantom

Radon transform

Inverse Radon transform

$Rf(\xi )=\int _{\xi }f(\mathbf {x} )\,d\sigma (\mathbf {x} ),\quad \forall \xi \in \Sigma _{n}$ where the integral is taken with respect to the natural hypersurface measure, $d\sigma$ (generalizing the $\vert d\mathbf {x} \vert$ term from the 2 -dimensional case). Observe that any element of $\Sigma _{n}$ is characterized as the solution locus of an equation $\mathbf {x} \cdot \alpha =s$ , where $\alpha \in S^{n-1}$ is a unit vector and $s\in \mathbb {R}$ . Thus the n -dimensional Radon transform may be rewritten as a function on $S^{n-1}\times \mathbb {R}$ via: $Rf(\alpha ,s)=\int _{\mathbf {x} \cdot \alpha =s}f(\mathbf {x} )\,d\sigma (\mathbf {x} ).$ It is also possible to generalize the Radon transform still further by integrating instead over k -dimensional affine subspaces of $\mathbb {R} ^{n}$ . The X-ray transform is the most widely used special case of this construction, and is obtained by integrating over straight lines.

## Relationship with the Fourier transform

The Radon transform is closely related to the Fourier transform. We define the univariate Fourier transform here as: ${\hat {f}}(\omega )=\int _{-\infty }^{\infty }f(x)e^{-2\pi ix\omega }\,dx.$ For a function of a 2 -vector $\mathbf {x} =(x,y)$ , the univariate Fourier transform is: ${\hat {f}}(\mathbf {w} )=\iint _{\mathbb {R} ^{2}}f(\mathbf {x} )e^{-2\pi i\mathbf {x} \cdot \mathbf {w} }\,dx\,dy.$ For convenience, denote ${\mathcal {R}}_{\alpha }[f](s)={\mathcal {R}}[f](\alpha ,s)$ . The Fourier slice theorem then states: ${\widehat {{\mathcal {R}}_{\alpha }[f]}}(\sigma )={\hat {f}}(\sigma \mathbf {n} (\alpha ))$ where $\mathbf {n} (\alpha )=(\cos \alpha ,\sin \alpha ).$

Thus the two-dimensional Fourier transform of the initial function along a line at the inclination angle $\alpha$ is the one variable Fourier transform of the Radon transform (acquired at angle $\alpha$ ) of that function. This fact can be used to compute both the Radon transform and its inverse. The result can be generalized into *n* dimensions: ${\hat {f}}(r\alpha )=\int _{\mathbb {R} }{\mathcal {R}}f(\alpha ,s)e^{-2\pi isr}\,ds.$

## Range characterization

The image of the Radon transform on $S^{n-1}\times \mathbb {R}$ can be characterized for functions of sufficient regularity and decay. Since the same unoriented hyperplane is represented by both $(\alpha ,s)$ and $(-\alpha ,-s)$ , every Radon transform satisfies the symmetry condition

$Rf(-\alpha ,-s)=Rf(\alpha ,s).$

There are also conditions on the moments of the Radon transform. If f is sufficiently regular and rapidly decreasing, and

$g(\alpha ,s)=Rf(\alpha ,s),$

then, for every nonnegative integer k , the moment

$M_{k}(\alpha )=\int _{-\infty }^{\infty }s^{k}g(\alpha ,s)\,ds$

is the restriction to $S^{n-1}$ of a homogeneous polynomial in $\alpha$ of degree k . Indeed, formally,

${\begin{aligned}M_{k}(\alpha )&=\int _{-\infty }^{\infty }s^{k}Rf(\alpha ,s)\,ds\\&=\int _{\mathbb {R} ^{n}}(x\cdot \alpha )^{k}f(x)\,dx,\end{aligned}}$

which is a homogeneous polynomial in $\alpha$ .

Conversely, the Helgason–Ludwig range theorem states that these conditions characterize the range of the Radon transform on appropriate test-function spaces. For example, a smooth rapidly decreasing function g on $S^{n-1}\times \mathbb {R}$ is the Radon transform of a Schwartz function on $\mathbb {R} ^{n}$ if and only if it satisfies the symmetry condition and the above moment conditions. A corresponding compactly supported version characterizes the image of $C_{c}^{\infty }(\mathbb {R} ^{n})$ ; in that case one also has the support relation that if f is supported in the ball $|x|\leq A$ , then $Rf(\alpha ,s)=0$ for $|s|>A$ .

In tomography, these consistency conditions describe when projection data can arise from an actual object rather than from an arbitrary function of angle and displacement.

## Dual transform

The dual Radon transform is a kind of adjoint to the Radon transform. Beginning with a function *g* on the space $\Sigma _{n}$ , the dual Radon transform is the function ${\mathcal {R}}^{*}g$ on **R***n* defined by: ${\mathcal {R}}^{*}g(\mathbf {x} )=\int _{\mathbf {x} \in \xi }g(\xi )\,d\mu (\xi ).$ The integral here is taken over the set of all hyperplanes incident with the point ${\textbf {x}}\in \mathbb {R} ^{n}$ , and the measure $d\mu$ is the unique probability measure on the set $\{\xi |\mathbf {x} \in \xi \}$ invariant under rotations about the point $\mathbf {x}$ .

Concretely, for the two-dimensional Radon transform, the dual transform is given by: ${\mathcal {R}}^{*}g(\mathbf {x} )={\frac {1}{2\pi }}\int _{\alpha =0}^{2\pi }g(\alpha ,\mathbf {n} (\alpha )\cdot \mathbf {x} )\,d\alpha .$ In the context of image processing, the dual transform is commonly called *back-projection* as it takes a function defined on each line in the plane and 'smears' or projects it back over the line to produce an image.

### Intertwining property

Let $\Delta$ denote the Laplacian on $\mathbb {R} ^{n}$ defined by: $\Delta ={\frac {\partial ^{2}}{\partial x_{1}^{2}}}+\cdots +{\frac {\partial ^{2}}{\partial x_{n}^{2}}}$ This is a natural rotationally invariant second-order differential operator. On $\Sigma _{n}$ , the "radial" second derivative $Lf(\alpha ,s)\equiv {\frac {\partial ^{2}}{\partial s^{2}}}f(\alpha ,s)$ is also rotationally invariant. The Radon transform and its dual are intertwining operators for these two differential operators in the sense that: ${\mathcal {R}}(\Delta f)=L({\mathcal {R}}f),\quad {\mathcal {R}}^{*}(Lg)=\Delta ({\mathcal {R}}^{*}g).$ In analysing the solutions to the wave equation in multiple spatial dimensions, the intertwining property leads to the translational representation of Lax and Philips. In imaging and numerical analysis this is exploited to reduce multi-dimensional problems into single-dimensional ones, as a dimensional splitting method.

## Reconstruction approaches

The process of *reconstruction* produces the image (or function f in the previous section) from its projection data. *Reconstruction* is an inverse problem.

### Radon inversion formula

In the two-dimensional case, the most commonly used analytical formula to recover f from its Radon transform is the *Filtered Back-projection Formula* or *Radon Inversion Formula*: $f(\mathbf {x} )=\int _{0}^{\pi }({\mathcal {R}}f(\cdot ,\theta )*h)(\left\langle \mathbf {x} ,\mathbf {n} _{\theta }\right\rangle )\,d\theta$ where h is such that ${\hat {h}}(k)=|k|$ and $\mathbf {n_{\theta }} =(\cos \theta ,\sin \theta )$ . The convolution kernel h is referred to as Ramp filter in some literature.

### Ill-posedness

Intuitively, in the *filtered back-projection* formula, by analogy with differentiation, for which ${\textstyle \left({\widehat {{\frac {d}{dx}}f}}\right)\!(k)=ik{\widehat {f}}(k)}$ , we see that the filter performs an operation similar to a derivative. Roughly speaking, then, the filter makes objects *more* singular. A quantitive statement of the ill-posedness of Radon inversion goes as follows: ${\widehat {{\mathcal {R}}^{*}{\mathcal {R}}[g]}}(\mathbf {k} )={\frac {1}{\|\mathbf {k} \|}}{\hat {g}}(\mathbf {k} )$ where ${\mathcal {R}}^{*}$ is the previously defined adjoint to the Radon transform. Thus for $g(\mathbf {x} )=e^{i\left\langle \mathbf {k} _{0},\mathbf {x} \right\rangle }$ , we have: ${\mathcal {R}}^{*}{\mathcal {R}}[g](\mathbf {x} )={\frac {1}{\|\mathbf {k_{0}} \|}}e^{i\left\langle \mathbf {k} _{0},\mathbf {x} \right\rangle }$ The complex exponential $e^{i\left\langle \mathbf {k} _{0},\mathbf {x} \right\rangle }$ is thus an eigenfunction of ${\mathcal {R}}^{*}{\mathcal {R}}$ with eigenvalue ${\textstyle {\frac {1}{\|\mathbf {k} _{0}\|}}}$ . Thus the singular values of ${\mathcal {R}}$ are ${\textstyle {\frac {1}{\sqrt {\|\mathbf {k} \|}}}}$ . Since these singular values tend to 0 , ${\mathcal {R}}^{-1}$ is unbounded.

### Iterative reconstruction methods

Compared with the *Filtered Back-projection* method, iterative reconstruction costs large computation time, limiting its practical use. However, due to the ill-posedness of Radon Inversion, the *Filtered Back-projection* method may be infeasible in the presence of discontinuity or noise. Iterative reconstruction methods (*e.g.* iterative Sparse Asymptotic Minimum Variance) could provide metal artefact reduction, noise and dose reduction for the reconstructed result that attract much research interest around the world.

## Inversion formulas

Explicit and computationally efficient inversion formulas for the Radon transform and its dual are available. The Radon transform in n dimensions can be inverted by the formula: $c_{n}f=(-\Delta )^{(n-1)/2}R^{*}Rf\,$ where $c_{n}=(4\pi )^{(n-1)/2}{\frac {\Gamma (n/2)}{\Gamma (1/2)}}$ , and the power of the Laplacian $(-\Delta )^{(n-1)/2}$ is defined as a pseudo-differential operator if necessary by the Fourier transform: $\left[{\mathcal {F}}(-\Delta )^{(n-1)/2}\varphi \right](\xi )=|2\pi \xi |^{n-1}({\mathcal {F}}\varphi )(\xi ).$ For computational purposes, the power of the Laplacian is commuted with the dual transform $R^{*}$ to give: $c_{n}f={\begin{cases}R^{*}{\frac {d^{n-1}}{ds^{n-1}}}Rf&n{\text{ odd}}\\R^{*}{\mathcal {H}}_{s}{\frac {d^{n-1}}{ds^{n-1}}}Rf&n{\text{ even}}\end{cases}}$ where ${\mathcal {H}}_{s}$ is the Hilbert transform with respect to the *s* variable. In two dimensions, the operator ${\mathcal {H}}_{s}{\frac {d}{ds}}$ appears in image processing as a ramp filter. One can prove directly from the Fourier slice theorem and change of variables for integration that for a compactly supported continuous function f of two variables: $f={\frac {1}{2}}R^{*}{\mathcal {H}}_{s}{\frac {d}{ds}}Rf.$ Thus in an image processing context the original image f can be recovered from the 'sinogram' data $Rf$ by applying a ramp filter (in the s variable) and then back-projecting. As the filtering step can be performed efficiently (for example using digital signal processing techniques) and the back projection step is simply an accumulation of values in the pixels of the image, this results in a highly efficient, and hence widely used, algorithm.

Explicitly, the inversion formula obtained by the latter method is: $f(x)={\begin{cases}\displaystyle -\imath 2\pi (2\pi )^{-n}(-1)^{n/2}\int _{S^{n-1}}{\frac {\partial ^{n-1}}{2\partial s^{n-1}}}Rf(\alpha ,\alpha \cdot x)\,d\alpha &n{\text{ odd}}\\\displaystyle (2\pi )^{-n}(-1)^{n/2}\iint _{\mathbb {R} \times S^{n-1}}{\frac {\partial ^{n-1}}{q\partial s^{n-1}}}Rf(\alpha ,\alpha \cdot x+q)\,d\alpha \,dq&n{\text{ even}}\\\end{cases}}$ The dual transform can also be inverted by an analogous formula: $c_{n}g=(-L)^{(n-1)/2}R(R^{*}g).\,$

## Radon transform in algebraic geometry

In algebraic geometry, a Radon transform (also known as the *Brylinski–Radon transform*) is constructed as follows.

Write

$\mathbf {P} ^{d}\,{\stackrel {p_{1}}{\gets }}\,H\,{\stackrel {p_{2}}{\to }}\,\mathbf {P} ^{\vee ,d}$

for the universal hyperplane, i.e., *H* consists of pairs (*x*, *h*) where *x* is a point in *d*-dimensional projective space $\mathbf {P} ^{d}$ and *h* is a point in the dual projective space (in other words, *x* is a line through the origin in (*d*+1)-dimensional affine space, and *h* is a hyperplane in that space) such that *x* is contained in *h*.

Then the Brylinksi–Radon transform is the functor between appropriate derived categories of étale sheaves

$\operatorname {Rad$

The main theorem about this transform is that this transform induces an equivalence of the categories of perverse sheaves on the projective space and its dual projective space, up to constant sheaves.
