---
title: "Perplexity"
source: https://en.wikipedia.org/wiki/Perplexity
domain: t-sne-embedding
license: CC-BY-SA-4.0
tags: t sne embedding, stochastic neighbor embedding, high dimensional visualization, nonlinear projection
fetched: 2026-07-02
---

# Perplexity

In information theory, **perplexity** is a measure of uncertainty for a discrete probability distribution. The perplexity of a fair coin toss is 2, and that of a fair die roll is 6; and generally, for a probability distribution with exactly N outcomes each having a probability of exactly 1 / *N*, the perplexity is simply N. But perplexity can also be applied to unfair dice, and to other non-uniform probability distributions. It can be defined as the exponentiation of the information entropy. The larger the perplexity, the less likely it is that an observer can guess the value which will be drawn from the distribution.

Perplexity was originally introduced in 1977 in the context of speech recognition by Frederick Jelinek, Robert Leroy Mercer, Lalit R. Bahl, and James K. Baker.

## Perplexity of a probability distribution

The perplexity PP of a discrete probability distribution p is a concept widely used in information theory, machine learning, and statistical modeling. It is defined as $\mathrm {PP} (p)=\prod _{x}p(x)^{-p(x)}=b^{-\sum _{x}p(x)\log _{b}p(x)},$ where x ranges over the events, where 0−0 is defined to be 1, and where the value of b does not affect the result; b can be chosen to be 2, 10, e, or any other positive value other than 1. In some contexts, this measure is also referred to as the *(order-1 true) diversity*.

The logarithm log PP(*p*) is the entropy of the distribution; it is given the unit shannon (bit) if the base of the logarithm is 2, and nat if the natural logarithm is used.

Perplexity of a random variable X may be defined as the perplexity of the distribution over its possible values x. It can be thought of as a measure of uncertainty or "surprise" related to the outcomes.

For a probability distribution p where exactly k outcomes each have a probability of 1 / *k* and all other outcomes have a probability of zero, the perplexity of this distribution is simply k. This is because the distribution models a fair k-sided die, with each of the k outcomes being equally likely. In this context, the perplexity k indicates that there is as much uncertainty as there would be when rolling a fair k-sided die. Even if a random variable has more than k possible outcomes, the perplexity will still be k if the distribution is uniform over k outcomes and zero for the rest. Thus, a random variable with a perplexity of k can be described as being "k-ways perplexed", meaning it has the same level of uncertainty as a fair k-sided die.

Perplexity is sometimes used as a measure of the difficulty of a prediction problem. It is, however, generally not a straightforward representation of the relevant probability. For example, if you have two choices, one with probability 0.9, your probability of a correct guess using the optimal strategy is 0.9. Yet, the perplexity is 0.9−0.9 0.1−0.1 = 1.38. The inverse of the perplexity, 1/1.38 = 0.72, is not equal to the probability 0.9.

The perplexity is the exponentiation of the entropy, a more commonly encountered quantity. Entropy measures the expected or "average" number of bits required to encode the outcome of the random variable using an optimal variable-length code. It can also be regarded as the expected information gain from learning the outcome of the random variable, providing insight into the uncertainty and complexity of the underlying probability distribution.

## Perplexity of a probability model

A model of an unknown probability distribution p may be proposed based on a training sample that was drawn from p. Given a proposed probability model q, one may evaluate q by asking how well it predicts a separate test sample *x*1, *x*2, ..., *x**N* also drawn from p. The perplexity of the model q is defined as $b^{-{\frac {1}{N}}\sum _{i=1}^{N}\log _{b}q(x_{i})}=\left(\prod _{i}q(x_{i})\right)^{-1/N},$ where b is customarily 2. Better models q of the unknown distribution p will tend to assign higher probabilities *q*(*x**i*) to the test events. Thus, they have lower perplexity because they are less surprised by the test sample. This is equivalent to saying that better models have higher likelihoods for the test data, which leads to a lower perplexity value.

The exponent, ${\textstyle -{\frac {1}{N}}\sum _{i=1}^{N}\log _{b}q(x_{i})}$ , with *b* = 2, may be regarded as the average number of bits needed to represent a test event *x**i* if one uses an optimal code based on q. Low-perplexity models do a better job of compressing the test sample, requiring few bits per test element on average because *q*(*x**i*) tends to be high.

The exponent may also be interpreted as a cross-entropy: $H({\tilde {p}},q)=-\sum _{x}{\tilde {p}}(x)\log _{b}q(x),$ where ~*p* denotes the empirical distribution of the test sample (i.e., ~*p*(*x*) = *n*/*N* if x appeared n times in the test sample of size N).

By the definition of KL divergence, it is also equal to *H*(~*p*) + *D*KL(~*p* || *q*), which is ≥ *H*(~*p*). Consequently, the perplexity is minimized when *q* = ~*p*.

## Token-normalized perplexity

In natural language processing (NLP), a corpus is a structured collection of texts or documents, and a language model is a probability distribution over entire texts or documents. Consequently, in NLP, the more commonly used measure is **token-normalized perplexity** (a token being a word or, more frequently, sub-word), defined as: $\left(\prod _{i=1}^{n}q(s_{i})\right)^{-1/N}$ where *s*1, ..., *s**n* are the *n* documents in the corpus and *N* is the number of *tokens* in the corpus. This normalizes the perplexity by the length of the text, allowing for more meaningful comparisons between different texts or models rather than documents.

Suppose the average text *x**i* in the corpus has a probability of 2−190 according to the language model. This would give a model perplexity of 2190 for a sentence. However, in NLP, it is more common to normalize by the length of a text. Thus, if the test sample has a length of 1000 tokens, and could be coded using 7.95 bits per token, one could report a model perplexity of token of 27.95 = 247. In other words, the model is as confused on test data as if it had to choose uniformly and independently among 247 possibilities for each token.

There are two standard evaluation metrics for language models: perplexity or word error rate (WER). The simpler of these measures, WER, is simply the percentage of erroneously recognized words *E* (deletions, insertions, substitutions) to total number of words *N*, in a speech recognition task i.e. $\mathrm {WER} =\left({\frac {E}{N}}\right)$

The second metric, perplexity (of a token), is an information theoretic measure that evaluates the similarity of proposed model m to the original distribution p. It can be computed as a inverse of (geometric) average probability of test set T $\mathrm {PPL} (D)={\sqrt[{N}]{\frac {1}{m(T)}}}=2^{-{\frac {1}{N}}\log _{2}\left(m(T)\right)},$ where N is the number of tokens in test set T. This equation can be seen as the exponentiated cross entropy, where cross entropy *H*(*p*; *m*) is approximated as $H(p;m)=-{\frac {1}{N}}\log _{2}\left(m(T)\right).$

### Recent advances in language modeling

Since 2007, significant advancements in language modeling have emerged, particularly with the advent of deep learning techniques. Token-normalized perplexity, a measure that quantifies the predictive power of a language model, has remained central to evaluating models such as the dominant transformer models like Google's BERT, OpenAI's GPT-4 and other large language models (LLMs).

This measure was employed to compare different models on the same dataset and guide the optimization of hyperparameters, although it has been found sensitive to factors such as linguistic features and sentence length.

Despite its pivotal role in language model development, perplexity has shown limitations, particularly as an inadequate predictor of speech recognition performance, overfitting and generalization, raising questions about the benefits of blindly optimizing perplexity alone.

### Brown Corpus

The lowest perplexity that had been published on the Brown Corpus (1 million words of American English of varying topics and genres) as of 1992 is indeed about 247 per word/token, corresponding to a cross-entropy of log2 247 = 7.95 bits per word or 1.75 bits per letter using a trigram model. While this figure represented the state of the art (SOTA) at the time, advancements in techniques such as deep learning have led to significant improvements in perplexity on other benchmarks, such as the One Billion Word Benchmark.

In the context of the Brown Corpus, simply guessing that the next word is "the" will achieve an accuracy of 7%, contrasting with the 1/247 = 0.4% that might be expected from a naive use of perplexity. This difference underscores the importance of the statistical model used and the nuanced nature of perplexity as a measure of predictiveness. The guess is based on unigram statistics, not on the trigram statistics that yielded the perplexity of 247, and utilizing trigram statistics would further refine the prediction.
