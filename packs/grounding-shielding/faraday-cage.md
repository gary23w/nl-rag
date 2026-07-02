---
title: "Faraday cage"
source: https://en.wikipedia.org/wiki/Faraday_cage
domain: grounding-shielding
license: CC-BY-SA-4.0
tags: ground loop, Faraday cage, chassis ground, electromagnetic shielding
fetched: 2026-07-02
---

# Faraday cage

A **Faraday cage** or **Faraday shield** is an enclosure used to block some electromagnetic fields. A Faraday shield may be formed by a continuous covering of conductive material, or in the case of a Faraday cage, by a mesh of such materials. Faraday cages are named after the scientist Michael Faraday, who first constructed one in 1836.

Faraday cages work because an external electrical field will cause the electric charges within the cage's conducting material to be distributed in a way that cancels out the field's effect inside the cage. This phenomenon can be used to protect sensitive electronic equipment (for example RF receivers) from external radio frequency interference (RFI), often during testing or alignment of the device. Faraday cages are also used to protect people and equipment against electric currents such as lightning strikes and electrostatic discharges, because the cage conducts electrical current around the outside of the enclosed space and none passes through the interior.

Faraday cages cannot block stable or slowly varying magnetic fields, such as the Earth's magnetic field (a compass will still work inside one). To a large degree, however, they shield the interior from external electromagnetic radiation if the conductor is thick enough and any hole is significantly smaller than the wavelength of the radiation. For example, certain computer forensic electronic systems test procedures that require an electromagnetic interference free environment can be carried out within a screened room. These rooms are spaces that are completely enclosed by one or more layers of a fine metal mesh or perforated sheet metal. The metal layers are grounded to dissipate any electric currents generated from external or internal electromagnetic fields, and thus they block a large amount of the electromagnetic interference (see also electromagnetic shielding). They provide less attenuation of outgoing transmissions than incoming: they can block electromagnetic pulse (EMP) waves from natural phenomena very effectively, but especially in upper frequencies, a tracking device may be able to penetrate from within the cage (e.g., some cell phones operate at various radio frequencies, so while one frequency may not work, another one will).

The reception or transmission of radio waves, a form of electromagnetic radiation, to or from an antenna within a Faraday cage is heavily attenuated or blocked by the cage; however, a Faraday cage has varied attenuation depending on wave form, frequency, or the distance from receiver or transmitter, and receiver or transmitter power. Near-field, high-powered frequency transmissions like HF RFID are more likely to penetrate. Solid cages generally attenuate fields over a broader frequency range than mesh cages.

## History

In 1754, Jean-Antoine Nollet published an account of the cage effect in his *Leçons de physique expérimentale*.

In 1755, Benjamin Franklin observed the effect by lowering an uncharged cork ball suspended on a silk thread through an opening in an electrically charged metal can. The behavior is that of a Faraday cage or shield.

In 1836, Michael Faraday observed that the excess charge on a charged conductor resided only on its exterior and had no influence on anything enclosed within it. To demonstrate this, he built a metal foil-coated room and allowed high-voltage discharges from an electrostatic generator to strike the outside of the room. He used an electroscope to show that there was no electric charge present on the inside of the room walls.

## Operation

### Continuous

A continuous Faraday shield is a hollow conductor. Externally or internally applied electromagnetic fields produce forces on the charge carriers (usually electrons) within the conductor; the charges are redistributed accordingly due to electrostatic induction. The redistributed charges greatly reduce the voltage within the surface, to an extent depending on the capacitance; however, full cancellation does not occur.

#### Interior charges

If charge $+Q$ is placed inside an ungrounded Faraday shield without touching the walls, the internal face of the shield becomes charged with $-Q$ , leading to field lines originating at the charge and extending to charges inside the inner surface of the metal. The field line paths in this inside space (to the endpoint negative charges) are dependent on the shape of the inner containment walls. Simultaneously $+Q$ accumulates on the outer face of the shield. The spread of charges on the outer face is not affected by the position of the internal charge inside the enclosure, but rather determined by the shape of the outer face. So for all intents and purposes, the Faraday shield generates the same static electric field on the outside that it would generate if the metal were simply charged with $+Q$ . See Faraday's ice pail experiment, for example, for more details on electric field lines and the decoupling of the outside from the inside. Note that electromagnetic waves are not static charges.

If the cage is grounded, the excess charges will be neutralized as the ground connection creates an equipotential bonding between the outside of the cage and the environment, so there is no voltage between them and therefore also no field. The inner face and the inner charge will remain the same, so the field is kept inside.

#### Exterior fields

Static electric shielding effectiveness is largely independent of the geometry of the conductive material; however, the static magnetic fields can penetrate the shield completely.

In the case of varying electromagnetic fields, the faster the variations are (i.e., the higher the frequencies), the better the material resists magnetic field penetration. In this case, the shielding also depends on the electrical conductivity, the magnetic properties of the conductive materials used in the cages, as well as their thicknesses.

A good example of the effectiveness of a Faraday shield can be obtained from considerations of skin depth. With skin depth, the current flowing is mostly on the surface and decays exponentially with depth through the material. Because a Faraday shield has finite thickness, this determines how well the shield works; a thicker shield can attenuate electromagnetic fields better, and to a lower frequency.

### Faraday cage

Faraday cages are Faraday shields that have holes in them and are therefore more complex to analyze. Whereas continuous shields essentially attenuate all wavelengths whose skin depth in the hull material is less than the thickness of the hull, the holes in a cage may permit shorter wavelengths to pass through or set up "evanescent fields" (oscillating fields that do not propagate as EM waves) just beyond the surface. The shorter the wavelength, the better it passes through a mesh of a given size. Thus, to work well at short wavelengths (i.e., high frequencies), the holes in the cage must be smaller than the wavelength of the incident wave.

## Examples

- Faraday cages are routinely used in analytical chemistry to reduce noise while making sensitive measurements.
- Faraday cages, more specifically dual-paired seam Faraday bags, are often used in digital forensics to prevent remote wiping and alteration of criminal digital evidence.
- Faraday bags are shielded security bags fabricated with metallic materials that are used to contain devices to protect them from electromagnetic transmissions for a wide range of applications, from enhancing digital privacy of cell telephones to protecting credit cards from RFID skimming.
- The U.S. and NATO Tempest standards, and similar standards in other countries, include Faraday cages as part of a broader effort to provide emission security for computers.
- Automobile and airplane passenger compartments are essentially Faraday cages, protecting passengers from electric charges, such as lightning.
- Electronic components in automobiles and aircraft use Faraday cages to protect signals from interference. Sensitive components may include wireless door locks, navigation/GPS systems, and lane departure warning systems. Faraday cages and shields are also critical to vehicle infotainment systems (e.g., radio, Wi-Fi, and GPS display units), which may be designed with the capability to function as critical circuits in emergencies.
- A booster bag (shopping bag lined with aluminum foil) acts as a Faraday cage. It is often used by shoplifters to steal RFID-tagged items. Similar containers are used to resist RFID skimming.
- Elevators and other rooms with metallic conducting frames and walls simulate a Faraday cage effect, leading to a loss of signal and "dead zones" for users of cellular phones, radios, and other electronic devices that require external electromagnetic signals. During training, firefighters and other first responders are cautioned that their two-way radios will probably not work inside elevators and to make allowances for that.
- Electronics engineers use small, physical Faraday cages during equipment testing to simulate such an environment to make sure that the device gracefully handles these conditions.
- Properly designed conductive clothing can also form a protective Faraday cage. Some electrical linemen wear Faraday suits, which allow them to work on live, high-voltage power lines without risk of electrocution. The suit prevents electric current from flowing through the body, and it has no theoretical voltage limit. Linemen have successfully worked even the highest voltage (Kazakhstan's Ekibastuz–Kokshetau line 1150 kV) lines safely.
- The scan room of a magnetic resonance imaging (MRI) machine is designed as a Faraday cage. This prevents external RF (radio frequency) signals from being added to data collected from the patient, which would affect the resulting image. Technologists are trained to identify the characteristic artifacts created on images should the Faraday cage be damaged, such as during a thunderstorm.
- A microwave oven uses a partial Faraday shield (on five of its interior six sides) and a partial Faraday cage, consisting of a wire mesh, on the sixth side (the transparent window), to contain the electromagnetic energy within the oven and to protect the user from exposure to microwave radiation.
- Plastic bags that are impregnated with metal are used to enclose electronic toll collection devices whenever tolls should not be charged to those devices, such as during transit or when the user is paying cash.
- The shield of a screened cable, such as USB cables or the coaxial cable used for cable television, protects the internal conductors from external electrical noise and prevents the RF signals from leaking out.
- Electronic components in some music instruments, such as in an electric guitar, are protected by Faraday cages made from copper or aluminum foils that protect the instrument's electromagnetic pickups from interference from speakers, amplifiers, stage lights, and other musical equipment.
- Some buildings, such as prisons, are constructed as a Faraday cage because they have reasons to block both incoming and outgoing cell phone calls by prisoners.
- The exhibit hall of the Green Bank Observatory is a Faraday cage to prevent interference with the operations of their radio telescopes.
