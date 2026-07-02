"""Web frameworks/APIs, cloud/infra, graphics and game development."""

from .common import CC_BY_SA, CC_BY_SA_25, MIT, WIKI, mdn, wiki

DOMAINS = {
    "react-docs": {
        "tags": ["react", "jsx", "react hooks", "usestate", "useeffect"],
        "license": "CC-BY-4.0 (react.dev)",
        "pages": [
            "https://react.dev/learn",
            "https://react.dev/learn/describing-the-ui",
            "https://react.dev/learn/adding-interactivity",
            "https://react.dev/learn/managing-state",
            "https://react.dev/reference/react/useState",
            "https://react.dev/reference/react/useEffect",
        ],
    },
    "vue-docs": {
        "tags": ["vue", "vuejs", "vue 3", "composition api", "single file component"],
        "license": MIT,
        "pages": [
            "https://vuejs.org/guide/introduction.html",
            "https://vuejs.org/guide/essentials/reactivity-fundamentals.html",
            "https://vuejs.org/guide/essentials/component-basics.html",
            "https://vuejs.org/guide/components/props.html",
        ],
    },
    "svelte-docs": {
        "tags": ["svelte", "sveltekit", "svelte component", "svelte store"],
        "license": MIT,
        "pages": [
            "https://svelte.dev/docs/svelte/overview",
            "https://svelte.dev/docs/svelte/svelte-files",
            "https://svelte.dev/docs/svelte/basic-markup",
        ],
    },
    "web-accessibility": {
        "tags": ["accessibility", "a11y", "aria", "wcag", "screen reader"],
        "license": CC_BY_SA_25 + " / W3C-doc",
        "pages": [
            mdn("Web/Accessibility"),
            mdn("Web/Accessibility/ARIA"),
            "https://www.w3.org/WAI/fundamentals/accessibility-intro/",
            WIKI + "Web_accessibility",
        ],
    },
    "graphql": {
        "tags": ["graphql", "graphql schema", "graphql query", "graphql mutation", "graphql subscription"],
        "license": "OWFa-1.0 (spec) / MIT (graphql.org)",
        "pages": [
            "https://graphql.org/learn/queries/",
            "https://graphql.org/learn/schema/",
            "https://graphql.org/learn/mutations/",
            "https://graphql.org/learn/execution/",
            WIKI + "GraphQL",
        ],
    },
    "grpc": {
        "tags": ["grpc", "protocol buffers rpc"],
        "license": "CC-BY-4.0 (grpc.io)",
        "pages": [
            "https://grpc.io/docs/what-is-grpc/introduction/",
            "https://grpc.io/docs/what-is-grpc/core-concepts/",
            WIKI + "GRPC",
        ],
    },
    "rest-api-design": {
        "tags": ["api design", "restful", "http api", "api guideline", "hateoas"],
        "license": CC_BY_SA,
        "pages": wiki(
            "REST",
            "HATEOAS",
            "API",
            "Web_API",
            "Richardson_Maturity_Model",
            "Rate_limiting",
            "Webhook",
        ),
    },
    "cloud-computing": {
        "tags": ["cloud computing", "serverless", "virtualization", "hypervisor", "iaas", "paas"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cloud_computing",
            "Serverless_computing",
            "Infrastructure_as_a_service",
            "Platform_as_a_service",
            "Software_as_a_service",
            "Function_as_a_service",
            "Virtualization",
            "Hypervisor",
            "Virtual_machine",
            "Multitenancy",
            "Autoscaling",
        ),
    },
    "kubernetes": {
        "tags": ["kubernetes", "k8s", "kubectl", "pod", "helm"],
        "license": "CC-BY-4.0 (k8s docs)",
        "pages": [
            "https://kubernetes.io/docs/concepts/overview/",
            "https://kubernetes.io/docs/concepts/workloads/pods/",
            "https://kubernetes.io/docs/concepts/services-networking/service/",
            "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/",
            "https://kubernetes.io/docs/concepts/configuration/configmap/",
        ],
    },
    "github-actions": {
        "tags": ["github actions", "github workflow", "actions runner"],
        "license": "CC-BY-4.0 (GitHub docs)",
        "pages": [
            "https://docs.github.com/en/actions/get-started/understanding-github-actions",
            "https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax",
            WIKI + "GitHub",
        ],
    },
    "nginx": {
        "tags": ["nginx", "nginx reverse proxy", "nginx conf"],
        "license": "BSD-2-Clause / " + CC_BY_SA,
        "pages": [
            "https://nginx.org/en/docs/beginners_guide.html",
            "https://nginx.org/en/docs/http/request_processing.html",
            WIKI + "Nginx",
            WIKI + "Reverse_proxy",
        ],
    },
    "terraform": {
        "tags": ["terraform", "hcl", "infrastructure as code", "terraform provider"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Terraform_(software)",
            "OpenTofu",
        ),
    },
    "ansible": {
        "tags": ["ansible", "ansible playbook", "ansible galaxy"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Ansible_(software)",
            "Configuration_management",
        ),
    },
    "encodings-serialization": {
        "tags": ["unicode", "utf-8", "character encoding", "protobuf", "serialization", "endianness"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Unicode",
            "UTF-8",
            "Character_encoding",
            "ASCII",
            "Protocol_Buffers",
            "Serialization",
            "Endianness",
            "Percent-encoding",
            "Punycode",
        ),
    },
    "graphics": {
        "tags": ["computer graphics", "rasterization", "ray tracing", "shader", "graphics pipeline", "texture mapping"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Computer_graphics",
            "Rasterisation",
            "Ray_tracing_(graphics)",
            "Shader",
            "Graphics_pipeline",
            "Z-buffering",
            "Texture_mapping",
            "Phong_shading",
            "Global_illumination",
            "Spatial_anti-aliasing",
            "Color_space",
            "RGB_color_model",
        ),
    },
    "game-dev": {
        "tags": ["game development", "game engine", "entity component system", "collision detection", "pathfinding", "game physics"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Video_game_development",
            "Game_engine",
            "Entity_component_system",
            "Collision_detection",
            "Pathfinding",
            "Physics_engine",
            "Sprite_(computer_graphics)",
            "Procedural_generation",
            "Frame_rate",
            "Game_design",
        ),
    },
}
