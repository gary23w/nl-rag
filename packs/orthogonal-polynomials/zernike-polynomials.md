---
title: "Zernike polynomials"
source: https://en.wikipedia.org/wiki/Zernike_polynomials
domain: orthogonal-polynomials
license: CC-BY-SA-4.0
tags: orthogonal polynomials, hermite polynomials, chebyshev polynomials, jacobi polynomials
fetched: 2026-07-02
---

# Zernike polynomials

In mathematics, the **Zernike polynomials** are a sequence of polynomials that are orthogonal on the unit disk. Named after optical physicist Frits Zernike, laureate of the 1953 Nobel Prize in Physics and the inventor of phase-contrast microscopy, they play important roles in various optics branches such as beam optics and imaging.

## Definitions

There are even and odd Zernike polynomials. The even Zernike polynomials are defined as

$Z_{n}^{m}(\rho ,\varphi )=R_{n}^{m}(\rho )\,\cos(m\,\varphi )\!$

(even function over the azimuthal angle $\varphi$ ), and the odd Zernike polynomials are defined as

$Z_{n}^{-m}(\rho ,\varphi )=R_{n}^{m}(\rho )\,\sin(m\,\varphi ),\!$

(odd function over the azimuthal angle $\varphi$ ) where *m* and *n* are nonnegative integers with *n ≥ m ≥ 0* (*m* = 0 for spherical Zernike polynomials), *$\varphi$* is the azimuthal angle, *ρ* is the radial distance $0\leq \rho \leq 1$ , and $R_{n}^{m}$ are the radial polynomials defined below.

The Zernike polynomials are sometimes represented in a way explicitly showing *o* (odd) and *e* (even): ${\begin{array}{lcl}^{e}\,U_{n}^{m}(\rho ,\varphi )&=&Z_{n}^{m}(\rho ,\varphi )&=&R_{n}^{m}(\rho )\,\cos(m\,\varphi )\\^{o}\,U_{n}^{m}(\rho ,\varphi )&=&Z_{n}^{-m}(\rho ,\varphi )&=&R_{n}^{m}(\rho )\,\sin(m\,\varphi )\end{array}}$ Zernike polynomials have the property of being limited to a range of −1 to +1 in the unit disk, i.e. $|Z_{n}^{m}(\rho ,\varphi )|\leq 1$ if $\rho \leq 1$ . The radial polynomials $R_{n}^{m}$ are defined as

$R_{n}^{m}(\rho )=\sum _{k=0}^{\tfrac {n-m}{2}}{\frac {(-1)^{k}\,(n-k)!}{k!\left({\tfrac {n+m}{2}}-k\right)!\left({\tfrac {n-m}{2}}-k\right)!}}\;\rho ^{n-2k}$

for even *n* − *m*, while it is 0 for odd *n* − *m*. A special value is

$R_{n}^{m}(1)=1.$

### Other representations

Rewriting the ratios of factorials in the radial part as products of binomials shows that the coefficients are integer numbers:

$R_{n}^{m}(\rho )=\sum _{k=0}^{\tfrac {n-m}{2}}(-1)^{k}{\binom {n-k}{k}}{\binom {n-2k}{{\tfrac {n-m}{2}}-k}}\rho ^{n-2k}$

.

A notation as terminating Gaussian hypergeometric functions is useful to reveal recurrences, to demonstrate that they are special cases of Jacobi polynomials, to write down the differential equations, etc.:

${\begin{aligned}R_{n}^{m}(\rho )&=(-1)^{(n-m)/2}\rho ^{m}P_{(n-m)/2}^{(m,0)}(1-2\rho ^{2})\\&={\binom {n}{\tfrac {n+m}{2}}}\rho ^{n}\ {}_{2}F_{1}\left(-{\tfrac {n+m}{2}},-{\tfrac {n-m}{2}};-n;\rho ^{-2}\right)\\&=(-1)^{\tfrac {n-m}{2}}{\binom {\tfrac {n+m}{2}}{m}}\rho ^{m}\ {}_{2}F_{1}\left(1+{\tfrac {n+m}{2}},-{\tfrac {n-m}{2}};1+m;\rho ^{2}\right)\end{aligned}}$

for *n* − *m* even.

The inverse relation expands $\rho ^{j}$ for fixed $m\leq j$ into $R_{n}^{m}(\rho )$

$\rho ^{j}=\sum _{n\equiv m{\pmod {2}}}^{j}h_{j,n,m}R_{n}^{m}(\rho )$

with rational coefficients $h_{j,n,m}$

$h_{j,n,m}={\frac {n+1}{1+{\frac {j+n}{2}}}}{\frac {\binom {(j-m)/2}{(n-m)/2}}{\binom {(j+n)/2}{(n-m)/2}}}$

for even $j-m=0,2,4,\ldots$ .

The factor $\rho ^{n-2k}$ in the radial polynomial $R_{n}^{m}(\rho )$ may be expanded in a Bernstein basis of $b_{s,n/2}(\rho ^{2})$ for even n or $\rho$ times a function of $b_{s,(n-1)/2}(\rho ^{2})$ for odd n in the range $\lfloor n/2\rfloor -k\leq s\leq \lfloor n/2\rfloor$ . The radial polynomial may therefore be expressed by a finite number of Bernstein Polynomials with rational coefficients:

$R_{n}^{m}(\rho )={\frac {1}{\binom {\lfloor n/2\rfloor }{\lfloor m/2\rfloor }}}\rho ^{n\mod 2}\sum _{s=\lfloor m/2\rfloor }^{\lfloor n/2\rfloor }(-1)^{\lfloor n/2\rfloor -s}{\binom {s}{\lfloor m/2\rfloor }}{\binom {(n+m)/2}{s+\lceil m/2\rceil }}b_{s,\lfloor n/2\rfloor }(\rho ^{2}).$

### Rodrigues Formula

The radial polynomials satisfy the Rodrigues' formula

$R_{n}^{m}(x)={\frac {1}{\left({\frac {n-m}{2}}\right)!x^{m}}}\left({\frac {d}{d\left(x^{2}\right)}}\right)^{\frac {n-m}{2}}\left[x^{n+m}\left(x^{2}-1\right)^{\frac {n-m}{2}}\right].$

## Properties

### Orthogonality

The orthogonality in the radial part reads

$\int _{0}^{1}{\sqrt {2n+2}}R_{n}^{m}(\rho )\,{\sqrt {2n'+2}}R_{n'}^{m}(\rho )\,\rho d\rho =\delta _{n,n'}$

or

${\underset {0}{\overset {1}{\mathop {\int } }}}\,R_{n}^{m}(\rho )R_{{n}'}^{m}(\rho )\rho d\rho ={\frac {{\delta }_{n,{n}'}}{2n+2}}.$

Orthogonality in the angular part is represented by the elementary

$\int _{0}^{2\pi }\cos(m\varphi )\cos(m'\varphi )\,d\varphi =\epsilon _{m}\pi \delta _{m,m'},$

$\int _{0}^{2\pi }\sin(m\varphi )\sin(m'\varphi )\,d\varphi =\pi \delta _{m,m'};\quad m\neq 0,$

$\int _{0}^{2\pi }\cos(m\varphi )\sin(m'\varphi )\,d\varphi =0,$

where $\epsilon _{m}$ (sometimes called the Neumann factor because it frequently appears in conjunction with Bessel functions) is defined as *2* if $m=0$ and *1* if $m\neq 0$ . The product of the angular and radial parts establishes the orthogonality of the Zernike functions with respect to both indices if integrated over the unit disk,

$\int Z_{n}^{l}(\rho ,\varphi )Z_{n'}^{l'}(\rho ,\varphi )\,d^{2}r={\frac {\epsilon _{l}\pi }{2n+2}}\delta _{n,n'}\delta _{l,l'},$

where $d^{2}r=\rho \,d\rho \,d\varphi$ is an infinitesimal area element of the circular coordinate system (where $\rho$ is the Jacobian of a formula converting this coordinate system to Cartesian coordinate system), and where $n-l$ and $n'-l'$ are both even.

### Zernike transform

Any sufficiently smooth real-valued phase field over the unit disk $G(\rho ,\varphi )$ can be represented in terms of its Zernike coefficients (odd and even), just as periodic functions find an orthogonal representation with the Fourier series. We have

$G(\rho ,\varphi )=\sum _{m,n}\left[a_{m,n}Z_{n}^{m}(\rho ,\varphi )+b_{m,n}Z_{n}^{-m}(\rho ,\varphi )\right],$

where the coefficients can be calculated using inner products. On the space of $L^{2}$ functions on the unit disk, there is an inner product defined by

$\langle F,G\rangle :=\int F(\rho ,\varphi )G(\rho ,\varphi )\rho d\rho d\varphi .$

The Zernike coefficients can then be expressed as follows:

${\begin{aligned}a_{m,n}&={\frac {2n+2}{\epsilon _{m}\pi }}\left\langle G(\rho ,\varphi ),Z_{n}^{m}(\rho ,\varphi )\right\rangle ,\\b_{m,n}&={\frac {2n+2}{\epsilon _{m}\pi }}\left\langle G(\rho ,\varphi ),Z_{n}^{-m}(\rho ,\varphi )\right\rangle .\end{aligned}}$

Alternatively, one can use the known values of phase function *G* on the circular grid to form a system of equations. The phase function is retrieved by the unknown-coefficient weighted product with (known values) of Zernike polynomial across the unit grid. Hence, coefficients can also be found by solving a linear system, for instance by matrix inversion. Fast algorithms to calculate the forward and inverse Zernike transform use symmetry properties of trigonometric functions, separability of radial and azimuthal parts of Zernike polynomials, and their rotational symmetries.

### Symmetries

The reflections of trigonometric functions result that the parity with respect to reflection along the *x* axis is

$Z_{n}^{l}(\rho ,\varphi )=Z_{n}^{l}(\rho ,-\varphi )$

for

l

≥ 0,

$Z_{n}^{l}(\rho ,\varphi )=-Z_{n}^{l}(\rho ,-\varphi )$

for

l

< 0.

The *π* shifts of trigonometric functions result that the parity with respect to point reflection at the center of coordinates is

$Z_{n}^{l}(\rho ,\varphi )=(-1)^{l}Z_{n}^{l}(\rho ,\varphi +\pi ),$

where $(-1)^{l}$ could as well be written $(-1)^{n}$ because $n-l$ as even numbers are only cases to get non-vanishing Zernike polynomials. (If *n* is even then *l* is also even. If *n* is odd, then *l* is also odd.) This property is sometimes used to categorize Zernike polynomials into even and odd polynomials in terms of their angular dependence. (it is also possible to add another category with *l* = 0 since it has a special property of no angular dependence.)

- Angularly even Zernike polynomials: Zernike polynomials with even *l* so that $Z_{n}^{l}(\rho ,\varphi )=Z_{n}^{l}(\rho ,\varphi +\pi ).$
- Angularly odd Zernike polynomials: Zernike polynomials with odd *l* so that $Z_{n}^{l}(\rho ,\varphi )=-Z_{n}^{l}(\rho ,\varphi +\pi ).$

(This nomenclature is not used in practice because non-vanishing polynomials have even *l* only combined with even *n* and odd *l* combined with odd *n*, so angularly even polynomials are also radially even polynomials and angularly odd polynomials are also radially odd polynomials such that the attribute *angularly* is superflous.)

The radial polynomials are also either even or odd, depending on the order *n* or the azimuthal index *m*:

$R_{n}^{m}(\rho )=(-1)^{n}R_{n}^{m}(-\rho )=(-1)^{m}R_{n}^{m}(-\rho ).$

These equalities are easily seen since $R_{n}^{m}(\rho )$ with an odd (even) *m* contains only odd (even) powers to *ρ* (see examples of $R_{n}^{m}(\rho )$ below).

The periodicity of the trigonometric functions results in invariance if rotated by multiples of $2\pi /l$ radian around the center:

$Z_{n}^{l}\left(\rho ,\varphi +{\tfrac {2\pi k}{l}}\right)=Z_{n}^{l}(\rho ,\varphi ),\qquad k=0,\pm 1,\pm 2,\cdots .$

### As eigenfunctions of a differential operator

The Zernike polynomials are eigenfunctions of the Zernike differential operator, in modern formulation

${\begin{aligned}L\left[f\right]=\nabla ^{2}f-({\bf {r}}\cdot \nabla )^{2}f-2{\bf {r}}\cdot \nabla f\end{aligned}}$

self-adjoint over the unit disk, with negative eigenvalues $L[Z_{n}^{m}]=-n(n+2)Z_{n}^{m}$ . Other self-adjoint differential operators can be constructed for which the Zernike polynomials form a spectrum, for example $\nabla \cdot (1-\rho ^{2})\nabla Z_{n}^{m}=\left(m^{2}-n(n+2)\right)Z_{n}^{m}$ (relating to rough surface BRDFs), which differs from the above by a factor $\partial _{\varphi \varphi }$ .

### Recurrence relations

The Zernike polynomials satisfy the following recurrence relation:

${\begin{aligned}R_{n}^{m}(\rho )+R_{n-2}^{m}(\rho )=\rho \left[R_{n-1}^{\left|m-1\right|}(\rho )+R_{n-1}^{m+1}(\rho )\right]{\text{ .}}\end{aligned}}$

From the definition of $R_{n}^{m}$ it can be seen that $R_{m}^{m}(\rho )=\rho ^{m}$ and $R_{m+2}^{m}(\rho )=((m+2)\rho ^{2}-(m+1))\rho ^{m}$ . The following three-term recurrence relation then allows to calculate all other $R_{n}^{m}(\rho )$ :

$R_{n}^{m}(\rho )={\frac {2(n-1)(2n(n-2)\rho ^{2}-m^{2}-n(n-2))R_{n-2}^{m}(\rho )-n(n+m-2)(n-m-2)R_{n-4}^{m}(\rho )}{(n+m)(n-m)(n-2)}}{\text{ .}}$

The main use of these recurrences is to avoid cancellation of digits that occurs for large n in the accumulation of the oscillatory binomial terms in the power series notation .

The above relation is also useful since the derivative of $R_{n}^{m}$ can be calculated from two radial Zernike polynomials of adjacent degree:

${\frac {\operatorname {d} }{\operatorname {d} \!\rho }}R_{n}^{m}(\rho )={\frac {(2nm(\rho ^{2}-1)+(n-m)(m+n(2\rho ^{2}-1)))R_{n}^{m}(\rho )-(n+m)(n-m)R_{n-2}^{m}(\rho )}{2n\rho (\rho ^{2}-1)}}{\text{ .}}$

The differential equation of the Gaussian Hypergeometric Function is equivalent to

$\rho ^{2}(\rho ^{2}-1){\frac {d^{2}}{d\rho ^{2}}}R_{n}^{m}(\rho )=[n(n+2)\rho ^{2}-m^{2}]R_{n}^{m}(\rho )+\rho (1-3\rho ^{2}){\frac {d}{d\rho }}R_{n}^{m}(\rho ).$

## Nomenclature

### Noll's sequential indices

Applications often involve linear algebra, where an integral over a product of Zernike polynomials and some other factor builds matrix elements. To enumerate the rows and columns of these matrices by a single index, a conventional mapping of the two indices *n* and *m* to a single index *j* has been introduced by Noll.

(In this section the m is the signed upper index of Z which may be positive or negative or zero.) The table of this association $Z_{n}^{m}\rightarrow Z_{j}$ starts as follows (sequence A176988 in the OEIS).

$j={\frac {n(n+1)}{2}}+|m|+\left\{{\begin{array}{ll}0,&m>0\land n\equiv \{0,1\}{\pmod {4}};\\0,&m<0\land n\equiv \{2,3\}{\pmod {4}};\\1,&m\geq 0\land n\equiv \{2,3\}{\pmod {4}};\\1,&m\leq 0\land n\equiv \{0,1\}{\pmod {4}}.\end{array}}\right.$

n,m

0,0

1,1

1,−1

2,0

2,−2

2,2

3,−1

3,1

3,−3

3,3

j

1

2

3

4

5

6

7

8

9

10

n,m

4,0

4,2

4,−2

4,4

4,−4

5,1

5,−1

5,3

5,−3

5,5

j

11

12

13

14

15

16

17

18

19

20

The rule is the following.

- The even Zernike polynomials *Z* with $m>0$ obtain even indices *j.*
- The odd *Z* where $m<0$ obtain odd indices *j*.
- Within a given *n*, a lower $\left\vert m\right\vert$ results in a lower *j*.

### OSA/ANSI standard indices

OSA and ANSI single-index Zernike polynomials using:

$j={\frac {n(n+2)+m}{2}}$

n,m

0,0

1,−1

1,1

2,−2

2,0

2,2

3,−3

3,−1

3,1

3,3

j

0

1

2

3

4

5

6

7

8

9

n,m

4,−4

4,−2

4,0

4,2

4,4

5,−5

5,−3

5,−1

5,1

5,3

j

10

11

12

13

14

15

16

17

18

19

OSA/ANSI indices can be converted back to standard indices as follows (where ${\textstyle \left\lfloor \ldots \right\rfloor }$ is the floor function):

$n=\left\lfloor {\frac {{\sqrt {8j+1}}-1}{2}}\right\rfloor ,\qquad m=2j-n(n+2).$

### Fringe/University of Arizona indices

The Fringe indexing scheme is used in commercial optical design software and optical testing in, e.g., photolithography.

$j=\left(1+{\frac {n+|m|}{2}}\right)^{2}-2|m|+\left\lfloor {\frac {1-\operatorname {sgn} m}{2}}\right\rfloor$

where $\operatorname {sgn} m$ is the sign or signum function. The first 20 fringe numbers are listed below.

n,m

0,0

1,1

1,−1

2,0

2,2

2,−2

3,1

3,−1

4,0

3,3

j

1

2

3

4

5

6

7

8

9

10

n,m

3,−3

4,2

4,−2

5,1

5,−1

6,0

4,4

4,−4

5,3

5,−3

j

11

12

13

14

15

16

17

18

19

20

### Wyant indices

James C. Wyant uses the "Fringe" indexing scheme except it starts at 0 instead of 1 (subtract 1). This method is commonly used including interferogram analysis software in Zygo interferometers and the open source software DFTFringe.

## Examples

### Radial polynomials

The first few radial polynomials are:

$R_{0}^{0}(\rho )=1\,$

$R_{1}^{1}(\rho )=\rho \,$

$R_{2}^{0}(\rho )=2\rho ^{2}-1\,$

$R_{2}^{2}(\rho )=\rho ^{2}\,$

$R_{3}^{1}(\rho )=3\rho ^{3}-2\rho \,$

$R_{3}^{3}(\rho )=\rho ^{3}\,$

$R_{4}^{0}(\rho )=6\rho ^{4}-6\rho ^{2}+1\,$

$R_{4}^{2}(\rho )=4\rho ^{4}-3\rho ^{2}\,$

$R_{4}^{4}(\rho )=\rho ^{4}\,$

$R_{5}^{1}(\rho )=10\rho ^{5}-12\rho ^{3}+3\rho \,$

$R_{5}^{3}(\rho )=5\rho ^{5}-4\rho ^{3}\,$

$R_{5}^{5}(\rho )=\rho ^{5}\,$

$R_{6}^{0}(\rho )=20\rho ^{6}-30\rho ^{4}+12\rho ^{2}-1\,$

$R_{6}^{2}(\rho )=15\rho ^{6}-20\rho ^{4}+6\rho ^{2}\,$

$R_{6}^{4}(\rho )=6\rho ^{6}-5\rho ^{4}\,$

$R_{6}^{6}(\rho )=\rho ^{6}.\,$

### Zernike polynomials

The first few Zernike modes, at various indices, are shown below. In this table they are normalized differently than in the remaining sections: $\int _{0}^{2\pi }\int _{0}^{1}[Z_{j}(\rho ,\phi )]^{2}\cdot \rho \,d\rho \,d\phi =\pi$ , which is equivalent to $\operatorname {Var} (Z)_{\text{unit circle}}=1$ .

$Z_{n}^{l}$

OSA/ANSI

index

(

j

)

Noll

index

(

j

)

Wyant

index

(

j

)

Fringe/UA

index

(

j

)

Radial

degree

(

n

)

Azimuthal

degree

(

l

)

$Z_{j}$

Classical name

$Z_{0}^{0}$

0

0

0

1

0

0

0

1

0

0

0

1

Piston

(see,

Wigner semicircle distribution

)

$Z_{1}^{-1}$

0

1

0

3

0

2

0

3

1

−1

$2\rho \sin \phi$

Tilt

(Y-Tilt, vertical tilt)

$Z_{1}^{1}$

0

2

0

2

0

1

0

2

1

+1

$2\rho \cos \phi$

Tilt

(X-Tilt, horizontal tilt)

$Z_{2}^{-2}$

0

3

0

5

0

5

0

6

2

−2

${\sqrt {6}}\rho ^{2}\sin 2\phi$

Oblique astigmatism

$Z_{2}^{0}$

0

4

0

4

0

3

0

4

2

0

0

${\sqrt {3}}(2\rho ^{2}-1)$

Defocus

(longitudinal position)

$Z_{2}^{2}$

0

5

0

6

0

4

0

5

2

+2

${\sqrt {6}}\rho ^{2}\cos 2\phi$

Vertical astigmatism

$Z_{3}^{-3}$

0

6

0

9

10

11

3

−3

${\sqrt {8}}\rho ^{3}\sin 3\phi$

Vertical trefoil

$Z_{3}^{-1}$

0

7

0

7

0

7

0

8

3

−1

${\sqrt {8}}(3\rho ^{3}-2\rho )\sin \phi$

Vertical coma

$Z_{3}^{1}$

0

8

0

8

0

6

0

7

3

+1

${\sqrt {8}}(3\rho ^{3}-2\rho )\cos \phi$

Horizontal coma

$Z_{3}^{3}$

0

9

10

0

9

10

3

+3

${\sqrt {8}}\rho ^{3}\cos 3\phi$

Oblique trefoil

$Z_{4}^{-4}$

10

15

17

18

4

−4

${\sqrt {10}}\rho ^{4}\sin 4\phi$

Oblique quadrafoil

$Z_{4}^{-2}$

11

13

12

13

4

−2

${\sqrt {10}}(4\rho ^{4}-3\rho ^{2})\sin 2\phi$

Oblique secondary astigmatism

$Z_{4}^{0}$

12

11

0

8

0

9

4

0

0

${\sqrt {5}}(6\rho ^{4}-6\rho ^{2}+1)$

Primary spherical

$Z_{4}^{2}$

13

12

11

12

4

+2

${\sqrt {10}}(4\rho ^{4}-3\rho ^{2})\cos 2\phi$

Vertical secondary astigmatism

$Z_{4}^{4}$

14

14

16

17

4

+4

${\sqrt {10}}\rho ^{4}\cos 4\phi$

Vertical quadrafoil

## Applications

The functions are a basis defined over the circular support area, typically the pupil planes in classical optical imaging at visible and infrared wavelengths through systems of lenses and mirrors of finite diameter. Their advantages are the simple analytical properties inherited from the simplicity of the radial functions and the factorization in radial and azimuthal functions; this leads, for example, to closed-form expressions of the two-dimensional Fourier transform in terms of Bessel functions. Their disadvantage, in particular if high *n* are involved, is the unequal distribution of nodal lines over the unit disk, which introduces ringing effects near the perimeter $\rho \approx 1$ , which often leads attempts to define other orthogonal functions over the circular disk.

In precision optical manufacturing, Zernike polynomials are used to characterize higher-order errors observed in interferometric analyses. In wavefront slope sensors like the Shack-Hartmann, Zernike coefficients of the wavefront can be obtained by fitting measured slopes with Zernike polynomial derivatives averaged over the sampling subapertures. In optometry and ophthalmology, Zernike polynomials are used to describe wavefront aberrations of the cornea or lens from an ideal spherical shape, which result in refraction errors. They are also commonly used in adaptive optics, where they can be used to characterize atmospheric distortion. Obvious applications for this are IR or visual astronomy and satellite imagery.

Another application of the Zernike polynomials is found in the Extended Nijboer–Zernike theory of diffraction and aberrations.

Zernike polynomials are widely used as basis functions of image moments. Since Zernike polynomials are orthogonal to each other, Zernike moments can represent properties of an image with no redundancy or overlap of information between the moments. Although Zernike moments are significantly dependent on the scaling and the translation of the object in a region of interest (ROI), their magnitudes are independent of the rotation angle of the object. Thus, they can be utilized to extract features from images that describe the shape characteristics of an object. For instance, Zernike moments are utilized as shape descriptors to classify benign and malignant breast masses or the surface of vibrating disks. Zernike Moments also have been used to quantify shape of osteosarcoma cancer cell lines in single cell level. Moreover, Zernike moments have been used for early detection of Alzheimer's disease by extracting discriminative information from the MR images of Alzheimer's disease, mild cognitive impairment, and healthy groups.

## Higher dimensions

The concept translates to higher dimensions *D* if multinomials $x_{1}^{i}x_{2}^{j}\cdots x_{D}^{k}$ in Cartesian coordinates are converted to hyperspherical coordinates, $\rho ^{s},s\leq D$ , multiplied by a product of Jacobi polynomials of the angular variables. In $D=3$ dimensions, the angular variables are spherical harmonics, for example. Linear combinations of the powers $\rho ^{s}$ define an orthogonal basis $R_{n}^{(l)}(\rho )$ satisfying

$\int _{0}^{1}\rho ^{D-1}R_{n}^{(l)}(\rho )R_{n'}^{(l)}(\rho )d\rho =\delta _{n,n'}$

.

(Note that a factor ${\sqrt {2n+D}}$ is absorbed in the definition of *R* here, whereas in $D=2$ the normalization is chosen slightly differently. This is largely a matter of taste, depending on whether one wishes to maintain an integer set of coefficients or prefers tighter formulas if the orthogonalization is involved.) The explicit representation is

${\begin{aligned}R_{n}^{(l)}(\rho )&={\sqrt {2n+D}}\sum _{s=0}^{\tfrac {n-l}{2}}(-1)^{s}{{\tfrac {n-l}{2}} \choose s}{n-s-1+{\tfrac {D}{2}} \choose {\tfrac {n-l}{2}}}\rho ^{n-2s}\\&=(-1)^{\tfrac {n-l}{2}}{\sqrt {2n+D}}\sum _{s=0}^{\tfrac {n-l}{2}}(-1)^{s}{{\tfrac {n-l}{2}} \choose s}{s-1+{\tfrac {n+l+D}{2}} \choose {\tfrac {n-l}{2}}}\rho ^{2s+l}\\&=(-1)^{\tfrac {n-l}{2}}{\sqrt {2n+D}}{{\tfrac {n+l+D}{2}}-1 \choose {\tfrac {n-l}{2}}}\rho ^{l}\ {}_{2}F_{1}\left(-{\tfrac {n-l}{2}},{\tfrac {n+l+D}{2}};l+{\tfrac {D}{2}};\rho ^{2}\right)\end{aligned}}$

for even $n-l\geq 0$ , else identical to zero, with special case $R_{n}^{(n)}(\rho )={\sqrt {2n+D}}\rho ^{n}.$

Its differential equation for the Gaussian Hypergeometric Function is equivalent to

$\rho ^{2}(\rho ^{2}-1){\frac {d^{2}}{d\rho ^{2}}}R_{n}^{(l)}(\rho )=\left[n\rho ^{2}(n+D)-l(D-2+l)\right]R_{n}^{(l)}(\rho )+\rho \left[D-1-(D+1)\rho ^{2}\right]{\frac {d}{d\rho }}R_{n}^{(l)}(\rho ).$

Kintner's recurrence for fixed l and variable $n\pm 2$ quoted for $D=2$ above is in the general form

${\begin{aligned}&-(1+{\frac {n-l}{2}})(1-n-{\frac {D}{2}}){\frac {n+l+D}{2}}{\frac {R_{n+2}^{(l)}(\rho )}{\sqrt {2(n+2)+D}}}\\=&{\frac {n-l}{2}}(1+n+{\frac {D}{2}})(1-{\frac {n+l+D}{2}}){\frac {R_{n-2}^{(l)}(\rho )}{\sqrt {2(n-2)+D}}}\\&+(n+{\frac {D}{2}})\left[(1+n+{\frac {D}{2}})(1-n-{\frac {D}{2}})(1-\rho ^{2})+{\frac {1}{2}}(n-l)(D+n+l)+l+{\frac {D}{2}}-1\right]{\frac {R_{n}^{(l)}(\rho )}{\sqrt {2n+D}}}.\end{aligned}}$

For $D=3$ this was proposed by Deng and Gwo.

For fixed n and variable $l\pm 2$ the recurrence is

${\begin{aligned}&(l+{\frac {D}{2}}-1)\left[(l+{\frac {D}{2}})(l-2+{\frac {D}{2}})-{\frac {1}{2}}(l^{2}+lD+Dn+D^{2}/2+n^{2}-2l-D)r^{2}\right]R_{n}^{(l)}(r)\\&=-(l+{\frac {D}{2}})({\frac {n+l+D}{2}}-1)(1+{\frac {n-l}{2}})r^{2}R_{n}^{(l-2)}(r)-({\frac {n-l}{2}})({\frac {n+l+D}{2}})(l-2+{\frac {D}{2}})r^{2}R_{n}^{(l+2)}(r).\end{aligned}}$

The case for $D=2$ was published by Chong et al.
