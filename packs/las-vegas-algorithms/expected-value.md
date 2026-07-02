---
title: "Expected value"
source: https://en.wikipedia.org/wiki/Expected_value
domain: las-vegas-algorithms
license: CC-BY-SA-4.0
tags: las vegas algorithm, expected running time, randomized quicksort, monte carlo algorithm
fetched: 2026-07-02
---

# Expected value

In probability theory, the **expected value** (also called **expectation**, **mean**, or **first moment**) is a generalization of the weighted average.

The expected value of a random variable with a finite number of outcomes is a weighted average of all possible outcomes. In the case of a continuum of possible outcomes, the expectation is defined by integration. In the axiomatic foundation for probability provided by measure theory, the expectation is given by Lebesgue integration.

The expected value of a random variable X is often denoted by ${\text{E}}(X)$ , ${\text{E}}[X]$ , or ${\text{E}}X$ , with E also often stylized as $\mathbb {E}$ , ${\mathcal {E}}$ or *E*.

## History

The concept of expected value emerged in the mid-17th century from the "problem of points", a puzzle centered on how to *fairly* divide stakes between two players forced to end a game prematurely. While the problem had been debated for centuries, it gained new momentum in 1654 when the Chevalier de Méré, a French writer and amateur mathematician, presented it to Blaise Pascal. Méré claimed that this problem could not be solved and that it showed just how flawed mathematics was when it came to its application to the real world. Pascal, being a mathematician, decided to work on a solution to the problem.

He began to discuss the problem in the famous series of letters to Pierre de Fermat. Soon enough, they both independently came up with a solution. They solved the problem in different computational ways, but their results were identical because their computations were based on the same fundamental principle. The principle is that the value of a future gain should be directly proportional to the chance of getting it. This principle seemed to have come naturally to both of them. They were very pleased by the fact that they had found essentially the same solution, and this in turn made them absolutely convinced that they had solved the problem conclusively; however, they did not publish their findings. They only informed a small circle of mutual scientific friends in Paris about it.

In Dutch mathematician Christiaan Huygens' book, he considered the problem of points, and presented a solution based on the same principle as the solutions of Pascal and Fermat. Huygens published his treatise in 1657, (see Huygens (1657)) "*De ratiociniis in ludo aleæ*" on probability theory just after visiting Paris. The book extended the concept of expectation by adding rules for how to calculate expectations in more complicated situations than the original problem (e.g., for three or more players), and can be seen as the first successful attempt at laying down the foundations of the theory of probability.

In the foreword to his treatise, Huygens wrote:

> It should be said, also, that for some time some of the best mathematicians of France have occupied themselves with this kind of calculus so that no one should attribute to me the honour of the first invention. This does not belong to me. But these savants, although they put each other to the test by proposing to each other many questions difficult to solve, have hidden their methods. I have had therefore to examine and go deeply for myself into this matter by beginning with the elements, and it is impossible for me for this reason to affirm that I have even started from the same principle. But finally I have found that my answers in many cases do not differ from theirs.

— Edwards (2002)

In the mid-nineteenth century, Pafnuty Chebyshev became the first person to think systematically in terms of the expectations of random variables.

### Etymology

Neither Pascal nor Huygens used the term "expectation" in its modern sense. In particular, Huygens writes:

> That any one Chance or Expectation to win any thing is worth just such a Sum, as wou'd procure in the same Chance and Expectation at a fair Lay. ... If I expect a or b, and have an equal chance of gaining them, my Expectation is worth (a+b)/2.

More than a hundred years later, in 1814, Pierre-Simon Laplace published his tract "*Théorie analytique des probabilités*", where the concept of expected value was defined explicitly:

> ... this advantage in the theory of chance is the product of the sum hoped for by the probability of obtaining it; it is the partial sum which ought to result when we do not wish to run the risks of the event in supposing that the division is made proportional to the probabilities. This division is the only equitable one when all strange circumstances are eliminated; because an equal degree of probability gives an equal right for the sum hoped for. We will call this advantage *mathematical hope.*

## Notations

The use of the letter E to denote "expected value" goes back to W. A. Whitworth in 1901. The symbol has since become popular for English writers. In German, E stands for *Erwartungswert*, in Spanish for *esperanza matemática*, and in French for *espérance mathématique.*

When "E" is used to denote "expected value", authors use a variety of stylizations: the expectation operator can be stylized as E (upright), E (italic), or $\mathbb {E}$ (in blackboard bold), while a variety of bracket notations (such as E(*X*), E[*X*], and E*X*) are all used.

Another popular notation is μ*X*. ⟨*X*⟩, ⟨*X*⟩av, and ${\overline {X}}$ are commonly used in physics. M(*X*) is used in Russian-language literature.

## Definition

As discussed above, there are several context-dependent ways of defining the expected value. The simplest and original definition deals with the case of finitely many possible outcomes, such as in the flip of a coin. With the theory of infinite series, this can be extended to the case of countably many possible outcomes. It is also very common to consider the distinct case of random variables dictated by (piecewise-)continuous probability density functions, as these arise in many natural contexts. All of these specific definitions may be viewed as special cases of the general definition based upon the mathematical tools of measure theory and Lebesgue integration, which provide these different contexts with an axiomatic foundation and common language.

Any definition of expected value may be extended to define an expected value of a multidimensional random variable, i.e. a random vector X . It is defined component by component, as $E[X]_{i}=E[X_{i}]$ . Similarly, one may define the expected value of a random matrix X with components $X_{ij}$ by $E[X]_{ij}=E[X_{ij}]$ .

### Random variables with finitely many outcomes

Consider a random variable X with a *finite* list $x_{1},...,x_{k}$ of possible outcomes, each of which (respectively) has probability $p_{1},...,p_{k}$ of occurring. The expectation of X is defined as $\operatorname {E} [X]=x_{1}p_{1}+x_{2}p_{2}+\cdots +x_{k}p_{k}.$

Since the probabilities must satisfy $p_{1}+...+p_{k}=1$ , it is natural to interpret $E[X]$ as a weighted average of the $x_{i}$ values, with weights given by their probabilities $p_{i}$ .

In the special case that all possible outcomes are equiprobable (that is $p_{1}=...=p_{k}$ ), the weighted average is given by the standard average. In the general case, the expected value takes into account the fact that some outcomes are more likely than others.

#### Examples

- Let X represent the outcome of a roll of a fair six-sided die. More specifically, X will be the number of pips showing on the top face of the die after the toss. The possible values for X are 1, 2, 3, 4, 5, and 6, all of which are equally likely with a probability of ⁠1/6⁠. The expectation of X is $\operatorname {E} [X]=1\cdot {\frac {1}{6}}+2\cdot {\frac {1}{6}}+3\cdot {\frac {1}{6}}+4\cdot {\frac {1}{6}}+5\cdot {\frac {1}{6}}+6\cdot {\frac {1}{6}}=3.5.$ If one rolls the die n times and computes the average (arithmetic mean) of the results, then as n grows, the average will almost surely converge to the expected value, a fact known as the strong law of large numbers.
- The roulette game consists of a small ball and a wheel with 38 numbered pockets around the edge. As the wheel is spun, the ball bounces around randomly until it settles down in one of the pockets. Suppose random variable X represents the (monetary) outcome of a $1 bet on a single number ("straight up" bet). If the bet wins (which happens with probability ⁠1/38⁠ in American roulette), the payoff is $35; otherwise the player loses the bet. The expected profit from such a bet will be $\operatorname {E} [\,{\text{gain from }}\$1{\text{ bet}}\,]=-\$1\cdot {\frac {37}{38}}+\$35\cdot {\frac {1}{38}}=-\${\frac {1}{19}}.$ That is, the expected value to be won from a $1 bet is −$⁠1/19⁠. Thus, in 190 bets, the net loss will probably be about $10.

### Random variables with countably infinitely many outcomes

Informally, the expectation of a random variable with a countably infinite set of possible outcomes is defined analogously as the weighted average of all possible outcomes, where the weights are given by the probabilities of realizing each given value. This is to say that $\operatorname {E} [X]=\sum _{i=1}^{\infty }x_{i}\,p_{i},$ where $x_{1},x_{2},...$ are the possible outcomes of the random variable X and $p_{1},p_{2},...$ are their corresponding probabilities. In many non-mathematical textbooks, this is presented as the full definition of expected values in this context.

However, there are some subtleties with infinite summation, so the above formula is not suitable as a mathematical definition. In particular, the Riemann series theorem of mathematical analysis illustrates that the value of certain infinite sums involving positive and negative summands depends on the order in which the summands are given. Since the outcomes of a random variable have no naturally given order, this creates a difficulty in defining expected value precisely.

For this reason, many mathematical textbooks only consider the case that the infinite sum given above converges absolutely, which implies that the infinite sum is a finite number independent of the ordering of summands. In the alternative case that the infinite sum does not converge absolutely, one says the random variable *does not have finite expectation.*

#### Example

Suppose $x_{i}=i$ and $p_{i}={\tfrac {c}{i\,\cdot \,2^{i}}}$ for $i=1,2,3,\ldots ,$ where $c={\tfrac {1}{\ln 2}}$ is the scaling factor which makes the probabilities sum to 1: $\sum _{i=1}^{\infty }p_{i}=\sum _{i=1}^{\infty }{\frac {c}{i\cdot 2^{i}}}=c\,\sum _{i=1}^{\infty }{\frac {1}{i}}\!\ \left({\frac {1}{2}}\right)^{i}=c\!\ \ln 2=1$ by the logarithm series for $\ln \left(1-{\tfrac {1}{2}}\right)=-\ln 2.$ Then we have $\mathrm {E} [X]=\sum _{i=1}^{\infty }x_{i}p_{i}=\sum _{i=1}^{\infty }i\cdot {\frac {c}{i\cdot 2^{i}}}=c\,\sum _{i=1}^{\infty }\left({\frac {1}{2}}\right)^{i}=c\cdot 1={\frac {1}{\ln 2}}$ due to the geometric series for $1{\big /}{\big (}1-{\tfrac {1}{2}}{\big )}.$

### Random variables with density

Now consider a random variable X which has a probability density function given by a function f on the real number line. This means that the probability of X taking on any value in a given open interval is given by the integral of f over that interval. The expectation of X is then given by the integral $\operatorname {E} [X]=\int _{-\infty }^{\infty }xf(x)\,dx.$ A general and mathematically precise formulation of this definition uses measure theory and Lebesgue integration, and the corresponding theory of *absolutely continuous random variables* is described in the next section. The density functions of many common distributions are piecewise continuous, and as such the theory is often developed in this restricted setting. For such functions, it is sufficient to only consider the standard Riemann integration. Sometimes *continuous random variables* are defined as those corresponding to this special class of densities, although the term is used differently by various authors.

Analogously to the countably-infinite case above, there are subtleties with this expression due to the infinite region of integration. Such subtleties can be seen concretely if the distribution of X is given by the Cauchy distribution Cauchy(0, π), so that $f(x)=(x^{2}+\pi ^{2})^{-1}$ . It is straightforward to compute in this case that $\int _{a}^{b}xf(x)\,dx=\int _{a}^{b}{\frac {x}{x^{2}+\pi ^{2}}}\,dx={\frac {1}{2}}\ln {\frac {b^{2}+\pi ^{2}}{a^{2}+\pi ^{2}}}.$ The limit of this expression as $a\to -\infty$ and $b\to +\infty$ does not exist: if the limits are taken so that $a=-b$ , then the limit is zero, while if the constraint $2a=-b$ is taken, then the limit is $\ln(2)$ .

To avoid such ambiguities, in mathematical textbooks it is common to require that the given integral converges absolutely, with $E[X]$ left undefined otherwise. However, measure-theoretic notions as given below can be used to give a systematic definition of $E[X]$ for more general random variables X .

### Arbitrary real-valued random variables

All definitions of the expected value may be expressed in the language of measure theory. In general, if X is a real-valued random variable defined on a probability space $(\Omega ,\Sigma ,P)$ , then the expected value of X , denoted by $E[X]$ , is defined as the Lebesgue integral $\operatorname {E} [X]=\int _{\Omega }X\,d\operatorname {P} .$ Despite the newly abstract situation, this definition is extremely similar in nature to the very simplest definition of expected values, given above, as certain weighted averages. This is because, in measure theory, the value of the Lebesgue integral of X is defined via weighted averages of *approximations* of X which take on finitely many values. Moreover, if given a random variable with finitely or countably many possible values, the Lebesgue theory of expectation is identical to the summation formulas given above. However, the Lebesgue theory clarifies the scope of the theory of probability density functions. A random variable X is said to be *absolutely continuous* if any of the following conditions are satisfied:

- there is a nonnegative measurable function f on the real line such that $\operatorname {P} (X\in A)=\int _{A}f(x)\,dx,$ for any Borel set A , in which the integral is Lebesgue.
- the cumulative distribution function of A is absolutely continuous.
- for any Borel set A of real numbers with Lebesgue measure equal to zero, the probability of X being valued in A is also equal to zero
- for any positive number $\varepsilon$ there is a positive number $\delta$ such that: if A is a Borel set with Lebesgue measure less than $\delta$ , then the probability of X being valued in A is less than $\varepsilon$ .

These conditions are all equivalent, although this is nontrivial to establish. In this definition, f is called the *probability density function* of X (relative to Lebesgue measure). According to the change-of-variables formula for Lebesgue integration, combined with the law of the unconscious statistician, it follows that $\operatorname {E} [X]\equiv \int _{\Omega }X\,d\operatorname {P} =\int _{\mathbb {R} }xf(x)\,dx$ for any absolutely continuous random variable X . The above discussion of continuous random variables is thus a special case of the general Lebesgue theory, due to the fact that every piecewise-continuous function is measurable.

The expected value of any real-valued random variable X can also be defined on the graph of its cumulative distribution function F by a nearby equality of areas. In fact, $\operatorname {E} [X]=\mu$ with a real number $\mu$ if and only if the two surfaces in the x - y -plane, described by $x\leq \mu ,\;\,0\leq y\leq F(x)\quad {\text{or}}\quad x\geq \mu ,\;\,F(x)\leq y\leq 1$ respectively, have the same finite area, i.e. if $\int _{-\infty }^{\mu }F(x)\,dx=\int _{\mu }^{\infty }{\big (}1-F(x){\big )}\,dx$ and both improper Riemann integrals converge. Finally, this is equivalent to the representation $\operatorname {E} [X]=\int _{0}^{\infty }{\bigl (}1-F(x){\bigr )}\,dx-\int _{-\infty }^{0}F(x)\,dx,$ also with convergent integrals.

#### Example

Let the daily precipitation (unit: $\textstyle \mathrm {L} /\mathrm {m} ^{2}=\mathrm {mm}$ ) at a location be simply modeled as a real-valued random variable X for which the following holds: $\mathrm {P} (X\!<\!0)=0,\qquad \mathrm {P} (X\!>\!x)=\alpha \!\ \mathrm {e} ^{-\lambda x}\;{\text{ if }}x\geq 0$ with two positive constants $\alpha <1$ and $\lambda .$ The cumulative distribution function $F\colon \,\mathbb {R} \to \mathbb {R}$ of X is thus obtained as $F(x)={\begin{cases}0&{\text{for }}x<0,\\1-\alpha \!\ \mathrm {e} ^{-\lambda x}&{\text{for }}x\geq 0.\end{cases}}$ Its only point of discontinuity is $x=0$ with jump height $1-\alpha <1.$ Therefore, the random variable X is neither discrete nor does it have a density. The latter representation of $\mathrm {E} [X]$ as difference of two improper Riemann integrals leads to $\mathrm {E} [X]=\int _{0}^{\infty }\alpha \!\ \mathrm {e} ^{-\lambda x}\,dx=\lim _{b\to \infty }\left[-{\frac {\alpha }{\lambda }}\,\mathrm {e} ^{-\lambda x}\right]_{0}^{b}={\frac {\alpha }{\lambda }}\,.$ For instance, the rough values $\alpha ={\tfrac {1}{2}}$ and $\lambda ={\tfrac {1}{4\!\ \mathrm {mm} }}$ result in the expected value $\mathrm {E} [X]=2\,\mathrm {mm} .$

### Infinite expected values

Expected values as defined above are automatically finite numbers. However, in many cases it is fundamental to be able to consider expected values of $\pm \infty$ . This is intuitive, for example, in the case of the St. Petersburg paradox, in which one considers a random variable with possible outcomes $x_{i}=2^{i}$ , with associated probabilities $p_{i}=2^{-i}$ , for i ranging over all positive integers. According to the summation formula in the case of random variables with countably many outcomes, one has $\operatorname {E} [X]=\sum _{i=1}^{\infty }x_{i}\,p_{i}=2\cdot {\frac {1}{2}}+4\cdot {\frac {1}{4}}+8\cdot {\frac {1}{8}}+16\cdot {\frac {1}{16}}+\cdots =1+1+1+1+\cdots .$ It is natural to say that the expected value equals $+\infty$ .

There is a rigorous mathematical theory underlying such ideas, which is often taken as part of the definition of the Lebesgue integral. The first fundamental observation is that, whichever of the above definitions are followed, any *nonnegative* random variable whatsoever can be given an unambiguous expected value; whenever absolute convergence fails, then the expected value can be defined as $+\infty$ . The second fundamental observation is that any random variable can be written as the difference of two nonnegative random variables. Given a random variable X , one defines the positive and negative parts by $X^{+}=\max(X,0)$ and $X^{-}=\max(-X,0)$ . These are nonnegative random variables, and it can be directly checked that $X=X^{+}-X^{-}$ . Since $E[X^{+}]$ and $E[X^{-}]$ are both then defined as either nonnegative numbers or +∞, it is then natural to define: $\operatorname {E} [X]={\begin{cases}\operatorname {E} [X^{+}]-\operatorname {E} [X^{-}]&{\text{if }}\operatorname {E} [X^{+}]<\infty {\text{ and }}\operatorname {E} [X^{-}]<\infty ;\\+\infty &{\text{if }}\operatorname {E} [X^{+}]=\infty {\text{ and }}\operatorname {E} [X^{-}]<\infty ;\\-\infty &{\text{if }}\operatorname {E} [X^{+}]<\infty {\text{ and }}\operatorname {E} [X^{-}]=\infty ;\\{\text{undefined}}&{\text{if }}\operatorname {E} [X^{+}]=\infty {\text{ and }}\operatorname {E} [X^{-}]=\infty .\end{cases}}$

According to this definition, $E[X]$ exists and is finite if and only if $E[X^{+}]$ and $E[X^{-}]$ are both finite. Due to the formula $\left|X\right|=X^{+}+X^{-}$ , this is the case if and only if $E[\left|X\right|]$ is finite, and this is equivalent to the absolute convergence conditions in the definitions above. As such, the present considerations do not define finite expected values in any cases not previously considered; they are only useful for infinite expectations.

- In the case of the St. Petersburg paradox, one has $X^{-}=0$ and so $E[X]=+\infty$ as desired.
- Suppose the random variable X takes values $1,-2,3,-4,...$ with respective probabilities $6\pi ^{-2},6(2\pi )^{-2},6(3\pi )^{-2},6(4\pi )^{-2},...$ . Then it follows that $X^{+}$ takes value $2k-1$ with probability $6((2k-1)\pi )^{-2}$ for each positive integer k , and takes value 0 with remaining probability. Similarly, $X^{-}$ takes value $2k$ with probability $6(2k\pi )^{-2}$ for each positive integer k and takes value 0 with remaining probability. Using the definition for non-negative random variables, one can show that both $E[X^{+}]=\infty$ and $E[X^{-}]=\infty$ (see Harmonic series). Hence, in this case the expectation of X is undefined.
- Similarly, the Cauchy distribution, as discussed above, has undefined expectation.

### Tail-sum formula

In the case of a non-negative integer-valued random variable X , the expected value can also be expressed in terms of its *tail probabilities* (sometimes called the **tail-sum formula**):

$\operatorname {E} [X]=\sum _{k=0}^{\infty }\Pr(X>k).$

A more general version holds for any non-negative random variable (discrete or continuous):

$\operatorname {E} [X]=\int _{0}^{\infty }\Pr(X>t)\,dt,$

where the integrand is the survival function of X .

## Expected values of common distributions

The following table gives the expected values of some commonly occurring probability distributions. The third column gives the expected values both in the form immediately given by the definition, as well as in the simplified form obtained by computation therefrom. The details of these computations, which are not always straightforward, can be found in the indicated references.

| Distribution | Notation | Mean E(X) |
|---|---|---|
| Bernoulli | $X\sim ~b(1,p)$ | $0\cdot (1-p)+1\cdot p=p$ |
| Binomial | $X\sim B(n,p)$ | $\sum _{i=0}^{n}i{n \choose i}p^{i}(1-p)^{n-i}=np$ |
| Poisson | $X\sim \mathrm {Po} (\lambda )$ | $\sum _{i=0}^{\infty }{\frac {ie^{-\lambda }\lambda ^{i}}{i!}}=\lambda$ |
| Geometric | $X\sim \mathrm {Geometric} (p)$ | $\sum _{i=1}^{\infty }ip(1-p)^{i-1}={\frac {1}{p}}$ |
| Uniform | $X\sim U(a,b)$ | $\int _{a}^{b}{\frac {x}{b-a}}\,dx={\frac {a+b}{2}}$ |
| Exponential | $X\sim \exp(\lambda )$ | $\int _{0}^{\infty }\lambda xe^{-\lambda x}\,dx={\frac {1}{\lambda }}$ |
| Normal | $X\sim N(\mu ,\sigma ^{2})$ | ${\frac {1}{\sqrt {2\pi \sigma ^{2}}}}\int _{-\infty }^{\infty }x\,e^{-{\frac {1}{2}}\left({\frac {x-\mu }{\sigma }}\right)^{2}}\,dx=\mu$ |
| Standard Normal | $X\sim N(0,1)$ | ${\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{\infty }xe^{-x^{2}/2}\,dx=0$ |
| Pareto | $X\sim \mathrm {Par} (\alpha ,k)$ | $\int _{k}^{\infty }\alpha k^{\alpha }x^{-\alpha }\,dx={\begin{cases}{\frac {\alpha k}{\alpha -1}}&{\text{if }}\alpha >1\\\infty &{\text{if }}0<\alpha \leq 1\end{cases}}$ |
| Cauchy | $X\sim \mathrm {Cauchy} (x_{0},\gamma )$ | ${\frac {1}{\pi }}\int _{-\infty }^{\infty }{\frac {\gamma x}{(x-x_{0})^{2}+\gamma ^{2}}}\,dx$ is undefined |

## Properties

The basic properties below (and their names in bold) replicate or follow immediately from those of Lebesgue integral. Note that the letters "a.s." stand for "almost surely"—a central property of the Lebesgue integral. Basically, one says that an inequality like $X\geq 0$ is true almost surely, when the probability measure attributes zero-mass to the complementary event $\left\{X<0\right\}.$

- Non-negativity: If $X\geq 0$ (a.s.), then $\operatorname {E} [X]\geq 0.$
- Linearity of expectation: The expected value operator (or *expectation operator*) $\operatorname {E} [\cdot ]$ is linear in the sense that, for any random variables X and $Y,$ and a constant $a,$ ${\begin{aligned}\operatorname {E} [X+Y]&=\operatorname {E} [X]+\operatorname {E} [Y],\\\operatorname {E} [aX]&=a\operatorname {E} [X],\end{aligned}}$ whenever the right-hand side is well-defined. By induction, this means that the expected value of the sum of any finite number of random variables is the sum of the expected values of the individual random variables, and the expected value scales linearly with a multiplicative constant. Symbolically, for N random variables $X_{i}$ and constants $a_{i}(1\leq i\leq N),$ we have ${\textstyle \operatorname {E} \left[\sum _{i=1}^{N}a_{i}X_{i}\right]=\sum _{i=1}^{N}a_{i}\operatorname {E} [X_{i}].}$ If we think of the set of random variables with finite expected value as forming a vector space, then the linearity of expectation implies that the expected value is a linear form on this vector space.
- Monotonicity: If $X\leq Y$ almost surely, and both $\operatorname {E} [X]$ and $\operatorname {E} [Y]$ exist, then $\operatorname {E} [X]\leq \operatorname {E} [Y].$ Proof follows from the linearity and the non-negativity property for $Z=Y-X,$ since $Z\geq 0$ (a.s.).
- Non-degeneracy: If $\operatorname {E} [|X|]=0,$ then $X=0$ (a.s.).
- If $X=Y$ (a.s.), then $\operatorname {E} [X]=\operatorname {E} [Y].$ In other words, if X and Y are random variables that take different values with probability zero, then the expectation of X will equal the expectation of Y.
- If $X=c$ (a.s.) for some real number c, then $\operatorname {E} [X]=c.$ In particular, for a random variable X with well-defined expectation, $\operatorname {E} [\operatorname {E} [X]]=\operatorname {E} [X].$ A well defined expectation implies that there is one number, or rather, one constant that defines the expected value. Thus follows that the expectation of this constant is just the original expected value.
- As a consequence of the formula |*X*| = *X*+ + *X*− as discussed above, together with the triangle inequality, it follows that for any random variable X with well-defined expectation, one has $|\operatorname {E} [X]|\leq \operatorname {E} |X|.$
- Let **1***A* denote the indicator function of an event A, then E[**1***A*] is given by the probability of A. This is nothing but a different way of stating the expectation of a Bernoulli random variable, as calculated in the table above.
- Formulas in terms of CDF: If $F(x)$ is the cumulative distribution function of a random variable X, then $\operatorname {E} [X]=\int _{-\infty }^{\infty }x\,dF(x),$ where the values on both sides are well defined or not well defined simultaneously, and the integral is taken in the sense of Lebesgue-Stieltjes. As a consequence of integration by parts as applied to this representation of E[*X*], it can be proved that $\operatorname {E} [X]=\int _{0}^{\infty }(1-F(x))\,dx-\int _{-\infty }^{0}F(x)\,dx,$ with the integrals taken in the sense of Lebesgue. As a special case, for any random variable X valued in the nonnegative integers {0, 1, 2, 3, ...}, one has $\operatorname {E} [X]=\sum _{n=0}^{\infty }\Pr(X>n),$ where P denotes the underlying probability measure.
- Non-multiplicativity: In general, the expected value is not multiplicative, i.e. $\operatorname {E} [XY]$ is not necessarily equal to $\operatorname {E} [X]\cdot \operatorname {E} [Y].$ If X and Y are independent, then one can show that $\operatorname {E} [XY]=\operatorname {E} [X]\operatorname {E} [Y].$ If the random variables are dependent, then generally $\operatorname {E} [XY]\neq \operatorname {E} [X]\operatorname {E} [Y],$ although in special cases of dependency the equality may hold.
- Law of the unconscious statistician: The expected value of a measurable function of $X,$ $g(X),$ given that X has a probability density function $f(x),$ is given by the inner product of f and g : $\operatorname {E} [g(X)]=\int _{\mathbb {R} }g(x)f(x)\,dx.$ This formula also holds in multidimensional case, when g is a function of several random variables, and f is their joint density.

### Inequalities

Concentration inequalities control the likelihood of a random variable taking on large values. Markov's inequality is among the best-known and simplest to prove: for a *nonnegative* random variable X and any positive number a, it states that $\operatorname {P} (X\geq a)\leq {\frac {\operatorname {E} [X]}{a}}.$

If X is any random variable with finite expectation, then Markov's inequality may be applied to the random variable |*X*−E[*X*]|2 to obtain Chebyshev's inequality $\operatorname {P} (|X-{\text{E}}[X]|\geq a)\leq {\frac {\operatorname {Var} [X]}{a^{2}}},$ where Var is the variance. These inequalities are significant for their nearly complete lack of conditional assumptions. For example, for any random variable with finite expectation, the Chebyshev inequality implies that there is at least a 75% probability of an outcome being within two standard deviations of the expected value. However, in special cases the Markov and Chebyshev inequalities often give much weaker information than is otherwise available. For example, in the case of an unweighted dice, Chebyshev's inequality says that odds of rolling between 1 and 6 is at least 53%; in reality, the odds are of course 100%. The Kolmogorov inequality extends the Chebyshev inequality to the context of sums of random variables.

The following three inequalities are of fundamental importance in the field of mathematical analysis and its applications to probability theory.

- Jensen's inequality: Let *f*: **R** → **R** be a convex function and X a random variable with finite expectation. Then $f(\operatorname {E} (X))\leq \operatorname {E} (f(X)).$ Part of the assertion is that the negative part of *f*(*X*) has finite expectation, so that the right-hand side is well-defined (possibly infinite). Convexity of f can be phrased as saying that the output of the weighted average of *two* inputs under-estimates the same weighted average of the two outputs; Jensen's inequality extends this to the setting of completely general weighted averages, as represented by the expectation. In the special case that *f*(*x*) = |*x*|*t*/*s* for positive numbers *s* < *t*, one obtains the Lyapunov inequality $\left(\operatorname {E} |X|^{s}\right)^{1/s}\leq \left(\operatorname {E} |X|^{t}\right)^{1/t}.$ This can also be proved by the Hölder inequality. In measure theory, this is particularly notable for proving the inclusion L*s* ⊂ L*t* of L*p* spaces, in the special case of probability spaces.
- Hölder's inequality: if *p* > 1 and *q* > 1 are numbers satisfying *p* −1 + *q* −1 = 1, then $\operatorname {E} |XY|\leq (\operatorname {E} |X|^{p})^{1/p}(\operatorname {E} |Y|^{q})^{1/q}.$ for any random variables X and Y. The special case of *p* = *q* = 2 is called the Cauchy–Schwarz inequality, and is particularly well-known.
- Minkowski inequality: given any number *p* ≥ 1, for any random variables X and Y with E|*X*|*p* and E|*Y*|*p* both finite, it follows that E|*X* + *Y*|*p* is also finite and ${\Bigl (}\operatorname {E} |X+Y|^{p}{\Bigr )}^{1/p}\leq {\Bigl (}\operatorname {E} |X|^{p}{\Bigr )}^{1/p}+{\Bigl (}\operatorname {E} |Y|^{p}{\Bigr )}^{1/p}.$

The Hölder and Minkowski inequalities can be extended to general measure spaces, and are often given in that context. By contrast, the Jensen inequality is special to the case of probability spaces.

### Expectations under convergence of random variables

In general, it is not the case that $\operatorname {E} [X_{n}]\to \operatorname {E} [X]$ even if $X_{n}\to X$ pointwise. Thus, one cannot interchange limits and expectation, without additional conditions on the random variables. To see this, let U be a random variable distributed uniformly on $[0,1].$ For $n\geq 1,$ define a sequence of random variables $X_{n}=n\cdot \mathbf {1} \left\{U\in \left(0,{\tfrac {1}{n}}\right)\right\},$ with $\mathbf {1} \{A\}$ being the indicator function of the event $A.$ Then, it follows that $X_{n}\to 0$ pointwise. But, $\operatorname {E} [X_{n}]=n\cdot \Pr \left(U\in \left[0,{\tfrac {1}{n}}\right]\right)=n\cdot {\tfrac {1}{n}}=1$ for each $n.$ Hence, $\lim _{n\to \infty }\operatorname {E} [X_{n}]=1\neq 0=\operatorname {E} \left[\lim _{n\to \infty }X_{n}\right].$

Analogously, for general sequence of random variables $\{Y_{n}:n\geq 0\},$ the expected value operator is not $\sigma$ -additive, i.e. $\operatorname {E} \left[\sum _{n=0}^{\infty }Y_{n}\right]\neq \sum _{n=0}^{\infty }\operatorname {E} [Y_{n}].$

An example is easily obtained by setting $Y_{0}=X_{1}$ and $Y_{n}=X_{n+1}-X_{n}$ for $n\geq 1,$ where $X_{n}$ is as in the previous example.

A number of convergence results specify exact conditions which allow one to interchange limits and expectations, as specified below.

- Monotone convergence theorem: Let $\{X_{n}:n\geq 0\}$ be a sequence of random variables, with $0\leq X_{n}\leq X_{n+1}$ (a.s) for each $n\geq 0.$ Furthermore, let $X_{n}\to X$ pointwise. Then, the monotone convergence theorem states that $\lim _{n}\operatorname {E} [X_{n}]=\operatorname {E} [X].$ Using the monotone convergence theorem, one can show that expectation indeed satisfies countable additivity for non-negative random variables. In particular, let $\{X_{i}\}_{i=0}^{\infty }$ be non-negative random variables. It follows from the monotone convergence theorem that $\operatorname {E} \left[\sum _{i=0}^{\infty }X_{i}\right]=\sum _{i=0}^{\infty }\operatorname {E} [X_{i}].$
- Fatou's lemma: Let $\{X_{n}\geq 0:n\geq 0\}$ be a sequence of non-negative random variables. Fatou's lemma states that $\operatorname {E} [\liminf _{n}X_{n}]\leq \liminf _{n}\operatorname {E} [X_{n}].$ **Corollary.** Let $X_{n}\geq 0$ with $\operatorname {E} [X_{n}]\leq C$ for all $n\geq 0.$ If $X_{n}\to X$ (a.s), then $\operatorname {E} [X]\leq C.$ **Proof** is by observing that ${\textstyle X=\liminf _{n}X_{n}}$ (a.s.) and applying Fatou's lemma.
- Dominated convergence theorem: Let $\{X_{n}:n\geq 0\}$ be a sequence of random variables. If $X_{n}\to X$ pointwise (a.s.), $|X_{n}|\leq Y\leq +\infty$ (a.s.), and $\operatorname {E} [Y]<\infty .$ Then, according to the dominated convergence theorem,
  - $\operatorname {E} |X|\leq \operatorname {E} [Y]<\infty$ ;
  - $\lim _{n}\operatorname {E} [X_{n}]=\operatorname {E} [X]$
  - $\lim _{n}\operatorname {E} |X_{n}-X|=0.$
- Uniform integrability: In some cases, the equality $\lim _{n}\operatorname {E} [X_{n}]=\operatorname {E} [\lim _{n}X_{n}]$ holds when the sequence $\{X_{n}\}$ is *uniformly integrable.*

### Relationship with characteristic function

The probability density function $f_{X}$ of a scalar random variable X is related to its characteristic function $\varphi _{X}$ by the inversion formula: $f_{X}(x)={\frac {1}{2\pi }}\int _{\mathbb {R} }e^{-itx}\varphi _{X}(t)\,dt.$

For the expected value of $g(X)$ (where $g:{\mathbb {R} }\to {\mathbb {R} }$ is a Borel function), we can use this inversion formula to obtain $\operatorname {E} [g(X)]={\frac {1}{2\pi }}\int _{\mathbb {R} }g(x)\left[\int _{\mathbb {R} }e^{-itx}\varphi _{X}(t)\,dt\right]dx.$

If $\operatorname {E} [g(X)]$ is finite, changing the order of integration, we get, in accordance with Fubini–Tonelli theorem, $\operatorname {E} [g(X)]={\frac {1}{2\pi }}\int _{\mathbb {R} }G(t)\varphi _{X}(t)\,dt,$ where $G(t)=\int _{\mathbb {R} }g(x)e^{-itx}\,dx$ is the Fourier transform of $g(x).$ The expression for $\operatorname {E} [g(X)]$ also follows directly from the Plancherel theorem.

## Uses and applications

The expectation of a random variable plays an important role in a variety of contexts.

In statistics, where one seeks estimates for unknown parameters based on available data gained from samples, the sample mean serves as an estimate for the expectation, and is itself a random variable. In such settings, the sample mean is considered to meet the desirable criterion for a "good" estimator in being unbiased; that is, the expected value of the estimate is equal to the true value of the underlying parameter.

For a different example, in decision theory, an agent making an optimal choice in the context of incomplete information is often assumed to maximize the expected value of their utility function.

It is possible to construct an expected value equal to the probability of an event by taking the expectation of an indicator function that is one if the event has occurred and zero otherwise. This relationship can be used to translate properties of expected values into properties of probabilities, e.g. using the law of large numbers to justify estimating probabilities by frequencies.

The expected values of the powers of *X* are called the moments of *X*; the moments about the mean of *X* are expected values of powers of *X* − E[*X*]. The moments of some random variables can be used to specify their distributions, via their moment generating functions.

To empirically estimate the expected value of a random variable, one repeatedly measures observations of the variable and computes the arithmetic mean of the results. If the expected value exists, this procedure estimates the true expected value in an unbiased manner and has the property of minimizing the sum of the squares of the residuals (the sum of the squared differences between the observations and the estimate). The law of large numbers demonstrates (under fairly mild conditions) that, as the size of the sample gets larger, the variance of this estimate gets smaller.

This property is often exploited in a wide variety of applications, including general problems of statistical estimation and machine learning, to estimate (probabilistic) quantities of interest via Monte Carlo methods, since most quantities of interest can be written in terms of expectation, e.g. $\operatorname {P} ({X\in {\mathcal {A}}})=\operatorname {E} [{\mathbf {1} }_{\mathcal {A}}],$ where ${\mathbf {1} }_{\mathcal {A}}$ is the indicator function of the set ${\mathcal {A}}.$

In classical mechanics, the center of mass is an analogous concept to expectation. For example, suppose *X* is a discrete random variable with values *xi* and corresponding probabilities *pi.* Now consider a weightless rod on which are placed weights, at locations *xi* along the rod and having masses *pi* (whose sum is one). The point at which the rod balances is E[*X*].

Expected values can also be used to compute the variance, by means of the computational formula for the variance $\operatorname {Var} (X)=\operatorname {E} [X^{2}]-(\operatorname {E} [X])^{2}.$

A very important application of the expectation value is in the field of quantum mechanics. The expectation value of a quantum mechanical operator ${\hat {A}}$ operating on a quantum state vector $|\psi \rangle$ is written as $\langle {\hat {A}}\rangle =\langle \psi |{\hat {A}}|\psi \rangle .$ The variance in ${\hat {A}}$ can be calculated by the formula $(\Delta A)^{2}=\langle {\hat {A}}^{2}\rangle -\langle {\hat {A}}\rangle ^{2}$ .
