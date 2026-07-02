---
title: "Dynamic programming (part 1/2)"
source: https://en.wikipedia.org/wiki/Dynamic_programming
domain: algorithms
license: CC-BY-SA-4.0
tags: algorithm, sorting, complexity, big-o, dynamic programming
fetched: 2026-07-02
part: 1/2
---

# Dynamic programming

**Dynamic programming** (**DP**) is both a mathematical optimization method and an algorithmic paradigm. The method was developed by Richard Bellman in the 1950s and has found applications in numerous fields, such as aerospace engineering and economics.

In both contexts it refers to simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner. While some decision problems cannot be taken apart this way, decisions that span several points in time do often break apart recursively. Likewise, in computer science, if a problem can be solved optimally by breaking it into sub-problems and then recursively finding the optimal solutions to the sub-problems, then it is said to have *optimal substructure*.

If sub-problems can be nested recursively inside larger problems, so that dynamic programming methods are applicable, then there is a relation between the value of the larger problem and the values of the sub-problems. In the optimization literature this relationship is called the Bellman equation.


## Overview

### Mathematical optimization

In terms of mathematical optimization, dynamic programming usually refers to simplifying a decision by breaking it down into a sequence of decision steps over time.

This is done by defining a sequence of **value functions** *V*1, *V*2, ..., *V**n* taking *y* as an argument representing the **state** of the system at times *i* from 1 to *n*.

The definition of *V**n*(*y*) is the value obtained in state *y* at the last time *n*.

The values *V**i* at earlier times *i* = *n* −1, *n* − 2, ..., 2, 1 can be found by working backwards, using a recursive relationship called the Bellman equation.

For *i* = 2, ..., *n*, *V**i*−1 at any state *y* is calculated from *V**i* by maximizing a simple function (usually the sum) of the gain from a decision at time *i* − 1 and the function *V**i* at the new state of the system if this decision is made.

Since *V**i* has already been calculated for the needed states, the above operation yields *V**i*−1 for those states.

Finally, *V*1 at the initial state of the system is the value of the optimal solution. The optimal values of the decision variables can be recovered, one by one, by tracking back the calculations already performed.

### Control theory

In control theory, a typical problem is to find an admissible control u ∗ {\displaystyle \mathbf {u} ^{\ast }} ({\displaystyle \mathbf {u} ^{\ast }}) which causes the system x ˙ ( t ) = g ( x ( t ) , u ( t ) , t ) {\displaystyle {\dot {\mathbf {x} }}(t)=\mathbf {g} \left(\mathbf {x} (t),\mathbf {u} (t),t\right)} ({\displaystyle {\dot {\mathbf {x} }}(t)=\mathbf {g} \left(\mathbf {x} (t),\mathbf {u} (t),t\right)}) to follow an admissible trajectory x ∗ {\displaystyle \mathbf {x} ^{\ast }} ({\displaystyle \mathbf {x} ^{\ast }}) on a continuous time interval t 0 ≤ t ≤ t 1 {\displaystyle t_{0}\leq t\leq t_{1}} ({\displaystyle t_{0}\leq t\leq t_{1}}) that minimizes a cost function

J

=

b

(

x

(

t

1

)

,

t

1

)

+

∫

t

0

t

1

f

(

x

(

t

)

,

u

(

t

)

,

t

)

d

t

{\displaystyle J=b\left(\mathbf {x} (t_{1}),t_{1}\right)+\int _{t_{0}}^{t_{1}}f\left(\mathbf {x} (t),\mathbf {u} (t),t\right)\mathrm {d} t}

The solution to this problem is an optimal control law or policy u ∗ = h ( x ( t ) , t ) {\displaystyle \mathbf {u} ^{\ast }=h(\mathbf {x} (t),t)} ({\displaystyle \mathbf {u} ^{\ast }=h(\mathbf {x} (t),t)}), which produces an optimal trajectory x ∗ {\displaystyle \mathbf {x} ^{\ast }} ({\displaystyle \mathbf {x} ^{\ast }}) and a cost-to-go function J ∗ {\displaystyle J^{\ast }} ({\displaystyle J^{\ast }}). The latter obeys the fundamental equation of dynamic programming:

−

J

t

∗

=

min

u

{

f

(

x

(

t

)

,

u

(

t

)

,

t

)

+

J

x

∗

T

g

(

x

(

t

)

,

u

(

t

)

,

t

)

}

{\displaystyle -J_{t}^{\ast }=\min _{\mathbf {u} }\left\{f\left(\mathbf {x} (t),\mathbf {u} (t),t\right)+J_{x}^{\ast {\mathsf {T}}}\mathbf {g} \left(\mathbf {x} (t),\mathbf {u} (t),t\right)\right\}}

a partial differential equation known as the Hamilton–Jacobi–Bellman equation, in which J x ∗ = ∂ J ∗ ∂ x = [ ∂ J ∗ ∂ x 1         ∂ J ∗ ∂ x 2         …         ∂ J ∗ ∂ x n ] T {\displaystyle J_{x}^{\ast }={\frac {\partial J^{\ast }}{\partial \mathbf {x} }}=\left[{\frac {\partial J^{\ast }}{\partial x_{1}}}~~~~{\frac {\partial J^{\ast }}{\partial x_{2}}}~~~~\dots ~~~~{\frac {\partial J^{\ast }}{\partial x_{n}}}\right]^{\mathsf {T}}} ({\displaystyle J_{x}^{\ast }={\frac {\partial J^{\ast }}{\partial \mathbf {x} }}=\left[{\frac {\partial J^{\ast }}{\partial x_{1}}}~~~~{\frac {\partial J^{\ast }}{\partial x_{2}}}~~~~\dots ~~~~{\frac {\partial J^{\ast }}{\partial x_{n}}}\right]^{\mathsf {T}}}) and J t ∗ = ∂ J ∗ ∂ t {\displaystyle J_{t}^{\ast }={\frac {\partial J^{\ast }}{\partial t}}} ({\displaystyle J_{t}^{\ast }={\frac {\partial J^{\ast }}{\partial t}}}). One finds that minimizing u {\displaystyle \mathbf {u} } ({\displaystyle \mathbf {u} }) in terms of t {\displaystyle t} ({\displaystyle t}), x {\displaystyle \mathbf {x} } ({\displaystyle \mathbf {x} }), and the unknown function J x ∗ {\displaystyle J_{x}^{\ast }} ({\displaystyle J_{x}^{\ast }}) and then substitutes the result into the Hamilton–Jacobi–Bellman equation to get the partial differential equation to be solved with boundary condition J ( t 1 ) = b ( x ( t 1 ) , t 1 ) {\displaystyle J\left(t_{1}\right)=b\left(\mathbf {x} (t_{1}),t_{1}\right)} ({\displaystyle J\left(t_{1}\right)=b\left(\mathbf {x} (t_{1}),t_{1}\right)}). In practice, this generally requires numerical techniques for some discrete approximation to the exact optimization relationship.

Alternatively, the continuous process can be approximated by a discrete system, which leads to a following recurrence relation analog to the Hamilton–Jacobi–Bellman equation:

J

k

∗

(

x

n

−

k

)

=

min

u

n

−

k

{

f

^

(

x

n

−

k

,

u

n

−

k

)

+

J

k

−

1

∗

(

g

^

(

x

n

−

k

,

u

n

−

k

)

)

}

{\displaystyle J_{k}^{\ast }\left(\mathbf {x} _{n-k}\right)=\min _{\mathbf {u} _{n-k}}\left\{{\hat {f}}\left(\mathbf {x} _{n-k},\mathbf {u} _{n-k}\right)+J_{k-1}^{\ast }\left({\hat {\mathbf {g} }}\left(\mathbf {x} _{n-k},\mathbf {u} _{n-k}\right)\right)\right\}}

at the k {\displaystyle k} ({\displaystyle k})-th stage of n {\displaystyle n} ({\displaystyle n}) equally spaced discrete time intervals, and where f ^ {\displaystyle {\hat {f}}} ({\displaystyle {\hat {f}}}) and g ^ {\displaystyle {\hat {\mathbf {g} }}} ({\displaystyle {\hat {\mathbf {g} }}}) denote discrete approximations to f {\displaystyle f} ({\displaystyle f}) and g {\displaystyle \mathbf {g} } ({\displaystyle \mathbf {g} }). This functional equation is known as the Bellman equation, which can be solved for an exact solution of the discrete approximation of the optimization equation.

#### Example from economics: Ramsey's problem of optimal saving

In economics, the objective is generally to maximize (rather than minimize) some dynamic social welfare function. In Ramsey's problem, this function relates amounts of consumption to levels of utility. Loosely speaking, the planner faces the trade-off between contemporaneous consumption and future consumption (via investment in capital stock that is used in production), known as intertemporal choice. Future consumption is discounted at a constant rate β ∈ ( 0 , 1 ) {\displaystyle \beta \in (0,1)} ({\displaystyle \beta \in (0,1)}). A discrete approximation to the transition equation of capital is given by

k

t

+

1

=

g

^

(

k

t

,

c

t

)

=

f

(

k

t

)

−

c

t

{\displaystyle k_{t+1}={\hat {g}}\left(k_{t},c_{t}\right)=f(k_{t})-c_{t}}

where c {\displaystyle c} ({\displaystyle c}) is consumption, k {\displaystyle k} ({\displaystyle k}) is capital, and f {\displaystyle f} ({\displaystyle f}) is a production function satisfying the Inada conditions. An initial capital stock k 0 > 0 {\displaystyle k_{0}>0} ({\displaystyle k_{0}>0}) is assumed.

Let c t {\displaystyle c_{t}} ({\displaystyle c_{t}}) be consumption in period t, and assume consumption yields utility u ( c t ) = ln ⁡ ( c t ) {\displaystyle u(c_{t})=\ln(c_{t})} ({\displaystyle u(c_{t})=\ln(c_{t})}) as long as the consumer lives. Assume the consumer is impatient, so that he discounts future utility by a factor b each period, where 0 < b < 1 {\displaystyle 0<b<1} ({\displaystyle 0<b<1}). Let k t {\displaystyle k_{t}} ({\displaystyle k_{t}}) be capital in period t. Assume initial capital is a given amount k 0 > 0 {\displaystyle k_{0}>0} ({\displaystyle k_{0}>0}), and suppose that this period's capital and consumption determine next period's capital as k t + 1 = A k t a − c t {\displaystyle k_{t+1}=Ak_{t}^{a}-c_{t}} ({\displaystyle k_{t+1}=Ak_{t}^{a}-c_{t}}), where A is a positive constant and 0 < a < 1 {\displaystyle 0<a<1} ({\displaystyle 0<a<1}). Assume capital cannot be negative. Then the consumer's decision problem can be written as follows:

max

∑

t

=

0

T

b

t

ln

⁡

(

c

t

)

{\displaystyle \max \sum _{t=0}^{T}b^{t}\ln(c_{t})}

subject to

k

t

+

1

=

A

k

t

a

−

c

t

≥

0

{\displaystyle k_{t+1}=Ak_{t}^{a}-c_{t}\geq 0}

for all

t

=

0

,

1

,

2

,

…

,

T

{\displaystyle t=0,1,2,\ldots ,T}

Written this way, the problem looks complicated, because it involves solving for all the choice variables c 0 , c 1 , c 2 , … , c T {\displaystyle c_{0},c_{1},c_{2},\ldots ,c_{T}} ({\displaystyle c_{0},c_{1},c_{2},\ldots ,c_{T}}). (The capital k 0 {\displaystyle k_{0}} ({\displaystyle k_{0}}) is not a choice variable—the consumer's initial capital is taken as given.)

The dynamic programming approach to solve this problem involves breaking it apart into a sequence of smaller decisions. To do so, we define a sequence of *value functions* V t ( k ) {\displaystyle V_{t}(k)} ({\displaystyle V_{t}(k)}), for t = 0 , 1 , 2 , … , T , T + 1 {\displaystyle t=0,1,2,\ldots ,T,T+1} ({\displaystyle t=0,1,2,\ldots ,T,T+1}) which represent the value of having any amount of capital k at each time t. There is (by assumption) no utility from having capital after death, V T + 1 ( k ) = 0 {\displaystyle V_{T+1}(k)=0} ({\displaystyle V_{T+1}(k)=0}).

The value of any quantity of capital at any previous time can be calculated by backward induction using the Bellman equation. In this problem, for each t = 0 , 1 , 2 , … , T {\displaystyle t=0,1,2,\ldots ,T} ({\displaystyle t=0,1,2,\ldots ,T}), the Bellman equation is

V

t

(

k

t

)

=

max

(

ln

⁡

(

c

t

)

+

b

V

t

+

1

(

k

t

+

1

)

)

{\displaystyle V_{t}(k_{t})\,=\,\max \left(\ln(c_{t})+bV_{t+1}(k_{t+1})\right)}

subject to

k

t

+

1

=

A

k

t

a

−

c

t

≥

0

{\displaystyle k_{t+1}=Ak_{t}^{a}-c_{t}\geq 0}

This problem is much simpler than the one we wrote down before, because it involves only two decision variables, c t {\displaystyle c_{t}} ({\displaystyle c_{t}}) and k t + 1 {\displaystyle k_{t+1}} ({\displaystyle k_{t+1}}). Intuitively, instead of choosing his whole lifetime plan at birth, the consumer can take things one step at a time. At time t, his current capital k t {\displaystyle k_{t}} ({\displaystyle k_{t}}) is given, and he only needs to choose current consumption c t {\displaystyle c_{t}} ({\displaystyle c_{t}}) and saving k t + 1 {\displaystyle k_{t+1}} ({\displaystyle k_{t+1}}).

To actually solve this problem, we work backwards. For simplicity, the current level of capital is denoted as k. V T + 1 ( k ) {\displaystyle V_{T+1}(k)} ({\displaystyle V_{T+1}(k)}) is already known, so using the Bellman equation once we can calculate V T ( k ) {\displaystyle V_{T}(k)} ({\displaystyle V_{T}(k)}), and so on until we get to V 0 ( k ) {\displaystyle V_{0}(k)} ({\displaystyle V_{0}(k)}), which is the *value* of the initial decision problem for the whole lifetime. In other words, once we know V T − j + 1 ( k ) {\displaystyle V_{T-j+1}(k)} ({\displaystyle V_{T-j+1}(k)}), we can calculate V T − j ( k ) {\displaystyle V_{T-j}(k)} ({\displaystyle V_{T-j}(k)}), which is the maximum of ln ⁡ ( c T − j ) + b V T − j + 1 ( A k a − c T − j ) {\displaystyle \ln(c_{T-j})+bV_{T-j+1}(Ak^{a}-c_{T-j})} ({\displaystyle \ln(c_{T-j})+bV_{T-j+1}(Ak^{a}-c_{T-j})}), where c T − j {\displaystyle c_{T-j}} ({\displaystyle c_{T-j}}) is the choice variable and A k a − c T − j ≥ 0 {\displaystyle Ak^{a}-c_{T-j}\geq 0} ({\displaystyle Ak^{a}-c_{T-j}\geq 0}).

Working backwards, it can be shown that the value function at time t = T − j {\displaystyle t=T-j} ({\displaystyle t=T-j}) is

V

T

−

j

(

k

)

=

a

∑

i

=

0

j

a

i

b

i

ln

⁡

k

+

v

T

−

j

{\displaystyle V_{T-j}(k)\,=\,a\sum _{i=0}^{j}a^{i}b^{i}\ln k+v_{T-j}}

where each v T − j {\displaystyle v_{T-j}} ({\displaystyle v_{T-j}}) is a constant, and the optimal amount to consume at time t = T − j {\displaystyle t=T-j} ({\displaystyle t=T-j}) is

c

T

−

j

(

k

)

=

1

∑

i

=

0

j

a

i

b

i

A

k

a

{\displaystyle c_{T-j}(k)\,=\,{\frac {1}{\sum _{i=0}^{j}a^{i}b^{i}}}Ak^{a}}

which can be simplified to

c

T

(

k

)

=

A

k

a

c

T

−

1

(

k

)

=

A

k

a

1

+

a

b

c

T

−

2

(

k

)

=

A

k

a

1

+

a

b

+

a

2

b

2

…

c

2

(

k

)

=

A

k

a

1

+

a

b

+

a

2

b

2

+

…

+

a

T

−

2

b

T

−

2

c

1

(

k

)

=

A

k

a

1

+

a

b

+

a

2

b

2

+

…

+

a

T

−

2

b

T

−

2

+

a

T

−

1

b

T

−

1

c

0

(

k

)

=

A

k

a

1

+

a

b

+

a

2

b

2

+

…

+

a

T

−

2

b

T

−

2

+

a

T

−

1

b

T

−

1

+

a

T

b

T

{\displaystyle {\begin{aligned}c_{T}(k)&=Ak^{a}\\c_{T-1}(k)&={\frac {Ak^{a}}{1+ab}}\\c_{T-2}(k)&={\frac {Ak^{a}}{1+ab+a^{2}b^{2}}}\\&\dots \\c_{2}(k)&={\frac {Ak^{a}}{1+ab+a^{2}b^{2}+\ldots +a^{T-2}b^{T-2}}}\\c_{1}(k)&={\frac {Ak^{a}}{1+ab+a^{2}b^{2}+\ldots +a^{T-2}b^{T-2}+a^{T-1}b^{T-1}}}\\c_{0}(k)&={\frac {Ak^{a}}{1+ab+a^{2}b^{2}+\ldots +a^{T-2}b^{T-2}+a^{T-1}b^{T-1}+a^{T}b^{T}}}\end{aligned}}}

We see that it is optimal to consume a larger fraction of current wealth as one gets older, finally consuming all remaining wealth in period T, the last period of life.

### Computer science

There are two key attributes that a problem must have in order for dynamic programming to be applicable: optimal substructure and overlapping sub-problems. If a problem can be solved by combining optimal solutions to *non-overlapping* sub-problems, the strategy is called "divide and conquer" instead. This is why merge sort and quick sort are not classified as dynamic programming problems.

*Optimal substructure* means that the solution to a given optimization problem can be obtained by the combination of optimal solutions to its sub-problems. Such optimal substructures are usually described by means of recursion. For example, given a graph *G=(V,E)*, the shortest path *p* from a vertex *u* to a vertex *v* exhibits optimal substructure: take any intermediate vertex *w* on this shortest path *p*. If *p* is truly the shortest path, then it can be split into sub-paths *p1* from *u* to *w* and *p2* from *w* to *v* such that these, in turn, are indeed the shortest paths between the corresponding vertices (by the simple cut-and-paste argument described in *Introduction to Algorithms*). Hence, one can easily formulate the solution for finding shortest paths in a recursive manner, which is what the Bellman–Ford algorithm or the Floyd–Warshall algorithm does.

*Overlapping* sub-problems means that the space of sub-problems must be small, that is, any recursive algorithm solving the problem should solve the same sub-problems over and over, rather than generating new sub-problems. For example, consider the recursive formulation for generating the Fibonacci sequence: *F**i* = *F**i*−1 + *F**i*−2, with base case *F*1 = *F*2 = 1. Then *F*43 = *F*42 + *F*41, and *F*42 = *F*41 + *F*40. Now *F*41 is being solved in the recursive sub-trees of both *F*43 as well as *F*42. Even though the total number of sub-problems is actually small (only 43 of them), we end up solving the same problems over and over if we adopt a naive recursive solution such as this. Dynamic programming takes account of this fact and solves each sub-problem only once.

This can be achieved in either of two ways:

- *Top-down approach*: This is the direct fall-out of the recursive formulation of any problem. If the solution to any problem can be formulated recursively using the solution to its sub-problems, and if its sub-problems are overlapping, then one can easily memoize or store the solutions to the sub-problems in a table (often an array or hashtable in practice). Whenever we attempt to solve a new sub-problem, we first check the table to see if it is already solved. If a solution has been recorded, we can use it directly, otherwise we solve the sub-problem and add its solution to the table.
- *Bottom-up approach*: Once we formulate the solution to a problem recursively as in terms of its sub-problems, we can try reformulating the problem in a bottom-up fashion: try solving the sub-problems first and use their solutions to build-on and arrive at solutions to bigger sub-problems. This is also usually done in a tabular form by iteratively generating solutions to bigger and bigger sub-problems by using the solutions to small sub-problems. For example, if we already know the values of *F*41 and *F*40, we can directly calculate the value of *F*42.

Some programming languages can automatically memoize the result of a function call with a particular set of arguments, in order to speed up call-by-name evaluation (this mechanism is referred to as *call-by-need*). Some languages make it possible portably (e.g. Scheme, Common Lisp, Perl or D). Some languages have automatic memoization built in, such as tabled Prolog and J, which supports memoization with the *M.* adverb. In any case, this is only possible for a referentially transparent function. Memoization is also encountered as an easily accessible design pattern within term-rewrite based languages such as Wolfram Language.

### Bioinformatics

Dynamic programming is widely used in bioinformatics for tasks such as sequence alignment, protein folding, RNA structure prediction and protein-DNA binding. The first dynamic programming algorithms for protein-DNA binding were developed in the 1970s independently by Charles DeLisi in the US and by Georgii Gurskii and Alexander Zasedatelev in the Soviet Union. Recently these algorithms have become very popular in bioinformatics and computational biology, particularly in the studies of nucleosome positioning and transcription factor binding.
