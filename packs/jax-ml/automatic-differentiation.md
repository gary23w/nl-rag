---
title: "Automatic differentiation"
source: https://en.wikipedia.org/wiki/Automatic_differentiation
domain: jax-ml
license: CC-BY-SA-4.0
tags: jax library, autograd differentiation, just in time compilation, numpy vectorization, accelerator computing
fetched: 2026-07-02
---

# Automatic differentiation

In mathematics and computer algebra, **automatic differentiation** (**auto-differentiation**, **autodiff**, or **AD**), also called **algorithmic differentiation**, **computational differentiation**, and **differentiation arithmetic** is a set of techniques to evaluate the partial derivative of a function specified by a computer program. Automatic differentiation is a subtle and central tool to automatize the simultaneous computation of the numerical values of arbitrarily complex functions and their derivatives with no need for the symbolic representation of the derivative; only the function rule or an algorithm thereof is required. Auto-differentiation is thus neither numeric nor symbolic, nor is it a combination of both. In contrast to the more traditional numerical methods based on finite differences, auto-differentiation is 'in theory' exact, and in comparison to symbolic algorithms, it is computationally inexpensive.

Automatic differentiation exploits the fact that every computer calculation, no matter how complicated, executes a sequence of elementary arithmetic operations (addition, subtraction, multiplication, division, etc.) and elementary functions (exp, log, sin, cos, etc.). By applying the chain rule repeatedly to these operations, partial derivatives of arbitrary order can be computed automatically, accurately to working precision, and using at most a small constant factor of more arithmetic operations than the original program.

## Difference from other differentiation methods

Automatic differentiation is distinct from symbolic differentiation and numerical differentiation. Symbolic differentiation faces the difficulty of converting a computer program into a single mathematical expression and can lead to inefficient code. Numerical differentiation (the method of finite differences) can introduce round-off errors in the discretization process and cancellation. Both of these classical methods have problems with calculating higher derivatives, where complexity and errors increase. Finally, both of these classical methods are slow at computing partial derivatives of a function with respect to *many* inputs, as is needed for gradient-based optimization algorithms. Automatic differentiation solves all of these problems.

## Applications

Because of its efficiency and accuracy in computing first and higher order derivatives, auto-differentiation finds diverse applications in scientific computing and mathematics, and there are numerous computational implementations of auto-differentiation. Among these, one mentions INTLAB, Sollya, and InCLosure. In practice, there are two types (modes) of algorithmic differentiation: a forward-type and a reversed-type. Presently, the two types are highly correlated and complementary and both have a wide variety of applications in, e.g., non-linear optimization, sensitivity analysis, robotics, machine learning, computer graphics, and computer vision. Automatic differentiation is particularly important in the field of machine learning. For example, it allows one to implement backpropagation in a neural network without a manually-computed derivative.

## Forward and reverse accumulation

### Chain rule of partial derivatives of composite functions

Fundamental to automatic differentiation is the decomposition of differentials provided by the chain rule of partial derivatives of composite functions. For the simple composition ${\begin{aligned}y&=f(g(h(x)))=f(g(h(w_{0})))=f(g(w_{1}))=f(w_{2})=w_{3}\\w_{0}&=x\\w_{1}&=h(w_{0})\\w_{2}&=g(w_{1})\\w_{3}&=f(w_{2})=y\end{aligned}}$ the chain rule gives ${\frac {\partial y}{\partial x}}={\frac {\partial y}{\partial w_{2}}}{\frac {\partial w_{2}}{\partial w_{1}}}{\frac {\partial w_{1}}{\partial x}}={\frac {\partial f(w_{2})}{\partial w_{2}}}{\frac {\partial g(w_{1})}{\partial w_{1}}}{\frac {\partial h(w_{0})}{\partial x}}$

### Two types of automatic differentiation

Usually, two distinct modes of automatic differentiation are presented.

- **forward accumulation** (also called **bottom-up**, **forward mode**, or **tangent mode**)
- **reverse accumulation** (also called **top-down**, **reverse mode**, or **adjoint mode**)

Forward accumulation specifies that one traverses the chain rule from inside to outside (that is, first compute ${\textstyle {\frac {\partial w_{1}}{\partial x}}}$ and then ${\textstyle {\frac {\partial w_{2}}{\partial w_{1}}}}$ and lastly ${\textstyle {\frac {\partial y}{\partial w_{2}}}}$ ), while reverse accumulation traverses from outside to inside (first compute ${\textstyle {\frac {\partial y}{\partial w_{2}}}}$ and then ${\textstyle {\frac {\partial w_{2}}{\partial w_{1}}}}$ and lastly ${\textstyle {\frac {\partial w_{1}}{\partial x}}}$ ). More succinctly,

- Forward accumulation computes the recursive relation: ${\frac {\partial w_{i}}{\partial x}}={\frac {\partial w_{i}}{\partial w_{i-1}}}{\frac {\partial w_{i-1}}{\partial x}}\quad {\text{with }}w_{3}=y,$
- Reverse accumulation computes the recursive relation: ${\frac {\partial y}{\partial w_{i}}}={\frac {\partial y}{\partial w_{i+1}}}{\frac {\partial w_{i+1}}{\partial w_{i}}}\quad {\text{with }}w_{0}=x.$

The value of the partial derivative, called the *seed*, is propagated forward or backward and is initially ${\textstyle {\frac {\partial x}{\partial x}}=1}$ or ${\textstyle {\frac {\partial y}{\partial y}}=1}$ . Forward accumulation evaluates the function and calculates the derivative with respect to one independent variable in one pass. For each independent variable ${\textstyle x_{1},x_{2},\dots ,x_{n}}$ a separate pass is therefore necessary in which the derivative with respect to that independent variable is set to one ( ${\textstyle {\frac {\partial x_{1}}{\partial x_{1}}}=1}$ ) and of all others to zero ( ${\textstyle {\frac {\partial x_{2}}{\partial x_{1}}}=\dots ={\frac {\partial x_{n}}{\partial x_{1}}}=0}$ ). In contrast, reverse accumulation requires the evaluated partial functions for the partial derivatives. Reverse accumulation therefore evaluates the function first and calculates the derivatives with respect to all independent variables in an additional pass.

Which of these two types should be used depends on the sweep count. The computational complexity of one sweep is proportional to the complexity of the original code.

- Forward accumulation is more efficient than reverse accumulation for functions $f:\mathbb {R} ^{n}\to \mathbb {R} ^{m}$ with $n\ll m$ as only n sweeps are necessary, compared to m sweeps for reverse accumulation.
- Reverse accumulation is more efficient than forward accumulation for functions $f:\mathbb {R} ^{n}\to \mathbb {R} ^{m}$ with $n\gg m$ as only m sweeps are necessary, compared to n sweeps for forward accumulation.

Backpropagation of errors in multilayer perceptrons, a technique used in machine learning, is a special case of reverse accumulation.

Forward accumulation was introduced by R. E. Wengert in 1964. According to Andreas Griewank, reverse accumulation has been suggested since the late 1960s, but the inventor is unknown. Seppo Linnainmaa published reverse accumulation in 1976.

### Forward accumulation

In forward accumulation AD, one first fixes the *independent variable* with respect to which differentiation is performed and computes the derivative of each sub-expression recursively. In a pen-and-paper calculation, this involves repeatedly substituting the derivative of the *inner* functions in the chain rule: ${\begin{aligned}{\frac {\partial y}{\partial x}}&={\frac {\partial y}{\partial w_{n-1}}}{\frac {\partial w_{n-1}}{\partial x}}\\[6pt]&={\frac {\partial y}{\partial w_{n-1}}}\left({\frac {\partial w_{n-1}}{\partial w_{n-2}}}{\frac {\partial w_{n-2}}{\partial x}}\right)\\[6pt]&={\frac {\partial y}{\partial w_{n-1}}}\left({\frac {\partial w_{n-1}}{\partial w_{n-2}}}\left({\frac {\partial w_{n-2}}{\partial w_{n-3}}}{\frac {\partial w_{n-3}}{\partial x}}\right)\right)\\[6pt]&=\cdots \end{aligned}}$ This can be generalized to multiple variables as a matrix product of Jacobians.

Compared to reverse accumulation, forward accumulation is natural and easy to implement as the flow of derivative information coincides with the order of evaluation. Each variable $w_{i}$ is augmented with its derivative ${\dot {w}}_{i}$ (stored as a numerical value, not a symbolic expression), ${\dot {w}}_{i}={\frac {\partial w_{i}}{\partial x}}$ as denoted by the dot. The derivatives are then computed in sync with the evaluation steps and combined with other derivatives via the chain rule.

Using the chain rule, if $w_{i}$ has predecessors in the computational graph: ${\dot {w}}_{i}=\sum _{j\in \{{\text{predecessors of }}i\}}{\frac {\partial w_{i}}{\partial w_{j}}}{\dot {w}}_{j}$

As an example, consider the function: ${\begin{aligned}y&=f(x_{1},x_{2})\\&=x_{1}x_{2}+\sin x_{1}\\&=w_{1}w_{2}+\sin w_{1}\\&=w_{3}+w_{4}\\&=w_{5}\end{aligned}}$ For clarity, the individual sub-expressions have been labeled with the variables $w_{i}$ .

The choice of the independent variable to which differentiation is performed affects the *seed* values *ẇ*1 and *ẇ*2. Given interest in the derivative of this function with respect to *x*1, the seed values should be set to: ${\begin{aligned}{\dot {w}}_{1}={\frac {\partial w_{1}}{\partial x_{1}}}={\frac {\partial x_{1}}{\partial x_{1}}}=1\\{\dot {w}}_{2}={\frac {\partial w_{2}}{\partial x_{1}}}={\frac {\partial x_{2}}{\partial x_{1}}}=0\end{aligned}}$

With the seed values set, the values propagate using the chain rule as shown. Figure 2 shows a pictorial depiction of this process as a computational graph.

| Operations to compute value | Operations to compute derivative |
|---|---|
| $w_{1}=x_{1}$ | ${\dot {w}}_{1}=1$ (seed) |
| $w_{2}=x_{2}$ | ${\dot {w}}_{2}=0$ (seed) |
| $w_{3}=w_{1}\cdot w_{2}$ | ${\dot {w}}_{3}=w_{2}\cdot {\dot {w}}_{1}+w_{1}\cdot {\dot {w}}_{2}$ |
| $w_{4}=\sin w_{1}$ | ${\dot {w}}_{4}=\cos w_{1}\cdot {\dot {w}}_{1}$ |
| $w_{5}=w_{3}+w_{4}$ | ${\dot {w}}_{5}={\dot {w}}_{3}+{\dot {w}}_{4}$ |

To compute the gradient of this example function, which requires not only ${\textstyle {\frac {\partial y}{\partial x_{1}}}}$ but also ${\textstyle {\frac {\partial y}{\partial x_{2}}}}$ , an *additional* sweep is performed over the computational graph using the seed values ${\textstyle {\dot {w}}_{1}=0}$ ; ${\textstyle {\dot {w}}_{2}=1}$ .

#### Implementation

##### Pseudocode

Forward accumulation calculates the function and the derivative (but only for one independent variable each) in one pass. The associated method call expects the expression Z to be derived with regard to a variable V. The method returns a pair of the evaluated function and its derivative. The method traverses the expression tree recursively until a variable is reached. If the derivative with respect to this variable is requested, its derivative is 1, 0 otherwise. Then the partial function as well as the partial derivative are evaluated.

```mw
tuple<float,float> evaluateAndDerive(Expression Z, Variable V) {
   if isVariable(Z)
      if (Z = V) return {valueOf(Z), 1};
      else return {valueOf(Z), 0};
   else if (Z = A + B)
      {a, a'} = evaluateAndDerive(A, V);
      {b, b'} = evaluateAndDerive(B, V);
      return {a + b, a' + b'};
   else if (Z = A - B)
      {a, a'} = evaluateAndDerive(A, V);
      {b, b'} = evaluateAndDerive(B, V);
      return {a - b, a' - b'};
   else if (Z = A * B)
      {a, a'} = evaluateAndDerive(A, V);
      {b, b'} = evaluateAndDerive(B, V);
      return {a * b, b * a' + a * b'};
}
```

##### C++

```mw
#include <iostream>
struct ValueAndPartial { float value, partial; };
struct Variable;
struct Expression {
   virtual ValueAndPartial evaluateAndDerive(Variable &variable) = 0;
};
struct Variable: public Expression {
   float value;
   Variable(float value): value(value) {}
   ValueAndPartial evaluateAndDerive(Variable &variable) {
      float partial = (this == &variable) ? 1.0f : 0.0f;
      return {value, partial};
   }
};
struct Plus: public Expression {
   Expression &a, &b;
   Plus(Expression &a, Expression &b): a(a), b(b) {}
   ValueAndPartial evaluateAndDerive(Variable &variable) {
      auto [valueA, partialA] = a.evaluateAndDerive(variable);
      auto [valueB, partialB] = b.evaluateAndDerive(variable);
      return {valueA + valueB, partialA + partialB};
   }
};
struct Multiply: public Expression {
   Expression &a, &b;
   Multiply(Expression &a, Expression &b): a(a), b(b) {}
   ValueAndPartial evaluateAndDerive(Variable &variable) {
      auto [valueA, partialA] = a.evaluateAndDerive(variable);
      auto [valueB, partialB] = b.evaluateAndDerive(variable);
      return {valueA * valueB, valueB * partialA + valueA * partialB};
   }
};
int main () {
   // Example: Finding the partials of z = x * (x + y) + y * y at (x, y) = (2, 3)
   Variable x(2), y(3);
   Plus p1(x, y); Multiply m1(x, p1); Multiply m2(y, y); Plus z(m1, m2);
   float xPartial = z.evaluateAndDerive(x).partial;
   float yPartial = z.evaluateAndDerive(y).partial;
   std::cout << "∂z/∂x = " << xPartial << ", "
             << "∂z/∂y = " << yPartial << std::endl;
   // Output: ∂z/∂x = 7, ∂z/∂y = 8
   return 0;
}
```

### Reverse accumulation

In reverse accumulation AD, the *dependent variable* to be differentiated is fixed and the derivative is computed *with respect to* each sub-expression recursively. In a pen-and-paper calculation, the derivative of the *outer* functions is repeatedly substituted in the chain rule: ${\begin{aligned}{\frac {\partial y}{\partial x}}&={\frac {\partial y}{\partial w_{1}}}{\frac {\partial w_{1}}{\partial x}}\\[6px]&=\left({\frac {\partial y}{\partial w_{2}}}{\frac {\partial w_{2}}{\partial w_{1}}}\right){\frac {\partial w_{1}}{\partial x}}\\[6px]&=\left(\left({\frac {\partial y}{\partial w_{3}}}{\frac {\partial w_{3}}{\partial w_{2}}}\right){\frac {\partial w_{2}}{\partial w_{1}}}\right){\frac {\partial w_{1}}{\partial x}}\\[6px]&=\cdots \end{aligned}}$

In reverse accumulation, the quantity of interest is the *adjoint*, denoted with a bar ${\bar {w}}_{i}$ ; it is a derivative of a chosen dependent variable with respect to a subexpression $w_{i}$ : ${\bar {w}}_{i}={\frac {\partial y}{\partial w_{i}}}$

Using the chain rule, if $w_{i}$ has successors in the computational graph: ${\bar {w}}_{i}=\sum _{j\in \{{\text{successors of }}i\}}{\bar {w}}_{j}{\frac {\partial w_{j}}{\partial w_{i}}}$

Reverse accumulation traverses the chain rule from outside to inside, or in the case of the computational graph in Figure 3, from top to bottom. The example function is scalar-valued, and thus there is only one seed for the derivative computation, and only one sweep of the computational graph is needed to calculate the (two-component) gradient. This is only half the work when compared to forward accumulation, but reverse accumulation requires the storage of the intermediate variables *w**i* as well as the instructions that produced them in a data structure known as a "tape" or a Wengert list (however, Wengert published forward accumulation, not reverse accumulation), which may consume significant memory if the computational graph is large. This can be mitigated to some extent by storing only a subset of the intermediate variables and then reconstructing the necessary work variables by repeating the evaluations, a technique known as rematerialization. Checkpointing is also used to save intermediary states.

We consider again the example function $y=f(x_{1},x_{2})=x_{1}x_{2}+\sin x_{1}$ with subexpressions $w_{1}=x_{1},$ $w_{2}=x_{2},$ $w_{3}=w_{1}w_{2},$ $w_{4}=\sin(w_{1}),$ $w_{5}=w_{3}+w_{4}$ . The operations to compute the adjoint values using reverse accumulation are shown in the table below (note the reversed order):

${\begin{aligned}{\bar {w}}_{5}&=1\quad {\text{(seed)}}\\{\bar {w}}_{4}&={\bar {w}}_{5}\cdot 1\\{\bar {w}}_{3}&={\bar {w}}_{5}\cdot 1\\{\bar {w}}_{2}&={\bar {w}}_{3}\cdot w_{1}\\{\bar {w}}_{1}&={\bar {w}}_{3}\cdot w_{2}+{\bar {w}}_{4}\cdot \cos w_{1}\end{aligned}}$ The sought-after partial derivatives are then $\partial y/\partial x_{1}={\bar {w}}_{1}$ and $\partial y/\partial x_{2}={\bar {w}}_{2}$ .

The data flow graph of a computation can be manipulated to calculate the gradient of its original calculation. This is done by adding an adjoint node for each primal node, connected by adjoint edges which parallel the primal edges but flow in the opposite direction. The nodes in the adjoint graph represent multiplication by the derivatives of the functions calculated by the nodes in the primal. For instance, addition in the primal causes fanout in the adjoint; fanout in the primal causes addition in the adjoint; a unary function *y* = *f*(*x*) in the primal causes *x̄* = *ȳ* *f*′(*x*) in the adjoint; etc.

#### Implementation

##### Pseudocode

Reverse accumulation requires two passes: In the forward pass, the function is evaluated first and the partial results are cached. In the reverse pass, the partial derivatives are calculated and the previously derived value is back-propagated. The corresponding method call expects the expression Z to be derived and *seeded* with the derived value of the parent expression. For the top expression, Z is differentiated with respect to Z, this is 1. The method traverses the expression tree recursively until a variable is reached and adds the current *seed* value to the derivative expression.

```mw
void derive(Expression Z, float seed) {
   if isVariable(Z)
      partialDerivativeOf(Z) += seed;
   else if (Z = A + B)
      derive(A, seed);
      derive(B, seed);
   else if (Z = A - B)
      derive(A, seed);
      derive(B, -seed);
   else if (Z = A * B)
      derive(A, valueOf(B) * seed);
      derive(B, valueOf(A) * seed);
}
```

##### C++

```mw
#include <iostream>
struct Expression {
   float value;
   virtual void evaluate() = 0;
   virtual void derive(float seed) = 0;
};
struct Variable: public Expression {
   float partial;
   Variable(float value) {
      this->value = value;
      partial = 0.0f;
   }
   void evaluate() {}
   void derive(float seed) {
      partial += seed;
   }
};
struct Plus: public Expression {
   Expression &a, &b;
   Plus(Expression &a, Expression &b): a(a), b(b) {}
   void evaluate() {
      a.evaluate();
      b.evaluate();
      value = a.value + b.value;
   }
   void derive(float seed) {
      a.derive(seed);
      b.derive(seed);
   }
};
struct Multiply: public Expression {
   Expression &a, &b;
   Multiply(Expression &a, Expression &b): a(a), b(b) {}
   void evaluate() {
      a.evaluate();
      b.evaluate();
      value = a.value * b.value;
   }
   void derive(float seed) {
      a.derive(b.value * seed);
      b.derive(a.value * seed);
   }
};
int main () {
   // Example: Finding the partials of z = x * (x + y) + y * y at (x, y) = (2, 3)
   Variable x(2), y(3);
   Plus p1(x, y); Multiply m1(x, p1); Multiply m2(y, y); Plus z(m1, m2);
   z.evaluate();
   std::cout << "z = " << z.value << std::endl;
   // Output: z = 19
   z.derive(1);
   std::cout << "∂z/∂x = " << x.partial << ", "
             << "∂z/∂y = " << y.partial << std::endl;
   // Output: ∂z/∂x = 7, ∂z/∂y = 8
   return 0;
}
```

### Beyond forward and reverse accumulation

Forward and reverse accumulation are just two (extreme) ways of traversing the chain rule. The problem of computing a full Jacobian of *f* : ℝ*n* → ℝ*m* with a minimum number of arithmetic operations is known as the *optimal Jacobian accumulation* (OJA) problem, which is NP-complete. Central to this proof is the idea that algebraic dependencies may exist between the local partials that label the edges of the graph. In particular, two or more edge labels may be recognized as equal. The complexity of the problem is still open if it is assumed that all edge labels are unique and algebraically independent.

## Automatic differentiation using dual numbers

Forward mode automatic differentiation is accomplished by augmenting the algebra of real numbers and obtaining a new arithmetic. An additional component is added to every number to represent the derivative of a function at the number, and all arithmetic operators are extended for the augmented algebra. The augmented algebra is the algebra of dual numbers.

Replace every number $\,x$ with the number $x+x'\varepsilon$ , where $x'$ is a real number, but $\varepsilon$ is an abstract number with the property $\varepsilon ^{2}=0$ (an infinitesimal; see *Smooth infinitesimal analysis*). Using only this, regular arithmetic gives ${\begin{aligned}(x+x'\varepsilon )+(y+y'\varepsilon )&=x+y+(x'+y')\varepsilon \\[4px](x+x'\varepsilon )-(y+y'\varepsilon )&=x-y+(x'-y')\varepsilon \\[4px](x+x'\varepsilon )\cdot (y+y'\varepsilon )&=xy+xy'\varepsilon +yx'\varepsilon +x'y'\varepsilon ^{2}=xy+(xy'+yx')\varepsilon \\[8px]{\frac {x+x'\varepsilon }{y+y'\varepsilon }}&={\frac {{\frac {x}{y}}+{\frac {x'\varepsilon }{y}}}{1+{\frac {y'\varepsilon }{y}}}}=\left({\frac {x}{y}}+{\frac {x'\varepsilon }{y}}\right)\cdot \left(1-{\frac {y'\varepsilon }{y}}\right)={\frac {x}{y}}+\left({\frac {x'}{y}}-{\frac {xy'}{y^{2}}}\right)\varepsilon \end{aligned}}$ using the fact that $\left(1+{\frac {y'\varepsilon }{y}}\right)\cdot \left(1-{\frac {y'\varepsilon }{y}}\right)=1.$

Now, polynomials can be calculated in this augmented arithmetic. If $P(x)=p_{0}+p_{1}x+p_{2}x^{2}+\cdots +p_{n}x^{n},$ then ${\begin{aligned}P(x+x'\varepsilon )&=p_{0}+p_{1}(x+x'\varepsilon )+\cdots +p_{n}(x+x'\varepsilon )^{n}\\&=p_{0}+p_{1}x+\cdots +p_{n}x^{n}+p_{1}x'\varepsilon +2p_{2}xx'\varepsilon +\cdots +np_{n}x^{n-1}x'\varepsilon \\&=P(x)+P^{(1)}(x)x'\varepsilon \end{aligned}}$ where $P^{(1)}$ denotes the derivative of P with respect to its first argument, and $x'$ , called a *seed*, can be chosen arbitrarily.

The new arithmetic consists of ordered pairs, elements written ${\textstyle \langle x,x'\rangle }$ , with ordinary arithmetics on the first component, and first order differentiation arithmetic on the second component, as described above. Extending the above results on polynomials to analytic functions gives a list of the basic arithmetic and some standard functions for the new arithmetic: ${\begin{aligned}\left\langle u,u'\right\rangle +\left\langle v,v'\right\rangle &=\left\langle u+v,u'+v'\right\rangle \\[4px]\left\langle u,u'\right\rangle -\left\langle v,v'\right\rangle &=\left\langle u-v,u'-v'\right\rangle \\[4px]\left\langle u,u'\right\rangle \cdot \left\langle v,v'\right\rangle &=\left\langle uv,u'v+uv'\right\rangle \\[8px]{\frac {\left\langle u,u'\right\rangle }{\left\langle v,v'\right\rangle }}&=\left\langle {\frac {u}{v}},{\frac {u'v-uv'}{v^{2}}}\right\rangle &&(v\neq 0)\\[8px]\sin \left\langle u,u'\right\rangle &=\left\langle \sin(u),u'\cos(u)\right\rangle \\[4px]\cos \left\langle u,u'\right\rangle &=\left\langle \cos(u),-u'\sin(u)\right\rangle \\[4px]e^{\left\langle u,u'\right\rangle }&=\left\langle e^{u},u'e^{u}\right\rangle \\[8px]\log \left\langle u,u'\right\rangle &=\left\langle \log(u),{\frac {u'}{u}}\right\rangle &&(u>0)\\[8px]\left\langle u,u'\right\rangle ^{k}&=\left\langle u^{k},u'ku^{k-1}\right\rangle &&(u\neq 0)\\[8px]\left|\left\langle u,u'\right\rangle \right|&=\left\langle \left|u\right|,u'\operatorname {sgn} u\right\rangle &&(u\neq 0)\end{aligned}}$ and in general for the primitive function g , $g(\langle u,u'\rangle ,\langle v,v'\rangle )=\langle g(u,v),g_{u}(u,v)u'+g_{v}(u,v)v'\rangle$ where $g_{u}$ and $g_{v}$ are the derivatives of g with respect to its first and second arguments, respectively.

When a binary basic arithmetic operation is applied to mixed arguments—the pair ${\textstyle \langle u,u'\rangle }$ and the real number c —the real number is first lifted to ${\textstyle \langle c,0\rangle }$ . The derivative of a function ${\textstyle f:\mathbb {R} \to \mathbb {R} }$ at the point $x_{0}$ is now found by calculating ${\textstyle f(\langle x_{0},1\rangle )}$ using the above arithmetic, which gives ${\textstyle \langle f(x_{0}),f'(x_{0})\rangle }$ as the result.

### Implementation

An example implementation based on the dual number approach follows.

#### Pseudocode

```
Dual plus(Dual A, Dual B) {
  return {
    realPartOf(A) + realPartOf(B),
    infinitesimalPartOf(A) + infinitesimalPartOf(B)
  };
}
Dual minus(Dual A, Dual B) {
  return {
    realPartOf(A) - realPartOf(B),
    infinitesimalPartOf(A) - infinitesimalPartOf(B)
  };
}
Dual multiply(Dual A, Dual B) {
  return {
    realPartOf(A) * realPartOf(B),
    realPartOf(B) * infinitesimalPartOf(A) + realPartOf(A) * infinitesimalPartOf(B)
  };
}
X = {x, 0};
Y = {y, 0};
Epsilon = {0, 1};
xPartial = infinitesimalPartOf(f(X + Epsilon, Y));
yPartial = infinitesimalPartOf(f(X, Y + Epsilon));
```

#### C++

```mw
#include <iostream>
struct Dual {
   float realPart, infinitesimalPart;
   Dual(float realPart, float infinitesimalPart=0): realPart(realPart), infinitesimalPart(infinitesimalPart) {}
   Dual operator+(Dual other) {
      return Dual(
         realPart + other.realPart,
         infinitesimalPart + other.infinitesimalPart
      );
   }
   Dual operator*(Dual other) {
      return Dual(
         realPart * other.realPart,
         other.realPart * infinitesimalPart + realPart * other.infinitesimalPart
      );
   }
};
// Example: Finding the partials of z = x * (x + y) + y * y at (x, y) = (2, 3)
Dual f(Dual x, Dual y) { return x * (x + y) + y * y; }
int main () {
   Dual x = Dual(2);
   Dual y = Dual(3);
   Dual epsilon = Dual(0, 1);
   Dual a = f(x + epsilon, y);
   Dual b = f(x, y + epsilon);
   std::cout << "∂z/∂x = " << a.infinitesimalPart << ", "
             << "∂z/∂y = " << b.infinitesimalPart << std::endl;
   // Output: ∂z/∂x = 7, ∂z/∂y = 8
   return 0;
}
```

### Vector arguments and functions

Multivariate functions can be handled with the same efficiency and mechanisms as univariate functions by adopting a directional derivative operator. That is, if it is sufficient to compute ${\textstyle y'=\nabla f(x)\cdot x'}$ , the directional derivative ${\textstyle y'\in \mathbb {R} ^{m}}$ of ${\textstyle f:\mathbb {R} ^{n}\to \mathbb {R} ^{m}}$ at ${\textstyle x\in \mathbb {R} ^{n}}$ in the direction ${\textstyle x'\in \mathbb {R} ^{n}}$ may be calculated as $(\langle y_{1},y'_{1}\rangle ,\ldots ,\langle y_{m},y'_{m}\rangle )=f(\langle x_{1},x'_{1}\rangle ,\ldots ,\langle x_{n},x'_{n}\rangle )$ using the same arithmetic as above. If all the elements of $\nabla f$ are desired, then n function evaluations are required. Note that in many optimization applications, the directional derivative is indeed sufficient.

### High order and many variables

The above arithmetic can be generalized to calculate second order and higher derivatives of multivariate functions. However, the arithmetic rules quickly grow complicated: complexity is quadratic in the highest derivative degree. Instead, truncated Taylor polynomial algebra can be used. The resulting arithmetic, defined on generalized dual numbers, allows efficient computation using functions as if they were a data type. Once the Taylor polynomial of a function is known, the derivatives are easily extracted.

## Implementation

Forward-mode AD is implemented by a nonstandard interpretation of the program in which real numbers are replaced by dual numbers, constants are lifted to dual numbers with a zero epsilon coefficient, and the numeric primitives are lifted to operate on dual numbers. This nonstandard interpretation is generally implemented using one of two strategies: *source code transformation* or *operator overloading*.

### Source code transformation (SCT)

The source code for a function is replaced by an automatically generated source code that includes statements for calculating the derivatives interleaved with the original instructions.

Source code transformation can be implemented for all programming languages, and it is also easier for the compiler to do compile time optimizations. However, the implementation of the AD tool itself is more difficult and the build system is more complex.

### Operator overloading (OO)

Operator overloading is a possibility for source code written in a language supporting it. Objects for real numbers and elementary mathematical operations must be overloaded to cater for the augmented arithmetic depicted above. This requires no change in the form or sequence of operations in the original source code for the function to be differentiated, but often requires changes in basic data types for numbers and vectors to support overloading and often also involves the insertion of special flagging operations. Due to the inherent operator overloading overhead on each loop, this approach usually demonstrates weaker speed performance.

### Operator overloading and source code transformation

Overloaded Operators can be used to extract the valuation graph, followed by automatic generation of the AD-version of the primal function at run-time. Unlike the classic OO AAD, such AD-function does not change from one iteration to the next one. Hence there is any OO or tape interpretation run-time overhead per Xi sample.

With the AD-function being generated at runtime, it can be optimised to take into account the current state of the program and precompute certain values. In addition, it can be generated in a way to consistently utilize native CPU vectorization to process 4(8)-double chunks of user data (AVX2\AVX512 speed up x4-x8). With multithreading added into account, such approach can lead to a final acceleration of order 8 × #Cores compared to the traditional AAD tools. A reference implementation is available on GitHub.
