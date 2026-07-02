"""Networking protocols, routing, and OS internals (Linux/Windows/filesystems/virtualization)."""

from .common import CC_BY_SA, WIKI, man7, wiki

DOMAINS = {
    "bgp-routing": {
        "tags": ["bgp", "border gateway protocol", "internet routing", "route reflector", "routing table"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Border_Gateway_Protocol",
            "Routing",
            "Autonomous_system_(Internet)",
            "Route_reflector",
            "Routing_table",
        ) + [
            "https://www.rfc-editor.org/rfc/rfc4271.html",
        ],
    },
    "ospf-routing": {
        "tags": ["ospf", "link-state routing", "interior gateway protocol", "dijkstra", "shortest path"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Open_Shortest_Path_First",
            "Link-state_routing_protocol",
            "Dijkstra%27s_algorithm",
            "Interior_gateway_protocol",
            "Routing",
        ) + [
            "https://www.rfc-editor.org/rfc/rfc2328.html",
        ],
    },
    "mpls": {
        "tags": ["mpls", "multiprotocol label switching", "label distribution protocol", "mpls vpn"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Multiprotocol_Label_Switching",
            "Label_Distribution_Protocol",
            "MPLS_VPN",
            "Traffic_engineering_(transportation)",
            "Control_plane",
            "Forwarding_plane",
        ) + [
            "https://www.rfc-editor.org/rfc/rfc3031.html",
        ],
    },
    "vlan-networking": {
        "tags": ["vlan", "virtual lan", "802.1q", "spanning tree protocol", "trunking"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Virtual_LAN",
            "IEEE_802.1Q",
            "Spanning_Tree_Protocol",
            "VLAN_Trunking_Protocol",
            "Network_switch",
            "Broadcast,_unknown-unicast_and_multicast_traffic",
        ),
    },
    "software-defined-networking": {
        "tags": ["software-defined networking", "sdn", "openflow", "network function virtualization"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Software-defined_networking",
            "OpenFlow",
            "Network_function_virtualization",
            "Control_plane",
            "Forwarding_plane",
            "Network_management",
        ),
    },
    "quic-protocol": {
        "tags": ["quic protocol", "quic transport", "udp transport", "connection migration"],
        "license": CC_BY_SA,
        "pages": wiki(
            "QUIC",
            "Transmission_Control_Protocol",
            "User_Datagram_Protocol",
            "Head-of-line_blocking",
            "Transport_layer",
        ) + [
            "https://www.rfc-editor.org/rfc/rfc9000.html",
        ],
    },
    "http2-protocol": {
        "tags": ["http/2", "http2", "hpack", "server push", "http multiplexing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "HTTP/2",
            "HPACK",
            "Server_Push",
            "HTTP_persistent_connection",
            "HTTP_pipelining",
        ) + [
            "https://www.rfc-editor.org/rfc/rfc7540.html",
        ],
    },
    "http3-protocol": {
        "tags": ["http/3", "http3", "http over quic", "head-of-line blocking"],
        "license": CC_BY_SA,
        "pages": wiki(
            "HTTP/3",
            "QUIC",
            "Head-of-line_blocking",
            "HTTP_persistent_connection",
            "Multiplexing",
        ) + [
            "https://www.rfc-editor.org/rfc/rfc9114.html",
        ],
    },
    "ipv6": {
        "tags": ["ipv6", "ipv6 address", "neighbor discovery protocol", "ipv6 transition"],
        "license": CC_BY_SA,
        "pages": wiki(
            "IPv6",
            "IPv6_address",
            "Neighbor_Discovery_Protocol",
            "IPv6_transition_mechanism",
            "ICMPv6",
        ) + [
            "https://www.rfc-editor.org/rfc/rfc8200.html",
        ],
    },
    "icmp": {
        "tags": ["icmp", "icmpv6", "internet control message protocol", "traceroute"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Internet_Control_Message_Protocol",
            "ICMPv6",
            "Ping_(networking_utility)",
            "Traceroute",
            "Time_to_live",
        ) + [
            "https://www.rfc-editor.org/rfc/rfc792.html",
        ],
    },
    "snmp": {
        "tags": ["snmp", "simple network management protocol", "management information base", "object identifier"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Simple_Network_Management_Protocol",
            "Management_information_base",
            "Object_identifier",
            "Network_monitoring",
            "Abstract_Syntax_Notation_One",
        ) + [
            "https://www.rfc-editor.org/rfc/rfc1157.html",
        ],
    },
    "ntp-protocol": {
        "tags": ["ntp", "network time protocol", "precision time protocol", "clock synchronization", "leap second"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Network_Time_Protocol",
            "Precision_Time_Protocol",
            "Clock_synchronization",
            "Time_server",
            "Leap_second",
            "Coordinated_Universal_Time",
        ) + [
            "https://www.rfc-editor.org/rfc/rfc5905.html",
        ],
    },
    "wireguard": {
        "tags": ["wireguard", "curve25519", "noise protocol framework", "chacha20-poly1305", "perfect forward secrecy"],
        "license": CC_BY_SA,
        "pages": wiki(
            "WireGuard",
            "Curve25519",
            "Noise_Protocol_Framework",
            "ChaCha20-Poly1305",
            "Perfect_forward_secrecy",
            "Symmetric-key_algorithm",
        ),
    },
    "ipsec": {
        "tags": ["ipsec", "internet key exchange", "security association", "encapsulating security payload"],
        "license": CC_BY_SA,
        "pages": wiki(
            "IPsec",
            "Internet_Key_Exchange",
            "Security_association",
            "Encapsulating_Security_Payload",
            "Perfect_forward_secrecy",
        ) + [
            "https://www.rfc-editor.org/rfc/rfc4301.html",
        ],
    },
    "vpn-tunneling": {
        "tags": ["vpn tunneling", "virtual private network", "tunneling protocol", "openvpn", "split tunneling"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Virtual_private_network",
            "Tunneling_protocol",
            "OpenVPN",
            "Layer_2_Tunneling_Protocol",
            "Generic_Routing_Encapsulation",
            "Split_tunneling",
        ),
    },
    "anycast": {
        "tags": ["anycast", "unicast", "multicast", "content delivery network", "ip multicast"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Anycast",
            "Unicast",
            "Multicast",
            "Content_delivery_network",
            "IP_multicast",
            "Broadcasting_(networking)",
        ),
    },
    "cidr-subnetting": {
        "tags": ["cidr", "subnetting", "classless inter-domain routing", "supernetwork"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Classless_Inter-Domain_Routing",
            "Subnetwork",
            "IP_address",
            "Supernetwork",
            "Variable-length_subnet_masking",
            "IPv4",
        ),
    },
    "linux-kernel": {
        "tags": ["linux kernel", "loadable kernel module", "monolithic kernel", "kernel preemption"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Linux_kernel",
            "Loadable_kernel_module",
            "Monolithic_kernel",
            "Kernel_preemption",
            "Procfs",
            "Kernel_(operating_system)",
        ),
    },
    "ebpf": {
        "tags": ["ebpf", "berkeley packet filter", "xdp", "express data path", "kernel tracing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "EBPF",
            "Berkeley_Packet_Filter",
            "Express_Data_Path",
            "Tracing_(software)",
            "Just-in-time_compilation",
        ) + [
            man7("bpf.2"),
        ],
    },
    "io-uring": {
        "tags": ["io_uring", "asynchronous i/o", "linux async io", "event loop", "reactor pattern"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Io_uring",
            "Asynchronous_I/O",
            "Event_loop",
            "Reactor_pattern",
            "File_descriptor",
        ) + [
            man7("io_uring_setup.2"),
            man7("io_uring_enter.2"),
        ],
    },
    "epoll-kqueue": {
        "tags": ["epoll", "kqueue", "event notification", "i/o multiplexing", "completion port"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Epoll",
            "Kqueue",
            "Completion_port",
            "File_descriptor",
        ) + [
            man7("epoll.7"),
            man7("epoll_create.2"),
            man7("epoll_ctl.2"),
            man7("select.2"),
        ],
    },
    "cgroups": {
        "tags": ["cgroups", "control groups", "resource limits", "linux cgroups"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cgroups",
            "Control_groups",
            "Resource_management_(computing)",
            "Chroot",
            "Namespace",
            "Overcommitment",
        ) + [
            man7("cgroups.7"),
        ],
    },
    "linux-namespaces": {
        "tags": ["linux namespaces", "network namespaces", "unshare", "clone namespaces", "process isolation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Linux_namespaces",
            "Chroot",
            "Process_(computing)",
        ) + [
            man7("namespaces.7"),
            man7("network_namespaces.7"),
            man7("unshare.2"),
            man7("clone.2"),
        ],
    },
    "ext4-filesystem": {
        "tags": ["ext4", "ext3 filesystem", "journaling file system", "inode", "extent"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Ext4",
            "Ext3",
            "Journaling_file_system",
            "Extent_(file_systems)",
            "Inode",
            "Fsck",
        ),
    },
    "zfs-filesystem": {
        "tags": ["zfs", "openzfs", "raid-z", "copy-on-write filesystem", "data scrubbing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "ZFS",
            "OpenZFS",
            "RAID-Z",
            "Copy-on-write",
            "Data_scrubbing",
            "Data_deduplication",
        ),
    },
    "btrfs-filesystem": {
        "tags": ["btrfs", "b-tree filesystem", "filesystem snapshot", "logical volume management"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Btrfs",
            "Snapshot_(computer_storage)",
            "Logical_volume_management",
            "Copy-on-write",
            "B-tree",
            "Data_deduplication",
        ),
    },
    "xfs-filesystem": {
        "tags": ["xfs filesystem", "allocate-on-flush", "sgi filesystem", "delayed allocation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "XFS",
            "SGI",
            "Allocate-on-flush",
            "Journaling_file_system",
            "Delayed_allocation",
            "Extent_(file_systems)",
        ),
    },
    "ntfs-filesystem": {
        "tags": ["ntfs", "master file table", "alternate data streams", "fat filesystem"],
        "license": CC_BY_SA,
        "pages": wiki(
            "NTFS",
            "Master_File_Table",
            "Alternate_Data_Streams",
            "File_Allocation_Table",
            "Encrypting_File_System",
            "Access-control_list",
        ),
    },
    "virtual-file-system": {
        "tags": ["virtual file system", "vfs layer", "filesystem in userspace", "symbolic link"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Virtual_file_system",
            "Filesystem_in_Userspace",
            "Symbolic_link",
            "Comparison_of_file_systems",
        ) + [
            man7("mount.2"),
            man7("statfs.2"),
            man7("fstab.5"),
        ],
    },
    "windows-internals": {
        "tags": ["windows internals", "windows nt architecture", "native api", "windows registry"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Architecture_of_Windows_NT",
            "Windows_NT",
            "Native_API",
            "Windows_Registry",
            "Object_Manager_(Windows)",
            "Windows_kernel",
        ),
    },
    "macos-darwin": {
        "tags": ["macos internals", "darwin operating system", "xnu kernel", "grand central dispatch"],
        "license": CC_BY_SA,
        "pages": wiki(
            "MacOS",
            "XNU",
            "Mach_(kernel)",
            "Darwin_(operating_system)",
            "Grand_Central_Dispatch",
            "APFS",
        ),
    },
    "freebsd-os": {
        "tags": ["freebsd", "berkeley software distribution", "freebsd jail", "dtrace", "sysctl"],
        "license": CC_BY_SA,
        "pages": wiki(
            "FreeBSD",
            "Berkeley_Software_Distribution",
            "Jail_(computer_security)",
            "DTrace",
            "Sysctl",
            "Kqueue",
        ),
    },
    "posix-standard": {
        "tags": ["posix", "single unix specification", "posix library", "filesystem hierarchy standard"],
        "license": CC_BY_SA,
        "pages": wiki(
            "POSIX",
            "Single_UNIX_Specification",
            "C_POSIX_library",
            "Filesystem_Hierarchy_Standard",
            "Berkeley_sockets",
            "Pthreads",
        ),
    },
    "linux-system-calls": {
        "tags": ["linux system calls", "syscall interface", "read syscall", "ioctl"],
        "license": CC_BY_SA,
        "pages": wiki(
            "System_call",
            "File_descriptor",
            "Fork_(system_call)",
        ) + [
            man7("syscalls.2"),
            man7("read.2"),
            man7("write.2"),
            man7("open.2"),
            man7("ioctl.2"),
        ],
    },
    "unix-signals": {
        "tags": ["unix signals", "signal handling", "sigaction", "async-signal-safe"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Signal_(IPC)",
            "Signal.h",
            "Interrupt",
        ) + [
            man7("signal.7"),
            man7("signal-safety.7"),
            man7("sigaction.2"),
            man7("kill.2"),
        ],
    },
    "unix-pipes": {
        "tags": ["unix pipes", "named pipe", "anonymous pipe", "mkfifo"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Anonymous_pipe",
            "Named_pipe",
            "File_descriptor",
        ) + [
            man7("pipe.2"),
            man7("pipe.7"),
            man7("mkfifo.3"),
        ],
    },
    "memory-mapped-files": {
        "tags": ["memory-mapped files", "mmap", "madvise", "msync"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Memory-mapped_file",
            "Page_(computer_memory)",
            "Demand_paging",
        ) + [
            man7("mmap.2"),
            man7("munmap.2"),
            man7("msync.2"),
            man7("madvise.2"),
        ],
    },
    "page-cache": {
        "tags": ["page cache", "buffer cache", "fsync", "disk cache", "working set"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Page_cache",
            "Cache_(computing)",
            "Working_set",
            "Block_(data_storage)",
        ) + [
            man7("fsync.2"),
            man7("free.1"),
        ],
    },
    "swap-memory": {
        "tags": ["swap memory", "memory paging", "swapon", "virtual memory swap", "thrashing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Memory_paging",
            "Paging",
            "Page_replacement_algorithm",
            "Thrashing_(computer_science)",
            "Demand_paging",
        ) + [
            man7("swapon.8"),
            man7("swapon.2"),
        ],
    },
    "kvm-virtualization": {
        "tags": ["kvm", "kernel-based virtual machine", "hardware-assisted virtualization", "libvirt"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kernel-based_Virtual_Machine",
            "Hypervisor",
            "Hardware-assisted_virtualization",
            "Libvirt",
            "X86_virtualization",
            "Second_Level_Address_Translation",
        ),
    },
    "qemu-emulator": {
        "tags": ["qemu", "binary translation", "machine emulator", "system emulation", "dynamic recompilation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "QEMU",
            "Binary_translation",
            "Emulator",
            "Dynamic_recompilation",
            "Instruction_set_simulator",
            "Type-2_hypervisor",
        ),
    },
    "xen-hypervisor": {
        "tags": ["xen", "xen hypervisor", "paravirtualization", "type-1 hypervisor", "dom0"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Xen",
            "Paravirtualization",
            "Hypervisor",
            "Dom0",
            "Popek_and_Goldberg_virtualization_requirements",
            "X86_virtualization",
        ),
    },
    "hyper-v": {
        "tags": ["hyper-v", "microsoft hyper-v", "hyperjacking", "windows virtualization"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Hyper-V",
            "Hyperjacking",
            "Hardware-assisted_virtualization",
            "Windows_Server",
            "Second_Level_Address_Translation",
            "Virtual_machine",
        ),
    },
    "containers-vs-vms": {
        "tags": ["os-level virtualization", "full virtualization", "application virtualization", "containers vs virtual machines"],
        "license": CC_BY_SA,
        "pages": wiki(
            "OS-level_virtualization",
            "Full_virtualization",
            "Application_virtualization",
            "System_virtual_machine",
            "Docker_(software)",
            "LXC",
        ),
    },
    "tcp-congestion-control": {
        "tags": ["tcp congestion control", "cubic tcp", "tcp vegas", "bufferbloat"],
        "license": CC_BY_SA,
        "pages": wiki(
            "TCP_congestion_control",
            "CUBIC_TCP",
            "TCP_Vegas",
            "Additive_increase/multiplicative_decrease",
            "Bufferbloat",
            "Slow_start",
        ),
    },
    "packet-switching": {
        "tags": ["packet switching", "network packet", "store and forward", "circuit switching", "datagram"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Packet_switching",
            "Network_packet",
            "Store_and_forward",
            "Circuit_switching",
            "Datagram",
            "Message_switching",
        ),
    },
    "ethernet": {
        "tags": ["ethernet", "ethernet frame", "csma/cd", "medium access control"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Ethernet",
            "Ethernet_frame",
            "Carrier-sense_multiple_access_with_collision_detection",
            "Medium_access_control",
            "Autonegotiation",
            "Gigabit_Ethernet",
        ),
    },
    "wifi-standards": {
        "tags": ["wi-fi", "802.11", "wi-fi 6", "wireless lan", "wireless access point"],
        "license": CC_BY_SA,
        "pages": wiki(
            "IEEE_802.11",
            "Wi-Fi",
            "Wi-Fi_6",
            "Wireless_LAN",
            "Wireless_access_point",
            "Wi-Fi_Protected_Access",
        ),
    },
    "network-load-balancing": {
        "tags": ["network load balancing", "round-robin dns", "weighted round robin", "failover"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Load_balancing_(computing)",
            "Round-robin_DNS",
            "Weighted_round_robin",
            "Failover",
            "High-availability_cluster",
            "Server_farm",
        ),
    },
    "proxy-servers": {
        "tags": ["proxy server", "reverse proxy", "transparent proxy", "socks proxy", "web cache"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Proxy_server",
            "Reverse_proxy",
            "Transparent_proxy",
            "SOCKS",
            "Web_cache",
            "Application-level_gateway",
        ),
    },
    "dns-security": {
        "tags": ["dnssec", "dns over https", "dns over tls", "dns spoofing", "zone transfer"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Domain_Name_System_Security_Extensions",
            "DNS_over_HTTPS",
            "DNS_over_TLS",
            "DNS_spoofing",
            "Zone_transfer",
        ) + [
            "https://www.rfc-editor.org/rfc/rfc4033.html",
        ],
    },
}
