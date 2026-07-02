---
title: "Crosstalk"
source: https://en.wikipedia.org/wiki/Crosstalk
domain: electromagnetic-compatibility
license: CC-BY-SA-4.0
tags: electromagnetic compatibility, electromagnetic interference, signal crosstalk, common-mode signal
fetched: 2026-07-02
---

# Crosstalk

In electronics, **crosstalk** (**XT**) is a phenomenon by which a signal transmitted on one circuit or channel of a transmission system creates an undesired effect in another circuit or channel. Crosstalk is usually caused by undesired capacitive, inductive, or conductive coupling from one circuit or channel to another.

Where the electric, magnetic, or traveling fields of two electric signals overlap, the electromagnetic interference created causes crosstalk. For example, crosstalk can comprise magnetic fields that induce a smaller signal in neighboring wires.

In electrical circuits sharing a common signal return path, electrical impedance in the return path creates **common impedance coupling** between the signals, resulting in crosstalk.

Crosstalk is a significant issue in structured cabling, audio electronics, integrated circuit design, wireless communication and other communications systems.

## In cabling

In structured cabling, crosstalk refers to electromagnetic interference from one unshielded twisted pair to another twisted pair, normally running in parallel. Signals traveling through adjacent pairs of wire create magnetic fields that interact with each other, inducing interference in the neighboring pair. The pair causing the interference is called the *disturbing pair*, while the pair experiencing the interference is the *disturbed pair*.

**Near-end crosstalk (NEXT)**

NEXT is a measure of the ability of a cable to reject crosstalk, so the higher the NEXT value, the greater the rejection of crosstalk at the local connection. It is referred to as

near end

because the interference between the two signals in the cable is measured at the same end of the cable as the interfering transmitter. The NEXT value for a given cable type is generally expressed in decibels per feet or decibels per 1000 feet and varies with the frequency of transmission. General specifications for cabling (such as CAT 5) usually include the minimum NEXT values.

**Power sum near-end crosstalk (PSNEXT)**

PSNEXT is a NEXT measurement which includes the sum of crosstalk contributions from all adjacent pairs as an algebraic sum of the NEXT of the three wire pairs as they affect the fourth pair in a four-pair cable (e.g., Category 6 cable).

The Superior Modular Products White paper

states that the testing process for PSNEXT consists of measuring all pair-to-pair crosstalk combinations and then summing all of the values for each pair. The specification was developed to directly address the effect of transmissions on multiple adjacent pairs on the pair being tested and is relevant to all connecting hardware and associated communications cables.

Cabling bandwidth in excess of 100

MHz (

Category 5 cable

bandwidth) makes consideration of PSNEXT more important as

Gigabit Ethernet

through

Cat 6

uses all four wire pairs simultaneously and bidirectionally. The additional wire pair usage and growing bandwidth increases the need to keep NEXT in check.

**Far-end crosstalk (FEXT)**

FEXT measures the interference between two pairs of a cable measured at the far end of the cable with respect to the interfering transmitter.

**Equal level far end crosstalk (ELFEXT)**

ELFEXT measures the FEXT with attenuation compensation.

**Alien crosstalk (AXT)**

AXT is interference caused by other cables routed close to the cable of interest as opposed to signals contained in the same cable.

## In audio

In stereo audio reproduction, crosstalk can refer to signal leakage across from one program channel to another, reducing channel separation and stereo imaging. Crosstalk between channels in mixing consoles, and between studio feeds is a much more noticeable problem, as these are likely to be carrying very different programs or material.

Crosstalk is an electrical effect and can be quantified with a crosstalk measurement. Crosstalk measurements are made on audio systems to determine the amount of signal leaking from one channel to another. The Independent Broadcasting Authority published a weighting curve for use in crosstalk measurement that gives due emphasis to the subjective audibility of different frequencies. In the absence of any international standards, this is still in use despite the demise of the IBA.

Good crosstalk performance for a stereo system is not difficult to achieve in today's digital audio systems, though it is difficult to keep below the desired figure of −30 dB or so on vinyl recordings and FM radio.

## Other examples

In telecommunication or telephony, crosstalk is often distinguishable as pieces of speech or in-band signaling tones leaking from other people's connections. If the connection is analog, twisted pair cabling can often be used to reduce crosstalk. Alternatively, the signals can be converted to digital form, which is typically less susceptible to crosstalk.

In wireless communication, crosstalk is often denoted co-channel interference, and is related to adjacent-channel interference.

In integrated circuit design, crosstalk normally refers to a signal affecting another nearby signal. Usually, the coupling is capacitive, and to the nearest neighbor, but other forms of coupling and effects on signal further away are sometimes important, especially in analog designs. See signal integrity for tools used to measure and prevent this problem, and substrate coupling for a discussion of crosstalk conveyed through the integrated circuit substrate. There are a wide variety of repair solutions, with increased spacing, wire re-ordering, and shielding being the most common.

In full-field optical coherence tomography, "crosstalk" refers to the phenomenon that due to highly scattering objects, multiple scattered photons reach the image plane and generate a coherent signal after travelling a path length that matches that of the sample depth within a coherence length.

In stereoscopic 3D displays, crosstalk refers to the incomplete isolation of the left and right image channels so that one bleeds into the other – like a double exposure, which produces a ghosting effect.
