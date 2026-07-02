---
title: "Expectation–maximization algorithm"
source: https://en.wikipedia.org/wiki/Expectation–maximization_algorithm
domain: expectation-maximization
license: CC-BY-SA-4.0
tags: expectation maximization algorithm, gaussian mixture model, maximum likelihood estimation, latent variable
fetched: 2026-07-02
---

# Expectation–maximization algorithm

In statistics, an **expectation–maximization** (**EM**) **algorithm** is an iterative method to find (local) maximum likelihood or maximum a posteriori (MAP) estimates of parameters in statistical models, where the model depends on unobserved latent variables. The EM iteration alternates between performing an expectation (E) step, which creates a function for the expectation of the log-likelihood evaluated using the current estimate for the parameters, and a maximization (M) step, which computes parameters maximizing the expected log-likelihood found on the E step. These parameter-estimates are then used to determine the distribution of the latent variables in the next E step. It can be used, for example, to estimate a mixture of gaussians, or to solve the multiple linear regression problem.

## History

The EM algorithm was explained and given its name in a classic 1977 paper by Arthur Dempster, Nan Laird, and Donald Rubin. They pointed out that the method had been "proposed many times in special circumstances" by earlier authors. One of the earliest is the gene-counting method for estimating allele frequencies by Cedric Smith. Another was proposed by H.O. Hartley in 1958, and Hartley and Hocking in 1977, from which many of the ideas in the Dempster–Laird–Rubin paper originated. Another one by S.K Ng, Thriyambakam Krishnan and G.J McLachlan in 1977. Hartley's ideas can be broadened to any grouped discrete distribution. A very detailed treatment of the EM method for exponential families was published by Rolf Sundberg in his thesis and several papers, following his collaboration with Per Martin-Löf and Anders Martin-Löf. The Dempster–Laird–Rubin paper in 1977 generalized the method and sketched a convergence analysis for a wider class of problems. The Dempster–Laird–Rubin paper established the EM method as an important tool of statistical analysis. See also Meng and van Dyk (1997).

The convergence analysis of the Dempster–Laird–Rubin algorithm was flawed and a correct convergence analysis was published by C. F. Jeff Wu in 1983. Wu's proof established the EM method's convergence also outside of the exponential family, as claimed by Dempster–Laird–Rubin.

## Introduction

The EM algorithm is used to find (local) maximum likelihood parameters of a statistical model in cases where the equations cannot be solved directly. Typically these models involve latent variables in addition to unknown parameters and known data observations. That is, either missing values exist among the data, or the model can be formulated more simply by assuming the existence of further unobserved data points. For example, a mixture model can be described more simply by assuming that each observed data point has a corresponding unobserved data point, or latent variable, specifying the mixture component to which each data point belongs.

Finding a maximum likelihood solution typically requires taking the derivatives of the likelihood function with respect to all the unknown values, the parameters and the latent variables, and simultaneously solving the resulting equations. In statistical models with latent variables, this is usually impossible. Instead, the result is typically a set of interlocking equations in which the solution to the parameters requires the values of the latent variables and vice versa, but substituting one set of equations into the other produces an unsolvable equation.

The EM algorithm proceeds from the observation that there is a way to solve these two sets of equations numerically. One can simply pick arbitrary values for one of the two sets of unknowns, use them to estimate the second set, then use these new values to find a better estimate of the first set, and then keep alternating between the two until the resulting values both converge to fixed points. It's not obvious that this will work, but it can be proven in this context. Additionally, it can be proven that the derivative of the likelihood is (arbitrarily close to) zero at that point, which in turn means that the point is either a local maximum or a saddle point. In general, multiple maxima may occur, with no guarantee that the global maximum will be found. Some likelihoods also have singularities in them, i.e., nonsensical maxima. For example, one of the *solutions* that may be found by EM in a mixture model involves setting one of the components to have zero variance and the mean parameter for the same component to be equal to one of the data points.

## Description

### The symbols

Given the statistical model which generates a set $\mathbf {X}$ of observed data, a set of unobserved latent data or missing values $\mathbf {Z}$ , and a vector of unknown parameters ${\boldsymbol {\theta }}$ , along with a likelihood function $L({\boldsymbol {\theta }};\mathbf {X} ,\mathbf {Z} )=p(\mathbf {X} ,\mathbf {Z} \mid {\boldsymbol {\theta }})$ , the maximum likelihood estimate (MLE) of the unknown parameters is determined by maximizing the marginal likelihood of the observed data

${\begin{aligned}L({\boldsymbol {\theta }};\mathbf {X} )=p(\mathbf {X} \mid {\boldsymbol {\theta }})&=\int p(\mathbf {X} ,\mathbf {Z} \mid {\boldsymbol {\theta }})\,d\mathbf {Z} \\&=\int p(\mathbf {X} \mid \mathbf {Z} ,{\boldsymbol {\theta }})p(\mathbf {Z} \mid {\boldsymbol {\theta }})\,d\mathbf {Z} \end{aligned}}$

However, this quantity is often intractable since $\mathbf {Z}$ is unobserved and the distribution of $\mathbf {Z}$ is unknown before attaining ${\boldsymbol {\theta }}$ .

### The EM algorithm

The EM algorithm seeks to find the maximum likelihood estimate of the marginal likelihood by iteratively applying these two steps:

Expectation step (E step)

: Define

$Q({\boldsymbol {\theta }}\mid {\boldsymbol {\theta }}^{(t)})$

as the

expected value

of the log

likelihood function

of

⁠

${\boldsymbol {\theta }}$

⁠

, with respect to the current

conditional distribution

of

$\mathbf {Z}$

given

$\mathbf {X}$

and the current estimates of the parameters

⁠

${\boldsymbol {\theta }}^{(t)}$

⁠

:

$Q({\boldsymbol {\theta }}\mid {\boldsymbol {\theta }}^{(t)})=\operatorname {E} _{\mathbf {Z} \sim p(\cdot |\mathbf {X} ,{\boldsymbol {\theta }}^{(t)})}\left[\log p(\mathbf {X} ,\mathbf {Z} |{\boldsymbol {\theta }})\right]:=\int \log p(\mathbf {X} ,\mathbf {Z} |{\boldsymbol {\theta }})\,p(\mathbf {Z} |\mathbf {X} ,{\boldsymbol {\theta }}^{(t)})\,d\mathbf {Z} \,$

Maximization step (M step)

: Find the parameters that maximize this quantity:

${\boldsymbol {\theta }}^{(t+1)}=\mathop {\arg \max } _{\boldsymbol {\theta }}Q({\boldsymbol {\theta }}\mid {\boldsymbol {\theta }}^{(t)})\,$

More succinctly, we can write it as one equation: ${\boldsymbol {\theta }}^{(t+1)}=\mathop {\arg \max } _{\boldsymbol {\theta }}\operatorname {E} _{\mathbf {Z} \sim p(\cdot |\mathbf {X} ,{\boldsymbol {\theta }}^{(t)})}\left[\log p(\mathbf {X} ,\mathbf {Z} |{\boldsymbol {\theta }})\right]\,$

### Interpretation of the variables

The typical models to which EM is applied use $\mathbf {Z}$ as a latent variable indicating membership in one of a set of groups:

1. The observed data points $\mathbf {X}$ may be discrete (taking values in a finite or countably infinite set) or continuous (taking values in an uncountably infinite set). Associated with each data point may be a vector of observations.
2. The missing values (aka latent variables) $\mathbf {Z}$ are discrete, drawn from a fixed number of values, and with one latent variable per observed unit.
3. The parameters are continuous, and are of two kinds: Parameters that are associated with all data points, and those associated with a specific value of a latent variable (i.e., associated with all data points whose corresponding latent variable has that value).

However, it is possible to apply EM to other sorts of models.

The motivation is as follows. If the value of the parameters ${\boldsymbol {\theta }}$ is known, usually the value of the latent variables $\mathbf {Z}$ can be found by maximizing the log-likelihood over all possible values of $\mathbf {Z}$ , either simply by iterating over $\mathbf {Z}$ or through an algorithm such as the Viterbi algorithm for hidden Markov models. Conversely, if we know the value of the latent variables $\mathbf {Z}$ , we can find an estimate of the parameters ${\boldsymbol {\theta }}$ fairly easily, typically by simply grouping the observed data points according to the value of the associated latent variable and averaging the values, or some function of the values, of the points in each group. This suggests an iterative algorithm, in the case where both ${\boldsymbol {\theta }}$ and $\mathbf {Z}$ are unknown:

1. First, initialize the parameters ${\boldsymbol {\theta }}$ to some random values.
2. Compute the probability of each possible value of ⁠ $\mathbf {Z}$ ⁠, given ⁠ ${\boldsymbol {\theta }}$ ⁠.
3. Then, use the just-computed values of $\mathbf {Z}$ to compute a better estimate for the parameters ⁠ ${\boldsymbol {\theta }}$ ⁠.
4. Iterate steps 2 and 3 until convergence.

The algorithm as just described monotonically approaches a local minimum of the cost function.

## Properties

Although an EM iteration does increase the observed data (i.e., marginal) likelihood function, no guarantee exists that the sequence converges to a maximum likelihood estimator. For multimodal distributions, this means that an EM algorithm may converge to a local maximum of the observed data likelihood function, depending on starting values. A variety of heuristic or metaheuristic approaches exist to escape a local maximum, such as random-restart hill climbing (starting with several different random initial estimates ⁠ ${\boldsymbol {\theta }}^{(t)}$ ⁠), or applying simulated annealing methods.

EM is especially useful when the likelihood is an exponential family, see Sundberg (2019, Ch. 8) for a comprehensive treatment: the E step becomes the sum of expectations of sufficient statistics, and the M step involves maximizing a linear function. In such a case, it is usually possible to derive closed-form expression updates for each step, using the Sundberg formula (proved and published by Rolf Sundberg, based on unpublished results of Per Martin-Löf and Anders Martin-Löf).

The EM method was modified to compute maximum a posteriori (MAP) estimates for Bayesian inference in the original paper by Dempster, Laird, and Rubin.

Other methods exist to find maximum likelihood estimates, such as gradient descent, conjugate gradient, or variants of the Gauss–Newton algorithm. Unlike EM, such methods typically require the evaluation of first and/or second derivatives of the likelihood function.

## Proof of correctness

Expectation-Maximization works to improve $Q({\boldsymbol {\theta }}\mid {\boldsymbol {\theta }}^{(t)})$ rather than directly improving $\log p(\mathbf {X} \mid {\boldsymbol {\theta }})$ . Here it is shown that improvements to the former imply improvements to the latter.

For any $\mathbf {Z}$ with non-zero probability ⁠ $p(\mathbf {Z} \mid \mathbf {X} ,{\boldsymbol {\theta }})$ ⁠, we can write $\log p(\mathbf {X} \mid {\boldsymbol {\theta }})=\log p(\mathbf {X} ,\mathbf {Z} \mid {\boldsymbol {\theta }})-\log p(\mathbf {Z} \mid \mathbf {X} ,{\boldsymbol {\theta }}).$ We take the expectation over possible values of the unknown data $\mathbf {Z}$ under the current parameter estimate $\theta ^{(t)}$ by multiplying both sides by $p(\mathbf {Z} \mid \mathbf {X} ,{\boldsymbol {\theta }}^{(t)})$ and summing (or integrating) over $\mathbf {Z}$ . The left-hand side is the expectation of a constant, so we get: ${\begin{aligned}\log p(\mathbf {X} \mid {\boldsymbol {\theta }})&=\sum _{\mathbf {Z} }p{\left(\mathbf {Z} \mid \mathbf {X} ,{\boldsymbol {\theta }}^{(t)}\right)}\log p(\mathbf {X} ,\mathbf {Z} \mid {\boldsymbol {\theta }})-\sum _{\mathbf {Z} }p{\left(\mathbf {Z} \mid \mathbf {X} ,{\boldsymbol {\theta }}^{(t)}\right)}\log p(\mathbf {Z} \mid \mathbf {X} ,{\boldsymbol {\theta }})\\&=Q({\boldsymbol {\theta }}\mid {\boldsymbol {\theta }}^{(t)})+H({\boldsymbol {\theta }}\mid {\boldsymbol {\theta }}^{(t)}),\end{aligned}}$ where $H({\boldsymbol {\theta }}\mid {\boldsymbol {\theta }}^{(t)})$ is defined by the negated sum it is replacing. This last equation holds for every value of ${\boldsymbol {\theta }}$ including ${\boldsymbol {\theta }}={\boldsymbol {\theta }}^{(t)}$ , $\log p(\mathbf {X} \mid {\boldsymbol {\theta }}^{(t)})=Q({\boldsymbol {\theta }}^{(t)}\mid {\boldsymbol {\theta }}^{(t)})+H({\boldsymbol {\theta }}^{(t)}\mid {\boldsymbol {\theta }}^{(t)}),$ and subtracting this last equation from the previous equation gives $\log p(\mathbf {X} \mid {\boldsymbol {\theta }})-\log p(\mathbf {X} \mid {\boldsymbol {\theta }}^{(t)})=Q({\boldsymbol {\theta }}\mid {\boldsymbol {\theta }}^{(t)})-Q({\boldsymbol {\theta }}^{(t)}\mid {\boldsymbol {\theta }}^{(t)})+H({\boldsymbol {\theta }}\mid {\boldsymbol {\theta }}^{(t)})-H({\boldsymbol {\theta }}^{(t)}\mid {\boldsymbol {\theta }}^{(t)}).$ However, Gibbs' inequality tells us that $H({\boldsymbol {\theta }}\mid {\boldsymbol {\theta }}^{(t)})\geq H({\boldsymbol {\theta }}^{(t)}\mid {\boldsymbol {\theta }}^{(t)})$ , so we can conclude that $\log p(\mathbf {X} \mid {\boldsymbol {\theta }})-\log p(\mathbf {X} \mid {\boldsymbol {\theta }}^{(t)})\geq Q({\boldsymbol {\theta }}\mid {\boldsymbol {\theta }}^{(t)})-Q({\boldsymbol {\theta }}^{(t)}\mid {\boldsymbol {\theta }}^{(t)}).$ In words, choosing ${\boldsymbol {\theta }}$ to improve $Q({\boldsymbol {\theta }}\mid {\boldsymbol {\theta }}^{(t)})$ causes $\log p(\mathbf {X} \mid {\boldsymbol {\theta }})$ to improve at least as much.

## As a maximization–maximization procedure

The EM algorithm can be viewed as two alternating maximization steps, that is, as an example of coordinate descent. Consider the function: $F(q,\theta ):=\operatorname {E} _{q}[\log L(\theta ;x,Z)]+H(q),$ where q is an arbitrary probability distribution over the unobserved data z and *H*(*q*) is the entropy of the distribution q. This function can be written as $F(q,\theta )=-D_{\mathrm {KL} }{\big (}q\parallel p_{Z\mid X}(\cdot \mid x;\theta ){\big )}+\log L(\theta ;x),$ where $p_{Z\mid X}(\cdot \mid x;\theta )$ is the conditional distribution of the unobserved data given the observed data x and $D_{KL}$ is the Kullback–Leibler divergence.

Then the steps in the EM algorithm may be viewed as:

- *Expectation step*: Choose q to maximize ⁠ F ⁠: $q^{(t)}=\mathop {\arg \max } _{q}F{\left(q,\theta ^{(t)}\right)}$
- *Maximization step*: Choose $\theta$ to maximize ⁠ F ⁠: $\theta ^{(t+1)}=\mathop {\arg \max } _{\theta }F{\left(q^{(t)},\theta \right)}$

## Applications

- EM is frequently used for parameter estimation of mixed models, notably in quantitative genetics.
- In psychometrics, EM is an important tool for estimating item parameters and latent abilities of item response theory models.
- With the ability to deal with missing data and observe unidentified variables, EM is becoming a useful tool to price and manage risk of a portfolio.
- The EM algorithm (and its faster variant ordered subset expectation maximization) is also widely used in medical image reconstruction, especially in positron emission tomography, single-photon emission computed tomography, and x-ray computed tomography. See below for other faster variants of EM.
- In structural engineering, the Structural Identification using Expectation Maximization (STRIDE) algorithm is an output-only method for identifying natural vibration properties of a structural system using sensor data (see Operational Modal Analysis).
- EM is also used for data clustering. In natural language processing, two prominent instances of the algorithm are the Baum–Welch algorithm for hidden Markov models, and the inside-outside algorithm for unsupervised induction of probabilistic context-free grammars.
- In the analysis of intertrade waiting times the EM algorithm has proved to be very useful.

## Filtering and smoothing EM algorithms

A Kalman filter is typically used for on-line state estimation and a minimum-variance smoother may be employed for off-line or batch state estimation. However, these minimum-variance solutions require estimates of the state-space model parameters. EM algorithms can be used for solving joint state and parameter estimation problems.

Filtering and smoothing EM algorithms arise by repeating this two-step procedure:

**E-step**

Operate a Kalman filter or a minimum-variance smoother designed with current parameter estimates to obtain updated state estimates.

**M-step**

Use the filtered or smoothed state estimates within maximum-likelihood calculations to obtain updated parameter estimates.

Suppose that a Kalman filter or minimum-variance smoother operates on measurements of a single-input-single-output system that possess additive white noise. An updated measurement noise variance estimate can be obtained from the maximum likelihood calculation ${\widehat {\sigma }}_{v}^{2}={\frac {1}{N}}\sum _{k=1}^{N}{(z_{k}-{\widehat {x}}_{k})}^{2},$

where ${\widehat {x}}_{k}$ are scalar output estimates calculated by a filter or a smoother from N scalar measurements $z_{k}$ . The above update can also be applied to updating a Poisson measurement noise intensity. Similarly, for a first-order auto-regressive process, an updated process noise variance estimate can be calculated by ${\widehat {\sigma }}_{w}^{2}={\frac {1}{N}}\sum _{k=1}^{N}{({\widehat {x}}_{k+1}-{\widehat {F}}{\widehat {x}}_{k})}^{2},$

where ${\widehat {x}}_{k}$ and ${\widehat {x}}_{k+1}$ are scalar state estimates calculated by a filter or a smoother. The updated model coefficient estimate is obtained via ${\widehat {F}}={\frac {\sum \limits _{k=1}^{N}{\left({\widehat {x}}_{k+1}-{\widehat {F}}{\widehat {x}}_{k}\right)}^{2}}{\sum \limits _{k=1}^{N}{\widehat {x}}_{k}^{2}}}.$

The convergence of parameter estimates such as those above are well studied.

## Variants

A number of methods have been proposed to accelerate the sometimes slow convergence of the EM algorithm, such as those using conjugate gradient and modified Newton's methods (Newton–Raphson). Also, EM can be used with constrained estimation methods.

*Parameter-expanded expectation maximization (PX-EM)* algorithm often provides speed up by "us[ing] a `covariance adjustment' to correct the analysis of the M step, capitalising on extra information captured in the imputed complete data".

*Expectation conditional maximization (ECM)* replaces each M step with a sequence of conditional maximization (CM) steps in which each parameter *θ**i* is maximized individually, conditionally on the other parameters remaining fixed. Itself can be extended into the *Expectation conditional maximization either (ECME)* algorithm.

This idea is further extended in *generalized expectation maximization (GEM)* algorithm, in which is sought only an increase in the objective function F for both the E step and M step as described in the As a maximization–maximization procedure section. GEM is further developed in a distributed environment and shows promising results.

It is also possible to consider the EM algorithm as a subclass of the **MM** (Majorize/Minimize or Minorize/Maximize, depending on context) algorithm, and therefore use any machinery developed in the more general case.

### α-EM algorithm

The Q-function used in the EM algorithm is based on the log likelihood. Therefore, it is regarded as the log-EM algorithm. The use of the log likelihood can be generalized to that of the α-log likelihood ratio. Then, the α-log likelihood ratio of the observed data can be exactly expressed as equality by using the Q-function of the α-log likelihood ratio and the α-divergence. Obtaining this Q-function is a generalized E step. Its maximization is a generalized M step. This pair is called the α-EM algorithm which contains the log-EM algorithm as its subclass. Thus, the α-EM algorithm by Yasuo Matsuyama is an exact generalization of the log-EM algorithm. No computation of gradient or Hessian matrix is needed. The α-EM shows faster convergence than the log-EM algorithm by choosing an appropriate α. The α-EM algorithm leads to a faster version of the Hidden Markov model estimation algorithm α-HMM.

## Relation to variational Bayes methods

EM is a partially non-Bayesian, maximum likelihood method. Its final result gives a probability distribution over the latent variables (in the Bayesian style) together with a point estimate for θ (either a maximum likelihood estimate or a posterior mode). A fully Bayesian version of this may be wanted, giving a probability distribution over θ and the latent variables. The Bayesian approach to inference is simply to treat θ as another latent variable. In this paradigm, the distinction between the E and M steps disappears. If using the factorized Q approximation as described above (variational Bayes), solving can iterate over each latent variable (now including θ) and optimize them one at a time. Now, k steps per iteration are needed, where k is the number of latent variables. For graphical models this is easy to do as each variable's new Q depends only on its Markov blanket, so local message passing can be used for efficient inference.

## Geometric interpretation

In information geometry, the E step and the M step are interpreted as projections under dual affine connections, called the e-connection and the m-connection; the Kullback–Leibler divergence can also be understood in these terms.

## Examples

### Gaussian mixture

Let $\mathbf {x} =(\mathbf {x} _{1},\mathbf {x} _{2},\ldots ,\mathbf {x} _{n})$ be a sample of n independent observations from a mixture of two multivariate normal distributions of dimension d , and let $\mathbf {z} =(z_{1},z_{2},\ldots ,z_{n})$ be the latent variables that determine the component from which the observation originates. ${\begin{aligned}X_{i}\mid (Z_{i}=1)&\sim {\mathcal {N}}_{d}({\boldsymbol {\mu }}_{1},\Sigma _{1}),\\X_{i}\mid (Z_{i}=2)&\sim {\mathcal {N}}_{d}({\boldsymbol {\mu }}_{2},\Sigma _{2}),\end{aligned}}$ where $\operatorname {P} (Z_{i}=1)=\tau _{1}\,\quad {\text{and}}\quad \operatorname {P} (Z_{i}=2)=\tau _{2}=1-\tau _{1}.$

The aim is to estimate the unknown parameters representing the *mixing* value between the Gaussians and the means and covariances of each: $\theta ={\big (}{\boldsymbol {\tau }},{\boldsymbol {\mu }}_{1},{\boldsymbol {\mu }}_{2},\Sigma _{1},\Sigma _{2}{\big )},$ where the incomplete-data likelihood function is $L(\theta ;\mathbf {x} )=\prod _{i=1}^{n}\sum _{j=1}^{2}\tau _{j}\ f(\mathbf {x} _{i};{\boldsymbol {\mu }}_{j},\Sigma _{j}),$

and the complete-data likelihood function is ${\begin{aligned}L(\theta ;\mathbf {x} ,\mathbf {z} )&=p(\mathbf {x} ,\mathbf {z} \mid \theta )\\&=\prod _{i=1}^{n}\prod _{j=1}^{2}\left[f(\mathbf {x} _{i};{\boldsymbol {\mu }}_{j},\Sigma _{j})\tau _{j}\right]^{\mathbb {I} (z_{i}=j)},\end{aligned}}$

or

$\log L(\theta ;\mathbf {x} ,\mathbf {z} )=\sum _{i=1}^{n}\sum _{j=1}^{2}\mathbb {I} (z_{i}=j)\left[\log \tau _{j}-{\tfrac {1}{2}}\log |\Sigma _{j}|-{\tfrac {1}{2}}(\mathbf {x} _{i}-{\boldsymbol {\mu }}_{j})^{\top }\Sigma _{j}^{-1}(\mathbf {x} _{i}-{\boldsymbol {\mu }}_{j})-{\tfrac {d}{2}}\log(2\pi )\right],$

where $\mathbb {I}$ is an indicator function and f is the probability density function of a multivariate normal.

In the last equality, for each i, one indicator $\mathbb {I} (z_{i}=j)$ is equal to zero, and one indicator is equal to one. The inner sum thus reduces to one term.

#### E step

Given our current estimate of the parameters *θ*(*t*), the conditional distribution of the *Z**i* is determined by Bayes' theorem to be the proportional height of the normal density weighted by τ: ${\begin{aligned}T_{j,i}^{(t)}:={}&\operatorname {P} (Z_{i}=j\mid X_{i}=\mathbf {x} _{i};\theta ^{(t)})\\={}&{\frac {\tau _{j}^{(t)}\,f{\left(\mathbf {x} _{i};{\boldsymbol {\mu }}_{j}^{(t)},\Sigma _{j}^{(t)}\right)}}{\tau _{1}^{(t)}\,f{\left(\mathbf {x} _{i};{\boldsymbol {\mu }}_{1}^{(t)},\Sigma _{1}^{(t)}\right)}+\tau _{2}^{(t)}\,f{\left(\mathbf {x} _{i};{\boldsymbol {\mu }}_{2}^{(t)},\Sigma _{2}^{(t)}\right)}}}.\end{aligned}}$

These are called the "membership probabilities", which are normally considered the output of the E step (although this is not the Q function of below).

This E step corresponds with setting up this function for Q: ${\begin{aligned}Q(\theta \mid \theta ^{(t)})&=\operatorname {E} _{\mathbf {Z} \mid \mathbf {X} =\mathbf {x} ;\mathbf {\theta } ^{(t)}}\left[\log L(\theta ;\mathbf {x} ,\mathbf {Z} )\right]\\&=\operatorname {E} _{\mathbf {Z} \mid \mathbf {X} =\mathbf {x} ;\mathbf {\theta } ^{(t)}}\left[\log \prod _{i=1}^{n}L(\theta ;\mathbf {x} _{i},Z_{i})\right]\\&=\operatorname {E} _{\mathbf {Z} \mid \mathbf {X} =\mathbf {x} ;\mathbf {\theta } ^{(t)}}\left[\sum _{i=1}^{n}\log L(\theta ;\mathbf {x} _{i},Z_{i})\right]\\&=\sum _{i=1}^{n}\operatorname {E} _{Z_{i}\mid X_{i}=x_{i};\mathbf {\theta } ^{(t)}}\left[\log L(\theta ;\mathbf {x} _{i},Z_{i})\right]\\&=\sum _{i=1}^{n}\sum _{j=1}^{2}P(Z_{i}=j\mid X_{i}=\mathbf {x} _{i};\theta ^{(t)})\log L(\theta ;\mathbf {x} _{i},j)\\&=\sum _{i=1}^{n}\sum _{j=1}^{2}T_{j,i}^{(t)}\left[\log \tau _{j}-{\tfrac {1}{2}}\log |\Sigma _{j}|-{\tfrac {1}{2}}(\mathbf {x} _{i}-{\boldsymbol {\mu }}_{j})^{\top }\Sigma _{j}^{-1}(\mathbf {x} _{i}-{\boldsymbol {\mu }}_{j})-{\tfrac {d}{2}}\log(2\pi )\right].\end{aligned}}$ The expectation of $\log L(\theta ;\mathbf {x} _{i},Z_{i})$ inside the sum is taken with respect to the probability density function $P(Z_{i}\mid X_{i}=\mathbf {x} _{i};\theta ^{(t)})$ , which might be different for each $\mathbf {x} _{i}$ of the training set. Everything in the E step is known before the step is taken except $T_{j,i}$ , which is computed according to the equation at the beginning of the E step section.

This full conditional expectation does not need to be calculated in one step, because τ and ***μ***/**Σ** appear in separate linear terms and can thus be maximized independently.

#### M step

$Q(\theta \mid \theta ^{(t)})$ being quadratic in form means that determining the maximizing values of $\theta$ is relatively straightforward. Also, $\tau$ , $({\boldsymbol {\mu }}_{1},\Sigma _{1})$ and $({\boldsymbol {\mu }}_{2},\Sigma _{2})$ may all be maximized independently since they all appear in separate linear terms.

To begin, consider $\tau$ , which has the constraint $\tau _{1}+\tau _{2}=1$ : ${\begin{aligned}{\boldsymbol {\tau }}^{(t+1)}&=\mathop {\arg \max } _{\boldsymbol {\tau }}Q{\left(\theta \mid \theta ^{(t)}\right)}\\&=\mathop {\arg \max } _{\boldsymbol {\tau }}\left\{\left[\sum _{i=1}^{n}T_{1,i}^{(t)}\right]\log \tau _{1}+\left[\sum _{i=1}^{n}T_{2,i}^{(t)}\right]\log \tau _{2}\right\}.\end{aligned}}$ This has the same form as the maximum likelihood estimate for the binomial distribution, so $\tau _{j}^{(t+1)}={\frac {\sum \limits _{i=1}^{n}T_{j,i}^{(t)}}{\sum \limits _{i=1}^{n}\left(T_{1,i}^{(t)}+T_{2,i}^{(t)}\right)}}={\frac {1}{n}}\sum _{i=1}^{n}T_{j,i}^{(t)}.$

For the next estimates of $({\boldsymbol {\mu }}_{1},\Sigma _{1})$ : ${\begin{aligned}\left({\boldsymbol {\mu }}_{1}^{(t+1)},\Sigma _{1}^{(t+1)}\right)&=\mathop {\arg \max } _{{\boldsymbol {\mu }}_{1},\Sigma _{1}}Q{\left(\theta \mid \theta ^{(t)}\right)}\\&=\mathop {\arg \max } _{{\boldsymbol {\mu }}_{1},\Sigma _{1}}\sum _{i=1}^{n}T_{1,i}^{(t)}\left\{-{\tfrac {1}{2}}\log \left|\Sigma _{1}\right|-{\tfrac {1}{2}}\left(\mathbf {x} _{i}-{\boldsymbol {\mu }}_{1}\right)^{\top }\Sigma _{1}^{-1}\left(\mathbf {x} _{i}-{\boldsymbol {\mu }}_{1}\right)\right\}.\end{aligned}}$ This has the same form as a weighted maximum likelihood estimate for a normal distribution, so ${\begin{aligned}{\boldsymbol {\mu }}_{1}^{(t+1)}&={\frac {\sum \limits _{i=1}^{n}T_{1,i}^{(t)}\mathbf {x} _{i}}{\sum \limits _{i=1}^{n}T_{1,i}^{(t)}}},\\[1ex]\Sigma _{1}^{(t+1)}&={\frac {\sum \limits _{i=1}^{n}T_{1,i}^{(t)}\left(\mathbf {x} _{i}-{\boldsymbol {\mu }}_{1}^{(t+1)}\right)\left(\mathbf {x} _{i}-{\boldsymbol {\mu }}_{1}^{(t+1)}\right)^{\top }}{\sum \limits _{i=1}^{n}T_{1,i}^{(t)}}}\end{aligned}}$ and, by symmetry, ${\begin{aligned}{\boldsymbol {\mu }}_{2}^{(t+1)}&={\frac {\sum \limits _{i=1}^{n}T_{2,i}^{(t)}\mathbf {x} _{i}}{\sum \limits _{i=1}^{n}T_{2,i}^{(t)}}},\\[1ex]\Sigma _{2}^{(t+1)}&={\frac {\sum \limits _{i=1}^{n}T_{2,i}^{(t)}\left(\mathbf {x} _{i}-{\boldsymbol {\mu }}_{2}^{(t+1)}\right)\left(\mathbf {x} _{i}-{\boldsymbol {\mu }}_{2}^{(t+1)}\right)^{\top }}{\sum \limits _{i=1}^{n}T_{2,i}^{(t)}}}.\end{aligned}}$

#### Termination

Conclude the iterative process if the expectation update is sufficiently small. That is, if $\left|\operatorname {E} _{Z\mid \theta ^{(t)},\mathbf {x} }[\log L(\theta ^{(t)};\mathbf {x} ,\mathbf {Z} )]-\operatorname {E} _{Z\mid \theta ^{(t-1)},\mathbf {x} }[\log L(\theta ^{(t-1)};\mathbf {x} ,\mathbf {Z} )]\right|\leq \varepsilon$ for $\varepsilon$ below some preset threshold.

#### Generalization

The algorithm illustrated above can be generalized for mixtures of more than two multivariate normal distributions.

### Truncated and censored regression

The EM algorithm has been implemented in the case where an underlying linear regression model exists explaining the variation of some quantity, but where the values actually observed are censored or truncated versions of those represented in the model. Special cases of this model include censored or truncated observations from one normal distribution.

## Alternatives

EM typically converges to a local optimum, not necessarily the global optimum, with no bound on the convergence rate in general. It is possible that it can be arbitrarily poor in high dimensions and there can be an exponential number of local optima. Hence, a need exists for alternative methods for guaranteed learning, especially in the high-dimensional setting. Alternatives to EM exist with better guarantees for consistency, which are termed *moment-based approaches* or the so-called *spectral techniques*. Moment-based approaches to learning the parameters of a probabilistic model enjoy guarantees such as global convergence under certain conditions unlike EM which is often plagued by the issue of getting stuck in local optima. Algorithms with guarantees for learning can be derived for a number of important models such as mixture models, HMMs etc. For these spectral methods, no spurious local optima occur, and the true parameters can be consistently estimated under some regularity conditions.
