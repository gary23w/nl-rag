---
title: "Axial compressor"
source: https://en.wikipedia.org/wiki/Axial_compressor
domain: air-turborocket
license: CC-BY-SA-4.0
tags: air turborocket
fetched: 2026-07-05
---

# Axial compressor

An **axial compressor** is a type of gas compressor that continuously pressurizes a working fluid. It is a rotating, airfoil-based device in which the fluid flows primarily in one direction parallel to the axis of rotation. This distinguishes axial compressors from other types of rotating compressors, such as centrifugal compressors, axi-centrifugal compressors, and mixed-flow compressors, in which the fluid flowing includes a significant radial component directed outward from the axis of rotation.

The rotor blades exert torque on the fluid, increasing its energy as it passes through the compressor. The stationary blades, or stators, slow the fluid, converting the circumferential component of flowing into pressure. Compressors are typically driven by an electric motor, a steam turbine, or a gas turbine.

Axial flow compressors produce a continuous flow of compressed gas. They exhibit high efficiency and large mass flow rate in relation to the size of their cross-section. They are more intricate and expensive relative to other designs, requiring several rows of airfoils to achieve a large pressure rise.

Axial compressors are integral to the design of large gas turbines such as jet engines, high speed ship engines, and small scale power stations. They are also used in industrial applications such as large volume air separation plants, blast furnace air, fluid catalytic cracking air, and propane dehydrogenation. Additionally, due to their performance and operability across the flight envelope (safe operational limits for an aircraft), they are widely used in aerospace applications.

| Typical application | Type of flow | Pressure ratio per stage | Efficiency per stage |
|---|---|---|---|
| Industrial | Subsonic | 1.05–1.2 | 88–92% |
| Aerospace | Transonic | 1.15–1.6 | 80–85% |
| Research | Supersonic | 1.8–2.2 | 75–85% |

## Description

Axial compressors consist of alternating rows of rotating and stationary airfoils. The rotating airfoils, or rotors, are mounted on a rotating drum, which is driven by a central shaft. The stationary airfoils, known as vanes or stators, are mounted to a tubular casing. One row of rotors and one row of stators together form a stage. The rotors impart kinetic energy to the working fluid, increasing its velocity in the axial and circumferential directions. The stators convert the increased kinetic energy into static pressure through diffusion and redirect the flow direction of the fluid to prepare it for the rotor blades of the next stage. The area between the rotor drum and casing decreases along the flow direction to maintain an optimum Mach number as the fluid is compressed.

Rotor passages can be designed to achieve diffusive pressure rise, leading to a higher pressure rise per stage. The ratio of pressure rise in the rotor to the total pressure rise of the stage is known as the degree of reaction.

## Design

The increase in pressure produced by a single stage is limited by the relative velocity between the rotor and the fluid, and the turning and diffusion capabilities of the airfoils. A typical stage in a commercial compressor will produce a pressure increase of between 15% and 60% (pressure ratios of 1.15–1.6) at design conditions with a polytropic efficiency in the region of 90–95%. To achieve different pressure ratios, axial compressors are designed with different numbers of stages and rotational speeds. As a rule of thumb, it can be assumed that each stage in a given compressor has the same temperature rise (ΔT). Therefore, at the entry, temperature (Tstage) to each stage must increase progressively through the compressor and the ratio (Delta T)/(Tstage) entry must decrease, thus implying a progressive reduction in stage pressure ratio through the unit. Hence the rear stage develops a significantly lower pressure ratio than the first stage. Higher stage pressure ratios are also possible if the relative velocity between fluid and rotors is supersonic, but this is achieved at the expense of efficiency and operability. Such compressors, with stage pressure ratios of over 2, are only used where minimizing the compressor size, weight or complexity is critical, such as in military jets.

The airfoil profiles are optimized and matched for specific velocities and turning. Although compressors can be run at other conditions with different flows, speeds, or pressure ratios, this can result in an efficiency penalty or even a partial or complete breakdown in flow (known as compressor stall and pressure surge respectively). Thus, a practical limit on the number of stages, and the overall pressure ratio, comes from the interaction of the different stages when required to work away from the design conditions. These "off-design" conditions can be mitigated to a certain extent by providing some flexibility in the compressor. This is achieved normally through the use of adjustable stators or with valves that can bleed fluid from the main flow between stages (inter-stage bleed). Modern jet engines use a series of compressors, running at different speeds; to supply air at around 40:1 pressure ratio for combustion with sufficient flexibility for all flight conditions.

## Kinetics and energy equations

The law of moment of momentum states that the sum of the moments of external forces acting on a fluid which is temporarily occupying the control volume is equal to the net change of angular momentum flux through the control volume.

The swirling fluid enters the control volume at radius, $r_{1}\,$ , with tangential velocity, $V_{w1}\,$ , and leaves at radius, $r_{2}\,$ , with tangential velocity, $V_{w2}\,$ .

$V_{1}\,$

and

$V_{2}\,$

are the absolute velocities at the inlet and outlet respectively.

$V_{f1}\,$

and

$V_{f2}\,$

are the axial flow velocities at the inlet and outlet respectively.

$V_{w1}\,$

and

$V_{w2}\,$

are the swirl velocities at the inlet and outlet respectively.

$V_{r1}\,$

and

$V_{r2}\,$

are the blade-relative velocities at the inlet and outlet respectively.

$U\,$

is the linear velocity of the blade.

$\alpha$

is the guide vane angle and

$\beta$

is the blade angle.

The rate of change of momentum, F , is given by:

$F={\dot {m}}\left(V_{w2}-V_{w1}\right)={\dot {m}}\left(V_{f2}\tan \alpha _{2}-V_{f1}\tan \alpha _{1}\right)\,$

(from velocity triangle)

Power consumed by an ideal moving blade, P is given by the equation:

$P={\dot {m}}U\left(V_{f2}\tan \alpha _{2}-V_{f1}\tan \alpha _{1}\right)\,$

Change in enthalpy of fluid in moving blades:

$P={\dot {m}}\left(h_{02}-h_{01}\right)={\dot {m}}c_{p}\left(T_{02}-T_{01}\right)\,$

Therefore,

$P={\dot {m}}U\left(V_{f2}\tan \alpha _{2}-V_{f1}\tan \alpha _{1}\right)={\dot {m}}c_{p}\left(T_{02}-T_{01}\right)\,$

which implies,

$\delta (T_{0})_{\text{isentropic}}={\frac {U}{c_{p}}}\left(V_{f2}\tan \alpha _{2}-V_{f1}\tan \alpha _{1}\right)\,$

*Isentropic compression in rotor blade*,

$p_{2}-p_{1}=p_{1}\left(\left[{\frac {T_{2}}{T_{1}}}\right]^{\frac {\gamma }{\gamma -1}}-1\right)\,$

Therefore,

${\frac {(p_{02})_{\text{actual}}}{p_{01}}}=\left(1+{\frac {\eta _{\text{stage}}\delta (T_{0})_{\text{isentropic}}}{T_{01}}}\right)^{\frac {\gamma }{\gamma -1}}\,$

which implies

${\frac {(p_{02})_{\text{actual}}}{p_{01}}}=\left(1+{\frac {\eta _{\text{stage}}U}{T_{01}c_{p}}}\left[V_{f2}\tan \alpha _{2}-V_{f1}\tan \alpha _{1}\right]\right)^{\frac {\gamma }{\gamma -1}}\,$

*Degree of Reaction*, The pressure difference between the entry and exit of the rotor blade is called reaction pressure. The change in pressure energy is calculated through *degree of reaction*.

${\begin{aligned}R&={\frac {h_{2}-h_{1}}{h_{02}-h_{01}}}\\P&={\dot {m}}c_{p}\left(T_{2}+{\frac {V_{2}^{2}}{2c_{p}}}-\left[T_{1}+{\frac {V_{1}^{2}}{2c_{p}}}\right]\right)\\P&={\dot {m}}\left(h_{2}-h_{1}+\left[{\frac {V_{2}^{2}}{2}}-{\frac {V_{1}^{2}}{2}}\right]\right)\\h_{2}-h_{1}&={\frac {V_{r1}^{2}}{2}}-{\frac {V_{r2}^{2}}{2}}\\T_{2}-T_{1}&={\frac {V_{r1}^{2}}{2c_{p}}}-{\frac {V_{r2}^{2}}{2c_{p}}}\end{aligned}}$

Therefore,

$R={\frac {V_{r1}^{2}-V_{r2}^{2}}{V_{r1}^{2}-V_{r2}^{2}+V_{1}^{2}-V_{2}^{2}}}\,$

## Performance characteristics

### Steady-state performance

Axial compressor performance is shown on a compressor map, also known as a characteristic, by plotting pressure ratio and efficiency against corrected mass flow at different values of corrected compressor speed.

Axial compressors, particularly near their design point are usually amenable to analytical treatment, and a good estimate of their performance can be made before they are first run on a rig. The compressor map shows the complete running range, i.e. off-design, of the compressor from ground idle to its highest corrected rotor speed, which for a civil engine may occur at top-of-climb, or, for a military combat engine, at take-off on a cold day. Not shown is the sub-idle performance region needed for analysing normal ground and in-flight windmill start behaviour.

The performance of a single compressor stage may be shown by plotting stage loading coefficient ( $\psi \,$ ) as a function of flow coefficient ( $\phi \,$ )

Stage pressure ratio against flow rate is lower than for a no-loss stage as shown. Losses are due to blade friction, flow separation, unsteady flow and vane-blade spacing.

### Off-design operation

The performance of a compressor is defined according to its design. But in actual practice, the operating point of the compressor deviates from the design point; this is known as *off-design operation*.

| $\psi =\phi (\tan \alpha _{2}-\tan \alpha _{1})\,$ |   | 1 |
|---|---|---|

| $\tan \alpha _{2}={\frac {1}{\phi }}-\tan \beta _{2}\,$ |   | 2 |
|---|---|---|

from equation (1) and (2)

$\psi =1-\phi (\tan \beta _{2}+\tan \alpha _{1})\,$

The value of $(\tan \beta _{2}+\tan \alpha _{1})\,$ doesn't change for a wide range of operating points till stalling. Also $\alpha _{1}=\alpha _{3}\,$ because of minor change in air angle at rotor and stator, where $\alpha _{3}\,$ is diffuser blade angle.

$J=\tan \beta _{2}+\tan \alpha _{3}\,$

is constant.

Representing design values with (')

| ${\begin{aligned}\psi '&=1-J(\phi ')\,\\J&={\frac {1-\psi '}{\phi '}}\end{aligned}}$ |   | 3 |
|---|---|---|

for off-design operations (from **eq. 3**):

${\begin{aligned}\psi &=1-J(\phi )\,\\\psi &=1-\phi \left({\frac {1-\psi '}{\phi '}}\right)\,\end{aligned}}$

for positive values of J, slope of the curve is negative and vice versa.

## Instabilities

There are multiple modes of instability an axial compressor could undergo. Edward Greitzer used a Helmholtz resonator type of compression system model to predict the transient response of a compression system after a small perturbation superimposed on a steady operating condition. He found a non-dimensional parameter which predicted which mode of compressor instability, rotating stall or surge, would result. The parameter used the rotor speed, the Helmholtz resonator frequency of the system, and an "effective length" of the compressor duct. These produced a critical value which predicted either rotating stall or surge where the slope of pressure ratio against flow changed from negative to positive.

### Surge

In the plot of pressure-flow rate, the line separating graph between two regions – unstable and stable – is known as the **surge line**. This line is formed by joining surge points at different rotational speeds. Surging is the unstable flow in axial compressors due to complete breakdown of the steady through flow. This phenomenon affects the performance of compressor and is undesirable.

### Surge cycle

The following explanation for surging refers to running a compressor at a constant speed on a rig and gradually reducing the exit area by closing a valve. What happens, i.e. crossing the surge line, is caused by the compressor trying to deliver air, still running at the same speed, to a higher exit pressure. When the compressor is operating as part of a complete gas turbine engine, as opposed to on a test rig, a higher delivery pressure at a particular speed can be caused momentarily by burning too-great a step-jump in fuel which causes a momentary blockage until the compressor increases to the speed which goes with the new fuel flow and the surging stops.

Suppose the initial operating point *D* ( ${\dot {m}},P_{D}\,$ ) at some rotational speed *N*. On decreasing the flow-rate at same rotational speed along the characteristic curve by partial closing of the valve, the pressure in the pipe increases which will be taken care by increase in input pressure at the compressor. With further increase in pressure up to point *P* (surge point), compressor pressure will increase. Further moving towards left keeping rotational speed constant, pressure in pipe will increase but compressor pressure will decrease leading to back air flow towards the compressor. Due to this back flow, pressure in pipe will decrease because this unequal pressure condition cannot stay for a long period of time. Though valve position is set for lower flow rate say point *G* but compressor will work according to normal stable operation point say *E*, so path *E*–*F*–*P*–*G*–*E* will be followed leading to breakdown of flow, hence pressure in the compressor falls further to point *H*( $P_{H}\,$ ). This increase and decrease of pressure in pipe will occur repeatedly in pipe and compressor following the cycle *E*–*F*–*P*–*G*–*H*–*E* also known as the surge cycle.

This phenomenon will cause vibrations in the whole machine and may lead to mechanical failure. That is why left portion of the curve from the surge point is called unstable region and may cause damage to the machine. So the recommended operation range is on the right side of the surge line.

### Stall

Stall is a phenomenon affecting the performance of the compressor whereby flow separation occurs at the compressor blades, leading to reduced compression and a drop in engine power. An analysis is made of rotating stall in compressors of many stages, finding conditions under which a flow distortion can occur which is steady in a traveling reference frame, even though upstream total and downstream static pressure are constant. In the compressor, a pressure-rise hysteresis is assumed.

Two types of stall are distinguished: *positive stall,* where flow separation occurs on the suction side of the blade, and *negative stall,* where it occurs on the pressure side. In practice, negative stall is negligible compared to positive stall as flow separation is least likely to occur on the pressure side of the blade.

In a multi-stage compressor, at the high pressure stages, axial velocity is very small. Stalling value decreases with a small deviation from the design point causing stall near the hub and tip regions whose size increases with decreasing flow rates. They grow larger at very low flow rate and affect the entire blade height. Delivery pressure significantly drops with large stalling which can lead to flow reversal, a condition known as *compressor surge.* However, in case of less severe stalling, it is possible for the compressor to remain operational though at a poorer performance, a situation referred to as *rotating stall.*

#### Rotating stall

Non-uniformity of air flow in the rotor blades may disturb local air flow in the compressor without upsetting it. The compressor continues to work normally but with reduced compression. Thus, rotating stall decreases the effectiveness of the compressor.

In a rotor with blades moving say towards right. Let some blades receives flow at higher incidence, this blade will stop positively. It creates obstruction in the passage between the blade to its left and itself. Thus the left blade will receive the flow at higher incidence and the blade to its right with decreased incidence. The left blade will experience more stall while the blade to its right will experience lesser stall. Towards the right stalling will decrease whereas it will increase towards its left. Movement of the rotating stall can be observed depending upon the chosen reference frame.

#### Effects

- This reduces efficiency of the compressor
- Forced vibrations in the blades due to passage through stall compartment.
- These forced vibrations may match with the natural frequency of the blades causing resonance and hence failure of the blade.

## Development

From an energy exchange point of view axial compressors are reversed turbines. Steam-turbine designer Charles Algernon Parsons, for example, recognized that a turbine which produced work by virtue of a fluid's static pressure (i.e. a reaction turbine) could have its action reversed to act as an air compressor, calling it a turbo compressor or pump. His rotor and stator blading described in one of his patents had little or no camber although in some cases the blade design was based on propeller theory. The machines, driven by steam turbines, were used for industrial purposes such as supplying air to blast furnaces. Parsons supplied the first commercial axial flow compressor for use in a lead smelter in 1901. Parsons' machines had low efficiencies, later attributed to blade stall, and were soon replaced with more efficient centrifugal compressors. Brown Boveri & Cie produced "reversed turbine" compressors, driven by gas turbines, with blading derived from aerodynamic research which were more efficient than centrifugal types when pumping large flow rates of 40,000 ft3/min (19 m3/s) at pressures up to 45 psi (310 kPa).

Because early axial compressors were not efficient enough a number of papers in the early 1920s claimed that a practical axial-flow turbojet engine would be impossible to construct. Things changed after A. A. Griffith published a seminal paper in 1926, noting that the reason for the poor performance was that existing compressors used flat blades and were essentially "flying stalled". He showed that the use of airfoils instead of the flat blades would increase efficiency to the point where a practical jet engine was a real possibility. He concluded the paper with a basic diagram of such an engine, which included a second turbine that was used to power a propeller.

Although Griffith was well known due to his earlier work on metal fatigue and stress measurement, little work appears to have started as a direct result of his paper. The only obvious effort was a test-bed compressor built by Hayne Constant, Griffith's colleague at the Royal Aircraft Establishment. Other early jet efforts, notably those of Frank Whittle and Hans von Ohain, were based on the more robust and better understood centrifugal compressor which was widely used in superchargers. Griffith had seen Whittle's work in 1929 and dismissed it, noting a mathematical error, and going on to claim that the frontal size of the engine would make it useless on a high-speed aircraft.

Real work on axial-flow engines started in the late 1930s, in several efforts that all started at about the same time. In England, Hayne Constant reached an agreement with the steam turbine company Metropolitan-Vickers (Metrovick) in 1937, starting their turboprop effort based on the Griffith design in 1938. In 1940, after the successful run of Whittle's centrifugal-flow design, their effort was re-designed as a pure jet, the Metrovick F.2. In Germany, von Ohain had produced several working centrifugal engines, some of which had flown including the world's first jet aircraft (He 178), but development efforts had moved on to Junkers (Jumo 004) and BMW (BMW 003), which used axial-flow designs in the world's first jet fighter (Messerschmitt Me 262) and jet bomber (Arado Ar 234). In the United States, both Lockheed and General Electric were awarded contracts in 1941 to develop axial-flow engines, the former a pure jet, the latter a turboprop. Northrop also started their own project to develop a turboprop, which the US Navy eventually contracted in 1943. Westinghouse also entered the race in 1942, their project proving to be the only successful one of the US efforts, later becoming the J30.

As Griffith had originally noted in 1929, the large frontal size of the centrifugal compressor caused it to have higher drag than the narrower axial-flow type. Additionally the axial-flow design could improve its compression ratio simply by adding additional stages and making the engine slightly longer. In the centrifugal-flow design the compressor itself had to be larger in diameter, which was much more difficult to fit properly into a thin and aerodynamic aircraft fuselage (although not dissimilar to the profile of radial engines already in widespread use). On the other hand, centrifugal-flow designs remained much less complex (the major reason they "won" in the race to flying examples) and therefore have a role in places where size and streamlining are not so important.

## Axial-flow jet engines

In the jet engine application, the compressor faces a wide variety of operating conditions. On the ground at high power settings the inlet pressure is high, inlet speed zero, and the compressor spun at a variety of speeds as the power is applied. Once in flight the inlet pressure drops, but the inlet speed increases (due to the forward motion of the aircraft) to recover some of this pressure, and the compressor tends to run at a single speed for long periods of time.

There is simply no "perfect" compressor for this wide range of operating conditions. Fixed geometry compressors, like those used on early jet engines, are limited to a design pressure ratio of about 4:1 or 5:1. As with any heat engine, fuel efficiency is strongly related to the compression ratio, so there is very strong financial need to improve the compressor stages beyond these sorts of ratios.

Additionally the compressor may stall if the inlet conditions change abruptly, a common problem on early engines. In some cases, if the stall occurs near the front of the engine, all of the stages from that point on will stop compressing the air. In this situation the energy required to run the compressor drops suddenly, and the remaining hot air in the rear of the engine allows the turbine to speed up the whole engine dramatically. This condition, known as surging, was a major problem on early engines and often led to the turbine or compressor breaking and shedding blades.

For all of these reasons, axial compressors on modern jet engines are considerably more complex than those on earlier designs.

### Spools

All compressors have an optimum point relating rotational speed and pressure, with higher compressions requiring higher speeds. Early engines were designed for simplicity, and used a single large compressor spinning at a single speed. Later designs added a second turbine and divided the compressor into low-pressure and high-pressure sections, the latter spinning faster. This *two-spool* design, pioneered on the Bristol Olympus, resulted in increased efficiency. Further increases in efficiency may be realised by adding a third spool, but in practice the added complexity increases maintenance costs to the point of negating any economic benefit. That said, there are several three-spool engines in use, perhaps the most famous being the Rolls-Royce RB211 (and its successor, the Rolls-Royce Trent), used on a wide variety of commercial aircraft.

### Bleed air, variable stators

As an aircraft changes speed or altitude, the pressure of the air at the inlet to the compressor will vary. In order to "tune" the compressor for these changing conditions, designs starting in the 1950s would "bleed" air out of the middle of the compressor in order to avoid trying to compress too much air in the final stages. This was also used to help start the engine, allowing it to be spun up without compressing much air by bleeding off as much as possible. Bleed systems were already commonly used anyway, to provide airflow into the turbine stage where it was used to cool the turbine blades, as well as provide pressurized air for the air conditioning systems inside the aircraft.

A more advanced design, the *variable stator*, used blades that can be individually rotated around their axis, as opposed to the power axis of the engine. For start up they are rotated to "closed", reducing compression, and then are rotated back into the airflow as the external conditions require. The General Electric J79 was the first major example of a variable stator design, and today it is a common feature of most military engines.

Closing the variable stators progressively, as compressor speed falls, reduces the slope of the surge (or stall) line on the operating characteristic (or map), improving the surge margin of the installed unit. By incorporating variable stators in the first five stages, General Electric Aircraft Engines has developed a ten-stage axial compressor capable of operating at a 23:1 design pressure ratio.

## Design notes

### Energy exchange between rotor and fluid

The relative motion of the blades to the fluid adds velocity or pressure or both to the fluid as it passes through the rotor. The fluid velocity is increased through the rotor, and the stator converts kinetic energy to pressure energy. Some diffusion also occurs in the rotor in most practical designs.

The increase in velocity of the fluid is primarily in the tangential direction (swirl) and the stator removes this angular momentum.

The pressure rise results in a stagnation temperature rise. For a given geometry the temperature rise depends on the square of the tangential Mach number of the rotor row. Current turbofan engines have fans that operate at Mach 1.7 or more, and require significant containment and noise suppression structures to reduce blade loss damage and noise.

### Compressor maps

A map shows the performance of a compressor and allows determination of optimal operating conditions. It shows the mass flow along the horizontal axis, typically as a percentage of the design mass flow rate, or in actual units. The pressure rise is indicated on the vertical axis as a ratio between inlet and exit stagnation pressures.

A surge or stall line identifies the boundary to the left of which the compressor performance rapidly degrades and identifies the maximum pressure ratio that can be achieved for a given mass flow. Contours of efficiency are drawn as well as performance lines for operation at particular rotational speeds.

### Compression stability

Operating efficiency is highest close to the stall line. If the downstream pressure is increased beyond the maximum possible the compressor will stall and become unstable.

Typically the instability will be at the Helmholtz frequency of the system, taking the downstream plenum into account.
