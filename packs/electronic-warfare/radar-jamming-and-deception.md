---
title: "Radar jamming and deception"
source: https://en.wikipedia.org/wiki/Radar_jamming_and_deception
domain: electronic-warfare
license: CC-BY-SA-4.0
tags: electronic warfare, radar jamming, electronic countermeasure, signals intelligence
fetched: 2026-07-02
---

# Radar jamming and deception

**Radar jamming and deception** is a form of electronic countermeasures (ECMs) that intentionally sends out radio frequency signals to interfere with the operation of radar by saturating its receiver with noise or false information. Concepts that blanket the radar with signals so its display cannot be read are normally known as **jamming**, while systems that produce confusing or contradictory signals are known as **deception**, but it is also common for all such systems to be referred to as jamming.

There are two general classes of radar jamming, mechanical and electronic. Mechanical jamming entails reflecting enemy radio signals in various ways to provide false or misleading target signals to the radar operator. Electronic jamming works by transmitting additional radio signals towards enemy receivers, making it difficult to detect real target signals, or take advantage of known behaviors of automated systems like radar lock-on to confuse the system.

Various Electronic counter-countermeasures (ECCMs) can sometimes help radar operators maintain target detection despite jamming.

## Mechanical jamming

Mechanical jamming is caused by devices that reflect or re-reflect radar energy back to the radar to produce false target returns on the operator's scope. Mechanical jamming devices include chaff, corner reflectors, and decoys.

- **Chaff** is made of different length metallic strips, which reflect different frequencies, to create a large area of false returns in which a real contact would be difficult to detect. Modern chaff is usually aluminum-coated glass fibers of various lengths. Their extremely low weight and small size allow them to form a dense, long-lasting cloud of interference. This cloud is only effective in the range cell that it occupies. The slow movement of the chaff (compared to a flying target) makes it easily discriminated, based on the lacking Doppler shift. Ships, on the other hand, can benefit greatly from a slow-moving chaff cloud. The cloud is released within the resolution cell of the ship and moves with the wind in one direction. The ship then escapes in another direction. The decoy (chaff cloud) should have a larger radar cross-section (RCS) than the target, so the radar tracks it.
- **Corner reflectors** have the same effect as chaff but are physically very different. Corner reflectors are many-sided objects that re-radiate radar energy mostly back toward its source. An aircraft cannot carry as many corner reflectors as it can chaff.
- **Decoys** are maneuverable flying objects that are intended to deceive a radar operator into believing that they are actually aircraft or missiles. They are especially dangerous because they can clutter up a radar with false targets making it easier for an attacker to get within weapons range and neutralize the radar. Corner reflectors can be fitted on decoys to make them appear larger than they are, thus furthering the illusion that a decoy is an actual aircraft. Some decoys have the capability to perform electronic jamming or drop chaff. Decoys also have a deliberately sacrificial purpose i.e. defenders may fire guided missiles at the decoys, thereby depleting limited stocks of expensive weaponry which might otherwise have been used against genuine targets.

## Electronic jamming

Electronic jamming is a form of electronic warfare where jammers radiate interfering signals toward an enemy's radar, blocking the receiver with highly concentrated energy signals. The two main technique styles are noise techniques and repeater techniques. The three types of noise jamming are spot, sweep, and barrage.

- **Spot jamming** or **spot noise** occurs when a jammer focuses all of its power on a single frequency. This overwhelms the reflection of the original radar signal off the targets, the "skin return" or "skin reflection", making it impossible to pick out the target on the radar display. This technique is only useful against radars that broadcast on a single frequency, and can be countered by changing the frequency or other operational parameters like the pulse repetition frequency (PRF) so the jammer is no longer broadcasting on the same frequency or at the right times. While multiple jammers could possibly jam a range of frequencies, this would consume many resources and be of little effect against modern frequency-agile radars that constantly change their broadcasts.
- **Sweep jamming** is a modification of spot jamming where the jammer's full power is shifted from one frequency to another. While this has the advantage of being able to jam multiple frequencies in quick succession, it does not affect them all at the same time, and thus limits the effectiveness of this type of jamming. Although, depending on the error checking in the device this can render a wide range of devices effectively useless.
- **Barrage jamming** is a further modification of sweep jamming in which the jammer changes frequencies so rapidly it appears to be a constant radiator across its entire bandwidth. The advantage is that multiple frequencies can be jammed essentially simultaneously. The first effective barrage jammer was introduced as the carcinotron in the early 1950s, and was so effective it was believed that all long-range radar systems might be rendered useless. However, the jamming effect can be limited because this requires the jammer to spread its full power between these frequencies—the effectiveness against each frequency decreases with the number of frequencies covered. The creation of extremely powerful multi-frequency radars like Blue Riband offset the effectiveness of the carcinotron.
- **Base jamming** is a new type of barrage jamming whereby one radar is jammed effectively at its source at all frequencies. However, all other radars continue working normally.
- **Pulse jamming** produces noise pulses with period depending on radar mast rotation speed thus creating blocked sectors from directions other than the jammer, making it harder to discover the jammer location.
- **Cover pulse jamming** creates a short noise pulse when radar signal is received thus concealing any aircraft flying behind the jammer with a block of noise.
- **Digital radio frequency memory, or DRFM jamming**, or **Repeater jamming** is a repeater technique that manipulates received radar energy and retransmits it to change the return the radar sees. This technique can change the range the radar detects by changing the delay in transmission of pulses, the velocity the radar detects by changing the Doppler shift of the transmitted signal, or the angle to the plane by using AM techniques to transmit into the sidelobes of the radar. Electronics, radio equipment, and antenna can cause DRFM jamming causing false targets, the signal must be timed after the received radar signal. By analysing received signal strength from side and backlobes and thus getting radar antennae radiation pattern, false targets can be created to directions other than one where the jammer is coming from. If each radar pulse is uniquely coded it is not possible to create targets in directions other than the direction of the jammer.
- **Interrupted-sampling repeater jamming** (ISRJ) provides a coherent-jamming mode against wideband radars. By ISRJ, radar jammers can reduce the sampling rate, and the transmit-receive isolation enable designers to reduce the number of antennas. A single-antenna jammer working under ISRJ mode periodically samples, i.e. interrupted sampling, and repeats a fraction of the intercepted signal. The coherent-jamming signal generated by ISRJ form multiple verisimilar false targets at the victim radar receiver, and some false targets can precede the real target.
- **Deceptive jamming** uses techniques like "range gate pull-off" to break a radar lock.
- **Signature Augmentation** is a technique of a (radar) ECM system to deceive high-resolution radars (HRR) by creating complex false targets that resemble the radar signature of another platform. A specific form of this technique is **Blip enhancement** which deliberately makes some radar returns look larger in order to hide their nature. This is used by escort ships to make them look as large as capital ships.

- (Protective/Standoff jamming) Protective/Standoff jamming
- (Protective/Escort jamming) Protective/Escort jamming

### Noise jamming

Radar noise jamming is when a radar transciever is intentionally flooded with other radar signals as "noise" to make it harder to distinguish real radar transmissions from jamming ones.

${\frac {J}{S}}={\frac {EIRP_{jam}}{EIRP_{radar}}}\times {\frac {4\pi R^{2}}{\sigma }}\times {\frac {BW_{radar}}{BW_{jam}}}$

.

### Radar burn-through

The burn-through range is the distance from the radar at which the jamming is ineffective. When a target is within this range, the radar receives an adequate target skin return to track it. The burn through range is a function of the target RCS (Radar cross-section), jamming ERP (Effective radiated power), the radars ERP and required J/S (for the jamming to be effective).

## Inadvertent jamming

In some cases, jamming of either type may be caused by friendly sources. Inadvertent mechanical jamming is fairly common because it is indiscriminate and affects any nearby radars, hostile or not. Electronic jamming can also be inadvertently caused by friendly sources, usually powerful EW platforms operating within range of the affected radar.

## Countermeasures

Electronic counter-countermeasures (ECCMs) are used to reduce or completely suppress the effects of radar jamming. There are several methods, some of which are listed below as examples:

- Constantly alternating the frequency that the radar operates on (frequency agility) over a spread-spectrum will limit the effectiveness of most jamming, making it easier to read through it. Modern jammers can track a predictable frequency change, so the more random the frequency change, the more likely it is to counter the jammer.
- Cloaking the outgoing signal with random noise makes it more difficult for a jammer to figure out the frequency that a radar is operating on.
- Limiting unsecure radio communication concerning the jamming and its effectiveness is also important. The jammer could be listening, and if they know that a certain technique is effective, they could direct more jamming assets to employ this method.
- The most important method to counter radar jammers is operator training. Any system can be fooled with a jamming signal but a properly trained operator pays attention to the raw video signal and can detect abnormal patterns on the radar screen.
- The best indicator of jamming effectiveness to the jammer is countermeasures taken by the operator. The jammer does not know if their jamming is effective before operator starts changing radar transmission settings.
- Using EW countermeasures will give away radar capabilities thus on peacetime operations most military radars are used on fixed frequencies, at minimal power levels and with blocked Tx sectors toward possible listeners (country borders).
- Mobile fire control radars are usually kept passive when military operations are not ongoing to keep radar locations secret.
- Active electronically scanned array (AESA) radars are innately harder to jam and can operate in low probability of intercept (LPI) modes to reduce the chance that the radar is detected.
- A quantum radar system would automatically detect attempts at deceptive jamming, which might otherwise go unnoticed.
- Anti-radiation missile (ARM) also known as Home-On-Jam (HOJ) missiles: When a target is using self-protective jamming (SPJ), it essentially broadcasts its position. An ARM could be deployed and take out the jamming source. The missile utilizes passive RF homing which reduces its probability of detection. A countermeasure to ARM is not to use SPJ (one could use stand-off jamming, assuming that the missiles has a range no longer than the radar), or have a decoy taking the missile (such as ADM-160 MALD and AN/ALE-55 Fiber-Optic Towed Decoy). By towing a decoy/jammer, the decoy maintains a realistic Doppler shift (which tricks the tracker) and lures an ARM away from the target.

## Stealth

For protective jamming, a small radar cross section $\sigma$ of the protected aircraft will increase the Jam-to-Signal ratio $J/S$ . A lower RCS also reduces the "burn-through" range. Stealth technologies like radiation-absorbent materials can be used to reduce the return of a target.

## Interference

While not usually caused by the enemy, interference can greatly impede the ability of an operator to track. Interference occurs when two radars in relatively close proximity (how close they need to be depends on the power of the radars) are operating on the same frequency. This will cause "running rabbits", a visual phenomenon that can severely clutter up a radar display scope with useless data. Interference is not that common between ground radars, however, because they are not usually placed close enough together. It is more likely that some sort of airborne radar system is inadvertently causing the interference—especially when two or more countries are involved.

The interference between airborne radars referred to above can sometimes (usually) be eliminated by frequency-shifting transmitters.

The other interference often experienced is between the aircraft's own electronic transmitters, i.e. transponders, being picked up by its radar. This interference is eliminated by suppressing the radar's reception for the duration of the transponder's transmission. Instead of "bright-light" rabbits across the display, one would observe very small black dots. Because the external radar causing the transponder to respond is generally not synchronised with your own radar (i.e. different pulse-repetition frequencies), these black dots appear randomly across the display and the operator sees through and around them. The returning image may be much larger than the "dot" or "hole", as it has become known, anyway. Keeping the transponder's pulse widths very narrow and mode of operation (single pulse rather than multi-pulse) becomes a crucial factor.

The external radar could, in theory, come from an aircraft flying alongside your own, or from space. Another factor often overlooked is to reduce the sensitivity of one's own transponder to external radars; i.e., ensure that the transponder's threshold is high. In this way it will only respond to nearby radars—which, after all, should be friendly.

One should also reduce the power output of the transponder in like manner.

## Jamming police radar

Jamming radar for the purpose of defeating police radar guns is more simple than military-grade radar jamming. The laws about jamming police radars vary by jurisdiction.

## Jamming in nature

The jamming of bat sonar by certain tiger moth species has been confirmed. This can be seen as nature's equivalent of radar jamming. Similar to human ECCM techniques, bats are found to change their emission lengths to defeat jamming.
