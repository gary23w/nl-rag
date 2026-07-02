---
title: "Ellipsoid method"
source: https://en.wikipedia.org/wiki/Ellipsoid_method
domain: interior-point-methods
license: CC-BY-SA-4.0
tags: interior-point method, karmarkar algorithm, barrier function, ellipsoid method
fetched: 2026-07-02
---

# Ellipsoid method

In mathematical optimization, the **ellipsoid method** is an iterative method for minimizing convex functions over convex sets. The ellipsoid method generates a sequence of ellipsoids whose volume uniformly decreases at every step, thus enclosing a minimizer of a convex function.

When specialized to solving feasible linear optimization problems with rational data, the ellipsoid method is an algorithm which finds an optimal solution in a number of steps that is polynomial in the input size.

## History

The ellipsoid method has a long history. As an iterative method, a preliminary version was introduced by Naum Z. Shor. In 1972, an approximation algorithm for real convex minimization was studied by Arkadi Nemirovski and David B. Yudin (Judin).

As an algorithm for solving linear programming problems with rational data, the ellipsoid algorithm was studied by Leonid Khachiyan; Khachiyan's achievement was to prove the polynomial-time solvability of linear programs. This was a notable step from a theoretical perspective: The standard algorithm for solving linear problems at the time was the simplex algorithm, which has a run time that *typically* is linear in the size of the problem, but for which examples exist for which it is *exponential* in the size of the problem. As such, having an algorithm that is *guaranteed* to be polynomial for all cases was a theoretical breakthrough.

Khachiyan's work showed, for the first time, that there can be algorithms for solving linear programs whose runtime can be proven to be polynomial. In practice, however, the algorithm is fairly slow and of little practical interest, though it provided inspiration for later work that turned out to be of much greater practical use. Specifically, Karmarkar's algorithm, an interior-point method, is much faster than the ellipsoid method in practice. Karmarkar's algorithm is also faster in the worst case.

The ellipsoidal algorithm allows complexity theorists to achieve (worst-case) bounds that depend on the dimension of the problem and on the size of the data, but not on the number of rows, so it remained important in combinatorial optimization theory for many years. Only in the 21st century have interior-point algorithms with similar complexity properties appeared.

## Description

A convex minimization problem consists of the following ingredients.

- A convex function $f_{0}(x):\mathbb {R} ^{n}\to \mathbb {R}$ to be minimized over the vector *x* (containing *n* variables);
- Convex inequality constraints of the form $f_{i}(x)\leqslant 0$ , where the functions $f_{i}$ are convex; these constraints define a convex set *Q*.
- Linear equality constraints of the form $h_{i}(x)=0$ .

We are also given an initial ellipsoid ${\mathcal {E}}^{(0)}\subset \mathbb {R} ^{n}$ defined as

${\mathcal {E}}^{(0)}=\left\{z\in \mathbb {R} ^{n}\ :\ (z-x_{0})^{T}P_{(0)}^{-1}(z-x_{0})\leqslant 1\right\}$

containing a minimizer $x^{*}$ , where $P_{(0)}\succ 0$ and $x_{0}$ is the center of ${\mathcal {E}}$ .

Finally, we require the existence of a separation oracle for the convex set *Q .*Given a point $x\in \mathbb {R} ^{n}$ , the oracle should return one of two answers:

- "The point x is in Q ", or -
- "The point x is not in Q , and moreover, here is a hyperplane that separates x from Q ", that is, a vector c such that $c\cdot x<c\cdot y$ for all $y\in Q$ .

The output of the ellipsoid method is either:

- Any point in the polytope *Q* (i.e., any feasible point), or -
- A proof that *Q* is empty.

Inequality-constrained minimization of a function that is zero everywhere corresponds to the problem of simply identifying any feasible point. It turns out that any linear programming problem can be reduced to a linear feasibility problem (i.e. minimize the zero function subject to some linear inequality and equality constraints). One way to do this is by combining the primal and dual linear programs together into one program, and adding the additional (linear) constraint that the value of the primal solution is no worse than the value of the dual solution. Another way is to treat the objective of the linear program as an additional constraint, and use binary search to find the optimum value.

## Unconstrained minimization

At the *k*-th iteration of the algorithm, we have a point $x^{(k)}$ at the center of an ellipsoid

${\mathcal {E}}^{(k)}=\left\{x\in \mathbb {R} ^{n}\ :\ \left(x-x^{(k)}\right)^{T}P_{(k)}^{-1}\left(x-x^{(k)}\right)\leqslant 1\right\}.$

We query the cutting-plane oracle to obtain a vector $g^{(k+1)}\in \mathbb {R} ^{n}$ such that

$g^{(k+1)T}\left(x^{*}-x^{(k)}\right)\leqslant 0.$

We therefore conclude that

$x^{*}\in {\mathcal {E}}^{(k)}\cap \left\{z\ :\ g^{(k+1)T}\left(z-x^{(k)}\right)\leqslant 0\right\}.$

We set ${\mathcal {E}}^{(k+1)}$ to be the ellipsoid of minimal volume containing the half-ellipsoid described above and compute $x^{(k+1)}$ . The update is given by

${\begin{aligned}x^{(k+1)}&=x^{(k)}-{\frac {1}{n+1}}P_{(k)}{\tilde {g}}^{(k+1)}\\P_{(k+1)}&={\frac {n^{2}}{n^{2}-1}}\left(P_{(k)}-{\frac {2}{n+1}}P_{(k)}{\tilde {g}}^{(k+1)}{\tilde {g}}^{(k+1)T}P_{(k)}\right)\end{aligned}}$

where

${\tilde {g}}^{(k+1)}=\left({\frac {1}{\sqrt {g^{(k+1)T}P_{(k)}g^{(k+1)}}}}\right)g^{(k+1)}.$

The stopping criterion is given by the property that

${\sqrt {g^{(k)T}P_{(k)}g^{(k)}}}\leqslant \epsilon \quad \Rightarrow \quad f(x^{(k)})-f\left(x^{*}\right)\leqslant \epsilon .$

## Inequality-constrained minimization

At the *k*-th iteration of the algorithm for constrained minimization, we have a point $x^{(k)}$ at the center of an ellipsoid ${\mathcal {E}}^{(k)}$ as before. We also must maintain a list of values $f_{\rm {best}}^{(k)}$ recording the smallest objective value of feasible iterates so far. Depending on whether or not the point $x^{(k)}$ is feasible, we perform one of two tasks:

- If $x^{(k)}$ is feasible, perform essentially the same update as in the unconstrained case, by choosing a subgradient $g_{0}$ that satisfies

$g_{0}^{T}(x^{*}-x^{(k)})+f_{0}(x^{(k)})-f_{\rm {best}}^{(k)}\leqslant 0$

- If $x^{(k)}$ is infeasible and violates the *j*-th constraint, update the ellipsoid with a feasibility cut. Our feasibility cut may be a subgradient $g_{j}$ of $f_{j}$ which must satisfy

$g_{j}^{T}(z-x^{(k)})+f_{j}(x^{(k)})\leqslant 0$

for all feasible *z*.

## Performance in convex programs

### Theoretical run-time complexity guarantee

The run-time complexity guarantee of the ellipsoid method in the real RAM model is given by the following theorem.

Consider a family of convex optimization problems of the form: **minimize *f*(*x*) s.t. *x* is in *G***, where *f* is a convex function and *G* is a convex set (a subset of an Euclidean space *Rn*). Each problem *p* in the family is represented by a data-vector Data(*p*), e.g., the real-valued coefficients in matrices and vectors representing the function *f* and the feasible region *G*. The *size* of a problem *p*, Size(*p*), is defined as the number of elements (real numbers) in Data(*p*). The following assumptions are needed:

1. *G* (the feasible region) is:
  - Bounded;
  - Has a non-empty interior (so there is a strictly-feasible point);
2. Given Data(*p*), one can compute using poly(Size(p)) arithmetic operations:
  - An ellipsoid that contains *G*;
  - A lower bound 'MinVol(p)>0' of the volume *G*.
3. Given Data(*p*) and a point *x* in *Rn*, one can compute using poly(Size(p)) arithmetic operations:
  - A separation oracle for *G* (that is: either assert that *x* is in *G*, or return a hyperplane separating *x* from *G*).
  - A first-order oracle for *f* (that is: compute the value of *f*(*x*) and a subgradient *f'*(*x*)).

Under these assumptions, the ellipsoid method is "R-polynomial". This means that there exists a polynomial Poly such that, for every problem-instance *p* and every approximation-ratio *ε*>0, the method finds a solution x satisfying :

> $f(x)-\min _{G}f\leq \varepsilon \cdot [\max _{G}f-\min _{G}f]$ ,

using at most the following number of arithmetic operations on real numbers:

> $Poly(Size(p))\cdot \ln \left({\frac {V(p)}{\epsilon }}\right)$

where *V*(*p*) is a data-dependent quantity. Intuitively, it means that the number of operations required for each additional digit of accuracy is polynomial in Size(*p*). In the case of the ellipsoid method, we have:

> $V(p)=\left[{\frac {Vol({\text{initial ellipsoid}})}{Vol(G)}}\right]^{1/n}\leq \left[{\frac {Vol({\text{initial ellipsoid}})}{MinVol(p)}}\right]^{1/n}$ .

The ellipsoid method requires at most $2(n-1)n\cdot \ln \left({\frac {V(p)}{\epsilon }}\right)$ steps, and each step requires Poly(Size(p)) arithmetic operations.

### Practical performance

The ellipsoid method is used on low-dimensional problems, such as planar location problems, where it is numerically stable. Nemirovsky and BenTal say that it is efficient if the number of variables is at most 20-30; this is so even if there are thousands of constraints, as the number of iterations does not depend on the number of constraints. However, in problems with many variables, the ellipsoid method is very inefficient, as the number of iterations grows as O(*n*2).

Even on "small"-sized problems, it suffers from numerical instability and poor performance in practice .

### Theoretical importance

The ellipsoid method is an important theoretical technique in combinatorial optimization. In computational complexity theory, the ellipsoid algorithm is attractive because its complexity depends on the number of columns and the digital size of the coefficients, but not on the number of rows.

The ellipsoid method can be used to show that many algorithmic problems on convex sets are polynomial-time equivalent.

## Performance in linear programs

Leonid Khachiyan applied the ellipsoid method to the special case of linear programming: **minimize cTx s.t. *Ax ≤ b***, where all coefficients in A,b,c are rational numbers. He showed that linear programs can be solved in polynomial time. Here is a sketch of Khachiyan's theorem.

**Step 1: reducing optimization to search**. The theorem of linear programming duality says that we can reduce the above minimization problem to the search problem: **find *x,y* s.t. *Ax ≤ b ; ATy = c ; y ≤ 0 ; cTx=bTy.*** The first problem is solvable iff the second problem is solvable; in case the problem is solvable, the *x*-components of the solution to the second problem are an optimal solution to the first problem. Therefore, from now on, we can assume that we need to solve the following problem: **find *z* ≥ 0 s.t. *Rz* ≤ *r***. Multiplying all rational coefficients by the common denominator, we can assume that all coefficients are integers.

**Step 2: reducing search to feasibility-check**. The problem **find *z* ≥ 0 s.t. *Rz* ≤ *r*** can be reduced to the binary decision problem: "**is there a *z ≥ 0* such that *Rz* ≤ *r*?**". This can be done as follows. If the answer to the decision problem is "no", then the answer to the search problem is "None", and we are done. Otherwise, take the first inequality constraint *R1z* ≤ *r1*; replace it with an equality *R1z* = *r1*; and apply the decision problem again. If the answer is "yes", we keep the equality; if the answer is "no", it means that the inequality is redundant, and we can remove it. Then we proceed to the next inequality constraint. For each constraint, we either convert it to equality or remove it. Finally, we have only equality constraints, which can be solved by any method for solving a system of linear equations.

**Step 3**: the decision problem can be reduced to a different optimization problem. Define the *residual function* f(z) := max[(Rz)1-r1, (Rz)2-r2, (Rz)3-r3,...]. Clearly, *f*(*z*)≤0 iff *Rz* ≤ *r*. Therefore, to solve the decision problem, it is sufficient to solve the minimization problem: min*z* *f*(*z*). The function *f* is convex (it is a maximum of linear functions). Denote the minimum value by *f**. Then the answer to the decision problem is "yes" iff f*≤0.

**Step 4**: In the optimization problem min*z* *f*(*z*), we can assume that *z* is in a box of side-length 2*L*, where *L* is the bit length of the problem data. Thus, we have a bounded convex program, that can be solved up to any accuracy ε by the ellipsoid method, in time polynomial in *L*.

**Step 5**: It can be proved that, if f*>0, then f*>2-poly(L), for some polynomial. Therefore, we can pick the accuracy ε=2-poly(L). Then, the ε-approximate solution found by the ellipsoid method will be positive, iff f*>0, iff the decision problem is unsolvable.

## Variants

The ellipsoid method has several variants, depending on what cuts exactly are used in each step.

### Different cuts

In the **central-cut ellipsoid method**, the cuts are always through the center of the current ellipsoid. The input is a rational number *ε*>0, a convex body *K* given by a **weak separation oracle**, and a number *R* such that S(0,*R*) (the ball of radius R around the origin) contains *K*. The output is one of the following:

- (a) A vector at a distance of at most *ε* from K, or --
- (b) A positive definite matrix **A** and a point **a** such that the ellipsoid E(**A**,**a**) contains *K*, and the volume of E(**A**,**a**) is at most *ε*.

The number of steps is $N:=\lceil 5n\log(1/\epsilon )+5n^{2}\log(2R)\rceil$ , the number of required accuracy digits is *p* := 8*N*, and the required accuracy of the separation oracle is *d* := 2−*p*.

In the **deep-cut ellipsoid method**, the cuts remove more than half of the ellipsoid in each step. This makes it faster to discover that *K* is empty. However, when *K* is nonempty, there are examples in which the central-cut method finds a feasible point faster. The use of deep cuts does not change the order of magnitude of the run-time.

In the **shallow-cut ellipsoid method**, the cuts remove less than half of the ellipsoid in each step. This variant is not very useful in practice, but it has theoretical importance: it allows to prove results that cannot be derived from other variants. The input is a rational number *ε*>0, a convex body *K* given by a **shallow separation oracle**, and a number *R* such that S(0,*R*) contains *K*. The output is a positive definite matrix **A** and a point **a** such that one of the following holds:

- (a) The ellipsoid E(**A**,**a**) has been declared "tough" by the oracle, or -
- (b) *K* is contained in E(**A**,**a**) and the volume of E(**A**,**a**) is at most *ε*.

The number of steps is $N:=\lceil 5n(n+1)^{2}\log(1/\epsilon )+5n^{2}(n+1)^{2}\log(2R)+\log(n+1)\rceil$ , and the number of required accuracy digits is *p* := 8*N.*

### Different ellipsoids

There is also a distinction between the circumscribed ellipsoid and the inscribed ellipsoid methods:

- In the **circumscribed ellipsoid method**, each iteration finds an ellipsoid of *smallest* volume that *contains* the remaining part of the previous ellipsoid. This method was developed by Yudin and Nemirovskii.
- In the **Inscribed ellipsoid method**, each iteration finds an ellipsoid of *largest* volume that is *contained* the remaining part of the previous ellipsoid. This method was developed by Tarasov, Khachian and Erlikh.

The methods differ in their runtime complexity (below, *n* is the number of variables and epsilon is the accuracy):

- The circumscribed method requires $O(n^{2})\ln {\frac {1}{\epsilon }}$ iterations, where each iteration consists of finding a separating hyperplane and finding a new circumscribed ellipsoid. Finding a circumscribed ellipsoid requires $O(n^{2})$ time.
- The inscribed method requires $O(n)\ln {\frac {1}{\epsilon }}$ iterations, where each iteration consists of finding a separating hyperplane and finding a new inscribed ellipsoid. Finding an inscribed ellipsoid requires $O(n^{3.5+\delta })$ time for some small $\delta >0$ .

The relative efficiency of the methods depends on the time required for finding a separating hyperplane, which depends on the application: if the runtime is $O(n^{t})$ for $t\leq 2.5$ then the circumscribed method is more efficient, but if $t>2.5$ then the inscribed method is more efficient.

- The center-of-gravity method is a conceptually simpler method, that requires fewer steps. However, each step is computationally expensive, as it requires to compute the center of gravity of the current feasible polytope.
- Interior point methods, too, allow solving convex optimization problems in polynomial time, but their practical performance is much better than the ellipsoid method.
