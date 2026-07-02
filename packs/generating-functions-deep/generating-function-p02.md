---
title: "Generating function (part 2/2)"
source: https://en.wikipedia.org/wiki/Generating_function
domain: generating-functions-deep
license: CC-BY-SA-4.0
tags: generating function, formal power series, umbral calculus, lagrange inversion theorem
fetched: 2026-07-02
part: 2/2
---

## Applications

Generating functions are used to:

- Find a closed formula for a sequence given in a recurrence relation, for example, Fibonacci numbers.
- Find recurrence relations for sequences—the form of a generating function may suggest a recurrence formula.
- Find relationships between sequences—if the generating functions of two sequences have a similar form, then the sequences themselves may be related.
- Explore the asymptotic behaviour of sequences.
- Prove identities involving sequences.
- Solve enumeration problems in combinatorics and encoding their solutions. Rook polynomials are an example of an application in combinatorics.
- Evaluate infinite sums.

### Various techniques: Evaluating sums and tackling other problems with generating functions

#### Example 1: Formula for sums of harmonic numbers

Generating functions give us several methods to manipulate sums and to establish identities between sums.

The simplest case occurs when *sn* = Σ*n* *k* = 0 *ak*. We then know that *S*(*z*) = ⁠*A*(*z*)/1 − *z*⁠ for the corresponding ordinary generating functions.

For example, we can manipulate $s_{n}=\sum _{k=1}^{n}H_{k}\,,$ where *Hk* = 1 + ⁠1/2⁠ + ⋯ + ⁠1/*k*⁠ are the harmonic numbers. Let $H(z)=\sum _{n=1}^{\infty }{H_{n}z^{n}}$ be the ordinary generating function of the harmonic numbers. Then $H(z)={\frac {1}{1-z}}\sum _{n=1}^{\infty }{\frac {z^{n}}{n}}\,,$ and thus $S(z)=\sum _{n=1}^{\infty }{s_{n}z^{n}}={\frac {1}{(1-z)^{2}}}\sum _{n=1}^{\infty }{\frac {z^{n}}{n}}\,.$

Using ${\frac {1}{(1-z)^{2}}}=\sum _{n=0}^{\infty }(n+1)z^{n}\,,$ convolution with the numerator yields $s_{n}=\sum _{k=1}^{n}{\frac {n+1-k}{k}}=(n+1)H_{n}-n\,,$ which can also be written as $\sum _{k=1}^{n}{H_{k}}=(n+1)(H_{n+1}-1)\,.$

#### Example 2: Modified binomial coefficient sums and the binomial transform

As another example of using generating functions to relate sequences and manipulate sums, for an arbitrary sequence ⟨ *fn* ⟩ we define the two sequences of sums ${\begin{aligned}s_{n}&:=\sum _{m=0}^{n}{\binom {n}{m}}f_{m}3^{n-m}\\[4px]{\tilde {s}}_{n}&:=\sum _{m=0}^{n}{\binom {n}{m}}(m+1)(m+2)(m+3)f_{m}3^{n-m}\,,\end{aligned}}$ for all *n* ≥ 0, and seek to express the second sums in terms of the first. We suggest an approach by generating functions.

First, we use the binomial transform to write the generating function for the first sum as $S(z)={\frac {1}{1-3z}}F\left({\frac {z}{1-3z}}\right).$

Since the generating function for the sequence ⟨ (*n* + 1)(*n* + 2)(*n* + 3) *fn* ⟩ is given by $6F(z)+18zF'(z)+9z^{2}F''(z)+z^{3}F'''(z)$ we may write the generating function for the second sum defined above in the form ${\tilde {S}}(z)={\frac {6}{(1-3z)}}F\left({\frac {z}{1-3z}}\right)+{\frac {18z}{(1-3z)^{2}}}F'\left({\frac {z}{1-3z}}\right)+{\frac {9z^{2}}{(1-3z)^{3}}}F''\left({\frac {z}{1-3z}}\right)+{\frac {z^{3}}{(1-3z)^{4}}}F'''\left({\frac {z}{1-3z}}\right).$

In particular, we may write this modified sum generating function in the form of $a(z)\cdot S(z)+b(z)\cdot zS'(z)+c(z)\cdot z^{2}S''(z)+d(z)\cdot z^{3}S'''(z),$ for *a*(*z*) = 6(1 − 3*z*)3, *b*(*z*) = 18(1 − 3*z*)3, *c*(*z*) = 9(1 − 3*z*)3, and *d*(*z*) = (1 − 3*z*)3, where (1 − 3*z*)3 = 1 − 9*z* + 27*z*2 − 27*z*3.

Finally, it follows that we may express the second sums through the first sums in the following form: ${\begin{aligned}{\tilde {s}}_{n}&=[z^{n}]\left(6(1-3z)^{3}\sum _{n=0}^{\infty }s_{n}z^{n}+18(1-3z)^{3}\sum _{n=0}^{\infty }ns_{n}z^{n}+9(1-3z)^{3}\sum _{n=0}^{\infty }n(n-1)s_{n}z^{n}+(1-3z)^{3}\sum _{n=0}^{\infty }n(n-1)(n-2)s_{n}z^{n}\right)\\[4px]&=(n+1)(n+2)(n+3)s_{n}-9n(n+1)(n+2)s_{n-1}+27(n-1)n(n+1)s_{n-2}-(n-2)(n-1)ns_{n-3}.\end{aligned}}$

#### Example 3: Generating functions for mutually recursive sequences

In this example, we reformulate a generating function example given in Section 7.3 of *Concrete Mathematics* (see also Section 7.1 of the same reference for pretty pictures of generating function series). In particular, suppose that we seek the total number of ways (denoted *Un*) to tile a 3-by-n rectangle with unmarked 2-by-1 domino pieces. Let the auxiliary sequence, *Vn*, be defined as the number of ways to cover a 3-by-n rectangle-minus-corner section of the full rectangle. We seek to use these definitions to give a closed form formula for *Un* without breaking down this definition further to handle the cases of vertical versus horizontal dominoes. Notice that the ordinary generating functions for our two sequences correspond to the series: ${\begin{aligned}U(z)=1+3z^{2}+11z^{4}+41z^{6}+\cdots ,\\V(z)=z+4z^{3}+15z^{5}+56z^{7}+\cdots .\end{aligned}}$

If we consider the possible configurations that can be given starting from the left edge of the 3-by-n rectangle, we are able to express the following mutually dependent, or *mutually recursive*, recurrence relations for our two sequences when *n* ≥ 2 defined as above where *U*0 = 1, *U*1 = 0, *V*0 = 0, and *V*1 = 1: ${\begin{aligned}U_{n}&=2V_{n-1}+U_{n-2}\\V_{n}&=U_{n-1}+V_{n-2}.\end{aligned}}$

Since we have that for all integers *m* ≥ 0, the index-shifted generating functions satisfy $z^{m}G(z)=\sum _{n=m}^{\infty }g_{n-m}z^{n}\,,$ we can use the initial conditions specified above and the previous two recurrence relations to see that we have the next two equations relating the generating functions for these sequences given by ${\begin{aligned}U(z)&=2zV(z)+z^{2}U(z)+1\\V(z)&=zU(z)+z^{2}V(z)={\frac {z}{1-z^{2}}}U(z),\end{aligned}}$ which then implies by solving the system of equations (and this is the particular trick to our method here) that $U(z)={\frac {1-z^{2}}{1-4z^{2}+z^{4}}}={\frac {1}{3-{\sqrt {3}}}}\cdot {\frac {1}{1-\left(2+{\sqrt {3}}\right)z^{2}}}+{\frac {1}{3+{\sqrt {3}}}}\cdot {\frac {1}{1-\left(2-{\sqrt {3}}\right)z^{2}}}.$

Thus by performing algebraic simplifications to the sequence resulting from the second partial fractions expansions of the generating function in the previous equation, we find that *U*2*n* + 1 ≡ 0 and that $U_{2n}=\left\lceil {\frac {\left(2+{\sqrt {3}}\right)^{n}}{3-{\sqrt {3}}}}\right\rceil \,,$ for all integers *n* ≥ 0. We also note that the same shifted generating function technique applied to the second-order recurrence for the Fibonacci numbers is the prototypical example of using generating functions to solve recurrence relations in one variable already covered, or at least hinted at, in the subsection on rational functions given above.

### Convolution (Cauchy products)

A discrete *convolution* of the terms in two formal power series turns a product of generating functions into a generating function enumerating a convolved sum of the original sequence terms (see Cauchy product).

1. Consider *A*(*z*) and *B*(*z*) are ordinary generating functions. $C(z)=A(z)B(z)\Leftrightarrow [z^{n}]C(z)=\sum _{k=0}^{n}{a_{k}b_{n-k}}$
2. Consider *A*(*z*) and *B*(*z*) are exponential generating functions. $C(z)=A(z)B(z)\Leftrightarrow \left[{\frac {z^{n}}{n!}}\right]C(z)=\sum _{k=0}^{n}{\binom {n}{k}}a_{k}b_{n-k}$
3. Consider the triply convolved sequence resulting from the product of three ordinary generating functions $C(z)=F(z)G(z)H(z)\Leftrightarrow [z^{n}]C(z)=\sum _{j+k+l=n}f_{j}g_{k}h_{l}$
4. Consider the triply convolved sequence resulting from the product of three exponential generating functions $C(z)=F(z)G(z)H(z)\Leftrightarrow \left[{\frac {z^{n}}{n!}}\right]C(z)=\sum _{j+k+l=n}{\frac {n!}{j!k!l!}}f_{j}g_{k}h_{l}$
5. Consider the m-fold convolution of a sequence with itself for some positive integer *m* ≥ 1 (see the example below for an application) $C(z)=G(z)^{m}\Leftrightarrow [z^{n}]C(z)=\sum _{k_{1}+k_{2}+\cdots +k_{m}=n}g_{k_{1}}g_{k_{2}}\cdots g_{k_{m}}$

Multiplication of generating functions, or convolution of their underlying sequences, can correspond to a notion of independent events in certain counting and probability scenarios. For example, if we adopt the notational convention that the probability generating function, or *pgf*, of a random variable Z is denoted by *GZ*(*z*), then we can show that for any two random variables $G_{X+Y}(z)=G_{X}(z)G_{Y}(z)\,,$ if X and Y are independent.

#### Example: The money-changing problem

The number of ways to pay *n* ≥ 0 cents in coin denominations of values in the set {1, 5, 10, 25, 50} (i.e., in pennies, nickels, dimes, quarters, and half dollars), where we distinguish instances based upon the total number of each coin but not upon the order in which the coins are presented, is given by the ordinary generating function ${\frac {1}{1-z}}{\frac {1}{1-z^{5}}}{\frac {1}{1-z^{10}}}{\frac {1}{1-z^{25}}}{\frac {1}{1-z^{50}}}\,.$ When we also distinguish based upon the order in which the coins are presented (e.g., one penny then one nickel is distinct from one nickel then one penny), the ordinary generating function is ${\frac {1}{1-z-z^{5}-z^{10}-z^{25}-z^{50}}}\,.$

If we allow the n cents to be paid in coins of *any* positive integer denomination, we arrive at the partition function ordinary generating function expanded by an infinite q-Pochhammer symbol product, $\prod _{n=1}^{\infty }\left(1-z^{n}\right)^{-1}\,.$ When the order of the coins matters, the ordinary generating function is ${\frac {1}{1-\sum _{n=1}^{\infty }z^{n}}}={\frac {1-z}{1-2z}}\,.$

#### Example: Generating function for the Catalan numbers

An example where convolutions of generating functions are useful allows us to solve for a specific closed-form function representing the ordinary generating function for the Catalan numbers, *Cn*. In particular, this sequence has the combinatorial interpretation as being the number of ways to insert parentheses into the product *x*0 · *x*1 ·⋯· *xn* so that the order of multiplication is completely specified. For example, *C*2 = 2 which corresponds to the two expressions *x*0 · (*x*1 · *x*2) and (*x*0 · *x*1) · *x*2. It follows that the sequence satisfies a recurrence relation given by $C_{n}=\sum _{k=0}^{n-1}C_{k}C_{n-1-k}+\delta _{n,0}=C_{0}C_{n-1}+C_{1}C_{n-2}+\cdots +C_{n-1}C_{0}+\delta _{n,0}\,,\quad n\geq 0\,,$ and so has a corresponding convolved generating function, *C*(*z*), satisfying $C(z)=z\cdot C(z)^{2}+1\,.$

Since *C*(0) = 1 ≠ ∞, we then arrive at a formula for this generating function given by $C(z)={\frac {1-{\sqrt {1-4z}}}{2z}}=\sum _{n=0}^{\infty }{\frac {1}{n+1}}{\binom {2n}{n}}z^{n}\,.$

Note that the first equation implicitly defining *C*(*z*) above implies that $C(z)={\frac {1}{1-z\cdot C(z)}}\,,$ which then leads to another "simple" (of form) continued fraction expansion of this generating function.

#### Example: Spanning trees of fans and convolutions of convolutions

A *fan of order n* is defined to be a graph on the vertices {0, 1, ..., *n*} with 2*n* − 1 edges connected according to the following rules: Vertex 0 is connected by a single edge to each of the other n vertices, and vertex k is connected by a single edge to the next vertex *k* + 1 for all 1 ≤ *k* < *n*. There is one fan of order one, three fans of order two, eight fans of order three, and so on. A spanning tree is a subgraph of a graph which contains all of the original vertices and which contains enough edges to make this subgraph connected, but not so many edges that there is a cycle in the subgraph. We ask how many spanning trees *fn* of a fan of order n are possible for each *n* ≥ 1.

As an observation, we may approach the question by counting the number of ways to join adjacent sets of vertices. For example, when *n* = 4, we have that *f*4 = 4 + 3 · 1 + 2 · 2 + 1 · 3 + 2 · 1 · 1 + 1 · 2 · 1 + 1 · 1 · 2 + 1 · 1 · 1 · 1 = 21, which is a sum over the m-fold convolutions of the sequence *gn* = *n* = [*zn*] ⁠*z*/(1 − *z*)2⁠ for *m* ≔ 1, 2, 3, 4. More generally, we may write a formula for this sequence as $f_{n}=\sum _{m>0}\sum _{\scriptstyle k_{1}+k_{2}+\cdots +k_{m}=n \atop \scriptstyle k_{1},k_{2},\ldots ,k_{m}>0}g_{k_{1}}g_{k_{2}}\cdots g_{k_{m}}\,,$ from which we see that the ordinary generating function for this sequence is given by the next sum of convolutions as $F(z)=G(z)+G(z)^{2}+G(z)^{3}+\cdots ={\frac {G(z)}{1-G(z)}}={\frac {z}{(1-z)^{2}-z}}={\frac {z}{1-3z+z^{2}}}\,,$ from which we are able to extract an exact formula for the sequence by taking the partial fraction expansion of the last generating function.

### Implicit generating functions and the Lagrange inversion formula

One often encounters generating functions specified by a functional equation, instead of an explicit specification. For example, the generating function *T(z)* for the number of binary trees on *n* nodes (leaves included) satisfies

$T(z)=z\left(1+T(z)^{2}\right)$

The Lagrange inversion theorem is a tool used to explicitly evaluate solutions to such equations.

**Lagrange inversion formula**—Let ${\textstyle \phi (z)\in C[[z]]}$ be a formal power series with a non-zero constant term. Then the functional equation $T(z)=z\phi (T(z))$ admits a unique solution in ${\textstyle T(z)\in C[[z]]}$ , which satisfies

$[z^{n}]T(z)=[z^{n-1}]{\frac {1}{n}}(\phi (z))^{n}$

where the notation $[z^{n}]F(z)$ returns the coefficient of $z^{n}$ in $F(z)$ .

Applying the above theorem to our functional equation yields (with ${\textstyle \phi (z)=1+z^{2}}$ ):

$[z^{n}]T(z)=[z^{n-1}]{\frac {1}{n}}(1+z^{2})^{n}$

Via the binomial theorem expansion, for even n , the formula returns 0 . This is expected as one can prove that the number of leaves of a binary tree are one more than the number of its internal nodes, so the total sum should always be an odd number. For odd n , however, we get

$[z^{n-1}]{\frac {1}{n}}(1+z^{2})^{n}={\frac {1}{n}}{\dbinom {n}{\frac {n+1}{2}}}$

The expression becomes much neater if we let n be the number of internal nodes: Now the expression just becomes the n th Catalan number.

### Introducing a free parameter (snake oil method)

Sometimes the sum *sn* is complicated, and it is not always easy to evaluate. The "Free Parameter" method is another method (called "snake oil" by H. Wilf) to evaluate these sums.

Both methods discussed so far have n as limit in the summation. When n does not appear explicitly in the summation, we may consider n as a "free" parameter and treat *sn* as a coefficient of *F*(*z*) = Σ *sn* *zn*, change the order of the summations on n and k, and try to compute the inner sum.

For example, if we want to compute $s_{n}=\sum _{k=0}^{\infty }{{\binom {n+k}{m+2k}}{\binom {2k}{k}}{\frac {(-1)^{k}}{k+1}}}\,,\quad m,n\in \mathbb {N} _{0}\,,$ we can treat n as a "free" parameter, and set $F(z)=\sum _{n=0}^{\infty }{\left(\sum _{k=0}^{\infty }{{\binom {n+k}{m+2k}}{\binom {2k}{k}}{\frac {(-1)^{k}}{k+1}}}\right)}z^{n}\,.$

Interchanging summation ("snake oil") gives $F(z)=\sum _{k=0}^{\infty }{{\binom {2k}{k}}{\frac {(-1)^{k}}{k+1}}z^{-k}}\sum _{n=0}^{\infty }{{\binom {n+k}{m+2k}}z^{n+k}}\,.$

Now the inner sum is ⁠*z**m* + 2*k*/(1 − *z*)*m* + 2*k* + 1⁠. Thus ${\begin{aligned}F(z)&={\frac {z^{m}}{(1-z)^{m+1}}}\sum _{k=0}^{\infty }{{\frac {1}{k+1}}{\binom {2k}{k}}\left({\frac {-z}{(1-z)^{2}}}\right)^{k}}\\[4px]&={\frac {z^{m}}{(1-z)^{m+1}}}\sum _{k=0}^{\infty }{C_{k}\left({\frac {-z}{(1-z)^{2}}}\right)^{k}}&{\text{where }}C_{k}=k{\text{th Catalan number}}\\[4px]&={\frac {z^{m}}{(1-z)^{m+1}}}{\frac {1-{\sqrt {1+{\frac {4z}{(1-z)^{2}}}}}}{\frac {-2z}{(1-z)^{2}}}}\\[4px]&={\frac {-z^{m-1}}{2(1-z)^{m-1}}}\left(1-{\frac {1+z}{1-z}}\right)\\[4px]&={\frac {z^{m}}{(1-z)^{m}}}=z{\frac {z^{m-1}}{(1-z)^{m}}}\,.\end{aligned}}$

Then we obtain $s_{n}={\begin{cases}\displaystyle {\binom {n-1}{m-1}}&{\text{for }}m\geq 1\,,\\{}[n=0]&{\text{for }}m=0\,.\end{cases}}$

It is instructive to use the same method again for the sum, but this time take m as the free parameter instead of n. We thus set $G(z)=\sum _{m=0}^{\infty }\left(\sum _{k=0}^{\infty }{\binom {n+k}{m+2k}}{\binom {2k}{k}}{\frac {(-1)^{k}}{k+1}}\right)z^{m}\,.$

Interchanging summation ("snake oil") gives $G(z)=\sum _{k=0}^{\infty }{\binom {2k}{k}}{\frac {(-1)^{k}}{k+1}}z^{-2k}\sum _{m=0}^{\infty }{\binom {n+k}{m+2k}}z^{m+2k}\,.$

Now the inner sum is (1 + *z*)*n* + *k*. Thus ${\begin{aligned}G(z)&=(1+z)^{n}\sum _{k=0}^{\infty }{\frac {1}{k+1}}{\binom {2k}{k}}\left({\frac {-(1+z)}{z^{2}}}\right)^{k}\\[4px]&=(1+z)^{n}\sum _{k=0}^{\infty }C_{k}\,\left({\frac {-(1+z)}{z^{2}}}\right)^{k}&{\text{where }}C_{k}=k{\text{th Catalan number}}\\[4px]&=(1+z)^{n}\,{\frac {1-{\sqrt {1+{\frac {4(1+z)}{z^{2}}}}}}{\frac {-2(1+z)}{z^{2}}}}\\[4px]&=(1+z)^{n}\,{\frac {z^{2}-z{\sqrt {z^{2}+4+4z}}}{-2(1+z)}}\\[4px]&=(1+z)^{n}\,{\frac {z^{2}-z(z+2)}{-2(1+z)}}\\[4px]&=(1+z)^{n}\,{\frac {-2z}{-2(1+z)}}=z(1+z)^{n-1}\,.\end{aligned}}$

Thus we obtain $s_{n}=\left[z^{m}\right]z(1+z)^{n-1}=\left[z^{m-1}\right](1+z)^{n-1}={\binom {n-1}{m-1}}\,,$ for *m* ≥ 1 as before.

### Generating functions prove congruences

We say that two generating functions (power series) are congruent modulo m, written *A*(*z*) ≡ *B*(*z*) (mod *m*) if their coefficients are congruent modulo m for all *n* ≥ 0, i.e., *an* ≡ *bn* (mod *m*) for all relevant cases of the integers n (note that we need not assume that m is an integer here—it may very well be polynomial-valued in some indeterminate x, for example). If the "simpler" right-hand-side generating function, *B*(*z*), is a rational function of z, then the form of this sequence suggests that the sequence is eventually periodic modulo fixed particular cases of integer-valued *m* ≥ 2. For example, we can prove that the Euler numbers, $\langle E_{n}\rangle =\langle 1,1,5,61,1385,\ldots \rangle \longmapsto \langle 1,1,2,1,2,1,2,\ldots \rangle {\pmod {3}}\,,$ satisfy the following congruence modulo 3: $\sum _{n=0}^{\infty }E_{n}z^{n}={\frac {1-z^{2}}{1+z^{2}}}{\pmod {3}}\,.$

One useful method of obtaining congruences for sequences enumerated by special generating functions modulo any integers (i.e., not only prime powers *pk*) is given in the section on continued fraction representations of (even non-convergent) ordinary generating functions by J-fractions above. We cite one particular result related to generating series expanded through a representation by continued fraction from Lando's *Lectures on Generating Functions* as follows:

**Theorem: congruences for series generated by expansions of continued fractions**—Suppose that the generating function *A*(*z*) is represented by an infinite continued fraction of the form $A(z)={\cfrac {1}{1-c_{1}z-{\cfrac {p_{1}z^{2}}{1-c_{2}z-{\cfrac {p_{2}z^{2}}{1-c_{3}z-{\ddots }}}}}}}$ and that *Ap*(*z*) denotes the pth convergent to this continued fraction expansion defined such that *an* = [*zn*] *Ap*(*z*) for all 0 ≤ *n* < 2*p*. Then:

1. the function *Ap*(*z*) is rational for all *p* ≥ 2 where we assume that one of divisibility criteria of *p* | *p*1, *p*1*p*2, *p*1*p*2*p*3 is met, that is, *p* | *p*1*p*2⋯*p**k* for some *k* ≥ 1; and
2. if the integer p divides the product *p*1*p*2⋯*p**k*, then we have *A*(*z*) ≡ *Ak*(*z*) (mod *p*).

Generating functions also have other uses in proving congruences for their coefficients. We cite the next two specific examples deriving special case congruences for the Stirling numbers of the first kind and for the partition function *p*(*n*) which show the versatility of generating functions in tackling problems involving integer sequences.

#### The Stirling numbers modulo small integers

The main article on the Stirling numbers generated by the finite products $S_{n}(x):=\sum _{k=0}^{n}{\begin{bmatrix}n\\k\end{bmatrix}}x^{k}=x(x+1)(x+2)\cdots (x+n-1)\,,\quad n\geq 1\,,$

provides an overview of the congruences for these numbers derived strictly from properties of their generating function as in Section 4.6 of Wilf's stock reference *Generatingfunctionology*. We repeat the basic argument and notice that when reduces modulo 2, these finite product generating functions each satisfy

$S_{n}(x)=[x(x+1)]\cdot [x(x+1)]\cdots =x^{\left\lceil {\frac {n}{2}}\right\rceil }(x+1)^{\left\lfloor {\frac {n}{2}}\right\rfloor }\,,$

which implies that the parity of these Stirling numbers matches that of the binomial coefficient

${\begin{bmatrix}n\\k\end{bmatrix}}\equiv {\binom {\left\lfloor {\frac {n}{2}}\right\rfloor }{k-\left\lceil {\frac {n}{2}}\right\rceil }}{\pmod {2}}\,,$

and consequently shows that [*n* *k*] is even whenever *k* < ⌊ ⁠*n*/2⁠ ⌋.

Similarly, we can reduce the right-hand-side products defining the Stirling number generating functions modulo 3 to obtain slightly more complicated expressions providing that ${\begin{aligned}{\begin{bmatrix}n\\m\end{bmatrix}}&\equiv [x^{m}]\left(x^{\left\lceil {\frac {n}{3}}\right\rceil }(x+1)^{\left\lceil {\frac {n-1}{3}}\right\rceil }(x+2)^{\left\lfloor {\frac {n}{3}}\right\rfloor }\right)&&{\pmod {3}}\\&\equiv \sum _{k=0}^{m}{\begin{pmatrix}\left\lceil {\frac {n-1}{3}}\right\rceil \\k\end{pmatrix}}{\begin{pmatrix}\left\lfloor {\frac {n}{3}}\right\rfloor \\m-k-\left\lceil {\frac {n}{3}}\right\rceil \end{pmatrix}}\times 2^{\left\lceil {\frac {n}{3}}\right\rceil +\left\lfloor {\frac {n}{3}}\right\rfloor -(m-k)}&&{\pmod {3}}\,.\end{aligned}}$

#### Congruences for the partition function

In this example, we pull in some of the machinery of infinite products whose power series expansions generate the expansions of many special functions and enumerate partition functions. In particular, we recall that *the* partition function *p*(*n*) is generated by the reciprocal infinite q-Pochhammer symbol product (or z-Pochhammer product as the case may be) given by ${\begin{aligned}\sum _{n=0}^{\infty }p(n)z^{n}&={\frac {1}{\left(1-z\right)\left(1-z^{2}\right)\left(1-z^{3}\right)\cdots }}\\[4pt]&=1+z+2z^{2}+3z^{3}+5z^{4}+7z^{5}+11z^{6}+\cdots .\end{aligned}}$

This partition function satisfies many known congruence properties, which notably include the following results though there are still many open questions about the forms of related integer congruences for the function: ${\begin{aligned}p(5m+4)&\equiv 0{\pmod {5}}\\p(7m+5)&\equiv 0{\pmod {7}}\\p(11m+6)&\equiv 0{\pmod {11}}\\p(25m+24)&\equiv 0{\pmod {5^{2}}}\,.\end{aligned}}$

We show how to use generating functions and manipulations of congruences for formal power series to give a highly elementary proof of the first of these congruences listed above.

First, we observe that in the binomial coefficient generating function ${\frac {1}{(1-z)^{5}}}=\sum _{i=0}^{\infty }{\binom {4+i}{4}}z^{i}\,,$ all of the coefficients are divisible by 5 except for those which correspond to the powers 1, *z*5, *z*10, ... and moreover in those cases the remainder of the coefficient is 1 modulo 5. Thus, ${\frac {1}{(1-z)^{5}}}\equiv {\frac {1}{1-z^{5}}}{\pmod {5}}\,,$ or equivalently ${\frac {1-z^{5}}{(1-z)^{5}}}\equiv 1{\pmod {5}}\,.$ It follows that ${\frac {\left(1-z^{5}\right)\left(1-z^{10}\right)\left(1-z^{15}\right)\cdots }{\left((1-z)\left(1-z^{2}\right)\left(1-z^{3}\right)\cdots \right)^{5}}}\equiv 1{\pmod {5}}\,.$

Using the infinite product expansions of $z\cdot {\frac {\left(1-z^{5}\right)\left(1-z^{10}\right)\cdots }{\left(1-z\right)\left(1-z^{2}\right)\cdots }}=z\cdot \left((1-z)\left(1-z^{2}\right)\cdots \right)^{4}\times {\frac {\left(1-z^{5}\right)\left(1-z^{10}\right)\cdots }{\left(\left(1-z\right)\left(1-z^{2}\right)\cdots \right)^{5}}}\,,$ it can be shown that the coefficient of *z*5*m* + 5 in *z* · ((1 − *z*)(1 − *z*2)⋯)4 is divisible by 5 for all m. Finally, since ${\begin{aligned}\sum _{n=1}^{\infty }p(n-1)z^{n}&={\frac {z}{(1-z)\left(1-z^{2}\right)\cdots }}\\[6px]&=z\cdot {\frac {\left(1-z^{5}\right)\left(1-z^{10}\right)\cdots }{(1-z)\left(1-z^{2}\right)\cdots }}\times \left(1+z^{5}+z^{10}+\cdots \right)\left(1+z^{10}+z^{20}+\cdots \right)\cdots \end{aligned}}$ we may equate the coefficients of *z*5*m* + 5 in the previous equations to prove our desired congruence result, namely that *p*(5*m* + 4) ≡ 0 (mod 5) for all *m* ≥ 0.

### Transformations of generating functions

There are a number of transformations of generating functions that provide other applications (see the main article). A transformation of a sequence's *ordinary generating function* (OGF) provides a method of converting the generating function for one sequence into a generating function enumerating another. These transformations typically involve integral formulas involving a sequence OGF (see integral transformations) or weighted sums over the higher-order derivatives of these functions (see derivative transformations).

Generating function transformations can come into play when we seek to express a generating function for the sums $s_{n}:=\sum _{m=0}^{n}{\binom {n}{m}}C_{n,m}a_{m},$

in the form of *S*(*z*) = *g*(*z*) *A*(*f*(*z*)) involving the original sequence generating function. For example, if the sums are $s_{n}:=\sum _{k=0}^{\infty }{\binom {n+k}{m+2k}}a_{k}\,$ then the generating function for the modified sum expressions is given by $S(z)={\frac {z^{m}}{(1-z)^{m+1}}}A\left({\frac {z}{(1-z)^{2}}}\right)$ (see also the binomial transform and the Stirling transform).

There are also integral formulas for converting between a sequence's OGF, *F*(*z*), and its exponential generating function, or EGF, *F̂*(*z*), and vice versa given by ${\begin{aligned}F(z)&=\int _{0}^{\infty }{\hat {F}}(tz)e^{-t}\,dt\,,\\[4px]{\hat {F}}(z)&={\frac {1}{2\pi }}\int _{-\pi }^{\pi }F\left(ze^{-i\vartheta }\right)e^{e^{i\vartheta }}\,d\vartheta \,,\end{aligned}}$

provided that these integrals converge for appropriate values of z.


## Tables of special generating functions

An initial listing of special mathematical series is found here. A number of useful and special sequence generating functions are found in Section 5.4 and 7.4 of *Concrete Mathematics* and in Section 2.5 of Wilf's *Generatingfunctionology*. Other special generating functions of note include the entries in the next table, which is by no means complete.

| Formal power series | Generating-function formula | Notes |
|---|---|---|
| $\sum _{n=0}^{\infty }{\binom {m+n}{n}}\left(H_{n+m}-H_{m}\right)z^{n}$ | ${\frac {1}{(1-z)^{m+1}}}\ln {\frac {1}{1-z}}$ | $H_{n}$ is a first-order harmonic number |
| $\sum _{n=0}^{\infty }B_{n}{\frac {z^{n}}{n!}}$ | ${\frac {z}{e^{z}-1}}$ | $B_{n}$ is a Bernoulli number |
| $\sum _{n=0}^{\infty }F_{mn}z^{n}$ | ${\frac {F_{m}z}{1-(F_{m-1}+F_{m+1})z+(-1)^{m}z^{2}}}$ | $F_{n}$ is a Fibonacci number and $m\in \mathbb {Z} ^{+}$ |
| $\sum _{n=0}^{\infty }\left\{{\begin{matrix}n\\m\end{matrix}}\right\}z^{n}$ | $(z^{-1})^{\overline {-m}}={\frac {z^{m}}{(1-z)(1-2z)\cdots (1-mz)}}$ | $x^{\overline {n}}$ denotes the rising factorial, or Pochhammer symbol and some integer $m\geq 0$ |
| $\sum _{n=0}^{\infty }\left[{\begin{matrix}n\\m\end{matrix}}\right]z^{n}$ | $z^{\overline {m}}=z(z+1)\cdots (z+m-1)$ |   |
| $\sum _{n=1}^{\infty }{\frac {(-1)^{n-1}4^{n}(4^{n}-2)B_{2n}z^{2n}}{(2n)\cdot (2n)!}}$ | $\ln {\frac {\tan(z)}{z}}$ |   |
| $\sum _{n=0}^{\infty }{\frac {(1/2)^{\overline {n}}z^{2n}}{(2n+1)\cdot n!}}$ | $z^{-1}\arcsin(z)$ |   |
| $\sum _{n=0}^{\infty }H_{n}^{(s)}z^{n}$ | ${\frac {\operatorname {Li} _{s}(z)}{1-z}}$ | $\operatorname {Li} _{s}(z)$ is the polylogarithm function and $H_{n}^{(s)}$ is a generalized harmonic number for $\Re (s)>1$ |
| $\sum _{n=0}^{\infty }n^{m}z^{n}$ | $\sum _{0\leq j\leq m}\left\{{\begin{matrix}m\\j\end{matrix}}\right\}{\frac {j!\cdot z^{j}}{(1-z)^{j+1}}}$ | $\left\{{\begin{matrix}n\\m\end{matrix}}\right\}$ is a Stirling number of the second kind and where the individual terms in the expansion satisfy ${\frac {z^{i}}{(1-z)^{i+1}}}=\sum _{k=0}^{i}{\binom {i}{k}}{\frac {(-1)^{k-i}}{(1-z)^{k+1}}}$ |
| $\sum _{k<n}{\binom {n-k}{k}}{\frac {n}{n-k}}z^{k}$ | $\left({\frac {1+{\sqrt {1+4z}}}{2}}\right)^{n}+\left({\frac {1-{\sqrt {1+4z}}}{2}}\right)^{n}$ |   |
| $\sum _{n_{1},\ldots ,n_{m}\geq 0}\min(n_{1},\ldots ,n_{m})z_{1}^{n_{1}}\cdots z_{m}^{n_{m}}$ | ${\frac {z_{1}\cdots z_{m}}{(1-z_{1})\cdots (1-z_{m})(1-z_{1}\cdots z_{m})}}$ | The two-variable case is given by $M(w,z):=\sum _{m,n\geq 0}\min(m,n)w^{m}z^{n}={\frac {wz}{(1-w)(1-z)(1-wz)}}$ |
| $\sum _{n=0}^{\infty }{\binom {s}{n}}z^{n}$ | $(1+z)^{s}$ | $s\in \mathbb {C}$ |
| $\sum _{n=0}^{\infty }{\binom {n}{k}}z^{n}$ | ${\frac {z^{k}}{(1-z)^{k+1}}}$ | $k\in \mathbb {N}$ |
| $\sum _{n=1}^{\infty }\log {(n)}z^{n}$ | $\left.-{\frac {\partial }{\partial s}}\operatorname {{Li}_{s}(z)} \right\|_{s=0}$ |   |
