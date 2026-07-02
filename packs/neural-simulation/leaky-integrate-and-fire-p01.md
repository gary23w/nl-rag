---
title: "Biological neuron model (part 1/2)"
source: https://en.wikipedia.org/wiki/Leaky_integrate-and-fire
domain: neural-simulation
license: CC-BY-SA-4.0
tags: neural simulation software, leaky integrate-and-fire, dendrite compartmental modelling, blue brain project
fetched: 2026-07-02
part: 1/2
---

# Biological neuron model

(Redirected from

Leaky integrate-and-fire

)

**Biological neuron models**, also known as **spiking** **neuron models**, are mathematical descriptions of the conduction of electrical signals in neurons. Neurons (or nerve cells) are electrically excitable cells within the nervous system, able to fire electric signals, called action potentials, across a neural network. These mathematical models describe the role of the biophysical and geometrical characteristics of neurons on the conduction of electrical activity.

Central to these models is the description of how the membrane potential (that is, the difference in electric potential between the interior and the exterior of a biological cell) across the cell membrane changes over time. In an experimental setting, stimulating neurons with an electrical current generates an action potential (or spike), that propagates down the neuron's axon. This axon can branch out and connect to a large number of downstream neurons at sites called synapses. At these synapses, the spike can cause the release of neurotransmitters, which in turn can change the voltage potential of downstream neurons. This change can potentially lead to even more spikes in those downstream neurons, thus passing down the signal. As many as 95% of neurons in the neocortex, the outermost layer of the mammalian brain, consist of excitatory pyramidal neurons, and each pyramidal neuron receives tens of thousands of inputs from other neurons. Thus, spiking neurons are a major information processing unit of the nervous system.

One such example of a spiking neuron model may be a highly detailed mathematical model that includes spatial morphology. Another may be a conductance-based neuron model that views neurons as points and describes the membrane voltage dynamics as a function of trans-membrane currents. A mathematically simpler "integrate-and-fire" model significantly simplifies the description of ion channel and membrane potential dynamics (initially studied by Lapique in 1907).


## Biological background, classification, and aims of neuron models

**Non-spiking cells, spiking cells, and their measurement**

Not all the cells of the nervous system produce the type of spike that defines the scope of the spiking neuron models. For example, cochlear hair cells, retinal receptor cells, and retinal bipolar cells do not spike. Furthermore, many cells in the nervous system are not classified as neurons but instead are classified as glia.

Neuronal activity can be measured with different experimental techniques, such as the "Whole cell" measurement technique, which captures the spiking activity of a single neuron and produces full amplitude action potentials.

With extracellular measurement techniques, one or more electrodes are placed in the extracellular space. Spikes, often from several spiking sources, depending on the size of the electrode and its proximity to the sources, can be identified with signal processing techniques. Extracellular measurement has several advantages:

- It is easier to obtain experimentally;
- It is robust and lasts for a longer time;
- It can reflect the dominant effect, especially when conducted in an anatomical region with many similar cells.

**Overview of neuron models**

Neuron models can be divided into two categories according to the physical units of the interface of the model. Each category could be further divided according to the abstraction/detail level:

1. Electrical input–output membrane voltage models – These models produce a prediction for membrane output voltage as a function of electrical stimulation given as current or voltage input. The various models in this category differ in the exact functional relationship between the input current and the output voltage and in the level of detail. Some models in this category predict only the moment of occurrence of the output spike (also known as "action potential"); other models are more detailed and account for sub-cellular processes. The models in this category can be either deterministic or probabilistic.
2. Natural stimulus or pharmacological input neuron models – The models in this category connect the input stimulus, which can be either pharmacological or natural, to the probability of a spike event. The input stage of these models is not electrical but rather has either pharmacological (chemical) concentration units, or physical units that characterize an external stimulus such as light, sound, or other forms of physical pressure. Furthermore, the output stage represents the probability of a spike event and not an electrical voltage.

Although it is not unusual in science and engineering to have several descriptive models for different abstraction/detail levels, the number of different, sometimes contradicting, biological neuron models is exceptionally high. This situation is partly the result of the many different experimental settings, and the difficulty to separate the intrinsic properties of a single neuron from measurement effects and interactions of many cells (network effects).

**Aims of neuron models**

Ultimately, biological neuron models aim to explain the mechanisms underlying the operation of the nervous system. However, several approaches can be distinguished, from more realistic models (e.g., mechanistic models) to more pragmatic models (e.g., phenomenological models). Modeling helps to analyze experimental data and address questions. Models are also important in the context of restoring lost brain functionality through neuroprosthetic devices.


## Electrical input–output membrane voltage models

The models in this category describe the relationship between neuronal membrane currents at the input stage and membrane voltage at the output stage. This category includes (generalized) integrate-and-fire models and biophysical models inspired by the work of Hodgkin–Huxley in the early 1950s using an experimental setup that punctured the cell membrane and allowed to force a specific membrane voltage/current.

Most modern electrical neural interfaces apply extra-cellular electrical stimulation to avoid membrane puncturing, which can lead to cell death and tissue damage. Hence, it is not clear to what extent the electrical neuron models hold for extra-cellular stimulation (see e.g.).

### Hodgkin–Huxley

| Property of the H&H model | Ref. |
|---|---|
| The shape of an individual spike |   |
| The identity of the ions involved |   |
| Spike speed across the axon |   |

The Hodgkin–Huxley model (H&H model) is a model of the relationship between the flow of ionic currents across the neuronal cell membrane and the membrane voltage of the cell. It consists of a set of nonlinear differential equations describing the behavior of ion channels that permeate the cell membrane of the squid giant axon. Hodgkin and Huxley were awarded the 1963 Nobel Prize in Physiology or Medicine for this work.

It is important to note the voltage-current relationship, with multiple voltage-dependent currents charging the cell membrane of capacity *C*m

$C_{\mathrm {m} }{\frac {dV(t)}{dt}}=-\sum _{i}I_{i}(t,V).$

The above equation is the time derivative of the law of capacitance, *Q* = *CV* where the change of the total charge must be explained as the sum over the currents. Each current is given by

$I(t,V)=g(t,V)\cdot (V-V_{\mathrm {eq} })$

where *g*(*t*,*V*) is the conductance, or inverse resistance, which can be expanded in terms of its maximal conductance *ḡ* and the activation and inactivation fractions *m* and *h*, respectively, that determine how many ions can flow through available membrane channels. This expansion is given by

$g(t,V)={\bar {g}}\cdot m(t,V)^{p}\cdot h(t,V)^{q}$

and our fractions follow the first-order kinetics

${\frac {dm(t,V)}{dt}}={\frac {m_{\infty }(V)-m(t,V)}{\tau _{\mathrm {m} }(V)}}=\alpha _{\mathrm {m} }(V)\cdot (1-m)-\beta _{\mathrm {m} }(V)\cdot m$

with similar dynamics for *h*, where we can use either *τ* and *m*∞ or *α* and *β* to define our gate fractions.

The Hodgkin–Huxley model may be extended to include additional ionic currents. Typically, these include inward Ca2+ and Na+ input currents, as well as several varieties of K+ outward currents, including a "leak" current.

The result can be at the small end of 20 parameters which one must estimate or measure for an accurate model. In a model of a complex system of neurons, numerical integration of the equations are computationally expensive. Careful simplifications of the Hodgkin–Huxley model are therefore needed.

The model can be reduced to two dimensions thanks to the dynamic relations which can be established between the gating variables. it is also possible to extend it to take into account the evolution of the concentrations (considered fixed in the original model).

### Perfect Integrate-and-fire

One of the earliest models of a neuron is the perfect integrate-and-fire model (also called non-leaky integrate-and-fire), first investigated in 1907 by Louis Lapicque. A neuron is represented by its membrane voltage *V* which evolves in time during stimulation with an input current *I(t)* according

$I(t)=C{\frac {dV(t)}{dt}}$

which is just the time derivative of the law of capacitance, *Q* = *CV*. When an input current is applied, the membrane voltage increases with time until it reaches a constant threshold *V*th, at which point a delta function spike occurs and the voltage is reset to its resting potential, after which the model continues to run. The *firing frequency* of the model thus increases linearly without bound as input current increases.

The model can be made more accurate by introducing a refractory period *t*ref that limits the firing frequency of a neuron by preventing it from firing during that period. For constant input *I(t)=I* the threshold voltage is reached after an integration time tint=CVthr/I after starting from zero. After a reset, the refractory period introduces a dead time so that the total time until the next firing is *t*ref+*t*int . The firing frequency is the inverse of the total inter-spike interval (including dead time). The firing frequency as a function of a constant input current, is therefore

$\,\!f(I)={\frac {I}{C_{\mathrm {} }V_{\mathrm {th} }+t_{\mathrm {ref} }I}}.$

A shortcoming of this model is that it describes neither adaptation nor leakage. If the model receives a below-threshold short current pulse at some time, it will retain that voltage boost forever - until another input later makes it fire. This characteristic is not in line with observed neuronal behavior. The following extensions make the integrate-and-fire model more plausible from a biological point of view.

### Leaky integrate-and-fire

The leaky integrate-and-fire model, which can be traced back to Louis Lapicque, contains a "leak" term in the membrane potential equation that reflects the diffusion of ions through the membrane, unlike the non-leaky integrate-and-fire model. The model equation looks like

$C_{\mathrm {m} }{\frac {dV_{\mathrm {m} }(t)}{dt}}=I(t)-{\frac {V_{\mathrm {m} }(t)}{R_{\mathrm {m} }}}$

where *V*m is the voltage across the cell membrane and *R*m is the membrane resistance. (The non-leaky integrate-and-fire model is retrieved in the limit *R*m to infinity, i.e. if the membrane is a perfect insulator). The model equation is valid for arbitrary time-dependent input until a threshold *V*th is reached; thereafter the membrane potential is reset.

For constant input, the minimum input to reach the threshold is *I*th = *V*th / *R*m. Assuming a reset to zero, the firing frequency thus looks like

$f(I)={\begin{cases}0,&I\leq I_{\mathrm {th} }\\\left[t_{\mathrm {ref} }-R_{\mathrm {m} }C_{\mathrm {m} }\log \left(1-{\tfrac {V_{\mathrm {th} }}{IR_{\mathrm {m} }}}\right)\right]^{-1},&I>I_{\mathrm {th} }\end{cases}}$

which converges for large input currents to the previous leak-free model with the refractory period. The model can also be used for inhibitory neurons.

The most significant disadvantage of this model is that it does not contain neuronal adaptation, so that it cannot describe an experimentally measured spike train in response to constant input current. This disadvantage is removed in generalized integrate-and-fire models that also contain one or several adaptation-variables and are able to predict spike times of cortical neurons under current injection to a high degree of accuracy.

### Adaptive integrate-and-fire

| Adaptive integrate-and-fire model model | Ref. |
|---|---|
| Sub-threshold voltage for time-dependent input current |   |
| Firing times for time-dependent input current |   |
| Firing Patterns in response to step current input |   |

Neuronal adaptation refers to the fact that even in the presence of a constant current injection into the soma, the intervals between output spikes increase. An adaptive integrate-and-fire neuron model combines the leaky integration of voltage *V* with one or several adaptation variables *w*k (see Chapter 6.1. in the textbook Neuronal Dynamics)

$\tau _{\mathrm {m} }{\frac {dV_{\mathrm {m} }(t)}{dt}}=RI(t)-[V_{\mathrm {m} }(t)-E_{\mathrm {m} }]-R\sum _{k}w_{k}$

$\tau _{k}{\frac {dw_{k}(t)}{dt}}=-a_{k}[V_{\mathrm {m} }(t)-E_{\mathrm {m} }]-w_{k}+b_{k}\tau _{k}\sum _{f}\delta (t-t^{f})$

where $\tau _{m}$ is the membrane time constant, *w*k is the adaptation current number, with index *k*, $\tau _{k}$ is the time constant of adaptation current *w**k*, *E*m is the resting potential and *t*f is the firing time of the neuron and the Greek delta denotes the Dirac delta function. Whenever the voltage reaches the firing threshold the voltage is reset to a value *V*r below the firing threshold. The reset value is one of the important parameters of the model. The simplest model of adaptation has only a single adaptation variable *w* and the sum over k is removed.

Integrate-and-fire neurons with one or several adaptation variables can account for a variety of neuronal firing patterns in response to constant stimulation, including adaptation, bursting, and initial bursting. Moreover, adaptive integrate-and-fire neurons with several adaptation variables are able to predict spike times of cortical neurons under time-dependent current injection into the soma.

### Fractional-order leaky integrate-and-fire

Recent advances in computational and theoretical fractional calculus lead to a new form of model called Fractional-order leaky integrate-and-fire. An advantage of this model is that it can capture adaptation effects with a single variable. The model has the following form

$I(t)-{\frac {V_{\mathrm {m} }(t)}{R_{\mathrm {m} }}}=C_{\mathrm {m} }{\frac {d^{\alpha }V_{\mathrm {m} }(t)}{d^{\alpha }t}}$

Once the voltage hits the threshold it is reset. Fractional integration has been used to account for neuronal adaptation in experimental data.

### 'Exponential integrate-and-fire' and 'adaptive exponential integrate-and-fire'

| Adaptive exponential integrate-and-fire | Ref. |
|---|---|
| The sub-threshold current-voltage relation |   |
| Firing patterns in response to step current input |   |
| Refractoriness and adaptation |   |

In the exponential integrate-and-fire model, spike generation is exponential, following the equation:

${\frac {dV}{dt}}-{\frac {R}{\tau _{m}}}I(t)={\frac {1}{\tau _{m}}}\left[E_{m}-V+\Delta _{T}\exp \left({\frac {V-V_{T}}{\Delta _{T}}}\right)\right].$

where V is the membrane potential, $V_{T}$ is the intrinsic membrane potential threshold, $\tau _{m}$ is the membrane time constant, $E_{m}$ is the resting potential, and $\Delta _{T}$ is the sharpness of action potential initiation, usually around 1 mV for cortical pyramidal neurons. Once the membrane potential crosses $V_{T}$ , it diverges to infinity in finite time. In numerical simulation the integration is stopped if the membrane potential hits an arbitrary threshold (much larger than $V_{T}$ ) at which the membrane potential is reset to a value *V*r . The voltage reset value *V*r is one of the important parameters of the model. Importantly, the right-hand side of the above equation contains a nonlinearity that can be directly extracted from experimental data. In this sense the exponential nonlinearity is strongly supported by experimental evidence.

In the **adaptive exponential integrate-and-fire neuron** the above exponential nonlinearity of the voltage equation is combined with an adaptation variable w

$\tau _{m}{\frac {dV}{dt}}=RI(t)+\left[E_{m}-V+\Delta _{T}\exp \left({\frac {V-V_{T}}{\Delta _{T}}}\right)\right]-Rw$

$\tau {\frac {dw(t)}{dt}}=-a[V_{\mathrm {m} }(t)-E_{\mathrm {m} }]-w+b\tau \delta (t-t^{f})$

where *w* denotes the adaptation current with time scale $\tau$ . Important model parameters are the voltage reset value *V*r, the intrinsic threshold $V_{T}$ , the time constants $\tau$ and $\tau _{m}$ as well as the coupling parameters *a* and *b*. The adaptive exponential integrate-and-fire model inherits the experimentally derived voltage nonlinearity of the exponential integrate-and-fire model. But going beyond this model, it can also account for a variety of neuronal firing patterns in response to constant stimulation, including adaptation, bursting, and initial bursting. However, since the adaptation is in the form of a current, aberrant hyperpolarization may appear. This problem was solved by expressing it as a conductance.

### Adaptive Threshold Neuron Model

In this model, a time-dependent function $\theta (t)$ is added to the fixed threshold, $v_{th0}$ , after every spike, causing an adaptation of the threshold. The threshold potential, $v_{th}$ , gradually returns to its steady state value depending on the threshold adaptation time constant $\tau _{\theta }$ . This is one of the simpler techniques to achieve spike frequency adaptation. The expression for the adaptive threshold is given by:

$v_{th}(t)=v_{th0}+{\frac {\sum \theta (t-t_{f})}{f}}=v_{th0}+{\frac {\sum \theta _{0}\exp \left[-{\frac {(t-t_{f})}{\tau _{\theta }}}\right]}{f}}$

where $\theta (t)$ is defined by: $\theta (t)=\theta _{0}\exp \left[-{\frac {t}{\tau _{\theta }}}\right]$

When the membrane potential, $u(t)$ , reaches a threshold, it is reset to $v_{rest}$ :

$u(t)\geq v_{th}(t)\Rightarrow v(t)=v_{\text{rest}}$

A simpler version of this with a single time constant in threshold decay with an LIF neuron is realized in to achieve LSTM like recurrent spiking neural networks to achieve accuracy nearer to ANNs on few spatio temporal tasks.

### Double Exponential Adaptive Threshold (DEXAT)

The DEXAT neuron model is a flavor of adaptive neuron model in which the threshold voltage decays with a double exponential having two time constants. Double exponential decay is governed by a fast initial decay and then a slower decay over a longer period of time. This neuron used in SNNs through surrogate gradient creates an adaptive learning rate yielding higher accuracy and faster convergence, and flexible long short-term memory compared to existing counterparts in the literature. The membrane potential dynamics are described through equations and the threshold adaptation rule is:

$v_{th}(t)=b_{0}+\beta _{1}b_{1}(t)+\beta _{2}b_{2}(t)$

The dynamics of $b_{1}(t)$ and $b_{2}(t)$ are given by

$b_{1}(t+\delta t)=p_{j1}b_{1}(t)+(1-p_{j1})z(t)\delta (t)$ ,

$b_{2}(t+\delta t)=p_{j2}b_{2}(t)+(1-p_{j2})z(t)\delta (t)$ ,

where $p_{j1}=\exp \left[-{\frac {\delta t}{\tau _{b1}}}\right]$ and $p_{j2}=\exp \left[-{\frac {\delta t}{\tau _{b2}}}\right]$ .

Further, multi-time scale adaptive threshold neuron model showing more complex dynamics is shown in.


## Stochastic models of membrane voltage and spike timing

The models in this category are generalized integrate-and-fire models that include a certain level of stochasticity. Cortical neurons in experiments are found to respond reliably to time-dependent input, albeit with a small degree of variations between one trial and the next if the same stimulus is repeated. Stochasticity in neurons has two important sources. First, even in a very controlled experiment where input current is injected directly into the soma, ion channels open and close stochastically and this channel noise leads to a small amount of variability in the exact value of the membrane potential and the exact timing of output spikes. Second, for a neuron embedded in a cortical network, it is hard to control the exact input because most inputs come from unobserved neurons somewhere else in the brain.

Stochasticity has been introduced into spiking neuron models in two fundamentally different forms: either (i) a **noisy input** **current** is added to the differential equation of the neuron model; or (ii) the process of **spike generation is noisy.** In both cases, the mathematical theory can be developed for continuous time, which is then, if desired for the use in computer simulations, transformed into a discrete-time model.

The relation of noise in neuron models to the variability of spike trains and neural codes is discussed in Neural Coding and in Chapter 7 of the textbook Neuronal Dynamics.

### Noisy input model (diffusive noise)

A neuron embedded in a network receives spike input from other neurons. Since the spike arrival times are not controlled by an experimentalist they can be considered as stochastic. Thus a (potentially nonlinear) integrate-and-fire model with nonlinearity f(v) receives two inputs: an input $I(t)$ controlled by the experimentalists and a noisy input current $I^{\rm {noise}}(t)$ that describes the uncontrolled background input.

$\tau _{m}{\frac {dV}{dt}}=f(V)+RI(t)+RI^{\text{noise}}(t)$

**Stein's model** is the special case of a leaky integrate-and-fire neuron and a stationary white noise current $I^{\rm {noise}}(t)=\xi (t)$ with mean zero and unit variance. In the subthreshold regime, these assumptions yield the equation of the Ornstein–Uhlenbeck process

$\tau _{m}{\frac {dV}{dt}}=[E_{m}-V]+RI(t)+R\xi (t)$

However, in contrast to the standard Ornstein–Uhlenbeck process, the membrane voltage is reset whenever *V* hits the firing threshold *V*th . Calculating the interval distribution of the Ornstein–Uhlenbeck model for constant input with threshold leads to a first-passage time problem. Stein's neuron model and variants thereof have been used to fit interspike interval distributions of spike trains from real neurons under constant input current.

In the mathematical literature, the above equation of the Ornstein–Uhlenbeck process is written in the form

$dV=[E_{m}-V+RI(t)]{\frac {dt}{\tau _{m}}}+\sigma \,dW$

where $\sigma$ is the amplitude of the noise input and *dW* are increments of a Wiener process. For discrete-time implementations with time step dt the voltage updates are

$\Delta V=[E_{m}-V+RI(t)]{\frac {\Delta t}{\tau _{m}}}+\sigma {\sqrt {\tau _{m}}}y$

where y is drawn from a Gaussian distribution with zero mean unit variance. The voltage is reset when it hits the firing threshold *V*th .

The noisy input model can also be used in generalized integrate-and-fire models. For example, the exponential integrate-and-fire model with noisy input reads

$\tau _{m}{\frac {dV}{dt}}=E_{m}-V+\Delta _{T}\exp \left({\frac {V-V_{T}}{\Delta _{T}}}\right)+RI(t)+R\xi (t)$

For constant deterministic input $I(t)=I_{0}$ it is possible to calculate the mean firing rate as a function of $I_{0}$ . This is important because the frequency-current relation (f-I-curve) is often used by experimentalists to characterize a neuron.

The leaky integrate-and-fire with noisy input has been widely used in the analysis of networks of spiking neurons. Noisy input is also called 'diffusive noise' because it leads to a diffusion of the subthreshold membrane potential around the noise-free trajectory (Johannesma, The theory of spiking neurons with noisy input is reviewed in Chapter 8.2 of the textbook *Neuronal Dynamics*.

### Noisy output model (escape noise)

In deterministic integrate-and-fire models, a spike is generated if the membrane potential *V*(t) hits the threshold $V_{th}$ . In noisy output models, the strict threshold is replaced by a noisy one as follows. At each moment in time t, a spike is generated stochastically with instantaneous stochastic intensity or 'escape rate'

$\rho (t)=f(V(t)-V_{th})$

that depends on the momentary difference between the membrane voltage *V*(t) and the threshold $V_{th}$ . A common choice for the **'escape rate' f** (that is consistent with biological data) is

$f(V-V_{th})={\frac {1}{\tau _{0}}}\exp[\beta (V-V_{th})]$

where $\tau _{0}$ is a time constant that describes how quickly a spike is fired once the membrane potential reaches the threshold and $\beta$ is a sharpness parameter. For $\beta \to \infty$ the threshold becomes sharp and spike firing occurs deterministically at the moment when the membrane potential hits the threshold from below. The sharpness value found in experiments is $1/\beta \approx 4mV$ which means that neuronal firing becomes non-negligible as soon as the membrane potential is a few mV below the formal firing threshold.

The escape rate process via a soft threshold is reviewed in Chapter 9 of the textbook *Neuronal Dynamics.*

For models in discrete time, a spike is generated with probability

$P_{F}(t_{n})=F[V(t_{n})-V_{th}]$

that depends on the momentary difference between the membrane voltage *V* at time $t_{n}$ and the threshold $V_{th}$ . The function F is often taken as a standard sigmoidal $F(x)=0.5[1+\tanh(\gamma x)]$ with steepness parameter $\gamma$ , similar to the update dynamics in artificial neural networks. But the functional form of F can also be derived from the stochastic intensity f in continuous time introduced above as $F(y_{n})\approx 1-\exp[y_{n}\Delta t]$ where $y_{n}=V(t_{n})-V_{th}$ is the threshold distance.

Integrate-and-fire models with output noise can be used to predict the peristimulus time histogram (PSTH) of real neurons under arbitrary time-dependent input. For non-adaptive integrate-and-fire neurons, the interval distribution under constant stimulation can be calculated from stationary renewal theory.

### Spike response model (SRM)

| Spike response model | Ref. |
|---|---|
| Sub-threshold voltage for time-dependent input current |   |
| Firing times for time-dependent input current |   |
| Firing Patterns in response to step current input |   |
| Interspike interval distribution |   |
| Spike-afterpotential |   |
| refractoriness and dynamic firing threshold |   |

*main article*: Spike response model

The spike response model (SRM) is a generalized linear model for the subthreshold membrane voltage combined with a nonlinear output noise process for spike generation. The membrane voltage *V*(t) at time *t* is

$V(t)=\sum _{f}\eta (t-t^{f})+\int \limits _{0}^{\infty }\kappa (s)I(t-s)\,ds+V_{\mathrm {rest} }$

where *t*f is the firing time of spike number f of the neuron, *V*rest is the resting voltage in the absence of input, *I(t-s)* is the input current at time t-s and $\kappa (s)$ is a linear filter (also called kernel) that describes the contribution of an input current pulse at time t-s to the voltage at time t. The contributions to the voltage caused by a spike at time $t^{f}$ are described by the refractory kernel $\eta (t-t^{f})$ . In particular, $\eta (t-t^{f})$ describes the reset after the spike and the time course of the spike-afterpotential following a spike. It therefore expresses the consequences of refractoriness and adaptation. The voltage V(t) can be interpreted as the result of an integration of the differential equation of a leaky integrate-and-fire model coupled to an arbitrary number of spike-triggered adaptation variables.

Spike firing is stochastic and happens with a time-dependent stochastic intensity (instantaneous rate)

$f(V-\vartheta (t))={\frac {1}{\tau _{0}}}\exp[\beta (V-\vartheta (t))]$

with parameters $\tau _{0}$ and $\beta$ and a **dynamic threshold** $\vartheta (t)$ given by

$\vartheta (t)=\vartheta _{0}+\sum _{f}\theta _{1}(t-t^{f})$

Here $\vartheta _{0}$ is the firing threshold of an inactive neuron and $\theta _{1}(t-t^{f})$ describes the increase of the threshold after a spike at time $t^{f}$ . In case of a fixed threshold, one sets $\theta _{1}(t-t^{f})=0$ . For $\beta \to \infty$ the threshold process is deterministic.

The time course of the filters $\eta ,\kappa ,\theta _{1}$ that characterize the spike response model can be directly extracted from experimental data. With optimized parameters the SRM describes the time course of the subthreshold membrane voltage for time-dependent input with a precision of 2mV and can predict the timing of most output spikes with a precision of 4ms. The SRM is closely related to linear-nonlinear-Poisson cascade models (also called Generalized Linear Model). The estimation of parameters of probabilistic neuron models such as the SRM using methods developed for Generalized Linear Models is discussed in Chapter 10 of the textbook *Neuronal Dynamics*.

The name **spike response model** arises because, in a network, the input current for neuron i is generated by the spikes of other neurons so that in the case of a network the voltage equation becomes

$V_{i}(t)=\sum _{f}\eta _{i}(t-t_{i}^{f})+\sum _{j=1}^{N}w_{ij}\sum _{f'}\varepsilon _{ij}(t-t_{j}^{f'})+V_{\mathrm {rest} }$

where $t_{j}^{f'}$ is the firing times of neuron j (i.e., its spike train); $\eta _{i}(t-t_{i}^{f})$ describes the time course of the spike and the spike after-potential for neuron i; and $w_{ij}$ and $\varepsilon _{ij}(t-t_{j}^{f'})$ describe the amplitude and time course of an excitatory or inhibitory **postsynaptic potential** (PSP) caused by the spike $t_{j}^{f'}$ of the presynaptic neuron j. The time course $\varepsilon _{ij}(s)$ of the PSP results from the convolution of the postsynaptic current $I(t)$ caused by the arrival of a presynaptic spike from neuron j with the membrane filter $\kappa (s)$ .

### SRM0

The **SRM0** is a stochastic neuron model related to time-dependent nonlinear renewal theory and a simplification of the Spike Response Model (SRM). The main difference to the voltage equation of the SRM introduced above is that in the term containing the refractory kernel $\eta (s)$ there is no summation sign over past spikes: only the *most recent spike* (denoted as the time ${\hat {t}}$ ) matters. Another difference is that the threshold is constant. The model SRM0 can be formulated in discrete or continuous time. For example, in continuous time, the single-neuron equation is

$V(t)=\eta (t-{\hat {t}})+\int _{0}^{\infty }\kappa (s)I(t-s)\,ds+V_{\mathrm {rest} }$

and the network equations of the SRM0 are

$V_{i}(t\mid {\hat {t}}_{i})=\eta _{i}(t-{\hat {t}}_{i})+\sum _{j}w_{ij}\sum _{f}\varepsilon _{ij}(t-{\hat {t}}_{i},t-t^{f})+V_{\mathrm {rest} }$

where ${\hat {t}}_{i}$ is the *last firing time neuron* i. Note that the time course of the postsynaptic potential $\varepsilon _{ij}$ is also allowed to depend on the time since the last spike of neuron i to describe a change in membrane conductance during refractoriness. The instantaneous firing rate (stochastic intensity) is

$f(V-\vartheta )={\frac {1}{\tau _{0}}}\exp[\beta (V-V_{th})]$

where $V_{th}$ is a fixed firing threshold. Thus spike firing of neuron i depends only on its input and the time since neuron i has fired its last spike.

With the SRM0, the interspike-interval distribution for constant input can be mathematically linked to the shape of the refractory kernel $\eta$ . Moreover the stationary frequency-current relation can be calculated from the escape rate in combination with the refractory kernel $\eta$ . With an appropriate choice of the kernels, the SRM0 approximates the dynamics of the Hodgkin-Huxley model to a high degree of accuracy. Moreover, the PSTH response to arbitrary time-dependent input can be predicted.


## Didactic toy models of membrane voltage

The models in this category are highly simplified toy models that qualitatively describe the membrane voltage as a function of input. They are mainly used for didactic reasons in teaching but are not considered valid neuron models for large-scale simulations or data fitting.

### FitzHugh–Nagumo

Sweeping simplifications to Hodgkin–Huxley were introduced by FitzHugh and Nagumo in 1961 and 1962. Seeking to describe "regenerative self-excitation" by a nonlinear positive-feedback membrane voltage and recovery by a linear negative-feedback gate voltage, they developed the model described by

${\begin{aligned}{rcl}{\dfrac {dV}{dt}}&=V-V^{3}/3-w+I_{\mathrm {ext} }\\\tau {\dfrac {dw}{dt}}&=V-a-bw\end{aligned}}$

where we again have a membrane-like voltage and input current with a slower general gate voltage *w* and experimentally-determined parameters *a* = -0.7, *b* = 0.8, *τ* = 1/0.08. Although not derivable from biology, the model allows for a simplified, immediately available dynamic, without being a trivial simplification. The experimental support is weak, but the model is useful as a didactic tool to introduce dynamics of spike generation through phase plane analysis. See Chapter 7 in the textbook *Methods of Neuronal Modeling*.

### Morris–Lecar

In 1981, Morris and Lecar combined the Hodgkin–Huxley and FitzHugh–Nagumo models into a voltage-gated calcium channel model with a delayed-rectifier potassium channel represented by

${\begin{aligned}C{\frac {dV}{dt}}&=-I_{\mathrm {ion} }(V,w)+I\\{\frac {dw}{dt}}&=\varphi \cdot {\frac {w_{\infty }-w}{\tau _{w}}}\end{aligned}}$

where $I_{\mathrm {ion} }(V,w)={\bar {g}}_{\mathrm {Ca} }m_{\infty }\cdot (V-V_{\mathrm {Ca} })+{\bar {g}}_{\mathrm {K} }w\cdot (V-V_{\mathrm {K} })+{\bar {g}}_{\mathrm {L} }\cdot (V-V_{\mathrm {L} })$ . The experimental support of the model is weak, but the model is useful as a didactic tool to introduce dynamics of spike generation through phase plane analysis. See Chapter 7 in the textbook *Methods of Neuronal Modeling*.

A two-dimensional neuron model very similar to the Morris-Lecar model can be derived step-by-step starting from the Hodgkin-Huxley model. See Chapter 4.2 in the textbook Neuronal Dynamics.

### Hindmarsh–Rose

Building upon the FitzHugh–Nagumo model, Hindmarsh and Rose proposed in 1984 a model of neuronal activity described by three coupled first-order differential equations:

${\begin{aligned}{\frac {dx}{dt}}&=y+3x^{2}-x^{3}-z+I\\{\frac {dy}{dt}}&=1-5x^{2}-y\\{\frac {dz}{dt}}&=r\cdot (4(x+{\tfrac {8}{5}})-z)\end{aligned}}$

with *r*2 = *x*2 + *y*2 + *z*2, and *r* ≈ 10−2 so that the *z* variable only changes very slowly. This extra mathematical complexity allows a great variety of dynamic behaviors for the membrane potential, described by the *x* variable of the model, which includes chaotic dynamics. This makes the Hindmarsh–Rose neuron model very useful, because it is still simple, allows a good qualitative description of the many different firing patterns of the action potential, in particular bursting, observed in experiments. Nevertheless, it remains a toy model and has not been fitted to experimental data. It is widely used as a reference model for bursting dynamics.

### Theta model and quadratic integrate-and-fire

The theta model, or Ermentrout–Kopell canonical Type I model, is mathematically equivalent to the quadratic integrate-and-fire model which in turn is an approximation to the exponential integrate-and-fire model and the Hodgkin-Huxley model. It is called a canonical model because it is one of the generic models for constant input close to the bifurcation point, which means close to the transition from silent to repetitive firing.

The standard formulation of the theta model is

${\frac {d\theta (t)}{dt}}=(I-I_{0})[1+\cos(\theta )]+[1-\cos(\theta )]$

The equation for the quadratic integrate-and-fire model is (see Chapter 5.3 in the textbook Neuronal Dynamics )

$\tau _{\mathrm {m} }{\frac {dV_{\mathrm {m} }(t)}{dt}}=(I-I_{0})R+[V_{\mathrm {m} }(t)-E_{\mathrm {m} }][V_{\mathrm {m} }(t)-V_{\mathrm {T} }]$

The equivalence of theta model and quadratic integrate-and-fire is for example reviewed in Chapter 4.1.2.2 of spiking neuron models.

For input $I(t)$ that changes over time or is far away from the bifurcation point, it is preferable to work with the exponential integrate-and-fire model (if one wants to stay in the class of one-dimensional neuron models), because real neurons exhibit the nonlinearity of the exponential integrate-and-fire model.


## Sensory input-stimulus encoding neuron models

The models in this category were derived following experiments involving natural stimulation such as light, sound, touch, or odor. In these experiments, the spike pattern resulting from each stimulus presentation varies from trial to trial, but the averaged response from several trials often converges to a clear pattern. Consequently, the models in this category generate a probabilistic relationship between the input stimulus to spike occurrences. Importantly, the recorded neurons are often located several processing steps after the sensory neurons, so that these models summarize the effects of the sequence of processing steps in a compact form

### The non-homogeneous Poisson process model (Siebert)

Siebert modeled the neuron spike firing pattern using a non-homogeneous Poisson process model, following experiments involving the auditory system. According to Siebert, the probability of a spiking event at the time interval $[t,t+\Delta _{t}]$ is proportional to a non-negative function $g[s(t)]$ , where $s(t)$ is the raw stimulus.:

$P_{\text{spike}}(t\in [t',t'+\Delta _{t}])=\Delta _{t}\cdot g[s(t)]$

Siebert considered several functions as $g[s(t)]$ , including $g[s(t)]\propto s^{2}(t)$ for low stimulus intensities.

The main advantage of Siebert's model is its simplicity. The shortcomings of the model is its inability to reflect properly the following phenomena:

- The transient enhancement of the neuronal firing activity in response to a step stimulus.
- The saturation of the firing rate.
- The values of inter-spike-interval-**histogram** at short intervals values (close to zero).

These shortcomings are addressed by the age-dependent point process model and the two-state Markov Model.

### Refractoriness and age-dependent point process model

Berry and Meister studied neuronal refractoriness using a stochastic model that predicts spikes as a product of two terms, a function f(s(t)) that depends on the time-dependent stimulus s(t) and one a recovery function $w(t-{\hat {t}})$ that depends on the time since the last spike

$\rho (t)=f(s(t))w(t-{\hat {t}})$

The model is also called an *inhomogeneous Markov interval (IMI) process*. Similar models have been used for many years in auditory neuroscience. Since the model keeps memory of the last spike time it is non-Poisson and falls in the class of time-dependent renewal models. It is closely related to the model SRM0 with exponential escape rate. Importantly, it is possible to fit parameters of the age-dependent point process model so as to describe not just the PSTH response, but also the interspike-interval statistics.

### Linear-nonlinear Poisson cascade model and GLM

The linear-nonlinear-Poisson cascade model is a cascade of a linear filtering process followed by a nonlinear spike generation step. In the case that output spikes feed back, via a linear filtering process, we arrive at a model that is known in the neurosciences as Generalized Linear Model (GLM). The GLM is mathematically equivalent to the spike response model SRM) with escape noise; but whereas in the SRM the internal variables are interpreted as the membrane potential and the firing threshold, in the GLM the internal variables are abstract quantities that summarizes the net effect of input (and recent output spikes) before spikes are generated in the final step.

### The two-state Markov model (Nossenson & Messer)

The spiking neuron model by Nossenson & Messer produces the probability of the neuron firing a spike as a function of either an external or pharmacological stimulus. The model consists of a cascade of a receptor layer model and a spiking neuron model, as shown in Fig 4. The connection between the external stimulus to the spiking probability is made in two steps: First, a receptor cell model translates the raw external stimulus to neurotransmitter concentration, and then, a spiking neuron model connects neurotransmitter concentration to the firing rate (spiking probability). Thus, the spiking neuron model by itself depends on neurotransmitter concentration at the input stage.

An important feature of this model is the prediction for neurons firing rate pattern which captures, using a low number of free parameters, the characteristic edge emphasized response of neurons to a stimulus pulse, as shown in Fig. 5. The firing rate is identified both as a normalized probability for neural spike firing and as a quantity proportional to the current of neurotransmitters released by the cell. The expression for the firing rate takes the following form:

$R_{\text{fire}}(t)={\frac {P_{\text{spike}}(t;\Delta _{t})}{\Delta _{t}}}=[y(t)+R_{0}]\cdot P_{0}(t)$

where,

- P0 is the probability of the neuron being "armed" and ready to fire. It is given by the following differential equation:

${\dot {P}}_{0}=-[y(t)+R_{0}+R_{1}]\cdot P_{0}(t)+R_{1}$

P0 could be generally calculated recursively using the Euler method, but in the case of a pulse of stimulus, it yields a simple closed-form expression.

- *y*(*t*) is the input of the model and is interpreted as the neurotransmitter concentration on the cell surrounding (in most cases glutamate). For an external stimulus it can be estimated through the receptor layer model:

$y(t)\simeq g_{\text{gain}}\cdot \langle s^{2}(t)\rangle ,$

with $\langle s^{2}(t)\rangle$ being a short temporal average of stimulus power (given in Watt or other energy per time unit).

- *R*0 corresponds to the intrinsic spontaneous firing rate of the neuron.
- *R*1 is the recovery rate of the neuron from the refractory state.

Other predictions by this model include:

1) The averaged evoked response potential (ERP) due to the population of many neurons in unfiltered measurements resembles the firing rate.

2) The voltage variance of activity due to multiple neuron activity resembles the firing rate (also known as Multi-Unit-Activity power or MUA).

3) The inter-spike-interval probability distribution takes the form a gamma-distribution like function.

| Property of the Model by Nossenson & Messer | Ref. | Description of experimental evidence |
|---|---|---|
| The shape of the firing rate in response to an auditory stimulus pulse |   | The Firing Rate has the same shape of Fig 5. |
| The shape of the firing rate in response to a visual stimulus pulse |   | The Firing Rate has the same shape of Fig 5. |
| The shape of the firing rate in response to an olfactory stimulus pulse |   | The Firing Rate has the same shape as Fig 5. |
| The shape of the firing rate in response to a somatosensory stimulus |   | The Firing Rate has the same shape as Fig 5. |
| The change in firing rate in response to neurotransmitter application (mostly glutamate) |   | Firing Rate change in response to neurotransmitter application (Glutamate) |
| Square dependence between an auditory stimulus pressure and the firing rate |   | Square Dependence between Auditory Stimulus pressure and the Firing Rate (- Linear dependence in pressure square (power)). |
| Square dependence between visual stimulus electric field (volts) and the firing rate |   | Square dependence between visual stimulus electric field (volts) - Linear Dependence between Visual Stimulus *Power* and the Firing Rate. |
| The shape of the Inter-Spike-Interval Statistics (ISI) |   | ISI shape resembles the gamma-function-like |
| The ERP resembles the firing rate in unfiltered measurements |   | The shape of the averaged evoked response potential in response to stimulus resembles the firing rate (Fig. 5). |
| MUA power resembles the firing rate |   | The shape of the empirical variance of extra-cellular measurements in response to stimulus pulse resembles the firing rate (Fig. 5). |


## Pharmacological input stimulus neuron models

The models in this category produce predictions for experiments involving pharmacological stimulation.

### Synaptic transmission (Koch & Segev)

According to the model by Koch and Segev, the response of a neuron to individual neurotransmitters can be modeled as an extension of the classical Hodgkin–Huxley model with both standard and nonstandard kinetic currents. Four neurotransmitters primarily influence the CNS. AMPA/kainate receptors are fast excitatory mediators while NMDA receptors mediate considerably slower currents. Fast inhibitory currents go through GABAA receptors, while GABAB receptors mediate by secondary *G*-protein-activated potassium channels. This range of mediation produces the following current dynamics:

- $I_{\mathrm {AMPA} }(t,V)={\bar {g}}_{\mathrm {AMPA} }\cdot [O]\cdot (V(t)-E_{\mathrm {AMPA} })$
- $I_{\mathrm {NMDA} }(t,V)={\bar {g}}_{\mathrm {NMDA} }\cdot B(V)\cdot [O]\cdot (V(t)-E_{\mathrm {NMDA} })$
- $I_{\mathrm {GABA_{A}} }(t,V)={\bar {g}}_{\mathrm {GABA_{A}} }\cdot ([O_{1}]+[O_{2}])\cdot (V(t)-E_{\mathrm {Cl} })$
- $I_{\mathrm {GABA_{B}} }(t,V)={\bar {g}}_{\mathrm {GABA_{B}} }\cdot {\tfrac {[G]^{n}}{[G]^{n}+K_{\mathrm {d} }}}\cdot (V(t)-E_{\mathrm {K} })$

where *ḡ* is the maximal conductance (around 1S) and *E* is the equilibrium potential of the given ion or transmitter (AMDA, NMDA, Cl, or K), while [*O*] describes the fraction of open receptors. For NMDA, there is a significant effect of *magnesium block* that depends sigmoidally on the concentration of intracellular magnesium by *B*(*V*). For GABAB, [*G*] is the concentration of the *G*-protein, and *K*d describes the dissociation of *G* in binding to the potassium gates.

The dynamics of this more complicated model have been well-studied experimentally and produce important results in terms of very quick synaptic potentiation and depression, that is fast, short-term learning.

The stochastic **model by Nossenson and Messer** translates neurotransmitter concentration at the input stage to the probability of releasing neurotransmitter at the output stage. For a more detailed description of this model, see the Two state Markov model section above.


## HTM neuron model

The HTM neuron model was developed by Jeff Hawkins and researchers at Numenta and is based on a theory called Hierarchical Temporal Memory, originally described in the book *On Intelligence*. It is based on neuroscience and the physiology and interaction of pyramidal neurons in the neocortex of the human brain.

| **Artificial Neural Network (ANN)** | **Neocortical Pyramidal Neuron (Biological Neuron)** | **HTM Model Neuron** |
|---|---|---|
| - Few synapses - No dendrites - Sum input x weights - Learns by modifying the weights of synapses | - Thousands of synapses on the dendrites - Active dendrites: cell recognizes hundreds of unique patterns - Co-activation of a set of synapses on a dendritic segment causes an NMDA spike and depolarization at the soma - Sources of input to the cell: Feedforward inputs that form synapses proximal to the soma and directly lead to action potentials NMDA spikes generated in the more distal basal Apical dendrites that depolarize the soma (usually insufficient to generate a somatic action potential) - Learns by growing new synapses | - Inspired by the pyramidal cells in neocortex layers 2/3 and 5 - Thousands of synapses - Active dendrites: cell recognizes hundreds of unique patterns - Models dendrites and NMDA spikes with each array of coincident detectors having a set of synapses - Learns by modeling the growth of new synapses |
