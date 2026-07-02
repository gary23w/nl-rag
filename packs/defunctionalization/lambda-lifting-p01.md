---
title: "Lambda lifting (part 1/2)"
source: https://en.wikipedia.org/wiki/Lambda_lifting
domain: defunctionalization
license: CC-BY-SA-4.0
tags: defunctionalization transform, closure conversion, higher-order function, apply function
fetched: 2026-07-02
part: 1/2
---

# Lambda lifting

**Lambda lifting** is a meta-process that restructures a computer program so that functions are defined independently of each other in a global scope. An individual *lift* transforms a local function (subroutine) into a global function. It is a two step process, consisting of:

- Eliminating free variables in the function by adding parameters.
- Moving functions from a restricted scope to broader or global scope.

The term "lambda lifting" was first introduced by Thomas Johnsson around 1982 and was historically considered as a mechanism for implementing programming languages based on functional programming. It is used in conjunction with other techniques in some modern compilers.

Lambda lifting is not the same as closure conversion. It requires all call sites to be adjusted (adding extra arguments (parameters) to calls) and does not introduce a closure for the lifted lambda expression. In contrast, closure conversion does not require call sites to be adjusted but does introduce a closure for the lambda expression mapping free variables to values.

The technique may be used on individual functions, in code refactoring, to make a function usable outside the scope in which it was written. Lambda lifts may also be repeated, to transform the program. Repeated lifts may be used to convert a program written in lambda calculus into a set of recursive functions, without lambdas. This demonstrates the equivalence of programs written in lambda calculus and programs written as functions. However it does not demonstrate the soundness of lambda calculus for deduction, as the eta reduction used in lambda lifting is the step that introduces cardinality problems into the lambda calculus, because it removes the value from the variable, without first checking that there is only one value that satisfies the conditions on the variable (see Curry's paradox).

Lambda lifting is expensive on processing time for the compiler. An efficient implementation of lambda lifting is $O(n^{2})$ on processing time for the compiler.

In the untyped lambda calculus, where the basic types are functions, lifting may change the result of beta reduction of a lambda expression. The resulting functions will have the same meaning, in a mathematical sense, but are not regarded as the same function in the untyped lambda calculus. See also intensional versus extensional equality.

The reverse operation to lambda lifting is lambda dropping.

Lambda dropping may make the compilation of programs quicker for the compiler, and may also increase the efficiency of the resulting program, by reducing the number of parameters, and reducing the size of stack frames. However it makes a function harder to re-use. A dropped function is tied to its context, and can only be used in a different context if it is first lifted.


## Algorithm

The following algorithm is one way to lambda-lift an arbitrary program in a language which doesn't support closures as first-class objects:

1. Rename the functions so that each function has a unique name.
2. Replace each free variable with an additional argument to the enclosing function, and pass that argument to every use of the function.
3. Replace every local function definition that has no free variables with an identical global function.
4. Repeat steps 2 and 3 until all free variables and local functions are eliminated.

If the language has closures as first-class objects that can be passed as arguments or returned from other functions, the closure will need to be represented by a data structure that captures the bindings of the free variables.


## Example

The following OCaml program computes the sum of the integers from 1 to 100:

```mw
let rec sum n =
  if n = 1 then
    1
  else
    let f x = n + x in
    f (sum (n - 1))
sum 100
```

(The `let rec` declares `sum` as a function that may call itself.) The function f, which adds sum's argument to the sum of the numbers less than the argument, is a local function. Within the definition of f, n is a free variable. Start by converting the free variable to a parameter:

```mw
let rec sum n =
  if n = 1 then
    1
  else
    let f w x =
      w + x in
    f n (sum (n - 1))
sum 100
```

Next, lift f into a global function:

```mw
let rec f w x =
  w + x
and sum n =
  if n = 1 then
    1
  else
    f n (sum (n - 1)) in
sum 100
```

The following is the same example, this time written in JavaScript:

```mw
// Initial version

function sum(n) {
    function f(x) {
        return n + x;
    }

    if (n == 1)
        return 1;
    else
        return f(sum(n - 1));
}

// After converting the free variable n to a formal parameter w

function sum(n) {
    function f(w, x) {
        return w + x;
    }

    if (n == 1)
        return 1;
    else
        return f(n, sum(n - 1));
}

// After lifting function f into the global scope

function f(w, x) {
    return w + x;
}

function sum(n) {
    if (n == 1)
        return 1;
    else
        return f(n, sum(n - 1));
}
```


## Lambda lifting versus closures

Lambda lifting and closure are both methods for implementing block structured programs. It implements block structure by eliminating it. All functions are lifted to the global level. Closure conversion provides a "closure" which links the current frame to other frames. Closure conversion takes less compile time.

Recursive functions, and block structured programs, with or without lifting, may be implemented using a stack based implementation, which is simple and efficient. However a stack frame based implementation must be strict (eager). The stack frame based implementation requires that the life of functions be last-in, first-out (LIFO). That is, the most recent function to start its calculation must be the first to end.

Some functional languages (such as Haskell) are implemented using lazy evaluation, which delays calculation until the value is needed. The lazy implementation strategy gives flexibility to the programmer. Lazy evaluation requires delaying the call to a function until a request is made to the value calculated by the function. One implementation is to record a reference to a "frame" of data describing the calculation, in place of the value. Later when the value is required, the frame is used to calculate the value, just in time for when it is needed. The calculated value then replaces the reference.

The "frame" is similar to a stack frame, the difference being that it is not stored on the stack. Lazy evaluation requires that all the data required for the calculation be saved in the frame. If the function is "lifted", then the frame needs only record the function pointer, and the parameters to the function. Some modern languages use garbage collection in place of stack based allocation to manage the life of variables. In a managed, garbage collected environment, a closure records references to the frames from which values may be obtained. In contrast a lifted function has parameters for each value needed in the calculation.


## Let expressions and lambda calculus

The Let expression is useful in describing lifting, dropping, and the relationship between recursive equations and lambda expressions. Most functional languages have let expressions. Also, block-structured programming languages like ALGOL and Pascal are similar in that they too allow the local definition of a function for use in a restricted scope.

The *let* expression used here is a fully mutually recursive version of *let rec*, as implemented in many functional languages.

Let expressions are related to Lambda calculus. Lambda calculus has a simple syntax and semantics, and is good for describing Lambda lifting. It is convenient to describe lambda lifting as a translations from *lambda* to a *let* expression, and lambda dropping as the reverse. This is because *let* expressions allow mutual recursion, which is, in a sense, more lifted than is supported in lambda calculus. Lambda calculus does not support mutual recursion and only one function may be defined at the outermost global scope.

Conversion rules which describe translation without lifting are given in the Let expression article.

The following rules describe the equivalence of lambda and let expressions,

| Name | Law |
|---|---|
| Eta-reduction equivalence | $f\ x=y\equiv f=\lambda x.y$ |
| Let-Lambda equivalence | $f\notin FV(E)\to (\operatorname {let} f:f=E\operatorname {in} L\equiv (\lambda f.L)\ E)\ {\text{(where }}f{\text{ is a variable name.)}}$ |
| Let combination | $x\notin FV(E)\to (\operatorname {let} v,\dots ,w,x:E\land F\operatorname {in} L\equiv \operatorname {let} v,\dots ,w:E\operatorname {in} \operatorname {let} x:F\operatorname {in} L)$ |

Meta-functions will be given that describe lambda lifting and dropping. A meta-function is a function that takes a program as a parameter. The program is data for the meta-program. The program and the meta program are at different meta-levels.

The following conventions will be used to distinguish program from the meta program,

- Square brackets [] will be used to represent function application in the meta program.
- Capital letters will be used for variables in the meta program. Lower case letters represent variables in the program.
- $\equiv$ will be used for equals in the meta program.
- $\_$ represents a dummy variable, or an unknown value.

For simplicity the first rule given that matches will be applied. The rules also assume that the lambda expressions have been pre-processed so that each lambda abstraction has a unique name.

The substitution operator is used extensively. The expression $L[G:=S]$ means substitute every occurrence of *G* in *L* by *S* and return the expression. The definition used is extended to cover the substitution of expressions, from the definition given on the Lambda calculus page. The matching of expressions should compare expressions for alpha equivalence (renaming of variables).


## Lambda lifting in lambda calculus

Each lambda lift takes a lambda abstraction which is a sub expression of a lambda expression and replaces it by a function call (application) to a function that it creates. The free variables in the sub expression are the parameters to the function call.

Lambda lifts may be used on individual functions, in code refactoring, to make a function usable outside the scope in which it was written. Such lifts may also be repeated, until the expression has no lambda abstractions, to transform the program.

### Lambda lift

A lift is given a sub-expression within an expression to lift to the top of that expression. The expression may be part of a larger program. This allows control of where the sub-expression is lifted to. The lambda lift operation used to perform a lift within a program is,

$\operatorname {lambda-lift-op} [S,L,P]=P[L:=\operatorname {lambda-lift} [S,L]]$

The sub expression may be either a lambda abstraction, or a lambda abstraction applied to a parameter.

Two types of lift are possible.

- Anonymous lift
- Named lift

An anonymous lift has a lift expression which is a lambda abstraction only. It is regarded as defining an anonymous function. A name must be created for the function.

A named lift expression has a lambda abstraction applied to an expression. This lift is regarded as a named definition of a function.

#### Anonymous lift

An anonymous lift takes a lambda abstraction (called *S*). For *S*;

- Create a name for the function that will replace *S* (called *V*). Make sure that the name identified by *V* has not been used.
- Add parameters to *V*, for all the free variables in *S*, to create an expression *G* (see *make-call*).

The lambda lift is the substitution of the lambda abstraction *S* for a function application, along with the addition of a definition for the function.

$\operatorname {lambda-lift} [S,L]\equiv \operatorname {let} V:\operatorname {de-lambda} [G=S]\operatorname {in} L[S:=G]$

The new lambda expression has *S* substituted for G: *L*[*S*:=*G*] means substitution of *S* for *G* in *L*. The function definitions has the function definition *G = S* added.

In the above rule *G* is the function application that is substituted for the expression *S*. It is defined by,

$G=\operatorname {make-call} [V,\operatorname {FV} [S]]$

where *V* is the function name. It must be a new variable, i.e. a name not already used in the lambda expression,

$V\not \in \operatorname {vars} [\operatorname {let} F\operatorname {in} L]$

where $\operatorname {vars} [E]$ is a meta function that returns the set of variables used in *E*.

| Example for anonymous lift. |
|---|
| For example, ${\begin{aligned}F&=\operatorname {true} \\L&=\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))\\S&=\lambda x.f\ (x\ x)\\G&=p\ f\end{aligned}}$ $\operatorname {de-lambda} [p\ f=\lambda x.f\ (x\ x)]\equiv p\ f\ x=f\ (x\ x)$ See *de-lambda* in Conversion from lambda to let expressions. The result is, $\operatorname {lambda-lift} [\lambda x.f\ (x\ x),\operatorname {let} \operatorname {true} \operatorname {in} \lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))]\equiv \operatorname {let} p\ f\ x=f\ (x\ x)\operatorname {in} \lambda f.(p\ f)\ (p\ f)$ |

##### Constructing the call

The function call *G* is constructed by adding parameters for each variable in the free variable set (represented by *V*), to the function *H*,

- $X\in V\to \operatorname {make-call} [H,V]\equiv \operatorname {make-call} [H,V\cap \neg \{X\}]\ X$
- $\operatorname {make-call} [H,\{\}]\equiv H$

| Example of call construction. |
|---|
| $S=\lambda x.f\ (x\ x)$ $\operatorname {FV} (S)=\{f\}$ $G\equiv \operatorname {make-call} [p,\operatorname {FV} [S]]\equiv \operatorname {make-call} [p,\{f\}]\equiv \operatorname {make-call} [p,\{\}]\ f\equiv p\ f$ |

#### Named lift

The named lift is similar to the anonymous lift except that the function name *V* is provided.

$\operatorname {lambda-lift} [(\lambda V.E)\ S,L]\equiv \operatorname {let} V:\operatorname {de-lambda} [G=S]\operatorname {in} L[(\lambda V.E)\ S:=E[V:=G]]$

As for the anonymous lift, the expression *G* is constructed from *V* by applying the free variables of *S*. It is defined by,

$G=\operatorname {make-call} [V,\operatorname {FV} [S]]$

| Example for named lift. |
|---|
| For example, ${\begin{aligned}V&=x\\E&=f\ (x\ x)\\S&=(\lambda x.f\ (x\ x))\\L&=\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))\\G&=x\ f\end{aligned}}$ $E[V:=G]=f\ (x\ x)[x:=x\ f]=f\ ((x\ f)\ (x\ f))$ $L[(\lambda V.E)\ F:=E[V:=G]]=L[(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x)):=f\ ((x\ f)\ (x\ f))]=\lambda f.f\ ((x\ f)\ (x\ f))$ $\operatorname {de-lambda} [x\ f=\lambda y.f\ (y\ y)]\equiv x\ f\ y=f\ (y\ y)$ See *de-lambda* in Conversion from lambda to let expressions. The result is, gives, $\operatorname {lambda-lift} [(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x)),\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))]\equiv \operatorname {let} x\ f\ y=f\ (y\ y)\operatorname {in} \lambda f.(x\ f)\ (x\ f)$ |

### Lambda-lift transformation

A lambda lift transformation takes a lambda expression and lifts all lambda abstractions to the top of the expression. The abstractions are then translated into recursive functions, which eliminates the lambda abstractions. The result is a functional program in the form,

- $\operatorname {let} M\operatorname {in} N$

where *M* is a series of function definitions, and *N* is the expression representing the value returned.

For example,

$\operatorname {lambda-lift-tran} [\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))]\equiv \operatorname {let} p\ f\ x=f\ (x\ x)\land q\ p\ f=(p\ f)\ (p\ f)\operatorname {in} q\ p$

The *de-let* meta function may then be used to convert the result back into lambda calculus.

$\operatorname {de-let} [\operatorname {lambda-lift-tran} [\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))]]\equiv (\lambda p.(\lambda q.q\ p)\ \lambda p.\lambda f.(p\ f)\ (p\ f))\ \lambda f.\lambda x.f\ (x\ x)$

The processing of transforming the lambda expression is a series of lifts. Each lift has,

- A sub expression chosen for it by the function *lift-choice*. The sub expression should be chosen so that it may be converted into an equation with no lambdas.
- The lift is performed by a call to the *lambda-lift* meta function, described in the next section,

${\begin{cases}\operatorname {lambda-lift-tran} [L]=\operatorname {drop-params-tran} [\operatorname {merge-let} [\operatorname {lambda-apply} [L]]]\\\operatorname {lambda-apply} [L]=\operatorname {lambda-process} [\operatorname {lift-choice} [L],L]\\\operatorname {lambda-process} [\operatorname {none} ,L]=L\\\operatorname {lambda-process} [S,L]=\operatorname {lambda-apply} [\operatorname {lambda-lift} [S,L]]\end{cases}}$

After the lifts are applied the lets are combined together into a single let.

${\begin{cases}\operatorname {merge-let} [\operatorname {let} V:E\operatorname {in} \operatorname {let} W:F\operatorname {in} G]=\operatorname {merge-let} [\operatorname {let} V,W:E\land F\operatorname {in} G]\\\operatorname {merge-let} [E]=E\end{cases}}$

Then Parameter dropping is applied to remove parameters that are not necessary in the "let" expression. The let expression allows the function definitions to refer to each other directly, whereas lambda abstractions are strictly hierarchical, and a function may not directly refer to itself.

#### Choosing the expression for lifting

There are two different ways that an expression may be selected for lifting. The first treats all lambda abstractions as defining anonymous functions. The second, treats lambda abstractions which are applied to a parameter as defining a function. Lambda abstractions applied to a parameter have a dual interpretation as either a let expression defining a function, or as defining an anonymous function. Both interpretations are valid.

These two predicates are needed for both definitions.

*lambda-free* - An expression containing no lambda abstractions.

${\begin{cases}\operatorname {lambda-free} [\lambda F.X]=\operatorname {false} \\\operatorname {lambda-free} [V]=\operatorname {true} \\\operatorname {lambda-free} [M\ N]=\operatorname {lambda-free} [M]\land \operatorname {lambda-free} [N]\end{cases}}$

*lambda-anon* - An anonymous function. An expression like $\lambda x_{1}.\ ...\ \lambda x_{n}.X$ where X is lambda free.

${\begin{cases}\operatorname {lambda-anon} [\lambda F.X]=\operatorname {lambda-free} [X]\lor \operatorname {lambda-anon} [X]\\\operatorname {lambda-anon} [V]=\operatorname {false} \\\operatorname {lambda-anon} [M\ N]=\operatorname {false} \end{cases}}$

##### Choosing anonymous functions only for lifting

Search for the deepest anonymous abstraction, so that when the lift is applied the function lifted will become a simple equation. This definition does not recognize a lambda abstractions with a parameter as defining a function. All lambda abstractions are regarded as defining anonymous functions.

*lift-choice* - The first anonymous found in traversing the expression or *none* if there is no function.

1. $\operatorname {lambda-anon} [X]\to \operatorname {lift-choice} [X]=X$
2. $\operatorname {lift-choice} [\lambda F.X]=\operatorname {lift-choice} [X]$
3. $\operatorname {lift-choice} [M]\neq \operatorname {none} \to \operatorname {lift-choice} [M\ N]=\operatorname {lift-choice} [M]$
4. $\operatorname {lift-choice} [M\ N]=\operatorname {lift-choice} [N]$
5. $\operatorname {lift-choice} [V]=\operatorname {none}$

For example,

| Rule | function type | choice |
|---|---|---|
| 2 |   | $\operatorname {lift-choice} [\lambda f.(\lambda x.f\ (x\ x))\ (\lambda y.f\ (y\ y))]$ |
| 3 |   | $\operatorname {lift-choice} [(\lambda x.f\ (x\ x))\ (\lambda y.f\ (y\ y))]$ |
| 1 | anon | $\operatorname {lift-choice} [\lambda x.f\ (x\ x)]$ |
|   |   | $\lambda x.f\ (x\ x)$ |

| Rule | function type | choice |
|---|---|---|
| 2 | anon | $\operatorname {lift-choice} [\lambda f.(p\ f)\ (p\ f)]$ |
| 2 |   | $\lambda f.(p\ f)\ (p\ f)$ |

##### Choosing named and anonymous functions for lifting

Search for the deepest named or anonymous function definition, so that when the lift is applied the function lifted will become a simple equation. This definition recognizes a lambda abstraction with an actual parameter as defining a function. Only lambda abstractions without an application are treated as anonymous functions.

***lambda-named***

A named function. An expression like

$(\lambda F.M)\ N$

where M is lambda free and N is lambda free or an anonymous function.

${\begin{array}{l}\operatorname {lambda-named} [(\lambda F.M)\ N]=\operatorname {lambda-free} [M]\land \operatorname {lambda-anon} [N]\\\operatorname {lambda-named} [\lambda F.X]=\operatorname {false} \\\operatorname {lambda-named} [V]=\operatorname {false} \end{array}}$

***lift-choice***

The first anonymous or named function found in traversing the expression or

none

if there is no function.

1. $\operatorname {lambda-named} [X]\lor \operatorname {lambda-anon} [X]\to \operatorname {lift-choice} [X]=X$
2. $\operatorname {lift-choice} [\lambda F.X]=\operatorname {lift-choice} [X]$
3. $\operatorname {lift-choice} [M]\neq \operatorname {none} \to \operatorname {lift-choice} [M\ N]=\operatorname {lift-choice} [M]$
4. $\operatorname {lift-choice} [M\ N]=\operatorname {lift-choice} [N]$
5. $\operatorname {lift-choice} [V]=\operatorname {none}$

For example,

| Rule | function type | choice |
|---|---|---|
| 2 |   | $\operatorname {lift-choice} [\lambda f.(\lambda x.f\ (x\ x))\ (\lambda y.f\ (y\ y))]$ |
| 1 | named | $\operatorname {lift-choice} [(\lambda x.f\ (x\ x))\ (\lambda y.f\ (y\ y))]$ |
|   |   | $(\lambda x.f\ (x\ x))\ (\lambda y.f\ (y\ y))$ |

| Rule | function type | choice |
|---|---|---|
| 1 | anon | $\operatorname {lift-choice} [\lambda f.f\ ((x\ f)\ (x\ f))]$ |
|   |   | $\lambda f.f\ ((x\ f)\ (x\ f))$ |

### Examples

For example, the Y combinator,

$\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))$

is lifted as,

$\operatorname {let} x\ f\ y=f\ (y\ y)\land q\ x\ f=f\ ((x\ f)\ (x\ f))\operatorname {in} q\ x$

and after Parameter dropping,

$\operatorname {let} x\ f\ y=f\ (y\ y)\land q\ f=f\ ((x\ f)\ (x\ f))\operatorname {in} q$

As a lambda expression (see Conversion from let to lambda expressions),

$(\lambda x.(\lambda q.q)\ \lambda f.f\ (x\ f)\ (x\ f))\ \lambda f.\lambda y.f\ (y\ y)$

|   | Lambda Expression | Function | From | To | Variables |
|---|---|---|---|---|---|
| 1 | $\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))$ | true | $(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))$ | $x\ f$ | $\{x,f\}$ |
| 2 | $(\lambda f.(\lambda x.f\ (x\ x))(\lambda x.f\ (x\ x)))$ $[(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x)):=f\ ((x\ f)\ (x\ f))]$ | $x\ f=\lambda y.f\ (y\ y)$ |   |   | $\{x,f,p\}$ |
| 3 | $\lambda f.f\ ((x\ f)\ (x\ f))$ | $x\ f\ y=f\ (y\ y)$ | $\lambda f.f\ ((x\ f)\ (x\ f))$ | $q\ x$ | $\{x,f,p\}$ |
| 4 | $\lambda f.f\ ((x\ f)\ (x\ f))[\lambda f.f\ ((x\ f)\ (x\ f)):=q\ x]$ | $x\ f\ y=f\ (y\ y)\land q\ x=\lambda f.f\ ((x\ f)\ (x\ f))$ |   |   | $\{x,f,p,q\}$ |
| 5 | $q\ x$ | $x\ f\ y=f\ (y\ y)\land q\ x\ f=f\ ((x\ f)\ (x\ f))$ |   |   | $\{x,f,p,q\}$ |

If lifting anonymous functions only, the Y combinator is,

$\operatorname {let} p\ f\ x=f\ (x\ x)\land q\ p\ f=(p\ f)\ (p\ f)\operatorname {in} q\ p$

and after Parameter dropping,

$\operatorname {let} p\ f\ x=f\ (x\ x)\land q\ f=(p\ f)\ (p\ f)\operatorname {in} q$

As a lambda expression,

$(\lambda p.(\lambda q.q)\ \lambda f.(p\ f)\ (p\ f))\ \lambda f.\lambda x.f\ (x\ x)$

|   | Lambda Expression | Function | From | To | Variables |
|---|---|---|---|---|---|
| 1 | $\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))$ | true | $\lambda x.f\ (x\ x)$ | $p\ f$ | $\{x,f\}$ |
| 2 | $(\lambda f.(\lambda x.f\ (x\ x))(\lambda x.f\ (x\ x)))[\lambda x.f\ (x\ x):=p\ f]$ | $p\ f=\lambda x.f\ (x\ x)$ |   |   | $\{x,f,p\}$ |
| 3 | $\lambda f.(p\ f)\ (p\ f)$ | $p\ f\ x=f\ (x\ x)$ | $\lambda f.(p\ f)\ (p\ f)$ | $q\ p$ | $\{x,f,p\}$ |
| 4 | $\lambda f.(p\ f)\ (p\ f)[\lambda f.(p\ f)\ (p\ f):=q\ p]$ | $p\ f\ x=f\ (x\ x)\land q\ p=\lambda f.(p\ f)\ (p\ f)$ |   |   | $\{x,f,p,q\}$ |
| 5 | $q\ p$ | $p\ f\ x=f\ (x\ x)\land q\ p\ f=(p\ f)\ (p\ f)$ |   |   | $\{x,f,p,q\}$ |

The first sub expression to be chosen for lifting is $\lambda x.f\ (x\ x)$ . This transforms the lambda expression into $\lambda f.(p\ f)\ (p\ f)$ and creates the equation $p\ f\ x=f(x\ x)$ .

The second sub expression to be chosen for lifting is $\lambda f.(p\ f)\ (p\ f)$ . This transforms the lambda expression into $q\ p$ and creates the equation $q\ p\ f=(p\ f)\ (p\ f)$ .

And the result is,

$\operatorname {let} p\ f\ x=f\ (x\ x)\land q\ p\ f=(p\ f)\ (p\ f)\operatorname {in} q\ p\$

Surprisingly this result is simpler than the one obtained from lifting named functions.

### Execution

Apply function to K,

${\begin{cases}\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))\ K&\ \operatorname {let} \ p\ f\ x=f\ (x\ x)\land q\ p\ f=(p\ f)\ (p\ f)\ \operatorname {in} \ q\ p\ K\\(\lambda x.K\ (x\ x))\ (\lambda x.K\ (x\ x))&\ \operatorname {let} \ p\ f\ x=f\ (x\ x)\land q\ p\ f=(p\ f)\ (p\ f)\ \operatorname {in} \ p\ K\ (p\ K)\\K\ ((\lambda x.K\ (x\ x))\ (\lambda x.K\ (x\ x)))&\ \operatorname {let} \ p\ f\ x=f\ (x\ x)\land q\ p\ f=p\ f\ (p\ f)\ \operatorname {in} \ K\ (p\ K\ (p\ K))\\\end{cases}}$

So,

$(\lambda x.K\ (x\ x))\ (\lambda x.K\ (x\ x))=K\ ((\lambda x.K\ (x\ x))\ (\lambda x.K\ (x\ x))))\$

or

$p\ K\ (p\ K)=K\ (p\ K\ (p\ K))$

The Y-Combinator calls its parameter (function) repeatedly on itself. The value is defined if the function has a fixed point. But the function will never terminate.
