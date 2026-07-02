---
title: "Lambda lifting (part 2/2)"
source: https://en.wikipedia.org/wiki/Lambda_lifting
domain: defunctionalization
license: CC-BY-SA-4.0
tags: defunctionalization transform, closure conversion, higher-order function, apply function
fetched: 2026-07-02
part: 2/2
---

## Lambda dropping in lambda calculus

Lambda dropping is making the scope of functions smaller and using the context from the reduced scope to reduce the number of parameters to functions. Reducing the number of parameters makes functions easier to comprehend.

In the Lambda lifting section, a meta function for first lifting and then converting the resulting lambda expression into recursive equation was described. The Lambda Drop meta function performs the reverse by first converting recursive equations to lambda abstractions, and then dropping the resulting lambda expression, into the smallest scope which covers all references to the lambda abstraction.

Lambda dropping is performed in two steps,

- Sinking
- Parameter dropping

### Lambda drop

A Lambda drop is applied to an expression which is part of a program. Dropping is controlled by a set of expressions from which the drop will be excluded.

$\operatorname {lambda-drop-op} [L,P,X]=P[L:=\operatorname {drop-params-tran} [\operatorname {sink-test} [L,X]]]$

where,

L

is the lambda abstraction to be dropped.

P

is the program

X

is a set of expressions to be excluded from dropping.

### Lambda drop transformation

The lambda drop transformation sinks all abstractions in an expression. Sinking is excluded from expressions in a set of expressions,

$\operatorname {lambda-drop-tran} [L,X]=\operatorname {drop-params-tran} [\operatorname {sink-tran} [\operatorname {de-let} [L,X]]]$

where,

L

is the expression to be transformed.

X

is a set of sub expressions to be excluded from the dropping.

*sink-tran* sinks each abstraction, starting from the innermost,

${\begin{cases}\operatorname {sink-tran} [(\lambda N.B)\ Y,X]=\operatorname {sink-test} [(\lambda N.\operatorname {sink-tran} [B])\ \operatorname {sink-tran} [Y],X]\\\operatorname {sink-tran} [\lambda N.B,X]=\lambda N.\operatorname {sink-tran} [B,X]\\\operatorname {sink-tran} [M\ N,X]=\operatorname {sink-tran} [M,X]\ \operatorname {sink-tran} [M,X]\\\operatorname {sink-tran} [V,X]=V\end{cases}}$

### Abstraction sinking

Sinking is moving a lambda abstraction inwards as far as possible such that it is still outside all references to the variable.

**Application** - 4 cases.

${\begin{cases}E\not \in \operatorname {FV} [G]\land E\not \in \operatorname {FV} [H]\to \operatorname {sink} [(\lambda E.G\ H)\ Y,X]=G\ H\\E\not \in \operatorname {FV} [G]\land E\in \operatorname {FV} [H]\to \operatorname {sink} [(\lambda E.G\ H)\ Y,X]=\operatorname {sink-test} [G\ \operatorname {sink-test} [(\lambda E.H)\ Y,X]]\\E\in \operatorname {FV} [G]\land E\not \in \operatorname {FV} [H]\to \operatorname {sink} [(\lambda E.G\ H)\ Y,X]=(\operatorname {sink-test} [(\lambda E.G)\ Y,X])\ H\\E\in \operatorname {FV} [G]\land E\in \operatorname {FV} [H]\to \operatorname {sink} [(\lambda E.G\ H)\ Y,X]=(\lambda E.G\ H)\ Y\end{cases}}$

**Abstraction**. Use renaming to ensure that the variable names are all distinct.

$V\neq W\to \operatorname {sink} [(\lambda V.\lambda W.E)\ Y,X]=\lambda W.\operatorname {sink-test} [(\lambda V.E)\ Y,X]$

**Variable** - 2 cases.

$E\neq V\to \operatorname {sink} [(\lambda E.V)\ Y,X]=V$

$E=V\to \operatorname {sink} [(\lambda E.V)\ Y,X]=Y$

Sink test excludes expressions from dropping,

$L\in X\to \operatorname {sink-test} [L,X]=L$

$L\not \in X\to \operatorname {sink-test} [L,X]=\operatorname {sink} [L,X]$

#### Example

| Example of sinking |
|---|
| For example, RuleExpression *de-let* $\operatorname {sink-tran} [\operatorname {de-let} [\operatorname {let} p\ f\ x=f\ (x\ x)\land q\ p\ f=(p\ f)\ (p\ f)\operatorname {in} q\ p]]$ *sink-tran* $\operatorname {sink-tran} [(\lambda p.(\lambda q.q\ p)\ (\lambda p.\lambda f.(p\ f)\ (p\ f)))\ (\lambda f.\lambda x.f\ (x\ x))]$ Application $\operatorname {sink} [(\lambda p.\operatorname {sink} [(\lambda q.q\ p)\ (\lambda p.\lambda f.(p\ f)\ (p\ f))])\ (\lambda f.\lambda x.f\ (x\ x))]$ $\operatorname {sink} [(\lambda q.q\ p)\ (\lambda p.\lambda f.(p\ f)\ (p\ f))]$ $E\in \operatorname {FV} [G]\land E\not \in \operatorname {FV} [H]\to \operatorname {sink} [(\lambda E.G\ H)\ Y,X]$ $E=q,G=q,H=p,Y=(\lambda p.\lambda f.(p\ f)\ (p\ f)),X=\{\}$ $(\operatorname {sink} [(\lambda E.G)\ Y,X])\ H$ $(\operatorname {sink} [(\lambda q.q)\ (\lambda p.\lambda f.(p\ f)\ (p\ f)),X])\ p$ Variable $\operatorname {sink} [(\lambda p.\operatorname {sink} [(\lambda q.q)\ (\lambda p.\lambda f.(p\ f)\ (p\ f))]\ p)\ (\lambda f.\lambda x.f\ (x\ x))]$ $\operatorname {sink} [(\lambda q.q)\ (\lambda p.\lambda f.(p\ f)\ (p\ f))]$ $E=V\to \operatorname {sink} [(\lambda E.V)\ Y,X]$ $E=q,V=q,Y=(\lambda p.\lambda f.(p\ f)\ (p\ f)),X=\{\}$ Y $(\lambda p.\lambda f.(p\ f)\ (p\ f))$ Application $\operatorname {sink} [(\lambda p.(\lambda p.\lambda f.(p\ f)\ (p\ f))\ p)\ (\lambda f.\lambda x.f\ (x\ x))]$ $E\not \in \operatorname {FV} [G]\land E\in \operatorname {FV} [H]\to \operatorname {sink} [(\lambda E.G\ H)\ Y,X]$ $E=p,G=(\lambda p.\lambda f.(p\ f)\ (p\ f)),H=p,Y=(\lambda f.\lambda x.f\ (x\ x))$ $\operatorname {sink} [G\ \operatorname {sink} [(\lambda E.H)\ Y,X]]$ Variable $\operatorname {sink} [(\lambda p.\lambda f.(p\ f)\ (p\ f))\ \operatorname {sink-test} [(\lambda p.p)\ (\lambda f.\lambda x.f\ (x\ x)),X]]$ $\operatorname {sink} [(\lambda p.p)\ (\lambda f.\lambda x.f\ (x\ x)),X]$ $E=V\to \operatorname {sink} [(\lambda E.V)\ Y,X]$ $E=p,V=p,Y=(\lambda f.\lambda x.f\ (x\ x)),X=\{\}$ Y $(\lambda f.\lambda x.f\ (x\ x))$ Abstraction $\operatorname {sink} [(\lambda p.\lambda f.(p\ f)\ (p\ f))\ (\lambda f.\lambda x.f\ (x\ x))]$ $V\neq W\to \operatorname {sink} [(\lambda V.\lambda W.E)\ Y,X]$ $V=p,W=f,E=(p\ f)\ (p\ f),Y=(\lambda f.\lambda x.f\ (x\ x))$ $\lambda W.\operatorname {sink} [(\lambda V.E)\ Y,X]$ Application $\lambda f.\operatorname {sink} [(\lambda p.(p\ f)\ (p\ f))\ (\lambda f.\lambda x.f\ (x\ x)),X]$ $\operatorname {sink} [(\lambda p.(p\ f)\ (p\ f))\ (\lambda f.\lambda x.f\ (x\ x)),X]$ $E\in \operatorname {FV} [G]\land E\in \operatorname {FV} [H]\to \operatorname {sink} [(\lambda E.G\ H)\ Y,X]$ $E=p,G=(p\ f),H=(p\ f),Y=(\lambda f.\lambda x.f\ (x\ x))$ $(\lambda E.G\ H)\ Y$ $(\lambda p.(p\ f)\ (p\ f))\ (\lambda f.\lambda x.f\ (x\ x))$ $\lambda f.(\lambda p.(p\ f)\ (p\ f))\ (\lambda f.\lambda x.f\ (x\ x))$ |

### Parameter dropping

Parameter dropping is optimizing a function for its position in the function. Lambda lifting added parameters that were necessary so that a function can be moved out of its context. In dropping, this process is reversed, and extra parameters that contain variables that are free may be removed.

Dropping a parameter is removing an unnecessary parameter from a function, where the actual parameter being passed in is always the same expression. The free variables of the expression must also be free where the function is defined. In this case the parameter that is dropped is replaced by the expression in the body of the function definition. This makes the parameter unnecessary.

For example, consider,

$\lambda m,p,q.(\lambda g.\lambda n.(n\ (g\ m\ p\ n)\ (g\ q\ p\ n)))\ \lambda x.\lambda o.\lambda y.o\ x\ y$

In this example the actual parameter for the formal parameter *o* is always *p*. As *p* is a free variable in the whole expression, the parameter may be dropped. The actual parameter for the formal parameter *y* is always *n*. However *n* is bound in a lambda abstraction. So this parameter may not be dropped.

The result of dropping the parameter is,

$\operatorname {drop-params-tran} [\lambda m,p,q.(\lambda g.\lambda n.n\ (g\ m\ p\ n)\ (g\ q\ p\ n))\ \lambda x.\lambda o.\lambda y.o\ x\ y$

$\equiv \lambda m,p,q.(\lambda g.\lambda n.n\ (g\ m\ n)\ (g\ q\ n))\ \lambda x.\lambda y.p\ x\ y$

For the main example,

$\operatorname {drop-params-tran} [\lambda f.(\lambda p.(p\ f)\ (p\ f))\ (\lambda f.\lambda x.f\ (x\ x))]$

$\equiv \lambda f.(\lambda p.p\ p)\ (\lambda x.f\ (x\ x))$

The definition of *drop-params-tran* is,

$\operatorname {drop-params-tran} [L]\equiv (\operatorname {drop-params} [L,D,FV[L],[]])$

where,

$\operatorname {build-param-list} [L,D,V,\_]$

#### Build parameter lists

For each abstraction that defines a function, build the information required to make decisions on dropping names. This information describes each parameter; the parameter name, the expression for the actual value, and an indication that all the expressions have the same value.

For example, in,

$\lambda m,p,q.(\lambda g.\lambda n.(n\ (g\ m\ p\ n)\ (g\ q\ p\ n)))\ \lambda x.\lambda o.\lambda y.o\ x\ y$

the parameters to the function *g* are,

| Formal parameter | All same value | Actual parameter expression |
|---|---|---|
| *x* | false | _ |
| *o* | true | *p* |
| *y* | true | *n* |

Each abstraction is renamed with a unique name, and the parameter list is associated with the name of the abstraction. For example, *g* there is parameter list.

$D[g]=[[x,\operatorname {false} ,\_],[o,\_,p],[y,\_,n]]$

*build-param-lists* builds all the lists for an expression, by traversing the expression. It has four parameters;

- The lambda expression being analyzed.
- The table parameter lists for names.
- The table of values for parameters.
- The returned parameter list, which is used internally by the

**Abstraction** - A lambda expression of the form $(\lambda N.S)\ L$ is analyzed to extract the names of parameters for the function.

${\begin{cases}\operatorname {build-param-lists} [(\lambda N.S)\ L,D,V,R]\equiv \operatorname {build-param-lists} [S,D,V,R]\land \operatorname {build-list} [L,D,V,D[N]]\\\operatorname {build-param-lists} [\lambda N.S,D,V,R]\equiv \operatorname {build-param-lists} [S,D,V,R]\end{cases}}$

Locate the name and start building the parameter list for the name, filling in the formal parameter names. Also receive any actual parameter list from the body of the expression, and return it as the actual parameter list from this expression

${\begin{cases}\operatorname {build-list} [\lambda P.B,D,V,[X,\_,\_]::L]\equiv \operatorname {build-list} [B,D,V,L]\\\operatorname {build-list} [B,D,V,[]]\equiv \operatorname {build-param-lists} [B,D,V,\_]\end{cases}}$

**Variable** - A call to a function.

$\operatorname {build-param-lists} [N,D,V,D[N]]$

For a function name or parameter start populating actual parameter list by outputting the parameter list for this name.

**Application** - An application (function call) is processed to extract actual parameter details.

$\operatorname {build-param-lists} [E\ P,D,V,R]\equiv \operatorname {build-param-lists} [E,D,V,T]\land \operatorname {build-param-lists} [P,D,V,K]$

$\land T=[F,S,A]::R\land (S\implies (\operatorname {equate} [A,P]\land V[F]=A))\land D[F]=K$

Retrieve the parameter lists for the expression, and the parameter. Retrieve a parameter record from the parameter list from the expression, and check that the current parameter value matches this parameter. Record the value for the parameter name for use later in checking.

${\begin{cases}\operatorname {equate} [A,N]\equiv A=N\lor (\operatorname {def} [V[N]]\land A=V[N])&{\text{if }}N{\text{ is a variable.}}\\\operatorname {equate} [A,E]\equiv A=E&{\text{otherwise.}}\end{cases}}$

The above logic is quite subtle in the way that it works. The same value indicator is never set to true. It is only set to false if all the values cannot be matched. The value is retrieved by using *S* to build a set of the Boolean values allowed for *S*. If true is a member then all the values for this parameter are equal, and the parameter may be dropped.

$\operatorname {ask} [S]\equiv S\in \{X:X=S\}$

Similarly, *def* uses set theory to query if a variable has been given a value;

$\operatorname {def} [F]\equiv |\{X:X=F\}|$

**Let** - Let expression.

$\operatorname {build-param-list} [\operatorname {let} V:E\operatorname {in} L,D,V,\_]\equiv \operatorname {build-param-list} [E,D,V,\_]\land \operatorname {build-param-list} [L,D,V,\_]$

**And** - For use in "let".

$\operatorname {build-param-lists} [E\land F,D,V,\_]\equiv \operatorname {build-param-lists} [E,D,V,\_]\land \operatorname {build-param-lists} [F,D,V,\_]$

##### Examples

For example, building the parameter lists for,

$\lambda m,p,q.(\lambda g.\lambda n.(n\ (g\ m\ p\ n)\ (g\ q\ p\ n)))\ \lambda x.\lambda o.\lambda y.o\ x\ y$

gives,

$D[g]=[[x,\operatorname {false} ,\_],[o,\operatorname {true} ,p],[y,\operatorname {true} ,n]]$

and the parameter o is dropped to give,

$\lambda m,p,q.(\lambda g.\lambda n.(n\ (g\ m\ n)\ (g\ q\ n)))\ \lambda x.\lambda y.p\ x\ y$

| Build parameter list for $\lambda m,p,q.(\lambda g.\lambda n.(n\ (g\ m\ p\ n)\ (g\ q\ p\ n)))\ \lambda x.\lambda o.\lambda y.o\ x\ y$ |
|---|
| Build parameter list example |
| $\operatorname {build-param-list} [\lambda m,p,q.(\lambda g.\lambda n.(n\ (g\ m\ p\ n)\ (g\ q\ p\ n)))\ \lambda x.\lambda o.\lambda y.o\ x\ y,D,V,\_]$ RuleExpression Abstraction $\operatorname {build-param-list} [\lambda m,p,q.(\lambda g.\lambda n.(n\ (g\ m\ p\ n)\ (g\ q\ p\ n)))\ \lambda x.\lambda o.\lambda y.o\ x\ y,D,V,\_]$ Abstraction $\operatorname {build-param-list} [(\lambda g.\lambda n.(n\ (g\ m\ p\ n)\ (g\ q\ p\ n)))\ \lambda x.\lambda o.\lambda y.o\ x\ y,D,V,\_]$ $\operatorname {build-param-lists} [n\ (g\ m\ p\ n)\ (g\ q\ p\ n),D,V,R]\land \operatorname {build-list} [\lambda x.\lambda o.\lambda y.o\ x\ y,D,V,D[g]]$ $\operatorname {build-list} [\lambda x.\lambda o.\lambda y.o\ x\ y,D,V,D[g]]$ RuleExpression Add param $\operatorname {build-list} [\lambda x.\lambda o.\lambda y.o\ x\ y,D,V,D[g]]\land D[g]=L_{1}$ Add param $\operatorname {build-list} [\lambda o.\lambda y.o\ x\ y,D,V,L_{1}]\land D[g]=[x,\_,\_]::L_{1}$ Add param $\operatorname {build-list} [\lambda y.o\ x\ y,D,V,L_{2}]\land D[g]=[x,\_,\_]::[o,\_,\_]::L_{2}$ End list $\operatorname {build-list} [o\ x\ y,D,V,L_{3}]\land D[g]=[x,\_,\_]::[o,\_,\_]::[y,\_,\_]::L_{3}$ $\operatorname {build-param-lists} [o\ x\ y,D,V,[]]\land D[g]=[x,\_,\_]::[o,\_,\_]::[y,\_,\_]::[]$ $\operatorname {build-param-lists} [n\ (g\ m\ p\ n)\ (g\ q\ p\ n),D,V,R]$ RuleExpression Application $\operatorname {build-param-lists} [n\ (g\ m\ p\ n)\ (g\ q\ p\ n),D,V,R]$ Application $\operatorname {build-param-lists} [n\ (g\ m\ p\ n),D,V,T_{1}]\land \operatorname {build-param-lists} [g\ q\ p\ n,D,V,K_{1}]$ $\land ((T_{1}=[F_{1},S_{1},A_{1}]::R$ $\land (S_{1}\implies (\operatorname {equate} [A_{1},g\ q\ p\ n]\land V[F_{1}]=g\ q\ p\ n))\land D[F_{1}]=K_{1})$ Variable $\operatorname {build-param-lists} [n,D,V,T_{2}]\land \operatorname {build-param-lists} [g\ m\ p\ n,D,V,K_{2}]\land \operatorname {build-param-lists} [g\ q\ p\ n,D,V,K_{1}]$ $\land ((T_{2}=[F_{2},S_{2},A_{2}]::[F_{1},S_{1},A_{1}]::R$ $\land (S_{1}\implies (\operatorname {equate} [A_{1},g\ q\ p\ n]\land V[F_{1}]=g\ q\ p\ n))\land D[F_{1}]=K_{1})$ $\land (S_{2}\implies (\operatorname {equate} [A_{2},g\ m\ p\ n]\land V[F_{2}]=g\ m\ p\ n))\land D[F_{2}]=K_{2})$ Variable $\operatorname {build-param-lists} [g\ m\ p\ n,D,V,K_{2}]\land \operatorname {build-param-lists} [g\ q\ p\ n,D,V,K_{1}]$ $\land ((D[n]=[F_{2},S_{2},A_{2}]::[F_{1},S_{1},A_{1}]::R$ $\land (S_{1}\implies (\operatorname {equate} [A_{1},g\ q\ p\ n]\land V[F_{1}]=g\ q\ p\ n))\land D[F_{1}]=K_{1})$ $\land (S_{2}\implies (\operatorname {equate} [A_{2},g\ m\ p\ n]\land V[F_{2}]=g\ m\ p\ n))\land D[F_{2}]=K_{2})$ Gives, $D[n]=[\_,\_,g\ m\ p\ n]::[\_,\_,g\ q\ p\ n]::R$ $\operatorname {build-param-lists} [g\ m\ p\ n,D,V,K_{2}]$ RuleExpression application $\operatorname {build-param-lists} [g\ m\ p\ n,D,V,K_{2}]$ $\operatorname {build-param-lists} [g\ m\ p,D,V,T_{3}]\land \operatorname {build-param-lists} [n,D,V,K_{3}]$ $\land ((T_{3}=[F_{3},S_{3},A_{3}]::K_{2}$ $\land (S_{3}\implies (\operatorname {equate} [A_{3},n]\land V[F_{3}]=n))\land D[F_{3}]=D[n])$ application, Variable $\operatorname {build-param-lists} [g\ m,D,V,T_{4}]\land \operatorname {build-param-lists} [p,D,V,K_{4}]$ $\land T_{4}=[\_,S_{4},A_{4}]::[\_,S_{3},A_{3}]::K_{2}$ $\land (S_{3}\implies (\operatorname {equate} [A_{3},n]\land V[F_{3}]=n))\land D[F_{3}]=D[n])$ $\land (S_{4}\implies (\operatorname {equate} [A_{4},p]\land V[F_{4}]=p))\land D[F_{4}]=D[p]$ application, Variable $\operatorname {build-param-lists} [g,D,V,T_{5}]\land \operatorname {build-param-lists} [m,D,V,K_{5}]$ $\land T_{5}=[F_{5},S_{5},A_{5}]::[F_{4},S_{4},A_{4}]::[F_{3},S_{3},A_{3}]::K_{2}$ $\land (S_{3}\implies (\operatorname {equate} [A_{3},n]\land V[F_{3}]=n))\land D[F_{3}]=D[n])$ $\land (S_{4}\implies (\operatorname {equate} [A_{4},p]\land V[F_{4}]=p))\land D[F_{4}]=D[p]$ $\land (S_{5}\implies (\operatorname {equate} [A_{5},m]\land V[F_{5}]=m))\land D[F_{5}]=D[m]$ Variable $D[g]=[x,S_{5},A_{5}]::[o,S_{4},A_{4}]::[y,S_{3},A_{3}]::K_{2}$ $\land (S_{3}\implies (\operatorname {equate} [A_{3},n]\land V[y]=n))\land D[y]=D[n])$ $\land (S_{4}\implies (\operatorname {equate} [A_{4},p]\land V[o]=p))\land D[o]=D[p]$ $\land (S_{5}\implies (\operatorname {equate} [A_{5},m]\land V[x]=m))\land D[x]=D[m]$ $\operatorname {build-param-lists} [g\ q\ p\ n,D,V,K_{1}]$ RuleExpression application $\operatorname {build-param-lists} [g\ q\ p\ n,D,V,K_{1}]$ $\operatorname {build-param-lists} [g\ q\ p,D,V,T_{6}]\land \operatorname {build-param-lists} [n,D,V,K_{6}]$ $\land ((T_{6}=[F_{6},S_{6},A_{6}]::K_{1}$ $\land (S_{6}\implies (\operatorname {equate} [A_{6},n]\land V[F_{6}]=n))\land D[F_{6}]=D[n])$ application, Variable $\operatorname {build-param-lists} [g\ q,D,V,T_{7}]\land \operatorname {build-param-lists} [p,D,V,K_{7}]$ $\land T_{7}=[\_,S_{7},A_{7}]::[\_,S_{6},A_{6}]::K_{1}$ $\land (S_{6}\implies (\operatorname {equate} [A_{6},n]\land V[F_{6}]=n))\land D[F_{6}]=D[n])$ $\land (S_{7}\implies (\operatorname {equate} [A_{7},p]\land V[F_{7}]=p))\land D[F_{7}]=D[p]$ application, Variable $\operatorname {build-param-lists} [g,D,V,T_{8}]\land \operatorname {build-param-lists} [m,D,V,K_{8}]$ $\land T_{8}=[F_{8},S_{8},A_{8}]::[F_{7},S_{7},A_{7}]::[F_{6},S_{6},A_{6}]::K_{1}$ $\land (S_{6}\implies (\operatorname {equate} [A_{6},n]\land V[F_{6}]=n))\land D[F_{6}]=D[n])$ $\land (S_{7}\implies (\operatorname {equate} [A_{7},p]\land V[F_{7}]=p))\land D[F_{7}]=D[p]$ $\land (S_{8}\implies (\operatorname {equate} [A_{8},q]\land V[F_{8}]=q))\land D[F_{8}]=D[q]$ Variable $D[g]=[x,S_{8},A_{8}]::[o,S_{6},A_{7}]::[y,S_{6},A_{6}]::K_{1}$ $\land (S_{6}\implies (\operatorname {equate} [A_{6},n]\land V[y]=n))\land D[y]=D[n])$ $\land (S_{7}\implies (\operatorname {equate} [A_{7},p]\land V[o]=p))\land D[o]=D[p]$ $\land (S_{8}\implies (\operatorname {equate} [A_{8},q]\land V[x]=q))\land D[x]=D[q]$ As there are no definitions for, $V[n],V[p],V[q],V[m]$ , then equate can be simplified to, $\operatorname {equate} [A,N]\equiv A=N\lor (\operatorname {def} [V[N]]\land A=V[N])\equiv A=N$ By removing expressions not needed, $D[g]=[x,S_{5},A_{5}]::[o,S_{4},A_{4}]::[y,S_{3},A_{3}]::K_{2}$ $\land S_{3}\implies A_{3}=n$ $\land S_{4}\implies A_{4}=p$ $\land S_{5}\implies A_{5}=m$ $D[g]=[x,S_{8},A_{8}]::[o,S_{6},A_{7}]::[y,S_{6},A_{6}]::K_{1}$ $\land S_{6}\implies A_{6}=n$ $\land S_{7}\implies A_{7}=p$ $\land S_{8}\implies A_{8}=q$ By comparing the two expressions for $D[g]$ , get, $S_{5}=S_{8},A_{5}=A_{8},S_{4}=S_{7},A_{4}=A_{7},S_{3}=S_{6},A_{3}=A_{6}$ If $S_{3}$ is true; $n=A_{3}=A_{6}=n$ If $S_{3}$ is false there is no implication. So $S_{3}=\_$ which means it may be true or false. If $S_{4}$ is true; $p=A_{4}=A_{7}=p$ If $S_{5}$ is true; $m=A_{5}=A_{8}=q$ So $S_{5}$ is false. The result is, $D[g]=[x,\operatorname {false} ,\_]::[o,\_,p]::[y,\_,n]::\_$ $\operatorname {build-param-lists} [o\ x\ y,D,V,L]$ RuleExpression application $\operatorname {build-param-lists} [o\ x\ y,D,V,L]$ application $\operatorname {build-param-lists} [o\ x,D,V,T_{9}]\land \operatorname {build-param-lists} [y,D,V,K_{9}]$ $\land T_{9}=[F_{9},S_{9},A_{9}]::L$ $\land (S_{9}\implies (\operatorname {equate} [A_{9},y]\land V[F_{9}]=A_{9})\land K_{9}=D[F_{9}]$ variable $\operatorname {build-param-lists} [o,D,V,T_{10}]\land \operatorname {build-param-lists} [x,D,V,K_{10}]\land \operatorname {build-param-lists} [y,D,V,K_{10}]$ $\land T_{10}=[F_{10},S_{10},A_{10}]::[F_{9},S_{9},A_{9}]::L$ $\land (S_{9}\implies (\operatorname {equate} [A_{9},y]\land V[F_{9}]=A_{9})\land K_{9}=D[F_{9}]$ $\land (S_{10}\implies (\operatorname {equate} [A_{10},y]\land V[F_{10}]=A_{10})\land K_{10}=D[F_{10}]$ $\land D[o]=[F_{10},S_{10},A_{10}]::[F_{9},S_{9},A_{9}]::L$ $\land (S_{9}\implies (\operatorname {equate} [A_{9},y]\land V[F_{9}]=A_{9})\land K_{9}=D[F_{9}]$ $\land (S_{10}\implies (\operatorname {equate} [A_{10},y]\land V[F_{10}]=A_{10})\land K_{10}=D[F_{10}]$ By similar arguments as used above get, $D[o]=[\_,\_,x]::[\_,\_,y]::\_$ and from previously, $D[g]=[[x,\operatorname {false} ,\_],[o,\operatorname {true} ,p],[y,\operatorname {true} ,n]]$ $D[n]=[[\_,\_,(g\ m\ p\ n)],[\_,\_,(g\ q\ p\ n)]]$ $D[m]=\_$ $D[p]=\_$ $D[q]=\_$ |

Another example is,

$\lambda f.((\lambda p.f\ (p\ p\ f))\ (\lambda q.\lambda x.x\ (q\ q\ x))$

Here x is equal to f. The parameter list mapping is,

$D[p]=[[q,\_,p],[x,\_,f]]$

and the parameter x is dropped to give,

$\lambda f.((\lambda q.f\ (q\ q))\ (\lambda q.f\ (q\ q))$

| Build parameter list for $\lambda f.((\lambda p.f\ (p\ p\ f))\ (\lambda q.\lambda x.x\ (q\ q\ x))$ |
|---|
| The logic in *equate* is used in this more difficult example. $\operatorname {build-param-list} [\lambda f.((\lambda p.f\ (p\ p\ f))\ (\lambda q.\lambda x.x\ (q\ q\ x)),D,V,\_]$ RuleExpression Abstraction $\operatorname {build-param-list} [\lambda f.((\lambda p.f\ (p\ p\ f))\ (\lambda q.\lambda x.x\ (q\ q\ x)),D,V,\_]$ Abstraction $\operatorname {build-param-list} [(\lambda p.f\ (p\ p\ f))\ (\lambda q.\lambda x.x\ (q\ q\ x)),D,V,\_]$ $\operatorname {build-param-lists} [f\ (p\ p\ f),D,\_]\land \operatorname {build-list} [\lambda q.\lambda x.x\ (q\ q\ x),D,D[p]]$ $\operatorname {build-param-lists} [f\ (p\ p\ f),D,\_]\land \operatorname {build-list} [\lambda q.\lambda x.x\ (q\ q\ x),D,D[p]]$ $\operatorname {build-list} [\lambda q.\lambda x.x\ (q\ q\ x),D,D[p]]$ RuleExpression Add param $\operatorname {build-list} [\lambda q.\lambda x.x\ (q\ q\ x),D,D[p]]\land D[p]=L_{1}$ Add param $\operatorname {build-list} [\lambda x.x\ (q\ q\ x),D,L_{2}]\land D[p]=[q,\_,\_]::L_{2}$ End list $\operatorname {build-list} [x\ (q\ q\ x),D,L_{3}]\land D[p]=[q,\_,\_]::[x,\_,\_]::L_{3}$ $\operatorname {build-param-lists} [x\ (q\ q\ x),D,[]]\land D[p]=[q,\_,\_]::[x,\_,\_]::[]$ $\operatorname {build-param-lists} [\lambda p.f\ (p\ p\ f),D,V,T_{1}]$ RuleExpression Abstraction $\operatorname {build-param-lists} [\lambda p.f\ (p\ p\ f),D,V,T_{1}]$ Application $\operatorname {build-param-lists} [f\ (p\ p\ f),D,V,T_{1}]$ Name $\operatorname {build-param-lists} [f,D,V,T_{2}]\land \operatorname {build-param-lists} [p\ p\ f,D,V,K_{2}]$ $\land T_{2}=[F_{2},S_{2},A_{2}]::[F_{1},S_{1},A_{1}]::\_$ $\land (S_{2}\implies (\operatorname {equate} [A_{2},p\ p\ f]\land V[F_{2}]=A_{2}))\land D[F_{2}]=K_{2}$ Name $\operatorname {build-param-lists} [p\ p\ f,D,V,K_{2}]$ $\land D[f]=[F_{2},S_{2},A_{2}]::[F_{1},S_{1},A_{1}]::\_$ $\land (S_{2}\implies (\operatorname {equate} [A_{2},p\ p\ f]\land V[F_{2}]=A_{2}))\land D[F_{2}]=K_{2}$ Name $\operatorname {build-param-lists} [p\ p,D,V,T_{3}]\land \operatorname {build-param-lists} [f,D,V,K_{3}]$ $\land T_{3}=[F_{3},S_{3},A_{3}]::K_{2}$ $\land (S_{3}\implies (\operatorname {equate} [A_{3},f]\land V[F_{3}]=A_{3}))\land D[F_{3}]=K_{3}$ Application $\operatorname {build-param-lists} [p\ p,D,V,T_{3}]$ $\land T_{3}=[F_{3},S_{3},A_{3}]::K_{2}$ $\land (S_{2}\implies (\operatorname {equate} [A_{2},p\ p\ f]\land V[F_{2}]=A_{2}))\land D[F_{2}]=K_{2}$ $\land (S_{3}\implies (\operatorname {equate} [A_{3},f]\land V[F_{3}]=A_{3}))\land D[F_{3}]=D[f]$ Name $\operatorname {build-param-lists} [p,D,V,T_{4}]\land \operatorname {build-param-lists} [p,D,V,K_{4}]$ $\land T_{4}=[F_{4},S_{4},A_{4}]::[F_{3},S_{3},A_{3}]::K_{2}$ $\land (S_{3}\implies (\operatorname {equate} [A_{3},f]\land V[F_{3}]=A_{3}))\land D[F_{3}]=D[f]$ $\land (S_{4}\implies (\operatorname {equate} [A_{4},p]\land V[F_{4}]=A_{4}))\land D[F_{4}]=K_{4}$ $D[p]=[F_{4},S_{4},A_{4}]::[F_{3},S_{3},A_{3}]::K_{2}$ $\land (S_{3}\implies (\operatorname {equate} [A_{3},f]\land V[F_{3}]=A_{3}))\land D[F_{3}]=D[f]$ $\land (S_{4}\implies (\operatorname {equate} [A_{4},p]\land V[F_{4}]=A_{4}))\land D[F_{4}]=D[p]$ $\operatorname {build-param-lists} [x\ (q\ q\ x)),D,V,\_]$ RuleExpression Abstraction $\operatorname {build-param-lists} [\lambda q.\lambda x.x\ (q\ q\ x)),D,V,\_]$ Application $\operatorname {build-param-lists} [x\ (q\ q\ x)),D,V,K_{1}]$ Name $\operatorname {build-param-lists} [x,D,V,T_{5}]\land \operatorname {build-param-lists} [q\ q\ x,D,V,K_{5}]$ $\land T_{5}=[F_{5},S_{5},A_{5}]::\_$ $\land (S_{5}\implies (\operatorname {equate} [A_{5},q\ q\ x]\land V[F_{5}]=A_{5}))\land D[F_{5}]=K_{5}$ Name $\operatorname {build-param-lists} [q\ q\ x,D,V,K_{5}]$ $\land D[x]=[F_{5},S_{5},A_{5}]::\_$ $\land (S_{5}\implies (\operatorname {equate} [A_{5},q\ q\ x]\land V[F_{5}]=A_{5}))\land D[F_{5}]=K_{5}$ Name $\operatorname {build-param-lists} [q\ q,D,V,T_{6}]\land \operatorname {build-param-lists} [x,D,V,K_{6}]$ $\land T_{6}=[F_{6},S_{6},A_{6}]::K_{5}$ $\land (S_{6}\implies (\operatorname {equate} [A_{6},x]\land V[F_{6}]=A_{6}))\land D[F_{6}]=K_{6}$ Application $\operatorname {build-param-lists} [q\ q,D,V,T_{6}]$ $\land T_{6}=[F_{6},S_{6},A_{6}]::K_{5}$ $\land (S_{6}\implies (\operatorname {equate} [A_{6},x]\land V[F_{6}]=A_{6}))\land D[F_{6}]=D[x]$ Name $\operatorname {build-param-lists} [q,D,V,T_{7}]\land \operatorname {build-param-lists} [q,D,V,K_{7}]$ $\land T_{7}=[F_{7},S_{7},A_{7}]::[F_{6},S_{6},A_{6}]::K_{5}$ $\land (S_{6}\implies (\operatorname {equate} [A_{6},x]\land V[F_{6}]=A_{6}))\land D[F_{6}]=D[x]$ $\land (S_{7}\implies (\operatorname {equate} [A_{7},q]\land V[F_{7}]=A_{7}))\land D[F_{7}]=K_{7}$ Name $\operatorname {build-param-lists} [q,D,V,K_{7}]$ $\land D[q]=[F_{7},S_{7},A_{7}]::[F_{6},S_{6},A_{6}]::K_{5}$ $\land (S_{6}\implies (\operatorname {equate} [A_{6},x]\land V[F_{6}]=A_{6}))\land D[F_{6}]=D[x]$ $\land (S_{7}\implies (\operatorname {equate} [A_{7},q]\land V[F_{7}]=A_{7}))\land D[F_{7}]=D[q]$ After collecting the results together, $D[p]=[q,\_,\_]::[x,\_,\_]::L_{3}$ $D[p]=[F_{4},S_{4},A_{4}]::[F_{3},S_{3},A_{3}]::K_{2}$ $\land (S_{3}\implies (\operatorname {equate} [A_{3},f]\land V[F_{3}]=A_{3}))\land D[F_{3}]=D[f]$ $\land (S_{4}\implies (\operatorname {equate} [A_{4},p]\land V[F_{4}]=A_{4}))\land D[F_{4}]=D[p]$ $D[q]=[F_{7},S_{7},A_{7}]::[F_{6},S_{6},A_{6}]::K_{5}$ $(S_{6}\implies (\operatorname {equate} [A_{6},x]\land V[F_{6}]=A_{6}))\land D[F_{6}]=D[x]$ $(S_{7}\implies (\operatorname {equate} [A_{7},q]\land V[F_{7}]=A_{7}))\land D[F_{7}]=D[q]$ From the two definitions for $D[p]$ ; $F_{4}=q$ $F_{3}=x$ so $D[p]=[q,S_{4},A_{4}]::[x,S_{3},A_{3}]::K_{2}$ $(S_{3}\implies (\operatorname {equate} [A_{3},f]\land V[x]=A_{3}))\land D[x]=D[f]$ $(S_{4}\implies (\operatorname {equate} [A_{4},p]\land V[q]=A_{4}))\land D[q]=D[p]$ Using $D[q]=D[p]$ and $D[p]=[F_{7},S_{7},A_{7}]::[F_{6},S_{6},A_{6}]::K_{5}$ $(S_{6}\implies (\operatorname {equate} [A_{6},x]\land V[F_{6}]=A_{6}))\land D[F_{6}]=D[x]$ $(S_{7}\implies (\operatorname {equate} [A_{7},q]\land V[F_{7}]=A_{7}))\land D[F_{7}]=D[q]$ by comparing with the above, $F_{7}=q,F_{6}=x,A_{3}=A_{6},A_{4}=A_{7},S_{3}=S_{6},S_{4}=S_{7}$ so, $V[x]=A_{3}$ $V[q]=A_{4}$ in, $S_{3}\implies A_{3}=f$ $S_{3}\implies (A_{3}=x\lor A_{3}=v[x])$ reduces to, $S_{3}\implies A_{3}=f$ also, $S_{4}\implies A_{4}=p$ $S_{4}\implies (A_{4}=q\lor A_{4}=v[q])$ reduces to, $S_{4}\implies A_{4}=p$ So the parameter list for p is effectively; $D[p]=[q,\_,p]::[x,\_,f]::\_$ |

#### Drop parameters

Use the information obtained by Build parameter lists to drop actual parameters that are no longer required. *drop-params* has the parameters,

- The lambda expression in which the parameters are to be dropped.
- The mapping of variable names to parameter lists (built in Build parameter lists).
- The set of variables free in the lambda expression.
- The returned parameter list. A parameter used internally in the algorithm.

**Abstraction**

$\operatorname {drop-params} [(\lambda N.S)\ L,D,V,R]\equiv (\lambda N.\operatorname {drop-params} [S,D,F,R])\ \operatorname {drop-formal} [D[N],L,F]$

where,

$F=FV[(\lambda N.S)\ L]$

$\operatorname {drop-params} [\lambda N.S,D,V,R]\equiv (\lambda N.\operatorname {drop-params} [S,D,F,R])$

where,

$F=FV[\lambda N.S]$

**Variable**

$\operatorname {drop-params} [N,D,V,D[N]]\equiv N$

For a function name or parameter start populating actual parameter list by outputting the parameter list for this name.

**Application** - An application (function call) is processed to extract

$(\operatorname {def} [F]\land \operatorname {ask} [S]\land FV[A]\subset V)\to \operatorname {drop-params} [E\ P,D,V,R]\equiv \operatorname {drop-params} [E,D,V,[F,S,A]::R]$

$\neg (\operatorname {def} [F]\land \operatorname {ask} [S]\land FV[A]\subset V)\to \operatorname {drop-params} [E\ P,D,V,R]\equiv \operatorname {drop-params} [E,D,V,[F,S,A]::R]\ \operatorname {drop-params} [P,D,V,\_]$

**Let** - Let expression.

$\operatorname {drop-params} [\operatorname {let} V:E\operatorname {in} L]\equiv \operatorname {let} V:\operatorname {drop-params} [E,D,FV[E],[]]\operatorname {in} \operatorname {drop-params} [L,D,FV[L],[]]$

**And** - For use in "let".

$\operatorname {drop-params} [E\land F,D,V,\_]\equiv \operatorname {drop-params} [E,D,V,\_]\land \operatorname {drop-params} [F,D,V,\_]$

| Drop parameters from applications |
|---|
| $\lambda g.\lambda n.n\ (g\ m\ p\ n)\ (g\ q\ p\ n)$ ConditionExpression $\operatorname {drop-param} [\lambda g.\lambda n.n\ (g\ m\ p\ n)\ (g\ q\ p\ n),D,\{p,q,m\},\_]$ $\lambda g.\operatorname {drop-param} [\lambda n.n\ (g\ m\ p\ n)\ (g\ q\ p\ n),D,\{p,q,m\},\_]$ $\neg (\operatorname {def} [F_{1}]\land ...)$ $\lambda g.\lambda n.\operatorname {drop-param} [n\ (g\ m\ p\ n),D,\{p,q,m\},[F_{1},S_{1},A_{1}]::\_]\ \operatorname {drop-param} [(g\ q\ p\ n),D,\{p,q,m\},\_]$ $\neg (\operatorname {def} [F_{2}]\land ...)$ $\lambda g.\lambda n.\operatorname {drop-param} [n\ ,D,\{p,q,m\},[F_{2},S_{2},A_{2}]::[F_{1},S_{1},A_{1}]::\_]\ \operatorname {drop-param} [(g\ m\ p\ n),D,\{p,q,m\},\_]\ \operatorname {drop-param} [(g\ q\ p\ n),D,\{p,q,m\},\_]$ $D[n]=[F_{2},S_{2},A_{2}]::[F_{1},S_{1},A_{1}]::\_]$ $\lambda g.\lambda n.n\ \operatorname {drop-param} [(g\ m\ p\ n),D,\{p,q,m\},\_]\ \operatorname {drop-param} [(g\ q\ p\ n),D,\{p,q,m\},\_]$ From the results of building parameter lists; $D[n]=[[\_,\_,(g\ m\ p\ n)],[\_,\_,(g\ q\ p\ n)]]$ so, $F_{1}=\_$ $F_{2}=\_$ so, $\operatorname {def} [F_{1}]=\operatorname {false}$ $\operatorname {def} [F_{2}]=\operatorname {false}$ $\operatorname {drop-param} [(g\ m\ p\ n),D,\{p,q,m\},\_]$ ConditionExpandedExpression $V=\{p,q,m\}$ $\operatorname {drop-param} [(g\ m\ p\ n),D,V,\_]$ $FV(A_{1})\not \subset \{p,q,m\}$ $n\not \subset \{p,q,m\}$ $\operatorname {drop-params} [g\ m\ p,D,V,[F_{1},S_{1},A_{1}]::\_]\ \operatorname {drop-params} [n,D,V,\_]$ $\operatorname {def} [F_{2}]\land \operatorname {ask} [S_{2}]\land FV[A_{2}]\subset V$ $\operatorname {def} [y]\land \operatorname {ask} [\_]\land FV[p]\subset \{p,q,m\}$ $\operatorname {drop-params} [g\ m,D,V,[F_{2},S_{2},A_{2}]::[F_{1},S_{1},A_{1}]::\_]\ \operatorname {drop-params} [n,D,V,\_]$ $\neg \operatorname {ask} [S_{3}]$ $\neg \operatorname {ask} [\operatorname {false} ]$ $\operatorname {drop-params} [g,D,V,[F_{3},S_{3},A_{3}]::[F_{2},S_{2},A_{2}]::[F_{1},S_{1},A_{1}]::\_]\ \operatorname {drop-params} [m,D,V,\_]\ \operatorname {drop-params} [n,D,V,\_]$ $D[g]=[[x,\operatorname {false} ,\_],[o,\_,p],[y,\_,n]]$ $=[F_{3},S_{3},A_{3}]::[F_{2},S_{2},A_{2}]::[F_{1},S_{1},A_{1}]::\_]$ $F_{3}=x,S_{3}=\operatorname {false} ,A_{3}=\_$ $F_{2}=o,S_{2}=\_,A_{2}=p$ $F_{1}=y,S_{1}=\_,A_{1}=n$ $g\ m\ n$ $\operatorname {drop-param} [(g\ q\ p\ n),D,\{p,q,m\},\_]$ ConditionExpandedExpression V = \{p, q, m\} $\operatorname {drop-param} [(g\ q\ p\ n),D,V,\_]$ $FV(A_{4})\not \subset V$ $n\not \subset \{p,q,m\}$ $\operatorname {drop-params} [g\ q\ p,D,V,[F_{4},S_{4},A_{4}]::\_]\ \operatorname {drop-params} [n,D,V,\_]$ $\operatorname {def} [F_{5}]\land \operatorname {ask} [S_{5}]\land FV[A_{5}]\subset V$ $\operatorname {def} [o]\land \operatorname {ask} [\_]\land p\subset \{p,q,m\})$ $\operatorname {drop-params} [g\ q,D,V,[F_{5},S_{5},A_{5}]::[F_{4},S_{4},A_{4}]::\_]\ \operatorname {drop-params} [n,D,V,\_]$ $\neg \operatorname {ask} [S-6]$ $\neg \operatorname {ask} [\operatorname {false} ]$ $\operatorname {drop-params} [g,D,V,[F_{6},S_{6},A_{6}]::[F_{5},S_{5},A_{5}]::[F_{4},S_{4},A_{4}]::\_]\ \operatorname {drop-params} [m,D,V,\_]\ \operatorname {drop-params} [n,D,V,\_]$ $D[g]=[[x,\operatorname {false} ,\_],[o,\_,p],[y,\_,n]]$ $=[F_{6},S_{6},A_{6}]::[F_{5},S_{5},A_{5}]::[F_{4},S_{4},A_{4}]::\_]$ $F_{6}=x,S_{6}=\operatorname {false} ,A_{6}=\_$ $F_{5}=o,S_{5}=\_,A_{5}=p$ $F_{4}=y,S_{4}=\_,A_{4}=n$ $g\ q\ n$ |

##### Drop formal parameters

*drop-formal* removes formal parameters, based on the contents of the drop lists. Its parameters are,

- The drop list,
- The function definition (lambda abstraction).
- The free variables from the function definition.

*drop-formal* is defined as,

1. $(\operatorname {ask} [S]\land FV[A]\subset V)\to \operatorname {drop-formal} [[F,S,A]::Z,\lambda F.Y,V]\equiv \operatorname {drop-formal} [[F,S,A]::Z,Y[F:=A],L]$
2. $\neg (\operatorname {ask} [S]\land FV[A]\subset V)\to \operatorname {drop-formal} [[F,S,A]::Z,\lambda F.Y,V]\equiv \lambda F.\operatorname {drop-formal} [[F,S,A]::Z,Y,V]$
3. $\operatorname {drop-formal} [Z,Y,V]\equiv Y$

Which can be explained as,

1. If all the actual parameters have the same value, and all the free variables of that value are available for definition of the function then drop the parameter, and replace the old parameter with its value.
2. else do not drop the parameter.
3. else return the body of the function.

| Condition | Expression |
|---|---|
| $\operatorname {false}$ | $\operatorname {drop-formal} [D,\lambda x.\lambda o.\lambda y.o\ x\ y,F]$ |
| $\operatorname {true} \land \{p\}\subset F$ | $\lambda x.\operatorname {drop-formal} [D,\lambda o.\lambda y.o\ x\ y,F]$ |
| $\neg (\operatorname {true} \land \{n\}\subset F$ ) | $\lambda x.\operatorname {drop-formal} [D,(\lambda y.o\ x\ y)[o:=p],F]$ |
|   | $\lambda x.\lambda y.\operatorname {drop-formal} [D,p\ x\ y,F]$ |
|   | $\lambda x.\lambda y.p\ x\ y$ |

### Example

Starting with the function definition of the Y-combinator,

$\operatorname {let} p\ f\ x=f\ (x\ x)\land q\ p\ f=(p\ f)\ (p\ f)\operatorname {in} q\ p\$

| Transformation | Expression |
|---|---|
|   | $\operatorname {let} p\ f\ x=f\ (x\ x)\land q\ p\ f=(p\ f)\ (p\ f)\operatorname {in} q\ p$ |
| *abstract* * 4 | $\operatorname {let} p=\lambda f.\lambda x.f\ (x\ x)\land q=\lambda p.\lambda f.(p\ f)\ (p\ f)\operatorname {in} q\ p$ |
| *lambda-abstract-tran* | $(\lambda q.(\lambda p.q\ p)\ (\lambda f.\lambda x.f\ (x\ x)))\ (\lambda p.\lambda f.(p\ f)\ (p\ f))$ |
| *sink-tran* | $(\lambda p.\lambda f.(p\ f)\ (p\ f))\ (\lambda f.\lambda x.f\ (x\ x))$ |
| *sink-tran* | $\lambda f.(\lambda p.(p\ f)\ (p\ f))\ (\lambda f.\lambda x.f\ (x\ x))$ |
| *drop-param* | $\lambda f.(\lambda p.p\ p)\ (\lambda x.f\ (x\ x))$ |
| *beta-redex* | $\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))\$ |

Which gives back the Y combinator,

$\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))$
