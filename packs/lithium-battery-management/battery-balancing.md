---
title: "Battery balancing"
source: https://en.wikipedia.org/wiki/Battery_balancing
domain: lithium-battery-management
license: CC-BY-SA-4.0
tags: lithium-ion battery, battery management system, state of charge, battery balancing
fetched: 2026-07-02
---

# Battery balancing

**Battery balancing** and **battery redistribution** refer to techniques that improve the available capacity of a battery pack with multiple cells (usually in series) and increase each cell's longevity. A *battery balancer* or *regulator* is an electrical device in a battery pack that performs battery balancing. Circuitry that includes designs to balance cell charges during battery pack recharging may be either *active* or *passive* in its design, and is most often found in lithium-ion batteries, e.g., for laptop computers, electrical vehicles. etc.

## Rationale

The individual cells in a battery pack naturally have somewhat different capacities, and so, over the course of charge and discharge cycles, may be at a different state of charge (SOC). Variations in capacity are due to manufacturing variances, assembly variances (e.g., cells from one production run mixed with others), cell aging, impurities, or environmental exposure (e.g., some cells may be subject to additional heat from nearby sources like motors, electronics, etc.), and can be exacerbated by the cumulative effect of parasitic loads, such as the cell monitoring circuitry often found in a battery management system (BMS).

Balancing a multi-cell pack helps to maximize capacity and service life of the pack by working to maintain equivalent state-of-charge of every cell, to the degree possible given their different capacities, over the widest possible range. Balancing is only necessary for packs that contain more than one cell in series. Parallel cells will naturally balance since they are directly connected to each other, but groups of parallel wired cells, wired in series (parallel-series wiring) must be balanced between cell groups.

### Implications for safety

To ensure safe operation and prevent hazardous conditions, the battery management system (BMS) continuously tracks critical parameters like temperature and voltage at the individual cell level, detecting any potential deviations that could lead to failure. While current is typically monitored at the pack level to optimize performance, the BMS may include one-shot protection mechanisms at the cell level to rapidly disconnect cells in case of an abnormally high current, such as during a short circuit or other fault conditions.

Under normal operation, discharging must stop when any cell first runs out of charge even though other cells may still hold significant charge. Likewise, charging must stop when any cell reaches its maximum safe charging voltage. Failure to do either may cause permanent damage to the cells, or in extreme cases, may drive cells into reverse polarity, cause internal gassing, thermal runaway, or other catastrophic failures. If the cells are not balanced, such that the high and low cutoff are at least aligned with the state of the lowest capacity cell, the energy that can be taken from and returned to the battery will be limited.

Because lithium chemistries often permit flexible membrane structures, lithium cells can be deployed in flexible though sealed bags, which permits higher packing densities within a battery pack. When a lithium cell is mistreated, some of the breakdown products (usually of electrolyte chemicals or additives) outgas. Such cells will become 'puffy' and are very much on the way to failure. In sealed lithium-ion cylindrical-format batteries, the same outgassing has caused rather large pressures (800+ psi has been reported); such cells can explode if not provided with a pressure relief mechanism. Compounding the danger is that many lithium cell chemistries include hydrocarbon chemicals (the exact nature of which is typically proprietary), and these are flammable. Therefore, in addition to the risk of cell mistreatment potentially causing an explosion, a simple non-explosive leak can cause a fire.

Most battery chemistries have less dramatic, and less dangerous, failure modes. The chemicals in most batteries are often toxic to some degree, but are rarely explosive or flammable; many are corrosive, which accounts for advice to avoid leaving batteries inside equipment for long periods as the batteries may leak and damage the equipment. Lead acid batteries are an exception, for charging them generates hydrogen gas, which can explode if exposed to an ignition source (e.g., a lit cigarette ) and such an explosion will spray sulfuric acid in all directions. Since this is corrosive and potentially blinding, this is a particular danger.

## Technology

Balancing can be *active* or *passive*. In active balancing, the balancer circuit enables transfer of charge between different cells of the battery, i.e., transferring energy from cells with a higher charge to cells with a lower charge.

The term *battery regulator* typically refers only to devices that perform passive balancing. A full BMS might include active balancing as well as temperature monitoring, charging, and other features to maximize the life of a battery pack.

Battery balancing can be performed by DC-DC converters, in one of three topologies:

- Cell-to-battery,
- Battery-to-cell, or
- Bidirectional.

Typically, the power handled by each DC-DC converter is a few orders of magnitude lower than the power handled by the battery pack as a whole.

### Passive balancing

In passive balancing, energy is drawn from the most charged cell and dissipated as heat, usually through resistors.

Passive balancing equalizes the state of charge at some fixed point—usually either "top balanced", with all cells reaching 100% SOC at the same time; or "bottom balanced", with all cells reaching minimum SOC at the same time. This can be accomplished by bleeding energy from the cells with higher state of charge (e.g., a controlled short through a resistor or transistor), or shunting energy through a path in parallel with a cell during the charge cycle so that less of the (typically regulated constant) current is consumed by the cell. Passive balancing is inherently wasteful, with some of the pack's energy spent as heat for the sake of equalizing the state of charge between cells. The build-up of waste heat may also limit the rate at which balancing can occur.

### Active balancing

In active balancing, energy may be drawn from the most charged cell and transferred to the least charged cells, e.g., through capacitor-based, inductor-based, or DC-DC converters.

Active balancing attempts to redistribute energy from cells at full charge to those with a lower state of charge. Energy can be bled from a cell at higher SOC by switching a reservoir capacitor in-circuit with the cell, then disconnecting the capacitor and reconnecting it to a cell with lower SOC, or through a DC-to-DC converter connected across the entire pack. Due to inefficiencies, some energy is still wasted as heat, but not to the same degree. Despite the obvious advantages, the additional cost and complexity of an active balancing topology can be substantial, and doesn't always make sense depending on the application.

Another variant sometimes used on electric bicycle battery packs uses a multi pin connector with a resistor and diode in series on each node: as the drops are known the charger then applies either a suitable discharge current or charges the weak cells until they all read the same loaded terminal voltage. This has the advantage of reducing pack weight slightly and lowering parasitic draw, as well as permitting multi-point balancing.
