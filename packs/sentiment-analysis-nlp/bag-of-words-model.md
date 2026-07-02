---
title: "Bag-of-words model"
source: https://en.wikipedia.org/wiki/Bag-of-words_model
domain: sentiment-analysis-nlp
license: CC-BY-SA-4.0
tags: sentiment analysis, opinion polarity classification, affective text mining, aspect based sentiment, emotion detection text
fetched: 2026-07-02
---

# Bag-of-words model

The **bag-of-words** (**BoW**) **model** is a model of text which uses an unordered collection (a "bag") of words. It is used in natural language processing and information retrieval (IR). It disregards word order (and thus most of syntax or grammar) but captures multiplicity.

The bag-of-words model is commonly used in methods of document classification where, for example, the (frequency of) occurrence of each word is used as a feature for training a classifier. It has also been used for computer vision.

An early reference to "bag of words" in a linguistic context can be found in Zellig Harris's 1954 article on *Distributional Structure*.

## Definition

The following models a text document using bag-of-words. Here are two simple text documents:

```mw
(1) John likes to watch movies. Mary likes movies too.
```

```mw
(2) Mary also likes to watch football games.
```

Based on these two text documents, a list is constructed as follows for each document:

```mw
"John","likes","to","watch","movies","Mary","likes","movies","too"

"Mary","also","likes","to","watch","football","games"
```

Representing each bag-of-words as a JSON object, and attributing to the respective JavaScript variable:

```mw
BoW1 = {"John":1,"likes":2,"to":1,"watch":1,"movies":2,"Mary":1,"too":1};
BoW2 = {"Mary":1,"also":1,"likes":1,"to":1,"watch":1,"football":1,"games":1};
```

Each key is the word, and each value is the number of occurrences of that word in the given text document.

The order of elements is free, so, for example `{"too":1,"Mary":1,"movies":2,"John":1,"watch":1,"likes":2,"to":1}` is also equivalent to *BoW1*. It is also what we expect from a strict *JSON object* representation.

Note: if another document is like a union of these two,

```mw
(3) John likes to watch movies. Mary likes movies too. Mary also likes to watch football games.
```

its JavaScript representation will be:

```mw
BoW3 = {"John":1,"likes":3,"to":2,"watch":2,"movies":2,"Mary":2,"too":1,"also":1,"football":1,"games":1};
```

So, as we see in the bag algebra, the "union" of two documents in the bags-of-words representation is, formally, the disjoint union, summing the multiplicities of each element.

| BoW3 = BoW1 ⨄ BoW2 |   | 1 |
|---|---|---|

### Word order

The BoW representation of a text removes all word ordering. For example, the BoW representation of "man bites dog" and "dog bites man" are the same, so any algorithm that operates with a BoW representation of text must treat them in the same way. Despite this lack of syntax or grammar, BoW representation is fast and may be sufficient for simple tasks that do not require word order. For instance, for document classification, if the words "stocks" "trade" "investors" appears multiple times, then the text is likely a financial report, even though it would be insufficient to distinguish between

> Yesterday, investors were rallying, but today, they are retreating.

and

> Yesterday, investors were retreating, but today, they are rallying.

and so the BoW representation would be insufficient to determine the detailed meaning of the document.

## Implementations

Implementations of the bag-of-words model might involve using frequencies of words in a document to represent its contents. The frequencies can be "normalized" by the inverse of document frequency, or tf–idf. Additionally, for the specific purpose of classification, supervised alternatives have been developed to account for the class label of a document. Lastly, binary (presence/absence or 1/0) weighting is used in place of frequencies for some problems (e.g., this option is implemented in the WEKA machine learning software system).

## Hashing trick

A common alternative to using dictionaries is the hashing trick, where words are mapped directly to indices with a hash function. When using a hash function, no memory is required to store a dictionary. In practice, hashing simplifies the implementation of bag-of-words models and improves scalability. Collisions can occur when two words are hashed to the same index, but this happens infrequently and may function as a form of regularization.
