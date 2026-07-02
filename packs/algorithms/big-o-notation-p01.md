---
title: "Big O notation (part 1/2)"
source: https://en.wikipedia.org/wiki/Big_O_notation
domain: algorithms
license: CC-BY-SA-4.0
tags: algorithm, sorting, complexity, big-o, dynamic programming
fetched: 2026-07-02
part: 1/2
---

# Big *O* notation

**Big *O* notation** is a mathematical notation that describes the approximate size of a function on a domain. Big O is a member of a family of notations invented by the German mathematicians Paul Bachmann and Edmund Landau and expanded by others, collectively called **Bachmann–Landau notation**. The letter O stands for *Ordnung*, that is, the order of approximation.

In computer science, big O notation is used to classify algorithms by how their run time or space requirements grow with the input. In analytic number theory, big O notation expresses bounds on the growth of an arithmetical function, as for the remainder term in the prime number theorem. In mathematical analysis, including calculus, Big O notation bounds the error when truncating a power series and expresses the quality of approximation of a real or complex valued function by a simpler function.

Often, big O notation characterizes functions according to their growth rates as the variable becomes large: different functions with the same asymptotic growth rate may be represented using the same O notation. The letter O is used because the growth rate of a function is also referred to as the **order of the function**. A description of a function in terms of big O notation only provides an upper bound on the growth rate of the function.

Associated with big O notation are several related notations, using the symbols o {\displaystyle o} ({\displaystyle o}), ∼ {\displaystyle \sim } ({\displaystyle \sim }), Ω {\displaystyle \Omega } ({\displaystyle \Omega }), ≪ {\displaystyle \ll } ({\displaystyle \ll }), ≫ {\displaystyle \gg } ({\displaystyle \gg }), ≍ {\displaystyle \asymp } ({\displaystyle \asymp }), ω {\displaystyle \omega } ({\displaystyle \omega }), and Θ {\displaystyle \Theta } ({\displaystyle \Theta }) to describe other kinds of bounds on growth rates.

Bachmann proposed the notation in 1894 and Landau extended it in 1909. An earlier notation was proposed by Paul du Bois-Reymond in 1870.


## Formal definition

Let f , {\textstyle f,} ({\textstyle f,}) the function to be estimated, be either a real or complex valued function defined on a domain D , {\textstyle D,} ({\textstyle D,}) and let g , {\textstyle g,} ({\textstyle g,}) the comparison function, be a non-negative real valued function defined on the same set D . {\textstyle D.} ({\textstyle D.}) Common choices for the domain are intervals of real numbers, bounded or unbounded, the set of positive integers, the set of complex numbers and tuples of real/complex numbers. With the domain written explicitly or understood implicitly, one writes

f

(

x

)

=

O

(

g

(

x

)

)

{\displaystyle f(x)=O{\bigl (}g(x){\bigr )}\ }

which is read as  " f ( x ) {\textstyle f(x)} ({\textstyle f(x)}) is big O {\textstyle O} ({\textstyle O}) of g ( x ) {\textstyle g(x)} ({\textstyle g(x)})"  if there exists a positive real number M {\textstyle M} ({\textstyle M}) such that

|

f

(

x

)

|

≤

M

g

(

x

)

f

o

r

a

l

l

x

∈

D

.

{\displaystyle \left|f(x)\right|\leq M\ g(x)\qquad ~{\mathsf {\ for\ all\ }}~\quad x\in D.}

If g ( x ) > 0 {\displaystyle g(x)>0} ({\displaystyle g(x)>0}) (i.e. g is also never zero) throughout the domain D , {\displaystyle D,} ({\displaystyle D,}) an equivalent definition is that the ratio f ( x ) g ( x ) {\textstyle {\frac {f(x)}{g(x)}}} ({\textstyle {\frac {f(x)}{g(x)}}}) is *bounded*, i.e. there is a positive real number M {\displaystyle M} ({\displaystyle M}) so that | f ( x ) g ( x ) | ≤ M {\textstyle {\Big |}{\frac {f(x)}{g(x)}}{\Big |}\leq M} ({\textstyle {\Big |}{\frac {f(x)}{g(x)}}{\Big |}\leq M}) for all x ∈ D . {\displaystyle x\in D.} ({\displaystyle x\in D.}) These encompass all the uses of big O {\textstyle O} ({\textstyle O}) in computer science and mathematics, including its use where the domain is finite, infinite, real, complex, single variate, or multivariate. In most applications, one chooses the function g ( x ) {\displaystyle g(x)} ({\displaystyle g(x)}) appearing within the argument of O ( ⋅ ) {\textstyle O{\bigl (}\cdot {\bigr )}} ({\textstyle O{\bigl (}\cdot {\bigr )}}) to be as simple a form as possible, omitting constant factors and lower order terms. The number M {\textstyle M} ({\textstyle M}) is called the *implied constant* because it is normally not specified. When using big O {\textstyle O} ({\textstyle O}) notation, what matters is that some finite M {\displaystyle M} ({\displaystyle M}) exists, not its specific value. This simplifies the presentation of many analytic inequalities.

For functions defined on positive real numbers or positive integers, a more restrictive and somewhat conflicting definition is still in common use, especially in computer science. When restricted to functions which are eventually positive, the notation

f

(

x

)

=

O

(

g

(

x

)

)

a

s

x

→

∞

{\displaystyle f(x)=O{\bigl (}g(x){\bigr )}\qquad ~{\mathsf {as}}\quad x\to \infty }

means that for some real number a , {\textstyle a,} ({\textstyle a,}) f ( x ) = O ( g ( x ) ) {\textstyle f(x)=O{\bigl (}g(x){\bigr )}} ({\textstyle f(x)=O{\bigl (}g(x){\bigr )}}) in the domain [ a , ∞ ) . {\textstyle \left[a,\infty \right).} ({\textstyle \left[a,\infty \right).}) Here, the expression x → ∞ {\textstyle x\to \infty } ({\textstyle x\to \infty }) does not indicate a limit, but the notion that the inequality holds for *large enough* x . {\textstyle x.} ({\textstyle x.}) The expression x → ∞ {\textstyle x\to \infty } ({\textstyle x\to \infty }) often is omitted.

Similarly, for a real number a , {\textstyle a,} ({\textstyle a,}) the notation

f

(

x

)

=

O

(

g

(

x

)

)

as

x

→

a

{\displaystyle f(x)=O{\bigl (}g(x){\bigr )}\qquad ~{\text{ as }}\ x\to a}

means that for some constant c > 0 , {\textstyle c>0,} ({\textstyle c>0,}) f ( x ) = O ( g ( x ) ) {\textstyle f(x)=O{\bigl (}g(x){\bigr )}} ({\textstyle f(x)=O{\bigl (}g(x){\bigr )}}) on the interval [ a − c , a + c ] ; {\displaystyle \left[a-c,a+c\right];} ({\displaystyle \left[a-c,a+c\right];}) that is, in a small neighborhood of a . {\displaystyle a.} ({\displaystyle a.}) In addition, the notation   f ( x ) = h ( x ) + O ( g ( x ) )   {\displaystyle \ f(x)=h(x)+O{\bigl (}g(x){\bigr )}\ } ({\displaystyle \ f(x)=h(x)+O{\bigl (}g(x){\bigr )}\ }) means f ( x ) − h ( x ) = O ( g ( x ) ) . {\textstyle f(x)-h(x)=O{\bigl (}g(x){\bigr )}.} ({\textstyle f(x)-h(x)=O{\bigl (}g(x){\bigr )}.}) More complicated expressions are also possible.

Despite the presence of the equal sign (=) as written, the expression f ( x ) = O ( g ( x ) ) {\textstyle f(x)=O{\bigl (}g(x){\bigr )}} ({\textstyle f(x)=O{\bigl (}g(x){\bigr )}}) does not refer to an equality, but rather to an inequality relating f {\textstyle f} ({\textstyle f}) and g . {\textstyle g.} ({\textstyle g.})

In the 1930s, the Russian number theorist I.M. Vinogradov introduced the notation ≪ , {\displaystyle \ll ,} ({\displaystyle \ll ,}) which has been increasingly used in number theory and other branches of mathematics, as an alternative to the O {\textstyle O} ({\textstyle O}) notation. We have

f

≪

g

⟺

f

=

O

(

g

)

.

{\displaystyle \ f\ll g\iff f=O{\bigl (}g{\bigr )}.}

Frequently both notations are used in the same work.

### Set version of big O

In computer science it is common to define big O {\textstyle O} ({\textstyle O}) as also defining a set of functions. With the positive (or non-negative) function g ( x ) {\displaystyle g(x)} ({\displaystyle g(x)}) specified, one interprets O ( g ( x ) ) {\textstyle O{\bigl (}g(x){\bigr )}} ({\textstyle O{\bigl (}g(x){\bigr )}}) as representing the *set* of all functions f ~ {\textstyle {\tilde {f}}} ({\textstyle {\tilde {f}}}) that satisfy f ~ ( x ) = O ( g ( x ) ) . {\textstyle {\tilde {f}}(x)=O{\bigl (}g(x){\bigr )}.} ({\textstyle {\tilde {f}}(x)=O{\bigl (}g(x){\bigr )}.}) One can then equivalently write f ( x ) ∈ O ( g ( x ) ) , {\textstyle f(x)\in O{\bigl (}g(x){\bigr )},} ({\textstyle f(x)\in O{\bigl (}g(x){\bigr )},}) read as "the function   f ( x )   {\textstyle \ f(x)\ } ({\textstyle \ f(x)\ }) is among the set of all functions of order at most g ( x ) . {\textstyle g(x).} ({\textstyle g(x).})"


## Examples with an infinite domain

In typical usage the O {\displaystyle O} ({\displaystyle O}) notation is applied to an infinite interval of real numbers [ a , ∞ ) {\displaystyle [a,\infty )} ({\displaystyle [a,\infty )}) and captures the behavior of the function for very large x {\displaystyle x} ({\displaystyle x}). In this setting, the contribution of the terms that grow "most quickly" will eventually make the other ones irrelevant. As a result, the following simplification rules can be applied:

- If f ( x ) {\displaystyle f(x)} ({\displaystyle f(x)}) is a sum of several terms, if there is one with largest growth rate, it can be kept, and all others omitted.
- If f ( x ) {\displaystyle f(x)} ({\displaystyle f(x)}) is a product of several factors, any constants (factors in the product that do not depend on x {\displaystyle x} ({\displaystyle x})) can be omitted.

For example, let f ( x ) = 6 x 4 − 2 x 3 + 5 {\displaystyle f(x)=6x^{4}-2x^{3}+5} ({\displaystyle f(x)=6x^{4}-2x^{3}+5}), and suppose we wish to simplify this function, using O {\displaystyle O} ({\displaystyle O}) notation, to describe its growth rate for large x {\displaystyle x} ({\displaystyle x}). This function is the sum of three terms: 6 x 4 {\displaystyle 6x^{4}} ({\displaystyle 6x^{4}}), − 2 x 3 {\displaystyle -2x^{3}} ({\displaystyle -2x^{3}}), and 5 {\displaystyle 5} ({\displaystyle 5}). Of these three terms, the one with the highest growth rate is the one with the largest exponent as a function of x {\displaystyle x} ({\displaystyle x}), namely 6 x 4 {\displaystyle 6x^{4}} ({\displaystyle 6x^{4}}). Now one may apply the second rule: 6 x 4 {\displaystyle 6x^{4}} ({\displaystyle 6x^{4}})is a product of 6 {\displaystyle 6} ({\displaystyle 6}) and x 4 {\displaystyle x^{4}} ({\displaystyle x^{4}}) in which the first factor does not depend on x {\displaystyle x} ({\displaystyle x}). Omitting this factor results in the simplified form x 4 {\displaystyle x^{4}} ({\displaystyle x^{4}}). Thus, we say that f ( x ) {\displaystyle f(x)} ({\displaystyle f(x)}) is a "big O" of x 4 {\displaystyle x^{4}} ({\displaystyle x^{4}}). Mathematically, we can write f ( x ) = O ( x 4 ) {\displaystyle f(x)=O(x^{4})} ({\displaystyle f(x)=O(x^{4})}) for all x ≥ 1 {\displaystyle x\geq 1} ({\displaystyle x\geq 1}). One may confirm this calculation using the formal definition: let f ( x ) = 6 x 4 − 2 x 3 + 5 {\displaystyle f(x)=6x^{4}-2x^{3}+5} ({\displaystyle f(x)=6x^{4}-2x^{3}+5}) and g ( x ) = x 4 {\displaystyle g(x)=x^{4}} ({\displaystyle g(x)=x^{4}}). Applying the formal definition from above, the statement that f ( x ) = O ( x 4 ) {\displaystyle f(x)=O(x^{4})} ({\displaystyle f(x)=O(x^{4})}) is equivalent to its expansion, | f ( x ) | ≤ M x 4 {\displaystyle |f(x)|\leq Mx^{4}} ({\displaystyle |f(x)|\leq Mx^{4}}) for some suitable choice of a positive real number M {\displaystyle M} ({\displaystyle M}) and for all x ≥ 1 {\displaystyle x\geq 1} ({\displaystyle x\geq 1}). To prove this, let M = 13 {\displaystyle M=13} ({\displaystyle M=13}). Then, for all x ≥ 1 {\displaystyle x\geq 1} ({\displaystyle x\geq 1}): | 6 x 4 − 2 x 3 + 5 | ≤ 6 x 4 + | − 2 x 3 | + 5 ≤ 6 x 4 + 2 x 4 + 5 x 4 = 13 x 4 {\displaystyle {\begin{aligned}|6x^{4}-2x^{3}+5|&\leq 6x^{4}+|-2x^{3}|+5\\&\leq 6x^{4}+2x^{4}+5x^{4}\\&=13x^{4}\end{aligned}}} ({\displaystyle {\begin{aligned}|6x^{4}-2x^{3}+5|&\leq 6x^{4}+|-2x^{3}|+5\\&\leq 6x^{4}+2x^{4}+5x^{4}\\&=13x^{4}\end{aligned}}}) so | 6 x 4 − 2 x 3 + 5 | ≤ 13 x 4 . {\displaystyle |6x^{4}-2x^{3}+5|\leq 13x^{4}.} ({\displaystyle |6x^{4}-2x^{3}+5|\leq 13x^{4}.}) While it is also true, by the same argument, that f ( x ) = O ( x 10 ) {\displaystyle f(x)=O(x^{10})} ({\displaystyle f(x)=O(x^{10})}), this is a less precise approximation of the function f {\displaystyle f} ({\displaystyle f}). On the other hand, the statement f ( x ) = O ( x 3 ) {\displaystyle f(x)=O(x^{3})} ({\displaystyle f(x)=O(x^{3})}) is false, because the term 6 x 4 {\displaystyle 6x^{4}} ({\displaystyle 6x^{4}}) causes f ( x ) / x 3 {\displaystyle f(x)/x^{3}} ({\displaystyle f(x)/x^{3}}) to be unbounded.

When a function T ( n ) {\displaystyle T(n)} ({\displaystyle T(n)}) describes the number of steps required in an algorithm with input n {\displaystyle n} ({\displaystyle n}), an expression such as T ( n ) = O ( n 2 ) {\displaystyle T(n)=O(n^{2})} ({\displaystyle T(n)=O(n^{2})}) with the implied domain being the set of positive integers, may be interpreted as saying that the algorithm has *at most the order of n 2 {\displaystyle n^{2}} ({\displaystyle n^{2}})* time complexity.


## Example with a finite domain

Big O can also be used to describe the error term in an approximation to a mathematical function on a finite interval. The most significant terms are written explicitly, and then the least-significant terms are summarized in a single big O term. Consider, for example, the exponential series and two expressions of it that are valid when x {\displaystyle x} ({\displaystyle x}) is small: e x = 1 + x + x 2   2 ! + x 3   3 ! + x 4   4 ! + ⋯  for all finite  x = 1 + x + x 2   2 + O ( | x | 3 )  for all  | x | ≤ 1 = 1 + x + O ( x 2 )  for all  | x | ≤ 1. {\displaystyle {\begin{aligned}e^{x}&=1+x+{\frac {\;x^{2}\ }{2!}}+{\frac {\;x^{3}\ }{3!}}+{\frac {\;x^{4}\ }{4!}}+\dotsb &&{\text{ for all finite }}x\\[4pt]&=1+x+{\frac {\;x^{2}\ }{2}}+O(|x|^{3})&&{\text{ for all }}|x|\leq 1\\[4pt]&=1+x+O(x^{2})&&{\text{ for all }}|x|\leq 1.\end{aligned}}} ({\displaystyle {\begin{aligned}e^{x}&=1+x+{\frac {\;x^{2}\ }{2!}}+{\frac {\;x^{3}\ }{3!}}+{\frac {\;x^{4}\ }{4!}}+\dotsb &&{\text{ for all finite }}x\\[4pt]&=1+x+{\frac {\;x^{2}\ }{2}}+O(|x|^{3})&&{\text{ for all }}|x|\leq 1\\[4pt]&=1+x+O(x^{2})&&{\text{ for all }}|x|\leq 1.\end{aligned}}}) The middle expression (the line with " O ( | x 3 | ) {\displaystyle O(|x^{3}|)} ({\displaystyle O(|x^{3}|)})") means the absolute-value of the error   e x − ( 1 + x + x 2   2 )   {\displaystyle \ e^{x}-(1+x+{\frac {\;x^{2}\ }{2}})\ } ({\displaystyle \ e^{x}-(1+x+{\frac {\;x^{2}\ }{2}})\ }) is at most some constant times   | x 3 |   {\displaystyle ~|x^{3}|\ } ({\displaystyle ~|x^{3}|\ }) when   x   {\displaystyle \ x~} ({\displaystyle \ x~}) is small. This is an example of the use of Taylor's theorem.

The behavior of a given function may be very different on finite domains than on infinite domains, for example, ( x + 1 ) 8 = x 8 + O ( x 7 )  for  x ≥ 1 {\displaystyle (x+1)^{8}=x^{8}+O(x^{7})\quad {\text{ for }}x\geq 1} ({\displaystyle (x+1)^{8}=x^{8}+O(x^{7})\quad {\text{ for }}x\geq 1}) while ( x + 1 ) 8 = 1 + 8 x + O ( x 2 )  for  | x | ≤ 1. {\displaystyle (x+1)^{8}=1+8x+O(x^{2})\quad {\text{ for }}|x|\leq 1.} ({\displaystyle (x+1)^{8}=1+8x+O(x^{2})\quad {\text{ for }}|x|\leq 1.})


## Multivariate examples

x sin ⁡ y = O ( x )  for  x ≥ 1 , y  any real number {\displaystyle x\sin y=O(x)\quad {\text{ for }}x\geq 1,y{\text{ any real number}}} ({\displaystyle x\sin y=O(x)\quad {\text{ for }}x\geq 1,y{\text{ any real number}}})

3 a 2 + 7 a b + 2 b 2 + a + 3 b + 14 ≪ a 2 + b 2 ≪ a 2  for all  a ≥ b ≥ 1 {\displaystyle 3a^{2}+7ab+2b^{2}+a+3b+14\ll a^{2}+b^{2}\ll a^{2}\quad {\text{ for all }}a\geq b\geq 1} ({\displaystyle 3a^{2}+7ab+2b^{2}+a+3b+14\ll a^{2}+b^{2}\ll a^{2}\quad {\text{ for all }}a\geq b\geq 1})

x y x 2 + y 2 = O ( 1 )  for all real  x , y  that are not both  0 {\displaystyle {\frac {xy}{x^{2}+y^{2}}}=O(1)\quad {\text{ for all real }}x,y{\text{ that are not both }}0} ({\displaystyle {\frac {xy}{x^{2}+y^{2}}}=O(1)\quad {\text{ for all real }}x,y{\text{ that are not both }}0})

x i t = O ( 1 )  for  x ≠ 0 , t ∈ R . {\displaystyle x^{it}=O(1)\quad {\text{ for }}x\neq 0,t\in \mathbb {R} .} ({\displaystyle x^{it}=O(1)\quad {\text{ for }}x\neq 0,t\in \mathbb {R} .})

Here we have a complex variable function of two variables. In general, any bounded function is O ( 1 ) {\displaystyle O(1)} ({\displaystyle O(1)}).

( x + y ) 10 = O ( x 10 )  for  x ≥ 1 , − 2 ≤ y ≤ 2. {\displaystyle (x+y)^{10}=O(x^{10})\quad {\text{ for }}x\geq 1,-2\leq y\leq 2.} ({\displaystyle (x+y)^{10}=O(x^{10})\quad {\text{ for }}x\geq 1,-2\leq y\leq 2.})

The last example illustrates a mixing of finite and infinite domains on the different variables.

In all of these examples, the bound is uniform in both variables. Sometimes in a multivariate expression, one variable is more important than others, and one may express that the implied constant M {\displaystyle M} ({\displaystyle M}) depends on one or more of the variables using subscripts to the big O symbol or the ≪ {\displaystyle \ll } ({\displaystyle \ll }) symbol. For example, consider the expression

( 1 + x ) b = 1 + O b ( x )  for  0 ≤ x ≤ 1 , b  any real number. {\displaystyle (1+x)^{b}=1+O_{b}(x)\quad {\text{ for }}0\leq x\leq 1,b{\text{ any real number.}}} ({\displaystyle (1+x)^{b}=1+O_{b}(x)\quad {\text{ for }}0\leq x\leq 1,b{\text{ any real number.}}})

This means that for each real number b {\displaystyle b} ({\displaystyle b}), there is a constant M b {\displaystyle M_{b}} ({\displaystyle M_{b}}), *which depends on b {\displaystyle b} ({\displaystyle b})*, so that for all 0 ≤ x ≤ 1 {\displaystyle 0\leq x\leq 1} ({\displaystyle 0\leq x\leq 1}), | ( 1 + x ) b − 1 | ≤ M b ⋅ x . {\displaystyle |(1+x)^{b}-1|\leq M_{b}\cdot x.} ({\displaystyle |(1+x)^{b}-1|\leq M_{b}\cdot x.}) This particular statement follows from the general binomial theorem.

Another example, common in the theory of Taylor series, is e x = 1 + x + O r ( x 2 )  for all  | x | ≤ r , r  being any real number. {\displaystyle e^{x}=1+x+O_{r}(x^{2})\quad {\text{ for all }}|x|\leq r,r{\text{ being any real number.}}} ({\displaystyle e^{x}=1+x+O_{r}(x^{2})\quad {\text{ for all }}|x|\leq r,r{\text{ being any real number.}}}) Here the implied constant depends on the size of the domain.

The subscript convention applies to all of the other notations in this page.


## Properties

### Product

f

1

=

O

(

g

1

)

and

f

2

=

O

(

g

2

)

⇒

f

1

f

2

=

O

(

g

1

g

2

)

{\displaystyle f_{1}=O(g_{1}){\text{ and }}f_{2}=O(g_{2})\Rightarrow f_{1}f_{2}=O(g_{1}g_{2})}

f

⋅

O

(

g

)

=

O

(

|

f

|

g

)

{\displaystyle f\cdot O(g)=O(|f|g)}

### Sum

If f 1 = O ( g 1 ) {\displaystyle f_{1}=O(g_{1})} ({\displaystyle f_{1}=O(g_{1})}) and f 2 = O ( g 2 ) {\displaystyle f_{2}=O(g_{2})} ({\displaystyle f_{2}=O(g_{2})}) then f 1 + f 2 = O ( max ( g 1 , g 2 ) ) {\displaystyle f_{1}+f_{2}=O(\max(g_{1},g_{2}))} ({\displaystyle f_{1}+f_{2}=O(\max(g_{1},g_{2}))}). It follows that if f 1 = O ( g ) {\displaystyle f_{1}=O(g)} ({\displaystyle f_{1}=O(g)}) and f 2 = O ( g ) {\displaystyle f_{2}=O(g)} ({\displaystyle f_{2}=O(g)}) then f 1 + f 2 = O ( g ) {\displaystyle f_{1}+f_{2}=O(g)} ({\displaystyle f_{1}+f_{2}=O(g)}).

### Multiplication by a constant

Let k be a nonzero constant. Then O ( | k | ⋅ g ) = O ( g ) {\displaystyle O(|k|\cdot g)=O(g)} ({\displaystyle O(|k|\cdot g)=O(g)}). In other words, if f = O ( g ) {\displaystyle f=O(g)} ({\displaystyle f=O(g)}), then k ⋅ f = O ( g ) . {\displaystyle k\cdot f=O(g).} ({\displaystyle k\cdot f=O(g).})

### Transitive property

If f = O ( g ) {\displaystyle f=O(g)} ({\displaystyle f=O(g)}) and g = O ( h ) {\displaystyle g=O(h)} ({\displaystyle g=O(h)}) then f = O ( h ) {\displaystyle f=O(h)} ({\displaystyle f=O(h)}).

If the function f {\displaystyle f} ({\displaystyle f}) of a positive integer n {\displaystyle n} ({\displaystyle n}) can be written as a finite sum of other functions, then the fastest growing one determines the order of f ( n ) {\displaystyle f(n)} ({\displaystyle f(n)}). For example,

f

(

n

)

=

9

log

⁡

n

+

5

(

log

⁡

n

)

4

+

3

n

2

+

2

n

3

=

O

(

n

3

)

for

n

≥

1.

{\displaystyle f(n)=9\log n+5(\log n)^{4}+3n^{2}+2n^{3}=O(n^{3})\qquad {\text{for }}n\geq 1.}

Some general rules about growth *toward infinity*; the 2nd and 3rd property below can be proved rigorously using L'Hôpital's rule:

### Large powers dominate small powers

For b ≥ a {\displaystyle b\geq a} ({\displaystyle b\geq a}), then n a = O ( n b ) {\displaystyle n^{a}=O(n^{b})} ({\displaystyle n^{a}=O(n^{b})}) as n → ∞ {\displaystyle n\to \infty } ({\displaystyle n\to \infty }).

### Powers dominate logarithms

For any positive a , b , {\displaystyle a,b,} ({\displaystyle a,b,}) ( log ⁡ n ) a = O a , b ( n b ) , {\displaystyle (\log n)^{a}=O_{a,b}(n^{b}),} ({\displaystyle (\log n)^{a}=O_{a,b}(n^{b}),}) no matter how large a {\displaystyle a} ({\displaystyle a}) is and how small b {\displaystyle b} ({\displaystyle b}) is. Here, the implied constant depends on both a {\displaystyle a} ({\displaystyle a}) and b {\displaystyle b} ({\displaystyle b}).

### Exponentials dominate powers

For any positive a , b , {\displaystyle a,b,} ({\displaystyle a,b,}) n a = O a , b ( e b n ) , {\displaystyle n^{a}=O_{a,b}(e^{bn}),} ({\displaystyle n^{a}=O_{a,b}(e^{bn}),}) no matter how large a {\displaystyle a} ({\displaystyle a}) is and how small b {\displaystyle b} ({\displaystyle b}) is.

A function that grows faster than n c {\displaystyle n^{c}} ({\displaystyle n^{c}}) for any c {\displaystyle c} ({\displaystyle c}) is called *superpolynomial*. One that grows more slowly than any exponential function of the form c n {\displaystyle c^{n}} ({\displaystyle c^{n}}) with c > 1 {\displaystyle c>1} ({\displaystyle c>1}) is called *subexponential*. An algorithm can require time that is both superpolynomial and subexponential; examples of this include the fastest known algorithms for integer factorization and the function n log ⁡ n {\displaystyle n^{\log n}} ({\displaystyle n^{\log n}}).

We may ignore any powers of n {\displaystyle n} ({\displaystyle n}) inside of the logarithms. For any positive c {\displaystyle c} ({\displaystyle c}), the notation O ( log ⁡ n ) {\displaystyle O(\log n)} ({\displaystyle O(\log n)}) means exactly the same thing as O ( log ⁡ ( n c ) ) {\displaystyle O(\log(n^{c}))} ({\displaystyle O(\log(n^{c}))}), since log ⁡ ( n c ) = c log ⁡ n {\displaystyle \log(n^{c})=c\log n} ({\displaystyle \log(n^{c})=c\log n}). Similarly, logs with different constant bases are equivalent with respect to Big O notation. On the other hand, exponentials with different bases are not of the same order. For example, 2 n {\displaystyle 2^{n}} ({\displaystyle 2^{n}}) and 3 n {\displaystyle 3^{n}} ({\displaystyle 3^{n}}) are not of the same order.

### More complicated expressions

In more complicated usage, O ( ⋅ ) {\displaystyle O(\cdot )} ({\displaystyle O(\cdot )}) can appear in different places in an equation, even several times on each side. For example, the following are true for n {\displaystyle n} ({\displaystyle n}) a positive integer: ( n + 1 ) 2 = n 2 + O ( n ) , ( n + O ( n 1 / 2 ) ) ⋅ ( n + O ( log ⁡ n ) ) 2 = n 3 + O ( n 5 / 2 ) , n O ( 1 ) = O ( e n ) . {\displaystyle {\begin{aligned}(n+1)^{2}&=n^{2}+O(n),\\(n+O(n^{1/2}))\cdot (n+O(\log n))^{2}&=n^{3}+O(n^{5/2}),\\n^{O(1)}&=O(e^{n}).\end{aligned}}} ({\displaystyle {\begin{aligned}(n+1)^{2}&=n^{2}+O(n),\\(n+O(n^{1/2}))\cdot (n+O(\log n))^{2}&=n^{3}+O(n^{5/2}),\\n^{O(1)}&=O(e^{n}).\end{aligned}}}) The meaning of such statements is as follows: for *any* functions which satisfy each O ( ⋅ ) {\displaystyle O(\cdot )} ({\displaystyle O(\cdot )}) on the left side, there are *some* functions satisfying each O ( ⋅ ) {\displaystyle O(\cdot )} ({\displaystyle O(\cdot )}) on the right side, such that substituting all these functions into the equation makes the two sides equal. For example, the third equation above means: "For any function satisfying f ( n ) = O ( 1 ) {\displaystyle f(n)=O(1)} ({\displaystyle f(n)=O(1)}), there is some function g ( n ) = O ( e n ) {\displaystyle g(n)=O(e^{n})} ({\displaystyle g(n)=O(e^{n})}) such that n f ( n ) = g ( n ) {\displaystyle n^{f(n)}=g(n)} ({\displaystyle n^{f(n)}=g(n)})". The implied constant in the statement " g ( n ) = O ( e n ) {\displaystyle g(n)=O(e^{n})} ({\displaystyle g(n)=O(e^{n})})" may depend on the implied constant in the expression " f ( n ) = O ( 1 ) {\displaystyle f(n)=O(1)} ({\displaystyle f(n)=O(1)})".

Some further examples: f = O ( g ) ⇒ ∫ a b f = O ( ∫ a b g ) f ( x ) = g ( x ) + O ( 1 ) ⇒ e f ( x ) = O ( e g ( x ) ) ( 1 + O ( 1 / x ) ) O ( x ) = O ( 1 )  for  x > 0 sin ⁡ x = O ( | x | )  for all real  x . {\displaystyle {\begin{aligned}f=O(g)\;&\Rightarrow \;\int _{a}^{b}f=O{\bigg (}\int _{a}^{b}g{\bigg )}\\f(x)=g(x)+O(1)\;&\Rightarrow \;e^{f(x)}=O(e^{g(x)})\\(1+O(1/x))^{O(x)}&=O(1)\quad {\text{ for }}x>0\\\sin x&=O(|x|)\quad {\text{ for all real }}x.\end{aligned}}} ({\displaystyle {\begin{aligned}f=O(g)\;&\Rightarrow \;\int _{a}^{b}f=O{\bigg (}\int _{a}^{b}g{\bigg )}\\f(x)=g(x)+O(1)\;&\Rightarrow \;e^{f(x)}=O(e^{g(x)})\\(1+O(1/x))^{O(x)}&=O(1)\quad {\text{ for }}x>0\\\sin x&=O(|x|)\quad {\text{ for all real }}x.\end{aligned}}})

### Vinogradov's ≫ and Knuth's big Ω

When f , g {\displaystyle f,g} ({\displaystyle f,g}) are both positive functions, Vinogradov introduced the notation f ( x ) ≫ g ( x ) {\displaystyle f(x)\gg g(x)} ({\displaystyle f(x)\gg g(x)}), which means the same as g ( x ) = O ( f ( x ) ) {\displaystyle g(x)=O(f(x))} ({\displaystyle g(x)=O(f(x))}). Vinogradov's two notations enjoy visual symmetry, as for positive functions f , g {\displaystyle f,g} ({\displaystyle f,g}), we have f ( x ) ≪ g ( x ) ⟺ g ( x ) ≫ f ( x ) . {\displaystyle f(x)\ll g(x)\Longleftrightarrow g(x)\gg f(x).} ({\displaystyle f(x)\ll g(x)\Longleftrightarrow g(x)\gg f(x).})

In 1976, Donald Knuth defined

f

(

x

)

=

Ω

(

g

(

x

)

)

⟺

g

(

x

)

=

O

(

f

(

x

)

)

{\displaystyle f(x)=\Omega (g(x))\Longleftrightarrow g(x)=O(f(x))}

which has the same meaning as Vinogradov's f ( x ) ≫ g ( x ) {\displaystyle f(x)\gg g(x)} ({\displaystyle f(x)\gg g(x)}).

However, much earlier, Hardy and Littlewood had defined Ω {\displaystyle \Omega } ({\displaystyle \Omega }) differently, and their notation enjoys widespread use today in analytic number theory. Justifying his use of the Ω {\displaystyle \Omega } ({\displaystyle \Omega })-symbol to describe a stronger property, Knuth wrote: "For all the applications I have seen so far in computer science, a stronger requirement ... is much more appropriate". Knuth further wrote, "Although I have changed Hardy and Littlewood's definition of Ω {\displaystyle \Omega } ({\displaystyle \Omega }), I feel justified in doing so because their definition is by no means in wide use, and because there are other ways to say what they want to say in the comparatively rare cases when their definition applies." Knuth's big Ω {\displaystyle \Omega } ({\displaystyle \Omega }) enjoys widespread use today in computer science and combinatorics.

### Hardy's ≍ and Knuth's big Θ

In analytic number theory, the notation f ( x ) ≍ g ( x ) {\displaystyle f(x)\asymp g(x)} ({\displaystyle f(x)\asymp g(x)}) means both f ( x ) = O ( g ( x ) ) {\displaystyle f(x)=O(g(x))} ({\displaystyle f(x)=O(g(x))}) and g ( x ) = O ( f ( x ) ) {\displaystyle g(x)=O(f(x))} ({\displaystyle g(x)=O(f(x))}). This notation is originally due to Hardy. Knuth's notation for the same notion is f ( x ) = Θ ( g ( x ) ) {\displaystyle f(x)=\Theta (g(x))} ({\displaystyle f(x)=\Theta (g(x))}). Roughly speaking, these statements assert that f ( x ) {\displaystyle f(x)} ({\displaystyle f(x)}) and g ( x ) {\displaystyle g(x)} ({\displaystyle g(x)}) have the *same order*. These notations mean that there are positive constants M , N {\displaystyle M,N} ({\displaystyle M,N}) so that N g ( x ) ≤ f ( x ) ≤ M g ( x ) {\displaystyle Ng(x)\leq f(x)\leq Mg(x)} ({\displaystyle Ng(x)\leq f(x)\leq Mg(x)}) for all x {\displaystyle x} ({\displaystyle x}) in the common domain of f , g {\displaystyle f,g} ({\displaystyle f,g}). When the functions are defined on the positive integers or positive real numbers, as with big O, writers oftentimes interpret statements f ( x ) = Ω ( g ( x ) ) {\displaystyle f(x)=\Omega (g(x))} ({\displaystyle f(x)=\Omega (g(x))}) and f ( x ) = Θ ( g ( x ) ) {\displaystyle f(x)=\Theta (g(x))} ({\displaystyle f(x)=\Theta (g(x))}) as holding for all sufficiently large x {\displaystyle x} ({\displaystyle x}), that is, for all x {\displaystyle x} ({\displaystyle x}) beyond some point x 0 {\displaystyle x_{0}} ({\displaystyle x_{0}}). Sometimes this is indicated by appending *x → ∞ {\displaystyle x\to \infty } ({\displaystyle x\to \infty })* to the statement. For example, 2 n 2 − 10 n = Θ ( n 2 ) {\displaystyle 2n^{2}-10n=\Theta (n^{2})} ({\displaystyle 2n^{2}-10n=\Theta (n^{2})}) is true for the domain n ≥ 6 {\displaystyle n\geq 6} ({\displaystyle n\geq 6}) but false if the domain is all positive integers, since the function is zero at n = 5 {\displaystyle n=5} ({\displaystyle n=5}).

#### Further examples

n 3 + 20 n 2 + n + 12 ≍ n 3  for all  n ≥ 1. {\displaystyle n^{3}+20n^{2}+n+12\asymp n^{3}\quad {\text{ for all }}n\geq 1.} ({\displaystyle n^{3}+20n^{2}+n+12\asymp n^{3}\quad {\text{ for all }}n\geq 1.})

( 1 + x ) 8 = x 8 + Θ ( x 7 )  for all  x ≥ 1. {\displaystyle (1+x)^{8}=x^{8}+\Theta (x^{7})\quad {\text{ for all }}x\geq 1.} ({\displaystyle (1+x)^{8}=x^{8}+\Theta (x^{7})\quad {\text{ for all }}x\geq 1.})

The notation

f ( n ) = e Ω ( n )  for all  n ≥ 1 , {\displaystyle f(n)=e^{\Omega (n)}\quad {\text{ for all }}n\geq 1,} ({\displaystyle f(n)=e^{\Omega (n)}\quad {\text{ for all }}n\geq 1,}) means that there is a positive constant M {\displaystyle M} ({\displaystyle M}) so that f ( n ) ≥ e M n {\displaystyle f(n)\geq e^{Mn}} ({\displaystyle f(n)\geq e^{Mn}}) for all n ≥ 1 {\displaystyle n\geq 1} ({\displaystyle n\geq 1}). By contrast, f ( n ) = e − O ( n )  for all  n ≥ 1 , {\displaystyle f(n)=e^{-O(n)}\quad {\text{ for all }}n\geq 1,} ({\displaystyle f(n)=e^{-O(n)}\quad {\text{ for all }}n\geq 1,}) means that there is a positive constant M {\displaystyle M} ({\displaystyle M}) so that f ( n ) ≥ e − M n {\displaystyle f(n)\geq e^{-Mn}} ({\displaystyle f(n)\geq e^{-Mn}}) for all n ≥ 1 {\displaystyle n\geq 1} ({\displaystyle n\geq 1}) and f ( n ) = e Θ ( n )  for all  n ≥ 1 , {\displaystyle f(n)=e^{\Theta (n)}\quad {\text{ for all }}n\geq 1,} ({\displaystyle f(n)=e^{\Theta (n)}\quad {\text{ for all }}n\geq 1,}) means that there are positive constants M , N {\displaystyle M,N} ({\displaystyle M,N}) so that e M n ≤ f ( n ) ≤ e N n {\displaystyle e^{Mn}\leq f(n)\leq e^{Nn}} ({\displaystyle e^{Mn}\leq f(n)\leq e^{Nn}}) for all n ≥ 1 {\displaystyle n\geq 1} ({\displaystyle n\geq 1}).

For any domain D {\displaystyle D} ({\displaystyle D}), f ( x ) = g ( x ) + O ( 1 ) ⟺ e f ( x ) ≍ e g ( x ) , {\displaystyle f(x)=g(x)+O(1)\Longleftrightarrow e^{f(x)}\asymp e^{g(x)},} ({\displaystyle f(x)=g(x)+O(1)\Longleftrightarrow e^{f(x)}\asymp e^{g(x)},}) each statement being for all x {\displaystyle x} ({\displaystyle x}) in D {\displaystyle D} ({\displaystyle D}).


## Orders of common functions

Here is a list of classes of functions that are commonly encountered when analyzing the running time of an algorithm. In each case, *c* is a positive constant and *n* increases without bound. The slower-growing functions are generally listed first.

| Notation | Name | Example |
|---|---|---|
| O ( 1 ) {\displaystyle O(1)} ({\displaystyle O(1)}) | constant | Finding the median value for a sorted array of numbers; Calculating ( − 1 ) n {\displaystyle (-1)^{n}} ({\displaystyle (-1)^{n}}); Using a constant-size lookup table |
| O ( α ( n ) ) {\displaystyle O(\alpha (n))} ({\displaystyle O(\alpha (n))}) | inverse Ackermann function | Amortized complexity per operation for the Disjoint-set data structure |
| O ( log ⁡ log ⁡ n ) {\displaystyle O(\log \log n)} ({\displaystyle O(\log \log n)}) | double logarithmic | Average number of comparisons spent finding an item using interpolation search in a sorted array of uniformly distributed values |
| O ( log ⁡ n ) {\displaystyle O(\log n)} ({\displaystyle O(\log n)}) | logarithmic | Finding an item in a sorted array with a binary search or a balanced search tree as well as all operations in a binomial heap |
| O ( ( log ⁡ n ) c ) {\displaystyle O((\log n)^{c})} ({\displaystyle O((\log n)^{c})}) c > 1 {\textstyle c>1} ({\textstyle c>1}) | polylogarithmic | Matrix chain ordering can be solved in polylogarithmic time on a parallel random-access machine. |
| O ( n c ) {\displaystyle O(n^{c})} ({\displaystyle O(n^{c})}) 0 < c < 1 {\textstyle 0<c<1} ({\textstyle 0<c<1}) | fractional power | Searching in a k-d tree Trial division naive primality testing ( O ( n ) {\displaystyle O({\sqrt {n}})} ({\displaystyle O({\sqrt {n}})})) |
| O ( n ) {\displaystyle O(n)} ({\displaystyle O(n)}) | linear | Finding an item in an unsorted list or in an unsorted array; adding two *n*-bit integers by ripple carry |
| O ( n log ∗ ⁡ n ) {\displaystyle O(n\log ^{*}n)} ({\displaystyle O(n\log ^{*}n)}) | *n* log-star *n* | Performing triangulation of a simple polygon using Seidel's algorithm, where log ∗ ⁡ ( n ) = { 0 , if  n ≤ 1 1 + log ∗ ⁡ ( log ⁡ n ) , if  n > 1 {\displaystyle \log ^{*}(n)={\begin{cases}0,&{\text{if }}n\leq 1\\1+\log ^{*}(\log n),&{\text{if }}n>1\end{cases}}} ({\displaystyle \log ^{*}(n)={\begin{cases}0,&{\text{if }}n\leq 1\\1+\log ^{*}(\log n),&{\text{if }}n>1\end{cases}}}) |
| O ( n log ⁡ n ) = O ( log ⁡ n ! ) {\displaystyle O(n\log n)=O(\log n!)} ({\displaystyle O(n\log n)=O(\log n!)}) | linearithmic, loglinear, quasilinear, or " n log ⁡ n {\displaystyle n\log n} ({\displaystyle n\log n})" | Performing a fast Fourier transform; fastest possible comparison sort; heapsort and merge sort |
| O ( n 2 ) {\displaystyle O(n^{2})} ({\displaystyle O(n^{2})}) | quadratic | Multiplying two n {\displaystyle n} ({\displaystyle n})-digit numbers by schoolbook multiplication; simple sorting algorithms, such as bubble sort, selection sort and insertion sort; (worst-case) bound on some usually faster sorting algorithms such as quicksort, Shellsort, and tree sort |
| O ( n c ) {\displaystyle O(n^{c})} ({\displaystyle O(n^{c})}) | polynomial or algebraic | Tree-adjoining grammar parsing; maximum matching for bipartite graphs; finding the determinant with LU decomposition |
| L n [ α , c ] = e ( c + o ( 1 ) ) ( ln ⁡ n ) α ( ln ⁡ ln ⁡ n ) 1 − α {\displaystyle L_{n}[\alpha ,c]=e^{(c+o(1))(\ln n)^{\alpha }(\ln \ln n)^{1-\alpha }}} ({\displaystyle L_{n}[\alpha ,c]=e^{(c+o(1))(\ln n)^{\alpha }(\ln \ln n)^{1-\alpha }}}) 0 < α < 1 {\textstyle 0<\alpha <1} ({\textstyle 0<\alpha <1}) | L-notation or sub-exponential | Factoring a number using the quadratic sieve or number field sieve |
| O ( c n ) {\displaystyle O(c^{n})} ({\displaystyle O(c^{n})}) c > 1 {\textstyle c>1} ({\textstyle c>1}) | exponential | Finding the (exact) solution to the travelling salesman problem using dynamic programming; determining if two logical statements are equivalent using brute-force search |
| O ( n ! ) {\displaystyle O(n!)} ({\displaystyle O(n!)}) | factorial | Solving the travelling salesman problem via brute-force search; generating all unrestricted permutations of a poset; finding the determinant with Laplace expansion; enumerating all partitions of a set |

The statement f ( n ) = O ( n ! ) {\displaystyle f(n)=O(n!)} ({\displaystyle f(n)=O(n!)}) is sometimes weakened to f ( n ) = O ( n n ) {\displaystyle f(n)=O\left(n^{n}\right)} ({\displaystyle f(n)=O\left(n^{n}\right)}) to derive simpler formulas for asymptotic complexity. In many of these examples, the running time is actually Θ ( g ( n ) ) {\displaystyle \Theta (g(n))} ({\displaystyle \Theta (g(n))}), which conveys more precision.
