---
title: "Ackermann function"
source: https://en.wikipedia.org/wiki/Ackermann_function
domain: union-find-algorithm
license: CC-BY-SA-4.0
tags: disjoint set data structure, union by rank, amortized analysis, connected components
fetched: 2026-07-02
---

# Ackermann function

In computability theory, the **Ackermann function**, named after Wilhelm Ackermann, is one of the simplest and earliest-discovered examples of a total computable function that is not primitive recursive. All primitive recursive functions are total and computable, but the Ackermann function illustrates that not all total computable functions are primitive recursive. It is essentially constructed by diagonalizing a sequence of primitive recursive functions $f_{1},f_{2},\dots$ selected from the Grzegorczyk hierarchy. This makes the Ackermann function the first limit point $f_{\omega }$ of the fast-growing hierarchy.

After Ackermann's publication of his function (which had three non-negative integer arguments), many authors modified it to suit various purposes, so that today "the Ackermann function" may refer to any of numerous variants of the original function. One common version is the two-argument **Ackermann–Péter function** developed by Rózsa Péter and Raphael Robinson. This function is defined from the recurrence relation $\operatorname {A} (m+1,n+1)=\operatorname {A} (m,\operatorname {A} (m+1,n))$ with appropriate base cases. Its value grows very rapidly; for example, $\operatorname {A} (4,2)$ results in $2^{65536}-3$ , an integer with 19,729 decimal digits.

## History

In the late 1920s, the mathematicians Gabriel Sudan and Wilhelm Ackermann, students of David Hilbert, were studying the foundations of computation. Both Sudan and Ackermann are credited with discovering total computable functions (termed simply "recursive" in some references) that are not primitive recursive. Sudan published the lesser-known Sudan function, then shortly afterwards and independently, in 1928, Ackermann published his function $\varphi$ (from Greek, the letter *phi*). Ackermann's three-argument function, $\varphi (m,n,p)$ , is defined such that for $p=0,1,2$ , it reproduces the basic operations of addition, multiplication, and exponentiation as

${\begin{aligned}\varphi (m,n,0)&=m+n\\\varphi (m,n,1)&=m\times n\\\varphi (m,n,2)&=m^{n}\end{aligned}}$

and for $p>2$ it extends these basic operations in a way that can be compared to the hyperoperations:

${\begin{aligned}\varphi (m,n,3)&=m[4](n+1)\\\varphi (m,n,p)&\gtrapprox m[p+1](n+1)&&{\text{for }}p>3\end{aligned}}$

(Aside from its historic role as a total-computable-but-not-primitive-recursive function, Ackermann's original function is seen to extend the basic arithmetic operations beyond exponentiation, although not as seamlessly as do variants of Ackermann's function that are specifically designed for that purpose—such as Goodstein's hyperoperation sequence.)

In *On the Infinite*, David Hilbert first hypothesized that the Ackermann function was not primitive recursive, but it was Ackermann, Hilbert's personal secretary and former student, who actually proved the hypothesis in his paper *On Hilbert's Construction of the Real Numbers*.

Rózsa Péter and Raphael Robinson later developed a two-variable version of the Ackermann function that became preferred by almost all authors.

The generalized hyperoperation sequence, e.g. $G(m,a,b)=a[m]b$ , is a version of the Ackermann function as well.

In 1963 R. Creighton Buck based an intuitive two-variable variant $\operatorname {F}$ on the hyperoperation sequence:

$\operatorname {F} (m,n)=2[m]n.$

Compared to most other versions, Buck's function has no unessential offsets:

${\begin{aligned}\operatorname {F} (0,n)&=2[0]n=n+1\\\operatorname {F} (1,n)&=2[1]n=2+n\\\operatorname {F} (2,n)&=2[2]n=2\times n\\\operatorname {F} (3,n)&=2[3]n=2^{n}\\\operatorname {F} (4,n)&=2[4]n=2^{2^{2^{{}^{.^{.^{{}_{.}2}}}}}}\\&\quad \vdots \end{aligned}}$

Many other versions of Ackermann function have been investigated.

## Definition

### Definition: as *m*-ary function

Ackermann's original three-argument function $\varphi (m,n,p)$ is defined recursively as follows for nonnegative integers $m,n,$ and p :

${\begin{aligned}\varphi (m,n,0)&=m+n\\\varphi (m,0,1)&=0\\\varphi (m,0,2)&=1\\\varphi (m,0,p)&=m&&{\text{for }}p>2\\\varphi (m,n,p)&=\varphi (m,\varphi (m,n-1,p),p-1)&&{\text{for }}n,p>0\end{aligned}}$

Of the various two-argument versions, the one developed by Péter and Robinson (called "the" Ackermann function by most authors) is defined for nonnegative integers m and n as follows:

${\begin{array}{lcl}\operatorname {A} (0,n)&=&n+1\\\operatorname {A} (m+1,0)&=&\operatorname {A} (m,1)\\\operatorname {A} (m+1,n+1)&=&\operatorname {A} (m,\operatorname {A} (m+1,n))\end{array}}$

The Ackermann function has also been expressed in relation to the hyperoperation sequence:

$A(m,n)={\begin{cases}n+1&m=0\\2[m](n+3)-3&m>0\\\end{cases}}$

or, written in Knuth's up-arrow notation (extended to integer indices $\geq -2$ ):

$A(m,n)={\begin{cases}n+1&m=0\\2\uparrow ^{m-2}(n+3)-3&m>0\\\end{cases}}$

or, equivalently, in terms of Buck's function F:

$A(m,n)={\begin{cases}n+1&m=0\\F(m,n+3)-3&m>0\\\end{cases}}$

By induction on m , one can show that $F(m,n)\leq A(m,n)$ for all $m,n\in \mathbb {N} _{0}$ .

### Definition: as iterated 1-ary function

Define $f^{n}$ as the *n*-th iterate of f :

${\begin{array}{rll}f^{0}(x)&=&x\\f^{n+1}(x)&=&f(f^{n}(x))\end{array}}$

Iteration is the process of composing a function with itself a certain number of times. Function composition is an associative operation, so $f(f^{n}(x))=f^{n}(f(x))$ .

Conceiving the Ackermann function as a sequence of unary functions, one can set $\operatorname {A} _{m}(n)=\operatorname {A} (m,n)$ .

The function then becomes a sequence $\operatorname {A} _{0},\operatorname {A} _{1},\operatorname {A} _{2},...$ of unary functions, defined from iteration:

${\begin{array}{lcl}\operatorname {A} _{0}(n)&=&n+1\\\operatorname {A} _{m+1}(n)&=&\operatorname {A} _{m}^{n+1}(1)\,.\end{array}}$

## Computation

### Computation by LOOP program

The functions $\operatorname {A} _{i}$ fit into the (finite-level) fast-growing hierarchy (FGH) of functions

${\begin{array}{lcl}\operatorname {FGH} _{0}(n)&=&n+1\\\operatorname {FGH} _{m+1}(n)&=&\operatorname {FGH} _{m}^{n}(n)\,.\end{array}}$

The following inequality holds: $\forall m>1,\forall n>1:\operatorname {A} _{m}(n)<\operatorname {FGH} _{m}(n)$

For fixed k , the function $\operatorname {FGH} _{k}(n)$ can be computed by a LOOP program of nesting depth k :

```mw
# INPUT (n)
LOOP n:                  # nesting depth: 1
    LOOP n:              # nesting depth: 2
        ...              # ...
            LOOP n:      # nesting depth: k
                n += 1   # 
# OUTPUT (n)
```

The function $\operatorname {A} _{k}(n)$ can also be computed by a LOOP-k program. (The program (schema) is not listed here.)

It is obvious that $\operatorname {A} (m,n)$ , not being a primitive recursive function —see below—, cannot be computed by a LOOP program.

### Computation by term rewriting system, based on 2-ary function

The recursive definition of the Ackermann function can naturally be transposed to a term rewriting system (TRS).

The definition of the **2-ary** Ackermann function leads to the obvious reduction rules

${\begin{array}{lll}{\text{(r1)}}&A(0,n)&\rightarrow &S(n)\\{\text{(r2)}}&A(S(m),0)&\rightarrow &A(m,S(0))\\{\text{(r3)}}&A(S(m),S(n))&\rightarrow &A(m,A(S(m),n))\end{array}}$

**Example**

Compute $A(1,2)\rightarrow _{*}4$

The reduction sequence is

| Leftmost-outermost (one-step) strategy: | Leftmost-innermost (one-step) strategy: |
|---|---|
| ${\underline {A(S(0),S(S(0)))}}$ | ${\underline {A(S(0),S(S(0)))}}$ |
| $\rightarrow _{r3}{\underline {A(0,A(S(0),S(0))}})$ | $\rightarrow _{r3}A(0,{\underline {A(S(0),S(0))}})$ |
| $\rightarrow _{r1}S({\underline {A(S(0),S(0))}})$ | $\rightarrow _{r3}A(0,A(0,{\underline {A(S(0),0)}}))$ |
| $\rightarrow _{r3}S({\underline {A(0,A(S0,0))}})$ | $\rightarrow _{r2}A(0,A(0,{\underline {A(0,S(0))}}))$ |
| $\rightarrow _{r1}S(S({\underline {A(S(0),0)}}))$ | $\rightarrow _{r1}A(0,{\underline {A(0,S(S(0)))}})$ |
| $\rightarrow _{r2}S(S({\underline {A(0,S(0))}}))$ | $\rightarrow _{r1}{\underline {A(0,S(S(S(0))))}}$ |
| $\rightarrow _{r1}S(S(S(S(0))))$ | $\rightarrow _{r1}S(S(S(S(0))))$ |

To compute $\operatorname {A} (m,n)$ one can use a stack, which initially contains the elements $\langle m,n\rangle$ .

Then repeatedly the two top elements are replaced according to the rules

${\begin{array}{lllllllll}{\text{(r1)}}&0&,&n&\rightarrow &(n+1)\\{\text{(r2)}}&(m+1)&,&0&\rightarrow &m&,&1\\{\text{(r3)}}&(m+1)&,&(n+1)&\rightarrow &m&,&(m+1)&,&n\end{array}}$

Schematically, starting from $\langle m,n\rangle$ :

```
WHILE stackLength <> 1
{
   POP 2 elements;
   PUSH 1 or 2 or 3 elements, applying the rules r1, r2, r3
}
```

The pseudocode is published in Grossman & Zeitman (1988).

For example, on input $\langle 2,1\rangle$ ,

| the stack configurations | reflect the reduction |
|---|---|
| ${\underline {2,1}}$ | ${\underline {A(2,1)}}$ |
| $\rightarrow 1,{\underline {2,0}}$ | $\rightarrow _{r1}A(1,{\underline {A(2,0)}})$ |
| $\rightarrow 1,{\underline {1,1}}$ | $\rightarrow _{r2}A(1,{\underline {A(1,1)}})$ |
| $\rightarrow 1,0,{\underline {1,0}}$ | $\rightarrow _{r3}A(1,A(0,{\underline {A(1,0)}}))$ |
| $\rightarrow 1,0,{\underline {0,1}}$ | $\rightarrow _{r2}A(1,A(0,{\underline {A(0,1)}}))$ |
| $\rightarrow 1,{\underline {0,2}}$ | $\rightarrow _{r1}A(1,{\underline {A(0,2)}})$ |
| $\rightarrow {\underline {1,3}}$ | $\rightarrow _{r1}{\underline {A(1,3)}}$ |
| $\rightarrow 0,{\underline {1,2}}$ | $\rightarrow _{r3}A(0,{\underline {A(1,2)}})$ |
| $\rightarrow 0,0,{\underline {1,1}}$ | $\rightarrow _{r3}A(0,A(0,{\underline {A(1,1)}}))$ |
| $\rightarrow 0,0,0,{\underline {1,0}}$ | $\rightarrow _{r3}A(0,A(0,A(0,{\underline {A(1,0)}})))$ |
| $\rightarrow 0,0,0,{\underline {0,1}}$ | $\rightarrow _{r2}A(0,A(0,A(0,{\underline {A(0,1)}})))$ |
| $\rightarrow 0,0,{\underline {0,2}}$ | $\rightarrow _{r1}A(0,A(0,{\underline {A(0,2)}}))$ |
| $\rightarrow 0,{\underline {0,3}}$ | $\rightarrow _{r1}A(0,{\underline {A(0,3)}})$ |
| $\rightarrow {\underline {0,4}}$ | $\rightarrow _{r1}{\underline {A(0,4)}}$ |
| $\rightarrow 5$ | $\rightarrow _{r1}5$ |

**Remarks**

- The leftmost-innermost strategy is implemented in 225 computer languages on Rosetta Code.
- For all $m,n$ the computation of $A(m,n)$ takes no more than $(A(m,n)+1)^{m}$ steps.
- Grossman & Zeitman (1988) pointed out that in the computation of $\operatorname {A} (m,n)$ the maximum length of the stack is $\operatorname {A} (m,n)$ , as long as $m>0$ . Their own algorithm, inherently iterative, computes $\operatorname {A} (m,n)$ within ${\mathcal {O}}(m\operatorname {A} (m,n))$ time and within ${\mathcal {O}}(m)$ space.

### Computation by TRS, based on iterated 1-ary function

The definition of the iterated **1-ary** Ackermann functions leads to different reduction rules

${\begin{array}{lll}{\text{(r4)}}&A(S(0),0,n)&\rightarrow &S(n)\\{\text{(r5)}}&A(S(0),S(m),n)&\rightarrow &A(S(n),m,S(0))\\{\text{(r6)}}&A(S(S(x)),m,n)&\rightarrow &A(S(0),m,A(S(x),m,n))\end{array}}$

As function composition is associative, instead of rule r6 one can define

${\begin{array}{lll}{\text{(r7)}}&A(S(S(x)),m,n)&\rightarrow &A(S(x),m,A(S(0),m,n))\end{array}}$

Like in the previous section the computation of $\operatorname {A} _{m}^{1}(n)$ can be implemented with a stack.

Initially the stack contains the three elements $\langle 1,m,n\rangle$ .

Then repeatedly the three top elements are replaced according to the rules

${\begin{array}{lllllllll}{\text{(r4)}}&1&,0&,n&\rightarrow &(n+1)\\{\text{(r5)}}&1&,(m+1)&,n&\rightarrow &(n+1)&,m&,1\\{\text{(r6)}}&(x+2)&,m&,n&\rightarrow &1&,m&,(x+1)&,m&,n\\\end{array}}$

Schematically, starting from $\langle 1,m,n\rangle$ :

```
WHILE stackLength <> 1
{
   POP 3 elements;
   PUSH 1 or 3 or 5 elements, applying the rules r4, r5, r6;
}
```

**Example**

On input $\langle 1,2,1\rangle$ the successive stack configurations are

${\begin{aligned}&{\underline {1,2,1}}\rightarrow _{r5}{\underline {2,1,1}}\rightarrow _{r6}1,1,{\underline {1,1,1}}\rightarrow _{r5}1,1,{\underline {2,0,1}}\rightarrow _{r6}1,1,1,0,{\underline {1,0,1}}\\&\rightarrow _{r4}1,1,{\underline {1,0,2}}\rightarrow _{r4}{\underline {1,1,3}}\rightarrow _{r5}{\underline {4,0,1}}\rightarrow _{r6}1,0,{\underline {3,0,1}}\rightarrow _{r6}1,0,1,0,{\underline {2,0,1}}\\&\rightarrow _{r6}1,0,1,0,1,0,{\underline {1,0,1}}\rightarrow _{r4}1,0,1,0,{\underline {1,0,2}}\rightarrow _{r4}1,0,{\underline {1,0,3}}\rightarrow _{r4}{\underline {1,0,4}}\rightarrow _{r4}5\end{aligned}}$

The corresponding equalities are

${\begin{aligned}&A_{2}(1)=A_{1}^{2}(1)=A_{1}(A_{1}(1))=A_{1}(A_{0}^{2}(1))=A_{1}(A_{0}(A_{0}(1)))\\&=A_{1}(A_{0}(2))=A_{1}(3)=A_{0}^{4}(1)=A_{0}(A_{0}^{3}(1))=A_{0}(A_{0}(A_{0}^{2}(1)))\\&=A_{0}(A_{0}(A_{0}(A_{0}(1))))=A_{0}(A_{0}(A_{0}(2)))=A_{0}(A_{0}(3))=A_{0}(4)=5\end{aligned}}$

When reduction rule r7 is used instead of rule r6, the replacements in the stack will follow

${\begin{array}{lllllllll}{\text{(r7)}}&(x+2)&,m&,n&\rightarrow &(x+1)&,m&,1&,m&,n\end{array}}$

The successive stack configurations will then be

${\begin{aligned}&{\underline {1,2,1}}\rightarrow _{r5}{\underline {2,1,1}}\rightarrow _{r7}1,1,{\underline {1,1,1}}\rightarrow _{r5}1,1,{\underline {2,0,1}}\rightarrow _{r7}1,1,1,0,{\underline {1,0,1}}\\&\rightarrow _{r4}1,1,{\underline {1,0,2}}\rightarrow _{r4}{\underline {1,1,3}}\rightarrow _{r5}{\underline {4,0,1}}\rightarrow _{r7}3,0,{\underline {1,0,1}}\rightarrow _{r4}{\underline {3,0,2}}\\&\rightarrow _{r7}2,0,{\underline {1,0,2}}\rightarrow _{r4}{\underline {2,0,3}}\rightarrow _{r7}1,0,{\underline {1,0,3}}\rightarrow _{r4}{\underline {1,0,4}}\rightarrow _{r4}5\end{aligned}}$

The corresponding equalities are

${\begin{aligned}&A_{2}(1)=A_{1}^{2}(1)=A_{1}(A_{1}(1))=A_{1}(A_{0}^{2}(1))=A_{1}(A_{0}(A_{0}(1)))\\&=A_{1}(A_{0}(2))=A_{1}(3)=A_{0}^{4}(1)=A_{0}^{3}(A_{0}(1))=A_{0}^{3}(2)\\&=A_{0}^{2}(A_{0}(2))=A_{0}^{2}(3)=A_{0}(A_{0}(3))=A_{0}(4)=5\end{aligned}}$

**Remarks**

- On any given input the TRSs presented so far converge in the same number of steps. They also use the same reduction rules (in this comparison the rules r1, r2, r3 are considered "the same as" the rules r4, r5, r6/r7 respectively). For example, the reduction of $A(2,1)$ converges in 14 steps: 6 × r1, 3 × r2, 5 × r3. The reduction of $A_{2}(1)$ converges in the same 14 steps: 6 × r4, 3 × r5, 5 × r6/r7. The TRSs differ in the order in which the reduction rules are applied.
- When $A_{i}(n)$ is computed following the rules {r4, r5, r6}, the maximum length of the stack stays below $2\times A(i,n)$ . When reduction rule r7 is used instead of rule r6, the maximum length of the stack is only $2(i+2)$ . The length of the stack reflects the recursion depth. As the reduction according to the rules {r4, r5, r7} involves a smaller maximum depth of recursion, this computation is more efficient in that respect.

### Computation by TRS, based on hyperoperators

As Sundblad (1971) — or Porto & Matos (1980) — showed explicitly, the Ackermann function can be expressed in terms of the hyperoperation sequence:

$A(m,n)={\begin{cases}n+1&m=0\\2[m](n+3)-3&m>0\\\end{cases}}$

or, after removal of the constant 2 from the parameter list, in terms of Buck's function

$A(m,n)={\begin{cases}n+1&m=0\\F(m,n+3)-3&m>0\\\end{cases}}$

Buck's function $\operatorname {F} (m,n)=2[m]n$ , a variant of Ackermann function by itself, can be computed with the following reduction rules:

${\begin{array}{lll}{\text{(b1)}}&F(S(0),0,n)&\rightarrow &S(n)\\{\text{(b2)}}&F(S(0),S(0),0)&\rightarrow &S(S(0))\\{\text{(b3)}}&F(S(0),S(S(0)),0)&\rightarrow &0\\{\text{(b4)}}&F(S(0),S(S(S(m))),0)&\rightarrow &S(0)\\{\text{(b5)}}&F(S(0),S(m),S(n))&\rightarrow &F(S(n),m,F(S(0),S(m),0))\\{\text{(b6)}}&F(S(S(x)),m,n)&\rightarrow &F(S(0),m,F(S(x),m,n))\end{array}}$ Instead of rule b6 one can define the rule

${\begin{array}{lll}{\text{(b7)}}&F(S(S(x)),m,n)&\rightarrow &F(S(x),m,F(S(0),m,n))\end{array}}$ To compute the Ackermann function it suffices to add three reduction rules

${\begin{array}{lll}{\text{(r8)}}&A(0,n)&\rightarrow &S(n)\\{\text{(r9)}}&A(S(m),n)&\rightarrow &P(F(S(0),S(m),S(S(S(n)))))\\{\text{(r10)}}&P(S(S(S(m))))&\rightarrow &m\\\end{array}}$

These rules take care of the base case $A(0,n)$ , the alignment $(n+3)$ and the fudge (-3).

**Example**

Compute $A(2,1)\rightarrow _{*}5$

| using reduction rule ${\text{b7}}$ : | using reduction rule ${\text{b6}}$ : |
|---|---|
| ${\underline {A(2,1)}}$ | ${\underline {A(2,1)}}$ |
| $\rightarrow _{r9}P({\underline {F(1,2,4)}})$ | $\rightarrow _{r9}P({\underline {F(1,2,4)}})$ |
| $\rightarrow _{b5}P(F(4,1,{\underline {F(1,2,0)}}))$ | $\rightarrow _{b5}P(F(4,1,{\underline {F(1,2,0)}}))$ |
| $\rightarrow _{b3}P({\underline {F(4,1,0)}})$ | $\rightarrow _{b3}P({\underline {F(4,1,0)}})$ |
| $\rightarrow _{b7}P(F(3,1,{\underline {F(1,1,0)}}))$ | $\rightarrow _{b6}P(F(1,1,{\underline {F(3,1,0)}}))$ |
| $\rightarrow _{b2}P({\underline {F(3,1,2)}})$ | $\rightarrow _{b6}P(F(1,1,F(1,1,{\underline {F(2,1,0)}})))$ |
| $\rightarrow _{b7}P(F(2,1,{\underline {F(1,1,2)}}))$ | $\rightarrow _{b6}P(F(1,1,F(1,1,F(1,1,{\underline {F(1,1,0)}}))))$ |
| $\rightarrow _{b5}P(F(2,1,F(2,0,{\underline {F(1,1,0)}})))$ | $\rightarrow _{b2}P(F(1,1,F(1,1,{\underline {F(1,1,2)}})))$ |
| $\rightarrow _{b2}P(F(2,1,{\underline {F(2,0,2)}}))$ | $\rightarrow _{b5}P(F(1,1,F(1,1,F(2,0,{\underline {F(1,1,0)}}))))$ |
| $\rightarrow _{b7}P(F(2,1,F(1,0,{\underline {F(1,0,2)}})))$ | $\rightarrow _{b2}P(F(1,1,F(1,1,{\underline {F(2,0,2)}})))$ |
| $\rightarrow _{b1}P(F(2,1,{\underline {F(1,0,3)}}))$ | $\rightarrow _{b6}P(F(1,1,F(1,1,F(1,0,{\underline {F(1,0,2)}}))))$ |
| $\rightarrow _{b1}P({\underline {F(2,1,4)}})$ | $\rightarrow _{b1}P(F(1,1,F(1,1,{\underline {F(1,0,3)}})))$ |
| $\rightarrow _{b7}P(F(1,1,{\underline {F(1,1,4)}}))$ | $\rightarrow _{b1}P(F(1,1,{\underline {F(1,1,4)}}))$ |
| $\rightarrow _{b5}P(F(1,1,F(4,0,{\underline {F(1,1,0)}})))$ | $\rightarrow _{b5}P(F(1,1,F(4,0,{\underline {F(1,1,0)}})))$ |
| $\rightarrow _{b2}P(F(1,1,{\underline {F(4,0,2)}}))$ | $\rightarrow _{b2}P(F(1,1,{\underline {F(4,0,2)}}))$ |
| $\rightarrow _{b7}P(F(1,1,F(3,0,{\underline {F(1,0,2)}})))$ | $\rightarrow _{b6}P(F(1,1,F(1,0,{\underline {F(3,0,2)}})))$ |
| $\rightarrow _{b1}P(F(1,1,{\underline {F(3,0,3)}}))$ | $\rightarrow _{b6}P(F(1,1,F(1,0,F(1,0,{\underline {F(2,0,2)}}))))$ |
| $\rightarrow _{b7}P(F(1,1,F(2,0,{\underline {F(1,0,3)}})))$ | $\rightarrow _{b6}P(F(1,1,F(1,0,F(1,0,F(1,0,{\underline {F(1,0,2)}})))))$ |
| $\rightarrow _{b1}P(F(1,1,{\underline {F(2,0,4)}}))$ | $\rightarrow _{b1}P(F(1,1,F(1,0,F(1,0,{\underline {F(1,0,3)}}))))$ |
| $\rightarrow _{b7}P(F(1,1,F(1,0,{\underline {F(1,0,4)}})))$ | $\rightarrow _{b1}P(F(1,1,F(1,0,{\underline {F(1,0,4)}})))$ |
| $\rightarrow _{b1}P(F(1,1,{\underline {F(1,0,5)}}))$ | $\rightarrow _{b1}P(F(1,1,{\underline {F(1,0,5)}}))$ |
| $\rightarrow _{b1}P({\underline {F(1,1,6)}})$ | $\rightarrow _{b1}P({\underline {F(1,1,6)}})$ |
| $\rightarrow _{b5}P(F(6,0,{\underline {F(1,1,0)}}))$ | $\rightarrow _{b5}P(F(6,0,{\underline {F(1,1,0)}}))$ |
| $\rightarrow _{b2}P({\underline {F(6,0,2)}})$ | $\rightarrow _{b2}P({\underline {F(6,0,2)}})$ |
| $\rightarrow _{b7}P(F(5,0,{\underline {F(1,0,2)}}))$ | $\rightarrow _{b6}P(F(1,0,{\underline {F(5,0,2)}}))$ |
| $\rightarrow _{b1}P({\underline {F(5,0,3)}})$ | $\rightarrow _{b6}P(F(1,0,F(1,0,{\underline {F(4,0,2)}})))$ |
| $\rightarrow _{b7}P(F(4,0,{\underline {F(1,0,3)}}))$ | $\rightarrow _{b6}P(F(1,0,F(1,0,F(1,0,{\underline {F(3,0,2)}}))))$ |
| $\rightarrow _{b1}P({\underline {F(4,0,4)}})$ | $\rightarrow _{b6}P(F(1,0,F(1,0,F(1,0,F(1,0,{\underline {F(2,0,2)}})))))$ |
| $\rightarrow _{b7}P(F(3,0,{\underline {F(1,0,4)}}))$ | $\rightarrow _{b6}P(F(1,0,F(1,0,F(1,0,F(1,0,F(1,0,{\underline {F(1,0,2)}}))))))$ |
| $\rightarrow _{b1}P({\underline {F(3,0,5)}})$ | $\rightarrow _{b1}P(F(1,0,F(1,0,F(1,0,F(1,0,{\underline {F(1,0,3)}})))))$ |
| $\rightarrow _{b7}P(F(2,0,{\underline {F(1,0,5)}}))$ | $\rightarrow _{b1}P(F(1,0,F(1,0,F(1,0,{\underline {F(1,0,4)}}))))$ |
| $\rightarrow _{b1}P({\underline {F(2,0,6)}})$ | $\rightarrow _{b1}P(F(1,0,F(1,0,{\underline {F(1,0,5)}})))$ |
| $\rightarrow _{b7}P(F(1,0,{\underline {F(1,0,6)}}))$ | $\rightarrow _{b1}P(F(1,0,{\underline {F(1,0,6)}}))$ |
| $\rightarrow _{b1}P({\underline {F(1,0,7)}})$ | $\rightarrow _{b1}P({\underline {F(1,0,7)}})$ |
| $\rightarrow _{b1}{\underline {P(8)}}$ | $\rightarrow _{b1}{\underline {P(8)}}$ |
| $\rightarrow _{r10}5$ | $\rightarrow _{r10}5$ |

The matching equalities are

- when the TRS with the reduction rule ${\text{b6}}$ is applied:

${\begin{aligned}&A(2,1)+3=F(2,4)=\dots =F^{6}(0,2)=F(0,F^{5}(0,2))=F(0,F(0,F^{4}(0,2)))\\&=F(0,F(0,F(0,F^{3}(0,2))))=F(0,F(0,F(0,F(0,F^{2}(0,2)))))=F(0,F(0,F(0,F(0,F(0,F(0,2))))))\\&=F(0,F(0,F(0,F(0,F(0,3)))))=F(0,F(0,F(0,F(0,4))))=F(0,F(0,F(0,5)))=F(0,F(0,6))=F(0,7)=8\end{aligned}}$

- when the TRS with the reduction rule ${\text{b7}}$ is applied:

${\begin{aligned}&A(2,1)+3=F(2,4)=\dots =F^{6}(0,2)=F^{5}(0,F(0,2))=F^{5}(0,3)=F^{4}(0,F(0,3))=F^{4}(0,4)\\&=F^{3}(0,F(0,4))=F^{3}(0,5)=F^{2}(0,F(0,5))=F^{2}(0,6)=F(0,F(0,6))=F(0,7)=8\end{aligned}}$ **Remarks**

- The computation of $\operatorname {A} _{i}(n)$ according to the rules {b1 - b5, b6, r8 - r10} is deeply recursive. The maximum depth of nested F s is $A(i,n)+1$ . The culprit is the order in which iteration is executed: $F^{n+1}(x)=F(F^{n}(x))$ . The first F disappears only after the whole sequence is unfolded.
- The computation according to the rules {b1 - b5, b7, r8 - r10} is more efficient in that respect. The iteration $F^{n+1}(x)=F^{n}(F(x))$ simulates the repeated loop over a block of code. The nesting is limited to $(i+1)$ , one recursion level per iterated function. Meyer & Ritchie (1967) showed this correspondence.
- These considerations concern the recursion depth only. Either way of iterating leads to the same number of reduction steps, involving the same rules (when the rules b6 and b7 are considered "the same"). The reduction of $A(2,1)$ for instance converges in 35 steps: 12 × b1, 4 × b2, 1 × b3, 4 × b5, 12 × b6/b7, 1 × r9, 1 × r10. The *modus iterandi* only affects the order in which the reduction rules are applied.
- A real gain of execution time can only be achieved by not recalculating subresults over and over again. Memoization is an optimization technique where the results of function calls are cached and returned when the same inputs occur again. See for instance Ward (1993). Grossman & Zeitman (1988) published a cunning algorithm that computes $A(i,n)$ within ${\mathcal {O}}(iA(i,n))$ time and within ${\mathcal {O}}(i)$ space.

### Huge numbers

To demonstrate how the computation of $A(4,3)$ results in many steps and in a large number:

${\begin{aligned}A(4,3)&\rightarrow A(3,A(4,2))\\&\rightarrow A(3,A(3,A(4,1)))\\&\rightarrow A(3,A(3,A(3,A(4,0))))\\&\rightarrow A(3,A(3,A(3,A(3,1))))\\&\rightarrow A(3,A(3,A(3,A(2,A(3,0)))))\\&\rightarrow A(3,A(3,A(3,A(2,A(2,1)))))\\&\rightarrow A(3,A(3,A(3,A(2,A(1,A(2,0))))))\\&\rightarrow A(3,A(3,A(3,A(2,A(1,A(1,1))))))\\&\rightarrow A(3,A(3,A(3,A(2,A(1,A(0,A(1,0)))))))\\&\rightarrow A(3,A(3,A(3,A(2,A(1,A(0,A(0,1)))))))\\&\rightarrow A(3,A(3,A(3,A(2,A(1,A(0,2))))))\\&\rightarrow A(3,A(3,A(3,A(2,A(1,3)))))\\&\rightarrow A(3,A(3,A(3,A(2,A(0,A(1,2))))))\\&\rightarrow A(3,A(3,A(3,A(2,A(0,A(0,A(1,1)))))))\\&\rightarrow A(3,A(3,A(3,A(2,A(0,A(0,A(0,A(1,0))))))))\\&\rightarrow A(3,A(3,A(3,A(2,A(0,A(0,A(0,A(0,1))))))))\\&\rightarrow A(3,A(3,A(3,A(2,A(0,A(0,A(0,2)))))))\\&\rightarrow A(3,A(3,A(3,A(2,A(0,A(0,3))))))\\&\rightarrow A(3,A(3,A(3,A(2,A(0,4)))))\\&\rightarrow A(3,A(3,A(3,A(2,5))))\\&\qquad \vdots \\&\rightarrow A(3,A(3,A(3,13)))\\&\qquad \vdots \\&\rightarrow A(3,A(3,65533))\\&\qquad \vdots \\&\rightarrow A(3,2^{65536}-3)\\&\qquad \vdots \\&\rightarrow 2^{2^{65536}}-3.\\\end{aligned}}$

## Table of values

Computing the Ackermann function can be restated in terms of an infinite table. First, place the natural numbers along the top row. To determine a number in the table, take the number immediately to the left. Then use that number to look up the required number in the column given by that number and one row up. If there is no number to its left, simply look at the column headed "1" in the previous row. Here is a small upper-left portion of the table:

| *n**m* | 0 | 1 | 2 | 3 | 4 | *n* |
|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | $n+1$ |
| 1 | 2 | 3 | 4 | 5 | 6 | $n+2=2+(n+3)-3$ |
| 2 | 3 | 5 | 7 | 9 | 11 | $2n+3=2\cdot (n+3)-3$ |
| 3 | 5 | 13 | 29 | 61 | 125 | $2^{(n+3)}-3$ |
| 4 | 13 | 65533 | 265536 – 3 | ${2^{2^{65536}}}-3$ | ${2^{2^{2^{65536}}}}-3$ | ${\begin{matrix}\underbrace {{2^{2}}^{{\cdot }^{{\cdot }^{{\cdot }^{2}}}}} _{n+3}-3\end{matrix}}$ |
|   |   | $=2\uparrow \uparrow 5-3$ $\approx 2.00353\cdot {10^{19728}}$ | $=2\uparrow \uparrow 6-3$ | $=2\uparrow \uparrow 7-3$ |   |   |
| $=2\uparrow \uparrow (n+3)-3$ |   |   |   |   |   |   |
| 5 | 65533 | $2\uparrow \uparrow 65536-3$ | $2\uparrow \uparrow \uparrow 5-3$ | $2\uparrow \uparrow \uparrow 6-3$ | $2\uparrow \uparrow \uparrow 7-3$ | $2\uparrow \uparrow \uparrow (n+3)-3$ |
| 6 | $2\uparrow \uparrow 65536-3$ | $2\uparrow \uparrow \uparrow \uparrow 4-3$ | $2\uparrow \uparrow \uparrow \uparrow 5-3$ | $2\uparrow \uparrow \uparrow \uparrow 6-3$ | $2\uparrow \uparrow \uparrow \uparrow 7-3$ | $2\uparrow \uparrow \uparrow \uparrow (n+3)-3$ |
| *m* | $(2\uparrow ^{m-2}3)-3$ | $(2\uparrow ^{m-2}4)-3$ | $(2\uparrow ^{m-2}5)-3$ | $(2\uparrow ^{m-2}6)-3$ | $(2\uparrow ^{m-2}7)-3$ | $(2\uparrow ^{m-2}(n+3))-3$ |

The numbers here that are only expressed with recursive exponentiation or Knuth arrows are very large and would take up too much space to notate in plain decimal digits.

Despite the large values occurring in this early section of the table, some even larger numbers have been defined, such as Graham's number, which cannot be written with any small number of Knuth arrows. This number is constructed with a technique similar to applying the Ackermann function to itself recursively.

This is a repeat of the above table, but with the values replaced by the relevant expression from the function definition to show the pattern clearly:

| *n**m* | 0 | 1 | 2 | 3 | 4 | *n* |
|---|---|---|---|---|---|---|
| 0 | 0+1 | 1+1 | 2+1 | 3+1 | 4+1 | *n* + 1 |
| 1 | *A*(0, 1) | *A*(0, *A*(1, 0)) = *A*(0, 2) | *A*(0, *A*(1, 1)) = *A*(0, 3) | *A*(0, *A*(1, 2)) = *A*(0, 4) | *A*(0, *A*(1, 3)) = *A*(0, 5) | *A*(0, *A*(1, *n*−1)) |
| 2 | *A*(1, 1) | *A*(1, *A*(2, 0)) = *A*(1, 3) | *A*(1, *A*(2, 1)) = *A*(1, 5) | *A*(1, *A*(2, 2)) = *A*(1, 7) | *A*(1, *A*(2, 3)) = *A*(1, 9) | *A*(1, *A*(2, *n*−1)) |
| 3 | *A*(2, 1) | *A*(2, *A*(3, 0)) = *A*(2, 5) | *A*(2, *A*(3, 1)) = *A*(2, 13) | *A*(2, *A*(3, 2)) = *A*(2, 29) | *A*(2, *A*(3, 3)) = *A*(2, 61) | *A*(2, *A*(3, *n*−1)) |
| 4 | *A*(3, 1) | *A*(3, *A*(4, 0)) = *A*(3, 13) | *A*(3, *A*(4, 1)) = *A*(3, 65533) | *A*(3, *A*(4, 2)) | *A*(3, *A*(4, 3)) | *A*(3, *A*(4, *n*−1)) |
| 5 | *A*(4, 1) | *A*(4, *A*(5, 0)) | *A*(4, *A*(5, 1)) | *A*(4, *A*(5, 2)) | *A*(4, *A*(5, 3)) | *A*(4, *A*(5, *n*−1)) |
| 6 | *A*(5, 1) | *A*(5, *A*(6, 0)) | *A*(5, *A*(6, 1)) | *A*(5, *A*(6, 2)) | *A*(5, *A*(6, 3)) | *A*(5, *A*(6, *n*−1)) |

## Properties

### General remarks

- It may not be immediately obvious that the evaluation of $A(m,n)$ always terminates. However, the recursion is bounded because in each recursive application either m decreases, or m remains the same and n decreases. Each time that n reaches zero, m decreases, so m eventually reaches zero as well. (Expressed more technically, in each case the pair $(m,n)$ decreases in the lexicographic order on pairs, which is a well-ordering, just like the ordering of single non-negative integers; this means one cannot go down in the ordering infinitely many times in succession.) However, when m decreases there is no upper bound on how much n can increase — and it will often increase greatly.
- For small values of *m* like 1, 2, or 3, the Ackermann function grows relatively slowly with respect to *n* (at most exponentially). For $m\geq 4$ , however, it grows much more quickly; even $A(4,2)$ is about 2.00353×1019728, and the decimal expansion of $A(4,3)$ is very large by any typical measure, about 2.12004×106.03123×1019727.
- An interesting aspect is that the only arithmetic operation it ever uses is addition of 1. Its fast growing power is based solely on nested recursion. This also implies that its running time is at least proportional to its output, and so is also extremely huge. In actuality, for most cases the running time is far larger than the output; see above.
- A single-argument version $f(n)=A(n,n)$ that increases both m and n at the same time dwarfs every primitive recursive function, including very fast-growing functions such as the exponential function, the factorial function, multi- and superfactorial functions, and even functions defined using Knuth's up-arrow notation (except when the indexed up-arrow is used). It can be seen that $f(n)$ is roughly comparable to $f_{\omega }(n)$ in the fast-growing hierarchy. This extreme growth can be exploited to show that f , which is obviously computable on a machine with infinite memory such as a Turing machine and so is a computable function, grows faster than any primitive recursive function and is therefore not primitive recursive.

### Not primitive recursive

The Ackermann function grows faster than any primitive recursive function and therefore is not itself primitive recursive.

**Proof sketch**:

Primitive recursive functions are built from basic functions using composition and primitive recursion, and all grow within a certain rate. We define, constructively, a hierarchy of total functions $\operatorname {FGH} _{k}(n)$ by:

$\operatorname {FGH} _{0}(n)=n+1,\quad \operatorname {FGH} _{k+1}(n)=\operatorname {FGH} _{k}^{n}(n)$

where $\operatorname {FGH} _{k}^{n}$ denotes n -fold iteration of $\operatorname {FGH} _{k}$ on input n . This hierarchy grows strictly faster with increasing k , and every primitive recursive function is eventually bounded above by some $\operatorname {FGH} _{k}$ . This can be shown by structural induction on the definitions of primitive recursive functions.

However, the Ackermann function $\operatorname {A} (m,n)$ eventually exceeds every $\operatorname {FGH} _{k}$ ; for every k , there exists m such that $\operatorname {A} (m,n)>\operatorname {FGH} _{k}(n)$ for all sufficiently large n . Thus, $\operatorname {A}$ grows faster than any primitive recursive function and is therefore not primitive recursive.

## Inverse

Since the function *f*(*n*) = *A*(*n*, *n*) considered above grows very rapidly, its inverse function, *f*−1, grows very slowly. This **inverse Ackermann function** *f*−1 is usually denoted by ***α***. In fact, *α*(*n*) is less than 5 for any practical input size *n*, since *A*(4, 4) is on the order of $2^{2^{2^{2^{16}}}}$ .

This inverse appears in the time complexity of some algorithms, such as the disjoint-set data structure and Chazelle's algorithm for minimum spanning trees. Sometimes Ackermann's original function or other variations are used in these settings, but they all grow at similarly high rates. In particular, some modified functions simplify the expression by eliminating the −3 and similar terms.

A two-parameter variation of the inverse Ackermann function can be defined as follows, where $\lfloor x\rfloor$ is the floor function:

$\alpha (m,n)=\min\{i\geq 1:A(i,\lfloor m/n\rfloor )\geq \log _{2}n\}.$

This function arises in more precise analyses of the algorithms mentioned above, and gives a more refined time bound. In the disjoint-set data structure, *m* represents the number of operations while *n* represents the number of elements; in the minimum spanning tree algorithm, *m* represents the number of edges while *n* represents the number of vertices. Several slightly different definitions of *α*(*m*, *n*) exist; for example, log2 *n* is sometimes replaced by *n*, and the floor function is sometimes replaced by a ceiling.

Other studies might define an inverse function of one where *m* is set to a constant, such that the inverse applies to a particular row.

The inverse of the Ackermann function is primitive recursive, since it is graph primitive recursive, and it is upper bounded by a primitive recursive function.

## Usage

### In computational complexity

The Ackermann function appears in the time complexity of some algorithms, such as vector addition systems and Petri net reachability, thus showing they are computationally infeasible for large instances.

The inverse of the Ackermann function appears in some time complexity results. For instance, the disjoint-set data structure takes amortized time per operation proportional to the inverse Ackermann function, and cannot be made faster within the cell-probe model of computational complexity.

### In discrete geometry

Certain problems in discrete geometry related to Davenport–Schinzel sequences have complexity bounds in which the inverse Ackermann function $\alpha (n)$ appears. For instance, for n line segments in the plane, the unbounded face of the arrangement of the segments has complexity $O(n\alpha (n))$ , and some systems of n line segments have an unbounded face of complexity $\Omega (n\alpha (n))$ .

### As a benchmark

The Ackermann function, due to its definition in terms of extremely deep recursion, can be used as a benchmark of a compiler's ability to optimize recursion. The first published use of Ackermann's function in this way was in 1970 by Dragoș Vaida and, almost simultaneously, in 1971, by Yngve Sundblad.

Sundblad's seminal paper was taken up by Brian Wichmann (co-author of the Whetstone benchmark) in a trilogy of papers written between 1975 and 1982.
