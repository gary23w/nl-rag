---
title: "Slice sampling"
source: https://en.wikipedia.org/wiki/Slice_sampling
domain: gibbs-sampling
license: CC-BY-SA-4.0
tags: Gibbs sampling, conjugate prior, slice sampling, conditional probability distribution
fetched: 2026-07-02
---

# Slice sampling

**Slice sampling** is a type of Markov chain Monte Carlo algorithm for pseudo-random number sampling, i.e. for drawing random samples from a statistical distribution. The method is based on the fact that to sample a random variable one can sample uniformly from the region under the graph of its density function.

## Motivation

Sampling a random variable *x* from a given probability density function $f(x)$ is a common task in statistics. The figure (below left) sketches the graph of $f(x)$ , where the height at *x* corresponds to the likelihood at that point. In the case of uniform distribution, each value of *x* would have the same likelihood of being sampled, and the corresponding function would be $f(x)=y$ for some constant y . Instead of the original black line, a uniform distribution is denoted by the blue line in the second figure (below right). In order to sample *x* in a manner which will retain the distribution $f(x)$ , a sampling technique that takes into account the varied likelihoods for each range of $f(x)$ must be used.

(Mathematical graph of an arbitrary continuous probability density function. The horizontal axis is given by x, and the density f(x) is plotted in the vertical.) (Illustration of a uniform distribution, layered on top of f(x) plotted in the previous figure.)

## Method

Slice sampling, in its simplest form, samples uniformly from underneath the curve $f(x)$ without the need to reject any points, as follows:

1. Choose a starting value *$x_{0}$* for which *$f(x_{0})>0$*
2. Sample a *y* value uniformly between *0* and *$f(x_{0})$*.
3. Draw a horizontal line across the curve at this *y* position.
4. Sample a point *$(x,y)$* from the line segments within the curve.
5. Repeat from step 2 using the new *x* value.

The motivation here is that one way to sample a point uniformly from within an arbitrary curve is first to draw thin uniform-height horizontal slices across the whole curve. Then, we can sample a point within the curve by randomly selecting a slice that falls at or below the curve at the *x*-position from the previous iteration, then randomly picking an *x*-position somewhere along the slice. By using the *x*-position from the previous iteration of the algorithm, in the long run we select slices with probabilities proportional to the lengths of their segments within the curve. The most difficult part of this algorithm is finding the bounds of the horizontal slice, which involves inverting the function describing the distribution being sampled from. This is especially problematic for multi-modal distributions, where the slice may consist of multiple discontinuous parts. It is often possible to use a form of rejection sampling to overcome this, where we sample from a larger slice that is known to include the desired slice in question, and then discard points outside of the desired slice. This algorithm can be used to sample from the area under *any* curve, regardless of whether the function integrates to 1. In fact, scaling a function by a constant has no effect on the sampled *x*-positions. This means that the algorithm can be used to sample from a distribution whose probability density function is only known up to a constant (i.e. whose normalizing constant is unknown), which is common in computational statistics.

## Implementation

Slice sampling gets its name from the first step: defining a *slice* by sampling from an auxiliary variable Y . This variable is sampled from $[0,f(x)]$ , where $f(x)$ is either the probability density function (PDF) of *x* or is at least proportional to its PDF. This defines a slice of *x* where $f(x)\geq Y$ . In other words, we are now looking at a region of *x* where the probability density is at least Y . Then the next value of *x* is sampled uniformly from this slice. A new value of Y is sampled, then *x*, and so on. This can be visualized as alternatively sampling the y-position and then the *x*-position of points under PDF, thus the *x*s are from the desired distribution. The Y values have no particular consequences or interpretations outside of their usefulness for the procedure.

If both the PDF and its inverse are available, and the distribution is unimodal, then finding the slice and sampling from it are simple. If not, a stepping-out procedure can be used to find a region whose endpoints fall outside the slice. Then, a sample can be drawn from the slice using rejection sampling. Various procedures for this are described in detail by Radford M. Neal.

Note that, in contrast to many available methods for generating random numbers from non-uniform distributions, random variates generated directly by this approach will exhibit serial statistical dependence. This is because to draw the next sample, we define the slice based on the value of *$f(x)$* for the current sample.

## Compared to other methods

Slice sampling is a Markov chain method and as such serves the same purpose as Gibbs sampling and Metropolis. Unlike Metropolis, there is no need to manually tune the candidate function or candidate standard deviation.

Recall that Metropolis is sensitive to step size. If the step size is too small, random walk causes slow decorrelation. If the step size is too large, there is great inefficiency due to a high rejection rate.

In contrast to Metropolis, slice sampling automatically adjusts the step size to match the local shape of the density function. Implementation is arguably easier and more efficient than Gibbs sampling or simple Metropolis updates.

Note that, in contrast to many available methods for generating random numbers from non-uniform distributions, random variates generated directly by this approach will exhibit serial statistical dependence. In other words, not all points have the same independent likelihood of selection. This is because, to draw the next sample, we define the slice based on the value of *$f(x)$* for the current sample. However, the generated samples are markovian, and are therefore expected to converge to the correct distribution in the long run.

Slice Sampling requires that the distribution to be sampled be evaluable. One way to relax this requirement is to substitute an evaluable distribution which is proportional to the true unevaluable distribution.

## Univariate case

To sample a random variable *x* with density *$f(x)$* we introduce an auxiliary variable *Y* and iterate as follows:

- Given a sample *x* we choose *y* uniformly at random from the interval $[0,f(x)]$ ;
- given *y* we choose *x* uniformly at random from the set $f^{-1}[y,+\infty )$ .
- The sample of *x* is obtained by ignoring the *y* values.

Our auxiliary variable *y* represents a horizontal "slice" of the distribution. The rest of each iteration is dedicated to sampling an *x* value from the slice which is representative of the density of the region being considered.

In practice, sampling from a horizontal slice of a multimodal distribution is difficult. There is a tension between obtaining a large sampling region and thereby making possible large moves in the distribution space, and obtaining a simpler sampling region to increase efficiency. One option for simplifying this process is regional expansion and contraction.

- First, a width parameter *w* is used to define the area containing the given *x* value. Each endpoint of this area is tested to see if it lies outside the given slice. If not, the region is extended in the appropriate direction(s) by *w* until the end both endpoints lie outside the slice.
- A candidate sample is selected uniformly from within this region. If the candidate sample lies inside of the slice, then it is accepted as the new sample. If it lies outside of the slice, the candidate point becomes the new boundary for the region. A new candidate sample is taken uniformly. The process repeats until the candidate sample is within the slice. (See diagram for a visual example).

→

## Slice-within-Gibbs sampling

In a Gibbs sampler, one needs to draw efficiently from all the full-conditional distributions. When sampling from a full-conditional density is not easy, a single iteration of slice sampling or the Metropolis-Hastings algorithm can be used within-Gibbs to sample from the variable in question. If the full-conditional density is log-concave, a more efficient alternative is the application of adaptive rejection sampling (ARS) methods. When the ARS techniques cannot be applied (since the full-conditional is non-log-concave), the **adaptive rejection Metropolis sampling algorithms** are often employed.

## Multivariate methods

### Treating each variable independently

Single variable slice sampling can be used in the multivariate case by sampling each variable in turn repeatedly, as in Gibbs sampling. To do so requires that we can compute, for each component $x_{i}$ a function that is proportional to $p(x_{i}|x_{0}...x_{n})$ .

To prevent random walk behavior, overrelaxation methods can be used to update each variable in turn. Overrelaxation chooses a new value on the opposite side of the mode from the current value, as opposed to choosing a new independent value from the distribution as done in Gibbs.

### Hyperrectangle slice sampling

This method adapts the univariate algorithm to the multivariate case by substituting a hyperrectangle for the one-dimensional *w* region used in the original. The hyperrectangle *H* is initialized to a random position over the slice. *H* is then shrunk as points from it are rejected.

### Reflective slice sampling

Reflective slice sampling is a technique to suppress random walk behavior in which the successive candidate samples of distribution *f*(*x*) are kept within the bounds of the slice by "reflecting" the direction of sampling inward toward the slice once the boundary has been hit.

In this graphical representation of reflective sampling, the shape indicates the bounds of a sampling slice. The dots indicate start and stopping points of a sampling walk. When the samples hit the bounds of the slice, the direction of sampling is "reflected" back into the slice.

(alt text)

## Example

Consider a single variable example. Suppose our true distribution is a normal distribution with mean 0 and standard deviation 3, $g(x)\sim N(0,3^{2})$ . So: $f(x)={\frac {1}{\sqrt {2\pi \cdot 3^{2}}}}\ e^{-{\frac {(x-0)^{2}}{2\cdot 3^{2}}}}$ . The peak of the distribution is obviously at $x=0$ , at which point $f(x)\approx 0.1330$ .

1. We first draw a uniform random value *y* from the range of *$f(x)$* in order to define our slice(es). *$f(x)$* ranges from 0 to ~0.1330, so any value between these two extremes suffice. Suppose we take *$y=0.1$*. The problem becomes how to sample points that have values *$y>0.1$*.
2. Next, we set our width parameter *w* which we will use to expand our region of consideration. This value is arbitrary. Suppose *$w=2$*.
3. Next, we need an initial value for *x*. We draw *x* from the uniform distribution within the domain of *$f(x)$* which satisfies *$f(x)>0.1$* (our *y* parameter). Suppose *$x=2$*. This works because *$f(2)=0.1065...>0.1$*.
4. Because *$x=2$* and *$w=2$*, our current region of interest is bounded by *$(1,3)$*.
5. Now, each endpoint of this area is tested to see if it lies outside the given slice. Our right bound lies outside our slice (*$f(3)=0.0807...<0.1$*), but the left value does not (*$f(1)=0.1258...>0.1$*). We expand the left bound by adding *w* to it until it extends past the limit of the slice. After this process, the new bounds of our region of interest are *$(-3,3)$*.
6. Next, we take a uniform sample within *$(-3,3)$*. Suppose this sample yields *$x=-2.9$*. Though this sample is within our region of interest, it does not lie within our slice (*$f(2.9)=0.08334...<0.1$*), so we modify the left bound of our region of interest to this point. Now we take a uniform sample from *$(-2.9,3)$*. Suppose this time our sample yields *$x=1$*, which is within our slice, and thus is the accepted sample output by slice sampling. Had our new *x* not been within our slice, we would continue the shrinking/resampling process until a valid *x* within bounds is found.

If we're interested in the peak of the distribution, we can keep repeating this process since the new point corresponds to a higher *$f(x)$* than the original point.

## Another example

To sample from the normal distribution $N(0,1)$ we first choose an initial *x*—say 0. After each sample of *x* we choose *y* uniformly at random from $(0,e^{-x^{2}/2}/{\sqrt {2\pi }}]$ , which is bounded the pdf of $N(0,1)$ . After each *y* sample we choose *x* uniformly at random from $[-\alpha ,\alpha ]$ where $\alpha ={\sqrt {-2\ln(y{\sqrt {2\pi }})}}$ . This is the slice where $f(x)>y$ .

An implementation in the Macsyma language is:

```mw
slice(x) := block([y, alpha],
 y:random(exp(-x^2 / 2.0) / sqrt(2.0 * dfloat(%pi))),
 alpha:sqrt(-2.0 * ln(y * sqrt(2.0 * dfloat(%pi)))),
 x:signum(random()) * random(alpha)
);
```
