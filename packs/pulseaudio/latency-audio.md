---
title: "Latency (audio)"
source: https://en.wikipedia.org/wiki/Latency_(audio)
domain: pulseaudio
license: CC-BY-SA-4.0
tags: pulseaudio server, alsa sound, sound server, open sound system
fetched: 2026-07-02
---

# Latency (audio)

**Latency** refers to a short period of delay (usually measured in milliseconds) between when an audio signal enters a system and when it emerges. Potential contributors to latency in an audio system include analog-to-digital conversion, buffering, digital signal processing, transmission time, digital-to-analog conversion, and the speed of sound in the transmission medium.

Latency can be a critical performance metric in professional audio, including sound reinforcement systems, foldback systems (especially those using in-ear monitors) live radio and television. Excessive audio latency has the potential to degrade call quality in telecommunications applications. Low-latency audio in computers is important for interactivity.

## Telephone calls

In all systems, latency can be said to consist of three elements: codec delay, playout delay and network delay.

Latency in telephone calls is sometimes referred to as **mouth-to-ear delay**; the telecommunications industry also uses the term *quality of experience* (QoE). Voice quality is measured according to the ITU model; measurable quality of a call degrades rapidly where the mouth-to-ear delay latency exceeds 200 milliseconds. The mean opinion score (MOS) is also comparable in a near-linear fashion with the ITU's quality scale - defined in standards G.107, G.108 and G.109 - with a quality factor *R* ranging from 0 to 100. An MOS of 4 ('Good') would have an *R* score of 80 or above; to achieve 100R requires an MOS exceeding 4.5.

The ITU and 3GPP groups end-user services into classes based on latency sensitivity:

|   | Very sensitive to delay Less sensitive to delay |   |   |   |
|---|---|---|---|---|
| Classes | Conversational Class (3GPP) Interactive Class (ITU) | Interactive Class (3GPP) Responsive Class (ITU) | Streaming Class (3GPP) Timely Class (ITU) | Background Class (3GPP) Non Critical Class (ITU) |
| Services | Conversational video/voice, real-time video | Voice messaging | Streaming video and voice | Fax |
| Realtime data | Transactional data | Non-realtime data | Background data |   |

Similarly, the G.114 recommendation regarding mouth-to-ear delay indicates that most users are "very satisfied" as long as latency does not exceed 200 ms, with an according *R* of 90+. Codec choice also plays an important role; the highest quality (and highest bandwidth) codecs like G.711 are usually configured to incur the least encode-decode latency, so on a network with sufficient throughput sub-100 ms latencies can be achieved. G.711 at a bitrate of 64 kbit/s is the encoding method predominantly used on the public switched telephone network.

### Mobile calls

The AMR narrowband codec, used in GSM and UMTS networks, introduces latency in the encode and decode processes.

As mobile operators upgrade existing *best-effort* networks to support concurrent multiple types of service over all-IP networks, services such as Hierarchical Quality of Service (*H-QoS*) allow for per-user, per-service QoS policies to prioritise time-sensitive protocols like voice calls, and other wireless backhaul traffic.

Another aspect of mobile latency is the inter-network handoff; as a customer on Network A calls a Network B customer, the call must traverse two separate Radio Access Networks, two core networks, and an interlinking Gateway Mobile Switching Centre (GMSC) which performs the physical interconnecting between the two providers.

### IP calls

With end-to-end QoS managed and assured rate connections, latency can be reduced to analogue PSTN/POTS levels. On a stable connection with sufficient bandwidth and minimal latency, VoIP systems typically have a minimum of 20 ms inherent latency. Under less ideal network conditions a 150 ms maximum latency is sought for general consumer use. Many popular videoconferencing systems rely on data buffering and data redundancy to cope for network jitter and packet loss. Measurements have shown that mouth-to-ear delay are between 160 and 300 ms over a 500-mile distance, on average US network conditions. Latency is a larger consideration when an echo is present and systems must perform echo suppression and cancellation.

## Computer audio

Latency can be a particular problem in audio platforms on computers. Supported interface optimizations reduce the delay to times that are too short for the human ear to detect. By reducing buffer sizes, latency can be reduced. A popular optimization solution is Steinberg's ASIO, which bypasses the audio platform and connects audio signals directly to the sound card's hardware. Many professional and semi-professional audio applications utilize the ASIO driver, allowing users to work with audio in real time. Pro Tools HD offers a low-latency system similar to ASIO. Pro Tools 10 and 11 are also compatible with ASIO interface drivers.

The Linux real-time kernel is a modified kernel that alters the standard timer frequency the Linux kernel uses and gives all processes or threads the ability to have real-time priority. This means that a time-critical process like an audio stream can get priority over another, less-critical process like network activity. This is also configurable per user (for example, the processes of user "tux" could have priority over processes of user "nobody" or over the processes of several system daemons).

## Digital television audio

Many modern digital television receivers, set-top boxes and AV receivers use sophisticated audio processing, which can create a delay between the time when the audio signal is received and the time when it is heard on the speakers. Since TVs also introduce delays in processing the video signal, this can result in the two signals being sufficiently synchronized to be unnoticeable by the viewer. However, if the difference between the audio and video delay is significant, the effect can be disconcerting. Some systems have a lip sync setting that allows the audio lag to be adjusted to synchronize with the video, and others may have advanced settings where some of the audio processing steps can be turned off.

Audio lag is also a significant detriment in rhythm games, where precise timing is required to succeed. Most of these games have a lag calibration setting whereby the game will adjust the timing windows by a certain number of milliseconds to compensate. In these cases, the notes of a song will be sent to the speakers before the game even receives the required input from the player in order to maintain the illusion of rhythm. Games that rely upon musical improvisation, such as Rock Band drums or DJ Hero, can still suffer tremendously, as the game cannot predict what the player will hit in these cases, and excessive lag will still create a noticeable delay between hitting notes and hearing them play.

## Broadcast audio

Audio latency can be experienced in broadcast systems where someone is contributing to a live broadcast over a satellite or similar link with high delay. The person in the main studio has to wait for the contributor at the other end of the link to react to questions. Latency in this context could be between several hundred milliseconds and a few seconds. Dealing with audio latencies as high as this takes special training in order to make the resulting combined audio output reasonably acceptable to the listeners. Wherever practical, it is important to try to keep live production audio latency low in order to keep the reactions and interchange of participants as natural as possible. A latency of 10 milliseconds or better is the target for audio circuits within professional production structures.

## Live performance audio

Latency in live performance occurs naturally from the speed of sound. It takes sound about 3 milliseconds to travel 1 meter. Small amounts of latency occur between performers, depending on how they are spaced from each other and from stage monitors if these are used. This creates a practical limit to how far apart the artists in a group can be from one another. Stage monitoring extends that limit, as sound in the form of an electrical signal travels close to the speed of light through the cables that connect stage monitors.

Performers, particularly in large spaces, will also hear reverberation, or echo of their music, as the sound that projects from the stage, bounces off of walls and structures, and returns with latency and distortion. A primary purpose of stage monitoring is to provide artists with more primary sound so that they are not confused by the latency of these reverberations.

### Live signal processing

While analog audio equipment has no appreciable latency, digital audio equipment has latency associated with two general processes: conversion from one format to another, and digital signal processing (DSP) tasks such as equalization, compression and routing.

Digital conversion processes include analog-to-digital converters (ADC), digital-to-analog converters (DAC), and various changes from one digital format to another, such as AES3 which carries low-voltage electrical signals to ADAT, an optical transport. Any such process takes a small amount of time to accomplish; typical latencies are in the range of 0.2 to 1.5 milliseconds, depending on sampling rate, software design and hardware architecture.

Different audio signal processing operations, such as finite impulse response (FIR) and infinite impulse response (IIR) filters, take different mathematical approaches to the same end and can have different latencies. In addition, input and output sample buffering add delay. Typical latencies range from 0.5 to 10 milliseconds, with some designs having as much as 30 milliseconds of delay.

Latency in digital audio equipment is most noticeable when a singer's voice is transmitted through their microphone, through digital audio mixing, processing and routing paths, then sent to their own ears via in-ear monitors or headphones. In this case, the singer's vocal sound is conducted to their own ear through the bones of the head, then through the digital pathway to their ears some milliseconds later. In one study, listeners found latency greater than 15 ms to be noticeable. Latency for other musical activities, such as playing guitar, does not have the same critical concern. Ten milliseconds of latency isn't as noticeable to a listener who is not hearing his or her own voice.

### Delayed loudspeakers

In sound reinforcement for music or speech presentation in large venues, it is optimal to deliver sufficient sound volume to the back of the venue without resorting to excessive sound volumes near the front. One way for audio engineers to achieve this is to use additional loudspeakers placed at a distance from the stage but closer to the rear of the audience. Sound travels through air at the speed of sound (around 343 metres (1,125 ft) per second depending on air temperature and humidity). By measuring or estimating the difference in latency between the loudspeakers near the stage and the loudspeakers nearer the audience, the audio engineer can introduce an appropriate delay in the audio signal going to the latter loudspeakers, so that the wavefronts from near and far loudspeakers arrive at the same time. Because of the Haas effect an *additional* 15 milliseconds can be added to the delay time of the loudspeakers nearer the audience, so that the stage's wavefront reaches them first, to focus the audience's attention on the stage rather than the local loudspeaker. The slightly later sound from delayed loudspeakers simply increases the perceived sound level without negatively affecting localization.
