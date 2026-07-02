---
title: "Language model"
source: https://en.wikipedia.org/wiki/Language_model
domain: bert-model
license: CC-BY-SA-4.0
tags: bert model, bidirectional transformer, masked language model, pretrained encoder
fetched: 2026-07-02
---

# Language model

A **language model** is a computational model that predicts sequences in natural language. Language models are useful for a variety of tasks, including speech recognition, machine translation, natural language generation (generating more human-like text), optical character recognition, route optimization, handwriting recognition, grammar induction, information retrieval and disaster response.

Large language models (LLMs), currently their most advanced form as of 2026, are predominantly based on transformers trained on larger datasets (frequently using texts scraped from the public internet). They have superseded recurrent neural network-based models, which had previously superseded the purely statistical models, such as the word *n*-gram language model.

## History

Noam Chomsky did pioneering work on language models in the 1950s by developing a theory of formal grammars.

In 1980, statistical approaches were explored and found to be more useful for many purposes than rule-based formal grammars. Discrete representations like word *n*-gram language models, with probabilities for discrete combinations of words, made significant advances.

In the 2000s, continuous representations for words, such as word embeddings, began to replace discrete representations. Typically, the representation is a real-valued vector that encodes a word’s meaning such that words closer in vector space are similar in meaning and common relationships between words, such as plurality or gender, are preserved.

## Pure statistical models

In 1980, the first significant statistical language model was proposed, and during the decade IBM performed 'Shannon-style' experiments, in which potential sources for language modeling improvement were identified by observing and analyzing the performance of human subjects in predicting or correcting text.

### Models based on word *n*-grams

A word *n*-gram language model is a statistical model of language which calculates the probability of the next word in a sequence from a fixed size window of previous words. If one previous word is considered, it is a bigram model; if two words, a trigram model; if *n* − 1 words, an *n*-gram model.

Special tokens are introduced to denote the start and end of a sentence $\langle s\rangle$ and $\langle /s\rangle$ . To prevent a zero probability being assigned to unseen words, the probability of each seen word is slightly lowered to make room for the unseen words in a given corpus. To achieve this, various smoothing methods are used, from simple "add-one" smoothing (assigning a count of 1 to unseen *n*-grams, as an uninformative prior) to more sophisticated techniques, such as Good–Turing discounting or back-off models.

Word *n-*gram models have largely been superseded by recurrent neural network–based models, which in turn have been superseded by Transformer-based models often referred to as large language models.

### Exponential

Maximum entropy language models encode the relationship between a word and the *n*-gram history using feature functions. The equation is

$P(w_{m}\mid w_{1},\ldots ,w_{m-1})={\frac {1}{Z(w_{1},\ldots ,w_{m-1})}}\exp(a^{T}f(w_{1},\ldots ,w_{m}))$

where $Z(w_{1},\ldots ,w_{m-1})$ is the partition function, a is the parameter vector, and $f(w_{1},\ldots ,w_{m})$ is the feature function. In the simplest case, the feature function is just an indicator of the presence of a certain *n*-gram. It is helpful to use a prior on a or some form of regularization.

The log-bilinear model is another example of an exponential language model.

Skip-gram language model is an attempt at overcoming the data sparsity problem that the preceding model (i.e. word *n*-gram language model) faced. Words represented in an embedding vector were not necessarily consecutive anymore, but could leave gaps that are *skipped* over (thus the name "skip-gram").

Formally, a k-skip-n-gram is a length-n subsequence where the components occur at distance at most k from each other.

For example, in the input text:

the rain in Spain falls mainly on the plain

the set of 1-skip-2-grams includes all the bigrams (2-grams), and in addition the subsequences

the in

,

rain Spain

,

in falls

,

Spain mainly

,

falls on

,

mainly the

, and

on plain

.

In skip-gram model, semantic relations between words are represented by linear combinations, capturing a form of compositionality. For example, in some such models, if v is the function that maps a word w to its n-d vector representation, then

$v(\mathrm {king} )-v(\mathrm {male} )+v(\mathrm {female} )\approx v(\mathrm {queen} )$

where ≈ is made precise by stipulating that its right-hand side must be the nearest neighbor of the value of the left-hand side.

## Neural models

### Recurrent neural network

Continuous representations or embeddings of words are produced in recurrent neural network-based language models (known also as *continuous space language models*). Such continuous space embeddings help to alleviate the curse of dimensionality, which is the consequence of the number of possible sequences of words increasing exponentially with the size of the vocabulary, further causing a data sparsity problem. Neural networks avoid this problem by representing words as non-linear combinations of weights in a neural net.

### Large language models

A large language model (LLM) is a neural network trained on a vast amount of text for natural language processing tasks, especially language generation. LLMs can typically generate, summarize, translate, and analyze text in many contexts, and are a foundational technology behind modern chatbots. Biased or inaccurate training data can make an LLM's output less reliable.

LLMs are typically based on transformer architecture. Generative pre-trained transformers (GPTs) are a type of LLM that is pre-trained to predict the next word. GPTs are then often fine-tuned to follow instructions and to behave as assistants.

Benchmark evaluations for LLMs attempt to measure model reasoning, factual accuracy, alignment, and safety.

Although sometimes matching human performance, it is not clear whether they are plausible cognitive models. At least for recurrent neural networks, it has been shown that they sometimes learn patterns that humans do not, but fail to learn patterns that humans typically do.

## Evaluation and benchmarks

Evaluation of the quality of language models is mostly done by comparison to human created sample benchmarks created from typical language-oriented tasks. Other, less established, quality tests examine the intrinsic character of a language model or compare two such models. Since language models are typically intended to be dynamic and to learn from data they see, some proposed models investigate the rate of learning, e.g., through inspection of learning curves.

Various data sets have been developed for use in evaluating language processing systems. These include:

- Massive Multitask Language Understanding (MMLU)
- Corpus of Linguistic Acceptability
- GLUE benchmark
- Microsoft Research Paraphrase Corpus
- Multi-Genre Natural Language Inference
- Question Natural Language Inference
- Quora Question Pairs
- Recognizing Textual Entailment
- Semantic Textual Similarity Benchmark
- SQuAD question answering Test
- Stanford Sentiment Treebank
- Winograd NLI
- BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC, OpenBookQA, NaturalQuestions, TriviaQA, RACE, BIG-bench hard, GSM8k, RealToxicityPrompts, WinoGender, CrowS-Pairs
