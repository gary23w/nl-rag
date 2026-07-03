---
title: "American wire gauge"
source: https://en.wikipedia.org/wiki/American_wire_gauge
domain: dc-connector
license: CC-BY-SA-4.0
tags: dc connector
fetched: 2026-07-03
---

# American wire gauge

**American Wire Gauge** (**AWG**) is a logarithmic stepped standardized wire gauge system used since 1857, predominantly in North America, for the diameters of round, solid, nonferrous, electrically conducting wire. Dimensions of the wires are given in ASTM standard B 258. The cross-sectional area of each gauge is an important factor for determining its current-carrying capacity.

## Origin

The AWG originated in the number of drawing operations used to produce a given gauge of wire. Very fine wire (for example, 30 gauge) required more passes through the drawing dies than 0 gauge wire did. Manufacturers of wire formerly had proprietary wire gauge systems; the development of standardized wire gauges rationalized selection of wire for a particular purpose.

While the AWG is essentially identical to the Brown & Sharpe (B&S) sheet metal gauge, the B&S gauge was designed for use with sheet metals. These are functionally interchangeable, but the use of B&S in relation to wire gauges, rather than sheet metal gauges, is technically improper.

## Specifications

Increasing gauge numbers denote logarithmically decreasing wire diameters, which is similar to many other non-metric gauging systems such as British Standard Wire Gauge (SWG). However, AWG is dissimilar to IEC 60228, the metric wire-size standard used in most parts of the world, based directly on the wire cross-section area (in square millimetres, mm2).

The AWG tables are for a single, solid and round conductor. The AWG of a stranded wire is determined by the cross-sectional area of the equivalent solid conductor. Because there are also small gaps between the strands, a stranded wire will always have a slightly larger overall diameter than a solid wire with the same AWG.

### Formulae

By definition, 36 AWG is 0.005 inches in diameter, and 0000 AWG is 0.46 inches (11.68 mm) in diameter. The ratio of these diameters is 1:92, and there are 40 gauge sizes from 36 to 0000, or 39 steps. Because each successive gauge number increases cross sectional area by a constant multiple, diameters vary geometrically. Any two successive gauges (e.g., *A* and *B*) have diameters whose ratio (dia. *B* ÷ dia. *A*) is ${\sqrt[{39}]{92}}$ (approximately 1.1229), while for gauges two steps apart (e.g., *A*, *B*, and *C*), the ratio of *C* to *A* is about 1.12292 ≈ 1.2610. Similarly for gauges *n* steps apart, the diameter ratio of the first to last gauges is about 1.1229*n*.

The diameter of an AWG wire is determined according to the following formula:

$d_{n}=0.005~\mathrm {inch} \times 92^{(36-n)/39}=0.127~\mathrm {mm} \times 92^{(36-n)/39}$

Where *n* is the AWG size for gauges from 36 to 0. For larger gauges *n* = −1 for 00, *n* = −2 for 000, and *n* = −3 for 0000.

or equivalently:

$d_{n}=e^{-1.12436-0.11594n}\ \mathrm {inch} =e^{2.1104-0.11594n}\ \mathrm {mm}$

The gauge can be calculated from the diameter using

$n=-39\log _{92}\left({\frac {d_{n}}{0.005~\mathrm {inch} }}\right)+36=-39\log _{92}\left({\frac {d_{n}}{0.127~\mathrm {mm} }}\right)+36$

and the cross-section area is

$A_{n}={\frac {\pi }{4}}d_{n}^{2}\approx 0.000019635~\mathrm {inch} ^{2}\times 92^{(36-n)/19.5}\approx 0.012668~\mathrm {mm} ^{2}\times 92^{(36-n)/19.5}$

.

The standard ASTM B258-02 (2008), *Standard Specification for Standard Nominal Diameters and Cross-Sectional Areas of AWG Sizes of Solid Round Wires Used as Electrical Conductors*, defines the ratio between successive sizes to be the 39th root of 92, or approximately 1.1229. ASTM B258-02 also dictates that wire diameters should be tabulated with no more than 4 significant figures, with a resolution of no more than 0.0001 inches (0.1 mils) for wires thicker than 44 AWG, and 0.00001 inches (0.01 mils) for wires 45 AWG and thinner.

Sizes with multiple zeros are successively thicker than 0 AWG and can be denoted using "*number of zeros*/0", for example 4/0 AWG for 0000 AWG. For an m/0 AWG wire, use *n* = −(*m* − 1) = 1 − *m* in the above formulas. For instance, for 0000 AWG or 4/0 AWG, use *n* = −3.

#### Rules of thumb

The sixth power of ${\sqrt[{39}]{92}}$ is very close to 2, which leads to the following rules of thumb:

- When the *cross-sectional area* of a wire is doubled, the AWG will decrease by 3; for example, two 14 AWG wires have about the same cross-sectional area as a single 11 AWG wire. This doubles the electrical conductance.
- When the *diameter* of a solid round wire is doubled, the AWG will decrease by 6; for example, 1 mm diameter wire is ≈18 AWG, 2 mm diameter wire is ≈12 AWG, and 4 mm diameter wire is ≈6 AWG. This quadruples the cross-sectional area and conductance.
- A decrease of ten gauge numbers; for example, from 24 AWG to 14 AWG multiplies the area, weight, and conductance by approximately 10.

Convenient coincidences result in the following rules of thumb for resistances:

- The resistance of copper wire is approximately ⁠1 Ω/1000 ft⁠ for 10 AWG, ⁠10 Ω/1000 ft⁠ for 20 AWG, ⁠100 Ω/1000 ft⁠ for 30 AWG, and so on. For an arbitrary gauge *n*, it is approximately 10*n*/10 Ω per 10000 ft.
- Because aluminum wire has a conductivity of approximately 61% of copper, an aluminum wire has nearly the same resistance as a copper wire that is two sizes smaller, which has 62.9% of the area.

### Tables of AWG wire sizes

The table below shows various data including both the resistance of the various wire gauges and the allowable current (ampacity) based on a copper conductor with plastic insulation. The diameter information in the table applies to *solid* wires. Stranded wires are calculated by calculating the equivalent cross sectional copper wire area. Fusing current (melting wire) is estimated based on 25 °C (77 °F) ambient temperature. The table below assumes DC, or AC frequencies equal to or less than 60 Hz, and does not take skin effect into account. "Turns of wire per unit length" refers to wire wound in a helix with the turns touching, as in a solenoid and is therefore the reciprocal of the conductor diameter. As wire in such a coil normally has insulation, this figure forms an upper bound.

AWG

Diameter

Turns of wire,

without

insulation

Area

Copper

wire

Length-specific

resistance

Ampacity

at

temperature rating (A)

Fusing current

Preece

Onderdonk

(in)

(mm)

(per in)

(per cm)

(

kcmil

)

(mm

2

)

(mΩ/m

)

(mΩ/ft

)

60 °C

75 °C

90 °C

~10 s

1 s

32 ms

0000 (4/0)

0.4600

11.684

2.17

0.856

212

107

0.1608

0.04901

195

230

260

3.2 kA

33 kA

182 kA

000 (3/0)

0.4096

10.405

2.44

0.961

168

85.0

0.2028

0.06180

165

200

225

2.7 kA

26 kA

144 kA

00 (2/0)

0.3648

9.266

2.74

1.08

133

67.4

0.2557

0.07793

145

175

195

2.3 kA

21 kA

115 kA

0 (1/0)

0.3249

8.251

3.08

1.21

106

53.5

0.3224

0.09827

125

150

170

1.9 kA

16 kA

91 kA

1

0.2893

7.348

3.46

1.36

83.7

42.4

0.4066

0.1239

110

130

145

1.6 kA

13 kA

72 kA

2

0.2576

6.544

3.88

1.53

66.4

33.6

0.5127

0.1563

95

115

130

1.3 kA

10.2 kA

57 kA

3

0.2294

5.827

4.36

1.72

52.6

26.7

0.6465

0.1970

85

100

115

1.1 kA

8.1 kA

45 kA

4

0.2043

5.189

4.89

1.93

41.7

21.2

0.8152

0.2485

70

85

95

946 A

6.4 kA

36 kA

5

0.1819

4.621

5.50

2.16

33.1

16.8

1.028

0.3133

795 A

5.1 kA

28 kA

6

0.1620

4.115

6.17

2.43

26.3

13.3

1.296

0.3951

55

65

75

668 A

4.0 kA

23 kA

7

0.1443

3.665

6.93

2.73

20.8

10.5

1.634

0.4982

561 A

3.2 kA

18 kA

8

0.1285

3.264

7.78

3.06

16.5

8.37

2.061

0.6282

40

50

55

472 A

2.5 kA

14 kA

9

0.1144

2.906

8.74

3.44

13.1

6.63

2.599

0.7921

396 A

2.0 kA

11 kA

10

0.1019

2.588

9.81

3.86

10.4

5.26

3.277

0.9989

30

35

40

333 A

1.6 kA

8.9 kA

11

0.0907

2.305

11.0

4.34

8.23

4.17

4.132

1.260

280 A

1.3 kA

7.1 kA

12

0.0808

2.053

12.4

4.87

6.53

3.31

5.211

1.588

20

25

30

235 A

1.0 kA

5.6 kA

13

0.0720

1.828

13.9

5.47

5.18

2.62

6.571

2.003

198 A

798 A

4.5 kA

14

0.0641

1.628

15.6

6.14

4.11

2.08

8.286

2.525

15

20

25

166 A

633 A

3.5 kA

15

0.0571

1.450

17.5

6.90

3.26

1.65

10.45

3.184

140 A

502 A

2.8 kA

16

0.0508

1.291

19.7

7.75

2.58

1.31

13.17

4.016

12

16

18

117 A

398 A

2.2 kA

17

0.0453

1.150

22.1

8.70

2.05

1.04

16.61

5.064

99 A

316 A

1.8 kA

18

0.0403

1.024

24.8

9.77

1.62

0.823

20.95

6.385

10

14

16

83 A

250 A

1.4 kA

19

0.0359

0.912

27.9

11.0

1.29

0.653

26.42

8.051

—

—

—

70 A

198 A

1.1 kA

20

0.0320

0.812

31.3

12.3

1.02

0.518

33.31

10.15

5

11

—

58.5 A

158 A

882 A

21

0.0285

0.723

35.1

13.8

0.810

0.410

42.00

12.80

—

—

—

49 A

125 A

700 A

22

0.0253

0.644

39.5

15.5

0.642

0.326

52.96

16.14

3

7

—

41 A

99 A

551 A

23

0.0226

0.573

44.3

17.4

0.509

0.258

66.79

20.36

—

—

—

35 A

79 A

440 A

24

0.0201

0.511

49.7

19.6

0.404

0.205

84.22

25.67

2.1

3.5

—

29 A

62 A

348 A

25

0.0179

0.455

55.9

22.0

0.320

0.162

106.2

32.37

—

—

—

24 A

49 A

276 A

26

0.0159

0.405

62.7

24.7

0.254

0.129

133.9

40.81

1.3

2.2

—

20 A

39 A

218 A

27

0.0142

0.361

70.4

27.7

0.202

0.102

168.9

51.47

—

—

—

17 A

31 A

174 A

28

0.0126

0.321

79.1

31.1

0.160

0.0810

212.9

64.90

0.83

1.4

—

14 A

24 A

137 A

29

0.0113

0.286

88.8

35.0

0.127

0.0642

268.5

81.84

—

—

—

12 A

20 A

110 A

30

0.0100

0.255

99.7

39.3

0.101

0.0509

338.6

103.2

0.52

0.86

—

10 A

15 A

86 A

31

0.00893

0.227

112

44.1

0.0797

0.0404

426.9

130.1

—

—

—

9 A

12 A

69 A

32

0.00795

0.202

126

49.5

0.0632

0.0320

538.3

164.1

0.32

0.53

—

7 A

10 A

54 A

33

0.00708

0.180

141

55.6

0.0501

0.0254

678.8

206.9

—

—

—

6 A

7.7 A

43 A

34

0.00630

0.160

159

62.4

0.0398

0.0201

856.0

260.9

0.18

0.3

—

5 A

6.1 A

34 A

35

0.00561

0.143

178

70.1

0.0315

0.0160

1079

329.0

—

—

—

4 A

4.8 A

27 A

36

0.00500

0.127

200

78.7

0.0250

0.0127

1361

414.8

—

—

—

4 A

3.9 A

22 A

37

0.00445

0.113

225

88.4

0.0198

0.0100

1716

523.1

—

—

—

3 A

3.1 A

17 A

38

0.00397

0.101

252

99.3

0.0157

0.00797

2164

659.6

—

—

—

3 A

2.4 A

14 A

39

0.00353

0.0897

283

111

0.0125

0.00632

2729

831.8

—

—

—

2 A

1.9 A

11 A

40

0.00314

0.0799

318

125

0.00989

0.00501

3441

1049

—

—

—

1 A

1.5 A

8.5 A

1. For enclosed wire at 30 °C ambient, with given insulation material temperature rating, or for single unbundled wires in equipment for 16 AWG and thinner.
2. or, equivalently, Ω/km
3. or, equivalently, Ω/kft
4. Exactly, by definition

In the North American electrical industry, conductors thicker than 4/0 AWG are generally identified by the area in thousands of circular mils (kcmil), where 1 kcmil = 0.5067 mm2. The next wire size thicker than 4/0 has a cross section of 250 kcmil. A *circular mil* is the area of a wire one mil in diameter. One million circular mils is the area of a circle with 1,000 mil (1 inch) diameter. An older abbreviation for one thousand circular mils is *MCM*.

### Stranded wire AWG sizes

AWG can also be used to describe stranded wire. The AWG size of a stranded wire represents the sum of the cross-sectional diameter of the individual strands; the gaps between strands are not counted. When made with circular strands, these gaps occupy about 25% of the wire area, thus requiring the overall bundle diameter to be about 13% larger than a solid wire of equal gauge.

Stranded wires are specified with three numbers, the overall AWG size, the number of strands, and the AWG size of a strand. The number of strands and the AWG size of a strand are separated by a slash. For example, a 22 AWG 7/30 stranded wire is a 22 AWG wire made from seven strands of 30 AWG wire.

As indicated in the Formulae and Rules of thumb sections above, differences in AWG size translate directly into ratios of diameter or area. This property can be employed to easily find the AWG size of a stranded bundle by measuring the diameter and count of its strands. (This only applies to bundles with circular strands of identical size.) To find the AWG size of 7-strand wire with equal strands, subtract 8.4 from the AWG size of a strand. Similarly, for 19-strand subtract 12.7, and for 37 subtract 15.6.

Measuring strand diameter is often easier and more accurate than attempting to measure bundle diameter and packing ratio. Such measurement can be done with a wire gauge go-no-go tool or with a caliper or micrometer.

## Nomenclature and abbreviations in electrical distribution

Alternative ways are commonly used in the electrical industry to specify wire sizes as AWG.

- **4 AWG** (proper)
  - **#4** (the number sign is used as an abbreviation of "number")
  - **№ 4** (the numero sign is used as an abbreviation for "number")
  - **No. 4** (an approximation of the numero is used as an abbreviation for "number")
  - **No. 4 AWG**
  - **4 ga.** (abbreviation for "gauge")
- **000 AWG** (proper for thick sizes)
  - **3/0** (common for thick sizes) Pronounced "three-aught" or "triple-aught"
  - **3/0 AWG**
  - **#000**

### Pronunciation

*AWG* is colloquially referred to as *gauge* and the zeros in thick wire sizes are referred to as *aught* /ˈɔːt/. Wire sized 1 AWG is referred to as "one gauge" or "No. 1" wire; similarly, thinner sizes are pronounced "*x* gauge" or "No. *x*" wire, where *x* is the positive-integer AWG number. Consecutive AWG wire sizes thicker than No. 1 wire are designated by the number of zeros:

- No. 0, often written 1/0 and referred to as "one-aught" or "single-aught" wire
- No. 00, often written 2/0 and referred to as "two-aught" or "double-aught" wire
- No. 000, often written 3/0 and referred to as "three-aught" or "triple-aught" wire

and so on.
