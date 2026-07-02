---
title: "Connectionist temporal classification"
source: https://en.wikipedia.org/wiki/Connectionist_temporal_classification
domain: optical-character-recognition
license: CC-BY-SA-4.0
tags: optical character recognition, text digitization, handwriting recognition, document text extraction, scanned page reading
fetched: 2026-07-02
---

# Connectionist temporal classification

**Connectionist temporal classification** (**CTC**) is a loss function and output representation used to train neural networks on sequence-labelling tasks where the input and output are not aligned in time. It can be used for tasks like on-line handwriting recognition or speech recognition. CTC refers to the outputs and scoring, and is independent of the underlying neural network structure. It was introduced in 2006.

The input is a sequence of observations, and the outputs are a sequence of labels, which can include blank outputs. The difficulty of training comes from there being many more observations than there are labels. For example, in speech audio there can be multiple time slices which correspond to a single phoneme. Since we don't know the alignment of the observed sequence with the target labels we predict a probability distribution at each time step. A CTC network has a continuous output (e.g. softmax), which is fitted through training to model the probability of a label. CTC does not attempt to learn boundaries and timings: Label sequences are considered equivalent if they differ only in alignment, ignoring blanks. Equivalent label sequences can occur in many ways – which makes scoring a non-trivial task, but there is an efficient forward–backward algorithm for that.

CTC scores can then be used with the back-propagation algorithm to update the neural network weights.

Alternative approaches to a CTC-fitted neural network include a hidden Markov model (HMM).

In 2009, a Connectionist Temporal Classification (CTC)-trained LSTM network was the first RNN to win pattern recognition contests when it won several competitions in connected handwriting recognition.

In 2014, the Chinese company Baidu used a bidirectional RNN (not an LSTM) trained on the CTC loss function to break the 2S09 Switchboard Hub5'00 speech recognition dataset benchmark without using any traditional speech processing methods.

In 2015, it was used in Google voice search and dictation on Android devices.

CTC is limited to monotonic alignment, which is not a problem for voice recognition, but may be a problem for language translation, as later words in a language A may correspond to earlier words in language B, since the word ordering is different for different languages.
