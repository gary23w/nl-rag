"""Identity, privacy engineering, cloud/OT/IoT security (defensive).

Encyclopedic + standards-level grounding only: privacy-preserving computation, identity
federation and credentials, key/certificate lifecycle, cloud posture, and OT/ICS defense.
All pages are Wikipedia articles (CC-BY-SA); every URL verified live via the MediaWiki API
at authoring time (no 404s, no within-domain redirect collapses).
"""

from .common import CC_BY_SA, wiki

DOMAINS = {
    "privacy-engineering": {
        "tags": ["privacy engineering", "privacy by design", "data minimization", "privacy enhancing technologies"],
        "license": CC_BY_SA,
        "pages": wiki("Privacy_engineering", "Privacy_by_design", "Data_minimization", "Information_privacy", "Personally_identifiable_information", "Data_anonymization"),
    },
    "differential-privacy-applied": {
        "tags": ["differential privacy", "local differential privacy", "privacy budget epsilon", "randomized response", "statistical disclosure control"],
        "license": CC_BY_SA,
        "pages": wiki("Differential_privacy", "Local_differential_privacy", "Laplace_distribution", "Randomized_response", "Statistical_disclosure_control", "Privacy-enhancing_technologies"),
    },
    "k-anonymity": {
        "tags": ["k anonymity", "l diversity", "t closeness", "quasi identifier", "data re identification"],
        "license": CC_BY_SA,
        "pages": wiki("K-anonymity", "L-diversity", "T-closeness", "Quasi-identifier", "Data_re-identification", "Record_linkage"),
    },
    "data-anonymization": {
        "tags": ["data anonymization", "de identification", "data masking", "synthetic data generation", "data scrubbing"],
        "license": CC_BY_SA,
        "pages": wiki("Data_anonymization", "De-identification", "Pseudonymization", "Data_masking", "Synthetic_data", "Data_scrubbing"),
    },
    "pseudonymization": {
        "tags": ["pseudonymization technique", "reversible pseudonym", "gdpr pseudonymization", "tokenized identifier", "data anonymization"],
        "license": CC_BY_SA,
        "pages": wiki("Pseudonymization", "Pseudonym", "Tokenization_(data_security)", "Data_anonymization", "General_Data_Protection_Regulation", "Hash_function"),
    },
    "homomorphic-encryption-applied": {
        "tags": ["homomorphic encryption", "fully homomorphic encryption", "paillier cryptosystem", "learning with errors", "lattice based cryptography"],
        "license": CC_BY_SA,
        "pages": wiki("Homomorphic_encryption", "Paillier_cryptosystem", "Learning_with_errors", "Ring_learning_with_errors", "Lattice-based_cryptography", "Functional_encryption"),
    },
    "secure-aggregation": {
        "tags": ["secure aggregation", "secure multiparty computation", "secret sharing scheme", "federated aggregation", "oblivious transfer"],
        "license": CC_BY_SA,
        "pages": wiki("Secure_multi-party_computation", "Secret_sharing", "Shamir's_secret_sharing", "Federated_learning", "Oblivious_transfer", "Homomorphic_encryption"),
    },
    "privacy-preserving-ml": {
        "tags": ["privacy preserving machine learning", "federated learning", "differential privacy training", "secure multiparty computation", "encrypted inference"],
        "license": CC_BY_SA,
        "pages": wiki("Federated_learning", "Differential_privacy", "Secure_multi-party_computation", "Machine_learning", "Homomorphic_encryption", "Privacy-enhancing_technologies"),
    },
    "gdpr-technical-controls": {
        "tags": ["gdpr technical controls", "right to erasure", "data portability", "data protection impact assessment", "privacy by design"],
        "license": CC_BY_SA,
        "pages": wiki("General_Data_Protection_Regulation", "Right_to_be_forgotten", "Data_Protection_Officer", "Data_portability", "Privacy_by_design", "Data_protection_impact_assessment"),
    },
    "ccpa-privacy": {
        "tags": ["ccpa privacy rights", "consumer privacy law", "data broker regulation", "right to opt out", "information privacy law"],
        "license": CC_BY_SA,
        "pages": wiki("California_Consumer_Privacy_Act", "Information_privacy_law", "Privacy_law", "Right_to_be_forgotten", "Consumer_privacy", "Data_broker"),
    },
    "consent-management": {
        "tags": ["consent management platform", "informed consent record", "cookie consent banner", "privacy policy disclosure", "do not track"],
        "license": CC_BY_SA,
        "pages": wiki("Consent", "Informed_consent", "HTTP_cookie", "Privacy_policy", "General_Data_Protection_Regulation", "Do_Not_Track"),
    },
    "identity-federation": {
        "tags": ["identity federation", "federated identity provider", "cross domain sso", "saml federation", "identity and access management"],
        "license": CC_BY_SA,
        "pages": wiki("Federated_identity", "Identity_provider", "Single_sign-on", "Security_Assertion_Markup_Language", "OpenID", "Identity_management"),
    },
    "single-sign-on-deep": {
        "tags": ["single sign on", "central authentication service", "integrated windows authentication", "kerberos authentication", "identity provider"],
        "license": CC_BY_SA,
        "pages": wiki("Single_sign-on", "Central_Authentication_Service", "Integrated_Windows_Authentication", "Kerberos_(protocol)", "Identity_provider", "OAuth"),
    },
    "oauth2-flows-deep": {
        "tags": ["oauth2 authorization flow", "authorization code grant", "access token issuance", "bearer token authentication", "json web token"],
        "license": CC_BY_SA,
        "pages": wiki("OAuth", "Authorization", "Access_token", "Basic_access_authentication", "JSON_Web_Token", "Authentication"),
    },
    "openid-connect-deep": {
        "tags": ["openid connect", "id token claims", "userinfo endpoint", "oidc authentication flow", "claims based identity"],
        "license": CC_BY_SA,
        "pages": wiki("OpenID_Connect", "Authentication", "JSON_Web_Token", "OAuth", "Identity_provider", "Claims-based_identity"),
    },
    "saml-deep": {
        "tags": ["saml assertion", "saml2 protocol", "saml metadata exchange", "service provider sso", "identity provider initiated"],
        "license": CC_BY_SA,
        "pages": wiki("Security_Assertion_Markup_Language", "SAML_2.0", "SAML_metadata", "Single_sign-on", "Assertion_(software_development)", "Identity_provider"),
    },
    "scim-provisioning-deep": {
        "tags": ["scim provisioning", "cross domain identity management", "automated user provisioning", "directory synchronization", "deprovisioning lifecycle"],
        "license": CC_BY_SA,
        "pages": wiki("System_for_Cross-domain_Identity_Management", "Provisioning_(technology)", "Identity_management", "Directory_service", "User_provisioning_software", "Lightweight_Directory_Access_Protocol"),
    },
    "decentralized-identity-deep": {
        "tags": ["decentralized identifier", "self sovereign identity", "verifiable credential exchange", "did document resolution", "distributed ledger identity"],
        "license": CC_BY_SA,
        "pages": wiki("Decentralized_identifier", "Self-sovereign_identity", "Verifiable_credentials", "Digital_identity", "Public-key_cryptography", "Distributed_ledger"),
    },
    "verifiable-credentials": {
        "tags": ["verifiable credential", "credential issuer holder", "zero knowledge proof presentation", "digital credential signature", "decentralized identifier"],
        "license": CC_BY_SA,
        "pages": wiki("Verifiable_credentials", "Decentralized_identifier", "Digital_credential", "Public-key_cryptography", "Zero-knowledge_proof", "Digital_signature"),
    },
    "self-sovereign-identity": {
        "tags": ["self sovereign identity", "user controlled identity", "decentralized identifier wallet", "verifiable credential holder", "digital identity ownership"],
        "license": CC_BY_SA,
        "pages": wiki("Self-sovereign_identity", "Decentralized_identifier", "Digital_identity", "Verifiable_credentials", "Identity_management", "Distributed_ledger"),
    },
    "passkeys-deep": {
        "tags": ["passkey authentication", "webauthn credential", "fido2 passwordless", "public key authenticator", "multi factor authentication"],
        "license": CC_BY_SA,
        "pages": wiki("WebAuthn", "Universal_2nd_Factor", "FIDO_Alliance", "Public-key_cryptography", "Multi-factor_authentication", "Authenticator"),
    },
    "fido2-ctap": {
        "tags": ["fido2 ctap protocol", "client to authenticator", "webauthn ceremony", "universal second factor", "hardware security key"],
        "license": CC_BY_SA,
        "pages": wiki("Authentication", "WebAuthn", "Universal_2nd_Factor", "FIDO_Alliance", "Security_token", "Challenge-response_authentication"),
    },
    "mutual-tls": {
        "tags": ["mutual tls authentication", "client certificate authentication", "x509 client certificate", "two way tls", "certificate based authentication"],
        "license": CC_BY_SA,
        "pages": wiki("Mutual_authentication", "Transport_Layer_Security", "Public_key_certificate", "Client_certificate", "X.509", "Public_key_infrastructure"),
    },
    "certificate-lifecycle": {
        "tags": ["certificate lifecycle management", "certificate revocation list", "ocsp revocation check", "certificate signing request", "certificate authority issuance"],
        "license": CC_BY_SA,
        "pages": wiki("Public_key_certificate", "Certificate_authority", "Certificate_revocation_list", "Online_Certificate_Status_Protocol", "Certificate_signing_request", "Public_key_infrastructure"),
    },
    "acme-protocol": {
        "tags": ["acme protocol", "automated certificate issuance", "lets encrypt automation", "domain validation challenge", "certificate renewal automation"],
        "license": CC_BY_SA,
        "pages": wiki("Automatic_Certificate_Management_Environment", "Let's_Encrypt", "Public_key_certificate", "Certificate_authority", "Transport_Layer_Security", "Domain_validation"),
    },
    "hsm-key-ceremony": {
        "tags": ["hardware security module", "key ceremony procedure", "root key generation", "dnssec key signing", "trust anchor provisioning"],
        "license": CC_BY_SA,
        "pages": wiki("Hardware_security_module", "Key_ceremony", "Key_management", "DNSSEC", "Root_certificate", "Trust_anchor"),
    },
    "key-management-deep": {
        "tags": ["key management system", "cryptographic key lifecycle", "key derivation function", "key exchange protocol", "key escrow recovery"],
        "license": CC_BY_SA,
        "pages": wiki("Key_management", "Key_(cryptography)", "Key_derivation_function", "Key_exchange", "Key_generation", "Key_escrow"),
    },
    "envelope-encryption-deep": {
        "tags": ["envelope encryption", "key wrapping scheme", "data encryption key", "disk encryption at rest", "symmetric key algorithm"],
        "license": CC_BY_SA,
        "pages": wiki("Key_management", "Key_wrap", "Encryption", "Disk_encryption", "Symmetric-key_algorithm", "Key_derivation_function"),
    },
    "tokenization-data": {
        "tags": ["data tokenization", "payment tokenization", "format preserving tokenization", "pci dss scope reduction", "token vault mapping"],
        "license": CC_BY_SA,
        "pages": wiki("Tokenization_(data_security)", "Data_masking", "Format-preserving_encryption", "Payment_Card_Industry_Data_Security_Standard", "Pseudonymization", "Primary_account_number"),
    },
    "format-preserving-encryption": {
        "tags": ["format preserving encryption", "feistel network cipher", "fpe ff1 ff3", "ciphertext format retention", "aes based fpe"],
        "license": CC_BY_SA,
        "pages": wiki("Format-preserving_encryption", "Block_cipher", "Feistel_cipher", "Advanced_Encryption_Standard", "Tokenization_(data_security)", "Ciphertext"),
    },
    "cloud-security-posture-deep": {
        "tags": ["cloud security posture management", "misconfiguration detection", "compliance drift monitoring", "infrastructure as code scanning", "security baseline enforcement"],
        "license": CC_BY_SA,
        "pages": wiki("Cloud_computing_security", "Security_controls", "Regulatory_compliance", "Configuration_management", "Infrastructure_as_code", "Cloud_computing"),
    },
    "cspm-tools": {
        "tags": ["cspm tooling", "cloud misconfiguration scanning", "posture compliance checks", "cloud attack surface", "vulnerability posture assessment"],
        "license": CC_BY_SA,
        "pages": wiki("Cloud_computing_security", "Security_controls", "Vulnerability_management", "Configuration_management", "Regulatory_compliance", "Attack_surface"),
    },
    "cnapp": {
        "tags": ["cloud native application protection", "cnapp platform", "container application security", "devsecops integration", "cloud workload vulnerability"],
        "license": CC_BY_SA,
        "pages": wiki("Cloud_computing_security", "Application_security", "Cloud_computing", "DevOps", "Vulnerability_(computing)", "Container_(virtualization)"),
    },
    "cwpp": {
        "tags": ["cloud workload protection platform", "workload runtime security", "virtual machine hardening", "container workload defense", "runtime application self protection"],
        "license": CC_BY_SA,
        "pages": wiki("Cloud_computing_security", "Cloud_workload_protection_platform", "Virtual_machine", "Container_(virtualization)", "Endpoint_security", "Runtime_application_self-protection"),
    },
    "cloud-entitlements-ciem": {
        "tags": ["cloud infrastructure entitlement management", "least privilege enforcement", "excessive permission detection", "cloud access governance", "attribute based access control"],
        "license": CC_BY_SA,
        "pages": wiki("Identity_management", "Principle_of_least_privilege", "Access_control", "Cloud_computing_security", "Attribute-based_access_control", "Privilege_(computing)"),
    },
    "container-security-deep": {
        "tags": ["container security", "container image hardening", "namespace isolation", "cgroups resource limits", "kubernetes runtime security"],
        "license": CC_BY_SA,
        "pages": wiki("Container_(virtualization)", "Docker_(software)", "OS-level_virtualization", "Linux_namespaces", "Cgroups", "Kubernetes"),
    },
    "kubernetes-threat-model": {
        "tags": ["kubernetes threat model", "cluster attack surface", "pod security context", "rbac privilege escalation", "microservices attack path"],
        "license": CC_BY_SA,
        "pages": wiki("Kubernetes", "Threat_model", "Container_(virtualization)", "Role-based_access_control", "Attack_surface", "Microservices"),
    },
    "serverless-security": {
        "tags": ["serverless security", "function as a service hardening", "event injection defense", "least privilege function role", "serverless attack surface"],
        "license": CC_BY_SA,
        "pages": wiki("Serverless_computing", "Function_as_a_service", "Cloud_computing_security", "Event-driven_architecture", "Principle_of_least_privilege", "Attack_surface"),
    },
    "api-gateway-security": {
        "tags": ["api gateway security", "api rate limiting", "oauth token validation", "reverse proxy enforcement", "api management policy"],
        "license": CC_BY_SA,
        "pages": wiki("API_management", "Web_API_security", "Rate_limiting", "OAuth", "Application_programming_interface", "Reverse_proxy"),
    },
    "waap": {
        "tags": ["web application and api protection", "web application firewall", "owasp top ten defense", "bot prevention filtering", "cross site scripting defense"],
        "license": CC_BY_SA,
        "pages": wiki("Web_application_firewall", "Application_security", "OWASP", "Denial-of-service_attack", "Bot_prevention", "Cross-site_scripting"),
    },
    "bot-management": {
        "tags": ["bot management", "automated bot detection", "captcha challenge", "credential stuffing defense", "web scraping mitigation"],
        "license": CC_BY_SA,
        "pages": wiki("Internet_bot", "CAPTCHA", "Web_scraping", "Denial-of-service_attack", "Botnet", "Rate_limiting"),
    },
    "ddos-mitigation-deep": {
        "tags": ["ddos mitigation", "volumetric attack scrubbing", "anycast absorption", "blackhole routing defense", "rate limiting protection"],
        "license": CC_BY_SA,
        "pages": wiki("Denial-of-service_attack", "DDoS_mitigation", "Content_delivery_network", "Anycast", "Black_hole_(networking)", "Rate_limiting"),
    },
    "iot-security-deep": {
        "tags": ["iot security", "embedded device hardening", "botnet compromise defense", "mirai botnet mitigation", "over the air update"],
        "license": CC_BY_SA,
        "pages": wiki("Internet_of_things", "Computer_security", "Botnet", "Embedded_system", "Mirai_(malware)", "Over-the-air_update"),
    },
    "ot-security-ics": {
        "tags": ["operational technology security", "industrial control system", "scada protection", "plc security hardening", "critical infrastructure defense"],
        "license": CC_BY_SA,
        "pages": wiki("Operational_technology", "Industrial_control_system", "SCADA", "Programmable_logic_controller", "Distributed_control_system", "Critical_infrastructure_protection"),
    },
    "industrial-control-security-deep": {
        "tags": ["industrial control system security", "scada network defense", "stuxnet class attack", "plc integrity protection", "critical infrastructure resilience"],
        "license": CC_BY_SA,
        "pages": wiki("Industrial_control_system", "SCADA", "Stuxnet", "Programmable_logic_controller", "Remote_terminal_unit", "Critical_infrastructure"),
    },
    "iec-62443-deep": {
        "tags": ["iec 62443 standard", "ics security levels", "defense in depth zones", "operational technology segmentation", "industrial security lifecycle"],
        "license": CC_BY_SA,
        "pages": wiki("IEC_62443", "Industrial_control_system", "Defense_in_depth_(computing)", "Security_level", "Operational_technology", "International_Electrotechnical_Commission"),
    },
    "purdue-model-security": {
        "tags": ["purdue model segmentation", "ics network zones", "ot it demilitarized zone", "level segmentation controls", "scada network isolation"],
        "license": CC_BY_SA,
        "pages": wiki("Purdue_Enterprise_Reference_Architecture", "Industrial_control_system", "SCADA", "Network_segmentation", "Operational_technology", "Demilitarized_zone_(computing)"),
    },
    "network-detection-deep": {
        "tags": ["network detection and response", "deep packet inspection", "network anomaly detection", "traffic behavior analysis", "packet capture analysis"],
        "license": CC_BY_SA,
        "pages": wiki("Intrusion_detection_system", "Network_traffic_measurement", "Deep_packet_inspection", "Anomaly_detection", "Network_behavior_anomaly_detection", "Packet_analyzer"),
    },
    "deception-technology-deep": {
        "tags": ["deception technology", "honeypot deployment", "honeytoken tripwire", "canary token alerting", "network tarpit"],
        "license": CC_BY_SA,
        "pages": wiki("Deception_technology", "Honeypot_(computing)", "Honeytoken", "Intrusion_detection_system", "Tarpit_(networking)", "Canary_trap"),
    },
    "insider-threat": {
        "tags": ["insider threat program", "user behavior analytics", "least privilege enforcement", "separation of duties", "data exfiltration monitoring"],
        "license": CC_BY_SA,
        "pages": wiki("Insider_threat", "Data_loss_prevention_software", "User_behavior_analytics", "Principle_of_least_privilege", "Separation_of_duties", "Access_control"),
    },
    "data-loss-prevention-deep": {
        "tags": ["data loss prevention", "sensitive data classification", "data exfiltration detection", "content inspection policy", "digital watermarking"],
        "license": CC_BY_SA,
        "pages": wiki("Data_loss_prevention_software", "Information_sensitivity", "Data_exfiltration", "Digital_watermarking", "Content-control_software", "Information_security"),
    },
    "casb-security": {
        "tags": ["cloud access security broker", "shadow it discovery", "saas security policy", "cloud dlp enforcement", "cloud access governance"],
        "license": CC_BY_SA,
        "pages": wiki("Cloud_access_security_broker", "Cloud_computing_security", "Software_as_a_service", "Shadow_IT", "Data_loss_prevention_software", "Access_control"),
    },
    "dspm": {
        "tags": ["data security posture management", "sensitive data discovery", "data classification governance", "data access risk", "cloud data protection"],
        "license": CC_BY_SA,
        "pages": wiki("Data_security", "Information_sensitivity", "Data_governance", "Data_classification", "Cloud_computing_security", "Regulatory_compliance"),
    },
}
