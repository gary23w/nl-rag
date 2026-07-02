---
title: "Reliability engineering (part 1/2)"
source: https://en.wikipedia.org/wiki/Reliability_engineering
domain: service-level-objectives
license: CC-BY-SA-4.0
tags: service level objective, service level indicator, reliability target, availability threshold
fetched: 2026-07-02
part: 1/2
---

# Reliability engineering

**Reliability engineering** is a sub-discipline of systems engineering that emphasizes the ability of equipment to function without failure. Reliability is defined as the probability that a product, system, or service will perform its intended function adequately for a specified period of time; or will operate in a defined environment without failure. Reliability is closely related to availability, which is typically described as the ability of a component or system to function at a specified moment or interval of time.

The *reliability function* is theoretically defined as the probability of success. In practice, it is calculated using different techniques, and its value ranges between 0 and 1, where 0 indicates no probability of success while 1 indicates definite success. This probability is estimated from detailed (physics of failure) analysis, previous data sets, or through reliability testing and reliability modeling. Availability, testability, maintainability, and maintenance are often defined as a part of "reliability engineering" in reliability programs. Reliability often plays a vital role in the cost-effectiveness of overall systems.

Reliability engineering deals with the prediction, prevention, and management of high levels of "lifetime" engineering uncertainty and risks of failure. Although stochastic parameters define and affect reliability, reliability is not only achieved by mathematics and statistics. "Nearly all teaching and literature on the subject emphasize these aspects and ignore the reality that the ranges of uncertainty involved largely invalidate quantitative methods for prediction and measurement." For example, it is easy to represent "probability of failure" as a symbol or value in an equation, but it is almost impossible to predict its true magnitude in practice, which is massively multivariate, so having the equation for reliability does not begin to equal having an accurate predictive measurement of reliability.

Reliability engineering relates closely to quality engineering, safety engineering, and system safety, in that they use common methods for their analysis and may require input from each other. It can be said that a system must be reliably safe.

Reliability engineering focuses on the costs of failure caused by the system downtime, cost of spares, repair equipment, personnel, and cost of warranty claims.


## History

The word *reliability* can be traced back to 1816 and is first attested to the poet Samuel Taylor Coleridge. Before World War II the term was linked mostly to repeatability; a test (in any type of science) was considered "reliable" if the same results would be obtained repeatedly. In the 1920s, product improvement through the use of statistical process control was promoted by Dr. Walter A. Shewhart at Bell Labs, around the time that Waloddi Weibull was working on statistical models for fatigue. The development of reliability engineering was here on a parallel path with quality. The modern use of the word reliability was defined by the U.S. military in the 1940s, characterizing a product that would operate when expected and for a specified period.

In World War II, many reliability issues stemmed from the inherent unreliability of electronic equipment available at the time and from fatigue. In 1945, M.A. Miner published a seminal paper titled "Cumulative Damage in Fatigue" in an ASME journal. A main application for reliability engineering in the military was for the vacuum tube as used in radar systems and other electronics, for which reliability proved to be very problematic and costly. The IEEE formed the Reliability Society in 1948. In 1950, the United States Department of Defense formed a group called the "Advisory Group on the Reliability of Electronic Equipment" (AGREE) to investigate reliability methods for military equipment. This group recommended three main ways of working:

- Improve component reliability.
- Establish quality and reliability requirements for suppliers.
- Collect field data and find root causes of failures.

In the 1960s, more emphasis was given to reliability testing on component and system levels. The famous military standard MIL-STD-781 was created at that time. Around this period also the much-used predecessor to military handbook 217 was published by RCA and was used for the prediction of failure rates of electronic components. The emphasis on component reliability and empirical research (e.g. Mil Std 217) alone slowly decreased. More pragmatic approaches, as used in the consumer industries, were being used. In the 1980s, televisions were increasingly made up of solid-state semiconductors. Automobiles rapidly increased their use of semiconductors with a variety of microcomputers under the hood and in the dash. Large air conditioning systems developed electronic controllers, as did microwave ovens and a variety of other appliances. Communications systems began to adopt electronics to replace older mechanical switching systems. Bellcore issued the first consumer prediction methodology for telecommunications, and SAE developed a similar document SAE870050 for automotive applications. The nature of predictions evolved during the decade, and it became apparent that die complexity wasn't the only factor that determined failure rates for integrated circuits (ICs).

Kam Wong published a paper questioning the bathtub curve—see also reliability-centered maintenance. During this decade, the failure rate of many components dropped by a factor of 10. Software became important to the reliability of systems. By the 1990s, the pace of IC development was picking up. Wider use of stand-alone microcomputers was common, and the PC market helped keep IC densities following Moore's law and doubling about every 18 months. Reliability engineering was now changing as it moved towards understanding the physics of failure. Failure rates for components kept dropping, but system-level issues became more prominent. Systems thinking has become more and more important. For software, the CMM model (Capability Maturity Model) was developed, which gave a more qualitative approach to reliability. ISO 9000 added reliability measures to the design and development portion of certification.

The expansion of the World Wide Web created new challenges of security and trust. The older problem of too little reliable information available had now been replaced by too much information of questionable value. Consumer reliability problems could now be discussed online in real-time using data. New technologies such as micro-electromechanical systems (MEMS), handheld GPS, and hand-held devices that combine cell phones and computers all represent challenges to maintaining reliability. Product development time continued to shorten through this decade and what had been done in three years was being done in 18 months. This meant that reliability tools and tasks had to be more closely tied to the development process itself. In many ways, reliability has become part of everyday life and consumer expectations.


## Overview

Reliability is the probability of a product performing its intended function under specified operating conditions in a manner that meets or exceeds customer expectations.

### Objective

The objectives of reliability engineering, in decreasing order of priority, are:

1. To apply engineering knowledge and specialist techniques to prevent or to reduce the likelihood or frequency of failures.
2. To identify and correct the causes of failures that do occur despite the efforts to prevent them.
3. To determine ways of coping with failures that do occur, if their causes have not been corrected.
4. To apply methods for estimating the likely reliability of new designs, and for analysing reliability data.

The reason for the priority emphasis is that it is by far the most effective way of working, in terms of minimizing costs and generating reliable products. The primary skills that are required, therefore, are the ability to understand and anticipate the possible causes of failures, and knowledge of how to prevent them. It is also necessary to know the methods that can be used for analyzing designs and data.

### Scope and techniques

Reliability engineering for "complex systems" requires a different, more elaborate systems approach than for non-complex systems. Reliability engineering may in that case involve:

- System availability and mission readiness analysis and related reliability and maintenance requirement allocation
- Functional system failure analysis and derived requirements specification
- Inherent (system) design reliability analysis and derived requirements specification for both hardware and software design
- System diagnostics design
- Fault tolerant systems (e.g. by redundancy)
- Predictive and preventive maintenance (e.g. reliability-centered maintenance)
- Human factors / human interaction / human errors
- Manufacturing- and assembly-induced failures (effect on the detected "0-hour quality" and reliability)
- Maintenance-induced failures
- Transport-induced failures
- Storage-induced failures
- Use (load) studies, component stress analysis, and derived requirements specification
- Software (systematic) failures
- Failure / reliability testing (and derived requirements)
- Field failure monitoring and corrective actions
- Spare parts stocking (availability control)
- Technical documentation, caution and warning analysis
- Data and information acquisition/organisation (creation of a general reliability development hazard log and FRACAS system)
- Chaos engineering

Effective reliability engineering requires understanding of the basics of failure mechanisms for which experience, broad engineering skills and good knowledge from many different special fields of engineering are required, for example:

- Tribology
- Stress (mechanics)
- Fracture mechanics / fatigue
- Thermal engineering
- Fluid mechanics / shock-loading engineering
- Electrical engineering
- Chemical engineering (e.g. corrosion)
- Material science

### Definitions

Reliability may be defined in the following ways:

- The idea that an item is fit for a purpose
- The capacity of a designed, produced, or maintained item to perform as required
- The capacity of a population of designed, produced or maintained items to perform as required
- The resistance to failure of an item
- The probability of an item to perform a required function under stated conditions
- The durability of an object

### Basics of a reliability assessment

Many engineering techniques are used in reliability risk assessments, such as reliability block diagrams, hazard analysis, failure mode and effects analysis (FMEA), fault tree analysis (FTA), Reliability Centered Maintenance, (probabilistic) load and material stress and wear calculations, (probabilistic) fatigue and creep analysis, human error analysis, manufacturing defect analysis, reliability testing, etc. These analyses must be done properly and with much attention to detail to be effective. Because of the large number of reliability techniques, their expense, and the varying degrees of reliability required for different situations, most projects develop a reliability program plan to specify the reliability tasks (statement of work (SoW) requirements) that will be performed for that specific system.

Consistent with the creation of safety cases, for example per ARP4761, the goal of reliability assessments is to provide a robust set of qualitative and quantitative evidence that the use of a component or system will not be associated with unacceptable risk. The basic steps to take are to:

- Thoroughly identify relevant unreliability "hazards", e.g. potential conditions, events, human errors, failure modes, interactions, failure mechanisms, and root causes, by specific analysis or tests.
- Assess the associated system risk, by specific analysis or testing.
- Propose mitigation, e.g. requirements, design changes, detection logic, maintenance, and training, by which the risks may be lowered and controlled at an acceptable level.
- Determine the best mitigation and get agreement on final, acceptable risk levels, possibly based on cost/benefit analysis.

The risk here is the combination of probability and severity of the failure incident (scenario) occurring. The severity can be looked at from a system safety or a system availability point of view. Reliability for safety can be thought of as a very different focus from reliability for system availability. Availability and safety can exist in dynamic tension as keeping a system too available can be unsafe. Forcing an engineering system into a safe state too quickly can force false alarms that impede the availability of the system.

In a *de minimis* definition, the severity of failures includes the cost of spare parts, man-hours, logistics, damage (secondary failures), and downtime of machines which may cause production loss. A more complete definition of failure also can mean injury, dismemberment, and death of people within the system (witness mine accidents, industrial accidents, space shuttle failures) and the same to innocent bystanders (witness the citizenry of cities like Bhopal, Love Canal, Chernobyl, or Sendai, and other victims of the 2011 Tōhoku earthquake and tsunami)—in this case, reliability engineering becomes system safety. What is acceptable is determined by the managing authority or customers or the affected communities. Residual risk is the risk that is left over after all reliability activities have finished, and includes the unidentified risk—and is therefore not completely quantifiable.

The complexity of the technical systems such as improvements of design and materials, planned inspections, fool-proof design, and backup redundancy decreases risk and increases the cost. The risk can be decreased to ALARA (as low as reasonably achievable) or ALAPA (as low as practically achievable) levels.


## Reliability and availability program plan

Implementing a reliability program is not simply a software purchase; it is not just a checklist of items that must be completed that ensure one has reliable products and processes. A reliability program is a complex learning and knowledge-based system unique to one's products and processes. It is supported by leadership, built on the skills that one develops within a team, integrated into business processes, and executed by following proven standard work practices.

A reliability program plan is used to document exactly what "best practices" (tasks, methods, tools, analysis, and tests) are required for a particular (sub)system, as well as clarify customer requirements for reliability assessment. For large-scale complex systems, the reliability program plan should be a separate document. Resource determination for manpower and budgets for testing and other tasks is critical for a successful program. In general, the amount of work required for an effective program for complex systems is large.

A reliability program plan is essential for achieving high levels of reliability, testability, maintainability, and the resulting system availability, and is developed early during system development and refined over the system's life cycle. It specifies not only what the reliability engineer does, but also the tasks performed by other stakeholders. An effective reliability program plan must be approved by top program management, which is responsible for the allocation of sufficient resources for its implementation.

A reliability program plan may also be used to evaluate and improve the availability of a system by the strategy of focusing on increasing testability & maintainability and not on reliability. Improving maintainability is generally easier than improving reliability. Maintainability estimates (repair rates) are also generally more accurate. However, because the uncertainties in the reliability estimates are in most cases very large, they are likely to dominate the availability calculation (prediction uncertainty problem), even when maintainability levels are very high. When reliability is not under control, more complicated issues may arise, like manpower (maintainers/customer service capability) shortages, spare part availability, logistic delays, lack of repair facilities, extensive retrofit and complex configuration management costs, and others. The problem of unreliability may be increased also due to the "domino effect" of maintenance-induced failures after repairs. Focusing only on maintainability is therefore not enough. If failures are prevented, none of the other issues are of any importance, and therefore reliability is generally regarded as the most important part of availability. Reliability needs to be evaluated and improved related to both availability and the total cost of ownership (TCO) due to the cost of spare parts, maintenance man-hours, transport costs, storage costs, part obsolete risks, etc. But, as GM and Toyota have belatedly discovered, TCO also includes the downstream liability costs when reliability calculations have not sufficiently or accurately addressed customers' bodily risks. Often a trade-off is needed between the two. There might be a maximum ratio between availability and cost of ownership. The testability of a system should also be addressed in the plan, as this is the link between reliability and maintainability. The maintenance strategy can influence the reliability of a system (e.g., by preventive and/or predictive maintenance), although it can never bring it above the inherent reliability.

The reliability plan should clearly provide a strategy for availability control. Whether only availability or also cost of ownership is more important depends on the use of the system. For example, a system that is a critical link in a production system—e.g., a big oil platform—is normally allowed to have a very high cost of ownership if that cost translates to even a minor increase in availability, as the unavailability of the platform results in a massive loss of revenue which can easily exceed the high cost of ownership. A proper reliability plan should always address RAMT analysis in its total context. RAMT stands for reliability, availability, maintainability/maintenance, and testability in the context of the customer's needs.


## Reliability requirements

For any system, one of the first tasks of reliability engineering is to adequately specify the reliability and maintainability requirements allocated from the overall availability needs and, more importantly, derived from proper design failure analysis or preliminary prototype test results. Clear requirements (able to be designed to) should constrain the designers from designing particular unreliable items/constructions/interfaces/systems. Setting only availability, reliability, testability, or maintainability targets (e.g., max. failure rates) is not appropriate. This is a broad misunderstanding about Reliability Requirements Engineering. Reliability requirements address the system itself, including test and assessment requirements, and associated tasks and documentation. Reliability requirements are included in the appropriate system or subsystem requirements specifications, test plans, and contract statements. The creation of proper lower-level requirements is critical. The provision of only quantitative minimum targets (e.g., Mean Time Between Failure (MTBF) values or failure rates) is not sufficient for different reasons. One reason is that a full validation (related to correctness and verifiability in time) of a quantitative reliability allocation (requirement spec) on lower levels for complex systems can (often) not be made as a consequence of (1) the fact that the requirements are probabilistic, (2) the extremely high level of uncertainties involved for showing compliance with all these probabilistic requirements, and because (3) reliability is a function of time, and accurate estimates of a (probabilistic) reliability number per item are available only very late in the project, sometimes even after many years of in-service use. Compare this problem with the continuous (re-)balancing of, for example, lower-level-system mass requirements in the development of an aircraft, which is already often a big undertaking. Notice that in this case, masses do only differ in terms of only some %, are not a function of time, and the data is non-probabilistic and available already in CAD models. In the case of reliability, the levels of unreliability (failure rates) may change with factors of decades (multiples of 10) as a result of very minor deviations in design, process, or anything else. The information is often not available without huge uncertainties within the development phase. This makes this allocation problem almost impossible to do in a useful, practical, valid manner that does not result in massive over- or under-specification. A pragmatic approach is therefore needed—for example: the use of general levels/classes of quantitative requirements depending only on severity of failure effects. Also, the validation of results is a far more subjective task than any other type of requirement. (Quantitative) reliability parameters—in terms of MTBF—are by far the most uncertain design parameters in any design.

Furthermore, reliability design requirements should drive a (system or part) design to incorporate features that prevent failures from occurring, or limit consequences from failure in the first place. Not only would it aid in some predictions, this effort would keep from distracting the engineering effort into a kind of accounting work. A design requirement should be precise enough so that a designer can "design to" it and can also prove—through analysis or testing—that the requirement has been achieved, and, if possible, within some a stated confidence. Any type of reliability requirement should be detailed and could be derived from failure analysis (Finite-Element Stress and Fatigue analysis, Reliability Hazard Analysis, FTA, FMEA, Human Factor Analysis, Functional Hazard Analysis, etc.) or any type of reliability testing. Also, requirements are needed for verification tests (e.g., required overload stresses) and test time needed. To derive these requirements in an effective manner, a systems engineering-based risk assessment and mitigation logic should be used. Robust hazard log systems must be created that contain detailed information on why and how systems could or have failed. Requirements are to be derived and tracked in this way. These practical design requirements shall drive the design and not be used only for verification purposes. These requirements (often design constraints) are in this way derived from failure analysis or preliminary tests. Understanding of this difference compared to only purely quantitative (logistic) requirement specification (e.g., Failure Rate / MTBF target) is paramount in the development of successful (complex) systems.

The maintainability requirements address the costs of repairs as well as repair time. Testability (not to be confused with test requirements) requirements provide the link between reliability and maintainability and should address detectability of failure modes (on a particular system level), isolation levels, and the creation of diagnostics (procedures). As indicated above, reliability engineers should also address requirements for various reliability tasks and documentation during system development, testing, production, and operation. These requirements are generally specified in the contract statement of work and depend on how much leeway the customer wishes to provide to the contractor. Reliability tasks include various analyses, planning, and failure reporting. Task selection depends on the criticality of the system as well as cost. A safety-critical system may require a formal failure reporting and review process throughout development, whereas a non-critical system may rely on final test reports. The most common reliability program tasks are documented in reliability program standards, such as MIL-STD-785 and IEEE 1332. Failure reporting analysis and corrective action systems are a common approach for product/process reliability monitoring.


## Reliability culture / human errors / human factors

In practice, most failures can be traced back to some type of human error, for example in:

- Management decisions (e.g. in budgeting, timing, and required tasks)
- Systems Engineering: Use studies (load cases)
- Systems Engineering: Requirement analysis / setting
- Systems Engineering: Configuration control
- Assumptions
- Calculations / simulations / FEM analysis
- Design
- Design drawings
- Testing (e.g. incorrect load settings or failure measurement)
- Statistical analysis
- Manufacturing
- Quality control
- Maintenance
- Maintenance manuals
- Training
- Classifying and ordering of information
- Feedback of field information (e.g. incorrect or too vague)
- etc.

However, humans are also very good at detecting such failures, correcting them, and improvising when abnormal situations occur. Therefore, policies that completely rule out human actions in design and production processes to improve reliability may not be effective. Some tasks are better performed by humans and some are better performed by machines.

Furthermore, human errors in management; the organization of data and information; or the misuse or abuse of items, may also contribute to unreliability. This is the core reason why high levels of reliability for complex systems can only be achieved by following a robust systems engineering process with proper planning and execution of the validation and verification tasks. This also includes the careful organization of data and information sharing and creating a "reliability culture", in the same way, that having a "safety culture" is paramount in the development of safety-critical systems.


## Reliability prediction and improvement

Reliability prediction combines:

- creation of a proper reliability model (see further on this page)
- estimation (and justification) of input parameters for this model (e.g. failure rates for a particular failure mode or event and the mean time to repair the system for a particular failure)
- estimation of output reliability parameters at system or part level (i.e. system availability or frequency of a particular functional failure) The emphasis on quantification and target setting (e.g. MTBF) might imply there is a limit to achievable reliability, however, there is no inherent limit and development of higher reliability does not need to be more costly. In addition, they argue that prediction of reliability from historic data can be very misleading, with comparisons only valid for identical designs, products, manufacturing processes, and maintenance with identical operating loads and usage environments. Even minor changes in any of these could have major effects on reliability. Furthermore, the most unreliable and important items (i.e. the most interesting candidates for a reliability investigation) are most likely to be modified and re-engineered since historical data was gathered, making the standard (re-active or pro-active) statistical methods and processes used in e.g. medical or insurance industries less effective. Another argument is that to be able to accurately predict reliability by testing, the exact mechanisms of failure must be known and therefore – in most cases – could be prevented. Following the incorrect route of trying to quantify and solve a complex reliability engineering problem in terms of MTBF or probability using an-incorrect – for example, the re-active – approach is referred to by Barnard as "Playing the Numbers Game" and is regarded as bad practice.

For existing systems, it is arguable that any attempt by a responsible program to correct the root cause of discovered failures may render the initial MTBF estimate invalid, as new assumptions (themselves subject to high error levels) of the effect of this correction must be made. Another practical issue is the general unavailability of detailed failure data, with those available often featuring inconsistent filtering of failure (feedback) data, and ignoring statistical errors (which are very high for rare events like reliability related failures). Very clear guidelines must be present to count and compare failures related to different type of root-causes (e.g. manufacturing-, maintenance-, transport-, system-induced or inherent design failures). Comparing different types of causes may lead to incorrect estimations and incorrect business decisions about the focus of improvement.

To perform a proper quantitative reliability prediction for systems may be difficult and very expensive if done by testing. At the individual part-level, reliability results can often be obtained with comparatively high confidence, as testing of many sample parts might be possible using the available testing budget. However, these tests may lack validity at a system-level due to assumptions made at part-level testing. These authors emphasized the importance of initial part- or system-level testing until failure, and to learn from such failures to improve the system or part. The general conclusion is drawn that an accurate and absolute prediction – by either field-data comparison or testing – of reliability is in most cases not possible. An exception might be failures due to wear-out problems such as fatigue failures. In the introduction of MIL-STD-785 it is written that reliability prediction should be used with great caution, if not used solely for comparison in trade-off studies.

### Design for reliability

Design for Reliability (DfR) is a process that encompasses tools and procedures to ensure that a product meets its reliability requirements, under its use environment, for the duration of its lifetime. DfR is implemented in the design stage of a product to proactively improve product reliability. DfR is often used as part of an overall Design for Excellence (DfX) strategy.

#### Statistics-based approach (i.e. MTBF)

Reliability design begins with the development of a (system) model. Reliability and availability models use block diagrams and Fault Tree Analysis to provide a graphical means of evaluating the relationships between different parts of the system. These models may incorporate predictions based on failure rates taken from historical data. While the (input data) predictions are often not accurate in an absolute sense, they are valuable to assess relative differences in design alternatives. Maintainability parameters, for example Mean time to repair (MTTR), can also be used as inputs for such models.

The most important fundamental initiating causes and failure mechanisms are to be identified and analyzed with engineering tools. A diverse set of practical guidance as to performance and reliability should be provided to designers so that they can generate low-stressed designs and products that protect, or are protected against, damage and excessive wear. Proper validation of input loads (requirements) may be needed, in addition to verification for reliability "performance" by testing.

One of the most important design techniques is redundancy. This means that if one part of the system fails, there is an alternate success path, such as a backup system. The reason why this is the ultimate design choice is related to the fact that high-confidence reliability evidence for new parts or systems is often not available, or is extremely expensive to obtain. By combining redundancy, together with a high level of failure monitoring, and the avoidance of common cause failures; even a system with relatively poor single-channel (part) reliability, can be made highly reliable at a system level (up to mission critical reliability). No testing of reliability has to be required for this. In conjunction with redundancy, the use of dissimilar designs or manufacturing processes (e.g. via different suppliers of similar parts) for single independent channels, can provide less sensitivity to quality issues (e.g. early childhood failures at a single supplier), allowing very-high levels of reliability to be achieved at all moments of the development cycle (from early life to long-term). Redundancy can also be applied in systems engineering by double checking requirements, data, designs, calculations, software, and tests to overcome systematic failures.

Another effective way to deal with reliability issues is to perform analysis that predicts degradation, enabling the prevention of unscheduled downtime events / failures. RCM (Reliability Centered Maintenance) programs can be used for this.

#### Physics-of-failure-based approach

For electronic assemblies, there has been an increasing shift towards a different approach called physics of failure. This technique relies on understanding the physical static and dynamic failure mechanisms. It accounts for variation in load, strength, and stress that lead to failure with a high level of detail, made possible with the use of modern finite element method (FEM) software programs that can handle complex geometries and mechanisms such as creep, stress relaxation, fatigue, and probabilistic design (Monte Carlo Methods/DOE). The material or component can be re-designed to reduce the probability of failure and to make it more robust against such variations. Another common design technique is component derating: i.e. selecting components whose specifications significantly exceed the expected stress levels, such as using heavier gauge electrical wire than might normally be specified for the expected electric current.

#### Common tools and techniques

Many of the tasks, techniques, and analyses used in Reliability Engineering are specific to particular industries and applications, but can commonly include:

- Physics of failure (PoF)
- Built-in self-test (BIT or BIST) (testability analysis)
- Failure mode and effects analysis (FMEA)
- Reliability hazard analysis
- Reliability block-diagram analysis
- Dynamic reliability block-diagram analysis
- Fault tree analysis
- Root cause analysis
- Statistical engineering, design of experiments – e.g. on simulations / FEM models or with testing
- Sneak circuit analysis
- Accelerated testing
- Reliability growth analysis (re-active reliability)
- Weibull analysis (for testing or mainly "re-active" reliability)
- Hypertabastic survival models
- Thermal analysis by finite element analysis (FEA) and / or measurement
- Thermal induced, shock and vibration fatigue analysis by FEA and / or measurement
- Electromagnetic analysis
- Avoidance of single point of failure (SPOF)
- Functional analysis and functional failure analysis (e.g., function FMEA, FHA or FFA)
- Predictive and preventive maintenance: reliability centered maintenance (RCM) analysis
- Testability analysis
- Failure diagnostics analysis (normally also incorporated in FMEA)
- Human error analysis
- Operational hazard analysis
- Preventative/Planned Maintenance Optimization (PMO)
- Manual screening
- Integrated logistics support

Results from these methods are presented during reviews of part or system design, and logistics. Reliability is just one requirement among many for a complex part or system. Engineering trade-off studies are used to determine the optimum balance between reliability requirements and other constraints.

### The importance of language

Reliability engineers, whether using quantitative or qualitative methods to describe a failure or hazard, rely on language to pinpoint the risks and enable issues to be solved. The language used must help create an orderly description of the function/item/system and its complex surrounding as it relates to the failure of these functions/items/systems. Systems engineering is very much about finding the correct words to describe the problem (and related risks), so that they can be readily solved via engineering solutions. Jack Ring said that a systems engineer's job is to "language the project." (Ring et al. 2000) For part/system failures, reliability engineers should concentrate more on the "why and how", rather that predicting "when". Understanding "why" a failure has occurred (e.g. due to over-stressed components or manufacturing issues) is far more likely to lead to improvement in the designs and processes used than quantifying "when" a failure is likely to occur (e.g. via determining MTBF). To do this, first the reliability hazards relating to the part/system need to be classified and ordered (based on some form of qualitative and quantitative logic if possible) to allow for more efficient assessment and eventual improvement. This is partly done in pure language and proposition logic, but also based on experience with similar items. This can for example be seen in descriptions of events in fault tree analysis, FMEA analysis, and hazard (tracking) logs. In this sense language and proper grammar (part of qualitative analysis) plays an important role in reliability engineering, just like it does in safety engineering or in-general within systems engineering.

Correct use of language can also be key to identifying or reducing the risks of human error, which are often the root cause of many failures. This can include proper instructions in maintenance manuals, operation manuals, emergency procedures, and others to prevent systematic human errors that may result in system failures. These should be written by trained or experienced technical authors using so-called simplified English or Simplified Technical English, where words and structure are specifically chosen and created so as to reduce ambiguity or risk of confusion (e.g. an "replace the old part" could ambiguously refer to a swapping a worn-out part with a non-worn-out part, or replacing a part with one using a more recent and hopefully improved design).


## Reliability modeling

Reliability modeling is the process of predicting or understanding the reliability of a component or system prior to its implementation. Two types of analysis that are often used to model a complete system's availability behavior including effects from logistics issues like spare part provisioning, transport and manpower are fault tree analysis and reliability block diagrams. At a component level, the same types of analyses can be used together with others. The input for the models can come from many sources including testing; prior operational experience; field data; as well as data handbooks from similar or related industries. Regardless of source, all model input data must be used with great caution, as predictions are only valid in cases where the same product was used in the same context. As such, predictions are often only used to help compare alternatives.

For part level predictions, two separate fields of investigation are common:

- The physics of failure approach uses an understanding of physical failure mechanisms involved, such as mechanical crack propagation or chemical corrosion degradation or failure;
- The parts stress modelling approach is an empirical method for prediction based on counting the number and type of components of the system, and the stress they undergo during operation.

### Reliability theory

Reliability is defined as the probability that a device will perform its intended function during a specified period of time under stated conditions. Mathematically, this may be expressed as,

$R(t)=Pr\{T>t\}=\int _{t}^{\infty }f(x)\,dx\ \!$ ,

where $f(x)\!$ is the failure probability density function and t is the length of the period of time (which is assumed to start from time zero).

There are a few key elements of this definition:

1. Reliability is predicated on "intended function:" Generally, this is taken to mean operation without failure. However, even if no individual part of the system fails, but the system as a whole does not do what was intended, then it is still charged against the system reliability. The system requirements specification is the criterion against which reliability is measured.
2. Reliability applies to a specified period of time. In practical terms, this means that a system has a specified chance that it will operate without failure before time $T\!$ . Reliability engineering ensures that components and materials will meet the requirements during the specified time. Note that units other than time may sometimes be used (e.g. "a mission", "operation cycles").
3. Reliability is restricted to operation under stated (or explicitly defined) conditions. This constraint is necessary because it is impossible to design a system for unlimited conditions. A Mars rover will have different specified conditions than a family car. The operating environment must be addressed during design and testing. That same rover may be required to operate in varying conditions requiring additional scrutiny.
4. Two notable references on reliability theory and its mathematical and statistical foundations are Barlow, R. E. and Proschan, F. (1982) and Samaniego, F. J. (2007).

Often, knowledge of the statistical dependence between component failures is unknown or only partially constrained. When it is desired to model such incomplete knowledge, reliability theory allows for analyses that characterize ranges or bounds on system failure probabilities rather than unique distributions, particularly for small multi-component systems.

### Quantitative system reliability parameters—theory

Quantitative requirements are specified using reliability parameters. The most common reliability parameter is the mean time to failure (MTTF), which can also be specified as the failure rate (this is expressed as a frequency or conditional probability density function (PDF)) or the number of failures during a given period. These parameters may be useful for higher system levels and systems that are operated frequently (i.e. vehicles, machinery, and electronic equipment). Reliability increases as the MTTF increases. The MTTF is usually specified in hours, but can also be used with other units of measurement, such as miles or cycles. Using MTTF values on lower system levels can be very misleading, especially if they do not specify the associated Failures Modes and Mechanisms (The F in MTTF).

In other cases, reliability is specified as the probability of mission success. For example, reliability of a scheduled aircraft flight can be specified as a dimensionless probability or a percentage, as often used in system safety engineering.

A special case of mission success is the single-shot device or system. These are devices or systems that remain relatively dormant and only operate once. Examples include automobile airbags, thermal batteries and missiles. Single-shot reliability is specified as a probability of one-time success or is subsumed into a related parameter. Single-shot missile reliability may be specified as a requirement for the probability of a hit. For such systems, the probability of failure on demand (PFD) is the reliability measure – this is actually an "unavailability" number. The PFD is derived from failure rate (a frequency of occurrence) and mission time for non-repairable systems.

For repairable systems, it is obtained from failure rate, mean-time-to-repair (MTTR), and test interval. This measure may not be unique for a given system as this measure depends on the kind of demand. In addition to system level requirements, reliability requirements may be specified for critical subsystems. In most cases, reliability parameters are specified with appropriate statistical confidence intervals.
