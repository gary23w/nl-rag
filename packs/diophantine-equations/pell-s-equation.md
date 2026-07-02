---
title: "Pell's equation"
source: https://en.wikipedia.org/wiki/Pell's_equation
domain: diophantine-equations
license: CC-BY-SA-4.0
tags: diophantine equation, pell's equation, fermat's last theorem, pythagorean triple
fetched: 2026-07-02
---

# Pell's equation

**Pell's equation**, also called the **Pell–Fermat equation**, is any Diophantine equation of the form $x^{2}-ny^{2}=1,$ where *n* is a given positive nonsquare integer, and integer solutions are sought for *x* and *y*. In Cartesian coordinates, the equation is represented by a hyperbola; solutions occur wherever the curve passes through a point whose *x* and *y* coordinates are both integers, such as the trivial solution with *x* = 1 and *y* = 0. Joseph Louis Lagrange proved that, as long as *n* is not a perfect square, Pell's equation has infinitely many distinct integer solutions. These solutions may be used to accurately approximate the square root of *n* by rational numbers of the form *x*/*y*.

This kind of equation was first studied extensively in India starting with Brahmagupta, who found an integer solution to $92x^{2}+1=y^{2}$ in his *Brāhmasphuṭasiddhānta* circa 628. Bhaskara II in the 12th century and Narayana Pandit in the 14th century both found general solutions to Pell's equation and other quadratic indeterminate equations. Bhaskara II is generally credited with developing the *chakravala* method, building on the work of Jayadeva and Brahmagupta. Solutions to specific examples of Pell's equation, such as the Pell numbers arising from the equation with *n* = 2, had been known for much longer, since the time of Pythagoras in Greece and a similar date in India. William Brouncker was the first European to solve Pell's equation. The name of Pell's equation arose from Leonhard Euler mistakenly attributing Brouncker's solution of the equation to John Pell.

## History

### Special cases

As early as 400 BC in India and Greece, mathematicians studied the numbers arising from the *n* = 2 case of Pell's equation, $x^{2}-2y^{2}=1,$ and from the closely related equation $x^{2}-2y^{2}=-1$ because of the connection of these equations to the square root of 2. Indeed, if *x* and *y* are positive integers satisfying this equation, then *x*/*y* is an approximation of √2. The numbers *x* and *y* appearing in these approximations, called side and diameter numbers, were known to the Pythagoreans, and Proclus observed that in the opposite direction these numbers obeyed one of these two equations. Similarly, Baudhayana discovered that *x* = 17, *y* = 12 and *x* = 577, *y* = 408 are two solutions to the Pell equation, and that 17/12 and 577/408 are very close approximations to the square root of 2.

Later, Archimedes approximated the square root of 3 by the rational number 1351/780. Although he did not explain his methods, this approximation may be obtained in the same way, as a solution to Pell's equation. Likewise, Archimedes's cattle problem—an ancient word problem about finding the number of cattle belonging to the sun god Helios—can be solved by reformulating it as a Pell's equation. The manuscript containing the problem states that it was devised by Archimedes and recorded in a letter to Eratosthenes, and the attribution to Archimedes is generally accepted today.

### General case

Around AD 250, Diophantus considered the equation $a^{2}x^{2}+c=y^{2},$ where *a* and *c* are fixed numbers, and *x* and *y* are the variables to be solved for. This equation is different in form from Pell's equation but equivalent to it. Diophantus solved the equation for (*a*, *c*) equal to (1, 1), (1, −1), (1, 12), and (3, 9). Al-Karaji, a 10th-century Persian mathematician, worked on similar problems to Diophantus.

In Indian mathematics, Brahmagupta discovered that $(x_{1}^{2}-Ny_{1}^{2})(x_{2}^{2}-Ny_{2}^{2})=(x_{1}x_{2}+Ny_{1}y_{2})^{2}-N(x_{1}y_{2}+x_{2}y_{1})^{2},$ a form of what is now known as Brahmagupta's identity. Using this, he was able to "compose" triples $(x_{1},y_{1},k_{1})$ and $(x_{2},y_{2},k_{2})$ that were solutions of $x^{2}-Ny^{2}=k$ , to generate the new triples

$(x_{1}x_{2}+Ny_{1}y_{2},x_{1}y_{2}+x_{2}y_{1},k_{1}k_{2})$

and

$(x_{1}x_{2}-Ny_{1}y_{2},x_{1}y_{2}-x_{2}y_{1},k_{1}k_{2}).$

Not only did this give a way to generate infinitely many solutions to $x^{2}-Ny^{2}=1$ starting with one solution, but also, by dividing such a composition by $k_{1}k_{2}$ , integer or "nearly integer" solutions could often be obtained. For instance, for $N=92$ , Brahmagupta composed the triple (10, 1, 8) (since $10^{2}-92(1^{2})=8$ ) with itself to get the new triple (192, 20, 64). Dividing throughout by 64 ("8" for x and y ) gave the triple (24, 5/2, 1), which when composed with itself gave the desired integer solution (1151, 120, 1). Brahmagupta solved many Pell's equations with this method, proving that it gives solutions starting from an integer solution of $x^{2}-Ny^{2}=k$ for *k* = ±1, ±2, or ±4.

The first general method for solving the Pell's equation (for all *N*) was given by Bhāskara II in 1150, extending the methods of Brahmagupta. Called the chakravala (cyclic) method, it starts by choosing two relatively prime integers a and b , then composing the triple $(a,b,k)$ (that is, one which satisfies $a^{2}-Nb^{2}=k$ ) with the trivial triple $(m,1,m^{2}-N)$ to get the triple ${\big (}am+Nb,a+bm,k(m^{2}-N){\big )}$ , which can be scaled down to $\left({\frac {am+Nb}{k}},{\frac {a+bm}{k}},{\frac {m^{2}-N}{k}}\right).$

When m is chosen so that ${\frac {a+bm}{k}}$ is an integer, so are the other two numbers in the triple. Among such m , the method chooses one that minimizes ${\frac {m^{2}-N}{k}}$ and repeats the process. This method always terminates with a solution. Bhaskara used it to give the solution *x* = 1766319049, *y* = 226153980 to the *N* = 61 case.

Several European mathematicians rediscovered how to solve Pell's equation in the 17th century. Pierre de Fermat found how to solve the equation and in a 1657 letter issued it as a challenge to English mathematicians. In a letter to Kenelm Digby, Bernard Frénicle de Bessy said that Fermat found the smallest solution for *N* up to 150 and challenged John Wallis to solve the cases *N* = 151 or 313. Both Wallis and William Brouncker gave solutions to these problems, though Wallis suggests in a letter that the solution was due to Brouncker.

John Pell's connection with the equation is that he revised Thomas Branker's translation of Johann Rahn's 1659 book *Teutsche Algebra* into English, with a discussion of Brouncker's solution of the equation. Leonhard Euler mistakenly thought that this solution was due to Pell, as a result of which he named the equation after Pell.

The general theory of Pell's equation, based on continued fractions and algebraic manipulations with numbers of the form $P+Q{\sqrt {a}},$ was developed by Lagrange in 1766–1769. In particular, Lagrange gave a proof that the Brouncker–Wallis algorithm always terminates.

## Solutions

### Fundamental solution via continued fractions

Let $h_{i}/k_{i}$ denote the unique sequence of convergents of the regular continued fraction for ${\sqrt {n}}$ . Then the pair of positive integers $(x_{1},y_{1})$ solving Pell's equation and minimizing *x* satisfies *x*1 = *hi* and *y*1 = *ki* for some *i*. This pair is called the *fundamental solution*. The sequence of integers $[a_{0};a_{1},a_{2},\ldots ]$ in the regular continued fraction of ${\sqrt {n}}$ is always eventually periodic. It can be written in the form $\left[\lfloor {\sqrt {n}}\rfloor ;\;{\overline {a_{1},a_{2},\ldots ,a_{r-1},2\lfloor {\sqrt {n}}\rfloor }}\right]$ , where $\lfloor \,\cdot \,\rfloor$ denotes integer floor, and the sequence $a_{1},a_{2},\ldots ,a_{r-1},2\lfloor {\sqrt {n}}\rfloor$ repeats infinitely. Moreover, the tuple $(a_{1},a_{2},\ldots ,a_{r-1})$ is palindromic, the same left-to-right or right-to-left.

The fundamental solution is $(x_{1},y_{1})={\begin{cases}(h_{r-1},k_{r-1}),&{\text{ for }}r{\text{ even}}\\(h_{2r-1},k_{2r-1}),&{\text{ for }}r{\text{ odd}}\end{cases}}$

The computation time for finding the fundamental solution using the continued fraction method, with the aid of the Schönhage–Strassen algorithm for fast integer multiplication, is within a logarithmic factor of the solution size, the number of digits in the pair $(x_{1},y_{1})$ . However, this is not a polynomial-time algorithm because the number of digits in the solution may be as large as ${\sqrt {n}}$ , far larger than a polynomial in the number of digits in the input value *n*.

### Additional solutions from the fundamental solution

Once the fundamental solution is found, all remaining solutions may be calculated algebraically from $x_{k}+y_{k}{\sqrt {n}}=(x_{1}+y_{1}{\sqrt {n}})^{k},$ expanding the right side, equating coefficients of ${\sqrt {n}}$ on both sides, and equating the other terms on both sides. This yields the recurrence relations $x_{k+1}=x_{1}x_{k}+ny_{1}y_{k},$ $y_{k+1}=x_{1}y_{k}+y_{1}x_{k}.$

### Concise representation and faster algorithms

Although writing out the fundamental solution (*x*1, *y*1) as a pair of binary numbers may require a large number of bits, it may in many cases be represented more compactly in the form $x_{1}+y_{1}{\sqrt {n}}=\prod _{i=1}^{t}\left(a_{i}+b_{i}{\sqrt {n}}\right)^{c_{i}}$ using much smaller integers *a**i*, *b**i*, and *c**i*.

For instance, Archimedes' cattle problem is equivalent to the Pell equation $x^{2}-410\,286\,423\,278\,424\ y^{2}=1$ , the fundamental solution of which has 206545 digits if written out explicitly. However, the solution is also equal to $x_{1}+y_{1}{\sqrt {n}}=u^{2329},$ where $u=x'_{1}+y'_{1}{\sqrt {4\,729\,494}}=(300\,426\,607\,914\,281\,713\,365\ {\sqrt {609}}+84\,129\,507\,677\,858\,393\,258\ {\sqrt {7766}})^{2}$ and $x'_{1}$ and $y'_{1}$ only have 45 and 41 decimal digits respectively.

Methods related to the quadratic sieve approach for integer factorization may be used to collect relations between prime numbers in the number field generated by ${\sqrt {n}}$ and to combine these relations to find a product representation of this type. The resulting algorithm for solving Pell's equation is more efficient than the continued fraction method, though it still takes more than polynomial time. Under the assumption of the generalized Riemann hypothesis, it can be shown to take time $\exp O\left({\sqrt {\log N\cdot \log \log N}}\right),$ where *N* = log *n* is the input size, similarly to the quadratic sieve.

### Quantum algorithms

Hallgren showed that a quantum computer can find a product representation, as described above, for the solution to Pell's equation in polynomial time. Hallgren's algorithm, which can be interpreted as an algorithm for finding the group of units of a real quadratic number field, was extended to more general fields by Schmidt and Völlmer.

## Example

As an example, consider the instance of Pell's equation for *n* = 7; that is, $x^{2}-7y^{2}=1.$ The continued fraction of ${\sqrt {7}}$ has the form $[2;\ {\overline {1,1,1,4}}]$ . Since the period has length 4 , which is an even number, the convergent producing the fundamental solution is obtained by truncating the continued fraction right before the end of the first occurrence of the period: $[2;\ 1,1,1]={\frac {8}{3}}$ .

The sequence of convergents for the square root of seven are

| $h/k$ (convergent) | $h^{2}-7k^{2}$ (Pell-type approximation) |
|---|---|
| $2/1$ | $-3$ |
| $3/1$ | $+2$ |
| $5/2$ | $-3$ |
| $8/3$ | $+1$ |

Applying the recurrence formula to this solution generates the infinite sequence of solutions

(1, 0); (8, 3); (127, 48); (2024, 765); (32257, 12192); (514088, 194307); (8193151, 3096720); (130576328, 49353213); ... (sequence

A001081

(

x

) and

A001080

(

y

) in

OEIS

)

For the Pell's equation $x^{2}-13y^{2}=1,$ the continued fraction ${\sqrt {13}}=[3;\ {\overline {1,1,1,1,6}}]$ has a period of odd length. For this the fundamental solution is obtained by truncating the continued fraction right before the second occurrence of the period $[3;\ 1,1,1,1,6,1,1,1,1]={\frac {649}{180}}$ . Thus, the fundamental solution is $(x_{1},y_{1})=(649,180)$ .

The smallest solution can be very large. For example, the smallest solution to $x^{2}-313y^{2}=1$ is (32188120829134849, 1819380158564160), and this is the equation which Frenicle challenged Wallis to solve. Values of *n* such that the smallest solution of $x^{2}-ny^{2}=1$ is greater than the smallest solution for any smaller value of *n* are

1, 2, 5, 10, 13, 29, 46, 53, 61, 109, 181, 277, 397, 409, 421, 541, 661, 1021, 1069, 1381, 1549, 1621, 2389, 3061, 3469, 4621, 4789, 4909, 5581, 6301, 6829, 8269, 8941, 9949, ... (sequence

A033316

in the

OEIS

).

(For these records, see (sequence A033315 in the OEIS) for *x* and (sequence A033319 in the OEIS) for *y*.)

## List of fundamental solutions of Pell's equations

The following is a list of the fundamental solution to $x^{2}-ny^{2}=1$ with *n* ≤ 128. When *n* is an integer square, there is no solution except for the trivial solution (1, 0). The values of *x* are sequence A002350 and those of *y* are sequence A002349 in OEIS.

| *n* | *x* | *y* |
|---|---|---|
| 1 | – | – |
| 2 | 3 | 2 |
| 3 | 2 | 1 |
| 4 | – | – |
| 5 | 9 | 4 |
| 6 | 5 | 2 |
| 7 | 8 | 3 |
| 8 | 3 | 1 |
| 9 | – | – |
| 10 | 19 | 6 |
| 11 | 10 | 3 |
| 12 | 7 | 2 |
| 13 | 649 | 180 |
| 14 | 15 | 4 |
| 15 | 4 | 1 |
| 16 | – | – |
| 17 | 33 | 8 |
| 18 | 17 | 4 |
| 19 | 170 | 39 |
| 20 | 9 | 2 |
| 21 | 55 | 12 |
| 22 | 197 | 42 |
| 23 | 24 | 5 |
| 24 | 5 | 1 |
| 25 | – | – |
| 26 | 51 | 10 |
| 27 | 26 | 5 |
| 28 | 127 | 24 |
| 29 | 9801 | 1820 |
| 30 | 11 | 2 |
| 31 | 1520 | 273 |
| 32 | 17 | 3 |

| *n* | *x* | *y* |
|---|---|---|
| 33 | 23 | 4 |
| 34 | 35 | 6 |
| 35 | 6 | 1 |
| 36 | – | – |
| 37 | 73 | 12 |
| 38 | 37 | 6 |
| 39 | 25 | 4 |
| 40 | 19 | 3 |
| 41 | 2049 | 320 |
| 42 | 13 | 2 |
| 43 | 3482 | 531 |
| 44 | 199 | 30 |
| 45 | 161 | 24 |
| 46 | 24335 | 3588 |
| 47 | 48 | 7 |
| 48 | 7 | 1 |
| 49 | – | – |
| 50 | 99 | 14 |
| 51 | 50 | 7 |
| 52 | 649 | 90 |
| 53 | 66249 | 9100 |
| 54 | 485 | 66 |
| 55 | 89 | 12 |
| 56 | 15 | 2 |
| 57 | 151 | 20 |
| 58 | 19603 | 2574 |
| 59 | 530 | 69 |
| 60 | 31 | 4 |
| 61 | 1766319049 | 226153980 |
| 62 | 63 | 8 |
| 63 | 8 | 1 |
| 64 | – | – |

| *n* | *x* | *y* |
|---|---|---|
| 65 | 129 | 16 |
| 66 | 65 | 8 |
| 67 | 48842 | 5967 |
| 68 | 33 | 4 |
| 69 | 7775 | 936 |
| 70 | 251 | 30 |
| 71 | 3480 | 413 |
| 72 | 17 | 2 |
| 73 | 2281249 | 267000 |
| 74 | 3699 | 430 |
| 75 | 26 | 3 |
| 76 | 57799 | 6630 |
| 77 | 351 | 40 |
| 78 | 53 | 6 |
| 79 | 80 | 9 |
| 80 | 9 | 1 |
| 81 | – | – |
| 82 | 163 | 18 |
| 83 | 82 | 9 |
| 84 | 55 | 6 |
| 85 | 285769 | 30996 |
| 86 | 10405 | 1122 |
| 87 | 28 | 3 |
| 88 | 197 | 21 |
| 89 | 500001 | 53000 |
| 90 | 19 | 2 |
| 91 | 1574 | 165 |
| 92 | 1151 | 120 |
| 93 | 12151 | 1260 |
| 94 | 2143295 | 221064 |
| 95 | 39 | 4 |
| 96 | 49 | 5 |

| *n* | *x* | *y* |
|---|---|---|
| 97 | 62809633 | 6377352 |
| 98 | 99 | 10 |
| 99 | 10 | 1 |
| 100 | – | – |
| 101 | 201 | 20 |
| 102 | 101 | 10 |
| 103 | 227528 | 22419 |
| 104 | 51 | 5 |
| 105 | 41 | 4 |
| 106 | 32080051 | 3115890 |
| 107 | 962 | 93 |
| 108 | 1351 | 130 |
| 109 | 158070671986249 | 15140424455100 |
| 110 | 21 | 2 |
| 111 | 295 | 28 |
| 112 | 127 | 12 |
| 113 | 1204353 | 113296 |
| 114 | 1025 | 96 |
| 115 | 1126 | 105 |
| 116 | 9801 | 910 |
| 117 | 649 | 60 |
| 118 | 306917 | 28254 |
| 119 | 120 | 11 |
| 120 | 11 | 1 |
| 121 | – | – |
| 122 | 243 | 22 |
| 123 | 122 | 11 |
| 124 | 4620799 | 414960 |
| 125 | 930249 | 83204 |
| 126 | 449 | 40 |
| 127 | 4730624 | 419775 |
| 128 | 577 | 51 |

## Connections

Pell's equation has connections to several other important subjects in mathematics.

### Algebraic number theory

Pell's equation is closely related to the theory of algebraic numbers, as the formula $x^{2}-ny^{2}=(x+y{\sqrt {n}})(x-y{\sqrt {n}})$ is the norm for the ring $\mathbb {Z} [{\sqrt {n}}]$ and for the closely related quadratic field $\mathbb {Q} ({\sqrt {n}})$ . Thus, a pair of integers $(x,y)$ solves Pell's equation if and only if $x+y{\sqrt {n}}$ is a unit with norm 1 in $\mathbb {Z} [{\sqrt {n}}]$ . Dirichlet's unit theorem, that all units of $\mathbb {Z} [{\sqrt {n}}]$ can be expressed as powers of a single fundamental unit (and multiplication by a sign), is an algebraic restatement of the fact that all solutions to the Pell's equation can be generated from the fundamental solution. The fundamental unit can in general be found by solving a Pell-like equation but it does not always correspond directly to the fundamental solution of Pell's equation itself, because the fundamental unit may have norm −1 rather than 1 and its coefficients may be half integers rather than integers.

### Chebyshev polynomials

Demeyer mentions a connection between Pell's equation and the Chebyshev polynomials: If $T_{i}(x)$ and $U_{i}(x)$ are the Chebyshev polynomials of the first and second kind respectively, then these polynomials satisfy a form of Pell's equation in any polynomial ring $R[x]$ , with $n=x^{2}-1$ : $T_{i}^{2}-(x^{2}-1)U_{i-1}^{2}=1.$ Thus, these polynomials can be generated by the standard technique for Pell's equations of taking powers of a fundamental solution: $T_{i}+U_{i-1}{\sqrt {x^{2}-1}}=(x+{\sqrt {x^{2}-1}})^{i}.$ It may further be observed that if $(x_{i},y_{i})$ are the solutions to any integer Pell's equation, then $x_{i}=T_{i}(x_{1})$ and $y_{i}=y_{1}U_{i-1}(x_{1})$ .

### Continued fractions

A general development of solutions of Pell's equation $x^{2}-ny^{2}=1$ in terms of continued fractions of ${\sqrt {n}}$ can be presented, as the solutions *x* and *y* are approximates to the square root of *n* and thus are a special case of continued fraction approximations for quadratic irrationals.

The relationship to the continued fractions implies that the solutions to Pell's equation form a semigroup subset of the modular group. Thus, for example, if *p* and *q* satisfy Pell's equation, then ${\begin{pmatrix}p&q\\nq&p\end{pmatrix}}$ is a matrix of unit determinant. Products of such matrices take exactly the same form, and thus all such products yield solutions to Pell's equation. This can be understood in part to arise from the fact that successive convergents of a continued fraction share the same property: If *p**k*−1/*q**k*−1 and *p**k*/*q**k* are two successive convergents of a continued fraction, then the matrix ${\begin{pmatrix}p_{k-1}&p_{k}\\q_{k-1}&q_{k}\end{pmatrix}}$

has determinant (−1)*k*.

### Smooth numbers

Størmer's theorem applies Pell equations to find pairs of consecutive smooth numbers, positive integers whose prime factors are all smaller than a given value. As part of this theory, Størmer also investigated divisibility relations among solutions to Pell's equation; in particular, he showed that each solution other than the fundamental solution has a prime factor that does not divide *n*.

## The negative Pell's equation

The negative Pell's equation is given by $x^{2}-ny^{2}=-1$ and has also been extensively studied. It can be solved by the same method of continued fractions and has solutions if and only if the period of the continued fraction has odd length. A necessary (but not sufficient) condition for solvability is that *n* is not divisible by 4 or by a prime of form 4*k* + 3. Thus, for example, *x*2 − 3 *y*2 = −1 is never solvable, but *x*2 − 5 *y*2 = −1 may be.

The first few numbers *n* for which *x*2 − *n y*2 = −1 is solvable are 1 (with only one trivial solution) and

2, 5, 10, 13, 17, 26, 29, 37, 41, 50, 53, 58, 61, 65, 73, 74, 82, 85, 89, 97, ... (sequence

A031396

in the

OEIS

)

with infinitely many solutions. The solutions of the negative Pell's equation for $1\leq n\leq 298$ are:

| *n* | *x* | *y* |
|---|---|---|
| 1 | 0 | 1 |
| 2 | 1 | 1 |
| 5 | 2 | 1 |
| 10 | 3 | 1 |
| 13 | 18 | 5 |
| 17 | 4 | 1 |
| 26 | 5 | 1 |
| 29 | 70 | 13 |
| 37 | 6 | 1 |
| 41 | 32 | 5 |
| 50 | 7 | 1 |
| 53 | 182 | 25 |
| 58 | 99 | 13 |
| 61 | 29718 | 3805 |
| 65 | 8 | 1 |
| 73 | 1068 | 125 |
| 74 | 43 | 5 |
| 82 | 9 | 1 |

| *n* | *x* | *y* |
|---|---|---|
| 85 | 378 | 41 |
| 89 | 500 | 53 |
| 97 | 5604 | 569 |
| 101 | 10 | 1 |
| 106 | 4005 | 389 |
| 109 | 8890182 | 851525 |
| 113 | 776 | 73 |
| 122 | 11 | 1 |
| 125 | 682 | 61 |
| 130 | 57 | 5 |
| 137 | 1744 | 149 |
| 145 | 12 | 1 |
| 149 | 113582 | 9305 |
| 157 | 4832118 | 385645 |
| 170 | 13 | 1 |
| 173 | 1118 | 85 |
| 181 | 1111225770 | 82596761 |
| 185 | 68 | 5 |

| *n* | *x* | *y* |
|---|---|---|
| 193 | 1764132 | 126985 |
| 197 | 14 | 1 |
| 202 | 3141 | 221 |
| 218 | 251 | 17 |
| 226 | 15 | 1 |
| 229 | 1710 | 113 |
| 233 | 23156 | 1517 |
| 241 | 71011068 | 4574225 |
| 250 | 4443 | 281 |
| 257 | 16 | 1 |
| 265 | 6072 | 373 |
| 269 | 82 | 5 |
| 274 | 1407 | 85 |
| 277 | 8920484118 | 535979945 |
| 281 | 1063532 | 63445 |
| 290 | 17 | 1 |
| 293 | 2482 | 145 |
| 298 | 409557 | 23725 |

Let $\alpha =\Pi _{j{\text{ is odd}}}(1-2^{j})$ . The proportion of square-free *n* divisible by *k* primes of the form 4*m* + 1 for which the negative Pell's equation is solvable is at least *α*. When the number of prime divisors is not fixed, the proportion is given by 1 − *α.*

If the negative Pell's equation does have a solution for a particular *n*, its fundamental solution leads to the fundamental one for the positive case by squaring both sides of the defining equation: $(x^{2}-ny^{2})^{2}=(-1)^{2}$ implies $(x^{2}+ny^{2})^{2}-n(2xy)^{2}=1.$

As stated above, if the negative Pell's equation is solvable, a solution can be found using the method of continued fractions as in the positive Pell's equation. The recursion relation works slightly differently however. Since $(x+y{\sqrt {n}})(x-y{\sqrt {n}})=-1$ , the next solution is determined in terms of $i(x_{k}+y_{k}{\sqrt {n}})=(i(x+y{\sqrt {n}}))^{k}$ whenever there is a match, that is, when k is odd. The resulting recursion relation is (modulo a minus sign, which is immaterial due to the quadratic nature of the equation) $x_{k}=x_{k-2}x_{1}^{2}+nx_{k-2}y_{1}^{2}+2ny_{k-2}y_{1}x_{1},$ $y_{k}=y_{k-2}x_{1}^{2}+ny_{k-2}y_{1}^{2}+2x_{k-2}y_{1}x_{1},$ which gives an infinite tower of solutions to the negative Pell's equation (except for $n=1$ ).

## Generalized Pell's equation

The equation $x^{2}-ny^{2}=N$ is called the **generalized** (or **general**) **Pell's equation**. The equation $\textstyle u^{2}-nv^{2}=1$ is the corresponding **Pell's resolvent**. A recursive algorithm was given by Lagrange in 1768 for solving the equation, reducing the problem to the case $|N|<{\sqrt {n}}$ . Such solutions can be derived using the continued-fractions method as outlined above.

If $(x_{0},y_{0})$ is a solution to $\textstyle x^{2}-ny^{2}=N,$ and $(u_{k},v_{k})$ is a solution to $\textstyle u^{2}-nv^{2}=1,$ then $(x_{k},y_{k})$ such that $x_{k}+y_{k}{\sqrt {n}}={\big (}x_{0}+y_{0}{\sqrt {n}}{\big )}{\big (}u_{k}+v_{k}{\sqrt {n}}{\big )}$ is a solution to $\textstyle x^{2}-ny^{2}=N$ , a principle named the *multiplicative principle*. The solution $(x_{k},y_{k})$ is called a *Pell multiple* of the solution $(x_{0},y_{0})$ .

There exists a finite set of solutions to $\textstyle x^{2}-ny^{2}=N$ such that every solution is a Pell multiple of a solution from that set. In particular, if $(u,v)$ is the fundamental solution to $\textstyle u^{2}-nv^{2}=1$ , then each solution to the equation is a Pell multiple of a solution $(x,y)$ with $\textstyle |x|\leq {\tfrac {1}{2}}{\sqrt {|N|}}\left({\sqrt {|U|}}+1\right)$ and $\textstyle |y|\leq {\tfrac {1}{2{\sqrt {n}}}}{\sqrt {|N|}}\left({\sqrt {|U|}}+1\right)$ , where $U=u+v{\sqrt {n}}$ .

If *x* and *y* are positive integer solutions to the Pell's equation with $|N|<{\sqrt {n}}$ , then $x/y$ is a convergent to the continued fraction of ${\sqrt {n}}$ .

Solutions to the generalized Pell's equation are used for solving certain Diophantine equations and units of certain rings, and they arise in the study of SIC-POVMs in quantum information theory.

The equation $x^{2}-ny^{2}=4$ is similar to the resolvent $\textstyle x^{2}-ny^{2}=1$ in that if a minimal solution to $\textstyle x^{2}-ny^{2}=4$ can be found, then all solutions of the equation can be generated in a similar manner to the case $N=1$ . For certain n , solutions to $\textstyle x^{2}-ny^{2}=1$ can be generated from those with $\textstyle x^{2}-ny^{2}=4$ , in that if $n\equiv 5{\pmod {8}},$ then every third solution to $\textstyle x^{2}-ny^{2}=4$ has $x,y$ even, generating a solution to $\textstyle x^{2}-ny^{2}=1$ .
