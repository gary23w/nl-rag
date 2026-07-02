---
title: "Kleene's recursion theorem"
source: https://en.wikipedia.org/wiki/Kleene's_recursion_theorem
domain: recursion-theory
license: CC-BY-SA-4.0
tags: computability theory, turing degree, halting problem, arithmetical hierarchy
fetched: 2026-07-02
---

# Kleene's recursion theorem

In computability theory, **Kleene's recursion theorems** are a pair of fundamental results about the application of computable functions to their own descriptions. The theorems were first proved by Stephen Kleene in 1938 and appear in his 1952 book *Introduction to Metamathematics*. A related theorem, which constructs fixed points of a computable function, is known as **Rogers's theorem** and is due to Hartley Rogers, Jr.

The recursion theorems can be applied to construct fixed points of certain operations on computable functions, to generate quines, and to construct functions defined via recursive definitions.

## Notation

The statement of the theorems refers to an admissible numbering $\varphi$ of the partial recursive functions, such that the function corresponding to index e is $\varphi _{e}$ .

If F and G are partial functions on the natural numbers, the notation $F\simeq G$ indicates that, for each *n*, either $F(n)$ and $G(n)$ are both defined and are equal, or else $F(n)$ and $G(n)$ are both undefined.

## Rogers's fixed-point theorem

Given a function F on the natural numbers, a **fixed point** of F is an index e in the domain of F such that $\varphi _{e}\simeq \varphi _{F(e)}$ . Note that the comparison of in- and outputs here is not in terms of numerical values, but in terms of their associated partial recursive functions.

Rogers describes the following result as "a simpler version" of Kleene's (second) recursion theorem.

**Rogers's fixed-point theorem**—If F is a total computable function, it has a fixed point in the above sense.

This essentially means that if we apply an effective transformation to programs (say, replace instructions such as successor, jump, remove lines), there will always be a program whose behaviour is not altered by the transformation. This theorem can therefore be interpreted in the following manner: “given any effective procedure to transform programs, there is always a program that, when modified by the procedure, does exactly what it did before”, or: “it’s impossible to write a program that changes the extensional behaviour of all programs”.

### Proof of the fixed-point theorem

The proof uses a particular total computable function h , defined as follows. Given a natural number x , the function h outputs the index of the partial computable function that performs the following computation:

Given an input

y

, first attempt to compute

$\varphi _{x}(x)$

. If that computation returns an output

e

, then compute

$\varphi _{e}(y)$

and return its value, if any. Thus, for all indices

x

of partial computable functions, if

$\varphi _{x}(x)$

is defined, then

$\varphi _{h(x)}\simeq \varphi _{\varphi _{x}(x)}$

. If

$\varphi _{x}(x)$

is not defined, then

$\varphi _{h(x)}$

is a function that is nowhere defined. The function

h

can be constructed from the partial computable function

$g(x,y)$

described above and the

S

m

n

theorem

: for each

x

, the number

$h(x)$

is the index of a program that computes the function

$y\mapsto g(x,y)$

.

To complete the proof, let F be any total computable function, and construct h as above. Let e be an index of the composition $F\circ h$ , which is a total computable function, so $\varphi _{e}(e)$ is defined. Then $\varphi _{h(e)}\simeq \varphi _{\varphi _{e}(e)}$ by the definition of h . But, because e is an index of $F\circ h$ , $\varphi _{e}(e)=(F\circ h)(e)=F(h(e))$ , and thus $\varphi _{h(e)}\simeq \varphi _{F(h(e))}$ . Hence $\varphi _{n}\simeq \varphi _{F(n)}$ for $n=h(e)$ .

This proof is a construction of a partial recursive function that implements the Y combinator.

### Fixed-point-free functions

A function F such that $\varphi _{e}\not \simeq \varphi _{F(e)}$ for all e is called **fixed-point free**. The fixed-point theorem shows that no total computable function is fixed-point free, but there are many non-computable fixed-point-free functions. **Arslanov's completeness criterion** states that the only recursively enumerable Turing degree that computes a fixed-point-free function is **0′**, the degree of the halting problem.

## Kleene's second recursion theorem

The second recursion theorem is a generalization of Rogers's theorem with a second input in the function. One informal interpretation of the second recursion theorem is that it is possible to construct self-referential programs; see "Application to quines" below.

The second recursion theorem

. For any partial recursive function

$Q(x,y)$

there is an index

p

such that

$\varphi _{p}\simeq \lambda y.Q(p,y)$

.

The theorem can be proved from Rogers's theorem by letting F be a function such that $\varphi _{F(p)}(y)=Q(p,y)$ (a construction described by the S m n  theorem). One can then verify that a fixed-point of this F is an index p as required. The theorem is constructive in the sense that a fixed computable function maps an index for Q into the index p .

### Comparison to Rogers's theorem

Kleene's second recursion theorem and Rogers's theorem can both be proved, rather simply, from each other. However, a direct proof of Kleene's theorem does not make use of a universal program, which means that the theorem holds for certain subrecursive programming systems that do not have a universal program.

### Application to quines

A classic example using the second recursion theorem is the function $Q(x,y)=x$ . The corresponding index p in this case yields a computable function that outputs its own index when applied to any value. When expressed as computer programs, such indices are known as **quines**.

The following example in Lisp illustrates how the p in the corollary can be effectively produced from the function Q . The function `s11` in the code is the function of that name produced by the S m n  theorem.

`Q` can be changed to any two-argument function.

```mw
(setq Q '(lambda (x y) x))
(setq s11 '(lambda (f x) (list 'lambda '(y) (list f x 'y))))
(setq n (list 'lambda '(x y) (list Q (list s11 'x 'x) 'y)))
(setq p (eval (list s11 n n)))
```

The results of the following expressions should be the same. $\varphi$ `p(nil)`

```mw
(eval (list p nil))
```

`Q(p, nil)`

```mw
(eval (list Q p nil))
```

### Application to elimination of recursion

Suppose that g and h are total computable functions that are used in a recursive definition for a function f :

$f(0,y)\simeq g(y),$

$f(x+1,y)\simeq h(f(x,y),x,y),$

The second recursion theorem can be used to show that such equations define a computable function, where the notion of computability does not have to allow, prima facie, for recursive definitions (for example, it may be defined by μ-recursion, or by Turing machines). This recursive definition can be converted into a computable function $\varphi _{F}(e,x,y)$ that assumes e is an index to itself, to simulate recursion:

$\varphi _{F}(e,0,y)\simeq g(y),$

$\varphi _{F}(e,x+1,y)\simeq h(\varphi _{e}(x,y),x,y).$

The recursion theorem establishes the existence of a computable function $\varphi _{f}$ such that $\varphi _{f}(x,y)\simeq \varphi _{F}(f,x,y)$ . Thus f satisfies the given recursive definition.

### Reflexive programming

Reflexive, or reflective, programming refers to the usage of self-reference in programs. Jones presents a view of the second recursion theorem based on a reflexive language. It is shown that the reflexive language defined is not stronger than a language without reflection (because an interpreter for the reflexive language can be implemented without using reflection); then, it is shown that the recursion theorem is almost trivial in the reflexive language.

## The first recursion theorem

While the second recursion theorem is about fixed points of computable functions, the first recursion theorem is related to fixed points determined by enumeration operators, which are a computable analogue of inductive definitions. An **enumeration operator** is a set of pairs (*A*,*n*) where *A* is a (code for a) finite set of numbers and *n* is a single natural number. Often, *n* will be viewed as a code for an ordered pair of natural numbers, particularly when functions are defined via enumeration operators. Enumeration operators are of central importance in the study of enumeration reducibility.

Each enumeration operator Φ determines a function from sets of naturals to sets of naturals given by

$\Phi (X)=\{n\mid \exists A\subseteq X[(A,n)\in \Phi ]\}.$

A **recursive operator** is an enumeration operator that, when given the graph of a partial recursive function, always returns the graph of a partial recursive function.

A fixed point of an enumeration operator Φ is a set *F* such that Φ(*F*) = *F*. The first enumeration theorem shows that fixed points can be effectively obtained if the enumeration operator itself is computable.

First recursion theorem

. The following statements hold.

1. For any computable enumeration operator Φ there is a recursively enumerable set *F* such that Φ(*F*) = *F* and *F* is the smallest set with this property.
2. For any recursive operator Ψ there is a partial computable function φ such that Ψ(φ) = φ and φ is the smallest partial computable function with this property.

The first recursion theorem is also called Fixed point theorem (of recursion theory). There is also a definition that can be applied to recursive functionals as follows:

Let $\Phi :\mathbb {F} (\mathbb {N} ^{k})\rightarrow (\mathbb {N} ^{k})$ be a recursive functional. Then $\Phi$ has a least fixed point $f_{\Phi }:\mathbb {N} ^{k}\rightarrow \mathbb {N}$ which is computable i.e.

1) $\Phi (f_{\phi })=f_{\Phi }$

2) $\forall g\in \mathbb {F} (\mathbb {N} ^{k})$ such that $\Phi (g)=g$ it holds that $f_{\Phi }\subseteq g$

3) $f_{\Phi }$ is computable

### Example

Like the second recursion theorem, the first recursion theorem can be used to obtain functions satisfying systems of recursion equations. To apply the first recursion theorem, the recursion equations must first be recast as a recursive operator.

Consider the recursion equations for the factorial function *f*: ${\begin{aligned}&f(0)=1\\&f(n+1)=(n+1)\cdot f(n)\end{aligned}}$ The corresponding recursive operator Φ will have information that tells how to get to the next value of *f* from the previous value. However, the recursive operator will actually define the graph of *f*. First, Φ will contain the pair $(\varnothing ,(0,1))$ . This indicates that *f*(0) is unequivocally 1, and thus the pair (0,1) is in the graph of *f*.

Next, for each *n* and *m*, Φ will contain the pair $(\{(n,m)\},(n+1,(n+1)\cdot m))$ . This indicates that, if *f*(*n*) is *m*, then *f*(*n* + 1) is (*n* + 1)*m*, so that the pair (*n* + 1, (*n* + 1)*m*) is in the graph of *f*. Unlike the base case *f*(0) = 1, the recursive operator requires some information about *f*(*n*) before it defines a value of *f*(*n* + 1).

The first recursion theorem (in particular, part 1) states that there is a set *F* such that Φ(*F*) = F. The set *F* will consist entirely of ordered pairs of natural numbers, and will be the graph of the factorial function *f*, as desired.

The restriction to recursion equations that can be recast as recursive operators ensures that the recursion equations actually define a least fixed point. For example, consider the set of recursion equations: ${\begin{aligned}&g(0)=1\\&g(n+1)=1\\&g(2n)=0\end{aligned}}$ There is no function *g* satisfying these equations, because they imply *g*(2) = 1 and also imply *g*(2) = 0. Thus there is no fixed point *g* satisfying these recursion equations. It is possible to make an enumeration operator corresponding to these equations, but it will not be a recursive operator.

### Proof sketch for the first recursion theorem

The proof of part 1 of the first recursion theorem is obtained by iterating the enumeration operator Φ beginning with the empty set. First, a sequence *F**k* is constructed, for $k=0,1,\ldots$ . Let *F*0 be the empty set. Proceeding inductively, for each *k*, let *F**k* + 1 be $F_{k}\cup \Phi (F_{k})$ . Finally, *F* is taken to be ${\textstyle \bigcup F_{k}}$ . The remainder of the proof consists of a verification that *F* is recursively enumerable and is the least fixed point of Φ. The sequence *F**k* used in this proof corresponds to the Kleene chain in the proof of the Kleene fixed-point theorem.

The second part of the first recursion theorem follows from the first part. The assumption that Φ is a recursive operator is used to show that the fixed point of Φ is the graph of a partial function. The key point is that if the fixed point *F* is not the graph of a function, then there is some *k* such that *F**k* is not the graph of a function.

### Comparison to the second recursion theorem

Compared to the second recursion theorem, the first recursion theorem produces a stronger conclusion but only when narrower hypotheses are satisfied. Rogers uses the term **weak recursion theorem** for the first recursion theorem and **strong recursion theorem** for the second recursion theorem.

One difference between the first and second recursion theorems is that the fixed points obtained by the first recursion theorem are guaranteed to be least fixed points, while those obtained from the second recursion theorem may not be least fixed points.

A second difference is that the first recursion theorem only applies to systems of equations that can be recast as recursive operators. This restriction is similar to the restriction to continuous operators in the Kleene fixed-point theorem of order theory. The second recursion theorem can be applied to any total recursive function.

## Generalized theorem

In the context of his theory of numberings, Ershov showed that Kleene's recursion theorem holds for any precomplete numbering. A Gödel numbering is a precomplete numbering on the set of computable functions so the generalized theorem yields the Kleene recursion theorem as a special case.

Given a precomplete numbering $\nu$ , then for any partial computable function f with two parameters there exists a total computable function t with one parameter such that

$\forall n\in \mathbb {N} :\nu \circ f(n,t(n))=\nu \circ t(n).$
