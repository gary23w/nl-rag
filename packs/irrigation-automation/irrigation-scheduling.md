---
title: "Irrigation scheduling"
source: https://en.wikipedia.org/wiki/Irrigation_scheduling
domain: irrigation-automation
license: CC-BY-SA-4.0
tags: irrigation automation, drip irrigation, soil moisture, evapotranspiration
fetched: 2026-07-02
---

# Irrigation scheduling

**Irrigation scheduling** is the process used by irrigation system managers to determine the correct frequency and duration of watering. The goal is to apply enough water to fully wet the plant's root zone while minimizing overwatering and ensuring high water use efficiency (WUE).

Modern scheduling has evolved from simple calendar-based timers to "smart" systems that adapt dynamically to weather conditions and soil moisture levels.

## Methods of scheduling

Irrigation scheduling can be grouped into three primary methodologies, ranging from observation to advanced data analytics.

### Observation method

The most basic form of scheduling relies on visual cues or physical inspection.

- Visual cues: Monitoring plants for signs of water stress (wilting, leaf curling, or color changes) before watering.
- Feel and appearance method: Taking a soil sample by hand to estimate moisture content based on how the soil ribbons or clumps.

### Soil moisture measurement

This method uses sensors placed directly in the root zone to measure the volumetric water content or soil water tension.

- Tensiometers: Measure the force (tension) roots must exert to extract water.
- Capacitance Sensors: Measure the dielectric permittivity of the soil to determine water volume.
- Neutron Probes: Used in agriculture for highly accurate deep-soil readings.

These sensors can act as a "thermostat" for irrigation, triggering the system only when moisture drops below a specific Management Allowed Depletion (MAD) threshold.

### Meteorological (water balance) method

Also known as the "Checkbook Method," this approach calculates the water balance of the soil. It treats the soil reservoir like a bank account:

- Deposits: Rainfall and Irrigation.
- Withdrawals: Evapotranspiration (ET)—the combined loss of water via soil evaporation and plant transpiration.

The daily soil water balance equation is often expressed as:

$D_{c}=D_{p}+ET_{c}-P-I$

Where:

- $D_{c}$ = Current soil moisture depletion
- $D_{p}$ = Previous depletion
- $ET_{c}$ = Crop evapotranspiration (water used by crop)
- P = Precipitation (rain)
- I = Irrigation applied

This method relies heavily on accurate weather data to calculate daily water loss.

## Smart irrigation technologies

Advancements in "weather awareness" have led to the development of smart irrigation controllers that automate the scheduling process.

### Weather-based (ET) controllers

Evapotranspiration (ET) controllers adjust irrigation schedules daily based on local weather conditions. They calculate the Reference Evapotranspiration ( $ET_{0}$ )—the amount of water a standard grass surface would lose given the current temperature, humidity, wind speed, and solar radiation.

- Signal-Based: The controller receives a daily ET value via Wi-Fi or cellular signal from a local weather station.
- On-Site Calculation: The controller uses attached sensors (temperature and solar radiation) to calculate ET directly at the site.
- Historical: The controller uses a pre-programmed curve of historical average weather for the region (least accurate).

### Soil-based controllers

Instead of predicting water loss via weather data, these controllers measure actual soil moisture.

- Bypass System: The timer is set to run, but the cycle is interrupted (bypassed) if the soil moisture sensor detects wet soil.
- On-Demand System: The controller initiates irrigation *only* when the soil moisture sensor reaches a low threshold, regardless of time of day.

### Reactive sensors

- Rain sensor: Simple hygroscopic disks that swell when wet, breaking the electrical circuit to the valves during a storm.
- Freeze Sensors: Prevent irrigation when air temperatures drop below 32 °F (0 °C) to prevent ice hazards and plant damage.

## Agronomic principles

Successful scheduling requires understanding specific crop needs.

### Crop coefficient (Kc)

Not all plants use water at the same rate. The "weather awareness" ( $ET_{0}$ ) must be modified by a Crop Coefficient ( $K_{c}$ ) to get the actual water requirement ( $ET_{c}$ ). This relationship is defined by the Food and Agriculture Organization (FAO) Paper 56 standard:

$ET_{c}=ET_{0}\times K_{c}$

- $K_{c}>1$ : High-water users (e.g., Corn, Fescue grass).
- $K_{c}<1$ : Drought-tolerant plants (e.g., Cactus, native shrubs).

### Management allowed depletion (MAD)

MAD is the percentage of available soil water that can be depleted before plant stress occurs.

- Standard Crops: Often set at 50% depletion.
- Sensitive Crops: (e.g., Vegetables) may require watering at 30% depletion.
- Stress Tolerant: (e.g., Established trees) may tolerate 60-70% depletion.

## Benefits

- Water Conservation: The EPA WaterSense program estimates that up to 50% of landscape water is wasted due to inefficient methods, and that smart controllers can significantly reduce this waste.
- Plant Health: Prevents root rot from overwatering and drought stress from underwatering.
- Runoff Reduction: Cycle-and-soak scheduling prevents water from flowing off the landscape into storm drains.
