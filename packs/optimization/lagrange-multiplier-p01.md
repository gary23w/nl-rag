---
title: "Lagrange multiplier (part 1/2)"
source: https://en.wikipedia.org/wiki/Lagrange_multiplier
domain: optimization
license: CC-BY-SA-4.0
tags: mathematical optimization, linear programming, convex optimization, simplex, lagrange multiplier
fetched: 2026-07-02
part: 1/2
---

# Lagrange multiplier

In mathematical optimization, the **method of Lagrange multipliers** is a strategy for finding the local maxima and minima of a function subject to equation constraints (i.e., subject to the condition that one or more equations have to be satisfied exactly by the chosen values of the variables). It is named after the mathematician Joseph-Louis Lagrange.


## Summary and rationale

The basic idea is to convert a constrained problem into a form such that the derivative test of an unconstrained problem can still be applied. The relationship between the gradient of the function and gradients of the constraints rather naturally leads to a reformulation of the original problem, known as the **Lagrangian function** or Lagrangian. In the general case, the Lagrangian is defined as

L ( x , λ ) ≡ f ( x ) + ⟨ λ , g ( x ) ⟩ {\displaystyle {\mathcal {L}}(x,\lambda )\equiv f(x)+\langle \lambda ,g(x)\rangle } ({\displaystyle {\mathcal {L}}(x,\lambda )\equiv f(x)+\langle \lambda ,g(x)\rangle })

for functions f , g {\displaystyle f,g} ({\displaystyle f,g}); the notation ⟨ ⋅ , ⋅ ⟩ {\displaystyle \langle \cdot ,\cdot \rangle } ({\displaystyle \langle \cdot ,\cdot \rangle }) denotes an inner product. The value λ {\displaystyle \lambda } ({\displaystyle \lambda }) is called the **Lagrange multiplier**.

In simple cases, where the inner product is defined as the dot product, the Lagrangian is

L ( x , λ ) ≡ f ( x ) + λ ⋅ g ( x ) {\displaystyle {\mathcal {L}}(x,\lambda )\equiv f(x)+\lambda \cdot g(x)} ({\displaystyle {\mathcal {L}}(x,\lambda )\equiv f(x)+\lambda \cdot g(x)})

The method can be summarized as follows: in order to find the maximum or minimum of a function f {\displaystyle f} ({\displaystyle f}) subject to the equality constraint g ( x ) = 0 {\displaystyle g(x)=0} ({\displaystyle g(x)=0}), find the stationary points of L {\displaystyle {\mathcal {L}}} ({\displaystyle {\mathcal {L}}}) considered as a function of x {\displaystyle x} ({\displaystyle x}) and the Lagrange multiplier λ   {\displaystyle \lambda ~} ({\displaystyle \lambda ~}). This means that all partial derivatives should be zero, including the partial derivative with respect to λ   {\displaystyle \lambda ~} ({\displaystyle \lambda ~}).

∂

L

∂

x

=

0

{\displaystyle {\frac {\partial {\mathcal {L}}}{\partial x}}=0}

and

∂

L

∂

λ

=

0

;

{\displaystyle {\frac {\ \partial {\mathcal {L}}\ }{\partial \lambda }}=0\ ;}

or equivalently

∂

f

(

x

)

∂

x

+

λ

⋅

∂

g

(

x

)

∂

x

=

0

{\displaystyle {\frac {\partial f(x)}{\partial x}}+\lambda \cdot {\frac {\partial g(x)}{\partial x}}=0}

and

g

(

x

)

=

0

.

{\displaystyle g(x)=0~.}

The solution corresponding to the original constrained optimization is always a saddle point of the Lagrangian function, which can be identified among the stationary points from the definiteness of the bordered Hessian matrix.

The great advantage of this method is that it allows the optimization to be solved without explicit parameterization in terms of the constraints. As a result, the method of Lagrange multipliers is widely used to solve challenging constrained optimization problems. Further, the method of Lagrange multipliers is generalized by the Karush–Kuhn–Tucker conditions, which can also take into account inequality constraints of the form h ( x ) ≤ c {\displaystyle h(\mathbf {x} )\leq c} ({\displaystyle h(\mathbf {x} )\leq c}) for a given constant c {\displaystyle c} ({\displaystyle c}).


## Statement

The following is known as the Lagrange multiplier theorem.

Let f : R n → R {\displaystyle f\colon \mathbb {R} ^{n}\to \mathbb {R} } ({\displaystyle f\colon \mathbb {R} ^{n}\to \mathbb {R} }) be the objective function and let g : R n → R c {\displaystyle g\colon \mathbb {R} ^{n}\to \mathbb {R} ^{c}} ({\displaystyle g\colon \mathbb {R} ^{n}\to \mathbb {R} ^{c}}) be the constraints function, both belonging to C 1 {\displaystyle C^{1}} ({\displaystyle C^{1}}) (that is, having continuous first derivatives). Consider the following constrained optimization problem:

maximize  f ( x ) subject to:  g ( x ) = 0 {\displaystyle {\begin{aligned}&{\text{maximize }}f(x)\\&{\text{subject to: }}g(x)=0\end{aligned}}} ({\displaystyle {\begin{aligned}&{\text{maximize }}f(x)\\&{\text{subject to: }}g(x)=0\end{aligned}}})

Let x ⋆ {\displaystyle x_{\star }} ({\displaystyle x_{\star }}) be an optimal solution to the above optimization problem such that, for the matrix of partial derivatives [ D ⁡ g ( x ⋆ ) ] j , k =   ∂ g j   ∂ x k {\displaystyle {\Bigl [}\operatorname {D} g(x_{\star }){\Bigr ]}_{j,k}={\frac {\ \partial g_{j}\ }{\partial x_{k}}}} ({\displaystyle {\Bigl [}\operatorname {D} g(x_{\star }){\Bigr ]}_{j,k}={\frac {\ \partial g_{j}\ }{\partial x_{k}}}}), rank ⁡ ( D ⁡ g ( x ⋆ ) ) = c ≤ n {\displaystyle \operatorname {rank} (\operatorname {D} g(x_{\star }))=c\leq n} ({\displaystyle \operatorname {rank} (\operatorname {D} g(x_{\star }))=c\leq n}): Then there exists a unique Lagrange multiplier λ ⋆ ∈ R c {\displaystyle \lambda _{\star }\in \mathbb {R} ^{c}} ({\displaystyle \lambda _{\star }\in \mathbb {R} ^{c}}) such that D ⁡ f ( x ⋆ ) = λ ⋆ T D ⁡ g ( x ⋆ )   . {\displaystyle \operatorname {D} f(x_{\star })=\lambda _{\star }^{\mathsf {T}}\operatorname {D} g(x_{\star })~.} ({\displaystyle \operatorname {D} f(x_{\star })=\lambda _{\star }^{\mathsf {T}}\operatorname {D} g(x_{\star })~.}) (In this equation, λ ⋆ {\displaystyle \lambda _{\star }} ({\displaystyle \lambda _{\star }}) is a column vector, so its transpose λ ⋆ T {\displaystyle \lambda _{\star }^{\mathsf {T}}} ({\displaystyle \lambda _{\star }^{\mathsf {T}}}) is a row vector. Alternatively, we can redefine the Lagrange multiplier directly as a row vector and thus avoid the transposition.)

The Lagrange multiplier theorem states that at any local maximum (or minimum) of the function evaluated under the equality constraints, if constraint qualification applies (explained below), then the gradient of the function (at that point) can be expressed as a linear combination of the gradients of the constraints (at that point), with the Lagrange multipliers acting as coefficients. This is equivalent to saying that any direction perpendicular to all gradients of the constraints is also perpendicular to the gradient of the function. Or still, saying that the directional derivative of the function is 0 in every feasible direction.


## Single constraint

For the case of only one constraint and only two choice variables (as exemplified in Figure 1), consider the optimization problem maximize x , y f ( x , y ) subject to g ( x , y ) = 0. {\displaystyle {\begin{aligned}{\underset {x,y}{\text{maximize}}}\quad &f(x,y)\\{\text{subject to}}\quad &g(x,y)=0.\end{aligned}}} ({\displaystyle {\begin{aligned}{\underset {x,y}{\text{maximize}}}\quad &f(x,y)\\{\text{subject to}}\quad &g(x,y)=0.\end{aligned}}}) (Sometimes an additive constant is shown separately rather than being included in g {\displaystyle g} ({\displaystyle g}), in which case the constraint is written g ( x , y ) = c , {\displaystyle g(x,y)=c,} ({\displaystyle g(x,y)=c,}) as in Figure 1.) We assume that both f {\displaystyle f} ({\displaystyle f}) and g {\displaystyle g} ({\displaystyle g}) have continuous first partial derivatives. We introduce a new variable ( λ {\displaystyle \lambda } ({\displaystyle \lambda })) called a **Lagrange multiplier** (or **Lagrange undetermined multiplier**) and study the **Lagrange function** (or **Lagrangian** or **Lagrangian expression**) defined by L ( x , y , λ ) = f ( x , y ) + λ ⋅ g ( x , y ) , {\displaystyle {\mathcal {L}}(x,y,\lambda )=f(x,y)+\lambda \cdot g(x,y),} ({\displaystyle {\mathcal {L}}(x,y,\lambda )=f(x,y)+\lambda \cdot g(x,y),}) where the λ {\displaystyle \lambda } ({\displaystyle \lambda }) term may be either added or subtracted. If f ( x 0 , y 0 ) {\displaystyle f(x_{0},y_{0})} ({\displaystyle f(x_{0},y_{0})}) is a maximum of f ( x , y ) {\displaystyle f(x,y)} ({\displaystyle f(x,y)}) for the original constrained problem and ∇ g ( x 0 , y 0 ) ≠ 0 , {\displaystyle \nabla g(x_{0},y_{0})\neq 0,} ({\displaystyle \nabla g(x_{0},y_{0})\neq 0,}) then there exists λ 0 {\displaystyle \lambda _{0}} ({\displaystyle \lambda _{0}}) such that ( x 0 , y 0 , λ 0 {\displaystyle x_{0},y_{0},\lambda _{0}} ({\displaystyle x_{0},y_{0},\lambda _{0}})) is a *stationary point* for the Lagrange function (stationary points are those points where the first partial derivatives of L {\displaystyle {\mathcal {L}}} ({\displaystyle {\mathcal {L}}}) are zero). The assumption ∇ g ≠ 0 {\displaystyle \nabla g\neq 0} ({\displaystyle \nabla g\neq 0}) is called constraint qualification. However, not all stationary points yield a solution of the original problem, as the method of Lagrange multipliers yields only a necessary condition for optimality in constrained problems. Sufficient conditions for a minimum or maximum also exist, but if a particular candidate solution satisfies the sufficient conditions, it is only guaranteed that that solution is the best one *locally* – that is, it is better than any permissible nearby points. The *global* optimum can be found by comparing the values of the original objective function at the points satisfying the necessary and locally sufficient conditions.

The method of Lagrange multipliers relies on the intuition that at a maximum, *f*(*x*, *y*) cannot be increasing in the direction of any such neighboring point that also has *g* = 0. If it were, we could walk along *g* = 0 to get higher, meaning that the starting point wasn't actually the maximum. Viewed in this way, it is an exact analogue to testing if the derivative of an unconstrained function is 0, that is, we are verifying that the directional derivative is 0 in any relevant (viable) direction.

We can visualize contours of f given by *f*(*x*, *y*) = *d* for various values of d, and the contour of g given by *g*(*x*, *y*) = *c*.

Suppose we walk along the contour line with *g* = *c* . We are interested in finding points where f almost does not change as we walk, since these points might be maxima.

There are two ways this could happen:

1. We could touch a contour line of f, since by definition f does not change as we walk along its contour lines. This would mean that the tangents to the contour lines of f and g are parallel here.
2. We have reached a "level" part of f, meaning that f does not change in any direction.

To check the first possibility (we touch a contour line of f), notice that since the gradient of a function is perpendicular to the contour lines, the tangents to the contour lines of f and g are parallel if and only if the gradients of f and g are parallel. Thus we want points (*x*, *y*) where *g*(*x*, *y*) = *c* and ∇ x , y f = λ ∇ x , y g , {\displaystyle \nabla _{x,y}f=\lambda \,\nabla _{x,y}g,} ({\displaystyle \nabla _{x,y}f=\lambda \,\nabla _{x,y}g,}) for some λ {\displaystyle \lambda } ({\displaystyle \lambda }) where ∇ x , y f = ( ∂ f ∂ x , ∂ f ∂ y ) , ∇ x , y g = ( ∂ g ∂ x , ∂ g ∂ y ) {\displaystyle \nabla _{x,y}f=\left({\frac {\partial f}{\partial x}},{\frac {\partial f}{\partial y}}\right),\qquad \nabla _{x,y}g=\left({\frac {\partial g}{\partial x}},{\frac {\partial g}{\partial y}}\right)} ({\displaystyle \nabla _{x,y}f=\left({\frac {\partial f}{\partial x}},{\frac {\partial f}{\partial y}}\right),\qquad \nabla _{x,y}g=\left({\frac {\partial g}{\partial x}},{\frac {\partial g}{\partial y}}\right)}) are the respective gradients. The constant λ {\displaystyle \lambda } ({\displaystyle \lambda }) is required because although the two gradient vectors are parallel, the magnitudes of the gradient vectors are generally not equal. This constant is called the Lagrange multiplier. (In some conventions λ {\displaystyle \lambda } ({\displaystyle \lambda }) is preceded by a minus sign).

Notice that this method also solves the second possibility, that f is level: if f is level, then its gradient is zero, and setting λ = 0 {\displaystyle \lambda =0} ({\displaystyle \lambda =0}) is a solution regardless of ∇ x , y g {\displaystyle \nabla _{x,y}g} ({\displaystyle \nabla _{x,y}g}).

To incorporate these conditions into one equation, we introduce an auxiliary function L ( x , y , λ ) ≡ f ( x , y ) + λ ⋅ g ( x , y ) , {\displaystyle {\mathcal {L}}(x,y,\lambda )\equiv f(x,y)+\lambda \cdot g(x,y)\,,} ({\displaystyle {\mathcal {L}}(x,y,\lambda )\equiv f(x,y)+\lambda \cdot g(x,y)\,,}) and solve ∇ x , y , λ L ( x , y , λ ) = 0   . {\displaystyle \nabla _{x,y,\lambda }{\mathcal {L}}(x,y,\lambda )=0~.} ({\displaystyle \nabla _{x,y,\lambda }{\mathcal {L}}(x,y,\lambda )=0~.})Note that this amounts to solving three equations in three unknowns. This is the method of Lagrange multipliers.

Note that   ∇ λ L ( x , y , λ ) = 0   {\displaystyle \ \nabla _{\lambda }{\mathcal {L}}(x,y,\lambda )=0\ } ({\displaystyle \ \nabla _{\lambda }{\mathcal {L}}(x,y,\lambda )=0\ }) implies   g ( x , y ) = 0   , {\displaystyle \ g(x,y)=0\ ,} ({\displaystyle \ g(x,y)=0\ ,}) as the partial derivative of L {\displaystyle {\mathcal {L}}} ({\displaystyle {\mathcal {L}}}) with respect to λ {\displaystyle \lambda } ({\displaystyle \lambda }) is   g ( x , y )   . {\displaystyle \ g(x,y)~.} ({\displaystyle \ g(x,y)~.})

To summarize ∇ x , y , λ L ( x , y , λ ) = 0 ⟺ { ∇ x , y f ( x , y ) = − λ ∇ x , y g ( x , y ) g ( x , y ) = 0 {\displaystyle \nabla _{x,y,\lambda }{\mathcal {L}}(x,y,\lambda )=0\iff {\begin{cases}\nabla _{x,y}f(x,y)=-\lambda \,\nabla _{x,y}g(x,y)\\g(x,y)=0\end{cases}}} ({\displaystyle \nabla _{x,y,\lambda }{\mathcal {L}}(x,y,\lambda )=0\iff {\begin{cases}\nabla _{x,y}f(x,y)=-\lambda \,\nabla _{x,y}g(x,y)\\g(x,y)=0\end{cases}}})The method generalizes readily to functions on n {\displaystyle n} ({\displaystyle n}) variables ∇ x 1 , … , x n , λ L ( x 1 , … , x n , λ ) = 0 {\displaystyle \nabla _{x_{1},\dots ,x_{n},\lambda }{\mathcal {L}}(x_{1},\dots ,x_{n},\lambda )=0} ({\displaystyle \nabla _{x_{1},\dots ,x_{n},\lambda }{\mathcal {L}}(x_{1},\dots ,x_{n},\lambda )=0}) which amounts to solving *n* + 1 equations in *n* + 1 unknowns.

The constrained extrema of f are *critical points* of the Lagrangian L {\displaystyle {\mathcal {L}}} ({\displaystyle {\mathcal {L}}}), but they are not necessarily *local extrema* of L {\displaystyle {\mathcal {L}}} ({\displaystyle {\mathcal {L}}}) (see § Example 2 below).

One may reformulate the Lagrangian as a Hamiltonian, in which case the solutions are local minima for the Hamiltonian. This is done in optimal control theory, in the form of Pontryagin's maximum principle.

The fact that solutions of the method of Lagrange multipliers are not necessarily extrema of the Lagrangian, also poses difficulties for numerical optimization. This can be addressed by minimizing the *magnitude* of the gradient of the Lagrangian, as these minima are the same as the zeros of the magnitude, as illustrated in Example 5: Numerical optimization.


## Multiple constraints

The method of Lagrange multipliers can be extended to solve problems with multiple constraints using a similar argument. Consider a paraboloid subject to two line constraints that intersect at a single point. As the only feasible solution, this point is obviously a constrained extremum. However, the level set of f {\displaystyle f} ({\displaystyle f}) is clearly not parallel to either constraint at the intersection point (see Figure 3); instead, it is a linear combination of the two constraints' gradients. In the case of multiple constraints, that will be what we seek in general: The method of Lagrange seeks points not at which the gradient of f {\displaystyle f} ({\displaystyle f}) is a multiple of any single constraint's gradient necessarily, but in which it is a linear combination of all the constraints' gradients.

Concretely, suppose we have M {\displaystyle M} ({\displaystyle M}) constraints and are walking along the set of points satisfying g i ( x ) = 0 , i = 1 , … , M . {\displaystyle g_{i}(\mathbf {x} )=0,i=1,\dots ,M\,.} ({\displaystyle g_{i}(\mathbf {x} )=0,i=1,\dots ,M\,.}) Every point x {\displaystyle \mathbf {x} } ({\displaystyle \mathbf {x} }) on the contour of a given constraint function g i {\displaystyle g_{i}} ({\displaystyle g_{i}}) has a space of allowable directions: the space of vectors perpendicular to ∇ g i ( x ) . {\displaystyle \nabla g_{i}(\mathbf {x} )\,.} ({\displaystyle \nabla g_{i}(\mathbf {x} )\,.}) The set of directions that are allowed by all constraints is thus the space of directions perpendicular to all of the constraints' gradients. Denote this space of allowable moves by   A   {\displaystyle \ A\ } ({\displaystyle \ A\ }) and denote the span of the constraints' gradients by S . {\displaystyle S\,.} ({\displaystyle S\,.}) Then A = S ⊥ , {\displaystyle A=S^{\perp }\,,} ({\displaystyle A=S^{\perp }\,,}) the space of vectors perpendicular to every element of S . {\displaystyle S\,.} ({\displaystyle S\,.})

We are still interested in finding points where f {\displaystyle f} ({\displaystyle f}) does not change as we walk, since these points might be (constrained) extrema. We therefore seek x {\displaystyle \mathbf {x} } ({\displaystyle \mathbf {x} }) such that any allowable direction of movement away from x {\displaystyle \mathbf {x} } ({\displaystyle \mathbf {x} }) is perpendicular to ∇ f ( x ) {\displaystyle \nabla f(\mathbf {x} )} ({\displaystyle \nabla f(\mathbf {x} )}) (otherwise we could increase f {\displaystyle f} ({\displaystyle f}) by moving along that allowable direction). In other words, ∇ f ( x ) ∈ A ⊥ = S . {\displaystyle \nabla f(\mathbf {x} )\in A^{\perp }=S\,.} ({\displaystyle \nabla f(\mathbf {x} )\in A^{\perp }=S\,.}) Thus there are scalars λ 1 , λ 2 ,   … , λ M {\displaystyle \lambda _{1},\lambda _{2},\ \dots ,\lambda _{M}} ({\displaystyle \lambda _{1},\lambda _{2},\ \dots ,\lambda _{M}}) such that ∇ f ( x ) = ∑ k = 1 M λ k ∇ g k ( x ) ⟺ ∇ f ( x ) − ∑ k = 1 M λ k ∇ g k ( x ) = 0   . {\displaystyle \nabla f(\mathbf {x} )=\sum _{k=1}^{M}\lambda _{k}\,\nabla g_{k}(\mathbf {x} )\quad \iff \quad \nabla f(\mathbf {x} )-\sum _{k=1}^{M}{\lambda _{k}\nabla g_{k}(\mathbf {x} )}=0~.} ({\displaystyle \nabla f(\mathbf {x} )=\sum _{k=1}^{M}\lambda _{k}\,\nabla g_{k}(\mathbf {x} )\quad \iff \quad \nabla f(\mathbf {x} )-\sum _{k=1}^{M}{\lambda _{k}\nabla g_{k}(\mathbf {x} )}=0~.})

These scalars are the Lagrange multipliers. We now have M {\displaystyle M} ({\displaystyle M}) of them, one for every constraint.

As before, we introduce an auxiliary function L ( x 1 , … , x n , λ 1 , … , λ M ) = f ( x 1 , … , x n ) − ∑ k = 1 M λ k g k ( x 1 , … , x n )   {\displaystyle {\mathcal {L}}\left(x_{1},\ldots ,x_{n},\lambda _{1},\ldots ,\lambda _{M}\right)=f\left(x_{1},\ldots ,x_{n}\right)-\sum \limits _{k=1}^{M}{\lambda _{k}g_{k}\left(x_{1},\ldots ,x_{n}\right)}\ } ({\displaystyle {\mathcal {L}}\left(x_{1},\ldots ,x_{n},\lambda _{1},\ldots ,\lambda _{M}\right)=f\left(x_{1},\ldots ,x_{n}\right)-\sum \limits _{k=1}^{M}{\lambda _{k}g_{k}\left(x_{1},\ldots ,x_{n}\right)}\ }) and solve ∇ x 1 , … , x n , λ 1 , … , λ M L ( x 1 , … , x n , λ 1 , … , λ M ) = 0 ⟺ { ∇ f ( x ) − ∑ k = 1 M λ k ∇ g k ( x ) = 0 g 1 ( x ) = ⋯ = g M ( x ) = 0 {\displaystyle \nabla _{x_{1},\ldots ,x_{n},\lambda _{1},\ldots ,\lambda _{M}}{\mathcal {L}}(x_{1},\ldots ,x_{n},\lambda _{1},\ldots ,\lambda _{M})=0\iff {\begin{cases}\nabla f(\mathbf {x} )-\sum _{k=1}^{M}{\lambda _{k}\,\nabla g_{k}(\mathbf {x} )}=0\\g_{1}(\mathbf {x} )=\cdots =g_{M}(\mathbf {x} )=0\end{cases}}} ({\displaystyle \nabla _{x_{1},\ldots ,x_{n},\lambda _{1},\ldots ,\lambda _{M}}{\mathcal {L}}(x_{1},\ldots ,x_{n},\lambda _{1},\ldots ,\lambda _{M})=0\iff {\begin{cases}\nabla f(\mathbf {x} )-\sum _{k=1}^{M}{\lambda _{k}\,\nabla g_{k}(\mathbf {x} )}=0\\g_{1}(\mathbf {x} )=\cdots =g_{M}(\mathbf {x} )=0\end{cases}}}) which amounts to solving n + M {\displaystyle n+M} ({\displaystyle n+M}) equations in   n + M   {\displaystyle \ n+M\ } ({\displaystyle \ n+M\ }) unknowns.

The constraint qualification assumption when there are multiple constraints is that the constraint gradients at the relevant point are linearly independent.


## Modern formulation via differentiable manifolds

The problem of finding the local maxima and minima subject to constraints can be generalized to finding local maxima and minima on a differentiable manifold   M   . {\displaystyle \ M~.} ({\displaystyle \ M~.}) In what follows, it is not necessary that M {\displaystyle M} ({\displaystyle M}) be a Euclidean space, or even a Riemannian manifold. All appearances of the gradient   ∇   {\displaystyle \ \nabla \ } ({\displaystyle \ \nabla \ }) (which depends on a choice of Riemannian metric) can be replaced with the exterior derivative   d {\displaystyle \ \operatorname {d} } ({\displaystyle \ \operatorname {d} }).

### Single constraint

Let   M   {\displaystyle \ M\ } ({\displaystyle \ M\ }) be a smooth manifold of dimension   m   . {\displaystyle \ m~.} ({\displaystyle \ m~.}) Suppose that we wish to find the stationary points   x   {\displaystyle \ x\ } ({\displaystyle \ x\ }) of a smooth function   f : M → R   {\displaystyle \ f:M\to \mathbb {R} \ } ({\displaystyle \ f:M\to \mathbb {R} \ }) when restricted to the submanifold   N   {\displaystyle \ N\ } ({\displaystyle \ N\ }) defined by   g ( x ) = 0   , {\displaystyle \ g(x)=0\ ,} ({\displaystyle \ g(x)=0\ ,}) where   g : M → R   {\displaystyle \ g:M\to \mathbb {R} \ } ({\displaystyle \ g:M\to \mathbb {R} \ }) is a smooth function for which 0 is a regular value.

Let   d ⁡ f   {\displaystyle \ \operatorname {d} f\ } ({\displaystyle \ \operatorname {d} f\ }) and   d ⁡ g   {\displaystyle \ \operatorname {d} g\ } ({\displaystyle \ \operatorname {d} g\ }) be the exterior derivatives of   f   {\displaystyle \ f\ } ({\displaystyle \ f\ }) and   g   {\displaystyle \ g\ } ({\displaystyle \ g\ }). Stationarity for the restriction   f | N   {\displaystyle \ f|_{N}\ } ({\displaystyle \ f|_{N}\ }) at   x ∈ N   {\displaystyle \ x\in N\ } ({\displaystyle \ x\in N\ }) means   d ⁡ ( f | N ) x = 0   . {\displaystyle \ \operatorname {d} (f|_{N})_{x}=0~.} ({\displaystyle \ \operatorname {d} (f|_{N})_{x}=0~.}) Equivalently, the kernel   ker ⁡ ( d ⁡ f x )   {\displaystyle \ \ker(\operatorname {d} f_{x})\ } ({\displaystyle \ \ker(\operatorname {d} f_{x})\ }) contains   T x N = ker ⁡ ( d ⁡ g x )   . {\displaystyle \ T_{x}N=\ker(\operatorname {d} g_{x})~.} ({\displaystyle \ T_{x}N=\ker(\operatorname {d} g_{x})~.}) In other words,   d ⁡ f x   {\displaystyle \ \operatorname {d} f_{x}\ } ({\displaystyle \ \operatorname {d} f_{x}\ }) and   d ⁡ g x   {\displaystyle \ \operatorname {d} g_{x}\ } ({\displaystyle \ \operatorname {d} g_{x}\ }) are proportional 1-forms. For this it is necessary and sufficient that the following system of   1 2 m ( m − 1 )   {\displaystyle \ {\tfrac {1}{2}}m(m-1)\ } ({\displaystyle \ {\tfrac {1}{2}}m(m-1)\ }) equations holds: d ⁡ f x ∧ d ⁡ g x = 0 ∈ Λ 2 ( T x ∗ M ) {\displaystyle \operatorname {d} f_{x}\wedge \operatorname {d} g_{x}=0\in \Lambda ^{2}(T_{x}^{\ast }M)} ({\displaystyle \operatorname {d} f_{x}\wedge \operatorname {d} g_{x}=0\in \Lambda ^{2}(T_{x}^{\ast }M)}) where   ∧   {\displaystyle \ \wedge \ } ({\displaystyle \ \wedge \ }) denotes the exterior product. The stationary points   x   {\displaystyle \ x\ } ({\displaystyle \ x\ }) are the solutions of the above system of equations plus the constraint   g ( x ) = 0   . {\displaystyle \ g(x)=0~.} ({\displaystyle \ g(x)=0~.}) Note that the   1 2 m ( m − 1 )   {\displaystyle \ {\tfrac {1}{2}}m(m-1)\ } ({\displaystyle \ {\tfrac {1}{2}}m(m-1)\ }) equations are not independent, since the left-hand side of the equation belongs to the subvariety of   Λ 2 ( T x ∗ M )   {\displaystyle \ \Lambda ^{2}(T_{x}^{\ast }M)\ } ({\displaystyle \ \Lambda ^{2}(T_{x}^{\ast }M)\ }) consisting of decomposable elements.

In this formulation, it is not necessary to explicitly find the Lagrange multiplier, a number   λ   {\displaystyle \ \lambda \ } ({\displaystyle \ \lambda \ }) such that   d ⁡ f x = λ ⋅ d ⁡ g x   . {\displaystyle \ \operatorname {d} f_{x}=\lambda \cdot \operatorname {d} g_{x}~.} ({\displaystyle \ \operatorname {d} f_{x}=\lambda \cdot \operatorname {d} g_{x}~.})

### Multiple constraints

Let   M   {\displaystyle \ M\ } ({\displaystyle \ M\ }) and   f   {\displaystyle \ f\ } ({\displaystyle \ f\ }) be as in the above section regarding the case of a single constraint. Rather than the function g {\displaystyle g} ({\displaystyle g}) described there, now consider a smooth function   G : M → R p ( p > 1 )   , {\displaystyle \ G:M\to \mathbb {R} ^{p}(p>1)\ ,} ({\displaystyle \ G:M\to \mathbb {R} ^{p}(p>1)\ ,}) with component functions   g i : M → R   , {\displaystyle \ g_{i}:M\to \mathbb {R} \ ,} ({\displaystyle \ g_{i}:M\to \mathbb {R} \ ,}) for which 0 ∈ R p {\displaystyle 0\in \mathbb {R} ^{p}} ({\displaystyle 0\in \mathbb {R} ^{p}}) is a regular value. Let N {\displaystyle N} ({\displaystyle N}) be the submanifold of   M   {\displaystyle \ M\ } ({\displaystyle \ M\ }) defined by   G ( x ) = 0   . {\displaystyle \ G(x)=0~.} ({\displaystyle \ G(x)=0~.})

x   {\displaystyle \ x\ } ({\displaystyle \ x\ }) is a stationary point of f | N {\displaystyle f|_{N}} ({\displaystyle f|_{N}}) if and only if   ker ⁡ ( d ⁡ f x )   {\displaystyle \ \ker(\operatorname {d} f_{x})\ } ({\displaystyle \ \ker(\operatorname {d} f_{x})\ }) contains   ker ⁡ ( d ⁡ G x )   . {\displaystyle \ \ker(\operatorname {d} G_{x})~.} ({\displaystyle \ \ker(\operatorname {d} G_{x})~.}) For convenience let   L x = d ⁡ f x   {\displaystyle \ L_{x}=\operatorname {d} f_{x}\ } ({\displaystyle \ L_{x}=\operatorname {d} f_{x}\ }) and   K x = d ⁡ G x   , {\displaystyle \ K_{x}=\operatorname {d} G_{x}\ ,} ({\displaystyle \ K_{x}=\operatorname {d} G_{x}\ ,}) where   d ⁡ G {\displaystyle \ \operatorname {d} G} ({\displaystyle \ \operatorname {d} G}) denotes the tangent map or Jacobian   T M → T R p   {\displaystyle \ TM\to T\mathbb {R} ^{p}~} ({\displaystyle \ TM\to T\mathbb {R} ^{p}~}) (   T x R p {\displaystyle \ T_{x}\mathbb {R} ^{p}} ({\displaystyle \ T_{x}\mathbb {R} ^{p}}) can be canonically identified with   R p {\displaystyle \ \mathbb {R} ^{p}} ({\displaystyle \ \mathbb {R} ^{p}})). The subspace ker ⁡ ( K x ) {\displaystyle \ker(K_{x})} ({\displaystyle \ker(K_{x})}) has dimension smaller than that of ker ⁡ ( L x ) {\displaystyle \ker(L_{x})} ({\displaystyle \ker(L_{x})}), namely   dim ⁡ ( ker ⁡ ( L x ) ) = n − 1   {\displaystyle \ \dim(\ker(L_{x}))=n-1\ } ({\displaystyle \ \dim(\ker(L_{x}))=n-1\ }) and   dim ⁡ ( ker ⁡ ( K x ) ) = n − p   . {\displaystyle \ \dim(\ker(K_{x}))=n-p~.} ({\displaystyle \ \dim(\ker(K_{x}))=n-p~.}) ker ⁡ ( K x ) {\displaystyle \ker(K_{x})} ({\displaystyle \ker(K_{x})}) belongs to   ker ⁡ ( L x )   {\displaystyle \ \ker(L_{x})\ } ({\displaystyle \ \ker(L_{x})\ }) if and only if L x ∈ T x ∗ M {\displaystyle L_{x}\in T_{x}^{\ast }M} ({\displaystyle L_{x}\in T_{x}^{\ast }M}) belongs to the image of   K x ∗ : R p ∗ → T x ∗ M   . {\displaystyle \ K_{x}^{\ast }:\mathbb {R} ^{p\ast }\to T_{x}^{\ast }M~.} ({\displaystyle \ K_{x}^{\ast }:\mathbb {R} ^{p\ast }\to T_{x}^{\ast }M~.}) Computationally speaking, the condition is that L x {\displaystyle L_{x}} ({\displaystyle L_{x}}) belongs to the row space of the matrix of   K x   , {\displaystyle \ K_{x}\ ,} ({\displaystyle \ K_{x}\ ,}) or equivalently the column space of the matrix of K x ∗ {\displaystyle K_{x}^{\ast }} ({\displaystyle K_{x}^{\ast }}) (the transpose). If   ω x ∈ Λ p ( T x ∗ M )   {\displaystyle \ \omega _{x}\in \Lambda ^{p}(T_{x}^{\ast }M)\ } ({\displaystyle \ \omega _{x}\in \Lambda ^{p}(T_{x}^{\ast }M)\ }) denotes the exterior product of the columns of the matrix of   K x ∗   , {\displaystyle \ K_{x}^{\ast }\ ,} ({\displaystyle \ K_{x}^{\ast }\ ,}) the stationary condition for   f | N   {\displaystyle \ f|_{N}\ } ({\displaystyle \ f|_{N}\ }) at   x   {\displaystyle \ x\ } ({\displaystyle \ x\ }) becomes L x ∧ ω x = 0 ∈ Λ p + 1 ( T x ∗ M ) {\displaystyle L_{x}\wedge \omega _{x}=0\in \Lambda ^{p+1}\left(T_{x}^{\ast }M\right)} ({\displaystyle L_{x}\wedge \omega _{x}=0\in \Lambda ^{p+1}\left(T_{x}^{\ast }M\right)}) Once again, in this formulation it is not necessary to explicitly find the Lagrange multipliers, the numbers   λ 1 , … , λ p   {\displaystyle \ \lambda _{1},\ldots ,\lambda _{p}\ } ({\displaystyle \ \lambda _{1},\ldots ,\lambda _{p}\ }) such that   d ⁡ f x = ∑ i = 1 p λ i d ⁡ ( g i ) x   . {\displaystyle \ \operatorname {d} f_{x}=\sum _{i=1}^{p}\lambda _{i}\operatorname {d} (g_{i})_{x}~.} ({\displaystyle \ \operatorname {d} f_{x}=\sum _{i=1}^{p}\lambda _{i}\operatorname {d} (g_{i})_{x}~.})


## Interpretation of the Lagrange multipliers

In this section, we modify the constraint equations from the form g i ( x ) = 0 {\displaystyle g_{i}({\bf {x}})=0} ({\displaystyle g_{i}({\bf {x}})=0}) to the form   g i ( x ) = c i   , {\displaystyle \ g_{i}({\bf {x}})=c_{i}\ ,} ({\displaystyle \ g_{i}({\bf {x}})=c_{i}\ ,}) where the   c i   {\displaystyle \ c_{i}\ } ({\displaystyle \ c_{i}\ }) are m real constants that are considered to be additional arguments of the Lagrangian expression L {\displaystyle {\mathcal {L}}} ({\displaystyle {\mathcal {L}}}).

Often the Lagrange multipliers have an interpretation as some quantity of interest. For example, by parametrising the constraint's contour line, that is, if the Lagrangian expression is L ( x 1 , x 2 , … ; λ 1 , λ 2 , … ; c 1 , c 2 , … ) = f ( x 1 , x 2 , … ) + λ 1 ( c 1 − g 1 ( x 1 , x 2 , … ) ) + λ 2 ( c 2 − g 2 ( x 1 , x 2 , … ) ) + ⋯ {\displaystyle {\begin{aligned}&{\mathcal {L}}(x_{1},x_{2},\ldots ;\lambda _{1},\lambda _{2},\ldots ;c_{1},c_{2},\ldots )\\[4pt]={}&f(x_{1},x_{2},\ldots )+\lambda _{1}(c_{1}-g_{1}(x_{1},x_{2},\ldots ))+\lambda _{2}(c_{2}-g_{2}(x_{1},x_{2},\dots ))+\cdots \end{aligned}}} ({\displaystyle {\begin{aligned}&{\mathcal {L}}(x_{1},x_{2},\ldots ;\lambda _{1},\lambda _{2},\ldots ;c_{1},c_{2},\ldots )\\[4pt]={}&f(x_{1},x_{2},\ldots )+\lambda _{1}(c_{1}-g_{1}(x_{1},x_{2},\ldots ))+\lambda _{2}(c_{2}-g_{2}(x_{1},x_{2},\dots ))+\cdots \end{aligned}}}) then   ∂ L ∂ c k = λ k   . {\displaystyle \ {\frac {\partial {\mathcal {L}}}{\partial c_{k}}}=\lambda _{k}~.} ({\displaystyle \ {\frac {\partial {\mathcal {L}}}{\partial c_{k}}}=\lambda _{k}~.})

So, *λk* is the rate of change of the quantity being optimized as a function of the constraint parameter. As examples, in Lagrangian mechanics the equations of motion are derived by finding stationary points of the action, the time integral of the difference between kinetic and potential energy. Thus, the force on a particle due to a scalar potential, *F* = −∇*V*, can be interpreted as a Lagrange multiplier determining the change in action (transfer of potential to kinetic energy) following a variation in the particle's constrained trajectory. In control theory this is formulated instead as costate equations.

Moreover, by the envelope theorem the optimal value of a Lagrange multiplier has an interpretation as the marginal effect of the corresponding constraint constant upon the optimal attainable value of the original objective function: If we denote values at the optimum with a star ( ⋆ {\displaystyle \star } ({\displaystyle \star })), then it can be shown that   d ⁡ f (   x 1 ⋆ ( c 1 , c 2 , … ) ,   x 2 ⋆ ( c 1 , c 2 , … ) ,   …   )   d ⁡ c k = λ ⋆ k   . {\displaystyle {\frac {\ \operatorname {d} f\left(\ x_{1\star }(c_{1},c_{2},\dots ),\ x_{2\star }(c_{1},c_{2},\dots ),\ \dots \ \right)\ }{\operatorname {d} c_{k}}}=\lambda _{\star k}~.} ({\displaystyle {\frac {\ \operatorname {d} f\left(\ x_{1\star }(c_{1},c_{2},\dots ),\ x_{2\star }(c_{1},c_{2},\dots ),\ \dots \ \right)\ }{\operatorname {d} c_{k}}}=\lambda _{\star k}~.})

For example, in economics the optimal profit to a player is calculated subject to a constrained space of actions, where a Lagrange multiplier is the change in the optimal value of the objective function (profit) due to the relaxation of a given constraint (e.g. through a change in income); in such a context   λ ⋆ k   {\displaystyle \ \lambda _{\star k}\ } ({\displaystyle \ \lambda _{\star k}\ }) is the marginal cost of the constraint, and is referred to as the shadow price.


## Sufficient conditions

Sufficient conditions for a constrained local maximum or minimum can be stated in terms of a sequence of principal minors (determinants of upper-left-justified sub-matrices) of the bordered Hessian matrix of second derivatives of the Lagrangian expression.
