---
title: "Carnot cycle"
source: https://en.wikipedia.org/wiki/Carnot_cycle
domain: thermodynamic-cycles
license: CC-BY-SA-4.0
tags: thermodynamic cycle, carnot cycle, rankine cycle, heat engine
fetched: 2026-07-02
---

# Carnot cycle

A **Carnot cycle** is an ideal thermodynamic cycle proposed by French physicist Sadi Carnot in 1824 and expanded upon by others in the 1830s and 1840s. By Carnot's theorem, it provides an upper limit on the efficiency of any classical thermodynamic engine during the conversion of heat into work, or conversely, the efficiency of a refrigeration system in creating a temperature difference through the application of work to the system.

In a Carnot cycle, a system or engine transfers energy in the form of heat between two thermal reservoirs at temperatures *T*H and *T*C (referred to as the hot and cold reservoirs, respectively), and a part of this transferred energy is converted to the work done by the system. The cycle is reversible, merely transferring thermal energy between the thermal reservoirs and the system without gain or loss. When work is applied to the system, heat moves from the cold to hot reservoir (heat pump or refrigeration). When heat moves from the hot to the cold reservoir, the system applies work to the environment. The work *W* done by the system or engine to the environment per Carnot cycle depends on the temperatures of the thermal reservoirs per cycle such as *W* = *Q*H(*T*H − *T*C)/*T*H, where *Q*H is heat transferred from the hot reservoir to the system per cycle.

## Stages

A Carnot cycle is an idealized thermodynamic cycle performed by a Carnot heat engine, consisting of the following steps:

1. **Isothermal expansion. Heat (as an energy) is transferred reversibly from the hot temperature reservoir at constant temperature *T*H to the gas at a temperature infinitesimally less than *T*H**. (The infinitesimal temperature difference allows the heat to transfer into the gas without a significant change in the gas temperature. This is called **isothermal heat addition or absorption**.) During this step (1 to 2 on **Figure 1**), the gas is in thermal contact with the hot temperature reservoir, and is thermally isolated from the cold temperature reservoir. The gas is allowed to expand, doing work on the surroundings by pushing up the piston (Stage One figure, right). Although the pressure drops from points 1 to 2 (figure 1) the temperature of the gas does not change during the process because the heat transferred from the hot temperature reservoir to the gas is exactly used to do work on the surroundings by the gas. There is no change in the gas internal energy, and no change in the gas temperature. Heat *Q*H > 0 is absorbed from the hot temperature reservoir.
2. **(reversible adiabatic) expansion of the gas ( work output).** For this step (2 to 3 on **Figure 1**) the gas in the engine is thermally insulated from both the hot and cold reservoirs, thus they neither gain nor lose heat. It is an adiabatic process. The gas continues to expand with reduction of its pressure, doing work on the surroundings (raising the piston; Stage Two figure, right), and losing an amount of internal energy equal to the work done. The loss of internal energy causes the gas to cool. In this step it is cooled to a temperature that is infinitesimally higher than the cold reservoir temperature *T*C.
3. **Isothermal compression. Heat is transferred reversibly to the low temperature reservoir at a constant temperature *T*C (isothermal heat rejection).** In this step (3 to 4 on **Figure 1**), the gas in the engine is in thermal contact with the cold reservoir at temperature *T*C, and is thermally isolated from the hot reservoir. The gas temperature is infinitesimally higher than *T*C to allow heat transfer from the gas to the cold reservoir. There is no change in temperature, it is an isothermal process. The surroundings do work on the gas, pushing the piston down (Stage Three figure, right). An amount of energy earned by the gas from this work exactly transfers as a heat energy *Q*C < 0 (negative as leaving from the system, according to the universal convention in thermodynamics) to the cold reservoir.
4. **Compression.** (4 to 1 on **Figure 1**) Once again the gas in the engine is thermally insulated from the hot and cold reservoirs, and the engine is assumed to be frictionless and the process is slow enough, hence reversible. During this step, the surroundings do work on the gas, pushing the piston down further (Stage Four figure, right), increasing its internal energy, compressing it, and causing its temperature to rise back to the temperature infinitesimally less than *T*H due solely to the work added to the system. At this point the gas is in the same state as at the start of step 1.

In this case, since it is a reversible thermodynamic cycle (no net change in the system and its surroundings per cycle) ${\frac {Q_{\text{H}}}{T_{\text{H}}}}=-{\frac {Q_{\text{C}}}{T_{\text{C}}}}.$

This is true as *Q*C and *T*C are both smaller in magnitude and in fact are in the same ratio as *Q*H/*T*H.

### Pressure–volume graph

When a Carnot cycle is plotted on a pressure–volume diagram (**Figure 1**), the isothermal stages follow the isotherm lines for the working fluid, the adiabatic stages move between isotherms, and the area bounded by the complete cycle path represents the total work that can be done during one cycle. From point 1 to 2 and point 3 to 4 the temperature is constant (isothermal process). Heat transfer from point 4 to 1 and point 2 to 3 are equal to zero (adiabatic process).

### Temperature-entropy graph

A Carnot cycle plotted on a Temperature-entropy diagram (**Figure 4**) is rather simple. Isothermic paths are horizontal, adiabatic paths are vertical. The area enclosed by the cycle is the amount of heat energy extracted from the hot reservoir but not delivered to the cold reservoir, which has been converted into work.

Defining ΔS = *S*B − *S*A, the heat energy injected into the engine is *Q*H = *T*HΔS and the heat energy extracted from the engine is *Q*C = *T*CΔS, which is the portion of the injected energy that is unavailable to do work. The engine is reversibly transporting entropy from the hot reservoir to the cold reservoir.

### Efficiency

The efficiency *η* is defined to be:

| $\eta ={\frac {W}{Q_{\text{H}}}}={\frac {Q_{\text{H}}-Q_{\text{C}}}{Q_{\text{H}}}}=1-{\frac {T_{\text{C}}}{T_{\text{H}}}}$ |   | 3 |
|---|---|---|

where

- W is the work done by the engine system (energy exiting the system as work),
- *Q*C > 0 is the heat taken from the engine system (heat energy leaving the system),
- *Q*H > 0 is the heat put into the engine system (heat energy entering the system),
- *T*C is the absolute temperature of the cold reservoir, and
- *T*H is the absolute temperature of the hot reservoir.

This is the Carnot heat engine working efficiency definition as the fraction of the work done by the engine system to the thermal energy received by the system from the hot reservoir per cycle. This thermal energy is the cycle initiator.

### Reversed Carnot cycle

A Carnot heat-engine cycle described is a totally reversible cycle. That is, all the processes that compose it can be reversed, in which case it becomes the Carnot heat pump and refrigeration cycle. This time, the cycle remains exactly the same except that the directions of any heat and work interactions are reversed. Heat is absorbed from the low-temperature reservoir, heat is rejected to a high-temperature reservoir, and a work input is required to accomplish all this. The *P*–*V* diagram of the reversed Carnot cycle is the same as for the Carnot heat-engine cycle except that the directions of the processes are reversed.

### Carnot's theorem

It can be seen from the above diagram that for any cycle operating between temperatures *T*H and *T*C, none can exceed the efficiency of a Carnot cycle.

**Carnot's theorem** is a formal statement of this fact: *No engine operating between two heat reservoirs can be more efficient than a Carnot engine operating between those same reservoirs.* Thus, Equation **3** gives the maximum efficiency possible for any engine using the corresponding temperatures. A corollary to Carnot's theorem states that: *All reversible engines operating between the same heat reservoirs are equally efficient.* Rearranging the right side of the equation gives what may be a more easily understood form of the equation, namely that the theoretical maximum efficiency of a heat engine equals the difference in temperature between the hot and cold reservoir divided by the absolute temperature of the hot reservoir. Looking at this formula an interesting fact becomes apparent: Lowering the temperature of the cold reservoir will have more effect on the ceiling efficiency of a heat engine than raising the temperature of the hot reservoir by the same amount. In the real world, this may be difficult to achieve since the cold reservoir is often an existing ambient temperature.

In mesoscopic heat engines, work per cycle of operation in general fluctuates due to thermal noise. If the cycle is performed quasi-statically, the fluctuations vanish even on the mesoscale. However, if the cycle is performed faster than the relaxation time of the working medium, the fluctuations of work are inevitable. Nevertheless, when work and heat fluctuations are counted, an exact equality relates the exponential average of work performed by any heat engine to the heat transfer from the hotter heat bath.

### Efficiency of real heat engines

Carnot realized that, in reality, it is not possible to build a thermodynamically reversible engine. So, real heat engines are even less efficient than indicated by Equation **3**. In addition, real engines that operate along the Carnot cycle style (isothermal expansion / adiabatic expansion / isothermal compression / adiabatic compression) are rare. Nevertheless, Equation **3** is extremely useful for determining the maximum efficiency that could ever be expected for a given set of thermal reservoirs.

This can help illustrate, for example, why a reheater or a regenerator can improve the thermal efficiency of steam power plants by increasing the value of *T*H and why the thermal efficiency of combined-cycle power plants (which incorporate gas turbines operating at even higher temperatures) exceeds that of conventional steam plants. The first prototype of the diesel engine was based on the principles of the Carnot cycle.

## As a macroscopic construct

The Carnot heat engine is, ultimately, a theoretical construct based on an *idealized* thermodynamic system. On a practical human-scale level the Carnot cycle has proven a valuable model, as in advancing the development of the diesel engine. However the requirement of perfect reversibility is unattainable in a practical sense, and, ultimately, a perfect Carnot engine is incapable of doing any work in a finite amount of time. As such, per Carnot's theorem, the Carnot engine may be thought as the theoretical limit of macroscopic scale heat engines rather than any practical device that could ever be built.
