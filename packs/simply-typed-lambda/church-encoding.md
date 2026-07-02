---
title: "Church encoding"
source: https://en.wikipedia.org/wiki/Church_encoding
domain: simply-typed-lambda
license: CC-BY-SA-4.0
tags: simply typed lambda calculus, typing rule, type judgment, strong normalization
fetched: 2026-07-02
---

# Church encoding

In mathematics, **Church encoding** is a way of representing various types of data in the lambda calculus.

In the untyped lambda calculus the only primitive data type are functions, represented by lambda abstraction terms. Types that are usually considered primitive in other notations (such as integers, Booleans, pairs, lists, and tagged unions) are not natively present.

Hence the need arises to have ways to represent the data of these varying types by lambda terms, that is, by functions that are taking functions as their arguments and are returning functions as their results.

The **Church numerals** are a representation of the natural numbers using lambda notation. The method is named for Alonzo Church, who first encoded data in the lambda calculus this way. It can also be extended to represent other data types in the similar spirit.

This article makes occasional use of the alternative syntax for lambda abstraction terms, where λ*x*.λ*y*.λ*z*.*N* is abbreviated as λ*xyz*.*N*, as well as the two standard combinators, $I\equiv \lambda x.x$ and $K\equiv \lambda xy.x$ , as needed.


## Church pairs

Church pairs are the Church encoding of the pair (two-tuple) type. To have two things is to be able to supply them to any observer expecting of two things. The pair is thus represented as a function that takes a function argument. The pair itself does not decide what to do with the elements of the tuple. When given its argument it will apply the argument to the two components of the pair. The definition of the pair *constructor*, the *select first element* and the *select second element* functions in lambda calculus are,

${\begin{aligned}\operatorname {pair} &\equiv \lambda xy.\lambda z.z\ x\ y\\\operatorname {first} &\equiv \lambda p.p\ (\lambda xy.x)\\\operatorname {second} &\equiv \lambda p.p\ (\lambda xy.y)\end{aligned}}$

For example,

${\begin{aligned}&\operatorname {first} \ (\operatorname {pair} \ a\ b)\\=&\ (\lambda p.p\ (\lambda xy.x))\ ((\lambda xyz.z\ x\ y)\ a\ b)\\=&\ (\lambda p.p\ (\lambda xy.x))\ (\lambda z.z\ a\ b)\\=&\ (\lambda z.z\ a\ b)\ (\lambda xy.x)\\=&\ (\lambda xy.x)\ a\ b\\=&\ a\end{aligned}}$


## Church Booleans

*Church Booleans* encode the Boolean values *true* and *false.* Some programming languages use these as an implementation model for Boolean arithmetic; examples are Smalltalk and Pico.

Boolean logic embodies a *choice* between *two* alternatives. Thus the Church encodings of *true* and *false* are functions of two parameters:

- *true* chooses the first parameter ;
- *false* chooses the second parameter.

The two definitions in lambda calculus are:

${\begin{aligned}\operatorname {true} &\equiv \lambda a.\lambda b.a\ \ \ \ \ =\lambda a.\lambda b.\operatorname {first} \,(\operatorname {pair} a\ b)\\\operatorname {false} &\equiv \lambda a.\lambda b.b\ \ \ \ \ \,=\lambda a.\lambda b.\operatorname {second} \,(\operatorname {pair} a\ b)\end{aligned}}$

These definitions allow predicates (i.e. functions returning logical values) to directly act as *if-test* clauses, so that *if* operator is just an identity function, and thus can be omitted. Each logical value already acts as an *if*, performing a choice between its two arguments. A Boolean value applied to two values returns either the first or the second value. The expression

$\operatorname {test-clause} \ \operatorname {then-clause} \ \operatorname {else-clause}$

returns *then-clause* if *test-clause* is *true*, and *else-clause* if *test-clause* is *false*.

Because logical values like *true* and *false* choose their first or second argument, they can be combined to provide logical operators. Several implementations are usually possible, whether by directly manipulating parameters or by reducing to the more basic logical values. Here are the definitions, using the shortened notation as mentioned at the start of the article (*p*,*q* are predicates; *a*,*b* are general values):

${\begin{aligned}\operatorname {if} &=\lambda pab.p\ a\ b&&\ \\\operatorname {and} &=\lambda pq.p\ q\ p&&=\lambda pqab.p\ (q\ a\ b)\ b\\\operatorname {or} &=\lambda pq.p\ p\ q&&=\lambda pqab.p\ a\ (q\ a\ b)\\\operatorname {not} &=\lambda p.p\operatorname {false} \operatorname {true} &&=\lambda pab\ \ .p\ b\ a\\\operatorname {xor} &=\lambda pq.p\ (\operatorname {not} \ q)\ q&&=\lambda pqab.p\ (q\ b\ a)\ (q\ a\ b)\\\operatorname {nand} &=\lambda pq.\operatorname {not} \ (\operatorname {and} p\ q)&&=\lambda pqab.p\ (q\ b\ a)\ a\\\operatorname {implies} &=\lambda pq.\operatorname {or} \ (\operatorname {not} p)\ q&&=\lambda pqab.p\ (q\ a\ b)\ a\\\end{aligned}}$

Some examples:

${\begin{aligned}\operatorname {and} \operatorname {true} \operatorname {false} &=(\lambda p.\lambda q.p\ q\ p)\ \operatorname {true} \ \operatorname {false} \\&=\operatorname {true} \operatorname {false} \operatorname {true} \\&=(\lambda a.\lambda b.a)\operatorname {false} \operatorname {true} \\&=\operatorname {false} \\\\\operatorname {or} \operatorname {true} \operatorname {false} &=(\lambda p.\lambda q.p\ p\ q)\ (\lambda a.\lambda b.a)\ (\lambda a.\lambda b.b)\\&=(\lambda a.\lambda b.a)\ (\lambda a.\lambda b.a)\ (\lambda a.\lambda b.b)\\&=(\lambda a.\lambda b.a)\\&=\operatorname {true} \\\\\operatorname {not} _{2}\ \operatorname {true} &=(\lambda p.\lambda a.\lambda b.p\ b\ a)(\lambda a.\lambda b.a)\\&=\lambda a.\lambda b.(\lambda a.\lambda b.a)\ b\ a\\&=\lambda a.\lambda b.(\lambda c.b)\ a\\&=\lambda a.\lambda b.b\\&=\operatorname {false} \\\\\operatorname {not} _{1}\ \operatorname {true} &=(\lambda p.\,p\ (\lambda a.\lambda b.\,b)\ (\lambda a.\lambda b.\,a))\ (\lambda a.\lambda b.\,a)\\&=(\lambda a.\lambda b.\,a)\ (\lambda a.\lambda b.\,b)\ (\lambda a.\lambda b.\,a)\\&=(\lambda b.\,(\lambda a.\lambda b.\,b))\ (\lambda a.\lambda b.\,a)\\&=\lambda a.\lambda b.\,b\\&=\operatorname {false} \end{aligned}}$


## Church numerals

Church numerals are the representations of natural numbers under Church encoding. The higher-order function that represents natural number *n* is a function that maps any function f to its *n*-fold composition. In simpler terms, a numeral represents the number by applying any given function that number of times in sequence, starting from any given starting value:

$n:f\mapsto f^{\circ n}$

$f^{\circ n}(x)=(\underbrace {f\circ f\circ \ldots \circ f} _{n{\text{ times}}})\,(x)=\underbrace {f(f(\ldots (f} _{n{\text{ times}}}\,(x))\ldots ))$

Church encoding is thus a *unary* encoding of natural numbers, corresponding to simple counting. Each Church numeral achieves this by construction.

All Church numerals are functions that take two parameters. Church numerals **0**, **1**, **2**, ..., are defined as follows in the lambda calculus:

Starting with

0

not applying the function at all, proceed with

1

applying the function once,

2

applying the function twice in a row,

3

applying the function three times in a row, etc.

:

${\begin{array}{r|l|l}{\text{Number}}&{\text{Function definition}}&{\text{Lambda expression}}\\\hline 0&0\ f\ x=x&0=\lambda f.\lambda x.x\\1&1\ f\ x=f\ x&1=\lambda f.\lambda x.f\ x\\2&2\ f\ x=f\ (f\ x)&2=\lambda f.\lambda x.f\ (f\ x)\\3&3\ f\ x=f\ (f\ (f\ x))&3=\lambda f.\lambda x.f\ (f\ (f\ x))\\\vdots &\vdots &\vdots \\n&n\ f\ x=f^{\circ n}\ x&n=\lambda f.\lambda x.f^{\circ n}\ x\end{array}}$

The Church numeral **3** is a chain of three applications of any given function in sequence, starting from some value. The supplied function is first applied to a supplied argument and then successively to its own result. The end result is not the number 3 (unless the supplied parameter happens to be 0 and the function is a successor function). The function itself, and not its end result, is the Church numeral **3**. The Church numeral **3** means simply to do something three times. It is an ostensive demonstration of what is meant by "three times".

### Calculation with Church numerals

Arithmetic operations on numbers produce numbers as their results. In Church encoding, these operations are represented by lambda abstractions which, when applied to Church numerals representing the operands, beta-reduce to the Church numerals representing the results.

Church representation of addition, $\operatorname {plus} (m,n)=m+n$ , uses the identity $f^{\circ (m+n)}(x)=(f^{\circ m}\circ f^{\circ n})(x)=f^{\circ m}(f^{\circ n}(x))$ :

$\operatorname {plus} \equiv \lambda mn.\lambda fx.m\ f\ (n\ f\ x)$

The successor operation, $\operatorname {succ} (n)=n+1$ , is obtained by β-reducing the expression " $\operatorname {plus} \ 1$ ":

$\operatorname {succ} \equiv \lambda n.\lambda fx.f\ (n\ f\ x)$

Multiplication, $\operatorname {mult} (m,n)=m*n$ , uses the identity $f^{\circ (m*n)}(x)=(f^{\circ n})^{\circ m}(x)$ :

$\operatorname {mult} \equiv \lambda mn.\lambda fx.m\ (n\ f)\ x$

Thus $b\ (b\ f)\equiv (\operatorname {mult} b\ b)\ f$ and $b\ (b\ (b\ f))\equiv (\operatorname {mult} b\ (\operatorname {mult} b\ b))\ f$ , and so by the virtue of Church encoding expressing the *n*-fold composition, the exponentiation operation $\operatorname {exp} (b,n)=b^{n}$ is given by

$\operatorname {exp} \equiv \lambda bn.n\ b\equiv \lambda bnfx.n\ b\ f\ x$

The predecessor operation $\operatorname {pred} (n)$ is a little bit more involved. We need to devise an operation that when repeated $n+1$ times will result in n applications of the given function f . This is achieved by using the identity function instead, one time only, and then switching back to f :

$\operatorname {pred} \equiv \lambda nfx.n\ (\lambda ri.i\ (r\ f))\ (\lambda f.x)\ I$

As previously mentioned, I is the identity function, $\lambda x.x$ . The variable name r is chosen as a mnemonic for "recursive result." This definition employs an additional argument to use the state-passing paradigm, since lambda calculus lacks mutation (so nothing can be changed, only replaced). See below for the detailed explanation.

This suggests implementing e.g. halving and factorial functions in the similar state-passing fashion,

${\begin{aligned}\operatorname {half} &\equiv \lambda nfx.n\ (\lambda rab.a\ (r\ b\ a))\ (\lambda ab.x)\ I\ f\\\operatorname {fact} &\equiv \lambda nf.n\ (\lambda ra.a\ (r\ (\operatorname {succ} a)))\ (\lambda a.f)\ 1\end{aligned}}$

For example, $\operatorname {pred} 4\ f\ x\,$ beta-reduces to $I(f\ (f\ (f\ x)))$ , $\operatorname {half} \ 5\ f\ x\,$ beta-reduces to $I\ (f\ (I\ (f\ (I\ x))))$ , and $\operatorname {fact} 4\,f\,$ beta-reduces to $1\ (2\ (3\ (4\ f)))$ .

Subtraction, $minus(m,n)=m-n$ , is expressed by repeated application of the predecessor operation a given number of times, just like addition can be expressed by repeated application of the successor operation a given number of times, etc.:

${\begin{aligned}(-)&\equiv \lambda mn.n\,\operatorname {pred} \,m\\(+)&\equiv \lambda mn.n\,\operatorname {succ} \,m\\(\times )&\equiv \lambda mn.n\ ((+)\ m)\ 0\\\operatorname {exp} &\equiv \lambda mn.n\ ((\times )\ m)\ 1\ \ \ \ \ \ \ \ \ \ \ \{-\ \ m^{n}\ -\}\\(\uparrow \uparrow )&\equiv \lambda mn.n\ (\operatorname {exp} \,m)\ 1\ \ \ \ \ \ \ \{-\ m\uparrow \uparrow n\ -\}\\\uparrow ^{k}&\equiv k\ (\lambda fmn.n\ (f\ m)\ 1)\ (\times )\\\end{aligned}}$

$(\uparrow \uparrow )$ is the tetration operation, $m\uparrow \uparrow 3=m^{(m^{(m^{1})})}$ , and $\uparrow ^{k}$ is Knuth's k  th arrow in general.

Similarly to the factorial definition above, tetration can also be defined by using the intrinsic properties of the Church encoding, creating the "code" expression for it and letting the Church numerals themselves do the rest:

${\begin{aligned}\operatorname {tet} &\equiv \lambda mn.n\ (\lambda r.r\ m)\ 1\end{aligned}}$

Here, again, $\operatorname {tet} \,m\ 3=1\ m\ m\ m=m^{(m^{(m^{1})})}$ .

### Direct subtraction and division

Just as addition as repeated successor has its counterpart in the direct style, so can subtraction be expressed directly and more efficiently as well:

${\begin{aligned}\operatorname {minus} \equiv \lambda &mnfx.\\&m\ (\lambda rq.q\ r)\ (\lambda q.x)\\&(n\ (\lambda qr.r\ q)\ (\operatorname {Y} \ (\lambda qr.f\ (r\ q))))\end{aligned}}$

For example, $\operatorname {minus} \ 6\ 3\ f\ x$ reduces to an equivalent of $f\ (2\ f\ x)$ .

This also gives another predecessor version, beta-reducing $\lambda m.\operatorname {minus} \ m\ 1$  :

${\begin{aligned}\operatorname {pred'} \equiv \lambda mfx.m\ &(\lambda rq.q\ r)\ (\lambda q.x)\\&(\lambda r.r\ (\operatorname {Y} \ (\lambda qr.f\ (r\ q))))\end{aligned}}$

Direct definition of division is given quite similarly as

${\begin{aligned}\operatorname {div} \equiv \lambda &mnfx.\\&m\ (\lambda rq.q\ r)\ (\lambda q.x)\\&(\operatorname {Y} \ (\lambda q.n\ (\lambda qr.r\ q)\ (\lambda r.f\ (r\ q))\ (\lambda x.x)))\end{aligned}}$

The application to $(\lambda x.x)$ achieves subtraction by 1 while creating a cycle of actions repeatedly emitting an f after $n-1$ steps.

Instead of $\operatorname {Y}$ , $(\lambda q.m\,q\,x)$ can also be used in each of the three definitions above.

### Table of functions on Church numerals

| Function | Algebra | Identity | Function definition | Lambda expressions |   |
|---|---|---|---|---|---|
| Successor | $n+1$ | $f^{\circ (n+1)}=f\circ f^{\circ n}$ | $\operatorname {succ} \ n\ f\ x=f\ (n\ f\ x)$ | $\lambda nfx.f\ (n\ f\ x)$ | ... |
| Addition | $m+n$ | $f^{\circ (m+n)}=f^{\circ m}\circ f^{\circ n}$ | $\operatorname {plus} \ m\ n\ f\ x=m\ f\ (n\ f\ x)$ | $\lambda mnfx.m\ f\ (n\ f\ x)$ | $\lambda mn.n\operatorname {succ} m$ |
| Multiplication | $m*n$ | $f^{\circ (m*n)}=(f^{\circ m})^{\circ n}$ | $\operatorname {multiply} \ m\ n\ f\ x=m\ (n\ f)\ x$ | $\lambda mnfx.m\ (n\ f)\ x$ | $\lambda mnf.m\ (n\ f)$ |
| Exponentiation | $b^{n}$ | $b^{\circ n}=(\operatorname {mult} b)^{\circ n}$ | $\operatorname {exp} \ b\ n\ f\ x=n\ b\ f\ x$ | $\lambda bnfx.n\ b\ f\ x$ | $\lambda bn.n\ b$ |
| Predecessor | $n-1$ | $first((\langle i,j\rangle \mapsto \langle j,f\circ j\rangle )^{\circ n}\langle I,I\rangle )=f^{\circ (n-1)}$ | $\operatorname {pred} (n+1)\ f\ x=I\ (n\ f\ x)$ | $\lambda nfx.n\ (\lambda ri.i\ (r\ f))\ (\lambda f.x)\ (\lambda u.u)$ |   |
| Subtraction (Monus) | $m-n$ | $m-n=pred^{\circ n}(m)$ | $\operatorname {minus} \ m\ n=n\operatorname {pred} m$ | ... | $\lambda mn.n\operatorname {pred} m$ |

**Notes**:

1. In the Church encoding, $\operatorname {pred} (0)=0$ $m\leq n\to m-n=0$

### Predecessor function

The predecessor function is given as

$\operatorname {pred} \equiv \lambda nfx.n\ (\lambda ri.i\ (r\ f))\ (\lambda f.x)\ (\lambda u.u)$

This encoding essentially uses the identity

$first(\ (\langle i,j\rangle \mapsto \langle j,f\circ j\rangle )^{\circ n}\langle I,I\rangle \ )={\begin{cases}I&{\mbox{if }}n=0,\\f^{\circ (n-1)}&{\mbox{otherwise}}\end{cases}}$

or

$first(\ (\langle x,y\rangle \mapsto \langle y,f(y)\rangle )^{\circ n}\langle x,x\rangle \ )={\begin{cases}x&{\mbox{if }}n=0,\\f^{\circ (n-1)}(x)&{\mbox{otherwise}}\end{cases}}$

#### An explanation of pred

The idea here is as follows. The only thing known to the Church numeral $\operatorname {pred} n$ is the numeral n itself. Given two arguments f and x , as usual, the only thing it can do is to apply that numeral to the two arguments, somehow modified so that the *n*-long chain of applications thus created will have one (specifically, leftmost) f in the chain replaced by the identity function:

${\begin{aligned}f^{\circ (n-1)}(x)&=\underbrace {I\ (\underbrace {f(f(\ldots (f} _{{n-1}{\text{ times}}}} _{n{\text{ times}}}\,(x))\ldots )))=(Xf)^{\circ n}(Z\,x)\ A\\&=\underbrace {Xf\ (Xf\ (\ldots (Xf} _{{n}{\text{ times}}}\,(Z\,x))\ldots ))\ A\\&=X\ f\ r_{1}\ A_{1}\,\,\,\{-\ and\ it\ must\ be\ equal\ to:\ -\}\\&=I\ (X\ f\ r_{2}\ A_{2})\\&=I\ (f\ (X\ f\ r_{3}\ A_{3}))\\&=I\ (f\ (f\ (X\ f\ r_{4}\ A_{4})))\\&\ldots \\&=I\ (f\ (f\ \ldots (X\ f\ r_{n}\ A_{n})\ldots ))\\&=\underbrace {I\ (f\ (f\ \ldots (f} _{n{\text{ times}}}\ (Z\ x\ A_{n+1}))\ldots ))\\\end{aligned}}$

Here $Xf$ is the modified f , and $Z\,x$ is the modified x . Since $Xf$ itself can not be changed, its behavior can only be modified through an additional argument, A .

The goal is achieved, then, by passing that additional argument A along *from the outside in*, while modifying it as necessary, with the definitions

${\begin{aligned}A_{1}\,\,\,\,\,\,\,\,\,\,&=\,I\\A_{\,i>1}\,\,\,\,\,&=\,f\\Z\ x\ f\,\,\,\,&=x=K\ x\ f\\X\ f\ r\ A_{i}&=A_{i}\ (r\ A_{i+1})\,\,\,\,\,\,\{-\ i.e.,\ -\}\\X\ f\ r\ i\,\,\,\,\,&=i\ (r\ f)\end{aligned}}$

Which is exactly what we have in the $\operatorname {pred}$ definition's lambda expression.

Now it is easy enough to see that

${\begin{aligned}\operatorname {pred} \ (\operatorname {succ} \ n)\ f\ x&=\operatorname {succ} \ n\ (Xf)\ (K\ x)\ I\\&=X\ f\ (n\ (X\ f)\ (K\ x))\ I\\&=I\ (n\ (Xf)\ (K\ x)\ \,\,f\,\,\,)\\&=\ \ldots \\&=I\ (f\ (f\ \ldots (f\ (K\ x\,\,f\,\,))\ldots ))\\&=I\ (n\ f\ x)\\&=n\ f\ x\ \end{aligned}}$

${\begin{aligned}\operatorname {pred} \ 0\ f\ x&=\ 0\ (Xf)\ (K\ x)\ I\\&=\ K\ x\ I\\&=\ x\\&=\ 0\ f\ x\end{aligned}}$

i.e. by eta-contraction and then by induction, it holds that

${\begin{aligned}&\operatorname {pred} \ (\operatorname {succ} \ n)&&=\ n\\&\operatorname {pred} \ 0&&=\ 0\\&\operatorname {pred} \ (\operatorname {pred} \ 0)&&=\ \operatorname {pred} \ 0\ =\ 0\\&\ldots \end{aligned}}$

and so on.

#### Defining pred through pairs

The identity above may be coded with the explicit use of pairs. It can be done in several ways, for instance,

${\begin{aligned}\operatorname {f} =&\ \lambda p.\ \operatorname {pair} \ (\operatorname {second} \ p)\ (\operatorname {succ} \ (\operatorname {second} \ p))\\\operatorname {pred} _{2}=&\ \lambda n.\ \operatorname {first} \ (n\ \operatorname {f} \ (\operatorname {pair} \ 0\ 0))\\\end{aligned}}$

The expansion for $\operatorname {pred} _{2}3$ is:

${\begin{aligned}\operatorname {pred} _{2}3=&\ \operatorname {first} \ (\operatorname {f} \ (\operatorname {f} \ (\operatorname {f} \ (\operatorname {pair} \ 0\ 0))))\\=&\ \operatorname {first} \ (\operatorname {f} \ (\operatorname {f} \ (\operatorname {pair} \ 0\ 1)))\\=&\ \operatorname {first} \ (\operatorname {f} \ (\operatorname {pair} \ 1\ 2))\\=&\ \operatorname {first} \ (\operatorname {pair} \ 2\ 3)\\=&\ 2\end{aligned}}$

This is a simpler definition to devise but leads to a more complex lambda expression,

${\begin{aligned}\operatorname {pred} _{2}\equiv \lambda n.n\ &(\lambda p.p\ (\lambda abh.h\ b\ (\operatorname {succ} \ b)))\,\,(\lambda h.h\ 0\ 0)\,\,(\lambda ab.a)\end{aligned}}$

Pairs in the lambda calculus are essentially just extra arguments, whether passing them inside out like here, or from the outside in as in the original $\operatorname {pred}$ definition. Another encoding follows the second variant of the predecessor identity directly,

${\begin{aligned}\operatorname {pred} _{3}\equiv \lambda nfx.n\ &(\lambda p.p\ (\lambda abh.h\ b\ (f\ b)))\,\,(\lambda h.h\ x\ x)\,\,(\lambda ab.a)\end{aligned}}$

This way it is already quite close to the original, "outside-in" $\operatorname {pred}$ definition, also creating the chain of f s like it does, only in a bit more wasteful way still. But it is very much less wasteful than the previous, $\operatorname {pred} _{2}$ definition here. Indeed if we trace its execution we arrive at the new, even more streamlined, yet fully equivalent, definition

${\begin{aligned}\operatorname {pred} _{4}\equiv \lambda nfx.n\ &(\lambda rab.r\ b\ (f\ b))\,K\ x\ x\end{aligned}}$

which makes it fully clear and apparent that this is all about just argument modification and passing. Its reduction proceeds as

${\begin{aligned}\operatorname {pred} _{4}3\ f\ x&=\ (..(..(..K)))\ x\ \,x\\&=\ (..(..K))\,\,\,\,\,\,\,x\ \,\,(f\ x)\\&=\ (..K)\,\,\,\,\,\,(f\ x)\ \,\,(f\ (f\ x))\\&=\ K\,\,\,\,(f\ (f\ x))\ \,\,(f\ (f\ (f\ x)))\\&=\ f\ (f\ x)\\\end{aligned}}$

clearly showing what is going on. Still, the original $\operatorname {pred}$ is much preferable since it's working in the top-down manner and is thus able to stop right away if the user-supplied function f is short-circuiting. The top-down approach is also used with other definitions like

${\begin{aligned}\operatorname {pred} _{5}\equiv \lambda nfx.n\ &(\lambda rab.a\ (r\ b\ b))\,(\lambda ab.x)\ I\ f\\\operatorname {third} \equiv \lambda nfx.n\ &(\lambda rabc.a\ (r\ b\ c\ a))\,(\lambda abc.x)\ I\ I\ f\\\operatorname {thirdRounded} \equiv \lambda nfx.n\ &(\lambda rabc.a\ (r\ b\ c\ a))\,(\lambda abc.x)\ I\ f\ I\\\operatorname {twoThirds} \equiv \lambda nfx.n\ &(\lambda rabc.a\ (r\ b\ c\ a))\,(\lambda abc.x)\ I\ f\ f\\\operatorname {factorial} \equiv \lambda nfx.n\ &(\lambda ra.a\ (r\ (\operatorname {succ} a)))\,(\lambda a.f)\ 1\ x\\\end{aligned}}$

### Division via general recursion

Division of natural numbers may be implemented by,

$n/m=\operatorname {if} \ n\geq m\ \operatorname {then} \ 1+(n-m)/m\ \operatorname {else} \ 0$

Calculating $n-m$ with $\lambda nm.m\,\operatorname {pred} \,n$ takes many beta reductions. Unless doing the reduction by hand, this doesn't matter that much, but it is preferable to not have to do this calculation twice (unless the direct subtraction definition is used, see above). The simplest predicate for testing numbers is *IsZero* so consider the condition.

$\operatorname {IsZero} \ (\operatorname {minus} \ n\ m)$

But this condition is equivalent to $n\leq m$ , not $n<m$ . If this expression is used then the mathematical definition of division given above is translated into function on Church numerals as,

$\operatorname {divide1} \ n\ m\ f\ x=(\lambda d.\operatorname {IsZero} \ d\ (0\ f\ x)\ (f\ (\operatorname {divide1} \ d\ m\ f\ x)))\ (\operatorname {minus} \ n\ m)$

As desired, this definition has a single call to $\operatorname {minus} \ n\ m$ . However the result is that this formula gives the value of $(n-1)/m$ .

This problem may be corrected by adding 1 to *n* before calling *divide*. The definition of *divide* is then,

$\operatorname {divide} \ n=\operatorname {divide1} \ (\operatorname {succ} \ n)$

*divide1* is a recursive definition. The Y combinator may be used to implement the recursion. Create a new function called *div* by;

- In the left hand side $\operatorname {divide1} \rightarrow \operatorname {div} \ c$
- In the right hand side $\operatorname {divide1} \rightarrow c$

to get,

$\operatorname {div} =\lambda c.\lambda n.\lambda m.\lambda f.\lambda x.(\lambda d.\operatorname {IsZero} \ d\ (0\ f\ x)\ (f\ (c\ d\ m\ f\ x)))\ (\operatorname {minus} \ n\ m)$

Then,

$\operatorname {divide} =\lambda n.\operatorname {divide1} \ (\operatorname {succ} \ n)$

where,

${\begin{aligned}\operatorname {divide1} &=Y\ \operatorname {div} \\\operatorname {succ} &=\lambda n.\lambda f.\lambda x.f\ (n\ f\ x)\\Y&=\lambda f.(\lambda x.f\ (x\ x))\ (\lambda x.f\ (x\ x))\\0&=\lambda f.\lambda x.x\\\operatorname {IsZero} &=\lambda n.n\ (\lambda x.\operatorname {false} )\ \operatorname {true} \end{aligned}}$

${\begin{aligned}\operatorname {true} &\equiv \lambda a.\lambda b.a\\\operatorname {false} &\equiv \lambda a.\lambda b.b\end{aligned}}$

${\begin{aligned}\operatorname {minus} &=\lambda m.\lambda n.n\operatorname {pred} m\\\operatorname {pred} &=\lambda n.\lambda f.\lambda x.n\ (\lambda g.\lambda h.h\ (g\ f))\ (\lambda u.x)\ (\lambda u.u)\end{aligned}}$

Gives,

$\scriptstyle \operatorname {divide} =\lambda n.((\lambda f.(\lambda x.x\ x)\ (\lambda x.f\ (x\ x)))\ (\lambda c.\lambda n.\lambda m.\lambda f.\lambda x.(\lambda d.(\lambda n.n\ (\lambda x.(\lambda a.\lambda b.b))\ (\lambda a.\lambda b.a))\ d\ ((\lambda f.\lambda x.x)\ f\ x)\ (f\ (c\ d\ m\ f\ x)))\ ((\lambda m.\lambda n.n(\lambda n.\lambda f.\lambda x.n\ (\lambda g.\lambda h.h\ (g\ f))\ (\lambda u.x)\ (\lambda u.u))m)\ n\ m)))\ ((\lambda n.\lambda f.\lambda x.f\ (n\ f\ x))\ n)$

Or as text, using \ for λ,

```
divide = (\n.((\f.(\x.x x) (\x.f (x x))) (\c.\n.\m.\f.\x.(\d.(\n.n (\x.(\a.\b.b)) (\a.\b.a)) d ((\f.\x.x) f x) (f (c d m f x))) ((\m.\n.n (\n.\f.\x.n (\g.\h.h (g f)) (\u.x) (\u.u)) m) n m))) ((\n.\f.\x. f (n f x)) n))
```

For example, 9/3 is represented by

```
divide (\f.\x.f (f (f (f (f (f (f (f (f x))))))))) (\f.\x.f (f (f x)))
```

Using a lambda calculus calculator, the above expression reduces to 3, using normal order.

```
\f.\x.f (f (f (x)))
```

### Predicates

A *predicate* is a function that returns a Boolean value. The most fundamental predicate on Church numerals is $\operatorname {IsZero}$ , which returns $\operatorname {true}$ if its argument is the Church numeral 0 , and $\operatorname {false}$ otherwise:

$\operatorname {IsZero} =\lambda n.n\ (\lambda x.\operatorname {false} )\ \operatorname {true}$

The following predicate tests whether the first argument is less-than-or-equal-to the second:

$\operatorname {LEQ} =\lambda m.\lambda n.\operatorname {IsZero} \ (\operatorname {minus} \ m\ n)$

Because of the identity

$x=y\equiv (x\leq y\land y\leq x)$

the test for equality can be implemented as

$\operatorname {EQ} =\lambda m.\lambda n.\operatorname {and} \ (\operatorname {LEQ} \ m\ n)\ (\operatorname {LEQ} \ n\ m)$

### In programming languages

Most real-world languages have support for machine-native integers; the *church* and *unchurch* functions convert between nonnegative integers and their corresponding Church numerals. The functions are given here in Haskell, where the `\` corresponds to the λ of Lambda calculus. Implementations in other languages are similar.

```mw
type Church a = (a -> a) -> a -> a

church :: Integer -> Church Integer
church 0 = \f -> \x -> x
church n = \f -> \x -> f (church (n-1) f x)

unchurch :: Church Integer -> Integer
unchurch cn = cn (+ 1) 0
```


## Signed numbers

One simple approach for extending Church Numerals to signed numbers is to use a Church pair, containing Church numerals representing a positive and a negative value. The integer value is the difference between the two Church numerals.

A natural number is converted to a signed number by,

$\operatorname {convert} _{s}=\lambda x.\operatorname {pair} \ x\ 0$

Negation is performed by swapping the values.

$\operatorname {neg} _{s}=\lambda x.\operatorname {pair} \ (\operatorname {second} \ x)\ (\operatorname {first} \ x)$

The integer value is more naturally represented if one of the pair is zero. The *OneZero* function achieves this condition,

$\operatorname {OneZero} =\lambda x.\operatorname {IsZero} \ (\operatorname {first} \ x)\ x\ (\operatorname {IsZero} \ (\operatorname {second} \ x)\ x\ (\operatorname {OneZero} \ (\operatorname {pair} \ (\operatorname {pred} \ (\operatorname {first} \ x))\ (\operatorname {pred} \ (\operatorname {second} \ x)))))$

The recursion may be implemented using the Y combinator,

$\operatorname {OneZ} =\lambda c.\lambda x.\operatorname {IsZero} \ (\operatorname {first} \ x)\ x\ (\operatorname {IsZero} \ (\operatorname {second} \ x)\ x\ (c\ (\operatorname {pair} \ (\operatorname {pred} \ (\operatorname {first} \ x))\ (\operatorname {pred} \ (\operatorname {second} \ x)))))$

$\operatorname {OneZero} =Y\operatorname {OneZ}$

### Plus and minus

Addition is defined mathematically on the pair by,

$x+y=[x_{p},x_{n}]+[y_{p},y_{n}]=x_{p}-x_{n}+y_{p}-y_{n}=(x_{p}+y_{p})-(x_{n}+y_{n})=[x_{p}+y_{p},x_{n}+y_{n}]$

The last expression is translated into lambda calculus as,

$\operatorname {plus} _{s}=\lambda x.\lambda y.\operatorname {OneZero} \ (\operatorname {pair} \ (\operatorname {plus} \ (\operatorname {first} \ x)\ (\operatorname {first} \ y))\ (\operatorname {plus} \ (\operatorname {second} \ x)\ (\operatorname {second} \ y)))$

Similarly subtraction is defined,

$x-y=[x_{p},x_{n}]-[y_{p},y_{n}]=x_{p}-x_{n}-y_{p}+y_{n}=(x_{p}+y_{n})-(x_{n}+y_{p})=[x_{p}+y_{n},x_{n}+y_{p}]$

giving,

$\operatorname {minus} _{s}=\lambda x.\lambda y.\operatorname {OneZero} \ (\operatorname {pair} \ (\operatorname {plus} \ (\operatorname {first} \ x)\ (\operatorname {second} \ y))\ (\operatorname {plus} \ (\operatorname {second} \ x)\ (\operatorname {first} \ y)))$

### Multiply and divide

Multiplication may be defined by,

$x*y=[x_{p},x_{n}]*[y_{p},y_{n}]=(x_{p}-x_{n})*(y_{p}-y_{n})=(x_{p}*y_{p}+x_{n}*y_{n})-(x_{p}*y_{n}+x_{n}*y_{p})=[x_{p}*y_{p}+x_{n}*y_{n},x_{p}*y_{n}+x_{n}*y_{p}]$

The last expression is translated into lambda calculus as,

$\operatorname {mult} _{s}=\lambda x.\lambda y.\operatorname {pair} \ (\operatorname {plus} \ (\operatorname {mult} \ (\operatorname {first} \ x)\ (\operatorname {first} \ y))\ (\operatorname {mult} \ (\operatorname {second} \ x)\ (\operatorname {second} \ y)))\ (\operatorname {plus} \ (\operatorname {mult} \ (\operatorname {first} \ x)\ (\operatorname {second} \ y))\ (\operatorname {mult} \ (\operatorname {second} \ x)\ (\operatorname {first} \ y)))$

A similar definition is given here for division, except in this definition, one value in each pair must be zero (see *OneZero* above). The *divZ* function allows us to ignore the value that has a zero component.

$\operatorname {divZ} =\lambda x.\lambda y.\operatorname {IsZero} \ y\ 0\ (\operatorname {divide} \ x\ y)$

*divZ* is then used in the following formula, which is the same as for multiplication, but with *mult* replaced by *divZ*.

$\operatorname {divide} _{s}=\lambda x.\lambda y.\operatorname {pair} \ (\operatorname {plus} \ (\operatorname {divZ} \ (\operatorname {first} \ x)\ (\operatorname {first} \ y))\ (\operatorname {divZ} \ (\operatorname {second} \ x)\ (\operatorname {second} \ y)))\ (\operatorname {plus} \ (\operatorname {divZ} \ (\operatorname {first} \ x)\ (\operatorname {second} \ y))\ (\operatorname {divZ} \ (\operatorname {second} \ x)\ (\operatorname {first} \ y)))$


## Rational and real numbers

Rational and computable real numbers may also be encoded in lambda calculus. Rational numbers may be encoded as a pair of signed numbers. Computable real numbers may be encoded by a limiting process that guarantees that the difference from the real value differs by a number which may be made as small as we need. The references given describe software that could, in theory, be translated into lambda calculus. Once real numbers are defined, complex numbers are naturally encoded as a pair of real numbers.

The data types and functions described above demonstrate that any data type or calculation may be encoded in lambda calculus. This is the Church–Turing thesis.


## List encodings

A list contains some items in order. The basic operations on lists are:

| Function | Description |
|---|---|
| *nil* | Construct an empty list |
| *isnil* | Test if list is empty |
| *cons* | Prepend a given value to a (possibly empty) list |
| *head* | Get the first element of the list |
| *tail* | Get the rest of the list |
| *singleton* | Create a list containing one given element |
| *append* | Append two lists together |
| *fold* | Fold the list with the given "plus" and "zero" |

A representation of lists should provide ways to implement these operations.

The archetypal lambda calculus representation of lists is Church List encoding. It represents lists as right folds, as functions to return the results of folding over the list with user-supplied arguments.

It follows the paradigm of "a thing is the result of its observation". No matter the concrete implementation, folding a given list of values results in the same result. This provides an abstract view at what a list is. Church List encoding is such a mechanism.

On the other hand, seen more concretely, lists can be represented as a sequence of linked list nodes.

What follows are four different representations of lists:

- Church lists – right fold representation.
- Two Church pairs for each list node.
- One Church pair for each list node.
- Scott encoding.

### Church lists – *right fold* representation

This is the original Church encoding for lists. A list is represented by a binary function, that, when supplied with two arguments, – a "combining function" and a "sentinel value", – will perform the right fold of the encoded list using those two arguments.

For an empty list the sentinel value is returned as the folding's result. The result of folding a non-empty list with *head* h and *tail* t is the result of combining, by the supplied function, of the *head* h with the *result* of folding the tail t with the supplied two arguments. Thus the combining function's two arguments are, conceptually, the *current element* and the *result* of folding the *rest* of the list.

For example, a list of three elements x, y and z is represented by a term that when applied to c and n returns c x (c y (c z n)). Equivalently, it is an application of the chain of functional compositions ( $\circ$ ) of partial applications, ((c x) $\circ$ (c y) $\circ$ (c z)) n.

${\begin{aligned}\operatorname {nil} &\equiv \lambda \,c\,n.n\\\operatorname {isnil} &\equiv \lambda \,l.l\ (\lambda \,h\,r.\operatorname {false} )\ \operatorname {true} \\\operatorname {cons} &\equiv \lambda \,h\,t.\lambda \,c\,n.c\ h\ (t\ c\ n)\\\operatorname {singleton} &\equiv \lambda \,h.\lambda \,c\,n.c\ h\ n\\\operatorname {append} &\equiv \lambda \,l\,t.\lambda \,c\,n.l\ c\ (t\ c\ n)\\\operatorname {nonempty} &\equiv \lambda \,l.l\ (\lambda \,h\,r.\operatorname {true} )\ \operatorname {false} \\\operatorname {head} &\equiv \lambda \,l.l\ (\lambda \,h\,r.h)\ \operatorname {false} \\\operatorname {safeHead} &\equiv \lambda \,l\,e\,s.l\ (\lambda \,h\,r.s\ h)\ e\\\operatorname {fold} &\equiv \lambda \,c\,n\,l.l\ c\ n\\\operatorname {map} &\equiv \lambda f\,l.\lambda \,c\,n.l\ (\lambda \,h\,r.c\ (f\ h)\ r)\ n\equiv \lambda f\,l\,c.l\ (c\circ f)\\\operatorname {tail} &\equiv \lambda \,l.\lambda \,c\,n.l\ (\lambda \,h\,r\,g.g\ h\ (r\ c))\ (\lambda \,g.n)\ (\lambda \,h\,t.t)\end{aligned}}$

These definitions follow the following logic: the equations

```
fold c n [  ]     =  n
fold c n [x ]     =  c x n
fold c n [x,y,z]  =  c x (c y (c z n))
```

mean that

${\begin{aligned}&\{\ [\ \ \ \ ]\ \}&&\equiv \lambda \,c\,n.n\\&\{\ [\ x\ \ \ ]\ \}&&\equiv \lambda \,c\,n.c\ x\ n\\&\{\ [\ x,\,y,\,z\ ]\ \}&&\equiv \lambda \,c\,n.c\ x\ (c\ y\ (c\ z\ n))\end{aligned}}$

where $\{\ l\ \}=\lambda \,c\,n.fold\ c\ n\ l$ denotes the Church List representation of the list l .

Since Church encoded list is its own folding function, folding it just means applying that function to the supplied arguments.

This list representation can be given type in System F.

The evident correspondence to Church numerals is non-coincidental, as that can be seen as a unary encoding, with natural numbers represented by lists of unit (i.e. non-important) values, e.g. [() () ()], with the list's length serving as the representation of the natural number. Right folding over such lists uses functions which necessarily ignore the element's value, and is equivalent to the chained functional composition, i.e. ( (c ()) $\circ$ (c ()) $\circ$ (c ()) ) n = (f $\circ$ f $\circ$ f) n, as is used in Church numerals.

### Two pairs as a list node

A nonempty list can be represented by a Church pair, where

- *first* contains the list's head
- *second* contains the list's tail

However this does not give a representation of the empty list, because there is no "null" pointer. To represent null, the pair can be wrapped in another pair, giving three values:

- *first* - the null list indicator (a Boolean).
- *first of second* contains the head (*car*).
- *second of second* contains the tail (*cdr*).

Using this idea the basic list operations can be defined like this:

| Expression | Description |
|---|---|
| $\operatorname {nil} \equiv \operatorname {pair} \ \operatorname {true} \ \operatorname {true}$ | The first element of the pair is *true* meaning the list is null. |
| $\operatorname {isnil} \equiv \operatorname {first}$ | Retrieve the null (or empty list) indicator. |
| $\operatorname {cons} \equiv \lambda h.\lambda t.\operatorname {pair} \operatorname {false} \ (\operatorname {pair} h\ t)$ | Create a list node, which is not null, and give it a head *h* and a tail *t*. |
| $\operatorname {head} \equiv \lambda z.\operatorname {first} \ (\operatorname {second} z)$ | *second.first* is the head. |
| $\operatorname {tail} \equiv \lambda z.\operatorname {second} \ (\operatorname {second} z)$ | *second.second* is the tail. |

In a *nil* node *second* is never accessed, provided that **head** and **tail** are only applied to nonempty lists.

### One pair as a list node

Alternatively, define

${\begin{aligned}\operatorname {cons} &\equiv \operatorname {pair} \\\operatorname {head} &\equiv \lambda l.\ l\ (\lambda htd.\ h)\ \operatorname {nil} \\\operatorname {tail} &\equiv \lambda l.\ l\ (\lambda htd.\ t)\ \operatorname {nil} \\\operatorname {nil} &\equiv \operatorname {false} \\\operatorname {isnil} &\equiv \lambda l.l\ (\lambda htd.\operatorname {false} )\operatorname {true} \\\end{aligned}}$

where the definitions like the last one all follow the same general pattern for the safe use of a list, with h and t referring to the list's head and tail, and d being discarded, as an artificial device:

${\begin{aligned}\lambda l.l\ (\lambda htd.\langle \operatorname {head-and-tail-clause} \rangle )\ \langle \operatorname {nil-clause} \rangle \\\end{aligned}}$

Other operations in this encoding are:

${\begin{aligned}\operatorname {lfold} &\equiv \lambda f.\ \operatorname {Y} \ (\lambda r.\lambda al.\ l\ (\lambda htd.\ r\ (f\ a\ h)\ t)\ a)\\\operatorname {rfold} &\equiv \lambda fa.\ \operatorname {Y} \ (\lambda r.\lambda l.\ l\ (\lambda htd.\ f\ (r\ t)\ h)\ a)\\\operatorname {length} &\equiv \operatorname {lfold} \ (\lambda ah.\ \operatorname {succ} \ a)\ \operatorname {zero} \end{aligned}}$

${\begin{aligned}\operatorname {map} &\equiv \lambda f.\ \operatorname {rfold} \ (\lambda ah.\ \operatorname {cons} \ (f\ h)\ a)\ \operatorname {nil} \\\operatorname {filter} &\equiv \lambda p.\ \operatorname {rfold} \ (\lambda ah.\ p\ h\ (\operatorname {cons} \ h\ a)\ a)\ \operatorname {nil} \\\operatorname {reverse} &\equiv \operatorname {fold} \ (\lambda ah.\ \operatorname {cons} \ h\ a)\ \operatorname {nil} \\\operatorname {concat} &\equiv \lambda lg.\ \operatorname {rfold} \ (\lambda ah.\ \operatorname {cons} \ h\ a)\ g\ l\\\operatorname {conj} &\equiv \lambda lv.\ \operatorname {concat} \ l\ (\operatorname {cons} \ v\ \operatorname {nil} )\end{aligned}}$

${\begin{aligned}\operatorname {drop} &\equiv \lambda n.\ n\ \operatorname {tail} \\&\equiv \operatorname {Y} \ (\lambda r.\lambda nl.\ l\ (\lambda htd.\ \operatorname {IsZero} \ n\ l\ (r\ (\operatorname {pred} \ n)\ t))\ \operatorname {nil} )\\\operatorname {drop-last} &\equiv \lambda nl.\ \operatorname {IsZero} \ n\ l\ \operatorname {second} (\\&\ \ \ \ \ \ \ \ \operatorname {Y} \ (\lambda rl_{r}.\ l_{r}\ (\lambda htd.\\&\ \ \ \ \ \ \ \ \ \ \ \ r\ t\ (\lambda n_{a}l_{a}.\ \operatorname {IsZero} \ n_{a}\\&\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ (\operatorname {pair} \ \operatorname {zero} \ (\operatorname {cons} \ h\ l_{a}))\\&\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ (\operatorname {pair} \ (\operatorname {pred} \ n_{a})\ \operatorname {nil} )\ ))\\&\ \ \ \ \ \ \ \ \ \ \ \ (\operatorname {pair} \ n\ \operatorname {nil} )\ )\\&\ \ \ \ \ \ \ \ \ l\ )\\\operatorname {drop-while} &\equiv \lambda p.\ \operatorname {Y} \ (\lambda rl.\ l\ (\lambda htd.\ p\ h\ (r\ t)\ l)\ \operatorname {nil} )\\\operatorname {take} &\equiv \operatorname {Y} \ (\lambda rnl.\ l\ (\lambda htd.\ \operatorname {IsZero} \ n\ \operatorname {nil} \ (\operatorname {cons} \ h\ (r\ (\operatorname {pred} \ n)\ t)))\ \operatorname {nil} )\\\operatorname {take-last} &\equiv \lambda nl.\ \operatorname {IsZero} \ n\ l\ \operatorname {second} (\\&\ \ \ \ \ \ \ \ \operatorname {Y} \ (\lambda rl_{r}.\ l_{r}\ (\lambda htd.\\&\ \ \ \ \ \ \ \ \ \ \ \ r\ t\ (\lambda n_{a}l_{a}.\ \operatorname {IsZero} \ n_{a}\\&\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ (\operatorname {pair} \ \operatorname {zero} \ l_{a})\\&\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ (\operatorname {pair} \ (\operatorname {pred} \ n_{a})\ l_{r})\ ))\\&\ \ \ \ \ \ \ \ \ \ \ \ (\operatorname {pair} \ n\ \operatorname {nil} )\ )\\&\ \ \ \ \ \ \ \ \ l)\\\operatorname {take-while} &\equiv \lambda p.\ \operatorname {Y} \ (\lambda rl.\ l\ (\lambda htd.\ p\ h\ (\operatorname {cons} \ h\ (r\ t))\ \operatorname {nil} )\ \operatorname {nil} )\end{aligned}}$

${\begin{aligned}\operatorname {all} &\equiv \operatorname {Y} \ (\lambda rpl.\ l\ (\lambda htd.\ p\ h\ (r\ p\ t)\ \operatorname {false} )\ \operatorname {true} )\\\operatorname {any} &\equiv \operatorname {Y} \ (\lambda rpl.\ l\ (\lambda htd.\ p\ h\ \operatorname {true} \ (r\ p\ t))\ \operatorname {false} )\\\operatorname {element-at} &\equiv \lambda nl.\ \operatorname {head} \ (\operatorname {drop} \ n\ l)\\\operatorname {insert-at} &\equiv \lambda nvl.\ \operatorname {concat} \ (\operatorname {take} \ n\ l)\ (\operatorname {cons} \ v\ (\operatorname {drop} \ n\ l))\\\operatorname {remove-at} &\equiv \lambda nl.\ \operatorname {concat} \ (\operatorname {take} \ n\ l)\ (\operatorname {drop} \ (\operatorname {succ} \ n)\ l)\\\operatorname {replace-at} &\equiv \lambda nvl.\ \operatorname {concat} \ (\operatorname {take} \ n\ l)\ (\operatorname {cons} \ v\ (\operatorname {drop} \ (\operatorname {succ} \ n)\ l))\\\operatorname {index-of} &\equiv \lambda p.\ \operatorname {Y} \ (\lambda rnl.\ l\ (\lambda htd.\ p\ h\ n\ (r\ (\operatorname {succ} \ n)\ t))\ \operatorname {zero} )\ \operatorname {one} \\\operatorname {last-index-of} &\equiv \lambda p.\ \operatorname {Y} \ (\lambda rnl.\ l\ (\lambda htd.\ (\lambda i.\ \operatorname {IsZero} \ i\ (p\ h\ n\ \operatorname {zero} )\ i)\ (r\ (\operatorname {succ} \ n)\ t))\ \operatorname {zero} )\ \operatorname {one} \\\operatorname {range} &\equiv \lambda fz.\ \operatorname {Y} \ (\lambda rsn.\ \operatorname {IsZero} \ n\ \operatorname {nil} \ (\operatorname {cons} \ (s\ f\ z)\ (r\ (\operatorname {succ} \ s)\ (\operatorname {pred} \ n))))\ \operatorname {zero} \\\operatorname {repeat} &\equiv \lambda v.\ \operatorname {Y} \ (\lambda rn.\ \operatorname {IsZero} \ n\ \operatorname {nil} \ (\operatorname {cons} \ v\ (r\ (\operatorname {pred} \ n))))\\\operatorname {zip} &\equiv Y\ (\lambda rl_{1}l_{2}.\ l_{1}\ (\lambda h_{1}t_{1}d_{1}.\ l_{2}\ (\lambda h_{2}t_{2}d_{2}.\ \operatorname {cons} \ (\operatorname {pair} \ h_{1}\ h_{2})\ (r\ t_{1}\ t_{2}))\ \operatorname {nil} )\ \operatorname {nil} )\\\end{aligned}}$

### Scott lists

Scott encoding for data types follows their surface syntax without regard to recursion in the data type. In the disjunction of conjunctions a.k.a. sum of products style of algebraic data type definitions, it represents a given datum as a function which expects as many arguments as there are alternatives in its data type definition, where each such argument is expected to be a "handler" function that must be able to handle the given number of data arguments that will correspond to the data fields for that alternative.

Given all the handlers as arguments, the datum representation function will then call the appropriate handler with the corresponding internal data. Scott encoded values can thus be said to embody the pattern matching case handling for their data type.

For lists, it means the data type definition of

$\qquad List:=\operatorname {NIL} \ |\,\operatorname {Cons} \,\langle val\rangle \,List$

and lists being represented as

$\quad {\begin{aligned}\operatorname {NIL} &=\lambda nc.n\\\operatorname {Cons} &=\lambda ad.\lambda nc.c\ a\ d\\\operatorname {IsEmpty} &=\lambda l.l\,\operatorname {true} \,(\lambda ad.\operatorname {false} )\\\operatorname {Head} &=\lambda l.l\,\operatorname {NIL} \,(\lambda ad.a)\\\operatorname {Tail} &=\lambda l.l\,\operatorname {NIL} \,(\lambda ad.d)\\\operatorname {fold} &=\lambda gz.\operatorname {Y} \lambda rl.l\ z\ (\lambda ad.g\,a\ (r\ d))\\\operatorname {Append} &=\operatorname {fold} \,\operatorname {Cons} \\\operatorname {Map} &=\lambda f.\operatorname {fold} \,(\lambda h.\operatorname {Cons} \,(f\,h))\,\operatorname {NIL} \\\operatorname {Map2} &=\lambda f.\operatorname {Y} \lambda rpq.p\,\operatorname {NIL} \,(\lambda ad.\\&\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ q\,\operatorname {NIL} \,(\lambda bg.\operatorname {Cons} \,(f\,a\,b)(r\ d\ g)))\\\end{aligned}}$

Recursive operations on Scott lists typically require explicit use of recursion, e.g. using $\operatorname {Y}$ combinator, or explicit self-application definitions. One such example is *fold*, unlike the no-op that it is under Church encoding. But *tail* is immediately available, so its definition is much simpler here, in comparison. See Scott encoding for more.

Scott encoding can be seen as using the idea of continuations, which can lead to simpler code. In this approach, we use the fact that lists can be observed using pattern matching expression. For example, using Scala notation, if `list` denotes a value of type `List` with empty list `Nil` and constructor `Cons(h, t)` we can inspect the list and compute `nilCode` in case the list is empty and `consCode(h, t)` when the list is not empty:

```mw
list match {
  case Nil        => nilCode
  case Cons(h, t) => consCode(h,t)
}
```

The `list` is given by how it acts upon `nilCode` and `consCode`. We therefore define a list as a function that accepts such `nilCode` and `consCode` as arguments, so that instead of the above pattern match we may simply write:

$\operatorname {list} \ \operatorname {nilCode} \ \operatorname {consCode}$

Let us denote by `n` the parameter corresponding to `nilCode` and by `c` the parameter corresponding to `consCode`. The empty list is the one that returns the nil argument:

$\operatorname {nil} \equiv \lambda n.\lambda c.\ n$

The non-empty list with head `h` and tail `t` is given by

$\operatorname {cons} \ h\ t\ \ \equiv \ \ \lambda n.\lambda c.\ c\ h\ t$

More generally, an algebraic data type with m alternatives becomes a function with m parameters. When the i th constructor has $n_{i}$ arguments, the corresponding parameter of the encoding takes $n_{i}$ arguments as well.

Scott encoding can be done in untyped lambda calculus, whereas its use with types requires a type system with recursion and type polymorphism. A list with element type E in this representation that is used to compute values of type C would have the following recursive type definition, where '=>' denotes function type:

```mw
type List =
  C =>                    // nil argument
  (E => List => C) =>     // cons argument
  C                       // result of pattern matching
```

A list that can be used to compute arbitrary types would have a type that quantifies over `C`. A list generic in `E` would also take `E` as the type argument.

## General remarks

A straightforward implementation of Church encoding slows some access operations from $O(1)$ to $O(n)$ , where n is the size of the data structure, making Church encoding impractical. Research has shown that this can be addressed by targeted optimizations, but most functional programming languages instead expand their intermediate representations to contain algebraic data types. Nonetheless Church encoding is often used in theoretical arguments, as it is a natural representation for partial evaluation and theorem proving. Operations can be typed using higher-ranked types, and primitive recursion is easily accessible. The assumption that functions are the only primitive data types streamlines many proofs.

Church encoding is complete but only representationally. Additional functions are needed to translate the representation into common data types, for display to people. It is not possible in general to decide if two functions are extensionally equal due to the undecidability of equivalence from Church's theorem. The translation may apply the function in some way to retrieve the value it represents, or look up its value as a literal lambda term. Lambda calculus is usually interpreted as using intensional equality. There are potential problems with the interpretation of results because of the difference between the intensional and extensional definition of equality.
