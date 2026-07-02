---
title: "Neuron (software)"
source: https://en.wikipedia.org/wiki/Neuron_(software)
domain: neural-simulation
license: CC-BY-SA-4.0
tags: neural simulation software, leaky integrate-and-fire, dendrite compartmental modelling, blue brain project
fetched: 2026-07-02
---

# Neuron (software)

**Neuron** is a simulation environment for modeling individual and networks of neurons. It was primarily developed by Michael Hines, John W. Moore, and Ted Carnevale at Yale and Duke.

Neuron models individual neurons via the use of sections that are automatically subdivided into individual compartments, instead of requiring the user to manually create compartments. The primary scripting language is hoc but a Python interface is also available. Programs can be written interactively in a shell, or loaded from a file. Neuron supports parallelization via the MPI protocol.

Neuron is capable of handling diffusion-reaction models, and integrating diffusion functions into models of synapses and cellular networks. Parallelization is possible via internal multithreaded routines, for use on multi-core computers. The properties of the membrane channels of the neuron are simulated using compiled mechanisms written using the NMODL language or by compiled routines operating on internal data structures that are set up with Channel Builder.

Along with the analogous software platform GENESIS, Neuron is the basis for instruction in computational neuroscience in many courses and laboratories around the world.

## User interface

Neuron features a graphical user interface (GUI), for use by individuals with minimal programming experience. The GUI comes equipped with a builder for single and multiple compartment cells, networks, network cells, channels and linear electric circuits. Single and multiple compartment cells differ in that multiple compartment cells features several "sections", each with potentially distinct parameters for dimensions and kinetics. Tutorials are available on the Neuron website, including for getting basic models out of the cell, channel and network builders. With these builders, the user can form the basis of all simulations and models.

### Cell Builder

Cell Builder allows the user to generate and modify stick figure cell structures. These sections form the basis of functionally distinct areas of the neuron.

The user can define functionally distinct groups of sections. Sections branching from one another can be labeled "dendrites," while another, single section that projects from the same central one can be labeled as the "axon." The user can define parameters along which certain values are variable as a function across a section. For instance, path length along a subset can be defined as a domain, the functions along which can then be defined later.

The user can select either individual sections, or groups and set precise parameters for length, diameter, area and length for that group or section. Any of these values can be set as a function of length or some other parameter of the corresponding section. The user can set the number of functional segments in a section, which is a strategy for spatial resolution. The higher the number of segments, the more precisely Neuron can handle a function in a section. Segments are the points where point process managers can be associated.

Users can define kinetic and electro-physiological functions across both subsets and sections. Neuron comes equipped with a probabilistic model of Hodgkin-Huxley Model giant squid axon kinetics, as well as a function to model passive leak channel kinetics. Both of these functions, and the features they describe, can be added to the membrane of the constructed cell. Values for leak rate, sodium conductance and potassium conductance can be set for modeling these kinetics can be set as functions over a parameterized domain. Channels become available for implementation in a cell membrane.

### Channel Builder

The user can generate both voltage- and ligand-gated channel models. Channel Builder supports local point channels, generally used for single, large channels whose function is to be modeled, and general channels whose density across the cell can be defined. Maximum conductance, reversal potential, ligand sensitivity, ion permeability, as well as precise dynamics of transitional states using activation and inactivation variables, and including differential conductance, can be defined.

### Network and Network Cell Builder

Neuron allows for the generation of mixed models, populated with both artificial cells and neurons. Artificial cells essentially function as point processes, implemented into the network. Artificial cells require only a point process, with defined parameters. The user can create the structure and dynamics of network cells. The user can create synapses, using simulated synapse point processes as archetypes. Parameters on these point processes can be manipulated to simulate both inhibitory and excitatory responses. Synapses can be placed on specific segments of the constructed cell, wherein, again, they will behave as point processes, except that they are sensitive to the activity of a pre-synaptic element. Cells can be managed. The user creates the basic grid of network cells, taking previously completed network cells as archetypes. Connections can be defined between source cells and target synapses on other cells. The cell containing the target synapse becomes the post-synaptic element, whereas the source cells function as pre-synaptic elements. Weights can be added to define strength of activation of a synapse by the pre-synaptic cell. A plot option can be activated to open a graph of spikes across time for individual neurons.

### Simulation and recording

Neuron comes equipped with a slew of simulation tools. Most notably, it includes several "point processes," which are simple functions at a particular segment of a cell. Point processes include simulations of voltage, patch, single electrode and current clamps, as well as several simulated synapses. Synapse point processes are distinct for their ability to model stimulation intensities that vary non-linearly across time. These can be placed on any segment of any section of a built cell, individual or network, and their precise values, including amplitude and duration of stimulation, delay time of activation in a run and time decay parameters (for synapses), can be defined from the point process manager module. When implemented into a network as synapses, point process parameters are defined in the synapse builder for a particular network cell. Graphs describing voltage, conductance, and current axes over time can be used to describe changes in electrical state at the location of any segment on the cell. Neuron allows for graphs of change at both individual points over time, and across an entire section through time. Duration of run can be set. All point processes, including those standing for cells or synapses of artificial neurons, and all graphs reflect the duration.

## Examples

This example creates a simple cell, with a single compartment soma and a multi compartment axon. It has the dynamics of the cell membrane simulated using Hodgkin-Huxley squid axon kinetics. The simulator stimulates the cell and runs for 50 ms.

```mw
//create two sections, the body of the neuron and a very long axon
create soma, axon

soma {
	//length is set to 100 micrometers	
	L = 100
	//diameter is set to 100 micrometers
	diam = 100
	//insert a mechanism simulating the standard squid Hodgkin–Huxley channels
	insert hh
	//insert a mechanism simulating the passive membrane properties
	insert pas
}
axon {
	L = 5000
	diam = 10
	insert hh
	insert pas
	//the axon shall be simulated using 10 compartments. By default a single compartment is used
	nseg = 10
}

//connect the proximal end of the axon to the distal end of the soma
connect axon(0), soma(1)

//declare and insert a current clamp into the middle of the soma
objref stim
soma stim = new IClamp(0.5)

//define some parameters of the stimulus: delay, duration (both in ms) and amplitude (in nA)
stim.del = 10
stim.dur = 5
stim.amp = 10

//load a default NEURON library file that defines the run routine
load_file("stdrun.hoc")
//set the simulation to run for 50 ms
tstop = 50

//run the simulation
run()
```

A plot can be generated showing the voltage traces starting from the soma and the distal end of the axon. The action potential at the end of the axon arrives slightly later than it appears in the soma at the point of stimulation. The plot is membrane voltage versus time.
