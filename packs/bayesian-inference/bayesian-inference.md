---
title: "Bayesian inference"
source: https://en.wikipedia.org/wiki/Bayesian_inference
domain: bayesian-inference
license: CC-BY-SA-4.0
tags: bayesian inference, posterior probability, prior distribution, probabilistic reasoning
fetched: 2026-07-02
---

# Bayesian inference

**Bayesian inference** (/ˈbeɪziən/ *BAY-zee-ən* or /ˈbeɪʒən/ *BAY-zhən*) is a method of statistical inference in which Bayes' theorem is used to calculate a probability of a hypothesis, given prior evidence, and update it as more information becomes available. Fundamentally, Bayesian inference uses a prior distribution to estimate posterior probabilities. Bayesian inference is an important technique in statistics, and especially in mathematical statistics. Bayesian updating is particularly important in the dynamic analysis of a sequence of data. Bayesian inference has found application in a wide range of activities, including science, engineering, philosophy, medicine, sport, psychology, and law. In the philosophy of decision theory, Bayesian inference is closely related to subjective probability, often called "Bayesian probability".

## Introduction to Bayes' rule

### Formal explanation

| Hypothesis Evidence | Satisfies hypothesis H | Violates hypothesis ⁠ $\neg H$ ⁠ |   | Total |
|---|---|---|---|---|
| Has evidence E | $P(H\|E)\cdot P(E)$ $=P(E\|H)\cdot P(H)$ | $P(\neg H\|E)\cdot P(E)$ $=P(E\|\neg H)\cdot P(\neg H)$ | ⁠ $P(E)$ ⁠ |   |
| No evidence ⁠ $\neg E$ ⁠ | $P(H\|\neg E)\cdot P(\neg E)$ $=P(\neg E\|H)\cdot P(H)$ | $P(\neg H\|\neg E)\cdot P(\neg E)$ $=P(\neg E\|\neg H)\cdot P(\neg H)$ | $P(\neg E)$ = $1-P(E)$ |   |
|   |   |   |   |   |
| Total | ⁠ $P(H)$ ⁠ | $P(\neg H)=1-P(H)$ | 1 |   |

Bayesian inference derives the posterior probability as a consequence of two antecedents: a prior probability and a "likelihood function" derived from a statistical model for the observed data. Bayesian inference computes the posterior probability according to Bayes' theorem:

$P(H\mid E)={\frac {P(E\mid H)\cdot P(H)}{P(E)}},$

where

- H stands for any *hypothesis* whose probability may be affected by data (called *evidence* below). Often there are competing hypotheses, and the task is to determine which is the most probable.
- $P(H)$ , the *prior probability*, is the estimate of the probability of the hypothesis H *before* the data E , the current evidence, is observed.
- E , the *evidence*, corresponds to new data that were not used in computing the prior probability.
- $P(H\mid E)$ , the *posterior probability*, is the probability of H *given* E , i.e., *after* E is observed. This is what we want to know: the probability of a hypothesis *given* the observed evidence.
- $P(E\mid H)$ is the probability of observing E *given* H and is called the *likelihood*. As a function of E with H fixed, it indicates the compatibility of the evidence with the given hypothesis. The likelihood function is a function of the evidence, E , while the posterior probability is a function of the hypothesis, H .
- $P(E)$ is sometimes termed the marginal likelihood or "model evidence". This factor is the same for all possible hypotheses being considered (as is evident from the fact that the hypothesis H does not appear anywhere in the symbol, unlike for all the other factors) and hence does not factor into determining the relative probabilities of different hypotheses.
- $P(E)>0$ (Else one has $0/0$ .)

For different values of H , only the factors $P(H)$ and $P(E\mid H)$ , both in the numerator, affect the value of $P(H\mid E)$  – the posterior probability of a hypothesis is proportional to its prior probability (its inherent likeliness) and the newly acquired likelihood (its compatibility with the new observed evidence).

In cases where $\neg H$ ("not H "), the logical negation of H , is a valid likelihood, Bayes' rule can be rewritten as follows:

${\begin{aligned}P(H\mid E)&={\frac {P(E\mid H)P(H)}{P(E)}}\\\\&={\frac {P(E\mid H)P(H)}{P(E\mid H)P(H)+P(E\mid \neg H)P(\neg H)}}\\\\&={\frac {1}{1+\left({\frac {1}{P(H)}}-1\right){\frac {P(E\mid \neg H)}{P(E\mid H)}}}}\\\end{aligned}}$

because

$P(E)=P(E\mid H)P(H)+P(E\mid \neg H)P(\neg H)$

and

$P(H)+P(\neg H)=1.$

This focuses attention on the term

$\left({\tfrac {1}{P(H)}}-1\right){\tfrac {P(E\mid \neg H)}{P(E\mid H)}}.$

If that term is approximately 1, then the probability of the hypothesis given the evidence, $P(H\mid E)$ , is about ${\tfrac {1}{2}}$ , about 50% likely - equally likely or not likely. If that term is very small, close to zero, then the probability of the hypothesis, given the evidence, $P(H\mid E)$ is close to 1 or the conditional hypothesis is quite likely. If that term is very large, much larger than 1, then the hypothesis, given the evidence, is quite unlikely. If the hypothesis (without consideration of evidence) is unlikely, then $P(H)$ is small (but not necessarily astronomically small) and ${\tfrac {1}{P(H)}}$ is much larger than 1 and this term can be approximated as ${\tfrac {P(E\mid \neg H)}{P(E\mid H)\cdot P(H)}}$ and relevant probabilities can be compared directly to each other.

One quick and easy way to remember the equation would be to use rule of multiplication:

$P(E\cap H)=P(E\mid H)P(H)=P(H\mid E)P(E).$

### Alternatives to Bayesian updating

Bayesian updating is widely used and computationally convenient. However, it is not the only updating rule that might be considered rational.

Ian Hacking noted that traditional "Dutch book" arguments did not specify Bayesian updating: they left open the possibility that non-Bayesian updating rules could avoid Dutch books. Hacking wrote: "And neither the Dutch book argument nor any other in the personalist arsenal of proofs of the probability axioms entails the dynamic assumption. Not one entails Bayesianism. So the personalist requires the dynamic assumption to be Bayesian. It is true that in consistency a personalist could abandon the Bayesian model of learning from experience. Salt could lose its savour."

Indeed, there are non-Bayesian updating rules that also avoid Dutch books (as discussed in the literature on "probability kinematics") following the publication of Richard C. Jeffrey's rule, which applies Bayes' rule to the case where the evidence itself is assigned a probability. The additional hypotheses needed to uniquely require Bayesian updating have been deemed to be substantial, complicated, and unsatisfactory.

## Inference over exclusive and exhaustive possibilities

If evidence is simultaneously used to update belief over a set of exclusive and exhaustive propositions, Bayesian inference may be thought of as acting on this belief distribution as a whole.

### General formulation

Suppose a process is generating independent and identically distributed events $E_{n},\ n=1,2,3,\ldots$ , but the probability distribution is unknown. Let the event space $\Omega$ represent the current state of belief for this process. Each model is represented by event $M_{m}$ . The conditional probabilities $P(E_{n}\mid M_{m})$ are specified to define the models. $P(M_{m})$ is the degree of belief in $M_{m}$ . Before the first inference step, $\{P(M_{m})\}$ is a set of *initial prior probabilities*. These must sum to 1, but are otherwise arbitrary.

Suppose that the process is observed to generate $E\in \{E_{n}\}$ . For each $M\in \{M_{m}\}$ , the prior $P(M)$ is updated to the posterior $P(M\mid E)$ . From Bayes' theorem:

$P(M\mid E)={\frac {P(E\mid M)}{\sum _{m}{P(E\mid M_{m})P(M_{m})}}}\cdot P(M).$

Upon observation of further evidence, this procedure may be repeated.

### Multiple observations

For a sequence of independent and identically distributed observations $\mathbf {E} =(e_{1},\dots ,e_{n})$ , it can be shown by induction that repeated application of the above is equivalent to $P(M\mid \mathbf {E} )={\frac {P(\mathbf {E} \mid M)}{\sum _{m}{P(\mathbf {E} \mid M_{m})P(M_{m})}}}\cdot P(M),$ where $P(\mathbf {E} \mid M)=\prod _{k}{P(e_{k}\mid M)}.$

### Parametric formulation: motivating the formal description

By parameterizing the space of models, the belief in all models may be updated in a single step. The distribution of belief over the model space may then be thought of as a distribution of belief over the parameter space. The distributions in this section are expressed as continuous, represented by probability densities, as this is the usual situation. The technique is, however, equally applicable to discrete distributions.

Let the vector ${\boldsymbol {\theta }}$ span the parameter space. Let the initial prior distribution over ${\boldsymbol {\theta }}$ be $p({\boldsymbol {\theta }}\mid {\boldsymbol {\alpha }})$ , where ${\boldsymbol {\alpha }}$ is a set of parameters to the prior itself, or *hyperparameters*. Let $\mathbf {E} =(e_{1},\dots ,e_{n})$ be a sequence of independent and identically distributed event observations, where all $e_{i}$ are distributed as $p(e\mid {\boldsymbol {\theta }})$ for some ${\boldsymbol {\theta }}$ . Bayes' theorem is applied to find the posterior distribution over ${\boldsymbol {\theta }}$ :

${\begin{aligned}p({\boldsymbol {\theta }}\mid \mathbf {E} ,{\boldsymbol {\alpha }})&={\frac {p(\mathbf {E} \mid {\boldsymbol {\theta }},{\boldsymbol {\alpha }})}{p(\mathbf {E} \mid {\boldsymbol {\alpha }})}}\cdot p({\boldsymbol {\theta }}\mid {\boldsymbol {\alpha }})\\&={\frac {p(\mathbf {E} \mid {\boldsymbol {\theta }},{\boldsymbol {\alpha }})}{\int p(\mathbf {E} \mid {\boldsymbol {\theta }},{\boldsymbol {\alpha }})p({\boldsymbol {\theta }}\mid {\boldsymbol {\alpha }})\,d{\boldsymbol {\theta }}}}\cdot p({\boldsymbol {\theta }}\mid {\boldsymbol {\alpha }}),\end{aligned}}$ where $p(\mathbf {E} \mid {\boldsymbol {\theta }},{\boldsymbol {\alpha }})=\prod _{k}p(e_{k}\mid {\boldsymbol {\theta }}).$

## Formal description

### Definitions

- x , a data point in general. This may be a vector of values.
- $\theta$ , the parameter of the data point's distribution, i.e., $x\sim p(x\mid \theta )$ . This may be a vector of parameters.
- $\alpha$ , the hyperparameter of the parameter distribution, i.e., $\theta \sim p(\theta \mid \alpha )$ . This may be a vector of hyperparameters.
- $\mathbf {X}$ is the sample, a set of n observed data points, i.e., $x_{1},\ldots ,x_{n}$ .
- ${\tilde {x}}$ , a new data point whose distribution is to be predicted.

### Bayesian inference

- The prior distribution is the distribution of the parameter(s) before any data is observed, i.e. $p(\theta \mid \alpha )$ . The prior distribution might not be easily determined; in such a case, one possibility may be to use the Jeffreys prior to obtain a prior distribution before updating it with newer observations.
- The sampling distribution is the distribution of the observed data conditional on its parameters, i.e. $p(\mathbf {X} \mid \theta )$ . This is also termed the likelihood, especially when viewed as a function of the parameter(s), sometimes written $\operatorname {L} (\theta \mid \mathbf {X} )=p(\mathbf {X} \mid \theta )$ .
- The marginal likelihood (sometimes also termed the *evidence*) is the distribution of the observed data marginalized over the parameter(s), i.e. $p(\mathbf {X} \mid \alpha )=\int p(\mathbf {X} \mid \theta )p(\theta \mid \alpha )d\theta .$ It quantifies the agreement between data and expert opinion, in a geometric sense that can be made precise. If the marginal likelihood is 0 then there is no agreement between the data and expert opinion and Bayes' rule cannot be applied.
- The posterior distribution is the distribution of the parameter(s) after taking into account the observed data. This is determined by Bayes' rule, which forms the heart of Bayesian inference:

$p(\theta \mid \mathbf {X} ,\alpha )={\frac {p(\theta ,\mathbf {X} ,\alpha )}{p(\mathbf {X} ,\alpha )}}={\frac {p(\mathbf {X} \mid \theta ,\alpha )p(\theta ,\alpha )}{p(\mathbf {X} \mid \alpha )p(\alpha )}}$ $={\frac {p(\mathbf {X} \mid \theta ,\alpha )p(\theta \mid \alpha )}{p(\mathbf {X} \mid \alpha )}}\propto p(\mathbf {X} \mid \theta ,\alpha )p(\theta \mid \alpha ).$

This is expressed in words as "posterior is proportional to likelihood times prior", or sometimes as "posterior = likelihood times prior, over evidence".

- In practice, for almost all complex Bayesian models used in machine learning, the posterior distribution $p(\theta \mid \mathbf {X} ,\alpha )$ is not obtained in a closed form distribution, mainly because the parameter space for $\theta$ can be very high, or the Bayesian model retains certain hierarchical structure formulated from the observations $\mathbf {X}$ and parameter $\theta$ . In such situations, we need to resort to approximation techniques.
- General case: Let $P_{Y}^{x}$ be the conditional distribution of Y given $X=x$ and let $P_{X}$ be the distribution of X . The joint distribution is then $P_{X,Y}(dx,dy)=P_{Y}^{x}(dy)P_{X}(dx)$ . The conditional distribution $P_{X}^{y}$ of X given $Y=y$ is then determined by

$P_{X}^{y}(A)=E(1_{A}(X)|Y=y)$ Existence and uniqueness of the needed conditional expectation is a consequence of the Radon–Nikodym theorem. This was formulated by Kolmogorov in his famous book from 1933. Kolmogorov underlines the importance of conditional probability by writing "I wish to call attention to ... and especially the theory of conditional probabilities and conditional expectations ..." in the Preface. The Bayes theorem determines the posterior distribution from the prior distribution. Uniqueness requires continuity assumptions. Bayes' theorem can be generalized to include improper prior distributions such as the uniform distribution on the real line. Modern Markov chain Monte Carlo methods have boosted the importance of Bayes' theorem including cases with improper priors.

### Bayesian prediction

- The posterior predictive distribution is the distribution of a new data point, marginalized over the posterior: $p({\tilde {x}}\mid \mathbf {X} ,\alpha )=\int p({\tilde {x}}\mid \theta )p(\theta \mid \mathbf {X} ,\alpha )d\theta$
- The prior predictive distribution is the distribution of a new data point, marginalized over the prior: $p({\tilde {x}}\mid \alpha )=\int p({\tilde {x}}\mid \theta )p(\theta \mid \alpha )d\theta$

Bayesian theory calls for the use of the posterior predictive distribution to do predictive inference, i.e., to predict the distribution of a new, unobserved data point. That is, instead of a fixed point as a prediction, a distribution over possible points is returned. Only this way is the entire posterior distribution of the parameter(s) used. By comparison, prediction in frequentist statistics often involves finding an optimum point estimate of the parameter(s)—e.g., by maximum likelihood or maximum a posteriori estimation (MAP)—and then plugging this estimate into the formula for the distribution of a data point. This has the disadvantage that it does not account for any uncertainty in the value of the parameter, and hence will underestimate the variance of the predictive distribution.

In some instances, frequentist statistics can work around this problem. For example, confidence intervals and prediction intervals in frequentist statistics when constructed from a normal distribution with unknown mean and variance are constructed using a Student's t-distribution. This correctly estimates the variance, due to the facts that (1) the average of normally distributed random variables is also normally distributed, and (2) the predictive distribution of a normally distributed data point with unknown mean and variance, using conjugate or uninformative priors, has a Student's t-distribution. In Bayesian statistics, however, the posterior predictive distribution can always be determined exactly—or at least to an arbitrary level of precision when numerical methods are used.

Both types of predictive distributions have the form of a compound probability distribution (as does the marginal likelihood). In fact, if the prior distribution is a conjugate prior, such that the prior and posterior distributions come from the same family, it can be seen that both prior and posterior predictive distributions also come from the same family of compound distributions. The only difference is that the posterior predictive distribution uses the updated values of the hyperparameters (applying the Bayesian update rules given in the conjugate prior article), while the prior predictive distribution uses the values of the hyperparameters that appear in the prior distribution.

## Mathematical properties

### Interpretation of factor

${\textstyle {\frac {P(E\mid M)}{P(E)}}>1\Rightarrow P(E\mid M)>P(E)}$ . That is, if the model were true, the evidence would be more likely than is predicted by the current state of belief. The reverse applies for a decrease in belief. If the belief does not change, ${\textstyle {\frac {P(E\mid M)}{P(E)}}=1\Rightarrow P(E\mid M)=P(E)}$ . That is, the evidence is independent of the model. If the model were true, the evidence would be exactly as likely as predicted by the current state of belief.

### Cromwell's rule

If $P(M)=0$ then $P(M\mid E)=0$ . If $P(M)=1$ and $P(E)>0$ , then $P(M|E)=1$ . This can be interpreted to mean that hard convictions are insensitive to counter-evidence.

The former follows directly from Bayes' theorem. The latter can be derived by applying the first rule to the event "not M " in place of " M ", yielding "if $1-P(M)=0$ , then $1-P(M\mid E)=0$ ", from which the result immediately follows.

### Asymptotic behaviour of posterior

Consider the behaviour of a belief distribution as it is updated a large number of times with independent and identically distributed trials. For sufficiently nice prior probabilities, the Bernstein-von Mises theorem gives that in the limit of infinite trials, the posterior converges to a Gaussian distribution independent of the initial prior under some conditions firstly outlined and rigorously proven by Joseph L. Doob in 1948, namely if the random variable in consideration has a finite probability space. The more general results were obtained later by the statistician David A. Freedman who published in two seminal research papers in 1963 and 1965 when and under what circumstances the asymptotic behaviour of posterior is guaranteed. His 1963 paper treats, like Doob (1949), the finite case and comes to a satisfactory conclusion. However, if the random variable has an infinite but countable probability space (i.e., corresponding to a die with infinite many faces) the 1965 paper demonstrates that for a dense subset of priors the Bernstein-von Mises theorem is not applicable. In this case there is almost surely no asymptotic convergence. Later in the 1980s and 1990s Freedman and Persi Diaconis continued to work on the case of infinite countable probability spaces. To summarise, there may be insufficient trials to suppress the effects of the initial choice, and especially for large (but finite) systems the convergence might be very slow.

### Conjugate priors

In parameterized form, the prior distribution is often assumed to come from a family of distributions called conjugate priors. The usefulness of a conjugate prior is that the corresponding posterior distribution will be in the same family, and the calculation may be expressed in closed form.

### Estimates of parameters and predictions

It is often desired to use a posterior distribution to estimate a parameter or variable. Several methods of Bayesian estimation select measurements of central tendency from the posterior distribution.

For one-dimensional problems, a unique median exists for practical continuous problems. The posterior median is attractive as a robust estimator.

If there exists a finite mean for the posterior distribution, then the posterior mean is a method of estimation. ${\tilde {\theta }}=\operatorname {E} [\theta ]=\int \theta \,p(\theta \mid \mathbf {X} ,\alpha )\,d\theta$

Taking a value with the greatest probability defines the maximum a posteriori estimation (MAP): $\{\theta _{\text{MAP}}\}\subset \arg \max _{\theta }p(\theta \mid \mathbf {X} ,\alpha ).$

There are examples where no maximum is attained, in which case the set of MAP estimates is empty.

There are other methods of estimation that minimize the posterior risk (expected-posterior loss) with respect to a loss function, and these are of interest to statistical decision theory using the sampling distribution (frequentist statistics).

The posterior predictive distribution of a new observation ${\tilde {x}}$ (that is independent of previous observations) is determined by $p({\tilde {x}}|\mathbf {X} ,\alpha )=\int p({\tilde {x}},\theta \mid \mathbf {X} ,\alpha )\,d\theta$ $=\int p({\tilde {x}}\mid \theta )p(\theta \mid \mathbf {X} ,\alpha )\,d\theta .$

## Examples

### Probability of a hypothesis

| Bowl Cookie | #1 *H*1 | #2 *H*2 |   | Total |
|---|---|---|---|---|
| Plain, *E* | **30** | 20 | **50** |   |
| Choc, ¬*E* | 10 | 20 | 30 |   |
| Total | 40 | 40 | 80 |   |
| *P*(*H*1\|*E*) = 30 / 50 = 0.6 |   |   |   |   |

Suppose there are two full bowls of cookies. Bowl #1 has 10 chocolate chip and 30 plain cookies, while bowl #2 has 20 of each. Fred picks a bowl at random and then picks a cookie at random, which means that there is no reason to believe Fred treats one bowl differently from another, likewise for the cookies. The cookie turns out to be a plain one. As to how probable it is that Fred picked it out of bowl #1, that is an example of a Bayesian inference-approachable problem.

Intuitively, it seems clear that the answer should be more than a half, since there are more plain cookies in bowl #1. The precise answer is given by Bayes' theorem. Let $H_{1}$ correspond to bowl #1, and $H_{2}$ to bowl #2. It is given that the bowls are identical from Fred's point of view, thus $P(H_{1})=P(H_{2})$ , and the two must add up to 1, so both are equal to 0.5. The event E is the observation of a plain cookie. From the contents of the bowls, it is known that $P(E\mid H_{1})=30/40=0.75$ and $P(E\mid H_{2})=20/40=0.5.$ Bayes' formula then yields $P(H_{1}\mid E)={\frac {P(E\mid H_{1})\,P(H_{1})}{P(E\mid H_{1})\,P(H_{1})\;+\;P(E\mid H_{2})\,P(H_{2})}}$ $={\frac {0.75\times 0.5}{0.75\times 0.5+0.5\times 0.5}}=0.6$

*Before* Fred's cookie is observed, the probability of Fred having chosen bowl #1 was the **prior** probability $P(H_{1})=50\%.$ By acknowledging the cookie, Fred's (any observer's) better-informed estimate of $P(H_{1})$ is updated to $P(H_{1}\mid E)=60\%.$

### Making a prediction

An archaeologist is working at a site thought to be from the medieval period, between the 11th century to the 16th century. However, it is uncertain exactly when in this period the site was inhabited. Fragments of pottery are found, some of which are glazed and some of which are decorated. It is expected that if the site were inhabited during the early medieval period, then 1% of the pottery would be glazed and 50% of its area decorated, whereas if it had been inhabited in the late medieval period then 81% would be glazed and 5% of its area decorated. How confident can the archaeologist be in the date of inhabitation as fragments are unearthed?

The degree of belief in the continuous variable C (century) is to be calculated, with the discrete set of events $\{GD,G{\bar {D}},{\bar {G}}D,{\bar {G}}{\bar {D}}\}$ as evidence. The information from the previous paragraph yields $p_{G}(c)=0.01+{\frac {0.80}{5}}(c-11)$ for the glaze probability and $p_{D}(c)=0.5-{\frac {0.45}{5}}(c-11)$ for the decoration probability; their complements being ${\bar {p}}_{G}(c)=1-p_{G}(c),\quad {\bar {p}}_{D}(c)=1-p_{D}(c).$ Assuming linear variation of glaze and decoration with time and that these variables are independent, the probability of each event reads

- $P(E=GD\mid C=c)=p_{G}(c)\,p_{D}(c)$
- $P(E=G{\bar {D}}\mid C=c)=p_{G}(c)\,{\bar {p}}_{D}(c)$
- $P(E={\bar {G}}D\mid C=c)={\bar {p}}_{G}(c)\,p_{D}(c)$
- $P(E={\bar {G}}{\bar {D}}\mid C=c)={\bar {p}}_{G}(c)\,{\bar {p}}_{D}(c)$

When a new fragment of type e is discovered, that means *more information* for the investigation and, through Bayes' theorem, an *updated* Bayesian inference towards an improved degree of belief (or confidence) in the archeologists' estimation. Assuming a uniform prior of ${\textstyle f_{C}(c)=0.2}$ , and that trials are independent and identically distributed,

$f_{C}(c\mid E=e)={\frac {P(E=e\mid C=c)}{P(E=e)}}f_{C}(c)$ $={\frac {P(E=e\mid C=c)}{\int _{11}^{16}{P(E=e\mid C=c)f_{C}(c)dc}}}f_{C}(c).$

A computer simulation of the changing belief as 50 fragments are unearthed is shown on the graph. In the simulation, the site was inhabited around 1420, or $c=15.2$ . By calculating the area under the relevant portion of the graph for 50 trials, the archaeologist can say that there is practically no chance the site was inhabited in the 11th and 12th centuries, about 1% chance that it was inhabited during the 13th century, 63% chance during the 14th century and 36% during the 15th century. The Bernstein-von Mises theorem asserts here the asymptotic convergence to the "true" distribution because the probability space corresponding to the discrete set of events $\{GD,G{\bar {D}},{\bar {G}}D,{\bar {G}}{\bar {D}}\}$ is finite (see above section on asymptotic behaviour of the posterior).

## In frequentist statistics and decision theory

A decision-theoretic justification of the use of Bayesian inference was given by Abraham Wald, who proved that every unique Bayesian procedure is admissible. Conversely, every admissible statistical procedure is either a Bayesian procedure or a limit of Bayesian procedures.

Wald characterized admissible procedures as Bayesian procedures (and limits of Bayesian procedures), making the Bayesian formalism a central technique in such areas of frequentist inference as parameter estimation, hypothesis testing, and computing confidence intervals. For example:

- "Under some conditions, all admissible procedures are either Bayes procedures or limits of Bayes procedures (in various senses). These remarkable results, at least in their original form, are due essentially to Wald. They are useful because the property of being Bayes is easier to analyze than admissibility."
- "In decision theory, a quite general method for proving admissibility consists in exhibiting a procedure as a unique Bayes solution."
- "In the first chapters of this work, prior distributions with finite support and the corresponding Bayes procedures were used to establish some of the main theorems relating to the comparison of experiments. Bayes procedures with respect to more general prior distributions have played a very important role in the development of statistics, including its asymptotic theory." "There are many problems where a glance at posterior distributions, for suitable priors, yields immediately interesting information. Also, this technique can hardly be avoided in sequential analysis."
- "A useful fact is that any Bayes decision rule obtained by taking a proper prior over the whole parameter space must be admissible"
- "An important area of investigation in the development of admissibility ideas has been that of conventional sampling-theory procedures, and many interesting results have been obtained."

### Model selection

Bayesian methodology also plays a role in model selection where the aim is to select one model from a set of competing models that represents most closely the underlying process that generated the observed data. In Bayesian model comparison, the model with the highest posterior probability given the data is selected. The posterior probability of a model depends on the evidence, or marginal likelihood, which reflects the probability that the data is generated by the model, and on the prior belief of the model. When two competing models are a priori considered to be equiprobable, the ratio of their posterior probabilities corresponds to the Bayes factor. Since Bayesian model comparison is aimed on selecting the model with the highest posterior probability, this methodology is also referred to as the maximum a posteriori (MAP) selection rule or the MAP probability rule.

## Probabilistic programming

While conceptually simple, Bayesian methods can be mathematically and numerically challenging. Probabilistic programming languages (PPLs) implement functions to easily build Bayesian models together with efficient automatic inference methods. This helps separate the model building from the inference, allowing practitioners to focus on their specific problems and leaving PPLs to handle the computational details for them.

## Applications

### Statistical data analysis

See the separate Wikipedia entry on Bayesian statistics, specifically the statistical modeling section in that page.

### Computer applications

Bayesian inference has applications in artificial intelligence and expert systems. Bayesian inference techniques have been a fundamental part of computerized pattern recognition techniques since the late 1950s. There is also an ever-growing connection between Bayesian methods and simulation-based Monte Carlo techniques since complex models cannot be processed in closed form by a Bayesian analysis, while a graphical model structure *may* allow for efficient simulation algorithms like the Gibbs sampling and other Metropolis–Hastings algorithm schemes. Recently Bayesian inference has gained popularity among the phylogenetics community for these reasons; a number of applications allow many demographic and evolutionary parameters to be estimated simultaneously.

As applied to statistical classification, Bayesian inference has been used to develop algorithms for identifying e-mail spam. Applications which make use of Bayesian inference for spam filtering include CRM114, DSPAM, Bogofilter, SpamAssassin, SpamBayes, Mozilla, XEAMS, and others. Spam classification is treated in more detail in the article on the naïve Bayes classifier.

Solomonoff's Inductive inference is the theory of prediction based on observations; for example, predicting the next symbol based upon a given series of symbols. The only assumption is that the environment follows some unknown but computable probability distribution. It is a formal inductive framework that combines two well-studied principles of inductive inference: Bayesian statistics and Occam's Razor. Solomonoff's universal prior probability of any prefix *p* of a computable sequence *x* is the sum of the probabilities of all programs (for a universal computer) that compute something starting with *p*. Given some *p* and any computable but unknown probability distribution from which *x* is sampled, the universal prior and Bayes' theorem can be used to predict the yet unseen parts of *x* in optimal fashion.

### Bioinformatics and healthcare applications

Bayesian inference has been applied in different bioinformatics applications, including differential gene expression analysis. Bayesian inference is also used in a general cancer risk model, called CIRI (Continuous Individualized Risk Index), where serial measurements are incorporated to update a Bayesian model which is primarily built from prior knowledge.

### Cosmology and astrophysical applications

The Bayesian approach has been central to recent progress in cosmology and astrophysical applications, and extends to a wide range of astrophysical problems, including the characterisation of exoplanet (such as the fitting of atmosphere for k2-18b), parameter constraints with cosmological data, and calibration in astrophysical experiments.

In cosmology, it is often employed with computational techniques such as Markov chain Monte Carlo(MCMC) and Nested sampling algorithm to analyse complex datasets and navigate high-dimensional parameter space. A notable application is to the Planck 2018 CMB data for parameter inference. The six base cosmological parameters in Lambda-CDM model are not predicted by a theory, but rather fitted from Cosmic microwave background (CMB) data to a chosen model of cosmology (the Lambda-CDM model). The bayesian code for cosmology `cobaya` sets up cosmological runs and interfaces cosmological likelihoods, Boltzmann code, which computes the predicted CMB anisotropies for any given set of cosmological parameters, with MCMC or nested sampler.

This computational framework is not limited to the standard model, it is also essential for testing alternative or extended theories of cosmology, such as theories with early dark energy, or modified gravity theories introducing additional parameters beyond Lambda-CDM. Bayesian model comparison can then be employed to calculate the evidence for competing models, providing a statistical basis to assess whether the data support them over the standard Lambda-CDM.

### In the courtroom

Bayesian inference can be used by jurors to coherently accumulate the evidence for and against a defendant, and to see whether, in totality, it meets their personal threshold for "beyond a reasonable doubt". Bayes' theorem is applied successively to all evidence presented, with the posterior from one stage becoming the prior for the next. The benefit of a Bayesian approach is that it gives the juror an unbiased, rational mechanism for combining evidence. It may be appropriate to explain Bayes' theorem to jurors in odds form, as betting odds are more widely understood than probabilities. Alternatively, a logarithmic approach, replacing multiplication with addition, might be easier for a jury to handle.

If the existence of the crime is not in doubt, only the identity of the culprit, it has been suggested that the prior should be uniform over the qualifying population. For example, if 1,000 people could have committed the crime, the prior probability of guilt would be 1/1000.

The use of Bayes' theorem by jurors is controversial. In the United Kingdom, a defence expert witness explained Bayes' theorem to the jury in *R v Adams*. The jury convicted, but the case went to appeal on the basis that no means of accumulating evidence had been provided for jurors who did not wish to use Bayes' theorem. The Court of Appeal upheld the conviction, but it also gave the opinion that "To introduce Bayes' Theorem, or any similar method, into a criminal trial plunges the jury into inappropriate and unnecessary realms of theory and complexity, deflecting them from their proper task."

Gardner-Medwin argues that the criterion on which a verdict in a criminal trial should be based is *not* the probability of guilt, but rather the *probability of the evidence, given that the defendant is innocent* (akin to a frequentist p-value). He argues that if the posterior probability of guilt is to be computed by Bayes' theorem, the prior probability of guilt must be known. This will depend on the incidence of the crime, which is an unusual piece of evidence to consider in a criminal trial. Consider the following three propositions:

A

– the known facts and testimony could have arisen if the defendant is guilty.

B

– the known facts and testimony could have arisen if the defendant is innocent.

C

– the defendant is guilty.

Gardner-Medwin argues that the jury should believe both *A* and not-*B* in order to convict. *A* and not-*B* implies the truth of *C*, but the reverse is not true. It is possible that *B* and *C* are both true, but in this case he argues that a jury should acquit, even though they know that they will be letting some guilty people go free. See also Lindley's paradox.

### Bayesian epistemology

Bayesian epistemology is a movement that advocates for Bayesian inference as a means of justifying the rules of inductive logic.

Karl Popper and David Miller have rejected the idea of Bayesian rationalism, i.e. using Bayes rule to make epistemological inferences: It is prone to the same vicious circle as any other justificationist epistemology, because it presupposes what it attempts to justify. According to this view, a rational interpretation of Bayesian inference would see it merely as a probabilistic version of falsification, rejecting the belief, commonly held by Bayesians, that high likelihood achieved by a series of Bayesian updates would prove the hypothesis beyond any reasonable doubt, or even with likelihood greater than 0.

### Other

- The scientific method is sometimes interpreted as an application of Bayesian inference. In this view, Bayes' rule guides (or should guide) the updating of probabilities about hypotheses conditional on new observations or experiments. The Bayesian inference has also been applied to treat stochastic scheduling problems with incomplete information by Cai et al. (2009).
- Bayesian search theory is used to search for lost objects.
- Bayesian inference in phylogeny
- Bayesian tool for methylation analysis
- Bayesian approaches to brain function investigate the brain as a Bayesian mechanism.
- Bayesian inference in ecological studies
- Bayesian inference is used to estimate parameters in stochastic chemical kinetic models
- Bayesian inference in econophysics for currency or prediction of trend changes in financial quotations
- Bayesian inference in marketing
- Bayesian inference in motor learning
- Bayesian inference is used in probabilistic numerics to solve numerical problems

## Bayes and Bayesian inference

The problem considered by Bayes in Proposition 9 of his essay, "An Essay Towards Solving a Problem in the Doctrine of Chances", is the posterior distribution for the parameter *a* (the success rate) of the binomial distribution.

## History

The term 'Bayesian' refers to Thomas Bayes (1701–1761), who proved that probabilistic limits could be placed on an unknown event. However, it was Pierre-Simon Laplace (1749–1827) who introduced (as Principle VI) what is now called Bayes' theorem and used it to address problems in celestial mechanics, medical statistics, reliability, and jurisprudence. Early Bayesian inference, which used uniform priors following Laplace's principle of insufficient reason, was called inverse probability (because it infers backwards from observations to parameters, or from effects to causes). After the 1920s, inverse probability was largely supplanted by a collection of methods that came to be called frequentist statistics.

In the 20th century, the ideas of Laplace were further developed in two different directions, giving rise to *objective* and *subjective* currents in Bayesian practice. In the objective (or "non-informative") current, the statistical analysis depends only on the model assumed, the data analyzed, and the method assigning the prior, which differs from one objective Bayesian practitioner to another. In the subjective (or "informative") current, the specification of the prior depends on the belief—the propositions on which the analysis is prepared to act—which can summarize information from experts, previous studies, etc.

In the 1980s, there was a dramatic growth in research and applications of Bayesian methods, mostly attributed to the discovery of Markov chain Monte Carlo methods, which removed many of the computational problems, and an increasing interest in nonstandard, complex applications. Despite growth of Bayesian research, most undergraduate teaching is still based on frequentist statistics. Nonetheless, Bayesian methods are widely accepted and used, such as for example in the field of machine learning.
