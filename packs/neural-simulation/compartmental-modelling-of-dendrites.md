---
title: "Compartmental neuron models"
source: https://en.wikipedia.org/wiki/Compartmental_modelling_of_dendrites
domain: neural-simulation
license: CC-BY-SA-4.0
tags: neural simulation software, leaky integrate-and-fire, dendrite compartmental modelling, blue brain project
fetched: 2026-07-02
---

# Compartmental neuron models

(Redirected from

Compartmental modelling of dendrites

)

**Compartmental modelling of dendrites** deals with multi-compartment modelling of the dendrites, to make the understanding of the electrical behavior of complex dendrites easier. Basically, compartmental modelling of dendrites is a very helpful tool to develop new biological neuron models. Dendrites are very important because they occupy the most membrane area in many of the neurons and give the neuron an ability to connect to thousands of other cells. Originally the dendrites were thought to have constant conductance and current but now it has been understood that they may have active Voltage-gated ion channels, which influences the firing properties of the neuron and also the response of neuron to synaptic inputs. Many mathematical models have been developed to understand the electric behavior of the dendrites. Dendrites tend to be very branchy and complex, so the compartmental approach to understand the electrical behavior of the dendrites makes it very useful.

## Introduction

Compartmental modelling is a very natural way of modelling dynamical systems that have certain inherent properties with conservation principles. The compartmental modelling is an elegant way, a state space formulation to elegantly capture the dynamical systems that are governed by the conservation laws. Whether it is the conservation of mass, energy, fluid flow or information flow. Basically, they are models whose state variables tend to be non-negative (such as mass, concentrations, energy). So the equations for mass balance, energy, concentration or fluid flow can be written. It ultimately goes down to networks in which the brain is the largest of them all, just like Avogadro number, very large amount of molecules that are interconnected. The brain has very interesting interconnections. On a microscopic level thermodynamics is virtually impossible to understand but from a macroscopic view we see that these follow some universal laws. In the same way brain has numerous interconnections, which is almost impossible to write a differential equation for.

General observations about how the brain functions can be made by looking at the first and second thermodynamic laws, which are universal laws. Brain is a very large-scale interconnected system; the neurons have to somehow behave like the chemical reaction system, so, it has to somehow obey the chemical thermodynamic laws. This approach may lead to more generalized model of brain.

## Multiple compartments

- Complicated dendritic structures can be treated as multiple compartments interconnected. The dendrites are divided into small compartments and they are linked together as shown in the figure.
- It is assumed that the compartment is isopotential and spatially uniform in its properties. Membrane non-uniformity such as diameter changes, and voltage differences are occurred in between the compartments but not inside them.
- An example of a simple two-compartment model:

Consider a two-compartmental model with the compartments viewed as isopotential cylinders with radius

$a_{i}$

and length

$L_{i}$

.

$V_{i}$

is the

membrane potential

of ith compartment.

$c_{i}$

is the specific membrane capacitance.

$r_{Mi}$

is the specific membrane resistivity.

The total electrode current, assuming that the compartment has it, is given by

$I_{\text{electrode}}^{i}$

.

The longitudinal resistance is given by

$r_{L}$

.

Now according to the balance that should exist for each compartment, we can say

$i_{\text{cap}}^{i}+i_{\text{ion}}^{i}=i_{\text{long}}^{i}+i_{\text{electrode}}^{i}$

.....eq(1)

where

$i_{\text{cap}}^{i}$

and

$i_{\text{ion}}^{i}$

are the capacitive and ionic currents per unit area of ith compartment membrane. i.e. they can be given by

$i_{\text{cap}}^{i}=c_{i}{\frac {dV_{i}}{dt}}$

and

$i_{\text{ion}}^{i}={\frac {V_{i}}{r_{Mi}}}$

.....eq(2)

If we assume the

resting potential

is 0. Then to compute

$i_{\text{long}}^{i}$

, we need total axial resistance. As the compartments are simply cylinders we can say

$R_{\text{long}}={\frac {r_{L}L_{1}}{2\pi a_{1}^{2}}}+{\frac {r_{L}L_{2}}{2\pi a_{2}^{2}}}$

.....eq(3)

Using ohms law we can express current from ith to jth compartment as

$i_{\text{long}}^{1}=g_{1,2}(V_{2}-V_{1})$

and

$i_{\text{long}}^{2}=g_{2,1}(V_{1}-V_{2})$

.....eq(4)

The coupling terms

$g_{1,2}$

and

$g_{2,1}$

are obtained by inverting eq(3) and dividing by surface area of interest.

So we get

$g_{1,2}={\frac {a_{1}a_{2}^{2}}{r_{L}L_{1}(a_{2}^{2}L_{1}+a_{1}^{2}L_{2})}}$

and

$g_{2,1}={\frac {a_{2}a_{1}^{2}}{r_{L}L_{1}(a_{1}^{2}L_{2}+a_{2}^{2}L_{1})}}$

Finally,

$i_{\text{electrode}}^{I}={\frac {I_{\text{electrode}}^{i}}{A_{i}}}$

$A_{i}=2\pi a_{i}L_{i}$

is the surface area of the compartment i.

If we put all these together we get

$c_{1}{\frac {dV_{1}}{dt}}+{\frac {V_{1}}{r_{M1}}}=g_{1,2}(V_{2}-V_{1})+{\frac {I_{\text{electrode}}^{1}}{A_{1}}}$

$c_{2}{\frac {dV_{2}}{dt}}+{\frac {V_{2}}{r_{M2}}}=g_{2,1}(V_{1}-V_{2})+{\frac {I_{\text{electrode}}^{2}}{A_{2}}}$

.....eq(5)

If we use

$r_{1}=1/g_{1,2}$

and

$r_{2}=1/g_{2,1}$

then eq(5) will become

$c_{1}{\frac {dV_{1}}{dt}}+{\frac {V_{1}}{r_{M1}}}={\frac {V_{2}-V_{1}}{r_{1}}}+{\frac {I_{\text{electrode}}^{1}}{A_{1}}}$

$c_{2}{\frac {dV_{2}}{dt}}+{\frac {V_{2}}{r_{M2}}}={\frac {V_{1}-V_{2}}{r_{2}}}+{\frac {I_{\text{electrode}}^{2}}{A_{2}}}$

.....eq(6)

Now if we inject current in cell 1 only and each cylinder is identical then

$r_{1}=r_{2}\equiv r$

Without loss in generality we can define

$r_{M}=r_{M1}=r_{M2}$

After some algebra we can show that

${\frac {V_{1}}{i_{1}}}={\frac {r_{M}(r+r_{M})}{r+2r_{M}}}$

also

${\frac {R_{\text{input,coupled}}}{R_{\text{input,uncoupled}}}}=1-{\frac {r_{M}}{r+2r_{M}}}$

i.e. the input resistance decreases. For increment in the potential, coupled system current should be greater than that is required for uncoupled system. This is because the second compartment drains some current.

Now, we can get a general compartmental model for a treelike structure and the equations are

$C_{j}{\frac {dV_{j}}{dt}}=-{\frac {V_{j}}{R_{j}}}+\sum _{k{\text{ connected }}j}{}{\frac {V_{k}-V_{j}}{R_{jk}}}+I_{j}$

### Increased computational accuracy in multi-compartmental cable models

- Input at the center

Each dendritic section is subdivided into segments, which are typically seen as uniform circular cylinders or tapered circular cylinders. In the traditional compartmental model, point process location is determined only to an accuracy of half segment length. This will make the model solution particularly sensitive to segment boundaries. The accuracy of the traditional approach for this reason is O(1/n) when a point current and synaptic input is present. Usually the trans-membrane current where the membrane potential is known is represented in the model at points, or nodes and is assumed to be at the center. The new approach partitions the effect of the input by distributing it to the boundaries of the segment. Hence any input is partitioned between the nodes at the proximal and distal boundaries of the segment. Therefore, this procedure makes sure that the solution obtained is not sensitive to small changes in location of these boundaries because it affects how the input is partitioned between the nodes. When these compartments are connected with continuous potentials and conservation of current at segment boundaries then a new compartmental model of a new mathematical form is obtained. This new approach also provides a model identical to the traditional model but an order more accurate. This model increases the accuracy and precision by an order of magnitude than that is achieved by point process input.

## Cable theory

Dendrites and axons are considered to be continuous (cable-like), rather than series of compartments.

## Some applications

### Information processing

- A theoretical framework along with a technological platform are provided by computational models to enhance the understanding of nervous system functions. There was a lot of advancement in the molecular and biophysical mechanisms underlying the neuronal activity. The same kind of advances have to be made in understanding the structure-functional relationship and rules followed by the information processing.
- Previously a neuron used to be thought as a transistor. However, it is shown recently that morphology and ionic composition of different neurons provide the cell with enhanced computational capabilities. These abilities are far more advanced than those captured by a point neuron.
- Some findings:
  - Different outputs given by the individual apical oblique dendrites of CA1 pyramidal neurons are linearly combined in the cell body. The outputs that come from these dendrites actually behave like individual computational units that use sigmoidal activation function to combine inputs.
  - The thin dendritic branches each act as a typical point neuron, which are capable of combining the incoming signals according to the thresholding non-linearity.
  - Considering the accuracy in prediction of different input patterns by a two-layer neural network, it is assumed that a simple mathematical equation can be used to describe the model. This allows the development of network models in which each neuron, instead of being modelled as a full blown compartmental cell, it is modelled as a simplified two layer neural network.
  - The firing pattern of the cell might contain the temporal information about incoming signals. For example, the delay between the two simulated pathways.
  - Single CA1 has a capability of encoding and transmitting spatio-temporal information on the incoming signals to the recipient cell.
  - Calcium-activated nonspecific cationic (CAN) mechanism is needed for giving constant activity and the synaptic stimulation alone does not induce persistent activity using the increasing conductance of NMDA mechanism. NMDA/ AMPA positively expands the range of persistent activity and negatively regulates the amount of CAN needed for constant activity.

### Midbrain dopaminergic neuron

- Movement, motivation, attention, neurological and psychiatric disorders and addictive behavior have a strong influence by Dopaminergic signalling.
- The dopaminergic neurons have a low irregular basal firing frequency in 1–8 Hz range *in vivo* in the ventral tegmental area (VTA) and substantia nigra pars compacta (SNc). This frequencies can dramatically increase in response to a cue predicting reward or unpredicted reward. The actions that preceded the reward are reinforced by this burst or phasic signal.
- The low safety factor for action potential generation gives a result of low maximal steady frequencies. The transient initial frequency in response to depolarizing pulse is controlled by rate of Ca2+ accumulation in distal dendrites.
- Results obtained from a mulch-compartmental model realistic with reconstructed morphology were similar. So, the salient contributions of the dendritic architecture have been captures by simpler model.

### Mode locking

- There are many important applications in neuroscience for Mode-locking response of excitable systems to periodic forcing. For example, The theta rhythm drives the spatially extended place cells in the hippocampus to generate a code giving information about spatial location. The role of neuronal dendrites in generating the response to periodic current injection can be explored by using a compartmental model (with linear dynamics for each compartment) coupled to an active soma model that generates action potentials.
- Some findings:
  - The response of whole neuron model i.e. soma and dendrites, can be written in closed form. The response of the spatially extended model to periodic forcing is described by stroboscopic map. A Arnol'd tongue quasi-active model can be constructed with a linear stability analysis of the map with carefully treating the non-differentiability of soma model.
  - The shape of the tongues is influenced by the presence of the quasi-active membrane.
  - The windows in parameter space for chaotic behavior can be enlarged with the resonant dendritic membrane.
  - The response of the spatially extended neuron model to global forcing is different from that of point forcing.

### Compartmental neural simulations with spatial adaptivity

- The computational cost of the method scales not with the physical size of the system being simulated but with the amount of activity present in the simulation. Spatial adaptivity for certain problems reduces up to 80%.

### Action potential (AP) initiation site

- Establishing a unique site for AP initiation at the axon initial segment is no longer accepted. The APs can be initiated and conducted by different sub-regions of the neuron morphology, which widened the capabilities of individual neurons in computation.
- Findings from a study of the Action Potential Initiation Site Along the Axosomatodendritic Axis of Neurons Using Compartmental Models:
  - Dendritic APs are initiated more effectively by synchronous spatially clustered inputs than equivalent disperse inputs.
  - The initiation site can also be determined by the average electrical distance from the dendritic input to the axon trigger zone, but it may be strongly modulated by the relative excitability of the two trigger zones and a number of factors.

### A finite-state automaton model

- Multi-neuron simulations with finite-state automaton model is capable of modelling the most important characteristics of neural membranes.

### Constraining compartmental models

- Can be done using extracellular action potential recordings
- Can be done using Multiple Voltage Recordings and Genetic Algorithms

### Multi-compartmental model of a CA1 pyramidal cell

- To study changes in hippocampal excitability that result from aging-induced alterations in calcium-dependent membrane mechanisms, the multi-compartmental model of CA1 pyramidal cell can be used. We can model the aging-induced alterations in CA1 excitability can be with simple coupling mechanisms that selectively link specific types of calcium channels to specific calcium-dependent potassium channels.

### Electrical compartmentalization

- Spine Neck Plasticity Controls Postsynaptic Calcium Signals through Electrical Compartmentalization. The spine neck plasticity through a process of electrical compartmentalization can dynamically regulate Calcium influx into spines (a key trigger for synaptic plasticity).

### Robust coding in motion-sensitive neurons

- Different receptive fields in axons and dendrites underlie robust coding in motion-sensitive neurons.

### Conductance-based neuron models

- The capabilities and limitations of conductance-based compartmental neuron models with reduced branched or unbranched morphologies and active dendrites.
