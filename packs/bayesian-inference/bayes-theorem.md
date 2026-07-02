---
title: "Bayes' theorem"
source: https://en.wikipedia.org/wiki/Bayes'_theorem
domain: bayesian-inference
license: CC-BY-SA-4.0
tags: bayesian inference, posterior probability, prior distribution, probabilistic reasoning
fetched: 2026-07-02
---

# Bayes' theorem

**Bayes' theorem** (alternatively **Bayes' law** or **Bayes' rule**), named after Thomas Bayes (/beɪz/), gives a mathematical rule for inverting conditional probabilities, allowing the probability of a cause to be found given its effect. For example, with Bayes' theorem, the probability that a patient has a disease given that they tested positive for that disease can be found using the probability that the test yields a positive result when the disease is present. The theorem was developed in the 18th century by Bayes and independently by Pierre-Simon Laplace.

One of Bayes' theorem's many applications is Bayesian inference, an approach to statistical inference, where it is used to invert the probability of observations given a model configuration (i.e., the likelihood function) to obtain the probability of the model configuration given the observations (i.e., the posterior probability).

## History

Bayes' theorem is named after Thomas Bayes, a minister, statistician, and philosopher. Bayes used conditional probability to provide an algorithm (his Proposition 9) that uses evidence to calculate limits on an unknown parameter. His work was published in 1763 as *An Essay Towards Solving a Problem in the Doctrine of Chances*. Bayes studied how to compute a distribution for the probability parameter of a binomial distribution (in modern terminology). After Bayes's death, his family gave his papers to a friend, the minister, philosopher, and mathematician Richard Price.

Price significantly edited the unpublished manuscript for two years before sending it to a friend who read it aloud at the Royal Society on 23 December 1763. Price edited Bayes's major work "An Essay Towards Solving a Problem in the Doctrine of Chances" (1763), which appeared in *Philosophical Transactions*, and contains Bayes' theorem. Price wrote an introduction to the paper that provides some of the philosophical basis of Bayesian statistics and chose one of the two solutions Bayes offered. In 1765, Price was elected a Fellow of the Royal Society in recognition of his work on Bayes's legacy. On 27 April, a letter sent to his friend Benjamin Franklin was read out at the Royal Society, and later published, in which Price applies this work to population and computing 'life-annuities'.

Independently of Bayes, Pierre-Simon Laplace used conditional probability to formulate the relation of an updated posterior probability from a prior probability, given evidence. He reproduced and extended Bayes's results in 1774, apparently unaware of Bayes's work, and summarized his results in *Théorie analytique des probabilités* (1812). The Bayesian interpretation of probability was developed mainly by Laplace.

About 200 years later, Sir Harold Jeffreys put Bayes's algorithm and Laplace's formulation on an axiomatic basis, writing in a 1973 book that Bayes' theorem "is to the theory of probability what the Pythagorean theorem is to geometry".

Stephen Stigler used a Bayesian argument to conclude that Bayes' theorem was discovered by Nicholas Saunderson, a blind English mathematician, some time before Bayes, but that is disputed. F. Thomas Bruss reviewed Bayes's "An essay towards solving a problem in the doctrine of chances" as communicated by Price. He agreed with Stigler's analysis on many points, but not on the question of priority. Bruss underlined the intuitive part of Bayes's formula and added independent arguments about Bayes's probable motivation for his work. He concluded that, unless the contrary is proven, the name "Bayes' Theorem" or "Bayes' formula" is justifiable.

Martyn Hooper and Sharon McGrayne have argued that Price's contribution was substantial:

> By modern standards, we should refer to the Bayes–Price rule. Price discovered Bayes's work, recognized its importance, corrected it, contributed to the article, and found a use for it. The modern convention of employing Bayes's name alone is unfair but so entrenched that anything else makes little sense.

The "Bayes factor" or "likelihood" that appears when writing Bayes' theorem in odds form appears in the early 1940s work of Alan Turing, who called it the "factor in favour of a proposition". In 1878, Charles Sanders Peirce used the logarithm of this factor as the "weight of evidence" for a proposition.

## Statement of theorem

Bayes' theorem is stated mathematically as the following equation:

$P(A\vert B)={\frac {P(B\vert A)P(A)}{P(B)}}$

where A and B are events and $P(B)\neq 0$ .

- $P(A\vert B)$ is a conditional probability: the probability of event A occurring given that B is true. It is also called the posterior probability of A given B .
- $P(B\vert A)$ is also a conditional probability: the probability of event B occurring given that A is true. It can also be interpreted as the likelihood function evaluated at A given a fixed B .
- $P(A)$ and $P(B)$ are the probabilities of observing A and B respectively without any given conditions. $P(A)$ , the quantity of interest, is often called 'the prior probability' (prior to new evidence). Technically both $P(A)$ and $P(B)$ could be called prior, unconditioned, or marginal probabilities.

Bayes' theorem may be derived from the relation between joint and conditional probabilities. The joint probability of the events A and B both happening, written $P(A\cap B)$ , is equal to the conditional probability of A given B times the probability of B : $P(A\cap B)=P(A\vert B)P(B).$ Likewise, $P(A\cap B)=P(B\vert A)P(A).$ The two products must therefore be equal to each other: $P(A\vert B)P(B)=P(B\vert A)P(A),$ and dividing both sides by $P(B)$ gives Bayes' theorem: $P(A\vert B)={\frac {P(B\vert A)P(A)}{P(B)}},{\text{ if }}P(B)\neq 0.$

If events *A*1, *A*2, ..., are mutually exclusive and exhaustive, i.e., one of them is certain to occur but no two can occur together, then, by the law of total probability, $P(B)=\sum _{i}P(B|A_{i})P(A_{i})$ for any event *B.* Substituting this expression for $P(B)$ into the denominator of the earlier equation gives: $P(A_{i}|B)={\frac {P(A_{i})P(B|A_{i})}{\sum _{j}P(A_{j})P(B|A_{j})}}.$

The events A and not- A , written $\neg A$ , are a mutually exclusive and exhaustive pair. Therefore the previous formula can be applied, and the sum in the denominator will have only two terms: $P(A|B)={\frac {P(B|A)P(A)}{P(B|A)P(A)+P(B|\neg A)P(\neg A)}}.$

## Examples

### Medical diagnosis

Suppose that a doctor is testing a patient for the presence of a certain disease. The patient either has the disease or does not; the test returns either positive or negative. If the patient does not have the disease but the test returns a positive result, that is a *false positive.* If the patient has the disease and the test returns a positive result, that is a *true positive.* Bayes' theorem gives the means to calculate the probability that the patient has the disease given a positive test result, using quantities that specify how prevalent the disease is in the population and how well the test works. Let E be the event that the patient has the disease. $P(E)$ is the probability that the patient has the disease. Let F be the event that the patient tests positive. The probability that the patient has the disease given that they test positive is thus denoted $P(E|F)$ . Bayes' theorem states: $P(E|F)={\frac {P(F|E)P(E)}{P(F|E)P(E)+P(F|\neg E)P(\neg E)}}.$ Here, $P(E)$ is the *prevalence rate* of the disease, and $P(F|E)$ is the *true positive rate* or *test sensitivity.*

For example, if all patients with pancreatic cancer have certain symptoms, it does not follow that anyone who has those symptoms has pancreatic cancer. Assuming the incidence rate of pancreatic cancer is 1/100000, while 10/99999 healthy people have the symptoms, the probability that a person who has the symptoms has pancreatic cancer is 9.1%.

Based on incidence rate, the following table presents the corresponding numbers per 100,000 people.

| SymptomCancer | Yes | No |   | Total |
|---|---|---|---|---|
| Yes | 1 | 0 | 1 |   |
| No | 10 | 99989 | 99999 |   |
|   |   |   |   |   |
| Total | 11 | 99989 | 100000 |   |

These numbers can then be used to calculate the probability that a patient who has the symptoms has cancer:

${\begin{aligned}P({\text{Cancer}}|{\text{Symptoms}})&={\frac {P({\text{Symptoms}}|{\text{Cancer}})P({\text{Cancer}})}{P({\text{Symptoms}})}}\\&={\frac {P({\text{Symptoms}}|{\text{Cancer}})P({\text{Cancer}})}{P({\text{Symptoms}}|{\text{Cancer}})P({\text{Cancer}})+P({\text{Symptoms}}|{\text{Non-Cancer}})P({\text{Non-Cancer}})}}\\[8pt]&={\frac {1\times 0.00001}{1\times 0.00001+(10/99999)\times 0.99999}}={\frac {1}{11}}\approx 9.1\%.\end{aligned}}$

### Drug testing

Suppose a particular test for whether someone has been using a drug (e.g., Substance D) is 99% sensitive, meaning the true positive rate (TPR) = 0.99. The test then has 99% true positive results (correct identification of drug use) for drug users. The test is also 99% specific, meaning its true negative rate (TNR) = 0.99. Therefore, the test correctly identifies 99% of non-use for non-users, but also generates 1% false positives, or false positive rate (FPR) = 0.01, for non-users. Assuming 0.3% of people use the drug, Bayes' theorem gives the probability that a random person who tests positive is a drug user: ${\begin{aligned}P({\text{User}}\vert {\text{Positive}})&={\frac {P({\text{Positive}}\vert {\text{User}})P({\text{User}})}{P({\text{Positive}})}}\\&={\frac {P({\text{Positive}}\vert {\text{User}})P({\text{User}})}{P({\text{Positive}}\vert {\text{User}})P({\text{User}})+P({\text{Positive}}\vert {\text{Non-user}})P({\text{Non-user}})}}\\[8pt]&={\frac {0.99\times 0.003}{0.99\times 0.003+0.01\times 0.997}}\approx 23\%.\end{aligned}}$ Consequently, even though the drug test is "99% accurate", most of its positive results will be false.

### Bent coins

An urn contains coins of three different types: A, B, and C. Coins of type A are fair and, when flipped, come up heads with probability 0.5. Coins of type B are biased and have probability 0.6 of turning up heads, and type-C coins come up heads with probability 0.9. The urn contains 2 type-A coins, 2 type-B coins and 1 type-C coin. A coin is drawn at random from the urn and flipped. Bayes' theorem gives the probability of a coin being of a given type given that it comes up heads: $P(A|H)={\frac {P(H|A)P(A)}{P(H)}},$ and likewise for $P(B|H)$ and $P(C|H)$ . The denominator can be found via the law of total probability: $P(H)=P(H|A)P(A)+P(H|B)P(B)+P(H|C)P(C).$ Assuming the coins are drawn from the urn at random, $P(A)=2/5$ , $P(B)=2/5$ , and $P(C)=1/5$ . It follows that $P(H)=0.62$ , and $P(A|H)=0.2/0.62\approx 32\%.$

## Interpretations

The interpretation of Bayes' rule depends on the interpretation of probability ascribed to the terms. The two predominant classes of interpretation are described below.

### Bayesian interpretations

In Bayesian (or epistemological) interpretations, probability measures a rational "degree of belief". Bayes' theorem links the degree of belief in a proposition before and after rationally accounting for evidence. For example, in a medical testing scenario, if a patient tests positive for a disease, the doctor will find it more plausible that the patient has that disease.

| Background Proposition | B | ⁠ $\lnot B$ ⁠ (not B) | Total |
|---|---|---|---|
| A | $P(B\|A)\cdot P(A)$ $=P(A\|B)\cdot P(B)$ | $P(\neg B\|A)\cdot P(A)$ $=P(A\|\neg B)\cdot P(\neg B)$ | ⁠ $P(A)$ ⁠ |
| ⁠ $\neg A$ ⁠ (not A) | $P(B\|\neg A)\cdot P(\neg A)$ $=P(\neg A\|B)\cdot P(B)$ | $P(\neg B\|\neg A)\cdot P(\neg A)$ $=P(\neg A\|\neg B)\cdot P(\neg B)$ | $P(\neg A)$ = $1-P(A)$ |
|   |   |   |   |
| Total | ⁠ $P(B)$ ⁠ | $P(\neg B)=1-P(B)$ | 1 |

If *A* denotes a proposition and *B* the evidence or background *B*, then

- $P(A)$ is the prior probability, the initial degree of belief in *A*.
- $P(\neg A)$ is the corresponding initial degree of belief that *A* is false, which is $P(\neg A)=1-P(A)$ .
- $P(B|A)$ is the conditional probability or likelihood, the degree of belief in *B* given that *A* is true.
- $P(B|\neg A)$ is the conditional probability or likelihood, the degree of belief in *B* given that *A* is false.
- $P(A|B)$ is the posterior probability, the probability of *A* after taking into account *B*.

For more on the application of Bayes' theorem under Bayesian interpretations of probability, see Bayesian inference.

### Frequentist interpretations

In the frequentist interpretations, probability measures a "proportion of outcomes". For example, suppose an experiment is performed many times. *P*(*A*) is the proportion of outcomes with property *A* (the prior) and *P*(*B*) is the proportion with property *B*. *P*(*B*|*A*) is the proportion of outcomes with property *B* *out of* outcomes with property *A*, and *P*(*A*|*B*) is the proportion of those with *A* *out of* those with *B* (the posterior).

## Forms

### Prior and likelihood

For events *A* and *B*, provided that *P*(*B*) ≠ 0,

$P(A|B)={\frac {P(B|A)P(A)}{P(B)}}.$

In many applications, for instance in Bayesian inference, the event *B* is fixed in the discussion and we wish to consider the effect of its having been observed on our belief in various possible events *A*. In such situations the denominator of the last expression, the probability of the given evidence *B*, is fixed; what we want to vary is *A*. Bayes' theorem shows that the posterior probabilities are proportional to the numerator, so the last equation becomes:

$P(A|B)\propto P(A)\cdot P(B|A).$

In other words, the posterior is proportional to the prior times the likelihood.

### Random variables

For two continuous random variables *X* and *Y*, Bayes' theorem may be analogously derived from the definition of conditional density:

$f_{X\vert Y=y}(x)={\frac {f_{X,Y}(x,y)}{f_{Y}(y)}}$

$f_{Y\vert X=x}(y)={\frac {f_{X,Y}(x,y)}{f_{X}(x)}}$

Bayes' theorem states:

$f_{X\vert Y=y}(x)={\frac {f_{Y\vert X=x}(y)f_{X}(x)}{f_{Y}(y)}}.$

This holds for values x and y within the support of *X* and *Y*, ensuring $f_{X}(x)>0$ and $f_{Y}(y)>0$ .

#### General case

Let $P_{Y}^{x}$ be the conditional distribution of Y given $X=x$ and let $P_{X}$ be the distribution of X . The joint distribution is then $P_{X,Y}(dx,dy)=P_{Y}^{x}(dy)P_{X}(dx)$ . The conditional distribution $P_{X}^{y}$ of X given $Y=y$ is then determined by

$P_{X}^{y}(A)=E(1_{A}(X)|Y=y)$

Existence and uniqueness of the needed conditional expectation is a consequence of the Radon–Nikodym theorem. Andrey Kolmogorov formulated this in 1933. He underlined the importance of conditional probability, writing, "I wish to call attention to ... the theory of conditional probabilities and conditional expectations". Bayes' theorem determines the posterior distribution from the prior distribution. Uniqueness requires continuity assumptions. Bayes' theorem can be generalized to include improper prior distributions such as the uniform distribution on the real line. Modern Markov chain Monte Carlo methods have boosted the importance of Bayes' theorem, including in cases with improper priors.

### In odds form

Probabilities are sometimes specified in terms of odds. For any proposition A , the ratio of the probability that A is true to the probability that A is false is called the odds on A . Bayes' theorem can be written using odds as follows. First, apply Bayes' theorem to the probability that A is true given some other proposition B : $P(A|B)=P(A){\frac {P(B|A)}{P(B)}}.$ Likewise, Bayes' theorem holds for the probability that A is false: $P(\neg A|B)=P(\neg A){\frac {P(B|\neg A)}{P(B)}}.$ Dividing these two equations, the probability $P(B)$ drops out: ${\frac {P(A|B)}{P(\neg A|B)}}={\frac {P(A)}{P(\neg A)}}{\frac {P(B|A)}{P(B|\neg A)}}.$ Consequently, the odds of A given B are the odds of A multiplied by the ratio $P(B|A)/P(B|\neg A)$ , a quantity called the Bayes factor or likelihood ratio. In symbols: $O(A|B)=O(A){\frac {P(B|A)}{P(B|\neg A)}}.$ This is often summarized by saying that the *posterior odds* are the *prior odds* times the likelihood.

For example, suppose that a disease has a prevalence of 1%, i.e., the probability that a randomly chosen person is infected is 0.01. And suppose that a test for the disease returns the correct result with 99% probability. The prior odds of being infected are $O({\text{infected}})={\frac {P({\text{infected}})}{P({\text{not infected}})}}={\frac {0.01}{1-0.01}}={\frac {1}{99}}.$

The probability that the test is positive given an infection is 99%: $P({\text{positive}}|{\text{infected}})=0.99.$ The probability that the test is negative given absence of an infection is also 99%, and so $P({\text{positive}}|{\text{not infected}})=1-P({\text{negative}}|{\text{not infected}})=1-0.99=0.01.$ The Bayes factor is the ratio ${\frac {P({\text{positive}}|{\text{infected}})}{P({\text{positive}}|{\text{not infected}})}}={\frac {0.99}{0.01}}={\frac {99}{1}}.$ Therefore, the posterior odds of an infection given a positive test result are ${\frac {1}{99}}\times {\frac {99}{1}}={\frac {1}{1}};$ in other words, the posterior odds of infection are one to one, and the posterior probability of infection is 50%.

## Generalizations

### Bayes' theorem for 3 events

A version of Bayes' theorem for 3 events results from the addition of a third event C , with $P(C)>0,$ on which all probabilities are conditioned:

$P(A\vert B\cap C)={\frac {P(B\vert A\cap C)\,P(A\vert C)}{P(B\vert C)}}$

This can be deduced as follows. Using the chain rule

$P(A\cap B\cap C)=P(A\vert B\cap C)\,P(B\vert C)\,P(C)$

And, on the other hand

$P(A\cap B\cap C)=P(B\cap A\cap C)=P(B\vert A\cap C)\,P(A\vert C)\,P(C)$

The desired result is obtained by identifying both expressions and solving for $P(A\vert B\cap C)$ .

### Inference rules

In subjective interpretations of probability theory, an event's probability is regarded as an agent's belief that the event will happen. Bayes' theorem is widely invoked to justify how an agent should update or modify their beliefs after receiving new information. If an agent assigns the probability $P(A)$ to the event A , $P(B)$ to the event B , and $P(B|A)$ to the event " B happens assuming A has already happened", Bayes' theorem gives the value of $P(A|B)$ . Suppose that, after the agent has made these probability assignments, event B occurs. An agent who follows *Bayesian updating,* also known as updating by *conditionalization,* will change their probability for event A from the old value $P(A)$ to the new value $P'(A)=P(A|B)$ . Conditionalization is not the only updating rule that might be considered rational. The issue of which assumptions can be invoked to constrain updating rules remains somewhat controversial.

### Quantum

In quantum mechanics, probability distributions are generalized to density matrices, arrays of complex numbers that describe the preparation of a quantum system. A *quantum Bayes rule* can be formulated that expresses how density matrices are updated as new experimental data about a system is obtained.

## Selected applications

### Parameter estimation

In Bayesian statistics, an object or system is represented by a mathematical model that contains one or more numerical parameters. The available information about the system is used to write a probability distribution over the possible values of those parameters, indicating which values are more plausible than others. Bayes' theorem is then used to update that probability distribution as new evidence is obtained.

### Recreational mathematics

Bayes' rule and computing conditional probabilities provide a method to solve a number of popular puzzles, such as the Three Prisoners problem, the Monty Hall problem, the Boy or Girl paradox, and the two envelopes problem.

### Cryptanalysis

Alan Turing and his collaborators at Bletchley Park pioneered the use of Bayes' theorem for breaking ciphers during World War II. In 1941, Turing wrote a set of pedagogical notes introducing Bayesian methods of cryptanalysis by applying them to problems like solving a Vigenère cipher, which were simpler than his team's primary focus, reading messages encrypted by the Enigma machine. Bayes' theorem was also applied to the cracking of the Japanese naval code JN 25.

### Genetics

In genetics, Bayes' rule can be used to estimate the probability that someone has a specific genotype. Many people seek to assess their chances of being affected by a genetic disease or their likelihood of being a carrier for a recessive gene of interest. A Bayesian analysis can be done based on family history or genetic testing to predict whether someone will develop a disease or pass one on to their children. (Genetic testing and prediction is common among couples who plan to have children but are concerned that they may both be carriers for a disease, especially in communities with low genetic variance.)

### Evolutionary biology

Bayes' theorem is employed in evolutionary biology to deduce trees of relationships among species that best explain the available data. This approach was made practical by the use of Markov chain Monte Carlo methods.
