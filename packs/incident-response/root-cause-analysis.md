---
title: "Root-cause analysis"
source: https://en.wikipedia.org/wiki/Root_cause_analysis
domain: incident-response
license: CC-BY-SA-4.0
tags: incident response, computer security incident, computer emergency response team, business continuity planning, root cause analysis
fetched: 2026-07-02
---

# Root-cause analysis

(Redirected from

Root cause analysis

)

In science and reliability engineering, **root-cause analysis** (**RCA**) is a method of problem solving used for identifying the root causes of faults or problems. It is widely used in IT operations, manufacturing, telecommunications, industrial process control, accident analysis (e.g., in aviation, rail transport, or nuclear plants), medical diagnosis, the healthcare industry (e.g., for epidemiology). Root-cause analysis is a form of inductive inference (first create a theory, or *root*, based on empirical evidence, or *causes*) and deductive inference (test the theory, i.e., the underlying causal mechanisms, with empirical data).

RCA can be decomposed into four steps:

1. Identify and describe the problem clearly
2. Establish a timeline from the normal situation until the problem occurrence
3. Distinguish between the root-cause and other causal factors (e.g., via event correlation)
4. Establish a causal graph between the root-cause and the problem.

RCA generally serves as input to a remediation process whereby corrective actions are taken to prevent the problem from recurring. The name of this process varies between application domains. According to ISO/IEC 31010, RCA may include these techniques: five whys, failure mode and effects analysis (FMEA), fault tree analysis, Ishikawa diagrams, and Pareto analysis.

## Definitions

There are essentially two ways of repairing faults and solving problems in science and engineering.

### Reactive management

Reactive management consists of reacting quickly after the problem occurs, by treating the symptoms. This type of management is implemented by reactive systems, self-adaptive systems, self-organized systems, and complex adaptive systems. The goal here is to react quickly and alleviate the effects of the problem as soon as possible.

### Proactive management

Proactive management, conversely, consists of preventing problems from occurring. Many techniques can be used for this purpose, ranging from good practices in design to analyzing in detail problems that have already occurred and taking actions to make sure they never recur. Speed is not as important here as the accuracy and precision of the diagnosis. The focus is on addressing the real cause of the problem rather than its effects.

Root-cause analysis is often used in proactive management to identify the root cause of a problem, that is, the factor that was the leading cause. It is customary to refer to the "root cause" in singular form, but one or several factors may constitute the *root cause(s)* of the problem under study.

A factor is considered the "root cause" of a problem if removing it prevents the problem from recurring. Conversely, a "causal factor" is a contributing action that affects an incident/event's outcome but is not the root cause. Although removing a causal factor can benefit an outcome, it does not prevent its recurrence with certainty.

A great way to look at the proactive/reactive picture is to consider the Bowtie Risk Assessment model. In the center of the model is the event or accident. To the left, are the anticipated hazards and the line of defenses put in place to prevent those hazards from causing events. The line of defense is the regulatory requirements, applicable procedures, physical barriers, and cyber barriers that are in place to manage operations and prevent events. A great way to use root-cause analysis is to proactively evaluate the effectiveness of those defenses by comparing actual performance against applicable requirements, identifying performance gaps, and then closing the gaps to strengthen those defenses. If an event occurs, then we are on the right side of the model, the reactive side where the emphasis is on identifying the root causes and mitigating the damage.

### Example

Imagine an investigation into a machine that stopped because it was overloaded and the fuse blew. Investigation shows that the machine was overloaded because it had a bearing that was not being sufficiently lubricated. The investigation proceeds further and finds that the automatic lubrication mechanism had a pump that was not pumping sufficiently, hence the lack of lubrication. Investigation of the pump shows that it has a worn shaft. Investigation of why the shaft was worn discovers that there is not an adequate mechanism to prevent metal scrap getting into the pump; this enabled scrap to get into the pump and damage it.

The apparent root cause of the problem is that metal scrap can contaminate the lubrication system. Fixing this problem ought to prevent the whole sequence of events from recurring. The *real* root cause could be a design issue if there is no filter to prevent the metal scrap getting into the system. Or if it has a filter that was blocked due to a lack of routine inspection, then the *real* root cause is a maintenance issue.

Compare this with an investigation that does not find the root cause: replacing the fuse, the bearing, or the lubrication pump will probably allow the machine to go back into operation for a while. However, there is a risk that the problem will simply recur until the root cause is dealt with.

In general terms, for the investigating team, such as quality and engineering personnel, vernacularly speaking, it commonly takes around 5 times asking "why".

The above example does not include cost/benefit analysis: does the cost of replacing one or more machines exceed the cost of downtime until the fuse is replaced? This situation is sometimes referred to as *the cure being worse than the disease*.

As an unrelated example of the conclusions that can be drawn in the absence of the cost/benefit analysis, consider the tradeoff between some claimed benefits of population decline: In the short term there will be fewer payers into pension/retirement systems; whereas halting the population decline will require higher taxes to cover the cost of building more schools. This can help explain the problem of the cure being worse than the disease.

Costs to consider go beyond finances when considering the personnel who operate the machinery. Ultimately, the goal is to prevent downtime; but more so prevent catastrophic injuries. Prevention begins with being proactive.

## General principles

Despite the different approaches among the various schools of root-cause analysis and the specifics of each application domain, RCA generally follows the same steps.

### Identification and description

Effective problem statements and event descriptions (as failures, for example) are helpful and usually required to ensure the execution of appropriate root-cause analyses. Problem statements are the North Star of the RCA as it keeps the team focused on what they are investigating and prevents them from going astray.

### Gathering, organizing and analyzing information

Most RCAs begin with a fact finding session to gather available information such as witness statements, the chronology of events and applicable requirements for the evolutions that were taking place at the time of the event. The information can be used to establish a sequence of events or timeline for the event, and to identify the line of the defenses that should have prevented the event (i.e. the administrative requirements, and physical and cyber barriers). Available databases should also be queried and analyzed (such as corrective action program and safety program databases), and data analysis tools such as Pareto charts, process maps, fault trees, and other tools that provide insights into performance gaps. Any number of data analysis tools can be brought to bear, including data analysis tools from Lean Six Sigma, statistical analysis tools, and others such as hierarchical clustering and data-mining solutions (such as graph-theory-based data mining). Another consists in comparing the situation under investigation with past situations stored in case libraries, using case-based reasoning tools and can include change analysis, comparative timeline analysis and task analysis.

### Analysis of defenses

After identifying the defenses in place that should have prevented the event or accident, an analysis of defenses (traditionally called Barrier Analysis) can be conducted in every case, including non-RCA investigations. One method is to list the defenses on chart or a virtual white board, then look at the information and data that was gathered for evidence of the effectiveness of that defense to look for deficiencies or gaps in performance where the administrative requirements were not met, or where the physical or cyber barriers were bypassed. These initial gaps in performance are merely symptoms of deeper-seated causes. These symptomatic performance gaps are used to develop lines of inquiry questions as outlined below, to pursue the symptoms back to their points of origin (i.e. the root causes) using cause-and-effect analysis.

### Generating focused, unbiased lines of inquiry questions

After gathering available information, organizing it into charts with timelines and other data, after analyzing available data, and after conducting an analysis of defenses, those insights are used to generate questions. These questions become lines of inquiry for cause-and-effect analysis. The questions must be unbiased, and to prevent any bias from the RCA team from tainting the investigation, questions should be tied to a specific defense, or to a specific insight from the data analysis (e.g., Pareto charts, process maps, fault trees, control charts) and other tools that provide insights into performance gaps. There should not be any curiosity questions, questions that reflect "confirmation bias" (i.e. asking a leading question so they answer what the RCA team thinks are the causes), or questions that are accusatory in nature that will cause those helping the investigation to close down and withdraw.

### Cause-and-effect analysis

Once a robust set of lines of inquiry questions has been developed from the factual evidence collected, the applicable requirements, and an analysis of the available data, those questions can be taken to the organization's subject matter experts. This begins the process of cause-and-effect analysis. Once a question is posed to the affected organization, their answer is used to pose a follow-up Socratic questions. Socratic questions keep the investigation flowing down to the next deeper causal factors until the organization runs out of answers, or the last causal factor is beyond the organization's control. There are many skills involved in conducting an effective cause-and-effect analysis, including facilitation skills, communication skills, and Socratic questioning. When conducted properly, this will take the RCA down to the deepest-seated root causes. A word of caution: Ishikawa or the Fishbone Diagram, and the 5-Whys methods, are not rigorous enough for conducting a root-cause analysis. The Fishbone is from the 1940s and the 5-Whys is from the 1930, and there are much more advanced methods available. Look for methods that were developed in this century (the year 2000 and later), as they are more likely to account for the new dynamics of the modern sociotechnical work environments.

### Charting the results of the RCA

The best way to chart the results of an RCA investigation is to start populating the final chart from the start. This process has become much easier with the advent of virtual whiteboards. In a single virtual whiteboard, the timelines, lines of defenses, data analysis, lines of inquiry questions, cause-and-effect analysis, root causes, and corrective action plan can be displayed.

### Corrective actions to prevent recurrence

From a management perspective, the RCA effort is not complete without a comprehensive corrective action plan to address the root causes, the contributing factors, and the "Extent of the Causes." The corrective action plan should be developed by the issue owners and does not require participation by the RCA team, although the team is an excellent source of guidance for the issue owners. The Extent of Cause reviews are conducted to determine the extent of the damage or impact that the root causes and contributing factors had on humans, equipment, or facilities. Extent of Cause reviews are an Achilles heel in the vast majority of organizations and a primary reason why RCAs and corrective action plans fail to prevent recurrence. Also, care must be taken to avoid corrective action plans that simply add more administrative requirements and more training to the organization. To avoid this, use the Hierarchy of Hazard Controls and Lean Mistake Proofing as guidelines for developing effective corrective actions that have a much higher likelihood of preventing recurrence.

### Effectiveness reviews

After a pre-determined period after the implementation of the corrective action plan, an effectiveness review is scheduled to evaluate the effectiveness of those corrective actions. This requires specifying a set of metrics or indicators that will be monitored prior to and after the corrective actions are implemented, so their impact can be measured. If the desired results are not achieved, which in most cases is a significant reduction in the magnitude or frequency of the event or problem, then the RCA must be reopened as it was not effective.

To be effective, root-cause analysis must be performed systematically. The process enables the chance to not miss any other important details. A team effort is typically required, and ideally all persons involved should arrive at the same conclusion. In aircraft accident analyses, for example, the conclusions of the investigation and the root causes that are identified must be backed up by documented evidence.

### Transition to corrective actions

The goal of RCA is to identify the root cause of the problem with the intent to stop the problem from recurring or worsening. The next step is to trigger long-term corrective actions to address the root cause identified during RCA, and make sure that the problem does not resurface. Correcting a problem is not formally part of RCA, however; these are different steps in a problem-solving process known as fault management in IT and telecommunications, repair in engineering, remediation in aviation, environmental remediation in ecology, therapy in medicine, etc.

## Application domains

Root-cause analysis is used in many application domains. RCA is specifically called out in the United States Code of Federal Regulations in many of the Titles. For example:

1. TITLE 10 - ENERGY >>> 10CFR Part 50, Appendix B, Criterion XVI, "Corrective Actions" (also adopted by NQA-1)
  - “Measures shall be established to assure that conditions adverse to quality such as failures, malfunctions, deficiencies, defective material and equipment, and non-conformances are promptly identified and corrected.
  - In the case of significant conditions adverse to quality, the measures shall assure that the cause of the condition is determined, and corrective action taken to prevent recurrence.”
2. TITLE 14 - AERONAUTICS AND SPACE >>> 14 CFR Chapter III, Subchapter C, Part 437, Subpart C, §437.73   Anomaly recording, reporting and implementation of corrective actions.
  1. A permittee must record each anomaly that affects a safety-critical system, subsystem, process, facility, or support equipment.
  2. A permittee must identify all root causes of each anomaly and implement all corrective actions for each anomaly.
3. TITLE 21 - FOOD AND DRUG >>> 21 CFR Subpart J: 21CFR820.100(a) – Corr./Preventive Action: (A) Each manufacturer shall establish and maintain procedures for implementing corrective and preventive action.  The procedures shall include requirements for:
  1. Investigating the cause of nonconformities relating to product, processes, and the quality system;
  2. Identifying the action(s) needed to correct and prevent recurrence of non- conforming product and other quality problems;
  3. Verifying or validating the corrective and preventive action to ensure that such action is effective and does not adversely affect the finished device;
4. TITLE 42 - PUBLIC HEALTH >>> 42 CFR PART 488, SURVEY, CERTIFICATION, AND ENFORCEMENT PROCEDURES > Subpart E—Survey and Certification of Long-Term Care Facilities
  1. §488.61   Special procedures for approval and re-approval of organ transplant programs.
  2. ...Root Cause Analysis for patient deaths and graft failures, including factors the program has identified as likely causal or contributing factors for patient deaths and graft failures;

### Manufacturing and industrial process control

The example above illustrates how RCA can be used in manufacturing. RCA is also routinely used in industrial process control, e.g. to control the production of chemicals (quality control).

RCA is also used for failure analysis in engineering and maintenance.

### IT and telecommunications

Root-cause analysis is frequently used in IT and telecommunications to detect the root causes of serious problems. For example, in the ITIL service management framework, the goal of incident management is to resume a faulty IT service as soon as possible (reactive management), whereas problem management deals with solving recurring problems for good by addressing their root causes (proactive management).

Another example is the computer security incident management process, where root-cause analysis is often used to investigate security breaches.

RCA is also used in conjunction with business activity monitoring and complex event processing to analyze faults in business processes.

Its use in the IT industry cannot always be compared to its use in safety critical industries, since in normality the use of RCA in IT industry is *not* supported by pre-existing fault trees or other design specs. Instead a mixture of debugging, event based detection and monitoring systems (where the services are individually modelled) is normally supporting the analysis. Training and supporting tools like simulation or different in-depth runbooks for all expected scenarios do not exist, instead they are created after the fact based on issues seen as 'worthy'. As a result the analysis is often limited to those things that have monitoring/observation interfaces and not the actual planned/seen function with focus on verification of inputs and outputs. Hence, the saying "there is no root cause" has become common in the IT industry.

### Health and safety

In the domains of health and safety, RCA is routinely used in medicine (diagnosis) and epidemiology (e.g., to identify the source of an infectious disease), where causal inference methods often require both clinical and statistical expertise to make sense of the complexities of the processes.

RCA is used in environmental science (e.g., to analyze environmental disasters), accident analysis (aviation and rail industry), and occupational safety and health. In the manufacture of medical devices, pharmaceuticals, food, and dietary supplements, root-cause analysis is a regulatory requirement.

### Systems analysis

RCA is also used in change management, risk management, and systems analysis.

## Challenges

Without delving in the idiosyncrasies of specific problems, several general conditions can make RCA more difficult than it may appear at first sight.

First, important information is often missing because it is generally not possible, in practice, to monitor everything and store all monitoring data for a long time.

Second, gathering data and evidence, and classifying them along a timeline of events to the final problem, can be nontrivial. In telecommunications, for instance, distributed monitoring systems typically manage between a million and a billion events per day. Finding a few relevant events in such a mass of irrelevant events is asking to find the proverbial needle in a haystack.

Third, there may be more than one root cause for a given problem, and this multiplicity can make the causal graph very difficult to establish.

Fourth, causal graphs often have many levels, and root-cause analysis terminates at a level that is "root" to the eyes of the investigator. Looking again at the example above in industrial process control, a deeper investigation could reveal that the maintenance procedures at the plant included periodic inspection of the lubrication subsystem every two years, while the current lubrication subsystem vendor's product specified a 6-month period. Switching vendors may have been due to management's desire to save money, and a failure to consult with engineering staff on the implication of the change on maintenance procedures. Thus, while the "root cause" shown above may have prevented the quoted recurrence, it would not have prevented other  – perhaps more severe – failures affecting other machines.
