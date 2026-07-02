---
title: "Lagrange multiplier"
source: https://en.wikipedia.org/wiki/Lagrange_multiplier
domain: optimization
license: CC-BY-SA-4.0
tags: mathematical optimization, linear programming, convex optimization, simplex, lagrange multiplier
fetched: 2026-07-02
---

# Lagrange multiplier

In mathematical optimization, the **method of Lagrange multipliers** is a strategy for finding the local maxima and minima of a function subject to equation constraints (i.e., subject to the condition that one or more equations have to be satisfied exactly by the chosen values of the variables). It is named after the mathematician Joseph-Louis Lagrange.

## Summary and rationale

The basic idea is to convert a constrained problem into a form such that the derivative test of an unconstrained problem can still be applied. The relationship between the gradient of the function and gradients of the constraints rather naturally leads to a reformulation of the original problem, known as the **Lagrangian function** or Lagrangian. In the general case, the Lagrangian is defined as

${\mathcal {L}}(x,\lambda )\equiv f(x)+\langle \lambda ,g(x)\rangle$

for functions $f,g$ ; the notation $\langle \cdot ,\cdot \rangle$ denotes an inner product. The value $\lambda$ is called the **Lagrange multiplier**.

In simple cases, where the inner product is defined as the dot product, the Lagrangian is

${\mathcal {L}}(x,\lambda )\equiv f(x)+\lambda \cdot g(x)$

The method can be summarized as follows: in order to find the maximum or minimum of a function f subject to the equality constraint $g(x)=0$ , find the stationary points of ${\mathcal {L}}$ considered as a function of x and the Lagrange multiplier $\lambda ~$ . This means that all partial derivatives should be zero, including the partial derivative with respect to $\lambda ~$ .

${\frac {\partial {\mathcal {L}}}{\partial x}}=0$

and

${\frac {\ \partial {\mathcal {L}}\ }{\partial \lambda }}=0\ ;$

or equivalently

${\frac {\partial f(x)}{\partial x}}+\lambda \cdot {\frac {\partial g(x)}{\partial x}}=0$

and

$g(x)=0~.$

The solution corresponding to the original constrained optimization is always a saddle point of the Lagrangian function, which can be identified among the stationary points from the definiteness of the bordered Hessian matrix.

The great advantage of this method is that it allows the optimization to be solved without explicit parameterization in terms of the constraints. As a result, the method of Lagrange multipliers is widely used to solve challenging constrained optimization problems. Further, the method of Lagrange multipliers is generalized by the Karush–Kuhn–Tucker conditions, which can also take into account inequality constraints of the form $h(\mathbf {x} )\leq c$ for a given constant c .

## Statement

The following is known as the Lagrange multiplier theorem.

Let $f\colon \mathbb {R} ^{n}\to \mathbb {R}$ be the objective function and let $g\colon \mathbb {R} ^{n}\to \mathbb {R} ^{c}$ be the constraints function, both belonging to $C^{1}$ (that is, having continuous first derivatives). Consider the following constrained optimization problem:

${\begin{aligned}&{\text{maximize }}f(x)\\&{\text{subject to: }}g(x)=0\end{aligned}}$

Let $x_{\star }$ be an optimal solution to the above optimization problem such that, for the matrix of partial derivatives ${\Bigl [}\operatorname {D} g(x_{\star }){\Bigr ]}_{j,k}={\frac {\ \partial g_{j}\ }{\partial x_{k}}}$ , $\operatorname {rank} (\operatorname {D} g(x_{\star }))=c\leq n$ : Then there exists a unique Lagrange multiplier $\lambda _{\star }\in \mathbb {R} ^{c}$ such that $\operatorname {D} f(x_{\star })=\lambda _{\star }^{\mathsf {T}}\operatorname {D} g(x_{\star })~.$ (In this equation, $\lambda _{\star }$ is a column vector, so its transpose $\lambda _{\star }^{\mathsf {T}}$ is a row vector. Alternatively, we can redefine the Lagrange multiplier directly as a row vector and thus avoid the transposition.)

The Lagrange multiplier theorem states that at any local maximum (or minimum) of the function evaluated under the equality constraints, if constraint qualification applies (explained below), then the gradient of the function (at that point) can be expressed as a linear combination of the gradients of the constraints (at that point), with the Lagrange multipliers acting as coefficients. This is equivalent to saying that any direction perpendicular to all gradients of the constraints is also perpendicular to the gradient of the function. Or still, saying that the directional derivative of the function is 0 in every feasible direction.

## Single constraint

For the case of only one constraint and only two choice variables (as exemplified in Figure 1), consider the optimization problem ${\begin{aligned}{\underset {x,y}{\text{maximize}}}\quad &f(x,y)\\{\text{subject to}}\quad &g(x,y)=0.\end{aligned}}$ (Sometimes an additive constant is shown separately rather than being included in g , in which case the constraint is written $g(x,y)=c,$ as in Figure 1.) We assume that both f and g have continuous first partial derivatives. We introduce a new variable ( $\lambda$ ) called a **Lagrange multiplier** (or **Lagrange undetermined multiplier**) and study the **Lagrange function** (or **Lagrangian** or **Lagrangian expression**) defined by ${\mathcal {L}}(x,y,\lambda )=f(x,y)+\lambda \cdot g(x,y),$ where the $\lambda$ term may be either added or subtracted. If $f(x_{0},y_{0})$ is a maximum of $f(x,y)$ for the original constrained problem and $\nabla g(x_{0},y_{0})\neq 0,$ then there exists $\lambda _{0}$ such that ( $x_{0},y_{0},\lambda _{0}$ ) is a *stationary point* for the Lagrange function (stationary points are those points where the first partial derivatives of ${\mathcal {L}}$ are zero). The assumption $\nabla g\neq 0$ is called constraint qualification. However, not all stationary points yield a solution of the original problem, as the method of Lagrange multipliers yields only a necessary condition for optimality in constrained problems. Sufficient conditions for a minimum or maximum also exist, but if a particular candidate solution satisfies the sufficient conditions, it is only guaranteed that that solution is the best one *locally* – that is, it is better than any permissible nearby points. The *global* optimum can be found by comparing the values of the original objective function at the points satisfying the necessary and locally sufficient conditions.

The method of Lagrange multipliers relies on the intuition that at a maximum, *f*(*x*, *y*) cannot be increasing in the direction of any such neighboring point that also has *g* = 0. If it were, we could walk along *g* = 0 to get higher, meaning that the starting point wasn't actually the maximum. Viewed in this way, it is an exact analogue to testing if the derivative of an unconstrained function is 0, that is, we are verifying that the directional derivative is 0 in any relevant (viable) direction.

We can visualize contours of f given by *f*(*x*, *y*) = *d* for various values of d, and the contour of g given by *g*(*x*, *y*) = *c*.

Suppose we walk along the contour line with *g* = *c* . We are interested in finding points where f almost does not change as we walk, since these points might be maxima.

There are two ways this could happen:

1. We could touch a contour line of f, since by definition f does not change as we walk along its contour lines. This would mean that the tangents to the contour lines of f and g are parallel here.
2. We have reached a "level" part of f, meaning that f does not change in any direction.

To check the first possibility (we touch a contour line of f), notice that since the gradient of a function is perpendicular to the contour lines, the tangents to the contour lines of f and g are parallel if and only if the gradients of f and g are parallel. Thus we want points (*x*, *y*) where *g*(*x*, *y*) = *c* and $\nabla _{x,y}f=\lambda \,\nabla _{x,y}g,$ for some $\lambda$ where $\nabla _{x,y}f=\left({\frac {\partial f}{\partial x}},{\frac {\partial f}{\partial y}}\right),\qquad \nabla _{x,y}g=\left({\frac {\partial g}{\partial x}},{\frac {\partial g}{\partial y}}\right)$ are the respective gradients. The constant $\lambda$ is required because although the two gradient vectors are parallel, the magnitudes of the gradient vectors are generally not equal. This constant is called the Lagrange multiplier. (In some conventions $\lambda$ is preceded by a minus sign).

Notice that this method also solves the second possibility, that f is level: if f is level, then its gradient is zero, and setting $\lambda =0$ is a solution regardless of $\nabla _{x,y}g$ .

To incorporate these conditions into one equation, we introduce an auxiliary function ${\mathcal {L}}(x,y,\lambda )\equiv f(x,y)+\lambda \cdot g(x,y)\,,$ and solve $\nabla _{x,y,\lambda }{\mathcal {L}}(x,y,\lambda )=0~.$ Note that this amounts to solving three equations in three unknowns. This is the method of Lagrange multipliers.

Note that $\ \nabla _{\lambda }{\mathcal {L}}(x,y,\lambda )=0\$ implies $\ g(x,y)=0\ ,$ as the partial derivative of ${\mathcal {L}}$ with respect to $\lambda$ is $\ g(x,y)~.$

To summarize $\nabla _{x,y,\lambda }{\mathcal {L}}(x,y,\lambda )=0\iff {\begin{cases}\nabla _{x,y}f(x,y)=-\lambda \,\nabla _{x,y}g(x,y)\\g(x,y)=0\end{cases}}$ The method generalizes readily to functions on n variables $\nabla _{x_{1},\dots ,x_{n},\lambda }{\mathcal {L}}(x_{1},\dots ,x_{n},\lambda )=0$ which amounts to solving *n* + 1 equations in *n* + 1 unknowns.

The constrained extrema of f are *critical points* of the Lagrangian ${\mathcal {L}}$ , but they are not necessarily *local extrema* of ${\mathcal {L}}$ (see § Example 2 below).

One may reformulate the Lagrangian as a Hamiltonian, in which case the solutions are local minima for the Hamiltonian. This is done in optimal control theory, in the form of Pontryagin's maximum principle.

The fact that solutions of the method of Lagrange multipliers are not necessarily extrema of the Lagrangian, also poses difficulties for numerical optimization. This can be addressed by minimizing the *magnitude* of the gradient of the Lagrangian, as these minima are the same as the zeros of the magnitude, as illustrated in Example 5: Numerical optimization.

## Multiple constraints

The method of Lagrange multipliers can be extended to solve problems with multiple constraints using a similar argument. Consider a paraboloid subject to two line constraints that intersect at a single point. As the only feasible solution, this point is obviously a constrained extremum. However, the level set of f is clearly not parallel to either constraint at the intersection point (see Figure 3); instead, it is a linear combination of the two constraints' gradients. In the case of multiple constraints, that will be what we seek in general: The method of Lagrange seeks points not at which the gradient of f is a multiple of any single constraint's gradient necessarily, but in which it is a linear combination of all the constraints' gradients.

Concretely, suppose we have M constraints and are walking along the set of points satisfying $g_{i}(\mathbf {x} )=0,i=1,\dots ,M\,.$ Every point $\mathbf {x}$ on the contour of a given constraint function $g_{i}$ has a space of allowable directions: the space of vectors perpendicular to $\nabla g_{i}(\mathbf {x} )\,.$ The set of directions that are allowed by all constraints is thus the space of directions perpendicular to all of the constraints' gradients. Denote this space of allowable moves by $\ A\$ and denote the span of the constraints' gradients by $S\,.$ Then $A=S^{\perp }\,,$ the space of vectors perpendicular to every element of $S\,.$

We are still interested in finding points where f does not change as we walk, since these points might be (constrained) extrema. We therefore seek $\mathbf {x}$ such that any allowable direction of movement away from $\mathbf {x}$ is perpendicular to $\nabla f(\mathbf {x} )$ (otherwise we could increase f by moving along that allowable direction). In other words, $\nabla f(\mathbf {x} )\in A^{\perp }=S\,.$ Thus there are scalars $\lambda _{1},\lambda _{2},\ \dots ,\lambda _{M}$ such that $\nabla f(\mathbf {x} )=\sum _{k=1}^{M}\lambda _{k}\,\nabla g_{k}(\mathbf {x} )\quad \iff \quad \nabla f(\mathbf {x} )-\sum _{k=1}^{M}{\lambda _{k}\nabla g_{k}(\mathbf {x} )}=0~.$

These scalars are the Lagrange multipliers. We now have M of them, one for every constraint.

As before, we introduce an auxiliary function ${\mathcal {L}}\left(x_{1},\ldots ,x_{n},\lambda _{1},\ldots ,\lambda _{M}\right)=f\left(x_{1},\ldots ,x_{n}\right)-\sum \limits _{k=1}^{M}{\lambda _{k}g_{k}\left(x_{1},\ldots ,x_{n}\right)}\$ and solve $\nabla _{x_{1},\ldots ,x_{n},\lambda _{1},\ldots ,\lambda _{M}}{\mathcal {L}}(x_{1},\ldots ,x_{n},\lambda _{1},\ldots ,\lambda _{M})=0\iff {\begin{cases}\nabla f(\mathbf {x} )-\sum _{k=1}^{M}{\lambda _{k}\,\nabla g_{k}(\mathbf {x} )}=0\\g_{1}(\mathbf {x} )=\cdots =g_{M}(\mathbf {x} )=0\end{cases}}$ which amounts to solving $n+M$ equations in $\ n+M\$ unknowns.

The constraint qualification assumption when there are multiple constraints is that the constraint gradients at the relevant point are linearly independent.

## Modern formulation via differentiable manifolds

The problem of finding the local maxima and minima subject to constraints can be generalized to finding local maxima and minima on a differentiable manifold $\ M~.$ In what follows, it is not necessary that M be a Euclidean space, or even a Riemannian manifold. All appearances of the gradient $\ \nabla \$ (which depends on a choice of Riemannian metric) can be replaced with the exterior derivative $\ \operatorname {d}$ .

### Single constraint

Let $\ M\$ be a smooth manifold of dimension $\ m~.$ Suppose that we wish to find the stationary points $\ x\$ of a smooth function $\ f:M\to \mathbb {R} \$ when restricted to the submanifold $\ N\$ defined by $\ g(x)=0\ ,$ where $\ g:M\to \mathbb {R} \$ is a smooth function for which 0 is a regular value.

Let $\ \operatorname {d} f\$ and $\ \operatorname {d} g\$ be the exterior derivatives of $\ f\$ and $\ g\$ . Stationarity for the restriction $\ f|_{N}\$ at $\ x\in N\$ means $\ \operatorname {d} (f|_{N})_{x}=0~.$ Equivalently, the kernel $\ \ker(\operatorname {d} f_{x})\$ contains $\ T_{x}N=\ker(\operatorname {d} g_{x})~.$ In other words, $\ \operatorname {d} f_{x}\$ and $\ \operatorname {d} g_{x}\$ are proportional 1-forms. For this it is necessary and sufficient that the following system of $\ {\tfrac {1}{2}}m(m-1)\$ equations holds: $\operatorname {d} f_{x}\wedge \operatorname {d} g_{x}=0\in \Lambda ^{2}(T_{x}^{\ast }M)$ where $\ \wedge \$ denotes the exterior product. The stationary points $\ x\$ are the solutions of the above system of equations plus the constraint $\ g(x)=0~.$ Note that the $\ {\tfrac {1}{2}}m(m-1)\$ equations are not independent, since the left-hand side of the equation belongs to the subvariety of $\ \Lambda ^{2}(T_{x}^{\ast }M)\$ consisting of decomposable elements.

In this formulation, it is not necessary to explicitly find the Lagrange multiplier, a number $\ \lambda \$ such that $\ \operatorname {d} f_{x}=\lambda \cdot \operatorname {d} g_{x}~.$

### Multiple constraints

Let $\ M\$ and $\ f\$ be as in the above section regarding the case of a single constraint. Rather than the function g described there, now consider a smooth function $\ G:M\to \mathbb {R} ^{p}(p>1)\ ,$ with component functions $\ g_{i}:M\to \mathbb {R} \ ,$ for which $0\in \mathbb {R} ^{p}$ is a regular value. Let N be the submanifold of $\ M\$ defined by $\ G(x)=0~.$

$\ x\$ is a stationary point of $f|_{N}$ if and only if $\ \ker(\operatorname {d} f_{x})\$ contains $\ \ker(\operatorname {d} G_{x})~.$ For convenience let $\ L_{x}=\operatorname {d} f_{x}\$ and $\ K_{x}=\operatorname {d} G_{x}\ ,$ where $\ \operatorname {d} G$ denotes the tangent map or Jacobian $\ TM\to T\mathbb {R} ^{p}~$ ( $\ T_{x}\mathbb {R} ^{p}$ can be canonically identified with $\ \mathbb {R} ^{p}$ ). The subspace $\ker(K_{x})$ has dimension smaller than that of $\ker(L_{x})$ , namely $\ \dim(\ker(L_{x}))=n-1\$ and $\ \dim(\ker(K_{x}))=n-p~.$ $\ker(K_{x})$ belongs to $\ \ker(L_{x})\$ if and only if $L_{x}\in T_{x}^{\ast }M$ belongs to the image of $\ K_{x}^{\ast }:\mathbb {R} ^{p\ast }\to T_{x}^{\ast }M~.$ Computationally speaking, the condition is that $L_{x}$ belongs to the row space of the matrix of $\ K_{x}\ ,$ or equivalently the column space of the matrix of $K_{x}^{\ast }$ (the transpose). If $\ \omega _{x}\in \Lambda ^{p}(T_{x}^{\ast }M)\$ denotes the exterior product of the columns of the matrix of $\ K_{x}^{\ast }\ ,$ the stationary condition for $\ f|_{N}\$ at $\ x\$ becomes $L_{x}\wedge \omega _{x}=0\in \Lambda ^{p+1}\left(T_{x}^{\ast }M\right)$ Once again, in this formulation it is not necessary to explicitly find the Lagrange multipliers, the numbers $\ \lambda _{1},\ldots ,\lambda _{p}\$ such that $\ \operatorname {d} f_{x}=\sum _{i=1}^{p}\lambda _{i}\operatorname {d} (g_{i})_{x}~.$

## Interpretation of the Lagrange multipliers

In this section, we modify the constraint equations from the form $g_{i}({\bf {x}})=0$ to the form $\ g_{i}({\bf {x}})=c_{i}\ ,$ where the $\ c_{i}\$ are m real constants that are considered to be additional arguments of the Lagrangian expression ${\mathcal {L}}$ .

Often the Lagrange multipliers have an interpretation as some quantity of interest. For example, by parametrising the constraint's contour line, that is, if the Lagrangian expression is ${\begin{aligned}&{\mathcal {L}}(x_{1},x_{2},\ldots ;\lambda _{1},\lambda _{2},\ldots ;c_{1},c_{2},\ldots )\\[4pt]={}&f(x_{1},x_{2},\ldots )+\lambda _{1}(c_{1}-g_{1}(x_{1},x_{2},\ldots ))+\lambda _{2}(c_{2}-g_{2}(x_{1},x_{2},\dots ))+\cdots \end{aligned}}$ then $\ {\frac {\partial {\mathcal {L}}}{\partial c_{k}}}=\lambda _{k}~.$

So, *λk* is the rate of change of the quantity being optimized as a function of the constraint parameter. As examples, in Lagrangian mechanics the equations of motion are derived by finding stationary points of the action, the time integral of the difference between kinetic and potential energy. Thus, the force on a particle due to a scalar potential, *F* = −∇*V*, can be interpreted as a Lagrange multiplier determining the change in action (transfer of potential to kinetic energy) following a variation in the particle's constrained trajectory. In control theory this is formulated instead as costate equations.

Moreover, by the envelope theorem the optimal value of a Lagrange multiplier has an interpretation as the marginal effect of the corresponding constraint constant upon the optimal attainable value of the original objective function: If we denote values at the optimum with a star ( $\star$ ), then it can be shown that ${\frac {\ \operatorname {d} f\left(\ x_{1\star }(c_{1},c_{2},\dots ),\ x_{2\star }(c_{1},c_{2},\dots ),\ \dots \ \right)\ }{\operatorname {d} c_{k}}}=\lambda _{\star k}~.$

For example, in economics the optimal profit to a player is calculated subject to a constrained space of actions, where a Lagrange multiplier is the change in the optimal value of the objective function (profit) due to the relaxation of a given constraint (e.g. through a change in income); in such a context $\ \lambda _{\star k}\$ is the marginal cost of the constraint, and is referred to as the shadow price.

## Sufficient conditions

Sufficient conditions for a constrained local maximum or minimum can be stated in terms of a sequence of principal minors (determinants of upper-left-justified sub-matrices) of the bordered Hessian matrix of second derivatives of the Lagrangian expression.

## Examples

### Example 1

Suppose we wish to maximize $\ f(x,y)=x+y\$ subject to the constraint $\ x^{2}+y^{2}=1~.$ The feasible set is the unit circle, and the level sets of f are diagonal lines (with slope −1), so we can see graphically that the maximum occurs at $\ \left({\tfrac {1}{\sqrt {2}}},{\tfrac {1}{\sqrt {2}}}\right)\ ,$ and that the minimum occurs at $\ \left(-{\tfrac {1}{\sqrt {2}}},-{\tfrac {1}{\sqrt {2}}}\right)~.$

For the method of Lagrange multipliers, the constraint is $g(x,y)=x^{2}+y^{2}-1=0\ ,$ hence the Lagrangian function, ${\begin{aligned}{\mathcal {L}}(x,y,\lambda )&=f(x,y)+\lambda \cdot g(x,y)\\[4pt]&=x+y+\lambda (x^{2}+y^{2}-1)\ ,\end{aligned}}$ is a function that is equivalent to $\ f(x,y)\$ when $\ g(x,y)\$ is set to 0.

Now we can calculate the gradient: ${\begin{aligned}\nabla _{x,y,\lambda }{\mathcal {L}}(x,y,\lambda )&=\left({\frac {\partial {\mathcal {L}}}{\partial x}},{\frac {\partial {\mathcal {L}}}{\partial y}},{\frac {\partial {\mathcal {L}}}{\partial \lambda }}\right)\\[4pt]&=\left(1+2\lambda x,1+2\lambda y,x^{2}+y^{2}-1\right)\ \color {gray}{,}\end{aligned}}$ and therefore: $\nabla _{x,y,\lambda }{\mathcal {L}}(x,y,\lambda )=0\quad \Leftrightarrow \quad {\begin{cases}1+2\lambda x=0\\1+2\lambda y=0\\x^{2}+y^{2}-1=0\end{cases}}$

Notice that the last equation is the original constraint.

The first two equations yield $x=y=-{\frac {1}{2\lambda }},\qquad \lambda \neq 0~.$ By substituting into the last equation we have: ${\frac {1}{4\lambda ^{2}}}+{\frac {1}{4\lambda ^{2}}}-1=0\ ,$ so $\lambda =\pm {\frac {1}{\sqrt {2\ }}}\ ,$ which implies that the stationary points of ${\mathcal {L}}$ are $\left({\tfrac {\sqrt {2\ }}{2}},{\tfrac {\sqrt {2\ }}{2}},-{\tfrac {1}{\sqrt {2\ }}}\right),\qquad \left(-{\tfrac {\sqrt {2\ }}{2}},-{\tfrac {\sqrt {2\ }}{2}},{\tfrac {1}{\sqrt {2\ }}}\right)~.$

Evaluating the objective function f at these points yields $f\left({\tfrac {\sqrt {2\ }}{2}},{\tfrac {\sqrt {2\ }}{2}}\right)={\sqrt {2\ }}\ ,\qquad f\left(-{\tfrac {\sqrt {2\ }}{2}},-{\tfrac {\sqrt {2\ }}{2}}\right)=-{\sqrt {2\ }}~.$

Thus the constrained maximum is $\ {\sqrt {2\ }}\$ and the constrained minimum is $-{\sqrt {2}}$ .

### Example 2

Now we modify the objective function of Example **1** so that we minimize $\ f(x,y)=(x+y)^{2}\$ instead of $\ f(x,y)=x+y\ ,$ again along the circle $\ g(x,y)=x^{2}+y^{2}-1=0~.$ Now the level sets of f are still lines of slope −1, and the points on the circle tangent to these level sets are again $\ ({\sqrt {2}}/2,{\sqrt {2}}/2)\$ and $\ (-{\sqrt {2}}/2,-{\sqrt {2}}/2)~.$ These tangency points are maxima of $\ f~.$

On the other hand, the minima occur on the level set for $\ f=0\$ (since by its construction $\ f\$ cannot take negative values), at $\ ({\sqrt {2}}/2,-{\sqrt {2}}/2)\$ and $\ (-{\sqrt {2}}/2,{\sqrt {2}}/2)\ ,$ where the level curves of $\ f\$ are not tangent to the constraint. The condition that $\ \nabla _{x,y,\lambda }\left(f(x,y)+\lambda \cdot g(x,y)\right)=0\$ correctly identifies all four points as extrema; the minima are characterized in by $\ \lambda =0\$ and the maxima by $\ \lambda =-2~.$

### Example 3

This example deals with more strenuous calculations, but it is still a single constraint problem.

Suppose one wants to find the maximum values of $f(x,y)=x^{2}y$ with the condition that the $\ x\$ - and $\ y\$ -coordinates lie on the circle around the origin with radius $\ {\sqrt {3\ }}~.$ That is, subject to the constraint $g(x,y)=x^{2}+y^{2}-3=0~.$

As there is just a single constraint, there is a single multiplier, say $\ \lambda ~.$

The constraint $\ g(x,y)\$ is identically zero on the circle of radius $\ {\sqrt {3\ }}~.$ Any multiple of $\ g(x,y)\$ may be added to $\ g(x,y)\$ leaving $\ g(x,y)\$ unchanged in the region of interest (on the circle where our original constraint is satisfied).

Applying the ordinary Lagrange multiplier method yields ${\begin{aligned}{\mathcal {L}}(x,y,\lambda )&=f(x,y)+\lambda \cdot g(x,y)\\&=x^{2}y+\lambda (x^{2}+y^{2}-3)\ ,\end{aligned}}$ from which the gradient can be calculated: ${\begin{aligned}\nabla _{x,y,\lambda }{\mathcal {L}}(x,y,\lambda )&=\left({\frac {\partial {\mathcal {L}}}{\partial x}},{\frac {\partial {\mathcal {L}}}{\partial y}},{\frac {\partial {\mathcal {L}}}{\partial \lambda }}\right)\\&=\left(2xy+2\lambda x,x^{2}+2\lambda y,x^{2}+y^{2}-3\right)~.\end{aligned}}$ And therefore: $\nabla _{x,y,\lambda }{\mathcal {L}}(x,y,\lambda )=0\quad \iff \quad {\begin{cases}2xy+2\lambda x=0\\x^{2}+2\lambda y=0\\x^{2}+y^{2}-3=0\end{cases}}\quad \iff \quad {\begin{cases}x(y+\lambda )=0&{\text{(i)}}\\x^{2}=-2\lambda y&{\text{(ii)}}\\x^{2}+y^{2}=3&{\text{(iii)}}\end{cases}}$ (iii) is just the original constraint. (i) implies $\ x=0\$ or $\ \lambda =-y~.$ If $x=0$ then $\ y=\pm {\sqrt {3\ }}\$ by (iii) and consequently $\ \lambda =0\$ from (ii). If $\ \lambda =-y\ ,$ substituting this into (ii) yields $\ x^{2}=2y^{2}~.$ Substituting this into (iii) and solving for $\ y\$ gives $\ y=\pm 1~.$ Thus there are six critical points of $\ {\mathcal {L}}\ :$ $({\sqrt {2\ }},1,-1);\quad (-{\sqrt {2\ }},1,-1);\quad ({\sqrt {2\ }},-1,1);\quad (-{\sqrt {2\ }},-1,1);\quad (0,{\sqrt {3\ }},0);\quad (0,-{\sqrt {3\ }},0)~.$

Evaluating the objective at these points, one finds that $f(\pm {\sqrt {2\ }},1)=2;\quad f(\pm {\sqrt {2\ }},-1)=-2;\quad f(0,\pm {\sqrt {3\ }})=0~.$

Therefore, the objective function attains the global maximum (subject to the constraints) at $\ (\pm {\sqrt {2\ }},1\ )$ and the global minimum at $\ (\pm {\sqrt {2\ }},-1)~.$ The point $\ (0,{\sqrt {3\ }})\$ is a local minimum of $\ f\$ and $\ (0,-{\sqrt {3\ }})\$ is a local maximum of $\ f\ ,$ as may be determined by consideration of the Hessian matrix of $\ {\mathcal {L}}(x,y,0)~.$

Note that while $\ ({\sqrt {2\ }},1,-1)\$ is a critical point of $\ {\mathcal {L}}\ ,$ it is not a local extremum of $\ {\mathcal {L}}~.$ We have ${\mathcal {L}}\left({\sqrt {2\ }}+\varepsilon ,1,-1+\delta \right)=2+\delta \left(\varepsilon ^{2}+\left(2{\sqrt {2\ }}\right)\varepsilon \right)~.$

Given any neighbourhood of $\ ({\sqrt {2\ }},1,-1)\ ,$ one can choose a small positive $\ \varepsilon \$ and a small $\ \delta \$ of either sign to get $\ {\mathcal {L}}$ values both greater and less than $\ 2~.$ This can also be seen from the Hessian matrix of $\ {\mathcal {L}}\$ evaluated at this point (or indeed at any of the critical points) which is an indefinite matrix. Each of the critical points of $\ {\mathcal {L}}\$ is a saddle point of $\ {\mathcal {L}}~.$

### Example 4 – Entropy

Suppose we wish to find the discrete probability distribution on the points $\ \{p_{1},p_{2},\ldots ,p_{n}\}\$ with maximal information entropy. This is the same as saying that we wish to find the least structured probability distribution on the points $\ \{p_{1},p_{2},\cdots ,p_{n}\}~.$ In other words, we wish to maximize the Shannon entropy equation: $f(p_{1},p_{2},\ldots ,p_{n})=-\sum _{j=1}^{n}p_{j}\log _{2}p_{j}~.$

For this to be a probability distribution the sum of the probabilities $\ p_{i}\$ at each point $\ x_{i}\$ must equal 1, so our constraint is: $g(p_{1},p_{2},\ldots ,p_{n})=\sum _{j=1}^{n}p_{j}=1~.$

We use Lagrange multipliers to find the point of maximum entropy, $\ {\vec {p}}^{\,*}\ ,$ across all discrete probability distributions $\ {\vec {p}}\$ on $\ \{x_{1},x_{2},\ldots ,x_{n}\}~.$ We require that: $\left.{\frac {\partial }{\partial {\vec {p}}}}(f+\lambda (g-1))\right|_{{\vec {p}}={\vec {p}}^{\,*}}=0\ ,$ which gives a system of n equations, $\ k=1,\ \ldots ,n\ ,$ such that: $\left.{\frac {\partial }{\partial p_{k}}}\left\{-\left(\sum _{j=1}^{n}p_{j}\log _{2}p_{j}\right)+\lambda \left(\sum _{j=1}^{n}p_{j}-1\right)\right\}\right|_{p_{k}=p_{\star k}}=0~.$

Carrying out the differentiation of these n equations, we get $-\left({\frac {1}{\ln 2}}+\log _{2}p_{\star k}\right)+\lambda =0~.$

This shows that all $\ p_{\star k}\$ are equal (because they depend on λ only). By using the constraint $\sum _{j}p_{j}=1\ ,$ we find $p_{\star k}={\frac {1}{n}}~.$

Hence, the uniform distribution is the distribution with the greatest entropy, among distributions on n points.

### Example 5 – Numerical optimization

The critical points of Lagrangians occur at saddle points, rather than at local maxima (or minima). Unfortunately, many numerical optimization techniques, such as hill climbing, gradient descent, some of the quasi-Newton methods, among others, are designed to find local maxima (or minima) and not saddle points. For this reason, one must either modify the formulation to ensure that it's a minimization problem (for example, by extremizing the square of the gradient of the Lagrangian as below), or else use an optimization technique that finds stationary points (such as Newton's method without an extremum seeking line search) and not necessarily extrema.

As a simple example, consider the problem of finding the value of x that minimizes $\ f(x)=x^{2}\ ,$ constrained such that $\ x^{2}=1~.$ (This problem is somewhat untypical because there are only two values that satisfy this constraint, but it is useful for illustration purposes because the corresponding unconstrained function can be visualized in three dimensions.)

Using Lagrange multipliers, this problem can be converted into an unconstrained optimization problem: ${\mathcal {L}}(x,\lambda )=x^{2}+\lambda (x^{2}-1)~.$

The two critical points occur at saddle points where *x* = 1 and *x* = −1.

In order to solve this problem with a numerical optimization technique, we must first transform this problem such that the critical points occur at local minima. This is done by computing the magnitude of the gradient of the unconstrained optimization problem.

First, we compute the partial derivative of the unconstrained problem with respect to each variable: ${\begin{aligned}&{\frac {\partial {\mathcal {L}}}{\partial x}}=2x+2x\lambda \\[5pt]&{\frac {\partial {\mathcal {L}}}{\partial \lambda }}=x^{2}-1~.\end{aligned}}$

If the target function is not easily differentiable, the differential with respect to each variable can be approximated as ${\begin{aligned}{\frac {\ \partial {\mathcal {L}}\ }{\partial x}}\approx {\frac {{\mathcal {L}}(x+\varepsilon ,\lambda )-{\mathcal {L}}(x,\lambda )}{\varepsilon }},\\[5pt]{\frac {\ \partial {\mathcal {L}}\ }{\partial \lambda }}\approx {\frac {{\mathcal {L}}(x,\lambda +\varepsilon )-{\mathcal {L}}(x,\lambda )}{\varepsilon }},\end{aligned}}$ where $\varepsilon$ is a small value.

Next, we compute the magnitude of the gradient, which is the square root of the sum of the squares of the partial derivatives: ${\begin{aligned}h(x,\lambda )&={\sqrt {(2x+2x\lambda )^{2}+(x^{2}-1)^{2}\ }}\\[4pt]&\approx {\sqrt {\left({\frac {\ {\mathcal {L}}(x+\varepsilon ,\lambda )-{\mathcal {L}}(x,\lambda )\ }{\varepsilon }}\right)^{2}+\left({\frac {\ {\mathcal {L}}(x,\lambda +\varepsilon )-{\mathcal {L}}(x,\lambda )\ }{\varepsilon }}\right)^{2}\ }}~.\end{aligned}}$

(Since magnitude is always non-negative, optimizing over the squared-magnitude is equivalent to optimizing over the magnitude. Thus, the "square root" may be omitted from these equations with no expected difference in the results of optimization.)

The critical points of h occur at *x* = 1 and *x* = −1, just as in ${\mathcal {L}}~.$ Unlike the critical points in ${\mathcal {L}}\,,$ however, the critical points in h occur at local minima, so numerical optimization techniques can be used to find them.

## Applications

### Lagrangian Mechanics

In Lagrangian Mechanics, the Euler-Lagrange equations can be augmented with Lagrange multipliers as a method to impose physical constraints on systems. This method is not required in general, because an alternative method is to choose a set of linearly independent generalised coordinates such that the constraints are implicitly imposed.

When Lagrange multipliers are used, the constraint equations need to be simultaneously solved with the Euler-Lagrange equations. Hence, the equations become a system of differential algebraic equations (as opposed to a system of ordinary differential equations).

The method of Lagrange multipliers is useful when it is difficult to write the Lagrangian in terms of a set of linearly independent generalised coordinates. For example, for use in programmatic dynamical systems modelling algorithms, or for use in modelling systems with closed kinematic chains. They are also useful for imposing non-holonomic constraints.

Given a set of holonomic constraint equations $f_{j}(\mathbf {q} ,t)=0$ , the Euler-Lagrange equations with Lagrange multipliers can be written as

${\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L}{\partial {\dot {q}}_{i}}}-{\frac {\partial L}{\partial q_{i}}}+\underbrace {\sum _{j=1}^{C}\lambda _{j}{\frac {\partial f_{j}}{\partial q_{i}}}} _{-\tau _{i,{\text{constraint}}}}=\tau _{i}$

The meaning of $\tau _{i,{\text{constraint}}}$ can be interpreted by moving it to the other side of the equation and absorbing it into the generalised force term $\tau _{i}$ . In this interpretation, the system has C number of additional degrees of freedom, and there are no additionally imposed constraints, but the constraint forces $\tau _{i,{\text{constraint}}}$ just happen to have the right values such that the constraints hold.

### Control theory

In optimal control theory, the Lagrange multipliers are interpreted as costate variables, and Lagrange multipliers are reformulated as the minimization of the Hamiltonian, in Pontryagin's maximum principle.

### Nonlinear programming

The Lagrange multiplier method has several generalizations. In nonlinear programming there are several multiplier rules, e.g. the Carathéodory–John Multiplier Rule and the Convex Multiplier Rule, for inequality constraints.

### Economics

In many models in mathematical economics such as general equilibrium models, consumer behavior is implemented as utility maximization and firm behavior as profit maximization, both entities being subject to constraints such as budget constraints and production constraints. The usual way to determine an optimal solution is achieved by maximizing some function, where the constraints are enforced using Lagrangian multipliers.

### Power systems

Methods based on Lagrange multipliers have applications in power systems, e.g. in distributed-energy-resources (DER) placement and load shedding.

### Safe Reinforcement Learning

The method of Lagrange multipliers applies to constrained Markov decision processes. It naturally produces gradient-based primal-dual algorithms in safe reinforcement learning.

### Normalized solutions

Considering the PDE problems with constraints, i.e., the study of the properties of the normalized solutions, Lagrange multipliers play an important role.
