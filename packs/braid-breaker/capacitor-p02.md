---
title: "Capacitor (part 2/2)"
source: https://en.wikipedia.org/wiki/Capacitor
domain: braid-breaker
license: CC-BY-SA-4.0
tags: braid-breaker
fetched: 2026-07-03
part: 2/2
---

## Capacitor types

Practical capacitors are available commercially in many different forms. The type of internal dielectric, the structure of the plates and the device packaging all strongly affect the characteristics of the capacitor, and its applications.

Values available range from very low (picofarad range; while arbitrarily low values are in principle possible, stray (parasitic) capacitance in any circuit is the limiting factor) to about 5 kF supercapacitors.

Above approximately 1 microfarad electrolytic capacitors are usually used because of their small size and low cost compared with other types, unless their relatively poor stability, life and polarised nature make them unsuitable. Very high capacity supercapacitors use a porous carbon-based electrode material.

### Dielectric materials

Most capacitors have a dielectric spacer, which increases their capacitance compared to air or a vacuum. In order to maximise the charge that a capacitor can hold, the dielectric material needs to have as high a permittivity as possible, while also having as high a breakdown voltage as possible. The dielectric also needs to have as low a loss with frequency as possible.

However, low value capacitors are available with a high vacuum between their plates to allow extremely high voltage operation and low losses. Variable capacitors with their plates open to the atmosphere were commonly used in radio tuning circuits. Later designs use polymer foil dielectric between the moving and stationary plates, with no significant air space between the plates.

Several solid dielectrics are available, including paper, plastic, glass, mica and ceramic.

Paper was used extensively in older capacitors and offers relatively high voltage performance. However, paper absorbs moisture, and has been largely replaced by plastic film capacitors.

Most of the plastic films now used offer better stability and ageing performance than such older dielectrics such as oiled paper, which makes them useful in timer circuits, although they may be limited to relatively low operating temperatures and frequencies, because of the limitations of the plastic film being used. Large plastic film capacitors are used extensively in suppression circuits, motor start circuits, and power-factor correction circuits.

Ceramic capacitors are generally small, cheap and useful for high frequency applications, although their capacitance varies strongly with voltage and temperature and they age poorly. They can also suffer from the piezoelectric effect. Ceramic capacitors are broadly categorized as class 1 dielectrics, which have predictable variation of capacitance with temperature or class 2 dielectrics, which can operate at higher voltage. Modern multilayer ceramics are usually quite small, but some types have inherently wide value tolerances, microphonic issues, and are usually physically brittle.

Glass and mica capacitors are extremely reliable, stable and tolerant to high temperatures and voltages, but are too expensive for most mainstream applications.

Electrolytic capacitors and supercapacitors are used to store small and larger amounts of energy, respectively, ceramic capacitors are often used in resonators, and parasitic capacitance occurs in circuits wherever the simple conductor-insulator-conductor structure is formed unintentionally by the configuration of the circuit layout.

Electrolytic capacitors use an aluminum or tantalum plate with an oxide dielectric layer. The second electrode is a liquid electrolyte, connected to the circuit by another foil plate. Electrolytic capacitors offer very high capacitance but suffer from poor tolerances, high instability, gradual loss of capacitance especially when subjected to heat, and high leakage current. Poor quality capacitors may leak electrolyte, which is harmful to printed circuit boards. The conductivity of the electrolyte drops at low temperatures, which increases equivalent series resistance. While widely used for power-supply conditioning, poor high-frequency characteristics make them unsuitable for many applications. Electrolytic capacitors suffer from self-degradation if unused for a period (around a year), and when full power is applied may short circuit, permanently damaging the capacitor and usually blowing a fuse or causing failure of rectifier diodes. For example, in older equipment, this may cause arcing in rectifier tubes. They can be restored before use by gradually applying the operating voltage, often performed on antique vacuum tube equipment over a period of thirty minutes by using a variable transformer to supply AC power. The use of this technique may be less satisfactory for some solid state equipment, which may be damaged by operation below its normal power range, requiring that the power supply first be isolated from the consuming circuits. Such remedies may not be applicable to modern high-frequency power supplies as these produce full output voltage even with reduced input.

Tantalum capacitors offer better frequency and temperature characteristics than aluminum, but higher dielectric absorption and leakage.

Polymer capacitors (OS-CON, OC-CON, KO, AO) use solid conductive polymer (or polymerized organic semiconductor) as electrolyte and offer longer life and lower ESR at higher cost than standard electrolytic capacitors.

A feedthrough capacitor is a component that, while not serving as its main use, has capacitance and is used to conduct signals through a conductive sheet.

Several other types of capacitor are available for specialist applications. Supercapacitors store large amounts of energy. Supercapacitors made from carbon aerogel, carbon nanotubes, or highly porous electrode materials, offer extremely high capacitance (up to 5 kF as of 2010) and can be used in some applications instead of rechargeable batteries. Alternating current capacitors are specifically designed to work on line (mains) voltage AC power circuits. They are commonly used in electric motor circuits and are often designed to handle large currents, so they tend to be physically large. They are usually ruggedly packaged, often in metal cases that can be easily grounded/earthed. They also are designed with direct current breakdown voltages of at least five times the maximum AC voltage.

### Voltage-dependent capacitors

The dielectric constant for a number of very useful dielectrics changes as a function of the applied electrical field, for example ferroelectric materials, so the capacitance for these devices is more complex. For example, in charging such a capacitor the differential increase in voltage with charge is governed by: $\mathop {} \!\mathrm {d} Q=C(V)\mathop {} \!\mathrm {d} V$ where the voltage dependence of capacitance, *C*(*V*), suggests that the capacitance is a function of the electric field strength, which in a large area parallel plate device is given by *ε* = *V*/*d*. This field polarizes the dielectric, which polarization, in the case of a ferroelectric, is a nonlinear *S*-shaped function of the electric field, which, in the case of a large area parallel plate device, translates into a capacitance that is a nonlinear function of the voltage.

Corresponding to the voltage-dependent capacitance, to charge the capacitor to voltage V an integral relation is found: $Q=\int _{0}^{V}C(V)\mathop {} \!\mathrm {d} V$ which agrees with *Q* = *CV* only when C does not depend on voltage V.

By the same token, the energy stored in the capacitor now is given by $\mathop {} \!\mathrm {d} W=Q\mathop {} \!\mathrm {d} V=\left[\int _{0}^{V}\mathop {} \!\mathrm {d} V'\,C(V')\right]\mathop {} \!\mathrm {d} V.$

Integrating: $W=\int _{0}^{V}\mathop {} \!\mathrm {d} V\int _{0}^{V}\mathop {} \!\mathrm {d} V'\,C(V')=\int _{0}^{V}\mathop {} \!\mathrm {d} V'\int _{V'}^{V}\mathop {} \!\mathrm {d} V\,C(V')=\int _{0}^{V}\mathop {} \!\mathrm {d} V'\left(V-V'\right)C(V'),$ where interchange of the order of integration is used.

The nonlinear capacitance of a microscope probe scanned along a ferroelectric surface is used to study the domain structure of ferroelectric materials.

Another example of voltage dependent capacitance occurs in semiconductor devices such as semiconductor diodes, where the voltage dependence stems not from a change in dielectric constant but in a voltage dependence of the spacing between the charges on the two sides of the capacitor. This effect is intentionally exploited in diode-like devices known as varicaps.

### Frequency-dependent capacitors

If a capacitor is driven with a time-varying voltage that changes rapidly enough, at some frequency the polarization of the dielectric cannot follow the voltage. As an example of the origin of this mechanism, the internal microscopic dipoles contributing to the dielectric constant cannot move instantly, and so as frequency of an applied alternating voltage increases, the dipole response is limited and the dielectric constant diminishes. A changing dielectric constant with frequency is referred to as dielectric dispersion, and is governed by dielectric relaxation processes, such as Debye relaxation. Under transient conditions, the displacement field can be expressed as (see electric susceptibility): ${\boldsymbol {D(t)}}=\varepsilon _{0}\int _{-\infty }^{t}\varepsilon _{r}(t-t'){\boldsymbol {E}}(t')\,\mathop {} \!\mathrm {d} t',$

indicating the lag in response by the time dependence of *εr*, calculated in principle from an underlying microscopic analysis, for example, of the dipole behavior in the dielectric. See, for example, linear response function. The integral extends over the entire past history up to the present time. A Fourier transform in time then results in: ${\boldsymbol {D}}(\omega )=\varepsilon _{0}\varepsilon _{r}(\omega ){\boldsymbol {E}}(\omega )\,,$

where *ε*r(*ω*) is now a complex function, with an imaginary part related to absorption of energy from the field by the medium. See permittivity. The capacitance, being proportional to the dielectric constant, also exhibits this frequency behavior. Fourier transforming Gauss's law with this form for displacement field:

${\begin{aligned}I(\omega )&=j\omega Q(\omega )=j\omega \oint _{\Sigma }{\boldsymbol {D}}({\boldsymbol {r}},\omega )\cdot \mathop {} \!\mathrm {d} {\boldsymbol {\Sigma }}\\&=\left[G(\omega )+j\omega C(\omega )\right]V(\omega )={\frac {V(\omega )}{Z(\omega )}}\,,\end{aligned}}$ where *j* is the imaginary unit, *V*(*ω*) is the voltage component at angular frequency ω, *G*(*ω*) is the *real* part of the current, called the *conductance*, and *C*(*ω*) determines the *imaginary* part of the current and is the *capacitance*. *Z*(*ω*) is the complex impedance.

When a parallel-plate capacitor is filled with a dielectric, the measurement of dielectric properties of the medium is based upon the relation: $\varepsilon _{r}(\omega )=\varepsilon '_{r}(\omega )-j\varepsilon ''_{r}(\omega )={\frac {1}{j\omega Z(\omega )C_{0}}}={\frac {C_{\text{cmplx}}(\omega )}{C_{0}}}\,,$ where a single *prime* denotes the real part and a double *prime* the imaginary part, *Z*(*ω*) is the complex impedance with the dielectric present, *C*cmplx(*ω*) is the so-called *complex* capacitance with the dielectric present, and *C*0 is the capacitance without the dielectric. (Measurement "without the dielectric" in principle means measurement in free space, an unattainable goal inasmuch as even the quantum vacuum is predicted to exhibit nonideal behavior, such as dichroism. For practical purposes, when measurement errors are taken into account, often a measurement in terrestrial vacuum, or simply a calculation of *C*0, is sufficiently accurate.)

Using this measurement method, the dielectric constant may exhibit a resonance at certain frequencies corresponding to characteristic response frequencies (excitation energies) of contributors to the dielectric constant. These resonances are the basis for a number of experimental techniques for detecting defects. The *conductance method* measures absorption as a function of frequency. Alternatively, the time response of the capacitance can be used directly, as in *deep-level transient spectroscopy*.

Another example of frequency dependent capacitance occurs with MOS capacitors, where the slow generation of minority carriers means that at high frequencies the capacitance measures only the majority carrier response, while at low frequencies both types of carrier respond.

At optical frequencies, in semiconductors the dielectric constant exhibits structure related to the band structure of the solid. Sophisticated modulation spectroscopy measurement methods based upon modulating the crystal structure by pressure or by other stresses and observing the related changes in absorption or reflection of light have advanced our knowledge of these materials.

### Styles

The arrangement of plates and dielectric has many variations in different styles depending on the desired ratings of the capacitor. For small values of capacitance (microfarads and less), ceramic disks use metallic coatings, with wire leads bonded to the coating. Larger values can be made by multiple stacks of plates and disks. Larger value capacitors usually use a metal foil or metal film layer deposited on the surface of a dielectric film to make the plates, and a dielectric film of impregnated paper or plastic – these are rolled up to save space. To reduce the series resistance and inductance for long plates, the plates and dielectric are staggered so that connection is made at the common edge of the rolled-up plates, not at the ends of the foil or metalized film strips that comprise the plates.

The assembly is encased to prevent moisture entering the dielectric – early radio equipment used a cardboard tube sealed with wax. Modern paper or film dielectric capacitors are dipped in a hard thermoplastic. Large capacitors for high-voltage use may have the roll form compressed to fit into a rectangular metal case, with bolted terminals and bushings for connections. The dielectric in larger capacitors is often impregnated with a liquid to improve its properties.

Capacitors may have their connecting leads arranged in many configurations, for example axially or radially. "Axial" means that the leads are on a common axis, typically the axis of the capacitor's cylindrical body – the leads extend from opposite ends. Radial leads are rarely aligned along radii of the body's circle, so the term is conventional. The leads (until bent) are usually in planes parallel to that of the flat body of the capacitor, and extend in the same direction; they are often parallel as manufactured.

Small, cheap discoidal ceramic capacitors have existed from the 1930s onward, and remain in widespread use. After the 1980s, surface mount packages for capacitors have been widely used. These packages are extremely small and lack connecting leads, allowing them to be soldered directly onto the surface of printed circuit boards. Surface mount components avoid undesirable high-frequency effects due to the leads and simplify automated assembly, although manual handling is made difficult due to their small size.

Mechanically controlled variable capacitors allow the plate spacing to be adjusted, for example by rotating or sliding a set of movable plates into alignment with a set of stationary plates. Low cost variable capacitors squeeze together alternating layers of aluminum and plastic with a screw. Electrical control of capacitance is achievable with varactors (or varicaps), which are reverse-biased semiconductor diodes whose depletion region width varies with applied voltage. They are used in phase-locked loops, amongst other applications.


## Capacitor markings

### Marking codes for larger parts

Most capacitors have designations printed on their bodies to indicate their electrical characteristics. Larger capacitors, such as electrolytic types usually display the capacitance as value with explicit unit, for example, *220 μF*.

For typographical reasons, some manufacturers print *MF* on capacitors to indicate microfarads (μF).

### Three-/four-character marking code for small capacitors

Smaller capacitors, such as ceramic types, often use a shorthand-notation consisting of three digits and an optional letter, where the digits (*XYZ*) denote the capacitance in picofarad (pF), calculated as *XY* × 10*Z*, and the letter indicating the tolerance. Common tolerances are ±5%, ±10%, and ±20%, denoted as J, K, and M, respectively.

A capacitor may also be labeled with its working voltage, temperature, and other relevant characteristics.

Example: A capacitor labeled or designated as *473K 330V* has a capacitance of 47×103 pF = 47 nF (±10%) with a maximum working voltage of 330 V. The working voltage of a capacitor is nominally the highest voltage that may be applied across it without undue risk of breaking down the dielectric layer.

### Two-character marking code for small capacitors

For capacitances following the E3, E6, E12 or E24 series of preferred values, the former ANSI/EIA-198-D:1991, ANSI/EIA-198-1-E:1998 and ANSI/EIA-198-1-F:2002 as well as the amendment IEC 60062:2016/AMD1:2019 to IEC 60062 define a *special two-character marking code for capacitors* for very small parts which leave no room to print the above-mentioned three-/four-character code onto them. The code consists of an uppercase letter denoting the two significant digits of the value followed by a digit indicating the multiplier. The EIA standard also defines a number of lowercase letters to specify a number of values not found in E24.

Code

Series

Digit

Letter

E24

9

0

1

2

3

4

5

6

7

8

A

1.0

0.10

pF

1.0

pF

10

pF

100

pF

1.0

nF

10

nF

100

nF

1.0

μF

10

μF

100

μF

B

1.1

0.11

pF

1.1

pF

11

pF

110

pF

1.1

nF

11

nF

110

nF

1.1

μF

11

μF

110

μF

C

1.2

0.12

pF

1.2

pF

12

pF

120

pF

1.2

nF

12

nF

120

nF

1.2

μF

12

μF

120

μF

D

1.3

0.13

pF

1.3

pF

13

pF

130

pF

1.3

nF

13

nF

130

nF

1.3

μF

13

μF

130

μF

E

1.5

0.15

pF

1.5

pF

15

pF

150

pF

1.5

nF

15

nF

150

nF

1.5

μF

15

μF

150

μF

F

1.6

0.16

pF

1.6

pF

16

pF

160

pF

1.6

nF

16

nF

160

nF

1.6

μF

16

μF

160

μF

G

1.8

0.18

pF

1.8

pF

18

pF

180

pF

1.8

nF

18

nF

180

nF

1.8

μF

18

μF

180

μF

H

2.0

0.20

pF

2.0

pF

20

pF

200

pF

2.0

nF

20

nF

200

nF

2.0

μF

20

μF

200

μF

J

2.2

0.22

pF

2.2

pF

22

pF

220

pF

2.2

nF

22

nF

220

nF

2.2

μF

22

μF

220

μF

K

2.4

0.24

pF

2.4

pF

24

pF

240

pF

2.4

nF

24

nF

240

nF

2.4

μF

24

μF

240

μF

L

2.7

0.27

pF

2.7

pF

27

pF

270

pF

2.7

nF

27

nF

270

nF

2.7

μF

27

μF

270

μF

M

3.0

0.30

pF

3.0

pF

30

pF

300

pF

3.0

nF

30

nF

300

nF

3.0

μF

30

μF

300

μF

N

3.3

0.33

pF

3.3

pF

33

pF

330

pF

3.3

nF

33

nF

330

nF

3.3

μF

33

μF

330

μF

P

3.6

0.36

pF

3.6

pF

36

pF

360

pF

3.6

nF

36

nF

360

nF

3.6

μF

36

μF

360

μF

Q

3.9

0.39

pF

3.9

pF

39

pF

390

pF

3.9

nF

39

nF

390

nF

3.9

μF

39

μF

390

μF

R

4.3

0.43

pF

4.3

pF

43

pF

430

pF

4.3

nF

43

nF

430

nF

4.3

μF

43

μF

430

μF

S

4.7

0.47

pF

4.7

pF

47

pF

470

pF

4.7

nF

47

nF

470

nF

4.7

μF

47

μF

470

μF

T

5.1

0.51

pF

5.1

pF

51

pF

510

pF

5.1

nF

51

nF

510

nF

5.1

μF

51

μF

510

μF

U

5.6

0.56

pF

5.6

pF

56

pF

560

pF

5.6

nF

56

nF

560

nF

5.6

μF

56

μF

560

μF

V

6.2

0.62

pF

6.2

pF

62

pF

620

pF

6.2

nF

62

nF

620

nF

6.2

μF

62

μF

620

μF

W

6.8

0.68

pF

6.8

pF

68

pF

680

pF

6.8

nF

68

nF

680

nF

6.8

μF

68

μF

680

μF

X

7.5

0.75

pF

7.5

pF

75

pF

750

pF

7.5

nF

75

nF

750

nF

7.5

μF

75

μF

750

μF

Y

8.2

0.82

pF

8.2

pF

82

pF

820

pF

8.2

nF

82

nF

820

nF

8.2

μF

82

μF

820

μF

Z

9.1

0.91

pF

9.1

pF

91

pF

910

pF

9.1

nF

91

nF

910

nF

9.1

μF

91

μF

910

μF

Code

Series

Digit

Letter

EIA

9

0

1

2

3

4

5

6

7

8

a

2.5

0.25

pF

2.5

pF

25

pF

250

pF

2.5

nF

25

nF

250

nF

2.5

μF

25

μF

250

μF

b?

3.0?

0.30

pF

3.0

pF

30

pF

300

pF

3.0

nF

30

nF

300

nF

3.0

μF

30

μF

300

μF

b?

/c?

3.5

0.35

pF

3.5

pF

35

pF

350

pF

3.5

nF

35

nF

350

nF

3.5

μF

35

μF

350

μF

d

4.0

0.40

pF

4.0

pF

40

pF

400

pF

4.0

nF

40

nF

400

nF

4.0

μF

40

μF

400

μF

e

4.5

0.45

pF

4.5

pF

45

pF

450

pF

4.5

nF

45

nF

450

nF

4.5

μF

45

μF

450

μF

f

5.0

0.50

pF

5.0

pF

50

pF

500

pF

5.0

nF

50

nF

500

nF

5.0

μF

50

μF

500

μF

m

6.0

0.60

pF

6.0

pF

60

pF

600

pF

6.0

nF

60

nF

600

nF

6.0

μF

60

μF

600

μF

n

7.0

0.70

pF

7.0

pF

70

pF

700

pF

7.0

nF

70

nF

700

nF

7.0

μF

70

μF

700

μF

t

8.0

0.80

pF

8.0

pF

80

pF

800

pF

8.0

nF

80

nF

800

nF

8.0

μF

80

μF

800

μF

g

9.0

0.90

pF

9.0

pF

90

pF

900

pF

9.0

nF

90

nF

900

nF

9.0

μF

90

μF

900

μF

### RKM code

The RKM code following IEC 60062 and BS 1852 is a notation to state a capacitor's value in a circuit diagram. It avoids using a decimal separator and replaces the decimal separator with the SI prefix symbol for the particular value (and the letter F for weight 1). The code is also used for part markings. Example: 4n7 for 4.7 nF or 2F2 for 2.2 F.

### Historical

In texts prior to the 1960s and on some capacitor packages until more recently, obsolete capacitance units were utilized in electronic books, magazines, and electronics catalogs. The old units "mfd" and "mf" meant *microfarad* (μF); and the old units "mmfd", "mmf", "uuf", "μμf", "pfd" meant *picofarad* (pF); but they are rarely used any more. Also, "Micromicrofarad" or "micro-microfarad" are obsolete units that are found in some older texts that is equivalent to *picofarad* (pF).

Summary of obsolete capacitance units: (upper/lower case variations are not shown)

- μF (microfarad) = mf, mfd
- pF (picofarad) = mmf, mmfd, pfd, μμF


## Applications

### Energy storage

A capacitor can store electric energy when disconnected from its charging circuit, so it can be used like a temporary battery, or like other types of rechargeable energy storage system. Capacitors are commonly used in electronic devices to maintain power supply while batteries are being changed. (This prevents loss of information in volatile memory.)

A capacitor can facilitate conversion of kinetic energy of charged particles into electric energy and store it.

There are tradeoffs between capacitors and batteries as storage devices. Without external resistors or inductors, capacitors can generally release their stored energy in a very short time compared to batteries. Conversely, batteries can hold a far greater charge per their size. Conventional capacitors provide less than 360 joules per kilogram of specific energy, whereas a conventional alkaline battery has a density of 590 kJ/kg. There is an intermediate solution: supercapacitors, which can accept and deliver charge much faster than batteries, and tolerate many more charge and discharge cycles than rechargeable batteries. They are, however, 10 times larger than conventional batteries for a given charge. On the other hand, it has been shown that the amount of charge stored in the dielectric layer of the thin film capacitor can be equal to, or can even exceed, the amount of charge stored on its plates.

In car audio systems, large capacitors store energy for the amplifier to use on demand. Also, for a flash tube, a capacitor is used to hold the high voltage.

### Digital memory

In the 1930s, John Atanasoff applied the principle of energy storage in capacitors to construct dynamic digital memories for the first binary computers that used electron tubes for logic.

### Pulsed power and weapons

Pulsed power is used in many applications to increase the power intensity (watts) of a volume of energy (joules) by releasing that volume within a very short time. Pulses in the nanosecond range and powers in the gigawatts are achievable. Short pulses often require specially constructed, low-inductance, high-voltage capacitors that are often used in large groups (*capacitor banks*) to supply huge pulses of current for many pulsed power applications. These include electromagnetic forming, Marx generators, pulsed lasers (especially TEA lasers), pulse forming networks, radar, fusion research, and particle accelerators.

Large capacitor banks (reservoir) are used as energy sources for the exploding-bridgewire detonators or slapper detonators in nuclear weapons and other specialty weapons. Experimental work is under way using banks of capacitors as power sources for electromagnetic armour and electromagnetic railguns and coilguns.

### Power conditioning

Reservoir capacitors are used in power supplies where they smooth the output of a full or half wave rectifier. They can also be used in charge pump circuits as the energy storage element in the generation of higher voltages than the input voltage.

Capacitors are connected in parallel with the power circuits of most electronic devices and larger systems (such as factories) to shunt away and conceal current fluctuations from the primary power source to provide a "clean" power supply for signal or control circuits. Audio equipment, for example, uses several capacitors in this way, to shunt away power line hum before it gets into the signal circuitry. The capacitors act as a local reserve for the DC power source, and bypass AC currents from the power supply. This is used in car audio applications, when a stiffening capacitor compensates for the inductance and resistance of the leads to the lead–acid car battery.

#### Power-factor correction

In electric power distribution, capacitors are used for power-factor correction. Such capacitors often come as three capacitors connected as a three phase load. Usually, the values of these capacitors are not given in farads but rather as a reactive power in volt-amperes reactive (var). The purpose is to counteract inductive loading from devices like electric motors and transmission lines to make the load appear to be mostly resistive. Individual motor or lamp loads may have capacitors for power-factor correction, or larger sets of capacitors (usually with automatic switching devices) may be installed at a load center within a building or in a large utility substation.

### Suppression and coupling

#### Signal coupling

Because capacitors pass AC but block DC signals (when charged up to the applied DC voltage), they are often used to separate the AC and DC components of a signal. This method is known as *AC coupling* or "capacitive coupling". Here, a large value of capacitance, whose value need not be accurately controlled, but whose reactance is small at the signal frequency, is employed.

#### Decoupling

A decoupling capacitor is a capacitor used to protect one part of a circuit from the effect of another, for instance to suppress noise or transients. Noise caused by other circuit elements is shunted through the capacitor, reducing the effect they have on the rest of the circuit. It is most commonly used between the power supply and ground. An alternative name is *bypass capacitor* as it is used to bypass the power supply or other high impedance component of a circuit.

Decoupling capacitors need not always be discrete components. Capacitors used in these applications may be built into a printed circuit board, between the various layers. These are often referred to as embedded capacitors. The layers in the board contributing to the capacitive properties also function as power and ground planes, and have a dielectric in between them, enabling them to operate as a parallel plate capacitor.

#### High-pass and low-pass filters

#### Noise suppression, spikes, and snubbers

When an inductive circuit is opened, the current through the inductance collapses quickly, creating a large voltage across the open circuit of the switch or relay. If the inductance is large enough, the energy may generate a spark, causing the contact points to oxidize, deteriorate, or sometimes weld together, or destroying a solid-state switch. A snubber capacitor across the newly opened circuit creates a path for this impulse to bypass the contact points, thereby preserving their life; these were commonly found in contact breaker ignition systems, for instance. Similarly, in smaller scale circuits, the spark may not be enough to damage the switch but may still radiate undesirable radio frequency interference (RFI), which a filter capacitor absorbs. Snubber capacitors are usually employed with a low-value resistor in series, to dissipate energy and minimize RFI. Such resistor-capacitor combinations are available in a single package.

Capacitors are also used in parallel with interrupting units of a high-voltage circuit breaker to equally distribute the voltage between these units. These are called "grading capacitors".

In schematic diagrams, a capacitor used primarily for DC charge storage is often drawn vertically in circuit diagrams with the lower, more negative, plate drawn as an arc. The straight plate indicates the positive terminal of the device, if it is polarized (see electrolytic capacitor).

### Motor starters

In single phase squirrel cage motors, the primary winding within the motor housing is not capable of starting a rotational motion on the rotor, but is capable of sustaining one. To start the motor, a secondary "start" winding has a series non-polarized *starting capacitor* to introduce a lead in the sinusoidal current. When the secondary (start) winding is placed at an angle with respect to the primary (run) winding, a rotating electric field is created. The force of the rotational field is not constant, but is sufficient to start the rotor spinning. When the rotor comes close to operating speed, a centrifugal switch (or current-sensitive relay in series with the main winding) disconnects the capacitor. The start capacitor is typically mounted to the side of the motor housing. These are called capacitor-start motors, that have relatively high starting torque. Typically they can have up-to four times as much starting torque as a split-phase motor and are used on applications such as compressors, pressure washers and any small device requiring high starting torques.

Capacitor-run induction motors have a permanently connected phase-shifting capacitor in series with a second winding. The motor is much like a two-phase induction motor.

Motor-starting capacitors are typically non-polarized electrolytic types, while running capacitors are conventional paper or plastic film dielectric types.

### Signal processing

The energy stored in a capacitor can be used to represent information, either in binary form, as in DRAMs, or in analogue form, as in analog sampled filters and CCDs. Capacitors can be used in analog circuits as components of integrators or more complex filters and in negative feedback loop stabilization. Signal processing circuits also use capacitors to integrate a current signal.

#### Tuned circuits

Capacitors and inductors are applied together in tuned circuits to select information in particular frequency bands. For example, radio receivers rely on variable capacitors to tune the station frequency. Speakers use passive analog crossovers, and analog equalizers use capacitors to select different audio bands.

The resonant frequency *f* of a tuned circuit is a function of the inductance (*L*) and capacitance (*C*) in series, and is given by: $f={\frac {1}{2\pi {\sqrt {LC}}}}$ where L is in henries and C is in farads.

### Sensing

Most capacitors are designed to maintain a fixed physical structure. However, various factors can change the structure of the capacitor, and the resulting change in capacitance can be used to sense those factors.

**Changing the dielectric**

The effects of varying the characteristics of the

dielectric

can be used for sensing purposes. Capacitors with an exposed and porous dielectric can be used to measure humidity in air. Capacitors are used to accurately measure the fuel level in

airplanes

; as the fuel covers more of a pair of plates, the circuit capacitance increases. Squeezing the dielectric can change a capacitor at a few tens of bar pressure sufficiently that it can be used as a pressure sensor.

A selected, but otherwise standard, polymer dielectric capacitor, when immersed in a compatible gas or liquid, can work usefully as a very low cost pressure sensor up to many hundreds of bar.

**Changing the distance between the plates**

Capacitors with a flexible plate can be used to measure strain or pressure. Industrial pressure transmitters used for

process control

use pressure-sensing diaphragms, which form a capacitor plate of an oscillator circuit. Capacitors are used as the

sensor

in

condenser microphones

, where one plate is moved by air pressure, relative to the fixed position of the other plate. Some

accelerometers

use

MEMS

capacitors etched on a chip to measure the magnitude and direction of the acceleration vector. They are used to detect changes in acceleration, in tilt sensors, or to detect free fall, as sensors triggering

airbag

deployment, and in many other applications. Some

fingerprint sensors

use capacitors. Additionally, a user can adjust the pitch of a

theremin

musical instrument by moving their hand since this changes the effective capacitance between the user's hand and the antenna.

**Changing the effective area of the plates**

Capacitive

touch switches

are used on many consumer electronic products.

### Oscillators

A capacitor can possess spring-like qualities in an oscillator circuit. In the image example, a capacitor acts to influence the biasing voltage at the npn transistor's base. The resistance values of the voltage-divider resistors and the capacitance value of the capacitor together control the oscillatory frequency.

### Producing light

A light-emitting capacitor is made from a dielectric that uses phosphorescence to produce light. If one of the conductive plates is made with a transparent material, the light is visible. Light-emitting capacitors are used in the construction of electroluminescent panels, for applications such as backlighting for laptop computers. In this case, the entire panel is a capacitor used for the purpose of generating light.


## Hazards and safety

The hazards posed by a capacitor are usually determined by the amount of energy stored, which can cause electrical burns or heart fibrillation. Factors such as voltage and chassis material are of secondary consideration, which are more related to how easily a shock can be initiated rather than how much damage can occur. Although they usually do not leave a burn, shocks as low as one joule have been reported to cause death under certain conditions, including conductivity of the surfaces, preexisting medical conditions, the humidity of the air, or the pathways it takes through the body (i.e. shocks that travel across the core of the body and, especially, through the heart are more dangerous than those limited to the extremities). Shocks over ten joules generally damage skin, and are considered hazardous. Any capacitor that can store 50 joules or more is considered potentially lethal.

Capacitors may retain a charge long after power is removed from a circuit; this charge can cause dangerous or fatal shocks or damage connected equipment. For example, the flash of a disposable camera has a photoflash capacitor that may contain over 15 joules of energy and be charged to over 300 volts. Service procedures for electronic devices usually include instructions to discharge large or high-voltage capacitors. Larger capacitors may have built-in discharge resistors to dissipate stored energy to a safe level within a few seconds after power is removed. High-voltage capacitors are stored with the terminals shorted, as protection from potentially dangerous voltages due to dielectric absorption or from transient voltages the capacitor may pick up from static charges or passing weather events.

Some old, large oil-filled paper or plastic film capacitors contain polychlorinated biphenyls (PCBs) which can leak into groundwater from landfills. Capacitors containing PCBs were labelled as containing "Askarel" and several other trade names. PCB-filled paper capacitors are found in pre-1975 fluorescent lamp ballasts, and other applications. Such capacitors may be sealed in a metal can with ceramic feed-through connectors.

Capacitors may catastrophically fail when subjected to voltages or currents beyond their rating, or in case of polarized capacitors, applied in a reverse polarity. Failures may create arcing that heats and vaporizes the dielectric fluid, causing a build up of pressurized gas that may result in swelling, rupture, or an explosion. Larger capacitors may have vents or similar mechanism to release of pressure in the event of failure. Capacitors used in RF or sustained high-current applications can overheat, especially in the center of the capacitor rolls. Capacitors used within high-energy capacitor banks can violently explode when a short in one capacitor causes sudden dumping of energy stored in the rest of the bank into the failing unit. High voltage vacuum capacitors can generate soft X-rays even during normal operation. Proper containment, fusing, and preventive maintenance can help to minimize these hazards.

High-voltage capacitors may benefit from a pre-charge to limit in-rush currents at power-up of high voltage direct current (HVDC) circuits. This extends the life of the component and may mitigate high-voltage hazards.

- (Swollen electrolytic capacitors. The vent on the tops allows the release of pressurized gas build-up in the event of failure, preventing it from exploding.)Swollen electrolytic capacitors. The vent on the tops allows the release of pressurized gas build-up in the event of failure, preventing it from exploding.
- (This high-energy capacitor from a defibrillator has a resistor connected between the terminals for safety, to dissipate stored energy.)This high-energy capacitor from a defibrillator has a resistor connected between the terminals for safety, to dissipate stored energy.
- (An exploded electrolytic capacitor, showing fragments of paper and metallic foil)An exploded electrolytic capacitor, showing fragments of paper and metallic foil
