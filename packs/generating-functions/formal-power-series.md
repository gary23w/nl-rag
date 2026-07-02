---
title: "Formal power series"
source: https://en.wikipedia.org/wiki/Formal_power_series
domain: generating-functions
license: CC-BY-SA-4.0
tags: generating function, formal power series, catalan number, binomial coefficient
fetched: 2026-07-02
---

# Formal power series

In mathematics, a **formal series** is an infinite sum that is considered independently from any notion of convergence, and can be manipulated with the usual algebraic operations on series (addition, subtraction, multiplication, division, partial sums, etc.).

A **formal power series** is a special kind of formal series, of the form $\sum _{n=0}^{\infty }a_{n}x^{n}=a_{0}+a_{1}x+a_{2}x^{2}+\cdots ,$ where the $a_{n},$ called *coefficients*, are numbers or, more generally, elements of some ring, and the $x^{n}$ are formal powers of the symbol x that is called an indeterminate or, commonly, a variable. Hence, formal power series can be viewed as a generalization of polynomials where the number of terms is allowed to be infinite, and differ from usual power series by the absence of convergence requirements, which implies that a formal power series may not represent a function of its variables. Formal power series are in one to one correspondence with their sequences of coefficients, but the two concepts must not be confused, since the operations that can be applied are different.

A formal power series with coefficients in a ring R is called a formal power series over $R.$ The formal power series over a ring R form a ring, commonly denoted by $R[[x]].$ (It can be seen as the (*x*)-adic completion of the polynomial ring $R[x],$ in the same way as the p-adic integers are the p-adic completion of the ring of the integers.)

Formal powers series in several indeterminates are defined similarly by replacing the powers of a single indeterminate by monomials in several indeterminates.

Formal power series are widely used in combinatorics for representing sequences of integers as generating functions. In this context, a recurrence relation between the elements of a sequence may often be interpreted as a differential equation that the generating function satisfies. This allows using methods of complex analysis for combinatorial problems (see analytic combinatorics).

## Introduction

A formal power series can be loosely thought of as an object that is like a polynomial, but with infinitely many terms. Alternatively, for those familiar with power series (or Taylor series), one may think of a formal power series as a power series in which we ignore questions of convergence by not assuming that the variable *X* denotes any numerical value (not even an unknown value). For example, consider the series $A=1-3X+5X^{2}-7X^{3}+9X^{4}-11X^{5}+\cdots .$ If we studied this as a power series, its properties would include, for example, that its radius of convergence is 1 by the Cauchy–Hadamard theorem. However, as a formal power series, we may ignore this completely; all that is relevant is the sequence of coefficients [1, −3, 5, −7, 9, −11, ...]. In other words, a formal power series is an object that just records a sequence of coefficients. It is perfectly acceptable to consider a formal power series with the factorials [1, 1, 2, 6, 24, 120, 720, 5040, ... ] as coefficients, even though the corresponding power series diverges for any nonzero value of *X*.

Algebra on formal power series is carried out by simply pretending that the series are polynomials. For example, if

$B=2X+4X^{3}+6X^{5}+\cdots ,$

then we add *A* and *B* term by term:

$A+B=1-X+5X^{2}-3X^{3}+9X^{4}-5X^{5}+\cdots .$

We can multiply formal power series, again just by treating them as polynomials (see in particular Cauchy product):

$AB=2X-6X^{2}+14X^{3}-26X^{4}+44X^{5}+\cdots .$

Notice that each coefficient in the product *AB* only depends on a *finite* number of coefficients of *A* and *B*. For example, the *X*5 term is given by

$44X^{5}=(1\times 6X^{5})+(5X^{2}\times 4X^{3})+(9X^{4}\times 2X).$

For this reason, one may multiply formal power series without worrying about the usual questions of absolute, conditional and uniform convergence which arise in dealing with power series in the setting of analysis.

Once we have defined multiplication for formal power series, we can define multiplicative inverses as follows. The multiplicative inverse of a formal power series *A* is a formal power series *C* such that *AC* = 1, provided that such a formal power series exists. It turns out that if *A* has a multiplicative inverse, it is unique, and we denote it by *A*−1. Now we can define division of formal power series by defining *B*/*A* to be the product *BA*−1, provided that the inverse of *A* exists. For example, one can use the definition of multiplication above to verify the familiar formula

${\frac {1}{1+X}}=1-X+X^{2}-X^{3}+X^{4}-X^{5}+\cdots .$

An important operation on formal power series is coefficient extraction. In its most basic form, the coefficient extraction operator $[X^{n}]$ applied to a formal power series A in one variable extracts the coefficient of the n th power of the variable, so that $[X^{2}]A=5$ and $[X^{5}]A=-11$ . Other examples include

${\begin{aligned}\left[X^{3}\right](B)&=4,\\\left[X^{2}\right](X+3X^{2}Y^{3}+10Y^{6})&=3Y^{3},\\\left[X^{2}Y^{3}\right](X+3X^{2}Y^{3}+10Y^{6})&=3,\\\left[X^{n}\right]\left({\frac {1}{1+X}}\right)&=(-1)^{n},\\\left[X^{n}\right]\left({\frac {X}{(1-X)^{2}}}\right)&=n.\end{aligned}}$

Similarly, many other operations that are carried out on polynomials can be extended to the formal power series setting, as explained below.

## The ring of formal power series

If one considers the set of all formal power series in *X* with coefficients in a commutative ring *R*, the elements of this set collectively constitute another ring which is written $R[[X]],$ and called the **ring of formal power series** in the variable *X* over *R*.

### Definition of the formal power series ring

One can characterize $R[[X]]$ abstractly as the completion of the polynomial ring $R[X]$ equipped with a particular metric. This automatically gives $R[[X]]$ the structure of a topological ring (and even of a complete metric space). But the general construction of a completion of a metric space is more involved than what is needed here, and would make formal power series seem more complicated than they are. It is possible to describe $R[[X]]$ more explicitly, and define the ring structure and topological structure separately, as follows.

#### Ring structure

As a set, $R[[X]]$ can be constructed as the set $R^{\mathbb {N} }$ of all infinite sequences of elements of R , indexed by the natural numbers (taken to include 0). Designating a sequence whose term at index n is $a_{n}$ by $(a_{n})$ , one defines addition of two such sequences by

$(a_{n})_{n\in \mathbb {N} }+(b_{n})_{n\in \mathbb {N} }=\left(a_{n}+b_{n}\right)_{n\in \mathbb {N} }$

and multiplication by

$(a_{n})_{n\in \mathbb {N} }\times (b_{n})_{n\in \mathbb {N} }=\left(\sum _{k=0}^{n}a_{k}b_{n-k}\right)_{\!n\in \mathbb {N} }.$

This type of product is called the Cauchy product of the two sequences of coefficients, and is a sort of discrete convolution. With these operations, $R^{\mathbb {N} }$ becomes a commutative ring with zero element $(0,0,0,\ldots )$ and multiplicative identity $(1,0,0,\ldots )$ .

The product is in fact the same one used to define the product of polynomials in one indeterminate, which suggests using a similar notation. One embeds R into $R[[X]]$ by sending any (constant) $a\in R$ to the sequence $(a,0,0,\ldots )$ and designates the sequence $(0,1,0,0,\ldots )$ by X ; then using the above definitions every sequence with only finitely many nonzero terms can be expressed in terms of these special elements as

$(a_{0},a_{1},a_{2},\ldots ,a_{n},0,0,\ldots )=a_{0}+a_{1}X+\cdots +a_{n}X^{n}=\sum _{i=0}^{n}a_{i}X^{i};$

these are precisely the polynomials in X . Given this, it is quite natural and convenient to designate a general sequence $(a_{n})_{n\in \mathbb {N} }$ by the formal expression $\textstyle \sum _{i\in \mathbb {N} }a_{i}X^{i}$ , even though the latter *is not* an expression formed by the operations of addition and multiplication defined above (from which only finite sums can be constructed). This notational convention allows reformulation of the above definitions as

$\left(\sum _{i\in \mathbb {N} }a_{i}X^{i}\right)+\left(\sum _{i\in \mathbb {N} }b_{i}X^{i}\right)=\sum _{i\in \mathbb {N} }(a_{i}+b_{i})X^{i}$

and

$\left(\sum _{i\in \mathbb {N} }a_{i}X^{i}\right)\times \left(\sum _{i\in \mathbb {N} }b_{i}X^{i}\right)=\sum _{n\in \mathbb {N} }\left(\sum _{k=0}^{n}a_{k}b_{n-k}\right)X^{n}.$

which is quite convenient, but one must be aware of the distinction between formal summation (a mere convention) and actual addition.

#### Topological structure

Having stipulated conventionally that

| $(a_{0},a_{1},a_{2},a_{3},\ldots )=\sum _{i=0}^{\infty }a_{i}X^{i},$ |   | 1 |
|---|---|---|

one would like to interpret the right hand side as a well-defined infinite summation. To that end, a notion of convergence in $R^{\mathbb {N} }$ is defined and a topology on $R^{\mathbb {N} }$ is constructed. There are several equivalent ways to define the desired topology.

- We may give $R^{\mathbb {N} }$ the product topology, where each copy of R is given the discrete topology.
- We may give $R^{\mathbb {N} }$ the I-adic topology, where $I=(X)$ is the ideal generated by X , which consists of all sequences whose first term $a_{0}$ is zero.
- The desired topology could also be derived from the following metric. The distance between distinct sequences $(a_{n}),(b_{n})\in R^{\mathbb {N} },$ is defined to be $d((a_{n}),(b_{n}))=2^{-k},$ where k is the smallest natural number such that $a_{k}\neq b_{k}$ ; the distance between two equal sequences is of course zero.

Informally, two sequences $(a_{n})$ and $(b_{n})$ become closer and closer if and only if more and more of their terms agree exactly. Formally, the sequence of partial sums of some infinite summation converges if for every fixed power of X the coefficient stabilizes: there is a point beyond which all further partial sums have the same coefficient. This is clearly the case for the right hand side of (**1**), regardless of the values $a_{n}$ , since inclusion of the term for $i=n$ gives the last (and in fact only) change to the coefficient of $X^{n}$ . It is also obvious that the limit of the sequence of partial sums is equal to the left hand side.

This topological structure, together with the ring operations described above, form a topological ring. This is called the **ring of formal power series over R** and is denoted by $R[[X]]$ . The topology has the useful property that an infinite summation converges if and only if the sequence of its terms converges to 0, which just means that any fixed power of X occurs in only finitely many terms.

The topological structure allows much more flexible usage of infinite summations. For instance the rule for multiplication can be restated simply as

$\left(\sum _{i\in \mathbb {N} }a_{i}X^{i}\right)\times \left(\sum _{i\in \mathbb {N} }b_{i}X^{i}\right)=\sum _{i,j\in \mathbb {N} }a_{i}b_{j}X^{i+j},$

since only finitely many terms on the right affect any fixed $X^{n}$ . Infinite products are also defined by the topological structure; it can be seen that an infinite product converges if and only if the sequence of its factors converges to 1 (in which case the product is nonzero) or infinitely many factors have no constant term (in which case the product is zero).

#### Alternative topologies

The above topology is the finest topology for which

$\sum _{i=0}^{\infty }a_{i}X^{i}$

always converges as a summation to the formal power series designated by the same expression, and it often suffices to give a meaning to infinite sums and products, or other kinds of limits that one wishes to use to designate particular formal power series. It can however happen occasionally that one wishes to use a coarser topology, so that certain expressions become convergent that would otherwise diverge. This applies in particular when the base ring R already comes with a topology other than the discrete one, for instance if it is also a ring of formal power series.

In the ring of formal power series $\mathbb {Z} [[X]][[Y]]$ , the topology of above construction only relates to the indeterminate Y , since the topology that was put on $\mathbb {Z} [[X]]$ has been replaced by the discrete topology when defining the topology of the whole ring. So

$\sum _{i=0}^{\infty }XY^{i}$

converges (and its sum can be written as ${\tfrac {X}{1-Y}}$ ); however

$\sum _{i=0}^{\infty }X^{i}Y$

would be considered to be divergent, since every term affects the coefficient of Y . This asymmetry disappears if the power series ring in Y is given the product topology where each copy of $\mathbb {Z} [[X]]$ is given its topology as a ring of formal power series rather than the discrete topology. With this topology, a sequence of elements of $\mathbb {Z} [[X]][[Y]]$ converges if the coefficient of each power of Y converges to a formal power series in X , a weaker condition than stabilizing entirely. For instance, with this topology, in the second example given above, the coefficient of Y converges to ${\tfrac {1}{1-X}}$ , so the whole summation converges to ${\tfrac {Y}{1-X}}$ .

This way of defining the topology is in fact the standard one for repeated constructions of rings of formal power series, and gives the same topology as one would get by taking formal power series in all indeterminates at once. In the above example that would mean constructing $\mathbb {Z} [[X,Y]]$ and here a sequence converges if and only if the coefficient of every monomial $X^{i}Y^{j}$ stabilizes. This topology, which is also the I -adic topology, where $I=(X,Y)$ is the ideal generated by X and Y , still enjoys the property that a summation converges if and only if its terms tend to 0.

The same principle could be used to make other divergent limits converge. For instance in $\mathbb {R} [[X]]$ the limit

$\lim _{n\to \infty }\left(1+{\frac {X}{n}}\right)^{\!n}$

does not exist, so in particular it does not converge to

$\exp(X)=\sum _{n\in \mathbb {N} }{\frac {X^{n}}{n!}}.$

This is because for $i\geq 2$ the coefficient ${\tbinom {n}{i}}/n^{i}$ of $X^{i}$ does not stabilize as $n\to \infty$ . It does however converge in the usual topology of $\mathbb {R}$ , and in fact to the coefficient ${\tfrac {1}{i!}}$ of $\exp(X)$ . Therefore, if one would give $\mathbb {R} [[X]]$ the product topology of $\mathbb {R} ^{\mathbb {N} }$ where the topology of $\mathbb {R}$ is the usual topology rather than the discrete one, then the above limit would converge to $\exp(X)$ . This more permissive approach is not however the standard when considering formal power series, as it would lead to convergence considerations that are as subtle as they are in analysis, while the philosophy of formal power series is on the contrary to make convergence questions as trivial as they can possibly be. With this topology it would *not* be the case that a summation converges if and only if its terms tend to 0.

### Universal property

The ring $R[[X]]$ may be characterized by the following universal property. If S is a commutative associative algebra over R , if I is an ideal of S such that the I -adic topology on S is complete, and if x is an element of I , then there is a *unique* $\Phi :R[[X]]\to S$ with the following properties:

- $\Phi$ is an R -algebra homomorphism
- $\Phi$ is continuous
- $\Phi (X)=x$ .

## Operations on formal power series

One can perform algebraic operations on power series to generate new power series.

### Power series raised to powers

For any natural number *n*, the nth power of a formal power series S is defined recursively by ${\begin{aligned}S^{1}&=S\\S^{n}&=S\cdot S^{n-1}\quad {\text{for }}n>1.\end{aligned}}$ If *a*0 is invertible in the ring of coefficients, one can prove that in the expansion ${\Big (}\sum _{k=0}^{\infty }a_{k}X^{k}{\Big )}^{n}=\sum _{m=0}^{\infty }c_{m}X^{m},$ the coefficients are given by $c_{0}=a_{0}^{n}$ and $c_{m}={\frac {1}{ma_{0}}}\sum _{k=1}^{m}(kn-m+k)a_{k}c_{m-k}$ for $m\geq 1$ if m is invertible in the ring of coefficients. In the case of formal power series with complex coefficients, its complex powers are well defined for series *f* with constant term equal to 1. In this case, $f^{\alpha }$ can be defined either by composition with the binomial series (1 + *x*)*α*, or by composition with the exponential and the logarithmic series, $f^{\alpha }=\exp(\alpha \log(f)),$ or as the solution of the differential equation (in terms of series) $f(f^{\alpha })'=\alpha f^{\alpha }f'$ with constant term 1; the three definitions are equivalent. The exponent rules $(f^{\alpha })^{\beta }=f^{\alpha \beta }$ and $f^{\alpha }g^{\alpha }=(fg)^{\alpha }$ easily follow for formal power series *f*, *g*.

### Multiplicative inverse

The series

$A=\sum _{n=0}^{\infty }a_{n}X^{n}\in R[[X]]$

is invertible in $R[[X]]$ if and only if its constant coefficient $a_{0}$ is invertible in R . This condition is necessary, for the following reason: if we suppose that A has an inverse $B=b_{0}+b_{1}x+\cdots$ then the constant term $a_{0}b_{0}$ of $A\cdot B$ is the constant term of the identity series, i.e. it is 1. This condition is also sufficient; we may compute the coefficients of the inverse series B via the explicit recursive formula

${\begin{aligned}b_{0}&={\frac {1}{a_{0}}},\\b_{n}&=-{\frac {1}{a_{0}}}\sum _{i=1}^{n}a_{i}b_{n-i},\ \ \ n\geq 1.\end{aligned}}$

An important special case is that the geometric series formula is valid in $R[[X]]$ :

$(1-X)^{-1}=\sum _{n=0}^{\infty }X^{n}.$

If $R=K$ is a field, then a series is invertible if and only if the constant term is non-zero, i.e. if and only if the series is not divisible by X . This means that $K[[X]]$ is a discrete valuation ring with uniformizing parameter X .

### Division

The computation of a quotient $f/g=h$

${\frac {\sum _{n=0}^{\infty }b_{n}X^{n}}{\sum _{n=0}^{\infty }a_{n}X^{n}}}=\sum _{n=0}^{\infty }c_{n}X^{n},$

assuming the denominator is invertible (that is, $a_{0}$ is invertible in the ring of scalars), can be performed as a product f and the inverse of g , or directly equating the coefficients in $f=gh$ :

$c_{n}={\frac {1}{a_{0}}}\left(b_{n}-\sum _{k=1}^{n}a_{k}c_{n-k}\right).$

### Extracting coefficients

The coefficient extraction operator applied to a formal power series

$f(X)=\sum _{n=0}^{\infty }a_{n}X^{n}$

in *X* is written

$\left[X^{m}\right]f(X)$

and extracts the coefficient of *Xm*, so that

$\left[X^{m}\right]f(X)=\left[X^{m}\right]\sum _{n=0}^{\infty }a_{n}X^{n}=a_{m}.$

### Composition

Given two formal power series

$f(X)=\sum _{n=1}^{\infty }a_{n}X^{n}=a_{1}X+a_{2}X^{2}+\cdots$

$g(X)=\sum _{n=0}^{\infty }b_{n}X^{n}=b_{0}+b_{1}X+b_{2}X^{2}+\cdots$

such that $a_{0}=0,$ one may form the *composition*

$g(f(X))=\sum _{n=0}^{\infty }b_{n}(f(X))^{n}=\sum _{n=0}^{\infty }c_{n}X^{n},$

where the coefficients *c**n* are determined by "expanding out" the powers of *f*(*X*):

$c_{n}:=\sum _{k\in \mathbb {N} ,|j|=n}b_{k}a_{j_{1}}a_{j_{2}}\cdots a_{j_{k}}.$

Here the sum is extended over all (*k*, *j*) with $k\in \mathbb {N}$ and $j\in \mathbb {N} _{+}^{k}$ with $|j|:=j_{1}+\cdots +j_{k}=n.$

Since $a_{0}=0,$ one must have $k\leq n$ and $j_{i}\leq n$ for every $i.$ This implies that the above sum is finite and that the coefficient $c_{n}$ is the coefficient of $X^{n}$ in the polynomial $g_{n}(f_{n}(X))$ , where $f_{n}$ and $g_{n}$ are the polynomials obtained by truncating the series at $x^{n},$ that is, by removing all terms involving a power of X higher than $n.$

A more explicit description of these coefficients is provided by Faà di Bruno's formula, at least in the case where the coefficient ring is a field of characteristic 0.

Composition is only valid when $f(X)$ has *no constant term*, so that each $c_{n}$ depends on only a finite number of coefficients of $f(X)$ and $g(X)$ . In other words, the series for $g(f(X))$ converges in the topology of $R[[X]]$ .

#### Example

Assume that the ring R has characteristic 0 and the nonzero integers are invertible in R . If one denotes by $\exp(X)$ the formal power series

$\exp(X)=1+X+{\frac {X^{2}}{2!}}+{\frac {X^{3}}{3!}}+{\frac {X^{4}}{4!}}+\cdots ,$

then the equality

$\exp(\exp(X)-1)=1+X+X^{2}+{\frac {5X^{3}}{6}}+{\frac {5X^{4}}{8}}+\cdots$

makes perfect sense as a formal power series, since the constant coefficient of $\exp(X)-1$ is zero.

### Composition inverse

Whenever a formal series

$f(X)=\sum _{k}f_{k}X^{k}\in R[[X]]$

has *f*0 = 0 and *f*1 being an invertible element of *R*, there exists a series

$g(X)=\sum _{k}g_{k}X^{k}$

that is the composition inverse of f , meaning that composing f with g gives the series representing the identity function $x=0+1x+0x^{2}+0x^{3}+\cdots$ . The coefficients of g may be found recursively by using the above formula for the coefficients of a composition, equating them with those of the composition identity *X* (that is 1 at degree 1 and 0 at every degree greater than 1). In the case when the coefficient ring is a field of characteristic 0, the Lagrange inversion formula (discussed below) provides a powerful tool to compute the coefficients of *g*, as well as the coefficients of the (multiplicative) powers of *g*.

### Formal differentiation

Given a formal power series

$f=\sum _{n\geq 0}a_{n}X^{n}\in R[[X]],$

we define its **formal derivative**, denoted *Df* or *f* ′, by

$Df=f'=\sum _{n\geq 1}a_{n}nX^{n-1}.$

The symbol *D* is called the **formal differentiation operator**. This definition simply mimics term-by-term differentiation of a polynomial.

This operation is *R*-linear:

$D(af+bg)=a\cdot Df+b\cdot Dg$

for any *a*, *b* in *R* and any *f*, *g* in $R[[X]].$ Additionally, the formal derivative has many of the properties of the usual derivative of calculus. For example, the product rule is valid:

$D(fg)\ =\ f\cdot (Dg)+(Df)\cdot g,$

and the chain rule works as well:

$D(f\circ g)=(Df\circ g)\cdot Dg,$

whenever the appropriate compositions of series are defined (see above under composition of series).

Thus, in these respects formal power series behave like Taylor series. Indeed, for the *f* defined above, we find that

$(D^{k}f)(0)=k!a_{k},$

where *D**k* denotes the *k*th formal derivative (that is, the result of formally differentiating *k* times).

### Formal antidifferentiation

If R is a ring with characteristic zero and the nonzero integers are invertible in R , then given a formal power series

$f=\sum _{n\geq 0}a_{n}X^{n}\in R[[X]],$

we define its **formal antiderivative** or **formal indefinite integral** by

$D^{-1}f=\int f\ dX=C+\sum _{n\geq 0}a_{n}{\frac {X^{n+1}}{n+1}}.$

for any constant $C\in R$ .

This operation is *R*-linear:

$D^{-1}(af+bg)=a\cdot D^{-1}f+b\cdot D^{-1}g$

for any *a*, *b* in *R* and any *f*, *g* in $R[[X]].$ Additionally, the formal antiderivative has many of the properties of the usual antiderivative of calculus. For example, the formal antiderivative is the right inverse of the formal derivative:

$D(D^{-1}(f))=f$

for any $f\in R[[X]]$ .

## Properties

### Algebraic properties of the formal power series ring

$R[[X]]$ is an associative algebra over R which contains the ring $R[X]$ of polynomials over R ; the polynomials correspond to the sequences which end in zeros.

The Jacobson radical of $R[[X]]$ is the ideal generated by X and the Jacobson radical of R ; this is implied by the element invertibility criterion discussed above.

The maximal ideals of $R[[X]]$ all arise from those in R in the following manner: an ideal M of $R[[X]]$ is maximal if and only if $M\cap R$ is a maximal ideal of R and M is generated as an ideal by X and $M\cap R$ .

Several algebraic properties of R are inherited by $R[[X]]$ :

- if R is a local ring, then so is $R[[X]]$ (with the set of non units the unique maximal ideal),
- if R is Noetherian, then so is $R[[X]]$ (a version of the Hilbert basis theorem),
- if R is an integral domain, then so is $R[[X]]$ , and
- if K is a field, then $K[[X]]$ is a discrete valuation ring.

### Topological properties of the formal power series ring

The metric space $(R[[X]],d)$ is complete.

The ring $R[[X]]$ is compact if and only if *R* is finite. This follows from Tychonoff's theorem and the characterisation of the topology on $R[[X]]$ as a product topology.

### Weierstrass preparation

The ring of formal power series with coefficients in a complete local ring satisfies the Weierstrass preparation theorem.

## Applications

Formal power series can be used to solve recurrences occurring in number theory and combinatorics. For an example involving finding a closed form expression for the Fibonacci numbers, see the article on Examples of generating functions.

One can use formal power series to prove several relations familiar from analysis in a purely algebraic setting. Consider for instance the following elements of $\mathbb {Q} [[X]]$ :

$\sin(X):=\sum _{n\geq 0}{\frac {(-1)^{n}}{(2n+1)!}}X^{2n+1}$

$\cos(X):=\sum _{n\geq 0}{\frac {(-1)^{n}}{(2n)!}}X^{2n}$

Then one can show that

$\sin ^{2}(X)+\cos ^{2}(X)=1,$

${\frac {\partial }{\partial X}}\sin(X)=\cos(X),$

$\sin(X+Y)=\sin(X)\cos(Y)+\cos(X)\sin(Y).$

The last one being valid in the ring $\mathbb {Q} [[X,Y]].$

For *K* a field, the ring $K[[X_{1},\ldots ,X_{r}]]$ is often used as the "standard, most general" complete local ring over *K* in algebra.

## Interpreting formal power series as functions

In mathematical analysis, every convergent power series defines a function with values in the real or complex numbers. Formal power series over certain special rings can also be interpreted as functions, but one has to be careful with the domain and codomain. Let

$f=\sum a_{n}X^{n}\in R[[X]],$

and suppose S is a commutative associative algebra over R , I is an ideal in S such that the I-adic topology on S is complete, and x is an element of I . Define:

$f(x)=\sum _{n\geq 0}a_{n}x^{n}.$

This series is guaranteed to converge in S given the above assumptions on x . Furthermore, we have

$(f+g)(x)=f(x)+g(x)$

and

$(fg)(x)=f(x)g(x).$

Unlike in the case of bona fide functions, these formulas are not definitions but have to be proved.

Since the topology on $R[[X]]$ is the $(X)$ -adic topology and $R[[X]]$ is complete, we can in particular apply power series to other power series, provided that the arguments don't have constant coefficients (so that they belong to the ideal $(X)$ ): $f(0)$ , $f(X^{2}-X)$ and $f((1-X)^{-1}-1)$ are all well defined for any formal power series $f\in R[[X]].$

With this formalism, we can give an explicit formula for the multiplicative inverse of a power series f whose constant coefficient $a=f(0)$ is invertible in R :

$f^{-1}=\sum _{n\geq 0}a^{-n-1}(a-f)^{n}.$

If the formal power series g with $g(0)=0$ is given implicitly by the equation

$f(g)=X$

where f is a known power series with $f(0)=0$ , then the coefficients of g can be explicitly computed using the Lagrange inversion formula.

## Generalizations

### Formal Laurent series

The **formal Laurent series** over a ring R are defined in a similar way to a formal power series, except that we also allow finitely many terms of negative degree. That is, they are the series that can be written as

$f=\sum _{n=N}^{\infty }a_{n}X^{n}$

for some integer N , so that there are only finitely many negative n with $a_{n}\neq 0$ . (This is different from the classical Laurent series of complex analysis.) For a non-zero formal Laurent series, the minimal integer n such that $a_{n}\neq 0$ is called the *order* of f and is denoted $\operatorname {ord} (f).$ (The order ord(0) of the zero series is $+\infty$ .)

For instance, $X^{-3}+{\frac {1}{2}}X^{-2}+{\frac {1}{3}}X^{-1}+{\frac {1}{4}}+{\frac {1}{5}}X+{\frac {1}{6}}X^{2}+{\frac {1}{7}}X^{3}+{\frac {1}{8}}X^{4}+\dots$ is a formal Laurent series of order –3.

Multiplication of such series can be defined. Indeed, similarly to the definition for formal power series, the coefficient of $X^{k}$ of two series with respective sequences of coefficients $\{a_{n}\}$ and $\{b_{n}\}$ is $\sum _{i\in \mathbb {Z} }a_{i}b_{k-i}.$ This sum has only finitely many nonzero terms because of the assumed vanishing of coefficients at sufficiently negative indices.

The formal Laurent series form the **ring of formal Laurent series** over R , denoted by $R((X))$ . It is equal to the localization of the ring $R[[X]]$ of formal power series with respect to the set of positive powers of X . If $R=K$ is a field, then $K((X))$ is in fact a field, which may alternatively be obtained as the field of fractions of the integral domain $K[[X]]$ .

As with $R[[X]]$ , the ring $R((X))$ of formal Laurent series may be endowed with the structure of a topological ring by introducing the metric $d(f,g)=2^{-\operatorname {ord} (f-g)}.$ (In particular, $\operatorname {ord} (0)=+\infty$ implies that $d(f,f)=2^{-\operatorname {ord} (0)}=0$ .)

One may define formal differentiation for formal Laurent series in the natural (term-by-term) way. Precisely, the formal derivative of the formal Laurent series f above is $f'=Df=\sum _{n\in \mathbb {Z} }na_{n}X^{n-1},$ which is again a formal Laurent series. If f is a non-constant formal Laurent series and with coefficients in a field of characteristic 0, then one has $\operatorname {ord} (f')=\operatorname {ord} (f)-1.$ However, in general this is not the case since the factor n for the lowest order term could be equal to 0 in R .

#### Formal residue

Assume that K is a field of characteristic 0. Then the map

$D\colon K((X))\to K((X))$

defined above is a K -derivation that satisfies

$\ker D=K$

$\operatorname {im} D=\left\{f\in K((X)):[X^{-1}]f=0\right\}.$

The latter shows that the coefficient of $X^{-1}$ in f is of particular interest; it is called *formal residue of f* and denoted $\operatorname {Res} (f)$ . The map

$\operatorname {Res} :K((X))\to K$

is K -linear, and by the above observation one has an exact sequence

$0\to K\to K((X)){\overset {D}{\longrightarrow }}K((X))\;{\overset {\operatorname {Res} }{\longrightarrow }}\;K\to 0.$

**Some rules of calculus**. As a quite direct consequence of the above definition, and of the rules of formal derivation, one has, for any $f,g\in K((X))$

1. $\operatorname {Res} (f')=0;$
2. $\operatorname {Res} (fg')=-\operatorname {Res} (f'g);$
3. $\operatorname {Res} (f'/f)=\operatorname {ord} (f),\qquad \forall f\neq 0;$
4. $\operatorname {Res} \left((g\circ f)f'\right)=\operatorname {ord} (f)\operatorname {Res} (g),$ if $\operatorname {ord} (f)>0;$
5. $[X^{n}]f(X)=\operatorname {Res} \left(X^{-n-1}f(X)\right).$

Property (i) is part of the exact sequence above. Property (ii) follows from (i) as applied to $(fg)'=f'g+fg'$ . Property (iii): any f can be written in the form $f=X^{m}g$ , with $m=\operatorname {ord} (f)$ and $\operatorname {ord} (g)=0$ : then $f'/f=mX^{-1}+g'/g.$ $\operatorname {ord} (g)=0$ implies g is invertible in $K[[X]]\subset \operatorname {im} (D)=\ker(\operatorname {Res} ),$ whence $\operatorname {Res} (f'/f)=m.$ Property (iv): Since $\operatorname {im} (D)=\ker(\operatorname {Res} ),$ we can write $g=g_{-1}X^{-1}+G',$ with $G\in K((X))$ . Consequently, $(g\circ f)f'=g_{-1}f^{-1}f'+(G'\circ f)f'=g_{-1}f'/f+(G\circ f)'$ and (iv) follows from (i) and (iii). Property (v) is clear from the definition.

### The Lagrange inversion formula

As mentioned above, any formal series $f\in K[[X]]$ with *f*0 = 0 and *f*1 ≠ 0 has a composition inverse $g\in K[[X]].$ The following relation between the coefficients of *gn* and *f*−*k* holds ("Lagrange inversion formula"):

$k[X^{k}]g^{n}=n[X^{-n}]f^{-k}.$

In particular, for *n* = 1 and all *k* ≥ 1,

$[X^{k}]g={\frac {1}{k}}\operatorname {Res} \left(f^{-k}\right).$

Since the proof of the Lagrange inversion formula is a very short computation, it is worth reporting one proof here. Noting $\operatorname {ord} (f)=1$ , we can apply the rules of calculus above, crucially Rule (iv) substituting $X\rightsquigarrow f(X)$ , to get:

${\begin{aligned}k[X^{k}]g^{n}&\ {\stackrel {\mathrm {(v)} }{=}}\ k\operatorname {Res} \left(g^{n}X^{-k-1}\right)\ {\stackrel {\mathrm {(iv)} }{=}}\ k\operatorname {Res} \left(X^{n}f^{-k-1}f'\right)\ {\stackrel {\mathrm {chain} }{=}}\ -\operatorname {Res} \left(X^{n}(f^{-k})'\right)\\&\ {\stackrel {\mathrm {(ii)} }{=}}\ \operatorname {Res} \left(\left(X^{n}\right)'f^{-k}\right)\ {\stackrel {\mathrm {chain} }{=}}\ n\operatorname {Res} \left(X^{n-1}f^{-k}\right)\ {\stackrel {\mathrm {(v)} }{=}}\ n[X^{-n}]f^{-k}.\end{aligned}}$

**Generalizations.** One may observe that the above computation can be repeated plainly in more general settings than *K*((*X*)): a generalization of the Lagrange inversion formula is already available working in the $\mathbb {C} ((X))$ -modules $X^{\alpha }\mathbb {C} ((X)),$ where α is a complex exponent. As a consequence, if *f* and *g* are as above, with $f_{1}=g_{1}=1$ , we can relate the complex powers of *f* / *X* and *g* / *X*: precisely, if α and β are non-zero complex numbers with negative integer sum, $m=-\alpha -\beta \in \mathbb {N} ,$ then

${\frac {1}{\alpha }}[X^{m}]\left({\frac {f}{X}}\right)^{\alpha }=-{\frac {1}{\beta }}[X^{m}]\left({\frac {g}{X}}\right)^{\beta }.$

For instance, this way one finds the power series for complex powers of the Lambert function.

### Power series in several variables

Formal power series in any number of indeterminates (even infinitely many) can be defined. If *I* is an index set and *XI* is the set of indeterminates *Xi* for *i*∈*I*, then a monomial *X**α* is any finite product of elements of *XI* (repetitions allowed); a formal power series in *XI* with coefficients in a ring *R* is determined by any mapping from the set of monomials *X**α* to a corresponding coefficient *c**α*, and is denoted ${\textstyle \sum _{\alpha }c_{\alpha }X^{\alpha }}$ . The set of all such formal power series is denoted $R[[X_{I}]],$ and it is given a ring structure by defining

$\left(\sum _{\alpha }c_{\alpha }X^{\alpha }\right)+\left(\sum _{\alpha }d_{\alpha }X^{\alpha }\right)=\sum _{\alpha }(c_{\alpha }+d_{\alpha })X^{\alpha }$

and

$\left(\sum _{\alpha }c_{\alpha }X^{\alpha }\right)\times \left(\sum _{\beta }d_{\beta }X^{\beta }\right)=\sum _{\alpha ,\beta }c_{\alpha }d_{\beta }X^{\alpha +\beta }$

#### Topology

The topology on $R[[X_{I}]]$ is such that a sequence of its elements converges only if for each monomial *X*α the corresponding coefficient stabilizes. If *I* is finite, then this the *J*-adic topology, where *J* is the ideal of $R[[X_{I}]]$ generated by all the indeterminates in *XI*. This does not hold if *I* is infinite. For example, if $I=\mathbb {N} ,$ then the sequence $(f_{n})_{n\in \mathbb {N} }$ with $f_{n}=X_{n}+X_{n+1}+X_{n+2}+\cdots$ does not converge with respect to any *J*-adic topology on *R*, but clearly for each monomial the corresponding coefficient stabilizes.

As remarked above, the topology on a repeated formal power series ring like $R[[X]][[Y]]$ is usually chosen in such a way that it becomes isomorphic as a topological ring to $R[[X,Y]].$

#### Operations

All of the operations defined for series in one variable may be extended to the several variables case.

- A series is invertible if and only if its constant term is invertible in *R*.
- The composition *f*(*g*(*X*)) of two series *f* and *g* is defined if *f* is a series in a single indeterminate, and the constant term of *g* is zero. For a series *f* in several indeterminates a form of "composition" can similarly be defined, with as many separate series in the place of *g* as there are indeterminates.

In the case of the formal derivative, there are now separate partial derivative operators, which differentiate with respect to each of the indeterminates. They all commute with each other.

#### Universal property

In the several variables case, the universal property characterizing $R[[X_{1},\ldots ,X_{r}]]$ becomes the following. If *S* is a commutative associative algebra over *R*, if *I* is an ideal of *S* such that the *I*-adic topology on *S* is complete, and if *x*1, ..., *xr* are elements of *I*, then there is a *unique* map $\Phi :R[[X_{1},\ldots ,X_{r}]]\to S$ with the following properties:

- Φ is an *R*-algebra homomorphism
- Φ is continuous
- Φ(*X**i*) = *x**i* for *i* = 1, ..., *r*.

### Non-commuting variables

The several variable case can be further generalised by taking *non-commuting variables* *Xi* for *i* ∈ *I*, where *I* is an index set and then a monomial *X*α is any word in the *XI*; a formal power series in *XI* with coefficients in a ring *R* is determined by any mapping from the set of monomials *X*α to a corresponding coefficient *c*α, and is denoted $\textstyle \sum _{\alpha }c_{\alpha }X^{\alpha }$ . The set of all such formal power series is denoted $R\langle \!\langle X_{I}\rangle \!\rangle$ , and it is given a ring structure by defining addition pointwise

$\left(\sum _{\alpha }c_{\alpha }X^{\alpha }\right)+\left(\sum _{\alpha }d_{\alpha }X^{\alpha }\right)=\sum _{\alpha }(c_{\alpha }+d_{\alpha })X^{\alpha }$

and multiplication by

$\left(\sum _{\alpha }c_{\alpha }X^{\alpha }\right)\times \left(\sum _{\alpha }d_{\alpha }X^{\alpha }\right)=\sum _{\alpha ,\beta }c_{\alpha }d_{\beta }X^{\alpha }\cdot X^{\beta }$

where · denotes concatenation of words. These formal power series over *R* form the **Magnus ring** over *R*.

### On a semiring

Given an alphabet $\Sigma$ and a semiring S . The formal power series over S supported on the language $\Sigma ^{*}$ is denoted by $S\langle \langle \Sigma ^{*}\rangle \rangle$ . It consists of all mappings $r:\Sigma ^{*}\to S$ , where $\Sigma ^{*}$ is the free monoid generated by the non-empty set $\Sigma$ .

The elements of $S\langle \langle \Sigma ^{*}\rangle \rangle$ can be written as formal sums

$r=\sum _{w\in \Sigma ^{*}}(r,w)w.$

where $(r,w)$ denotes the value of r at the word $w\in \Sigma ^{*}$ . The elements $(r,w)\in S$ are called the coefficients of r .

For $r\in S\langle \langle \Sigma ^{*}\rangle \rangle$ the support of r is the set

$\operatorname {supp} (r)=\{w\in \Sigma ^{*}|\ (r,w)\neq 0\}$

A series where every coefficient is either 0 or 1 is called the characteristic series of its support.

The subset of $S\langle \langle \Sigma ^{*}\rangle \rangle$ consisting of all series with a finite support is denoted by $S\langle \Sigma ^{*}\rangle$ and called polynomials.

For $r_{1},r_{2}\in S\langle \langle \Sigma ^{*}\rangle \rangle$ and $s\in S$ , the sum $r_{1}+r_{2}$ is defined by

$(r_{1}+r_{2},w)=(r_{1},w)+(r_{2},w)$

The (Cauchy) product $r_{1}\cdot r_{2}$ is defined by

$(r_{1}\cdot r_{2},w)=\sum _{w_{1}w_{2}=w}(r_{1},w_{1})(r_{2},w_{2})$

The Hadamard product $r_{1}\odot r_{2}$ is defined by

$(r_{1}\odot r_{2},w)=(r_{1},w)(r_{2},w)$

And the products by a scalar $sr_{1}$ and $r_{1}s$ by

$(sr_{1},w)=s(r_{1},w)$

and

$(r_{1}s,w)=(r_{1},w)s$

, respectively.

With these operations $(S\langle \langle \Sigma ^{*}\rangle \rangle ,+,\cdot ,0,\varepsilon )$ and $(S\langle \Sigma ^{*}\rangle ,+,\cdot ,0,\varepsilon )$ are semirings, where $\varepsilon$ is the empty word in $\Sigma ^{*}$ .

These formal power series are used to model the behavior of weighted automata, in theoretical computer science, when the coefficients $(r,w)$ of the series are taken to be the weight of a path with label w in the automata.

### Replacing the index set by an ordered abelian group

Suppose G is an ordered abelian group, meaning an abelian group with a total ordering < respecting the group's addition, so that $a<b$ if and only if $a+c<b+c$ for all c . Let **I** be a well-ordered subset of G , meaning **I** contains no infinite descending chain. Consider the set consisting of

$\sum _{i\in I}a_{i}X^{i}$

for all such **I**, with $a_{i}$ in a commutative ring R , where we assume that for any index set, if all of the $a_{i}$ are zero then the sum is zero. Then $R((G))$ is the ring of formal power series on G ; because of the condition that the indexing set be well-ordered the product is well-defined, and we of course assume that two elements which differ by zero are the same. Sometimes the notation $[[R^{G}]]$ is used to denote $R((G))$ .

Various properties of R transfer to $R((G))$ . If R is a field, then so is $R((G))$ . If R is an ordered field, we can order $R((G))$ by setting any element to have the same sign as its leading coefficient, defined as the least element of the index set **I** associated to a non-zero coefficient. Finally if G is a divisible group and R is a real closed field, then $R((G))$ is a real closed field, and if R is algebraically closed, then so is $R((G))$ .

This theory is due to Hans Hahn, who also showed that one obtains subfields when the number of (non-zero) terms is bounded by some fixed infinite cardinality.

- Bell series are used to study the properties of multiplicative arithmetic functions
- Formal groups are used to define an abstract group law using formal power series
- Puiseux series are an extension of formal Laurent series, allowing fractional exponents
- Rational series
