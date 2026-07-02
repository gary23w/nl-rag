---
title: "Generative adversarial network (part 1/2)"
source: https://en.wikipedia.org/wiki/Generative_adversarial_network
domain: gan-networks
license: CC-BY-SA-4.0
tags: gan network, generative adversarial, discriminator generator, adversarial training, image synthesis
fetched: 2026-07-02
part: 1/2
---

# Generative adversarial network

A **generative adversarial network** (**GAN**) is a class of machine learning frameworks and a prominent framework for approaching generative artificial intelligence. The concept was initially developed by Ian Goodfellow and his colleagues in June 2014. In a GAN, two neural networks compete with each other in the form of a zero-sum game, where one agent's gain is another agent's loss.

Given a training set, this technique learns to generate new data with the same statistics as the training set. For example, a GAN trained on photographs can generate new photographs that look at least superficially authentic to human observers, having many realistic characteristics. Though originally proposed as a form of generative model for unsupervised learning, GANs have also proved useful for semi-supervised learning, fully supervised learning, and reinforcement learning.

The core idea of a GAN is based on the "indirect" training through the discriminator, another neural network that can tell how "realistic" the input seems, which itself is also being updated dynamically. This means that the generator is not trained to minimize the distance to a specific image, but rather to fool the discriminator. This enables the model to learn in an unsupervised manner.

GANs are similar to mimicry in evolutionary biology, with an evolutionary arms race between both networks.


## Definition

### Mathematical

The original GAN is defined as the following game:

> Each probability space $(\Omega ,\mu _{\text{ref}})$ defines a GAN game.
> 
> There are 2 players: generator and discriminator.
> 
> The generator's strategy set is ${\mathcal {P}}(\Omega )$ , the set of all probability measures $\mu _{G}$ on $\Omega$ .
> 
> The discriminator's strategy set is the set of Markov kernels $\mu _{D}:\Omega \to {\mathcal {P}}[0,1]$ , where ${\mathcal {P}}[0,1]$ is the set of probability measures on $[0,1]$ .
> 
> The GAN game is a zero-sum game, with objective function $L(\mu _{G},\mu _{D}):=\operatorname {E} _{x\sim \mu _{\text{ref}},y\sim \mu _{D}(x)}[\ln y]+\operatorname {E} _{x\sim \mu _{G},y\sim \mu _{D}(x)}[\ln(1-y)].$ The generator aims to minimize the objective, and the discriminator aims to maximize the objective.

The generator's task is to approach $\mu _{G}\approx \mu _{\text{ref}}$ , that is, to match its own output distribution as closely as possible to the reference distribution. The discriminator's task is to output a value close to 1 when the input appears to be from the reference distribution, and to output a value close to 0 when the input looks like it came from the generator distribution.

### In practice

The *generative* network generates candidates while the *discriminative* network evaluates them. This creates a contest based on data distributions, where the generator learns to map from a latent space to the true data distribution, aiming to produce candidates that the discriminator cannot distinguish from real data. The discriminator's goal is to correctly identify these candidates, but as the generator improves, its task becomes more challenging, increasing the discriminator's error rate.

A known dataset serves as the initial training data for the discriminator. Training involves presenting it with samples from the training dataset until it achieves acceptable accuracy. The generator is trained based on whether it succeeds in fooling the discriminator. Typically, the generator is seeded with randomized input that is sampled from a predefined latent space (e.g. a multivariate normal distribution). Thereafter, candidates synthesized by the generator are evaluated by the discriminator. Independent backpropagation procedures are applied to both networks so that the generator produces better samples, while the discriminator becomes more skilled at flagging synthetic samples. When used for image generation, the generator is typically a deconvolutional neural network, and the discriminator is a convolutional neural network.

### Relation to other statistical machine learning methods

GANs are **implicit generative models**, which means that they do not explicitly model the likelihood function nor provide a means for finding the latent variable corresponding to a given sample, unlike alternatives such as flow-based generative model.

Compared to fully visible belief networks such as WaveNet and PixelRNN and autoregressive models in general, GANs can generate one complete sample in one pass, rather than multiple passes through the network.

Compared to Boltzmann machines and linear ICA, there is no restriction on the type of function used by the network.

Since neural networks are universal approximators, GANs are asymptotically consistent. Variational autoencoders might be universal approximators, but it is not proven as of 2017.


## Mathematical properties

### Measure-theoretic considerations

This section provides some of the mathematical theory behind these methods.

In modern probability theory based on measure theory, a probability space also needs to be equipped with a σ-algebra. As a result, a more rigorous definition of the GAN game would make the following changes:

> Each probability space $(\Omega ,{\mathcal {B}},\mu _{\text{ref}})$ defines a GAN game.
> 
> The generator's strategy set is ${\mathcal {P}}(\Omega ,{\mathcal {B}})$ , the set of all probability measures $\mu _{G}$ on the measure-space $(\Omega ,{\mathcal {B}})$ .
> 
> The discriminator's strategy set is the set of Markov kernels $\mu _{D}:(\Omega ,{\mathcal {B}})\to {\mathcal {P}}([0,1],{\mathcal {B}}([0,1]))$ , where ${\mathcal {B}}([0,1])$ is the Borel σ-algebra on $[0,1]$ .

Since issues of measurability never arise in practice, these will not concern us further.

### Choice of the strategy set

In the most generic version of the GAN game described above, the strategy set for the discriminator contains all Markov kernels $\mu _{D}:\Omega \to {\mathcal {P}}[0,1]$ , and the strategy set for the generator contains arbitrary probability distributions $\mu _{G}$ on $\Omega$ .

However, as shown below, the optimal discriminator strategy against any $\mu _{G}$ is deterministic, so there is no loss of generality in restricting the discriminator's strategies to deterministic functions $D:\Omega \to [0,1]$ . In most applications, D is a deep neural network function.

As for the generator, while $\mu _{G}$ could theoretically be any computable probability distribution, in practice, it is usually implemented as a pushforward: $\mu _{G}=\mu _{Z}\circ G^{-1}$ . That is, start with a random variable $z\sim \mu _{Z}$ , where $\mu _{Z}$ is a probability distribution that is easy to compute (such as the uniform distribution, or the Gaussian distribution), then define a function $G:\Omega _{Z}\to \Omega$ . Then the distribution $\mu _{G}$ is the distribution of $G(z)$ .

Consequently, the generator's strategy is usually defined as just G , leaving $z\sim \mu _{Z}$ implicit. In this formalism, the GAN game objective is $L(G,D):=\operatorname {E} _{x\sim \mu _{\text{ref}}}[\ln D(x)]+\operatorname {E} _{z\sim \mu _{Z}}[\ln(1-D(G(z)))].$

### Generative reparametrization

The GAN architecture has two main components. One is casting optimization into a game, of form $\min _{G}\max _{D}L(G,D)$ , which is different from the usual kind of optimization, of form $\min _{\theta }L(\theta )$ . The other is the decomposition of $\mu _{G}$ into $\mu _{Z}\circ G^{-1}$ , which can be understood as a reparametrization trick.

To see its significance, one must compare GAN with previous methods for learning generative models, which were plagued with "intractable probabilistic computations that arise in maximum likelihood estimation and related strategies".

At the same time, Kingma and Welling and Rezende et al. developed the same idea of reparametrization into a general stochastic backpropagation method. Among its first applications was the variational autoencoder.

### Move order and strategic equilibria

In the original paper, as well as most subsequent papers, it is usually assumed that the generator *moves first*, and the discriminator *moves second*, thus giving the following minimax game: $\min _{\mu _{G}}\max _{\mu _{D}}L(\mu _{G},\mu _{D}):=\operatorname {E} _{x\sim \mu _{\text{ref}},y\sim \mu _{D}(x)}[\ln y]+\operatorname {E} _{x\sim \mu _{G},y\sim \mu _{D}(x)}[\ln(1-y)].$

If both the generator's and the discriminator's strategy sets are spanned by a finite number of strategies, then by the minimax theorem, $\min _{\mu _{G}}\max _{\mu _{D}}L(\mu _{G},\mu _{D})=\max _{\mu _{D}}\min _{\mu _{G}}L(\mu _{G},\mu _{D})$ that is, the move order does not matter.

However, since the strategy sets are both not finitely spanned, the minimax theorem does not apply, and the idea of an "equilibrium" becomes delicate. To wit, there are the following different concepts of equilibrium:

- Equilibrium when generator moves first, and discriminator moves second: ${\hat {\mu }}_{G}\in \arg \min _{\mu _{G}}\max _{\mu _{D}}L(\mu _{G},\mu _{D}),\quad {\hat {\mu }}_{D}\in \arg \max _{\mu _{D}}L({\hat {\mu }}_{G},\mu _{D}),\quad$
- Equilibrium when discriminator moves first, and generator moves second: ${\hat {\mu }}_{D}\in \arg \max _{\mu _{D}}\min _{\mu _{G}}L(\mu _{G},\mu _{D}),\quad {\hat {\mu }}_{G}\in \arg \min _{\mu _{G}}L(\mu _{G},{\hat {\mu }}_{D}),$
- Nash equilibrium $({\hat {\mu }}_{D},{\hat {\mu }}_{G})$ , which is stable under simultaneous move order: ${\hat {\mu }}_{D}\in \arg \max _{\mu _{D}}L({\hat {\mu }}_{G},\mu _{D}),\quad {\hat {\mu }}_{G}\in \arg \min _{\mu _{G}}L(\mu _{G},{\hat {\mu }}_{D})$

For general games, these equilibria do not have to agree, or even to exist. For the original GAN game, these equilibria all exist, and are all equal. However, for more general GAN games, these do not necessarily exist, or agree.

### Main theorems for GAN game

The original GAN paper proved the following two theorems:

**Theorem** (the optimal discriminator computes the Jensen–Shannon divergence)—For any fixed generator strategy $\mu _{G}$ , let the optimal reply be $D^{*}=\arg \max _{D}L(\mu _{G},D)$ , then

${\begin{aligned}D^{*}(x)&={\frac {d\mu _{\text{ref}}}{d(\mu _{\text{ref}}+\mu _{G})}}\\[6pt]L(\mu _{G},D^{*})&=2D_{JS}(\mu _{\text{ref}};\mu _{G})-2\ln 2\end{aligned}}$

where the derivative is the Radon–Nikodym derivative, and $D_{JS}$ is the Jensen–Shannon divergence.

Proof

By Jensen's inequality,

$\operatorname {E} _{x\sim \mu _{\text{ref}},y\sim \mu _{D}(x)}[\ln y]\leq \operatorname {E} _{x\sim \mu _{\text{ref}}}[\ln \operatorname {E} _{y\sim \mu _{D}(x)}[y]]$ and similarly for the other term. Therefore, the optimal reply can be deterministic, i.e. $\mu _{D}(x)=\delta _{D(x)}$ for some function $D:\Omega \to [0,1]$ , in which case

$L(\mu _{G},\mu _{D}):=\operatorname {E} _{x\sim \mu _{\text{ref}}}[\ln D(x)]+\operatorname {E} _{x\sim \mu _{G}}[\ln(1-D(x))].$

To define suitable density functions, we define a base measure ${\displaystyle \mu$ , which allows us to take the Radon–Nikodym derivatives

$\rho _{\text{ref}}={\frac {d\mu _{\text{ref}}}{d\mu }}\quad \rho _{G}={\frac {d\mu _{G}}{d\mu }}$ with $\rho _{\text{ref}}+\rho _{G}=1$ .

We then have

$L(\mu _{G},\mu _{D}):=\int \mu (dx)\left[\rho _{\text{ref}}(x)\ln(D(x))+\rho _{G}(x)\ln(1-D(x))\right].$

The integrand is just the negative cross-entropy between two Bernoulli random variables with parameters $\rho _{\text{ref}}(x)$ and $D(x)$ . We can write this as $-H(\rho _{\text{ref}}(x))-D_{KL}(\rho _{\text{ref}}(x)\parallel D(x))$ , where H is the binary entropy function, so

$L(\mu _{G},\mu _{D})=-\int \mu (dx)(H(\rho _{\text{ref}}(x))+D_{KL}(\rho _{\text{ref}}(x)\parallel D(x))).$

This means that the optimal strategy for the discriminator is $D(x)=\rho _{\text{ref}}(x)$ , with $L(\mu _{G},\mu _{D}^{*})=-\int \mu (dx)H(\rho _{\text{ref}}(x))=D_{JS}(\mu _{\text{ref}}\parallel \mu _{G})-2\ln 2$

after routine calculation.

**Interpretation**: For any fixed generator strategy $\mu _{G}$ , the optimal discriminator keeps track of the likelihood ratio between the reference distribution and the generator distribution: ${\frac {D(x)}{1-D(x)}}={\frac {d\mu _{\text{ref}}}{d\mu _{G}}}(x)={\frac {\mu _{\text{ref}}(dx)}{\mu _{G}(dx)}};\quad D(x)=\sigma (\ln \mu _{\text{ref}}(dx)-\ln \mu _{G}(dx))$ where $\sigma$ is the logistic function. In particular, if the prior probability for an image x to come from the reference distribution is equal to ${\frac {1}{2}}$ , then $D(x)$ is just the posterior probability that x came from the reference distribution: $D(x)=\Pr(x{\text{ came from reference distribution}}\mid x).$

**Theorem** (the unique equilibrium point)—For any GAN game, there exists a pair $({\hat {\mu }}_{D},{\hat {\mu }}_{G})$ that is both a sequential equilibrium and a Nash equilibrium:

${\begin{aligned}&L({\hat {\mu }}_{G},{\hat {\mu }}_{D})=\min _{\mu _{G}}\max _{\mu _{D}}L(\mu _{G},\mu _{D})=&\max _{\mu _{D}}\min _{\mu _{G}}L(\mu _{G},\mu _{D})=-2\ln 2\\[6pt]&{\hat {\mu }}_{D}\in \arg \max _{\mu _{D}}\min _{\mu _{G}}L(\mu _{G},\mu _{D}),&\quad {\hat {\mu }}_{G}\in \arg \min _{\mu _{G}}\max _{\mu _{D}}L(\mu _{G},\mu _{D})\\[6pt]&{\hat {\mu }}_{D}\in \arg \max _{\mu _{D}}L({\hat {\mu }}_{G},\mu _{D}),&\quad {\hat {\mu }}_{G}\in \arg \min _{\mu _{G}}L(\mu _{G},{\hat {\mu }}_{D})\\[6pt]&\forall x\in \Omega ,{\hat {\mu }}_{D}(x)=\delta _{\frac {1}{2}},&\quad {\hat {\mu }}_{G}=\mu _{\text{ref}}\end{aligned}}$

That is, the generator perfectly mimics the reference, and the discriminator outputs ${\frac {1}{2}}$ deterministically on all inputs.

Proof

From the previous proposition,

$\arg \min _{\mu _{G}}\max _{\mu _{D}}L(\mu _{G},\mu _{D})=\mu _{\text{ref}};\quad \min _{\mu _{G}}\max _{\mu _{D}}L(\mu _{G},\mu _{D})=-2\ln 2.$

For any fixed discriminator strategy $\mu _{D}$ , any $\mu _{G}$ concentrated on the set

$\{x\mid \operatorname {E} _{y\sim \mu _{D}(x)}[\ln(1-y)]=\inf _{x}\operatorname {E} _{y\sim \mu _{D}(x)}[\ln(1-y)]\}$ is an optimal strategy for the generator. Thus,

$\arg \max _{\mu _{D}}\min _{\mu _{G}}L(\mu _{G},\mu _{D})=\arg \max _{\mu _{D}}\operatorname {E} _{x\sim \mu _{\text{ref}},y\sim \mu _{D}(x)}[\ln y]+\inf _{x}\operatorname {E} _{y\sim \mu _{D}(x)}[\ln(1-y)].$

By Jensen's inequality, the discriminator can only improve by adopting the deterministic strategy of always playing $D(x)=\operatorname {E} _{y\sim \mu _{D}(x)}[y]$ . Therefore,

$\arg \max _{\mu _{D}}\min _{\mu _{G}}L(\mu _{G},\mu _{D})=\arg \max _{D}\operatorname {E} _{x\sim \mu _{\text{ref}}}[\ln D(x)]+\inf _{x}\ln(1-D(x))$

By Jensen's inequality,

${\begin{aligned}&\ln \operatorname {E} _{x\sim \mu _{\text{ref}}}[D(x)]+\inf _{x}\ln(1-D(x))\\[6pt]={}&\ln \operatorname {E} _{x\sim \mu _{\text{ref}}}[D(x)]+\ln(1-\sup _{x}D(x))\\[6pt]={}&\ln[\operatorname {E} _{x\sim \mu _{\text{ref}}}[D(x)](1-\sup _{x}D(x))]\leq \ln[\sup _{x}D(x))(1-\sup _{x}D(x))]\leq \ln {\frac {1}{4}},\end{aligned}}$

with equality if $D(x)={\frac {1}{2}}$ , so

$\forall x\in \Omega ,{\hat {\mu }}_{D}(x)=\delta _{\frac {1}{2}};\quad \max _{\mu _{D}}\min _{\mu _{G}}L(\mu _{G},\mu _{D})=-2\ln 2.$

Finally, to check that this is a Nash equilibrium, note that when $\mu _{G}=\mu _{\text{ref}}$ , we have

$L(\mu _{G},\mu _{D}):=\operatorname {E} _{x\sim \mu _{\text{ref}},y\sim \mu _{D}(x)}[\ln(y(1-y))]$ which is always maximized by $y={\frac {1}{2}}$ .

When $\forall x\in \Omega ,\mu _{D}(x)=\delta _{\frac {1}{2}}$ , any strategy is optimal for the generator.


## Training and evaluating GAN

### Training

#### Unstable convergence

While the GAN game has a unique global equilibrium point when both the generator and discriminator have access to their entire strategy sets, the equilibrium is no longer guaranteed when they have a restricted strategy set.

In practice, the generator has access only to measures of form $\mu _{Z}\circ G_{\theta }^{-1}$ , where $G_{\theta }$ is a function computed by a neural network with parameters $\theta$ , and $\mu _{Z}$ is an easily sampled distribution, such as the uniform or normal distribution. Similarly, the discriminator has access only to functions of form $D_{\zeta }$ , a function computed by a neural network with parameters $\zeta$ . These restricted strategy sets take up a *vanishingly small proportion* of their entire strategy sets.

Further, even if an equilibrium still exists, it can only be found by searching in the high-dimensional space of all possible neural network functions. The standard strategy of using gradient descent to find the equilibrium often does not work for GAN, and often the game "collapses" into one of several failure modes. To improve the convergence stability, some training strategies start with an easier task, such as generating low-resolution images or simple images (one object with uniform background), and gradually increase the difficulty of the task during training. This essentially translates to applying a curriculum learning scheme.

#### Mode collapse

GANs often suffer from **mode collapse** where they fail to generalize properly, missing entire modes from the input data. For example, a GAN trained on the MNIST dataset containing many samples of each digit might only generate pictures of digit 0. This was termed "the Helvetica scenario".

A typical mechanism for mode collapse is the generator only generating one or a few of the likely values, or a very incomplete picture of the target distribution. As the discriminator is only trained to distinguish real from fake samples, it will correctly identify the generated samples as real, but no penalty is imposed on the GAN's ability to generate data that represents the full range of the target distribution.

Weak discriminators, for instance underparametrized ones, or ones trained too slow compared to the generator, may as well be unable to fully discriminate over the entire support of the distribution, and only become able to correctly discriminate a very incomplete part of the target distribution.

Some researchers perceive the root problem to be a weak discriminative network that fails to notice the pattern of omission, while others assign blame to a bad choice of objective function. Many solutions have been proposed, but it is still an open problem.

Even the state-of-the-art architecture, BigGAN (2019), could not avoid mode collapse. The authors resorted to "allowing collapse to occur at the later stages of training, by which time a model is sufficiently trained to achieve good results".

#### Two time-scale update rule

The **two time-scale update rule (TTUR)** is proposed to make GAN convergence more stable by making the learning rate of the generator lower than that of the discriminator. They prove that when trained this way, GANs "converge, under mild assumptions to a stationary local Nash equilibrium". They further show that this property extends to the use of the Adam optimizer, which is commonly used in stochastic gradient descent.

A local Nash equilibrium in no way signifies an absence of mode collapse - for instance, a GAN trained on MNIST collapsed to generating a single digit may satisfy the hypotheses of the paper, while still presenting mode collapse.

#### Vanishing gradient

Conversely, if the discriminator learns too fast compared to the generator, then the discriminator could almost perfectly distinguish $\mu _{G_{\theta }},\mu _{\text{ref}}$ . In such case, the generator $G_{\theta }$ could be stuck with a very high loss no matter which direction it changes its $\theta$ , meaning that the gradient $\nabla _{\theta }L(G_{\theta },D_{\zeta })$ would be close to zero. In such case, the generator cannot learn, a case of the **vanishing gradient** problem.

Intuitively speaking, the discriminator is too good, and since the generator cannot take any small step (only small steps are considered in gradient descent) to improve its payoff, it does not even try.

One important method for solving this problem is the Wasserstein GAN.

### Evaluation

GANs are usually evaluated by Inception score (IS), which measures how varied the generator's outputs are (as classified by an image classifier, usually Inception-v3), or Fréchet inception distance (FID), which measures how similar the generator's outputs are to a reference set (as classified by a learned image featurizer, such as Inception-v3 without its final layer). Many papers that propose new GAN architectures for image generation report how their architectures break the state of the art on FID or IS.

Another evaluation method is the Learned Perceptual Image Patch Similarity (LPIPS), which starts with a learned image featurizer $f_{\theta }:{\text{Image}}\to \mathbb {R} ^{n}$ , and finetunes it by supervised learning on a set of $(x,x',\operatorname {perceptual~difference} (x,x'))$ , where x is an image, $x'$ is a perturbed version of it, and $\operatorname {perceptual~difference} (x,x')$ is how much they differ, as reported by human subjects. The model is finetuned so that it can approximate $\|f_{\theta }(x)-f_{\theta }(x')\|\approx \operatorname {perceptual~difference} (x,x')$ . This finetuned model is then used to define $\operatorname {LPIPS} (x,x'):=\|f_{\theta }(x)-f_{\theta }(x')\|$ .

Other evaluation methods are reviewed in.


## Variants

There is a veritable zoo of GAN variants. Some of the most prominent are as follows:

### Conditional GAN

Conditional GANs are similar to standard GANs except they allow the model to conditionally generate samples based on additional information. For example, if we want to generate a cat face given a dog picture, we could use a conditional GAN.

The generator in a GAN game generates $\mu _{G}$ , a probability distribution on the probability space $\Omega$ . This leads to the idea of a conditional GAN, where instead of generating one probability distribution on $\Omega$ , the generator generates a different probability distribution $\mu _{G}(c)$ on $\Omega$ , for each given class label c .

For example, for generating images that look like ImageNet, the generator should be able to generate a picture of cat when given the class label "cat".

In the original paper, the authors noted that GAN can be trivially extended to conditional GAN by providing the labels to both the generator and the discriminator.

Concretely, the conditional GAN game is just the GAN game with class labels provided: $L(\mu _{G},D):=\operatorname {E} _{c\sim \mu _{C},x\sim \mu _{\text{ref}}(c)}[\ln D(x,c)]+\operatorname {E} _{c\sim \mu _{C},x\sim \mu _{G}(c)}[\ln(1-D(x,c))]$ where $\mu _{C}$ is a probability distribution over classes, $\mu _{\text{ref}}(c)$ is the probability distribution of real images of class c , and $\mu _{G}(c)$ the probability distribution of images generated by the generator when given class label c .

In 2017, a conditional GAN learned to generate 1000 image classes of ImageNet.

### GANs with alternative architectures

The GAN game is a general framework and can be run with any reasonable parametrization of the generator G and discriminator D . In the original paper, the authors demonstrated it using multilayer perceptron networks and convolutional neural networks. Many alternative architectures have been tried.

**Deep convolutional GAN (DCGAN):** For both generator and discriminator, uses only deep networks consisting entirely of convolution-deconvolution layers, that is, fully convolutional networks.

**Self-attention GAN (SAGAN):** Starts with the DCGAN, then adds residually-connected standard self-attention modules to the generator and discriminator.

**Variational autoencoder GAN (VAEGAN):** Uses a variational autoencoder (VAE) for the generator.

**Transformer GAN (TransGAN):** Uses the pure transformer architecture for both the generator and discriminator, entirely devoid of convolution-deconvolution layers.

**Flow-GAN:** Uses flow-based generative model for the generator, allowing efficient computation of the likelihood function.

### GANs with alternative objectives

Many GAN variants are merely obtained by changing the loss functions for the generator and discriminator.

**Original GAN:**

We recast the original GAN objective into a form more convenient for comparison: ${\begin{cases}\min _{D}L_{D}(D,\mu _{G})=-\operatorname {E} _{x\sim \mu _{G}}[\ln D(x)]-\operatorname {E} _{x\sim \mu _{\text{ref}}}[\ln(1-D(x))]\\\min _{G}L_{G}(D,\mu _{G})=-\operatorname {E} _{x\sim \mu _{G}}[\ln(1-D(x))]\end{cases}}$

**Original GAN, non-saturating loss:**

This objective for generator was recommended in the original paper for faster convergence. $L_{G}=\operatorname {E} _{x\sim \mu _{G}}[\ln D(x)]$ The effect of using this objective is analyzed in Section 2.2.2 of Arjovsky et al.

**Original GAN, maximum likelihood:**

$L_{G}=\operatorname {E} _{x\sim \mu _{G}}[({\exp }\circ \sigma ^{-1}\circ D)(x)]$ where $\sigma$ is the logistic function. When the discriminator is optimal, the generator gradient is the same as in maximum likelihood estimation, even though GAN cannot perform maximum likelihood estimation *itself*.

**Hinge loss GAN**: $L_{D}=-\operatorname {E} _{x\sim p_{\text{ref}}}\left[\min \left(0,-1+D(x)\right)\right]-\operatorname {E} _{x\sim \mu _{G}}\left[\min \left(0,-1-D\left(x\right)\right)\right]$ $L_{G}=-\operatorname {E} _{x\sim \mu _{G}}[D(x)]$ **Least squares GAN:** $L_{D}=\operatorname {E} _{x\sim \mu _{\text{ref}}}[(D(x)-b)^{2}]+\operatorname {E} _{x\sim \mu _{G}}[(D(x)-a)^{2}]$ $L_{G}=\operatorname {E} _{x\sim \mu _{G}}[(D(x)-c)^{2}]$ where $a,b,c$ are parameters to be chosen. The authors recommended $a=-1,b=1,c=0$ .

### Wasserstein GAN (WGAN)

The Wasserstein GAN modifies the GAN game at two points:

- The discriminator's strategy set is the set of measurable functions of type $D:\Omega \to \mathbb {R}$ with bounded Lipschitz norm: $\|D\|_{L}\leq K$ , where K is a fixed positive constant.
- The objective is $L_{WGAN}(\mu _{G},D):=\operatorname {E} _{x\sim \mu _{G}}[D(x)]-\mathbb {E} _{x\sim \mu _{\text{ref}}}[D(x)]$

One of its purposes is to solve the problem of mode collapse (see above). The authors claim "In no experiment did we see evidence of mode collapse for the WGAN algorithm".

### GANs with more than two players

#### Adversarial autoencoder

An adversarial autoencoder (AAE) is more autoencoder than GAN. The idea is to start with a plain autoencoder, but train a discriminator to discriminate the latent vectors from a reference distribution (often the normal distribution).

#### InfoGAN

In conditional GAN, the generator receives both a noise vector z and a label c , and produces an image $G(z,c)$ . The discriminator receives image-label pairs $(x,c)$ , and computes $D(x,c)$ .

When the training dataset is unlabeled, conditional GAN does not work directly.

The idea of InfoGAN is to decree that every latent vector in the latent space can be decomposed as $(z,c)$ : an incompressible noise part z , and an informative label part c , and encourage the generator to comply with the decree, by encouraging it to maximize $I(c,G(z,c))$ , the mutual information between c and $G(z,c)$ , while making no demands on the mutual information z between $G(z,c)$ .

Unfortunately, $I(c,G(z,c))$ is intractable in general, The key idea of InfoGAN is Variational Mutual Information Maximization: indirectly maximize it by maximizing a lower bound ${\hat {I}}(G,Q)=\mathbb {E} _{z\sim \mu _{Z},c\sim \mu _{C}}[\ln Q(c\mid G(z,c))];\quad I(c,G(z,c))\geq \sup _{Q}{\hat {I}}(G,Q)$ where Q ranges over all Markov kernels of type $Q:\Omega _{Y}\to {\mathcal {P}}(\Omega _{C})$ .

The InfoGAN game is defined as follows:

> Three probability spaces define an InfoGAN game:
> 
> - $(\Omega _{X},\mu _{\text{ref}})$ , the space of reference images.
> - $(\Omega _{Z},\mu _{Z})$ , the fixed random noise generator.
> - $(\Omega _{C},\mu _{C})$ , the fixed random information generator.
> 
> There are 3 players in 2 teams: generator, Q, and discriminator. The generator and Q are on one team, and the discriminator on the other team.
> 
> The objective function is $L(G,Q,D)=L_{GAN}(G,D)-\lambda {\hat {I}}(G,Q)$ where $L_{GAN}(G,D)=\operatorname {E} _{x\sim \mu _{\text{ref}},}[\ln D(x)]+\operatorname {E} _{z\sim \mu _{Z}}[\ln(1-D(G(z,c)))]$ is the original GAN game objective, and ${\hat {I}}(G,Q)=\mathbb {E} _{z\sim \mu _{Z},c\sim \mu _{C}}[\ln Q(c\mid G(z,c))]$
> 
> Generator-Q team aims to minimize the objective, and discriminator aims to maximize it: $\min _{G,Q}\max _{D}L(G,Q,D)$

#### Bidirectional GAN (BiGAN)

The standard GAN generator is a function of type $G:\Omega _{Z}\to \Omega _{X}$ , that is, it is a mapping from a latent space $\Omega _{Z}$ to the image space $\Omega _{X}$ . This can be understood as a "decoding" process, whereby every latent vector $z\in \Omega _{Z}$ is a code for an image $x\in \Omega _{X}$ , and the generator performs the decoding. This naturally leads to the idea of training another network that performs "encoding", creating an autoencoder out of the encoder-generator pair.

Already in the original paper, the authors noted that "Learned approximate inference can be performed by training an auxiliary network to predict z given x ". The bidirectional GAN architecture performs exactly this.

The BiGAN is defined as follows:

> Two probability spaces define a BiGAN game:
> 
> - $(\Omega _{X},\mu _{X})$ , the space of reference images.
> - $(\Omega _{Z},\mu _{Z})$ , the latent space.
> 
> There are 3 players in 2 teams: generator, encoder, and discriminator. The generator and encoder are on one team, and the discriminator on the other team.
> 
> The generator's strategies are functions $G:\Omega _{Z}\to \Omega _{X}$ , and the encoder's strategies are functions $E:\Omega _{X}\to \Omega _{Z}$ . The discriminator's strategies are functions $D:\Omega _{X}\to [0,1]$ .
> 
> The objective function is $L(G,E,D)=\mathbb {E} _{x\sim \mu _{X}}[\ln D(x,E(x))]+\mathbb {E} _{z\sim \mu _{Z}}[\ln(1-D(G(z),z))]$
> 
> Generator-encoder team aims to minimize the objective, and discriminator aims to maximize it: $\min _{G,E}\max _{D}L(G,E,D)$

In the paper, they gave a more abstract definition of the objective as: $L(G,E,D)=\mathbb {E} _{(x,z)\sim \mu _{E,X}}[\ln D(x,z)]+\mathbb {E} _{(x,z)\sim \mu _{G,Z}}[\ln(1-D(x,z))]$ where $\mu _{E,X}(dx,dz)=\mu _{X}(dx)\cdot \delta _{E(x)}(dz)$ is the probability distribution on $\Omega _{X}\times \Omega _{Z}$ obtained by pushing $\mu _{X}$ forward via $x\mapsto (x,E(x))$ , and $\mu _{G,Z}(dx,dz)=\delta _{G(z)}(dx)\cdot \mu _{Z}(dz)$ is the probability distribution on $\Omega _{X}\times \Omega _{Z}$ obtained by pushing $\mu _{Z}$ forward via $z\mapsto (G(x),z)$ .

Applications of bidirectional models include semi-supervised learning, interpretable machine learning, and neural machine translation.

#### CycleGAN

CycleGAN is an architecture for performing translations between two domains, such as between photos of horses and photos of zebras, or photos of night cities and photos of day cities.

The CycleGAN game is defined as follows:

> There are two probability spaces $(\Omega _{X},\mu _{X}),(\Omega _{Y},\mu _{Y})$ , corresponding to the two domains needed for translations fore-and-back.
> 
> There are 4 players in 2 teams: generators $G_{X}:\Omega _{X}\to \Omega _{Y},G_{Y}:\Omega _{Y}\to \Omega _{X}$ , and discriminators $D_{X}:\Omega _{X}\to [0,1],D_{Y}:\Omega _{Y}\to [0,1]$ .
> 
> The objective function is $L(G_{X},G_{Y},D_{X},D_{Y})=L_{GAN}(G_{X},D_{X})+L_{GAN}(G_{Y},D_{Y})+\lambda L_{cycle}(G_{X},G_{Y})$
> 
> where $\lambda$ is a positive adjustable parameter, $L_{GAN}$ is the GAN game objective, and $L_{cycle}$ is the *cycle consistency loss*: $L_{cycle}(G_{X},G_{Y})=E_{x\sim \mu _{X}}\|G_{X}(G_{Y}(x))-x\|+E_{y\sim \mu _{Y}}\|G_{Y}(G_{X}(y))-y\|$ The generators aim to minimize the objective, and the discriminators aim to maximize it: $\min _{G_{X},G_{Y}}\max _{D_{X},D_{Y}}L(G_{X},G_{Y},D_{X},D_{Y})$

Unlike previous work like pix2pix, which requires paired training data, cycleGAN requires no paired data. For example, to train a pix2pix model to turn a summer scenery photo to winter scenery photo and back, the dataset must contain pairs of the same place in summer and winter, shot at the same angle; cycleGAN would only need a set of summer scenery photos, and an unrelated set of winter scenery photos.

### GANs with particularly large or small scales

#### BigGAN

The BigGAN is essentially a self-attention GAN trained on a large scale (up to 80 million parameters) to generate large images of ImageNet (up to 512 x 512 resolution), with numerous engineering tricks to make it converge.

#### Invertible data augmentation

When there is insufficient training data, the reference distribution $\mu _{\text{ref}}$ cannot be well-approximated by the empirical distribution given by the training dataset. In such cases, data augmentation can be applied, to allow training GAN on smaller datasets. Naïve data augmentation, however, brings its problems.

Consider the original GAN game, slightly reformulated as follows: ${\begin{cases}\min _{D}L_{D}(D,\mu _{G})=-\operatorname {E} _{x\sim \mu _{\text{ref}}}[\ln D(x)]-\operatorname {E} _{x\sim \mu _{G}}[\ln(1-D(x))]\\\min _{G}L_{G}(D,\mu _{G})=-\operatorname {E} _{x\sim \mu _{G}}[\ln(1-D(x))]\end{cases}}$ Now we use data augmentation by randomly sampling semantic-preserving transforms $T:\Omega \to \Omega$ and applying them to the dataset, to obtain the reformulated GAN game: ${\begin{cases}\min _{D}L_{D}(D,\mu _{G})=-\operatorname {E} _{x\sim \mu _{\text{ref}},T\sim \mu _{\text{trans}}}[\ln D(T(x))]-\operatorname {E} _{x\sim \mu _{G}}[\ln(1-D(x))]\\\min _{G}L_{G}(D,\mu _{G})=-\operatorname {E} _{x\sim \mu _{G}}[\ln(1-D(x))]\end{cases}}$ This is equivalent to a GAN game with a different distribution $\mu _{\text{ref}}'$ , sampled by $T(x)$ , with $x\sim \mu _{\text{ref}},T\sim \mu _{\text{trans}}$ . For example, if $\mu _{\text{ref}}$ is the distribution of images in ImageNet, and $\mu _{\text{trans}}$ samples identity-transform with probability 0.5, and horizontal-reflection with probability 0.5, then $\mu _{\text{ref}}'$ is the distribution of images in ImageNet and horizontally-reflected ImageNet, combined.

The result of such training would be a generator that mimics $\mu _{\text{ref}}'$ . For example, it would generate images that look like they are randomly cropped, if the data augmentation uses random cropping.

The solution is to apply data augmentation to both generated and real images: ${\begin{cases}\min _{D}L_{D}(D,\mu _{G})=-\operatorname {E} _{x\sim \mu _{\text{ref}},T\sim \mu _{\text{trans}}}[\ln D(T(x))]-\operatorname {E} _{x\sim \mu _{G},T\sim \mu _{\text{trans}}}[\ln(1-D(T(x)))]\\\min _{G}L_{G}(D,\mu _{G})=-\operatorname {E} _{x\sim \mu _{G},T\sim \mu _{\text{trans}}}[\ln(1-D(T(x)))]\end{cases}}$ The authors demonstrated high-quality generation using just 100-picture-large datasets.

The StyleGAN-2-ADA paper points out a further point on data augmentation: it must be *invertible*. Continue with the example of generating ImageNet pictures. If the data augmentation is "randomly rotate the picture by 0, 90, 180, 270 degrees with *equal* probability", then there is no way for the generator to know which is the true orientation: Consider two generators $G,G'$ , such that for any latent z , the generated image $G(z)$ is a 90-degree rotation of $G'(z)$ . They would have exactly the same expected loss, and so neither is preferred over the other.

The solution is to only use invertible data augmentation: instead of "randomly rotate the picture by 0, 90, 180, 270 degrees with *equal* probability", use "randomly rotate the picture by 90, 180, 270 degrees with 0.1 probability, and keep the picture as it is with 0.7 probability". This way, the generator is still rewarded to keep images oriented the same way as un-augmented ImageNet pictures.

Abstractly, the effect of randomly sampling transformations $T:\Omega \to \Omega$ from the distribution $\mu _{\text{trans}}$ is to define a Markov kernel $K_{\text{trans}}:\Omega \to {\mathcal {P}}(\Omega )$ . Then, the data-augmented GAN game pushes the generator to find some ${\hat {\mu }}_{G}\in {\mathcal {P}}(\Omega )$ , such that $K_{\text{trans}}*\mu _{\text{ref}}=K_{\text{trans}}*{\hat {\mu }}_{G}$ where * is the Markov kernel convolution. A data-augmentation method is defined to be *invertible* if its Markov kernel $K_{\text{trans}}$ satisfies $K_{\text{trans}}*\mu =K_{\text{trans}}*\mu '\implies \mu =\mu '\quad \forall \mu ,\mu '\in {\mathcal {P}}(\Omega )$ Immediately by definition, we see that composing multiple invertible data-augmentation methods results in yet another invertible method. Also by definition, if the data-augmentation method is invertible, then using it in a GAN game does not change the optimal strategy ${\hat {\mu }}_{G}$ for the generator, which is still $\mu _{\text{ref}}$ .

There are two prototypical examples of invertible Markov kernels:

**Discrete case**: Invertible stochastic matrices, when $\Omega$ is finite.

For example, if $\Omega =\{\uparrow ,\downarrow ,\leftarrow ,\rightarrow \}$ is the set of four images of an arrow, pointing in 4 directions, and the data augmentation is "randomly rotate the picture by 90, 180, 270 degrees with probability p , and keep the picture as it is with probability $(1-3p)$ ", then the Markov kernel $K_{\text{trans}}$ can be represented as a stochastic matrix: $[K_{\text{trans}}]={\begin{bmatrix}(1-3p)&p&p&p\\p&(1-3p)&p&p\\p&p&(1-3p)&p\\p&p&p&(1-3p)\end{bmatrix}}$ and $K_{\text{trans}}$ is an invertible kernel iff $[K_{\text{trans}}]$ is an invertible matrix, that is, $p\neq 1/4$ .

**Continuous case**: The gaussian kernel, when $\Omega =\mathbb {R} ^{n}$ for some $n\geq 1$ .

For example, if $\Omega =\mathbb {R} ^{256^{2}}$ is the space of 256x256 images, and the data-augmentation method is "generate a gaussian noise $z\sim {\mathcal {N}}(0,I_{256^{2}})$ , then add $\epsilon z$ to the image", then $K_{\text{trans}}$ is just convolution by the density function of ${\mathcal {N}}(0,\epsilon ^{2}I_{256^{2}})$ . This is invertible, because convolution by a gaussian is just convolution by the heat kernel, so given any $\mu \in {\mathcal {P}}(\mathbb {R} ^{n})$ , the convolved distribution $K_{\text{trans}}*\mu$ can be obtained by heating up $\mathbb {R} ^{n}$ precisely according to $\mu$ , then wait for time $\epsilon ^{2}/4$ . With that, we can recover $\mu$ by running the heat equation *backwards in time* for $\epsilon ^{2}/4$ .

More examples of invertible data augmentations are found in the paper.

#### SinGAN

SinGAN pushes data augmentation to the limit, by using only a single image as training data and performing data augmentation on it. The GAN architecture is adapted to this training method by using a multi-scale pipeline.

The generator G is decomposed into a pyramid of generators $G=G_{1}\circ G_{2}\circ \cdots \circ G_{N}$ , with the lowest one generating the image $G_{N}(z_{N})$ at the lowest resolution, then the generated image is scaled up to $r(G_{N}(z_{N}))$ , and fed to the next level to generate an image $G_{N-1}(z_{N-1}+r(G_{N}(z_{N})))$ at a higher resolution, and so on. The discriminator is decomposed into a pyramid as well.

### StyleGAN series

The StyleGAN family is a series of architectures published by Nvidia's research division.

#### Progressive GAN

Progressive GAN is a method for training GAN for large-scale image generation stably, by growing a GAN generator from small to large scale in a pyramidal fashion. Like SinGAN, it decomposes the generator as $G=G_{1}\circ G_{2}\circ \cdots \circ G_{N}$ , and the discriminator as $D=D_{1}\circ D_{2}\circ \cdots \circ D_{N}$ .

During training, at first only $G_{N},D_{N}$ are used in a GAN game to generate 4x4 images. Then $G_{N-1},D_{N-1}$ are added to reach the second stage of GAN game, to generate 8x8 images, and so on, until we reach a GAN game to generate 1024x1024 images.

To avoid shock between stages of the GAN game, each new layer is "blended in" (Figure 2 of the paper). For example, this is how the second stage GAN game starts:

- Just before, the GAN game consists of the pair $G_{N},D_{N}$ generating and discriminating 4x4 images.
- Just after, the GAN game consists of the pair $((1-\alpha )+\alpha \cdot G_{N-1})\circ u\circ G_{N},D_{N}\circ d\circ ((1-\alpha )+\alpha \cdot D_{N-1})$ generating and discriminating 8x8 images. Here, the functions $u,d$ are image up- and down-sampling functions, and $\alpha$ is a blend-in factor (much like an alpha in image composing) that smoothly glides from 0 to 1.

#### StyleGAN-1

StyleGAN-1 is designed as a combination of Progressive GAN with neural style transfer.

The key architectural choice of StyleGAN-1 is a progressive growth mechanism, similar to Progressive GAN. Each generated image starts as a constant $4\times 4\times 512$ array, and repeatedly passed through style blocks. Each style block applies a "style latent vector" via affine transform ("adaptive instance normalization"), similar to how neural style transfer uses Gramian matrix. It then adds noise, and normalize (subtract the mean, then divide by the variance).

At training time, usually only one style latent vector is used per image generated, but sometimes two ("mixing regularization") in order to encourage each style block to independently perform its stylization without expecting help from other style blocks (since they might receive an entirely different style latent vector).

After training, multiple style latent vectors can be fed into each style block. Those fed to the lower layers control the large-scale styles, and those fed to the higher layers control the fine-detail styles.

Style-mixing between two images $x,x'$ can be performed as well. First, run a gradient descent to find $z,z'$ such that $G(z)\approx x,G(z')\approx x'$ . This is called "projecting an image back to style latent space". Then, z can be fed to the lower style blocks, and $z'$ to the higher style blocks, to generate a composite image that has the large-scale style of x , and the fine-detail style of $x'$ . Multiple images can also be composed this way.

#### StyleGAN-2

StyleGAN-2 improves upon StyleGAN-1, by using the style latent vector to transform the convolution layer's weights instead, thus solving the "blob" problem.

This was updated by the StyleGAN-2-ADA ("ADA" stands for "adaptive"), which uses invertible data augmentation as described above. It also tunes the amount of data augmentation applied by starting at zero, and gradually increasing it until an "overfitting heuristic" reaches a target level, thus the name "adaptive".

#### StyleGAN-3

StyleGAN-3 improves upon StyleGAN-2 by solving the "texture sticking" problem, which can be seen in the official videos. They analyzed the problem by the Nyquist–Shannon sampling theorem, and argued that the layers in the generator learned to exploit the high-frequency signal in the pixels they operate upon.

To solve this, they proposed imposing strict lowpass filters between each generator's layers, so that the generator is forced to operate on the pixels in a way faithful to the continuous signals they represent, rather than operate on them as merely discrete signals. They further imposed rotational and translational invariance by using more signal filters. The resulting StyleGAN-3 is able to solve the texture sticking problem, as well as generating images that rotate and translate smoothly.


## Other uses

Other than for generative and discriminative modelling of data, GANs have been used for other things.

GANs have been used for transfer learning to enforce the alignment of the latent feature space, such as in deep reinforcement learning. This works by feeding the embeddings of the source and target task to the discriminator which tries to guess the context. The resulting loss is then (inversely) backpropagated through the encoder.
