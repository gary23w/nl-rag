---
title: "Transformer (deep learning) (part 2/2)"
source: https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)
domain: machine-learning
license: CC-BY-SA-4.0
tags: machine learning, neural network, llm, embedding, transformer model, gradient descent
fetched: 2026-07-02
part: 2/2
---

## Subsequent work

### Alternative activation functions

The original transformer uses ReLU activation function. Other activation functions were developed. The Llama series and PaLM used SwiGLU; both GPT-1 and BERT used GELU.

Alternative activation functions are often used in combination with Gated Linear Units in the feedforward module.

### Alternative normalizations

The normalization used in the transformer can be different from LayerNorm. One example is RMSNorm which is used in the Llama series. Other examples include ScaleNorm and FixNorm.

### Alternative positional encodings

Transformers may use other positional encoding methods than sinusoidal.

The original transformer paper reported using a learned positional encoding, but finding it not superior to the sinusoidal one. Later, found that causal masking itself provides enough signal to a transformer decoder that it can learn to implicitly perform absolute positional encoding without the positional encoding module.

#### RoPE

RoPE (rotary positional embedding), is best explained by considering a list of 2-dimensional vectors $[(x_{1}^{(1)},x_{1}^{(2)}),(x_{2}^{(1)},x_{2}^{(2)}),(x_{3}^{(1)},x_{3}^{(2)}),...]$ . Now pick some angle $\theta$ . Then RoPE encoding is ${\text{RoPE}}{\big (}x_{m}^{(1)},x_{m}^{(2)},m{\big )}={\begin{pmatrix}\cos m\theta &-\sin m\theta \\\sin m\theta &\cos m\theta \end{pmatrix}}{\begin{pmatrix}x_{m}^{(1)}\\x_{m}^{(2)}\\\end{pmatrix}}={\begin{pmatrix}x_{m}^{(1)}\cos m\theta -x_{m}^{(2)}\sin m\theta \\x_{m}^{(2)}\cos m\theta +x_{m}^{(1)}\sin m\theta \\\end{pmatrix}}$ Equivalently, if we write the 2-dimensional vectors as complex numbers $z_{m}:=x_{m}^{(1)}+ix_{m}^{(2)}$ , then RoPE encoding is just multiplication by an angle: ${\text{RoPE}}{\big (}z_{m},m{\big )}=e^{im\theta }z_{m}$ For a list of $2n$ -dimensional vectors, a RoPE encoder is defined by a sequence of angles $\theta ^{(1)},...,\theta ^{(n)}$ . Then the RoPE encoding is applied to each pair of coordinates.

The benefit of RoPE is that the dot-product between two vectors depends on their relative location only: ${\text{RoPE}}{\big (}x,m{\big )}^{T}{\text{RoPE}}{\big (}y,n{\big )}={\text{RoPE}}{\big (}x,m+k{\big )}^{T}{\text{RoPE}}{\big (}y,n+k{\big )}$ for any integer k .

#### ALiBi

ALiBi (Attention with Linear Biases) is not a *replacement* for the positional encoder on the original transformer. Instead, it is an *additional* positional encoder that is directly plugged into the attention mechanism. Specifically, the ALiBi attention mechanism is ${\begin{aligned}{\text{Attention}}(Q,K,V)={\text{softmax}}\left({\frac {QK^{\mathrm {T} }}{\sqrt {d_{k}}}}+sB\right)V\end{aligned}}$ Here, s is a real number ("scalar"), and B is the *linear bias* matrix defined by $B={\begin{pmatrix}0&1&2&3&\cdots \\-1&0&1&2&\cdots \\-2&-1&0&1&\cdots \\-3&-2&-1&0&\cdots \\\vdots &\vdots &\vdots &\vdots &\ddots \\\end{pmatrix}}$ in other words, $B_{i,j}=j-i$ . The idea being that the linear bias matrix is a softened mask. Just as 0 represent full attention paid, and $-\infty$ represents no attention paid, the linear bias matrix increases attention paid in one direction and decreases attention paid in the other direction.

ALiBi allows pretraining on short context windows, then fine-tuning on longer context windows. Since it is directly plugged into the attention mechanism, it can be combined with any positional encoder that is plugged into the "bottom" of the entire network (which is where the sinusoidal encoder on the original transformer, as well as RoPE and many others, are located).

#### Relative Position Encodings

Relative Position Encodings is similar to ALiBi, but more generic: ${\begin{aligned}{\text{Attention}}(Q,K,V)={\text{softmax}}\left({\frac {QK^{\mathrm {T} }}{\sqrt {d_{k}}}}+B\right)V\end{aligned}}$ where B is a Toeplitz matrix, that is, $B_{i,j}=B_{i',j'}$ whenever $i-j=i'-j'$ . This is contrasted with the original sinusoidal positional encoding, which is an "absolute positional encoding".

### Efficient implementation

The transformer model has been implemented in standard deep learning frameworks such as TensorFlow and PyTorch. *Transformers* is a library produced by Hugging Face that supplies transformer-based architectures and pretrained models.

#### KV caching

When an autoregressive transformer is used for inference, such as generating text, the query vector is different at each step, but the already-computed key and value vectors are always the same. The **KV caching** method saves the computed key and value vectors at each attention block, so that they are not recomputed at each new token. PagedAttention applies memory paging to KV caching.

If a transformer is used with a baked-in prompt, such as ["You are a customer support agent..."], then the key and value vectors can be computed for the prompt, and saved on disk. The saving in compute is significant when the model is used for many short real-time interactions, such as in online chatbots.

In general, when a user uses an autoregressive transformer to generate a continuation to a sequence of tokens, the model would first perform a forward-pass on this sequence, whereby the KV caches over this sequence are computed. This is called **prefilling**. Hyperscalers serving large Transformer models may use **disaggregated inference**, wherein prefilling and decoding are performed on separately specialized hardware.

#### FlashAttention

FlashAttention is an algorithm that implements the transformer attention mechanism efficiently on a GPU. It is a communication-avoiding algorithm that performs matrix multiplications in blocks, such that each block fits within the cache of a GPU, and by careful management of the blocks it minimizes data copying between GPU caches (as data movement is slow).

The FlashAttention method is a communication-avoiding algorithm that fuses these operations into a single loop, increasing the arithmetic intensity. It is an online algorithm that computes the following quantities: ${\begin{aligned}z_{i}&=q^{T}k_{i}&\\m_{i}&=\max(z_{1},\dots ,z_{i})&={}&\max(m_{i-1},z_{i})\\\ell _{i}&=e^{z_{1}-m_{i}}+\dots +e^{z_{i}-m_{i}}&={}&e^{m_{i-1}-m_{i}}\ell _{i-1}+e^{z_{i}-m_{i}}\\o_{i}&=e^{z_{1}-m_{i}}v_{1}+\dots +e^{z_{i}-m_{i}}v_{i}&={}&e^{m_{i-1}-m_{i}}o_{i-1}+e^{z_{i}-m_{i}}v_{i}\end{aligned}}$ and returns $o_{N}/\ell _{N}$ . In practice, FlashAttention operates over multiple queries and keys per loop iteration, in a similar way as blocked matrix multiplication. If backpropagation is needed, then the output vectors and the intermediate arrays $[m_{1},\dots ,m_{N}],[\ell _{1},\dots ,\ell _{N}]$ are cached, and during the backward pass, attention matrices are rematerialized from these, making it a form of gradient checkpointing.

An improved version, FlashAttention-2, was developed to cater to the rising demand for language models capable of handling longer context lengths. It offers enhancements in work partitioning and parallelism, enabling it to achieve up to 230 TFLOPs/s on A100 GPUs (FP16/BF16), a 2x speed increase over the original FlashAttention.

Key advancements in FlashAttention-2 include the reduction of non-matmul FLOPs, improved parallelism over the sequence length dimension, better work partitioning between GPU warps, and added support for head dimensions up to 256 and multi-query attention (MQA) and grouped-query attention (GQA).

Benchmarks revealed FlashAttention-2 to be up to 2x faster than FlashAttention and up to 9x faster than a standard attention implementation in PyTorch. Future developments include optimization for new hardware like H100 GPUs and new data types like FP8.

FlashAttention-4 focuses on pipelining to increase instruction throughput, and was developed to perform particularly well on Blackwell GPUs.

#### Multi-Query Attention

Multi-Query Attention changes the Multihead Attention mechanism. Whereas normally,

${\text{MultiheadAttention}}(Q,K,V)={\text{Concat}}_{i\in [n_{\text{heads}}]}\left({\text{Attention}}(XW_{i}^{Q},XW_{i}^{K},XW_{i}^{V})\right)W^{O}$ with Multi-Query Attention, there is just one $W^{K},W^{V}$ , thus:

${\text{MultiQueryAttention}}(Q,K,V)={\text{Concat}}_{i\in [n_{\text{heads}}]}\left({\text{Attention}}(XW_{i}^{Q},XW^{K},XW^{V})\right)W^{O}$

This has a neutral effect on model quality and training speed, but increases inference speed.

More generally, grouped-query attention (GQA) partitions attention heads into groups, each of which shares the key-value pair. MQA is GQA with one group, while standard Multihead Attention is GQA with the maximal number of groups.

Multihead Latent Attention (MLA) is a low-rank approximation to standard MHA. Specifically, each hidden vector, before entering the attention mechanism, is first projected to two low-dimensional spaces ("latent space"), one for query and one for key-value (KV vector). This design minimizes the KV cache, as only the low-dimensional KV vector needs to be cached.

#### Speculative decoding

Speculative decoding is a method to accelerate token decoding. Similarly to speculative execution in CPUs, future tokens are computed quickly, then verified. If the quickly computed tokens are incorrect, they are discarded and computed slowly.

The key factor in speculative decoding is that a transformer decoder can verify faster than it can decode, in the following sense.

Suppose we have two transformer models like GPT-3 and GPT-3-small, both with a context window size of 512. To generate an entire context window autoregressively with greedy decoding with GPT-3, it must be run for 512 times, each time generating a token $x_{1},x_{2},...,x_{512}$ , taking time $512T_{\text{GPT-3}}$ . However, if we had some educated guess for the values of these tokens, we could verify all of them in parallel, in one run of the model, by checking that each $x_{t}$ is indeed the token with the largest log-likelihood in the t -th output.

In speculative decoding, a smaller model or some other simple heuristic is used to generate a few speculative tokens that are subsequently verified by the larger model. For example, suppose we use GPT-3-small to generate four speculative tokens: ${\tilde {x}}_{1},{\tilde {x}}_{2},{\tilde {x}}_{3},{\tilde {x}}_{4}$ . This only takes $4T_{\text{GPT-3-small}}$ . These tokens are then run through the larger GPT-3 in one go. Suppose that ${\tilde {x}}_{1}$ and ${\tilde {x}}_{2}$ are verified by GPT-3 as what it would have picked, then those are kept, but ${\tilde {x}}_{3}$ is not, so ${\tilde {x}}_{3},{\tilde {x}}_{4}$ are discarded, and GPT-3 is run on those. This would take $4T_{\text{GPT-3-small}}+3T_{\text{GPT-3}}$ , which might be shorter than $4T_{\text{GPT-3}}$ .

For non-greedy decoding, similar ideas apply, except the speculative tokens are accepted or rejected stochastically, in a way that guarantees the final output distribution is the same as if speculative decoding was not used.

In Multi-Token Prediction, a single forward pass creates a final embedding vector, which then is un-embedded into a token probability. However, that vector can then be further processed by another transformer block to predict the *next* token, and so on for arbitrarily many steps into the future. This trades off accuracy for speed, since each new token costs just one more transformer block, rather than the entire stack.

### Sub-quadratic transformers

Training transformer-based architectures can be expensive, especially for long inputs. Many methods have been developed to attempt to address the issue. In the image domain, Swin transformer is an efficient architecture that performs attention inside shifting windows. In the audio domain, SepTr decouples the attention in time and frequency domains. *Long Range Arena* (2020) is a standard benchmark for comparing the behavior of transformer architectures over long inputs.

#### Alternative attention graphs

The standard attention graph is either all-to-all or causal, both of which scales as $O(N^{2})$ where N is the number of tokens in a sequence.

Reformer (2020) reduces the computational load from $O(N^{2})$ to $O(N\ln N)$ by using locality-sensitive hashing and reversible layers.

Sparse attention uses attention graphs that grows slower than $O(N^{2})$ . For example, BigBird (2020) uses random small-world networks which grows as $O(N)$ .

Ordinary transformers require a memory size that is quadratic in the size of the context window. Attention-free transformers reduce this to a linear dependence while still retaining the advantages of a transformer by linking the key to the value.

#### Random Feature Attention

Random Feature Attention (2021) uses Fourier random features: $\varphi (x)={\frac {1}{\sqrt {D}}}[\cos \langle w_{1},x\rangle ,\sin \langle w_{1},x\rangle ,\cdots \cos \langle w_{D},x\rangle ,\sin \langle w_{D},x\rangle ]^{T}$ where $w_{1},...,w_{D}$ are independent samples from the normal distribution $N(0,\sigma ^{2}I)$ . This choice of parameters satisfy $\mathbb {E} [\langle \varphi (x),\varphi (y)\rangle ]=e^{-{\frac {\|x-y\|^{2}}{2\sigma ^{2}}}}$ , or $e^{\langle x,y\rangle /\sigma ^{2}}=\mathbb {E} [\langle e^{\|x\|^{2}/2\sigma ^{2}}\varphi (x),e^{\|y\|^{2}/2\sigma ^{2}}\varphi (y)\rangle ]\approx \langle e^{\|x\|^{2}/2\sigma ^{2}}\varphi (x),e^{\|y\|^{2}/2\sigma ^{2}}\varphi (y)\rangle$ Consequently, the one-headed attention, with one query, can be written as ${\text{Attention}}(q,K,V)={\text{softmax}}\left({\frac {qK^{\mathrm {T} }}{\sqrt {d_{k}}}}\right)V\approx {\frac {\varphi (q)^{T}\sum _{i}e^{\|k_{i}\|^{2}/2\sigma ^{2}}\varphi (k_{i})v_{i}^{T}}{\varphi (q)^{T}\sum _{i}e^{\|k_{i}\|^{2}/2\sigma ^{2}}\varphi (k_{i})}}$ where $\sigma =d_{K}^{1/4}$ . Similarly for multiple queries, and for multihead attention.

This approximation can be computed in linear time, as we can compute the matrix $\varphi (k_{i})v_{i}^{T}$ first, then multiply it with the query. In essence, we have managed to obtain a more precise version of ${\text{Attention}}(Q,K,V)={\text{softmax}}\left({\frac {QK^{\mathrm {T} }}{\sqrt {d_{k}}}}\right)V\approx Q(K^{T}V/{\sqrt {d_{k}}})$ Performer (2022) uses the same Random Feature Attention, but $w_{1},...,w_{D}$ are first independently sampled from the normal distribution $N(0,\sigma ^{2}I)$ , then they are Gram–Schmidt processed.

### Multimodality

Transformers can also be used/adapted for modalities (input or output) beyond just text, usually by finding a way to "tokenize" the modality.

Multimodal models can either be trained from scratch, or by finetuning. A 2022 study found that transformers pretrained only on natural language can be finetuned on only 0.03% of parameters and become competitive with LSTMs on a variety of logical and visual tasks, demonstrating transfer learning. The LLaVA was a vision-language model composed of a language model (Vicuna-13B) and a vision model (ViT-L/14), connected by a linear layer. Only the linear layer is finetuned.

Vision transformers adapt the transformer to computer vision by breaking down input images as a series of patches, turning them into vectors, and treating them like embedding vector of tokens in a standard transformer.

Conformer and later Whisper follow the same pattern for speech recognition, first turning the speech signal into a spectrogram, which is then treated like an image, i.e. broken down into a series of patches, turned into vectors and treated like embedding vector of tokens in a standard transformer.

Perceivers are a variant of transformers designed for multimodality.

For image generation, notable architectures are DALL-E 1 (2021), Parti (2022), Phenaki (2023), and Muse (2023). Unlike later models, DALL-E is not a diffusion model. Instead, it uses a decoder-only transformer that autoregressively generates a text, followed by the token representation of an image, which is then converted by a variational autoencoder to an image. Parti is an encoder–decoder transformer, where the encoder processes a text prompt, and the decoder generates a token representation of an image. Muse is an encoder-only transformer that is trained to predict masked image tokens from unmasked image tokens. During generation, all input tokens are masked, and the highest-confidence predictions are included for the next iteration, until all tokens are predicted. Phenaki is a text-to-video model. It is a bidirectional masked transformer conditioned on pre-computed text tokens. The generated tokens are then decoded to a video.


## Applications

The transformer has had great success in natural language processing (NLP). Many large language models such as GPT-2, GPT-3, GPT-4, Gemini, AlbertAGPT, Claude, BERT, Grok, XLNet, RoBERTa and ChatGPT demonstrate the ability of transformers to perform a wide variety of NLP-related subtasks and their related real-world applications, including:

- machine translation
- time series prediction
- document summarization
- document generation
- named entity recognition (NER)
- writing computer code based on requirements expressed in natural language.
- speech-to-text

Beyond traditional NLP, the transformer architecture has had success in other applications, such as:

- biological sequence analysis
- video understanding
- protein folding (such as AlphaFold)
- evaluating chess board positions. Using static evaluation alone (that is, with no Minimax search) transformer achieved an Elo of 2895, putting it at grandmaster level.
