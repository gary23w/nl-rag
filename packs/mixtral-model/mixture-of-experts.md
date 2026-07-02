---
title: "Mixture of experts"
source: https://en.wikipedia.org/wiki/Mixture_of_experts
domain: mixtral-model
license: CC-BY-SA-4.0
tags: mixtral model, sparse mixture of experts, mistral ai model, sparse expert routing
fetched: 2026-07-02
---

# Mixture of experts

**Mixture of experts** (**MoE**) is a machine learning technique where multiple expert networks (learners) are used to divide a problem space into homogeneous regions. MoE represents a form of ensemble learning. They were also called **committee machines**.

## Basic theory

MoE always has the following components, but they are implemented and combined differently according to the problem being solved:

- Experts $f_{1},...,f_{n}$ , each taking the same input x , and producing outputs $f_{1}(x),...,f_{n}(x)$ .
- A weighting function (also known as a gating function) w , which takes input x and produces a vector of outputs $(w(x)_{1},...,w(x)_{n})$ . This may or may not be a probability distribution, but in both cases, its entries are non-negative.
- $\theta =(\theta _{0},\theta _{1},...,\theta _{n})$ is the set of parameters. The parameter $\theta _{0}$ is for the weighting function. The parameters $\theta _{1},\dots ,\theta _{n}$ are for the experts.
- Given an input x , the mixture of experts produces a single output by combining $f_{1}(x),...,f_{n}(x)$ according to the weights $w(x)_{1},...,w(x)_{n}$ in some way, usually by $f(x)=\sum _{i}w(x)_{i}f_{i}(x)$ .

Both the experts and the weighting function are trained by minimizing some loss function, generally via gradient descent. There is much freedom in choosing the precise form of experts, the weighting function, and the loss function.

### Meta-pi network

The meta-pi network, reported by Hampshire and Waibel, uses $f(x)=\sum _{i}w(x)_{i}f_{i}(x)$ as the output. The model is trained by performing gradient descent on the mean-squared error loss $L:={\frac {1}{N}}\sum _{k}\|y_{k}-f(x_{k})\|^{2}$ . The experts may be arbitrary functions.

In their original publication, they were solving the problem of classifying phonemes in speech signal from 6 different Japanese speakers, 2 females and 4 males. They trained 6 experts, each being a "time-delayed neural network" (essentially a multilayered convolution network over the mel spectrogram). They found that the resulting mixture of experts dedicated 5 experts for 5 of the speakers, but the 6th (male) speaker does not have a dedicated expert, instead his voice was classified by a linear combination of the experts for the other 3 male speakers.

### Adaptive mixtures of local experts

The adaptive mixtures of local experts uses a Gaussian mixture model. Each expert simply predicts a Gaussian distribution, and totally ignores the input. Specifically, the i -th expert predicts that the output is $y\sim N(\mu _{i},I)$ , where $\mu _{i}$ is a learnable parameter. The weighting function is a linear-softmax function: $w(x)_{i}={\frac {e^{k_{i}^{T}x+b_{i}}}{\sum _{j}e^{k_{j}^{T}x+b_{j}}}}$ The mixture of experts predict that the output is distributed according to the log-probability density function: $\ln f_{\theta }(y|x)=\ln \left[\sum _{i}{\frac {e^{k_{i}^{T}x+b_{i}}}{\sum _{j}e^{k_{j}^{T}x+b_{j}}}}N(y|\mu _{i},I)\right]=\ln \left[(2\pi )^{-d/2}\sum _{i}{\frac {e^{k_{i}^{T}x+b_{i}}}{\sum _{j}e^{k_{j}^{T}x+b_{j}}}}e^{-{\frac {1}{2}}\|y-\mu _{i}\|^{2}}\right]$ It is trained by maximal likelihood estimation, that is, gradient ascent on $f(y|x)$ . The gradient for the i -th expert is

$\nabla _{\mu _{i}}\ln f_{\theta }(y|x)={\frac {w(x)_{i}N(y|\mu _{i},I)}{\sum _{j}w(x)_{j}N(y|\mu _{j},I)}}\;(y-\mu _{i})$

and the gradient for the weighting function is $\nabla _{[k_{i},b_{i}]}\ln f_{\theta }(y|x)={\begin{bmatrix}x\\1\end{bmatrix}}{\frac {w(x)_{i}}{\sum _{j}w(x)_{j}N(y|\mu _{j},I)}}(f_{i}(x)-f_{\theta }(y|x))$

For each input-output pair $(x,y)$ , the weighting function is changed to increase the weight on all experts that performed above average, and decrease the weight on all experts that performed below average. This encourages the weighting function to learn to select only the experts that make the right predictions for each input.

The i -th expert is changed to make its prediction closer to y , but the amount of change is proportional to $w(x)_{i}N(y|\mu _{i},I)$ . This has a Bayesian interpretation. Given input x , the prior probability that expert i is the right one is $w(x)_{i}$ , and $N(y|\mu _{i},I)$ is the likelihood of evidence y . So, ${\frac {w(x)_{i}N(y|\mu _{i},I)}{\sum _{j}w(x)_{j}N(y|\mu _{j},I)}}$ is the posterior probability for expert i , and so the rate of change for the i -th expert is proportional to its posterior probability.

In words, the experts that, in hindsight, seemed like the good experts to consult, are asked to learn on the example. The experts that, in hindsight, were not, are left alone.

The combined effect is that the experts become specialized: Suppose two experts are both good at predicting a certain kind of input, but one is slightly better, then the weighting function would eventually learn to favor the better one. After that happens, the lesser expert is unable to obtain a high gradient signal, and becomes even worse at predicting such kind of input. Conversely, the lesser expert can become better at predicting other kinds of input, and increasingly pulled away into another region. This has a positive feedback effect, causing each expert to move apart from the rest and take care of a local region alone (thus the name "*local* experts").

### Hierarchical MoE

Hierarchical mixtures of experts uses multiple levels of gating in a tree. Each gating is a probability distribution over the next level of gatings, and the experts are on the leaf nodes of the tree. They are similar to decision trees.

For example, a 2-level hierarchical MoE would have a first order gating function $w_{i}$ , and second order gating functions $w_{j|i}$ and experts $f_{j|i}$ . The total prediction is then $\sum _{i}w_{i}(x)\sum _{j}w_{j|i}(x)f_{j|i}(x)$ .

### Variants

The mixture of experts, being similar to the gaussian mixture model, can also be trained by the expectation-maximization algorithm, just like gaussian mixture models. Specifically, during the expectation step, the "burden" for explaining each data point is assigned over the experts, and during the maximization step, the experts are trained to improve the explanations they got a high burden for, while the gate is trained to improve its burden assignment. This can converge faster than gradient ascent on the log-likelihood.

The choice of gating function is often softmax. Other than that, gating may use gaussian distributions and exponential families.

Instead of performing a weighted sum of all the experts, in hard MoE, only the highest ranked expert is chosen. That is, $f(x)=f_{\arg \max _{i}w_{i}(x)}(x)$ . This can accelerate training and inference time.

The experts can use more general forms of multivariant gaussian distributions. For example, proposed $f_{i}(y|x)=N(y|A_{i}x+b_{i},\Sigma _{i})$ , where $A_{i},b_{i},\Sigma _{i}$ are learnable parameters. In words, each expert learns to do linear regression, with a learnable uncertainty estimate.

One can use different experts than gaussian distributions. For example, one can use Laplace distribution, or Student's t-distribution. For binary classification, it also proposed logistic regression experts, with $f_{i}(y|x)={\begin{cases}{\frac {1}{1+e^{\beta _{i}^{T}x+\beta _{i,0}}}},&y=0\\1-{\frac {1}{1+e^{\beta _{i}^{T}x+\beta _{i,0}}}},&y=1\end{cases}}$ where $\beta _{i},\beta _{i,0}$ are learnable parameters. This is later generalized for multi-class classification, with multinomial logistic regression experts.

One paper proposed mixture of softmaxes for autoregressive language modelling. Specifically, consider a language model that given a previous text c , predicts the next word x . The network encodes the text into a vector $v_{c}$ , and predicts the probability distribution of the next word as $\mathrm {Softmax} (v_{c}W)$ for an embedding matrix W . In mixture of softmaxes, the model outputs multiple vectors $v_{c,1},\dots ,v_{c,n}$ , and predict the next word as $\sum _{i=1}^{n}p_{i}\;\mathrm {Softmax} (v_{c,i}W_{i})$ , where $p_{i}$ is a probability distribution by a linear-softmax operation on the activations of the hidden neurons within the model. The original paper demonstrated its effectiveness for recurrent neural networks. This was later found to work for Transformers as well.

## Deep learning

The previous section described MoE as it was used before the era of deep learning. After deep learning, MoE found applications in running the largest models, as a simple way to perform *conditional computation*: only parts of the model are used, the parts chosen according to what the input is.

The earliest paper that applies MoE to deep learning dates back to 2013, which proposed to use a different gating network at each layer in a deep neural network. Specifically, each gating is a linear-ReLU-linear-softmax network, and each expert is a linear-ReLU network. Since the output from the gating is not sparse, all expert outputs are needed, and no conditional computation is performed.

The key goal when using MoE in deep learning is to reduce computing cost. Consequently, for each query, only a small subset of the experts should be queried. This makes MoE in deep learning different from classical MoE. In classical MoE, the output for each query is a weighted sum of *all* experts' outputs. In deep learning MoE, the output for each query can only involve a few experts' outputs. Consequently, the key design choice in MoE becomes routing: given a batch of queries, how to route the queries to the best experts.

### Sparsely-gated MoE layer

The sparsely-gated MoE layer, published by researchers from Google Brain, uses feedforward networks as experts, and linear-softmax gating. Similar to the previously proposed hard MoE, they achieve sparsity by a weighted sum of only the top-k experts, instead of the weighted sum of all of them. Specifically, in a MoE layer, there are feedforward networks $f_{1},...,f_{n}$ , and a gating network w . The gating network is defined by $w(x)=\mathrm {softmax} (\mathrm {top} _{k}(Wx+{\text{noise}}))$ , where $\mathrm {top} _{k}$ is a function that keeps the top-k entries of a vector the same, but sets all other entries to $-\infty$ . The addition of noise helps with load balancing.

The choice of k is a hyperparameter that is chosen according to application. Typical values are $k=1,2$ . The $k=1$ version is also called the Switch Transformer. The original Switch Transformer was applied to a T5 language model.

As demonstration, they trained a series of models for machine translation with alternating layers of MoE and LSTM, and compared with deep LSTM models. Table 3 shows that the MoE models used less inference time compute, despite having 30x more parameters.

This architectural module was published in 2017-01, within a few months of the publication of the Transformer architecture (2017-06-12), and they were combined into a multimodal architecture called MultiModel published 4 days later (2017-06-16).

### Load balancing

Vanilla MoE tend to have issues of load balancing: some experts are consulted often, while other experts rarely or not at all. To encourage the gate to select each expert with equal frequency (proper load balancing) within each batch, each MoE layer has two auxiliary loss functions. This is improved by Switch Transformer into a single auxiliary loss function. Specifically, let n be the number of experts, then for a given batch of queries $\{x_{1},x_{2},...,x_{T}\}$ , the auxiliary loss for the batch is $n\sum _{i=1}^{n}f_{i}P_{i}$ Here, $f_{i}={\frac {1}{T}}\#({\text{queries sent to expert }}i)$ is the fraction of tokens that chose expert i , and $P_{i}={\frac {1}{T}}\sum _{j=1}^{T}{\frac {w_{i}(x_{j})}{\sum _{i'\in {\text{experts}}}w_{i'}(x_{j})}}$ is the fraction of weight on expert i . This loss is minimized at 1 , precisely when every expert has equal weight $1/n$ in all situations.

Researchers at DeepSeek designed a variant of MoE, with "shared experts" that are always queried, and "routed experts" that might not be. They found that standard load balancing encourages the experts to be equally consulted, but this then causes experts to replicate the same core capacity, such as English grammar. They proposed the shared experts to learn core capacities that are often used, and let the routed experts to learn the peripheral capacities that are rarely used.

They also proposed "auxiliary-loss-free load balancing strategy", which does not use auxiliary loss. Instead, each expert i has an extra "expert bias" $b_{i}$ . If an expert is being neglected, then their bias increases, and vice versa. During token assignment, each token picks the top-k experts, but with the bias added in. That is: $f(x)=\sum _{i{\text{ is in the top-k of }}\{w(x)_{j}+b_{j}\}_{j}}w(x)_{i}f_{i}(x)$ Note that the expert bias matters for picking the experts, but not in adding up the responses from the experts.

### Capacity factor

Suppose there are n experts in a layer. For a given batch of queries $\{x_{1},x_{2},...,x_{T}\}$ , each query is routed to one or more experts. For example, if each query is routed to one expert as in Switch Transformers, and if the experts are load-balanced, then each expert should expect on average $T/n$ queries in a batch. In practice, the experts cannot expect perfect load balancing: in some batches, one expert might be underworked, while in other batches, it would be overworked.

Since the inputs cannot move through the layer until every expert in the layer has finished the queries it is assigned, load balancing is important. The capacity factor is sometimes used to enforce a hard constraint on load balancing. Each expert is only allowed to process up to $c\cdot T/n$ queries in a batch. The ST-MoE report found $c\in [1.25,2]$ to work well in practice.

### Routing

In the original sparsely-gated MoE, only the top-k experts are queried, and their outputs are weighted-summed. There are other methods. Generally speaking, routing is an assignment problem: How to assign tokens to experts, such that a variety of constraints are followed (such as throughput, load balancing, etc.)? There are typically three classes of routing algorithm: the experts choose the tokens ("expert choice"), the tokens choose the experts (the original sparsely-gated MoE), and a global assigner matching experts and tokens.

During inference, the MoE works over a large batch of tokens at any time. If the tokens were to choose the experts, then some experts might get few tokens, while a few experts get so many tokens that it exceeds their maximum batch size, so they would have to ignore some of the tokens. Similarly, if the experts were to choose the tokens, then some tokens might not be picked by any expert. This is the "token drop" problem. Dropping a token is not necessarily a serious problem, since in Transformers, due to residual connections, if a token is "dropped", it does not disappear. Instead, its vector representation simply passes through the feedforward layer without change.

Other approaches include solving it as a constrained linear programming problem, using reinforcement learning to train the routing algorithm (since picking an expert is a discrete action, like in RL). The token-expert match may involve no learning ("static routing"): It can be done by a deterministic hash function or a random number generator.

### Applications to transformer models

MoE layers are used in the largest transformer models, for which learning and inferring over the full model is too costly. They are typically sparsely-gated, with sparsity 1 or 2. In Transformer models, the MoE layers are often used to select the feedforward layers (typically a linear-ReLU-linear network), appearing in each Transformer block after the multiheaded attention. This is because the feedforward layers take up an increasing portion of the computing cost as models grow larger. For example, in the Palm-540B model, 90% of parameters are in its feedforward layers.

A trained Transformer can be converted to a MoE by duplicating its feedforward layers, with randomly initialized gating, then trained further. This is a technique called "sparse upcycling".

There are a large number of design choices involved in Transformer MoE that affect the training stability and final performance. The OLMoE report describes these in some detail.

As of 2023, models large enough to use MoE tend to be large language models, where each expert has on the order of 10 billion parameters. Other than language models, Vision MoE is a Transformer model with MoE layers. They demonstrated it by training a model with 15 billion parameters. MoE Transformer has also been applied for diffusion models.

A series of large language models from Google used MoE. GShard uses MoE with up to top-2 experts per layer. Specifically, the top-1 expert is always selected, and the top-2th expert is selected with probability proportional to that experts' weight according to the gating function. Later, GLaM demonstrated a language model with 1.2 trillion parameters, each MoE layer using top-2 out of 64 experts. Switch Transformers use top-1 in all MoE layers.

The NLLB-200 by Meta AI is a machine translation model for 200 languages. Each MoE layer uses a hierarchical MoE with two levels. On the first level, the gating function chooses to use either a "shared" feedforward layer, or to use the experts. If using the experts, then another gating function computes the weights and chooses the top-2 experts.

MoE large language models can be adapted for downstream tasks by instruction tuning.

In December 2023, Mistral AI released Mixtral 8x7B under Apache 2.0 license. It is a MoE language model with 46.7B parameters, 8 experts, and sparsity 2. They also released a version finetuned for instruction following.

In March 2024, Databricks released DBRX. It is a MoE language model with 132B parameters, 16 experts, and sparsity 4. They also released a version finetuned for instruction following.
