---
title: "Residue theorem"
source: https://en.wikipedia.org/wiki/Residue_theorem
domain: complex-analysis
license: CC-BY-SA-4.0
tags: complex analysis, holomorphic function, residue theorem, conformal map
fetched: 2026-07-02
---

# Residue theorem

In complex analysis, the **residue theorem**, sometimes called **Cauchy's residue theorem**, is a powerful tool to evaluate line integrals of analytic functions over closed curves; it can often be used to compute real integrals and infinite series as well. It generalizes the Cauchy integral theorem and Cauchy's integral formula. The **residue theorem** should not be confused with special cases of the generalized Stokes' theorem; however, the latter can be used as a component of its proof.

## Statement of Cauchy's residue theorem

The statement is as follows:

> **Residue theorem**: Let U be a simply connected open subset of the complex plane containing a finite list of points ⁠ $a_{1},\ldots ,a_{n}$ ⁠, ⁠ $U_{0}=U\smallsetminus \{a_{1},\ldots ,a_{n}\}$ ⁠, and a function f holomorphic on ⁠ $U_{0}$ ⁠. Letting $\gamma$ be a closed rectifiable curve in ⁠ $U_{0}$ ⁠, and denoting the residue of f at each point $a_{k}$ by $\operatorname {Res} (f,a_{k})$ and the winding number of $\gamma$ around $a_{k}$ by ⁠ $\operatorname {I} (\gamma ,a_{k})$ ⁠, the line integral of f around $\gamma$ is equal to $2\pi i$ times the sum of residues, each counted as many times as $\gamma$ winds around the respective point: $\oint _{\gamma }f(z)\,dz=2\pi i\sum _{k=1}^{n}\operatorname {I} (\gamma ,a_{k})\operatorname {Res} (f,a_{k}).$
> 
> If $\gamma$ is a positively oriented simple closed curve, $\operatorname {I} (\gamma ,a_{k})$ is 1 if $a_{k}$ is in the interior of $\gamma$ and 0 if not, therefore $\oint _{\gamma }f(z)\,dz=2\pi i\sum \operatorname {Res} (f,a_{k})$ with the sum over those $a_{k}$ inside ⁠ $\gamma$ ⁠.

The relationship of the residue theorem to Stokes' theorem is given by the Jordan curve theorem. The general plane curve γ must first be reduced to a set of simple closed curves $\{\gamma _{i}\}$ whose total is equivalent to $\gamma$ for integration purposes; this reduces the problem to finding the integral of $f\,dz$ along a Jordan curve $\gamma _{i}$ with interior ⁠ V ⁠. The requirement that f be holomorphic on $U_{0}=U\smallsetminus \{a_{k}\}$ is equivalent to the statement that the exterior derivative $d(f\,dz)=0$ on ⁠ $U_{0}$ ⁠. Thus if two planar regions V and W of U enclose the same subset $\{a_{j}\}$ of ⁠ $\{a_{k}\}$ ⁠, the regions $V\smallsetminus W$ and $W\smallsetminus V$ lie entirely in ⁠ $U_{0}$ ⁠, hence $\int _{V\smallsetminus W}d(f\,dz)-\int _{W\smallsetminus V}d(f\,dz)$ is well-defined and equal to zero. Consequently, the contour integral of $f\,dz$ along $\gamma _{j}=\partial V$ is equal to the sum of a set of integrals along paths ⁠ $\gamma _{j}$ ⁠, each enclosing an arbitrarily small region around a single $a_{j}$ — the residues of f (up to the conventional factor $2\pi i$ at ⁠ $\{a_{j}\}$ ⁠. Summing over ⁠ $\{\gamma _{j}\}$ ⁠, we recover the final expression of the contour integral in terms of the winding numbers ⁠ $\{\operatorname {I} (\gamma ,a_{k})\}$ ⁠.

In order to evaluate real integrals, the residue theorem is used in the following manner: the integrand is extended to the complex plane and its residues are computed (which is usually easy), and a part of the real axis is extended to a closed curve by attaching a half-circle in the upper or lower half-plane, forming a semicircle. The integral over this curve can then be computed using the residue theorem. Often, the half-circle part of the integral will tend towards zero as the radius of the half-circle grows, leaving only the real-axis part of the integral, the one we were originally interested in.

## Calculation of residues

Suppose a punctured disk ⁠ $D=\{z:0<\vert z-c\vert <R\}$ ⁠ in the complex plane is given and ⁠ f ⁠ is a holomorphic function defined (at least) on ⁠ D ⁠. The residue ⁠ $\operatorname {Res} (f,c)$ ⁠ of ⁠ f ⁠ at ⁠ c ⁠ is the coefficient ⁠ $a_{-1}$ ⁠ of ⁠ $(z-c)^{-1}$ ⁠ in the Laurent series expansion of ⁠ f ⁠ around ⁠ c ⁠. Various methods exist for calculating this value, and the choice of which method to use depends on the function in question, and on the nature of the singularity.

According to the residue theorem, we have:

$\operatorname {Res} (f,c)={1 \over 2\pi i}\oint _{\gamma }f(z)\,dz$

where ⁠ $\gamma$ ⁠ traces out a circle around ⁠ c ⁠ in a counterclockwise manner and does not pass through or contain other singularities within it. We may choose the path ⁠ $\gamma$ ⁠ to be a circle of radius ⁠ $\varepsilon$ ⁠ around ⁠ c ⁠. Since ⁠ $\varepsilon$ ⁠ can be as small as we desire it can be made to contain only the singularity of ⁠ c ⁠ due to nature of isolated singularities. This may be used for calculation in cases where the integral can be calculated directly, but it is usually the case that residues are used to simplify calculation of integrals, and not the other way around.

### Removable singularities

If the function ⁠ f ⁠ can be continued to a holomorphic function on the whole disk ⁠ $\vert y-c\vert <R$ ⁠, then ⁠ $\operatorname {Res} (f,c)=0$ ⁠. The converse is not in general true.

### Simple poles

If ⁠ c ⁠ is a simple pole of ⁠ f ⁠, the residue of ⁠ f ⁠ is given by:

$\operatorname {Res} (f,c)=\lim _{z\to c}(z-c)f(z).$

If that limit does not exist, then ⁠ f ⁠ instead has an essential singularity at ⁠ c ⁠. If the limit is ⁠ 0 ⁠, then ⁠ f ⁠ is either analytic at ⁠ c ⁠ or has a removable singularity there. If the limit is equal to infinity, then the order of the pole is higher than ⁠ 1 ⁠.

It may be that the function ⁠ f ⁠ can be expressed as a quotient of two functions, ⁠ $f(z)={g(z)}/{h(z)}$ ⁠, where ⁠ g ⁠ and ⁠ h ⁠ are holomorphic functions in a neighbourhood of ⁠ c ⁠, with ⁠ $h(c)=0$ ⁠ and ⁠ $h'(c)\neq 0$ ⁠. In such a case, L'Hôpital's rule can be used to simplify the above formula to:

${\begin{aligned}\operatorname {Res} (f,c)&=\lim _{z\to c}(z-c)f(z)=\lim _{z\to c}{\frac {zg(z)-cg(z)}{h(z)}}\\[4pt]&=\lim _{z\to c}{\frac {g(z)+zg'(z)-cg'(z)}{h'(z)}}={\frac {g(c)}{h'(c)}}.\end{aligned}}$

### Limit formula for higher-order poles

More generally, if ⁠ c ⁠ is a pole of order ⁠ p ⁠, then the residue of ⁠ f ⁠ around ⁠ $z=c$ ⁠ can be found by the formula:

$\operatorname {Res} (f,c)={\frac {1}{(p-1)!}}\lim _{z\to c}{\frac {d^{p-1}}{dz^{p-1}}}\left((z-c)^{p}f(z)\right).$

This formula can be very useful in determining the residues for low-order poles. For higher-order poles, the calculations can become unmanageable, and series expansion is usually easier. For essential singularities, no such simple formula exists, and residues must usually be taken directly from series expansions.

### Residue at infinity

In general, the residue at infinity is defined as:

$\operatorname {Res} (f(z),\infty )=-{\operatorname {Res} }\left({\frac {1}{z^{2}}}f\left({\frac {1}{z}}\right),0\right).$

If the following condition is met:

$\lim _{|z|\to \infty }f(z)=0,$

then the residue at infinity can be computed using the following formula:

$\operatorname {Res} (f,\infty )=-\lim _{|z|\to \infty }zf(z).$

If instead

$\lim _{|z|\to \infty }f(z)=c\neq 0,$

then the residue at infinity is

$\operatorname {Res} (f,\infty )=\lim _{|z|\to \infty }z^{2}f'(z).$

For functions that are meromorphic on the entire complex plane with finitely many singularities, the sum of the residues at the (necessarily) isolated singularities plus the residue at infinity is zero, which gives:

$\operatorname {Res} (f(z),\infty )=-\sum _{k}\operatorname {Res} (f(z),a_{k}).$

### Series methods

If parts or all of a function can be expanded into a Taylor series or Laurent series, which may be possible if the parts or the whole of the function has a standard series expansion, then calculating the residue is significantly simpler than by other methods. The residue of the function is simply given by the coefficient of ⁠ $(z-c)^{-1}$ ⁠ in the Laurent series expansion of the function.

## Examples

### An integral along the real axis

The integral $\int _{-\infty }^{\infty }{\frac {e^{itx}}{x^{2}+1}}\,dx$

arises in probability theory when calculating the characteristic function of the Cauchy distribution. It resists the techniques of elementary calculus but can be evaluated by expressing it as a limit of contour integrals.

Suppose *t* > 0 and define the contour C that goes along the real line from −*a* to a and then counterclockwise along a semicircle centered at 0 from a to −*a*. Take a to be greater than 1, so that the imaginary unit i is enclosed within the curve. Now consider the contour integral $\int _{C}{f(z)}\,dz=\int _{C}{\frac {e^{itz}}{z^{2}+1}}\,dz.$

Since *e**itz* is an entire function (having no singularities at any point in the complex plane), this function has singularities only where the denominator *z*2 + 1 is zero. Since *z*2 + 1 = (*z* + *i*)(*z* − *i*), that happens only where *z* = *i* or *z* = −*i*. Only one of those points is in the region bounded by this contour. Because *f*(*z*) is ${\begin{aligned}{\frac {e^{itz}}{z^{2}+1}}&={\frac {e^{itz}}{2i}}\left({\frac {1}{z-i}}-{\frac {1}{z+i}}\right)\\&={\frac {e^{itz}}{2i(z-i)}}-{\frac {e^{itz}}{2i(z+i)}},\end{aligned}}$ the residue of *f*(*z*) at *z* = *i* is $\operatorname {Res} _{z=i}f(z)={\frac {e^{-t}}{2i}}.$

According to the residue theorem, then, we have $\int _{C}f(z)\,dz=2\pi i\cdot \operatorname {Res} \limits _{z=i}f(z)=2\pi i{\frac {e^{-t}}{2i}}=\pi e^{-t}.$

The contour C may be split into a straight part and a curved arc, so that $\int _{\mathrm {straight} }f(z)\,dz+\int _{\mathrm {arc} }f(z)\,dz=\pi e^{-t}$ and thus $\int _{-a}^{a}f(z)\,dz=\pi e^{-t}-\int _{\mathrm {arc} }f(z)\,dz.$

Using some estimations, we have $\left|\int _{\mathrm {arc} }{\frac {e^{itz}}{z^{2}+1}}\,dz\right|\leq \pi a\cdot \sup _{\text{arc}}\left|{\frac {e^{itz}}{z^{2}+1}}\right|\leq \pi a\cdot \sup _{\text{arc}}{\frac {1}{|z^{2}+1|}}\leq {\frac {\pi a}{a^{2}-1}},$ and $\lim _{a\to \infty }{\frac {\pi a}{a^{2}-1}}=0.$

The estimate on the numerator follows since *t* > 0, and for complex numbers z along the arc (which lies in the upper half-plane), the argument φ of z lies between 0 and π. So, $\left|e^{itz}\right|=\left|e^{it|z|(\cos \varphi +i\sin \varphi )}\right|=\left|e^{-t|z|\sin \varphi +it|z|\cos \varphi }\right|=e^{-t|z|\sin \varphi }\leq 1.$

Therefore, $\int _{-\infty }^{\infty }{\frac {e^{itz}}{z^{2}+1}}\,dz=\pi e^{-t}.$

If *t* < 0 then a similar argument with an arc *C*′ that winds around −*i* rather than *i* shows that

$\int _{-\infty }^{\infty }{\frac {e^{itz}}{z^{2}+1}}\,dz=\pi e^{t},$ and finally we have $\int _{-\infty }^{\infty }{\frac {e^{itz}}{z^{2}+1}}\,dz=\pi e^{-\left|t\right|}.$

(If *t* = 0 then the integral yields immediately to elementary calculus methods and its value is π.)

### Evaluating zeta functions

The fact that *π* cot(*πz*) has simple poles with residue 1 at each integer can be used to compute the sum $\sum _{n=-\infty }^{\infty }f(n).$

Consider, for example, *f*(*z*) = *z*−2. Let Γ*N* be the rectangle that is the boundary of [−*N* − ⁠1/2⁠, *N* + ⁠1/2⁠]2 with positive orientation, with an integer N. By the residue formula, ${\frac {1}{2\pi i}}\int _{\Gamma _{N}}f(z)\pi \cot(\pi z)\,dz=\operatorname {Res} \limits _{z=0}+\sum _{n=-N \atop n\neq 0}^{N}n^{-2}.$

The left-hand side goes to zero as *N* → ∞ since $|\cot(\pi z)|$ is uniformly bounded on the contour, thanks to using $x=\pm \left({\frac {1}{2}}+N\right)$ on the left and right side of the contour, and so the integrand has order $O(N^{-2})$ over the entire contour. On the other hand, ${\frac {z}{2}}\cot \left({\frac {z}{2}}\right)=1-B_{2}{\frac {z^{2}}{2!}}+\cdots$ where the Bernoulli number ⁠ $B_{2}={\frac {1}{6}}$ ⁠.

(In fact, ⁠*z*/2⁠ cot(⁠*z*/2⁠) = ⁠*iz*/1 − *e*−*iz*⁠ − ⁠*iz*/2⁠.) Thus, the residue Res*z*=0 is −⁠*π*2/3⁠. We conclude: $\sum _{n=1}^{\infty }{\frac {1}{n^{2}}}={\frac {\pi ^{2}}{6}}$ which is a proof of the Basel problem.

The same argument works for all $f(x)=x^{-2n}$ where n is a positive integer, giving us $\zeta (2n)={\frac {(-1)^{n+1}B_{2n}(2\pi )^{2n}}{2(2n)!}}.$ The trick does not work when ⁠ $f(x)=x^{-2n-1}$ ⁠, since in this case, the residue at zero vanishes, and we obtain the useless identity ⁠ $0+\zeta (2n+1)-\zeta (2n+1)=0$ ⁠.

### Evaluating Eisenstein series

The same trick can be used to establish the sum of the Eisenstein series: $\pi \cot(\pi z)=\lim _{N\to \infty }\sum _{n=-N}^{N}(z-n)^{-1}.$

Proof

Pick an arbitrary ⁠ $w\in \mathbb {C} \setminus \mathbb {Z}$ ⁠. As above, define $g(z):={\frac {1}{w-z}}\pi \cot(\pi z)$

By the Cauchy residue theorem, for all N large enough such that $\Gamma _{N}$ encircles ⁠ w ⁠, ${\frac {1}{2\pi i}}\oint _{\Gamma _{N}}g(z)dz=-\pi \cot(\pi z)+\sum _{n=-N}^{N}{\frac {1}{z-n}}$

It remains to prove the integral converges to zero. Since $\pi \cot(\pi z)/z$ is an even function, and $\Gamma _{N}$ is symmetric about the origin, we have ⁠ $\oint _{\Gamma _{N}}\pi \cot(\pi z)/zdz=0$ ⁠, and so $\oint _{\Gamma _{N}}g(z)dz=\oint _{\Gamma _{N}}\left({\frac {1}{z}}+{\frac {1}{w-z}}\right)\pi \cot(\pi z)dz=-w\oint _{\Gamma _{N}}{\frac {1}{z(z-w)}}\pi \cot(\pi z)dz=O(1/N)$
