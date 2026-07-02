---
title: "Kolmogorov complexity"
source: https://en.wikipedia.org/wiki/Kolmogorov_complexity
domain: information-theory
license: CC-BY-SA-4.0
tags: information theory, shannon entropy, channel capacity, error correction, hamming code
fetched: 2026-07-02
---

# Kolmogorov complexity

In algorithmic information theory (a subfield of computer science and mathematics), the **Kolmogorov complexity** of an object, such as a piece of text, is the length of a shortest computer program (in a predetermined programming language) that produces the object as output. It is a measure of the computational resources needed to specify the object, and is also known as **algorithmic complexity**, **Solomonoff–Kolmogorov–Chaitin complexity**, **program-size complexity**, **descriptive complexity**, or **algorithmic entropy**. It is named after Andrey Kolmogorov, who first published on the subject in 1963 and is a generalization of classical information theory.

The notion of Kolmogorov complexity can be used to state and prove impossibility results akin to Cantor's diagonal argument, Gödel's incompleteness theorem, and Turing's halting problem. In particular, no program *P* computing a lower bound for each text's Kolmogorov complexity can return a value essentially larger than *P*'s own length (see section § Chaitin's incompleteness theorem); hence no single program can compute the exact Kolmogorov complexity for infinitely many texts.

## Definition

### Intuition

Consider the following two strings of 32 lowercase letters and digits:

abababababababababababababababab

, and

4c1j5b2p0cv4w1x8rx2y39umgw5q85s7

The first string has a short English-language description, namely "write ab 16 times", which consists of **17** characters. The second one has no obvious simple description (using the same character set) other than writing down the string itself, i.e., "write 4c1j5b2p0cv4w1x8rx2y39umgw5q85s7" which has **38** characters. Hence the operation of writing the first string can be said to have "less complexity" than writing the second.

More formally, the complexity of a string is the length of the shortest possible description of the string in some fixed universal description language (the sensitivity of complexity relative to the choice of description language is discussed below). It can be shown that the Kolmogorov complexity of any string cannot be more than a few bytes larger than the length of the string itself. Strings like the *abab* example above, whose Kolmogorov complexity is small relative to the string's size, are not considered to be complex.

The Kolmogorov complexity can be defined for any mathematical object, but for simplicity the scope of this article is restricted to strings. We must first specify a description language for strings. Such a description language can be based on any computer programming language, such as Lisp, Pascal, or Java. If **P** is a program which outputs a string *x*, then **P** is a description of *x*. The length of the description is just the length of **P** as a character string, multiplied by the number of bits in a character (e.g., 7 for ASCII).

We could, alternatively, choose an encoding for Turing machines, where an *encoding* is a function which associates to each Turing Machine **M** a bitstring <**M**>. If **M** is a Turing Machine which, on input *w*, outputs string *x*, then the concatenated string <**M**> *w* is a description of *x*. For theoretical analysis, this approach is more suited for constructing detailed formal proofs and is generally preferred in the research literature. In this article, an informal approach is discussed.

Any string *s* has at least one description. For example, the second string above is output by the pseudo-code:

```mw
def generate_string2():
    return "4c1j5b2p0cv4w1x8rx2y39umgw5q85s7"
```

whereas the first string is output by the (much shorter) pseudo-code:

```mw
def generate_string1():
    return "ab" × 16
```

If a description *d*(*s*) of a string *s* is of minimal length (i.e., using the fewest bits), it is called a **minimal description** of *s*, and the length of *d*(*s*) (i.e. the number of bits in the minimal description) is the **Kolmogorov complexity** of *s*, written *K*(*s*). Symbolically,

K

(

s

) = |

d

(

s

)|.

The length of the shortest description will depend on the choice of description language; but the effect of changing languages is bounded (a result called the *invariance theorem*, see below).

### Plain Kolmogorov complexity *C*

There are two definitions of Kolmogorov complexity: *plain* and *prefix-free*. The plain complexity is the minimal description length of any program, and denoted $C(x)$ while the prefix-free complexity is the minimal description length of any program encoded in a prefix-free code, and denoted $K(x)$ . The plain complexity is more intuitive, but the prefix-free complexity is easier to study.

By default, all equations hold only up to an additive constant. For example, $f(x)=g(x)$ really means that $f(x)=g(x)+O(1)$ , that is, $\exists c,\forall x,|f(x)-g(x)|\leq c$ .

Let $U:2^{*}\to 2^{*}$ be a computable function mapping finite binary strings to binary strings. It is a universal function if, and only if, for any computable $f:2^{*}\to 2^{*}$ , we can encode the function in a "program" $s_{f}$ , such that $\forall x\in 2^{*},U(s_{f}x)=f(x)$ . We can think of U as a program interpreter, which takes in an initial segment describing the program, followed by data that the program should process.

One problem with plain complexity is that $C(xy)\not <C(x)+C(y)$ , because intuitively speaking, there is no general way to tell where to divide an output string just by looking at the concatenated string. We can divide it by specifying the length of x or y , but that would take $O(\min(\ln x,\ln y))$ extra symbols. Indeed, for any $c>0$ there exists $x,y$ such that $C(xy)\geq C(x)+C(y)+c$ .

Typically, inequalities with plain complexity have a term like $O(\min(\ln x,\ln y))$ on one side, whereas the same inequalities with prefix-free complexity have only $O(1)$ .

The main problem with plain complexity is that there is something extra sneaked into a program. A program not only represents for something with its code, but also represents its own length. In particular, a program x may represent a binary number up to $\log _{2}|x|$ , simply by its own length. Stated in another way, it is as if we are using a termination symbol to denote where a word ends, and so we are not using 2 symbols, but 3. To fix this defect, we introduce the prefix-free Kolmogorov complexity.

### Prefix-free Kolmogorov complexity *K*

A **prefix-free universal Turing machine** is a universal partial computable function $U:2^{*}\rightarrow 2^{*}$ whose domain is a prefix-free set of binary strings. Equivalently, no valid program for U is a prefix of any other, the domain satisfies the prefix property. For instance, if every valid program for a universal Turing machine U ended with a termination string that could not appear elsewhere in the program, U would be prefix-free.

The prefix-free Kolmogorov complexity of a string x is defined by $K(x):=\min\{|c|:U(c)=x\}$ the length of the shortest self-delimiting program that causes U to output x .

Different choices of prefix-free universal machines change $K(x)$ by at most an additive constant.

## Invariance theorem

### Informal treatment

There are some description languages which are optimal, in the following sense: given any description of an object in a description language, said description may be used in the optimal description language with a constant overhead. The constant depends only on the languages involved, not on the description of the object, nor the object being described.

Here is an example of an optimal description language. A description will have two parts:

- The first part describes another description language.
- The second part is a description of the object in that language.

In more technical terms, the first part of a description is a computer program (specifically: a compiler for the object's language, written in the description language), with the second part being the input to that computer program which produces the object as output.

**The invariance theorem follows:** Given any description language *L*, the optimal description language is at least as efficient as *L*, with some constant overhead.

**Proof:** Any description *D* in *L* can be converted into a description in the optimal language by first describing *L* as a computer program *P* (part 1), and then using the original description *D* as input to that program (part 2). The total length of this new description *D′* is (approximately):

|

D′

| = |

P

| + |

D

|

The length of *P* is a constant that doesn't depend on *D*. So, there is at most a constant overhead, regardless of the object described. Therefore, the optimal language is universal up to this additive constant.

### A more formal treatment

**Theorem**: If *K*1 and *K*2 are the complexity functions relative to Turing complete description languages *L*1 and *L*2, then there is a constant *c* – which depends only on the languages *L*1 and *L*2 chosen – such that

$\forall s.-c\leq K_{1}(s)-K_{2}(s)\leq c$

.

**Proof**: By symmetry, it suffices to prove that there is some constant *c* such that for all strings *s*

$K_{1}(s)\leq K_{2}(s)+c$

.

Now, suppose there is a program in the language *L*1 which acts as an interpreter for *L*2:

```mw
def interpret_language(p: str)
```

where *p* is a program in *L*2. The interpreter is characterized by the following property:

Running

interpret_language

on input

p

returns the result of running

p

.

Thus, if **P** is a program in *L*2 which is a minimal description of *s*, then `interpret_language`(**P**) returns the string *s*. The length of this description of *s* is the sum of

1. The length of the program `interpret_language`, which we can take to be the constant *c*.
2. The length of **P** which by definition is *K*2(*s*).

This proves the desired upper bound.

## History and context

Algorithmic information theory is the area of computer science that studies Kolmogorov complexity and other complexity measures on strings (or other data structures).

The concept and theory of Kolmogorov Complexity is based on a crucial theorem first discovered by Ray Solomonoff, who published it in 1960, describing it in "A Preliminary Report on a General Theory of Inductive Inference" as part of his invention of algorithmic probability. He gave a more complete description in his 1964 publications, "A Formal Theory of Inductive Inference," Part 1 and Part 2 in *Information and Control*.

Andrey Kolmogorov later independently published this theorem in *Problems Inform. Transmission* in 1965. Gregory Chaitin also presents this theorem in the *Journal of the ACM* – Chaitin's paper was submitted October 1966 and revised in December 1968, and cites both Solomonoff's and Kolmogorov's papers.

The theorem says that, among algorithms that decode strings from their descriptions (codes), there exists an optimal one. This algorithm, for all strings, allows codes as short as allowed by any other algorithm up to an additive constant that depends on the algorithms, but not on the strings themselves. Solomonoff used this algorithm and the code lengths it allows to define a "universal probability" of a string on which inductive inference of the subsequent digits of the string can be based. Kolmogorov used this theorem to define several functions of strings, including complexity, randomness, and information.

When Kolmogorov became aware of Solomonoff's work, he acknowledged Solomonoff's priority. For several years, Solomonoff's work was better known in the Soviet Union than in the West. The general consensus in the scientific community, however, was to associate this type of complexity with Kolmogorov, who was concerned with randomness of a sequence, while Algorithmic Probability became associated with Solomonoff, who focused on prediction using his invention of the universal prior probability distribution. The broader area encompassing descriptional complexity and probability is often called Kolmogorov complexity. The computer scientist Ming Li considers this an example of the Matthew effect: "...to everyone who has, more will be given..."

There are several other variants of Kolmogorov complexity or algorithmic information. The most widely used one is based on self-delimiting programs, and is mainly due to Leonid Levin (1974).

An axiomatic approach to Kolmogorov complexity based on Blum axioms (Blum 1967) was introduced by Mark Burgin in the paper presented for publication by Andrey Kolmogorov.

## Basic results

We write $K(x,y)$ to be $K((x,y))$ , where $(x,y)$ means some fixed way to code for a tuple of strings x and y.

### Inequalities

We omit additive factors of $O(1)$ . This section is based on.

**Theorem.** $K(x)\leq C(x)+2\log _{2}C(x)$

**Proof.** Take any program for the universal Turing machine used to define plain complexity, and convert it to a prefix-free program by first coding the length of the program in binary, then convert the length to prefix-free coding. For example, suppose the program has length 9, then we can convert it as follows: $9\mapsto 1001\mapsto 11-00-00-11-\color {red}{01}$ where we double each digit, then add a termination code. The prefix-free universal Turing machine can then read in any program for the other machine as follows: $[{\text{code for simulating the other machine}}][{\text{coded length of the program}}][{\text{the program}}]$ The first part programs the machine to simulate the other machine, and is a constant overhead $O(1)$ . The second part has length $\leq 2\log _{2}C(x)+3$ . The third part has length $C(x)$ .

**Theorem**: There exists c such that $\forall x,C(x)\leq |x|+c$ . More succinctly, $C(x)\leq |x|$ . Similarly, $K(x)\leq |x|+2\log _{2}|x|$ , and $K(x||x|)\leq |x|$ .

**Proof.** For the plain complexity, just write a program that simply copies the input to the output. For the prefix-free complexity, we need to first describe the length of the string, before writing out the string itself.

**Theorem. (extra information bounds, subadditivity)**

- $K(x|y)\leq K(x)\leq K(x,y)\leq \max(K(x|y)+K(y),K(y|x)+K(x))\leq K(x)+K(y)$
- $K(xy)\leq K(x,y)$

Note that there is no way to compare $K(xy)$ and $K(x|y)$ or $K(x)$ or $K(y|x)$ or $K(y)$ . There are strings such that the whole string $xy$ is easy to describe, but its substrings are very hard to describe.

**Theorem. (symmetry of information)** $K(x,y)=K(x|y,K(y))+K(y)=K(y,x)$ .

**Proof.** One side is simple. For the other side with $K(x,y)\geq K(x|y,K(y))+K(y)$ , we need to use a counting argument (page 38 ).

**Theorem. (information non-increase)** For any computable function f , we have $K(f(x))\leq K(x)+K(f)$ .

**Proof.** Program the Turing machine to read two subsequent programs, one describing the function and one describing the string. Then run both programs on the work tape to produce $f(x)$ , and write it out.

### Uncomputability of Kolmogorov complexity

#### A naive attempt at a program to compute *K*

At first glance it might seem trivial to write a program which can compute *K*(*s*) for any *s*, such as the following:

```mw
def kolmogorov_complexity(s: str):
    for i = 1 to infinity:
        for each string p of length exactly i
            if is_valid_program(p) and evaluate(p) == s
                return i
```

This program iterates through all possible programs (by iterating through all possible strings and only considering those which are valid programs), starting with the shortest. Each program is executed to find the result produced by that program, comparing it to the input *s*. If the result matches then the length of the program is returned.

However this will not work because some of the programs *p* tested will not terminate, e.g. if they contain infinite loops. There is no way to avoid all of these programs by testing them in some way before executing them due to the non-computability of the halting problem.

What is more, no program at all can compute the function *K*, be it ever so sophisticated. This is proven in the following.

#### Formal proof of uncomputability of *K*

**Theorem**: There exist strings of arbitrarily large Kolmogorov complexity. Formally: for each natural number *n*, there is a string *s* with *K*(*s*) ≥ *n*.

**Proof:** Otherwise all of the infinitely many possible finite strings could be generated by the finitely many programs with a complexity below *n* bits.

**Theorem**: *K* is not a computable function. In other words, there is no program which takes any string *s* as input and produces the integer *K*(*s*) as output.

The following **proof** by contradiction uses a simple Pascal-like language to denote programs; for sake of proof simplicity assume its description (i.e. an interpreter) to have a length of 1400000 bits. Assume for contradiction there is a program

```mw
def kolmogorov_complexity(s: str)
```

which takes as input a string *s* and returns *K*(*s*). All programs are of finite length so, for sake of proof simplicity, assume it to be 7000000000 bits. Now, consider the following program of length 1288 bits:

```mw
def generate_complex_string(): str
    for i = 1 to infinity:
        for each string s of length exactly i
            if kolmogorov_complexity(s) >= 8000000000
                return s
```

Using `kolmogorov_complexity` as a subroutine, the program tries every string, starting with the shortest, until it returns a string with Kolmogorov complexity at least 8000000000 bits, i.e. a string that cannot be produced by any program shorter than 8000000000 bits. However, the overall length of the above program that produced *s* is only 7001401288 bits, which is a contradiction. (If the code of `KolmogorovComplexity` is shorter, the contradiction remains. If it is longer, the constant used in `GenerateComplexString` can always be changed appropriately.)

The above proof uses a contradiction similar to that of the Berry paradox: "1The 2smallest 3positive 4integer 5that 6cannot 7be 8defined 9in 10fewer 11than 12twenty 13English 14words". It is also possible to show the non-computability of *K* by reduction from the non-computability of the halting problem *H*, since *K* and *H* are Turing-equivalent.

There is a corollary, humorously called the "full employment theorem" in the programming language community, stating that there is no perfect size-optimizing compiler.

### Chain rule for Kolmogorov complexity

The chain rule for Kolmogorov complexity states that there exists a constant *c* such that for all *X* and *Y*:

$K(X,Y)=K(X)+K(Y|X)+c\cdot max(1,log(K(X,Y)))$

.

It states that the shortest program that reproduces *X* and *Y* is no more than a logarithmic term larger than a program to reproduce *X* and a program to reproduce *Y* given *X*. Using this statement, one can define an analogue of mutual information for Kolmogorov complexity.

## Compression

It is straightforward to compute upper bounds for *K*(*s*) – simply compress the string *s* with some method, implement the corresponding decompressor in the chosen language, concatenate the decompressor to the compressed string, and measure the length of the resulting string – concretely, the size of a self-extracting archive in the given language.

A string *s* is compressible by a number *c* if it has a description whose length does not exceed |*s*| − *c* bits. This is equivalent to saying that *K*(*s*) ≤ |*s*| − *c*. Otherwise, *s* is incompressible by *c*. A string incompressible by 1 is said to be simply *incompressible* – by the pigeonhole principle, which applies because every compressed string maps to only one uncompressed string, incompressible strings must exist, since there are 2*n* bit strings of length *n*, but only 2*n* − 1 shorter strings, that is, strings of length less than *n*, (i.e. with length 0, 1, ..., *n* − 1).

For the same reason, most strings are complex in the sense that they cannot be significantly compressed – their *K*(*s*) is not much smaller than |*s*|, the length of *s* in bits. To make this precise, fix a value of *n*. There are 2*n* bitstrings of length *n*. The uniform probability distribution on the space of these bitstrings assigns exactly equal weight 2−*n* to each string of length *n*.

**Theorem**: With the uniform probability distribution on the space of bitstrings of length *n*, the probability that a string is incompressible by *c* is at least 1 − 2−*c*+1 + 2−*n*.

To prove the theorem, note that the number of descriptions of length not exceeding *n* − *c* is given by the geometric series:

1 + 2 + 2

2

+ ... + 2

n

−

c

= 2

n

−

c

+1

− 1.

There remain at least

2

n

− 2

n

−

c

+1

+ 1

bitstrings of length *n* that are incompressible by *c*. To determine the probability, divide by 2*n*.

## Chaitin's incompleteness theorem

By the above theorem (§ Compression), most strings are complex in the sense that they cannot be described in any significantly "compressed" way. However, it turns out that the fact that a specific string is complex cannot be formally proven, if the complexity of the string is above a certain threshold. The precise formalization is as follows. First, fix a particular axiomatic system **S** for the natural numbers. The axiomatic system has to be powerful enough so that, to certain assertions **A** about complexity of strings, one can associate a formula **F****A** in **S**. This association must have the following property:

If **F****A** is provable from the axioms of **S**, then the corresponding assertion **A** must be true. This "formalization" can be achieved based on a Gödel numbering.

**Theorem**: There exists a constant *L* (which only depends on **S** and on the choice of description language) such that there does not exist a string *s* for which the statement

$K(s)\geq L$

(as formalized in

S

)

can be proven within **S**.

**Proof Idea**: The proof of this result is modeled on a self-referential construction used in Berry's paradox. We initially obtain a program which enumerates the proofs within **S** and we specify a procedure *P* which takes as an input an integer *L* and prints the strings *x* which are within proofs within **S** of the statement *K*(*x*) ≥ *L*. By then setting *L* to greater than the length of this procedure *P*, we have that the required length of a program to print *x* as stated in *K*(*x*) ≥ *L* as being at least *L* is then less than the amount *L* since the string *x* was printed by the procedure *P*. This is a contradiction. So it is not possible for the proof system **S** to prove *K*(*x*) ≥ *L* for *L* arbitrarily large, in particular, for *L* larger than the length of the procedure *P*, (which is finite).

**Proof**:

We can find an effective enumeration of all the formal proofs in **S** by some procedure

```mw
def nth_proof(n: int)
```

which takes as input *n* and outputs some proof. This function enumerates all proofs. Some of these are proofs for formulas we do not care about here, since every possible proof in the language of **S** is produced for some *n*. Some of these are complexity formulas of the form *K*(*s*) ≥ *n* where *s* and *n* are constants in the language of **S**. There is a procedure

```mw
def nth_proof_proves_complexity_formula(n: int): bool
```

which determines whether the *n*th proof actually proves a complexity formula *K*(*s*) ≥ *L*. The strings *s*, and the integer *L* in turn, are computable by procedure:

```mw
def string_nth_proof(n: int)
```

```mw
def complexity_lower_bound_nth_proof(n: int): int
```

Consider the following procedure:

```mw
def generate_provably_complex_string(n: int):
    for i = 1 to infinity:
        if nth_proof_proves_complexity_formula(i) and complexity_lower_bound_nth_proof(i) ≥ n
            return string_nth_proof(i)
```

Given an n , this procedure tries every proof until it finds a string and a proof in the formal system **S** of the formula $K(s)\geq L$ for some $L\geq n$ ; if no such proof exists, it loops forever.

Finally, consider the program consisting of all these procedure definitions, and a main call:

```mw
generate_provably_complex_string(n₀)
```

where the constant $n_{0}$ will be determined later on. The overall program length can be expressed as $U+log_{2}(n_{0})$ , where U is some constant and $log_{2}(n_{0})$ represents the length of the integer value $n_{0}$ , under the reasonable assumption that it is encoded in binary digits. We will choose $n_{0}$ to be greater than the program length, that is, such that $n_{0}>U+log_{2}(n_{0})$ . This is clearly true for $n_{0}$ sufficiently large, because the left hand side grows linearly in $n_{0}$ whilst the right hand side grows logarithmically in $n_{0}$ up to the fixed constant U .

Then no proof of the form " $K(s)\geq L$ " with $L\geq n_{0}$ can be obtained in **S**, as can be seen by an indirect argument: If `complexity_lower_bound_nth_proof(i)` could return a value $\geq n_{0}$ , then the loop inside `generate_provably_complex_string` would eventually terminate, and that procedure would return a string *s* such that

|   | $K(s)$ |   |
|---|---|---|
| ≥ | $n_{0}$ | by construction of `generate_provably_complex_string` |
| > | $U+log_{2}(n_{0})$ | by the choice of $n_{0}$ |
| ≥ | $K(s)$ | since s was described by the program with that length |

This is a contradiction, Q.E.D.

As a consequence, the above program, with the chosen value of $n_{0}$ , must loop forever.

Similar ideas are used to prove the properties of Chaitin's constant.

## Minimum message length

The minimum message length principle of statistical and inductive inference and machine learning was developed by C.S. Wallace and D.M. Boulton in 1968. MML is Bayesian (i.e. it incorporates prior beliefs) and information-theoretic. It has the desirable properties of statistical invariance (i.e. the inference transforms with a re-parametrisation, such as from polar coordinates to Cartesian coordinates), statistical consistency (i.e. even for very hard problems, MML will converge to any underlying model) and efficiency (i.e. the MML model will converge to any true underlying model about as quickly as is possible). C.S. Wallace and D.L. Dowe (1999) showed a formal connection between MML and algorithmic information theory (or Kolmogorov complexity).

## Kolmogorov randomness

*Kolmogorov randomness* defines a string (usually of bits) as being random if the shortest computer program that can produce that string is about as long as the string itself. To make this precise, a string x of length n is called *Kolmogorov random* if $K(x)\geq n+O(1)$ where K is the prefix-free Kolmogorov complexity defined above. A random string in this sense is *incompressible* in that it is impossible to "compress" the string into a program that is shorter than the string itself. There is at least one Kolmogorov random string of each length.

This definition can be extended to define a notion of randomness for *infinite* sequences from a finite alphabet. These algorithmically random sequences can be defined in three equivalent ways. One way uses an effective analogue of measure theory; another uses effective martingales. The third way defines an infinite sequence to be random if the prefix-free Kolmogorov complexity of its initial segments grows quickly enough — there must be a constant *c* such that the complexity of an initial segment of length *n* is always at least *n*−*c*.

## Relation to entropy

For dynamical systems, entropy rate and algorithmic complexity of the trajectories are related by a theorem of Brudno, that the equality $K(x;T)=h(T)$ holds for almost all x .

It can be shown that for the output of Markov information sources, Kolmogorov complexity is related to the entropy of the information source. More precisely, the Kolmogorov complexity of the output of a Markov information source, normalized by the length of the output, converges almost surely (as the length of the output goes to infinity) to the entropy of the source.

**Theorem.** (Theorem 14.2.5 ) The conditional Kolmogorov complexity of a binary string $x_{1:n}$ satisfies ${\frac {1}{n}}K(x_{1:n}|n)\leq H_{b}\left({\frac {1}{n}}\sum _{i}x_{i}\right)+{\frac {\log n}{2n}}+O(1/n)$ where $H_{b}$ is the binary entropy function (not to be confused with the entropy rate).

## Halting problem

The Kolmogorov complexity function is equivalent to deciding the halting problem.

If we have a halting oracle, then the Kolmogorov complexity of a string can be computed by simply trying every halting program, in lexicographic order, until one of them outputs the string.

The other direction is much more involved. It shows that given a Kolmogorov complexity function, we can construct a function p , such that $p(n)\geq BB(n)$ for all large n , where $BB$ is the Busy Beaver shift function (also denoted as $S(n)$ ). By modifying the function at lower values of n we get an upper bound on $BB$ , which solves the halting problem.

Consider this program ${\textstyle p_{K}}$ , which takes input as ${\textstyle n}$ , and uses ${\textstyle K}$ .

- List all strings of length ${\textstyle \leq 2n+1}$ .
- For each such string ${\textstyle x}$ , enumerate all (prefix-free) programs of length $K(x)$ until one of them does output ${\textstyle x}$ . Record its runtime ${\textstyle n_{x}}$ .
- Output the largest ${\textstyle n_{x}}$ .

We prove by contradiction that ${\textstyle p_{K}(n)\geq BB(n)}$ for all large ${\textstyle n}$ .

Let ${\textstyle p_{n}}$ be a Busy Beaver of length n . Consider this (prefix-free) program, which takes no input:

- Run the program ${\textstyle p_{n}}$ , and record its runtime length ${\textstyle BB(n)}$ .
- Generate all programs with length ${\textstyle \leq 2n}$ . Run every one of them for up to ${\textstyle BB(n)}$ steps. Note the outputs of those that have halted.
- Output the string with the lowest lexicographic order that has not been output by any of those.

Let the string output by the program be ${\textstyle x}$ .

The program has length ${\textstyle \leq n+2\log _{2}n+O(1)}$ , where n comes from the length of the Busy Beaver ${\textstyle p_{n}}$ , $2\log _{2}n$ comes from using the (prefix-free) Elias delta code for the number n , and $O(1)$ comes from the rest of the program. Therefore, $K(x)\leq n+2\log _{2}n+O(1)\leq 2n$ for all big ${\textstyle n}$ . Further, since there are only so many possible programs with length ${\textstyle \leq 2n}$ , we have ${\textstyle l(x)\leq 2n+1}$ by pigeonhole principle. By assumption, ${\textstyle p_{K}(n)<BB(n)}$ , so every string of length ${\textstyle \leq 2n+1}$ has a minimal program with runtime ${\textstyle <BB(n)}$ . Thus, the string ${\textstyle x}$ has a minimal program with runtime ${\textstyle <BB(n)}$ . Further, that program has length ${\textstyle K(x)\leq 2n}$ . This contradicts how ${\textstyle x}$ was constructed.

## Universal probability

Fix a universal Turing machine U , the same one used to define the (prefix-free) Kolmogorov complexity. Define the (prefix-free) universal probability of a string x to be $P(x)=\sum _{U(p)=x}2^{-l(p)}$ In other words, it is the probability that, given a uniformly random binary stream as input, the universal Turing machine would halt after reading a certain prefix of the stream, and output x .

Note. $U(p)=x$ does not mean that the input stream is $p000\cdots$ , but that the universal Turing machine would halt at some point after reading the initial segment p , without reading any further input, and that, when it halts, it has written x to the output tape.

**Theorem.** (Theorem 14.11.1) $\log {\frac {1}{P(x)}}=K(x)+O(1)$

## Implications in biology

Kolmogorov complexity has been used in the context of biology to argue that the symmetries and modular arrangements observed in multiple species emerge from the tendency of evolution to prefer minimal Kolmogorov complexity. Considering the genome as a program that must solve a task or implement a series of functions, shorter programs would be preferred on the basis that they are easier to find by the mechanisms of evolution. An example of this approach is the eight-fold symmetry of the compass circuit that is found across insect species, which correspond to the circuit that is both functional and requires the minimum Kolmogorov complexity to be generated from self-replicating units.

## Conditional versions

The conditional Kolmogorov complexity of two strings $K(x|y)$ is, roughly speaking, defined as the Kolmogorov complexity of *x* given *y* as an auxiliary input to the procedure. So while the (unconditional) Kolmogorov complexity $K(x)$ of a sequence x is the length of the shortest binary program that outputs x on a universal computer and can be thought of as the minimal amount of information necessary to produce x , the conditional Kolmogorov complexity $K(x|y)$ is defined as the length of the shortest binary program that computes x when y is given as input, using a universal computer.

There is also a length-conditional complexity $K(x|L(x))$ , which is the complexity of *x* given the length of *x* as known/input.

## Time-bounded complexity

Time-bounded Kolmogorov complexity is a modified version of Kolmogorov complexity where the space of programs to be searched for a solution is confined to only programs that can run within some pre-defined number of steps. It is hypothesised that the possibility of the existence of an efficient algorithm for determining approximate time-bounded Kolmogorov complexity is related to the question of whether true one-way functions exist.
