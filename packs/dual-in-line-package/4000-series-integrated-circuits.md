---
title: "4000-series integrated circuits"
source: https://en.wikipedia.org/wiki/4000-series_integrated_circuits
domain: dual-in-line-package
license: CC-BY-SA-4.0
tags: dual in-line package
fetched: 2026-07-03
---

# 4000-series integrated circuits

The **4000 series** is a CMOS logic family of integrated circuits (ICs) first introduced in 1968 by RCA. It was slowly migrated into the 4000B buffered series after about 1975. It had a much wider supply voltage range than any contemporary logic family (3 V to 18 V recommended range for "B" series). Almost all IC manufacturers active during this initial era fabricated models for this series. Its naming convention is still in use today.

## History

The 4000 series was introduced as the *CD4000 COS/MOS* series in 1968 by RCA as a lower-power and more versatile alternative to the 7400 series of transistor-transistor logic (TTL) chips. The logic functions were implemented with the newly introduced complementary metal–oxide–semiconductor (CMOS) technology. While initially marketed with "COS/MOS" labeling by RCA (which stood for "complementary symmetry metal–oxide semiconductor"), the shorter *CMOS* terminology emerged as the industry preference to refer to the technology. The first chips in the series were designed by a group led by Albert Medwin.

Wide adoption was initially hindered by the comparatively lower speeds of the designs compared to TTL-based designs. Speed limitations were eventually overcome with newer fabrication methods (such as self-aligned gates of polysilicon instead of metal). These CMOS variants performed on par with contemporary TTL. The series was extended in the late 1970s and 1980s with new models that were given 45xx and 45xxx designations, but are usually still regarded by engineers as part of the 4000 series. In the 1990s, some manufacturers (e.g. Texas Instruments) ported the 4000 series to newer HCMOS-based designs to provide greater speeds.

## Design considerations

The 4000 series facilitates simpler circuit design through relatively low power consumption, a wide range of supply voltages, and vastly increased load-driving capability (fanout) compared to TTL. This makes the series ideal for use in prototyping LSI designs. While TTL ICs are similarly modular, these usually lack the symmetrical drive strength of CMOS and may therefore require more consideration of the loads applied on its outputs. Just like with TTL, buffered models can drive higher electrical current (mainly available for I/O devices like octal latches and three-state drivers) but have a slightly higher risk of introducing ringing (transient oscillations), unless correctly damped or terminated. Many models contain a high level of integration, including fully integrated 7-segment display counters, walking ring counters, and full adders.

## Common chips

**Logic gates**

**Flip-flops**

- 4013 – Dual D-type flip-flop. Each flip-flop has independent data, Q, /Q, clock, reset, set.
- 40174 – Hex D-type flip-flop. Each flip-flop has independent data and Q. All share clock and reset.
- 40175 – Quad D-type flip-flop. Each flip-flop has independent data, Q, /Q. All share clock and reset.

**Counters**

- 4017 – Decade counter with 10-output decoder.
- 4026 – Decade counter with 7-segment digit decoded output.
- 40110 – Up/down decade counter with 7-segment display decoder with 25 mA output drivers.
- 40192 – Up/down decade counter with 4-bit BCD preset.
- 40193 – Up/down binary counter with 4-bit binary preset.

**Decoders**

- 4028 – 4-bit BCD to 10-output decoder (can be used as 3-bit binary to 8-output decoder)
- 4511 – 4-bit BCD to 7-segment display decoder with 25 mA output drivers.

**Timers**

- 4047 – Monostable/astable multivibrator with external RC oscillator.
- 4060 – 14-bit ripple counter with external RC or crystal oscillator (long duration) (schmitt-trigger inputs) (can be used with 32.768 kHz crystal)
- 4541 – 16-bit ripple counter with external RC oscillator (long duration).

**Analog**

- 4051 – Single 8-channel analog mux.
- 4066 – Quad SPST analog switch.
