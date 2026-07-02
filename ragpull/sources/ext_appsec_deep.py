"""Deep defensive application security and applied cryptography."""

from .common import CC_BY_SA, wiki

# Non-Wikipedia static sources, each verified live (HTTP 200) at authoring time.
# OWASP Cheat Sheet Series serves clean static HTML under CC-BY-SA:
#   cheatsheetseries.owasp.org
# OWASP www-community pages and the Web Security Testing Guide are static HTML too.
OWASP_CS = "https://cheatsheetseries.owasp.org/cheatsheets/"
OWASP_COMM = "https://owasp.org/www-community/"

DOMAINS = {
    "ssrf-defense": {
        "tags": [
            "server-side request forgery",
            "ssrf mitigation",
            "url validation defense",
            "outbound request filtering",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Server-side_request_forgery",
            "Input_validation",
            "Whitelisting",
            "Cloud_computing_security",
            "Private_network",
        )
        + [
            OWASP_CS + "Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html",
            OWASP_CS + "Input_Validation_Cheat_Sheet.html",
        ],
    },
    "xxe-prevention": {
        "tags": [
            "xml external entity",
            "xxe prevention",
            "xml parser hardening",
            "document type definition",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "XML_external_entity_attack",
            "Document_type_definition",
            "XML",
            "Billion_laughs_attack",
        )
        + [
            OWASP_CS + "XML_External_Entity_Prevention_Cheat_Sheet.html",
            OWASP_CS + "XML_Security_Cheat_Sheet.html",
        ],
    },
    "insecure-deserialization": {
        "tags": [
            "insecure deserialization",
            "object serialization risk",
            "deserialization gadget chain",
            "untrusted data marshalling",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Serialization",
            "Marshalling_(computer_science)",
            "Object_(computer_science)",
            "Java_(programming_language)",
        )
        + [
            OWASP_CS + "Deserialization_Cheat_Sheet.html",
            OWASP_COMM + "vulnerabilities/Deserialization_of_untrusted_data",
        ],
    },
    "prototype-pollution": {
        "tags": [
            "prototype pollution",
            "javascript prototype chain",
            "object property injection",
            "recursive merge hazard",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Prototype-based_programming",
            "JavaScript",
            "Object_(computer_science)",
            "Inheritance_(object-oriented_programming)",
        )
        + [
            OWASP_CS + "Prototype_Pollution_Prevention_Cheat_Sheet.html",
            OWASP_CS + "Nodejs_Security_Cheat_Sheet.html",
        ],
    },
    "path-traversal-defense": {
        "tags": [
            "directory traversal",
            "path traversal defense",
            "canonical path resolution",
            "file access control",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Directory_traversal_attack",
            "Path_(computing)",
            "Canonicalization",
            "Symbolic_link",
        )
        + [
            OWASP_CS + "File_Upload_Cheat_Sheet.html",
            OWASP_COMM + "attacks/Path_Traversal",
        ],
    },
    "open-redirect-defense": {
        "tags": [
            "open redirect vulnerability",
            "unvalidated redirect",
            "url forwarding abuse",
            "redirect allowlist",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "URL_redirection",
            "Phishing",
            "Uniform_Resource_Locator",
            "HTTP_302",
            "List_of_HTTP_status_codes",
        )
        + [
            OWASP_CS + "Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html",
        ],
    },
    "http-request-smuggling": {
        "tags": [
            "http request smuggling",
            "content length transfer encoding",
            "proxy desynchronization",
            "request boundary parsing",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "HTTP_request_smuggling",
            "Chunked_transfer_encoding",
            "Proxy_server",
            "Hypertext_Transfer_Protocol",
            "Reverse_proxy",
            "HTTP_persistent_connection",
        )
        + [
            OWASP_CS + "HTTP_Headers_Cheat_Sheet.html",
        ],
    },
    "cache-poisoning-defense": {
        "tags": [
            "web cache poisoning",
            "http cache key",
            "cache deception defense",
            "unkeyed input handling",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Web_cache",
            "Cache_(computing)",
            "Content_delivery_network",
            "Cache_stampede",
        )
        + [
            OWASP_CS + "HTTP_Headers_Cheat_Sheet.html",
            OWASP_COMM + "attacks/Cache_Poisoning",
        ],
    },
    "mass-assignment-defense": {
        "tags": [
            "mass assignment vulnerability",
            "object binding allowlist",
            "auto binding overposting",
            "parameter binding control",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Object-relational_mapping",
            "Data_binding",
            "Model%E2%80%93view%E2%80%93controller",
            "Ruby_on_Rails",
            "Create,_read,_update_and_delete",
        )
        + [
            OWASP_CS + "Mass_Assignment_Cheat_Sheet.html",
        ],
    },
    "race-condition-security": {
        "tags": [
            "time of check time of use",
            "race condition security",
            "concurrency vulnerability",
            "atomic operation defense",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Race_condition",
            "Time-of-check_to_time-of-use",
            "Linearizability",
            "File_locking",
            "Mutual_exclusion",
            "Idempotence",
        )
        + [
            OWASP_COMM + "vulnerabilities/Race_condition",
        ],
    },
    "business-logic-flaws": {
        "tags": [
            "business logic vulnerability",
            "application workflow abuse",
            "logic flaw exploitation",
            "state machine validation",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Business_logic",
            "Workflow",
            "Finite-state_machine",
            "Application_security",
        )
        + [
            OWASP_COMM + "vulnerabilities/Business_logic_vulnerability",
            OWASP_CS + "Abuse_Case_Cheat_Sheet.html",
        ],
    },
    "authorization-bypass-defense": {
        "tags": [
            "broken access control",
            "authorization bypass defense",
            "privilege escalation prevention",
            "forced browsing control",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Authorization",
            "Privilege_escalation",
            "Access_control",
            "Confused_deputy_problem",
        )
        + [
            OWASP_CS + "Authorization_Cheat_Sheet.html",
            OWASP_CS + "Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html",
        ],
    },
    "idor-prevention": {
        "tags": [
            "insecure direct object reference",
            "idor prevention",
            "object reference authorization",
            "indirect reference map",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Access_control",
            "Authorization",
            "Identifier",
            "Universally_unique_identifier",
            "Vertical_and_horizontal",
        )
        + [
            OWASP_CS + "Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html",
        ],
    },
    "jwt-security-pitfalls": {
        "tags": [
            "json web token",
            "jwt security pitfalls",
            "token signature validation",
            "algorithm confusion defense",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "JSON_Web_Token",
            "JSON_Web_Signature",
            "HMAC",
            "Digital_signature",
            "Replay_attack",
        )
        + [
            OWASP_CS + "JSON_Web_Token_Cheat_Sheet.html",
        ],
    },
    "oauth-security-hardening": {
        "tags": [
            "oauth security hardening",
            "authorization code flow",
            "pkce proof key",
            "token leakage defense",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "OAuth",
            "OpenID_Connect",
            "Authorization",
            "PKCE",
        )
        + [
            "https://oauth.net/2/",
            "https://datatracker.ietf.org/doc/html/rfc6749",
        ],
    },
    "saml-security": {
        "tags": [
            "security assertion markup language",
            "saml assertion validation",
            "xml signature wrapping defense",
            "identity federation security",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Security_Assertion_Markup_Language",
            "SAML_2.0",
            "XML_Signature",
            "Federated_identity",
            "OpenID_Connect",
        )
        + [
            OWASP_CS + "SAML_Security_Cheat_Sheet.html",
        ],
    },
    "session-fixation-defense": {
        "tags": [
            "session fixation defense",
            "session identifier rotation",
            "session hijacking prevention",
            "session lifecycle management",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Session_fixation",
            "Session_(computer_science)",
            "Session_hijacking",
            "HTTP_cookie",
            "Multi-factor_authentication",
        )
        + [
            OWASP_CS + "Session_Management_Cheat_Sheet.html",
        ],
    },
    "clickjacking-prevention": {
        "tags": [
            "clickjacking defense",
            "ui redress attack",
            "frame ancestors policy",
            "frame busting technique",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Clickjacking",
            "Framekiller",
            "Framing_(World_Wide_Web)",
            "HTML_element",
            "Web_browser",
        )
        + [
            OWASP_CS + "Clickjacking_Defense_Cheat_Sheet.html",
        ],
    },
    "cors-misconfiguration": {
        "tags": [
            "cross-origin resource sharing",
            "cors misconfiguration",
            "origin allowlist policy",
            "preflight request handling",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cross-origin_resource_sharing",
            "Same-origin_policy",
            "Web_resource",
            "XMLHttpRequest",
            "Web_browser_engine",
        )
        + [
            OWASP_CS + "HTML5_Security_Cheat_Sheet.html",
        ],
    },
    "subdomain-takeover": {
        "tags": [
            "subdomain takeover",
            "dangling dns record",
            "orphaned cname defense",
            "domain hijacking prevention",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Domain_hijacking",
            "CNAME_record",
            "Domain_Name_System",
            "Fully_qualified_domain_name",
            "Cloud_storage",
        )
        + [
            "https://owasp.org/www-project-web-security-testing-guide/",
        ],
    },
    "dns-rebinding-defense": {
        "tags": [
            "dns rebinding defense",
            "same-origin policy bypass",
            "dns pinning mitigation",
            "internal network exposure",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "DNS_rebinding",
            "Same-origin_policy",
            "Domain_Name_System",
            "Time_to_live",
            "IP_address",
        )
        + [
            OWASP_COMM + "attacks/Server_Side_Request_Forgery",
        ],
    },
    "dependency-confusion": {
        "tags": [
            "dependency confusion attack",
            "package namespace hijack",
            "internal registry precedence",
            "supply chain package pinning",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Supply_chain_attack",
            "Package_manager",
            "Software_repository",
            "Namespace",
            "Npm",
        )
        + [
            OWASP_CS + "Vulnerable_Dependency_Management_Cheat_Sheet.html",
        ],
    },
    "typosquatting-defense": {
        "tags": [
            "typosquatting defense",
            "package name confusion",
            "malicious lookalike package",
            "registry namespace protection",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Typosquatting",
            "Supply_chain_attack",
            "Package_manager",
            "Brandjacking",
            "Cybersquatting",
            "Levenshtein_distance",
        )
        + [
            OWASP_CS + "Vulnerable_Dependency_Management_Cheat_Sheet.html",
        ],
    },
    "secure-headers": {
        "tags": [
            "http security headers",
            "response header hardening",
            "referrer policy header",
            "permissions policy header",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "List_of_HTTP_header_fields",
            "HTTP_header",
            "HTTP_referer",
            "X-Frame-Options",
            "Cross-site_scripting",
        )
        + [
            OWASP_CS + "HTTP_Headers_Cheat_Sheet.html",
        ],
    },
    "cookie-security-attributes": {
        "tags": [
            "http cookie attributes",
            "samesite cookie flag",
            "httponly secure cookie",
            "cookie prefix hardening",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "HTTP_cookie",
            "Session_hijacking",
            "Cross-site_request_forgery",
            "Secure_cookie",
            "Web_storage",
        )
        + [
            OWASP_CS + "Cookie_Theft_Mitigation_Cheat_Sheet.html",
        ],
    },
    "csp-hardening": {
        "tags": [
            "content security policy",
            "csp hardening",
            "nonce based script policy",
            "inline script mitigation",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Content_Security_Policy",
            "Cross-site_scripting",
            "Same-origin_policy",
            "Cryptographic_nonce",
            "Eval",
        )
        + [
            OWASP_CS + "Content_Security_Policy_Cheat_Sheet.html",
        ],
    },
    "sri-integrity": {
        "tags": [
            "subresource integrity",
            "sri hash verification",
            "third party script integrity",
            "content tampering defense",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Subresource_Integrity",
            "Cryptographic_hash_function",
            "Content_delivery_network",
            "Base64",
            "SHA-2",
        )
        + [
            OWASP_CS + "Third_Party_Javascript_Management_Cheat_Sheet.html",
        ],
    },
    "tls-configuration-hardening": {
        "tags": [
            "tls configuration hardening",
            "cipher suite selection",
            "perfect forward secrecy",
            "protocol version deprecation",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Transport_Layer_Security",
            "Cipher_suite",
            "Forward_secrecy",
            "Server_Name_Indication",
            "HTTPS",
            "OpenSSL",
        )
        + [
            OWASP_CS + "Transport_Layer_Security_Cheat_Sheet.html",
        ],
    },
    "certificate-pinning": {
        "tags": [
            "certificate pinning",
            "public key pinning",
            "man in the middle defense",
            "trust anchor validation",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "HTTP_Public_Key_Pinning",
            "Public_key_certificate",
            "Man-in-the-middle_attack",
            "Certificate_authority",
            "Trust_on_first_use",
        )
        + [
            OWASP_CS + "Pinning_Cheat_Sheet.html",
        ],
    },
    "hsts-preload": {
        "tags": [
            "http strict transport security",
            "hsts preload list",
            "ssl stripping defense",
            "https enforcement policy",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "HTTP_Strict_Transport_Security",
            "HTTPS",
            "Man-in-the-middle_attack",
            "Moxie_Marlinspike",
            "Downgrade_attack",
        )
        + [
            "https://hstspreload.org/",
        ],
    },
    "secure-random-generation": {
        "tags": [
            "cryptographically secure random",
            "random number generation",
            "entropy source seeding",
            "deterministic random bit generator",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cryptographically_secure_pseudorandom_number_generator",
            "Random_number_generation",
            "Entropy_(computing)",
            "/dev/random",
            "Hardware_random_number_generator",
        )
        + [
            OWASP_CS + "Cryptographic_Storage_Cheat_Sheet.html",
        ],
    },
    "key-derivation-functions": {
        "tags": [
            "key derivation function",
            "password based key derivation",
            "kdf salt stretching",
            "hkdf extract expand",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Key_derivation_function",
            "PBKDF2",
            "HKDF",
            "Key_stretching",
            "Salt_(cryptography)",
        )
        + [
            OWASP_CS + "Key_Management_Cheat_Sheet.html",
        ],
    },
    "password-hashing-argon2": {
        "tags": [
            "argon2 password hashing",
            "memory hard function",
            "password storage hashing",
            "salt and pepper hashing",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Argon2",
            "Bcrypt",
            "Scrypt",
            "Key_derivation_function",
            "Rainbow_table",
        )
        + [
            OWASP_CS + "Password_Storage_Cheat_Sheet.html",
        ],
    },
    "message-authentication-codes": {
        "tags": [
            "message authentication code",
            "hmac construction",
            "keyed hash integrity",
            "constant time comparison",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Message_authentication_code",
            "HMAC",
            "Poly1305",
            "Timing_attack",
            "Length_extension_attack",
        )
        + [
            OWASP_CS + "Cryptographic_Storage_Cheat_Sheet.html",
        ],
    },
    "authenticated-encryption": {
        "tags": [
            "authenticated encryption",
            "aead cipher mode",
            "galois counter mode",
            "encrypt then mac",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Authenticated_encryption",
            "Galois/Counter_Mode",
            "ChaCha20-Poly1305",
            "Block_cipher_mode_of_operation",
            "Padding_oracle_attack",
        )
        + [
            OWASP_CS + "Cryptographic_Storage_Cheat_Sheet.html",
        ],
    },
    "nonce-management": {
        "tags": [
            "cryptographic nonce",
            "initialization vector reuse",
            "nonce uniqueness invariant",
            "counter mode nonce",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cryptographic_nonce",
            "Initialization_vector",
            "Galois/Counter_Mode",
            "Stream_cipher_attacks",
            "Salsa20",
        )
        + [
            OWASP_CS + "Cryptographic_Storage_Cheat_Sheet.html",
        ],
    },
    "key-rotation": {
        "tags": [
            "cryptographic key rotation",
            "key lifecycle management",
            "crypto period policy",
            "re-encryption strategy",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Key_management",
            "Key_(cryptography)",
            "Cryptoperiod",
            "Forward_secrecy",
            "Key_size",
        )
        + [
            OWASP_CS + "Key_Management_Cheat_Sheet.html",
        ],
    },
    "envelope-encryption": {
        "tags": [
            "envelope encryption",
            "data encryption key wrapping",
            "key encryption key",
            "key hierarchy management",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Key_management",
            "Key_Wrap",
            "Encryption",
            "Amazon_Web_Services",
            "Cryptographic_key_types",
        )
        + [
            OWASP_CS + "Key_Management_Cheat_Sheet.html",
        ],
    },
    "secrets-vaulting": {
        "tags": [
            "secrets vaulting",
            "dynamic secret leasing",
            "secret zero problem",
            "credential injection runtime",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Password_manager",
            "Privileged_access_management",
            "Environment_variable",
            "Credential",
            "Access_token",
        )
        + [
            OWASP_CS + "Secrets_Management_Cheat_Sheet.html",
        ],
    },
    "hardware-backed-keystore": {
        "tags": [
            "hardware backed keystore",
            "secure key storage element",
            "trusted platform module keystore",
            "non exportable private key",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Trusted_Platform_Module",
            "Secure_cryptoprocessor",
            "Key_management",
            "Smart_card",
            "Public-key_cryptography",
        )
        + [
            OWASP_CS + "Cryptographic_Storage_Cheat_Sheet.html",
        ],
    },
    "secure-enclave-usage": {
        "tags": [
            "secure enclave usage",
            "hardware isolated key storage",
            "biometric protected key",
            "trusted execution keystore",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apple_A11",
            "Trusted_execution_environment",
            "Secure_cryptoprocessor",
            "Biometrics",
            "IOS",
        )
        + [
            OWASP_CS + "Mobile_Application_Security_Cheat_Sheet.html",
        ],
    },
    "threat-detection-appsec": {
        "tags": [
            "application layer threat detection",
            "attack detection instrumentation",
            "security logging monitoring",
            "runtime application self protection",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Runtime_application_self-protection",
            "Application_security",
            "Anomaly_detection",
            "Intrusion_detection_system",
            "Security_information_and_event_management",
        )
        + [
            OWASP_CS + "Logging_Cheat_Sheet.html",
        ],
    },
    "waf-rule-tuning": {
        "tags": [
            "web application firewall tuning",
            "waf rule set",
            "false positive reduction",
            "virtual patching rule",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Web_application_firewall",
            "ModSecurity",
            "OWASP",
            "Application_firewall",
            "Regular_expression",
        )
        + [
            OWASP_CS + "Virtual_Patching_Cheat_Sheet.html",
        ],
    },
    "api-security-testing": {
        "tags": [
            "api security testing",
            "rest api abuse defense",
            "api rate limiting",
            "broken object level authorization",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Web_API_security",
            "Representational_state_transfer",
            "Rate_limiting",
            "API",
            "Hypertext_Transfer_Protocol",
        )
        + [
            OWASP_CS + "REST_Security_Cheat_Sheet.html",
        ],
    },
    "graphql-security": {
        "tags": [
            "graphql security",
            "query depth limiting",
            "introspection hardening",
            "resolver authorization",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "GraphQL",
            "Query_language",
            "Denial-of-service_attack",
            "Application_programming_interface",
            "JSON",
        )
        + [
            OWASP_CS + "GraphQL_Cheat_Sheet.html",
        ],
    },
    "mobile-app-security": {
        "tags": [
            "mobile application security",
            "mobile secure storage",
            "app transport security",
            "reverse engineering resistance",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Mobile_security",
            "Mobile_app",
            "Application_security",
            "Obfuscation_(software)",
            "Mobile_operating_system",
        )
        + [
            OWASP_CS + "Mobile_Application_Security_Cheat_Sheet.html",
        ],
    },
    "android-app-hardening": {
        "tags": [
            "android application hardening",
            "android keystore system",
            "android permission model",
            "network security config",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Android_(operating_system)",
            "Android_software_development",
            "Sandbox_(computer_security)",
            "Application_permissions",
            "Trusted_execution_environment",
        )
        + [
            OWASP_CS + "Mobile_Application_Security_Cheat_Sheet.html",
        ],
    },
    "ios-app-hardening": {
        "tags": [
            "ios application hardening",
            "ios keychain services",
            "app sandbox entitlements",
            "jailbreak detection defense",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "IOS",
            "App_Store_(Apple)",
            "Sandbox_(computer_security)",
            "Keychain_(software)",
            "Public-key_cryptography",
        )
        + [
            OWASP_CS + "Mobile_Application_Security_Cheat_Sheet.html",
        ],
    },
    "container-image-hardening": {
        "tags": [
            "container image hardening",
            "minimal base image",
            "rootless container runtime",
            "distroless image build",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "OS-level_virtualization",
            "Docker_(software)",
            "Open_Container_Initiative",
            "Principle_of_least_privilege",
            "Cgroups",
        )
        + [
            OWASP_CS + "Docker_Security_Cheat_Sheet.html",
        ],
    },
    "kubernetes-security-hardening": {
        "tags": [
            "kubernetes security hardening",
            "pod security standards",
            "kubernetes network policy",
            "admission controller policy",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "OS-level_virtualization",
            "Role-based_access_control",
            "Microservices",
            "Provisioning_(technology)",
        )
        + [
            OWASP_CS + "Kubernetes_Security_Cheat_Sheet.html",
        ],
    },
    "iac-security-scanning": {
        "tags": [
            "infrastructure as code security",
            "iac misconfiguration scanning",
            "policy as code enforcement",
            "declarative provisioning audit",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Infrastructure_as_code",
            "Terraform_(software)",
            "Configuration_management",
            "DevSecOps",
            "Ansible_(software)",
        )
        + [
            OWASP_CS + "Infrastructure_as_Code_Security_Cheat_Sheet.html",
        ],
    },
    "sast-dast-integration": {
        "tags": [
            "static application security testing",
            "dynamic application security testing",
            "interactive application security testing",
            "security pipeline integration",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Static_application_security_testing",
            "Dynamic_application_security_testing",
            "Interactive_application_security_testing",
            "DevSecOps",
            "CI/CD",
        )
        + [
            OWASP_CS + "Vulnerability_Disclosure_Cheat_Sheet.html",
        ],
    },
    "software-composition-analysis": {
        "tags": [
            "software composition analysis",
            "open source dependency scanning",
            "known vulnerability detection",
            "transitive dependency audit",
        ],
        "license": CC_BY_SA,
        "pages": wiki(
            "Software_composition_analysis",
            "Open-source_software",
            "Software_bill_of_materials",
            "Common_Vulnerabilities_and_Exposures",
            "Vulnerability_database",
        )
        + [
            OWASP_CS + "Vulnerable_Dependency_Management_Cheat_Sheet.html",
        ],
    },
}
