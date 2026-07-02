"""Industrial, building-automation, and energy-systems protocols."""
from .common import CC_BY_SA, wiki

DOMAINS = {
    "profinet": {
        "tags": ['profinet', 'industrial ethernet', 'real-time fieldbus', 'profinet io'],
        "license": CC_BY_SA,
        "pages": wiki('PROFINET', 'Industrial_Ethernet', 'Fieldbus', 'Programmable_logic_controller', 'Real-time_computing', 'Automation'),
    },
    "ethercat": {
        "tags": ['ethercat', 'ethercat protocol', 'industrial ethernet', 'distributed clocks'],
        "license": CC_BY_SA,
        "pages": wiki('EtherCAT', 'Industrial_Ethernet', 'Fieldbus', 'Distributed_control_system', 'Real-time_computing', 'Motion_control'),
    },
    "modbus-protocol": {
        "tags": ['modbus protocol', 'modbus rtu', 'modbus tcp', 'serial fieldbus'],
        "license": CC_BY_SA,
        "pages": wiki('Modbus', 'RS-485', 'Serial_communication', 'Master/slave_(technology)', 'Remote_terminal_unit', 'SCADA'),
    },
    "opc-ua-deep": {
        "tags": ['opc ua', 'opc unified architecture', 'industrial interoperability', 'opc ua information model'],
        "license": CC_BY_SA,
        "pages": wiki('OPC_Unified_Architecture', 'Open_Platform_Communications', 'Service-oriented_architecture', 'Information_model', 'Publish%E2%80%93subscribe_pattern', 'Industrial_internet_of_things'),
    },
    "dnp3-protocol": {
        "tags": ['dnp3 protocol', 'distributed network protocol', 'scada outstation', 'utility telemetry'],
        "license": CC_BY_SA,
        "pages": wiki('DNP3', 'SCADA', 'Remote_terminal_unit', 'Electric_power_transmission', 'Substation', 'Telemetry'),
    },
    "iec-61850": {
        "tags": ['iec 61850', 'substation automation', 'goose messaging', 'intelligent electronic device'],
        "license": CC_BY_SA,
        "pages": wiki('IEC_61850', 'Electrical_substation', 'Intelligent_electronic_device', 'Generic_Substation_Events', 'Protective_relay', 'Electric_power_system'),
    },
    "bacnet": {
        "tags": ['bacnet building automation', 'bacnet protocol', 'building automation network', 'direct digital control'],
        "license": CC_BY_SA,
        "pages": wiki('BACnet', 'Building_automation', 'HVAC_control_system', 'Direct_digital_control', 'ASHRAE', 'Building_management_system'),
    },
    "canopen": {
        "tags": ['canopen protocol', 'canopen fieldbus', 'can bus higher-layer', 'embedded device network'],
        "license": CC_BY_SA,
        "pages": wiki('CANopen', 'CAN_bus', 'Fieldbus', 'Embedded_system', 'Electronic_data_sheet', 'Motion_control'),
    },
    "devicenet": {
        "tags": ['devicenet protocol', 'devicenet fieldbus', 'common industrial protocol', 'can-based fieldbus'],
        "license": CC_BY_SA,
        "pages": wiki('DeviceNet', 'CAN_bus', 'Fieldbus', 'Common_Industrial_Protocol', 'Open_DeviceNet_Vendors_Association', 'Industrial_control_system'),
    },
    "profibus": {
        "tags": ['profibus protocol', 'profibus dp', 'profibus pa', 'process fieldbus'],
        "license": CC_BY_SA,
        "pages": wiki('Profibus', 'Fieldbus', 'RS-485', 'Master/slave_(technology)', 'Distributed_control_system', 'Process_control'),
    },
    "ethernet-ip": {
        "tags": ['ethernet/ip protocol', 'ethernet industrial protocol', 'common industrial protocol', 'odva network'],
        "license": CC_BY_SA,
        "pages": wiki('EtherNet/IP', 'Common_Industrial_Protocol', 'Industrial_Ethernet', 'ODVA_(company)', 'Fieldbus', 'Producer%E2%80%93consumer_problem'),
    },
    "powerlink": {
        "tags": ['ethernet powerlink', 'powerlink protocol', 'real-time industrial ethernet', 'deterministic ethernet'],
        "license": CC_BY_SA,
        "pages": wiki('Ethernet_Powerlink', 'Industrial_Ethernet', 'Real-time_computing', 'Fieldbus', 'Time-division_multiple_access', 'Motion_control'),
    },
    "sercos": {
        "tags": ['sercos interface', 'sercos iii', 'motion control bus', 'servo drive network'],
        "license": CC_BY_SA,
        "pages": wiki('SERCOS_interface', 'SERCOS_III', 'Industrial_Ethernet', 'Motion_control', 'Real-time_computing', 'Servomotor'),
    },
    "io-link": {
        "tags": ['io-link protocol', 'io-link sensor', 'point-to-point sensor link', 'smart sensor interface'],
        "license": CC_BY_SA,
        "pages": wiki('IO-Link', 'Sensor', 'Actuator', 'Fieldbus', 'Point-to-point_(telecommunications)', 'Automation'),
    },
    "hart-protocol": {
        "tags": ['hart protocol', 'highway addressable remote transducer', '4-20 ma signaling', 'smart field instrument'],
        "license": CC_BY_SA,
        "pages": wiki('Highway_Addressable_Remote_Transducer_Protocol', '4-20_mA', 'Fieldbus', 'Process_control', 'Transmitter', 'Instrumentation'),
    },
    "foundation-fieldbus": {
        "tags": ['foundation fieldbus', 'fieldbus function block', 'process automation fieldbus', 'h1 fieldbus'],
        "license": CC_BY_SA,
        "pages": wiki('Foundation_Fieldbus', 'Fieldbus', 'Process_control', 'Distributed_control_system', 'Instrumentation', 'Function_block_diagram'),
    },
    "as-interface": {
        "tags": ['as-interface protocol', 'actuator sensor interface', 'binary sensor bus', 'lowest-level fieldbus'],
        "license": CC_BY_SA,
        "pages": wiki('AS-Interface', 'Fieldbus', 'Actuator', 'Sensor', 'Automation', 'Master/slave_(technology)'),
    },
    "knx-building": {
        "tags": ['knx building automation', 'knx protocol', 'home and building control', 'building control bus'],
        "license": CC_BY_SA,
        "pages": wiki('KNX_(standard)', 'Building_automation', 'Home_automation', 'Twisted_pair', 'Lighting_control_system', 'Building_management_system'),
    },
    "lonworks": {
        "tags": ['lonworks protocol', 'lontalk network', 'control networking', 'power-line building control'],
        "license": CC_BY_SA,
        "pages": wiki('LonWorks', 'Building_automation', 'Fieldbus', 'Power-line_communication', 'Echelon_Corporation', 'Home_automation'),
    },
    "mbus-metering": {
        "tags": ['m-bus metering', 'meter-bus protocol', 'remote meter reading', 'utility metering bus'],
        "license": CC_BY_SA,
        "pages": wiki('Meter-Bus', 'Smart_meter', 'Automatic_meter_reading', 'Utility_submeter', 'Water_metering', 'Data_logger'),
    },
    "zigbee-deep": {
        "tags": ['zigbee protocol', 'zigbee mesh', 'ieee 802.15.4 network', 'low-power mesh networking'],
        "license": CC_BY_SA,
        "pages": wiki('Zigbee', 'IEEE_802.15.4', 'Personal_area_network', 'Mesh_networking', 'Home_automation', 'Low-power_electronics'),
    },
    "z-wave-deep": {
        "tags": ['z-wave protocol', 'z-wave mesh', 'smart home rf', 'sub-ghz home automation'],
        "license": CC_BY_SA,
        "pages": wiki('Z-Wave', 'Home_automation', 'Mesh_networking', 'Wireless_sensor_network', 'Smart_home', 'ISM_radio_band'),
    },
    "thread-matter": {
        "tags": ['thread network protocol', 'matter standard', 'thread mesh', 'ipv6 smart home'],
        "license": CC_BY_SA,
        "pages": wiki('Thread_(network_protocol)', 'Matter_(standard)', '6LoWPAN', 'IEEE_802.15.4', 'IPv6', 'Connectivity_Standards_Alliance'),
    },
    "wirelesshart": {
        "tags": ['wirelesshart protocol', 'wireless hart mesh', 'industrial wireless sensor', 'process wireless network'],
        "license": CC_BY_SA,
        "pages": wiki('WirelessHART', 'Highway_Addressable_Remote_Transducer_Protocol', 'IEEE_802.15.4', 'Mesh_networking', 'Wireless_sensor_network', 'Process_control'),
    },
    "isa-100": {
        "tags": ['isa100 wireless', 'isa100.11a protocol', 'industrial wireless automation', 'process control wireless'],
        "license": CC_BY_SA,
        "pages": wiki('ISA100.11a', 'International_Society_of_Automation', 'Wireless_sensor_network', 'IEEE_802.15.4', 'Mesh_networking', 'Process_control'),
    },
    "lorawan-deep": {
        "tags": ['lorawan protocol', 'lora wide-area network', 'lpwan networking', 'chirp spread spectrum radio'],
        "license": CC_BY_SA,
        "pages": wiki('LoRaWAN', 'LoRa', 'Low-power_wide-area_network', 'Chirp_spread_spectrum', 'ISM_radio_band', 'Wireless_sensor_network'),
    },
    "nb-iot-deep": {
        "tags": ['nb-iot protocol', 'narrowband iot', 'cellular lpwan', '3gpp machine-type communication'],
        "license": CC_BY_SA,
        "pages": wiki('Narrowband_IoT', 'LTE_(telecommunication)', 'Low-power_wide-area_network', '3GPP', 'Cellular_network', 'Machine_to_machine'),
    },
    "sigfox": {
        "tags": ['sigfox network', 'sigfox lpwan', 'ultra-narrowband iot', 'low-throughput network'],
        "license": CC_BY_SA,
        "pages": wiki('Sigfox', 'Low-power_wide-area_network', 'Narrowband', 'ISM_radio_band', 'Machine_to_machine', 'Internet_of_things'),
    },
    "wireless-mbus": {
        "tags": ['wireless m-bus', 'wireless meter-bus', 'radio meter reading', 'wm-bus metering'],
        "license": CC_BY_SA,
        "pages": wiki('Wireless_M-Bus', 'Smart_meter', 'Automatic_meter_reading', 'Short-range_device', 'Telemetry', 'Utility_submeter'),
    },
    "dali-lighting": {
        "tags": ['dali lighting protocol', 'digital addressable lighting interface', 'lighting control bus', 'led dimming control'],
        "license": CC_BY_SA,
        "pages": wiki('Digital_Addressable_Lighting_Interface', 'Lighting_control_system', 'Light-emitting_diode', 'Electrical_ballast', 'Building_automation', 'Dimmer'),
    },
    "dmx512-lighting": {
        "tags": ['dmx512 protocol', 'dmx lighting control', 'stage lighting control', 'entertainment lighting bus'],
        "license": CC_BY_SA,
        "pages": wiki('DMX512', 'Stage_lighting', 'RS-485', 'Lighting_control_console', 'Architectural_lighting_design', 'RDM_(lighting)'),
    },
    "obix": {
        "tags": ['obix protocol', 'open building information exchange', 'building automation web service', 'facilities data exchange'],
        "license": CC_BY_SA,
        "pages": wiki('OBIX', 'Building_automation', 'Web_service', 'Representational_state_transfer', 'Building_management_system', 'Extensible_Markup_Language'),
    },
    "mtconnect": {
        "tags": ['mtconnect protocol', 'mtconnect standard', 'machine tool data', 'cnc monitoring standard'],
        "license": CC_BY_SA,
        "pages": wiki('MTConnect', 'Machine_tool', 'Computer_numerical_control', 'Manufacturing_execution_system', 'Extensible_Markup_Language', 'Overall_equipment_effectiveness'),
    },
    "opc-classic": {
        "tags": ['opc classic', 'ole for process control', 'opc da protocol', 'com-based process interface'],
        "license": CC_BY_SA,
        "pages": wiki('Open_Platform_Communications', 'OLE_for_Process_Control', 'Component_Object_Model', 'SCADA', 'Distributed_Component_Object_Model', 'Process_control'),
    },
    "iec-60870": {
        "tags": ['iec 60870-5', 'telecontrol protocol', 'scada telecontrol', 'power system telemetry'],
        "license": CC_BY_SA,
        "pages": wiki('IEC_60870-5', 'SCADA', 'Remote_terminal_unit', 'Electric_power_transmission', 'Telecontrol', 'Telemetry'),
    },
    "iec-62443-security": {
        "tags": ['iec 62443', 'industrial automation security', 'ot security standard', 'control system cybersecurity'],
        "license": CC_BY_SA,
        "pages": wiki('IEC_62443', 'Industrial_control_system', 'Cyber-physical_system', 'Defense_in_depth_(computing)', 'Security_level', 'Operational_technology'),
    },
    "purdue-model": {
        "tags": ['purdue model', 'purdue reference architecture', 'ics network segmentation', 'ot network zones'],
        "license": CC_BY_SA,
        "pages": wiki('Purdue_Enterprise_Reference_Architecture', 'Industrial_control_system', 'Operational_technology', 'Manufacturing_execution_system', 'Enterprise_resource_planning', 'Defense_in_depth_(computing)'),
    },
    "industrial-control-security": {
        "tags": ['industrial control security', 'ics cybersecurity', 'ot threat model', 'critical infrastructure defense'],
        "license": CC_BY_SA,
        "pages": wiki('Industrial_control_system', 'Stuxnet', 'SCADA', 'Air_gap_(networking)', 'Critical_infrastructure_protection', 'Operational_technology'),
    },
    "smart-grid": {
        "tags": ['smart grid', 'intelligent electrical grid', 'grid modernization', 'distributed energy grid'],
        "license": CC_BY_SA,
        "pages": wiki('Smart_grid', 'Electrical_grid', 'Demand_response', 'Distributed_generation', 'Advanced_metering_infrastructure', 'Grid_energy_storage'),
    },
    "ami-metering": {
        "tags": ['ami metering', 'advanced metering infrastructure', 'smart meter network', 'meter data collection'],
        "license": CC_BY_SA,
        "pages": wiki('Advanced_metering_infrastructure', 'Smart_meter', 'Automatic_meter_reading', 'Meter_data_management', 'Net_metering', 'Home_area_network'),
    },
    "iec-61970-cim": {
        "tags": ['iec 61970 cim', 'common information model electricity', 'power system data model', 'grid model interoperability'],
        "license": CC_BY_SA,
        "pages": wiki('Common_Information_Model_(electricity)', 'Energy_management_system', 'Electric_power_system', 'Interoperability', 'Unified_Modeling_Language', 'Electrical_grid'),
    },
    "synchrophasor-pmu": {
        "tags": ['synchrophasor measurement', 'phasor measurement unit', 'wide-area monitoring', 'grid phasor telemetry'],
        "license": CC_BY_SA,
        "pages": wiki('Phasor_measurement_unit', 'Wide_area_synchronous_grid', 'Electric_power_transmission', 'Phasor', 'Power-system_protection', 'Electrical_grid'),
    },
    "demand-response": {
        "tags": ['demand response', 'electricity load management', 'peak demand shaping', 'dynamic electricity demand'],
        "license": CC_BY_SA,
        "pages": wiki('Demand_response', 'Load_management', 'Peak_demand', 'Electricity_market', 'Smart_grid', 'Dynamic_demand_(electric_power)'),
    },
    "scada-historian": {
        "tags": ['scada historian', 'operational historian', 'process data historian', 'time-series process archive'],
        "license": CC_BY_SA,
        "pages": wiki('Operational_historian', 'SCADA', 'Time_series_database', 'Data_historian', 'Process_control', 'Manufacturing_execution_system'),
    },
    "batch-control-isa88": {
        "tags": ['isa-88 batch control', 'batch process control', 'batch recipe model', 'batch manufacturing standard'],
        "license": CC_BY_SA,
        "pages": wiki('ISA-88', 'Batch_production', 'Process_control', 'Manufacturing_execution_system', 'Sequential_function_chart', 'International_Society_of_Automation'),
    },
    "iso-15926": {
        "tags": ['iso 15926', 'process plant data model', 'plant lifecycle data', 'engineering data interoperability'],
        "license": CC_BY_SA,
        "pages": wiki('ISO_15926', 'Process_plant', 'Product_lifecycle', 'Data_modeling', 'Ontology_(information_science)', 'Interoperability'),
    },
    "packml": {
        "tags": ['packml standard', 'packaging machine language', 'omac state model', 'machine state automation'],
        "license": CC_BY_SA,
        "pages": wiki('PackML', 'Packaging_machinery', 'Automation', 'State_machine', 'OMAC', 'Manufacturing_execution_system'),
    },
    "weihenstephan-standards": {
        "tags": ['weihenstephan standards', 'weihenstephan machine data', 'beverage line monitoring', 'oee data acquisition'],
        "license": CC_BY_SA,
        "pages": wiki('Weihenstephan_Standards', 'Manufacturing_execution_system', 'Overall_equipment_effectiveness', 'Bottling_line', 'Programmable_logic_controller', 'Automation'),
    },
    "vehicle-to-grid": {
        "tags": ['vehicle-to-grid', 'v2g energy', 'ev grid integration', 'bidirectional ev charging'],
        "license": CC_BY_SA,
        "pages": wiki('Vehicle-to-grid', 'Electric_vehicle', 'Battery_electric_vehicle', 'Grid_energy_storage', 'Smart_grid', 'Charging_station'),
    },
    "home-energy-management": {
        "tags": ['home energy management', 'hems system', 'residential energy control', 'household energy monitoring'],
        "license": CC_BY_SA,
        "pages": wiki('Home_energy_monitor', 'Smart_meter', 'Demand_response', 'Home_automation', 'Distributed_generation', 'Energy_conservation'),
    },
    "building-management-system": {
        "tags": ['building management system', 'bms building control', 'facility energy management', 'integrated building control'],
        "license": CC_BY_SA,
        "pages": wiki('Building_management_system', 'Building_automation', 'HVAC_control_system', 'Direct_digital_control', 'Energy_management_system', 'Facility_management'),
    },
    "predictive-maintenance-iiot": {
        "tags": ['predictive maintenance', 'condition-based monitoring', 'iiot prognostics', 'equipment health monitoring'],
        "license": CC_BY_SA,
        "pages": wiki('Predictive_maintenance', 'Condition_monitoring', 'Industrial_internet_of_things', 'Prognostics', 'Vibration_analysis', 'Reliability_engineering'),
    },
}
