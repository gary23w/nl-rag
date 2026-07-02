"""Embedded RTOS variants, automotive buses, and functional-safety standards."""
from .common import CC_BY_SA, wiki

DOMAINS = {
    "misra-c": {
        "tags": ["misra c", "safety-critical coding", "automotive c guidelines", "cert c standard"],
        "license": CC_BY_SA,
        "pages": wiki("MISRA_C", "Coding_conventions", "Static_program_analysis",
                      "Safety-critical_system", "Defensive_programming",
                      "CERT_C_Coding_Standard", "Software_bug")},
    "threadx-rtos": {
        "tags": ["threadx rtos", "azure rtos", "preemptive scheduler", "priority inheritance"],
        "license": CC_BY_SA,
        "pages": wiki("ThreadX", "Real-time_operating_system", "Preemption_(computing)",
                      "Priority_inheritance", "Microcontroller", "Microsoft")},
    "zephyr-rtos": {
        "tags": ["zephyr rtos", "zephyr project", "device tree", "kconfig build"],
        "license": CC_BY_SA,
        "pages": wiki("Zephyr_(operating_system)", "Linux_Foundation", "Device_tree",
                      "Kconfig", "Embedded_system", "ARM_Cortex-M")},
    "riot-os": {
        "tags": ["riot os", "riot the friendly", "6lowpan stack", "constrained node"],
        "license": CC_BY_SA,
        "pages": wiki("RIOT_(operating_system)", "6LoWPAN", "Constrained_Application_Protocol",
                      "Internet_of_things", "Wireless_sensor_network", "Cortex-M")},
    "contiki-os": {
        "tags": ["contiki os", "contiki ng", "protothread model", "micro ip stack"],
        "license": CC_BY_SA,
        "pages": wiki("Contiki", "Adam_Dunkels", "UIP_(micro_IP)", "LwIP",
                      "Protothread", "Wireless_sensor_network")},
    "mbed-os": {
        "tags": ["mbed os", "arm mbed", "cortex-m platform", "cmsis abstraction"],
        "license": CC_BY_SA,
        "pages": wiki("Mbed", "Arm_Holdings", "ARM_Cortex-M", "Firmware",
                      "Microcontroller", "Embedded_software")},
    "nuttx-rtos": {
        "tags": ["nuttx rtos", "apache nuttx", "posix embedded", "px4 flight stack"],
        "license": CC_BY_SA,
        "pages": wiki("NuttX", "POSIX", "Apache_Software_Foundation", "Unix-like",
                      "PX4_autopilot", "Real-time_computing")},
    "ti-rtos": {
        "tags": ["ti-rtos kernel", "sysbios scheduler", "msp430 mcu", "code composer studio"],
        "license": CC_BY_SA,
        "pages": wiki("Texas_Instruments", "MSP430", "Code_Composer_Studio",
                      "Digital_signal_processor", "Microcontroller", "Real-time_operating_system")},
    "embos": {
        "tags": ["embos rtos", "segger embos", "j-link debugger", "stm32 target"],
        "license": CC_BY_SA,
        "pages": wiki("Segger_Microcontroller_Systems", "STM32", "Cortex-M",
                      "Task_(computing)", "Embedded_system", "Firmware")},
    "chibios": {
        "tags": ["chibios rt", "chibios hal", "real-time kernel", "stm32 board"],
        "license": CC_BY_SA,
        "pages": wiki("ChibiOS/RT", "STM32", "Real-time_operating_system",
                      "Board_support_package", "Microcontroller", "Embedded_software")},
    "rt-thread": {
        "tags": ["rt-thread rtos", "rt-thread iot", "finsh shell", "device driver framework"],
        "license": CC_BY_SA,
        "pages": wiki("RT-Thread", "Internet_of_Things", "Real-time_operating_system",
                      "Microcontroller", "Task_(computing)", "Firmware")},
    "vxworks-deep": {
        "tags": ["vxworks rtos", "wind river vxworks", "mars rover software", "hard real-time kernel"],
        "license": CC_BY_SA,
        "pages": wiki("VxWorks", "Wind_River_Systems", "Mars_rover",
                      "Board_support_package", "Real-time_computing", "Embedded_system")},
    "qnx-rtos": {
        "tags": ["qnx neutrino", "qnx microkernel", "message-passing os", "automotive infotainment"],
        "license": CC_BY_SA,
        "pages": wiki("QNX", "Microkernel", "BlackBerry_Limited", "Message_passing",
                      "In-vehicle_infotainment", "Real-time_operating_system")},
    "integrity-rtos": {
        "tags": ["integrity rtos", "green hills integrity", "separation kernel", "common criteria eal"],
        "license": CC_BY_SA,
        "pages": wiki("Integrity_(operating_system)", "Green_Hills_Software", "Separation_kernel",
                      "Common_Criteria", "Avionics", "Real-time_operating_system")},
    "sel4-microkernel": {
        "tags": ["sel4 microkernel", "formally verified kernel", "capability-based security", "isabelle proof"],
        "license": CC_BY_SA,
        "pages": wiki("SeL4", "L4_microkernel_family", "Formal_verification",
                      "Capability-based_security", "Isabelle_(proof_assistant)", "Trusted_computing_base")},
    "real-time-linux-preempt": {
        "tags": ["preempt rt patch", "real-time linux", "kernel preemption", "interrupt latency bound"],
        "license": CC_BY_SA,
        "pages": wiki("PREEMPT_RT", "Linux_kernel", "Real-time_computing",
                      "Scheduling_(computing)", "Interrupt_latency", "Preemption_(computing)")},
    "xenomai": {
        "tags": ["xenomai cobalt", "dual-kernel real-time", "adeos pipeline", "rtai co-kernel"],
        "license": CC_BY_SA,
        "pages": wiki("Xenomai", "Adeos", "RTAI", "Real-time_computing",
                      "Kernel_(operating_system)", "Interrupt_latency")},
    "u-boot-bootloader": {
        "tags": ["das u-boot", "u-boot loader", "embedded boot stage", "board bring-up"],
        "license": CC_BY_SA,
        "pages": wiki("Das_U-Boot", "Booting", "Bootloader", "Firmware",
                      "Embedded_system", "Board_support_package")},
    "barebox": {
        "tags": ["barebox bootloader", "second-stage loader", "device tree boot", "u-boot alternative"],
        "license": CC_BY_SA,
        "pages": wiki("Barebox", "Bootloader", "Das_U-Boot", "Device_tree",
                      "Booting", "Embedded_software")},
    "tianocore-edk": {
        "tags": ["tianocore edk2", "uefi firmware", "edk2 build", "platform initialization"],
        "license": CC_BY_SA,
        "pages": wiki("TianoCore", "UEFI", "Unified_Extensible_Firmware_Interface",
                      "BIOS", "Boot_ROM", "Firmware")},
    "can-fd-bus": {
        "tags": ["can fd", "flexible data-rate", "controller area network", "bit stuffing frame"],
        "license": CC_BY_SA,
        "pages": wiki("CAN_FD", "CAN_bus", "Bit_stuffing", "Automotive_electronics",
                      "Electronic_control_unit", "Serial_communication")},
    "lin-bus": {
        "tags": ["lin bus", "local interconnect network", "lin master node", "automotive sub-bus"],
        "license": CC_BY_SA,
        "pages": wiki("Local_Interconnect_Network", "Serial_communication", "Master/slave_(technology)",
                      "Automotive_electronics", "Electronic_control_unit", "CAN_bus")},
    "flexray": {
        "tags": ["flexray bus", "time-triggered protocol", "flexray cluster", "x-by-wire network"],
        "license": CC_BY_SA,
        "pages": wiki("FlexRay", "Time-triggered_architecture", "Time-division_multiple_access",
                      "Drive_by_wire", "Automotive_electronics", "Electronic_control_unit")},
    "automotive-ethernet": {
        "tags": ["automotive ethernet", "audio video bridging", "time-sensitive networking", "in-car backbone"],
        "license": CC_BY_SA,
        "pages": wiki("Automotive_Ethernet", "Audio_Video_Bridging", "Time-Sensitive_Networking",
                      "Ethernet", "Physical_layer", "In-vehicle_infotainment")},
    "some-ip": {
        "tags": ["some/ip middleware", "service-oriented middleware", "automotive rpc", "publish-subscribe vehicle"],
        "license": CC_BY_SA,
        "pages": wiki("Service-oriented_architecture", "Middleware", "Remote_procedure_call",
                      "Publish%E2%80%93subscribe_pattern", "Automotive_Ethernet", "AUTOSAR")},
    "doip-diagnostics": {
        "tags": ["diagnostics over ip", "doip protocol", "vehicle ecu diagnostics", "iso 13400 transport"],
        "license": CC_BY_SA,
        "pages": wiki("Vehicle_diagnostics", "Unified_Diagnostic_Services", "On-board_diagnostics",
                      "Electronic_control_unit", "Automotive_Ethernet", "Ethernet")},
    "uds-diagnostics": {
        "tags": ["unified diagnostic services", "uds protocol", "iso 14229 services", "iso-tp transport"],
        "license": CC_BY_SA,
        "pages": wiki("Unified_Diagnostic_Services", "ISO_15765-2", "Vehicle_diagnostics",
                      "Electronic_control_unit", "CAN_bus", "On-board_diagnostics")},
    "obd-ii": {
        "tags": ["obd-ii port", "on-board diagnostics", "obd pid codes", "emissions readiness"],
        "license": CC_BY_SA,
        "pages": wiki("On-board_diagnostics", "OBD-II_PIDs", "Vehicle_diagnostics",
                      "Electronic_control_unit", "Automotive_electronics", "CAN_bus")},
    "j1939": {
        "tags": ["sae j1939", "j1939 protocol", "heavy-duty vehicle bus", "commercial truck network"],
        "license": CC_BY_SA,
        "pages": wiki("SAE_J1939", "CAN_bus", "Commercial_vehicle", "Truck",
                      "Society_of_Automotive_Engineers", "Electronic_control_unit")},
    "autosar-classic": {
        "tags": ["autosar classic", "autosar rte", "basic software layer", "automotive software architecture"],
        "license": CC_BY_SA,
        "pages": wiki("AUTOSAR", "Software_architecture", "Electronic_control_unit",
                      "Embedded_software", "Middleware", "Automotive_electronics")},
    "autosar-adaptive": {
        "tags": ["autosar adaptive", "adaptive platform", "posix automotive", "service-oriented vehicle"],
        "license": CC_BY_SA,
        "pages": wiki("AUTOSAR", "POSIX", "POSIX_Threads", "Service-oriented_architecture",
                      "Automotive_Ethernet", "Middleware")},
    "do-178c": {
        "tags": ["do-178c", "airborne software", "dal assurance level", "avionics certification"],
        "license": CC_BY_SA,
        "pages": wiki("DO-178C", "DO-178B", "Avionics_software", "Avionics",
                      "Software_verification", "Safety-critical_system")},
    "do-254": {
        "tags": ["do-254", "airborne hardware", "complex electronic hardware", "fpga assurance"],
        "license": CC_BY_SA,
        "pages": wiki("DO-254", "Field-programmable_gate_array", "Application-specific_integrated_circuit",
                      "Hardware_verification", "Avionics", "Reliability_engineering")},
    "iec-61508": {
        "tags": ["iec 61508", "functional safety standard", "safety instrumented system", "e/e/pe systems"],
        "license": CC_BY_SA,
        "pages": wiki("IEC_61508", "Functional_safety", "Safety_instrumented_system",
                      "Safety_integrity_level", "Reliability_engineering", "Hazard_analysis")},
    "iec-62304-medical": {
        "tags": ["iec 62304", "medical device software", "software lifecycle process", "iso 13485 quality"],
        "license": CC_BY_SA,
        "pages": wiki("IEC_62304", "Medical_device", "Software_development_process",
                      "ISO_13485", "Software_safety", "Safety-critical_system")},
    "en-50128-railway": {
        "tags": ["en 50128", "railway software safety", "cenelec railway standard", "signalling software"],
        "license": CC_BY_SA,
        "pages": wiki("Railway_signalling", "Automatic_train_protection", "CENELEC",
                      "Communications-based_train_control", "Software_safety", "Safety_integrity_level")},
    "arinc-653": {
        "tags": ["arinc 653", "integrated modular avionics", "time and space partitioning", "apex interface"],
        "license": CC_BY_SA,
        "pages": wiki("ARINC_653", "Integrated_modular_avionics", "ARINC",
                      "Avionics_software", "Separation_kernel", "Real-time_operating_system")},
    "functional-safety-concepts": {
        "tags": ["functional safety", "hazard analysis", "fail-safe design", "redundancy engineering"],
        "license": CC_BY_SA,
        "pages": wiki("Functional_safety", "Hazard_analysis", "Fail-safe",
                      "Redundancy_(engineering)", "Fault_tolerance", "Reliability_engineering")},
    "fault-tree-analysis": {
        "tags": ["fault tree analysis", "top event logic", "event tree analysis", "reliability block diagram"],
        "license": CC_BY_SA,
        "pages": wiki("Fault_tree_analysis", "Event_tree_analysis", "Reliability_block_diagram",
                      "Single_point_of_failure", "Root_cause_analysis", "Hazard_and_operability_study")},
    "failure-mode-effects-analysis": {
        "tags": ["failure mode and effects analysis", "fmea worksheet", "risk priority number", "criticality analysis"],
        "license": CC_BY_SA,
        "pages": wiki("Failure_mode_and_effects_analysis", "FMEA", "Failure_mode",
                      "Risk_priority_number", "Root_cause_analysis", "Reliability_engineering")},
    "safety-integrity-level": {
        "tags": ["safety integrity level", "automotive safety integrity level", "iso 26262 asil", "sil target"],
        "license": CC_BY_SA,
        "pages": wiki("Safety_integrity_level", "Automotive_Safety_Integrity_Level", "ISO_26262",
                      "Software_safety", "Functional_safety", "Reliability_engineering")},
    "watchdog-timer-design": {
        "tags": ["watchdog timer", "hardware watchdog", "system reset supervisor", "fail-safe recovery"],
        "license": CC_BY_SA,
        "pages": wiki("Watchdog_timer", "Fail-safe", "Fault_tolerance",
                      "Microcontroller", "Embedded_system", "Reliability_engineering")},
    "memory-protection-unit": {
        "tags": ["memory protection unit", "mpu region", "memory management unit", "protection ring"],
        "license": CC_BY_SA,
        "pages": wiki("Memory_protection_unit", "Memory_protection", "Memory_management_unit",
                      "Protection_ring", "Memory_segmentation", "ARM_Cortex-M")},
    "lockstep-cores": {
        "tags": ["lockstep cores", "dual-core lockstep", "triple modular redundancy", "dual modular redundancy"],
        "license": CC_BY_SA,
        "pages": wiki("Lockstep_(computing)", "Triple_modular_redundancy", "Dual_modular_redundancy",
                      "Redundancy_(engineering)", "Fault_tolerance", "Reliability_engineering")},
    "ecc-memory-embedded": {
        "tags": ["ecc memory", "single event upset", "hamming code correction", "soft error mitigation"],
        "license": CC_BY_SA,
        "pages": wiki("ECC_memory", "Error_correction_code", "Hamming_code",
                      "Parity_bit", "Soft_error", "Single_event_upset")},
    "bootloader-security": {
        "tags": ["secure boot", "chain of trust", "code signing", "trusted execution environment"],
        "license": CC_BY_SA,
        "pages": wiki("Secure_boot", "Chain_of_trust", "Code_signing",
                      "Trusted_execution_environment", "ARM_TrustZone", "Boot_ROM")},
    "secure-firmware-update": {
        "tags": ["secure firmware update", "signed firmware image", "hardware security module", "trusted platform module"],
        "license": CC_BY_SA,
        "pages": wiki("Code_signing", "Hardware_security_module", "Trusted_Platform_Module",
                      "Chain_of_trust", "Patch_(computing)", "Firmware")},
    "over-the-air-updates": {
        "tags": ["over-the-air update", "firmware over-the-air", "a/b partition rollback", "ota campaign"],
        "license": CC_BY_SA,
        "pages": wiki("Over-the-air_update", "Firmware_over-the-air", "Patch_(computing)",
                      "Rollback_(data_management)", "A/B_testing", "Embedded_software")},
    "hardware-in-the-loop": {
        "tags": ["hardware-in-the-loop simulation", "hil test rig", "system under test", "real-time plant model"],
        "license": CC_BY_SA,
        "pages": wiki("Hardware-in-the-loop_simulation", "Simulation", "System_under_test",
                      "Software_testing", "Real-time_computing", "Embedded_system")},
    "model-based-design": {
        "tags": ["model-based design", "model-based systems engineering", "systems modeling", "plant model"],
        "license": CC_BY_SA,
        "pages": wiki("Model-based_design", "Model-based_systems_engineering", "Systems_modeling",
                      "Simulation", "Embedded_software", "Automatic_programming")},
    "simulink-embedded": {
        "tags": ["simulink model", "matlab simulink", "dataflow block diagram", "embedded coder"],
        "license": CC_BY_SA,
        "pages": wiki("Simulink", "MATLAB", "Dataflow_programming",
                      "Model-based_design", "Automatic_programming", "Embedded_software")},
    "code-generation-embedded": {
        "tags": ["embedded code generation", "automatic programming", "autocode toolchain", "model to c"],
        "license": CC_BY_SA,
        "pages": wiki("Automatic_programming", "Model-based_design", "Dataflow_programming",
                      "Static_program_analysis", "Firmware", "Embedded_system")},
}
