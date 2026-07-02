---
title: "Graph neural network"
source: https://en.wikipedia.org/wiki/Graph_neural_network
domain: graph-neural-networks
license: CC-BY-SA-4.0
tags: graph neural network, message passing, node embedding, graph representation, relational learning
fetched: 2026-07-02
---

# Graph neural network

**Graph neural networks** (**GNNs**) are artificial neural networks designed for tasks whose inputs are graphs.

Because graphs usually do not have a canonical ordering of their nodes, GNN architectures are commonly designed to be permutation equivariant: reordering the nodes in the input reorders the corresponding node representations in the same way. For graph-level prediction tasks, GNNs typically use a permutation-invariant readout function, whose output is unchanged by the ordering of the nodes.

A prominent example is molecular drug design. Molecules can be represented as graphs, with nodes for atoms and edges for atomic bonds, often including known chemical properties as features. Inputs may thus differ in size, due to varying number of atoms and bonds. A graph-level task may be to predict the efficacy of a given molecule for a specific medical application, such as eliminating *E. coli* bacteria.

The key design element of GNNs is the use of *pairwise message passing*, such that graph nodes iteratively update their representations by exchanging information with their neighbors. Several GNN architectures have been proposed, which implement different flavors of message passing, started by recursive or convolutional constructive approaches. A 2022 position paper argued that many architectures described as going "beyond" message passing can instead be interpreted as message passing over suitably modified graphs, and proposed the term "augmented message passing" for such approaches.

In the more general subject of "geometric deep learning", certain existing neural network architectures can be interpreted as GNNs operating on suitably defined graphs. A convolutional neural network layer, in the context of computer vision, can be considered a GNN applied to graphs whose nodes are pixels, and only adjacent pixels are connected by edges in the graph. A transformer layer, in natural language processing, can be considered a GNN applied to complete graphs whose nodes are words or tokens in a passage of natural language text.

Relevant application domains for GNNs include natural language processing, social networks, citation networks, molecular biology, chemistry, physics and NP-hard combinatorial optimization problems.

Open source libraries implementing GNNs include PyTorch Geometric (PyTorch), TensorFlow GNN (TensorFlow), Deep Graph Library (framework agnostic), jraph (Google JAX), and GraphNeuralNetworks.jl/GeometricFlux.jl (Julia, Flux).

## Architecture

The architecture of a generic GNN implements the following fundamental layers:

1. *Permutation-equivariant layers*: a permutation equivariant layer maps a representation of a graph into an updated representation of the same graph. In the literature, permutation equivariant layers are implemented via pairwise message passing between graph nodes. Intuitively, in a message passing layer, nodes *update* their representations by *aggregating* the *messages* received from their immediate neighbours. As such, each message passing layer increases the receptive field of the GNN by one hop.
2. *Local pooling*: a local pooling layer coarsens the graph via downsampling. Local pooling is used to increase the receptive field of a GNN, in a similar fashion to pooling layers in convolutional neural networks. Examples include k-nearest neighbours pooling, top-k pooling, and self-attention pooling.
3. *Global pooling*: a global pooling layer, also known as *readout* layer, provides fixed-size representation of the whole graph. The global pooling layer must be permutation invariant, such that permutations in the ordering of graph nodes and edges do not alter the final output. Examples include element-wise sum, mean or maximum.

Standard message-passing GNNs are at most as expressive as the Weisfeiler Leman graph isomorphism test. In practice, this means that there exist different graph structures that cannot be distinguished by GNNs. More powerful GNNs operating on higher-dimension geometries such as simplicial complexes can be designed. As of 2022, whether or not future architectures will overcome the message passing primitive is an open research question.

## Message passing layers

Message passing layers are permutation-equivariant layers mapping a graph into an updated representation of the same graph. Formally, they can be expressed as message passing neural networks (MPNNs).

Let $G=(V,E)$ be a graph, where V is the node set and E is the edge set. Let $N_{u}$ be the neighbourhood of some node $u\in V$ . Additionally, let $\mathbf {x} _{u}$ be the features of node $u\in V$ , and $\mathbf {e} _{uv}$ be the features of edge $(u,v)\in E$ . An MPNN layer can be expressed as follows:

$\mathbf {h} _{u}=\phi \left(\mathbf {x} _{u},\bigoplus _{v\in N_{u}}\psi (\mathbf {x} _{u},\mathbf {x} _{v},\mathbf {e} _{uv})\right)$

where $\phi$ and $\psi$ are differentiable functions (e.g., artificial neural networks), and $\bigoplus$ is a permutation invariant aggregation operator that can accept an arbitrary number of inputs (e.g., element-wise sum, mean, or max). In particular, $\phi$ and $\psi$ are referred to as *update* and *message* functions, respectively. Intuitively, in an MPNN computational block, graph nodes *update* their representations by *aggregating* the *messages* received from their neighbours.

The outputs of one or more MPNN layers are node representations $\mathbf {h} _{u}$ for each node $u\in V$ in the graph. Node representations can be employed for any downstream task, such as node/graph classification or edge prediction.

Graph nodes in an MPNN update their representation aggregating information from their immediate neighbours. As such, stacking n MPNN layers means that one node will be able to communicate with nodes that are at most n "hops" away. In principle, to ensure that every node receives information from every other node, one would need to stack a number of MPNN layers equal to the graph diameter. However, stacking many MPNN layers may cause issues such as oversmoothing and oversquashing. Oversmoothing refers to the issue of node representations becoming indistinguishable. Oversquashing refers to the bottleneck that is created by squeezing long-range dependencies into fixed-size representations. Countermeasures such as skip connections (as in residual neural networks), gated update rules and jumping knowledge can mitigate oversmoothing. Modifying the final layer to be a fully-adjacent layer, i.e., by considering the graph as a complete graph, can mitigate oversquashing in problems where long-range dependencies are required.

Other "flavours" of MPNN have been developed in the literature, such as graph convolutional networks and graph attention networks, whose definitions can be expressed in terms of the MPNN formalism.

### Graph convolutional network

The graph convolutional network (GCN) was first introduced by Thomas Kipf and Max Welling in 2017.

A GCN layer defines a first-order approximation of a localized spectral filter on graphs. GCNs can be understood as a generalization of convolutional neural networks to graph-structured data.

The formal expression of a GCN layer reads as follows:

$\mathbf {H} =\sigma \left({\tilde {\mathbf {D} }}^{-{\frac {1}{2}}}{\tilde {\mathbf {A} }}{\tilde {\mathbf {D} }}^{-{\frac {1}{2}}}\mathbf {X} \mathbf {\Theta } \right)$

where $\mathbf {H}$ is the matrix of node representations $\mathbf {h} _{u}$ , $\mathbf {X}$ is the matrix of node features $\mathbf {x} _{u}$ , $\sigma (\cdot )$ is an activation function (e.g., ReLU), ${\tilde {\mathbf {A} }}$ is the graph adjacency matrix with the addition of self-loops, ${\tilde {\mathbf {D} }}$ is the graph degree matrix with the addition of self-loops, and $\mathbf {\Theta }$ is a matrix of trainable parameters.

In particular, let $\mathbf {A}$ be the graph adjacency matrix: then, one can define ${\tilde {\mathbf {A} }}=\mathbf {A} +\mathbf {I}$ and ${\tilde {\mathbf {D} }}_{ii}=\sum _{j\in V}{\tilde {A}}_{ij}$ , where $\mathbf {I}$ denotes the identity matrix. This normalization ensures that the eigenvalues of ${\tilde {\mathbf {D} }}^{-{\frac {1}{2}}}{\tilde {\mathbf {A} }}{\tilde {\mathbf {D} }}^{-{\frac {1}{2}}}$ are bounded in the range $[0,1]$ , avoiding numerical instabilities and exploding/vanishing gradients.

A limitation of GCNs is that they do not allow multidimensional edge features $\mathbf {e} _{uv}$ . It is however possible to associate scalar weights $w_{uv}$ to each edge by imposing $A_{uv}=w_{uv}$ , i.e., by setting each nonzero entry in the adjacency matrix equal to the weight of the corresponding edge.

### Graph attention network

The graph attention network (GAT) was introduced by Petar Veličković et al. in 2018.

A graph attention network is a combination of a GNN and an attention layer. The implementation of attention layer in graphical neural networks helps provide attention or focus to the important information from the data instead of focusing on the whole data.

A multi-head GAT layer can be expressed as follows:

$\mathbf {h} _{u}={\overset {K}{\underset {k=1}{\Big \Vert }}}\sigma \left(\sum _{v\in N_{u}}\alpha _{uv}^{k}\mathbf {W} ^{k}\mathbf {x} _{v}\right)$

where K is the number of attention heads, ${\Big \Vert }$ denotes vector concatenation, $\sigma (\cdot )$ is an activation function (e.g., ReLU), $N_{u}$ is the set of immediate neighbor nodes of node u , including node u itself, $\alpha _{uv}^{k}$ are attention coefficients for the k -th attention head, and $W^{k}$ is a matrix of trainable parameters for the k -th attention head.

For the final GAT layer, the outputs from each attention head are averaged before the application of the activation function. Formally, the final GAT layer can be written as:

$\mathbf {h} _{u}=\sigma \left({\frac {1}{K}}\sum _{k=1}^{K}\sum _{v\in N_{u}}\alpha _{uv}^{k}\mathbf {W} ^{k}\mathbf {x} _{v}\right)$

Attention in Machine Learning is a technique that mimics cognitive attention. In the context of learning on graphs, the attention coefficient $\alpha _{uv}$ measures *how important* node v is to node u .

Normalized attention coefficients are computed as follows:

$\alpha _{uv}={\frac {\exp({\text{LeakyReLU}}\left(\mathbf {a} ^{T}[\mathbf {W} \mathbf {x} _{u}\Vert \mathbf {W} \mathbf {x} _{v}\Vert \mathbf {e} _{uv}]\right))}{\sum _{z\in N_{u}}\exp({\text{LeakyReLU}}\left(\mathbf {a} ^{T}[\mathbf {W} \mathbf {x} _{u}\Vert \mathbf {W} \mathbf {x} _{z}\Vert \mathbf {e} _{uz}]\right))}}$

where $\mathbf {a}$ is a vector of learnable weights, $\cdot ^{T}$ indicates transposition, $\mathbf {e} _{uv}$ are the edge features (if present), and ${\text{LeakyReLU}}$ is a modified ReLU activation function. Attention coefficients are then normalized via softmax to make them easily comparable across different nodes.

A GCN can be seen as a special case of a GAT where attention coefficients are not learnable, but fixed and equal to the edge weights $w_{uv}$ .

### Gated graph sequence neural network

The gated graph sequence neural network (GGS-NN) was introduced by Yujia Li et al. in 2015. The GGS-NN extends the GNN formulation by Scarselli et al. to output sequences. The message passing framework is implemented as an update rule to a gated recurrent unit (GRU) cell.

A GGS-NN can be expressed as follows:

$\mathbf {h} _{u}^{(0)}=\mathbf {x} _{u}\,\Vert \,\mathbf {0}$

$\mathbf {m} _{u}^{(l+1)}=\sum _{v\in N_{u}}\mathbf {\Theta } \mathbf {h} _{v}$

$\mathbf {h} _{u}^{(l+1)}={\text{GRU}}(\mathbf {m} _{u}^{(l+1)},\mathbf {h} _{u}^{(l)})$

where $\Vert$ denotes vector concatenation, $\mathbf {0}$ is a vector of zeros, $\mathbf {\Theta }$ is a matrix of learnable parameters, ${\text{GRU}}$ is a GRU cell, and l denotes the sequence index. In a GGS-NN, the node representations are regarded as the hidden states of a GRU cell. The initial node features $\mathbf {x} _{u}^{(0)}$ are zero-padded up to the hidden state dimension of the GRU cell. The same GRU cell is used for updating representations for each node.

## Local pooling layers

Local pooling layers, transform a graph into a smaller coarsened graph before subsequent message-passing or readout layers. In contrast to global pooling, which aggregates all node representations into a single graph-level representation, local pooling produces an intermediate graph with its own node-feature matrix and adjacency matrix. Pooling methods differ in how this coarsened graph is constructed: node-selection methods, such as top-k pooling and self-attention pooling, retain a subset of the original nodes, whereas node-clustering methods assign original nodes to clusters, which become new nodes, or supernodes, in the coarsened graph. In each case, the input is a graph represented by a node-feature matrix $\mathbf {X}$ and an adjacency matrix $\mathbf {A}$ . The output is a coarsened node-feature matrix $\mathbf {X} '$ and a coarsened adjacency matrix $\mathbf {A} '$ .

### Differentiable pooling

Differentiable pooling, or DiffPool, is a node-clustering pooling method introduced in 2018. Instead of selecting a subset of the original nodes, DiffPool learns a soft assignment of nodes to clusters (by using scores between 0 and 1). These clusters become the nodes of the coarsened graph used by the next GNN layer.

Given a node-feature matrix $\mathbf {X}$ and an adjacency matrix $\mathbf {A}$ , DiffPool uses two graph neural networks. One computes updated node embeddings,

$\mathbf {Z} =\operatorname {GNN} _{\mathrm {embed} }(\mathbf {X} ,\mathbf {A} )$

and the other computes an assignment matrix,

$\mathbf {S} =\operatorname {softmax} (\operatorname {GNN} _{\mathrm {pool} }(\mathbf {X} ,\mathbf {A} ))$

where $S_{ij}$ denotes the soft assignment of node i to cluster j . The coarsened node-feature matrix and adjacency matrix are then computed as

$\mathbf {X} '=\mathbf {S} ^{T}\mathbf {Z}$

$\mathbf {A} '=\mathbf {S} ^{T}\mathbf {A} \mathbf {S}$

In this formulation, each new node in $\mathbf {X} '$ represents a learned cluster of nodes from the previous graph, and edges in $\mathbf {A} '$ represent aggregate connectivity between clusters. Because the assignment matrix is differentiable, DiffPool can be trained end-to-end together with the surrounding GNN layers. The original formulation additionally introduced auxiliary losses to encourage nearby nodes to be assigned to similar clusters and to encourage confident cluster assignments.

### Top-k pooling

We first set $\mathbf {y} ={\frac {\mathbf {X} \mathbf {p} }{\Vert \mathbf {p} \Vert }}$ where $\mathbf {p}$ is a learnable projection vector that computes a scalar projection value for each node.

The top-k pooling layer can then be formalised as follows:

$\mathbf {X} '=(\mathbf {X} \odot {\text{sigmoid}}(\mathbf {y} ))_{\mathbf {i} }$

$\mathbf {A} '=\mathbf {A} _{\mathbf {i} ,\mathbf {i} }$

where $\mathbf {i} ={\text{top}}_{k}(\mathbf {y} )$ is the subset of nodes with the top-k highest projection scores, $\odot$ denotes element-wise matrix multiplication, and ${\text{sigmoid}}(\cdot )$ is the sigmoid function. In other words, the nodes with the top-k highest projection scores are retained in the new adjacency matrix $\mathbf {A} '$ . The ${\text{sigmoid}}(\cdot )$ operation makes the projection vector $\mathbf {p}$ trainable by backpropagation, which otherwise would produce discrete outputs.

### Self-attention pooling

Using $\mathbf {y} ={\text{GNN}}(\mathbf {X} ,\mathbf {A} )$ as a generic permutation equivariant GNN layer (e.g., GCN, GAT, MPNN), the self-attention pooling layer can then be formalised as follows:

$\mathbf {X} '=(\mathbf {X} \odot \mathbf {y} )_{\mathbf {i} }$

$\mathbf {A} '=\mathbf {A} _{\mathbf {i} ,\mathbf {i} }$

where $\mathbf {i} ={\text{top}}_{k}(\mathbf {y} )$ is the subset of nodes with the top-k highest projection scores, $\odot$ denotes element-wise matrix multiplication.

The self-attention pooling layer can be seen as an extension of the top-k pooling layer. Differently from top-k pooling, the self-attention scores computed in self-attention pooling account both for the graph features and the graph topology.

## Heterophilic Graph Learning

The homophily principle, i.e., nodes with the same labels or similar attributes are more likely to be connected, has been commonly believed to be the main reason for the superiority of GNNs over traditional Neural Networks (NNs) on graph-structured data, especially on node-level tasks. However, recent work has identified a non-trivial set of datasets where GNN's performance compared to the NN's is not satisfactory. Heterophily, i.e., low homophily, has been considered the main cause of this empirical observation. People have begun to revisit and re-evaluate most existing graph models in the heterophily scenario across various kinds of graphs, e.g., heterogeneous graphs, temporal graphs and hypergraphs. Moreover, numerous graph-related applications are found to be closely related to the heterophily problem, e.g. graph fraud/anomaly detection, graph adversarial attacks and robustness, privacy, federated learning and point cloud segmentation, graph clustering, recommender systems, generative models, link prediction, graph classification and coloring, etc. In the past few years, considerable effort has been devoted to studying and addressing the heterophily issue in graph learning.

## Scalability and distributed training

Training GNNs on large graphs presents computational challenges that differ substantially from those in other neural network architectures. Two broad problem settings arise: training on a single very large graph (such as a social network with billions of nodes), and training on collections of large individual graphs (such as molecular systems requiring higher-order interaction modeling).

For the single large graph setting, sampling-based methods reduce memory requirements by operating on subgraphs rather than the full graph. Cluster-GCN partitions the graph into subgraphs using graph partitioning algorithms, training the model on each partition in sequence. GraphSAINT instead samples subgraphs stochastically during training, constructing unbiased estimators for the full graph loss. Distributed frameworks such as DistDGL extend training to multi-machine settings, managing the inter-machine communication required for neighborhood aggregation when a graph's nodes are distributed across machines.

For tasks such as atomic simulations, a different bottleneck arises: GNN architectures that model higher-order interactions between triplets or quadruplets of atoms are memory-intensive at the level of individual graphs, making standard data parallelism — where each GPU processes a separate sample — insufficient when individual graphs exceed single-device memory. **Graph Parallelism** addresses this by distributing a single input graph across multiple GPUs, partitioning nodes and edges across devices rather than distributing samples across devices. This approach enabled GNNs with hundreds of millions to billions of parameters to be trained on atomic systems that would otherwise exceed single-device memory, and has been applied to the development of large-scale universal interatomic potentials.

## Applications

Social networks are a major application domain for GNNs due to their natural representation as social graphs. GNNs are used to develop recommender systems based on both social relations and item relations.

### Combinatorial optimization

GNNs are used as fundamental building blocks for several combinatorial optimization algorithms. Examples include computing shortest paths or Eulerian circuits for a given graph, deriving chip placements superior or competitive to handcrafted human solutions, and improving expert-designed branching rules in branch and bound.

### Cyber security

When viewed as a graph, a network of computers can be analyzed with GNNs for anomaly detection. Anomalies within provenance graphs often correlate to malicious activity within the network. GNNs have been used to identify these anomalies on individual nodes and within paths to detect malicious processes, or on the edge level to detect lateral movement.

### Water distribution networks

Water distribution systems can be modeled as graphs. GNNs have been applied to water demand forecasting, interconnecting District Metered Areas (DMAs) to improve the forecasting capacity. Another application is the development of metamodels.

### Computer Vision

To represent an image as a graph structure, the image is first divided into multiple patches, each of which is treated as a node in the graph. Edges are then formed by connecting each node to its nearest neighbors based on spatial or feature similarity. This graph-based representation enables the application of graph learning models to visual tasks. The relational structure helps to enhance feature extraction and improve performance on image understanding.

### Text and NLP

Graph-based representation of text helps to capture deeper semantic relationships between words. Many studies have used graph networks to enhance performance in various text processing tasks such as text classification, question answering, Neural Machine Translation (NMT), event extraction, fact verification, etc.

### Atomic simulations and materials science

GNNs have become a primary tool for modeling atomic interactions in computational chemistry and materials science, where molecules and crystal structures are naturally represented as graphs with atoms as nodes and chemical bonds or spatial proximity as edges. A key advantage over traditional quantum chemistry methods such as density functional theory (DFT) is the reduction in computational cost from O(n³) to O(n), enabling simulations at previously impractical scales.

Early GNN architectures for this domain include SchNet (2017), which introduced continuous-filter convolutional layers for learning on 3D molecular structures, and DimeNet (2020), which incorporated angular information between atoms to improve geometric expressivity. Subsequent equivariant architectures such as NequIP and MACE, which respect the rotational and translational symmetries of physical systems, achieved significant accuracy improvements on standard benchmarks including QM9, MD17, and the Materials Project.

Large open datasets have driven rapid progress in this area. The Open Catalyst 2020 (OC20) dataset, comprising over 260 million DFT calculations of adsorbate-catalyst surface interactions, established a widely used benchmark for energy and force prediction tasks relevant to catalyst discovery. The Materials Project and Alexandria databases have similarly provided large-scale crystal structure data for training universal interatomic potentials. More recent datasets including OMat24 and OMol25 have extended coverage to organic molecules and complex materials at greater computational scale.

These datasets have enabled the development of universal machine learning interatomic potentials (MLIPs) — models trained across diverse chemical domains rather than on system-specific data. Examples include CHGNet, M3GNet, MACE-MP, and Meta FAIR's Universal Models for Atoms (UMA), the latter trained on approximately 500 million atomic structures spanning molecules, materials, and catalysts. GNoME, developed by Google DeepMind, applied GNNs to predict the stability of crystal structures, reporting the identification of millions of new stable candidate materials.
