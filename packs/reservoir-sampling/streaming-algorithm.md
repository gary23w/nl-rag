---
title: "Streaming algorithm"
source: https://en.wikipedia.org/wiki/Streaming_algorithm
domain: reservoir-sampling
license: CC-BY-SA-4.0
tags: reservoir sampling, streaming algorithm, simple random sample, online algorithm
fetched: 2026-07-02
---

# Streaming algorithm

In computer science, **streaming algorithms** process input data streams as a sequence of items, typically making just one pass (or a few passes) through the data. These algorithms are designed to operate with limited memory, generally logarithmic in the size of the stream and/or in the maximum value in the stream, and may also have limited processing time per item.

As a result of these constraints, streaming algorithms often produce approximate answers based on a summary or "sketch" of the data stream.

## History

Though streaming algorithms had already been studied by Munro and Paterson as early as 1978, as well as Philippe Flajolet and G. Nigel Martin in 1982/83, the field of streaming algorithms was first formalized and popularized in a 1996 paper by Noga Alon, Yossi Matias, and Mario Szegedy. For this paper, the authors later won the Gödel Prize in 2005 "for their foundational contribution to streaming algorithms." There has since been a large body of work centered around data streaming algorithms that spans a diverse spectrum of computer science fields such as theory, databases, networking, and natural language processing.

Semi-streaming algorithms were introduced in 2005 as a relaxation of streaming algorithms for graphs, in which the space allowed is linear in the number of vertices *n*, but only logarithmic in the number of edges *m*. This relaxation is still meaningful for dense graphs, and can solve interesting problems (such as connectivity) that are insoluble in $o(n)$ space.

## Models

### Data stream model

In the data stream model, some or all of the input is represented as a finite sequence of integers (from some finite domain) which is generally not available for random access, but instead arrives one at a time in a "stream". If the stream has length *n* and the domain has size *m*, algorithms are generally constrained to use space that is logarithmic in *m* and *n*. They can generally make only some small constant number of passes over the stream, sometimes just one.

### Turnstile and cash register models

Much of the streaming literature is concerned with computing statistics on frequency distributions that are too large to be stored. For this class of problems, there is a vector $\mathbf {a} =(a_{1},\dots ,a_{n})$ (initialized to the zero vector $\mathbf {0}$ ) that has updates presented to it in a stream. The goal of these algorithms is to compute functions of $\mathbf {a}$ using considerably less space than it would take to represent $\mathbf {a}$ precisely. There are two common models for updating such streams, called the "cash register" and "turnstile" models.

In the cash register model, each update is of the form $\langle i,c\rangle$ , so that $a_{i}$ is incremented by some positive integer c . A notable special case is when $c=1$ (only unit insertions are permitted).

In the turnstile model, each update is of the form $\langle i,c\rangle$ , so that $a_{i}$ is incremented by some (possibly negative) integer c . In the "strict turnstile" model, no $a_{i}$ at any time may be less than zero.

### Sliding window model

Several papers also consider the "sliding window" model. In this model, the function of interest is computing over a fixed-size window in the stream. As the stream progresses, items from the end of the window are removed from consideration while new items from the stream take their place.

Besides the above frequency-based problems, some other types of problems have also been studied. Many graph problems are solved in the setting where the adjacency matrix or the adjacency list of the graph is streamed in some unknown order. There are also some problems that are very dependent on the order of the stream (i.e., asymmetric functions), such as counting the number of inversions in a stream and finding the longest increasing subsequence.

## Evaluation

The performance of an algorithm that operates on data streams is measured by three basic factors:

- The number of passes the algorithm must make over the stream.
- The available memory.
- The running time of the algorithm.

These algorithms have many similarities with online algorithms since they both require decisions to be made before all data are available, but they are not identical. Data stream algorithms only have limited memory available but they may be able to defer action until a group of points arrive, while online algorithms are required to take action as soon as each point arrives.

If the algorithm is an approximation algorithm then the accuracy of the answer is another key factor. The accuracy is often stated as an $(\epsilon ,\delta )$ approximation meaning that the algorithm achieves an error of less than $\epsilon$ with probability $1-\delta$ .

## Applications

Streaming algorithms have several applications in networking such as monitoring network links for elephant flows, counting the number of distinct flows, estimating the distribution of flow sizes, and so on. They also have applications in databases, such as estimating the size of a join .

## Some streaming problems

### Frequency moments

The kth frequency moment of a set of frequencies $\mathbf {a}$ is defined as $F_{k}(\mathbf {a} )=\sum _{i=1}^{n}a_{i}^{k}$ .

The first moment $F_{1}$ is simply the sum of the frequencies (i.e., the total count). The second moment $F_{2}$ is useful for computing statistical properties of the data, such as the Gini coefficient of variation. $F_{\infty }$ is defined as the frequency of the most frequent items.

The seminal paper of Alon, Matias, and Szegedy dealt with the problem of estimating the frequency moments.

#### Calculating frequency moments

A direct approach to find the frequency moments requires to maintain a register mi for all distinct elements *a**i* ∈ (1,2,3,4,...,*N*) which requires at least memory of order $\Omega (N)$ . But we have space limitations and require an algorithm that computes in much lower memory. This can be achieved by using approximations instead of exact values. An algorithm that computes an (*ε,δ*)approximation of Fk, where F'k is the (*ε,δ*)- approximated value of Fk. Where *ε* is the approximation parameter and *δ* is the confidence parameter.

##### Calculating *F*0 (distinct elements in a data stream)

###### FM-Sketch algorithm

Flajolet et al. in introduced a probabilistic method of counting which was inspired from a paper by Robert Morris. Morris in his paper says that if the requirement of accuracy is dropped, a counter *n* can be replaced by a counter log *n* which can be stored in log log *n* bits. Flajolet et al. in improved this method by using a hash function h which is assumed to uniformly distribute the element in the hash space (a binary string of length L).

$h:[m]\rightarrow [0,2^{L}-1]$

Let bit(*y,k*) represent the kth bit in binary representation of y

$y=\sum _{k\geq 0}\mathrm {bit} (y,k)*2^{k}$

Let $\rho (y)$ represents the position of least significant 1-bit in the binary representation of yi with a suitable convention for $\rho (0)$ .

$\rho (y)={\begin{cases}\mathrm {Min} (k:\mathrm {bit} (y,k)==1)&{\text{if }}y>0\\L&{\text{if }}y=0\end{cases}}$

Let *A* be the sequence of data stream of length *M* whose cardinality need to be determined. Let *BITMAP* [0...*L* − 1] be the

hash space where the ρ(*hashedvalues*) are recorded. The below algorithm then determines approximate cardinality of *A*.

```
Procedure FM-Sketch:

    for i in 0 to L − 1 do
        BITMAP[i] := 0 
    end for
    for x in A: do
        Index := ρ(hash(x))
        if BITMAP[index] = 0 then
            BITMAP[index] := 1
        end if
    end for
    B := Position of left most 0 bit of BITMAP[] 
    return 2 ^ B
```

If there are *N* distinct elements in a data stream.

- For $i\gg \log(N)$ then *BITMAP*[*i*] is certainly 0
- For $i\ll \log(N)$ then *BITMAP*[*i*] is certainly 1
- For $i\approx \log(N)$ then *BITMAP*[*i*] is a fringes of 0's and 1's

###### *K*-minimum value algorithm

The previous algorithm describes the first attempt to approximate *F*0 in the data stream by Flajolet and Martin. Their algorithm picks a random hash function which they assume to uniformly distribute the hash values in hash space.

Bar-Yossef et al. in introduced k-minimum value algorithm for determining number of distinct elements in data stream. They used a similar hash function *h* which can be normalized to [0,1] as $h:[m]\rightarrow [0,1]$ . But they fixed a limit *t* to number of values in hash space. The value of *t* is assumed of the order $O\left({\dfrac {1}{\varepsilon _{2}}}\right)$ (i.e. less approximation-value *ε* requires more *t*). KMV algorithm keeps only *t*-smallest hash values in the hash space. After all the *m* values of stream have arrived, $\upsilon =\mathrm {Max} (h(a_{i}))$ is used to calculate $F'_{0}={\dfrac {t}{\upsilon }}$ . That is, in a close-to uniform hash space, they expect at-least *t* elements to be less than $O\left({\dfrac {t}{F_{0}}}\right)$ .

```
Procedure 2 K-Minimum Value

Initialize first t values of KMV 
for a in a1 to an do
    if h(a) < Max(KMV) then
        Remove Max(KMV) from KMV set
        Insert h(a) to KMV 
    end if
end for 
return t/Max(KMV)
```

###### Complexity analysis of KMV

KMV algorithm can be implemented in $O\left(\left({\dfrac {1}{\varepsilon _{2}}}\right)\cdot \log(m)\right)$ memory bits space. Each hash value requires space of order $O(\log(m))$ memory bits. There are hash values of the order $O\left({\dfrac {1}{\varepsilon _{2}}}\right)$ . The access time can be reduced if we store the *t* hash values in a binary tree. Thus the time complexity will be reduced to $O\left(\log \left({\dfrac {1}{\varepsilon }}\right)\cdot \log(m)\right)$ .

##### Calculating *F*k

Alon et al. estimates Fk by defining random variables that can be computed within given space and time. The expected value of random variables gives the approximate value of Fk.

Assume length of sequence *m* is known in advance. Then construct a random variable *X* as follows:

- Select ap be a random member of sequence A with index at p, $a_{p}=l\in (1,2,3,\ldots ,n)$
- Let $r=|\{q:q\geq p,a_{q}=l\}|$ , represents the number of occurrences of l within the members of the sequence A following ap.
- Random variable $X=m(r^{k}-(r-1)^{k})$ .

Assume *S*1 be of the order $O(n^{1-1/k}/\lambda ^{2})$ and *S*2 be of the order $O(\log(1/\varepsilon ))$ . Algorithm takes *S*2 random variable $Y_{1},Y_{2},...,Y_{S2}$ and outputs the median Y . Where Yi is the average of Xij where 1 ≤ *j* ≤ *S*1.

Now calculate expectation of random variable *E*(*X*).

${\begin{array}{lll}E(X)&=&\sum _{i=1}^{n}\sum _{i=1}^{m_{i}}(j^{k}-(j-1)^{k})\\&=&{\frac {m}{m}}[(1^{k}+(2^{k}-1^{k})+\ldots +(m_{1}^{k}-(m_{1}-1)^{k}))\\&&\;+\;(1^{k}+(2^{k}-1^{k})+\ldots +(m_{2}^{k}-(m_{2}-1)^{k}))+\ldots \\&&\;+\;(1^{k}+(2^{k}-1^{k})+\ldots +(m_{n}^{k}-(m_{n}-1)^{k}))]\\&=&\sum _{i=1}^{n}m_{i}^{k}=F_{k}\end{array}}$

###### Complexity of *F*k

From the algorithm to calculate Fk discussed above, we can see that each random variable X stores value of ap and r. So, to compute X we need to maintain only log(*n*) bits for storing ap and log(*n*) bits for storing r. Total number of random variable X will be the ⁠ $S_{1}*S_{2}$ ⁠.

Hence the total space complexity the algorithm takes is of the order of $O\left({\dfrac {k\log {1 \over \varepsilon }}{\lambda ^{2}}}n^{1-{1 \over k}}\left(\log n+\log m\right)\right)$

###### Simpler approach to calculate *F*2

The previous algorithm calculates $F_{2}$ in order of $O({\sqrt {n}}(\log m+\log n))$ memory bits. Alon et al. in simplified this algorithm using four-wise independent random variable with values mapped to $\{-1,1\}$ .

This further reduces the complexity to calculate $F_{2}$ to $O\left({\dfrac {\log {1 \over \varepsilon }}{\lambda ^{2}}}\left(\log n+\log m\right)\right)$

### Frequent elements

In the data stream model, the **frequent elements problem** is to output a set of elements that constitute more than some fixed fraction of the stream. A special case is the **majority problem**, which is to determine whether or not any value constitutes a majority of the stream.

More formally, fix some positive constant *c* > 1, let the length of the stream be *m*, and let *f**i* denote the frequency of value *i* in the stream. The frequent elements problem is to output the set { *i* | *f**i* > m/c }.

Some notable algorithms are:

- Boyer–Moore majority vote algorithm
- Count-Min sketch
- Lossy counting
- Multi-stage Bloom filters
- Misra–Gries heavy hitters algorithm
- Misra–Gries summary

### Event detection

Detecting events in data streams is often done using a heavy hitters algorithm as listed above: the most frequent items and their frequency are determined using one of these algorithms, then the largest increase over the previous time point is reported as trend. This approach can be refined by using exponentially weighted moving averages and variance for normalization.

### Counting distinct elements

Counting the number of distinct elements in a stream (sometimes called the *F*0 moment) is another problem that has been well studied. The first algorithm for it was proposed by Flajolet and Martin. In 2010, Daniel Kane, Jelani Nelson and David Woodruff found an asymptotically optimal algorithm for this problem. It uses *O*(*ε*2 + log *d*) space, with *O*(1) worst-case update and reporting times, as well as universal hash functions and a r-wise independent hash family where *r* = Ω(log(1/*ε*) / log log(1/*ε*)).

### Entropy

The (empirical) entropy of a set of frequencies $\mathbf {a}$ is defined as $F_{k}(\mathbf {a} )=\sum _{i=1}^{n}{\frac {a_{i}}{m}}\log {\frac {a_{i}}{m}}$ , where $m=\sum _{i=1}^{n}a_{i}$ .

### Online learning

Learn a model (e.g. a classifier) by a single pass over a training set.

- Feature hashing
- Stochastic gradient descent

## Lower bounds

Lower bounds have been computed for many of the data streaming problems that have been studied. By far, the most common technique for computing these lower bounds has been using communication complexity.
