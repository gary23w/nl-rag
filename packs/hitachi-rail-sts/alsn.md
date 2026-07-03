---
title: "ALSN"
source: https://en.wikipedia.org/wiki/ALSN
domain: hitachi-rail-sts
license: CC-BY-SA-4.0
tags: hitachi rail sts
fetched: 2026-07-03
---

# ALSN

**ALSN** (автоматическая локомотивная сигнализация непрерывная, in Latin - avtomaticheskaya lokomotivnaya signalizatsiya nepreryvnaya, meaning *Continuous Automatic Train Signalling*) is a train control system used widely on the main lines of the ex-Soviet states (Russian Federation, Ukraine, Belarus, Latvia, Lithuania, Estonia). It uses modulated pulses inducted into rails similar to the Italian RS4 Codici and American Pulse Code Cab Signaling. On high-speed lines the variant ALS-EN (АЛС-ЕН) is used which takes advantage of a double phase difference modulation of the carrier wave.

The name ALSN (АЛСН - автоматическая локомотивная сигнализация непрерывного действия) is composed of ALS, literally "Automatic Locomotive Signalling" (АЛС - автоматическая локомотивная сигнализация) and the variant designation N "Continuous Effect" (Н - Непрерывного действия). Other variants are built according to the same scheme like ALST (АЛСТ) for "Fixed Point Automatic Train Signalling" (АЛС точечного действия) and ALSR (АЛСР) for "Radio-Based Automatic Train Signalling" (АЛС с использованием радиоканала). The term ALS-ARS (АЛС-АРС) refers to "Automatic Train Signalling with Automatic Speed Regulation" (автоматическая локомотивная сигнализация с автоматическим регулированием скорости) used in subways which is a form of an automatic train control system.

## ALSN operation principles

The system makes use of several distinct pulse train patterns of alternating current flowing through a track circuit to convey an aspect of the next signal. The circuit comprises the feedpoint at the next signal, one running rail, first locomotive axle, another running rail and back to the signal feedpoint. The resulting electromagnetic field is picked up by receiver coils located just front of the first axle of the locomotive. The signal is then amplified, filtered and evaluated. If the received signal changes from a more permissive to a less permissive aspect (like when passing a yellow light, indicating the next signal is red, which, in turn, requires stopping in front of it), an immediate vigilance control acknowledge is required; depending on configuration and aspects, periodic checks and a speed limit may be enforced as well.

The benefits of the system are relative encoder simplicity (a simple motor-operated camwheel closing and opening relay contacts generates the pulse train) and the ability to use the same signal for track occupancy detection. The drawbacks are a somewhat long response time unsuitable for high speed operation (which resulted in ALS-EN's implementation), and the necessity to switch between 25/50/75 Hz frequency variants depending on traction current type (AC/DC) and other conditions.

## VEPS

A new, modular ALSN automatic train protection onboard system VEPS has been under development since 2002 in Estonia. Based on programmable logic controller technologies, the system was developed by Estonian Railway engineers and patented in 2004 by Indrek Syld. The new system was installed in the CE35 type of locomotive (77 systems) during 2003–2004. A new platform (level 2.0) was installed on Stadler's FLIRT trains for Estonia in 2012 (76 systems), and in 2016 a third generation of the system was introduced for the international market.

## KLUB

Since the 1990s, the Russian Railroad Company has introduced a computerized successor system KLUB-U which requires either ALSN only or both, ALSN and ALS-EN sensors for compatibility. In ERTMS the ALSN/ALS-EN systems are listed as ETCS Class-B systems.

## ALS-ARS

A similar in general theory of operation, but differently implemented, is an ALS-ARS system used in subways of the former Soviet Union. It uses low frequency signals transmitted and received as described above, with the difference that the signals are continuous wave and the signal's *frequency* determines its code meaning, which results in much faster response time. Typically, two frequencies are transmitted at the same time, indicating the current speed limit and, if lower, the limit for the next section, providing the train driver with a warning and time to react and reduce speed.

In case of an overspeed, the train is unconditionally braked to the indicated speed limit, and then, if not acknowledged by a driver pressing a vigilance button, to a complete stop. Should be there no frequency received (such as on an uncoded track in a maintenance depot or in case of an equipment failure), the driver may proceed at a low speed while holding a vigilance pedal.

- (ALSN railway cab signal)ALSN railway cab signal
- (Electro-pneumatic valve which causes emergency brakes to be applied should the driver fail to acknowledge vigilance check or exceed a speed limit)Electro-pneumatic valve which causes emergency brakes to be applied should the driver fail to acknowledge vigilance check or exceed a speed limit
- (ALSN pickup coil)ALSN pickup coil
