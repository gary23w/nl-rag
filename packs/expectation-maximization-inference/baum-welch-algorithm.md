---
title: "Baum–Welch algorithm"
source: https://en.wikipedia.org/wiki/Baum–Welch_algorithm
domain: expectation-maximization-inference
license: CC-BY-SA-4.0
tags: expectation maximization, baum welch algorithm, gaussian mixture fitting, latent variable inference
fetched: 2026-07-02
---

# Baum–Welch algorithm

In electrical engineering, statistical computing and bioinformatics, the **Baum–Welch algorithm** is a special case of the expectation–maximization algorithm used to find the unknown parameters of a hidden Markov model (HMM). It makes use of the forward-backward algorithm to compute the statistics for the expectation step. The Baum–Welch algorithm, the primary method for inference in hidden Markov models, is numerically unstable due to its recursive calculation of joint probabilities. As the number of variables grows, these joint probabilities become increasingly small, leading to the forward recursions rapidly approaching values below machine precision.

## History

The Baum–Welch algorithm was named after its inventors Leonard E. Baum and Lloyd R. Welch. The algorithm and the Hidden Markov models were first described in a series of articles by Baum and his peers at the IDA Center for Communications Research, Princeton in the late 1960s and early 1970s. One of the first major applications of HMMs was to the field of speech processing. In the 1980s, HMMs were emerging as a useful tool in the analysis of biological systems and information, and in particular genetic information. They have since become an important tool in the probabilistic modeling of genomic sequences.

## Description

A hidden Markov model describes the joint probability of a collection of "hidden" and observed discrete random variables. It relies on the assumption that the *i*-th hidden variable given the (*i* − 1)-th hidden variable is independent of previous hidden variables, and the current observation variables depend only on the current hidden state.

The Baum–Welch algorithm uses the well known EM algorithm to find the maximum likelihood estimate of the parameters of a hidden Markov model given a set of observed feature vectors.

Let $X_{t}$ be a discrete hidden random variable with N possible values (i.e. We assume there are N states in total). We assume the $P(X_{t}\mid X_{t-1})$ is independent of time t , which leads to the definition of the time-independent stochastic transition matrix

$A=\{a_{ij}\}=P(X_{t}=j\mid X_{t-1}=i).$

The initial state distribution (i.e. when $t=1$ ) is given by

$\pi _{i}=P(X_{1}=i).$

The observation variables $Y_{t}$ can take one of K possible values. We also assume the observation given the "hidden" state is time independent. The probability of a certain observation $y_{i}$ at time t for state $X_{t}=j$ is given by

$b_{j}(y_{i})=P(Y_{t}=y_{i}\mid X_{t}=j).$

Taking into account all the possible values of $Y_{t}$ and $X_{t}$ , we obtain the $N\times K$ matrix $B=\{b_{j}(y_{i})\}$ where $b_{j}$ belongs to all the possible states and $y_{i}$ belongs to all the observations.

An observation sequence is given by $Y=(Y_{1}=y_{1},Y_{2}=y_{2},\ldots ,Y_{T}=y_{T})$ .

Thus we can describe a hidden Markov chain by $\theta =(A,B,\pi )$ . The Baum–Welch algorithm finds a local maximum for $\theta ^{*}=\operatorname {arg\,max} _{\theta }P(Y\mid \theta )$ (i.e. the HMM parameters $\theta$ that maximize the probability of the observation).

### Algorithm

Set $\theta =(A,B,\pi )$ with random initial conditions. They can also be set using prior information about the parameters if it is available; this can speed up the algorithm and also steer it toward the desired local maximum.

#### Forward procedure

Let $\alpha _{i}(t)=P(Y_{1}=y_{1},\ldots ,Y_{t}=y_{t},X_{t}=i\mid \theta )$ , the probability of seeing the observations $y_{1},y_{2},\ldots ,y_{t}$ and being in state i at time t . This is found recursively:

1. $\alpha _{i}(1)=\pi _{i}b_{i}(y_{1}),$
2. $\alpha _{i}(t+1)=b_{i}(y_{t+1})\sum _{j=1}^{N}\alpha _{j}(t)a_{ji}.$

Since this series converges exponentially to zero, the algorithm will numerically underflow for longer sequences. However, this can be avoided in a slightly modified algorithm by scaling $\alpha$ in the forward and $\beta$ in the backward procedure below.

#### Backward procedure

Let $\beta _{i}(t)=P(Y_{t+1}=y_{t+1},\ldots ,Y_{T}=y_{T}\mid X_{t}=i,\theta )$ that is the probability of the ending partial sequence $y_{t+1},\ldots ,y_{T}$ given starting state i at time t . We calculate $\beta _{i}(t)$ as,

1. $\beta _{i}(T)=1,$
2. $\beta _{i}(t)=\sum _{j=1}^{N}\beta _{j}(t+1)a_{ij}b_{j}(y_{t+1}).$

#### Update

We can now calculate the temporary variables, according to Bayes' theorem:

$\gamma _{i}(t)=P(X_{t}=i\mid Y,\theta )={\frac {P(X_{t}=i,Y\mid \theta )}{P(Y\mid \theta )}}={\frac {\alpha _{i}(t)\beta _{i}(t)}{\sum _{j=1}^{N}\alpha _{j}(t)\beta _{j}(t)}},$

which is the probability of being in state i at time t given the observed sequence Y and the parameters $\theta$

$\xi _{ij}(t)=P(X_{t}=i,X_{t+1}=j\mid Y,\theta )={\frac {P(X_{t}=i,X_{t+1}=j,Y\mid \theta )}{P(Y\mid \theta )}}={\frac {\alpha _{i}(t)a_{ij}\beta _{j}(t+1)b_{j}(y_{t+1})}{\sum _{k=1}^{N}\sum _{w=1}^{N}\alpha _{k}(t)a_{kw}\beta _{w}(t+1)b_{w}(y_{t+1})}},$

which is the probability of being in state i and j at times t and $t+1$ respectively given the observed sequence Y and parameters $\theta$ .

The denominators of $\gamma _{i}(t)$ and $\xi _{ij}(t)$ are the same ; they represent the probability of making the observation Y given the parameters $\theta$ .

The parameters of the hidden Markov model $\theta$ can now be updated:

- $\pi _{i}^{*}=\gamma _{i}(1),$

which is the expected frequency spent in state i at time 1 .

- $a_{ij}^{*}={\frac {\sum _{t=1}^{T-1}\xi _{ij}(t)}{\sum _{t=1}^{T-1}\gamma _{i}(t)}},$

which is the expected number of transitions from state *i* to state *j* compared to the expected total number of transitions starting in state *i*, including from state *i* to itself. The number of transitions starting in state *i* is equivalent to the number of times state *i* is observed in the sequence from *t* = 1 to *t* = *T* − 1.

- $b_{i}^{*}(v_{k})={\frac {\sum _{t=1}^{T}1_{y_{t}=v_{k}}\gamma _{i}(t)}{\sum _{t=1}^{T}\gamma _{i}(t)}},$

where

$1_{y_{t}=v_{k}}={\begin{cases}1&{\text{if }}y_{t}=v_{k},\\0&{\text{otherwise}}\end{cases}}$

is an indicator function, and $b_{i}^{*}(v_{k})$ is the expected number of times the output observations have been equal to $v_{k}$ while in state i over the expected total number of times in state i .

These steps are now repeated iteratively until a desired level of convergence.

**Note:** It is possible to over-fit a particular data set. That is, $P(Y\mid \theta _{\text{final}})>P(Y\mid \theta _{\text{true}})$ . The algorithm also does **not** guarantee a global maximum.

#### Multiple sequences

The algorithm described thus far assumes a single observed sequence $Y=y_{1},\ldots ,y_{T}$ . However, in many situations, there are several sequences observed: $Y_{1},\ldots ,Y_{R}$ . In this case, the information from all of the observed sequences must be used in the update of the parameters A , $\pi$ , and b . Assuming that you have computed $\gamma _{ir}(t)$ and $\xi _{ijr}(t)$ for each sequence $y_{1,r},\ldots ,y_{N_{r},r}$ , the parameters can now be updated:

- $\pi _{i}^{*}={\frac {\sum _{r=1}^{R}\gamma _{ir}(1)}{R}}$
- $a_{ij}^{*}={\frac {\sum _{r=1}^{R}\sum _{t=1}^{T-1}\xi _{ijr}(t)}{\sum _{r=1}^{R}\sum _{t=1}^{T-1}\gamma _{ir}(t)}},$
- $b_{i}^{*}(v_{k})={\frac {\sum _{r=1}^{R}\sum _{t=1}^{T}1_{y_{tr}=v_{k}}\gamma _{ir}(t)}{\sum _{r=1}^{R}\sum _{t=1}^{T}\gamma _{ir}(t)}},$

where

$1_{y_{tr}=v_{k}}={\begin{cases}1&{\text{if }}y_{t,r}=v_{k},\\0&{\text{otherwise}}\end{cases}}$

is an indicator function

## Example

Suppose we have a chicken from which we collect eggs at noon every day. Now whether or not the chicken has laid eggs for collection depends on some unknown factors that are hidden. We can however (for simplicity) assume that the chicken is always in one of two states that influence whether the chicken lays eggs, and that this state only depends on the state on the previous day. Now we don't know the state at the initial starting point, we don't know the transition probabilities between the two states and we don't know the probability that the chicken lays an egg given a particular state. To start we first guess the transition and emission matrices.

| Transition State 1 State 2 State 1 0.5 0.5 State 2 0.3 0.7 | Emission No Eggs Eggs State 1 0.3 0.7 State 2 0.8 0.2 | Initial State 1 0.2 State 2 0.8 |
|---|---|---|

We then take a set of observations (E = eggs, N = no eggs): N, N, N, N, N, E, E, N, N, N

This gives us a set of observed transitions between days: NN, NN, NN, NN, NE, EE, EN, NN, NN

The next step is to estimate a new transition matrix. For example, the probability of the sequence NN and the state being ⁠ $S_{1}$ ⁠ then ⁠ $S_{2}$ ⁠ is given by the following, $P(S_{1})\cdot P(N|S_{1})\cdot P(S_{1}\rightarrow S_{2})\cdot P(N|S_{2}).$

| Observed sequence | Highest probability of observing that sequence if state is ⁠ $S_{1}$ ⁠ then ⁠ $S_{2}$ ⁠ | Highest Probability of observing that sequence |   |
|---|---|---|---|
| NN | 0.024 = 0.2 × 0.3 × 0.5 × 0.8 | 0.3584 | ⁠ $S_{2}$ ⁠,⁠ $S_{2}$ ⁠ |
| NN | 0.024 = 0.2 × 0.3 × 0.5 × 0.8 | 0.3584 | ⁠ $S_{2}$ ⁠,⁠ $S_{2}$ ⁠ |
| NN | 0.024 = 0.2 × 0.3 × 0.5 × 0.8 | 0.3584 | ⁠ $S_{2}$ ⁠,⁠ $S_{2}$ ⁠ |
| NN | 0.024 = 0.2 × 0.3 × 0.5 × 0.8 | 0.3584 | ⁠ $S_{2}$ ⁠,⁠ $S_{2}$ ⁠ |
| NE | 0.006 = 0.2 × 0.3 × 0.5 × 0.2 | 0.1344 | ⁠ $S_{2}$ ⁠,⁠ $S_{1}$ ⁠ |
| EE | 0.014 = 0.2 × 0.7 × 0.5 × 0.2 | 0.0490 | ⁠ $S_{1}$ ⁠,⁠ $S_{1}$ ⁠ |
| EN | 0.056 = 0.2 × 0.7 × 0.5 × 0.8 | 0.0896 | ⁠ $S_{2}$ ⁠,⁠ $S_{2}$ ⁠ |
| NN | 0.024 = 0.2 × 0.3 × 0.5 × 0.8 | 0.3584 | ⁠ $S_{2}$ ⁠,⁠ $S_{2}$ ⁠ |
| NN | 0.024 = 0.2 × 0.3 × 0.5 × 0.8 | 0.3584 | ⁠ $S_{2}$ ⁠,⁠ $S_{2}$ ⁠ |
| Total | 0.22 | 2.4234 |   |

Thus the new estimate for the ⁠ $S_{1}$ ⁠ to ⁠ $S_{2}$ ⁠ transition is now ${\frac {0.22}{2.4234}}=0.0908$ (referred to as "Pseudo probabilities" in the following tables). We then calculate the ⁠ $S_{2}$ ⁠ to ⁠ $S_{1}$ ⁠, ⁠ $S_{2}$ ⁠ to ⁠ $S_{2}$ ⁠ and ⁠ $S_{1}$ ⁠ to ⁠ $S_{1}$ ⁠ transition probabilities and normalize each row of the transition matrix so that the probabilities of transitions from a given starting state sum to 1. This gives us the updated transition matrix:

| Old Transition Matrix State 1 State 2 State 1 0.5 0.5 State 2 0.3 0.7 | New Transition Matrix (Pseudo Probabilities) State 1 State 2 State 1 0.0598 0.0908 State 2 0.2179 0.9705 | New Transition Matrix (After Normalization) State 1 State 2 State 1 0.3973 0.6027 State 2 0.1833 0.8167 |
|---|---|---|

Next, we want to estimate a new emission matrix,

| Observed Sequence | Highest probability of observing that sequence if E is assumed to come from ⁠ $S_{1}$ ⁠ | Highest Probability of observing that sequence |   |   |
|---|---|---|---|---|
| NE | 0.1344 | ⁠ $S_{2}$ ⁠,⁠ $S_{1}$ ⁠ | 0.1344 | ⁠ $S_{2}$ ⁠,⁠ $S_{1}$ ⁠ |
| EE | 0.0490 | ⁠ $S_{1}$ ⁠,⁠ $S_{1}$ ⁠ | 0.0490 | ⁠ $S_{1}$ ⁠,⁠ $S_{1}$ ⁠ |
| EN | 0.0560 | ⁠ $S_{1}$ ⁠,⁠ $S_{2}$ ⁠ | 0.0896 | ⁠ $S_{2}$ ⁠,⁠ $S_{2}$ ⁠ |
| Total | 0.2394 |   | 0.2730 |   |

The new estimate for the E coming from ⁠ $S_{1}$ ⁠ emission is now ${\frac {0.2394}{0.2730}}=0.8769$ .

This allows us to calculate the emission matrix as described above in the algorithm, by adding up the probabilities for the respective observed sequences. We then repeat for if N came from ⁠ $S_{1}$ ⁠ and for if N and E came from ⁠ $S_{2}$ ⁠ and normalize.

| Old Emission Matrix No Eggs Eggs State 1 0.3 0.7 State 2 0.8 0.2 | New Emission Matrix (Estimates) No Eggs Eggs State 1 0.0404 0.8769 State 2 1.0000 0.7385 | New Emission Matrix (After Normalization) No Eggs Eggs State 1 0.0441 0.9559 State 2 0.5752 0.4248 |
|---|---|---|

To estimate the initial probabilities we assume all sequences start with the hidden state ⁠ $S_{1}$ ⁠ and calculate the highest probability and then repeat for ⁠ $S_{2}$ ⁠. Again we then normalize to give an updated initial vector.

Finally we repeat these steps until the resulting probabilities converge satisfactorily.

## Applications

### Speech recognition

Hidden Markov Models were first applied to speech recognition by James K. Baker in 1975. Continuous speech recognition occurs by the following steps, modeled by a HMM. Feature analysis is first undertaken on temporal and/or spectral features of the speech signal. This produces an observation vector. The feature is then compared to all sequences of the speech recognition units. These units could be phonemes, syllables, or whole-word units. A lexicon decoding system is applied to constrain the paths investigated, so only words in the system's lexicon (word dictionary) are investigated. Similar to the lexicon decoding, the system path is further constrained by the rules of grammar and syntax. Finally, semantic analysis is applied and the system outputs the recognized utterance. A limitation of many HMM applications to speech recognition is that the current state only depends on the state at the previous time-step, which is unrealistic for speech as dependencies are often several time-steps in duration. The Baum–Welch algorithm also has extensive applications in solving HMMs used in the field of speech synthesis.

### Cryptanalysis

The Baum–Welch algorithm is often used to estimate the parameters of HMMs in deciphering hidden or noisy information and consequently is often used in cryptanalysis. In data security an observer would like to extract information from a data stream without knowing all the parameters of the transmission. This can involve reverse engineering a channel encoder. HMMs and as a consequence the Baum–Welch algorithm have also been used to identify spoken phrases in encrypted VoIP calls. In addition HMM cryptanalysis is an important tool for automated investigations of cache-timing data. It allows for the automatic discovery of critical algorithm state, for example key values.

### Applications in bioinformatics

#### Finding genes

##### Prokaryotic

The GLIMMER (Gene Locator and Interpolated Markov ModelER) software was an early gene-finding program used for the identification of coding regions in prokaryotic DNA. GLIMMER uses Interpolated Markov Models (IMMs) to identify the coding regions and distinguish them from the noncoding DNA. The latest release (GLIMMER3) has been shown to have increased specificity and accuracy compared with its predecessors with regard to predicting translation initiation sites, demonstrating an average 99% accuracy in locating 3' locations compared to confirmed genes in prokaryotes.

##### Eukaryotic

The GENSCAN webserver is a gene locator capable of analyzing eukaryotic sequences up to one million base-pairs (1 Mbp) long. GENSCAN utilizes a general inhomogeneous, three periodic, fifth order Markov model of DNA coding regions. Additionally, this model accounts for differences in gene density and structure (such as intron lengths) that occur in different isochores. While most integrated gene-finding software (at the time of GENSCANs release) assumed input sequences contained exactly one gene, GENSCAN solves a general case where partial, complete, or multiple genes (or even no gene at all) is present. GENSCAN was shown to exactly predict exon location with 90% accuracy with 80% specificity compared to an annotated database.

#### Copy-number variation detection

Copy-number variations (CNVs) are an abundant form of genome structure variation in humans. A discrete-valued bivariate HMM (dbHMM) was used assigning chromosomal regions to seven distinct states: unaffected regions, deletions, duplications and four transition states. Solving this model using Baum-Welch demonstrated the ability to predict the location of CNV breakpoint to approximately 300 bp from micro-array experiments. This magnitude of resolution enables more precise correlations between different CNVs and across populations than previously possible, allowing the study of CNV population frequencies. It also demonstrated a direct inheritance pattern for a particular CNV.

## Implementations

- Accord.NET in C#
- ghmm C library with Python bindings that supports both discrete and continuous emissions.
- hmmlearn Python library that implements Baum-Welch on various discrete-time HMMs
- Jajapy Python library that implements Baum-Welch on various kind of Markov Models ( HMM, MC, MDP, CTMC).
- HiddenMarkovModels.jl package for Julia.
- HMMFit function in the RHmm package for R.
- hmmtrain in MATLAB
- rustbio in Rust
