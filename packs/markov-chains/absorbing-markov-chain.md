---
title: "Absorbing Markov chain"
source: https://en.wikipedia.org/wiki/Absorbing_Markov_chain
domain: markov-chains
license: CC-BY-SA-4.0
tags: markov chain, markov property, stochastic matrix, hidden markov model
fetched: 2026-07-02
---

# Absorbing Markov chain

In the mathematical theory of probability, an **absorbing Markov chain** is a Markov chain in which every state can reach an absorbing state. An absorbing state is a state that, once entered, cannot be left.

Like general Markov chains, there can be continuous-time absorbing Markov chains with an infinite state space. However, this article concentrates on the discrete-time discrete-state-space case.

## Formal definition

A Markov chain is an absorbing chain if

1. there is at least one absorbing state and
2. it is possible to go from any state to at least one absorbing state in a finite number of steps.

In an absorbing Markov chain, a state that is not absorbing is called transient.

### Canonical form

Let an absorbing Markov chain with transition matrix *P* have *t* transient states and *r* absorbing states. The rows of *P* represent sources, while columns represent destinations. By ordering the transient states before the absorbing states, it can be assumed that *P* has the form

$P={\begin{bmatrix}Q&R\\\mathbf {0} &I_{r}\end{bmatrix}},$

where *Q* is a *t*-by-*t* matrix, *R* is a nonzero *t*-by-*r* matrix, **0** is an *r*-by-*t* zero matrix, and *I**r* is the *r*-by-*r* identity matrix. Thus, *Q* describes the probability of transitioning from some transient state to another while *R* describes the probability of transitioning from some transient state to some absorbing state.

The probability of transitioning from *i* to *j* in exactly *k* steps is the (*i*,*j*)-entry of *P*k, further computed below. When considering only transient states, the probability is found in the upper left of *P*k, the (*i*,*j*)-entry of *Q*k.

## Fundamental matrix

### Expected number of visits to a transient state

A basic property about an absorbing Markov chain is the expected number of visits to a transient state *j* starting from a transient state *i* (before being absorbed). This can be established to be given by the (*i*, *j*) entry of so-called fundamental matrix *N*, obtained by summing *Q*k for all *k* (from 0 to ∞). It can be proven that

$N:=\sum _{k=0}^{\infty }Q^{k}=(I_{t}-Q)^{-1},$

where *I**t* is the *t*-by-*t* identity matrix. The computation of this formula is the matrix equivalent of the geometric series of scalars, ${\textstyle \sum }_{k=0}^{\infty }q^{k}={\tfrac {1}{1-q}}$ .

With the matrix *N* in hand, also other properties of the Markov chain are easy to obtain.

### Expected number of steps before being absorbed

The expected number of steps before being absorbed in any absorbing state, when starting in transient state *i* can be computed via a sum over transient states. The value is given by the *i*th entry of the vector

$\mathbf {t$

where **1** is a length-*t* column vector whose entries are all 1.

### Absorbing probabilities

By induction,

$P^{k}={\begin{bmatrix}Q^{k}&(I_{t}-Q^{k})NR\\\mathbf {0} &I_{r}\end{bmatrix}}.$

The probability of eventually being absorbed in the absorbing state *j* when starting from transient state *i* is given by the (*i*,*j*)-entry of the matrix

$B:=NR$

.

The number of columns of this matrix equals the number of absorbing states *r*.

An approximation of those probabilities can also be obtained directly from the (*i*,*j*)-entry of $P^{k}$ for a large enough value of *k*, when *i* is the index of a transient, and *j* the index of an absorbing state. This is because

$\left(\lim _{k\to \infty }P^{k}\right)_{i,t+j}=B_{i,j}$

.

### Transient visiting probabilities

The probability of visiting transient state *j* when starting at a transient state *i* is the (*i*,*j*)-entry of the matrix

$H:=(N-I_{t})(N_{\operatorname {dg} })^{-1},$

where *N*dg is the diagonal matrix with the same diagonal as *N*.

### Variance on number of transient visits

The variance on the number of visits to a transient state *j* with starting at a transient state *i* (before being absorbed) is the (*i*,*j*)-entry of the matrix

$N_{2}:=N(2N_{\operatorname {dg} }-I_{t})-N_{\operatorname {sq} },$

where *N*sq is the Hadamard product of *N* with itself (i.e. each entry of *N* is squared).

### Variance on number of steps

The variance on the number of steps before being absorbed when starting in transient state *i* is the *i*th entry of the vector

$(2N-I_{t})\mathbf {t} -\mathbf {t} _{\operatorname {sq} },$

where **t**sq is the Hadamard product of **t** with itself (i.e., as with *N*sq, each entry of **t** is squared).

## Examples

### String generation

Consider the process of repeatedly flipping a fair coin until the sequence (heads, tails, heads) appears. This process is modeled by an absorbing Markov chain with transition matrix

$P={\begin{bmatrix}1/2&1/2&0&0\\0&1/2&1/2&0\\1/2&0&0&1/2\\0&0&0&1\end{bmatrix}}.$

The first state represents the empty string, the second state the string "H", the third state the string "HT", and the fourth state the string "HTH". Although in reality, the coin flips cease after the string "HTH" is generated, the perspective of the absorbing Markov chain is that the process has transitioned into the absorbing state representing the string "HTH" and, therefore, cannot leave.

For this absorbing Markov chain, the fundamental matrix is

${\begin{aligned}N&=(I-Q)^{-1}=\left({\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}}-{\begin{bmatrix}1/2&1/2&0\\0&1/2&1/2\\1/2&0&0\end{bmatrix}}\right)^{-1}\\[4pt]&={\begin{bmatrix}1/2&-1/2&0\\0&1/2&-1/2\\-1/2&0&1\end{bmatrix}}^{-1}={\begin{bmatrix}4&4&2\\2&4&2\\2&2&2\end{bmatrix}}.\end{aligned}}$

The expected number of steps starting from each of the transient states is

$\mathbf {t} =N\mathbf {1} ={\begin{bmatrix}4&4&2\\2&4&2\\2&2&2\end{bmatrix}}{\begin{bmatrix}1\\1\\1\end{bmatrix}}={\begin{bmatrix}10\\8\\6\end{bmatrix}}.$

Therefore, the expected number of coin flips before observing the sequence (heads, tails, heads) is 10, the entry for the state representing the empty string.

### Games of chance

Games based entirely on chance can be modeled by an absorbing Markov chain. A classic example of this is the ancient Indian board game Snakes and Ladders. The graph on the left plots the probability mass in the lone absorbing state that represents the final square as the transition matrix is raised to larger and larger powers. To determine the expected number of turns to complete the game, compute the vector **t** as described above and examine **t**start, which is approximately 39.2.

### Infectious disease testing

Infectious disease testing, either of blood products or in medical clinics, is often taught as an example of an absorbing Markov chain. The public U.S. Centers for Disease Control and Prevention (CDC) model for HIV and for hepatitis B, for example, illustrates the property that absorbing Markov chains can lead to the detection of disease, versus the loss of detection through other means.

In the standard CDC model, the Markov chain has five states, a state in which the individual is uninfected, then a state with infected but undetectable virus, a state with detectable virus, and absorbing states of having quit/been lost from the clinic, or of having been detected (the goal). The typical rates of transition between the Markov states are the probability *p* per unit time of being infected with the virus, *w* for the rate of window period removal (time until virus is detectable), *q* for quit/loss rate from the system, and *d* for detection, assuming a typical rate $\lambda$ at which the health system administers tests of the blood product or patients in question.

It follows that we can "walk along" the Markov model to identify the overall probability of detection for a person starting as undetected, by multiplying the probabilities of transition to each next state of the model as:

${\frac {p}{(p+q)}}{\frac {w}{(w+q)}}{\frac {d}{(d+q)}}$ .

The subsequent total absolute number of false negative tests—the primary CDC concern—would then be the rate of tests, multiplied by the probability of reaching the infected but undetectable state, times the duration of staying in the infected undetectable state:

${\frac {p}{(p+q)}}{\frac {1}{(w+q)}}\lambda$ .
