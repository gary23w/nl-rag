---
title: "Newton's method (part 2/2)"
source: https://en.wikipedia.org/wiki/Newton's_method
domain: numerical-methods
license: CC-BY-SA-4.0
tags: numerical analysis, numerical method, root finding, polynomial interpolation, numerical integration
fetched: 2026-07-02
part: 2/2
---

## Multidimensional formulations

### Systems of equations

#### k variables, k functions

One may also use Newton's method to solve systems of k equations, which amounts to finding the (simultaneous) zeroes of k continuously differentiable functions f : R k → R . {\displaystyle f:\mathbb {R} ^{k}\to \mathbb {R} .} ({\displaystyle f:\mathbb {R} ^{k}\to \mathbb {R} .}) This is equivalent to finding the zeroes of a single vector-valued function F : R k → R k . {\displaystyle F:\mathbb {R} ^{k}\to \mathbb {R} ^{k}.} ({\displaystyle F:\mathbb {R} ^{k}\to \mathbb {R} ^{k}.}) In the formulation given above, the scalars xn are replaced by vectors **x***n* and instead of dividing the function *f*(*x**n*) by its derivative *f′*(*x**n*) one instead has to left multiply the function *F*(**x***n*) by the inverse of its *k* × *k* Jacobian matrix *J**F*(**x***n*). This results in the expression

x n + 1 = x n − J F ( x n ) − 1 F ( x n ) . {\displaystyle \mathbf {x} _{n+1}=\mathbf {x} _{n}-J_{F}(\mathbf {x} _{n})^{-1}F(\mathbf {x} _{n}).} ({\displaystyle \mathbf {x} _{n+1}=\mathbf {x} _{n}-J_{F}(\mathbf {x} _{n})^{-1}F(\mathbf {x} _{n}).})

or, by solving the system of linear equations

J F ( x n ) ( x n + 1 − x n ) = − F ( x n ) {\displaystyle J_{F}(\mathbf {x} _{n})(\mathbf {x} _{n+1}-\mathbf {x} _{n})=-F(\mathbf {x} _{n})} ({\displaystyle J_{F}(\mathbf {x} _{n})(\mathbf {x} _{n+1}-\mathbf {x} _{n})=-F(\mathbf {x} _{n})})

for the unknown **x***n* + 1 − **x***n*.

#### k variables, m equations, with *m* > *k*

The k-dimensional variant of Newton's method can be used to solve systems of greater than k (nonlinear) equations as well if the algorithm uses the generalized inverse of the non-square Jacobian matrix *J*+ = (*J*T*J*)−1*J*T instead of the inverse of J. If the nonlinear system has no solution, the method attempts to find a solution in the non-linear least squares sense. See Gauss–Newton algorithm for more information.

#### Example

A milk carton with a capacity of 2 pints is to be constructed from a sheet of waxed carboard with a 5mm overlap. The requirement is that the minimum surface area is used for the carton.

Suppose the width, breadth and height of the carton are denoted by w {\displaystyle w} ({\displaystyle w}), b {\displaystyle b} ({\displaystyle b}) and h {\displaystyle h} ({\displaystyle h}) respectively, in millimetres. The total surface area, A {\displaystyle A} ({\displaystyle A}), is given by

A = ( 2 b + 2 w + 5 ) ( h + b + 10 ) . {\displaystyle A=(2b+2w+5)(h+b+10).} ({\displaystyle A=(2b+2w+5)(h+b+10).})

Since 2 pints is approximately 1.136 litres, and 1 litre is 1000000 m m 3 {\displaystyle 1000000mm^{3}} ({\displaystyle 1000000mm^{3}}), it also follows that

h b w = 1136000. {\displaystyle hbw=1136000.} ({\displaystyle hbw=1136000.})

Solving for w {\displaystyle w} ({\displaystyle w}) gives

w = 1136000 h b . {\displaystyle w={\frac {1136000}{hb}}.} ({\displaystyle w={\frac {1136000}{hb}}.})

Letting x = [ b , h ] ∈ R 2 {\displaystyle \mathbf {x} =\left[b,h\right]\in {\mathbb {R} }^{2}} ({\displaystyle \mathbf {x} =\left[b,h\right]\in {\mathbb {R} }^{2}}) be the vector of two unknowns, b {\displaystyle b} ({\displaystyle b}) and h {\displaystyle h} ({\displaystyle h}), the surface area can then be expressed as

A ( x ) = ( h + b + 10 ) ( 2272000 h b + 2 b + 5 ) . {\displaystyle A(\mathbf {x} )=(h+b+10)\left({\frac {2272000}{hb}}+2b+5\right).} ({\displaystyle A(\mathbf {x} )=(h+b+10)\left({\frac {2272000}{hb}}+2b+5\right).})

Minimization of this function entails equating its partial derivatives to zero, which gives

∂ A ∂ b = 2272000 h b + 2 b + 5 + ( h + b + 10 ) ( − 2272000 h b 2 + 2 ) = 0 {\displaystyle {\frac {\partial A}{\partial b}}={\frac {2272000}{hb}}+2b+5+(h+b+10)\left({\frac {-2272000}{hb^{2}}}+2\right)=0} ({\displaystyle {\frac {\partial A}{\partial b}}={\frac {2272000}{hb}}+2b+5+(h+b+10)\left({\frac {-2272000}{hb^{2}}}+2\right)=0})

and

∂ A ∂ h = 2272000 h b + 2 b + 5 − ( h + b + 10 ) ( 2272000 h 2 b ) = 0. {\displaystyle {\frac {\partial A}{\partial h}}={\frac {2272000}{hb}}+2b+5-(h+b+10)\left({\frac {2272000}{h^{2}b}}\right)=0.} ({\displaystyle {\frac {\partial A}{\partial h}}={\frac {2272000}{hb}}+2b+5-(h+b+10)\left({\frac {2272000}{h^{2}b}}\right)=0.})

To simplify notation, let

f 1 ( x ) = ∂ A ∂ b {\displaystyle f_{1}(\mathbf {x} )={\frac {\partial A}{\partial b}}} ({\displaystyle f_{1}(\mathbf {x} )={\frac {\partial A}{\partial b}}})

and

f 2 ( x ) = ∂ A ∂ h . {\displaystyle f_{2}(\mathbf {x} )={\frac {\partial A}{\partial h}}.} ({\displaystyle f_{2}(\mathbf {x} )={\frac {\partial A}{\partial h}}.})

The function vector F ( x ) {\displaystyle \mathbf {F} (\mathbf {x} )} ({\displaystyle \mathbf {F} (\mathbf {x} )}) is therefore

F ( x ) = [   f 1 ( x )   f 2 ( x ) ]   =   [   2272000 h b + 2 b + 5 + ( h + b + 10 ) ( − 2272000 h b 2 + 2 )   2272000 h b + 2 b + 5 − ( h + b + 10 ) ( 2272000 h 2 b ) ] {\displaystyle \mathbf {F} (\mathbf {x} )={\begin{bmatrix}{\begin{aligned}~&f_{1}(\mathbf {x} )\\~&f_{2}(\mathbf {x} )\end{aligned}}\end{bmatrix}}~=~{\begin{bmatrix}{\begin{aligned}~&{\frac {2272000}{hb}}+2b+5+(h+b+10)\left({\frac {-2272000}{hb^{2}}}+2\right)\\~&{\frac {2272000}{hb}}+2b+5-(h+b+10)\left({\frac {2272000}{h^{2}b}}\right)\end{aligned}}\end{bmatrix}}} ({\displaystyle \mathbf {F} (\mathbf {x} )={\begin{bmatrix}{\begin{aligned}~&f_{1}(\mathbf {x} )\\~&f_{2}(\mathbf {x} )\end{aligned}}\end{bmatrix}}~=~{\begin{bmatrix}{\begin{aligned}~&{\frac {2272000}{hb}}+2b+5+(h+b+10)\left({\frac {-2272000}{hb^{2}}}+2\right)\\~&{\frac {2272000}{hb}}+2b+5-(h+b+10)\left({\frac {2272000}{h^{2}b}}\right)\end{aligned}}\end{bmatrix}}})

and Jacobian matrix J ( x ) {\displaystyle \mathbf {J} (\mathbf {x} )} ({\displaystyle \mathbf {J} (\mathbf {x} )}) is

J ( x ) = [     ∂ f 1   ∂ b       ∂ f 1   ∂ h       ∂ f 2   ∂ b       ∂ f 2   ∂ h   ]   =   [   4544000 b 3 + 45440000 h b 3 + 4   22720000 h 2 b 2 + 2   22720000 h 2 b 2 + 2   4544000 h 3 + 45440000 b h 3 ] . {\displaystyle {\begin{aligned}\mathbf {J} (\mathbf {x} )={\begin{bmatrix}~{\frac {\ \partial {f_{1}}\ }{\partial {b}}}\ &~{\frac {\ \partial {f_{1}}\ }{\partial {h}}}~\\~{\frac {\ \partial {f_{2}}\ }{\partial {b}}}\ &~{\frac {\ \partial {f_{2}}\ }{\partial {h}}}~\end{bmatrix}}~=~{\begin{bmatrix}{\begin{aligned}~&{\frac {4544000}{b^{3}}}+{\frac {45440000}{hb^{3}}}+4\ &&{\frac {22720000}{h^{2}b^{2}}}+2\\~&{\frac {22720000}{h^{2}b^{2}}}+2\ &&{\frac {4544000}{h^{3}}}+{\frac {45440000}{bh^{3}}}\end{aligned}}\end{bmatrix}}.\end{aligned}}} ({\displaystyle {\begin{aligned}\mathbf {J} (\mathbf {x} )={\begin{bmatrix}~{\frac {\ \partial {f_{1}}\ }{\partial {b}}}\ &~{\frac {\ \partial {f_{1}}\ }{\partial {h}}}~\\~{\frac {\ \partial {f_{2}}\ }{\partial {b}}}\ &~{\frac {\ \partial {f_{2}}\ }{\partial {h}}}~\end{bmatrix}}~=~{\begin{bmatrix}{\begin{aligned}~&{\frac {4544000}{b^{3}}}+{\frac {45440000}{hb^{3}}}+4\ &&{\frac {22720000}{h^{2}b^{2}}}+2\\~&{\frac {22720000}{h^{2}b^{2}}}+2\ &&{\frac {4544000}{h^{3}}}+{\frac {45440000}{bh^{3}}}\end{aligned}}\end{bmatrix}}.\end{aligned}}})

Applying Newton's method with initial guess x 0 = [ 100 , 100 ] {\displaystyle \mathbf {x} _{0}=\left[100,100\right]} ({\displaystyle \mathbf {x} _{0}=\left[100,100\right]}) and with a stopping criterion of ‖   x i − x i − 1 ‖ 2 < 10 − 6 {\displaystyle \|\ \mathbf {x} _{i}-\mathbf {x} _{i-1}\|_{2}<10^{-6}} ({\displaystyle \|\ \mathbf {x} _{i}-\mathbf {x} _{i-1}\|_{2}<10^{-6}}) gives the following iterations:

| Iteration | Solution Vector | Function Vector | ‖   x i − x i − 1 ‖ 2 {\displaystyle \\|\ \mathbf {x} _{i}-\mathbf {x} _{i-1}\\|_{2}} ({\displaystyle \\|\ \mathbf {x} _{i}-\mathbf {x} _{i-1}\\|_{2}}) |
|---|---|---|---|
| 0 | x 0 = [ 100 , 100 ] {\displaystyle \mathbf {x} _{0}=\left[100,100\right]} ({\displaystyle \mathbf {x} _{0}=\left[100,100\right]}) | F ( x 0 )   =   [   375.08   − 44.92 ] {\displaystyle \mathbf {F} (\mathbf {x} _{0})~=~{\begin{bmatrix}{\begin{aligned}~&\quad 375.08\\~&-44.92\end{aligned}}\end{bmatrix}}} ({\displaystyle \mathbf {F} (\mathbf {x} _{0})~=~{\begin{bmatrix}{\begin{aligned}~&\quad 375.08\\~&-44.92\end{aligned}}\end{bmatrix}}}) | - |
| 1 | x 1 = [ 47.99347513 , 132.16007766 ] {\displaystyle \mathbf {x} _{1}=\left[47.99347513,132.16007766\right]} ({\displaystyle \mathbf {x} _{1}=\left[47.99347513,132.16007766\right]}) | F ( x 1 )   =   [   − 579.72039   − 56.19573 ] {\displaystyle \mathbf {F} (\mathbf {x} _{1})~=~{\begin{bmatrix}{\begin{aligned}~&-579.72039\\~&-56.19573\end{aligned}}\end{bmatrix}}} ({\displaystyle \mathbf {F} (\mathbf {x} _{1})~=~{\begin{bmatrix}{\begin{aligned}~&-579.72039\\~&-56.19573\end{aligned}}\end{bmatrix}}}) | 16.07552 {\displaystyle 16.07552} ({\displaystyle 16.07552}) |
| 2 | x 2 = [ 60.16520202 , 142.66110819 ] {\displaystyle \mathbf {x} _{2}=\left[60.16520202,142.66110819\right]} ({\displaystyle \mathbf {x} _{2}=\left[60.16520202,142.66110819\right]}) | F ( x 2 )   =   [   − 120.66290   − 4.85837 ] {\displaystyle \mathbf {F} (\mathbf {x} _{2})~=~{\begin{bmatrix}{\begin{aligned}~&-120.66290\\~&-4.85837\end{aligned}}\end{bmatrix}}} ({\displaystyle \mathbf {F} (\mathbf {x} _{2})~=~{\begin{bmatrix}{\begin{aligned}~&-120.66290\\~&-4.85837\end{aligned}}\end{bmatrix}}}) | 6.48393 {\displaystyle 6.48393} ({\displaystyle 6.48393}) |
| 3 | x 3 = [ 65.34915899 , 138.76649357 ] {\displaystyle \mathbf {x} _{3}=\left[65.34915899,138.76649357\right]} ({\displaystyle \mathbf {x} _{3}=\left[65.34915899,138.76649357\right]}) | F ( x 3 )   =   [   − 6.43007   − 0.34509 ] {\displaystyle \mathbf {F} (\mathbf {x} _{3})~=~{\begin{bmatrix}{\begin{aligned}~&-6.43007\\~&-0.34509\end{aligned}}\end{bmatrix}}} ({\displaystyle \mathbf {F} (\mathbf {x} _{3})~=~{\begin{bmatrix}{\begin{aligned}~&-6.43007\\~&-0.34509\end{aligned}}\end{bmatrix}}}) | 4.03613 × 10 − 1 {\displaystyle 4.03613\times 10^{-1}} ({\displaystyle 4.03613\times 10^{-1}}) |
| 4 | x 4 = [ 65.68871009 , 138.5482994 ] {\displaystyle \mathbf {x} _{4}=\left[65.68871009,138.5482994\right]} ({\displaystyle \mathbf {x} _{4}=\left[65.68871009,138.5482994\right]}) | F ( x 4 )   =   [   3.13226 × 10 − 1   − 1.20192 × 10 − 3 ] {\displaystyle \mathbf {F} (\mathbf {x} _{4})~=~{\begin{bmatrix}{\begin{aligned}~&\quad 3.13226\times 10^{-1}\\~&-1.20192\times 10^{-3}\end{aligned}}\end{bmatrix}}} ({\displaystyle \mathbf {F} (\mathbf {x} _{4})~=~{\begin{bmatrix}{\begin{aligned}~&\quad 3.13226\times 10^{-1}\\~&-1.20192\times 10^{-3}\end{aligned}}\end{bmatrix}}}) | 2.79029 × 10 − 2 {\displaystyle 2.79029\times 10^{-2}} ({\displaystyle 2.79029\times 10^{-2}}) |
| 5 | x 5 = [ 65.67075217 , 138.56965564 ] {\displaystyle \mathbf {x} _{5}=\left[65.67075217,138.56965564\right]} ({\displaystyle \mathbf {x} _{5}=\left[65.67075217,138.56965564\right]}) | F ( x 5 )   =   [   − 1.88252 × 10 − 2   − 9.54744 × 10 − 6 ] {\displaystyle \mathbf {F} (\mathbf {x} _{5})~=~{\begin{bmatrix}{\begin{aligned}~&-1.88252\times 10^{-2}\\~&-9.54744\times 10^{-6}\end{aligned}}\end{bmatrix}}} ({\displaystyle \mathbf {F} (\mathbf {x} _{5})~=~{\begin{bmatrix}{\begin{aligned}~&-1.88252\times 10^{-2}\\~&-9.54744\times 10^{-6}\end{aligned}}\end{bmatrix}}}) | 1.63648 × 10 − 3 {\displaystyle 1.63648\times 10^{-3}} ({\displaystyle 1.63648\times 10^{-3}}) |
| 6 | x 6 = [ 65.67182534 , 138.56842016 ] {\displaystyle \mathbf {x} _{6}=\left[65.67182534,138.56842016\right]} ({\displaystyle \mathbf {x} _{6}=\left[65.67182534,138.56842016\right]}) | F ( x 6 )   =   [   1.11786 × 10 − 3   − 3.20764 × 10 − 8 ] {\displaystyle \mathbf {F} (\mathbf {x} _{6})~=~{\begin{bmatrix}{\begin{aligned}~&\quad 1.11786\times 10^{-3}\\~&-3.20764\times 10^{-8}\end{aligned}}\end{bmatrix}}} ({\displaystyle \mathbf {F} (\mathbf {x} _{6})~=~{\begin{bmatrix}{\begin{aligned}~&\quad 1.11786\times 10^{-3}\\~&-3.20764\times 10^{-8}\end{aligned}}\end{bmatrix}}}) | 9.74697 × 10 − 5 {\displaystyle 9.74697\times 10^{-5}} ({\displaystyle 9.74697\times 10^{-5}}) |
| 7 | x 7 = [ 65.67176157 , 138.56849388 ] {\displaystyle \mathbf {x} _{7}=\left[65.67176157,138.56849388\right]} ({\displaystyle \mathbf {x} _{7}=\left[65.67176157,138.56849388\right]}) | F ( x 7 )   =   [   − 6.64497 × 10 − 5   − 1.14255 × 10 − 10 ] {\displaystyle \mathbf {F} (\mathbf {x} _{7})~=~{\begin{bmatrix}{\begin{aligned}~&-6.64497\times 10^{-5}\\~&-1.14255\times 10^{-10}\end{aligned}}\end{bmatrix}}} ({\displaystyle \mathbf {F} (\mathbf {x} _{7})~=~{\begin{bmatrix}{\begin{aligned}~&-6.64497\times 10^{-5}\\~&-1.14255\times 10^{-10}\end{aligned}}\end{bmatrix}}}) | 5.79292 × 10 − 6 {\displaystyle 5.79292\times 10^{-6}} ({\displaystyle 5.79292\times 10^{-6}}) |
| 8 | x 8 = [ 65.67176536 , 138.5684895 ] {\displaystyle \mathbf {x} _{8}=\left[65.67176536,138.5684895\right]} ({\displaystyle \mathbf {x} _{8}=\left[65.67176536,138.5684895\right]}) | F ( x 8 )   =   [   3.94975 × 10 − 6   − 3.41060 × 10 − 13 ] {\displaystyle \mathbf {F} (\mathbf {x} _{8})~=~{\begin{bmatrix}{\begin{aligned}~&\quad 3.94975\times 10^{-6}\\~&-3.41060\times 10^{-13}\end{aligned}}\end{bmatrix}}} ({\displaystyle \mathbf {F} (\mathbf {x} _{8})~=~{\begin{bmatrix}{\begin{aligned}~&\quad 3.94975\times 10^{-6}\\~&-3.41060\times 10^{-13}\end{aligned}}\end{bmatrix}}}) | 3.44333 × 10 − 7 {\displaystyle 3.44333\times 10^{-7}} ({\displaystyle 3.44333\times 10^{-7}}) |

To show that x 8 = [ 65.67176536 , 138.5684895 ] {\displaystyle \mathbf {x} _{8}=\left[65.67176536,138.5684895\right]} ({\displaystyle \mathbf {x} _{8}=\left[65.67176536,138.5684895\right]}) minimises A ( x ) {\displaystyle A(\mathbf {x} )} ({\displaystyle A(\mathbf {x} )}), it suffices to show that its Hessian matrix is positive definite. In this case, the Hessian matrix is simply

J ( x 8 ) ≈ [   20.15939696   2.27436075     2.27436075   1.9678865   ] . {\displaystyle \mathbf {J} (\mathbf {x} _{8})\approx {\begin{bmatrix}~20.15939696&~2.27436075~\\~2.27436075&~1.9678865~\end{bmatrix}}.} ({\displaystyle \mathbf {J} (\mathbf {x} _{8})\approx {\begin{bmatrix}~20.15939696&~2.27436075~\\~2.27436075&~1.9678865~\end{bmatrix}}.})

The characteristic polynomial of this matrix is

λ 2 − 22.12728346 λ + 34.49868830 = 0 {\displaystyle \lambda ^{2}-22.12728346\lambda +34.49868830=0} ({\displaystyle \lambda ^{2}-22.12728346\lambda +34.49868830=0}).

Applying the quadratic formula gives the two eigenvalues as

λ 1 = 22.12728346 + 351.62192 2 ≈ 20.43943 {\displaystyle \lambda _{1}={\frac {22.12728346+{\sqrt {351.62192}}}{2}}\approx 20.43943} ({\displaystyle \lambda _{1}={\frac {22.12728346+{\sqrt {351.62192}}}{2}}\approx 20.43943})

and

λ 2 = 22.12728346 − 351.62192 2 ≈ 1.68784. {\displaystyle \lambda _{2}={\frac {22.12728346-{\sqrt {351.62192}}}{2}}\approx 1.68784.} ({\displaystyle \lambda _{2}={\frac {22.12728346-{\sqrt {351.62192}}}{2}}\approx 1.68784.})

Since all eigenvalues are positive, J ( x 8 ) {\displaystyle \mathbf {J} (\mathbf {x} _{8})} ({\displaystyle \mathbf {J} (\mathbf {x} _{8})}) is positive definite, and therefore x 8 {\displaystyle \mathbf {x} _{8}} ({\displaystyle \mathbf {x} _{8}}) is a minimum.

### Complex functions

When dealing with complex functions, Newton's method can be directly applied to find their zeroes. Each zero has a basin of attraction in the complex plane, the set of all starting values that cause the method to converge to that particular zero. These sets can be mapped as in the image shown. For many complex functions, the boundaries of the basins of attraction are fractals.

In some cases there are regions in the complex plane which are not in any of these basins of attraction, meaning the iterates do not converge. For example, if one uses a real initial condition to seek a root of *x*2 + 1, all subsequent iterates will be real numbers and so the iterations cannot converge to either root, since both roots are non-real. In this case almost all real initial conditions lead to chaotic behavior, while some initial conditions iterate either to infinity or to repeating cycles of any finite length.

Curt McMullen has shown that for any possible purely iterative algorithm similar to Newton's method, the algorithm will diverge on some open regions of the complex plane when applied to some polynomial of degree 4 or higher. However, McMullen gave a generally convergent algorithm for polynomials of degree 3. Also, for any polynomial, Hubbard, Schleicher, and Sutherland gave a method for selecting a set of initial points such that Newton's method will certainly converge at one of them at least.

### In a Banach space

Another generalization is Newton's method to find a root of a functional F defined in a Banach space. In this case the formulation is

X n + 1 = X n − ( F ′ ( X n ) ) − 1 F ( X n ) , {\displaystyle X_{n+1}=X_{n}-{\bigl (}F'(X_{n}){\bigr )}^{-1}F(X_{n}),\,} ({\displaystyle X_{n+1}=X_{n}-{\bigl (}F'(X_{n}){\bigr )}^{-1}F(X_{n}),\,})

where *F′*(*X**n*) is the Fréchet derivative computed at *X**n*. One needs the Fréchet derivative to be boundedly invertible at each *X**n* in order for the method to be applicable. A condition for existence of and convergence to a root is given by the Newton–Kantorovich theorem.

#### Nash–Moser iteration

In the 1950s, John Nash developed a version of the Newton's method to apply to the problem of constructing isometric embeddings of general Riemannian manifolds in Euclidean space. The *loss of derivatives* problem, present in this context, made the standard Newton iteration inapplicable, since it could not be continued indefinitely (much less converge). Nash's solution involved the introduction of smoothing operators into the iteration. He was able to prove the convergence of his smoothed Newton method, for the purpose of proving an implicit function theorem for isometric embeddings. In the 1960s, Jürgen Moser showed that Nash's methods were flexible enough to apply to problems beyond isometric embedding, particularly in celestial mechanics. Since then, a number of mathematicians, including Mikhael Gromov and Richard Hamilton, have found generalized abstract versions of the Nash–Moser theory. In Hamilton's formulation, the Nash–Moser theorem forms a generalization of the Banach space Newton method which takes place in certain Fréchet spaces.


## Modifications

### Quasi-Newton methods

When the Jacobian is unavailable or too expensive to compute at every iteration, a quasi-Newton method can be used.

### Chebyshev's third-order method

Since higher-order Taylor expansions offer more accurate local approximations of a function f, it is reasonable to ask why Newton’s method relies only on a second-order Taylor approximation. In the 19th century, Russian mathematician Pafnuty Chebyshev explored this idea by developing a variant of Newton’s method that used cubic approximations.

### Over p-adic numbers

In p-adic analysis, the standard method to show a polynomial equation in one variable has a p-adic root is Hensel's lemma, which uses the recursion from Newton's method on the p-adic numbers. Because of the more stable behavior of addition and multiplication in the p-adic numbers compared to the real numbers (specifically, the unit ball in the p-adics is a ring), convergence in Hensel's lemma can be guaranteed under much simpler hypotheses than in the classical Newton's method on the real line.

### q-analog

Newton's method can be generalized with the q-analog of the usual derivative.

### Modified Newton methods

#### Maehly's procedure

A nonlinear equation has multiple solutions in general. But if the initial value is not appropriate, Newton's method may not converge to the desired solution or may converge to the same solution found earlier. When we have already found N solutions of f ( x ) = 0 {\displaystyle f(x)=0} ({\displaystyle f(x)=0}), then the next root can be found by applying Newton's method to the next equation:

F ( x ) = f ( x ) ∏ i = 1 N ( x − x i ) = 0. {\displaystyle F(x)={\frac {f(x)}{\prod _{i=1}^{N}(x-x_{i})}}=0.} ({\displaystyle F(x)={\frac {f(x)}{\prod _{i=1}^{N}(x-x_{i})}}=0.})

This method is applied to obtain zeros of the Bessel function of the second kind.

#### Hirano's modified Newton method

Hirano's modified Newton method is a modification conserving the convergence of Newton method and avoiding unstableness. It is developed to solve complex polynomials.

#### Interval Newton's method

Combining Newton's method with interval arithmetic is very useful in some contexts. This provides a stopping criterion that is more reliable than the usual ones (which are a small value of the function or a small variation of the variable between consecutive iterations). Also, this may detect cases where Newton's method converges theoretically but diverges numerically because of an insufficient floating-point precision (this is typically the case for polynomials of large degree, where a very small change of the variable may change dramatically the value of the function; see Wilkinson's polynomial).

Consider *f* → C1(*X*), where X is a real interval, and suppose that we have an interval extension F′ of f′, meaning that F′ takes as input an interval *Y* ⊆ *X* and outputs an interval *F′*(*Y*) such that:

F ′ ( [ y , y ] ) = { f ′ ( y ) } F ′ ( Y ) ⊇ { f ′ ( y ) ∣ y ∈ Y } . {\displaystyle {\begin{aligned}F'([y,y])&=\{f'(y)\}\\[5pt]F'(Y)&\supseteq \{f'(y)\mid y\in Y\}.\end{aligned}}} ({\displaystyle {\begin{aligned}F'([y,y])&=\{f'(y)\}\\[5pt]F'(Y)&\supseteq \{f'(y)\mid y\in Y\}.\end{aligned}}})

We also assume that 0 ∉ *F′*(*X*), so in particular f has at most one root in X. We then define the interval Newton operator by:

N ( Y ) = m − f ( m ) F ′ ( Y ) = { m − f ( m ) z   |   z ∈ F ′ ( Y ) } {\displaystyle N(Y)=m-{\frac {f(m)}{F'(Y)}}=\left\{\left.m-{\frac {f(m)}{z}}~\right|~z\in F'(Y)\right\}} ({\displaystyle N(Y)=m-{\frac {f(m)}{F'(Y)}}=\left\{\left.m-{\frac {f(m)}{z}}~\right|~z\in F'(Y)\right\}})

where *m* ∈ *Y*. Note that the hypothesis on F′ implies that *N*(*Y*) is well defined and is an interval (see interval arithmetic for further details on interval operations). This naturally leads to the following sequence:

X 0 = X X k + 1 = N ( X k ) ∩ X k . {\displaystyle {\begin{aligned}X_{0}&=X\\X_{k+1}&=N(X_{k})\cap X_{k}.\end{aligned}}} ({\displaystyle {\begin{aligned}X_{0}&=X\\X_{k+1}&=N(X_{k})\cap X_{k}.\end{aligned}}})

The mean value theorem ensures that if there is a root of f in *X**k*, then it is also in *X**k* + 1. Moreover, the hypothesis on F′ ensures that *X**k* + 1 is at most half the size of *X**k* when m is the midpoint of Y, so this sequence converges towards [*x**, *x**], where x* is the root of f in X.

If *F′*(*X*) strictly contains 0, the use of extended interval division produces a union of two intervals for *N*(*X*); multiple roots are therefore automatically separated and bounded.


## Applications

### Minimization and maximization problems

Newton's method can be used to find a minimum or maximum of a function *f*(*x*). The derivative is zero at a minimum or maximum, so local minima and maxima can be found by applying Newton's method to the derivative. The iteration becomes:

x n + 1 = x n − f ′ ( x n ) f ″ ( x n ) . {\displaystyle x_{n+1}=x_{n}-{\frac {f'(x_{n})}{f''(x_{n})}}.} ({\displaystyle x_{n+1}=x_{n}-{\frac {f'(x_{n})}{f''(x_{n})}}.})

### Multiplicative inverses of numbers and power series

An important application is Newton–Raphson division, which can be used to quickly find the reciprocal of a number a, using only multiplication and subtraction, that is to say the number x such that ⁠1/*x*⁠ = *a*. We can rephrase that as finding the zero of *f*(*x*) = ⁠1/*x*⁠ − *a*. We have *f′*(*x*) = −⁠1/*x*2⁠.

Newton's iteration is

x n + 1 = x n − f ( x n ) f ′ ( x n ) = x n + 1 x n − a 1 x n 2 = x n ( 2 − a x n ) . {\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=x_{n}+{\frac {{\frac {1}{x_{n}}}-a}{\frac {1}{x_{n}^{2}}}}=x_{n}(2-ax_{n}).} ({\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}=x_{n}+{\frac {{\frac {1}{x_{n}}}-a}{\frac {1}{x_{n}^{2}}}}=x_{n}(2-ax_{n}).})

Therefore, Newton's iteration needs only two multiplications and one subtraction.

This method is also very efficient to compute the multiplicative inverse of a power series.

### Solving transcendental equations

Many transcendental equations can be solved up to an arbitrary precision by using Newton's method. For example, finding the cumulative probability density function, such as a Normal distribution to fit a known probability generally involves integral functions with no known means to solve in closed form. However, computing the derivatives needed to solve them numerically with Newton's method is generally known, making numerical solutions possible. For an example, see the numerical solution to the inverse Normal cumulative distribution.

### Numerical verification for solutions of nonlinear equations

A numerical verification for solutions of nonlinear equations has been established by using Newton's method multiple times and forming a set of solution candidates.


## Code

The following is an example of a possible implementation of Newton's method in the Python (version 3.x) programming language for finding a root of a function `f` which has derivative `f_prime`.

The initial guess will be *x*0 = 1 and the function will be *f*(*x*) = *x*2 − 2 so that *f′*(*x*) = 2*x*.

Each new iteration of Newton's method will be denoted by `x1`. We will check during the computation whether the denominator (`y_prime`) becomes too small (smaller than `epsilon`), which would be the case if *f′*(*x**n*) ≈ 0, since otherwise a large amount of error could be introduced.

```mw
def f(x):             
	return x**2 - 2   # f(x) = x^2 - 2

def f_prime(x):
	return 2*x        # f'(x) = 2x

def newtons_method(x0, f, f_prime, tolerance, epsilon, max_iterations):
    """Newton's method

    Args:
      x0:              The initial guess
      f:               The function whose root we are trying to find
      f_prime:         The derivative of the function
      tolerance:       Stop when iterations change by less than this
      epsilon:         Do not divide by a number smaller than this
      max_iterations:  The maximum number of iterations to compute
    """
    for _ in range(max_iterations):
        y = f(x0)
        y_prime = f_prime(x0)

        if abs(y_prime) < epsilon:       # Give up if the denominator is too small
            break

        x1 = x0 - y / y_prime            # Do Newton's computation

        if abs(x1 - x0) <= tolerance:   # Stop when the result is within the desired tolerance
            return x1                   # x1 is a solution within tolerance and maximum number of iterations

        x0 = x1                         # Update x0 to start the process again

    return None                         # Newton's method did not converge
```
