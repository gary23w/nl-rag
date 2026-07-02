---
title: "Communication complexity"
source: https://en.wikipedia.org/wiki/Communication_complexity
domain: communication-complexity
license: CC-BY-SA-4.0
tags: communication complexity, two party protocol, fooling set, discrepancy method
fetched: 2026-07-02
---

# Communication complexity

In theoretical computer science, **communication complexity** studies the amount of communication required to solve a problem when the input to the problem is distributed among two or more parties. The study of communication complexity was first introduced by Andrew Yao in 1979, while studying the problem of computation distributed among several machines. The problem is usually stated as follows: two parties (traditionally called Alice and Bob) each receive a (potentially different) n -bit string x and y . The goal is for Alice to compute the value of a certain function, $f(x,y)$ , that depends on both x and y , with the least amount of communication between them.

While Alice and Bob can always succeed by having Bob send his whole n -bit string to Alice (who then computes the function f ), the idea here is to find clever ways of calculating *f* with fewer than n bits of communication. Note that, unlike in computational complexity theory, communication complexity is not concerned with the amount of computation performed by Alice or Bob, or the size of the memory used, as we generally assume nothing about the computational power of either Alice or Bob.

This abstract problem with two parties (called two-party communication complexity), and its general form with more than two parties, is relevant in many contexts. In VLSI circuit design, for example, one seeks to minimize energy used by decreasing the amount of electric signals passed between the different components during a distributed computation. The problem is also relevant in the study of data structures and in the optimization of computer networks. For surveys of the field, see the textbooks by Rao & Yehudayoff (2020) and Kushilevitz & Nisan (2006).

## Formal definition

Let $f:X\times Y\rightarrow Z$ where we assume in the typical case that $X=Y=\{0,1\}^{n}$ and $Z=\{0,1\}$ . Alice holds an n -bit string $x\in X$ while Bob holds an n -bit string $y\in Y$ . By communicating to each other one bit at a time (adopting some *communication protocol* that is agreed upon in advance), Alice and Bob wish to compute the value of $f(x,y)$ such that at least one party knows the value at the end of the communication. At this point the answer can be communicated back so that at the cost of one extra bit, both parties will know the answer. The worst case communication complexity of this communication problem of computing f , denoted as $D(f)$ , is then defined to be

$D(f)=$

minimum number of bits exchanged between Alice and Bob in the worst case.

As observed above, for any function $f:\{0,1\}^{n}\times \{0,1\}^{n}\rightarrow \{0,1\}$ , we have $D(f)\leq n$ . Using the above definition, it is useful to think of the function f as a matrix A (called the *input matrix* or *communication matrix*) where the rows are indexed by $x\in X$ and columns by $y\in Y$ . The entries of the matrix are $A_{x,y}=f(x,y)$ . Initially both Alice and Bob have a copy of the entire matrix A (assuming the function f is known to both parties). Then the problem of computing the function value can be rephrased as "zeroing-in" on the corresponding matrix entry. This problem can be solved if either Alice or Bob knows both x and y . At the start of communication, the number of choices for the matrix position corresponding to the inputs is the size of matrix, i.e. $2^{2n}$ . Then, as and when each party communicates a bit to the other, the number of choices for the position reduces, as this eliminates a set of rows/columns, resulting in a submatrix of A .

More formally, a set $R\subseteq X\times Y$ is called a *(combinatorial) rectangle* if whenever $(x_{1},y_{1})\in R$ and $(x_{2},y_{2})\in R$ then $(x_{1},y_{2})\in R$ . Equivalently, R is a combinatorial rectangle if it can be expressed as $R=M\times N$ for some $M\subseteq X$ and $N\subseteq Y$ . Consider the case when k bits are already exchanged between the parties. Now, for a particular $h\in \{0,1\}^{k}$ , let us define a matrix

$T_{h}=\{(x,y):{\text{ the }}k{\text{-bits exchanged on input }}(x,y){\text{ is }}h\}$

Then $T_{h}\subseteq X\times Y$ , and it is not hard to show that $T_{h}$ is a combinatorial rectangle in A .

### Example: *EQ*

We consider the case where Alice and Bob try to determine whether or not their input strings are equal. Formally, define the *Equality* function, denoted $EQ:\{0,1\}^{n}\times \{0,1\}^{n}\rightarrow \{0,1\}$ , by $EQ(x,y)=1$ if $x=y$ . As we demonstrate below, any deterministic communication protocol solving $EQ$ requires n bits of communication in the worst case. As a warm-up example, consider the simple case of $x,y\in \{0,1\}^{3}$ . The equality function in this case can be represented by the matrix below. The rows represent all the possibilities of x , the columns those of y .

EQ

000

001

010

011

100

101

110

111

000

1

0

0

0

0

0

0

0

001

0

1

0

0

0

0

0

0

010

0

0

1

0

0

0

0

0

011

0

0

0

1

0

0

0

0

100

0

0

0

0

1

0

0

0

101

0

0

0

0

0

1

0

0

110

0

0

0

0

0

0

1

0

111

0

0

0

0

0

0

0

1

In this table, the function only evaluates to 1 when x equals y (i.e., on the diagonal). It is also fairly easy to see how communicating a single bit divides someone's possibilities in half. When the first bit of y is 1, consider only half of the columns (where y can equal 100, 101, 110, or 111).

### Theorem: *D(EQ) = n*

Proof. Assume that $D(EQ)\leq n-1$ . This means that there exists $x\neq x'$ such that $(x,x)$ and $(x',x')$ have the same communication transcript h . Since this transcript defines a rectangle, $f(x,x')$ must also be 1. By definition $x\neq x'$ and we know that equality is only true for $(a,b)$ when $a=b$ . This yields a contradiction.

This technique of proving deterministic communication lower bounds is called the *fooling set* technique.

## Randomized communication complexity

In the above definition, we are concerned with the number of bits that must be *deterministically* transmitted between two parties. If both the parties are given access to a random number generator, can they determine the value of f with much less information exchanged? Yao, in his seminal paper answers this question by defining **randomized communication complexity**.

A randomized protocol R for a function f has two-sided error.

$\Pr[R(x,y)=0]>{\frac {2}{3}},{\textrm {if}}\,f(x,y)=0$

$\Pr[R(x,y)=1]>{\frac {2}{3}},{\textrm {if}}\,f(x,y)=1$

A randomized protocol is a deterministic protocol that uses an extra random string in addition to its normal input. There are two models for this: a *public string* is a random string that is known by both parties beforehand, while a *private string* is generated by one party and must be communicated to the other party. A theorem presented below shows that any public string protocol can be simulated by a private string protocol that uses *O(log n)* additional bits compared to the original.

In the probability inequalities above, the outcome of the protocol is understood to depend *only* on the random string; both strings *x* and *y* remain fixed. In other words, if *R*(*x*,*y*) yields *g*(*x*,*y*,*r*) when using random string *r*, then *g*(*x*,*y*,*r*) = *f*(*x*,*y*) for at least 2/3 of all choices for the string *r*.

The randomized complexity is simply defined as the number of bits exchanged in such a protocol.

Note that it is also possible to define a randomized protocol with one-sided error, and the complexity is defined similarly.

### Example: EQ

Returning to the previous example of *EQ*, if certainty is not required, Alice and Bob can check for equality using only ⁠ $O(\log n)$ ⁠ messages. Consider the following protocol: Assume that Alice and Bob both have access to the same random string $z\in \{0,1\}^{n}$ . Alice computes $z\cdot x$ and sends this bit (call it *b*) to Bob. (The $(\cdot )$ is the dot product in GF(2).) Then Bob compares *b* to $z\cdot y$ . If they are the same, then Bob accepts, saying *x* equals *y*. Otherwise, he rejects.

Clearly, if $x=y$ , then $z\cdot x=z\cdot y$ , so $Prob_{z}[Accept]=1$ . If *x* does not equal *y*, it is still possible that $z\cdot x=z\cdot y$ , which would give Bob the wrong answer. How does this happen?

If *x* and *y* are not equal, they must differ in some locations:

${\begin{cases}x=c_{1}c_{2}\ldots p\ldots p'\ldots x_{n}\\y=c_{1}c_{2}\ldots q\ldots q'\ldots y_{n}\\z=z_{1}z_{2}\ldots z_{i}\ldots z_{j}\ldots z_{n}\end{cases}}$

Where x and y agree, $z_{i}*x_{i}=z_{i}*c_{i}=z_{i}*y_{i}$ so those terms affect the dot products equally. We can safely ignore those terms and look only at where x and y differ. Furthermore, we can swap the bits $x_{i}$ and $y_{i}$ without changing whether or not the dot products are equal. This means we can swap bits so that x contains only zeros and y contains only ones:

${\begin{cases}x'=00\ldots 0\\y'=11\ldots 1\\z'=z_{1}z_{2}\ldots z_{n'}\end{cases}}$

Note that $z'\cdot x'=0$ and $z'\cdot y'=\Sigma _{i}z'_{i}$ . Now, the question becomes: for some random string $z'$ , what is the probability that $\Sigma _{i}z'_{i}=0$ ? Since each $z'_{i}$ is equally likely to be 0 or 1, this probability is just $1/2$ . Thus, when x does not equal y, $Prob_{z}[Accept]=1/2$ . The algorithm can be repeated many times to increase its accuracy. This fits the requirements for a randomized communication algorithm.

This shows that *if Alice and Bob share a random string of length n*, they can send one bit to each other to compute $EQ(x,y)$ . In the next section, it is shown that Alice and Bob can exchange only ⁠ $O(\log n)$ ⁠ bits that are as good as sharing a random string of length *n*. Once that is shown, it follows that *EQ* can be computed in ⁠ $O(\log n)$ ⁠ messages.

### Example: GH

For yet another example of randomized communication complexity, we turn to an example known as the *gap-Hamming problem* (abbreviated *GH*). Formally, Alice and Bob both maintain binary messages, $x,y\in \{-1,+1\}^{n}$ and would like to determine if the strings are very similar or if they are not very similar. In particular, they would like to find a communication protocol requiring the transmission of as few bits as possible to compute the following partial Boolean function,

${\text{GH}}_{n}(x,y):={\begin{cases}-1&\langle x,y\rangle \leq {\sqrt {n}}\\+1&\langle x,y\rangle \geq {\sqrt {n}}.\end{cases}}$

Clearly, they must communicate all their bits if the protocol is to be deterministic (this is because, if there is a deterministic, strict subset of indices that Alice and Bob relay to one another, then imagine having a pair of strings that on that set disagree in ${\sqrt {n}}-1$ positions. If another disagreement occurs in any position that is not relayed, then this affects the result of ${\text{GH}}_{n}(x,y)$ , and hence would result in an incorrect procedure.

A natural question one then asks is, if we're permitted to err $1/3$ of the time (over random instances $x,y$ drawn uniformly at random from $\{-1,+1\}^{n}$ ), then can we get away with a protocol with fewer bits? It turns out that the answer somewhat surprisingly is no, due to a result of Chakrabarti and Regev in 2012: they show that for random instances, any procedure that is correct at least $2/3$ of the time must send $\Omega (n)$ bits worth of communication, which is to say essentially all of them.

### Public coins versus private coins

Creating random protocols becomes easier when both parties have access to the same random string, known as a shared string protocol. However, even in cases where the two parties do not share a random string, it is still possible to use private string protocols with only a small communication cost. Any shared string random protocol using any number of random string can be simulated by a private string protocol that uses an extra *O(log n)* bits.

Intuitively, we can find some set of strings that has enough randomness in it to run the random protocol with only a small increase in error. This set can be shared beforehand, and instead of drawing a random string, Alice and Bob need only agree on which string to choose from the shared set. This set is small enough that the choice can be communicated efficiently. A formal proof follows.

Consider some random protocol *P* with a maximum error rate of 0.1. Let R be $100n$ strings of length *n*, numbered $r_{1},r_{2},\dots ,r_{100n}$ . Given such an R , define a new protocol $P'_{R}$ that randomly picks some $r_{i}$ and then runs *P* using $r_{i}$ as the shared random string. It takes *O*(log 100*n*) = *O*(log *n*) bits to communicate the choice of $r_{i}$ .

Let us define $p(x,y)$ and $p'_{R}(x,y)$ to be the probabilities that P and $P'_{R}$ compute the correct value for the input $(x,y)$ .

For a fixed $(x,y)$ , we can use Hoeffding's inequality to get the following equation:

$\Pr _{R}[|p'_{R}(x,y)-p(x,y)|\geq 0.1]\leq 2\exp(-2(0.1)^{2}\cdot 100n)<2^{-2n}$

Thus when we don't have $(x,y)$ fixed:

$\Pr _{R}[\exists (x,y):\ |p'_{R}(x,y)-p(x,y)|\geq 0.1]\leq \sum _{(x,y)}\Pr _{R}[|p'_{R}(x,y)-p(x,y)|\geq 0.1]<\sum _{(x,y)}2^{-2n}=1$

The last equality above holds because there are $2^{2n}$ different pairs $(x,y)$ . Since the probability does not equal 1, there is some $R_{0}$ so that for all $(x,y)$ :

$|p'_{R_{0}}(x,y)-p(x,y)|<0.1$

Since P has at most 0.1 error probability, $P'_{R_{0}}$ can have at most 0.2 error probability.

### Collapse of randomized communication complexity

Let's say we additionally allow Alice and Bob to share some resource, for example a pair of entangled particles. Using that ressource, Alice and Bob can correlate their information and thus try to 'collapse' (or 'trivialize') communication complexity in the following sense.

**Definition.** *A resource R is said to be*"collapsing"*if, using that resource R , only one bit of classical communication is enough for Alice to know the evaluation $f(x,y)$ in the worst case scenario for any Boolean function f .*

The surprising fact of a collapse of communication complexity is that the function f can have arbitrarily large entry size, but still the number of communication bit is constant to a single one.

Some resources are shown to be non-collapsing, such as quantum correlations or more generally almost-quantum correlations, whereas on the contrary some other resources are shown to collapse randomized communication complexity, such as the PR-box, or some noisy PR-boxes satisfying some conditions.

### Distributional complexity

One approach to studying randomized communication complexity is through distributional complexity.

Given a joint distribution $\mu$ on the inputs of both players, the corresponding distributional complexity of a function f is the minimum cost of a *deterministic* protocol R such that $\Pr[f(x,y)=R(x,y)]\geq 2/3$ , where the inputs are sampled according to $\mu$ .

Yao's minimax principle (a special case of von Neumann's minimax theorem) states that the randomized communication complexity of a function equals its maximum distributional complexity, where the maximum is taken over all joint distributions of the inputs (not necessarily product distributions!).

Yao's principle can be used to prove lower bounds on the randomized communication complexity of a function: design the appropriate joint distribution, and prove a lower bound on the distributional complexity. Since distributional complexity concerns deterministic protocols, this could be easier than proving a lower bound on randomized protocols directly.

As an example, let us consider the *disjointness* function DISJ: each of the inputs is interpreted as a subset of $\{1,\dots ,n\}$ , and DISJ(x,y)=1 if the two sets are disjoint. Razborov proved an $\Omega (n)$ lower bound on the randomized communication complexity by considering the following distribution: with probability 3/4, sample two random disjoint sets of size $n/4$ , and with probability 1/4, sample two random sets of size $n/4$ with a unique intersection.

### Information complexity

A powerful approach to the study of distributional complexity is information complexity. Initiated by Bar-Yossef, Jayram, Kumar and Sivakumar, the approach was codified in work of Barak, Braverman, Chen and Rao and by Braverman and Rao.

The (internal) information complexity of a (possibly randomized) protocol R with respect to a distribution μ is defined as follows. Let $(X,Y)\sim \mu$ be random inputs sampled according to μ, and let Π be the transcript of R when run on the inputs $X,Y$ . The information complexity of the protocol is

$\operatorname {IC} _{\mu }(R)=I(\Pi ;Y|X)+I(\Pi ;X|Y),$

where I denotes conditional mutual information. The first summand measures the amount of information that Alice learns about Bob's input from the transcript, and the second measures the amount of information that Bob learns about Alice's input.

The ε-error information complexity of a function f with respect to a distribution μ is the infimal information complexity of a protocol for f whose error (with respect to μ) is at most ε.

Braverman and Rao proved that information equals amortized communication. This means that the cost for solving n independent copies of f is roughly n times the information complexity of f. This is analogous to the well-known interpretation of Shannon entropy as the amortized bit-length required to transmit data from a given information source. Braverman and Rao's proof uses a technique known as "protocol compression", in which an information-efficient protocol is "compressed" into a communication-efficient protocol.

The techniques of information complexity enable the computation of the exact (up to first order) communication complexity of set disjointness to be $1.4923\ldots n$ .

Information complexity techniques have also been used to analyze extended formulations, proving an essentially optimal lower bound on the complexity of algorithms based on linear programming that approximately solve the maximum clique problem.

Omri Weinstein's 2015 survey surveys the subject.

## Quantum communication complexity

Quantum communication complexity tries to quantify the communication reduction possible by using quantum effects during a distributed computation.

At least three quantum generalizations of communication complexity have been proposed; for a survey see the suggested text by G. Brassard.

The first one is the qubit-communication model, where the parties can use quantum communication instead of classical communication, for example by exchanging photons through an optical fiber.

In a second model the communication is still performed with classical bits, but the parties are allowed to manipulate an unlimited supply of quantum entangled states as part of their protocols. By doing measurements on their entangled states, the parties can save on classical communication during a distributed computation (see an application in Collapse of Randomized Communication Complexity).

The third model involves access to previously shared entanglement in addition to qubit communication, and is the least explored of the three quantum models.

## Nondeterministic communication complexity

In nondeterministic communication complexity, Alice and Bob have access to an oracle. After receiving the oracle's word, the parties communicate to deduce $f(x,y)$ . The nondeterministic communication complexity is then the maximum over all pairs $(x,y)$ over the sum of number of bits exchanged and the coding length of the oracle word.

Viewed differently, this amounts to covering all 1-entries of the 0/1-matrix by combinatorial 1-rectangles (i.e., non-contiguous, non-convex submatrices, whose entries are all one (see Kushilevitz and Nisan or Dietzfelbinger et al.)). The nondeterministic communication complexity is the binary logarithm of the *rectangle covering number* of the matrix: the minimum number of combinatorial 1-rectangles required to cover all 1-entries of the matrix, without covering any 0-entries.

Nondeterministic communication complexity occurs as a means to obtaining lower bounds for deterministic communication complexity (see Dietzfelbinger et al.), but also in the theory of nonnegative matrices, where it gives a lower bound on the nonnegative rank of a nonnegative matrix.

## Unbounded-error communication complexity

In the unbounded-error setting, Alice and Bob have access to a private coin and their own inputs $(x,y)$ . In this setting, Alice succeeds if she responds with the correct value of $f(x,y)$ with probability strictly greater than 1/2. In other words, if Alice's responses have *any* non-zero correlation to the true value of $f(x,y)$ , then the protocol is considered valid.

Note that the requirement that the coin is *private* is essential. In particular, if the number of public bits shared between Alice and Bob are not counted against the communication complexity, it is easy to argue that computing any function has $O(1)$ communication complexity. On the other hand, both models are equivalent if the number of public bits used by Alice and Bob is counted against the protocol's total communication.

Though subtle, lower bounds on this model are extremely strong. More specifically, it is clear that any bound on problems of this class immediately imply equivalent bounds on problems in the deterministic model and the private and public coin models, but such bounds also hold immediately for nondeterministic communication models and quantum communication models.

Forster was the first to prove explicit lower bounds for this class, showing that computing the inner product $\langle x,y\rangle$ requires at least $\Omega (n)$ bits of communication, though an earlier result of Alon, Frankl, and Rödl proved that the communication complexity for almost all Boolean functions $f:\{0,1\}^{n}\times \{0,1\}^{n}\to \{0,1\}$ is $\Omega (n)$ .

## Lifting

Lifting is a general technique in complexity theory in which a lower bound on a simple measure of complexity is "lifted" to a lower bound on a more difficult measure.

This technique was pioneered in the context of communication complexity by Raz and McKenzie, who proved the first query-to-communication lifting theorem, and used the result to separate the monotone NC hierarchy.

Given a function $f\colon \{0,1\}^{n}\to \{0,1\}$ and a gadget $g\colon \{0,1\}^{a}\times \{0,1\}^{b}\to \{0,1\}$ , their composition $f\circ g\colon \{0,1\}^{na}\times \{0,1\}^{nb}\to \{0,1\}$ is defined as follows:

$(f\circ g)(x,y)=f(g(x_{1,1}\cdots x_{1,a},y_{1,1}\cdots y_{1,b}),\dots ,g(x_{n,1}\cdots x_{n,a},y_{n,1}\cdots y_{n,b})).$

In words, x is partitioned into n blocks of length a , and y is partitioned into n blocks of length b . The gadget is applied n times on the blocks, and the outputs are fed into f . Diagrammatically:

In this diagram, each of the inputs $\mathbf {x} _{1},\dots ,\mathbf {x} _{n}$ is a bits long, and each of the inputs $\mathbf {y} _{1},\dots ,\mathbf {y} _{n}$ is b bits long.

A decision tree of depth $\Delta$ for f can be translated to a communication protocol whose cost is $\Delta \cdot D(g)$ : each time the tree queries a bit, the corresponding value of g is computed using an optimal protocol for g . Raz and McKenzie showed that this is optimal up to a constant factor when g is the so-called "indexing gadget", in which x has length $c\log n$ (for a large enough constant c), y has length $n^{c}$ , and $g(x,y)$ is the x -th bit of y .

The proof of the Raz–McKenzie lifting theorem uses the method of simulation, in which a protocol for the composed function $f\circ g$ is used to generate a decision tree for f . Göös, Pitassi and Watson gave an exposition of the original proof. Since then, several works have proved similar theorems with different gadgets, such as inner product. The smallest gadget that can be handled is the indexing gadget with $c=1+\epsilon$ . Göös, Pitassi and Watson extended the Raz–McKenzie technique to randomized protocols.

A simple modification of the Raz–McKenzie lifting theorem gives a lower bound of $\Delta \cdot D(g)$ on the logarithm of the size of a protocol tree for computing $f\circ g$ , where $\Delta$ is the depth of the optimal decision tree for f . Garg, Göös, Kamath and Sokolov extended this to the DAG-like setting, and used their result to obtain monotone circuit lower bounds. The same technique has also yielded applications to proof complexity.

A different type of lifting is exemplified by Sherstov's pattern matrix method, which gives a lower bound on the quantum communication complexity of $f\circ g$ , where g is a modified indexing gadget, in terms of the approximate degree of f. The approximate degree of a Boolean function is the minimal degree of a polynomial that approximates the function on all Boolean points up to an additive error of 1/3.

In contrast to the Raz–McKenzie proof, which uses the method of simulation, Sherstov's proof takes a *dual witness* to the approximate degree of f and gives a lower bound on the quantum query complexity of $f\circ g$ using the *generalized discrepancy method*. The dual witness for the approximate degree of f is a lower bound witness for the approximate degree obtained via LP duality. This dual witness is massaged into other objects constituting data for the generalized discrepancy method.

Another example of this approach is the work of Pitassi and Robere, in which an *algebraic gap* is lifted to a lower bound on Razborov's *rank measure*. The result is a strongly exponential lower bound on the monotone circuit complexity of an explicit function, obtained via the Karchmer–Wigderson characterization of monotone circuit size in terms of communication complexity.

## Open problems

Considering a 0 or 1 input matrix $M_{f}=[f(x,y)]_{x,y\in \{0,1\}^{n}}$ , the minimum number of bits exchanged to compute f deterministically in the worst case, $D(f)$ , is known to be bounded from below by the logarithm of the rank of the matrix $M_{f}$ . The log rank conjecture proposes that the communication complexity, $D(f)$ , is bounded from above by a constant power of the logarithm of the rank of $M_{f}$ . Since D(f) is bounded from above and below by polynomials of log rank $(M_{f})$ , we can say D(f) is polynomially related to log rank $(M_{f})$ . Since the rank of a matrix is polynomial time computable in the size of the matrix, such an upper bound would allow the matrix's communication complexity to be approximated in polynomial time. Note, however, that the size of the matrix itself is exponential in the size of the input.

For a randomized protocol, the number of bits exchanged in the worst case, R(f), was conjectured to be polynomially related to the following formula:

$\log \min({\textrm {rank}}(M'_{f}):M'_{f}\in \mathbb {R} ^{2^{n}\times 2^{n}},(M_{f}-M'_{f})_{\infty }\leq 1/3).$

Such log rank conjectures are valuable because they reduce the question of a matrix's communication complexity to a question of linearly independent rows (columns) of the matrix. This particular version, called the Log-Approximate-Rank Conjecture, was recently refuted by Chattopadhyay, Mande and Sherif (2019) using a surprisingly simple counter-example. This reveals that the essence of the communication complexity problem, for example in the EQ case above, is figuring out where in the matrix the inputs are, in order to find out if they're equivalent.

## Applications

Lower bounds in communication complexity can be used to prove lower bounds in decision tree complexity, VLSI circuits, data structures, streaming algorithms, space–time tradeoffs for Turing machines and more.

Conitzer and Sandholm studied the communication complexity of some common voting rules, which are essential in political and non political organizations. Compilation complexity is a closely related notion, which can be seen as a single-round communication complexity.

Nayebi has studied the communication complexity of unbounded and bounded Bayesians, establishing no-free-lunch theorems (lower bounds) on AI alignment.
