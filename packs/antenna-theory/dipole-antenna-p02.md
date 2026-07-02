---
title: "Dipole antenna (part 2/2)"
source: https://en.wikipedia.org/wiki/Dipole_antenna
domain: antenna-theory
license: CC-BY-SA-4.0
tags: dipole antenna, radiation pattern, antenna aperture, monopole antenna
fetched: 2026-07-02
part: 2/2
---

## Hertzian dipole

The *Hertzian dipole* or *elementary doublet* refers to a theoretical construction, rather than a physical antenna design: It is an idealized tiny segment of conductor carrying a RF current with constant amplitude and direction along its entire (short) length; a real antenna can be modeled as the combination of many Hertzian dipoles laid end-to-end.

The Hertzian dipole may be defined as a finite oscillating current (in a specified direction) of $\ I\ e^{i\omega t}\$ over a tiny or infinitesimal length $\ \delta \ell \$ at a specified position. The solution of the fields from a Hertzian dipole can be used as the basis for analytical or numerical calculation of the radiation from more complex antenna geometries (such as practical dipoles) by forming the superposition of fields from a large number of Hertzian dipoles comprising the current pattern of the actual antenna. As a function of position, taking the elementary current elements $\ I\!\left(\mathbf {r} \right)\ ,$ multiplied by infinitesimal lengths $\ \delta \ell \ ,$ the resulting field pattern then reduces to an integral over the path of an antenna conductor (modeled as a thin wire).

For the following derivation, we shall take the current to be in the $\ z\$ direction, centered at the origin where $\ x=y=z=0\ ,$ with the sinusoidal time dependence $\ e^{i\omega t}\$ for all quantities being understood. The simplest approach is to use the calculation of the vector potential $\ \mathbf {A} \!\left(\mathbf {r} \right)\$ using the formula for the retarded potential. Although the value of $\ \mathbf {A} \$ is not unique, we shall constrain it by adopting the Lorenz gauge, and assuming sinusoidal current at radian frequency $\ \omega \$ the retardation of the field is converted just into a phase factor $\ e^{-ikr}\ ,$ where the wave number ${\textstyle \ k={\frac {\omega }{\ c\ }}\ }$ in free space and $\ r\$ is the linear distance between the point being considered to the origin (where we assumed the current source to be), so $\ r\equiv \left|\ \mathbf {r} \ \right|~.$ This results in a vector potential $\ \mathbf {A} \$ at position $\ \mathbf {r} \$ due to that current element only, which we find is purely in the $\ z\$ direction (the direction of the current):

$\mathbf {A} \!\left(\mathbf {r} \right)=I\ \delta \ell \ {\frac {\mu _{0}}{\ 4\pi r\ }}\ e^{-ikr}\ {\hat {\mathbf {z} }}\$

where $\ \mu _{0}\$ is the permeability of free space. Then using

$\ \mu \mathbf {H} =\mathbf {B} =\nabla \times \mathbf {A} \$

we can solve for the magnetic field $\ \mathbf {H} \ ,$ and from that (dependent on us having chosen the Lorenz gauge) the electric field $\ \mathbf {E} \$ using

$\mathbf {E} ={\frac {\ \nabla \times \mathbf {H} \ }{i\omega \epsilon }}$

In spherical coordinates we find that the magnetic field $\ \mathbf {H} \$ has only a component in the $\ \phi \$ direction:

$\mathbf {H} =H_{\phi }\ {\hat {\boldsymbol {\phi }}}$

where

$H_{\phi }=i{\frac {\ I\ \delta \ell \ }{4\pi }}\left({\frac {\ k\ }{r}}-{\frac {i}{\ r^{2}}}\right)\ e^{-ikr}\ \sin \theta \ ,$

while the electric field has components both in the $\ \theta \$ and $\ r\$ directions:

$\mathbf {E} =E_{\theta }\ {\hat {\boldsymbol {\theta }}}+E_{r}\ {\hat {\mathbf {r} }}$

where

${\begin{aligned}E_{\theta }&=i{\frac {\ \zeta _{0}\ I\ \delta \ell \ }{4\pi }}\left({\frac {\ k\ }{r}}-{\frac {i}{\ r^{2}}}-{\frac {1}{\ k\ r^{3}}}\right)\ e^{-ikr}\ \sin \theta \ ,\\[2pt]E_{r}&={\frac {\ \zeta _{0}\ I\ \delta \ell \ }{2\pi }}\left({\frac {1}{\ r^{2}\ }}-{\frac {i}{\ kr^{3}}}\right)\ e^{-ikr}\ \cos \theta \ ,\end{aligned}}$

with $\ \zeta _{0}\equiv {\sqrt {{\frac {\ \mu _{0}\ }{\epsilon _{0}}}\;}}\$ is the impedance of free space.

This solution includes near field terms that are very strong near the source but which are not radiated. As seen in the accompanying animation, the $\ \mathbf {E} \$ and $\ \mathbf {H} \$ fields very close to the source are almost 90° out of phase, thus contributing very little to the Poynting vector by which radiated flux is computed. The near field solution for an antenna element (from the integral using this formula over the length of that element) is the field that can be used to compute the mutual impedance between it and another nearby element.

For computation of the far field radiation pattern, the above equations are simplified as only the ${\textstyle \ {\frac {\ 1\ }{r}}\ }$ terms remain significant:

${\begin{aligned}H_{\phi }&=i{\frac {\ I\ \delta \ell \ k\ }{4\pi r}}\ e^{-ikr}\ \sin \theta \ ,\\[2pt]E_{\theta }&=i{\frac {\ \zeta _{0}\ I\ \delta \ell \ k\ }{4\pi r}}\ e^{-ikr}\ \sin \theta ~.\end{aligned}}$

The far-field pattern is thus seen to consist of a transverse electromagnetic (TEM) wave, with electric and magnetic fields at right angles to each other and at right angles to the direction of propagation (the direction of $\ \mathbf {r} \$ , as we assumed the source to be at the origin). The electric polarization, in the $\theta$ direction, is coplanar with the source current (in the $\ z\$ direction), while the magnetic field is at right angles to that, in the $\ \phi \$ direction. It can be seen from these equations, and also in the animation, that the fields at these distances are exactly *in phase*. Both fields fall according to ${\textstyle \ {\frac {\ 1\ }{r}}\ ,}$ with the power thus falling according to ${\textstyle \ {\frac {1}{\ r^{2}}}\ }$ as dictated by the inverse square law.

### Radiation resistance

If one knows the far field radiation pattern due to a given antenna current, then it is possible to compute the radiation resistance directly. For the above fields due to the Hertzian dipole, we can compute the power flux according to the Poynting vector, resulting in a power (as averaged over one cycle) of:

$\langle \mathbf {S} \rangle ={\frac {\ 1\ }{2}}{\mathcal {R_{e}}}\left\{\ \mathbf {E} \times \mathbf {H} ^{*}\ \right\}=\langle S_{\mathsf {r}}\rangle \ {\hat {\mathbf {r} }}+\langle S_{\mathsf {\phi }}\rangle \ {\hat {\boldsymbol {\phi }}}~.$

With increasing $\ r\$ the $\ \langle S_{\mathsf {\phi }}\rangle \$ becomes insignificantly small compared to the $\ \langle S_{\mathsf {r}}\rangle \$ component. Although not required, it is easiest to only work with the asymptotic value that $\ \langle S_{\mathsf {r}}\rangle \$ approaches at a large $\ r\$ using the simpler far-field expressions for $\ \mathbf {E} \$ and $\ \mathbf {H} ~.$ Consider a large sphere surrounding the source with a radius $\ r~.$ We find the power per unit area crossing the surface of that sphere in the $\ {\hat {\mathbf {r} }}\$ direction is:

$\left\langle S_{\mathsf {r}}\right\rangle ={\frac {\ \zeta _{0}\ }{2}}\ \left({\frac {\ \left|I\right|\ k\ \delta \ell \ }{4\pi r}}\ \sin \theta \right)^{2}\$

Integration of this flux over the complete sphere results in:

${\begin{aligned}P_{\mathsf {net}}&=\int _{0}^{2\pi }\!\!\int _{0}^{\pi }\left|\langle S_{\mathsf {r}}\rangle \right|\ r^{2}\sin \theta \ \mathrm {d} {\phi }\ \mathrm {d} \theta \\&={\tfrac {\ 1\ }{2}}\zeta _{0}\ \left({\frac {\ \left|I\right|\ k\ \delta \ell \ }{4\pi }}\right)^{2}\int _{0}^{2\pi }\!\!\int _{0}^{\pi }\sin ^{3}\theta \ \mathrm {d} {\phi }\ \mathrm {d} \theta \\&={\frac {\zeta _{0}}{\ 12\pi \ }}\left(\left|I\right|\ k\ \delta \ell \right)^{2}={\frac {\ \pi \ }{3}}\zeta _{0}\ \left(\left|I\right|{\frac {\ \delta \ell \ }{\lambda }}\right)^{2}\end{aligned}}$

where $\ \lambda =2\pi /k\$ is the free space wavelength corresponding to the radian frequency $\ \omega ~.$ By definition, the radiation resistance $R_{\text{rad}}$ times the average of the square of the current ${\textstyle \ {\tfrac {\ 1\ }{2}}\left|\ I\ \right|^{2}\ }$ is the net power radiated due to that current, so equating the above to ${\textstyle \ {\tfrac {\ 1\ }{2}}\left|I\right|^{2}R_{\text{rad}}\ }$ we find:

$R_{\text{rad}}={\tfrac {\ 2\ \pi \ }{3}}\zeta _{0}\ \left({\frac {\ \delta \ell \ }{\lambda }}\right)^{2}~.$

This method can be used to compute the radiation resistance for any antenna whose far-field radiation pattern has been found in terms of a specific antenna current. If ohmic losses in the conductors are neglected, the radiation resistance (considered relative to the feedpoint) is identical to the resistive (real) component of the feedpoint impedance. Unfortunately, this exercise tells us nothing about the reactive (imaginary) component of feedpoint impedance, whose calculation is considered below.

### Directive gain

Using the above expression for the radiated flux given by the Poynting vector, it is also possible to compute the directive gain of the Hertzian dipole. Dividing the total power computed above by $4\pi r^{2}$ we can find the flux averaged over all directions $\ P_{\text{avg}}\$ as

$\ P_{\text{avg}}={\frac {P_{\text{net}}}{\ 4\pi \ r^{2}}}={\frac {\zeta _{0}}{\ 48\pi ^{2}\ r^{2}}}k^{2}\ \left|I\right|^{2}\ \left(\delta \ell \right)^{2}~.$

Dividing the flux radiated in a *particular* direction by $\ P_{\text{avg}}\$ we obtain the directive gain $\ \operatorname {\mathsf {G}} \left(\theta \right)\ :$

$\ \operatorname {\mathsf {G}} \left(\theta \right)={\frac {\ \left\langle \mathbf {S} _{\mathsf {r}}\right\rangle \ }{P_{\text{avg}}}}={\tfrac {\ 3\ }{2}}\sin ^{2}\theta \$

The commonly quoted antenna "gain", meaning the peak value of the gain pattern (radiation pattern), is found to be 1.5~1.76 dBi, lower than practically any other antenna configuration.

### Comparison with the short dipole

The Hertzian dipole is *similar to* but differs from the short dipole, discussed above. In both cases the conductor is very short compared to a wavelength, so the standing wave pattern present on a half-wave dipole (for instance) is absent. However, with the Hertzian dipole we specified that the current along that conductor is *constant* over its short length. This makes the Hertzian dipole useful for analysis of more complex antenna configurations, where every infinitesimal section of that *real* antenna's conductor can be modeled as a Hertzian dipole with the current found to be flowing in that real antenna.

However a short conductor fed with a RF voltage will not have a uniform current even along that short range. Rather, a short dipole in real life has a current equal to the feedpoint current at the feedpoint but falling linearly to zero over the length of that short conductor. By placing a *capacitive hat*, such as a metallic ball, at the end of the conductor, it is possible for its self capacitance to absorb the current from the conductor and better approximate the constant current assumed for the Hertzian dipole. But again, the Hertzian dipole is meant only as a theoretical construct for antenna analysis.

The short dipole, with a feedpoint current of $\ I_{0}\ ,$ has an *average* current over each conductor of only ${\textstyle \ {\tfrac {\ 1\ }{2}}\ I_{0}~.}$ The above field equations for the Hertzian dipole of length $\ \delta \ell \$ would then predict the *actual* fields for a short dipole using that effective current ${\textstyle \ I={\tfrac {\ 1\ }{2}}\ I_{0}~.}$ This would result in a power measured in the far field of *one quarter* that given by the above equation for the magnitude of the Poynting vector $\ \langle S_{\mathsf {r}}\rangle \$ if we had assumed an element current of $\ I_{0}~.$ Consequently, it can be seen that the radiation resistance computed for the short dipole is one quarter of that computed above for the Hertzian dipole. But their radiation patterns (and gains) are otherwise identical.


## Detailed calculation of dipole feedpoint impedance

The impedance seen at the feedpoint of a dipole of various lengths has been plotted above, in terms of the real (resistive) component Rdipole and the imaginary (reactive) component j Xdipole of that impedance. For the case of an antenna with perfect conductors (no Ohmic loss), Rdipole is identical to the radiation resistance, which can more easily be computed from the total power in the far-field radiation pattern for a given applied current as we showed for the short dipole. The calculation of Xdipole is more difficult.

### Induced EMF method

Using the *induced EMF method* closed form expressions are obtained for both components of the feedpoint impedance; such results are plotted above. The solution depends on an assumption for the form of the current distribution along the antenna conductors. For wavelength-to-element diameter ratios greater than about 60, the current distribution along each antenna element of length ⁠1/ 2 ⁠ L is very well approximated as having the form of the sine function at points along the antenna z, with the current reaching zero at the elements' ends, where *z* = ⁠±+1/2⁠ *L* , as follows:

$\ I(z)=A\sin {\Bigl (}\ k\left({\tfrac {\ 1\ }{2}}\ L-\left|z\right|\right)\ {\Bigr )}\ ,$

where k is the wavenumber given by *k* = ⁠2 *π*/ *λ* ⁠ = ⁠2 *π f*/ *c* ⁠ , and the amplitude A is set to match a specified driving point current at *z* = 0 .

In cases where an approximately sinusoidal current distribution can be assumed, this method solves for the driving point impedance in closed form using the cosine and sine integral functions Si(*x*) and Ci(*x*) . For a dipole of total length L , the resistive and reactive components of the driving point impedance can be expressed as:

${\begin{aligned}R_{\mathsf {dipole}}={\frac {\zeta _{0}}{\ 2\pi \sin ^{2}\left({\tfrac {1}{2}}kL\right)\ }}{\Biggl \{}\ \gamma _{e}+\ln(kL)-\operatorname {Ci} (kL)+{}&{\tfrac {1}{2}}\sin(kL)\,{\Bigl [}+\operatorname {Si} (2kL)-2\operatorname {Si} (kL)\ {\Bigr ]}\\{}+{}&{\tfrac {1}{2}}\cos(kL)\,{\Big [}+\operatorname {Ci} (2kL)-2\operatorname {Ci} (kL)+\gamma _{e}+\ln \left({\tfrac {1}{2}}kL\right)\ {\Bigr ]}\ {\Bigg \}}\ ,\\X_{\mathsf {dipole}}={\frac {\zeta _{0}}{\ 2\pi \sin ^{2}\left({\tfrac {1}{2}}kL\right)\ }}{\Biggl \{}{}+\operatorname {Si} (kL)+{}&{\tfrac {1}{2}}\cos(kL)\,{\Bigl [}-\operatorname {Si} (2kL)+2\operatorname {Si} (kL)\ {\Bigr ]}\\{}+{}&{\tfrac {1}{2}}\sin(kL)\,{\Bigl [}+\operatorname {Ci} (2kL)-2\operatorname {Ci} (kL)+\operatorname {Ci} \left({\tfrac {\;2ka^{2}\ }{L}}\right)\ {\Bigr ]}\ {\Biggr \}}\ ,\end{aligned}}$

where a is the radius of the conductors, k is again the wavenumber as defined above, ζ0 is the impedance of empty space, which very nearly the same as impedance of air: ζ0 ≈ 377 Ω , and $\ \gamma _{e}=0.57721566\ \ldots \$ is Euler's constant. There is an equivalent alternate form favored by some authors that uses a different function, Cin .

### Integral methods

The induced EMF method is dependent on the assumption of a sinusoidal current distribution, delivering an accuracy better than about 10% as long as the wavelength-to-element diameter ratio is greater than about 60. However, for yet larger conductors numerical solutions are required which solve for the conductor's current distribution (rather than *assuming* a sinusoidal pattern). This can be based on approximating solutions for either *Pocklington's integrodifferential equation* or the *Hallén integral equation*. These approaches also have greater generality, not being limited to linear conductors.

Numerical solution of either is performed using the *moment method solution* which requires expansion of that current into a set of basis functions; one simple (but not the best) choice, for instance, is to break up the conductor into N segments with a constant current assumed along each. After setting an appropriate weighting function the cost may be minimized through the inversion of a *N*×*N* matrix. Determination of each matrix element requires at least one double integration involving the weighting functions, which may become computationally intensive. These are simplified if the weighting functions are simply delta functions, which corresponds to fitting the boundary conditions for the current along the conductor at only N discrete points. Then the *N*×*N* matrix must be inverted, which is also computationally intensive as N increases. In one simple example, Balanis (2011) performs this computation to find the antenna impedance with different N using Pocklington's method, and finds that with *N* > 60 the solutions approach their limiting values to within a few percent.
