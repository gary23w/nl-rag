---
title: "Count–min sketch"
source: https://en.wikipedia.org/wiki/Count%E2%80%93min_sketch
domain: streaming-algorithms
license: CC-BY-SA-4.0
tags: streaming algorithm, data stream model, frequency moment, misra gries summary
fetched: 2026-07-02
---

# Count–min sketch

In computing, the **count–min sketch** (**CM sketch**) is a probabilistic data structure that serves as a frequency table of events in a stream of data. It uses hash functions to map events to frequencies, but unlike a hash table uses only sub-linear space, at the expense of overcounting some events due to collisions. The count–min sketch was invented in 2003 by Graham Cormode and S. Muthu Muthukrishnan and described by them in a 2005 paper.

Count–min sketch is an alternative to count sketch and AMS sketch and can be considered an implementation of a counting Bloom filter (Fan et al., 1998) or multistage-filter. However, they are used differently and therefore sized differently: a count–min sketch typically has a sublinear number of cells, related to the desired approximation quality of the sketch, while a counting Bloom filter is more typically sized to match the number of elements in the set.

## Data structure

The goal of the basic version of the count–min sketch is to consume a stream of events, one at a time, and count the frequency of the different types of events in the stream. At any time, the sketch can be queried for the frequency of a particular event type i from a universe of event types ${\mathcal {U}}$ , and will return an estimate of this frequency that is within a certain distance of the true frequency, with a certain probability.

The actual sketch data structure is a two-dimensional array of w columns and d rows. The parameters w and d are fixed when the sketch is created, and determine the time and space needs and the probability of error when the sketch is queried for a frequency or inner product. Associated with each of the d rows is a separate hash function; the hash functions must be pairwise independent. The parameters w and d can be chosen by setting *w* = ⌈*e*/*ε*⌉ and *d* = ⌈ln 1/*δ*⌉, where the error in answering a query is within an additive factor of ε with probability 1 − *δ* (see below), and *e* is Euler's number.

When a new event of type i arrives we update as follows: for each row j of the table, apply the corresponding hash function to obtain a column index *k* = *h**j*(*i*). Then increment the value in row j, column k by one.

### Point Query

The *point query* asks for the count of an event type i. The estimated count is given by the least value in the table for i, namely ${\hat {a}}_{i}=\min _{j}\mathrm {count} [j,h_{j}(i)]$ , where $\mathrm {count}$ is the table.

Obviously, for each i, one has $a_{i}\leq {\hat {a}}_{i}$ , where $a_{i}$ is the true frequency with which i occurred in the stream.

Additionally, this estimate has the guarantee that ${\hat {a}}_{i}\leq a_{i}+\varepsilon N$ with probability $1-\delta$ , where $N=\sum _{i\in {\mathcal {U}}}a_{i}$ is the stream size, i.e. the total number of items seen by the sketch.

### Inner Product

An *inner product query* asks for the inner product between the histograms represented by two count–min sketches, $\mathrm {count} _{a}$ and $\mathrm {count} _{b}$ .

Let ${\widehat {a\cdot b}}_{j}=\sum _{k=0}^{w}\mathrm {count} _{a}[j,k]\cdot \mathrm {count} _{b}[j,k]$ . The inner product can then be estimated as ${\widehat {a\cdot b}}=\min _{j}{\widehat {a\cdot b}}_{j}$ .

One can show that $a\cdot b\leq {\widehat {a\cdot b}}$ , and with probability $1-\delta$ , ${\widehat {a\cdot b}}\leq a\cdot b+\varepsilon ||a||_{1}||b||_{1}$ .

### Merging Streams

Like the count sketch, the Count–min sketch is a linear sketch. That is, given two streams, constructing a sketch on each stream and summing the sketches yields the same result as concatenating the streams and constructing a sketch on the concatenated streams. This makes the sketch mergeable and appropriate for use in distributed settings in addition to streaming ones.

## Reducing bias and error

One potential problem with the usual min estimator for count–min sketches is that they are biased estimators of the true frequency of events: they may overestimate, but never underestimate the true count in a point query. Furthermore, while the min estimator works well when the distribution is highly skewed, other sketches such as the Count sketch based on means are more accurate when the distribution is not sufficiently skewed. Several variations on the sketch have been proposed to reduce error and reduce or eliminate bias.

To remove bias, the `hCount*` estimator repeatedly randomly selects d random entries in the sketch and takes the minimum to obtain an unbiased estimate of the bias and subtracts it off.

A maximum likelihood estimator (MLE) was derived in Ting. By using the MLE, the estimator is always able to match or better the min estimator and works well even if the distribution is not skewed. This paper also showed the hCount* debiasing operation is a bootstrapping procedure that can be efficiently computed without random sampling and can be generalized to any estimator.

Since errors arise from hash collisions with unknown items from the universe, several approaches correct for the collisions when multiple elements of the universe are known or queried for simultaneously . For each of these, a large proportion of the universe must be known to observe a significant benefit.

*Conservative updating* changes the update, but not the query algorithms. To count c instances of event type i, one first computes an estimate ${\hat {a}}_{i}=\min _{j}\mathrm {count} [j,h_{j}(i)]$ , then updates $\mathrm {count} [j,h_{j}(i)]\leftarrow \max\{\mathrm {count} [j,h_{j}(i)],{\hat {a_{i}}}+c\}$ for each row j. While this update procedure makes the sketch not a linear sketch, it is still mergeable.
