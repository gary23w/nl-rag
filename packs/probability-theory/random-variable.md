---
title: "Random variable"
source: https://en.wikipedia.org/wiki/Random_variable
domain: probability-theory
license: CC-BY-SA-4.0
tags: probability theory, random variable, probability space, law of large numbers
fetched: 2026-07-02
---

# Random variable

A **random variable** (also called **random quantity**, **aleatory variable**, or **stochastic variable**) is a mathematical formalization of a quantity or object which depends on random events. The term 'random variable' in its mathematical definition refers to neither randomness nor variability but instead is a mathematical function in which

- the domain is the set of possible outcomes in a sample space (e.g. the set $\{H,T\}$ (which are the possible upper sides of a flipped coin heads H or tails T as the result from tossing a coin); and
- the range is a measurable space (e.g. corresponding to the domain above, the range might be the set $\{-1,1\}$ if say heads H mapped to −1 and T mapped to 1). Typically, the range of a random variable is a subset of the real numbers.

Informally, randomness typically represents some fundamental element of chance, such as in the roll of a die; it may also represent uncertainty, such as measurement error. However, the interpretation of probability is philosophically complicated, and even in specific cases is not always straightforward. The purely mathematical analysis of random variables is independent of such interpretational difficulties, and can be based upon a rigorous axiomatic setup.

In the formal mathematical language of measure theory, a random variable is defined as a measurable function from a probability measure space (called the *sample space*) to a measurable space. This allows consideration of the pushforward measure, which is called the *distribution* of the random variable; the distribution is thus a probability measure on the set of all possible values of the random variable. It is possible for two random variables to have identical distributions but to differ in significant ways; for instance, they may be independent.

It is common to consider the special cases of discrete random variables and absolutely continuous random variables, corresponding to whether a random variable is valued in a countable subset or in an interval of real numbers. There are other important possibilities, especially in the theory of stochastic processes, wherein it is natural to consider random sequences or random functions. Sometimes a *random variable* is taken to be automatically valued in the real numbers, with more general random quantities instead being called *random elements*. A *random variate* is a particular outcome or realization of a random variable.

According to George Mackey, Pafnuty Chebyshev was the first person "to think systematically in terms of random variables".

## Definition

A **random variable** X is a measurable function $X\colon \Omega \to E$ from a sample space $\Omega$ as a set of possible outcomes to a measurable space E . For the measurability of X to be meaningful, the sample space $\Omega$ needs to belong to a probability triple $(\Omega ,{\mathcal {F}},\operatorname {P} )$ (see the measure-theoretic definition). A random variable is often denoted by capital Roman letters such as $X,Y,Z,T$ .

The probability that X takes on a value in a measurable set $S\subseteq E$ is written as

$\operatorname {P} (X\in S)=\operatorname {P} (\{\omega \in \Omega \mid X(\omega )\in S\})$

.

### Standard case

In many cases, X is real-valued, i.e. $E=\mathbb {R}$ . In some contexts, the term random element (see extensions) is used to denote a random variable not of this form.

When the image (or range) of X is finite or countably infinite, the random variable is called a **discrete random variable** and its distribution is a discrete probability distribution, i.e. can be described by a probability mass function that assigns a probability to each value in the image of X . If the image is uncountably infinite (usually an interval) then X is called a **continuous random variable**. In the special case that it is absolutely continuous, its distribution can be described by a probability density function, which assigns probabilities to intervals; in particular, each individual point must necessarily have probability zero for an absolutely continuous random variable. Not all continuous random variables are absolutely continuous.

Any random variable can be described by its cumulative distribution function, which describes the probability that the random variable will be less than or equal to a certain value.

### Extensions

The term "random variable" in statistics is traditionally limited to the real-valued case (⁠ $E=\mathbb {R}$ ⁠). In this case, the structure of the real numbers makes it possible to define quantities such as the expected value and variance of a random variable, its cumulative distribution function, and the moments of its distribution.

However, the definition above is valid for any measurable space E of values. Thus one can consider random elements of other sets E , such as random Boolean values, categorical values, complex numbers, vectors, matrices, sequences, trees, sets, shapes, manifolds, and functions. One may then specifically refer to a *random variable of type E*, or an *E -valued random variable*.

This more general concept of a random element is particularly useful in disciplines such as graph theory, machine learning, natural language processing, and other fields in discrete mathematics and computer science, where one is often interested in modeling the random variation of non-numerical data structures. In some cases, it is nonetheless convenient to represent each element of E , using one or more real numbers. In this case, a random element may optionally be represented as a vector of real-valued random variables (all defined on the same underlying probability space $\Omega$ , which allows the different random variables to covary). For example:

- A random word may be represented as a random integer that serves as an index into the vocabulary of possible words. Alternatively, it can be represented as a random indicator vector, whose length equals the size of the vocabulary, where the only values of positive probability are $(1\ 0\ 0\ 0\ \cdots )$ , $(0\ 1\ 0\ 0\ \cdots )$ , $(0\ 0\ 1\ 0\ \cdots )$ and the position of the 1 indicates the word.
- A random sentence of given length N may be represented as a vector of N random words.
- A random graph on N given vertices may be represented as a $N\times N$ matrix of random variables, whose values specify the adjacency matrix of the random graph.
- A random function F may be represented as a collection of random variables $F(x)$ , giving the function's values at the various points x in the function's domain. The $F(x)$ are ordinary real-valued random variables provided that the function is real-valued. For example, a stochastic process is a random function of time, a random vector is a random function of some index set such as $1,2,\ldots ,n$ , and a random field is a random function on any set (typically time, space, or a discrete set).

## Distribution functions

If a random variable $X\colon \Omega \to \mathbb {R}$ defined on the probability space $(\Omega ,{\mathcal {F}},\operatorname {P} )$ is given, we can ask questions like "How likely is it that the value of X is equal to 2?". This is the same as the probability of the event $\{\omega :X(\omega )=2\}\,\!$ which is often written as $P(X=2)\,\!$ or $p_{X}(2)$ for short.

Recording all these probabilities of outputs of a random variable X yields the probability distribution of X . The probability distribution "forgets" about the particular probability space used to define X and only records the probabilities of various output values of X . Such a probability distribution, if X is real-valued, can always be captured by its cumulative distribution function

$F_{X}(x)=\operatorname {P} (X\leq x)$

and sometimes also using a probability density function, $f_{X}$ . In measure-theoretic terms, we use the random variable X to "push-forward" the measure P on $\Omega$ to a measure $p_{X}$ on $\mathbb {R}$ . The measure $p_{X}$ is called the "(probability) distribution of X " or the "law of X ". The density $f_{X}=dp_{X}/d\mu$ , the Radon–Nikodym derivative of $p_{X}$ with respect to some reference measure $\mu$ on $\mathbb {R}$ (often, this reference measure is the Lebesgue measure in the case of continuous random variables, or the counting measure in the case of discrete random variables). The underlying probability space $\Omega$ is a technical device used to guarantee the existence of random variables, sometimes to construct them, and to define notions such as correlation and dependence or independence based on a joint distribution of two or more random variables on the same probability space. In practice, one often disposes of the space $\Omega$ altogether and just puts a measure on $\mathbb {R}$ that assigns measure 1 to the whole real line, i.e., one works with probability distributions instead of random variables. See the article on quantile functions for fuller development.

## Examples

### Discrete random variable

Consider an experiment where a person is chosen at random. An example of a random variable may be the person's height. Mathematically, the random variable is interpreted as a function which maps the person to their height. Associated with the random variable is a probability distribution that allows the computation of the probability that the height is in any subset of possible values, such as the probability that the height is between 180 and 190 cm, or the probability that the height is either less than 150 or more than 200 cm.

Another random variable may be the person's number of children; this is a discrete random variable with non-negative integer values. It allows the computation of probabilities for individual integer values – the probability mass function (PMF) – or for sets of values, including infinite sets. For example, the event of interest may be "an even number of children". For both finite and infinite event sets, their probabilities can be found by adding up the PMFs of the elements; that is, the probability of an even number of children is the infinite sum ⁠ $\operatorname {PMF} (0)+\operatorname {PMF} (2)+\operatorname {PMF} (4)+\cdots$ ⁠.

In examples such as these, the sample space is often suppressed, since it is mathematically hard to describe, and the possible values of the random variables are then treated as a sample space. But when two random variables are measured on the same sample space of outcomes, such as the height and number of children being computed on the same random persons, it is easier to track their relationship if it is acknowledged that both height and number of children come from the same random person, for example so that questions of whether such random variables are correlated or not can be posed.

If ${\textstyle \{a_{n}\},\{b_{n}\}}$ are countable sets of real numbers, ${\textstyle b_{n}>0}$ and ⁠ $\textstyle \sum _{n}b_{n}=1$ ⁠, then ${\textstyle F=\sum _{n}b_{n}\delta _{a_{n}}(x)}$ is a discrete distribution function. Here $\delta _{t}(x)=0$ for ⁠ $x<t$ ⁠, ⁠ $\delta _{t}(x)=1$ ⁠ for ⁠ $x\geq t$ ⁠. Taking for instance an enumeration of all rational numbers as ⁠ $\{a_{n}\}$ ⁠, one gets a discrete function that is not necessarily a step function (piecewise constant).

#### Coin toss

The possible outcomes for one coin toss can be described by the sample space $\Omega =\{{\text{heads}},{\text{tails}}\}$ . We can introduce a real-valued random variable Y that models a $1 payoff for a successful bet on heads as follows: $Y(\omega )={\begin{cases}1,&{\text{if }}\omega ={\text{heads}},\\[6pt]0,&{\text{if }}\omega ={\text{tails}}.\end{cases}}$

If the coin is a fair coin, ⁠ Y ⁠ has a probability mass function $f_{Y}$ given by: $f_{Y}(y)={\begin{cases}{\tfrac {1}{2}},&{\text{if }}y=1,\\[6pt]{\tfrac {1}{2}},&{\text{if }}y=0,\end{cases}}$

#### Dice roll

A random variable can also be used to describe the process of rolling dice and the possible outcomes. The most obvious representation for the two-dice case is to take the set of pairs of numbers *n*1 and *n*2 from {1, 2, 3, 4, 5, 6} (representing the numbers on the two dice) as the sample space. The total number rolled (the sum of the numbers in each pair) is then a random variable *X* given by the function that maps the pair to the sum: $X((n_{1},n_{2}))=n_{1}+n_{2}$ and (if the dice are fair) has a probability mass function *f**X* given by: $f_{X}(S)={\frac {\min(S-1,13-S)}{36}},{\text{ for }}S\in \{2,3,4,5,6,7,8,9,10,11,12\}$

### Continuous random variable

Formally, a continuous random variable is a random variable whose cumulative distribution function is continuous everywhere. There are no "gaps", which would correspond to numbers which have a finite probability of occurring. Instead, continuous random variables almost never take an exact prescribed value *c* (formally, ${\textstyle \forall c\in \mathbb {R}$ ) but there is a positive probability that its value will lie in particular intervals which can be arbitrarily small. Continuous random variables usually admit probability density functions (PDF), which characterize their CDF and probability measures; such distributions are also called absolutely continuous; but some continuous distributions are singular, or mixes of an absolutely continuous part and a singular part.

An example of a continuous random variable would be one based on a spinner that can choose a horizontal direction. Then the values taken by the random variable are directions. We could represent these directions by North, West, East, South, Southeast, etc. However, it is commonly more convenient to map the sample space to a random variable which takes values which are real numbers. This can be done, for example, by mapping a direction to a bearing in degrees clockwise from North. The random variable then takes values which are real numbers from the interval [0, 360), with all parts of the range being "equally likely". In this case, ***X*** = the angle spun. Any real number has probability zero of being selected, but a positive probability can be assigned to any *range* of values. For example, the probability of choosing a number in [0, 180] is ⁠1/2⁠. Instead of speaking of a probability mass function, we say that the probability *density* of ***X*** is 1/360. The probability of a subset of [0, 360) can be calculated by multiplying the measure of the set by 1/360. In general, the probability of a set for a given continuous random variable can be calculated by integrating the density over the given set.

More formally, given any interval ${\textstyle I=[a,b]=\{x\in \mathbb {R} :a\leq x\leq b\}}$ , a random variable $X_{I}\sim \operatorname {U} (I)=\operatorname {U} [a,b]$ is called a "continuous uniform random variable" (CURV) if the probability that it takes a value in a subinterval depends only on the length of the subinterval. This implies that the probability of $X_{I}$ falling in any subinterval $[c,d]\subseteq [a,b]$ is proportional to the length of the subinterval, that is, if *a* ≤ *c* ≤ *d* ≤ *b*, one has $\Pr \left(X_{I}\in [c,d]\right)={\frac {d-c}{b-a}}$ where the last equality results from the unitarity axiom of probability. The probability density function of a CURV $X\sim \operatorname {U} [a,b]$ is given by the indicator function of its interval of support normalized by the interval's length: $f_{X}(x)={\begin{cases}\displaystyle {1 \over b-a},&a\leq x\leq b\\0,&{\text{otherwise}}.\end{cases}}$ Of particular interest is the uniform distribution on the unit interval $[0,1]$ . Samples of any desired probability distribution $\operatorname {D}$ can be generated by calculating the quantile function of $\operatorname {D}$ on a randomly-generated number distributed uniformly on the unit interval. This exploits properties of cumulative distribution functions, which are a unifying framework for all random variables.

### Mixed type

A **mixed random variable** is a random variable whose cumulative distribution function is neither discrete nor everywhere-continuous. It can be realized as a mixture of a discrete random variable and a continuous random variable; in which case the CDF will be the weighted average of the CDFs of the component variables.

An example of a random variable of mixed type would be based on an experiment where a coin is flipped and the spinner is spun only if the result of the coin toss is heads. If the result is tails, ***X*** = −1; otherwise ***X*** is the value of the spinner as in the preceding example. There is a probability of ⁠1/2⁠ that this random variable will have the value −1. Other ranges of values would have half the probabilities of the last example.

Most generally, every probability distribution on the real line is a mixture of discrete part, singular part, and an absolutely continuous part; see *Lebesgue's decomposition theorem § Refinement*. The discrete part is concentrated on a countable set, but this set may be dense (like the set of all rational numbers).

## Measure-theoretic definition

The most formal, axiomatic definition of a random variable involves measure theory. Continuous random variables are defined in terms of sets of numbers, along with functions that map such sets to probabilities. Because of various difficulties (e.g. the Banach–Tarski paradox) that arise if such sets are insufficiently constrained, it is necessary to introduce what is termed a sigma-algebra to constrain the possible sets over which probabilities can be defined. Normally, a particular such sigma-algebra is used, the Borel σ-algebra, which allows for probabilities to be defined over any sets that can be derived either directly from continuous intervals of numbers or by a finite or countably infinite number of unions and/or intersections of such intervals.

The measure-theoretic definition is as follows.

Let $(\Omega ,{\mathcal {F}},P)$ be a probability space and $(E,{\mathcal {E}})$ a measurable space. Then an **$(E,{\mathcal {E}})$ -valued random variable** is a measurable function ⁠ $X:\Omega \to E$ ⁠, which means that, for every subset ⁠ $B\in {\mathcal {E}}$ ⁠, its preimage is ${\mathcal {F}}$ -measurable; $X^{-1}(B)\in {\mathcal {F}}$ , where $X^{-1}(B)=\{\omega :X(\omega )\in B\}$ . This definition enables us to measure any subset $B\in {\mathcal {E}}$ in the target space by looking at its preimage, which by assumption is measurable.

In more intuitive terms, a member of $\Omega$ is a possible outcome, a member of ${\mathcal {F}}$ is a measurable subset of possible outcomes, the function P gives the probability of each such measurable subset, E represents the set of values that the random variable can take (such as the set of real numbers), and a member of ${\mathcal {E}}$ is a "well-behaved" (measurable) subset of E (those for which the probability may be determined). The random variable is then a function from any outcome to a quantity, such that the outcomes leading to any useful subset of quantities for the random variable have a well-defined probability.

When E is a topological space, then the most common choice for the σ-algebra ${\mathcal {E}}$ is the Borel σ-algebra ⁠ ${\mathcal {B}}(E)$ ⁠, which is the σ-algebra generated by the collection of all open sets in E . In such case the $(E,{\mathcal {E}})$ -valued random variable is called an **E -valued random variable**. Moreover, when the space E is the real line $\mathbb {R}$ , then such a real-valued random variable is called simply a **random variable**. Note that we are not giving $\mathbb {R}$ the usual Lebesgue $\sigma$ -algebra, which is the completion of the Borel $\sigma$ -algebra. This choice allows for more measurable functions $f:\Omega \to \mathbb {R}$ and makes it easier to check that a function $f:\Omega \to \mathbb {R}$ is measurable, as we only need to check that preimages of open sets are measurable.

### Real-valued random variables

In this case the observation space is the set of real numbers. Recall, $(\Omega ,{\mathcal {F}},P)$ is the probability space. For a real observation space, the function $X\colon \Omega \rightarrow \mathbb {R}$ is a real-valued random variable if

$\{\omega :X(\omega )\leq r\}\in {\mathcal {F}}\qquad \forall r\in \mathbb {R} .$

This definition is a special case of the above because the set $\{(-\infty ,r]:r\in \mathbb {R} \}$ generates the Borel σ-algebra on the set of real numbers, and it suffices to check measurability on any generating set. Here we can prove measurability on this generating set by using the fact that ⁠ $\{\omega :X(\omega )\leq r\}=X^{-1}((-\infty ,r])$ ⁠.

## Moments

The probability distribution of a random variable is often characterised by a small number of parameters, which also have a practical interpretation. For example, it is often enough to know what its "average value" is. This is captured by the mathematical concept of expected value of a random variable, denoted $\operatorname {E} [X]$ , and also called the **first moment.** In general, $\operatorname {E} [f(X)]$ is not equal to $f(\operatorname {E} [X])$ . Once the "average value" is known, one could then ask how far from this average value the values of X typically are, a question that is answered by the variance and standard deviation of a random variable. $\operatorname {E} [X]$ can be viewed intuitively as an average obtained from an infinite population, the members of which are particular evaluations of X .

Mathematically, this is known as the (generalised) problem of moments: for a given class of random variables X , find a collection $\{f_{i}\}$ of functions such that the expectation values $\operatorname {E} [f_{i}(X)]$ fully characterise the distribution of the random variable X .

Moments can only be defined for real-valued functions of random variables (or complex-valued, etc.). If the random variable is itself real-valued, then moments of the variable itself can be taken, which are equivalent to moments of the identity function $f(X)=X$ of the random variable. However, even for non-real-valued random variables, moments can be taken of real-valued functions of those variables. For example, for a categorical random variable *X* that can take on the nominal values "red", "blue" or "green", the real-valued function $[X={\text{green}}]$ can be constructed; this uses the Iverson bracket, and has the value 1 if X has the value "green", 0 otherwise. Then, the expected value and other moments of this function can be determined.

## Functions of random variables

A new random variable ⁠ Y ⁠ can be defined by applying a real Borel measurable function $g\colon \mathbb {R} \rightarrow \mathbb {R}$ to the outcomes of a real-valued random variable X . That is, $Y=g(X)$ . The cumulative distribution function of Y is then

$F_{Y}(y)=\operatorname {P} (g(X)\leq y).$

If function g is invertible (i.e., $h=g^{-1}$ exists, where h is g 's inverse function) and is either increasing or decreasing, then the previous relation can be extended to obtain

$F_{Y}(y)=\operatorname {P} (g(X)\leq y)={\begin{cases}\operatorname {P} (X\leq h(y))=F_{X}(h(y)),&{\text{if }}h=g^{-1}{\text{ increasing}},\\\\\operatorname {P} (X\geq h(y))=1-F_{X}(h(y)),&{\text{if }}h=g^{-1}{\text{ decreasing}}.\end{cases}}$

With the same hypotheses of invertibility of g , assuming also differentiability, the relation between the probability density functions can be found by differentiating both sides of the above expression with respect to y , in order to obtain

$f_{Y}(y)=f_{X}{\bigl (}h(y){\bigr )}\left|{\frac {dh(y)}{dy}}\right|.$

If there is no invertibility of g but each y admits at most a countable number of roots (i.e., a finite, or countably infinite, number of $x_{i}$ such that $y=g(x_{i})$ ) then the previous relation between the probability density functions can be generalized with

$f_{Y}(y)=\sum _{i}f_{X}(g_{i}^{-1}(y))\left|{\frac {dg_{i}^{-1}(y)}{dy}}\right|$

where ⁠ $x_{i}=g_{i}^{-1}(y)$ ⁠, according to the inverse function theorem. The formulas for densities do not demand g to be increasing.

In the measure-theoretic, axiomatic approach to probability, if a random variable X on $\Omega$ and a Borel measurable function $g\colon \mathbb {R} \rightarrow \mathbb {R}$ , then $Y=g(X)$ is also a random variable on ⁠ $\Omega$ ⁠, since the composition of measurable functions is also measurable. (However, this is not necessarily true if g is Lebesgue measurable.) The same procedure that allowed one to go from a probability space $(\Omega ,P)$ to $(\mathbb {R} ,dF_{X})$ can be used to obtain the distribution of ⁠ Y ⁠.

### Example 1

Let X be a real-valued, continuous random variable and let ⁠ $Y=X^{2}$ ⁠.

$F_{Y}(y)=\operatorname {P} (X^{2}\leq y).$

If ⁠ $y<0$ ⁠, then ⁠ $P(X^{2}\leq y)=0$ ⁠, so

$F_{Y}(y)=0\qquad {\hbox{if}}\quad y<0.$

If ⁠ $y\geq 0$ ⁠, then

$\operatorname {P} (X^{2}\leq y)=\operatorname {P} (|X|\leq {\sqrt {y}})=\operatorname {P} (-{\sqrt {y}}\leq X\leq {\sqrt {y}}),$

so

$F_{Y}(y)=F_{X}({\sqrt {y}})-F_{X}(-{\sqrt {y}})\qquad {\hbox{if}}\quad y\geq 0.$

### Example 2

Suppose X is a random variable with a cumulative distribution

$F_{X}(x)=P(X\leq x)={\frac {1}{(1+e^{-x})^{\theta }}}$

where $\theta >0$ is a fixed parameter. Consider the random variable $Y=\mathrm {log} (1+e^{-X}).$ Then,

$F_{Y}(y)=P(Y\leq y)=P(\mathrm {log} (1+e^{-X})\leq y)=P(X\geq -\mathrm {log} (e^{y}-1)).\,$

The last expression can be calculated in terms of the cumulative distribution of ⁠ X ⁠, so

${\begin{aligned}F_{Y}(y)&=1-F_{X}(-\log(e^{y}-1))\\[5pt]&=1-{\frac {1}{(1+e^{\log(e^{y}-1)})^{\theta }}}\\[5pt]&=1-{\frac {1}{(1+e^{y}-1)^{\theta }}}\\[5pt]&=1-e^{-y\theta },\end{aligned}}$

which is the cumulative distribution function (CDF) of an exponential distribution.

### Example 3

Suppose X is a random variable with a standard normal distribution, whose density is

$f_{X}(x)={\frac {1}{\sqrt {2\pi }}}e^{-x^{2}/2}.$

Consider the random variable ⁠ $Y=X^{2}$ ⁠. We can find the density using the above formula for a change of variables:

$f_{Y}(y)=\sum _{i}f_{X}(g_{i}^{-1}(y))\left|{\frac {dg_{i}^{-1}(y)}{dy}}\right|.$

In this case the change is not monotonic, because every value of Y has two corresponding values of X (one positive and negative). However, because of symmetry, both halves will transform identically, i.e.,

$f_{Y}(y)=2f_{X}(g^{-1}(y))\left|{\frac {dg^{-1}(y)}{dy}}\right|.$

The inverse transformation is

$x=g^{-1}(y)={\sqrt {y}}$

and its derivative is

${\frac {dg^{-1}(y)}{dy}}={\frac {1}{2{\sqrt {y}}}}.$

Then,

$f_{Y}(y)=2{\frac {1}{\sqrt {2\pi }}}e^{-y/2}{\frac {1}{2{\sqrt {y}}}}={\frac {1}{\sqrt {2\pi y}}}e^{-y/2}.$

This is a chi-squared distribution with one degree of freedom.

### Example 4

Suppose X is a random variable with a normal distribution, whose density is

$f_{X}(x)={\frac {1}{\sqrt {2\pi \sigma ^{2}}}}e^{-(x-\mu )^{2}/(2\sigma ^{2})}.$

Consider the random variable $Y=X^{2}.$ We can find the density using the above formula for a change of variables:

$f_{Y}(y)=\sum _{i}f_{X}(g_{i}^{-1}(y))\left|{\frac {dg_{i}^{-1}(y)}{dy}}\right|.$

In this case the change is not monotonic, because every value of Y has two corresponding values of X (one positive and negative). Differently from the previous example, in this case however, there is no symmetry and we have to compute the two distinct terms:

$f_{Y}(y)=f_{X}(g_{1}^{-1}(y))\left|{\frac {dg_{1}^{-1}(y)}{dy}}\right|+f_{X}(g_{2}^{-1}(y))\left|{\frac {dg_{2}^{-1}(y)}{dy}}\right|.$

The inverse transformation is

$x=g_{1,2}^{-1}(y)=\pm {\sqrt {y}}$

and its derivative is

${\frac {dg_{1,2}^{-1}(y)}{dy}}=\pm {\frac {1}{2{\sqrt {y}}}}.$

Then,

$f_{Y}(y)={\frac {1}{\sqrt {2\pi \sigma ^{2}}}}{\frac {1}{2{\sqrt {y}}}}(e^{-({\sqrt {y}}-\mu )^{2}/(2\sigma ^{2})}+e^{-(-{\sqrt {y}}-\mu )^{2}/(2\sigma ^{2})}).$

This is a noncentral chi-squared distribution with one degree of freedom.

## Some properties

- The probability distribution of the sum of two independent random variables is the **convolution** of each of their distributions.
- Probability distributions are not a vector space – they are not closed under linear combinations, as these do not preserve non-negativity or total integral 1—but they are closed under convex combination, thus forming a convex subset of the space of functions (or measures).

## Equivalence of random variables

There are several different senses in which random variables can be considered to be equivalent. Two random variables can be equal, equal almost surely, or equal in distribution.

In increasing order of strength, the precise definition of these notions of equivalence is given below.

### Equality in distribution

If the sample space is a subset of the real line, random variables *X* and *Y* are *equal in distribution* (denoted ⁠ $X~{\stackrel {d}{=}}~Y$ ⁠) if they have the same distribution functions:

$\operatorname {P} (X\leq x)=\operatorname {P} (Y\leq x)\quad {\text{for all }}x.$

To be equal in distribution, random variables need not be defined on the same probability space. Two random variables having equal moment generating functions have the same distribution. This provides, for example, a useful method of checking equality of certain functions of independent, identically distributed (IID) random variables. However, the moment generating function exists only for distributions that have a defined Laplace transform.

### Almost sure equality

Two random variables *X* and *Y* are *equal almost surely* (denoted $X\;{\stackrel {\text{a.s.}}{=}}\;Y$ ) if, and only if, the probability that they are different is zero:

$\operatorname {P} (X\neq Y)=0.$

For all practical purposes in probability theory, this notion of equivalence is as strong as actual equality. It is associated to the following distance:

$d_{\infty }(X,Y)=\operatorname {ess} \sup _{\omega }|X(\omega )-Y(\omega )|,$

where "ess sup" represents the essential supremum in the sense of measure theory.

### Equality

Finally, the two random variables *X* and *Y* are *equal* if they are equal as functions on their measurable space:

$X(\omega )=Y(\omega )\qquad {\hbox{for all }}\omega .$

This notion is typically the least useful in probability theory because in practice and in theory, the underlying measure space of the experiment is rarely explicitly characterized or even characterizable.

### Practical difference between notions of equivalence

Since we rarely explicitly construct the probability space underlying a random variable, the difference between these notions of equivalence is somewhat subtle. Essentially, two random variables considered *in isolation* are "practically equivalent" if they are equal in distribution -- but once we relate them to *other* random variables defined on the same probability space, then they only remain "practically equivalent" if they are equal almost surely.

For example, consider the real random variables *A*, *B*, *C*, and *D* all defined on the same probability space. Suppose that *A* and *B* are equal almost surely ( $A\;{\stackrel {\text{a.s.}}{=}}\;B$ ), but *A* and *C* are only equal in distribution ( $A~{\stackrel {d}{=}}~C$ ). Then $A+D\;{\stackrel {\text{a.s.}}{=}}\;B+D$ , but in general $A+D\neq C+D$ (not even in distribution). Similarly, we have that the expectation values $\mathbb {E} (AD)=\mathbb {E} (BD)$ , but in general $\mathbb {E} (AD)\neq \mathbb {E} (CD)$ . Therefore, two random variables that are equal in distribution (but not equal almost surely) can have different covariances with a third random variable.

## Convergence

A significant theme in mathematical statistics consists of obtaining convergence results for certain sequences of random variables; for instance the law of large numbers and the central limit theorem.

There are various senses in which a sequence $X_{n}$ of random variables can converge to a random variable ⁠ X ⁠. These are explained in the article on convergence of random variables.
