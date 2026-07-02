"""Deep network engineering: routing, switching, wireless, datacenter, optical, performance."""
from .common import CC_BY_SA, wiki

DOMAINS = {
    "vxlan-overlay": {"tags": ["vxlan overlay", "network overlay", "layer 2 tunneling", "network virtualization"],
                      "license": CC_BY_SA,
                      "pages": wiki("Virtual_Extensible_LAN", "Overlay_network", "Network_virtualization", "Tunneling_protocol", "Encapsulation_(networking)", "Software-defined_networking")},

    "geneve-encapsulation": {"tags": ["geneve encapsulation", "generic encapsulation", "tunnel headers", "overlay transport"],
                             "license": CC_BY_SA,
                             "pages": wiki("Generic_Network_Virtualization_Encapsulation", "Generic_Routing_Encapsulation", "Network_Virtualization_using_Generic_Routing_Encapsulation", "Tunneling_protocol", "Encapsulation_(networking)", "Overlay_network")},

    "network-overlays": {"tags": ["network overlay", "overlay tunneling", "virtual networks", "data center fabric"],
                         "license": CC_BY_SA,
                         "pages": wiki("Overlay_network", "Network_virtualization", "Virtual_Extensible_LAN", "Software-defined_networking", "Data_center_network_architectures", "Tunneling_protocol")},

    "evpn": {"tags": ["ethernet vpn", "layer 2 vpn", "provider backbone", "mac learning"],
             "license": CC_BY_SA,
             "pages": wiki("Ethernet_VPN", "Virtual_private_network", "MPLS_VPN", "Provider_Backbone_Bridges", "Multiprotocol_BGP", "Virtual_Extensible_LAN")},

    "is-is-routing": {"tags": ["is-is protocol", "link-state routing", "interior gateway protocol", "network convergence"],
                      "license": CC_BY_SA,
                      "pages": wiki("IS-IS", "Interior_gateway_protocol", "Link-state_routing_protocol", "Routing_protocol", "Convergence_(routing)", "Open_Shortest_Path_First")},

    "eigrp": {"tags": ["eigrp protocol", "distance-vector routing", "interior gateway protocol", "route metric"],
              "license": CC_BY_SA,
              "pages": wiki("Enhanced_Interior_Gateway_Routing_Protocol", "Interior_Gateway_Routing_Protocol", "Distance-vector_routing_protocol", "Routing_protocol", "Administrative_distance", "Routing_table")},

    "rip-routing": {"tags": ["routing information protocol", "distance-vector routing", "hop count", "split horizon"],
                    "license": CC_BY_SA,
                    "pages": wiki("Routing_Information_Protocol", "Distance-vector_routing_protocol", "Hop_(networking)", "Split_horizon_route_advertisement", "Interior_gateway_protocol", "Routing_protocol")},

    "route-reflectors": {"tags": ["route reflector", "bgp scaling", "internal bgp", "autonomous system"],
                         "license": CC_BY_SA,
                         "pages": wiki("Route_reflector", "Border_Gateway_Protocol", "Autonomous_system_(Internet)", "BGP_confederation", "Multiprotocol_BGP", "Convergence_(routing)")},

    "bgp-communities": {"tags": ["bgp communities", "bgp policy", "path attributes", "route tagging"],
                        "license": CC_BY_SA,
                        "pages": wiki("Multiprotocol_BGP", "Border_Gateway_Protocol", "BGP_confederation", "Route_reflector", "Autonomous_system_(Internet)", "BGP_hijacking")},

    "segment-routing": {"tags": ["segment routing", "source routing", "srv6 dataplane", "traffic steering"],
                        "license": CC_BY_SA,
                        "pages": wiki("Segment_routing", "SRv6", "Multiprotocol_Label_Switching", "IP_routing", "Label_switching", "Forwarding_information_base")},

    "traffic-engineering-mpls": {"tags": ["mpls traffic engineering", "label distribution", "resource reservation", "path signaling"],
                                 "license": CC_BY_SA,
                                 "pages": wiki("Teletraffic_engineering", "RSVP-TE", "Multiprotocol_Label_Switching", "Label_Distribution_Protocol", "Resource_Reservation_Protocol", "Traffic_engineering")},

    "qos-networking": {"tags": ["quality of service", "class of service", "differentiated services", "integrated services"],
                       "license": CC_BY_SA,
                       "pages": wiki("Quality_of_service", "Class_of_service", "Differentiated_services", "Integrated_services", "Type_of_service", "Per-hop_behavior")},

    "diffserv": {"tags": ["differentiated services", "per-hop behavior", "traffic classification", "explicit congestion notification"],
                 "license": CC_BY_SA,
                 "pages": wiki("Differentiated_services", "Per-hop_behavior", "Type_of_service", "Explicit_Congestion_Notification", "Quality_of_service", "Class_of_service")},

    "traffic-shaping": {"tags": ["traffic shaping", "token bucket", "leaky bucket", "traffic policing"],
                        "license": CC_BY_SA,
                        "pages": wiki("Traffic_shaping", "Token_bucket", "Leaky_bucket", "Traffic_policing_(communications)", "Network_traffic_control", "Committed_information_rate")},

    "spanning-tree-protocol": {"tags": ["spanning tree protocol", "loop prevention", "network bridging", "broadcast domain"],
                               "license": CC_BY_SA,
                               "pages": wiki("Spanning_Tree_Protocol", "Rapid_Spanning_Tree_Protocol", "Multiple_Spanning_Tree_Protocol", "Bridging_(networking)", "Broadcast_domain", "IEEE_802.1aq")},

    "link-aggregation": {"tags": ["link aggregation", "port channel", "etherchannel bonding", "network bonding"],
                         "license": CC_BY_SA,
                         "pages": wiki("Link_aggregation", "Link_Aggregation_Control_Protocol", "EtherChannel", "Ethernet_flow_control", "Network_switch", "Frame_(networking)")},

    "network-switching": {"tags": ["network switching", "packet switching", "cut-through switching", "collision domain"],
                          "license": CC_BY_SA,
                          "pages": wiki("Network_switch", "Packet_switching", "Cut-through_switching", "Store_and_forward", "Collision_domain", "Frame_(networking)")},

    "layer3-switching": {"tags": ["layer 3 switching", "multilayer switch", "vlan routing", "ip forwarding"],
                         "license": CC_BY_SA,
                         "pages": wiki("Multilayer_switch", "Router_(computing)", "VLAN", "IEEE_802.1Q", "IP_routing", "Routing_table")},

    "first-hop-redundancy": {"tags": ["first hop redundancy", "gateway redundancy", "virtual router", "hot standby"],
                             "license": CC_BY_SA,
                             "pages": wiki("First_hop_redundancy_protocols", "Hot_Standby_Router_Protocol", "Virtual_Router_Redundancy_Protocol", "Common_Address_Redundancy_Protocol", "Gateway_Load_Balancing_Protocol", "Proxy_ARP")},

    "network-address-translation": {"tags": ["network address translation", "port translation", "address rewriting", "private addressing"],
                                    "license": CC_BY_SA,
                                    "pages": wiki("Network_address_translation", "Port_address_translation", "Application-level_gateway", "IPv4", "Carrier-grade_NAT", "Proxy_ARP")},

    "carrier-grade-nat": {"tags": ["carrier-grade nat", "large scale nat", "address sharing", "ipv4 exhaustion"],
                          "license": CC_BY_SA,
                          "pages": wiki("Carrier-grade_NAT", "Network_address_translation", "Port_address_translation", "IPv4", "Application-level_gateway", "Virtual_private_network")},

    "stateful-firewall": {"tags": ["stateful firewall", "connection tracking", "next-generation firewall", "packet filtering"],
                          "license": CC_BY_SA,
                          "pages": wiki("Stateful_firewall", "Firewall_(computing)", "Next-generation_firewall", "Application-level_gateway", "Deep_packet_inspection", "Content-control_software")},

    "deep-packet-inspection": {"tags": ["deep packet inspection", "packet analysis", "content inspection", "traffic classification"],
                               "license": CC_BY_SA,
                               "pages": wiki("Deep_packet_inspection", "Firewall_(computing)", "Next-generation_firewall", "Content-control_software", "Network_traffic_control", "Stateful_firewall")},

    "load-balancer-algorithms": {"tags": ["load balancing", "weighted round robin", "consistent hashing", "health check"],
                                 "license": CC_BY_SA,
                                 "pages": wiki("Load_balancing_(computing)", "Weighted_round_robin", "Consistent_hashing", "Round-robin_DNS", "Content_delivery_network", "Network_switch")},

    "anycast-routing": {"tags": ["anycast routing", "anycast addressing", "content delivery", "route selection"],
                        "license": CC_BY_SA,
                        "pages": wiki("Anycast", "Border_Gateway_Protocol", "Content_delivery_network", "Round-robin_DNS", "IP_routing", "Routing_table")},

    "ecmp-routing": {"tags": ["equal-cost multipath", "load sharing", "path hashing", "flow distribution"],
                     "license": CC_BY_SA,
                     "pages": wiki("Equal-cost_multi-path_routing", "IP_routing", "Consistent_hashing", "Forwarding_information_base", "Routing_table", "Load_balancing_(computing)")},

    "datacenter-fabric": {"tags": ["data center fabric", "network fabric", "fat tree topology", "network architecture"],
                          "license": CC_BY_SA,
                          "pages": wiki("Data_center_network_architectures", "Fat_tree", "Data_center", "Network_topology", "Network_architecture", "Three-tier_architecture")},

    "clos-network": {"tags": ["clos network", "non-blocking fabric", "multistage switching", "fat tree"],
                     "license": CC_BY_SA,
                     "pages": wiki("Clos_network", "Fat_tree", "Network_topology", "Data_center_network_architectures", "Packet_switching", "Network_switch")},

    "leaf-spine": {"tags": ["leaf spine architecture", "data center topology", "two-tier fabric", "network scaling"],
                   "license": CC_BY_SA,
                   "pages": wiki("Data_center_network_architectures", "Clos_network", "Fat_tree", "Three-tier_architecture", "Network_topology", "Data_center")},

    "rdma-networking": {"tags": ["remote direct memory access", "zero-copy transfer", "kernel bypass", "low latency networking"],
                        "license": CC_BY_SA,
                        "pages": wiki("Remote_direct_memory_access", "RDMA_over_Converged_Ethernet", "InfiniBand", "Data_center_bridging", "Ethernet_flow_control", "Network_performance")},

    "infiniband": {"tags": ["infiniband fabric", "high performance interconnect", "hpc networking", "channel adapter"],
                   "license": CC_BY_SA,
                   "pages": wiki("InfiniBand", "Remote_direct_memory_access", "Fibre_Channel", "Data_center", "Network_switch", "Fibre_Channel_over_Ethernet")},

    "roce": {"tags": ["rdma over converged ethernet", "lossless ethernet", "priority flow control", "data center bridging"],
             "license": CC_BY_SA,
             "pages": wiki("RDMA_over_Converged_Ethernet", "Remote_direct_memory_access", "Data_center_bridging", "Ethernet_flow_control", "InfiniBand", "Converged_network_adapter")},

    "dpdk-networking": {"tags": ["data plane development kit", "kernel bypass", "packet processing", "network processor"],
                        "license": CC_BY_SA,
                        "pages": wiki("Data_Plane_Development_Kit", "Network_processor", "Single-root_input/output_virtualization", "SmartNIC", "Network_performance", "Packet_switching")},

    "smartnic": {"tags": ["smart network adapter", "network offload", "programmable nic", "io virtualization"],
                 "license": CC_BY_SA,
                 "pages": wiki("SmartNIC", "Network_processor", "Single-root_input/output_virtualization", "Data_Plane_Development_Kit", "Converged_network_adapter", "Software-defined_networking")},

    "network-telemetry": {"tags": ["network telemetry", "flow monitoring", "network management", "streaming metrics"],
                          "license": CC_BY_SA,
                          "pages": wiki("Telemetry", "Network_management", "Simple_Network_Management_Protocol", "NetFlow", "IP_Flow_Information_Export", "Network_performance")},

    "netflow-sflow": {"tags": ["netflow accounting", "flow export", "traffic monitoring", "flow information export"],
                      "license": CC_BY_SA,
                      "pages": wiki("NetFlow", "IP_Flow_Information_Export", "Network_traffic_control", "Telemetry", "Network_management", "Deep_packet_inspection")},

    "wifi-6": {"tags": ["wi-fi 6", "802.11ax standard", "wireless lan", "ofdma channel access"],
               "license": CC_BY_SA,
               "pages": wiki("Wi-Fi_6", "IEEE_802.11ax", "IEEE_802.11", "Wireless_LAN", "IEEE_802.11ac", "Wi-Fi")},

    "wifi-security-wpa": {"tags": ["wi-fi protected access", "wireless security", "wlan authentication", "802.1x port authentication"],
                          "license": CC_BY_SA,
                          "pages": wiki("Wi-Fi_Protected_Access", "IEEE_802.11i-2004", "Wireless_security", "Wired_Equivalent_Privacy", "Extensible_Authentication_Protocol", "IEEE_802.1X")},

    "cellular-4g-lte": {"tags": ["4g lte", "long term evolution", "system architecture evolution", "mobile broadband"],
                        "license": CC_BY_SA,
                        "pages": wiki("LTE_(telecommunication)", "System_Architecture_Evolution", "Radio_access_network", "MIMO", "Beamforming", "Multi-user_MIMO")},

    "cellular-5g-nr": {"tags": ["5g new radio", "5g networking", "millimeter wave", "massive mimo"],
                       "license": CC_BY_SA,
                       "pages": wiki("5G_NR", "5G", "Radio_access_network", "Network_slicing", "MIMO", "Beamforming")},

    "radio-access-network": {"tags": ["radio access network", "cloud ran", "base station", "mobile backhaul"],
                             "license": CC_BY_SA,
                             "pages": wiki("Radio_access_network", "C-RAN", "5G_NR", "LTE_(telecommunication)", "Beamforming", "Multi-user_MIMO")},

    "network-slicing": {"tags": ["network slicing", "5g slicing", "virtual network partition", "software-defined networking"],
                        "license": CC_BY_SA,
                        "pages": wiki("Network_slicing", "5G_NR", "Software-defined_networking", "Network_virtualization", "Radio_access_network", "Quality_of_service")},

    "optical-networking": {"tags": ["optical networking", "optical communication", "optical transport", "optical amplifier"],
                           "license": CC_BY_SA,
                           "pages": wiki("Optical_communication", "Optical_fiber", "Optical_transport_network", "Optical_amplifier", "Wavelength-division_multiplexing", "Optical_add-drop_multiplexer")},

    "dwdm": {"tags": ["dense wavelength multiplexing", "wavelength division multiplexing", "optical add-drop", "reconfigurable optical"],
             "license": CC_BY_SA,
             "pages": wiki("Dense_wavelength_division_multiplexing", "Wavelength-division_multiplexing", "Optical_add-drop_multiplexer", "Reconfigurable_optical_add-drop_multiplexer", "Optical_amplifier", "Optical_transport_network")},

    "sonet-sdh": {"tags": ["synchronous optical networking", "synchronous digital hierarchy", "optical transport", "time division multiplexing"],
                  "license": CC_BY_SA,
                  "pages": wiki("Synchronous_optical_networking", "Synchronous_Digital_Hierarchy", "Optical_transport_network", "Optical_communication", "Synchronous_Ethernet", "Optical_fiber")},

    "passive-optical-network": {"tags": ["passive optical network", "fiber to the home", "gigabit pon", "optical distribution"],
                                "license": CC_BY_SA,
                                "pages": wiki("Passive_optical_network", "Gigabit_Passive_Optical_Network", "10G-PON", "Optical_fiber", "Optical_communication", "Wavelength-division_multiplexing")},

    "satellite-networking": {"tags": ["satellite internet", "communications satellite", "satellite constellation", "satellite backhaul"],
                             "license": CC_BY_SA,
                             "pages": wiki("Satellite_Internet_access", "Communications_satellite", "Satellite_constellation", "Low_Earth_orbit", "Network_performance", "Beamforming")},

    "low-earth-orbit": {"tags": ["low earth orbit", "leo constellation", "satellite mesh", "orbital networking"],
                        "license": CC_BY_SA,
                        "pages": wiki("Low_Earth_orbit", "Satellite_constellation", "Satellite_Internet_access", "Communications_satellite", "Mesh_networking", "Beamforming")},

    "mesh-networking": {"tags": ["mesh networking", "wireless mesh network", "self-healing topology", "multi-hop routing"],
                        "license": CC_BY_SA,
                        "pages": wiki("Mesh_networking", "Wireless_mesh_network", "Network_topology", "Mobile_ad_hoc_network", "Zigbee", "Routing_protocol")},

    "ad-hoc-networks": {"tags": ["ad hoc network", "mobile ad hoc network", "wireless ad hoc", "decentralized routing"],
                        "license": CC_BY_SA,
                        "pages": wiki("Ad_hoc_network", "Mobile_ad_hoc_network", "Wireless_ad_hoc_network", "Wireless_mesh_network", "Zigbee", "Routing_protocol")},

    "network-time-sync": {"tags": ["network time protocol", "clock synchronization", "time synchronization", "gps timing"],
                          "license": CC_BY_SA,
                          "pages": wiki("Network_Time_Protocol", "Clock_synchronization", "Time_synchronization", "GPS", "Synchronous_Ethernet", "Precision_Time_Protocol")},

    "precision-time-protocol": {"tags": ["precision time protocol", "ieee 1588", "hardware timestamping", "synchronous ethernet"],
                                "license": CC_BY_SA,
                                "pages": wiki("Precision_Time_Protocol", "IEEE_1588", "Clock_synchronization", "Synchronous_Ethernet", "Time_synchronization", "Network_Time_Protocol")},

    "network-performance": {"tags": ["network performance", "network congestion", "active queue management", "bufferbloat"],
                            "license": CC_BY_SA,
                            "pages": wiki("Network_performance", "Network_congestion", "Network_congestion_avoidance", "Active_queue_management", "Random_early_detection", "Bufferbloat")},

    "queue-management": {"tags": ["active queue management", "weighted fair queueing", "random early detection", "congestion avoidance"],
                         "license": CC_BY_SA,
                         "pages": wiki("Active_queue_management", "Weighted_fair_queueing", "Random_early_detection", "Explicit_Congestion_Notification", "Network_congestion_avoidance", "Bufferbloat")},
}
