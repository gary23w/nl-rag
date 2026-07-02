---
title: "Simple random sample"
source: https://en.wikipedia.org/wiki/Simple_random_sample
domain: reservoir-sampling
license: CC-BY-SA-4.0
tags: reservoir sampling, streaming algorithm, simple random sample, online algorithm
fetched: 2026-07-02
---

# Simple random sample

In statistics, a **simple random sample** (or **SRS**) is a subset of individuals (a sample) chosen from a larger set (a population) in which a subset of individuals are chosen randomly, all with the same probability. It is a process of selecting a sample in a random way. In SRS, each subset of *k* individuals has the same probability of being chosen for the sample as any other subset of *k* individuals. Simple random sampling is a basic type of sampling and can be a component of other more complex sampling methods.

## Introduction

The principle of simple random sampling is that every set with the same number of items has the same probability of being chosen. For example, suppose 10 college students want a ticket for a basketball game, but there are only six tickets available to them, so they decide to have a fair way to see who gets to go. Then, everybody is given a number in the range from 1 to 10, and random numbers are generated, either electronically or from a table of random numbers. Numbers outside the range from 1 to 10 are ignored, as are any numbers previously selected. The first six numbers would identify the lucky ticket winners.

In small populations and often in large ones, such sampling is typically done "**without replacement**", i.e., one deliberately avoids choosing any member of the population more than once. Although simple random sampling can be conducted with replacement instead, this is less common and would normally be described more fully as simple random sampling **with replacement**. Sampling done without replacement is no longer independent, but still satisfies exchangeability, hence most results of mathematical statistics still hold. Further, for a small sample from a large population, sampling without replacement is approximately the same as sampling with replacement, since the probability of choosing the same individual twice is low. Survey methodology textbooks generally consider simple random sampling without replacement as the benchmark to compute the relative efficiency of other sampling approaches.

An unbiased random selection of individuals is important so that if many samples were drawn, the average sample would accurately represent the population. However, this does not guarantee that a particular sample is a perfect representation of the population. Simple random sampling merely allows one to draw externally valid conclusions about the entire population based on the sample. The concept can be extended when the population is a geographic area. In this case, area sampling frames are relevant.

Conceptually, simple random sampling is the simplest of the probability sampling techniques. It requires a complete sampling frame, which may not be available or feasible to construct for large populations. Even if a complete frame is available, more efficient approaches may be possible if other useful information is available about the units in the population.

Advantages are that it is free of classification error, and it requires minimum previous knowledge of the population other than the frame. Its simplicity also makes it relatively easy to interpret data collected in this manner. For these reasons, simple random sampling best suits situations where not much information is available about the population and data collection can be efficiently conducted on randomly distributed items, or where the cost of sampling is small enough to make efficiency less important than simplicity. If these conditions do not hold, stratified sampling or cluster sampling may be a better choice.

## Relationship between simple random sample and other methods

### Equal probability sampling (epsem)

A sampling method for which each individual unit has the same chance of being selected is called **equal probability sampling** (epsem for short).

Using a simple random sample will always lead to an epsem, but not all epsem samples are SRS. For example, if a teacher has a class arranged in 5 rows of 6 columns and she wants to take a random sample of 5 students she might pick one of the 6 columns at random. This would be an epsem sample but not all subsets of 5 pupils are equally likely here, as only the subsets that are arranged as a single column are eligible for selection. There are also ways of constructing multistage sampling, that are not srs, while the final sample will be epsem. For example, systematic random sampling produces a sample for which each individual unit has the same probability of inclusion, but different sets of units have different probabilities of being selected.

Samples that are epsem are **self weighting**, meaning that the inverse of selection probability for each sample is equal.

### Distinction between a systematic random sample and a simple random sample

Consider a school with 1000 students, and suppose that a researcher wants to select 100 of them for further study. All their names might be put in a bucket and then 100 names might be pulled out. Not only does each person have an equal chance of being selected, we can also easily calculate the probability (*P*) of a given person being chosen, since we know the sample size (*n*) and the population (*N*):

1. In the case that any given person can only be selected once (i.e., after selection a person is removed from the selection pool):

${\begin{aligned}P&=1-{\frac {N-1}{N}}\cdot {\frac {N-2}{N-1}}\cdot \cdots \cdot {\frac {N-n}{N-(n-1)}}\\[8pt]&{\stackrel {\text{Canceling:}}{=}}1-{\frac {N-n}{N}}\\[8pt]&={\frac {n}{N}}\\[8pt]&={\frac {100}{1000}}\\[8pt]&=10\%\end{aligned}}$

2. In the case that any selected person is returned to the selection pool (i.e., can be picked more than once):

$P=1-\left(1-{\frac {1}{N}}\right)^{n}=1-\left({\frac {999}{1000}}\right)^{100}=0.0952\dots \approx 9.5\%$

This means that every student in the school has in any case approximately a 1 in 10 chance of being selected using this method. Further, any combination of 100 students has the same probability of selection.

If a systematic pattern is introduced into random sampling, it is referred to as "systematic (random) sampling". An example would be if the students in the school had numbers attached to their names ranging from 0001 to 1000, and we chose a random starting point, e.g. 0533, and then picked every 10th name thereafter to give us our sample of 100 (starting over with 0003 after reaching 0993). In this sense, this technique is similar to cluster sampling, since the choice of the first unit will determine the remainder. This is no longer simple random sampling, because some combinations of 100 students have a larger selection probability than others – for instance, {3, 13, 23, ..., 993} has a 1/10 chance of selection, while {1, 2, 3, ..., 100} cannot be selected under this method.

## Sampling a dichotomous population

If the members of the population come in three kinds, say "blue", "red" and "black", the number of red elements in a sample of given size will vary by sample and hence is a random variable whose distribution can be studied. That distribution depends on the numbers of red and black elements in the full population. For a simple random sample *with* replacement, the distribution is a *binomial distribution*. For a simple random sample *without* replacement, one obtains a *hypergeometric distribution*.

## Algorithms

Several efficient algorithms for simple random sampling have been developed. A naive algorithm is the draw-by-draw algorithm where at each step we remove the item at that step from the set with equal probability and put the item in the sample. We continue until we have a sample of desired size k . The drawback of this method is that it requires random access in the set.

The selection-rejection algorithm developed by Fan et al. in 1962 requires a single pass over data; however, it is a sequential algorithm and requires knowledge of total count of items n , which is not available in streaming scenarios.

A very simple random sort algorithm was proved by Sunter in 1977. The algorithm simply assigns a random number drawn from uniform distribution $(0,1)$ as a key to each item, then sorts all items using the key and selects the smallest k items.

J. Vitter in 1985 proposed reservoir sampling algorithms, which are widely used. This algorithm does not require knowledge of the size of the population n in advance, and uses constant space.

Random sampling can also be accelerated by sampling from the distribution of gaps between samples and skipping over the gaps.
