"""Deep platform engineering, observability, SRE, and release engineering."""

from .common import CC_BY_SA, wiki

DOMAINS = {
    "distributed-tracing-deep": {
        "tags": ["distributed tracing", "span context propagation", "trace sampling", "request correlation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Tracing_(software)",
            "Observability_(software)",
            "Distributed_computing",
            "Microservices",
            "Application_performance_management",
            "Instrumentation_(computer_programming)",
        ) + [
            "https://opentelemetry.io/docs/concepts/signals/traces/",
            "https://opentelemetry.io/docs/concepts/context-propagation/",
        ],
    },
    "structured-logging": {
        "tags": ["structured logging", "log event schema", "json log lines", "log correlation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Logging_(computing)",
            "Log_file",
            "Syslog",
            "Common_Log_Format",
            "Observability_(software)",
            "JSON",
        ) + [
            "https://opentelemetry.io/docs/concepts/signals/logs/",
        ],
    },
    "log-aggregation": {
        "tags": ["log aggregation", "centralized logging", "log shipping pipeline", "log ingestion"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Log_management",
            "Server_log",
            "Syslog",
            "Elasticsearch",
            "Fluentd",
            "Data_logging",
        ) + [
            "https://opensearch.org/docs/latest/",
            "https://www.elastic.co/guide/en/logstash/current/introduction.html",
        ],
    },
    "metrics-cardinality": {
        "tags": ["metric cardinality", "label dimensions explosion", "time series count", "tag value blowup"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cardinality",
            "Time_series",
            "Time_series_database",
            "Metric_(mathematics)",
            "Dimension_(data_warehouse)",
            "Observability_(software)",
        ) + [
            "https://prometheus.io/docs/practices/naming/",
            "https://prometheus.io/docs/concepts/data_model/",
        ],
    },
    "time-series-databases-obs": {
        "tags": ["time series storage", "metrics retention downsampling", "data point compaction", "monitoring backend"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Time_series_database",
            "Time_series",
            "Column-oriented_DBMS",
            "Data_compression",
            "InfluxDB",
            "RRDtool",
        ) + [
            "https://docs.influxdata.com/influxdb/v2/",
            "https://prometheus.io/docs/prometheus/latest/storage/",
        ],
    },
    "exemplars-metrics": {
        "tags": ["metric exemplar", "trace to metric link", "histogram exemplar", "high resolution sample"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Histogram",
            "Sampling_(statistics)",
            "Percentile",
            "Observability_(software)",
            "Latency_(engineering)",
            "Tracing_(software)",
        ) + [
            "https://opentelemetry.io/docs/specs/otel/metrics/data-model/",
            "https://prometheus.io/docs/prometheus/latest/feature_flags/",
        ],
    },
    "service-level-objectives": {
        "tags": ["service level objective", "service level indicator", "reliability target", "availability threshold"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Service-level_objective",
            "Service-level_agreement",
            "Site_reliability_engineering",
            "High_availability",
            "Reliability_engineering",
            "Quality_of_service",
        ) + [
            "https://sre.google/sre-book/service-level-objectives/",
        ],
    },
    "error-budgets": {
        "tags": ["error budget", "reliability spend policy", "budget burn allowance", "release velocity tradeoff"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Site_reliability_engineering",
            "Service-level_objective",
            "Reliability_engineering",
            "Availability",
            "Risk_management",
            "Failure_rate",
        ) + [
            "https://sre.google/sre-book/embracing-risk/",
            "https://sre.google/workbook/error-budget-policy/",
        ],
    },
    "slo-burn-rate": {
        "tags": ["burn rate alerting", "error budget consumption", "multiwindow burn alert", "fast slow burn"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Site_reliability_engineering",
            "Service-level_objective",
            "Alarm_management",
            "Exponential_decay",
            "Rate_(mathematics)",
            "Reliability_engineering",
        ) + [
            "https://sre.google/workbook/alerting-on-slos/",
        ],
    },
    "golden-signals": {
        "tags": ["four golden signals", "latency traffic errors saturation", "monitoring signals", "service health metrics"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Site_reliability_engineering",
            "Observability_(software)",
            "Latency_(engineering)",
            "Throughput",
            "Network_congestion",
            "Performance_engineering",
        ) + [
            "https://sre.google/sre-book/monitoring-distributed-systems/",
        ],
    },
    "red-method": {
        "tags": ["rate errors duration", "request driven monitoring", "service level method", "microservice metrics"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Observability_(software)",
            "Microservices",
            "Latency_(engineering)",
            "Throughput",
            "Application_performance_management",
            "Site_reliability_engineering",
        ) + [
            "https://grafana.com/blog/2018/08/02/the-red-method-how-to-instrument-your-services/",
        ],
    },
    "use-method": {
        "tags": ["utilization saturation errors", "resource driven analysis", "system performance checklist", "bottleneck diagnosis"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Performance_engineering",
            "CPU_time",
            "Load_(computing)",
            "Bottleneck_(software)",
            "Computer_performance",
            "Resource_(computing)",
        ) + [
            "https://www.brendangregg.com/usemethod.html",
        ],
    },
    "apdex-score": {
        "tags": ["apdex index", "application performance index", "user satisfaction score", "response time bucket"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apdex",
            "Application_performance_management",
            "Response_time_(technology)",
            "User_experience",
            "Latency_(engineering)",
            "Quality_of_experience",
        ),
    },
    "synthetic-monitoring-deep": {
        "tags": ["synthetic monitoring", "scripted probe check", "proactive uptime test", "synthetic transaction"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Synthetic_monitoring",
            "Website_monitoring",
            "Application_performance_management",
            "Uptime",
            "Web_performance",
            "Ping_(networking_utility)",
        ) + [
            "https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/",
        ],
    },
    "real-user-monitoring-deep": {
        "tags": ["real user monitoring", "field performance telemetry", "page load timing", "core web vitals capture"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Real_user_monitoring",
            "Web_performance",
            "Application_performance_management",
            "Web_page",
            "User_experience",
            "Web_analytics",
        ) + [
            "https://web.dev/articles/vitals",
        ],
    },
    "profiling-continuous": {
        "tags": ["continuous profiling", "production cpu profile", "sampling profiler", "profile data collection"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Profiling_(computer_programming)",
            "Program_optimization",
            "Sampling_(signal_processing)",
            "Call_stack",
            "Performance_engineering",
            "Software_performance_testing",
        ) + [
            "https://grafana.com/docs/pyroscope/latest/introduction/",
        ],
    },
    "flame-graphs": {
        "tags": ["flame graph", "stack trace visualization", "cpu hotpath chart", "call stack aggregation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Profiling_(computer_programming)",
            "Call_stack",
            "Call_graph",
            "Program_optimization",
            "Data_and_information_visualization",
            "Stack_trace",
        ) + [
            "https://www.brendangregg.com/flamegraphs.html",
        ],
    },
    "ebpf-observability": {
        "tags": ["ebpf tracing", "kernel probe instrumentation", "in kernel observability", "bpf program"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Berkeley_Packet_Filter",
            "Kernel_(operating_system)",
            "Tracing_(software)",
            "System_call",
            "Loadable_kernel_module",
            "Linux_kernel",
        ) + [
            "https://ebpf.io/what-is-ebpf/",
            "https://docs.cilium.io/en/stable/",
        ],
    },
    "service-mesh-deep": {
        "tags": ["service mesh data plane", "mesh control plane", "mutual tls mesh", "east west traffic"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Service_mesh",
            "Microservices",
            "Proxy_server",
            "Mutual_authentication",
            "Load_balancing_(computing)",
            "Control_plane",
        ) + [
            "https://istio.io/latest/docs/concepts/traffic-management/",
            "https://linkerd.io/2/features/",
        ],
    },
    "sidecar-proxy": {
        "tags": ["sidecar proxy pattern", "per pod proxy", "transparent traffic intercept", "sidecar container"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Proxy_server",
            "Reverse_proxy",
            "Microservices",
            "Service_mesh",
            "OS-level_virtualization",
            "Design_pattern",
        ) + [
            "https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/",
        ],
    },
    "envoy-filters": {
        "tags": ["envoy http filter", "listener filter chain", "proxy filter extension", "wasm filter"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Proxy_server",
            "Reverse_proxy",
            "WebAssembly",
            "Load_balancing_(computing)",
            "Middleware",
            "Application_layer",
        ) + [
            "https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http_filters",
            "https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/listeners/network_filter_chain",
        ],
    },
    "traffic-mirroring": {
        "tags": ["traffic mirroring", "request shadowing", "shadow deployment test", "duplicated production traffic"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Port_mirroring",
            "Load_balancing_(computing)",
            "Reverse_proxy",
            "Software_testing",
            "Network_traffic_measurement",
            "Service_mesh",
        ) + [
            "https://istio.io/latest/docs/tasks/traffic-management/mirroring/",
        ],
    },
    "progressive-delivery-deep": {
        "tags": ["progressive delivery", "automated canary analysis", "gradual traffic shift", "release promotion gate"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Continuous_delivery",
            "Software_release_life_cycle",
            "Software_deployment",
            "Feature_toggle",
            "A/B_testing",
            "DevOps",
        ) + [
            "https://argo-rollouts.readthedocs.io/en/stable/",
            "https://flagger.app/",
        ],
    },
    "deployment-strategies": {
        "tags": ["deployment strategy", "rolling update release", "recreate strategy", "zero downtime rollout"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Software_deployment",
            "Deployment_environment",
            "Software_release_life_cycle",
            "Rolling_release",
            "Continuous_deployment",
            "High_availability",
        ) + [
            "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/",
        ],
    },
    "rollback-strategies": {
        "tags": ["deployment rollback", "revision revert", "safe undo release", "roll forward recovery"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Rollback_(data_management)",
            "Software_deployment",
            "Version_control",
            "Software_release_life_cycle",
            "Disaster_recovery",
            "Fault_tolerance",
        ) + [
            "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/",
        ],
    },
    "immutable-infrastructure": {
        "tags": ["immutable infrastructure", "replace not patch", "baked machine image", "phoenix server"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Immutable_object",
            "System_image",
            "Provisioning_(technology)",
            "Infrastructure_as_code",
            "Configuration_management",
            "Virtual_machine",
        ) + [
            "https://developer.hashicorp.com/packer/docs/intro",
        ],
    },
    "infrastructure-drift": {
        "tags": ["configuration drift", "declared versus actual state", "drift detection reconcile", "state divergence"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Configuration_management",
            "Infrastructure_as_code",
            "Software_configuration_management",
            "System_administration",
            "Change_management_(engineering)",
            "Idempotence",
        ) + [
            "https://developer.hashicorp.com/terraform/tutorials/state/resource-drift",
        ],
    },
    "policy-as-code": {
        "tags": ["policy as code", "declarative guardrail rules", "compliance automation", "policy enforcement engine"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Infrastructure_as_code",
            "Policy",
            "Regulatory_compliance",
            "Access_control",
            "Governance",
            "Rule-based_system",
        ) + [
            "https://www.openpolicyagent.org/docs/latest/",
        ],
    },
    "opa-rego-policy": {
        "tags": ["open policy agent", "rego policy language", "declarative authorization query", "policy decision point"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Access_control",
            "Authorization",
            "Declarative_programming",
            "Datalog",
            "Rule-based_system",
            "Attribute-based_access_control",
        ) + [
            "https://www.openpolicyagent.org/docs/latest/policy-language/",
            "https://www.openpolicyagent.org/docs/latest/policy-reference/",
        ],
    },
    "admission-control-k8s": {
        "tags": ["admission controller", "validating admission webhook", "mutating webhook", "request admission gate"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "Webhook",
            "Access_control",
            "API",
            "Orchestration_(computing)",
            "Middleware",
        ) + [
            "https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/",
            "https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/",
        ],
    },
    "cluster-autoscaling": {
        "tags": ["cluster autoscaler", "node pool scaling", "capacity provisioning nodes", "scale to zero nodes"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Autoscaling",
            "Kubernetes",
            "Provisioning_(technology)",
            "Cloud_computing",
            "Load_balancing_(computing)",
            "Elasticity_(cloud_computing)",
        ) + [
            "https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/",
        ],
    },
    "horizontal-pod-autoscaling": {
        "tags": ["horizontal pod autoscaler", "replica count scaling", "metric driven scale out", "target utilization scaling"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Autoscaling",
            "Kubernetes",
            "Load_balancing_(computing)",
            "Scalability",
            "Elasticity_(cloud_computing)",
            "Control_theory",
        ) + [
            "https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/",
        ],
    },
    "vertical-pod-autoscaling": {
        "tags": ["vertical pod autoscaler", "resource request tuning", "right sizing workloads", "recommended limits"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Autoscaling",
            "Kubernetes",
            "Scalability",
            "Resource_management_(computing)",
            "Memory_management",
            "Capacity_management",
        ) + [
            "https://kubernetes.io/docs/concepts/workloads/autoscaling/",
        ],
    },
    "resource-quotas-k8s": {
        "tags": ["resource quota", "namespace resource cap", "limit range default", "aggregate consumption limit"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "Resource_management_(computing)",
            "Multitenancy",
            "Quota",
            "Scheduling_(computing)",
            "Namespace",
        ) + [
            "https://kubernetes.io/docs/concepts/policy/resource-quotas/",
            "https://kubernetes.io/docs/concepts/policy/limit-range/",
        ],
    },
    "pod-disruption-budgets": {
        "tags": ["pod disruption budget", "voluntary disruption limit", "minimum available replicas", "graceful eviction guard"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "High_availability",
            "Fault_tolerance",
            "Reliability_engineering",
            "Availability",
            "Scheduling_(computing)",
        ) + [
            "https://kubernetes.io/docs/concepts/workloads/pods/disruptions/",
            "https://kubernetes.io/docs/tasks/run-application/configure-pdb/",
        ],
    },
    "node-affinity": {
        "tags": ["node affinity rules", "pod placement scheduling", "affinity anti affinity", "topology spread constraint"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "Scheduling_(computing)",
            "Load_balancing_(computing)",
            "Constraint_satisfaction",
            "Network_topology",
            "Bin_packing_problem",
        ) + [
            "https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/",
        ],
    },
    "taints-tolerations": {
        "tags": ["node taint", "pod toleration", "repel schedule constraint", "dedicated node isolation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "Scheduling_(computing)",
            "Resource_management_(computing)",
            "Multitenancy",
            "Fault_tolerance",
            "Orchestration_(computing)",
        ) + [
            "https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/",
        ],
    },
    "kubernetes-operators": {
        "tags": ["kubernetes operator", "operator reconcile loop", "domain specific controller", "operator pattern"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "Control_loop",
            "Automation",
            "State_machine",
            "Declarative_programming",
            "Software_agent",
        ) + [
            "https://kubernetes.io/docs/concepts/extend-kubernetes/operator/",
            "https://sdk.operatorframework.io/docs/",
        ],
    },
    "custom-resource-definitions": {
        "tags": ["custom resource definition", "extend kubernetes api", "declarative crd schema", "aggregated api server"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "API",
            "Schema",
            "Declarative_programming",
            "Extensibility",
            "Data_validation",
        ) + [
            "https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/",
            "https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/",
        ],
    },
    "kubernetes-controllers": {
        "tags": ["controller reconcile", "desired state loop", "informer watch cache", "control loop convergence"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "Control_loop",
            "Control_theory",
            "Cache_(computing)",
            "Event-driven_programming",
            "Idempotence",
        ) + [
            "https://kubernetes.io/docs/concepts/architecture/controller/",
        ],
    },
    "gitops-workflows": {
        "tags": ["gitops workflow", "git as source of truth", "pull based reconciliation", "declarative delivery"],
        "license": CC_BY_SA,
        "pages": wiki(
            "DevOps",
            "Version_control",
            "Continuous_delivery",
            "Infrastructure_as_code",
            "Control_plane",
            "Application_lifecycle_management",
        ) + [
            "https://argo-cd.readthedocs.io/en/stable/core_concepts/",
            "https://fluxcd.io/flux/concepts/",
        ],
    },
    "secrets-management-ops": {
        "tags": ["secrets management", "credential lifecycle rotation", "encrypted secret storage", "dynamic secret lease"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Key_management",
            "Secret_sharing",
            "Encryption",
            "Access_control",
            "Public_key_infrastructure",
            "Hardware_security_module",
        ) + [
            "https://developer.hashicorp.com/vault/docs/secrets",
            "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html",
        ],
    },
    "external-secrets": {
        "tags": ["external secrets operator", "secret store sync", "provider backed secret", "secret synchronization"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Key_management",
            "Kubernetes",
            "Encryption",
            "Access_control",
            "Cloud_computing_security",
            "Identity_management",
        ) + [
            "https://external-secrets.io/latest/",
            "https://external-secrets.io/latest/introduction/overview/",
        ],
    },
    "sealed-secrets": {
        "tags": ["sealed secrets", "encrypted secret in git", "asymmetric secret sealing", "controller decrypt"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Public-key_cryptography",
            "Encryption",
            "Key_management",
            "Kubernetes",
            "Version_control",
            "Hybrid_cryptosystem",
        ) + [
            "https://github.com/bitnami-labs/sealed-secrets",
        ],
    },
    "backstage-idp": {
        "tags": ["backstage developer portal", "software catalog", "service metadata registry", "portal plugin"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Web_portal",
            "Software_documentation",
            "Metadata",
            "Cloud_Native_Computing_Foundation",
            "Service_catalog",
            "Application_lifecycle_management",
        ) + [
            "https://backstage.io/docs/overview/what-is-backstage",
            "https://backstage.io/docs/features/software-catalog/",
        ],
    },
    "internal-developer-platform": {
        "tags": ["internal developer platform", "self service infrastructure", "platform abstraction layer", "paved road tooling"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Platform_as_a_service",
            "DevOps",
            "Self-service",
            "Abstraction_(computer_science)",
            "Software_as_a_service",
            "Application_lifecycle_management",
        ) + [
            "https://internaldeveloperplatform.org/what-is-an-internal-developer-platform/",
        ],
    },
    "platform-engineering": {
        "tags": ["platform engineering", "cognitive load reduction", "product mindset infrastructure", "platform team"],
        "license": CC_BY_SA,
        "pages": wiki(
            "DevOps",
            "Software_engineering",
            "Systems_engineering",
            "Cognitive_load",
            "Platform_as_a_service",
            "Site_reliability_engineering",
        ) + [
            "https://platformengineering.org/blog/what-is-platform-engineering",
        ],
    },
    "developer-experience": {
        "tags": ["developer experience", "inner loop feedback", "friction reduction tooling", "developer productivity"],
        "license": CC_BY_SA,
        "pages": wiki(
            "User_experience",
            "Software_development",
            "Programmer",
            "Usability",
            "Software_development_process",
            "Productivity",
        ) + [
            "https://backstage.io/docs/overview/what-is-backstage",
        ],
    },
    "golden-paths": {
        "tags": ["golden path template", "paved road workflow", "opinionated scaffold", "recommended project setup"],
        "license": CC_BY_SA,
        "pages": wiki(
            "DevOps",
            "Software_development_process",
            "Best_practice",
            "Template_(software_engineering)",
            "Standardization",
            "Reference_architecture",
        ) + [
            "https://backstage.io/docs/features/software-templates/",
        ],
    },
    "dora-metrics": {
        "tags": ["dora metrics", "deployment frequency lead time", "change failure rate", "delivery performance measure"],
        "license": CC_BY_SA,
        "pages": wiki(
            "DevOps",
            "Continuous_delivery",
            "Software_metric",
            "Performance_indicator",
            "Lead_time",
            "Software_deployment",
        ) + [
            "https://dora.dev/guides/dora-metrics-four-keys/",
        ],
    },
    "value-stream-management": {
        "tags": ["value stream mapping", "flow efficiency waste", "end to end delivery flow", "value stream metrics"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Value-stream_mapping",
            "Lean_software_development",
            "Lean_manufacturing",
            "Kanban_(development)",
            "Business_process",
            "Continuous_delivery",
        ),
    },
    "incident-management-deep": {
        "tags": ["incident management", "incident command structure", "severity classification", "incident response coordination"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Incident_management",
            "Incident_Command_System",
            "IT_service_management",
            "Site_reliability_engineering",
            "Escalation",
            "Root_cause_analysis",
        ) + [
            "https://sre.google/sre-book/managing-incidents/",
        ],
    },
    "blameless-postmortems": {
        "tags": ["blameless postmortem", "incident retrospective learning", "root cause writeup", "corrective action tracking"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Postmortem_documentation",
            "Root_cause_analysis",
            "Site_reliability_engineering",
            "Learning_organization",
            "Safety_culture",
            "Just_culture",
        ) + [
            "https://sre.google/sre-book/postmortem-culture/",
        ],
    },
    "on-call-practices": {
        "tags": ["on call rotation", "pager alert fatigue", "escalation policy handoff", "sustainable on call"],
        "license": CC_BY_SA,
        "pages": wiki(
            "On-call",
            "Site_reliability_engineering",
            "Alarm_management",
            "Occupational_burnout",
            "Shift_work",
            "Incident_management",
        ) + [
            "https://sre.google/sre-book/being-on-call/",
        ],
    },
    "runbook-automation": {
        "tags": ["runbook automation", "operational procedure script", "automated remediation", "playbook execution"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Runbook",
            "Automation",
            "IT_service_management",
            "Scripting_language",
            "Standard_operating_procedure",
            "Self-healing",
        ) + [
            "https://sre.google/workbook/eliminating-toil/",
        ],
    },
    "capacity-planning": {
        "tags": ["capacity planning", "demand forecasting headroom", "resource provisioning forecast", "load projection model"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Capacity_planning",
            "Capacity_management",
            "Forecasting",
            "Scalability",
            "Queueing_theory",
            "Little's_law",
        ) + [
            "https://sre.google/sre-book/software-engineering-in-sre/",
        ],
    },
    "load-testing-deep": {
        "tags": ["load testing", "stress spike soak test", "throughput saturation test", "performance test workload"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Load_testing",
            "Software_performance_testing",
            "Stress_testing_(software)",
            "Scalability_testing",
            "Soak_testing",
            "Benchmark_(computing)",
        ) + [
            "https://k6.io/docs/",
            "https://jmeter.apache.org/usermanual/get-started.html",
        ],
    },
    "cost-optimization-cloud": {
        "tags": ["cloud cost optimization", "rightsizing spend reduction", "reserved capacity commitment", "idle resource cleanup"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cloud_computing",
            "Total_cost_of_ownership",
            "Utility_computing",
            "Elasticity_(cloud_computing)",
            "Resource_management_(computing)",
            "Pay-as-you-go",
        ) + [
            "https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html",
        ],
    },
    "finops-practices": {
        "tags": ["finops discipline", "cloud spend accountability", "cost allocation showback", "unit economics cloud"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cloud_computing",
            "Management_accounting",
            "Cost_accounting",
            "Chargeback",
            "Budget",
            "Total_cost_of_ownership",
        ) + [
            "https://www.finops.org/introduction/what-is-finops/",
        ],
    },
}
