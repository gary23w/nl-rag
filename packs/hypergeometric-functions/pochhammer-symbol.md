---
title: "Falling and rising factorials"
source: https://en.wikipedia.org/wiki/Pochhammer_symbol
domain: hypergeometric-functions
license: CC-BY-SA-4.0
tags: hypergeometric function, confluent hypergeometric function, pochhammer symbol, hypergeometric series
fetched: 2026-07-02
---

# Falling and rising factorials

(Redirected from

Pochhammer symbol

)

In mathematics, the **falling factorial** (sometimes called the **descending factorial**, **falling sequential product**, or **lower factorial**) is defined as the polynomial ${\begin{aligned}(x)_{n}=x^{\underline {n}}&=\overbrace {x(x-1)(x-2)\cdots (x-n+1)} ^{n{\text{ factors}}}\\&=\prod _{k=1}^{n}(x-k+1)=\prod _{k=0}^{n-1}(x-k).\end{aligned}}$

The **rising factorial** (sometimes called the **Pochhammer function**, **Pochhammer polynomial**, **ascending factorial**, **rising sequential product**, or **upper factorial**) is defined as ${\begin{aligned}x^{(n)}=x^{\overline {n}}&=\overbrace {x(x+1)(x+2)\cdots (x+n-1)} ^{n{\text{ factors}}}\\&=\prod _{k=1}^{n}(x+k-1)=\prod _{k=0}^{n-1}(x+k).\end{aligned}}$

The value of each is taken to be 1 (an empty product) when $n=0$ . These symbols are collectively called **factorial powers**.

The **Pochhammer symbol**, introduced by Leo August Pochhammer, is the notation $(x)_{n}$ , where n is a non-negative integer. It may represent *either* the rising or the falling factorial, with different articles and authors using different conventions. Pochhammer himself actually used $(x)_{n}$ with yet another meaning, namely to denote the binomial coefficient ${\tbinom {x}{n}}$ .

In this article, the symbol $(x)_{n}$ is used to represent the falling factorial, and the symbol $x^{(n)}$ is used for the rising factorial. These conventions are used in combinatorics, although Knuth's underline and overline notations $x^{\underline {n}}$ and $x^{\overline {n}}$ are increasingly popular. In the theory of special functions (in particular the hypergeometric function) and in the standard reference work *Abramowitz and Stegun*, the Pochhammer symbol $(x)_{n}$ is used to represent the rising factorial.

When x is a positive integer, the falling factorial $(x)_{n}$ gives the number of n-permutations, sequences of n distinct elements) from an x -element set, or equivalently the number of injective functions from a set of size n to a set of size x . The rising factorial $x^{(n)}$ gives the number of partitions of an n -element set into x ordered sequences (possibly empty).

## Examples and combinatorial interpretation

The first few falling factorials are as follows: ${\begin{alignedat}{2}(x)_{0}&&&=1\\(x)_{1}&&&=x\\(x)_{2}&=x(x-1)&&=x^{2}-x\\(x)_{3}&=x(x-1)(x-2)&&=x^{3}-3x^{2}+2x\\(x)_{4}&=x(x-1)(x-2)(x-3)&&=x^{4}-6x^{3}+11x^{2}-6x\end{alignedat}}$

The first few rising factorials are as follows: ${\begin{alignedat}{2}x^{(0)}&&&=1\\x^{(1)}&&&=x\\x^{(2)}&=x(x+1)&&=x^{2}+x\\x^{(3)}&=x(x+1)(x+2)&&=x^{3}+3x^{2}+2x\\x^{(4)}&=x(x+1)(x+2)(x+3)&&=x^{4}+6x^{3}+11x^{2}+6x\end{alignedat}}$

The coefficients that appear in the expansions are Stirling numbers of the first kind; see § Connection coefficients and identities below.

When the variable x is a positive integer, the number $(x)_{n}$ is equal to the number of n-permutations from a set of x items, that is, the number of ways of choosing an ordered list of length n consisting of distinct elements drawn from a collection of size x . For example, $(8)_{3}=8\times 7\times 6=336$ is the number of possible different podiums, assignments of gold, silver, and bronze medals in eight-person race. On the other hand, $x^{(n)}$ is "the number of ways to arrange n flags on x flagpoles", where all flags must be used and each flagpole can have any number of flags. Equivalently, this is the number of ways to partition a set of size n (the flags) into x disjoint parts (the flagpoles), with a linear order on the elements in each part (the order of the flags on each pole).

## Properties

The rising and falling factorials are simply related to one another: ${\begin{alignedat}{2}{(x)}_{n}&={(x-n+1)}^{(n)}&&=(-1)^{n}(-x)^{(n)},\\x^{(n)}&={(x+n-1)}_{n}&&=(-1)^{n}(-x)_{n}.\end{alignedat}}$ Falling and rising factorials of integers are directly related to the ordinary factorial: ${\begin{aligned}n!&=1^{(n)}=(n)_{n},\\[6pt](m)_{n}&={\frac {m!}{(m-n)!}},\\[6pt]m^{(n)}&={\frac {(m+n-1)!}{(m-1)!}}.\end{aligned}}$ A useful identity for the sums of falling factorials is $\sum _{k=0}^{n-1}(k)_{m}={\frac {(n)_{m+1}}{m+1}}.$ Rising factorials of half integers are directly related to the double factorial $m!!=m(m-2)(m-4)\cdots$ : ${\begin{aligned}\left[{\frac {1}{2}}\right]^{(n)}={\frac {(2n-1)!!}{2^{n}}},\quad \left[{\frac {2m+1}{2}}\right]^{(n)}={\frac {(2(n+m)-1)!!}{2^{n}(2m-1)!!}}.\end{aligned}}$ The falling and rising factorials can be used to express a binomial coefficient: ${\begin{aligned}{\frac {(x)_{n}}{n!}}&={\binom {x}{n}},\\[6pt]{\frac {x^{(n)}}{n!}}&={\binom {x+n-1}{n}}.\end{aligned}}$ Thus many identities on binomial coefficients carry over to the falling and rising factorials.

The rising and falling factorials are well defined in any unital ring, and therefore x can be taken to be, for example, a complex number, including negative integers, or a polynomial with complex coefficients, or any complex-valued function.

### Calculus

Falling factorials appear in multiple differentiation of simple power functions: $\left({\frac {\mathrm {d} }{\mathrm {d} x}}\right)^{n}x^{a}=(a)_{n}\cdot x^{a-n}.$ The rising factorial is also integral to the definition of the hypergeometric function: The hypergeometric function is defined for $|z|<1$ by the power series ${}_{2}F_{1}(a,b;c;z)=\sum _{n=0}^{\infty }{\frac {a^{(n)}b^{(n)}}{c^{(n)}}}{\frac {z^{n}}{n!}}$ provided that $c\neq 0,-1,-2,\ldots$ . Note, however, that the hypergeometric function literature typically uses the notation $(a)_{n}$ for rising factorials.

## Connection coefficients and identities

Falling and rising factorials are closely related to Stirling numbers. Indeed, expanding the product reveals Stirling numbers of the first kind ${\begin{aligned}(x)_{n}&=\sum _{k=0}^{n}s(n,k)x^{k}=\sum _{k=0}^{n}{\begin{bmatrix}n\\k\end{bmatrix}}(-1)^{n-k}x^{k}\\x^{(n)}&=\sum _{k=0}^{n}{\begin{bmatrix}n\\k\end{bmatrix}}x^{k}\\\end{aligned}}$ And the inverse relations uses Stirling numbers of the second kind ${\begin{aligned}x^{n}&=\sum _{k=0}^{n}{\begin{Bmatrix}n\\k\end{Bmatrix}}(x)_{k}\\&=\sum _{k=0}^{n}{\begin{Bmatrix}n\\k\end{Bmatrix}}(-1)^{n-k}x^{(k)}.\end{aligned}}$ The falling and rising factorials are related to one another through the Lah numbers ${\textstyle L(n,k)={\binom {n-1}{k-1}}{\frac {n!}{k!}}}$ : ${\begin{aligned}x^{(n)}&=\sum _{k=0}^{n}L(n,k)(x)_{k}\\(x)_{n}&=\sum _{k=0}^{n}L(n,k)(-1)^{n-k}x^{(k)}\end{aligned}}$ Since the falling factorials are a basis for the polynomial ring, one can express the product of two of them as a linear combination of falling factorials: $(x)_{m}(x)_{n}=\sum _{k=0}^{m}{\binom {m}{k}}{\binom {n}{k}}k!\cdot (x)_{m+n-k}\ .$ The coefficients ${\tbinom {m}{k}}{\tbinom {n}{k}}k!$ are called *connection coefficients*, and have a combinatorial interpretation as the number of ways to identify (or "glue together") k elements each from a set of size m and a set of size n.

There is also a connection formula for the ratio of two rising factorials given by ${\frac {x^{(n)}}{x^{(i)}}}=(x+i)^{(n-i)},\quad {\text{for }}n\geq i.$ Additionally, we can expand generalized exponent laws and negative rising and falling powers through the following identities: ${\begin{aligned}(x)_{m+n}&=(x)_{m}(x-m)_{n}=(x)_{n}(x-n)_{m}\\[6pt]x^{(m+n)}&=x^{(m)}(x+m)^{(n)}=x^{(n)}(x+n)^{(m)}\\[6pt]x^{(-n)}&={\frac {\Gamma (x-n)}{\Gamma (x)}}={\frac {(x-n-1)!}{(x-1)!}}={\frac {1}{(x-n)^{(n)}}}={\frac {1}{(x-1)_{n}}}={\frac {1}{(x-1)(x-2)\cdots (x-n)}}\\[6pt](x)_{-n}&={\frac {\Gamma (x+1)}{\Gamma (x+n+1)}}={\frac {x!}{(x+n)!}}={\frac {1}{(x+n)_{n}}}={\frac {1}{(x+1)^{(n)}}}={\frac {1}{(x+1)(x+2)\cdots (x+n)}}\end{aligned}}$ Finally, duplication and multiplication formulas for the falling and rising factorials provide the next relations: ${\begin{aligned}(x)_{k+mn}&=x^{(k)}m^{mn}\prod _{j=0}^{m-1}\left({\frac {x-k-j}{m}}\right)_{n}&{\text{ for }}m&\in \mathbb {N} \\[6pt]x^{(k+mn)}&=x^{(k)}m^{mn}\prod _{j=0}^{m-1}\left({\frac {x+k+j}{m}}\right)^{(n)}&{\text{ for }}m&\in \mathbb {N} \\[6pt](ax+b)^{(n)}&=x^{n}\prod _{j=0}^{n-1}\left(a+{\frac {b+j}{x}}\right)&{\text{ for }}x&\neq 0\\[6pt](2x)^{(2n)}&=2^{2n}x^{(n)}\left(x+{\frac {1}{2}}\right)^{(n)}.\end{aligned}}$

## Relation to umbral calculus

The falling factorial occurs in a formula which represents polynomials using the forward difference operator $\operatorname {\Delta } f(x)~{\stackrel {\mathrm {def} }{=}}~f(x+1)-f(x),$ which in form is an exact analogue to Taylor's theorem: Compare the series expansion from umbral calculus

$\qquad f(t)=\sum _{n=0}^{\infty }\ {\frac {1}{n!}}\operatorname {\Delta } _{x}^{n}f(x){\bigg \vert }_{x=0}(t)_{n}\qquad$

with the corresponding series from differential calculus

$\qquad f(t)=\sum _{n=0}^{\infty }{\frac {1}{n!}}\left[{\frac {d}{dx}}\right]^{n}f(x){\bigg \vert }_{x=0}t^{n}~.$

In this formula and in many other places, the falling factorial $(x)_{n}$ in the calculus of finite differences plays the role of $x^{n}$ in differential calculus. For another example, note the similarity of $~\operatorname {\Delta } (x)_{n}=n(x)_{n-1}~$ to $~{\frac {d}{dx}}x^{n}=nx^{n-1}~.$

A corresponding relation holds for the rising factorial and the backward difference operator.

The study of analogies of this type is known as umbral calculus. A general theory covering such relations, including the falling and rising factorial functions, is given by the theory of polynomial sequences of binomial type and Sheffer sequences. Falling and rising factorials are Sheffer sequences of binomial type, as shown by the relations:

$\ {\begin{aligned}(a+b)_{n}&=\sum _{j=0}^{n}{\binom {n}{j}}(a)_{n-j}(b)_{j}\\[6pt](a+b)^{(n)}&=\sum _{j=0}^{n}{\binom {n}{j}}a^{(n-j)}b^{(j)}\end{aligned}}\$

where the coefficients are the same as those in the binomial theorem.

Similarly, the generating function of Pochhammer polynomials then amounts to the umbral exponential,

$\ \sum _{n=0}^{\infty }(x)_{n}{\frac {t^{n}}{n!}}=(1+t)^{x},$

since

$\ \operatorname {\Delta } _{x}(1+t)^{x}=t\cdot (1+t)^{x}~.$

## Alternative notations

An alternative notation for the rising factorial $x^{\overline {m}}\equiv (x)_{+m}\equiv (x)_{m}=\overbrace {x(x+1)\ldots (x+m-1)} ^{m{\text{ factors}}}\quad {\text{for integer }}m\geq 0$ and for the falling factorial $x^{\underline {m}}\equiv (x)_{-m}=\overbrace {x(x-1)\ldots (x-m+1)} ^{m{\text{ factors}}}\quad {\text{for integer }}m\geq 0$ goes back to A. Capelli (1893) and L. Toscano (1939), respectively. Graham, Knuth, and Patashnik propose to pronounce these expressions as "x to the m rising" and "x to the m falling", respectively.

An alternative notation for the rising factorial $x^{(n)}$ is the less common $(x)_{n}^{+}~.$ When $(x)_{n}^{+}$ is used to denote the rising factorial, the notation $(x)_{n}^{-}$ is typically used for the ordinary falling factorial, to avoid confusion.

## Generalizations

The Pochhammer symbol has a generalized version called the generalized Pochhammer symbol, used in multivariate analysis. There is also a q-analogue, the q-Pochhammer symbol.

For any fixed arithmetic function $f:\mathbb {N} \rightarrow \mathbb {C}$ and symbolic parameters x, t, related generalized factorial products of the form

$(x)_{n,f,t}:=\prod _{k=0}^{n-1}\left(x+{\frac {f(k)}{t^{k}}}\right)$

may be studied from the point of view of the classes of generalized Stirling numbers of the first kind defined by the following coefficients of the powers of x in the expansions of (*x*)*n*,*f*,*t* and then by the next corresponding triangular recurrence relation:

${\begin{aligned}\left[{\begin{matrix}n\\k\end{matrix}}\right]_{f,t}&=\left[x^{k-1}\right](x)_{n,f,t}\\&=f(n-1)t^{1-n}\left[{\begin{matrix}n-1\\k\end{matrix}}\right]_{f,t}+\left[{\begin{matrix}n-1\\k-1\end{matrix}}\right]_{f,t}+\delta _{n,0}\delta _{k,0}.\end{aligned}}$

These coefficients satisfy a number of analogous properties to those for the Stirling numbers of the first kind as well as recurrence relations and functional equations related to the f-harmonic numbers, $F_{n}^{(r)}(t):=\sum _{k\leq n}{\frac {t^{k}}{f(k)^{r}}}\,.$
