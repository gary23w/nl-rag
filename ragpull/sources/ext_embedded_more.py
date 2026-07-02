"""Sensors, actuators, motors, power, and low-level hardware building blocks."""
from .common import CC_BY_SA, wiki

DOMAINS = {
    "imu-sensors": {
        "tags": ["inertial measurement unit", "sensor fusion", "attitude heading reference", "dead reckoning"],
        "license": CC_BY_SA,
        "pages": wiki("Inertial_measurement_unit", "Sensor_fusion",
                      "Attitude_and_heading_reference_system", "Dead_reckoning",
                      "Microelectromechanical_systems", "Angular_velocity", "Precession")},
    "accelerometer-mems": {
        "tags": ["accelerometer sensor", "piezoelectric accelerometer", "proof mass", "seismometer"],
        "license": CC_BY_SA,
        "pages": wiki("Accelerometer", "Piezoelectric_accelerometer", "Proof_mass",
                      "Seismometer", "Comb_drive")},
    "gyroscope-mems": {
        "tags": ["gyroscope sensor", "vibrating structure gyroscope", "coriolis force", "ring laser gyroscope"],
        "license": CC_BY_SA,
        "pages": wiki("Gyroscope", "Vibrating_structure_gyroscope", "Coriolis_force",
                      "Ring_laser_gyroscope", "Fibre_optic_gyroscope")},
    "magnetometer-sensors": {
        "tags": ["magnetometer sensor", "hall effect", "magnetoresistance", "fluxgate magnetometer"],
        "license": CC_BY_SA,
        "pages": wiki("Magnetometer", "Hall_effect", "Magnetoresistance",
                      "Fluxgate_magnetometer", "Giant_magnetoresistance", "Compass")},
    "pressure-sensors": {
        "tags": ["pressure sensor", "piezoresistive effect", "bourdon tube", "barometer"],
        "license": CC_BY_SA,
        "pages": wiki("Pressure_sensor", "Piezoresistive_effect", "Bourdon_tube",
                      "Barometer", "Pressure_measurement")},
    "temperature-sensors": {
        "tags": ["thermistor sensor", "temperature measurement", "infrared thermometer", "bimetallic strip"],
        "license": CC_BY_SA,
        "pages": wiki("Thermistor", "Temperature_measurement", "Infrared_thermometer",
                      "Bimetallic_strip", "Thermometer")},
    "humidity-sensors": {
        "tags": ["hygrometer sensor", "relative humidity", "dew point", "psychrometrics"],
        "license": CC_BY_SA,
        "pages": wiki("Hygrometer", "Humidity", "Relative_humidity",
                      "Dew_point", "Psychrometrics")},
    "gas-sensors": {
        "tags": ["gas detector", "chemiresistor sensor", "nondispersive infrared sensor", "catalytic bead sensor"],
        "license": CC_BY_SA,
        "pages": wiki("Gas_detector", "Chemiresistor", "Nondispersive_infrared_sensor",
                      "Catalytic_bead_sensor", "Electrochemical_gas_sensor", "Carbon_dioxide_sensor")},
    "proximity-sensors": {
        "tags": ["proximity sensor", "photoelectric sensor", "passive infrared sensor", "capacitive displacement sensor"],
        "license": CC_BY_SA,
        "pages": wiki("Proximity_sensor", "Photoelectric_sensor", "Passive_infrared_sensor",
                      "Capacitive_displacement_sensor", "Time-of-flight_camera")},
    "hall-effect-sensors": {
        "tags": ["hall effect sensor", "magnetic field sensing", "wiegand effect", "reed switch"],
        "license": CC_BY_SA,
        "pages": wiki("Hall_effect_sensor", "Magnetic_field", "Wiegand_effect", "Reed_switch")},
    "rotary-encoders": {
        "tags": ["rotary encoder", "incremental encoder", "gray code", "resolver device"],
        "license": CC_BY_SA,
        "pages": wiki("Rotary_encoder", "Incremental_encoder", "Gray_code",
                      "Resolver_(electrical)", "Linear_encoder", "Encoder")},
    "load-cells-strain": {
        "tags": ["load cell", "strain gauge", "wheatstone bridge", "force-sensing resistor"],
        "license": CC_BY_SA,
        "pages": wiki("Load_cell", "Strain_gauge", "Wheatstone_bridge",
                      "Force-sensing_resistor", "Deformation_(engineering)", "Torque")},
    "capacitive-sensing": {
        "tags": ["capacitive sensing", "capacitance measurement", "touchscreen sensing", "tactile sensor"],
        "license": CC_BY_SA,
        "pages": wiki("Capacitive_sensing", "Capacitance", "Touchscreen", "Tactile_sensor")},
    "inductive-sensing": {
        "tags": ["inductive sensor", "eddy current", "inductance measurement", "linear variable differential transformer"],
        "license": CC_BY_SA,
        "pages": wiki("Inductive_sensor", "Eddy_current", "Inductance",
                      "Linear_variable_differential_transformer")},
    "ultrasonic-sensors": {
        "tags": ["ultrasonic transducer", "ultrasonic sonar", "echo sounding", "piezoelectricity transducer"],
        "license": CC_BY_SA,
        "pages": wiki("Ultrasonic_transducer", "Sonar", "Echo_sounding", "Piezoelectricity")},
    "time-of-flight-sensors": {
        "tags": ["time of flight", "single-photon avalanche diode", "laser rangefinder", "rangefinder device"],
        "license": CC_BY_SA,
        "pages": wiki("Time_of_flight", "Single-photon_avalanche_diode",
                      "Laser_rangefinder", "Rangefinder")},
    "lidar-sensors-deep": {
        "tags": ["lidar scanning", "optical time-domain reflectometer", "point cloud", "beam steering"],
        "license": CC_BY_SA,
        "pages": wiki("Lidar", "Optical_time-domain_reflectometer", "Point_cloud", "Beam_steering")},
    "image-sensors-cmos": {
        "tags": ["image sensor", "active-pixel sensor", "bayer filter", "rolling shutter"],
        "license": CC_BY_SA,
        "pages": wiki("Image_sensor", "Active-pixel_sensor", "Bayer_filter",
                      "Rolling_shutter", "Quantum_efficiency")},
    "ccd-sensors": {
        "tags": ["charge-coupled device", "photodetector element", "photoelectric effect", "responsivity metric"],
        "license": CC_BY_SA,
        "pages": wiki("Charge-coupled_device", "Photodetector", "Photoelectric_effect", "Responsivity")},
    "photodiodes": {
        "tags": ["photodiode sensor", "avalanche photodiode", "photoresistor cell", "phototransistor device"],
        "license": CC_BY_SA,
        "pages": wiki("Photodiode", "Avalanche_photodiode", "Photoresistor", "Phototransistor")},
    "thermocouples": {
        "tags": ["thermocouple sensor", "thermoelectric effect", "seebeck coefficient", "thermopile array"],
        "license": CC_BY_SA,
        "pages": wiki("Thermocouple", "Thermoelectric_effect", "Seebeck_coefficient", "Thermopile")},
    "rtd-sensors": {
        "tags": ["resistance thermometer", "platinum resistance thermometer", "callendar van dusen equation", "temperature coefficient"],
        "license": CC_BY_SA,
        "pages": wiki("Resistance_thermometer", "Platinum_resistance_thermometer",
                      "Callendar%E2%80%93Van_Dusen_equation")},
    "ph-sensors": {
        "tags": ["ph meter", "glass electrode", "ion-selective electrode", "nernst equation"],
        "license": CC_BY_SA,
        "pages": wiki("PH_meter", "Glass_electrode", "Ion-selective_electrode",
                      "Reference_electrode", "Nernst_equation", "Buffer_solution")},
    "flow-sensors": {
        "tags": ["flow measurement", "mass flow meter", "venturi effect", "orifice plate"],
        "license": CC_BY_SA,
        "pages": wiki("Flow_measurement", "Mass_flow_meter", "Venturi_effect",
                      "Orifice_plate", "Rotameter", "Thermal_mass_flow_meter")},
    "current-sensing": {
        "tags": ["current sensor", "current clamp", "rogowski coil", "current transformer"],
        "license": CC_BY_SA,
        "pages": wiki("Current_sensor", "Current_clamp", "Shunt_(electrical)",
                      "Rogowski_coil", "Current_transformer", "Ammeter")},
    "dc-motors": {
        "tags": ["brushed dc motor", "electric commutator", "motor armature", "back electromotive force"],
        "license": CC_BY_SA,
        "pages": wiki("DC_motor", "Brushed_DC_electric_motor", "Commutator_(electric)",
                      "Electric_motor", "Armature_(electrical)", "Back_electromotive_force")},
    "stepper-motors-deep": {
        "tags": ["stepper motor", "microstepping drive", "switched reluctance motor", "holding torque"],
        "license": CC_BY_SA,
        "pages": wiki("Stepper_motor", "Switched_reluctance_motor", "Reluctance_motor")},
    "servo-motors-deep": {
        "tags": ["servomotor drive", "servomechanism loop", "closed-loop controller", "radio control servo"],
        "license": CC_BY_SA,
        "pages": wiki("Servomotor", "Servomechanism", "Closed-loop_controller",
                      "Servo_(radio_control)")},
    "brushless-dc-motors": {
        "tags": ["brushless dc motor", "field-oriented control", "permanent magnet synchronous motor", "commutation scheme"],
        "license": CC_BY_SA,
        "pages": wiki("Brushless_DC_electric_motor", "Field-oriented_control",
                      "Permanent_magnet_synchronous_motor")},
    "ac-induction-motors": {
        "tags": ["induction motor", "squirrel-cage rotor", "rotating magnetic field", "wound rotor motor"],
        "license": CC_BY_SA,
        "pages": wiki("Induction_motor", "Squirrel-cage_rotor", "Rotating_magnetic_field",
                      "Wound_rotor_motor", "Synchronous_motor")},
    "motor-drivers-hbridge": {
        "tags": ["h-bridge driver", "motor controller", "pulse-width modulation drive", "freewheeling diode"],
        "license": CC_BY_SA,
        "pages": wiki("H_bridge", "Motor_controller", "Pulse-width_modulation",
                      "Freewheeling_diode", "Current_limiting")},
    "solenoids-relays": {
        "tags": ["solenoid coil", "electromechanical relay", "contactor switch", "solenoid valve"],
        "license": CC_BY_SA,
        "pages": wiki("Solenoid", "Relay", "Contactor", "Electromagnet", "Solenoid_valve")},
    "piezoelectric-actuators": {
        "tags": ["piezoelectric motor", "ultrasonic motor", "piezoelectric sensor", "inchworm motor"],
        "license": CC_BY_SA,
        "pages": wiki("Piezoelectric_motor", "Ultrasonic_motor", "Piezoelectric_sensor",
                      "Inchworm_motor")},
    "shape-memory-alloys": {
        "tags": ["shape-memory alloy", "nitinol material", "superelasticity effect", "martensite phase"],
        "license": CC_BY_SA,
        "pages": wiki("Shape-memory_alloy", "Nitinol", "Superelasticity",
                      "Martensite", "Austenite")},
    "linear-actuators": {
        "tags": ["linear actuator", "ball screw", "leadscrew drive", "rack and pinion"],
        "license": CC_BY_SA,
        "pages": wiki("Linear_actuator", "Ball_screw", "Leadscrew",
                      "Actuator", "Roller_screw", "Rack_and_pinion")},
    "pneumatic-actuators": {
        "tags": ["pneumatic actuator", "pneumatic cylinder", "compressed air", "control valve"],
        "license": CC_BY_SA,
        "pages": wiki("Pneumatic_actuator", "Pneumatic_cylinder", "Pneumatics",
                      "Compressed_air", "Control_valve", "Air_compressor")},
    "hydraulic-actuators": {
        "tags": ["hydraulic actuator", "hydraulic cylinder", "hydraulic machinery", "hydraulic pump"],
        "license": CC_BY_SA,
        "pages": wiki("Hydraulic_actuator", "Hydraulics", "Hydraulic_machinery",
                      "Hydraulic_fluid", "Hydraulic_pump")},
    "battery-chemistry-embedded": {
        "tags": ["rechargeable battery", "nickel metal hydride battery", "lead acid battery", "energy density"],
        "license": CC_BY_SA,
        "pages": wiki("Rechargeable_battery", "Battery_(electricity)",
                      "Nickel%E2%80%93metal_hydride_battery", "Lead%E2%80%93acid_battery",
                      "Battery_pack", "Energy_density", "Battery_charger")},
    "lithium-battery-management": {
        "tags": ["lithium-ion battery", "battery management system", "state of charge", "battery balancing"],
        "license": CC_BY_SA,
        "pages": wiki("Lithium-ion_battery", "Battery_management_system", "State_of_charge",
                      "Battery_balancing", "Depth_of_discharge")},
    "supercapacitors": {
        "tags": ["supercapacitor cell", "pseudocapacitance charge", "equivalent series resistance", "ragone plot"],
        "license": CC_BY_SA,
        "pages": wiki("Supercapacitor", "Pseudocapacitor", "Equivalent_series_resistance",
                      "Ragone_plot")},
    "energy-harvesting-deep": {
        "tags": ["energy harvesting", "rectenna device", "thermoelectric generator", "vibration powered generator"],
        "license": CC_BY_SA,
        "pages": wiki("Energy_harvesting", "Rectenna", "Thermoelectric_generator",
                      "Photovoltaics", "Vibration_powered_generator")},
    "voltage-regulators-deep": {
        "tags": ["voltage regulator", "linear regulator", "low-dropout regulator", "switched-mode power supply"],
        "license": CC_BY_SA,
        "pages": wiki("Voltage_regulator", "Linear_regulator", "Low-dropout_regulator",
                      "Switched-mode_power_supply", "DC-to-DC_converter",
                      "Buck_converter", "Boost_converter")},
    "power-sequencing": {
        "tags": ["power-on reset", "inrush current", "hot swapping", "power management integrated circuit"],
        "license": CC_BY_SA,
        "pages": wiki("Power-on_reset", "Inrush_current", "Hot_swapping",
                      "Power_management_integrated_circuit")},
    "level-shifters": {
        "tags": ["level shifter", "logic level", "open collector", "logic family"],
        "license": CC_BY_SA,
        "pages": wiki("Level_shifter", "Logic_level", "Open_collector",
                      "Voltage_divider", "Logic_family")},
    "gpio-expanders": {
        "tags": ["general-purpose input output", "shift register", "serial peripheral interface", "port expander"],
        "license": CC_BY_SA,
        "pages": wiki("General-purpose_input/output", "I%C2%B2C", "Shift_register",
                      "Serial_Peripheral_Interface")},
    "real-time-clock": {
        "tags": ["real-time clock", "backup battery", "time standard", "epoch counter"],
        "license": CC_BY_SA,
        "pages": wiki("Real-time_clock", "Backup_battery", "Time_standard")},
    "crystal-oscillators-deep": {
        "tags": ["crystal oscillator", "colpitts oscillator", "pierce oscillator", "quartz clock"],
        "license": CC_BY_SA,
        "pages": wiki("Crystal_oscillator", "Electronic_oscillator", "Colpitts_oscillator",
                      "Pierce_oscillator", "Quartz_clock", "Frequency_drift", "Crystal_oven")},
    "watchdog-supervisors": {
        "tags": ["watchdog timer", "brownout detection", "reset circuit", "fail-safe design"],
        "license": CC_BY_SA,
        "pages": wiki("Watchdog_timer", "Brownout_(electricity)", "Reset_(computing)",
                      "Fail-safe")},
    "esd-protection-deep": {
        "tags": ["electrostatic discharge", "transient-voltage-suppression diode", "human body model", "varistor clamp"],
        "license": CC_BY_SA,
        "pages": wiki("Electrostatic_discharge", "Transient-voltage-suppression_diode",
                      "Human_body_model", "Gas_discharge_tube", "Varistor")},
    "emc-design-embedded": {
        "tags": ["electromagnetic compatibility", "electromagnetic interference", "ferrite bead", "common mode choke"],
        "license": CC_BY_SA,
        "pages": wiki("Electromagnetic_compatibility", "Electromagnetic_interference",
                      "Ferrite_bead", "Choke_(electronics)", "Faraday_cage",
                      "Ground_loop_(electricity)")},
    "pcb-layout-embedded": {
        "tags": ["printed circuit board", "surface-mount technology", "board via", "solder mask"],
        "license": CC_BY_SA,
        "pages": wiki("Printed_circuit_board", "Surface-mount_technology",
                      "Via_(electronics)", "Solder_mask", "Decoupling_capacitor",
                      "Copper_pour")},
}
