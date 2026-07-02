---
title: "Diffusion model (part 2/2)"
source: https://en.wikipedia.org/wiki/Diffusion_model
domain: stable-diffusion
license: CC-BY-SA-4.0
tags: stable diffusion, text to image, latent diffusion, image generation, generative model
fetched: 2026-07-02
part: 2/2
---

## Choice of architecture

### Diffusion model

For generating images by DDPM, we need a neural network that takes a time t and a noisy image $x_{t}$ , and predicts a noise $\epsilon _{\theta }(x_{t},t)$ from it. Since predicting the noise is the same as predicting the denoised image, then subtracting it from $x_{t}$ , denoising architectures tend to work well. For example, the U-Net, which was found to be good for denoising images, is often used for denoising diffusion models that generate images.

For DDPM, the underlying architecture ("backbone") does not have to be a U-Net. It just has to predict the noise somehow. For example, the diffusion transformer (DiT) uses a Transformer to predict the mean and diagonal covariance of the noise, given the textual conditioning and the partially denoised image. It is the same as standard U-Net-based denoising diffusion model, with a Transformer replacing the U-Net. Mixture of experts-Transformer can also be applied.

DDPM can be used to model general data distributions, not just natural-looking images. For example, Human Motion Diffusion models human motion trajectory by DDPM. Each human motion trajectory is a sequence of poses, represented by either joint rotations or positions. It uses a Transformer network to generate a less noisy trajectory out of a noisy one.

### Conditioning

The base diffusion model can only generate unconditionally from the whole distribution. For example, a diffusion model learned on ImageNet would generate images that look like a random image from ImageNet. To generate images from just one category, one would need to impose the condition, and then sample from the conditional distribution. Whatever condition one wants to impose, one needs to first convert the conditioning into a vector of floating point numbers, then feed it into the underlying diffusion model neural network. However, one has freedom in choosing how to convert the conditioning into a vector.

Stable Diffusion, for example, imposes conditioning in the form of cross-attention mechanism, where the query is an intermediate representation of the image in the U-Net, and both key and value are the conditioning vectors. The conditioning can be selectively applied to only parts of an image, and new kinds of conditionings can be finetuned upon the base model, as used in ControlNet.

As a particularly simple example, consider image inpainting. The conditions are ${\tilde {x}}$ , the reference image, and m , the inpainting mask. The conditioning is imposed at each step of the backward diffusion process, by first sampling ${\tilde {x}}_{t}\sim N\left({\sqrt {{\bar {\alpha }}_{t}}}{\tilde {x}},\sigma _{t}^{2}I\right)$ , a noisy version of ${\tilde {x}}$ , then replacing $x_{t}$ with $(1-m)\odot x_{t}+m\odot {\tilde {x}}_{t}$ , where $\odot$ means elementwise multiplication. Another application of cross-attention mechanism is prompt-to-prompt image editing.

Conditioning is not limited to just generating images from a specific category, or according to a specific caption (as in text-to-image). For example, demonstrated generating human motion, conditioned on an audio clip of human walking (allowing syncing motion to a soundtrack), or video of human running, or a text description of human motion, etc. For how conditional diffusion models are mathematically formulated, see a methodological summary in.

### Upscaling

As generating an image takes a long time, one can try to generate a small image by a base diffusion model, then upscale it by other models. Upscaling can be done by GAN, Transformer, or signal processing methods like Lanczos resampling.

Diffusion models themselves can be used to perform upscaling. Cascading diffusion model stacks multiple diffusion models one after another, in the style of Progressive GAN. The lowest level is a standard diffusion model that generate 32x32 image, then the image would be upscaled by a diffusion model specifically trained for upscaling, and the process repeats.

In more detail, the diffusion upscaler is trained as follows:

- Sample $(x_{0},z_{0},c)$ , where $x_{0}$ is the high-resolution image, $z_{0}$ is the same image but scaled down to a low-resolution, and c is the conditioning, which can be the caption of the image, the class of the image, etc.
- Sample two white noises $\epsilon _{x},\epsilon _{z}$ , two time-steps $t_{x},t_{z}$ . Compute the noisy versions of the high-resolution and low-resolution images: ${\begin{cases}x_{t_{x}}&={\sqrt {{\bar {\alpha }}_{t_{x}}}}x_{0}+\sigma _{t_{x}}\epsilon _{x}\\z_{t_{z}}&={\sqrt {{\bar {\alpha }}_{t_{z}}}}z_{0}+\sigma _{t_{z}}\epsilon _{z}\end{cases}}$ .
- Train the denoising network to predict $\epsilon _{x}$ given $x_{t_{x}},z_{t_{z}},t_{x},t_{z},c$ . That is, apply gradient descent on $\theta$ on the L2 loss $\|\epsilon _{\theta }(x_{t_{x}},z_{t_{z}},t_{x},t_{z},c)-\epsilon _{x}\|_{2}^{2}$ .


## Examples

This section collects some notable diffusion models, and briefly describes their architecture.

### OpenAI

The DALL-E series by OpenAI are text-conditional diffusion models of images.

The first version of DALL-E (2021) is not actually a diffusion model. Instead, it uses a Transformer architecture that autoregressively generates a sequence of tokens, which is then converted to an image by the decoder of a discrete VAE. Released with DALL-E was the CLIP classifier, which was used by DALL-E to rank generated images according to how close the image fits the text.

GLIDE (2022–03) is a 3.5-billion diffusion model, and a small version was released publicly. Soon after, DALL-E 2 was released (2022–04). DALL-E 2 is a 3.5-billion cascaded diffusion model that generates images from text by "inverting the CLIP image encoder", the technique which they termed "unCLIP".

The unCLIP method contains 4 models: a CLIP image encoder, a CLIP text encoder, an image decoder, and a "prior" model (which can be a diffusion model, or an autoregressive model). During training, the prior model is trained to convert CLIP image encodings to CLIP text encodings. The image decoder is trained to convert CLIP image encodings back to images. During inference, a text is converted by the CLIP text encoder to a vector, then it is converted by the prior model to an image encoding, then it is converted by the image decoder to an image.

Sora (2024–02) is a diffusion Transformer model (DiT).

### Lightricks

LTX is a family of open source artificial intelligence video foundation models developed by Lightricks, first released in November 2024. The latest models, LTX-2, create videos based on user prompts, conditioned on text, images, video or audio - and capable of generating audio and visual in a unified way. They were preceded by LTX Video, which was released in 2024 as the company's first text-to-video model.

### Stability AI

Stable Diffusion (2022–08), released by Stability AI, consists of a denoising latent diffusion model (860 million parameters), a VAE, and a text encoder. The denoising network is a U-Net, with cross-attention blocks to allow for conditional image generation.

Stable Diffusion 3 (2024–03) changed the latent diffusion model from the UNet to a Transformer model, and so it is a DiT. It uses rectified flow.

Stable Video 4D (2024–07) is a latent diffusion model for videos of 3D objects.

### Google

Imagen (2022) uses a T5-XXL language model to encode the input text into an embedding vector. It is a cascaded diffusion model with three sub-models. The first step denoises a white noise to a 64×64 image, conditional on the embedding vector of the text. This model has 2B parameters. The second step upscales the image by 64×64→256×256, conditional on embedding. This model has 650M parameters. The third step is similar, upscaling by 256×256→1024×1024. This model has 400M parameters. The three denoising networks are all U-Nets.

Muse (2023–01) is not a diffusion model, but an encoder-only Transformer that is trained to predict masked image tokens from unmasked image tokens.

Imagen 2 (2023–12) is also diffusion-based. It can generate images based on a prompt that mixes images and text. No further information available. Imagen 3 (2024–05) is too. No further information available.

Veo (2024) generates videos by latent diffusion. The diffusion is conditioned on a vector that encodes both a text prompt and an image prompt.

### Meta

Make-A-Video (2022) is a text-to-video diffusion model.

CM3leon (2023) is not a diffusion model, but an autoregressive causally masked Transformer, with mostly the same architecture as LLaMa-2.

Transfusion (2024) is a Transformer that combines autoregressive text generation and denoising diffusion. Specifically, it generates text autoregressively (with causal masking), and generates images by denoising multiple times over image tokens (with all-to-all attention).

Movie Gen (2024) is a series of Diffusion Transformers operating on latent space and by flow matching.
