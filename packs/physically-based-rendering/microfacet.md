---
title: "Specular highlight"
source: https://en.wikipedia.org/wiki/Microfacet
domain: physically-based-rendering
license: CC-BY-SA-4.0
tags: physically based rendering, pbr material, microfacet model, fresnel reflectance
fetched: 2026-07-02
---

# Specular highlight

(Redirected from

Microfacet

)

A **specular highlight** is the bright spot of light that appears on shiny objects when illuminated (for example, see image on right). Specular highlights are important in 3D computer graphics, as they provide a strong visual cue for the shape of an object and its location with respect to light sources in the scene.

## Microfacets

The term *specular* means that light is perfectly reflected in a mirror-like way from the light source to the viewer. Specular reflection is visible only where the surface normal is oriented precisely halfway between the direction of incoming light and the direction of the viewer; this is called the **half-angle** direction because it bisects (divides into halves) the angle between the incoming light and the viewer. Thus, a specularly reflecting surface would show a specular highlight as the perfectly sharp reflected image of a light source. However, many shiny objects show blurred specular highlights.

This can be explained by the existence of **microfacets**. We assume that surfaces that are not perfectly smooth are composed of many very tiny facets, each of which is a perfect specular reflector. These microfacets have normals that are distributed about the normal of the approximating smooth surface. The degree to which microfacet normals differ from the smooth surface normal is determined by the roughness of the surface. At points on the object where the smooth normal is close to the half-angle direction, many of the microfacets point in the half-angle direction and so the specular highlight is bright. As one moves away from the center of the highlight, the smooth normal and the half-angle direction get farther apart; the number of microfacets oriented in the half-angle direction falls, and so the intensity of the highlight falls off to zero.

The specular highlight often reflects the color of the light source, not the color of the reflecting object. This is because many materials have a thin layer of clear material above the surface of the pigmented material. For example, plastic is made up of tiny beads of color suspended in a clear polymer and human skin often has a thin layer of oil or sweat above the pigmented cells. Such materials will show specular highlights in which all parts of the color spectrum are reflected equally. On metallic materials such as gold the color of the specular highlight will reflect the color of the material.

## Models

A number of different models exist to predict the distribution of microfacets. Most assume that the microfacet normals are distributed evenly around the normal; these models are called **isotropic**. If microfacets are distributed with a preference for a certain direction along the surface, the distribution is **anisotropic**.

NOTE: In most equations, when it says $({\hat {A}}\cdot {\hat {B}})$ it means $\max(0,({\hat {A}}\cdot {\hat {B}}))$

### Phong distribution

In the Phong reflection model, the intensity of the specular highlight is calculated as:

$k_{\mathrm {spec} }=\|R\|\|V\|\cos ^{n}\beta =({\hat {R}}\cdot {\hat {V}})^{n}$

Where *R* is the mirror reflection of the light vector off the surface, and *V* is the viewpoint vector.

In the Blinn–Phong shading model, the intensity of a specular highlight is calculated as:

$k_{\mathrm {spec} }=\|N\|\|H\|\cos ^{n}\beta =({\hat {N}}\cdot {\hat {H}})^{n}$

Where *N* is the smooth surface normal and *H* is the half-angle direction (the direction vector midway between *L*, the vector to the light, and *V*, the viewpoint vector).

The number *n* is called the Phong exponent, and is a user-chosen value that controls the apparent smoothness of the surface. These equations imply that the distribution of microfacet normals is an approximately Gaussian distribution (for large n ), or approximately Pearson type II distribution, of the corresponding angle. While this is a useful heuristic and produces believable results, it is not a physically based model.

Another similar formula, but only calculated differently:

$k=({\vec {L}}\cdot {\vec {R}})^{n}=[{\vec {L}}\cdot ({\vec {E}}-2{\vec {N}}({\vec {N}}\cdot {\vec {E}}))]^{n},$

where

R

is an eye reflection vector,

E

is an eye vector (

view vector

),

N

is

surface normal vector

. All vectors are normalized (

$\|{\vec {E}}\|=\|{\vec {N}}\|=1$

).

L

is a light vector. For example,

${\vec {N}}=\{0;\;1;\;0\};\;\;{\vec {E}}=\{{\frac {\sqrt {3}}{2}};\;{\frac {1}{2}};\;0\};\;\;{\vec {L}}=\{-0.6;\;0.8;\;0\};\;\;n=3$

then:

$k=[{\vec {L}}\cdot ({\vec {E}}-2{\vec {N}}({\vec {N}}\cdot {\vec {E}}))]^{n}=[{\vec {L}}\cdot ({\vec {E}}-2{\vec {N}}(0\cdot {\frac {\sqrt {3}}{2}}+1\cdot 0.5+0\cdot 0))]^{3}=$

$=[{\vec {L}}\cdot ({\vec {E}}-{\vec {N}})]^{3}=[{\vec {L}}\cdot (\{{\frac {\sqrt {3}}{2}}-0;\;{\frac {1}{2}}-1;\;0-0\})]^{3}=[-0.6\cdot {\frac {\sqrt {3}}{2}}+0.8\cdot (-0.5)+0\cdot 0]^{3}=(-0.5196-0.4)^{3}=0.9196^{3}=0.7777.$

Approximate formula is this:

$k=({\vec {N}}\cdot {\vec {H}})^{n}=({\vec {N}}\cdot (({\vec {L}}+{\vec {E}})/2))^{n}=({\vec {N}}\cdot ((\{-0.6+{\frac {\sqrt {3}}{2}};\;0.8+0.5;\;0+0\})/2))^{3}=({\vec {N}}\cdot ((\{0.266;\;1.3;\;0\})/2))^{3}=$

$=({\vec {N}}\cdot (\{0.133;\;0.65;\;0\}))^{3}=(0\cdot 0.133+1\cdot 0.65+0)^{3}=0.65^{3}=0.274625.$

If vector

H

is normalized

${\frac {{\vec {H}}\{0.133;\;0.65;\;0\}}{\|{\vec {H}}\|}}={\frac {{\vec {H}}\{0.133;\;0.65;\;0\}}{\sqrt {0.133^{2}+0.65^{2}}}}={\frac {{\vec {H}}\{0.133;\;0.65;\;0\}}{0.668}}=\{0.20048;0.979701;0\},$

then

$k=({\vec {N}}\cdot {\vec {H}})^{n}=(0\cdot 0.2+1\cdot 0.9797+0\cdot 0)^{3}=0.979701^{3}=0.940332.$

### Gaussian distribution

A slightly better model of microfacet distribution can be created using a Gaussian distribution. The usual function calculates specular highlight intensity as:

$k_{\mathrm {spec} }=e^{-\left({\frac {\angle (N,H)}{m}}\right)^{2}}$

where *m* is a constant between 0 and 1 that controls the apparent smoothness of the surface.

### Beckmann distribution

A physically based model of microfacet distribution is the Beckmann distribution:

$k_{\mathrm {spec} }={\frac {\exp {\left(-\tan ^{2}(\alpha )/\sigma ^{2}\right)}}{\pi \sigma ^{2}\cos ^{4}(\alpha )}},~\alpha =\arccos(N\cdot H)$

where *$\sigma$* is the rms slope of the surface microfacets (the roughness of the material). Compared to the empirical models above, this function "gives the absolute magnitude of the reflectance without introducing arbitrary constants; the disadvantage is that it requires more computation". However, this model can be simplified since $\tan ^{2}(\alpha )/\sigma ^{2}={\frac {1-\cos ^{2}(\alpha )}{\cos ^{2}(\alpha )\sigma ^{2}}}$ . Also note that the product of $\cos(\alpha )$ and a surface distribution function is normalized over the half-sphere which is obeyed by this function.

### Heidrich–Seidel anisotropic distribution

The Heidrich–Seidel. distribution is a simple anisotropic distribution, based on the Phong model. It can be used to model surfaces that have small parallel grooves or fibers, such as brushed metal, satin, and hair.

#### Parameters

Input parameters:

- *D* = Thread direction ( In original papers this appears as *T* )
- *s* = Shininess exponent. Values are between 0 and infinity
- *N* = Real surface normal
- *L* = Vector from point to light
- *V* = Vector from point to viewer
- *T* = Thread direction based on real surface normal.
- *P* = Projection of vector L onto plane with normal T ( in original paper this appears as *N'* ).
- *R* = Reflected incoming light ray against *T*. Incoming light ray is equal to negative *L*.

All vectors are unit.

#### Conditions

If some of the conditions are not satisfied from the list then the color is zero

- $0<N\cdot V$
- $0<P\cdot V$
- $0<R\cdot V$

Note: This list is not optimized.

#### Formula

First we need to correct original direction of fiber *D* to be perpendicular to real surface normal *N*. This can be done by projection fiber direction on to plane with normal *N*:

$T={\frac {D+(-D\cdot N)*N}{\|D+(-D\cdot N)*N\|}}$

It is expected that fiber is cylindrical. Note the fact that normal of fiber depends on light position. Normal of fiber at given point is:

$P={\frac {L+(-L\cdot T)*T}{\|L+(-L\cdot T)*T\|}}$

Reflected ray needed for specular calculation:

$R={\frac {-L+2*(L\cdot P)*P}{\|-L+2*(L\cdot P)*P\|}}$

##### Final calculation

$k_{\mathrm {diff} }=L\cdot P$

$k_{\mathrm {spec} }=(V\cdot R)^{s}$

#### Optimization

Calculation of *R* and *P* are expensive operation. To avoid their calculation original formula can be rewritten in next form:

##### Diffuse

$k_{\mathrm {diff} }=L\cdot P=L\cdot {\frac {L+(-L\cdot T)*T}{\|L+(-L\cdot T)*T\|}}=...={\sqrt {1-(L\cdot T)^{2}}}$

##### Specular

${\begin{aligned}k_{\mathrm {spec} }&{}=(V\cdot R)^{s}\\&{}=({\sqrt {1-(L\cdot T)^{2}}}*{\sqrt {1-(V\cdot T)^{2}}}-(L\cdot T)*(V\cdot T))^{s}\\&{}=\left[\sin(\angle (L,T))\sin(\angle (V,T))-\cos(\angle (L,T))\cos(\angle (V,T))\right]^{s}\\&{}=(-\cos(\angle (L,T)+\angle (V,T)))^{s}\end{aligned}}$

*T* can be observed as bump normal and after that it is possible to apply other BRDF than Phong. The anisotropic $k_{\mathrm {spec} }$ should be used in conjunction with an isotropic distribution like a Phong distribution to produce the correct specular highlight

### Ward anisotropic distribution

The Ward anisotropic distribution uses two user-controllable parameters *αx* and *αy* to control the anisotropy. If the two parameters are equal, then an isotropic highlight results. The specular term in the distribution is:

$k_{\mathrm {spec} }={\frac {\rho _{s}}{\sqrt {(N\cdot L)(N\cdot V)}}}{\frac {N\cdot L}{4\pi \alpha _{x}\alpha _{y}}}\exp \left[-2{\frac {\left({\frac {H\cdot X}{\alpha _{x}}}\right)^{2}+\left({\frac {H\cdot Y}{\alpha _{y}}}\right)^{2}}{1+(H\cdot N)}}\right]$

The specular term is zero if *N*·*L* < 0 or *N*·*V* < 0. All vectors are unit vectors. The vector *V* is the viewing direction, *L* is the direction from the surface point to the light, *H* is the half-angle direction between *V* and *L*, *N* is the surface normal, and *X* and *Y* are two orthogonal vectors in the normal plane which specify the anisotropic directions.

### Cook–Torrance model

The Cook–Torrance model uses a specular term of the form

$k_{\mathrm {spec} }={\frac {F}{\pi }}{\frac {DG}{(V\cdot N)(N\cdot L)}}$

.

Here D is the Beckmann distribution factor as above and F is the Fresnel term. For performance reasons, in real-time 3D graphics Schlick's approximation is often used to approximate the Fresnel term.

G is the geometric attenuation term, describing selfshadowing due to the microfacets, and is of the form

$G=\min {\left(1,{\frac {2(H\cdot N)(V\cdot N)}{V\cdot H}},{\frac {2(H\cdot N)(L\cdot N)}{V\cdot H}}\right)}$

.

In these formulas V is the vector to the camera or eye, H is the half-angle vector, L is the vector to the light source and N is the normal vector, and α is the angle between H and N.

### Using multiple distributions

If desired, different distributions (usually, using the same distribution function with different values of *m* or *n*) can be combined using a weighted average. This is useful for modelling, for example, surfaces that have small smooth and rough patches rather than uniform roughness.
