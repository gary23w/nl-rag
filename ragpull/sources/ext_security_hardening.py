"""Systems-security hardening, memory safety, side-channel defenses, and supply-chain integrity."""

from .common import CC_BY_SA, wiki

# Non-Wikipedia static sources are each verified live (HTTP 200/2xx) at authoring time.
# SLSA (Supply-chain Levels for Software Artifacts) serves clean static docs:      slsa.dev
# Sigstore, in-toto, TUF, reproducible-builds, and the seccomp/AppArmor/Landlock
# project docs are static HTML/Markdown pages under permissive/CC licenses.
SLSA = "https://slsa.dev/spec/v1.0/"
SIGSTORE = "https://docs.sigstore.dev/"
INTOTO = "https://in-toto.io/"

DOMAINS = {
    # ---- memory safety -------------------------------------------------------
    "memory-safety": {
        "tags": [
            "memory safety",
            "spatial memory safety",
            "temporal memory safety",
            "memory safe language",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Memory_safety",
            "Dangling_pointer",
            "Buffer_over-read",
            "Type_safety",
            "Garbage_collection_(computer_science)",
            "Rust_(programming_language)",
        ),
    },
    "use-after-free-defense": {
        "tags": [
            "use after free defense",
            "dangling pointer mitigation",
            "temporal memory safety",
            "quarantine allocator hardening",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Dangling_pointer",
            "Manual_memory_management",
            "Memory_management",
            "C_dynamic_memory_allocation",
            "AddressSanitizer",
            "Memory_leak",
        ),
    },
    "buffer-overflow-protection": {
        "tags": [
            "buffer overflow protection",
            "bounds checking defense",
            "out of bounds write mitigation",
            "heap overflow hardening",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Buffer_overflow",
            "Buffer_overflow_protection",
            "Bounds_checking",
            "Heap_overflow",
            "Stack_buffer_overflow",
            "Address_space_layout_randomization",
        ),
    },
    "stack-smashing-protection": {
        "tags": [
            "stack smashing protection",
            "return address integrity",
            "stack guard defense",
            "prologue epilogue canary",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Stack_buffer_overflow",
            "Buffer_overflow_protection",
            "Call_stack",
            "Return-oriented_programming",
            "Executable_space_protection",
            "Buffer_over-read",
        ),
    },
    "shadow-stack": {
        "tags": [
            "shadow stack defense",
            "return address protection",
            "hardware enforced stack protection",
            "control flow enforcement technology",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Shadow_stack",
            "Return-oriented_programming",
            "Call_stack",
            "Control-flow_integrity",
            "X86",
            "Buffer_overflow",
        ),
    },
    "pointer-authentication": {
        "tags": [
            "pointer authentication code",
            "cryptographic pointer signing",
            "return address tampering defense",
            "arm memory protection",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Pointer_(computer_programming)",
            "ARM_architecture_family",
            "Return-oriented_programming",
            "Message_authentication_code",
            "Control-flow_integrity",
            "Public-key_cryptography",
        ),
    },
    "memory-tagging-extension": {
        "tags": [
            "memory tagging extension",
            "hardware memory tagging",
            "tagged pointer safety",
            "lock and key memory model",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Tagged_pointer",
            "ARM_architecture_family",
            "Dangling_pointer",
            "Memory_safety",
            "Tagged_architecture",
            "Memory_protection",
        ),
    },
    "hardware-memory-safety": {
        "tags": [
            "hardware enforced memory safety",
            "capability based addressing",
            "fat pointer hardware",
            "cheri capability model",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Capability-based_addressing",
            "Capability-based_security",
            "Tagged_architecture",
            "Memory_protection",
            "Fat_pointer",
            "Bounds_checking",
        ),
    },
    "rust-memory-safety": {
        "tags": [
            "rust ownership model",
            "borrow checker safety",
            "affine type discipline",
            "compile time memory safety",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Rust_(programming_language)",
            "Substructural_type_system",
            "Region-based_memory_management",
            "Resource_acquisition_is_initialization",
            "Memory_safety",
            "Memory_management",
        ),
    },
    "fortify-source": {
        "tags": [
            "fortify source hardening",
            "compiler runtime buffer checks",
            "glibc object size checking",
            "hardened build flags",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Buffer_overflow_protection",
            "GNU_C_Library",
            "GNU_Compiler_Collection",
            "C_standard_library",
            "Hardening_(computing)",
            "Executable_space_protection",
        ),
    },
    "safe-stack": {
        "tags": [
            "safe stack isolation",
            "unsafe stack separation",
            "control data protection",
            "code pointer integrity",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Call_stack",
            "Control-flow_integrity",
            "Clang",
            "Stack_buffer_overflow",
            "Buffer_overflow_protection",
            "Return-oriented_programming",
        ),
    },
    # ---- side-channel & speculative-execution defenses -----------------------
    "spectre-mitigation": {
        "tags": [
            "spectre mitigation",
            "speculative execution defense",
            "cpu side channel defense",
            "branch predictor hardening",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Spectre_(security_vulnerability)",
            "Speculative_execution_CPU_vulnerabilities",
            "Side-channel_attack",
            "Branch_predictor",
            "CPU_cache",
            "Retpoline",
        ),
    },
    "meltdown-mitigation": {
        "tags": [
            "meltdown mitigation",
            "kernel page table isolation",
            "out of order execution defense",
            "transient execution defense",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Meltdown_(security_vulnerability)",
            "Kernel_page-table_isolation",
            "Out-of-order_execution",
            "Transient_execution_CPU_vulnerability",
            "Speculative_execution",
            "Central_processing_unit",
        ),
    },
    "rowhammer-defense": {
        "tags": [
            "rowhammer defense",
            "dram disturbance mitigation",
            "target row refresh",
            "bit flip attack defense",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Row_hammer",
            "Dynamic_random-access_memory",
            "Error_correction_code",
            "Memory_refresh",
            "ECC_memory",
            "Bit_flipping",
        ),
    },
    "cache-timing-defense": {
        "tags": [
            "cache timing side channel",
            "cache partitioning defense",
            "prime and probe mitigation",
            "flush reload defense",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Side-channel_attack",
            "Timing_attack",
            "CPU_cache",
            "Cache_replacement_policies",
            "Translation_lookaside_buffer",
            "Cache_(computing)",
        ),
    },
    "constant-time-crypto": {
        "tags": [
            "constant time cryptography",
            "timing attack resistance",
            "data independent execution",
            "branchless cryptographic code",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Timing_attack",
            "Side-channel_attack",
            "Montgomery_modular_multiplication",
            "Cryptographic_primitive",
            "Branch_(computer_science)",
            "Modular_exponentiation",
        ),
    },
    "blinding-cryptography": {
        "tags": [
            "cryptographic blinding",
            "rsa blinding defense",
            "message randomization countermeasure",
            "side channel blinding",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Blinding_(cryptography)",
            "RSA_(cryptosystem)",
            "Side-channel_attack",
            "Timing_attack",
            "Modular_exponentiation",
            "Public-key_cryptography",
        ),
    },
    "fault-injection-defense": {
        "tags": [
            "fault injection defense",
            "glitch attack countermeasure",
            "redundant computation checking",
            "differential fault analysis defense",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Fault_injection",
            "Differential_fault_analysis",
            "Tamper_resistance",
            "Hardware_security",
            "Error_detection_and_correction",
            "Cryptography",
        ),
    },
    "power-analysis-defense": {
        "tags": [
            "power analysis countermeasure",
            "differential power analysis defense",
            "masking side channel defense",
            "hiding leakage countermeasure",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Power_analysis",
            "Side-channel_attack",
            "Tamper_resistance",
            "Smart_card",
            "Countermeasure_(computer)",
            "Cryptographic_primitive",
        ),
    },
    # ---- boot / attestation / measured integrity -----------------------------
    "secure-boot-measured": {
        "tags": [
            "measured boot integrity",
            "boot chain of trust",
            "platform configuration register",
            "trusted boot measurement",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Trusted_Platform_Module",
            "Root_of_trust",
            "Chain_of_trust",
            "Unified_Extensible_Firmware_Interface",
            "Booting",
            "Trusted_Computing",
        ),
    },
    "remote-attestation": {
        "tags": [
            "remote attestation protocol",
            "platform integrity attestation",
            "attestation evidence verification",
            "trusted computing attestation",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Trusted_Computing",
            "Trusted_Platform_Module",
            "Direct_Anonymous_Attestation",
            "Attestation",
            "Root_of_trust",
            "Trusted_Computing_Group",
        ),
    },
    "tpm-attestation": {
        "tags": [
            "tpm quote attestation",
            "platform configuration register quote",
            "endorsement key attestation",
            "trusted platform module measurement",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Trusted_Platform_Module",
            "Trusted_Computing_Group",
            "Direct_Anonymous_Attestation",
            "Public-key_cryptography",
            "Root_of_trust",
            "Trusted_Computing",
        ),
    },
    "uefi-secure-boot-deep": {
        "tags": [
            "uefi secure boot verification",
            "firmware signature enforcement",
            "boot loader signing key",
            "platform key hierarchy",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Unified_Extensible_Firmware_Interface",
            "BIOS",
            "Booting",
            "Code_signing",
            "Public_key_certificate",
            "Firmware",
        ),
    },
    "dm-verity": {
        "tags": [
            "device mapper verity",
            "block device integrity verification",
            "read only rootfs integrity",
            "merkle tree block hashing",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Dm-verity",
            "Device_mapper",
            "Merkle_tree",
            "Cryptographic_hash_function",
            "Linux_kernel",
            "Read-only_memory",
        ),
    },
    "integrity-measurement": {
        "tags": [
            "integrity measurement architecture",
            "runtime file integrity attestation",
            "linux ima appraisal",
            "measured runtime integrity",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "File_integrity_monitoring",
            "Trusted_Platform_Module",
            "File_verification",
            "Linux_Security_Modules",
            "Cryptographic_hash_function",
            "Merkle_tree",
        ),
    },
    # ---- supply-chain integrity ----------------------------------------------
    "slsa-framework": {
        "tags": [
            "slsa provenance framework",
            "build integrity levels",
            "supply chain provenance",
            "hermetic build attestation",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Supply_chain_attack",
            "Provenance",
            "Software_build",
            "Reproducible_builds",
            "DevSecOps",
        )
        + [
            SLSA + "levels",
            SLSA + "requirements",
        ],
    },
    "sigstore-signing": {
        "tags": [
            "sigstore keyless signing",
            "transparency log signing",
            "artifact signature verification",
            "ephemeral signing certificate",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Code_signing",
            "Digital_signature",
            "Public_key_infrastructure",
            "Certificate_Transparency",
            "Public-key_cryptography",
        )
        + [
            SIGSTORE + "about/overview/",
            SIGSTORE + "cosign/verifying/verify/",
        ],
    },
    "in-toto-attestation": {
        "tags": [
            "in-toto supply chain attestation",
            "software supply chain metadata",
            "build step link metadata",
            "layout policy verification",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Supply_chain_attack",
            "Metadata",
            "Digital_signature",
            "Provenance",
            "Software_build",
        )
        + [
            INTOTO + "specs/",
            INTOTO + "docs/what-is-in-toto/",
        ],
    },
    "reproducible-builds": {
        "tags": [
            "reproducible build determinism",
            "bit for bit build reproducibility",
            "deterministic compilation",
            "build environment normalization",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Reproducible_builds",
            "Deterministic_algorithm",
            "Compiler",
            "Build_automation",
            "Software_distribution",
        )
        + [
            "https://reproducible-builds.org/docs/",
        ],
    },
    "software-bill-of-materials-deep": {
        "tags": [
            "software bill of materials format",
            "spdx component inventory",
            "cyclonedx dependency manifest",
            "transitive component disclosure",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Software_bill_of_materials",
            "Software_Package_Data_Exchange",
            "Software_supply_chain",
            "Open-source_software",
            "Component-based_software_engineering",
            "Vulnerability_(computer_security)",
        ),
    },
    "dependency-pinning": {
        "tags": [
            "dependency version pinning",
            "lock file reproducibility",
            "hash pinned dependency",
            "deterministic dependency resolution",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Package_manager",
            "Dependency_hell",
            "Software_versioning",
            "Coupling_(computer_programming)",
            "Reproducible_builds",
            "Hash_function",
        ),
    },
    "vendoring-dependencies": {
        "tags": [
            "vendored dependency tree",
            "third party source inclusion",
            "monorepo dependency vendoring",
            "offline build dependency copy",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Coupling_(computer_programming)",
            "Monorepo",
            "Package_manager",
            "Fork_(software_development)",
            "Source_code",
            "Version_control",
        ),
    },
    "artifact-signing": {
        "tags": [
            "build artifact signing",
            "release artifact provenance",
            "detached signature verification",
            "artifact integrity attestation",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Digital_signature",
            "Code_signing",
            "Cryptographic_hash_function",
            "GNU_Privacy_Guard",
            "Public-key_cryptography",
            "Checksum",
        ),
    },
    "code-signing-deep": {
        "tags": [
            "code signing certificate",
            "authenticode signature verification",
            "timestamped code signature",
            "signing key protection",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Code_signing",
            "Public_key_certificate",
            "Trusted_timestamping",
            "Certificate_authority",
            "Digital_signature",
            "Malware",
        ),
    },
    "notary-tuf": {
        "tags": [
            "the update framework",
            "tuf role delegation",
            "repository signing metadata",
            "rollback attack defense",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "The_Update_Framework",
            "Software_repository",
            "Digital_signature",
            "Key_management",
            "Public-key_cryptography",
            "Software_versioning",
        ),
    },
    # ---- sandboxing & OS isolation -------------------------------------------
    "seccomp-sandboxing": {
        "tags": [
            "seccomp system call filtering",
            "syscall allowlist sandbox",
            "berkeley packet filter seccomp",
            "process privilege reduction",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Seccomp",
            "System_call",
            "Sandbox_(computer_security)",
            "Berkeley_Packet_Filter",
            "Linux_kernel",
            "Process_(computing)",
        ),
    },
    "linux-capabilities": {
        "tags": [
            "linux capability model",
            "privilege decomposition capabilities",
            "capability bounding set",
            "least privilege capability drop",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Capability-based_security",
            "Superuser",
            "Principle_of_least_privilege",
            "Setuid",
            "Linux_kernel",
            "Sudo",
        ),
    },
    "apparmor-mac": {
        "tags": [
            "apparmor mandatory access control",
            "path based confinement profile",
            "application confinement policy",
            "linux security module profile",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "AppArmor",
            "Mandatory_access_control",
            "Linux_Security_Modules",
            "Access_control",
            "Sandbox_(computer_security)",
            "Novell",
        ),
    },
    "selinux-policy": {
        "tags": [
            "selinux type enforcement",
            "security enhanced linux policy",
            "mandatory access control label",
            "domain transition policy",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Security-Enhanced_Linux",
            "Type_enforcement",
            "Mandatory_access_control",
            "Multilevel_security",
            "Linux_Security_Modules",
            "National_Security_Agency",
        ),
    },
    "landlock-lsm": {
        "tags": [
            "landlock unprivileged sandbox",
            "filesystem access restriction",
            "self restricting process sandbox",
            "linux security module ruleset",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Linux_Security_Modules",
            "Sandbox_(computer_security)",
            "Principle_of_least_privilege",
            "File-system_permissions",
            "Linux_kernel",
            "System_call",
        ),
    },
    "namespaces-isolation": {
        "tags": [
            "linux namespace isolation",
            "process resource namespacing",
            "user namespace remapping",
            "container primitive isolation",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Linux_namespaces",
            "OS-level_virtualization",
            "Cgroups",
            "Chroot",
            "Process_isolation",
            "Container_(virtualization)",
        ),
    },
    "gvisor-sandbox": {
        "tags": [
            "gvisor user space kernel",
            "application kernel sandbox",
            "syscall interception isolation",
            "container runtime sandbox",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Sandbox_(computer_security)",
            "OS-level_virtualization",
            "System_call",
            "Kernel_(operating_system)",
            "Hypervisor",
            "Go_(programming_language)",
        ),
    },
    "kata-containers": {
        "tags": [
            "kata lightweight virtual machine",
            "hardware virtualized container",
            "vm isolated container runtime",
            "micro vm workload isolation",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "OS-level_virtualization",
            "Hardware_virtualization",
            "Hypervisor",
            "Open_Container_Initiative",
            "Kernel-based_Virtual_Machine",
            "Container_(virtualization)",
        ),
    },
    "firecracker-microvm": {
        "tags": [
            "firecracker micro virtual machine",
            "lightweight vmm isolation",
            "serverless workload isolation",
            "minimal device model vmm",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Hypervisor",
            "Kernel-based_Virtual_Machine",
            "Virtual_machine",
            "Serverless_computing",
            "Hardware_virtualization",
            "Amazon_Web_Services",
        ),
    },
    "container-escape-defense": {
        "tags": [
            "container escape prevention",
            "container breakout defense",
            "privileged container hardening",
            "namespace escape mitigation",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "OS-level_virtualization",
            "Privilege_escalation",
            "Sandbox_(computer_security)",
            "Cgroups",
            "Kernel_(operating_system)",
            "Vulnerability_(computer_security)",
        ),
    },
    # ---- Kubernetes / cloud-native policy ------------------------------------
    "kubernetes-pod-security": {
        "tags": [
            "pod security standards",
            "pod security admission",
            "restricted pod profile",
            "workload privilege constraint",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "OS-level_virtualization",
            "Principle_of_least_privilege",
            "Role-based_access_control",
            "Microservices",
            "Container_(virtualization)",
        ),
    },
    "network-policy-k8s": {
        "tags": [
            "kubernetes network policy",
            "pod network segmentation",
            "east west traffic control",
            "cluster microsegmentation policy",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "Network_segmentation",
            "Software-defined_networking",
            "Firewall_(computing)",
            "Overlay_network",
            "Container_(virtualization)",
        ),
    },
    "admission-controllers": {
        "tags": [
            "admission controller webhook",
            "validating admission policy",
            "mutating admission webhook",
            "cluster request interception",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "Webhook",
            "Access_control",
            "Policy-based_management",
            "Application_programming_interface",
            "Authorization",
        ),
    },
    "opa-gatekeeper": {
        "tags": [
            "open policy agent",
            "rego policy language",
            "policy as code enforcement",
            "gatekeeper constraint template",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Policy-based_management",
            "Declarative_programming",
            "Access_control",
            "Kubernetes",
            "Domain-specific_language",
            "Authorization",
        ),
    },
    "falco-runtime": {
        "tags": [
            "falco runtime threat detection",
            "syscall anomaly detection",
            "runtime security monitoring",
            "kernel event detection rules",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Intrusion_detection_system",
            "System_call",
            "Anomaly_detection",
            "Extended_Berkeley_Packet_Filter",
            "OS-level_virtualization",
            "Cloud_computing_security",
        ),
    },
    "ebpf-security-deep": {
        "tags": [
            "ebpf security observability",
            "kernel programmable tracing",
            "in kernel verifier safety",
            "syscall tracing enforcement",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Extended_Berkeley_Packet_Filter",
            "Berkeley_Packet_Filter",
            "Kernel_(operating_system)",
            "Tracing_(software)",
            "Just-in-time_compilation",
            "Observability",
        ),
    },
    # ---- kernel & OS hardening -----------------------------------------------
    "kernel-hardening": {
        "tags": [
            "linux kernel hardening",
            "kernel self protection",
            "kernel attack surface reduction",
            "kernel address space isolation",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kernel_(operating_system)",
            "Hardening_(computing)",
            "Kernel_page-table_isolation",
            "Address_space_layout_randomization",
            "Attack_surface",
            "Memory_protection",
        ),
    },
    "grsecurity-concepts": {
        "tags": [
            "grsecurity hardening patchset",
            "pax memory protection",
            "role based access control kernel",
            "kernel exploitation mitigation",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Exec_Shield",
            "Memory_protection",
            "Executable_space_protection",
            "Address_space_layout_randomization",
            "Hardening_(computing)",
            "Kernel_(operating_system)",
        ),
    },
}
