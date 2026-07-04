---
title: "Hysteresis"
source: https://en.wikipedia.org/wiki/Hysteresis_loop
domain: olsen-cycle
license: CC-BY-SA-4.0
tags: olsen cycle
fetched: 2026-07-04
---

# Hysteresis

(Redirected from

Hysteresis loop

)

**Hysteresis** is the dependence of the state of a system on its history. For example, a magnet may have more than one possible magnetic moment in a given magnetic field, depending on how the field changed in the past. Such a system is called **hysteretic**. Plots of a single component of the moment often form a loop or hysteresis curve, where there are different values of one variable depending on the direction of change of another variable. This history dependence is the basis of memory in a hard disk drive and the remanence that retains a record of the Earth's magnetic field magnitude in the past. Hysteresis occurs in ferromagnetic and ferroelectric materials, as well as in the deformation of rubber bands and shape-memory alloys and many other natural phenomena. In natural systems, it is often associated with irreversible thermodynamic change such as phase transitions and with internal friction; and dissipation is a common side effect.

Hysteresis can be found in physics, chemistry, engineering, biology, and economics. It is incorporated in many artificial systems: for example, in thermostats and Schmitt triggers, it prevents unwanted frequent switching.

Hysteresis can be a dynamic lag between an input and an output that disappears if the input is varied more slowly; this is known as *rate-dependent* hysteresis. However, phenomena such as the magnetic hysteresis loops are mainly *rate-independent*, which makes a durable memory possible.

Systems with hysteresis are nonlinear, and can be mathematically challenging to model. Some hysteretic models, such as the Preisach model (originally applied to ferromagnetism) and the Bouc–Wen model, attempt to capture general features of hysteresis; and there are also phenomenological models for particular phenomena such as the Jiles–Atherton model for ferromagnetism.

It is difficult to define hysteresis precisely. Isaak D. Mayergoyz wrote "...the very meaning of hysteresis varies from one area to another, from paper to paper and from author to author. As a result, a stringent mathematical definition of hysteresis is needed in order to avoid confusion and ambiguity.".

## Etymology and history

The term "hysteresis" is derived from ὑστέρησις, an Ancient Greek word meaning "deficiency" or "lagging behind". It was coined in 1881 by Sir James Alfred Ewing to describe the behaviour of magnetic materials.

Some early work on describing hysteresis in mechanical systems was performed by James Clerk Maxwell. Subsequently, hysteretic models have received significant attention in the works of Ferenc Preisach (Preisach model of hysteresis), Louis Néel and Douglas Hugh Everett in connection with magnetism and absorption. A more formal mathematical theory of systems with hysteresis was developed in the 1970s by a group of Russian mathematicians led by Mark Krasnosel'skii.

## Types

### Rate-dependent

One type of hysteresis is a lag between input and output. An example is a sinusoidal input *X(t)* that results in a sinusoidal output *Y(t)*, but with a phase lag *φ*:

${\begin{aligned}X(t)&=X_{0}\sin \omega t\\Y(t)&=Y_{0}\sin \left(\omega t-\varphi \right).\end{aligned}}$

Such behavior can occur in linear systems, and a more general form of response is

$Y(t)=\chi _{\text{i}}X(t)+\int _{0}^{\infty }\Phi _{\text{d}}(\tau )X(t-\tau )\,\mathrm {d} \tau ,$

where $\chi _{\text{i}}$ is the instantaneous response and $\Phi _{d}(\tau )$ is the impulse response to an impulse that occurred $\tau$ time units in the past. In the frequency domain, input and output are related by a complex *generalized susceptibility* that can be computed from $\Phi _{d}$ ; it is mathematically equivalent to a transfer function in linear filter theory and analogue signal processing.

This kind of hysteresis is often referred to as *rate-dependent hysteresis*. If the input is reduced to zero, the output continues to respond for a finite time. This constitutes a memory of the past, but a limited one because it disappears as the output decays to zero. The phase lag depends on the frequency of the input, and goes to zero as the frequency decreases.

When rate-dependent hysteresis is due to dissipative effects like friction, it is associated with power loss.

### Rate-independent

Systems with *rate-independent hysteresis* have a *persistent* memory of the past that remains after the transients have died out. The future development of such a system depends on the history of states visited, but does not fade as the events recede into the past. If an input variable *X(t)* cycles from *X*0 to *X*1 and back again, the output *Y(t)* may be *Y*0 initially but a different value *Y*2 upon return. The values of *Y(t)* depend on the path of values that *X(t)* passes through but not on the speed at which it traverses the path. Many authors restrict the term hysteresis to mean only rate-independent hysteresis. Hysteresis effects can be characterized using the Preisach model and the generalized Prandtl−Ishlinskii model.

## In engineering

### Control systems

In control systems, hysteresis can be used to filter signals so that the output reacts less rapidly than it otherwise would by taking recent system history into account. For example, a thermostat controlling a heater may switch the heater on when the temperature drops below A, but not turn it off until the temperature rises above B. (For instance, if one wishes to maintain a temperature of 20 °C then one might set the thermostat to turn the heater on when the temperature drops to below 18 °C and off when the temperature exceeds 22 °C).

Similarly, a pressure switch can be designed to exhibit hysteresis, with pressure set-points substituted for temperature thresholds.

### Electronic circuits

Often, some amount of hysteresis is intentionally added to an electronic circuit to prevent unwanted rapid switching. This and similar techniques are used to compensate for contact bounce in switches, or noise in an electrical signal.

A Schmitt trigger is a simple electronic circuit that exhibits this property.

A latching relay uses a solenoid to actuate a ratcheting mechanism that keeps the relay closed even if power to the relay is terminated.

Some positive feedback from the output to one input of a comparator can increase the natural hysteresis (a function of its gain) it exhibits.

Hysteresis is essential to the workings of some memristors (circuit components which "remember" changes in the current passing through them by changing their resistance).

Hysteresis can be used when connecting arrays of elements such as nanoelectronics, electrochrome cells and memory effect devices using passive matrix addressing. Shortcuts are made between adjacent components (see crosstalk) and the hysteresis helps to keep the components in a particular state while the other components change states. Thus, all rows can be addressed at the same time instead of individually.

In the field of audio electronics, a noise gate often implements hysteresis intentionally to prevent the gate from "chattering" when signals close to its threshold are applied.

### User interface design

A hysteresis is sometimes intentionally added to computer algorithms. The field of user interface design has borrowed the term hysteresis to refer to times when the state of the user interface intentionally lags behind the apparent user input. For example, a menu that was drawn in response to a mouse-over event may remain on-screen for a brief moment after the mouse has moved out of the trigger region and the menu region. This allows the user to move the mouse directly to an item on the menu, even if part of that direct mouse path is outside of both the trigger region and the menu region. For instance, right-clicking on the desktop in most Windows interfaces will create a menu that exhibits this behavior.

### Aerodynamics

In aerodynamics, hysteresis can be observed when decreasing the angle of attack of a wing after stall, regarding the lift and drag coefficients. The angle of attack at which the flow on top of the wing reattaches is generally lower than the angle of attack at which the flow separates during the increase of the angle of attack.

### Hydraulics

Hysteresis can be observed in the stage-flow relationship of a river during rapidly changing conditions such as passing of a flood wave. It is most pronounced in low gradient streams with steep leading edge hydrographs.

### Backlash

Moving parts within machines, such as the components of a gear train, normally have a small gap between them, to allow movement and lubrication. As a consequence of this gap, any reversal in direction of a drive part will not be passed on immediately to the driven part. This unwanted delay is normally kept as small as practicable, and is usually called backlash. The amount of backlash will increase with time as the surfaces of moving parts wear.

## In mechanics

### Elastic hysteresis

In the elastic hysteresis of rubber, the area in the centre of a hysteresis loop is the energy dissipated due to material internal friction.

Elastic hysteresis was one of the first types of hysteresis to be examined.

The effect can be demonstrated using a rubber band with weights attached to it. If the top of a rubber band is hung on a hook and small weights are attached to the bottom of the band one at a time, it will stretch and get longer. As more weights are *loaded* onto it, the band will continue to stretch because the force the weights are exerting on the band is increasing. When each weight is taken off, or *unloaded*, the band will contract as the force is reduced. As the weights are taken off, each weight that produced a specific length as it was loaded onto the band now contracts less, resulting in a slightly longer length as it is unloaded. This is because the band does not obey Hooke's law perfectly. The hysteresis loop of an idealized rubber band is shown in the figure.

In terms of force, the rubber band was harder to stretch when it was being loaded than when it was being unloaded. In terms of time, when the band is unloaded, the effect (the length) lagged behind the cause (the force of the weights) because the length has not yet reached the value it had for the same weight during the loading part of the cycle. In terms of energy, more energy was required during the loading than the unloading, the excess energy being dissipated as thermal energy.

Elastic hysteresis is more pronounced when the loading and unloading is done quickly than when it is done slowly. Some materials such as hard metals don't show elastic hysteresis under a moderate load, whereas other hard materials like granite and marble do. Materials such as rubber exhibit a high degree of elastic hysteresis.

When the intrinsic hysteresis of rubber is being measured, the material can be considered to behave like a gas. When a rubber band is stretched, it heats up, and if it is suddenly released, it cools down perceptibly. These effects correspond to a large hysteresis from the thermal exchange with the environment and a smaller hysteresis due to internal friction within the rubber. This proper, intrinsic hysteresis can be measured only if the rubber band is thermally isolated.

Small vehicle suspensions using rubber (or other elastomers) can achieve the dual function of springing and damping because rubber, unlike metal springs, has pronounced hysteresis and does not return all the absorbed compression energy on the rebound. Mountain bikes have made use of elastomer suspension, as did the original Mini car.

The primary cause of rolling resistance when a body (such as a ball, tire, or wheel) rolls on a surface is hysteresis. This is attributed to the viscoelastic characteristics of the material of the rolling body.

### Contact angle hysteresis

The contact angle formed between a liquid and solid phase will exhibit a range of contact angles that are possible. There are two common methods for measuring this range of contact angles. The first method is referred to as the tilting base method. Once a drop is dispensed on the surface with the surface level, the surface is then tilted from 0° to 90°. As the drop is tilted, the downhill side will be in a state of imminent wetting while the uphill side will be in a state of imminent dewetting. As the tilt increases the downhill contact angle will increase and represents the advancing contact angle while the uphill side will decrease; this is the receding contact angle. The values for these angles just prior to the drop releasing will typically represent the advancing and receding contact angles. The difference between these two angles is the contact angle hysteresis.

The second method is often referred to as the add/remove volume method. When the maximum liquid volume is removed from the drop without the interfacial area decreasing the receding contact angle is thus measured. When volume is added to the maximum before the interfacial area increases, this is the advancing contact angle. As with the tilt method, the difference between the advancing and receding contact angles is the contact angle hysteresis. Most researchers prefer the tilt method; the add/remove method requires that a tip or needle stay embedded in the drop which can affect the accuracy of the values, especially the receding contact angle.

### Bubble shape hysteresis

The equilibrium shapes of bubbles expanding and contracting on capillaries (blunt needles) can exhibit hysteresis depending on the relative magnitude of the maximum capillary pressure to ambient pressure, and the relative magnitude of the bubble volume at the maximum capillary pressure to the dead volume in the system. The bubble shape hysteresis is a consequence of gas compressibility, which causes the bubbles to behave differently across expansion and contraction. During expansion, bubbles undergo large non equilibrium jumps in volume, while during contraction the bubbles are more stable and undergo a relatively smaller jump in volume resulting in an asymmetry across expansion and contraction. The bubble shape hysteresis is qualitatively similar to the adsorption hysteresis, and as in the contact angle hysteresis, the interfacial properties play an important role in bubble shape hysteresis.

The existence of the bubble shape hysteresis has important consequences in interfacial rheology experiments involving bubbles. As a result of the hysteresis, not all sizes of the bubbles can be formed on a capillary. Further the gas compressibility causing the hysteresis leads to unintended complications in the phase relation between the applied changes in interfacial area to the expected interfacial stresses. These difficulties can be avoided by designing experimental systems to avoid the bubble shape hysteresis.

### Adsorption hysteresis

Hysteresis can also occur during physical adsorption processes. In this type of hysteresis, the quantity adsorbed is different when gas is being added than it is when being removed. The specific causes of adsorption hysteresis are still an active area of research, but it is linked to differences in the nucleation and evaporation mechanisms inside mesopores. These mechanisms are further complicated by effects such as cavitation and pore blocking.

In physical adsorption, hysteresis is evidence of mesoporosity-indeed, the definition of mesopores (2–50 nm) is associated with the appearance (50 nm) and disappearance (2 nm) of mesoporosity in nitrogen adsorption isotherms as a function of Kelvin radius. An adsorption isotherm showing hysteresis is said to be of Type IV (for a wetting adsorbate) or Type V (for a non-wetting adsorbate), and hysteresis loops themselves are classified according to how symmetric the loop is. Adsorption hysteresis loops also have the unusual property that it is possible to scan within a hysteresis loop by reversing the direction of adsorption while on a point on the loop. The resulting scans are called "crossing", "converging", or "returning", depending on the shape of the isotherm at this point.

### Matric potential hysteresis

The relationship between matric water potential and water content is the basis of the water retention curve. Matric potential measurements (Ψm) are converted to volumetric water content (θ) measurements based on a site or soil specific calibration curve. Hysteresis is a source of water content measurement error. Matric potential hysteresis arises from differences in wetting behaviour causing dry medium to re-wet; that is, it depends on the saturation history of the porous medium. Hysteretic behaviour means that, for example, at a matric potential (Ψm) of 5 kPa, the volumetric water content (θ) of a fine sandy soil matrix could be anything between 8% and 25%.

Tensiometers are directly influenced by this type of hysteresis. Two other types of sensors used to measure soil water matric potential are also influenced by hysteresis effects within the sensor itself. Resistance blocks, both nylon and gypsum based, measure matric potential as a function of electrical resistance. The relation between the sensor's electrical resistance and sensor matric potential is hysteretic. Thermocouples measure matric potential as a function of heat dissipation. Hysteresis occurs because measured heat dissipation depends on sensor water content, and the sensor water content–matric potential relationship is hysteretic. As of 2002, only desorption curves are usually measured during calibration of soil moisture sensors. Despite the fact that it can be a source of significant error, the sensor specific effect of hysteresis is generally ignored.

## In materials

### Magnetic hysteresis

When an external magnetic field is applied to a ferromagnetic material such as iron, the atomic domains align themselves with it. Even when the field is removed, part of the alignment will be retained: the material has become *magnetized*. Once magnetized, the magnet will stay magnetized indefinitely. To demagnetize it requires heat or a magnetic field in the opposite direction. This is the effect that provides the element of memory in a hard disk drive.

The relationship between field strength *H* and magnetization *M* is not linear in such materials. If a magnet is demagnetized (*H = M = 0*) and the relationship between *H* and *M* is plotted for increasing levels of field strength, *M* follows the *initial magnetization curve*. This curve increases rapidly at first and then approaches an asymptote called magnetic saturation. If the magnetic field is now reduced monotonically, *M* follows a different curve. At zero field strength, the magnetization is offset from the origin by an amount called the remanence. If the *H-M* relationship is plotted for all strengths of applied magnetic field the result is a hysteresis loop called the *main loop*. The width of the middle section is twice the coercivity of the material.

A closer look at a magnetization curve generally reveals a series of small, random jumps in magnetization called Barkhausen jumps. This effect is due to crystallographic defects such as dislocations.

Magnetic hysteresis loops are not exclusive to materials with ferromagnetic ordering. Other magnetic orderings, such as spin glass ordering, also exhibit this phenomenon.

#### Physical origin

The phenomenon of hysteresis in ferromagnetic materials is the result of two effects: rotation of magnetization and changes in size or number of magnetic domains. In general, the magnetization varies (in direction but not magnitude) across a magnet, but in sufficiently small magnets, it does not. In these single-domain magnets, the magnetization responds to a magnetic field by rotating. Single-domain magnets are used wherever a strong, stable magnetization is needed (for example, magnetic recording).

Larger magnets are divided into regions called *domains*. Across each domain, the magnetization does not vary; but between domains are relatively thin *domain walls* in which the direction of magnetization rotates from the direction of one domain to another. If the magnetic field changes, the walls move, changing the relative sizes of the domains. Because the domains are not magnetized in the same direction, the magnetic moment per unit volume is smaller than it would be in a single-domain magnet; but domain walls involve rotation of only a small part of the magnetization, so it is much easier to change the magnetic moment. The magnetization can also change by addition or subtraction of domains (called *nucleation* and *denucleation*).

#### Magnetic hysteresis models

The most known empirical models in hysteresis are Preisach and Jiles-Atherton models. These models allow an accurate modeling of the hysteresis loop and are widely used in the industry. However, these models lose the connection with thermodynamics and the energy consistency is not ensured. A more recent model, with a more consistent thermodynamical foundation, is the vectorial incremental nonconservative consistent hysteresis (VINCH) model of Lavet et al. (2011)

#### Applications

There are a great variety of applications of the hysteresis in ferromagnets. Many of these make use of their ability to retain a memory, for example magnetic tape, hard disks, and credit cards. In these applications, *hard* magnets (high coercivity) like iron are desirable, such that as much energy is absorbed as possible during the write operation and the resultant magnetized information is not easily erased.

On the other hand, magnetically *soft* (low coercivity) iron is used for the cores in electromagnets. The low coercivity minimizes the energy loss associated with hysteresis, as the magnetic field periodically reverses in the presence of an alternating current. The low energy loss during a hysteresis loop is the reason why soft iron is used for transformer cores and electric motors.

### Electrical hysteresis

Electrical hysteresis typically occurs in ferroelectric material, where domains of polarization contribute to the total polarization. Polarization is the electrical dipole moment (either C·m−2 or C·m). The mechanism, an organization of the polarization into domains, is similar to that of magnetic hysteresis.

### Liquid–solid-phase transitions

Hysteresis manifests itself in state transitions when melting temperature and freezing temperature do not agree. For example, agar melts at 85 °C (185 °F) and solidifies from 32 to 40 °C (90 to 104 °F). This is to say that once agar is melted at 85 °C, it retains a liquid state until cooled to 40 °C. Therefore, from the temperatures of 40 to 85 °C, agar can be either solid or liquid, depending on which state it was before.

## In biology

### Cell biology and genetics

Hysteresis in cell biology often follows bistable systems where the same input state can lead to two different, stable outputs. Where bistability can lead to digital, switch-like outputs from the continuous inputs of chemical concentrations and activities, hysteresis makes these systems more resistant to noise. These systems are often characterized by higher values of the input required to switch into a particular state as compared to the input required to stay in the state, allowing for a transition that is not continuously reversible, and thus less susceptible to noise.

#### Irreversible hysteresis

In the case of mitosis, irreversibility is essential to maintain the overall integrity of the system such that we have three designated checkpoints to account for this: G1/S, G2/M, and the spindle checkpoint. Irreversible hysteresis in this context ensures that once a cell commits to a specific phase (e.g., entering mitosis or DNA replication), it does not revert to a previous phase, even if conditions or regulatory signals change. Based on the irreversible hysteresis curve, there does exist an input at which the cell jumps to the next stable state, but there is no input that allows the cell to revert to its previous stable state, even when the input is 0, demonstrating irreversibility. Positive feedback is critical for generating hysteresis in the cell cycle. For example: In the G2/M transition, active CDK1 promotes the activation of more CDK1 molecules by inhibiting Wee1 (an inhibitor) and activating Cdc25 (a phosphatase that activates CDK1). These loops lock the cell into its current state and amplify the activation of CDK1. Positive feedback also serves to create a bistable system where CDK1 is either fully inactivated or fully activated. Hysteresis prevents the cell from oscillating between these two states from small perturbations in signal (input).

#### Reversible hysteresis

A biochemical system that is under the control of reversible hysteresis has both forward and reverse trajectories. The system generally requires a higher [input] to proceed forward into the next bistable state then to exit from that stage. For example, cells undergoing cell division exhibit reversible hysteresis in that it takes a higher concentration of cyclins to switch them from G2 phase into mitosis than to stay in mitosis once begun.  Additionally, because the [cyclin] required to reverse the cell back to the G2 phase is much lower than the [cyclin] to enter mitosis, this improved the bistability of mitosis because it is more resistance to weak or transient signals. Small perturbations the [input] will be unable to push the cell out of mitosis so easily.

#### History and memory

In systems with bistability, the same input level can correspond to two distinct stable states (e.g., "low output" and "high output"). The actual state of the system depends on its history –whether the input level was increasing (forward trajectory) or decreasing (backward trajectory). Thus, it is difficult to determine which state a cell is in if given only a bistability curve. The cell's ability to "remember" its prior state ensures stability and prevents it from switching states unnecessarily due to minor fluctuations in input. This memory is often maintained through molecular feedback loops, such as positive feedback in signaling pathways, or the persistence of regulatory molecules like proteins or phosphorylated components. For example, the refractory period in action potentials is primarily controlled by history. Absolute refraction period prevents a volted-gated sodium channel from activating or refiring after it has just fired. This is because following the absolute refractory period, the neuron is less excitable due to hyperpolarization caused by potassium efflux. This molecular inhibitory feedback creates a memory for the neuron or cell, so that the neuron does not fire too soon. As time passes, the neuron or cell will slowly lose the memory of having fired and will begin to fire again. Thus, memory is time-dependent, which is important in maintaining homeostasis and regulating many different biological processes.

#### Biochemical systems: regulating the cell cycle in *Xenopus laevis* egg extracts

Cells advancing through the cell cycle must make an irreversible commitment to mitosis, ensuring they do not revert to interphase before successfully segregating their chromosomes. A mathematical model of cell-cycle progression in cell-free egg extracts from frogs suggests that hysteresis in the molecular control system drives these irreversible transitions into and out of mitosis. Here, Cdc2 (Cyclin-dependent kinase 1 or CDK1) is responsible for mitotic entry and exit such that binding of cyclin B forms a complex called Maturation-Promoting Factor (MPF). The activation threshold for mitotic entry was found to be between 32 and 40 nM cyclin B in the frog extracts while the inactivation threshold for exiting mitosis was lower, between 16 and 24 nM cyclin B. The higher threshold for mitotic entry compared to the lower threshold for mitotic exit indicates hysteresis, a hallmark of history-dependent behavior in the system. Concentrations between 24 and 32 nM cyclin B demonstrated bistability, where the system could exist in either interphase or mitosis, depending on its prior state (history). Though, the cell cycle is not completely irreversible, the difference in thresholds is enough for growth and survival of the cells.

Hysteric thresholds in biological systems are not definite and can be recalibrated. For example, unreplicated DNA or chromosomes inhibits Cdc25 phosphatase and maintains Wee1 kinase activity. This prevents the activation of Cyclin B-Cdc2, effectively raising the threshold for mitotic entry. As a result, the cell delays the transition to mitosis until replication is complete, ensuring genomic integrity. Other instances may be DNA damage and unattached chromosomes during the spindle assembly checkpoint.

#### Biochemical systems: regulating the cell cycle in yeast

Biochemical systems can also show hysteresis-like output when slowly varying states that are not directly monitored are involved, as in the case of the cell cycle arrest in yeast exposed to mating pheromone. The proposed model is that α-factor, a yeast mating pheromone binds to its analog receptor on another yeast cell promoting transcription of Fus3 and promoting mating. Fus3 further promotes Far1 which inhibits Cln1/2, activators of the cell cycle. This is representative of a coherent feedforward loop that can modeled as a hysteresis curve.

Far1 transcription is the primary mechanism responsible for the hysteresis observed in cell-cycle reentry. The history of pheromone exposure influences the accumulation of Far1, which, in turn, determines the delay in cell-cycle reentry. Previous pulse experiments demonstrated that after exposure to high pheromone concentrations, cells enter a stabilized arrested state where reentry thresholds are elevated due to increased Far1-dependent inhibition of CDK activity. Even when pheromone levels drop to concentrations that would allow naive cells to reenter the cell cycle, pre-exposed cells take longer to resume proliferation. This delay reflects the history-dependent nature of hysteresis, where past exposure to high pheromone concentrations influences the current state. Hysteresis ensures that cells make robust and irreversible decisions about mating and proliferation in response to pheromone signals. It allows cells to "remember" high pheromone exposure, and this helps yeast cells adapt and stability their responses to environmental conditions, avoiding fast premature reentry into the cell cycle, the moment that pheromone signal dies down.

Additionally, the duration of cell cycle arrest depends not only on the final level of input Fus3, but also on the previously achieved Fus3 levels. This effect is achieved due to the slower time scales involved in the transcription of intermediate Far1, such that the total Far1 activity reaches its equilibrium value slowly, and for transient changes in Fus3 concentration, the response of the system depends on the Far1 concentration achieved with the transient value. Experiments in this type of hysteresis benefit from the ability to change the concentration of the inputs with time. The mechanisms are often elucidated by allowing independent control of the concentration of the key intermediate, for instance, by using an inducible promoter.

Biochemical systems can also show hysteresis-like output when slowly varying states that are not directly monitored are involved, as in the case of the cell cycle arrest in yeast exposed to mating pheromone. Here, the duration of cell cycle arrest depends not only on the final level of input Fus3, but also on the previously achieved Fus3 levels. This effect is achieved due to the slower time scales involved in the transcription of intermediate Far1, such that the total Far1 activity reaches its equilibrium value slowly, and for transient changes in Fus3 concentration, the response of the system depends on the Far1 concentration achieved with the transient value. Experiments in this type of hysteresis benefit from the ability to change the concentration of the inputs with time. The mechanisms are often elucidated by allowing independent control of the concentration of the key intermediate, for instance, by using an inducible promoter.

Darlington in his classic works on genetics discussed hysteresis of the chromosomes, by which he meant "failure of the external form of the chromosomes to respond immediately to the internal stresses due to changes in their molecular spiral", as they lie in a somewhat rigid medium in the limited space of the cell nucleus.

In developmental biology, cell type diversity is regulated by long range-acting signaling molecules called morphogens that pattern uniform pools of cells in a concentration- and time-dependent manner. The morphogen sonic hedgehog (Shh), for example, acts on limb bud and neural progenitors to induce expression of a set of homeodomain-containing transcription factors to subdivide these tissues into distinct domains. It has been shown that these tissues have a 'memory' of previous exposure to Shh. In neural tissue, this hysteresis is regulated by a homeodomain (HD) feedback circuit that amplifies Shh signaling. In this circuit, expression of Gli transcription factors, the executors of the Shh pathway, is suppressed. Glis are processed to repressor forms (GliR) in the absence of Shh, but in the presence of Shh, a proportion of Glis are maintained as full-length proteins allowed to translocate to the nucleus, where they act as activators (GliA) of transcription. By reducing Gli expression then, the HD transcription factors reduce the total amount of Gli (GliT), so a higher proportion of GliT can be stabilized as GliA for the same concentration of Shh.

### Immunology

There is some evidence that T cells exhibit hysteresis in that it takes a lower signal threshold to activate T cells that have been previously activated. Ras GTPase activation is required for downstream effector functions of activated T cells. Triggering of the T cell receptor induces high levels of Ras activation, which results in higher levels of GTP-bound (active) Ras at the cell surface. Since higher levels of active Ras have accumulated at the cell surface in T cells that have been previously stimulated by strong engagement of the T cell receptor, weaker subsequent T cell receptor signals received shortly afterwards will deliver the same level of activation due to the presence of higher levels of already activated Ras as compared to a naïve cell.

### Neuroscience

The property by which some neurons do not return to their basal conditions from a stimulated condition immediately after removal of the stimulus is an example of hysteresis.

### Neuropsychology

Neuropsychology, in exploring the neural correlates of consciousness, interfaces with neuroscience, although the complexity of the central nervous system is a challenge to its study (that is, its operation resists easy reduction). Context-dependent memory and state-dependent memory show hysteretic aspects of neurocognition.

### Respiratory physiology

Lung hysteresis is evident when observing the compliance of a lung on inspiration versus expiration. The difference in compliance (Δvolume/Δpressure) is due to the additional energy required to overcome surface tension forces during inspiration to recruit and inflate additional alveoli.

The transpulmonary pressure vs Volume curve of inhalation is different from the Pressure vs Volume curve of exhalation, the difference being described as hysteresis. Lung volume at any given pressure during inhalation is less than the lung volume at any given pressure during exhalation.

### Voice and speech physiology

A hysteresis effect may be observed in voicing onset versus offset. The threshold value of the subglottal pressure required to start the vocal fold vibration is lower than the threshold value at which the vibration stops, when other parameters are kept constant. In utterances of vowel-voiceless consonant-vowel sequences during speech, the intraoral pressure is lower at the voice onset of the second vowel compared to the voice offset of the first vowel, the oral airflow is lower, the transglottal pressure is larger and the glottal width is smaller.

### Ecology and epidemiology

Hysteresis is a commonly encountered phenomenon in ecology and epidemiology, where the observed equilibrium of a system can not be predicted solely based on environmental variables, but also requires knowledge of the system's past history. Notable examples include the theory of spruce budworm outbreaks and behavioral-effects on disease transmission.

It is commonly examined in relation to critical transitions between ecosystem or community types in which dominant competitors or entire landscapes can change in a largely irreversible fashion.

## In ocean and climate science

Complex ocean and climate models rely on the principle.

## In economics

Economic systems can exhibit hysteresis. For example, export performance is subject to strong hysteresis effects: because of the fixed transportation costs it may take a big push to start a country's exports, but once the transition is made, not much may be required to keep them going.

When some negative shock reduces employment in a company or industry, fewer employed workers then remain. As usually the employed workers have the power to set wages, their reduced number incentivizes them to bargain for higher wages when the economy again gets better instead of letting the wage be at the equilibrium wage level, where the supply and demand of workers would match. This causes hysteresis: the unemployment becomes permanently higher after negative shocks.

### Permanently higher unemployment

The idea of hysteresis is used extensively in the area of labor economics, specifically with reference to the unemployment rate. According to theories based on hysteresis, severe economic downturns (recession) and/or persistent stagnation (slow demand growth, usually after a recession) cause unemployed individuals to lose their job skills (commonly developed on the job) or to find that their skills have become obsolete, or become demotivated, disillusioned or depressed or lose job-seeking skills. In addition, employers may use time spent in unemployment as a screening tool, i.e., to weed out less desired employees in hiring decisions. Then, in times of an economic upturn, recovery, or "boom", the affected workers will not share in the prosperity, remaining unemployed for long periods (e.g., over 52 weeks). This makes unemployment "structural", i.e., extremely difficult to reduce simply by increasing the aggregate demand for products and labor without causing increased inflation. That is, it is possible that a ratchet effect in unemployment rates exists, so a short-term rise in unemployment rates tends to persist. For example, traditional anti-inflationary policy (the use of recession to fight inflation) leads to a permanently higher "natural" rate of unemployment (more scientifically known as the NAIRU). This occurs first because inflationary expectations are "sticky" downward due to wage and price rigidities (and so adapt slowly over time rather than being approximately correct as in theories of rational expectations) and second because labor markets do not clear instantly in response to unemployment.

The existence of hysteresis has been put forward as a possible explanation for the persistently high unemployment of many economies in the 1990s. Hysteresis has been invoked by Olivier Blanchard among others to explain the differences in long run unemployment rates between Europe and the United States. Labor market reform (usually meaning institutional change promoting more flexible wages, firing, and hiring) or strong demand-side economic growth may not therefore reduce this pool of long-term unemployed. Thus, specific targeted training programs are presented as a possible policy solution. However, the hysteresis hypothesis suggests such training programs are aided by persistently high demand for products (perhaps with incomes policies to avoid increased inflation), which reduces the transition costs out of unemployment and into paid employment easier.

## Models

Hysteretic models are mathematical models capable of simulating complex nonlinear behavior (hysteresis) characterizing mechanical systems and materials used in different fields of engineering, such as aerospace, civil, and mechanical engineering. Some examples of mechanical systems and materials having hysteretic behavior are:

- materials, such as steel, reinforced concrete, wood;
- structural elements, such as steel, reinforced concrete, or wood joints;
- devices, such as seismic isolators and dampers.

Each subject that involves hysteresis has models that are specific to the subject. In addition, there are hysteretic models that capture general features of many systems with hysteresis. An example is the Preisach model of hysteresis, which represents a hysteresis nonlinearity as a linear superposition of square loops called non-ideal relays. Many complex models of hysteresis arise from the simple parallel connection, or superposition, of elementary carriers of hysteresis termed hysterons.

A simple and intuitive parametric description of various hysteresis loops may be found in the Lapshin model. Along with the smooth loops, substitution of trapezoidal, triangular or rectangular pulses instead of the harmonic functions allows piecewise-linear hysteresis loops frequently used in discrete automatics to be built in the model. There are implementations of the hysteresis loop model in Mathcad and in R programming language.

The Bouc–Wen model of hysteresis is often used to describe non-linear hysteretic systems. It was introduced by Bouc and extended by Wen, who demonstrated its versatility by producing a variety of hysteretic patterns. This model is able to capture in analytical form, a range of shapes of hysteretic cycles which match the behaviour of a wide class of hysteretical systems; therefore, given its versability and mathematical tractability, the Bouc–Wen model has quickly gained popularity and has been extended and applied to a wide variety of engineering problems, including multi-degree-of-freedom (MDOF) systems, buildings, frames, bidirectional and torsional response of hysteretic systems two- and three-dimensional continua, and soil liquefaction among others. The Bouc–Wen model and its variants/extensions have been used in applications of structural control, in particular in the modeling of the behaviour of magnetorheological dampers, base isolation devices for buildings and other kinds of damping devices; it has also been used in the modelling and analysis of structures built of reinforced concrete, steel, masonry and timber.. The most important extension of Bouc-Wen Model was carried out by Baber and Noori and later by Noori and co-workers. That extended model, named, BWBN, can reproduce the complex shear pinching or slip-lock phenomenon that earlier model could not reproduce. The BWBN model has been widely used in a wide spectrum of applications and implementations are available in software such as OpenSees.

Hysteretic models may have a generalized displacement u as input variable and a generalized force f as output variable, or vice versa. In particular, in rate-independent hysteretic models, the output variable does not depend on the rate of variation of the input one.

Rate-independent hysteretic models can be classified into four different categories depending on the type of equation that needs to be solved to compute the output variable:

- algebraic models
- transcendental models
- differential models
- integral models

### List of models

Some notable hysteretic models are listed below, along with their associated fields.

- Bean's critical state model (magnetism)
- Bouc–Wen model (structural engineering)
- Ising model (magnetism)
- Jiles–Atherton model (magnetism)
- Novak–Tyson model (cell-cycle control)
- Preisach model (magnetism)
- Stoner–Wohlfarth model (magnetism)

## Energy

When hysteresis occurs with extensive and intensive variables, the work done on the system is the area under the hysteresis graph.
