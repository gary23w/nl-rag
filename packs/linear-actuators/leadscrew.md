---
title: "Leadscrew"
source: https://en.wikipedia.org/wiki/Leadscrew
domain: linear-actuators
license: CC-BY-SA-4.0
tags: linear actuator, ball screw, leadscrew drive, rack and pinion
fetched: 2026-07-02
---

# Leadscrew

A **leadscrew** (or **lead screw**), pronounced /liːd skruː/, also known as a **power screw** or **translation screw**, is a screw used as a linkage in a machine, to translate turning motion into linear motion. Because of the large area of sliding contact between their male and female members, screw threads have larger frictional energy losses compared to other linkages. They are not typically used to carry high power, but more for intermittent use in low power actuator and positioner mechanisms. Leadscrews are commonly used in linear actuators, machine slides (such as in machine tools), vises, presses, and jacks. The word "lead" – pronounced /liːd/, from the verb "to lead" – refers to the amount of distance travelled per rotation, not the metal.

Leadscrews are manufactured in the same way as other thread forms: they may be rolled, cut, or ground.

A lead screw is sometimes used with a split nut (also called a half nut) which allows the nut to be disengaged from the threads and moved axially, independently of the screw's rotation, when needed (such as in single-point threading on a manual lathe). A split nut can also be used to compensate for wear by compressing the parts of the nut.

A hydrostatic leadscrew overcomes many of the disadvantages of a normal leadscrew, having high positional accuracy, very low friction, and very low wear, but requires continuous supply of high-pressure fluid and high-precision manufacture, leading to significantly greater cost than most other linear motion linkages.

## Types

Power screws are classified by the geometry of their thread.

### V-thread

V-threads are less suitable for leadscrews than others such as Acme because they have more friction between the threads. Their threads are designed to induce this friction to keep the fastener from loosening. Leadscrews, on the other hand, are designed to minimize friction. Therefore, in most commercial and industrial use, V-threads are avoided for leadscrew use. Nevertheless, V-threads are sometimes successfully used as leadscrews, for example on microlathes and micromills.

### Square thread

Square threads are named after their square geometry. They are the most efficient, having the least friction, so they are often used for screws that carry high power; however, they are also the most difficult to machine, and are thus the most expensive.

### Acme thread / Trapezoidal thread

Acme threads have a 29° thread angle, which is easier to machine than square threads. They are not as efficient as square threads, due to the increased friction induced by the thread angle. Acme threads are generally also stronger than square threads due to their trapezoidal thread profile, which provides greater load-bearing capabilities.

### Buttress thread

Buttress threads are of a triangular shape. These are used where the load force on the screw is only applied in one direction. They are as efficient as square threads in these applications, but are easier to manufacture.

## Advantages and disadvantages

The advantages of a leadscrew are:

- Large load carrying capability
- Compactness
- Simplicity of design
- Ease of manufacture
- Large mechanical advantage
- Precise and accurate linear motion
- Smooth and quiet operation
- Low maintenance
- Minimal number of parts
- Most are self-locking (cannot be back-driven)

The disadvantages are that most are not very efficient. Due to this low efficiency, they cannot be used in continuous power transmission applications. They also have a high degree of friction on the threads, which can wear the threads out quickly. For square threads, the nut must be replaced; for trapezoidal threads, a split nut may be used to compensate for the wear.

## Alternatives

Alternatives to actuation by leadscrew include:

- Ball screws and roller screws (sometimes categorized as types of leadscrew rather than in contradistinction)
- Fluid power (i.e., hydraulics and pneumatics)
- Gear trains (e.g., worm drives, rack-and-pinion drives)
- Electromagnetic actuation (e.g., solenoids)
- Piezoelectric actuation

## Mechanics

The torque required to lift or lower a load can be calculated by "unwrapping" one revolution of a thread. This is most easily described for a square or buttress thread as the thread angle is 0 and has no bearing on the calculations. The unwrapped thread forms a right angle triangle where the base is $\pi d_{\text{m}}$ long and the height is the lead (pictured to the right). The force of the load is directed downward, the normal force is perpendicular to the hypotenuse of the triangle, the frictional force is directed in the opposite direction of the direction of motion (perpendicular to the normal force or along the hypotenuse), and an imaginary "effort" force is acting *horizontally* in the direction opposite the direction of the frictional force. Using this free-body diagram the torque required to lift or lower a load can be calculated:

$T_{\text{raise}}={\frac {Fd_{\text{m}}}{2}}\left({\frac {l+\pi \mu d_{\text{m}}}{\pi d_{\text{m}}-\mu l}}\right)={\frac {Fd_{\text{m}}}{2}}\tan {\left(\phi +\lambda \right)}$

$T_{\text{lower}}={\frac {Fd_{\text{m}}}{2}}\left({\frac {\pi \mu d_{\text{m}}-l}{\pi d_{\text{m}}+\mu l}}\right)={\frac {Fd_{\text{m}}}{2}}\tan {\left(\phi -\lambda \right)}$

| Screw material | Nut material |   |   |   |
|---|---|---|---|---|
| Steel | Bronze | Brass | Cast iron |   |
| Steel, dry | 0.15–0.25 | 0.15–0.23 | 0.15–0.19 | 0.15–0.25 |
| Steel, machine oil | 0.11–0.17 | 0.10–0.16 | 0.10–0.15 | 0.11–0.17 |
| Bronze | 0.08–0.12 | 0.04–0.06 | - | 0.06–0.09 |

where

- T = torque
- F = load on the screw
- $d_{\text{m}}$ = mean diameter
- $\mu \,$ = coefficient of friction (common values are found in the adjacent table)
- l = lead
- $\phi \,$ = angle of friction
- $\lambda \,$ = lead angle

Based on the $T_{\text{lower}}$ equation, it can be found that the screw is self-locking when the coefficient of friction is greater than the tangent of the lead angle. An equivalent comparison is when the friction angle is greater than the lead angle ( $\phi >\lambda$ ). However, this self-locking property is not absolute. Under dynamic conditions—particularly in the presence of vibration or shock loading—the effective coefficient of friction may drop to dynamic levels (which are typically lower than static), allowing the screw to back-drive unexpectedly. For this reason, safety-critical applications often require a secondary holding brake rather than relying solely on the lead screw geometry.

### Efficiency

The efficiency, calculated using the torque equations above, is:

${\mbox{efficiency}}={\frac {T_{0}}{T_{\text{raise}}}}={\frac {Fl}{2\pi T_{\text{raise}}}}={\frac {\tan {\lambda }}{\tan {\left(\phi +\lambda \right)}}}$

### Non-zero thread angle

For screws that have a thread angle other than zero, such as a trapezoidal thread, this must be compensated as it increases the frictional forces. The equations below take this into account:

$T_{\text{raise}}={\frac {Fd_{\text{m}}}{2}}\left({\frac {l+\pi \mu d_{\text{m}}\sec {\alpha }}{\pi d_{\text{m}}-\mu l\sec {\alpha }}}\right)={\frac {Fd_{\text{m}}}{2}}\left({\frac {\mu \sec {\alpha }+\tan {\lambda }}{1-\mu \sec {\alpha }\tan {\lambda }}}\right)$

$T_{\text{lower}}={\frac {Fd_{\text{m}}}{2}}\left({\frac {\pi \mu d_{\text{m}}\sec {\alpha }-l}{\pi d_{\text{m}}+\mu l\sec {\alpha }}}\right)={\frac {Fd_{\text{m}}}{2}}\left({\frac {\mu \sec {\alpha }-\tan {\lambda }}{1+\mu \sec {\alpha }\tan {\lambda }}}\right)$

where $\alpha \,$ is one half the thread angle.

If the leadscrew has a collar which the load rides on, then the frictional forces between the interface must be accounted for in the torque calculations as well. For the following equation the load is assumed to be concentrated at the mean collar diameter ( $d_{\text{c}}$ ):

$T_{\text{c}}={\frac {F\mu _{\text{c}}d_{\text{c}}}{2}}$

where $\mu _{\text{c}}$ is the coefficient of friction between the collar on the load and $d_{\text{c}}$ is the mean collar diameter. For collars that use thrust bearings, the frictional loss is negligible and the above equation can be ignored.

Efficiency for non-zero thread angles can be written as follows:

$\eta ={\frac {\cos \alpha \ -\ \mu \tan \lambda }{\cos \alpha \ +\ \mu \cot \lambda }}$

| Material combination | Starting $\mu _{\text{c}}$ | Running $\mu _{\text{c}}$ |
|---|---|---|
| Soft steel / cast iron | 0.17 | 0.12 |
| Hardened steel / cast iron | 0.15 | 0.09 |
| Soft steel / bronze | 0.10 | 0.08 |
| Hardened steel / bronze | 0.08 | 0.06 |

### Running speed

| Nut material | Safe loads (psi) | Safe loads (bar) | Speed (fpm) | Speed (m/s) |
|---|---|---|---|---|
| Bronze | 2,500–3,500 psi | 170–240 bar | Low speed |   |
| Bronze | 1,600–2,500 psi | 110–170 bar | 10 fpm | 0.05 m/s |
| Cast iron | 1,800–2,500 psi | 120–170 bar | 8 fpm | 0.04 m/s |
| Bronze | 800–1,400 psi | 55–97 bar | 20–40 fpm | 0.10–0.20 m/s |
| Cast iron | 600–1,000 psi | 41–69 bar | 20–40 fpm | 0.10–0.20 m/s |
| Bronze | 150–240 psi | 10–17 bar | 50 fpm | 0.25 m/s |

The running speed for a leadscrew (or ball screw) is typically limited to, at most, 80% of the calculated critical speed. The critical speed is the speed that excites the natural frequency of the screw. For a steel leadscrew or steel ballscrew, the critical speed is approximately

$N={(4.76\times 10^{6})d_{\text{r}}C \over L^{2}}$

where

- N = critical speed in RPM
- $d_{\text{r}}$ = smallest (root) diameter of the leadscrew in inches
- L = length between bearing supports in inches
- C = .36 for one end fixed, one end free
- C = 1.00 for both ends simple
- C = 1.47 for one end fixed, one end simple
- C = 2.23 for both ends fixed

Alternatively using metric units:

$N={\frac {Cd_{\text{r}}\times 10^{7}}{L^{2}}}$

where the variables are identical to above, but the values are in millimetres and C is as follows:

- C = 3.9 for fixed-free supports
- C = 12.1 for both ends supported
- C = 18.7 for fixed-supported structure
- C = 27.2 for both ends fixed
