"""Deep electrical, RF, analog, and power engineering."""
from .common import CC_BY_SA, wiki

DOMAINS = {
    "transmission-lines": {
        "tags": ["transmission line", "characteristic impedance", "standing wave ratio", "reflection coefficient"],
        "license": CC_BY_SA,
        "pages": wiki("Transmission_line", "Characteristic_impedance", "Standing_wave_ratio",
                      "Smith_chart", "Impedance_matching", "Reflection_coefficient")},
    "waveguides": {
        "tags": ["rectangular waveguide", "cutoff frequency", "transverse mode", "waveguide filter"],
        "license": CC_BY_SA,
        "pages": wiki("Waveguide", "Rectangular_waveguide", "Waveguide_(electromagnetism)",
                      "Cutoff_frequency", "Transverse_mode", "Waveguide_filter", "Circulator")},
    "antenna-theory": {
        "tags": ["dipole antenna", "radiation pattern", "antenna aperture", "monopole antenna"],
        "license": CC_BY_SA,
        "pages": wiki("Antenna_(radio)", "Dipole_antenna", "Radiation_pattern", "Antenna_gain",
                      "Antenna_aperture", "Yagi-Uda_antenna", "Monopole_antenna")},
    "antenna-arrays": {
        "tags": ["antenna array", "phased array", "adaptive beamformer", "grating lobe"],
        "license": CC_BY_SA,
        "pages": wiki("Antenna_array", "Phased_array", "Beamforming", "Grating_lobe",
                      "Array_gain", "Adaptive_beamformer")},
    "microstrip-design": {
        "tags": ["microstrip line", "coplanar waveguide", "microstrip antenna", "stripline board"],
        "license": CC_BY_SA,
        "pages": wiki("Microstrip", "Microstrip_antenna", "Coplanar_waveguide",
                      "Stripline", "Microstrip_line")},
    "rf-amplifiers": {
        "tags": ["distributed amplifier", "Doherty amplifier", "traveling wave tube", "load pull"],
        "license": CC_BY_SA,
        "pages": wiki("RF_power_amplifier", "Distributed_amplifier", "Class-D_amplifier",
                      "Doherty_amplifier", "Travelling-wave_tube", "Load_pull")},
    "low-noise-amplifier": {
        "tags": ["low noise amplifier", "noise figure", "noise temperature", "Friis formula"],
        "license": CC_BY_SA,
        "pages": wiki("Low-noise_amplifier", "Noise_figure", "Noise_temperature",
                      "Friis_formulas_for_noise", "LC_circuit")},
    "power-amplifier-rf": {
        "tags": ["power amplifier classes", "power amplifier", "load pull", "Doherty amplifier"],
        "license": CC_BY_SA,
        "pages": wiki("Power_amplifier_classes", "Power_amplifier", "Class-D_amplifier",
                      "Doherty_amplifier", "Distributed_amplifier", "RF_power_amplifier")},
    "mixer-rf": {
        "tags": ["frequency mixer", "Gilbert cell", "image frequency", "superheterodyne receiver"],
        "license": CC_BY_SA,
        "pages": wiki("Frequency_mixer", "Gilbert_cell", "Heterodyne", "Image_frequency",
                      "Frequency_changer", "Superheterodyne_receiver")},
    "oscillator-circuits": {
        "tags": ["electronic oscillator", "Colpitts oscillator", "crystal oscillator", "phase noise"],
        "license": CC_BY_SA,
        "pages": wiki("Electronic_oscillator", "Colpitts_oscillator", "Hartley_oscillator",
                      "Crystal_oscillator", "Voltage-controlled_oscillator", "Phase_noise")},
    "phase-locked-loop": {
        "tags": ["phase-locked loop", "charge pump", "phase detector", "loop gain"],
        "license": CC_BY_SA,
        "pages": wiki("Phase-locked_loop", "Charge_pump", "Loop_gain",
                      "Phase_detector", "Frequency_divider")},
    "frequency-synthesizer": {
        "tags": ["frequency synthesizer", "direct digital synthesis", "fractional-N synthesizer", "numerically controlled oscillator"],
        "license": CC_BY_SA,
        "pages": wiki("Frequency_synthesizer", "Direct_digital_synthesis",
                      "Fractional-N_synthesizer", "Numerically-controlled_oscillator")},
    "rf-filters": {
        "tags": ["Butterworth filter", "Chebyshev filter", "elliptic filter", "interdigital filter"],
        "license": CC_BY_SA,
        "pages": wiki("Electronic_filter", "Butterworth_filter", "Chebyshev_filter",
                      "Elliptic_filter", "Interdigital_filter", "Combline_filter",
                      "Distributed-element_filter")},
    "cavity-resonators": {
        "tags": ["microwave cavity", "dielectric resonator", "quality factor", "helical resonator"],
        "license": CC_BY_SA,
        "pages": wiki("Resonator", "Microwave_cavity", "Dielectric_resonator",
                      "Q_factor", "Helical_resonator")},
    "smith-chart-matching": {
        "tags": ["antenna tuner", "quarter-wave transformer", "impedance matching", "matching stub"],
        "license": CC_BY_SA,
        "pages": wiki("Antenna_tuner", "Stub_(electronics)", "Quarter-wave_impedance_transformer",
                      "Balun", "Directional_coupler", "Impedance_matching")},
    "s-parameters": {
        "tags": ["scattering parameters", "two-port network", "return loss", "insertion loss"],
        "license": CC_BY_SA,
        "pages": wiki("Scattering_parameters", "Two-port_network", "Return_loss", "Insertion_loss")},
    "vector-network-analyzer": {
        "tags": ["vector network analyzer", "network analyzer", "time-domain reflectometer", "directional coupler"],
        "license": CC_BY_SA,
        "pages": wiki("Vector_network_analyzer", "Network_analyzer_(electrical)",
                      "Time-domain_reflectometer", "Directional_coupler")},
    "operational-amplifiers": {
        "tags": ["operational amplifier", "op amp integrator", "differential amplifier", "chopper amplifier"],
        "license": CC_BY_SA,
        "pages": wiki("Operational_amplifier", "Op_amp_integrator", "Op_amp",
                      "Differential_amplifier", "Chopper_(electronics)")},
    "instrumentation-amplifier": {
        "tags": ["instrumentation amplifier", "common-mode rejection ratio", "differential amplifier", "operational amplifier"],
        "license": CC_BY_SA,
        "pages": wiki("Instrumentation_amplifier", "Common-mode_rejection_ratio",
                      "Differential_amplifier", "Operational_amplifier")},
    "active-filters": {
        "tags": ["active filter", "Sallen-Key topology", "state variable filter", "gyrator circuit"],
        "license": CC_BY_SA,
        "pages": wiki("Active_filter", "Sallen-Key_topology", "State_variable_filter",
                      "Gyrator", "Butterworth_filter")},
    "passive-filters": {
        "tags": ["passive filter", "constant k filter", "m-derived filter", "resonant circuit"],
        "license": CC_BY_SA,
        "pages": wiki("Passive_filter", "RC_circuit", "RLC_circuit",
                      "Constant_k_filter", "M-derived_filter")},
    "switched-capacitor-filter": {
        "tags": ["switched capacitor", "correlated double sampling", "charge redistribution", "switched-capacitor filter"],
        "license": CC_BY_SA,
        "pages": wiki("Switched_capacitor", "Correlated_double_sampling", "LC_circuit")},
    "analog-to-digital-conversion": {
        "tags": ["analog-to-digital converter", "successive approximation", "flash ADC", "effective number of bits"],
        "license": CC_BY_SA,
        "pages": wiki("Analog-to-digital_converter", "Successive-approximation_ADC",
                      "Flash_ADC", "Integrating_ADC", "Effective_number_of_bits")},
    "digital-to-analog-conversion": {
        "tags": ["digital-to-analog converter", "R-2R ladder", "pulse-width modulation", "zero-order hold"],
        "license": CC_BY_SA,
        "pages": wiki("Digital-to-analog_converter", "R-2R_ladder",
                      "Pulse-width_modulation", "Zero-order_hold")},
    "sigma-delta-adc": {
        "tags": ["delta-sigma modulation", "noise shaping", "oversampling ratio", "decimation filter"],
        "license": CC_BY_SA,
        "pages": wiki("Delta-sigma_modulation", "Noise_shaping", "Oversampling",
                      "Decimation_(signal_processing)")},
    "sample-and-hold": {
        "tags": ["sample and hold", "aperture jitter", "zero-order hold", "track and hold"],
        "license": CC_BY_SA,
        "pages": wiki("Sample_and_hold", "Aperture_(antenna)", "Jitter", "Zero-order_hold")},
    "voltage-references": {
        "tags": ["voltage reference", "Zener diode", "shunt regulator", "precision reference"],
        "license": CC_BY_SA,
        "pages": wiki("Voltage_reference", "Zener_diode", "Shunt_regulator")},
    "bandgap-reference": {
        "tags": ["bandgap voltage reference", "Brokaw bandgap reference", "Widlar current mirror", "temperature compensation"],
        "license": CC_BY_SA,
        "pages": wiki("Bandgap_voltage_reference", "Brokaw_bandgap_reference", "Widlar_current_mirror")},
    "current-mirror": {
        "tags": ["current mirror", "Wilson current mirror", "cascode stage", "output impedance"],
        "license": CC_BY_SA,
        "pages": wiki("Current_mirror", "Wilson_current_mirror", "Widlar_current_mirror", "Cascode")},
    "differential-pair": {
        "tags": ["long-tailed pair", "differential amplifier", "emitter-coupled logic", "common-mode rejection ratio"],
        "license": CC_BY_SA,
        "pages": wiki("Long-tailed_pair", "Differential_amplifier",
                      "Emitter-coupled_logic", "Common-mode_rejection_ratio")},
    "power-supply-design": {
        "tags": ["power supply", "voltage regulator", "load regulation", "output ripple"],
        "license": CC_BY_SA,
        "pages": wiki("Power_supply", "Voltage_regulator", "Load_regulation", "Ripple_(electrical)")},
    "linear-regulator": {
        "tags": ["linear regulator", "dropout voltage", "quiescent current", "shunt regulator"],
        "license": CC_BY_SA,
        "pages": wiki("Linear_regulator", "Dropout_voltage", "Quiescent_current", "Shunt_regulator")},
    "switching-regulator": {
        "tags": ["switched-mode power supply", "DC-to-DC converter", "pulse-frequency modulation", "switching regulator"],
        "license": CC_BY_SA,
        "pages": wiki("Switched-mode_power_supply", "DC-to-DC_converter", "Pulse-frequency_modulation")},
    "buck-converter": {
        "tags": ["buck converter", "boost converter", "buck-boost converter", "Cuk converter"],
        "license": CC_BY_SA,
        "pages": wiki("Buck_converter", "Boost_converter", "Buck-boost_converter", "Ćuk_converter")},
    "boost-converter": {
        "tags": ["boost converter", "buck-boost converter", "power converter", "step-up converter"],
        "license": CC_BY_SA,
        "pages": wiki("Boost_converter", "Buck-boost_converter", "DC-to-DC_converter")},
    "flyback-converter": {
        "tags": ["flyback converter", "flyback transformer", "forward converter", "isolated converter"],
        "license": CC_BY_SA,
        "pages": wiki("Flyback_converter", "Flyback_transformer", "Forward_converter")},
    "ldo-regulator": {
        "tags": ["low-dropout regulator", "dropout voltage", "quiescent current", "power supply rejection ratio"],
        "license": CC_BY_SA,
        "pages": wiki("Low-dropout_regulator", "Dropout_voltage", "Quiescent_current")},
    "power-factor-correction": {
        "tags": ["power factor correction", "total harmonic distortion", "displacement power factor", "reactive power"],
        "license": CC_BY_SA,
        "pages": wiki("Power_factor", "Power_factor_correction",
                      "Total_harmonic_distortion", "Displacement_power_factor")},
    "motor-drive-electronics": {
        "tags": ["motor controller", "variable-frequency drive", "space vector modulation", "motor drive"],
        "license": CC_BY_SA,
        "pages": wiki("Motor_controller", "Variable-frequency_drive", "Space_vector_modulation")},
    "bldc-motor-control": {
        "tags": ["brushless DC motor", "back electromotive force", "Hall effect sensor", "electric commutator"],
        "license": CC_BY_SA,
        "pages": wiki("Brushless_DC_electric_motor", "Commutator_(electric)",
                      "Back_electromotive_force", "Hall_effect_sensor")},
    "field-oriented-control": {
        "tags": ["vector control motor", "Clarke transformation", "space vector modulation", "field-oriented control"],
        "license": CC_BY_SA,
        "pages": wiki("Vector_control_(motor)", "Clarke_transformation",
                      "Direct-quadrature-zero_transformation", "Space_vector_modulation")},
    "igbt-power": {
        "tags": ["insulated-gate bipolar transistor", "power semiconductor device", "safe operating area", "switching loss"],
        "license": CC_BY_SA,
        "pages": wiki("Insulated-gate_bipolar_transistor", "Power_semiconductor_device", "Safe_operating_area")},
    "mosfet-power": {
        "tags": ["power MOSFET", "body diode", "safe operating area", "on-state resistance"],
        "license": CC_BY_SA,
        "pages": wiki("Power_MOSFET", "Body_diode", "Safe_operating_area", "Power_semiconductor_device")},
    "gate-driver": {
        "tags": ["gate driver", "Miller effect", "bootstrap circuit", "high-side driver"],
        "license": CC_BY_SA,
        "pages": wiki("Gate_driver", "Miller_effect", "Bootstrapping_(electronics)")},
    "snubber-circuits": {
        "tags": ["snubber circuit", "RC snubber", "flyback diode", "transient-voltage-suppression diode"],
        "license": CC_BY_SA,
        "pages": wiki("Snubber", "RC_snubber", "Flyback_diode", "Transient-voltage-suppression_diode")},
    "thermal-management-electronics": {
        "tags": ["thermal management electronics", "heat sink", "thermal resistance", "junction temperature"],
        "license": CC_BY_SA,
        "pages": wiki("Thermal_management_(electronics)", "Heat_sink",
                      "Thermal_resistance", "Junction_temperature")},
    "electromagnetic-compatibility": {
        "tags": ["electromagnetic compatibility", "electromagnetic interference", "signal crosstalk", "common-mode signal"],
        "license": CC_BY_SA,
        "pages": wiki("Electromagnetic_compatibility", "Electromagnetic_interference",
                      "Crosstalk", "Common-mode_signal")},
    "emi-filtering": {
        "tags": ["ferrite bead", "common mode choke", "line filter", "electromagnetic interference"],
        "license": CC_BY_SA,
        "pages": wiki("Electromagnetic_shielding", "Ferrite_bead", "Common_mode_choke", "Line_filter")},
    "grounding-shielding": {
        "tags": ["ground loop", "Faraday cage", "chassis ground", "electromagnetic shielding"],
        "license": CC_BY_SA,
        "pages": wiki("Ground_(electricity)", "Ground_loop_(electricity)",
                      "Faraday_cage", "Chassis_ground")},
    "esd-protection": {
        "tags": ["electrostatic discharge", "human body model", "ohmic contact", "clamp diode"],
        "license": CC_BY_SA,
        "pages": wiki("Electrostatic_discharge", "Human_body_model",
                      "Transient-voltage-suppression_diode", "Ohmic_contact")},
    "battery-management-system": {
        "tags": ["battery management system", "state of charge", "battery balancing", "coulomb counting"],
        "license": CC_BY_SA,
        "pages": wiki("Battery_management_system", "State_of_charge",
                      "Battery_balancing", "Coulomb_counting", "Depth_of_discharge")},
    "energy-harvesting-circuits": {
        "tags": ["energy harvesting", "thermoelectric generator", "piezoelectric transducer", "power management circuit"],
        "license": CC_BY_SA,
        "pages": wiki("Energy_harvesting", "Rectenna", "Piezoelectricity", "Thermoelectric_generator")},
    "wireless-power-transfer": {
        "tags": ["wireless power transfer", "resonant inductive coupling", "inductive charging", "magnetic coupling"],
        "license": CC_BY_SA,
        "pages": wiki("Wireless_power_transfer", "Resonant_inductive_coupling",
                      "Inductive_charging", "Qi_(standard)")},
}
