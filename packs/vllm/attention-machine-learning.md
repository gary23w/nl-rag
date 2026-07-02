---
title: "Attention (machine learning)"
source: https://en.wikipedia.org/wiki/Attention_(machine_learning)
domain: vllm
license: CC-BY-SA-4.0
tags: vllm engine, llm inference, paged attention, throughput serving, gpu batching
fetched: 2026-07-02
---

# Attention (machine learning)

In machine learning, **attention** is a method that determines the importance of each component in a sequence relative to the other components in that sequence. In natural language processing, importance is represented by "soft" weights assigned to each word in a sentence. More generally, attention encodes vectors called token embeddings across a fixed-width sequence that can range from tens to millions of tokens in size.

Unlike "hard" weights, which are computed during the backwards training pass, "soft" weights exist only in the forward pass and therefore change with every step of the input. Earlier designs implemented the attention mechanism in a serial recurrent neural network (RNN) language translation system, but a more recent design, namely the transformer, removed the slower sequential RNN and relied more heavily on the faster parallel attention scheme.

Inspired by ideas about attention in humans, the attention mechanism was developed to address the weaknesses of using information from the hidden layers of recurrent neural networks. Recurrent neural networks favor information contained in words at the end of a sentence and thus deemed more recent, thereby tending to attenuate the significance and associated predictive weight assigned to information earlier in the sentence. Attention allows a token equal access to any part of a sentence directly, rather than only through the previous state.

## History

| 1950s–1960s | Psychology and biology of attention. Cocktail party effect — focusing on content by filtering out background noise. Filter model of attention, partial report paradigm, and saccade control. |
|---|---|
| 1980s | Sigma-pi units, higher-order neural networks. |
| 1990s | *Fast weight controllers* and dynamic links between neurons, anticipating key-value mechanisms in attention. |
| 1998 | The bilateral filter was introduced in image processing. It uses pairwise affinity matrices to propagate relevance across elements. |
| 2005 | Non-local means extended affinity-based filtering in image denoising, using Gaussian similarity kernels as fixed attention-like weights. |
| 2014 | seq2seq with RNN + Attention. Attention was introduced to enhance RNN encoder-decoder translation, particularly for long sentences. See Overview section. Attentional Neural Networks introduced a learned feature selection mechanism using top-down cognitive modulation, showing how attention weights can highlight relevant inputs. |
| 2015 | Attention was extended to vision for image captioning tasks. |
| 2016 | Self-attention was integrated into RNN-based models to capture intra-sequence dependencies. Self-attention was explored in decomposable attention models for natural language inference and structured self-attentive sentence embeddings. |
| 2017 | The Transformer architecture introduced in the research paper Attention is All You Need formalized scaled dot-product self-attention: $A={\text{softmax}}\left({\frac {QK^{T}}{\sqrt {d_{k}}}}\right)V$ Relation networks and set Transformers applied attention to unordered sets and relational reasoning, generalizing pairwise interaction models. |
| 2018 | Non-local neural networks extended attention to computer vision by capturing long-range dependencies in space and time. Graph attention networks applied attention mechanisms to graph-structured data. |
| 2019–2020 | Efficient Transformers, including Reformer, Linformer, and Performer, introduced scalable approximations of attention for long sequences. |
| 2019+ | Hopfield networks were reinterpreted as associative memory-based attention systems, and vision transformers (ViTs) achieved competitive results in image classification. Transformers were adopted across scientific domains, including AlphaFold for protein folding, CLIP for vision-language pretraining, and attention-based dense segmentation models like CCNet and DANet. |

Additional surveys of the attention mechanism in deep learning are provided by Niu et al. and Soydaner.

The major breakthrough came with self-attention, where each element in the input sequence attends to all others, enabling the model to capture global dependencies. This idea was central to the Transformer architecture, which replaced recurrence with attention mechanisms. As a result, Transformers became the foundation for models like BERT, T5 and generative pre-trained transformers (GPT).

## Overview

The modern era of machine attention was revitalized by grafting an attention mechanism (Fig 1. orange) to an Encoder-Decoder.

|   | (Fig 1. Encoder-decoder with attention.[36] Numerical subscripts (100, 300, 500, 9k, 10k) indicate vector sizes while lettered subscripts i and i − 1 indicate time steps. Pinkish regions in H matrix and w vector are zero values. See Legend for details.)Fig 1. Encoder-decoder with attention. Numerical subscripts (100, 300, 500, 9k, 10k) indicate vector sizes while lettered subscripts i and i − 1 indicate time steps. Pinkish regions in H matrix and w vector are zero values. See Legend for details. Legend Label Description 100 Max. sentence length 300 Embedding size (word dimension) 500 Length of hidden vector 9k, 10k Dictionary size of input & output languages respectively. x, Y 9k and 10k 1-hot dictionary vectors. x → x implemented as a lookup table rather than vector multiplication. Y is the 1-hot maximizer of the linear Decoder layer D; that is, it takes the argmax of D's linear layer output. x 300-long word embedding vector. The vectors are usually pre-calculated from other projects such as GloVe or Word2Vec. h 500-long encoder hidden vector. At each point in time, this vector summarizes all the preceding words before it. The final h can be viewed as a "sentence" vector, or a thought vector as Hinton calls it. s 500-long decoder hidden state vector. E 500 neuron recurrent neural network encoder. 500 outputs. Input count is 800–300 from source embedding + 500 from recurrent connections. The encoder feeds directly into the decoder only to initialize it, but not thereafter; hence, that direct connection is shown very faintly. D 2-layer decoder. The recurrent layer has 500 neurons and the fully-connected linear layer has 10k neurons (the size of the target vocabulary). The linear layer alone has 5 million (500 × 10k) weights – ~10 times more weights than the recurrent layer. score 100-long alignment score w 100-long vector attention weight. These are "soft" weights which changes during the forward pass, in contrast to "hard" neuronal weights that change during the learning phase. A Attention module – this can be a dot product of recurrent states, or the query-key-value fully-connected layers. The output is a 100-long vector w. H 500×100. 100 hidden vectors h concatenated into a matrix c 500-long context vector = H * w. c is a linear combination of h vectors weighted by w. |
|---|---|

Figure 2 shows the internal step-by-step operation of the attention block (A) in Fig 1.

Figure 2. The diagram shows the attention forward pass calculating correlations of the word "that" with other words in "See that girl run." Given the right weights from training, the network should be able to identify "girl" as a highly correlated word. Some things to note:

- This example focuses on the attention of a single word "that". In practice, the attention of each word is calculated in parallel to speed up calculations. Simply changing the lowercase "x" vector to the uppercase "X" matrix will yield the formula for this.
- Softmax scaling qWkT / √100 prevents a high variance in qWkT that would allow a single word to excessively dominate the softmax resulting in attention to only one word, as a discrete hard max would do.
- Notation: the commonly written row-wise softmax formula above assumes that vectors are rows, which runs contrary to the standard math notation of column vectors. More correctly, we should take the transpose of the context vector and use the column-wise softmax, resulting in the more correct form

${\begin{aligned}(XW_{v})^{T}*{[(W_{k}X^{T})*{({\underline {x}}W_{q})^{T}}]_{sm}}\end{aligned}}$

.

### Interpreting attention weights

In translating between languages, alignment is the process of matching words from the source sentence to words of the translated sentence. Networks that perform verbatim translation without regard to word order would show the highest scores along the (dominant) diagonal of the matrix. The off-diagonal dominance shows that the attention mechanism is more nuanced.

Consider an example of translating *I love you* to French. On the first pass through the decoder, 94% of the attention weight is on the first English word *I*, so the network offers the word *je*. On the second pass of the decoder, 88% of the attention weight is on the third English word *you*, so it offers *t'*. On the last pass, 95% of the attention weight is on the second English word *love*, so it offers *aime*.

In the *I love you* example, the second word *love* is aligned with the third word *aime*. Stacking soft row vectors together for *je*, *t'*, and *aime* yields an alignment matrix:

|   | I | love | you |
|---|---|---|---|
| je | 0.94 | 0.02 | 0.04 |
| t' | 0.11 | 0.01 | 0.88 |
| aime | 0.03 | 0.95 | 0.02 |

Sometimes, alignment can be multiple-to-multiple. For example, the English phrase *look it up* corresponds to *cherchez-le*. Thus, "soft" attention weights work better than "hard" attention weights (setting one attention weight to 1, and the others to 0), as we would like the model to make a context vector consisting of a weighted sum of the hidden vectors, rather than "the best one", as there may not be a best hidden vector.

## Variants

Many variants of attention implement soft weights, such as

- fast weight programmers, or fast weight controllers (1992). A "slow" neural network outputs the "fast" weights of another neural network through outer products. The slow network learns by gradient descent. It was later renamed as "linearized self-attention".
- Bahdanau-style attention, also referred to as *additive attention*,
- Luong-style attention, which is known as *multiplicative attention*,
- Early attention mechanisms similar to modern self-attention were proposed using recurrent neural networks. However, the highly parallelizable self-attention was introduced in 2017 and successfully used in the Transformer model,
- *positional attention* and *factorized positional attention*.

For convolutional neural networks, attention mechanisms can be distinguished by the dimension on which they operate, namely: spatial attention, channel attention, or combinations.

These variants recombine the encoder-side inputs to redistribute those effects to each target output. Often, a correlation-style matrix of dot products provides the re-weighting coefficients. In the figures below, W is the matrix of context attention weights, similar to the formula in Overview section above.

| 1. encoder-decoder dot product | 2. encoder-decoder QKV | 3. encoder-only dot product | 4. encoder-only QKV | 5. Pytorch tutorial |
|---|---|---|---|---|
|   |   |   |   |   |

| Label | Description |
|---|---|
| Variables X, H, S, T | Upper case variables represent the entire sentence, and not just the current word. For example, H is a matrix of the encoder hidden state—one word per column. |
| S, T | S, decoder hidden state; T, target word embedding. In the Pytorch Tutorial variant training phase, T alternates between 2 sources depending on the level of teacher forcing used. T could be the embedding of the network's output word; i.e. embedding(argmax(FC output)). Alternatively with teacher forcing, T could be the embedding of the known correct word which can occur with a constant forcing probability, say 1/2. |
| X, H | H, encoder hidden state; X, input word embeddings. |
| W | Attention coefficients |
| Qw, Kw, Vw, FC | Weight matrices for query, key, value respectively. FC is a fully-connected weight matrix. |
| ⊕, ⊗ | ⊕, vector concatenation; ⊗, matrix multiplication. |
| corr | Column-wise softmax(matrix of all combinations of dot products). The dot products are **xi * xj** in variant #3, **hi* s**j in variant 1, and column **i** ( Kw * H ) * column **j** ( Qw * S ) in variant 2, and column **i** ( Kw * X ) * column **j** ( Qw * X ) in variant 4. Variant 5 uses a fully-connected layer to determine the coefficients. If the variant is QKV, then the dot products are normalized by the √d where d is the height of the QKV matrices. |

## Optimizations

### Flash attention

The size of the attention matrix is proportional to the square of the number of input tokens. Therefore, when the input is long, calculating the attention matrix requires a lot of GPU memory. Flash attention is an implementation that reduces the memory needs and increases efficiency without sacrificing accuracy. It achieves this by partitioning the attention computation into smaller blocks that fit into the GPU's faster on-chip memory, reducing the need to store large intermediate matrices and thus lowering memory usage while increasing computational efficiency.

### FlexAttention

FlexAttention is an attention kernel developed by Meta that allows users to modify attention scores prior to softmax and dynamically chooses the optimal attention algorithm.

## Applications

Attention is widely used in natural language processing, computer vision, and speech recognition. In NLP, it improves context understanding in tasks like question answering and summarization. In vision, visual attention helps models focus on relevant image regions, enhancing object detection and image captioning.

### Attention maps as explanations for vision transformers

From the original paper on vision transformers (ViT), visualizing attention scores as a heat map (called saliency maps or attention maps) has become an important and routine way to inspect the decision making process of ViT models. One can compute the attention maps with respect to any attention head at any layer, while the deeper layers tend to show more semantically meaningful visualization. Attention rollout is a recursive algorithm to combine attention scores across all layers, by computing the dot product of successive attention maps.

Because vision transformers are typically trained in a self-supervised manner, attention maps are generally not class-sensitive. When a classification head is attached to the ViT backbone, class-discriminative attention maps (CDAM) combines attention maps and gradients with respect to the class `[CLS]` token. Some class-sensitive interpretability methods originally developed for convolutional neural networks can be also applied to ViT, such as GradCAM, which back-propagates the gradients to the outputs of the final attention layer.

Using attention as basis of explanation for the transformers in language and vision is not without debate. While some pioneering papers analyzed and framed attention scores as explanations, higher attention scores do not always correlate with greater impact on model performances.

## Mathematical representation

### Standard scaled dot-product attention

For matrices: $Q\in \mathbb {R} ^{m\times d_{k}},K\in \mathbb {R} ^{n\times d_{k}}$ and $V\in \mathbb {R} ^{n\times d_{v}}$ , the scaled dot-product, or QKV attention, is defined as: ${\text{Attention}}(Q,K,V)={\text{softmax}}\left({\frac {QK^{T}}{\sqrt {d_{k}}}}\right)V\in \mathbb {R} ^{m\times d_{v}}$ where ${}^{T}$ denotes transpose and the softmax function is applied independently to every row of its argument. The matrix Q contains m queries, while matrices $K,V$ jointly contain an *unordered* set of n key-value pairs. Value vectors in matrix V are weighted using the weights resulting from the softmax operation, so that the rows of the m -by- $d_{v}$ output matrix are confined to the convex hull of the points in $\mathbb {R} ^{d_{v}}$ given by the rows of V .

To understand the permutation invariance and permutation equivariance properties of QKV attention, let $A\in \mathbb {R} ^{m\times m}$ and $B\in \mathbb {R} ^{n\times n}$ be permutation matrices; and $D\in \mathbb {R} ^{m\times n}$ an arbitrary matrix. The softmax function is permutation equivariant in the sense that: ${\text{softmax}}(ADB)=A\,{\text{softmax}}(D)B$ By noting that the transpose of a permutation matrix is also its inverse, it follows that: ${\text{Attention}}(AQ,BK,BV)=A\,{\text{Attention}}(Q,K,V)$ which shows that QKV attention is equivariant with respect to re-ordering the queries (rows of Q ); and invariant to re-ordering of the key-value pairs in $K,V$ . These properties are inherited when applying linear transforms to the inputs and outputs of QKV attention blocks. For example, a simple self-attention function defined as: $X\mapsto {\text{Attention}}(XT_{q},XT_{k},XT_{v})$ is permutation equivariant with respect to re-ordering the rows of the input matrix X in a non-trivial way, because every row of the output is a function of all the rows of the input. Similar properties hold for *multi-head attention*, which is defined below.

### Masked attention

When QKV attention is used as a building block for an autoregressive decoder, and when at training time all input and output matrices have n rows, a masked attention variant is used: ${\text{Attention}}(Q,K,V)={\text{softmax}}\left({\frac {QK^{T}}{\sqrt {d_{k}}}}+M\right)V$ where the mask, $M\in \mathbb {R} ^{n\times n}$ is a strictly upper triangular matrix, with zeros on and below the diagonal and $-\infty$ in every element above the diagonal. The softmax output, also in $\mathbb {R} ^{n\times n}$ is then *lower triangular*, with zeros in all elements above the diagonal. The masking ensures that for all $1\leq i<j\leq n$ , row i of the attention output is independent of row j of any of the three input matrices. The permutation invariance and equivariance properties of standard QKV attention do not hold for the masked variant.

### Multi-head attention

Multi-head attention ${\text{MultiHead}}(Q,K,V)={\text{Concat}}({\text{head}}_{1},...,{\text{head}}_{h})W^{O}$ where each head is computed with QKV attention as: ${\text{head}}_{i}={\text{Attention}}(QW_{i}^{Q},KW_{i}^{K},VW_{i}^{V})$ and $W_{i}^{Q},W_{i}^{K},W_{i}^{V}$ , and $W^{O}$ are parameter matrices.

The permutation properties of (standard, unmasked) QKV attention apply here also. For permutation matrices, $A,B$ : ${\text{MultiHead}}(AQ,BK,BV)=A\,{\text{MultiHead}}(Q,K,V)$ from which we also see that multi-head self-attention: $X\mapsto {\text{MultiHead}}(XT_{q},XT_{k},XT_{v})$ is equivariant with respect to re-ordering of the rows of input matrix X .

### Bahdanau (additive) attention

${\text{Attention}}(Q,K,V)={\text{softmax}}(\tanh(W_{Q}Q+W_{K}K))V$ where $W_{Q}$ and $W_{K}$ are learnable weight matrices.

### Luong attention (general)

${\text{Attention}}(Q,K,V)={\text{softmax}}(QWK^{T})V$ where W is a learnable weight matrix.

### Self-attention

Self-attention is essentially the same as cross-attention, except that query, key, and value vectors all come from the same model. Both encoder and decoder can use self-attention, but with subtle differences.

For encoder self-attention, we can start with a simple encoder without self-attention, such as an "embedding layer", which simply converts each input word into a vector by a fixed lookup table. This gives a sequence of hidden vectors $h_{0},h_{1},\dots$ . These can then be applied to a dot-product attention mechanism, to obtain ${\begin{aligned}h_{0}'&=\mathrm {Attention} (h_{0}W^{Q},HW^{K},HW^{V})\\h_{1}'&=\mathrm {Attention} (h_{1}W^{Q},HW^{K},HW^{V})\\&\;\,\vdots \end{aligned}}$ or more succinctly, $H'=\mathrm {Attention} (HW^{Q},HW^{K},HW^{V})$ . This can be applied repeatedly, to obtain a multilayered encoder. This is the "encoder self-attention", sometimes called the "all-to-all attention", as the vector at every position can attend to every other.

### Masking

For decoder self-attention, all-to-all attention is inappropriate, because during the autoregressive decoding process, the decoder cannot attend to future outputs that has yet to be decoded. This can be solved by forcing the attention weights $w_{ij}=0$ for all $i<j$ , called "causal masking". This attention mechanism is the "causally masked self-attention".
