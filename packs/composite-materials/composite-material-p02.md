---
title: "Composite material (part 2/2)"
source: https://en.wikipedia.org/wiki/Composite_material
domain: composite-materials
license: CC-BY-SA-4.0
tags: composite materials, fiber reinforced, carbon fiber, laminate structure
fetched: 2026-07-02
part: 2/2
---

## Mechanical properties of composites

### Particle reinforcement

In general, particle reinforcement is strengthening the composites less than fiber reinforcement. It is used to enhance the stiffness of the composites while increasing the strength and the toughness. Because of their mechanical properties, they are used in applications in which wear resistance is required. For example, hardness of cement can be increased by reinforcing gravel particles, drastically. Particle reinforcement a highly advantageous method of tuning mechanical properties of materials since it is very easy implement while being low cost.

The elastic modulus of particle-reinforced composites can be expressed as,

$E_{c}=V_{m}E_{m}+K_{c}V_{p}E_{p}$

where E is the elastic modulus, V is the volume fraction. The subscripts c, p and m are indicating composite, particle and matrix, respectively. $K_{c}$ is a constant can be found empirically.

Similarly, tensile strength of particle-reinforced composites can be expressed as,

$(T.S.)_{c}=V_{m}(T.S.)_{m}+K_{s}V_{p}(T.S.)_{p}$

where T.S. is the tensile strength, and $K_{s}$ is a constant (not equal to $K_{c}$ ) that can be found empirically.

### Short fiber reinforcement (shear lag theory)

Short fibers are often cheaper or more convenient to manufacture than longer continuous fibers, but still provide better properties than particle reinforcement. A common example is carbon fiber reinforced 3D printing filaments, which use chopped short carbon fibers mixed into a matrix, typically PLA or PETG.

Shear lag theory uses the shear lag model to predict properties such as the Young's modulus for short fiber composites. The model assumes that load is transferred from the matrix to the fibers solely through the interfacial shear stresses $\tau _{i}$ acting on the cylindrical interface. Shear lag theory says then that the rate of change of the axial stress in the fiber as you move along the fiber is proportional to the ratio of the interfacial shear stresses over the radius of the fibre $r_{0}$ :

${\frac {d\sigma _{f}}{dx}}=-{\frac {2\tau _{i}}{r_{0}}}$

This leads to the average fiber stress over the full length of the fibre being given by:

$\sigma _{f}=E_{f}\varepsilon _{1}\left(1-{\frac {\tanh(ns)}{ns}}\right)$

where

- $\varepsilon _{1}$ is the macroscopic strain in the composite
- s is the *fiber aspect ratio* (length over diameter)
- $n=\left({\frac {2E_{m}}{E_{f}(1+\nu _{m})\ln(1/f)}}\right)^{1/2}$ is a dimensionless constant
- $\nu _{m}$ is the Poisson's ratio of the matrix

By assuming a uniform tensile strain, this results in:

$E_{1}={\frac {\sigma _{1}}{\varepsilon _{1}}}=fE_{f}\left(1-{\frac {\tanh(ns)}{ns}}\right)+(1-f)E_{m}$

As *s* becomes larger, this tends towards the rule of mixtures, which represents the Young's modulus parallel to continuous fibers.

### Continuous fiber reinforcement

In general, continuous fiber reinforcement is implemented by incorporating a fiber as the strong phase into a weak phase, matrix. The reason for the popularity of fiber usage is materials with extraordinary strength can be obtained in their fiber form. Non-metallic fibers are usually showing a very high strength to density ratio compared to metal fibers because of the covalent nature of their bonds. The most famous example of this is carbon fibers that have many applications extending from sports gear to protective equipment to space industries.

The stress on the composite can be expressed in terms of the volume fraction of the fiber and the matrix.

$\sigma _{c}=V_{f}\sigma _{f}+V_{m}\sigma _{m}$

where $\sigma$ is the stress, V is the volume fraction. The subscripts c, f and m are indicating composite, fiber and matrix, respectively.

Although the stress–strain behavior of fiber composites can only be determined by testing, there is an expected trend, three stages of the stress–strain curve. The first stage is the region of the stress–strain curve where both fiber and the matrix are elastically deformed. This linearly elastic region can be expressed in the following form.

$\sigma _{c}=E_{c}\epsilon _{c}=\epsilon _{c}(V_{f}E_{f}+V_{m}E_{m})$

where $\sigma$ is the stress, $\epsilon$ is the strain, E is the elastic modulus, and V is the volume fraction. The subscripts c, f, and m are indicating composite, fiber, and matrix, respectively.

After passing the elastic region for both fiber and the matrix, the second region of the stress–strain curve can be observed. In the second region, the fiber is still elastically deformed while the matrix is plastically deformed since the matrix is the weak phase. The instantaneous modulus can be determined using the slope of the stress–strain curve in the second region. The relationship between stress and strain can be expressed as,

$\sigma _{c}=V_{f}E_{f}\epsilon _{c}+V_{m}\sigma _{m}(\epsilon _{c})$

where $\sigma$ is the stress, $\epsilon$ is the strain, E is the elastic modulus, and V is the volume fraction. The subscripts c, f, and m are indicating composite, fiber, and matrix, respectively. To find the modulus in the second region derivative of this equation can be used since the slope of the curve is equal to the modulus.

$E_{c}'={\frac {d\sigma _{c}}{d\epsilon _{c}}}=V_{f}E_{f}+V_{m}\left({\frac {d\sigma _{c}}{d\epsilon _{c}}}\right)$

In most cases it can be assumed $E_{c}'=V_{f}E_{f}$ since the second term is much less than the first one.

In reality, the derivative of stress with respect to strain is not always returning the modulus because of the binding interaction between the fiber and matrix. The strength of the interaction between these two phases can result in changes in the mechanical properties of the composite. The compatibility of the fiber and matrix is a measure of internal stress.

The covalently bonded high strength fibers (e.g. carbon fibers) experience mostly elastic deformation before the fracture since the plastic deformation can happen due to dislocation motion. Whereas, metallic fibers have more space to plastically deform, so their composites exhibit a third stage where both fiber and the matrix are plastically deforming. Metallic fibers have many applications to work at cryogenic temperatures that is one of the advantages of composites with metal fibers over nonmetallic. The stress in this region of the stress–strain curve can be expressed as,

$\sigma _{c}(\epsilon _{c})=V_{f}\sigma _{f}\epsilon _{c}+V_{m}\sigma _{m}(\epsilon _{c})$

where $\sigma$ is the stress, $\epsilon$ is the strain, E is the elastic modulus, and V is the volume fraction. The subscripts c, f, and m are indicating composite, fiber, and matrix, respectively. $\sigma _{f}(\epsilon _{c})$ and $\sigma _{m}(\epsilon _{c})$ are for fiber and matrix flow stresses respectively. Just after the third region the composite exhibit necking. The necking strain of composite is happened to be between the necking strain of the fiber and the matrix just like other mechanical properties of the composites. The necking strain of the weak phase is delayed by the strong phase. The amount of the delay depends upon the volume fraction of the strong phase.

Thus, the tensile strength of the composite can be expressed in terms of the volume fraction.

$(T.S.)_{c}=V_{f}(T.S.)_{f}+V_{m}\sigma _{m}(\epsilon _{m})$

where T.S. is the tensile strength, $\sigma$ is the stress, $\epsilon$ is the strain, E is the elastic modulus, and V is the volume fraction. The subscripts c, f, and m are indicating composite, fiber, and matrix, respectively. The composite tensile strength can be expressed as

$(T.S.)_{c}=V_{m}(T.S.)_{m}$

for

$V_{f}$

is less than or equal to

$V_{c}$

(arbitrary critical value of volume fraction)

$(T.S.)_{c}=V_{f}(T.S.)_{f}+V_{m}(\sigma _{m})$

for

$V_{f}$

is greater than or equal to

$V_{c}$

The critical value of volume fraction can be expressed as,

$V_{c}={\frac {[(T.S.)_{m}-\sigma _{m}(\epsilon _{f})]}{[(T.S.)_{f}+(T.S.)_{m}-\sigma _{m}(\epsilon _{f})]}}$

Evidently, the composite tensile strength can be higher than the matrix if $(T.S.)_{c}$ is greater than $(T.S.)_{m}$ .

Thus, the minimum volume fraction of the fiber can be expressed as,

$V_{c}={\frac {[(T.S.)_{m}-\sigma _{m}(\epsilon _{f})]}{[(T.S.)_{f}-\sigma _{m}(\epsilon _{f})]}}$

Although this minimum value is very low in practice, it is very important to know since the reason for the incorporation of continuous fibers is to improve the mechanical properties of the materials/composites, and this value of volume fraction is the threshold of this improvement.

### The effect of fiber orientation

#### Aligned fibers

A change in the angle between the applied stress and fiber orientation will affect the mechanical properties of fiber-reinforced composites, especially the tensile strength. This angle, $\theta$ , can be used predict the dominant tensile fracture mechanism.

At small angles, $\theta \approx 0^{\circ }$ , the dominant fracture mechanism is the same as with load-fiber alignment, tensile fracture. The resolved force acting upon the length of the fibers is reduced by a factor of $\cos \theta$ from rotation. $F_{\mbox{res}}=F\cos \theta$ . The resolved area on which the fiber experiences the force is increased by a factor of $\cos \theta$ from rotation. $A_{\mbox{res}}=A_{0}/\cos \theta$ . Taking the effective tensile strength to be $({\mbox{T.S.}})_{\mbox{c}}=F_{\mbox{res}}/A_{\mbox{res}}$ and the aligned tensile strength $\sigma _{\parallel }^{*}=F/A$ .

$({\mbox{T.S.}})_{\mbox{c}}\;({\mbox{longitudinal fracture}})={\frac {\sigma _{\parallel }^{*}}{\cos ^{2}\theta }}$

At moderate angles, $\theta \approx 45^{\circ }$ , the material experiences shear failure. The effective force direction is reduced with respect to the aligned direction. $F_{\mbox{res}}=F\cos \theta$ . The resolved area on which the force acts is $A_{\mbox{res}}=A_{m}/\sin \theta$ . The resulting tensile strength depends on the shear strength of the matrix, $\tau _{m}$ .

$({\mbox{T.S.}})_{\mbox{c}}\;({\mbox{shear failure}})={\frac {\tau _{m}}{\sin {\theta }\cos {\theta }}}$

At extreme angles, $\theta \approx 90^{\circ }$ , the dominant mode of failure is tensile fracture in the matrix in the perpendicular direction. As in the isostress case of layered composite materials, the strength in this direction is lower than in the aligned direction. The effective areas and forces act perpendicular to the aligned direction so they both scale by $\sin \theta$ . The resolved tensile strength is proportional to the transverse strength, $\sigma _{\perp }^{*}$ .

$({\mbox{T.S.}})_{\mbox{c}}\;({\mbox{transverse fracture}})={\frac {\sigma _{\perp }^{*}}{\sin ^{2}\theta }}$

The critical angles from which the dominant fracture mechanism changes can be calculated as,

$\theta _{c_{1}}=\tan ^{-1}\left({\frac {\tau _{m}}{\sigma _{\parallel }^{*}}}\right)$

$\theta _{c_{2}}=\tan ^{-1}\left({\frac {\sigma _{\perp }^{*}}{\tau _{m}}}\right)$

where $\theta _{c_{1}}$ is the critical angle between longitudinal fracture and shear failure, and $\theta _{c_{2}}$ is the critical angle between shear failure and transverse fracture.

By ignoring length effects, this model is most accurate for continuous fibers and does not effectively capture the strength-orientation relationship for short fiber reinforced composites. Furthermore, most realistic systems do not experience the local maxima predicted at the critical angles. The Tsai-Hill criterion provides a more complete description of fiber composite tensile strength as a function of orientation angle by coupling the contributing yield stresses: $\sigma _{\parallel }^{*}$ , $\sigma _{\perp }^{*}$ , and $\tau _{m}$ .

$({\mbox{T.S.}})_{\mbox{c}}\;({\mbox{Tsai-Hill}})={\bigg [}{\frac {\cos ^{4}\theta }{({\sigma _{\parallel }^{*}})^{2}}}+\cos ^{2}\theta \sin ^{2}\theta \left({\frac {1}{({\tau _{m}})^{2}}}-{\frac {1}{({\sigma _{\parallel }^{*}})^{2}}}\right)+{\frac {\sin ^{4}\theta }{({\sigma _{\perp }^{*}})^{2}}}{\bigg ]}^{-1/2}$

#### Randomly oriented fibers

Anisotropy in the tensile strength of fiber reinforced composites can be removed by randomly orienting the fiber directions within the material. It sacrifices the ultimate strength in the aligned direction for an overall, isotropically strengthened material.

$E_{c}=KV_{f}E_{f}+V_{m}E_{m}$

Where K is an empirically determined reinforcement factor; similar to the particle reinforcement equation. For fibers with randomly distributed orientations in a plane, $K\approx 0.38$ , and for a random distribution in 3D, $K\approx 0.20$ .

### Stiffness and Compliance Elasticity

Composite materials are generally anisotropic, and in many cases are orthotropic. Voigt notation can be used to reduce the rank of the stress and strain tensors such that the stiffness C (often also referred to by Q ) and compliance S can be written as a matrix:

${\begin{bmatrix}\sigma _{1}\\\sigma _{2}\\\sigma _{3}\\\sigma _{4}\\\sigma _{5}\\\sigma _{6}\end{bmatrix}}={\begin{bmatrix}C_{11}&C_{12}&C_{13}&C_{14}&C_{15}&C_{16}\\C_{12}&C_{22}&C_{23}&C_{24}&C_{25}&C_{26}\\C_{13}&C_{23}&C_{33}&C_{34}&C_{35}&C_{36}\\C_{14}&C_{24}&C_{34}&C_{44}&C_{45}&C_{46}\\C_{15}&C_{25}&C_{35}&C_{45}&C_{55}&C_{56}\\C_{16}&C_{26}&C_{36}&C_{46}&C_{56}&C_{66}\end{bmatrix}}{\begin{bmatrix}\varepsilon _{1}\\\varepsilon _{2}\\\varepsilon _{3}\\\varepsilon _{4}\\\varepsilon _{5}\\\varepsilon _{6}\end{bmatrix}}$ and ${\begin{bmatrix}\varepsilon _{1}\\\varepsilon _{2}\\\varepsilon _{3}\\\varepsilon _{4}\\\varepsilon _{5}\\\varepsilon _{6}\end{bmatrix}}={\begin{bmatrix}S_{11}&S_{12}&S_{13}&S_{14}&S_{15}&S_{16}\\S_{12}&S_{22}&S_{23}&S_{24}&S_{25}&S_{26}\\S_{13}&S_{23}&S_{33}&S_{34}&S_{35}&S_{36}\\S_{14}&S_{24}&S_{34}&S_{44}&S_{45}&S_{46}\\S_{15}&S_{25}&S_{35}&S_{45}&S_{55}&S_{56}\\S_{16}&S_{26}&S_{36}&S_{46}&S_{56}&S_{66}\end{bmatrix}}{\begin{bmatrix}\sigma _{1}\\\sigma _{2}\\\sigma _{3}\\\sigma _{4}\\\sigma _{5}\\\sigma _{6}\end{bmatrix}}$

When considering each ply individually, it is assumed that they can be treated as thi lamina and so out–of–plane stresses and strains are negligible. That is $\sigma _{3}=\sigma _{4}=\sigma _{5}=0$ and $\varepsilon _{4}=\varepsilon _{5}=0$ . This allows the stiffness and compliance matrices to be reduced to 3x3 matrices as follows:

$C={\begin{bmatrix}{\tfrac {E_{\rm {1}}}{1-{\nu _{\rm {12}}}{\nu _{\rm {21}}}}}&{\tfrac {E_{\rm {2}}{\nu _{\rm {12}}}}{1-{\nu _{\rm {12}}}{\nu _{\rm {21}}}}}&0\\{\tfrac {E_{\rm {2}}{\nu _{\rm {12}}}}{1-{\nu _{\rm {12}}}{\nu _{\rm {21}}}}}&{\tfrac {E_{\rm {2}}}{1-{\nu _{\rm {12}}}{\nu _{\rm {21}}}}}&0\\0&0&G_{\rm {12}}\\\end{bmatrix}}\quad$ and $\quad S={\begin{bmatrix}{\tfrac {1}{E_{\rm {1}}}}&-{\tfrac {\nu _{\rm {21}}}{E_{\rm {2}}}}&0\\-{\tfrac {\nu _{\rm {12}}}{E_{\rm {1}}}}&{\tfrac {1}{E_{\rm {2}}}}&0\\0&0&{\tfrac {1}{G_{\rm {12}}}}\\\end{bmatrix}}$

For fiber-reinforced composite, the fiber orientation in material affect anisotropic properties of the structure. From characterizing technique i.e. tensile testing, the material properties were measured based on sample (1-2) coordinate system. The tensors above express stress-strain relationship in (1-2) coordinate system. While the known material properties is in the principal coordinate system (x-y) of material. Transforming the tensor between two coordinate system help identify the material properties of the tested sample. The transformation matrix with $\theta$ degree rotation is

$T(\theta )_{\epsilon }={\begin{bmatrix}\cos ^{2}\theta &\sin ^{2}\theta &\cos \theta \sin \theta \\sin^{2}\theta &\cos ^{2}\theta &-\cos \theta \sin \theta \\-2\cos \theta \sin \theta &2\cos \theta \sin \theta &\cos ^{2}\theta -\sin ^{2}\theta \end{bmatrix}}$ for ${\begin{bmatrix}{\acute {\epsilon }}\end{bmatrix}}=T(\theta )_{\epsilon }{\begin{bmatrix}\epsilon \end{bmatrix}}$ $T(\theta )_{\sigma }={\begin{bmatrix}\cos ^{2}\theta &\sin ^{2}\theta &2\cos \theta \sin \theta \\sin^{2}\theta &\cos ^{2}\theta &-2\cos \theta \sin \theta \\-\cos \theta \sin \theta &\cos \theta \sin \theta &\cos ^{2}\theta -\sin ^{2}\theta \end{bmatrix}}$ for ${\begin{bmatrix}{\acute {\sigma }}\end{bmatrix}}=T(\theta )_{\sigma }{\begin{bmatrix}\sigma \end{bmatrix}}$

### Types of fibers and mechanical properties

The most common types of fibers used in industry are glass fibers, carbon fibers, and kevlar due to their ease of production and availability. Their mechanical properties are very important to know, therefore the table of their mechanical properties is given below to compare them with S97 steel. The angle of fiber orientation is very important because of the anisotropy of fiber composites (please see the section "Physical properties" for a more detailed explanation). The mechanical properties of the composites can be tested using standard mechanical testing methods by positioning the samples at various angles (the standard angles are 0°, 45°, and 90°) with respect to the orientation of fibers within the composites. In general, 0° axial alignment makes composites resistant to longitudinal bending and axial tension/compression, 90° hoop alignment is used to obtain resistance to internal/external pressure, and ± 45° is the ideal choice to obtain resistance against pure torsion.

#### Mechanical properties of fiber composite materials

Fibres @ 0° (UD), 0/90° (fabric) to loading axis, Dry, Room Temperature, V

f

= 60% (UD), 50% (fabric) Fibre / Epoxy Resin (cured at 120 °C)

Symbol

Units

Standard

Carbon Fiber

Fabric

High Modulus

Carbon Fiber

Fabric

E-Glass

Fibre Glass Fabric

Kevlar

Fabric

Standard

Unidirectional

Carbon Fiber

Fabric

High Modulus

Unidirectional

Carbon Fiber

Fabric

E-Glass

Unidirectional

Fiber Glass Fabric

Kevlar

Unidirectional Fabric

Steel

S97

Young's Modulus 0°

E1

GPa

70

85

25

30

135

175

40

75

207

Young's Modulus 90°

E2

GPa

70

85

25

30

10

8

8

6

207

In-plane Shear Modulus

G12

GPa

5

5

4

5

5

5

4

2

80

Major Poisson's Ratio

v12

0.10

0.10

0.20

0.20

0.30

0.30

0.25

0.34

–

Ult. Tensile Strength 0°

Xt

MPa

600

350

440

480

1500

1000

1000

1300

990

Ult. Comp. Strength 0°

Xc

MPa

570

150

425

190

1200

850

600

280

–

Ult. Tensile Strength 90°

Yt

MPa

600

350

440

480

50

40

30

30

–

Ult. Comp. Strength 90°

Yc

MPa

570

150

425

190

250

200

110

140

–

Ult. In-plane Shear Stren.

S

MPa

90

35

40

50

70

60

40

60

–

Ult. Tensile Strain 0°

ext

%

0.85

0.40

1.75

1.60

1.05

0.55

2.50

1.70

–

Ult. Comp. Strain 0°

exc

%

0.80

0.15

1.70

0.60

0.85

0.45

1.50

0.35

–

Ult. Tensile Strain 90°

eyt

%

0.85

0.40

1.75

1.60

0.50

0.50

0.35

0.50

–

Ult. Comp. Strain 90°

eyc

%

0.80

0.15

1.70

0.60

2.50

2.50

1.35

2.30

–

Ult. In-plane shear strain

es

%

1.80

0.70

1.00

1.00

1.40

1.20

1.00

3.00

–

Density

g/cc

1.60

1.60

1.90

1.40

1.60

1.60

1.90

1.40

–

Fibres @ ±45 Deg. to loading axis, Dry, Room Temperature, Vf = 60% (UD), 50% (fabric)

Symbol

Units

Standard

Carbon Fiber

High Modulus

Carbon Fiber

E-Glass

Fiber Glass

Standard

Carbon Fibers

Fabric

E-Glass

Fiber Glass Fabric

Steel

Al

Longitudinal Modulus

E1

GPa

17

17

12.3

19.1

12.2

207

72

Transverse Modulus

E2

GPa

17

17

12.3

19.1

12.2

207

72

In Plane Shear Modulus

G12

GPa

33

47

11

30

8

80

25

Poisson's Ratio

v12

.77

.83

.53

.74

.53

Tensile Strength

Xt

MPa

110

110

90

120

120

990

460

Compressive Strength

Xc

MPa

110

110

90

120

120

990

460

In Plane Shear Strength

S

MPa

260

210

100

310

150

Thermal Expansion Co-ef

Alpha1

Strain/K

2.15 E-6

0.9 E-6

12 E-6

4.9 E-6

10 E-6

11 E-6

23 E-6

Moisture Co-ef

Beta1

Strain/K

3.22 E-4

2.49 E-4

6.9 E-4

#### Carbon fiber & fiberglass composites vs. aluminum alloy and steel

Although strength and stiffness of steel and aluminum alloys are comparable to fiber composites, specific strength and stiffness of composites (i.e. in relation to their weight) are significantly higher.

|   | **Carbon Fiber Composite (aerospace grade)** | **Carbon Fiber Composite (commercial grade)** | **Fiberglass Composite** | **Aluminum 6061 T-6** | **Steel,** **Mild** |
|---|---|---|---|---|---|
| **Cost $/LB** | $20 – $250+ | $5 – $20 | $1.50 – $3.00 | $3 | $0.30 |
| **Strength (psi)** | 90,000 – 200,000 | 50,000 – 90,000 | 20,000 – 35,000 | 35,000 | 60,000 |
| **Stiffness (psi)** | 10 × 106– 50 × 106 | 8 × 106 – 10 × 106 | 1 × 106 – 1.5 × 106 | 10 × 106 | 30 × 106 |
| **Density (lb/in3)** | 0.050 | 0.050 | 0.055 | 0.10 | 0.30 |
| **Specific Strength** | 1.8 × 106 – 4 × 106 | 1 × 106 – 1.8 × 106 | 363,640–636,360 | 350,000 | 200,000 |
| **Specific Stiffness** | 200 × 106 – 1,000 × 106 | 160 × 106 – 200 × 106 | 18 × 106 – 27 × 106 | 100 × 106 | 100 × 106 |

### Failure

Shock, impact of varying speed, or repeated cyclic stresses can provoke the laminate to separate at the interface between two layers, a condition known as delamination. Individual fibres can separate from the matrix, for example, fibre pull-out.

Composites can fail on the macroscopic or microscopic scale. Compression failures can happen at both the macro scale or at each individual reinforcing fibre in compression buckling. Tension failures can be net section failures of the part or degradation of the composite at a microscopic scale where one or more of the layers in the composite fail in tension of the matrix or failure of the bond between the matrix and fibres.

Some composites are brittle and possess little reserve strength beyond the initial onset of failure while others may have large deformations and have reserve energy absorbing capacity past the onset of damage. The distinctions in fibres and matrices that are available and the mixtures that can be made with blends leave a very broad range of properties that can be designed into a composite structure. The most famous failure of a brittle ceramic matrix composite occurred when the carbon-carbon composite tile on the leading edge of the wing of the Space Shuttle Columbia fractured when impacted during take-off. It directed to the catastrophic break-up of the vehicle when it re-entered the Earth's atmosphere on 1 February 2003.

Composites have relatively poor bearing strength compared to metals.

Another failure mode is fiber tensile fracture, which becomes more likely when fibers are aligned with the loading direction, so is the possibility of fiber tensile fracture, assuming the tensile strength exceeds that of the matrix. When a fiber has some angle of misorientation θ, several fracture modes are possible. For small values of θ the stress required to initiate fracture is increased by a factor of (cos θ)−2 due to the increased cross-sectional area (*A* cos θ) of the fibre and reduced force (*F/*cos θ) experienced by the fiber, leading to a composite tensile strength of *σparallel /*cos2 θ where *σparallel* is the tensile strength of the composite with fibers aligned parallel with the applied force.

Intermediate angles of misorientation θ lead to matrix shear failure. Again the cross sectional area is modified but since shear stress is now the driving force for failure the area of the matrix parallel to the fibers is of interest, increasing by a factor of 1/sin θ. Similarly, the force parallel to this area again decreases (*F/*cos θ) leading to a total tensile strength of *τmy /*sin θ cos θ where *τmy* is the matrix shear strength.

Finally, for large values of θ (near π/2) transverse matrix failure is the most likely to occur, since the fibers no longer carry the majority of the load. Still, the tensile strength will be greater than for the purely perpendicular orientation, since the force perpendicular to the fibers will decrease by a factor of 1/sin θ and the area decreases by a factor of 1/sin θ producing a composite tensile strength of *σperp /*sin2θ where *σperp* is the tensile strength of the composite with fibers align perpendicular to the applied force.

### Testing

Composites are tested before and after construction to assist in predicting and preventing failures. Pre-construction testing may adopt finite element analysis (FEA) for ply-by-ply analysis of curved surfaces and predicting wrinkling, crimping and dimpling of composites. Materials may be tested during manufacturing and after construction by various non-destructive methods including ultrasonic, thermography, shearography and X-ray radiography, and laser bond inspection for NDT of relative bond strength integrity in a localized area.
