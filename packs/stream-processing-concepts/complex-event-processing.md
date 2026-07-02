---
title: "Complex event processing"
source: https://en.wikipedia.org/wiki/Complex_event_processing
domain: stream-processing-concepts
license: CC-BY-SA-4.0
tags: stream processing, event stream processing, data stream management system, windowing state, complex event processing
fetched: 2026-07-02
---

# Complex event processing

**Event processing** is a method of tracking and analyzing (processing) streams of information (data) about things that happen (events), and deriving a conclusion from them. **Complex event processing** (**CEP**) consists of a set of concepts and techniques developed in the early 1990s for processing real-time events and extracting information from event streams as they arrive. The goal of complex event processing is to identify meaningful events (such as opportunities or threats) in real-time situations and respond to them as quickly as possible.

These events may be happening across the various layers of an organization as sales leads, orders or customer service calls. Or, they may be news items, text messages, social media posts, business processes (such as supply chain), traffic reports, weather reports, or other kinds of data. An event may also be defined as a "change of state," when a measurement exceeds a predefined threshold of time, temperature, or other value.

Analysts have suggested that CEP will give organizations a new way to analyze patterns in real-time and help the business side communicate better with IT and service departments. CEP has since become an enabling technology in many systems that are used to take immediate action in response to incoming streams of events. Applications are now to be found (2018) in many sectors of business including stock market trading systems, mobile devices, internet operations, fraud detection, the transportation industry, and governmental intelligence gathering.

The vast amount of information available about events is sometimes referred to as the event cloud.

## Conceptual description

Among thousands of incoming events, a monitoring system may for instance receive the following three from the same source:

1. church bells ringing.
2. the appearance of a man in a tuxedo with a woman in a flowing white gown.
3. rice flying through the air.

From these events the monitoring system may infer a *complex event*: a wedding. CEP as a technique helps discover complex events by analyzing and correlating other events: the bells, the man and woman in wedding attire and the rice flying through the air.

CEP relies on a number of techniques, including:

- Event-pattern detection
- Event abstraction
- Event filtering
- Event aggregation and transformation
- Modeling event hierarchies
- Detecting relationships (such as causality, membership or timing) between events
- Abstracting event-driven processes

Commercial applications of CEP exist in variety of industries and include the detection of credit-card fraud, business activity monitoring, and security monitoring.

## History

The CEP area has roots in discrete event simulation, the active database area and some programming languages. The activity in the industry was preceded by a wave of research projects in the 1990s. According to the first project that paved the way to a generic CEP language and execution model was the Rapide project in Stanford University, directed by David Luckham. In parallel there have been two other research projects: Infospheres in California Institute of Technology, directed by K. Mani Chandy, and Apama in University of Cambridge directed by John Bates. The commercial products were dependents of the concepts developed in these and some later research projects. Community efforts started in a series of event processing symposia organized by the Event Processing Technical Society, and later by the ACM DEBS conference series. One of the community efforts was to produce the event processing manifesto.

CEP is used in operational intelligence (OI) products to provide insight into business operations by running query analysis against live feeds and event data. OI collects real-time data and correlates against historical data to provide insight and analysis. Multiple sources of data can be combined to provide a common operating picture that uses current information.

In network management, systems management, application management and service management, people usually refer instead to event correlation. As CEP engines, event correlation engines (*event correlators*) analyze a mass of events, pinpoint the most significant ones, and trigger actions. However, most of them do not produce new inferred events. Instead, they relate high-level events with low-level events.

Inference engines, e.g., rule-based reasoning engines, typically produce inferred information in artificial intelligence. However, they do not usually produce new information in the form of complex (i.e., inferred) events.

## Example

A more systemic example of CEP involves a car, some sensors and various events and reactions. Imagine that a car has several sensors—one that measures tire pressure, one that measures speed, and one that detects if someone sits on a seat or leaves a seat.

In the first situation, the car is moving and the pressure of one of the tires moves from 45 psi to 41 psi over 15 minutes. As the pressure in the tire is decreasing, a series of events containing the tire pressure is generated. In addition, a series of events containing the speed of the car is generated. The car's Event Processor may detect a situation whereby a loss of tire pressure over a relatively long period of time results in the creation of the "lossOfTirePressure" event. This new event may trigger a reaction process to note the pressure loss into the car's maintenance log, and alert the driver via the car's portal that the tire pressure has reduced.

In the second situation, the car is moving and the pressure of one of the tires drops from 45 psi to 20 psi in 5 seconds. A different situation is detected—perhaps because the loss of pressure occurred over a shorter period of time, or perhaps because the difference in values between each event were larger than a predefined limit. The different situation results in a new event "blowOutTire" being generated. This new event triggers a different reaction process to immediately alert the driver and to initiate onboard computer routines to assist the driver in bringing the car to a stop without losing control through skidding.

In addition, events that represent detected situations can also be combined with other events in order to detect more complex situations. For example, in the final situation the car is moving normally and suffers a blown tire which results in the car leaving the road and striking a tree, and the driver is thrown from the car. A series of different situations are rapidly detected. The combination of "blowOutTire", "zeroSpeed" and "driverLeftSeat" within a very short period of time results in a new situation being detected: "occupantThrownAccident". Even though there is no direct measurement that can determine conclusively that the driver was thrown, or that there was an accident, the combination of events allows the situation to be detected and a new event to be created to signify the detected situation. This is the essence of a complex (or composite) event. It is complex because one cannot directly detect the situation; one has to infer or deduce that the situation has occurred from a combination of other events.

## Integration with business process management

A natural fit for CEP has been with business process management (BPM). BPM focuses on end-to-end business processes, in order to continuously optimize and align for its operational environment.

However, the optimization of a business does not rely solely upon its individual, end-to-end processes. Seemingly disparate processes can affect each other significantly. Consider this scenario: In the aerospace industry, it is good practice to monitor breakdowns of vehicles to look for trends (determine potential weaknesses in manufacturing processes, material, etc.). Another separate process monitors current operational vehicles' life cycles and decommissions them when appropriate. One use for CEP is to link these separate processes, so that in the case of the initial process (breakdown monitoring) discovering a malfunction based on metal fatigue (a significant event), an action can be created to exploit the second process (life cycle) to issue a recall on vehicles using the same batch of metal discovered as faulty in the initial process.

The integration of CEP and BPM must exist at two levels, both at the business awareness level (users must understand the potential holistic benefits of their individual processes) and also at the technological level (there needs to be a method by which CEP can interact with BPM implementation). For a recent state of the art review on the integration of CEP with BPM, which is frequently labeled as Event-Driven Business Process Management, refer to.

Computation-oriented CEP's role can arguably be seen to overlap with Business Rule technology.

For example, customer service centers are using CEP for click-stream analysis and customer experience management. CEP software can factor real-time information about millions of events (clicks or other interactions) per second into business intelligence and other decision-support applications. These "recommendation applications" help agents provide personalized service based on each customer's experience. The CEP application may collect data about what customers on the phone are currently doing, or how they have recently interacted with the company in other various channels, including in-branch, or on the Web via self-service features, instant messaging and email. The application then analyzes the total customer experience and recommends scripts or next steps that guide the agent on the phone, and hopefully keep the customer happy.

## Integration with time series databases

A time series database is a software system that is optimized for the handling of data organized by time. Time series are finite or infinite sequences of data items, where each item has an associated timestamp and the sequence of timestamps is non-decreasing. Elements of a time series are often called ticks. The timestamps are not required to be ascending (merely non-decreasing) because in practice the time resolution of some systems such as financial data sources can be quite low (milliseconds, microseconds or even nanoseconds), so consecutive events may carry equal timestamps.

Time series data provides a historical context to the analysis typically associated with complex event processing. This can apply to any vertical industry such as finance and cooperatively with other technologies such as BPM.

The ideal case for CEP analysis is to view historical time series and real-time streaming data as a single time continuum. What happened yesterday, last week or last month is simply an extension of what is occurring today and what may occur in the future. An example may involve comparing current market volumes to historic volumes, prices and volatility for trade execution logic. Or the need to act upon live market prices may involve comparisons to benchmarks that include sector and index movements, whose intra-day and historic trends gauge volatility and smooth outliers.

## Internet of things and smart cyber-physical systems

Complex event processing is a key enabler in Internet of things (IoT) settings and smart cyber-physical systems (CPS) as well. Processing dense and heterogeneous streams from various sensors and matching patterns against those streams is a typical task in such cases. The majority of these techniques rely on the fact that representing the IoT system's state and its changes is more efficient in the form of a data stream, instead of having a static, materialized model. Reasoning over such stream-based models fundamentally differs from traditional reasoning techniques and typically require the combination of model transformations and CEP.
