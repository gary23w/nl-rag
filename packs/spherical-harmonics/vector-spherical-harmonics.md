---
title: "Vector spherical harmonics"
source: https://en.wikipedia.org/wiki/Vector_spherical_harmonics
domain: spherical-harmonics
license: CC-BY-SA-4.0
tags: spherical harmonics, associated legendre polynomials, multipole expansion, wigner d-matrix
fetched: 2026-07-02
---

# Vector spherical harmonics

In mathematics, **vector spherical harmonics** (**VSH**) are an extension of the scalar spherical harmonics for use with vector fields. The components of the VSH are complex-valued functions expressed in the spherical coordinate basis vectors.

## Definition

Several conventions have been used to define the VSH. We follow that of Barrera *et al.*. Given a scalar spherical harmonic *Yℓm*(*θ*, *φ*), we define three VSH:

- $\mathbf {Y} _{\ell m}=Y_{\ell m}{\hat {\mathbf {r} }},$
- $\mathbf {\Psi } _{\ell m}=r\nabla Y_{\ell m},$
- $\mathbf {\Phi } _{\ell m}=\mathbf {r} \times \nabla Y_{\ell m},$

with ${\hat {\mathbf {r} }}$ being the unit vector along the radial direction in spherical coordinates and $\mathbf {r}$ the vector along the radial direction with the same norm as the radius, i.e., $\mathbf {r} =r{\hat {\mathbf {r} }}$ . The radial factors are included to guarantee that the dimensions of the VSH are the same as those of the ordinary spherical harmonics and that the VSH do not depend on the radial spherical coordinate.

The interest of these new vector fields is to separate the radial dependence from the angular one when using spherical coordinates, so that a vector field admits a multipole expansion

$\mathbf {E} =\sum _{\ell =0}^{\infty }\sum _{m=-\ell }^{\ell }\left(E_{\ell m}^{r}(r)\mathbf {Y} _{\ell m}+E_{\ell m}^{(1)}(r)\mathbf {\Psi } _{\ell m}+E_{\ell m}^{(2)}(r)\mathbf {\Phi } _{\ell m}\right).$

The labels on the components reflect that $E_{\ell m}^{r}$ is the radial component of the vector field, while $E_{\ell m}^{(1)}$ and $E_{\ell m}^{(2)}$ are transverse components (with respect to the radius vector $\mathbf {r}$ ).

### In physics

In physics, the vector spherical harmonics $\mathbf {Y} _{j,\ell ,s}^{m_{j}}$ are defined as spin ${\textstyle s=1}$ eigenfunctions of the angular momentum operators ${\textstyle J^{2},J_{z},L^{2}}$ , and ${\textstyle S^{2}}$ , where ${\textstyle \mathbf {J} =\mathbf {L} +\mathbf {S} }$ is the total angular momentum. They are written as $\mathbf {Y} _{j,\ell ,1}^{m_{j}}(\mathbf {k} )=\sum _{m_{\ell }\,=\,-\ell }^{+\ell }~\sum _{m_{s}\,=\,-1}^{+1}\langle j~m_{j}|\ell ~1~m_{\ell }~m_{s}\rangle Y_{\ell }^{m_{\ell }}(\mathbf {k} )\,{\hat {\mathbf {e} }}_{m_{s}},$ which are linear combinations of the scalar spherical harmonics $Y_{\ell }^{m_{\ell }}$ with the vector angular momentum basis ${\hat {\mathbf {e} }}_{\pm 1}=\mp {\frac {{\hat {\mathbf {x} }}\pm i{\hat {\mathbf {y} }}}{\sqrt {2}}},\quad {\hat {\mathbf {e} }}_{0}={\hat {\mathbf {z} }}.$ using the Clebsch-Gordan coefficients $\langle j~m_{j}|\ell ~1~m_{\ell }~m_{s}\rangle$ .

Because vector bosons such as the photon are spin-one, the vector spherical harmonics are commonly used in physics to describe vector and pseudovector interactions, such as electromagnetic transitions, in atomic and nuclear systems. They are a special ( ${\textstyle s=1}$ ) case of the spin spherical harmonics.

To derive these relations, one begins with the plane-wave expansion for plane waves with vector polarization.

## Main properties

### Symmetry

Like the scalar spherical harmonics, the VSH satisfy

${\begin{aligned}\mathbf {Y} _{\ell ,-m}&=(-1)^{m}\mathbf {Y} _{\ell m}^{*},\\\mathbf {\Psi } _{\ell ,-m}&=(-1)^{m}\mathbf {\Psi } _{\ell m}^{*},\\\mathbf {\Phi } _{\ell ,-m}&=(-1)^{m}\mathbf {\Phi } _{\ell m}^{*},\end{aligned}}$

which cuts the number of independent functions roughly in half. The star indicates complex conjugation.

### Orthogonality

The VSH are orthogonal in the usual three-dimensional way at each point $\mathbf {r}$ :

${\begin{aligned}\mathbf {Y} _{\ell m}(\mathbf {r} )\cdot \mathbf {\Psi } _{\ell m}(\mathbf {r} )&=0,\\\mathbf {Y} _{\ell m}(\mathbf {r} )\cdot \mathbf {\Phi } _{\ell m}(\mathbf {r} )&=0,\\\mathbf {\Psi } _{\ell m}(\mathbf {r} )\cdot \mathbf {\Phi } _{\ell m}(\mathbf {r} )&=0.\end{aligned}}$

They are also orthogonal in Hilbert space:

${\begin{aligned}\int \mathbf {Y} _{\ell m}\cdot \mathbf {Y} _{\ell 'm'}^{*}\,d\Omega &=\delta _{\ell \ell '}\delta _{mm'},\\\int \mathbf {\Psi } _{\ell m}\cdot \mathbf {\Psi } _{\ell 'm'}^{*}\,d\Omega &=\ell (\ell +1)\delta _{\ell \ell '}\delta _{mm'},\\\int \mathbf {\Phi } _{\ell m}\cdot \mathbf {\Phi } _{\ell 'm'}^{*}\,d\Omega &=\ell (\ell +1)\delta _{\ell \ell '}\delta _{mm'},\\\int \mathbf {Y} _{\ell m}\cdot \mathbf {\Psi } _{\ell 'm'}^{*}\,d\Omega &=0,\\\int \mathbf {Y} _{\ell m}\cdot \mathbf {\Phi } _{\ell 'm'}^{*}\,d\Omega &=0,\\\int \mathbf {\Psi } _{\ell m}\cdot \mathbf {\Phi } _{\ell 'm'}^{*}\,d\Omega &=0.\end{aligned}}$

An additional result at a single point $\mathbf {r}$ (not reported in Barrera et al, 1985) is, for all $\ell ,m,\ell ',m'$ ,

${\begin{aligned}\mathbf {Y} _{\ell m}(\mathbf {r} )\cdot \mathbf {\Psi } _{\ell 'm'}(\mathbf {r} )&=0,\\\mathbf {Y} _{\ell m}(\mathbf {r} )\cdot \mathbf {\Phi } _{\ell 'm'}(\mathbf {r} )&=0.\end{aligned}}$

### Vector multipole moments

The orthogonality relations allow one to compute the spherical multipole moments of a vector field as

${\begin{aligned}E_{\ell m}^{r}&=\int \mathbf {E} \cdot \mathbf {Y} _{\ell m}^{*}\,d\Omega ,\\E_{\ell m}^{(1)}&={\frac {1}{\ell (\ell +1)}}\int \mathbf {E} \cdot \mathbf {\Psi } _{\ell m}^{*}\,d\Omega ,\\E_{\ell m}^{(2)}&={\frac {1}{\ell (\ell +1)}}\int \mathbf {E} \cdot \mathbf {\Phi } _{\ell m}^{*}\,d\Omega .\end{aligned}}$

### The gradient of a scalar field

Given the multipole expansion of a scalar field

$\phi =\sum _{\ell =0}^{\infty }\sum _{m=-\ell }^{\ell }\phi _{\ell m}(r)Y_{\ell m}(\theta ,\phi ),$

we can express its gradient in terms of the VSH as

$\nabla \phi =\sum _{\ell =0}^{\infty }\sum _{m=-\ell }^{\ell }\left({\frac {d\phi _{\ell m}}{dr}}\mathbf {Y} _{\ell m}+{\frac {\phi _{\ell m}}{r}}\mathbf {\Psi } _{\ell m}\right).$

### Divergence

For any multipole field we have

${\begin{aligned}\nabla \cdot \left(f(r)\mathbf {Y} _{\ell m}\right)&=\left({\frac {df}{dr}}+{\frac {2}{r}}f\right)Y_{\ell m},\\\nabla \cdot \left(f(r)\mathbf {\Psi } _{\ell m}\right)&=-{\frac {\ell (\ell +1)}{r}}fY_{\ell m},\\\nabla \cdot \left(f(r)\mathbf {\Phi } _{\ell m}\right)&=0.\end{aligned}}$

By superposition we obtain the divergence of any vector field:

$\nabla \cdot \mathbf {E} =\sum _{\ell =0}^{\infty }\sum _{m=-\ell }^{\ell }\left({\frac {dE_{\ell m}^{r}}{dr}}+{\frac {2}{r}}E_{\ell m}^{r}-{\frac {\ell (\ell +1)}{r}}E_{\ell m}^{(1)}\right)Y_{\ell m}.$

We see that the component on **Φ***ℓm* is always solenoidal.

### Curl

For any multipole field we have

${\begin{aligned}\nabla \times \left(f(r)\mathbf {Y} _{\ell m}\right)&=-{\frac {1}{r}}f\mathbf {\Phi } _{\ell m},\\\nabla \times \left(f(r)\mathbf {\Psi } _{\ell m}\right)&=\left({\frac {df}{dr}}+{\frac {1}{r}}f\right)\mathbf {\Phi } _{\ell m},\\\nabla \times \left(f(r)\mathbf {\Phi } _{\ell m}\right)&=-{\frac {\ell (\ell +1)}{r}}f\mathbf {Y} _{\ell m}-\left({\frac {df}{dr}}+{\frac {1}{r}}f\right)\mathbf {\Psi } _{\ell m}.\end{aligned}}$

By superposition we obtain the curl of any vector field:

$\nabla \times \mathbf {E} =\sum _{\ell =0}^{\infty }\sum _{m=-\ell }^{\ell }\left(-{\frac {\ell (\ell +1)}{r}}E_{\ell m}^{(2)}\mathbf {Y} _{\ell m}-\left({\frac {dE_{\ell m}^{(2)}}{dr}}+{\frac {1}{r}}E_{\ell m}^{(2)}\right)\mathbf {\Psi } _{\ell m}+\left(-{\frac {1}{r}}E_{\ell m}^{r}+{\frac {dE_{\ell m}^{(1)}}{dr}}+{\frac {1}{r}}E_{\ell m}^{(1)}\right)\mathbf {\Phi } _{\ell m}\right).$

### Laplacian

The action of the Laplace operator $\Delta =\nabla \cdot \nabla$ separates as follows:

$\Delta \left(f(r)\mathbf {Z} _{\ell m}\right)=\left({\frac {1}{r^{2}}}{\frac {\partial }{\partial r}}r^{2}{\frac {\partial f}{\partial r}}\right)\mathbf {Z} _{\ell m}+f(r)\Delta \mathbf {Z} _{\ell m},$ where $\mathbf {Z} _{\ell m}=\mathbf {Y} _{\ell m},\mathbf {\Psi } _{\ell m},\mathbf {\Phi } _{\ell m}$ and

${\begin{aligned}\Delta \mathbf {Y} _{\ell m}&=-{\frac {1}{r^{2}}}(2+\ell (\ell +1))\mathbf {Y} _{\ell m}+{\frac {2}{r^{2}}}\mathbf {\Psi } _{\ell m},\\\Delta \mathbf {\Psi } _{\ell m}&={\frac {2\ell (\ell +1)}{r^{2}}}\mathbf {Y} _{\ell m}-{\frac {1}{r^{2}}}\ell (\ell +1)\mathbf {\Psi } _{\ell m},\\\Delta \mathbf {\Phi } _{\ell m}&=-{\frac {1}{r^{2}}}\ell (\ell +1)\mathbf {\Phi } _{\ell m}.\end{aligned}}$

Also note that this action becomes symmetric, i.e. the off-diagonal coefficients are equal to ${\textstyle {\frac {2}{r^{2}}}{\sqrt {\ell (\ell +1)}}}$ , for properly normalized VSH.

## Examples

$\mathbf {\Psi } _{1m}$

$\mathbf {\Psi } _{2m}$

$\mathbf {\Psi } _{3m}$

$\mathbf {\Phi } _{1m}$

$\mathbf {\Phi } _{2m}$

$\mathbf {\Phi } _{3m}$

Visualizations of the real parts of

$\ell =1,2,3$

VSHs. Click to expand.

### First vector spherical harmonics

- $\ell =0$ . ${\begin{aligned}\mathbf {Y} _{00}&={\sqrt {\frac {1}{4\pi }}}{\hat {\mathbf {r} }},\\\mathbf {\Psi } _{00}&=\mathbf {0} ,\\\mathbf {\Phi } _{00}&=\mathbf {0} .\end{aligned}}$
- $\ell =1$ . ${\begin{aligned}\mathbf {Y} _{10}&={\sqrt {\frac {3}{4\pi }}}\cos \theta \,{\hat {\mathbf {r} }},\\\mathbf {Y} _{11}&=-{\sqrt {\frac {3}{8\pi }}}e^{i\varphi }\sin \theta \,{\hat {\mathbf {r} }},\end{aligned}}$ ${\begin{aligned}\mathbf {\Psi } _{10}&=-{\sqrt {\frac {3}{4\pi }}}\sin \theta \,{\hat {\mathbf {\theta } }},\\\mathbf {\Psi } _{11}&=-{\sqrt {\frac {3}{8\pi }}}e^{i\varphi }\left(\cos \theta \,{\hat {\mathbf {\theta } }}+i\,{\hat {\mathbf {\varphi } }}\right),\end{aligned}}$ ${\begin{aligned}\mathbf {\Phi } _{10}&=-{\sqrt {\frac {3}{4\pi }}}\sin \theta \,{\hat {\mathbf {\varphi } }},\\\mathbf {\Phi } _{11}&={\sqrt {\frac {3}{8\pi }}}e^{i\varphi }\left(i\,{\hat {\mathbf {\theta } }}-\cos \theta \,{\hat {\mathbf {\varphi } }}\right).\end{aligned}}$
- $\ell =2$ . ${\begin{aligned}\mathbf {Y} _{20}&={\frac {1}{4}}{\sqrt {\frac {5}{\pi }}}\,(3\cos ^{2}\theta -1)\,{\hat {\mathbf {r} }},\\\mathbf {Y} _{21}&=-{\sqrt {\frac {15}{8\pi }}}\,\sin \theta \,\cos \theta \,e^{i\varphi }\,{\hat {\mathbf {r} }},\\\mathbf {Y} _{22}&={\frac {1}{4}}{\sqrt {\frac {15}{2\pi }}}\,\sin ^{2}\theta \,e^{2i\varphi }\,{\hat {\mathbf {r} }}.\end{aligned}}$ ${\begin{aligned}\mathbf {\Psi } _{20}&=-{\frac {3}{2}}{\sqrt {\frac {5}{\pi }}}\,\sin \theta \,\cos \theta \,{\hat {\mathbf {\theta } }},\\\mathbf {\Psi } _{21}&=-{\sqrt {\frac {15}{8\pi }}}\,e^{i\varphi }\,\left(\cos 2\theta \,{\hat {\mathbf {\theta } }}+i\cos \theta \,{\hat {\mathbf {\varphi } }}\right),\\\mathbf {\Psi } _{22}&={\sqrt {\frac {15}{8\pi }}}\,\sin \theta \,e^{2i\varphi }\,\left(\cos \theta \,{\hat {\mathbf {\theta } }}+i\,{\hat {\mathbf {\varphi } }}\right).\end{aligned}}$ ${\begin{aligned}\mathbf {\Phi } _{20}&=-{\frac {3}{2}}{\sqrt {\frac {5}{\pi }}}\sin \theta \,\cos \theta \,{\hat {\mathbf {\varphi } }},\\\mathbf {\Phi } _{21}&={\sqrt {\frac {15}{8\pi }}}\,e^{i\varphi }\,\left(i\cos \theta \,{\hat {\mathbf {\theta } }}-\cos 2\theta \,{\hat {\mathbf {\varphi } }}\right),\\\mathbf {\Phi } _{22}&={\sqrt {\frac {15}{8\pi }}}\,\sin \theta \,e^{2i\varphi }\,\left(-i\,{\hat {\mathbf {\theta } }}+\cos \theta \,{\hat {\mathbf {\varphi } }}\right).\end{aligned}}$

Expressions for negative values of m are obtained by applying the symmetry relations.

## Applications

### Electrodynamics

The VSH are especially useful in the study of multipole radiation fields. For instance, a magnetic multipole is due to an oscillating current with angular frequency $\omega$ and complex amplitude

${\hat {\mathbf {J} }}=J(r)\mathbf {\Phi } _{\ell m},$

and the corresponding electric and magnetic fields, can be written as

${\begin{aligned}{\hat {\mathbf {E} }}&=E(r)\mathbf {\Phi } _{\ell m},\\{\hat {\mathbf {B} }}&=B^{r}(r)\mathbf {Y} _{\ell m}+B^{(1)}(r)\mathbf {\Psi } _{\ell m}.\end{aligned}}$

Substituting into Maxwell equations, Gauss's law is automatically satisfied

$\nabla \cdot {\hat {\mathbf {E} }}=0,$

while Faraday's law decouples as

$\nabla \times {\hat {\mathbf {E} }}=-i\omega {\hat {\mathbf {B} }}\quad \Rightarrow \quad {\begin{cases}{\dfrac {\ell (\ell +1)}{r}}E=i\omega B^{r},\\{\dfrac {dE}{dr}}+{\dfrac {E}{r}}=i\omega B^{(1)}.\end{cases}}$

Gauss' law for the magnetic field implies

$\nabla \cdot {\hat {\mathbf {B} }}=0\quad \Rightarrow \quad {\frac {dB^{r}}{dr}}+{\frac {2}{r}}B^{r}-{\frac {\ell (\ell +1)}{r}}B^{(1)}=0,$

and Ampère–Maxwell's equation gives

$\nabla \times {\hat {\mathbf {B} }}=\mu _{0}{\hat {\mathbf {J} }}+i\mu _{0}\varepsilon _{0}\omega {\hat {\mathbf {E} }}\quad \Rightarrow \quad -{\frac {B^{r}}{r}}+{\frac {dB^{(1)}}{dr}}+{\frac {B^{(1)}}{r}}=\mu _{0}J+i\omega \mu _{0}\varepsilon _{0}E.$

In this way, the partial differential equations have been transformed into a set of ordinary differential equations.

#### Alternative definition

In many applications, vector spherical harmonics are defined as fundamental set of the solutions of vector Helmholtz equation in spherical coordinates.

In this case, vector spherical harmonics are generated by scalar functions, which are solutions of scalar Helmholtz equation with the wavevector $\mathbf {k}$ . ${\begin{array}{l}{\psi _{emn}=\cos m\varphi P_{n}^{m}(\cos \vartheta )z_{n}({k}r)}\\{\psi _{omn}=\sin m\varphi P_{n}^{m}(\cos \vartheta )z_{n}({k}r)}\end{array}}$ here $P_{n}^{m}(\cos \theta )$ are the associated Legendre polynomials, and $z_{n}({k}r)$ are any of the spherical Bessel functions.

Vector spherical harmonics are defined as:

**longitudinal harmonics**

$\mathbf {L} _{^{e}_{o}mn}=\mathbf {\nabla } \psi _{^{e}_{o}mn}$

**magnetic harmonics**

$\mathbf {M} _{^{e}_{o}mn}=\nabla \times \left(\mathbf {r} \psi _{^{e}_{o}mn}\right)$

**electric harmonics**

$\mathbf {N} _{^{e}_{o}mn}={\frac {\nabla \times \mathbf {M} _{^{e}_{o}mn}}{k}}$

Here we use harmonics real-valued angular part, where $m\geq 0$ , but complex functions can be introduced in the same way.

Let us introduce the notation $\rho =kr$ . In the component form vector spherical harmonics are written as: ${\begin{aligned}{\mathbf {M} _{emn}(k,\mathbf {r} )=\qquad {{\frac {-m}{\sin(\theta )}}\sin(m\varphi )P_{n}^{m}(\cos(\theta ))}z_{n}(\rho )\mathbf {e} _{\theta }}\\{{}-\cos(m\varphi ){\frac {dP_{n}^{m}(\cos(\theta ))}{d\theta }}}z_{n}(\rho )\mathbf {e} _{\varphi }\end{aligned}}$ ${\begin{aligned}{\mathbf {M} _{omn}(k,\mathbf {r} )=\qquad {{\frac {m}{\sin(\theta )}}\cos(m\varphi )P_{n}^{m}(\cos(\theta ))}}z_{n}(\rho )\mathbf {e} _{\theta }\\{{}-\sin(m\varphi ){\frac {dP_{n}^{m}(\cos(\theta ))}{d\theta }}z_{n}(\rho )\mathbf {e} _{\varphi }}\end{aligned}}$

${\begin{aligned}{\mathbf {N} _{emn}(k,\mathbf {r} )=\qquad {\frac {z_{n}(\rho )}{\rho }}\cos(m\varphi )n(n+1)P_{n}^{m}(\cos(\theta ))\mathbf {e} _{\mathbf {r} }}\\{{}+\cos(m\varphi ){\frac {dP_{n}^{m}(\cos(\theta ))}{d\theta }}}{\frac {1}{\rho }}{\frac {d}{d\rho }}\left[\rho z_{n}(\rho )\right]\mathbf {e} _{\theta }\\{{}-m\sin(m\varphi ){\frac {P_{n}^{m}(\cos(\theta ))}{\sin(\theta )}}}{\frac {1}{\rho }}{\frac {d}{d\rho }}\left[\rho z_{n}(\rho )\right]\mathbf {e} _{\varphi }\end{aligned}}$

${\begin{aligned}\mathbf {N} _{omn}(k,\mathbf {r} )=\qquad {\frac {z_{n}(\rho )}{\rho }}\sin(m\varphi )n(n+1)P_{n}^{m}(\cos(\theta ))\mathbf {e} _{\mathbf {r} }\\{}+\sin(m\varphi ){\frac {dP_{n}^{m}(\cos(\theta ))}{d\theta }}{\frac {1}{\rho }}{\frac {d}{d\rho }}\left[\rho z_{n}(\rho )\right]\mathbf {e} _{\theta }\\{}+{m\cos(m\varphi ){\frac {P_{n}^{m}(\cos(\theta ))}{\sin(\theta )}}}{\frac {1}{\rho }}{\frac {d}{d\rho }}\left[\rho z_{n}(\rho )\right]\mathbf {e} _{\varphi }\end{aligned}}$ There is no radial part for magnetic harmonics. For electric harmonics, the radial part decreases faster than angular, and for big $\rho$ can be neglected. We can also see that for electric and magnetic harmonics angular parts are the same up to permutation of the polar and azimuthal unit vectors, so for big $\rho$ electric and magnetic harmonics vectors are equal in value and perpendicular to each other.

Longitudinal harmonics: ${\begin{aligned}\mathbf {L} _{^{e}_{o}{mn}}(k,\mathbf {r} ){}=\qquad &{\frac {\partial }{\partial r}}z_{n}(kr)P_{n}^{m}(\cos \theta ){^{\cos }_{\sin }}{m\varphi }\mathbf {e} _{r}\\{}+{}&{\frac {1}{r}}z_{n}(kr){\frac {\partial }{\partial \theta }}P_{n}^{m}(\cos \theta ){^{\cos }_{\sin }}m\varphi \mathbf {e} _{\theta }\\{}\mp {}&{\frac {m}{r\sin \theta }}z_{n}(kr)P_{n}^{m}(\cos \theta ){^{\sin }_{\cos }}m\varphi \mathbf {e} _{\varphi }\end{aligned}}$

#### Orthogonality

The solutions of the Helmholtz vector equation obey the following orthogonality relations: ${\begin{aligned}\int _{0}^{2\pi }\int _{0}^{\pi }\mathbf {L} _{^{e}_{o}mn}\cdot \mathbf {L} _{^{e}_{o}mn}\sin \vartheta d\vartheta d\varphi &=(1+\delta _{m,0}){\frac {2\pi }{(2n+1)^{2}}}{\frac {(n+m)!}{(n-m)!}}k^{2}\left\{n\left[z_{n-1}(kr)\right]^{2}+(n+1)\left[z_{n+1}(kr)\right]^{2}\right\}\\[3pt]\int _{0}^{2\pi }\int _{0}^{\pi }\mathbf {M} _{^{e}_{o}mn}\cdot \mathbf {M} _{^{e}_{o}mn}\sin \vartheta d\vartheta d\varphi &=(1+\delta _{m,0}){\frac {2\pi }{2n+1}}{\frac {(n+m)!}{(n-m)!}}n(n+1)\left[z_{n}(kr)\right]^{2}\\[3pt]\int _{0}^{2\pi }\int _{0}^{\pi }\mathbf {N} _{^{e}_{o}mn}\cdot \mathbf {N} _{^{e}_{o}mn}\sin \vartheta d\vartheta d\varphi &=(1+\delta _{m,0}){\frac {2\pi }{(2n+1)^{2}}}{\frac {(n+m)!}{(n-m)!}}n(n+1)\left\{(n+1)\left[z_{n-1}(kr)\right]^{2}+n\left[z_{n+1}(kr)\right]^{2}\right\}\\[3pt]\int _{0}^{\pi }\int _{0}^{2\pi }\mathbf {L} _{^{e}_{o}mn}\cdot \mathbf {N} _{^{e}_{o}mn}\sin \vartheta d\vartheta d\varphi &=(1+\delta _{m,0}){\frac {2\pi }{(2n+1)^{2}}}{\frac {(n+m)!}{(n-m)!}}n(n+1)k\left\{\left[z_{n-1}(kr)\right]^{2}-\left[z_{n+1}(kr)\right]^{2}\right\}\end{aligned}}$

All other integrals over the angles between different functions or functions with different indices are equal to zero.

### Rotation and inversion

Under rotation, vector spherical harmonics are transformed through each other in the same way as the corresponding scalar spherical functions, which are generating for a specific type of vector harmonics. For example, if the generating functions are the usual spherical harmonics, then the vector harmonics will also be transformed through the Wigner D-matrices ${\hat {D}}(\alpha ,\beta ,\gamma )\mathbf {Y} _{JM}^{(s)}(\theta ,\varphi )=\sum _{M'=-J}^{J}[D_{MM'}^{(J)}(\alpha ,\beta ,\gamma )]^{*}\mathbf {Y} _{JM'}^{(s)}(\theta ,\varphi ),$ The behavior under rotations is the same for electrical, magnetic and longitudinal harmonics.

Under inversion, electric and longitudinal spherical harmonics behave in the same way as scalar spherical functions, i.e. ${\hat {I}}\mathbf {N} _{JM}(\theta ,\varphi )=(-1)^{J}\mathbf {N} _{JM}(\theta ,\varphi ),$ and magnetic ones have the opposite parity: ${\hat {I}}\mathbf {M} _{JM}(\theta ,\varphi )=(-1)^{J+1}\mathbf {M} _{JM}(\theta ,\varphi ),$

### Fluid dynamics

In the calculation of the Stokes' law for the drag that a viscous fluid exerts on a small spherical particle, the velocity distribution obeys Navier–Stokes equations neglecting inertia, i.e.,

${\begin{aligned}0&=\nabla \cdot \mathbf {v} ,\\\mathbf {0} &=-\nabla p+\eta \nabla ^{2}\mathbf {v} ,\end{aligned}}$

with the boundary conditions

$\mathbf {v} ={\begin{cases}\mathbf {0} &r=a,\\-\mathbf {U} _{0}&r\to \infty .\end{cases}}$

where **U** is the relative velocity of the particle to the fluid far from the particle. In spherical coordinates this velocity at infinity can be written as

$\mathbf {U} _{0}=U_{0}\left(\cos \theta \,{\hat {\mathbf {r} }}-\sin \theta \,{\hat {\mathbf {\theta } }}\right)=U_{0}\left(\mathbf {Y} _{10}+\mathbf {\Psi } _{10}\right).$

The last expression suggests an expansion in spherical harmonics for the liquid velocity and the pressure

${\begin{aligned}p&=p(r)Y_{10},\\\mathbf {v} &=v^{r}(r)\mathbf {Y} _{10}+v^{(1)}(r)\mathbf {\Psi } _{10}.\end{aligned}}$

Substitution in the Navier–Stokes equations produces a set of ordinary differential equations for the coefficients.

## Integral relations

Here the following definitions are used:

${\begin{aligned}Y_{emn}&=\cos m\varphi P_{n}^{m}(\cos \theta )\\Y_{omn}&=\sin m\varphi P_{n}^{m}(\cos \theta )\end{aligned}}$

$\mathbf {X} _{^{e}_{o}mn}\left({\frac {\mathbf {k} }{k}}\right)=\nabla \times \left(\mathbf {k} Y_{^{o}_{e}mn}\left({\frac {\mathbf {k} }{k}}\right)\right)$

$\mathbf {Z} _{^{o}_{e}mn}\left({\frac {\mathbf {k} }{k}}\right)=i{\frac {\mathbf {k} }{k}}\times \mathbf {X} _{^{e}_{o}mn}\left({\frac {\mathbf {k} }{k}}\right)$ In case, when instead of $z_{n}$ are spherical Bessel functions, with help of plane wave expansion one can obtain the following integral relations:

$\mathbf {N} _{pmn}^{(1)}(k,\mathbf {r} )={\frac {i^{-n}}{4\pi }}\int \mathbf {Z} _{pmn}\left({\frac {\mathbf {k} }{k}}\right)e^{i\mathbf {k} \cdot \mathbf {r} }d\Omega _{k}$

$\mathbf {M} _{pmn}^{(1)}(k,\mathbf {r} )={\frac {i^{-n}}{4\pi }}\int \mathbf {X} _{pmn}\left({\frac {\mathbf {k} }{k}}\right)e^{i\mathbf {k} \cdot \mathbf {r} }d\Omega _{k}$

In case, when $z_{n}$ are spherical Hankel functions, one should use the different formulae. For vector spherical harmonics the following relations are obtained:

$\mathbf {M} _{pmn}^{(3)}(k,\mathbf {r} )={\frac {i^{-n}}{2\pi k}}\iint _{-\infty }^{\infty }dk_{\|}{\frac {e^{i\left(k_{x}x+k_{y}y\pm k_{z}z\right)}}{k_{z}}}\mathbf {X} _{pmn}\left({\frac {\mathbf {k} }{k}}\right)$

$\mathbf {N} _{pmn}^{(3)}(k,\mathbf {r} )={\frac {i^{-n}}{2\pi k}}\iint _{-\infty }^{\infty }dk_{\|}{\frac {e^{i\left(k_{x}x+k_{y}y\pm k_{z}z\right)}}{k_{z}}}\mathbf {Z} _{pmn}\left({\frac {\mathbf {k} }{k}}\right)$ where ${\textstyle k_{z}={\sqrt {k^{2}-k_{x}^{2}-k_{y}^{2}}}}$ , index $(3)$ means, that spherical Hankel functions are used.
