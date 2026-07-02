---
title: "Reliability engineering (part 2/2)"
source: https://en.wikipedia.org/wiki/Reliability_engineering
domain: aws-well-architected
license: CC-BY-SA-4.0
tags: well-architected framework, cloud architecture, reliability engineering, high availability
fetched: 2026-07-02
part: 2/2
---

## Reliability testing

The purpose of **reliability testing** or **reliability verification** is to discover potential problems with the design as early as possible and, ultimately, provide confidence that the system meets its reliability requirements. The reliability of the product in all environments such as expected use, transportation, or storage during the specified lifespan should be considered. It is to expose the product to natural or artificial environmental conditions to undergo its action to evaluate the performance of the product under the environmental conditions of actual use, transportation, and storage, and to analyze and study the degree of influence of environmental factors and their mechanism of action. Through the use of various environmental test equipment to simulate the high temperature, low temperature, and high humidity, and temperature changes in the climate environment, to accelerate the reaction of the product in the use environment, to verify whether it reaches the expected quality in R&D, design, and manufacturing.

Reliability verification is also called reliability testing, which refers to the use of modeling, statistics, and other methods to evaluate the reliability of the product based on the product's life span and expected performance. Most product on the market requires reliability testing, such as automotive, integrated circuit, heavy machinery used to mine nature resources, Aircraft auto software.

Reliability testing may be performed at several levels and there are different types of testing. Complex systems may be tested at component, circuit board, unit, assembly, subsystem and system levels. (The test level nomenclature varies among applications.) For example, performing environmental stress screening tests at lower levels, such as piece parts or small assemblies, catches problems before they cause failures at higher levels. Testing proceeds during each level of integration through full-up system testing, developmental testing, and operational testing, thereby reducing program risk. However, testing does not mitigate unreliability risk.

With each test both statistical type I and type II errors could be made, depending on sample size, test time, assumptions and the needed discrimination ratio. There is risk of incorrectly rejecting a good design (type I error) and the risk of incorrectly accepting a bad design (type II error).

It is not always feasible to test all system requirements. Some systems are prohibitively expensive to test; some failure modes may take years to observe; some complex interactions result in a huge number of possible test cases; and some tests require the use of limited test ranges or other resources. In such cases, different approaches to testing can be used, such as (highly) accelerated life testing, design of experiments, and simulations.

The desired level of statistical confidence also plays a role in reliability testing. Statistical confidence is increased by increasing either the test time or the number of items tested. Reliability test plans are designed to achieve the specified reliability at the specified confidence level with the minimum number of test units and test time. Different test plans result in different levels of risk to the producer and consumer. The desired reliability, statistical confidence, and risk levels for each side influence the ultimate test plan. The customer and developer should agree in advance on how reliability requirements will be tested.

A key aspect of reliability testing is to define "failure". Although this may seem obvious, there are many situations where it is not clear whether a failure is really the fault of the system. Variations in test conditions, operator differences, weather and unexpected situations create differences between the customer and the system developer. One strategy to address this issue is to use a scoring conference process. A scoring conference includes representatives from the customer, the developer, the test organization, the reliability organization, and sometimes independent observers. The scoring conference process is defined in the statement of work. Each test case is considered by the group and "scored" as a success or failure. This scoring is the official result used by the reliability engineer.

As part of the requirements phase, the reliability engineer develops a test strategy with the customer. The test strategy makes trade-offs between the needs of the reliability organization, which wants as much data as possible, and constraints such as cost, schedule and available resources. Test plans and procedures are developed for each reliability test, and results are documented.

Reliability testing is common in the Photonics industry. Examples of reliability tests of lasers are life test and burn-in. These tests consist of the highly accelerated aging, under controlled conditions, of a group of lasers. The data collected from these life tests are used to predict laser life expectancy under the intended operating characteristics.

### Reliability test requirements

There are many criteria to test depends on the product or process that are testing on, and mainly, there are five components that are most common:

1. Product life span
2. Intended function
3. Operating Condition
4. Probability of Performance
5. User exceptions

The product life span can be split into four different for analysis. Useful life is the estimated economic life of the product, which is defined as the time can be used before the cost of repair do not justify the continue use to the product. Warranty life is the product should perform the function within the specified time period. Design life is where during the design of the product, designer take into consideration on the life time of competitive product and customer desire and ensure that the product do not result in customer dissatisfaction.

Reliability test requirements can follow from any analysis for which the first estimate of failure probability, failure mode or effect needs to be justified. Evidence can be generated with some level of confidence by testing. With software-based systems, the probability is a mix of software and hardware-based failures. Testing reliability requirements is problematic for several reasons. A single test is in most cases insufficient to generate enough statistical data. Multiple tests or long-duration tests are usually very expensive. Some tests are simply impractical, and environmental conditions can be hard to predict over a systems life-cycle.

Reliability engineering is used to design a realistic and affordable test program that provides empirical evidence that the system meets its reliability requirements. Statistical confidence levels are used to address some of these concerns. A certain parameter is expressed along with a corresponding confidence level: for example, an MTBF of 1000 hours at 90% confidence level. From this specification, the reliability engineer can, for example, design a test with explicit criteria for the number of hours and number of failures until the requirement is met or failed. Different sorts of tests are possible.

The combination of required reliability level and required confidence level greatly affects the development cost and the risk to both the customer and producer. Care is needed to select the best combination of requirements—e.g. cost-effectiveness. Reliability testing may be performed at various levels, such as component, subsystem and system. Also, many factors must be addressed during testing and operation, such as extreme temperature and humidity, shock, vibration, or other environmental factors (like loss of signal, cooling or power; or other catastrophes such as fire, floods, excessive heat, physical or security violations or other myriad forms of damage or degradation). For systems that must last many years, accelerated life tests may be needed.

### Testing method

A systematic approach to reliability testing is to, first, determine reliability goal, then do tests that are linked to performance and determine the reliability of the product. A reliability verification test in modern industries should clearly determine how they relate to the product's overall reliability performance and how individual tests impact the warranty cost and customer satisfaction.

### Accelerated testing

The purpose of accelerated life testing (ALT test) is to induce field failure in the laboratory at a much faster rate by providing a harsher, but nonetheless representative, environment. In such a test, the product is expected to fail in the lab just as it would have failed in the field—but in much less time. The main objective of an accelerated test is either of the following:

- To discover failure modes
- To predict the normal field life from the high stress lab life

An accelerated testing program can be broken down into the following steps:

- Define objective and scope of the test
- Collect required information about the product
- Identify the stress(es)
- Determine level of stress(es)
- Conduct the accelerated test and analyze the collected data.

Common ways to determine a life stress relationship are:

- Arrhenius model
- Eyring model
- Inverse power law model
- Temperature–humidity model
- Temperature non-thermal model


## Software reliability

Software reliability is a special aspect of reliability engineering. It focuses on foundations and techniques to make software more reliable, i.e., resilient to faults. System reliability, by definition, includes all parts of the system, including hardware, software, supporting infrastructure (including critical external interfaces), operators and procedures. Traditionally, reliability engineering focuses on critical hardware parts of the system. Since the widespread use of digital integrated circuit technology, software has become an increasingly critical part of most electronics and, hence, nearly all present day systems. Therefore, software reliability has gained prominence within the field of system reliability.

There are significant differences, however, in how software and hardware behave. Most hardware unreliability is the result of a component or material failure that results in the system not performing its intended function. Repairing or replacing the hardware component restores the system to its original operating state. However, software does not fail in the same sense that hardware fails. Instead, software unreliability is the result of unanticipated results of software operations. Even relatively small software programs can have astronomically large combinations of inputs and states that are infeasible to exhaustively test. Restoring software to its original state only works until the same combination of inputs and states results in the same unintended result. Software reliability engineering must take this into account.

Despite this difference in the source of failure between software and hardware, several software reliability models based on statistics have been proposed to quantify what we experience with software: the longer software is run, the higher the probability that it will eventually be used in an untested manner and exhibit a latent defect that results in a failure (Shooman 1987), (Musa 2005), (Denney 2005).

As with hardware, software reliability depends on good requirements, design and implementation. Software reliability engineering relies heavily on a disciplined software engineering process to anticipate and design against unintended consequences. There is more overlap between software quality engineering and software reliability engineering than between hardware quality and reliability. A good software development plan is a key aspect of the software reliability program. The software development plan describes the design and coding standards, peer reviews, unit tests, configuration management, software metrics and software models to be used during software development.

In modern distributed and microservices-based systems, reliability considerations increasingly extend beyond component-level correctness to include the behavior of applications at the business-logic level. While traditional software reliability engineering and Site Reliability Engineering (SRE) focus on system-level indicators such as availability and latency, some sources and industry practitioners refer to this application-focused perspective as *application reliability engineering* (ARE) This perspective emphasizes end-to-end user transactions and the correctness of business workflows, including metrics such as transaction success rates, data consistency, and workflow completion across multiple interacting services. It addresses scenarios in which individual system components may appear operational, while failures arise from service interactions or logic errors, potentially leading to degraded user experience or incorrect outcomes.

Practices associated with application-level reliability include end-to-end observability, synthetic transaction testing, and validation of business-critical processes, complementing traditional infrastructure-focused reliability methods.

A common reliability metric is the number of software faults per line of code (FLOC), usually expressed as faults per thousand lines of code. This metric, along with software execution time, is key to most software reliability models and estimates. The theory is that the software reliability increases as the number of faults (or fault density) decreases. Establishing a direct connection between fault density and mean-time-between-failure is difficult, however, because of the way software faults are distributed in the code, their severity, and the probability of the combination of inputs necessary to encounter the fault. Nevertheless, fault density serves as a useful indicator for the reliability engineer. Other software metrics, such as complexity, are also used. This metric remains controversial, since changes in software development and verification practices can have dramatic impact on overall defect rates.

Software testing is an important aspect of software reliability. Even the best software development process results in some software faults that are nearly undetectable until tested. Software is tested at several levels, starting with individual units, through integration and full-up system testing. All phases of testing, software faults are discovered, corrected, and re-tested. Reliability estimates are updated based on the fault density and other metrics. At a system level, mean-time-between-failure data can be collected and used to estimate reliability. Unlike hardware, performing exactly the same test on exactly the same software configuration does not provide increased statistical confidence. Instead, software reliability uses different metrics, such as code coverage.

The Software Engineering Institute's capability maturity model is a common means of assessing the overall software development process for reliability and quality purposes.


## Structural reliability

Structural reliability or the reliability of structures is the application of reliability theory to the behavior of structures. It is used in both the design and maintenance of different types of structures including concrete and steel structures. In structural reliability studies both loads and resistances are modeled as probabilistic variables. Using this approach the probability of failure of a structure is calculated.


## Comparison to safety engineering

Reliability for safety and reliability for availability are often closely related. Lost availability of an engineering system can cost money. If a subway system is unavailable the subway operator will lose money for each hour the system is down. The subway operator will lose more money if safety is compromised. The definition of reliability is tied to a probability of not encountering a failure. A failure can cause loss of safety, loss of availability or both. It is undesirable to lose safety or availability in a critical system.

Reliability engineering is concerned with overall minimisation of failures that could lead to financial losses for the responsible entity, whereas safety engineering focuses on minimising a specific set of failure types that in general could lead to loss of life, injury or damage to equipment.

Reliability hazards could transform into incidents leading to a loss of revenue for the company or the customer, for example due to direct and indirect costs associated with: loss of production due to system unavailability; unexpected high or low demands for spares; repair costs; man-hours; re-designs or interruptions to normal production.

Safety engineering is often highly specific, relating only to certain tightly regulated industries, applications, or areas. It primarily focuses on system safety hazards that could lead to severe accidents including: loss of life; destruction of equipment; or environmental damage. As such, the related system functional reliability requirements are often extremely high. Although it deals with unwanted failures in the same sense as reliability engineering, it, however, has less of a focus on direct costs, and is not concerned with post-failure repair actions. Another difference is the level of impact of failures on society, leading to a tendency for strict control by governments or regulatory bodies (e.g. nuclear, aerospace, defense, rail and oil industries).

### Fault tolerance

Safety can be increased using a 2oo2 cross checked redundant system. Availability can be increased by using "1oo2" (1 out of 2) redundancy at a part or system level. If both redundant elements disagree the more permissive element will maximize availability. A 1oo2 system should never be relied on for safety. Fault-tolerant systems often rely on additional redundancy (e.g. 2oo3 voting logic) where multiple redundant elements must agree on a potentially unsafe action before it is performed. This increases both availability and safety at a system level. This is common practice in aerospace systems that need continued availability and do not have a fail-safe mode. For example, aircraft may use triple modular redundancy for flight computers and control surfaces (including occasionally different modes of operation e.g. electrical/mechanical/hydraulic) as these need to always be operational, due to the fact that there are no "safe" default positions for control surfaces such as rudders or ailerons when the aircraft is flying.

### Basic reliability and mission reliability

The above example of a 2oo3 fault tolerant system increases both mission reliability as well as safety. However, the "basic" reliability of the system will in this case still be lower than a non-redundant (1oo1) or 2oo2 system. Basic reliability engineering covers all failures, including those that might not result in system failure, but do result in additional cost due to: maintenance repair actions; logistics; spare parts etc. For example, replacement or repair of 1 faulty channel in a 2oo3 voting system, (the system is still operating, although with one failed channel it has actually become a 2oo2 system) is contributing to basic unreliability but not mission unreliability. As an example, the failure of the tail-light of an aircraft will not prevent the plane from flying (and so is not considered a mission failure), but it does need to be remedied (with a related cost, and so does contribute to the basic unreliability levels).

### Detectability and common cause failures

When using fault tolerant (redundant) systems or systems that are equipped with protection functions, detectability of failures and avoidance of common cause failures becomes paramount for safe functioning and/or mission reliability.


## Reliability versus quality (Six Sigma)

Quality often focuses on manufacturing defects during the warranty phase. Reliability looks at the failure intensity over the whole life of a product or engineering system from commissioning to decommissioning. Six Sigma has its roots in statistical control in quality of manufacturing. Reliability engineering is a specialty part of systems engineering. The systems engineering process is a discovery process that is often unlike a manufacturing process. A manufacturing process is often focused on repetitive activities that achieve high quality outputs with minimum cost and time.

The everyday usage term "quality of a product" is loosely taken to mean its inherent degree of excellence. In industry, a more precise definition of quality as "conformance to requirements or specifications at the start of use" is used. Assuming the final product specification adequately captures the original requirements and customer/system needs, the quality level can be measured as the fraction of product units shipped that meet specifications. Manufactured goods quality often focuses on the number of warranty claims during the warranty period.

Quality is a snapshot at the start of life through the warranty period and is related to the control of lower-level product specifications. This includes time-zero defects i.e. where manufacturing mistakes escaped final Quality Control. In theory the quality level might be described by a single fraction of defective products. Reliability, as a part of systems engineering, acts as more of an ongoing assessment of failure rates over many years. Theoretically, all items will fail over an infinite period of time. Defects that appear over time are referred to as reliability fallout. To describe reliability fallout a probability model that describes the fraction fallout over time is needed. This is known as the life distribution model. Some of these reliability issues may be due to inherent design issues, which may exist even though the product conforms to specifications. Even items that are produced perfectly will fail over time due to one or more failure mechanisms (e.g. due to human error or mechanical, electrical, and chemical factors). These reliability issues can also be influenced by acceptable levels of variation during initial production.

Quality and reliability are, therefore, related to manufacturing. Reliability is more targeted towards clients who are focused on failures throughout the whole life of the product such as the military, airlines or railroads. Items that do not conform to product specification will generally do worse in terms of reliability (having a lower MTTF), but this does not always have to be the case. The full mathematical quantification (in statistical models) of this combined relation is in general very difficult or even practically impossible. In cases where manufacturing variances can be effectively reduced, six sigma tools have been shown to be useful to find optimal process solutions which can increase quality and reliability. Six Sigma may also help to design products that are more robust to manufacturing induced failures and infant mortality defects in engineering systems and manufactured product.

In contrast with Six Sigma, reliability engineering solutions are generally found by focusing on reliability testing and system design. Solutions are found in different ways, such as by simplifying a system to allow more of the mechanisms of failure involved to be understood; performing detailed calculations of material stress levels allowing suitable safety factors to be determined; finding possible abnormal system load conditions and using this to increase robustness of a design to manufacturing variance related failure mechanisms. Furthermore, reliability engineering uses system-level solutions, like designing redundant and fault-tolerant systems for situations with high availability needs (see Reliability engineering vs Safety engineering above).

Note: A "defect" in six-sigma/quality literature is not the same as a "failure" (Field failure | e.g. fractured item) in reliability. A six-sigma/quality defect refers generally to non-conformance with a requirement (e.g. basic functionality or a key dimension). Items can, however, fail over time, even if these requirements are all fulfilled. Quality is generally not concerned with asking the crucial question "are the requirements actually correct?", whereas reliability is.


## Reliability operational assessment

Once systems or parts are being produced, reliability engineering attempts to monitor, assess, and correct deficiencies. Monitoring includes electronic and visual surveillance of critical parameters identified during the fault tree analysis design stage. Data collection is highly dependent on the nature of the system. Most large organizations have quality control groups that collect failure data on vehicles, equipment and machinery. Consumer product failures are often tracked by the number of returns. For systems in dormant storage or on standby, it is necessary to establish a formal surveillance program to inspect and test random samples. Any changes to the system, such as field upgrades or recall repairs, require additional reliability testing to ensure the reliability of the modification. Since it is not possible to anticipate all the failure modes of a given system, especially ones with a human element, failures will occur. The reliability program also includes a systematic root cause analysis that identifies the causal relationships involved in the failure such that effective corrective actions may be implemented. When possible, system failures and corrective actions are reported to the reliability engineering organization.

Some of the most common methods to apply to a reliability operational assessment are failure reporting, analysis, and corrective action systems (FRACAS). This systematic approach develops a reliability, safety, and logistics assessment based on failure/incident reporting, management, analysis, and corrective/preventive actions. Organizations today are adopting this method and utilizing commercial systems (such as Web-based FRACAS applications) that enable them to create a failure/incident data repository from which statistics can be derived to view accurate and genuine reliability, safety, and quality metrics.

It is extremely important for an organization to adopt a common FRACAS system for all end items. Also, it should allow test results to be captured in a practical way. Failure to adopt one easy-to-use (in terms of ease of data-entry for field engineers and repair shop engineers) and easy-to-maintain integrated system is likely to result in a failure of the FRACAS program itself.

Some of the common outputs from a FRACAS system include Field MTBF, MTTR, spares consumption, reliability growth, failure/incidents distribution by type, location, part no., serial no., and symptom.

The use of past data to predict the reliability of new comparable systems/items can be misleading as reliability is a function of the context of use and can be affected by small changes in design/manufacturing.


## Reliability organizations

Systems of any significant complexity are developed by organizations of people, such as a commercial company or a government agency. The reliability engineering organization must be consistent with the company's organizational structure. For small, non-critical systems, reliability engineering may be informal. As complexity grows, the need arises for a formal reliability function. Because reliability is important to the customer, the customer may even specify certain aspects of the reliability organization.

There are several common types of reliability organizations. The project manager or chief engineer may employ one or more reliability engineers directly. In larger organizations, there is usually a product assurance or specialty engineering organization, which may include reliability, maintainability, quality, safety, human factors, logistics, etc. In such case, the reliability engineer reports to the product assurance manager or specialty engineering manager.

In some cases, a company may wish to establish an independent reliability organization. This is desirable to ensure that the system reliability, which is often expensive and time-consuming, is not unduly slighted due to budget and schedule pressures. In such cases, the reliability engineer works for the project day-to-day, but is actually employed and paid by a separate organization within the company.

Because reliability engineering is critical to early system design, it has become common for reliability engineers, however, the organization is structured, to work as part of an integrated product team.


## Education

Some universities offer graduate degrees in reliability engineering. Other reliability professionals typically have an engineering, statistics, math, or physics degree from a university or college program. Many engineering programs offer reliability courses, and some universities have entire reliability engineering programs. A reliability engineer must be registered as a professional engineer by the state or province by law, but not all reliability professionals are engineers. Reliability engineers are required in systems where public safety is at risk. There are many professional conferences and industry training programs available for reliability engineers. Several professional organizations exist for reliability engineers, including the American Society for Quality Reliability Division (ASQ-RD), the IEEE Reliability Society, the American Society for Quality (ASQ), and the Society of Reliability Engineers (SRE).
