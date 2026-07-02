---
title: "Big O notation"
source: https://en.wikipedia.org/wiki/Big_O_notation
domain: algorithms
license: CC-BY-SA-4.0
tags: algorithm, sorting, complexity, big-o, dynamic programming
fetched: 2026-07-02
---

# Big *O* notation

**Big *O* notation** is a mathematical notation that describes the approximate size of a function on a domain. Big O is a member of a family of notations invented by the German mathematicians Paul Bachmann and Edmund Landau and expanded by others, collectively called **Bachmann–Landau notation**. The letter O stands for *Ordnung*, that is, the order of approximation.

In computer science, big O notation is used to classify algorithms by how their run time or space requirements grow with the input. In analytic number theory, big O notation expresses bounds on the growth of an arithmetical function, as for the remainder term in the prime number theorem. In mathematical analysis, including calculus, Big O notation bounds the error when truncating a power series and expresses the quality of approximation of a real or complex valued function by a simpler function.

Often, big O notation characterizes functions according to their growth rates as the variable becomes large: different functions with the same asymptotic growth rate may be represented using the same O notation. The letter O is used because the growth rate of a function is also referred to as the **order of the function**. A description of a function in terms of big O notation only provides an upper bound on the growth rate of the function.

Associated with big O notation are several related notations, using the symbols o , $\sim$ , $\Omega$ , $\ll$ , $\gg$ , $\asymp$ , $\omega$ , and $\Theta$ to describe other kinds of bounds on growth rates.

Bachmann proposed the notation in 1894 and Landau extended it in 1909. An earlier notation was proposed by Paul du Bois-Reymond in 1870.

## Formal definition

Let ${\textstyle f,}$ the function to be estimated, be either a real or complex valued function defined on a domain ${\textstyle D,}$ and let ${\textstyle g,}$ the comparison function, be a non-negative real valued function defined on the same set ${\textstyle D.}$ Common choices for the domain are intervals of real numbers, bounded or unbounded, the set of positive integers, the set of complex numbers and tuples of real/complex numbers. With the domain written explicitly or understood implicitly, one writes

$f(x)=O{\bigl (}g(x){\bigr )}\$

which is read as  " ${\textstyle f(x)}$ is big ${\textstyle O}$ of ${\textstyle g(x)}$ "  if there exists a positive real number ${\textstyle M}$ such that

$\left|f(x)\right|\leq M\ g(x)\qquad ~{\mathsf {\ for\ all\ }}~\quad x\in D.$

If $g(x)>0$ (i.e. g is also never zero) throughout the domain $D,$ an equivalent definition is that the ratio ${\textstyle {\frac {f(x)}{g(x)}}}$ is *bounded*, i.e. there is a positive real number M so that ${\textstyle {\Big |}{\frac {f(x)}{g(x)}}{\Big |}\leq M}$ for all $x\in D.$ These encompass all the uses of big ${\textstyle O}$ in computer science and mathematics, including its use where the domain is finite, infinite, real, complex, single variate, or multivariate. In most applications, one chooses the function $g(x)$ appearing within the argument of ${\textstyle O{\bigl (}\cdot {\bigr )}}$ to be as simple a form as possible, omitting constant factors and lower order terms. The number ${\textstyle M}$ is called the *implied constant* because it is normally not specified. When using big ${\textstyle O}$ notation, what matters is that some finite M exists, not its specific value. This simplifies the presentation of many analytic inequalities.

For functions defined on positive real numbers or positive integers, a more restrictive and somewhat conflicting definition is still in common use, especially in computer science. When restricted to functions which are eventually positive, the notation

$f(x)=O{\bigl (}g(x){\bigr )}\qquad ~{\mathsf {as}}\quad x\to \infty$

means that for some real number ${\textstyle a,}$ ${\textstyle f(x)=O{\bigl (}g(x){\bigr )}}$ in the domain ${\textstyle \left[a,\infty \right).}$ Here, the expression ${\textstyle x\to \infty }$ does not indicate a limit, but the notion that the inequality holds for *large enough* ${\textstyle x.}$ The expression ${\textstyle x\to \infty }$ often is omitted.

Similarly, for a real number ${\textstyle a,}$ the notation

$f(x)=O{\bigl (}g(x){\bigr )}\qquad ~{\text{ as }}\ x\to a$

means that for some constant ${\textstyle c>0,}$ ${\textstyle f(x)=O{\bigl (}g(x){\bigr )}}$ on the interval $\left[a-c,a+c\right];$ that is, in a small neighborhood of $a.$ In addition, the notation $\ f(x)=h(x)+O{\bigl (}g(x){\bigr )}\$ means ${\textstyle f(x)-h(x)=O{\bigl (}g(x){\bigr )}.}$ More complicated expressions are also possible.

Despite the presence of the equal sign (=) as written, the expression ${\textstyle f(x)=O{\bigl (}g(x){\bigr )}}$ does not refer to an equality, but rather to an inequality relating ${\textstyle f}$ and ${\textstyle g.}$

In the 1930s, the Russian number theorist I.M. Vinogradov introduced the notation $\ll ,$ which has been increasingly used in number theory and other branches of mathematics, as an alternative to the ${\textstyle O}$ notation. We have

$\ f\ll g\iff f=O{\bigl (}g{\bigr )}.$

Frequently both notations are used in the same work.

### Set version of big O

In computer science it is common to define big ${\textstyle O}$ as also defining a set of functions. With the positive (or non-negative) function $g(x)$ specified, one interprets ${\textstyle O{\bigl (}g(x){\bigr )}}$ as representing the *set* of all functions ${\textstyle {\tilde {f}}}$ that satisfy ${\textstyle {\tilde {f}}(x)=O{\bigl (}g(x){\bigr )}.}$ One can then equivalently write ${\textstyle f(x)\in O{\bigl (}g(x){\bigr )},}$ read as "the function ${\textstyle \ f(x)\ }$ is among the set of all functions of order at most ${\textstyle g(x).}$ "

## Examples with an infinite domain

In typical usage the O notation is applied to an infinite interval of real numbers $[a,\infty )$ and captures the behavior of the function for very large x . In this setting, the contribution of the terms that grow "most quickly" will eventually make the other ones irrelevant. As a result, the following simplification rules can be applied:

- If $f(x)$ is a sum of several terms, if there is one with largest growth rate, it can be kept, and all others omitted.
- If $f(x)$ is a product of several factors, any constants (factors in the product that do not depend on x ) can be omitted.

For example, let $f(x)=6x^{4}-2x^{3}+5$ , and suppose we wish to simplify this function, using O notation, to describe its growth rate for large x . This function is the sum of three terms: $6x^{4}$ , $-2x^{3}$ , and 5 . Of these three terms, the one with the highest growth rate is the one with the largest exponent as a function of x , namely $6x^{4}$ . Now one may apply the second rule: $6x^{4}$ is a product of 6 and $x^{4}$ in which the first factor does not depend on x . Omitting this factor results in the simplified form $x^{4}$ . Thus, we say that $f(x)$ is a "big O" of $x^{4}$ . Mathematically, we can write $f(x)=O(x^{4})$ for all $x\geq 1$ . One may confirm this calculation using the formal definition: let $f(x)=6x^{4}-2x^{3}+5$ and $g(x)=x^{4}$ . Applying the formal definition from above, the statement that $f(x)=O(x^{4})$ is equivalent to its expansion, $|f(x)|\leq Mx^{4}$ for some suitable choice of a positive real number M and for all $x\geq 1$ . To prove this, let $M=13$ . Then, for all $x\geq 1$ : ${\begin{aligned}|6x^{4}-2x^{3}+5|&\leq 6x^{4}+|-2x^{3}|+5\\&\leq 6x^{4}+2x^{4}+5x^{4}\\&=13x^{4}\end{aligned}}$ so $|6x^{4}-2x^{3}+5|\leq 13x^{4}.$ While it is also true, by the same argument, that $f(x)=O(x^{10})$ , this is a less precise approximation of the function f . On the other hand, the statement $f(x)=O(x^{3})$ is false, because the term $6x^{4}$ causes $f(x)/x^{3}$ to be unbounded.

When a function $T(n)$ describes the number of steps required in an algorithm with input n , an expression such as $T(n)=O(n^{2})$ with the implied domain being the set of positive integers, may be interpreted as saying that the algorithm has *at most the order of $n^{2}$* time complexity.

## Example with a finite domain

Big O can also be used to describe the error term in an approximation to a mathematical function on a finite interval. The most significant terms are written explicitly, and then the least-significant terms are summarized in a single big O term. Consider, for example, the exponential series and two expressions of it that are valid when x is small: ${\begin{aligned}e^{x}&=1+x+{\frac {\;x^{2}\ }{2!}}+{\frac {\;x^{3}\ }{3!}}+{\frac {\;x^{4}\ }{4!}}+\dotsb &&{\text{ for all finite }}x\\[4pt]&=1+x+{\frac {\;x^{2}\ }{2}}+O(|x|^{3})&&{\text{ for all }}|x|\leq 1\\[4pt]&=1+x+O(x^{2})&&{\text{ for all }}|x|\leq 1.\end{aligned}}$ The middle expression (the line with " $O(|x^{3}|)$ ") means the absolute-value of the error $\ e^{x}-(1+x+{\frac {\;x^{2}\ }{2}})\$ is at most some constant times $~|x^{3}|\$ when $\ x~$ is small. This is an example of the use of Taylor's theorem.

The behavior of a given function may be very different on finite domains than on infinite domains, for example, $(x+1)^{8}=x^{8}+O(x^{7})\quad {\text{ for }}x\geq 1$ while $(x+1)^{8}=1+8x+O(x^{2})\quad {\text{ for }}|x|\leq 1.$

## Multivariate examples

$x\sin y=O(x)\quad {\text{ for }}x\geq 1,y{\text{ any real number}}$

$3a^{2}+7ab+2b^{2}+a+3b+14\ll a^{2}+b^{2}\ll a^{2}\quad {\text{ for all }}a\geq b\geq 1$

${\frac {xy}{x^{2}+y^{2}}}=O(1)\quad {\text{ for all real }}x,y{\text{ that are not both }}0$

$x^{it}=O(1)\quad {\text{ for }}x\neq 0,t\in \mathbb {R} .$

Here we have a complex variable function of two variables. In general, any bounded function is $O(1)$ .

$(x+y)^{10}=O(x^{10})\quad {\text{ for }}x\geq 1,-2\leq y\leq 2.$

The last example illustrates a mixing of finite and infinite domains on the different variables.

In all of these examples, the bound is uniform in both variables. Sometimes in a multivariate expression, one variable is more important than others, and one may express that the implied constant M depends on one or more of the variables using subscripts to the big O symbol or the $\ll$ symbol. For example, consider the expression

$(1+x)^{b}=1+O_{b}(x)\quad {\text{ for }}0\leq x\leq 1,b{\text{ any real number.}}$

This means that for each real number b , there is a constant $M_{b}$ , *which depends on b*, so that for all $0\leq x\leq 1$ , $|(1+x)^{b}-1|\leq M_{b}\cdot x.$ This particular statement follows from the general binomial theorem.

Another example, common in the theory of Taylor series, is $e^{x}=1+x+O_{r}(x^{2})\quad {\text{ for all }}|x|\leq r,r{\text{ being any real number.}}$ Here the implied constant depends on the size of the domain.

The subscript convention applies to all of the other notations in this page.

## Properties

### Product

$f_{1}=O(g_{1}){\text{ and }}f_{2}=O(g_{2})\Rightarrow f_{1}f_{2}=O(g_{1}g_{2})$

$f\cdot O(g)=O(|f|g)$

### Sum

If $f_{1}=O(g_{1})$ and $f_{2}=O(g_{2})$ then $f_{1}+f_{2}=O(\max(g_{1},g_{2}))$ . It follows that if $f_{1}=O(g)$ and $f_{2}=O(g)$ then $f_{1}+f_{2}=O(g)$ .

### Multiplication by a constant

Let k be a nonzero constant. Then $O(|k|\cdot g)=O(g)$ . In other words, if $f=O(g)$ , then $k\cdot f=O(g).$

### Transitive property

If $f=O(g)$ and $g=O(h)$ then $f=O(h)$ .

If the function f of a positive integer n can be written as a finite sum of other functions, then the fastest growing one determines the order of $f(n)$ . For example,

$f(n)=9\log n+5(\log n)^{4}+3n^{2}+2n^{3}=O(n^{3})\qquad {\text{for }}n\geq 1.$

Some general rules about growth *toward infinity*; the 2nd and 3rd property below can be proved rigorously using L'Hôpital's rule:

### Large powers dominate small powers

For $b\geq a$ , then $n^{a}=O(n^{b})$ as $n\to \infty$ .

### Powers dominate logarithms

For any positive $a,b,$ $(\log n)^{a}=O_{a,b}(n^{b}),$ no matter how large a is and how small b is. Here, the implied constant depends on both a and b .

### Exponentials dominate powers

For any positive $a,b,$ $n^{a}=O_{a,b}(e^{bn}),$ no matter how large a is and how small b is.

A function that grows faster than $n^{c}$ for any c is called *superpolynomial*. One that grows more slowly than any exponential function of the form $c^{n}$ with $c>1$ is called *subexponential*. An algorithm can require time that is both superpolynomial and subexponential; examples of this include the fastest known algorithms for integer factorization and the function $n^{\log n}$ .

We may ignore any powers of n inside of the logarithms. For any positive c , the notation $O(\log n)$ means exactly the same thing as $O(\log(n^{c}))$ , since $\log(n^{c})=c\log n$ . Similarly, logs with different constant bases are equivalent with respect to Big O notation. On the other hand, exponentials with different bases are not of the same order. For example, $2^{n}$ and $3^{n}$ are not of the same order.

### More complicated expressions

In more complicated usage, $O(\cdot )$ can appear in different places in an equation, even several times on each side. For example, the following are true for n a positive integer: ${\begin{aligned}(n+1)^{2}&=n^{2}+O(n),\\(n+O(n^{1/2}))\cdot (n+O(\log n))^{2}&=n^{3}+O(n^{5/2}),\\n^{O(1)}&=O(e^{n}).\end{aligned}}$ The meaning of such statements is as follows: for *any* functions which satisfy each $O(\cdot )$ on the left side, there are *some* functions satisfying each $O(\cdot )$ on the right side, such that substituting all these functions into the equation makes the two sides equal. For example, the third equation above means: "For any function satisfying $f(n)=O(1)$ , there is some function $g(n)=O(e^{n})$ such that $n^{f(n)}=g(n)$ ". The implied constant in the statement " $g(n)=O(e^{n})$ " may depend on the implied constant in the expression " $f(n)=O(1)$ ".

Some further examples: ${\begin{aligned}f=O(g)\;&\Rightarrow \;\int _{a}^{b}f=O{\bigg (}\int _{a}^{b}g{\bigg )}\\f(x)=g(x)+O(1)\;&\Rightarrow \;e^{f(x)}=O(e^{g(x)})\\(1+O(1/x))^{O(x)}&=O(1)\quad {\text{ for }}x>0\\\sin x&=O(|x|)\quad {\text{ for all real }}x.\end{aligned}}$

### Vinogradov's ≫ and Knuth's big Ω

When $f,g$ are both positive functions, Vinogradov introduced the notation $f(x)\gg g(x)$ , which means the same as $g(x)=O(f(x))$ . Vinogradov's two notations enjoy visual symmetry, as for positive functions $f,g$ , we have $f(x)\ll g(x)\Longleftrightarrow g(x)\gg f(x).$

In 1976, Donald Knuth defined

$f(x)=\Omega (g(x))\Longleftrightarrow g(x)=O(f(x))$

which has the same meaning as Vinogradov's $f(x)\gg g(x)$ .

However, much earlier, Hardy and Littlewood had defined $\Omega$ differently, and their notation enjoys widespread use today in analytic number theory. Justifying his use of the $\Omega$ -symbol to describe a stronger property, Knuth wrote: "For all the applications I have seen so far in computer science, a stronger requirement ... is much more appropriate". Knuth further wrote, "Although I have changed Hardy and Littlewood's definition of $\Omega$ , I feel justified in doing so because their definition is by no means in wide use, and because there are other ways to say what they want to say in the comparatively rare cases when their definition applies." Knuth's big $\Omega$ enjoys widespread use today in computer science and combinatorics.

### Hardy's ≍ and Knuth's big Θ

In analytic number theory, the notation $f(x)\asymp g(x)$ means both $f(x)=O(g(x))$ and $g(x)=O(f(x))$ . This notation is originally due to Hardy. Knuth's notation for the same notion is $f(x)=\Theta (g(x))$ . Roughly speaking, these statements assert that $f(x)$ and $g(x)$ have the *same order*. These notations mean that there are positive constants $M,N$ so that $Ng(x)\leq f(x)\leq Mg(x)$ for all x in the common domain of $f,g$ . When the functions are defined on the positive integers or positive real numbers, as with big O, writers oftentimes interpret statements $f(x)=\Omega (g(x))$ and $f(x)=\Theta (g(x))$ as holding for all sufficiently large x , that is, for all x beyond some point $x_{0}$ . Sometimes this is indicated by appending *$x\to \infty$* to the statement. For example, $2n^{2}-10n=\Theta (n^{2})$ is true for the domain $n\geq 6$ but false if the domain is all positive integers, since the function is zero at $n=5$ .

#### Further examples

$n^{3}+20n^{2}+n+12\asymp n^{3}\quad {\text{ for all }}n\geq 1.$

$(1+x)^{8}=x^{8}+\Theta (x^{7})\quad {\text{ for all }}x\geq 1.$

The notation

$f(n)=e^{\Omega (n)}\quad {\text{ for all }}n\geq 1,$ means that there is a positive constant M so that $f(n)\geq e^{Mn}$ for all $n\geq 1$ . By contrast, $f(n)=e^{-O(n)}\quad {\text{ for all }}n\geq 1,$ means that there is a positive constant M so that $f(n)\geq e^{-Mn}$ for all $n\geq 1$ and $f(n)=e^{\Theta (n)}\quad {\text{ for all }}n\geq 1,$ means that there are positive constants $M,N$ so that $e^{Mn}\leq f(n)\leq e^{Nn}$ for all $n\geq 1$ .

For any domain D , $f(x)=g(x)+O(1)\Longleftrightarrow e^{f(x)}\asymp e^{g(x)},$ each statement being for all x in D .

## Orders of common functions

Here is a list of classes of functions that are commonly encountered when analyzing the running time of an algorithm. In each case, *c* is a positive constant and *n* increases without bound. The slower-growing functions are generally listed first.

| Notation | Name | Example |
|---|---|---|
| $O(1)$ | constant | Finding the median value for a sorted array of numbers; Calculating $(-1)^{n}$ ; Using a constant-size lookup table |
| $O(\alpha (n))$ | inverse Ackermann function | Amortized complexity per operation for the Disjoint-set data structure |
| $O(\log \log n)$ | double logarithmic | Average number of comparisons spent finding an item using interpolation search in a sorted array of uniformly distributed values |
| $O(\log n)$ | logarithmic | Finding an item in a sorted array with a binary search or a balanced search tree as well as all operations in a binomial heap |
| $O((\log n)^{c})$ ${\textstyle c>1}$ | polylogarithmic | Matrix chain ordering can be solved in polylogarithmic time on a parallel random-access machine. |
| $O(n^{c})$ ${\textstyle 0<c<1}$ | fractional power | Searching in a k-d tree Trial division naive primality testing ( $O({\sqrt {n}})$ ) |
| $O(n)$ | linear | Finding an item in an unsorted list or in an unsorted array; adding two *n*-bit integers by ripple carry |
| $O(n\log ^{*}n)$ | *n* log-star *n* | Performing triangulation of a simple polygon using Seidel's algorithm, where $\log ^{*}(n)={\begin{cases}0,&{\text{if }}n\leq 1\\1+\log ^{*}(\log n),&{\text{if }}n>1\end{cases}}$ |
| $O(n\log n)=O(\log n!)$ | linearithmic, loglinear, quasilinear, or " $n\log n$ " | Performing a fast Fourier transform; fastest possible comparison sort; heapsort and merge sort |
| $O(n^{2})$ | quadratic | Multiplying two n -digit numbers by schoolbook multiplication; simple sorting algorithms, such as bubble sort, selection sort and insertion sort; (worst-case) bound on some usually faster sorting algorithms such as quicksort, Shellsort, and tree sort |
| $O(n^{c})$ | polynomial or algebraic | Tree-adjoining grammar parsing; maximum matching for bipartite graphs; finding the determinant with LU decomposition |
| $L_{n}[\alpha ,c]=e^{(c+o(1))(\ln n)^{\alpha }(\ln \ln n)^{1-\alpha }}$ ${\textstyle 0<\alpha <1}$ | L-notation or sub-exponential | Factoring a number using the quadratic sieve or number field sieve |
| $O(c^{n})$ ${\textstyle c>1}$ | exponential | Finding the (exact) solution to the travelling salesman problem using dynamic programming; determining if two logical statements are equivalent using brute-force search |
| $O(n!)$ | factorial | Solving the travelling salesman problem via brute-force search; generating all unrestricted permutations of a poset; finding the determinant with Laplace expansion; enumerating all partitions of a set |

The statement $f(n)=O(n!)$ is sometimes weakened to $f(n)=O\left(n^{n}\right)$ to derive simpler formulas for asymptotic complexity. In many of these examples, the running time is actually $\Theta (g(n))$ , which conveys more precision.

## Little-o notation

For real or complex-valued functions of a real variable x with $g(x)>0$ for sufficiently large x , one writes

$f(x)=o(g(x))\quad {\text{ as }}x\to \infty$

if $\lim _{x\to \infty }{\frac {f(x)}{g(x)}}=0.$ That is, for every positive constant ε there exists a constant $x_{0}$ such that

$|f(x)|\leq \varepsilon g(x)\quad {\text{ for all }}x\geq x_{0}.$

Intuitively, this means that $g(x)$ grows much faster than $f(x)$ , or equivalently $f(x)$ grows much slower than $g(x)$ . For example, one has

$200x=o(x^{2})$

and

$1/x=o(1),$

both as

$x\to \infty .$

When one is interested in the behavior of a function for large values of x , little-o notation makes a *stronger statement* than the corresponding big-O notation: every function that is little-o of g is also big-O of g on some interval $[a,\infty )$ , but not every function that is big-O of g is little-o of g . For example, $2x^{2}=O(x^{2})$ but $2x^{2}\neq o(x^{2})$ for $x\geq 1$ .

Little-o respects a number of arithmetic operations. For example,

if

c

is a nonzero constant and

$f=o(g)$

then

$c\cdot f=o(g)$

, and

if

$f=o(F)$

and

$g=o(G)$

then

$f\cdot g=o(F\cdot G).$

if

$f=o(F)$

and

$g=o(G)$

then

$f+g=o(F+G)$

It also satisfies a transitivity relation:

if

$f=o(g)$

and

$g=o(h)$

then

$f=o(h).$

Little-o can also be generalized to the finite case: $f(x)=o(g(x))\quad {\text{ as }}x\to x_{0}$ if $\lim _{x\to x_{0}}{\frac {f(x)}{g(x)}}=0.$ In other words, $f(x)=\alpha (x)g(x)$ for some $\alpha (x)$ with $\lim _{x\to x_{0}}\alpha (x)=0$ .

This definition is especially useful in the computation of limits using Taylor series. For example:

$\sin x=x-{\frac {x^{3}}{3!}}+\ldots =x+o(x^{2}){\text{ as }}x\to 0$ , so $\lim _{x\to 0}{\frac {\sin x}{x}}=\lim _{x\to 0}{\frac {x+o(x^{2})}{x}}=\lim _{x\to 0}1+o(x)=1$

### Asymptotic notation

A relation related to little-o is the *asymptotic* notation $\sim$ . For real valued functions $f,g$ , the expression $f(x)\sim g(x)\quad {\text{ as }}x\to \infty$ means $\lim _{x\to \infty }{\frac {f(x)}{g(x)}}=1.$ One can connect this to little-o by observing that $f(x)\sim g(x)$ is also equivalent to $f(x)=(1+o(1))g(x)$ . Here $o(1)$ refers to a function tending to zero as $x\to \infty$ . One reads this as " $f(x)$ is *asymptotic to* $g(x)$ ". For nonzero functions on the same (finite or infinite) domain, $\sim$ forms an equivalence relation.

One of the most famous theorems using the notation $\sim$ is Stirling's formula $n!\sim {\bigg (}{\frac {n}{e}}{\bigg )}^{n}{\sqrt {2\pi n}}\quad {\text{ as }}n\to \infty .$ In number theory, the famous prime number theorem states that $\pi (x)\sim {\frac {x}{\log x}}\quad {\text{ as }}x\to \infty ,$ where $\pi (x)$ is the number of primes which are at most x and $\log$ is the natural logarithm of x .

As with little-o, there is a version with finite limits (two-sided or one-sided) as well, for example $\sin x\sim x\quad {\text{ as }}x\to 0.$

Further examples: $x^{a}=o_{a,b}(e^{bx})\quad {\text{ as }}x\to \infty ,{\text{ for any positive constants }}a,b,$ $f(x)=g(x)+o(1)\quad \Longleftrightarrow \quad e^{f(x)}\sim e^{g(x)}\quad (x\to \infty ).$ $\sum _{n=1}^{\infty }{\frac {1}{n^{s}}}\sim {\frac {1}{s-1}}\quad (s\to 1^{+}).$ The last asymptotic is a basic property of the Riemann zeta function.

### Knuth's little 𝜔

For eventually positive, real valued functions $f,g,$ the notation $f(x)=\omega (g(x))\quad {\text{ as }}x\to \infty$ means $\lim _{x\to \infty }{\frac {f(x)}{g(x)}}=\infty .$ In other words, $g(x)=o(f(x))$ . Roughly speaking, this means that $f(x)$ grows much faster than does $g(x)$ .

### The Hardy–Littlewood Ω notation

In 1914 G. H. Hardy and J. E. Littlewood introduced the new symbol $\ \Omega ,$ which is defined as follows:

$f(x)=\Omega (g(x))\quad$

as

$\quad x\to \infty \quad$

if

$\quad \limsup _{x\to \infty }\ \left|{\frac {\ f(x)\ }{g(x)}}\right|>0~.$

Thus $~f(x)=\Omega (g(x))~$ is the negation of $~f(x)=o(g(x))~.$

In 1916 the same authors introduced the two new symbols $\ \Omega _{R}\$ and $\ \Omega _{L}\ ,$ defined as:

$f(x)=\Omega _{R}(g(x))\quad$

as

$\quad x\to \infty \quad$

if

$\quad \limsup _{x\to \infty }\ {\frac {\ f(x)\ }{g(x)}}>0\ ;$

$f(x)=\Omega _{L}(g(x))\quad$

as

$\quad x\to \infty \quad$

if

$\quad ~\liminf _{x\to \infty }\ {\frac {\ f(x)\ }{g(x)}}<0~.$

These symbols were used by E. Landau, with the same meanings, in 1924. Authors that followed Landau, however, use a different notation for the same definitions: The symbol $\ \Omega _{R}\$ has been replaced by the current notation $\ \Omega _{+}\$ with the same definition, and $\ \Omega _{L}\$ became $\ \Omega _{-}~.$

These three symbols $\ \Omega \ ,\Omega _{+}\ ,\Omega _{-}\ ,$ as well as $\ f(x)=\Omega _{\pm }(g(x))\$ (meaning that $\ f(x)=\Omega _{+}(g(x))\$ and $\ f(x)=\Omega _{-}(g(x))\$ are both satisfied), are now currently used in analytic number theory.

#### Simple examples

We have

$\sin x=\Omega (1)\quad$

as

$\quad x\to \infty \ ,$

and more precisely

$\sin x=\Omega _{\pm }(1)\quad$

as

$\quad x\to \infty ,~$

where $\Omega _{\pm }$ means that the left side is both $\Omega _{+}(1)$ and $\Omega _{-}(1)$ ,

We have

$1+\sin x=\Omega (1)\quad$

as

$\quad x\to \infty \ ,$

and more precisely

$1+\sin x=\Omega _{+}(1)\quad$

as

$\quad x\to \infty \ ;$

however

$1+\sin x\neq \Omega _{-}(1)\quad$

as

$\quad x\to \infty ~.$

### Family of Bachmann–Landau notations

For understanding the formal definitions, consult the list of logic symbols used in mathematics.

| Notation | Name | Description | Formal definition | Compact definition |
|---|---|---|---|---|
| $f(n)=O(g(n))$ or $f(n)\ll g(n)$ (Vinogradov's notation) | Big O; Big Oh; Big Omicron | $\|f\|$ is bounded above by g (up to constant factor k ) | $\exists k>0\,\forall n\in D\colon \|f(n)\|\leq k\,g(n)$ | $\sup _{n\in D}{\frac {\left\|f(n)\right\|}{g(n)}}<\infty$ |
| $f(n)=o(g(n))$ | Small O; Small Oh; Little O; Little Oh | f is dominated by g asymptotically (for any constant factor k ) | $\forall k>0\,\exists n_{0}\,\forall n>n_{0}\colon \|f(n)\|\leq k\,g(n)$ | $\lim _{n\to \infty }{\frac {f(n)}{g(n)}}=0$ |
| $f(n)=\Omega (g(n))$ | Big Omega in number theory (Hardy–Littlewood) | $\|f\|$ is not dominated by g asymptotically | $\exists k>0\,\forall n_{0}\,\exists n>n_{0}\colon \|f(n)\|\geq k\,g(n)$ | $\limsup _{n\to \infty }{\frac {\|f(n)\|}{g(n)}}>0$ |
| $f(n)=\Omega _{+}(g(n))$ | Omega plus (Hardy–Littlewood) | f is not dominated by g asymptotically | $\exists k>0\,\forall n_{0}\,\exists n>n_{0}\colon f(n)\geq k\,g(n)$ | $\limsup _{n\to \infty }{\frac {f(n)}{g(n)}}>0$ |
| $f(n)=\Omega _{-}(g(n))$ | Omega minus (Hardy–Littlewood) | $-f$ is not dominated by g asymptotically | $\exists k>0\,\forall n_{0}\,\exists n>n_{0}\colon -f(n)\geq k\,g(n)$ | $\limsup _{n\to \infty }{\frac {-f(n)}{g(n)}}>0$ |
| $f(n)=\Omega _{\pm }(g(n))$ | Omega plus and minus | neither f nor $-f$ is dominated by g asymptotically | $f(n)=\Omega _{+}(g(n))$ and $f(n)=\Omega _{-}(g(n))$ |   |
| $f(n)\asymp g(n)$ (Hardy's notation) or $f(n)=\Theta (g(n))$ (Knuth notation) | Of the same order as (Hardy); Big Theta (Knuth) | f is bounded by g both above (with constant factor $k_{2}$ ) and below (with constant factor $k_{1}$ ) | $\exists k_{1}>0\,\exists k_{2}>0\,\forall n\in D\colon$ $k_{1}\,g(n)\leq f(n)\leq k_{2}\,g(n)$ | $f(n)=O(g(n))$ and $g(n)=O(f(n))$ |
| $f(n)\sim g(n)$ as $n\to a$ , where a is finite, $\infty$ or $-\infty$ | Asymptotic equivalence | f is equal to g asymptotically | $\forall \varepsilon >0\,\exists n_{0}\,\forall n>n_{0}\colon \left\|{\frac {f(n)}{g(n)}}-1\right\|<\varepsilon$ (in the case $a=\infty$ ) | $\lim _{n\to a}{\frac {f(n)}{g(n)}}=1$ |
| $f(n)=\Omega (g(n))$ (Knuth's notation), or $f(n)\gg g(n)$ (Vinogradov's notation) | Big Omega in complexity theory (Knuth) | f is bounded below by g, up to a constant factor | $\exists k>0\,\forall n\in D\colon f(n)\geq k\,g(n)$ | $\inf _{n\in D}{\frac {f(n)}{g(n)}}>0$ |
| $f(n)=\omega (g(n))$ as $n\to a$ , where a can be finite, $\infty$ or $-\infty$ | Small Omega; Little Omega | f dominates g asymptotically | $\forall k>0\,\exists n_{0}\,\forall n>n_{0}\colon f(n)>k\,g(n)$ (for $a=\infty$ ) | $\lim _{n\to a}{\frac {f(n)}{g(n)}}=\infty$ |

The limit definitions assume $g(n)>0$ for n in a neighborhood of the limit; when the limit is $\infty$ , this means that $g(n)>0$ for sufficiently large n .

Computer science and combinatorics use the big O , big Theta $\Theta$ , little o , little omega $\omega$ and Knuth's big Omega $\Omega$ notations. Analytic number theory often uses the big O , small o , Hardy's $\asymp$ , Hardy–Littlewood's big Omega $\Omega$ (with or without the +, − or ± subscripts), Vinogradov's $\ll$ and $\gg$ notations and $\sim$ notations. The small omega $\omega$ notation is not used as often in analysis or in number theory.

### Quality of approximations using different notation

Informally, especially in computer science, the big O notation often can be used somewhat differently to describe an asymptotic tight bound where using big Theta $\Theta$ notation might be more factually appropriate in a given context . For example, when considering a function $T(n)=73n^{3}+22n^{2}+58$ , all of the following are generally acceptable, but tighter bounds (such as numbers 2,3 and 4 below) are usually strongly preferred over looser bounds (such as number 1 below).

1. $T(n)=O(n^{100})$
2. $T(n)=O(n^{3})$
3. $T(n)=\Theta (n^{3})$
4. $T(n)\sim 73n^{3}$ as $n\to \infty$ .

While all three statements are true, progressively more information is contained in each. In some fields, however, the big O notation (number 2 in the lists above) would be used more commonly than the big Theta notation (items numbered 3 in the lists above). For example, if $T(n)$ represents the running time of a newly developed algorithm for input size n , the inventors and users of the algorithm might be more inclined to put an upper bound on how long it will take to run without making an explicit statement about the lower bound or asymptotic behavior.

### Extensions to the Bachmann–Landau notations

Another notation sometimes used in computer science is ${\tilde {O}}$ (read *soft-O*), which hides polylogarithmic factors. There are two definitions in use: some authors use $f(n)={\tilde {O}}(g(n))$ as shorthand for $f(n)=O(g(n)\log ^{k}n)$ for some k , while others use it as shorthand for $f(n)=O(g(n)\log ^{k}g(n))$ . When $g(n)$ is polynomial in n , there is no difference; however, the latter definition allows one to say, e.g. that $n2^{n}={\tilde {O}}(2^{n})$ while the former definition allows for $\log ^{k}n={\tilde {O}}(1)$ for any constant k . Some authors write *O** for the same purpose as the latter definition. Essentially, it is less precise version of the big *O* notation, ignoring logarithmic factors in the growth-rate of the function. Since $\log ^{k}n=o(n^{\varepsilon })$ for any constant k and any $\varepsilon >0$ , logarithmic factors are far less significant than powers of n and even more insignificant compared with exponentials.

Also, the *L* notation, defined as

$L_{n}[\alpha ,c]=e^{(c+o(1))(\ln n)^{\alpha }(\ln \ln n)^{1-\alpha }},$

is convenient for functions that are between polynomial and exponential in terms of $\log n$ .

The generalization to functions taking values in any normed vector space is straightforward (replacing absolute values by norms), where f and g need not take their values in the same space. A generalization to functions g taking values in any topological group is also possible. The "limiting process" $x\to x_{0}$ can also be generalized by introducing an arbitrary filter base, i.e. to directed nets f and g . The o notation can be used to define derivatives and differentiability in quite general spaces, and also (asymptotical) equivalence of functions,

$f\sim g\iff (f-g)\in o(g)$

which is an equivalence relation and a more restrictive notion than the relationship " f is $\Theta (g)$ " from above. (It reduces to $\lim f/g=1$ if f and g are positive real valued functions.) For example, $2x=\Theta (x)$ is, but $2x-x\neq o(x)$ .

## History

In 1870, Paul du Bois-Reymond defined $f(x)\succ \phi (x)$ , $f(x)\sim \phi (x)$ and $f(x)\prec \phi (x)$ to mean, respectively, $\lim _{x\to \infty }{\frac {f(x)}{\phi (x)}}=\infty ,\quad \lim _{x\to \infty }{\frac {f(x)}{\phi (x)}}>0,\quad \lim _{x\to \infty }{\frac {f(x)}{\phi (x)}}=0.$ These were not widely adopted and are not used today. The first and third are symmetric: $f(x)\prec \phi (x)$ means the same as $\phi (x)\succ f(x)$ . Landau later adopted $\sim$ with the narrower definition that the limit of $f(x)/\phi (x)$ equals 1.

The symbol O was first introduced by the number theorist Paul Bachmann in 1894, in the second volume of his book *Analytische Zahlentheorie* ("analytic number theory"). The number theorist Edmund Landau adopted it, and was thus inspired to introduce in 1909 the notation o; hence both are now called Landau symbols. These notations were used in applied mathematics during the 1950s for asymptotic analysis. The symbol $\Omega$ (in the sense "is not little *o* of") was introduced in 1914 by Hardy and Littlewood. Hardy and Littlewood also introduced in 1916 the left and right $\Omega$ symbols $\Omega _{R}$ , $\Omega _{L}$ (now commonly denoted $\Omega _{+},\Omega _{-}$ ). This $\Omega$ notation has been commonly used in number theory since the 1950s.

Hardy introduced the symbols $\preccurlyeq$ and advocated for Bois-Reymond's $\prec$ (as well as the already mentioned other symbols) in his 1910 tract "Orders of Infinity", but made use of them only in three papers (1910–1913). In his nearly 400 remaining papers and books he consistently used the Landau symbols O and o. Hardy's symbols $\preccurlyeq$ and $\mathbin {\,\asymp \;\;\;\;\!\!\!\!\!\!\!\!\!\!\!\!\!-}$ are not used any more.

The symbol $\sim$ , although it had been used before with different meanings, was given its modern definition by Landau in 1909 and by Hardy in 1910. On the same page, Hardy defined the symbol $\asymp$ , where $f(x)\asymp g(x)$ means that both $f(x)=O(g(x))$ and $g(x)=O(f(x))$ are satisfied. The notation is still used in analytic number theory. Hardy also proposed the symbol $\mathbin {\,\asymp \;\;\;\;\!\!\!\!\!\!\!\!\!\!\!\!\!-}$ , where $f\mathbin {\,\asymp \;\;\;\;\!\!\!\!\!\!\!\!\!\!\!\!\!-} g$ means that $f\sim Kg$ for some constant $K\not =0$ (this corresponds to Bois-Reymond's notation $f\sim g$ ).

In the 1930s, Vinogradov popularized the notation $f(x)\ll g(x)$ and $g(x)\gg f(x)$ , both of which mean $f(x)=O(g(x))$ . This notation became standard in analytic number theory.

In the 1970s, big O was popularized in computer science by Donald Knuth, who proposed the different notation $f(x)=\Theta (g(x))$ for Hardy's $f(x)\asymp g(x)$ , and proposed a different definition for the Hardy and Littlewood Omega notation.

## Matters of notation

### Arrows

In mathematics, an expression such as $x\to \infty$ indicates the presence of a limit. In big-O notation and related notations $\Omega ,\Theta ,\gg ,\ll ,\asymp$ , there is no implied limit, in contrast with little-o, $\sim$ and $\omega$ notations. Notation such as $f(x)=O(g(x))\;\;(x\to \infty )$ can be considered an abuse of notation.

### Equals sign

Some consider $f(x)=O(g(x))$ to also be an abuse of notation, since the use of the equals sign could be misleading as it suggests a symmetry that this statement does not have. As de Bruijn says, $O(x)=O(x^{2})$ is true but $O(x^{2})=O(x)$ is not. Knuth describes such statements as "one-way equalities", since if the sides could be reversed, "we could deduce ridiculous things like $n=n^{2}$ from the identities $n=O(n^{2})$ and $n^{2}=O(n^{2})$ . In another letter, Knuth also pointed out that

> the equality sign is not symmetric with respect to such notations [as, in this notation,] mathematicians customarily use the '=' sign as they use the word 'is' in English: Aristotle is a man, but a man isn't necessarily Aristotle.

For these reasons, some advocate for using set notation and write $f(x)\in O(g(x))$ , read as " $f(x)$ is an element of $O(g(x))$ ", or " $f(x)$ is in the set $O(g(x))$ " – thinking of $O(g(x))$ as the class of all functions $h(x)$ such that $h(x)=O(g(x))$ . However, the use of the equals sign is customary. and is more convenient in more complex expressions of the form $f(x)=g(x)+O(h(x))=O(k(x)).$

The Vinogradov notations $\ll$ and $\gg$ , which are widely used in number theory do not suffer from this defect, as they more clearly indicate that big-O indicates an *inequality* rather than an *equality*. They also enjoy a symmetry that big-O notation lacks: $f(x)\ll g(x)$ means the same as $g(x)\gg f(x)$ . In combinatorics and computer science, these notations are rarely seen.

### Typesetting

Big O is typeset as an italicized uppercase "O", as in the following example: $O(n^{2})$ . In TeX, it is produced by simply typing 'O' inside math mode. Unlike Greek-named Bachmann–Landau notations, it needs no special symbol. However, some authors use the calligraphic variant ${\mathcal {O}}$ instead.

The big-O originally stands for "order of" ("Ordnung", Bachmann 1894), and is thus a Latin letter. Neither Bachmann nor Landau ever call it "Omicron". The symbol was much later on (1976) viewed by Knuth as a capital omicron, probably in reference to his definition of the symbol Omega. The digit zero should not be used.
