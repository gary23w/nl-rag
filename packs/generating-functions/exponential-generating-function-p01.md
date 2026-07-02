---
title: "Generating function (part 1/2)"
source: https://en.wikipedia.org/wiki/Exponential_generating_function
domain: generating-functions
license: CC-BY-SA-4.0
tags: generating function, formal power series, catalan number, binomial coefficient
fetched: 2026-07-02
part: 1/2
---

# Generating function

(Redirected from

Exponential generating function

)

In mathematics, a **generating function** is a representation of an infinite sequence of numbers as the coefficients of a formal power series. Generating functions are often expressed in closed form (rather than as a series), by some expression involving operations on the formal series.

There are various types of generating functions, including **ordinary generating functions**, **exponential generating functions**, *Lambert series*, *Bell series*, and *Dirichlet series*. Every sequence in principle has a generating function of each type (except that Lambert and Dirichlet series require indices to start at 1 rather than 0), but the ease with which they can be handled may differ considerably. The particular generating function, if any, that is most useful in a given context will depend upon the nature of the sequence and the details of the problem being addressed.

Generating functions are sometimes called **generating series**, in that a series of terms can be said to be the generator of its sequence of term coefficients.


## History

Generating functions were first introduced by Abraham de Moivre in 1730, in order to solve the general linear recurrence problem.

George Pólya writes in *Mathematics and plausible reasoning*:

> The name "generating function" is due to Laplace. Yet, without giving it a name, Euler used the device of generating functions long before Laplace [..]. He applied this mathematical tool to several problems in Combinatory Analysis and the Theory of Numbers.


## Definition

> A generating function is a device somewhat similar to a bag. Instead of carrying many little objects detachedly, which could be embarrassing, we put them all in a bag, and then we have only one object to carry, the bag.

— George Pólya, *Mathematics and plausible reasoning* (1954)

> A generating function is a clothesline on which we hang up a sequence of numbers for display.

— Herbert Wilf, *Generatingfunctionology* (1994)

### Convergence

Unlike an ordinary series, the *formal* power series is not required to converge: in fact, the generating function is not actually regarded as a function, and the "variable" remains an indeterminate. One can generalize to formal power series in more than one indeterminate, to encode information about infinite multi-dimensional arrays of numbers. Thus generating functions are not functions in the formal sense of a mapping from a domain to a codomain.

These expressions in terms of the indeterminate x may involve arithmetic operations, differentiation with respect to x and composition with (i.e., substitution into) other generating functions; since these operations are also defined for functions, the result looks like a function of x. Indeed, the closed form expression can often be interpreted as a function that can be evaluated at (sufficiently small) concrete values of x, and which has the formal series as its series expansion; this explains the designation "generating functions". However such interpretation is not required to be possible, because formal series are not required to give a convergent series when a nonzero numeric value is substituted for x.

### Limitations

Not all expressions that are meaningful as functions of x are meaningful as expressions designating formal series; for example, negative and fractional powers of x are examples of functions that do not have a corresponding formal power series.


## Types

### Ordinary generating function (OGF)

When the term *generating function* is used without qualification, it is usually taken to mean an ordinary generating function. The *ordinary generating function* of a sequence *a**n* is: $G(a_{n};x)=\sum _{n=0}^{\infty }a_{n}x^{n}.$ If *a**n* is the probability mass function of a discrete random variable, then its ordinary generating function is called a probability-generating function.

### Exponential generating function (EGF)

The *exponential generating function* of a sequence *a**n* is $\operatorname {EG} (a_{n};x)=\sum _{n=0}^{\infty }a_{n}{\frac {x^{n}}{n!}}.$

Exponential generating functions are generally more convenient than ordinary generating functions for combinatorial enumeration problems that involve labelled objects.

Another benefit of exponential generating functions is that they are useful in transferring linear recurrence relations to the realm of differential equations. For example, take the Fibonacci sequence {*fn*} that satisfies the linear recurrence relation *f**n*+2 = *f**n*+1 + *f**n*. The corresponding exponential generating function has the form $\operatorname {EF} (x)=\sum _{n=0}^{\infty }{\frac {f_{n}}{n!}}x^{n}$

and its derivatives can readily be shown to satisfy the differential equation EF″(*x*) = EF′(*x*) + EF(*x*) as a direct analogue with the recurrence relation above. In this view, the factorial term *n*! is merely a counter-term to normalise the derivative operator acting on *x**n*.

### Poisson generating function

The *Poisson generating function* of a sequence *a**n* is $\operatorname {PG} (a_{n};x)=\sum _{n=0}^{\infty }a_{n}e^{-x}{\frac {x^{n}}{n!}}=e^{-x}\,\operatorname {EG} (a_{n};x).$

### Lambert series

The *Lambert series* of a sequence *a**n* is $\operatorname {LG} (a_{n};x)=\sum _{n=1}^{\infty }a_{n}{\frac {x^{n}}{1-x^{n}}}.$ Note that in a Lambert series the index n starts at 1, not at 0, as the first term would otherwise be undefined.

The Lambert series coefficients in the power series expansions $b_{n}:=[x^{n}]\operatorname {LG} (a_{n};x)$ for integers *n* ≥ 1 are related by the divisor sum $b_{n}=\sum _{d|n}a_{d}.$ The main article provides several more classical, or at least well-known examples related to special arithmetic functions in number theory. As an example of a Lambert series identity not given in the main article, we can show that for |*x*|, |*xq*| < 1 we have that $\sum _{n=1}^{\infty }{\frac {q^{n}x^{n}}{1-x^{n}}}=\sum _{n=1}^{\infty }{\frac {q^{n}x^{n^{2}}}{1-qx^{n}}}+\sum _{n=1}^{\infty }{\frac {q^{n}x^{n(n+1)}}{1-x^{n}}},$

where we have the special case identity for the generating function of the divisor function, *d*(*n*) ≡ *σ*0(*n*), given by $\sum _{n=1}^{\infty }{\frac {x^{n}}{1-x^{n}}}=\sum _{n=1}^{\infty }{\frac {x^{n^{2}}\left(1+x^{n}\right)}{1-x^{n}}}.$

### Bell series

The Bell series of a sequence *a**n* is an expression in terms of both an indeterminate x and a prime p and is given by: $\operatorname {BG} _{p}(a_{n};x)=\sum _{n=0}^{\infty }a_{p^{n}}x^{n}.$

### Dirichlet series generating functions (DGFs)

Formal Dirichlet series are often classified as generating functions, although they are not strictly formal power series. The *Dirichlet series generating function* of a sequence *a**n* is: $\operatorname {DG} (a_{n};s)=\sum _{n=1}^{\infty }{\frac {a_{n}}{n^{s}}}.$

The Dirichlet series generating function is especially useful when *a**n* is a multiplicative function, in which case it has an Euler product expression in terms of the function's Bell series: $\operatorname {DG} (a_{n};s)=\prod _{p}\operatorname {BG} _{p}(a_{n};p^{-s})\,.$

If *a**n* is a Dirichlet character then its Dirichlet series generating function is called a Dirichlet L-series. We also have a relation between the pair of coefficients in the Lambert series expansions above and their DGFs. Namely, we can prove that: $[x^{n}]\operatorname {LG} (a_{n};x)=b_{n}$ if and only if $\operatorname {DG} (a_{n};s)\zeta (s)=\operatorname {DG} (b_{n};s),$ where *ζ*(*s*) is the Riemann zeta function.

The sequence ak generated by a Dirichlet series generating function (DGF) corresponding to: $\operatorname {DG} (a_{k};s)=\zeta (s)^{m}$ has the ordinary generating function: $\sum _{k=1}^{k=n}a_{k}x^{k}=x+{\binom {m}{1}}\sum _{2\leq a\leq n}x^{a}+{\binom {m}{2}}{\underset {ab\leq n}{\sum _{a=2}^{\infty }\sum _{b=2}^{\infty }}}x^{ab}+{\binom {m}{3}}{\underset {abc\leq n}{\sum _{a=2}^{\infty }\sum _{c=2}^{\infty }\sum _{b=2}^{\infty }}}x^{abc}+{\binom {m}{4}}{\underset {abcd\leq n}{\sum _{a=2}^{\infty }\sum _{b=2}^{\infty }\sum _{c=2}^{\infty }\sum _{d=2}^{\infty }}}x^{abcd}+\cdots$

### Polynomial sequence generating functions

The idea of generating functions can be extended to sequences of other objects. Thus, for example, polynomial sequences of binomial type are generated by: $e^{xf(t)}=\sum _{n=0}^{\infty }{\frac {p_{n}(x)}{n!}}t^{n}$ where *p**n*(*x*) is a sequence of polynomials and *f*(*t*) is a function of a certain form. Sheffer sequences are generated in a similar way. See the main article generalized Appell polynomials for more information.

Examples of polynomial sequences generated by more complex generating functions include:

- Appell polynomials
- Chebyshev polynomials
- Difference polynomials
- Generalized Appell polynomials
- q-difference polynomials

### Other generating functions

Other sequences generated by more complex generating functions include:

- Double exponential generating functions
- Hadamard products of generating functions and diagonal generating functions, and their corresponding integral transformations

#### Convolution polynomials

Knuth's article titled "*Convolution Polynomials*" defines a generalized class of *convolution polynomial* sequences by their special generating functions of the form $F(z)^{x}=\exp {\bigl (}x\log F(z){\bigr )}=\sum _{n=0}^{\infty }f_{n}(x)z^{n},$ for some analytic function F with a power series expansion such that *F*(0) = 1.

We say that a family of polynomials, *f*0, *f*1, *f*2, ..., forms a *convolution family* if deg *fn* ≤ *n* and if the following convolution condition holds for all x, y and for all *n* ≥ 0: $f_{n}(x+y)=f_{n}(x)f_{0}(y)+f_{n-1}(x)f_{1}(y)+\cdots +f_{1}(x)f_{n-1}(y)+f_{0}(x)f_{n}(y).$

We see that for non-identically zero convolution families, this definition is equivalent to requiring that the sequence have an ordinary generating function of the first form given above.

A sequence of convolution polynomials defined in the notation above has the following properties:

- The sequence *n*! · *fn*(*x*) is of binomial type
- Special values of the sequence include *fn*(1) = [*zn*] *F*(*z*) and *fn*(0) = *δ**n*,0, and
- For arbitrary (fixed) $x,y,t\in \mathbb {C}$ , these polynomials satisfy convolution formulas of the form

${\begin{aligned}f_{n}(x+y)&=\sum _{k=0}^{n}f_{k}(x)f_{n-k}(y)\\f_{n}(2x)&=\sum _{k=0}^{n}f_{k}(x)f_{n-k}(x)\\xnf_{n}(x+y)&=(x+y)\sum _{k=0}^{n}kf_{k}(x)f_{n-k}(y)\\{\frac {(x+y)f_{n}(x+y+tn)}{x+y+tn}}&=\sum _{k=0}^{n}{\frac {xf_{k}(x+tk)}{x+tk}}{\frac {yf_{n-k}(y+t(n-k))}{y+t(n-k)}}.\end{aligned}}$

For a fixed non-zero parameter $t\in \mathbb {C}$ , we have modified generating functions for these convolution polynomial sequences given by ${\frac {zF_{n}(x+tn)}{(x+tn)}}=\left[z^{n}\right]{\mathcal {F}}_{t}(z)^{x},$ where 𝓕*t*(*z*) is implicitly defined by a functional equation of the form 𝓕*t*(*z*) = *F*(*x*𝓕*t*(*z*)*t*). Moreover, we can use matrix methods (as in the reference) to prove that given two convolution polynomial sequences, ⟨ *fn*(*x*) ⟩ and ⟨ *gn*(*x*) ⟩, with respective corresponding generating functions, *F*(*z*)*x* and *G*(*z*)*x*, then for arbitrary t we have the identity $\left[z^{n}\right]\left(G(z)F\left(zG(z)^{t}\right)\right)^{x}=\sum _{k=0}^{n}F_{k}(x)G_{n-k}(x+tk).$

Examples of convolution polynomial sequences include the *binomial power series*, 𝓑*t*(*z*) = 1 + *z*𝓑*t*(*z*)*t*, so-termed *tree polynomials*, the Bell numbers, *B*(*n*), the Laguerre polynomials, and the Stirling convolution polynomials.


## Ordinary generating functions

### Examples for simple sequences

Polynomials are a special case of ordinary generating functions, corresponding to finite sequences, or equivalently sequences that vanish after a certain point. These are important in that many finite sequences can usefully be interpreted as generating functions, such as the Poincaré polynomial and others.

A fundamental generating function is that of the constant sequence 1, 1, 1, 1, 1, 1, 1, 1, 1, ..., whose ordinary generating function is the geometric series $\sum _{n=0}^{\infty }x^{n}={\frac {1}{1-x}}.$

The left-hand side is the Maclaurin series expansion of the right-hand side. Alternatively, the equality can be justified by multiplying the power series on the left by 1 − *x*, and checking that the result is the constant power series 1 (in other words, that all coefficients except the one of *x*0 are equal to 0). Moreover, there can be no other power series with this property. The left-hand side therefore designates the multiplicative inverse of 1 − *x* in the ring of power series.

Expressions for the ordinary generating function of other sequences are easily derived from this one. For instance, the substitution *x* → *ax* gives the generating function for the geometric sequence 1, *a*, *a*2, *a*3, ... for any constant a: $\sum _{n=0}^{\infty }(ax)^{n}={\frac {1}{1-ax}}.$

(The equality also follows directly from the fact that the left-hand side is the Maclaurin series expansion of the right-hand side.) In particular, $\sum _{n=0}^{\infty }(-1)^{n}x^{n}={\frac {1}{1+x}}.$

One can also introduce regular gaps in the sequence by replacing x by some power of x, so for instance for the sequence 1, 0, 1, 0, 1, 0, 1, 0, ... (which skips over *x*, *x*3, *x*5, ...) one gets the generating function $\sum _{n=0}^{\infty }x^{2n}={\frac {1}{1-x^{2}}}.$

By squaring the initial generating function, or by finding the derivative of both sides with respect to x and making a change of running variable *n* → *n* + 1, one sees that the coefficients form the sequence 1, 2, 3, 4, 5, ..., so one has $\sum _{n=0}^{\infty }(n+1)x^{n}={\frac {1}{(1-x)^{2}}},$

and the third power has as coefficients the triangular numbers 1, 3, 6, 10, 15, 21, ... whose term n is the binomial coefficient (*n* + 2 2), so that $\sum _{n=0}^{\infty }{\binom {n+2}{2}}x^{n}={\frac {1}{(1-x)^{3}}}.$

More generally, for any non-negative integer k and non-zero real value a, it is true that $\sum _{n=0}^{\infty }a^{n}{\binom {n+k}{k}}x^{n}={\frac {1}{(1-ax)^{k+1}}}\,.$

Since $2{\binom {n+2}{2}}-3{\binom {n+1}{1}}+{\binom {n}{0}}=2{\frac {(n+1)(n+2)}{2}}-3(n+1)+1=n^{2},$

one can find the ordinary generating function for the sequence 0, 1, 4, 9, 16, ... of square numbers by linear combination of binomial-coefficient generating sequences: $G(n^{2};x)=\sum _{n=0}^{\infty }n^{2}x^{n}={\frac {2}{(1-x)^{3}}}-{\frac {3}{(1-x)^{2}}}+{\frac {1}{1-x}}={\frac {x(x+1)}{(1-x)^{3}}}.$

We may also expand alternately to generate this same sequence of squares as a sum of derivatives of the geometric series in the following form: ${\begin{aligned}G(n^{2};x)&=\sum _{n=0}^{\infty }n^{2}x^{n}\\[4px]&=\sum _{n=0}^{\infty }n(n-1)x^{n}+\sum _{n=0}^{\infty }nx^{n}\\[4px]&=x^{2}D^{2}\left[{\frac {1}{1-x}}\right]+xD\left[{\frac {1}{1-x}}\right]\\[4px]&={\frac {2x^{2}}{(1-x)^{3}}}+{\frac {x}{(1-x)^{2}}}={\frac {x(x+1)}{(1-x)^{3}}}.\end{aligned}}$

By induction, we can similarly show for positive integers *m* ≥ 1 that $n^{m}=\sum _{j=0}^{m}{\begin{Bmatrix}m\\j\end{Bmatrix}}{\frac {n!}{(n-j)!}},$

where {*n* *k*} denote the Stirling numbers of the second kind and where the generating function $\sum _{n=0}^{\infty }{\frac {n!}{(n-j)!}}\,z^{n}={\frac {j!\cdot z^{j}}{(1-z)^{j+1}}},$

so that we can form the analogous generating functions over the integral mth powers generalizing the result in the square case above. In particular, since we can write ${\frac {z^{k}}{(1-z)^{k+1}}}=\sum _{i=0}^{k}{\binom {k}{i}}{\frac {(-1)^{k-i}}{(1-z)^{i+1}}},$

we can apply a well-known finite sum identity involving the Stirling numbers to obtain that $\sum _{n=0}^{\infty }n^{m}z^{n}=\sum _{j=0}^{m}{\begin{Bmatrix}m+1\\j+1\end{Bmatrix}}{\frac {(-1)^{m-j}j!}{(1-z)^{j+1}}}.$

### Rational functions

The ordinary generating function of a sequence can be expressed as a rational function (the ratio of two finite-degree polynomials) if and only if the sequence is a linear recursive sequence with constant coefficients; this generalizes the examples above. Conversely, every sequence generated by a fraction of polynomials satisfies a linear recurrence with constant coefficients; these coefficients are identical to the coefficients of the fraction denominator polynomial (so they can be directly read off). This observation shows it is easy to solve for generating functions of sequences defined by a linear finite difference equation with constant coefficients, and then hence, for explicit closed-form formulas for the coefficients of these generating functions. The prototypical example here is to derive Binet's formula for the Fibonacci numbers via generating function techniques.

We also notice that the class of rational generating functions precisely corresponds to the generating functions that enumerate *quasi-polynomial* sequences of the form $f_{n}=p_{1}(n)\rho _{1}^{n}+\cdots +p_{\ell }(n)\rho _{\ell }^{n},$

where the reciprocal roots, $\rho _{i}\in \mathbb {C}$ , are fixed scalars and where *p**i*(*n*) is a polynomial in n for all 1 ≤ *i* ≤ *ℓ*.

In general, Hadamard products of rational functions produce rational generating functions. Similarly, if $F(s,t):=\sum _{m,n\geq 0}f(m,n)w^{m}z^{n}$

is a bivariate rational generating function, then its corresponding *diagonal generating function*, $\operatorname {diag} (F):=\sum _{n=0}^{\infty }f(n,n)z^{n},$

is *algebraic*. For example, if we let $F(s,t):=\sum _{i,j\geq 0}{\binom {i+j}{i}}s^{i}t^{j}={\frac {1}{1-s-t}},$

then this generating function's diagonal coefficient generating function is given by the well-known OGF formula $\operatorname {diag} (F)=\sum _{n=0}^{\infty }{\binom {2n}{n}}z^{n}={\frac {1}{\sqrt {1-4z}}}.$

This result is computed in many ways, including Cauchy's integral formula or contour integration, taking complex residues, or by direct manipulations of formal power series in two variables.

### Operations on generating functions

#### Multiplication yields convolution

Multiplication of ordinary generating functions yields a discrete convolution (the Cauchy product) of the sequences. For example, the sequence of cumulative sums (compare to the slightly more general Euler–Maclaurin formula) $(a_{0},a_{0}+a_{1},a_{0}+a_{1}+a_{2},\ldots )$ of a sequence with ordinary generating function *G*(*an*; *x*) has the generating function $G(a_{n};x)\cdot {\frac {1}{1-x}}$ because ⁠1/1 − *x*⁠ is the ordinary generating function for the sequence (1, 1, ...). See also the section on convolutions in the applications section of this article below for further examples of problem solving with convolutions of generating functions and interpretations.

#### Shifting sequence indices

For integers *m* ≥ 1, we have the following two analogous identities for the modified generating functions enumerating the shifted sequence variants of ⟨ *g**n* − *m* ⟩ and ⟨ *g**n* + *m* ⟩, respectively: ${\begin{aligned}&z^{m}G(z)=\sum _{n=m}^{\infty }g_{n-m}z^{n}\\[4px]&{\frac {G(z)-g_{0}-g_{1}z-\cdots -g_{m-1}z^{m-1}}{z^{m}}}=\sum _{n=0}^{\infty }g_{n+m}z^{n}.\end{aligned}}$

#### Differentiation and integration of generating functions

We have the following respective power series expansions for the first derivative of a generating function and its integral: ${\begin{aligned}G'(z)&=\sum _{n=0}^{\infty }(n+1)g_{n+1}z^{n}\\[4px]z\cdot G'(z)&=\sum _{n=0}^{\infty }ng_{n}z^{n}\\[4px]\int _{0}^{z}G(t)\,dt&=\sum _{n=1}^{\infty }{\frac {g_{n-1}}{n}}z^{n}.\end{aligned}}$

The differentiation–multiplication operation of the second identity can be repeated k times to multiply the sequence by *n**k*, but that requires alternating between differentiation and multiplication. If instead doing k differentiations in sequence, the effect is to multiply by the kth falling factorial: $z^{k}G^{(k)}(z)=\sum _{n=0}^{\infty }n^{\underline {k}}g_{n}z^{n}=\sum _{n=0}^{\infty }n(n-1)\dotsb (n-k+1)g_{n}z^{n}\quad {\text{for all }}k\in \mathbb {N} .$

Using the Stirling numbers of the second kind, that can be turned into another formula for multiplying by $n^{k}$ as follows (see the main article on generating function transformations): $\sum _{j=0}^{k}{\begin{Bmatrix}k\\j\end{Bmatrix}}z^{j}F^{(j)}(z)=\sum _{n=0}^{\infty }n^{k}f_{n}z^{n}\quad {\text{for all }}k\in \mathbb {N} .$

A negative-order reversal of this sequence powers formula corresponding to the operation of repeated integration is defined by the zeta series transformation and its generalizations defined as a derivative-based transformation of generating functions, or alternately termwise by and performing an integral transformation on the sequence generating function. Related operations of performing fractional integration on a sequence generating function are discussed here.

#### Enumerating arithmetic progressions of sequences

In this section we give formulas for generating functions enumerating the sequence {*f**an* + *b*} given an ordinary generating function *F*(*z*), where *a* ≥ 2, 0 ≤ *b* < *a*, and *a* and *b* are integers (see the main article on transformations). For *a* = 2, this is simply the familiar decomposition of a function into even and odd parts (i.e., even and odd powers): ${\begin{aligned}\sum _{n=0}^{\infty }f_{2n}z^{2n}&={\frac {F(z)+F(-z)}{2}}\\[4px]\sum _{n=0}^{\infty }f_{2n+1}z^{2n+1}&={\frac {F(z)-F(-z)}{2}}.\end{aligned}}$

More generally, suppose that *a* ≥ 3 and that *ωa* = exp ⁠2*πi*/*a*⁠ denotes the ath primitive root of unity. Then, as an application of the discrete Fourier transform, we have the formula $\sum _{n=0}^{\infty }f_{an+b}z^{an+b}={\frac {1}{a}}\sum _{m=0}^{a-1}\omega _{a}^{-mb}F\left(\omega _{a}^{m}z\right).$

For integers *m* ≥ 1, another useful formula providing somewhat *reversed* floored arithmetic progressions — effectively repeating each coefficient m times — are generated by the identity $\sum _{n=0}^{\infty }f_{\left\lfloor {\frac {n}{m}}\right\rfloor }z^{n}={\frac {1-z^{m}}{1-z}}F(z^{m})=\left(1+z+\cdots +z^{m-2}+z^{m-1}\right)F(z^{m}).$

### *P*-recursive sequences and holonomic generating functions

#### Definitions

A formal power series (or function) *F*(*z*) is said to be **holonomic** if it satisfies a linear differential equation of the form $c_{0}(z)F^{(r)}(z)+c_{1}(z)F^{(r-1)}(z)+\cdots +c_{r}(z)F(z)=0,$

where the coefficients *ci*(*z*) are in the field of rational functions, $\mathbb {C} (z)$ . Equivalently, $F(z)$ is holonomic if the vector space over $\mathbb {C} (z)$ spanned by the set of all of its derivatives is finite dimensional.

Since we can clear denominators if need be in the previous equation, we may assume that the functions, *ci*(*z*) are polynomials in z. Thus we can see an equivalent condition that a generating function is holonomic if its coefficients satisfy a **P-recurrence** of the form ${\widehat {c}}_{s}(n)f_{n+s}+{\widehat {c}}_{s-1}(n)f_{n+s-1}+\cdots +{\widehat {c}}_{0}(n)f_{n}=0,$

for all large enough *n* ≥ *n*0 and where the *ĉi*(*n*) are fixed finite-degree polynomials in n. In other words, the properties that a sequence be *P-recursive* and have a holonomic generating function are equivalent. Holonomic functions are closed under the Hadamard product operation ⊙ on generating functions.

#### Examples

The functions *e**z*, log *z*, cos *z*, arcsin *z*, ${\sqrt {1+z}}$ , the dilogarithm function Li2(*z*), the generalized hypergeometric functions *pFq*(...; ...; *z*) and the functions defined by the power series $\sum _{n=0}^{\infty }{\frac {z^{n}}{(n!)^{2}}}$

and the non-convergent $\sum _{n=0}^{\infty }n!\cdot z^{n}$ are all holonomic.

Examples of P-recursive sequences with holonomic generating functions include *f**n* ≔ ⁠1/*n* + 1⁠ (2*n* *n*) and *f**n* ≔ ⁠2*n*/*n*2 + 1⁠, where sequences such as ${\sqrt {n}}$ and log *n* are *not* P-recursive due to the nature of singularities in their corresponding generating functions. Similarly, functions with infinitely many singularities such as tan *z*, sec *z*, and Γ(*z*) are *not* holonomic functions.

#### Software for working with *P*-recursive sequences and holonomic generating functions

Tools for processing and working with P-recursive sequences in *Mathematica* include the software packages provided for non-commercial use on the RISC Combinatorics Group algorithmic combinatorics software site. Despite being mostly closed-source, particularly powerful tools in this software suite are provided by the `**Guess**` package for guessing *P-recurrences* for arbitrary input sequences (useful for experimental mathematics and exploration) and the `**Sigma**` package which is able to find P-recurrences for many sums and solve for closed-form solutions to P-recurrences involving generalized harmonic numbers. Other packages listed on this particular RISC site are targeted at working with holonomic *generating functions* specifically.

### Relation to discrete-time Fourier transform

When the series converges absolutely, $G\left(a_{n};e^{-i\omega }\right)=\sum _{n=0}^{\infty }a_{n}e^{-i\omega n}$ is the discrete-time Fourier transform of the sequence *a*0, *a*1, ....

### Asymptotic growth of a sequence

In calculus, often the growth rate of the coefficients of a power series can be used to deduce a radius of convergence for the power series. The reverse can also hold; often the radius of convergence for a generating function can be used to deduce the asymptotic growth of the underlying sequence.

For instance, if an ordinary generating function *G*(*a**n*; *x*) that has a finite radius of convergence of r can be written as $G(a_{n};x)={\frac {A(x)+B(x)\left(1-{\frac {x}{r}}\right)^{-\beta }}{x^{\alpha }}}$

where each of *A*(*x*) and *B*(*x*) is a function that is analytic to a radius of convergence greater than r (or is entire), and where *B*(*r*) ≠ 0 then $a_{n}\sim {\frac {B(r)}{r^{\alpha }\Gamma (\beta )}}\,n^{\beta -1}\left({\frac {1}{r}}\right)^{n}\sim {\frac {B(r)}{r^{\alpha }}}{\binom {n+\beta -1}{n}}\left({\frac {1}{r}}\right)^{n}={\frac {B(r)}{r^{\alpha }}}\left(\!\!{\binom {\beta }{n}}\!\!\right)\left({\frac {1}{r}}\right)^{n}\,,$ using the gamma function, a binomial coefficient, or a multiset coefficient. Note that limit as n goes to infinity of the ratio of *a**n* to any of these expressions is guaranteed to be 1; not merely that *a**n* is proportional to them.

Often this approach can be iterated to generate several terms in an asymptotic series for *a**n*. In particular, $G\left(a_{n}-{\frac {B(r)}{r^{\alpha }}}{\binom {n+\beta -1}{n}}\left({\frac {1}{r}}\right)^{n};x\right)=G(a_{n};x)-{\frac {B(r)}{r^{\alpha }}}\left(1-{\frac {x}{r}}\right)^{-\beta }\,.$

The asymptotic growth of the coefficients of this generating function can then be sought via the finding of A, B, α, β, and r to describe the generating function, as above.

Similar asymptotic analysis is possible for exponential generating functions; with an exponential generating function, it is ⁠*a**n*/*n*!⁠ that grows according to these asymptotic formulae. Generally, if the generating function of one sequence minus the generating function of a second sequence has a radius of convergence that is larger than the radius of convergence of the individual generating functions then the two sequences have the same asymptotic growth.

#### Asymptotic growth of the sequence of squares

As derived above, the ordinary generating function for the sequence of squares is: $G(n^{2};x)={\frac {x(x+1)}{(1-x)^{3}}}.$

With *r* = 1, *α* = −1, *β* = 3, *A*(*x*) = 0, and *B*(*x*) = *x* + 1, we can verify that the squares grow as expected, like the squares: $a_{n}\sim {\frac {B(r)}{r^{\alpha }\Gamma (\beta )}}\,n^{\beta -1}\left({\frac {1}{r}}\right)^{n}={\frac {1+1}{1^{-1}\,\Gamma (3)}}\,n^{3-1}\left({\frac {1}{1}}\right)^{n}=n^{2}.$

#### Asymptotic growth of the Catalan numbers

The ordinary generating function for the Catalan numbers is $G(C_{n};x)={\frac {1-{\sqrt {1-4x}}}{2x}}.$

With *r* = ⁠1/4⁠, *α* = 1, *β* = −⁠1/2⁠, *A*(*x*) = ⁠1/2⁠, and *B*(*x*) = −⁠1/2⁠, we can conclude that, for the Catalan numbers: $C_{n}\sim {\frac {B(r)}{r^{\alpha }\Gamma (\beta )}}\,n^{\beta -1}\left({\frac {1}{r}}\right)^{n}={\frac {-{\frac {1}{2}}}{\left({\frac {1}{4}}\right)^{1}\Gamma \left(-{\frac {1}{2}}\right)}}\,n^{-{\frac {1}{2}}-1}\left({\frac {1}{\,{\frac {1}{4}}\,}}\right)^{n}={\frac {4^{n}}{n^{\frac {3}{2}}{\sqrt {\pi }}}}.$

### Bivariate and multivariate generating functions

The generating function in several variables can be generalized to arrays with multiple indices. These non-polynomial double sum examples are called **multivariate generating functions**, or **super generating functions**. For two variables, these are often called **bivariate generating functions**.

#### Bivariate case

The ordinary generating function of a two-dimensional array *a**m*,*n* (where n and m are natural numbers) is: $G(a_{m,n};x,y)=\sum _{m,n=0}^{\infty }a_{m,n}x^{m}y^{n}.$ For instance, since (1 + *x*)*n* is the ordinary generating function for binomial coefficients for a fixed n, one may ask for a bivariate generating function that generates the binomial coefficients (*n* *k*) for all k and n. To do this, consider (1 + *x*)*n* itself as a sequence in n, and find the generating function in y that has these sequence values as coefficients. Since the generating function for *a**n* is: ${\frac {1}{1-ay}},$ the generating function for the binomial coefficients is: $\sum _{n,k}{\binom {n}{k}}x^{k}y^{n}={\frac {1}{1-(1+x)y}}={\frac {1}{1-y-xy}}.$ Other examples of such include the following two-variable generating functions for the binomial coefficients, the Stirling numbers, and the Eulerian numbers, where *ω* and *z* denote the two variables: ${\begin{aligned}e^{z+wz}&=\sum _{m,n\geq 0}{\binom {n}{m}}w^{m}{\frac {z^{n}}{n!}}\\[4px]e^{w(e^{z}-1)}&=\sum _{m,n\geq 0}{\begin{Bmatrix}n\\m\end{Bmatrix}}w^{m}{\frac {z^{n}}{n!}}\\[4px]{\frac {1}{(1-z)^{w}}}&=\sum _{m,n\geq 0}{\begin{bmatrix}n\\m\end{bmatrix}}w^{m}{\frac {z^{n}}{n!}}\\[4px]{\frac {1-w}{e^{(w-1)z}-w}}&=\sum _{m,n\geq 0}\left\langle {\begin{matrix}n\\m\end{matrix}}\right\rangle w^{m}{\frac {z^{n}}{n!}}\\[4px]{\frac {e^{w}-e^{z}}{we^{z}-ze^{w}}}&=\sum _{m,n\geq 0}\left\langle {\begin{matrix}m+n+1\\m\end{matrix}}\right\rangle {\frac {w^{m}z^{n}}{(m+n+1)!}}.\end{aligned}}$

#### Multivariate case

Multivariate generating functions arise in practice when calculating the number of contingency tables of non-negative integers with specified row and column totals. Suppose the table has r rows and c columns; the row sums are *t*1, *t*2 ... *tr* and the column sums are *s*1, *s*2 ... *sc*. Then, according to I. J. Good, the number of such tables is the coefficient of: $x_{1}^{t_{1}}\cdots x_{r}^{t_{r}}y_{1}^{s_{1}}\cdots y_{c}^{s_{c}}$ in: $\prod _{i=1}^{r}\prod _{j=1}^{c}{\frac {1}{1-x_{i}y_{j}}}.$

### Representation by continued fractions (Jacobi-type *J*-fractions)

#### Definitions

Expansions of (formal) *Jacobi-type* and *Stieltjes-type* continued fractions (*J-fractions* and *S-fractions*, respectively) whose hth rational convergents represent 2*h*-order accurate power series are another way to express the typically divergent ordinary generating functions for many special one and two-variate sequences. The particular form of the Jacobi-type continued fractions (J-fractions) are expanded as in the following equation and have the next corresponding power series expansions with respect to z for some specific, application-dependent component sequences, {ab*i*} and {*c**i*}, where *z* ≠ 0 denotes the formal variable in the second power series expansion given below: ${\begin{aligned}J^{[\infty ]}(z)&={\cfrac {1}{1-c_{1}z-{\cfrac {{\text{ab}}_{2}z^{2}}{1-c_{2}z-{\cfrac {{\text{ab}}_{3}z^{2}}{\ddots }}}}}}\\[4px]&=1+c_{1}z+\left({\text{ab}}_{2}+c_{1}^{2}\right)z^{2}+\left(2{\text{ab}}_{2}c_{1}+c_{1}^{3}+{\text{ab}}_{2}c_{2}\right)z^{3}+\cdots \end{aligned}}$

The coefficients of $z^{n}$ , denoted in shorthand by *jn* ≔ [*zn*] *J*[∞](*z*), in the previous equations correspond to matrix solutions of the equations: ${\begin{bmatrix}k_{0,1}&k_{1,1}&0&0&\cdots \\k_{0,2}&k_{1,2}&k_{2,2}&0&\cdots \\k_{0,3}&k_{1,3}&k_{2,3}&k_{3,3}&\cdots \\\vdots &\vdots &\vdots &\vdots \end{bmatrix}}={\begin{bmatrix}k_{0,0}&0&0&0&\cdots \\k_{0,1}&k_{1,1}&0&0&\cdots \\k_{0,2}&k_{1,2}&k_{2,2}&0&\cdots \\\vdots &\vdots &\vdots &\vdots \end{bmatrix}}\cdot {\begin{bmatrix}c_{1}&1&0&0&\cdots \\{\text{ab}}_{2}&c_{2}&1&0&\cdots \\0&{\text{ab}}_{3}&c_{3}&1&\cdots \\\vdots &\vdots &\vdots &\vdots \end{bmatrix}},$

where *j*0 ≡ *k*0,0 = 1, *jn* = *k*0,*n* for *n* ≥ 1, *k**r*,*s* = 0 if *r* > *s*, and where for all integers *p*, *q* ≥ 0, we have an *addition formula* relation given by: $j_{p+q}=k_{0,p}\cdot k_{0,q}+\sum _{i=1}^{\min(p,q)}{\text{ab}}_{2}\cdots {\text{ab}}_{i+1}\times k_{i,p}\cdot k_{i,q}.$

#### Properties of the *h*th convergent functions

For *h* ≥ 0 (though in practice when *h* ≥ 2), we can define the rational hth convergents to the infinite J-fraction, *J*[∞](*z*), expanded by: $\operatorname {Conv} _{h}(z):={\frac {P_{h}(z)}{Q_{h}(z)}}=j_{0}+j_{1}z+\cdots +j_{2h-1}z^{2h-1}+\sum _{n=2h}^{\infty }{\widetilde {j}}_{h,n}z^{n}$

component-wise through the sequences, *Ph*(*z*) and *Qh*(*z*), defined recursively by: ${\begin{aligned}P_{h}(z)&=(1-c_{h}z)P_{h-1}(z)-{\text{ab}}_{h}z^{2}P_{h-2}(z)+\delta _{h,1}\\Q_{h}(z)&=(1-c_{h}z)Q_{h-1}(z)-{\text{ab}}_{h}z^{2}Q_{h-2}(z)+(1-c_{1}z)\delta _{h,1}+\delta _{0,1}.\end{aligned}}$

Moreover, the rationality of the convergent function Conv*h*(*z*) for all *h* ≥ 2 implies additional finite difference equations and congruence properties satisfied by the sequence of *jn*, *and* for *Mh* ≔ ab2 ⋯ ab*h* + 1 if *h* ‖ *M**h* then we have the congruence $j_{n}\equiv [z^{n}]\operatorname {Conv} _{h}(z){\pmod {h}},$

for non-symbolic, determinate choices of the parameter sequences {ab*i*} and {*c**i*} when *h* ≥ 2, that is, when these sequences do not implicitly depend on an auxiliary parameter such as q, x, or R as in the examples contained in the table below.

#### Examples

The next table provides examples of closed-form formulas for the component sequences found computationally (and subsequently proved correct in the cited references) in several special cases of the prescribed sequences, *jn*, generated by the general expansions of the J-fractions defined in the first subsection. Here we define 0 < |*a*|, |*b*|, |*q*| < 1 and the parameters $R,\alpha \in \mathbb {Z} ^{+}$ and x to be indeterminates with respect to these expansions, where the prescribed sequences enumerated by the expansions of these J-fractions are defined in terms of the q-Pochhammer symbol, Pochhammer symbol, and the binomial coefficients.

| $j_{n}$ | $c_{1}$ | $c_{i}(i\geq 2)$ | $\mathrm {ab} _{i}(i\geq 2)$ |
|---|---|---|---|
| $q^{n^{2}}$ | q | $q^{2h-3}\left(q^{2h}+q^{2h-2}-1\right)$ | $q^{6h-10}\left(q^{2h-2}-1\right)$ |
| $(a;q)_{n}$ | $1-a$ | $q^{h-1}-aq^{h-2}\left(q^{h}+q^{h-1}-1\right)$ | $aq^{2h-4}\left(aq^{h-2}-1\right)\left(q^{h-1}-1\right)$ |
| $\left(zq^{-n};q\right)_{n}$ | ${\frac {q-z}{q}}$ | ${\frac {q^{h}-z-qz+q^{h}z}{q^{2h-1}}}$ | ${\frac {\left(q^{h-1}-1\right)\left(q^{h-1}-z\right)\cdot z}{q^{4h-5}}}$ |
| ${\frac {(a;q)_{n}}{(b;q)_{n}}}$ | ${\frac {1-a}{1-b}}$ | ${\frac {q^{i-2}\left(q+abq^{2i-3}+a(1-q^{i-1}-q^{i})+b(q^{i}-q-1)\right)}{\left(1-bq^{2i-4}\right)\left(1-bq^{2i-2}\right)}}$ | ${\frac {q^{2i-4}\left(1-bq^{i-3}\right)\left(1-aq^{i-2}\right)\left(a-bq^{i-2}\right)\left(1-q^{i-1}\right)}{\left(1-bq^{2i-5}\right)\left(1-bq^{2i-4}\right)^{2}\left(1-bq^{2i-3}\right)}}$ |
| $\alpha ^{n}\cdot \left({\frac {R}{\alpha }}\right)_{n}$ | R | $R+2\alpha (i-1)$ | $(i-1)\alpha {\bigl (}R+(i-2)\alpha {\bigr )}$ |
| $(-1)^{n}{\binom {x}{n}}$ | $-x$ | $-{\frac {(x+2(i-1)^{2})}{(2i-1)(2i-3)}}$ | ${\begin{cases}-{\dfrac {(x-i+2)(x+i-1)}{4\cdot (2i-3)^{2}}}&{\text{for }}i\geq 3;\\[4px]-{\frac {1}{2}}x(x+1)&{\text{for }}i=2.\end{cases}}$ |
| $(-1)^{n}{\binom {x+n}{n}}$ | $-(x+1)$ | ${\frac {{\bigl (}x-2i(i-2)-1{\bigr )}}{(2i-1)(2i-3)}}$ | ${\begin{cases}-{\dfrac {(x-i+2)(x+i-1)}{4\cdot (2i-3)^{2}}}&{\text{for }}i\geq 3;\\[4px]-{\frac {1}{2}}x(x+1)&{\text{for }}i=2.\end{cases}}$ |

The radii of convergence of these series corresponding to the definition of the Jacobi-type J-fractions given above are in general different from that of the corresponding power series expansions defining the ordinary generating functions of these sequences.


## Examples

### Square numbers

Generating functions for the sequence of square numbers *a**n* = *n*2 are:

| Generating function type | Equation |
|---|---|
| Ordinary generating function | $G(n^{2};x)=\sum _{n=0}^{\infty }n^{2}x^{n}={\frac {x(x+1)}{(1-x)^{3}}}$ |
| Exponential generating function | $\operatorname {EG} (n^{2};x)=\sum _{n=0}^{\infty }{\frac {n^{2}x^{n}}{n!}}=x(x+1)e^{x}$ |
| Bell series | $\operatorname {BG} _{p}\left(n^{2};x\right)=\sum _{n=0}^{\infty }\left(p^{n}\right)^{2}x^{n}={\frac {1}{1-p^{2}x}}$ |
| Dirichlet series | $\operatorname {DG} \left(n^{2};s\right)=\sum _{n=1}^{\infty }{\frac {n^{2}}{n^{s}}}=\zeta (s-2)$ |

where *ζ*(*s)* is the Riemann zeta function.
