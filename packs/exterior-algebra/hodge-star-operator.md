---
title: "Hodge star operator"
source: https://en.wikipedia.org/wiki/Hodge_star_operator
domain: exterior-algebra
license: CC-BY-SA-4.0
tags: exterior algebra, differential form, wedge product, exterior derivative
fetched: 2026-07-02
---

# Hodge star operator

In mathematics, the **Hodge star operator** or **Hodge star** is a linear map defined on the exterior algebra of a finite-dimensional oriented vector space endowed with a nondegenerate symmetric bilinear form. Applying the operator to an element of the algebra produces the **Hodge dual** of the element. This map was introduced by W. V. D. Hodge.

For example, in an oriented 3-dimensional Euclidean space, an oriented plane can be represented by the exterior product of two basis vectors, and its Hodge dual is the normal vector given by their cross product; conversely, any vector is dual to the oriented plane perpendicular to it, endowed with a suitable bivector. Generalizing this to an n -dimensional vector space, the Hodge star is a one-to-one mapping of k -vectors to $(n-k)$ -vectors; the dimensions of these spaces are the binomial coefficients ${\tbinom {n}{k}}={\tbinom {n}{n-k}}$ .

The naturality of the star operator means it can play a role in differential geometry when applied to the cotangent bundle of a pseudo-Riemannian manifold, and hence to differential *k*-forms. This allows the definition of the codifferential as the Hodge adjoint of the exterior derivative, leading to the Laplace–de Rham operator. This generalizes the case of 3-dimensional Euclidean space, in which divergence of a vector field may be realized as the codifferential opposite to the gradient operator, and the Laplace operator on a function is the divergence of its gradient. An important application is the Hodge decomposition of differential forms on a closed Riemannian manifold.

## Formal definition

Let *V* be an *n*-dimensional oriented vector space with a symmetric bilinear form $\langle \cdot ,\cdot \rangle$ , referred to here as an inner product. (In more general contexts such as pseudo-Riemannian manifolds and Minkowski space, the bilinear form may not be positive-definite.) This induces an inner product on *k*-vectors ${\textstyle \alpha ,\beta \in \bigwedge ^{\!k}V}$ , for $0\leq k\leq n$ , by defining it on simple *k*-vectors $\alpha =\alpha _{1}\wedge \cdots \wedge \alpha _{k}$ and $\beta =\beta _{1}\wedge \cdots \wedge \beta _{k}$ to equal the Gram determinant

$\langle \alpha ,\beta \rangle =\det \left(\left\langle \alpha _{i},\beta _{j}\right\rangle _{i,j=1}^{k}\right)$

extended to ${\textstyle \bigwedge ^{\!k}V}$ through linearity. The Gram matrix *G* of Gram determinants is a $2^{n}\times 2^{n}$ matrix allowing the inner product on the whole of ${\textstyle \bigoplus _{0<k\leq n}\bigwedge ^{\!k}V}$ to be expressed as $a^{\mathrm {T} }Gb$ , where *a* and *b* are arbitrary multivectors represented by $2^{n}\times 1$ column matrices with entries corresponding to a fixed ordering of the $2^{n}$ basis elements.

The unit *n*-vector $\omega \in {\textstyle \bigwedge }^{\!n}V$ is defined in terms of an oriented orthonormal basis $\{e_{1},\ldots ,e_{n}\}$ of *V* as:

$\omega :=\pm e_{1}\wedge \cdots \wedge e_{n}$

,

where the sign is free to be chosen and fixed as plus or minus. (Note: In the general pseudo-Riemannian case, orthonormality means $\langle e_{i},e_{j}\rangle \in \{\delta _{ij},-\delta _{ij}\}$ for all pairs of basis vectors.) With respect to $\omega$ , the *right complement* of a basis element m is defined as the quantity ${\overline {m}}$ such that $m\wedge {\overline {m}}=\omega$ , and this is extended to ${\textstyle \bigwedge ^{\!k}V}$ through linearity.

The **Hodge star operator** is a linear operator on the exterior algebra of *V*, mapping *k*-vectors to (*n*–*k*)-vectors, for $0\leq k\leq n$ . It is defined for an arbitrary multivector $\alpha$ by the constructive formula

$\star \alpha ={\overline {G\alpha }}$

,

which applies the Gram matrix and takes the right complement. The Hodge star has the following property, which can be derived from the definition:

$\alpha \wedge \star \beta =\langle \alpha ,\beta \rangle \,\omega$

for all

k

-vectors

$\alpha ,\beta \in {\textstyle \bigwedge }^{\!k}V.$

Dually, in the space ${\textstyle \bigwedge }^{\!n}V^{*}$ of *n*-forms (alternating *n*-multilinear functions on $V^{n}$ ), the dual to $\omega$ is the volume form $\det$ , the function whose value on $v_{1}\wedge \cdots \wedge v_{n}$ is the determinant of the $n\times n$ matrix assembled from the column vectors of $v_{j}$ in $e_{i}$ -coordinates. Applying $\det$ to the above equation, we obtain the dual property

$\det(\alpha \wedge {\star }\beta )=\langle \alpha ,\beta \rangle$

for all

k

-vectors

$\alpha ,\beta \in {\textstyle \bigwedge }^{\!k}V.$

Equivalently, taking $\alpha =\alpha _{1}\wedge \cdots \wedge \alpha _{k}$ , $\beta =\beta _{1}\wedge \cdots \wedge \beta _{k}$ , and ${\star }\beta =\beta _{1}^{\star }\wedge \cdots \wedge \beta _{n-k}^{\star }$ :

$\det \left(\alpha _{1}\wedge \cdots \wedge \alpha _{k}\wedge \beta _{1}^{\star }\wedge \cdots \wedge \beta _{n-k}^{\star }\right)\ =\ \det \left(\langle \alpha _{i},\beta _{j}\rangle \right).$

This means that, writing an orthonormal basis of *k*-vectors as $e_{I}\ =\ e_{i_{1}}\wedge \cdots \wedge e_{i_{k}}$ over all subsets $I=\{i_{1}<\cdots <i_{k}\}$ of $[n]=\{1,\ldots ,n\}$ , the Hodge dual is the (*n – k*)-vector corresponding to the complementary set ${\bar {I}}=[n]\smallsetminus I=\left\{{\bar {i}}_{1}<\cdots <{\bar {i}}_{n-k}\right\}$ :

$\star e_{I}=s\cdot t\cdot e_{\bar {I}},$

where $s\in \{1,-1\}$ is the sign of the permutation $i_{1}\cdots i_{k}{\bar {i}}_{1}\cdots {\bar {i}}_{n-k}$ and $t\in \{1,-1\}$ is the product $\langle e_{i_{1}},e_{i_{1}}\rangle \cdots \langle e_{i_{k}},e_{i_{k}}\rangle$ . In the Riemannian case, $t=1$ .

The Hodge dual of a multivector *m* can be calculated with the geometric product using the identity

$\star m={\widetilde {m}}I,$

where the tilde denotes the reverse operation, and *I* is the volume element, or pseudoscalar.

There is a left version of the Hodge dual that can have per-grade sign differences compared to the right version defined above in even numbers of dimensions. When a distinction needs to be made, the right Hodge dual is often denoted by a superscript star such that $\alpha ^{\bigstar }={\overline {G\alpha }}$ . The left Hodge dual is denoted by a subscript star and defined as

$\alpha _{\bigstar }={\underline {G\alpha }}$

,

where the underline takes the *left complement* satisfying ${\underline {m}}\wedge m=\omega$ for any basis element m . Using the geometric product, the left Hodge dual of an arbitrary multivector m can be calculated with $m_{\bigstar }=I{\widetilde {m}}.$

When the bilinear form is nondegenerate, the Hodge star operator takes an orthonormal basis to an orthonormal basis. In this case, it is an isometry on the exterior algebra ${\textstyle \bigwedge V}$ .

## Geometric explanation

The Hodge star is motivated by the correspondence between a subspace *W* of *V* and its orthogonal subspace (with respect to the scalar product), where each space is endowed with an orientation and a numerical scaling factor. Specifically, a non-zero decomposable *k*-vector $w_{1}\wedge \cdots \wedge w_{k}\in \textstyle \bigwedge ^{\!k}V$ corresponds by the Plücker embedding to the subspace W with oriented basis $w_{1},\ldots ,w_{k}$ , endowed with a scaling factor equal to the *k*-dimensional volume of the parallelepiped spanned by this basis (equal to the Gramian, the determinant of the matrix of scalar products $\langle w_{i},w_{j}\rangle$ ). The Hodge star acting on a decomposable vector can be written as a decomposable (*n* − *k*)-vector:

${\star }(w_{1}\wedge \cdots \wedge w_{k})\,=\,u_{1}\wedge \cdots \wedge u_{n-k},$

where $u_{1},\ldots ,u_{n-k}$ form an oriented basis of the orthogonal space $U=W^{\perp }\!$ . Furthermore, the (*n* − *k*)-volume of the $u_{i}$ -parallelepiped must equal the *k*-volume of the $w_{i}$ -parallelepiped, and $w_{1},\ldots ,w_{k},u_{1},\ldots ,u_{n-k}$ must form an oriented basis of V .

A general *k*-vector is a linear combination of decomposable *k*-vectors, and the definition of Hodge star is extended to general *k*-vectors by defining it as being linear.

## Examples

### Two dimensions

In two dimensions with the normalized Euclidean metric and orientation given by the ordering (*x*, *y*), the Hodge star on *k*-forms is given by ${\begin{aligned}{\star }\,1&=dx\wedge dy\\{\star }\,dx&=dy\\{\star }\,dy&=-dx\\{\star }(dx\wedge dy)&=1.\end{aligned}}$

### Three dimensions

A common example of the Hodge star operator is the case *n* = 3, when it can be taken as the correspondence between vectors and bivectors. Specifically, for Euclidean **R**3 with the basis $dx,dy,dz$ of one-forms often used in vector calculus, one finds that ${\begin{aligned}{\star }\,dx&=dy\wedge dz\\{\star }\,dy&=dz\wedge dx\\{\star }\,dz&=dx\wedge dy.\end{aligned}}$

The Hodge star relates the exterior and cross product in three dimensions: ${\star }(\mathbf {u} \wedge \mathbf {v} )=\mathbf {u} \times \mathbf {v} \qquad {\star }(\mathbf {u} \times \mathbf {v} )=\mathbf {u} \wedge \mathbf {v} .$ Applied to three dimensions, the Hodge star provides an isomorphism between axial vectors and bivectors, so each axial vector **a** is associated with a bivector **A** and vice versa, that is: $\mathbf {A} ={\star }\mathbf {a} ,\ \ \mathbf {a} ={\star }\mathbf {A}$ .

The Hodge star can also be interpreted as a form of the geometric correspondence between an axis of rotation and an infinitesimal rotation (see also: 3D rotation group#Lie algebra) around the axis, with speed equal to the length of the axis of rotation. A scalar product on a vector space V gives an isomorphism $V\cong V^{*}\!$ identifying V with its dual space, and the vector space $L(V,V)$ is naturally isomorphic to the tensor product $V^{*}\!\!\otimes V\cong V\otimes V$ . Thus for $V=\mathbb {R} ^{3}$ , the star mapping ${\textstyle \textstyle {\star }:V\to \bigwedge ^{\!2}\!V\subset V\otimes V}$ takes each vector $\mathbf {v}$ to a bivector ${\star }\mathbf {v} \in V\otimes V$ , which corresponds to a linear operator $L_{\mathbf {v} }:V\to V$ . Specifically, $L_{\mathbf {v} }$ is a skew-symmetric operator, which corresponds to an infinitesimal rotation: that is, the macroscopic rotations around the axis $\mathbb {v}$ are given by the matrix exponential $\exp(tL_{\mathbf {v} })$ . With respect to the basis $dx,dy,dz$ of $\mathbb {R} ^{3}$ , the tensor $dx\otimes dy$ corresponds to a coordinate matrix with 1 in the $dx$ row and $dy$ column, etc., and the wedge $dx\wedge dy\,=\,dx\otimes dy-dy\otimes dx$ is the skew-symmetric matrix $\scriptscriptstyle \left[{\begin{array}{rrr}\,0\!\!&\!\!1&\!\!\!\!0\!\!\!\!\!\!\\[-.5em]\,\!-1\!\!&\!\!0\!\!&\!\!\!\!0\!\!\!\!\!\!\\[-.5em]\,0\!\!&\!\!0\!\!&\!\!\!\!0\!\!\!\!\!\!\end{array}}\!\!\!\right]$ , etc. That is, we may interpret the star operator as: $\mathbf {v} =a\,dx+b\,dy+c\,dz\quad \longrightarrow \quad {\star }{\mathbf {v} }\ \cong \ L_{\mathbf {v} }\ =\left[{\begin{array}{rrr}0&c&-b\\-c&0&a\\b&-a&0\end{array}}\right].$ Under this correspondence, cross product of vectors corresponds to the commutator Lie bracket of linear operators: $L_{\mathbf {u} \times \mathbf {v} }=L_{\mathbf {v} }L_{\mathbf {u} }-L_{\mathbf {u} }L_{\mathbf {v} }=-\left[L_{\mathbf {u} },L_{\mathbf {v} }\right]$ .

### Four dimensions

In case $n=4$ , the Hodge star acts as an endomorphism of the second exterior power (i.e. it maps 2-forms to 2-forms, since 4 − 2 = 2). If the signature of the metric tensor is all positive, i.e. on a Riemannian manifold, then the Hodge star is an involution. If the signature is mixed, i.e., pseudo-Riemannian, then applying the operator twice will return the argument up to a sign – see *§ Duality* below. This particular endomorphism property of 2-forms in four dimensions makes self-dual and anti-self-dual two-forms natural geometric objects to study. That is, one can describe the space of 2-forms in four dimensions with a basis that "diagonalizes" the Hodge star operator with eigenvalues $\pm 1$ (or $\pm i$ , depending on the signature).

For concreteness, we discuss the Hodge star operator in Minkowski spacetime where $n=4$ with metric signature (− + + +) and coordinates $(t,x,y,z)$ . The volume form is oriented as $\varepsilon _{0123}=1$ . For one-forms, ${\begin{aligned}{\star }dt&=-dx\wedge dy\wedge dz\,,\\{\star }dx&=-dt\wedge dy\wedge dz\,,\\{\star }dy&=-dt\wedge dz\wedge dx\,,\\{\star }dz&=-dt\wedge dx\wedge dy\,,\end{aligned}}$ while for 2-forms, ${\begin{aligned}{\star }(dt\wedge dx)&=-dy\wedge dz\,,\\{\star }(dt\wedge dy)&=-dz\wedge dx\,,\\{\star }(dt\wedge dz)&=-dx\wedge dy\,,\\{\star }(dx\wedge dy)&=dt\wedge dz\,,\\{\star }(dz\wedge dx)&=dt\wedge dy\,,\\{\star }(dy\wedge dz)&=dt\wedge dx\,.\end{aligned}}$

These are summarized in the index notation as ${\begin{aligned}{\star }(dx^{\mu })&=\eta ^{\mu \lambda }\varepsilon _{\lambda \nu \rho \sigma }{\frac {1}{3!}}dx^{\nu }\wedge dx^{\rho }\wedge dx^{\sigma }\,,\\{\star }(dx^{\mu }\wedge dx^{\nu })&=\eta ^{\mu \kappa }\eta ^{\nu \lambda }\varepsilon _{\kappa \lambda \rho \sigma }{\frac {1}{2!}}dx^{\rho }\wedge dx^{\sigma }\,.\end{aligned}}$

Hodge dual of three- and four-forms can be easily deduced from the fact that, in the Lorentzian signature, ${\star }^{2}=1$ for odd-rank forms and ${\star }^{2}=-1$ for even-rank forms. An easy rule to remember for these Hodge operations is that given a form $\alpha$ , its Hodge dual ${\star }\alpha$ may be obtained by writing the components not involved in $\alpha$ in an order such that $\alpha \wedge ({\star }\alpha )=dt\wedge dx\wedge dy\wedge dz$ . An extra minus sign will enter only if $\alpha$ contains $dt$ . (For (+ − − −), one puts in a minus sign only if $\alpha$ involves an odd number of the space-associated forms $dx$ , $dy$ and $dz$ .)

Note that the combinations $(dx^{\mu }\wedge dx^{\nu })^{\pm }:={\frac {1}{2}}{\big (}dx^{\mu }\wedge dx^{\nu }\mp i{\star }(dx^{\mu }\wedge dx^{\nu }){\big )}$ take $\pm i$ as the eigenvalue for Hodge star operator, i.e., ${\star }(dx^{\mu }\wedge dx^{\nu })^{\pm }=\pm i(dx^{\mu }\wedge dx^{\nu })^{\pm },$ and hence deserve the name self-dual and anti-self-dual two-forms. Understanding the geometry, or kinematics, of Minkowski spacetime in self-dual and anti-self-dual sectors turns out to be insightful in both mathematical and physical perspectives, making contacts to the use of the two-spinor language in modern physics such as spinor-helicity formalism or twistor theory.

### Conformal invariance

The Hodge star is conformally invariant on *n*-forms on a 2*n*-dimensional vector space V , i.e. if g is a metric on V and $\lambda >0$ , then the induced Hodge stars ${\star }_{g},{\star }_{\lambda g}:\Lambda ^{n}V\to \Lambda ^{n}V$ are the same.

### Example: Derivatives in three dimensions

The combination of the ${\star }$ operator and the exterior derivative *d* generates the classical operators grad, curl, and div on vector fields in three-dimensional Euclidean space. This works out as follows: *d* takes a 0-form (a function) to a 1-form, a 1-form to a 2-form, and a 2-form to a 3-form (and takes a 3-form to zero). For a 0-form $f=f(x,y,z)$ , the first case written out in components gives: $df={\frac {\partial f}{\partial x}}\,dx+{\frac {\partial f}{\partial y}}\,dy+{\frac {\partial f}{\partial z}}\,dz.$

The scalar product identifies 1-forms with vector fields as $dx\mapsto (1,0,0)$ , etc., so that $df$ becomes ${\textstyle \operatorname {grad} f=\left({\frac {\partial f}{\partial x}},{\frac {\partial f}{\partial y}},{\frac {\partial f}{\partial z}}\right)}$ .

In the second case, a vector field $\mathbf {F} =(A,B,C)$ corresponds to the 1-form $\varphi =A\,dx+B\,dy+C\,dz$ , which has exterior derivative: $d\varphi =\left({\frac {\partial C}{\partial y}}-{\frac {\partial B}{\partial z}}\right)dy\wedge dz+\left({\frac {\partial C}{\partial x}}-{\frac {\partial A}{\partial z}}\right)dx\wedge dz+\left({\partial B \over \partial x}-{\frac {\partial A}{\partial y}}\right)dx\wedge dy.$

Applying the Hodge star gives the 1-form: ${\star }d\varphi =\left({\partial C \over \partial y}-{\partial B \over \partial z}\right)\,dx-\left({\partial C \over \partial x}-{\partial A \over \partial z}\right)\,dy+\left({\partial B \over \partial x}-{\partial A \over \partial y}\right)\,dz,$ which becomes the vector field ${\textstyle \operatorname {curl} \mathbf {F} =\left({\frac {\partial C}{\partial y}}-{\frac {\partial B}{\partial z}},\,-{\frac {\partial C}{\partial x}}+{\frac {\partial A}{\partial z}},\,{\frac {\partial B}{\partial x}}-{\frac {\partial A}{\partial y}}\right)}$ .

In the third case, $\mathbf {F} =(A,B,C)$ again corresponds to $\varphi =A\,dx+B\,dy+C\,dz$ . Applying Hodge star, exterior derivative, and Hodge star again: ${\begin{aligned}{\star }\varphi &=A\,dy\wedge dz-B\,dx\wedge dz+C\,dx\wedge dy,\\d{\star \varphi }&=\left({\frac {\partial A}{\partial x}}+{\frac {\partial B}{\partial y}}+{\frac {\partial C}{\partial z}}\right)dx\wedge dy\wedge dz,\\{\star }d{\star }\varphi &={\frac {\partial A}{\partial x}}+{\frac {\partial B}{\partial y}}+{\frac {\partial C}{\partial z}}=\operatorname {div} \mathbf {F} .\end{aligned}}$

One advantage of this expression is that the identity *d*2 = 0, which is true in all cases, has as special cases two other identities: (1) curl grad *f* = 0, and (2) div curl **F** = 0. In particular, Maxwell's equations take on a particularly simple and elegant form, when expressed in terms of the exterior derivative and the Hodge star. The expression ${\star }d{\star }$ (multiplied by an appropriate power of −1) is called the *codifferential*; it is defined in full generality, for any dimension, further in the article below.

One can also obtain the Laplacian Δ*f* = div grad *f* in terms of the above operations: $\Delta f={\star }d{\star }df={\frac {\partial ^{2}f}{\partial x^{2}}}+{\frac {\partial ^{2}f}{\partial y^{2}}}+{\frac {\partial ^{2}f}{\partial z^{2}}}.$

The Laplacian can also be seen as a special case of the more general Laplace–deRham operator $\Delta =d\delta +\delta d$ where in three dimensions, $\delta =(-1)^{k}{\star }d{\star }$ is the codifferential for k -forms. Any function f is a 0-form, and $\delta f=0$ and so this reduces to the ordinary Laplacian. For the 1-form $\varphi$ above, the codifferential is $\delta =-{\star }d{\star }$ and after some straightforward calculations one obtains the Laplacian acting on $\varphi$ .

## Duality

When the bilinear form is nondegenerate, applying the Hodge star twice leaves a *k*-vector unchanged up to a sign: for $\eta \in {\textstyle \bigwedge }^{k}V$ in an n-dimensional space *V*, one has

${\star }{\star }\eta =(-1)^{k(n-k)}s\,\eta ,$

where s is the parity of the signature of the scalar product on *V*, that is, the sign of the determinant of the matrix of the scalar product with respect to any basis. For example, if *n* = 4 and the signature of the scalar product is either (+ − − −) or (− + + +) then *s* = −1. For Riemannian manifolds (including Euclidean spaces), we always have *s* = 1.

The above identity implies that the inverse of ${\star }$ can be given as

${\begin{aligned}{\star }^{-1}:~{\textstyle \bigwedge }^{\!k}V&\to {\textstyle \bigwedge }^{\!n-k}V\\\eta &\mapsto (-1)^{k(n-k)}\!s\,{\star }\eta \end{aligned}}$

If n is odd then *k*(*n* − *k*) is even for any k, whereas if n is even then *k*(*n* − *k*) has the parity of k. Therefore:

${\star }^{-1}={\begin{cases}s\,{\star }&n{\text{ is odd}}\\(-1)^{k}s\,{\star }&n{\text{ is even}}\end{cases}}$

where k is the degree of the element operated on.

## On manifolds

For an *n*-dimensional oriented pseudo-Riemannian manifold *M*, we apply the construction above to each cotangent space ${\text{T}}_{p}^{*}M$ and its exterior powers ${\textstyle \bigwedge ^{k}{\text{T}}_{p}^{*}M}$ , and hence to the differential *k*-forms ${\textstyle \zeta \in \Omega ^{k}(M)=\Gamma \left(\bigwedge ^{k}{\text{T}}^{*}\!M\right)}$ , the global sections of the bundle ${\textstyle \bigwedge ^{k}\mathrm {T} ^{*}\!M\to M}$ . The Riemannian metric induces a scalar product on ${\textstyle \bigwedge ^{k}{\text{T}}_{p}^{*}M}$ at each point $p\in M$ . We define the **Hodge dual** of a *k*-form $\zeta$ , defining ${\star }\zeta$ as the unique (*n* – *k*)-form satisfying $\eta \wedge {\star }\zeta \ =\ \langle \eta ,\zeta \rangle \,\omega$ for every *k*-form $\eta$ , where $\langle \eta ,\zeta \rangle$ is a real-valued function on M , and the volume form $\omega$ is induced by the pseudo-Riemannian metric. Integrating this equation over M , the right side becomes the $L^{2}$ (square-integrable) scalar product on *k*-forms, and we obtain: $\int _{M}\eta \wedge {\star }\zeta \ =\ \int _{M}\langle \eta ,\zeta \rangle \ \omega .$

More generally, if M is non-orientable, one can define the Hodge star of a *k*-form as a (*n* – *k*)-pseudo differential form; that is, a differential form with values in the canonical line bundle.

### Computation in index notation

We compute in terms of tensor index notation with respect to a (not necessarily orthonormal) basis ${\textstyle \left\{{\frac {\partial }{\partial x_{1}}},\ldots ,{\frac {\partial }{\partial x_{n}}}\right\}}$ in a tangent space $V=T_{p}M$ and its dual basis $\{dx_{1},\ldots ,dx_{n}\}$ in $V^{*}=T_{p}^{*}M$ , having the metric matrix ${\textstyle (g_{ij})=\left(\left\langle {\frac {\partial }{\partial x_{i}}},{\frac {\partial }{\partial x_{j}}}\right\rangle \right)}$ and its inverse matrix $(g^{ij})=(\langle dx^{i},dx^{j}\rangle )$ . The Hodge dual of a decomposable *k*-form is: ${\star }\left(dx^{i_{1}}\wedge \dots \wedge dx^{i_{k}}\right)\ =\ {\frac {\sqrt {\left|\det[g_{ij}]\right|}}{(n-k)!}}g^{i_{1}j_{1}}\cdots g^{i_{k}j_{k}}\varepsilon _{j_{1}\dots j_{n}}dx^{j_{k+1}}\wedge \dots \wedge dx^{j_{n}}.$

Here $\varepsilon _{j_{1}\dots j_{n}}$ is the Levi-Civita symbol with $\varepsilon _{1\dots n}=1$ , and we implicitly take the sum over all values of the repeated indices $j_{1},\ldots ,j_{n}$ . The factorial $(n-k)!$ accounts for double counting, and is not present if the summation indices are restricted so that $j_{k+1}<\dots <j_{n}$ . The absolute value of the determinant is necessary since it may be negative, as for tangent spaces to Lorentzian manifolds.

An arbitrary differential form can be written as follows: $\alpha \ =\ {\frac {1}{k!}}\alpha _{i_{1},\dots ,i_{k}}dx^{i_{1}}\wedge \dots \wedge dx^{i_{k}}\ =\ \sum _{i_{1}<\dots <i_{k}}\alpha _{i_{1},\dots ,i_{k}}dx^{i_{1}}\wedge \dots \wedge dx^{i_{k}}.$

The factorial $k!$ is again included to account for double counting when we allow non-increasing indices. We would like to define the dual of the component $\alpha _{i_{1},\dots ,i_{k}}$ so that the Hodge dual of the form is given by ${\star }\alpha ={\frac {1}{(n-k)!}}({\star }\alpha )_{i_{k+1},\dots ,i_{n}}dx^{i_{k+1}}\wedge \dots \wedge dx^{i_{n}}.$

Using the above expression for the Hodge dual of $dx^{i_{1}}\wedge \dots \wedge dx^{i_{k}}$ , we find: $({\star }\alpha )_{j_{k+1},\dots ,j_{n}}={\frac {\sqrt {\left|\det[g_{ab}]\right|}}{k!}}\alpha _{i_{1},\dots ,i_{k}}\,g^{i_{1}j_{1}}\cdots g^{i_{k}j_{k}}\,\varepsilon _{j_{1},\dots ,j_{n}}\,.$

Although one can apply this expression to any tensor $\alpha$ , the result is antisymmetric, since contraction with the completely anti-symmetric Levi-Civita symbol cancels all but the totally antisymmetric part of the tensor. It is thus equivalent to antisymmetrization followed by applying the Hodge star.

The unit volume form ${\textstyle \omega ={\star }1\in \bigwedge ^{n}V^{*}}$ is given by: $\omega ={\sqrt {\left|\det[g_{ij}]\right|}}\;dx^{1}\wedge \cdots \wedge dx^{n}.$

### Codifferential

The most important application of the Hodge star on manifolds is to define the **codifferential** $\delta$ on k -forms. Let $\delta =(-1)^{n(k+1)+1}s\ {\star }d{\star }=(-1)^{k}\,{\star }^{-1}d{\star }$ where d is the exterior derivative or differential, and $s=1$ for Riemannian manifolds. Then $d:\Omega ^{k}(M)\to \Omega ^{k+1}(M)$ while $\delta :\Omega ^{k}(M)\to \Omega ^{k-1}(M).$

The codifferential is not an antiderivation on the exterior algebra, in contrast to the exterior derivative.

The codifferential is the adjoint of the exterior derivative with respect to the square-integrable scalar product: $\langle \!\langle \eta ,\delta \zeta \rangle \!\rangle \ =\ \langle \!\langle d\eta ,\zeta \rangle \!\rangle ,$ where $\zeta$ is a k -form and $\eta$ a $(k\!-\!1)$ -form. This property is useful as it can be used to define the codifferential even when the manifold is non-orientable (and the Hodge star operator not defined). The identity can be proved from Stokes' theorem for smooth forms: $0\ =\ \int _{M}d(\eta \wedge {\star }\zeta )\ =\ \int _{M}\left(d\eta \wedge {\star }\zeta +(-1)^{k-1}\eta \wedge {\star }\,{\star }^{-1}d\,{\star }\zeta \right)\ =\ \langle \!\langle d\eta ,\zeta \rangle \!\rangle -\langle \!\langle \eta ,\delta \zeta \rangle \!\rangle ,$ provided M has empty boundary, or $\eta$ or ${\star }\zeta$ has zero boundary values. (The proper definition of the above requires specifying a topological vector space that is closed and complete on the space of smooth forms. The Sobolev space is conventionally used; it allows the convergent sequence of forms $\zeta _{i}\to \zeta$ (as $i\to \infty$ ) to be interchanged with the combined differential and integral operations, so that $\langle \!\langle \eta ,\delta \zeta _{i}\rangle \!\rangle \to \langle \!\langle \eta ,\delta \zeta \rangle \!\rangle$ and likewise for sequences converging to $\eta$ .)

Since the differential satisfies $d^{2}=0$ , the codifferential has the corresponding property $\delta ^{2}=(-1)^{n}s^{2}{\star }d{\star }{\star }d{\star }=(-1)^{nk+k+1}s^{3}{\star }d^{2}{\star }=0.$

The Laplace–deRham operator is given by $\Delta =(\delta +d)^{2}=\delta d+d\delta$ and lies at the heart of Hodge theory. It is symmetric: $\langle \!\langle \Delta \zeta ,\eta \rangle \!\rangle =\langle \!\langle \zeta ,\Delta \eta \rangle \!\rangle$ and non-negative: $\langle \!\langle \Delta \eta ,\eta \rangle \!\rangle \geq 0.$

The Hodge star sends harmonic forms to harmonic forms. As a consequence of Hodge theory, the de Rham cohomology is naturally isomorphic to the space of harmonic k-forms, and so the Hodge star induces an isomorphism of cohomology groups ${\star }:H_{\Delta }^{k}(M)\to H_{\Delta }^{n-k}(M),$ which in turn gives canonical identifications via Poincaré duality of *H k*(*M*) with its dual space.

In coordinates, with notation as above, the codifferential of the form $\alpha$ may be written as $\delta \alpha =\ -{\frac {1}{k!}}g^{ml}\left({\frac {\partial }{\partial x_{l}}}\alpha _{m,i_{1},\dots ,i_{k-1}}-\Gamma _{ml}^{j}\alpha _{j,i_{1},\dots ,i_{k-1}}\right)dx^{i_{1}}\wedge \dots \wedge dx^{i_{k-1}},$ where here $\Gamma _{ml}^{j}$ denotes the Christoffel symbols of ${\textstyle \left\{{\frac {\partial }{\partial x_{1}}},\ldots ,{\frac {\partial }{\partial x_{n}}}\right\}}$ .

#### Poincaré lemma for codifferential

In analogy to the Poincaré lemma for exterior derivative, one can define its version for codifferential, which reads

If

$\delta \omega =0$

for

$\omega \in \Lambda ^{k}(U)$

, where

U

is a

star domain

on a manifold, then there is

$\alpha \in \Lambda ^{k+1}(U)$

such that

$\omega =\delta \alpha$

.

A practical way of finding $\alpha$ is to use cohomotopy operator h , that is a local inverse of $\delta$ . One has to define a homotopy operator

$H\beta =\int _{0}^{1}{\mathcal {K}}\lrcorner \beta |_{F(t,x)}t^{k}dt,$

where $F(t,x)=x_{0}+t(x-x_{0})$ is the linear homotopy between its center $x_{0}\in U$ and a point $x\in U$ , and the (Euler) vector ${\mathcal {K}}=\sum _{i=1}^{n}(x-x_{0})^{i}\partial _{x^{i}}$ for $n=\dim(U)$ is inserted into the form $\beta \in \Lambda ^{*}(U)$ . We can then define cohomotopy operator as

$h:\Lambda (U)\rightarrow \Lambda (U),\quad h:=\eta {\star }^{-1}H\star$

,

where $\eta \beta =(-1)^{k}\beta$ for $\beta \in \Lambda ^{k}(U)$ .

The cohomotopy operator fulfills (co)homotopy invariance formula

$\delta h+h\delta =I-S_{x_{0}},$

where $S_{x_{0}}={\star }^{-1}s_{x_{0}}^{*}{\star }$ , and $s_{x_{0}}^{*}$ is the pullback along the constant map $s_{x_{0}}:x\rightarrow x_{0}$ .

Therefore, if we want to solve the equation $\delta \omega =0$ , applying cohomotopy invariance formula we get

$\omega =\delta h\omega +S_{x_{0}}\omega ,$

where

$h\omega \in \Lambda ^{k+1}(U)$

is a differential form we are looking for, and "constant of integration"

$S_{x_{0}}\omega$

vanishes unless

$\omega$

is a top form.

Cohomotopy operator fulfills the following properties: $h^{2}=0,\quad \delta h\delta =\delta ,\quad h\delta h=h$ . They make it possible to use it to define *anticoexact* forms on U by ${\mathcal {Y}}(U)=\{\omega \in \Lambda (U)|\omega =h\delta \omega \}$ , which together with exact forms ${\mathcal {C}}(U)=\{\omega \in \Lambda (U)|\omega =\delta h\omega \}$ make a direct sum decomposition

$\Lambda (U)={\mathcal {C}}(U)\oplus {\mathcal {Y}}(U)$

.

This direct sum is another way of saying that the cohomotopy invariance formula is a decomposition of unity, and the projector operators on the summands fulfills idempotence formulas: $(h\delta )^{2}=h\delta ,\quad (\delta h)^{2}=\delta h$ .

These results are extension of similar results for exterior derivative.
