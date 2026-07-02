---
title: "Signal reflection"
source: https://en.wikipedia.org/wiki/Reflection_(electrical)
domain: signal-integrity
license: CC-BY-SA-4.0
tags: signal integrity, crosstalk noise, eye diagram, transmission line effects
fetched: 2026-07-02
---

# Signal reflection

(Redirected from

Reflection (electrical)

)

In telecommunications, **signal reflection** happens when a signal is transmitted along a transmission medium (such as a copper cable or an optical fiber) and part of it is reflected back toward the source instead of reaching the end. This reflection is caused by imperfections or physical variations in the cable (such as abrupt changes in its geometry) that lead to impedance mismatches. These mismatches disrupt the signal and cause some of it to bounce back. In radio frequency (RF) systems, this is typically measured using the voltage standing wave ratio (VSWR), with a device called a VSWR bridge. The amount of reflected energy depends on the degree of impedance mismatch and is mathematically described by the reflection coefficient.

Because the principles are the same, this concept is perhaps easiest to understand when considering an optical fiber. Imperfections in the glass create mirrors that reflect the light back along the fiber.

Impedance discontinuities cause attenuation, attenuation distortion, standing waves, ringing and other effects because a portion of a transmitted signal will be reflected back to the transmitting device rather than continuing to the receiver, much like an echo. This effect is compounded if multiple discontinuities cause additional portions of the remaining signal to be reflected back to the transmitter. This is a fundamental problem with the daisy chain method of connecting electronic components.

When a returning reflection strikes another discontinuity, some of the signal rebounds in the original signal direction, creating multiple echo effects. These forward echoes strike the receiver at different intervals making it difficult for the receiver to accurately detect data values on the signal. The effects can resemble those of jitter.

Because damage to the cable can cause reflections, an instrument called an electrical time-domain reflectometer (ETDR; for electrical cables) or an optical time-domain reflectometer (OTDR; for optical cables) can be used to locate the damaged part of a cable. These instruments work by sending a short pulsed signal into the cable and measuring how long the reflection takes to return. If only reflection magnitudes are desired, however, and exact fault locations are not required, VSWR bridges perform a similar but lesser function for RF cables.

The combination of the effects of signal attenuation and impedance discontinuities on a communications link is called insertion loss. Proper network operation depends on constant characteristic impedance in all cables and connectors, with no impedance discontinuities in the entire cable system. When a sufficient degree of impedance matching is not practical, echo suppressors or echo cancellers, or both, can sometimes reduce the problems.

The Bergeron diagram method, valid for both linear and non-linear models, evaluates the reflection's effects in an electric line.
