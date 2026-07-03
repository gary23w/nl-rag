---
title: "Electrolytic capacitor (part 2/2)"
source: https://en.wikipedia.org/wiki/Electrolytic_capacitor
domain: electrolytic-capacitor
license: CC-BY-SA-4.0
tags: electrolytic capacitor
fetched: 2026-07-03
part: 2/2
---

## Electrical characteristics

### Series-equivalent circuit

The electrical characteristics of capacitors are harmonized by the international generic specification IEC 60384-1. In this standard, the electrical characteristics of capacitors are described by an idealized series-equivalent circuit with electrical components which model all ohmic losses, capacitive and inductive parameters of an electrolytic capacitor:

- *C*, the capacitance of the capacitor
- *R*ESR, the equivalent series resistance which summarizes all ohmic losses of the capacitor, usually abbreviated as "ESR"
- *L*ESL, the equivalent series inductance which is the effective self-inductance of the capacitor, usually abbreviated as "ESL".
- *R*leak, the resistance representing the leakage current of the capacitor

### Capacitance, standard values and tolerances

The electrical characteristics of electrolytic capacitors depend on the structure of the anode and the electrolyte used. This influences the capacitance value of electrolytic capacitors, which depends on measuring frequency and temperature. Electrolytic capacitors with non-solid electrolytes show a broader aberration over frequency and temperature ranges than do capacitors with solid electrolytes.

The basic unit of an electrolytic capacitor's capacitance is the microfarad (μF). The capacitance value specified in the data sheets of the manufacturers is called the rated capacitance CR or nominal capacitance CN and is the value for which the capacitor has been designed.

The standardized measuring condition for electrolytic capacitors is an AC measuring method with 0.5 V at a frequency of 100/120 Hz at a temperature of 20 °C. For tantalum capacitors a DC bias voltage of 1.1 to 1.5  V for types with a rated voltage ≤2.5 V, or 2.1 to 2.5 V for types with a rated voltage of >2.5 V, may be applied during the measurement to avoid reverse voltage.

The capacitance value measured at the frequency of 1 kHz is about 10% less than the 100/120 Hz value. Therefore, the capacitance values of electrolytic capacitors are not directly comparable and differ from those of film capacitors or ceramic capacitors, whose capacitance is measured at 1 kHz or higher.

Measured with an AC measuring method at 100/120 Hz the capacitance value is the closest value to the electrical charge stored in the e-caps. The stored charge is measured with a special discharge method and is called the DC capacitance. The DC capacitance is about 10% higher than the 100/120 Hz AC capacitance. The DC capacitance is of interest for discharge applications like photoflash.

The percentage of allowed deviation of the measured capacitance from the rated value is called the capacitance tolerance. Electrolytic capacitors are available in different tolerance series, whose values are specified in the E series specified in IEC 60063. For abbreviated marking in tight spaces, a letter code for each tolerance is specified in IEC 60062.

- rated capacitance, series E3, tolerance ±20%, letter code "M"
- rated capacitance, series E6, tolerance ±20%, letter code "M"
- rated capacitance, series E12, tolerance ±10%, letter code "K"

The required capacitance tolerance is determined by the particular application. Electrolytic capacitors, which are often used for filtering and bypassing, do not have the need for narrow tolerances because they are mostly not used for accurate frequency applications like in oscillators.

### Rated and category voltage

Referring to the IEC/EN 60384-1 standard, the allowed operating voltage for electrolytic capacitors is called the "rated voltage UR" or "nominal voltage UN". The rated voltage UR is the maximum DC voltage or peak pulse voltage that may be applied continuously at any temperature within the rated temperature range TR.

The voltage proof of electrolytic capacitors decreases with increasing temperature. For some applications it is important to use a higher temperature range. Lowering the voltage applied at a higher temperature maintains safety margins. For some capacitor types therefore the IEC standard specifies a "temperature derated voltage" for a higher temperature, the "category voltage UC". The category voltage is the maximum DC voltage or peak pulse voltage that may be applied continuously to a capacitor at any temperature within the category temperature range TC. The relation between both voltages and temperatures is given in the picture at right.

Applying a higher voltage than specified may destroy electrolytic capacitors.

Applying a lower voltage may have a positive influence on electrolytic capacitors. For aluminium electrolytic capacitors a lower applied voltage can in some cases extend the lifetime. For tantalum electrolytic capacitors lowering the voltage applied increases the reliability and reduces the expected failure rate. I

### Surge voltage

The surge voltage indicates the maximum peak voltage value that may be applied to electrolytic capacitors during their application for a limited number of cycles. The surge voltage is standardized in IEC/EN 60384-1. For aluminium electrolytic capacitors with a rated voltage of up to 315 V, the surge voltage is 1.15 times the rated voltage, and for capacitors with a rated voltage exceeding 315 V, the surge voltage is 1.10 times the rated voltage.

For tantalum electrolytic capacitors the surge voltage can be 1.3 times the rated voltage, rounded off to the nearest volt. The surge voltage applied to tantalum capacitors may influence the capacitor's failure rate.

### Transient voltage

aluminium electrolytic capacitors with non-solid electrolyte are relatively insensitive to high and short-term transient voltages higher than surge voltage, if the frequency and the energy content of the transients are low. This ability depends on rated voltage and component size. Low energy transient voltages lead to a voltage limitation similar to a zener diode. An unambiguous and general specification of tolerable transients or peak voltages is not possible. In every case transients arise, the application has to be approved very carefully.

Electrolytic capacitors with solid manganese oxide or polymer electrolyte, and aluminium as well as tantalum electrolytic capacitors cannot withstand transients or peak voltages higher than the surge voltage. Transients may destroy this type of electrolytic capacitor.

### Reverse voltage

Standard electrolytic capacitors, and aluminium as well as tantalum and niobium electrolytic capacitors are polarized and generally require the anode electrode voltage to be positive relative to the cathode voltage.

Nevertheless, electrolytic capacitors can withstand for short instants a reverse voltage for a limited number of cycles. Specifically, aluminium electrolytic capacitors with non-solid electrolyte can withstand a reverse voltage of about 1 V to 1.5 V. This reverse voltage should never be used to determine the maximum reverse voltage under which a capacitor can be used permanently.

Solid tantalum capacitors can also withstand reverse voltages for short periods. The most common guidelines for tantalum reverse voltage are:

- 10 % of rated voltage to a maximum of 1 V at 25 °C,
- 3 % of rated voltage to a maximum of 0.5 V at 85 °C,
- 1 % of rated voltage to a maximum of 0.1 V at 125 °C.

These guidelines apply for short excursion and should never be used to determine the maximum reverse voltage under which a capacitor can be used permanently.

But in no case, for aluminium as well as for tantalum and niobium electrolytic capacitors, may a reverse voltage be used for a permanent AC application.

To minimize the likelihood of a polarized electrolytic being incorrectly inserted into a circuit, polarity has to be very clearly indicated on the case, see the section on polarity marking below.

Special bipolar aluminium electrolytic capacitors designed for bipolar operation are available, and usually referred to as "non-polarized" or "bipolar" types. In these, the capacitors have two anode foils with full-thickness oxide layers connected in reverse polarity. On the alternate halves of the AC cycles, one of the oxides on the foil acts as a blocking dielectric, preventing reverse current from damaging the electrolyte of the other one. But these bipolar electrolytic capacitors are not suitable for main AC applications instead of power capacitors with metallized polymer film or paper dielectric.

### Impedance

In general, a capacitor is seen as a storage component for electric energy. But this is only one capacitor application. A capacitor can also act as an AC resistor. Aluminium electrolytic capacitors in particular are often used as decoupling capacitors to filter or bypass undesired AC frequencies to ground or for capacitive coupling of audio AC signals. Then the dielectric is used only for blocking DC. For such applications, the impedance (AC resistance) is as important as the capacitance value.

The impedance *Z* is the vector sum of reactance and resistance; it describes the phase difference and the ratio of amplitudes between sinusoidally varying voltage and sinusoidally varying current at a given frequency. In this sense impedance is a measure of the ability of the capacitor to pass alternating currents and can be used like Ohm's law.

$Z={\frac {\hat {u}}{\hat {\imath }}}={\frac {U_{\mathrm {eff} }}{I_{\mathrm {eff} }}}.$

In other words, impedance is a frequency-dependent AC resistance and possesses both magnitude and phase at a particular frequency.

In data sheets of electrolytic capacitors only the impedance magnitude *|Z|* is specified, and simply written as *"Z".* Regarding the IEC/EN 60384-1 standard, the impedance values of electrolytic capacitors are measured and specified at 10 kHz or 100 kHz depending on the capacitance and voltage of the capacitor.

Besides measuring, the impedance can be calculated using the idealized components of a capacitor's series-equivalent circuit, including an ideal capacitor *C*, a resistor *ESR*, and an inductance *ESL*. In this case the impedance at the angular frequency *ω* is given by the geometric (complex) addition of *ESR*, by a capacitive reactance *XC*

$X_{C}=-{\frac {1}{\omega C}}$

and by an inductive reactance *XL* (Inductance)

$X_{L}=\omega L_{\mathrm {ESL} }$ .

Then *Z* is given by

$Z={\sqrt {{ESR}^{2}+(X_{\mathrm {C} }+(-X_{\mathrm {L} }))^{2}}}$

.

In the special case of resonance, in which the both reactive resistances *XC* and *XL* have the same value (*XC=XL*), then the impedance will only be determined by *ESR*. With frequencies above the resonance frequency, the impedance increases again because of the *ESL* of the capacitor. The capacitor becomes an inductor.

### ESR and dissipation factor tan δ

- Typical impedance and ESR curves as a function of frequency and temperature
- (Typical impedance and ESR as a function of frequency) Typical impedance and ESR as a function of frequency
- (Typical impedance as a function of temperature) Typical impedance as a function of temperature

The equivalent series resistance (*ESR*) summarizes all resistive losses of the capacitor. These are the terminal resistances, the contact resistance of the electrode contact, the line resistance of the electrodes, the electrolyte resistance, and the dielectric losses in the dielectric oxide layer.

For electrolytic capacitors, *ESR* generally decreases with increasing frequency and temperature.

*ESR* influences the superimposed AC ripple after smoothing and may influence the circuit functionality. Within the capacitor, *ESR* accounts for internal heat generation if a ripple current flows across the capacitor. This internal heat reduces the lifetime of non-solid aluminium electrolytic capacitors and affects the reliability of solid tantalum electrolytic capacitors.

For electrolytic capacitors, for historical reasons the dissipation factor *tan δ* will sometimes be specified in the data sheet instead of the *ESR*. The dissipation factor is determined by the tangent of the phase angle between the capacitive reactance *XC* minus the inductive reactance *XL* and the *ESR*. If the inductance *ESL* is small, the dissipation factor can be approximated as:

$\tan \delta ={\mbox{ESR}}\cdot \omega C$

The dissipation factor is used for capacitors with very low losses in frequency-determining circuits where the reciprocal value of the dissipation factor is called the quality factor (Q), which represents a resonator's bandwidth.

### Ripple current

"Ripple current" is the RMS value of a superimposed AC current of any frequency and any waveform of the current curve for continuous operation within the specified temperature range. It arises mainly in power supplies (including switched-mode power supplies) after rectifying an AC voltage and flows as charge and discharge current through any decoupling and smoothing capacitors.

Ripple currents generate heat inside the capacitor body. This dissipation power loss *PL* is caused by *ESR* and is the squared value of the effective (RMS) ripple current *IR*.

$P_{L}=I_{R}^{2}\cdot ESR$

This internally generated heat, additional to the ambient temperature and possibly other external heat sources, leads to a capacitor body temperature having a temperature difference of *Δ T* relative to ambient. This heat has to be distributed as thermal losses *Pth* over the capacitor's surface *A* and the thermal resistance *β* to ambient.

$P_{th}=\Delta T\cdot A\cdot \beta$

The internally generated heat has to be distributed to ambient by thermal radiation, convection, and thermal conduction. The temperature of the capacitor, which is the net difference between heat produced and heat dissipated, must not exceed the capacitor's maximum specified temperature.

The ripple current is specified as an effective (RMS) value at 100 or 120 Hz or at 10 kHz at upper category temperature. Non-sinusoidal ripple currents have to be analyzed and separated into their single sinusoidal frequencies by means of Fourier analysis and summarized by squared addition the single currents.

$I_{R}={\sqrt {{i_{1}}^{2}+{i_{2}}^{2}+{i_{3}}^{2}+{i_{n}}^{2}}}$

In non-solid electrolytic capacitors the heat generated by the ripple current causes the evaporation of electrolytes, shortening the lifetime of the capacitors. Exceeding the limit tends to result in explosive failure.

In solid tantalum electrolytic capacitors with manganese dioxide electrolyte the heat generated by the ripple current affects the reliability of the capacitors. Exceeding the limit tends to result in catastrophic failure, failing short-circuit, with visible burning.

The heat generated by the ripple current also affects the lifetime of aluminium and tantalum electrolytic capacitors with solid polymer electrolytes. Exceeding the limit tends to result in catastrophic failure, failing short-circuit.

### Current surge, peak or pulse current

Aluminium electrolytic capacitors with non-solid electrolytes normally can be charged up to the rated voltage without any current surge, peak or pulse limitation. This property is a result of the limited ion movability in the liquid electrolyte, which slows down the voltage ramp across the dielectric, and of the capacitor's ESR. Only the frequency of peaks integrated over time must not exceed the maximal specified ripple current.

Solid tantalum electrolytic capacitors with manganese dioxide electrolyte or polymer electrolyte are damaged by peak or pulse currents. Solid Tantalum capacitors which are exposed to surge, peak or pulse currents, for example, in highly inductive circuits, should be used with a voltage derating. If possible, the voltage profile should be a ramp turn-on, as this reduces the peak current experienced by the capacitor.

### Leakage current

For electrolytic capacitors, DC leakage current (DCL) is a special characteristic that other conventional capacitors do not have. This current is represented by the resistor Rleak in parallel with the capacitor in the series-equivalent circuit of electrolytic capacitors.

The reasons for leakage current are different between electrolytic capacitors with non-solid and with solid electrolyte or more common for "wet" aluminium and for "solid" tantalum electrolytic capacitors with manganese dioxide electrolyte as well as for electrolytic capacitors with polymer electrolytes. For non-solid aluminium electrolytic capacitors the leakage current includes all weakened imperfections of the dielectric caused by unwanted chemical processes taking place during the time without applied voltage (storage time) between operating cycles. These unwanted chemical processes depend on the kind of electrolyte. Water-based electrolytes are more aggressive to the aluminium oxide layer than are electrolytes based on organic liquids. This is why different electrolytic capacitor series specify different storage time without reforming.

Applying a positive voltage to a "wet" capacitor causes a reforming (self-healing) process which repairs all weakened dielectric layers, and the leakage current remain at a low level.

Although the leakage current of non-solid electrolytic capacitors is higher than current flow across the dielectric in ceramic or film capacitors, self-discharge of modern non-solid electrolytic capacitors with organic electrolytes takes several weeks.

The main causes of DCL for solid tantalum capacitors include electrical breakdown of the dielectric; conductive paths due to impurities or poor anodization; and bypassing of dielectric due to excess manganese dioxide, to moisture paths, or to cathode conductors (carbon, silver). This "normal" leakage current in solid electrolyte capacitors cannot be reduced by "healing", because under normal conditions solid electrolytes cannot provide oxygen for forming processes. This statement should not be confused with the self-healing process during field crystallization, see below, Reliability (Failure rate).

The specification of the leakage current in data sheets is often given as multiplication of the rated capacitance value *CR* with the value of the rated voltage *UR* together with an addendum figure, measured after a measuring time of two or five minutes, for example:

$I_{\mathrm {Leak} }=0{,}01\,\mathrm {{A} \over {V\cdot F}} \cdot U_{\mathrm {R} }\cdot C_{\mathrm {R} }+3\,\mathrm {\mu A}$

The leakage current value depends on the voltage applied, on the temperature of the capacitor, and on measuring time. Leakage current in solid MnO2 tantalum electrolytic capacitors generally drops very much faster than for non-solid electrolytic capacitors but remain at the level reached.

### Dielectric absorption (soakage)

Dielectric absorption occurs when a capacitor that has remained charged for a long time discharges only incompletely when briefly discharged. Although an ideal capacitor would reach zero volts after discharge, real capacitors develop a small voltage from time-delayed dipole discharging, a phenomenon that is also called dielectric relaxation, "soakage" or "battery action".

| Type of capacitor | Dielectric absorption |
|---|---|
| Tantalum electrolytic capacitors with solid electrolyte | 2 to 3%, 10% |
| Aluminium electrolytic capacitor with non solid electrolyte | 10 to 15% |

Dielectric absorption may be a problem in circuits where very small currents are used in the function of an electronic circuit, such as long-time-constant integrators or sample-and-hold circuits. In most electrolytic capacitor applications supporting power supply lines, dielectric absorption is not a problem.

But especially for electrolytic capacitors with high rated voltage, the voltage at the terminals generated by the dielectric absorption can pose a safety risk to personnel or circuits. In order to prevent shocks, most very large capacitors are shipped with shorting wires that need to be removed before the capacitors are used.


## Operational characteristics

### Reliability (failure rate)

The reliability of a component is a property that indicates how reliably this component performs its function in a time interval. It is subject to a stochastic process and can be described qualitatively and quantitatively; it is not directly measurable. The reliability of electrolytic capacitors is empirically determined by identifying the failure rate in production accompanying endurance tests, see Reliability engineering.

Reliability normally is shown as a bathtub curve and is divided into three areas: early failures or infant mortality failures, constant random failures and wear out failures. Failures totalized in a failure rate are short circuit, open circuit, and degradation failures (exceeding electrical parameters).

The reliability prediction is generally expressed in a failure rate λ, abbreviated **FIT** (**F**ailures **I**n **T**ime). This is the number of failures that can be expected in one billion (109) component-hours of operation (e.g., 1000 components for 1 million hours, or 1  million components for 1000 hours which is 1 ppm/1000 hours) at fixed working conditions during the period of constant random failures. This failure rate model implicitly assumes the idea of "random failure". Individual components fail at random times but at a predictable rate.

Billions of tested capacitor unit-hours would be needed to establish failure rates in the very low level range which are required today to ensure the production of large quantities of components without failures. This requires about a million units over a long time period, which means a large staff and considerable financing. The tested failure rates are often complemented with figures resulting from feedback from the field from major customers (field failure rate), which mostly results in a lower failure rate than tested.

The reciprocal value of FIT is Mean Time Between Failures (MTBF).

The standard operating conditions for FIT testing are 40 °C and 0.5 UR. For other conditions of applied voltage, current load, temperature, capacitance value, circuit resistance (for tantalum capacitors), mechanical influences and humidity, the FIT figure can be converted with acceleration factors standardized for industrial or military applications. The higher the temperature and applied voltage, the higher the failure rate, for example.

The most often cited source for failure rate conversion is MIL-HDBK-217F, the “bible” of failure rate calculations for electronic components. SQC Online, the online statistical calculator for acceptance sampling and quality control, provides an online tool for short examination to calculate given failure rate values for given application conditions.

Some manufacturers may have their own FIT calculation tables for tantalum capacitors. or for aluminium capacitors

For tantalum capacitors the failure rate is often specified at 85 °C and rated voltage UR as reference conditions and expressed as percent failed components per thousand hours (n %/1000 h). That is, “n” number of failed components per 105 hours, or in FIT the ten-thousand-fold value per 109 hours.

Tantalum capacitors are now very reliable components. Continuous improvement in tantalum powder and capacitor technologies have resulted in a significant reduction in the amount of impurities which formerly caused most field crystallization failures. Commercially available industrially produced tantalum capacitors now have reached as standard products the high MIL standard "C" level, which is 0.01%/1000 h at 85 °C and UR or 1 failure per 107 hours at 85 °C and UR. Converted to FIT with the acceleration factors coming from MIL HDKB 217F at 40 °C and 0.5 , UR is the failure rate. For a 100 μF/25 V tantalum chip capacitor used with a series resistance of 0.1 Ω the failure rate is 0.02 FIT.

Aluminium electrolytic capacitors do not use a specification in "% per 1000 h at 85 °C and UR". They use the FIT specification with 40 °C and 0.5 UR as reference conditions. aluminium electrolytic capacitors are very reliable components. Published figures show for low voltage types (6.3…160 V) FIT rates in the range of 1 to 20 FIT and for high voltage types (>160 …550 V) FIT rates in the range of 20 to 200 FIT. Field failure rates for aluminium e-caps are in the range of 0.5 to 20 FIT.

The published figures show that both tantalum and aluminium capacitor types are reliable components, comparable with other electronic components and achieving safe operation for decades under normal conditions. But a great difference exists in the case of wear-out failures. Electrolytic capacitors with non-solid electrolyte, have a limited period of constant random failures up to the point when wear-out failures begin. The constant random failure rate period corresponds to the lifetime or service life of “wet” aluminium electrolytic capacitors.

### Lifetime

The lifetime, service life, load life or useful life of electrolytic capacitors is a special characteristic of non-solid aluminium electrolytic capacitors, whose liquid electrolyte can evaporate over time. Lowering the electrolyte level affects the electrical parameters of the capacitors. The capacitance decreases and the impedance and ESR increase with decreasing amounts of electrolyte. This very slow electrolyte drying-out depends on the temperature, the applied ripple current load, and the applied voltage. The lower these parameters compared to their maximum values, the longer the capacitor's “life”. The “end of life” point is defined by the appearance of wear-out failures or degradation failures when either capacitance, impedance, ESR or leakage current exceed their specified change limits.

The lifetime is a specification of a collection of tested capacitors and delivers an expectation of the behavior of similar types. This lifetime definition corresponds to the time of the constant random failure rate in the bathtub curve.

But even after exceeding the specified limits and the capacitors having reached their “end of life”, the electronic circuit is not in immediate danger; only the functionality of the capacitors is reduced. With today's high levels of purity in the manufacture of electrolytic capacitors it is not to be expected that short circuits occur after the end-of-life-point with progressive evaporation combined with parameter degradation.

The lifetime of non-solid aluminium electrolytic capacitors is specified in terms of “hours per temperature", like "2,000h/105 °C". With this specification the lifetime at operational conditions can be estimated by special formulas or graphs specified in the data sheets of serious manufacturers. They use different ways for specification, some give special formulas, others specify their e-caps lifetime calculation with graphs that consider the influence of applied voltage. The basic principle for calculating the time under operational conditions is the so-called “10-degree-rule”.

This rule is also known as the Arrhenius rule. It characterizes the change of thermic reaction speed. For every 10 °C lower temperature the evaporation is reduced by half. That means for every 10 °C reduction in temperature, the lifetime of capacitors doubles. If a lifetime specification of an electrolytic capacitor is, for example, 2000  h/105 °C, the capacitor's lifetime at 45 °C can be ”calculated” as 128,000 hours—that is roughly 15 years—by using the 10-degrees-rule.

However, solid polymer electrolytic capacitors, and aluminium, tantalum, and niobium electrolytic capacitors also have a lifetime specification. The polymer electrolyte exhibits a small deterioration of conductivity caused by thermal degradation of the conductive polymer. The electrical conductivity decreases as a function of time, in agreement with a granular metal type structure, in which aging is due to the shrinking of the conductive polymer grains. The lifetime of polymer electrolytic capacitors is specified in terms similar to non-solid electrolytic capacitors but its lifetime calculation follows other rules, leading to much longer operational lifetimes.

Tantalum electrolytic capacitors with solid manganese dioxide electrolyte do not have wear-out failures, so they do not have a lifetime specification in the sense of non-solid aluminium electrolytic capacitors. Also, tantalum capacitors with non-solid electrolyte, the "wet tantalums", do not have a lifetime specification because they are hermetically sealed.

### Failure modes, self-healing mechanism and application rules

The many different types of electrolytic capacitors exhibit different electrical long-term behavior, intrinsic failure modes, and self-healing mechanisms. Application rules for types with an intrinsic failure mode are specified to ensure capacitors with high reliability and long life.

| Type of electrolytic capacitors | Long-term electrical behavior | Failure modes | Self-healing mechanism | Application rules |
|---|---|---|---|---|
| aluminium electrolytic capacitors, non-solid electrolyte | Drying out over time, capacitance decreases, ESR increases | no unique determinable | New generated oxide (forming) by applying a voltage | Lifetime calculation |
| aluminium electrolytic capacitors, solid polymer electrolyte | Deterioration of conductivity, ESR increases | no unique determinable | Insulating of faults in the dielectric by oxidation or evaporation of the polymer electrolyte | Lifetime calculation |
| Tantalum electrolytic capacitors, solid MnO2 electrolyte | Stable | Field crystallization | Thermally induced insulating of faults in the dielectric by oxidization of the electrolyte MnO2 into insulating MnO2O3 if current availability is limited | Voltage derating 50% Series resistance 3 Ω/V |
| Tantalum electrolytic capacitors, solid polymer electrolyte | Deterioration of conductivity, ESR increases | Field crystallization | Insulating of faults in the dielectric by oxidation or evaporation of the polymer electrolyte | Voltage derating 20 % |
| Niobium electrolytic capacitors, solid MnO2 electrolyte | Stable | no unique determinable | Thermally induced insulation of faults in the dielectric by oxidation of Nb2O5 into insulating NbO2 | Niobium anode: voltage derating 50% Niobium oxide anode: voltage derating 20 % |
| Niobium electrolytic capacitors, solid polymer electrolyte | Deterioration of conductivity, ESR increases | no unique determinable | Insulating of faults in the dielectric by oxidation or evaporation of the polymer electrolyte | Niobium anode: voltage derating 50% Niobium oxide anode: voltage derating 20 % |
| Hybrid aluminium electrolytic capacitors, solid polymer + non-solid electrolyte | Deterioration of conductivity, drying out over time, capacitance decreases, ESR increases | no unique determinable | New generated oxide (forming) by applying a voltage | Lifetime calculation |

### Performance after storage

All electrolytic capacitors are "aged" during manufacturing by applying the rated voltage at high temperature for a sufficient time to repair all cracks and weaknesses that may have occurred during production. However, a particular problem with non-solid aluminium models may occur after storage or unpowered periods. Chemical processes (corrosion) can weaken the oxide layer, which may lead to a higher leakage current. Most modern electrolytic systems are chemically inert and do not exhibit corrosion problems, even after storage times of two years or longer. Non-solid electrolytic capacitors using organic solvents like GBL as electrolyte do not have problems with high leakage current after prolonged storage. They can be stored for up to 10 years without problems

Storage times can be tested using accelerated shelf-life testing, which requires storage without applied voltage at the upper category temperature for a certain period, usually 1000 hours. This shelf life test is a good indicator for chemical stability and of the oxide layer, because all chemical reactions are accelerated by higher temperatures. Nearly all commercial series of non-solid electrolytic capacitors fulfill the 1000 hour shelf life test. However, many series are specified only for two years of storage. This also ensures solderability of the terminals.

For antique radio equipment or for electrolytic capacitors built in the 1970s or earlier, "preconditioning" may be appropriate. This is performed by applying the rated voltage to the capacitor via a series resistor of approximately 1 kΩ for one hour, allowing the oxide layer to repair itself through self-healing. Capacitors that fail leakage current requirements after preconditioning may have experienced mechanical damage.

Electrolytic capacitors with solid electrolytes do not have preconditioning requirements.


## Causes of explosion

Electrolytic capacitors are chemical in nature. Some undesired reactions produce gases, which causes a buildup of internal pressure. Even though most capacitors have a vent to gradually release the pressure, the buildup can still be so great that the electrolyte itself is forced out: an "explosion". If the vent is not functional, it is also possible for the sleeve to be destroyed in a real explosion. Explosions can be due to:

- **Overvoltage and Reverse Polarity:** Applying a voltage higher than the rated value or reversing the polarity can cause excessive current to flow, leading to rapid heating. This heating can decompose the electrolyte, generating gas and increasing internal pressure until the capacitor explodes.
- **Electrolyte Decomposition:** Electrolytes in capacitors can decompose into gasses such as hydrogen when exposed to high temperatures or electrical stresses. The resulting gas increases internal pressure, leading to the rupture of the capacitor casing.
- **Design Flaws and Manufacturing Defects:** Poor manufacturing processes can lead to weak points in the capacitor’s structure. During the capacitor plague, a widespread issue arose from the use of an incomplete electrolyte formula, which lacked necessary inhibitors to prevent gas formation and pressure buildup.
- **Thermal Runaway:** High ripple currents can cause the capacitor to overheat. As the temperature rises, the electrolyte evaporates faster, creating more gas and increasing pressure, which can result in an explosion.
- **Aging and Deterioration:** Over time, the materials within electrolytic capacitors degrade, reducing their ability to handle electrical stress and heat. This aging process can lead to internal failures and explosions.

Explosion accompanies a loss of electrolyte fluid and results in a nonfunctional capacitor. It is also possible for the electrolyte to flow onto neighboring components, causing short circuits and further damage.


## Additional information

### Capacitor symbols

**Electrolytic capacitor symbols**

- (Electrolytic capacitor) Electrolytic capacitor
- (Electrolytic capacitor) Electrolytic capacitor
- (Electrolytic capacitor) Electrolytic capacitor
- (Bipolar electrolytic capacitor) Bipolar electrolytic capacitor

### Parallel connection

If an individual capacitor within a bank of parallel capacitors develops a short, the entire energy of the capacitor bank discharges through that short. Thus, large capacitors, particularly high voltage types, should be individually protected against sudden discharge.

### Series connection

In applications where high withstanding voltages are needed, electrolytic capacitors can be connected in series. Because of individual variation in insulation resistance, and thus the leakage current when voltage is applied, the voltage is not distributed evenly across each series capacitor. This can result in the voltage rating of an individual capacitor being exceeded. A passive or active balancer circuit must be provided in order to equalize the voltage across each individual capacitor.

### Polarity marking

- Polarity markings for aluminium electrolytic capacitors
- (Electrolytic capacitors with non-solid electrolyte have a polarity marking on the cathode (minus) side, with a shorter lead) Electrolytic capacitors with **non-solid** electrolyte have a polarity marking on the cathode (**minus**) side, with a shorter lead
- (Electrolytic capacitors with solid electrolyte have a polarity marking on the anode (plus) side, except for cylindrical leaded (single-ended) and SMD polymer capacitors[116]) Electrolytic capacitors with **solid** electrolyte have a polarity marking on the anode (**plus**) side, except for cylindrical leaded (single-ended) and SMD polymer capacitors

**Polarity marking for polymer electrolytic capacitors**

|   |   |
|---|---|
| Rectangular polymer capacitors, tantalum as well as aluminium, have a polarity marking on the anode (**plus**) side | Cylindrical polymer capacitors have a polarity marking on the cathode (**minus**) side |

### Imprinted markings

Electrolytic capacitors, like most other electronic components, are marked, space permitting, with

- manufacturer's name or trademark;
- manufacturer's type designation;
- polarity of the terminations (for polarized capacitors)
- rated capacitance;
- tolerance on rated capacitance
- rated voltage and nature of supply (AC or DC)
- climatic category or rated temperature;
- year and month (or week) of manufacture;
- certification marks of safety standards (for safety EMI/RFI suppression capacitors)

Smaller capacitors use a shorthand notation. The most commonly used format is: XYZ J/K/M “V”, where XYZ represents the capacitance (calculated as XY × 10Z pF), the letters K or M indicate the tolerance (±10% and ±20% respectively) and “V” represents the working voltage.

Examples:

- 105K 330V implies a capacitance of 10 × 105 pF = 1 μF (K = ±10%) with a rated voltage of 330 V.
- 476M 100V implies a capacitance of 47 × 106 pF = 47 μF (M = ±20%) with a rated voltage of 100 V.

Capacitance, tolerance and date of manufacture can be indicated with a short code specified in IEC/EN 60062. Examples of short-marking of the rated capacitance (microfarads): μ47 = 0,47 μF, 4μ7 = 4,7 μF, 47μ = 47 μF

The date of manufacture is often printed according to international standards.

- Version 1: coding with year/week numeral code, "1208" is "2012, week number 8".
- Version 2: coding with year code/month code. The year codes are: "R" = 2003, "S"= 2004, "T" = 2005, "U" = 2006, "V" = 2007, "W" = 2008, "X" = 2009, "A" = 2010, "B" = 2011, "C" = 2012, "D" = 2013, “E” = 2014 etc. Month codes are: "1" to "9" = Jan. to Sept., "O" = October, "N" = November, "D" = December. "X5" is then "2009, May"

For very small capacitors no marking is possible. Here only the traceability of the manufacturers can ensure the identification of a type.

### Standardization

The standardization for all electrical, electronic components and related technologies follows the rules given by the International Electrotechnical Commission (IEC), a non-profit, non-governmental international standards organization.

The definition of the characteristics and the procedure of the test methods for capacitors for use in electronic equipment are set out in the **Generic specification**:

- IEC/EN 60384-1 - Fixed capacitors for use in electronic equipment

The tests and requirements to be met by aluminium and tantalum electrolytic capacitors for use in electronic equipment for approval as standardized types are set out in the following **sectional specifications**:

- IEC/EN 60384-3—*Surface mount fixed tantalum electrolytic capacitors with manganese dioxide solid electrolyte*
- IEC/EN 60384-4—*Aluminium electrolytic capacitors with solid (MnO2) and non-solid electrolyte*
- IEC/EN 60384-15—*Fixed tantalum capacitors with non-solid and solid electrolyte*
- IEC/EN 60384-18—*Fixed aluminium electrolytic surface mount capacitors with solid (MnO2) and non-solid electrolyte*
- IEC/EN 60384-24—*Surface mount fixed tantalum electrolytic capacitors with conductive polymer solid electrolyte*
- IEC/EN 60384-25—*Surface mount fixed aluminium electrolytic capacitors with conductive polymer solid electrolyte*
- IEC/EN 60384-26—*Fixed aluminium electrolytic capacitors with conductive polymer solid electrolyte*

### Market

The market for electrolytic capacitors in 2008 was roughly 30% of the total market in value

- aluminium electrolytic capacitors—US$3.9 billion (22%);
- Tantalum electrolytic capacitors—US$2.2 billion (12%);

In number of pieces, these capacitors cover about 10% of the total capacitor market, or about 100 to 120 billion pieces.

### Manufacturers and products

Worldwide operating manufacturers and their electrolytic capacitor product program

Manufacturer

aluminium

electrolytic capacitors

Tantalum

electrolytic capacitors

Niobium

electrolytic

capacitors

SMD

Radial

Power

SI, ST

Polymer

SMD

Radial

Polymer

Hybrid

SMD

MnO

2

SMD

Polymer

Wet

electrolyte

SMD

MnO

2

Polymer

AVX

-

-

-

-

X

X

X

X

CapXon

X

X

X

X

-

-

-

-

CDE Cornell Dubilier

X

X

X

X

X

X

-

-

Capacitor Industries

-

X

-

-

-

-

-

-

Chinsan, (Elite)

X

X

X

-

-

-

-

-

Daewoo, (Partsnic)

Archived

2018-06-12 at the

Wayback Machine

X

X

-

-

-

-

-

-

Elna

Archived

2015-03-14 at the

Wayback Machine

X

X

X

-

-

-

-

-

Exxelia group

-

X

-

-

X

X

-

-

Frolyt

X

X

-

-

-

-

-

-

Hitachi

-

X

-

-

-

-

-

-

Hitano

X

X

X

-

X

-

-

-

Itelcond

-

X

-

-

-

-

-

-

Jackcon

X

X

-

-

-

-

-

-

Jianghai

X

X

X

X

-

-

-

-

Kaimei Electronic Corp, (Jamicon)

X

X

-

-

-

-

-

-

KEMET

Archived

2013-12-12 at the

Wayback Machine

X

X

X

-

X

X

X

-

Lelon

X

X

X

-

-

-

-

-

MAN YUE, (Samxon)

X

X

-

-

-

-

-

-

NEC Tokin

-

-

-

-

X

-

X

-

Nippon Chemi-Con

X

X

X

X

-

-

-

-

NIC

Archived

2016-02-07 at the

Wayback Machine

X

X

X

X

X

-

X

-

Nichicon

Archived

2018-06-12 at the

Wayback Machine

X

X

X

-

-

-

-

-

YMIN

X

-

X

X

X

X

-

-

Panasonic, Matsushita

X

X

X

X

-

-

X

-

Richey

X

X

-

-

-

-

-

-

ROHM

-

-

-

-

X

-

X

-

Rubycon

X

X

X

-

-

-

-

-

Samwha

X

X

X

-

-

-

-

-

SUN Electronic Industry

X

-

-

X

-

-

-

-

TDK EPCOS

X

X

-

-

-

-

-

-

Teapo (Luxon)

Archived

2016-03-04 at the

Wayback Machine

X

X

X

-

-

-

-

-

Vishay

X

X

X

-

X

X

X

X

Yageo

X

X

X

-

-

-

-

-

Date of the table: March 2015
