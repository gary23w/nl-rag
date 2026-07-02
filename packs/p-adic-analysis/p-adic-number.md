---
title: "p-adic number"
source: https://en.wikipedia.org/wiki/P-adic_number
domain: p-adic-analysis
license: CC-BY-SA-4.0
tags: p-adic analysis, p-adic number, hensel's lemma, local field
fetched: 2026-07-02
---

# *p*-adic number

In number theory, given a prime number p, the **p-adic numbers** form an extension of the rational numbers that is distinct from the real numbers, though with some similar properties; p-adic numbers can be written in a form similar to (possibly infinite) decimals, but with digits based on a prime number p rather than ten, and extending to the left rather than to the right.

For example, comparing the expansion of the rational number ${\tfrac {1}{5}}$ in base 3 vs. the 3-adic expansion, ${\begin{alignedat}{3}{\tfrac {1}{5}}&{}=0.01210121\ldots \ ({\text{base }}3)&&{}=0\cdot 3^{0}+0\cdot 3^{-1}+1\cdot 3^{-2}+2\cdot 3^{-3}+\cdots \\[5mu]{\tfrac {1}{5}}&{}=\dots 121012102\ \ ({\text{3-adic}})&&{}=\cdots +2\cdot 3^{3}+1\cdot 3^{2}+0\cdot 3^{1}+2\cdot 3^{0}.\end{alignedat}}$

Formally, given a prime number p, a p-adic number can be defined as a series $s=\sum _{i=k}^{\infty }a_{i}p^{i}=a_{k}p^{k}+a_{k+1}p^{k+1}+a_{k+2}p^{k+2}+\cdots$ where k is an integer (possibly negative), and each $a_{i}$ is an integer such that $0\leq a_{i}<p.$ A **p-adic integer** is a p-adic number such that $k\geq 0.$

In general the series that represents a p-adic number is not convergent in the usual sense, but it is convergent for the p-adic absolute value $|s|_{p}=p^{-k},$ where k is the least integer i such that $a_{i}\neq 0$ (if all $a_{i}$ are zero, one has the zero p-adic number, which has 0 as its p-adic absolute value).

Every rational number can be uniquely expressed as the sum of a series as above, with respect to the p-adic absolute value. This allows considering rational numbers as special p-adic numbers, and alternatively defining the p-adic numbers as the completion of the rational numbers for the p-adic absolute value, exactly as the real numbers are the completion of the rational numbers for the usual absolute value.

p-adic numbers were first described by Kurt Hensel in 1897, though, with hindsight, some of Ernst Kummer's earlier work can be interpreted as implicitly using p-adic numbers.

## Motivation

Roughly speaking, modular arithmetic modulo a positive integer n consists of "approximating" every integer by the remainder of its division by n, called its *residue modulo* n. The main property of modular arithmetic is that the residue modulo n of the result of a succession of operations on integers is the same as the result of the same succession of operations on residues modulo n.

When studying Diophantine equations, it's sometimes useful to reduce the equation modulo a prime p, since this usually provides more insight about the equation itself. Unfortunately, doing this loses some information because the reduction $\mathbb {Z} \twoheadrightarrow \mathbb {Z} /p$ is not injective.

One way to preserve more information is to use larger moduli, such as higher prime powers, *p*2, *p*3, .... However, this has the disadvantage of $\mathbb {Z} /p^{e}$ not being a field, which loses a lot of the algebraic properties that $\mathbb {Z} /p$ has.

Kurt Hensel discovered a method which consists of using a prime modulus p, and applying Hensel's lemma to lift solutions modulo p to modulo *p*2, *p*3, .... This process creates an infinite sequence of residues, and a p-adic number is defined as the "limit" of such a sequence.

Essentially, p-adic numbers allows "taking modulo *p**e* for all e at once". A distinguishing feature of p-adic numbers from ordinary modulo arithmetic is that the set of p-adic numbers $\mathbb {Q} _{p}$ forms a field, making division by p possible (unlike when working modulo *p**e*). Furthermore, the mapping $\mathbb {Z} \hookrightarrow \mathbb {Z} _{p}$ is injective, so not much information is lost when reducing to p-adic numbers.

## Informal description

There are multiple ways to understand p-adic numbers.

### As a base-*p* expansion

One way to think about p-adic integers is using "base p". For example, every integer can be written in base p,

$50=1212_{3}=1\cdot 3^{3}+2\cdot 3^{2}+1\cdot 3^{1}+2\cdot 3^{0}$

Informally, **p-adic integers** can be thought of as integers in base-p, but the digits extend *infinitely to the left*.

$\ldots 121012102_{3}=\cdots +2\cdot 3^{3}+1\cdot 3^{2}+0\cdot 3^{1}+2\cdot 3^{0}$

Addition and multiplication on p-adic integers can be carried in a way somewhat similar to integers in base-p.

When adding together two p-adic integers, for example $\ldots 012102_{3}+\ldots 101211_{3}$ , their digits are added with carries being propagated from right to left.

${\begin{array}{cccccccc}&&&_{1}&_{1}&&_{1}&\\&\cdots &0&1&2&1&0&2\,_{3}\\+&\cdots &1&0&1&2&1&1\,_{3}\\\hline &\cdots &1&2&1&0&2&0\,_{3}\end{array}}$

Multiplication of p-adic integers works similarly via long multiplication. Since addition and multiplication can be performed with p-adic integers, they form a ring, denoted $\mathbb {Z} _{p}$ or $\mathbf {Z} _{p}$ .

Note that some rational numbers can also be p-adic integers, even if they aren't integers in a real sense. For example, the rational number ⁠1/5⁠ is a 3-adic integer, and has the 3-adic expansion ${\tfrac {1}{5}}=\ldots 121012102_{3}$ . However, some rational numbers, such as ${\tfrac {1}{p}}$ , cannot be written as a p-adic integer. Because of this, p-adic integers are generalized further to p-adic numbers:

**p-adic numbers** can be thought of as p-adic integers with *finitely many digits after the decimal point*. An example of a 3-adic number is

$\ldots 121012.102_{3}=\cdots +1\cdot 3^{1}+2\cdot 3^{0}+1\cdot 3^{-1}+0\cdot 3^{-2}+2\cdot 3^{-3}$

Equivalently, every p-adic number is of the form ${\tfrac {x}{p^{k}}}$ , where x is a p-adic integer.

For any nonzero p-adic number x, its multiplicative inverse ${\tfrac {1}{x}}$ is also a p-adic number, which can be computed using a variant of long division. For this reason, the p-adic numbers form a field, denoted $\mathbb {Q} _{p}$ or $\mathbf {Q} _{p}$ .

### As a sequence of residues mod p*k*

Another way to define p-adic integers is by representing it as a sequence of residues $x_{e}$ mod $p^{e}$ for each integer e ,, Here each $x_{i}$ denotes an integer representative of a residue class modulo $p^{i}$

$x=(x_{1}\operatorname {mod} p,~x_{2}\operatorname {mod} p^{2},~x_{3}\operatorname {mod} p^{3},~\ldots )$

satisfying the compatibility relations $x_{i}\equiv x_{j}~(\operatorname {mod} p^{i})$ for $i<j$ . In this notation, addition and multiplication of p-adic integers are defined component-wise:

$x+y=(x_{1}+y_{1}\operatorname {mod} p,~x_{2}+y_{2}\operatorname {mod} p^{2},~x_{3}+y_{3}\operatorname {mod} p^{3},~\ldots )$ $x\cdot y=(x_{1}\cdot y_{1}\operatorname {mod} p,~x_{2}\cdot y_{2}\operatorname {mod} p^{2},~x_{3}\cdot y_{3}\operatorname {mod} p^{3},~\ldots )$

This is equivalent to the base-p definition, because the last k digits of a base-p expansion uniquely define its value mod p*k*, and vice versa.

This form can also explain why some rational numbers are p-adic integers, even if they are not integers. For example, ⁠1/5⁠ is a 3-adic integer, because its 3-adic expansion consists of the multiplicative inverses of 5 mod 3, 32, 33, ...

${\begin{aligned}{\frac {1}{5}}&=({\tfrac {1}{5}}\operatorname {mod} 3,~{\tfrac {1}{5}}\operatorname {mod} 3^{2},~{\tfrac {1}{5}}\operatorname {mod} 3^{3},~{\tfrac {1}{5}}\operatorname {mod} 3^{4},~\ldots )\\&=(2\operatorname {mod} 3,~2\operatorname {mod} 3^{2},~11\operatorname {mod} 3^{3},~65\operatorname {mod} 3^{4},~\ldots )\end{aligned}}$

## Definition

There are several equivalent definitions of p-adic numbers. The two approaches given below are relatively elementary.

### As formal series in base p

A **p-adic integer** is often defined as a formal power series of the form $r=\sum _{i=0}^{\infty }a_{i}p^{i}=a_{0}+a_{1}p+a_{2}p^{2}+a_{3}p^{3}+\cdots$ where each $a_{i}\in \{0,1,\ldots ,p-1\}$ represents a "digit in base p".

A **p-adic unit** is a p-adic integer whose first digit is nonzero, i.e. $a_{0}\neq 0$ . The set of all p-adic integers is usually denoted $\mathbb {Z} _{p}$ .

A **p-adic number** is then defined as a formal Laurent series of the form $r=\sum _{i=v}^{\infty }a_{i}p^{i}=a_{v}p^{v}+a_{v+1}p^{v+1}+a_{v+2}p^{v+2}+a_{v+3}p^{v+3}+\cdots$ where v is a (possibly negative) integer, and each $a_{i}\in \{0,1,\ldots ,p-1\}$ . Equivalently, a p-adic number is anything of the form ${\tfrac {x}{p^{k}}}$ , where x is a p-adic integer.

The first index v for which the digit $a_{v}$ is nonzero in r is called the p-adic valuation of r, denoted $v_{p}(r)$ . If $r=0$ , then such an index does not exist, so by convention $v_{p}(0)=\infty$ .

In this definition, addition, subtraction, multiplication, and division of p-adic numbers are carried out similarly to numbers in base p, with "carries" or "borrows" moving from left to right rather than right to left. As an example in $\mathbb {Q} _{3}$ ,

${\begin{array}{lllllllllll}&&&_{1}&&&&_{1}&&_{1}\\&2\cdot 3^{0}&+&0\cdot 3^{1}&+&1\cdot 3^{2}&+&2\cdot 3^{3}&+&1\cdot 3^{4}&+\cdots \\+&1\cdot 3^{0}&+&1\cdot 3^{1}&+&2\cdot 3^{2}&+&1\cdot 3^{3}&+&0\cdot 3^{4}&+\cdots \\\hline &0\cdot 3^{0}&+&2\cdot 3^{1}&+&0\cdot 3^{2}&+&1\cdot 3^{3}&+&2\cdot 3^{4}&+\cdots \end{array}}$

Division of p-adic numbers may also be carried out "formally" via division of formal power series, with some care about having to "carry".

With these operations, the set of p-adic numbers form a field, denoted $\mathbb {Q} _{p}$ .

### As equivalence classes

The p-adic numbers may also be defined as equivalence classes, in a similar way as the definition of real numbers as equivalence classes of Cauchy sequences. It is fundamentally based on the following lemma:

Every nonzero rational number

r

can be written

${\textstyle r=p^{v}{\frac {m}{n}},}$

where

v

,

m

, and

n

are integers and neither

m

nor

n

is divisible by

p

.

The exponent v is uniquely determined by r and is called its **p-adic valuation**, denoted $v_{p}(r)$ . The proof of the lemma results directly from the fundamental theorem of arithmetic.

A **p-adic series** is a formal Laurent series of the form $\sum _{i=v}^{\infty }r_{i}p^{i},$ where v is a (possibly negative) integer and the $r_{i}$ are rational numbers that either are zero or have a nonnegative valuation (that is, the denominator of $r_{i}$ is not divisible by p).

Every rational number may be viewed as a p-adic series with a single nonzero term, consisting of its factorization of the form $p^{k}{\tfrac {m}{n}},$ with m and n both coprime with p.

Two p-adic series ${\textstyle \sum _{i=v}^{\infty }r_{i}p^{i}}$ and ${\textstyle \sum _{i=w}^{\infty }s_{i}p^{i}}$ are *equivalent* if there is an integer N such that, for every integer $n>N,$ the rational number $\sum _{i=v}^{n}r_{i}p^{i}-\sum _{i=w}^{n}s_{i}p^{i}$ is zero or has a p-adic valuation greater than n.

A p-adic series ${\textstyle \sum _{i=v}^{\infty }a_{i}p^{i}}$ is *normalized* if either all $a_{i}$ are integers such that $0\leq a_{i}<p,$ and $a_{v}>0,$ or all $a_{i}$ are zero. In the latter case, the series is called the *zero series*.

Every p-adic series is equivalent to exactly one normalized series. This normalized series is obtained by a sequence of transformations, which are equivalences of series; see § Normalization of a p-adic series, below.

In other words, the equivalence of p-adic series is an equivalence relation, and each equivalence class contains exactly one normalized p-adic series.

The usual operations of series (addition, subtraction, multiplication, division) are compatible with equivalence of p-adic series. That is, denoting the equivalence with ~, if S, T and U are nonzero p-adic series such that $S\sim T,$ one has ${\begin{aligned}S\pm U&\sim T\pm U,\\SU&\sim TU,\\1/S&\sim 1/T.\end{aligned}}$

With this, the **p-adic numbers** are defined as the *equivalence classes* of p-adic series.

The uniqueness property of normalization, allows uniquely representing any p-adic number by the corresponding normalized p-adic series. The compatibility of the series equivalence leads almost immediately to basic properties of p-adic numbers:

- *Addition*, *multiplication* and multiplicative inverse of p-adic numbers are defined as for formal power series, followed by the normalization of the result.
- With these operations, the p-adic numbers form a field, which is an extension field of the rational numbers.
- The *valuation* of a nonzero p-adic number x, commonly denoted $v_{p}(x)$ is the exponent of p in the first non zero term of the corresponding normalized series; the valuation of zero is $v_{p}(0)=+\infty$
- The *p-adic absolute value* of a nonzero p-adic number x, is $|x|_{p}=p^{-v(x)};$ for the zero p-adic number, one has $|0|_{p}=0.$

#### Normalization of a *p*-adic series

Starting with the series ${\textstyle \sum _{i=v}^{\infty }r_{i}p^{i},}$ we wish to arrive at an equivalent series such that the p-adic valuation of $r_{v}$ is zero. For that, one considers the first nonzero $r_{i}.$ If its p-adic valuation is zero, it suffices to change v into i, that is to start the summation from v. Otherwise, the p-adic valuation of $r_{i}$ is $j>0,$ and $r_{i}=p^{j}s_{i}$ where the valuation of $s_{i}$ is zero; so, one gets an equivalent series by changing $r_{i}$ to 0 and $r_{i+j}$ to $r_{i+j}+s_{i}.$ Iterating this process, one gets eventually, possibly after infinitely many steps, an equivalent series that either is the zero series or is a series such that the valuation of $r_{v}$ is zero.

Then, if the series is not normalized, consider the first nonzero $r_{i}$ that is not an integer in the interval $[0,p-1].$ Using Bézout's lemma, write this as $r_{i}=a_{i}+ps_{i}$ , where $a_{i}\in [0,p-1]$ and $s_{i}$ has nonnegative valuation. Then, one gets an equivalent series by replacing $r_{i}$ with $a_{i},$ and adding $s_{i}$ to $r_{i+1}.$ Iterating this process, possibly infinitely many times, provides eventually the desired normalized p-adic series.

### Other equivalent definitions

Other equivalent definitions use completion of a discrete valuation ring (see § p-adic integers), completion of a metric space (see § Topological properties), or inverse limits (see § Modular properties).

A p-adic number can be defined as a *normalized p-adic series*. Since there are other equivalent definitions that are commonly used, one says often that a normalized p-adic series *represents* a p-adic number, instead of saying that it *is* a p-adic number.

One can say also that any p-adic series represents a p-adic number, since every p-adic series is equivalent to a unique normalized p-adic series. This is useful for defining operations (addition, subtraction, multiplication, division) of p-adic numbers: the result of such an operation is obtained by normalizing the result of the corresponding operation on series. This well defines operations on p-adic numbers, since the series operations are compatible with equivalence of p-adic series.

With these operations, p-adic numbers form a field called the **field of *p*-adic numbers** and denoted $\mathbb {Q} _{p}$ or $\mathbf {Q} _{p}.$ There is a unique field homomorphism from the rational numbers into the p-adic numbers, which maps a rational number to its p-adic expansion. The image of this homomorphism is commonly identified with the field of rational numbers. This allows considering the *p*-adic numbers as an extension field of the rational numbers, and the rational numbers as a subfield of the *p*-adic numbers.

The *valuation* of a nonzero p-adic number x, commonly denoted $v_{p}(x),$ is the exponent of p in the first nonzero term of every p-adic series that represents x. By convention, $v_{p}(0)=\infty ;$ that is, the valuation of zero is $\infty .$ This valuation is a discrete valuation. The restriction of this valuation to the rational numbers is the p-adic valuation of $\mathbb {Q} ,$ that is, the exponent v in the factorization of a rational number as ${\tfrac {n}{d}}p^{v},$ with both n and d coprime with p.

## Notation

There are several different conventions for writing p-adic expansions. So far this article has used a notation for p-adic expansions in which powers of p increase from right to left. With this right-to-left notation the 3-adic expansion of ${\tfrac {1}{5}},$ for example, is written as ${\frac {1}{5}}=\dots 121012102_{3}.$

When performing arithmetic in this notation, digits are carried to the left. It is also possible to write p-adic expansions so that the powers of p increase from left to right, and digits are carried to the right. With this left-to-right notation the 3-adic expansion of ${\tfrac {1}{5}}$ is ${\frac {1}{5}}=2.01210121\dots _{3}{\mbox{ or }}{\frac {1}{15}}=20.1210121\dots _{3}.$

p-adic expansions may be written with other sets of digits instead of {0, 1, ..., *p* − 1}. For example, the 3-adic expansion of ${\tfrac {1}{5}}$ can be written using balanced ternary digits {1, 0, 1}, with 1 representing negative one, as ${\frac {1}{5}}=\dots {\underline {1}}11{\underline {11}}11{\underline {11}}11{\underline {1}}_{\text{3}}.$

In fact any set of p integers which are in distinct residue classes modulo p may be used as p-adic digits. In number theory, Teichmüller representatives are sometimes used as digits.

**Quote notation** is a variant of the p-adic representation of rational numbers that was proposed in 1979 by Eric Hehner and Nigel Horspool for implementing on computers the (exact) arithmetic with these numbers. It can be used as a compact way to represent rational numbers, which have an infinite periodic sequence of digits. In this notation, a quote mark (') is used to separate the repeating part from the nonrepeating part. ${\frac {1}{5}}=1210\,'2_{3}$

## *p*-adic expansion of rational numbers

The decimal expansion of a positive rational number r is its representation as a series $r=\sum _{i=k}^{\infty }a_{i}10^{-i},$ where k is an integer and each $a_{i}$ is also an integer such that $0\leq a_{i}<10.$ This expansion can be computed by long division of the numerator by the denominator, which is itself based on the following theorem: If $r={\tfrac {n}{d}}$ is a rational number such that $0\leq r<1,$ there is an integer a such that $0\leq a<10,$ and $10r=a+r',$ with $0\leq r'<1.$ The decimal expansion is obtained by repeatedly applying this result to the remainder $r'$ which in the iteration assumes the role of the original rational number r .

The p-*adic expansion* of a rational number can be computed similarly, but with a different division step. Suppose that $r={\tfrac {n}{d}}$ is a rational number with nonnegative valuation (that is, d is not divisible by p). The division step consists of writing $r=a+p\,r'$ where a is an integer such that $0\leq a<p,$ and $r'$ has nonnegative valuation.

The integer a can be computed as a modular multiplicative inverse: $a=nd^{-1}\operatorname {mod} p$ . Because of this, writing r in this way is always possible, and such a representation is unique.

The p-adic expansion of a rational number is eventually periodic. Conversely, a series ${\textstyle \sum _{i=k}^{\infty }a_{i}p^{i},}$ with $0\leq a_{i}<p$ converges (for the p-adic absolute value) to a rational number if and only if it is eventually periodic; in this case, the series is the p-adic expansion of that rational number. The proof is similar to that of the similar result for repeating decimals.

### Example

Let us compute the 5-adic expansion of ${\tfrac {1}{3}}.$ We can write this number as ${\tfrac {1}{3}}=2+5\cdot {\tfrac {-1}{3}}$ . Thus we use $a=2$ for the first step. ${\frac {1}{3}}=2+5^{1}\cdot \left({\frac {-1}{3}}\right)$ For the next step, we can write the "remainder" ${\tfrac {-1}{3}}$ as ${\tfrac {-1}{3}}=3+5\cdot {\tfrac {-2}{3}}$ . Thus we use $a=3$ . ${\frac {1}{3}}=2+3\cdot 5^{1}+5^{2}\cdot \left({\frac {-2}{3}}\right)$ We can write the "remainder" ${\tfrac {-2}{3}}$ as ${\tfrac {-2}{3}}=1+5\cdot {\tfrac {-1}{3}}$ . Thus we use $a=1$ . ${\frac {1}{3}}=2+3\cdot 5^{1}+1\cdot 5^{2}+5^{3}\cdot \left({\frac {-1}{3}}\right)$ Notice that we obtain the "remainder" ${\tfrac {-1}{3}}$ again, which means the digits can only repeat from this point on. ${\frac {1}{3}}=2+3\cdot 5^{1}+1\cdot 5^{2}+3\cdot 5^{3}+1\cdot 5^{4}+3\cdot 5^{5}+1\cdot 5^{6}+\cdots$ In the standard 5-adic notation, we can write this as ${\frac {1}{3}}=\ldots 1313132_{5}$ with the ellipsis $\ldots$ on the left hand side.

## *p*-adic integers

The **p-adic integers** are the p-adic numbers with a nonnegative valuation.

A p -adic integer can be represented as a sequence $x=(x_{1}\operatorname {mod} p,~x_{2}\operatorname {mod} p^{2},~x_{3}\operatorname {mod} p^{3},~\ldots )$ of residues $x_{e}$ mod $p^{e}$ for each integer e , satisfying the compatibility relations $x_{i}\equiv x_{j}~(\operatorname {mod} p^{i})$ for $i<j$ .

Every integer is a p -adic integer (including zero, since $0<\infty$ ). The rational numbers of the form ${\textstyle {\tfrac {n}{d}}p^{k}}$ with d coprime with p and $k\geq 0$ are also p -adic integers (for the reason that d has an inverse mod $p^{e}$ for every e ).

The p-adic integers form a commutative ring, denoted $\mathbb {Z} _{p}$ or $\mathbf {Z} _{p}$ , that has the following properties.

- It is an integral domain, since it is a subring of a field, or since the first term of the series representation of the product of two non zero p-adic series is the product of their first terms.
- The units (invertible elements) of $\mathbb {Z} _{p}$ are the p-adic numbers of valuation zero.
- It is a principal ideal domain, such that each ideal is generated by a power of p.
- It is a local ring of Krull dimension one, since its only prime ideals are the zero ideal and the ideal generated by p, the unique maximal ideal.
- It is a discrete valuation ring, since this results from the preceding properties.
- It is the completion of the local ring $\mathbb {Z} _{(p)}={\bigl \{}{\tfrac {n}{d}}\mathbin {\big |} n,d\in \mathbb {Z} ,\,d\not \in p\mathbb {Z} {\bigr \}},$ which is the localization of $\mathbb {Z}$ at the prime ideal $p\mathbb {Z} .$

The last property provides a definition of the p-adic numbers that is equivalent to the above one: the field of the p-adic numbers is the field of fractions of the completion of the localization of the integers at the prime ideal generated by p.

## Topological properties

The p-adic valuation allows defining an absolute value on p-adic numbers: the p-adic absolute value of a nonzero p-adic number x is $|x|_{p}=p^{-v_{p}(x)},$ where $v_{p}(x)$ is the p-adic valuation of x. The p-adic absolute value of 0 is $|0|_{p}=0.$ This is an absolute value that satisfies the strong triangle inequality since, for every x and y:

- $|x|_{p}=0$ if and only if $x=0;$
- $|x|_{p}\cdot |y|_{p}=|xy|_{p};$
- $|x+y|_{p}\leq \max\{|x|_{p},|y|_{p}\}\leq |x|_{p}+|y|_{p}.$

Moreover, if $|x|_{p}\neq |y|_{p},$ then $|x+y|_{p}=\max {\bigl (}|x|_{p},|y|_{p}{\bigr )}.$

This makes the p-adic numbers a metric space, and even an ultrametric space, with the p-adic distance defined by $d_{p}(x,y)=|x-y|_{p}.$

As a metric space, the p-adic numbers form the completion of the rational numbers equipped with the p-adic absolute value. This provides another way for defining the p-adic numbers.

As the metric is defined from a discrete valuation, every open ball is also closed. More precisely, the open ball $B_{r}(x)=\{y\mid d_{p}(x,y)<r\}$ equals the closed ball $\textstyle B_{p^{-v}}[x]=\{y\mid d_{p}(x,y)\leq p^{-v}\},$ where v is the least integer such that $\textstyle p^{-v}<r.$ Similarly, $\textstyle B_{r}[x]=B_{p^{-w}}(x),$ where w is the greatest integer such that $\textstyle p^{-w}>r.$

This implies that the p-adic numbers $\mathbb {Q} _{p}$ form a locally compact space (locally compact field), and the p-adic integers $\mathbb {Z} _{p}$ —that is, the ball $B_{1}[0]=B_{p}(0)$ —form a compact space.

The space of 2-adic integers $\mathbb {Z} _{2}$ is homeomorphic to the Cantor set ${\mathcal {C}}$ . This can be seen by considering the continuous 1-to-1 mapping $\psi :\mathbb {Z} _{2}\to {\mathcal {C}}$ defined by $\psi :~a_{0}+a_{1}2+a_{2}2^{2}+a_{3}2^{3}+\cdots ~\longmapsto ~{\frac {2a_{0}}{3}}+{\frac {2a_{1}}{3^{2}}}+{\frac {2a_{2}}{3^{3}}}+{\frac {2a_{3}}{3^{4}}}+\cdots$ Moreover, for any p, $\mathbb {Z} _{p}$ is homeomorphic to $\mathbb {Z} _{2}$ , and therefore also homeomorphic to the Cantor set.

The Pontryagin dual of the group of p-adic integers is the Prüfer p-group $\mathbb {Z} (p^{\infty })$ , and the Pontryagin dual of the Prüfer p-group is the group of p-adic integers.

## Modular properties

The quotient ring $\mathbb {Z} _{p}/p^{n}\mathbb {Z} _{p}$ may be identified with the ring $\mathbb {Z} /p^{n}\mathbb {Z}$ of the integers modulo $p^{n}.$ This can be shown by remarking that every p-adic integer, represented by its normalized p-adic series, is congruent modulo $p^{n}$ with its partial sum ${\textstyle \sum _{i=0}^{n-1}a_{i}p^{i},}$ whose value is an integer in the interval $[0,p^{n}-1].$ A straightforward verification shows that this defines a ring isomorphism from $\mathbb {Z} _{p}/p^{n}\mathbb {Z} _{p}$ to $\mathbb {Z} /p^{n}\mathbb {Z} .$

The inverse limit of the rings $\mathbb {Z} _{p}/p^{n}\mathbb {Z} _{p}$ is defined as the ring formed by the sequences $a_{0},a_{1},\ldots$ such that $a_{i}\in \mathbb {Z} /p^{i}\mathbb {Z}$ and ${\textstyle a_{i}\equiv a_{i+1}{\pmod {p^{i}}}}$ for every i.

The mapping that maps a normalized p-adic series to the sequence of its partial sums is a ring isomorphism from $\mathbb {Z} _{p}$ to the inverse limit of the $\mathbb {Z} _{p}/p^{n}\mathbb {Z} _{p}.$ This provides another way for defining p-adic integers (up to an isomorphism).

This definition of p-adic integers is specially useful for practical computations, as allowing building p-adic integers by successive approximations.

For example, for computing the p-adic (multiplicative) inverse of an integer, one can use Newton's method, starting from the inverse modulo p; then, each Newton step computes the inverse modulo ${\textstyle p^{n^{2}}}$ from the inverse modulo ${\textstyle p^{n}.}$

The same method can be used for computing the p-adic square root of an integer that is a quadratic residue modulo p. This seems to be the fastest known method for testing whether a large integer is a square: it suffices to test whether the given integer is the square of the value found in $\mathbb {Z} _{p}/p^{n}\mathbb {Z} _{p}$ . Applying Newton's method to find the square root requires ${\textstyle p^{n}}$ to be larger than twice the given integer, which is quickly satisfied.

Hensel lifting is a similar method that allows to "lift" the factorization modulo p of a polynomial with integer coefficients to a factorization modulo ${\textstyle p^{n}}$ for large values of n. This is commonly used by polynomial factorization algorithms.

## Cardinality

Both $\mathbb {Z} _{p}$ and $\mathbb {Q} _{p}$ are uncountable and have the cardinality of the continuum. For $\mathbb {Z} _{p},$ this results from the p-adic representation, which defines a bijection of $\mathbb {Z} _{p}$ on the power set $\{0,\ldots ,p-1\}^{\mathbb {N} }.$ For $\mathbb {Q} _{p}$ this results from its expression as a countably infinite union of copies of $\mathbb {Z} _{p}$ : $\mathbb {Q} _{p}=\bigcup _{i=0}^{\infty }{\frac {1}{p^{i}}}\mathbb {Z} _{p}.$

## Algebraic closure

The field $\mathbb {Q} _{p}$ contains $\mathbb {Q}$ and is a field of characteristic 0.

Because 0 can be written as sum of squares, $\mathbb {Q} _{p}$ cannot be turned into an ordered field.

The field of real numbers $\mathbb {R}$ has only a single proper algebraic extension: the complex numbers $\mathbb {C}$ . In other words, this quadratic extension is already algebraically closed. By contrast, the algebraic closure of $\mathbb {Q} _{p}$ , denoted ${\overline {\mathbb {Q} _{p}}},$ has infinite degree, that is, $\mathbb {Q} _{p}$ has infinitely many inequivalent algebraic extensions. Also contrasting the case of real numbers, although there is a unique extension of the p-adic valuation to ${\overline {\mathbb {Q} _{p}}},$ the latter is not (metrically) complete.

Its (metric) completion is denoted $\mathbb {C} _{p}$ or $\Omega _{p}$ , and sometimes called the **complex p-adic numbers** by analogy to the complex numbers. The field $\mathbb {C} _{p}$ is algebraically closed. However, unlike $\mathbb {C}$ , this field is not locally compact.

The fields $\mathbb {C} _{p}$ and $\mathbb {C}$ are isomorphic, so we may regard $\mathbb {C} _{p}$ as $\mathbb {C}$ endowed with an exotic metric. The proof of existence of such a field isomorphism relies on the axiom of choice, and does not provide an explicit example of such an isomorphism (that is, it is not constructive).

If K is any finite Galois extension of $\mathbb {Q} _{p},$ the Galois group $\operatorname {Gal} \left(K/\mathbb {Q} _{p}\right)$ is solvable. Thus, the absolute Galois group ${\operatorname {Gal} }{\bigl (}\,{\overline {\mathbb {Q} _{p}}}/\mathbb {Q} _{p}{\bigr )}$ is prosolvable.

## Multiplicative group

The unit group $\mathbb {Z} _{p}^{\times }$ is contained in the multiplicative group $\mathbb {Q} _{p}^{\times }=\mathbb {Q} _{p}-\{0\}$ . They have the same torsion subgroup (subgroup of elements of finite order). Hensel's lemma implies that the torsion subgroup of $\mathbb {Z} _{p}^{\times }$ maps surjectively to $\mathbb {F} _{p}^{\times }$ . The kernel is $\{1\}$ when $p>2$ and $\{\pm 1\}$ when $p=2$ . In particular, the torsion subgroup of $\mathbb {Q} _{p}^{\times }$ is cyclic of order $p-1$ when $p>2$ , and equals $\{\pm 1\}$ when $p=2$ . Therefore, for *n* > 2, the field $\mathbb {Q} _{p}$ contains the nth cyclotomic field if and only if *n* | *p* − 1.

Given a natural number k, let $\mathbb {Q} _{p}^{\times k}$ be the group of *k*th powers of elements of $\mathbb {Q} _{p}^{\times }$ ; then the index $(\mathbb {Q} _{p}^{\times }:\mathbb {Q} _{p}^{\times k})$ is finite.

## Local–global principle

Helmut Hasse's local–global principle is said to hold for an equation if it can be solved over the rational numbers if and only if it can be solved over the real numbers and over the p-adic numbers for every prime p. This principle holds, for example, for equations given by quadratic forms, but fails for higher polynomials in several indeterminates.

## Rational arithmetic with Hensel lifting

## Applications

The *p*-adic numbers have appeared in several fields of mathematics as well as physics.

### Analysis

Similar to the more classical fields of real and complex analysis, which deal, respectively, with functions on the real and complex numbers, ***p*-adic analysis** studies functions on *p*-adic numbers. The theory of complex-valued numerical functions on the *p*-adic numbers is part of the theory of locally compact groups (abstract harmonic analysis). The usual meaning taken for *p*-adic analysis is the theory of *p*-adic-valued functions on spaces of interest.

Applications of *p*-adic analysis have mainly been in number theory, where it has a significant role in diophantine geometry and diophantine approximation. Some applications have required the development of *p*-adic functional analysis and spectral theory. In many ways *p*-adic analysis is less subtle than classical analysis, since the ultrametric inequality means, for example, that convergence of infinite series of *p*-adic numbers is much simpler. Topological vector spaces over *p*-adic fields show distinctive features; for example aspects relating to convexity and the Hahn–Banach theorem are different.

Two important concepts from *p*-adic analysis are Mahler's theorem, which characterizes every continuous *p*-adic function in terms of polynomials, and Volkenborn integral, which provides a method of integration for *p*-adic functions.

### Hodge theory

***p*-adic Hodge theory** is a theory that provides a way to classify and study *p*-adic Galois representations of characteristic 0 local fields with residual characteristic *p* (such as **Q***p*). The theory has its beginnings in Jean-Pierre Serre and John Tate's study of Tate modules of abelian varieties and the notion of Hodge–Tate representation. Hodge–Tate representations are related to certain decompositions of *p*-adic cohomology theories analogous to the Hodge decomposition, hence the name *p*-adic Hodge theory. Further developments were inspired by properties of *p*-adic Galois representations arising from the étale cohomology of varieties. Jean-Marc Fontaine introduced many of the basic concepts of the field.

### Teichmüller theory

***p*-adic Teichmüller theory** describes the "uniformization" of *p*-adic curves and their moduli, generalizing the usual Teichmüller theory that describes the uniformization of Riemann surfaces and their moduli. It was introduced and developed by Shinichi Mochizuki.

### Quantum physics

***p*-adic quantum mechanics** is a collection of related research efforts in quantum physics that replace real numbers with *p*-adic numbers. Historically, this research was inspired by the discovery that the Veneziano amplitude of the open bosonic string, which is calculated using an integral over the real numbers, can be generalized to the *p*-adic numbers. This observation initiated the study of ***p*-adic string theory**.

The reals and the p-adic numbers are the completions of the rationals; it is also possible to complete other fields, for instance general algebraic number fields, in an analogous way. This will be described now.

Suppose *D* is a Dedekind domain and *E* is its field of fractions. Pick a non-zero prime ideal *P* of *D*. If *x* is a non-zero element of *E*, then *xD* is a fractional ideal and can be uniquely factored as a product of positive and negative powers of non-zero prime ideals of *D*. Therefore, writing ord*P*(*x*) for the exponent of *P* in this factorization gives a well-defined discrete valuation, and for any choice of number *c* greater than 1 we can set $|x|_{P}=c^{-\!\operatorname {ord} _{P}(x)}.$ Completing with respect to this absolute value |⋅|*P* yields a field *E**P*, the proper generalization of the field of *p*-adic numbers to this setting. The choice of *c* does not change the completion (different choices yield the same concept of Cauchy sequence, so the same completion). It is convenient, when the residue field *D*/*P* is finite, to take for *c* the size of *D*/*P*.

For example, when *E* is a number field and *D* is its ring of integers, Ostrowski's theorem says that every non-trivial non-Archimedean absolute value on *E* arises as some |⋅|*P*. The remaining non-trivial absolute values on *E* arise from the different embeddings of *E* into the real or complex numbers. (In fact, the non-Archimedean absolute values can be considered as simply the different embeddings of *E* into the fields **C***p*, thus putting the description of all the non-trivial absolute values of a number field on a common footing.)

Often, one needs to simultaneously keep track of all the above-mentioned completions when *E* is a number field (or more generally a global field), which are seen as encoding "local" information. This is accomplished by adele rings and idele groups.

*p*-adic integers can be extended to *p*-adic solenoids $\mathbb {T} _{p}$ . There is a map from $\mathbb {T} _{p}$ to the circle group whose fibers are the *p*-adic integers $\mathbb {Z} _{p}$ , in analogy to how there is a map from $\mathbb {R}$ to the circle whose fibers are $\mathbb {Z}$ .

The *p*-adic integers can also be extended to profinite integers ${\widehat {\mathbb {Z} }}$ , which can be understood as the direct product of rings ${\widehat {\mathbb {Z} }}=\prod _{p}\mathbb {Z} _{p}.$ Unlike the *p*-adic integers which only generalize the modulo over prime powers *p**k*, the profinite integers generalizes the modulo over *all* natural numbers *n*. The Chinese remainder theorem likewise implies a structure of $\mathbb {Z} _{n}$ for composite bases: for any *n* which has at least two distinct prime factors, the *n*-adic integer ring $\mathbb {Z} _{n}$ is isomorphic to $\prod _{p|n}\mathbb {Z} _{p}$ .
