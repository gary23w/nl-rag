---
title: "Narrowing of algebraic value sets"
source: https://en.wikipedia.org/wiki/Narrowing_of_algebraic_value_sets
domain: curry-language
license: CC-BY-SA-4.0
tags: curry language, functional logic programming, haskell language, lazy evaluation, narrowing algebraic
fetched: 2026-07-02
---

# Narrowing of algebraic value sets

Like logic programming, **narrowing** **of algebraic value sets** gives a method of reasoning about the values in unsolved or partially solved equations. Where logic programming relies on resolution, the algebra of value sets relies on narrowing rules. Narrowing rules allow the elimination of values from a solution set which are inconsistent with the equations being solved.

Unlike logic programming, narrowing of algebraic value sets makes no use of backtracking. Instead all values are contained in value sets, and are considered in parallel.

The approach is also similar to the use of constraints in constraint logic programming, but without the logic processing basis.

Probabilistic value sets is a natural extension of value sets to deductive probability. The value set construct holds the information required to calculate probabilities of calculated values based on probabilities of initial values.

## History

Early programming languages were imperative. These implement functionality by allowing change to be represented. The assignment statement allows a variable to change its value.

In mathematics a variable's value may not change. This is fundamental to the mathematical approach. Functional languages based on lambda calculus allow this mathematical approach to programming. Functional languages developed by implementing lazy evaluation, and allowing functions to be passed as parameters.

Lazy evaluation is an essential feature of modern functional programming languages such as Haskell. Haskell is the latest in a series of languages based on lambda calculus and let expressions. These languages provide rich functionality through lazy evaluation, and a polymorphic type system using type inference. Functional programming languages also naturally support higher-order functions.

Logic programming based on Resolution developed alongside functional programming. Logic programming is a form of relational programming that makes deductions about values. Constraint logic programming extends logic programming, by supporting constraints. Constraint logic programming languages such as ECLiPSe provide the ability to solve complex logic problems. However ECLiPSe is not lazy.

Logic programming languages, although they have greater deduction abilities, never gained the power and flexibility of functional languages.

Narrowing is a technique that allows logical deduction, with the flexibility of functional languages.

## Introduction

In mathematics an expression represents a single value. A function maps one or more values to one unique value.

Inverses of functions are not always well defined as functions. Sometimes extra conditions are required to make an inverse of a function fit the definition of a function.

Some Boolean operations, in particular do not have inverses that may be defined as functions. In particular the disjunction "or" has inverses that allow two values. In natural language "or" represents alternate possibilities.

Narrowing is based on value sets that allow multiple values to be packaged and considered as a single value. This allows the inverses of functions to always be considered as functions.

To achieve this value sets must record the context to which a value belongs. A variable may only take on a single value in each possible world. The value sets tag each value in the value set with the world to which it belongs.

Possible worlds belong to world sets. A world set is a set of all mutually exclusive worlds. Combining values from different possible worlds is impossible, because that would mean combining mutually exclusive possible worlds.

The application of functions to value sets creates combinations of value sets from different worlds. Narrowing reduces those worlds by eliminating combinations of different worlds from the same world set. Narrowing rules also detect situations where some combinations of worlds are shown to be impossible.

No back tracking is required in the use of narrowing. By packaging the possible values in a value set all combinations of values may be considered at the same time. Evaluation proceeds as for a functional language, combining combinations of values in value sets, with narrowing rules eliminating impossible values from the sets.

## Introduction to value sets

A *value set* is an object, which represents the set of values a variable may have. The value set behaves mathematically as a single value, while internally representing multiple values. To achieve this the value set tracks the value along with the context, or world, in which they occurred.

### Multiple solutions to an equation

In mathematics, an expression must represent a single value. For example consider the equation,

$x^{2}=4$

which implies,

$x=2\lor x=-2$

But this is a bit long winded, and it does not allow us to work with multiple values at the same time. If further conditions or constraints are added to x we would like to consider each value to see if it matches the constraint. So naively we would like to write,

$x=\pm 2$

Naively then,

$x+x\in \lbrace 4,0,-4\rbrace$

but this is wrong. Each x must represent a single value in the expression. Either x is 2 or x = −2. This can be resolved by keeping track of the two values so that we make sure that the values are used consistently, and this is what a value set does.

### Representation

The value set for 'x' is written as,

$V(\{2::x_{1},-2::x_{2}\})$

It is container *V* which has a set of tag, value pairs,

- $2::x_{1}$
- $-2::x_{2}$

The value 2 is associated with the possible world $x_{1}$ . The value −2 is associated with the possible world $x_{2}$ . This means that the value cannot be both 2 and −2 at the same time. In the world $x_{1}$ the value of the value set must be 2. In the world $x_{2}$ the value of the value set must be −2.

The solution of the equation,

$x^{2}=4$

is,

$x=V(\{2::x_{1},-2::x_{2}\})$

### Possible worlds

A possible world is used here as an informal term. Formally a possible world is defined by a Boolean condition. A possible world may be considered the set of possibilities for the world that match the condition.

The term "possible world" is used to make the description of value sets easier to follow.

### World sets

A world set is a set of possible worlds that represent all possibilities. So $\{x_{1},x_{2}\}$ is a world set as either x = 2 (in world $x_{1}$ ) or x= −2 (in world $x_{2}$ ). There are no other possibilities.

Worlds from the same world set are mutually exclusive, so it is not possible that the propositions for both worlds $x_{1}$ and $x_{2}$ are true at the same time.

$(x=2\land x=-2)={\text{false}}$

### Application of functions

The rule for the application of functions to value sets is,

$V(M)\ V(N)=V(\{(m_{v}\ n_{v},m_{l}\cap n_{l}):m_{v}::m_{l}\in M\land n_{v}::n_{l}\in N\})$

For example,

$x+x=V(\{2::x_{1},-2::x_{2}\})+V(\{2::x_{1},-2::x_{2}\})$

is,

$=V(\{-2+-2::x_{1}\cap x_{1},-2+2::x_{1}\cap x_{2},2+-2::x_{1}\cap x_{2},2+2::x_{2}\})$

$=V(\{-4::x_{1}\cap x_{1},0::x_{1}\cap x_{2},0::x_{2}\land x_{1},2+2::x_{2}\cap x_{1}\})$

The intersection of the possible world with itself is the possible world,

$x_{1}\cap x_{1}=x_{1}$

$x_{2}\cap x_{2}=x_{2}$

The intersection of the possible world with another possible world from the same world set is empty,

$x_{1}\cap x_{2}=\{\}$

$x_{2}\cap x_{1}=\{\}$

So,

$=V(\{-4::x_{1},0::\{\},0::\{\},4::x_{2}\})$

The empty worlds rule allows tagged values from empty worlds to be dropped

$V(K)=V(\{(v,l):(v,l)\in K\land l\neq \{\}\}$

giving,

$=V(\{-4::x_{1},4::x_{2}\})$

Giving the result that $x+x$ is either −4 or 4, as expected.

### Application to Booleans

$a\land b$

Is a relationship between *a*, *b* and *true* that implies that both *a* and *b* must be true.

$a\lor b$

Allows multiple values for *a* and *b*. If *a* is,

$a=V(\{\operatorname {false} ::a_{1},\operatorname {true} ::a_{2}\})$

then for *b*

$b=V(\{\operatorname {true} ::a_{1},\operatorname {false} ::a_{2},\operatorname {true} ::a_{2}\})$

This means that if *a* is *false* then *b* must be *true*.

Now consider,

$x=2\lor x=-2$

gives,

$x=V(\{\_::a_{1},2::a_{2}\})$

and

$x=V(\{-2::a_{1},\_::a_{2},-2::a_{2}\})$

unifying these two value sets gives,

$x=V(\{-2::a_{1},2::a_{2}\})$

The pair $-2::a_{2}$ is dropped because of the "assert equal" rule,

$\forall m_{v}\forall m_{l}\forall n_{v}\forall n_{l}((m_{v},m_{l})\in M\land (n_{v},n_{l})\in N)\to (m_{v}\neq n_{v}\to m_{l}\cap n_{l}=\{\})$

Its value $-2::a_{2}$ did not match with $2::a_{2}$ .

### Dependent worlds

Consider the problem,

$X=V(\{1::x_{1},3::x_{2},4::x_{3}\})$

$Y=V(\{8::y_{1},9::y_{2}\})$

$X*Y<25$

$X+Y>10$

Firstly calculate the value set for $X*Y<25$ ,

$V(\{8::x_{1}\cap y_{1},24::x_{2}\cap y_{1},32::x_{3}\cap y_{1},9::x_{1}\cap y_{2},27::x_{2}\cap y_{2},36::x_{3}\cap y_{2}\})<25$

$V(\{8<25::x_{1}\cap y_{1},24<25::x_{2}\cap y_{1},32<25::x_{3}\cap y_{1},9<25::x_{1}\cap y_{2},27<25::x_{2}\cap y_{2},36<25::x_{3}\cap y_{2}\})<25$

$V(\{{\text{true}}::x_{1}\cap y_{1},{\text{true}}::x_{2}\cap y_{1},{\text{false}}::x_{3}\cap y_{1},{\text{true}}::x_{1}\cap y_{2},{\text{false}}::x_{2}\cap y_{2},{\text{false}}::x_{3}\cap y_{2}\})$

As this statement is asserted true, all the false values are dropped giving,

$V(\{{\text{true}}::x_{1}\cap y_{1},{\text{true}}::x_{2}\cap y_{2},{\text{true}}::x_{1}\cap y_{2}\})$

The worlds,

$x_{3}\cap y_{1}$

$x_{2}\cap y_{2}$

$x_{3}\cap y_{2}$

are impossible. The worlds are empty.

If a world set is included in a calculation then every world from the world set must be included in the result. If a world is not found, it is called a dependent world, and must be empty. The world $X_{3}$ is not represented in this value, and so must be empty. The value set for X is now smaller,

$X=V(\{1::x_{1},3::x_{2}\})$

The second condition is now simpler, because of the smaller value set.

$X+Y>10$

Then the value sets are,

$X=V(\{1::x_{1},3::x_{2}\})$

$Y=V(\{8::y_{1},9::y_{2}\})$

And the calculation is,

$V(\{1+8::x_{1}\cap y_{1},3+8::x_{2}\cap y_{1},2+9::x_{1}\cap y_{2},1+9::x_{2}\cap y_{2}\})>10$

But $x_{2}\cap y_{2}$ is empty. So,

$V(\{9>10::x_{1}\cap y_{1},11>10::x_{2}\cap y_{1},10>10::x_{1}\cap y_{2}\})$

So $x_{1}\cap y_{1}$ and $x_{1}\cap y_{2}$ are empty,

$V(\{11>10::x_{2}\cap y_{1}\})$

Now $X_{1}$ and $Y_{2}$ are not represented, and are removed as dependent worlds. So,

$X=V(\{3::x_{2}\})=3$

$Y=V(\{8::y_{1}\})=8$

Every calculation made may reduce the size of value sets by removing dependent worlds, but add a new value set whose size is the product of the sizes of the input value sets. Then calculations should proceed first where the product of the sizes of the input value sets is smallest.

### Pizza, beer, whiskey

After a hard day's work attempting to meet some crazy deadline with the project from hell, there comes that desperate time at 10 PM when we all need pizza, beer, and whiskey. Pizza shops are open at,

${\text{PizzaShop}}(V(\{{\text{Carlton}}::p_{1},{\text{Richmond}}::p_{2},{\text{South Melbourne}}::p_{3},{\text{Footscray}}::p_{4},{\text{St Kilda}}::p_{5},{\text{Toorak}}::p_{6}\}))$

Beer you can get at,

${\text{BottleshopWithBeer}}(V(\{{\text{South Melbourne}}::b_{1},{\text{St Kilda}}::b_{2},{\text{Carlton}}::b_{3},{\text{Docklands}}::b_{4}\}))$

Whiskey,

${\text{BottleshopWithWhiskey}}(V(\{{\text{Essendon}}::w_{1},{\text{South Melbourne}}::w_{2}\}))$

The cops are about and we are not getting any younger. Where to go?

${\text{WhereToGo}}(x)={\text{PizzaShop}}(x)\land {\text{BottleshopWithBeer}}(x)\land {\text{BottleshopWithWhiskey}}(x)$

**If the constraints are applied in the order left to right**,

$x=V(\{{\text{Carlton}}::p_{1},{\text{Richmond}}::p_{2},{\text{South Melbourne}}::p_{3},{\text{Footscray}}::p_{4},{\text{St Kilda}}::p_{5},{\text{Toorak}}::p_{6}\})$

Then we need to unify this with,

$x=V(\{{\text{South Melbourne}}::b_{1},{\text{St Kilda}}::b_{2},{\text{Carlton}}::b_{3},{\text{Docklands}}::b_{4}\})$

This will create 24 combinations from which the matching ones are,

$x=V(\{{\text{South Melbourne}}::b_{1}\cap p_{3},{\text{St Kilda}}::b_{2}\cap p_{5},{\text{Carlton}}::b_{3}\cap p_{1}\})$

Finally we need to unify with whiskey.

$x=V(\{{\text{Essendon}}::w_{1},{\text{South Melbourne}}::w_{2}\})$

Which gives 6 combinations. The matching one is,

$x=V(\{{\text{South Melbourne}}::b_{1}\cap p_{3}\cap w_{2}\})$

A total of 30 combinations were generated.

**If the constraints are applied in the order right to left**,

$x=V(\{{\text{Essendon}}::w_{1},{\text{South Melbourne}}::w_{2}\})$

Then we need to unify this with,

$x=V(\{{\text{South Melbourne}}::b_{1},{\text{St Kilda}}::b_{2},{\text{Carlton}}::b_{3},{\text{Docklands}}::b_{4}\})$

This will create 8 combinations from which the matching one is,

$x=V(\{{\text{South Melbourne}}::b_{1}\cap w_{2}\})$

Finally we need to unify with pizza.

$x=\{{\text{Carlton}}::p_{1},{\text{Richmond}}::p_{2},{\text{South Melbourne}}::p_{3},{\text{Footscray}}::p_{4},{\text{St Kilda}}::p_{5},{\text{Toorak}}::p_{6}\}$

Which gives 6 combinations. The matching one is,

$x=V(\{{\text{South Melbourne}}::b_{1}\cap w_{2}\ \cap p_{3}\})$

The result is the same but only 14 combinations were generated to arrive at the conclusion.

Every calculation combines value sets to create a value set which is the product of the sizes of the input value sets. The value set will then be trimmed down. And every calculation has an equal chance of narrowing the calculation. So by controlling the order and proceeding with calculations with the smallest product of sizes, there will be less calculation and less combinatorial explosion.

## Let expressions and multiple values

A general solution to the problem of inverses of functions that are not functions is needed. What is required is a representation of a value that is constrained to be a member of a set of values. A let expression may be used to represent a value that is a member of a set,

$\operatorname {let} x\in X\operatorname {in} x$

In this expression $x\in X$ is a constraint. A constraint is a Boolean expression that a variable must satisfy. The *let* expression allows the constraint be represented in an expression. If there was a general rule for function application of constraint expressions, then a constraint could be treated like a value.

Under function application, of one let expression to another,

$(\operatorname {let} x\in X\operatorname {in} x)\ (\operatorname {let} y\in Y\operatorname {in} y)$

$=\operatorname {let} x\in X\land y\in Y\operatorname {in} x\ y$

$=\operatorname {let} (x,y)\in X\times Y\operatorname {in} x\ y$

But a different rule applies for applying the let expression to itself. The let expression does not restrict the scope of the variable x, so x is the same variable in the two let expressions.

$(\operatorname {let} x\in X\operatorname {in} x)\ (\operatorname {let} x\in X\operatorname {in} x)$

$=\operatorname {let} x\in X\operatorname {in} x\ x$

There appears no simple rule for combining let expressions. What is required is a general form of expression that represents a variable whose value is a member of a set of values. The expression should be based on the variable and the set.

Function application applied to this form should give another expression in the same form. In this way any expression on functions of multiple values may be treated as if it had one value.

It is not sufficient for the form to represent only the set of values. Each value must have a condition that determines when the expression takes the value. The resulting construct is a set of pairs of conditions and values, called a "value set".

## Theory of value sets

A "value set" *K* is defined as a set of pairs, each pair consisting of a value and a set of dependent conditions. The set of dependent conditions is used by the "condition function", to determine if the value set takes that value.

The condition function is defined by 3 axioms,

1. Each pair $(v,l)$ means that the value of the value set $V(K)$ is *v* if the condition function applied to the list, $C(l)$ , is true.
2. One of the conditions is true.
3. Only one of the conditions is true.

The condition is represented as a function applied to a set of dependent conditions, to allow the structure of the condition to be controlled. Also the set of conditions is used in narrowing by exclusion of dependent values. However for most purposes the value set may be thought of as a set of value, condition pairs. The condition function translates the set into the condition.

Formally,

| Name | Definition |
|---|---|
| Condition function | $C(l)=({\bigwedge _{(r,z,u)\in l}z=u}))=(\forall r\forall z\forall u(r,z,u)\in l\to z=u)$ |
| Value condition | $\forall v\forall l((v,l)\in K\land C(l)\to v=V(K)$ |
| Complete set | $\exists v\exists l(v,l)\in K\land C(l)$ |
| Exclusion | $\forall v_{1}\forall l_{1}\forall v_{2}\forall l_{2}((v_{1},l_{1})\in K\land (v_{2},l_{2})\in K\land (v_{1},l_{1})\neq (v_{2},l_{2}))\to \neg (C(l_{1})\land C(l_{2}))$ |

### Value function

Using the value condition and complete set axioms,

$\exists v\exists l(v,l)\in K\land C(l)\land v=V(K)$

As a let expression this becomes,

$V(K)=\operatorname {let} (v,l)\in K\land C(l)\operatorname {in} v$

### Single value

The value set to represent a single value is,

$k=V(\{(k,\{\})\})$

The derivation is,

$V(\{(k,\{\})\})$

$=\operatorname {let} (v,l)\in \{(k,\{\})\}\land C(l)\operatorname {in} v$

$=\operatorname {let} v=k\land C(\{\})\operatorname {in} v$

$=\operatorname {let} v=k\operatorname {in} v$

$=k$

### Element of a set

The value set to represent an element of a set is,

$\forall x\forall X(\operatorname {let} x\in X\operatorname {in} x)=\operatorname {let} R=V(\{(w,\{(R,x,w)\}):w\in X\})\operatorname {in} R$

This rather strange definition adds the value set in as part of the dependent condition. This is used in narrowing by exclusion of dependent values.

The value of the expression is

$x=V(R)$

.

Both *R* and *x* must be included in the dependent condition, because *R* identifies the value set to which the dependent condition belongs, and *x* provides the variable used to carry the value in the let expression.

If the addition of *R* to the dependent condition is ignored, the expression takes on a simpler and more understandable form,

$\forall x\forall X(\operatorname {let} x\in X\operatorname {in} x)=V(\{(w,\{(\_,x,w)\}):w\in X\})$

The derivation is,

$V(\{(w,\{(r,x,w):w\in X\})$

$=\operatorname {let} (v,l)\in \{(w,\{(r,x,w)\}):w\in X\}\land C(l)\operatorname {in} v$

$=\operatorname {let} v\in X\land ({\bigwedge _{(r,z,u)\in \{(\_,x,v)\}}z=u})\operatorname {in} v$

$=\operatorname {let} v\in X\land (\forall r\forall z\forall u(r,z,u)\in \{(\_,x,v)\}\to z=u)\operatorname {in} v$

$=\operatorname {let} v\in X\land x=v\operatorname {in} v$

$=\operatorname {let} x\in X\operatorname {in} x$

### Application of functions

Function application of value sets is given by,

$V(M)\ V(N)=V(\{(m_{v}\ n_{v},m_{l}\cup n_{l}):(m_{v},m_{l})\in M\land (n_{v},n_{l})\in N\})$

Derivation,

$V(M)\ V(N)$

$=\operatorname {let} (m_{v},m_{l})\in M\land C(m_{l})\operatorname {in} m_{v})\ (\operatorname {let} (n_{v},n_{l})\in N\land C(n_{l})\operatorname {in} n_{v})$

$=\operatorname {let} (m_{v},m_{l})\in M\land (n_{v},n_{l})\in N\land C(n_{l})\land C(n_{l})\operatorname {in} m_{v}\ n_{v})$

Then using,

$C(m_{l})\land C(n_{l})$

$=({\bigwedge _{(z,u)\in m_{l}}z=u})\land ({\bigwedge _{(z,u)\in n_{l}}z=u})$

$=({\bigwedge _{(z,u)\in m_{l}\cup n_{l}}z=u})$

$=C(m_{l}\cup n_{l})$

get,

$=\operatorname {let} (m_{v},m_{l})\in M\land (n_{v},n_{l})\in N\land C(n_{l}\cup n_{l})\operatorname {in} m_{v}\ n_{v})$

$=\operatorname {let} (v,l)\in \{(m_{v}\ n_{v},m_{l}\cup n_{l}):(m_{v},m_{l})\in M\land (n_{v},n_{l})\in N\}\land C(l)\operatorname {in} v$

$=V(\{(m_{v}\ n_{v},m_{l}\cup n_{l}):(m_{v},m_{l})\in M\land (n_{v},n_{l})\in N\})$

### Exclusion

The exclusion is a rule that determines when conditions must be false,

$V(M)\in s\iff (\forall v\forall l((v,l)\in M\land v\not \in s)\to \neg C(l))$

This may be derived from,

$V(M)\in s$

$\to \forall v\forall l((v,l)\in M\land C(l))\to (v=V[M]\land V(M)\in s)$

$\to \forall v\forall l((v,l)\in M\land C(l))\to v\in S$

$\to \forall v\forall l((v,l)\in M\land v\not \in S)\to \neg C(l)$

### Simplification

The simplification rule allows values whose condition is false to be dropped.

$V(K)=V(\{(v,l):(v,l)\in K\land C(l)\}$

Derivation

$V(\{(v,l):(v,l)\in K\land C(l)\})$

$=\operatorname {let} (v,l)\in \{(v,l):(v,l)\in K\land C(l)\}\land C(l)\operatorname {in} v$

$=\operatorname {let} (v,l)\in K\land C(l)\land C(l)\operatorname {in} v$

$=\operatorname {let} (v,l)\in K\land C(l)\operatorname {in} v$

$=V(K)$

### Summary of results

| Name | Rule |
|---|---|
| Value function | $V(K)=\operatorname {let} (v,l)\in K\land C(l)\operatorname {in} v$ |
| Single value | $k=V(\{(k,\{\})\})$ |
| Set element | $\forall x\forall X(\operatorname {let} x\in X\operatorname {in} x)=\operatorname {let} R=V(\{(w,\{(R,x,w)\}):w\in X\})\operatorname {in} R$ |
| Function application | $V(M)\ V(N)=V(\{(m_{v}\ n_{v},m_{l}\cup n_{l}):(m_{v},m_{l})\in M\land (n_{v},n_{l})\in N\})$ |
| Exclusion | $V(M)\in s\iff (\forall v\forall l((v,l)\in M\land v\not \in s)\to \neg C(l))$ |
| Simplification | $V(K)=V(\{(v,l):(v,l)\in K\land C(l)\})$ |
| Assert equal | $V(M)=V(N)\to (\forall v\forall l((v,l)\in N\land v\not \in S(M))\to \neg C(l))$ |

## A value sets identity

By defining the application of functions to value sets the definition of equality of value sets has also been redefined. The old definition of equality still exists, because value sets are constructed as a set of pairs. Two sets are equal if they contain the same elements. This definition of equality for value sets is at best misleading.

What is needed is to use the name, or identity of the variable from which the value set is constructed as part of the structure of the value set. This would make value sets distinct, unless they are based on the same variable.

In mathematics, quantification is over values, not formulas. To proceed further with the exact definition of value sets, quantification over formulas is needed, in a way that allows the comparison of the identity of formulas. The distinction between the formula representing a value and the identity of the formula is the use–mention distinction. The notation,

$\forall x\#u$

is introduced to mean quantification over formula *x* where *x* refers to the value, as a use, and *u* refers to the identity of the formula as represented or mentioned.

Using this notation the element of a set definition would be,

$\forall x\#u\forall X(\operatorname {let} x\in X\operatorname {in} x)=\operatorname {let} R=V((u,\{(w,\{(R,x,w)\}):w\in X\}))\operatorname {in} R$

Every reference to a value set would then need to be changed to take account of the extra level of structure in the value set, which would make the description harder to read. For the sake of readability this extra level of structure has been omitted from the definition of value sets.

## Narrowing

"Narrowing" is determining when conditions for values must be *false*. Narrowing starts when the value of two value sets is asserted equal.

### Narrowing by asserting equal

Assertion that two value sets are equal gives the narrowing rule,

$\forall m_{v}\forall m_{l}\forall n_{v}\forall n_{l}((m_{v},m_{l})\in M\land (n_{v},n_{l})\in N)\to (m_{v}\neq n_{v}\to \neg (C(m_{l})\land C(n_{l})))$

For the derivation, start with,

$V(M)=V(N)$

The value condition gives,

$(\forall m_{v}\forall m_{l}((m_{v},m_{l})\in M\land C(m_{l})\to v=V(M))\land (\forall n_{v}\forall n_{l}((n_{v},k)\in N\land C(n_{l}))\to n_{v}=V(N))\land V(M)=V(N)$

$\forall m_{v}\forall m_{l}\forall n_{v}\forall n_{l}(((m_{v},m_{l})\in M\land C(m_{l}))\to m_{v}=V(M))\land (((n_{v},n_{l})\in N\land C(n_{l}))\to n_{v}=V(N))\land V(M)=V(N)$

$\forall m_{v}\forall m_{l}\forall n_{v}\forall n_{l}((m_{v},m_{l})\in M\land (n_{v},n_{l})\in N)\to (C(j)\land C(k)\to v=u)$

$\forall m_{v}\forall m_{l}\forall n_{v}\forall n_{l}((m_{v},m_{l})\in M\land (n_{v},n_{l})\in N)\to (m_{v}\neq n_{v}\to \neg (C(m_{l})\land C(n_{l})))$

### Narrowing by conjunction

If any base condition is false, all the conditions obtained from it are false.

This comes from the definition of the Condition function,

$C(l)=({\bigwedge _{(r,z,u)\in l}z=u}))$

The base condition for (r, z, u) is,

$C(\{(r,z,u)\}=(z=u)$

So if this is false $C(l)$ is false.

### Narrowing by crossed conditions

If a dependent condition list has two different base conditions from the same value set it must be false.

To derive this, start with the exclusion rule which is,

$\forall v_{1}\forall l_{1}\forall v_{2}\forall l_{2}((v_{1},l_{1})\in K\land (v_{2},l_{2})\in K\land (v_{1},l_{1})\neq (v_{2},l_{2}))\implies \neg (C(l_{1})\land C(l_{2}))$

Then for any set of dependent conditions *l*,

$((K,x,v_{1})\in l\ \land (K,x,v_{2})\in l\land v_{1}\neq v_{2}$

$\implies (v_{1},\{(K,x,v_{1})\})\in K\land (v_{2},\{(K,x,v_{2})\})\in K\land (v_{1},l_{1})\neq (v_{2},l_{2}))$

$\implies \neg (C(\{(K,x,v_{1})\})\land C(\{(K,x,v_{2})\}))$

$\implies \neg C(l)$

So if a dependent condition list is based on two conditions from the same value set, the condition value of that dependent condition list is false.

### Narrowing by exclusion of dependent values

Each value set puts a constraint on the base value set from which it is constructed. If a base values set includes values that are not present as dependent values in the value set, the conditions for these values must be false.

To derive this, start with the complete set rule,

$\exists v\exists \ l(v,l)\in K\to C(l)$

The condition function is,

$C(l)=({\bigwedge _{(r,z,u)\in l}z=u}))$

A particular dependent condition may be chosen, as being implied by the whole condition,

$\forall L\ C(l)\to (L,z,u)\in l\to z=u$

So

$\forall L\exists v\exists l\ (v,l)\in K\to C(l)\to (L,z,u)\in l\to z=u$

Here $z=V(L)$ . The expression may be rearranged to define the set of values that $V(L)$ might take,

$E(K,L)=\{w:(v,l)\in K\land C(l)\land (L,z,w)\in l\}$

and so,

$V(L)\in E(K,L)$

Then using the exclusion rule,

$V(M)\in s\iff (\forall v\forall l((v,l)\in M\land v\not \in s)\to \neg C(l))$

gives,

$(\forall K\forall L\forall v\forall l((v,l)\in L\land v\not \in E(K,L))\to \neg C(l))$

This is the narrowing exclusion rule. $E(K,L)$ is the set of values in the base value *L* set which are represented in the value set *K*. Conditions for other values must be false.

## Probabilistic value sets

The value set records the dependent conditions that the condition function may be applied to in order to deduce the truth of the proposition that the value set has a particular value. The same structure may be used to give the probability of a value set being equal to a particular value. The condition function is,

$C(l)=({\bigwedge _{(r,z,u)\in l}z=u}))$

The probability function is,

$P(l)=({\prod _{(r,z,u)\in l}P(z=u)}))$

This is the probability of each base case holding the particular value, if the events are independent.

The probability function is defined by 3 axioms,

1. Each pair $(v,l)$ means that the probability of the value set $V(K)$ is *v* is the probability function applied to the list, $P(l)$ .
2. The sum of the probabilities over the whole value set is 1.
3. The probability of any two pairs in the value set is zero.

The probability function gives probabilities for results based on initial probabilities given by Boolean inductive inference.

Formally,

| Name | Definition |
|---|---|
| Probability function | $P(l)=({\prod _{(r,z,u)\in l}P(z=u)}))$ |
| Value condition | $\forall vP(v=V(K))=\sum _{(v,l)\in K}P(l)$ |
| Complete set | $\sum _{(v,l)\in K}P(l)=1$ |
| Allowed values | $\sum _{(v,l)\in K\land v\in \operatorname {gset} (V(K))}P(l)=1$ |
| Exclusion | $\forall v_{1}\forall l_{1}\forall v_{2}\forall l_{2}((v_{1},l_{1})\in K\land (v_{2},l_{2})\in K\land (v_{1},l_{1})\neq (v_{2},l_{2}))\to P(C(l_{1})\land C(l_{2}))=0$ |

Probabilities for each value in a value set may be calculated from probabilities in base value sets using the probability function and the value condition. Base value sets are either for a single value, or multiple value value set.

### Probability for a single value

The value set to represent a single value is,

$k=V(\{(k,\{\})\})$

The complete set rule is,

$\sum _{(v,l)\in K}P(l)$

$=\sum _{(v,l)\in \{(k,\{\})\}}P(l)$

$=P(\{\})$

$=1$

Which is consistent with the axiom.

### Probabilities for multiple values

The value set to represent multiple values is,

$\forall x\forall X(\operatorname {let} x\in X\operatorname {in} x)=V(\{(w,\{(\_,x,w)\}):w\in X\})$

The probability is given by the allowed values rule,

$\sum _{(v,l)\in K\land v\in \operatorname {gset} (V(K))}P(l)=1$

which simplifies to,

$\sum _{v\in \operatorname {gset} (V(K))}P(x=v)=1$

If prior estimates of probabilities for values are given then they will be proportional to the posterior probabilities, if the value is in the value set.

$\forall v\in \operatorname {gset} (V(K)),P(x=v)=w*P_{i}(x=v)$

If the value is not in the value set the probabilities will be zero,

$\forall v\not \in \operatorname {gset} (V(K)),P(x=v)=0$

So,

$\sum _{v\in \operatorname {gset} (V(K))}w*P_{i}(x=v)=1$

$w={\frac {1}{\sum _{v\in \operatorname {gset} (V(K))}P_{i}(x=v)}}$

$\forall v\in \operatorname {gset} (V(K)),P(x=v)={\frac {P_{i}(x=v)}{\sum _{v\in \operatorname {gset} (V(K))}P_{i}(x=v)}}$

$\forall v\not \in \operatorname {gset} (V(K)),P(x=v)=0$

If the prior probabilities are all the same the probabilities are,

$\forall v\in \operatorname {gset} (V(K)),P(x=v)={\frac {1}{|\operatorname {gset} (V(K))|}}$

### Probabilities of general value sets

A general value set is created out of the application of base value sets. The value condition rule and the probability function may be combined to give,

$\forall vP(v=V(K))=\sum _{(v,l)\in K\land v\in \operatorname {gset} (V(K))}({\prod _{(r,z,u)\in l}P(z=u)}))$

## Accessing the value set

Narrowing allows the elimination of values that do not satisfy a variable's constraints. Considered as the basis for an algorithm for solving equations, this narrowing gives a set of values consistent with the constraints on a variable. However in mathematics there is no way to access this set of values.

If $E(x)$ is an expression constraining a variable *x* then the set of values that the variable may take is,

$\{z:E(z)\}$

Define the *gset* of *x* to be the set of values that satisfy the constraints on *x*. Consider defining *gset* as,

$\operatorname {gset} (x)=\{z:E(z)\}$

This definition depends on knowing the expression *E*, which is the condition giving all the constraints on *x*. Within mathematics *E* may not be obtained from *x*. So there is no mathematical function that may be applied to a variable to request the set of values. So may the *gset* function be added to mathematics?

### Meta math definition

A meta-mathematical definition of *gset* may be possible. Imagine that what we know of as mathematics is actually implemented by a meta function called *math*. *math* takes an abstract syntax tree and gives meaning to the variables and mathematical structures and adds existential quantifiers for variables not explicitly quantified.

*math* would be an expression in a meta mathematical environment with its own variables. To distinguish these meta-variables from math variables represent them by capital letters and the mathematical variables by lower case letters.

Now suppose there is an extended implementation of mathematics implemented by the *xmath* function, defined as,

$\operatorname {xmath} [E]=\forall M,\operatorname {let} T[M]=\operatorname {math} [E]\operatorname {in} T[\_]$

Using *xmath*, *gset* may be defined by,

$\forall x\#u,\exists N,\operatorname {gset} (x)=\operatorname {let} M[u]=x\operatorname {in} \{z:z=N[u]\land T[N]\}$

Here again the notation,

$\forall x\#u$

is used to mean quantification over variables *x* where *x* refers to the value, and *u* refers to the unique identity of the variable.

### Example

For example take the constraint expression $x^{2}=4$ . Then,

$x^{2}=4$

$\land s=\operatorname {gset} (x)$

$\land (\forall x\#u,\exists N\operatorname {gset} (x)=\operatorname {let} M[u]=x\operatorname {in} \{z:z=N[u]\land T[N]\})$

Then the *xmath* expression is,

$\forall M,\operatorname {let} T[M]=$

$\exists x,\exists s,(x^{2}=4$

$\land s=\operatorname {gset} (x)$

$\land (\forall x\#u,\exists N,\operatorname {gset} (x)=\operatorname {let} M[u]=x\operatorname {in} \{z:z=N[u]\land T[N]\})$

$\operatorname {in} T[\_]$

Then where u is the unique identity of the variable x, represented here as the number 1 (for the first variable used in a call to *gset*),

$M[1]=x\land s=\{z:z=N[1]\land T[N]\}$

Here $T[N]$ invokes *T* with M as N.

$s=\{z:z=N[1]\land x^{2}=4\land x=N[1]\}$

$s=\{z:z^{2}=4\}$
