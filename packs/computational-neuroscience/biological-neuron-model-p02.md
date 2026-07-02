---
title: "Biological neuron model (part 2/2)"
source: https://en.wikipedia.org/wiki/Biological_neuron_model
domain: computational-neuroscience
license: CC-BY-SA-4.0
tags: computational neuroscience, hodgkin-huxley model, biological neuron model, cable theory
fetched: 2026-07-02
part: 2/2
---

## Applications

Spiking Neuron Models are used in a variety of applications that need encoding into or decoding from neuronal spike trains in the context of neuroprosthesis and brain-computer interfaces such as retinal prosthesis: or artificial limb control and sensation. Applications are not part of this article; for more information on this topic please refer to the main article.


## Relation between artificial and biological neuron models

The most basic model of a neuron consists of an input with some synaptic weight vector and an activation function or transfer function inside the neuron determining output. This is the basic structure used for artificial neurons, which in a neural network often looks like

$y_{i}=\varphi \left(\sum _{j}w_{ij}x_{j}\right)$

where *y**i* is the output of the *i* th neuron, *x**j* is the *j*th input neuron signal, *w**ij* is the synaptic weight (or strength of connection) between the neurons *i* and *j*, and *φ* is the activation function. While this model has seen success in machine-learning applications, it is a poor model for real (biological) neurons, because it lacks time-dependence in input and output.

When an input is switched on at a time t and kept constant thereafter, biological neurons emit a spike train. Importantly, this spike train is not regular but exhibits a temporal structure characterized by adaptation, bursting, or initial bursting followed by regular spiking. Generalized integrate-and-fire models such as the Adaptive Exponential Integrate-and-Fire model, the spike response model, or the (linear) adaptive integrate-and-fire model can capture these neuronal firing patterns.

Moreover, neuronal input in the brain is time-dependent. Time-dependent input is transformed by complex linear and nonlinear filters into a spike train in the output. Again, the spike response model or the adaptive integrate-and-fire model enables to prediction of the spike train in the output for arbitrary time-dependent input, whereas an artificial neuron or a simple leaky integrate-and-fire does not.

If we take the Hodkgin-Huxley model as a starting point, generalized integrate-and-fire models can be derived systematically in a step-by-step simplification procedure. This has been shown explicitly for the exponential integrate-and-fire model and the spike response model.

In the case of modeling a biological neuron, physical analogs are used in place of abstractions such as "weight" and "transfer function". A neuron is filled and surrounded with water-containing ions, which carry electric charge. The neuron is bound by an insulating cell membrane and can maintain a concentration of charged ions on either side that determines a capacitance *C*m. The firing of a neuron involves the movement of ions into the cell, that occurs when neurotransmitters cause ion channels on the cell membrane to open. We describe this by a physical time-dependent current *I*(*t*). With this comes a change in voltage, or the electrical potential energy difference between the cell and its surroundings, which is observed to sometimes result in a voltage spike called an action potential which travels the length of the cell and triggers the release of further neurotransmitters. The voltage, then, is the quantity of interest and is given by *V*m(*t*).

If the input current is constant, most neurons emit after some time of adaptation or initial bursting a regular spike train. The frequency of regular firing in response to a constant current *I* is described by the frequency-current relation, which corresponds to the transfer function $\varphi$ of artificial neural networks. Similarly, for all spiking neuron models, the transfer function $\varphi$ can be calculated numerically (or analytically).


## Cable theory and compartmental models

All of the above deterministic models are point-neuron models because they do not consider the spatial structure of a neuron. However, the dendrite contributes to transforming input into output. Point neuron models are valid description in three cases. (i) If input current is directly injected into the soma. (ii) If synaptic input arrives predominantly at or close to the soma (closeness is defined by a length scale $\lambda$ introduced below. (iii) If synapse arrives anywhere on the dendrite, but the dendrite is completely linear. In the last case, the cable acts as a linear filter; these linear filter properties can be included in the formulation of generalized integrate-and-fire models such as the spike response model.

The filter properties can be calculated from a cable equation.

Let us consider a cell membrane in the form of a cylindrical cable. The position on the cable is denoted by x and the voltage across the cell membrane by V. The cable is characterized by a longitudinal resistance $r_{l}$ per unit length and a membrane resistance $r_{m}$ . If everything is linear, the voltage changes as a function of time

| ${\frac {r_{m}}{r_{l}}}{\frac {\partial ^{2}V}{\partial x^{2}}}=c_{m}r_{m}{\frac {\partial V}{\partial t}}+V$ |   | 19 |
|---|---|---|

We introduce a length scale $\lambda ^{2}={r_{m}}/{r_{l}}$ on the left side and time constant $\tau =c_{m}r_{m}$ on the right side. The cable equation can now be written in its perhaps best-known form:

| $\lambda ^{2}{\frac {\partial ^{2}V}{\partial x^{2}}}=\tau {\frac {\partial V}{\partial t}}+V$ |   | 20 |
|---|---|---|

The above cable equation is valid for a single cylindrical cable.

Linear cable theory describes the dendritic arbor of a neuron as a cylindrical structure undergoing a regular pattern of bifurcation, like branches in a tree. For a single cylinder or an entire tree, the static input conductance at the base (where the tree meets the cell body or any such boundary) is defined as

$G_{in}={\frac {G_{\infty }\tanh(L)+G_{L}}{1+(G_{L}/G_{\infty })\tanh(L)}}$

,

where *L* is the electrotonic length of the cylinder, which depends on its length, diameter, and resistance. A simple recursive algorithm scales linearly with the number of branches and can be used to calculate the effective conductance of the tree. This is given by

$\,\!G_{D}=G_{m}A_{D}\tanh(L_{D})/L_{D}$

where *A**D* = *πld* is the total surface area of the tree of total length *l*, and *L**D* is its total electrotonic length. For an entire neuron in which the cell body conductance is *G**S* and the membrane conductance per unit area is *G**md* = *G**m* / *A*, we find the total neuron conductance *G**N* for *n* dendrite trees by adding up all tree and soma conductances, given by

$G_{N}=G_{S}+\sum _{j=1}^{n}A_{D_{j}}F_{dga_{j}},$

where we can find the general correction factor *F**dga* experimentally by noting *G**D* = *G**md**A**D**F**dga*.

The linear cable model makes several simplifications to give closed analytic results, namely that the dendritic arbor must branch in diminishing pairs in a fixed pattern and that dendrites are linear. A compartmental model allows for any desired tree topology with arbitrary branches and lengths, as well as arbitrary nonlinearities. It is essentially a discretized computational implementation of nonlinear dendrites.

Each piece, or compartment, of a dendrite, is modeled by a straight cylinder of arbitrary length *l* and diameter *d* which connects with fixed resistance to any number of branching cylinders. We define the conductance ratio of the *i*th cylinder as *B**i* = *G**i* / *G*∞, where $G_{\infty }={\tfrac {\pi d^{3/2}}{2{\sqrt {R_{i}R_{m}}}}}$ and *R**i* is the resistance between the current compartment and the next. We obtain a series of equations for conductance ratios in and out of a compartment by making corrections to the normal dynamic *B*out,*i* = *B*in,*i+1*, as

- $B_{\mathrm {out} ,i}={\frac {B_{\mathrm {in} ,i+1}(d_{i+1}/d_{i})^{3/2}}{\sqrt {R_{\mathrm {m} ,i+1}/R_{\mathrm {m} ,i}}}}$
- $B_{\mathrm {in} ,i}={\frac {B_{\mathrm {out} ,i}+\tanh X_{i}}{1+B_{\mathrm {out} ,i}\tanh X_{i}}}$
- $B_{\mathrm {out,par} }={\frac {B_{\mathrm {in,dau1} }(d_{\mathrm {dau1} }/d_{\mathrm {par} })^{3/2}}{\sqrt {R_{\mathrm {m,dau1} }/R_{\mathrm {m,par} }}}}+{\frac {B_{\mathrm {in,dau2} }(d_{\mathrm {dau2} }/d_{\mathrm {par} })^{3/2}}{\sqrt {R_{\mathrm {m,dau2} }/R_{\mathrm {m,par} }}}}+\ldots$

where the last equation deals with *parents* and *daughters* at branches, and $X_{i}={\tfrac {l_{i}{\sqrt {4R_{i}}}}{\sqrt {d_{i}R_{m}}}}$ . We can iterate these equations through the tree until we get the point where the dendrites connect to the cell body (soma), where the conductance ratio is *B*in,stem. Then our total neuron conductance for static input is given by

$G_{N}={\frac {A_{\mathrm {soma} }}{R_{\mathrm {m,soma} }}}+\sum _{j}B_{\mathrm {in,stem} ,j}G_{\infty ,j}.$

Importantly, static input is a very special case. In biology, inputs are time-dependent. Moreover, dendrites are not always linear.

Compartmental models enable to include nonlinearities via ion channels positioned at arbitrary locations along the dendrites. For static inputs, it is sometimes possible to reduce the number of compartments (increase the computational speed) and yet retain the salient electrical characteristics.


## Conjectures regarding the role of the neuron in the wider context of the brain principle of operation

### The neurotransmitter-based energy detection scheme

The neurotransmitter-based energy detection scheme suggests that the neural tissue chemically executes a Radar-like detection procedure.

As shown in Fig. 6, the key idea of the conjecture is to account for neurotransmitter concentration, neurotransmitter generation, and neurotransmitter removal rates as the important quantities in executing the detection task, while referring to the measured electrical potentials as a side effect that only in certain conditions coincide with the functional purpose of each step. The detection scheme is similar to a radar-like "energy detection" because it includes signal squaring, temporal summation, and a threshold switch mechanism, just like the energy detector, but it also includes a unit that emphasizes stimulus edges and a variable memory length (variable memory). According to this conjecture, the physiological equivalent of the energy test statistics is neurotransmitter concentration, and the firing rate corresponds to neurotransmitter current. The advantage of this interpretation is that it leads to a unit-consistent explanation which allows for bridge between electrophysiological measurements, biochemical measurements, and psychophysical results.

The evidence reviewed in suggests the following association between functionality to histological classification:

1. Stimulus squaring is likely to be performed by receptor cells.
2. Stimulus edge emphasizing and signal transduction is performed by neurons.
3. Temporal accumulation of neurotransmitters is performed by glial cells. Short-term neurotransmitter accumulation is likely to occur also in some types of neurons.
4. Logical switching is executed by glial cells, and it results from exceeding a threshold level of neurotransmitter concentration. This threshold crossing is also accompanied by a change in neurotransmitter leak rate.
5. Physical all-or-non movement switching is due to muscle cells and results from exceeding a certain neurotransmitter concentration threshold on muscle surroundings.

Note that although the electrophysiological signals in Fig.6 are often similar to the functional signal (signal power/neurotransmitter concentration / muscle force), there are some stages in which the electrical observation differs from the functional purpose of the corresponding step. In particular, Nossenson et al. suggested that glia threshold crossing has a completely different functional operation compared to the radiated electrophysiological signal and that the latter might only be a side effect of glia break.

- The models above are still idealizations. Corrections must be made for the increased membrane surface area given by numerous dendritic spines, temperatures significantly hotter than room-temperature experimental data, and nonuniformity in the cell's internal structure. Certain observed effects do not fit into some of these models. For instance, the temperature cycling (with minimal net temperature increase) of the cell membrane during action potential propagation is not compatible with models that rely on modeling the membrane as a resistance that must dissipate energy when current flows through it. The transient thickening of the cell membrane during action potential propagation is also not predicted by these models, nor is the changing capacitance and voltage spike that results from this thickening incorporated into these models. The action of some anesthetics such as inert gases is problematic for these models as well. New models, such as the soliton model attempt to explain these phenomena, but are less developed than older models and have yet to be widely applied.
- Modern views regarding the role of the scientific model suggest that "All models are wrong but some are useful" (Box and Draper, 1987, Gribbin, 2009; Paninski et al., 2009).
- Recent conjecture suggests that each neuron might function as a collection of independent threshold units. It is suggested that a neuron could be anisotropically activated following the origin of its arriving signals to the membrane, via its dendritic trees. The spike waveform was also proposed to be dependent on the origin of the stimulus.
