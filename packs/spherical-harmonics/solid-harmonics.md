---
title: "Solid harmonics"
source: https://en.wikipedia.org/wiki/Solid_harmonics
domain: spherical-harmonics
license: CC-BY-SA-4.0
tags: spherical harmonics, associated legendre polynomials, multipole expansion, wigner d-matrix
fetched: 2026-07-02
---

# Solid harmonics

In physics and mathematics, the **solid harmonics** are solutions of the Laplace equation in spherical polar coordinates, assumed to be (smooth) functions $\mathbb {R} ^{3}\to \mathbb {C}$ . There are two kinds: the *regular solid harmonics* $R_{\ell }^{m}(\mathbf {r} )$ , which are well-defined at the origin and the *irregular solid harmonics* $I_{\ell }^{m}(\mathbf {r} )$ , which are singular at the origin. Both sets of functions play an important role in potential theory, and are obtained by rescaling spherical harmonics appropriately: $R_{\ell }^{m}(\mathbf {r} )\equiv {\sqrt {\frac {4\pi }{2\ell +1}}}\;r^{\ell }Y_{\ell }^{m}(\theta ,\varphi )$ $I_{\ell }^{m}(\mathbf {r} )\equiv {\sqrt {\frac {4\pi }{2\ell +1}}}\;{\frac {Y_{\ell }^{m}(\theta ,\varphi )}{r^{\ell +1}}}$

## Derivation, relation to spherical harmonics

Introducing r, θ, and φ for the spherical polar coordinates of the 3-vector **r**, and assuming that $\Phi$ is a (smooth) function $\mathbb {R} ^{3}\to \mathbb {C}$ , we can write the Laplace equation in the following form $\nabla ^{2}\Phi (\mathbf {r} )=\left({\frac {1}{r}}{\frac {\partial ^{2}}{\partial r^{2}}}r-{\frac {{\hat {L}}^{2}}{r^{2}}}\right)\Phi (\mathbf {r} )=0,\qquad \mathbf {r} \neq \mathbf {0} ,$ where *L*2 is the square of the *nondimensional* angular momentum operator, $\mathbf {\hat {L}} =-i\,(\mathbf {r} \times \mathbf {\nabla } ).$

It is known that spherical harmonics *Y**m* *ℓ* are eigenfunctions of *L*2: ${\hat {L}}^{2}Y_{\ell }^{m}\equiv \left[{\hat {L}}_{x}^{2}+{\hat {L}}_{y}^{2}+{\hat {L}}_{z}^{2}\right]Y_{\ell }^{m}=\ell (\ell +1)Y_{\ell }^{m}.$

Substitution of Φ(**r**) = *F*(*r*) *Y**m* *ℓ* into the Laplace equation gives, after dividing out the spherical harmonic function, the following radial equation and its general solution,

${\frac {1}{r}}{\frac {\partial ^{2}}{\partial r^{2}}}rF(r)={\frac {\ell (\ell +1)}{r^{2}}}F(r)\Longrightarrow F(r)=Ar^{\ell }+Br^{-\ell -1}.$

The particular solutions of the total Laplace equation are **regular solid harmonics**: $R_{\ell }^{m}(\mathbf {r} )\equiv {\sqrt {\frac {4\pi }{2\ell +1}}}\;r^{\ell }Y_{\ell }^{m}(\theta ,\varphi ),$ and **irregular solid harmonics**: $I_{\ell }^{m}(\mathbf {r} )\equiv {\sqrt {\frac {4\pi }{2\ell +1}}}\;{\frac {Y_{\ell }^{m}(\theta ,\varphi )}{r^{\ell +1}}}.$ The regular solid harmonics correspond to harmonic homogeneous polynomials, i.e. homogeneous polynomials which are solutions to Laplace's equation.

### Racah's normalization

Racah's normalization (also known as Schmidt's semi-normalization) is applied to both functions $\int _{0}^{\pi }\sin \theta \,d\theta \int _{0}^{2\pi }d\varphi \;R_{\ell }^{m}(\mathbf {r} )^{*}\;R_{\ell }^{m}(\mathbf {r} )={\frac {4\pi }{2\ell +1}}r^{2\ell }$ (and analogously for the irregular solid harmonic) instead of normalization to unity. This is convenient because in many applications the Racah normalization factor appears unchanged throughout the derivations.

## Addition theorems

The translation of the regular solid harmonic gives a finite expansion, $R_{\ell }^{m}(\mathbf {r} +\mathbf {a} )=\sum _{\lambda =0}^{\ell }{\binom {2\ell }{2\lambda }}^{1/2}\sum _{\mu =-\lambda }^{\lambda }R_{\lambda }^{\mu }(\mathbf {r} )R_{\ell -\lambda }^{m-\mu }(\mathbf {a} )\;\langle \lambda ,\mu ;\ell -\lambda ,m-\mu |\ell m\rangle ,$ where the Clebsch–Gordan coefficient is given by $\langle \lambda ,\mu ;\ell -\lambda ,m-\mu |\ell m\rangle ={\binom {\ell +m}{\lambda +\mu }}^{1/2}{\binom {\ell -m}{\lambda -\mu }}^{1/2}{\binom {2\ell }{2\lambda }}^{-1/2}.$

The similar expansion for irregular solid harmonics gives an infinite series, $I_{\ell }^{m}(\mathbf {r} +\mathbf {a} )=\sum _{\lambda =0}^{\infty }{\binom {2\ell +2\lambda +1}{2\lambda }}^{1/2}\sum _{\mu =-\lambda }^{\lambda }R_{\lambda }^{\mu }(\mathbf {r} )I_{\ell +\lambda }^{m-\mu }(\mathbf {a} )\;\langle \lambda ,\mu ;\ell +\lambda ,m-\mu |\ell m\rangle$ with $|r|\leq |a|\,$ . The quantity between pointed brackets is again a Clebsch-Gordan coefficient, $\langle \lambda ,\mu ;\ell +\lambda ,m-\mu |\ell m\rangle =(-1)^{\lambda +\mu }{\binom {\ell +\lambda -m+\mu }{\lambda +\mu }}^{1/2}{\binom {\ell +\lambda +m-\mu }{\lambda -\mu }}^{1/2}{\binom {2\ell +2\lambda +1}{2\lambda }}^{-1/2}.$

The addition theorems were proved in different manners by several authors.

## Complex form

The regular solid harmonics are homogeneous, polynomial solutions to the Laplace equation $\Delta R=0$ . Separating the indeterminate z and writing ${\textstyle R=\sum _{a}p_{a}(x,y)z^{a}}$ , the Laplace equation is easily seen to be equivalent to the recursion formula $p_{a+2}={\frac {-\left(\partial _{x}^{2}+\partial _{y}^{2}\right)p_{a}}{\left(a+2\right)\left(a+1\right)}}$ so that any choice of polynomials $p_{0}(x,y)$ of degree $\ell$ and $p_{1}(x,y)$ of degree $\ell -1$ gives a solution to the equation. One particular basis of the space of homogeneous polynomials (in two variables) of degree k is $\left\{(x^{2}+y^{2})^{m}(x\pm iy)^{k-2m}\mid 0\leq m\leq k/2\right\}$ . Note that it is the (unique up to normalization) basis of eigenvectors of the rotation group $SO(2)$ : The rotation $\rho _{\alpha }$ of the plane by $\alpha \in [0,2\pi ]$ acts as multiplication by $e^{\pm i(k-2m)\alpha }$ on the basis vector $(x^{2}+y^{2})^{m}(x+iy)^{k-2m}$ .

If we combine the degree $\ell$ basis and the degree $\ell -1$ basis with the recursion formula, we obtain a basis of the space of harmonic, homogeneous polynomials (in three variables this time) of degree $\ell$ consisting of eigenvectors for $SO(2)$ (note that the recursion formula is compatible with the $SO(2)$ -action because the Laplace operator is rotationally invariant). These are the complex solid harmonics: ${\begin{aligned}R_{\ell }^{\pm \ell }&=(x\pm iy)^{\ell }z^{0}\\R_{\ell }^{\pm (\ell -1)}&=(x\pm iy)^{\ell -1}z^{1}\\R_{\ell }^{\pm (\ell -2)}&=(x^{2}+y^{2})(x\pm iy)^{\ell -2}z^{0}+{\frac {-(\partial _{x}^{2}+\partial _{y}^{2})\left((x^{2}+y^{2})(x\pm iy)^{\ell -2}\right)}{1\cdot 2}}z^{2}\\R_{\ell }^{\pm (\ell -3)}&=(x^{2}+y^{2})(x\pm iy)^{\ell -3}z^{1}+{\frac {-(\partial _{x}^{2}+\partial _{y}^{2})\left((x^{2}+y^{2})(x\pm iy)^{\ell -3}\right)}{2\cdot 3}}z^{3}\\R_{\ell }^{\pm (\ell -4)}&=(x^{2}+y^{2})^{2}(x\pm iy)^{\ell -4}z^{0}+{\frac {-(\partial _{x}^{2}+\partial _{y}^{2})\left((x^{2}+y^{2})^{2}(x\pm iy)^{\ell -4}\right)}{1\cdot 2}}z^{2}+{\frac {(\partial _{x}^{2}+\partial _{y}^{2})^{2}\left((x^{2}+y^{2})^{2}(x\pm iy)^{\ell -4}\right)}{1\cdot 2\cdot 3\cdot 4}}z^{4}\\R_{\ell }^{\pm (\ell -5)}&=(x^{2}+y^{2})^{2}(x\pm iy)^{\ell -5}z^{1}+{\frac {-(\partial _{x}^{2}+\partial _{y}^{2})\left((x^{2}+y^{2})^{2}(x\pm iy)^{\ell -5}\right)}{2\cdot 3}}z^{3}+{\frac {(\partial _{x}^{2}+\partial _{y}^{2})^{2}\left((x^{2}+y^{2})^{2}(x\pm iy)^{\ell -5}\right)}{2\cdot 3\cdot 4\cdot 5}}z^{5}\\&\;\,\vdots \end{aligned}}$ and in general $R_{\ell }^{\pm m}={\begin{cases}\sum _{k}(\partial _{x}^{2}+\partial _{y}^{2})^{k}\left((x^{2}+y^{2})^{(\ell -m)/2}(x\pm iy)^{m}\right){\frac {(-1)^{k}z^{2k}}{(2k)!}}&\ell -m{\text{ is even}}\\\sum _{k}(\partial _{x}^{2}+\partial _{y}^{2})^{k}\left((x^{2}+y^{2})^{(\ell -1-m)/2}(x\pm iy)^{m}\right){\frac {(-1)^{k}z^{2k+1}}{(2k+1)!}}&\ell -m{\text{ is odd}}\end{cases}}$ for $0\leq m\leq \ell$ .

Plugging in spherical coordinates $x=r\cos(\theta )\sin(\varphi )$ , $y=r\sin(\theta )\sin(\varphi )$ , $z=r\cos(\varphi )$ and using $x^{2}+y^{2}=r^{2}\sin(\varphi )^{2}=r^{2}(1-\cos(\varphi )^{2})$ one finds the usual relationship to spherical harmonics $R_{\ell }^{m}=r^{\ell }e^{im\phi }P_{\ell }^{m}(\cos(\vartheta ))$ with a polynomial $P_{\ell }^{m}$ , which is (up to normalization) the associated Legendre polynomial, and so $R_{\ell }^{m}=r^{\ell }Y_{\ell }^{m}(\theta ,\varphi )$ (again, up to the specific choice of normalization).

## Real form

By a simple linear combination of solid harmonics of ±*m* these functions are transformed into real functions, i.e. functions $\mathbb {R} ^{3}\to \mathbb {R}$ . The real regular solid harmonics, expressed in Cartesian coordinates, are real-valued homogeneous polynomials of order $\ell$ in *x*, *y*, *z*. The explicit form of these polynomials is of some importance. They appear, for example, in the form of spherical atomic orbitals and real multipole moments. The explicit Cartesian expression of the real regular harmonics will now be derived.

### Linear combination

We write in agreement with the earlier definition $R_{\ell }^{m}(r,\theta ,\varphi )=(-1)^{(m+|m|)/2}\;r^{\ell }\;\Theta _{\ell }^{|m|}(\cos \theta )e^{im\varphi },\qquad -\ell \leq m\leq \ell ,$ with $\Theta _{\ell }^{m}(\cos \theta )\equiv \left[{\frac {(\ell -m)!}{(\ell +m)!}}\right]^{1/2}\,\sin ^{m}\theta \,{\frac {d^{m}P_{\ell }(\cos \theta )}{d\cos ^{m}\theta }},\qquad m\geq 0,$ where $P_{\ell }(\cos \theta )$ is a Legendre polynomial of order ℓ. The m dependent phase is known as the Condon–Shortley phase.

The following expression defines the real regular solid harmonics: ${\begin{pmatrix}C_{\ell }^{m}\\S_{\ell }^{m}\end{pmatrix}}\equiv {\sqrt {2}}\;r^{\ell }\;\Theta _{\ell }^{m}{\begin{pmatrix}\cos m\varphi \\\sin m\varphi \end{pmatrix}}={\frac {1}{\sqrt {2}}}{\begin{pmatrix}(-1)^{m}&\quad 1\\-(-1)^{m}i&\quad i\end{pmatrix}}{\begin{pmatrix}R_{\ell }^{m}\\R_{\ell }^{-m}\end{pmatrix}},\qquad m>0.$ and for *m* = 0: $C_{\ell }^{0}\equiv R_{\ell }^{0}.$ Since the transformation is by a unitary matrix the normalization of the real and the complex solid harmonics is the same.

### *z*-dependent part

Upon writing *u* = cos *θ* the m-th derivative of the Legendre polynomial can be written as the following expansion in u ${\frac {d^{m}P_{\ell }(u)}{du^{m}}}=\sum _{k=0}^{\left\lfloor (\ell -m)/2\right\rfloor }\gamma _{\ell k}^{(m)}\;u^{\ell -2k-m}$ with $\gamma _{\ell k}^{(m)}=(-1)^{k}2^{-\ell }{\binom {\ell }{k}}{\binom {2\ell -2k}{\ell }}{\frac {(\ell -2k)!}{(\ell -2k-m)!}}.$ Since *z* = *r* cos *θ* it follows that this derivative, times an appropriate power of r, is a simple polynomial in z, $\Pi _{\ell }^{m}(z)\equiv r^{\ell -m}{\frac {d^{m}P_{\ell }(u)}{du^{m}}}=\sum _{k=0}^{\left\lfloor (\ell -m)/2\right\rfloor }\gamma _{\ell k}^{(m)}\;r^{2k}\;z^{\ell -2k-m}.$

### (*x*,*y*)-dependent part

Consider next, recalling that *x* = *r* sin *θ* cos *φ* and *y* = *r* sin *θ* sin *φ*, $r^{m}\sin ^{m}\theta \cos m\varphi ={\frac {1}{2}}\left[(r\sin \theta e^{i\varphi })^{m}+(r\sin \theta e^{-i\varphi })^{m}\right]={\frac {1}{2}}\left[(x+iy)^{m}+(x-iy)^{m}\right]$ Likewise $r^{m}\sin ^{m}\theta \sin m\varphi ={\frac {1}{2i}}\left[(r\sin \theta e^{i\varphi })^{m}-(r\sin \theta e^{-i\varphi })^{m}\right]={\frac {1}{2i}}\left[(x+iy)^{m}-(x-iy)^{m}\right].$ Further $A_{m}(x,y)\equiv {\frac {1}{2}}\left[(x+iy)^{m}+(x-iy)^{m}\right]=\sum _{p=0}^{m}{\binom {m}{p}}x^{p}y^{m-p}\cos(m-p){\frac {\pi }{2}}$ and $B_{m}(x,y)\equiv {\frac {1}{2i}}\left[(x+iy)^{m}-(x-iy)^{m}\right]=\sum _{p=0}^{m}{\binom {m}{p}}x^{p}y^{m-p}\sin(m-p){\frac {\pi }{2}}.$

### In total

$C_{\ell }^{m}(x,y,z)=\left[{\frac {(2-\delta _{m0})(\ell -m)!}{(\ell +m)!}}\right]^{1/2}\Pi _{\ell }^{m}(z)\;A_{m}(x,y),\qquad m=0,1,\ldots ,\ell$ $S_{\ell }^{m}(x,y,z)=\left[{\frac {2(\ell -m)!}{(\ell +m)!}}\right]^{1/2}\Pi _{\ell }^{m}(z)\;B_{m}(x,y),\qquad m=1,2,\ldots ,\ell .$

### List of lowest functions

We list explicitly the lowest functions up to and including *ℓ* = 5. Here ${\bar {\Pi }}_{\ell }^{m}(z)\equiv \left[{\tfrac {(2-\delta _{m0})(\ell -m)!}{(\ell +m)!}}\right]^{1/2}\Pi _{\ell }^{m}(z).$

${\begin{aligned}{\bar {\Pi }}_{0}^{0}&=1&{\bar {\Pi }}_{3}^{1}&={\frac {1}{4}}{\sqrt {6}}(5z^{2}-r^{2})&{\bar {\Pi }}_{4}^{4}&={\frac {1}{8}}{\sqrt {35}}\\{\bar {\Pi }}_{1}^{0}&=z&{\bar {\Pi }}_{3}^{2}&={\frac {1}{2}}{\sqrt {15}}\;z&{\bar {\Pi }}_{5}^{0}&={\frac {1}{8}}z(63z^{4}-70z^{2}r^{2}+15r^{4})\\{\bar {\Pi }}_{1}^{1}&=1&{\bar {\Pi }}_{3}^{3}&={\frac {1}{4}}{\sqrt {10}}&{\bar {\Pi }}_{5}^{1}&={\frac {1}{8}}{\sqrt {15}}(21z^{4}-14z^{2}r^{2}+r^{4})\\{\bar {\Pi }}_{2}^{0}&={\frac {1}{2}}(3z^{2}-r^{2})&{\bar {\Pi }}_{4}^{0}&={\frac {1}{8}}(35z^{4}-30r^{2}z^{2}+3r^{4})&{\bar {\Pi }}_{5}^{2}&={\frac {1}{4}}{\sqrt {105}}(3z^{2}-r^{2})z\\{\bar {\Pi }}_{2}^{1}&={\sqrt {3}}z&{\bar {\Pi }}_{4}^{1}&={\frac {\sqrt {10}}{4}}z(7z^{2}-3r^{2})&{\bar {\Pi }}_{5}^{3}&={\frac {1}{16}}{\sqrt {70}}(9z^{2}-r^{2})\\{\bar {\Pi }}_{2}^{2}&={\frac {1}{2}}{\sqrt {3}}&{\bar {\Pi }}_{4}^{2}&={\frac {1}{4}}{\sqrt {5}}(7z^{2}-r^{2})&{\bar {\Pi }}_{5}^{4}&={\frac {3}{8}}{\sqrt {35}}z\\{\bar {\Pi }}_{3}^{0}&={\frac {1}{2}}z(5z^{2}-3r^{2})&{\bar {\Pi }}_{4}^{3}&={\frac {1}{4}}{\sqrt {70}}\;z&{\bar {\Pi }}_{5}^{5}&={\frac {3}{16}}{\sqrt {14}}\\\end{aligned}}$

The lowest functions $A_{m}(x,y)\,$ and $B_{m}(x,y)\,$ are:

| *m* | *A*m | *B*m |
|---|---|---|
| 0 | $1\,$ | $0\,$ |
| 1 | $x\,$ | $y\,$ |
| 2 | $x^{2}-y^{2}\,$ | $2xy\,$ |
| 3 | $x^{3}-3xy^{2}\,$ | $3x^{2}y-y^{3}\,$ |
| 4 | $x^{4}-6x^{2}y^{2}+y^{4}\,$ | $4x^{3}y-4xy^{3}\,$ |
| 5 | $x^{5}-10x^{3}y^{2}+5xy^{4}\,$ | $5x^{4}y-10x^{2}y^{3}+y^{5}\,$ |
