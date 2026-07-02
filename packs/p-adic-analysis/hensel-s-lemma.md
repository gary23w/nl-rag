---
title: "Hensel's lemma"
source: https://en.wikipedia.org/wiki/Hensel's_lemma
domain: p-adic-analysis
license: CC-BY-SA-4.0
tags: p-adic analysis, p-adic number, hensel's lemma, local field
fetched: 2026-07-02
---

# Hensel's lemma

In mathematics, **Hensel's lemma**, also known as **Hensel's lifting lemma**, named after Kurt Hensel, is a result in modular arithmetic, stating that if a univariate polynomial has a simple root modulo a prime number *p*, then this root can be *lifted* to a unique root modulo any higher power of *p*. (The *lifting process* is the inverse of the reduction modulo *p* and is precisely defined below.) More generally, if a polynomial factors modulo *p* into two coprime polynomials, this factorization can be lifted to a factorization modulo any higher power of *p* (the case of roots corresponds to the case of degree 1 for one of the factors).

By passing to the "limit" (in fact this is an inverse limit) when the power of p tends to infinity, it follows that a root or a factorization modulo p can be lifted to a root or a factorization over the p-adic integers.

These results have been widely generalized, under the same name, to the case of polynomials over an arbitrary commutative ring, where p is replaced by an ideal, and "coprime polynomials" means "polynomials that generate an ideal containing 1".

Hensel's lemma is fundamental in p-adic analysis, a branch of analytic number theory.

The proof of Hensel's lemma is constructive, and leads to an efficient algorithm for **Hensel lifting**, which is fundamental for factoring polynomials, and gives the most efficient known algorithm for exact linear algebra over the rational numbers.

## Modular reduction and lifting

Hensel's original lemma concerns the relation between polynomial factorization over the integers and over the integers modulo a prime number p and its powers. It can be straightforwardly extended to the case where the integers are replaced by any commutative ring, and p is replaced by any maximal ideal (indeed, the maximal ideals of $\mathbb {Z}$ have the form $p\mathbb {Z} ,$ where p is a prime number).

Making this precise requires a generalization of the usual modular arithmetic, and so it is useful to define accurately the terminology that is commonly used in this context.

Let R be a commutative ring, and I an ideal of R. *Reduction modulo* I refers to the replacement of every element of R by its image under the canonical map $R\to R/I.$ For example, if $f\in R[X]$ is a polynomial with coefficients in R, its reduction modulo I, denoted $f{\bmod {I}},$ is the polynomial in $(R/I)[X]=R[X]/IR[X]$ obtained by replacing the coefficients of f by their image in $R/I.$ Two polynomials f and g in $R[X]$ are *congruent modulo* I, denoted ${\textstyle f\equiv g{\pmod {I}}}$ if they have the same coefficients modulo I, that is if $f-g\in IR[X].$ If $h\in R[X],$ a factorization of h modulo I consists in two (or more) polynomials f, g in $R[X]$ such that ${\textstyle h\equiv fg{\pmod {I}}.}$

The *lifting process* is the inverse of reduction. That is, given objects depending on elements of $R/I,$ the lifting process replaces these elements by elements of R (or of $R/I^{k}$ for some *k* > 1) that maps to them in a way that keeps the properties of the objects.

For example, given a polynomial $h\in R[X]$ and a factorization modulo I expressed as ${\textstyle h\equiv fg{\pmod {I}},}$ lifting this factorization modulo $I^{k}$ consists of finding polynomials $f',g'\in R[X]$ such that ${\textstyle f'\equiv f{\pmod {I}},}$ ${\textstyle g'\equiv g{\pmod {I}},}$ and ${\textstyle h\equiv f'g'{\pmod {I^{k}}}.}$ Hensel's lemma asserts that such a lifting is always possible under mild conditions; see next section.

## Statement

Originally, Hensel's lemma was stated (and proved) for lifting a factorization modulo a prime number p of a polynomial over the integers to a factorization modulo any power of p and to a factorization over the p-adic integers. This can be generalized easily, with the same proof to the case where the integers are replaced by any commutative ring, the prime number is replaced by a maximal ideal, and the p-adic integers are replaced by the completion with respect to the maximal ideal. It is this generalization, which is also widely used, that is presented here.

Let ${\mathfrak {m}}$ be a maximal ideal of a commutative ring R, and

$h=\alpha _{0}X^{n}+\cdots +\alpha _{n-1}X+\alpha _{n}$

be a polynomial in $R[X]$ with a leading coefficient $\alpha _{0}$ not in ${\mathfrak {m}}.$

Since ${\mathfrak {m}}$ is a maximal ideal, the quotient ring $R/{\mathfrak {m}}$ is a field, and $(R/{\mathfrak {m}})[X]$ is a principal ideal domain, and, in particular, a unique factorization domain, which means that every nonzero polynomial in $(R/{\mathfrak {m}})[X]$ can be factorized in a unique way as the product of a nonzero element of $(R/{\mathfrak {m}})$ and irreducible polynomials that are monic (that is, their leading coefficients are 1).

Hensel's lemma asserts that every factorization of h modulo ${\mathfrak {m}}$ into coprime polynomials can be lifted in a unique way into a factorization modulo ${\mathfrak {m}}^{k}$ for every k.

More precisely, with the above hypotheses, if ${\textstyle h\equiv \alpha _{0}fg{\pmod {\mathfrak {m}}},}$ where f and g are monic and coprime modulo ${\mathfrak {m}},$ then, for every positive integer k there are monic polynomials $f_{k}$ and $g_{k}$ such that

${\begin{aligned}h&\equiv \alpha _{0}f_{k}g_{k}{\pmod {{\mathfrak {m}}^{k}}},\\f_{k}&\equiv f{\pmod {\mathfrak {m}}},\\g_{k}&\equiv g{\pmod {\mathfrak {m}}},\end{aligned}}$

and $f_{k}$ and $g_{k}$ are unique (with these properties) modulo ${\mathfrak {m}}^{k}.$

### Lifting simple roots

An important special case is when $f=X-r.$ In this case the coprimality hypothesis means that r is a simple root of $h{\bmod {\mathfrak {m}}}.$ This gives the following special case of Hensel's lemma, which is often also called Hensel's lemma.

With above hypotheses and notations, if r is a simple root of $h{\bmod {\mathfrak {m}}},$ then r can be lifted in a unique way to a simple root of $h{\bmod {{\mathfrak {m}}^{n}}}$ for every positive integer n. Explicitly, for every positive integer n, there is a unique $r_{n}\in R/{\mathfrak {m}}^{n}$ such that ${\textstyle r_{n}\equiv r{\pmod {\mathfrak {m}}}}$ and $r_{n}$ is a simple root of $h{\bmod {\mathfrak {m}}}^{n}.$

### Lifting to adic completion

The fact that one can lift to $R/{\mathfrak {m}}^{n}$ for every positive integer n suggests to "pass to the limit" when n tends to the infinity. This was one of the main motivations for introducing p-adic integers.

Given a maximal ideal ${\mathfrak {m}}$ of a commutative ring R, the powers of ${\mathfrak {m}}$ form a basis of open neighborhoods for a topology on R, which is called the ${\mathfrak {m}}$ -adic topology. The completion of this topology can be identified with the completion of the local ring $R_{\mathfrak {m}},$ and with the inverse limit $\lim _{\leftarrow }R/{\mathfrak {m}}^{n}.$ This completion is a complete local ring, generally denoted ${\widehat {R}}_{\mathfrak {m}}.$ When R is the ring of the integers, and ${\mathfrak {m}}=p\mathbb {Z} ,$ where p is a prime number, this completion is the ring of p-adic integers $\mathbb {Z} _{p}.$

The definition of the completion as an inverse limit, and the above statement of Hensel's lemma imply that every factorization into pairwise coprime polynomials modulo ${\mathfrak {m}}$ of a polynomial $h\in R[X]$ can be uniquely lifted to a factorization of the image of h in ${\widehat {R}}_{\mathfrak {m}}[X].$ Similarly, every simple root of h modulo ${\mathfrak {m}}$ can be lifted to a simple root of the image of h in ${\widehat {R}}_{\mathfrak {m}}[X].$

## Proof

Hensel's lemma is generally proved incrementally by lifting a factorization over $R/{\mathfrak {m}}^{n}$ to either a factorization over $R/{\mathfrak {m}}^{n+1}$ (Linear lifting), or a factorization over $R/{\mathfrak {m}}^{2n}$ (Quadratic lifting).

The main ingredient of the proof is that coprime polynomials over a field satisfy Bézout's identity. That is, if f and g are coprime univariate polynomials over a field (here $R/{\mathfrak {m}}$ ), there are polynomials a and b such that $\deg a<\deg g,$ $\deg b<\deg f,$ and

$af+bg=1.$

Bézout's identity allows defining coprime polynomials and proving Hensel's lemma, even if the ideal ${\mathfrak {m}}$ is not maximal. Therefore, in the following proofs, one starts from a commutative ring R, an ideal I, a polynomial $h\in R[X]$ that has a leading coefficient that is invertible modulo I (that is its image in $R/I$ is a unit in $R/I$ ), and factorization of h modulo I or modulo a power of I, such that the factors satisfy a Bézout's identity modulo I. In these proofs, ${\textstyle A\equiv B{\pmod {I}}}$ means $A-B\in IR[X].$

### Linear lifting

Let I be an ideal of a commutative ring R, and $h\in R[X]$ be a univariate polynomial with coefficients in R that has a leading coefficient $\alpha$ that is invertible modulo I (that is, the image of $\alpha$ in $R/I$ is a unit in $R/I$ ).

Suppose that for some positive integer k there is a factorization

$h\equiv \alpha fg{\pmod {I^{k}}},$

such that f and g are monic polynomials that are coprime modulo I, in the sense that there exist $a,b\in R[X],$ such that ${\textstyle af+bg\equiv 1{\pmod {I}}.}$ Then, there are polynomials $\delta _{f},\delta _{g}\in I^{k}R[X],$ such that $\deg \delta _{f}<\deg f,$ $\deg \delta _{g}<\deg g,$ and

$h\equiv \alpha (f+\delta _{f})(g+\delta _{g}){\pmod {I^{k+1}}}.$

Under these conditions, $\delta _{f}$ and $\delta _{g}$ are unique modulo $I^{k+1}R[X].$

Moreover, $f+\delta _{f}$ and $g+\delta _{g}$ satisfy the same Bézout's identity as f and g, that is, $a(f+\delta _{f})+b(g+\delta _{g})\equiv 1{\pmod {I}}.$ This follows immediately from the preceding assertions, but is needed to apply iteratively the result with increasing values of k.

The proof that follows is written for computing $\delta _{f}$ and $\delta _{g}$ by using only polynomials with coefficients in $R/I$ or $I^{k}/I^{k+1}.$ When $R=\mathbb {Z}$ and $I=p\mathbb {Z} ,$ this allows manipulating only integers modulo p.

*Proof:*By hypothesis, $\alpha$ is invertible modulo I. This means that there exists $\beta \in R$ and $\gamma \in I$ such that $\alpha \beta =1-\gamma .$

Let $\delta _{h}\in I^{k}R[X],$ of degree less than $\deg h,$ such that

$\delta _{h}\equiv h-\alpha fg{\pmod {I^{k+1}}}.$

(One may choose $\delta _{h}=h-\alpha fg,$ but other choices may lead to simpler computations. For example, if $R=\mathbb {Z}$ and $I=p\mathbb {Z} ,$ it is possible and better to choose $\delta _{h}=p^{k}\delta '_{h}$ where the coefficients of $\delta '_{h}$ are integers in the interval $[0,p-1].$ )

As g is monic, the Euclidean division of $a\delta _{h}$ by g is defined, and provides q and c such that $a\delta _{h}=qg+c,$ and $\deg c<\deg g.$ Moreover, both q and c are in $I^{k}R[X].$ Similarly, let $b\delta _{h}=q'f+d,$ with $\deg d<\deg f,$ and $q',d\in I^{k}R[X].$

One has $q+q'\in I^{k+1}R[X].$ Indeed, one has

$fc+gd=af\delta _{h}+bg\delta _{h}-fg(q+q')\equiv \delta _{h}-fg(q+q'){\pmod {I^{k+1}}}.$

As $fg$ is monic, the degree modulo $I^{k+1}$ of $fg(q+q')$ can be less than $\deg fg$ only if $q+q'\in I^{k+1}R[X].$

Thus, considering congruences modulo $I^{k+1},$ one has

${\begin{aligned}\alpha (f+\beta d)&(g+\beta c)-h\\&\equiv \alpha fg-h+\alpha \beta (f(a\delta _{h}-qg)+g(b\delta _{h}-q'f))\\&\equiv \delta _{h}(-1+\alpha \beta (af+bg))-\alpha \beta fg(q+q')\\&\equiv 0{\pmod {I^{k+1}}}.\end{aligned}}$

So, the existence assertion is verified with

$\delta _{f}=\beta d,\qquad \delta _{g}=\beta c.$

### Uniqueness

Let R, I, h and $\alpha$ as a in the preceding section. Let

$h\equiv \alpha fg{\pmod {I}}$

be a factorization into coprime polynomials (in the above sense), such $\deg f_{0}+\deg g_{0}=\deg h.$ The application of linear lifting for $k=1,2,\ldots ,n-1\ldots ,$ shows the existence of $\delta _{f}$ and $\delta _{g}$ such that $\deg \delta _{f}<\deg f,$ $\deg \delta _{g}<\deg g,$ and

$h\equiv \alpha (f+\delta _{f})(g+\delta _{g}){\pmod {I^{n}}}.$

The polynomials $\delta _{f}$ and $\delta _{g}$ are uniquely defined modulo $I^{n}.$ This means that, if another pair $(\delta '_{f},\delta '_{g})$ satisfies the same conditions, then one has

$\delta '_{f}\equiv \delta _{f}{\pmod {I^{n}}}\qquad {\text{and}}\qquad \delta '_{g}\equiv \delta _{g}{\pmod {I^{n}}}.$

*Proof*: Since a congruence modulo $I^{n}$ implies the same congruence modulo $I^{n-1},$ one can proceed by induction and suppose that the uniqueness has been proved for *n* − 1, the case *n* = 0 being trivial. That is, one can suppose that

$\delta _{f}-\delta '_{f}\in I^{n-1}R[X]\qquad {\text{and}}\qquad \delta _{g}-\delta '_{g}\in I^{n-1}R[X].$

By hypothesis, has

$h\equiv \alpha (f+\delta _{f})(g+\delta _{g})\equiv \alpha (f+\delta '_{f})(g+\delta '_{g}){\pmod {I^{n}}},$

and thus

${\begin{aligned}\alpha (f+\delta _{f})(g+\delta _{g})&-\alpha (f+\delta '_{f})(g+\delta '_{g})\\&=\alpha (f(\delta _{g}-\delta '_{g})+g(\delta _{f}-\delta '_{f}))+\alpha (\delta _{f}(\delta _{g}-\delta '_{g})-\delta _{g}(\delta _{f}-\delta '_{f}))\in I^{n}R[X].\end{aligned}}$

By induction hypothesis, the second term of the latter sum belongs to $I^{n},$ and the same is thus true for the first term. As $\alpha$ is invertible modulo I, there exist $\beta \in R$ and $\gamma \in I$ such that $\alpha \beta =1+\gamma .$ Thus

${\begin{aligned}f(\delta _{g}-\delta '_{g})&+g(\delta _{f}-\delta '_{f})\\&=\alpha \beta (f(\delta _{g}-\delta '_{g})+g(\delta _{f}-\delta '_{f}))-\gamma (f(\delta _{g}-\delta '_{g})+g(\delta _{f}-\delta '_{f}))\in I^{n}R[X],\end{aligned}}$

using the induction hypothesis again.

The coprimality modulo I implies the existence of $a,b\in R[X]$ such that ${\textstyle 1\equiv af+bg{\pmod {I}}.}$ Using the induction hypothesis once more, one gets

${\begin{aligned}\delta _{g}-\delta '_{g}&\equiv (af+bg)(\delta _{g}-\delta '_{g})\\&\equiv g(b(\delta _{g}-\delta '_{g})-a(\delta _{f}-\delta '_{f})){\pmod {I^{n}}}.\end{aligned}}$

Thus one has a polynomial of degree less than $\deg g$ that is congruent modulo $I^{n}$ to the product of the *monic* polynomial g and another polynomial w. This is possible only if $w\in I^{n}R[X],$ and implies $\delta _{g}-\delta '_{g}\in I^{n}R[X].$ Similarly, $\delta _{f}-\delta '_{f}$ is also in $I^{n}R[X],$ and this proves the uniqueness.

### Quadratic lifting

Linear lifting allows lifting a factorization modulo $I^{n}$ to a factorization modulo $I^{n+1}.$ Quadratic lifting allows lifting directly to a factorization modulo $I^{2n},$ at the cost of lifting also the Bézout's identity and of computing modulo $I^{n}$ instead of modulo I (if one uses the above description of linear lifting).

For lifting up to modulo $I^{N}$ for large N one can use either method. If, say, $N=2^{k},$ a factorization modulo $I^{N}$ requires *N* − 1 steps of linear lifting or only *k* − 1 steps of quadratic lifting. However, in the latter case the size of the coefficients that have to be manipulated increase during the computation. This implies that the best lifting method depends on the context (value of N, nature of R, multiplication algorithm that is used, hardware specificities, etc.).

Quadratic lifting is based on the following property.

Suppose that for some positive integer k there is a factorization

$h\equiv \alpha fg{\pmod {I^{k}}},$

such that f and g are monic polynomials that are coprime modulo I, in the sense that there exist $a,b\in R[X],$ such that ${\textstyle af+bg\equiv 1{\pmod {I^{k}}}.}$ Then, there are polynomials $\delta _{f},\delta _{g}\in I^{k}R[X],$ such that $\deg \delta _{f}<\deg f,$ $\deg \delta _{g}<\deg g,$ and

$h\equiv \alpha (f+\delta _{f})(g+\delta _{g}){\pmod {I^{2k}}}.$

Moreover, $f+\delta _{f}$ and $g+\delta _{g}$ satisfy a Bézout's identity of the form

$(a+\delta _{a})(f+\delta _{f})+(b+\delta _{b})(g+\delta _{g})\equiv 1{\pmod {I^{2k}}}.$

(This is required for allowing iterations of quadratic lifting.)

*Proof*: The first assertion is exactly that of linear lifting applied with *k* = 1 to the ideal $I^{k}$ instead of $I.$

Let $\alpha =af+bg-1\in I^{k}R[X].$ One has

$a(f+\delta _{f})+b(g+\delta _{g})=1+\Delta ,$

where

$\Delta =\alpha +a\delta _{f}+b\delta _{g}\in I^{k}R[X].$

Setting $\delta _{a}=-a\Delta$ and $\delta _{b}=-b\Delta ,$ one gets

$(a+\delta _{a})(f+\delta _{f})+(b+\delta _{b})(g+\delta _{g})=1-\Delta ^{2}\in I^{2k}R[X],$

which proves the second assertion.

## Explicit example

Let $f(X)=X^{6}-2\in \mathbb {Q} [X].$

Modulo 2, Hensel's lemma cannot be applied since the reduction of $f(X)$ modulo 2 is simplypg 15-16

${\bar {f}}(X)=X^{6}-{\overline {2}}=X^{6}$

with 6 factors X not being relatively prime to each other. By Eisenstein's criterion, however, one can conclude that the polynomial $f(X)$ is irreducible in $\mathbb {Q} _{2}[X].$ Over $k=\mathbb {F} _{7}$ , on the other hand, one has

${\bar {f}}(X)=X^{6}-{\overline {2}}=X^{6}-{\overline {16}}=(X^{3}-{\overline {4}})\;(X^{3}+{\overline {4}})$

where 4 is the square root of 2 in $\mathbb {F} _{7}$ . As 4 is not a cube in $\mathbb {F} _{7},$ these two factors are irreducible over $\mathbb {F} _{7}$ . Hence the complete factorization of $X^{6}-2$ in $\mathbb {Z} _{7}[X]$ and $\mathbb {Q} _{7}[X]$ is

$f(X)=X^{6}-2=(X^{3}-\alpha )\;(X^{3}+\alpha ),$

where $\alpha =\ldots 450\,454_{7}$ is a square root of 2 in $\mathbb {Z} _{7}$ that can be obtained by lifting the above factorization. Finally, in $\mathbb {F} _{727}[X]$ the polynomial splits into

${\bar {f}}(X)=X^{6}-{\overline {2}}=(X-{\overline {3}})\;(X-{\overline {116}})\;(X-{\overline {119}})\;(X-{\overline {608}})\;(X-{\overline {611}})\;(X-{\overline {724}})$

with all factors relatively prime to each other, so that in $\mathbb {Z} _{727}[X]$ and $\mathbb {Q} _{727}[X]$ there are 6 factors $X-\beta$ with the (non-rational) 727-adic integers

$\beta =\left\{{\begin{array}{rrr}3\;+&\!\!\!545\cdot 727\;+&\!\!\!537\cdot 727^{2}\,+&\!\!\!161\cdot 727^{3}+\ldots \\116\;+&\!\!\!48\cdot 727\;+&\!\!\!130\cdot 727^{2}\,+&\!\!\!498\cdot 727^{3}+\ldots \\119\;+&\!\!\!593\cdot 727\;+&\!\!\!667\cdot 727^{2}\,+&\!\!\!659\cdot 727^{3}+\ldots \\608\;+&\!\!\!133\cdot 727\;+&\!\!\!59\cdot 727^{2}\,+&\!\!\!67\cdot 727^{3}+\ldots \\611\;+&\!\!\!678\cdot 727\;+&\!\!\!596\cdot 727^{2}\,+&\!\!\!228\cdot 727^{3}+\ldots \\724\;+&\!\!\!181\cdot 727\;+&\!\!\!189\cdot 727^{2}\,+&\!\!\!565\cdot 727^{3}+\ldots \end{array}}\right.$

## Using derivatives for lifting roots

Let $f(x)$ be a polynomial with integer (or p-adic integer) coefficients, and let *m*, *k* be positive integers such that *m* ≤ *k*. If *r* is an integer such that

$f(r)\equiv 0{\bmod {p}}^{k}\quad {\text{and}}\quad f'(r)\not \equiv 0{\bmod {p}}$

then, for every $m>0$ there exists an integer *s* such that

$f(s)\equiv 0{\bmod {p}}^{k+m}\quad {\text{and}}\quad r\equiv s{\bmod {p}}^{k}.$

Furthermore, this *s* is unique modulo *p**k*+*m*, and can be computed explicitly as the integer such that

$s=r-f(r)\cdot a,$

where a is an integer satisfying

$a\equiv [f'(r)]^{-1}{\bmod {p}}^{m}.$

Note that $f(r)\equiv 0{\bmod {p}}^{k}$ so that the condition $s\equiv r{\bmod {p}}^{k}$ is met. As an aside, if $f'(r)\equiv 0{\bmod {p}}$ , then 0, 1, or several *s* may exist (see Hensel Lifting below).

### Derivation

We use the Taylor expansion of *f* around *r* to write:

$f(s)=\sum _{n=0}^{N}c_{n}(s-r)^{n},\qquad c_{n}=f^{(n)}(r)/n!.$

From $r\equiv s{\bmod {p}}^{k},$ we see that *s* − *r* = *tpk* for some integer *t*. Let

${\begin{aligned}f(s)&=\sum _{n=0}^{N}c_{n}\left(tp^{k}\right)^{n}\\&=f(r)+tp^{k}f'(r)+\sum _{n=2}^{N}c_{n}t^{n}p^{kn}\\&=f(r)+tp^{k}f'(r)+p^{2k}t^{2}g(t)&&g(t)\in \mathbb {Z} [t]\\&=zp^{k}+tp^{k}f'(r)+p^{2k}t^{2}g(t)&&f(r)\equiv 0{\bmod {p}}^{k}\\&=(z+tf'(r))p^{k}+p^{2k}t^{2}g(t)\end{aligned}}$

For $m\leqslant k,$ we have:

${\begin{aligned}f(s)\equiv 0{\bmod {p}}^{k+m}&\Longleftrightarrow (z+tf'(r))p^{k}\equiv 0{\bmod {p}}^{k+m}\\&\Longleftrightarrow z+tf'(r)\equiv 0{\bmod {p}}^{m}\\&\Longleftrightarrow tf'(r)\equiv -z{\bmod {p}}^{m}\\&\Longleftrightarrow t\equiv -z[f'(r)]^{-1}{\bmod {p}}^{m}&&p\nmid f'(r)\end{aligned}}$

The assumption that $f'(r)$ is not divisible by *p* ensures that $f'(r)$ has an inverse mod $p^{m}$ which is necessarily unique. Hence a solution for *t* exists uniquely modulo $p^{m},$ and *s* exists uniquely modulo $p^{k+m}.$

## Observations

### Criterion for irreducible polynomials

Using the above hypotheses, if we consider an irreducible polynomial

$f(x)=a_{0}+a_{1}x+\cdots +a_{n}x^{n}\in K[X]$

such that $a_{0},a_{n}\neq 0$ , then

$|f|=\max\{|a_{0}|,|a_{n}|\}$

In particular, for $f(X)=X^{6}+10X-1$ , we find in $\mathbb {Q} _{2}[X]$

${\begin{aligned}|f(X)|&=\max\{|a_{0}|,\ldots ,|a_{n}|\}\\&=\max\{0,1,0\}=1\end{aligned}}$

but $\max\{|a_{0}|,|a_{n}|\}=0$ , hence the polynomial cannot be irreducible. Whereas in $\mathbb {Q} _{7}[X]$ we have both values agreeing, meaning the polynomial *could* be irreducible. In order to determine irreducibility, the Newton polygon must be employed.

### Frobenius

Note that given an $a\in \mathbb {F} _{p}$ the Frobenius endomorphism $y\mapsto y^{p}$ gives a nonzero polynomial $x^{p}-a$ that has zero derivative

${\begin{aligned}{\frac {d}{dx}}(x^{p}-a)&=p\cdot x^{p-1}\\&\equiv 0\cdot x^{p-1}{\bmod {p}}\\&\equiv 0{\bmod {p}}\end{aligned}}$

hence the *p*th roots of a do not exist in $\mathbb {Z} _{p}$ . For $a=1$ , this implies that $\mathbb {Z} _{p}$ cannot contain the root of unity $\mu _{p}$ .

### Roots of unity

Although the *p*th roots of unity are not contained in $\mathbb {F} _{p}$ , there are solutions of $x^{p}-x=x(x^{p-1}-1)$ . Note that

${\begin{aligned}{\frac {d}{dx}}(x^{p}-x)&=px^{p-1}-1\\&\equiv -1{\bmod {p}}\end{aligned}}$

is never zero, so if there exists a solution, it necessarily lifts to $\mathbb {Z} _{p}$ . Because the Frobenius gives $a^{p}=a,$ all of the non-zero elements $\mathbb {F} _{p}^{\times }$ are solutions. In fact, these are the only roots of unity contained in $\mathbb {Q} _{p}$ .

## Hensel lifting

Using the lemma, one can "lift" a root *r* of the polynomial *f* modulo *pk* to a new root *s* modulo *p**k*+1 such that *r* ≡ *s* mod *pk* (by taking *m* = 1; taking larger *m* follows by induction). In fact, a root modulo *p**k*+1 is also a root modulo *pk*, so the roots modulo *p**k*+1 are precisely the liftings of roots modulo *pk*. The new root *s* is congruent to *r* modulo *p*, so the new root also satisfies $f'(s)\equiv f'(r)\not \equiv 0{\bmod {p}}.$ So the lifting can be repeated, and starting from a solution *rk* of $f(x)\equiv 0{\bmod {p}}^{k}$ we can derive a sequence of solutions *r**k*+1, *r**k*+2, ... of the same congruence for successively higher powers of *p*, provided that $f'(r_{k})\not \equiv 0{\bmod {p}}$ for the initial root *rk*. This also shows that *f* has the same number of roots mod *pk* as mod *p**k*+1, mod *p**k*+2, or any other higher power of *p*, provided that the roots of *f* mod *pk* are all simple.

What happens to this process if *r* is not a simple root mod *p*? Suppose that

$f(r)\equiv 0{\bmod {p}}^{k}\quad {\text{and}}\quad f'(r)\equiv 0{\bmod {p}}.$

Then $s\equiv r{\bmod {p}}^{k}$ implies $f(s)\equiv f(r){\bmod {p}}^{k+1}.$ That is, $f(r+tp^{k})\equiv f(r){\bmod {p}}^{k+1}$ for all integers *t*. Therefore, we have two cases:

- If $f(r)\not \equiv 0{\bmod {p}}^{k+1}$ then there is no lifting of *r* to a root of *f*(*x*) modulo *p**k*+1.
- If $f(r)\equiv 0{\bmod {p}}^{k+1}$ then every lifting of *r* to modulus *p**k*+1 is a root of *f*(*x*) modulo *p**k*+1.

**Example.** To see both cases we examine two different polynomials with *p* = 2:

$f(x)=x^{2}+1$ and *r* = 1. Then $f(1)\equiv 0{\bmod {2}}$ and $f'(1)\equiv 0{\bmod {2}}.$ We have $f(1)\not \equiv 0{\bmod {4}}$ which means that no lifting of 1 to modulus 4 is a root of *f*(*x*) modulo 4.

$g(x)=x^{2}-17$ and *r* = 1. Then $g(1)\equiv 0{\bmod {2}}$ and $g'(1)\equiv 0{\bmod {2}}.$ However, since $g(1)\equiv 0{\bmod {4}},$ we can lift our solution to modulus 4 and both lifts (i.e. 1, 3) are solutions. The derivative is still 0 modulo 2, so *a priori* we don't know whether we can lift them to modulo 8, but in fact we can, since *g*(1) is 0 mod 8 and *g*(3) is 0 mod 8, giving solutions at 1, 3, 5, and 7 mod 8. Since of these only *g*(1) and *g*(7) are 0 mod 16 we can lift only 1 and 7 to modulo 16, giving 1, 7, 9, and 15 mod 16. Of these, only 7 and 9 give *g*(*x*) = 0 mod 32, so these can be raised giving 7, 9, 23, and 25 mod 32. It turns out that for every integer *k* ≥ 3, there are four liftings of 1 mod 2 to a root of *g*(*x*) mod 2*k*.

## Hensel's lemma for *p*-adic numbers

In the p-adic numbers, where we can make sense of rational numbers modulo powers of *p* as long as the denominator is not a multiple of *p*, the recursion from *rk* (roots mod *pk*) to *r**k*+1 (roots mod *p**k*+1) can be expressed in a much more intuitive way. Instead of choosing *t* to be an(y) integer which solves the congruence

$tf'(r_{k})\equiv -(f(r_{k})/p^{k}){\bmod {p}}^{m},$

let *t* be the rational number (the *pk* here is not really a denominator since *f*(*rk*) is divisible by *pk*):

$-(f(r_{k})/p^{k})/f'(r_{k}).$

Then set

$r_{k+1}=r_{k}+tp^{k}=r_{k}-{\frac {f(r_{k})}{f'(r_{k})}}.$

This fraction may not be an integer, but it is a p-adic integer, and the sequence of numbers *rk* converges in the p-adic integers to a root of *f*(*x*) = 0. Moreover, the displayed recursive formula for the (new) number *r**k*+1 in terms of *rk* is precisely Newton's method for finding roots to equations in the real numbers.

By working directly in the p-adics and using the p-adic valuation, there is a version of Hensel's lemma which can be applied even if we start with a solution of *f*(*a*) ≡ 0 mod *pk* such that $f'(a)\equiv 0{\bmod {p}}.$ We just need to make sure the number $f'(a)$ is not exactly 0, and *n* is sufficiently large. This more general version is as follows: if there is an integer *a* which satisfies:

$\nu _{p}(f(a))>2\nu _{p}(f'(a)),$

then there is a unique p-adic integer *b* such *f*(*b*) = 0 and $\nu _{p}(b-a)\geq \nu _{p}(f(a))-\nu _{p}(f'(a)).$ The construction of *b* amounts to showing that the recursion from Newton's method with initial value *a* converges in the p-adics and we let *b* be the limit. The uniqueness of *b* as a root fitting the condition $\nu _{p}(b-a)>\nu _{p}(f'(a))$ needs additional work.

The statement of Hensel's lemma given above above is a special case of this more general version, since the conditions that *f*(*a*) ≡ 0 mod *pk* and $f'(a)\not \equiv 0{\bmod {p}}$ say that $\nu _{p}(f(a))\geq k$ and $\nu _{p}(f'(a))=0.$

## Examples

Suppose that *p* is an odd prime and *a* is a non-zero quadratic residue modulo *p*. Then Hensel's lemma implies that *a* has a square root in the ring of p-adic integers $\mathbb {Z} _{p}.$ Indeed, let $f(x)=x^{2}-a.$ If *r* is a square root of *a* modulo *p* then:

$f(r)=r^{2}-a\equiv 0{\bmod {p}}\quad {\text{and}}\quad f'(r)=2r\not \equiv 0{\bmod {p}},$

where the second condition is dependent on the fact that *p* is odd. The basic version of Hensel's lemma tells us that starting from *r*1 = *r* we can recursively construct a sequence of integers $\{r_{k}\}$ such that:

$r_{k+1}\equiv r_{k}{\bmod {p}}^{k},\quad r_{k}^{2}\equiv a{\bmod {p}}^{k}.$

This sequence converges to some p-adic integer *b* which satisfies *b*2 = *a*. In fact, *b* is the unique square root of *a* in $\mathbb {Z} _{p}$ congruent to *r*1 modulo *p*. Conversely, if *a* is a perfect square in $\mathbb {Z} _{p}$ and it is not divisible by *p* then it is a nonzero quadratic residue mod *p*. Note that the quadratic reciprocity law allows one to easily test whether *a* is a nonzero quadratic residue mod *p*, thus we get a practical way to determine which p-adic numbers (for *p* odd) have a p-adic square root, and it can be extended to cover the case *p* = 2 using the more general version of Hensel's lemma (an example with 2-adic square roots of 17 is given later).

To make the discussion above more explicit, let us find a "square root of 2" (the solution to $x^{2}-2=0$ ) in the 7-adic integers. Modulo 7 one solution is 3 (we could also take 4), so we set $r_{1}=3$ . Hensel's lemma then allows us to find $r_{2}$ as follows:

${\begin{aligned}f(r_{1})&=3^{2}-2=7\\f(r_{1})/p^{1}&=7/7=1\\f'(r_{1})&=2r_{1}=6\end{aligned}}$

Based on which the expression

$tf'(r_{1})\equiv -(f(r_{1})/p^{k}){\bmod {p}},$

turns into:

$t\cdot 6\equiv -1{\bmod {7}}$

which implies $t=1.$ Now:

$r_{2}=r_{1}+tp^{1}=3+1\cdot 7=10=13_{7}.$

And sure enough, $10^{2}\equiv 2{\bmod {7}}^{2}.$ (If we had used the Newton method recursion directly in the 7-adics, then $r_{2}=r_{1}-f(r_{1})/f'(r_{1})=3-7/6=11/6,$ and $11/6\equiv 10{\bmod {7}}^{2}.$ )

We can continue and find $r_{3}=108=3+7+2\cdot 7^{2}=213_{7}$ . Each time we carry out the calculation (that is, for each successive value of *k*), one more base 7 digit is added for the next higher power of 7. In the 7-adic integers this sequence converges, and the limit is a square root of 2 in $\mathbb {Z} _{7}$ which has initial 7-adic expansion

$3+7+2\cdot 7^{2}+6\cdot 7^{3}+7^{4}+2\cdot 7^{5}+7^{6}+2\cdot 7^{7}+4\cdot 7^{8}+\cdots .$

If we started with the initial choice $r_{1}=4$ then Hensel's lemma would produce a square root of 2 in $\mathbb {Z} _{7}$ which is congruent to 4 (mod 7) instead of 3 (mod 7) and in fact this second square root would be the negative of the first square root (which is consistent with 4 = −3 mod 7).

As an example where the original version of Hensel's lemma is not valid but the more general one is, let $f(x)=x^{2}-17$ and $a=1.$ Then $f(a)=-16$ and $f'(a)=2,$ so

$|f(a)|_{2}<|f'(a)|_{2}^{2},$

which implies there is a unique 2-adic integer *b* satisfying

$b^{2}=17\quad {\text{and}}\quad |b-a|_{2}<|f'(a)|_{2}={\frac {1}{2}},$

i.e., *b* ≡ 1 mod 4. There are two square roots of 17 in the 2-adic integers, differing by a sign, and although they are congruent mod 2 they are not congruent mod 4. This is consistent with the general version of Hensel's lemma only giving us a unique 2-adic square root of 17 that is congruent to 1 mod 4 rather than mod 2. If we had started with the initial approximate root *a* = 3 then we could apply the more general Hensel's lemma again to find a unique 2-adic square root of 17 which is congruent to 3 mod 4. This is the other 2-adic square root of 17.

In terms of lifting the roots of $x^{2}-17$ from modulus 2*k* to 2*k*+1, the lifts starting with the root 1 mod 2 are as follows:

1 mod 2 → 1, 3 mod 4

1 mod 4 → 1, 5 mod 8 and 3 mod 4 → 3, 7 mod 8

1 mod 8 → 1, 9 mod 16 and 7 mod 8 → 7, 15 mod 16, while 3 mod 8 and 5 mod 8 don't lift to roots mod 16

9 mod 16 → 9, 25 mod 32 and 7 mod 16 → 7, 23 mod 16, while 1 mod 16 and 15 mod 16 don't lift to roots mod 32.

For every *k* at least 3, there are *four* roots of *x*2 − 17 mod 2*k*, but if we look at their 2-adic expansions we can see that in pairs they are converging to just *two* 2-adic limits. For instance, the four roots mod 32 break up into two pairs of roots which each look the same mod 16:

9 = 1 + 2

3

and 25 = 1 + 2

3

+ 2

4

.

7 = 1 + 2 + 2

2

and 23 = 1 + 2 + 2

2

+ 2

4

.

The 2-adic square roots of 17 have expansions

$1+2^{3}+2^{5}+2^{6}+2^{7}+2^{9}+2^{10}+\cdots$

$1+2+2^{2}+2^{4}+2^{8}+2^{11}+\cdots$

Another example where we can use the more general version of Hensel's lemma but not the basic version is a proof that any 3-adic integer *c* ≡ 1 mod 9 is a cube in $\mathbb {Z} _{3}.$ Let $f(x)=x^{3}-c$ and take initial approximation *a* = 1. The basic Hensel's lemma cannot be used to find roots of *f*(*x*) since $f'(r)\equiv 0{\bmod {3}}$ for every *r*. To apply the general version of Hensel's lemma we want $|f(1)|_{3}<|f'(1)|_{3}^{2},$ which means $c\equiv 1{\bmod {2}}7.$ That is, if *c* ≡ 1 mod 27 then the general Hensel's lemma tells us *f*(*x*) has a 3-adic root, so *c* is a 3-adic cube. However, we wanted to have this result under the weaker condition that *c* ≡ 1 mod 9. If *c* ≡ 1 mod 9 then *c* ≡ 1, 10, or 19 mod 27. We can apply the general Hensel's lemma three times depending on the value of *c* mod 27: if *c* ≡ 1 mod 27 then use *a* = 1, if *c* ≡ 10 mod 27 then use *a* = 4 (since 4 is a root of *f*(*x*) mod 27), and if *c* ≡ 19 mod 27 then use *a* = 7. (It is not true that every *c* ≡ 1 mod 3 is a 3-adic cube, e.g., 4 is not a 3-adic cube since it is not a cube mod 9.)

In a similar way, after some preliminary work, Hensel's lemma can be used to show that for any *odd* prime number *p*, any p-adic integer *c* congruent to 1 modulo *p*2 is a *p*-th power in $\mathbb {Z} _{p}.$ (This is false for *p* = 2.)

## Generalizations

Suppose *A* is a commutative ring, complete with respect to an ideal ${\mathfrak {m}},$ and let $f(x)\in A[x].$ *a* ∈ *A* is called an "approximate root" of *f*, if

$f(a)\equiv 0{\bmod {f}}'(a)^{2}{\mathfrak {m}}.$

If *f* has an approximate root then it has an exact root *b* ∈ *A* "close to" *a*; that is,

$f(b)=0\quad {\text{and}}\quad b\equiv a{\bmod {\mathfrak {m}}}.$

Furthermore, if $f'(a)$ is not a zero-divisor then *b* is unique.

This result can be generalized to several variables as follows:

Theorem.

Let

A

be a commutative ring that is complete with respect to ideal

${\mathfrak {m}}\subset A.$

Let

$f_{1},\ldots ,f_{n}\in A[x_{1},\ldots ,x_{n}]$

be a system of

n

polynomials in

n

variables over

A

. View

$\mathbf {f} =(f_{1},\ldots ,f_{n}),$

as a mapping from

A

n

to itself, and let

$J_{\mathbf {f} }(\mathbf {x} )$

denote its

Jacobian matrix

. Suppose

a

= (

a

1

, ...,

a

n

) ∈

A

n

is an approximate solution to

f

=

0

in the sense that

$f_{i}(\mathbf {a} )\equiv 0{\bmod {(}}{\det J_{\mathbf {f} }(a)})^{2}{\mathfrak {m}},\qquad 1\leqslant i\leqslant n.$

Then there is some

b

= (

b

1

, ...,

b

n

) ∈

A

n

satisfying

f

(

b

) =

0

, i.e.,

$f_{i}(\mathbf {b} )=0,\qquad 1\leqslant i\leqslant n.$

Furthermore this solution is "close" to

a

in the sense that

$b_{i}\equiv a_{i}{\bmod {\det }}J_{\mathbf {f} }(a){\mathfrak {m}},\qquad 1\leqslant i\leqslant n.$

As a special case, if $f_{i}(\mathbf {a} )\equiv 0{\bmod {\mathfrak {m}}}$ for all *i* and $\det J_{\mathbf {f} }(\mathbf {a} )$ is a unit in *A* then there is a solution to **f**(**b**) = **0** with $b_{i}\equiv a_{i}{\bmod {\mathfrak {m}}}$ for all *i*.

When *n* = 1, **a** = *a* is an element of *A* and $J_{\mathbf {f} }(\mathbf {a} )=J_{f}(a)=f'(a).$ The hypotheses of this multivariable Hensel's lemma reduce to the ones which were stated in the one-variable Hensel's lemma.

Completeness of a ring is not a necessary condition for the ring to have the Henselian property: Goro Azumaya in 1950 defined a commutative local ring satisfying the Henselian property for the maximal ideal **m** to be a **Henselian ring**.

Masayoshi Nagata proved in the 1950s that for any commutative local ring *A* with maximal ideal **m** there always exists a smallest ring *A*h containing *A* such that *A*h is Henselian with respect to **m***A*h. This *A*h is called the **Henselization** of *A*. If *A* is noetherian, *A*h will also be noetherian, and *A*h is manifestly algebraic as it is constructed as a limit of étale neighbourhoods. This means that *A*h is usually much smaller than the completion *Â* while still retaining the Henselian property and remaining in the same category.
