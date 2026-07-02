---
title: "Quality of experience"
source: https://en.wikipedia.org/wiki/Quality_of_experience
domain: apdex-score
license: CC-BY-SA-4.0
tags: apdex index, application performance index, user satisfaction score, response time bucket
fetched: 2026-07-02
---

# Quality of experience

**Quality of experience** (**QoE**) is a measure of the delight or annoyance of a customer's experiences with a service (e.g., web browsing, phone call, TV broadcast). QoE focuses on the entire service experience; it is a holistic concept, similar to the field of user experience, but with its roots in telecommunication. QoE is an emerging multidisciplinary field based on social psychology, cognitive science, economics, and engineering science, focused on understanding overall human quality requirements.

## Definition and concepts

In 2013, within the context of the COST Action *QUALINET*, QoE has been defined as:

> The degree of delight or annoyance of the user of an application or service. It results from the fulfillment of his or her expectations with respect to the utility and / or enjoyment of the application or service in the light of the user’s personality and current state.

This definition has been adopted in 2016 by the International Telecommunication Union in Recommendation ITU-T P.10/G.100. Before, various definitions of QoE had existed in the domain, with the above-mentioned definition now finding wide acceptance in the community.

QoE has historically emerged from Quality of Service (QoS), which attempts to objectively measure service parameters (such as packet loss rates or average throughput). QoS measurement is most of the time not related to a customer, but to the media or network itself. QoE however is a purely subjective measure from the user's perspective of the overall quality of the service provided, by capturing people's aesthetic and hedonic needs.

QoE looks at a vendor's or purveyor's offering from the standpoint of the customer or end user, and asks, "What mix of goods, services, and support, do you think will provide you with the perception that the total product is providing you with the experience you desired and/or expected?" It then asks, "Is this what the vendor/purveyor has actually provided?" If not, "What changes need to be made to enhance your total experience?" In short, QoE provides an assessment of human expectations, feelings, perceptions, cognition and satisfaction with respect to a particular product, service or application.

QoE is a blueprint of all human subjective and objective quality needs and experiences arising from the interaction of a person with technology and with business entities in a particular context. Although QoE is perceived as subjective, it is an important measure that counts for customers of a service. Being able to measure it in a controlled manner helps operators understand what may be wrong with their services and how to improve them.

## QoE factors

QoE aims at taking into consideration every factor that contributes to a user's perceived quality of a system or service. This includes system, human and contextual factors. The following so-called "influence factors" have been identified and classified by Reiter et al.:

- **Human Influence Factors**
  - Low-level processing (visual and auditory acuity, gender, age, mood, …)
  - Higher-level processing (cognitive processes, socio-cultural and economic background, expectations, needs and goals, other personality traits…)
- **System Influence Factors**
  - Content-related
  - Media-related (encoding, resolution, sample rate, …)
  - Network-related (bandwidth, delay, jitter, …)
  - Device-related (screen resolution, display size, …)
- **Context Influence Factors**
  - Physical context (location and space)
  - Temporal context (time of day, frequency of use, …)
  - Social context (inter-personal relations during experience)
  - Economic context
  - Task context (multitasking, interruptions, task type)
  - Technical and information context (relationship between systems)

Studies in the field of QoE have typically focused on system factors, primarily due to its origin in the QoS and network engineering domains. Through the use of dedicated test laboratories, the context is often sought to be kept constant.

## QoE versus User Experience

QoE is strongly related to but different from the field of User Experience (UX), which also focuses on users' experiences with services. Historically, QoE has emerged from telecommunication research, while UX has its roots in Human–Computer Interaction. Both fields can be considered multi-disciplinary. In contrast to UX, the goal of improving QoE for users was more strongly motivated by economic needs.

Wechsung and De Moor identify the following key differences between the fields:

|   | QoE | UX |
|---|---|---|
| **Origins** | Telecommunication | Human–Computer Interaction |
| **Driving Force** | Technology-centered | Human-centered |
| **Theoretical Basis** | Measurement and instrumentation approaches Historical lack of theoretical frameworks | Non-instrumental research Theoretic background in hedonic psychology |
| **Measurement and Evaluation** | Predominantly quantitative research Empirical–positivist research | Predominantly qualitative methods Interpretative and constructivist research |
| **Experience and Perceptions** | Focus on "quality formation" and perception of quality | Focus on "experience" concept |

## QoE measurement

As a measure of the end-to-end performance at the service level from the user's perspective, QoE is an important metric for the design of systems and engineering processes. This is particularly relevant for video services because – due to their high traffic demands –, bad network performance may highly affect the user's experience. So, when designing systems, the expected output, i.e. the expected QoE, is often taken into account – also as a system output metric and optimization goal.

To measure this level of QoE, human ratings can be used. The mean opinion score (MOS) is a widely used measure for assessing the quality of media signals. It is a limited form of QoE measurement, relating to a specific media type, in a controlled environment and without explicitly taking into account user expectations. The MOS as an indicator of experienced quality has been used for audio and speech communication, as well as for the assessment of quality of Internet video, television and other multimedia signals, and web browsing. Due to inherent limitations in measuring QoE in a single scalar value, the usefulness of the MOS is often debated.

Subjective quality evaluation requires a lot of human resources, establishing it as a time-consuming process. Objective evaluation methods can provide quality results faster, but require dedicated computing resources. Since such instrumental video quality algorithms are often developed based on a limited set of subjective data, their QoE prediction accuracy may be low when compared to human ratings.

QoE metrics are often measured at the end devices and can conceptually be seen as the remaining quality after the distortion introduced during the preparation of the content and the delivery through the network, until it reaches the decoder at the end device. There are several elements in the media preparation and delivery chain, and some of them may introduce distortion. This causes degradation of the content, and several elements in this chain can be considered as "QoE-relevant" for the offered services. The causes of degradation are applicable for any multimedia service, that is, not exclusive to video or speech. Typical degradations occur at the encoding system (compression degradation), transport network, access network (e.g., packet loss or packet delay), home network (e.g. WiFi performance) and end device (e.g. decoding performance).

## QoE management

Several QoE-centric network management and bandwidth management solutions have been proposed, which aim to improve the QoE delivered to the end-users.

When managing a network, QoE fairness may be taken into account in order to keep the users sufficiently satisfied (i.e., high QoE) in a fair manner. From a QoE perspective, network resources and multimedia services should be managed in order to guarantee specific QoE levels instead of classical QoS parameters, which are unable to reflect the actual delivered QoE. A pure QoE-centric management is challenged by the nature of the Internet itself, as the Internet protocols and architecture were not originally designed to support today's complex and high demanding multimedia services.

As an example for an implementation of QoE management, network nodes can become QoE-aware by estimating the status of the multimedia service as perceived by the end-users. This information can then be used to improve the delivery of the multimedia service over the network and proactively improve the users' QoE. This can be achieved, for example, via traffic shaping. QoE management gives the service provider and network operator the capability to minimize storage and network resources by allocating only the resources that are sufficient to maintain a specific level of user satisfaction.

As it may involve limiting resources for some users or services in order to increase the overall network performance and QoE, the practice of QoE management requires that net neutrality regulations are considered.
