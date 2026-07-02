---
title: "Dual linear program"
source: https://en.wikipedia.org/wiki/Dual_linear_program
domain: hungarian-assignment
license: CC-BY-SA-4.0
tags: hungarian algorithm, assignment problem, kuhn munkres method, cost matrix
fetched: 2026-07-02
---

# Dual linear program

The **dual** of a given linear program (LP) is another LP that is derived from the original (the **primal**) LP in the following schematic way:

- Each variable in the primal LP becomes a constraint in the dual LP;
- Each constraint in the primal LP becomes a variable in the dual LP;
- The objective direction is inversed – maximum in the primal becomes minimum in the dual and vice versa.

The **weak duality theorem** states that the objective value of the dual LP at any feasible solution is always a bound on the objective of the primal LP at any feasible solution (upper or lower bound, depending on whether it is a maximization or minimization problem). In fact, this bounding property holds for the optimal values of the dual and primal LPs.

The **strong duality theorem** states that, moreover, if the primal has an optimal solution then the dual has an optimal solution too, *and the two optima are equal*.

These theorems belong to a larger class of duality theorems in optimization. The strong duality theorem is one of the cases in which the duality gap (the gap between the optimum of the primal and the optimum of the dual) is 0.

## Form of the dual LP

Suppose we have the linear program:

> Maximize **c**T**x** subject to *A***x** ≤ **b**, **x** ≥ 0.

We would like to construct an upper bound on the solution. So we create a linear combination of the constraints, with positive coefficients, such that the coefficients of **x** in the constraints are at least **c**T. This linear combination gives us an upper bound on the objective. The variables **y** of the dual LP are the coefficients of this linear combination. The dual LP tries to find such coefficients that *minimize* the resulting upper bound. This gives the following LP:

> Minimize **b**T**y** subject to *A*T**y** ≥ **c**, **y** ≥ 0

This LP is called the *dual of* the original LP.

### Interpretation

The duality theorem has an economic interpretation. If we interpret the primal LP as a classical "resource allocation" problem, its dual LP can be interpreted as a "resource valuation" problem.

Consider a factory that is planning its production of goods $1,\ldots ,n$ , which it produces using raw materials $1,\ldots ,m$ . To produce one unit of good i , the factory needs $A_{ji}\geq 0$ units of raw material j . Let x be the factory's production schedule (produce $x_{i}$ units of good i ), let $c\geq 0$ be the market prices (a unit of good i can sell for $c_{i}$ ), and let $b\geq 0$ be the amounts of raw material that the factory has available (it has $b_{j}$ units of raw material j ). The constraints are that $x\geq 0$ (it cannot produce negative goods), and that the factory can only produce as many goods as is allowed by its amounts of raw materials, i.e., $Ax\leq b$ . The factory wishes to maximize its total revenue $c^{\top }x$ .

Thus, the constrained revenue maximization is the primal LP:

> Maximize $c^{\top }x$ subject to $Ax\leq b,x\geq 0$

Now consider another factory that wishes to purchase the entire stock of raw material b from the previous factory. It offers a price vector of y (a unit of raw material i for $y_{i}$ ). For the offer to be accepted, it should be the case that $A^{T}y\geq c$ , as otherwise the first factory could earn more cash by producing a certain product than selling off the raw material used to produce the goods. It also should be $y\geq 0$ , since the first factory would not sell its materials for a negative price. The second factory wishes to minimize the amount $b^{\top }y$ that it pays for the first factory's entire stock of raw materials. Then, the second factory's optimization problem is the dual LP:

> Minimize $b^{\top }y$ subject to $A^{\top }y\geq c,y\geq 0$

The duality theorem states that the duality gap between the two LP problems is non-negative. In other words, an optimal solution to this dual LP is *at least* as large as an optimal solution to the primal LP, meaning that an optimal offer $b^{\top }y$ by the second factory will always be no less than the first factory's optimal revenue $c^{\top }x$ . If the first factory is given an offer to buy its entire stock of raw material, at a per-item price of y , such that $A^{\top }y\geq c,y\geq 0$ , then it should take the offer. It will make at least as much revenue as it could producing finished goods.

The strong duality theorem further states that the duality gap is zero. With strong duality, the dual solution $y^{*}$ is, economically speaking, the "equilibrium price" (see shadow price) for the raw material that a factory with production matrix A and raw material stock b would accept for raw material, given the market price for finished goods c . (Note that $y^{*}$ may not be unique, so the equilibrium price may not be fully determined by A , b , and c .)

To see why, consider if the raw material prices $y\geq 0$ are such that $(A^{T}y)_{i}<c_{i}$ for some i , then the factory would purchase more raw material to produce more of good i , since the prices are "too low". Conversely, if the raw material prices satisfy $A^{T}y\geq c,y\geq 0$ , but does not minimize $b^{T}y$ , then the factory would make more money by selling its raw material than producing goods, since the prices are "too high". At equilibrium price $y^{*}$ , the factory cannot increase its profit by purchasing or selling off raw material.

The duality theorem has a physical interpretation too.

## Constructing the dual LP

In general, given a primal LP, the following algorithm can be used to construct its dual LP. The primal LP is defined by:

- A set of *n* variables: $x_{1},\ldots ,x_{n}$ .
- For each variable $x_{i}$ , a *sign constraint* – it should be either non-negative ( $x_{i}\geq 0$ ), or non-positive ( $x_{i}\leq 0$ ), or unconstrained ( $x_{i}\in \mathbb {R}$ ).
- An objective function: ${\text{maximize}}~~~c_{1}x_{1}+\cdots +c_{n}x_{n}$
- A list of *m* constraints. Each constraint *j* is: $a_{j1}x_{1}+\cdots +a_{jn}x_{n}\lesseqqgtr b_{j}$ where the symbol before the $b_{j}$ can be one of $\geq$ or $\leq$ or = .

The dual LP is constructed as follows.

- Each primal constraint becomes a dual variable. So there are *m* variables: $y_{1},\ldots ,y_{m}$ .
- The sign constraint of each dual variable is "opposite" to the sign of its primal constraint. So " $\geq b_{j}$ " becomes $y_{j}\leq 0$ and " $\leq b_{j}$ " becomes $y_{j}\geq 0$ and " $=b_{j}$ " becomes $y_{j}\in \mathbb {R}$ .
- The dual objective function is ${\text{minimize }}~~~b_{1}y_{1}+\cdots +b_{m}y_{m}$
- Each primal variable becomes a dual constraint. So there are *n* constraints. The coefficient of a dual variable in the dual constraint is the coefficient of its primal variable in its primal constraint. So each constraint *i* is: $a_{1i}y_{1}+\cdots +a_{mi}y_{m}\lesseqqgtr c_{i}$ , where the symbol before the $c_{i}$ is similar to the sign constraint on variable *i* in the primal LP. So $x_{i}\leq 0$ becomes " $\leq c_{i}$ " and $x_{i}\geq 0$ becomes " $\geq c_{i}$ " and $x_{i}\in \mathbb {R}$ becomes " $=c_{i}$ ".

From this algorithm, it is easy to see that the dual of the dual is the primal.

## Vector formulations

If all constraints have the same sign, it is possible to present the above recipe in a shorter way using matrices and vectors. The following table shows the relation between various kinds of primals and duals.

| Primal | Dual | Note |
|---|---|---|
| Maximize **c**T**x** subject to *A***x** ≤ **b**, **x** ≥ 0 | Minimize **b**T**y** subject to *A*T**y** ≥ **c**, **y** ≥ 0 | This is called a "symmetric" dual problem |
| Maximize **c**T**x** subject to *A***x** ≤ **b** | Minimize **b**T**y** subject to *A*T**y** = **c**, **y** ≥ 0 | This is called an "asymmetric" dual problem |
| Maximize **c**T**x** subject to *A***x** = **b**, **x** ≥ 0 | Minimize **b**T**y** subject to *A*T**y** ≥ **c** |   |

## The duality theorems

Below, suppose the primal LP is "maximize **c**T**x** subject to [constraints]" and the dual LP is "minimize **b**T**y** subject to [constraints]".

### Weak duality

The **weak duality theorem** says that, for each feasible solution **x** of the primal and each feasible solution **y** of the dual: **c**T**x** ≤ **b**T**y**. In other words, the objective value in each feasible solution of the dual is an upper-bound on the objective value of the primal, and objective value in each feasible solution of the primal is a lower-bound on the objective value of the dual. Here is a proof for the primal LP "Maximize **c**T**x** subject to *A***x** ≤ **b**, **x** ≥ 0":

- **c**T**x**
- = **xTc** [since this just a scalar product of the two vectors]
- ≤ **xT**(***A*****T****y**) [since *A*T**y** ≥ **c** by the dual constraints, and **x** ≥ 0]
- = (**xT*A*T**)**y** [by associativity]
- = (**Ax**)**T****y** [by properties of transpose]
- ≤ **bTy** [since *A***x** ≤ **b** by the primal constraints, and **y** ≥ 0]

Weak duality implies:

> max**x** **c**T**x** ≤ min**y** **b**T**y**

In particular, if the primal is unbounded (from above) then the dual has no feasible solution, and if the dual is unbounded (from below) then the primal has no feasible solution.

### Strong duality

The **strong duality theorem** says that if one of the two problems has an optimal solution, so does the other one and that the bounds given by the weak duality theorem are tight, i.e.:

> max**x** **c**T**x** = min**y** **b**T**y**

The strong duality theorem is harder to prove; the proofs usually use the weak duality theorem as a sub-routine.

One proof uses the simplex algorithm and relies on the proof that, with the suitable pivot rule, it provides a correct solution. The proof establishes that, once the simplex algorithm finishes with a solution to the primal LP, it is possible to read from the final tableau, a solution to the dual LP. So, by running the simplex algorithm, we obtain solutions to both the primal and the dual simultaneously.

Another proof uses the Farkas lemma.

### Theoretical implications

1. The weak duality theorem implies that finding a *single* feasible solution is as hard as finding an *optimal* feasible solution. Suppose we have an oracle that, given an LP, finds an arbitrary feasible solution (if one exists). Given the LP "Maximize **c**T**x** subject to *A***x** ≤ **b**, **x** ≥ 0", we can construct another LP by combining this LP with its dual. The combined LP has both **x** and **y** as variables:

> Maximize **1**

> subject to *A***x** ≤ **b**, *A*T**y** ≥ **c**, **c**T**x** ≥ **b**T**y**, **x** ≥ 0, **y** ≥ 0

If the combined LP has a feasible solution (**x**,**y**), then by weak duality, **c**T**x** = **b**T**y**. So **x** must be a maximal solution of the primal LP and **y** must be a minimal solution of the dual LP. If the combined LP has no feasible solution, then the primal LP has no feasible solution either.

2. The strong duality theorem provides a "good characterization" of the optimal value of an LP in that it allows us to easily prove that some value *t* is the optimum of some LP. The proof proceeds in two steps:

- Show a feasible solution to the primal LP with value *t*; this proves that the optimum is at least *t*.
- Show a feasible solution to the dual LP with value *t*; this proves that the optimum is at most *t*.

## Examples

### Tiny example

Consider the primal LP, with two variables and one constraint:

${\begin{aligned}{\text{maximize }}&3x_{1}+4x_{2}\\{\text{subject to }}&5x_{1}+6x_{2}=7\\&x_{1}\geq 0,x_{2}\geq 0\end{aligned}}$

Applying the recipe above gives the following dual LP, with one variable and two constraints:

${\begin{aligned}{\text{minimize }}&7y_{1}\\{\text{subject to }}&5y_{1}\geq 3\\&6y_{1}\geq 4\\&y_{1}\in \mathbb {R} \end{aligned}}$

It is easy to see that the maximum of the primal LP is attained when *x*1 is minimized to its lower bound (0) and *x*2 is maximized to its upper bound under the constraint (7/6). The maximum is 4 ⋅ 7/6 = 14/3.

Similarly, the minimum of the dual LP is attained when *y*1 is minimized to its lower bound under the constraints: the first constraint gives a lower bound of 3/5 while the second constraint gives a stricter lower bound of 4/6, so the actual lower bound is 4/6 and the minimum is 7 ⋅ 4/6 = 14/3.

In accordance with the strong duality theorem, the maximum of the primal equals the minimum of the dual.

We use this example to illustrate the proof of the weak duality theorem. Suppose that, in the primal LP, we want to get an upper bound on the objective $3x_{1}+4x_{2}$ . We can use the constraint multiplied by some coefficient, say $y_{1}$ . For any $y_{1}$ we get: $y_{1}\cdot (5x_{1}+6x_{2})=7y_{1}$ . Now, if $y_{1}\cdot 5x_{1}\geq 3x_{1}$ and $y_{1}\cdot 6x_{2}\geq 4x_{2}$ , then $y_{1}\cdot (5x_{1}+6x_{2})\geq 3x_{1}+4x_{2}$ , so $7y_{1}\geq 3x_{1}+4x_{2}$ . Hence, the objective of the dual LP is an upper bound on the objective of the primal LP.

### Farmer example

Consider a farmer who may grow wheat and barley with the set provision of some *L* land, *F* fertilizer and *P* pesticide. To grow one unit of wheat, one unit of land, $F_{1}$ units of fertilizer and $P_{1}$ units of pesticide must be used. Similarly, to grow one unit of barley, one unit of land, $F_{2}$ units of fertilizer and $P_{2}$ units of pesticide must be used.

The primal problem would be the farmer deciding how much wheat ( $x_{1}$ ) and barley ( $x_{2}$ ) to grow if their sell prices are $S_{1}$ and $S_{2}$ per unit.

| Maximize: $S_{1}\cdot x_{1}+S_{2}\cdot x_{2}$ | (maximize the revenue from producing wheat and barley) |   |
|---|---|---|
| subject to: | $x_{1}+x_{2}\leq L$ | (cannot use more land than available) |
|   | $F_{1}\cdot x_{1}+F_{2}\cdot x_{2}\leq F$ | (cannot use more fertilizer than available) |
|   | $P_{1}\cdot x_{1}+P_{2}\cdot x_{2}\leq P$ | (cannot use more pesticide than available) |
|   | $x_{1},x_{2}\geq 0$ | (cannot produce negative quantities of wheat or barley). |

In matrix form this becomes:

Maximize:

${\begin{bmatrix}S_{1}&S_{2}\end{bmatrix}}{\begin{bmatrix}x_{1}\\x_{2}\end{bmatrix}}$

subject to:

${\begin{bmatrix}1&1\\F_{1}&F_{2}\\P_{1}&P_{2}\end{bmatrix}}{\begin{bmatrix}x_{1}\\x_{2}\end{bmatrix}}\leq {\begin{bmatrix}L\\F\\P\end{bmatrix}},\,{\begin{bmatrix}x_{1}\\x_{2}\end{bmatrix}}\geq 0.$

For the dual problem assume that *y* unit prices for each of these means of production (inputs) are set by a planning board. The planning board's job is to minimize the total cost of procuring the set amounts of inputs while providing the farmer with a floor on the unit price of each of his crops (outputs), *S*1 for wheat and *S*2 for barley. This corresponds to the following LP:

| Minimize: $L\cdot y_{L}+F\cdot y_{F}+P\cdot y_{P}$ | (minimize the total cost of the means of production as the "objective function") |   |
|---|---|---|
| subject to: | $y_{L}+F_{1}\cdot y_{F}+P_{1}\cdot y_{P}\geq S_{1}$ | (the farmer must receive no less than *S*1 for his wheat) |
|   | $y_{L}+F_{2}\cdot y_{F}+P_{2}\cdot y_{P}\geq S_{2}$ | (the farmer must receive no less than *S*2 for his barley) |
|   | $y_{L},y_{F},y_{P}\geq 0$ | (prices cannot be negative). |

In matrix form this becomes:

Minimize:

${\begin{bmatrix}L&F&P\end{bmatrix}}{\begin{bmatrix}y_{L}\\y_{F}\\y_{P}\end{bmatrix}}$

subject to:

${\begin{bmatrix}1&F_{1}&P_{1}\\1&F_{2}&P_{2}\end{bmatrix}}{\begin{bmatrix}y_{L}\\y_{F}\\y_{P}\end{bmatrix}}\geq {\begin{bmatrix}S_{1}\\S_{2}\end{bmatrix}},\,{\begin{bmatrix}y_{L}\\y_{F}\\y_{P}\end{bmatrix}}\geq 0.$

The primal problem deals with physical quantities. With all inputs available in limited quantities, and assuming the unit prices of all outputs is known, what quantities of outputs to produce so as to maximize total revenue? The dual problem deals with economic values. With floor guarantees on all output unit prices, and assuming the available quantity of all inputs is known, what input unit pricing scheme to set so as to minimize total expenditure?

To each variable in the primal space corresponds an inequality to satisfy in the dual space, both indexed by output type. To each inequality to satisfy in the primal space corresponds a variable in the dual space, both indexed by input type.

The coefficients that bound the inequalities in the primal space are used to compute the objective in the dual space, input quantities in this example. The coefficients used to compute the objective in the primal space bound the inequalities in the dual space, output unit prices in this example.

Both the primal and the dual problems make use of the same matrix. In the primal space, this matrix expresses the consumption of physical quantities of inputs necessary to produce set quantities of outputs. In the dual space, it expresses the creation of the economic values associated with the outputs from set input unit prices.

Since each inequality can be replaced by an equality and a slack variable, this means each primal variable corresponds to a dual slack variable, and each dual variable corresponds to a primal slack variable. This relation allows us to speak about complementary slackness.

### Infeasible program

A LP can also be unbounded or infeasible. Duality theory tells us that:

- If the primal is unbounded, then the dual is infeasible;
- If the dual is unbounded, then the primal is infeasible.

However, it is possible for both the dual and the primal to be infeasible. Here is an example:

| Maximize: $2x_{1}-x_{2}$ |   |
|---|---|
| Subject to: | $x_{1}-x_{2}\leq 1$ |
|   | $-x_{1}+x_{2}\leq -2$ |
|   | $x_{1},x_{2}\geq 0.$ |

## Viewing the solution to a linear programming problem as a (generalized) eigenvector

There is a close connection between linear programming problems, eigenequations, and von Neumann's general equilibrium model. The solution to a linear programming problem can be regarded as a generalized eigenvector.

The eigenequations of a square matrix are as follows:

${\begin{matrix}\mathbf {p} ^{T}\mathbf {A} =\rho \mathbf {p} ^{T}\\\mathbf {A} \mathbf {z} =\rho {\mathbf {z} }\\\end{matrix}}$

where $\mathbf {p} ^{T}$ and $\mathbf {z}$ are the left and right eigenvectors of the square matrix $\mathbf {A}$ , respectively, and $\rho$ is the eigenvalue.

The above eigenequations for the square matrix can be extended to von Neumann's general equilibrium model:

${\begin{matrix}\mathbf {p} ^{T}\mathbf {A} \geq \rho \mathbf {p} ^{T}\mathbf {B} \\\mathbf {A} \mathbf {z} \leq \rho \mathbf {B} {\mathbf {z} }\\\end{matrix}}$

where the economic meanings of $\mathbf {p}$ and $\mathbf {z}$ are the equilibrium prices of various goods and the equilibrium activity levels of various economic agents, respectively.

The von Neumann's equilibrium model can be further extended to the following structural equilibrium model with $\mathbf {A}$ and $\mathbf {B}$ as matrix-valued functions:

${\begin{matrix}\mathbf {p} ^{T}\mathbf {A} (\mathbf {p} ,\mathbf {u} ,\mathbf {z} )\geq \rho \mathbf {p} ^{T}\mathbf {B} (\mathbf {p} ,\mathbf {u} ,\mathbf {z} )\\\mathbf {A} (\mathbf {p} ,\mathbf {u} ,\mathbf {z} )\mathbf {z} \leq \rho \mathbf {B} (\mathbf {p} ,\mathbf {u} ,\mathbf {z} ){\mathbf {z} }\\\end{matrix}}$

where the economic meaning of $\mathbf {u}$ is the utility levels of various consumers. A special case of the above model is

${\begin{matrix}\mathbf {p} ^{T}\mathbf {A} (u)\geq \mathbf {p} ^{T}\mathbf {B} \\\mathbf {A} (u)\mathbf {z} \leq \mathbf {B} {\mathbf {z} }\end{matrix}}$

This form of the structural equilibrium model and linear programming problems can often be converted to each other, that is, the solutions to these two types of problems are often consistent.

If we define $\mathbf {A} (u)={\begin{bmatrix}\mathbf {0} &u\\\mathbf {A} &\mathbf {0} \\\end{bmatrix}}$ , $\mathbf {B} ={\begin{bmatrix}\mathbf {c} ^{T}&0\\\mathbf {0} &\mathbf {b} \\\end{bmatrix}}$ , $\mathbf {p} ={\begin{bmatrix}1\\\mathbf {y} \\\end{bmatrix}}$ , $\mathbf {z} ={\begin{bmatrix}\mathbf {x} \\1\\\end{bmatrix}}$ , then the structural equilibrium model can be written as

${\begin{bmatrix}\mathbf {y} ^{T}\mathbf {A} &u\\\end{bmatrix}}\geq {\begin{bmatrix}\mathbf {c} ^{T}&\mathbf {y} ^{T}\mathbf {b} \\\end{bmatrix}}$

${\begin{bmatrix}u\\\mathbf {A} \mathbf {x} \\\end{bmatrix}}\leq {\begin{bmatrix}\mathbf {c} ^{T}\mathbf {x} \\\mathbf {b} \\\end{bmatrix}}$

Let us illustrate the structural equilibrium model with the previously discussed tiny example. In this example, we have $\mathbf {A} ={\begin{bmatrix}5&6\end{bmatrix}}$ , $\mathbf {A} (u)={\begin{bmatrix}0&0&u\\5&6&0\\\end{bmatrix}}$ and $\mathbf {B} ={\begin{bmatrix}3&4&0\\0&0&7\\\end{bmatrix}}$ .

To solve the structural equilibrium model, we obtain

$\mathbf {p} ^{*}=(1,2/3)^{T},\quad \mathbf {z} ^{*}=(0,7/6,1)^{T},\quad u^{*}=14/3$

These are consistent with the solutions to the linear programming problems.

We substitute the above calculation results into the structural equilibrium model, obtaining ${\begin{matrix}\mathbf {p} ^{T}\mathbf {A} (u)=(10/3,4,14/3)\geq (3,4,14/3)=\mathbf {p} ^{T}\mathbf {B} \\\mathbf {A} (u)\mathbf {z} =(14/3,7)^{T}\leq (14/3,7)^{T}=\mathbf {B} {\mathbf {z} }\end{matrix}}$

## Applications

The max-flow min-cut theorem is a special case of the strong duality theorem: flow-maximization is the primal LP, and cut-minimization is the dual LP. See Max-flow min-cut theorem#Linear program formulation.

Other graph-related theorems can be proved using the strong duality theorem, in particular, Konig's theorem.

The Minimax theorem for zero-sum games can be proved using the strong-duality theorem.

## Alternative algorithm

Sometimes, one may find it more intuitive to obtain the dual program without looking at the program matrix. Consider the following linear program:

| Minimize | $\sum _{i=1}^{m}c_{i}x_{i}+\sum _{j=1}^{n}d_{j}t_{j}$ |   |   |
|---|---|---|---|
| subject to | $\sum _{i=1}^{m}a_{ij}x_{i}+e_{j}t_{j}\geq g_{j},$ |   | $1\leq j\leq n$ |
|   | $f_{i}x_{i}+\sum _{j=1}^{n}b_{ij}t_{j}\geq h_{i},$ |   | $1\leq i\leq m$ |
|   | $x_{i}\geq 0,\,t_{j}\geq 0,$ |   | $1\leq i\leq m,1\leq j\leq n$ |

We have *m* + *n* conditions and all variables are non-negative. We shall define *m* + *n* dual variables: **y**j and **s***i*. We get:

| Minimize | $\sum _{i=1}^{m}c_{i}x_{i}+\sum _{j=1}^{n}d_{j}t_{j}$ |   |   |
|---|---|---|---|
| subject to | $\sum _{i=1}^{m}a_{ij}x_{i}\cdot y_{j}+e_{j}t_{j}\cdot y_{j}\geq g_{j}\cdot y_{j},$ |   | $1\leq j\leq n$ |
|   | $f_{i}x_{i}\cdot s_{i}+\sum _{j=1}^{n}b_{ij}t_{j}\cdot s_{i}\geq h_{i}\cdot s_{i},$ |   | $1\leq i\leq m$ |
|   | $x_{i}\geq 0,\,t_{j}\geq 0,$ |   | $1\leq i\leq m,1\leq j\leq n$ |
|   | $y_{j}\geq 0,\,s_{i}\geq 0,$ |   | $1\leq j\leq n,1\leq i\leq m$ |

Since this is a minimization problem, we would like to obtain a dual program that is a lower bound of the primal. In other words, we would like the sum of all right hand side of the constraints to be the maximal under the condition that for each primal variable the sum of its coefficients do not exceed its coefficient in the linear function. For example, **x**1 appears in *n* + 1 constraints. If we sum its constraints' coefficients we get *a*1,1**y**1 + *a*1,2**y**2 + ... + *a*1,;;n;;**y***n* + *f*1**s**1. This sum must be at most **c**1. As a result, we get:

| Maximize | $\sum _{j=1}^{n}g_{j}y_{j}+\sum _{i=1}^{m}h_{i}s_{i}$ |   |   |
|---|---|---|---|
| subject to | $\sum _{j=1}^{n}a_{ij}y_{j}+f_{i}s_{i}\leq c_{i},$ |   | $1\leq i\leq m$ |
|   | $e_{j}y_{j}+\sum _{i=1}^{m}b_{ij}s_{i}\leq d_{j},$ |   | $1\leq j\leq n$ |
|   | $y_{j}\geq 0,\,s_{i}\geq 0,$ |   | $1\leq j\leq n,1\leq i\leq m$ |

Note that we assume in our calculations steps that the program is in standard form. However, any linear program may be transformed to standard form and it is therefore not a limiting factor.
