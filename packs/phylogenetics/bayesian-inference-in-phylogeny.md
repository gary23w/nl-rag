---
title: "Bayesian inference in phylogeny"
source: https://en.wikipedia.org/wiki/Bayesian_inference_in_phylogeny
domain: phylogenetics
license: CC-BY-SA-4.0
tags: computational phylogenetics, phylogenetic tree, maximum parsimony, neighbor joining
fetched: 2026-07-02
---

# Bayesian inference in phylogeny

**Bayesian inference of phylogeny** combines the information in the prior and in the data likelihood to create the so-called posterior probability of trees, which is the probability that the tree is correct given the data, the prior and the likelihood model. Bayesian inference was introduced into molecular phylogenetics in the 1990s by three independent groups: Bruce Rannala and Ziheng Yang in Berkeley, Bob Mau in Madison, and Shuying Li in University of Iowa, the last two being PhD students at the time. The approach has become very popular since the release of the MrBayes software in 2001, and is now one of the most popular methods in molecular phylogenetics.

## Bayesian inference of phylogeny background and bases

Bayesian inference refers to a probabilistic method developed by Reverend Thomas Bayes based on Bayes' theorem. Published posthumously in 1763 it was the first expression of inverse probability and the basis of Bayesian inference. Independently, unaware of Bayes' work, Pierre-Simon Laplace developed Bayes' theorem in 1774.

Bayesian inference or the inverse probability method was the standard approach in statistical thinking until the early 1900s before RA Fisher developed what's now known as the classical/frequentist/Fisherian inference. Computational difficulties and philosophical objections had prevented the widespread adoption of the Bayesian approach until the 1990s, when Markov Chain Monte Carlo (MCMC) algorithms revolutionized Bayesian computation.

The Bayesian approach to phylogenetic reconstruction combines the prior probability of a tree P(A) with the likelihood of the data (B) to produce a posterior probability distribution on trees P(A|B). The posterior probability of a tree will be the probability that the tree is correct, given the prior, the data, and the correctness of the likelihood model.

MCMC methods can be described in three steps: first using a stochastic mechanism a new state for the Markov chain is proposed. Secondly, the probability of this new state to be correct is calculated. Thirdly, a new random variable (0,1) is proposed. If this new value is less than the acceptance probability the new state is accepted and the state of the chain is updated. This process is run thousands or millions of times. The number of times a single tree is visited during the course of the chain is an approximation of its posterior probability. Some of the most common algorithms used in MCMC methods include the Metropolis–Hastings algorithms, the Metropolis-Coupling MCMC (MC³) and the LOCAL algorithm of Larget and Simon.

### Metropolis–Hastings algorithm

One of the most common MCMC methods used is the Metropolis–Hastings algorithm, a modified version of the original Metropolis algorithm. It is a widely used method to sample randomly from complicated and multi-dimensional distribution probabilities. The Metropolis algorithm is described in the following steps:

1. An initial tree, Ti, is randomly selected.
2. A neighbour tree, Tj, is selected from the collection of trees.
3. The ratio, R, of the probabilities (or probability density functions) of Tj and Ti is computed as follows: R = f(Tj)/f(Ti)
4. If R ≥ 1, Tj is accepted as the current tree.
5. If R < 1, Tj is accepted as the current tree with probability R, otherwise Ti is kept.
6. At this point the process is repeated from Step 2 N times.

The algorithm keeps running until it reaches an equilibrium distribution. It also assumes that the probability of proposing a new tree Tj when we are at the old tree state Ti, is the same probability of proposing Ti when we are at Tj. When this is not the case Hastings corrections are applied. The aim of Metropolis-Hastings algorithm is to produce a collection of states with a determined distribution until the Markov process reaches a stationary distribution. The algorithm has two components:

1. A potential transition from one state to another (i → j) using a transition probability function qi,j
2. Movement of the chain to state j with probability αi,j and remains in i with probability 1 – αi,j.

### Metropolis-coupled MCMC

Metropolis-coupled MCMC algorithm (MC³) has been proposed to solve a practical concern of the Markov chain moving across peaks when the target distribution has multiple local peaks, separated by low valleys, are known to exist in the tree space. This is the case during heuristic tree search under maximum parsimony (MP), maximum likelihood (ML), and minimum evolution (ME) criteria, and the same can be expected for stochastic tree search using MCMC. This problem will result in samples not approximating correctly to the posterior density. The (MC³) improves the mixing of Markov chains in presence of multiple local peaks in the posterior density. It runs multiple (m) chains in parallel, each for n iterations and with different stationary distributions $\pi _{j}(.)\$ , $j=1,2,\ldots ,m\$ , where the first one, $\pi _{1}=\pi \$ is the target density, while $\pi _{j}\$ , $j=2,3,\ldots ,m\$ are chosen to improve mixing. For example, one can choose incremental heating of the form:

$\pi _{j}(\theta )=\pi (\theta )^{1/[1+\lambda (j-1)]},\ \ \lambda >0,$

so that the first chain is the cold chain with the correct target density, while chains $2,3,\ldots ,m$ are heated chains. Note that raising the density $\pi (.)$ to the power $1/T\$ with $T>1\$ has the effect of flattening out the distribution, similar to heating a metal. In such a distribution, it is easier to traverse between peaks (separated by valleys) than in the original distribution. After each iteration, a swap of states between two randomly chosen chains is proposed through a Metropolis-type step. Let $\theta ^{(j)}\$ be the current state in chain $j\$ , $j=1,2,\ldots ,m\$ . A swap between the states of chains $i\$ and $j\$ is accepted with probability:

$\alpha ={\frac {\pi _{i}(\theta ^{(j)})\pi _{j}(\theta ^{(i)})}{\pi _{i}(\theta ^{(i)})\pi _{j}(\theta ^{(j)})}}\$

At the end of the run, output from only the cold chain is used, while those from the hot chains are discarded. Heuristically, the hot chains will visit the local peaks rather easily, and swapping states between chains will let the cold chain occasionally jump valleys, leading to better mixing. However, if $\pi _{i}(\theta )/\pi _{j}(\theta )\$ is unstable, proposed swaps will seldom be accepted. This is the reason for using several chains which differ only incrementally.

An obvious disadvantage of the algorithm is that $m\$ chains are run and only one chain is used for inference. For this reason, $\mathrm {MC} ^{3}\$ is ideally suited for implementation on parallel machines, since each chain will in general require the same amount of computation per iteration.

### LOCAL algorithm of Larget and Simon

The LOCAL algorithms offers a computational advantage over previous methods and demonstrates that a Bayesian approach is able to assess uncertainty computationally practical in larger trees. The LOCAL algorithm is an improvement of the GLOBAL algorithm presented in Mau, Newton and Larget (1999) in which all branch lengths are changed in every cycle. The LOCAL algorithms modifies the tree by selecting an internal branch of the tree at random. The nodes at the ends of this branch are each connected to two other branches. One of each pair is chosen at random. Imagine taking these three selected edges and stringing them like a clothesline from left to right, where the direction (left/right) is also selected at random. The two endpoints of the first branch selected will have a sub-tree hanging like a piece of clothing strung to the line. The algorithm proceeds by multiplying the three selected branches by a common random amount, akin to stretching or shrinking the clothesline. Finally the leftmost of the two hanging sub-trees is disconnected and reattached to the clothesline at a location selected uniformly at random. This would be the candidate tree.

Suppose we began by selecting the internal branch with length $t_{8}\$ that separates taxa $A\$ and $B\$ from the rest. Suppose also that we have (randomly) selected branches with lengths $t_{1}\$ and $t_{9}\$ from each side, and that we oriented these branches. Let $m=t_{1}+t_{8}+t_{9}\$ , be the current length of the clothesline. We select the new length to be $m^{\star }=m\exp(\lambda (U_{1}-0.5))\$ , where $U_{1}\$ is a uniform random variable on $(0,1)\$ . Then for the LOCAL algorithm, the acceptance probability can be computed to be:

${\frac {h(y)}{h(x)}}\times {\frac {{m^{\star }}^{3}}{m^{3}}}\$

#### Assessing convergence

To estimate a branch length t of a 2-taxon tree under JC, in which $n_{1}$ sites are unvaried and $n_{2}$ are variable, assume exponential prior distribution with rate $\lambda \$ . The density is $p(t)=\lambda e^{-\lambda t}\$ . The probabilities of the possible site patterns are:

$1/4\left(1/4+3/4e^{-4/3t}\right)\$

for unvaried sites, and

$1/4\left(1/4-1/4e^{-4/3t}\right)\$

Thus the unnormalized posterior distribution is:

$h(t)=\left(1/4\right)^{n_{1}+n_{2}}\left(1/4+3/4{e^{-4/3t}}^{n_{1}}\right)\$

or, alternately,

$h(t)=\left(1/4-1/4{e^{-4/3t}}^{n_{2}}\right)(\lambda e^{-\lambda t})\$

Update branch length by choosing new value uniformly at random from a window of half-width $w\$ centered at the current value:

$t^{\star }=|t+U|\$

where $U\$ is uniformly distributed between $-w\$ and $w\$ . The acceptance probability is:

$h(t^{\star })/h(t)\$

Example: $n_{1}=70\$ , $n_{2}=30\$ . We will compare results for two values of $w\$ , $w=0.1\$ and $w=0.5\$ . In each case, we will begin with an initial length of $5\$ and update the length $2000\$ times.

## Maximum parsimony and maximum likelihood

There are many approaches to reconstructing phylogenetic trees, each with advantages and disadvantages, and there is no straightforward answer to "what is the best method?". Maximum parsimony (MP) and maximum likelihood (ML) are traditional methods widely used for the estimation of phylogenies and both use character information directly, as Bayesian methods do.

Maximum Parsimony recovers one or more optimal trees based on a matrix of discrete characters for a certain group of taxa and it does not require a model of evolutionary change. MP gives the most simple explanation for a given set of data, reconstructing a phylogenetic tree that includes as few changes across the sequences as possible. The support of the tree branches is represented by bootstrap percentage. For the same reason that it has been widely used, its simplicity, MP has also received criticism and has been pushed into the background by ML and Bayesian methods. MP presents several problems and limitations. As shown by Felsenstein (1978), MP might be statistically inconsistent, meaning that as more and more data (e.g. sequence length) is accumulated, results can converge on an incorrect tree and lead to long branch attraction, a phylogenetic phenomenon where taxa with long branches (numerous character state changes) tend to appear more closely related in the phylogeny than they really are. For morphological data, recent simulation studies suggest that parsimony may be less accurate than trees built using Bayesian approaches, potentially due to overprecision, although this has been disputed. Studies using novel simulation methods have demonstrated that differences between inference methods result from the search strategy and consensus method employed, rather than the optimization used.

As in maximum parsimony, maximum likelihood will evaluate alternative trees. However it considers the probability of each tree explaining the given data based on a model of evolution. In this case, the tree with the highest probability of explaining the data is chosen over the other ones. In other words, it compares how different trees predict the observed data. The introduction of a model of evolution in ML analyses presents an advantage over MP as the probability of nucleotide substitutions and rates of these substitutions are taken into account, explaining the phylogenetic relationships of taxa in a more realistic way. An important consideration of this method is the branch length, which parsimony ignores, with changes being more likely to happen along long branches than short ones. This approach might eliminate long branch attraction and explain the greater consistency of ML over MP. Although considered by many to be the best approach to inferring phylogenies from a theoretical point of view, ML is computationally intensive and it is almost impossible to explore all trees as there are too many. Bayesian inference also incorporates a model of evolution and the main advantages over MP and ML are that it is computationally more efficient than traditional methods, it quantifies and addresses the source of uncertainty and is able to incorporate complex models of evolution.

## Pitfalls and controversies

- Bootstrap values vs posterior probabilities. It has been observed that bootstrap support values, calculated under parsimony or maximum likelihood, tend to be lower than the posterior probabilities obtained by Bayesian inference. This leads to a number of questions such as: Do posterior probabilities lead to overconfidence in the results? Are bootstrap values more robust than posterior probabilities? One fact underlying this controversy is that all data are used during Bayesian analysis and the calculation of posterior probabilities, while the nature of bootstrapping means that most bootstrap replicates will be missing some of the original data. As a result, bipartitions (branches) supported by relatively few characters in the dataset may receive very high posterior probabilities but moderate or even low bootstrap support, as many of the bootstrap replicates don't contain enough of the critical characters to retrieve the bipartition.
- Controversy of using prior probabilities. Using prior probabilities for Bayesian analysis has been seen by many as an advantage as it provides a way of incorporating information from sources other than the data being analyzed. However, when such external information is lacking, one is forced to use a prior even if it is impossible to use a statistical distribution to represent total ignorance. It is also a concern that the Bayesian posterior probabilities may reflect subjective opinions when the prior is arbitrary and subjective.
- Model choice. The results of the Bayesian analysis of a phylogeny are directly correlated to the model of evolution chosen so it is important to choose a model that fits the observed data, otherwise inferences in the phylogeny will be erroneous. Many scientists have raised questions about the interpretation of Bayesian inference when the model is unknown or incorrect. For example, an oversimplified model might give higher posterior probabilities.

## MrBayes software

MrBayes is a free software tool that performs Bayesian inference of phylogeny. It was originally written by John P. Huelsenbeck and Frederik Ronquist in 2001. As Bayesian methods increased in popularity, MrBayes became one of the software of choice for many molecular phylogeneticists. It is offered for Macintosh, Windows, and UNIX operating systems and it has a command-line interface. The program uses the standard MCMC algorithm as well as the Metropolis coupled MCMC variant. MrBayes reads aligned matrices of sequences (DNA or amino acids) in the standard NEXUS format.

MrBayes uses MCMC to approximate the posterior probabilities of trees. The user can change assumptions of the substitution model, priors and the details of the MC³ analysis. It also allows the user to remove and add taxa and characters to the analysis. The program includes, among several nucleotide models, the most standard model of DNA substitution, the 4x4 also called JC69, which assumes that changes across nucleotides occur with equal probability. It also implements a number of 20x20 models of amino acid substitution, and codon models of DNA substitution. It offers different methods for relaxing the assumption of equal substitutions rates across nucleotide sites. MrBayes is also able to infer ancestral states accommodating uncertainty to the phylogenetic tree and model parameters.

MrBayes 3 was a completely reorganized and restructured version of the original MrBayes. The main novelty was the ability of the software to accommodate heterogeneity of data sets. This new framework allows the user to mix models and take advantages of the efficiency of Bayesian MCMC analysis when dealing with different type of data (e.g. protein, nucleotide, and morphological). It uses the Metropolis-Coupling MCMC by default.

MrBayes 3.2 was released in 2012. This version allows the users to run multiple analyses in parallel. It also provides faster likelihood calculations and allow these calculations to be delegated to graphics processing unites (GPUs). Version 3.2 provides wider outputs options compatible with FigTree and other tree viewers.

## List of phylogenetics software

This table includes some of the most common phylogenetic software used for inferring phylogenies under a Bayesian framework. Some of them do not use exclusively Bayesian methods.

| Name | Description | Method | Author | Website link |
|---|---|---|---|---|
| MrBayes | Phylogenetic inference | A program for Bayesian inference and model choice across a wide range of phylogenetic and evolutionary models. | Zangh, Huelsenbeck, Der Mark, Ronquist & Teslenko | https://nbisweden.github.io/MrBayes/ |
| BEAST | Bayesian Evolutionary Analysis Sampling Trees | Bayesian inference, relaxed molecular clock, demographic history | A. J. Drummond, A. Rambaut & M. A. Suchard | https://beast.community |
| BEAST 2 | A software platform for Bayesian evolutionary analysis | Bayesian inference, packages, multiple models | R Bouckaert, J Heled, D Kühnert, T Vaughan, CH Wu, D Xie, MA Suchard, A Rambaut, AJ Drummond. | http://www.beast2.org |
| PhyloBayes / PhyloBayes MPI | Bayesian Monte Carlo Markov Chain (MCMC) sampler for phylogenetic reconstruction. | Non-parametric methods for modeling among-site variation in nucleotide or amino-acid propensities. | N. Lartillot, N. Rodrigue, D. Stubbs, J. Richer | http://www.atgc-montpellier.fr/phylobayes/ |
| Bali-Phy | Simultaneous Bayesian inference of alignment and phylogeny | Bayesian inference, alignment as well as tree search | Suchard MA, Redelings BD | http://www.bali-phy.org |
| BUCKy | Bayesian concordance of gene trees | Bayesian concordance using modified greedy consensus of unrooted quartets | C. Ané, B. Larget, D.A. Baum, S.D. Smith, A. Rokas and B. Larget, S.K. Kotha, C.N. Dewey, C. Ané | http://www.stat.wisc.edu/~ane/bucky/ |
| BATWING | Bayesian Analysis of Trees With Internal Node Generation | Bayesian inference, demographic history, population splits | I. J. Wilson, D. Weale, D.Balding | http://www.maths.abdn.ac.uk/˜ijw |
| Bayes Phylogenies | Bayesian inference of trees using Markov Chain Monte Carlo methods | Bayesian inference, multiple models, mixture model (auto-partitioning) | M. Pagel, A. Meade | http://www.evolution.rdg.ac.uk/BayesPhy.html Archived 2020-02-19 at the Wayback Machine |
| Armadillo Workflow Platform | Workflow platform dedicated to phylogenetic and general bioinformatic analysis | GUI wrapper around MrBayes | E. Lord, M. Leclercq, A. Boc, A.B. Diallo and V. Makarenkov | https://github.com/armadilloUQAM/armadillo2/ |
| Geneious (MrBayes plugin) | Geneious provides genome and proteome research tools | GUI wrapper around MrBayes | A. J. Drummond,M.Suchard,V.Lefort et al. | http://www.geneious.com |
| TOPALi | Phylogenetic inference | GUI wrapper around MrBayes | I.Milne, D.Lindner, et al. | http://www.topali.org |

## Applications

Bayesian Inference has extensively been used by molecular phylogeneticists for a wide number of applications. Some of these include:

- Inference of phylogenies.
- Inference and evaluation of uncertainty of phylogenies.
- Inference of ancestral character state evolution.
- Inference of ancestral areas.
- Molecular dating analysis.
- Model dynamics of species diversification and extinction
- Elucidate patterns in pathogens dispersal.
- Inference of phenotypic trait evolution.
