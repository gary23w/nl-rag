---
title: "Simulation (part 1/2)"
source: https://en.wikipedia.org/wiki/Simulation
domain: discrete-event-simulation
license: CC-BY-SA-4.0
tags: discrete-event simulation, stochastic simulation, poisson point process, queueing theory
fetched: 2026-07-02
part: 1/2
---

# Simulation

A **simulation** is an imitative representation of a process or system that could exist in the real world. In this broad sense, simulation can often be used interchangeably with model. Sometimes a clear distinction between the two terms is made, in which simulations require the use of models; the model represents the key characteristics or behaviors of the selected system or process, whereas the simulation represents the evolution of the model over time. Another way to distinguish between the terms is to define simulation as experimentation with the help of a model. This definition includes time-independent simulations. Often, computers are used to execute the simulation.

Simulation is used in many contexts, such as simulation of technology for performance tuning or optimizing, safety engineering, testing, training, education, and video games. Simulation is also used with scientific modelling of natural systems or human systems to gain insight into their functioning, as in economics. Simulation can be used to show the eventual real effects of alternative conditions and courses of action. Simulation is also used when the real system cannot be engaged, because it may not be accessible, or it may be dangerous or unacceptable to engage, or it is being designed but not yet built, or it may simply not exist.

Key issues in modeling and simulation include the acquisition of valid sources of information about the relevant selection of key characteristics and behaviors used to build the model, the use of simplifying approximations and assumptions within the model, and the fidelity and validity of the simulation outcomes. Procedures and protocols for model verification and validation are an ongoing field of academic study, refinement, research and development in simulations technology or practice, particularly in the work of computer simulation.


## Classification and terminology

Historically, simulations used in different fields developed largely independently, but 20th-century studies of systems theory and cybernetics combined with the spreading use of computers across all those fields have led to some unification and a more systematic view of the concept.

*Physical simulation* refers to simulation in which physical objects are substituted for the real thing. These physical objects are often chosen because they are smaller or cheaper than the actual object or system. () Alternatively, *physical simulation* may refer to computer simulations considering selected laws of physics, as in multiphysics simulation. ()

*Interactive simulation* is a special kind of physical simulation, often referred to as a *human-in-the-loop* simulation, in which physical simulations include human operators, such as in a flight simulator, sailing simulator, or driving simulator.

*Continuous simulation* is a simulation based on continuous-time rather than discrete-time steps, using numerical integration of differential equations.

*Discrete-event simulation* studies systems whose states change their values only at discrete times. For example, a simulation of an epidemic could change the number of infected people at time instants when susceptible individuals get infected or when infected individuals recover.

*Stochastic simulation* is a simulation where some variable or process is subject to random variations and is projected using Monte Carlo techniques using pseudo-random numbers. Thus replicated runs with the same boundary conditions will each produce different results within a specific confidence band.

*Deterministic simulation* is a simulation which is not stochastic: thus the variables are regulated by deterministic algorithms. So replicated runs from the same boundary conditions always produce identical results.

*Hybrid simulation* (or combined simulation) corresponds to a mix between continuous and discrete event simulation and results in integrating numerically the differential equations between two sequential events numerically to reduce the number of discontinuities.

A *stand-alone simulation* is a simulation running on a single workstation by itself.

A **distributed simulation** is one which uses more than one computer simultaneously, to guarantee access from/to different resources (e.g. multi-users operating different systems, or distributed data sets); a classical example is Distributed Interactive Simulation (DIS).

*Parallel simulation* speeds up a simulation's execution by concurrently distributing its workload over multiple processors, as in high-performance computing.

*Interoperable simulation* is where multiple models, simulators (often defined as federates) interoperate locally, distributed over a network; a classical example is High-Level Architecture.

*Modeling and simulation as a service* is where simulation is accessed as a service over the web.

*Modeling, interoperable simulation and serious games* is where serious game approaches (e.g. game engines and engagement methods) are integrated with interoperable simulation.

*Simulation fidelity* is used to describe the accuracy of a simulation and how closely it imitates the real-life counterpart. Fidelity is broadly classified as one of three categories: low, medium, and high. Specific descriptions of fidelity levels are subject to interpretation, but the following generalizations can be made:

- Low – the minimum simulation required for a system to respond to accept inputs and provide outputs
- Medium – responds automatically to stimuli, with limited accuracy
- High – nearly indistinguishable or as close as possible to the real system

A *synthetic environment* is a computer simulation that can be included in human-in-the-loop simulations.

*Simulation in failure analysis* refers to simulation in which we create environment/conditions to identify the cause of equipment failure. This can be the best and fastest method to identify the failure cause.

### Data simulation

Data simulation creates artificial data to replicate the behavior of real-world data. The artificial data is generated using computer models or programs based on specific rules, patterns, or characteristics. This type of data is designed to imitate the operations of real systems, processes, or behaviors, enabling researchers and analysts to study and test scenarios without directly observing or collecting information from the real world.


## Computer simulation

A computer simulation (or "sim") is an attempt to model a real-life or hypothetical situation on a computer so that it can be studied to see how the system works. By changing variables in the simulation, predictions may be made about the behaviour of the system. It is a tool to virtually investigate the behaviour of the system under study.

Computer simulation has become a useful part of modeling many natural systems in physics, chemistry and biology, and human systems in economics and social science (e.g., computational sociology) as well as in engineering to gain insight into the operation of those systems. A good example of the usefulness of using computers to simulate can be found in the field of network traffic simulation. In such simulations, the model behaviour will change each simulation according to the set of initial parameters assumed for the environment.

Traditionally, the formal modeling of systems has been via a mathematical model, which attempts to find analytical solutions enabling the prediction of the behaviour of the system from a set of parameters and initial conditions. Computer simulation is often used as an adjunct to, or substitution for, modeling systems for which simple closed form analytic solutions are not possible. There are many different types of computer simulation, the common feature they all share is the attempt to generate a sample of representative scenarios for a model in which a complete enumeration of all possible states would be prohibitive or impossible.

Several software packages exist for running computer-based simulation modeling (e.g. Monte Carlo simulation, stochastic modeling, multimethod modeling) that makes all the modeling almost effortless.

Modern usage of the term "computer simulation" may encompass virtually any computer-based representation.

### Computer science

In computer science, simulation has some specialized meanings: Alan Turing used the term *simulation* to refer to what happens when a universal machine executes a state transition table (in modern terminology, a computer runs a program) that describes the state transitions, inputs and outputs of a subject discrete-state machine. The computer simulates the subject machine. Accordingly, in theoretical computer science the term *simulation* is a relation between state transition systems, useful in the study of operational semantics.

Less theoretically, an interesting application of computer simulation is to simulate computers using computers. In computer architecture, a type of simulator, typically called an *emulator*, is often used to execute a program that has to run on some inconvenient type of computer (for example, a newly designed computer that has not yet been built or an obsolete computer that is no longer available), or in a tightly controlled testing environment (see Computer architecture simulator and Platform virtualization). For example, simulators have been used to debug a microprogram or sometimes commercial application programs, before the program is downloaded to the target machine. Since the operation of the computer is simulated, all of the information about the computer's operation is directly available to the programmer, and the speed and execution of the simulation can be varied at will.

Simulators may also be used to interpret fault trees, or test VLSI logic designs before they are constructed. Symbolic simulation uses variables to stand for unknown values.

In the field of optimization, simulations of physical processes are often used in conjunction with evolutionary computation to optimize control strategies.


## Simulation in education and training

Simulation is extensively used for educational purposes. It is used for cases where it is prohibitively expensive or simply too dangerous to allow trainees to use the real equipment in the real world. In such situations they will spend time learning valuable lessons in a "safe" virtual environment yet living a lifelike experience (or at least it is the goal). Often the convenience is to permit mistakes during training for a safety-critical system.

Simulations in education are somewhat like training simulations. They focus on specific tasks. The term 'microworld' is used to refer to educational simulations which model some abstract concept rather than simulating a realistic object or environment, or in some cases model a real-world environment in a simplistic way so as to help a learner develop an understanding of the key concepts. Normally, a user can create some sort of construction within the microworld that will behave in a way consistent with the concepts being modeled. Seymour Papert was one of the first to advocate the value of microworlds, and the Logo programming environment developed by Papert is one of the most well-known microworlds.

Project management simulation is increasingly used to train students and professionals in the art and science of project management. Using simulation for project management training improves learning retention and enhances the learning process.

*Social simulations* may be used in social science classrooms to illustrate social and political processes in anthropology, economics, history, political science, or sociology courses, typically at the high school or university level. These may, for example, take the form of civics simulations, in which participants assume roles in a simulated society, or international relations simulations in which participants engage in negotiations, alliance formation, trade, diplomacy, and the use of force. Such simulations might be based on fictitious political systems, or be based on current or historical events. An example of the latter would be Barnard College's *Reacting to the Past* series of historical educational games. The National Science Foundation has also supported the creation of reacting games that address science and math education. In social media simulations, participants train communication with critics and other stakeholders in a private environment.

In recent years, there has been increasing use of social simulations for staff training in aid and development agencies. The Carana simulation, for example, was first developed by the United Nations Development Programme, and is now used in a very revised form by the World Bank for training staff to deal with fragile and conflict-affected countries.

Military uses for simulation often involve aircraft or armoured fighting vehicles, but can also target small arms and other weapon systems training. Specifically, virtual firearms ranges have become the norm in most military training processes and there is a significant amount of data to suggest this is a useful tool for armed professionals.


## Virtual simulation

A **virtual simulation** is a category of simulation that uses simulation equipment to create a **simulated world** for the user. Virtual simulations allow users to interact with a virtual world. Virtual worlds operate on platforms of integrated software and hardware components. In this manner, the system can accept input from the user (e.g., body tracking, voice/sound recognition, physical controllers) and produce output to the user (e.g., visual display, aural display, haptic display) . Virtual simulations use the aforementioned modes of interaction to produce a sense of immersion for the user.

### Virtual simulation input hardware

There is a wide variety of input hardware available to accept user input for virtual simulations. The following list briefly describes several of them:

- *Body tracking*: The motion capture method is often used to record the user's movements and translate the captured data into inputs for the virtual simulation. For example, if a user physically turns their head, the motion would be captured by the simulation hardware in some way and translated to a corresponding shift in view within the simulation.
  - Capture suits and/or gloves may be used to capture movements of users body parts. The systems may have sensors incorporated inside them to sense movements of different body parts (e.g., fingers). Alternatively, these systems may have exterior tracking devices or marks that can be detected by external ultrasound, optical receivers or electromagnetic sensors. Internal inertial sensors are also available on some systems. The units may transmit data either wirelessly or through cables.
  - Eye trackers can also be used to detect eye movements so that the system can determine precisely where a user is looking at any given instant.
- *Physical controllers*: Physical controllers provide input to the simulation only through direct manipulation by the user. In virtual simulations, tactile feedback from physical controllers is highly desirable in a number of simulation environments.
  - Omnidirectional treadmills can be used to capture the users locomotion as they walk or run.
  - High fidelity instrumentation such as instrument panels in virtual aircraft cockpits provides users with actual controls to raise the level of immersion. For example, pilots can use the actual global positioning system controls from the real device in a simulated cockpit to help them practice procedures with the actual device in the context of the integrated cockpit system.
- *Voice/sound recognition*: This form of interaction may be used either to interact with agents within the simulation (e.g., virtual people) or to manipulate objects in the simulation (e.g., information). Voice interaction presumably increases the level of immersion for the user.
  - Users may use headsets with boom microphones, lapel microphones or the room may be equipped with strategically located microphones.

#### Current research into user input systems

Research in future input systems holds a great deal of promise for virtual simulations. Systems such as brain–computer interfaces (BCIs) offer the ability to further increase the level of immersion for virtual simulation users. Lee, Keinrath, Scherer, Bischof, Pfurtscheller proved that naïve subjects could be trained to use a BCI to navigate a virtual apartment with relative ease. Using the BCI, the authors found that subjects were able to freely navigate the virtual environment with relatively minimal effort. It is possible that these types of systems will become standard input modalities in future virtual simulation systems.

### Virtual simulation output hardware

There is a wide variety of output hardware available to deliver stimuli to users in virtual simulations. The following list briefly describes several of them:

- *Visual display*: Visual displays provide the visual stimulus to the user.
  - Stationary displays can vary from a conventional desktop display to 360-degree wrap-around screens to stereo three-dimensional screens. Conventional desktop displays can vary in size from 15 to 60 inches (380 to 1,520 mm). Wrap around screens is typically used in what is known as a cave automatic virtual environment (CAVE). Stereo three-dimensional screens produce three-dimensional images either with or without special glasses—depending on the design.
  - Head-mounted displays (HMDs) have small displays that are mounted on headgear worn by the user. These systems are connected directly into the virtual simulation to provide the user with a more immersive experience. Weight, update rates and field of view are some of the key variables that differentiate HMDs. Naturally, heavier HMDs are undesirable as they cause fatigue over time. If the update rate is too slow, the system is unable to update the displays fast enough to correspond with a quick head turn by the user. Slower update rates tend to cause simulation sickness and disrupt the sense of immersion. Field of view or the angular extent of the world that is seen at a given moment field of view can vary from system to system and has been found to affect the user's sense of immersion.
- *Aural display*: Several different types of audio systems exist to help the user hear and localize sounds spatially. Special software can be used to produce 3D audio effects 3D audio to create the illusion that sound sources are placed within a defined three-dimensional space around the user.
  - Stationary conventional speaker systems may be used to provide dual or multi-channel surround sound. However, external speakers are not as effective as headphones in producing 3D audio effects.
  - Conventional headphones offer a portable alternative to stationary speakers. They also have the added advantages of masking real-world noise and facilitate more effective 3D audio sound effects.
- *Haptic display*: These displays provide a sense of touch to the user (haptic technology). This type of output is sometimes referred to as force feedback.
  - Tactile tile displays use different types of actuators such as inflatable bladders, vibrators, low-frequency sub-woofers, pin actuators and/or thermo-actuators to produce sensations for the user.
  - End effector displays can respond to users inputs with resistance and force. These systems are often used in medical applications for remote surgeries that employ robotic instruments.
- *Vestibular display*: These displays provide a sense of motion to the user (motion simulator). They often manifest as motion bases for virtual vehicle simulation such as driving simulators or flight simulators. Motion bases are fixed in place but use actuators to move the simulator in ways that can produce the sensations pitching, yawing or rolling. The simulators can also move in such a way as to produce a sense of acceleration on all axes (e.g., the motion base can produce the sensation of falling).


## Clinical healthcare simulators

**Clinical healthcare simulators** are increasingly being developed and deployed to teach therapeutic and diagnostic procedures as well as medical concepts and decision making to personnel in the health professions. Simulators have been developed for training procedures ranging from the basics such as blood draw, to laparoscopic surgery and trauma care. They are also important to help on prototyping new devices for biomedical engineering problems. Currently, simulators are applied to research and develop tools for new therapies, treatments and early diagnosis in medicine.

Many medical simulators involve a computer connected to a plastic simulation of the relevant anatomy. Sophisticated simulators of this type employ a life-size mannequin that responds to injected drugs and can be programmed to create simulations of life-threatening emergencies.

In other simulations, visual components of the procedure are reproduced by computer graphics techniques, while touch-based components are reproduced by haptic feedback devices combined with physical simulation routines computed in response to the user's actions. Medical simulations of this sort will often use 3D CT or MRI scans of patient data to enhance realism. Some medical simulations are developed to be widely distributed (such as web-enabled simulations and procedural simulations that can be viewed via standard web browsers) and can be interacted with using standard computer interfaces, such as the keyboard and mouse.

### Placebo

An important medical application of a simulator—although, perhaps, denoting a slightly different meaning of *simulator*—is the use of a placebo drug, a formulation that simulates the active drug in trials of drug efficacy.

### Improving patient safety

Patient safety is a concern in the medical industry. Patients have been known to suffer injuries and even death due to management error, and lack of using best standards of care and training. According to Building a National Agenda for Simulation-Based Medical Education (Eder-Van Hook, Jackie, 2004), "a health care provider's ability to react prudently in an unexpected situation is one of the most critical factors in creating a positive outcome in medical emergency, regardless of whether it occurs on the battlefield, freeway, or hospital emergency room." Eder-Van Hook (2004) also noted that medical errors kill up to 98,000 with an estimated cost between $37 and $50 million and $17 to $29 billion for preventable adverse events dollars per year.

Simulation is being used to study patient safety, as well as train medical professionals. Studying patient safety and safety interventions in healthcare is challenging, because there is a lack of experimental control (i.e., patient complexity, system/process variances) to see if an intervention made a meaningful difference (Groves & Manges, 2017). An example of innovative simulation to study patient safety is from nursing research. Groves et al. (2016) used a high-fidelity simulation to examine nursing safety-oriented behaviors during times such as change-of-shift report.

However, the value of simulation interventions to translating to clinical practice are is still debatable. As Nishisaki states, "there is good evidence that simulation training improves provider and team self-efficacy and competence on manikins. There is also good evidence that procedural simulation improves actual operational performance in clinical settings." However, there is a need to have improved evidence to show that crew resource management training through simulation. One of the largest challenges is showing that team simulation improves team operational performance at the bedside. Although evidence that simulation-based training actually improves patient outcome has been slow to accrue, today the ability of simulation to provide hands-on experience that translates to the operating room is no longer in doubt.

One of the largest factors that might impact the ability to have training impact the work of practitioners at the bedside is the ability to empower frontline staff (Stewart, Manges, Ward, 2015). Another example of an attempt to improve patient safety through the use of simulations training is patient care to deliver just-in-time service or/and just-in-place. This training consists of 20  minutes of simulated training just before workers report to shift. One study found that just in time training improved the transition to the bedside. The conclusion as reported in Nishisaki (2008) work, was that the simulation training improved resident participation in real cases; but did not sacrifice the quality of service. It could be therefore hypothesized that by increasing the number of highly trained residents through the use of simulation training, that the simulation training does, in fact, increase patient safety.

### History of simulation in healthcare

The first medical simulators were simple models of human patients.

Since antiquity, these representations in clay and stone were used to demonstrate clinical features of disease states and their effects on humans. Models have been found in many cultures and continents. These models have been used in some cultures (e.g., Chinese culture) as a "diagnostic" instrument, allowing women to consult male physicians while maintaining social laws of modesty. Models are used today to help students learn the anatomy of the musculoskeletal system and organ systems.

In 2002, the Society for Simulation in Healthcare (SSH) was formed to become a leader in international interprofessional advances the application of medical simulation in healthcare

The need for a "uniform mechanism to educate, evaluate, and certify simulation instructors for the health care profession" was recognized by McGaghie et al. in their critical review of simulation-based medical education research. In 2012 the SSH piloted two new certifications to provide recognition to educators in an effort to meet this need.

### Type of models

#### Active models

Active models that attempt to reproduce living anatomy or physiology are recent developments. The famous "Harvey" mannequin was developed at the University of Miami and is able to recreate many of the physical findings of the cardiology examination, including palpation, auscultation, and electrocardiography.

#### Interactive models

More recently, interactive models have been developed that respond to actions taken by a student or physician. Until recently, these simulations were two dimensional computer programs that acted more like a textbook than a patient. Computer simulations have the advantage of allowing a student to make judgments, and also to make errors. The process of iterative learning through assessment, evaluation, decision making, and error correction creates a much stronger learning environment than passive instruction.

#### Computer simulators

Simulators have been proposed as an ideal tool for assessment of students for clinical skills. For patients, "cybertherapy" can be used for sessions simulating traumatic experiences, from fear of heights to social anxiety.

Programmed patients and simulated clinical situations, including mock disaster drills, have been used extensively for education and evaluation. These "lifelike" simulations are expensive, and lack reproducibility. A fully functional "3Di" simulator would be the most specific tool available for teaching and measurement of clinical skills. Gaming platforms have been applied to create these virtual medical environments to create an interactive method for learning and application of information in a clinical context.

Immersive disease state simulations allow a doctor or HCP to experience what a disease actually feels like. Using sensors and transducers, symptomatic effects can be delivered to a participant, allowing them to experience the patient’s disease state.

Such a simulator meets the goals of an objective and standardized examination for clinical competence. This system is superior to examinations that use "standard patients" because it permits the quantitative measurement of competence, as well as reproducing the same objective findings.


## Simulation in entertainment

**Simulation in entertainment** encompasses many large and popular industries such as film, television, video games (including serious games) and rides in theme parks. Although modern simulation is thought to have its roots in training and the military, in the 20th century it also became a conduit for enterprises which were more hedonistic in nature.

### History of visual simulation in film and games

#### Early history (1940s and 1950s)

The first simulation game may have been created as early as 1947 by Thomas T. Goldsmith Jr. and Estle Ray Mann. This was a straightforward game that simulated a missile being fired at a target. The curve of the missile and its speed could be adjusted using several knobs. In 1958, a computer game called *Tennis for Two* was created by Willy Higginbotham which simulated a tennis game between two players who could both play at the same time using hand controls and was displayed on an oscilloscope. This was one of the first electronic video games to use a graphical display.

#### 1970s and early 1980s

Computer-generated imagery was used in the film to simulate objects as early as 1972 in *A Computer Animated Hand*, parts of which were shown on the big screen in the 1976 film *Futureworld*. This was followed by the "targeting computer" that young Skywalker turns off in the 1977 film *Star Wars*.

The film *Tron* (1982) was the first film to use computer-generated imagery for more than a couple of minutes.

Advances in technology in the 1980s caused 3D simulation to become more widely used and it began to appear in movies and in computer-based games such as Atari's *Battlezone* (1980) and Acornsoft's *Elite* (1984), one of the first wire-frame 3D graphics games for home computers.

#### Pre-virtual cinematography era (early 1980s to 1990s)

Advances in technology in the 1980s made the computer more affordable and more capable than they were in previous decades, which facilitated the rise of computer such as the Xbox gaming. The first video game consoles released in the 1970s and early 1980s fell prey to the industry crash in 1983, but in 1985, Nintendo released the Nintendo Entertainment System (NES) which became one of the best selling consoles in video game history. In the 1990s, computer games became widely popular with the release of such game as *The Sims* and *Command & Conquer* and the still increasing power of desktop computers. Today, computer simulation games such as *World of Warcraft* are played by millions of people around the world.

In 1993, the film *Jurassic Park* became the first popular film to use computer-generated graphics extensively, integrating the simulated dinosaurs almost seamlessly into live action scenes.

This event transformed the film industry; in 1995, the film *Toy Story* was the first film to use only computer-generated images and by the new millennium computer generated graphics were the leading choice for special effects in films.

#### Virtual cinematography (early 2000s–present)

The advent of virtual cinematography in the early 2000s has led to an explosion of movies that would have been impossible to shoot without it. Classic examples are the digital look-alikes of Neo, Smith and other characters in the *Matrix* sequels and the extensive use of physically impossible camera runs in *The Lord of the Rings* trilogy.

The terminal in the Pan Am (TV series) no longer existed during the filming of this 2011–2012 aired series, which was no problem as they created it in virtual cinematography using automated viewpoint finding and matching in conjunction with compositing real and simulated footage, which has been the bread and butter of the movie artist in and around film studios since the early 2000s.

Computer-generated imagery is "the application of the field of 3D computer graphics to special effects". This technology is used for visual effects because they are high in quality, controllable, and can create effects that would not be feasible using any other technology either because of cost, resources or safety. Computer-generated graphics can be seen in many live-action movies today, especially those of the action genre. Further, computer-generated imagery has almost completely supplanted hand-drawn animation in children's movies which are increasingly computer-generated only. Examples of movies that use computer-generated imagery include *Finding Nemo*, *300* and *Iron Man*.

### Examples of non-film entertainment simulation

#### Simulation games

Simulation games, as opposed to other genres of video and computer games, represent or simulate an environment accurately. Moreover, they represent the interactions between the playable characters and the environment realistically. These kinds of games are usually more complex in terms of gameplay. Simulation games have become incredibly popular among people of all ages. Popular simulation games include *SimCity* and *Tiger Woods PGA Tour*. There are also flight simulator and driving simulator games.

#### Theme park rides

Simulators have been used for entertainment since the Link Trainer in the 1930s. The first modern simulator ride to open at a theme park was Disney's Star Tours in 1987 soon followed by Universal's The Funtastic World of Hanna-Barbera in 1990 which was the first ride to be done entirely with computer graphics.

Simulator rides are the progeny of military training simulators and commercial simulators, but they are different in a fundamental way. While military training simulators react realistically to the input of the trainee in real time, ride simulators only feel like they move realistically and move according to prerecorded motion scripts. One of the first simulator rides, Star Tours, which cost $32 million, used a hydraulic motion based cabin. The movement was programmed by a joystick. Today's simulator rides, such as The Amazing Adventures of Spider-Man include elements to increase the amount of immersion experienced by the riders such as: 3D imagery, physical effects (spraying water or producing scents), and movement through an environment.


## Simulation and manufacturing

**Manufacturing simulation** represents one of the most important applications of simulation. This technique represents a valuable tool used by engineers when evaluating the effect of capital investment in equipment and physical facilities like factory plants, warehouses, and distribution centers. Simulation can be used to predict the performance of an existing or planned system and to compare alternative solutions for a particular design problem.

Another important goal of simulation in manufacturing systems is to quantify system performance. Common measures of system performance include the following:

- Throughput under average and peak loads
- System cycle time (how long it takes to produce one part)
- Use of resource, labor, and machines
- Bottlenecks and choke points
- Queuing at work locations
- Queuing and delays caused by material-handling devices and systems
- WIP storages needs
- Staffing requirements
- Effectiveness of scheduling systems
- Effectiveness of control systems
