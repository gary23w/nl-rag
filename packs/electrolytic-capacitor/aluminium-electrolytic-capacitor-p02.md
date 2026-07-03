---
title: "Aluminum electrolytic capacitor (part 2/2)"
source: https://en.wikipedia.org/wiki/Aluminium_electrolytic_capacitor
domain: electrolytic-capacitor
license: CC-BY-SA-4.0
tags: electrolytic capacitor
fetched: 2026-07-03
part: 2/2
---

## Electrical parameters

The electrical characteristics of capacitors are harmonized by the international generic specification IEC 60384-1. In this standard, the electrical characteristics of capacitors are described by an idealized series-equivalent circuit with electrical components that model all ohmic losses, capacitive and inductive parameters of an electrolytic capacitor:

- *C*, the capacitance of the capacitor,
- *R*ESR, the equivalent series resistance, which summarizes all ohmic losses of the capacitor, usually abbreviated as "ESR".
- *L*ESL, the equivalent series inductance, which is the effective self-inductance of the capacitor, usually abbreviated as "ESL".
- *R*leakage, the resistance that represents the leakage current

### Capacitance standard values and tolerances

The basic unit of electrolytic capacitors capacitance is the microfarad (μF, or less correctly uF).

The capacitance value specified in manufacturers' data sheets is called the rated capacitance CR or nominal capacitance CN and is the value for which the capacitor has been designed. Standardized measuring conditions for electrolytic capacitors are an AC measurement with 0.5 V at a frequency of 100/120 Hz and a temperature of 20 °C.

The capacitance value of an electrolytic capacitor depends on the measuring frequency and temperature. The value at a measuring frequency of 1 kHz is about 10% less than the 100/120 Hz value. Therefore, the capacitance values of electrolytic capacitors are not directly comparable and differ from those of film capacitors or ceramic capacitors, whose capacitance is measured at 1 kHz or higher.

Measured with an AC measuring method with 100/120 Hz the measured capacitance value is the closest value to the electrical charge stored in the capacitor. The stored charge is measured with a special discharge method and is called DC capacitance. The DC capacitance is about 10% higher than the 100/120 Hz AC capacitance. The DC capacitance is of interest for discharge applications like photoflash.

The percentage of allowed deviation of the measured capacitance from the rated value is called capacitance tolerance. Electrolytic capacitors are available in different tolerance series, whose values are specified in the E series specified in IEC 60063. For abbreviated marking in tight spaces, a letter code for each tolerance is specified in IEC 60062.

- rated capacitance, E3 series, tolerance ±20%, letter code "M"
- rated capacitance, E6 series, tolerance ±20%, letter code "M"
- rated capacitance, E12 series, tolerance ±10%, letter code "K"

The required capacitance tolerance is determined by the particular application. Electrolytic capacitors that are often used for filtering and bypassing capacitors do not need narrow tolerances because they are not used for accurate frequency applications, such as for oscillators.

### Rated and category voltage

In IEC 60384-1 the allowed operating voltage is called the "rated voltage" UR or the "nominal voltage" UN. The rated voltage is the maximum DC voltage or peak pulse voltage that may be applied continuously at any temperature within the rated temperature range.

The voltage proof of electrolytic capacitors, which is directly proportional to the dielectric layer thickness, decreases with increasing temperature. For some applications it is important to use a high temperature range. Lowering the voltage applied at a higher temperature maintains safety margins. For some capacitor types, therefore, the IEC standard specifies a second "temperature derated voltage" for a higher temperature range, the "category voltage" UC. The category voltage is the maximum DC voltage, peak pulse voltage or superimposed AC voltage that may be applied continuously to a capacitor at any temperature within the category temperature range.

### Surge voltage

Aluminum electrolytic capacitors can be applied for a short time with an overvoltage, also called a surge voltage. The surge voltage indicates the maximum voltage value within the temperature range that may be applied during the lifetime at a frequency of 1000 cycles (with a dwell time of 30 seconds and a pause of 5 minutes and 30 seconds in each instance) without causing any visible damage to the capacitor or a capacitance change of more than 15%.

Usually, for capacitors with a rated voltage of ≤ 315 volts, the surge voltage is 1.15 times the rated voltage and for capacitors with a rated voltage exceeding 315 volts the surge voltage is 1.10 times the rated voltage.

### Transient voltage

Aluminum electrolytic capacitors with non-solid electrolyte are relatively insensitive to high and short-term transient voltages higher than the surge voltage, if the frequency and the energy content of the transients is low. This ability depends on the rated voltage and component size. Low energy transient voltages lead to a voltage limitation similar to a zener diode.

The electrochemical oxide forming processes take place when voltage in correct polarity is applied and generates an additional oxide when transients arise. This formation is accompanied with heat and hydrogen gas generation. This is tolerable if the energy content of the transient is low. However, when a transient peak voltage causes an electric field strength that is too high for the dielectric, it can directly cause a short circuit. An unambiguous and general specification of tolerable transients or peak voltages is not possible. In every case transients arise, the application has to be carefully approved.

Electrolytic capacitors with solid electrolyte cannot withstand transients or peak voltages higher than the surge voltage. Transients for this type of electrolytic capacitor may destroy the component.

### Reverse voltage

Electrolytic capacitors are polarized capacitors and generally require an anode electrode voltage to be positive relative to the cathode voltage. However, the cathode foil of aluminum electrolytic capacitors is provided with a very thin, natural air-originated oxide layer. This oxide layer has a voltage proof of approximately 1 to 1.5 V. Therefore, aluminum electrolytic capacitors with non-solid electrolyte can continuously withstand a very small reverse voltage and, for example, can be measured with an AC voltage of about 0.5 V, as specified in relevant standards.

At a reverse voltage lower than −1.5 V at room temperature, the cathode aluminum foil begins to build up an oxide layer corresponding to the applied voltage. This is aligned with generating hydrogen gas with increasing pressure. At the same time the oxide layer on the anode foil begins dissolution of the oxide, which weakens the voltage proof. It is now a question of the outside circuit whether the increasing gas pressure from oxidization leads to bursting of the case, or the weakened anode oxide leads to a breakdown with a short circuit. If the outside circuit is high-ohmic the capacitor fails and the vent opens due to high gas pressure. If the outside circuit is low-ohmic, an internal short-circuit is more likely. In every case a reverse voltage lower than −1.5 V at room temperature may cause the component to catastrophically fail due to a dielectric breakdown or overpressure, which causes the capacitor to burst, often in a spectacularly dramatic fashion. Modern electrolytic capacitors have a safety vent that is typically either a scored section of the case or a specially designed end seal to vent the hot gas/liquid, but ruptures can still be dramatic.

To minimize the likelihood of a polarized electrolytic being incorrectly inserted into a circuit, the polarity is very clearly indicated on the case, see the section headed "Polarity marking".

Special bipolar capacitors designed for AC operation, usually referred to as "bipolar", "non-polarized" or "NP" types, are available. In these, the capacitors have two anode foils of opposite polarity connected in series. On each of the alternate halves of the AC cycle, one anode acts as a blocking dielectric, preventing reverse voltage from damaging the opposite anode. The voltage rating does not need to be symmetrical; "semi-polar" capacitors can be made with different thicknesses of oxide coatings, so they can withstand different voltages in each direction, but these bipolar electrolytic capacitors are not adaptable for main AC applications instead of power capacitors with metallized polymer film or paper dielectric.

### Impedance

In general, a capacitor is seen as a storage component for electric energy. But this is only one capacitor function. A capacitor can also act as an AC resistor. Especially aluminum electrolytic capacitors are used in many applications as a decoupling capacitors to filter or bypass undesired biased AC frequencies to the ground or for capacitive coupling of audio AC signals. Then the dielectric is used only for blocking DC. For such applications the AC resistance, the impedance is as important as the capacitance value.

The impedance is the vector sum of reactance and resistance; it describes the phase difference and the ratio of amplitudes between sinusoidally varying voltage and sinusoidally varying current at a given frequency in an AC circuit. In this sense impedance can be used like Ohm's law

$Z={\frac {\hat {u}}{\hat {\imath }}}={\frac {U_{\mathrm {eff} }}{I_{\mathrm {eff} }}}.$

In other words, impedance is a frequency-dependent AC resistance and possesses both magnitude and phase at a particular frequency.

In capacitor data sheets, only the impedance magnitude |Z| is specified, and simply written as "Z". In this sense the impedance is a measure of the capacitor's ability to pass alternating currents.

Impedance can be calculated using the idealized components of a capacitor's series-equivalent circuit, including an ideal capacitor $\scriptstyle C$ , a resistor $\scriptstyle ESR$ , and an inductance $\scriptstyle ESL$ . In this case the impedance at the angular frequency $\omega$ is therefore given by the geometric (complex) addition of ESR, by a capacitive reactance (Capacitance)

$X_{C}=-{\frac {1}{\omega C}}$

and by an inductive reactance (Inductance)

$X_{L}=\omega L_{\mathrm {ESL} }$

.

Then Z is given by

$Z={\sqrt {{ESR}^{2}+(X_{\mathrm {C} }+(-X_{\mathrm {L} }))^{2}}}$

.

In the special case of resonance, in which the both reactive resistances $\scriptstyle X_{C}$ and $\scriptstyle X_{L}$ have the same value ( $\scriptstyle X_{C}=X_{L}$ ), then the impedance is only determined by $\scriptstyle ESR$ .

The impedance specified in the data sheets of various capacitors often shows typical curves for different capacitance values. The impedance at the resonant frequency defines the best working point for coupling or decoupling circuits. The higher the capacitance the lower the operable frequency range. Due to their large capacitance values, aluminum electrolytic capacitors have relatively good decoupling properties in the lower frequency range up to about 1 MHz or a little more. This and the relatively low price is often the reason for using electrolytic capacitors in 50/60 Hz standard or switched-mode power supplies.

### ESR and dissipation factor tan δ

- Typical impedance and ESR curves as a function of frequency and temperature
- (Typical impedance and ESR as a function of frequency) Typical impedance and ESR as a function of frequency
- (Typical impedance as a function of temperature) Typical impedance as a function of temperature

The equivalent series resistance (ESR) summarizes all resistive losses of the capacitor. These are the terminal resistances, the contact resistance of the electrode contact, the line resistance of the electrodes, the electrolyte resistance, and the dielectric losses in the dielectric oxide layer.

ESR depends on temperature and frequency. For aluminum electrolytic capacitors with non-solid electrolyte the ESR generally decreases with increasing frequency and temperature. ESR influences the remaining superimposed AC ripple behind smoothing and may influence circuit functionality. Related to the capacitor, ESR is accountable for internal heat generation if a ripple current flows over the capacitor. This internal heat reduces capacitor lifetime.

Referring to the IEC/EN 60384-1 standard, the impedance values of electrolytic capacitors are measured at 10 kHz or 100 kHz, depending on the capacitance and voltage of the capacitor.

For aluminum electrolytic capacitors, for historical reasons sometimes the dissipation factor tan δ is specified in the relevant data sheets instead of the $\scriptstyle ESR$ . The dissipation factor is determined by the tangent of the phase angle between the capacitive reactance $\scriptstyle X_{C}$ minus the inductive reactance $\scriptstyle X_{L}$ and the $\scriptstyle ESR$ . If the inductance $\scriptstyle ESL$ is small, the dissipation factor for a given frequency can be approximated as:

$\tan \delta ={\mbox{ESR}}\cdot \omega C$

### Ripple current

A ripple current is the RMS value of a superimposed AC current of any frequency and any waveform of the current curve for continuous operation. It arises, for example, in power supplies (including switched-mode power supplies) after rectifying an AC voltage and flows as biased charge and discharge current through the decoupling or smoothing capacitor.

Due to the ESR of the capacitor the ripple current IR causes electrical power losses *PV el*

$P_{Vel}=I_{R}^{2}\cdot \ ESR$

which result in heat generation inside the capacitor winding core.

This internally generated heat, together with ambient temperature and possibly other external heat sources, leads to a capacitor core temperature whose hottest area is located in the winding, having a temperature difference of *Δ T* compared with the ambient temperature. This heat has to be distributed as thermal losses *PV th* over the capacitor's surface *A* and the thermal resistance *β* to the ambient environment.

$P_{Vth}=\Delta T\cdot A\cdot \beta$

The thermal resistance β depends on the case size of the relevant capacitor and if applicable on additional cooling conditions.

If the internally generated power losses *PV el* dissipated by thermal radiation, convection, and thermal conduction to the ambient environment correspond to the thermal losses *PV th,*, then a temperature balance between capacitor temperature and ambient temperature is given.

Typically, the specified rated value for maximum ripple current in manufacturers' data sheets is calculated for a heating the capacitor core (cell) of 10 °C for 85 °C series, 5 °C for 105 °C series and 3 °C for 125 °C series.

The rated ripple current of aluminum electrolytic capacitors with non-solid electrolyte corresponds with the specified lifetime of the capacitor series. This current may flow permanent over the capacitor up to the maximum temperature during the specified or calculated time. Ripple current lower than specified or forced cooling lengthen the capacitor's lifetime.

The lifetime of electrolytic capacitors with non-solid electrolyte depends on the evaporation rate and therefore on the core temperature of the capacitor. With forced cooling or special positioning of the capacitor on the PCB the lifetime can be influenced positively.

The ripple current is specified as an effective (RMS) value at 100 or 120 Hz or at 10 kHz at upper category temperature. Non-sinusoidal ripple currents have to be analyzed and separated into their single sinusoidal frequencies by means of Fourier analysis and summarized by squared addition of the single currents.

$I_{R}={\sqrt {{i_{1}}^{2}+{i_{2}}^{2}+{i_{3}}^{2}+{i_{n}}^{2}}}$

Periodically appearing high current pulses, which may be much higher than the rated ripple current, have to be analyzed in the same matter.

Because the ESR decreases with increasing frequencies. the ripple current data sheet value, specified at 100/120 Hz, can be higher at higher frequencies. In cases like this manufacturers specify correction factors for ripple current values at higher frequencies. For example, the ripple current at 10 kHz can usually be approximated to be 30 to 40% higher than the 100/120 value.

If the ripple current exceeds the rated value, the corresponding heat generation exceeds the capacitor's temperature limit and may destroy the internal structure (voltage proof, boiling point) of the capacitors. Then the components tend to short circuiting, vent opening or explosion. Ripple currents higher than rated values are possible only with forced cooling.

### Charge/discharge stability

Aluminum electrolytic capacitors with non-solid electrolytes always contain, in addition to the anode foil, a cathode foil that serves as electrical contact to the electrolyte. This cathode foil is provided with a very thin, natural, air-originated oxide layer, which act also as a dielectric. Thus, the capacitor construction forms a series circuit of two capacitors, the capacitance of the anode foil CA and the cathode foil CK. As described above, the capacitance of the capacitor Ce-cap is mainly determined by the anode capacitance CA when the cathode capacitance CK is approximately 10 times higher than the anode capacitance CA.

Aluminum electrolytic capacitors with non-solid electrolytes normally can be charged up to the rated voltage without any current limitation. This property is a result of the limited ion movability in the liquid electrolyte, which slows down the voltage ramp across the dielectric, and the capacitor's ESR.

During discharging the internal construction of the capacitor reverses the internal polarity. The cathode (-) gets an anode (+), and changes the current flow direction. Two voltages arise over these electrode. In principle the voltage distribution over both electrodes behaves as the reciprocally CV product of each electrode.

The design rule of high cathode capacitance assures that the voltage appearing over the cathode during discharge is not higher than roughly 1.5 V, that is its natural air-originated voltage proof. No further post-forming of the cathode foil takes place, which may lead to capacitance degradation. Then the capacitors are discharge-proof.

### Current surge, peak or pulse current

Small (diameter <25 mm) aluminum electrolytic capacitors with non-solid electrolytes can normally be charged up to the rated voltage without any current surge, peak or pulse limitation up to a peak current value of about 50 A. This property is a result of the limited ion movability in the liquid electrolyte, which slows down the voltage ramp across the dielectric, and the capacitor's ESR. Only the frequency of peaks integrated over time must not exceed the maximal specified ripple current.

### Leakage current

A characteristic property of electrolytic capacitors is the "leakage current". This DC current is represented by the resistor Rleak in parallel with the capacitor in the series-equivalent circuit of electrolytic capacitors, and flows if a voltage is applied.

The leakage current includes all weak imperfections of the dielectric caused by unwanted chemical processes and mechanical damage and is the DC current that can pass through the dielectric after applying a voltage in correct polarity. It depends on the capacitance value, on applied voltage and temperature of the capacitor, on measuring time, on the kind of electrolyte, and on preconditions like previous storage time without voltage applied or thermic stress from soldering. (All non-solid electrolytic capacitors needs a recovery time of some hours after soldering before measuring the leakage current. Non-solid chip capacitors need a recovery time after reflow soldering of about 24 hours.) Leakage current is reduced by applying operational voltage by self-healing processes.

The leakage current drops in the first minutes after applying DC voltage. In this time the dielectric oxide layer can repair all weaknesses by building up new layers in a self-healing process. The time it takes leakage current to drop generally depends on the kind of electrolyte. Solid electrolytes' leakage current drops much faster than in the case of non-solid types, but it remain at a somewhat higher level. Wet electrolytic capacitors with high water content electrolytes in the first minutes generally have higher leakage current than those with organic electrolyte, but after several minutes they reach the same level. Although the leakage current of electrolytic capacitors is higher compared with the current flow over the insulation resistance at ceramic or film capacitors, the self-discharge of modern non-solid electrolytic capacitors can take several weeks.

The leakage current *Ileak* specification in manufacturers' data sheets refers to the capacitor's capacitance value *CR,* rated voltage *UR,* a correlation factor and a minimum current value. For example,

$I_{\mathrm {Leak} }=0{.}01\,\mathrm {{A} \over {V\cdot F}} \cdot U_{\mathrm {R} }\cdot C_{\mathrm {R} }+3\,\mathrm {\mu A}$

After a measuring time of 2 or 5 minutes, depending on the data sheet specification, the measured leakage current value has to be lower than the calculated value. Normally the leakage current is always lower the longer the capacitor voltage is applied. The leakage current during operation after, for example, one hour is the operational leakage current. This value depends strongly on the manufacturer's series characteristics. It could be lower than 1/100 of the specified value.

The leakage current depends on the applied voltage and the ambient temperature. The value during continuous operation at 85 °C is approximately four times higher than at 20 °C. Otherwise the value is approximately one half, reducing the applied voltage to 70% of the rated voltage.

Non-solid aluminum electrolytic capacitors that leakage current after an operation time of, for example, one hour remain on a higher level than specified. Mostly they have been mechanically damaged internally due to high mechanical stress during mounting.

### Dielectric absorption (soakage)

Dielectric absorption occurs when a capacitor that has remained charged for a long time discharges only incompletely when briefly discharged. Although an ideal capacitor would reach zero volts after discharge, real capacitors develop a small voltage from time-delayed dipole discharging, a phenomenon that is also called dielectric relaxation, "soakage" or "battery action".

| Type of capacitor | Dielectric absorption |
|---|---|
| Tantalum electrolytic capacitors with solid electrolyte | 2 to 3%, 10% |
| Aluminium electrolytic capacitor with non solid electrolyte | 10 to 15% |

Dielectric absorption may be a problem in circuits using very small currents in electronic circuits, such as long-time-constant integrators or sample-and-hold circuits. Dielectric absorption is not a problem in most applications of electrolytic capacitors supporting power supply lines.

But especially for electrolytic capacitors with high rated voltage the voltage at the terminals generated by the dielectric absorption can be a safety risk to personnel or circuits. In order to prevent shocks most very large capacitors are shipped with shorting wires that need to be removed before use.


## Reliability, lifetime and failure modes

### Reliability (failure rate)

The reliability prediction of aluminum electrolytic capacitors is generally expressed as a Failure rate λ, abbreviated FIT (Failures In Time). It is a measure of the number of failures per unit hour during the time of constant random failures in the bathtub curve. The flat part in the bathtub curve corresponds with the calculated lifetime or service life of non-solid electrolytic capacitors. The failure rate is used to calculate a survival probability for a desired lifetime of an electronic circuit in combination with other participating components.

FIT is the number of failures that can be expected in one billion (109) component-hours of operation at fixed working conditions (e.g., 1000 components for 1 million hours, or 1 million components for 1000 hours) (1 ppm/1000 hours) each during the period of constant random failures. This failure rate model implicitly assumes the idea of "random failure". Individual components fail at random times but at a predictable rate. Failures are short circuits, open circuits and degradation failures (exceeding specified limits of electrical parameters).

The reciprocal value of FIT is the MTBF, the Mean Time Between Failures.

The standard operating conditions for the failure rate FIT are 40 °C and 0.5 UR. For other conditions of applied voltage, current load, temperature, capacitance value, circuit resistance (for tantalum capacitors), mechanical influences and humidity the FIT figure can recalculated with acceleration factors standardized for industrial or military contexts. The higher the temperature and the applied voltage, the higher the failure rate.

It is good to know that for capacitors with solid electrolytes the failure rate is often expressed as per cent failed components per thousand hours (n %/1000 h), and specified at reference conditions 85 °C and rated voltage UR. That is, "n" number of failed components per 105 hours, or in FIT the ten-thousand-fold value per 109 hours but for different reference conditions. For these other conditions the "%I1000 h" figure can be recalculated with acceleration factors standardized for industrial or military contexts.

Most modern aluminum electrolytic capacitors with non-solid electrolytes nowadays are very reliable components with very low failure rates, with predicted life expectancies of decades under normal conditions. It is best practice to have electrolytic capacitors pass a post-forming process step after production, similar to a "burn in, so that early failures are eliminated during production. The FIT values given in data sheets are calculated from the long-time experience of the manufacturer, based on the lifetime test results. Typical reference failure rate values for aluminum electrolytic capacitors with non-solid electrolytes are for low voltages types (6.3–160 V) FIT rates in the range of 1 to 20 FIT and for high voltage types (>160–550 V) FIT rates in the range of 20 to 200 FIT. Field failure rates for aluminum capacitors are in the range of 0.5 to 20 FIT.

The data for the "failure rate" specification are based on the results of lifetime testing (endurance testing). In addition a "field failure rate" is sometimes specified. This figures comes from big customers that noticed failures in the field out of their application. Field failure rates could have much lower values. For aluminum electrolytic capacitors they are in the range of 0.5 to 20 FIT. The field failure rate values are in line with the usual orders of magnitude for electronic components.

### Lifetime, service life

Aluminum electrolytic capacitors with non-solid electrolytes have an exceptional position among electronic components because they work with an electrolyte as liquid ingredient. The liquid electrolyte determines the time-dependent behavior of electrolytic capacitors. They age over time as the electrolyte evaporates. This also implies that there is a sharp decline in useful lifespan with increasing temperature. As a rule of thumb, every 10 degrees rise halves the useful life span. This very slow drying-out of the electrolyte depends on the series construction, ambient temperature, voltage and ripple current load. Lowering the electrolyte over time influences the capacitance, impedance and ESR of the capacitors. The capacitance decreases and impedance and ESR increases with decreasing amounts of electrolyte. The leakage current decreases because all weaknesses are healed after the long forming time. In contrast to electrolytic capacitors with solid electrolytes, "wet" electrolytic capacitors have an "end of life" when the components reach specified maximum changes of capacitance, impedance or ESR. The time period to the "end of life" is called the "lifetime", "useful life", "load life" or "service life". It represents the time of constant failure rate in the failure rate bathtub curve.

Under normal ambient conditions electrolytic capacitors can have more than a 15-year lifetime, but this can be limited depending on the degradation behavior of the rubber bung (which is not typically aged during lifetime testing). This rating is tested with an accelerated aging test called an "endurance test" according to IEC 60384-4-1 with rated voltage at the upper category temperature. One of the challenges with this aging test is the time required to extract any meaningful results. In response to demands for long life, high temperature performance from automotive and green energy applications (solar microvinverters, LEDs, wind turbines, etc.), some capacitors require more than a year's worth of testing (10000 hours) before they can be qualified. Due to this limitation, there has been increasing interest in methodologies to accelerate the test in a manner that still produces relevant results.

The graph at right show the behavior of the electrical parameters of aluminum electrolytic capacitors with non-solid electrolytes due to evaporation of the electrolyte in a 2000 h endurance test at 105 °C. The process of drying out is also detectable by weight loss.

After this endurance test the specified parameter limits to pass the test are, on the one hand, no total failures (short circuit, open circuit) and on the other hand, not reaching degradation failure, a reduction of capacitance over 30% and an increase of the ESR, impedance or loss factor by more than a factor of 3 compared to the initial value. Parameters of the tested component beyond these limits can be counted as evidence of degradation failure.

The testing time and temperature depend on the tested series. That is the reason for the many different lifetime specifications in the data sheets of manufacturers, which are given in the form of a time/temperature indication, for example: 2000 h/85 °C, 2000 h/105 °C, 5000 h/105 °C, 2000 h/125 °C. This figures specifies the minimum lifetime of the capacitors of a series, when exposed at the maximum temperature with applied rated voltage.

Referring to the endurance test, this specification does not include the capacitors' being loaded with the rated ripple current value. But the additional internal heat of 3 to 10 K, depending on the series, which is generated by the ripple current is usually taken into account by the manufacturer due to safety margins when interpreting the results of its endurance tests. A test with an actual applied ripple current is affordable for any manufacturer.

A capacitor's lifetime for different operational conditions can be estimated using special formulas or graphs specified in the data sheets of serious manufacturers. They use different ways achieve the specification; some provide special formulas, others specify their capacitor lifetime calculation with graphs that take into account the influence of applied voltage. The basic principle for calculating the time under operational conditions is the so-called "10-degree-rule".

This rule is also well known as the Arrhenius rule. It characterizes the change of thermic reaction speed. For every 10 °C lower temperature, evaporation halves. That means for every 10 °C lower temperature the lifetime of capacitors doubles.

$L_{x}=L_{\text{Spec}}\cdot 2^{\frac {T_{0}-T_{A}}{10}}$

- ***Lx*** = life time to be estimated
- ***LSpec*** = specified life time (useful life, load life, service life)
- ***T0*** = upper category temperature (°C)
- ***TA*** = temperature (°C) of the case or ambient temperature near the capacitor

If a lifetime specification of an electrolytic capacitor is, for example, 2000 h/105 °C, the capacitor's lifetime at 45 °C can be "calculated" as 128,000 hours—roughly 15 years—by using the 10-degree-rule. Although the result of the longer lifetime at lower temperatures comes from a mathematical calculation, the result is always an estimation of the expected behavior of a group of similar components.

The lifetime of electrolytic capacitors with non-solid electrolytes depends on the evaporations rate and therefore on the core temperature of the capacitor. This core temperature on the other hand depends on the ripple current load. Using the 10-degree-rule with the capacitor case temperature gives a good approach to operational conditions. In case of higher ripple currents the lifetime could be influenced positively with force cooling.

Near the end of the capacitor's lifetime degradation failure begins to appear. At the same time the range of the constant failure rate ends. But even after exceeding the capacitor's specified end of life the electronic circuit is not in immediate danger; only the functionality of the capacitor is reduced. With today's high levels of purity in the manufacture of electrolytic capacitors it is not to be expected that short circuits occur after the end-of-life-point with progressive evaporation combined with parameter degradation.

### Failure modes

Aluminum electrolytic capacitors with non-solid electrolytes have, in terms of quality, a relatively negative public image. This is contrary to industrial experience, where electrolytic capacitors are considered to be reliable components if used within their specified specifications during the calculated lifetime. The negative public image might be, among other reasons, because failed electrolytic capacitors in devices are easily and immediately visible. This is exceptional and not the case with other electronic components.

As with any industrial product, specific causes of failure modes are known for aluminum electrolytic capacitors with non-solid electrolytes. They can be differentiated in failures causes by capacitor development and production, by device production, by capacitor application or by external influences during use.

The capacitor manufacturing industries can only influence the first failure mode. Most manufacturers have had well-structured quality control departments for decades, supervising all development and manufacturing steps. Failure mode flow charts demonstrate this. However, a typical physically or chemically caused major failure mode during application, like "field crystallization" for tantalum capacitors, is not known for non-solid aluminum electrolytic capacitors.

### Capacitor behavior after storage or disuse

In many quarters, electrolytic capacitors are considered very unreliable components when compared to other passives. This is partly a function of the history of these components. Capacitors manufactured during and before World War II sometimes suffered from contamination during manual manufacturing, and in particular chlorine salts were often the reason for corrosive processes leading to high leakage currents. Chlorine acts on aluminum as a catalyst for the formation of unstable oxide without becoming chemically bound itself.

After World War II this problem was known but the measuring equipment was not accurate enough to detect chlorine in very low ppm concentration. The situation improved over the next 20 years and the capacitors became good enough for longer life applications. This leads in turn to a previously unnoticed water driven corrosion, which weakens the stable dielectric oxide layer during storage or disuse. This leads to high leakage currents after storage. Most of the electrolytes in that time contain water, and many of the capacitors reach their end of life by drying out. Water driven corrosion was the reason for recommended precondition instructions.

The first solution in the 1970s was the development of water-free electrolyte systems based on organic solvents. Their advantages, among other things were lower leakage currents and nearly unlimited shelf life, but this led to another problem: the growing mass production with automatic insertion machines requires a washing of the PCB's after soldering; these cleaning solutions contained chloroalkane (CFC) agents. Such halogen solutions sometimes permeate the seal of a capacitor and initiate chlorine corrosion. Again there was a leakage current problem.

The use of CFCs as solvents for dry cleaning have been phased out, for example, by the IPPC directive on greenhouse gases in 1994 and by the volatile organic compounds (VOC) directive of the EU in 1997. In the meantime electrolytic systems have been developed with additives to inhibit the reaction between anodic aluminum oxide and water, which solve most of the high leakage current problems after storage.

The ability of non-solid aluminum electrolytic capacitors to have a stable behavior during longer storage times can be tested using an accelerating test of storing the capacitor at its upper category temperature for a certain period, usually 1000 hours, without voltage applied. This "shelf life test" is a good indicator for an inert chemical behavior of the electrolytic system against the dielectric aluminum oxide layer because all chemical reactions are accelerated by high temperatures. Nearly all today's series of capacitors fulfill the 1000 hours shelf life test, which is equivalent to a minimum five years of storage at room temperature. Modern electrolytic capacitors do not need preconditioning after such storage. However, many capacitor series are specified only for two years storage time, but the limit is set by oxidation of terminals and resulting solderability problems.

For restoring antique radio equipment using older electrolytic capacitors built in the 1970s or earlier, "pre-conditioning" is often recommended. For this purpose, the rated voltage is applied to the capacitor via a series resistance of approximately 1 kΩ for a period of one hour. Applying a voltage via a safety resistor repairs the oxide layer by self-healing, but slowly, minimizing internal heating. If capacitors still do not meet the leakage current requirements after preconditioning, it may be an indication of permanent damage.


## Additional information

### Capacitor symbols

|   |   |   |   |
|---|---|---|---|
| Electrolytic capacitor | Electrolytic capacitor | Electrolytic capacitor | Bipolar electrolytic capacitor |

Capacitor symbols

### Parallel connection

Smaller or low voltage aluminum electrolytic capacitors may be connected in parallel without any safety correction action. Large sizes capacitors, especially large sizes and high voltage types, should be individually guarded against sudden energy charge of the whole capacitor bank due to a failed specimen.

### Series connection

Some applications like AC/AC converters with DC-link for frequency controls in three-phase grids need higher voltages than electrolytic capacitors usually offer. For such applications electrolytic capacitors can be connected in series for increased voltage-withstanding capability. During charging, the voltage across each of the capacitors connected in series is proportional to the inverse of the individual capacitor's leakage current. Since every capacitor differs somewhat in individual leakage current, the capacitors with a higher leakage current will get less voltage. The voltage balance over the series-connected capacitors is not symmetrical. Passive or active voltage balance has to be provided in order to stabilize the voltage over each individual capacitor.

### Imprinted markings

Electrolytic capacitors, like most other electronic components, have imprinted markings to indicate the manufacturer, the type, the electrical and thermal characteristics, and the date of manufacture. In the ideal case, if they are large enough the capacitor should be marked with:

- Manufacturer's name or trademark;
- Manufacturer's type designation;
- Polarity of the terminations (for polarized capacitors)
- Rated capacitance;
- Tolerance on rated capacitance
- Rated voltage and nature of supply (AC or DC)
- Climatic category or rated temperature;
- Year and month (or week) of manufacture;

Smaller capacitors use a shorthand notation to display all the relevant information in the limited space available. The most commonly used format is: XYZ K/M VOLTS V, where XYZ represents the capacitance in μF, the letters K or M indicate the tolerance (±10% and ±20% respectively), and VOLTS V represents the rated voltage. Example:

- A capacitor with the following text on its body: 10K 25 has a capacitance of 10 μF, tolerance K = ±10% with a rated voltage of 25 V.

Capacitance, tolerance, and date of manufacture can also be identified with a short code according to IEC 60062. Examples of short-marking of the rated capacitance (microfarads):

- μ47 = 0.47 μF, 4μ7 = 4.7 μF, 47μ = 47 μF

The date of manufacture is often printed in accordance with international standards in abbreviated form.

- Version 1: coding with year/week numeral code, "1208" is "2012, week number 8".
- Version 2: coding with year code/month code,

Year code: "R" = 2003, "S"= 2004, "T" = 2005, "U" = 2006, "V" = 2007, "W" = 2008, "X" = 2009, "A" = 2010, "B" = 2011, "C" = 2012, "D" = 2013, "E" = 2014, "F" = 2015 etc. Month code: "1" to "9" = Jan. to Sept., "O" = October, "N" = November, "D" = December "C5" is then "2012, May"

### Polarity marking

- Polarity marking for non-solid and solid aluminum electrolytic capacitors

- Aluminum electrolytic capacitors with non-solid electrolyte have a polarity marking at the cathode (minus) side
- Aluminum electrolytic capacitors with solid electrolyte have a polarity marking at the anode (plus) side

SMD style electrolytic capacitors with non-solid electrolyte (vertical-chips, V-chips) have a colored filled half circle or a minus bar on the top case side visible to indicate the minus terminal side. Additionally, the insulating plate under the capacitor body uses two skewed edges to indicate that the negative terminal is on the complement position.

Radial or single-ended electrolytic capacitors have a bar across the side of the capacitor to indicate the negative terminal. The negative terminal lead may be shorter than the positive terminal lead (similar to LEDs). In addition, the negative terminal may have a knurled surface stamped on the top of the connecting lug.

Axial electrolytic capacitor styles have a bar across or around the case pointing to the negative lead end to indicate the negative terminal. The positive terminal of the capacitor is on the side of the sealing. The negative terminal lead is shorter than the positive terminal lead.

On a printed circuit board it is customary to indicate the correct orientation by using a square through-hole pad for the positive lead and a round pad for the negative one.

### Standardization

The standardization for all electrical, electronic components and related technologies follows the rules given by the International Electrotechnical Commission (IEC), a non-profit, non-governmental international standards organization.

The definition of the characteristics and the procedure of the test methods for capacitors for use in electronic equipment are set out in the Generic Specification:

- IEC/EN 60384-1—*Fixed capacitors for use in electronic equipment*

The tests and requirements to be met by aluminum electrolytic capacitors for use in electronic equipment for approval as standardized types are set out in the following Sectional Specifications:

- IEC/EN 60384-3—*Surface mount fixed tantalum electrolytic capacitors with manganese dioxide solid electrolyte*
- IEC/EN 60384-4—*Aluminium electrolytic capacitors with solid (MnO2) and non-solid electrolyte*
- IEC/EN 60384-18—*Fixed aluminum electrolytic surface mount capacitors with solid (MnO2) and non-solid electrolyte*
- IEC/EN 60384-25—*Surface mount fixed aluminum electrolytic capacitors with conductive polymer solid electrolyte*
- IEC/EN 60384-26—*Fixed aluminum electrolytic capacitors with conductive polymer solid electrolyte*


## Applications and market

### Applications

Typical applications of aluminum electrolytic capacitors with non-solid electrolyte are:

- Input and output decoupling capacitors for smoothing and filtering in AC power supplies and switched-mode power supplies, as well as in DC/DC-converters
- DC-link capacitors in AC/AC converters for variable-frequency drive and frequency changers as well as in uninterruptible power supplies
- Correction capacitors for power-factor correction
- Energy storage for airbags, photoflash devices, civil detonators
- Motor start capacitors for AC motors
- Bipolar capacitors for audio signal coupling
- Flash capacitor for camera flashes

### Advantages and disadvantages

Advantages:

- Inexpensive capacitors with high capacitance values for filtering lower frequencies
- Higher energy density than film capacitors and ceramic capacitors
- Higher power density than supercapacitors
- No peak current limitation required
- Impassible to transients
- Very great diversification in styles, series with tailored lifetimes, temperatures, and electrical parameters
- Many manufacturers

Disadvantages:

- Limited lifetime due to evaporation
- Relatively poor ESR and Z behavior at very low temperatures
- Sensitive to mechanical stress
- Sensitive to contamination with halogenates
- Polarized application

### Market

The market for aluminum electrolytic capacitors in 2010 was around US$3.9 billion (approximately €2.9 billion), about 22% of the value of the total capacitor market of approximately US$18 billion (2008). In number of pieces these capacitors cover about 6% of the total capacitor market of some 70 to 80 billion pieces.

### Manufacturers and products

Worldwide operating manufacturers and their aluminum electrolytic capacitor product program'

Manufacturer

Available styles

SMD-

Radial

Axial

Snap-in

Screw-

terminal

Bipolar

Audio

Motor-

start

Polymer

Polymer-

Hybrid

CapXon

,

X

X

–

X

X

X

–

X

X

Daewoo, (Partsnic)

Archived

2018-06-12 at the

Wayback Machine

X

X

–

X

–

–

–

–

–

Cornell Dubilier, (CDE)

X

X

X

X

X

–

X

X

X

Capacitor Industries

–

–

–

X

X

–

X

–

–

Chinsan, (Elite)

–

X

–

X

X

X

X

X

–

Elna

X

X

–

X

X

X

–

X

–

Frolyt

X

X

X

–

X

–

–

–

–

Fischer & Tausche

–

X

X

X

X

–

X

–

–

Hitachi

–

–

–

X

X

–

–

–

–

Hitano

X

X

X

X

–

–

–

–

–

Illinois Capacitor

X

X

X

X

X

X

–

–

–

Itelcond

–

–

–

X

X

–

–

–

–

Jackcon

X

X

X

X

–

X

–

–

–

Jianghai

X

X

–

X

X

–

–

X

–

Lelon

X

X

–

X

X

X

–

X

–

Kaimei Electronic Corp, (Jamicon)

X

X

–

X

X

X

–

X

–

KEMET-Evox-Rifa Group

X

X

X

X

X

–

X

–

–

Kyocera AVX

X

X

–

X

X

–

X

X

X

MAN YUE, (Capxon)

X

X

–

X

X

X

–

–

–

Nantung

X

X

–

X

–

X

–

–

–

Nippon Chemi-Con, (NCC, ECC, UCC)

X

X

X

X

X

X

–

X

X

NIC

X

X

–

X

–

X

–

X

X

Nichicon

Archived

2018-06-12 at the

Wayback Machine

X

X

–

X

X

X

–

X

X

YMIN

X

X

-

X

X

-

-

X

X

Panasonic, Matsushita

X

X

X

X

–

X

–

X

X

Richey Capacitor Inc. Richey

X

X

X

X

–

–

–

–

–

Rubycon

X

X

–

X

X

X

–

X

–

SUN Electronic Industry

–

X

–

–

–

–

–

X

–

Suntan

X

X

X

X

X

X

–

X

–

TDK EPCOS

–

X

X

X

X

–

–

–

–

Vishay, (BCc, Roederstein)

X

X

X

X

X

–

–

–

–

Würth Elektronik eiSos

X

X

–

X

X

X

–

X

–

Yageo

X

X

–

X

X

–

–

X

–
