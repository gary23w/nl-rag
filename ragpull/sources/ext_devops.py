"""DevOps, CI/CD, observability, and container/infra tooling."""

from .common import CC_BY_SA, wiki

DOMAINS = {
    "helm-charts": {
        "tags": ["helm chart", "helm package manager", "kubernetes package", "chart template"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Helm_(package_manager)",
            "Kubernetes",
            "Package_manager",
        ) + [
            "https://helm.sh/docs/",
            "https://helm.sh/docs/topics/charts/",
            "https://helm.sh/docs/intro/using_helm/",
            "https://helm.sh/docs/chart_template_guide/getting_started/",
            "https://helm.sh/docs/topics/charts_hooks/",
        ],
    },
    "prometheus-monitoring": {
        "tags": ["prometheus metrics", "metrics monitoring", "time-series metrics", "promql query"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Prometheus_(software)",
            "Monitoring",
            "Time_series_database",
        ) + [
            "https://prometheus.io/docs/introduction/overview/",
            "https://prometheus.io/docs/concepts/data_model/",
            "https://prometheus.io/docs/prometheus/latest/querying/basics/",
            "https://prometheus.io/docs/prometheus/latest/getting_started/",
            "https://prometheus.io/docs/instrumenting/exporters/",
        ],
    },
    "grafana": {
        "tags": ["grafana dashboard", "metrics dashboard", "data visualization", "observability dashboard"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Grafana",
            "Data_visualization",
            "Dashboard_(computing)",
        ) + [
            "https://grafana.com/docs/grafana/latest/",
            "https://grafana.com/docs/grafana/latest/introduction/",
            "https://grafana.com/docs/grafana/latest/panels-visualizations/",
            "https://grafana.com/docs/grafana/latest/dashboards/",
        ],
    },
    "opentelemetry": {
        "tags": ["opentelemetry instrumentation", "distributed tracing", "observability instrumentation", "telemetry signals"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cloud_Native_Computing_Foundation",
            "Observability_(software)",
            "Tracing_(software)",
            "Telemetry",
        ) + [
            "https://opentelemetry.io/docs/",
            "https://opentelemetry.io/docs/concepts/",
            "https://opentelemetry.io/docs/what-is-opentelemetry/",
            "https://opentelemetry.io/docs/concepts/signals/traces/",
        ],
    },
    "jaeger-tracing": {
        "tags": ["jaeger tracing", "distributed tracing", "trace span", "request tracing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cloud_Native_Computing_Foundation",
            "Tracing_(software)",
            "Observability_(software)",
        ) + [
            "https://www.jaegertracing.io/docs/",
            "https://www.jaegertracing.io/docs/latest/architecture/",
            "https://www.jaegertracing.io/docs/latest/getting-started/",
            "https://www.jaegertracing.io/docs/latest/deployment/",
        ],
    },
    "istio-mesh": {
        "tags": ["istio service mesh", "service mesh", "sidecar proxy", "traffic management"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Service_mesh",
            "Cloud_Native_Computing_Foundation",
            "Microservices",
        ) + [
            "https://istio.io/latest/docs/",
            "https://istio.io/latest/docs/concepts/what-is-istio/",
            "https://istio.io/latest/docs/concepts/traffic-management/",
            "https://istio.io/latest/docs/ops/deployment/architecture/",
        ],
    },
    "linkerd": {
        "tags": ["linkerd service mesh", "service mesh", "cloud native networking", "mesh proxy"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Service_mesh",
            "Cloud_Native_Computing_Foundation",
            "Microservices",
        ) + [
            "https://linkerd.io/2/overview/",
            "https://linkerd.io/2/getting-started/",
            "https://linkerd.io/2/features/",
        ],
    },
    "envoy-proxy": {
        "tags": ["envoy proxy", "edge proxy", "load balancing", "reverse proxy"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Proxy_server",
            "Reverse_proxy",
            "Load_balancing_(computing)",
            "Cloud_Native_Computing_Foundation",
        ) + [
            "https://www.envoyproxy.io/docs/envoy/latest/intro/what_is_envoy",
            "https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/arch_overview",
            "https://www.envoyproxy.io/docs/envoy/latest/intro/intro",
        ],
    },
    "hashicorp-vault": {
        "tags": ["hashicorp vault", "secrets management", "secret sharing", "key management"],
        "license": CC_BY_SA,
        "pages": wiki(
            "HashiCorp",
            "Secret_sharing",
            "Key_management",
        ) + [
            "https://developer.hashicorp.com/vault/docs",
            "https://developer.hashicorp.com/vault/docs/what-is-vault",
            "https://developer.hashicorp.com/vault/docs/concepts",
            "https://developer.hashicorp.com/vault/docs/secrets",
        ],
    },
    "hashicorp-consul": {
        "tags": ["hashicorp consul", "service discovery", "service mesh", "distributed configuration"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Consul_(software)",
            "Service_discovery",
            "HashiCorp",
            "Service_mesh",
        ) + [
            "https://developer.hashicorp.com/consul/docs",
            "https://developer.hashicorp.com/consul/docs/intro",
        ],
    },
    "hashicorp-packer": {
        "tags": ["hashicorp packer", "machine image", "immutable infrastructure", "image builder"],
        "license": CC_BY_SA,
        "pages": wiki(
            "HashiCorp",
            "System_image",
            "Disk_image",
            "Virtual_machine",
        ) + [
            "https://developer.hashicorp.com/packer/docs",
            "https://developer.hashicorp.com/packer/docs/intro",
        ],
    },
    "vagrant": {
        "tags": ["hashicorp vagrant", "development environment", "virtual machine provisioning", "reproducible dev environment"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Vagrant_(software)",
            "VirtualBox",
            "Development_environment_(software_development_process)",
            "HashiCorp",
        ) + [
            "https://developer.hashicorp.com/vagrant/docs",
            "https://developer.hashicorp.com/vagrant/intro",
        ],
    },
    "pulumi": {
        "tags": ["pulumi iac", "infrastructure as code", "cloud provisioning", "declarative infrastructure"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Pulumi",
            "Infrastructure_as_code",
            "Provisioning_(technology)",
        ) + [
            "https://www.pulumi.com/docs/",
            "https://www.pulumi.com/docs/concepts/",
            "https://www.pulumi.com/docs/languages-sdks/",
            "https://www.pulumi.com/docs/using-pulumi/",
        ],
    },
    "argocd": {
        "tags": ["argo cd", "gitops continuous delivery", "kubernetes continuous delivery", "declarative deployment"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Continuous_delivery",
            "DevOps",
            "Cloud_Native_Computing_Foundation",
        ) + [
            "https://argo-cd.readthedocs.io/en/stable/",
            "https://argo-cd.readthedocs.io/en/stable/core_concepts/",
            "https://argo-cd.readthedocs.io/en/stable/getting_started/",
        ],
    },
    "flux-cd": {
        "tags": ["flux cd", "gitops toolkit", "continuous deployment", "kubernetes reconciliation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Continuous_deployment",
            "DevOps",
            "Cloud_Native_Computing_Foundation",
        ) + [
            "https://fluxcd.io/flux/",
            "https://fluxcd.io/flux/concepts/",
            "https://fluxcd.io/flux/get-started/",
        ],
    },
    "jenkins": {
        "tags": ["jenkins ci", "continuous integration", "build automation", "jenkins pipeline"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Jenkins_(software)",
            "Continuous_integration",
            "Build_automation",
        ) + [
            "https://www.jenkins.io/doc/",
            "https://www.jenkins.io/doc/book/pipeline/",
            "https://www.jenkins.io/doc/book/using/",
        ],
    },
    "gitlab-ci": {
        "tags": ["gitlab ci", "gitlab pipeline", "ci cd pipeline", "continuous integration"],
        "license": CC_BY_SA,
        "pages": wiki(
            "GitLab",
            "CI/CD",
            "Continuous_integration",
        ) + [
            "https://docs.gitlab.com/ee/ci/",
            "https://docs.gitlab.com/ee/ci/pipelines/",
            "https://docs.gitlab.com/ee/ci/yaml/",
            "https://docs.gitlab.com/ee/ci/quick_start/",
        ],
    },
    "circleci": {
        "tags": ["circleci pipeline", "continuous integration", "ci cd pipeline", "build automation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "CircleCI",
            "Continuous_integration",
            "Software_testing",
        ) + [
            "https://circleci.com/docs/",
            "https://circleci.com/docs/concepts/",
            "https://circleci.com/docs/configuration-reference/",
            "https://circleci.com/docs/getting-started/",
        ],
    },
    "travis-ci": {
        "tags": ["travis ci", "continuous integration", "hosted ci", "build pipeline"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Travis_CI",
            "Continuous_integration",
            "Version_control",
        ) + [
            "https://docs.travis-ci.com/",
            "https://docs.travis-ci.com/user/getting-started/",
            "https://docs.travis-ci.com/user/for-beginners/",
            "https://docs.travis-ci.com/user/languages/",
        ],
    },
    "drone-ci": {
        "tags": ["drone ci", "container native ci", "continuous integration", "ci pipeline"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Continuous_integration",
            "Build_automation",
            "Container_(virtualization)",
        ) + [
            "https://docs.drone.io/",
            "https://docs.drone.io/pipeline/overview/",
            "https://readme.drone.io/",
        ],
    },
    "bazel-build": {
        "tags": ["bazel build", "build system", "hermetic build", "incremental build"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Bazel_(software)",
            "Build_automation",
            "Incremental_build_model",
            "Make_(software)",
        ) + [
            "https://bazel.build/docs",
            "https://bazel.build/concepts/build-ref",
        ],
    },
    "buck-build": {
        "tags": ["buck build system", "build system", "incremental build", "monorepo build"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Buck_(software)",
            "Build_automation",
            "Incremental_build_model",
        ) + [
            "https://buck2.build/",
            "https://buck2.build/docs/",
            "https://buck2.build/docs/getting_started/",
            "https://buck2.build/docs/why/",
        ],
    },
    "nix-package-manager": {
        "tags": ["nix package manager", "reproducible builds", "functional package management", "declarative packaging"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Nix_(package_manager)",
            "Reproducible_builds",
            "Functional_programming",
        ) + [
            "https://nixos.org/manual/nix/stable/",
            "https://nix.dev/manual/nix/2.18/",
            "https://nixos.org/guides/nix-pills/",
        ],
    },
    "nixos": {
        "tags": ["nixos distribution", "declarative linux distribution", "reproducible system configuration", "immutable operating system"],
        "license": CC_BY_SA,
        "pages": wiki(
            "NixOS",
            "Linux_distribution",
            "Declarative_programming",
            "Reproducible_builds",
        ) + [
            "https://nixos.org/manual/nixos/stable/",
            "https://nixos.org/download/",
        ],
    },
    "guix": {
        "tags": ["gnu guix", "functional package management", "reproducible builds", "declarative system"],
        "license": CC_BY_SA,
        "pages": wiki(
            "GNU_Guix",
            "GNU",
            "Free_software",
            "Reproducible_builds",
        ) + [
            "https://guix.gnu.org/manual/en/html_node/",
            "https://guix.gnu.org/manual/en/html_node/Introduction.html",
        ],
    },
    "podman": {
        "tags": ["podman containers", "rootless containers", "container engine", "daemonless containers"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Podman",
            "Docker_(software)",
            "OS-level_virtualization",
        ) + [
            "https://docs.podman.io/en/latest/",
            "https://podman.io/docs",
            "https://docs.podman.io/en/latest/Introduction.html",
            "https://docs.podman.io/en/latest/Commands.html",
        ],
    },
    "containerd": {
        "tags": ["containerd runtime", "container runtime", "oci runtime", "container lifecycle"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Containerd",
            "Container_(virtualization)",
            "Open_Container_Initiative",
            "OS-level_virtualization",
        ) + [
            "https://containerd.io/docs/",
            "https://containerd.io/releases/",
            "https://containerd.io/scope/",
        ],
    },
    "cri-o": {
        "tags": ["cri-o runtime", "kubernetes container runtime", "oci runtime", "container runtime interface"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Container_(virtualization)",
            "Open_Container_Initiative",
            "Kubernetes",
        ) + [
            "https://cri-o.io/",
            "https://kubernetes.io/docs/concepts/architecture/cri/",
            "https://kubernetes.io/docs/setup/production-environment/container-runtimes/",
        ],
    },
    "buildah": {
        "tags": ["buildah image builder", "container image builder", "oci image", "dockerfile build"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Dockerfile",
            "Open_Container_Initiative",
            "Container_(virtualization)",
            "OS-level_virtualization",
        ) + [
            "https://buildah.io/",
            "https://buildah.io/blogs/",
        ],
    },
    "skaffold": {
        "tags": ["skaffold workflow", "kubernetes development workflow", "continuous development", "build deploy loop"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "Continuous_integration",
            "DevOps",
        ) + [
            "https://skaffold.dev/docs/",
            "https://skaffold.dev/docs/quickstart/",
            "https://skaffold.dev/docs/init/",
            "https://skaffold.dev/docs/pipeline-stages/",
        ],
    },
    "kustomize": {
        "tags": ["kustomize overlay", "kubernetes configuration management", "yaml overlay", "declarative configuration"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "YAML",
            "Configuration_management",
        ) + [
            "https://kustomize.io/",
            "https://kubectl.docs.kubernetes.io/references/kustomize/",
            "https://kubectl.docs.kubernetes.io/guides/config_management/introduction/",
            "https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/",
        ],
    },
    "rancher": {
        "tags": ["rancher kubernetes", "kubernetes management platform", "multi cluster management", "container orchestration"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Rancher_Labs",
            "SUSE",
            "Kubernetes",
            "Container_(virtualization)",
            "Orchestration_(computing)",
            "Cloud_Native_Computing_Foundation",
        ),
    },
    "openshift": {
        "tags": ["openshift platform", "kubernetes platform", "platform as a service", "enterprise kubernetes"],
        "license": CC_BY_SA,
        "pages": wiki(
            "OpenShift",
            "Red_Hat",
            "Kubernetes",
            "Platform_as_a_service",
            "Container_(virtualization)",
            "DevOps",
        ),
    },
    "hashicorp-nomad": {
        "tags": ["hashicorp nomad", "workload orchestration", "cluster scheduler", "container orchestration"],
        "license": CC_BY_SA,
        "pages": wiki(
            "HashiCorp",
            "Orchestration_(computing)",
            "Scheduling_(computing)",
            "Job_scheduler",
        ) + [
            "https://developer.hashicorp.com/nomad/docs",
            "https://developer.hashicorp.com/nomad/intro",
            "https://developer.hashicorp.com/nomad/docs/concepts",
        ],
    },
    "apache-mesos": {
        "tags": ["apache mesos", "cluster manager", "resource scheduling", "datacenter orchestration"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Mesos",
            "Cluster_manager",
            "Orchestration_(computing)",
            "Mesosphere",
            "Distributed_computing",
            "Apache_ZooKeeper",
        ),
    },
    "spinnaker": {
        "tags": ["spinnaker delivery", "continuous delivery platform", "multi cloud deployment", "deployment pipeline"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Spinnaker_(software)",
            "Continuous_delivery",
            "Software_deployment",
            "Netflix",
        ) + [
            "https://spinnaker.io/docs/",
            "https://spinnaker.io/docs/concepts/",
            "https://spinnaker.io/docs/reference/",
            "https://spinnaker.io/docs/setup/",
        ],
    },
    "tekton": {
        "tags": ["tekton pipelines", "cloud native ci", "kubernetes native pipeline", "continuous delivery"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Continuous_integration",
            "Continuous_delivery",
            "Kubernetes",
        ) + [
            "https://tekton.dev/docs/",
            "https://tekton.dev/docs/pipelines/",
            "https://tekton.dev/docs/concepts/",
            "https://tekton.dev/docs/getting-started/",
        ],
    },
    "cert-manager": {
        "tags": ["cert manager", "certificate automation", "public key infrastructure", "acme certificates"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Public_key_certificate",
            "Let%27s_Encrypt",
            "Automatic_Certificate_Management_Environment",
            "Public_key_infrastructure",
        ) + [
            "https://cert-manager.io/docs/",
            "https://cert-manager.io/docs/concepts/",
            "https://cert-manager.io/docs/installation/",
        ],
    },
    "fluentd": {
        "tags": ["fluentd logging", "log collection", "log management", "unified logging layer"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Fluentd",
            "Log_management",
            "Syslog",
            "Fluent_Bit",
        ) + [
            "https://www.fluentd.org/architecture",
            "https://docs.fluentd.org/",
        ],
    },
    "grafana-loki": {
        "tags": ["grafana loki", "log aggregation", "log management", "label based logs"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Grafana",
            "Log_management",
            "Elasticsearch",
        ) + [
            "https://grafana.com/docs/loki/latest/",
            "https://grafana.com/docs/loki/latest/get-started/",
            "https://grafana.com/oss/loki/",
        ],
    },
    "thanos-metrics": {
        "tags": ["thanos metrics", "prometheus long term storage", "highly available metrics", "global query view"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Prometheus_(software)",
            "Time_series_database",
            "Monitoring",
            "Observability_(software)",
        ) + [
            "https://grafana.com/docs/tempo/latest/",
            "https://grafana.com/oss/tempo/",
        ],
    },
    "chaos-engineering-tools": {
        "tags": ["chaos engineering", "fault injection", "resilience testing", "failure injection"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Chaos_engineering",
            "Fault_injection",
            "Resilience_(network)",
            "Reliability_engineering",
        ) + [
            "https://principlesofchaos.org/",
            "https://www.gremlin.com/community/tutorials/chaos-engineering-the-history-principles-and-practice",
        ],
    },
    "minikube": {
        "tags": ["minikube cluster", "local kubernetes cluster", "kubernetes development", "single node kubernetes"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "Container_(virtualization)",
            "Development_environment_(software_development_process)",
        ) + [
            "https://minikube.sigs.k8s.io/docs/",
            "https://minikube.sigs.k8s.io/docs/start/",
            "https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/",
        ],
    },
    "kubeadm": {
        "tags": ["kubeadm bootstrap", "kubernetes cluster bootstrap", "cluster provisioning", "control plane setup"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Kubernetes",
            "Provisioning_(technology)",
            "Orchestration_(computing)",
        ) + [
            "https://kubernetes.io/docs/reference/setup-tools/kubeadm/",
            "https://kubernetes.io/docs/tasks/tools/",
            "https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/",
        ],
    },
    "container-registry": {
        "tags": ["container registry", "container image registry", "oci image", "image distribution"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Docker_(software)",
            "Open_Container_Initiative",
            "Container_(virtualization)",
            "Software_repository",
        ) + [
            "https://kubernetes.io/docs/concepts/containers/images/",
            "https://distribution.github.io/distribution/",
            "https://distribution.github.io/distribution/about/",
            "https://distribution.github.io/distribution/spec/api/",
        ],
    },
    "gitops": {
        "tags": ["gitops workflow", "declarative infrastructure", "git driven operations", "continuous reconciliation"],
        "license": CC_BY_SA,
        "pages": wiki(
            "DevOps",
            "Infrastructure_as_code",
            "Continuous_delivery",
            "Version_control",
            "Control_plane",
            "Application_lifecycle_management",
        ),
    },
    "blue-green-deployment": {
        "tags": ["blue green deployment", "zero downtime deployment", "release strategy", "traffic switching"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Blue%E2%80%93green_deployment",
            "Software_deployment",
            "Continuous_deployment",
            "Deployment_environment",
            "Software_release_life_cycle",
            "Site_reliability_engineering",
        ),
    },
    "canary-deployment": {
        "tags": ["canary deployment", "progressive delivery", "incremental rollout", "release strategy"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Feature_toggle",
            "Software_deployment",
            "Continuous_deployment",
            "Software_release_life_cycle",
            "Rolling_release",
            "Deployment_environment",
        ),
    },
    "feature-flags": {
        "tags": ["feature flag", "feature toggle", "progressive delivery", "runtime configuration"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Feature_toggle",
            "Continuous_delivery",
            "A/B_testing",
            "Software_release_life_cycle",
            "Software_deployment",
            "Continuous_deployment",
        ),
    },
}
