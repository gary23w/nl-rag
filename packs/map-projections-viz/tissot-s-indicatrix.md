---
title: "Tissot's indicatrix"
source: https://en.wikipedia.org/wiki/Tissot%27s_indicatrix
domain: map-projections-viz
license: CC-BY-SA-4.0
tags: map projection, tissot indicatrix, robinson projection, winkel tripel
fetched: 2026-07-02
---

# Tissot's indicatrix

In cartography, a **Tissot's indicatrix** (**Tissot indicatrix**, **Tissot's ellipse**, **Tissot ellipse**, **ellipse of distortion**) (plural: "Tissot's indicatrices") is a mathematical contrivance presented by French mathematician Nicolas Auguste Tissot in 1859 and 1871 to characterize local distortions due to map projection. It is the geometry that results from projecting a circle of infinitesimal radius from a curved geometric model, such as a globe, onto a map. Tissot proved that the resulting diagram is an ellipse whose axes indicate the two principal directions along which scale is maximal and minimal at that point on the map.

A single indicatrix describes the distortion at a single point. Because distortion varies across a map, generally Tissot's indicatrices are placed across a map to illustrate the spatial change in distortion. A common scheme places them at each intersection of displayed meridians and parallels. These schematics are important in the study of map projections, both to illustrate distortion and to provide the basis for the calculations that represent the magnitude of distortion precisely at each point. Because the infinitesimal circles represented by the ellipses on the map all have the same area on the underlying curved geometric model, the distortion imposed by the map projection is evident.

There is a one-to-one correspondence between the Tissot indicatrix and the metric tensor of the map projection coordinate conversion.

## Description

Tissot's theory was developed in the context of cartographic analysis. Generally the geometric model represents the Earth, and comes in the form of a sphere or ellipsoid.

Tissot's indicatrices illustrate linear, angular, and areal distortions of maps:

- A map distorts distances (linear distortion) wherever the quotient between the lengths of an infinitesimally short line as projected onto the projection surface, and as it originally is on the Earth model, deviates from 1. The quotient is called the *scale factor*. Unless the projection is conformal at the point being considered, the scale factor varies by direction around the point.
- A map distorts angles wherever the angles measured on the model of the Earth are not conserved in the projection. This is expressed by an ellipse of distortion which is not a circle.
- A map distorts areas wherever areas measured in the model of the Earth are not conserved in the projection. This is expressed by ellipses of distortion whose areas vary across the map.

In conformal maps, where each point preserves angles projected from the geometric model, the Tissot's indicatrices are all circles of size varying by location, possibly also with varying orientation (given the four circle quadrants split by meridians and parallels). In equal-area projections, where area proportions between objects are conserved, the Tissot's indicatrices all have the same area, though their shapes and orientations vary with location. In arbitrary projections, both area and shape vary across the map.

| World maps comparing Tissot's indicatrices on some common projections |
|---|
| (Equirectangular projection) Equirectangular projection (Mercator projection) Mercator projection (Gall–Peters projection) Gall–Peters projection (Mollweide projection) Mollweide projection (Winkel tripel projection) Winkel tripel projection (Azimuthal equidistant projection) Azimuthal equidistant projection (Fuller projection) Fuller projection (Transverse Mercator projection) Transverse Mercator projection (Lambert cylindrical equal-area projection) Lambert cylindrical equal-area projection (Sinusoidal projection) Sinusoidal projection (Robinson projection) Robinson projection (Stereographic projection) Stereographic projection |

## Mathematics

In the diagram below, the circle $ABCD$ has unit area as defined on the surface of a sphere. The ellipse ${A'B'C'D'}$ is the Tissot's indicatrix that results from some projection of $ABCD$ onto a plane. Linear scale has not been preserved in this projection, as ${OA'\ncong OA}$ and $OB'\ncong OB$ . Because ${\angle M'OA'\ncong \angle MOA}$ , we know that there is an angular distortion. Because $\operatorname {Area} (A'B'C'D')\neq \operatorname {Area} (ABCD)$ , we know there is an areal distortion.

The original circle in the above example had a radius of 1, but when dealing with a Tissot indicatrix, one deals with ellipses of infinitesimal radius. Even though the radii of the original circle and its distortion ellipse will all be infinitesimal, by employing differential calculus the ratios between them can still be meaningfully calculated. For example, if the ratio between the radius of the input circle and a projected circle is equal to 1, then the indicatrix is drawn with as a circle with an area of 1. The size that the indicatrix gets drawn on the map is arbitrary: they are all scaled by the same factor so that their sizes are proportional to one another. Like M in the diagram, the axes from O along the parallel and along the meridian may undergo a change of length and a rotation during projection. For a given point, it is common in the literature to represent the scale along the meridian as h and the scale along the parallel as k . Unless the projection is conformal, all angles except the one subtended by the semi-major axis and semi-minor axis of the ellipse may have changed as well. A particular angle will have changed the most, and the value of that maximum change is known as the angular deformation, denoted as $\theta$ . In general, which angle that is and how it is oriented do not figure prominently into distortion analysis; it is the magnitude of the change that is significant. The values of h , k , and $\theta$ can be computed as follows:

${\begin{aligned}h&={\frac {1}{R}}{\sqrt {{{\left({\frac {\partial x}{\partial \varphi }}\right)}^{2}}+{{\left({\frac {\partial y}{\partial \varphi }}\right)}^{2}}}}\\[4pt]k&={\frac {1}{R\cos \varphi }}{\sqrt {{{\left({\frac {\partial x}{\partial \lambda }}\right)}^{2}}+{{\left({\frac {\partial y}{\partial \lambda }}\right)}^{2}}}}\\[4pt]\sin \theta '&={\frac {1}{R^{2}hk\cos \varphi }}\left({{\frac {\partial y}{\partial \varphi }}{\frac {\partial x}{\partial \lambda }}-{\frac {\partial x}{\partial \varphi }}{\frac {\partial y}{\partial \lambda }}}\right)\\[4pt]a'&={\sqrt {{h^{2}}+{k^{2}}+2hk\sin \theta '}},\quad b'={\sqrt {{h^{2}}+{k^{2}}-2hk\sin \theta '}}\\[4pt]a&={\frac {a'+b'}{2}},\quad b={\frac {a'-b'}{2}}\\[4pt]s&=hk\sin \theta '\\[4pt]\omega &=2\arcsin {\frac {b'}{a'}}\end{aligned}}$

where $\varphi$ and $\lambda$ are the latitude and longitude coordinates of a point, R is the radius of the globe, and x and y are the point's resulting coordinates after projection.

In the result for any given point, a and b are the maximum and minimum scale factors, analogous to the semimajor and semiminor axes in the diagram; s represents the amount of inflation or deflation in area, and $\omega$ represents the maximum angular distortion.

For conformal projections such as the Mercator projection, $h=k$ and $\theta ={\pi \over 2}$ , such that at each point the ellipse degenerates into a circle, with the radius being equal to the scale factor.

For equal-area such as the sinusoidal projection, the semi-major axis of the ellipse is the reciprocal of the semi-minor axis, such that every ellipse has equal area even as their eccentricities vary.

For arbitrary projections, the shape and the area of the ellipses at each point are largely independent from one another.

## An alternative derivation for numerical computation

Another way to understand and derive Tissot's indicatrix is through the differential geometry of surfaces. This approach lends itself well to modern numerical methods, as the parameters of Tissot's indicatrix can be computed using singular value decomposition (SVD) and central difference approximation.

### Differential distance on the ellipsoid

Let a 3D point, ${\hat {X}}$ , on an ellipsoid be parameterized as:

${\hat {X}}(\lambda ,\phi )=\left[{\begin{matrix}N\cos {\lambda }\cos {\phi }\\-N(1-e^{2})\sin {\phi }\\N\sin {\lambda }\cos {\phi }\end{matrix}}\right]$

where $(\lambda ,\phi )$ are longitude and latitude, respectively, and N is a function of the equatorial radius, R , and eccentricity, e :

$N={\frac {R}{\sqrt {1-e^{2}\sin ^{2}(\phi )}}}$

The element of distance on the sphere, $ds$ is defined by the first fundamental form:

$ds^{2}={\begin{bmatrix}d\lambda &d\phi \end{bmatrix}}{\begin{bmatrix}E&F\\F&G\end{bmatrix}}{\begin{bmatrix}d\lambda \\d\phi \end{bmatrix}}$

whose coefficients are defined as:

${\begin{aligned}&E={\frac {\partial {\hat {X}}}{\partial \lambda }}{\boldsymbol {\cdot }}{\frac {\partial {\hat {X}}}{\partial \lambda }}\\&F={\frac {\partial {\hat {X}}}{\partial \lambda }}{\boldsymbol {\cdot }}{\frac {\partial {\hat {X}}}{\partial \phi }}\\&G={\frac {\partial {\hat {X}}}{\partial \phi }}{\boldsymbol {\cdot }}{\frac {\partial {\hat {X}}}{\partial \phi }}\\\end{aligned}}$

Computing the necessary derivatives gives:

${\frac {\partial {\hat {X}}}{\partial \lambda }}=\left[{\begin{matrix}-N\sin {\lambda }\cos {\phi }\\0\\N\cos {\lambda }\cos {\phi }\end{matrix}}\right]\qquad \qquad {\frac {\partial {\hat {X}}}{\partial \phi }}=\left[{\begin{matrix}-M\cos {\lambda }\sin {\phi }\\-M\cos {\phi }\\M\sin {\lambda }\sin {\phi }\end{matrix}}\right]$

where M is a function of the equatorial radius, R , and the ellipsoid eccentricity, e :

$M={\frac {R(1-e^{2})}{(1-e^{2}\sin ^{2}(\phi ))^{\frac {3}{2}}}}$

Substituting these values into the first fundamental form gives the formula for elemental distance on the ellipsoid:

$ds^{2}=\left(N\cos {\phi }\right)^{2}d\lambda ^{2}+M^{2}d\phi ^{2}$

This result relates the measure of distance on the ellipsoid surface as a function of the spherical coordinate system.

### Transforming the element of distance

Recall that the purpose of Tissot's indicatrix is to relate how distances on the sphere change when mapped to a planar surface. Specifically, the desired relation is the transform ${\mathcal {T}}$ that relates differential distance along the bases of the spherical coordinate system to differential distance along the bases of the Cartesian coordinate system on the planar map. This can be expressed by the relation:

${\begin{bmatrix}dx\\dy\end{bmatrix}}={\mathcal {T}}{\begin{bmatrix}ds(\lambda ,0)\\ds(0,\phi )\end{bmatrix}}$

where $ds(\lambda ,0)$ and $ds(0,\phi )$ represent the computation of $ds$ along the longitudinal and latitudinal axes, respectively. Computation of $ds(\lambda ,0)$ and $ds(0,\phi )$ can be performed directly from the equation above, yielding:

${\begin{aligned}&ds(\lambda ,0)=N\cos(\phi )d\lambda \\&ds(0,\phi )=Md\phi \end{aligned}}$

For the purposes of this computation, it is useful to express this relationship as a matrix operation:

${\begin{bmatrix}d\lambda \\d\phi \end{bmatrix}}=K{\begin{bmatrix}ds(\lambda ,0)\\ds(0,\phi )\end{bmatrix}},\qquad K={\begin{bmatrix}{\frac {1}{N\cos {\phi }}}&0\\0&{\frac {1}{M}}\end{bmatrix}}$

Now, in order to relate the distances on the ellipsoid surface to those on the plane, we need to relate the coordinate systems. From the chain rule, we can write:

${\begin{bmatrix}dx\\dy\end{bmatrix}}=J{\begin{bmatrix}d\lambda \\d\phi \end{bmatrix}}$

where J is the Jacobian matrix:

$J={\begin{bmatrix}{\frac {\partial x}{\partial \lambda }}&{\frac {\partial x}{\partial \phi }}\\{\frac {\partial y}{\partial \lambda }}&{\frac {\partial y}{\partial \phi }}\end{bmatrix}}$

Plugging in the matrix expression for $d\lambda$ and $d\phi$ yields the definition of the transform ${\mathcal {T}}$ represented by the indicatrix:

${\begin{bmatrix}dx\\dy\end{bmatrix}}=JK{\begin{bmatrix}ds(\lambda ,0)\\ds(0,\phi )\end{bmatrix}}$

${\mathcal {T}}=JK$

This transform ${\mathcal {T}}$ encapsulates the mapping from the ellipsoid surface to the plane. Expressed in this form, SVD can be used to parcel out the important components of the local transformation.

### Numerical computation and SVD

In order to extract the desired distortion information, at any given location in the spherical coordinate system, the values of K can be computed directly. The Jacobian, J , can be computed analytically from the mapping function itself, but it is often simpler to numerically approximate the values at any location on the map using central differences. Once these values are computed, SVD can be applied to each transformation matrix to extract the local distortion information. Remember that, because distortion is local, every location on the map will have its own transformation.

Recall the definition of SVD:

$\mathrm {SVD} ({\mathcal {T}})=U\Lambda V^{T}$

It is the decomposition of the transformation, ${\mathcal {T}}$ , into a rotation in the source domain (i.e. the ellipsoid surface), $V^{T}$ , a scaling along the basis, $\Lambda$ , and a subsequent second rotation, U . For understanding distortion, the first rotation is irrelevant, as it rotates the axes of the circle but has no bearing on the final orientation of the ellipse. The next operation, represented by the diagonal singular value matrix, scales the circle along its axes, deforming it to an ellipse. Thus, the singular values represent the scale factors along axes of the ellipse. The first singular value provides the semi-major axis, a , and the second provides the semi-minor axis, b , which are the directional scaling factors of distortion. Scale distortion can be computed as the area of the ellipse, $ab$ , or equivalently by the determinant of ${\mathcal {T}}$ . Finally, the orientation of the ellipse, $\theta$ , can be extracted from the first column of U as:

$\theta =\arctan \left({\frac {u_{1,0}}{u_{0,0}}}\right)$

## Gallery

- (The transverse Mercator projection with Tissot's indicatrices) The transverse Mercator projection with Tissot's indicatrices
- (The stereographic projection with Tissot's indicatrices) The stereographic projection with Tissot's indicatrices
- (The sinusoidal projection with Tissot's indicatrices) The sinusoidal projection with Tissot's indicatrices
- (The Peirce quincuncial projection with Tissot's indicatrices) The Peirce quincuncial projection with Tissot's indicatrices
- (The Miller cylindrical projection with Tissot's indicatrices) The Miller cylindrical projection with Tissot's indicatrices
- (The Hammer projection with Tissot's indicatrices) The Hammer projection with Tissot's indicatrices
- (The azimuthal equidistant projection with Tissot's indicatrices) The azimuthal equidistant projection with Tissot's indicatrices
- (The Fuller projection with Tissot's indicatrices) The Fuller projection with Tissot's indicatrices
