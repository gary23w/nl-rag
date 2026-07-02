---
title: "Neural network (machine learning) (part 2/2)"
source: https://en.wikipedia.org/wiki/Artificial_neural_network
domain: onnx
license: CC-BY-SA-4.0
tags: onnx format, model interoperability, inference engine, neural network exchange
fetched: 2026-07-02
part: 2/2
---

## Issues

### Training

NNs require millions of training samples to become functional. As of 2026, training a commercial LLM (GPT, Grok, Gemini) typically required hundreds of thousands of computers, and cost 10s of millions of dollars.

### Theory

A central claim of NNs is that they embody new and powerful general principles for processing information. However, at root they use statistical long-developed methods.

### Hardware

Neural networks require enormous computing resources for training. While the brain requires only 20 watts of power, training commercial transformers requires (2026) data centers with hundreds of megawatts.

From 1991 to 2015, computing power, especially as delivered by GPGPUs (on GPUs), increased around a million-fold, enabling the use of the backpropagation algorithm.

Neuromorphic engineering or a physical neural network constructed non-von-Neumann chips to directly implement neural networks in circuitry. For example, Alphabet introduced custom chips (Tensor Processing Unit).

### Concept drift

The statistical properties of input data may change over time, a phenomenon known as concept drift or non-stationarity. Drift can reduce predictive accuracy and lead to unreliable or biased decisions if it is not detected and corrected. In practice, this means that the model's accuracy in deployment may differ substantially from levels observed during training.

Several strategies have been developed to monitor neural networks for drift and degradation:

- **Error-based monitoring**: comparing current predictions against ground-truth labels. This approach directly quantifies predictive performance but may be impractical when labels are delayed or impractical to obtain.
- **Data distribution monitoring**: detecting changes in the input data distribution using statistical tests, divergence measures, or density-ratio estimation.
- **Representation monitoring**: tracking the distribution of internal *embeddings* or hidden-layer features. Shifts in the latent representation can indicate nonstationarity even when labels are unavailable. Statistical methods such as *statistical process control* charts have been adapted for this purpose.

### Dataset bias

Neural networks are dependent on the quality of their training data; low quality data can lead the model to product poor results. Biased data produces biased results, requiring trainers to detect and correct them. For example, data that underrepresents some demographic groups may prevent cause errors, e.g., in facial recognition and law enforcement. In 2018, Amazon scrapped a recruiting tool because the model favored men over women for jobs in software engineering due to the larger number of male workers in the field. The system penalized resumes with the word "woman" or the name of a women's college. One corrective is to add synthetic data to offset the bias.

### Lack of interpretability

NNs are "black box" systems that have complicated understanding of their decision-making processes. NNs are further vulnerable to adversarial examples ("poison"), that can cause incorrect predictions.

These concerns have led to increased research in explainable artificial intelligence (XAI), robust machine learning, and hybrid AI approaches that combine neural learning with symbolic reasoning. Advocates of hybrid models also say that such a mixture can better capture the mechanisms of the human mind.

Progress has included local vs. non-local learning and shallow vs. deep architectures.

Analyzing human thought (a biological neural network) has also proven difficult.


## Gallery

- (A single-layer feedforward artificial neural network. Arrows originating from x 2 {\displaystyle x_{2}} are omitted for clarity. There are p inputs to this network and q outputs. In this system, the value of the qth output, y q {\displaystyle y_{q}} , is calculated as y q = K ⋅ ( ∑ i ( x i w i q ) − b q ) . {\displaystyle y_{q}=K\cdot \left(\sum _{i}(x_{i}w_{iq})-b_{q}\right).}) A single-layer feedforward neural network. Arrows originating from $x_{2}$ are omitted for clarity. There are *p* inputs to this network and *q* outputs. In this system, the value of the *q*th output, $y_{q}$ , is calculated as $y_{q}=K\cdot \left(\sum _{i}(x_{i}w_{iq})-b_{q}\right).$
- (A two-layer feedforward neural network) A two-layer feedforward neural network
- (An neural network) An neural network
- (An NN dependency graph) An NN dependency graph
- (A single-layer feedforward neural network with 4 inputs, 6 hidden nodes and 2 outputs. Given position state and direction, it outputs wheel based control values.) A single-layer feedforward neural network with 4 inputs, 6 hidden nodes and 2 outputs. Given position state and direction, it outputs wheel based control values.
- (A two-layer feedforward neural network with 8 inputs, 2x8 hidden nodes and 2 outputs. Given position state, direction and other environment values, it outputs thruster based control values.) A two-layer feedforward neural network with 8 inputs, 2x8 hidden nodes and 2 outputs. Given position state, direction and other environment values, it outputs thruster based control values.
- (Parallel pipeline structure of CMAC neural network. This learning algorithm can converge in one step.) Parallel pipeline structure of CMAC neural network. This learning algorithm can converge in one step.
