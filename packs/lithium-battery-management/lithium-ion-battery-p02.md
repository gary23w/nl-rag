---
title: "Lithium-ion battery (part 2/2)"
source: https://en.wikipedia.org/wiki/Lithium-ion_battery
domain: lithium-battery-management
license: CC-BY-SA-4.0
tags: lithium-ion battery, battery management system, state of charge, battery balancing
fetched: 2026-07-02
part: 2/2
---

## Safety

The problem of lithium-ion battery safety was recognized even before were first commercially released in 1991. The two main reasons for lithium-ion battery fires and explosions are related to processes on the negative electrode (anode when discharging, cathode when charging). During a normal battery charge lithium ions intercalate into graphite. However, if the charge is too fast or the temperature is too low lithium metal starts plating on the negative electrode, and the resulting dendrites can penetrate the battery separator, internally short-circuit the cell, and result in high electric current, heating and ignition. In other mechanisms, an explosive reaction between the negative electrode material (LiC6) and the solvent (liquid organic carbonate) occurs even at open circuit, provided that the electrode temperature exceeds a certain threshold above 70 °C.

Lithium-ion batteries in the 18650 format or larger may incorporate safety mechanisms such as a current interrupt device (CID) and a positive temperature coefficient (PTC) device. The CID consists of two metal disks in electrical contact. When internal pressure increases, the disks separate, breaking the circuit and terminating the current. The PTC device is composed of a conductive polymer; an increase in current causes the polymer to heat, increasing its electrical resistance and reducing the current flow.

### Fire hazard

Lithium-ion batteries can be a safety hazard since they contain a flammable electrolyte and may become pressurized if they become damaged. A battery cell charged too quickly could cause a short circuit, leading to overheating, explosions, and fires. A Li-ion battery fire can be started due to

1. thermal abuse, e.g. poor cooling or external fire,
2. electrical abuse, e.g. overcharge or external short circuit,
3. mechanical abuse, e.g. penetration or crash, or
4. internal short circuit, e.g. due to manufacturing flaws or aging.

Because of these risks, testing standards are more stringent than those for acid-electrolyte batteries, requiring both a broader range of test conditions and additional battery-specific tests, and there are shipping limitations imposed by safety regulators. There have been battery-related recalls by some companies, including the 2016 Samsung Galaxy Note 7 recall for battery fires.

Lithium-ion batteries have a flammable liquid electrolyte. A faulty battery can cause a serious fire. Faulty chargers can affect the safety of the battery because they can destroy the battery's protection circuit. While charging at temperatures below 0 °C, the negative electrode of the cells gets plated with pure lithium, which can compromise the safety of the whole pack.

Short-circuiting a battery will cause the cell to overheat and possibly to catch fire. Smoke from thermal runaway in a Li-ion battery is both flammable and toxic. Batteries are tested according to the UL 9540A fire standard, and the TS-800 standard also tests fire propagation from one battery container to adjacent containers.

Around 2010, large lithium-ion batteries were introduced in place of other chemistries to power systems on some aircraft; as of January 2014, there had been at least four serious lithium-ion battery fires, or smoke, on the Boeing 787 passenger aircraft, introduced in 2011, which did not cause crashes but had the potential to do so. UPS Airlines Flight 6 crashed in Dubai after its payload of batteries spontaneously ignited.

To reduce fire hazards, research projects are intended to develop non-flammable electrolytes.

### Damaging and overloading

If a lithium-ion battery is damaged, crushed, or subjected to a higher electrical load without having overcharge protection, problems may arise. External short circuit can trigger a battery explosion. Such incidents can occur when lithium-ion batteries are not disposed of through the appropriate channels, but are thrown away with other waste. The way they are treated by recycling companies can damage them and cause fires, which in turn can lead to large-scale conflagrations. Twelve such fires were recorded in Swiss recycling facilities in 2023.

If overheated or overcharged, Li-ion batteries may suffer thermal runaway and cell rupture. During thermal runaway, internal degradation and oxidization processes can keep cell temperatures above 500 °C, with the possibility of igniting secondary combustibles, as well as leading to leakage, explosion or fire in extreme cases. To reduce these risks, many lithium-ion cells (and battery packs) contain fail-safe circuitry that disconnects the battery when its voltage is outside the safe range of 3–4.2 V per cell, or when overcharged or discharged. Lithium battery packs, whether constructed by a vendor or the end-user, without effective battery management circuits are susceptible to these issues. Poorly designed or implemented battery management circuits also may cause problems; it is difficult to be certain that any particular battery management circuitry is properly implemented.

### Voltage limits

Lithium-ion cells are susceptible to stress by voltage ranges outside of safe ones between 2.5 and 3.65/4.1/4.2 or 4.35 V (depending on the components of the cell). Exceeding this voltage range results in premature aging and in safety risks due to the reactive components in the cells. When stored for long periods the small current draw of the protection circuitry may drain the battery below its shutoff voltage; normal chargers may then be useless since the battery management system (BMS) may retain a record of this battery (or charger) "failure". Many types of lithium-ion cells cannot be charged safely below 0 °C, as this can result in plating of lithium on the anode of the cell, which may cause complications such as internal short-circuit paths.

Other safety features are required in each cell:

- Shut-down separator (for overheating)
- Tear-away tab (for internal pressure relief)
- Vent (pressure relief in case of severe outgassing)
- Thermal interrupt (overcurrent/overcharging/environmental exposure)

These features are required because the negative electrode produces heat during use, while the positive electrode may produce oxygen. However, these additional devices occupy space inside the cells, add points of failure, and may irreversibly disable the cell when activated. Further, these features increase costs compared to nickel metal hydride batteries, which require only a hydrogen/oxygen recombination device and a back-up pressure valve. Contaminants inside the cells can defeat these safety devices. Also, these features can not be applied to all kinds of cells, e.g., prismatic high-current cells cannot be equipped with a vent or thermal interrupt. High-current cells must not produce excessive heat or oxygen, lest there be a failure, possibly violent. Instead, they must be equipped with internal thermal fuses which act before the anode and cathode reach their thermal limits.

Replacing the lithium cobalt oxide positive electrode material with a lithium metal phosphate such as lithium iron phosphate (LFP) improves cycle counts, shelf life and safety, but lowers capacity. As of 2006, these safer lithium-ion batteries were mainly used in electric cars and other large-capacity battery applications, where safety is critical. In 2016, an LFP-based energy storage system was chosen to be installed in Paiyun Lodge on Mt.Jade (Yushan) (the highest lodge in Taiwan). As of June 2024, the system was still operating safely.

### Recalls

In 2006, approximately 10 million Sony batteries used in laptops were recalled, including those in laptops from Dell, Sony, Apple, Lenovo, Panasonic, Toshiba, Hitachi, Fujitsu and Sharp. The batteries were found to be susceptible to internal contamination by metal particles during manufacture. Under some circumstances, these particles could pierce the separator, causing a dangerous short circuit.

IATA estimates that over a billion lithium metal and lithium-ion cells are flown each year. Some kinds of lithium batteries may be prohibited aboard aircraft because of the fire hazard. Some postal administrations restrict air shipping (including EMS) of lithium and lithium-ion batteries, either separately or installed in equipment.

### Non-flammable electrolyte

In 2023, most commercial Li-ion batteries employed alkylcarbonate solvents to assure the formation solid electrolyte interface on the negative electrode. Since such solvents are readily flammable, there has been active research to replace them with non-flammable solvents or to add fire suppressants. Another source of hazard is hexafluorophosphate anion, which is needed to passivate the negative current collector made of aluminium. Hexafluorophosphate reacts with water and releases volatile and toxic hydrogen fluoride.

Several strategies have been explored for developing non-flammable Li-ion battery electrolytes. One approach uses fluorinated (co-)solvents, such as methyl-(2,2,2-trifluoroethyl)-carbonate (FEMC) or methyl-3,3,3-trifluoropropionate (MTFP). Another approach uses fluorinated anions, such as lithium bis(trifluoromethanesulfonyl)imide or lithium difluoro(oxalato)borate in high concentrations.


## Supply chain

As of 2021, almost 90% of raw lithium extraction originated from three countries: Australia (53%), Chile (24%), and China (10%), with almost all production coming from China (56%), Chile (32%) and Argentina (11%).

### Environmental impact

Extraction of lithium, nickel, and cobalt, manufacture of solvents, and mining byproducts present significant environmental and health hazards. Lithium extraction can be fatal to aquatic life due to water pollution. It is known to cause surface water contamination, drinking water contamination, respiratory problems, ecosystem degradation and landscape damage. It also leads to unsustainable water consumption in arid regions (1.9 million liters per ton of lithium). Massive byproduct generation of lithium extraction also presents unsolved problems, such as large amounts of magnesium and lime waste.

Lithium mining takes place in North and South America, Asia, South Africa, Australia, and China.

Cobalt for Li-ion batteries is largely mined in the Congo (see also Mining industry of the Democratic Republic of the Congo). Open-pit cobalt mining has led to deforestation and habitat destruction in the Democratic Republic of Congo.

Open-pit nickel mining has led to environmental degradation and pollution in developing countries such as the Philippines and Indonesia. In 2024, nickel mining and processing was one of the main causes of deforestation in Indonesia.

Manufacturing a kg of Li-ion battery takes about 67 megajoules (MJ) of energy. The global warming potential of lithium-ion batteries manufacturing strongly depends on the energy source used in mining and manufacturing operations, and is difficult to estimate, but one 2019 study estimated 73 kg CO2e/kWh. Effective recycling can reduce the carbon footprint of the production significantly.

### Solid waste and recycling

The Li-ion battery recycling rate is often misconstrued to be 5%, in reality, insufficient research exists to determine the exact figure. The European Union estimates 49% of portable batteries sold were collected for recycling in 2023, whilst the UK estimates 45% as of 2026. New EU legislation requires 70% of collected Li-ion battery material to be recovered through recycling by 2031, which must include recovery rates of 80% for lithium and 95% for cobalt, nickel, and manganese; however, no recycled lithium has re-entered the EU as of 2023. These measures aim to aid sustainability efforts and reduce pressure on raw material extraction, as demand for lithium and cobalt is expected to increase 8-fold by 2040, far exceeding current production capabilities. Most research focuses on the recovery of active materials, especially lithium which is a critical raw material; however, through advanced recycling techniques and more sustainable design considerations, electrolytes, binders, and separators can also recycled.

Recycling is a multi-step process, starting with the storage of batteries before disposal, followed by manual testing, disassembling, and finally the chemical separation of battery components. Re-use of the battery is preferred over complete recycling as there is less embodied energy in the process. As these batteries are a lot more reactive than classical vehicle waste like tire rubber, there are significant risks to stockpiling used batteries.

#### Pyrometallurgical recovery

The pyrometallurgical method uses a high-temperature furnace to reduce the components of the metal oxides in the battery to an alloy of Co, Cu, Fe, and Ni. This is the most common and commercially established method of recycling and can be combined with other similar batteries to increase smelting efficiency and improve thermodynamics. The metal current collectors aid the smelting process, allowing whole cells or modules to be melted at once. The product of this method is a collection of metallic alloy, slag, and gas. At high temperatures, the polymers used to hold the battery cells together burn off and the metal alloy can be separated through a hydrometallurgical process into its separate components. The slag can be further refined or used in the cement industry. The process is relatively risk-free and the exothermic reaction from polymer combustion reduces the required input energy. However, in the process, the plastics, electrolytes, and lithium salts will be lost.

#### Hydrometallurgical metals reclamation

This method involves the use of aqueous solutions to remove the desired metals from the cathode. The most common reagent is sulfuric acid. Factors that affect the leaching rate include the concentration of the acid, time, temperature, solid-to-liquid-ratio, and reducing agent. It is experimentally proven that H2O2 acts as a reducing agent to speed up the rate of leaching through the reaction:

2 LiCoO

2

(s)

+ 3 H

2

SO

4

+ H

2

O

2

→ 2 CoSO

4

(aq)

+ Li

2

SO

4

+ 4 H

2

O + O

2

Once leached, the metals can be extracted through precipitation reactions controlled by changing the pH level of the solution. Cobalt, the most expensive metal, can then be recovered in the form of sulfate, oxalate, hydroxide, or carbonate. More recently, recycling methods experiment with the direct reproduction of the cathode from the leached metals. In these procedures, concentrations of the various leached metals are premeasured to match the target cathode and then the cathodes are directly synthesized.

The main issues with this method, however, are the large volume of solvent required and the high cost of neutralization. Although it is easy to shred up the battery, mixing the cathode and anode at the beginning complicates the process, so they will also need to be separated. Unfortunately, the current design of batteries makes the process extremely complex and it is difficult to separate the metals in a closed-loop battery system. Shredding and dissolving may occur at different locations.

#### Direct recycling

Direct recycling is the removal of the cathode or anode from the electrode, which are then reconditioned and reused in a new battery. Mixed metal-oxides can be added to the new electrode with very little change to the crystal morphology. The process generally involves the addition of new lithium to replenish the loss of lithium in the cathode due to degradation from cycling. Cathode strips are obtained from the dismantled batteries, then soaked in NMP, and undergo sonication to remove excess deposits. It is treated hydrothermally with a solution containing LiOH/Li2SO4 before annealing.

This method is extremely cost-effective for noncobalt-based batteries as the raw materials do not make up the bulk of the cost. Direct recycling avoids the time-consuming and expensive purification steps, which is great for low-cost cathodes such as LiMn2O4 and LiFePO4. For these cheaper cathodes, most of the cost, embedded energy, and carbon footprint is associated with the manufacturing rather than the raw material. It is experimentally shown that direct recycling can reproduce similar properties to pristine graphite.

The drawback of the method lies in the condition of the retired battery. In the case where the battery is relatively healthy, direct recycling can cheaply restore its properties. However, for batteries where the state of charge is low, direct recycling may not be worth the investment. The process must also be tailored to the specific cathode composition, and therefore the process must be configured to one type of battery at a time. Lastly, in a time with rapidly developing battery technology, the design of a battery today may no longer be desirable a decade from now, rendering direct recycling ineffective.

#### Physical materials separation

Physical materials separation recovered materials by mechanical crushing and exploiting physical properties of different components such as particle size, density, ferromagnetism and hydrophobicity. Copper, aluminum and steel casing can be recovered by sorting. The remaining materials, called "black mass", which is composed of nickel, cobalt, lithium and manganese, need a secondary treatment to recover.

#### Biological metals reclamation

For the biological metals reclamation or bio-leaching, the process uses microorganisms to digest metal oxides selectively. Then, recyclers can reduce these oxides to produce metal nanoparticles. Although bio-leaching has been used successfully in the mining industry, this process is still nascent to the recycling industry and plenty of opportunities exists for further investigation.

#### Electrolyte recycling

Electrolyte recycling consists of two phases. The collection phase extracts the electrolyte from the spent Li-ion battery. This can be achieved through mechanical processes, distillation, freezing, solvent extraction, and supercritical fluid extraction. Due to the volatility, flammability, and sensitivity of the electrolyte, the collection process poses a greater difficulty than the collection process for other components of a Li-ion battery. The next phase consists of separation/electrolyte regeneration. Separation consists of isolating the individual components of the electrolyte. This approach is often used for the direct recovery of the Li salts from the organic solvents. In contrast, regeneration of the electrolyte aims to preserve the electrolyte composition by removing impurities which can be achieved through filtration methods.

The recycling of the electrolytes, which consists 10–15 wt.% of the Li-ion battery, provides both economic and environmental benefits. These benefits include the recovery of the valuable Li-based salts and the prevention of hazardous compounds, such as volatile organic compounds (VOCs) and carcinogens, being released into the environment.

Compared to electrode recycling, less focus is placed on recycling the electrolyte of Li-ion batteries due to lower economic benefits and greater process challenges. Such challenges can include the difficulty associated with recycling different electrolyte compositions, removing side products accumulated from electrolyte decomposition during its runtime, and removal of electrolyte adsorbed onto the electrodes. Due to these challenges, current pyrometallurgical methods of Li-ion battery recycling forgo electrolyte recovery, releasing hazardous gases upon heating. However, due to high energy consumption and environmental impact, future recycling methods are being directed away from this approach.

### Human rights impact

Extraction of raw materials for lithium-ion batteries may present dangers to local people, especially land-based indigenous populations.

Cobalt sourced from the Democratic Republic of the Congo is often mined by workers using hand tools with few safety precautions, resulting in frequent injuries and deaths. Pollution from these mines has exposed people to toxic chemicals that health officials believe to cause birth defects and breathing difficulties. Human rights activists have alleged, and investigative journalism reported confirmation, that child labor is used in these mines.

A study of relationships between lithium extraction companies and indigenous peoples in Argentina indicated that the state may not have protected indigenous peoples' right to free prior and informed consent, and that extraction companies generally controlled community access to information and set the terms for discussion of the projects and benefit sharing.

Development of the Thacker Pass lithium mine in Nevada, USA has been met with protests and lawsuits from several indigenous tribes who have said they were not provided free prior and informed consent and that the project threatens cultural and sacred sites. Links between resource extraction and missing and murdered indigenous women have also prompted local communities to express concerns that the project will create risks to indigenous women. Protestors have been occupying the site of the proposed mine since January, 2021.


## Research

Researchers are actively working to improve the power density, safety, cycle durability (battery life), recharge time, cost, flexibility, and other characteristics, as well as research methods and uses, of these batteries. Solid-state batteries are being researched as a breakthrough in technological barriers. Currently, solid-state batteries are expected to be the most promising next-generation battery, and various companies are working to popularize them.

Research areas for lithium-ion batteries include extending lifetime, increasing energy density, improving safety, reducing cost, and increasing charging speed, among others. Research has been under way in the area of non-flammable electrolytes as a pathway to increased safety based on the flammability and volatility of the organic solvents used in the typical electrolyte. Strategies include aqueous lithium-ion batteries, ceramic solid electrolytes, polymer electrolytes, ionic liquids, and heavily fluorinated systems.

One of the ways to improve batteries is to combine the various cathode materials. This allows researchers to improve on the qualities of a material, while limiting the negatives. One possibility is coating lithium nickel manganese oxide with lithium iron phosphate through resonant acoustic mixing. The resulting material benefits from an increase electrochemical performance and improved capacity retention. Similar work was done with iron (III) phosphate. As it is now accepted that not only transition metals, but also anions in cathodes participate in redox activity necessary for lithium insertion and removal, the design of cathode materials with diverse transition metal cations increasingly consider also oxygen redox reactions in lithium-ion battery cathodes and how these may enhance capacity beyond transition metal limitations, with computational studies using density functional theory helping to optimize materials while minimizing structural degradation. Advances in anionic redox understanding have led to stabilization strategies like surface fluorination, improving cycling stability and safety.
