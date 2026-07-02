---
title: "Transformer (deep learning) (part 1/2)"
source: https://en.wikipedia.org/wiki/Encoder-decoder_model
domain: machine-translation-nlp
license: CC-BY-SA-4.0
tags: neural machine translation, sequence to sequence translation, cross lingual generation, attention alignment translation, bilingual corpus training
fetched: 2026-07-02
part: 1/2
---

# Transformer (deep learning)

(Redirected from

Encoder-decoder model

)

In deep learning, the **transformer** is a family of artificial neural network architectures based on the multi-head attention mechanism, in which text is converted to numerical representations called tokens, and each token is converted into a vector via lookup from a word embedding table. At each layer, each token is then contextualized within the scope of the context window with other (unmasked) tokens via a parallel multi-head attention mechanism, allowing the signal for key tokens to be amplified and less important tokens to be diminished. Because self-attention alone is permutation-invariant, transformers inject positional information, typically through positional encodings or learned positional embeddings, so token order can affect the output.

Transformers have the advantage of having no recurrent units, therefore requiring less training time than earlier recurrent neural architectures (RNNs) such as long short-term memory (LSTM). Later variations have been widely adopted for training large language models (LLMs) on large (language) datasets. Modern transformer designs are commonly grouped into encoder-only, decoder-only, and encoder-decoder variants, depending on whether they are optimized for representation learning, autoregressive generation, or conditional sequence-to-sequence tasks.

The original version of the transformer architecture was proposed in the 2017 paper "Attention Is All You Need" by researchers at Google. The predecessors of transformers were developed as an improvement over previous architectures for machine translation, but have found many applications since. They are used in large-scale natural language processing, computer vision (vision transformers), reinforcement learning, audio, multimodal learning, robotics, and playing chess. It has also led to the development of pre-trained systems, such as generative pre-trained transformers (GPTs) and BERT (bidirectional encoder representations from transformers).


## History

### Predecessors

For many years, sequence modelling and generation was done by using plain recurrent neural networks (RNNs). A well-cited early example was the Elman network (1990). In theory, the information from one token can propagate arbitrarily far down the sequence, but in practice the vanishing-gradient problem leaves the model's state at the end of a long sentence without precise, extractable information about preceding tokens.

A key breakthrough was LSTM (originally described in a 1995 technical report and formally published in 1997), an RNN that introduced gating mechanisms to mitigate the vanishing gradient problem, allowing efficient learning of long-sequence modelling. One key architectural element was the use of *multiplicative gating units*, in which the outputs of some neurons modulate the outputs of others. These multiplicative units are conceptually distinct from the additive attention mechanism later introduced for sequence-to-sequence models. Neural networks using multiplicative units were later called *sigma-pi networks* or *higher-order networks*. LSTM became the standard architecture for long sequence modelling until the 2017 publication of transformers. However, LSTM still used sequential processing, like most other RNNs. Specifically, RNNs operate one token at a time from first to last; they cannot operate in parallel over all tokens in a sequence.

Modern transformers overcome this problem, but unlike RNNs, they require computation time that is quadratic in the size of the context window. The linearly scaling fast weight controller (1992) learns to compute a weight matrix for further processing depending on the input. One of its two networks has "fast weights" or "dynamic links" (1981). A slow neural network learns by gradient descent to generate keys and values for computing the weight changes of the fast neural network which computes answers to queries. This was later shown to be equivalent to the unnormalized linear transformer.

### Attention with seq2seq

The idea of encoder–decoder sequence transduction had been developed in the early 2010s; commonly cited as the originators that produced seq2seq are two concurrently published papers from 2014.

A 380M-parameter model for machine translation uses two long short-term memories (LSTM). Its architecture consists of two parts. The *encoder* is an LSTM that takes in a sequence of tokens and turns it into a vector. The *decoder* is another LSTM that converts the vector into a sequence of tokens. Similarly, another 130M-parameter model used gated recurrent units (GRU) instead of LSTM. Later research showed that GRUs are neither better nor worse than LSTMs for seq2seq.

These early seq2seq models had no attention mechanism, and the state vector is accessible only after the *last* word of the source text was processed. Although in theory such a vector retains the information about the whole original sentence, in practice the information is poorly preserved. This is because the input is processed sequentially by one recurrent network into a *fixed*-size output vector, which is then processed by another recurrent network into an output. If the input is long, then the output vector would not be able to contain all relevant information, degrading the output. As evidence, reversing the input sentence improved seq2seq translation.

The *RNN search* model introduced an attention mechanism to seq2seq for machine translation to solve the bottleneck problem (of the *fixed-size* output vector), allowing the model to process long-distance dependencies more easily. The name is because it "emulates searching through a source sentence during decoding a translation".

The relative performances were compared between global (that of *RNN search*) and local (sliding window) attention model architectures for machine translation, finding that mixed attention had higher quality than global attention, while local attention reduced translation time.

In 2016, Google Translate was revamped to Google Neural Machine Translation, which replaced the previous model based on statistical machine translation. The new model was a seq2seq model where the encoder and the decoder were both 8 layers of bidirectional LSTM. It took nine months to develop, and it outperformed the statistical approach, which took ten years to develop.

### Parallelizing attention

Seq2seq models with attention (including self-attention) still suffered from the same issue with recurrent networks, which is that they are hard to parallelize, which prevented them from being accelerated on GPUs. In 2016, *decomposable attention* applied a self-attention mechanism to feedforward networks, which are easy to parallelize, and achieved SOTA result in textual entailment with an order of magnitude fewer parameters than LSTMs. One of its authors, Jakob Uszkoreit, suspected that attention *without* recurrence would be sufficient for language translation, thus the title "attention is *all* you need". That hypothesis was against conventional wisdom at the time, and even his father Hans Uszkoreit, a well-known computational linguist, was skeptical. In the same year, self-attention (called *intra-attention or* *intra-sentence attention*) was proposed for LSTMs.

On 2017-06-12, the original (100M-parameter) encoder–decoder transformer model was published in the "Attention is all you need" paper. At the time, the focus of the research was on improving seq2seq for machine translation, by removing its recurrence to process all tokens in parallel, but preserving its dot-product attention mechanism to keep its text processing performance. This led to the introduction of a multi-head attention model that was easier to parallelize due to the use of independent heads and the lack of recurrence. Its parallelizability was an important factor to its widespread use in large neural networks.

### AI boom era

As early as spring 2017, even before the "Attention is all you need" preprint was published, one of the co-authors applied the "decoder-only" variation of the architecture to generate fictitious Wikipedia articles. Transformer architecture is now used alongside many generative models that contribute to the ongoing AI boom.

The "reference implementation" of the original Transformer was written in a TensorFlow library. In language modelling, ELMo (2018) was a bi-directional LSTM that produces contextualized word embeddings, improving upon the line of research from bag of words and word2vec. It was followed by BERT (2018), an encoder-only transformer model. In October 2019, Google started using BERT to process search queries. In 2020, Google Translate replaced the previous RNN-encoder–RNN-decoder model by a transformer-encoder–RNN-decoder model.

Starting in 2018, the OpenAI GPT series of decoder-only transformers became state of the art in natural language generation. At the end of 2022, ChatGPT, a chatbot based on a fine-tuned variant of GPT-3.5, became unexpectedly popular, triggering a boom around large language models.

Transformers have been applied in modalities beyond text. Four days after the publication of "Attention is All You Need", a multimodal transformer architecture, MultiModel, was published by most authors of that paper. Other examples include the vision transformer, speech recognition, robotics, and multimodal. The vision transformer, in turn, stimulated new developments in convolutional neural networks. Image and video generators like DALL-E (2021), Stable Diffusion 3 (2024), and Sora (2024), use transformers to analyse input data (like text prompts) by breaking it down into "tokens" and then calculating the relevance between each token using self-attention, which helps the model understand the context and relationships within the data.


## Training

### Methods for stabilizing training

The plain transformer architecture had difficulty in converging. In the original paper, the authors recommended using learning rate warmup. That is, the learning rate should linearly scale up from 0 to maximal value for the first part of the training (usually recommended to be 2% of the total number of training steps), before decaying again.

A 2020 paper found that using layer normalization *before* (instead of after) multihead attention and feedforward layers stabilizes training, not requiring learning rate warmup. This is the "pre-LN Transformer" and is more commonly used, compared to the original "post-LN Transformer".

### Pretrain-finetune

Transformers typically are first pretrained by self-supervised learning on a large generic dataset, followed by supervised fine-tuning on a small task-specific dataset. The pretrain dataset is typically an unlabeled large corpus, such as The Pile. Tasks for pretraining and fine-tuning commonly include:

- language modeling
- next-sentence prediction
- question answering
- reading comprehension
- sentiment analysis
- paraphrasing

The T5 transformer report documents a large number of natural language pretraining tasks. Some examples are:

- restoring or repairing incomplete or corrupted text. For example, the input, *"Thank you ~~ me to your party ~~ week",* might generate the output, *"Thank you **for inviting** me to your party **last** week".*
- translation between natural languages (machine translation)
- judging the pragmatic acceptability of natural language. For example, the following sentence might be judged "not acceptable", because even though it is syntactically well-formed, it is improbable in ordinary human usage: *The course is jumping well.*

Note that while each of these tasks is trivial or obvious for human native speakers of the language (or languages), they have typically proved challenging for previous generations of machine learning architecture.

### Tasks

In general, there are 3 classes of language modelling tasks: "masked", "autoregressive", and "prefixLM". These classes are independent of a specific modeling architecture such as transformer, but they are often discussed in the context of transformer.

In a masked task, one or more of the tokens is masked out, and the model would produce a probability distribution predicting what the masked-out tokens are based on the context. The loss function for the task is typically sum of log-perplexities for the masked-out tokens: ${\text{Loss}}=-\sum _{t\in {\text{masked tokens}}}\ln({\text{probability of }}t{\text{ conditional on its context}})$ and the model is trained to minimize this loss function. The BERT series of models are trained for masked token prediction and another task.

In an autoregressive task, the entire sequence is masked at first, and the model produces a probability distribution for the first token. Then the first token is revealed and the model predicts the second token, and so on. The loss function for the task is still typically the same. The GPT series of models are trained by autoregressive tasks.

In a prefixLM task, the sequence is divided into two parts. The first part is presented as context, and the model predicts the first token of the second part. Then that would be revealed, and the model predicts the second token, and so on. The loss function for the task is still typically the same. The T5 series of models are trained by prefixLM tasks.

Note that "masked" as in "masked language modelling" is not "masked" as in "masked attention", and "prefixLM" as in "prefix language modeling" is not "prefixLM" as in " prefix language model".


## Architecture

All transformers have the same primary components:

- Tokenizers, which convert text into tokens.
- Embedding layer, which converts tokens and positions of the tokens into vector representations.
- Transformer layers, which carry out repeated transformations on the vector representations, extracting more and more linguistic information. These consist of alternating attention and feedforward layers. There are two major types of transformer layers: encoder layers and decoder layers, with further variants.
- Un-embedding layer, which converts the final vector representations back to a probability distribution over the tokens.

The following description follows exactly the transformer as described in the original paper. There are variants, described in the following section.

By convention, we write all vectors as row vectors. For example, pushing a vector through a linear layer means multiplying it by a weight matrix on the right, as $xW$ .

### Tokenization

As the transformer architecture natively consists of operations over numbers (matrix multiplications, dot products, activation functions) rather than over text, there must first be a mapping from any input text to some numerical representation. This happens in three steps.

First, the input text is treated by a *preprocessor*, which performs both textual transformations and splits the text into coarse-grained segments called *pretokens*. The latter is referred to as *pretokenization*. Second, each pretoken is segmented further into *tokens* by a *tokenizer* that expects to only see pretokens output by its preprocessor. Each token it produces is a string of one or more characters belonging to a finite set of strings called the *vocabulary* V . Third, because the vocabulary is finite and known beforehand, each token can be assigned an integer identifier, and this mapping is applied to the sequence of tokens to represent any input text as a numerical sequence. Since this mapping is bijective, the output side can produce a sequence of integer identifiers which can then be turned back into tokens. After undoing some of the preprocessing, the result is again legible text.

Training a tokenizer (sometimes referred to as *vocabularization*) means finding a suitable vocabulary V , but also learning how to use it, since any given string s of length $|s|$ has $2^{|s|-1}$ hypothetical segmentations, some of which containing segments that are not in the vocabulary. The most important hyperparameter during vocabularization is the *vocabulary size* $|V|$ : when it is small, the learned vocabulary generally consists of characters and smaller strings, and words will be segmented into many tokens. At larger sizes, it becomes affordable to dedicate tokens to full words, although depending on the preprocessor and tokenizer, it is not necessarily the case that large vocabularies will always use the largest token(s) available to segment a word.

Because tokens are not always full words, they may also be referred to as *subwords* and tokenization algorithms may be referred to as *subword tokenizers*. This is also to differentiate these systems from traditional terminology used in older information retrieval and natural language processing systems, where "tokenization" was used to denote what is today called "pretokenization" (very crudely: splitting into words). In tokenizers that produce tokens that are *not* part of the vocabulary, a special token that does belong to the vocabulary is used as a generic stand-in, written as "[UNK]" for "unknown". In principle, any string could be hidden by such an [UNK]. Indeed, in information retrieval, pretokenizers were themselves used as tokenizers (and also called "tokenizers") with a word-level vocabulary that contained an [UNK].

Commonly used subword tokenization algorithms are byte pair encoding (BPE) and the unigram language model (ULM), which each include a vocabularization algorithm and a dedicated segmentation algorithm. There also exist several segmentation algorithms that require no learning and can be applied given a vocabulary (produced by BPE or ULM, for example), like greedily recognising tokens in a pretoken by moving through it left-to-right. Well-known software implementations of subword tokenizers are Hugging Face's `tokenizers` Python package implemented in Rust, and the `sentencepiece` Python package implemented in C++. The latter package is named as such because one of its configuration options allows disabling the built-in pretokenizer, hence effectively making entire sentences a pretoken and thus having the tokenizer see entire sentences, rather than individual words.

### Embedding

Each integer token identifier is converted into an embedding vector via a lookup table. Equivalently stated, it multiplies a one-hot representation of the token identifier by an embedding matrix M . For example, if the input token's identifier is 3 , then the one-hot representation is $[0,0,0,1,0,0,\dots ]$ , and its embedding vector is $\mathrm {Embed} (3)=[0,0,0,1,0,0,\dots ]M$ The token embedding vectors are added to their respective positional encoding vectors (see below), producing the sequence of input vectors.

The dimension of an embedding vector is called *hidden size* or *embedding size* and written as $d_{\text{emb}}$ . This size is written as $d_{\text{model}}$ in the original transformer paper.

### Un-embedding

An un-embedding layer is almost the reverse of an embedding layer. Whereas an embedding layer converts a token identifier into a vector, an un-embedding layer converts a vector into a probability distribution over tokens.

The un-embedding layer is a linear-softmax layer: $\mathrm {UnEmbed} (x)=\mathrm {softmax} (xW+b)$ The matrix has shape $(d_{\text{emb}},|V|)$ . Some architectures use the transpose of the embedding matrix M as the un-embedding matrix W in order to avoid needing double the amount of embedding-related parameters and to avoid divergence during training. This practice is called *weight tying*.

### Positional encoding

A positional encoding is a fixed-size vector representation of the relative positions of tokens within a sequence: it provides the transformer model with information about *where* the words are in the input sequence. This induces a bias towards the order of the input sequence, so that, for example, the input sequence "man bites dog" is processed differently from "dog bites man".

The positional encoding is defined as a function of type $f:\mathbb {R} \to \mathbb {R} ^{d}$ , where d is a positive even integer. The full positional encoding defined in the original paper is: $(f(t)_{2k},f(t)_{2k+1})=(\sin(\theta ),\cos(\theta ))\quad \forall k\in \{0,1,\ldots ,d/2-1\}$ where $\theta ={\frac {t}{r^{k}}},r=N^{2/d}$ .

Here, N is a free parameter that should be significantly larger than the biggest k that would be input into the positional encoding function. The original paper uses $N=10000$ .

The function is in a simpler form when written as a complex function of type $f:\mathbb {R} \to \mathbb {C} ^{d/2}$ $f(t)=\left(e^{it/r^{k}}\right)_{k=0,1,\ldots ,{\frac {d}{2}}-1}$ where $r=N^{2/d}$ .

The main reason for using this positional encoding function is that using it, shifts are linear transformations: $f(t+\Delta t)=\mathrm {diag} (f(\Delta t))f(t)$ where $\Delta t\in \mathbb {R}$ is the distance one wishes to shift. This allows the transformer to take any encoded position, and find the encoding of the position n-steps-ahead or n-steps-behind, by a matrix multiplication.

By taking a linear sum, any convolution can also be implemented as linear transformations: $\sum _{j}c_{j}f(t+\Delta t_{j})=\left(\sum _{j}c_{j}\,\mathrm {diag} (f(\Delta t_{j}))\right)f(t)$ for any constants $c_{j}$ . This allows the transformer to take any encoded position and find a linear sum of the encoded locations of its neighbors. This sum of encoded positions, when fed into the attention mechanism, would create attention weights on its neighbors, much like what happens in a convolutional neural network language model. In the author's words, "we hypothesized it would allow the model to easily learn to attend by relative position."

In typical implementations, all operations are done over the real numbers, not the complex numbers, but since complex multiplication can be implemented as real 2-by-2 matrix multiplication, this is a mere notational difference.

### Encoder–decoder (overview)

Like earlier seq2seq models, the original transformer model used an **encoder–decoder** architecture. The encoder consists of encoding layers that process all the input tokens together one layer after another, while the decoder consists of decoding layers that iteratively process the encoder's output and the decoder's output tokens so far.

The purpose of each encoder layer is to create contextualized representations of the tokens, where each representation corresponds to a token that "mixes" information from other input tokens via self-attention mechanism. Each decoder layer contains two attention sublayers: (1) cross-attention for incorporating the output of encoder (contextualized input token representations), and (2) self-attention for "mixing" information among the input tokens to the decoder (i.e. the tokens generated so far during inference time).

Both the encoder and decoder layers have a feed-forward neural network for additional processing of their outputs and contain residual connections and layer normalization steps. These feed-forward layers contain most of the parameters in a transformer model.

### Feedforward network

The feedforward network (FFN) modules in a transformer are 2-layered multilayer perceptrons: $\mathrm {FFN} (x)=\phi (xW^{(1)}+b^{(1)})W^{(2)}+b^{(2)}$ where $W^{(1)}$ and $W^{(2)}$ are weight matrices and $b^{(1)}$ and $b^{(2)}$ are bias vectors, and $\phi$ is its activation function. The original transformer used ReLU activation.

The number of neurons in the middle layer is called *intermediate size* (GPT), *filter size* (BERT), or *feedforward size* (BERT). It is typically larger than the embedding size. For example, in both GPT-2 series and BERT series, the intermediate size of a model is 4 times its embedding size: $d_{\text{ffn}}=4d_{\text{emb}}$ .

### Scaled dot-product attention

#### Attention head

The attention mechanism used in the transformer architecture are scaled dot-product attention units. For each unit, the transformer model learns three weight matrices: the query weights $W^{Q}$ , the key weights $W^{K}$ , and the value weights $W^{V}$ .

The module takes three sequences, a query sequence, a key sequence, and a value sequence. The query sequence is a sequence of length $\ell _{\text{seq, query}}$ , and each entry is a vector of dimension $d_{\text{emb, query}}$ . Similarly for the key and value sequences.

For each vector $x_{i,{\text{query}}}$ in the query sequence, it is multiplied by a matrix $W^{Q}$ to produce a query vector $q_{i}=x_{i,{\text{query}}}W^{Q}$ . The matrix of all query vectors is the query matrix: $Q=X_{\text{query}}W^{Q}$ Similarly, we construct the key matrix $K=X_{\text{key}}W^{K}$ and the value matrix $V=X_{\text{value}}W^{V}$ .

It is usually the case that all $W^{Q},W^{K},W^{V}$ are square matrices, meaning $d_{\text{emb, query}}=d_{\text{query}}$ , etc.

Attention weights are calculated using the query and key vectors: the attention weight $a_{ij}$ from token i to token j is the dot product between $q_{i}$ and $k_{j}$ . The attention weights are divided by the square root of the dimension of the key vectors, ${\sqrt {d_{k}}}$ , which stabilizes gradients during training, and passed through a softmax which normalizes the weights. The fact that $W^{Q}$ and $W^{K}$ are different matrices allows attention to be non-symmetric: if token i attends to token j (i.e. $q_{i}\cdot k_{j}$ is large), this does not necessarily mean that token j will attend to token i (i.e. $q_{j}\cdot k_{i}$ could be small). The output of the attention unit for token i is the weighted sum of the value vectors of all tokens, weighted by $a_{ij}$ , the attention from token i to each token.

The attention calculation for all tokens can be expressed as one large matrix calculation using the softmax function, which is useful for training due to computational matrix operation optimizations that quickly compute matrix operations. The matrices Q , K and V are defined as the matrices where the i th rows are vectors $q_{i}$ , $k_{i}$ , and $v_{i}$ respectively. Then we can represent the attention as ${\begin{aligned}{\text{Attention}}(Q,K,V)={\text{softmax}}\left({\frac {QK^{\mathrm {T} }}{\sqrt {d_{k}}}}\right)V\end{aligned}}$

where the softmax is applied over each of the rows of the matrix.

The number of dimensions in a query vector is *query size* $d_{\text{query}}$ and similarly for the *key size* $d_{\text{key}}$ and *value size* $d_{\text{value}}$ . The output dimension of an attention head is its *head dimension* $d_{\text{head}}$ . The attention mechanism requires the following three equalities to hold: $\ell _{\text{seq, key}}=\ell _{\text{seq, value}},\;d_{\text{query}}=d_{\text{key}},\;d_{\text{value}}=d_{\text{head}}$ but is otherwise unconstrained.

If the attention head is used in a self-attention fashion, then $X_{\text{query}}=X_{\text{key}}=X_{\text{value}}$ . If the attention head is used in a cross-attention fashion, then usually $X_{\text{query}}\neq X_{\text{key}}=X_{\text{value}}$ . It is theoretically possible for all three to be different, but that is rarely the case in practice.

#### Multihead attention

One set of $\left(W^{Q},W^{K},W^{V}\right)$ matrices is called an *attention head*, and each layer in a transformer model has multiple attention heads. While each attention head attends to the tokens that are relevant to each token, multiple attention heads allow the model to do this for different definitions of "relevance". Specifically, the query and key projection matrices, $W^{Q}$ and $W^{K}$ , which are involved in the attention score computation, defines the "relevance". Meanwhile, the value projection matrix $W^{V}$ , in combination with the part of the output projection matrix $W^{O}$ , determines how the attended tokens influence what information is passed to subsequent layers and ultimately the output logits. In addition, the scope of attention, or the range of token relationships captured by each attention head, can expand as tokens pass through successive layers. This allows the model to capture more complex and long-range dependencies in deeper layers. Many transformer attention heads encode relevance relations that are meaningful to humans. For example, some attention heads can attend mostly to the next word, while others mainly attend from verbs to their direct objects. The computations for each attention head can be performed in parallel, which allows for fast processing. The outputs for the attention layer are concatenated to pass into the feedforward neural network layers.

Concretely, let the multiple attention heads be indexed by i , then we have ${\text{MultiheadAttention}}(Q,K,V)={\text{Concat}}_{i\in [n_{\text{heads}}]}({\text{Attention}}(XW_{i}^{Q},XW_{i}^{K},XW_{i}^{V}))W^{O}$ where the matrix X is the concatenation of word embeddings, and the matrices $W_{i}^{Q},W_{i}^{K},W_{i}^{V}$ are "projection matrices" owned by individual attention head i , and $W^{O}$ is a final projection matrix owned by the whole multihead attention head.

It is theoretically possible for each attention head to have a different head dimension $d_{\text{head}}$ , but that is rarely the case in practice.

As an example, in the smallest GPT-2 model, there are only self-attention mechanisms. It has the following dimensions: $d_{\text{emb}}=768,n_{\text{head}}=12,d_{\text{head}}=64$ Since $12\times 64=768$ , its output projection matrix $W^{O}\in \mathbb {R} ^{(12\times 64)\times 768}$ is a square matrix.

#### Masked attention

The transformer architecture is constructed to calculate output tokens iteratively. Assuming $t=0$ refers to the calculation of the first output token $i=0$ , for step $t>0$ , the output token $i=0$ shall remain constant. This ensures properties of the model similar to autoregressive models. Therefore, at every time step t , the calculation for all outputs i should not have access to tokens at position j for $j>=i$ (as it naturally is the case for time step $t=i$ , when tokens $j>t$ are not yet calculated). This behavior may be accomplished before the softmax stage by adding a mask matrix M that is $-\infty$ at entries where the attention link must be cut, and 0 at other places: ${\begin{aligned}{\text{MaskedAttention}}(Q,K,V)={\text{softmax}}\left(M+{\frac {QK^{\mathrm {T} }}{\sqrt {d_{k}}}}\right)V\end{aligned}}$ The following matrix is commonly used in decoder self-attention modules, called "causal masking": $M_{\text{causal}}={\begin{bmatrix}0&-\infty &-\infty &\dots &-\infty \\0&0&-\infty &\dots &-\infty \\0&0&0&\dots &-\infty \\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\dots &0\end{bmatrix}}$

In words, it means that each token can pay attention to itself, and every token before it, but not any after it. A non-masked attention module can be thought of as a masked attention module where the mask has all entries zero. As an example of an uncommon use of mask matrix, the XLNet considers all masks of the form $PM_{\text{causal}}P^{-1}$ , where P is a random permutation matrix.

### Encoder

An encoder consists of an embedding layer, followed by multiple encoder layers.

Each encoder layer consists of two major components: a self-attention mechanism and a feed-forward layer. It takes an input as a sequence of input vectors, applies the self-attention mechanism, to produce an intermediate sequence of vectors, then applies the feed-forward layer for each vector individually. Schematically, we have: ${\begin{aligned}{\text{given input vectors }}&h_{0},h_{1},\dots \\{\text{combine them into a matrix }}H&={\begin{bmatrix}h_{0}\\h_{1}\\\vdots \end{bmatrix}}\\{\text{EncoderLayer}}(H)&={\begin{bmatrix}{\text{FFN}}({\text{MultiheadAttention}}(H,H,H)_{0})\\{\text{FFN}}({\text{MultiheadAttention}}(H,H,H)_{1})\\\vdots \end{bmatrix}}\\\end{aligned}}$

where ${\text{FFN}}$ stands for "feed-forward network". We can more succinctly write it as ${\text{EncoderLayer}}(H)={\text{FFN}}({\text{MultiheadAttention}}(H,H,H))$ with the implicit convention that the ${\text{FFN}}$ is applied to each row of the matrix individually.

The encoder layers are stacked. The first encoder layer takes the sequence of input vectors from the embedding layer, producing a sequence of vectors. This sequence of vectors is processed by the second encoder, and so on. The output from the final encoder layer is then used by the decoder.

As the encoder processes the entire input all at once, every token can attend to every other token (all-to-all attention), so there is no need for causal masking.

### Decoder

A decoder consists of an embedding layer, followed by multiple decoder layers, followed by an un-embedding layer.

Each decoder consists of three major components: a causally masked self-attention mechanism, a cross-attention mechanism, and a feed-forward neural network. The decoder functions in a similar fashion to the encoder, but an additional attention mechanism is inserted which instead draws relevant information from the encodings generated by the encoders. This mechanism can also be called the *encoder–decoder attention*.

Like the first encoder, the first decoder takes positional information and embeddings of the output sequence as its input, rather than encodings. The transformer must not use the current or future output to predict an output, so the output sequence must be partially masked to prevent this reverse information flow. This allows for autoregressive text generation. For decoding, all-to-all attention is inappropriate, because a token cannot attend to tokens not yet generated. Thus, the self-attention module in the decoder is causally masked.

In contrast, the cross-attention mechanism attends to the output vectors of the encoder, which is computed before the decoder starts decoding. Consequently, there is no need for masking in the cross-attention mechanism.

Schematically, we have: ${\begin{aligned}H'&={\text{MaskedMultiheadAttention}}(H,H,H)\\{\text{DecoderLayer}}(H)&={\text{FFN}}({\text{MultiheadAttention}}(H',H^{E},H^{E}))\end{aligned}}$ where $H^{E}$ is the matrix with rows being the output vectors from the encoder.

The last decoder is followed by a final un-embedding layer to produce the output probabilities over the vocabulary. Then, one of the tokens is sampled according to the probability, and the decoder can be run again to produce the next token, etc., autoregressively generating output text.


## Full transformer architecture

### Sublayers

Each encoder layer contains 2 sublayers: the self-attention and the feedforward network. Each decoder layer contains 3 sublayers: the causally masked self-attention, the cross-attention, and the feedforward network.

The final points of detail are the residual connections and layer normalization, (denoted as "LayerNorm", or "LN" in the following), which while conceptually unnecessary, are necessary for numerical stability and convergence.

The residual connections are introduced to avoid vanishing gradient issues and stabilize the training process. They can be expressed by $x\mapsto F(x)+x$ , where F is a given component of the transformer. Adding the input x can preserve the input information and avoid issues when the gradient of $F(x)$ is close to zero.

Similarly to how the feedforward network modules are applied individually to each vector, the LayerNorm is also applied individually to each vector.

There are two common conventions in use: the *post-LN* and the *pre-LN* convention. In the post-LN convention, the output of each sublayer is $\mathrm {LayerNorm} (x+\mathrm {Sublayer} (x))$ where $\mathrm {Sublayer} (x)$ is the function implemented by the sublayer itself.

In the pre-LN convention, the output of each sublayer is $x+\mathrm {Sublayer} (\mathrm {LayerNorm} (x))$ The original 2017 transformer used the post-LN convention. It was difficult to train and required careful hyperparameter tuning and a "warm-up" in learning rate, where it starts small and gradually increases. The pre-LN convention, proposed several times in 2018, was found to be easier to train, requiring no warm-up, leading to faster convergence.

### Pseudocode

The following is the pseudocode for a standard pre-LN encoder–decoder transformer, adapted from *Formal Algorithms for Transformers*

```
input: Encoder input t_e
       Decoder input t_d
output: Array of probability distributions, with shape (decoder vocabulary size x length(decoder output sequence))

/* encoder */
z_e ← encoder.tokenizer(t_e)

for each t in 1:length(z_e) do
    z_e[t] ← encoder.embedding(z_e[t]) + encoder.positional_embedding(t)

for each l in 1:length(encoder.layers) do
    layer ← encoder.layers[l]

    /* first sublayer */
    z_e_copy ← copy(z_e)
    for each t in 1:length(z_e) do
        z_e[t] ← layer.layer_norm(z_e[t])
    z_e ← layer.multihead_attention(z_e, z_e, z_e)
    for each t in 1:length(z_e) do
        z_e[t] ← z_e[t] + z_e_copy[t]

    /* second sublayer */
    z_e_copy ← copy(z_e)
    for each t in 1:length(z_e) do
        z_e[t] ← layer.layer_norm(z_e[t])
    z_e ← layer.feedforward(z_e)
    for each t in 1:length(z_e) do
        z_e[t] ← z_e[t] + z_e_copy[t]

for each t in 1:length(z_e) do
    z_e[t] ← encoder.final_layer_norm(z_e[t])

/* decoder */
z_d ← decoder.tokenizer(t_d)

for each t in 1:length(z_d) do
    z_d[t] ← decoder.embedding(z_d[t]) + decoder.positional_embedding(t)

for each l in 1:length(decoder.layers) do
        layer ← decoder.layers[l]

        /* first sublayer */
        z_d_copy ← copy(z_d)
        for each t in 1:length(z_d) do
            z_d[t] ← layer.layer_norm(z_d[t])
        z_d ← layer.masked_multihead_attention(z_d, z_d, z_d)
        for each t in 1:length(z_d) do
            z_d[t] ← z_d[t] + z_d_copy[t]

        /* second sublayer */
        z_d_copy ← copy(z_d)
        for each t in 1:length(z_d) do
            z_d[t] ← layer.layer_norm(z_d[t])
        z_d ← layer.multihead_attention(z_d, z_e, z_e) 
       for each t in 1:length(z_d) do
           z_d[t] ← z_d[t] + z_d_copy[t]

        /* third sublayer */
        z_d_copy ← copy(z_d)
        for each t in 1:length(z_d) do
            z_d[t] ← layer.layer_norm(z_d[t])
        z_d ← layer.feedforward(z_d)
        for each t in 1:length(z_d) do
            z_d[t] ← z_d[t] + z_d_copy[t]

z_d ← decoder.final_layer_norm(z_d)

output_distributions ← []
for each t in 1:length(z_d) do
    output_distributions.append(decoder.unembed(z_d[t]))

return output_distributions
```

### Terminology

The transformer architecture, being modular, allows variations. Several common variations are described here.

An "encoder-only" transformer applies the encoder to map an input text into a sequence of vectors that represent the input text. This is usually used for text embedding and representation learning for downstream applications. BERT is encoder-only. They are less often used currently, as they were found to be not significantly better than training an encoder–decoder transformer, then taking just the encoder. They are also referred to as "all-to-all" or "BERT-like".

A "decoder-only" transformer is not literally decoder-only, since without an encoder, the cross-attention mechanism has nothing to attend to. Thus, the decoder layers in a decoder-only transformer is composed of just two sublayers: the causally masked self-attention, and the feedforward network. This is usually used for text generation and instruction following. The models in the GPT series and Chinchilla series are decoder-only. They are also referred to as "autoregressive" or "causal".

An "encoder–decoder" transformer is generally the same as the original transformer, with 2 sublayers per encoder layer and 3 sublayers per decoder layer, etc. They might have minor architectural improvements, such as alternative activation functions, changing the location of normalization, etc. This is also usually used for text generation and instruction following. The models in the T5 series are encoder–decoder.

A "prefixLM" (prefix language model) is a decoder-only architecture, but with prefix masking, which is different from causal masking. Specifically, it has mask of the form $M_{\text{prefixLM}}={\begin{bmatrix}\mathbf {0} &-\infty \\\mathbf {0} &M_{\text{causal}}\end{bmatrix}}$ where the first columns correspond to the "prefix", and the subsequent columns correspond to the autoregressively generated text based on the prefix. They resemble encoder–decoder models, but has less "sparsity". Such models are rarely used, though they are cited as theoretical possibilities and benchmarked comparisons.

There are also mixed seq2seq models. For example, in 2020, Google Translate replaced the previous RNN-encoder–RNN-decoder model with a transformer-encoder–RNN-decoder model, as transformer-based decoders did not appear to significantly increase quality unlike the encoder, while the RNN decoder was much faster.
