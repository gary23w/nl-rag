---
title: "Conditional probability"
source: https://en.wikipedia.org/wiki/Conditional_probability
domain: probability-theory
license: CC-BY-SA-4.0
tags: probability theory, random variable, probability space, law of large numbers
fetched: 2026-07-02
---

# Conditional probability

In probability theory, **conditional probability** is a measure of the probability of an event occurring, given that another event (by assumption, presumption, assertion, or evidence) is already known to have occurred. This particular method relies on event A occurring with some sort of relationship with another event B. In this situation, the event A can be analyzed by a conditional probability with respect to B. If the event of interest is A and the event B is known or assumed to have occurred, "the conditional probability of A given B", or "the probability of A under the condition B", is usually written as P(*A*|*B*) or occasionally P*B*(*A*). This can also be understood as the fraction of probability B that intersects with A, or the ratio of the probabilities of both events happening to the "given" one happening (how many times A occurs rather than not assuming B has occurred):

$P(A\mid B)={\frac {P(A\cap B)}{P(B)}}$

.

For example, the probability that any given person has a cough on any given day may be only 5%. But if we know or assume that the person is sick, then they are much more likely to be coughing. For example, the conditional probability that someone sick is coughing might be 75%, in which case we would have that P(Cough) = 5% and P(Cough|Sick) = 75%. Although there is a relationship between A and B in this example, such a relationship or dependence between A and B is not necessary, nor do they have to occur simultaneously.

P(*A*|*B*) may or may not be equal to P(*A*), i.e., the **unconditional probability** or **absolute probability** of A. If P(*A*|*B*) = P(*A*), then events A and B are said to be *independent*: in such a case, knowledge about either event does not alter the likelihood of the other. P(*A*|*B*) (the conditional probability of A given B) typically differs from P(*B*|*A*). For example, if a person has dengue fever, the person might have a 90% chance of being tested as positive for the disease. In this case, what is being measured is that if event B (*having dengue*) has occurred, the probability of A (*tested as positive*) given that B occurred is 90%, simply writing P(*A*|*B*) = 90%. Alternatively, if a person is tested as positive for dengue fever, they may have only a 15% chance of actually having this rare disease due to high false positive rates. In this case, the probability of the event B (*having dengue*) given that the event A (*testing positive*) has occurred is 15% or P(*B*|*A*) = 15%. It should be apparent now that falsely equating the two probabilities can lead to various errors of reasoning, which is commonly seen through base rate fallacies.

While conditional probabilities can provide extremely useful information, limited information is often supplied or at hand. Therefore, it can be useful to reverse or convert a conditional probability using Bayes' theorem: $P(A\mid B)={{P(B\mid A)P(A)} \over {P(B)}}$ . Another option is to display conditional probabilities in a conditional probability table to illuminate the relationship between events.

## Definition

### Conditioning on an event

#### Kolmogorov definition

Given two events A and B from the sigma-field of a probability space, with the unconditional probability of B being greater than zero (i.e., P(*B*) > 0), the conditional probability of A given B ( $P(A\mid B)$ ) is the probability of *A* occurring if *B* has or is assumed to have happened. *A* is assumed to be the set of all possible outcomes of an experiment or random trial that has a restricted or reduced sample space. The conditional probability can be found by the quotient of the probability of the joint intersection of events A and B, that is, $P(A\cap B)$ , the probability at which *A* and *B* occur together, and the probability of B:

$P(A\mid B)={\frac {P(A\cap B)}{P(B)}}.$

For a sample space consisting of equal likelihood outcomes, the probability of the event *A* is understood as the fraction of the number of outcomes in *A* to the number of all outcomes in the sample space. Then, this equation is understood as the fraction of the set $A\cap B$ to the set *B*. Note that the above equation is a definition, not just a theoretical result. We denote the quantity ${\frac {P(A\cap B)}{P(B)}}$ as $P(A\mid B)$ and call it the "conditional probability of A given B."

#### As an axiom of probability

Some authors, such as de Finetti, prefer to introduce conditional probability as an axiom of probability:

$P(A\cap B)=P(A\mid B)P(B).$

This equation for a conditional probability, although mathematically equivalent, may be intuitively easier to understand. It can be interpreted as "the probability of *B* occurring multiplied by the probability of *A* occurring, provided that *B* has occurred, is equal to the probability of the *A* and *B* occurrences together, although not necessarily occurring at the same time". Additionally, this may be preferred philosophically; under major probability interpretations, such as the subjective theory, conditional probability is considered a primitive entity. Moreover, this "multiplication rule" can be practically useful in computing the probability of $A\cap B$ and introduces a symmetry with the summation axiom for Poincaré Formula:

$P(A\cup B)=P(A)+P(B)-P(A\cap B)$

Thus the equations can be combined to find a new representation of the

:

$P(A\cap B)=P(A)+P(B)-P(A\cup B)=P(A\mid B)P(B)$

$P(A\cup B)={P(A)+P(B)-P(A\mid B){P(B)}}$

#### As the probability of a conditional event

Conditional probability can be defined as the probability of a conditional event $A_{B}$ . The Goodman–Nguyen–Van Fraassen conditional event can be defined as:

$A_{B}=\bigcup _{i\geq 1}\left(\bigcap _{j<i}{\overline {B}}_{j},A_{i}B_{i}\right),$

where

$A_{i}$

and

$B_{i}$

represent states or elements of

A

or

B.

It can be shown that

$P(A_{B})={\frac {P(A\cap B)}{P(B)}}$

which meets the Kolmogorov definition of conditional probability.

### Conditioning on an event of probability zero

If $P(B)=0$ , then according to the definition, $P(A\mid B)$ is undefined.

The case of greatest interest is that of a random variable Y, conditioned on a continuous random variable X resulting in a particular outcome x. The event $B=\{X=x\}$ has probability zero and, as such, cannot be conditioned on.

Instead of conditioning on X being *exactly* x, we could condition on it being closer than distance $\varepsilon$ away from x. The event $B=\{x-\varepsilon <X<x+\varepsilon \}$ will generally have nonzero probability and hence, can be conditioned on. We can then take the limit

| $\lim _{\varepsilon \to 0}P(A\mid x-\varepsilon <X<x+\varepsilon ).$ |   | 1 |
|---|---|---|

For example, if two continuous random variables X and Y have a joint density $f_{X,Y}(x,y)$ , then by L'Hôpital's rule and Leibniz integral rule, upon differentiation with respect to $\varepsilon$ :

${\begin{aligned}\lim _{\varepsilon \to 0}P(Y\in U\mid x_{0}-\varepsilon <X<x_{0}+\varepsilon )&=\lim _{\varepsilon \to 0}{\frac {\int _{x_{0}-\varepsilon }^{x_{0}+\varepsilon }\int _{U}f_{X,Y}(x,y)\,\mathrm {d} y\,\mathrm {d} x}{\int _{x_{0}-\varepsilon }^{x_{0}+\varepsilon }\int _{\mathbb {R} }f_{X,Y}(x,y)\,\mathrm {d} y\,\mathrm {d} x}}\\[6pt]&={\frac {\int _{U}f_{X,Y}(x_{0},y)\,\mathrm {d} y}{\int _{\mathbb {R} }f_{X,Y}(x_{0},y)\,\mathrm {d} y}}.\end{aligned}}$

The resulting limit is the conditional probability distribution of Y given X and exists when the denominator, the probability density $f_{X}(x_{0})$ , is strictly positive.

It is tempting to *define* the undefined probability $P(A\mid X=x)$ using limit (**1**), but this cannot be done in a consistent manner. In particular, it is possible to find random variables X and W and values x, w such that the events $\{X=x\}$ and $\{W=w\}$ are identical but the resulting limits are not:

$\lim _{\varepsilon \to 0}P(A\mid x-\varepsilon \leq X\leq x+\varepsilon )\neq \lim _{\varepsilon \to 0}P(A\mid w-\varepsilon \leq W\leq w+\varepsilon ).$

The Borel–Kolmogorov paradox demonstrates this with a geometrical argument.

### Conditioning on a discrete random variable

Let X be a discrete random variable and its possible outcomes denoted V. For example, if X represents the value of a rolled dice then V is the set $\{1,2,3,4,5,6\}$ . Let us assume for the sake of presentation that X is a discrete random variable, so that each value in V has a nonzero probability.

For a value x in V and an event A, the conditional probability is given by $P(A\mid X=x)$ . Writing

$c(x,A)=P(A\mid X=x)$

for short, we see that it is a function of two variables, x and A.

For a fixed A, we can form the random variable $Y=c(X,A)$ . It represents an outcome of $P(A\mid X=x)$ whenever a value x of X is observed.

The conditional probability of A given X can thus be treated as a random variable Y with outcomes in the interval $[0,1]$ . From the law of total probability, its expected value is equal to the unconditional probability of A.

### Partial conditional probability

The partial conditional probability $P(A\mid B_{1}\equiv b_{1},\ldots ,B_{m}\equiv b_{m})$ is about the probability of event A given that each of the condition events $B_{i}$ has occurred to a degree $b_{i}$ (degree of belief, degree of experience) that might be different from 100%. Frequentistically, partial conditional probability makes sense, if the conditions are tested in experiment repetitions of appropriate length n . Such n -bounded partial conditional probability can be defined as the conditionally expected average occurrence of event A in testbeds of length n that adhere to all of the probability specifications $B_{i}\equiv b_{i}$ , i.e.:

$P^{n}(A\mid B_{1}\equiv b_{1},\ldots ,B_{m}\equiv b_{m})=\operatorname {E} ({\overline {A}}^{n}\mid {\overline {B}}_{1}^{n}=b_{1},\ldots ,{\overline {B}}_{m}^{n}=b_{m})$

Based on that, partial conditional probability can be defined as

$P(A\mid B_{1}\equiv b_{1},\ldots ,B_{m}\equiv b_{m})=\lim _{n\to \infty }P^{n}(A\mid B_{1}\equiv b_{1},\ldots ,B_{m}\equiv b_{m}),$

where $b_{i}n\in \mathbb {N}$

Jeffrey conditionalization is a special case of partial conditional probability, in which the condition events must form a partition:

$P(A\mid B_{1}\equiv b_{1},\ldots ,B_{m}\equiv b_{m})=\sum _{i=1}^{m}b_{i}P(A\mid B_{i})$

## Example

Suppose that somebody secretly rolls two fair six-sided dice, and we wish to compute the probability that the face-up value of the first one is 2, given the information that their sum is no greater than 5.

- Let *D*1 be the value rolled on dice 1.
- Let *D*2 be the value rolled on dice 2.

***Probability that* *D*1 = 2**

Table 1 shows the sample space of 36 combinations of rolled values of the two dice, each of which occurs with probability 1/36, with the numbers displayed in the red and dark gray cells being *D*1 + *D*2.

*D*1 = 2 in exactly 6 of the 36 outcomes; thus *P*(*D*1 = 2) = 6⁄36 = 1⁄6:

| + | D2 |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 |   |   |
| *D*1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 2 | 3 | 4 | 5 | 6 | 7 | 8 |   |
| 3 | 4 | 5 | 6 | 7 | 8 | 9 |   |
| 4 | 5 | 6 | 7 | 8 | 9 | 10 |   |
| 5 | 6 | 7 | 8 | 9 | 10 | 11 |   |
| 6 | 7 | 8 | 9 | 10 | 11 | 12 |   |

***Probability that* *D*1 + *D*2 ≤ 5**

Table 2 shows that *D*1 + *D*2 ≤ 5 for exactly 10 of the 36 outcomes, thus *P*(*D*1 + *D*2 ≤ 5) = 10⁄36:

| + | *D*2 |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 |   |   |
| *D*1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 2 | 3 | 4 | 5 | 6 | 7 | 8 |   |
| 3 | 4 | 5 | 6 | 7 | 8 | 9 |   |
| 4 | 5 | 6 | 7 | 8 | 9 | 10 |   |
| 5 | 6 | 7 | 8 | 9 | 10 | 11 |   |
| 6 | 7 | 8 | 9 | 10 | 11 | 12 |   |

***Probability that* *D*1 = 2 *given that* *D*1 + *D*2 ≤ 5**

Table 3 shows that for 3 of these 10 outcomes, *D*1 = 2.

Thus, the conditional probability P(*D*1 = 2 | *D*1+*D*2 ≤ 5) = 3⁄10 = 0.3:

| + | *D*2 |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 |   |   |
| *D*1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 2 | 3 | 4 | 5 | 6 | 7 | 8 |   |
| 3 | 4 | 5 | 6 | 7 | 8 | 9 |   |
| 4 | 5 | 6 | 7 | 8 | 9 | 10 |   |
| 5 | 6 | 7 | 8 | 9 | 10 | 11 |   |
| 6 | 7 | 8 | 9 | 10 | 11 | 12 |   |

Here, in the earlier notation for the definition of conditional probability, the conditioning event *B* is that *D*1 + *D*2 ≤ 5, and the event *A* is *D*1 = 2. We have $P(A\mid B)={\tfrac {P(A\cap B)}{P(B)}}={\tfrac {3/36}{10/36}}={\tfrac {3}{10}},$ as seen in the table.

## Use in inference

In statistical inference, the conditional probability is an update of the probability of an event based on new information. The new information can be incorporated as follows:

- Let *A*, the event of interest, be in the sample space, say (*X*,*P*).
- The occurrence of the event *A* knowing that event *B* has or will have occurred, means the occurrence of *A* as it is restricted to *B*, i.e. $A\cap B$ .
- Without the knowledge of the occurrence of *B*, the information about the occurrence of *A* would simply be *P*(*A*)
- The probability of *A* knowing that event *B* has or will have occurred, will be the probability of $A\cap B$ relative to *P*(*B*), the probability that *B* has occurred.
- This results in ${\textstyle P(A\mid B)=P(A\cap B)/P(B)}$ whenever *P*(*B*) > 0 and 0 otherwise.

This approach results in a probability measure that is consistent with the original probability measure and satisfies all the Kolmogorov axioms. This conditional probability measure also could have resulted by assuming that the relative magnitude of the probability of *A* with respect to *X* will be preserved with respect to *B* (cf. a Formal Derivation below).

The wording "evidence" or "information" is generally used in the Bayesian interpretation of probability. The conditioning event is interpreted as evidence for the conditioned event. That is, *P*(*A*) is the probability of *A* before accounting for evidence *E*, and *P*(*A*|*E*) is the probability of *A* after having accounted for evidence *E* or after having updated *P*(*A*). This is consistent with the frequentist interpretation, which is the first definition given above.

### Example

When Morse code is transmitted, there is a certain probability that the "dot" or "dash" that was received is erroneous. This is often taken as interference in the transmission of a message. Therefore, it is important to consider when sending a "dot", for example, the probability that a "dot" was received. This is represented by: $P({\text{dot sent }}|{\text{ dot received}})=P({\text{dot received }}|{\text{ dot sent}}){\frac {P({\text{dot sent}})}{P({\text{dot received}})}}.$ In Morse code, the ratio of dots to dashes is 3:4 at the point of sending, so the probabilities of a "dot" and "dash" are $P({\text{dot sent}})={\frac {3}{7}}{\text{ and }}P({\text{dash sent}})={\frac {4}{7}}$ . If it is assumed that the probability that a dot is transmitted as a dash is 1/10, and that the probability that a dash is transmitted as a dot is likewise 1/10, then Bayes's rule can be used to calculate $P({\text{dot received}})$ .

$P({\text{dot received}})=P({\text{dot received}}\cap {\text{dot sent}})+P({\text{dot received}}\cap {\text{dash sent}})$

$P({\text{dot received}})=P({\text{dot received}}\mid {\text{dot sent}})P({\text{dot sent}})+P({\text{dot received}}\mid {\text{dash sent}})P({\text{dash sent}})$

$P({\text{dot received}})={\frac {9}{10}}\times {\frac {3}{7}}+{\frac {1}{10}}\times {\frac {4}{7}}={\frac {31}{70}}$

Now, $P({\text{dot sent}}\mid {\text{dot received}})$ can be calculated:

$P({\text{dot sent}}\mid {\text{dot received}})=P({\text{dot received}}\mid {\text{dot sent}}){\frac {P({\text{dot sent}})}{P({\text{dot received}})}}={\frac {9}{10}}\times {\frac {\frac {3}{7}}{\frac {31}{70}}}={\frac {27}{31}}$

## Information, Conditional Probability, and Statistical Independence

The concepts of **conditional probability** and **statistical independence** can be understood through the idea of how new information changes an individual's uncertainty about an event.

### Example 1

**Dependent Events (Six-Sided Die)**

Consider the experiment of rolling a fair six-sided die, where the sample space is $S=\{1,2,3,4,5,6\}$ . Let event **A** denote the occurrence of an even number, so $A=\{2,4,6\}$ , and let event **B** denote the occurrence of a number less than or equal to **3**, so $B=\{1,2,3\}$ . Before any additional information is available, the probabilities of these events are $P(A)={\frac {3}{6}}={\frac {1}{2}}$ and $P(B)={\frac {3}{6}}={\frac {1}{2}}$ . The intersection of the two events is $A\cap B=\{2\}$ , and therefore $P(A\cap B)={\frac {1}{6}}$ . If the events were statistically independent, we would expect $P(A\cap B)=P(A)P(B)$ . However, ${\frac {1}{6}}\neq {\frac {1}{2}}\times {\frac {1}{2}}={\frac {1}{4}}$ , indicating that events **A** and **B** are not independent but are instead statistically dependent.

Now suppose that an observer reveals that event **A** has occurred; that is, the outcome is known to be an even number. This new information reduces the effective sample space from $S=\{1,2,3,4,5,6\}$ to $A=\{2,4,6\}$ . Within this reduced sample space, event **B** can occur only when the outcome is **2**, so the relevant event becomes $A\cap B=\{2\}$ . Consequently, the conditional probability of event **B** given that event **A** has occurred is $P(B\mid A)={\frac {P(A\cap B)}{P(A)}}={\frac {1/6}{1/2}}={\frac {1}{3}}$ . Thus, the probability of event **B** changes from ${\frac {1}{2}}$ to ${\frac {1}{3}}$ after the additional information is provided. This change in probability demonstrates that knowledge of event **A** affects the likelihood of event **B**, confirming that the two events are statistically dependent. In such situations, additional information reduces uncertainty and can significantly influence rational decision-making, prediction, and betting behaviour.

### Example 2

**Independent Events (Eight-Sided Die)**

Consider the experiment of rolling a fair eight-sided die with sample space $S=\{1,2,3,4,5,6,7,8\}$ . Let event **A** represent the outcome being less than **5**, so that $A=\{1,2,3,4\}$ , and let event **B** represent the outcome being either **3, 4, 5, or 6**, so that $B=\{3,4,5,6\}$ . Initially, the probabilities of these events are $P(A)={\frac {4}{8}}={\frac {1}{2}}$ and $P(B)={\frac {4}{8}}={\frac {1}{2}}$ . The intersection of the two events is $A\cap B=\{3,4\}$ , and therefore $P(A\cap B)={\frac {2}{8}}={\frac {1}{4}}$ . Since $P(A)P(B={\frac {1}{2}}\times {\frac {1}{2}}={\frac {1}{4}}$ , we obtain $P(A\cap B)=P(A)P(B)$ , which confirms that events **A** and **B** are statistically independent.

Now suppose that an observer reveals that event (A) has occurred. This information reduces the effective sample space from $S=\{1,2,3,4,5,6,7,8\}$ to $A=\{1,2,3,4\}$ . Within this reduced sample space, the outcomes that also satisfy event **B** are $A\cap B=\{3,4\}$ . Consequently, the conditional probability of event **B** given that event **A** has occurred is $P(B\mid A)={\frac {P(A\cap B)}{P(A)}}={\frac {1/4}{1/2}}={\frac {1}{2}}$ . Notice that this conditional probability is equal to the original probability of event **B**, that is, $P(B\mid A)=P(B)$ . Therefore, learning that event **A** has occurred does not change the likelihood of event **B**. The information provided by event **A** has no effect on the uncertainty associated with event **B**, demonstrating the fundamental property of statistical independence: knowledge of one event does not alter the probability of the other event.

**Interpretation**

Statistical independence can therefore be interpreted as the absence of informational value between events. If knowledge of one event changes the probability of another event, the events are dependent. Conversely, if the probability remains unchanged after obtaining new information, the events are independent.

Formally, two events **A** and **B** are independent if and only if:

$P(B\mid A)=P(B),$ which is equivalent to: $P(A\cap B)=P(A)P(B).$

In this sense, independence implies that observing one event provides no additional information about the occurrence of the other event.

## Statistical independence

Events *A* and *B* are defined to be statistically independent if the probability of the intersection of A and B is equal to the product of the probabilities of A and B:

$P(A\cap B)=P(A)P(B).$

If *P*(*B*) is not zero, then this is equivalent to the statement that

$P(A\mid B)=P(A).$

Similarly, if *P*(*A*) is not zero, then

$P(B\mid A)=P(B)$

is also equivalent. Although the derived forms may seem more intuitive, they are not the preferred definition as the conditional probabilities may be undefined, and the preferred definition is symmetrical in *A* and *B*. Independence does not refer to a disjoint event.

It should also be noted that given the independent event pair [*A*,*B*] and an event *C*, the pair is defined to be conditionally independent if

$P(AB\mid C)=P(A\mid C)P(B\mid C).$

This theorem is useful in applications where multiple independent events are being observed.

**Independent events vs. mutually exclusive events**

The concepts of mutually independent events and mutually exclusive events are separate and distinct. The following table contrasts results for the two cases (provided that the probability of the conditioning event is not zero).

|   | **If statistically independent** | **If mutually exclusive** |
|---|---|---|
| $P(A\mid B)=$ | $P(A)$ | 0 |
| $P(B\mid A)=$ | $P(B)$ | 0 |
| $P(A\cap B)=$ | $P(A)P(B)$ | 0 |

In fact, mutually exclusive events cannot be statistically independent (unless both of them are impossible), since knowing that one occurs gives information about the other (in particular, that the latter will certainly not occur).

**Independent vs. Positive association vs. Negative association of events**

| Relation between A and B | Condition | Result |
|---|---|---|
| Independent | $P(A\cap B)=$ $P(A)P(B)$ | $P(B\mid A)=$ $P(B)$ |
| Positive Association | $P(A\cap B)$ > $P(A)P(B)$ | $P(B\mid A)$ > $P(B)$ |
| Negative Association | $P(A\cap B)$ < $P(A)P(B)$ | $P(B\mid A)$ < $P(B)$ |

## Common fallacies

These fallacies should not be confused with Robert K. Shope's 1978

"conditional fallacy"

, which deals with counterfactual examples that

beg the question

.

### Assuming conditional probability is of similar size to its inverse

In general, it cannot be assumed that *P*(*A*|*B*) ≈ *P*(*B*|*A*). This can be an insidious error, even for those who are highly conversant with statistics. The relationship between *P*(*A*|*B*) and *P*(*B*|*A*) is given by Bayes' theorem:

${\begin{aligned}P(B\mid A)&={\frac {P(A\mid B)P(B)}{P(A)}}\\\Leftrightarrow {\frac {P(B\mid A)}{P(A\mid B)}}&={\frac {P(B)}{P(A)}}\end{aligned}}$

That is, *P*(*A*|*B*) ≈ *P*(*B*|*A*) only if *P*(*B*)/*P*(*A*) ≈ 1, or equivalently, *P*(*A*) ≈ *P*(*B*).

### Assuming marginal and conditional probabilities are of similar size

In general, it cannot be assumed that *P*(*A*) ≈ *P*(*A*|*B*). These probabilities are linked through the law of total probability:

$P(A)=\sum _{n}P(A\cap B_{n})=\sum _{n}P(A\mid B_{n})P(B_{n}).$

where the events $(B_{n})$ form a countable partition of $\Omega$ .

This fallacy may arise through selection bias. For example, in the context of a medical claim, let *S**C* be the event that a sequela (chronic disease) *S* occurs as a consequence of circumstance (acute condition) *C*. Let *H* be the event that an individual seeks medical help. Suppose that in most cases, *C* does not cause *S* (so that *P*(*S**C*) is low). Suppose also that medical attention is only sought if *S* has occurred due to *C*. From experience of patients, a doctor may therefore erroneously conclude that *P*(*S**C*) is high. The actual probability observed by the doctor is *P*(*S**C*|*H*).

### Over- or under-weighting priors

Not taking prior probability into account partially or completely is called *base rate neglect*. The reverse, insufficient adjustment from the prior probability is *conservatism*.

## Formal derivation

Formally, *P*(*A* | *B*) is defined as the probability of *A* according to a new probability function on the sample space, such that outcomes not in *B* have probability 0 and that it is consistent with all original probability measures.

Let Ω be a discrete sample space with elementary events {*ω*}, and let *P* be the probability measure with respect to the σ-algebra of Ω. Suppose we are told that the event *B* ⊆ Ω has occurred. A new probability distribution (denoted by the conditional notation) is to be assigned on {*ω*} to reflect this. All events that are not in *B* will have null probability in the new distribution. For events in *B*, two conditions must be met: the probability of *B* is one and the relative magnitudes of the probabilities must be preserved. The former is required by the axioms of probability, and the latter stems from the fact that the new probability measure has to be the analog of *P* in which the probability of *B* is one—and every event that is not in *B*, therefore, has a null probability. Hence, for some scale factor *α*, the new distribution must satisfy:

1. $\omega \in B:P(\omega \mid B)=\alpha P(\omega )$
2. $\omega \notin B:P(\omega \mid B)=0$
3. $\sum _{\omega \in \Omega }{P(\omega \mid B)}=1.$

Substituting 1 and 2 into 3 to select *α*:

${\begin{aligned}1&=\sum _{\omega \in \Omega }{P(\omega \mid B)}\\&=\sum _{\omega \in B}{P(\omega \mid B)}+{\cancelto {0}{\sum _{\omega \notin B}P(\omega \mid B)}}\\&=\alpha \sum _{\omega \in B}{P(\omega )}\\[5pt]&=\alpha \cdot P(B)\\[5pt]\Rightarrow \alpha &={\frac {1}{P(B)}}\end{aligned}}$

So the new probability distribution is

1. $\omega \in B:P(\omega \mid B)={\frac {P(\omega )}{P(B)}}$
2. $\omega \notin B:P(\omega \mid B)=0$

Now for a general event *A*,

${\begin{aligned}P(A\mid B)&=\sum _{\omega \in A\cap B}{P(\omega \mid B)}+{\cancelto {0}{\sum _{\omega \in A\cap B^{c}}P(\omega \mid B)}}\\&=\sum _{\omega \in A\cap B}{\frac {P(\omega )}{P(B)}}\\[5pt]&={\frac {P(A\cap B)}{P(B)}}\end{aligned}}$
