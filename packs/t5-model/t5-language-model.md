---
title: "T5 (language model)"
source: https://en.wikipedia.org/wiki/T5_(language_model)
domain: t5-model
license: CC-BY-SA-4.0
tags: t5 model, text to text transformer, sequence to sequence model, transfer learning
fetched: 2026-07-02
---

# T5 (language model)

**T5 (Text-to-Text Transfer Transformer)** is a series of large language models developed by Google AI introduced in 2019. Like the original Transformer model, T5 models are encoder-decoder Transformers, where the encoder processes the input text, and the decoder generates the output text.

T5 models are usually pretrained on a massive dataset of text and code, after which they can perform the text-based tasks that are similar to their pretrained tasks. They can also be finetuned to perform other tasks.

T5 models have been employed in various applications, including chatbots, machine translation systems, text summarization tools, code generation, and robotics.

## Training

The original T5 models are pre-trained on the Colossal Clean Crawled Corpus (C4), containing text and code scraped from the internet. This pre-training process enables the models to learn general language understanding and generation abilities. T5 models can then be fine-tuned on specific downstream tasks, adapting their knowledge to perform well in various applications.

The T5 models were pretrained on many tasks, all in the format of `<input text>` -> `<output text>`.

Some examples are:

- restoring corrupted text: `Thank you <X> me to your party <Y> week.` -> `<X> for inviting <Y> last <Z>`, where the `<Z>` means "end of output", and the `<X>` and `<Y>` denote blanks to be filled, called "sentinels" in the original report.
- translation: `translate English to German: That is good.` -> `Das ist gut.`.
- judging the grammatical acceptability of a sentence (CoLA sentence): `The course is jumping well.` -> `not acceptable` .

## Architecture

The T5 series encompasses several models with varying sizes and capabilities, all encoder-decoder Transformers, where the encoder processes the input text, and the decoder generates the output text.

These models are often distinguished by their parameter count, which indicates the complexity and potential capacity of the model. The original paper reported the following 5 models:

T5 properties

Name

Total parameters

Encoder parameters

Decoder parameters

$n_{\text{layer}}$

$d_{\text{model}}$

$d_{\text{ff}}$

$d_{\text{kv}}$

$n_{\text{head}}$

Small

76,956,160

35,330,816

41,625,344

6

512

2048

64

8

Base

247,577,856

109,628,544

137,949,312

12

768

3072

64

12

Large

770,567,168

334,939,648

435,627,520

24

1024

4096

64

16

3B

2,884,497,408

1,240,909,824

1,643,587,584

24

1024

16384

128

32

11B

11,340,220,416

4,864,791,552

6,475,428,864

24

1024

65536

128

128

*The encoder and the decoder have the same shape. So for example, the T5-small has 6 layers in the encoder and 6 layers in the decoder.

In the above table,

- $n_{\text{layer}}$ : Number of layers in the encoder; also, number of layers in the decoder. They always have the same number of layers.
- $n_{\text{head}}$ : Number of attention heads in each attention block.
- $d_{\text{model}}$ : Dimension of the embedding vectors.
- $d_{\text{ff}}$ : Dimension of the feedforward network within each encoder and decoder layer.
- **$d_{\text{kv}}$**: Dimension of the key and value vectors used in the self-attention mechanism.

Note that unlike typical Transformers, the 3B and 11B models do not satisfy $d_{\text{model}}=d_{\text{kv}}n_{\text{head}}$ .

Compared to the original Transformer, it uses a few minor modifications: layer normalization with no additive bias; placing the layer normalization outside the residual path; relative positional embedding.

For all experiments, they used a WordPiece tokenizer, with vocabulary size 32,000. The tokenizer is shared across both the input and output of each model. It was trained on a mixture of English, German, French, and Romanian data from the C4 dataset, at a ratio of 10:1:1:1.

## Variants

Several subsequent models used the T5 architecture, with non-standardized naming conventions used to differentiate them. This section attempts to collect the main ones. An exhaustive list of the variants released by Google Brain is on the GitHub repo for T5X.

Some models are trained from scratch while others are trained by starting with a previous trained model. By default, each model is trained from scratch, except otherwise noted.

- *T5* small, base, large, 3B, 11B (2019): The original models.
- *T5 1.1* small, base, large, XL, XXL: Improved versions of the original T5 series. These have roughly equal parameters. The activation function is GEGLU instead of ReLU. The 3B and the 11B were changed to "XL" and "XXL", and their shapes are changed:

T5 v1.1 properties

Name

Total parameters

Encoder parameters

Decoder parameters

$n_{\text{layer}}$

$d_{\text{model}}$

$d_{\text{ff}}$

$d_{\text{kv}}$

$n_{\text{head}}$

Small

76,961,152

35,332,800

41,628,352

8

512

1024

64

6

Base

247,577,856

109,628,544

137,949,312

12

768

2048

64

12

Large

783,150,080

341,231,104

441,918,976

24

1024

2816

64

16

XL

2,849,757,184

1,223,527,424

1,626,229,760

24

2048

5120

64

32

XXL

11,135,332,352

4,762,310,656

6,373,021,696

24

4096

10240

64

64

- *LM-adapted T5* (2021): a series of models (from small to XXL) that started from checkpoints of the *T5* series, but trained further on 100B additional tokens from C4.
- Switch Transformer (2021): a mixture-of-experts variant of T5, by replacing the feedforward layers in the encoder and decoder blocks with mixture of expert feedforward layers.
- *T0* 3B, 11B (2021): a series of models that started from checkpoints of *LM-adapted T5*, and further trained to perform tasks based only on task instruction (zero-shot). Different entries in the series uses different finetuning data.
- *ByT5* (2021): a byte-level version of T5, trained on mC4 (multilingual C4) dataset. It operates on text encoded as UTF-8 bytes, without tokenizers.
- *Flan-T5-XL* (2022): a model that started with a checkpoint of *T5 XL*, then instruction-tuned on the FLAN dataset.
- *T5X* (2022): a JAX-based re-implementation of the original *T5* codebase. It is **not** a model. The original T5 codebase was implemented in TensorFlow with MeshTF.
- *UL2* 20B (2022): a model with the same architecture as the *T5* series, but scaled up to 20B, and trained with "mixture of denoisers" objective on the C4. It was trained on a TPU cluster by accident, when a training run was left running accidentally for a month.
- *Flan-UL2* 20B (2022): *UL2* 20B instruction-finetuned on the FLAN dataset.
- *Pile-T5* (2024): has the same architecture of *T5*, except it used the Llama tokenizer. It was trained on The Pile. It came in sizes of base, large, XL, XXL.

## Applications

The T5 model itself is an encoder-decoder model, allowing it to be used for instruction following. The encoder encodes the instruction, and the decoder autoregressively generates the reply.

The T5 encoder can be used as a text encoder, much like BERT. It encodes a text into a sequence of real-number vectors, which can be used for downstream applications. For example, Google Imagen uses *T5-XXL* as text encoder, and the encoded text vectors are used as conditioning on a diffusion model. As another example, the AuraFlow diffusion model uses *Pile-T5-XL*.
