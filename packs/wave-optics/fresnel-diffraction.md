---
title: "Fresnel diffraction"
source: https://en.wikipedia.org/wiki/Fresnel_diffraction
domain: wave-optics
license: CC-BY-SA-4.0
tags: wave interference, fresnel diffraction, fraunhofer diffraction, diffraction grating
fetched: 2026-07-02
---

# Fresnel diffraction

In optics, the **Fresnel diffraction** equation for **near-field diffraction** is an approximation of the Kirchhoff–Fresnel diffraction that can be applied to the propagation of waves in the near field. It is used to calculate the diffraction pattern created by waves passing through an aperture or around an object, when viewed from relatively close to the object. In contrast the diffraction pattern in the far field region is given by the Fraunhofer diffraction equation.

The near field can be specified by the Fresnel number, *F*, of the optical arrangement. When $F\ll 1$ the diffracted wave is considered to be in the Fraunhofer field. However, the validity of the Fresnel diffraction integral is deduced by the approximations derived below. Specifically, the phase terms of third order and higher must be negligible, a condition that may be written as

${\frac {F\theta ^{2}}{4}}\ll 1,$

where $\theta$ is the maximal angle described by $\theta \approx a/L,$ *a* and *L* the same as in the definition of the Fresnel number. Hence this condition can be approximated as ${\textstyle {\frac {a^{4}}{4L^{3}\lambda }}\ll 1}$ .

The multiple Fresnel diffraction at closely spaced periodical ridges (ridged mirror) causes the specular reflection; this effect can be used for atomic mirrors.

## Early treatments of this phenomenon

Some of the earliest work on what would become known as Fresnel diffraction was carried out by Francesco Maria Grimaldi in Italy in the 17th century. In his monograph entitled "Light", Richard C. MacLaurin explains Fresnel diffraction by asking what happens when light propagates, and how that process is affected when a barrier with a slit or hole in it is interposed in the beam produced by a distant source of light. He uses the Principle of Huygens to investigate, in classical terms, what transpires. The wave front that proceeds from the slit and on to a detection screen some distance away very closely approximates a wave front originating across the area of the gap without regard to any minute interactions with the actual physical edge.

The result is that if the gap is very narrow only diffraction patterns with bright centers can occur. If the gap is made progressively wider, then diffraction patterns with dark centers will alternate with diffraction patterns with bright centers. As the gap becomes larger, the differentials between dark and light bands decrease until a diffraction effect can no longer be detected.

MacLaurin does not mention the possibility that the center of the series of diffraction rings produced when light is shone through a small hole may be black, but he does point to the inverse situation wherein the shadow produced by a small circular object can paradoxically have a bright center. (p. 219)

In his *Optics*, Francis Weston Sears offers a mathematical approximation suggested by Fresnel that predicts the main features of diffraction patterns and uses only simple mathematics. By considering the perpendicular distance from the hole in a barrier screen to a nearby detection screen along with the wavelength of the incident light, it is possible to compute a number of regions called half-period elements or Fresnel zones. The inner zone is a circle and each succeeding zone will be a concentric annular ring. If the diameter of the circular hole in the screen is sufficient to expose the first or central Fresnel zone, the amplitude of light at the center of the detection screen will be double what it would be if the detection screen were not obstructed. If the diameter of the circular hole in the screen is sufficient to expose two Fresnel zones, then the amplitude at the center is almost zero. That means that a Fresnel diffraction pattern can have a dark center. These patterns can be seen and measured, and correspond well to the values calculated for them.

## The Fresnel diffraction integral

According to the Rayleigh–Sommerfeld diffraction theory, the electric-field diffraction pattern at a point (*x*, *y*, *z*) is given by the following solution to the Helmholtz equation:

$E(x,y,z)={\frac {1}{i\lambda }}\iint _{-\infty }^{+\infty }E(x',y',0){\frac {e^{ikr}}{r}}{\frac {z}{r}}\left(1+{\frac {i}{kr}}\right)\,dx'dy',$

where

- $E(x',y',0)$ is the electric field at the aperture,
- $r={\sqrt {(x-x')^{2}+(y-y')^{2}+z^{2}}},$
- k is the wavenumber $2\pi /\lambda ,$
- i is the imaginary unit.

The analytical solution of this integral quickly becomes impractically complex for all but the simplest diffraction geometries. Therefore, it is usually calculated numerically.

### The Fresnel approximation

The main problem for solving the integral is the expression of *r*. First, we can simplify the algebra by introducing the substitution $\rho ^{2}=(x-x')^{2}+(y-y')^{2}.$

Substituting into the expression for *r*, we find $r={\sqrt {\rho ^{2}+z^{2}}}=z{\sqrt {1+{\frac {\rho ^{2}}{z^{2}}}}}.$

Next, by the binomial expansion, ${\sqrt {1+u}}=(1+u)^{\frac {1}{2}}=1+{\frac {u}{2}}-{\frac {u^{2}}{8}}+\cdots$

We can express r as ${\begin{aligned}r&=z{\sqrt {1+{\frac {\rho ^{2}}{z^{2}}}}}\\&=z\left[1+{\frac {\rho ^{2}}{2z^{2}}}-{\frac {1}{8}}\left({\frac {\rho ^{2}}{z^{2}}}\right)^{2}+\cdots \right]\\&=z+{\frac {\rho ^{2}}{2z}}-{\frac {\rho ^{4}}{8z^{3}}}+\cdots \end{aligned}}$

If we consider all the terms of binomial series, then there is no approximation. Let us substitute this expression in the argument of the exponential within the integral; the key to the Fresnel approximation is to assume that the third term is very small and can be ignored, and henceforth any higher orders. In order to make this possible, it has to contribute to the variation of the exponential for an almost null term. In other words, it has to be much smaller than the period of the complex exponential, i.e., $2\pi$ : $k{\frac {\rho ^{4}}{8z^{3}}}\ll 2\pi .$

Expressing *k* in terms of the wavelength, $k={\frac {2\pi }{\lambda }},$

we get the following relationship: ${\frac {\rho ^{4}}{z^{3}\lambda }}\ll 8.$

Multiplying both sides by $z^{3}/\lambda ^{3},$ we have ${\frac {\rho ^{4}}{\lambda ^{4}}}\ll 8{\frac {z^{3}}{\lambda ^{3}}},$

or, substituting the earlier expression for $\rho ^{2},$ ${\frac {1}{\lambda ^{4}}}\left[(x-x')^{2}+(y-y')^{2}\right]^{2}\ll 8{\frac {z^{3}}{\lambda ^{3}}}.$

If this condition holds true for all values of x, x', y and y', then we can ignore the third term in the Taylor expression. Furthermore, if the third term is negligible, then all terms of higher order will be even smaller, so we can ignore them as well.

For applications involving optical wavelengths, the wavelength λ is typically many orders of magnitude smaller than the relevant physical dimensions. In particular, $\lambda \ll z,$

and $\lambda \ll \rho .$

Thus, as a practical matter, the required inequality will always hold true as long as $\rho \ll z.$

We can then approximate the expression with only the first two terms: $r\approx z+{\frac {\rho ^{2}}{2z}}=z+{\frac {(x-x')^{2}+(y-y')^{2}}{2z}}.$

This equation is the **Fresnel approximation**, and the inequality stated above is a condition for the approximation's validity.

### Fresnel diffraction

The condition for validity is fairly weak, and it allows all length parameters to take comparable values, provided the aperture is small compared to the path length. For the r in the denominator we go one step further and approximate it with only the first term, $r\approx z.$ This is valid in particular if we are interested in the behaviour of the field only in a small area close to the origin, where the values of x and y are much smaller than z. In general, Fresnel diffraction is valid if the Fresnel number is approximately 1.

For Fresnel diffraction the electric field at point $(x,y,z)$ is then given by $E(x,y,z)={\frac {e^{ikz}}{i\lambda z}}\iint _{-\infty }^{+\infty }E(x',y',0)e^{{\frac {ik}{2z}}\left[(x-x')^{2}+(y-y')^{2}\right]}\,dx'dy'.$

This is the Fresnel diffraction integral; it means that, if the Fresnel approximation is valid, the propagating field is a spherical wave, originating at the aperture and moving along z. The integral modulates the amplitude and phase of the spherical wave. Analytical solution of this expression is still only possible in rare cases. For a further simplified case, valid only for much larger distances from the diffraction source, see Fraunhofer diffraction. Unlike Fraunhofer diffraction, Fresnel diffraction accounts for the curvature of the wavefront, in order to correctly calculate the relative phase of interfering waves.

## Alternative forms

### Convolution

The integral can be expressed in other ways in order to calculate it using some mathematical properties. If we define the function $h(x,y,z)={\frac {e^{ikz}}{i\lambda z}}e^{i{\frac {k}{2z}}(x^{2}+y^{2})},$

then the integral can be expressed in terms of a convolution: $E(x,y,z)=E(x,y,0)*h(x,y,z);$

in other words, we are representing the propagation using a linear-filter modeling. That is why we might call the function $h(x,y,z)$ the impulse response of free-space propagation.

### Fourier transform

Another possible way is through the Fourier transform. If in the integral we express k in terms of the wavelength: $k={\frac {2\pi }{\lambda }}$

and expand each component of the transverse displacement: ${\begin{aligned}\left(x-x'\right)^{2}&=x^{2}+x'^{2}-2xx',\\\left(y-y'\right)^{2}&=y^{2}+y'^{2}-2yy',\end{aligned}}$

then we can express the integral in terms of the two-dimensional Fourier transform. Let us use the following definition: $G(p,q)={\mathcal {F}}\{g(x,y)\}\equiv \iint _{-\infty }^{\infty }g(x,y)e^{-i2\pi (px+qy)}\,dx\,dy,$

where p and q are spatial frequencies (wavenumbers). The Fresnel integral can be expressed as ${\begin{aligned}E(x,y,z)&=\left.{\frac {e^{ikz}}{i\lambda z}}e^{i{\frac {\pi }{\lambda z}}(x^{2}+y^{2})}{\mathcal {F}}\left\{E(x',y',0)e^{i{\frac {\pi }{\lambda z}}(x'^{2}+y'^{2})}\right\}\right|_{p={\frac {x}{\lambda z}},\ q={\frac {y}{\lambda z}}}\\&=h(x,y)\cdot G(p,q){\big |}_{p={\frac {x}{\lambda z}},\ q={\frac {y}{\lambda z}}}.\end{aligned}}$

That is, first multiply the field to be propagated by a complex exponential, calculate its two-dimensional Fourier transform, replace $(p,q)$ with $\left({\tfrac {x}{\lambda z}},{\tfrac {y}{\lambda z}}\right)$ and multiply it by another factor. This expression is better than the others when the process leads to a known Fourier transform, and the connection with the Fourier transform is tightened in the linear canonical transformation, discussed below.

### Linear canonical transformation

From the point of view of the linear canonical transformation, Fresnel diffraction can be seen as a shear in the time–frequency domain, corresponding to how the Fourier transform is a rotation in the time–frequency domain.
