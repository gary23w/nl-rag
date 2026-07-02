"""More networking: automation, deterministic/TSN, wireless deep, and network security."""
from .common import CC_BY_SA, wiki

DOMAINS = {
    "network-automation": {"tags": ["network automation", "zero touch provisioning", "config management", "net devops"],
                           "license": CC_BY_SA,
                           "pages": wiki("Network_Automation", "Provisioning_(technology)", "Zero-touch_provisioning", "Configuration_management", "Ansible_(software)", "Software-defined_networking", "Network_management")},

    "netconf-yang": {"tags": ["netconf protocol", "yang modeling", "config datastore", "model-driven config"],
                     "license": CC_BY_SA,
                     "pages": wiki("NETCONF", "YANG", "Network_management", "Simple_Network_Management_Protocol", "Protocol_Buffers", "Representational_state_transfer")},

    "restconf": {"tags": ["restconf protocol", "rest network config", "http config api", "yang over http"],
                 "license": CC_BY_SA,
                 "pages": wiki("Representational_state_transfer", "NETCONF", "YANG", "Hypertext_Transfer_Protocol", "JSON", "Network_management")},

    "openconfig": {"tags": ["openconfig models", "vendor-neutral yang", "streaming telemetry", "declarative config"],
                   "license": CC_BY_SA,
                   "pages": wiki("YANG", "NETCONF", "GRPC", "Protocol_Buffers", "Model_checking", "Network_management")},

    "network-telemetry-streaming": {"tags": ["streaming telemetry", "push telemetry", "network monitoring", "flow export"],
                                    "license": CC_BY_SA,
                                    "pages": wiki("Telemetry", "NetFlow", "IP_Flow_Information_Export", "Simple_Network_Management_Protocol", "Protocol_Buffers", "Network_performance")},

    "gnmi-protocol": {"tags": ["gnmi protocol", "grpc network management", "grpc streaming", "protobuf encoding"],
                      "license": CC_BY_SA,
                      "pages": wiki("GRPC", "Protocol_Buffers", "YANG", "Telemetry", "Hypertext_Transfer_Protocol", "Remote_procedure_call")},

    "p4-programming": {"tags": ["p4 language", "programmable data plane", "packet forwarding pipeline", "match-action tables"],
                       "license": CC_BY_SA,
                       "pages": wiki("P4_(programming_language)", "Ternary_content-addressable_memory", "Forwarding_information_base", "Software-defined_networking", "Network_processor", "Packet_switching")},

    "network-verification": {"tags": ["network verification", "formal verification", "model checking", "reachability analysis"],
                             "license": CC_BY_SA,
                             "pages": wiki("Formal_verification", "Model_checking", "Reachability_problem", "Binary_decision_diagram", "Boolean_satisfiability_problem", "Forwarding_information_base")},

    "network-digital-twin": {"tags": ["network digital twin", "network simulation", "discrete event simulation", "what-if modeling"],
                             "license": CC_BY_SA,
                             "pages": wiki("Digital_twin", "Network_simulation", "Discrete-event_simulation", "Model_checking", "Network_performance", "Network_management")},

    "intent-based-networking": {"tags": ["intent-based networking", "autonomic networking", "closed-loop automation", "policy abstraction"],
                                "license": CC_BY_SA,
                                "pages": wiki("Intent-Based_Networking", "Autonomic_networking", "Autonomic_computing", "Software-defined_networking", "Network_management", "Network_Automation")},

    "sd-wan": {"tags": ["software-defined wan", "wan edge", "overlay transport", "application-aware routing"],
               "license": CC_BY_SA,
               "pages": wiki("SD-WAN", "Wide_area_network", "Overlay_network", "Software-defined_networking", "Quality_of_service", "Network_function_virtualization")},

    "sase-architecture": {"tags": ["secure access service edge", "sase model", "cloud-delivered security", "converged networking security"],
                          "license": CC_BY_SA,
                          "pages": wiki("Secure_access_service_edge", "SD-WAN", "Zero_trust_security_model", "Web_application_firewall", "Content-control_software", "Network_function_virtualization")},

    "zero-trust-network-access": {"tags": ["zero trust access", "zero trust model", "least privilege access", "identity-aware proxy"],
                                  "license": CC_BY_SA,
                                  "pages": wiki("Zero_trust_security_model", "BeyondCorp", "Principle_of_least_privilege", "Reverse_proxy", "Extensible_Authentication_Protocol", "Network_segmentation")},

    "microsegmentation-network": {"tags": ["network microsegmentation", "east-west isolation", "workload segmentation", "policy enforcement"],
                                  "license": CC_BY_SA,
                                  "pages": wiki("Network_segmentation", "Virtual_LAN", "Zero_trust_security_model", "Stateful_firewall", "Principle_of_least_privilege", "Software-defined_networking")},

    "network-access-control": {"tags": ["network access control", "endpoint admission", "posture assessment", "port-based authentication"],
                               "license": CC_BY_SA,
                               "pages": wiki("Network_Access_Control", "IEEE_802.1X", "Extensible_Authentication_Protocol", "RADIUS", "AAA_(computer_security)", "Media_access_control")},

    "802-1x-authentication": {"tags": ["802.1x authentication", "port-based access control", "supplicant authenticator", "eap over lan"],
                              "license": CC_BY_SA,
                              "pages": wiki("IEEE_802.1X", "Extensible_Authentication_Protocol", "RADIUS", "Network_Access_Control", "AAA_(computer_security)", "Wired_Equivalent_Privacy")},

    "radius-protocol": {"tags": ["radius protocol", "aaa authentication", "diameter protocol", "access accounting"],
                        "license": CC_BY_SA,
                        "pages": wiki("RADIUS", "Diameter_(protocol)", "AAA_(computer_security)", "Extensible_Authentication_Protocol", "IEEE_802.1X", "TACACS")},

    "tacacs-plus": {"tags": ["tacacs plus", "device administration aaa", "command authorization", "network device auth"],
                    "license": CC_BY_SA,
                    "pages": wiki("TACACS", "RADIUS", "AAA_(computer_security)", "Diameter_(protocol)", "Network_management", "Principle_of_least_privilege")},

    "network-firewall-deep": {"tags": ["stateful firewall", "connection tracking", "packet filtering", "application gateway"],
                              "license": CC_BY_SA,
                              "pages": wiki("Firewall_(computing)", "Stateful_firewall", "Application-level_gateway", "Unified_threat_management", "Proxy_ARP", "Network_segmentation")},

    "next-gen-firewall": {"tags": ["next-generation firewall", "application awareness", "unified threat management", "deep inspection"],
                          "license": CC_BY_SA,
                          "pages": wiki("Next-generation_firewall", "Unified_threat_management", "Web_application_firewall", "Intrusion_prevention_system", "Content-control_software", "Stateful_firewall")},

    "ids-ips-network": {"tags": ["intrusion detection", "intrusion prevention", "signature detection", "network sensors"],
                        "license": CC_BY_SA,
                        "pages": wiki("Intrusion_detection_system", "Intrusion_prevention_system", "Snort_(software)", "Suricata_(software)", "Zeek", "Deep_packet_inspection")},

    "network-detection-response": {"tags": ["network detection response", "endpoint detection response", "threat hunting", "security analytics"],
                                   "license": CC_BY_SA,
                                   "pages": wiki("Network_detection_and_response", "Endpoint_detection_and_response", "Security_information_and_event_management", "Intrusion_detection_system", "Zeek", "NetFlow")},

    "dns-security-extensions": {"tags": ["dnssec extensions", "dns authentication", "signed dns zones", "chain of trust"],
                                "license": CC_BY_SA,
                                "pages": wiki("Domain_Name_System_Security_Extensions", "DNS_spoofing", "DNS_over_HTTPS", "DNS_over_TLS", "Public-key_cryptography", "Domain_Name_System")},

    "dns-filtering": {"tags": ["dns filtering", "dns sinkhole", "content filtering", "protective dns"],
                      "license": CC_BY_SA,
                      "pages": wiki("DNS_sinkhole", "Content-control_software", "DNS_over_HTTPS", "DNS_over_TLS", "DNS_spoofing", "Domain_Name_System")},

    "dhcp-snooping": {"tags": ["dhcp snooping", "rogue dhcp defense", "trusted ports", "binding table"],
                      "license": CC_BY_SA,
                      "pages": wiki("DHCP_snooping", "Dynamic_Host_Configuration_Protocol", "Dynamic_ARP_Inspection", "IP_address_spoofing", "Media_access_control", "Virtual_LAN")},

    "arp-spoofing-defense": {"tags": ["arp spoofing defense", "dynamic arp inspection", "address resolution", "man-in-the-middle prevention"],
                             "license": CC_BY_SA,
                             "pages": wiki("ARP_spoofing", "Dynamic_ARP_Inspection", "Address_Resolution_Protocol", "IP_address_spoofing", "Proxy_ARP", "DHCP_snooping")},

    "mac-security": {"tags": ["macsec encryption", "layer 2 encryption", "link-layer security", "media access encryption"],
                     "license": CC_BY_SA,
                     "pages": wiki("MACsec", "IEEE_802.1AE", "Media_access_control", "IEEE_802.1X", "Data_center_bridging", "Extensible_Authentication_Protocol")},

    "port-security": {"tags": ["switch port security", "mac address limiting", "unauthorized access prevention", "sticky mac"],
                      "license": CC_BY_SA,
                      "pages": wiki("Port_security", "Media_access_control", "IEEE_802.1X", "Network_switch", "Network_Access_Control", "Virtual_LAN")},

    "storm-control": {"tags": ["storm control", "broadcast radiation", "broadcast storm", "traffic rate limiting"],
                      "license": CC_BY_SA,
                      "pages": wiki("Broadcast_radiation", "Broadcast_storm", "Traffic_policing_(communications)", "Rate_limiting", "Broadcast,_unknown-unicast_and_multicast_traffic", "Multicast")},

    "time-sensitive-networking": {"tags": ["time-sensitive networking", "bounded latency", "deterministic ethernet", "scheduled traffic"],
                                  "license": CC_BY_SA,
                                  "pages": wiki("Time-Sensitive_Networking", "IEEE_802.1", "Audio_Video_Bridging", "IEEE_802.1Q", "Stream_Reservation_Protocol", "Real-time_computing")},

    "ieee-802-1-tsn": {"tags": ["ieee 802.1 tsn", "stream reservation", "frame preemption", "credit-based shaper"],
                       "license": CC_BY_SA,
                       "pages": wiki("Stream_Reservation_Protocol", "Time-Sensitive_Networking", "IEEE_802.1", "IEEE_802.1Q", "Audio_Video_Bridging", "Data_center_bridging")},

    "audio-video-bridging": {"tags": ["audio video bridging", "avb streams", "media clock synchronization", "reserved bandwidth"],
                             "license": CC_BY_SA,
                             "pages": wiki("Audio_Video_Bridging", "Stream_Reservation_Protocol", "Time-Sensitive_Networking", "Precision_Time_Protocol", "IEEE_802.1", "Jitter")},

    "deterministic-networking": {"tags": ["deterministic networking", "guaranteed latency", "bounded jitter", "real-time delivery"],
                                 "license": CC_BY_SA,
                                 "pages": wiki("Deterministic_Networking", "Real-time_computing", "Jitter", "Time-Sensitive_Networking", "Quality_of_service", "Network_performance")},

    "precision-time-protocol-deep": {"tags": ["precision time protocol", "ieee 1588", "hardware timestamping", "clock synchronization"],
                                     "license": CC_BY_SA,
                                     "pages": wiki("Precision_Time_Protocol", "IEEE_1588", "Clock_synchronization", "Synchronous_Ethernet", "Primary_reference_clock", "Time_division_multiple_access")},

    "synchronous-ethernet": {"tags": ["synchronous ethernet", "syncE frequency", "physical layer clock", "reference clock distribution"],
                             "license": CC_BY_SA,
                             "pages": wiki("Synchronous_Ethernet", "Primary_reference_clock", "Clock_synchronization", "Precision_Time_Protocol", "Carrier_Ethernet", "Time_division_multiple_access")},

    "carrier-ethernet": {"tags": ["carrier ethernet", "provider backbone bridging", "ethernet services", "operator networks"],
                         "license": CC_BY_SA,
                         "pages": wiki("Carrier_Ethernet", "Provider_Backbone_Bridges", "Provider_Backbone_Bridge_Traffic_Engineering", "Ethernet_in_the_First_Mile", "Synchronous_Ethernet", "Quality_of_service")},

    "metro-ethernet": {"tags": ["metro ethernet", "metropolitan area network", "ethernet transport", "service provider ethernet"],
                       "license": CC_BY_SA,
                       "pages": wiki("Metro_Ethernet", "Carrier_Ethernet", "Provider_Backbone_Bridges", "Ethernet_in_the_First_Mile", "Wide_area_network", "Quality_of_service")},

    "gpon-deep": {"tags": ["gigabit pon", "passive optical network", "optical line termination", "fiber access"],
                  "license": CC_BY_SA,
                  "pages": wiki("Gigabit_Passive_Optical_Network", "Passive_optical_network", "10G-PON", "NG-PON2", "Optical_line_termination", "Optical_Network_Unit")},

    "docsis-cable": {"tags": ["docsis standard", "cable modem", "cable termination system", "hybrid fiber coax"],
                     "license": CC_BY_SA,
                     "pages": wiki("DOCSIS", "Cable_modem", "Cable_modem_termination_system", "Hybrid_fibre-coaxial", "Fiber_to_the_x", "Wide_area_network")},

    "wifi-7": {"tags": ["wi-fi 7", "802.11be standard", "multi-link operation", "extremely high throughput"],
               "license": CC_BY_SA,
               "pages": wiki("Wi-Fi_7", "IEEE_802.11be", "IEEE_802.11ax", "Wi-Fi", "Wireless_LAN", "Multi-user_MIMO")},

    "wifi-mesh": {"tags": ["wi-fi mesh", "wireless mesh network", "self-healing wireless", "multi-hop wireless"],
                  "license": CC_BY_SA,
                  "pages": wiki("Wireless_mesh_network", "IEEE_802.11s", "Mesh_networking", "Wi-Fi", "Mobile_ad_hoc_network", "Routing_protocol")},

    "cellular-6g": {"tags": ["6g networks", "terahertz communication", "sub-terahertz spectrum", "next-generation cellular"],
                    "license": CC_BY_SA,
                    "pages": wiki("6G_(network)", "Terahertz_radiation", "Cellular_network", "Free-space_optical_communication", "Network_slicing", "Beamforming")},

    "private-5g": {"tags": ["private 5g", "enterprise cellular", "industrial iot connectivity", "dedicated mobile network"],
                   "license": CC_BY_SA,
                   "pages": wiki("5G", "Industrial_internet_of_things", "Network_slicing", "Open_RAN", "Network_function_virtualization", "Cellular_network")},

    "open-ran": {"tags": ["open ran", "disaggregated radio", "ran interfaces", "virtualized base station"],
                 "license": CC_BY_SA,
                 "pages": wiki("Open_RAN", "Network_function_virtualization", "5G", "Network_slicing", "Software-defined_networking", "Cellular_network")},

    "network-slicing-5g": {"tags": ["5g network slicing", "logical network partition", "slice isolation", "service-level networking"],
                           "license": CC_BY_SA,
                           "pages": wiki("5G_network_slicing", "Network_slicing", "Network_function_virtualization", "Software-defined_networking", "Quality_of_service", "Open_RAN")},

    "satellite-constellation": {"tags": ["satellite constellation", "leo constellation", "communications satellite", "ground station"],
                                "license": CC_BY_SA,
                                "pages": wiki("Satellite_constellation", "Low_Earth_orbit", "Communications_satellite", "Ground_station", "Beamforming", "Free-space_optical_communication")},

    "starlink-networking": {"tags": ["starlink network", "low earth orbit internet", "satellite backhaul", "phased array terminal"],
                            "license": CC_BY_SA,
                            "pages": wiki("Starlink", "Satellite_constellation", "Low_Earth_orbit", "Ground_station", "Communications_satellite", "Beamforming")},

    "li-fi": {"tags": ["li-fi optical", "visible light communication", "free-space optics", "photonic data transfer"],
              "license": CC_BY_SA,
              "pages": wiki("Li-Fi", "Visible_light_communication", "Free-space_optical_communication", "Modulation", "Optical_communication", "Wireless")},

    "bluetooth-mesh": {"tags": ["bluetooth mesh", "bluetooth low energy", "managed flooding", "iot mesh network"],
                       "license": CC_BY_SA,
                       "pages": wiki("Bluetooth_mesh_networking", "Bluetooth_Low_Energy", "Mesh_networking", "Home_automation", "Wireless_mesh_network", "Low-power_electronics")},

    "thread-network-deep": {"tags": ["thread protocol", "6lowpan mesh", "low-power ipv6", "border router"],
                            "license": CC_BY_SA,
                            "pages": wiki("Thread_(network_protocol)", "6LoWPAN", "IEEE_802.15.4", "Mesh_networking", "Constrained_Application_Protocol", "Home_automation")},

    "zigbee-3": {"tags": ["zigbee 3", "802.15.4 radio", "low-rate wireless", "personal area network"],
                 "license": CC_BY_SA,
                 "pages": wiki("Zigbee", "IEEE_802.15.4", "6LoWPAN", "Mesh_networking", "Home_automation", "Wireless_sensor_network")},

    "matter-protocol-deep": {"tags": ["matter protocol", "connectivity standards alliance", "smart home interoperability", "thread ip transport"],
                             "license": CC_BY_SA,
                             "pages": wiki("Matter_(standard)", "Connectivity_Standards_Alliance", "Thread_(network_protocol)", "Home_automation", "Bluetooth_Low_Energy", "Internet_of_things")},

    "network-congestion-control": {"tags": ["congestion control", "tcp congestion avoidance", "congestion window", "flow throttling"],
                                   "license": CC_BY_SA,
                                   "pages": wiki("Network_congestion", "TCP_congestion_control", "Explicit_Congestion_Notification", "Bufferbloat", "Active_queue_management", "Network_performance")},

    "active-queue-management": {"tags": ["active queue management", "random early detection", "controlled delay", "weighted fair queueing"],
                                "license": CC_BY_SA,
                                "pages": wiki("Active_queue_management", "Random_early_detection", "CoDel", "Weighted_fair_queueing", "Bufferbloat", "Network_congestion")},

    "ecn-networking": {"tags": ["explicit congestion notification", "ecn marking", "congestion signaling", "packet marking"],
                       "license": CC_BY_SA,
                       "pages": wiki("Explicit_Congestion_Notification", "TCP_congestion_control", "Network_congestion", "Active_queue_management", "Data_center_bridging", "Quality_of_service")},

    "load-balancing-l4-l7": {"tags": ["layer 4 load balancing", "layer 7 load balancing", "reverse proxy", "consistent hashing"],
                             "license": CC_BY_SA,
                             "pages": wiki("Load_balancing_(computing)", "Reverse_proxy", "Application_delivery_controller", "Consistent_hashing", "Round-robin_DNS", "Quality_of_service")},
}
