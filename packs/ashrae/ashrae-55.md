---
title: "ASHRAE 55"
source: https://en.wikipedia.org/wiki/ASHRAE_55
domain: ashrae
license: CC-BY-SA-4.0
tags: ashrae
fetched: 2026-07-03
---

# ASHRAE 55

***ANSI/ASHRAE Standard 55: Thermal Environmental Conditions for Human Occupancy*** is an American National Standard published by ASHRAE that establishes the ranges of indoor environmental conditions to achieve acceptable thermal comfort for occupants of buildings. It was first published in 1966, and since 2004 has been updated every three to six years. The most recent version of the standard was published in 2023.

## Organization of standard

The body of the standard consists of a foreword (describing changes made in the current version), eight sections and several normative appendices:

1. Purpose
2. Scope
3. Definitions
4. General requirements
5. Conditions that provide thermal comfort
6. Design compliance
7. Evaluation of comfort in existing buildings
8. References

Normative Appendix A: Methods for determining operative temperature

Normative Appendix B: Computer program for calculation of

PMV/PPD

Normative Appendix C: Procedure for Calculating Comfort Impact of Solar Gain on Occupants

Normative Appendix D: Procedure for Evaluating Cooling Effect of Elevated Air Speed Using

SET

Informative Appendix E: Conditions That Provide Thermal Comfort

Informative Appendix F: Use of Metabolic Rate Data

Informative Appendix G: Clothing Insulation

Informative Appendix H: Comfort Zone Methods

Informative Appendix I: Local Discomfort and Variations with Time

Informative Appendix J: Occupant-Controlled Naturally Conditioned Spaces

Informative Appendix K: Sample Design Compliance Documentation

Informative Appendix L: Measurements, Surveys, and Evaluations of Comfort in Existing Spaces: Parts 1 and 2

Informative Appendix M: Bibliography and Informative References

Informative Appendix N: Addenda Description

The informative appendices are not part of the standard, but provide additional information about terms and methods described within the standard, as well as a bibliography, and a description of the addenda incorporated from the previous version in the current version.

## Purpose

As described within the standard: "The purpose of the standard is to specify the combinations of indoor thermal environmental factors and personal factors that will produce thermal environmental conditions acceptable to a majority of the occupants within the space".

## Scope

The standard addresses the four primary environmental factors (temperature, thermal radiation, humidity, and air speed) and two personal factors (activity and clothing) that affect thermal comfort. It is applicable for:

- healthy adults at atmospheric pressures in altitudes up to (or equivalent to) 3,000 m (9,800 ft),
- people whose clothing insulation is between 0.0 and 1.5 clo, who are not wearing highly impermeable clothing,
- metabolic rates between 1.0 and 2.0 met,
- people who are neither sleeping nor reclining,
- for indoor spaces designed for occupancy of at least 15 minutes.

## Definitions

### Adaptive model

Adaptive model is a model that relates indoor design temperatures or acceptable temperature ranges to outdoor meteorological or climatological parameters.

### Thermal comfort

Thermal comfort is the condition of mind that expresses satisfaction with the thermal environment and is assessed by subjective evaluation.

### Occupant-controlled naturally conditioned spaces

A occupant-controlled naturally conditioned space is where the thermal conditions of the space are primarily regulated by occupant-controlled openings.

### Predicted mean vote (PMV)

Predicted mean vote is an index that predicts the mean value of the thermal sensation votes (self-reported perceptions) of a large group of persons on a sensation scale expressed from -3 to +3 corresponding to the categories "cold," "cool," "slightly cool," "neutral," "slight warm," "warm," and "hot." The value of PMV can be calculated either using the code provided in Appendix B of the standard or can be freely calculated with either the CBE Thermal Comfort Tool for ASHRAE 55, with the Python package pythermalcomfort and with the R package comf.

### Comfort zone

Comfort zone refers to the combinations of air temperature, mean radiant temperature (tr), and humidity that are predicted to be an acceptable thermal environment at particular values of air speed, metabolic rate, and clothing insulation (Icl)

### Clothing insulation (Icl)

Clothing insulation is the resistance to sensible heat transfer provided by a clothing ensemble (expressed in units of clo, which is a unit to quantify the insulation provided by garments and clothing ensembles. 1 *clo* = 0.155 m2 °C/W (0.88 ft2·h·°F/Btu))

### Metabolic rate (met)

Metabolic rate is the rate of transformation of chemical energy into heat and mechanical work by metabolic activities of an individual, per unit of skin surface area (expressed in units of met) equal to 58.2 W/m2 (18.4 Btu/h·ft2), which is the energy produced per unit skin surface area of an average person seated at rest.

### Exceedance hours

Exceedance hour is the number of occupied hours within a defined time period in which the environmental conditions in an occupied space are outside the comfort zone.

## Methods to evaluate thermal comfort

### Graphic comfort zone method

The graphic method utilizes an overlay on a psychrometric chart to indicate the operative temperatures and humidity at which thermal comfort is achieved in the winter (1.0 *clo*) and summer (0.5 *clo*). It is based on the Predicted Mean Vote (PMV) model. The graphic comfort zone model is limited in applicability to conditions when the metabolic rate of occupants is 1.0-1.3 met and the humidity ratio is below 0.012 kg H2O/kg dry air (0.012 lb H2O/lb dry air). If these requirements are met and the environmental conditions inside the building fall within the indicated ranges, then compliance is achieved.

### Analytical comfort zone method

For humidity ratios above 0.012 kg H2O/kg dry air (0.012 lb H2O/lb dry air), or for metabolic rates up to 2.0 met, the analytical model must be used to determine thermal comfort sensation. Also based on the PMV model, this method uses tools such as the ASHRAE Thermal Comfort Tool or the online CBE Thermal Comfort Tool for ASHRAE 55 to evaluate thermal comfort. Users provide operative temperature (or air temperature and mean radiant temperature), air speed, humidity, metabolic rate, and clothing insulation value, and the tool evaluates predicted thermal sensation on a scale from -3 (cold) to +3 (hot). Compliance is achieved if the conditions provide thermal neutrality, measured as falling between -0.5 and +0.5 on the PMV scale.

### Elevated air speed

The section sets provisions for increasing the upper air temperature limit at elevated air speeds above 0.20 m/s (39 ft/min). The methodology is based on the SET (Standard Effective Temperature) model, which provides a way to assign an effective temperature (at a standard metabolic rate, and clothing insulation values) to compare thermal sensations experienced at a range of thermal conditions. The upper limit of air speed is based on whether occupants have local control or not. To evaluate compliance, the ASHRAE Thermal Comfort Tool may be used, or a computer model validated against the code provided in Informative Appendix D of the standard.

### Local thermal discomfort

Radiant temperature asymmetry between ceiling and floor, and air and walls must be limited to reduce discomfort. To reduce draft risk at temperatures below 22.5 °C (72.5 °F), air speed due to the HVAC system must be 0.15 m/s (30 ft/min) or below. The vertical air temperature difference between ankle and head is limited to 3 °C (5.4 °F) for seated occupants and 4 °C (7.2 °F) for standing occupants. If occupants' feet will be in contact with the floor, the temperature must be 19–29 °C (66–84 °F).

### Temperature variations with time

When occupants do not have control over the cyclical variation or drifts in indoor environmental conditions, the conditions within this section must be met. Operative temperatures may not fluctuate more than 1.1 °C (2.0 °F) within 15 minutes, nor change more than 2.2 °C (4.0 °F) within 1 hour.

### Acceptable thermal conditions in occupant-controlled naturally conditioned spaces

This method, also known as the adaptive comfort model, is applicable in buildings without mechanical cooling (and no operating heating system) where occupants' met rates are 1.0-1.3 met and their clothing levels are 0.5-1.0 *clo*. For this model the standard provides a graph of acceptable indoor temperature limits at prevailing mean outdoor temperatures (a mean of the daily mean outdoor temperatures of the previous 7–30 days). An accompanying table lists provisions for higher operative temperatures at air speeds above 0.3 m/s (59 ft/min) and up to 1.2 m/s (240 ft/min). The graph is valid for prevailing mean temperatures between 10 and 33.5 °C (50.0 and 92.3 °F). It provides 80% and 90% acceptability ranges, indicating the percentage of occupants expected to be comfortable at the indicated indoor and prevailing mean outdoor temperatures.

## Demonstrating design compliance

This section of the standard is applicable for the design of buildings. All of the building systems must be designed to maintain the occupied spaces at the indoor conditions specified by one of the described evaluation methods at design conditions. The systems must be able to maintain these conditions within the expected range of indoor and outdoor operating conditions.

For demonstrating design compliance, the following are the core requirements that must be documented:

- Each unique space. Spaces excluded from compliance documentation must be clearly identified with a rationale.
- The method of design compliance: Determining Satisfactory Thermal Environment in Occupied Spaces (Section 5.3 of ANSI/ASHRAE Standard 55-2023) or Determining Acceptable Thermal Conditions in Occupant-Controlled Naturally Conditioned Spaces (Section 5.4 of ANSI/ASHRAE Standard 55-2023).
- Each representative occupant and their location within the space, along with clothing insulation (*Icl*) and metabolic rate (*met*) values for each design comfort condition: When selecting a single value, the rationale must be explained. If occupants are considered nonrepresentative, this must be documented with an explanation.
- Description of the design comfort conditions: The conditions should combine indoor and outdoor factors at which occupant thermal comfort shall be evaluated and cover the most challenging scenarios for occupant comfort. Every unique combination of space and representative occupant must be evaluated under at least two conditions: cooling and heating. The design comfort conditions should be carefully considered as they may not align with the room peak heating and cooling load conditions.
- The operative temperature *to* and its expected range used in the comfort calculation.
- Solar radiation impact: If direct-beam solar radiation affects a representative occupant, the documentation must include the compliance method used, along with all applicable calculation inputs, methods, and results.
- Thermal environmental control classification level: The level must be documented for each space, including the control measures, the means of control, and the degree of change of the environmental factor.
- Compliance status: The compliance or non-compliance for each combination of space, representative occupant, and design comfort condition must be clearly stated.

## Evaluation of comfort in existing buildings

Although the evaluation of comfort in existing buildings is not mandatory in ASHRAE 55, it can be used as a guideline when required by other standards. Occupant surveys and environmental measurements are primarily used for evaluation. When the building automation system is added, the relevant characteristics must be described.

### Measurement methods

Indoor thermal comfort can be determined from the responses of the occupant survey. Surveys must cover either the entire occupancy or a sample of it. When soliciting feedback from over 45 occupants, a minimum 35% response rate is required. For sample sizes between 20 and 45, at least 15 responses are necessary, while surveys directed at fewer than 20 occupants need an 80% response rate to ensure reliability.

Generally, the scale in thermal satisfaction surveys must end with options "very dissatisfied" and "very satisfied." An open-ended response to document reasons for dissatisfaction should also be provided.

The Point-in-Time surveys, which shall be solicited and conducted during active occupancy hours, require gathering responses on a continuous or seven-point Likert scale from "very dissatisfied" to "very satisfied." Thermal sensation questions should employ terms: "cold," "cool," "slightly cool," "neutral," "slightly warm," "warm," and "hot". "Cooler", "without change" and "warmer" are used for thermal preference questions.

#### Physical measurements

For mechanically conditioned spaces, the PMV-based comfort zone has to be determined, which includes measuring and recording the metabolic activity and clothing insulation. The comfort zone boundaries must be adjusted to the air movements, and the zone conditions should be adjusted to avoid local thermal discomfort. For occupant-controlled naturally conditioned space, the adaptive model shall be used to determine the thermal comfort boundaries. For such spaces, the indoor and outdoor air temperature and mean radiant temperature and the air speed need to be measured.

*ANSI/ASHRAE Standard 55* provides guideline on the position, time, and equipment accuracy of the physical measurement. The measurement locations should be where the occupants are expected to spend time in. If there are multiple such locations, the measurement can be performed at a representative location. In cases that the optimal representative location cannot be found, the standard suggests specific locations in the space.

Air temperature and speed must be measured at heights of 0.1 m, 0.6 m, and 1.1 m for seated occupants; 0.1 m, 1.1 m, and 1.7 m for standing occupants; and at the mean height of the body for horizontal occupants. Operative temperature or PMV should be calculated at 0.6 m for seated occupants, 1.1 m for standing occupants, and the mean height of the body for horizontal occupants. Local discomfort caused by floor temperature and radiant temperature asymmetry should be measured at the floor surface and at the occupants' locations, respectively.

The standard suggests that the time of measurements should last two or more hours long, and it should also be a representative time of the year for this specific building. Measuring time step should be no more than five minutes for air temperature, mean radiant temperature, and humidity, and no more than three minutes for the air speed.

In order to achieve acceptable results, the standard also suggests the minimum equipment accuracy based the current industry standard.

#### Measurements from Building Automation System (BAS)

When measuring environmental data from the Building Automation System, sensor placement must align with the recommended criteria for physical measurements. Temperature sensors should achieve an accuracy of ±0.5 °C (±1 °F) and humidity sensors ±5% relative humidity. The trending capabilities require data to be recorded at intervals of no more than 15 minutes, spanning a minimum of 30 days. Concurrent data, such as equipment status and supply/return air temperatures, should also be collected for a comprehensive analysis.

### Evaluation methods

To evaluate the probability of satisfaction from satisfaction surveys, the standard suggests dividing the number of the votes falling between "just satisfied" and "very satisfied" by the total number of votes in that questions. The answers of open-ended questions from "very dissatisfied" occupants should be documented for later analysis. For point-in-time surveys, the comfort evaluation shall be performed by dividing the number of votes between -1 and +3 by the total number of votes. One has to keep in mind that the results from point-in-time surveys are only effective during the time when the surveys were solicited.

#### Physical measurements

The measured results should be evaluated against the adjusted comfort zone for the specific building. There are two cases when evaluating thermal comfort: at a specific time or over a period of time. For a mechanically conditioned space at an instance in time, the PMV and SET model shall be used to establish the comfort zone, and the local thermal discomfort shall be evaluated against the limit posed this standard as well. For occupant-controlled naturally conditioned spaces, the measured results shall be check with the comfort zone established by adaptive model.

To evaluate the thermal comfort over a period of time in a mechanically conditioned space, the exceedance hours are the sum of all the hours when the absolute value of PMV is greater than 0.5. For an occupant-controlled naturally conditioned space, the exceedance hours are the sum of hours when the operative temperature falls outside of the lower and upper boundaries of the comfort zone.

## Appendix F: Use the metabolic rate data

Metabolic rate is the rate of transformation of chemical energy into heat and mechanical work by metabolic activities of an individual. It is defined as per unit of skin surface area which equals to 58.2 W/m2 (18.4 Btu/h·ft2). This is the energy produced from a unit skin surface area of an average person seated at rest.

*ANSI/ASHRAE Standard 55* provides a table of metabolic rate of different continuous activities. These values are valid for an average adult with surface skin area of 1.8 m2 (19.6 ft2). The standard reminds the users that they should use their own judgment to match the activities being considered to the comparable activities in the table. Except sedentary activities, metabolic rate for all other activities is likely to have range of variation. This variation is depending on the individual performing the task and his/her environment.

When the duration of an activity is equal or less than one hour, one can use a time-weighted metabolic rate. As metabolic rates increase over 1.0 met, the evaporation of the sweat becomes an increasingly important factor, and the PMV method does not fully account for this factor.

## Appendix G: Clothing insulation

Clothing insulation refers to the heat transfer of the entire body, which includes the uncovered parts, such as hands and heads. There is a variety of means to determine the insulation provided by clothing. Accurate data from the measurement using thermal manikins is acceptable. When such measurement is not feasible, this standard provides four methods to determine the clothing insulation. It is also specified that the methods provided by this standard are no longer valid when the clothing insulation exceed 1.5 *clo*. And it is also not valid when occupants wear clothing that is highly impermeable to moisture transport. The first method is the least accurate, according to *ANSI/ASHRAE Standard 55*, and the accuracy increases in order of the methods.

First, one can estimate the clothing insulation from the table provided in section five. If the clothing ensemble in question reasonably matches the clothing ensemble in the table, the indicated value can be used. The second method is to add or subtract individual garment clo value to achieve the clothing ensemble in question. Section five of the *ANSI/ASHRAE Standard 55* provides a table with clothing insulation of a variety of individual garments. This table can be used together with the previous one, so that one can add or subtract the clothing ensemble from the *clo* value of each garment. The third method is to add all the *clo* value of each garment to match the clothing ensemble in question.

The fourth method described in *ANSI/ASHRAE Standard 55* can be used to determine the clothing insulation in mechanically conditioned spaces. This method is based on the concept that when occupants choose their clothing according to their environment, the outdoor environment is more influential than the indoor one. There is a figure in the section five of the standard which predicts the representative clothing insulation of the occupants as a function of the average outdoor air temperature at 06:00 am. The function line has four segments: the average outdoor air temperature is below −5.0 °C (23.0 °F), between −5.0 °C (23.0 °F) and 5.0 °C (41.0 °F), between 5.0 °C (41.0 °F) and 26.0 °C (78.8 °F), and above 26.0 °C (78.8 °F).

There is a function to determine the representative clothing insulation at each segment. One can also take into account the posture of the occupants. So far, all the clothing insulation value can be used when the occupant is standing. When occupant is sitting, one has to realize the insulation effect of the chair, and the decrease of insulation due to compression of the air in the clothing.

If the occupant is moving, it also affects the insulation value of clothing. In general, body motion decreases the clothing insulation by pumping air through clothing. *ANSI/ASHRAE Standard 55* recognizes that this effect varies largely depending on the nature of the movements and the nature clothing, such as how tight the clothing is. Thus, it only provides an approximation of the clothing insulation value of a moving person. This approximation is an equation that relates the clothing insulation with the metabolic rate. And this equation is only valid when the metabolic rate is between 1.2 and 2.0.

*ANSI/ASHRAE Standard 55* also states that the thermal environment conditions desired for sleeping and resting vary largely among individuals and cannot be determined using the methods provided in this standard. Considering that a sleeping person or one in reclining posture will be provided with sufficient insulation with the bedding material, and he or she is also free to adjust, it is impossible to determine the clothing insulation effect for these occupants unless they are immobile.

*ANSI/ASHRAE Standard 55* cautious the users that there are two forms of variability among occupants. In the first form, different individuals wear different clothing due to factors that are not related to thermal conditions, and the second form is opposite. For the first, it is not correct to use the average clothing insulation value to determine the desired thermal conditions for all occupants.

## History of the standard

*ANSI/ASHRAE Standard 55* was first published in 1966. It was revised in 1974, 1981, 1992, 2004, 2010, 2013, 2017, 2020 and 2023. Starting in 2004, it is now updated based on ASHRAE's standard maintenance procedures. These periodic revisions are based on a publicly reviewed addenda to the previous version available on ASHRAE's website.

In 1992 the standard was updated with more extensive information on measurement protocols and an expanded definitions section.

In 2004 the standard underwent significant changes with the addition of two thermal comfort models: the PMV/PPD model and the adaptive comfort model.

In 2010 the standard included the following changes. It re-introduced the Standard Effective Temperature (SET) as a method to calculate the cooling effect of air movement. It also added a general satisfaction survey to section 7 intended to evaluate general thermal comfort in an occupied space, bringing the standard in line with current survey-based post-occupancy evaluation (POE) practices.

In 2013 the body of the standard was rewritten in mandatory language, with informative language moved from the body of the standard to informative appendices. The applicability of the cooling effect of air movement was expanded to apply to naturally conditioned spaces. Section 7 underwent major revisions for measuring thermal comfort in existing spaces including procedures for physical measurements and survey methods, and how to evaluate and report results. The last major change concerns measuring air speed and air temperature experienced by the occupant, which now must be an average across three heights and over a period of time. The 2020 edition included eleven addenda, that introduced following changes:

- Replacement of the graphical method with normative graphical examples of specific conditions using the analytical method and elevated airspeed methods
- Expanded applicability of the adaptive model used for naturally conditioned spaces that have a mechanical cooling system installed
- A new method for assessment of local thermal discomfort with vertical air temperature gradient between the head level and ankle level
- A wider applicability if the standard, which covers metabolic rates up to 4 from 2
- A consolidation and simplification of calculation methods in the standard, which are now limited to two methods - standard and adaptive - and a new flow chart that provides guidance in when to use each calculation method
- An overhaul of the documentation requirements of the standard (Section 6) that includes additions, clarifications, and simplifications, along with a new example spreadsheet compliance form that replaced the prior example form.

It was replaced by 2023 edition, which incorporated previous addenda to 2020 edition with renewed focus on organizational clarity.
